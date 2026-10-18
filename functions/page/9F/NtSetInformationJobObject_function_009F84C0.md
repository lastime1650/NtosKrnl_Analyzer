# NtSetInformationJobObject

- RVA: `0x009F84C0`–`0x009FB06C` (길이 `11,180` bytes)
- VA: `0x00000001409F84C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A6E38`
- 디코드: `2,390`개 명령, `11,180/11,180` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **166**; 고유 호출 대상: **78**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **24**

### Outgoing calls
- `0x009F8516` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009F854B` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009F8580` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009F85C4` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009F86D1` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009F8776` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009F882C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009F8895` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x009F88A2` → [PspLockJobMemoryLimitsExclusive](../91/PspLockJobMemoryLimitsExclusive_function_00916990.md) (function, `0x00916990`)
- `0x009F88BD` → [PspUnlockJobMemoryLimitsExclusive](../87/PspUnlockJobMemoryLimitsExclusive_function_0087D390.md) (function, `0x0087D390`)
- `0x009F88C6` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x009F88DC` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009F8914` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x009F8937` → [IoAllocateMiniCompletionPacket](../9A/IoAllocateMiniCompletionPacket_function_009A81E0.md) (function, `0x009A81E0`)
- `0x009F8961` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x009F89AB` → [PspLockJobMemoryLimitsExclusive](../91/PspLockJobMemoryLimitsExclusive_function_00916990.md) (function, `0x00916990`)
- `0x009F89DD` → [PspUnlockJobMemoryLimitsExclusive](../87/PspUnlockJobMemoryLimitsExclusive_function_0087D390.md) (function, `0x0087D390`)
- `0x009F8A06` → [PspEnumJobsAndProcessesInJobHierarchy](../91/PspEnumJobsAndProcessesInJobHierarchy_function_0091A1EC.md) (function, `0x0091A1EC`)
- `0x009F8A0F` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x009F8A1A` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x009F8A2C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009F8A61` → [IopFreeMiniCompletionPacket](../9A/IopFreeMiniCompletionPacket_function_009A82D0.md) (function, `0x009A82D0`)
- `0x009F8A91` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x009F8AA1` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x009F8B45` → [PspSetUILimitJobObject](../6F/PspSetUILimitJobObject_function_006FD218.md) (function, `0x006FD218`)
- `0x009F8B74` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009F8B97` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009F8BA7` → [PspGetJobLimitInformationValidFlags](PspGetJobLimitInformationValidFlags_function_009FB458.md) (function, `0x009FB458`)
- `0x009F8BE0` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009F8C7A` → [SeCheckPrivilegedObject](SeCheckPrivilegedObject_function_009F62CC.md) (function, `0x009F62CC`)
- `0x009F8CE6` → [SeCheckPrivilegedObject](SeCheckPrivilegedObject_function_009F62CC.md) (function, `0x009F62CC`)
- `0x009F8DCD` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x009F8EC7` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009F8F1E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009F8F51` → [PsChargeSharedPoolQuota](../99/PsChargeSharedPoolQuota_function_0099E340.md) (function, `0x0099E340`)
- `0x009F8F6B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009F8FA5` → [SeCaptureSubjectContextEx](../8C/SeCaptureSubjectContextEx_function_008C4C90.md) (function, `0x008C4C90`)
- `0x009F8FFB` → [SePrivilegeCheck](../9B/SePrivilegeCheck_function_009BAE70.md) (function, `0x009BAE70`)
- `0x009F902D` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x009F90B9` → [KeFirstGroupAffinityEx](../../text/46/KeFirstGroupAffinityEx_function_00463810.md) (function, `0x00463810`)
- `0x009F90D1` → [KeQueryPrimaryGroupThread](../../text/49/KeQueryPrimaryGroupThread_function_004903B4.md) (function, `0x004903B4`)
- `0x009F9126` → [KeAddGroupAffinityEx](../../text/25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x009F9151` → [PspEnumJobsAndProcessesInJobHierarchy](../91/PspEnumJobsAndProcessesInJobHierarchy_function_0091A1EC.md) (function, `0x0091A1EC`)
- `0x009F9233` → [ExfAcquireReleasePushLockExclusive](../../text/41/ExfAcquireReleasePushLockExclusive_function_00419C2C.md) (function, `0x00419C2C`)
- `0x009F9355` → [PspLockJobMemoryLimitsExclusive](../91/PspLockJobMemoryLimitsExclusive_function_00916990.md) (function, `0x00916990`)
- `0x009F93BA` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x009F93C6` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009F9429` → [PspEnumJobsAndProcessesInJobHierarchy](../91/PspEnumJobsAndProcessesInJobHierarchy_function_0091A1EC.md) (function, `0x0091A1EC`)
- `0x009F943F` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x009F949A` → [PspEnumJobsAndProcessesInJobHierarchy](../91/PspEnumJobsAndProcessesInJobHierarchy_function_0091A1EC.md) (function, `0x0091A1EC`)
- `0x009F94B4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x009F94D9` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x009F951A` → [PspAddProcessToWorkingSetChangeList](../78/PspAddProcessToWorkingSetChangeList_function_00784B38.md) (function, `0x00784B38`)
- `0x009F952C` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x009F9539` → [PspApplyWorkingSetLimits](../78/PspApplyWorkingSetLimits_function_00784C00.md) (function, `0x00784C00`)
- `0x009F954E` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x009F9569` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009F960A` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009F960F` → [KeQueryActiveGroupCount](../../text/48/KeQueryActiveGroupCount_function_0048C600.md) (function, `0x0048C600`)
- `0x009F96C4` → [KeAddGroupAffinityEx](../../text/25/KeAddGroupAffinityEx_function_0025B6C0.md) (function, `0x0025B6C0`)
- `0x009F9769` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009F9791` → [PsChargeSharedPoolQuota](../99/PsChargeSharedPoolQuota_function_0099E340.md) (function, `0x0099E340`)
- `0x009F97C7` → [SeCaptureSubjectContextEx](../8C/SeCaptureSubjectContextEx_function_008C4C90.md) (function, `0x008C4C90`)
- `0x009F981D` → [SePrivilegeCheck](../9B/SePrivilegeCheck_function_009BAE70.md) (function, `0x009BAE70`)
- `0x009F984C` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x009F9872` → [PspEnumJobsAndProcessesInJobHierarchy](../91/PspEnumJobsAndProcessesInJobHierarchy_function_0091A1EC.md) (function, `0x0091A1EC`)
- `0x009F999B` → [KeIsEmptyAffinityEx](../../text/2D/KeIsEmptyAffinityEx_function_002D1580.md) (function, `0x002D1580`)
- `0x009F99F4` → [PspEnumJobsAndProcessesInJobHierarchy](../91/PspEnumJobsAndProcessesInJobHierarchy_function_0091A1EC.md) (function, `0x0091A1EC`)
- `0x009F9A01` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x009F9A16` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x009F9A2C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009F9A41` → [PsReturnSharedPoolQuota](../8B/PsReturnSharedPoolQuota_function_008BCC30.md) (function, `0x008BCC30`)
- `0x009F9AA8` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x009F9AE9` → [KeInitializeDpc](../../text/45/KeInitializeDpc_function_0045BBD0.md) (function, `0x0045BBD0`)
- `0x009F9AFC` → [KeSetSchedulingGroupCycleNotification](../../text/5C/KeSetSchedulingGroupCycleNotification_function_005C8C24.md) (function, `0x005C8C24`)
- `0x009F9B66` → [PspEnumJobsAndProcessesInJobHierarchy](../91/PspEnumJobsAndProcessesInJobHierarchy_function_0091A1EC.md) (function, `0x0091A1EC`)
- `0x009F9BA5` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x009F9C15` → [KeSetSchedulingGroupRankBias](../../text/46/KeSetSchedulingGroupRankBias_function_0046DB74.md) (function, `0x0046DB74`)
- `0x009F9C38` → [PspEnumJobsAndProcessesInJobHierarchy](../91/PspEnumJobsAndProcessesInJobHierarchy_function_0091A1EC.md) (function, `0x0091A1EC`)
- `0x009F9C76` → [PspSetBackgroundJobTree](../A6/PspSetBackgroundJobTree_function_00A6FCF0.md) (function, `0x00A6FCF0`)
- `0x009F9CFA` → [PspFreezeJobTree](PspFreezeJobTree_function_009FB074.md) (function, `0x009FB074`)
- `0x009F9D75` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x009F9D82` → [PspLockJobMemoryLimitsExclusive](../91/PspLockJobMemoryLimitsExclusive_function_00916990.md) (function, `0x00916990`)
- `0x009F9D96` → [PspUnlockJobMemoryLimitsExclusive](../87/PspUnlockJobMemoryLimitsExclusive_function_0087D390.md) (function, `0x0087D390`)
- `0x009F9DC5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009F9E81` → [PspLockJobChain](../87/PspLockJobChain_function_0087DAD0.md) (function, `0x0087DAD0`)
- `0x009F9EA0` → [PspAllocateRateControl](../99/PspAllocateRateControl_function_0099E208.md) (function, `0x0099E208`)
- `0x009F9F9C` → [PspAddSchedulingGroupToJobChain](../99/PspAddSchedulingGroupToJobChain_function_0099DE5C.md) (function, `0x0099DE5C`)
- `0x009F9FCD` → [PspFreeRateControl](../99/PspFreeRateControl_function_0099E1BC.md) (function, `0x0099E1BC`)
- `0x009F9FFD` → [KeSetSchedulingGroupWeights](../../text/46/KeSetSchedulingGroupWeights_function_0046D024.md) (function, `0x0046D024`)
- `0x009FA004` → [KeSetSchedulingGroupCpuRates](../../text/46/KeSetSchedulingGroupCpuRates_function_0046DE5C.md) (function, `0x0046DE5C`)
- `0x009FA07C` → [KeQuerySchedulingGroupReadyTime](../../text/47/KeQuerySchedulingGroupReadyTime_function_0047A9E4.md) (function, `0x0047A9E4`)
- `0x009FA095` → [KeSetSchedulingGroupCpuRates](../../text/46/KeSetSchedulingGroupCpuRates_function_0046DE5C.md) (function, `0x0046DE5C`)
- `0x009FA0CB` → [PspEnumJobsAndProcessesInJobHierarchy](../91/PspEnumJobsAndProcessesInJobHierarchy_function_0091A1EC.md) (function, `0x0091A1EC`)
- `0x009FA0FD` → [EtwTraceJobSetQuery](EtwTraceJobSetQuery_function_009FB480.md) (function, `0x009FB480`)
- `0x009FA10D` → [PspUnlockJobChain](../87/PspUnlockJobChain_function_0087DC78.md) (function, `0x0087DC78`)
- `0x009FA140` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x009FA148` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x009FA151` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x009FA1C9` → [PspJobIsAppSilo](../../text/5E/PspJobIsAppSilo_function_005E2740.md) (function, `0x005E2740`)
- `0x009FA1EE` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x009FA21E` → [PspHardDereferenceSiloWorker](../../text/38/PspHardDereferenceSiloWorker_function_0038F740.md) (function, `0x0038F740`)
- `0x009FA252` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x009FA279` → [PspSetJobSiloThreadImpersonationPolicy](../78/PspSetJobSiloThreadImpersonationPolicy_function_007858B8.md) (function, `0x007858B8`)
- `0x009FA2A3` → [PspConvertSiloToServerSilo](../77/PspConvertSiloToServerSilo_function_0077F9B4.md) (function, `0x0077F9B4`)
- `0x009FA2CF` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x009FA306` → [PspSetJobSiloThreadImpersonationPolicy](../78/PspSetJobSiloThreadImpersonationPolicy_function_007858B8.md) (function, `0x007858B8`)
- `0x009FA327` → [ObCreateSiloRootDirectory](../83/ObCreateSiloRootDirectory_function_0083CA34.md) (function, `0x0083CA34`)
- `0x009FA350` → [PspCreateSilo](../A8/PspCreateSilo_function_00A89CFC.md) (function, `0x00A89CFC`)
- `0x009FA362` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009FA3F9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009FA51A` → [PspNotificationLimitRateControlToleranceField](../A7/PspNotificationLimitRateControlToleranceField_function_00A71D24.md) (function, `0x00A71D24`)
- `0x009FA52A` → [PspNotificationLimitRateControlToleranceIntervalField](../A7/PspNotificationLimitRateControlToleranceIntervalField_function_00A7015C.md) (function, `0x00A7015C`)
- `0x009FA534` → [PspRateControlLimitFlag](../91/PspRateControlLimitFlag_function_0091A3FC.md) (function, `0x0091A3FC`)
- `0x009FA5A3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009FA5D0` → [PsChargeSharedPoolQuota](../99/PsChargeSharedPoolQuota_function_0099E340.md) (function, `0x0099E340`)
- `0x009FA5E5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009FA5F9` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009FA612` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x009FA63D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009FA64B` → [PsReturnSharedPoolQuota](../8B/PsReturnSharedPoolQuota_function_008BCC30.md) (function, `0x008BCC30`)
- `0x009FA6EB` → [PspLockJobMemoryLimitsExclusive](../91/PspLockJobMemoryLimitsExclusive_function_00916990.md) (function, `0x00916990`)
- `0x009FA73A` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x009FA746` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009FA7A9` → [PspEnumJobsAndProcessesInJobHierarchy](../91/PspEnumJobsAndProcessesInJobHierarchy_function_0091A1EC.md) (function, `0x0091A1EC`)
- `0x009FA7DC` → [EtwTraceJobSetQuery](EtwTraceJobSetQuery_function_009FB480.md) (function, `0x009FB480`)
- `0x009FA7E5` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x009FA7EF` → [PspLockJobMemoryLimitsShared](../91/PspLockJobMemoryLimitsShared_function_0091A394.md) (function, `0x0091A394`)
- `0x009FA813` → [PspGetJobMemoryUsageNotificationViolations](PspGetJobMemoryUsageNotificationViolations_function_009FE2B4.md) (function, `0x009FE2B4`)
- `0x009FA830` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x009FA838` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x009FA84D` → [PspScheduleEnforcementWorker](../A6/PspScheduleEnforcementWorker_function_00A60158.md) (function, `0x00A60158`)
- `0x009FA87F` → [PspSetNetRateControl](../78/PspSetNetRateControl_function_00785944.md) (function, `0x00785944`)
- `0x009FA8A2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009FA8D4` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009FA935` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009FA976` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009FA9E9` → [EtwpCoverageUserIsAdmin](EtwpCoverageUserIsAdmin_function_009FE548.md) (function, `0x009FE548`)
- `0x009FAA09` → [PspSetJobIoRateControl](PspSetJobIoRateControl_function_009F78EC.md) (function, `0x009F78EC`)
- `0x009FAA43` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009FAA5A` → [PspLockJobMemoryLimitsExclusive](../91/PspLockJobMemoryLimitsExclusive_function_00916990.md) (function, `0x00916990`)
- `0x009FAA75` → [PspUnlockJobMemoryLimitsExclusive](../87/PspUnlockJobMemoryLimitsExclusive_function_0087D390.md) (function, `0x0087D390`)
- `0x009FAB19` → [PspLockRootJobExclusive](../91/PspLockRootJobExclusive_function_00917D0C.md) (function, `0x00917D0C`)
- `0x009FAB3E` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x009FAB4F` → [PspSetJobIoAttribution](PspSetJobIoAttribution_function_009F7C50.md) (function, `0x009F7C50`)
- `0x009FAB77` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x009FAB8C` → [PspUnlockJob](../91/PspUnlockJob_function_00919E00.md) (function, `0x00919E00`)
- `0x009FABC8` → [PspUnlockJobConditionally](../A4/PspUnlockJobConditionally_function_00A454A4.md) (function, `0x00A454A4`)
- `0x009FABDD` → [PspUnlockJob](../91/PspUnlockJob_function_00919E00.md) (function, `0x00919E00`)
- `0x009FAC71` → [PspSetPagePriorityLimitJobTree](../78/PspSetPagePriorityLimitJobTree_function_00785C10.md) (function, `0x00785C10`)
- `0x009FACCD` → [PspSetIoPriorityLimitJobTree](../78/PspSetIoPriorityLimitJobTree_function_007854C4.md) (function, `0x007854C4`)
- `0x009FAD1E` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x009FAD55` → [PspSetJobSiloThreadImpersonationPolicy](../78/PspSetJobSiloThreadImpersonationPolicy_function_007858B8.md) (function, `0x007858B8`)
- `0x009FAD9F` → [PspSetEnergyTrackingStateJobTree](PspSetEnergyTrackingStateJobTree_function_009FE5AC.md) (function, `0x009FE5AC`)
- `0x009FAE36` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x009FAE7C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x009FAEAD` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009FAEBF` → [wcsnlen](../../text/50/wcsnlen_function_00501D60.md) (function, `0x00501D60`)
- `0x009FAEE8` → [PspAssignSiloSystemRootPath](../77/PspAssignSiloSystemRootPath_function_0077F720.md) (function, `0x0077F720`)
- `0x009FAF4A` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x009FAF91` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x009FAFBB` → [PspSetJobMemoryPartition](../78/PspSetJobMemoryPartition_function_00785574.md) (function, `0x00785574`)
- `0x009FB001` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x009FB02D` → [EtwTraceJobSetQuery](EtwTraceJobSetQuery_function_009FB480.md) (function, `0x009FB480`)
- `0x009FB03A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x009FB053` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x009F84D3` → RVA `0x00E0A740` (`.data`; read)
- `0x009F8655` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x009F873D` → RVA `0x00FC6C58` (`ALMOSTRO`; read)
- `0x009F88E6` → RVA `0x00FC6CC0` (`ALMOSTRO`; read)
- `0x009F8930` → RVA `0x00A67B30` (`PspNotificationPacketCallback`; read)
- `0x009F89F7` → RVA `0x00A83290` (`PspAssociateCompletionPortCallback`; read)
- `0x009F8C73` → RVA `0x00FD9AE8` (`PAGEDATA`; read)
- `0x009F8DB9` → RVA `0x00FD8240` (`PAGEDATA`; read)
- `0x009F8FD1` → RVA `0x00FD9A80` (`PAGEDATA`; read)
- `0x009F913D` → RVA `0x00785460` (`PspSetAffinityLimitCallback`; read)
- `0x009F9220` → RVA `0x00FC70B0` (`ALMOSTRO`; read)
- `0x009F941A` → RVA `0x00785900` (`PspSetJobTimeLimitCallback`; read)
- `0x009F944F` → RVA `0x00F065E0` (`.data`; read/write)
- `0x009F9482` → RVA `0x00A57220` (`PspSetJobLimitsProcessCallback`; read)
- `0x009F9489` → RVA `0x00A802D0` (`PspSetJobLimitsJobPostCallback`; read)
- `0x009F9490` → RVA `0x0087E6C0` (`PspSetJobLimitsJobPreCallback`; read)
- `0x009F94BC` → RVA `0x00FC70B0` (`ALMOSTRO`; read/write)
- `0x009F9ADE` → RVA `0x005E3980` (`PspJobCycleTimeNotificationDpcRoutine`; read)
- `0x009F9B4E` → RVA `0x00A9D870` (`PspEnableProcessTimerVirtualization`; read)
- `0x009F9B55` → RVA `0x00AA37D0` (`PspEnableTimerVirtualization`; read)
- `0x009F9C29` → RVA `0x004A7C60` (`PspSetProcessCacheIsolationCallback`; read)
- `0x009FA0D3` → RVA `0x00FC6B00` (`ALMOSTRO`; read)
- `0x009FA24B` → RVA `0x00FD9A78` (`PAGEDATA`; read)
- `0x009FA79F` → RVA `0x00A9D520` (`PspSetJobNotificationCountCallback`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **83**
  - `0x009F8516` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009F854B` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009F8580` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009F85C4` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009F882C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009F8895` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x009F88C6` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x009F88DC` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009F8961` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x009F8A0F` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x009F8A1A` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x009F8A2C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009F8A91` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x009F8AA1` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x009F8B74` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009F8B97` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009F8BE0` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009F8EC7` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009F8F1E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009F8F6B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009F902D` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x009F90B9` → [KeFirstGroupAffinityEx](../../text/46/KeFirstGroupAffinityEx_function_00463810.md) (`PAGE` → `.text`)
  - `0x009F90D1` → [KeQueryPrimaryGroupThread](../../text/49/KeQueryPrimaryGroupThread_function_004903B4.md) (`PAGE` → `.text`)
  - `0x009F9126` → [KeAddGroupAffinityEx](../../text/25/KeAddGroupAffinityEx_function_0025B6C0.md) (`PAGE` → `.text`)
  - `0x009F9233` → [ExfAcquireReleasePushLockExclusive](../../text/41/ExfAcquireReleasePushLockExclusive_function_00419C2C.md) (`PAGE` → `.text`)
  - `0x009F93BA` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x009F93C6` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009F943F` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (`PAGE` → `.text`)
  - `0x009F94B4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x009F94D9` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x009F952C` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x009F9569` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009F960A` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009F960F` → [KeQueryActiveGroupCount](../../text/48/KeQueryActiveGroupCount_function_0048C600.md) (`PAGE` → `.text`)
  - `0x009F96C4` → [KeAddGroupAffinityEx](../../text/25/KeAddGroupAffinityEx_function_0025B6C0.md) (`PAGE` → `.text`)
  - `0x009F9769` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009F984C` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x009F999B` → [KeIsEmptyAffinityEx](../../text/2D/KeIsEmptyAffinityEx_function_002D1580.md) (`PAGE` → `.text`)
  - `0x009F9A01` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x009F9A2C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009F9AA8` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x009F9AE9` → [KeInitializeDpc](../../text/45/KeInitializeDpc_function_0045BBD0.md) (`PAGE` → `.text`)
  - `0x009F9AFC` → [KeSetSchedulingGroupCycleNotification](../../text/5C/KeSetSchedulingGroupCycleNotification_function_005C8C24.md) (`PAGE` → `.text`)
  - `0x009F9BA5` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x009F9C15` → [KeSetSchedulingGroupRankBias](../../text/46/KeSetSchedulingGroupRankBias_function_0046DB74.md) (`PAGE` → `.text`)
  - `0x009F9D75` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x009F9DC5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009F9FFD` → [KeSetSchedulingGroupWeights](../../text/46/KeSetSchedulingGroupWeights_function_0046D024.md) (`PAGE` → `.text`)
  - `0x009FA004` → [KeSetSchedulingGroupCpuRates](../../text/46/KeSetSchedulingGroupCpuRates_function_0046DE5C.md) (`PAGE` → `.text`)
  - `0x009FA07C` → [KeQuerySchedulingGroupReadyTime](../../text/47/KeQuerySchedulingGroupReadyTime_function_0047A9E4.md) (`PAGE` → `.text`)
  - `0x009FA095` → [KeSetSchedulingGroupCpuRates](../../text/46/KeSetSchedulingGroupCpuRates_function_0046DE5C.md) (`PAGE` → `.text`)
  - `0x009FA140` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x009FA148` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (`PAGE` → `.text`)
  - `0x009FA151` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x009FA1C9` → [PspJobIsAppSilo](../../text/5E/PspJobIsAppSilo_function_005E2740.md) (`PAGE` → `.text`)
  - `0x009FA1EE` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x009FA21E` → [PspHardDereferenceSiloWorker](../../text/38/PspHardDereferenceSiloWorker_function_0038F740.md) (`PAGE` → `.text`)
  - `0x009FA362` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009FA3F9` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009FA5A3` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009FA5E5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009FA5F9` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009FA612` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x009FA63D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009FA73A` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x009FA746` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009FA7E5` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x009FA830` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x009FA838` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x009FA8A2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009FA935` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009FA976` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009FAA43` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009FAB3E` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x009FAB77` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x009FAE7C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x009FAEAD` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x009FAEBF` → [wcsnlen](../../text/50/wcsnlen_function_00501D60.md) (`PAGE` → `.text`)
  - `0x009FAF4A` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x009FAF91` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x009FB001` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x009FB03A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x009FB053` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009F84C0  40 53                           push rbx
009F84C2  56                              push rsi
009F84C3  57                              push rdi
009F84C4  41 54                           push r12
009F84C6  41 55                           push r13
009F84C8  41 56                           push r14
009F84CA  41 57                           push r15
009F84CC  48 81 EC 60 0C 00 00            sub rsp, 0xc60
009F84D3  48 8B 05 66 22 41 00            mov rax, qword ptr [rip + 0x412266]
009F84DA  48 33 C4                        xor rax, rsp
009F84DD  48 89 84 24 50 0C 00 00         mov qword ptr [rsp + 0xc50], rax
009F84E5  45 8B E1                        mov r12d, r9d
009F84E8  48 63 DA                        movsxd rbx, edx
009F84EB  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
009F84EF  48 8B F9                        mov rdi, rcx
009F84F2  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
009F84FA  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
009F84FE  4C 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r8
009F8506  33 D2                           xor edx, edx
009F8508  41 B8 00 01 00 00               mov r8d, 0x100
009F850E  48 8D 8C 24 18 04 00 00         lea rcx, [rsp + 0x418]
009F8516  E8 25 E7 CC FF                  call 0x1406c6c40
009F851B  45 33 FF                        xor r15d, r15d
009F851E  4C 89 BC 24 18 01 00 00         mov qword ptr [rsp + 0x118], r15
009F8526  4C 89 BC 24 28 01 00 00         mov qword ptr [rsp + 0x128], r15
009F852E  44 88 7C 24 5C                  mov byte ptr [rsp + 0x5c], r15b
009F8533  4C 89 BC 24 48 01 00 00         mov qword ptr [rsp + 0x148], r15
009F853B  33 D2                           xor edx, edx
009F853D  41 B8 98 00 00 00               mov r8d, 0x98
009F8543  48 8D 8C 24 70 03 00 00         lea rcx, [rsp + 0x370]
009F854B  E8 F0 E6 CC FF                  call 0x1406c6c40
009F8550  0F 57 C0                        xorps xmm0, xmm0
009F8553  0F 11 84 24 F8 02 00 00         movups xmmword ptr [rsp + 0x2f8], xmm0
009F855B  0F 57 C9                        xorps xmm1, xmm1
009F855E  0F 11 8C 24 38 01 00 00         movups xmmword ptr [rsp + 0x138], xmm1
009F8566  4C 89 BC 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r15
009F856E  BE 90 00 00 00                  mov esi, 0x90
009F8573  44 8B C6                        mov r8d, esi
009F8576  33 D2                           xor edx, edx
009F8578  48 8D 8C 24 00 02 00 00         lea rcx, [rsp + 0x200]
009F8580  E8 BB E6 CC FF                  call 0x1406c6c40
009F8585  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
009F858A  0F 57 C0                        xorps xmm0, xmm0
009F858D  0F 11 84 24 68 01 00 00         movups xmmword ptr [rsp + 0x168], xmm0
009F8595  0F 11 84 24 78 01 00 00         movups xmmword ptr [rsp + 0x178], xmm0
009F859D  33 C0                           xor eax, eax
009F859F  0F 11 84 24 D8 00 00 00         movups xmmword ptr [rsp + 0xd8], xmm0
009F85A7  0F 11 84 24 E8 00 00 00         movups xmmword ptr [rsp + 0xe8], xmm0
009F85AF  89 84 24 F8 00 00 00            mov dword ptr [rsp + 0xf8], eax
009F85B6  33 D2                           xor edx, edx
009F85B8  45 8D 47 48                     lea r8d, [r15 + 0x48]
009F85BC  48 8D 8C 24 90 02 00 00         lea rcx, [rsp + 0x290]
009F85C4  E8 77 E6 CC FF                  call 0x1406c6c40
009F85C9  0F 57 C0                        xorps xmm0, xmm0
009F85CC  0F 11 84 24 40 03 00 00         movups xmmword ptr [rsp + 0x340], xmm0
009F85D4  0F 11 84 24 50 03 00 00         movups xmmword ptr [rsp + 0x350], xmm0
009F85DC  0F 11 84 24 60 03 00 00         movups xmmword ptr [rsp + 0x360], xmm0
009F85E4  0F 57 C9                        xorps xmm1, xmm1
009F85E7  33 C0                           xor eax, eax
009F85E9  0F 11 8C 24 08 03 00 00         movups xmmword ptr [rsp + 0x308], xmm1
009F85F1  0F 11 8C 24 18 03 00 00         movups xmmword ptr [rsp + 0x318], xmm1
009F85F9  0F 11 8C 24 28 03 00 00         movups xmmword ptr [rsp + 0x328], xmm1
009F8601  48 89 84 24 38 03 00 00         mov qword ptr [rsp + 0x338], rax
009F8609  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
009F860E  44 88 7C 24 5D                  mov byte ptr [rsp + 0x5d], r15b
009F8613  0F 11 84 24 E0 02 00 00         movups xmmword ptr [rsp + 0x2e0], xmm0
009F861B  89 84 24 F0 02 00 00            mov dword ptr [rsp + 0x2f0], eax
009F8622  4C 89 BC 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r15
009F862A  0F 11 84 24 00 01 00 00         movups xmmword ptr [rsp + 0x100], xmm0
009F8632  8D 43 FF                        lea eax, [rbx - 1]
009F8635  83 F8 32                        cmp eax, 0x32
009F8638  0F 87 05 2A 00 00               ja 0x1409fb043
009F863E  83 FB 09                        cmp ebx, 9
009F8641  0F 84 9C 00 00 00               je 0x1409f86e3
009F8647  83 FB 0C                        cmp ebx, 0xc
009F864A  0F 84 87 00 00 00               je 0x1409f86d7
009F8650  83 FB 1F                        cmp ebx, 0x1f
009F8653  74 24                           je 0x1409f8679
009F8655  48 8D 15 A4 79 60 FF            lea rdx, [rip - 0x9f865c]
009F865C  8B 8C 9A 2C E5 B4 00            mov ecx, dword ptr [rdx + rbx*4 + 0xb4e52c]
009F8663  44 3B E1                        cmp r12d, ecx
009F8666  74 2A                           je 0x1409f8692
009F8668  83 FB 0B                        cmp ebx, 0xb
009F866B  74 05                           je 0x1409f8672
009F866D  83 FB 0E                        cmp ebx, 0xe
009F8670  75 7D                           jne 0x1409f86ef
009F8672  44 3B E1                        cmp r12d, ecx
009F8675  73 1B                           jae 0x1409f8692
009F8677  EB 76                           jmp 0x1409f86ef
009F8679  41 8B C4                        mov eax, r12d
009F867C  83 E8 30                        sub eax, 0x30
009F867F  74 0A                           je 0x1409f868b
009F8681  83 E8 30                        sub eax, 0x30
009F8684  74 05                           je 0x1409f868b
009F8686  83 F8 30                        cmp eax, 0x30
009F8689  75 64                           jne 0x1409f86ef
009F868B  48 8D 15 6E 79 60 FF            lea rdx, [rip - 0x9f8692]
009F8692  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
009F869B  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
009F86A3  8A 81 32 02 00 00               mov al, byte ptr [rcx + 0x232]
009F86A9  88 44 24 48                     mov byte ptr [rsp + 0x48], al
009F86AD  88 44 24 68                     mov byte ptr [rsp + 0x68], al
009F86B1  84 C0                           test al, al
009F86B3  74 71                           je 0x1409f8726
009F86B5  8B 84 9A FC E5 B4 00            mov eax, dword ptr [rdx + rbx*4 + 0xb4e5fc]
009F86BC  4C 8B AC 24 C8 00 00 00         mov r13, qword ptr [rsp + 0xc8]
009F86C4  45 85 E4                        test r12d, r12d
009F86C7  74 52                           je 0x1409f871b
009F86C9  8D 48 FF                        lea ecx, [rax - 1]
009F86CC  49 85 CD                        test r13, rcx
009F86CF  74 28                           je 0x1409f86f9
009F86D1  E8 FA 18 EA FF                  call 0x140899fd0
009F86D6  90                              nop
009F86D7  41 83 FC 30                     cmp r12d, 0x30
009F86DB  74 AE                           je 0x1409f868b
009F86DD  41 83 FC 38                     cmp r12d, 0x38
009F86E1  EB A6                           jmp 0x1409f8689
009F86E3  41 8B C4                        mov eax, r12d
009F86E6  2B C6                           sub eax, esi
009F86E8  74 A1                           je 0x1409f868b
009F86EA  83 F8 08                        cmp eax, 8
009F86ED  74 9C                           je 0x1409f868b
009F86EF  B8 04 00 00 C0                  mov eax, 0xc0000004
009F86F4  E9 4F 29 00 00                  jmp 0x1409fb048
009F86F9  4B 8D 0C 2C                     lea rcx, [r12 + r13]
009F86FD  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
009F8707  48 3B C8                        cmp rcx, rax
009F870A  77 05                           ja 0x1409f8711
009F870C  49 3B CD                        cmp rcx, r13
009F870F  73 0A                           jae 0x1409f871b
009F8711  8A 00                           mov al, byte ptr [rax]
009F8713  4C 8B AC 24 C8 00 00 00         mov r13, qword ptr [rsp + 0xc8]
009F871B  8A 44 24 48                     mov al, byte ptr [rsp + 0x48]
009F871F  EB 0D                           jmp 0x1409f872e
009F8721  E9 22 29 00 00                  jmp 0x1409fb048
009F8726  4C 8B AC 24 C8 00 00 00         mov r13, qword ptr [rsp + 0xc8]
009F872E  48 85 FF                        test rdi, rdi
009F8731  75 0A                           jne 0x1409f873d
009F8733  B8 08 00 00 C0                  mov eax, 0xc0000008
009F8738  E9 0B 29 00 00                  jmp 0x1409fb048
009F873D  4C 8B 05 14 E5 5C 00            mov r8, qword ptr [rip + 0x5ce514]
009F8744  BA 10 00 00 00                  mov edx, 0x10
009F8749  44 8D 72 F2                     lea r14d, [rdx - 0xe]
009F874D  83 FB 05                        cmp ebx, 5
009F8750  41 0F 45 D6                     cmovne edx, r14d
009F8754  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
009F8759  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
009F875E  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
009F8763  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
009F8768  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
009F8770  44 8A C8                        mov r9b, al
009F8773  48 8B CF                        mov rcx, rdi
009F8776  E8 D5 0E E7 FF                  call 0x140869650
009F877B  85 C0                           test eax, eax
009F877D  0F 88 C5 28 00 00               js 0x1409fb048
009F8783  41 8B F7                        mov esi, r15d
009F8786  44 89 7C 24 58                  mov dword ptr [rsp + 0x58], r15d
009F878B  41 8A DF                        mov bl, r15b
009F878E  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
009F8796  48 83 CF FF                     or rdi, 0xffffffffffffffff
009F879A  66 01 B8 E6 01 00 00            add word ptr [rax + 0x1e6], di
009F87A1  90                              nop
009F87A2  8B 4C 24 50                     mov ecx, dword ptr [rsp + 0x50]
009F87A6  83 F9 19                        cmp ecx, 0x19
009F87A9  0F 8F AF 19 00 00               jg 0x1409fa15e
009F87AF  0F 84 79 19 00 00               je 0x1409fa12e
009F87B5  83 F9 0E                        cmp ecx, 0xe
009F87B8  0F 8F 8D 12 00 00               jg 0x1409f9a4b
009F87BE  0F 84 CE 0D 00 00               je 0x1409f9592
009F87C4  8B D1                           mov edx, ecx
009F87C6  41 2B D6                        sub edx, r14d
009F87C9  0F 84 97 03 00 00               je 0x1409f8b66
009F87CF  41 2B D6                        sub edx, r14d
009F87D2  0F 84 4E 03 00 00               je 0x1409f8b26
009F87D8  83 EA 01                        sub edx, 1
009F87DB  0F 84 E1 02 00 00               je 0x1409f8ac2
009F87E1  83 EA 01                        sub edx, 1
009F87E4  0F 84 81 02 00 00               je 0x1409f8a6b
009F87EA  83 EA 01                        sub edx, 1
009F87ED  74 78                           je 0x1409f8867
009F87EF  41 2B D6                        sub edx, r14d
009F87F2  0F 84 6E 03 00 00               je 0x1409f8b66
009F87F8  41 2B D6                        sub edx, r14d
009F87FB  0F 84 91 0D 00 00               je 0x1409f9592
009F8801  83 FA 01                        cmp edx, 1
009F8804  0F 85 14 24 00 00               jne 0x1409fac1e
009F880A  4D 8B C4                        mov r8, r12
009F880D  49 8B D5                        mov rdx, r13
009F8810  41 83 FC 30                     cmp r12d, 0x30
009F8814  0F 84 D7 1B 00 00               je 0x1409fa3f1
009F881A  41 83 FC 38                     cmp r12d, 0x38
009F881E  0F 84 36 1B 00 00               je 0x1409fa35a
009F8824  48 8D 8C 24 90 02 00 00         lea rcx, [rsp + 0x290]
009F882C  E8 0F E0 CC FF                  call 0x1406c6840
009F8831  B8 04 82 1F 00                  mov eax, 0x1f8204
009F8836  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
009F883A  44 8B 84 24 B8 02 00 00         mov r8d, dword ptr [rsp + 0x2b8]
009F8842  48 8B 94 24 A8 02 00 00         mov rdx, qword ptr [rsp + 0x2a8]
009F884A  4C 8B 8C 24 A0 02 00 00         mov r9, qword ptr [rsp + 0x2a0]
009F8852  4C 8B 9C 24 98 02 00 00         mov r11, qword ptr [rsp + 0x298]
009F885A  4C 8B 94 24 90 02 00 00         mov r10, qword ptr [rsp + 0x290]
009F8862  E9 0C 1C 00 00                  jmp 0x1409fa473
009F8867  49 8B FF                        mov rdi, r15
009F886A  41 0F 10 45 00                  movups xmm0, xmmword ptr [r13]
009F886F  F3 0F 7F 84 24 B0 00 00 00      movdqu xmmword ptr [rsp + 0xb0], xmm0
009F8878  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
009F8880  48 85 C9                        test rcx, rcx
009F8883  75 61                           jne 0x1409f88e6
009F8885  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F888A  44 8D 61 01                     lea r12d, [rcx + 1]
009F888E  41 8A D4                        mov dl, r12b
009F8891  49 8D 4E 38                     lea rcx, [r14 + 0x38]
009F8895  E8 86 C5 81 FF                  call 0x140214e20
009F889A  45 33 C0                        xor r8d, r8d
009F889D  33 D2                           xor edx, edx
009F889F  49 8B CE                        mov rcx, r14
009F88A2  E8 E9 E0 F1 FF                  call 0x140916990
009F88A7  49 8B BE 28 02 00 00            mov rdi, qword ptr [r14 + 0x228]
009F88AE  4D 89 BE 28 02 00 00            mov qword ptr [r14 + 0x228], r15
009F88B5  45 33 C0                        xor r8d, r8d
009F88B8  33 D2                           xor edx, edx
009F88BA  49 8B CE                        mov rcx, r14
009F88BD  E8 CE 4A E8 FF                  call 0x14087d390
009F88C2  49 8D 4E 38                     lea rcx, [r14 + 0x38]
009F88C6  E8 45 71 86 FF                  call 0x14025fa10
009F88CB  48 85 FF                        test rdi, rdi
009F88CE  0F 84 F4 26 00 00               je 0x1409fafc8
009F88D4  BA 50 73 4A 62                  mov edx, 0x624a7350
009F88D9  48 8B CF                        mov rcx, rdi
009F88DC  E8 FF EF 8F FF                  call 0x1402f78e0
009F88E1  E9 E2 26 00 00                  jmp 0x1409fafc8
009F88E6  4C 8B 05 D3 E3 5C 00            mov r8, qword ptr [rip + 0x5ce3d3]
009F88ED  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
009F88F2  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
009F88F7  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
009F88FF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009F8904  C7 44 24 20 50 73 4A 62         mov dword ptr [rsp + 0x20], 0x624a7350
009F890C  44 8A 4C 24 48                  mov r9b, byte ptr [rsp + 0x48]
009F8911  41 8B D6                        mov edx, r14d
009F8914  E8 37 0D E7 FF                  call 0x140869650
009F8919  8B F0                           mov esi, eax
009F891B  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F8920  85 C0                           test eax, eax
009F8922  78 25                           js 0x1409f8949
009F8924  4D 39 BE D0 04 00 00            cmp qword ptr [r14 + 0x4d0], r15
009F892B  75 27                           jne 0x1409f8954
009F892D  49 8B D6                        mov rdx, r14
009F8930  48 8D 0D F9 F1 06 00            lea rcx, [rip + 0x6f1f9]
009F8937  E8 A4 F8 FA FF                  call 0x1409a81e0
009F893C  48 8B F8                        mov rdi, rax
009F893F  48 85 C0                        test rax, rax
009F8942  75 10                           jne 0x1409f8954
009F8944  BE 9A 00 00 C0                  mov esi, 0xc000009a
009F8949  41 BC 01 00 00 00               mov r12d, 1
009F894F  E9 FD 00 00 00                  jmp 0x1409f8a51
009F8954  41 BC 01 00 00 00               mov r12d, 1
009F895A  41 8A D4                        mov dl, r12b
009F895D  49 8D 4E 38                     lea rcx, [r14 + 0x38]
009F8961  E8 BA C4 81 FF                  call 0x140214e20
009F8966  4D 39 BE 28 02 00 00            cmp qword ptr [r14 + 0x228], r15
009F896D  0F 85 A3 00 00 00               jne 0x1409f8a16
009F8973  41 F7 86 00 01 00 00 00 20 00 00  test dword ptr [r14 + 0x100], 0x2000
009F897E  74 10                           je 0x1409f8990
009F8980  41 8B 86 10 06 00 00            mov eax, dword ptr [r14 + 0x610]
009F8987  41 84 C4                        test r12b, al
009F898A  0F 85 86 00 00 00               jne 0x1409f8a16
009F8990  4D 39 BE D0 04 00 00            cmp qword ptr [r14 + 0x4d0], r15
009F8997  75 0A                           jne 0x1409f89a3
009F8999  49 89 BE D0 04 00 00            mov qword ptr [r14 + 0x4d0], rdi
009F89A0  49 8B FF                        mov rdi, r15
009F89A3  45 33 C0                        xor r8d, r8d
009F89A6  33 D2                           xor edx, edx
009F89A8  49 8B CE                        mov rcx, r14
009F89AB  E8 E0 DF F1 FF                  call 0x140916990
009F89B0  48 8B 84 24 B0 00 00 00         mov rax, qword ptr [rsp + 0xb0]
009F89B8  49 89 86 30 02 00 00            mov qword ptr [r14 + 0x230], rax
009F89BF  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
009F89C7  49 89 86 28 02 00 00            mov qword ptr [r14 + 0x228], rax
009F89CE  4D 89 BE 38 02 00 00            mov qword ptr [r14 + 0x238], r15
009F89D5  45 33 C0                        xor r8d, r8d
009F89D8  33 D2                           xor edx, edx
009F89DA  49 8B CE                        mov rcx, r14
009F89DD  E8 AE 49 E8 FF                  call 0x14087d390
009F89E2  41 8B 86 50 04 00 00            mov eax, dword ptr [r14 + 0x450]
009F89E9  A8 40                           test al, 0x40
009F89EB  74 1E                           je 0x1409f8a0b
009F89ED  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
009F89F2  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
009F89F7  4C 8D 0D 92 A8 08 00            lea r9, [rip + 0x8a892]
009F89FE  45 33 C0                        xor r8d, r8d
009F8A01  33 D2                           xor edx, edx
009F8A03  49 8B CE                        mov rcx, r14
009F8A06  E8 E1 17 F2 FF                  call 0x14091a1ec
009F8A0B  49 8D 4E 38                     lea rcx, [r14 + 0x38]
009F8A0F  E8 FC 6F 86 FF                  call 0x14025fa10
009F8A14  EB 3B                           jmp 0x1409f8a51
009F8A16  49 8D 4E 38                     lea rcx, [r14 + 0x38]
009F8A1A  E8 F1 6F 86 FF                  call 0x14025fa10
009F8A1F  BA 50 73 4A 62                  mov edx, 0x624a7350
009F8A24  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
009F8A2C  E8 AF EE 8F FF                  call 0x1402f78e0
009F8A31  BE 0D 00 00 C0                  mov esi, 0xc000000d
009F8A36  EB 19                           jmp 0x1409f8a51
009F8A38  8B F0                           mov esi, eax
009F8A3A  45 33 FF                        xor r15d, r15d
009F8A3D  45 8D 67 01                     lea r12d, [r15 + 1]
009F8A41  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F8A46  41 8B FF                        mov edi, r15d
009F8A49  8B 5C 24 60                     mov ebx, dword ptr [rsp + 0x60]
009F8A4D  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
009F8A51  48 85 FF                        test rdi, rdi
009F8A54  0F 84 6E 25 00 00               je 0x1409fafc8
009F8A5A  4C 89 7F 38                     mov qword ptr [rdi + 0x38], r15
009F8A5E  48 8B CF                        mov rcx, rdi
009F8A61  E8 6A F8 FA FF                  call 0x1409a82d0
009F8A66  E9 5D 25 00 00                  jmp 0x1409fafc8
009F8A6B  41 8B 5D 00                     mov ebx, dword ptr [r13]
009F8A6F  89 9C 24 88 01 00 00            mov dword ptr [rsp + 0x188], ebx
009F8A76  41 BC 01 00 00 00               mov r12d, 1
009F8A7C  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F8A81  41 3B DC                        cmp ebx, r12d
009F8A84  0F 87 B9 22 00 00               ja 0x1409fad43
009F8A8A  41 8A D4                        mov dl, r12b
009F8A8D  49 8D 4E 38                     lea rcx, [r14 + 0x38]
009F8A91  E8 8A C3 81 FF                  call 0x140214e20
009F8A96  41 89 9E 24 02 00 00            mov dword ptr [r14 + 0x224], ebx
009F8A9D  49 8D 4E 38                     lea rcx, [r14 + 0x38]
009F8AA1  E8 6A 6F 86 FF                  call 0x14025fa10
009F8AA6  E9 1D 25 00 00                  jmp 0x1409fafc8
009F8AAB  8B F0                           mov esi, eax
009F8AAD  41 BC 01 00 00 00               mov r12d, 1
009F8AB3  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F8AB8  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009F8ABD  E9 1F 25 00 00                  jmp 0x1409fafe1
009F8AC2  41 0F 10 45 00                  movups xmm0, xmmword ptr [r13]
009F8AC7  0F 11 84 24 90 01 00 00         movups xmmword ptr [rsp + 0x190], xmm0
009F8ACF  41 0F 10 4D 10                  movups xmm1, xmmword ptr [r13 + 0x10]
009F8AD4  0F 11 8C 24 A0 01 00 00         movups xmmword ptr [rsp + 0x1a0], xmm1
009F8ADC  F2 41 0F 10 45 20               movsd xmm0, qword ptr [r13 + 0x20]
009F8AE2  F2 0F 11 84 24 B0 01 00 00      movsd qword ptr [rsp + 0x1b0], xmm0
009F8AEB  8B 84 24 90 01 00 00            mov eax, dword ptr [rsp + 0x190]
009F8AF2  83 E0 F0                        and eax, 0xfffffff0
009F8AF5  F7 D8                           neg eax
009F8AF7  1B F6                           sbb esi, esi
009F8AF9  81 E6 52 FF FF FF               and esi, 0xffffff52
009F8AFF  81 C6 BB 00 00 C0               add esi, 0xc00000bb
009F8B05  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F8B0A  E9 B3 24 00 00                  jmp 0x1409fafc2
009F8B0F  8B F0                           mov esi, eax
009F8B11  41 BC 01 00 00 00               mov r12d, 1
009F8B17  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F8B1C  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009F8B21  E9 BB 24 00 00                  jmp 0x1409fafe1
009F8B26  45 8B 45 00                     mov r8d, dword ptr [r13]
009F8B2A  44 89 84 24 60 01 00 00         mov dword ptr [rsp + 0x160], r8d
009F8B32  45 33 C9                        xor r9d, r9d
009F8B35  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
009F8B3D  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F8B42  49 8B CE                        mov rcx, r14
009F8B45  E8 CE 46 D0 FF                  call 0x1406fd218
009F8B4A  E9 71 24 00 00                  jmp 0x1409fafc0
009F8B4F  8B F0                           mov esi, eax
009F8B51  41 BC 01 00 00 00               mov r12d, 1
009F8B57  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F8B5C  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009F8B61  E9 7B 24 00 00                  jmp 0x1409fafe1
009F8B66  4D 8B C4                        mov r8, r12
009F8B69  49 8B D5                        mov rdx, r13
009F8B6C  48 8D 8C 24 70 03 00 00         lea rcx, [rsp + 0x370]
009F8B74  E8 C7 DC CC FF                  call 0x1406c6840
009F8B79  90                              nop
009F8B7A  BA 98 00 00 00                  mov edx, 0x98
009F8B7F  44 3B E2                        cmp r12d, edx
009F8B82  73 18                           jae 0x1409f8b9c
009F8B84  49 2B D4                        sub rdx, r12
009F8B87  48 8D 8C 24 70 03 00 00         lea rcx, [rsp + 0x370]
009F8B8F  49 03 CC                        add rcx, r12
009F8B92  4C 8B C2                        mov r8, rdx
009F8B95  33 D2                           xor edx, edx
009F8B97  E8 A4 E0 CC FF                  call 0x1406c6c40
009F8B9C  41 8B D4                        mov edx, r12d
009F8B9F  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
009F8BA4  41 8B CD                        mov ecx, r13d
009F8BA7  E8 AC 28 00 00                  call 0x1409fb458
009F8BAC  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
009F8BB0  F7 D0                           not eax
009F8BB2  85 84 24 80 03 00 00            test dword ptr [rsp + 0x380], eax
009F8BB9  74 15                           je 0x1409f8bd0
009F8BBB  41 BC 01 00 00 00               mov r12d, 1
009F8BC1  BE 0D 00 00 C0                  mov esi, 0xc000000d
009F8BC6  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F8BCB  E9 11 24 00 00                  jmp 0x1409fafe1
009F8BD0  33 D2                           xor edx, edx
009F8BD2  41 B8 28 07 00 00               mov r8d, 0x728
009F8BD8  48 8D 8C 24 20 05 00 00         lea rcx, [rsp + 0x520]
009F8BE0  E8 5B E0 CC FF                  call 0x1406c6c40
009F8BE5  0F 57 C0                        xorps xmm0, xmm0
009F8BE8  33 C0                           xor eax, eax
009F8BEA  0F 11 84 24 D8 00 00 00         movups xmmword ptr [rsp + 0xd8], xmm0
009F8BF2  0F 11 84 24 E8 00 00 00         movups xmmword ptr [rsp + 0xe8], xmm0
009F8BFA  48 89 84 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rax
009F8C02  8B 94 24 80 03 00 00            mov edx, dword ptr [rsp + 0x380]
009F8C09  89 94 24 20 06 00 00            mov dword ptr [rsp + 0x620], edx
009F8C10  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
009F8C15  4C 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], r15
009F8C1D  4C 89 BC 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r15
009F8C25  8A C2                           mov al, dl
009F8C27  24 08                           and al, 8
009F8C29  F6 D8                           neg al
009F8C2B  1B C9                           sbb ecx, ecx
009F8C2D  23 8C 24 98 03 00 00            and ecx, dword ptr [rsp + 0x398]
009F8C34  89 8C 24 24 06 00 00            mov dword ptr [rsp + 0x624], ecx
009F8C3B  41 BE 20 00 00 00               mov r14d, 0x20
009F8C41  45 8D 66 E1                     lea r12d, [r14 - 0x1f]
009F8C45  41 84 D6                        test r14b, dl
009F8C48  74 5B                           je 0x1409f8ca5
009F8C4A  8B 84 24 A8 03 00 00            mov eax, dword ptr [rsp + 0x3a8]
009F8C51  83 F8 06                        cmp eax, 6
009F8C54  0F 87 67 FF FF FF               ja 0x1409f8bc1
009F8C5A  83 C0 FD                        add eax, -3
009F8C5D  41 3B C4                        cmp eax, r12d
009F8C60  77 33                           ja 0x1409f8c95
009F8C62  44 8A 4C 24 48                  mov r9b, byte ptr [rsp + 0x48]
009F8C67  45 8D 46 E2                     lea r8d, [r14 - 0x1e]
009F8C6B  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
009F8C73  48 8B 0D 6E 0E 5E 00            mov rcx, qword ptr [rip + 0x5e0e6e]
009F8C7A  E8 4D D6 FF FF                  call 0x1409f62cc
009F8C7F  41 22 C4                        and al, r12b
009F8C82  8A D8                           mov bl, al
009F8C84  C0 E3 02                        shl bl, 2
009F8C87  84 C0                           test al, al
009F8C89  75 0A                           jne 0x1409f8c95
009F8C8B  BE 61 00 00 C0                  mov esi, 0xc0000061
009F8C90  E9 31 FF FF FF                  jmp 0x1409f8bc6
009F8C95  8B 84 24 A8 03 00 00            mov eax, dword ptr [rsp + 0x3a8]
009F8C9C  88 84 24 6D 09 00 00            mov byte ptr [rsp + 0x96d], al
009F8CA3  EB 08                           jmp 0x1409f8cad
009F8CA5  44 88 BC 24 6D 09 00 00         mov byte ptr [rsp + 0x96d], r15b
009F8CAD  F6 84 24 80 03 00 00 80         test byte ptr [rsp + 0x380], 0x80
009F8CB5  74 50                           je 0x1409f8d07
009F8CB7  8B 84 24 AC 03 00 00            mov eax, dword ptr [rsp + 0x3ac]
009F8CBE  83 F8 0A                        cmp eax, 0xa
009F8CC1  0F 83 FA FE FF FF               jae 0x1409f8bc1
009F8CC7  83 F8 05                        cmp eax, 5
009F8CCA  76 32                           jbe 0x1409f8cfe
009F8CCC  44 8A 4C 24 48                  mov r9b, byte ptr [rsp + 0x48]
009F8CD1  41 B8 02 00 00 00               mov r8d, 2
009F8CD7  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
009F8CDF  48 8B 0D 02 0E 5E 00            mov rcx, qword ptr [rip + 0x5e0e02]
009F8CE6  E8 E1 D5 FF FF                  call 0x1409f62cc
009F8CEB  41 22 C4                        and al, r12b
009F8CEE  8A D8                           mov bl, al
009F8CF0  C0 E3 02                        shl bl, 2
009F8CF3  84 C0                           test al, al
009F8CF5  74 94                           je 0x1409f8c8b
009F8CF7  8B 84 24 AC 03 00 00            mov eax, dword ptr [rsp + 0x3ac]
009F8CFE  89 84 24 64 07 00 00            mov dword ptr [rsp + 0x764], eax
009F8D05  EB 0B                           jmp 0x1409f8d12
009F8D07  C7 84 24 64 07 00 00 05 00 00 00  mov dword ptr [rsp + 0x764], 5
009F8D12  F6 84 24 80 03 00 00 02         test byte ptr [rsp + 0x380], 2
009F8D1A  74 1B                           je 0x1409f8d37
009F8D1C  48 8B 84 24 70 03 00 00         mov rax, qword ptr [rsp + 0x370]
009F8D24  48 85 C0                        test rax, rax
009F8D27  0F 84 94 FE FF FF               je 0x1409f8bc1
009F8D2D  48 89 84 24 00 06 00 00         mov qword ptr [rsp + 0x600], rax
009F8D35  EB 08                           jmp 0x1409f8d3f
009F8D37  4C 89 BC 24 00 06 00 00         mov qword ptr [rsp + 0x600], r15
009F8D3F  F6 84 24 80 03 00 00 04         test byte ptr [rsp + 0x380], 4
009F8D47  74 19                           je 0x1409f8d62
009F8D49  48 8B 84 24 78 03 00 00         mov rax, qword ptr [rsp + 0x378]
009F8D51  48 85 C0                        test rax, rax
009F8D54  0F 84 67 FE FF FF               je 0x1409f8bc1
009F8D5A  48 89 84 24 08 06 00 00         mov qword ptr [rsp + 0x608], rax
009F8D62  44 84 A4 24 80 03 00 00         test byte ptr [rsp + 0x380], r12b
009F8D6A  0F 84 8C 00 00 00               je 0x1409f8dfc
009F8D70  48 8B 8C 24 88 03 00 00         mov rcx, qword ptr [rsp + 0x388]
009F8D78  48 85 C9                        test rcx, rcx
009F8D7B  75 0E                           jne 0x1409f8d8b
009F8D7D  4C 39 BC 24 90 03 00 00         cmp qword ptr [rsp + 0x390], r15
009F8D85  0F 84 36 FE FF FF               je 0x1409f8bc1
009F8D8B  48 3B CF                        cmp rcx, rdi
009F8D8E  75 0E                           jne 0x1409f8d9e
009F8D90  48 39 BC 24 90 03 00 00         cmp qword ptr [rsp + 0x390], rdi
009F8D98  0F 84 23 FE FF FF               je 0x1409f8bc1
009F8D9E  48 3B 8C 24 90 03 00 00         cmp rcx, qword ptr [rsp + 0x390]
009F8DA6  0F 87 15 FE FF FF               ja 0x1409f8bc1
009F8DAC  48 81 F9 00 40 01 00            cmp rcx, 0x14000
009F8DB3  0F 82 08 FE FF FF               jb 0x1409f8bc1
009F8DB9  48 3B 0D 80 F4 5D 00            cmp rcx, qword ptr [rip + 0x5df480]
009F8DC0  76 20                           jbe 0x1409f8de2
009F8DC2  8A 54 24 48                     mov dl, byte ptr [rsp + 0x48]
009F8DC6  48 8B 0D 1B 0D 5E 00            mov rcx, qword ptr [rip + 0x5e0d1b]
009F8DCD  E8 4E 90 E7 FF                  call 0x140871e20
009F8DD2  84 C0                           test al, al
009F8DD4  0F 84 B1 FE FF FF               je 0x1409f8c8b
009F8DDA  48 8B 8C 24 88 03 00 00         mov rcx, qword ptr [rsp + 0x388]
009F8DE2  48 89 8C 24 10 06 00 00         mov qword ptr [rsp + 0x610], rcx
009F8DEA  48 8B 84 24 90 03 00 00         mov rax, qword ptr [rsp + 0x390]
009F8DF2  48 89 84 24 18 06 00 00         mov qword ptr [rsp + 0x618], rax
009F8DFA  EB 10                           jmp 0x1409f8e0c
009F8DFC  4C 89 BC 24 10 06 00 00         mov qword ptr [rsp + 0x610], r15
009F8E04  4C 89 BC 24 18 06 00 00         mov qword ptr [rsp + 0x618], r15
009F8E0C  BA 00 01 00 00                  mov edx, 0x100
009F8E11  B8 00 10 00 00                  mov eax, 0x1000
009F8E16  85 94 24 80 03 00 00            test dword ptr [rsp + 0x380], edx
009F8E1D  74 1F                           je 0x1409f8e3e
009F8E1F  48 8B 8C 24 E0 03 00 00         mov rcx, qword ptr [rsp + 0x3e0]
009F8E27  48 3B C8                        cmp rcx, rax
009F8E2A  0F 82 91 FD FF FF               jb 0x1409f8bc1
009F8E30  48 C1 E9 0C                     shr rcx, 0xc
009F8E34  48 89 8C 24 D0 07 00 00         mov qword ptr [rsp + 0x7d0], rcx
009F8E3C  EB 08                           jmp 0x1409f8e46
009F8E3E  4C 89 BC 24 D0 07 00 00         mov qword ptr [rsp + 0x7d0], r15
009F8E46  F7 84 24 80 03 00 00 00 02 00 00  test dword ptr [rsp + 0x380], 0x200
009F8E51  74 1F                           je 0x1409f8e72
009F8E53  48 8B 8C 24 E8 03 00 00         mov rcx, qword ptr [rsp + 0x3e8]
009F8E5B  48 3B C8                        cmp rcx, rax
009F8E5E  0F 82 5D FD FF FF               jb 0x1409f8bc1
009F8E64  48 C1 E9 0C                     shr rcx, 0xc
009F8E68  48 89 8C 24 D8 07 00 00         mov qword ptr [rsp + 0x7d8], rcx
009F8E70  EB 08                           jmp 0x1409f8e7a
009F8E72  4C 89 BC 24 D8 07 00 00         mov qword ptr [rsp + 0x7d8], r15
009F8E7A  F7 84 24 80 03 00 00 00 00 20 00  test dword ptr [rsp + 0x380], 0x200000
009F8E85  74 1F                           je 0x1409f8ea6
009F8E87  48 8B 8C 24 00 04 00 00         mov rcx, qword ptr [rsp + 0x400]
009F8E8F  48 3B C8                        cmp rcx, rax
009F8E92  0F 82 29 FD FF FF               jb 0x1409f8bc1
009F8E98  48 C1 E9 0C                     shr rcx, 0xc
009F8E9C  48 89 8C 24 E0 07 00 00         mov qword ptr [rsp + 0x7e0], rcx
009F8EA4  EB 08                           jmp 0x1409f8eae
009F8EA6  4C 89 BC 24 E0 07 00 00         mov qword ptr [rsp + 0x7e0], r15
009F8EAE  48 C7 84 24 28 06 00 00 01 00 20 00  mov qword ptr [rsp + 0x628], 0x200001
009F8EBA  4C 8B C2                        mov r8, rdx
009F8EBD  33 D2                           xor edx, edx
009F8EBF  48 8D 8C 24 30 06 00 00         lea rcx, [rsp + 0x630]
009F8EC7  E8 74 DD CC FF                  call 0x1406c6c40
009F8ECC  8B 84 24 20 06 00 00            mov eax, dword ptr [rsp + 0x620]
009F8ED3  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
009F8ED7  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F8EDC  A8 10                           test al, 0x10
009F8EDE  0F 84 42 01 00 00               je 0x1409f9026
009F8EE4  41 8B 86 10 06 00 00            mov eax, dword ptr [r14 + 0x610]
009F8EEB  A8 02                           test al, 2
009F8EED  0F 85 6A 01 00 00               jne 0x1409f905d
009F8EF3  4C 39 BC 24 A0 03 00 00         cmp qword ptr [rsp + 0x3a0], r15
009F8EFB  0F 84 5C 01 00 00               je 0x1409f905d
009F8F01  4D 39 BE 10 02 00 00            cmp qword ptr [r14 + 0x210], r15
009F8F08  0F 85 80 00 00 00               jne 0x1409f8f8e
009F8F0E  BA 28 00 00 00                  mov edx, 0x28
009F8F13  B9 00 01 00 00                  mov ecx, 0x100
009F8F18  41 B8 50 73 4A 61               mov r8d, 0x614a7350
009F8F1E  E8 CD 91 18 00                  call 0x140b820f0
009F8F23  48 8B F0                        mov rsi, rax
009F8F26  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
009F8F2B  48 85 C0                        test rax, rax
009F8F2E  75 0A                           jne 0x1409f8f3a
009F8F30  BE 9A 00 00 C0                  mov esi, 0xc000009a
009F8F35  E9 A7 20 00 00                  jmp 0x1409fafe1
009F8F3A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009F8F43  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
009F8F4A  45 33 C0                        xor r8d, r8d
009F8F4D  41 8D 50 28                     lea edx, [r8 + 0x28]
009F8F51  E8 EA 53 FA FF                  call 0x14099e340
009F8F56  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
009F8F5E  48 85 C0                        test rax, rax
009F8F61  75 17                           jne 0x1409f8f7a
009F8F63  48 8B CE                        mov rcx, rsi
009F8F66  BA 50 73 4A 61                  mov edx, 0x614a7350
009F8F6B  E8 00 99 18 00                  call 0x140b82870
009F8F70  BE 9A 00 00 C0                  mov esi, 0xc000009a
009F8F75  E9 4C FC FF FF                  jmp 0x1409f8bc6
009F8F7A  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F8F7F  8B 84 24 20 06 00 00            mov eax, dword ptr [rsp + 0x620]
009F8F86  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
009F8F8A  8B 74 24 58                     mov esi, dword ptr [rsp + 0x58]
009F8F8E  4C 8D 84 24 E0 00 00 00         lea r8, [rsp + 0xe0]
009F8F96  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
009F8F9E  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
009F8FA5  E8 E6 BC EC FF                  call 0x1408c4c90
009F8FAA  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
009F8FB2  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
009F8FBA  44 38 7C 24 48                  cmp byte ptr [rsp + 0x48], r15b
009F8FBF  74 5A                           je 0x1409f901b
009F8FC1  44 89 A4 24 E0 02 00 00         mov dword ptr [rsp + 0x2e0], r12d
009F8FC9  44 89 A4 24 E4 02 00 00         mov dword ptr [rsp + 0x2e4], r12d
009F8FD1  48 8B 05 A8 0A 5E 00            mov rax, qword ptr [rip + 0x5e0aa8]
009F8FD8  48 89 84 24 E8 02 00 00         mov qword ptr [rsp + 0x2e8], rax
009F8FE0  44 89 BC 24 F0 02 00 00         mov dword ptr [rsp + 0x2f0], r15d
009F8FE8  45 8A C4                        mov r8b, r12b
009F8FEB  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
009F8FF3  48 8D 8C 24 E0 02 00 00         lea rcx, [rsp + 0x2e0]
009F8FFB  E8 70 1E FC FF                  call 0x1409bae70
009F9000  0F B6 C8                        movzx ecx, al
009F9003  41 23 CC                        and ecx, r12d
009F9006  8B 84 24 D8 00 00 00            mov eax, dword ptr [rsp + 0xd8]
009F900D  83 E0 FE                        and eax, 0xfffffffe
009F9010  0B C8                           or ecx, eax
009F9012  89 8C 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], ecx
009F9019  EB 08                           jmp 0x1409f9023
009F901B  44 09 A4 24 D8 00 00 00         or dword ptr [rsp + 0xd8], r12d
009F9023  80 CB 02                        or bl, 2
009F9026  49 8D 4E 38                     lea rcx, [r14 + 0x38]
009F902A  41 8A D4                        mov dl, r12b
009F902D  E8 EE BD 81 FF                  call 0x140214e20
009F9032  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
009F9036  F6 C2 04                        test dl, 4
009F9039  75 34                           jne 0x1409f906f
009F903B  F6 C2 40                        test dl, 0x40
009F903E  74 27                           je 0x1409f9067
009F9040  41 8B 86 00 01 00 00            mov eax, dword ptr [r14 + 0x100]
009F9047  83 E0 04                        and eax, 4
009F904A  0B D0                           or edx, eax
009F904C  49 8B 86 E8 00 00 00            mov rax, qword ptr [r14 + 0xe8]
009F9053  48 89 84 24 08 06 00 00         mov qword ptr [rsp + 0x608], rax
009F905B  EB 12                           jmp 0x1409f906f
009F905D  BE 0D 00 00 C0                  mov esi, 0xc000000d
009F9062  E9 7A 1F 00 00                  jmp 0x1409fafe1
009F9067  4C 89 BC 24 08 06 00 00         mov qword ptr [rsp + 0x608], r15
009F906F  83 E2 BF                        and edx, 0xffffffbf
009F9072  89 94 24 20 06 00 00            mov dword ptr [rsp + 0x620], edx
009F9079  B9 02 00 00 00                  mov ecx, 2
009F907E  84 D9                           test cl, bl
009F9080  0F 84 6A 01 00 00               je 0x1409f91f0
009F9086  41 8B 86 10 06 00 00            mov eax, dword ptr [r14 + 0x610]
009F908D  84 C1                           test cl, al
009F908F  74 0E                           je 0x1409f909f
009F9091  BE 0D 00 00 C0                  mov esi, 0xc000000d
009F9096  89 74 24 58                     mov dword ptr [rsp + 0x58], esi
009F909A  E9 00 04 00 00                  jmp 0x1409f949f
009F909F  41 8B 86 00 01 00 00            mov eax, dword ptr [r14 + 0x100]
009F90A6  A8 10                           test al, 0x10
009F90A8  74 1E                           je 0x1409f90c8
009F90AA  49 8D 96 08 01 00 00            lea rdx, [r14 + 0x108]
009F90B1  48 8D 8C 24 38 01 00 00         lea rcx, [rsp + 0x138]
009F90B9  E8 52 A7 A6 FF                  call 0x140463810
009F90BE  0F B7 84 24 40 01 00 00         movzx eax, word ptr [rsp + 0x140]
009F90C6  EB 16                           jmp 0x1409f90de
009F90C8  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
009F90D1  E8 DE 72 A9 FF                  call 0x1404903b4
009F90D6  66 89 84 24 40 01 00 00         mov word ptr [rsp + 0x140], ax
009F90DE  0F B7 C8                        movzx ecx, ax
009F90E1  48 8D 05 18 6F 60 FF            lea rax, [rip - 0x9f90e8]
009F90E8  48 8B 8C C8 28 71 FC 00         mov rcx, qword ptr [rax + rcx*8 + 0xfc7128]
009F90F0  4C 8B 84 24 A0 03 00 00         mov r8, qword ptr [rsp + 0x3a0]
009F90F8  49 8B C0                        mov rax, r8
009F90FB  48 23 C1                        and rax, rcx
009F90FE  4C 3B C0                        cmp r8, rax
009F9101  74 13                           je 0x1409f9116
009F9103  BE 0D 00 00 C0                  mov esi, 0xc000000d
009F9108  89 74 24 58                     mov dword ptr [rsp + 0x58], esi
009F910C  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F9111  E9 89 03 00 00                  jmp 0x1409f949f
009F9116  0F B7 94 24 40 01 00 00         movzx edx, word ptr [rsp + 0x140]
009F911E  48 8D 8C 24 28 06 00 00         lea rcx, [rsp + 0x628]
009F9126  E8 95 25 86 FF                  call 0x14025b6c0
009F912B  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
009F9130  48 8D 84 24 D8 00 00 00         lea rax, [rsp + 0xd8]
009F9138  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009F913D  4C 8D 0D 1C C3 D8 FF            lea r9, [rip - 0x273ce4]
009F9144  45 33 C0                        xor r8d, r8d
009F9147  33 D2                           xor edx, edx
009F9149  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F914E  49 8B CE                        mov rcx, r14
009F9151  E8 96 10 F2 FF                  call 0x14091a1ec
009F9156  8B F0                           mov esi, eax
009F9158  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
009F915C  85 C0                           test eax, eax
009F915E  0F 88 3B 03 00 00               js 0x1409f949f
009F9164  49 8B 86 10 02 00 00            mov rax, qword ptr [r14 + 0x210]
009F916B  48 85 C0                        test rax, rax
009F916E  75 2A                           jne 0x1409f919a
009F9170  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
009F9175  49 89 86 10 02 00 00            mov qword ptr [r14 + 0x210], rax
009F917C  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
009F9184  49 89 86 18 02 00 00            mov qword ptr [r14 + 0x218], rax
009F918B  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
009F9190  4C 89 BC 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r15
009F9198  EB 28                           jmp 0x1409f91c2
009F919A  0F 10 40 08                     movups xmm0, xmmword ptr [rax + 8]
009F919E  0F 11 84 24 68 01 00 00         movups xmmword ptr [rsp + 0x168], xmm0
009F91A6  0F 10 48 18                     movups xmm1, xmmword ptr [rax + 0x18]
009F91AA  0F 11 8C 24 78 01 00 00         movups xmmword ptr [rsp + 0x178], xmm1
009F91B2  48 8D 84 24 68 01 00 00         lea rax, [rsp + 0x168]
009F91BA  48 89 84 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rax
009F91C2  49 8B 86 10 02 00 00            mov rax, qword ptr [r14 + 0x210]
009F91C9  0F 10 84 24 D8 00 00 00         movups xmm0, xmmword ptr [rsp + 0xd8]
009F91D1  0F 11 00                        movups xmmword ptr [rax], xmm0
009F91D4  0F 10 8C 24 E8 00 00 00         movups xmm1, xmmword ptr [rsp + 0xe8]
009F91DC  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
009F91E0  F2 0F 10 84 24 F8 00 00 00      movsd xmm0, qword ptr [rsp + 0xf8]
009F91E9  F2 0F 11 40 20                  movsd qword ptr [rax + 0x20], xmm0
009F91EE  EB 15                           jmp 0x1409f9205
009F91F0  0F BA E2 0E                     bt edx, 0xe
009F91F4  73 0F                           jae 0x1409f9205
009F91F6  41 8B 86 10 06 00 00            mov eax, dword ptr [r14 + 0x610]
009F91FD  84 C1                           test cl, al
009F91FF  0F 84 8C FE FF FF               je 0x1409f9091
009F9205  41 8B 86 00 01 00 00            mov eax, dword ptr [r14 + 0x100]
009F920C  41 84 C4                        test r12b, al
009F920F  74 30                           je 0x1409f9241
009F9211  44 84 A4 24 20 06 00 00         test byte ptr [rsp + 0x620], r12b
009F9219  75 26                           jne 0x1409f9241
009F921B  F0 44 09 3C 24                  lock or dword ptr [rsp], r15d
009F9220  48 8B 05 89 DE 5C 00            mov rax, qword ptr [rip + 0x5cde89]
009F9227  41 84 C4                        test r12b, al
009F922A  74 0C                           je 0x1409f9238
009F922C  48 8D 0D 7D DE 5C 00            lea rcx, [rip + 0x5cde7d]
009F9233  E8 F4 09 A2 FF                  call 0x140419c2c
009F9238  8B 74 24 58                     mov esi, dword ptr [rsp + 0x58]
009F923C  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F9241  4C 89 B4 24 00 01 00 00         mov qword ptr [rsp + 0x100], r14
009F9249  49 8D 8E 00 01 00 00            lea rcx, [r14 + 0x100]
009F9250  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
009F9258  8B 01                           mov eax, dword ptr [rcx]
009F925A  89 84 24 0C 01 00 00            mov dword ptr [rsp + 0x10c], eax
009F9261  48 8B 84 24 10 06 00 00         mov rax, qword ptr [rsp + 0x610]
009F9269  49 89 86 F0 00 00 00            mov qword ptr [r14 + 0xf0], rax
009F9270  48 8B 84 24 18 06 00 00         mov rax, qword ptr [rsp + 0x618]
009F9278  49 89 86 F8 00 00 00            mov qword ptr [r14 + 0xf8], rax
009F927F  8B 84 24 24 06 00 00            mov eax, dword ptr [rsp + 0x624]
009F9286  41 89 86 04 01 00 00            mov dword ptr [r14 + 0x104], eax
009F928D  B8 02 00 00 00                  mov eax, 2
009F9292  84 D8                           test al, bl
009F9294  74 6B                           je 0x1409f9301
009F9296  49 8D 8E 08 01 00 00            lea rcx, [r14 + 0x108]
009F929D  48 8D 94 24 28 06 00 00         lea rdx, [rsp + 0x628]
009F92A5  44 8D 40 7E                     lea r8d, [rax + 0x7e]
009F92A9  0F 10 02                        movups xmm0, xmmword ptr [rdx]
009F92AC  0F 11 01                        movups xmmword ptr [rcx], xmm0
009F92AF  0F 10 4A 10                     movups xmm1, xmmword ptr [rdx + 0x10]
009F92B3  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
009F92B7  0F 10 42 20                     movups xmm0, xmmword ptr [rdx + 0x20]
009F92BB  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
009F92BF  0F 10 4A 30                     movups xmm1, xmmword ptr [rdx + 0x30]
009F92C3  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
009F92C7  0F 10 42 40                     movups xmm0, xmmword ptr [rdx + 0x40]
009F92CB  0F 11 41 40                     movups xmmword ptr [rcx + 0x40], xmm0
009F92CF  0F 10 4A 50                     movups xmm1, xmmword ptr [rdx + 0x50]
009F92D3  0F 11 49 50                     movups xmmword ptr [rcx + 0x50], xmm1
009F92D7  0F 10 42 60                     movups xmm0, xmmword ptr [rdx + 0x60]
009F92DB  0F 11 41 60                     movups xmmword ptr [rcx + 0x60], xmm0
009F92DF  49 03 C8                        add rcx, r8
009F92E2  0F 10 4A 70                     movups xmm1, xmmword ptr [rdx + 0x70]
009F92E6  0F 11 49 F0                     movups xmmword ptr [rcx - 0x10], xmm1
009F92EA  49 03 D0                        add rdx, r8
009F92ED  48 83 E8 01                     sub rax, 1
009F92F1  75 B6                           jne 0x1409f92a9
009F92F3  48 8B 02                        mov rax, qword ptr [rdx]
009F92F6  48 89 01                        mov qword ptr [rcx], rax
009F92F9  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
009F9301  8A 84 24 6D 09 00 00            mov al, byte ptr [rsp + 0x96d]
009F9308  41 88 86 4D 04 00 00            mov byte ptr [r14 + 0x44d], al
009F930F  8B 84 24 64 07 00 00            mov eax, dword ptr [rsp + 0x764]
009F9316  41 89 86 44 02 00 00            mov dword ptr [r14 + 0x244], eax
009F931D  48 8B 84 24 00 06 00 00         mov rax, qword ptr [rsp + 0x600]
009F9325  49 89 86 E0 00 00 00            mov qword ptr [r14 + 0xe0], rax
009F932C  49 8D 96 E8 00 00 00            lea rdx, [r14 + 0xe8]
009F9333  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
009F9338  48 8B 84 24 08 06 00 00         mov rax, qword ptr [rsp + 0x608]
009F9340  48 89 02                        mov qword ptr [rdx], rax
009F9343  41 83 FD 09                     cmp r13d, 9
009F9347  0F 85 96 00 00 00               jne 0x1409f93e3
009F934D  45 33 C0                        xor r8d, r8d
009F9350  33 D2                           xor edx, edx
009F9352  49 8B CE                        mov rcx, r14
009F9355  E8 36 D6 F1 FF                  call 0x140916990
009F935A  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
009F935E  F7 D0                           not eax
009F9360  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
009F9368  23 01                           and eax, dword ptr [rcx]
009F936A  0B 84 24 20 06 00 00            or eax, dword ptr [rsp + 0x620]
009F9371  89 01                           mov dword ptr [rcx], eax
009F9373  48 8B 84 24 D0 07 00 00         mov rax, qword ptr [rsp + 0x7d0]
009F937B  49 89 86 B0 02 00 00            mov qword ptr [r14 + 0x2b0], rax
009F9382  48 8B 84 24 D8 07 00 00         mov rax, qword ptr [rsp + 0x7d8]
009F938A  49 89 86 B8 02 00 00            mov qword ptr [r14 + 0x2b8], rax
009F9391  48 8B 84 24 E0 07 00 00         mov rax, qword ptr [rsp + 0x7e0]
009F9399  49 89 86 C0 02 00 00            mov qword ptr [r14 + 0x2c0], rax
009F93A0  F0 49 0F C1 BE F0 04 00 00      lock xadd qword ptr [r14 + 0x4f0], rdi
009F93A9  40 80 E7 06                     and dil, 6
009F93AD  40 80 FF 02                     cmp dil, 2
009F93B1  75 0C                           jne 0x1409f93bf
009F93B3  49 8D 8E F0 04 00 00            lea rcx, [r14 + 0x4f0]
009F93BA  E8 11 CA 86 FF                  call 0x140265dd0
009F93BF  49 8D 8E F0 04 00 00            lea rcx, [r14 + 0x4f0]
009F93C6  E8 35 82 8E FF                  call 0x1402e1600
009F93CB  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F93D0  8B 74 24 58                     mov esi, dword ptr [rsp + 0x58]
009F93D4  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
009F93DC  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
009F93E1  EB 11                           jmp 0x1409f93f4
009F93E3  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
009F93E7  F7 D0                           not eax
009F93E9  23 01                           and eax, dword ptr [rcx]
009F93EB  0B 84 24 20 06 00 00            or eax, dword ptr [rsp + 0x620]
009F93F2  89 01                           mov dword ptr [rcx], eax
009F93F4  8B 84 24 0C 01 00 00            mov eax, dword ptr [rsp + 0x10c]
009F93FB  0B 01                           or eax, dword ptr [rcx]
009F93FD  F7 D0                           not eax
009F93FF  89 84 24 08 01 00 00            mov dword ptr [rsp + 0x108], eax
009F9406  F6 84 24 80 03 00 00 04         test byte ptr [rsp + 0x380], 4
009F940E  74 34                           je 0x1409f9444
009F9410  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
009F9415  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
009F941A  4C 8D 0D DF C4 D8 FF            lea r9, [rip - 0x273b21]
009F9421  45 33 C0                        xor r8d, r8d
009F9424  33 D2                           xor edx, edx
009F9426  49 8B CE                        mov rcx, r14
009F9429  E8 BE 0D F2 FF                  call 0x14091a1ec
009F942E  4D 89 BE B8 00 00 00            mov qword ptr [r14 + 0xb8], r15
009F9435  4D 89 BE C0 00 00 00            mov qword ptr [r14 + 0xc0], r15
009F943C  49 8B CE                        mov rcx, r14
009F943F  E8 0C EF 84 FF                  call 0x140248350
009F9444  41 8B 86 00 01 00 00            mov eax, dword ptr [r14 + 0x100]
009F944B  A8 06                           test al, 6
009F944D  74 11                           je 0x1409f9460
009F944F  F0 4C 01 25 89 D1 50 00         lock add qword ptr [rip + 0x50d189], r12
009F9457  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F945C  8B 74 24 58                     mov esi, dword ptr [rsp + 0x58]
009F9460  44 84 A4 24 08 01 00 00         test byte ptr [rsp + 0x108], r12b
009F9468  75 03                           jne 0x1409f946d
009F946A  41 0A DC                        or bl, r12b
009F946D  C7 44 24 28 05 00 00 00         mov dword ptr [rsp + 0x28], 5
009F9475  48 8D 84 24 00 01 00 00         lea rax, [rsp + 0x100]
009F947D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009F9482  4C 8D 0D 97 DD 05 00            lea r9, [rip + 0x5dd97]
009F9489  4C 8D 05 40 6E 08 00            lea r8, [rip + 0x86e40]
009F9490  48 8D 15 29 52 E8 FF            lea rdx, [rip - 0x17add7]
009F9497  49 8B CE                        mov rcx, r14
009F949A  E8 4D 0D F2 FF                  call 0x14091a1ec
009F949F  41 84 DC                        test r12b, bl
009F94A2  0F 84 80 00 00 00               je 0x1409f9528
009F94A8  45 33 C0                        xor r8d, r8d
009F94AB  33 D2                           xor edx, edx
009F94AD  48 8D 0D FC DB 5C 00            lea rcx, [rip + 0x5cdbfc]
009F94B4  E8 77 6D 81 FF                  call 0x140210230
009F94B9  48 8B F8                        mov rdi, rax
009F94BC  F0 48 0F BA 2D EA DB 5C 00 00   lock bts qword ptr [rip + 0x5cdbea], 0
009F94C6  73 16                           jae 0x1409f94de
009F94C8  4C 8D 05 E1 DB 5C 00            lea r8, [rip + 0x5cdbe1]
009F94CF  48 8B D0                        mov rdx, rax
009F94D2  48 8D 0D D7 DB 5C 00            lea rcx, [rip + 0x5cdbd7]
009F94D9  E8 B2 67 81 FF                  call 0x14020fc90
009F94DE  48 85 FF                        test rdi, rdi
009F94E1  74 04                           je 0x1409f94e7
009F94E3  44 88 67 0A                     mov byte ptr [rdi + 0xa], r12b
009F94E7  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
009F94EC  F0 81 88 10 06 00 00 00 01 00 00  lock or dword ptr [rax + 0x610], 0x100
009F94F7  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F94FC  49 8D 76 28                     lea rsi, [r14 + 0x28]
009F9500  48 8B 3E                        mov rdi, qword ptr [rsi]
009F9503  48 3B FE                        cmp rdi, rsi
009F9506  74 1C                           je 0x1409f9524
009F9508  48 8D 8F A8 FC FF FF            lea rcx, [rdi - 0x358]
009F950F  8B 81 F0 01 00 00               mov eax, dword ptr [rcx + 0x1f0]
009F9515  41 84 C4                        test r12b, al
009F9518  75 05                           jne 0x1409f951f
009F951A  E8 19 B6 D8 FF                  call 0x140784b38
009F951F  48 8B 3F                        mov rdi, qword ptr [rdi]
009F9522  EB DF                           jmp 0x1409f9503
009F9524  8B 74 24 58                     mov esi, dword ptr [rsp + 0x58]
009F9528  49 8D 4E 38                     lea rcx, [r14 + 0x38]
009F952C  E8 DF 64 86 FF                  call 0x14025fa10
009F9531  41 84 DC                        test r12b, bl
009F9534  74 08                           je 0x1409f953e
009F9536  49 8B CE                        mov rcx, r14
009F9539  E8 C2 B6 D8 FF                  call 0x140784c00
009F953E  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
009F9546  48 85 C0                        test rax, rax
009F9549  74 08                           je 0x1409f9553
009F954B  48 8B C8                        mov rcx, rax
009F954E  E8 BD 21 E7 FF                  call 0x14086b710
009F9553  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
009F9558  48 85 C0                        test rax, rax
009F955B  0F 84 80 1A 00 00               je 0x1409fafe1
009F9561  BA 50 73 4A 61                  mov edx, 0x614a7350
009F9566  48 8B C8                        mov rcx, rax
009F9569  E8 02 93 18 00                  call 0x140b82870
009F956E  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
009F9576  E9 BE 04 00 00                  jmp 0x1409f9a39
009F957B  8B F0                           mov esi, eax
009F957D  41 BC 01 00 00 00               mov r12d, 1
009F9583  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F9588  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009F958D  E9 4F 1A 00 00                  jmp 0x1409fafe1
009F9592  49 8B FF                        mov rdi, r15
009F9595  4C 89 BC 24 80 00 00 00         mov qword ptr [rsp + 0x80], r15
009F959D  41 B8 10 00 00 00               mov r8d, 0x10
009F95A3  83 F9 0E                        cmp ecx, 0xe
009F95A6  45 0F 45 C6                     cmovne r8d, r14d
009F95AA  44 89 84 24 C0 00 00 00         mov dword ptr [rsp + 0xc0], r8d
009F95B2  33 D2                           xor edx, edx
009F95B4  41 8B C4                        mov eax, r12d
009F95B7  41 F7 F0                        div r8d
009F95BA  85 D2                           test edx, edx
009F95BC  74 18                           je 0x1409f95d6
009F95BE  BE 04 00 00 C0                  mov esi, 0xc0000004
009F95C3  41 BC 01 00 00 00               mov r12d, 1
009F95C9  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F95CE  44 8B E9                        mov r13d, ecx
009F95D1  E9 0B 1A 00 00                  jmp 0x1409fafe1
009F95D6  33 D2                           xor edx, edx
009F95D8  41 8B C4                        mov eax, r12d
009F95DB  41 F7 F0                        div r8d
009F95DE  44 8B F0                        mov r14d, eax
009F95E1  89 84 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], eax
009F95E8  41 BC 01 00 00 00               mov r12d, 1
009F95EE  48 C7 84 24 10 04 00 00 01 00 20 00  mov qword ptr [rsp + 0x410], 0x200001
009F95FA  33 D2                           xor edx, edx
009F95FC  41 B8 00 01 00 00               mov r8d, 0x100
009F9602  48 8D 8C 24 18 04 00 00         lea rcx, [rsp + 0x418]
009F960A  E8 31 D6 CC FF                  call 0x1406c6c40
009F960F  E8 EC 2F A9 FF                  call 0x14048c600
009F9614  0F B7 C8                        movzx ecx, ax
009F9617  66 41 2B CC                     sub cx, r12w
009F961B  66 89 8C 24 9A 00 00 00         mov word ptr [rsp + 0x9a], cx
009F9623  8B 5C 24 50                     mov ebx, dword ptr [rsp + 0x50]
009F9627  45 85 F6                        test r14d, r14d
009F962A  0F 84 E0 00 00 00               je 0x1409f9710
009F9630  83 FB 0E                        cmp ebx, 0xe
009F9633  75 29                           jne 0x1409f965e
009F9635  41 0F 10 45 00                  movups xmm0, xmmword ptr [r13]
009F963A  0F 11 84 24 38 01 00 00         movups xmmword ptr [rsp + 0x138], xmm0
009F9642  66 0F C5 C0 04                  pextrw eax, xmm0, 4
009F9647  66 89 44 24 6C                  mov word ptr [rsp + 0x6c], ax
009F964C  66 0F D6 84 24 10 01 00 00      movq qword ptr [rsp + 0x110], xmm0
009F9655  48 8D 15 A4 69 60 FF            lea rdx, [rip - 0x9f965c]
009F965C  EB 2F                           jmp 0x1409f968d
009F965E  41 0F B7 45 00                  movzx eax, word ptr [r13]
009F9663  66 89 44 24 6C                  mov word ptr [rsp + 0x6c], ax
009F9668  66 3B C1                        cmp ax, cx
009F966B  0F 87 96 00 00 00               ja 0x1409f9707
009F9671  48 8D 15 88 69 60 FF            lea rdx, [rip - 0x9f9678]
009F9678  48 8B 84 C2 28 71 FC 00         mov rax, qword ptr [rdx + rax*8 + 0xfc7128]
009F9680  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
009F9688  0F B7 44 24 6C                  movzx eax, word ptr [rsp + 0x6c]
009F968D  66 3B C1                        cmp ax, cx
009F9690  77 75                           ja 0x1409f9707
009F9692  0F B7 C0                        movzx eax, ax
009F9695  4C 39 BC C4 18 04 00 00         cmp qword ptr [rsp + rax*8 + 0x418], r15
009F969D  75 68                           jne 0x1409f9707
009F969F  48 8B 84 C2 28 71 FC 00         mov rax, qword ptr [rdx + rax*8 + 0xfc7128]
009F96A7  4C 8B 84 24 10 01 00 00         mov r8, qword ptr [rsp + 0x110]
009F96AF  49 23 C0                        and rax, r8
009F96B2  4C 3B C0                        cmp r8, rax
009F96B5  75 50                           jne 0x1409f9707
009F96B7  0F B7 54 24 6C                  movzx edx, word ptr [rsp + 0x6c]
009F96BC  48 8D 8C 24 10 04 00 00         lea rcx, [rsp + 0x410]
009F96C4  E8 F7 1F 86 FF                  call 0x14025b6c0
009F96C9  44 8B B4 24 D0 00 00 00         mov r14d, dword ptr [rsp + 0xd0]
009F96D1  41 FF CE                        dec r14d
009F96D4  44 89 B4 24 D0 00 00 00         mov dword ptr [rsp + 0xd0], r14d
009F96DC  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
009F96E3  4C 8B AC 24 C8 00 00 00         mov r13, qword ptr [rsp + 0xc8]
009F96EB  4C 03 E8                        add r13, rax
009F96EE  4C 89 AC 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r13
009F96F6  8B 74 24 58                     mov esi, dword ptr [rsp + 0x58]
009F96FA  0F B7 8C 24 9A 00 00 00         movzx ecx, word ptr [rsp + 0x9a]
009F9702  E9 20 FF FF FF                  jmp 0x1409f9627
009F9707  BE 0D 00 00 C0                  mov esi, 0xc000000d
009F970C  89 74 24 58                     mov dword ptr [rsp + 0x58], esi
009F9710  44 8B EB                        mov r13d, ebx
009F9713  BB 02 00 00 00                  mov ebx, 2
009F9718  EB 29                           jmp 0x1409f9743
009F971A  8B F0                           mov esi, eax
009F971C  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
009F9720  45 33 FF                        xor r15d, r15d
009F9723  41 8D 5F 02                     lea ebx, [r15 + 2]
009F9727  45 8D 67 01                     lea r12d, [r15 + 1]
009F972B  41 8B FF                        mov edi, r15d
009F972E  8A 44 24 68                     mov al, byte ptr [rsp + 0x68]
009F9732  88 44 24 48                     mov byte ptr [rsp + 0x48], al
009F9736  4C 89 BC 24 80 00 00 00         mov qword ptr [rsp + 0x80], r15
009F973E  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009F9743  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F9748  85 F6                           test esi, esi
009F974A  0F 88 91 18 00 00               js 0x1409fafe1
009F9750  4D 39 BE 10 02 00 00            cmp qword ptr [r14 + 0x210], r15
009F9757  75 57                           jne 0x1409f97b0
009F9759  BA 28 00 00 00                  mov edx, 0x28
009F975E  B9 00 01 00 00                  mov ecx, 0x100
009F9763  41 B8 50 73 4A 61               mov r8d, 0x614a7350
009F9769  E8 82 89 18 00                  call 0x140b820f0
009F976E  48 8B F8                        mov rdi, rax
009F9771  48 85 C0                        test rax, rax
009F9774  0F 84 B6 F7 FF FF               je 0x1409f8f30
009F977A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009F9783  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
009F978A  45 33 C0                        xor r8d, r8d
009F978D  41 8D 50 28                     lea edx, [r8 + 0x28]
009F9791  E8 AA 4B FA FF                  call 0x14099e340
009F9796  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
009F979E  48 85 C0                        test rax, rax
009F97A1  75 08                           jne 0x1409f97ab
009F97A3  48 8B CF                        mov rcx, rdi
009F97A6  E9 BB F7 FF FF                  jmp 0x1409f8f66
009F97AB  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F97B0  4C 8D 84 24 E0 00 00 00         lea r8, [rsp + 0xe0]
009F97B8  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
009F97C0  48 8B 91 B8 00 00 00            mov rdx, qword ptr [rcx + 0xb8]
009F97C7  E8 C4 B4 EC FF                  call 0x1408c4c90
009F97CC  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
009F97D4  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
009F97DC  44 38 7C 24 48                  cmp byte ptr [rsp + 0x48], r15b
009F97E1  74 5A                           je 0x1409f983d
009F97E3  44 89 A4 24 E0 02 00 00         mov dword ptr [rsp + 0x2e0], r12d
009F97EB  44 89 A4 24 E4 02 00 00         mov dword ptr [rsp + 0x2e4], r12d
009F97F3  48 8B 05 86 02 5E 00            mov rax, qword ptr [rip + 0x5e0286]
009F97FA  48 89 84 24 E8 02 00 00         mov qword ptr [rsp + 0x2e8], rax
009F9802  44 89 BC 24 F0 02 00 00         mov dword ptr [rsp + 0x2f0], r15d
009F980A  45 8A C4                        mov r8b, r12b
009F980D  48 8D 94 24 E0 00 00 00         lea rdx, [rsp + 0xe0]
009F9815  48 8D 8C 24 E0 02 00 00         lea rcx, [rsp + 0x2e0]
009F981D  E8 4E 16 FC FF                  call 0x1409bae70
009F9822  0F B6 C8                        movzx ecx, al
009F9825  41 23 CC                        and ecx, r12d
009F9828  8B 84 24 D8 00 00 00            mov eax, dword ptr [rsp + 0xd8]
009F982F  83 E0 FE                        and eax, 0xfffffffe
009F9832  0B C8                           or ecx, eax
009F9834  89 8C 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], ecx
009F983B  EB 08                           jmp 0x1409f9845
009F983D  44 09 A4 24 D8 00 00 00         or dword ptr [rsp + 0xd8], r12d
009F9845  49 8D 4E 38                     lea rcx, [r14 + 0x38]
009F9849  41 8A D4                        mov dl, r12b
009F984C  E8 CF B5 81 FF                  call 0x140214e20
009F9851  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
009F9856  48 8D 84 24 D8 00 00 00         lea rax, [rsp + 0xd8]
009F985E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009F9863  4C 8D 0D F6 BB D8 FF            lea r9, [rip - 0x27440a]
009F986A  45 33 C0                        xor r8d, r8d
009F986D  33 D2                           xor edx, edx
009F986F  49 8B CE                        mov rcx, r14
009F9872  E8 75 09 F2 FF                  call 0x14091a1ec
009F9877  8B F0                           mov esi, eax
009F9879  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
009F987D  85 C0                           test eax, eax
009F987F  0F 88 78 01 00 00               js 0x1409f99fd
009F9885  49 8B 86 10 02 00 00            mov rax, qword ptr [r14 + 0x210]
009F988C  48 85 C0                        test rax, rax
009F988F  75 23                           jne 0x1409f98b4
009F9891  49 89 BE 10 02 00 00            mov qword ptr [r14 + 0x210], rdi
009F9898  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
009F98A0  49 89 86 18 02 00 00            mov qword ptr [r14 + 0x218], rax
009F98A7  49 8B FF                        mov rdi, r15
009F98AA  4C 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], r15
009F98B2  EB 28                           jmp 0x1409f98dc
009F98B4  0F 10 40 08                     movups xmm0, xmmword ptr [rax + 8]
009F98B8  0F 11 84 24 68 01 00 00         movups xmmword ptr [rsp + 0x168], xmm0
009F98C0  0F 10 48 18                     movups xmm1, xmmword ptr [rax + 0x18]
009F98C4  0F 11 8C 24 78 01 00 00         movups xmmword ptr [rsp + 0x178], xmm1
009F98CC  48 8D 84 24 68 01 00 00         lea rax, [rsp + 0x168]
009F98D4  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
009F98DC  49 8B 86 10 02 00 00            mov rax, qword ptr [r14 + 0x210]
009F98E3  0F 10 84 24 D8 00 00 00         movups xmm0, xmmword ptr [rsp + 0xd8]
009F98EB  0F 11 00                        movups xmmword ptr [rax], xmm0
009F98EE  0F 10 8C 24 E8 00 00 00         movups xmm1, xmmword ptr [rsp + 0xe8]
009F98F6  0F 11 48 10                     movups xmmword ptr [rax + 0x10], xmm1
009F98FA  F2 0F 10 84 24 F8 00 00 00      movsd xmm0, qword ptr [rsp + 0xf8]
009F9903  F2 0F 11 40 20                  movsd qword ptr [rax + 0x20], xmm0
009F9908  4C 89 B4 24 00 01 00 00         mov qword ptr [rsp + 0x100], r14
009F9910  41 8B 86 00 01 00 00            mov eax, dword ptr [r14 + 0x100]
009F9917  89 84 24 0C 01 00 00            mov dword ptr [rsp + 0x10c], eax
009F991E  BE EF FF FF FF                  mov esi, 0xffffffef
009F9923  89 B4 24 08 01 00 00            mov dword ptr [rsp + 0x108], esi
009F992A  49 8D 8E 08 01 00 00            lea rcx, [r14 + 0x108]
009F9931  48 8B D1                        mov rdx, rcx
009F9934  48 8D 84 24 10 04 00 00         lea rax, [rsp + 0x410]
009F993C  4C 8B C3                        mov r8, rbx
009F993F  41 B9 80 00 00 00               mov r9d, 0x80
009F9945  0F 10 00                        movups xmm0, xmmword ptr [rax]
009F9948  0F 11 02                        movups xmmword ptr [rdx], xmm0
009F994B  0F 10 48 10                     movups xmm1, xmmword ptr [rax + 0x10]
009F994F  0F 11 4A 10                     movups xmmword ptr [rdx + 0x10], xmm1
009F9953  0F 10 40 20                     movups xmm0, xmmword ptr [rax + 0x20]
009F9957  0F 11 42 20                     movups xmmword ptr [rdx + 0x20], xmm0
009F995B  0F 10 48 30                     movups xmm1, xmmword ptr [rax + 0x30]
009F995F  0F 11 4A 30                     movups xmmword ptr [rdx + 0x30], xmm1
009F9963  0F 10 40 40                     movups xmm0, xmmword ptr [rax + 0x40]
009F9967  0F 11 42 40                     movups xmmword ptr [rdx + 0x40], xmm0
009F996B  0F 10 48 50                     movups xmm1, xmmword ptr [rax + 0x50]
009F996F  0F 11 4A 50                     movups xmmword ptr [rdx + 0x50], xmm1
009F9973  0F 10 40 60                     movups xmm0, xmmword ptr [rax + 0x60]
009F9977  0F 11 42 60                     movups xmmword ptr [rdx + 0x60], xmm0
009F997B  49 03 D1                        add rdx, r9
009F997E  0F 10 48 70                     movups xmm1, xmmword ptr [rax + 0x70]
009F9982  0F 11 4A F0                     movups xmmword ptr [rdx - 0x10], xmm1
009F9986  49 03 C1                        add rax, r9
009F9989  49 83 E8 01                     sub r8, 1
009F998D  75 B6                           jne 0x1409f9945
009F998F  48 8B 00                        mov rax, qword ptr [rax]
009F9992  48 89 02                        mov qword ptr [rdx], rax
009F9995  41 83 FD 0E                     cmp r13d, 0xe
009F9999  75 1B                           jne 0x1409f99b6
009F999B  E8 E0 7B 8D FF                  call 0x1402d1580
009F99A0  85 C0                           test eax, eax
009F99A2  74 12                           je 0x1409f99b6
009F99A4  41 21 B6 00 01 00 00            and dword ptr [r14 + 0x100], esi
009F99AB  F0 41 83 A6 10 06 00 00 FD      lock and dword ptr [r14 + 0x610], 0xfffffffd
009F99B4  EB 10                           jmp 0x1409f99c6
009F99B6  41 83 8E 00 01 00 00 10         or dword ptr [r14 + 0x100], 0x10
009F99BE  F0 41 09 9E 10 06 00 00         lock or dword ptr [r14 + 0x610], ebx
009F99C6  C7 44 24 28 05 00 00 00         mov dword ptr [rsp + 0x28], 5
009F99CE  48 8D 84 24 00 01 00 00         lea rax, [rsp + 0x100]
009F99D6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009F99DB  4C 8D 0D 3E D8 05 00            lea r9, [rip + 0x5d83e]
009F99E2  45 33 C0                        xor r8d, r8d
009F99E5  48 8D 15 D4 4C E8 FF            lea rdx, [rip - 0x17b32c]
009F99EC  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F99F1  49 8B CE                        mov rcx, r14
009F99F4  E8 F3 07 F2 FF                  call 0x14091a1ec
009F99F9  8B 74 24 58                     mov esi, dword ptr [rsp + 0x58]
009F99FD  49 8D 4E 38                     lea rcx, [r14 + 0x38]
009F9A01  E8 0A 60 86 FF                  call 0x14025fa10
009F9A06  48 8B 84 24 90 00 00 00         mov rax, qword ptr [rsp + 0x90]
009F9A0E  48 85 C0                        test rax, rax
009F9A11  74 08                           je 0x1409f9a1b
009F9A13  48 8B C8                        mov rcx, rax
009F9A16  E8 F5 1C E7 FF                  call 0x14086b710
009F9A1B  48 85 FF                        test rdi, rdi
009F9A1E  0F 84 BD 15 00 00               je 0x1409fafe1
009F9A24  BA 50 73 4A 61                  mov edx, 0x614a7350
009F9A29  48 8B CF                        mov rcx, rdi
009F9A2C  E8 3F 8E 18 00                  call 0x140b82870
009F9A31  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
009F9A39  BA 28 00 00 00                  mov edx, 0x28
009F9A3E  45 33 C0                        xor r8d, r8d
009F9A41  E8 EA 31 EC FF                  call 0x1408bcc30
009F9A46  E9 96 15 00 00                  jmp 0x1409fafe1
009F9A4B  83 E9 0F                        sub ecx, 0xf
009F9A4E  0F 84 63 03 00 00               je 0x1409f9db7
009F9A54  83 E9 01                        sub ecx, 1
009F9A57  0F 84 EF 02 00 00               je 0x1409f9d4c
009F9A5D  41 2B CE                        sub ecx, r14d
009F9A60  0F 84 49 02 00 00               je 0x1409f9caf
009F9A66  83 E9 03                        sub ecx, 3
009F9A69  0F 84 F4 01 00 00               je 0x1409f9c63
009F9A6F  83 E9 01                        sub ecx, 1
009F9A72  0F 84 13 01 00 00               je 0x1409f9b8b
009F9A78  83 E9 01                        sub ecx, 1
009F9A7B  0F 84 9F 00 00 00               je 0x1409f9b20
009F9A81  83 F9 01                        cmp ecx, 1
009F9A84  0F 85 94 11 00 00               jne 0x1409fac1e
009F9A8A  49 8B 75 00                     mov rsi, qword ptr [r13]
009F9A8E  48 89 B4 24 E0 01 00 00         mov qword ptr [rsp + 0x1e0], rsi
009F9A96  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F9A9B  41 BC 01 00 00 00               mov r12d, 1
009F9AA1  41 8A D4                        mov dl, r12b
009F9AA4  49 8D 4E 38                     lea rcx, [r14 + 0x38]
009F9AA8  E8 73 B3 81 FF                  call 0x140214e20
009F9AAD  41 8B 86 10 06 00 00            mov eax, dword ptr [r14 + 0x610]
009F9AB4  41 8D 4C 24 1F                  lea ecx, [r12 + 0x1f]
009F9AB9  84 C1                           test cl, al
009F9ABB  75 0A                           jne 0x1409f9ac7
009F9ABD  BE 0D 00 00 C0                  mov esi, 0xc000000d
009F9AC2  E9 D6 EF FF FF                  jmp 0x1409f8a9d
009F9AC7  49 8B BE D8 04 00 00            mov rdi, qword ptr [r14 + 0x4d8]
009F9ACE  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
009F9AD1  A8 10                           test al, 0x10
009F9AD3  75 19                           jne 0x1409f9aee
009F9AD5  83 C8 10                        or eax, 0x10
009F9AD8  89 47 28                        mov dword ptr [rdi + 0x28], eax
009F9ADB  4D 8B C6                        mov r8, r14
009F9ADE  48 8D 15 9B 9E BE FF            lea rdx, [rip - 0x416165]
009F9AE5  48 8D 4F 30                     lea rcx, [rdi + 0x30]
009F9AE9  E8 E2 20 A6 FF                  call 0x14045bbd0
009F9AEE  48 8D 8F 80 00 00 00            lea rcx, [rdi + 0x80]
009F9AF5  4C 8B C6                        mov r8, rsi
009F9AF8  48 8D 57 30                     lea rdx, [rdi + 0x30]
009F9AFC  E8 23 F1 BC FF                  call 0x1405c8c24
009F9B01  41 8B F7                        mov esi, r15d
009F9B04  E9 94 EF FF FF                  jmp 0x1409f8a9d
009F9B09  8B F0                           mov esi, eax
009F9B0B  41 BC 01 00 00 00               mov r12d, 1
009F9B11  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F9B16  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009F9B1B  E9 C1 14 00 00                  jmp 0x1409fafe1
009F9B20  41 BC 01 00 00 00               mov r12d, 1
009F9B26  45 38 65 00                     cmp byte ptr [r13], r12b
009F9B2A  74 18                           je 0x1409f9b44
009F9B2C  BE 0D 00 00 C0                  mov esi, 0xc000000d
009F9B31  89 74 24 58                     mov dword ptr [rsp + 0x58], esi
009F9B35  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F9B3A  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
009F9B3F  E9 9D 14 00 00                  jmp 0x1409fafe1
009F9B44  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
009F9B49  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
009F9B4E  4C 8D 0D 1B 3D 0A 00            lea r9, [rip + 0xa3d1b]
009F9B55  4C 8D 05 74 9C 0A 00            lea r8, [rip + 0xa9c74]
009F9B5C  33 D2                           xor edx, edx
009F9B5E  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F9B63  49 8B CE                        mov rcx, r14
009F9B66  E8 81 06 F2 FF                  call 0x14091a1ec
009F9B6B  E9 E6 05 00 00                  jmp 0x1409fa156
009F9B70  8B F0                           mov esi, eax
009F9B72  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
009F9B76  41 BC 01 00 00 00               mov r12d, 1
009F9B7C  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F9B81  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009F9B86  E9 56 14 00 00                  jmp 0x1409fafe1
009F9B8B  41 8A 45 00                     mov al, byte ptr [r13]
009F9B8F  88 44 24 5C                     mov byte ptr [rsp + 0x5c], al
009F9B93  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F9B98  49 8D 4E 38                     lea rcx, [r14 + 0x38]
009F9B9C  41 BC 01 00 00 00               mov r12d, 1
009F9BA2  41 8A D4                        mov dl, r12b
009F9BA5  E8 76 B2 81 FF                  call 0x140214e20
009F9BAA  41 8B 86 10 06 00 00            mov eax, dword ptr [r14 + 0x610]
009F9BB1  41 8D 4C 24 1F                  lea ecx, [r12 + 0x1f]
009F9BB6  84 C1                           test cl, al
009F9BB8  0F 84 FF FE FF FF               je 0x1409f9abd
009F9BBE  4D 8B 8E D8 04 00 00            mov r9, qword ptr [r14 + 0x4d8]
009F9BC5  41 8B 51 28                     mov edx, dword ptr [r9 + 0x28]
009F9BC9  F6 C2 40                        test dl, 0x40
009F9BCC  0F 85 EB FE FF FF               jne 0x1409f9abd
009F9BD2  F6 C2 21                        test dl, 0x21
009F9BD5  75 6B                           jne 0x1409f9c42
009F9BD7  8B CA                           mov ecx, edx
009F9BD9  C1 E9 03                        shr ecx, 3
009F9BDC  41 23 CC                        and ecx, r12d
009F9BDF  41 8B C7                        mov eax, r15d
009F9BE2  44 8A 44 24 5C                  mov r8b, byte ptr [rsp + 0x5c]
009F9BE7  45 84 C0                        test r8b, r8b
009F9BEA  0F 95 C0                        setne al
009F9BED  3B C8                           cmp ecx, eax
009F9BEF  0F 84 C8 FE FF FF               je 0x1409f9abd
009F9BF5  41 F6 D8                        neg r8b
009F9BF8  1B C0                           sbb eax, eax
009F9BFA  83 E0 08                        and eax, 8
009F9BFD  83 E2 F7                        and edx, 0xfffffff7
009F9C00  0B D0                           or edx, eax
009F9C02  41 89 51 28                     mov dword ptr [r9 + 0x28], edx
009F9C06  49 8B 8E D8 04 00 00            mov rcx, qword ptr [r14 + 0x4d8]
009F9C0D  48 83 E9 80                     sub rcx, -0x80
009F9C11  8A 54 24 5C                     mov dl, byte ptr [rsp + 0x5c]
009F9C15  E8 5A 3F A7 FF                  call 0x14046db74
009F9C1A  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
009F9C1F  48 8D 44 24 5C                  lea rax, [rsp + 0x5c]
009F9C24  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009F9C29  4C 8D 0D 30 E0 AA FF            lea r9, [rip - 0x551fd0]
009F9C30  45 33 C0                        xor r8d, r8d
009F9C33  33 D2                           xor edx, edx
009F9C35  49 8B CE                        mov rcx, r14
009F9C38  E8 AF 05 F2 FF                  call 0x14091a1ec
009F9C3D  E9 BF FE FF FF                  jmp 0x1409f9b01
009F9C42  BE BB 00 00 C0                  mov esi, 0xc00000bb
009F9C47  E9 51 EE FF FF                  jmp 0x1409f8a9d
009F9C4C  8B F0                           mov esi, eax
009F9C4E  41 BC 01 00 00 00               mov r12d, 1
009F9C54  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F9C59  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009F9C5E  E9 7E 13 00 00                  jmp 0x1409fafe1
009F9C63  41 8A 55 00                     mov dl, byte ptr [r13]
009F9C67  88 94 24 98 00 00 00            mov byte ptr [rsp + 0x98], dl
009F9C6E  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F9C73  49 8B CE                        mov rcx, r14
009F9C76  E8 75 60 07 00                  call 0x140a6fcf0
009F9C7B  8B F0                           mov esi, eax
009F9C7D  41 BC 01 00 00 00               mov r12d, 1
009F9C83  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
009F9C88  85 C0                           test eax, eax
009F9C8A  0F 88 51 13 00 00               js 0x1409fafe1
009F9C90  41 8B F7                        mov esi, r15d
009F9C93  E9 49 13 00 00                  jmp 0x1409fafe1
009F9C98  8B F0                           mov esi, eax
009F9C9A  41 BC 01 00 00 00               mov r12d, 1
009F9CA0  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F9CA5  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009F9CAA  E9 32 13 00 00                  jmp 0x1409fafe1
009F9CAF  41 0F 10 45 00                  movups xmm0, xmmword ptr [r13]
009F9CB4  F3 0F 7F 84 24 F8 02 00 00      movdqu xmmword ptr [rsp + 0x2f8], xmm0
009F9CBD  8B 84 24 F8 02 00 00            mov eax, dword ptr [rsp + 0x2f8]
009F9CC4  85 C0                           test eax, eax
009F9CC6  0F 84 C7 07 00 00               je 0x1409fa493
009F9CCC  A9 F0 FF FF FF                  test eax, 0xfffffff0
009F9CD1  0F 85 BC 07 00 00               jne 0x1409fa493
009F9CD7  41 BC 01 00 00 00               mov r12d, 1
009F9CDD  41 84 C4                        test r12b, al
009F9CE0  75 08                           jne 0x1409f9cea
009F9CE2  A8 08                           test al, 8
009F9CE4  0F 85 1A 10 00 00               jne 0x1409fad04
009F9CEA  48 8D 94 24 F8 02 00 00         lea rdx, [rsp + 0x2f8]
009F9CF2  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F9CF7  49 8B CE                        mov rcx, r14
009F9CFA  E8 75 13 00 00                  call 0x1409fb074
009F9CFF  8B F0                           mov esi, eax
009F9D01  85 C0                           test eax, eax
009F9D03  0F 88 BF 12 00 00               js 0x1409fafc8
009F9D09  8B 84 24 F8 02 00 00            mov eax, dword ptr [rsp + 0x2f8]
009F9D10  41 89 45 00                     mov dword ptr [r13], eax
009F9D14  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
009F9D19  E9 C3 12 00 00                  jmp 0x1409fafe1
009F9D1E  8B F0                           mov esi, eax
009F9D20  41 BC 01 00 00 00               mov r12d, 1
009F9D26  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F9D2B  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009F9D30  E9 AC 12 00 00                  jmp 0x1409fafe1
009F9D35  8B F0                           mov esi, eax
009F9D37  41 BC 01 00 00 00               mov r12d, 1
009F9D3D  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F9D42  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009F9D47  E9 95 12 00 00                  jmp 0x1409fafe1
009F9D4C  41 8B 7D 00                     mov edi, dword ptr [r13]
009F9D50  89 BC 24 5C 01 00 00            mov dword ptr [rsp + 0x15c], edi
009F9D57  41 BC 01 00 00 00               mov r12d, 1
009F9D5D  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F9D62  F7 C7 01 C0 FF FF               test edi, 0xffffc001
009F9D68  0F 85 D5 0F 00 00               jne 0x1409fad43
009F9D6E  41 8A D4                        mov dl, r12b
009F9D71  49 8D 4E 38                     lea rcx, [r14 + 0x38]
009F9D75  E8 A6 B0 81 FF                  call 0x140214e20
009F9D7A  45 33 C0                        xor r8d, r8d
009F9D7D  33 D2                           xor edx, edx
009F9D7F  49 8B CE                        mov rcx, r14
009F9D82  E8 09 CC F1 FF                  call 0x140916990
009F9D87  41 89 BE 50 04 00 00            mov dword ptr [r14 + 0x450], edi
009F9D8E  45 33 C0                        xor r8d, r8d
009F9D91  33 D2                           xor edx, edx
009F9D93  49 8B CE                        mov rcx, r14
009F9D96  E8 F5 35 E8 FF                  call 0x14087d390
009F9D9B  E9 AD 03 00 00                  jmp 0x1409fa14d
009F9DA0  8B F0                           mov esi, eax
009F9DA2  41 BC 01 00 00 00               mov r12d, 1
009F9DA8  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F9DAD  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009F9DB2  E9 2A 12 00 00                  jmp 0x1409fafe1
009F9DB7  4D 8B C4                        mov r8, r12
009F9DBA  49 8B D5                        mov rdx, r13
009F9DBD  48 8D 8C 24 28 01 00 00         lea rcx, [rsp + 0x128]
009F9DC5  E8 76 CA CC FF                  call 0x1406c6840
009F9DCA  90                              nop
009F9DCB  48 8B 9C 24 28 01 00 00         mov rbx, qword ptr [rsp + 0x128]
009F9DD3  41 BC 01 00 00 00               mov r12d, 1
009F9DD9  F7 C3 C0 FF FF FF               test ebx, 0xffffffc0
009F9DDF  0F 85 1F 0F 00 00               jne 0x1409fad04
009F9DE5  44 89 7C 24 60                  mov dword ptr [rsp + 0x60], r15d
009F9DEA  8B B4 24 2C 01 00 00            mov esi, dword ptr [rsp + 0x12c]
009F9DF1  89 74 24 70                     mov dword ptr [rsp + 0x70], esi
009F9DF5  41 84 DC                        test r12b, bl
009F9DF8  74 6F                           je 0x1409f9e69
009F9DFA  41 84 DE                        test r14b, bl
009F9DFD  74 17                           je 0x1409f9e16
009F9DFF  F6 C3 10                        test bl, 0x10
009F9E02  0F 85 FC 0E 00 00               jne 0x1409fad04
009F9E08  8D 46 FF                        lea eax, [rsi - 1]
009F9E0B  83 F8 08                        cmp eax, 8
009F9E0E  0F 87 F0 0E 00 00               ja 0x1409fad04
009F9E14  EB 40                           jmp 0x1409f9e56
009F9E16  F6 C3 10                        test bl, 0x10
009F9E19  74 2D                           je 0x1409f9e48
009F9E1B  F6 C3 04                        test bl, 4
009F9E1E  0F 85 E0 0E 00 00               jne 0x1409fad04
009F9E24  66 41 3B F4                     cmp si, r12w
009F9E28  0F 82 D6 0E 00 00               jb 0x1409fad04
009F9E2E  8B C6                           mov eax, esi
009F9E30  C1 E8 10                        shr eax, 0x10
009F9E33  66 3B F0                        cmp si, ax
009F9E36  0F 87 C8 0E 00 00               ja 0x1409fad04
009F9E3C  41 BD 10 27 00 00               mov r13d, 0x2710
009F9E42  66 41 3B C5                     cmp ax, r13w
009F9E46  EB C6                           jmp 0x1409f9e0e
009F9E48  8D 46 FF                        lea eax, [rsi - 1]
009F9E4B  3D 0F 27 00 00                  cmp eax, 0x270f
009F9E50  0F 87 AE 0E 00 00               ja 0x1409fad04
009F9E56  BF 20 00 00 00                  mov edi, 0x20
009F9E5B  40 84 DF                        test dil, bl
009F9E5E  74 0E                           je 0x1409f9e6e
009F9E60  8D 47 E8                        lea eax, [rdi - 0x18]
009F9E63  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
009F9E67  EB 05                           jmp 0x1409f9e6e
009F9E69  BF 20 00 00 00                  mov edi, 0x20
009F9E6E  45 33 C0                        xor r8d, r8d
009F9E71  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
009F9E79  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F9E7E  49 8B CE                        mov rcx, r14
009F9E81  E8 4A 3C E8 FF                  call 0x14087dad0
009F9E86  41 8B 86 10 06 00 00            mov eax, dword ptr [r14 + 0x610]
009F9E8D  41 84 DC                        test r12b, bl
009F9E90  74 2E                           je 0x1409f9ec0
009F9E92  41 BD 02 00 00 00               mov r13d, 2
009F9E98  40 84 C7                        test dil, al
009F9E9B  75 38                           jne 0x1409f9ed5
009F9E9D  41 8B CD                        mov ecx, r13d
009F9EA0  E8 63 43 FA FF                  call 0x14099e208
009F9EA5  48 8B C8                        mov rcx, rax
009F9EA8  48 85 C0                        test rax, rax
009F9EAB  75 0A                           jne 0x1409f9eb7
009F9EAD  BE 9A 00 00 C0                  mov esi, 0xc000009a
009F9EB2  E9 4B 02 00 00                  jmp 0x1409fa102
009F9EB7  49 89 86 D8 04 00 00            mov qword ptr [r14 + 0x4d8], rax
009F9EBE  EB 18                           jmp 0x1409f9ed8
009F9EC0  40 84 C7                        test dil, al
009F9EC3  75 0A                           jne 0x1409f9ecf
009F9EC5  BE 0D 00 00 C0                  mov esi, 0xc000000d
009F9ECA  E9 33 02 00 00                  jmp 0x1409fa102
009F9ECF  41 BD 02 00 00 00               mov r13d, 2
009F9ED5  49 8B CF                        mov rcx, r15
009F9ED8  49 8B 86 D8 04 00 00            mov rax, qword ptr [r14 + 0x4d8]
009F9EDF  44 89 78 28                     mov dword ptr [rax + 0x28], r15d
009F9EE3  49 8B 86 D8 04 00 00            mov rax, qword ptr [r14 + 0x4d8]
009F9EEA  89 70 2C                        mov dword ptr [rax + 0x2c], esi
009F9EED  41 84 DC                        test r12b, bl
009F9EF0  0F 84 3A 01 00 00               je 0x1409fa030
009F9EF6  F6 C3 04                        test bl, 4
009F9EF9  74 10                           je 0x1409f9f0b
009F9EFB  49 8B 86 D8 04 00 00            mov rax, qword ptr [r14 + 0x4d8]
009F9F02  44 09 60 28                     or dword ptr [rax + 0x28], r12d
009F9F06  66 89 74 24 72                  mov word ptr [rsp + 0x72], si
009F9F0B  41 84 DD                        test r13b, bl
009F9F0E  74 18                           je 0x1409f9f28
009F9F10  49 8B 86 D8 04 00 00            mov rax, qword ptr [r14 + 0x4d8]
009F9F17  83 48 28 04                     or dword ptr [rax + 0x28], 4
009F9F1B  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
009F9F1F  83 E0 FE                        and eax, 0xfffffffe
009F9F22  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
009F9F26  EB 1A                           jmp 0x1409f9f42
009F9F28  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
009F9F2C  41 0B C4                        or eax, r12d
009F9F2F  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
009F9F33  F6 C3 14                        test bl, 0x14
009F9F36  75 0A                           jne 0x1409f9f42
009F9F38  B8 10 27 00 00                  mov eax, 0x2710
009F9F3D  66 89 44 24 72                  mov word ptr [rsp + 0x72], ax
009F9F42  F6 C3 08                        test bl, 8
009F9F45  74 0B                           je 0x1409f9f52
009F9F47  49 8B 86 D8 04 00 00            mov rax, qword ptr [r14 + 0x4d8]
009F9F4E  44 09 68 28                     or dword ptr [rax + 0x28], r13d
009F9F52  F6 C3 10                        test bl, 0x10
009F9F55  74 0A                           je 0x1409f9f61
009F9F57  49 8B 86 D8 04 00 00            mov rax, qword ptr [r14 + 0x4d8]
009F9F5E  09 78 28                        or dword ptr [rax + 0x28], edi
009F9F61  40 84 DF                        test dil, bl
009F9F64  74 11                           je 0x1409f9f77
009F9F66  49 8B 86 D8 04 00 00            mov rax, qword ptr [r14 + 0x4d8]
009F9F6D  41 B8 80 00 00 00               mov r8d, 0x80
009F9F73  44 09 40 28                     or dword ptr [rax + 0x28], r8d
009F9F77  49 8B 86 D8 04 00 00            mov rax, qword ptr [r14 + 0x4d8]
009F9F7E  48 8D 90 80 00 00 00            lea rdx, [rax + 0x80]
009F9F85  48 3B C1                        cmp rax, rcx
009F9F88  75 54                           jne 0x1409f9fde
009F9F8A  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
009F9F8F  48 89 02                        mov qword ptr [rdx], rax
009F9F92  49 8B D6                        mov rdx, r14
009F9F95  49 8B 8E 18 05 00 00            mov rcx, qword ptr [r14 + 0x518]
009F9F9C  E8 BB 3E FA FF                  call 0x14099de5c
009F9FA1  8B F0                           mov esi, eax
009F9FA3  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
009F9FA7  85 C0                           test eax, eax
009F9FA9  78 0F                           js 0x1409f9fba
009F9FAB  F0 41 09 BE 10 06 00 00         lock or dword ptr [r14 + 0x610], edi
009F9FB3  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009F9FB8  EB 4F                           jmp 0x1409fa009
009F9FBA  49 8B 8E D8 04 00 00            mov rcx, qword ptr [r14 + 0x4d8]
009F9FC1  48 85 C9                        test rcx, rcx
009F9FC4  0F 84 38 01 00 00               je 0x1409fa102
009F9FCA  41 8B D5                        mov edx, r13d
009F9FCD  E8 EA 41 FA FF                  call 0x14099e1bc
009F9FD2  4D 89 BE D8 04 00 00            mov qword ptr [r14 + 0x4d8], r15
009F9FD9  E9 24 01 00 00                  jmp 0x1409fa102
009F9FDE  48 89 94 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rdx
009F9FE6  8B 40 28                        mov eax, dword ptr [rax + 0x28]
009F9FE9  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
009F9FEE  48 8D 94 24 B0 00 00 00         lea rdx, [rsp + 0xb0]
009F9FF6  A8 04                           test al, 4
009F9FF8  74 0A                           je 0x1409fa004
009F9FFA  41 8B CC                        mov ecx, r12d
009F9FFD  E8 22 30 A7 FF                  call 0x14046d024
009FA002  EB 05                           jmp 0x1409fa009
009FA004  E8 53 3E A7 FF                  call 0x14046de5c
009FA009  49 8B 86 D8 04 00 00            mov rax, qword ptr [r14 + 0x4d8]
009FA010  8B 48 28                        mov ecx, dword ptr [rax + 0x28]
009FA013  89 8C 24 18 01 00 00            mov dword ptr [rsp + 0x118], ecx
009FA01A  49 8B 86 D8 04 00 00            mov rax, qword ptr [r14 + 0x4d8]
009FA021  8B 48 2C                        mov ecx, dword ptr [rax + 0x2c]
009FA024  89 8C 24 1C 01 00 00            mov dword ptr [rsp + 0x11c], ecx
009FA02B  E9 A0 00 00 00                  jmp 0x1409fa0d0
009FA030  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
009FA034  83 C8 03                        or eax, 3
009FA037  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
009FA03B  C7 44 24 70 10 27 10 27         mov dword ptr [rsp + 0x70], 0x27102710
009FA043  49 8B 86 D8 04 00 00            mov rax, qword ptr [r14 + 0x4d8]
009FA04A  83 48 28 40                     or dword ptr [rax + 0x28], 0x40
009FA04E  49 8B 86 D8 04 00 00            mov rax, qword ptr [r14 + 0x4d8]
009FA055  8B 5C 24 70                     mov ebx, dword ptr [rsp + 0x70]
009FA059  89 58 2C                        mov dword ptr [rax + 0x2c], ebx
009FA05C  49 8B 8E D8 04 00 00            mov rcx, qword ptr [r14 + 0x4d8]
009FA063  48 83 E9 80                     sub rcx, -0x80
009FA067  48 89 8C 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], rcx
009FA06F  8B 41 04                        mov eax, dword ptr [rcx + 4]
009FA072  C1 E8 02                        shr eax, 2
009FA075  41 22 C4                        and al, r12b
009FA078  88 44 24 5D                     mov byte ptr [rsp + 0x5d], al
009FA07C  E8 63 09 A8 FF                  call 0x14047a9e4
009FA081  49 01 86 E8 04 00 00            add qword ptr [r14 + 0x4e8], rax
009FA088  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
009FA08D  48 8D 94 24 B0 00 00 00         lea rdx, [rsp + 0xb0]
009FA095  E8 C2 3D A7 FF                  call 0x14046de5c
009FA09A  89 9C 24 1C 01 00 00            mov dword ptr [rsp + 0x11c], ebx
009FA0A1  44 38 7C 24 5D                  cmp byte ptr [rsp + 0x5d], r15b
009FA0A6  74 28                           je 0x1409fa0d0
009FA0A8  44 88 7C 24 5D                  mov byte ptr [rsp + 0x5d], r15b
009FA0AD  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
009FA0B2  48 8D 44 24 5D                  lea rax, [rsp + 0x5d]
009FA0B7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009FA0BC  4C 8D 0D 9D DB AA FF            lea r9, [rip - 0x552463]
009FA0C3  45 33 C0                        xor r8d, r8d
009FA0C6  33 D2                           xor edx, edx
009FA0C8  49 8B CE                        mov rcx, r14
009FA0CB  E8 1C 01 F2 FF                  call 0x14091a1ec
009FA0D0  41 8B F7                        mov esi, r15d
009FA0D3  F7 05 23 CA 5C 00 00 00 08 00   test dword ptr [rip + 0x5cca23], 0x80000
009FA0DD  74 23                           je 0x1409fa102
009FA0DF  66 C7 44 24 28 25 07            mov word ptr [rsp + 0x28], 0x725
009FA0E6  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
009FA0EB  45 33 C9                        xor r9d, r9d
009FA0EE  4C 8D 84 24 18 01 00 00         lea r8, [rsp + 0x118]
009FA0F6  41 8D 51 0F                     lea edx, [r9 + 0xf]
009FA0FA  49 8B CE                        mov rcx, r14
009FA0FD  E8 7E 13 00 00                  call 0x1409fb480
009FA102  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
009FA10A  49 8B CE                        mov rcx, r14
009FA10D  E8 66 3B E8 FF                  call 0x14087dc78
009FA112  E9 B1 0E 00 00                  jmp 0x1409fafc8
009FA117  8B F0                           mov esi, eax
009FA119  41 BC 01 00 00 00               mov r12d, 1
009FA11F  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FA124  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009FA129  E9 B3 0E 00 00                  jmp 0x1409fafe1
009FA12E  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FA133  41 BC 01 00 00 00               mov r12d, 1
009FA139  41 8A D4                        mov dl, r12b
009FA13C  49 8D 4E 38                     lea rcx, [r14 + 0x38]
009FA140  E8 DB AC 81 FF                  call 0x140214e20
009FA145  49 8B CE                        mov rcx, r14
009FA148  E8 03 E2 84 FF                  call 0x140248350
009FA14D  49 8D 4E 38                     lea rcx, [r14 + 0x38]
009FA151  E8 BA 58 86 FF                  call 0x14025fa10
009FA156  41 8B F7                        mov esi, r15d
009FA159  E9 6A 0E 00 00                  jmp 0x1409fafc8
009FA15E  83 F9 2A                        cmp ecx, 0x2a
009FA161  0F 84 1B 09 00 00               je 0x1409faa82
009FA167  0F 8F 7A 0A 00 00               jg 0x1409fabe7
009FA16D  83 E9 1B                        sub ecx, 0x1b
009FA170  0F 84 D7 08 00 00               je 0x1409faa4d
009FA176  83 E9 04                        sub ecx, 4
009FA179  0F 84 0A 07 00 00               je 0x1409fa889
009FA17F  83 E9 01                        sub ecx, 1
009FA182  0F 84 E9 06 00 00               je 0x1409fa871
009FA188  83 E9 01                        sub ecx, 1
009FA18B  0F 84 79 E6 FF FF               je 0x1409f880a
009FA191  41 2B CE                        sub ecx, r14d
009FA194  0F 84 AE 01 00 00               je 0x1409fa348
009FA19A  41 2B CE                        sub ecx, r14d
009FA19D  0F 84 21 01 00 00               je 0x1409fa2c4
009FA1A3  83 E9 03                        sub ecx, 3
009FA1A6  0F 84 99 00 00 00               je 0x1409fa245
009FA1AC  83 F9 01                        cmp ecx, 1
009FA1AF  0F 85 69 0A 00 00               jne 0x1409fac1e
009FA1B5  45 8B 45 00                     mov r8d, dword ptr [r13]
009FA1B9  44 89 84 24 58 01 00 00         mov dword ptr [rsp + 0x158], r8d
009FA1C1  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FA1C6  49 8B CE                        mov rcx, r14
009FA1C9  E8 72 85 BE FF                  call 0x1405e2740
009FA1CE  84 C0                           test al, al
009FA1D0  0F 84 39 01 00 00               je 0x1409fa30f
009FA1D6  41 83 F8 02                     cmp r8d, 2
009FA1DA  0F 85 2F 01 00 00               jne 0x1409fa30f
009FA1E0  49 8D 5E 38                     lea rbx, [r14 + 0x38]
009FA1E4  45 8D 60 FF                     lea r12d, [r8 - 1]
009FA1E8  41 8A D4                        mov dl, r12b
009FA1EB  48 8B CB                        mov rcx, rbx
009FA1EE  E8 2D AC 81 FF                  call 0x140214e20
009FA1F3  45 39 BE B0 05 00 00            cmp dword ptr [r14 + 0x5b0], r15d
009FA1FA  74 07                           je 0x1409fa203
009FA1FC  BE 0F 05 00 C0                  mov esi, 0xc000050f
009FA201  EB 23                           jmp 0x1409fa226
009FA203  F0 41 0F BA AE 10 06 00 00 1D   lock bts dword ptr [r14 + 0x610], 0x1d
009FA20D  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FA212  73 07                           jae 0x1409fa21b
009FA214  BE FF 00 00 00                  mov esi, 0xff
009FA219  EB 0B                           jmp 0x1409fa226
009FA21B  49 8B CE                        mov rcx, r14
009FA21E  E8 1D 55 99 FF                  call 0x14038f740
009FA223  41 8B F7                        mov esi, r15d
009FA226  48 8B CB                        mov rcx, rbx
009FA229  E9 73 E8 FF FF                  jmp 0x1409f8aa1
009FA22E  8B F0                           mov esi, eax
009FA230  41 BC 01 00 00 00               mov r12d, 1
009FA236  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FA23B  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009FA240  E9 9C 0D 00 00                  jmp 0x1409fafe1
009FA245  8A 5C 24 48                     mov bl, byte ptr [rsp + 0x48]
009FA249  8A D3                           mov dl, bl
009FA24B  48 8B 0D 26 F8 5D 00            mov rcx, qword ptr [rip + 0x5df826]
009FA252  E8 C9 7B E7 FF                  call 0x140871e20
009FA257  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FA25C  84 C0                           test al, al
009FA25E  74 7D                           je 0x1409fa2dd
009FA260  41 F7 86 10 06 00 00 00 00 00 40  test dword ptr [r14 + 0x610], 0x40000000
009FA26B  0F 84 83 00 00 00               je 0x1409fa2f4
009FA271  BA 04 00 00 00                  mov edx, 4
009FA276  49 8B CE                        mov rcx, r14
009FA279  E8 3A B6 D8 FF                  call 0x1407858b8
009FA27E  84 C0                           test al, al
009FA280  0F 84 89 00 00 00               je 0x1409fa30f
009FA286  4D 8B 45 00                     mov r8, qword ptr [r13]
009FA28A  4C 89 84 24 E8 01 00 00         mov qword ptr [rsp + 0x1e8], r8
009FA292  45 8B 4D 08                     mov r9d, dword ptr [r13 + 8]
009FA296  44 89 8C 24 54 01 00 00         mov dword ptr [rsp + 0x154], r9d
009FA29E  8A D3                           mov dl, bl
009FA2A0  49 8B CE                        mov rcx, r14
009FA2A3  E8 0C 57 D8 FF                  call 0x14077f9b4
009FA2A8  E9 13 0D 00 00                  jmp 0x1409fafc0
009FA2AD  8B F0                           mov esi, eax
009FA2AF  41 BC 01 00 00 00               mov r12d, 1
009FA2B5  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FA2BA  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009FA2BF  E9 1D 0D 00 00                  jmp 0x1409fafe1
009FA2C4  8A 54 24 48                     mov dl, byte ptr [rsp + 0x48]
009FA2C8  48 8B 0D A9 F7 5D 00            mov rcx, qword ptr [rip + 0x5df7a9]
009FA2CF  E8 4C 7B E7 FF                  call 0x140871e20
009FA2D4  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FA2D9  84 C0                           test al, al
009FA2DB  75 0A                           jne 0x1409fa2e7
009FA2DD  BE 61 00 00 C0                  mov esi, 0xc0000061
009FA2E2  E9 DB 0C 00 00                  jmp 0x1409fafc2
009FA2E7  41 F7 86 10 06 00 00 00 00 00 40  test dword ptr [r14 + 0x610], 0x40000000
009FA2F2  75 0A                           jne 0x1409fa2fe
009FA2F4  BE 09 05 00 C0                  mov esi, 0xc0000509
009FA2F9  E9 C4 0C 00 00                  jmp 0x1409fafc2
009FA2FE  BA 04 00 00 00                  mov edx, 4
009FA303  49 8B CE                        mov rcx, r14
009FA306  E8 AD B5 D8 FF                  call 0x1407858b8
009FA30B  84 C0                           test al, al
009FA30D  75 0A                           jne 0x1409fa319
009FA30F  BE 0D 00 00 C0                  mov esi, 0xc000000d
009FA314  E9 A9 0C 00 00                  jmp 0x1409fafc2
009FA319  41 8B 55 00                     mov edx, dword ptr [r13]
009FA31D  89 94 24 50 01 00 00            mov dword ptr [rsp + 0x150], edx
009FA324  49 8B CE                        mov rcx, r14
009FA327  E8 08 27 E4 FF                  call 0x14083ca34
009FA32C  E9 8F 0C 00 00                  jmp 0x1409fafc0
009FA331  8B F0                           mov esi, eax
009FA333  41 BC 01 00 00 00               mov r12d, 1
009FA339  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FA33E  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009FA343  E9 99 0C 00 00                  jmp 0x1409fafe1
009FA348  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FA34D  49 8B CE                        mov rcx, r14
009FA350  E8 A7 F9 08 00                  call 0x140a89cfc
009FA355  E9 66 0C 00 00                  jmp 0x1409fafc0
009FA35A  48 8D 8C 24 08 03 00 00         lea rcx, [rsp + 0x308]
009FA362  E8 D9 C4 CC FF                  call 0x1406c6840
009FA367  4C 8B 84 24 38 03 00 00         mov r8, qword ptr [rsp + 0x338]
009FA36F  44 89 84 24 B8 02 00 00         mov dword ptr [rsp + 0x2b8], r8d
009FA377  4C 8B 94 24 08 03 00 00         mov r10, qword ptr [rsp + 0x308]
009FA37F  4C 89 94 24 90 02 00 00         mov qword ptr [rsp + 0x290], r10
009FA387  4C 8B 9C 24 10 03 00 00         mov r11, qword ptr [rsp + 0x310]
009FA38F  4C 89 9C 24 98 02 00 00         mov qword ptr [rsp + 0x298], r11
009FA397  4C 8B 8C 24 18 03 00 00         mov r9, qword ptr [rsp + 0x318]
009FA39F  4C 89 8C 24 A0 02 00 00         mov qword ptr [rsp + 0x2a0], r9
009FA3A7  48 8B 8C 24 20 03 00 00         mov rcx, qword ptr [rsp + 0x320]
009FA3AF  48 89 8C 24 C0 02 00 00         mov qword ptr [rsp + 0x2c0], rcx
009FA3B7  48 8B 94 24 28 03 00 00         mov rdx, qword ptr [rsp + 0x328]
009FA3BF  48 89 94 24 A8 02 00 00         mov qword ptr [rsp + 0x2a8], rdx
009FA3C7  8B 84 24 30 03 00 00            mov eax, dword ptr [rsp + 0x330]
009FA3CE  89 84 24 B0 02 00 00            mov dword ptr [rsp + 0x2b0], eax
009FA3D5  8B 84 24 34 03 00 00            mov eax, dword ptr [rsp + 0x334]
009FA3DC  89 84 24 B4 02 00 00            mov dword ptr [rsp + 0x2b4], eax
009FA3E3  B8 04 82 27 00                  mov eax, 0x278204
009FA3E8  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
009FA3EC  E9 8A 00 00 00                  jmp 0x1409fa47b
009FA3F1  48 8D 8C 24 40 03 00 00         lea rcx, [rsp + 0x340]
009FA3F9  E8 42 C4 CC FF                  call 0x1406c6840
009FA3FE  44 8B 84 24 68 03 00 00         mov r8d, dword ptr [rsp + 0x368]
009FA406  44 89 84 24 B8 02 00 00         mov dword ptr [rsp + 0x2b8], r8d
009FA40E  4C 8B 94 24 40 03 00 00         mov r10, qword ptr [rsp + 0x340]
009FA416  4C 89 94 24 90 02 00 00         mov qword ptr [rsp + 0x290], r10
009FA41E  4C 8B 9C 24 48 03 00 00         mov r11, qword ptr [rsp + 0x348]
009FA426  4C 89 9C 24 98 02 00 00         mov qword ptr [rsp + 0x298], r11
009FA42E  4C 8B 8C 24 50 03 00 00         mov r9, qword ptr [rsp + 0x350]
009FA436  4C 89 8C 24 A0 02 00 00         mov qword ptr [rsp + 0x2a0], r9
009FA43E  48 8B 94 24 58 03 00 00         mov rdx, qword ptr [rsp + 0x358]
009FA446  48 89 94 24 A8 02 00 00         mov qword ptr [rsp + 0x2a8], rdx
009FA44E  8B 84 24 60 03 00 00            mov eax, dword ptr [rsp + 0x360]
009FA455  89 84 24 B0 02 00 00            mov dword ptr [rsp + 0x2b0], eax
009FA45C  8B 84 24 64 03 00 00            mov eax, dword ptr [rsp + 0x364]
009FA463  89 84 24 B4 02 00 00            mov dword ptr [rsp + 0x2b4], eax
009FA46A  B8 04 02 07 00                  mov eax, 0x70204
009FA46F  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
009FA473  48 8B 8C 24 C0 02 00 00         mov rcx, qword ptr [rsp + 0x2c0]
009FA47B  F7 D0                           not eax
009FA47D  41 85 C0                        test r8d, eax
009FA480  75 11                           jne 0x1409fa493
009FA482  B8 00 10 00 00                  mov eax, 0x1000
009FA487  41 0F BA E0 0F                  bt r8d, 0xf
009FA48C  73 0F                           jae 0x1409fa49d
009FA48E  48 3B C8                        cmp rcx, rax
009FA491  73 15                           jae 0x1409fa4a8
009FA493  BE 0D 00 00 C0                  mov esi, 0xc000000d
009FA498  E9 68 E6 FF FF                  jmp 0x1409f8b05
009FA49D  49 8B CF                        mov rcx, r15
009FA4A0  48 89 8C 24 C0 02 00 00         mov qword ptr [rsp + 0x2c0], rcx
009FA4A8  41 0F BA E0 09                  bt r8d, 9
009FA4AD  73 0C                           jae 0x1409fa4bb
009FA4AF  48 3B D0                        cmp rdx, rax
009FA4B2  72 DF                           jb 0x1409fa493
009FA4B4  48 3B D1                        cmp rdx, rcx
009FA4B7  73 0A                           jae 0x1409fa4c3
009FA4B9  EB D8                           jmp 0x1409fa493
009FA4BB  4C 89 BC 24 A8 02 00 00         mov qword ptr [rsp + 0x2a8], r15
009FA4C3  41 F6 C0 04                     test r8b, 4
009FA4C7  74 07                           je 0x1409fa4d0
009FA4C9  4D 85 C9                        test r9, r9
009FA4CC  75 0A                           jne 0x1409fa4d8
009FA4CE  EB C3                           jmp 0x1409fa493
009FA4D0  4C 89 BC 24 A0 02 00 00         mov qword ptr [rsp + 0x2a0], r15
009FA4D8  41 0F BA E0 10                  bt r8d, 0x10
009FA4DD  73 07                           jae 0x1409fa4e6
009FA4DF  4D 85 D2                        test r10, r10
009FA4E2  75 0A                           jne 0x1409fa4ee
009FA4E4  EB AD                           jmp 0x1409fa493
009FA4E6  4C 89 BC 24 90 02 00 00         mov qword ptr [rsp + 0x290], r15
009FA4EE  41 0F BA E0 11                  bt r8d, 0x11
009FA4F3  73 07                           jae 0x1409fa4fc
009FA4F5  4D 85 DB                        test r11, r11
009FA4F8  75 0A                           jne 0x1409fa504
009FA4FA  EB 97                           jmp 0x1409fa493
009FA4FC  4C 89 BC 24 98 02 00 00         mov qword ptr [rsp + 0x298], r15
009FA504  41 8B D7                        mov edx, r15d
009FA507  41 BC 01 00 00 00               mov r12d, 1
009FA50D  83 FA 03                        cmp edx, 3
009FA510  7D 68                           jge 0x1409fa57a
009FA512  48 8D 8C 24 90 02 00 00         lea rcx, [rsp + 0x290]
009FA51A  E8 05 78 07 00                  call 0x140a71d24
009FA51F  4C 8B C8                        mov r9, rax
009FA522  48 8D 8C 24 90 02 00 00         lea rcx, [rsp + 0x290]
009FA52A  E8 2D 5C 07 00                  call 0x140a7015c
009FA52F  4C 8B D0                        mov r10, rax
009FA532  8B CA                           mov ecx, edx
009FA534  E8 C3 FE F1 FF                  call 0x14091a3fc
009FA539  41 85 C0                        test r8d, eax
009FA53C  74 29                           je 0x1409fa567
009FA53E  41 8B 09                        mov ecx, dword ptr [r9]
009FA541  85 C9                           test ecx, ecx
009FA543  0F 84 BB 07 00 00               je 0x1409fad04
009FA549  83 F9 03                        cmp ecx, 3
009FA54C  0F 8F B2 07 00 00               jg 0x1409fad04
009FA552  41 8B 02                        mov eax, dword ptr [r10]
009FA555  85 C0                           test eax, eax
009FA557  0F 84 A7 07 00 00               je 0x1409fad04
009FA55D  83 F8 03                        cmp eax, 3
009FA560  7E 13                           jle 0x1409fa575
009FA562  E9 9D 07 00 00                  jmp 0x1409fad04
009FA567  45 89 39                        mov dword ptr [r9], r15d
009FA56A  45 89 3A                        mov dword ptr [r10], r15d
009FA56D  44 8B 84 24 B8 02 00 00         mov r8d, dword ptr [rsp + 0x2b8]
009FA575  41 03 D4                        add edx, r12d
009FA578  EB 93                           jmp 0x1409fa50d
009FA57A  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FA57F  49 8D 86 C0 04 00 00            lea rax, [r14 + 0x4c0]
009FA586  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
009FA58E  BE 88 00 00 00                  mov esi, 0x88
009FA593  4C 39 38                        cmp qword ptr [rax], r15
009FA596  75 6D                           jne 0x1409fa605
009FA598  41 B8 50 73 4A 62               mov r8d, 0x624a7350
009FA59E  8B D6                           mov edx, esi
009FA5A0  8D 4E 78                        lea ecx, [rsi + 0x78]
009FA5A3  E8 48 7B 18 00                  call 0x140b820f0
009FA5A8  48 8B D8                        mov rbx, rax
009FA5AB  48 85 C0                        test rax, rax
009FA5AE  75 0A                           jne 0x1409fa5ba
009FA5B0  BE 9A 00 00 C0                  mov esi, 0xc000009a
009FA5B5  E9 0E 0A 00 00                  jmp 0x1409fafc8
009FA5BA  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009FA5C3  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
009FA5CA  45 33 C0                        xor r8d, r8d
009FA5CD  48 8B D6                        mov rdx, rsi
009FA5D0  E8 6B 3D FA FF                  call 0x14099e340
009FA5D5  4C 8B E8                        mov r13, rax
009FA5D8  48 8B CB                        mov rcx, rbx
009FA5DB  48 85 C0                        test rax, rax
009FA5DE  75 14                           jne 0x1409fa5f4
009FA5E0  BA 50 73 4A 62                  mov edx, 0x624a7350
009FA5E5  E8 86 82 18 00                  call 0x140b82870
009FA5EA  BE 9A 00 00 C0                  mov esi, 0xc000009a
009FA5EF  E9 15 07 00 00                  jmp 0x1409fad09
009FA5F4  4C 8B C6                        mov r8, rsi
009FA5F7  33 D2                           xor edx, edx
009FA5F9  E8 42 C6 CC FF                  call 0x1406c6c40
009FA5FE  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FA603  EB 06                           jmp 0x1409fa60b
009FA605  49 8B DF                        mov rbx, r15
009FA608  4D 8B EF                        mov r13, r15
009FA60B  49 8D 4E 38                     lea rcx, [r14 + 0x38]
009FA60F  41 8A D4                        mov dl, r12b
009FA612  E8 09 A8 81 FF                  call 0x140214e20
009FA617  48 8B 84 24 20 01 00 00         mov rax, qword ptr [rsp + 0x120]
009FA61F  4C 39 38                        cmp qword ptr [rax], r15
009FA622  75 0C                           jne 0x1409fa630
009FA624  48 89 18                        mov qword ptr [rax], rbx
009FA627  4D 89 AE C8 04 00 00            mov qword ptr [r14 + 0x4c8], r13
009FA62E  EB 20                           jmp 0x1409fa650
009FA630  48 85 DB                        test rbx, rbx
009FA633  74 1B                           je 0x1409fa650
009FA635  BA 50 73 4A 62                  mov edx, 0x624a7350
009FA63A  48 8B CB                        mov rcx, rbx
009FA63D  E8 2E 82 18 00                  call 0x140b82870
009FA642  45 33 C0                        xor r8d, r8d
009FA645  48 8B D6                        mov rdx, rsi
009FA648  49 8B CD                        mov rcx, r13
009FA64B  E8 E0 25 EC FF                  call 0x1408bcc30
009FA650  49 8B 9E C0 04 00 00            mov rbx, qword ptr [r14 + 0x4c0]
009FA657  8B 33                           mov esi, dword ptr [rbx]
009FA659  48 8B 84 24 90 02 00 00         mov rax, qword ptr [rsp + 0x290]
009FA661  48 89 43 08                     mov qword ptr [rbx + 8], rax
009FA665  48 8B 84 24 98 02 00 00         mov rax, qword ptr [rsp + 0x298]
009FA66D  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
009FA671  48 8B 84 24 A0 02 00 00         mov rax, qword ptr [rsp + 0x2a0]
009FA679  48 89 43 18                     mov qword ptr [rbx + 0x18], rax
009FA67D  41 8B CF                        mov ecx, r15d
009FA680  4C 8D 43 3C                     lea r8, [rbx + 0x3c]
009FA684  85 C9                           test ecx, ecx
009FA686  74 19                           je 0x1409fa6a1
009FA688  41 3B CC                        cmp ecx, r12d
009FA68B  74 0A                           je 0x1409fa697
009FA68D  44 8B 8C 24 B0 02 00 00         mov r9d, dword ptr [rsp + 0x2b0]
009FA695  EB 12                           jmp 0x1409fa6a9
009FA697  44 8B 8C 24 BC 02 00 00         mov r9d, dword ptr [rsp + 0x2bc]
009FA69F  EB 08                           jmp 0x1409fa6a9
009FA6A1  44 8B 8C 24 CC 02 00 00         mov r9d, dword ptr [rsp + 0x2cc]
009FA6A9  85 C9                           test ecx, ecx
009FA6AB  74 19                           je 0x1409fa6c6
009FA6AD  41 3B CC                        cmp ecx, r12d
009FA6B0  74 0A                           je 0x1409fa6bc
009FA6B2  48 8D 84 24 B4 02 00 00         lea rax, [rsp + 0x2b4]
009FA6BA  EB 12                           jmp 0x1409fa6ce
009FA6BC  48 8D 84 24 C8 02 00 00         lea rax, [rsp + 0x2c8]
009FA6C4  EB 08                           jmp 0x1409fa6ce
009FA6C6  48 8D 84 24 D0 02 00 00         lea rax, [rsp + 0x2d0]
009FA6CE  45 89 48 F4                     mov dword ptr [r8 - 0xc], r9d
009FA6D2  8B 00                           mov eax, dword ptr [rax]
009FA6D4  41 89 00                        mov dword ptr [r8], eax
009FA6D7  41 03 CC                        add ecx, r12d
009FA6DA  49 83 C0 04                     add r8, 4
009FA6DE  83 F9 03                        cmp ecx, 3
009FA6E1  7C A1                           jl 0x1409fa684
009FA6E3  45 33 C0                        xor r8d, r8d
009FA6E6  33 D2                           xor edx, edx
009FA6E8  49 8B CE                        mov rcx, r14
009FA6EB  E8 A0 C2 F1 FF                  call 0x140916990
009FA6F0  48 8B 84 24 C0 02 00 00         mov rax, qword ptr [rsp + 0x2c0]
009FA6F8  48 C1 E8 0C                     shr rax, 0xc
009FA6FC  48 89 43 20                     mov qword ptr [rbx + 0x20], rax
009FA700  48 8B 84 24 A8 02 00 00         mov rax, qword ptr [rsp + 0x2a8]
009FA708  48 C1 E8 0C                     shr rax, 0xc
009FA70C  48 89 43 28                     mov qword ptr [rbx + 0x28], rax
009FA710  49 8B 8E C0 04 00 00            mov rcx, qword ptr [r14 + 0x4c0]
009FA717  8B 84 24 B8 02 00 00            mov eax, dword ptr [rsp + 0x2b8]
009FA71E  89 01                           mov dword ptr [rcx], eax
009FA720  F0 49 0F C1 BE F0 04 00 00      lock xadd qword ptr [r14 + 0x4f0], rdi
009FA729  40 80 E7 06                     and dil, 6
009FA72D  40 80 FF 02                     cmp dil, 2
009FA731  75 0C                           jne 0x1409fa73f
009FA733  49 8D 8E F0 04 00 00            lea rcx, [r14 + 0x4f0]
009FA73A  E8 91 B6 86 FF                  call 0x140265dd0
009FA73F  49 8D 8E F0 04 00 00            lea rcx, [r14 + 0x4f0]
009FA746  E8 B5 6E 8E FF                  call 0x1402e1600
009FA74B  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
009FA750  48 8B 83 C0 04 00 00            mov rax, qword ptr [rbx + 0x4c0]
009FA757  F7 00 FF 7D FF FF               test dword ptr [rax], 0xffff7dff
009FA75D  74 0D                           je 0x1409fa76c
009FA75F  F0 4C 01 25 79 BE 50 00         lock add qword ptr [rip + 0x50be79], r12
009FA767  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
009FA76C  85 F6                           test esi, esi
009FA76E  75 10                           jne 0x1409fa780
009FA770  48 8B 83 C0 04 00 00            mov rax, qword ptr [rbx + 0x4c0]
009FA777  44 39 38                        cmp dword ptr [rax], r15d
009FA77A  75 10                           jne 0x1409fa78c
009FA77C  85 F6                           test esi, esi
009FA77E  74 2E                           je 0x1409fa7ae
009FA780  48 8B 83 C0 04 00 00            mov rax, qword ptr [rbx + 0x4c0]
009FA787  44 39 38                        cmp dword ptr [rax], r15d
009FA78A  75 22                           jne 0x1409fa7ae
009FA78C  C7 44 24 28 05 00 00 00         mov dword ptr [rsp + 0x28], 5
009FA794  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009FA799  45 33 C9                        xor r9d, r9d
009FA79C  45 33 C0                        xor r8d, r8d
009FA79F  48 8D 15 7A 2D 0A 00            lea rdx, [rip + 0xa2d7a]
009FA7A6  48 8B CB                        mov rcx, rbx
009FA7A9  E8 3E FA F1 FF                  call 0x14091a1ec
009FA7AE  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
009FA7B3  F7 05 43 C3 5C 00 00 00 08 00   test dword ptr [rip + 0x5cc343], 0x80000
009FA7BD  74 22                           je 0x1409fa7e1
009FA7BF  66 C7 44 24 28 25 07            mov word ptr [rsp + 0x28], 0x725
009FA7C6  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
009FA7CB  45 33 C9                        xor r9d, r9d
009FA7CE  4C 8D 84 24 90 02 00 00         lea r8, [rsp + 0x290]
009FA7D6  41 8B D5                        mov edx, r13d
009FA7D9  48 8B CB                        mov rcx, rbx
009FA7DC  E8 9F 0C 00 00                  call 0x1409fb480
009FA7E1  48 8D 4B 38                     lea rcx, [rbx + 0x38]
009FA7E5  E8 26 52 86 FF                  call 0x14025fa10
009FA7EA  33 D2                           xor edx, edx
009FA7EC  48 8B CB                        mov rcx, rbx
009FA7EF  E8 A0 FB F1 FF                  call 0x14091a394
009FA7F4  4C 8B 83 20 06 00 00            mov r8, qword ptr [rbx + 0x620]
009FA7FB  4C 8B 5C 24 40                  mov r11, qword ptr [rsp + 0x40]
009FA800  49 8B 93 B8 04 00 00            mov rdx, qword ptr [r11 + 0x4b8]
009FA807  4C 03 C2                        add r8, rdx
009FA80A  41 B9 00 82 00 00               mov r9d, 0x8200
009FA810  49 8B CB                        mov rcx, r11
009FA813  E8 9C 3A 00 00                  call 0x1409fe2b4
009FA818  8B F8                           mov edi, eax
009FA81A  49 8D 9B F0 04 00 00            lea rbx, [r11 + 0x4f0]
009FA821  B8 11 00 00 00                  mov eax, 0x11
009FA826  F0 4C 0F B1 3B                  lock cmpxchg qword ptr [rbx], r15
009FA82B  74 08                           je 0x1409fa835
009FA82D  48 8B CB                        mov rcx, rbx
009FA830  E8 0B 8C 86 FF                  call 0x140263440
009FA835  48 8B CB                        mov rcx, rbx
009FA838  E8 C3 6D 8E FF                  call 0x1402e1600
009FA83D  85 FF                           test edi, edi
009FA83F  74 11                           je 0x1409fa852
009FA841  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
009FA846  48 8B 89 20 05 00 00            mov rcx, qword ptr [rcx + 0x520]
009FA84D  E8 06 59 06 00                  call 0x140a60158
009FA852  41 8B F7                        mov esi, r15d
009FA855  E9 6C E3 FF FF                  jmp 0x1409f8bc6
009FA85A  8B F0                           mov esi, eax
009FA85C  41 BC 01 00 00 00               mov r12d, 1
009FA862  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FA867  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009FA86C  E9 70 07 00 00                  jmp 0x1409fafe1
009FA871  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FA876  4D 8B C6                        mov r8, r14
009FA879  41 8B D4                        mov edx, r12d
009FA87C  49 8B CD                        mov rcx, r13
009FA87F  E8 C0 B0 D8 FF                  call 0x140785944
009FA884  E9 37 07 00 00                  jmp 0x1409fafc0
009FA889  49 8B DF                        mov rbx, r15
009FA88C  48 89 9C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rbx
009FA894  4D 8B C4                        mov r8, r12
009FA897  49 8B D5                        mov rdx, r13
009FA89A  48 8D 8C 24 00 02 00 00         lea rcx, [rsp + 0x200]
009FA8A2  E8 99 BF CC FF                  call 0x1406c6840
009FA8A7  48 8B 94 24 18 02 00 00         mov rdx, qword ptr [rsp + 0x218]
009FA8AF  41 BC 01 00 00 00               mov r12d, 1
009FA8B5  48 85 D2                        test rdx, rdx
009FA8B8  0F 84 EF 00 00 00               je 0x1409fa9ad
009FA8BE  0F B7 8C 24 28 02 00 00         movzx ecx, word ptr [rsp + 0x228]
009FA8C6  66 85 C9                        test cx, cx
009FA8C9  0F 84 C6 00 00 00               je 0x1409fa995
009FA8CF  41 84 D4                        test r12b, dl
009FA8D2  74 05                           je 0x1409fa8d9
009FA8D4  E8 F7 F6 E9 FF                  call 0x140899fd0
009FA8D9  4C 8D 04 0A                     lea r8, [rdx + rcx]
009FA8DD  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
009FA8E7  4C 3B C0                        cmp r8, rax
009FA8EA  77 05                           ja 0x1409fa8f1
009FA8EC  4C 3B C2                        cmp r8, rdx
009FA8EF  73 12                           jae 0x1409fa903
009FA8F1  8A 00                           mov al, byte ptr [rax]
009FA8F3  0F B7 8C 24 28 02 00 00         movzx ecx, word ptr [rsp + 0x228]
009FA8FB  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
009FA903  66 85 C9                        test cx, cx
009FA906  0F 84 89 00 00 00               je 0x1409fa995
009FA90C  41 84 CC                        test r12b, cl
009FA90F  0F 85 80 00 00 00               jne 0x1409fa995
009FA915  0F B7 D1                        movzx edx, cx
009FA918  49 03 D6                        add rdx, r14
009FA91B  B8 20 00 00 00                  mov eax, 0x20
009FA920  B9 01 01 00 00                  mov ecx, 0x101
009FA925  44 38 64 24 48                  cmp byte ptr [rsp + 0x48], r12b
009FA92A  0F 44 C1                        cmove eax, ecx
009FA92D  41 B8 50 73 4A 62               mov r8d, 0x624a7350
009FA933  8B C8                           mov ecx, eax
009FA935  E8 B6 77 18 00                  call 0x140b820f0
009FA93A  48 8B D8                        mov rbx, rax
009FA93D  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
009FA945  48 85 C0                        test rax, rax
009FA948  75 18                           jne 0x1409fa962
009FA94A  BE 17 00 00 C0                  mov esi, 0xc0000017
009FA94F  89 74 24 58                     mov dword ptr [rsp + 0x58], esi
009FA953  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FA958  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
009FA95D  E9 D3 00 00 00                  jmp 0x1409faa35
009FA962  44 0F B7 84 24 28 02 00 00      movzx r8d, word ptr [rsp + 0x228]
009FA96B  48 8B 94 24 18 02 00 00         mov rdx, qword ptr [rsp + 0x218]
009FA973  48 8B CB                        mov rcx, rbx
009FA976  E8 C5 BE CC FF                  call 0x1406c6840
009FA97B  0F B7 84 24 28 02 00 00         movzx eax, word ptr [rsp + 0x228]
009FA983  48 D1 E8                        shr rax, 1
009FA986  66 44 89 3C 43                  mov word ptr [rbx + rax*2], r15w
009FA98B  48 89 9C 24 18 02 00 00         mov qword ptr [rsp + 0x218], rbx
009FA993  EB 18                           jmp 0x1409fa9ad
009FA995  BE 0D 00 00 C0                  mov esi, 0xc000000d
009FA99A  89 74 24 58                     mov dword ptr [rsp + 0x58], esi
009FA99E  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FA9A3  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
009FA9A8  E9 88 00 00 00                  jmp 0x1409faa35
009FA9AD  F7 84 24 24 02 00 00 F0 FF FF FF  test dword ptr [rsp + 0x224], 0xfffffff0
009FA9B8  74 11                           je 0x1409fa9cb
009FA9BA  BE 0D 00 00 C0                  mov esi, 0xc000000d
009FA9BF  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FA9C4  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
009FA9C9  EB 6A                           jmp 0x1409faa35
009FA9CB  4C 39 BC 24 38 02 00 00         cmp qword ptr [rsp + 0x238], r15
009FA9D3  75 14                           jne 0x1409fa9e9
009FA9D5  4C 39 BC 24 10 02 00 00         cmp qword ptr [rsp + 0x210], r15
009FA9DD  75 0A                           jne 0x1409fa9e9
009FA9DF  4C 39 BC 24 50 02 00 00         cmp qword ptr [rsp + 0x250], r15
009FA9E7  74 10                           je 0x1409fa9f9
009FA9E9  E8 5A 3B 00 00                  call 0x1409fe548
009FA9EE  84 C0                           test al, al
009FA9F0  75 07                           jne 0x1409fa9f9
009FA9F2  BE 22 00 00 C0                  mov esi, 0xc0000022
009FA9F7  EB C6                           jmp 0x1409fa9bf
009FA9F9  48 8D 94 24 00 02 00 00         lea rdx, [rsp + 0x200]
009FAA01  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FAA06  49 8B CE                        mov rcx, r14
009FAA09  E8 DE CE FF FF                  call 0x1409f78ec
009FAA0E  8B F0                           mov esi, eax
009FAA10  EB B2                           jmp 0x1409fa9c4
009FAA12  8B F0                           mov esi, eax
009FAA14  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
009FAA18  41 BC 01 00 00 00               mov r12d, 1
009FAA1E  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FAA23  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
009FAA2B  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009FAA30  44 89 6C 24 50                  mov dword ptr [rsp + 0x50], r13d
009FAA35  48 85 DB                        test rbx, rbx
009FAA38  0F 84 8A 05 00 00               je 0x1409fafc8
009FAA3E  33 D2                           xor edx, edx
009FAA40  48 8B CB                        mov rcx, rbx
009FAA43  E8 28 7E 18 00                  call 0x140b82870
009FAA48  E9 94 05 00 00                  jmp 0x1409fafe1
009FAA4D  45 33 C0                        xor r8d, r8d
009FAA50  33 D2                           xor edx, edx
009FAA52  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FAA57  49 8B CE                        mov rcx, r14
009FAA5A  E8 31 BF F1 FF                  call 0x140916990
009FAA5F  4D 89 BE D0 02 00 00            mov qword ptr [r14 + 0x2d0], r15
009FAA66  4D 89 BE C8 02 00 00            mov qword ptr [r14 + 0x2c8], r15
009FAA6D  45 33 C0                        xor r8d, r8d
009FAA70  33 D2                           xor edx, edx
009FAA72  49 8B CE                        mov rcx, r14
009FAA75  E8 16 29 E8 FF                  call 0x14087d390
009FAA7A  41 8B F7                        mov esi, r15d
009FAA7D  E9 40 05 00 00                  jmp 0x1409fafc2
009FAA82  41 8A DF                        mov bl, r15b
009FAA85  41 0F 10 45 00                  movups xmm0, xmmword ptr [r13]
009FAA8A  0F 29 84 24 90 01 00 00         movaps xmmword ptr [rsp + 0x190], xmm0
009FAA92  41 0F 10 4D 10                  movups xmm1, xmmword ptr [r13 + 0x10]
009FAA97  0F 29 8C 24 A0 01 00 00         movaps xmmword ptr [rsp + 0x1a0], xmm1
009FAA9F  41 0F 10 45 20                  movups xmm0, xmmword ptr [r13 + 0x20]
009FAAA4  0F 29 84 24 B0 01 00 00         movaps xmmword ptr [rsp + 0x1b0], xmm0
009FAAAC  41 0F 10 4D 30                  movups xmm1, xmmword ptr [r13 + 0x30]
009FAAB1  0F 29 8C 24 C0 01 00 00         movaps xmmword ptr [rsp + 0x1c0], xmm1
009FAAB9  F2 41 0F 10 45 40               movsd xmm0, qword ptr [r13 + 0x40]
009FAABF  F2 0F 11 84 24 D0 01 00 00      movsd qword ptr [rsp + 0x1d0], xmm0
009FAAC8  41 BC 01 00 00 00               mov r12d, 1
009FAACE  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FAAD3  F7 84 24 90 01 00 00 FC FF FF FF  test dword ptr [rsp + 0x190], 0xfffffffc
009FAADE  74 0F                           je 0x1409faaef
009FAAE0  BE 0D 00 00 C0                  mov esi, 0xc000000d
009FAAE5  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
009FAAEA  E9 C5 00 00 00                  jmp 0x1409fabb4
009FAAEF  F6 84 24 90 01 00 00 03         test byte ptr [rsp + 0x190], 3
009FAAF7  74 E7                           je 0x1409faae0
009FAAF9  40 8A BC 24 90 01 00 00         mov dil, byte ptr [rsp + 0x190]
009FAB01  41 22 FC                        and dil, r12b
009FAB04  B3 08                           mov bl, 8
009FAB06  4C 8D 84 24 B0 00 00 00         lea r8, [rsp + 0xb0]
009FAB0E  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
009FAB16  49 8B CE                        mov rcx, r14
009FAB19  E8 EE D1 F1 FF                  call 0x140917d0c
009FAB1E  41 8B CF                        mov ecx, r15d
009FAB21  41 3B CC                        cmp ecx, r12d
009FAB24  73 11                           jae 0x1409fab37
009FAB26  8B C1                           mov eax, ecx
009FAB28  4C 3B B4 C4 B0 00 00 00         cmp r14, qword ptr [rsp + rax*8 + 0xb0]
009FAB30  74 11                           je 0x1409fab43
009FAB32  41 03 CC                        add ecx, r12d
009FAB35  EB EA                           jmp 0x1409fab21
009FAB37  49 8D 4E 38                     lea rcx, [r14 + 0x38]
009FAB3B  41 8A D4                        mov dl, r12b
009FAB3E  E8 DD A2 81 FF                  call 0x140214e20
009FAB43  45 8B CC                        mov r9d, r12d
009FAB46  45 8A C4                        mov r8b, r12b
009FAB49  40 8A D7                        mov dl, dil
009FAB4C  49 8B CE                        mov rcx, r14
009FAB4F  E8 FC D0 FF FF                  call 0x1409f7c50
009FAB54  8B F0                           mov esi, eax
009FAB56  85 C0                           test eax, eax
009FAB58  78 8B                           js 0x1409faae5
009FAB5A  41 8B CF                        mov ecx, r15d
009FAB5D  41 3B CC                        cmp ecx, r12d
009FAB60  73 11                           jae 0x1409fab73
009FAB62  8B C1                           mov eax, ecx
009FAB64  4C 3B B4 C4 B0 00 00 00         cmp r14, qword ptr [rsp + rax*8 + 0xb0]
009FAB6C  74 0E                           je 0x1409fab7c
009FAB6E  41 03 CC                        add ecx, r12d
009FAB71  EB EA                           jmp 0x1409fab5d
009FAB73  49 8D 4E 38                     lea rcx, [r14 + 0x38]
009FAB77  E8 94 4E 86 FF                  call 0x14025fa10
009FAB7C  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
009FAB84  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
009FAB8C  E8 6F F2 F1 FF                  call 0x140919e00
009FAB91  41 8A DF                        mov bl, r15b
009FAB94  E9 4C FF FF FF                  jmp 0x1409faae5
009FAB99  8B F0                           mov esi, eax
009FAB9B  45 33 FF                        xor r15d, r15d
009FAB9E  45 8D 67 01                     lea r12d, [r15 + 1]
009FABA2  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FABA7  41 8A DF                        mov bl, r15b
009FABAA  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009FABAF  44 89 6C 24 50                  mov dword ptr [rsp + 0x50], r13d
009FABB4  80 FB 08                        cmp bl, 8
009FABB7  0F 85 0B 04 00 00               jne 0x1409fafc8
009FABBD  48 8D 94 24 B0 00 00 00         lea rdx, [rsp + 0xb0]
009FABC5  49 8B CE                        mov rcx, r14
009FABC8  E8 D7 A8 04 00                  call 0x140a454a4
009FABCD  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
009FABD5  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
009FABDD  E8 1E F2 F1 FF                  call 0x140919e00
009FABE2  E9 FA 03 00 00                  jmp 0x1409fafe1
009FABE7  83 E9 2B                        sub ecx, 0x2b
009FABEA  0F 84 B3 03 00 00               je 0x1409fafa3
009FABF0  83 E9 01                        sub ecx, 1
009FABF3  0F 84 3F 03 00 00               je 0x1409faf38
009FABF9  83 E9 01                        sub ecx, 1
009FABFC  0F 84 BE 01 00 00               je 0x1409fadc0
009FAC02  83 E9 01                        sub ecx, 1
009FAC05  0F 84 78 01 00 00               je 0x1409fad83
009FAC0B  83 E9 01                        sub ecx, 1
009FAC0E  0F 84 DA 00 00 00               je 0x1409facee
009FAC14  83 E9 01                        sub ecx, 1
009FAC17  74 79                           je 0x1409fac92
009FAC19  83 F9 01                        cmp ecx, 1
009FAC1C  74 0A                           je 0x1409fac28
009FAC1E  BE 03 00 00 C0                  mov esi, 0xc0000003
009FAC23  E9 DD DE FF FF                  jmp 0x1409f8b05
009FAC28  49 8B 45 00                     mov rax, qword ptr [r13]
009FAC2C  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
009FAC34  41 BC 01 00 00 00               mov r12d, 1
009FAC3A  A9 FE FF FF FF                  test eax, 0xfffffffe
009FAC3F  0F 85 BF 00 00 00               jne 0x1409fad04
009FAC45  48 8B D0                        mov rdx, rax
009FAC48  48 C1 EA 20                     shr rdx, 0x20
009FAC4C  83 FA 08                        cmp edx, 8
009FAC4F  0F 83 AF 00 00 00               jae 0x1409fad04
009FAC55  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FAC5A  41 84 C4                        test r12b, al
009FAC5D  74 0A                           je 0x1409fac69
009FAC5F  85 D2                           test edx, edx
009FAC61  0F 84 DC 00 00 00               je 0x1409fad43
009FAC67  EB 05                           jmp 0x1409fac6e
009FAC69  BA 08 00 00 00                  mov edx, 8
009FAC6E  49 8B CE                        mov rcx, r14
009FAC71  E8 9A AF D8 FF                  call 0x140785c10
009FAC76  E9 DB F4 FF FF                  jmp 0x1409fa156
009FAC7B  8B F0                           mov esi, eax
009FAC7D  41 BC 01 00 00 00               mov r12d, 1
009FAC83  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FAC88  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009FAC8D  E9 4F 03 00 00                  jmp 0x1409fafe1
009FAC92  49 8B 45 00                     mov rax, qword ptr [r13]
009FAC96  48 89 84 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rax
009FAC9E  41 BC 01 00 00 00               mov r12d, 1
009FACA4  A9 FE FF FF FF                  test eax, 0xfffffffe
009FACA9  75 59                           jne 0x1409fad04
009FACAB  48 8B D0                        mov rdx, rax
009FACAE  48 C1 EA 20                     shr rdx, 0x20
009FACB2  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FACB7  83 FA 05                        cmp edx, 5
009FACBA  0F 83 83 00 00 00               jae 0x1409fad43
009FACC0  49 8B CE                        mov rcx, r14
009FACC3  41 84 C4                        test r12b, al
009FACC6  75 05                           jne 0x1409faccd
009FACC8  41 8D 54 24 04                  lea edx, [r12 + 4]
009FACCD  E8 F2 A7 D8 FF                  call 0x1407854c4
009FACD2  E9 7F F4 FF FF                  jmp 0x1409fa156
009FACD7  8B F0                           mov esi, eax
009FACD9  41 BC 01 00 00 00               mov r12d, 1
009FACDF  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FACE4  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009FACE9  E9 F3 02 00 00                  jmp 0x1409fafe1
009FACEE  41 8A 45 00                     mov al, byte ptr [r13]
009FACF2  88 84 24 99 00 00 00            mov byte ptr [rsp + 0x99], al
009FACF9  41 BC 01 00 00 00               mov r12d, 1
009FACFF  41 3A C4                        cmp al, r12b
009FAD02  74 0F                           je 0x1409fad13
009FAD04  BE 0D 00 00 C0                  mov esi, 0xc000000d
009FAD09  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FAD0E  E9 B5 02 00 00                  jmp 0x1409fafc8
009FAD13  8A 54 24 48                     mov dl, byte ptr [rsp + 0x48]
009FAD17  48 8B 0D 5A ED 5D 00            mov rcx, qword ptr [rip + 0x5ded5a]
009FAD1E  E8 FD 70 E7 FF                  call 0x140871e20
009FAD23  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FAD28  84 C0                           test al, al
009FAD2A  75 0A                           jne 0x1409fad36
009FAD2C  BE 61 00 00 C0                  mov esi, 0xc0000061
009FAD31  E9 92 02 00 00                  jmp 0x1409fafc8
009FAD36  41 F7 86 10 06 00 00 00 00 00 40  test dword ptr [r14 + 0x610], 0x40000000
009FAD41  75 0A                           jne 0x1409fad4d
009FAD43  BE 0D 00 00 C0                  mov esi, 0xc000000d
009FAD48  E9 7B 02 00 00                  jmp 0x1409fafc8
009FAD4D  BA 02 00 00 00                  mov edx, 2
009FAD52  49 8B CE                        mov rcx, r14
009FAD55  E8 5E AB D8 FF                  call 0x1407858b8
009FAD5A  F6 D8                           neg al
009FAD5C  1B C9                           sbb ecx, ecx
009FAD5E  F7 D1                           not ecx
009FAD60  BE 22 00 00 C0                  mov esi, 0xc0000022
009FAD65  23 F1                           and esi, ecx
009FAD67  E9 5C 02 00 00                  jmp 0x1409fafc8
009FAD6C  8B F0                           mov esi, eax
009FAD6E  41 BC 01 00 00 00               mov r12d, 1
009FAD74  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FAD79  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009FAD7E  E9 5E 02 00 00                  jmp 0x1409fafe1
009FAD83  49 8B 45 00                     mov rax, qword ptr [r13]
009FAD87  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
009FAD8F  48 8D 94 24 48 01 00 00         lea rdx, [rsp + 0x148]
009FAD97  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FAD9C  49 8B CE                        mov rcx, r14
009FAD9F  E8 08 38 00 00                  call 0x1409fe5ac
009FADA4  E9 D2 EE FF FF                  jmp 0x1409f9c7b
009FADA9  8B F0                           mov esi, eax
009FADAB  41 BC 01 00 00 00               mov r12d, 1
009FADB1  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FADB6  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009FADBB  E9 21 02 00 00                  jmp 0x1409fafe1
009FADC0  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FADC5  41 F7 86 10 06 00 00 00 00 00 40  test dword ptr [r14 + 0x610], 0x40000000
009FADD0  0F 84 1E F5 FF FF               je 0x1409fa2f4
009FADD6  4C 89 BC 24 30 01 00 00         mov qword ptr [rsp + 0x130], r15
009FADDE  41 0F 10 45 00                  movups xmm0, xmmword ptr [r13]
009FADE3  0F 11 84 24 A0 00 00 00         movups xmmword ptr [rsp + 0xa0], xmm0
009FADEB  66 0F 73 D8 08                  psrldq xmm0, 8
009FADF0  66 48 0F 7E C3                  movq rbx, xmm0
009FADF5  41 BC 01 00 00 00               mov r12d, 1
009FADFB  48 85 DB                        test rbx, rbx
009FADFE  0F 84 ED 00 00 00               je 0x1409faef1
009FAE04  0F B7 B4 24 A0 00 00 00         movzx esi, word ptr [rsp + 0xa0]
009FAE0C  0F B7 C6                        movzx eax, si
009FAE0F  66 41 2B C4                     sub ax, r12w
009FAE13  B9 06 02 00 00                  mov ecx, 0x206
009FAE18  66 3B C1                        cmp ax, cx
009FAE1B  0F 87 D0 00 00 00               ja 0x1409faef1
009FAE21  41 84 F4                        test r12b, sil
009FAE24  0F 85 C7 00 00 00               jne 0x1409faef1
009FAE2A  44 38 64 24 48                  cmp byte ptr [rsp + 0x48], r12b
009FAE2F  75 39                           jne 0x1409fae6a
009FAE31  41 84 DC                        test r12b, bl
009FAE34  74 05                           je 0x1409fae3b
009FAE36  E8 95 F1 E9 FF                  call 0x140899fd0
009FAE3B  48 8D 0C 33                     lea rcx, [rbx + rsi]
009FAE3F  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
009FAE49  48 3B C8                        cmp rcx, rax
009FAE4C  77 05                           ja 0x1409fae53
009FAE4E  48 3B CB                        cmp rcx, rbx
009FAE51  73 17                           jae 0x1409fae6a
009FAE53  8A 00                           mov al, byte ptr [rax]
009FAE55  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FAE5A  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
009FAE62  0F B7 B4 24 A0 00 00 00         movzx esi, word ptr [rsp + 0xa0]
009FAE6A  44 0F B7 EE                     movzx r13d, si
009FAE6E  41 B8 50 73 53 72               mov r8d, 0x72537350
009FAE74  41 8B D5                        mov edx, r13d
009FAE77  B9 00 01 00 00                  mov ecx, 0x100
009FAE7C  E8 6F 72 18 00                  call 0x140b820f0
009FAE81  48 8B F8                        mov rdi, rax
009FAE84  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
009FAE8C  48 85 C0                        test rax, rax
009FAE8F  75 13                           jne 0x1409faea4
009FAE91  BE 9A 00 00 C0                  mov esi, 0xc000009a
009FAE96  89 74 24 58                     mov dword ptr [rsp + 0x58], esi
009FAE9A  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
009FAE9F  E9 3D 01 00 00                  jmp 0x1409fafe1
009FAEA4  4D 8B C5                        mov r8, r13
009FAEA7  48 8B D3                        mov rdx, rbx
009FAEAA  48 8B CF                        mov rcx, rdi
009FAEAD  E8 8E B9 CC FF                  call 0x1406c6840
009FAEB2  90                              nop
009FAEB3  0F B7 DE                        movzx ebx, si
009FAEB6  48 D1 EB                        shr rbx, 1
009FAEB9  48 8B D3                        mov rdx, rbx
009FAEBC  48 8B CF                        mov rcx, rdi
009FAEBF  E8 9C 6E B0 FF                  call 0x140501d60
009FAEC4  48 3B C3                        cmp rax, rbx
009FAEC7  74 0C                           je 0x1409faed5
009FAEC9  BE 0D 00 00 C0                  mov esi, 0xc000000d
009FAECE  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
009FAED3  EB 4D                           jmp 0x1409faf22
009FAED5  48 89 BC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdi
009FAEDD  48 8D 94 24 A0 00 00 00         lea rdx, [rsp + 0xa0]
009FAEE5  49 8B CE                        mov rcx, r14
009FAEE8  E8 33 48 D8 FF                  call 0x14077f720
009FAEED  8B F0                           mov esi, eax
009FAEEF  EB DD                           jmp 0x1409faece
009FAEF1  BE 0D 00 00 C0                  mov esi, 0xc000000d
009FAEF6  89 74 24 58                     mov dword ptr [rsp + 0x58], esi
009FAEFA  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
009FAEFF  E9 DD 00 00 00                  jmp 0x1409fafe1
009FAF04  8B F0                           mov esi, eax
009FAF06  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
009FAF0A  41 BC 01 00 00 00               mov r12d, 1
009FAF10  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FAF15  48 8B BC 24 30 01 00 00         mov rdi, qword ptr [rsp + 0x130]
009FAF1D  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009FAF22  48 85 FF                        test rdi, rdi
009FAF25  0F 84 B6 00 00 00               je 0x1409fafe1
009FAF2B  BA 50 73 53 72                  mov edx, 0x72537350
009FAF30  48 8B CF                        mov rcx, rdi
009FAF33  E9 0B FB FF FF                  jmp 0x1409faa43
009FAF38  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FAF3D  41 BC 01 00 00 00               mov r12d, 1
009FAF43  41 8A D4                        mov dl, r12b
009FAF46  49 8D 4E 38                     lea rcx, [r14 + 0x38]
009FAF4A  E8 D1 9E 81 FF                  call 0x140214e20
009FAF4F  45 39 BE 10 06 00 00            cmp dword ptr [r14 + 0x610], r15d
009FAF56  7D 0A                           jge 0x1409faf62
009FAF58  BE 21 00 00 C0                  mov esi, 0xc0000021
009FAF5D  E9 3B DB FF FF                  jmp 0x1409f8a9d
009FAF62  41 0F 10 45 00                  movups xmm0, xmmword ptr [r13]
009FAF67  F3 41 0F 7F 86 D0 05 00 00      movdqu xmmword ptr [r14 + 0x5d0], xmm0
009FAF70  F0 41 81 8E 10 06 00 00 00 00 00 80  lock or dword ptr [r14 + 0x610], 0x80000000
009FAF7C  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FAF81  E9 C7 F1 FF FF                  jmp 0x1409fa14d
009FAF86  8B F0                           mov esi, eax
009FAF88  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FAF8D  49 8D 4E 38                     lea rcx, [r14 + 0x38]
009FAF91  E8 7A 4A 86 FF                  call 0x14025fa10
009FAF96  41 BC 01 00 00 00               mov r12d, 1
009FAF9C  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009FAFA1  EB 3E                           jmp 0x1409fafe1
009FAFA3  4D 8B 45 00                     mov r8, qword ptr [r13]
009FAFA7  4C 89 84 24 F0 01 00 00         mov qword ptr [rsp + 0x1f0], r8
009FAFAF  8A 54 24 48                     mov dl, byte ptr [rsp + 0x48]
009FAFB3  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FAFB8  49 8B CE                        mov rcx, r14
009FAFBB  E8 B4 A5 D8 FF                  call 0x140785574
009FAFC0  8B F0                           mov esi, eax
009FAFC2  41 BC 01 00 00 00               mov r12d, 1
009FAFC8  44 8B 6C 24 50                  mov r13d, dword ptr [rsp + 0x50]
009FAFCD  EB 12                           jmp 0x1409fafe1
009FAFCF  8B F0                           mov esi, eax
009FAFD1  41 BC 01 00 00 00               mov r12d, 1
009FAFD7  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009FAFDC  44 8B 6C 24 60                  mov r13d, dword ptr [rsp + 0x60]
009FAFE1  90                              nop
009FAFE2  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
009FAFEA  66 44 01 A1 E6 01 00 00         add word ptr [rcx + 0x1e6], r12w
009FAFF2  75 12                           jne 0x1409fb006
009FAFF4  90                              nop
009FAFF5  48 8D 81 98 00 00 00            lea rax, [rcx + 0x98]
009FAFFC  48 39 00                        cmp qword ptr [rax], rax
009FAFFF  74 05                           je 0x1409fb006
009FB001  E8 7A 7C 8E FF                  call 0x1402e2c80
009FB006  85 F6                           test esi, esi
009FB008  74 28                           je 0x1409fb032
009FB00A  F7 05 EC BA 5C 00 00 00 08 00   test dword ptr [rip + 0x5cbaec], 0x80000
009FB014  74 1C                           je 0x1409fb032
009FB016  66 C7 44 24 28 27 07            mov word ptr [rsp + 0x28], 0x727
009FB01D  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
009FB021  45 33 C9                        xor r9d, r9d
009FB024  45 33 C0                        xor r8d, r8d
009FB027  41 8B D5                        mov edx, r13d
009FB02A  49 8B CE                        mov rcx, r14
009FB02D  E8 4E 04 00 00                  call 0x1409fb480
009FB032  BA 50 73 51 79                  mov edx, 0x79517350
009FB037  49 8B CE                        mov rcx, r14
009FB03A  E8 A1 C8 8F FF                  call 0x1402f78e0
009FB03F  8B C6                           mov eax, esi
009FB041  EB 05                           jmp 0x1409fb048
009FB043  B8 03 00 00 C0                  mov eax, 0xc0000003
009FB048  48 8B 8C 24 50 0C 00 00         mov rcx, qword ptr [rsp + 0xc50]
009FB050  48 33 CC                        xor rcx, rsp
009FB053  E8 E8 15 CB FF                  call 0x1406ac640
009FB058  48 81 C4 60 0C 00 00            add rsp, 0xc60
009FB05F  41 5F                           pop r15
009FB061  41 5E                           pop r14
009FB063  41 5D                           pop r13
009FB065  41 5C                           pop r12
009FB067  5F                              pop rdi
009FB068  5E                              pop rsi
009FB069  5B                              pop rbx
009FB06A  C3                              ret
009FB06B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtSetInformationJobObject(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m32B;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m4B8;
    unsigned __int64 v_stack_m4C0;
    unsigned __int64 v_stack_m4C8;
    unsigned int v_stack_m534;
    unsigned __int64 v_stack_m668;
    unsigned __int64 v_stack_m670;
    unsigned int v_stack_m674;
    unsigned int v_stack_m678;
    unsigned __int64 v_stack_m680;
    unsigned __int64 v_stack_m688;
    unsigned __int64 v_stack_m690;
    unsigned __int64 v_stack_m698;
    unsigned __int64 v_stack_m778;
    unsigned __int64 v_stack_m880;
    unsigned __int64 v_stack_m888;
    unsigned __int64 v_stack_m898;
    unsigned __int64 v_stack_m8B0;
    unsigned __int64 v_stack_m8B8;
    unsigned int v_stack_m8EC;
    unsigned int v_stack_m8F0;
    unsigned __int64 v_stack_m8F8;
    unsigned int v_stack_m900;
    unsigned __int64 v_stack_m908;
    unsigned __int64 v_stack_m910;
    unsigned int v_stack_m918;
    unsigned __int64 v_stack_m920;
    unsigned __int64 v_stack_m928;
    unsigned int v_stack_m930;
    unsigned int v_stack_m934;
    unsigned __int64 v_stack_m938;
    unsigned __int64 v_stack_m940;
    unsigned __int64 v_stack_m948;
    unsigned __int64 v_stack_m950;
    unsigned __int64 v_stack_m958;
    unsigned __int64 v_stack_m960;
    unsigned int v_stack_m964;
    unsigned int v_stack_m968;
    unsigned __int64 v_stack_m970;
    unsigned __int64 v_stack_m978;
    unsigned __int64 v_stack_m980;
    unsigned __int64 v_stack_m988;
    unsigned __int64 v_stack_m990;
    unsigned __int64 v_stack_m9A0;
    unsigned int v_stack_m9A8;
    unsigned __int64 v_stack_m9B0;
    unsigned int v_stack_m9B4;
    unsigned __int64 v_stack_m9B8;
    unsigned __int64 v_stack_m9C8;
    unsigned int v_stack_m9CC;
    unsigned __int64 v_stack_m9D0;
    unsigned __int64 v_stack_m9D8;
    unsigned int v_stack_m9DC;
    unsigned int v_stack_m9E0;
    unsigned int v_stack_m9E4;
    unsigned int v_stack_m9E8;
    unsigned __int64 v_stack_m9F0;
    unsigned __int64 v_stack_m9F8;
    unsigned __int64 v_stack_mA00;
    unsigned __int64 v_stack_mA08;
    unsigned __int64 v_stack_mA48;
    unsigned __int64 v_stack_mA60;
    unsigned __int16 v_stack_mA70;
    unsigned int v_stack_mA74;
    unsigned __int64 v_stack_mA80;
    unsigned __int64 v_stack_mA88;
    unsigned __int64 v_stack_mA98;
    unsigned __int64 v_stack_mAA8;
    unsigned __int64 v_stack_mAB0;
    unsigned __int64 v_stack_mAB8;
    unsigned __int64 v_stack_mAC8;
    unsigned __int64 v_stack_mAD8;
    unsigned __int64 v_stack_mAE8;
    unsigned __int64 v_stack_mAF8;
    unsigned __int64 v_stack_mB08;
    unsigned int v_stack_mB10;
    unsigned __int64 v_stack_mB20;
    unsigned __int64 v_stack_mB30;
    unsigned int v_stack_mB38;
    unsigned int v_stack_mB3C;
    unsigned int v_stack_mB40;
    unsigned int v_stack_mB44;
    unsigned int v_stack_mB48;
    unsigned __int64 v_stack_mB50;
    unsigned __int16 v_stack_mB58;
    unsigned __int64 v_stack_mB60;
    unsigned __int64 v_stack_mB68;
    unsigned int v_stack_mB6C;
    unsigned __int64 v_stack_mB70;
    unsigned __int64 v_stack_mB78;
    unsigned int v_stack_mB7C;
    unsigned __int64 v_stack_mB80;
    unsigned __int64 v_stack_mB88;
    unsigned int v_stack_mB8C;
    unsigned int v_stack_mB90;
    unsigned __int64 v_stack_mB98;
    unsigned int v_stack_mBA0;
    unsigned __int64 v_stack_mBB0;
    unsigned __int64 v_stack_mBB8;
    unsigned __int64 v_stack_mBC0;
    unsigned int v_stack_mBC8;
    unsigned __int64 v_stack_mBD0;
    unsigned __int64 v_stack_mBD8;
    unsigned __int64 v_stack_mBE0;
    unsigned __int64 v_stack_mBE8;
    unsigned __int64 v_stack_mBF0;
    unsigned __int64 v_stack_mBF8;
    unsigned __int16 v_stack_mBFE;
    unsigned __int8 v_stack_mBFF;
    unsigned __int8 v_stack_mC00;
    unsigned __int64 v_stack_mC08;
    unsigned __int64 v_stack_mC10;
    unsigned __int64 v_stack_mC18;
    unsigned int v_stack_mC20;
    unsigned int v_stack_mC24;
    unsigned __int16 v_stack_mC26;
    unsigned __int64 v_stack_mC28;
    unsigned __int16 v_stack_mC2C;
    unsigned __int8 v_stack_mC30;
    unsigned int v_stack_mC38;
    unsigned __int8 v_stack_mC3B;
    unsigned __int8 v_stack_mC3C;
    unsigned int v_stack_mC40;
    unsigned int v_stack_mC48;
    unsigned __int8 v_stack_mC50;
    unsigned __int64 v_stack_mC58;
    unsigned __int64 v_stack_mC60;
    unsigned __int64 v_stack_mC68;
    unsigned __int64 v_stack_mC70;
    unsigned int v_stack_mC78;
    unsigned int v_stack_mC98;

    v_rsp = (v_rsp) - (0xC60ULL);
    result = (*(unsigned __int64 *)(v_rip + 4268646)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_mC48 = (unsigned int)((int)(a2));
    v_stack_mC18 = a1;
    v_stack_mC38 = (unsigned int)((int)(a2));
    v_stack_mBD0 = a3;
    a2 = 0;
    result = memset(v_stack_m880, a2, 256, a4);
    v_r15 = 0;
    v_stack_mB80 = 0;
    v_stack_mB70 = 0;
    v_stack_mC3C = 0;
    v_stack_mB50 = 0;
    a2 = 0;
    result = memset(v_stack_m928, a2, 152, a4);
    v_stack_m9A0 = v_xmm0;
    v_stack_mB60 = v_xmm1;
    v_stack_mBF8 = 0;
    a2 = 0;
    result = memset(v_stack_mA98, a2, 144, a4);
    v_stack_mC58 = 0;
    v_stack_mB30 = v_xmm0;
    v_stack_mB20 = v_xmm0;
    result = 0;
    v_stack_mBC0 = v_xmm0;
    v_stack_mBB0 = v_xmm0;
    v_stack_mBA0 = 0;
    a2 = 0;
    result = memset(v_stack_mA08, a2, v_r15 + 72, a4);
    v_stack_m958 = v_xmm0;
    v_stack_m948 = v_xmm0;
    v_stack_m938 = v_xmm0;
    result = 0;
    v_stack_m990 = v_xmm1;
    v_stack_m980 = v_xmm1;
    v_stack_m970 = v_xmm1;
    v_stack_m960 = 0;
    v_stack_mC28 = 0;
    v_stack_mC3B = 0;
    v_stack_m9B8 = v_xmm0;
    v_stack_m9A8 = 0;
    v_stack_mBE8 = 0;
    v_stack_mB98 = v_xmm0;
    if (((unsigned int)((int)(a2) - 1)) > 50) goto loc_009FB043;
    if (((unsigned int)((int)(a2))) == 9) goto loc_009F86E3;
    if (((unsigned int)((int)(a2))) == 12) goto loc_009F86D7;
    if (((unsigned int)((int)(a2))) == 31) goto loc_009F8679;
    if (((unsigned int)((unsigned int)(a4))) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 10454620 + (int)(a2) * 4 + 11855148))))) goto loc_009F8692;
    if (((unsigned int)((int)(a2))) == 11) goto loc_009F8672;
    if (((unsigned int)((int)(a2))) != 14) goto loc_009F86EF;
loc_009F8672:
    if (((unsigned int)((unsigned int)(a4))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 10454620 + (int)(a2) * 4 + 11855148))))) goto loc_009F8692;
    goto loc_009F86EF;
loc_009F8679:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) - (48));
    if (condition_is_equal) goto loc_009F868B;
    result = (unsigned int)((result) - (48));
    if (condition_is_equal) goto loc_009F868B;
loc_009F8689:
    if (((unsigned int)(result)) != 48) goto loc_009F86EF;
loc_009F868B:
loc_009F8692:
    v_stack_mC10 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_mC50 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_mC30 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_009F8726;
    if ((unsigned int)((unsigned int)(a4)) == 0) goto loc_009F871B;
    if (((v_stack_mBD0) & ((unsigned int)(*(unsigned int *)(v_rip - 10454674 + (int)(a2) * 4 + 11855356)) - 1)) == 0) goto loc_009F86F9;
    result = ExRaiseDatatypeMisalignment((unsigned int)(*(unsigned int *)(v_rip - 10454674 + (int)(a2) * 4 + 11855356)) - 1, v_rip - 10454674, v_r15 + 72, a4);
loc_009F86D7:
    if (((unsigned int)((unsigned int)(a4))) == 48) goto loc_009F868B;
    goto loc_009F8689;
loc_009F86E3:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) - (144));
    if (condition_is_equal) goto loc_009F868B;
    if (((unsigned int)(result)) == 8) goto loc_009F868B;
loc_009F86EF:
    goto loc_009FB048;
loc_009F86F9:
    if (((unsigned int)(a4) + v_stack_mBD0 * 1) > ((unsigned int)(0xC0000004ULL))) goto loc_009F8711;
    result = (unsigned int)(0xC0000004ULL);
    v_r13 = v_stack_mBD0;
    if (((unsigned int)(a4) + v_stack_mBD0 * 1) < v_stack_mBD0) {
        result = *(unsigned __int8 *)((unsigned int)(0xC0000004ULL));
        v_r13 = v_stack_mBD0;
    }
    goto loc_009F872E;
loc_009F8726:
loc_009F872E:
    if (a1 != 0) goto loc_009F873D;
    goto loc_009FB048;
loc_009F873D:
    a2 = 16;
    if (((unsigned int)((int)(a2))) != 5) { a2 = (unsigned int)(16 - 14); }
    v_stack_mC60 = 0;
    v_stack_mC68 = 0;
    v_stack_mC70 = v_stack_mC58;
    v_stack_mC78 = 0x79517350ULL;
    result = ObpReferenceObjectByHandleWithTag(a1, a2, *(unsigned __int64 *)(v_rip + 6087956), (unsigned __int8)((unsigned int)(0xC0000008ULL)));
    if (sign_flag) goto loc_009FB048;
    v_stack_mC40 = 0;
    v_rdi = (a1) | (-1);
    if (((unsigned int)((unsigned int)(v_stack_mC48))) > 25) goto loc_009FA15E;
    if (((unsigned int)((unsigned int)(v_stack_mC48))) == 25) goto loc_009FA12E;
    if (((unsigned int)((unsigned int)(v_stack_mC48))) > 14) goto loc_009F9A4B;
    if (((unsigned int)((unsigned int)(v_stack_mC48))) == 14) goto loc_009F9592;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mC48)))) - ((unsigned int)(16 - 14)));
    if (condition_is_equal) goto loc_009F8B66;
    a2 = (unsigned int)((a2) - ((unsigned int)(16 - 14)));
    if (condition_is_equal) goto loc_009F8B26;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_009F8AC2;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_009F8A6B;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_009F8867;
    a2 = (unsigned int)((a2) - ((unsigned int)(16 - 14)));
    if (condition_is_equal) goto loc_009F8B66;
    a2 = (unsigned int)((a2) - ((unsigned int)(16 - 14)));
    if (condition_is_equal) goto loc_009F9592;
    if (a2 != 1) goto loc_009FAC1E;
loc_009F880A:
    if (((unsigned int)((unsigned int)(a4))) == 48) goto loc_009FA3F1;
    if (((unsigned int)((unsigned int)(a4))) == 56) goto loc_009FA35A;
    result = memcpy(v_stack_mA08, v_stack_mBD0, (unsigned int)(a4), (unsigned __int8)((unsigned int)(0xC0000008ULL)));
    v_stack_mC20 = (unsigned int)((unsigned int)(0x1F8204ULL));
    goto loc_009FA473;
loc_009F8867:
    v_stack_mBE8 = v_xmm0;
    if (v_stack_mBE0 != 0) goto loc_009F88E6;
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, (unsigned __int8)(v_stack_mBE0 + 1), (unsigned int)(v_stack_m9E0), v_stack_m9F8);
    a3 = 0;
    a2 = 0;
    result = PspLockJobMemoryLimitsExclusive(v_stack_mC58, a2, a3, v_stack_m9F8);
    *(unsigned __int64 *)(v_stack_mC58 + 552) = 0;
    a3 = 0;
    a2 = 0;
    result = PspUnlockJobMemoryLimitsExclusive(v_stack_mC58, a2, a3, v_stack_m9F8);
    result = ExReleaseResourceLite(v_stack_mC58 + 56, a2, a3, v_stack_m9F8);
    if (*(unsigned __int64 *)(v_stack_mC58 + 552) == 0) goto loc_009FAFC8;
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(v_stack_mC58 + 552), (unsigned int)(0x624A7350ULL), a3, v_stack_m9F8);
    goto loc_009FAFC8;
loc_009F88E6:
    v_stack_mC60 = 0;
    v_stack_mC68 = 0;
    v_stack_mC70 = v_stack_mBF8;
    v_stack_mC78 = 0x624A7350ULL;
    result = ObpReferenceObjectByHandleWithTag(*(unsigned __int64 *)(v_stack_mC58 + 552), (unsigned int)((unsigned int)(v_stack_mC58)), *(unsigned __int64 *)(v_rip + 6087635), v_stack_mC50);
    if (sign_flag) goto loc_009F8949;
    if ((*(unsigned __int64 *)(v_stack_mC58 + 1232)) != 0) goto loc_009F8954;
    result = IoAllocateMiniCompletionPacket(v_rip + 455161, v_stack_mC58, *(unsigned __int64 *)(v_rip + 6087635), v_stack_mC50);
    if (result != 0) goto loc_009F8954;
loc_009F8949:
    goto loc_009F8A51;
loc_009F8954:
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, 1, *(unsigned __int64 *)(v_rip + 6087635), v_stack_mC50);
    if ((*(unsigned __int64 *)(v_stack_mC58 + 552)) != 0) goto loc_009F8A16;
    if (((*(unsigned int *)(v_stack_mC58 + 256)) & (0x2000ULL)) == 0) goto loc_009F8990;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mC58 + 1552))))) != 0) goto loc_009F8A16;
loc_009F8990:
    v_rdi = result;
    if ((*(unsigned __int64 *)(v_stack_mC58 + 1232)) == 0) {
        *(unsigned __int64 *)(v_stack_mC58 + 1232) = result;
        v_rdi = 0;
    }
    a3 = 0;
    a2 = 0;
    result = PspLockJobMemoryLimitsExclusive(v_stack_mC58, a2, a3, v_stack_mC50);
    *(unsigned __int64 *)(v_stack_mC58 + 560) = v_stack_mBE8;
    *(unsigned __int64 *)(v_stack_mC58 + 552) = v_stack_mBF8;
    *(unsigned __int64 *)(v_stack_mC58 + 568) = 0;
    a3 = 0;
    a2 = 0;
    result = PspUnlockJobMemoryLimitsExclusive(v_stack_mC58, a2, a3, v_stack_mC50);
    result = (unsigned int)(*(unsigned int *)(v_stack_mC58 + 1104));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mC58 + 1104)))) & (64)) != 0) {
        v_stack_mC70 = 1;
        v_stack_mC78 = v_stack_mC58;
        a4 = v_rip + 567442;
        a3 = 0;
        a2 = 0;
        a1 = v_stack_mC58;
        result = PspEnumJobsAndProcessesInJobHierarchy(a1, a2, a3, a4);
    }
    result = ExReleaseResourceLite(v_stack_mC58 + 56, a2, a3, a4);
    goto loc_009F8A51;
loc_009F8A16:
    result = ExReleaseResourceLite(v_stack_mC58 + 56, a2, a3, a4);
    result = ObfDereferenceObjectWithTag(v_stack_mBF8, (unsigned int)(0x624A7350ULL), a3, a4);
    goto loc_009F8A51;
loc_009F8A51:
    if (v_rdi == 0) goto loc_009FAFC8;
    *(unsigned __int64 *)(v_rdi + 56) = 0;
    result = IopFreeMiniCompletionPacket(v_rdi, (unsigned int)(0x624A7350ULL), a3, a4);
    goto loc_009FAFC8;
loc_009F8A6B:
    v_stack_mB10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mBD0)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mBD0)))) > 1) goto loc_009FAD43;
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, 1, a3, a4);
    *(unsigned int *)(v_stack_mC58 + 548) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mBD0)));
loc_009F8A9D:
loc_009F8AA1:
    result = ExReleaseResourceLite(v_stack_mC58 + 56, 1, a3, a4);
    goto loc_009FAFC8;
loc_009F8AC2:
    v_stack_mB08 = v_xmm0;
    v_stack_mAF8 = v_xmm1;
    v_stack_mAE8 = v_xmm0;
    result = (unsigned int)(((unsigned int)(v_stack_mB08)) & (0xFFFFFFF0ULL));
    result = (unsigned int)(-(result));
    v_rsi = (unsigned int)(((unsigned int)(0xC000000DULL)) & (0xFFFFFF52ULL));
    v_rsi = (unsigned int)((v_rsi) + (0xC00000BBULL));
loc_009F8B05:
    goto loc_009FAFC2;
loc_009F8B26:
    v_stack_mB38 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mBD0)));
    a4 = 0;
    result = PspSetUILimitJobObject(v_stack_mC58, v_stack_mC10, (unsigned int)(*(unsigned int *)(v_stack_mBD0)), a4);
    goto loc_009FAFC0;
loc_009F8B66:
    result = memcpy(v_stack_m928, v_stack_mBD0, 1, a4);
    if (1 < 152) {
        a2 = (152) - (1);
        a1 = v_stack_m928;
        a1 = (a1) + (1);
        a3 = a2;
        a2 = 0;
        result = memset(a1, a2, a3, a4);
    }
    result = PspGetJobLimitInformationValidFlags((unsigned int)((unsigned int)((unsigned int)(v_stack_mC48))), 1, a3, a4);
    v_stack_mC20 = (unsigned int)(result);
    result = (unsigned int)(~(result));
    if (((v_stack_m918) & ((unsigned int)(result))) == 0) goto loc_009F8BD0;
loc_009F8BC1:
loc_009F8BC6:
    goto loc_009FAFE1;
loc_009F8BD0:
    a2 = 0;
    result = memset(v_stack_m778, a2, (unsigned int)(0x728ULL), a4);
    result = 0;
    v_stack_mBC0 = v_xmm0;
    v_stack_mBB0 = v_xmm0;
    v_stack_mBA0 = 0;
    v_stack_m678 = (unsigned int)((unsigned int)(v_stack_m918));
    v_stack_mC48 = 0;
    v_stack_mC08 = 0;
    v_stack_mBD8 = 0;
    result = (unsigned __int8)(((unsigned __int8)((unsigned int)(v_stack_m918))) & (8));
    result = (unsigned __int8)(-(result));
    a1 = (unsigned int)((v_stack_m778) & (v_stack_m900));
    v_stack_m674 = (unsigned int)(a1);
    if (((32) & ((unsigned __int8)((unsigned int)(v_stack_m918)))) == 0) goto loc_009F8CA5;
    if (((unsigned int)((unsigned int)(v_stack_m8F0))) > 6) goto loc_009F8BC1;
    result = (unsigned int)(((unsigned int)(v_stack_m8F0)) + (-3));
    if (((unsigned int)(result)) > ((unsigned int)(32 - 31))) goto loc_009F8C95;
    result = SeCheckPrivilegedObject(*(unsigned __int64 *)(v_rip + 6164078), v_stack_mC18, 32 - 30, v_stack_mC50);
    result = (unsigned __int8)((result) & ((unsigned __int8)(32 - 31)));
    v_rbx = (unsigned __int8)(((unsigned __int8)(result)) << (2));
    if ((unsigned __int8)(result) != 0) goto loc_009F8C95;
loc_009F8C8B:
    goto loc_009F8BC6;
loc_009F8C95:
    v_stack_m32B = (unsigned __int8)((unsigned int)(v_stack_m8F0));
    goto loc_009F8CAD;
loc_009F8CA5:
    v_stack_m32B = 0;
loc_009F8CAD:
    if (((v_stack_m918) & (128)) == 0) goto loc_009F8D07;
    if (((unsigned int)((unsigned int)(v_stack_m8EC))) >= 10) goto loc_009F8BC1;
    if (((unsigned int)((unsigned int)(v_stack_m8EC))) <= 5) goto loc_009F8CFE;
    result = SeCheckPrivilegedObject(*(unsigned __int64 *)(v_rip + 6163970), v_stack_mC18, 2, v_stack_mC50);
    result = (unsigned __int8)((result) & ((unsigned __int8)(32 - 31)));
    v_rbx = (unsigned __int8)(((unsigned __int8)(result)) << (2));
    if ((unsigned __int8)(result) == 0) goto loc_009F8C8B;
loc_009F8CFE:
    v_stack_m534 = (unsigned int)((unsigned int)(v_stack_m8EC));
    goto loc_009F8D12;
loc_009F8D07:
    v_stack_m534 = 5;
loc_009F8D12:
    if (((v_stack_m918) & (2)) == 0) goto loc_009F8D37;
    if (v_stack_m928 == 0) goto loc_009F8BC1;
    v_stack_m698 = v_stack_m928;
    goto loc_009F8D3F;
loc_009F8D37:
    v_stack_m698 = 0;
loc_009F8D3F:
    if (((v_stack_m918) & (4)) == 0) goto loc_009F8D62;
    if (v_stack_m920 == 0) goto loc_009F8BC1;
    v_stack_m690 = v_stack_m920;
loc_009F8D62:
    if (((v_stack_m918) & ((unsigned __int8)(32 - 31))) == 0) goto loc_009F8DFC;
    if (v_stack_m910 != 0) goto loc_009F8D8B;
    if (v_stack_m908 == 0) goto loc_009F8BC1;
loc_009F8D8B:
    if (v_stack_m910 != v_rdi) goto loc_009F8D9E;
    if (v_stack_m908 == v_rdi) goto loc_009F8BC1;
loc_009F8D9E:
    if (v_stack_m910 > v_stack_m908) goto loc_009F8BC1;
    if (v_stack_m910 < 0x14000ULL) goto loc_009F8BC1;
    if (v_stack_m910 <= (*(unsigned __int64 *)(v_rip + 6157440))) goto loc_009F8DE2;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 6163739), v_stack_mC50, 2, v_stack_mC50);
    if ((unsigned __int8)(result) == 0) goto loc_009F8C8B;
loc_009F8DE2:
    v_stack_m688 = v_stack_m910;
    v_stack_m680 = v_stack_m908;
    goto loc_009F8E0C;
loc_009F8DFC:
    v_stack_m688 = 0;
    v_stack_m680 = 0;
loc_009F8E0C:
    if (((v_stack_m918) & (256)) == 0) goto loc_009F8E3E;
    if (v_stack_m8B8 < ((unsigned int)(0x1000ULL))) goto loc_009F8BC1;
    a1 = (v_stack_m8B8) >> (12);
    v_stack_m4C8 = a1;
    goto loc_009F8E46;
loc_009F8E3E:
    v_stack_m4C8 = 0;
loc_009F8E46:
    if (((v_stack_m918) & (512)) == 0) goto loc_009F8E72;
    if (v_stack_m8B0 < ((unsigned int)(0x1000ULL))) goto loc_009F8BC1;
    a1 = (v_stack_m8B0) >> (12);
    v_stack_m4C0 = a1;
    goto loc_009F8E7A;
loc_009F8E72:
    v_stack_m4C0 = 0;
loc_009F8E7A:
    if (((v_stack_m918) & (0x200000ULL)) == 0) goto loc_009F8EA6;
    if (v_stack_m898 < ((unsigned int)(0x1000ULL))) goto loc_009F8BC1;
    a1 = (v_stack_m898) >> (12);
    v_stack_m4B8 = a1;
    goto loc_009F8EAE;
loc_009F8EA6:
    v_stack_m4B8 = 0;
loc_009F8EAE:
    v_stack_m670 = 0x200001ULL;
    a2 = 0;
    result = memset(v_stack_m668, a2, 256, v_stack_mC50);
    v_stack_mC38 = (unsigned int)((unsigned int)(v_stack_m678));
    if ((((unsigned __int8)((unsigned int)(v_stack_m678))) & (16)) == 0) goto loc_009F9026;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mC58 + 1552)))) & (2)) != 0) goto loc_009F905D;
    if (v_stack_m8F8 == 0) goto loc_009F905D;
    if ((*(unsigned __int64 *)(v_stack_mC58 + 528)) != 0) goto loc_009F8F8E;
    result = ExAllocatePool2(256, 40, (unsigned int)(0x614A7350ULL), v_stack_mC50);
    v_stack_mC48 = result;
    if (result != 0) goto loc_009F8F3A;
loc_009F8F30:
    goto loc_009FAFE1;
loc_009F8F3A:
    a3 = 0;
    result = PsChargeSharedPoolQuota(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3 + 40, a3, v_stack_mC50);
    v_stack_mC08 = result;
    if (result != 0) goto loc_009F8F7A;
loc_009F8F66:
    result = ExFreePoolWithTag((unsigned int)(0xC000009AULL), (unsigned int)(0x614A7350ULL), a3, v_stack_mC50);
    goto loc_009F8BC6;
loc_009F8F7A:
    v_stack_mC38 = (unsigned int)((unsigned int)(v_stack_m678));
loc_009F8F8E:
    result = SeCaptureSubjectContextEx(v_stack_mC10, *(unsigned __int64 *)(v_stack_mC10 + 184), v_stack_mBB8, v_stack_mC50);
    v_stack_mBD8 = v_stack_mBB8;
    if (v_stack_mC50 == 0) goto loc_009F901B;
    v_stack_m9B8 = (unsigned int)(32 - 31);
    v_stack_m9B4 = (unsigned int)(32 - 31);
    v_stack_m9B0 = *(unsigned __int64 *)(v_rip + 6163112);
    v_stack_m9A8 = 0;
    result = SePrivilegeCheck(v_stack_m9B8, v_stack_mBB8, (unsigned __int8)(32 - 31), v_stack_mC50);
    a1 = (unsigned int)(((unsigned __int8)(result)) & ((unsigned int)(32 - 31)));
    result = (unsigned int)(((unsigned int)(v_stack_mBC0)) & (0xFFFFFFFEULL));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    v_stack_mBC0 = (unsigned int)(a1);
    goto loc_009F9023;
loc_009F901B:
loc_009F9023:
    v_rbx = (unsigned __int8)((v_rbx) | (2));
loc_009F9026:
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, (unsigned __int8)(32 - 31), (unsigned __int8)(32 - 31), v_stack_mC50);
    if ((((unsigned __int8)((unsigned int)(v_stack_mC38))) & (4)) != 0) goto loc_009F906F;
    if ((((unsigned __int8)((unsigned int)(v_stack_mC38))) & (64)) == 0) goto loc_009F9067;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mC58 + 256))) & (4));
    a2 = (unsigned int)(((unsigned int)(v_stack_mC38)) | ((unsigned int)(result)));
    v_stack_m690 = *(unsigned __int64 *)(v_stack_mC58 + 232);
    goto loc_009F906F;
loc_009F905D:
    goto loc_009FAFE1;
loc_009F9067:
    v_stack_m690 = 0;
loc_009F906F:
    a2 = (unsigned int)((a2) & (0xFFFFFFBFULL));
    v_stack_m678 = a2;
    if (((2) & ((unsigned __int8)(v_rbx))) == 0) goto loc_009F91F0;
    if (((2) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mC58 + 1552))))) == 0) goto loc_009F909F;
loc_009F9091:
    v_stack_mC40 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_009F949F;
loc_009F909F:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mC58 + 256)))) & (16)) == 0) goto loc_009F90C8;
    result = KeFirstGroupAffinityEx(v_stack_mB60, v_stack_mC58 + 264, (unsigned __int8)(32 - 31), v_stack_mC50);
    goto loc_009F90DE;
loc_009F90C8:
    result = KeQueryPrimaryGroupThread(*(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_mC58 + 264, (unsigned __int8)(32 - 31), v_stack_mC50);
    v_stack_mB58 = (unsigned __int16)(result);
loc_009F90DE:
    result = (v_stack_m8F8) & (*(unsigned __int64 *)(v_rip - 10457320 + (unsigned __int16)(result) * 8 + 16544040));
    if (v_stack_m8F8 == result) goto loc_009F9116;
    v_stack_mC40 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_009F949F;
loc_009F9116:
    result = KeAddGroupAffinityEx(v_stack_m670, v_stack_mB58, v_stack_m8F8, v_stack_mC50);
    v_stack_mC70 = (unsigned int)(32 - 31);
    v_stack_mC78 = v_stack_mBC0;
    a3 = 0;
    a2 = 0;
    result = PspEnumJobsAndProcessesInJobHierarchy(v_stack_mC58, a2, a3, v_rip - 2571492);
    v_stack_mC40 = (unsigned int)(result);
    if (sign_flag) goto loc_009F949F;
    if (*(unsigned __int64 *)(v_stack_mC58 + 528) != 0) goto loc_009F919A;
    *(unsigned __int64 *)(v_stack_mC58 + 528) = v_stack_mC48;
    *(unsigned __int64 *)(v_stack_mC58 + 536) = v_stack_mC08;
    v_stack_mC48 = 0;
    v_stack_mBD8 = 0;
    goto loc_009F91C2;
loc_009F919A:
    v_stack_mB30 = v_xmm0;
    v_stack_mB20 = v_xmm1;
    v_stack_mBD8 = v_stack_mB30;
loc_009F91C2:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC58 + 528)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC58 + 528) + 16) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC58 + 528) + 32) = v_xmm0;
    goto loc_009F9205;
loc_009F91F0:
    if (condition_is_above_or_equal) goto loc_009F9205;
    if ((((unsigned __int8)(v_stack_mC58)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mC58 + 1552))))) == 0) goto loc_009F9091;
loc_009F9205:
    if ((((unsigned __int8)(32 - 31)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mC58 + 256))))) == 0) goto loc_009F9241;
    if (((v_stack_m678) & ((unsigned __int8)(32 - 31))) != 0) goto loc_009F9241;
    result = *(unsigned __int64 *)(v_rip + 6086281);
    if ((((unsigned __int8)(32 - 31)) & ((unsigned __int8)(*(unsigned __int64 *)(v_rip + 6086281)))) != 0) {
        a1 = v_rip + 6086269;
        result = ExfAcquireReleasePushLockExclusive(a1, a2, a3, v_rip - 2571492);
    }
loc_009F9241:
    v_stack_mB98 = v_stack_mC58;
    v_stack_mC18 = v_stack_mC58 + 256;
    v_stack_mB8C = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mC58 + 256)));
    *(unsigned __int64 *)(v_stack_mC58 + 240) = v_stack_m688;
    *(unsigned __int64 *)(v_stack_mC58 + 248) = v_stack_m680;
    *(unsigned int *)(v_stack_mC58 + 260) = (unsigned int)((unsigned int)(v_stack_m674));
    if (((2) & ((unsigned __int8)(v_rbx))) == 0) goto loc_009F9301;
loc_009F92A9:
    *(unsigned __int64 *)(v_stack_mC58 + 264) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mC58 + 264 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_stack_mC58 + 264 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mC58 + 264 + 48) = v_xmm1;
    *(unsigned __int64 *)(v_stack_mC58 + 264 + 64) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mC58 + 264 + 80) = v_xmm1;
    *(unsigned __int64 *)(v_stack_mC58 + 264 + 96) = v_xmm0;
    a1 = (v_stack_mC58 + 264) + (2 + 126);
    *(unsigned __int64 *)(a1 - 16) = v_xmm1;
    a2 = (v_stack_m670) + (2 + 126);
    result = (2) - (1);
    if (condition_is_not_equal) goto loc_009F92A9;
    *(unsigned __int64 *)(a1) = *(unsigned __int64 *)(a2);
loc_009F9301:
    *(unsigned __int8 *)(v_stack_mC58 + 1101) = (unsigned __int8)(v_stack_m32B);
    *(unsigned int *)(v_stack_mC58 + 580) = (unsigned int)((unsigned int)(v_stack_m534));
    *(unsigned __int64 *)(v_stack_mC58 + 224) = v_stack_m698;
    v_stack_mC38 = v_stack_mC58 + 232;
    *(unsigned __int64 *)(v_stack_mC58 + 232) = v_stack_m690;
    if (((unsigned int)((unsigned int)(v_stack_mC48))) != 9) goto loc_009F93E3;
    a3 = 0;
    a2 = 0;
    result = PspLockJobMemoryLimitsExclusive(v_stack_mC58, a2, a3, v_rip - 2571492);
    result = (unsigned int)(~((unsigned int)(v_stack_mC20)));
    result = (unsigned int)((result) & (*(unsigned int *)(v_stack_mC18)));
    result = (unsigned int)((result) | (v_stack_m678));
    *(unsigned int *)(v_stack_mC18) = (unsigned int)(result);
    *(unsigned __int64 *)(v_stack_mC58 + 688) = v_stack_m4C8;
    *(unsigned __int64 *)(v_stack_mC58 + 696) = v_stack_m4C0;
    *(unsigned __int64 *)(v_stack_mC58 + 704) = v_stack_m4B8;
    v_rdi = (unsigned __int8)((v_rdi) & (6));
    result = v_stack_m4B8;
    if (((unsigned __int8)(v_rdi)) == 2) {
        a1 = v_stack_mC58 + 1264;
        result = ExfTryToWakePushLock(a1, a2, a3, v_rip - 2571492);
    }
    result = KeAbPostRelease(v_stack_mC58 + 1264, a2, a3, v_rip - 2571492);
    goto loc_009F93F4;
loc_009F93E3:
    result = (unsigned int)(~((unsigned int)(v_stack_mC20)));
    result = (unsigned int)((result) & (*(unsigned int *)(v_stack_mC18)));
    result = (unsigned int)((result) | (v_stack_m678));
    *(unsigned int *)(v_stack_mC18) = (unsigned int)(result);
loc_009F93F4:
    result = (unsigned int)(((unsigned int)(v_stack_mB8C)) | (*(unsigned int *)(v_stack_mC18)));
    result = (unsigned int)(~(result));
    v_stack_mB90 = (unsigned int)(result);
    if (((v_stack_m918) & (4)) != 0) {
        v_stack_mC70 = (unsigned int)(32 - 31);
        v_stack_mC78 = v_stack_mC38;
        a4 = v_rip - 2571041;
        a3 = 0;
        a2 = 0;
        a1 = v_stack_mC58;
        result = PspEnumJobsAndProcessesInJobHierarchy(a1, a2, a3, a4);
        *(unsigned __int64 *)(v_stack_mC58 + 184) = 0;
        *(unsigned __int64 *)(v_stack_mC58 + 192) = 0;
        a1 = v_stack_mC58;
        result = KeResetEvent(a1, a2, a3, a4);
    }
    v_rsi = (unsigned int)(v_stack_mC40);
    v_r14 = v_stack_mC58;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mC58 + 256)))) & (6)) != 0) {
        v_r14 = v_stack_mC58;
        v_rsi = v_stack_mC40;
    }
    if (((v_stack_mB90) & ((unsigned __int8)(32 - 31))) == 0) {
        v_rbx = (unsigned __int8)((v_rbx) | ((unsigned __int8)(32 - 31)));
    }
    v_stack_mC70 = 5;
    v_stack_mC78 = v_stack_mB98;
    result = PspEnumJobsAndProcessesInJobHierarchy(v_r14, v_rip - 1551831, v_rip + 552512, v_rip + 384407);
loc_009F949F:
    if ((((unsigned __int8)(32 - 31)) & ((unsigned __int8)(v_rbx))) == 0) goto loc_009F9528;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 6085628, a2, a3, v_rip + 384407);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 6085601;
        a2 = result;
        a1 = v_rip + 6085591;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, v_rip + 384407);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(32 - 31);
    }
loc_009F9503:
    if ((*(unsigned __int64 *)(v_stack_mC58 + 40)) == (v_stack_mC58 + 40)) goto loc_009F9524;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 40) - 856 + 496));
    if ((((unsigned __int8)(32 - 31)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 40) - 856 + 496))))) == 0) {
        result = PspAddProcessToWorkingSetChangeList(*(unsigned __int64 *)(v_stack_mC58 + 40) - 856, a2, a3, v_rip + 384407);
    }
    goto loc_009F9503;
loc_009F9524:
loc_009F9528:
    result = ExReleaseResourceLite(v_stack_mC58 + 56, a2, a3, v_rip + 384407);
    if ((((unsigned __int8)(32 - 31)) & ((unsigned __int8)(v_rbx))) != 0) {
        a1 = v_stack_mC58;
        result = PspApplyWorkingSetLimits(a1, a2, a3, v_rip + 384407);
    }
    result = v_stack_mBD8;
    if (v_stack_mBD8 != 0) {
        a1 = v_stack_mBD8;
        result = SeReleaseSubjectContext(a1, a2, a3, v_rip + 384407);
    }
    if (v_stack_mC48 == 0) goto loc_009FAFE1;
    result = ExFreePoolWithTag(v_stack_mC48, (unsigned int)(0x614A7350ULL), a3, v_rip + 384407);
    goto loc_009F9A39;
loc_009F9592:
    v_stack_mC18 = 0;
    a3 = 16;
    if (((unsigned int)(v_stack_mC08)) != 14) { a3 = (unsigned int)(v_stack_mC58); }
    v_stack_mBD8 = (unsigned int)(a3);
    a2 = 0;
    if (0 == 0) goto loc_009F95D6;
    goto loc_009FAFE1;
loc_009F95D6:
    a2 = 0;
    v_stack_mBC8 = 1;
    v_stack_m888 = 0x200001ULL;
    a2 = 0;
    result = memset(v_stack_m880, a2, 256, v_rip + 384407);
    result = KeQueryActiveGroupCount(v_stack_m880, a2, 256, v_rip + 384407);
    a1 = (unsigned __int16)(((unsigned __int16)(result)) - (1));
    v_stack_mBFE = (unsigned __int16)(a1);
loc_009F9627:
    if (1 == 0) goto loc_009F9710;
    if (((unsigned int)((unsigned int)(v_stack_mC48))) != 14) goto loc_009F965E;
    v_stack_mB60 = v_xmm0;
    v_stack_mC2C = (unsigned __int16)(result);
    v_stack_mB88 = v_xmm0;
    goto loc_009F968D;
loc_009F965E:
    v_stack_mC2C = (unsigned __int16)(*(unsigned __int16 *)((unsigned int)((unsigned int)(v_stack_mC08))));
    if (((unsigned __int16)(*(unsigned __int16 *)((unsigned int)((unsigned int)(v_stack_mC08))))) > ((unsigned __int16)(a1))) goto loc_009F9707;
    v_stack_mB88 = *(unsigned __int64 *)(v_rip - 10458744 + *(unsigned __int16 *)((unsigned int)((unsigned int)(v_stack_mC08))) * 8 + 16544040);
loc_009F968D:
    if (((unsigned __int16)(v_stack_mC2C)) > ((unsigned __int16)(a1))) goto loc_009F9707;
    if ((*(unsigned __int64 *)(v_rsp + (unsigned __int16)(v_stack_mC2C) * 8 + 1048)) != 0) goto loc_009F9707;
    result = (*(unsigned __int64 *)(v_rip - 10458744 + (unsigned __int16)(v_stack_mC2C) * 8 + 16544040)) & (v_stack_mB88);
    if (v_stack_mB88 != result) goto loc_009F9707;
    result = KeAddGroupAffinityEx(v_stack_m888, v_stack_mC2C, v_stack_mB88, v_rip + 384407);
    v_r14 = (unsigned int)(((unsigned int)(v_stack_mBC8)) - 1);
    v_stack_mBC8 = (unsigned int)(v_r14);
    v_r13 = (v_stack_mBD0) + ((unsigned int)(v_stack_mBD8));
    v_stack_mBD0 = v_r13;
    goto loc_009F9627;
loc_009F9707:
    v_stack_mC40 = (unsigned int)((unsigned int)(0xC000000DULL));
loc_009F9710:
    goto loc_009F9743;
loc_009F9743:
    if (sign_flag) goto loc_009FAFE1;
    if ((*(unsigned __int64 *)(v_stack_mC58 + 528)) != 0) goto loc_009F97B0;
    result = ExAllocatePool2(256, 40, (unsigned int)(0x614A7350ULL), v_rip + 384407);
    if (result == 0) goto loc_009F8F30;
    a3 = 0;
    result = PsChargeSharedPoolQuota(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), a3 + 40, a3, v_rip + 384407);
    v_stack_mC18 = result;
    if (result != 0) goto loc_009F97AB;
    goto loc_009F8F66;
loc_009F97AB:
loc_009F97B0:
    result = SeCaptureSubjectContextEx(v_stack_mC10, *(unsigned __int64 *)(v_stack_mC10 + 184), v_stack_mBB8, v_rip + 384407);
    v_stack_mC08 = v_stack_mBB8;
    if (v_stack_mC50 == 0) goto loc_009F983D;
    v_stack_m9B8 = 1;
    v_stack_m9B4 = 1;
    v_stack_m9B0 = *(unsigned __int64 *)(v_rip + 6161030);
    v_stack_m9A8 = 0;
    result = SePrivilegeCheck(v_stack_m9B8, v_stack_mBB8, 1, v_rip + 384407);
    a1 = (unsigned int)(((unsigned __int8)(result)) & (1));
    result = (unsigned int)(((unsigned int)(v_stack_mBC0)) & (0xFFFFFFFEULL));
    a1 = (unsigned int)((a1) | ((unsigned int)(result)));
    v_stack_mBC0 = (unsigned int)(a1);
    goto loc_009F9845;
loc_009F983D:
loc_009F9845:
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, 1, 1, v_rip + 384407);
    v_stack_mC70 = 1;
    v_stack_mC78 = v_stack_mBC0;
    a3 = 0;
    a2 = 0;
    result = PspEnumJobsAndProcessesInJobHierarchy(v_stack_mC58, a2, a3, v_rip - 2573322);
    v_stack_mC40 = (unsigned int)(result);
    if (sign_flag) goto loc_009F99FD;
    if (*(unsigned __int64 *)(v_stack_mC58 + 528) != 0) goto loc_009F98B4;
    *(unsigned __int64 *)(v_stack_mC58 + 528) = result;
    *(unsigned __int64 *)(v_stack_mC58 + 536) = v_stack_mC18;
    v_stack_mC08 = 0;
    goto loc_009F98DC;
loc_009F98B4:
    v_stack_mB30 = v_xmm0;
    v_stack_mB20 = v_xmm1;
    v_stack_mC08 = v_stack_mB30;
loc_009F98DC:
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC58 + 528)) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC58 + 528) + 16) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC58 + 528) + 32) = v_xmm0;
    v_stack_mB98 = v_stack_mC58;
    v_stack_mB8C = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mC58 + 256)));
    v_stack_mB90 = (unsigned int)((unsigned int)(0xFFFFFFEFULL));
loc_009F9945:
    *(unsigned __int64 *)(v_stack_mC58 + 264) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mC58 + 264 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_stack_mC58 + 264 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mC58 + 264 + 48) = v_xmm1;
    *(unsigned __int64 *)(v_stack_mC58 + 264 + 64) = v_xmm0;
    *(unsigned __int64 *)(v_stack_mC58 + 264 + 80) = v_xmm1;
    *(unsigned __int64 *)(v_stack_mC58 + 264 + 96) = v_xmm0;
    a2 = (v_stack_mC58 + 264) + (128);
    *(unsigned __int64 *)(a2 - 16) = v_xmm1;
    result = (v_stack_m888) + (128);
    a3 = (2) - (1);
    if (condition_is_not_equal) goto loc_009F9945;
    *(unsigned __int64 *)(a2) = *(unsigned __int64 *)(result);
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_mC48))))) != 14) goto loc_009F99B6;
    result = KeIsEmptyAffinityEx(v_stack_mC58 + 264, a2, a3, 128);
    if ((unsigned int)(result) == 0) goto loc_009F99B6;
    goto loc_009F99C6;
loc_009F99B6:
loc_009F99C6:
    v_stack_mC70 = 5;
    v_stack_mC78 = v_stack_mB98;
    a3 = 0;
    result = PspEnumJobsAndProcessesInJobHierarchy(v_stack_mC58, v_rip - 1553196, a3, v_rip + 383038);
loc_009F99FD:
    result = ExReleaseResourceLite(v_stack_mC58 + 56, v_rip - 1553196, a3, v_rip + 383038);
    result = v_stack_mC08;
    if (v_stack_mC08 != 0) {
        a1 = v_stack_mC08;
        result = SeReleaseSubjectContext(a1, v_rip - 1553196, a3, v_rip + 383038);
    }
    if (0 == 0) goto loc_009FAFE1;
    result = ExFreePoolWithTag(0, (unsigned int)(0x614A7350ULL), a3, v_rip + 383038);
loc_009F9A39:
    a3 = 0;
    result = PsReturnSharedPoolQuota(v_stack_mC18, 40, a3, v_rip + 383038);
    goto loc_009FAFE1;
loc_009F9A4B:
    a1 = (unsigned int)((v_stack_mC18) - (15));
    if (condition_is_equal) goto loc_009F9DB7;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009F9D4C;
    a1 = (unsigned int)((a1) - ((unsigned int)(v_stack_mC58)));
    if (condition_is_equal) goto loc_009F9CAF;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_009F9C63;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009F9B8B;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009F9B20;
    if (((unsigned int)(a1)) != 1) goto loc_009FAC1E;
    v_stack_mAB8 = *(unsigned __int64 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_mC48))));
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, 1, a3, v_rip + 383038);
    if ((((unsigned __int8)(1 + 31)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mC58 + 1552))))) != 0) goto loc_009F9AC7;
loc_009F9ABD:
    goto loc_009F8A9D;
loc_009F9AC7:
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 1240) + 40));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 1240) + 40)))) & (16)) == 0) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 1240) + 40))) | (16));
        *(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 1240) + 40) = (unsigned int)(result);
        a3 = v_stack_mC58;
        a2 = v_rip - 4284773;
        a1 = *(unsigned __int64 *)(v_stack_mC58 + 1240) + 48;
        result = KeInitializeDpc(a1, a2, a3, v_rip + 383038);
    }
    result = KeSetSchedulingGroupCycleNotification(*(unsigned __int64 *)(v_stack_mC58 + 1240) + 128, *(unsigned __int64 *)(v_stack_mC58 + 1240) + 48, (unsigned int)(0xC000000DULL), v_rip + 383038);
loc_009F9B01:
    goto loc_009F8A9D;
loc_009F9B20:
    if ((*(unsigned __int8 *)((unsigned int)((unsigned int)((unsigned int)(v_stack_mC48))))) == 1) goto loc_009F9B44;
    v_stack_mC40 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_009FAFE1;
loc_009F9B44:
    v_stack_mC70 = 0;
    v_stack_mC78 = 0;
    a2 = 0;
    result = PspEnumJobsAndProcessesInJobHierarchy(v_stack_mC58, a2, v_rip + 695412, v_rip + 671003);
    goto loc_009FA156;
loc_009F9B8B:
    v_stack_mC3C = (unsigned __int8)(*(unsigned __int8 *)((unsigned int)(v_stack_mC48)));
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, 1, v_rip + 695412, v_rip + 671003);
    if ((((unsigned __int8)(1 + 31)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mC58 + 1552))))) == 0) goto loc_009F9ABD;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 1240) + 40)))) & (64)) != 0) goto loc_009F9ABD;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 1240) + 40)))) & (33)) != 0) goto loc_009F9C42;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 1240) + 40))))) >> (3));
    a1 = (unsigned int)((a1) & (1));
    result = ((unsigned __int8)(v_stack_mC3C) != 0) ? 1 : 0;
    if (((unsigned int)(a1)) == ((unsigned int)(result))) goto loc_009F9ABD;
    a3 = (unsigned __int8)(-(v_stack_mC3C));
    result = (unsigned int)((result) & (8));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 1240) + 40))) & (0xFFFFFFF7ULL));
    a2 = (unsigned int)((a2) | ((unsigned int)(result)));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 1240) + 40) = a2;
    a1 = (*(unsigned __int64 *)(v_stack_mC58 + 1240)) - (-128);
    result = KeSetSchedulingGroupRankBias(a1, v_stack_mC3C, a3, *(unsigned __int64 *)(v_stack_mC58 + 1240));
    v_stack_mC70 = 1;
    v_stack_mC78 = v_stack_mC3C;
    a3 = 0;
    a2 = 0;
    result = PspEnumJobsAndProcessesInJobHierarchy(v_stack_mC58, a2, a3, v_rip - 5578704);
    goto loc_009F9B01;
loc_009F9C42:
    goto loc_009F8A9D;
loc_009F9C63:
    v_stack_mC00 = (unsigned __int8)(*(unsigned __int8 *)((unsigned int)(v_stack_mC48)));
    result = PspSetBackgroundJobTree(v_stack_mC58, *(unsigned __int8 *)((unsigned int)(v_stack_mC48)), a3, v_rip - 5578704);
loc_009F9C7B:
    if (sign_flag) goto loc_009FAFE1;
    goto loc_009FAFE1;
loc_009F9CAF:
    v_stack_m9A0 = v_xmm0;
    if ((unsigned int)((unsigned int)(v_stack_m9A0)) == 0) goto loc_009FA493;
    if ((((unsigned int)((unsigned int)(v_stack_m9A0))) & (0xFFFFFFF0ULL)) != 0) goto loc_009FA493;
    if (((1) & ((unsigned __int8)((unsigned int)(v_stack_m9A0)))) != 0) goto loc_009F9CEA;
    if ((((unsigned __int8)((unsigned int)(v_stack_m9A0))) & (8)) != 0) goto loc_009FAD04;
loc_009F9CEA:
    result = PspFreezeJobTree(v_stack_mC58, v_stack_m9A0, a3, v_rip - 5578704);
    if (sign_flag) goto loc_009FAFC8;
    *(unsigned int *)((unsigned int)(v_stack_mC48)) = (unsigned int)((unsigned int)(v_stack_m9A0));
    goto loc_009FAFE1;
loc_009F9D4C:
    v_stack_mB3C = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_mC48))));
    if ((((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_mC48))))) & (0xFFFFC001ULL)) != 0) goto loc_009FAD43;
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, 1, a3, v_rip - 5578704);
    a3 = 0;
    a2 = 0;
    result = PspLockJobMemoryLimitsExclusive(v_stack_mC58, a2, a3, v_rip - 5578704);
    *(unsigned int *)(v_stack_mC58 + 1104) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_mC48))));
    a3 = 0;
    a2 = 0;
    result = PspUnlockJobMemoryLimitsExclusive(v_stack_mC58, a2, a3, v_rip - 5578704);
    goto loc_009FA14D;
loc_009F9DB7:
    result = memcpy(v_stack_mB70, (unsigned int)(v_stack_mC48), 1, v_rip - 5578704);
    if ((((unsigned int)(v_stack_mB70)) & (0xFFFFFFC0ULL)) != 0) goto loc_009FAD04;
    v_stack_mC38 = 0;
    v_stack_mC28 = (unsigned int)((unsigned int)(v_stack_mB6C));
    if (((1) & ((unsigned __int8)(v_stack_mB70))) == 0) goto loc_009F9E69;
    if ((((unsigned __int8)(v_stack_mC58)) & ((unsigned __int8)(v_stack_mB70))) == 0) goto loc_009F9E16;
    if ((((unsigned __int8)(v_stack_mB70)) & (16)) != 0) goto loc_009FAD04;
loc_009F9E0E:
    if (((unsigned int)((unsigned int)(v_stack_mB6C) - 1)) > 8) goto loc_009FAD04;
    goto loc_009F9E56;
loc_009F9E16:
    if ((((unsigned __int8)(v_stack_mB70)) & (16)) == 0) goto loc_009F9E48;
    if ((((unsigned __int8)(v_stack_mB70)) & (4)) != 0) goto loc_009FAD04;
    if (((unsigned __int16)((unsigned int)(v_stack_mB6C))) < 1) goto loc_009FAD04;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_mB6C)))) >> (16));
    if (((unsigned __int16)((unsigned int)(v_stack_mB6C))) > ((unsigned __int16)(result))) goto loc_009FAD04;
    goto loc_009F9E0E;
loc_009F9E48:
    if (((unsigned int)((unsigned int)(v_stack_mB6C) - 1)) > 0x270FULL) goto loc_009FAD04;
loc_009F9E56:
    if (((32) & ((unsigned __int8)(v_stack_mB70))) == 0) goto loc_009F9E6E;
    v_stack_mC38 = (unsigned int)(32 - 24);
    goto loc_009F9E6E;
loc_009F9E69:
loc_009F9E6E:
    a3 = 0;
    result = PspLockJobChain(v_stack_mC58, v_stack_mC10, a3, v_rip - 5578704);
    if (((1) & ((unsigned __int8)(v_stack_mB70))) == 0) goto loc_009F9EC0;
    if (((32) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_mC58 + 1552))))) != 0) goto loc_009F9ED5;
    result = PspAllocateRateControl(2, v_stack_mC10, a3, v_rip - 5578704);
    if (result != 0) goto loc_009F9EB7;
    goto loc_009FA102;
loc_009F9EB7:
    *(unsigned __int64 *)(v_stack_mC58 + 1240) = result;
    goto loc_009F9ED8;
loc_009F9EC0:
    if (((32) & ((unsigned __int8)(result))) != 0) goto loc_009F9ECF;
    goto loc_009FA102;
loc_009F9ECF:
loc_009F9ED5:
loc_009F9ED8:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 1240) + 40) = 0;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 1240) + 44) = (unsigned int)((unsigned int)(0xC000000DULL));
    if (((1) & ((unsigned __int8)(v_stack_mB70))) == 0) goto loc_009FA030;
    result = *(unsigned __int64 *)(v_stack_mC58 + 1240);
    if ((((unsigned __int8)(v_stack_mB70)) & (4)) != 0) {
        result = *(unsigned __int64 *)(v_stack_mC58 + 1240);
        v_stack_mC26 = (unsigned __int16)((unsigned int)(0xC000000DULL));
    }
    if (((2) & ((unsigned __int8)(v_stack_mB70))) == 0) goto loc_009F9F28;
    result = (unsigned int)(((unsigned int)(v_stack_mC38)) & (0xFFFFFFFEULL));
    v_stack_mC24 = (unsigned int)(result);
    goto loc_009F9F42;
loc_009F9F28:
    result = (unsigned int)(((unsigned int)(v_stack_mC38)) | (1));
    v_stack_mC24 = (unsigned int)(result);
    if ((((unsigned __int8)(v_stack_mB70)) & (20)) == 0) {
        result = 0x2710ULL;
        v_stack_mC26 = (unsigned __int16)(result);
    }
    if ((((unsigned __int8)(v_stack_mB70)) & (8)) != 0) {
        result = *(unsigned __int64 *)(v_stack_mC58 + 1240);
    }
    if ((((unsigned __int8)(v_stack_mB70)) & (16)) != 0) {
        result = *(unsigned __int64 *)(v_stack_mC58 + 1240);
    }
    if (((32) & ((unsigned __int8)(v_stack_mB70))) != 0) {
        result = *(unsigned __int64 *)(v_stack_mC58 + 1240);
        a3 = 128;
    }
    if ((*(unsigned __int64 *)(v_stack_mC58 + 1240)) != 0) goto loc_009F9FDE;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC58 + 1240) + 128) = v_stack_mC28;
    result = PspAddSchedulingGroupToJobChain(*(unsigned __int64 *)(v_stack_mC58 + 1304), v_stack_mC58, a3, v_rip - 5578704);
    v_stack_mC40 = (unsigned int)(result);
    if (sign_flag) goto loc_009F9FBA;
    goto loc_009FA009;
loc_009F9FBA:
    if (*(unsigned __int64 *)(v_stack_mC58 + 1240) == 0) goto loc_009FA102;
    result = PspFreeRateControl(*(unsigned __int64 *)(v_stack_mC58 + 1240), 2, a3, v_rip - 5578704);
    *(unsigned __int64 *)(v_stack_mC58 + 1240) = 0;
    goto loc_009FA102;
loc_009F9FDE:
    v_stack_mBE8 = 2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 40)))) & (4)) == 0) goto loc_009FA004;
    result = KeSetSchedulingGroupWeights(1, v_stack_mBE8, v_stack_mC28, v_rip - 5578704);
    goto loc_009FA009;
loc_009FA004:
    result = KeSetSchedulingGroupCpuRates(1, v_stack_mBE8, v_stack_mC28, v_rip - 5578704);
loc_009FA009:
    v_stack_mB80 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 1240) + 40)));
    v_stack_mB7C = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 1240) + 44)));
    goto loc_009FA0D0;
loc_009FA030:
    result = (unsigned int)(((unsigned int)(v_stack_mC38)) | (3));
    v_stack_mC24 = (unsigned int)(result);
    v_stack_mC28 = 0x27102710ULL;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 1240) + 44) = (unsigned int)((unsigned int)(v_stack_mC28));
    a1 = (*(unsigned __int64 *)(v_stack_mC58 + 1240)) - (-128);
    v_stack_mBE8 = a1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 4))) >> (2));
    result = (unsigned __int8)((result) & (1));
    v_stack_mC3B = (unsigned __int8)(result);
    result = KeQuerySchedulingGroupReadyTime(a1, v_stack_mBE8, v_stack_mC28, v_rip - 5578704);
    result = KeSetSchedulingGroupCpuRates(a1, v_stack_mBE8, v_stack_mC28, v_rip - 5578704);
    v_stack_mB7C = (unsigned int)((unsigned int)(v_stack_mC28));
    if (v_stack_mC3B != 0) {
        v_stack_mC3B = 0;
        v_stack_mC70 = 1;
        result = v_stack_mC3B;
        v_stack_mC78 = result;
        a4 = v_rip - 5579875;
        a3 = 0;
        a2 = 0;
        a1 = v_stack_mC58;
        result = PspEnumJobsAndProcessesInJobHierarchy(a1, a2, a3, a4);
    }
    if (((*(unsigned int *)(v_rip + 6081059)) & (0x80000ULL)) != 0) {
        v_stack_mC70 = 0x725ULL;
        v_stack_mC78 = 0;
        a4 = 0;
        a3 = v_stack_mB80;
        a2 = a4 + 15;
        a1 = v_stack_mC58;
        result = EtwTraceJobSetQuery(a1, a2, a3, a4);
    }
    result = PspUnlockJobChain(v_stack_mC58, v_stack_mC10, a3, a4);
    goto loc_009FAFC8;
loc_009FA12E:
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, 1, a3, a4);
    result = KeResetEvent(v_stack_mC58, 1, a3, a4);
loc_009FA14D:
    result = ExReleaseResourceLite(v_stack_mC58 + 56, 1, a3, a4);
loc_009FA156:
    goto loc_009FAFC8;
loc_009FA15E:
    if (((unsigned int)(v_stack_mC58 + 56)) == 42) goto loc_009FAA82;
    if (((unsigned int)(v_stack_mC58 + 56)) > 42) goto loc_009FABE7;
    a1 = (unsigned int)((v_stack_mC58 + 56) - (27));
    if (condition_is_equal) goto loc_009FAA4D;
    a1 = (unsigned int)((a1) - (4));
    if (condition_is_equal) goto loc_009FA889;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009FA871;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009F880A;
    a1 = (unsigned int)((a1) - ((unsigned int)(v_stack_mC58)));
    if (condition_is_equal) goto loc_009FA348;
    a1 = (unsigned int)((a1) - ((unsigned int)(v_stack_mC58)));
    if (condition_is_equal) goto loc_009FA2C4;
    a1 = (unsigned int)((a1) - (3));
    if (condition_is_equal) goto loc_009FA245;
    if (((unsigned int)(a1)) != 1) goto loc_009FAC1E;
    v_stack_mB40 = (unsigned int)((unsigned int)(*(unsigned int *)(2)));
    result = PspJobIsAppSilo(v_stack_mC58, 1, (unsigned int)(*(unsigned int *)(2)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_009FA30F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(2)))) != 2) goto loc_009FA30F;
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, (unsigned __int8)((unsigned int)(*(unsigned int *)(2)) - 1), (unsigned int)(*(unsigned int *)(2)), a4);
    if ((*(unsigned int *)(v_stack_mC58 + 1456)) == 0) goto loc_009FA203;
    goto loc_009FA226;
loc_009FA203:
    if ((*(unsigned int *)(v_stack_mC58 + 1456)) >= 0) goto loc_009FA21B;
    goto loc_009FA226;
loc_009FA21B:
    result = PspHardDereferenceSiloWorker(v_stack_mC58, (unsigned __int8)((unsigned int)(*(unsigned int *)(2)) - 1), (unsigned int)(*(unsigned int *)(2)), a4);
loc_009FA226:
    goto loc_009F8AA1;
loc_009FA245:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 6158374), (unsigned __int8)(v_stack_mC50), (unsigned int)(*(unsigned int *)(2)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_009FA2DD;
    if (((*(unsigned int *)(v_stack_mC58 + 1552)) & (0x40000000ULL)) == 0) goto loc_009FA2F4;
    result = PspSetJobSiloThreadImpersonationPolicy(v_stack_mC58, 4, (unsigned int)(*(unsigned int *)(2)), a4);
    if ((unsigned __int8)(result) == 0) goto loc_009FA30F;
    v_stack_mAB0 = *(unsigned __int64 *)(2);
    v_stack_mB44 = (unsigned int)((unsigned int)(*(unsigned int *)(2 + 8)));
    result = PspConvertSiloToServerSilo(v_stack_mC58, (unsigned __int8)(v_stack_mC50), *(unsigned __int64 *)(2), (unsigned int)(*(unsigned int *)(2 + 8)));
    goto loc_009FAFC0;
loc_009FA2C4:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 6158249), v_stack_mC50, *(unsigned __int64 *)(2), (unsigned int)(*(unsigned int *)(2 + 8)));
    if ((unsigned __int8)(result) != 0) goto loc_009FA2E7;
loc_009FA2DD:
    goto loc_009FAFC2;
loc_009FA2E7:
    if (((*(unsigned int *)(v_stack_mC58 + 1552)) & (0x40000000ULL)) != 0) goto loc_009FA2FE;
loc_009FA2F4:
    goto loc_009FAFC2;
loc_009FA2FE:
    result = PspSetJobSiloThreadImpersonationPolicy(v_stack_mC58, 4, *(unsigned __int64 *)(2), (unsigned int)(*(unsigned int *)(2 + 8)));
    if ((unsigned __int8)(result) != 0) goto loc_009FA319;
loc_009FA30F:
    goto loc_009FAFC2;
loc_009FA319:
    v_stack_mB48 = (unsigned int)((unsigned int)(*(unsigned int *)(2)));
    result = ObCreateSiloRootDirectory(v_stack_mC58, (unsigned int)(*(unsigned int *)(2)), *(unsigned __int64 *)(2), (unsigned int)(*(unsigned int *)(2 + 8)));
    goto loc_009FAFC0;
loc_009FA348:
    result = PspCreateSilo(v_stack_mC58, (unsigned int)(*(unsigned int *)(2)), *(unsigned __int64 *)(2), (unsigned int)(*(unsigned int *)(2 + 8)));
    goto loc_009FAFC0;
loc_009FA35A:
    result = memcpy(v_stack_m990, (unsigned int)(*(unsigned int *)(2)), *(unsigned __int64 *)(2), (unsigned int)(*(unsigned int *)(2 + 8)));
    v_stack_m9E0 = (unsigned int)(v_stack_m960);
    v_stack_mA08 = v_stack_m990;
    v_stack_mA00 = v_stack_m988;
    v_stack_m9F8 = v_stack_m980;
    v_stack_m9D8 = v_stack_m978;
    v_stack_m9F0 = v_stack_m970;
    v_stack_m9E8 = (unsigned int)((unsigned int)(v_stack_m968));
    v_stack_m9E4 = (unsigned int)((unsigned int)(v_stack_m964));
    v_stack_mC20 = (unsigned int)((unsigned int)(0x278204ULL));
    goto loc_009FA47B;
loc_009FA3F1:
    result = memcpy(v_stack_m958, v_stack_m970, v_stack_m960, v_stack_m980);
    v_stack_m9E0 = (unsigned int)((unsigned int)(v_stack_m930));
    v_stack_mA08 = v_stack_m958;
    v_stack_mA00 = v_stack_m950;
    v_stack_m9F8 = v_stack_m948;
    v_stack_m9F0 = v_stack_m940;
    v_stack_m9E8 = (unsigned int)((unsigned int)(v_stack_m938));
    v_stack_m9E4 = (unsigned int)((unsigned int)(v_stack_m934));
    v_stack_mC20 = (unsigned int)((unsigned int)(0x70204ULL));
loc_009FA473:
loc_009FA47B:
    result = (unsigned int)(~((unsigned int)(0x70204ULL)));
    if ((((unsigned int)((unsigned int)(v_stack_m930))) & ((unsigned int)(result))) != 0) goto loc_009FA493;
    if (condition_is_above_or_equal) goto loc_009FA49D;
    if (v_stack_m9D8 >= ((unsigned int)(0x1000ULL))) goto loc_009FA4A8;
loc_009FA493:
    goto loc_009F8B05;
loc_009FA49D:
    v_stack_m9D8 = 0;
loc_009FA4A8:
    if (v_stack_m9D8 >= ((unsigned int)(0x1000ULL))) goto loc_009FA4BB;
    if (v_stack_m940 < ((unsigned int)(0x1000ULL))) goto loc_009FA493;
    if (v_stack_m940 >= 0) goto loc_009FA4C3;
    goto loc_009FA493;
loc_009FA4BB:
    v_stack_m9F0 = 0;
loc_009FA4C3:
    if ((((unsigned __int8)((unsigned int)(v_stack_m930))) & (4)) == 0) goto loc_009FA4D0;
    if (v_stack_m948 != 0) goto loc_009FA4D8;
    goto loc_009FA493;
loc_009FA4D0:
    v_stack_m9F8 = 0;
loc_009FA4D8:
    if (condition_is_above_or_equal) goto loc_009FA4E6;
    if (v_stack_m958 != 0) goto loc_009FA4EE;
    goto loc_009FA493;
loc_009FA4E6:
    v_stack_mA08 = 0;
loc_009FA4EE:
    if (condition_is_above_or_equal) goto loc_009FA4FC;
    if (v_stack_m950 != 0) goto loc_009FA504;
    goto loc_009FA493;
loc_009FA4FC:
    v_stack_mA00 = 0;
loc_009FA504:
loc_009FA50D:
    if (0 >= 3) goto loc_009FA57A;
    result = PspNotificationLimitRateControlToleranceField(v_stack_mA08, 0, (unsigned int)(v_stack_m930), v_stack_m948);
    result = PspNotificationLimitRateControlToleranceIntervalField(v_stack_mA08, 0, (unsigned int)(v_stack_m930), result);
    result = PspRateControlLimitFlag(0, 0, (unsigned int)(v_stack_m930), result);
    if ((((unsigned int)((unsigned int)(v_stack_m930))) & ((unsigned int)(result))) == 0) goto loc_009FA567;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result))) == 0) goto loc_009FAD04;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result)))) > 3) goto loc_009FAD04;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result))) == 0) goto loc_009FAD04;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result)))) <= 3) goto loc_009FA575;
    goto loc_009FAD04;
loc_009FA567:
    *(unsigned int *)(result) = 0;
    *(unsigned int *)(result) = 0;
loc_009FA575:
    a2 = (unsigned int)((0) + (1));
    goto loc_009FA50D;
loc_009FA57A:
    v_stack_mB78 = v_stack_mC58 + 1216;
    if ((*(unsigned __int64 *)(v_stack_mC58 + 1216)) != 0) goto loc_009FA605;
    result = ExAllocatePool2(136 + 120, 136, (unsigned int)(0x624A7350ULL), result);
    if (result != 0) goto loc_009FA5BA;
    goto loc_009FAFC8;
loc_009FA5BA:
    a3 = 0;
    result = PsChargeSharedPoolQuota(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), (unsigned int)(0xC000009AULL), a3, result);
    if (result != 0) goto loc_009FA5F4;
    result = ExFreePoolWithTag(result, (unsigned int)(0x624A7350ULL), a3, result);
    goto loc_009FAD09;
loc_009FA5F4:
    a2 = 0;
    result = memset(result, a2, (unsigned int)(0xC000009AULL), result);
    goto loc_009FA60B;
loc_009FA605:
loc_009FA60B:
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, 1, (unsigned int)(0xC000009AULL), result);
    if ((*(unsigned __int64 *)(v_stack_mB78)) != 0) goto loc_009FA630;
    *(unsigned __int64 *)(v_stack_mB78) = 0;
    *(unsigned __int64 *)(v_stack_mC58 + 1224) = 0;
    goto loc_009FA650;
loc_009FA630:
    result = v_stack_mB78;
    if (0 != 0) {
        a2 = 0x624A7350ULL;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)(0xC000009AULL), result);
        a3 = 0;
        a2 = (unsigned int)(0xC000009AULL);
        a1 = 0;
        result = PsReturnSharedPoolQuota(a1, a2, a3, result);
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC58 + 1216) + 8) = v_stack_mA08;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC58 + 1216) + 16) = v_stack_mA00;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC58 + 1216) + 24) = v_stack_m9F8;
loc_009FA684:
    if (0 == 0) goto loc_009FA6A1;
    if (0 == 1) goto loc_009FA697;
    goto loc_009FA6A9;
loc_009FA697:
    goto loc_009FA6A9;
loc_009FA6A1:
loc_009FA6A9:
    if (0 == 0) goto loc_009FA6C6;
    if (0 == 1) goto loc_009FA6BC;
    goto loc_009FA6CE;
loc_009FA6BC:
    goto loc_009FA6CE;
loc_009FA6C6:
loc_009FA6CE:
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 1216) + 60 - 12) = (unsigned int)((unsigned int)(v_stack_m9CC));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 1216) + 60) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m9C8)));
    a1 = (unsigned int)((0) + (1));
    a3 = (*(unsigned __int64 *)(v_stack_mC58 + 1216) + 60) + (4);
    if (((unsigned int)(a1)) < 3) goto loc_009FA684;
    a3 = 0;
    a2 = 0;
    result = PspLockJobMemoryLimitsExclusive(v_stack_mC58, a2, a3, (unsigned int)(v_stack_m9CC));
    result = (v_stack_m9D8) >> (12);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC58 + 1216) + 32) = result;
    result = (v_stack_m9F0) >> (12);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC58 + 1216) + 40) = result;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 1216)) = (unsigned int)((unsigned int)(v_stack_m9E0));
    v_rdi = (unsigned __int8)((32) & (6));
    result = (unsigned int)(v_stack_m9E0);
    if (((unsigned __int8)(v_rdi)) == 2) {
        a1 = v_stack_mC58 + 1264;
        result = ExfTryToWakePushLock(a1, a2, a3, (unsigned int)(v_stack_m9CC));
    }
    result = KeAbPostRelease(v_stack_mC58 + 1264, a2, a3, (unsigned int)(v_stack_m9CC));
    v_rbx = v_stack_mC58;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 1216))) & (0xFFFF7DFFULL)) != 0) {
        v_rbx = v_stack_mC58;
    }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 1216)))) != 0) goto loc_009FA780;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rbx + 1216))) != 0) goto loc_009FA78C;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mC58 + 1216)))) == 0) goto loc_009FA7AE;
loc_009FA780:
    result = *(unsigned __int64 *)(v_rbx + 1216);
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rbx + 1216))) == 0) {
        v_stack_mC70 = 5;
        v_stack_mC78 = *(unsigned __int64 *)(v_rbx + 1216);
        a4 = 0;
        a3 = 0;
        a2 = v_rip + 667002;
        a1 = v_rbx;
        result = PspEnumJobsAndProcessesInJobHierarchy(a1, a2, a3, a4);
    }
    if (((*(unsigned int *)(v_rip + 6079299)) & (0x80000ULL)) != 0) {
        v_stack_mC70 = 0x725ULL;
        v_stack_mC78 = 0;
        a4 = 0;
        a3 = v_stack_mA08;
        a2 = (unsigned int)((unsigned int)(v_stack_mC48));
        a1 = v_rbx;
        result = EtwTraceJobSetQuery(a1, a2, a3, a4);
    }
    result = ExReleaseResourceLite(v_rbx + 56, a2, a3, a4);
    a2 = 0;
    result = PspLockJobMemoryLimitsShared(v_rbx, a2, a3, a4);
    a3 = (*(unsigned __int64 *)(v_rbx + 1568)) + (*(unsigned __int64 *)(v_stack_mC58 + 1208));
    result = PspGetJobMemoryUsageNotificationViolations(v_stack_mC58, *(unsigned __int64 *)(v_stack_mC58 + 1208), a3, (unsigned int)(0x8200ULL));
    result = 17;
    if (!(condition_is_equal)) {
        a1 = v_stack_mC58 + 1264;
        result = ExfReleasePushLockShared(a1, *(unsigned __int64 *)(v_stack_mC58 + 1208), a3, (unsigned int)(0x8200ULL));
    }
    result = KeAbPostRelease(v_stack_mC58 + 1264, *(unsigned __int64 *)(v_stack_mC58 + 1208), a3, (unsigned int)(0x8200ULL));
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) {
        a1 = v_stack_mC58;
        a1 = *(unsigned __int64 *)(a1 + 1312);
        result = PspScheduleEnforcementWorker(a1, *(unsigned __int64 *)(v_stack_mC58 + 1208), a3, (unsigned int)(0x8200ULL));
    }
    goto loc_009F8BC6;
loc_009FA871:
    result = PspSetNetRateControl((unsigned int)(v_stack_mC48), 1, v_stack_mC58, (unsigned int)(0x8200ULL));
    goto loc_009FAFC0;
loc_009FA889:
    v_stack_mBF0 = 0;
    result = memcpy(v_stack_mA98, (unsigned int)(v_stack_mC48), 1, (unsigned int)(0x8200ULL));
    if (v_stack_mA80 == 0) goto loc_009FA9AD;
    if ((unsigned __int16)(v_stack_mA70) == 0) goto loc_009FA995;
    if (((1) & ((unsigned __int8)(v_stack_mA80))) != 0) {
        result = ExRaiseDatatypeMisalignment(v_stack_mA70, v_stack_mA80, 1, (unsigned int)(0x8200ULL));
    }
    if ((v_stack_mA80 + v_stack_mA70 * 1) > result) goto loc_009FA8F1;
    v_rbx = 0;
    if ((v_stack_mA80 + v_stack_mA70 * 1) < v_stack_mA80) {
        result = *(unsigned __int8 *)(result);
        a1 = v_stack_mA70;
        v_rbx = v_stack_mBF0;
    }
    if ((unsigned __int16)(a1) == 0) goto loc_009FA995;
    if (((1) & ((unsigned __int8)(a1))) != 0) goto loc_009FA995;
    a2 = ((unsigned __int16)(a1)) + (v_stack_mC58);
    result = 32;
    if (v_stack_mC50 == 1) { result = 257; }
    result = ExAllocatePool2((unsigned int)((unsigned int)(result)), a2, (unsigned int)(0x624A7350ULL), (unsigned int)(0x8200ULL));
    v_stack_mBF0 = result;
    if (result != 0) goto loc_009FA962;
    v_stack_mC40 = (unsigned int)((unsigned int)(0xC0000017ULL));
    goto loc_009FAA35;
loc_009FA962:
    result = memcpy(result, v_stack_mA80, v_stack_mA70, (unsigned int)(0x8200ULL));
    result = (v_stack_mA70) >> (1);
    *(unsigned __int16 *)(result + result * 2) = 0;
    v_stack_mA80 = result;
    goto loc_009FA9AD;
loc_009FA995:
    v_stack_mC40 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_009FAA35;
loc_009FA9AD:
    if (((v_stack_mA74) & (0xFFFFFFF0ULL)) == 0) goto loc_009FA9CB;
loc_009FA9BF:
loc_009FA9C4:
    goto loc_009FAA35;
loc_009FA9CB:
    if (v_stack_mA60 != 0) goto loc_009FA9E9;
    if (v_stack_mA88 != 0) goto loc_009FA9E9;
    if (v_stack_mA48 == 0) goto loc_009FA9F9;
loc_009FA9E9:
    result = EtwpCoverageUserIsAdmin(result, v_stack_mA80, v_stack_mA70, (unsigned int)(0x8200ULL));
    if ((unsigned __int8)(result) != 0) goto loc_009FA9F9;
    goto loc_009FA9BF;
loc_009FA9F9:
    result = PspSetJobIoRateControl(v_stack_mC58, v_stack_mA98, v_stack_mA70, (unsigned int)(0x8200ULL));
    goto loc_009FA9C4;
loc_009FAA35:
    if (result == 0) goto loc_009FAFC8;
    a2 = 0;
loc_009FAA43:
    result = ExFreePoolWithTag(result, a2, v_stack_mA70, (unsigned int)(0x8200ULL));
    goto loc_009FAFE1;
loc_009FAA4D:
    a3 = 0;
    a2 = 0;
    result = PspLockJobMemoryLimitsExclusive(v_stack_mC58, a2, a3, (unsigned int)(0x8200ULL));
    *(unsigned __int64 *)(v_stack_mC58 + 720) = 0;
    *(unsigned __int64 *)(v_stack_mC58 + 712) = 0;
    a3 = 0;
    a2 = 0;
    result = PspUnlockJobMemoryLimitsExclusive(v_stack_mC58, a2, a3, (unsigned int)(0x8200ULL));
    goto loc_009FAFC2;
loc_009FAA82:
    v_stack_mB08 = v_xmm0;
    v_stack_mAF8 = v_xmm1;
    v_stack_mAE8 = v_xmm0;
    v_stack_mAD8 = v_xmm1;
    v_stack_mAC8 = v_xmm0;
    if (((v_stack_mB08) & (0xFFFFFFFCULL)) == 0) goto loc_009FAAEF;
loc_009FAAE0:
loc_009FAAE5:
    goto loc_009FABB4;
loc_009FAAEF:
    if (((v_stack_mB08) & (3)) == 0) goto loc_009FAAE0;
    v_rdi = (unsigned __int8)((v_stack_mB08) & (1));
    result = PspLockRootJobExclusive(v_stack_mC58, v_stack_mC10, v_stack_mBE8, (unsigned int)(0x8200ULL));
loc_009FAB21:
    if (0 >= 1) goto loc_009FAB37;
    if (v_stack_mC58 == (*(unsigned __int64 *)(v_rsp + 0 * 8 + 176))) goto loc_009FAB43;
    a1 = (unsigned int)((0) + (1));
    goto loc_009FAB21;
loc_009FAB37:
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, 1, v_stack_mBE8, (unsigned int)(0x8200ULL));
loc_009FAB43:
    result = PspSetJobIoAttribution(v_stack_mC58, (unsigned __int8)(v_rdi), 1, 1);
    if (sign_flag) goto loc_009FAAE5;
loc_009FAB5D:
    if (0 >= 1) goto loc_009FAB73;
    if (v_stack_mC58 == (*(unsigned __int64 *)(v_rsp + 0 * 8 + 176))) goto loc_009FAB7C;
    a1 = (unsigned int)((0) + (1));
    goto loc_009FAB5D;
loc_009FAB73:
    result = ExReleaseResourceLite(v_stack_mC58 + 56, (unsigned __int8)(v_rdi), 1, 1);
loc_009FAB7C:
    result = PspUnlockJob(v_stack_mBE8, v_stack_mC10, 1, 1);
    goto loc_009FAAE5;
loc_009FABB4:
    if (0 != 8) goto loc_009FAFC8;
    result = PspUnlockJobConditionally(v_stack_mC58, v_stack_mBE8, 1, 1);
    result = PspUnlockJob(v_stack_mBE8, v_stack_mC10, 1, 1);
    goto loc_009FAFE1;
loc_009FABE7:
    a1 = (unsigned int)((v_stack_mBE8) - (43));
    if (condition_is_equal) goto loc_009FAFA3;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009FAF38;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009FADC0;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009FAD83;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009FACEE;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_009FAC92;
    if (((unsigned int)(a1)) == 1) goto loc_009FAC28;
loc_009FAC1E:
    goto loc_009F8B05;
loc_009FAC28:
    v_stack_mBF8 = *(unsigned __int64 *)((unsigned int)(v_stack_mC48));
    if ((((unsigned int)(*(unsigned __int64 *)((unsigned int)(v_stack_mC48)))) & (0xFFFFFFFEULL)) != 0) goto loc_009FAD04;
    a2 = (*(unsigned __int64 *)((unsigned int)(v_stack_mC48))) >> (32);
    if (a2 >= 8) goto loc_009FAD04;
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)((unsigned int)(v_stack_mC48))))) == 0) goto loc_009FAC69;
    if (a2 == 0) goto loc_009FAD43;
    goto loc_009FAC6E;
loc_009FAC69:
loc_009FAC6E:
    result = PspSetPagePriorityLimitJobTree(v_stack_mC58, 8, 1, 1);
    goto loc_009FA156;
loc_009FAC92:
    v_stack_mBF8 = *(unsigned __int64 *)((unsigned int)(v_stack_mC48));
    if ((((unsigned int)(*(unsigned __int64 *)((unsigned int)(v_stack_mC48)))) & (0xFFFFFFFEULL)) != 0) goto loc_009FAD04;
    a2 = (*(unsigned __int64 *)((unsigned int)(v_stack_mC48))) >> (32);
    if (a2 >= 5) goto loc_009FAD43;
    if (((1) & ((unsigned __int8)(*(unsigned __int64 *)((unsigned int)(v_stack_mC48))))) == 0) {
        a2 = 1 + 4;
    }
    result = PspSetIoPriorityLimitJobTree(v_stack_mC58, a2, 1, 1);
    goto loc_009FA156;
loc_009FACEE:
    v_stack_mBFF = (unsigned __int8)(*(unsigned __int8 *)((unsigned int)(v_stack_mC48)));
    if (((unsigned __int8)(*(unsigned __int8 *)((unsigned int)(v_stack_mC48)))) == 1) goto loc_009FAD13;
loc_009FAD04:
loc_009FAD09:
    goto loc_009FAFC8;
loc_009FAD13:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 6155610), v_stack_mC50, 1, 1);
    if ((unsigned __int8)(result) != 0) goto loc_009FAD36;
    goto loc_009FAFC8;
loc_009FAD36:
    if (((*(unsigned int *)(v_stack_mC58 + 1552)) & (0x40000000ULL)) != 0) goto loc_009FAD4D;
loc_009FAD43:
    goto loc_009FAFC8;
loc_009FAD4D:
    result = PspSetJobSiloThreadImpersonationPolicy(v_stack_mC58, 2, 1, 1);
    result = (unsigned __int8)(-(result));
    a1 = (unsigned int)(~(v_stack_mC58));
    v_rsi = (unsigned int)(((unsigned int)(0xC0000022ULL)) & ((unsigned int)(a1)));
    goto loc_009FAFC8;
loc_009FAD83:
    v_stack_mB50 = *(unsigned __int64 *)((unsigned int)(v_stack_mC48));
    result = PspSetEnergyTrackingStateJobTree(v_stack_mC58, v_stack_mB50, 1, 1);
    goto loc_009F9C7B;
loc_009FADC0:
    if (((*(unsigned int *)(v_stack_mC58 + 1552)) & (0x40000000ULL)) == 0) goto loc_009FA2F4;
    v_stack_mB68 = 0;
    v_stack_mBF8 = v_xmm0;
    if (0 == 0) goto loc_009FAEF1;
    result = (unsigned __int16)(((unsigned __int16)(v_stack_mBF8)) - (1));
    if (((unsigned __int16)(result)) > 518) goto loc_009FAEF1;
    if (((1) & ((unsigned __int8)(v_stack_mBF8))) != 0) goto loc_009FAEF1;
    if (v_stack_mC50 != 1) goto loc_009FAE6A;
    if (((1) & (0)) != 0) {
        result = ExRaiseDatatypeMisalignment(518, v_stack_mB50, 1, 1);
    }
    if ((0 + v_stack_mBF8 * 1) > result) goto loc_009FAE53;
    v_rbx = 0;
    v_rsi = v_stack_mBF8;
    v_r14 = v_stack_mC58;
    if ((0 + v_stack_mBF8 * 1) < 0) {
        result = *(unsigned __int8 *)(result);
        v_r14 = v_stack_mC58;
        v_rbx = v_stack_mBF0;
        v_rsi = v_stack_mBF8;
    }
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned __int16)(v_rsi))), (unsigned int)(0x72537350ULL), 1);
    v_stack_mB68 = result;
    if (result != 0) goto loc_009FAEA4;
    v_stack_mC40 = (unsigned int)((unsigned int)(0xC000009AULL));
    goto loc_009FAFE1;
loc_009FAEA4:
    result = memcpy(result, v_rbx, (unsigned int)(v_stack_mC48), 1);
    v_rbx = ((unsigned __int16)((unsigned int)(0xC000009AULL))) >> (1);
    result = wcsnlen(result, v_rbx, (unsigned int)(v_stack_mC48), 1);
    if (result == v_rbx) goto loc_009FAED5;
loc_009FAECE:
    goto loc_009FAF22;
loc_009FAED5:
    v_stack_mBF0 = result;
    result = PspAssignSiloSystemRootPath(v_r14, v_stack_mBF8, (unsigned int)(v_stack_mC48), 1);
    goto loc_009FAECE;
loc_009FAEF1:
    v_stack_mC40 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_009FAFE1;
loc_009FAF22:
    if (result == 0) goto loc_009FAFE1;
    goto loc_009FAA43;
loc_009FAF38:
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, 1, (unsigned int)(v_stack_mC48), 1);
    if ((*(unsigned int *)(v_stack_mC58 + 1552)) >= 0) goto loc_009FAF62;
    goto loc_009F8A9D;
loc_009FAF62:
    *(unsigned __int64 *)(v_stack_mC58 + 1488) = v_xmm0;
    goto loc_009FA14D;
loc_009FAFA3:
    v_stack_mAA8 = *(unsigned __int64 *)((unsigned int)(v_stack_mC48));
    result = PspSetJobMemoryPartition(v_stack_mC58, v_stack_mC50, *(unsigned __int64 *)((unsigned int)(v_stack_mC48)), 1);
loc_009FAFC0:
loc_009FAFC2:
loc_009FAFC8:
    goto loc_009FAFE1;
loc_009FAFE1:
    if ((*(unsigned int *)(v_stack_mC58 + 1552)) != 0) goto loc_009FB006;
    result = v_stack_mC10 + 152;
    if ((*(unsigned __int64 *)(v_stack_mC10 + 152)) != (v_stack_mC10 + 152)) {
        result = KiCheckForKernelApcDelivery(v_stack_mC10, v_stack_mC50, *(unsigned __int64 *)((unsigned int)(v_stack_mC48)), 1);
    }
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_009FB032;
    if (((*(unsigned int *)(v_rip + 6077164)) & (0x80000ULL)) != 0) {
        v_stack_mC70 = 0x727ULL;
        v_stack_mC78 = (unsigned int)((unsigned int)((unsigned int)(result)));
        a4 = 0;
        a3 = 0;
        a2 = (unsigned int)((unsigned int)(v_stack_mC48));
        a1 = v_stack_mC58;
        result = EtwTraceJobSetQuery(a1, a2, a3, a4);
    }
    result = ObfDereferenceObjectWithTag(v_stack_mC58, (unsigned int)(0x79517350ULL), a3, a4);
    goto loc_009FB048;
loc_009FB043:
loc_009FB048:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(0x79517350ULL), a3, a4);
    v_rsp = (v_rsp) + (0xC60ULL);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtSetInformationJobObject(int64_t Arg1, void *Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m32B;
    uint64_t v_stack_m48;
    uint64_t v_stack_m4B8;
    uint64_t v_stack_m4C0;
    uint64_t v_stack_m4C8;
    uint32_t v_stack_m534;
    uint64_t v_stack_m668;
    uint64_t v_stack_m670;
    uint32_t v_stack_m674;
    uint32_t v_stack_m678;
    uint64_t v_stack_m680;
    uint64_t v_stack_m688;
    uint64_t v_stack_m690;
    uint64_t v_stack_m698;
    uint64_t v_stack_m778;
    uint64_t v_stack_m880;
    uint64_t v_stack_m888;
    uint64_t v_stack_m898;
    uint64_t v_stack_m8B0;
    uint64_t v_stack_m8B8;
    uint32_t v_stack_m8EC;
    uint32_t v_stack_m8F0;
    uint64_t v_stack_m8F8;
    uint32_t v_stack_m900;
    uint64_t v_stack_m908;
    uint64_t v_stack_m910;
    uint32_t v_stack_m918;
    uint64_t v_stack_m920;
    uint64_t v_stack_m928;
    uint32_t v_stack_m930;
    uint32_t v_stack_m934;
    uint64_t v_stack_m938;
    uint64_t v_stack_m940;
    uint64_t v_stack_m948;
    uint64_t v_stack_m950;
    uint64_t v_stack_m958;
    uint64_t v_stack_m960;
    uint32_t v_stack_m964;
    uint32_t v_stack_m968;
    uint64_t v_stack_m970;
    uint64_t v_stack_m978;
    uint64_t v_stack_m980;
    uint64_t v_stack_m988;
    uint64_t v_stack_m990;
    uint64_t v_stack_m9A0;
    uint32_t v_stack_m9A8;
    uint64_t v_stack_m9B0;
    uint32_t v_stack_m9B4;
    uint64_t v_stack_m9B8;
    uint64_t v_stack_m9C8;
    uint32_t v_stack_m9CC;
    uint64_t v_stack_m9D0;
    uint64_t v_stack_m9D8;
    uint32_t v_stack_m9DC;
    uint32_t v_stack_m9E0;
    uint32_t v_stack_m9E4;
    uint32_t v_stack_m9E8;
    uint64_t v_stack_m9F0;
    uint64_t v_stack_m9F8;
    uint64_t v_stack_mA00;
    uint64_t v_stack_mA08;
    uint64_t v_stack_mA48;
    uint64_t v_stack_mA60;
    uint16_t v_stack_mA70;
    uint32_t v_stack_mA74;
    uint64_t v_stack_mA80;
    uint64_t v_stack_mA88;
    uint64_t v_stack_mA98;
    uint64_t v_stack_mAA8;
    uint64_t v_stack_mAB0;
    uint64_t v_stack_mAB8;
    uint64_t v_stack_mAC8;
    uint64_t v_stack_mAD8;
    uint64_t v_stack_mAE8;
    uint64_t v_stack_mAF8;
    uint64_t v_stack_mB08;
    uint32_t v_stack_mB10;
    uint64_t v_stack_mB20;
    uint64_t v_stack_mB30;
    uint32_t v_stack_mB38;
    uint32_t v_stack_mB3C;
    uint32_t v_stack_mB40;
    uint32_t v_stack_mB44;
    uint32_t v_stack_mB48;
    uint64_t v_stack_mB50;
    uint16_t v_stack_mB58;
    uint64_t v_stack_mB60;
    uint64_t v_stack_mB68;
    uint32_t v_stack_mB6C;
    uint64_t v_stack_mB70;
    uint64_t v_stack_mB78;
    uint32_t v_stack_mB7C;
    uint64_t v_stack_mB80;
    uint64_t v_stack_mB88;
    uint32_t v_stack_mB8C;
    uint32_t v_stack_mB90;
    uint64_t v_stack_mB98;
    uint32_t v_stack_mBA0;
    uint64_t v_stack_mBB0;
    uint64_t v_stack_mBB8;
    uint64_t v_stack_mBC0;
    uint32_t v_stack_mBC8;
    uint64_t v_stack_mBD0;
    uint64_t v_stack_mBD8;
    uint64_t v_stack_mBE0;
    uint64_t v_stack_mBE8;
    uint64_t v_stack_mBF0;
    uint64_t v_stack_mBF8;
    uint16_t v_stack_mBFE;
    uint8_t v_stack_mBFF;
    uint8_t v_stack_mC00;
    uint64_t v_stack_mC08;
    uint64_t v_stack_mC10;
    uint64_t v_stack_mC18;
    uint32_t v_stack_mC20;
    uint32_t v_stack_mC24;
    uint16_t v_stack_mC26;
    uint64_t v_stack_mC28;
    uint16_t v_stack_mC2C;
    uint8_t v_stack_mC30;
    uint32_t v_stack_mC38;
    uint8_t v_stack_mC3B;
    uint8_t v_stack_mC3C;
    uint32_t v_stack_mC40;
    uint32_t v_stack_mC48;
    uint8_t v_stack_mC50;
    uint64_t v_stack_mC58;
    uint64_t v_stack_mC60;
    uint64_t v_stack_mC68;
    uint64_t v_stack_mC70;
    uint32_t v_stack_mC78;
    uint32_t v_stack_mC98;

    local_rsp = (local_rsp) - (0xC60ULL);
    result = (*(uint64_t *)(v_rip + 0x412266)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_mC48 = (uint32_t)((int32_t)(Arg2));
    v_stack_mC18 = Arg1;
    v_stack_mC38 = (uint32_t)((int32_t)(Arg2));
    v_stack_mBD0 = Arg3;
    Arg2 = 0;
    result = memset(v_stack_m880, Arg2, 256, Arg4);
    local_r15 = 0;
    v_stack_mB80 = 0;
    v_stack_mB70 = 0;
    v_stack_mC3C = 0;
    v_stack_mB50 = 0;
    Arg2 = 0;
    result = memset(v_stack_m928, Arg2, 152, Arg4);
    v_stack_m9A0 = v_xmm0;
    v_stack_mB60 = v_xmm1;
    v_stack_mBF8 = 0;
    Arg2 = 0;
    result = memset(v_stack_mA98, Arg2, 144, Arg4);
    v_stack_mC58 = 0;
    v_stack_mB30 = v_xmm0;
    v_stack_mB20 = v_xmm0;
    result = 0;
    v_stack_mBC0 = v_xmm0;
    v_stack_mBB0 = v_xmm0;
    v_stack_mBA0 = 0;
    Arg2 = 0;
    result = memset(v_stack_mA08, Arg2, local_r15 + 72, Arg4);
    v_stack_m958 = v_xmm0;
    v_stack_m948 = v_xmm0;
    v_stack_m938 = v_xmm0;
    result = 0;
    v_stack_m990 = v_xmm1;
    v_stack_m980 = v_xmm1;
    v_stack_m970 = v_xmm1;
    v_stack_m960 = 0;
    v_stack_mC28 = 0;
    v_stack_mC3B = 0;
    v_stack_m9B8 = v_xmm0;
    v_stack_m9A8 = 0;
    v_stack_mBE8 = 0;
    v_stack_mB98 = v_xmm0;
    if (((uint32_t)((int32_t)(Arg2) - 1)) > 50) goto loc_009FB043;
    if (((uint32_t)((int32_t)(Arg2))) == 9) goto loc_009F86E3;
    if (((uint32_t)((int32_t)(Arg2))) == 12) goto loc_009F86D7;
    if (((uint32_t)((int32_t)(Arg2))) == 31) goto loc_009F8679;
    if (((uint32_t)((uint32_t)(Arg4))) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x9F865C + (int32_t)(arg2) * 4 + 0xB4E52C))))) goto loc_009F8692;
    if (((uint32_t)((int32_t)(Arg2))) == 11) goto loc_009F8672;
    if (((uint32_t)((int32_t)(Arg2))) != 14) goto loc_009F86EF;
loc_009F8672:
    if (((uint32_t)((uint32_t)(Arg4))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x9F865C + (int32_t)(arg2) * 4 + 0xB4E52C))))) goto loc_009F8692;
    goto loc_009F86EF;
loc_009F8679:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) - (48));
    if (condition_is_equal) goto loc_009F868B;
    result = (uint32_t)((result) - (48));
    if (condition_is_equal) goto loc_009F868B;
loc_009F8689:
    if (((uint32_t)(result)) != 48) goto loc_009F86EF;
loc_009F868B:
loc_009F8692:
    v_stack_mC10 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_mC50 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_mC30 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_009F8726;
    if ((uint32_t)((uint32_t)(Arg4)) == 0) goto loc_009F871B;
    if (((v_stack_mBD0) & ((uint32_t)(*(uint32_t *)(v_rip - 0x9F8692 + (int32_t)(arg2) * 4 + 0xB4E5FC)) - 1)) == 0) goto loc_009F86F9;
    result = ExRaiseDatatypeMisalignment((uint32_t)(*(uint32_t *)(v_rip - 0x9F8692 + (int32_t)(arg2) * 4 + 0xB4E5FC)) - 1, v_rip - 10454674, local_r15 + 72, Arg4);
loc_009F86D7:
    if (((uint32_t)((uint32_t)(Arg4))) == 48) goto loc_009F868B;
    goto loc_009F8689;
loc_009F86E3:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) - (144));
    if (condition_is_equal) goto loc_009F868B;
    if (((uint32_t)(result)) == 8) goto loc_009F868B;
loc_009F86EF:
    goto loc_009FB048;
loc_009F86F9:
    if (((uint32_t)(Arg4) + v_stack_mBD0 * 1) > ((uint32_t)(0xC0000004ULL))) goto loc_009F8711;
    result = (uint32_t)(0xC0000004ULL);
    local_r13 = v_stack_mBD0;
    if (((uint32_t)(Arg4) + v_stack_mBD0 * 1) < v_stack_mBD0) {
        result = *(uint8_t *)((uint32_t)(0xC0000004ULL));
        local_r13 = v_stack_mBD0;
    }
    goto loc_009F872E;
loc_009F8726:
loc_009F872E:
    if (Arg1 != 0) goto loc_009F873D;
    goto loc_009FB048;
loc_009F873D:
    Arg2 = 16;
    if (((uint32_t)((int32_t)(Arg2))) != 5) { Arg2 = (uint32_t)(16 - 14); }
    v_stack_mC60 = 0;
    v_stack_mC68 = 0;
    v_stack_mC70 = v_stack_mC58;
    v_stack_mC78 = 0x79517350ULL;
    result = ObpReferenceObjectByHandleWithTag(Arg1, Arg2, *(uint64_t *)(v_rip + 0x5CE514), (uint8_t)((uint32_t)(0xC0000008ULL)));
    if (sign_flag) goto loc_009FB048;
    v_stack_mC40 = 0;
    local_rdi = (Arg1) | (-1);
    if (((uint32_t)((uint32_t)(v_stack_mC48))) > 25) goto loc_009FA15E;
    if (((uint32_t)((uint32_t)(v_stack_mC48))) == 25) goto loc_009FA12E;
    if (((uint32_t)((uint32_t)(v_stack_mC48))) > 14) goto loc_009F9A4B;
    if (((uint32_t)((uint32_t)(v_stack_mC48))) == 14) goto loc_009F9592;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mC48)))) - ((uint32_t)(16 - 14)));
    if (condition_is_equal) goto loc_009F8B66;
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(16 - 14)));
    if (condition_is_equal) goto loc_009F8B26;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_009F8AC2;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_009F8A6B;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_009F8867;
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(16 - 14)));
    if (condition_is_equal) goto loc_009F8B66;
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(16 - 14)));
    if (condition_is_equal) goto loc_009F9592;
    if (Arg2 != 1) goto loc_009FAC1E;
loc_009F880A:
    if (((uint32_t)((uint32_t)(Arg4))) == 48) goto loc_009FA3F1;
    if (((uint32_t)((uint32_t)(Arg4))) == 56) goto loc_009FA35A;
    result = memcpy(v_stack_mA08, v_stack_mBD0, (uint32_t)(Arg4), (uint8_t)((uint32_t)(0xC0000008ULL)));
    v_stack_mC20 = (uint32_t)((uint32_t)(0x1F8204ULL));
    goto loc_009FA473;
loc_009F8867:
    v_stack_mBE8 = v_xmm0;
    if (v_stack_mBE0 != 0) goto loc_009F88E6;
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, (uint8_t)(v_stack_mBE0 + 1), (uint32_t)(v_stack_m9E0), v_stack_m9F8);
    Arg3 = 0;
    Arg2 = 0;
    result = PspLockJobMemoryLimitsExclusive(v_stack_mC58, Arg2, Arg3, v_stack_m9F8);
    *(uint64_t *)(v_stack_mC58 + 0x228) = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = PspUnlockJobMemoryLimitsExclusive(v_stack_mC58, Arg2, Arg3, v_stack_m9F8);
    result = ExReleaseResourceLite(v_stack_mC58 + 56, Arg2, Arg3, v_stack_m9F8);
    if (*(uint64_t *)(v_stack_mC58 + 0x228) == 0) goto loc_009FAFC8;
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(v_stack_mC58 + 0x228), (uint32_t)(0x624A7350ULL), Arg3, v_stack_m9F8);
    goto loc_009FAFC8;
loc_009F88E6:
    v_stack_mC60 = 0;
    v_stack_mC68 = 0;
    v_stack_mC70 = v_stack_mBF8;
    v_stack_mC78 = 0x624A7350ULL;
    result = ObpReferenceObjectByHandleWithTag(*(uint64_t *)(v_stack_mC58 + 0x228), (uint32_t)((uint32_t)(v_stack_mC58)), *(uint64_t *)(v_rip + 0x5CE3D3), v_stack_mC50);
    if (sign_flag) goto loc_009F8949;
    if ((*(uint64_t *)(v_stack_mC58 + 0x4D0)) != 0) goto loc_009F8954;
    result = IoAllocateMiniCompletionPacket(v_rip + 455161, v_stack_mC58, *(uint64_t *)(v_rip + 0x5CE3D3), v_stack_mC50);
    if (result != 0) goto loc_009F8954;
loc_009F8949:
    goto loc_009F8A51;
loc_009F8954:
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, 1, *(uint64_t *)(v_rip + 0x5CE3D3), v_stack_mC50);
    if ((*(uint64_t *)(v_stack_mC58 + 0x228)) != 0) goto loc_009F8A16;
    if (((*(uint32_t *)(v_stack_mC58 + 0x100)) & (0x2000ULL)) == 0) goto loc_009F8990;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mC58 + 0x610))))) != 0) goto loc_009F8A16;
loc_009F8990:
    local_rdi = result;
    if ((*(uint64_t *)(v_stack_mC58 + 0x4D0)) == 0) {
        *(uint64_t *)(v_stack_mC58 + 0x4D0) = result;
        local_rdi = 0;
    }
    Arg3 = 0;
    Arg2 = 0;
    result = PspLockJobMemoryLimitsExclusive(v_stack_mC58, Arg2, Arg3, v_stack_mC50);
    *(uint64_t *)(v_stack_mC58 + 0x230) = v_stack_mBE8;
    *(uint64_t *)(v_stack_mC58 + 0x228) = v_stack_mBF8;
    *(uint64_t *)(v_stack_mC58 + 0x238) = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = PspUnlockJobMemoryLimitsExclusive(v_stack_mC58, Arg2, Arg3, v_stack_mC50);
    result = (uint32_t)(*(uint32_t *)(v_stack_mC58 + 0x450));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mC58 + 0x450)))) & (64)) != 0) {
        v_stack_mC70 = 1;
        v_stack_mC78 = v_stack_mC58;
        Arg4 = v_rip + 567442;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_stack_mC58;
        result = PspEnumJobsAndProcessesInJobHierarchy(Arg1, Arg2, Arg3, Arg4);
    }
    result = ExReleaseResourceLite(v_stack_mC58 + 56, Arg2, Arg3, Arg4);
    goto loc_009F8A51;
loc_009F8A16:
    result = ExReleaseResourceLite(v_stack_mC58 + 56, Arg2, Arg3, Arg4);
    result = ObfDereferenceObjectWithTag(v_stack_mBF8, (uint32_t)(0x624A7350ULL), Arg3, Arg4);
    goto loc_009F8A51;
loc_009F8A51:
    if (local_rdi == 0) goto loc_009FAFC8;
    *(uint64_t *)(local_rdi + 0x38) = 0;
    result = IopFreeMiniCompletionPacket(local_rdi, (uint32_t)(0x624A7350ULL), Arg3, Arg4);
    goto loc_009FAFC8;
loc_009F8A6B:
    v_stack_mB10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mBD0)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mBD0)))) > 1) goto loc_009FAD43;
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, 1, Arg3, Arg4);
    *(uint32_t *)(v_stack_mC58 + 0x224) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mBD0)));
loc_009F8A9D:
loc_009F8AA1:
    result = ExReleaseResourceLite(v_stack_mC58 + 56, 1, Arg3, Arg4);
    goto loc_009FAFC8;
loc_009F8AC2:
    v_stack_mB08 = v_xmm0;
    v_stack_mAF8 = v_xmm1;
    v_stack_mAE8 = v_xmm0;
    result = (uint32_t)(((uint32_t)(v_stack_mB08)) & (0xFFFFFFF0ULL));
    result = (uint32_t)(-(result));
    local_rsi = (uint32_t)(((uint32_t)(0xC000000DULL)) & (0xFFFFFF52ULL));
    local_rsi = (uint32_t)((local_rsi) + (0xC00000BBULL));
loc_009F8B05:
    goto loc_009FAFC2;
loc_009F8B26:
    v_stack_mB38 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mBD0)));
    Arg4 = 0;
    result = PspSetUILimitJobObject(v_stack_mC58, v_stack_mC10, (uint32_t)(*(uint32_t *)(v_stack_mBD0)), Arg4);
    goto loc_009FAFC0;
loc_009F8B66:
    result = memcpy(v_stack_m928, v_stack_mBD0, 1, Arg4);
    if (1 < 152) {
        Arg2 = (152) - (1);
        Arg1 = v_stack_m928;
        Arg1 = (Arg1) + (1);
        Arg3 = Arg2;
        Arg2 = 0;
        result = memset(Arg1, Arg2, Arg3, Arg4);
    }
    result = PspGetJobLimitInformationValidFlags((uint32_t)((uint32_t)((uint32_t)(v_stack_mC48))), 1, Arg3, Arg4);
    v_stack_mC20 = (uint32_t)(result);
    result = (uint32_t)(~(result));
    if (((v_stack_m918) & ((uint32_t)(result))) == 0) goto loc_009F8BD0;
loc_009F8BC1:
loc_009F8BC6:
    goto loc_009FAFE1;
loc_009F8BD0:
    Arg2 = 0;
    result = memset(v_stack_m778, Arg2, (uint32_t)(0x728ULL), Arg4);
    result = 0;
    v_stack_mBC0 = v_xmm0;
    v_stack_mBB0 = v_xmm0;
    v_stack_mBA0 = 0;
    v_stack_m678 = (uint32_t)((uint32_t)(v_stack_m918));
    v_stack_mC48 = 0;
    v_stack_mC08 = 0;
    v_stack_mBD8 = 0;
    result = (uint8_t)(((uint8_t)((uint32_t)(v_stack_m918))) & (8));
    result = (uint8_t)(-(result));
    Arg1 = (uint32_t)((v_stack_m778) & (v_stack_m900));
    v_stack_m674 = (uint32_t)(Arg1);
    if (((32) & ((uint8_t)((uint32_t)(v_stack_m918)))) == 0) goto loc_009F8CA5;
    if (((uint32_t)((uint32_t)(v_stack_m8F0))) > 6) goto loc_009F8BC1;
    result = (uint32_t)(((uint32_t)(v_stack_m8F0)) + (-3));
    if (((uint32_t)(result)) > ((uint32_t)(32 - 31))) goto loc_009F8C95;
    result = SeCheckPrivilegedObject(*(uint64_t *)(v_rip + 0x5E0E6E), v_stack_mC18, 32 - 30, v_stack_mC50);
    result = (uint8_t)((result) & ((uint8_t)(32 - 31)));
    local_rbx = (uint8_t)(((uint8_t)(result)) << (2));
    if ((uint8_t)(result) != 0) goto loc_009F8C95;
loc_009F8C8B:
    goto loc_009F8BC6;
loc_009F8C95:
    v_stack_m32B = (uint8_t)((uint32_t)(v_stack_m8F0));
    goto loc_009F8CAD;
loc_009F8CA5:
    v_stack_m32B = 0;
loc_009F8CAD:
    if (((v_stack_m918) & (128)) == 0) goto loc_009F8D07;
    if (((uint32_t)((uint32_t)(v_stack_m8EC))) >= 10) goto loc_009F8BC1;
    if (((uint32_t)((uint32_t)(v_stack_m8EC))) <= 5) goto loc_009F8CFE;
    result = SeCheckPrivilegedObject(*(uint64_t *)(v_rip + 0x5E0E02), v_stack_mC18, 2, v_stack_mC50);
    result = (uint8_t)((result) & ((uint8_t)(32 - 31)));
    local_rbx = (uint8_t)(((uint8_t)(result)) << (2));
    if ((uint8_t)(result) == 0) goto loc_009F8C8B;
loc_009F8CFE:
    v_stack_m534 = (uint32_t)((uint32_t)(v_stack_m8EC));
    goto loc_009F8D12;
loc_009F8D07:
    v_stack_m534 = 5;
loc_009F8D12:
    if (((v_stack_m918) & (2)) == 0) goto loc_009F8D37;
    if (v_stack_m928 == 0) goto loc_009F8BC1;
    v_stack_m698 = v_stack_m928;
    goto loc_009F8D3F;
loc_009F8D37:
    v_stack_m698 = 0;
loc_009F8D3F:
    if (((v_stack_m918) & (4)) == 0) goto loc_009F8D62;
    if (v_stack_m920 == 0) goto loc_009F8BC1;
    v_stack_m690 = v_stack_m920;
loc_009F8D62:
    if (((v_stack_m918) & ((uint8_t)(32 - 31))) == 0) goto loc_009F8DFC;
    if (v_stack_m910 != 0) goto loc_009F8D8B;
    if (v_stack_m908 == 0) goto loc_009F8BC1;
loc_009F8D8B:
    if (v_stack_m910 != local_rdi) goto loc_009F8D9E;
    if (v_stack_m908 == local_rdi) goto loc_009F8BC1;
loc_009F8D9E:
    if (v_stack_m910 > v_stack_m908) goto loc_009F8BC1;
    if (v_stack_m910 < 0x14000ULL) goto loc_009F8BC1;
    if (v_stack_m910 <= (*(uint64_t *)(v_rip + 0x5DF480))) goto loc_009F8DE2;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x5E0D1B), v_stack_mC50, 2, v_stack_mC50);
    if ((uint8_t)(result) == 0) goto loc_009F8C8B;
loc_009F8DE2:
    v_stack_m688 = v_stack_m910;
    v_stack_m680 = v_stack_m908;
    goto loc_009F8E0C;
loc_009F8DFC:
    v_stack_m688 = 0;
    v_stack_m680 = 0;
loc_009F8E0C:
    if (((v_stack_m918) & (256)) == 0) goto loc_009F8E3E;
    if (v_stack_m8B8 < ((uint32_t)(0x1000ULL))) goto loc_009F8BC1;
    Arg1 = (v_stack_m8B8) >> (12);
    v_stack_m4C8 = Arg1;
    goto loc_009F8E46;
loc_009F8E3E:
    v_stack_m4C8 = 0;
loc_009F8E46:
    if (((v_stack_m918) & (512)) == 0) goto loc_009F8E72;
    if (v_stack_m8B0 < ((uint32_t)(0x1000ULL))) goto loc_009F8BC1;
    Arg1 = (v_stack_m8B0) >> (12);
    v_stack_m4C0 = Arg1;
    goto loc_009F8E7A;
loc_009F8E72:
    v_stack_m4C0 = 0;
loc_009F8E7A:
    if (((v_stack_m918) & (0x200000ULL)) == 0) goto loc_009F8EA6;
    if (v_stack_m898 < ((uint32_t)(0x1000ULL))) goto loc_009F8BC1;
    Arg1 = (v_stack_m898) >> (12);
    v_stack_m4B8 = Arg1;
    goto loc_009F8EAE;
loc_009F8EA6:
    v_stack_m4B8 = 0;
loc_009F8EAE:
    v_stack_m670 = 0x200001ULL;
    Arg2 = 0;
    result = memset(v_stack_m668, Arg2, 256, v_stack_mC50);
    v_stack_mC38 = (uint32_t)((uint32_t)(v_stack_m678));
    if ((((uint8_t)((uint32_t)(v_stack_m678))) & (16)) == 0) goto loc_009F9026;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mC58 + 0x610)))) & (2)) != 0) goto loc_009F905D;
    if (v_stack_m8F8 == 0) goto loc_009F905D;
    if ((*(uint64_t *)(v_stack_mC58 + 0x210)) != 0) goto loc_009F8F8E;
    result = ExAllocatePool2(256, 40, (uint32_t)(0x614A7350ULL), v_stack_mC50);
    v_stack_mC48 = result;
    if (result != 0) goto loc_009F8F3A;
loc_009F8F30:
    goto loc_009FAFE1;
loc_009F8F3A:
    Arg3 = 0;
    result = PsChargeSharedPoolQuota(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3 + 40, Arg3, v_stack_mC50);
    v_stack_mC08 = result;
    if (result != 0) goto loc_009F8F7A;
loc_009F8F66:
    result = ExFreePoolWithTag((uint32_t)(0xC000009AULL), (uint32_t)(0x614A7350ULL), Arg3, v_stack_mC50);
    goto loc_009F8BC6;
loc_009F8F7A:
    v_stack_mC38 = (uint32_t)((uint32_t)(v_stack_m678));
loc_009F8F8E:
    result = SeCaptureSubjectContextEx(v_stack_mC10, *(uint64_t *)(v_stack_mC10 + 0xB8), v_stack_mBB8, v_stack_mC50);
    v_stack_mBD8 = v_stack_mBB8;
    if (v_stack_mC50 == 0) goto loc_009F901B;
    v_stack_m9B8 = (uint32_t)(32 - 31);
    v_stack_m9B4 = (uint32_t)(32 - 31);
    v_stack_m9B0 = *(uint64_t *)(v_rip + 0x5E0AA8);
    v_stack_m9A8 = 0;
    result = SePrivilegeCheck(v_stack_m9B8, v_stack_mBB8, (uint8_t)(32 - 31), v_stack_mC50);
    Arg1 = (uint32_t)(((uint8_t)(result)) & ((uint32_t)(32 - 31)));
    result = (uint32_t)(((uint32_t)(v_stack_mBC0)) & (0xFFFFFFFEULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    v_stack_mBC0 = (uint32_t)(Arg1);
    goto loc_009F9023;
loc_009F901B:
loc_009F9023:
    local_rbx = (uint8_t)((local_rbx) | (2));
loc_009F9026:
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, (uint8_t)(32 - 31), (uint8_t)(32 - 31), v_stack_mC50);
    if ((((uint8_t)((uint32_t)(v_stack_mC38))) & (4)) != 0) goto loc_009F906F;
    if ((((uint8_t)((uint32_t)(v_stack_mC38))) & (64)) == 0) goto loc_009F9067;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mC58 + 0x100))) & (4));
    Arg2 = (uint32_t)(((uint32_t)(v_stack_mC38)) | ((uint32_t)(result)));
    v_stack_m690 = *(uint64_t *)(v_stack_mC58 + 0xE8);
    goto loc_009F906F;
loc_009F905D:
    goto loc_009FAFE1;
loc_009F9067:
    v_stack_m690 = 0;
loc_009F906F:
    Arg2 = (uint32_t)((Arg2) & (0xFFFFFFBFULL));
    v_stack_m678 = Arg2;
    if (((2) & ((uint8_t)(local_rbx))) == 0) goto loc_009F91F0;
    if (((2) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mC58 + 0x610))))) == 0) goto loc_009F909F;
loc_009F9091:
    v_stack_mC40 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_009F949F;
loc_009F909F:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mC58 + 0x100)))) & (16)) == 0) goto loc_009F90C8;
    result = KeFirstGroupAffinityEx(v_stack_mB60, v_stack_mC58 + 264, (uint8_t)(32 - 31), v_stack_mC50);
    goto loc_009F90DE;
loc_009F90C8:
    result = KeQueryPrimaryGroupThread(*(uint64_t *)(gs_base + (0 + 0x188)), v_stack_mC58 + 264, (uint8_t)(32 - 31), v_stack_mC50);
    v_stack_mB58 = (uint16_t)(result);
loc_009F90DE:
    result = (v_stack_m8F8) & (*(uint64_t *)(v_rip - 0x9F90E8 + (uint16_t)(result) * 8 + 0xFC7128));
    if (v_stack_m8F8 == result) goto loc_009F9116;
    v_stack_mC40 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_009F949F;
loc_009F9116:
    result = KeAddGroupAffinityEx(v_stack_m670, v_stack_mB58, v_stack_m8F8, v_stack_mC50);
    v_stack_mC70 = (uint32_t)(32 - 31);
    v_stack_mC78 = v_stack_mBC0;
    Arg3 = 0;
    Arg2 = 0;
    result = PspEnumJobsAndProcessesInJobHierarchy(v_stack_mC58, Arg2, Arg3, v_rip - 2571492);
    v_stack_mC40 = (uint32_t)(result);
    if (sign_flag) goto loc_009F949F;
    if (*(uint64_t *)(v_stack_mC58 + 0x210) != 0) goto loc_009F919A;
    *(uint64_t *)(v_stack_mC58 + 0x210) = v_stack_mC48;
    *(uint64_t *)(v_stack_mC58 + 0x218) = v_stack_mC08;
    v_stack_mC48 = 0;
    v_stack_mBD8 = 0;
    goto loc_009F91C2;
loc_009F919A:
    v_stack_mB30 = v_xmm0;
    v_stack_mB20 = v_xmm1;
    v_stack_mBD8 = v_stack_mB30;
loc_009F91C2:
    *(uint64_t *)(*(uint64_t *)(v_stack_mC58 + 0x210)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(v_stack_mC58 + 0x210) + 0x10) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(v_stack_mC58 + 0x210) + 0x20) = v_xmm0;
    goto loc_009F9205;
loc_009F91F0:
    if (condition_is_above_or_equal) goto loc_009F9205;
    if ((((uint8_t)(v_stack_mC58)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mC58 + 0x610))))) == 0) goto loc_009F9091;
loc_009F9205:
    if ((((uint8_t)(32 - 31)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mC58 + 0x100))))) == 0) goto loc_009F9241;
    if (((v_stack_m678) & ((uint8_t)(32 - 31))) != 0) goto loc_009F9241;
    result = *(uint64_t *)(v_rip + 0x5CDE89);
    if ((((uint8_t)(32 - 31)) & ((uint8_t)(*(uint64_t *)(v_rip + 0x5CDE89)))) != 0) {
        Arg1 = v_rip + 6086269;
        result = ExfAcquireReleasePushLockExclusive(Arg1, Arg2, Arg3, v_rip - 2571492);
    }
loc_009F9241:
    v_stack_mB98 = v_stack_mC58;
    v_stack_mC18 = v_stack_mC58 + 256;
    v_stack_mB8C = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mC58 + 0x100)));
    *(uint64_t *)(v_stack_mC58 + 0xF0) = v_stack_m688;
    *(uint64_t *)(v_stack_mC58 + 0xF8) = v_stack_m680;
    *(uint32_t *)(v_stack_mC58 + 0x104) = (uint32_t)((uint32_t)(v_stack_m674));
    if (((2) & ((uint8_t)(local_rbx))) == 0) goto loc_009F9301;
loc_009F92A9:
    *(uint64_t *)(v_stack_mC58 + 0x108) = v_xmm0;
    *(uint64_t *)(v_stack_mC58 + 0x108 + 0x10) = v_xmm1;
    *(uint64_t *)(v_stack_mC58 + 0x108 + 0x20) = v_xmm0;
    *(uint64_t *)(v_stack_mC58 + 0x108 + 0x30) = v_xmm1;
    *(uint64_t *)(v_stack_mC58 + 0x108 + 0x40) = v_xmm0;
    *(uint64_t *)(v_stack_mC58 + 0x108 + 0x50) = v_xmm1;
    *(uint64_t *)(v_stack_mC58 + 0x108 + 0x60) = v_xmm0;
    Arg1 = (v_stack_mC58 + 264) + (2 + 126);
    *(uint64_t *)(Arg1 - 0x10) = v_xmm1;
    Arg2 = (v_stack_m670) + (2 + 126);
    result = (2) - (1);
    if (condition_is_not_equal) goto loc_009F92A9;
    *(uint64_t *)(Arg1) = *(uint64_t *)(arg2);
loc_009F9301:
    *(uint8_t *)(v_stack_mC58 + 0x44D) = (uint8_t)(v_stack_m32B);
    *(uint32_t *)(v_stack_mC58 + 0x244) = (uint32_t)((uint32_t)(v_stack_m534));
    *(uint64_t *)(v_stack_mC58 + 0xE0) = v_stack_m698;
    v_stack_mC38 = v_stack_mC58 + 232;
    *(uint64_t *)(v_stack_mC58 + 0xE8) = v_stack_m690;
    if (((uint32_t)((uint32_t)(v_stack_mC48))) != 9) goto loc_009F93E3;
    Arg3 = 0;
    Arg2 = 0;
    result = PspLockJobMemoryLimitsExclusive(v_stack_mC58, Arg2, Arg3, v_rip - 2571492);
    result = (uint32_t)(~((uint32_t)(v_stack_mC20)));
    result = (uint32_t)((result) & (*(uint32_t *)(v_stack_mC18)));
    result = (uint32_t)((result) | (v_stack_m678));
    *(uint32_t *)(v_stack_mC18) = (uint32_t)(result);
    *(uint64_t *)(v_stack_mC58 + 0x2B0) = v_stack_m4C8;
    *(uint64_t *)(v_stack_mC58 + 0x2B8) = v_stack_m4C0;
    *(uint64_t *)(v_stack_mC58 + 0x2C0) = v_stack_m4B8;
    local_rdi = (uint8_t)((local_rdi) & (6));
    result = v_stack_m4B8;
    if (((uint8_t)(local_rdi)) == 2) {
        Arg1 = v_stack_mC58 + 1264;
        result = ExfTryToWakePushLock(Arg1, Arg2, Arg3, v_rip - 2571492);
    }
    result = KeAbPostRelease(v_stack_mC58 + 1264, Arg2, Arg3, v_rip - 2571492);
    goto loc_009F93F4;
loc_009F93E3:
    result = (uint32_t)(~((uint32_t)(v_stack_mC20)));
    result = (uint32_t)((result) & (*(uint32_t *)(v_stack_mC18)));
    result = (uint32_t)((result) | (v_stack_m678));
    *(uint32_t *)(v_stack_mC18) = (uint32_t)(result);
loc_009F93F4:
    result = (uint32_t)(((uint32_t)(v_stack_mB8C)) | (*(uint32_t *)(v_stack_mC18)));
    result = (uint32_t)(~(result));
    v_stack_mB90 = (uint32_t)(result);
    if (((v_stack_m918) & (4)) != 0) {
        v_stack_mC70 = (uint32_t)(32 - 31);
        v_stack_mC78 = v_stack_mC38;
        Arg4 = v_rip - 2571041;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_stack_mC58;
        result = PspEnumJobsAndProcessesInJobHierarchy(Arg1, Arg2, Arg3, Arg4);
        *(uint64_t *)(v_stack_mC58 + 0xB8) = 0;
        *(uint64_t *)(v_stack_mC58 + 0xC0) = 0;
        Arg1 = v_stack_mC58;
        result = KeResetEvent(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsi = (uint32_t)(v_stack_mC40);
    local_r14 = v_stack_mC58;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mC58 + 0x100)))) & (6)) != 0) {
        local_r14 = v_stack_mC58;
        local_rsi = v_stack_mC40;
    }
    if (((v_stack_mB90) & ((uint8_t)(32 - 31))) == 0) {
        local_rbx = (uint8_t)((local_rbx) | ((uint8_t)(32 - 31)));
    }
    v_stack_mC70 = 5;
    v_stack_mC78 = v_stack_mB98;
    result = PspEnumJobsAndProcessesInJobHierarchy(local_r14, v_rip - 1551831, v_rip + 552512, v_rip + 384407);
loc_009F949F:
    if ((((uint8_t)(32 - 31)) & ((uint8_t)(local_rbx))) == 0) goto loc_009F9528;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 6085628, Arg2, Arg3, v_rip + 384407);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 6085601;
        Arg2 = result;
        Arg1 = v_rip + 6085591;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, v_rip + 384407);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(32 - 31);
    }
loc_009F9503:
    if ((*(uint64_t *)(v_stack_mC58 + 0x28)) == (v_stack_mC58 + 40)) goto loc_009F9524;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x28) - 0x358 + 0x1F0));
    if ((((uint8_t)(32 - 31)) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x28) - 0x358 + 0x1F0))))) == 0) {
        result = PspAddProcessToWorkingSetChangeList(*(uint64_t *)(v_stack_mC58 + 0x28) - 856, Arg2, Arg3, v_rip + 384407);
    }
    goto loc_009F9503;
loc_009F9524:
loc_009F9528:
    result = ExReleaseResourceLite(v_stack_mC58 + 56, Arg2, Arg3, v_rip + 384407);
    if ((((uint8_t)(32 - 31)) & ((uint8_t)(local_rbx))) != 0) {
        Arg1 = v_stack_mC58;
        result = PspApplyWorkingSetLimits(Arg1, Arg2, Arg3, v_rip + 384407);
    }
    result = v_stack_mBD8;
    if (v_stack_mBD8 != 0) {
        Arg1 = v_stack_mBD8;
        result = SeReleaseSubjectContext(Arg1, Arg2, Arg3, v_rip + 384407);
    }
    if (v_stack_mC48 == 0) goto loc_009FAFE1;
    result = ExFreePoolWithTag(v_stack_mC48, (uint32_t)(0x614A7350ULL), Arg3, v_rip + 384407);
    goto loc_009F9A39;
loc_009F9592:
    v_stack_mC18 = 0;
    Arg3 = 16;
    if (((uint32_t)(v_stack_mC08)) != 14) { Arg3 = (uint32_t)(v_stack_mC58); }
    v_stack_mBD8 = (uint32_t)(Arg3);
    Arg2 = 0;
    if (0 == 0) goto loc_009F95D6;
    goto loc_009FAFE1;
loc_009F95D6:
    Arg2 = 0;
    v_stack_mBC8 = 1;
    v_stack_m888 = 0x200001ULL;
    Arg2 = 0;
    result = memset(v_stack_m880, Arg2, 256, v_rip + 384407);
    result = KeQueryActiveGroupCount(v_stack_m880, Arg2, 256, v_rip + 384407);
    Arg1 = (uint16_t)(((uint16_t)(result)) - (1));
    v_stack_mBFE = (uint16_t)(Arg1);
loc_009F9627:
    if (1 == 0) goto loc_009F9710;
    if (((uint32_t)((uint32_t)(v_stack_mC48))) != 14) goto loc_009F965E;
    v_stack_mB60 = v_xmm0;
    v_stack_mC2C = (uint16_t)(result);
    v_stack_mB88 = v_xmm0;
    goto loc_009F968D;
loc_009F965E:
    v_stack_mC2C = (uint16_t)(*(uint16_t *)((uint32_t)((uint32_t)(v_stack_mC08))));
    if (((uint16_t)(*(uint16_t *)((uint32_t)((uint32_t)(v_stack_mC08))))) > ((uint16_t)(Arg1))) goto loc_009F9707;
    v_stack_mB88 = *(uint64_t *)(v_rip - 0x9F9678 + *(uint16_t *)((uint32_t)((uint32_t)(v_stack_mC08))) * 8 + 0xFC7128);
loc_009F968D:
    if (((uint16_t)(v_stack_mC2C)) > ((uint16_t)(Arg1))) goto loc_009F9707;
    if ((*(uint64_t *)(local_rsp + (uint16_t)(v_stack_mC2C) * 8 + 0x418)) != 0) goto loc_009F9707;
    result = (*(uint64_t *)(v_rip - 0x9F9678 + (uint16_t)(v_stack_mC2C) * 8 + 0xFC7128)) & (v_stack_mB88);
    if (v_stack_mB88 != result) goto loc_009F9707;
    result = KeAddGroupAffinityEx(v_stack_m888, v_stack_mC2C, v_stack_mB88, v_rip + 384407);
    local_r14 = (uint32_t)(((uint32_t)(v_stack_mBC8)) - 1);
    v_stack_mBC8 = (uint32_t)(local_r14);
    local_r13 = (v_stack_mBD0) + ((uint32_t)(v_stack_mBD8));
    v_stack_mBD0 = local_r13;
    goto loc_009F9627;
loc_009F9707:
    v_stack_mC40 = (uint32_t)((uint32_t)(0xC000000DULL));
loc_009F9710:
    goto loc_009F9743;
loc_009F9743:
    if (sign_flag) goto loc_009FAFE1;
    if ((*(uint64_t *)(v_stack_mC58 + 0x210)) != 0) goto loc_009F97B0;
    result = ExAllocatePool2(256, 40, (uint32_t)(0x614A7350ULL), v_rip + 384407);
    if (result == 0) goto loc_009F8F30;
    Arg3 = 0;
    result = PsChargeSharedPoolQuota(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), Arg3 + 40, Arg3, v_rip + 384407);
    v_stack_mC18 = result;
    if (result != 0) goto loc_009F97AB;
    goto loc_009F8F66;
loc_009F97AB:
loc_009F97B0:
    result = SeCaptureSubjectContextEx(v_stack_mC10, *(uint64_t *)(v_stack_mC10 + 0xB8), v_stack_mBB8, v_rip + 384407);
    v_stack_mC08 = v_stack_mBB8;
    if (v_stack_mC50 == 0) goto loc_009F983D;
    v_stack_m9B8 = 1;
    v_stack_m9B4 = 1;
    v_stack_m9B0 = *(uint64_t *)(v_rip + 0x5E0286);
    v_stack_m9A8 = 0;
    result = SePrivilegeCheck(v_stack_m9B8, v_stack_mBB8, 1, v_rip + 384407);
    Arg1 = (uint32_t)(((uint8_t)(result)) & (1));
    result = (uint32_t)(((uint32_t)(v_stack_mBC0)) & (0xFFFFFFFEULL));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(result)));
    v_stack_mBC0 = (uint32_t)(Arg1);
    goto loc_009F9845;
loc_009F983D:
loc_009F9845:
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, 1, 1, v_rip + 384407);
    v_stack_mC70 = 1;
    v_stack_mC78 = v_stack_mBC0;
    Arg3 = 0;
    Arg2 = 0;
    result = PspEnumJobsAndProcessesInJobHierarchy(v_stack_mC58, Arg2, Arg3, v_rip - 2573322);
    v_stack_mC40 = (uint32_t)(result);
    if (sign_flag) goto loc_009F99FD;
    if (*(uint64_t *)(v_stack_mC58 + 0x210) != 0) goto loc_009F98B4;
    *(uint64_t *)(v_stack_mC58 + 0x210) = result;
    *(uint64_t *)(v_stack_mC58 + 0x218) = v_stack_mC18;
    v_stack_mC08 = 0;
    goto loc_009F98DC;
loc_009F98B4:
    v_stack_mB30 = v_xmm0;
    v_stack_mB20 = v_xmm1;
    v_stack_mC08 = v_stack_mB30;
loc_009F98DC:
    *(uint64_t *)(*(uint64_t *)(v_stack_mC58 + 0x210)) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(v_stack_mC58 + 0x210) + 0x10) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(v_stack_mC58 + 0x210) + 0x20) = v_xmm0;
    v_stack_mB98 = v_stack_mC58;
    v_stack_mB8C = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mC58 + 0x100)));
    v_stack_mB90 = (uint32_t)((uint32_t)(0xFFFFFFEFULL));
loc_009F9945:
    *(uint64_t *)(v_stack_mC58 + 0x108) = v_xmm0;
    *(uint64_t *)(v_stack_mC58 + 0x108 + 0x10) = v_xmm1;
    *(uint64_t *)(v_stack_mC58 + 0x108 + 0x20) = v_xmm0;
    *(uint64_t *)(v_stack_mC58 + 0x108 + 0x30) = v_xmm1;
    *(uint64_t *)(v_stack_mC58 + 0x108 + 0x40) = v_xmm0;
    *(uint64_t *)(v_stack_mC58 + 0x108 + 0x50) = v_xmm1;
    *(uint64_t *)(v_stack_mC58 + 0x108 + 0x60) = v_xmm0;
    Arg2 = (v_stack_mC58 + 264) + (128);
    *(uint64_t *)(arg2 - 0x10) = v_xmm1;
    result = (v_stack_m888) + (128);
    Arg3 = (2) - (1);
    if (condition_is_not_equal) goto loc_009F9945;
    *(uint64_t *)(arg2) = *(uint64_t *)(result);
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mC48))))) != 14) goto loc_009F99B6;
    result = KeIsEmptyAffinityEx(v_stack_mC58 + 264, Arg2, Arg3, 128);
    if ((uint32_t)(result) == 0) goto loc_009F99B6;
    goto loc_009F99C6;
loc_009F99B6:
loc_009F99C6:
    v_stack_mC70 = 5;
    v_stack_mC78 = v_stack_mB98;
    Arg3 = 0;
    result = PspEnumJobsAndProcessesInJobHierarchy(v_stack_mC58, v_rip - 1553196, Arg3, v_rip + 383038);
loc_009F99FD:
    result = ExReleaseResourceLite(v_stack_mC58 + 56, v_rip - 1553196, Arg3, v_rip + 383038);
    result = v_stack_mC08;
    if (v_stack_mC08 != 0) {
        Arg1 = v_stack_mC08;
        result = SeReleaseSubjectContext(Arg1, v_rip - 1553196, Arg3, v_rip + 383038);
    }
    if (0 == 0) goto loc_009FAFE1;
    result = ExFreePoolWithTag(0, (uint32_t)(0x614A7350ULL), Arg3, v_rip + 383038);
loc_009F9A39:
    Arg3 = 0;
    result = PsReturnSharedPoolQuota(v_stack_mC18, 40, Arg3, v_rip + 383038);
    goto loc_009FAFE1;
loc_009F9A4B:
    Arg1 = (uint32_t)((v_stack_mC18) - (15));
    if (condition_is_equal) goto loc_009F9DB7;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009F9D4C;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(v_stack_mC58)));
    if (condition_is_equal) goto loc_009F9CAF;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_009F9C63;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009F9B8B;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009F9B20;
    if (((uint32_t)(Arg1)) != 1) goto loc_009FAC1E;
    v_stack_mAB8 = *(uint64_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_mC48))));
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, 1, Arg3, v_rip + 383038);
    if ((((uint8_t)(1 + 31)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mC58 + 0x610))))) != 0) goto loc_009F9AC7;
loc_009F9ABD:
    goto loc_009F8A9D;
loc_009F9AC7:
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x4D8) + 0x28));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x4D8) + 0x28)))) & (16)) == 0) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x4D8) + 0x28))) | (16));
        *(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x4D8) + 0x28) = (uint32_t)(result);
        Arg3 = v_stack_mC58;
        Arg2 = v_rip - 4284773;
        Arg1 = *(uint64_t *)(v_stack_mC58 + 0x4D8) + 48;
        result = KeInitializeDpc(Arg1, Arg2, Arg3, v_rip + 383038);
    }
    result = KeSetSchedulingGroupCycleNotification(*(uint64_t *)(v_stack_mC58 + 0x4D8) + 128, *(uint64_t *)(v_stack_mC58 + 0x4D8) + 48, (uint32_t)(0xC000000DULL), v_rip + 383038);
loc_009F9B01:
    goto loc_009F8A9D;
loc_009F9B20:
    if ((*(uint8_t *)((uint32_t)((uint32_t)((uint32_t)(v_stack_mC48))))) == 1) goto loc_009F9B44;
    v_stack_mC40 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_009FAFE1;
loc_009F9B44:
    v_stack_mC70 = 0;
    v_stack_mC78 = 0;
    Arg2 = 0;
    result = PspEnumJobsAndProcessesInJobHierarchy(v_stack_mC58, Arg2, v_rip + 695412, v_rip + 671003);
    goto loc_009FA156;
loc_009F9B8B:
    v_stack_mC3C = (uint8_t)(*(uint8_t *)((uint32_t)(v_stack_mC48)));
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, 1, v_rip + 695412, v_rip + 671003);
    if ((((uint8_t)(1 + 31)) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mC58 + 0x610))))) == 0) goto loc_009F9ABD;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x4D8) + 0x28)))) & (64)) != 0) goto loc_009F9ABD;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x4D8) + 0x28)))) & (33)) != 0) goto loc_009F9C42;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x4D8) + 0x28))))) >> (3));
    Arg1 = (uint32_t)((Arg1) & (1));
    result = ((uint8_t)(v_stack_mC3C) != 0) ? 1 : 0;
    if (((uint32_t)(Arg1)) == ((uint32_t)(result))) goto loc_009F9ABD;
    Arg3 = (uint8_t)(-(v_stack_mC3C));
    result = (uint32_t)((result) & (8));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x4D8) + 0x28))) & (0xFFFFFFF7ULL));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(result)));
    *(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x4D8) + 0x28) = Arg2;
    Arg1 = (*(uint64_t *)(v_stack_mC58 + 0x4D8)) - (-128);
    result = KeSetSchedulingGroupRankBias(Arg1, v_stack_mC3C, Arg3, *(uint64_t *)(v_stack_mC58 + 0x4D8));
    v_stack_mC70 = 1;
    v_stack_mC78 = v_stack_mC3C;
    Arg3 = 0;
    Arg2 = 0;
    result = PspEnumJobsAndProcessesInJobHierarchy(v_stack_mC58, Arg2, Arg3, v_rip - 5578704);
    goto loc_009F9B01;
loc_009F9C42:
    goto loc_009F8A9D;
loc_009F9C63:
    v_stack_mC00 = (uint8_t)(*(uint8_t *)((uint32_t)(v_stack_mC48)));
    result = PspSetBackgroundJobTree(v_stack_mC58, *(uint8_t *)((uint32_t)(v_stack_mC48)), Arg3, v_rip - 5578704);
loc_009F9C7B:
    if (sign_flag) goto loc_009FAFE1;
    goto loc_009FAFE1;
loc_009F9CAF:
    v_stack_m9A0 = v_xmm0;
    if ((uint32_t)((uint32_t)(v_stack_m9A0)) == 0) goto loc_009FA493;
    if ((((uint32_t)((uint32_t)(v_stack_m9A0))) & (0xFFFFFFF0ULL)) != 0) goto loc_009FA493;
    if (((1) & ((uint8_t)((uint32_t)(v_stack_m9A0)))) != 0) goto loc_009F9CEA;
    if ((((uint8_t)((uint32_t)(v_stack_m9A0))) & (8)) != 0) goto loc_009FAD04;
loc_009F9CEA:
    result = PspFreezeJobTree(v_stack_mC58, v_stack_m9A0, Arg3, v_rip - 5578704);
    if (sign_flag) goto loc_009FAFC8;
    *(uint32_t *)((uint32_t)(v_stack_mC48)) = (uint32_t)((uint32_t)(v_stack_m9A0));
    goto loc_009FAFE1;
loc_009F9D4C:
    v_stack_mB3C = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_mC48))));
    if ((((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_mC48))))) & (0xFFFFC001ULL)) != 0) goto loc_009FAD43;
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, 1, Arg3, v_rip - 5578704);
    Arg3 = 0;
    Arg2 = 0;
    result = PspLockJobMemoryLimitsExclusive(v_stack_mC58, Arg2, Arg3, v_rip - 5578704);
    *(uint32_t *)(v_stack_mC58 + 0x450) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_mC48))));
    Arg3 = 0;
    Arg2 = 0;
    result = PspUnlockJobMemoryLimitsExclusive(v_stack_mC58, Arg2, Arg3, v_rip - 5578704);
    goto loc_009FA14D;
loc_009F9DB7:
    result = memcpy(v_stack_mB70, (uint32_t)(v_stack_mC48), 1, v_rip - 5578704);
    if ((((uint32_t)(v_stack_mB70)) & (0xFFFFFFC0ULL)) != 0) goto loc_009FAD04;
    v_stack_mC38 = 0;
    v_stack_mC28 = (uint32_t)((uint32_t)(v_stack_mB6C));
    if (((1) & ((uint8_t)(v_stack_mB70))) == 0) goto loc_009F9E69;
    if ((((uint8_t)(v_stack_mC58)) & ((uint8_t)(v_stack_mB70))) == 0) goto loc_009F9E16;
    if ((((uint8_t)(v_stack_mB70)) & (16)) != 0) goto loc_009FAD04;
loc_009F9E0E:
    if (((uint32_t)((uint32_t)(v_stack_mB6C) - 1)) > 8) goto loc_009FAD04;
    goto loc_009F9E56;
loc_009F9E16:
    if ((((uint8_t)(v_stack_mB70)) & (16)) == 0) goto loc_009F9E48;
    if ((((uint8_t)(v_stack_mB70)) & (4)) != 0) goto loc_009FAD04;
    if (((uint16_t)((uint32_t)(v_stack_mB6C))) < 1) goto loc_009FAD04;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_mB6C)))) >> (16));
    if (((uint16_t)((uint32_t)(v_stack_mB6C))) > ((uint16_t)(result))) goto loc_009FAD04;
    goto loc_009F9E0E;
loc_009F9E48:
    if (((uint32_t)((uint32_t)(v_stack_mB6C) - 1)) > 0x270FULL) goto loc_009FAD04;
loc_009F9E56:
    if (((32) & ((uint8_t)(v_stack_mB70))) == 0) goto loc_009F9E6E;
    v_stack_mC38 = (uint32_t)(32 - 24);
    goto loc_009F9E6E;
loc_009F9E69:
loc_009F9E6E:
    Arg3 = 0;
    result = PspLockJobChain(v_stack_mC58, v_stack_mC10, Arg3, v_rip - 5578704);
    if (((1) & ((uint8_t)(v_stack_mB70))) == 0) goto loc_009F9EC0;
    if (((32) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_mC58 + 0x610))))) != 0) goto loc_009F9ED5;
    result = PspAllocateRateControl(2, v_stack_mC10, Arg3, v_rip - 5578704);
    if (result != 0) goto loc_009F9EB7;
    goto loc_009FA102;
loc_009F9EB7:
    *(uint64_t *)(v_stack_mC58 + 0x4D8) = result;
    goto loc_009F9ED8;
loc_009F9EC0:
    if (((32) & ((uint8_t)(result))) != 0) goto loc_009F9ECF;
    goto loc_009FA102;
loc_009F9ECF:
loc_009F9ED5:
loc_009F9ED8:
    *(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x4D8) + 0x28) = 0;
    *(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x4D8) + 0x2C) = (uint32_t)((uint32_t)(0xC000000DULL));
    if (((1) & ((uint8_t)(v_stack_mB70))) == 0) goto loc_009FA030;
    result = *(uint64_t *)(v_stack_mC58 + 0x4D8);
    if ((((uint8_t)(v_stack_mB70)) & (4)) != 0) {
        result = *(uint64_t *)(v_stack_mC58 + 0x4D8);
        v_stack_mC26 = (uint16_t)((uint32_t)(0xC000000DULL));
    }
    if (((2) & ((uint8_t)(v_stack_mB70))) == 0) goto loc_009F9F28;
    result = (uint32_t)(((uint32_t)(v_stack_mC38)) & (0xFFFFFFFEULL));
    v_stack_mC24 = (uint32_t)(result);
    goto loc_009F9F42;
loc_009F9F28:
    result = (uint32_t)(((uint32_t)(v_stack_mC38)) | (1));
    v_stack_mC24 = (uint32_t)(result);
    if ((((uint8_t)(v_stack_mB70)) & (20)) == 0) {
        result = 0x2710ULL;
        v_stack_mC26 = (uint16_t)(result);
    }
    if ((((uint8_t)(v_stack_mB70)) & (8)) != 0) {
        result = *(uint64_t *)(v_stack_mC58 + 0x4D8);
    }
    if ((((uint8_t)(v_stack_mB70)) & (16)) != 0) {
        result = *(uint64_t *)(v_stack_mC58 + 0x4D8);
    }
    if (((32) & ((uint8_t)(v_stack_mB70))) != 0) {
        result = *(uint64_t *)(v_stack_mC58 + 0x4D8);
        Arg3 = 128;
    }
    if ((*(uint64_t *)(v_stack_mC58 + 0x4D8)) != 0) goto loc_009F9FDE;
    *(uint64_t *)(*(uint64_t *)(v_stack_mC58 + 0x4D8) + 0x80) = v_stack_mC28;
    result = PspAddSchedulingGroupToJobChain(*(uint64_t *)(v_stack_mC58 + 0x518), v_stack_mC58, Arg3, v_rip - 5578704);
    v_stack_mC40 = (uint32_t)(result);
    if (sign_flag) goto loc_009F9FBA;
    goto loc_009FA009;
loc_009F9FBA:
    if (*(uint64_t *)(v_stack_mC58 + 0x4D8) == 0) goto loc_009FA102;
    result = PspFreeRateControl(*(uint64_t *)(v_stack_mC58 + 0x4D8), 2, Arg3, v_rip - 5578704);
    *(uint64_t *)(v_stack_mC58 + 0x4D8) = 0;
    goto loc_009FA102;
loc_009F9FDE:
    v_stack_mBE8 = 2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0x28)))) & (4)) == 0) goto loc_009FA004;
    result = KeSetSchedulingGroupWeights(1, v_stack_mBE8, v_stack_mC28, v_rip - 5578704);
    goto loc_009FA009;
loc_009FA004:
    result = KeSetSchedulingGroupCpuRates(1, v_stack_mBE8, v_stack_mC28, v_rip - 5578704);
loc_009FA009:
    v_stack_mB80 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x4D8) + 0x28)));
    v_stack_mB7C = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x4D8) + 0x2C)));
    goto loc_009FA0D0;
loc_009FA030:
    result = (uint32_t)(((uint32_t)(v_stack_mC38)) | (3));
    v_stack_mC24 = (uint32_t)(result);
    v_stack_mC28 = 0x27102710ULL;
    *(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x4D8) + 0x2C) = (uint32_t)((uint32_t)(v_stack_mC28));
    Arg1 = (*(uint64_t *)(v_stack_mC58 + 0x4D8)) - (-128);
    v_stack_mBE8 = Arg1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1 + 0x4))) >> (2));
    result = (uint8_t)((result) & (1));
    v_stack_mC3B = (uint8_t)(result);
    result = KeQuerySchedulingGroupReadyTime(Arg1, v_stack_mBE8, v_stack_mC28, v_rip - 5578704);
    result = KeSetSchedulingGroupCpuRates(Arg1, v_stack_mBE8, v_stack_mC28, v_rip - 5578704);
    v_stack_mB7C = (uint32_t)((uint32_t)(v_stack_mC28));
    if (v_stack_mC3B != 0) {
        v_stack_mC3B = 0;
        v_stack_mC70 = 1;
        result = v_stack_mC3B;
        v_stack_mC78 = result;
        Arg4 = v_rip - 5579875;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_stack_mC58;
        result = PspEnumJobsAndProcessesInJobHierarchy(Arg1, Arg2, Arg3, Arg4);
    }
    if (((*(uint32_t *)(v_rip + 0x5CCA23)) & (0x80000ULL)) != 0) {
        v_stack_mC70 = 0x725ULL;
        v_stack_mC78 = 0;
        Arg4 = 0;
        Arg3 = v_stack_mB80;
        Arg2 = Arg4 + 15;
        Arg1 = v_stack_mC58;
        result = EtwTraceJobSetQuery(Arg1, Arg2, Arg3, Arg4);
    }
    result = PspUnlockJobChain(v_stack_mC58, v_stack_mC10, Arg3, Arg4);
    goto loc_009FAFC8;
loc_009FA12E:
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, 1, Arg3, Arg4);
    result = KeResetEvent(v_stack_mC58, 1, Arg3, Arg4);
loc_009FA14D:
    result = ExReleaseResourceLite(v_stack_mC58 + 56, 1, Arg3, Arg4);
loc_009FA156:
    goto loc_009FAFC8;
loc_009FA15E:
    if (((uint32_t)(v_stack_mC58 + 56)) == 42) goto loc_009FAA82;
    if (((uint32_t)(v_stack_mC58 + 56)) > 42) goto loc_009FABE7;
    Arg1 = (uint32_t)((v_stack_mC58 + 56) - (27));
    if (condition_is_equal) goto loc_009FAA4D;
    Arg1 = (uint32_t)((Arg1) - (4));
    if (condition_is_equal) goto loc_009FA889;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009FA871;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009F880A;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(v_stack_mC58)));
    if (condition_is_equal) goto loc_009FA348;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(v_stack_mC58)));
    if (condition_is_equal) goto loc_009FA2C4;
    Arg1 = (uint32_t)((Arg1) - (3));
    if (condition_is_equal) goto loc_009FA245;
    if (((uint32_t)(Arg1)) != 1) goto loc_009FAC1E;
    v_stack_mB40 = (uint32_t)((uint32_t)(*(uint32_t *)(2)));
    result = PspJobIsAppSilo(v_stack_mC58, 1, (uint32_t)(*(uint32_t *)(2)), Arg4);
    if ((uint8_t)(result) == 0) goto loc_009FA30F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(2)))) != 2) goto loc_009FA30F;
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, (uint8_t)((uint32_t)(*(uint32_t *)(2)) - 1), (uint32_t)(*(uint32_t *)(2)), Arg4);
    if ((*(uint32_t *)(v_stack_mC58 + 0x5B0)) == 0) goto loc_009FA203;
    goto loc_009FA226;
loc_009FA203:
    if ((*(uint32_t *)(v_stack_mC58 + 0x5B0)) >= 0) goto loc_009FA21B;
    goto loc_009FA226;
loc_009FA21B:
    result = PspHardDereferenceSiloWorker(v_stack_mC58, (uint8_t)((uint32_t)(*(uint32_t *)(2)) - 1), (uint32_t)(*(uint32_t *)(2)), Arg4);
loc_009FA226:
    goto loc_009F8AA1;
loc_009FA245:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x5DF826), (uint8_t)(v_stack_mC50), (uint32_t)(*(uint32_t *)(2)), Arg4);
    if ((uint8_t)(result) == 0) goto loc_009FA2DD;
    if (((*(uint32_t *)(v_stack_mC58 + 0x610)) & (0x40000000ULL)) == 0) goto loc_009FA2F4;
    result = PspSetJobSiloThreadImpersonationPolicy(v_stack_mC58, 4, (uint32_t)(*(uint32_t *)(2)), Arg4);
    if ((uint8_t)(result) == 0) goto loc_009FA30F;
    v_stack_mAB0 = *(uint64_t *)(2);
    v_stack_mB44 = (uint32_t)((uint32_t)(*(uint32_t *)(2 + 0x8)));
    result = PspConvertSiloToServerSilo(v_stack_mC58, (uint8_t)(v_stack_mC50), *(uint64_t *)(2), (uint32_t)(*(uint32_t *)(2 + 0x8)));
    goto loc_009FAFC0;
loc_009FA2C4:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x5DF7A9), v_stack_mC50, *(uint64_t *)(2), (uint32_t)(*(uint32_t *)(2 + 0x8)));
    if ((uint8_t)(result) != 0) goto loc_009FA2E7;
loc_009FA2DD:
    goto loc_009FAFC2;
loc_009FA2E7:
    if (((*(uint32_t *)(v_stack_mC58 + 0x610)) & (0x40000000ULL)) != 0) goto loc_009FA2FE;
loc_009FA2F4:
    goto loc_009FAFC2;
loc_009FA2FE:
    result = PspSetJobSiloThreadImpersonationPolicy(v_stack_mC58, 4, *(uint64_t *)(2), (uint32_t)(*(uint32_t *)(2 + 0x8)));
    if ((uint8_t)(result) != 0) goto loc_009FA319;
loc_009FA30F:
    goto loc_009FAFC2;
loc_009FA319:
    v_stack_mB48 = (uint32_t)((uint32_t)(*(uint32_t *)(2)));
    result = ObCreateSiloRootDirectory(v_stack_mC58, (uint32_t)(*(uint32_t *)(2)), *(uint64_t *)(2), (uint32_t)(*(uint32_t *)(2 + 0x8)));
    goto loc_009FAFC0;
loc_009FA348:
    result = PspCreateSilo(v_stack_mC58, (uint32_t)(*(uint32_t *)(2)), *(uint64_t *)(2), (uint32_t)(*(uint32_t *)(2 + 0x8)));
    goto loc_009FAFC0;
loc_009FA35A:
    result = memcpy(v_stack_m990, (uint32_t)(*(uint32_t *)(2)), *(uint64_t *)(2), (uint32_t)(*(uint32_t *)(2 + 0x8)));
    v_stack_m9E0 = (uint32_t)(v_stack_m960);
    v_stack_mA08 = v_stack_m990;
    v_stack_mA00 = v_stack_m988;
    v_stack_m9F8 = v_stack_m980;
    v_stack_m9D8 = v_stack_m978;
    v_stack_m9F0 = v_stack_m970;
    v_stack_m9E8 = (uint32_t)((uint32_t)(v_stack_m968));
    v_stack_m9E4 = (uint32_t)((uint32_t)(v_stack_m964));
    v_stack_mC20 = (uint32_t)((uint32_t)(0x278204ULL));
    goto loc_009FA47B;
loc_009FA3F1:
    result = memcpy(v_stack_m958, v_stack_m970, v_stack_m960, v_stack_m980);
    v_stack_m9E0 = (uint32_t)((uint32_t)(v_stack_m930));
    v_stack_mA08 = v_stack_m958;
    v_stack_mA00 = v_stack_m950;
    v_stack_m9F8 = v_stack_m948;
    v_stack_m9F0 = v_stack_m940;
    v_stack_m9E8 = (uint32_t)((uint32_t)(v_stack_m938));
    v_stack_m9E4 = (uint32_t)((uint32_t)(v_stack_m934));
    v_stack_mC20 = (uint32_t)((uint32_t)(0x70204ULL));
loc_009FA473:
loc_009FA47B:
    result = (uint32_t)(~((uint32_t)(0x70204ULL)));
    if ((((uint32_t)((uint32_t)(v_stack_m930))) & ((uint32_t)(result))) != 0) goto loc_009FA493;
    if (condition_is_above_or_equal) goto loc_009FA49D;
    if (v_stack_m9D8 >= ((uint32_t)(0x1000ULL))) goto loc_009FA4A8;
loc_009FA493:
    goto loc_009F8B05;
loc_009FA49D:
    v_stack_m9D8 = 0;
loc_009FA4A8:
    if (v_stack_m9D8 >= ((uint32_t)(0x1000ULL))) goto loc_009FA4BB;
    if (v_stack_m940 < ((uint32_t)(0x1000ULL))) goto loc_009FA493;
    if (v_stack_m940 >= 0) goto loc_009FA4C3;
    goto loc_009FA493;
loc_009FA4BB:
    v_stack_m9F0 = 0;
loc_009FA4C3:
    if ((((uint8_t)((uint32_t)(v_stack_m930))) & (4)) == 0) goto loc_009FA4D0;
    if (v_stack_m948 != 0) goto loc_009FA4D8;
    goto loc_009FA493;
loc_009FA4D0:
    v_stack_m9F8 = 0;
loc_009FA4D8:
    if (condition_is_above_or_equal) goto loc_009FA4E6;
    if (v_stack_m958 != 0) goto loc_009FA4EE;
    goto loc_009FA493;
loc_009FA4E6:
    v_stack_mA08 = 0;
loc_009FA4EE:
    if (condition_is_above_or_equal) goto loc_009FA4FC;
    if (v_stack_m950 != 0) goto loc_009FA504;
    goto loc_009FA493;
loc_009FA4FC:
    v_stack_mA00 = 0;
loc_009FA504:
loc_009FA50D:
    if (0 >= 3) goto loc_009FA57A;
    result = PspNotificationLimitRateControlToleranceField(v_stack_mA08, 0, (uint32_t)(v_stack_m930), v_stack_m948);
    result = PspNotificationLimitRateControlToleranceIntervalField(v_stack_mA08, 0, (uint32_t)(v_stack_m930), result);
    result = PspRateControlLimitFlag(0, 0, (uint32_t)(v_stack_m930), result);
    if ((((uint32_t)((uint32_t)(v_stack_m930))) & ((uint32_t)(result))) == 0) goto loc_009FA567;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result))) == 0) goto loc_009FAD04;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result)))) > 3) goto loc_009FAD04;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result))) == 0) goto loc_009FAD04;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result)))) <= 3) goto loc_009FA575;
    goto loc_009FAD04;
loc_009FA567:
    *(uint32_t *)(result) = 0;
    *(uint32_t *)(result) = 0;
loc_009FA575:
    Arg2 = (uint32_t)((0) + (1));
    goto loc_009FA50D;
loc_009FA57A:
    v_stack_mB78 = v_stack_mC58 + 1216;
    if ((*(uint64_t *)(v_stack_mC58 + 0x4C0)) != 0) goto loc_009FA605;
    result = ExAllocatePool2(136 + 120, 136, (uint32_t)(0x624A7350ULL), result);
    if (result != 0) goto loc_009FA5BA;
    goto loc_009FAFC8;
loc_009FA5BA:
    Arg3 = 0;
    result = PsChargeSharedPoolQuota(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), (uint32_t)(0xC000009AULL), Arg3, result);
    if (result != 0) goto loc_009FA5F4;
    result = ExFreePoolWithTag(result, (uint32_t)(0x624A7350ULL), Arg3, result);
    goto loc_009FAD09;
loc_009FA5F4:
    Arg2 = 0;
    result = memset(result, Arg2, (uint32_t)(0xC000009AULL), result);
    goto loc_009FA60B;
loc_009FA605:
loc_009FA60B:
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, 1, (uint32_t)(0xC000009AULL), result);
    if ((*(uint64_t *)(v_stack_mB78)) != 0) goto loc_009FA630;
    *(uint64_t *)(v_stack_mB78) = 0;
    *(uint64_t *)(v_stack_mC58 + 0x4C8) = 0;
    goto loc_009FA650;
loc_009FA630:
    result = v_stack_mB78;
    if (0 != 0) {
        Arg2 = 0x624A7350ULL;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)(0xC000009AULL), result);
        Arg3 = 0;
        Arg2 = (uint32_t)(0xC000009AULL);
        Arg1 = 0;
        result = PsReturnSharedPoolQuota(Arg1, Arg2, Arg3, result);
    }
    *(uint64_t *)(*(uint64_t *)(v_stack_mC58 + 0x4C0) + 0x8) = v_stack_mA08;
    *(uint64_t *)(*(uint64_t *)(v_stack_mC58 + 0x4C0) + 0x10) = v_stack_mA00;
    *(uint64_t *)(*(uint64_t *)(v_stack_mC58 + 0x4C0) + 0x18) = v_stack_m9F8;
loc_009FA684:
    if (0 == 0) goto loc_009FA6A1;
    if (0 == 1) goto loc_009FA697;
    goto loc_009FA6A9;
loc_009FA697:
    goto loc_009FA6A9;
loc_009FA6A1:
loc_009FA6A9:
    if (0 == 0) goto loc_009FA6C6;
    if (0 == 1) goto loc_009FA6BC;
    goto loc_009FA6CE;
loc_009FA6BC:
    goto loc_009FA6CE;
loc_009FA6C6:
loc_009FA6CE:
    *(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x4C0) + 0x3C - 0xC) = (uint32_t)((uint32_t)(v_stack_m9CC));
    *(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x4C0) + 0x3C) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m9C8)));
    Arg1 = (uint32_t)((0) + (1));
    Arg3 = (*(uint64_t *)(v_stack_mC58 + 0x4C0) + 60) + (4);
    if (((uint32_t)(Arg1)) < 3) goto loc_009FA684;
    Arg3 = 0;
    Arg2 = 0;
    result = PspLockJobMemoryLimitsExclusive(v_stack_mC58, Arg2, Arg3, (uint32_t)(v_stack_m9CC));
    result = (v_stack_m9D8) >> (12);
    *(uint64_t *)(*(uint64_t *)(v_stack_mC58 + 0x4C0) + 0x20) = result;
    result = (v_stack_m9F0) >> (12);
    *(uint64_t *)(*(uint64_t *)(v_stack_mC58 + 0x4C0) + 0x28) = result;
    *(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x4C0)) = (uint32_t)((uint32_t)(v_stack_m9E0));
    local_rdi = (uint8_t)((32) & (6));
    result = (uint32_t)(v_stack_m9E0);
    if (((uint8_t)(local_rdi)) == 2) {
        Arg1 = v_stack_mC58 + 1264;
        result = ExfTryToWakePushLock(Arg1, Arg2, Arg3, (uint32_t)(v_stack_m9CC));
    }
    result = KeAbPostRelease(v_stack_mC58 + 1264, Arg2, Arg3, (uint32_t)(v_stack_m9CC));
    local_rbx = v_stack_mC58;
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x4C0))) & (0xFFFF7DFFULL)) != 0) {
        local_rbx = v_stack_mC58;
    }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x4C0)))) != 0) goto loc_009FA780;
    if ((*(uint32_t *)(*(uint64_t *)(local_rbx + 0x4C0))) != 0) goto loc_009FA78C;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mC58 + 0x4C0)))) == 0) goto loc_009FA7AE;
loc_009FA780:
    result = *(uint64_t *)(local_rbx + 0x4C0);
    if ((*(uint32_t *)(*(uint64_t *)(local_rbx + 0x4C0))) == 0) {
        v_stack_mC70 = 5;
        v_stack_mC78 = *(uint64_t *)(local_rbx + 0x4C0);
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = v_rip + 667002;
        Arg1 = local_rbx;
        result = PspEnumJobsAndProcessesInJobHierarchy(Arg1, Arg2, Arg3, Arg4);
    }
    if (((*(uint32_t *)(v_rip + 0x5CC343)) & (0x80000ULL)) != 0) {
        v_stack_mC70 = 0x725ULL;
        v_stack_mC78 = 0;
        Arg4 = 0;
        Arg3 = v_stack_mA08;
        Arg2 = (uint32_t)((uint32_t)(v_stack_mC48));
        Arg1 = local_rbx;
        result = EtwTraceJobSetQuery(Arg1, Arg2, Arg3, Arg4);
    }
    result = ExReleaseResourceLite(local_rbx + 56, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = PspLockJobMemoryLimitsShared(local_rbx, Arg2, Arg3, Arg4);
    Arg3 = (*(uint64_t *)(local_rbx + 0x620)) + (*(uint64_t *)(v_stack_mC58 + 0x4B8));
    result = PspGetJobMemoryUsageNotificationViolations(v_stack_mC58, *(uint64_t *)(v_stack_mC58 + 0x4B8), Arg3, (uint32_t)(0x8200ULL));
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = v_stack_mC58 + 1264;
        result = ExfReleasePushLockShared(Arg1, *(uint64_t *)(v_stack_mC58 + 0x4B8), Arg3, (uint32_t)(0x8200ULL));
    }
    result = KeAbPostRelease(v_stack_mC58 + 1264, *(uint64_t *)(v_stack_mC58 + 0x4B8), Arg3, (uint32_t)(0x8200ULL));
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) {
        Arg1 = v_stack_mC58;
        Arg1 = *(uint64_t *)(Arg1 + 0x520);
        result = PspScheduleEnforcementWorker(Arg1, *(uint64_t *)(v_stack_mC58 + 0x4B8), Arg3, (uint32_t)(0x8200ULL));
    }
    goto loc_009F8BC6;
loc_009FA871:
    result = PspSetNetRateControl((uint32_t)(v_stack_mC48), 1, v_stack_mC58, (uint32_t)(0x8200ULL));
    goto loc_009FAFC0;
loc_009FA889:
    v_stack_mBF0 = 0;
    result = memcpy(v_stack_mA98, (uint32_t)(v_stack_mC48), 1, (uint32_t)(0x8200ULL));
    if (v_stack_mA80 == 0) goto loc_009FA9AD;
    if ((uint16_t)(v_stack_mA70) == 0) goto loc_009FA995;
    if (((1) & ((uint8_t)(v_stack_mA80))) != 0) {
        result = ExRaiseDatatypeMisalignment(v_stack_mA70, v_stack_mA80, 1, (uint32_t)(0x8200ULL));
    }
    if ((v_stack_mA80 + v_stack_mA70 * 1) > result) goto loc_009FA8F1;
    local_rbx = 0;
    if ((v_stack_mA80 + v_stack_mA70 * 1) < v_stack_mA80) {
        result = *(uint8_t *)(result);
        Arg1 = v_stack_mA70;
        local_rbx = v_stack_mBF0;
    }
    if ((uint16_t)(Arg1) == 0) goto loc_009FA995;
    if (((1) & ((uint8_t)(Arg1))) != 0) goto loc_009FA995;
    Arg2 = ((uint16_t)(Arg1)) + (v_stack_mC58);
    result = 32;
    if (v_stack_mC50 == 1) { result = 257; }
    result = ExAllocatePool2((uint32_t)((uint32_t)(result)), Arg2, (uint32_t)(0x624A7350ULL), (uint32_t)(0x8200ULL));
    v_stack_mBF0 = result;
    if (result != 0) goto loc_009FA962;
    v_stack_mC40 = (uint32_t)((uint32_t)(0xC0000017ULL));
    goto loc_009FAA35;
loc_009FA962:
    result = memcpy(result, v_stack_mA80, v_stack_mA70, (uint32_t)(0x8200ULL));
    result = (v_stack_mA70) >> (1);
    *(uint16_t *)(result + result * 2) = 0;
    v_stack_mA80 = result;
    goto loc_009FA9AD;
loc_009FA995:
    v_stack_mC40 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_009FAA35;
loc_009FA9AD:
    if (((v_stack_mA74) & (0xFFFFFFF0ULL)) == 0) goto loc_009FA9CB;
loc_009FA9BF:
loc_009FA9C4:
    goto loc_009FAA35;
loc_009FA9CB:
    if (v_stack_mA60 != 0) goto loc_009FA9E9;
    if (v_stack_mA88 != 0) goto loc_009FA9E9;
    if (v_stack_mA48 == 0) goto loc_009FA9F9;
loc_009FA9E9:
    result = EtwpCoverageUserIsAdmin(result, v_stack_mA80, v_stack_mA70, (uint32_t)(0x8200ULL));
    if ((uint8_t)(result) != 0) goto loc_009FA9F9;
    goto loc_009FA9BF;
loc_009FA9F9:
    result = PspSetJobIoRateControl(v_stack_mC58, v_stack_mA98, v_stack_mA70, (uint32_t)(0x8200ULL));
    goto loc_009FA9C4;
loc_009FAA35:
    if (result == 0) goto loc_009FAFC8;
    Arg2 = 0;
loc_009FAA43:
    result = ExFreePoolWithTag(result, Arg2, v_stack_mA70, (uint32_t)(0x8200ULL));
    goto loc_009FAFE1;
loc_009FAA4D:
    Arg3 = 0;
    Arg2 = 0;
    result = PspLockJobMemoryLimitsExclusive(v_stack_mC58, Arg2, Arg3, (uint32_t)(0x8200ULL));
    *(uint64_t *)(v_stack_mC58 + 0x2D0) = 0;
    *(uint64_t *)(v_stack_mC58 + 0x2C8) = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = PspUnlockJobMemoryLimitsExclusive(v_stack_mC58, Arg2, Arg3, (uint32_t)(0x8200ULL));
    goto loc_009FAFC2;
loc_009FAA82:
    v_stack_mB08 = v_xmm0;
    v_stack_mAF8 = v_xmm1;
    v_stack_mAE8 = v_xmm0;
    v_stack_mAD8 = v_xmm1;
    v_stack_mAC8 = v_xmm0;
    if (((v_stack_mB08) & (0xFFFFFFFCULL)) == 0) goto loc_009FAAEF;
loc_009FAAE0:
loc_009FAAE5:
    goto loc_009FABB4;
loc_009FAAEF:
    if (((v_stack_mB08) & (3)) == 0) goto loc_009FAAE0;
    local_rdi = (uint8_t)((v_stack_mB08) & (1));
    result = PspLockRootJobExclusive(v_stack_mC58, v_stack_mC10, v_stack_mBE8, (uint32_t)(0x8200ULL));
loc_009FAB21:
    if (0 >= 1) goto loc_009FAB37;
    if (v_stack_mC58 == (*(uint64_t *)(local_rsp + 0x0 * 8 + 0xB0))) goto loc_009FAB43;
    Arg1 = (uint32_t)((0) + (1));
    goto loc_009FAB21;
loc_009FAB37:
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, 1, v_stack_mBE8, (uint32_t)(0x8200ULL));
loc_009FAB43:
    result = PspSetJobIoAttribution(v_stack_mC58, (uint8_t)(local_rdi), 1, 1);
    if (sign_flag) goto loc_009FAAE5;
loc_009FAB5D:
    if (0 >= 1) goto loc_009FAB73;
    if (v_stack_mC58 == (*(uint64_t *)(local_rsp + 0x0 * 8 + 0xB0))) goto loc_009FAB7C;
    Arg1 = (uint32_t)((0) + (1));
    goto loc_009FAB5D;
loc_009FAB73:
    result = ExReleaseResourceLite(v_stack_mC58 + 56, (uint8_t)(local_rdi), 1, 1);
loc_009FAB7C:
    result = PspUnlockJob(v_stack_mBE8, v_stack_mC10, 1, 1);
    goto loc_009FAAE5;
loc_009FABB4:
    if (0 != 8) goto loc_009FAFC8;
    result = PspUnlockJobConditionally(v_stack_mC58, v_stack_mBE8, 1, 1);
    result = PspUnlockJob(v_stack_mBE8, v_stack_mC10, 1, 1);
    goto loc_009FAFE1;
loc_009FABE7:
    Arg1 = (uint32_t)((v_stack_mBE8) - (43));
    if (condition_is_equal) goto loc_009FAFA3;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009FAF38;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009FADC0;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009FAD83;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009FACEE;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_009FAC92;
    if (((uint32_t)(Arg1)) == 1) goto loc_009FAC28;
loc_009FAC1E:
    goto loc_009F8B05;
loc_009FAC28:
    v_stack_mBF8 = *(uint64_t *)((uint32_t)(v_stack_mC48));
    if ((((uint32_t)(*(uint64_t *)((uint32_t)(v_stack_mC48)))) & (0xFFFFFFFEULL)) != 0) goto loc_009FAD04;
    Arg2 = (*(uint64_t *)((uint32_t)(v_stack_mC48))) >> (32);
    if (Arg2 >= 8) goto loc_009FAD04;
    if (((1) & ((uint8_t)(*(uint64_t *)((uint32_t)(v_stack_mC48))))) == 0) goto loc_009FAC69;
    if (Arg2 == NULL) goto loc_009FAD43;
    goto loc_009FAC6E;
loc_009FAC69:
loc_009FAC6E:
    result = PspSetPagePriorityLimitJobTree(v_stack_mC58, 8, 1, 1);
    goto loc_009FA156;
loc_009FAC92:
    v_stack_mBF8 = *(uint64_t *)((uint32_t)(v_stack_mC48));
    if ((((uint32_t)(*(uint64_t *)((uint32_t)(v_stack_mC48)))) & (0xFFFFFFFEULL)) != 0) goto loc_009FAD04;
    Arg2 = (*(uint64_t *)((uint32_t)(v_stack_mC48))) >> (32);
    if (Arg2 >= 5) goto loc_009FAD43;
    if (((1) & ((uint8_t)(*(uint64_t *)((uint32_t)(v_stack_mC48))))) == 0) {
        Arg2 = 1 + 4;
    }
    result = PspSetIoPriorityLimitJobTree(v_stack_mC58, Arg2, 1, 1);
    goto loc_009FA156;
loc_009FACEE:
    v_stack_mBFF = (uint8_t)(*(uint8_t *)((uint32_t)(v_stack_mC48)));
    if (((uint8_t)(*(uint8_t *)((uint32_t)(v_stack_mC48)))) == 1) goto loc_009FAD13;
loc_009FAD04:
loc_009FAD09:
    goto loc_009FAFC8;
loc_009FAD13:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x5DED5A), v_stack_mC50, 1, 1);
    if ((uint8_t)(result) != 0) goto loc_009FAD36;
    goto loc_009FAFC8;
loc_009FAD36:
    if (((*(uint32_t *)(v_stack_mC58 + 0x610)) & (0x40000000ULL)) != 0) goto loc_009FAD4D;
loc_009FAD43:
    goto loc_009FAFC8;
loc_009FAD4D:
    result = PspSetJobSiloThreadImpersonationPolicy(v_stack_mC58, 2, 1, 1);
    result = (uint8_t)(-(result));
    Arg1 = (uint32_t)(~(v_stack_mC58));
    local_rsi = (uint32_t)(((uint32_t)(0xC0000022ULL)) & ((uint32_t)(Arg1)));
    goto loc_009FAFC8;
loc_009FAD83:
    v_stack_mB50 = *(uint64_t *)((uint32_t)(v_stack_mC48));
    result = PspSetEnergyTrackingStateJobTree(v_stack_mC58, v_stack_mB50, 1, 1);
    goto loc_009F9C7B;
loc_009FADC0:
    if (((*(uint32_t *)(v_stack_mC58 + 0x610)) & (0x40000000ULL)) == 0) goto loc_009FA2F4;
    v_stack_mB68 = 0;
    v_stack_mBF8 = v_xmm0;
    if (0 == 0) goto loc_009FAEF1;
    result = (uint16_t)(((uint16_t)(v_stack_mBF8)) - (1));
    if (((uint16_t)(result)) > 518) goto loc_009FAEF1;
    if (((1) & ((uint8_t)(v_stack_mBF8))) != 0) goto loc_009FAEF1;
    if (v_stack_mC50 != 1) goto loc_009FAE6A;
    if (((1) & (0)) != 0) {
        result = ExRaiseDatatypeMisalignment(518, v_stack_mB50, 1, 1);
    }
    if ((0 + v_stack_mBF8 * 1) > result) goto loc_009FAE53;
    local_rbx = 0;
    local_rsi = v_stack_mBF8;
    local_r14 = v_stack_mC58;
    if ((0 + v_stack_mBF8 * 1) < 0) {
        result = *(uint8_t *)(result);
        local_r14 = v_stack_mC58;
        local_rbx = v_stack_mBF0;
        local_rsi = v_stack_mBF8;
    }
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint16_t)(local_rsi))), (uint32_t)(0x72537350ULL), 1);
    v_stack_mB68 = result;
    if (result != 0) goto loc_009FAEA4;
    v_stack_mC40 = (uint32_t)((uint32_t)(0xC000009AULL));
    goto loc_009FAFE1;
loc_009FAEA4:
    result = memcpy(result, local_rbx, (uint32_t)(v_stack_mC48), 1);
    local_rbx = ((uint16_t)((uint32_t)(0xC000009AULL))) >> (1);
    result = wcsnlen(result, local_rbx, (uint32_t)(v_stack_mC48), 1);
    if (result == local_rbx) goto loc_009FAED5;
loc_009FAECE:
    goto loc_009FAF22;
loc_009FAED5:
    v_stack_mBF0 = result;
    result = PspAssignSiloSystemRootPath(local_r14, v_stack_mBF8, (uint32_t)(v_stack_mC48), 1);
    goto loc_009FAECE;
loc_009FAEF1:
    v_stack_mC40 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_009FAFE1;
loc_009FAF22:
    if (result == 0) goto loc_009FAFE1;
    goto loc_009FAA43;
loc_009FAF38:
    result = ExAcquireResourceExclusiveLite(v_stack_mC58 + 56, 1, (uint32_t)(v_stack_mC48), 1);
    if ((*(uint32_t *)(v_stack_mC58 + 0x610)) >= 0) goto loc_009FAF62;
    goto loc_009F8A9D;
loc_009FAF62:
    *(uint64_t *)(v_stack_mC58 + 0x5D0) = v_xmm0;
    goto loc_009FA14D;
loc_009FAFA3:
    v_stack_mAA8 = *(uint64_t *)((uint32_t)(v_stack_mC48));
    result = PspSetJobMemoryPartition(v_stack_mC58, v_stack_mC50, *(uint64_t *)((uint32_t)(v_stack_mC48)), 1);
loc_009FAFC0:
loc_009FAFC2:
loc_009FAFC8:
    goto loc_009FAFE1;
loc_009FAFE1:
    if ((*(uint32_t *)(v_stack_mC58 + 0x610)) != 0) goto loc_009FB006;
    result = v_stack_mC10 + 152;
    if ((*(uint64_t *)(v_stack_mC10 + 0x98)) != (v_stack_mC10 + 152)) {
        result = KiCheckForKernelApcDelivery(v_stack_mC10, v_stack_mC50, *(uint64_t *)((uint32_t)(v_stack_mC48)), 1);
    }
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_009FB032;
    if (((*(uint32_t *)(v_rip + 0x5CBAEC)) & (0x80000ULL)) != 0) {
        v_stack_mC70 = 0x727ULL;
        v_stack_mC78 = (uint32_t)((uint32_t)((uint32_t)(result)));
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = (uint32_t)((uint32_t)(v_stack_mC48));
        Arg1 = v_stack_mC58;
        result = EtwTraceJobSetQuery(Arg1, Arg2, Arg3, Arg4);
    }
    result = ObfDereferenceObjectWithTag(v_stack_mC58, (uint32_t)(0x79517350ULL), Arg3, Arg4);
    goto loc_009FB048;
loc_009FB043:
loc_009FB048:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(0x79517350ULL), Arg3, Arg4);
    local_rsp = (local_rsp) + (0xC60ULL);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `- 0x1` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009F84C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
