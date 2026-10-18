# ObpReferenceObjectByHandleWithTag

- RVA: `0x00869650`–`0x00869DA6` (길이 `1,878` bytes)
- VA: `0x0000000140869650`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006BE9C`
- 디코드: `437`개 명령, `1,878/1,878` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **28**; 고유 호출 대상: **16**
- 직접 호출자로 확인된 함수: **108**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00869734` → [ExpLookupHandleTableEntry](ExpLookupHandleTableEntry_function_00869DB0.md) (function, `0x00869DB0`)
- `0x0086977F` → [ExpBlockOnLockedHandleEntry](ExpBlockOnLockedHandleEntry_function_00868838.md) (function, `0x00868838`)
- `0x008697CA` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (function, `0x00430C90`)
- `0x008697E2` → [ObpTraceObjectReferenceIfActive](../../text/21/ObpTraceObjectReferenceIfActive_function_00210780.md) (function, `0x00210780`)
- `0x0086984E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0086987E` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086992C` → [ObpTraceObjectReferenceIfActive](../../text/21/ObpTraceObjectReferenceIfActive_function_00210780.md) (function, `0x00210780`)
- `0x0086996D` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (function, `0x00430C90`)
- `0x00869980` → [ExSlowReplenishHandleTableEntry](../../text/44/ExSlowReplenishHandleTableEntry_function_0044BEF0.md) (function, `0x0044BEF0`)
- `0x008699AE` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (function, `0x002A3FE0`)
- `0x008699D1` → [ExpBlockOnLockedHandleEntry](ExpBlockOnLockedHandleEntry_function_00868838.md) (function, `0x00868838`)
- `0x00869A74` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x00869ADD` → [ObpTraceObjectReferenceIfActive](../../text/21/ObpTraceObjectReferenceIfActive_function_00210780.md) (function, `0x00210780`)
- `0x00869B42` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)
- `0x00869B4C` → [ExfAcquireRundownProtection](../../text/34/ExfAcquireRundownProtection_function_0034C050.md) (function, `0x0034C050`)
- `0x00869BEA` → [ExpGetHandleExtraInfo](ExpGetHandleExtraInfo_function_0086B454.md) (function, `0x0086B454`)
- `0x00869C18` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00869C2F` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00869C46` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00869C5A` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)
- `0x00869C64` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)
- `0x00869C96` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (function, `0x00430C90`)
- `0x00869CBF` → [ExFastReplenishHandleTableEntry](../../text/47/ExFastReplenishHandleTableEntry_function_0047E210.md) (function, `0x0047E210`)
- `0x00869CFD` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00869D0F` → [VfCheckUserHandle](../../pagevrfy/BB/VfCheckUserHandle_function_00BB9218.md) (function, `0x00BB9218`)
- `0x00869D31` → [ObpAuditObjectAccess](../94/ObpAuditObjectAccess_function_0094C270.md) (function, `0x0094C270`)
- `0x00869D7F` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00869D9C` → [ExHandleLogBadReference](../../text/44/ExHandleLogBadReference_function_00440580.md) (function, `0x00440580`)

### Direct callers
- [NtResumeProcess](../70/NtResumeProcess_function_007009C0.md) at `0x00700A03`
- [MmGetSectionStrongImageReference](../70/MmGetSectionStrongImageReference_function_00701DF0.md) at `0x00701E3B`
- [HalpAcquirePccInterface](../70/HalpAcquirePccInterface_function_0070D524.md) at `0x0070D5D4`
- [DbgkpCreateNotificationEvent](../71/DbgkpCreateNotificationEvent_function_00710480.md) at `0x0071071F`
- [PfSnAppLaunchScenarioControl](../75/PfSnAppLaunchScenarioControl_function_00752294.md) at `0x0075231C`
- [PfSnSetAltPrefetchParam](../75/PfSnSetAltPrefetchParam_function_00752424.md) at `0x007524E9`
- [PopCreateHiberFile](../75/PopCreateHiberFile_function_0075CE70.md) at `0x0075D10D`
- [PopGetPolicyDeviceObject](../76/PopGetPolicyDeviceObject_function_00765EB8.md) at `0x00765F71`
- [PspConvertSiloToServerSilo](../77/PspConvertSiloToServerSilo_function_0077F9B4.md) at `0x0077FA5F`
- [NtChangeProcessState](../78/NtChangeProcessState_function_00782C00.md) at `0x00782CA3`
- [NtChangeProcessState](../78/NtChangeProcessState_function_00782C00.md) at `0x00782CE9`
- [NtCreateProcessStateChange](../78/NtCreateProcessStateChange_function_007830C0.md) at `0x00783170`
- [PspReferenceCpuPartitionByHandle](../78/PspReferenceCpuPartitionByHandle_function_007846F4.md) at `0x007847FF`
- [PspAssignPrimaryToken](../78/PspAssignPrimaryToken_function_00784870.md) at `0x00784945`
- [PspCreatePicoProcess](../78/PspCreatePicoProcess_function_007873B0.md) at `0x00787446`
- [PspCreatePicoProcess](../78/PspCreatePicoProcess_function_007873B0.md) at `0x00787487`
- [PspCreatePicoProcess](../78/PspCreatePicoProcess_function_007873B0.md) at `0x00787552`
- [NtAlertResumeThread](../78/NtAlertResumeThread_function_00787920.md) at `0x0078799B`
- [PsIumEnableOnDemandDebugWithResponse](../78/PsIumEnableOnDemandDebugWithResponse_function_00787C30.md) at `0x00787C81`
- [ExpProfileCreate](../7D/ExpProfileCreate_function_007D1AB8.md) at `0x007D1DEE`
- [NtPssCaptureVaSpaceBulk](../7D/NtPssCaptureVaSpaceBulk_function_007D4EA0.md) at `0x007D5154`
- [MiCreatePagingFile](../7F/MiCreatePagingFile_function_007FEFF4.md) at `0x007FF5DD`
- [MiCreatePagingFile](../7F/MiCreatePagingFile_function_007FEFF4.md) at `0x007FF872`
- [MiInsertPageFileInList](../7F/MiInsertPageFileInList_function_007FFF80.md) at `0x00800194`
- [MiInjectThreadForHotPatch](../80/MiInjectThreadForHotPatch_function_00803FD8.md) at `0x008040F4`
- [NtCreateEnclave](../80/NtCreateEnclave_function_00808CC0.md) at `0x00808F81`
- [NtInitializeEnclave](../80/NtInitializeEnclave_function_008090B0.md) at `0x0080924D`
- [MmStoreRegister](../80/MmStoreRegister_function_0080E6D8.md) at `0x0080E92E`
- [MmScrubMemory](../80/MmScrubMemory_function_0080EFA0.md) at `0x0080F000`
- [MiCreateMemoryEvent](../81/MiCreateMemoryEvent_function_00810D98.md) at `0x00810E64`
- [VrpHandleIoctlCreateMultipleNamespaceNodes](../83/VrpHandleIoctlCreateMultipleNamespaceNodes_function_0083B17C.md) at `0x0083B1FA`
- [VrpHandleIoctlModifyFlags](../83/VrpHandleIoctlModifyFlags_function_0083B69C.md) at `0x0083B70F`
- [ObWaitForSingleObject](ObWaitForSingleObject_function_00868C50.md) at `0x00868C97`
- [ObReferenceObjectByHandle](ObReferenceObjectByHandle_function_00868DB0.md) at `0x00868DD9`
- [ObReferenceObjectByHandleWithTag](ObReferenceObjectByHandleWithTag_function_00869610.md) at `0x0086963C`
- [sub_0088018D](../88/Unknown_function_0088018D.md) at `0x008801D6`
- [NtProtectVirtualMemory](../88/NtProtectVirtualMemory_function_00880CA0.md) at `0x00880E26`
- [MiAllocateVirtualMemoryPrepare](../88/MiAllocateVirtualMemoryPrepare_function_00883220.md) at `0x00883442`
- [NtUnmapViewOfSection](../88/NtUnmapViewOfSection_function_0088A330.md) at `0x0088A38E`
- [sub_0088A40D](../88/Unknown_function_0088A40D.md) at `0x0088A460`
- [MiMapViewOfSectionCommon](../89/MiMapViewOfSectionCommon_function_00898C90.md) at `0x00898D3B`
- [MiMapViewOfSectionCommon](../89/MiMapViewOfSectionCommon_function_00898C90.md) at `0x00898D8E`
- [ObpLookupObjectName](../89/ObpLookupObjectName_function_0089BE90.md) at `0x0089C05B`
- [NtOpenProcessTokenEx](../8B/NtOpenProcessTokenEx_function_008B72D0.md) at `0x008B7381`
- [NtDuplicateObject](../8C/NtDuplicateObject_function_008C4DC0.md) at `0x008C4E61`
- [NtDuplicateObject](../8C/NtDuplicateObject_function_008C4DC0.md) at `0x008C4EA6`
- [NtGetNextThread](../8C/NtGetNextThread_function_008C7D40.md) at `0x008C7E4F`
- [NtGetNextThread](../8C/NtGetNextThread_function_008C7D40.md) at `0x008C7E8B`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CA1CA`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CA256`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CA348`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CA441`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CA55B`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CA5D6`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CA67B`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CA761`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CA7D3`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CAA56`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CAB1A`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CAB6C`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CAC41`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CAD5E`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CADDA`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CAE4C`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CAEEA`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CB16F`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CB297`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CB3B1`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CB427`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CB52F`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CB615`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CB686`
- [NtSetInformationThread](../8C/NtSetInformationThread_function_008C9F60.md) at `0x008CB730`
- [PsReferencePartitionByHandle](../90/PsReferencePartitionByHandle_function_0090337C.md) at `0x009033C6`
- [NtTerminateThread](../90/NtTerminateThread_function_00905DA0.md) at `0x00905E35`
- [NtQueryWnfStateData](../90/NtQueryWnfStateData_function_00909DF0.md) at `0x0090A074`
- [ExpNtUpdateWnfStateData](../90/ExpNtUpdateWnfStateData_function_0090A7A0.md) at `0x0090A968`
- [NtGetNextProcess](../91/NtGetNextProcess_function_0091DF50.md) at `0x0091E052`
- [NtQuerySection](../92/NtQuerySection_function_00921770.md) at `0x00921874`
- [VrpHandleIoctlCreateNamespaceNode](../93/VrpHandleIoctlCreateNamespaceNode_function_0093511C.md) at `0x009351EE`
- [VrpHandleIoctlGetVirtualRootKey](../93/VrpHandleIoctlGetVirtualRootKey_function_00935374.md) at `0x009353F4`
- [VrpHandleIoctlLoadDifferencingHive](../93/VrpHandleIoctlLoadDifferencingHive_function_00935C5C.md) at `0x00935DBA`
- [VrpHandleIoctlInitializeJobForVreg](../93/VrpHandleIoctlInitializeJobForVreg_function_00937254.md) at `0x009373CB`
- [VrpHandleIoctlUnloadDynamicallyLoadedHives](../93/VrpHandleIoctlUnloadDynamicallyLoadedHives_function_0093778C.md) at `0x0093781B`
- [MmPrefetchVirtualMemory](../93/MmPrefetchVirtualMemory_function_0093A698.md) at `0x0093A7B4`
- [sub_009848DC](../98/Unknown_function_009848DC.md) at `0x0098493F`
- [PopEtEnergyTrackerQuery](../98/PopEtEnergyTrackerQuery_function_0098B668.md) at `0x0098B71F`
- [NtCreateWorkerFactory](../9A/NtCreateWorkerFactory_function_009A7E10.md) at `0x009A7F23`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AA460`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AA5B4`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AAF3D`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AAFC6`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AB0A0`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AB151`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AB1DD`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AB25F`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AB460`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AB539`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AB5E0`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AB6A3`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AB7D7`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AB8B5`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ABAE2`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ABB59`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ABBF6`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ABD13`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ABE55`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ABF4D`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AC045`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AC12F`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AC19D`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AC270`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AC3D8`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AC47E`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AC560`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AC6CB`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AC743`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AC7F9`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AC8C4`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ACA6D`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ACB0B`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ACC18`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ACE49`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ACED6`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ACF43`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ACFE5`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AD065`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AD363`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AD3B3`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AD4BE`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AD54F`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AD80D`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AD84C`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AD910`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ADA39`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ADB25`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ADBCF`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ADC72`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ADD1D`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ADDC9`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ADE66`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ADF07`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009ADF85`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AE01C`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AE086`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AE111`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AE1DF`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AE22F`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AE29B`
- [NtQueryInformationProcess](../9A/NtQueryInformationProcess_function_009AA250.md) at `0x009AE31F`
- [PspSetQuotaLimits](../9B/PspSetQuotaLimits_function_009BA8A8.md) at `0x009BAA90`
- [MiReadWriteVirtualMemory](../9B/MiReadWriteVirtualMemory_function_009BB4E0.md) at `0x009BB63B`
- [PspQueryQuotaLimits](../9D/PspQueryQuotaLimits_function_009D6280.md) at `0x009D6325`
- [NtFlushVirtualMemory](../9D/NtFlushVirtualMemory_function_009D6DB0.md) at `0x009D6EB1`
- [MmQueryVirtualMemory](../9D/MmQueryVirtualMemory_function_009D9280.md) at `0x009D9608`
- [MiLockUnlockCommon](../9E/MiLockUnlockCommon_function_009EA5D0.md) at `0x009EA6B6`
- [ExpWnfCaptureScopeInstanceId](../9E/ExpWnfCaptureScopeInstanceId_function_009EC110.md) at `0x009EC188`
- [PsCreateSystemThreadEx](../9E/PsCreateSystemThreadEx_function_009ED120.md) at `0x009ED2C4`
- [NtCreateThreadEx](../9E/NtCreateThreadEx_function_009ED3D0.md) at `0x009ED4F7`
- [PspBuildCreateProcessContext](../9E/PspBuildCreateProcessContext_function_009ED6E0.md) at `0x009EE0C8`
- [PspCreateThread](../9E/PspCreateThread_function_009EF034.md) at `0x009EF136`
- [PspCreatePicoThread](../9F/PspCreatePicoThread_function_009F0D70.md) at `0x009F0E40`
- [NtSetInformationVirtualMemory](../9F/NtSetInformationVirtualMemory_function_009F4580.md) at `0x009F4B22`
- [NtSetInformationVirtualMemory](../9F/NtSetInformationVirtualMemory_function_009F4580.md) at `0x009F4BFF`
- [NtSetInformationJobObject](../9F/NtSetInformationJobObject_function_009F84C0.md) at `0x009F8776`
- [NtSetInformationJobObject](../9F/NtSetInformationJobObject_function_009F84C0.md) at `0x009F8914`
- [NtQueryInformationJobObject](../9F/NtQueryInformationJobObject_function_009FB860.md) at `0x009FBC3F`
- [NtRemoveProcessDebug](../A0/NtRemoveProcessDebug_function_00A0FAF0.md) at `0x00A0FB57`
- [NtDebugActiveProcess](../A0/NtDebugActiveProcess_function_00A0FC60.md) at `0x00A0FCCF`
- [NtSuspendProcess](../A1/NtSuspendProcess_function_00A10850.md) at `0x00A10893`
- [NtSuspendThread](../A1/NtSuspendThread_function_00A11000.md) at `0x00A11081`
- [PspCreateProcess](../A1/PspCreateProcess_function_00A12758.md) at `0x00A129F7`
- [NtResumeThread](../A2/NtResumeThread_function_00A20D90.md) at `0x00A20E0D`
- [PspQueryWorkingSetWatch](../A2/PspQueryWorkingSetWatch_function_00A21478.md) at `0x00A21511`
- [PopPowerRequestActionInfo](../A2/PopPowerRequestActionInfo_function_00A21968.md) at `0x00A219BC`
- [PopPowerRequestSpecialRequestSet](../A2/PopPowerRequestSpecialRequestSet_function_00A21B4C.md) at `0x00A21BC9`
- [NtAssignProcessToJobObject](../A2/NtAssignProcessToJobObject_function_00A22FC0.md) at `0x00A2304C`
- [NtIsProcessInJob](../A2/NtIsProcessInJob_function_00A23940.md) at `0x00A239A2`
- [MmProcessWorkingSetControl](../A6/MmProcessWorkingSetControl_function_00A616C4.md) at `0x00A617A7`
- [MiResolveMemoryEvent](../A7/MiResolveMemoryEvent_function_00A70A70.md) at `0x00A70AD6`
- [NtCreateThreadStateChange](../A7/NtCreateThreadStateChange_function_00A77110.md) at `0x00A771BA`
- [NtAlertThread](../A8/NtAlertThread_function_00A89FB0.md) at `0x00A89FF5`
- [NtExtendSection](../A8/NtExtendSection_function_00A8EC60.md) at `0x00A8ECC7`
- [NtAcquireProcessActivityReference](../A8/NtAcquireProcessActivityReference_function_00A8EFF0.md) at `0x00A8F076`
- [DbgkpWerInitializeDeferredLiveDump](../AB/DbgkpWerInitializeDeferredLiveDump_function_00AB1088.md) at `0x00AB1135`
- [MiMapImageForEnclaveUse](../AB/MiMapImageForEnclaveUse_function_00AB213C.md) at `0x00AB21B0`
- [MiCombineIdenticalPages](../AB/MiCombineIdenticalPages_function_00AB2324.md) at `0x00AB2432`
- [MiCombineIdenticalPages](../AB/MiCombineIdenticalPages_function_00AB2324.md) at `0x00AB2478`
- [MiLoadHotPatch](../AB/MiLoadHotPatch_function_00AB521C.md) at `0x00AB5420`
- [MiQueryProcessActivePatches](../AC/MiQueryProcessActivePatches_function_00AC6164.md) at `0x00AC6313`
- [PsIumGetOnDemandDebugChallenge](../AC/PsIumGetOnDemandDebugChallenge_function_00ACA8B4.md) at `0x00ACA90C`
- [PspQueryPooledQuotaLimits](../AC/PspQueryPooledQuotaLimits_function_00ACB678.md) at `0x00ACB6F8`
- [MiForceCrashForInvalidAccess](../AC/MiForceCrashForInvalidAccess_function_00ACEFA4.md) at `0x00ACF16F`
- [PfpSourceGetPrefetchSupport](../AC/PfpSourceGetPrefetchSupport_function_00ACF6C0.md) at `0x00ACF78D`
- [PfpDeprioritizeOldPagesInWs](../AD/PfpDeprioritizeOldPagesInWs_function_00ADF310.md) at `0x00ADF3FE`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE3960`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE3AEE`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE3B60`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE3C3E`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE3CDE`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE3D40`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE3DAC`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE3E4C`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE3EC1`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE3F39`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE3FB0`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE4028`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE4093`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE40F1`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE4198`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE424B`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE4315`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE4565`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE45FE`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE467D`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE4707`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE477F`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE481E`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE48E8`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE4993`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE4AFF`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE4B8E`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE4C03`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE4D2A`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE4E29`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE4EEB`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE500B`
- [NtQueryInformationThread](../AE/NtQueryInformationThread_function_00AE3760.md) at `0x00AE510F`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE5709`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE5812`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE58C5`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE598F`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE5B09`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE5C85`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE5DB7`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE5E75`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE5F9F`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE618A`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE61EE`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE623C`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE62A5`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE630A`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE640D`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE64DE`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE666A`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE66E0`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE6791`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE682D`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE68C4`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE6976`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE6A44`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE6BED`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE7409`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE78CA`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE7947`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE7D51`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE8A97`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE8BFB`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE8C96`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE8D9E`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE8E17`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE8F71`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE8FFC`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE90FA`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE9167`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE9208`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE92EA`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE93E5`
- [NtSetInformationProcess](../AE/NtSetInformationProcess_function_00AE5370.md) at `0x00AE94D6`
- [NtChangeThreadState](../AE/NtChangeThreadState_function_00AEA210.md) at `0x00AEA31F`
- [NtChangeThreadState](../AE/NtChangeThreadState_function_00AEA210.md) at `0x00AEA36A`
- [NtCreateUserProcess](../AE/NtCreateUserProcess_function_00AEA680.md) at `0x00AEA9D8`
- [NtTerminateProcess](../AE/NtTerminateProcess_function_00AEC320.md) at `0x00AEC388`
- [NtLoadEnclaveData](../AF/NtLoadEnclaveData_function_00AF8DF0.md) at `0x00AF90A4`
- [sub_00B1B2E4](../B1/Unknown_function_00B1B2E4.md) at `0x00B1B36B`
- [sub_00B1B2E4](../B1/Unknown_function_00B1B2E4.md) at `0x00B1B431`
- [sub_00B1B2E4](../B1/Unknown_function_00B1B2E4.md) at `0x00B1B53C`
- [sub_00B1B2E4](../B1/Unknown_function_00B1B2E4.md) at `0x00B1B632`
- [sub_00B1B2E4](../B1/Unknown_function_00B1B2E4.md) at `0x00B1B785`
- [sub_00B3B77E](../B3/Unknown_function_00B3B77E.md) at `0x00B3B7AF`

### Static image references
- `0x008696CC` → RVA `0x00F04A20` (`.data`; read)
- `0x00869715` → RVA `0x00F0F5B8` (`.data`; read)
- `0x008697EF` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00869800` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x00869828` → RVA `0x00FC6C08` (`ALMOSTRO`; read)
- `0x008698E1` → RVA `0x00FC6A98` (`ALMOSTRO`; read)
- `0x00869A99` → RVA `0x00FC6AC8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **23**
  - `0x008697CA` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (`PAGE` → `.text`)
  - `0x008697E2` → [ObpTraceObjectReferenceIfActive](../../text/21/ObpTraceObjectReferenceIfActive_function_00210780.md) (`PAGE` → `.text`)
  - `0x0086984E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0086987E` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086992C` → [ObpTraceObjectReferenceIfActive](../../text/21/ObpTraceObjectReferenceIfActive_function_00210780.md) (`PAGE` → `.text`)
  - `0x0086996D` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (`PAGE` → `.text`)
  - `0x00869980` → [ExSlowReplenishHandleTableEntry](../../text/44/ExSlowReplenishHandleTableEntry_function_0044BEF0.md) (`PAGE` → `.text`)
  - `0x008699AE` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (`PAGE` → `.text`)
  - `0x00869A74` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x00869ADD` → [ObpTraceObjectReferenceIfActive](../../text/21/ObpTraceObjectReferenceIfActive_function_00210780.md) (`PAGE` → `.text`)
  - `0x00869B42` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (`PAGE` → `.text`)
  - `0x00869B4C` → [ExfAcquireRundownProtection](../../text/34/ExfAcquireRundownProtection_function_0034C050.md) (`PAGE` → `.text`)
  - `0x00869C18` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00869C2F` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00869C46` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00869C5A` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (`PAGE` → `.text`)
  - `0x00869C64` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (`PAGE` → `.text`)
  - `0x00869C96` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (`PAGE` → `.text`)
  - `0x00869CBF` → [ExFastReplenishHandleTableEntry](../../text/47/ExFastReplenishHandleTableEntry_function_0047E210.md) (`PAGE` → `.text`)
  - `0x00869CFD` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00869D0F` → [VfCheckUserHandle](../../pagevrfy/BB/VfCheckUserHandle_function_00BB9218.md) (`PAGE` → `PAGEVRFY`)
  - `0x00869D7F` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00869D9C` → [ExHandleLogBadReference](../../text/44/ExHandleLogBadReference_function_00440580.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00869650  44 88 4C 24 20                  mov byte ptr [rsp + 0x20], r9b
00869655  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
0086965A  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
0086965E  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
00869663  53                              push rbx
00869664  55                              push rbp
00869665  56                              push rsi
00869666  41 54                           push r12
00869668  41 57                           push r15
0086966A  48 81 EC 80 00 00 00            sub rsp, 0x80
00869671  65 4C 8B 3C 25 88 01 00 00      mov r15, qword ptr gs:[0x188]
0086967A  33 ED                           xor ebp, ebp
0086967C  48 8B B4 24 D8 00 00 00         mov rsi, qword ptr [rsp + 0xd8]
00869684  48 8B D9                        mov rbx, rcx
00869687  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
0086968F  40 88 6C 24 30                  mov byte ptr [rsp + 0x30], bpl
00869694  4D 8B A7 B8 00 00 00            mov r12, qword ptr [r15 + 0xb8]
0086969B  48 89 2E                        mov qword ptr [rsi], rbp
0086969E  48 85 C0                        test rax, rax
008696A1  74 05                           je 0x1408696a8
008696A3  33 C9                           xor ecx, ecx
008696A5  48 89 08                        mov qword ptr [rax], rcx
008696A8  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
008696AD  48 8B C3                        mov rax, rbx
008696B0  48 25 00 00 00 80               and rax, 0xffffffff80000000
008696B6  4C 89 6C 24 70                  mov qword ptr [rsp + 0x70], r13
008696BB  4C 89 74 24 68                  mov qword ptr [rsp + 0x68], r14
008696C0  48 3D 00 00 00 80               cmp rax, -0x80000000
008696C6  0F 84 D8 01 00 00               je 0x1408698a4
008696CC  F7 05 4A B3 69 00 00 01 00 00   test dword ptr [rip + 0x69b34a], 0x100
008696D6  0F 85 27 06 00 00               jne 0x140869d03
008696DC  66 41 FF 8F E4 01 00 00         dec word ptr [r15 + 0x1e4]
008696E4  90                              nop
008696E5  4D 3B A7 20 02 00 00            cmp r12, qword ptr [r15 + 0x220]
008696EC  0F 85 0B 04 00 00               jne 0x140869afd
008696F2  41 8B 84 24 F4 01 00 00         mov eax, dword ptr [r12 + 0x1f4]
008696FA  0F BA E0 1A                     bt eax, 0x1a
008696FE  0F 83 CB 04 00 00               jae 0x140869bcf
00869704  4D 8B AC 24 00 03 00 00         mov r13, qword ptr [r12 + 0x300]
0086970C  4D 85 ED                        test r13, r13
0086970F  0F 84 BA 04 00 00               je 0x140869bcf
00869715  4C 3B 2D 9C 5E 6A 00            cmp r13, qword ptr [rip + 0x6a5e9c]
0086971C  0F 84 A3 04 00 00               je 0x140869bc5
00869722  F7 C3 FC 03 00 00               test ebx, 0x3fc
00869728  0F 84 8E 04 00 00               je 0x140869bbc
0086972E  48 8B D3                        mov rdx, rbx
00869731  49 8B CD                        mov rcx, r13
00869734  E8 77 06 00 00                  call 0x140869db0
00869739  48 8B F8                        mov rdi, rax
0086973C  48 85 C0                        test rax, rax
0086973F  0F 84 77 04 00 00               je 0x140869bbc
00869745  0F 0D 08                        prefetchw byte ptr [rax]
00869748  48 8B 00                        mov rax, qword ptr [rax]
0086974B  4C 8B 77 08                     mov r14, qword ptr [rdi + 8]
0086974F  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00869754  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00869759  4C 89 74 24 50                  mov qword ptr [rsp + 0x50], r14
0086975E  90                              nop
0086975F  48 F7 C6 FE FF 01 00            test rsi, 0x1fffe
00869766  0F 84 E4 01 00 00               je 0x140869950
0086976C  40 0F B6 C6                     movzx eax, sil
00869770  F6 D0                           not al
00869772  A8 01                           test al, 1
00869774  74 16                           je 0x14086978c
00869776  4C 8B C6                        mov r8, rsi
00869779  48 8B D7                        mov rdx, rdi
0086977C  49 8B CD                        mov rcx, r13
0086977F  E8 B4 F0 FF FF                  call 0x140868838
00869784  0F 0D 0F                        prefetchw byte ptr [rdi]
00869787  48 8B 07                        mov rax, qword ptr [rdi]
0086978A  EB BF                           jmp 0x14086974b
0086978C  48 8D 5E FE                     lea rbx, [rsi - 2]
00869790  49 8B CE                        mov rcx, r14
00869793  48 8B C6                        mov rax, rsi
00869796  49 8B D6                        mov rdx, r14
00869799  F0 48 0F C7 0F                  lock cmpxchg16b xmmword ptr [rdi]
0086979E  48 8B F0                        mov rsi, rax
008697A1  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008697A6  0F 94 C0                        sete al
008697A9  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
008697AE  4C 8B F2                        mov r14, rdx
008697B1  84 C0                           test al, al
008697B3  74 A9                           je 0x14086975e
008697B5  48 8B CE                        mov rcx, rsi
008697B8  48 D1 E9                        shr rcx, 1
008697BB  66 83 F9 10                     cmp cx, 0x10
008697BF  0F 84 B3 04 00 00               je 0x140869c78
008697C5  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
008697CA  E8 C1 74 BC FF                  call 0x140430c90
008697CF  48 8B D8                        mov rbx, rax
008697D2  44 8B 84 24 D0 00 00 00         mov r8d, dword ptr [rsp + 0xd0]
008697DA  BA 01 00 00 00                  mov edx, 1
008697DF  48 8B CB                        mov rcx, rbx
008697E2  E8 99 6F 9A FF                  call 0x140210780
008697E7  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
008697EF  48 8D 15 0A 68 79 FF            lea rdx, [rip - 0x8697f6]
008697F6  48 8B C3                        mov rax, rbx
008697F9  48 C1 E8 08                     shr rax, 8
008697FD  32 43 18                        xor al, byte ptr [rbx + 0x18]
00869800  32 05 46 D6 75 00               xor al, byte ptr [rip + 0x75d646]
00869806  48 85 C9                        test rcx, rcx
00869809  74 09                           je 0x140869814
0086980B  38 41 28                        cmp byte ptr [rcx + 0x28], al
0086980E  0F 84 C7 01 00 00               je 0x1408699db
00869814  0F B6 C0                        movzx eax, al
00869817  4C 8B 84 C2 00 78 FC 00         mov r8, qword ptr [rdx + rax*8 + 0xfc7800]
0086981F  4D 85 C0                        test r8, r8
00869822  0F 84 C5 04 00 00               je 0x140869ced
00869828  4C 3B 05 D9 D3 75 00            cmp r8, qword ptr [rip + 0x75d3d9]
0086982F  0F 84 B8 04 00 00               je 0x140869ced
00869835  48 85 C9                        test rcx, rcx
00869838  0F 84 9D 01 00 00               je 0x1408699db
0086983E  BD 24 00 00 C0                  mov ebp, 0xc0000024
00869843  8B 94 24 D0 00 00 00            mov edx, dword ptr [rsp + 0xd0]
0086984A  48 8D 4B 30                     lea rcx, [rbx + 0x30]
0086984E  E8 8D E0 A8 FF                  call 0x1402f78e0
00869853  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
00869858  74 21                           je 0x14086987b
0086985A  49 8D 8C 24 E8 01 00 00         lea rcx, [r12 + 0x1e8]
00869862  0F 0D 09                        prefetchw byte ptr [rcx]
00869865  48 8B 01                        mov rax, qword ptr [rcx]
00869868  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0086986C  48 8D 50 FE                     lea rdx, [rax - 2]
00869870  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
00869875  0F 85 DF 03 00 00               jne 0x140869c5a
0086987B  49 8B CF                        mov rcx, r15
0086987E  E8 6D 57 9F FF                  call 0x14025eff0
00869883  8B C5                           mov eax, ebp
00869885  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
0086988A  4C 8B 6C 24 70                  mov r13, qword ptr [rsp + 0x70]
0086988F  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
00869894  48 81 C4 80 00 00 00            add rsp, 0x80
0086989B  41 5F                           pop r15
0086989D  41 5C                           pop r12
0086989F  5E                              pop rsi
008698A0  5D                              pop rbp
008698A1  5B                              pop rbx
008698A2  C3                              ret
008698A3  CC                              int3
008698A4  48 83 FB FF                     cmp rbx, -1
008698A8  74 37                           je 0x1408698e1
008698AA  48 83 FB FE                     cmp rbx, -2
008698AE  0F 84 E5 01 00 00               je 0x140869a99
008698B4  45 84 C9                        test r9b, r9b
008698B7  0F 85 B1 03 00 00               jne 0x140869c6e
008698BD  4C 8B 2D F4 5C 6A 00            mov r13, qword ptr [rip + 0x6a5cf4]
008698C4  48 81 F3 00 00 00 80            xor rbx, 0xffffffff80000000
008698CB  66 41 FF 8F E4 01 00 00         dec word ptr [r15 + 0x1e4]
008698D3  90                              nop
008698D4  48 89 9C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rbx
008698DC  E9 41 FE FF FF                  jmp 0x140869722
008698E1  4C 3B 05 B0 D1 75 00            cmp r8, qword ptr [rip + 0x75d1b0]
008698E8  0F 85 98 01 00 00               jne 0x140869a86
008698EE  49 8B BF B8 00 00 00            mov rdi, qword ptr [r15 + 0xb8]
008698F5  F7 C2 00 00 E0 FF               test edx, 0xffe00000
008698FB  0F 85 47 04 00 00               jne 0x140869d48
00869901  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00869909  48 85 C0                        test rax, rax
0086990C  74 09                           je 0x140869917
0086990E  C7 40 04 FF FF 1F 00            mov dword ptr [rax + 4], 0x1fffff
00869915  89 28                           mov dword ptr [rax], ebp
00869917  44 8B 84 24 D0 00 00 00         mov r8d, dword ptr [rsp + 0xd0]
0086991F  48 8D 4F D0                     lea rcx, [rdi - 0x30]
00869923  41 BC 01 00 00 00               mov r12d, 1
00869929  41 8B D4                        mov edx, r12d
0086992C  E8 4F 6E 9A FF                  call 0x140210780
00869931  F0 4C 0F C1 67 D0               lock xadd qword ptr [rdi - 0x30], r12
00869937  49 FF C4                        inc r12
0086993A  49 83 FC 01                     cmp r12, 1
0086993E  0F 8E DA 02 00 00               jle 0x140869c1e
00869944  48 89 3E                        mov qword ptr [rsi], rdi
00869947  E9 37 FF FF FF                  jmp 0x140869883
0086994C  0F 1F 40 00                     nop dword ptr [rax]
00869950  0F 0D 0F                        prefetchw byte ptr [rdi]
00869953  4C 8B 07                        mov r8, qword ptr [rdi]
00869956  41 F6 C0 01                     test r8b, 1
0086995A  74 66                           je 0x1408699c2
0086995C  49 8D 48 FF                     lea rcx, [r8 - 1]
00869960  49 8B C0                        mov rax, r8
00869963  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
00869968  75 E6                           jne 0x140869950
0086996A  48 8B CF                        mov rcx, rdi
0086996D  E8 1E 73 BC FF                  call 0x140430c90
00869972  0F 10 07                        movups xmm0, xmmword ptr [rdi]
00869975  48 8B CF                        mov rcx, rdi
00869978  48 8B D8                        mov rbx, rax
0086997B  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
00869980  E8 6B 25 BE FF                  call 0x14044bef0
00869985  FF C0                           inc eax
00869987  48 63 C8                        movsxd rcx, eax
0086998A  48 8B C1                        mov rax, rcx
0086998D  F0 48 0F C1 03                  lock xadd qword ptr [rbx], rax
00869992  48 85 C0                        test rax, rax
00869995  0F 8E 68 02 00 00               jle 0x140869c03
0086999B  F0 48 FF 07                     lock inc qword ptr [rdi]
0086999F  49 8D 4D 30                     lea rcx, [r13 + 0x30]
008699A3  F0 09 2C 24                     lock or dword ptr [rsp], ebp
008699A7  48 39 29                        cmp qword ptr [rcx], rbp
008699AA  74 07                           je 0x1408699b3
008699AC  33 D2                           xor edx, edx
008699AE  E8 2D A6 A3 FF                  call 0x1402a3fe0
008699B3  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
008699B8  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
008699BD  E9 10 FE FF FF                  jmp 0x1408697d2
008699C2  4D 85 C0                        test r8, r8
008699C5  0F 84 E9 01 00 00               je 0x140869bb4
008699CB  48 8B D7                        mov rdx, rdi
008699CE  49 8B CD                        mov rcx, r13
008699D1  E8 62 EE FF FF                  call 0x140868838
008699D6  E9 75 FF FF FF                  jmp 0x140869950
008699DB  41 81 E6 FF FF FF 01            and r14d, 0x1ffffff
008699E2  40 38 AC 24 C8 00 00 00         cmp byte ptr [rsp + 0xc8], bpl
008699EA  8B AC 24 B8 00 00 00            mov ebp, dword ptr [rsp + 0xb8]
008699F1  0F 85 68 01 00 00               jne 0x140869b5f
008699F7  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
008699FF  48 C1 FE 11                     sar rsi, 0x11
00869A03  48 85 C0                        test rax, rax
00869A06  74 78                           je 0x140869a80
00869A08  83 E6 07                        and esi, 7
00869A0B  44 89 70 04                     mov dword ptr [rax + 4], r14d
00869A0F  89 30                           mov dword ptr [rax], esi
00869A11  C1 EE 02                        shr esi, 2
00869A14  4C 8B 9C 24 E8 00 00 00         mov r11, qword ptr [rsp + 0xe8]
00869A1C  40 80 E6 01                     and sil, 1
00869A20  4C 8B 94 24 B0 00 00 00         mov r10, qword ptr [rsp + 0xb0]
00869A28  4D 85 DB                        test r11, r11
00869A2B  0F 85 A8 01 00 00               jne 0x140869bd9
00869A31  40 84 F6                        test sil, sil
00869A34  0F 85 DF 02 00 00               jne 0x140869d19
00869A3A  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
00869A3F  48 8D 43 30                     lea rax, [rbx + 0x30]
00869A43  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
00869A4B  48 89 01                        mov qword ptr [rcx], rax
00869A4E  74 21                           je 0x140869a71
00869A50  49 8D 8C 24 E8 01 00 00         lea rcx, [r12 + 0x1e8]
00869A58  0F 0D 09                        prefetchw byte ptr [rcx]
00869A5B  48 8B 01                        mov rax, qword ptr [rcx]
00869A5E  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00869A62  48 8D 50 FE                     lea rdx, [rax - 2]
00869A66  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
00869A6B  0F 85 F3 01 00 00               jne 0x140869c64
00869A71  49 8B CF                        mov rcx, r15
00869A74  E8 77 55 9F FF                  call 0x14025eff0
00869A79  33 C0                           xor eax, eax
00869A7B  E9 05 FE FF FF                  jmp 0x140869885
00869A80  40 C0 EE 02                     shr sil, 2
00869A84  EB 8E                           jmp 0x140869a14
00869A86  4D 85 C0                        test r8, r8
00869A89  0F 84 5F FE FF FF               je 0x1408698ee
00869A8F  BD 24 00 00 C0                  mov ebp, 0xc0000024
00869A94  E9 EA FD FF FF                  jmp 0x140869883
00869A99  4C 3B 05 28 D0 75 00            cmp r8, qword ptr [rip + 0x75d028]
00869AA0  0F 85 A6 01 00 00               jne 0x140869c4c
00869AA6  F7 C2 00 00 E0 FF               test edx, 0xffe00000
00869AAC  0F 85 A9 02 00 00               jne 0x140869d5b
00869AB2  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00869ABA  48 85 C0                        test rax, rax
00869ABD  74 09                           je 0x140869ac8
00869ABF  C7 40 04 FF FF 1F 00            mov dword ptr [rax + 4], 0x1fffff
00869AC6  89 28                           mov dword ptr [rax], ebp
00869AC8  44 8B 84 24 D0 00 00 00         mov r8d, dword ptr [rsp + 0xd0]
00869AD0  49 8D 4F D0                     lea rcx, [r15 - 0x30]
00869AD4  41 BC 01 00 00 00               mov r12d, 1
00869ADA  41 8B D4                        mov edx, r12d
00869ADD  E8 9E 6C 9A FF                  call 0x140210780
00869AE2  F0 4D 0F C1 67 D0               lock xadd qword ptr [r15 - 0x30], r12
00869AE8  49 FF C4                        inc r12
00869AEB  49 83 FC 01                     cmp r12, 1
00869AEF  0F 8E 40 01 00 00               jle 0x140869c35
00869AF5  4C 89 3E                        mov qword ptr [rsi], r15
00869AF8  E9 86 FD FF FF                  jmp 0x140869883
00869AFD  4C 8B ED                        mov r13, rbp
00869B00  49 8D BC 24 E8 01 00 00         lea rdi, [r12 + 0x1e8]
00869B08  0F 0D 0F                        prefetchw byte ptr [rdi]
00869B0B  48 8B 07                        mov rax, qword ptr [rdi]
00869B0E  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00869B12  48 8D 48 02                     lea rcx, [rax + 2]
00869B16  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
00869B1B  75 2C                           jne 0x140869b49
00869B1D  4D 8B AC 24 00 03 00 00         mov r13, qword ptr [r12 + 0x300]
00869B25  4D 85 ED                        test r13, r13
00869B28  75 2B                           jne 0x140869b55
00869B2A  0F 0D 0F                        prefetchw byte ptr [rdi]
00869B2D  48 8B 07                        mov rax, qword ptr [rdi]
00869B30  48 83 E0 FE                     and rax, 0xfffffffffffffffe
00869B34  48 8D 50 FE                     lea rdx, [rax - 2]
00869B38  F0 48 0F B1 17                  lock cmpxchg qword ptr [rdi], rdx
00869B3D  74 16                           je 0x140869b55
00869B3F  48 8B CF                        mov rcx, rdi
00869B42  E8 69 03 AE FF                  call 0x140349eb0
00869B47  EB 0C                           jmp 0x140869b55
00869B49  48 8B CF                        mov rcx, rdi
00869B4C  E8 FF 24 AE FF                  call 0x14034c050
00869B51  84 C0                           test al, al
00869B53  75 C8                           jne 0x140869b1d
00869B55  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
00869B5A  E9 AD FB FF FF                  jmp 0x14086970c
00869B5F  41 8B C6                        mov eax, r14d
00869B62  F7 D0                           not eax
00869B64  85 C5                           test ebp, eax
00869B66  0F 85 77 01 00 00               jne 0x140869ce3
00869B6C  0F B6 43 1A                     movzx eax, byte ptr [rbx + 0x1a]
00869B70  A8 40                           test al, 0x40
00869B72  0F 84 7F FE FF FF               je 0x1408699f7
00869B78  83 E0 7F                        and eax, 0x7f
00869B7B  48 8B CB                        mov rcx, rbx
00869B7E  0F B6 84 10 80 FF F0 00         movzx eax, byte ptr [rax + rdx + 0xf0ff80]
00869B86  48 2B C8                        sub rcx, rax
00869B89  48 8B 01                        mov rax, qword ptr [rcx]
00869B8C  80 78 18 00                     cmp byte ptr [rax + 0x18], 0
00869B90  0F 84 61 FE FF FF               je 0x1408699f7
00869B96  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00869B9A  48 83 F8 01                     cmp rax, 1
00869B9E  75 0A                           jne 0x140869baa
00869BA0  BD 06 A0 00 C0                  mov ebp, 0xc000a006
00869BA5  E9 99 FC FF FF                  jmp 0x140869843
00869BAA  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00869BAF  E9 43 FE FF FF                  jmp 0x1408699f7
00869BB4  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
00869BBC  48 85 DB                        test rbx, rbx
00869BBF  0F 85 C0 01 00 00               jne 0x140869d85
00869BC5  BD 08 00 00 C0                  mov ebp, 0xc0000008
00869BCA  E9 84 FC FF FF                  jmp 0x140869853
00869BCF  BD 08 00 00 C0                  mov ebp, 0xc0000008
00869BD4  E9 A2 FC FF FF                  jmp 0x14086987b
00869BD9  41 83 7D 04 00                  cmp dword ptr [r13 + 4], 0
00869BDE  0F 84 4D FE FF FF               je 0x140869a31
00869BE4  49 8B D2                        mov rdx, r10
00869BE7  49 8B CD                        mov rcx, r13
00869BEA  E8 65 18 00 00                  call 0x14086b454
00869BEF  48 85 C0                        test rax, rax
00869BF2  0F 84 39 FE FF FF               je 0x140869a31
00869BF8  48 8B 00                        mov rax, qword ptr [rax]
00869BFB  49 89 03                        mov qword ptr [r11], rax
00869BFE  E9 2E FE FF FF                  jmp 0x140869a31
00869C03  33 D2                           xor edx, edx
00869C05  4C 8D 43 30                     lea r8, [rbx + 0x30]
00869C09  48 03 C1                        add rax, rcx
00869C0C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00869C11  8D 4A 18                        lea ecx, [rdx + 0x18]
00869C14  44 8D 4A 10                     lea r9d, [rdx + 0x10]
00869C18  E8 43 3A C9 FF                  call 0x1404fd660
00869C1D  CC                              int3
00869C1E  33 D2                           xor edx, edx
00869C20  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00869C25  4C 8B C7                        mov r8, rdi
00869C28  8D 4A 18                        lea ecx, [rdx + 0x18]
00869C2B  44 8D 4A 10                     lea r9d, [rdx + 0x10]
00869C2F  E8 2C 3A C9 FF                  call 0x1404fd660
00869C34  CC                              int3
00869C35  33 D2                           xor edx, edx
00869C37  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
00869C3C  4D 8B C7                        mov r8, r15
00869C3F  8D 4A 18                        lea ecx, [rdx + 0x18]
00869C42  44 8D 4A 10                     lea r9d, [rdx + 0x10]
00869C46  E8 15 3A C9 FF                  call 0x1404fd660
00869C4B  CC                              int3
00869C4C  4D 85 C0                        test r8, r8
00869C4F  0F 85 3A FE FF FF               jne 0x140869a8f
00869C55  E9 4C FE FF FF                  jmp 0x140869aa6
00869C5A  E8 51 02 AE FF                  call 0x140349eb0
00869C5F  E9 17 FC FF FF                  jmp 0x14086987b
00869C64  E8 47 02 AE FF                  call 0x140349eb0
00869C69  E9 03 FE FF FF                  jmp 0x140869a71
00869C6E  B8 08 00 00 C0                  mov eax, 0xc0000008
00869C73  E9 0D FC FF FF                  jmp 0x140869885
00869C78  48 8D 41 FF                     lea rax, [rcx - 1]
00869C7C  48 81 E6 01 00 FE FF            and rsi, 0xfffffffffffe0001
00869C83  0F B7 C8                        movzx ecx, ax
00869C86  48 03 C9                        add rcx, rcx
00869C89  48 0B CE                        or rcx, rsi
00869C8C  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
00869C91  48 8D 4C 24 48                  lea rcx, [rsp + 0x48]
00869C96  E8 F5 6F BC FF                  call 0x140430c90
00869C9B  48 8B D8                        mov rbx, rax
00869C9E  B9 F0 7F 00 00                  mov ecx, 0x7ff0
00869CA3  F0 48 0F C1 08                  lock xadd qword ptr [rax], rcx
00869CA8  48 85 C9                        test rcx, rcx
00869CAB  0F 8E B5 00 00 00               jle 0x140869d66
00869CB1  41 B8 F0 7F 00 00               mov r8d, 0x7ff0
00869CB7  48 8D 54 24 48                  lea rdx, [rsp + 0x48]
00869CBC  48 8B CF                        mov rcx, rdi
00869CBF  E8 4C 45 C1 FF                  call 0x14047e210
00869CC4  85 C0                           test eax, eax
00869CC6  0F 84 E7 FC FF FF               je 0x1408699b3
00869CCC  F7 D8                           neg eax
00869CCE  48 98                           cdqe
00869CD0  F0 48 01 03                     lock add qword ptr [rbx], rax
00869CD4  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
00869CD9  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
00869CDE  E9 EF FA FF FF                  jmp 0x1408697d2
00869CE3  BD 22 00 00 C0                  mov ebp, 0xc0000022
00869CE8  E9 56 FB FF FF                  jmp 0x140869843
00869CED  45 33 C9                        xor r9d, r9d
00869CF0  48 89 6C 24 20                  mov qword ptr [rsp + 0x20], rbp
00869CF5  48 8B D3                        mov rdx, rbx
00869CF8  B9 89 01 00 00                  mov ecx, 0x189
00869CFD  E8 5E 39 C9 FF                  call 0x1404fd660
00869D02  CC                              int3
00869D03  45 84 C9                        test r9b, r9b
00869D06  0F 85 D0 F9 FF FF               jne 0x1408696dc
00869D0C  48 8B CB                        mov rcx, rbx
00869D0F  E8 04 F5 34 00                  call 0x140bb9218
00869D14  E9 C3 F9 FF FF                  jmp 0x1408696dc
00869D19  85 ED                           test ebp, ebp
00869D1B  0F 84 19 FD FF FF               je 0x140869a3a
00869D21  4C 8B CB                        mov r9, rbx
00869D24  89 6C 24 20                     mov dword ptr [rsp + 0x20], ebp
00869D28  4C 8B C7                        mov r8, rdi
00869D2B  49 8B D2                        mov rdx, r10
00869D2E  49 8B CD                        mov rcx, r13
00869D31  E8 3A 25 0E 00                  call 0x14094c270
00869D36  84 C0                           test al, al
00869D38  0F 85 FC FC FF FF               jne 0x140869a3a
00869D3E  BD 08 00 00 C0                  mov ebp, 0xc0000008
00869D43  E9 FB FA FF FF                  jmp 0x140869843
00869D48  45 84 C9                        test r9b, r9b
00869D4B  0F 84 B0 FB FF FF               je 0x140869901
00869D51  BD 22 00 00 C0                  mov ebp, 0xc0000022
00869D56  E9 28 FB FF FF                  jmp 0x140869883
00869D5B  45 84 C9                        test r9b, r9b
00869D5E  0F 84 4E FD FF FF               je 0x140869ab2
00869D64  EB EB                           jmp 0x140869d51
00869D66  33 D2                           xor edx, edx
00869D68  4C 8D 40 30                     lea r8, [rax + 0x30]
00869D6C  48 81 C1 F0 7F 00 00            add rcx, 0x7ff0
00869D73  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00869D78  8D 4A 18                        lea ecx, [rdx + 0x18]
00869D7B  44 8D 4A 10                     lea r9d, [rdx + 0x10]
00869D7F  E8 DC 38 C9 FF                  call 0x1404fd660
00869D84  CC                              int3
00869D85  65 4C 8B 04 25 88 01 00 00      mov r8, qword ptr gs:[0x188]
00869D8E  48 8B D3                        mov rdx, rbx
00869D91  49 8B CD                        mov rcx, r13
00869D94  45 0F B6 80 32 02 00 00         movzx r8d, byte ptr [r8 + 0x232]
00869D9C  E8 DF 67 BD FF                  call 0x140440580
00869DA1  E9 1F FE FF FF                  jmp 0x140869bc5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObpReferenceObjectByHandleWithTag(__int64 a1, int a2, __int64 a3, unsigned __int8 a4, unsigned int a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int8 v_stack_m78;
    unsigned int v_stack_p0;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_pB0;
    unsigned int v_stack_pB8;
    unsigned __int8 v_stack_pC8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (128);
    v_rbp = 0;
    v_stack_m78 = 0;
    *(unsigned __int64 *)(a6) = 0;
    if (a8 != 0) {
        a1 = 0;
        *(unsigned __int64 *)(a8) = 0;
    }
    v_stack_m30 = v_rdi;
    result = (0) & (0xFFFFFFFF80000000ULL);
    v_stack_m38 = v_r13;
    v_stack_m40 = v_r14;
    if (result == 0xFFFFFFFF80000000ULL) goto loc_008698A4;
    if (((*(unsigned int *)(v_rip + 6927178)) & (256)) != 0) goto loc_00869D03;
loc_008696DC:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544))) goto loc_00869AFD;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544))) goto loc_00869BCF;
loc_0086970C:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 768) == 0) goto loc_00869BCF;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 768)) == (*(unsigned __int64 *)(v_rip + 6971036))) goto loc_00869BC5;
loc_00869722:
    if (((0) & (0x3FCULL)) == 0) goto loc_00869BBC;
    result = ExpLookupHandleTableEntry(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 768), 0, a3, a4);
    if (result == 0) goto loc_00869BBC;
loc_0086974B:
    v_stack_m60 = *(unsigned __int64 *)(result);
    v_stack_m58 = *(unsigned __int64 *)(result + 8);
loc_0086975E:
    if (((v_stack_m60) & (0x1FFFEULL)) == 0) goto loc_00869950;
    result = (unsigned __int8)(~((unsigned __int8)(v_stack_m60)));
    if ((((unsigned __int8)(result)) & (1)) == 0) goto loc_0086978C;
    result = ExpBlockOnLockedHandleEntry(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 768), result, v_stack_m60, a4);
    goto loc_0086974B;
loc_0086978C:
    v_stack_m60 = v_stack_m60;
    result = ((((unsigned __int8)(result)) & (1)) == 0) ? 1 : 0;
    v_stack_m58 = *(unsigned __int64 *)(result + 8);
    if ((unsigned __int8)(result) == 0) goto loc_0086975E;
    a1 = (v_stack_m60) >> (1);
    if (((unsigned __int16)(a1)) == 16) goto loc_00869C78;
    result = ExGetHandlePointer(v_stack_m60, *(unsigned __int64 *)(result + 8), v_stack_m60, a4);
loc_008697D2:
    result = ObpTraceObjectReferenceIfActive(result, 1, (unsigned int)(a5), a4);
    result = (result) >> (8);
    result = (unsigned __int8)((result) ^ (*(unsigned __int8 *)(result + 24)));
    result = (unsigned __int8)((result) ^ (*(unsigned __int8 *)(v_rip + 7722566)));
    if (v_stack_p18 == 0) goto loc_00869814;
    if ((*(unsigned __int8 *)(v_stack_p18 + 40)) == ((unsigned __int8)(result))) goto loc_008699DB;
loc_00869814:
    if (*(unsigned __int64 *)(v_rip - 8820726 + (unsigned __int8)(result) * 8 + 16545792) == 0) goto loc_00869CED;
    if ((*(unsigned __int64 *)(v_rip - 8820726 + (unsigned __int8)(result) * 8 + 16545792)) == (*(unsigned __int64 *)(v_rip + 7721945))) goto loc_00869CED;
    if (v_stack_p18 == 0) goto loc_008699DB;
loc_00869843:
    result = ObfDereferenceObjectWithTag(result + 48, (unsigned int)(a5), *(unsigned __int64 *)(v_rip - 8820726 + (unsigned __int8)(result) * 8 + 16545792), a4);
loc_00869853:
    if (v_stack_m78 == 0) goto loc_0086987B;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 488)) & (-2);
    if (condition_is_not_equal) goto loc_00869C5A;
loc_0086987B:
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), result - 2, *(unsigned __int64 *)(v_rip - 8820726 + (unsigned __int8)(result) * 8 + 16545792), a4);
loc_00869883:
loc_00869885:
    v_rsp = (v_rsp) + (128);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000024ULL)));
loc_008698A4:
    if (result == -1) goto loc_008698E1;
    if (result == -2) goto loc_00869A99;
    if (a4 != 0) goto loc_00869C6E;
    v_rbx = (result) ^ (0xFFFFFFFF80000000ULL);
    v_stack_pB0 = v_rbx;
    goto loc_00869722;
loc_008698E1:
    if ((*(unsigned __int64 *)(v_rip - 8820726 + (unsigned __int8)(result) * 8 + 16545792)) != (*(unsigned __int64 *)(v_rip + 7721392))) goto loc_00869A86;
loc_008698EE:
    if ((((unsigned int)(result - 2)) & (0xFFE00000ULL)) != 0) goto loc_00869D48;
loc_00869901:
    if (a7 != 0) {
        *(unsigned int *)(a7 + 4) = 0x1FFFFFULL;
        *(unsigned int *)(a7) = (unsigned int)((unsigned int)(0xC0000024ULL));
    }
    result = ObpTraceObjectReferenceIfActive(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) - 48, 1, (unsigned int)(a5), a4);
    v_r12 = (1) + 1;
    if (v_r12 <= 1) goto loc_00869C1E;
    *(unsigned __int64 *)(v_stack_m60) = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    goto loc_00869883;
loc_00869950:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)))) & (1)) == 0) goto loc_008699C2;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)))) & (1)) != 0) goto loc_00869950;
    result = ExGetHandlePointer(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), 1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)), a4);
    v_stack_p48 = v_xmm0;
    result = ExSlowReplenishHandleTableEntry(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), 1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)), a4);
    result = (unsigned int)((result) + 1);
    if (condition_is_less_or_equal) goto loc_00869C03;
    result = (int)((unsigned int)(result));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6970612) + 48)) != ((unsigned int)(0xC0000024ULL))) {
        a2 = 0;
        result = ExfUnblockPushLock(*(unsigned __int64 *)(v_rip + 6970612) + 48, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)), a4);
    }
    goto loc_008697D2;
loc_008699C2:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) == 0) goto loc_00869BB4;
    result = ExpBlockOnLockedHandleEntry(*(unsigned __int64 *)(v_rip + 6970612), *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)), a4);
    goto loc_00869950;
loc_008699DB:
    v_r14 = (unsigned int)((v_stack_p50) & (0x1FFFFFFULL));
    if (v_stack_pC8 != ((unsigned __int8)((unsigned int)(0xC0000024ULL)))) goto loc_00869B5F;
loc_008699F7:
    v_rsi = (v_stack_p48) >> (17);
    if (a7 == 0) goto loc_00869A80;
    v_rsi = (unsigned int)((v_rsi) & (7));
    *(unsigned int *)(a7 + 4) = (unsigned int)(v_r14);
    *(unsigned int *)(a7) = (unsigned int)(v_rsi);
    v_rsi = (unsigned int)((v_rsi) >> (2));
loc_00869A14:
    v_rsi = (unsigned __int8)((v_rsi) & (1));
    if (a8 != 0) goto loc_00869BD9;
loc_00869A31:
    if ((unsigned __int8)(v_rsi) != 0) goto loc_00869D19;
loc_00869A3A:
    *(unsigned __int64 *)(a6) = result + 48;
    if (v_stack_p30 == 0) goto loc_00869A71;
    result = (*(unsigned __int64 *)(v_r12 + 488)) & (-2);
    if (condition_is_not_equal) goto loc_00869C64;
loc_00869A71:
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), result - 2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)), a4);
    result = 0;
    goto loc_00869885;
loc_00869A80:
    v_rsi = (unsigned __int8)((v_rsi) >> (2));
    goto loc_00869A14;
loc_00869A86:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) == 0) goto loc_008698EE;
loc_00869A8F:
    goto loc_00869883;
loc_00869A99:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184))) != (*(unsigned __int64 *)(v_rip + 7721000))) goto loc_00869C4C;
loc_00869AA6:
    if ((((unsigned int)(result - 2)) & (0xFFE00000ULL)) != 0) goto loc_00869D5B;
loc_00869AB2:
    if (a7 != 0) {
        *(unsigned int *)(a7 + 4) = 0x1FFFFFULL;
        *(unsigned int *)(a7) = (unsigned int)((unsigned int)(0xC0000024ULL));
    }
    result = ObpTraceObjectReferenceIfActive(*(unsigned __int64 *)(gs_base + (0 + 392)) - 48, 1, (unsigned int)(a5), a4);
    v_r12 = (1) + 1;
    if (v_r12 <= 1) goto loc_00869C35;
    *(unsigned __int64 *)(v_rsi) = *(unsigned __int64 *)(gs_base + (0 + 392));
    goto loc_00869883;
loc_00869AFD:
    result = (*(unsigned __int64 *)(v_r12 + 488)) & (-2);
    if (condition_is_not_equal) goto loc_00869B49;
loc_00869B1D:
    if (*(unsigned __int64 *)(v_r12 + 768) != 0) goto loc_00869B55;
    result = (*(unsigned __int64 *)(v_r12 + 488)) & (-2);
    if (condition_is_equal) goto loc_00869B55;
    result = ExfReleaseRundownProtection(v_r12 + 488, result - 2, (unsigned int)(a5), a4);
    goto loc_00869B55;
loc_00869B49:
    result = ExfAcquireRundownProtection(v_r12 + 488, result - 2, (unsigned int)(a5), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00869B1D;
loc_00869B55:
    v_stack_p30 = 1;
    goto loc_0086970C;
loc_00869B5F:
    result = (unsigned int)(~((unsigned int)((unsigned int)(v_r14))));
    if ((((unsigned int)((unsigned int)(0xC0000024ULL))) & ((unsigned int)(result))) != 0) goto loc_00869CE3;
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 26))) & (64)) == 0) goto loc_008699F7;
    result = (unsigned int)((*(unsigned __int8 *)(result + 26)) & (127));
    a1 = (result) - (*(unsigned __int8 *)(result + result - 2 * 1 + 15794048));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1) + 24)) == 0) goto loc_008699F7;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1) + 16)) != 1) goto loc_00869BAA;
    goto loc_00869843;
loc_00869BAA:
    goto loc_008699F7;
loc_00869BB4:
loc_00869BBC:
    if (v_stack_pB0 != 0) goto loc_00869D85;
loc_00869BC5:
    goto loc_00869853;
loc_00869BCF:
    goto loc_0086987B;
loc_00869BD9:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_r12 + 768) + 4)) == 0) goto loc_00869A31;
    result = ExpGetHandleExtraInfo(*(unsigned __int64 *)(v_r12 + 768), v_stack_pB0, (unsigned int)(a5), a4);
    if (result == 0) goto loc_00869A31;
    *(unsigned __int64 *)(a8) = *(unsigned __int64 *)(result);
    goto loc_00869A31;
loc_00869C03:
    a2 = 0;
    result = (*(unsigned __int64 *)(result)) + (*(unsigned __int64 *)(v_r12 + 768));
    v_stack_p20 = result;
    result = KeBugCheckEx(a2 + 24, a2, v_stack_pB0 + 48, a2 + 16);
loc_00869C1E:
    a2 = 0;
    v_stack_p20 = v_r12;
    result = KeBugCheckEx(a2 + 24, a2, v_r12 + 488, a2 + 16);
loc_00869C35:
    a2 = 0;
    v_stack_p20 = v_r12;
    result = KeBugCheckEx(a2 + 24, a2, *(unsigned __int64 *)(gs_base + (0 + 392)), a2 + 16);
loc_00869C4C:
    if (*(unsigned __int64 *)(gs_base + (0 + 392)) != 0) goto loc_00869A8F;
    goto loc_00869AA6;
loc_00869C5A:
    result = ExfReleaseRundownProtection(a2 + 24, a2, *(unsigned __int64 *)(gs_base + (0 + 392)), a2 + 16);
    goto loc_0086987B;
loc_00869C64:
    result = ExfReleaseRundownProtection(a2 + 24, a2, *(unsigned __int64 *)(gs_base + (0 + 392)), a2 + 16);
    goto loc_00869A71;
loc_00869C6E:
    goto loc_00869885;
loc_00869C78:
    v_rsi = (v_stack_p48) & (0xFFFFFFFFFFFE0001ULL);
    a1 = ((unsigned __int16)(a2 + 24 - 1)) + ((unsigned __int16)(a2 + 24 - 1));
    a1 = (a1) | (v_rsi);
    v_stack_p48 = a1;
    result = ExGetHandlePointer(v_stack_p48, a2, *(unsigned __int64 *)(gs_base + (0 + 392)), a2 + 16);
    if (condition_is_less_or_equal) goto loc_00869D66;
    result = ExFastReplenishHandleTableEntry(v_r12 + 488, v_stack_p48, (unsigned int)(0x7FF0ULL), a2 + 16);
    if ((unsigned int)(result) == 0) goto loc_008699B3;
    result = (unsigned int)(-(result));
    goto loc_008697D2;
loc_00869CE3:
    goto loc_00869843;
loc_00869CED:
    a4 = 0;
    v_stack_p20 = (unsigned int)(0xC0000022ULL);
    result = KeBugCheckEx(393, result, (unsigned int)(0x7FF0ULL), a4);
loc_00869D03:
    if (0 != 0) goto loc_008696DC;
    result = VfCheckUserHandle(result, result, (unsigned int)(0x7FF0ULL), a4);
    goto loc_008696DC;
loc_00869D19:
    if ((unsigned int)((unsigned int)(0xC0000022ULL)) == 0) goto loc_00869A3A;
    v_stack_p20 = (unsigned int)((unsigned int)(0xC0000022ULL));
    result = ObpAuditObjectAccess(*(unsigned __int64 *)(v_r12 + 768), v_stack_pB0, v_r12 + 488, result);
    if ((unsigned __int8)(result) != 0) goto loc_00869A3A;
    goto loc_00869843;
loc_00869D48:
    if ((unsigned __int8)(result) == 0) goto loc_00869901;
loc_00869D51:
    goto loc_00869883;
loc_00869D5B:
    if ((unsigned __int8)(result) == 0) goto loc_00869AB2;
    goto loc_00869D51;
loc_00869D66:
    a2 = 0;
    a1 = (*(unsigned __int64 *)(v_r12 + 768)) + (0x7FF0ULL);
    v_stack_p20 = a1;
    result = KeBugCheckEx(a2 + 24, a2, result + 48, a2 + 16);
loc_00869D85:
    result = ExHandleLogBadReference(*(unsigned __int64 *)(v_r12 + 768), result, *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), a2 + 16);
    goto loc_00869BC5;
}
```

## 5. (Beta) C Style

```c
int64_t ObpReferenceObjectByHandleWithTag(int64_t Arg1, int32_t Arg2, int64_t Arg3, uint8_t Arg4, uint32_t Arg5, void *Arg6, int64_t Arg7, int64_t Arg8)
{
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint8_t v_stack_m78;
    uint32_t v_stack_p0;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint8_t v_stack_p20;
    uint8_t v_stack_p30;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p8;
    uint64_t v_stack_pB0;
    uint32_t v_stack_pB8;
    uint8_t v_stack_pC8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (128);
    local_rbp = 0;
    v_stack_m78 = 0;
    *(uint64_t *)(arg6) = 0;
    if (Arg8 != 0) {
        Arg1 = 0;
        *(uint64_t *)(Arg8) = 0;
    }
    v_stack_m30 = local_rdi;
    result = (0) & (0xFFFFFFFF80000000ULL);
    v_stack_m38 = local_r13;
    v_stack_m40 = local_r14;
    if (result == 0xFFFFFFFF80000000ULL) goto loc_008698A4;
    if (((*(uint32_t *)(v_rip + 0x69B34A)) & (256)) != 0) goto loc_00869D03;
loc_008696DC:
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) != (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220))) goto loc_00869AFD;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) >= (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220))) goto loc_00869BCF;
loc_0086970C:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x300) == 0) goto loc_00869BCF;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x300)) == (*(uint64_t *)(v_rip + 0x6A5E9C))) goto loc_00869BC5;
loc_00869722:
    if (((0) & (0x3FCULL)) == 0) goto loc_00869BBC;
    result = ExpLookupHandleTableEntry(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x300), 0, Arg3, Arg4);
    if (result == 0) goto loc_00869BBC;
loc_0086974B:
    v_stack_m60 = *(uint64_t *)(result);
    v_stack_m58 = *(uint64_t *)(result + 0x8);
loc_0086975E:
    if (((v_stack_m60) & (0x1FFFEULL)) == 0) goto loc_00869950;
    result = (uint8_t)(~((uint8_t)(v_stack_m60)));
    if ((((uint8_t)(result)) & (1)) == 0) goto loc_0086978C;
    result = ExpBlockOnLockedHandleEntry(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x300), result, v_stack_m60, Arg4);
    goto loc_0086974B;
loc_0086978C:
    v_stack_m60 = v_stack_m60;
    result = ((((uint8_t)(result)) & (1)) == 0) ? 1 : 0;
    v_stack_m58 = *(uint64_t *)(result + 0x8);
    if ((uint8_t)(result) == 0) goto loc_0086975E;
    Arg1 = (v_stack_m60) >> (1);
    if (((uint16_t)(Arg1)) == 16) goto loc_00869C78;
    result = ExGetHandlePointer(v_stack_m60, *(uint64_t *)(result + 0x8), v_stack_m60, Arg4);
loc_008697D2:
    result = ObpTraceObjectReferenceIfActive(result, 1, (uint32_t)(Arg5), Arg4);
    result = (result) >> (8);
    result = (uint8_t)((result) ^ (*(uint8_t *)(result + 0x18)));
    result = (uint8_t)((result) ^ (*(uint8_t *)(v_rip + 0x75D646)));
    if (v_stack_p18 == 0) goto loc_00869814;
    if ((*(uint8_t *)(v_stack_p18 + 0x28)) == ((uint8_t)(result))) goto loc_008699DB;
loc_00869814:
    if (*(uint64_t *)(v_rip - 0x8697F6 + (uint8_t)(result) * 8 + 0xFC7800) == 0) goto loc_00869CED;
    if ((*(uint64_t *)(v_rip - 0x8697F6 + (uint8_t)(result) * 8 + 0xFC7800)) == (*(uint64_t *)(v_rip + 0x75D3D9))) goto loc_00869CED;
    if (v_stack_p18 == 0) goto loc_008699DB;
loc_00869843:
    result = ObfDereferenceObjectWithTag(result + 48, (uint32_t)(Arg5), *(uint64_t *)(v_rip - 0x8697F6 + (uint8_t)(result) * 8 + 0xFC7800), Arg4);
loc_00869853:
    if (v_stack_m78 == 0) goto loc_0086987B;
    result = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1E8)) & (-2);
    if (condition_is_not_equal) goto loc_00869C5A;
loc_0086987B:
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), result - 2, *(uint64_t *)(v_rip - 0x8697F6 + (uint8_t)(result) * 8 + 0xFC7800), Arg4);
loc_00869883:
loc_00869885:
    local_rsp = (local_rsp) + (128);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000024ULL)));
loc_008698A4:
    if (result == -1) goto loc_008698E1;
    if (result == -2) goto loc_00869A99;
    if (Arg4 != 0) goto loc_00869C6E;
    local_rbx = (result) ^ (0xFFFFFFFF80000000ULL);
    v_stack_pB0 = local_rbx;
    goto loc_00869722;
loc_008698E1:
    if ((*(uint64_t *)(v_rip - 0x8697F6 + (uint8_t)(result) * 8 + 0xFC7800)) != (*(uint64_t *)(v_rip + 0x75D1B0))) goto loc_00869A86;
loc_008698EE:
    if ((((uint32_t)(result - 2)) & (0xFFE00000ULL)) != 0) goto loc_00869D48;
loc_00869901:
    if (Arg7 != 0) {
        *(uint32_t *)(Arg7 + 0x4) = 0x1FFFFFULL;
        *(uint32_t *)(Arg7) = (uint32_t)((uint32_t)(0xC0000024ULL));
    }
    result = ObpTraceObjectReferenceIfActive(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) - 48, 1, (uint32_t)(Arg5), Arg4);
    local_r12 = (1) + 1;
    if (local_r12 <= 1) goto loc_00869C1E;
    *(uint64_t *)(v_stack_m60) = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    goto loc_00869883;
loc_00869950:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)))) & (1)) == 0) goto loc_008699C2;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)))) & (1)) != 0) goto loc_00869950;
    result = ExGetHandlePointer(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), 1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)), Arg4);
    v_stack_p48 = v_xmm0;
    result = ExSlowReplenishHandleTableEntry(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), 1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)), Arg4);
    result = (uint32_t)((result) + 1);
    if (condition_is_less_or_equal) goto loc_00869C03;
    result = (int32_t)((uint32_t)(result));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x6A5CF4) + 0x30)) != ((uint32_t)(0xC0000024ULL))) {
        Arg2 = 0;
        result = ExfUnblockPushLock(*(uint64_t *)(v_rip + 0x6A5CF4) + 48, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)), Arg4);
    }
    goto loc_008697D2;
loc_008699C2:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) == 0) goto loc_00869BB4;
    result = ExpBlockOnLockedHandleEntry(*(uint64_t *)(v_rip + 0x6A5CF4), *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)), Arg4);
    goto loc_00869950;
loc_008699DB:
    local_r14 = (uint32_t)((v_stack_p50) & (0x1FFFFFFULL));
    if (v_stack_pC8 != ((uint8_t)((uint32_t)(0xC0000024ULL)))) goto loc_00869B5F;
loc_008699F7:
    local_rsi = (v_stack_p48) >> (17);
    if (Arg7 == 0) goto loc_00869A80;
    local_rsi = (uint32_t)((local_rsi) & (7));
    *(uint32_t *)(Arg7 + 0x4) = (uint32_t)(local_r14);
    *(uint32_t *)(Arg7) = (uint32_t)(local_rsi);
    local_rsi = (uint32_t)((local_rsi) >> (2));
loc_00869A14:
    local_rsi = (uint8_t)((local_rsi) & (1));
    if (Arg8 != 0) goto loc_00869BD9;
loc_00869A31:
    if ((uint8_t)(local_rsi) != 0) goto loc_00869D19;
loc_00869A3A:
    *(uint64_t *)(arg6) = result + 48;
    if (v_stack_p30 == 0) goto loc_00869A71;
    result = (*(uint64_t *)(local_r12 + 0x1E8)) & (-2);
    if (condition_is_not_equal) goto loc_00869C64;
loc_00869A71:
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), result - 2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)), Arg4);
    result = 0;
    goto loc_00869885;
loc_00869A80:
    local_rsi = (uint8_t)((local_rsi) >> (2));
    goto loc_00869A14;
loc_00869A86:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) == 0) goto loc_008698EE;
loc_00869A8F:
    goto loc_00869883;
loc_00869A99:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8))) != (*(uint64_t *)(v_rip + 0x75D028))) goto loc_00869C4C;
loc_00869AA6:
    if ((((uint32_t)(result - 2)) & (0xFFE00000ULL)) != 0) goto loc_00869D5B;
loc_00869AB2:
    if (Arg7 != 0) {
        *(uint32_t *)(Arg7 + 0x4) = 0x1FFFFFULL;
        *(uint32_t *)(Arg7) = (uint32_t)((uint32_t)(0xC0000024ULL));
    }
    result = ObpTraceObjectReferenceIfActive(*(uint64_t *)(gs_base + (0 + 0x188)) - 48, 1, (uint32_t)(Arg5), Arg4);
    local_r12 = (1) + 1;
    if (local_r12 <= 1) goto loc_00869C35;
    *(uint64_t *)(local_rsi) = *(uint64_t *)(gs_base + (0 + 0x188));
    goto loc_00869883;
loc_00869AFD:
    result = (*(uint64_t *)(local_r12 + 0x1E8)) & (-2);
    if (condition_is_not_equal) goto loc_00869B49;
loc_00869B1D:
    if (*(uint64_t *)(local_r12 + 0x300) != 0) goto loc_00869B55;
    result = (*(uint64_t *)(local_r12 + 0x1E8)) & (-2);
    if (condition_is_equal) goto loc_00869B55;
    result = ExfReleaseRundownProtection(local_r12 + 488, result - 2, (uint32_t)(Arg5), Arg4);
    goto loc_00869B55;
loc_00869B49:
    result = ExfAcquireRundownProtection(local_r12 + 488, result - 2, (uint32_t)(Arg5), Arg4);
    if ((uint8_t)(result) != 0) goto loc_00869B1D;
loc_00869B55:
    v_stack_p30 = 1;
    goto loc_0086970C;
loc_00869B5F:
    result = (uint32_t)(~((uint32_t)((uint32_t)(local_r14))));
    if ((((uint32_t)((uint32_t)(0xC0000024ULL))) & ((uint32_t)(result))) != 0) goto loc_00869CE3;
    if ((((uint8_t)(*(uint8_t *)(result + 0x1A))) & (64)) == 0) goto loc_008699F7;
    result = (uint32_t)((*(uint8_t *)(result + 0x1A)) & (127));
    Arg1 = (result) - (*(uint8_t *)(result + result - 0x2 * 1 + 0xF0FF80));
    if ((*(uint8_t *)(*(uint64_t *)(Arg1) + 0x18)) == 0) goto loc_008699F7;
    if ((*(uint64_t *)(*(uint64_t *)(Arg1) + 0x10)) != 1) goto loc_00869BAA;
    goto loc_00869843;
loc_00869BAA:
    goto loc_008699F7;
loc_00869BB4:
loc_00869BBC:
    if (v_stack_pB0 != 0) goto loc_00869D85;
loc_00869BC5:
    goto loc_00869853;
loc_00869BCF:
    goto loc_0086987B;
loc_00869BD9:
    if ((*(uint32_t *)(*(uint64_t *)(local_r12 + 0x300) + 0x4)) == 0) goto loc_00869A31;
    result = ExpGetHandleExtraInfo(*(uint64_t *)(local_r12 + 0x300), v_stack_pB0, (uint32_t)(Arg5), Arg4);
    if (result == 0) goto loc_00869A31;
    *(uint64_t *)(Arg8) = *(uint64_t *)(result);
    goto loc_00869A31;
loc_00869C03:
    Arg2 = 0;
    result = (*(uint64_t *)(result)) + (*(uint64_t *)(local_r12 + 0x300));
    v_stack_p20 = result;
    result = KeBugCheckEx(Arg2 + 24, Arg2, v_stack_pB0 + 48, Arg2 + 16);
loc_00869C1E:
    Arg2 = 0;
    v_stack_p20 = local_r12;
    result = KeBugCheckEx(Arg2 + 24, Arg2, local_r12 + 488, Arg2 + 16);
loc_00869C35:
    Arg2 = 0;
    v_stack_p20 = local_r12;
    result = KeBugCheckEx(Arg2 + 24, Arg2, *(uint64_t *)(gs_base + (0 + 0x188)), Arg2 + 16);
loc_00869C4C:
    if (*(uint64_t *)(gs_base + (0 + 0x188)) != 0) goto loc_00869A8F;
    goto loc_00869AA6;
loc_00869C5A:
    result = ExfReleaseRundownProtection(Arg2 + 24, Arg2, *(uint64_t *)(gs_base + (0 + 0x188)), Arg2 + 16);
    goto loc_0086987B;
loc_00869C64:
    result = ExfReleaseRundownProtection(Arg2 + 24, Arg2, *(uint64_t *)(gs_base + (0 + 0x188)), Arg2 + 16);
    goto loc_00869A71;
loc_00869C6E:
    goto loc_00869885;
loc_00869C78:
    local_rsi = (v_stack_p48) & (0xFFFFFFFFFFFE0001ULL);
    Arg1 = ((uint16_t)(Arg2 + 24 - 1)) + ((uint16_t)(Arg2 + 24 - 1));
    Arg1 = (Arg1) | (local_rsi);
    v_stack_p48 = Arg1;
    result = ExGetHandlePointer(v_stack_p48, Arg2, *(uint64_t *)(gs_base + (0 + 0x188)), Arg2 + 16);
    if (condition_is_less_or_equal) goto loc_00869D66;
    result = ExFastReplenishHandleTableEntry(local_r12 + 488, v_stack_p48, (uint32_t)(0x7FF0ULL), Arg2 + 16);
    if ((uint32_t)(result) == 0) goto loc_008699B3;
    result = (uint32_t)(-(result));
    goto loc_008697D2;
loc_00869CE3:
    goto loc_00869843;
loc_00869CED:
    Arg4 = 0;
    v_stack_p20 = (uint32_t)(0xC0000022ULL);
    result = KeBugCheckEx(393, result, (uint32_t)(0x7FF0ULL), Arg4);
loc_00869D03:
    if (0 != 0) goto loc_008696DC;
    result = VfCheckUserHandle(result, result, (uint32_t)(0x7FF0ULL), Arg4);
    goto loc_008696DC;
loc_00869D19:
    if ((uint32_t)((uint32_t)(0xC0000022ULL)) == 0) goto loc_00869A3A;
    v_stack_p20 = (uint32_t)((uint32_t)(0xC0000022ULL));
    result = ObpAuditObjectAccess(*(uint64_t *)(local_r12 + 0x300), v_stack_pB0, local_r12 + 488, result);
    if ((uint8_t)(result) != 0) goto loc_00869A3A;
    goto loc_00869843;
loc_00869D48:
    if ((uint8_t)(result) == 0) goto loc_00869901;
loc_00869D51:
    goto loc_00869883;
loc_00869D5B:
    if ((uint8_t)(result) == 0) goto loc_00869AB2;
    goto loc_00869D51;
loc_00869D66:
    Arg2 = 0;
    Arg1 = (*(uint64_t *)(local_r12 + 0x300)) + (0x7FF0ULL);
    v_stack_p20 = Arg1;
    result = KeBugCheckEx(Arg2 + 24, Arg2, result + 48, Arg2 + 16);
loc_00869D85:
    result = ExHandleLogBadReference(*(uint64_t *)(local_r12 + 0x300), result, *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), Arg2 + 16);
    goto loc_00869BC5;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00869650&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
