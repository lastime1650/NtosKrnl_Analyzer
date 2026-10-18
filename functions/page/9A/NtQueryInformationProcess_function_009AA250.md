# NtQueryInformationProcess

- RVA: `0x009AA250`–`0x009AE763` (길이 `17,683` bytes)
- VA: `0x00000001409AA250`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009D8C4`
- 디코드: `3,914`개 명령, `17,683/17,683` bytes 표시
- 미해석 바이트: `58` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **228**; 고유 호출 대상: **83**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **11**

### Outgoing calls
- `0x009AA2E6` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009AA31C` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009AA391` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009AA3A4` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009AA460` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AA516` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AA5B4` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AA5EF` → [VslGetSecurePebAddress](../A7/VslGetSecurePebAddress_function_00A71B64.md) (function, `0x00A71B64`)
- `0x009AA66A` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009AA68F` → [KeQueryAffinityProcess](../../text/2C/KeQueryAffinityProcess_function_002CE710.md) (function, `0x002CE710`)
- `0x009AA852` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AA91A` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009AABF5` → [ObReferenceProcessHandleTable](../89/ObReferenceProcessHandleTable_function_00893B70.md) (function, `0x00893B70`)
- `0x009AAC10` → [ExQueryHandleExceptionsPermanency](../../text/45/ExQueryHandleExceptionsPermanency_function_00458CE0.md) (function, `0x00458CE0`)
- `0x009AAC50` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x009AAE11` → [PsQueryProcessSignatureMitigationPolicy](../A1/PsQueryProcessSignatureMitigationPolicy_function_00A11660.md) (function, `0x00A11660`)
- `0x009AAE82` → [PspGetNoChildProcessRestrictedPolicy](../A1/PspGetNoChildProcessRestrictedPolicy_function_00A172B8.md) (function, `0x00A172B8`)
- `0x009AAF3D` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AAF5D` → [PspAllocateAndQueryProcessNotificationChannel](../9D/PspAllocateAndQueryProcessNotificationChannel_function_009D0140.md) (function, `0x009D0140`)
- `0x009AAF81` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AAFC6` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AAFE5` → [PsQueryRuntimeProcess](../9D/PsQueryRuntimeProcess_function_009D6C10.md) (function, `0x009D6C10`)
- `0x009AB03B` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AB067` → [PspQueryQuotaLimits](../9D/PspQueryQuotaLimits_function_009D6280.md) (function, `0x009D6280`)
- `0x009AB0A0` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AB0D4` → [PsQueryFullProcessImageName](../A1/PsQueryFullProcessImageName_function_00A115D0.md) (function, `0x00A115D0`)
- `0x009AB0E5` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AB151` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AB1DD` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AB202` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AB25F` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AB2B8` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x009AB2F7` → [MmQueryWorkingSetInformation](../../text/41/MmQueryWorkingSetInformation_function_0041CB20.md) (function, `0x0041CB20`)
- `0x009AB30A` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x009AB3BC` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AB3DB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009AB420` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (function, `0x00428814`)
- `0x009AB460` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AB484` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x009AB4D2` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AB4DE` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (function, `0x00456DC0`)
- `0x009AB539` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AB551` → [ObQueryDeviceMapInformation](../96/ObQueryDeviceMapInformation_function_0096C5C0.md) (function, `0x0096C5C0`)
- `0x009AB562` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AB5E0` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AB62F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AB648` → [MmGetSectionInformation](../92/MmGetSectionInformation_function_00921910.md) (function, `0x00921910`)
- `0x009AB658` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009AB6A3` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AB6DA` → [PsReferenceProcessFilePointer](../8D/PsReferenceProcessFilePointer_function_008D6870.md) (function, `0x008D6870`)
- `0x009AB6F1` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AB709` → [IoQueryFileDosDeviceName](../8A/IoQueryFileDosDeviceName_function_008A6340.md) (function, `0x008A6340`)
- `0x009AB713` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009AB75E` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009AB792` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009AB7D7` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AB7F4` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AB81E` → [KeTestBitGroupMask](../../text/43/KeTestBitGroupMask_function_00431330.md) (function, `0x00431330`)
- `0x009AB8B5` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AB8D2` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x009AB8EC` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x009AB9BF` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x009ABA23` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x009ABA8F` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x009ABA9C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009ABAE2` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009ABAF4` → [PsGetProcessSessionId](../../text/22/PsGetProcessSessionId_function_002233A0.md) (function, `0x002233A0`)
- `0x009ABB05` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009ABB59` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009ABB81` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009ABB97` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x009ABBA7` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x009ABBB3` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x009ABBF6` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009ABC1C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009ABC47` → [PsQueryProcessAttributes](../9D/PsQueryProcessAttributes_function_009DB630.md) (function, `0x009DB630`)
- `0x009ABC60` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (function, `0x00456DC0`)
- `0x009ABCAA` → [KeGetExecuteOptions](../A2/KeGetExecuteOptions_function_00A218E0.md) (function, `0x00A218E0`)
- `0x009ABCBF` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009ABD13` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009ABD20` → [BvgaSetVirtualFrameBuffer](../../text/4F/BvgaSetVirtualFrameBuffer_function_004FC600.md) (function, `0x004FC600`)
- `0x009ABD31` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009ABE10` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009ABE55` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009ABE71` → [PsQueryStatisticsProcess](../91/PsQueryStatisticsProcess_function_00919350.md) (function, `0x00919350`)
- `0x009ABEE0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009ABF4D` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009ABF73` → [EtwQueryProcessTelemetryInfo](../8A/EtwQueryProcessTelemetryInfo_function_008A51A0.md) (function, `0x008A51A0`)
- `0x009ABF8F` → [PsGetWin32KFilterSet](../../text/45/PsGetWin32KFilterSet_function_00458CC0.md) (function, `0x00458CC0`)
- `0x009AC045` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AC07B` → [MmQueryCommitReleaseState](../../text/48/MmQueryCommitReleaseState_function_004880B8.md) (function, `0x004880B8`)
- `0x009AC12F` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AC19D` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AC1C3` → [PsQueryProcessCommandLine](../../text/46/PsQueryProcessCommandLine_function_00469810.md) (function, `0x00469810`)
- `0x009AC20B` → [ExIsRestrictedCaller](../A2/ExIsRestrictedCaller_function_00A217E8.md) (function, `0x00A217E8`)
- `0x009AC270` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AC288` → [ObReferenceProcessHandleTable](../89/ObReferenceProcessHandleTable_function_00893B70.md) (function, `0x00893B70`)
- `0x009AC2A4` → [ExReferenceHandleDebugInfo](../9F/ExReferenceHandleDebugInfo_function_009F1E18.md) (function, `0x009F1E18`)
- `0x009AC2D2` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x009AC2F2` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x009AC303` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x009AC344` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x009AC36C` → [ObReferenceProcessHandleTable](../89/ObReferenceProcessHandleTable_function_00893B70.md) (function, `0x00893B70`)
- `0x009AC386` → [ExQueryProcessHandleInformation](../94/ExQueryProcessHandleInformation_function_0094C3D8.md) (function, `0x0094C3D8`)
- `0x009AC395` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x009AC3D8` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AC3F7` → [PsQueryTotalCycleTimeProcess](../A2/PsQueryTotalCycleTimeProcess_function_00A26840.md) (function, `0x00A26840`)
- `0x009AC43B` → [PspQueryWorkingSetWatch](../A2/PspQueryWorkingSetWatch_function_00A21478.md) (function, `0x00A21478`)
- `0x009AC47E` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AC4B3` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AC524` → [ExLockUserBuffer](../95/ExLockUserBuffer_function_009533B8.md) (function, `0x009533B8`)
- `0x009AC560` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AC582` → [ObReferenceProcessHandleTable](../89/ObReferenceProcessHandleTable_function_00893B70.md) (function, `0x00893B70`)
- `0x009AC5C8` → [ExEnumHandleTable](../91/ExEnumHandleTable_function_0091DB20.md) (function, `0x0091DB20`)
- `0x009AC5D4` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x009AC5E1` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AC5F4` → [ExUnlockUserBuffer](../../text/29/ExUnlockUserBuffer_function_0029F258.md) (function, `0x0029F258`)
- `0x009AC62C` → [PspGetNoChildProcessRestrictedPolicy](../A1/PspGetNoChildProcessRestrictedPolicy_function_00A172B8.md) (function, `0x00A172B8`)
- `0x009AC686` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AC6CB` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AC6EF` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AC743` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AC7AF` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AC7F9` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AC86C` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x009AC8C4` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AC8F5` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x009AC910` → [ZwQueryInformationJobObject](../../text/6A/ZwQueryInformationJobObject_function_006AFBB0.md) (function, `0x006AFBB0`)
- `0x009AC92C` → [ZwQueryInformationJobObject](../../text/6A/ZwQueryInformationJobObject_function_006AFBB0.md) (function, `0x006AFBB0`)
- `0x009AC93B` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x009AC9FB` → [PspGetRedirectionTrustPolicy](../A7/PspGetRedirectionTrustPolicy_function_00A769A8.md) (function, `0x00A769A8`)
- `0x009ACA6D` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009ACB0B` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009ACC18` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009ACC9A` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x009ACCA5` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009ACCE9` → [PspFindFirstThreadByTebValue](../AD/PspFindFirstThreadByTebValue_function_00AD8E2C.md) (function, `0x00AD8E2C`)
- `0x009ACD2B` → [KeQuerySystemTimePrecise](../../text/37/KeQuerySystemTimePrecise_function_0037DA40.md) (function, `0x0037DA40`)
- `0x009ACD3B` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x009ACD46` → [ExGenRandom](../../text/41/ExGenRandom_function_0041B010.md) (function, `0x0041B010`)
- `0x009ACDFA` → [MiCopyVirtualMemory](../9B/MiCopyVirtualMemory_function_009BBB50.md) (function, `0x009BBB50`)
- `0x009ACE49` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009ACE60` → [ObGetProcessHandleCount](../91/ObGetProcessHandleCount_function_009195D0.md) (function, `0x009195D0`)
- `0x009ACE71` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009ACED6` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009ACEF9` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009ACF43` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009ACF66` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009ACF97` → [PspQueryPooledQuotaLimits](../AC/PspQueryPooledQuotaLimits_function_00ACB678.md) (function, `0x00ACB678`)
- `0x009ACFE5` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AD008` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AD065` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AD086` → [PspLockProcessShared](../../text/40/PspLockProcessShared_function_004016D0.md) (function, `0x004016D0`)
- `0x009AD141` → [PspUnlockProcessShared](../../text/26/PspUnlockProcessShared_function_00263950.md) (function, `0x00263950`)
- `0x009AD151` → [PsGetProcessDeepFreezeStats](../8A/PsGetProcessDeepFreezeStats_function_008A375C.md) (function, `0x008A375C`)
- `0x009AD1CB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009AD1F2` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AD363` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AD3B3` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AD3D1` → [DbgkOpenProcessDebugPort](../A8/DbgkOpenProcessDebugPort_function_00A82414.md) (function, `0x00A82414`)
- `0x009AD3F9` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AD428` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x009AD4BE` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AD54F` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AD573` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AD5A2` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)
- `0x009AD779` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x009AD784` → [ExDereferenceHandleDebugInfo](../A1/ExDereferenceHandleDebugInfo_function_00A17430.md) (function, `0x00A17430`)
- `0x009AD795` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x009AD7A8` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x009AD7B0` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009AD80D` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AD84C` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AD865` → [PsReferenceProcessFilePointer](../8D/PsReferenceProcessFilePointer_function_008D6870.md) (function, `0x008D6870`)
- `0x009AD876` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AD8A7` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009AD8AF` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009AD910` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AD939` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AD998` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009AD9BD` → [KeQueryAffinityProcess](../../text/2C/KeQueryAffinityProcess_function_002CE710.md) (function, `0x002CE710`)
- `0x009ADA39` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009ADA56` → [KeQueryGroupMaskProcess](../../text/48/KeQueryGroupMaskProcess_function_0048E804.md) (function, `0x0048E804`)
- `0x009ADA6E` → [KeFindFirstSetRightGroupMask](../../text/25/KeFindFirstSetRightGroupMask_function_00256BE4.md) (function, `0x00256BE4`)
- `0x009ADAA0` → [KeClearBitGroupMask](../../text/46/KeClearBitGroupMask_function_00467898.md) (function, `0x00467898`)
- `0x009ADAAF` → [KeIsEmptyGroupMask](../../text/25/KeIsEmptyGroupMask_function_002553B0.md) (function, `0x002553B0`)
- `0x009ADAE0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009ADB25` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009ADB4E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009ADBCF` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009ADC72` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009ADCA9` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009ADCDF` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009ADD1D` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009ADD3E` → [PoQueryProcessEnergyTrackingState](../AA/PoQueryProcessEnergyTrackingState_function_00AAC8D0.md) (function, `0x00AAC8D0`)
- `0x009ADD5E` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009ADD95` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009ADDC9` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009ADDEC` → [PsQueryProcessEnergyValues](../91/PsQueryProcessEnergyValues_function_0091A4E0.md) (function, `0x0091A4E0`)
- `0x009ADE0A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009ADE66` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009ADE73` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x009ADE8C` → [PsGetEffectiveServerSilo](../../text/22/PsGetEffectiveServerSilo_function_002257F0.md) (function, `0x002257F0`)
- `0x009ADE94` → [PsGetSiloIdentifier](../A7/PsGetSiloIdentifier_function_00A7F480.md) (function, `0x00A7F480`)
- `0x009ADEA5` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009ADF07` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009ADF23` → [ObReferenceProcessHandleTable](../89/ObReferenceProcessHandleTable_function_00893B70.md) (function, `0x00893B70`)
- `0x009ADF85` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009ADFC8` → [ExUnlockUserBuffer](../../text/29/ExUnlockUserBuffer_function_0029F258.md) (function, `0x0029F258`)
- `0x009AE01C` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AE086` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AE0A2` → [ObReferenceProcessHandleTable](../89/ObReferenceProcessHandleTable_function_00893B70.md) (function, `0x00893B70`)
- `0x009AE111` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AE141` → [KeQueryCpuSetsProcess](../../text/4D/KeQueryCpuSetsProcess_function_004DE068.md) (function, `0x004DE068`)
- `0x009AE157` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AE188` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009AE1A6` → [PsIumGetOnDemandDebugChallenge](../AC/PsIumGetOnDemandDebugChallenge_function_00ACA8B4.md) (function, `0x00ACA8B4`)
- `0x009AE1DF` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AE22F` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AE29B` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AE2D5` → [VslLiveDumpCaptureProcess](../AA/VslLiveDumpCaptureProcess_function_00AA4C48.md) (function, `0x00AA4C48`)
- `0x009AE2E4` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AE31F` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009AE33A` → [EtwQueryProcessTelemetryCoverage](../70/EtwQueryProcessTelemetryCoverage_function_00701B8C.md) (function, `0x00701B8C`)
- `0x009AE3C9` → [ObOpenObjectByPointer](../8B/ObOpenObjectByPointer_function_008B7420.md) (function, `0x008B7420`)
- `0x009AE401` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009AE4EE` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009AE74B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x009AA263` → RVA `0x00E0A740` (`.data`; read)
- `0x009AA431` → RVA `0x00FC6A98` (`ALMOSTRO`; read)
- `0x009AA47B` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x009AAFEB` → RVA `0x00FC6AA0` (`ALMOSTRO`; read)
- `0x009AB419` → RVA `0x00FC6CA0` (`ALMOSTRO`; read)
- `0x009AC14B` → RVA `0x00F06570` (`.data`; read)
- `0x009AC5BE` → RVA `0x002A4000` (`PspHandleTableWalker`; read)
- `0x009AD81A` → RVA `0x00FC6AE0` (`ALMOSTRO`; read)
- `0x009AE3AD` → RVA `0x00FC6BD8` (`ALMOSTRO`; read)
- `0x009AE63B` → RVA `0x-31647EFC` (`image boundary/outside`; read/write)
- `0x009AE731` → RVA `0x47E12C88` (`image boundary/outside`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **116**
  - `0x009AA2E6` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009AA31C` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009AA391` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009AA3A4` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009AA516` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AA66A` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009AA68F` → [KeQueryAffinityProcess](../../text/2C/KeQueryAffinityProcess_function_002CE710.md) (`PAGE` → `.text`)
  - `0x009AA852` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AAC10` → [ExQueryHandleExceptionsPermanency](../../text/45/ExQueryHandleExceptionsPermanency_function_00458CE0.md) (`PAGE` → `.text`)
  - `0x009AAC50` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x009AAF81` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AB03B` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AB0E5` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AB202` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AB2B8` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x009AB2F7` → [MmQueryWorkingSetInformation](../../text/41/MmQueryWorkingSetInformation_function_0041CB20.md) (`PAGE` → `.text`)
  - `0x009AB30A` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x009AB3BC` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AB3DB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009AB420` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (`PAGE` → `.text`)
  - `0x009AB484` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x009AB4D2` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AB4DE` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (`PAGE` → `.text`)
  - `0x009AB562` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AB62F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AB658` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009AB6F1` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AB713` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009AB75E` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009AB792` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009AB7F4` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AB81E` → [KeTestBitGroupMask](../../text/43/KeTestBitGroupMask_function_00431330.md) (`PAGE` → `.text`)
  - `0x009AB8D2` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x009AB8EC` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x009AB9BF` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x009ABA23` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x009ABA8F` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x009ABA9C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009ABAF4` → [PsGetProcessSessionId](../../text/22/PsGetProcessSessionId_function_002233A0.md) (`PAGE` → `.text`)
  - `0x009ABB05` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009ABB81` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009ABB97` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x009ABBA7` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x009ABBB3` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x009ABC1C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009ABC60` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (`PAGE` → `.text`)
  - `0x009ABCBF` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009ABD20` → [BvgaSetVirtualFrameBuffer](../../text/4F/BvgaSetVirtualFrameBuffer_function_004FC600.md) (`PAGE` → `.text`)
  - `0x009ABD31` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009ABE10` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009ABEE0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009ABF8F` → [PsGetWin32KFilterSet](../../text/45/PsGetWin32KFilterSet_function_00458CC0.md) (`PAGE` → `.text`)
  - `0x009AC07B` → [MmQueryCommitReleaseState](../../text/48/MmQueryCommitReleaseState_function_004880B8.md) (`PAGE` → `.text`)
  - `0x009AC1C3` → [PsQueryProcessCommandLine](../../text/46/PsQueryProcessCommandLine_function_00469810.md) (`PAGE` → `.text`)
  - `0x009AC2D2` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x009AC2F2` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x009AC303` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x009AC395` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x009AC4B3` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AC5D4` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x009AC5E1` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AC5F4` → [ExUnlockUserBuffer](../../text/29/ExUnlockUserBuffer_function_0029F258.md) (`PAGE` → `.text`)
  - `0x009AC686` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AC6EF` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AC7AF` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AC8F5` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x009AC910` → [ZwQueryInformationJobObject](../../text/6A/ZwQueryInformationJobObject_function_006AFBB0.md) (`PAGE` → `.text`)
  - `0x009AC92C` → [ZwQueryInformationJobObject](../../text/6A/ZwQueryInformationJobObject_function_006AFBB0.md) (`PAGE` → `.text`)
  - `0x009AC93B` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x009ACC9A` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x009ACD2B` → [KeQuerySystemTimePrecise](../../text/37/KeQuerySystemTimePrecise_function_0037DA40.md) (`PAGE` → `.text`)
  - `0x009ACD3B` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`PAGE` → `.text`)
  - `0x009ACD46` → [ExGenRandom](../../text/41/ExGenRandom_function_0041B010.md) (`PAGE` → `.text`)
  - `0x009ACE71` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009ACEF9` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009ACF66` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AD008` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AD086` → [PspLockProcessShared](../../text/40/PspLockProcessShared_function_004016D0.md) (`PAGE` → `.text`)
  - `0x009AD141` → [PspUnlockProcessShared](../../text/26/PspUnlockProcessShared_function_00263950.md) (`PAGE` → `.text`)
  - `0x009AD1CB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009AD1F2` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AD3F9` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AD573` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AD5A2` → [ExAcquireFastMutex](../../text/20/ExAcquireFastMutex_function_0020E5A0.md) (`PAGE` → `.text`)
  - `0x009AD779` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (`PAGE` → `.text`)
  - `0x009AD795` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x009AD7A8` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x009AD7B0` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009AD876` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AD8A7` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009AD8AF` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009AD939` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AD998` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009AD9BD` → [KeQueryAffinityProcess](../../text/2C/KeQueryAffinityProcess_function_002CE710.md) (`PAGE` → `.text`)
  - `0x009ADA56` → [KeQueryGroupMaskProcess](../../text/48/KeQueryGroupMaskProcess_function_0048E804.md) (`PAGE` → `.text`)
  - `0x009ADA6E` → [KeFindFirstSetRightGroupMask](../../text/25/KeFindFirstSetRightGroupMask_function_00256BE4.md) (`PAGE` → `.text`)
  - `0x009ADAA0` → [KeClearBitGroupMask](../../text/46/KeClearBitGroupMask_function_00467898.md) (`PAGE` → `.text`)
  - `0x009ADAAF` → [KeIsEmptyGroupMask](../../text/25/KeIsEmptyGroupMask_function_002553B0.md) (`PAGE` → `.text`)
  - `0x009ADAE0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009ADB4E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009ADCA9` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009ADCDF` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009ADD5E` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009ADD95` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009ADE0A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009ADE73` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x009ADE8C` → [PsGetEffectiveServerSilo](../../text/22/PsGetEffectiveServerSilo_function_002257F0.md) (`PAGE` → `.text`)
  - `0x009ADEA5` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009ADFC8` → [ExUnlockUserBuffer](../../text/29/ExUnlockUserBuffer_function_0029F258.md) (`PAGE` → `.text`)
  - `0x009AE141` → [KeQueryCpuSetsProcess](../../text/4D/KeQueryCpuSetsProcess_function_004DE068.md) (`PAGE` → `.text`)
  - `0x009AE157` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AE188` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009AE2E4` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AE401` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009AE4EE` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009AE74B` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x009AE52D` → [sub_00B2D784 + 0x44](../B2/Unknown_function_00B2D784.md) (`tail-transfer`)
  - `0x009AE540` → [sub_00B2D784](../B2/Unknown_function_00B2D784.md) (`tail-transfer`)
  - `0x009AE549` → [sub_00B2D784](../B2/Unknown_function_00B2D784.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009AA250  40 53                           push rbx
009AA252  56                              push rsi
009AA253  57                              push rdi
009AA254  41 54                           push r12
009AA256  41 55                           push r13
009AA258  41 56                           push r14
009AA25A  41 57                           push r15
009AA25C  48 81 EC D0 09 00 00            sub rsp, 0x9d0
009AA263  48 8B 05 D6 04 46 00            mov rax, qword ptr [rip + 0x4604d6]
009AA26A  48 33 C4                        xor rax, rsp
009AA26D  48 89 84 24 C0 09 00 00         mov qword ptr [rsp + 0x9c0], rax
009AA275  45 8B F1                        mov r14d, r9d
009AA278  49 8B F0                        mov rsi, r8
009AA27B  48 63 FA                        movsxd rdi, edx
009AA27E  4C 8B F9                        mov r15, rcx
009AA281  4C 8B A4 24 30 0A 00 00         mov r12, qword ptr [rsp + 0xa30]
009AA289  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
009AA28E  4C 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], r8
009AA296  44 89 B4 24 D8 01 00 00         mov dword ptr [rsp + 0x1d8], r14d
009AA29E  4C 89 A4 24 30 01 00 00         mov qword ptr [rsp + 0x130], r12
009AA2A6  0F 57 C0                        xorps xmm0, xmm0
009AA2A9  0F 11 84 24 60 04 00 00         movups xmmword ptr [rsp + 0x460], xmm0
009AA2B1  0F 11 84 24 70 04 00 00         movups xmmword ptr [rsp + 0x470], xmm0
009AA2B9  0F 11 84 24 80 04 00 00         movups xmmword ptr [rsp + 0x480], xmm0
009AA2C1  33 DB                           xor ebx, ebx
009AA2C3  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
009AA2C7  48 89 9C 24 20 01 00 00         mov qword ptr [rsp + 0x120], rbx
009AA2CF  89 9C 24 EC 00 00 00            mov dword ptr [rsp + 0xec], ebx
009AA2D6  33 D2                           xor edx, edx
009AA2D8  41 B8 08 01 00 00               mov r8d, 0x108
009AA2DE  48 8D 8C 24 C0 04 00 00         lea rcx, [rsp + 0x4c0]
009AA2E6  E8 55 C9 D1 FF                  call 0x1406c6c40
009AA2EB  48 89 9C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rbx
009AA2F3  0F 57 C0                        xorps xmm0, xmm0
009AA2F6  0F 11 84 24 30 04 00 00         movups xmmword ptr [rsp + 0x430], xmm0
009AA2FE  89 9C 24 B8 01 00 00            mov dword ptr [rsp + 0x1b8], ebx
009AA305  89 9C 24 B4 01 00 00            mov dword ptr [rsp + 0x1b4], ebx
009AA30C  33 D2                           xor edx, edx
009AA30E  41 B8 98 00 00 00               mov r8d, 0x98
009AA314  48 8D 8C 24 D0 05 00 00         lea rcx, [rsp + 0x5d0]
009AA31C  E8 1F C9 D1 FF                  call 0x1406c6c40
009AA321  0F 57 C0                        xorps xmm0, xmm0
009AA324  0F 11 84 24 08 03 00 00         movups xmmword ptr [rsp + 0x308], xmm0
009AA32C  48 89 9C 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], rbx
009AA334  0F 57 C9                        xorps xmm1, xmm1
009AA337  33 C0                           xor eax, eax
009AA339  0F 11 8C 24 90 04 00 00         movups xmmword ptr [rsp + 0x490], xmm1
009AA341  0F 11 8C 24 A0 04 00 00         movups xmmword ptr [rsp + 0x4a0], xmm1
009AA349  48 89 84 24 B0 04 00 00         mov qword ptr [rsp + 0x4b0], rax
009AA351  48 89 9C 24 C8 01 00 00         mov qword ptr [rsp + 0x1c8], rbx
009AA359  48 89 9C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rbx
009AA361  66 89 5C 24 60                  mov word ptr [rsp + 0x60], bx
009AA366  66 89 9C 24 98 00 00 00         mov word ptr [rsp + 0x98], bx
009AA36E  48 89 5C 24 40                  mov qword ptr [rsp + 0x40], rbx
009AA373  48 89 9C 24 E8 01 00 00         mov qword ptr [rsp + 0x1e8], rbx
009AA37B  48 89 9C 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rbx
009AA383  33 D2                           xor edx, edx
009AA385  44 8D 43 68                     lea r8d, [rbx + 0x68]
009AA389  48 8D 8C 24 20 03 00 00         lea rcx, [rsp + 0x320]
009AA391  E8 AA C8 D1 FF                  call 0x1406c6c40
009AA396  33 D2                           xor edx, edx
009AA398  44 8D 43 70                     lea r8d, [rbx + 0x70]
009AA39C  48 8D 8C 24 40 01 00 00         lea rcx, [rsp + 0x140]
009AA3A4  E8 97 C8 D1 FF                  call 0x1406c6c40
009AA3A9  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009AA3B2  44 0F B6 A8 32 02 00 00         movzx r13d, byte ptr [rax + 0x232]
009AA3BA  44 88 6C 24 4C                  mov byte ptr [rsp + 0x4c], r13b
009AA3BF  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
009AA3C8  4C 89 94 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r10
009AA3D0  45 84 ED                        test r13b, r13b
009AA3D3  0F 85 86 04 00 00               jne 0x1409aa85f
009AA3D9  44 8D 4B 01                     lea r9d, [rbx + 1]
009AA3DD  48 C7 84 24 90 00 00 00 03 00 00 00  mov qword ptr [rsp + 0x90], 3
009AA3E9  49 B8 00 00 FF FF FF 7F 00 00   movabs r8, 0x7fffffff0000
009AA3F3  83 FF 34                        cmp edi, 0x34
009AA3F6  0F 85 29 01 00 00               jne 0x1409aa525
009AA3FC  89 9C 24 F0 00 00 00            mov dword ptr [rsp + 0xf0], ebx
009AA403  C6 44 24 4E 00                  mov byte ptr [rsp + 0x4e], 0
009AA408  C6 44 24 4F 00                  mov byte ptr [rsp + 0x4f], 0
009AA40D  41 83 FE 08                     cmp r14d, 8
009AA411  0F 85 8A 11 00 00               jne 0x1409ab5a1
009AA417  8B 3E                           mov edi, dword ptr [rsi]
009AA419  89 BC 24 B0 01 00 00            mov dword ptr [rsp + 0x1b0], edi
009AA420  EB 05                           jmp 0x1409aa427
009AA422  E9 19 43 00 00                  jmp 0x1409ae740
009AA427  49 83 FF FF                     cmp r15, -1
009AA42B  0F 84 80 05 00 00               je 0x1409aa9b1
009AA431  4C 8B 05 60 C6 61 00            mov r8, qword ptr [rip + 0x61c660]
009AA438  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AA43D  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AA442  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AA447  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AA44C  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AA454  45 0F B6 CD                     movzx r9d, r13b
009AA458  BA 00 10 00 00                  mov edx, 0x1000
009AA45D  49 8B CF                        mov rcx, r15
009AA460  E8 EB F1 EB FF                  call 0x140869650
009AA465  85 C0                           test eax, eax
009AA467  0F 88 D3 42 00 00               js 0x1409ae740
009AA46D  FF CF                           dec edi
009AA46F  83 FF 0F                        cmp edi, 0xf
009AA472  0F 87 CF 0B 00 00               ja 0x1409ab047
009AA478  48 63 C7                        movsxd rax, edi
009AA47B  48 8D 0D 7E 5B 65 FF            lea rcx, [rip - 0x9aa482]
009AA482  8B 84 81 68 E5 9A 00            mov eax, dword ptr [rcx + rax*4 + 0x9ae568]
009AA489  48 03 C1                        add rax, rcx
009AA48C  FF E0                           jmp rax
009AA48E  CC                              int3
009AA48F  CC                              int3
009AA490  CC                              int3
009AA491  CC                              int3
009AA492  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009AA496  89 5E 04                        mov dword ptr [rsi + 4], ebx
009AA499  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AA49E  8B 88 50 07 00 00               mov ecx, dword ptr [rax + 0x750]
009AA4A4  0F BA E1 08                     bt ecx, 8
009AA4A8  72 46                           jb 0x1409aa4f0
009AA4AA  0F BA E1 0B                     bt ecx, 0xb
009AA4AE  72 38                           jb 0x1409aa4e8
009AA4B0  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AA4B5  F7 80 50 07 00 00 00 02 00 00   test dword ptr [rax + 0x750], 0x200
009AA4BF  75 1C                           jne 0x1409aa4dd
009AA4C1  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AA4C6  F7 80 50 07 00 00 00 04 00 00   test dword ptr [rax + 0x750], 0x400
009AA4D0  74 29                           je 0x1409aa4fb
009AA4D2  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AA4D5  83 C8 04                        or eax, 4
009AA4D8  89 46 04                        mov dword ptr [rsi + 4], eax
009AA4DB  EB 1E                           jmp 0x1409aa4fb
009AA4DD  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AA4E0  83 C8 02                        or eax, 2
009AA4E3  89 46 04                        mov dword ptr [rsi + 4], eax
009AA4E6  EB D9                           jmp 0x1409aa4c1
009AA4E8  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AA4EB  83 C8 08                        or eax, 8
009AA4EE  EB 06                           jmp 0x1409aa4f6
009AA4F0  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AA4F3  83 C8 01                        or eax, 1
009AA4F6  89 46 04                        mov dword ptr [rsi + 4], eax
009AA4F9  EB B5                           jmp 0x1409aa4b0
009AA4FB  EB 09                           jmp 0x1409aa506
009AA4FD  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AA501  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
009AA506  49 83 FF FF                     cmp r15, -1
009AA50A  74 0F                           je 0x1409aa51b
009AA50C  BA 50 73 51 79                  mov edx, 0x79517350
009AA511  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AA516  E8 C5 D3 94 FF                  call 0x1402f78e0
009AA51B  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
009AA51F  E9 1C 42 00 00                  jmp 0x1409ae740
009AA524  CC                              int3
009AA525  83 FF 73                        cmp edi, 0x73
009AA528  0F 87 20 40 00 00               ja 0x1409ae54e
009AA52E  48 8D 0D CB 5A 65 FF            lea rcx, [rip - 0x9aa535]
009AA535  0F B6 84 39 CC E6 9A 00         movzx eax, byte ptr [rcx + rdi + 0x9ae6cc]
009AA53D  8B 94 81 A8 E5 9A 00            mov edx, dword ptr [rcx + rax*4 + 0x9ae5a8]
009AA544  48 03 D1                        add rdx, rcx
009AA547  FF E2                           jmp rdx
009AA549  CC                              int3
009AA54A  CC                              int3
009AA54B  CC                              int3
009AA54C  CC                              int3
009AA54D  C6 44 24 4D 00                  mov byte ptr [rsp + 0x4d], 0
009AA552  41 83 FE 40                     cmp r14d, 0x40
009AA556  0F 84 E1 17 00 00               je 0x1409abd3d
009AA55C  41 83 FE 30                     cmp r14d, 0x30
009AA560  0F 85 3B 10 00 00               jne 0x1409ab5a1
009AA566  48 89 9C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rbx
009AA56E  41 8B FE                        mov edi, r14d
009AA571  48 89 BC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdi
009AA579  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
009AA57D  48 89 B4 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rsi
009AA585  4C 8B 05 0C C5 61 00            mov r8, qword ptr [rip + 0x61c50c]
009AA58C  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AA591  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AA596  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AA59B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AA5A0  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AA5A8  45 0F B6 CD                     movzx r9d, r13b
009AA5AC  BA 00 10 00 00                  mov edx, 0x1000
009AA5B1  49 8B CF                        mov rcx, r15
009AA5B4  E8 97 F0 EB FF                  call 0x140869650
009AA5B9  44 8B F0                        mov r14d, eax
009AA5BC  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AA5C0  85 C0                           test eax, eax
009AA5C2  0F 88 78 41 00 00               js 0x1409ae740
009AA5C8  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009AA5CD  8B 87 54 05 00 00               mov eax, dword ptr [rdi + 0x554]
009AA5D3  89 06                           mov dword ptr [rsi], eax
009AA5D5  48 8D 56 08                     lea rdx, [rsi + 8]
009AA5D9  48 8B 87 E0 02 00 00            mov rax, qword ptr [rdi + 0x2e0]
009AA5E0  48 89 02                        mov qword ptr [rdx], rax
009AA5E3  F6 87 70 01 00 00 01            test byte ptr [rdi + 0x170], 1
009AA5EA  74 08                           je 0x1409aa5f4
009AA5EC  48 8B CF                        mov rcx, rdi
009AA5EF  E8 70 75 0C 00                  call 0x140a71b64
009AA5F4  EB 36                           jmp 0x1409aa62c
009AA5F6  44 8B F0                        mov r14d, eax
009AA5F9  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AA5FD  33 DB                           xor ebx, ebx
009AA5FF  48 C7 84 24 90 00 00 00 03 00 00 00  mov qword ptr [rsp + 0x90], 3
009AA60B  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009AA610  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
009AA618  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
009AA61C  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
009AA624  4C 8B A4 24 30 01 00 00         mov r12, qword ptr [rsp + 0x130]
009AA62C  45 85 F6                        test r14d, r14d
009AA62F  0F 88 15 02 00 00               js 0x1409aa84a
009AA635  4C 8B FB                        mov r15, rbx
009AA638  F7 87 88 00 00 00 00 10 00 00   test dword ptr [rdi + 0x88], 0x1000
009AA642  0F 85 F5 11 00 00               jne 0x1409ab83d
009AA648  41 BD 01 00 00 00               mov r13d, 1
009AA64E  48 C7 84 24 C0 04 00 00 01 00 20 00  mov qword ptr [rsp + 0x4c0], 0x200001
009AA65A  33 D2                           xor edx, edx
009AA65C  41 B8 00 01 00 00               mov r8d, 0x100
009AA662  48 8D 8C 24 C8 04 00 00         lea rcx, [rsp + 0x4c8]
009AA66A  E8 D1 C5 D1 FF                  call 0x1406c6c40
009AA66F  48 8D 44 24 60                  lea rax, [rsp + 0x60]
009AA674  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009AA679  45 33 C9                        xor r9d, r9d
009AA67C  4C 8D 84 24 30 04 00 00         lea r8, [rsp + 0x430]
009AA684  48 8D 94 24 C0 04 00 00         lea rdx, [rsp + 0x4c0]
009AA68C  48 8B CF                        mov rcx, rdi
009AA68F  E8 7C 40 92 FF                  call 0x1402ce710
009AA694  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
009AA69C  48 3B B8 20 02 00 00            cmp rdi, qword ptr [rax + 0x220]
009AA6A3  0F 84 66 11 00 00               je 0x1409ab80f
009AA6A9  0F B7 54 24 60                  movzx edx, word ptr [rsp + 0x60]
009AA6AE  66 83 FA 20                     cmp dx, 0x20
009AA6B2  74 0B                           je 0x1409aa6bf
009AA6B4  0F B7 C2                        movzx eax, dx
009AA6B7  4C 8B BC C4 C8 04 00 00         mov r15, qword ptr [rsp + rax*8 + 0x4c8]
009AA6BF  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
009AA6C7  48 85 D2                        test rdx, rdx
009AA6CA  0F 85 6C 15 00 00               jne 0x1409abc3c
009AA6D0  4C 89 7E 10                     mov qword ptr [rsi + 0x10], r15
009AA6D4  0F BE 87 90 00 00 00            movsx eax, byte ptr [rdi + 0x90]
009AA6DB  89 46 18                        mov dword ptr [rsi + 0x18], eax
009AA6DE  48 8B 87 D0 01 00 00            mov rax, qword ptr [rdi + 0x1d0]
009AA6E5  48 89 46 20                     mov qword ptr [rsi + 0x20], rax
009AA6E9  48 8B 87 D0 02 00 00            mov rax, qword ptr [rdi + 0x2d0]
009AA6F0  48 89 46 28                     mov qword ptr [rsi + 0x28], rax
009AA6F4  48 85 D2                        test rdx, rdx
009AA6F7  0F 84 EF 00 00 00               je 0x1409aa7ec
009AA6FD  89 5A 38                        mov dword ptr [rdx + 0x38], ebx
009AA700  F6 87 FA 05 00 00 07            test byte ptr [rdi + 0x5fa], 7
009AA707  0F 86 F2 00 00 00               jbe 0x1409aa7ff
009AA70D  44 89 6A 38                     mov dword ptr [rdx + 0x38], r13d
009AA711  48 83 BF 10 03 00 00 00         cmp qword ptr [rdi + 0x310], 0
009AA719  0F 85 F0 00 00 00               jne 0x1409aa80f
009AA71F  8B 87 F4 01 00 00               mov eax, dword ptr [rdi + 0x1f4]
009AA725  A9 08 00 00 40                  test eax, 0x40000008
009AA72A  74 09                           je 0x1409aa735
009AA72C  8B 42 38                        mov eax, dword ptr [rdx + 0x38]
009AA72F  83 C8 04                        or eax, 4
009AA732  89 42 38                        mov dword ptr [rdx + 0x38], eax
009AA735  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
009AA73A  41 8B 88 F0 01 00 00            mov ecx, dword ptr [r8 + 0x1f0]
009AA741  C1 E9 04                        shr ecx, 4
009AA744  83 E1 08                        and ecx, 8
009AA747  8B 42 38                        mov eax, dword ptr [rdx + 0x38]
009AA74A  83 E0 F7                        and eax, 0xfffffff7
009AA74D  0B C8                           or ecx, eax
009AA74F  89 4A 38                        mov dword ptr [rdx + 0x38], ecx
009AA752  41 8B 80 88 00 00 00            mov eax, dword ptr [r8 + 0x88]
009AA759  C1 E8 03                        shr eax, 3
009AA75C  83 E0 01                        and eax, 1
009AA75F  41 03 80 50 01 00 00            add eax, dword ptr [r8 + 0x150]
009AA766  74 06                           je 0x1409aa76e
009AA768  83 C9 10                        or ecx, 0x10
009AA76B  89 4A 38                        mov dword ptr [rdx + 0x38], ecx
009AA76E  49 8B 80 A0 02 00 00            mov rax, qword ptr [r8 + 0x2a0]
009AA775  48 85 C0                        test rax, rax
009AA778  74 1E                           je 0x1409aa798
009AA77A  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AA77F  48 8B 88 A0 02 00 00            mov rcx, qword ptr [rax + 0x2a0]
009AA786  83 B9 30 04 00 00 00            cmp dword ptr [rcx + 0x430], 0
009AA78D  76 09                           jbe 0x1409aa798
009AA78F  8B 42 38                        mov eax, dword ptr [rdx + 0x38]
009AA792  83 C8 20                        or eax, 0x20
009AA795  89 42 38                        mov dword ptr [rdx + 0x38], eax
009AA798  80 7C 24 4D 00                  cmp byte ptr [rsp + 0x4d], 0
009AA79D  74 09                           je 0x1409aa7a8
009AA79F  8B 42 38                        mov eax, dword ptr [rdx + 0x38]
009AA7A2  83 C8 40                        or eax, 0x40
009AA7A5  89 42 38                        mov dword ptr [rdx + 0x38], eax
009AA7A8  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009AA7AD  F6 87 70 01 00 00 01            test byte ptr [rdi + 0x170], 1
009AA7B4  74 0A                           je 0x1409aa7c0
009AA7B6  8B 42 38                        mov eax, dword ptr [rdx + 0x38]
009AA7B9  0F BA E8 07                     bts eax, 7
009AA7BD  89 42 38                        mov dword ptr [rdx + 0x38], eax
009AA7C0  F6 87 70 01 00 00 02            test byte ptr [rdi + 0x170], 2
009AA7C7  74 0A                           je 0x1409aa7d3
009AA7C9  8B 42 38                        mov eax, dword ptr [rdx + 0x38]
009AA7CC  0F BA E8 09                     bts eax, 9
009AA7D0  89 42 38                        mov dword ptr [rdx + 0x38], eax
009AA7D3  48 83 BF 40 06 00 00 00         cmp qword ptr [rdi + 0x640], 0
009AA7DB  74 0A                           je 0x1409aa7e7
009AA7DD  8B 42 38                        mov eax, dword ptr [rdx + 0x38]
009AA7E0  0F BA E8 08                     bts eax, 8
009AA7E4  89 42 38                        mov dword ptr [rdx + 0x38], eax
009AA7E7  44 8B 74 24 48                  mov r14d, dword ptr [rsp + 0x48]
009AA7EC  4D 85 E4                        test r12, r12
009AA7EF  74 4F                           je 0x1409aa840
009AA7F1  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
009AA7F9  41 89 04 24                     mov dword ptr [r12], eax
009AA7FD  EB 41                           jmp 0x1409aa840
009AA7FF  C7 84 24 90 00 00 00 02 00 00 00  mov dword ptr [rsp + 0x90], 2
009AA80A  E9 02 FF FF FF                  jmp 0x1409aa711
009AA80F  0F B7 87 EC 06 00 00            movzx eax, word ptr [rdi + 0x6ec]
009AA816  B9 4C 01 00 00                  mov ecx, 0x14c
009AA81B  66 3B C1                        cmp ax, cx
009AA81E  75 10                           jne 0x1409aa830
009AA820  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
009AA828  89 42 38                        mov dword ptr [rdx + 0x38], eax
009AA82B  E9 EF FE FF FF                  jmp 0x1409aa71f
009AA830  B9 C4 01 00 00                  mov ecx, 0x1c4
009AA835  66 3B C1                        cmp ax, cx
009AA838  0F 85 E1 FE FF FF               jne 0x1409aa71f
009AA83E  EB E0                           jmp 0x1409aa820
009AA840  EB 08                           jmp 0x1409aa84a
009AA842  44 8B F0                        mov r14d, eax
009AA845  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009AA84A  BA 50 73 51 79                  mov edx, 0x79517350
009AA84F  48 8B CF                        mov rcx, rdi
009AA852  E8 89 D0 94 FF                  call 0x1402f78e0
009AA857  41 8B C6                        mov eax, r14d
009AA85A  E9 E1 3E 00 00                  jmp 0x1409ae740
009AA85F  83 FF 12                        cmp edi, 0x12
009AA862  0F 84 D0 00 00 00               je 0x1409aa938
009AA868  83 FF 3D                        cmp edi, 0x3d
009AA86B  0F 84 C7 00 00 00               je 0x1409aa938
009AA871  83 FF 41                        cmp edi, 0x41
009AA874  0F 84 11 01 00 00               je 0x1409aa98b
009AA87A  8D 47 BA                        lea eax, [rdi - 0x46]
009AA87D  A9 FB FF FF FF                  test eax, 0xfffffffb
009AA882  0F 84 B0 00 00 00               je 0x1409aa938
009AA888  83 FF 5C                        cmp edi, 0x5c
009AA88B  0F 84 DE 00 00 00               je 0x1409aa96f
009AA891  83 FF 5E                        cmp edi, 0x5e
009AA894  0F 84 85 00 00 00               je 0x1409aa91f
009AA89A  83 FF 57                        cmp edi, 0x57
009AA89D  0F 84 95 00 00 00               je 0x1409aa938
009AA8A3  83 FF 2F                        cmp edi, 0x2f
009AA8A6  0F 84 A3 00 00 00               je 0x1409aa94f
009AA8AC  41 B9 03 00 00 00               mov r9d, 3
009AA8B2  4C 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], r9
009AA8BA  41 8B C1                        mov eax, r9d
009AA8BD  B9 07 00 00 00                  mov ecx, 7
009AA8C2  83 FF 73                        cmp edi, 0x73
009AA8C5  0F 44 C1                        cmove eax, ecx
009AA8C8  8B C8                           mov ecx, eax
009AA8CA  41 B9 01 00 00 00               mov r9d, 1
009AA8D0  45 85 F6                        test r14d, r14d
009AA8D3  74 39                           je 0x1409aa90e
009AA8D5  48 85 F1                        test rcx, rsi
009AA8D8  75 40                           jne 0x1409aa91a
009AA8DA  4A 8D 0C 36                     lea rcx, [rsi + r14]
009AA8DE  49 B8 00 00 FF FF FF 7F 00 00   movabs r8, 0x7fffffff0000
009AA8E8  49 3B C8                        cmp rcx, r8
009AA8EB  77 7C                           ja 0x1409aa969
009AA8ED  48 3B CE                        cmp rcx, rsi
009AA8F0  72 77                           jb 0x1409aa969
009AA8F2  4D 85 E4                        test r12, r12
009AA8F5  0F 84 AC 00 00 00               je 0x1409aa9a7
009AA8FB  49 8B C8                        mov rcx, r8
009AA8FE  4D 3B E0                        cmp r12, r8
009AA901  49 0F 42 CC                     cmovb rcx, r12
009AA905  8B 01                           mov eax, dword ptr [rcx]
009AA907  89 01                           mov dword ptr [rcx], eax
009AA909  E9 99 00 00 00                  jmp 0x1409aa9a7
009AA90E  49 B8 00 00 FF FF FF 7F 00 00   movabs r8, 0x7fffffff0000
009AA918  EB D8                           jmp 0x1409aa8f2
009AA91A  E8 B1 F6 EE FF                  call 0x140899fd0
009AA91F  B9 07 00 00 00                  mov ecx, 7
009AA924  41 B9 01 00 00 00               mov r9d, 1
009AA92A  48 C7 84 24 90 00 00 00 03 00 00 00  mov qword ptr [rsp + 0x90], 3
009AA936  EB 98                           jmp 0x1409aa8d0
009AA938  48 8B CB                        mov rcx, rbx
009AA93B  41 B9 01 00 00 00               mov r9d, 1
009AA941  48 C7 84 24 90 00 00 00 03 00 00 00  mov qword ptr [rsp + 0x90], 3
009AA94D  EB 81                           jmp 0x1409aa8d0
009AA94F  41 B9 01 00 00 00               mov r9d, 1
009AA955  41 8B C9                        mov ecx, r9d
009AA958  48 C7 84 24 90 00 00 00 03 00 00 00  mov qword ptr [rsp + 0x90], 3
009AA964  E9 67 FF FF FF                  jmp 0x1409aa8d0
009AA969  41 0F B6 00                     movzx eax, byte ptr [r8]
009AA96D  EB 83                           jmp 0x1409aa8f2
009AA96F  B9 07 00 00 00                  mov ecx, 7
009AA974  41 B9 01 00 00 00               mov r9d, 1
009AA97A  48 C7 84 24 90 00 00 00 03 00 00 00  mov qword ptr [rsp + 0x90], 3
009AA986  E9 45 FF FF FF                  jmp 0x1409aa8d0
009AA98B  B9 07 00 00 00                  mov ecx, 7
009AA990  41 B9 01 00 00 00               mov r9d, 1
009AA996  48 C7 84 24 90 00 00 00 03 00 00 00  mov qword ptr [rsp + 0x90], 3
009AA9A2  E9 29 FF FF FF                  jmp 0x1409aa8d0
009AA9A7  E9 47 FA FF FF                  jmp 0x1409aa3f3
009AA9AC  E9 8F 3D 00 00                  jmp 0x1409ae740
009AA9B1  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009AA9BA  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
009AA9C1  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
009AA9C6  8B BC 24 B0 01 00 00            mov edi, dword ptr [rsp + 0x1b0]
009AA9CD  E9 9B FA FF FF                  jmp 0x1409aa46d
009AA9D2  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009AA9D6  89 5E 04                        mov dword ptr [rsi + 4], ebx
009AA9D9  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AA9DE  8B 88 50 07 00 00               mov ecx, dword ptr [rax + 0x750]
009AA9E4  F6 C1 01                        test cl, 1
009AA9E7  74 09                           je 0x1409aa9f2
009AA9E9  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AA9EC  83 C8 01                        or eax, 1
009AA9EF  89 46 04                        mov dword ptr [rsi + 4], eax
009AA9F2  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AA9F7  8B 88 50 07 00 00               mov ecx, dword ptr [rax + 0x750]
009AA9FD  F6 C1 02                        test cl, 2
009AAA00  75 1B                           jne 0x1409aaa1d
009AAA02  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AAA07  8B 88 50 07 00 00               mov ecx, dword ptr [rax + 0x750]
009AAA0D  F6 C1 04                        test cl, 4
009AAA10  74 16                           je 0x1409aaa28
009AAA12  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAA15  83 C8 04                        or eax, 4
009AAA18  89 46 04                        mov dword ptr [rsi + 4], eax
009AAA1B  EB 0B                           jmp 0x1409aaa28
009AAA1D  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAA20  83 C8 02                        or eax, 2
009AAA23  89 46 04                        mov dword ptr [rsi + 4], eax
009AAA26  EB DA                           jmp 0x1409aaa02
009AAA28  E9 D9 FA FF FF                  jmp 0x1409aa506
009AAA2D  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AAA31  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
009AAA36  E9 CB FA FF FF                  jmp 0x1409aa506
009AAA3B  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009AAA3F  89 5E 04                        mov dword ptr [rsi + 4], ebx
009AAA42  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AAA47  8B 88 54 07 00 00               mov ecx, dword ptr [rax + 0x754]
009AAA4D  F6 C1 01                        test cl, 1
009AAA50  74 09                           je 0x1409aaa5b
009AAA52  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAA55  83 C8 01                        or eax, 1
009AAA58  89 46 04                        mov dword ptr [rsi + 4], eax
009AAA5B  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AAA60  8B 88 54 07 00 00               mov ecx, dword ptr [rax + 0x754]
009AAA66  F6 C1 04                        test cl, 4
009AAA69  0F 85 DA 00 00 00               jne 0x1409aab49
009AAA6F  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AAA74  F7 80 54 07 00 00 00 04 00 00   test dword ptr [rax + 0x754], 0x400
009AAA7E  0F 85 D3 00 00 00               jne 0x1409aab57
009AAA84  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AAA89  8B 88 54 07 00 00               mov ecx, dword ptr [rax + 0x754]
009AAA8F  F6 C1 10                        test cl, 0x10
009AAA92  0F 85 CD 00 00 00               jne 0x1409aab65
009AAA98  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AAA9D  8B 88 54 07 00 00               mov ecx, dword ptr [rax + 0x754]
009AAAA3  F6 C1 40                        test cl, 0x40
009AAAA6  0F 85 C7 00 00 00               jne 0x1409aab73
009AAAAC  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AAAB1  F7 80 54 07 00 00 00 01 00 00   test dword ptr [rax + 0x754], 0x100
009AAABB  0F 85 C1 00 00 00               jne 0x1409aab82
009AAAC1  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AAAC6  8B 88 54 07 00 00               mov ecx, dword ptr [rax + 0x754]
009AAACC  F6 C1 02                        test cl, 2
009AAACF  0F 85 BC 00 00 00               jne 0x1409aab91
009AAAD5  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AAADA  8B 88 54 07 00 00               mov ecx, dword ptr [rax + 0x754]
009AAAE0  F6 C1 08                        test cl, 8
009AAAE3  0F 85 B6 00 00 00               jne 0x1409aab9f
009AAAE9  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AAAEE  F7 80 54 07 00 00 00 08 00 00   test dword ptr [rax + 0x754], 0x800
009AAAF8  0F 85 AF 00 00 00               jne 0x1409aabad
009AAAFE  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AAB03  8B 88 54 07 00 00               mov ecx, dword ptr [rax + 0x754]
009AAB09  F6 C1 20                        test cl, 0x20
009AAB0C  0F 85 A9 00 00 00               jne 0x1409aabbb
009AAB12  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AAB17  8B 88 54 07 00 00               mov ecx, dword ptr [rax + 0x754]
009AAB1D  84 C9                           test cl, cl
009AAB1F  0F 88 A5 00 00 00               js 0x1409aabca
009AAB25  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AAB2A  F7 80 54 07 00 00 00 02 00 00   test dword ptr [rax + 0x754], 0x200
009AAB34  0F 84 9F 00 00 00               je 0x1409aabd9
009AAB3A  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAB3D  0F BA E8 0B                     bts eax, 0xb
009AAB41  89 46 04                        mov dword ptr [rsi + 4], eax
009AAB44  E9 90 00 00 00                  jmp 0x1409aabd9
009AAB49  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAB4C  83 C8 04                        or eax, 4
009AAB4F  89 46 04                        mov dword ptr [rsi + 4], eax
009AAB52  E9 18 FF FF FF                  jmp 0x1409aaa6f
009AAB57  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAB5A  83 C8 10                        or eax, 0x10
009AAB5D  89 46 04                        mov dword ptr [rsi + 4], eax
009AAB60  E9 1F FF FF FF                  jmp 0x1409aaa84
009AAB65  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAB68  83 C8 40                        or eax, 0x40
009AAB6B  89 46 04                        mov dword ptr [rsi + 4], eax
009AAB6E  E9 25 FF FF FF                  jmp 0x1409aaa98
009AAB73  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAB76  0F BA E8 08                     bts eax, 8
009AAB7A  89 46 04                        mov dword ptr [rsi + 4], eax
009AAB7D  E9 2A FF FF FF                  jmp 0x1409aaaac
009AAB82  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAB85  0F BA E8 0A                     bts eax, 0xa
009AAB89  89 46 04                        mov dword ptr [rsi + 4], eax
009AAB8C  E9 30 FF FF FF                  jmp 0x1409aaac1
009AAB91  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAB94  83 C8 02                        or eax, 2
009AAB97  89 46 04                        mov dword ptr [rsi + 4], eax
009AAB9A  E9 36 FF FF FF                  jmp 0x1409aaad5
009AAB9F  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AABA2  83 C8 08                        or eax, 8
009AABA5  89 46 04                        mov dword ptr [rsi + 4], eax
009AABA8  E9 3C FF FF FF                  jmp 0x1409aaae9
009AABAD  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AABB0  83 C8 20                        or eax, 0x20
009AABB3  89 46 04                        mov dword ptr [rsi + 4], eax
009AABB6  E9 43 FF FF FF                  jmp 0x1409aaafe
009AABBB  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AABBE  0F BA E8 07                     bts eax, 7
009AABC2  89 46 04                        mov dword ptr [rsi + 4], eax
009AABC5  E9 48 FF FF FF                  jmp 0x1409aab12
009AABCA  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AABCD  0F BA E8 09                     bts eax, 9
009AABD1  89 46 04                        mov dword ptr [rsi + 4], eax
009AABD4  E9 4C FF FF FF                  jmp 0x1409aab25
009AABD9  E9 28 F9 FF FF                  jmp 0x1409aa506
009AABDE  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AABE2  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
009AABE7  E9 1A F9 FF FF                  jmp 0x1409aa506
009AABEC  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009AABF0  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AABF5  E8 76 8F EE FF                  call 0x140893b70
009AABFA  48 85 C0                        test rax, rax
009AABFD  0F 84 6A 10 00 00               je 0x1409abc6d
009AAC03  4C 8D 44 24 4F                  lea r8, [rsp + 0x4f]
009AAC08  48 8D 54 24 4E                  lea rdx, [rsp + 0x4e]
009AAC0D  48 8B C8                        mov rcx, rax
009AAC10  E8 CB E0 AA FF                  call 0x140458ce0
009AAC15  90                              nop
009AAC16  89 5E 04                        mov dword ptr [rsi + 4], ebx
009AAC19  80 7C 24 4E 00                  cmp byte ptr [rsp + 0x4e], 0
009AAC1E  74 09                           je 0x1409aac29
009AAC20  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAC23  83 C8 01                        or eax, 1
009AAC26  89 46 04                        mov dword ptr [rsi + 4], eax
009AAC29  80 7C 24 4F 00                  cmp byte ptr [rsp + 0x4f], 0
009AAC2E  74 09                           je 0x1409aac39
009AAC30  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAC33  83 C8 02                        or eax, 2
009AAC36  89 46 04                        mov dword ptr [rsi + 4], eax
009AAC39  EB 09                           jmp 0x1409aac44
009AAC3B  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AAC3F  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
009AAC44  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AAC49  48 81 C1 E8 01 00 00            add rcx, 0x1e8
009AAC50  E8 2B F2 99 FF                  call 0x140349e80
009AAC55  E9 AC F8 FF FF                  jmp 0x1409aa506
009AAC5A  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009AAC5E  89 5E 04                        mov dword ptr [rsi + 4], ebx
009AAC61  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AAC66  8B 88 50 07 00 00               mov ecx, dword ptr [rax + 0x750]
009AAC6C  F6 C1 40                        test cl, 0x40
009AAC6F  75 09                           jne 0x1409aac7a
009AAC71  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAC74  83 C8 01                        or eax, 1
009AAC77  89 46 04                        mov dword ptr [rsi + 4], eax
009AAC7A  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AAC7F  8B 88 50 07 00 00               mov ecx, dword ptr [rax + 0x750]
009AAC85  F6 C1 10                        test cl, 0x10
009AAC88  74 09                           je 0x1409aac93
009AAC8A  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAC8D  83 C8 02                        or eax, 2
009AAC90  89 46 04                        mov dword ptr [rsi + 4], eax
009AAC93  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AAC98  8B 88 50 07 00 00               mov ecx, dword ptr [rax + 0x750]
009AAC9E  F6 C1 20                        test cl, 0x20
009AACA1  74 09                           je 0x1409aacac
009AACA3  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AACA6  83 C8 04                        or eax, 4
009AACA9  89 46 04                        mov dword ptr [rsi + 4], eax
009AACAC  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AACB1  8B 88 50 07 00 00               mov ecx, dword ptr [rax + 0x750]
009AACB7  F6 C1 08                        test cl, 8
009AACBA  74 09                           je 0x1409aacc5
009AACBC  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AACBF  83 C8 08                        or eax, 8
009AACC2  89 46 04                        mov dword ptr [rsi + 4], eax
009AACC5  E9 3C F8 FF FF                  jmp 0x1409aa506
009AACCA  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AACCE  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
009AACD3  E9 2E F8 FF FF                  jmp 0x1409aa506
009AACD8  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009AACDC  89 5E 04                        mov dword ptr [rsi + 4], ebx
009AACDF  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AACE4  8B 88 50 07 00 00               mov ecx, dword ptr [rax + 0x750]
009AACEA  0F BA E1 0C                     bt ecx, 0xc
009AACEE  72 36                           jb 0x1409aad26
009AACF0  0F BA E1 0D                     bt ecx, 0xd
009AACF4  72 28                           jb 0x1409aad1e
009AACF6  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AACFB  8B 88 D8 07 00 00               mov ecx, dword ptr [rax + 0x7d8]
009AAD01  F6 C1 02                        test cl, 2
009AAD04  75 0D                           jne 0x1409aad13
009AAD06  F6 C1 04                        test cl, 4
009AAD09  74 26                           je 0x1409aad31
009AAD0B  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAD0E  83 C8 08                        or eax, 8
009AAD11  EB 06                           jmp 0x1409aad19
009AAD13  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAD16  83 C8 04                        or eax, 4
009AAD19  89 46 04                        mov dword ptr [rsi + 4], eax
009AAD1C  EB 13                           jmp 0x1409aad31
009AAD1E  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAD21  83 C8 02                        or eax, 2
009AAD24  EB 06                           jmp 0x1409aad2c
009AAD26  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAD29  83 C8 01                        or eax, 1
009AAD2C  89 46 04                        mov dword ptr [rsi + 4], eax
009AAD2F  EB C5                           jmp 0x1409aacf6
009AAD31  E9 D0 F7 FF FF                  jmp 0x1409aa506
009AAD36  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AAD3A  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
009AAD3F  E9 C2 F7 FF FF                  jmp 0x1409aa506
009AAD44  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009AAD48  89 5E 04                        mov dword ptr [rsi + 4], ebx
009AAD4B  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AAD50  8B 88 50 07 00 00               mov ecx, dword ptr [rax + 0x750]
009AAD56  0F BA E1 13                     bt ecx, 0x13
009AAD5A  72 4C                           jb 0x1409aada8
009AAD5C  0F BA E1 14                     bt ecx, 0x14
009AAD60  72 3E                           jb 0x1409aada0
009AAD62  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AAD67  8B 88 50 07 00 00               mov ecx, dword ptr [rax + 0x750]
009AAD6D  0F BA E1 15                     bt ecx, 0x15
009AAD71  72 22                           jb 0x1409aad95
009AAD73  0F BA E1 16                     bt ecx, 0x16
009AAD77  72 3A                           jb 0x1409aadb3
009AAD79  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AAD7E  F7 80 50 07 00 00 00 00 04 00   test dword ptr [rax + 0x750], 0x40000
009AAD88  74 31                           je 0x1409aadbb
009AAD8A  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAD8D  83 C8 04                        or eax, 4
009AAD90  89 46 04                        mov dword ptr [rsi + 4], eax
009AAD93  EB 26                           jmp 0x1409aadbb
009AAD95  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAD98  83 C8 02                        or eax, 2
009AAD9B  89 46 04                        mov dword ptr [rsi + 4], eax
009AAD9E  EB D9                           jmp 0x1409aad79
009AADA0  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AADA3  83 C8 08                        or eax, 8
009AADA6  EB 06                           jmp 0x1409aadae
009AADA8  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AADAB  83 C8 01                        or eax, 1
009AADAE  89 46 04                        mov dword ptr [rsi + 4], eax
009AADB1  EB AF                           jmp 0x1409aad62
009AADB3  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AADB6  83 C8 10                        or eax, 0x10
009AADB9  EB E0                           jmp 0x1409aad9b
009AADBB  E9 46 F7 FF FF                  jmp 0x1409aa506
009AADC0  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AADC4  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
009AADC9  E9 38 F7 FF FF                  jmp 0x1409aa506
009AADCE  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009AADD2  89 5E 04                        mov dword ptr [rsi + 4], ebx
009AADD5  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AADDA  8B 88 50 07 00 00               mov ecx, dword ptr [rax + 0x750]
009AADE0  84 C9                           test cl, cl
009AADE2  79 09                           jns 0x1409aaded
009AADE4  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AADE7  83 C8 01                        or eax, 1
009AADEA  89 46 04                        mov dword ptr [rsi + 4], eax
009AADED  E9 14 F7 FF FF                  jmp 0x1409aa506
009AADF2  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AADF6  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
009AADFB  E9 06 F7 FF FF                  jmp 0x1409aa506
009AAE00  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009AAE04  48 8D 94 24 F0 00 00 00         lea rdx, [rsp + 0xf0]
009AAE0C  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AAE11  E8 4A 68 06 00                  call 0x140a11660
009AAE16  90                              nop
009AAE17  8B 84 24 F0 00 00 00            mov eax, dword ptr [rsp + 0xf0]
009AAE1E  89 46 04                        mov dword ptr [rsi + 4], eax
009AAE21  E9 E0 F6 FF FF                  jmp 0x1409aa506
009AAE26  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AAE2A  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
009AAE2F  E9 D2 F6 FF FF                  jmp 0x1409aa506
009AAE34  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009AAE38  89 5E 04                        mov dword ptr [rsi + 4], ebx
009AAE3B  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AAE40  8B 88 50 07 00 00               mov ecx, dword ptr [rax + 0x750]
009AAE46  0F BA E1 10                     bt ecx, 0x10
009AAE4A  72 11                           jb 0x1409aae5d
009AAE4C  0F BA E1 11                     bt ecx, 0x11
009AAE50  73 14                           jae 0x1409aae66
009AAE52  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAE55  83 C8 02                        or eax, 2
009AAE58  89 46 04                        mov dword ptr [rsi + 4], eax
009AAE5B  EB 09                           jmp 0x1409aae66
009AAE5D  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAE60  83 C8 01                        or eax, 1
009AAE63  89 46 04                        mov dword ptr [rsi + 4], eax
009AAE66  E9 9B F6 FF FF                  jmp 0x1409aa506
009AAE6B  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AAE6F  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
009AAE74  E9 8D F6 FF FF                  jmp 0x1409aa506
009AAE79  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009AAE7D  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AAE82  E8 31 C4 06 00                  call 0x140a172b8
009AAE87  90                              nop
009AAE88  89 5E 04                        mov dword ptr [rsi + 4], ebx
009AAE8B  83 E8 01                        sub eax, 1
009AAE8E  74 1E                           je 0x1409aaeae
009AAE90  83 E8 01                        sub eax, 1
009AAE93  74 10                           je 0x1409aaea5
009AAE95  83 F8 01                        cmp eax, 1
009AAE98  75 1D                           jne 0x1409aaeb7
009AAE9A  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAE9D  83 C8 02                        or eax, 2
009AAEA0  89 46 04                        mov dword ptr [rsi + 4], eax
009AAEA3  EB 12                           jmp 0x1409aaeb7
009AAEA5  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAEA8  83 C8 04                        or eax, 4
009AAEAB  89 46 04                        mov dword ptr [rsi + 4], eax
009AAEAE  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AAEB1  83 C8 01                        or eax, 1
009AAEB4  89 46 04                        mov dword ptr [rsi + 4], eax
009AAEB7  E9 4A F6 FF FF                  jmp 0x1409aa506
009AAEBC  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AAEC0  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
009AAEC5  E9 3C F6 FF FF                  jmp 0x1409aa506
009AAECA  41 83 FE 04                     cmp r14d, 4
009AAECE  0F 85 CD 06 00 00               jne 0x1409ab5a1
009AAED4  C7 84 24 40 01 00 00 10 00 00 00  mov dword ptr [rsp + 0x140], 0x10
009AAEDF  C7 06 10 00 00 00               mov dword ptr [rsi], 0x10
009AAEE5  4D 85 E4                        test r12, r12
009AAEE8  74 04                           je 0x1409aaeee
009AAEEA  45 89 34 24                     mov dword ptr [r12], r14d
009AAEEE  EB 05                           jmp 0x1409aaef5
009AAEF0  E9 4B 38 00 00                  jmp 0x1409ae740
009AAEF5  33 C0                           xor eax, eax
009AAEF7  E9 44 38 00 00                  jmp 0x1409ae740
009AAEFC  45 84 ED                        test r13b, r13b
009AAEFF  0F 85 81 0C 00 00               jne 0x1409abb86
009AAF05  41 83 FE 30                     cmp r14d, 0x30
009AAF09  0F 85 92 06 00 00               jne 0x1409ab5a1
009AAF0F  4C 8B 05 82 BB 61 00            mov r8, qword ptr [rip + 0x61bb82]
009AAF16  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AAF1B  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AAF20  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AAF25  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AAF2A  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AAF32  45 33 C9                        xor r9d, r9d
009AAF35  BA 00 10 00 00                  mov edx, 0x1000
009AAF3A  49 8B CF                        mov rcx, r15
009AAF3D  E8 0E E7 EB FF                  call 0x140869650
009AAF42  85 C0                           test eax, eax
009AAF44  0F 88 F6 37 00 00               js 0x1409ae740
009AAF4A  4C 8B C6                        mov r8, rsi
009AAF4D  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
009AAF52  48 8B D3                        mov rdx, rbx
009AAF55  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
009AAF5D  E8 DE 51 02 00                  call 0x1409d0140
009AAF62  8B F8                           mov edi, eax
009AAF64  85 C0                           test eax, eax
009AAF66  0F 88 C7 00 00 00               js 0x1409ab033
009AAF6C  4D 85 E4                        test r12, r12
009AAF6F  0F 84 BE 00 00 00               je 0x1409ab033
009AAF75  45 89 34 24                     mov dword ptr [r12], r14d
009AAF79  48 8B CB                        mov rcx, rbx
009AAF7C  BA 50 73 51 79                  mov edx, 0x79517350
009AAF81  E8 5A C9 94 FF                  call 0x1402f78e0
009AAF86  8B C7                           mov eax, edi
009AAF88  E9 B3 37 00 00                  jmp 0x1409ae740
009AAF8D  41 83 FE 20                     cmp r14d, 0x20
009AAF91  0F 85 0A 06 00 00               jne 0x1409ab5a1
009AAF97  4C 8B 05 FA BA 61 00            mov r8, qword ptr [rip + 0x61bafa]
009AAF9E  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AAFA3  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AAFA8  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AAFAD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AAFB2  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AAFBA  45 0F B6 CD                     movzx r9d, r13b
009AAFBE  BA 00 10 00 00                  mov edx, 0x1000
009AAFC3  49 8B CF                        mov rcx, r15
009AAFC6  E8 85 E6 EB FF                  call 0x140869650
009AAFCB  8B F8                           mov edi, eax
009AAFCD  85 C0                           test eax, eax
009AAFCF  0F 88 6B 37 00 00               js 0x1409ae740
009AAFD5  48 8D 94 24 F8 00 00 00         lea rdx, [rsp + 0xf8]
009AAFDD  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
009AAFE2  48 8B CB                        mov rcx, rbx
009AAFE5  E8 26 BC 02 00                  call 0x1409d6c10
009AAFEA  90                              nop
009AAFEB  8B 0D AF BA 61 00               mov ecx, dword ptr [rip + 0x61baaf]
009AAFF1  48 0F AF C1                     imul rax, rcx
009AAFF5  48 89 46 10                     mov qword ptr [rsi + 0x10], rax
009AAFF9  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
009AB001  48 0F AF C1                     imul rax, rcx
009AB005  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
009AB009  48 8B 83 F8 01 00 00            mov rax, qword ptr [rbx + 0x1f8]
009AB010  48 89 06                        mov qword ptr [rsi], rax
009AB013  48 8B 83 C0 05 00 00            mov rax, qword ptr [rbx + 0x5c0]
009AB01A  48 89 46 08                     mov qword ptr [rsi + 8], rax
009AB01E  4D 85 E4                        test r12, r12
009AB021  74 07                           je 0x1409ab02a
009AB023  41 8B C6                        mov eax, r14d
009AB026  41 89 04 24                     mov dword ptr [r12], eax
009AB02A  EB 07                           jmp 0x1409ab033
009AB02C  8B F8                           mov edi, eax
009AB02E  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
009AB033  48 8B CB                        mov rcx, rbx
009AB036  BA 50 73 51 79                  mov edx, 0x79517350
009AB03B  E8 A0 C8 94 FF                  call 0x1402f78e0
009AB040  8B C7                           mov eax, edi
009AB042  E9 F9 36 00 00                  jmp 0x1409ae740
009AB047  C7 44 24 48 BB 00 00 C0         mov dword ptr [rsp + 0x48], 0xc00000bb
009AB04F  E9 B2 F4 FF FF                  jmp 0x1409aa506
009AB054  44 88 6C 24 28                  mov byte ptr [rsp + 0x28], r13b
009AB059  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
009AB05E  45 8B CE                        mov r9d, r14d
009AB061  4C 8B C6                        mov r8, rsi
009AB064  49 8B CF                        mov rcx, r15
009AB067  E8 14 B2 02 00                  call 0x1409d6280
009AB06C  E9 CF 36 00 00                  jmp 0x1409ae740
009AB071  4C 8B 05 20 BA 61 00            mov r8, qword ptr [rip + 0x61ba20]
009AB078  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AB07D  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AB082  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AB087  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AB08C  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AB094  45 0F B6 CD                     movzx r9d, r13b
009AB098  BA 00 10 00 00                  mov edx, 0x1000
009AB09D  49 8B CF                        mov rcx, r15
009AB0A0  E8 AB E5 EB FF                  call 0x140869650
009AB0A5  85 C0                           test eax, eax
009AB0A7  0F 88 93 36 00 00               js 0x1409ae740
009AB0AD  41 83 FE 10                     cmp r14d, 0x10
009AB0B1  0F 82 C6 04 00 00               jb 0x1409ab57d
009AB0B7  48 8D 5E 10                     lea rbx, [rsi + 0x10]
009AB0BB  41 83 C6 F0                     add r14d, -0x10
009AB0BF  44 89 74 24 50                  mov dword ptr [rsp + 0x50], r14d
009AB0C4  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
009AB0C9  4C 8B C3                        mov r8, rbx
009AB0CC  48 8B D6                        mov rdx, rsi
009AB0CF  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AB0D4  E8 F7 64 06 00                  call 0x140a115d0
009AB0D9  8B F0                           mov esi, eax
009AB0DB  BA 50 73 51 79                  mov edx, 0x79517350
009AB0E0  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AB0E5  E8 F6 C7 94 FF                  call 0x1402f78e0
009AB0EA  BF 04 00 00 C0                  mov edi, 0xc0000004
009AB0EF  85 F6                           test esi, esi
009AB0F1  0F 89 FC 02 00 00               jns 0x1409ab3f3
009AB0F7  4D 85 E4                        test r12, r12
009AB0FA  74 1F                           je 0x1409ab11b
009AB0FC  B9 00 00 00 80                  mov ecx, 0x80000000
009AB101  8D 04 0E                        lea eax, [rsi + rcx]
009AB104  85 C1                           test ecx, eax
009AB106  0F 84 24 07 00 00               je 0x1409ab830
009AB10C  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
009AB110  83 C0 10                        add eax, 0x10
009AB113  41 89 04 24                     mov dword ptr [r12], eax
009AB117  EB 02                           jmp 0x1409ab11b
009AB119  8B F0                           mov esi, eax
009AB11B  8B C6                           mov eax, esi
009AB11D  E9 1E 36 00 00                  jmp 0x1409ae740
009AB122  4C 8B 05 6F B9 61 00            mov r8, qword ptr [rip + 0x61b96f]
009AB129  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AB12E  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AB133  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AB138  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AB13D  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AB145  45 0F B6 CD                     movzx r9d, r13b
009AB149  BA 00 10 00 00                  mov edx, 0x1000
009AB14E  49 8B CF                        mov rcx, r15
009AB151  E8 FA E4 EB FF                  call 0x140869650
009AB156  8B F8                           mov edi, eax
009AB158  85 C0                           test eax, eax
009AB15A  0F 88 E0 FE FF FF               js 0x1409ab040
009AB160  41 83 FE 01                     cmp r14d, 1
009AB164  0F 82 6E 33 00 00               jb 0x1409ae4d8
009AB16A  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AB16F  0F B6 81 FA 05 00 00            movzx eax, byte ptr [rcx + 0x5fa]
009AB176  88 06                           mov byte ptr [rsi], al
009AB178  4D 85 E4                        test r12, r12
009AB17B  74 0A                           je 0x1409ab187
009AB17D  41 BD 01 00 00 00               mov r13d, 1
009AB183  45 89 2C 24                     mov dword ptr [r12], r13d
009AB187  EB 09                           jmp 0x1409ab192
009AB189  8B F8                           mov edi, eax
009AB18B  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AB190  EB 02                           jmp 0x1409ab194
009AB192  8B FB                           mov edi, ebx
009AB194  48 85 C9                        test rcx, rcx
009AB197  0F 85 99 FE FF FF               jne 0x1409ab036
009AB19D  8B C7                           mov eax, edi
009AB19F  E9 9C 35 00 00                  jmp 0x1409ae740
009AB1A4  41 83 FE 02                     cmp r14d, 2
009AB1A8  0F 85 F3 03 00 00               jne 0x1409ab5a1
009AB1AE  4C 8B 05 E3 B8 61 00            mov r8, qword ptr [rip + 0x61b8e3]
009AB1B5  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AB1BA  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AB1BF  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AB1C4  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AB1C9  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AB1D1  45 0F B6 CD                     movzx r9d, r13b
009AB1D5  BA 00 10 00 00                  mov edx, 0x1000
009AB1DA  49 8B CF                        mov rcx, r15
009AB1DD  E8 6E E4 EB FF                  call 0x140869650
009AB1E2  85 C0                           test eax, eax
009AB1E4  0F 88 56 35 00 00               js 0x1409ae740
009AB1EA  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AB1EF  0F B6 81 47 03 00 00            movzx eax, byte ptr [rcx + 0x347]
009AB1F6  88 84 24 99 00 00 00            mov byte ptr [rsp + 0x99], al
009AB1FD  BA 50 73 51 79                  mov edx, 0x79517350
009AB202  E8 D9 C6 94 FF                  call 0x1402f78e0
009AB207  90                              nop
009AB208  0F B7 84 24 98 00 00 00         movzx eax, word ptr [rsp + 0x98]
009AB210  66 89 06                        mov word ptr [rsi], ax
009AB213  4D 85 E4                        test r12, r12
009AB216  74 04                           je 0x1409ab21c
009AB218  45 89 34 24                     mov dword ptr [r12], r14d
009AB21C  E9 D4 FC FF FF                  jmp 0x1409aaef5
009AB221  E9 1A 35 00 00                  jmp 0x1409ae740
009AB226  41 83 FE 70                     cmp r14d, 0x70
009AB22A  0F 85 5D 03 00 00               jne 0x1409ab58d
009AB230  4C 8B 05 61 B8 61 00            mov r8, qword ptr [rip + 0x61b861]
009AB237  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AB23C  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AB241  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AB246  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AB24B  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AB253  45 0F B6 CD                     movzx r9d, r13b
009AB257  BA 00 10 00 00                  mov edx, 0x1000
009AB25C  49 8B CF                        mov rcx, r15
009AB25F  E8 EC E3 EB FF                  call 0x140869650
009AB264  85 C0                           test eax, eax
009AB266  0F 88 D4 34 00 00               js 0x1409ae740
009AB26C  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AB271  48 8B 80 20 02 00 00            mov rax, qword ptr [rax + 0x220]
009AB278  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
009AB280  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AB285  48 8B 80 28 02 00 00            mov rax, qword ptr [rax + 0x228]
009AB28C  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
009AB294  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AB299  8B 80 04 04 00 00               mov eax, dword ptr [rax + 0x404]
009AB29F  89 84 24 50 01 00 00            mov dword ptr [rsp + 0x150], eax
009AB2A6  4C 8D 84 24 60 04 00 00         lea r8, [rsp + 0x460]
009AB2AE  33 D2                           xor edx, edx
009AB2B0  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
009AB2B5  48 8B CB                        mov rcx, rbx
009AB2B8  E8 63 B5 86 FF                  call 0x140216820
009AB2BD  48 8D 84 24 B8 01 00 00         lea rax, [rsp + 0x1b8]
009AB2C5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AB2CA  48 8D 84 24 C0 01 00 00         lea rax, [rsp + 0x1c0]
009AB2D2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009AB2D7  4C 8D 8C 24 C8 01 00 00         lea r9, [rsp + 0x1c8]
009AB2DF  4C 8D 84 24 A0 01 00 00         lea r8, [rsp + 0x1a0]
009AB2E7  48 8D 94 24 60 01 00 00         lea rdx, [rsp + 0x160]
009AB2EF  48 8D 8C 24 58 01 00 00         lea rcx, [rsp + 0x158]
009AB2F7  E8 24 18 A7 FF                  call 0x14041cb20
009AB2FC  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AB300  33 D2                           xor edx, edx
009AB302  48 8D 8C 24 60 04 00 00         lea rcx, [rsp + 0x460]
009AB30A  E8 21 CA 86 FF                  call 0x140217d30
009AB30F  48 8B 83 08 02 00 00            mov rax, qword ptr [rbx + 0x208]
009AB316  48 89 84 24 70 01 00 00         mov qword ptr [rsp + 0x170], rax
009AB31E  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AB323  48 8B 88 18 02 00 00            mov rcx, qword ptr [rax + 0x218]
009AB32A  48 89 8C 24 68 01 00 00         mov qword ptr [rsp + 0x168], rcx
009AB332  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AB337  48 8B 88 00 02 00 00            mov rcx, qword ptr [rax + 0x200]
009AB33E  48 89 8C 24 80 01 00 00         mov qword ptr [rsp + 0x180], rcx
009AB346  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AB34B  48 8B 88 10 02 00 00            mov rcx, qword ptr [rax + 0x210]
009AB352  48 89 8C 24 78 01 00 00         mov qword ptr [rsp + 0x178], rcx
009AB35A  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AB35F  48 8B 88 D8 03 00 00            mov rcx, qword ptr [rax + 0x3d8]
009AB366  48 C1 E1 0C                     shl rcx, 0xc
009AB36A  48 89 8C 24 88 01 00 00         mov qword ptr [rsp + 0x188], rcx
009AB372  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AB377  48 8B 88 E0 03 00 00            mov rcx, qword ptr [rax + 0x3e0]
009AB37E  48 C1 E1 0C                     shl rcx, 0xc
009AB382  48 89 8C 24 90 01 00 00         mov qword ptr [rsp + 0x190], rcx
009AB38A  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AB38F  48 8B 88 A8 06 00 00            mov rcx, qword ptr [rax + 0x6a8]
009AB396  48 C1 E1 0C                     shl rcx, 0xc
009AB39A  48 89 8C 24 A8 01 00 00         mov qword ptr [rsp + 0x1a8], rcx
009AB3A2  48 8B 84 24 88 01 00 00         mov rax, qword ptr [rsp + 0x188]
009AB3AA  48 89 84 24 98 01 00 00         mov qword ptr [rsp + 0x198], rax
009AB3B2  BA 50 73 51 79                  mov edx, 0x79517350
009AB3B7  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AB3BC  E8 1F C5 94 FF                  call 0x1402f78e0
009AB3C1  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
009AB3C5  85 C0                           test eax, eax
009AB3C7  0F 88 73 33 00 00               js 0x1409ae740
009AB3CD  4D 8B C6                        mov r8, r14
009AB3D0  48 8D 94 24 40 01 00 00         lea rdx, [rsp + 0x140]
009AB3D8  48 8B CE                        mov rcx, rsi
009AB3DB  E8 60 B4 D1 FF                  call 0x1406c6840
009AB3E0  4D 85 E4                        test r12, r12
009AB3E3  74 04                           je 0x1409ab3e9
009AB3E5  45 89 34 24                     mov dword ptr [r12], r14d
009AB3E9  E9 07 FB FF FF                  jmp 0x1409aaef5
009AB3EE  E9 4D 33 00 00                  jmp 0x1409ae740
009AB3F3  48 85 DB                        test rbx, rbx
009AB3F6  0F 44 F7                        cmove esi, edi
009AB3F9  E9 F9 FC FF FF                  jmp 0x1409ab0f7
009AB3FE  33 C0                           xor eax, eax
009AB400  48 89 84 24 40 04 00 00         mov qword ptr [rsp + 0x440], rax
009AB408  89 84 24 48 04 00 00            mov dword ptr [rsp + 0x448], eax
009AB40F  41 83 FE 0C                     cmp r14d, 0xc
009AB413  0F 85 88 01 00 00               jne 0x1409ab5a1
009AB419  48 8B 0D 80 B8 61 00            mov rcx, qword ptr [rip + 0x61b880]
009AB420  E8 EF D3 A7 FF                  call 0x140428814
009AB425  48 8B F8                        mov rdi, rax
009AB428  48 85 C0                        test rax, rax
009AB42B  0F 84 31 2E 00 00               je 0x1409ae262
009AB431  4C 8B 05 60 B6 61 00            mov r8, qword ptr [rip + 0x61b660]
009AB438  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AB43D  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AB442  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AB447  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AB44C  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AB454  45 0F B6 CD                     movzx r9d, r13b
009AB458  BA 00 10 00 00                  mov edx, 0x1000
009AB45D  49 8B CF                        mov rcx, r15
009AB460  E8 EB E1 EB FF                  call 0x140869650
009AB465  44 8B F0                        mov r14d, eax
009AB468  85 C0                           test eax, eax
009AB46A  0F 88 E9 07 00 00               js 0x1409abc59
009AB470  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
009AB474  48 8D 94 24 40 04 00 00         lea rdx, [rsp + 0x440]
009AB47C  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009AB481  49 8B CE                        mov rcx, r14
009AB484  E8 47 F6 D0 FF                  call 0x1406baad0
009AB489  8B F8                           mov edi, eax
009AB48B  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AB48F  85 C0                           test eax, eax
009AB491  78 37                           js 0x1409ab4ca
009AB493  F2 0F 10 84 24 40 04 00 00      movsd xmm0, qword ptr [rsp + 0x440]
009AB49C  F2 0F 11 06                     movsd qword ptr [rsi], xmm0
009AB4A0  8B 84 24 48 04 00 00            mov eax, dword ptr [rsp + 0x448]
009AB4A7  89 46 08                        mov dword ptr [rsi + 8], eax
009AB4AA  4D 85 E4                        test r12, r12
009AB4AD  74 08                           je 0x1409ab4b7
009AB4AF  41 C7 04 24 0C 00 00 00         mov dword ptr [r12], 0xc
009AB4B7  8B FB                           mov edi, ebx
009AB4B9  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009AB4BD  EB 0B                           jmp 0x1409ab4ca
009AB4BF  8B F8                           mov edi, eax
009AB4C1  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AB4C5  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009AB4CA  BA 50 73 51 79                  mov edx, 0x79517350
009AB4CF  49 8B CE                        mov rcx, r14
009AB4D2  E8 09 C4 94 FF                  call 0x1402f78e0
009AB4D7  48 8B 0D C2 B7 61 00            mov rcx, qword ptr [rip + 0x61b7c2]
009AB4DE  E8 DD B8 AA FF                  call 0x140456dc0
009AB4E3  8B C7                           mov eax, edi
009AB4E5  E9 56 32 00 00                  jmp 0x1409ae740
009AB4EA  41 83 FE 24                     cmp r14d, 0x24
009AB4EE  0F 82 AD 00 00 00               jb 0x1409ab5a1
009AB4F4  41 83 FE 30                     cmp r14d, 0x30
009AB4F8  0F 84 36 1F 00 00               je 0x1409ad434
009AB4FE  41 83 FE 24                     cmp r14d, 0x24
009AB502  0F 85 99 00 00 00               jne 0x1409ab5a1
009AB508  8B FB                           mov edi, ebx
009AB50A  4C 8B 05 87 B5 61 00            mov r8, qword ptr [rip + 0x61b587]
009AB511  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AB516  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AB51B  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AB520  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AB525  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AB52D  45 0F B6 CD                     movzx r9d, r13b
009AB531  BA 00 04 00 00                  mov edx, 0x400
009AB536  49 8B CF                        mov rcx, r15
009AB539  E8 12 E1 EB FF                  call 0x140869650
009AB53E  85 C0                           test eax, eax
009AB540  0F 88 FA 31 00 00               js 0x1409ae740
009AB546  44 8B C7                        mov r8d, edi
009AB549  48 8B D6                        mov rdx, rsi
009AB54C  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AB551  E8 6A 10 FC FF                  call 0x14096c5c0
009AB556  8B F8                           mov edi, eax
009AB558  BA 50 73 51 79                  mov edx, 0x79517350
009AB55D  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AB562  E8 79 C3 94 FF                  call 0x1402f78e0
009AB567  85 FF                           test edi, edi
009AB569  0F 88 D1 FA FF FF               js 0x1409ab040
009AB56F  4D 85 E4                        test r12, r12
009AB572  0F 84 C8 FA FF FF               je 0x1409ab040
009AB578  E9 81 1C 00 00                  jmp 0x1409ad1fe
009AB57D  48 8D B4 24 08 03 00 00         lea rsi, [rsp + 0x308]
009AB585  44 8B F3                        mov r14d, ebx
009AB588  E9 32 FB FF FF                  jmp 0x1409ab0bf
009AB58D  41 83 FE 58                     cmp r14d, 0x58
009AB591  0F 84 99 FC FF FF               je 0x1409ab230
009AB597  41 83 FE 60                     cmp r14d, 0x60
009AB59B  0F 84 8F FC FF FF               je 0x1409ab230
009AB5A1  B8 04 00 00 C0                  mov eax, 0xc0000004
009AB5A6  E9 95 31 00 00                  jmp 0x1409ae740
009AB5AB  41 83 FE 40                     cmp r14d, 0x40
009AB5AF  75 F0                           jne 0x1409ab5a1
009AB5B1  4C 8B 05 E0 B4 61 00            mov r8, qword ptr [rip + 0x61b4e0]
009AB5B8  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AB5BD  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AB5C2  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AB5C7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AB5CC  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AB5D4  45 0F B6 CD                     movzx r9d, r13b
009AB5D8  BA 00 10 00 00                  mov edx, 0x1000
009AB5DD  49 8B CF                        mov rcx, r15
009AB5E0  E8 6B E0 EB FF                  call 0x140869650
009AB5E5  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
009AB5E9  85 C0                           test eax, eax
009AB5EB  0F 88 4F 31 00 00               js 0x1409ae740
009AB5F1  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009AB5F6  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
009AB5FE  48 3B B9 20 02 00 00            cmp rdi, qword ptr [rcx + 0x220]
009AB605  0F 85 BD 0C 00 00               jne 0x1409ac2c8
009AB60B  48 8B 9F A8 02 00 00            mov rbx, qword ptr [rdi + 0x2a8]
009AB612  B9 0A 01 00 C0                  mov ecx, 0xc000010a
009AB617  48 85 DB                        test rbx, rbx
009AB61A  0F 44 C1                        cmove eax, ecx
009AB61D  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
009AB621  45 32 F6                        xor r14b, r14b
009AB624  44 8B F8                        mov r15d, eax
009AB627  BA 50 73 51 79                  mov edx, 0x79517350
009AB62C  48 8B CF                        mov rcx, rdi
009AB62F  E8 AC C2 94 FF                  call 0x1402f78e0
009AB634  45 85 FF                        test r15d, r15d
009AB637  0F 88 64 04 00 00               js 0x1409abaa1
009AB63D  4C 8B C6                        mov r8, rsi
009AB640  BA 01 00 00 00                  mov edx, 1
009AB645  48 8B CB                        mov rcx, rbx
009AB648  E8 C3 62 F7 FF                  call 0x140921910
009AB64D  44 8B F8                        mov r15d, eax
009AB650  45 84 F6                        test r14b, r14b
009AB653  74 08                           je 0x1409ab65d
009AB655  48 8B CB                        mov rcx, rbx
009AB658  E8 F3 DC 94 FF                  call 0x1402f9350
009AB65D  45 85 FF                        test r15d, r15d
009AB660  0F 88 3B 04 00 00               js 0x1409abaa1
009AB666  4D 85 E4                        test r12, r12
009AB669  0F 85 BA 11 00 00               jne 0x1409ac829
009AB66F  E9 2D 04 00 00                  jmp 0x1409abaa1
009AB674  4C 8B 05 1D B4 61 00            mov r8, qword ptr [rip + 0x61b41d]
009AB67B  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AB680  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AB685  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AB68A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AB68F  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AB697  45 0F B6 CD                     movzx r9d, r13b
009AB69B  BA 00 10 00 00                  mov edx, 0x1000
009AB6A0  49 8B CF                        mov rcx, r15
009AB6A3  E8 A8 DF EB FF                  call 0x140869650
009AB6A8  8B F8                           mov edi, eax
009AB6AA  85 C0                           test eax, eax
009AB6AC  0F 88 8E 30 00 00               js 0x1409ae740
009AB6B2  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
009AB6B7  4D 8B BD 30 03 00 00            mov r15, qword ptr [r13 + 0x330]
009AB6BE  4C 89 BC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r15
009AB6C6  4D 85 FF                        test r15, r15
009AB6C9  0F 85 C1 04 00 00               jne 0x1409abb90
009AB6CF  48 8D 94 24 A8 00 00 00         lea rdx, [rsp + 0xa8]
009AB6D7  49 8B CD                        mov rcx, r13
009AB6DA  E8 91 B1 F2 FF                  call 0x1408d6870
009AB6DF  8B F8                           mov edi, eax
009AB6E1  4C 8B BC 24 A8 00 00 00         mov r15, qword ptr [rsp + 0xa8]
009AB6E9  BA 50 73 51 79                  mov edx, 0x79517350
009AB6EE  49 8B CD                        mov rcx, r13
009AB6F1  E8 EA C1 94 FF                  call 0x1402f78e0
009AB6F6  85 FF                           test edi, edi
009AB6F8  0F 88 42 F9 FF FF               js 0x1409ab040
009AB6FE  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
009AB706  49 8B CF                        mov rcx, r15
009AB709  E8 32 AC EF FF                  call 0x1408a6340
009AB70E  8B F8                           mov edi, eax
009AB710  49 8B CF                        mov rcx, r15
009AB713  E8 38 DC 94 FF                  call 0x1402f9350
009AB718  85 FF                           test edi, edi
009AB71A  0F 88 20 F9 FF FF               js 0x1409ab040
009AB720  4C 8B BC 24 A0 00 00 00         mov r15, qword ptr [rsp + 0xa0]
009AB728  45 0F B7 6F 02                  movzx r13d, word ptr [r15 + 2]
009AB72D  45 8D 6D 10                     lea r13d, [r13 + 0x10]
009AB731  45 3B EE                        cmp r13d, r14d
009AB734  77 3C                           ja 0x1409ab772
009AB736  41 0F B7 07                     movzx eax, word ptr [r15]
009AB73A  66 89 06                        mov word ptr [rsi], ax
009AB73D  41 0F B7 47 02                  movzx eax, word ptr [r15 + 2]
009AB742  66 89 46 02                     mov word ptr [rsi + 2], ax
009AB746  41 0F B7 47 02                  movzx eax, word ptr [r15 + 2]
009AB74B  66 85 C0                        test ax, ax
009AB74E  74 13                           je 0x1409ab763
009AB750  48 8D 5E 10                     lea rbx, [rsi + 0x10]
009AB754  44 8B C0                        mov r8d, eax
009AB757  49 8B 57 08                     mov rdx, qword ptr [r15 + 8]
009AB75B  48 8B CB                        mov rcx, rbx
009AB75E  E8 DD B0 D1 FF                  call 0x1406c6840
009AB763  48 89 5E 08                     mov qword ptr [rsi + 8], rbx
009AB767  4D 85 E4                        test r12, r12
009AB76A  74 11                           je 0x1409ab77d
009AB76C  45 89 2C 24                     mov dword ptr [r12], r13d
009AB770  EB 0B                           jmp 0x1409ab77d
009AB772  BF 04 00 00 C0                  mov edi, 0xc0000004
009AB777  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
009AB77B  EB EA                           jmp 0x1409ab767
009AB77D  EB 0E                           jmp 0x1409ab78d
009AB77F  8B F8                           mov edi, eax
009AB781  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AB785  4C 8B BC 24 A0 00 00 00         mov r15, qword ptr [rsp + 0xa0]
009AB78D  33 D2                           xor edx, edx
009AB78F  49 8B CF                        mov rcx, r15
009AB792  E8 D9 70 1D 00                  call 0x140b82870
009AB797  8B C7                           mov eax, edi
009AB799  E9 A2 2F 00 00                  jmp 0x1409ae740
009AB79E  41 83 FE 04                     cmp r14d, 4
009AB7A2  0F 85 F9 FD FF FF               jne 0x1409ab5a1
009AB7A8  4C 8B 05 E9 B2 61 00            mov r8, qword ptr [rip + 0x61b2e9]
009AB7AF  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AB7B4  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AB7B9  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AB7BE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AB7C3  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AB7CB  45 0F B6 CD                     movzx r9d, r13b
009AB7CF  BA 00 10 00 00                  mov edx, 0x1000
009AB7D4  49 8B CF                        mov rcx, r15
009AB7D7  E8 74 DE EB FF                  call 0x140869650
009AB7DC  85 C0                           test eax, eax
009AB7DE  0F 88 5C 2F 00 00               js 0x1409ae740
009AB7E4  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AB7E9  8B 99 88 03 00 00               mov ebx, dword ptr [rcx + 0x388]
009AB7EF  BA 50 73 51 79                  mov edx, 0x79517350
009AB7F4  E8 E7 C0 94 FF                  call 0x1402f78e0
009AB7F9  90                              nop
009AB7FA  89 1E                           mov dword ptr [rsi], ebx
009AB7FC  4D 85 E4                        test r12, r12
009AB7FF  74 04                           je 0x1409ab805
009AB801  45 89 34 24                     mov dword ptr [r12], r14d
009AB805  E9 EB F6 FF FF                  jmp 0x1409aaef5
009AB80A  E9 31 2F 00 00                  jmp 0x1409ae740
009AB80F  0F B7 90 30 02 00 00            movzx edx, word ptr [rax + 0x230]
009AB816  48 8D 8C 24 30 04 00 00         lea rcx, [rsp + 0x430]
009AB81E  E8 0D 5B A8 FF                  call 0x140431330
009AB823  85 C0                           test eax, eax
009AB825  0F 85 83 EE FF FF               jne 0x1409aa6ae
009AB82B  E9 8F EE FF FF                  jmp 0x1409aa6bf
009AB830  3B F7                           cmp esi, edi
009AB832  0F 84 D4 F8 FF FF               je 0x1409ab10c
009AB838  E9 DE F8 FF FF                  jmp 0x1409ab11b
009AB83D  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
009AB845  48 3B B9 20 02 00 00            cmp rdi, qword ptr [rcx + 0x220]
009AB84C  0F 84 F6 ED FF FF               je 0x1409aa648
009AB852  41 BD 01 00 00 00               mov r13d, 1
009AB858  E9 62 EE FF FF                  jmp 0x1409aa6bf
009AB85D  89 9C 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], ebx
009AB864  0F 57 C0                        xorps xmm0, xmm0
009AB867  0F 11 84 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm0
009AB86F  48 89 9C 24 C0 02 00 00         mov qword ptr [rsp + 0x2c0], rbx
009AB877  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
009AB87C  41 80 FD 01                     cmp r13b, 1
009AB880  0F 85 F7 22 00 00               jne 0x1409adb7d
009AB886  4C 8B 05 0B B2 61 00            mov r8, qword ptr [rip + 0x61b20b]
009AB88D  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AB892  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AB897  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AB89C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AB8A1  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AB8A9  45 0F B6 CD                     movzx r9d, r13b
009AB8AD  BA 00 10 00 00                  mov edx, 0x1000
009AB8B2  49 8B CF                        mov rcx, r15
009AB8B5  E8 96 DD EB FF                  call 0x140869650
009AB8BA  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AB8BE  85 C0                           test eax, eax
009AB8C0  0F 88 7A 2E 00 00               js 0x1409ae740
009AB8C6  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009AB8CB  48 8D 8F E8 01 00 00            lea rcx, [rdi + 0x1e8]
009AB8D2  E8 49 AD 86 FF                  call 0x140216620
009AB8D7  84 C0                           test al, al
009AB8D9  0F 84 C2 16 00 00               je 0x1409acfa1
009AB8DF  4C 8D 84 24 60 04 00 00         lea r8, [rsp + 0x460]
009AB8E7  33 D2                           xor edx, edx
009AB8E9  48 8B CF                        mov rcx, rdi
009AB8EC  E8 2F AF 86 FF                  call 0x140216820
009AB8F1  90                              nop
009AB8F2  48 8B C3                        mov rax, rbx
009AB8F5  48 8B 8F 10 03 00 00            mov rcx, qword ptr [rdi + 0x310]
009AB8FC  48 85 C9                        test rcx, rcx
009AB8FF  74 03                           je 0x1409ab904
009AB901  48 8B 01                        mov rax, qword ptr [rcx]
009AB904  48 85 C0                        test rax, rax
009AB907  0F 85 85 00 00 00               jne 0x1409ab992
009AB90D  48 8B 87 E0 02 00 00            mov rax, qword ptr [rdi + 0x2e0]
009AB914  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
009AB918  48 89 8C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rcx
009AB920  48 8B C1                        mov rax, rcx
009AB923  48 05 A4 00 00 00               add rax, 0xa4
009AB929  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
009AB933  48 3B C2                        cmp rax, rdx
009AB936  48 0F 43 C2                     cmovae rax, rdx
009AB93A  90                              nop
009AB93B  8B 00                           mov eax, dword ptr [rax]
009AB93D  89 84 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], eax
009AB944  0F 57 C0                        xorps xmm0, xmm0
009AB947  0F 11 84 24 00 01 00 00         movups xmmword ptr [rsp + 0x100], xmm0
009AB94F  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
009AB957  48 81 C1 B0 00 00 00            add rcx, 0xb0
009AB95E  48 3B CA                        cmp rcx, rdx
009AB961  48 0F 43 CA                     cmovae rcx, rdx
009AB965  90                              nop
009AB966  8B 01                           mov eax, dword ptr [rcx]
009AB968  89 84 24 00 01 00 00            mov dword ptr [rsp + 0x100], eax
009AB96F  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
009AB973  48 89 84 24 08 01 00 00         mov qword ptr [rsp + 0x108], rax
009AB97B  0F 28 84 24 00 01 00 00         movaps xmm0, xmmword ptr [rsp + 0x100]
009AB983  0F 29 84 24 D0 00 00 00         movaps xmmword ptr [rsp + 0xd0], xmm0
009AB98B  66 41 0F 7E C5                  movd r13d, xmm0
009AB990  EB 5A                           jmp 0x1409ab9ec
009AB992  8B 40 10                        mov eax, dword ptr [rax + 0x10]
009AB995  48 89 84 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rax
009AB99D  90                              nop
009AB99E  8B 40 68                        mov eax, dword ptr [rax + 0x68]
009AB9A1  89 84 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], eax
009AB9A8  48 8B 94 24 B0 00 00 00         mov rdx, qword ptr [rsp + 0xb0]
009AB9B0  48 83 C2 70                     add rdx, 0x70
009AB9B4  41 B8 08 00 00 00               mov r8d, 8
009AB9BA  48 8D 4C 24 58                  lea rcx, [rsp + 0x58]
009AB9BF  E8 0C 10 D1 FF                  call 0x1406bc9d0
009AB9C4  44 0F B7 6C 24 58               movzx r13d, word ptr [rsp + 0x58]
009AB9CA  66 44 89 AC 24 D0 00 00 00      mov word ptr [rsp + 0xd0], r13w
009AB9D3  0F B7 44 24 5A                  movzx eax, word ptr [rsp + 0x5a]
009AB9D8  66 89 84 24 D2 00 00 00         mov word ptr [rsp + 0xd2], ax
009AB9E0  8B 44 24 5C                     mov eax, dword ptr [rsp + 0x5c]
009AB9E4  48 89 84 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rax
009AB9EC  44 8B 7C 24 48                  mov r15d, dword ptr [rsp + 0x48]
009AB9F1  EB 26                           jmp 0x1409aba19
009AB9F3  44 8B F8                        mov r15d, eax
009AB9F6  33 DB                           xor ebx, ebx
009AB9F8  44 0F B7 AC 24 D0 00 00 00      movzx r13d, word ptr [rsp + 0xd0]
009ABA01  48 8B B4 24 28 01 00 00         mov rsi, qword ptr [rsp + 0x128]
009ABA09  44 8B B4 24 D8 01 00 00         mov r14d, dword ptr [rsp + 0x1d8]
009ABA11  4C 8B A4 24 30 01 00 00         mov r12, qword ptr [rsp + 0x130]
009ABA19  33 D2                           xor edx, edx
009ABA1B  48 8D 8C 24 60 04 00 00         lea rcx, [rsp + 0x460]
009ABA23  E8 08 C3 86 FF                  call 0x140217d30
009ABA28  45 85 FF                        test r15d, r15d
009ABA2B  78 56                           js 0x1409aba83
009ABA2D  41 0F B7 C5                     movzx eax, r13w
009ABA31  83 C0 06                        add eax, 6
009ABA34  4D 85 E4                        test r12, r12
009ABA37  74 04                           je 0x1409aba3d
009ABA39  41 89 04 24                     mov dword ptr [r12], eax
009ABA3D  44 3B F0                        cmp r14d, eax
009ABA40  72 10                           jb 0x1409aba52
009ABA42  8B 84 24 C8 00 00 00            mov eax, dword ptr [rsp + 0xc8]
009ABA49  89 06                           mov dword ptr [rsi], eax
009ABA4B  66 44 89 6E 04                  mov word ptr [rsi + 4], r13w
009ABA50  EB 0C                           jmp 0x1409aba5e
009ABA52  BF 04 00 00 C0                  mov edi, 0xc0000004
009ABA57  44 8B FF                        mov r15d, edi
009ABA5A  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
009ABA5E  EB 1A                           jmp 0x1409aba7a
009ABA60  44 8B F8                        mov r15d, eax
009ABA63  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009ABA67  33 DB                           xor ebx, ebx
009ABA69  44 0F B7 AC 24 D0 00 00 00      movzx r13d, word ptr [rsp + 0xd0]
009ABA72  48 8B B4 24 28 01 00 00         mov rsi, qword ptr [rsp + 0x128]
009ABA7A  45 85 FF                        test r15d, r15d
009ABA7D  0F 89 26 13 00 00               jns 0x1409acda9
009ABA83  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009ABA88  48 8D 8F E8 01 00 00            lea rcx, [rdi + 0x1e8]
009ABA8F  E8 EC E3 99 FF                  call 0x140349e80
009ABA94  BA 50 73 51 79                  mov edx, 0x79517350
009ABA99  48 8B CF                        mov rcx, rdi
009ABA9C  E8 3F BE 94 FF                  call 0x1402f78e0
009ABAA1  41 8B C7                        mov eax, r15d
009ABAA4  E9 97 2C 00 00                  jmp 0x1409ae740
009ABAA9  41 83 FE 04                     cmp r14d, 4
009ABAAD  0F 85 EE FA FF FF               jne 0x1409ab5a1
009ABAB3  4C 8B 05 DE AF 61 00            mov r8, qword ptr [rip + 0x61afde]
009ABABA  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ABABF  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ABAC4  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ABAC9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ABACE  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ABAD6  45 0F B6 CD                     movzx r9d, r13b
009ABADA  BA 00 10 00 00                  mov edx, 0x1000
009ABADF  49 8B CF                        mov rcx, r15
009ABAE2  E8 69 DB EB FF                  call 0x140869650
009ABAE7  85 C0                           test eax, eax
009ABAE9  0F 88 51 2C 00 00               js 0x1409ae740
009ABAEF  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ABAF4  E8 A7 78 87 FF                  call 0x1402233a0
009ABAF9  8B D8                           mov ebx, eax
009ABAFB  BA 50 73 51 79                  mov edx, 0x79517350
009ABB00  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ABB05  E8 D6 BD 94 FF                  call 0x1402f78e0
009ABB0A  90                              nop
009ABB0B  89 1E                           mov dword ptr [rsi], ebx
009ABB0D  4D 85 E4                        test r12, r12
009ABB10  74 04                           je 0x1409abb16
009ABB12  45 89 34 24                     mov dword ptr [r12], r14d
009ABB16  E9 DA F3 FF FF                  jmp 0x1409aaef5
009ABB1B  E9 20 2C 00 00                  jmp 0x1409ae740
009ABB20  41 83 FE 04                     cmp r14d, 4
009ABB24  0F 85 77 FA FF FF               jne 0x1409ab5a1
009ABB2A  4C 8B 05 67 AF 61 00            mov r8, qword ptr [rip + 0x61af67]
009ABB31  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ABB36  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ABB3B  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ABB40  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ABB45  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ABB4D  45 0F B6 CD                     movzx r9d, r13b
009ABB51  BA 18 04 00 00                  mov edx, 0x418
009ABB56  49 8B CF                        mov rcx, r15
009ABB59  E8 F2 DA EB FF                  call 0x140869650
009ABB5E  85 C0                           test eax, eax
009ABB60  0F 88 DA 2B 00 00               js 0x1409ae740
009ABB66  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009ABB6B  48 8B CF                        mov rcx, rdi
009ABB6E  48 83 BF 70 01 00 00 00         cmp qword ptr [rdi + 0x170], 0
009ABB76  0F 85 59 27 00 00               jne 0x1409ae2d5
009ABB7C  BA 50 73 51 79                  mov edx, 0x79517350
009ABB81  E8 5A BD 94 FF                  call 0x1402f78e0
009ABB86  B8 22 00 00 C0                  mov eax, 0xc0000022
009ABB8B  E9 B0 2B 00 00                  jmp 0x1409ae740
009ABB90  49 8D 8D E8 01 00 00            lea rcx, [r13 + 0x1e8]
009ABB97  E8 84 AA 86 FF                  call 0x140216620
009ABB9C  84 C0                           test al, al
009ABB9E  0F 84 86 17 00 00               je 0x1409ad32a
009ABBA4  49 8B CF                        mov rcx, r15
009ABBA7  E8 74 3E 86 FF                  call 0x14020fa20
009ABBAC  49 8D 8D E8 01 00 00            lea rcx, [r13 + 0x1e8]
009ABBB3  E8 C8 E2 99 FF                  call 0x140349e80
009ABBB8  E9 2C FB FF FF                  jmp 0x1409ab6e9
009ABBBD  41 83 FE 08                     cmp r14d, 8
009ABBC1  0F 85 DA F9 FF FF               jne 0x1409ab5a1
009ABBC7  4C 8B 05 CA AE 61 00            mov r8, qword ptr [rip + 0x61aeca]
009ABBCE  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ABBD3  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ABBD8  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ABBDD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ABBE2  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ABBEA  45 0F B6 CD                     movzx r9d, r13b
009ABBEE  BA 00 10 00 00                  mov edx, 0x1000
009ABBF3  49 8B CF                        mov rcx, r15
009ABBF6  E8 55 DA EB FF                  call 0x140869650
009ABBFB  85 C0                           test eax, eax
009ABBFD  0F 88 3D 2B 00 00               js 0x1409ae740
009ABC03  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ABC08  48 8B 81 10 03 00 00            mov rax, qword ptr [rcx + 0x310]
009ABC0F  48 85 C0                        test rax, rax
009ABC12  74 03                           je 0x1409abc17
009ABC14  48 8B 18                        mov rbx, qword ptr [rax]
009ABC17  BA 50 73 51 79                  mov edx, 0x79517350
009ABC1C  E8 BF BC 94 FF                  call 0x1402f78e0
009ABC21  90                              nop
009ABC22  48 89 1E                        mov qword ptr [rsi], rbx
009ABC25  4D 85 E4                        test r12, r12
009ABC28  74 08                           je 0x1409abc32
009ABC2A  41 C7 04 24 08 00 00 00         mov dword ptr [r12], 8
009ABC32  E9 BE F2 FF FF                  jmp 0x1409aaef5
009ABC37  E9 04 2B 00 00                  jmp 0x1409ae740
009ABC3C  45 33 C0                        xor r8d, r8d
009ABC3F  48 8D 54 24 4D                  lea rdx, [rsp + 0x4d]
009ABC44  48 8B CF                        mov rcx, rdi
009ABC47  E8 E4 F9 02 00                  call 0x1409db630
009ABC4C  48 8B 94 24 A0 00 00 00         mov rdx, qword ptr [rsp + 0xa0]
009ABC54  E9 77 EA FF FF                  jmp 0x1409aa6d0
009ABC59  48 8B 0D 40 B0 61 00            mov rcx, qword ptr [rip + 0x61b040]
009ABC60  E8 5B B1 AA FF                  call 0x140456dc0
009ABC65  41 8B C6                        mov eax, r14d
009ABC68  E9 D3 2A 00 00                  jmp 0x1409ae740
009ABC6D  B8 0A 01 00 C0                  mov eax, 0xc000010a
009ABC72  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009ABC76  E9 8B E8 FF FF                  jmp 0x1409aa506
009ABC7B  41 83 FE 04                     cmp r14d, 4
009ABC7F  0F 85 1C F9 FF FF               jne 0x1409ab5a1
009ABC85  49 83 FF FF                     cmp r15, -1
009ABC89  0F 85 A5 16 00 00               jne 0x1409ad334
009ABC8F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009ABC98  4C 8B 90 B8 00 00 00            mov r10, qword ptr [rax + 0xb8]
009ABC9F  48 8D 94 24 EC 00 00 00         lea rdx, [rsp + 0xec]
009ABCA7  49 8B CA                        mov rcx, r10
009ABCAA  E8 31 5C 07 00                  call 0x140a218e0
009ABCAF  8B D8                           mov ebx, eax
009ABCB1  49 83 FF FF                     cmp r15, -1
009ABCB5  74 0D                           je 0x1409abcc4
009ABCB7  BA 50 73 51 79                  mov edx, 0x79517350
009ABCBC  49 8B CA                        mov rcx, r10
009ABCBF  E8 1C BC 94 FF                  call 0x1402f78e0
009ABCC4  85 DB                           test ebx, ebx
009ABCC6  78 6E                           js 0x1409abd36
009ABCC8  8B 84 24 EC 00 00 00            mov eax, dword ptr [rsp + 0xec]
009ABCCF  89 06                           mov dword ptr [rsi], eax
009ABCD1  4D 85 E4                        test r12, r12
009ABCD4  74 08                           je 0x1409abcde
009ABCD6  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
009ABCDE  EB 56                           jmp 0x1409abd36
009ABCE0  8B D8                           mov ebx, eax
009ABCE2  EB 52                           jmp 0x1409abd36
009ABCE4  4C 8B 05 AD AD 61 00            mov r8, qword ptr [rip + 0x61adad]
009ABCEB  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ABCF0  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ABCF5  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ABCFA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ABCFF  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ABD07  45 0F B6 CD                     movzx r9d, r13b
009ABD0B  BA 10 04 00 00                  mov edx, 0x410
009ABD10  49 8B CF                        mov rcx, r15
009ABD13  E8 38 D9 EB FF                  call 0x140869650
009ABD18  85 C0                           test eax, eax
009ABD1A  0F 88 20 2A 00 00               js 0x1409ae740
009ABD20  E8 DB 08 B5 FF                  call 0x1404fc600
009ABD25  8B D8                           mov ebx, eax
009ABD27  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ABD2C  BA 50 73 51 79                  mov edx, 0x79517350
009ABD31  E8 AA BB 94 FF                  call 0x1402f78e0
009ABD36  8B C3                           mov eax, ebx
009ABD38  E9 03 2A 00 00                  jmp 0x1409ae740
009ABD3D  48 89 B4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rsi
009ABD45  8B C3                           mov eax, ebx
009ABD47  BF 40 00 00 00                  mov edi, 0x40
009ABD4C  48 89 BC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdi
009ABD54  48 89 3E                        mov qword ptr [rsi], rdi
009ABD57  EB 36                           jmp 0x1409abd8f
009ABD59  33 DB                           xor ebx, ebx
009ABD5B  48 C7 84 24 90 00 00 00 03 00 00 00  mov qword ptr [rsp + 0x90], 3
009ABD67  BF 40 00 00 00                  mov edi, 0x40
009ABD6C  48 89 BC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdi
009ABD74  44 0F B6 6C 24 4C               movzx r13d, byte ptr [rsp + 0x4c]
009ABD7A  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
009ABD7F  48 8B B4 24 28 01 00 00         mov rsi, qword ptr [rsp + 0x128]
009ABD87  4C 8B A4 24 30 01 00 00         mov r12, qword ptr [rsp + 0x130]
009ABD8F  85 C0                           test eax, eax
009ABD91  0F 88 A9 29 00 00               js 0x1409ae740
009ABD97  48 83 C6 08                     add rsi, 8
009ABD9B  E9 D9 E7 FF FF                  jmp 0x1409aa579
009ABDA0  48 89 9C 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rbx
009ABDA8  41 83 FE 04                     cmp r14d, 4
009ABDAC  0F 85 EF F7 FF FF               jne 0x1409ab5a1
009ABDB2  49 83 FF FF                     cmp r15, -1
009ABDB6  0F 85 83 0A 00 00               jne 0x1409ac83f
009ABDBC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009ABDC5  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
009ABDCC  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
009ABDD1  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009ABDD5  41 BD 01 00 00 00               mov r13d, 1
009ABDDB  8B 81 B8 02 00 00               mov eax, dword ptr [rcx + 0x2b8]
009ABDE1  85 C0                           test eax, eax
009ABDE3  0F 84 3A 0F 00 00               je 0x1409acd23
009ABDE9  89 06                           mov dword ptr [rsi], eax
009ABDEB  4D 85 E4                        test r12, r12
009ABDEE  74 08                           je 0x1409abdf8
009ABDF0  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
009ABDF8  EB 0C                           jmp 0x1409abe06
009ABDFA  8B D8                           mov ebx, eax
009ABDFC  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ABE01  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
009ABE06  49 83 FF FF                     cmp r15, -1
009ABE0A  0F 84 26 FF FF FF               je 0x1409abd36
009ABE10  E8 3B D5 94 FF                  call 0x1402f9350
009ABE15  8B C3                           mov eax, ebx
009ABE17  E9 24 29 00 00                  jmp 0x1409ae740
009ABE1C  41 83 FE 30                     cmp r14d, 0x30
009ABE20  0F 85 7B F7 FF FF               jne 0x1409ab5a1
009ABE26  4C 8B 05 6B AC 61 00            mov r8, qword ptr [rip + 0x61ac6b]
009ABE2D  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ABE32  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ABE37  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ABE3C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ABE41  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ABE49  45 0F B6 CD                     movzx r9d, r13b
009ABE4D  BA 00 10 00 00                  mov edx, 0x1000
009ABE52  49 8B CF                        mov rcx, r15
009ABE55  E8 F6 D7 EB FF                  call 0x140869650
009ABE5A  8B F8                           mov edi, eax
009ABE5C  85 C0                           test eax, eax
009ABE5E  0F 88 DC 28 00 00               js 0x1409ae740
009ABE64  48 8D 94 24 20 03 00 00         lea rdx, [rsp + 0x320]
009ABE6C  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ABE71  E8 DA D4 F6 FF                  call 0x140919350
009ABE76  48 8B 84 24 48 03 00 00         mov rax, qword ptr [rsp + 0x348]
009ABE7E  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
009ABE86  48 8B 84 24 50 03 00 00         mov rax, qword ptr [rsp + 0x350]
009ABE8E  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
009ABE96  48 8B 84 24 58 03 00 00         mov rax, qword ptr [rsp + 0x358]
009ABE9E  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
009ABEA6  48 8B 84 24 60 03 00 00         mov rax, qword ptr [rsp + 0x360]
009ABEAE  48 89 84 24 58 01 00 00         mov qword ptr [rsp + 0x158], rax
009ABEB6  48 8B 84 24 68 03 00 00         mov rax, qword ptr [rsp + 0x368]
009ABEBE  48 89 84 24 60 01 00 00         mov qword ptr [rsp + 0x160], rax
009ABEC6  48 8B 84 24 70 03 00 00         mov rax, qword ptr [rsp + 0x370]
009ABECE  48 89 84 24 68 01 00 00         mov qword ptr [rsp + 0x168], rax
009ABED6  BA 50 73 51 79                  mov edx, 0x79517350
009ABEDB  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ABEE0  E8 FB B9 94 FF                  call 0x1402f78e0
009ABEE5  90                              nop
009ABEE6  0F 28 84 24 40 01 00 00         movaps xmm0, xmmword ptr [rsp + 0x140]
009ABEEE  0F 11 06                        movups xmmword ptr [rsi], xmm0
009ABEF1  0F 28 8C 24 50 01 00 00         movaps xmm1, xmmword ptr [rsp + 0x150]
009ABEF9  0F 11 4E 10                     movups xmmword ptr [rsi + 0x10], xmm1
009ABEFD  0F 28 84 24 60 01 00 00         movaps xmm0, xmmword ptr [rsp + 0x160]
009ABF05  0F 11 46 20                     movups xmmword ptr [rsi + 0x20], xmm0
009ABF09  4D 85 E4                        test r12, r12
009ABF0C  74 04                           je 0x1409abf12
009ABF0E  45 89 34 24                     mov dword ptr [r12], r14d
009ABF12  E9 29 F1 FF FF                  jmp 0x1409ab040
009ABF17  8B F8                           mov edi, eax
009ABF19  E9 22 F1 FF FF                  jmp 0x1409ab040
009ABF1E  4C 8B 05 73 AB 61 00            mov r8, qword ptr [rip + 0x61ab73]
009ABF25  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ABF2A  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ABF2F  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ABF34  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ABF39  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ABF41  45 0F B6 CD                     movzx r9d, r13b
009ABF45  BA 00 10 00 00                  mov edx, 0x1000
009ABF4A  49 8B CF                        mov rcx, r15
009ABF4D  E8 FE D6 EB FF                  call 0x140869650
009ABF52  8B F8                           mov edi, eax
009ABF54  85 C0                           test eax, eax
009ABF56  0F 88 E4 F0 FF FF               js 0x1409ab040
009ABF5C  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
009ABF61  45 0F B6 CD                     movzx r9d, r13b
009ABF65  45 8B C6                        mov r8d, r14d
009ABF68  48 8B D6                        mov rdx, rsi
009ABF6B  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
009ABF70  48 8B CB                        mov rcx, rbx
009ABF73  E8 28 92 EF FF                  call 0x1408a51a0
009ABF78  8B F8                           mov edi, eax
009ABF7A  48 85 DB                        test rbx, rbx
009ABF7D  0F 85 B0 F0 FF FF               jne 0x1409ab033
009ABF83  E9 B8 F0 FF FF                  jmp 0x1409ab040
009ABF88  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009ABF8C  89 5E 04                        mov dword ptr [rsi + 4], ebx
009ABF8F  E8 2C CD AA FF                  call 0x140458cc0
009ABF94  8B 4E 04                        mov ecx, dword ptr [rsi + 4]
009ABF97  8B D1                           mov edx, ecx
009ABF99  33 D0                           xor edx, eax
009ABF9B  83 E2 0F                        and edx, 0xf
009ABF9E  33 D1                           xor edx, ecx
009ABFA0  89 56 04                        mov dword ptr [rsi + 4], edx
009ABFA3  E9 5E E5 FF FF                  jmp 0x1409aa506
009ABFA8  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009ABFAC  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
009ABFB1  E9 50 E5 FF FF                  jmp 0x1409aa506
009ABFB6  89 5C 24 58                     mov dword ptr [rsp + 0x58], ebx
009ABFBA  41 83 FE 20                     cmp r14d, 0x20
009ABFBE  0F 85 14 25 00 00               jne 0x1409ae4d8
009ABFC4  0F 10 06                        movups xmm0, xmmword ptr [rsi]
009ABFC7  0F 11 84 24 00 01 00 00         movups xmmword ptr [rsp + 0x100], xmm0
009ABFCF  0F 10 4E 10                     movups xmm1, xmmword ptr [rsi + 0x10]
009ABFD3  0F 11 8C 24 10 01 00 00         movups xmmword ptr [rsp + 0x110], xmm1
009ABFDB  EB 07                           jmp 0x1409abfe4
009ABFDD  8B F8                           mov edi, eax
009ABFDF  E9 F0 00 00 00                  jmp 0x1409ac0d4
009ABFE4  83 BC 24 00 01 00 00 03         cmp dword ptr [rsp + 0x100], 3
009ABFEC  0F 85 E2 1F 00 00               jne 0x1409adfd4
009ABFF2  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
009ABFFA  48 C1 E8 20                     shr rax, 0x20
009ABFFE  83 F8 08                        cmp eax, 8
009AC001  0F 83 80 1B 00 00               jae 0x1409adb87
009AC007  48 83 BC 24 08 01 00 00 00      cmp qword ptr [rsp + 0x108], 0
009AC010  0F 85 71 1B 00 00               jne 0x1409adb87
009AC016  4C 8B 05 7B AA 61 00            mov r8, qword ptr [rip + 0x61aa7b]
009AC01D  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AC022  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AC027  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AC02C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AC031  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AC039  45 0F B6 CD                     movzx r9d, r13b
009AC03D  BA 00 10 00 00                  mov edx, 0x1000
009AC042  49 8B CF                        mov rcx, r15
009AC045  E8 06 D6 EB FF                  call 0x140869650
009AC04A  8B F8                           mov edi, eax
009AC04C  85 C0                           test eax, eax
009AC04E  0F 88 80 00 00 00               js 0x1409ac0d4
009AC054  48 8D 84 24 18 01 00 00         lea rax, [rsp + 0x118]
009AC05C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009AC061  4C 8D 8C 24 10 01 00 00         lea r9, [rsp + 0x110]
009AC069  4C 8D 84 24 08 01 00 00         lea r8, [rsp + 0x108]
009AC071  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
009AC076  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AC07B  E8 38 C0 AD FF                  call 0x1404880b8
009AC080  8B 8C 24 04 01 00 00            mov ecx, dword ptr [rsp + 0x104]
009AC087  83 E1 FE                        and ecx, 0xfffffffe
009AC08A  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
009AC08E  83 E0 01                        and eax, 1
009AC091  0B C8                           or ecx, eax
009AC093  89 8C 24 04 01 00 00            mov dword ptr [rsp + 0x104], ecx
009AC09A  48 C1 A4 24 08 01 00 00 0C      shl qword ptr [rsp + 0x108], 0xc
009AC0A3  48 C1 A4 24 10 01 00 00 0C      shl qword ptr [rsp + 0x110], 0xc
009AC0AC  48 C1 A4 24 18 01 00 00 0C      shl qword ptr [rsp + 0x118], 0xc
009AC0B5  0F 10 84 24 00 01 00 00         movups xmm0, xmmword ptr [rsp + 0x100]
009AC0BD  0F 11 06                        movups xmmword ptr [rsi], xmm0
009AC0C0  0F 10 8C 24 10 01 00 00         movups xmm1, xmmword ptr [rsp + 0x110]
009AC0C8  0F 11 4E 10                     movups xmmword ptr [rsi + 0x10], xmm1
009AC0CC  EB 04                           jmp 0x1409ac0d2
009AC0CE  8B F8                           mov edi, eax
009AC0D0  EB 02                           jmp 0x1409ac0d4
009AC0D2  8B FB                           mov edi, ebx
009AC0D4  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AC0D9  E9 B6 F0 FF FF                  jmp 0x1409ab194
009AC0DE  41 83 FE 08                     cmp r14d, 8
009AC0E2  0F 84 73 13 00 00               je 0x1409ad45b
009AC0E8  4D 85 E4                        test r12, r12
009AC0EB  0F 84 B0 F4 FF FF               je 0x1409ab5a1
009AC0F1  E9 02 24 00 00                  jmp 0x1409ae4f8
009AC0F6  41 83 FE 04                     cmp r14d, 4
009AC0FA  0F 85 A1 F4 FF FF               jne 0x1409ab5a1
009AC100  4C 8B 05 91 A9 61 00            mov r8, qword ptr [rip + 0x61a991]
009AC107  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AC10C  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AC111  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AC116  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AC11B  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AC123  45 0F B6 CD                     movzx r9d, r13b
009AC127  BA 00 10 00 00                  mov edx, 0x1000
009AC12C  49 8B CF                        mov rcx, r15
009AC12F  E8 1C D5 EB FF                  call 0x140869650
009AC134  8B F8                           mov edi, eax
009AC136  85 C0                           test eax, eax
009AC138  0F 88 02 26 00 00               js 0x1409ae740
009AC13E  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AC143  48 83 B9 40 06 00 00 00         cmp qword ptr [rcx + 0x640], 0
009AC14B  0F 45 1D 1E A4 55 00            cmovne ebx, dword ptr [rip + 0x55a41e]
009AC152  89 1E                           mov dword ptr [rsi], ebx
009AC154  4D 85 E4                        test r12, r12
009AC157  74 04                           je 0x1409ac15d
009AC159  45 89 34 24                     mov dword ptr [r12], r14d
009AC15D  E9 D4 EE FF FF                  jmp 0x1409ab036
009AC162  8B F8                           mov edi, eax
009AC164  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AC169  E9 C8 EE FF FF                  jmp 0x1409ab036
009AC16E  4C 8B 05 23 A9 61 00            mov r8, qword ptr [rip + 0x61a923]
009AC175  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AC17A  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AC17F  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AC184  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AC189  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AC191  45 0F B6 CD                     movzx r9d, r13b
009AC195  BA 00 10 00 00                  mov edx, 0x1000
009AC19A  49 8B CF                        mov rcx, r15
009AC19D  E8 AE D4 EB FF                  call 0x140869650
009AC1A2  8B F8                           mov edi, eax
009AC1A4  85 C0                           test eax, eax
009AC1A6  0F 88 94 EE FF FF               js 0x1409ab040
009AC1AC  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
009AC1B1  45 0F B6 CD                     movzx r9d, r13b
009AC1B5  45 8B C6                        mov r8d, r14d
009AC1B8  48 8B D6                        mov rdx, rsi
009AC1BB  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
009AC1C0  48 8B CB                        mov rcx, rbx
009AC1C3  E8 48 D6 AB FF                  call 0x140469810
009AC1C8  E9 AB FD FF FF                  jmp 0x1409abf78
009AC1CD  83 FF 57                        cmp edi, 0x57
009AC1D0  0F 85 35 05 00 00               jne 0x1409ac70b
009AC1D6  41 83 FE 01                     cmp r14d, 1
009AC1DA  0F 82 C1 F3 FF FF               jb 0x1409ab5a1
009AC1E0  E9 26 05 00 00                  jmp 0x1409ac70b
009AC1E5  41 83 FE 08                     cmp r14d, 8
009AC1E9  0F 85 B2 F3 FF FF               jne 0x1409ab5a1
009AC1EF  E9 20 0D 00 00                  jmp 0x1409acf14
009AC1F4  89 5C 24 58                     mov dword ptr [rsp + 0x58], ebx
009AC1F8  41 83 FE 10                     cmp r14d, 0x10
009AC1FC  0F 82 9F F3 FF FF               jb 0x1409ab5a1
009AC202  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
009AC207  41 0F B6 CD                     movzx ecx, r13b
009AC20B  E8 D8 55 07 00                  call 0x140a217e8
009AC210  85 C0                           test eax, eax
009AC212  0F 85 6E F9 FF FF               jne 0x1409abb86
009AC218  41 8D 4E F0                     lea ecx, [r14 - 0x10]
009AC21C  48 B8 CD CC CC CC CC CC CC CC   movabs rax, 0xcccccccccccccccd
009AC226  48 F7 E1                        mul rcx
009AC229  48 C1 EA 07                     shr rdx, 7
009AC22D  48 89 94 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rdx
009AC235  48 8D 46 10                     lea rax, [rsi + 0x10]
009AC239  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
009AC241  4C 8B 05 50 A8 61 00            mov r8, qword ptr [rip + 0x61a850]
009AC248  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AC24D  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AC252  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AC257  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AC25C  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AC264  45 0F B6 CD                     movzx r9d, r13b
009AC268  BA 00 04 00 00                  mov edx, 0x400
009AC26D  49 8B CF                        mov rcx, r15
009AC270  E8 DB D3 EB FF                  call 0x140869650
009AC275  44 8B F8                        mov r15d, eax
009AC278  85 C0                           test eax, eax
009AC27A  0F 88 C0 24 00 00               js 0x1409ae740
009AC280  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009AC285  48 8B CF                        mov rcx, rdi
009AC288  E8 E3 78 EE FF                  call 0x140893b70
009AC28D  4C 8B E8                        mov r13, rax
009AC290  48 89 84 24 C8 01 00 00         mov qword ptr [rsp + 0x1c8], rax
009AC298  48 85 C0                        test rax, rax
009AC29B  0F 84 00 0D 00 00               je 0x1409acfa1
009AC2A1  48 8B C8                        mov rcx, rax
009AC2A4  E8 6F 5B 04 00                  call 0x1409f1e18
009AC2A9  4C 8B F0                        mov r14, rax
009AC2AC  48 89 84 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], rax
009AC2B4  48 85 C0                        test rax, rax
009AC2B7  0F 85 D1 12 00 00               jne 0x1409ad58e
009AC2BD  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
009AC2C3  E9 C6 14 00 00                  jmp 0x1409ad78e
009AC2C8  41 B6 01                        mov r14b, 1
009AC2CB  48 8D 8F E8 01 00 00            lea rcx, [rdi + 0x1e8]
009AC2D2  E8 49 A3 86 FF                  call 0x140216620
009AC2D7  84 C0                           test al, al
009AC2D9  0F 84 9B 11 00 00               je 0x1409ad47a
009AC2DF  48 8B 9F A8 02 00 00            mov rbx, qword ptr [rdi + 0x2a8]
009AC2E6  48 85 DB                        test rbx, rbx
009AC2E9  0F 84 80 11 00 00               je 0x1409ad46f
009AC2EF  48 8B CB                        mov rcx, rbx
009AC2F2  E8 29 37 86 FF                  call 0x14020fa20
009AC2F7  44 8B 7C 24 50                  mov r15d, dword ptr [rsp + 0x50]
009AC2FC  48 8D 8F E8 01 00 00            lea rcx, [rdi + 0x1e8]
009AC303  E8 78 DB 99 FF                  call 0x140349e80
009AC308  E9 1A F3 FF FF                  jmp 0x1409ab627
009AC30D  41 83 FE 10                     cmp r14d, 0x10
009AC311  0F 82 E4 11 00 00               jb 0x1409ad4fb
009AC317  4C 8B 05 7A A7 61 00            mov r8, qword ptr [rip + 0x61a77a]
009AC31E  48 89 9C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rbx
009AC326  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
009AC32B  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
009AC333  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009AC338  45 0F B6 CD                     movzx r9d, r13b
009AC33C  BA 00 04 00 00                  mov edx, 0x400
009AC341  49 8B CF                        mov rcx, r15
009AC344  E8 67 CA EB FF                  call 0x140868db0
009AC349  85 C0                           test eax, eax
009AC34B  0F 88 EF 23 00 00               js 0x1409ae740
009AC351  48 8B BC 24 C0 00 00 00         mov rdi, qword ptr [rsp + 0xc0]
009AC359  66 FF 8F E4 01 00 00            dec word ptr [rdi + 0x1e4]
009AC360  90                              nop
009AC361  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
009AC369  48 8B CB                        mov rcx, rbx
009AC36C  E8 FF 77 EE FF                  call 0x140893b70
009AC371  48 85 C0                        test rax, rax
009AC374  0F 84 25 14 00 00               je 0x1409ad79f
009AC37A  4D 8B CC                        mov r9, r12
009AC37D  45 8B C6                        mov r8d, r14d
009AC380  48 8B D6                        mov rdx, rsi
009AC383  48 8B C8                        mov rcx, rax
009AC386  E8 4D 00 FA FF                  call 0x14094c3d8
009AC38B  44 8B F8                        mov r15d, eax
009AC38E  48 8D 8B E8 01 00 00            lea rcx, [rbx + 0x1e8]
009AC395  E8 E6 DA 99 FF                  call 0x140349e80
009AC39A  E9 06 14 00 00                  jmp 0x1409ad7a5
009AC39F  41 83 FE 10                     cmp r14d, 0x10
009AC3A3  0F 85 F8 F1 FF FF               jne 0x1409ab5a1
009AC3A9  4C 8B 05 E8 A6 61 00            mov r8, qword ptr [rip + 0x61a6e8]
009AC3B0  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AC3B5  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AC3BA  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AC3BF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AC3C4  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AC3CC  45 0F B6 CD                     movzx r9d, r13b
009AC3D0  BA 00 10 00 00                  mov edx, 0x1000
009AC3D5  49 8B CF                        mov rcx, r15
009AC3D8  E8 73 D2 EB FF                  call 0x140869650
009AC3DD  8B F8                           mov edi, eax
009AC3DF  85 C0                           test eax, eax
009AC3E1  0F 88 59 23 00 00               js 0x1409ae740
009AC3E7  48 8D 94 24 E8 01 00 00         lea rdx, [rsp + 0x1e8]
009AC3EF  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
009AC3F4  48 8B CB                        mov rcx, rbx
009AC3F7  E8 44 A4 07 00                  call 0x140a26840
009AC3FC  90                              nop
009AC3FD  48 89 06                        mov qword ptr [rsi], rax
009AC400  48 8B 84 24 E8 01 00 00         mov rax, qword ptr [rsp + 0x1e8]
009AC408  48 89 46 08                     mov qword ptr [rsi + 8], rax
009AC40C  4D 85 E4                        test r12, r12
009AC40F  74 04                           je 0x1409ac415
009AC411  45 89 34 24                     mov dword ptr [r12], r14d
009AC415  E9 19 EC FF FF                  jmp 0x1409ab033
009AC41A  8B F8                           mov edi, eax
009AC41C  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
009AC421  E9 0D EC FF FF                  jmp 0x1409ab033
009AC426  44 88 6C 24 28                  mov byte ptr [rsp + 0x28], r13b
009AC42B  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
009AC430  45 8B CE                        mov r9d, r14d
009AC433  4C 8B C6                        mov r8, rsi
009AC436  8B D7                           mov edx, edi
009AC438  49 8B CF                        mov rcx, r15
009AC43B  E8 38 50 07 00                  call 0x140a21478
009AC440  E9 FB 22 00 00                  jmp 0x1409ae740
009AC445  41 83 FE 08                     cmp r14d, 8
009AC449  0F 85 52 F1 FF FF               jne 0x1409ab5a1
009AC44F  4C 8B 05 42 A6 61 00            mov r8, qword ptr [rip + 0x61a642]
009AC456  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AC45B  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AC460  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AC465  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AC46A  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AC472  45 0F B6 CD                     movzx r9d, r13b
009AC476  BA 00 10 00 00                  mov edx, 0x1000
009AC47B  49 8B CF                        mov rcx, r15
009AC47E  E8 CD D1 EB FF                  call 0x140869650
009AC483  8B D8                           mov ebx, eax
009AC485  85 C0                           test eax, eax
009AC487  0F 88 B3 22 00 00               js 0x1409ae740
009AC48D  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AC492  48 8B 81 78 06 00 00            mov rax, qword ptr [rcx + 0x678]
009AC499  48 89 06                        mov qword ptr [rsi], rax
009AC49C  4D 85 E4                        test r12, r12
009AC49F  74 04                           je 0x1409ac4a5
009AC4A1  45 89 34 24                     mov dword ptr [r12], r14d
009AC4A5  EB 07                           jmp 0x1409ac4ae
009AC4A7  8B D8                           mov ebx, eax
009AC4A9  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AC4AE  BA 50 73 51 79                  mov edx, 0x79517350
009AC4B3  E8 28 B4 94 FF                  call 0x1402f78e0
009AC4B8  8B C3                           mov eax, ebx
009AC4BA  E9 81 22 00 00                  jmp 0x1409ae740
009AC4BF  41 83 FE 04                     cmp r14d, 4
009AC4C3  0F 85 D8 F0 FF FF               jne 0x1409ab5a1
009AC4C9  44 89 0E                        mov dword ptr [rsi], r9d
009AC4CC  4D 85 E4                        test r12, r12
009AC4CF  74 04                           je 0x1409ac4d5
009AC4D1  45 89 34 24                     mov dword ptr [r12], r14d
009AC4D5  E9 1B EA FF FF                  jmp 0x1409aaef5
009AC4DA  E9 61 22 00 00                  jmp 0x1409ae740
009AC4DF  48 89 9C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rbx
009AC4E7  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
009AC4EC  41 83 FE 04                     cmp r14d, 4
009AC4F0  0F 82 AB F0 FF FF               jb 0x1409ab5a1
009AC4F6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009AC4FF  44 0F B6 80 32 02 00 00         movzx r8d, byte ptr [rax + 0x232]
009AC507  48 8D 44 24 58                  lea rax, [rsp + 0x58]
009AC50C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AC511  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
009AC519  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009AC51E  41 8B D6                        mov edx, r14d
009AC521  48 8B CE                        mov rcx, rsi
009AC524  E8 8F 6E FA FF                  call 0x1409533b8
009AC529  85 C0                           test eax, eax
009AC52B  0F 88 0F 22 00 00               js 0x1409ae740
009AC531  4C 8B 05 60 A5 61 00            mov r8, qword ptr [rip + 0x61a560]
009AC538  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AC53D  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AC542  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AC547  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AC54C  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AC554  45 0F B6 CD                     movzx r9d, r13b
009AC558  BA 40 04 00 00                  mov edx, 0x440
009AC55D  49 8B CF                        mov rcx, r15
009AC560  E8 EB D0 EB FF                  call 0x140869650
009AC565  8B F8                           mov edi, eax
009AC567  85 C0                           test eax, eax
009AC569  0F 88 54 1A 00 00               js 0x1409adfc3
009AC56F  0F 57 C0                        xorps xmm0, xmm0
009AC572  0F 11 84 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm0
009AC57A  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009AC57F  48 8B CF                        mov rcx, rdi
009AC582  E8 E9 75 EE FF                  call 0x140893b70
009AC587  48 85 C0                        test rax, rax
009AC58A  0F 84 9F 16 00 00               je 0x1409adc2f
009AC590  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
009AC598  48 89 8C 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rcx
009AC5A0  41 C1 EE 02                     shr r14d, 2
009AC5A4  44 89 B4 24 D8 00 00 00         mov dword ptr [rsp + 0xd8], r14d
009AC5AC  89 9C 24 DC 00 00 00            mov dword ptr [rsp + 0xdc], ebx
009AC5B3  45 33 C9                        xor r9d, r9d
009AC5B6  4C 8D 84 24 D0 00 00 00         lea r8, [rsp + 0xd0]
009AC5BE  48 8D 15 3B 7A 8F FF            lea rdx, [rip - 0x7085c5]
009AC5C5  48 8B C8                        mov rcx, rax
009AC5C8  E8 53 15 F7 FF                  call 0x14091db20
009AC5CD  48 8D 8F E8 01 00 00            lea rcx, [rdi + 0x1e8]
009AC5D4  E8 A7 D8 99 FF                  call 0x140349e80
009AC5D9  BA 50 73 51 79                  mov edx, 0x79517350
009AC5DE  48 8B CF                        mov rcx, rdi
009AC5E1  E8 FA B2 94 FF                  call 0x1402f78e0
009AC5E6  4D 85 E4                        test r12, r12
009AC5E9  0F 85 22 16 00 00               jne 0x1409adc11
009AC5EF  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
009AC5F4  E8 5F 2C 8F FF                  call 0x14029f258
009AC5F9  8B C3                           mov eax, ebx
009AC5FB  E9 40 21 00 00                  jmp 0x1409ae740
009AC600  41 83 FE 03                     cmp r14d, 3
009AC604  0F 85 97 EF FF FF               jne 0x1409ab5a1
009AC60A  49 83 FF FF                     cmp r15, -1
009AC60E  0F 85 9C 1B 00 00               jne 0x1409ae1b0
009AC614  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009AC61D  48 8B B8 B8 00 00 00            mov rdi, qword ptr [rax + 0xb8]
009AC624  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
009AC629  48 8B CF                        mov rcx, rdi
009AC62C  E8 87 AC 06 00                  call 0x140a172b8
009AC631  90                              nop
009AC632  33 C9                           xor ecx, ecx
009AC634  66 89 0E                        mov word ptr [rsi], cx
009AC637  88 4E 02                        mov byte ptr [rsi + 2], cl
009AC63A  83 F8 02                        cmp eax, 2
009AC63D  74 1E                           je 0x1409ac65d
009AC63F  83 E8 01                        sub eax, 1
009AC642  74 1D                           je 0x1409ac661
009AC644  83 F8 02                        cmp eax, 2
009AC647  75 04                           jne 0x1409ac64d
009AC649  C6 46 02 01                     mov byte ptr [rsi + 2], 1
009AC64D  4D 85 E4                        test r12, r12
009AC650  74 14                           je 0x1409ac666
009AC652  B8 03 00 00 00                  mov eax, 3
009AC657  41 89 04 24                     mov dword ptr [r12], eax
009AC65B  EB 09                           jmp 0x1409ac666
009AC65D  C6 46 01 01                     mov byte ptr [rsi + 1], 1
009AC661  C6 06 01                        mov byte ptr [rsi], 1
009AC664  EB E7                           jmp 0x1409ac64d
009AC666  EB 0C                           jmp 0x1409ac674
009AC668  8B D8                           mov ebx, eax
009AC66A  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009AC66F  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
009AC674  49 83 FF FF                     cmp r15, -1
009AC678  0F 84 B8 F6 FF FF               je 0x1409abd36
009AC67E  BA 50 73 51 79                  mov edx, 0x79517350
009AC683  48 8B CF                        mov rcx, rdi
009AC686  E8 55 B2 94 FF                  call 0x1402f78e0
009AC68B  8B C3                           mov eax, ebx
009AC68D  E9 AE 20 00 00                  jmp 0x1409ae740
009AC692  41 83 FE 08                     cmp r14d, 8
009AC696  0F 85 05 EF FF FF               jne 0x1409ab5a1
009AC69C  4C 8B 05 F5 A3 61 00            mov r8, qword ptr [rip + 0x61a3f5]
009AC6A3  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AC6A8  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AC6AD  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AC6B2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AC6B7  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AC6BF  45 0F B6 CD                     movzx r9d, r13b
009AC6C3  BA 00 04 00 00                  mov edx, 0x400
009AC6C8  49 8B CF                        mov rcx, r15
009AC6CB  E8 80 CF EB FF                  call 0x140869650
009AC6D0  85 C0                           test eax, eax
009AC6D2  0F 88 68 20 00 00               js 0x1409ae740
009AC6D8  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AC6DD  48 8B 81 08 03 00 00            mov rax, qword ptr [rcx + 0x308]
009AC6E4  48 F7 D8                        neg rax
009AC6E7  48 1B DB                        sbb rbx, rbx
009AC6EA  BA 50 73 51 79                  mov edx, 0x79517350
009AC6EF  E8 EC B1 94 FF                  call 0x1402f78e0
009AC6F4  90                              nop
009AC6F5  48 89 1E                        mov qword ptr [rsi], rbx
009AC6F8  4D 85 E4                        test r12, r12
009AC6FB  74 04                           je 0x1409ac701
009AC6FD  45 89 34 24                     mov dword ptr [r12], r14d
009AC701  E9 EF E7 FF FF                  jmp 0x1409aaef5
009AC706  E9 35 20 00 00                  jmp 0x1409ae740
009AC70B  83 FF 60                        cmp edi, 0x60
009AC70E  0F 84 EE 14 00 00               je 0x1409adc02
009AC714  4C 8B 05 7D A3 61 00            mov r8, qword ptr [rip + 0x61a37d]
009AC71B  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AC720  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AC725  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AC72A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AC72F  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AC737  45 0F B6 CD                     movzx r9d, r13b
009AC73B  BA 00 10 00 00                  mov edx, 0x1000
009AC740  49 8B CF                        mov rcx, r15
009AC743  E8 08 CF EB FF                  call 0x140869650
009AC748  8B D8                           mov ebx, eax
009AC74A  85 C0                           test eax, eax
009AC74C  0F 88 EE 1F 00 00               js 0x1409ae740
009AC752  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
009AC757  41 8B 80 F0 01 00 00            mov eax, dword ptr [r8 + 0x1f0]
009AC75E  C1 E8 18                        shr eax, 0x18
009AC761  24 03                           and al, 3
009AC763  88 06                           mov byte ptr [rsi], al
009AC765  83 FF 60                        cmp edi, 0x60
009AC768  75 34                           jne 0x1409ac79e
009AC76A  41 8B 88 FC 05 00 00            mov ecx, dword ptr [r8 + 0x5fc]
009AC771  8B D1                           mov edx, ecx
009AC773  C1 EA 02                        shr edx, 2
009AC776  81 E2 00 00 00 08               and edx, 0x8000000
009AC77C  8B C1                           mov eax, ecx
009AC77E  25 00 00 00 10                  and eax, 0x10000000
009AC783  0B D0                           or edx, eax
009AC785  C1 EA 06                        shr edx, 6
009AC788  8B C1                           mov eax, ecx
009AC78A  25 00 00 10 00                  and eax, 0x100000
009AC78F  0B D0                           or edx, eax
009AC791  81 E1 00 00 08 00               and ecx, 0x80000
009AC797  0B D1                           or edx, ecx
009AC799  C1 EA 11                        shr edx, 0x11
009AC79C  09 16                           or dword ptr [rsi], edx
009AC79E  EB 07                           jmp 0x1409ac7a7
009AC7A0  8B D8                           mov ebx, eax
009AC7A2  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
009AC7A7  49 8B C8                        mov rcx, r8
009AC7AA  BA 50 73 51 79                  mov edx, 0x79517350
009AC7AF  E8 2C B1 94 FF                  call 0x1402f78e0
009AC7B4  8B C3                           mov eax, ebx
009AC7B6  E9 85 1F 00 00                  jmp 0x1409ae740
009AC7BB  41 8D 46 F8                     lea eax, [r14 - 8]
009AC7BF  A9 F7 FF FF FF                  test eax, 0xfffffff7
009AC7C4  0F 85 D7 ED FF FF               jne 0x1409ab5a1
009AC7CA  4C 8B 05 C7 A2 61 00            mov r8, qword ptr [rip + 0x61a2c7]
009AC7D1  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AC7D6  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AC7DB  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AC7E0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AC7E5  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AC7ED  45 0F B6 CD                     movzx r9d, r13b
009AC7F1  BA 00 10 00 00                  mov edx, 0x1000
009AC7F6  49 8B CF                        mov rcx, r15
009AC7F9  E8 52 CE EB FF                  call 0x140869650
009AC7FE  44 8B F8                        mov r15d, eax
009AC801  85 C0                           test eax, eax
009AC803  0F 88 37 1F 00 00               js 0x1409ae740
009AC809  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009AC80E  F7 87 88 00 00 00 00 10 00 00   test dword ptr [rdi + 0x88], 0x1000
009AC818  0F 84 5E 11 00 00               je 0x1409ad97c
009AC81E  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
009AC824  E9 6B F2 FF FF                  jmp 0x1409aba94
009AC829  B8 40 00 00 00                  mov eax, 0x40
009AC82E  41 89 04 24                     mov dword ptr [r12], eax
009AC832  E9 6A F2 FF FF                  jmp 0x1409abaa1
009AC837  44 8B F8                        mov r15d, eax
009AC83A  E9 62 F2 FF FF                  jmp 0x1409abaa1
009AC83F  4C 8B 05 52 A2 61 00            mov r8, qword ptr [rip + 0x61a252]
009AC846  48 89 9C 24 F8 01 00 00         mov qword ptr [rsp + 0x1f8], rbx
009AC84E  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
009AC853  48 8D 84 24 F8 01 00 00         lea rax, [rsp + 0x1f8]
009AC85B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009AC860  45 0F B6 CD                     movzx r9d, r13b
009AC864  BA 20 00 00 00                  mov edx, 0x20
009AC869  49 8B CF                        mov rcx, r15
009AC86C  E8 3F C5 EB FF                  call 0x140868db0
009AC871  48 8B 8C 24 F8 01 00 00         mov rcx, qword ptr [rsp + 0x1f8]
009AC879  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
009AC87E  85 C0                           test eax, eax
009AC880  0F 88 BA 1E 00 00               js 0x1409ae740
009AC886  E9 46 F5 FF FF                  jmp 0x1409abdd1
009AC88B  41 83 FE 28                     cmp r14d, 0x28
009AC88F  0F 85 0C ED FF FF               jne 0x1409ab5a1
009AC895  4C 8B 05 FC A1 61 00            mov r8, qword ptr [rip + 0x61a1fc]
009AC89C  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AC8A1  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AC8A6  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AC8AB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AC8B0  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AC8B8  45 0F B6 CD                     movzx r9d, r13b
009AC8BC  BA 00 10 00 00                  mov edx, 0x1000
009AC8C1  49 8B CF                        mov rcx, r15
009AC8C4  E8 87 CD EB FF                  call 0x140869650
009AC8C9  85 C0                           test eax, eax
009AC8CB  0F 88 6F 1E 00 00               js 0x1409ae740
009AC8D1  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AC8D6  48 8B 88 A0 02 00 00            mov rcx, qword ptr [rax + 0x2a0]
009AC8DD  48 85 C9                        test rcx, rcx
009AC8E0  0F 84 DE 15 00 00               je 0x1409adec4
009AC8E6  4C 8D 84 24 60 04 00 00         lea r8, [rsp + 0x460]
009AC8EE  33 D2                           xor edx, edx
009AC8F0  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AC8F5  E8 26 9F 86 FF                  call 0x140216820
009AC8FA  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
009AC8FF  45 8B CE                        mov r9d, r14d
009AC902  4C 8D 84 24 90 04 00 00         lea r8, [rsp + 0x490]
009AC90A  41 8D 56 F4                     lea edx, [r14 - 0xc]
009AC90E  33 C9                           xor ecx, ecx
009AC910  E8 9B 32 D0 FF                  call 0x1406afbb0
009AC915  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
009AC91A  45 8D 4E 70                     lea r9d, [r14 + 0x70]
009AC91E  4C 8D 84 24 D0 05 00 00         lea r8, [rsp + 0x5d0]
009AC926  41 8D 56 E1                     lea edx, [r14 - 0x1f]
009AC92A  33 C9                           xor ecx, ecx
009AC92C  E8 7F 32 D0 FF                  call 0x1406afbb0
009AC931  33 D2                           xor edx, edx
009AC933  48 8D 8C 24 60 04 00 00         lea rcx, [rsp + 0x460]
009AC93B  E8 F0 B3 86 FF                  call 0x140217d30
009AC940  48 8B 84 24 90 04 00 00         mov rax, qword ptr [rsp + 0x490]
009AC948  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
009AC950  48 8B 84 24 98 04 00 00         mov rax, qword ptr [rsp + 0x498]
009AC958  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
009AC960  48 8B 84 24 A0 04 00 00         mov rax, qword ptr [rsp + 0x4a0]
009AC968  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
009AC970  F7 84 24 E0 05 00 00 00 00 20 00  test dword ptr [rsp + 0x5e0], 0x200000
009AC97B  48 8B 84 24 60 01 00 00         mov rax, qword ptr [rsp + 0x160]
009AC983  48 0F 45 84 24 60 06 00 00      cmovne rax, qword ptr [rsp + 0x660]
009AC98C  48 89 84 24 60 01 00 00         mov qword ptr [rsp + 0x160], rax
009AC994  F7 84 24 E0 05 00 00 00 02 00 00  test dword ptr [rsp + 0x5e0], 0x200
009AC99F  48 8B 84 24 58 01 00 00         mov rax, qword ptr [rsp + 0x158]
009AC9A7  48 0F 45 84 24 48 06 00 00      cmovne rax, qword ptr [rsp + 0x648]
009AC9B0  48 89 84 24 58 01 00 00         mov qword ptr [rsp + 0x158], rax
009AC9B8  0F 28 84 24 40 01 00 00         movaps xmm0, xmmword ptr [rsp + 0x140]
009AC9C0  0F 11 06                        movups xmmword ptr [rsi], xmm0
009AC9C3  0F 28 8C 24 50 01 00 00         movaps xmm1, xmmword ptr [rsp + 0x150]
009AC9CB  0F 11 4E 10                     movups xmmword ptr [rsi + 0x10], xmm1
009AC9CF  F2 0F 10 84 24 60 01 00 00      movsd xmm0, qword ptr [rsp + 0x160]
009AC9D8  F2 0F 11 46 20                  movsd qword ptr [rsi + 0x20], xmm0
009AC9DD  4D 85 E4                        test r12, r12
009AC9E0  74 04                           je 0x1409ac9e6
009AC9E2  45 89 34 24                     mov dword ptr [r12], r14d
009AC9E6  E9 3C F3 FF FF                  jmp 0x1409abd27
009AC9EB  8B D8                           mov ebx, eax
009AC9ED  E9 35 F3 FF FF                  jmp 0x1409abd27
009AC9F2  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009AC9F6  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AC9FB  E8 A8 9F 0C 00                  call 0x140a769a8
009ACA00  90                              nop
009ACA01  89 5E 04                        mov dword ptr [rsi + 4], ebx
009ACA04  83 E8 01                        sub eax, 1
009ACA07  74 10                           je 0x1409aca19
009ACA09  83 F8 01                        cmp eax, 1
009ACA0C  75 13                           jne 0x1409aca21
009ACA0E  8B 46 04                        mov eax, dword ptr [rsi + 4]
009ACA11  83 C8 02                        or eax, 2
009ACA14  89 46 04                        mov dword ptr [rsi + 4], eax
009ACA17  EB 08                           jmp 0x1409aca21
009ACA19  8B 46 04                        mov eax, dword ptr [rsi + 4]
009ACA1C  83 C8 01                        or eax, 1
009ACA1F  EB F3                           jmp 0x1409aca14
009ACA21  E9 E0 DA FF FF                  jmp 0x1409aa506
009ACA26  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009ACA2A  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
009ACA2F  E9 D2 DA FF FF                  jmp 0x1409aa506
009ACA34  41 83 FE 04                     cmp r14d, 4
009ACA38  0F 85 63 EB FF FF               jne 0x1409ab5a1
009ACA3E  4C 8B 05 53 A0 61 00            mov r8, qword ptr [rip + 0x61a053]
009ACA45  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ACA4A  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ACA4F  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ACA54  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ACA59  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ACA61  45 0F B6 CD                     movzx r9d, r13b
009ACA65  BA 00 10 00 00                  mov edx, 0x1000
009ACA6A  49 8B CF                        mov rcx, r15
009ACA6D  E8 DE CB EB FF                  call 0x140869650
009ACA72  8B D8                           mov ebx, eax
009ACA74  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009ACA78  85 C0                           test eax, eax
009ACA7A  0F 88 C0 1C 00 00               js 0x1409ae740
009ACA80  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009ACA85  8B 88 F4 01 00 00               mov ecx, dword ptr [rax + 0x1f4]
009ACA8B  C1 E9 1B                        shr ecx, 0x1b
009ACA8E  83 E1 07                        and ecx, 7
009ACA91  83 FF 21                        cmp edi, 0x21
009ACA94  75 11                           jne 0x1409acaa7
009ACA96  89 0E                           mov dword ptr [rsi], ecx
009ACA98  4D 85 E4                        test r12, r12
009ACA9B  74 29                           je 0x1409acac6
009ACA9D  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
009ACAA5  EB 1F                           jmp 0x1409acac6
009ACAA7  48 8B 80 A0 02 00 00            mov rax, qword ptr [rax + 0x2a0]
009ACAAE  48 85 C0                        test rax, rax
009ACAB1  74 0B                           je 0x1409acabe
009ACAB3  8B 80 3C 04 00 00               mov eax, dword ptr [rax + 0x43c]
009ACAB9  3B C8                           cmp ecx, eax
009ACABB  0F 4D C8                        cmovge ecx, eax
009ACABE  89 0E                           mov dword ptr [rsi], ecx
009ACAC0  8B 5C 24 48                     mov ebx, dword ptr [rsp + 0x48]
009ACAC4  EB D2                           jmp 0x1409aca98
009ACAC6  E9 5C F2 FF FF                  jmp 0x1409abd27
009ACACB  8B D8                           mov ebx, eax
009ACACD  E9 55 F2 FF FF                  jmp 0x1409abd27
009ACAD2  41 83 FE 04                     cmp r14d, 4
009ACAD6  0F 85 C5 EA FF FF               jne 0x1409ab5a1
009ACADC  4C 8B 05 B5 9F 61 00            mov r8, qword ptr [rip + 0x619fb5]
009ACAE3  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ACAE8  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ACAED  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ACAF2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ACAF7  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ACAFF  45 0F B6 CD                     movzx r9d, r13b
009ACB03  BA 00 10 00 00                  mov edx, 0x1000
009ACB08  49 8B CF                        mov rcx, r15
009ACB0B  E8 40 CB EB FF                  call 0x140869650
009ACB10  8B D8                           mov ebx, eax
009ACB12  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009ACB16  85 C0                           test eax, eax
009ACB18  0F 88 22 1C 00 00               js 0x1409ae740
009ACB1E  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009ACB23  8B 88 F0 01 00 00               mov ecx, dword ptr [rax + 0x1f0]
009ACB29  C1 E9 0C                        shr ecx, 0xc
009ACB2C  83 E1 07                        and ecx, 7
009ACB2F  83 FF 27                        cmp edi, 0x27
009ACB32  75 11                           jne 0x1409acb45
009ACB34  89 0E                           mov dword ptr [rsi], ecx
009ACB36  4D 85 E4                        test r12, r12
009ACB39  74 29                           je 0x1409acb64
009ACB3B  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
009ACB43  EB 1F                           jmp 0x1409acb64
009ACB45  48 8B 80 A0 02 00 00            mov rax, qword ptr [rax + 0x2a0]
009ACB4C  48 85 C0                        test rax, rax
009ACB4F  74 0B                           je 0x1409acb5c
009ACB51  8B 80 44 04 00 00               mov eax, dword ptr [rax + 0x444]
009ACB57  3B C8                           cmp ecx, eax
009ACB59  0F 43 C8                        cmovae ecx, eax
009ACB5C  89 0E                           mov dword ptr [rsi], ecx
009ACB5E  8B 5C 24 48                     mov ebx, dword ptr [rsp + 0x48]
009ACB62  EB D2                           jmp 0x1409acb36
009ACB64  E9 BE F1 FF FF                  jmp 0x1409abd27
009ACB69  8B D8                           mov ebx, eax
009ACB6B  E9 B7 F1 FF FF                  jmp 0x1409abd27
009ACB70  41 83 FE 08                     cmp r14d, 8
009ACB74  0F 85 27 EA FF FF               jne 0x1409ab5a1
009ACB7A  49 83 FF FF                     cmp r15, -1
009ACB7E  0F 85 E8 16 00 00               jne 0x1409ae26c
009ACB84  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009ACB8D  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
009ACB94  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
009ACB99  89 1E                           mov dword ptr [rsi], ebx
009ACB9B  8B D3                           mov edx, ebx
009ACB9D  F7 81 50 07 00 00 00 40 00 00   test dword ptr [rcx + 0x750], 0x4000
009ACBA7  74 06                           je 0x1409acbaf
009ACBA9  44 89 0E                        mov dword ptr [rsi], r9d
009ACBAC  41 8B D1                        mov edx, r9d
009ACBAF  F7 81 50 07 00 00 00 80 00 00   test dword ptr [rcx + 0x750], 0x8000
009ACBB9  74 05                           je 0x1409acbc0
009ACBBB  83 CA 02                        or edx, 2
009ACBBE  89 16                           mov dword ptr [rsi], edx
009ACBC0  8B 81 E8 06 00 00               mov eax, dword ptr [rcx + 0x6e8]
009ACBC6  89 46 04                        mov dword ptr [rsi + 4], eax
009ACBC9  4D 85 E4                        test r12, r12
009ACBCC  0F 84 E6 16 00 00               je 0x1409ae2b8
009ACBD2  41 C7 04 24 08 00 00 00         mov dword ptr [r12], 8
009ACBDA  E9 D9 16 00 00                  jmp 0x1409ae2b8
009ACBDF  41 83 FE 08                     cmp r14d, 8
009ACBE3  0F 85 B8 E9 FF FF               jne 0x1409ab5a1
009ACBE9  4C 8B 05 A8 9E 61 00            mov r8, qword ptr [rip + 0x619ea8]
009ACBF0  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ACBF5  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ACBFA  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ACBFF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ACC04  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ACC0C  45 0F B6 CD                     movzx r9d, r13b
009ACC10  BA 00 10 00 00                  mov edx, 0x1000
009ACC15  49 8B CF                        mov rcx, r15
009ACC18  E8 33 CA EB FF                  call 0x140869650
009ACC1D  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009ACC21  85 C0                           test eax, eax
009ACC23  0F 88 17 1B 00 00               js 0x1409ae740
009ACC29  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ACC2E  F7 81 F0 01 00 00 00 80 00 00   test dword ptr [rcx + 0x1f0], 0x8000
009ACC38  0F 84 BE 17 00 00               je 0x1409ae3fc
009ACC3E  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
009ACC43  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009ACC48  48 8B 80 60 07 00 00            mov rax, qword ptr [rax + 0x760]
009ACC4F  48 89 06                        mov qword ptr [rsi], rax
009ACC52  4D 85 E4                        test r12, r12
009ACC55  0F 84 B5 17 00 00               je 0x1409ae410
009ACC5B  45 89 34 24                     mov dword ptr [r12], r14d
009ACC5F  E9 AC 17 00 00                  jmp 0x1409ae410
009ACC64  0F 57 C0                        xorps xmm0, xmm0
009ACC67  0F 11 84 24 50 04 00 00         movups xmmword ptr [rsp + 0x450], xmm0
009ACC6F  41 83 FE 10                     cmp r14d, 0x10
009ACC73  0F 85 28 E9 FF FF               jne 0x1409ab5a1
009ACC79  49 83 FF FF                     cmp r15, -1
009ACC7D  0F 85 E2 07 00 00               jne 0x1409ad465
009ACC83  45 84 ED                        test r13b, r13b
009ACC86  0F 84 98 17 00 00               je 0x1409ae424
009ACC8C  45 8B C6                        mov r8d, r14d
009ACC8F  48 8B D6                        mov rdx, rsi
009ACC92  48 8D 8C 24 50 04 00 00         lea rcx, [rsp + 0x450]
009ACC9A  E8 31 FD D0 FF                  call 0x1406bc9d0
009ACC9F  40 F6 C6 03                     test sil, 3
009ACCA3  74 06                           je 0x1409accab
009ACCA5  E8 26 D3 EE FF                  call 0x140899fd0
009ACCAA  CC                              int3
009ACCAB  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
009ACCB5  48 3B F2                        cmp rsi, rdx
009ACCB8  48 0F 42 D6                     cmovb rdx, rsi
009ACCBC  8B 02                           mov eax, dword ptr [rdx]
009ACCBE  89 02                           mov dword ptr [rdx], eax
009ACCC0  EB 05                           jmp 0x1409accc7
009ACCC2  E9 79 1A 00 00                  jmp 0x1409ae740
009ACCC7  48 8D BC 24 50 04 00 00         lea rdi, [rsp + 0x450]
009ACCCF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009ACCD8  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
009ACCDF  8B 57 04                        mov edx, dword ptr [rdi + 4]
009ACCE2  4C 8B CF                        mov r9, rdi
009ACCE5  4C 8B 47 08                     mov r8, qword ptr [rdi + 8]
009ACCE9  E8 3E C1 12 00                  call 0x140ad8e2c
009ACCEE  8B C8                           mov ecx, eax
009ACCF0  3D 25 02 00 C0                  cmp eax, 0xc0000225
009ACCF5  0F 85 5D 18 00 00               jne 0x1409ae558
009ACCFB  89 1F                           mov dword ptr [rdi], ebx
009ACCFD  8B CB                           mov ecx, ebx
009ACCFF  45 84 ED                        test r13b, r13b
009ACD02  0F 84 24 17 00 00               je 0x1409ae42c
009ACD08  8B 07                           mov eax, dword ptr [rdi]
009ACD0A  89 06                           mov dword ptr [rsi], eax
009ACD0C  4D 85 E4                        test r12, r12
009ACD0F  74 08                           je 0x1409acd19
009ACD11  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
009ACD19  E9 1B 17 00 00                  jmp 0x1409ae439
009ACD1E  E9 1D 1A 00 00                  jmp 0x1409ae740
009ACD23  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
009ACD2B  E8 10 0D 9D FF                  call 0x14037da40
009ACD30  65 48 8B 3C 25 20 00 00 00      mov rdi, qword ptr gs:[0x20]
009ACD39  33 C9                           xor ecx, ecx
009ACD3B  E8 A0 1A 9D FF                  call 0x14037e7e0
009ACD40  48 8B D8                        mov rbx, rax
009ACD43  41 8B CD                        mov ecx, r13d
009ACD46  E8 C5 E2 A6 FF                  call 0x14041b010
009ACD4B  8B C8                           mov ecx, eax
009ACD4D  0F 31                           rdtsc
009ACD4F  48 C1 E2 20                     shl rdx, 0x20
009ACD53  48 0B C2                        or rax, rdx
009ACD56  33 C8                           xor ecx, eax
009ACD58  8B 97 10 2D 00 00               mov edx, dword ptr [rdi + 0x2d10]
009ACD5E  33 D1                           xor edx, ecx
009ACD60  44 8B 87 38 2D 00 00            mov r8d, dword ptr [rdi + 0x2d38]
009ACD67  44 33 87 50 86 00 00            xor r8d, dword ptr [rdi + 0x8650]
009ACD6E  44 33 87 40 86 00 00            xor r8d, dword ptr [rdi + 0x8640]
009ACD75  44 33 C3                        xor r8d, ebx
009ACD78  44 33 C2                        xor r8d, edx
009ACD7B  44 33 84 24 E4 00 00 00         xor r8d, dword ptr [rsp + 0xe4]
009ACD83  44 33 84 24 E0 00 00 00         xor r8d, dword ptr [rsp + 0xe0]
009ACD8B  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ACD90  33 C0                           xor eax, eax
009ACD92  F0 44 0F B1 81 B8 02 00 00      lock cmpxchg dword ptr [rcx + 0x2b8], r8d
009ACD9B  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ACDA0  8B 5C 24 48                     mov ebx, dword ptr [rsp + 0x48]
009ACDA4  E9 32 F0 FF FF                  jmp 0x1409abddb
009ACDA9  66 45 85 ED                     test r13w, r13w
009ACDAD  0F 84 D0 EC FF FF               je 0x1409aba83
009ACDB3  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009ACDBC  4C 8B 80 B8 00 00 00            mov r8, qword ptr [rax + 0xb8]
009ACDC3  0F B7 84 24 D0 00 00 00         movzx eax, word ptr [rsp + 0xd0]
009ACDCB  4C 8D 4E 06                     lea r9, [rsi + 6]
009ACDCF  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
009ACDD3  48 8D 8C 24 C0 02 00 00         lea rcx, [rsp + 0x2c0]
009ACDDB  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
009ACDE0  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
009ACDE5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009ACDEA  48 8B 94 24 D8 00 00 00         mov rdx, qword ptr [rsp + 0xd8]
009ACDF2  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009ACDF7  48 8B CF                        mov rcx, rdi
009ACDFA  E8 51 ED 00 00                  call 0x1409bbb50
009ACDFF  44 8B F8                        mov r15d, eax
009ACE02  E9 81 EC FF FF                  jmp 0x1409aba88
009ACE07  89 5C 24 58                     mov dword ptr [rsp + 0x58], ebx
009ACE0B  41 8D 46 FC                     lea eax, [r14 - 4]
009ACE0F  A9 FB FF FF FF                  test eax, 0xfffffffb
009ACE14  0F 85 87 E7 FF FF               jne 0x1409ab5a1
009ACE1A  4C 8B 05 77 9C 61 00            mov r8, qword ptr [rip + 0x619c77]
009ACE21  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ACE26  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ACE2B  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ACE30  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ACE35  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ACE3D  45 0F B6 CD                     movzx r9d, r13b
009ACE41  BA 00 10 00 00                  mov edx, 0x1000
009ACE46  49 8B CF                        mov rcx, r15
009ACE49  E8 02 C8 EB FF                  call 0x140869650
009ACE4E  85 C0                           test eax, eax
009ACE50  0F 88 EA 18 00 00               js 0x1409ae740
009ACE56  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
009ACE5B  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ACE60  E8 6B C7 F6 FF                  call 0x1409195d0
009ACE65  8B F8                           mov edi, eax
009ACE67  BA 50 73 51 79                  mov edx, 0x79517350
009ACE6C  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ACE71  E8 6A AA 94 FF                  call 0x1402f78e0
009ACE76  90                              nop
009ACE77  89 3E                           mov dword ptr [rsi], edi
009ACE79  41 83 FE 04                     cmp r14d, 4
009ACE7D  74 07                           je 0x1409ace86
009ACE7F  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
009ACE83  89 46 04                        mov dword ptr [rsi + 4], eax
009ACE86  4D 85 E4                        test r12, r12
009ACE89  74 08                           je 0x1409ace93
009ACE8B  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
009ACE93  E9 5D E0 FF FF                  jmp 0x1409aaef5
009ACE98  E9 A3 18 00 00                  jmp 0x1409ae740
009ACE9D  41 83 FE 04                     cmp r14d, 4
009ACEA1  0F 85 FA E6 FF FF               jne 0x1409ab5a1
009ACEA7  4C 8B 05 EA 9B 61 00            mov r8, qword ptr [rip + 0x619bea]
009ACEAE  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ACEB3  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ACEB8  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ACEBD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ACEC2  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ACECA  45 0F B6 CD                     movzx r9d, r13b
009ACECE  BA 00 10 00 00                  mov edx, 0x1000
009ACED3  49 8B CF                        mov rcx, r15
009ACED6  E8 75 C7 EB FF                  call 0x140869650
009ACEDB  85 C0                           test eax, eax
009ACEDD  0F 88 5D 18 00 00               js 0x1409ae740
009ACEE3  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ACEE8  8B 99 F4 01 00 00               mov ebx, dword ptr [rcx + 0x1f4]
009ACEEE  C1 EB 0D                        shr ebx, 0xd
009ACEF1  83 E3 01                        and ebx, 1
009ACEF4  BA 50 73 51 79                  mov edx, 0x79517350
009ACEF9  E8 E2 A9 94 FF                  call 0x1402f78e0
009ACEFE  90                              nop
009ACEFF  89 1E                           mov dword ptr [rsi], ebx
009ACF01  4D 85 E4                        test r12, r12
009ACF04  74 04                           je 0x1409acf0a
009ACF06  45 89 34 24                     mov dword ptr [r12], r14d
009ACF0A  E9 E6 DF FF FF                  jmp 0x1409aaef5
009ACF0F  E9 2C 18 00 00                  jmp 0x1409ae740
009ACF14  4C 8B 05 7D 9B 61 00            mov r8, qword ptr [rip + 0x619b7d]
009ACF1B  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ACF20  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ACF25  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ACF2A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ACF2F  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ACF37  45 0F B6 CD                     movzx r9d, r13b
009ACF3B  BA 00 10 00 00                  mov edx, 0x1000
009ACF40  49 8B CF                        mov rcx, r15
009ACF43  E8 08 C7 EB FF                  call 0x140869650
009ACF48  85 C0                           test eax, eax
009ACF4A  0F 88 F0 17 00 00               js 0x1409ae740
009ACF50  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009ACF55  48 8B 98 D8 02 00 00            mov rbx, qword ptr [rax + 0x2d8]
009ACF5C  BA 50 73 51 79                  mov edx, 0x79517350
009ACF61  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ACF66  E8 75 A9 94 FF                  call 0x1402f78e0
009ACF6B  90                              nop
009ACF6C  48 89 1E                        mov qword ptr [rsi], rbx
009ACF6F  4D 85 E4                        test r12, r12
009ACF72  74 08                           je 0x1409acf7c
009ACF74  41 C7 04 24 08 00 00 00         mov dword ptr [r12], 8
009ACF7C  E9 74 DF FF FF                  jmp 0x1409aaef5
009ACF81  E9 BA 17 00 00                  jmp 0x1409ae740
009ACF86  44 88 6C 24 20                  mov byte ptr [rsp + 0x20], r13b
009ACF8B  4D 8B CC                        mov r9, r12
009ACF8E  45 8B C6                        mov r8d, r14d
009ACF91  48 8B D6                        mov rdx, rsi
009ACF94  49 8B CF                        mov rcx, r15
009ACF97  E8 DC E6 11 00                  call 0x140acb678
009ACF9C  E9 9F 17 00 00                  jmp 0x1409ae740
009ACFA1  41 BF 0A 01 00 C0               mov r15d, 0xc000010a
009ACFA7  E9 E8 EA FF FF                  jmp 0x1409aba94
009ACFAC  41 83 FE 04                     cmp r14d, 4
009ACFB0  0F 85 EB E5 FF FF               jne 0x1409ab5a1
009ACFB6  4C 8B 05 DB 9A 61 00            mov r8, qword ptr [rip + 0x619adb]
009ACFBD  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ACFC2  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ACFC7  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ACFCC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ACFD1  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ACFD9  45 0F B6 CD                     movzx r9d, r13b
009ACFDD  BA 00 04 00 00                  mov edx, 0x400
009ACFE2  49 8B CF                        mov rcx, r15
009ACFE5  E8 66 C6 EB FF                  call 0x140869650
009ACFEA  8B F8                           mov edi, eax
009ACFEC  85 C0                           test eax, eax
009ACFEE  0F 88 4C E0 FF FF               js 0x1409ab040
009ACFF4  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ACFF9  0F B6 99 F7 01 00 00            movzx ebx, byte ptr [rcx + 0x1f7]
009AD000  83 E3 01                        and ebx, 1
009AD003  BA 50 73 51 79                  mov edx, 0x79517350
009AD008  E8 D3 A8 94 FF                  call 0x1402f78e0
009AD00D  90                              nop
009AD00E  89 1E                           mov dword ptr [rsi], ebx
009AD010  4D 85 E4                        test r12, r12
009AD013  74 04                           je 0x1409ad019
009AD015  45 89 34 24                     mov dword ptr [r12], r14d
009AD019  E9 22 E0 FF FF                  jmp 0x1409ab040
009AD01E  E9 1D 17 00 00                  jmp 0x1409ae740
009AD023  0F 57 C0                        xorps xmm0, xmm0
009AD026  0F 11 84 24 D8 02 00 00         movups xmmword ptr [rsp + 0x2d8], xmm0
009AD02E  0F 11 84 24 E8 02 00 00         movups xmmword ptr [rsp + 0x2e8], xmm0
009AD036  4C 8B 05 5B 9A 61 00            mov r8, qword ptr [rip + 0x619a5b]
009AD03D  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AD042  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AD047  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AD04C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AD051  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AD059  45 0F B6 CD                     movzx r9d, r13b
009AD05D  BA 00 10 00 00                  mov edx, 0x1000
009AD062  49 8B CF                        mov rcx, r15
009AD065  E8 E6 C5 EB FF                  call 0x140869650
009AD06A  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AD06E  85 C0                           test eax, eax
009AD070  0F 88 CA 16 00 00               js 0x1409ae740
009AD076  48 8B 94 24 C0 00 00 00         mov rdx, qword ptr [rsp + 0xc0]
009AD07E  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009AD083  48 8B CF                        mov rcx, rdi
009AD086  E8 45 46 A5 FF                  call 0x1404016d0
009AD08B  4C 8B BF A0 06 00 00            mov r15, qword ptr [rdi + 0x6a0]
009AD092  49 8B C7                        mov rax, r15
009AD095  48 C1 E8 3D                     shr rax, 0x3d
009AD099  48 83 F8 04                     cmp rax, 4
009AD09D  74 1F                           je 0x1409ad0be
009AD09F  48 83 F8 03                     cmp rax, 3
009AD0A3  74 19                           je 0x1409ad0be
009AD0A5  4C 8B BC 24 60 01 00 00         mov r15, qword ptr [rsp + 0x160]
009AD0AD  4C 8B AC 24 58 01 00 00         mov r13, qword ptr [rsp + 0x158]
009AD0B5  8B 94 24 70 01 00 00            mov edx, dword ptr [rsp + 0x170]
009AD0BC  EB 44                           jmp 0x1409ad102
009AD0BE  48 B9 FF FF FF FF FF FF FF 1F   movabs rcx, 0x1fffffffffffffff
009AD0C8  4C 23 F9                        and r15, rcx
009AD0CB  4C 89 BC 24 60 01 00 00         mov qword ptr [rsp + 0x160], r15
009AD0D3  4C 8B AF 98 06 00 00            mov r13, qword ptr [rdi + 0x698]
009AD0DA  4C 89 AC 24 50 01 00 00         mov qword ptr [rsp + 0x150], r13
009AD0E2  4C 2B AF 80 06 00 00            sub r13, qword ptr [rdi + 0x680]
009AD0E9  4C 89 AC 24 58 01 00 00         mov qword ptr [rsp + 0x158], r13
009AD0F1  48 83 F8 03                     cmp rax, 3
009AD0F5  75 BE                           jne 0x1409ad0b5
009AD0F7  8B 94 24 70 01 00 00            mov edx, dword ptr [rsp + 0x170]
009AD0FE  0F BA EA 09                     bts edx, 9
009AD102  0F B6 87 FB 05 00 00            movzx eax, byte ptr [rdi + 0x5fb]
009AD109  8B C8                           mov ecx, eax
009AD10B  83 E1 38                        and ecx, 0x38
009AD10E  03 C9                           add ecx, ecx
009AD110  83 E0 07                        and eax, 7
009AD113  0B C8                           or ecx, eax
009AD115  81 E2 00 FF FF FF               and edx, 0xffffff00
009AD11B  0B CA                           or ecx, edx
009AD11D  8B 87 FC 05 00 00               mov eax, dword ptr [rdi + 0x5fc]
009AD123  83 E0 04                        and eax, 4
009AD126  C1 E0 06                        shl eax, 6
009AD129  0F BA F1 08                     btr ecx, 8
009AD12D  0B C1                           or eax, ecx
009AD12F  89 84 24 70 01 00 00            mov dword ptr [rsp + 0x170], eax
009AD136  48 8B 94 24 C0 00 00 00         mov rdx, qword ptr [rsp + 0xc0]
009AD13E  48 8B CF                        mov rcx, rdi
009AD141  E8 0A 68 8B FF                  call 0x140263950
009AD146  48 8D 94 24 D8 02 00 00         lea rdx, [rsp + 0x2d8]
009AD14E  48 8B CF                        mov rcx, rdi
009AD151  E8 06 66 EF FF                  call 0x1408a375c
009AD156  48 8B 8C 24 D8 02 00 00         mov rcx, qword ptr [rsp + 0x2d8]
009AD15E  48 89 8C 24 40 01 00 00         mov qword ptr [rsp + 0x140], rcx
009AD166  48 8B 84 24 E0 02 00 00         mov rax, qword ptr [rsp + 0x2e0]
009AD16E  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
009AD176  48 8B 94 24 E8 02 00 00         mov rdx, qword ptr [rsp + 0x2e8]
009AD17E  48 89 94 24 68 01 00 00         mov qword ptr [rsp + 0x168], rdx
009AD186  4D 85 ED                        test r13, r13
009AD189  75 0F                           jne 0x1409ad19a
009AD18B  48 2B 8F 80 06 00 00            sub rcx, qword ptr [rdi + 0x680]
009AD192  48 89 8C 24 58 01 00 00         mov qword ptr [rsp + 0x158], rcx
009AD19A  4D 85 FF                        test r15, r15
009AD19D  75 12                           jne 0x1409ad1b1
009AD19F  48 2B 87 88 06 00 00            sub rax, qword ptr [rdi + 0x688]
009AD1A6  48 2B C2                        sub rax, rdx
009AD1A9  48 89 84 24 60 01 00 00         mov qword ptr [rsp + 0x160], rax
009AD1B1  B8 38 00 00 00                  mov eax, 0x38
009AD1B6  44 3B F0                        cmp r14d, eax
009AD1B9  44 0F 43 F0                     cmovae r14d, eax
009AD1BD  45 8B C6                        mov r8d, r14d
009AD1C0  48 8D 94 24 40 01 00 00         lea rdx, [rsp + 0x140]
009AD1C8  48 8B CE                        mov rcx, rsi
009AD1CB  E8 70 96 D1 FF                  call 0x1406c6840
009AD1D0  4D 85 E4                        test r12, r12
009AD1D3  74 04                           je 0x1409ad1d9
009AD1D5  45 89 34 24                     mov dword ptr [r12], r14d
009AD1D9  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009AD1DD  EB 0B                           jmp 0x1409ad1ea
009AD1DF  8B D8                           mov ebx, eax
009AD1E1  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AD1E5  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009AD1EA  48 8B CF                        mov rcx, rdi
009AD1ED  BA 50 73 51 79                  mov edx, 0x79517350
009AD1F2  E8 E9 A6 94 FF                  call 0x1402f78e0
009AD1F7  8B C3                           mov eax, ebx
009AD1F9  E9 42 15 00 00                  jmp 0x1409ae740
009AD1FE  45 89 34 24                     mov dword ptr [r12], r14d
009AD202  E9 39 DE FF FF                  jmp 0x1409ab040
009AD207  E9 34 15 00 00                  jmp 0x1409ae740
009AD20C  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009AD210  89 5E 04                        mov dword ptr [rsi + 4], ebx
009AD213  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AD218  F7 80 54 07 00 00 00 40 00 00   test dword ptr [rax + 0x754], 0x4000
009AD222  74 09                           je 0x1409ad22d
009AD224  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AD227  83 C8 01                        or eax, 1
009AD22A  89 46 04                        mov dword ptr [rsi + 4], eax
009AD22D  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AD232  F7 80 54 07 00 00 00 80 00 00   test dword ptr [rax + 0x754], 0x8000
009AD23C  74 09                           je 0x1409ad247
009AD23E  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AD241  83 C8 02                        or eax, 2
009AD244  89 46 04                        mov dword ptr [rsi + 4], eax
009AD247  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AD24C  F7 80 54 07 00 00 00 00 02 00   test dword ptr [rax + 0x754], 0x20000
009AD256  74 09                           je 0x1409ad261
009AD258  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AD25B  83 C8 04                        or eax, 4
009AD25E  89 46 04                        mov dword ptr [rsi + 4], eax
009AD261  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AD266  F7 80 54 07 00 00 00 00 04 00   test dword ptr [rax + 0x754], 0x40000
009AD270  74 09                           je 0x1409ad27b
009AD272  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AD275  83 C8 08                        or eax, 8
009AD278  89 46 04                        mov dword ptr [rsi + 4], eax
009AD27B  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AD280  F7 80 54 07 00 00 00 00 10 00   test dword ptr [rax + 0x754], 0x100000
009AD28A  74 09                           je 0x1409ad295
009AD28C  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AD28F  83 C8 10                        or eax, 0x10
009AD292  89 46 04                        mov dword ptr [rsi + 4], eax
009AD295  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AD29A  F7 80 54 07 00 00 00 00 20 00   test dword ptr [rax + 0x754], 0x200000
009AD2A4  74 09                           je 0x1409ad2af
009AD2A6  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AD2A9  83 C8 20                        or eax, 0x20
009AD2AC  89 46 04                        mov dword ptr [rsi + 4], eax
009AD2AF  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AD2B4  F7 80 54 07 00 00 00 00 40 00   test dword ptr [rax + 0x754], 0x400000
009AD2BE  74 09                           je 0x1409ad2c9
009AD2C0  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AD2C3  83 C8 40                        or eax, 0x40
009AD2C6  89 46 04                        mov dword ptr [rsi + 4], eax
009AD2C9  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AD2CE  F7 80 54 07 00 00 00 00 80 00   test dword ptr [rax + 0x754], 0x800000
009AD2D8  74 0A                           je 0x1409ad2e4
009AD2DA  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AD2DD  0F BA E8 07                     bts eax, 7
009AD2E1  89 46 04                        mov dword ptr [rsi + 4], eax
009AD2E4  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AD2E9  F7 80 54 07 00 00 00 00 00 40   test dword ptr [rax + 0x754], 0x40000000
009AD2F3  74 0A                           je 0x1409ad2ff
009AD2F5  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AD2F8  0F BA E8 08                     bts eax, 8
009AD2FC  89 46 04                        mov dword ptr [rsi + 4], eax
009AD2FF  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AD304  83 B8 54 07 00 00 00            cmp dword ptr [rax + 0x754], 0
009AD30B  7D 0A                           jge 0x1409ad317
009AD30D  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AD310  0F BA E8 09                     bts eax, 9
009AD314  89 46 04                        mov dword ptr [rsi + 4], eax
009AD317  E9 EA D1 FF FF                  jmp 0x1409aa506
009AD31C  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AD320  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
009AD325  E9 DC D1 FF FF                  jmp 0x1409aa506
009AD32A  BF 0A 01 00 C0                  mov edi, 0xc000010a
009AD32F  E9 B5 E3 FF FF                  jmp 0x1409ab6e9
009AD334  4C 8B 05 5D 97 61 00            mov r8, qword ptr [rip + 0x61975d]
009AD33B  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AD340  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AD345  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AD34A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AD34F  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AD357  45 0F B6 CD                     movzx r9d, r13b
009AD35B  BA 00 04 00 00                  mov edx, 0x400
009AD360  49 8B CF                        mov rcx, r15
009AD363  E8 E8 C2 EB FF                  call 0x140869650
009AD368  85 C0                           test eax, eax
009AD36A  0F 88 D0 13 00 00               js 0x1409ae740
009AD370  4C 8B 54 24 40                  mov r10, qword ptr [rsp + 0x40]
009AD375  E9 25 E9 FF FF                  jmp 0x1409abc9f
009AD37A  41 83 FE 08                     cmp r14d, 8
009AD37E  0F 85 1D E2 FF FF               jne 0x1409ab5a1
009AD384  4C 8B 05 0D 97 61 00            mov r8, qword ptr [rip + 0x61970d]
009AD38B  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AD390  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AD395  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AD39A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AD39F  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AD3A7  45 0F B6 CD                     movzx r9d, r13b
009AD3AB  BA 00 04 00 00                  mov edx, 0x400
009AD3B0  49 8B CF                        mov rcx, r15
009AD3B3  E8 98 C2 EB FF                  call 0x140869650
009AD3B8  85 C0                           test eax, eax
009AD3BA  0F 88 80 13 00 00               js 0x1409ae740
009AD3C0  4C 8D 84 24 20 01 00 00         lea r8, [rsp + 0x120]
009AD3C8  41 0F B6 D5                     movzx edx, r13b
009AD3CC  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AD3D1  E8 3E 50 0D 00                  call 0x140a82414
009AD3D6  44 8B F8                        mov r15d, eax
009AD3D9  4C 8B B4 24 20 01 00 00         mov r14, qword ptr [rsp + 0x120]
009AD3E1  85 C0                           test eax, eax
009AD3E3  4C 0F 48 F3                     cmovs r14, rbx
009AD3E7  4C 89 B4 24 20 01 00 00         mov qword ptr [rsp + 0x120], r14
009AD3EF  BA 50 73 51 79                  mov edx, 0x79517350
009AD3F4  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AD3F9  E8 E2 A4 94 FF                  call 0x1402f78e0
009AD3FE  90                              nop
009AD3FF  4C 89 36                        mov qword ptr [rsi], r14
009AD402  4D 85 E4                        test r12, r12
009AD405  74 08                           je 0x1409ad40f
009AD407  41 C7 04 24 08 00 00 00         mov dword ptr [r12], 8
009AD40F  E9 8D E6 FF FF                  jmp 0x1409abaa1
009AD414  8B D8                           mov ebx, eax
009AD416  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
009AD41E  48 85 C9                        test rcx, rcx
009AD421  74 0A                           je 0x1409ad42d
009AD423  0F B6 54 24 4C                  movzx edx, byte ptr [rsp + 0x4c]
009AD428  E8 43 44 EF FF                  call 0x1408a1870
009AD42D  8B C3                           mov eax, ebx
009AD42F  E9 0C 13 00 00                  jmp 0x1409ae740
009AD434  8B 7E 28                        mov edi, dword ptr [rsi + 0x28]
009AD437  89 BC 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], edi
009AD43E  EB 05                           jmp 0x1409ad445
009AD440  E9 FB 12 00 00                  jmp 0x1409ae740
009AD445  F7 C7 FE FF FF FF               test edi, 0xfffffffe
009AD44B  0F 84 B9 E0 FF FF               je 0x1409ab50a
009AD451  B8 0D 00 00 C0                  mov eax, 0xc000000d
009AD456  E9 E5 12 00 00                  jmp 0x1409ae740
009AD45B  49 83 FF FF                     cmp r15, -1
009AD45F  0F 84 A5 10 00 00               je 0x1409ae50a
009AD465  B8 0D 00 00 C0                  mov eax, 0xc000000d
009AD46A  E9 D1 12 00 00                  jmp 0x1409ae740
009AD46F  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
009AD475  E9 82 EE FF FF                  jmp 0x1409ac2fc
009AD47A  41 BF 0A 01 00 C0               mov r15d, 0xc000010a
009AD480  E9 A2 E1 FF FF                  jmp 0x1409ab627
009AD485  41 83 FE 04                     cmp r14d, 4
009AD489  0F 85 12 E1 FF FF               jne 0x1409ab5a1
009AD48F  4C 8B 05 02 96 61 00            mov r8, qword ptr [rip + 0x619602]
009AD496  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AD49B  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AD4A0  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AD4A5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AD4AA  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AD4B2  45 0F B6 CD                     movzx r9d, r13b
009AD4B6  BA 00 04 00 00                  mov edx, 0x400
009AD4BB  49 8B CF                        mov rcx, r15
009AD4BE  E8 8D C1 EB FF                  call 0x140869650
009AD4C3  8B D8                           mov ebx, eax
009AD4C5  85 C0                           test eax, eax
009AD4C7  0F 88 73 12 00 00               js 0x1409ae740
009AD4CD  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AD4D2  8B 81 F4 01 00 00               mov eax, dword ptr [rcx + 0x1f4]
009AD4D8  D1 E8                           shr eax, 1
009AD4DA  F7 D0                           not eax
009AD4DC  83 E0 01                        and eax, 1
009AD4DF  89 06                           mov dword ptr [rsi], eax
009AD4E1  4D 85 E4                        test r12, r12
009AD4E4  74 04                           je 0x1409ad4ea
009AD4E6  45 89 34 24                     mov dword ptr [r12], r14d
009AD4EA  E9 BF EF FF FF                  jmp 0x1409ac4ae
009AD4EF  8B D8                           mov ebx, eax
009AD4F1  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AD4F6  E9 B3 EF FF FF                  jmp 0x1409ac4ae
009AD4FB  4D 85 E4                        test r12, r12
009AD4FE  0F 84 9D E0 FF FF               je 0x1409ab5a1
009AD504  41 C7 04 24 10 00 00 00         mov dword ptr [r12], 0x10
009AD50C  E9 90 E0 FF FF                  jmp 0x1409ab5a1
009AD511  E9 2A 12 00 00                  jmp 0x1409ae740
009AD516  41 83 FE 04                     cmp r14d, 4
009AD51A  0F 85 81 E0 FF FF               jne 0x1409ab5a1
009AD520  4C 8B 05 71 95 61 00            mov r8, qword ptr [rip + 0x619571]
009AD527  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AD52C  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AD531  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AD536  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AD53B  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AD543  45 0F B6 CD                     movzx r9d, r13b
009AD547  BA 00 10 00 00                  mov edx, 0x1000
009AD54C  49 8B CF                        mov rcx, r15
009AD54F  E8 FC C0 EB FF                  call 0x140869650
009AD554  8B F8                           mov edi, eax
009AD556  85 C0                           test eax, eax
009AD558  0F 88 E2 DA FF FF               js 0x1409ab040
009AD55E  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AD563  8B 99 88 00 00 00               mov ebx, dword ptr [rcx + 0x88]
009AD569  D1 EB                           shr ebx, 1
009AD56B  83 E3 01                        and ebx, 1
009AD56E  BA 50 73 51 79                  mov edx, 0x79517350
009AD573  E8 68 A3 94 FF                  call 0x1402f78e0
009AD578  90                              nop
009AD579  89 1E                           mov dword ptr [rsi], ebx
009AD57B  4D 85 E4                        test r12, r12
009AD57E  74 04                           je 0x1409ad584
009AD580  45 89 34 24                     mov dword ptr [r12], r14d
009AD584  E9 B7 DA FF FF                  jmp 0x1409ab040
009AD589  E9 B2 11 00 00                  jmp 0x1409ae740
009AD58E  45 32 C9                        xor r9b, r9b
009AD591  44 88 4C 24 4C                  mov byte ptr [rsp + 0x4c], r9b
009AD596  8B 48 08                        mov ecx, dword ptr [rax + 8]
009AD599  F6 C1 03                        test cl, 3
009AD59C  74 11                           je 0x1409ad5af
009AD59E  48 8D 48 10                     lea rcx, [rax + 0x10]
009AD5A2  E8 F9 0F 86 FF                  call 0x14020e5a0
009AD5A7  41 B1 01                        mov r9b, 1
009AD5AA  44 88 4C 24 4C                  mov byte ptr [rsp + 0x4c], r9b
009AD5AF  89 5E 08                        mov dword ptr [rsi + 8], ebx
009AD5B2  33 D2                           xor edx, edx
009AD5B4  41 8B 46 48                     mov eax, dword ptr [r14 + 0x48]
009AD5B8  41 F7 76 04                     div dword ptr [r14 + 4]
009AD5BC  89 94 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], edx
009AD5C3  44 8B D3                        mov r10d, ebx
009AD5C6  89 9C 24 D0 01 00 00            mov dword ptr [rsp + 0x1d0], ebx
009AD5CD  BF 04 00 00 C0                  mov edi, 0xc0000004
009AD5D2  45 3B 56 04                     cmp r10d, dword ptr [r14 + 4]
009AD5D6  0F 83 53 01 00 00               jae 0x1409ad72f
009AD5DC  48 8D 04 92                     lea rax, [rdx + rdx*4]
009AD5E0  48 C1 E0 05                     shl rax, 5
009AD5E4  49 03 C6                        add rax, r14
009AD5E7  48 8D 8C 24 90 03 00 00         lea rcx, [rsp + 0x390]
009AD5EF  0F 10 40 50                     movups xmm0, xmmword ptr [rax + 0x50]
009AD5F3  0F 11 01                        movups xmmword ptr [rcx], xmm0
009AD5F6  0F 10 48 60                     movups xmm1, xmmword ptr [rax + 0x60]
009AD5FA  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
009AD5FE  0F 10 40 70                     movups xmm0, xmmword ptr [rax + 0x70]
009AD602  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
009AD606  0F 10 88 80 00 00 00            movups xmm1, xmmword ptr [rax + 0x80]
009AD60D  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
009AD611  0F 10 80 90 00 00 00            movups xmm0, xmmword ptr [rax + 0x90]
009AD618  0F 11 41 40                     movups xmmword ptr [rcx + 0x40], xmm0
009AD61C  0F 10 88 A0 00 00 00            movups xmm1, xmmword ptr [rax + 0xa0]
009AD623  0F 11 49 50                     movups xmmword ptr [rcx + 0x50], xmm1
009AD627  0F 10 80 B0 00 00 00            movups xmm0, xmmword ptr [rax + 0xb0]
009AD62E  0F 11 41 60                     movups xmmword ptr [rcx + 0x60], xmm0
009AD632  0F 10 88 C0 00 00 00            movups xmm1, xmmword ptr [rax + 0xc0]
009AD639  0F 11 49 70                     movups xmmword ptr [rcx + 0x70], xmm1
009AD63D  0F 10 80 D0 00 00 00            movups xmm0, xmmword ptr [rax + 0xd0]
009AD644  0F 11 81 80 00 00 00            movups xmmword ptr [rcx + 0x80], xmm0
009AD64B  0F 10 88 E0 00 00 00            movups xmm1, xmmword ptr [rax + 0xe0]
009AD652  0F 11 89 90 00 00 00            movups xmmword ptr [rcx + 0x90], xmm1
009AD659  48 8B 06                        mov rax, qword ptr [rsi]
009AD65C  4C 8B 9C 24 A0 03 00 00         mov r11, qword ptr [rsp + 0x3a0]
009AD664  49 3B C3                        cmp rax, r11
009AD667  74 05                           je 0x1409ad66e
009AD669  48 85 C0                        test rax, rax
009AD66C  75 78                           jne 0x1409ad6e6
009AD66E  44 8B 84 24 A8 03 00 00         mov r8d, dword ptr [rsp + 0x3a8]
009AD676  45 85 C0                        test r8d, r8d
009AD679  74 6B                           je 0x1409ad6e6
009AD67B  8B 46 08                        mov eax, dword ptr [rsi + 8]
009AD67E  FF C0                           inc eax
009AD680  89 46 08                        mov dword ptr [rsi + 8], eax
009AD683  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
009AD68B  85 C0                           test eax, eax
009AD68D  0F 84 93 00 00 00               je 0x1409ad726
009AD693  FF C8                           dec eax
009AD695  48 89 84 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rax
009AD69D  89 84 24 88 02 00 00            mov dword ptr [rsp + 0x288], eax
009AD6A4  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
009AD6AC  4C 89 19                        mov qword ptr [rcx], r11
009AD6AF  0F 28 84 24 90 03 00 00         movaps xmm0, xmmword ptr [rsp + 0x390]
009AD6B7  0F 11 41 08                     movups xmmword ptr [rcx + 8], xmm0
009AD6BB  44 89 41 18                     mov dword ptr [rcx + 0x18], r8d
009AD6BF  44 8B C3                        mov r8d, ebx
009AD6C2  89 9C 24 BC 01 00 00            mov dword ptr [rsp + 0x1bc], ebx
009AD6C9  41 83 F8 10                     cmp r8d, 0x10
009AD6CD  72 38                           jb 0x1409ad707
009AD6CF  48 81 C1 A0 00 00 00            add rcx, 0xa0
009AD6D6  48 89 8C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rcx
009AD6DE  48 89 8C 24 F8 02 00 00         mov qword ptr [rsp + 0x2f8], rcx
009AD6E6  85 D2                           test edx, edx
009AD6E8  75 04                           jne 0x1409ad6ee
009AD6EA  41 8B 56 04                     mov edx, dword ptr [r14 + 4]
009AD6EE  FF CA                           dec edx
009AD6F0  89 94 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], edx
009AD6F7  41 FF C2                        inc r10d
009AD6FA  44 89 94 24 D0 01 00 00         mov dword ptr [rsp + 0x1d0], r10d
009AD702  E9 CB FE FF FF                  jmp 0x1409ad5d2
009AD707  83 7C 24 58 00                  cmp dword ptr [rsp + 0x58], 0
009AD70C  74 36                           je 0x1409ad744
009AD70E  4C 8B DB                        mov r11, rbx
009AD711  41 8B C0                        mov eax, r8d
009AD714  4C 89 5C C1 20                  mov qword ptr [rcx + rax*8 + 0x20], r11
009AD719  41 FF C0                        inc r8d
009AD71C  44 89 84 24 BC 01 00 00         mov dword ptr [rsp + 0x1bc], r8d
009AD724  EB A3                           jmp 0x1409ad6c9
009AD726  44 8B FF                        mov r15d, edi
009AD729  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
009AD72D  EB B7                           jmp 0x1409ad6e6
009AD72F  4D 85 E4                        test r12, r12
009AD732  74 1D                           je 0x1409ad751
009AD734  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
009AD73C  2B C6                           sub eax, esi
009AD73E  41 89 04 24                     mov dword ptr [r12], eax
009AD742  EB 0D                           jmp 0x1409ad751
009AD744  41 8B C0                        mov eax, r8d
009AD747  4C 8B 9C C4 B0 03 00 00         mov r11, qword ptr [rsp + rax*8 + 0x3b0]
009AD74F  EB C0                           jmp 0x1409ad711
009AD751  EB 1D                           jmp 0x1409ad770
009AD753  44 8B F8                        mov r15d, eax
009AD756  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AD75A  4C 8B AC 24 C8 01 00 00         mov r13, qword ptr [rsp + 0x1c8]
009AD762  4C 8B B4 24 C0 01 00 00         mov r14, qword ptr [rsp + 0x1c0]
009AD76A  44 0F B6 4C 24 4C               movzx r9d, byte ptr [rsp + 0x4c]
009AD770  45 84 C9                        test r9b, r9b
009AD773  74 09                           je 0x1409ad77e
009AD775  49 8D 4E 10                     lea rcx, [r14 + 0x10]
009AD779  E8 42 42 8A FF                  call 0x1402519c0
009AD77E  49 8B D6                        mov rdx, r14
009AD781  49 8B CD                        mov rcx, r13
009AD784  E8 A7 9C 06 00                  call 0x140a17430
009AD789  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009AD78E  48 8D 8F E8 01 00 00            lea rcx, [rdi + 0x1e8]
009AD795  E8 E6 C6 99 FF                  call 0x140349e80
009AD79A  E9 F5 E2 FF FF                  jmp 0x1409aba94
009AD79F  41 BF 0A 01 00 C0               mov r15d, 0xc000010a
009AD7A5  48 8B CF                        mov rcx, rdi
009AD7A8  E8 63 18 8B FF                  call 0x14025f010
009AD7AD  48 8B CB                        mov rcx, rbx
009AD7B0  E8 9B BB 94 FF                  call 0x1402f9350
009AD7B5  41 8B C7                        mov eax, r15d
009AD7B8  E9 83 0F 00 00                  jmp 0x1409ae740
009AD7BD  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
009AD7C2  41 83 FE 08                     cmp r14d, 8
009AD7C6  0F 85 D5 DD FF FF               jne 0x1409ab5a1
009AD7CC  48 8B 3E                        mov rdi, qword ptr [rsi]
009AD7CF  48 89 BC 24 00 03 00 00         mov qword ptr [rsp + 0x300], rdi
009AD7D7  EB 05                           jmp 0x1409ad7de
009AD7D9  E9 62 0F 00 00                  jmp 0x1409ae740
009AD7DE  4C 8B 05 B3 92 61 00            mov r8, qword ptr [rip + 0x6192b3]
009AD7E5  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AD7EA  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AD7EF  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AD7F4  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AD7F9  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AD801  45 0F B6 CD                     movzx r9d, r13b
009AD805  BA 00 04 00 00                  mov edx, 0x400
009AD80A  49 8B CF                        mov rcx, r15
009AD80D  E8 3E BE EB FF                  call 0x140869650
009AD812  85 C0                           test eax, eax
009AD814  0F 88 26 0F 00 00               js 0x1409ae740
009AD81A  4C 8B 05 BF 92 61 00            mov r8, qword ptr [rip + 0x6192bf]
009AD821  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AD826  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AD82B  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
009AD833  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AD838  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AD840  45 0F B6 CD                     movzx r9d, r13b
009AD844  BA 20 00 10 00                  mov edx, 0x100020
009AD849  48 8B CF                        mov rcx, rdi
009AD84C  E8 FF BD EB FF                  call 0x140869650
009AD851  8B F8                           mov edi, eax
009AD853  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AD858  85 C0                           test eax, eax
009AD85A  0F 88 D6 D7 FF FF               js 0x1409ab036
009AD860  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
009AD865  E8 06 90 F2 FF                  call 0x1408d6870
009AD86A  8B F0                           mov esi, eax
009AD86C  BA 50 73 51 79                  mov edx, 0x79517350
009AD871  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AD876  E8 65 A0 94 FF                  call 0x1402f78e0
009AD87B  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
009AD883  85 F6                           test esi, esi
009AD885  0F 88 63 0C 00 00               js 0x1409ae4ee
009AD88B  4C 8B 71 28                     mov r14, qword ptr [rcx + 0x28]
009AD88F  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
009AD894  48 8B 77 28                     mov rsi, qword ptr [rdi + 0x28]
009AD898  44 8B FB                        mov r15d, ebx
009AD89B  B8 01 00 00 C0                  mov eax, 0xc0000001
009AD8A0  4C 3B F6                        cmp r14, rsi
009AD8A3  44 0F 45 F8                     cmovne r15d, eax
009AD8A7  E8 A4 BA 94 FF                  call 0x1402f9350
009AD8AC  48 8B CF                        mov rcx, rdi
009AD8AF  E8 9C BA 94 FF                  call 0x1402f9350
009AD8B4  41 8B C7                        mov eax, r15d
009AD8B7  4C 3B F6                        cmp r14, rsi
009AD8BA  0F 85 80 0E 00 00               jne 0x1409ae740
009AD8C0  4D 85 E4                        test r12, r12
009AD8C3  0F 84 77 0E 00 00               je 0x1409ae740
009AD8C9  41 89 1C 24                     mov dword ptr [r12], ebx
009AD8CD  E9 6E 0E 00 00                  jmp 0x1409ae740
009AD8D2  E9 69 0E 00 00                  jmp 0x1409ae740
009AD8D7  41 83 FE 04                     cmp r14d, 4
009AD8DB  0F 85 C0 DC FF FF               jne 0x1409ab5a1
009AD8E1  4C 8B 05 B0 91 61 00            mov r8, qword ptr [rip + 0x6191b0]
009AD8E8  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AD8ED  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AD8F2  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AD8F7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AD8FC  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AD904  45 0F B6 CD                     movzx r9d, r13b
009AD908  BA 00 10 00 00                  mov edx, 0x1000
009AD90D  49 8B CF                        mov rcx, r15
009AD910  E8 3B BD EB FF                  call 0x140869650
009AD915  85 C0                           test eax, eax
009AD917  0F 88 23 0E 00 00               js 0x1409ae740
009AD91D  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AD922  8B 88 F0 01 00 00               mov ecx, dword ptr [rax + 0x1f0]
009AD928  89 8C 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], ecx
009AD92F  BA 50 73 51 79                  mov edx, 0x79517350
009AD934  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AD939  E8 A2 9F 94 FF                  call 0x1402f78e0
009AD93E  F7 84 24 B8 00 00 00 00 00 08 00  test dword ptr [rsp + 0xb8], 0x80000
009AD949  41 BD 01 00 00 00               mov r13d, 1
009AD94F  41 0F 45 DD                     cmovne ebx, r13d
009AD953  F7 84 24 B8 00 00 00 00 00 04 00  test dword ptr [rsp + 0xb8], 0x40000
009AD95E  74 03                           je 0x1409ad963
009AD960  83 CB 02                        or ebx, 2
009AD963  89 1E                           mov dword ptr [rsi], ebx
009AD965  4D 85 E4                        test r12, r12
009AD968  74 08                           je 0x1409ad972
009AD96A  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
009AD972  E9 7E D5 FF FF                  jmp 0x1409aaef5
009AD977  E9 C4 0D 00 00                  jmp 0x1409ae740
009AD97C  48 C7 84 24 C0 04 00 00 01 00 20 00  mov qword ptr [rsp + 0x4c0], 0x200001
009AD988  33 D2                           xor edx, edx
009AD98A  41 B8 00 01 00 00               mov r8d, 0x100
009AD990  48 8D 8C 24 C8 04 00 00         lea rcx, [rsp + 0x4c8]
009AD998  E8 A3 92 D1 FF                  call 0x1406c6c40
009AD99D  48 8D 44 24 60                  lea rax, [rsp + 0x60]
009AD9A2  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009AD9A7  45 33 C9                        xor r9d, r9d
009AD9AA  4C 8D 84 24 30 04 00 00         lea r8, [rsp + 0x430]
009AD9B2  48 8D 94 24 C0 04 00 00         lea rdx, [rsp + 0x4c0]
009AD9BA  48 8B CF                        mov rcx, rdi
009AD9BD  E8 4E 0D 92 FF                  call 0x1402ce710
009AD9C2  0F B7 4C 24 60                  movzx ecx, word ptr [rsp + 0x60]
009AD9C7  48 8B 94 CC C8 04 00 00         mov rdx, qword ptr [rsp + rcx*8 + 0x4c8]
009AD9CF  41 83 FE 10                     cmp r14d, 0x10
009AD9D3  75 04                           jne 0x1409ad9d9
009AD9D5  66 89 4E 08                     mov word ptr [rsi + 8], cx
009AD9D9  48 89 16                        mov qword ptr [rsi], rdx
009AD9DC  4D 85 E4                        test r12, r12
009AD9DF  74 04                           je 0x1409ad9e5
009AD9E1  45 89 34 24                     mov dword ptr [r12], r14d
009AD9E5  E9 AA E0 FF FF                  jmp 0x1409aba94
009AD9EA  44 8B F8                        mov r15d, eax
009AD9ED  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009AD9F2  E9 9D E0 FF FF                  jmp 0x1409aba94
009AD9F7  4D 85 E4                        test r12, r12
009AD9FA  0F 84 65 FA FF FF               je 0x1409ad465
009ADA00  41 F6 C6 01                     test r14b, 1
009ADA04  0F 85 5B FA FF FF               jne 0x1409ad465
009ADA0A  4C 8B 05 87 90 61 00            mov r8, qword ptr [rip + 0x619087]
009ADA11  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ADA16  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ADA1B  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ADA20  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ADA25  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ADA2D  45 0F B6 CD                     movzx r9d, r13b
009ADA31  BA 00 10 00 00                  mov edx, 0x1000
009ADA36  49 8B CF                        mov rcx, r15
009ADA39  E8 12 BC EB FF                  call 0x140869650
009ADA3E  85 C0                           test eax, eax
009ADA40  0F 88 FA 0C 00 00               js 0x1409ae740
009ADA46  4C 8B 7C 24 40                  mov r15, qword ptr [rsp + 0x40]
009ADA4B  49 8B D7                        mov rdx, r15
009ADA4E  48 8D 8C 24 00 01 00 00         lea rcx, [rsp + 0x100]
009ADA56  E8 A9 0D AE FF                  call 0x14048e804
009ADA5B  0F 10 08                        movups xmm1, xmmword ptr [rax]
009ADA5E  0F 11 8C 24 30 04 00 00         movups xmmword ptr [rsp + 0x430], xmm1
009ADA66  48 8D 8C 24 30 04 00 00         lea rcx, [rsp + 0x430]
009ADA6E  E8 71 91 8A FF                  call 0x140256be4
009ADA73  0F B7 D0                        movzx edx, ax
009ADA76  89 94 24 B4 01 00 00            mov dword ptr [rsp + 0x1b4], edx
009ADA7D  8D 7B 02                        lea edi, [rbx + 2]
009ADA80  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
009ADA84  41 3B FE                        cmp edi, r14d
009ADA87  77 0F                           ja 0x1409ada98
009ADA89  66 89 16                        mov word ptr [rsi], dx
009ADA8C  48 83 C6 02                     add rsi, 2
009ADA90  48 89 B4 24 18 03 00 00         mov qword ptr [rsp + 0x318], rsi
009ADA98  48 8D 8C 24 30 04 00 00         lea rcx, [rsp + 0x430]
009ADAA0  E8 F3 9D AB FF                  call 0x140467898
009ADAA5  8B DF                           mov ebx, edi
009ADAA7  48 8D 8C 24 30 04 00 00         lea rcx, [rsp + 0x430]
009ADAAF  E8 FC 78 8A FF                  call 0x1402553b0
009ADAB4  85 C0                           test eax, eax
009ADAB6  74 AE                           je 0x1409ada66
009ADAB8  41 89 3C 24                     mov dword ptr [r12], edi
009ADABC  44 3B F7                        cmp r14d, edi
009ADABF  1B DB                           sbb ebx, ebx
009ADAC1  81 E3 23 00 00 C0               and ebx, 0xc0000023
009ADAC7  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009ADACB  EB 0B                           jmp 0x1409adad8
009ADACD  8B D8                           mov ebx, eax
009ADACF  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009ADAD3  4C 8B 7C 24 40                  mov r15, qword ptr [rsp + 0x40]
009ADAD8  BA 50 73 51 79                  mov edx, 0x79517350
009ADADD  49 8B CF                        mov rcx, r15
009ADAE0  E8 FB 9D 94 FF                  call 0x1402f78e0
009ADAE5  8B C3                           mov eax, ebx
009ADAE7  E9 54 0C 00 00                  jmp 0x1409ae740
009ADAEC  41 83 FE 04                     cmp r14d, 4
009ADAF0  0F 85 AB DA FF FF               jne 0x1409ab5a1
009ADAF6  4C 8B 05 9B 8F 61 00            mov r8, qword ptr [rip + 0x618f9b]
009ADAFD  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ADB02  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ADB07  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ADB0C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ADB11  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ADB19  45 0F B6 CD                     movzx r9d, r13b
009ADB1D  BA 00 10 00 00                  mov edx, 0x1000
009ADB22  49 8B CF                        mov rcx, r15
009ADB25  E8 26 BB EB FF                  call 0x140869650
009ADB2A  85 C0                           test eax, eax
009ADB2C  0F 88 0E 0C 00 00               js 0x1409ae740
009ADB32  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009ADB37  8B 88 F4 01 00 00               mov ecx, dword ptr [rax + 0x1f4]
009ADB3D  89 8C 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], ecx
009ADB44  BA 50 73 51 79                  mov edx, 0x79517350
009ADB49  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ADB4E  E8 8D 9D 94 FF                  call 0x1402f78e0
009ADB53  F7 84 24 B8 00 00 00 00 00 20 00  test dword ptr [rsp + 0xb8], 0x200000
009ADB5E  41 BD 01 00 00 00               mov r13d, 1
009ADB64  41 0F 45 DD                     cmovne ebx, r13d
009ADB68  89 1E                           mov dword ptr [rsi], ebx
009ADB6A  4D 85 E4                        test r12, r12
009ADB6D  74 04                           je 0x1409adb73
009ADB6F  45 89 34 24                     mov dword ptr [r12], r14d
009ADB73  E9 7D D3 FF FF                  jmp 0x1409aaef5
009ADB78  E9 C3 0B 00 00                  jmp 0x1409ae740
009ADB7D  B8 01 00 00 C0                  mov eax, 0xc0000001
009ADB82  E9 B9 0B 00 00                  jmp 0x1409ae740
009ADB87  BF 0D 00 00 C0                  mov edi, 0xc000000d
009ADB8C  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ADB91  E9 FE D5 FF FF                  jmp 0x1409ab194
009ADB96  41 83 FE 04                     cmp r14d, 4
009ADB9A  0F 85 01 DA FF FF               jne 0x1409ab5a1
009ADBA0  4C 8B 05 F1 8E 61 00            mov r8, qword ptr [rip + 0x618ef1]
009ADBA7  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ADBAC  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ADBB1  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ADBB6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ADBBB  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ADBC3  45 0F B6 CD                     movzx r9d, r13b
009ADBC7  BA 00 04 00 00                  mov edx, 0x400
009ADBCC  49 8B CF                        mov rcx, r15
009ADBCF  E8 7C BA EB FF                  call 0x140869650
009ADBD4  8B D8                           mov ebx, eax
009ADBD6  85 C0                           test eax, eax
009ADBD8  0F 88 62 0B 00 00               js 0x1409ae740
009ADBDE  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ADBE3  8B 81 88 00 00 00               mov eax, dword ptr [rcx + 0x88]
009ADBE9  C1 E8 05                        shr eax, 5
009ADBEC  83 E0 01                        and eax, 1
009ADBEF  89 06                           mov dword ptr [rsi], eax
009ADBF1  E9 B8 E8 FF FF                  jmp 0x1409ac4ae
009ADBF6  8B D8                           mov ebx, eax
009ADBF8  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ADBFD  E9 AC E8 FF FF                  jmp 0x1409ac4ae
009ADC02  41 83 FE 04                     cmp r14d, 4
009ADC06  0F 83 08 EB FF FF               jae 0x1409ac714
009ADC0C  E9 90 D9 FF FF                  jmp 0x1409ab5a1
009ADC11  8B 84 24 DC 00 00 00            mov eax, dword ptr [rsp + 0xdc]
009ADC18  8D 04 85 00 00 00 00            lea eax, [rax*4]
009ADC1F  41 89 04 24                     mov dword ptr [r12], eax
009ADC23  E9 C7 E9 FF FF                  jmp 0x1409ac5ef
009ADC28  8B D8                           mov ebx, eax
009ADC2A  E9 C0 E9 FF FF                  jmp 0x1409ac5ef
009ADC2F  BB 0A 01 00 C0                  mov ebx, 0xc000010a
009ADC34  E9 A0 E9 FF FF                  jmp 0x1409ac5d9
009ADC39  41 83 FE 10                     cmp r14d, 0x10
009ADC3D  0F 85 5E D9 FF FF               jne 0x1409ab5a1
009ADC43  4C 8B 05 4E 8E 61 00            mov r8, qword ptr [rip + 0x618e4e]
009ADC4A  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ADC4F  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ADC54  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ADC59  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ADC5E  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ADC66  45 0F B6 CD                     movzx r9d, r13b
009ADC6A  BA 00 10 00 00                  mov edx, 0x1000
009ADC6F  49 8B CF                        mov rcx, r15
009ADC72  E8 D9 B9 EB FF                  call 0x140869650
009ADC77  8B D8                           mov ebx, eax
009ADC79  85 C0                           test eax, eax
009ADC7B  0F 88 BF 0A 00 00               js 0x1409ae740
009ADC81  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ADC86  48 8B 91 F0 07 00 00            mov rdx, qword ptr [rcx + 0x7f0]
009ADC8D  48 8B 02                        mov rax, qword ptr [rdx]
009ADC90  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
009ADC98  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
009ADC9C  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
009ADCA4  BA 50 73 51 79                  mov edx, 0x79517350
009ADCA9  E8 32 9C 94 FF                  call 0x1402f78e0
009ADCAE  90                              nop
009ADCAF  0F 28 84 24 40 01 00 00         movaps xmm0, xmmword ptr [rsp + 0x140]
009ADCB7  0F 11 06                        movups xmmword ptr [rsi], xmm0
009ADCBA  4D 85 E4                        test r12, r12
009ADCBD  74 04                           je 0x1409adcc3
009ADCBF  45 89 34 24                     mov dword ptr [r12], r14d
009ADCC3  E9 6E E0 FF FF                  jmp 0x1409abd36
009ADCC8  8B D8                           mov ebx, eax
009ADCCA  E9 67 E0 FF FF                  jmp 0x1409abd36
009ADCCF  33 D2                           xor edx, edx
009ADCD1  41 B8 90 00 00 00               mov r8d, 0x90
009ADCD7  48 8D 8C 24 70 06 00 00         lea rcx, [rsp + 0x670]
009ADCDF  E8 5C 8F D1 FF                  call 0x1406c6c40
009ADCE4  41 83 FE 08                     cmp r14d, 8
009ADCE8  0F 82 B3 D8 FF FF               jb 0x1409ab5a1
009ADCEE  4C 8B 05 A3 8D 61 00            mov r8, qword ptr [rip + 0x618da3]
009ADCF5  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ADCFA  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ADCFF  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ADD04  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ADD09  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ADD11  45 0F B6 CD                     movzx r9d, r13b
009ADD15  BA 00 10 00 00                  mov edx, 0x1000
009ADD1A  49 8B CF                        mov rcx, r15
009ADD1D  E8 2E B9 EB FF                  call 0x140869650
009ADD22  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009ADD26  85 C0                           test eax, eax
009ADD28  0F 88 12 0A 00 00               js 0x1409ae740
009ADD2E  48 8D 94 24 70 06 00 00         lea rdx, [rsp + 0x670]
009ADD36  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009ADD3B  48 8B CF                        mov rcx, rdi
009ADD3E  E8 8D EB 0F 00                  call 0x140aac8d0
009ADD43  90                              nop
009ADD44  B8 90 00 00 00                  mov eax, 0x90
009ADD49  44 3B F0                        cmp r14d, eax
009ADD4C  44 0F 43 F0                     cmovae r14d, eax
009ADD50  45 8B C6                        mov r8d, r14d
009ADD53  48 8D 94 24 70 06 00 00         lea rdx, [rsp + 0x670]
009ADD5B  48 8B CE                        mov rcx, rsi
009ADD5E  E8 DD 8A D1 FF                  call 0x1406c6840
009ADD63  4D 85 E4                        test r12, r12
009ADD66  74 04                           je 0x1409add6c
009ADD68  45 89 34 24                     mov dword ptr [r12], r14d
009ADD6C  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009ADD70  E9 09 E9 FF FF                  jmp 0x1409ac67e
009ADD75  8B D8                           mov ebx, eax
009ADD77  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009ADD7B  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009ADD80  E9 F9 E8 FF FF                  jmp 0x1409ac67e
009ADD85  33 D2                           xor edx, edx
009ADD87  41 B8 B8 01 00 00               mov r8d, 0x1b8
009ADD8D  48 8D 8C 24 00 07 00 00         lea rcx, [rsp + 0x700]
009ADD95  E8 A6 8E D1 FF                  call 0x1406c6c40
009ADD9A  4C 8B 05 F7 8C 61 00            mov r8, qword ptr [rip + 0x618cf7]
009ADDA1  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ADDA6  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ADDAB  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ADDB0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ADDB5  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ADDBD  45 0F B6 CD                     movzx r9d, r13b
009ADDC1  BA 00 10 00 00                  mov edx, 0x1000
009ADDC6  49 8B CF                        mov rcx, r15
009ADDC9  E8 82 B8 EB FF                  call 0x140869650
009ADDCE  8B D8                           mov ebx, eax
009ADDD0  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009ADDD4  85 C0                           test eax, eax
009ADDD6  0F 88 64 09 00 00               js 0x1409ae740
009ADDDC  48 8D 94 24 00 07 00 00         lea rdx, [rsp + 0x700]
009ADDE4  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009ADDE9  48 8B CF                        mov rcx, rdi
009ADDEC  E8 EF C6 F6 FF                  call 0x14091a4e0
009ADDF1  90                              nop
009ADDF2  41 B8 B0 01 00 00               mov r8d, 0x1b0
009ADDF8  45 3B F0                        cmp r14d, r8d
009ADDFB  45 0F 46 C6                     cmovbe r8d, r14d
009ADDFF  48 8D 94 24 00 07 00 00         lea rdx, [rsp + 0x700]
009ADE07  48 8B CE                        mov rcx, rsi
009ADE0A  E8 31 8A D1 FF                  call 0x1406c6840
009ADE0F  4D 85 E4                        test r12, r12
009ADE12  74 08                           je 0x1409ade1c
009ADE14  41 C7 04 24 B0 01 00 00         mov dword ptr [r12], 0x1b0
009ADE1C  E9 5D E8 FF FF                  jmp 0x1409ac67e
009ADE21  8B D8                           mov ebx, eax
009ADE23  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009ADE28  E9 51 E8 FF FF                  jmp 0x1409ac67e
009ADE2D  41 83 FE 04                     cmp r14d, 4
009ADE31  0F 85 6A D7 FF FF               jne 0x1409ab5a1
009ADE37  4C 8B 05 5A 8C 61 00            mov r8, qword ptr [rip + 0x618c5a]
009ADE3E  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ADE43  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ADE48  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ADE4D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ADE52  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ADE5A  45 0F B6 CD                     movzx r9d, r13b
009ADE5E  BA 00 10 00 00                  mov edx, 0x1000
009ADE63  49 8B CF                        mov rcx, r15
009ADE66  E8 E5 B7 EB FF                  call 0x140869650
009ADE6B  85 C0                           test eax, eax
009ADE6D  0F 88 CD 08 00 00               js 0x1409ae740
009ADE73  E8 68 84 A8 FF                  call 0x1404362e0
009ADE78  84 C0                           test al, al
009ADE7A  0F 85 62 06 00 00               jne 0x1409ae4e2
009ADE80  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ADE85  48 8B 89 A0 02 00 00            mov rcx, qword ptr [rcx + 0x2a0]
009ADE8C  E8 5F 79 87 FF                  call 0x1402257f0
009ADE91  48 8B C8                        mov rcx, rax
009ADE94  E8 E7 15 0D 00                  call 0x140a7f480
009ADE99  8B D8                           mov ebx, eax
009ADE9B  BA 50 73 51 79                  mov edx, 0x79517350
009ADEA0  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ADEA5  E8 36 9A 94 FF                  call 0x1402f78e0
009ADEAA  90                              nop
009ADEAB  89 1E                           mov dword ptr [rsi], ebx
009ADEAD  4D 85 E4                        test r12, r12
009ADEB0  74 08                           je 0x1409adeba
009ADEB2  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
009ADEBA  E9 36 D0 FF FF                  jmp 0x1409aaef5
009ADEBF  E9 7C 08 00 00                  jmp 0x1409ae740
009ADEC4  BB AE 01 00 C0                  mov ebx, 0xc00001ae
009ADEC9  E9 59 DE FF FF                  jmp 0x1409abd27
009ADECE  41 83 FE 04                     cmp r14d, 4
009ADED2  0F 85 C9 D6 FF FF               jne 0x1409ab5a1
009ADED8  4C 8B 05 B9 8B 61 00            mov r8, qword ptr [rip + 0x618bb9]
009ADEDF  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ADEE4  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ADEE9  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ADEEE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ADEF3  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ADEFB  45 0F B6 CD                     movzx r9d, r13b
009ADEFF  BA 00 04 00 00                  mov edx, 0x400
009ADF04  49 8B CF                        mov rcx, r15
009ADF07  E8 44 B7 EB FF                  call 0x140869650
009ADF0C  44 8B F8                        mov r15d, eax
009ADF0F  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009ADF13  85 C0                           test eax, eax
009ADF15  0F 88 25 08 00 00               js 0x1409ae740
009ADF1B  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009ADF20  48 8B CF                        mov rcx, rdi
009ADF23  E8 48 5C EE FF                  call 0x140893b70
009ADF28  48 85 C0                        test rax, rax
009ADF2B  0F 84 70 F0 FF FF               je 0x1409acfa1
009ADF31  F6 40 2C 02                     test byte ptr [rax + 0x2c], 2
009ADF35  0F 95 C3                        setne bl
009ADF38  89 1E                           mov dword ptr [rsi], ebx
009ADF3A  E9 4F F8 FF FF                  jmp 0x1409ad78e
009ADF3F  44 8B F8                        mov r15d, eax
009ADF42  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009ADF47  E9 42 F8 FF FF                  jmp 0x1409ad78e
009ADF4C  41 83 FE 08                     cmp r14d, 8
009ADF50  0F 85 4B D6 FF FF               jne 0x1409ab5a1
009ADF56  4C 8B 05 3B 8B 61 00            mov r8, qword ptr [rip + 0x618b3b]
009ADF5D  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ADF62  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ADF67  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009ADF6C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009ADF71  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009ADF79  45 0F B6 CD                     movzx r9d, r13b
009ADF7D  BA 00 04 00 00                  mov edx, 0x400
009ADF82  49 8B CF                        mov rcx, r15
009ADF85  E8 C6 B6 EB FF                  call 0x140869650
009ADF8A  8B D8                           mov ebx, eax
009ADF8C  85 C0                           test eax, eax
009ADF8E  0F 88 AC 07 00 00               js 0x1409ae740
009ADF94  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ADF99  8B 81 2C 07 00 00               mov eax, dword ptr [rcx + 0x72c]
009ADF9F  0F BA F0 1F                     btr eax, 0x1f
009ADFA3  89 06                           mov dword ptr [rsi], eax
009ADFA5  8B 81 4C 07 00 00               mov eax, dword ptr [rcx + 0x74c]
009ADFAB  0F BA F0 1F                     btr eax, 0x1f
009ADFAF  89 46 04                        mov dword ptr [rsi + 4], eax
009ADFB2  E9 F7 E4 FF FF                  jmp 0x1409ac4ae
009ADFB7  8B D8                           mov ebx, eax
009ADFB9  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ADFBE  E9 EB E4 FF FF                  jmp 0x1409ac4ae
009ADFC3  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
009ADFC8  E8 8B 12 8F FF                  call 0x14029f258
009ADFCD  8B C7                           mov eax, edi
009ADFCF  E9 6C 07 00 00                  jmp 0x1409ae740
009ADFD4  BF 59 00 00 C0                  mov edi, 0xc0000059
009ADFD9  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009ADFDE  E9 B1 D1 FF FF                  jmp 0x1409ab194
009ADFE3  41 83 FE 01                     cmp r14d, 1
009ADFE7  0F 85 B4 D5 FF FF               jne 0x1409ab5a1
009ADFED  4C 8B 05 A4 8A 61 00            mov r8, qword ptr [rip + 0x618aa4]
009ADFF4  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009ADFF9  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009ADFFE  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AE003  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AE008  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AE010  45 0F B6 CD                     movzx r9d, r13b
009AE014  BA 00 10 00 00                  mov edx, 0x1000
009AE019  49 8B CF                        mov rcx, r15
009AE01C  E8 2F B6 EB FF                  call 0x140869650
009AE021  8B D8                           mov ebx, eax
009AE023  85 C0                           test eax, eax
009AE025  0F 88 15 07 00 00               js 0x1409ae740
009AE02B  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AE030  83 B9 F0 01 00 00 00            cmp dword ptr [rcx + 0x1f0], 0
009AE037  0F 9C C0                        setl al
009AE03A  88 06                           mov byte ptr [rsi], al
009AE03C  E9 6D E4 FF FF                  jmp 0x1409ac4ae
009AE041  8B D8                           mov ebx, eax
009AE043  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AE048  E9 61 E4 FF FF                  jmp 0x1409ac4ae
009AE04D  41 83 FE 04                     cmp r14d, 4
009AE051  0F 85 4A D5 FF FF               jne 0x1409ab5a1
009AE057  4C 8B 05 3A 8A 61 00            mov r8, qword ptr [rip + 0x618a3a]
009AE05E  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AE063  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AE068  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AE06D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AE072  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AE07A  45 0F B6 CD                     movzx r9d, r13b
009AE07E  BA 00 10 00 00                  mov edx, 0x1000
009AE083  49 8B CF                        mov rcx, r15
009AE086  E8 C5 B5 EB FF                  call 0x140869650
009AE08B  44 8B F8                        mov r15d, eax
009AE08E  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AE092  85 C0                           test eax, eax
009AE094  0F 88 A6 06 00 00               js 0x1409ae740
009AE09A  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009AE09F  48 8B CF                        mov rcx, rdi
009AE0A2  E8 C9 5A EE FF                  call 0x140893b70
009AE0A7  48 85 C0                        test rax, rax
009AE0AA  0F 84 F1 EE FF FF               je 0x1409acfa1
009AE0B0  F6 40 2C 10                     test byte ptr [rax + 0x2c], 0x10
009AE0B4  0F 95 C3                        setne bl
009AE0B7  89 1E                           mov dword ptr [rsi], ebx
009AE0B9  E9 D0 F6 FF FF                  jmp 0x1409ad78e
009AE0BE  44 8B F8                        mov r15d, eax
009AE0C1  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009AE0C6  E9 C3 F6 FF FF                  jmp 0x1409ad78e
009AE0CB  41 F6 C6 07                     test r14b, 7
009AE0CF  0F 85 CC D4 FF FF               jne 0x1409ab5a1
009AE0D5  41 81 FE 00 01 00 00            cmp r14d, 0x100
009AE0DC  0F 87 BF D4 FF FF               ja 0x1409ab5a1
009AE0E2  4C 8B 05 AF 89 61 00            mov r8, qword ptr [rip + 0x6189af]
009AE0E9  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AE0EE  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AE0F3  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AE0F8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AE0FD  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AE105  45 0F B6 CD                     movzx r9d, r13b
009AE109  BA 00 10 00 00                  mov edx, 0x1000
009AE10E  49 8B CF                        mov rcx, r15
009AE111  E8 3A B5 EB FF                  call 0x140869650
009AE116  44 8B F8                        mov r15d, eax
009AE119  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AE11D  85 C0                           test eax, eax
009AE11F  0F 88 7C D9 FF FF               js 0x1409abaa1
009AE125  83 FF 43                        cmp edi, 0x43
009AE128  0F 94 C3                        sete bl
009AE12B  44 8B CB                        mov r9d, ebx
009AE12E  41 B8 20 00 00 00               mov r8d, 0x20
009AE134  48 8D 94 24 C0 08 00 00         lea rdx, [rsp + 0x8c0]
009AE13C  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AE141  E8 22 FF B2 FF                  call 0x1404de068
009AE146  8D 1C C5 00 00 00 00            lea ebx, [rax*8]
009AE14D  BA 50 73 51 79                  mov edx, 0x79517350
009AE152  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AE157  E8 84 97 94 FF                  call 0x1402f78e0
009AE15C  89 9C 24 E0 01 00 00            mov dword ptr [rsp + 0x1e0], ebx
009AE163  4D 85 E4                        test r12, r12
009AE166  74 04                           je 0x1409ae16c
009AE168  41 89 1C 24                     mov dword ptr [r12], ebx
009AE16C  41 3B DE                        cmp ebx, r14d
009AE16F  41 0F 43 DE                     cmovae ebx, r14d
009AE173  89 9C 24 E0 01 00 00            mov dword ptr [rsp + 0x1e0], ebx
009AE17A  44 8B C3                        mov r8d, ebx
009AE17D  48 8D 94 24 C0 08 00 00         lea rdx, [rsp + 0x8c0]
009AE185  48 8B CE                        mov rcx, rsi
009AE188  E8 B3 86 D1 FF                  call 0x1406c6840
009AE18D  E9 0F D9 FF FF                  jmp 0x1409abaa1
009AE192  44 8B F8                        mov r15d, eax
009AE195  E9 07 D9 FF FF                  jmp 0x1409abaa1
009AE19A  4D 8B CC                        mov r9, r12
009AE19D  45 8B C6                        mov r8d, r14d
009AE1A0  48 8B D6                        mov rdx, rsi
009AE1A3  49 8B CF                        mov rcx, r15
009AE1A6  E8 09 C7 11 00                  call 0x140aca8b4
009AE1AB  E9 90 05 00 00                  jmp 0x1409ae740
009AE1B0  4C 8B 05 E1 88 61 00            mov r8, qword ptr [rip + 0x6188e1]
009AE1B7  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AE1BC  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AE1C1  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AE1C6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AE1CB  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AE1D3  45 0F B6 CD                     movzx r9d, r13b
009AE1D7  BA 00 04 00 00                  mov edx, 0x400
009AE1DC  49 8B CF                        mov rcx, r15
009AE1DF  E8 6C B4 EB FF                  call 0x140869650
009AE1E4  85 C0                           test eax, eax
009AE1E6  0F 88 54 05 00 00               js 0x1409ae740
009AE1EC  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
009AE1F1  E9 33 E4 FF FF                  jmp 0x1409ac629
009AE1F6  41 83 FE 01                     cmp r14d, 1
009AE1FA  0F 85 A1 D3 FF FF               jne 0x1409ab5a1
009AE200  4C 8B 05 91 88 61 00            mov r8, qword ptr [rip + 0x618891]
009AE207  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AE20C  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AE211  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AE216  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AE21B  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AE223  45 0F B6 CD                     movzx r9d, r13b
009AE227  BA 00 10 00 00                  mov edx, 0x1000
009AE22C  49 8B CF                        mov rcx, r15
009AE22F  E8 1C B4 EB FF                  call 0x140869650
009AE234  8B D8                           mov ebx, eax
009AE236  85 C0                           test eax, eax
009AE238  0F 88 02 05 00 00               js 0x1409ae740
009AE23E  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AE243  8B 81 FC 05 00 00               mov eax, dword ptr [rcx + 0x5fc]
009AE249  C1 E8 09                        shr eax, 9
009AE24C  41 22 C6                        and al, r14b
009AE24F  88 06                           mov byte ptr [rsi], al
009AE251  E9 58 E2 FF FF                  jmp 0x1409ac4ae
009AE256  8B D8                           mov ebx, eax
009AE258  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AE25D  E9 4C E2 FF FF                  jmp 0x1409ac4ae
009AE262  B8 02 00 00 C0                  mov eax, 0xc0000002
009AE267  E9 D4 04 00 00                  jmp 0x1409ae740
009AE26C  4C 8B 05 25 88 61 00            mov r8, qword ptr [rip + 0x618825]
009AE273  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AE278  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AE27D  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AE282  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AE287  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AE28F  45 0F B6 CD                     movzx r9d, r13b
009AE293  BA 00 04 00 00                  mov edx, 0x400
009AE298  49 8B CF                        mov rcx, r15
009AE29B  E8 B0 B3 EB FF                  call 0x140869650
009AE2A0  85 C0                           test eax, eax
009AE2A2  0F 88 98 04 00 00               js 0x1409ae740
009AE2A8  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AE2AD  41 B9 01 00 00 00               mov r9d, 1
009AE2B3  E9 E1 E8 FF FF                  jmp 0x1409acb99
009AE2B8  EB 0C                           jmp 0x1409ae2c6
009AE2BA  8B D8                           mov ebx, eax
009AE2BC  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AE2C1  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
009AE2C6  49 83 FF FF                     cmp r15, -1
009AE2CA  0F 85 DE E1 FF FF               jne 0x1409ac4ae
009AE2D0  E9 61 DA FF FF                  jmp 0x1409abd36
009AE2D5  E8 6E 69 0F 00                  call 0x140aa4c48
009AE2DA  8B D8                           mov ebx, eax
009AE2DC  BA 50 73 51 79                  mov edx, 0x79517350
009AE2E1  48 8B CF                        mov rcx, rdi
009AE2E4  E8 F7 95 94 FF                  call 0x1402f78e0
009AE2E9  8B C3                           mov eax, ebx
009AE2EB  E9 50 04 00 00                  jmp 0x1409ae740
009AE2F0  4C 8B 05 A1 87 61 00            mov r8, qword ptr [rip + 0x6187a1]
009AE2F7  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
009AE2FC  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
009AE301  48 8D 44 24 40                  lea rax, [rsp + 0x40]
009AE306  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009AE30B  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009AE313  45 0F B6 CD                     movzx r9d, r13b
009AE317  BA 00 10 00 00                  mov edx, 0x1000
009AE31C  49 8B CF                        mov rcx, r15
009AE31F  E8 2C B3 EB FF                  call 0x140869650
009AE324  85 C0                           test eax, eax
009AE326  0F 88 14 04 00 00               js 0x1409ae740
009AE32C  4D 8B CC                        mov r9, r12
009AE32F  45 8B C6                        mov r8d, r14d
009AE332  48 8B D6                        mov rdx, rsi
009AE335  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009AE33A  E8 4D 38 D5 FF                  call 0x140701b8c
009AE33F  E9 E1 D9 FF FF                  jmp 0x1409abd25
009AE344  48 89 9C 24 F0 01 00 00         mov qword ptr [rsp + 0x1f0], rbx
009AE34C  41 83 FE 08                     cmp r14d, 8
009AE350  0F 85 4B D2 FF FF               jne 0x1409ab5a1
009AE356  45 84 ED                        test r13b, r13b
009AE359  74 14                           je 0x1409ae36f
009AE35B  49 3B F0                        cmp rsi, r8
009AE35E  4C 0F 42 C6                     cmovb r8, rsi
009AE362  49 8B 00                        mov rax, qword ptr [r8]
009AE365  49 89 00                        mov qword ptr [r8], rax
009AE368  EB 05                           jmp 0x1409ae36f
009AE36A  E9 D1 03 00 00                  jmp 0x1409ae740
009AE36F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009AE378  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
009AE37F  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
009AE384  49 83 FF FF                     cmp r15, -1
009AE388  0F 85 F8 D7 FF FF               jne 0x1409abb86
009AE38E  49 3B 8A 20 02 00 00            cmp rcx, qword ptr [r10 + 0x220]
009AE395  0F 85 EB D7 FF FF               jne 0x1409abb86
009AE39B  48 8D 84 24 F0 01 00 00         lea rax, [rsp + 0x1f0]
009AE3A3  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009AE3A8  44 88 6C 24 28                  mov byte ptr [rsp + 0x28], r13b
009AE3AD  48 8B 05 24 88 61 00            mov rax, qword ptr [rip + 0x618824]
009AE3B4  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009AE3B9  45 8D 4F 06                     lea r9d, [r15 + 6]
009AE3BD  45 33 C0                        xor r8d, r8d
009AE3C0  33 D2                           xor edx, edx
009AE3C2  48 8B 89 A8 02 00 00            mov rcx, qword ptr [rcx + 0x2a8]
009AE3C9  E8 52 90 F0 FF                  call 0x1408b7420
009AE3CE  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AE3D2  85 C0                           test eax, eax
009AE3D4  0F 88 66 03 00 00               js 0x1409ae740
009AE3DA  48 8B 8C 24 F0 01 00 00         mov rcx, qword ptr [rsp + 0x1f0]
009AE3E2  48 89 0E                        mov qword ptr [rsi], rcx
009AE3E5  4D 85 E4                        test r12, r12
009AE3E8  74 08                           je 0x1409ae3f2
009AE3EA  41 C7 04 24 08 00 00 00         mov dword ptr [r12], 8
009AE3F2  E9 49 03 00 00                  jmp 0x1409ae740
009AE3F7  E9 44 03 00 00                  jmp 0x1409ae740
009AE3FC  BA 50 73 51 79                  mov edx, 0x79517350
009AE401  E8 DA 94 94 FF                  call 0x1402f78e0
009AE406  B8 7C 00 00 C0                  mov eax, 0xc000007c
009AE40B  E9 30 03 00 00                  jmp 0x1409ae740
009AE410  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009AE414  E9 0E D9 FF FF                  jmp 0x1409abd27
009AE419  8B D8                           mov ebx, eax
009AE41B  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AE41F  E9 03 D9 FF FF                  jmp 0x1409abd27
009AE424  48 8B FE                        mov rdi, rsi
009AE427  E9 A3 E8 FF FF                  jmp 0x1409acccf
009AE42C  4D 85 E4                        test r12, r12
009AE42F  74 08                           je 0x1409ae439
009AE431  41 C7 04 24 04 00 00 00         mov dword ptr [r12], 4
009AE439  8B C1                           mov eax, ecx
009AE43B  E9 00 03 00 00                  jmp 0x1409ae740
009AE440  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009AE444  89 5E 04                        mov dword ptr [rsi + 4], ebx
009AE447  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AE44C  F7 80 50 07 00 00 00 00 00 40   test dword ptr [rax + 0x750], 0x40000000
009AE456  74 09                           je 0x1409ae461
009AE458  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AE45B  83 C8 01                        or eax, 1
009AE45E  89 46 04                        mov dword ptr [rsi + 4], eax
009AE461  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AE466  83 B8 50 07 00 00 00            cmp dword ptr [rax + 0x750], 0
009AE46D  7D 09                           jge 0x1409ae478
009AE46F  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AE472  83 C8 02                        or eax, 2
009AE475  89 46 04                        mov dword ptr [rsi + 4], eax
009AE478  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AE47D  F7 80 54 07 00 00 00 10 00 00   test dword ptr [rax + 0x754], 0x1000
009AE487  74 09                           je 0x1409ae492
009AE489  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AE48C  83 C8 04                        or eax, 4
009AE48F  89 46 04                        mov dword ptr [rsi + 4], eax
009AE492  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AE497  F7 80 54 07 00 00 00 20 00 00   test dword ptr [rax + 0x754], 0x2000
009AE4A1  74 09                           je 0x1409ae4ac
009AE4A3  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AE4A6  83 C8 08                        or eax, 8
009AE4A9  89 46 04                        mov dword ptr [rsi + 4], eax
009AE4AC  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009AE4B1  8B 88 D8 07 00 00               mov ecx, dword ptr [rax + 0x7d8]
009AE4B7  F6 C1 01                        test cl, 1
009AE4BA  74 09                           je 0x1409ae4c5
009AE4BC  8B 46 04                        mov eax, dword ptr [rsi + 4]
009AE4BF  83 C8 10                        or eax, 0x10
009AE4C2  89 46 04                        mov dword ptr [rsi + 4], eax
009AE4C5  E9 3C C0 FF FF                  jmp 0x1409aa506
009AE4CA  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009AE4CE  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
009AE4D3  E9 2E C0 FF FF                  jmp 0x1409aa506
009AE4D8  BF 04 00 00 C0                  mov edi, 0xc0000004
009AE4DD  E9 F2 DB FF FF                  jmp 0x1409ac0d4
009AE4E2  8B 9C 24 40 01 00 00            mov ebx, dword ptr [rsp + 0x140]
009AE4E9  E9 AD F9 FF FF                  jmp 0x1409ade9b
009AE4EE  E8 5D AE 94 FF                  call 0x1402f9350
009AE4F3  E9 23 CC FF FF                  jmp 0x1409ab11b
009AE4F8  41 C7 04 24 08 00 00 00         mov dword ptr [r12], 8
009AE500  E9 9C D0 FF FF                  jmp 0x1409ab5a1
009AE505  E9 36 02 00 00                  jmp 0x1409ae740
009AE50A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009AE513  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
009AE51A  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
009AE51F  89 5C 24 48                     mov dword ptr [rsp + 0x48], ebx
009AE523  4C 8B 81 E0 02 00 00            mov r8, qword ptr [rcx + 0x2e0]
009AE52A  4D 85 C0                        test r8, r8
009AE52D  0F 84 95 F2 17 00               je 0x140b2d7c8
009AE533  48 8B C3                        mov rax, rbx
009AE536  48 8B 91 10 03 00 00            mov rdx, qword ptr [rcx + 0x310]
009AE53D  48 85 D2                        test rdx, rdx
009AE540  0F 84 3E F2 17 00               je 0x140b2d784
009AE546  48 8B 02                        mov rax, qword ptr [rdx]
009AE549  E9 36 F2 17 00                  jmp 0x140b2d784
009AE54E  B8 03 00 00 C0                  mov eax, 0xc0000003
009AE553  E9 E8 01 00 00                  jmp 0x1409ae740
009AE558  85 C0                           test eax, eax
009AE55A  0F 88 D9 FE FF FF               js 0x1409ae439
009AE560  E9 9A E7 FF FF                  jmp 0x1409accff
009AE565  90                              nop
009AE566  66 90                           nop
009AE568  5A                              pop rdx
009AE569  AC                              lodsb al, byte ptr [rsi]
009AE56A  9A                              .byte 0x9a
009AE56B  00 92 A4 9A 00 EC               add byte ptr [rdx - 0x13ff655c], dl
009AE571  AB                              stosd dword ptr [rdi], eax
009AE572  9A                              .byte 0x9a
009AE573  00 D8                           add al, bl
009AE575  AC                              lodsb al, byte ptr [rsi]
009AE576  9A                              .byte 0x9a
009AE577  00 47 B0                        add byte ptr [rdi - 0x50], al
009AE57A  9A                              .byte 0x9a
009AE57B  00 CE                           add dh, cl
009AE57D  AD                              lodsd eax, dword ptr [rsi]
009AE57E  9A                              .byte 0x9a
009AE57F  00 D2                           add dl, dl
009AE581  A9 9A 00 00 AE                  test eax, 0xae00009a
009AE586  9A                              .byte 0x9a
009AE587  00 34 AE                        add byte ptr [rsi + rbp*4], dh
009AE58A  9A                              .byte 0x9a
009AE58B  00 44 AD 9A                     add byte ptr [rbp + rbp*4 - 0x66], al
009AE58F  00 88 BF 9A 00 3B               add byte ptr [rax + 0x3b009abf], cl
009AE595  AA                              stosb byte ptr [rdi], al
009AE596  9A                              .byte 0x9a
009AE597  00 79 AE                        add byte ptr [rcx - 0x52], bh
009AE59A  9A                              .byte 0x9a
009AE59B  00 40 E4                        add byte ptr [rax - 0x1c], al
009AE59E  9A                              .byte 0x9a
009AE59F  00 0C D2                        add byte ptr [rdx + rdx*8], cl
009AE5A2  9A                              .byte 0x9a
009AE5A3  00 F2                           add dl, dh
009AE5A5  C9                              leave
009AE5A6  9A                              .byte 0x9a
009AE5A7  00 4D A5                        add byte ptr [rbp - 0x5b], cl
009AE5AA  9A                              .byte 0x9a
009AE5AB  00 54 B0 9A                     add byte ptr [rax + rsi*4 - 0x66], dl
009AE5AF  00 1C BE                        add byte ptr [rsi + rdi*4], bl
009AE5B2  9A                              .byte 0x9a
009AE5B3  00 26                           add byte ptr [rsi], ah
009AE5B5  B2 9A                           mov dl, 0x9a
009AE5B7  00 8D AF 9A 00 92               add byte ptr [rbp - 0x6dff6551], cl
009AE5BD  C6                              .byte 0xc6
009AE5BE  9A                              .byte 0x9a
009AE5BF  00 E4                           add ah, ah
009AE5C1  BC 9A 00 9E B7                  mov esp, 0xb79e009a
009AE5C6  9A                              .byte 0x9a
009AE5C7  00 86 CF 9A 00 26               add byte ptr [rsi + 0x26009acf], al
009AE5CD  C4                              .byte 0xc4
009AE5CE  9A                              .byte 0x9a
009AE5CF  00 A4 B1 9A 00 AC CF            add byte ptr [rcx + rsi*4 - 0x3053ff66], ah
009AE5D6  9A                              .byte 0x9a
009AE5D7  00 07                           add byte ptr [rdi], al
009AE5D9  CE                              .byte 0xce
009AE5DA  9A                              .byte 0x9a
009AE5DB  00 BB C7 9A 00 16               add byte ptr [rbx + 0x16009ac7], bh
009AE5E1  D5                              .byte 0xd5
009AE5E2  9A                              .byte 0x9a
009AE5E3  00 EA                           add dl, ch
009AE5E5  B4 9A                           mov ah, 0x9a
009AE5E7  00 A9 BA 9A 00 BD               add byte ptr [rcx - 0x42ff6546], ch
009AE5ED  BB 9A 00 71 B0                  mov ebx, 0xb071009a
009AE5F2  9A                              .byte 0x9a
009AE5F3  00 BF C4 9A 00 9D               add byte ptr [rdi - 0x62ff653c], bh
009AE5F9  CE                              .byte 0xce
009AE5FA  9A                              .byte 0x9a
009AE5FB  00 7A D3                        add byte ptr [rdx - 0x2d], bh
009AE5FE  9A                              .byte 0x9a
009AE5FF  00 85 D4 9A 00 F4               add byte ptr [rbp - 0xbff652c], al
009AE605  C1 9A 00 34 CA 9A 00            rcr dword ptr [rdx - 0x6535cc00], 0
009AE60C  7B BC                           jnp 0x1409ae5ca
009AE60E  9A                              .byte 0x9a
009AE60F  00 A0 BD 9A 00 AB               add byte ptr [rax - 0x54ff6543], ah
009AE615  B5 9A                           mov ch, 0x9a
009AE617  00 9F C3 9A 00 D2               add byte ptr [rdi - 0x2dff653d], bl
009AE61D  CA 9A 00                        retf 0x9a
009AE620  74 B6                           je 0x1409ae5d8
009AE622  9A                              .byte 0x9a
009AE623  00 BD D7 9A 00 D7               add byte ptr [rbp - 0x28ff6529], bh
009AE629  D8 9A 00 EC DA 9A               fcomp dword ptr [rdx - 0x65251400]
009AE62F  00 F7                           add bh, dh
009AE631  D9 9A 00 E5 C1 9A               fstp dword ptr [rdx - 0x653e1b00]
009AE637  00 5D B8                        add byte ptr [rbp - 0x48], bl
009AE63A  9A                              .byte 0x9a
009AE63B  00 0D C3 9A 00 CE               add byte ptr [rip - 0x31ff653d], cl
009AE641  DE 9A 00 4C DF 9A               ficomp word ptr [rdx - 0x6520b400]
009AE647  00 DF                           add bh, bl
009AE649  C4                              .byte 0xc4
009AE64A  9A                              .byte 0x9a
009AE64B  00 96 DB 9A 00 6E               add byte ptr [rsi + 0x6e009adb], dl
009AE651  C1 9A 00 22 B1 9A 00            rcr dword ptr [rdx - 0x654ede00], 0
009AE658  1E                              .byte 0x1e
009AE659  BF 9A 00 B6 BF                  mov edi, 0xbfb6009a
009AE65E  9A                              .byte 0x9a
009AE65F  00 CB                           add bl, cl
009AE661  E0 9A                           loopne 0x1409ae5fd
009AE663  00 8B C8 9A 00 E3               add byte ptr [rbx - 0x1cff6538], cl
009AE669  DF 9A 00 4D E0 9A               fistp word ptr [rdx - 0x651fb300]
009AE66F  00 9A E1 9A 00 00               add byte ptr [rdx + 0x9ae1], bl
009AE675  C6                              .byte 0xc6
009AE676  9A                              .byte 0x9a
009AE677  00 F6                           add dh, dh
009AE679  E1 9A                           loope 0x1409ae615
009AE67B  00 F6                           add dh, dh
009AE67D  C0 9A 00 85 DD 9A 00            rcr byte ptr [rdx - 0x65227b00], 0
009AE684  FE                              .byte 0xfe
009AE685  B3 9A                           mov bl, 0x9a
009AE687  00 70 CB                        add byte ptr [rax - 0x35], dh
009AE68A  9A                              .byte 0x9a
009AE68B  00 FC                           add ah, bh
009AE68D  AE                              scasb al, byte ptr [rdi]
009AE68E  9A                              .byte 0x9a
009AE68F  00 CF                           add bh, cl
009AE691  DC 9A 00 20 BB 9A               fcomp qword ptr [rdx - 0x6544e000]
009AE697  00 F0                           add al, dh
009AE699  E2 9A                           loop 0x1409ae635
009AE69B  00 CD                           add ch, cl
009AE69D  C1 9A 00 23 D0 9A 00            rcr dword ptr [rdx - 0x652fdd00], 0
009AE6A4  44 E3 9A                        jrcxz 0x1409ae641
009AE6A7  00 45 C4                        add byte ptr [rbp - 0x3c], al
009AE6AA  9A                              .byte 0x9a
009AE6AB  00 DF                           add bh, bl
009AE6AD  CB                              retf
009AE6AE  9A                              .byte 0x9a
009AE6AF  00 DE                           add dh, bl
009AE6B1  C0 9A 00 CA AE 9A 00            rcr byte ptr [rdx - 0x65513600], 0
009AE6B8  2D DE 9A 00 4E                  sub eax, 0x4e009ade
009AE6BD  E5 9A                           in eax, 0x9a
009AE6BF  00 39                           add byte ptr [rcx], bh
009AE6C1  DC 9A 00 64 CC 9A               fcomp qword ptr [rdx - 0x65339c00]
009AE6C7  00 4E E5                        add byte ptr [rsi - 0x1b], cl
009AE6CA  9A                              .byte 0x9a
009AE6CB  00 00                           add byte ptr [rax], al
009AE6CD  01 02                           add dword ptr [rdx], eax
009AE6CF  03 04 48                        add eax, dword ptr [rax + rcx*2]
009AE6D2  48 05 48 48 06 48               add rax, 0x48064848
009AE6D8  07                              .byte 0x07
009AE6D9  48 08 09                        or byte ptr [rcx], cl
009AE6DC  48 48 0A 0B                     or cl, byte ptr [rbx]
009AE6E0  0C 0D                           or al, 0xd
009AE6E2  0E                              .byte 0x0e
009AE6E3  0F 10 48 11                     movups xmm1, xmmword ptr [rax + 0x11]
009AE6E7  12 13                           adc dl, byte ptr [rbx]
009AE6E9  14 15                           adc al, 0x15
009AE6EB  16                              .byte 0x16
009AE6EC  17                              .byte 0x17
009AE6ED  18 19                           sbb byte ptr [rcx], bl
009AE6EF  48 1A 1B                        sbb bl, byte ptr [rbx]
009AE6F2  1C 1D                           sbb al, 0x1d
009AE6F4  48 48 09 1E                     or qword ptr [rsi], rbx
009AE6F8  1F                              .byte 0x1f
009AE6F9  20 21                           and byte ptr [rcx], ah
009AE6FB  22 48 23                        and cl, byte ptr [rax + 0x23]
009AE6FE  24 25                           and al, 0x25
009AE700  48                              .byte 0x48
009AE701  48                              .byte 0x48
009AE702  26                              .byte 0x26
009AE703  27                              .byte 0x27
009AE704  48 48 28 29                     sub byte ptr [rcx], bpl
009AE708  2A 2B                           sub ch, byte ptr [rbx]
009AE70A  48 48 2C 2D                     sub al, 0x2d
009AE70E  2E                              .byte 0x2e
009AE70F  2E                              .byte 0x2e
009AE710  48                              .byte 0x48
009AE711  2F                              .byte 0x2f
009AE712  30 31                           xor byte ptr [rcx], dh
009AE714  32 33                           xor dh, byte ptr [rbx]
009AE716  34 35                           xor al, 0x35
009AE718  36                              .byte 0x36
009AE719  37                              .byte 0x37
009AE71A  48 38 48 39                     cmp byte ptr [rax + 0x39], cl
009AE71E  3A 48 3B                        cmp cl, byte ptr [rax + 0x3b]
009AE721  3C 48                           cmp al, 0x48
009AE723  3D 3E 3F 48 48                  cmp eax, 0x48483f3e
009AE728  40 48 41 48 3D 42 48 48 48      cmp rax, 0x48484842
009AE731  48 48 48 48 48 43 48 48 44 18 1D 48 45 46 47  sbb byte ptr [rip + 0x47464548], r11b
009AE740  48 8B 8C 24 C0 09 00 00         mov rcx, qword ptr [rsp + 0x9c0]
009AE748  48 33 CC                        xor rcx, rsp
009AE74B  E8 F0 DE CF FF                  call 0x1406ac640
009AE750  48 81 C4 D0 09 00 00            add rsp, 0x9d0
009AE757  41 5F                           pop r15
009AE759  41 5E                           pop r14
009AE75B  41 5D                           pop r13
009AE75D  41 5C                           pop r12
009AE75F  5F                              pop rdi
009AE760  5E                              pop rsi
009AE761  5B                              pop rbx
009AE762  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtQueryInformationProcess(__int64 a1, int a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m308;
    unsigned __int64 v_stack_m398;
    unsigned __int64 v_stack_m3A8;
    unsigned __int64 v_stack_m3C0;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m428;
    unsigned __int64 v_stack_m438;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m540;
    unsigned __int64 v_stack_m548;
    unsigned __int64 v_stack_m558;
    unsigned __int64 v_stack_m568;
    unsigned __int64 v_stack_m570;
    unsigned __int64 v_stack_m578;
    unsigned __int64 v_stack_m588;
    unsigned __int64 v_stack_m598;
    unsigned __int64 v_stack_m5A8;
    unsigned __int64 v_stack_m5B8;
    unsigned int v_stack_m5C0;
    unsigned __int64 v_stack_m5C8;
    unsigned __int64 v_stack_m5D8;
    unsigned int v_stack_m660;
    unsigned __int64 v_stack_m668;
    unsigned __int64 v_stack_m678;
    unsigned __int64 v_stack_m698;
    unsigned __int64 v_stack_m6A0;
    unsigned __int64 v_stack_m6A8;
    unsigned __int64 v_stack_m6B0;
    unsigned __int64 v_stack_m6B8;
    unsigned __int64 v_stack_m6C0;
    unsigned __int64 v_stack_m6E8;
    unsigned __int64 v_stack_m6F0;
    unsigned __int64 v_stack_m700;
    unsigned __int64 v_stack_m708;
    unsigned __int64 v_stack_m710;
    unsigned __int64 v_stack_m720;
    unsigned __int64 v_stack_m728;
    unsigned __int64 v_stack_m730;
    unsigned __int64 v_stack_m748;
    unsigned int v_stack_m780;
    unsigned __int64 v_stack_m810;
    unsigned __int64 v_stack_m818;
    unsigned __int64 v_stack_m820;
    unsigned int v_stack_m828;
    unsigned int v_stack_m830;
    unsigned int v_stack_m838;
    unsigned __int64 v_stack_m840;
    unsigned __int64 v_stack_m848;
    unsigned int v_stack_m84C;
    unsigned int v_stack_m850;
    unsigned int v_stack_m854;
    unsigned int v_stack_m858;
    unsigned __int64 v_stack_m860;
    unsigned __int64 v_stack_m868;
    unsigned __int64 v_stack_m870;
    unsigned __int64 v_stack_m878;
    unsigned __int64 v_stack_m880;
    unsigned __int64 v_stack_m888;
    unsigned __int64 v_stack_m890;
    unsigned __int64 v_stack_m898;
    unsigned __int64 v_stack_m8A0;
    unsigned __int64 v_stack_m8A8;
    unsigned __int64 v_stack_m8B0;
    unsigned int v_stack_m8B8;
    unsigned __int64 v_stack_m8C0;
    unsigned __int64 v_stack_m8C8;
    unsigned __int64 v_stack_m8D8;
    unsigned __int64 v_stack_m8E0;
    unsigned __int64 v_stack_m8E8;
    unsigned __int64 v_stack_m8F0;
    unsigned __int64 v_stack_m8F8;
    unsigned __int64 v_stack_m900;
    unsigned int v_stack_m904;
    unsigned __int64 v_stack_m908;
    unsigned __int64 v_stack_m910;
    unsigned int v_stack_m918;
    unsigned int v_stack_m91C;
    unsigned int v_stack_m920;
    unsigned int v_stack_m924;
    unsigned __int64 v_stack_m928;
    unsigned int v_stack_m92C;
    unsigned __int64 v_stack_m930;
    unsigned __int16 v_stack_m936;
    unsigned __int64 v_stack_m938;
    unsigned int v_stack_m940;
    unsigned __int64 v_stack_m948;
    unsigned int v_stack_m950;
    unsigned __int64 v_stack_m958;
    unsigned __int64 v_stack_m960;
    unsigned __int64 v_stack_m968;
    unsigned __int8 v_stack_m96F;
    unsigned __int16 v_stack_m970;
    unsigned __int64 v_stack_m978;
    unsigned __int64 v_stack_m9A0;
    unsigned __int16 v_stack_m9A8;
    unsigned int v_stack_m9AC;
    unsigned __int16 v_stack_m9AE;
    unsigned __int64 v_stack_m9B0;
    unsigned int v_stack_m9B8;
    unsigned __int8 v_stack_m9B9;
    unsigned __int8 v_stack_m9BA;
    unsigned __int8 v_stack_m9BB;
    unsigned __int8 v_stack_m9BC;
    unsigned int v_stack_m9C0;
    unsigned __int64 v_stack_m9C8;
    unsigned __int64 v_stack_m9D0;
    unsigned __int64 v_stack_m9D8;
    unsigned __int64 v_stack_m9E0;
    unsigned int v_stack_m9E8;
    unsigned int v_stack_mA08;

    v_rsp = (v_rsp) - (0x9D0ULL);
    result = (*(unsigned __int64 *)(v_rip + 4588758)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m9A0 = a1;
    v_stack_m8E0 = a3;
    v_stack_m830 = (unsigned int)((unsigned int)(a4));
    v_stack_m8D8 = a5;
    v_stack_m5A8 = v_xmm0;
    v_stack_m598 = v_xmm0;
    v_stack_m588 = v_xmm0;
    v_rbx = 0;
    v_stack_m9B8 = 0;
    v_stack_m8E8 = 0;
    v_stack_m91C = 0;
    a2 = 0;
    result = memset(v_stack_m548, a2, 264, a4);
    v_stack_m960 = 0;
    v_stack_m5D8 = v_xmm0;
    v_stack_m850 = 0;
    v_stack_m854 = 0;
    a2 = 0;
    result = memset(v_stack_m438, a2, 152, a4);
    v_stack_m700 = v_xmm0;
    v_stack_m848 = 0;
    result = 0;
    v_stack_m578 = v_xmm1;
    v_stack_m568 = v_xmm1;
    v_stack_m558 = 0;
    v_stack_m840 = 0;
    v_stack_m968 = 0;
    v_stack_m9A8 = 0;
    v_stack_m970 = 0;
    v_stack_m9C8 = 0;
    v_stack_m820 = 0;
    v_stack_m910 = 0;
    a2 = 0;
    result = memset(v_stack_m6E8, a2, v_rbx + 104, a4);
    a2 = 0;
    result = memset(v_stack_m8C8, a2, v_rbx + 112, a4);
    v_stack_m9BC = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m948 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_009AA85F;
    v_stack_m978 = 3;
loc_009AA3F3:
    if (((unsigned int)((int)(a2))) != 52) goto loc_009AA525;
    v_stack_m918 = 0;
    v_stack_m9BA = 0;
    v_stack_m9B9 = 0;
    if (((unsigned int)((unsigned int)(a4))) != 8) goto loc_009AB5A1;
    v_stack_m858 = (unsigned int)((unsigned int)(*(unsigned int *)(a3)));
    goto loc_009AA427;
loc_009AA427:
    if (a1 == -1) goto loc_009AA9B1;
    v_stack_m9D0 = 0;
    v_stack_m9D8 = 0;
    v_stack_m9E0 = v_stack_m9C8;
    v_stack_m9E8 = 0x79517350ULL;
    result = ObpReferenceObjectByHandleWithTag(a1, (unsigned int)(0x1000ULL), *(unsigned __int64 *)(v_rip + 6407776), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (sign_flag) goto loc_009AE740;
loc_009AA46D:
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(a3))) - 1);
    if (((unsigned int)(v_rdi)) > 15) goto loc_009AB047;
    result = ((unsigned int)(*(unsigned int *)(v_rip - 10134658 + (int)((unsigned int)(v_rdi)) * 4 + 10151272))) + (v_rip - 10134658);
loc_009AA506:
    if (a1 != -1) {
        a2 = 0x79517350ULL;
        a1 = v_stack_m9C8;
        result = ObfDereferenceObjectWithTag(a1, a2, *(unsigned __int64 *)(v_rip + 6407776), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    }
    goto loc_009AE740;
loc_009AA525:
    if (((unsigned int)(v_rdi)) > 115) goto loc_009AE54E;
    a2 = ((unsigned int)(*(unsigned int *)(v_rip - 10134837 + *(unsigned __int8 *)(v_rip - 10134837 + v_rdi * 1 + 10151628) * 4 + 10151336))) + (v_rip - 10134837);
loc_009AA85F:
    if (((unsigned int)(v_rdi)) == 18) goto loc_009AA938;
    if (((unsigned int)(v_rdi)) == 61) goto loc_009AA938;
    if (((unsigned int)(v_rdi)) == 65) goto loc_009AA98B;
    if ((((unsigned int)(v_rdi - 70)) & (0xFFFFFFFBULL)) == 0) goto loc_009AA938;
    if (((unsigned int)(v_rdi)) == 92) goto loc_009AA96F;
    if (((unsigned int)(v_rdi)) == 94) goto loc_009AA91F;
    if (((unsigned int)(v_rdi)) == 87) goto loc_009AA938;
    if (((unsigned int)(v_rdi)) == 47) goto loc_009AA94F;
    v_stack_m978 = 3;
    result = 3;
    if (((unsigned int)(v_rdi)) == 115) { result = 7; }
loc_009AA8D0:
    if ((unsigned int)((unsigned int)(a4)) == 0) goto loc_009AA90E;
    if ((((unsigned int)((unsigned int)(result))) & (a3)) != 0) goto loc_009AA91A;
    if ((a3 + (unsigned int)(a4) * 1) > (*(unsigned __int64 *)(v_rip + 6407776))) goto loc_009AA969;
    if ((a3 + (unsigned int)(a4) * 1) < a3) goto loc_009AA969;
loc_009AA8F2:
    if (a5 == 0) goto loc_009AA9A7;
    a1 = *(unsigned __int64 *)(v_rip + 6407776);
    if (a5 < (*(unsigned __int64 *)(v_rip + 6407776))) { a1 = a5; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    goto loc_009AA9A7;
loc_009AA90E:
    goto loc_009AA8F2;
loc_009AA91A:
    result = ExRaiseDatatypeMisalignment(a1, a2, *(unsigned __int64 *)(v_rip + 6407776), 1);
loc_009AA91F:
    v_stack_m978 = 3;
    goto loc_009AA8D0;
loc_009AA938:
    v_stack_m978 = 3;
    goto loc_009AA8D0;
loc_009AA94F:
    v_stack_m978 = 3;
    goto loc_009AA8D0;
loc_009AA969:
    goto loc_009AA8F2;
loc_009AA96F:
    v_stack_m978 = 3;
    goto loc_009AA8D0;
loc_009AA98B:
    v_stack_m978 = 3;
    goto loc_009AA8D0;
loc_009AA9A7:
    goto loc_009AA3F3;
loc_009AA9B1:
    v_stack_m9C8 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    goto loc_009AA46D;
loc_009AB047:
    v_stack_m9C0 = 0xC00000BBULL;
    goto loc_009AA506;
loc_009AB5A1:
    goto loc_009AE740;
loc_009AE54E:
    goto loc_009AE740;
loc_009AE740:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, *(unsigned __int64 *)(v_rip + 6407776), 1);
    v_rsp = (v_rsp) + (0x9D0ULL);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtQueryInformationProcess(int64_t Arg1, int32_t Arg2, void *Arg3, int32_t Arg4, int64_t Arg5)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m148;
    uint64_t v_stack_m308;
    uint64_t v_stack_m398;
    uint64_t v_stack_m3A8;
    uint64_t v_stack_m3C0;
    uint64_t v_stack_m40;
    uint32_t v_stack_m428;
    uint64_t v_stack_m438;
    uint64_t v_stack_m48;
    uint64_t v_stack_m540;
    uint64_t v_stack_m548;
    uint64_t v_stack_m558;
    uint64_t v_stack_m568;
    uint64_t v_stack_m570;
    uint64_t v_stack_m578;
    uint64_t v_stack_m588;
    uint64_t v_stack_m598;
    uint64_t v_stack_m5A8;
    uint64_t v_stack_m5B8;
    uint32_t v_stack_m5C0;
    uint64_t v_stack_m5C8;
    uint64_t v_stack_m5D8;
    uint32_t v_stack_m660;
    uint64_t v_stack_m668;
    uint64_t v_stack_m678;
    uint64_t v_stack_m698;
    uint64_t v_stack_m6A0;
    uint64_t v_stack_m6A8;
    uint64_t v_stack_m6B0;
    uint64_t v_stack_m6B8;
    uint64_t v_stack_m6C0;
    uint64_t v_stack_m6E8;
    uint64_t v_stack_m6F0;
    uint64_t v_stack_m700;
    uint64_t v_stack_m708;
    uint64_t v_stack_m710;
    uint64_t v_stack_m720;
    uint64_t v_stack_m728;
    uint64_t v_stack_m730;
    uint64_t v_stack_m748;
    uint32_t v_stack_m780;
    uint64_t v_stack_m810;
    uint64_t v_stack_m818;
    uint64_t v_stack_m820;
    uint32_t v_stack_m828;
    uint32_t v_stack_m830;
    uint32_t v_stack_m838;
    uint64_t v_stack_m840;
    uint64_t v_stack_m848;
    uint32_t v_stack_m84C;
    uint32_t v_stack_m850;
    uint32_t v_stack_m854;
    uint32_t v_stack_m858;
    uint64_t v_stack_m860;
    uint64_t v_stack_m868;
    uint64_t v_stack_m870;
    uint64_t v_stack_m878;
    uint64_t v_stack_m880;
    uint64_t v_stack_m888;
    uint64_t v_stack_m890;
    uint64_t v_stack_m898;
    uint64_t v_stack_m8A0;
    uint64_t v_stack_m8A8;
    uint64_t v_stack_m8B0;
    uint32_t v_stack_m8B8;
    uint64_t v_stack_m8C0;
    uint64_t v_stack_m8C8;
    uint64_t v_stack_m8D8;
    uint64_t v_stack_m8E0;
    uint64_t v_stack_m8E8;
    uint64_t v_stack_m8F0;
    uint64_t v_stack_m8F8;
    uint64_t v_stack_m900;
    uint32_t v_stack_m904;
    uint64_t v_stack_m908;
    uint64_t v_stack_m910;
    uint32_t v_stack_m918;
    uint32_t v_stack_m91C;
    uint32_t v_stack_m920;
    uint32_t v_stack_m924;
    uint64_t v_stack_m928;
    uint32_t v_stack_m92C;
    uint64_t v_stack_m930;
    uint16_t v_stack_m936;
    uint64_t v_stack_m938;
    uint32_t v_stack_m940;
    uint64_t v_stack_m948;
    uint32_t v_stack_m950;
    uint64_t v_stack_m958;
    uint64_t v_stack_m960;
    uint64_t v_stack_m968;
    uint8_t v_stack_m96F;
    uint16_t v_stack_m970;
    uint64_t v_stack_m978;
    uint64_t v_stack_m9A0;
    uint16_t v_stack_m9A8;
    uint32_t v_stack_m9AC;
    uint16_t v_stack_m9AE;
    uint64_t v_stack_m9B0;
    uint32_t v_stack_m9B8;
    uint8_t v_stack_m9B9;
    uint8_t v_stack_m9BA;
    uint8_t v_stack_m9BB;
    uint8_t v_stack_m9BC;
    uint32_t v_stack_m9C0;
    uint64_t v_stack_m9C8;
    uint64_t v_stack_m9D0;
    uint64_t v_stack_m9D8;
    uint64_t v_stack_m9E0;
    uint32_t v_stack_m9E8;
    uint32_t v_stack_mA08;

    local_rsp = (local_rsp) - (0x9D0ULL);
    result = (*(uint64_t *)(v_rip + 0x4604D6)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m9A0 = Arg1;
    v_stack_m8E0 = Arg3;
    v_stack_m830 = (uint32_t)((uint32_t)(Arg4));
    v_stack_m8D8 = Arg5;
    v_stack_m5A8 = v_xmm0;
    v_stack_m598 = v_xmm0;
    v_stack_m588 = v_xmm0;
    local_rbx = 0;
    v_stack_m9B8 = 0;
    v_stack_m8E8 = 0;
    v_stack_m91C = 0;
    Arg2 = 0;
    result = memset(v_stack_m548, Arg2, 264, Arg4);
    v_stack_m960 = 0;
    v_stack_m5D8 = v_xmm0;
    v_stack_m850 = 0;
    v_stack_m854 = 0;
    Arg2 = 0;
    result = memset(v_stack_m438, Arg2, 152, Arg4);
    v_stack_m700 = v_xmm0;
    v_stack_m848 = 0;
    result = 0;
    v_stack_m578 = v_xmm1;
    v_stack_m568 = v_xmm1;
    v_stack_m558 = 0;
    v_stack_m840 = 0;
    v_stack_m968 = 0;
    v_stack_m9A8 = 0;
    v_stack_m970 = 0;
    v_stack_m9C8 = 0;
    v_stack_m820 = 0;
    v_stack_m910 = 0;
    Arg2 = 0;
    result = memset(v_stack_m6E8, Arg2, local_rbx + 104, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m8C8, Arg2, local_rbx + 112, Arg4);
    v_stack_m9BC = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m948 = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_009AA85F;
    v_stack_m978 = 3;
loc_009AA3F3:
    if (((uint32_t)((int32_t)(Arg2))) != 52) goto loc_009AA525;
    v_stack_m918 = 0;
    v_stack_m9BA = 0;
    v_stack_m9B9 = 0;
    if (((uint32_t)((uint32_t)(Arg4))) != 8) goto loc_009AB5A1;
    v_stack_m858 = (uint32_t)((uint32_t)(*(uint32_t *)(arg3)));
    goto loc_009AA427;
loc_009AA427:
    if (Arg1 == -1) goto loc_009AA9B1;
    v_stack_m9D0 = 0;
    v_stack_m9D8 = 0;
    v_stack_m9E0 = v_stack_m9C8;
    v_stack_m9E8 = 0x79517350ULL;
    result = ObpReferenceObjectByHandleWithTag(Arg1, (uint32_t)(0x1000ULL), *(uint64_t *)(v_rip + 0x61C660), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (sign_flag) goto loc_009AE740;
loc_009AA46D:
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(arg3))) - 1);
    if (((uint32_t)(local_rdi)) > 15) goto loc_009AB047;
    result = ((uint32_t)(*(uint32_t *)(v_rip - 0x9AA482 + (int32_t)((uint32_t)(local_rdi)) * 4 + 0x9AE568))) + (v_rip - 10134658);
loc_009AA506:
    if (Arg1 != -1) {
        Arg2 = 0x79517350ULL;
        Arg1 = v_stack_m9C8;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, *(uint64_t *)(v_rip + 0x61C660), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    }
    goto loc_009AE740;
loc_009AA525:
    if (((uint32_t)(local_rdi)) > 115) goto loc_009AE54E;
    Arg2 = ((uint32_t)(*(uint32_t *)(v_rip - 0x9AA535 + *(uint8_t *)(v_rip - 0x9AA535 + local_rdi * 1 + 0x9AE6CC) * 4 + 0x9AE5A8))) + (v_rip - 10134837);
loc_009AA85F:
    if (((uint32_t)(local_rdi)) == 18) goto loc_009AA938;
    if (((uint32_t)(local_rdi)) == 61) goto loc_009AA938;
    if (((uint32_t)(local_rdi)) == 65) goto loc_009AA98B;
    if ((((uint32_t)(local_rdi - 70)) & (0xFFFFFFFBULL)) == 0) goto loc_009AA938;
    if (((uint32_t)(local_rdi)) == 92) goto loc_009AA96F;
    if (((uint32_t)(local_rdi)) == 94) goto loc_009AA91F;
    if (((uint32_t)(local_rdi)) == 87) goto loc_009AA938;
    if (((uint32_t)(local_rdi)) == 47) goto loc_009AA94F;
    v_stack_m978 = 3;
    result = 3;
    if (((uint32_t)(local_rdi)) == 115) { result = 7; }
loc_009AA8D0:
    if ((uint32_t)((uint32_t)(Arg4)) == 0) goto loc_009AA90E;
    if ((((uint32_t)((uint32_t)(result))) & (Arg3)) != 0) goto loc_009AA91A;
    if ((Arg3 + (uint32_t)(Arg4) * 1) > (*(uint64_t *)(v_rip + 0x61C660))) goto loc_009AA969;
    if ((Arg3 + (uint32_t)(Arg4) * 1) < Arg3) goto loc_009AA969;
loc_009AA8F2:
    if (Arg5 == 0) goto loc_009AA9A7;
    Arg1 = *(uint64_t *)(v_rip + 0x61C660);
    if (Arg5 < (*(uint64_t *)(v_rip + 0x61C660))) { Arg1 = Arg5; }
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    goto loc_009AA9A7;
loc_009AA90E:
    goto loc_009AA8F2;
loc_009AA91A:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, *(uint64_t *)(v_rip + 0x61C660), 1);
loc_009AA91F:
    v_stack_m978 = 3;
    goto loc_009AA8D0;
loc_009AA938:
    v_stack_m978 = 3;
    goto loc_009AA8D0;
loc_009AA94F:
    v_stack_m978 = 3;
    goto loc_009AA8D0;
loc_009AA969:
    goto loc_009AA8F2;
loc_009AA96F:
    v_stack_m978 = 3;
    goto loc_009AA8D0;
loc_009AA98B:
    v_stack_m978 = 3;
    goto loc_009AA8D0;
loc_009AA9A7:
    goto loc_009AA3F3;
loc_009AA9B1:
    v_stack_m9C8 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    goto loc_009AA46D;
loc_009AB047:
    v_stack_m9C0 = 0xC00000BBULL;
    goto loc_009AA506;
loc_009AB5A1:
    goto loc_009AE740;
loc_009AE54E:
    goto loc_009AE740;
loc_009AE740:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, *(uint64_t *)(v_rip + 0x61C660), 1);
    local_rsp = (local_rsp) + (0x9D0ULL);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `32` | `R` |
| `Arg3` | `+ 0x0 + r14*1` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009AA250&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
