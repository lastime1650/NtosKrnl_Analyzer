# ObpCreateHandle

- RVA: `0x0086B950`–`0x0086DA05` (길이 `8,373` bytes)
- VA: `0x000000014086B950`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C0A0`
- 디코드: `1,996`개 명령, `8,373/8,373` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **137**; 고유 호출 대상: **73**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **24**

### Outgoing calls
- `0x0086BB45` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x0086BB6C` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x0086BBAF` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (function, `0x003A6BC0`)
- `0x0086BC07` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0086BC16` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x0086BC6C` → [SeOpenObjectAuditAlarmWithTransaction](SeOpenObjectAuditAlarmWithTransaction_function_0086E790.md) (function, `0x0086E790`)
- `0x0086BC79` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0086BC87` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086BC99` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0086BCA7` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086BDDD` → [SeComputeCreatorDeniedRights](../../text/3A/SeComputeCreatorDeniedRights_function_003A6080.md) (function, `0x003A6080`)
- `0x0086BE5B` → [ObpIncrementHandleCountEx](ObpIncrementHandleCountEx_function_0086DA10.md) (function, `0x0086DA10`)
- `0x0086BF20` → [SeComputeCreatorDeniedRights](../../text/3A/SeComputeCreatorDeniedRights_function_003A6080.md) (function, `0x003A6080`)
- `0x0086BF87` → [ObReferenceObjectExWithTag](../../text/41/ObReferenceObjectExWithTag_function_0041FDB0.md) (function, `0x0041FDB0`)
- `0x0086BF97` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0086C083` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0086C09C` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0086C0EB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0086C14B` → [ExpUpdateDebugInfo](ExpUpdateDebugInfo_function_0086B174.md) (function, `0x0086B174`)
- `0x0086C162` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086C26F` → [SepAdtPrivilegeObjectAuditAlarm](SepAdtPrivilegeObjectAuditAlarm_function_0086E3F0.md) (function, `0x0086E3F0`)
- `0x0086C27F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0086C37D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0086C38B` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086C41F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0086C446` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0086C475` → [ExpLookupHandleTableEntry](ExpLookupHandleTableEntry_function_00869DB0.md) (function, `0x00869DB0`)
- `0x0086C4D6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0086C53E` → [CmpSecurityMethod](../87/CmpSecurityMethod_function_00870CC0.md) (function, `0x00870CC0`)
- `0x0086C5A8` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)
- `0x0086C5BA` → [ExfAcquireRundownProtection](../../text/34/ExfAcquireRundownProtection_function_0034C050.md) (function, `0x0034C050`)
- `0x0086C6D9` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x0086C6F5` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x0086C712` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0086C720` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086C729` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0086C737` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086C746` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0086C830` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0086C856` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0086C87B` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0086C906` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0086C92C` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x0086C979` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0086C9B4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0086C9DB` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0086CA3C` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0086CA62` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (function, `0x002E2C80`)
- `0x0086CACC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0086CB0C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0086CB1A` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086CB3C` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x0086CB64` → [ExpAllocateTablePagedPool](../94/ExpAllocateTablePagedPool_function_0094D634.md) (function, `0x0094D634`)
- `0x0086CB93` → [ExpFreeTablePagedPool](ExpFreeTablePagedPool_function_0086B410.md) (function, `0x0086B410`)
- `0x0086CBC6` → [ExpGetHandleExtraInfo](ExpGetHandleExtraInfo_function_0086B454.md) (function, `0x0086B454`)
- `0x0086CC05` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0086CC1E` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0086CC68` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0086CC9A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0086CCA3` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0086CCB9` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)
- `0x0086CCE0` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0086CD0D` → [ObpInsertOrLocateNamedObject](../99/ObpInsertOrLocateNamedObject_function_0099F2C0.md) (function, `0x0099F2C0`)
- `0x0086CD95` → [SepPrivilegeCheck](../../text/40/SepPrivilegeCheck_function_0040B6B0.md) (function, `0x0040B6B0`)
- `0x0086CDB2` → [SePrivilegedServiceAuditAlarm](../87/SePrivilegedServiceAuditAlarm_function_00871CB0.md) (function, `0x00871CB0`)
- `0x0086CDC7` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0086CDEB` → [ObpCreateSymbolicLinkName](../74/ObpCreateSymbolicLinkName_function_0074EB80.md) (function, `0x0074EB80`)
- `0x0086CDFF` → [ObpDecrementHandleCount](ObpDecrementHandleCount_function_008632E0.md) (function, `0x008632E0`)
- `0x0086CE19` → [ObDereferenceObjectExWithTag](../../text/43/ObDereferenceObjectExWithTag_function_0043CBC0.md) (function, `0x0043CBC0`)
- `0x0086CE33` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)
- `0x0086CF00` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (function, `0x00400AD0`)
- `0x0086CF15` → [OBJECT_HEADER_TO_HANDLE_REVOCATION_INFO](../../text/3A/OBJECT_HEADER_TO_HANDLE_REVOCATION_INFO_function_003A1840.md) (function, `0x003A1840`)
- `0x0086CF40` → [SepSidInTokenSidHash](../../text/3C/SepSidInTokenSidHash_function_003C85E0.md) (function, `0x003C85E0`)
- `0x0086CF5E` → [ObHandleRevocationBlockAddObject](../9A/ObHandleRevocationBlockAddObject_function_009A9280.md) (function, `0x009A9280`)
- `0x0086CF6D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0086CF90` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0086CFAB` → [ObpAllocateAndQuerySecurityDescriptorInfo](../87/ObpAllocateAndQuerySecurityDescriptorInfo_function_0087421C.md) (function, `0x0087421C`)
- `0x0086CFC3` → [ObpSetObjectAuditInfo](../8B/ObpSetObjectAuditInfo_function_008BD1F8.md) (function, `0x008BD1F8`)
- `0x0086CFE6` → [EtwpTraceHandle](EtwpTraceHandle_function_0086AA44.md) (function, `0x0086AA44`)
- `0x0086CFF8` → [ObDereferenceSecurityDescriptor](../87/ObDereferenceSecurityDescriptor_function_008740A0.md) (function, `0x008740A0`)
- `0x0086D002` → [ExfAcquireRundownProtection](../../text/34/ExfAcquireRundownProtection_function_0034C050.md) (function, `0x0034C050`)
- `0x0086D03E` → [IopGetSetSecurityObject](../87/IopGetSetSecurityObject_function_00873A80.md) (function, `0x00873A80`)
- `0x0086D050` → [ObpReferenceSecurityDescriptorSlow](../87/ObpReferenceSecurityDescriptorSlow_function_0087484C.md) (function, `0x0087484C`)
- `0x0086D06D` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x0086D086` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x0086D0A0` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)
- `0x0086D0D0` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0086D0EA` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0086D10B` → [ExpAllocateHandleTableEntrySlow](../94/ExpAllocateHandleTableEntrySlow_function_0094D2FC.md) (function, `0x0094D2FC`)
- `0x0086D12E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0086D172` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)
- `0x0086D194` → [SeAppendPrivileges](../9D/SeAppendPrivileges_function_009D7980.md) (function, `0x009D7980`)
- `0x0086D1C0` → [ObDereferenceSecurityDescriptor](../87/ObDereferenceSecurityDescriptor_function_008740A0.md) (function, `0x008740A0`)
- `0x0086D1E3` → [ObpReferenceSecurityDescriptorSlow](../87/ObpReferenceSecurityDescriptorSlow_function_0087484C.md) (function, `0x0087484C`)
- `0x0086D1F8` → [ObDereferenceSecurityDescriptor](../87/ObDereferenceSecurityDescriptor_function_008740A0.md) (function, `0x008740A0`)
- `0x0086D20A` → [ObpReferenceSecurityDescriptorSlow](../87/ObpReferenceSecurityDescriptorSlow_function_0087484C.md) (function, `0x0087484C`)
- `0x0086D224` → [ObpSetObjectAuditInfo](../8B/ObpSetObjectAuditInfo_function_008BD1F8.md) (function, `0x008BD1F8`)
- `0x0086D267` → [ZwDuplicateObject](../../text/6A/ZwDuplicateObject_function_006AD850.md) (function, `0x006AD850`)
- `0x0086D296` → [ObReferenceObjectByHandle](ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x0086D2B2` → [SepAdtClassifyObjectIntoSubCategory](../91/SepAdtClassifyObjectIntoSubCategory_function_0091FA60.md) (function, `0x0091FA60`)
- `0x0086D2C3` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0086D2D1` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x0086D2DA` → [PsGetCurrentProcessId](../../text/43/PsGetCurrentProcessId_function_00433560.md) (function, `0x00433560`)
- `0x0086D36F` → [SepAdtOpenObjectAuditAlarm](../91/SepAdtOpenObjectAuditAlarm_function_0091F23C.md) (function, `0x0091F23C`)
- `0x0086D3BA` → [SepAdtStagingEvent](../91/SepAdtStagingEvent_function_0091F948.md) (function, `0x0091F948`)
- `0x0086D419` → [SepAdtPrivilegeObjectAuditAlarm](SepAdtPrivilegeObjectAuditAlarm_function_0086E3F0.md) (function, `0x0086E3F0`)
- `0x0086D438` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0086D4A4` → [ObpCallPostOperationCallbacks](../9A/ObpCallPostOperationCallbacks_function_009A7BC0.md) (function, `0x009A7BC0`)
- `0x0086D548` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (function, `0x0044BEE0`)
- `0x0086D550` → [PsAttachSiloToCurrentThread](../../text/44/PsAttachSiloToCurrentThread_function_004428C0.md) (function, `0x004428C0`)
- `0x0086D564` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (function, `0x00216800`)
- `0x0086D58B` → [CmpCloseKeyObject](CmpCloseKeyObject_function_00863AD0.md) (function, `0x00863AD0`)
- `0x0086D59F` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x0086D5A8` → [PsDetachSiloFromCurrentThread](../../text/44/PsDetachSiloFromCurrentThread_function_00449AC0.md) (function, `0x00449AC0`)
- `0x0086D5B6` → [ObpDeleteNameCheck](../89/ObpDeleteNameCheck_function_0089A3F0.md) (function, `0x0089A3F0`)
- `0x0086D5D4` → [ObDereferenceObjectExWithTag](../../text/43/ObDereferenceObjectExWithTag_function_0043CBC0.md) (function, `0x0043CBC0`)
- `0x0086D60C` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x0086D63D` → [EtwpEventWriteTemplateSessAndProv](EtwpEventWriteTemplateSessAndProv_function_00863D18.md) (function, `0x00863D18`)
- `0x0086D66B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0086D688` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0086D76E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0086D77C` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086D79F` → [IopCloseFile](IopCloseFile_function_008640C0.md) (function, `0x008640C0`)
- `0x0086D80D` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0086D81B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0086D82A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0086D845` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0086D898` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0086D8AD` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086D8BE` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0086D90B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0086D93F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0086D94E` → [SepConcatenatePrivileges](../9D/SepConcatenatePrivileges_function_009D7AD0.md) (function, `0x009D7AD0`)
- `0x0086D95E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0086D986` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0086D993` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0086D9EC` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_0089A903](../89/Unknown_function_0089A903.md) at `0x0089ACA5`
- [sub_008B756E](../8B/Unknown_function_008B756E.md) at `0x008B75DA`
- [ObInsertObjectEx](../8B/ObInsertObjectEx_function_008B97A0.md) at `0x008B98F6`
- [ObInsertObjectEx](../8B/ObInsertObjectEx_function_008B97A0.md) at `0x008B9BE8`

### Static image references
- `0x0086B96C` → RVA `0x00E0A740` (`.data`; read)
- `0x0086BA38` → RVA `0x00F0F5B8` (`.data`; read)
- `0x0086BA95` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x0086BAA3` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0086BABA` → RVA `0x008BA2B0` (`SeDefaultObjectMethod`; read)
- `0x0086C042` → RVA `0x00FD9B18` (`PAGEDATA`; read)
- `0x0086C179` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x0086C237` → RVA `0x000013A8` (`.rdata`; read)
- `0x0086C28C` → RVA `0x00FC6AC0` (`ALMOSTRO`; read)
- `0x0086C394` → RVA `0x00FC6B10` (`ALMOSTRO`; read)
- `0x0086C4A2` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x0086C4B9` → RVA `0x00E0B38C` (`.data`; read)
- `0x0086C500` → RVA `0x00870CC0` (`CmpSecurityMethod`; read)
- `0x0086C69A` → RVA `0x00FC6AE0` (`ALMOSTRO`; read)
- `0x0086CD3D` → RVA `0x00FD9B00` (`PAGEDATA`; read)
- `0x0086CDD1` → RVA `0x00F0F658` (`.data`; read)
- `0x0086CF23` → RVA `0x00F05870` (`.data`; read)
- `0x0086D01F` → RVA `0x00873A80` (`IopGetSetSecurityObject`; read)
- `0x0086D574` → RVA `0x00863AD0` (`CmpCloseKeyObject`; read)
- `0x0086D5DE` → RVA `0x00A0CEB0` (`EtwpCloseRegistrationObject`; read)
- `0x0086D5FE` → RVA `0x00EFF840` (`.data`; read)
- `0x0086D605` → RVA `0x00010888` (`.rdata`; read)
- `0x0086D788` → RVA `0x008640C0` (`IopCloseFile`; read)
- `0x0086D839` → RVA `0x00E0B38C` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **99**
  - `0x0086BB45` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x0086BB6C` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x0086BBAF` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (`PAGE` → `.text`)
  - `0x0086BC07` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0086BC16` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x0086BC79` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x0086BC87` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086BC99` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x0086BCA7` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086BDDD` → [SeComputeCreatorDeniedRights](../../text/3A/SeComputeCreatorDeniedRights_function_003A6080.md) (`PAGE` → `.text`)
  - `0x0086BF20` → [SeComputeCreatorDeniedRights](../../text/3A/SeComputeCreatorDeniedRights_function_003A6080.md) (`PAGE` → `.text`)
  - `0x0086BF87` → [ObReferenceObjectExWithTag](../../text/41/ObReferenceObjectExWithTag_function_0041FDB0.md) (`PAGE` → `.text`)
  - `0x0086BF97` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0086C083` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0086C09C` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0086C0EB` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0086C162` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086C27F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0086C37D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0086C38B` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086C41F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0086C446` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0086C4D6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0086C5A8` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (`PAGE` → `.text`)
  - `0x0086C5BA` → [ExfAcquireRundownProtection](../../text/34/ExfAcquireRundownProtection_function_0034C050.md) (`PAGE` → `.text`)
  - `0x0086C6D9` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x0086C6F5` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x0086C712` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x0086C720` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086C729` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x0086C737` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086C746` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0086C830` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x0086C856` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0086C87B` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0086C906` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0086C92C` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x0086C979` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0086C9B4` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0086C9DB` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0086CA3C` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0086CA62` → [KiCheckForKernelApcDelivery](../../text/2E/KiCheckForKernelApcDelivery_function_002E2C80.md) (`PAGE` → `.text`)
  - `0x0086CACC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0086CB0C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0086CB1A` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086CB3C` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x0086CC05` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0086CC1E` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0086CC68` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0086CC9A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x0086CCA3` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x0086CCB9` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (`PAGE` → `.text`)
  - `0x0086CCE0` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x0086CD95` → [SepPrivilegeCheck](../../text/40/SepPrivilegeCheck_function_0040B6B0.md) (`PAGE` → `.text`)
  - `0x0086CDC7` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0086CE19` → [ObDereferenceObjectExWithTag](../../text/43/ObDereferenceObjectExWithTag_function_0043CBC0.md) (`PAGE` → `.text`)
  - `0x0086CE33` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (`PAGE` → `.text`)
  - `0x0086CF00` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (`PAGE` → `.text`)
  - `0x0086CF15` → [OBJECT_HEADER_TO_HANDLE_REVOCATION_INFO](../../text/3A/OBJECT_HEADER_TO_HANDLE_REVOCATION_INFO_function_003A1840.md) (`PAGE` → `.text`)
  - `0x0086CF40` → [SepSidInTokenSidHash](../../text/3C/SepSidInTokenSidHash_function_003C85E0.md) (`PAGE` → `.text`)
  - `0x0086CF6D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0086CF90` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0086D002` → [ExfAcquireRundownProtection](../../text/34/ExfAcquireRundownProtection_function_0034C050.md) (`PAGE` → `.text`)
  - `0x0086D06D` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (`PAGE` → `.text`)
  - `0x0086D086` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (`PAGE` → `.text`)
  - `0x0086D0A0` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (`PAGE` → `.text`)
  - `0x0086D0D0` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0086D0EA` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0086D12E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0086D172` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (`PAGE` → `.text`)
  - `0x0086D267` → [ZwDuplicateObject](../../text/6A/ZwDuplicateObject_function_006AD850.md) (`PAGE` → `.text`)
  - `0x0086D2C3` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0086D2D1` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x0086D2DA` → [PsGetCurrentProcessId](../../text/43/PsGetCurrentProcessId_function_00433560.md) (`PAGE` → `.text`)
  - `0x0086D438` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x0086D548` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (`PAGE` → `.text`)
  - `0x0086D550` → [PsAttachSiloToCurrentThread](../../text/44/PsAttachSiloToCurrentThread_function_004428C0.md) (`PAGE` → `.text`)
  - `0x0086D564` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (`PAGE` → `.text`)
  - `0x0086D59F` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x0086D5A8` → [PsDetachSiloFromCurrentThread](../../text/44/PsDetachSiloFromCurrentThread_function_00449AC0.md) (`PAGE` → `.text`)
  - `0x0086D5D4` → [ObDereferenceObjectExWithTag](../../text/43/ObDereferenceObjectExWithTag_function_0043CBC0.md) (`PAGE` → `.text`)
  - `0x0086D60C` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x0086D66B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0086D688` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0086D76E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0086D77C` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086D80D` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x0086D81B` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0086D82A` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0086D845` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0086D898` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0086D8AD` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086D8BE` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0086D90B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0086D93F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0086D95E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0086D986` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0086D993` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0086D9EC` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0086B950  40 55                           push rbp
0086B952  53                              push rbx
0086B953  56                              push rsi
0086B954  57                              push rdi
0086B955  41 54                           push r12
0086B957  41 55                           push r13
0086B959  41 56                           push r14
0086B95B  41 57                           push r15
0086B95D  48 8D AC 24 78 FE FF FF         lea rbp, [rsp - 0x188]
0086B965  48 81 EC A8 02 00 00            sub rsp, 0x2a8
0086B96C  48 8B 05 CD ED 59 00            mov rax, qword ptr [rip + 0x59edcd]
0086B973  48 33 C4                        xor rax, rsp
0086B976  48 89 85 78 01 00 00            mov qword ptr [rbp + 0x178], rax
0086B97D  48 8B 85 18 02 00 00            mov rax, qword ptr [rbp + 0x218]
0086B984  49 8B F1                        mov rsi, r9
0086B987  44 8B B5 F8 01 00 00            mov r14d, dword ptr [rbp + 0x1f8]
0086B98E  45 33 C9                        xor r9d, r9d
0086B991  4C 8B AD 08 02 00 00            mov r13, qword ptr [rbp + 0x208]
0086B998  0F 57 C0                        xorps xmm0, xmm0
0086B99B  48 89 85 B0 00 00 00            mov qword ptr [rbp + 0xb0], rax
0086B9A2  4C 8B E2                        mov r12, rdx
0086B9A5  48 8B 85 20 02 00 00            mov rax, qword ptr [rbp + 0x220]
0086B9AC  41 8B D8                        mov ebx, r8d
0086B9AF  48 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], rax
0086B9B6  8B 85 10 02 00 00               mov eax, dword ptr [rbp + 0x210]
0086B9BC  44 89 4D 84                     mov dword ptr [rbp - 0x7c], r9d
0086B9C0  4C 89 4D 40                     mov qword ptr [rbp + 0x40], r9
0086B9C4  89 45 44                        mov dword ptr [rbp + 0x44], eax
0086B9C7  48 89 55 A0                     mov qword ptr [rbp - 0x60], rdx
0086B9CB  8B D1                           mov edx, ecx
0086B9CD  89 4D E8                        mov dword ptr [rbp - 0x18], ecx
0086B9D0  4C 89 6D A8                     mov qword ptr [rbp - 0x58], r13
0086B9D4  4C 89 4D 18                     mov qword ptr [rbp + 0x18], r9
0086B9D8  44 88 4D 82                     mov byte ptr [rbp - 0x7e], r9b
0086B9DC  4C 89 4D 20                     mov qword ptr [rbp + 0x20], r9
0086B9E0  44 88 4D 88                     mov byte ptr [rbp - 0x78], r9b
0086B9E4  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0086B9E8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086B9F1  4C 8B 90 B8 00 00 00            mov r10, qword ptr [rax + 0xb8]
0086B9F8  4C 89 55 98                     mov qword ptr [rbp - 0x68], r10
0086B9FC  41 0F BA E6 09                  bt r14d, 9
0086BA01  0F 82 9B 0A 00 00               jb 0x14086c4a2
0086BA07  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086BA10  80 B8 4A 02 00 00 01            cmp byte ptr [rax + 0x24a], 1
0086BA17  0F 84 43 0B 00 00               je 0x14086c560
0086BA1D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086BA26  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0086BA2D  48 8B 89 00 03 00 00            mov rcx, qword ptr [rcx + 0x300]
0086BA34  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
0086BA38  48 3B 0D 79 3B 6A 00            cmp rcx, qword ptr [rip + 0x6a3b79]
0086BA3F  0F 94 C0                        sete al
0086BA42  88 45 83                        mov byte ptr [rbp - 0x7d], al
0086BA45  48 85 F6                        test rsi, rsi
0086BA48  0F 84 A3 0B 00 00               je 0x14086c5f1
0086BA4E  84 C0                           test al, al
0086BA50  0F 85 91 0B 00 00               jne 0x14086c5e7
0086BA56  0F B6 85 00 02 00 00            movzx eax, byte ptr [rbp + 0x200]
0086BA5D  41 0F BA E6 0A                  bt r14d, 0xa
0086BA62  41 BF 01 00 00 00               mov r15d, 1
0086BA68  44 89 4D B4                     mov dword ptr [rbp - 0x4c], r9d
0086BA6C  44 0F 43 F8                     cmovae r15d, eax
0086BA70  8D 42 FF                        lea eax, [rdx - 1]
0086BA73  83 F8 01                        cmp eax, 1
0086BA76  49 8D 44 24 D0                  lea rax, [r12 - 0x30]
0086BA7B  0F 87 72 02 00 00               ja 0x14086bcf3
0086BA81  48 C1 E8 08                     shr rax, 8
0086BA85  0F B6 C8                        movzx ecx, al
0086BA88  41 0F B6 44 24 E8               movzx eax, byte ptr [r12 - 0x18]
0086BA8E  48 33 C8                        xor rcx, rax
0086BA91  44 89 4D 28                     mov dword ptr [rbp + 0x28], r9d
0086BA95  0F B6 05 B0 B3 75 00            movzx eax, byte ptr [rip + 0x75b3b0]
0086BA9C  48 33 C8                        xor rcx, rax
0086BA9F  4C 89 4D 68                     mov qword ptr [rbp + 0x68], r9
0086BAA3  48 8D 05 56 45 79 FF            lea rax, [rip - 0x86baaa]
0086BAAA  44 89 4D B0                     mov dword ptr [rbp - 0x50], r9d
0086BAAE  44 89 4D C0                     mov dword ptr [rbp - 0x40], r9d
0086BAB2  4C 8B AC C8 00 78 FC 00         mov r13, qword ptr [rax + rcx*8 + 0xfc7800]
0086BABA  48 8D 05 EF E7 04 00            lea rax, [rip + 0x4e7ef]
0086BAC1  4C 89 6D 08                     mov qword ptr [rbp + 8], r13
0086BAC5  49 39 85 98 00 00 00            cmp qword ptr [r13 + 0x98], rax
0086BACC  0F 85 E7 09 00 00               jne 0x14086c4b9
0086BAD2  41 0F 0D 4C 24 F8               prefetchw byte ptr [r12 - 8]
0086BAD8  49 8B 54 24 F8                  mov rdx, qword ptr [r12 - 8]
0086BADD  F6 C2 0F                        test dl, 0xf
0086BAE0  74 17                           je 0x14086baf9
0086BAE2  48 8D 4A FF                     lea rcx, [rdx - 1]
0086BAE6  48 8B C2                        mov rax, rdx
0086BAE9  F0 49 0F B1 4C 24 F8            lock cmpxchg qword ptr [r12 - 8], rcx
0086BAF0  74 07                           je 0x14086baf9
0086BAF2  48 8B D0                        mov rdx, rax
0086BAF5  A8 0F                           test al, 0xf
0086BAF7  75 E9                           jne 0x14086bae2
0086BAF9  48 8B DA                        mov rbx, rdx
0086BAFC  83 E2 0F                        and edx, 0xf
0086BAFF  48 83 E3 F0                     and rbx, 0xfffffffffffffff0
0086BB03  83 FA 01                        cmp edx, 1
0086BB06  77 09                           ja 0x14086bb11
0086BB08  48 85 DB                        test rbx, rbx
0086BB0B  0F 85 F1 16 00 00               jne 0x14086d202
0086BB11  C6 45 80 00                     mov byte ptr [rbp - 0x80], 0
0086BB15  48 85 DB                        test rbx, rbx
0086BB18  0F 84 59 11 00 00               je 0x14086cc77
0086BB1E  41 8B F9                        mov edi, r9d
0086BB21  48 85 DB                        test rbx, rbx
0086BB24  0F 84 3B 0B 00 00               je 0x14086c665
0086BB2A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086BB33  B2 01                           mov dl, 1
0086BB35  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0086BB3C  90                              nop
0086BB3D  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
0086BB41  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
0086BB45  E8 76 60 9A FF                  call 0x140211bc0
0086BB4A  48 83 7E 20 00                  cmp qword ptr [rsi + 0x20], 0
0086BB4F  74 20                           je 0x14086bb71
0086BB51  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086BB5A  B2 01                           mov dl, 1
0086BB5C  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0086BB63  90                              nop
0086BB64  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
0086BB68  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
0086BB6C  E8 4F 60 9A FF                  call 0x140211bc0
0086BB71  44 8B 4E 10                     mov r9d, dword ptr [rsi + 0x10]
0086BB75  48 8D 4D B4                     lea rcx, [rbp - 0x4c]
0086BB79  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
0086BB7E  49 8D 45 4C                     lea rax, [r13 + 0x4c]
0086BB82  48 8D 4D 28                     lea rcx, [rbp + 0x28]
0086BB86  41 B0 01                        mov r8b, 1
0086BB89  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
0086BB8E  48 8D 56 20                     lea rdx, [rsi + 0x20]
0086BB92  44 88 7C 24 38                  mov byte ptr [rsp + 0x38], r15b
0086BB97  48 8B CB                        mov rcx, rbx
0086BB9A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0086BB9F  48 8D 45 68                     lea rax, [rbp + 0x68]
0086BBA3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0086BBA8  8B 46 14                        mov eax, dword ptr [rsi + 0x14]
0086BBAB  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0086BBAF  E8 0C B0 B3 FF                  call 0x1403a6bc0
0086BBB4  4C 8B 65 68                     mov r12, qword ptr [rbp + 0x68]
0086BBB8  44 0F B6 E8                     movzx r13d, al
0086BBBC  4D 85 E4                        test r12, r12
0086BBBF  74 5A                           je 0x14086bc1b
0086BBC1  48 8B 46 48                     mov rax, qword ptr [rsi + 0x48]
0086BBC5  45 8B 04 24                     mov r8d, dword ptr [r12]
0086BBC9  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
0086BBCD  48 8B 38                        mov rdi, qword ptr [rax]
0086BBD0  8B 17                           mov edx, dword ptr [rdi]
0086BBD2  42 8D 0C 02                     lea ecx, [rdx + r8]
0086BBD6  83 F9 03                        cmp ecx, 3
0086BBD9  0F 87 E9 1C 00 00               ja 0x14086d8c8
0086BBDF  48 85 FF                        test rdi, rdi
0086BBE2  0F 84 93 0A 00 00               je 0x14086c67b
0086BBE8  85 D2                           test edx, edx
0086BBEA  0F 85 5E 12 00 00               jne 0x14086ce4e
0086BBF0  B8 08 00 00 00                  mov eax, 8
0086BBF5  8B C8                           mov ecx, eax
0086BBF7  47 8D 04 40                     lea r8d, [r8 + r8*2]
0086BBFB  48 03 CF                        add rcx, rdi
0086BBFE  41 C1 E0 02                     shl r8d, 2
0086BC02  49 8D 54 24 08                  lea rdx, [r12 + 8]
0086BC07  E8 34 AC E5 FF                  call 0x1406c6840
0086BC0C  41 8B 04 24                     mov eax, dword ptr [r12]
0086BC10  01 07                           add dword ptr [rdi], eax
0086BC12  48 8B 4D 68                     mov rcx, qword ptr [rbp + 0x68]
0086BC16  E8 65 A1 C0 FF                  call 0x140475d80
0086BC1B  45 84 ED                        test r13b, r13b
0086BC1E  74 0F                           je 0x14086bc2f
0086BC20  8B 4D 28                        mov ecx, dword ptr [rbp + 0x28]
0086BC23  09 4E 14                        or dword ptr [rsi + 0x14], ecx
0086BC26  0F BA E9 19                     bts ecx, 0x19
0086BC2A  F7 D1                           not ecx
0086BC2C  21 4E 10                        and dword ptr [rsi + 0x10], ecx
0086BC2F  4C 8B 65 A0                     mov r12, qword ptr [rbp - 0x60]
0086BC33  45 84 FF                        test r15b, r15b
0086BC36  74 39                           je 0x14086bc71
0086BC38  48 8B 4D 08                     mov rcx, qword ptr [rbp + 8]
0086BC3C  48 8D 46 0A                     lea rax, [rsi + 0xa]
0086BC40  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0086BC45  48 83 C1 10                     add rcx, 0x10
0086BC49  33 C0                           xor eax, eax
0086BC4B  4C 8B CB                        mov r9, rbx
0086BC4E  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0086BC53  45 33 C0                        xor r8d, r8d
0086BC56  44 88 7C 24 38                  mov byte ptr [rsp + 0x38], r15b
0086BC5B  49 8B D4                        mov rdx, r12
0086BC5E  44 88 6C 24 30                  mov byte ptr [rsp + 0x30], r13b
0086BC63  88 44 24 28                     mov byte ptr [rsp + 0x28], al
0086BC67  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
0086BC6C  E8 1F 2B 00 00                  call 0x14086e790
0086BC71  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
0086BC75  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
0086BC79  E8 92 3D 9F FF                  call 0x14025fa10
0086BC7E  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086BC87  E8 64 33 9F FF                  call 0x14025eff0
0086BC8C  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
0086BC90  48 85 C9                        test rcx, rcx
0086BC93  74 17                           je 0x14086bcac
0086BC95  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
0086BC99  E8 72 3D 9F FF                  call 0x14025fa10
0086BC9E  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086BCA7  E8 44 33 9F FF                  call 0x14025eff0
0086BCAC  80 7D 80 00                     cmp byte ptr [rbp - 0x80], 0
0086BCB0  0F 85 8B 0A 00 00               jne 0x14086c741
0086BCB6  41 0F 0D 4C 24 F8               prefetchw byte ptr [r12 - 8]
0086BCBC  49 8B 44 24 F8                  mov rax, qword ptr [r12 - 8]
0086BCC1  48 8B C8                        mov rcx, rax
0086BCC4  48 33 CB                        xor rcx, rbx
0086BCC7  48 83 F9 0F                     cmp rcx, 0xf
0086BCCB  0F 83 1F 15 00 00               jae 0x14086d1f0
0086BCD1  48 8D 48 01                     lea rcx, [rax + 1]
0086BCD5  F0 49 0F B1 4C 24 F8            lock cmpxchg qword ptr [r12 - 8], rcx
0086BCDC  75 E3                           jne 0x14086bcc1
0086BCDE  45 84 ED                        test r13b, r13b
0086BCE1  0F 84 C7 1C 00 00               je 0x14086d9ae
0086BCE7  4C 8B 6D A8                     mov r13, qword ptr [rbp - 0x58]
0086BCEB  45 33 C9                        xor r9d, r9d
0086BCEE  E9 28 01 00 00                  jmp 0x14086be1b
0086BCF3  48 C1 E8 08                     shr rax, 8
0086BCF7  0F B6 D0                        movzx edx, al
0086BCFA  41 0F B6 44 24 E8               movzx eax, byte ptr [r12 - 0x18]
0086BD00  48 33 D0                        xor rdx, rax
0086BD03  0F B6 05 42 B1 75 00            movzx eax, byte ptr [rip + 0x75b142]
0086BD0A  48 33 D0                        xor rdx, rax
0086BD0D  48 8D 05 EC 42 79 FF            lea rax, [rip - 0x86bd14]
0086BD14  48 8B 9C D0 00 78 FC 00         mov rbx, qword ptr [rax + rdx*8 + 0xfc7800]
0086BD1C  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
0086BD1F  0F BA E0 19                     bt eax, 0x19
0086BD23  73 0B                           jae 0x14086bd30
0086BD25  0F BA F0 19                     btr eax, 0x19
0086BD29  0F BA E8 1C                     bts eax, 0x1c
0086BD2D  89 46 10                        mov dword ptr [rsi + 0x10], eax
0086BD30  A9 00 00 00 F0                  test eax, 0xf0000000
0086BD35  74 2A                           je 0x14086bd61
0086BD37  85 C0                           test eax, eax
0086BD39  79 03                           jns 0x14086bd3e
0086BD3B  0B 43 4C                        or eax, dword ptr [rbx + 0x4c]
0086BD3E  0F BA E0 1E                     bt eax, 0x1e
0086BD42  73 03                           jae 0x14086bd47
0086BD44  0B 43 50                        or eax, dword ptr [rbx + 0x50]
0086BD47  0F BA E0 1D                     bt eax, 0x1d
0086BD4B  73 03                           jae 0x14086bd50
0086BD4D  0B 43 54                        or eax, dword ptr [rbx + 0x54]
0086BD50  0F BA E0 1C                     bt eax, 0x1c
0086BD54  73 03                           jae 0x14086bd59
0086BD56  0B 43 58                        or eax, dword ptr [rbx + 0x58]
0086BD59  25 FF FF FF 0F                  and eax, 0xfffffff
0086BD5E  89 46 10                        mov dword ptr [rsi + 0x10], eax
0086BD61  0F BA E0 18                     bt eax, 0x18
0086BD65  0F 82 D2 0F 00 00               jb 0x14086cd3d
0086BD6B  8B 4E 10                        mov ecx, dword ptr [rsi + 0x10]
0086BD6E  0B 4E 14                        or ecx, dword ptr [rsi + 0x14]
0086BD71  89 4E 14                        mov dword ptr [rsi + 0x14], ecx
0086BD74  44 89 4E 10                     mov dword ptr [rsi + 0x10], r9d
0086BD78  8B 43 5C                        mov eax, dword ptr [rbx + 0x5c]
0086BD7B  0F BA E8 18                     bts eax, 0x18
0086BD7F  23 C1                           and eax, ecx
0086BD81  89 46 14                        mov dword ptr [rsi + 0x14], eax
0086BD84  41 0F 0D 4C 24 F8               prefetchw byte ptr [r12 - 8]
0086BD8A  49 8B 54 24 F8                  mov rdx, qword ptr [r12 - 8]
0086BD8F  F6 C2 0F                        test dl, 0xf
0086BD92  74 23                           je 0x14086bdb7
0086BD94  0F 1F 40 00                     nop dword ptr [rax]
0086BD98  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
0086BDA0  48 8D 4A FF                     lea rcx, [rdx - 1]
0086BDA4  48 8B C2                        mov rax, rdx
0086BDA7  F0 49 0F B1 4C 24 F8            lock cmpxchg qword ptr [r12 - 8], rcx
0086BDAE  74 07                           je 0x14086bdb7
0086BDB0  48 8B D0                        mov rdx, rax
0086BDB3  A8 0F                           test al, 0xf
0086BDB5  75 E9                           jne 0x14086bda0
0086BDB7  48 8B FA                        mov rdi, rdx
0086BDBA  83 E2 0F                        and edx, 0xf
0086BDBD  48 83 E7 F0                     and rdi, 0xfffffffffffffff0
0086BDC1  83 FA 01                        cmp edx, 1
0086BDC4  77 09                           ja 0x14086bdcf
0086BDC6  48 85 FF                        test rdi, rdi
0086BDC9  0F 85 79 12 00 00               jne 0x14086d048
0086BDCF  44 8B 46 14                     mov r8d, dword ptr [rsi + 0x14]
0086BDD3  48 8D 4E 20                     lea rcx, [rsi + 0x20]
0086BDD7  4C 8B CF                        mov r9, rdi
0086BDDA  48 8B D6                        mov rdx, rsi
0086BDDD  E8 9E A2 B3 FF                  call 0x1403a6080
0086BDE2  F7 D0                           not eax
0086BDE4  21 46 14                        and dword ptr [rsi + 0x14], eax
0086BDE7  48 85 FF                        test rdi, rdi
0086BDEA  74 28                           je 0x14086be14
0086BDEC  41 0F 0D 4C 24 F8               prefetchw byte ptr [r12 - 8]
0086BDF2  49 8B 44 24 F8                  mov rax, qword ptr [r12 - 8]
0086BDF7  48 8B C8                        mov rcx, rax
0086BDFA  48 33 CF                        xor rcx, rdi
0086BDFD  48 83 F9 0F                     cmp rcx, 0xf
0086BE01  0F 83 E9 11 00 00               jae 0x14086cff0
0086BE07  48 8D 48 01                     lea rcx, [rax + 1]
0086BE0B  F0 49 0F B1 4C 24 F8            lock cmpxchg qword ptr [r12 - 8], rcx
0086BE12  75 E3                           jne 0x14086bdf7
0086BE14  45 33 C9                        xor r9d, r9d
0086BE17  44 89 4D B4                     mov dword ptr [rbp - 0x4c], r9d
0086BE1B  8B 46 14                        mov eax, dword ptr [rsi + 0x14]
0086BE1E  4C 8B 55 98                     mov r10, qword ptr [rbp - 0x68]
0086BE22  89 45 84                        mov dword ptr [rbp - 0x7c], eax
0086BE25  49 8B C1                        mov rax, r9
0086BE28  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
0086BE2C  4D 85 ED                        test r13, r13
0086BE2F  74 08                           je 0x14086be39
0086BE31  49 8B 45 20                     mov rax, qword ptr [r13 + 0x20]
0086BE35  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
0086BE39  0F B6 9D 00 02 00 00            movzx ebx, byte ptr [rbp + 0x200]
0086BE40  48 8D 55 84                     lea rdx, [rbp - 0x7c]
0086BE44  8B 4D E8                        mov ecx, dword ptr [rbp - 0x18]
0086BE47  4D 8B CC                        mov r9, r12
0086BE4A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0086BE4F  4D 8B C2                        mov r8, r10
0086BE52  44 89 74 24 28                  mov dword ptr [rsp + 0x28], r14d
0086BE57  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
0086BE5B  E8 B0 1B 00 00                  call 0x14086da10
0086BE60  8B F8                           mov edi, eax
0086BE62  85 C0                           test eax, eax
0086BE64  0F 88 38 05 00 00               js 0x14086c3a2
0086BE6A  48 85 F6                        test rsi, rsi
0086BE6D  0F 84 39 08 00 00               je 0x14086c6ac
0086BE73  4D 85 ED                        test r13, r13
0086BE76  0F 85 6E 0E 00 00               jne 0x14086ccea
0086BE7C  48 8B 7D 18                     mov rdi, qword ptr [rbp + 0x18]
0086BE80  80 7E 0A 00                     cmp byte ptr [rsi + 0xa], 0
0086BE84  74 04                           je 0x14086be8a
0086BE86  41 83 CE 04                     or r14d, 4
0086BE8A  8B 5D 84                        mov ebx, dword ptr [rbp - 0x7c]
0086BE8D  4D 8D 7C 24 D0                  lea r15, [r12 - 0x30]
0086BE92  49 8B C7                        mov rax, r15
0086BE95  48 C1 E8 08                     shr rax, 8
0086BE99  0F B6 C8                        movzx ecx, al
0086BE9C  41 0F B6 47 18                  movzx eax, byte ptr [r15 + 0x18]
0086BEA1  48 33 C8                        xor rcx, rax
0086BEA4  0F B6 05 A1 AF 75 00            movzx eax, byte ptr [rip + 0x75afa1]
0086BEAB  48 33 C8                        xor rcx, rax
0086BEAE  48 8D 05 4B 41 79 FF            lea rax, [rip - 0x86beb5]
0086BEB5  48 8B 84 C8 00 78 FC 00         mov rax, qword ptr [rax + rcx*8 + 0xfc7800]
0086BEBD  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
0086BEC1  8B 40 5C                        mov eax, dword ptr [rax + 0x5c]
0086BEC4  0F BA E8 18                     bts eax, 0x18
0086BEC8  23 D8                           and ebx, eax
0086BECA  89 5D 84                        mov dword ptr [rbp - 0x7c], ebx
0086BECD  48 85 F6                        test rsi, rsi
0086BED0  0F 84 09 07 00 00               je 0x14086c5df
0086BED6  41 0F 0D 4F 28                  prefetchw byte ptr [r15 + 0x28]
0086BEDB  49 8B 57 28                     mov rdx, qword ptr [r15 + 0x28]
0086BEDF  F6 C2 0F                        test dl, 0xf
0086BEE2  74 16                           je 0x14086befa
0086BEE4  48 8D 4A FF                     lea rcx, [rdx - 1]
0086BEE8  48 8B C2                        mov rax, rdx
0086BEEB  F0 49 0F B1 4F 28               lock cmpxchg qword ptr [r15 + 0x28], rcx
0086BEF1  74 07                           je 0x14086befa
0086BEF3  48 8B D0                        mov rdx, rax
0086BEF6  A8 0F                           test al, 0xf
0086BEF8  75 EA                           jne 0x14086bee4
0086BEFA  48 8B DA                        mov rbx, rdx
0086BEFD  83 E2 0F                        and edx, 0xf
0086BF00  48 83 E3 F0                     and rbx, 0xfffffffffffffff0
0086BF04  83 FA 01                        cmp edx, 1
0086BF07  77 09                           ja 0x14086bf12
0086BF09  48 85 DB                        test rbx, rbx
0086BF0C  0F 85 CB 12 00 00               jne 0x14086d1dd
0086BF12  44 8B 45 84                     mov r8d, dword ptr [rbp - 0x7c]
0086BF16  48 8D 4E 20                     lea rcx, [rsi + 0x20]
0086BF1A  4C 8B CB                        mov r9, rbx
0086BF1D  48 8B D6                        mov rdx, rsi
0086BF20  E8 5B A1 B3 FF                  call 0x1403a6080
0086BF25  8B F8                           mov edi, eax
0086BF27  48 85 DB                        test rbx, rbx
0086BF2A  74 25                           je 0x14086bf51
0086BF2C  41 0F 0D 4F 28                  prefetchw byte ptr [r15 + 0x28]
0086BF31  49 8B 47 28                     mov rax, qword ptr [r15 + 0x28]
0086BF35  48 8B C8                        mov rcx, rax
0086BF38  48 33 CB                        xor rcx, rbx
0086BF3B  48 83 F9 0F                     cmp rcx, 0xf
0086BF3F  0F 83 73 12 00 00               jae 0x14086d1b8
0086BF45  48 8D 48 01                     lea rcx, [rax + 1]
0086BF49  F0 49 0F B1 4F 28               lock cmpxchg qword ptr [r15 + 0x28], rcx
0086BF4F  75 E4                           jne 0x14086bf35
0086BF51  8B 5D 84                        mov ebx, dword ptr [rbp - 0x7c]
0086BF54  F7 D7                           not edi
0086BF56  48 8B 46 48                     mov rax, qword ptr [rsi + 0x48]
0086BF5A  23 DF                           and ebx, edi
0086BF5C  48 8B 7D 18                     mov rdi, qword ptr [rbp + 0x18]
0086BF60  89 5D 84                        mov dword ptr [rbp - 0x7c], ebx
0086BF63  89 5E 14                        mov dword ptr [rsi + 0x14], ebx
0086BF66  8B 40 1C                        mov eax, dword ptr [rax + 0x1c]
0086BF69  89 45 40                        mov dword ptr [rbp + 0x40], eax
0086BF6C  44 8B AD F0 01 00 00            mov r13d, dword ptr [rbp + 0x1f0]
0086BF73  89 45 F8                        mov dword ptr [rbp - 8], eax
0086BF76  45 85 ED                        test r13d, r13d
0086BF79  74 14                           je 0x14086bf8f
0086BF7B  41 B8 44 66 6C 74               mov r8d, 0x746c6644
0086BF81  41 8B D5                        mov edx, r13d
0086BF84  49 8B CC                        mov rcx, r12
0086BF87  E8 24 3E BB FF                  call 0x14041fdb0
0086BF8C  8B 5D 84                        mov ebx, dword ptr [rbp - 0x7c]
0086BF8F  48 85 FF                        test rdi, rdi
0086BF92  74 0B                           je 0x14086bf9f
0086BF94  48 8B CF                        mov rcx, rdi
0086BF97  E8 B4 D3 A8 FF                  call 0x1402f9350
0086BF9C  8B 5D 84                        mov ebx, dword ptr [rbp - 0x7c]
0086BF9F  48 83 7D A8 00                  cmp qword ptr [rbp - 0x58], 0
0086BFA4  48 8B 7D B8                     mov rdi, qword ptr [rbp - 0x48]
0086BFA8  0F 85 23 0E 00 00               jne 0x14086cdd1
0086BFAE  48 8D 45 D0                     lea rax, [rbp - 0x30]
0086BFB2  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
0086BFB6  48 8D 45 D0                     lea rax, [rbp - 0x30]
0086BFBA  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0086BFBE  F6 47 42 40                     test byte ptr [rdi + 0x42], 0x40
0086BFC2  0F 85 88 07 00 00               jne 0x14086c750
0086BFC8  41 8B CE                        mov ecx, r14d
0086BFCB  45 33 C9                        xor r9d, r9d
0086BFCE  83 E1 07                        and ecx, 7
0086BFD1  4C 89 4D 58                     mov qword ptr [rbp + 0x58], r9
0086BFD5  48 C1 E1 11                     shl rcx, 0x11
0086BFD9  81 E3 FF FF FF 01               and ebx, 0x1ffffff
0086BFDF  49 8B C7                        mov rax, r15
0086BFE2  89 5D 58                        mov dword ptr [rbp + 0x58], ebx
0086BFE5  48 C1 E0 10                     shl rax, 0x10
0086BFE9  48 25 FF FF F1 FF               and rax, 0xfffffffffff1ffff
0086BFEF  48 0B C8                        or rcx, rax
0086BFF2  48 89 4D 50                     mov qword ptr [rbp + 0x50], rcx
0086BFF6  41 F6 C6 08                     test r14b, 8
0086BFFA  74 04                           je 0x14086c000
0086BFFC  0F BA EB 19                     bts ebx, 0x19
0086C000  65 4C 8B 24 25 88 01 00 00      mov r12, qword ptr gs:[0x188]
0086C009  48 83 C9 01                     or rcx, 1
0086C00D  4C 8B 45 90                     mov r8, qword ptr [rbp - 0x70]
0086C011  4D 8B F1                        mov r14, r9
0086C014  89 5D 58                        mov dword ptr [rbp + 0x58], ebx
0086C017  48 89 4D 50                     mov qword ptr [rbp + 0x50], rcx
0086C01B  66 41 FF 8C 24 E4 01 00 00      dec word ptr [r12 + 0x1e4]
0086C024  90                              nop
0086C025  41 0F B6 40 2C                  movzx eax, byte ptr [r8 + 0x2c]
0086C02A  A8 04                           test al, 4
0086C02C  0F 85 2D 01 00 00               jne 0x14086c15f
0086C032  A8 01                           test al, 1
0086C034  0F 85 77 0C 00 00               jne 0x14086ccb1
0086C03A  65 8B 14 25 A4 01 00 00         mov edx, dword ptr gs:[0x1a4]
0086C042  8B 0D D0 DA 76 00               mov ecx, dword ptr [rip + 0x76dad0]
0086C048  8B DA                           mov ebx, edx
0086C04A  89 5D 00                        mov dword ptr [rbp], ebx
0086C04D  89 55 F0                        mov dword ptr [rbp - 0x10], edx
0086C050  89 4D 08                        mov dword ptr [rbp + 8], ecx
0086C053  41 8B 00                        mov eax, dword ptr [r8]
0086C056  89 45 A8                        mov dword ptr [rbp - 0x58], eax
0086C059  41 8B C1                        mov eax, r9d
0086C05C  89 45 C8                        mov dword ptr [rbp - 0x38], eax
0086C05F  3B C1                           cmp eax, ecx
0086C061  0F 83 43 10 00 00               jae 0x14086d0aa
0086C067  48 FF C3                        inc rbx
0086C06A  48 C1 E3 06                     shl rbx, 6
0086C06E  49 03 D8                        add rbx, r8
0086C071  4C 39 73 08                     cmp qword ptr [rbx + 8], r14
0086C075  0F 84 48 19 00 00               je 0x14086d9c3
0086C07B  45 33 C0                        xor r8d, r8d
0086C07E  33 D2                           xor edx, edx
0086C080  48 8B CB                        mov rcx, rbx
0086C083  E8 A8 41 9A FF                  call 0x140210230
0086C088  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
0086C08E  48 8B F8                        mov rdi, rax
0086C091  73 0E                           jae 0x14086c0a1
0086C093  4C 8B C3                        mov r8, rbx
0086C096  48 8B D0                        mov rdx, rax
0086C099  48 8B CB                        mov rcx, rbx
0086C09C  E8 EF 3B 9A FF                  call 0x14020fc90
0086C0A1  48 85 FF                        test rdi, rdi
0086C0A4  74 04                           je 0x14086c0aa
0086C0A6  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
0086C0AA  48 8B 7B 08                     mov rdi, qword ptr [rbx + 8]
0086C0AE  48 85 FF                        test rdi, rdi
0086C0B1  74 1F                           je 0x14086c0d2
0086C0B3  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
0086C0B7  48 89 43 08                     mov qword ptr [rbx + 8], rax
0086C0BB  48 85 C0                        test rax, rax
0086C0BE  75 04                           jne 0x14086c0c4
0086C0C0  48 89 43 10                     mov qword ptr [rbx + 0x10], rax
0086C0C4  FF 43 18                        inc dword ptr [rbx + 0x18]
0086C0C7  8B 43 18                        mov eax, dword ptr [rbx + 0x18]
0086C0CA  3B 43 1C                        cmp eax, dword ptr [rbx + 0x1c]
0086C0CD  7E 03                           jle 0x14086c0d2
0086C0CF  89 43 1C                        mov dword ptr [rbx + 0x1c], eax
0086C0D2  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
0086C0D9  F0 48 0F C1 03                  lock xadd qword ptr [rbx], rax
0086C0DE  24 06                           and al, 6
0086C0E0  3C 02                           cmp al, 2
0086C0E2  0F 84 DC 0C 00 00               je 0x14086cdc4
0086C0E8  48 8B CB                        mov rcx, rbx
0086C0EB  E8 10 55 A7 FF                  call 0x1402e1600
0086C0F0  48 85 FF                        test rdi, rdi
0086C0F3  0F 84 BD 18 00 00               je 0x14086d9b6
0086C0F9  48 8B C7                        mov rax, rdi
0086C0FC  48 8B CF                        mov rcx, rdi
0086C0FF  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
0086C105  48 2B C8                        sub rcx, rax
0086C108  48 C1 F9 04                     sar rcx, 4
0086C10C  83 7D F8 00                     cmp dword ptr [rbp - 8], 0
0086C110  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0086C114  4C 8D 34 88                     lea r14, [rax + rcx*4]
0086C118  41 8B C6                        mov eax, r14d
0086C11B  41 8B CE                        mov ecx, r14d
0086C11E  0F 85 30 03 00 00               jne 0x14086c454
0086C124  83 BD 10 02 00 00 00            cmp dword ptr [rbp + 0x210], 0
0086C12B  0F 85 23 03 00 00               jne 0x14086c454
0086C131  4C 8B 55 90                     mov r10, qword ptr [rbp - 0x70]
0086C135  49 83 7A 60 00                  cmp qword ptr [r10 + 0x60], 0
0086C13A  74 14                           je 0x14086c150
0086C13C  41 B9 01 00 00 00               mov r9d, 1
0086C142  4D 8B C6                        mov r8, r14
0086C145  49 8B D4                        mov rdx, r12
0086C148  49 8B CA                        mov rcx, r10
0086C14B  E8 24 F0 FF FF                  call 0x14086b174
0086C150  48 8B 45 58                     mov rax, qword ptr [rbp + 0x58]
0086C154  48 89 47 08                     mov qword ptr [rdi + 8], rax
0086C158  48 8B 45 50                     mov rax, qword ptr [rbp + 0x50]
0086C15C  48 89 07                        mov qword ptr [rdi], rax
0086C15F  49 8B CC                        mov rcx, r12
0086C162  E8 89 2E 9F FF                  call 0x14025eff0
0086C167  4D 85 F6                        test r14, r14
0086C16A  0F 84 88 0C 00 00               je 0x14086cdf8
0086C170  48 8B 7D A0                     mov rdi, qword ptr [rbp - 0x60]
0086C174  45 85 ED                        test r13d, r13d
0086C177  74 0D                           je 0x14086c186
0086C179  83 3D 90 8E 75 00 00            cmp dword ptr [rip + 0x758e90], 0
0086C180  0F 85 D7 0E 00 00               jne 0x14086d05d
0086C186  48 85 F6                        test rsi, rsi
0086C189  0F 84 17 01 00 00               je 0x14086c2a6
0086C18F  41 0F B6 47 1A                  movzx eax, byte ptr [r15 + 0x1a]
0086C194  33 D2                           xor edx, edx
0086C196  48 89 55 20                     mov qword ptr [rbp + 0x20], rdx
0086C19A  8B DA                           mov ebx, edx
0086C19C  A8 20                           test al, 0x20
0086C19E  74 1E                           je 0x14086c1be
0086C1A0  83 E0 3F                        and eax, 0x3f
0086C1A3  48 8D 0D 56 3E 79 FF            lea rcx, [rip - 0x86c1aa]
0086C1AA  4D 8B E7                        mov r12, r15
0086C1AD  0F B6 84 08 80 FF F0 00         movzx eax, byte ptr [rax + rcx + 0xf0ff80]
0086C1B5  4C 2B E0                        sub r12, rax
0086C1B8  0F 85 B8 0C 00 00               jne 0x14086ce76
0086C1BE  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0086C1C2  48 85 C0                        test rax, rax
0086C1C5  48 0F 45 D8                     cmovne rbx, rax
0086C1C9  4C 8B 7E 48                     mov r15, qword ptr [rsi + 0x48]
0086C1CD  40 32 FF                        xor dil, dil
0086C1D0  48 85 DB                        test rbx, rbx
0086C1D3  4C 89 75 38                     mov qword ptr [rbp + 0x38], r14
0086C1D7  4C 8B E3                        mov r12, rbx
0086C1DA  48 89 55 10                     mov qword ptr [rbp + 0x10], rdx
0086C1DE  48 8B DA                        mov rbx, rdx
0086C1E1  75 0D                           jne 0x14086c1f0
0086C1E3  4D 8B 67 38                     mov r12, qword ptr [r15 + 0x38]
0086C1E7  4D 85 E4                        test r12, r12
0086C1EA  75 04                           jne 0x14086c1f0
0086C1EC  4C 8B 66 40                     mov r12, qword ptr [rsi + 0x40]
0086C1F0  80 7E 09 00                     cmp byte ptr [rsi + 9], 0
0086C1F4  0F 85 CE 11 00 00               jne 0x14086d3c8
0086C1FA  41 80 BF D8 00 00 00 00         cmp byte ptr [r15 + 0xd8], 0
0086C202  0F 85 37 10 00 00               jne 0x14086d23f
0086C208  8B 5D E8                        mov ebx, dword ptr [rbp - 0x18]
0086C20B  40 88 7E 0A                     mov byte ptr [rsi + 0xa], dil
0086C20F  85 DB                           test ebx, ebx
0086C211  75 61                           jne 0x14086c274
0086C213  48 8B 46 48                     mov rax, qword ptr [rsi + 0x48]
0086C217  48 8B 10                        mov rdx, qword ptr [rax]
0086C21A  48 85 D2                        test rdx, rdx
0086C21D  74 55                           je 0x14086c274
0086C21F  39 1A                           cmp dword ptr [rdx], ebx
0086C221  76 51                           jbe 0x14086c274
0086C223  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086C22C  38 98 32 02 00 00               cmp byte ptr [rax + 0x232], bl
0086C232  74 40                           je 0x14086c274
0086C234  8B 46 14                        mov eax, dword ptr [rsi + 0x14]
0086C237  48 8D 0D 6A 51 79 FF            lea rcx, [rip - 0x86ae96]
0086C23E  C6 44 24 48 01                  mov byte ptr [rsp + 0x48], 1
0086C243  4D 8B CE                        mov r9, r14
0086C246  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0086C24B  45 33 C0                        xor r8d, r8d
0086C24E  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0086C252  33 D2                           xor edx, edx
0086C254  48 8B 46 38                     mov rax, qword ptr [rsi + 0x38]
0086C258  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0086C25D  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
0086C261  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0086C266  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
0086C26A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0086C26F  E8 7C 21 00 00                  call 0x14086e3f0
0086C274  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
0086C278  48 85 C9                        test rcx, rcx
0086C27B  74 07                           je 0x14086c284
0086C27D  33 D2                           xor edx, edx
0086C27F  E8 EC 65 31 00                  call 0x140b82870
0086C284  85 DB                           test ebx, ebx
0086C286  75 1E                           jne 0x14086c2a6
0086C288  48 8B 45 B8                     mov rax, qword ptr [rbp - 0x48]
0086C28C  48 3B 05 2D A8 75 00            cmp rax, qword ptr [rip + 0x75a82d]
0086C293  0F 85 01 04 00 00               jne 0x14086c69a
0086C299  48 8B 5E 20                     mov rbx, qword ptr [rsi + 0x20]
0086C29D  48 85 DB                        test rbx, rbx
0086C2A0  0F 85 0F 04 00 00               jne 0x14086c6b5
0086C2A6  48 8B 75 A0                     mov rsi, qword ptr [rbp - 0x60]
0086C2AA  45 85 ED                        test r13d, r13d
0086C2AD  0F 85 CF 03 00 00               jne 0x14086c682
0086C2B3  F6 5D 82                        neg byte ptr [rbp - 0x7e]
0086C2B6  0F B6 45 83                     movzx eax, byte ptr [rbp - 0x7d]
0086C2BA  1B FF                           sbb edi, edi
0086C2BC  81 E7 00 00 00 40               and edi, 0x40000000
0086C2C2  84 C0                           test al, al
0086C2C4  74 07                           je 0x14086c2cd
0086C2C6  49 81 CE 00 00 00 80            or r14, 0xffffffff80000000
0086C2CD  4C 8B BD A0 00 00 00            mov r15, qword ptr [rbp + 0xa0]
0086C2D4  4D 89 37                        mov qword ptr [r15], r14
0086C2D7  4C 8B 45 D0                     mov r8, qword ptr [rbp - 0x30]
0086C2DB  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0086C2DF  4C 3B C1                        cmp r8, rcx
0086C2E2  0F 84 AC 00 00 00               je 0x14086c394
0086C2E8  48 8B 5D A0                     mov rbx, qword ptr [rbp - 0x60]
0086C2EC  48 8D 4D 60                     lea rcx, [rbp + 0x60]
0086C2F0  0F B6 C0                        movzx eax, al
0086C2F3  45 33 C9                        xor r9d, r9d
0086C2F6  48 89 8D 10 01 00 00            mov qword ptr [rbp + 0x110], rcx
0086C2FD  41 8B C9                        mov ecx, r9d
0086C300  83 E1 FE                        and ecx, 0xfffffffe
0086C303  44 89 8D 0C 01 00 00            mov dword ptr [rbp + 0x10c], r9d
0086C30A  0B C8                           or ecx, eax
0086C30C  C7 85 E8 00 00 00 01 00 00 00   mov dword ptr [rbp + 0xe8], 1
0086C316  89 8D EC 00 00 00               mov dword ptr [rbp + 0xec], ecx
0086C31C  48 8D 43 D0                     lea rax, [rbx - 0x30]
0086C320  48 C1 E8 08                     shr rax, 8
0086C324  0F B6 C8                        movzx ecx, al
0086C327  0F B6 43 E8                     movzx eax, byte ptr [rbx - 0x18]
0086C32B  48 33 C8                        xor rcx, rax
0086C32E  48 89 9D F0 00 00 00            mov qword ptr [rbp + 0xf0], rbx
0086C335  0F B6 05 10 AB 75 00            movzx eax, byte ptr [rip + 0x75ab10]
0086C33C  48 33 C8                        xor rcx, rax
0086C33F  4C 89 8D 00 01 00 00            mov qword ptr [rbp + 0x100], r9
0086C346  48 8D 05 B3 3C 79 FF            lea rax, [rip - 0x86c34d]
0086C34D  89 BD 08 01 00 00               mov dword ptr [rbp + 0x108], edi
0086C353  48 8B 84 C8 00 78 FC 00         mov rax, qword ptr [rax + rcx*8 + 0xfc7800]
0086C35B  48 89 85 F8 00 00 00            mov qword ptr [rbp + 0xf8], rax
0086C362  8B 45 84                        mov eax, dword ptr [rbp - 0x7c]
0086C365  89 45 60                        mov dword ptr [rbp + 0x60], eax
0086C368  48 8D 45 D0                     lea rax, [rbp - 0x30]
0086C36C  4C 3B C0                        cmp r8, rax
0086C36F  75 63                           jne 0x14086c3d4
0086C371  48 8B 8D F0 00 00 00            mov rcx, qword ptr [rbp + 0xf0]
0086C378  BA 4F 62 43 62                  mov edx, 0x6243624f
0086C37D  E8 5E B5 A8 FF                  call 0x1402f78e0
0086C382  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086C38B  E8 60 2C 9F FF                  call 0x14025eff0
0086C390  48 8B 75 A0                     mov rsi, qword ptr [rbp - 0x60]
0086C394  8B 05 76 A7 75 00               mov eax, dword ptr [rip + 0x75a776]
0086C39A  A8 40                           test al, 0x40
0086C39C  0F 85 2D 0C 00 00               jne 0x14086cfcf
0086C3A2  48 8B 5D 98                     mov rbx, qword ptr [rbp - 0x68]
0086C3A6  80 7D 88 00                     cmp byte ptr [rbp - 0x78], 0
0086C3AA  74 20                           je 0x14086c3cc
0086C3AC  48 8D 8B E8 01 00 00            lea rcx, [rbx + 0x1e8]
0086C3B3  0F 0D 09                        prefetchw byte ptr [rcx]
0086C3B6  48 8B 01                        mov rax, qword ptr [rcx]
0086C3B9  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0086C3BD  48 8D 50 FE                     lea rdx, [rax - 2]
0086C3C1  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
0086C3C6  0F 85 ED 08 00 00               jne 0x14086ccb9
0086C3CC  8B C7                           mov eax, edi
0086C3CE  E9 0F 16 00 00                  jmp 0x14086d9e2
0086C3D3  CC                              int3
0086C3D4  48 8B 75 D8                     mov rsi, qword ptr [rbp - 0x28]
0086C3D8  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0086C3DC  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0086C3E0  48 39 0E                        cmp qword ptr [rsi], rcx
0086C3E3  0F 85 10 07 00 00               jne 0x14086caf9
0086C3E9  48 39 30                        cmp qword ptr [rax], rsi
0086C3EC  0F 85 07 07 00 00               jne 0x14086caf9
0086C3F2  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
0086C3F6  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0086C3FA  48 89 08                        mov qword ptr [rax], rcx
0086C3FD  48 8D 95 E8 00 00 00            lea rdx, [rbp + 0xe8]
0086C404  48 8B 5E 10                     mov rbx, qword ptr [rsi + 0x10]
0086C408  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
0086C40C  48 89 85 00 01 00 00            mov qword ptr [rbp + 0x100], rax
0086C413  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
0086C417  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
0086C41B  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
0086C41F  E8 AC E6 E4 FF                  call 0x1406baad0
0086C424  48 8D 4B 38                     lea rcx, [rbx + 0x38]
0086C428  0F 0D 09                        prefetchw byte ptr [rcx]
0086C42B  48 8B 01                        mov rax, qword ptr [rcx]
0086C42E  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0086C432  48 8D 50 FE                     lea rdx, [rax - 2]
0086C436  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
0086C43B  0F 85 F2 09 00 00               jne 0x14086ce33
0086C441  33 D2                           xor edx, edx
0086C443  48 8B CE                        mov rcx, rsi
0086C446  E8 25 64 31 00                  call 0x140b82870
0086C44B  4C 8B 45 D0                     mov r8, qword ptr [rbp - 0x30]
0086C44F  E9 14 FF FF FF                  jmp 0x14086c368
0086C454  4C 8B 55 90                     mov r10, qword ptr [rbp - 0x70]
0086C458  81 E1 03 FC FF FF               and ecx, 0xfffffc03
0086C45E  4C 89 75 F8                     mov qword ptr [rbp - 8], r14
0086C462  89 4D F8                        mov dword ptr [rbp - 8], ecx
0086C465  49 8B CA                        mov rcx, r10
0086C468  48 8B 55 F8                     mov rdx, qword ptr [rbp - 8]
0086C46C  C1 E8 02                        shr eax, 2
0086C46F  0F B6 C0                        movzx eax, al
0086C472  89 45 A8                        mov dword ptr [rbp - 0x58], eax
0086C475  E8 36 D9 FF FF                  call 0x140869db0
0086C47A  48 8B D8                        mov rbx, rax
0086C47D  48 85 C0                        test rax, rax
0086C480  0F 84 22 07 00 00               je 0x14086cba8
0086C486  48 8B 08                        mov rcx, qword ptr [rax]
0086C489  48 85 C9                        test rcx, rcx
0086C48C  0F 84 C9 06 00 00               je 0x14086cb5b
0086C492  8B 55 A8                        mov edx, dword ptr [rbp - 0x58]
0086C495  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
0086C499  48 89 04 D1                     mov qword ptr [rcx + rdx*8], rax
0086C49D  E9 93 FC FF FF                  jmp 0x14086c135
0086C4A2  4C 8B 15 07 A6 75 00            mov r10, qword ptr [rip + 0x75a607]
0086C4A9  48 8B 0D 08 31 6A 00            mov rcx, qword ptr [rip + 0x6a3108]
0086C4B0  4C 89 55 98                     mov qword ptr [rbp - 0x68], r10
0086C4B4  E9 7B F5 FF FF                  jmp 0x14086ba34
0086C4B9  8B 05 CD EE 59 00               mov eax, dword ptr [rip + 0x59eecd]
0086C4BF  B9 00 01 00 00                  mov ecx, 0x100
0086C4C4  8B D0                           mov edx, eax
0086C4C6  C7 45 C0 BF 01 00 00            mov dword ptr [rbp - 0x40], 0x1bf
0086C4CD  41 B8 4F 62 53 71               mov r8d, 0x7153624f
0086C4D3  89 45 B0                        mov dword ptr [rbp - 0x50], eax
0086C4D6  E8 15 5C 31 00                  call 0x140b820f0
0086C4DB  48 8B D8                        mov rbx, rax
0086C4DE  48 85 C0                        test rax, rax
0086C4E1  0F 84 EC 0C 00 00               je 0x14086d1d3
0086C4E7  49 8B 85 98 00 00 00            mov rax, qword ptr [r13 + 0x98]
0086C4EE  4D 8D 44 24 F8                  lea r8, [r12 - 8]
0086C4F3  41 8B 4D 64                     mov ecx, dword ptr [r13 + 0x64]
0086C4F7  49 8D 55 4C                     lea rdx, [r13 + 0x4c]
0086C4FB  44 88 7C 24 40                  mov byte ptr [rsp + 0x40], r15b
0086C500  4C 8D 0D B9 47 00 00            lea r9, [rip + 0x47b9]
0086C507  48 89 54 24 38                  mov qword ptr [rsp + 0x38], rdx
0086C50C  BA 01 00 00 00                  mov edx, 1
0086C511  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0086C515  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
0086C51A  4C 89 45 B8                     mov qword ptr [rbp - 0x48], r8
0086C51E  4C 8D 45 C0                     lea r8, [rbp - 0x40]
0086C522  C6 45 80 01                     mov byte ptr [rbp - 0x80], 1
0086C526  49 3B C1                        cmp rax, r9
0086C529  0F 85 F0 0A 00 00               jne 0x14086d01f
0086C52F  48 8D 45 B0                     lea rax, [rbp - 0x50]
0086C533  4C 8B CB                        mov r9, rbx
0086C536  49 8B CC                        mov rcx, r12
0086C539  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0086C53E  E8 7D 47 00 00                  call 0x140870cc0
0086C543  8B F8                           mov edi, eax
0086C545  3D 23 00 00 C0                  cmp eax, 0xc0000023
0086C54A  0F 84 D5 12 00 00               je 0x14086d825
0086C550  85 FF                           test edi, edi
0086C552  0F 88 10 0A 00 00               js 0x14086cf68
0086C558  45 33 C9                        xor r9d, r9d
0086C55B  E9 C1 F5 FF FF                  jmp 0x14086bb21
0086C560  4C 89 4D 90                     mov qword ptr [rbp - 0x70], r9
0086C564  49 8D BA E8 01 00 00            lea rdi, [r10 + 0x1e8]
0086C56B  0F 0D 0F                        prefetchw byte ptr [rdi]
0086C56E  48 8B 07                        mov rax, qword ptr [rdi]
0086C571  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0086C575  48 8D 48 02                     lea rcx, [rax + 2]
0086C579  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
0086C57E  75 37                           jne 0x14086c5b7
0086C580  49 8B 8A 00 03 00 00            mov rcx, qword ptr [r10 + 0x300]
0086C587  48 89 4D 90                     mov qword ptr [rbp - 0x70], rcx
0086C58B  48 85 C9                        test rcx, rcx
0086C58E  75 40                           jne 0x14086c5d0
0086C590  0F 0D 0F                        prefetchw byte ptr [rdi]
0086C593  48 8B 07                        mov rax, qword ptr [rdi]
0086C596  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0086C59A  48 8D 50 FE                     lea rdx, [rax - 2]
0086C59E  F0 48 0F B1 17                  lock cmpxchg qword ptr [rdi], rdx
0086C5A3  74 26                           je 0x14086c5cb
0086C5A5  48 8B CF                        mov rcx, rdi
0086C5A8  E8 03 D9 AD FF                  call 0x140349eb0
0086C5AD  BF 0A 01 00 C0                  mov edi, 0xc000010a
0086C5B2  E9 15 FE FF FF                  jmp 0x14086c3cc
0086C5B7  48 8B CF                        mov rcx, rdi
0086C5BA  E8 91 FA AD FF                  call 0x14034c050
0086C5BF  4C 8B 55 98                     mov r10, qword ptr [rbp - 0x68]
0086C5C3  84 C0                           test al, al
0086C5C5  75 B9                           jne 0x14086c580
0086C5C7  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0086C5CB  48 85 C9                        test rcx, rcx
0086C5CE  74 DD                           je 0x14086c5ad
0086C5D0  8B 55 E8                        mov edx, dword ptr [rbp - 0x18]
0086C5D3  45 33 C9                        xor r9d, r9d
0086C5D6  C6 45 88 01                     mov byte ptr [rbp - 0x78], 1
0086C5DA  E9 59 F4 FF FF                  jmp 0x14086ba38
0086C5DF  8B 45 40                        mov eax, dword ptr [rbp + 0x40]
0086C5E2  E9 85 F9 FF FF                  jmp 0x14086bf6c
0086C5E7  83 7E 18 00                     cmp dword ptr [rsi + 0x18], 0
0086C5EB  0F 85 65 F4 FF FF               jne 0x14086ba56
0086C5F1  0F BA E3 19                     bt ebx, 0x19
0086C5F5  73 08                           jae 0x14086c5ff
0086C5F7  0F BA F3 19                     btr ebx, 0x19
0086C5FB  0F BA EB 1C                     bts ebx, 0x1c
0086C5FF  4C 8D 05 FA 39 79 FF            lea r8, [rip - 0x86c606]
0086C606  F7 C3 00 00 00 F0               test ebx, 0xf0000000
0086C60C  74 4F                           je 0x14086c65d
0086C60E  49 8D 44 24 D0                  lea rax, [r12 - 0x30]
0086C613  48 C1 E8 08                     shr rax, 8
0086C617  0F B6 C8                        movzx ecx, al
0086C61A  41 0F B6 44 24 E8               movzx eax, byte ptr [r12 - 0x18]
0086C620  48 33 C8                        xor rcx, rax
0086C623  0F B6 05 22 A8 75 00            movzx eax, byte ptr [rip + 0x75a822]
0086C62A  48 33 C8                        xor rcx, rax
0086C62D  49 8B 84 C8 00 78 FC 00         mov rax, qword ptr [r8 + rcx*8 + 0xfc7800]
0086C635  85 DB                           test ebx, ebx
0086C637  79 03                           jns 0x14086c63c
0086C639  0B 58 4C                        or ebx, dword ptr [rax + 0x4c]
0086C63C  0F BA E3 1E                     bt ebx, 0x1e
0086C640  73 03                           jae 0x14086c645
0086C642  0B 58 50                        or ebx, dword ptr [rax + 0x50]
0086C645  0F BA E3 1D                     bt ebx, 0x1d
0086C649  73 03                           jae 0x14086c64e
0086C64B  0B 58 54                        or ebx, dword ptr [rax + 0x54]
0086C64E  0F BA E3 1C                     bt ebx, 0x1c
0086C652  73 03                           jae 0x14086c657
0086C654  0B 58 58                        or ebx, dword ptr [rax + 0x58]
0086C657  81 E3 FF FF FF 0F               and ebx, 0xfffffff
0086C65D  89 5D 84                        mov dword ptr [rbp - 0x7c], ebx
0086C660  E9 C0 F7 FF FF                  jmp 0x14086be25
0086C665  8B 46 10                        mov eax, dword ptr [rsi + 0x10]
0086C668  09 46 14                        or dword ptr [rsi + 0x14], eax
0086C66B  4C 8B 6D A8                     mov r13, qword ptr [rbp - 0x58]
0086C66F  44 89 4E 10                     mov dword ptr [rsi + 0x10], r9d
0086C673  89 7D B4                        mov dword ptr [rbp - 0x4c], edi
0086C676  E9 A0 F7 FF FF                  jmp 0x14086be1b
0086C67B  33 C0                           xor eax, eax
0086C67D  E9 73 F5 FF FF                  jmp 0x14086bbf5
0086C682  48 8B 85 B0 00 00 00            mov rax, qword ptr [rbp + 0xb0]
0086C689  48 85 C0                        test rax, rax
0086C68C  0F 84 21 FC FF FF               je 0x14086c2b3
0086C692  48 89 30                        mov qword ptr [rax], rsi
0086C695  E9 19 FC FF FF                  jmp 0x14086c2b3
0086C69A  48 3B 05 3F A4 75 00            cmp rax, qword ptr [rip + 0x75a43f]
0086C6A1  0F 84 F2 FB FF FF               je 0x14086c299
0086C6A7  E9 FA FB FF FF                  jmp 0x14086c2a6
0086C6AC  48 8B 7D 18                     mov rdi, qword ptr [rbp + 0x18]
0086C6B0  E9 D5 F7 FF FF                  jmp 0x14086be8a
0086C6B5  48 8B 7E 30                     mov rdi, qword ptr [rsi + 0x30]
0086C6B9  B2 01                           mov dl, 1
0086C6BB  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086C6C4  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0086C6CB  90                              nop
0086C6CC  48 3B FB                        cmp rdi, rbx
0086C6CF  0F 83 63 04 00 00               jae 0x14086cb38
0086C6D5  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
0086C6D9  E8 E2 54 9A FF                  call 0x140211bc0
0086C6DE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086C6E7  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0086C6EE  90                              nop
0086C6EF  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
0086C6F3  B2 01                           mov dl, 1
0086C6F5  E8 C6 54 9A FF                  call 0x140211bc0
0086C6FA  F7 83 C8 00 00 00 00 40 00 00   test dword ptr [rbx + 0xc8], 0x4000
0086C704  0F 85 D5 07 00 00               jne 0x14086cedf
0086C70A  48 8B 75 A0                     mov rsi, qword ptr [rbp - 0x60]
0086C70E  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
0086C712  E8 F9 32 9F FF                  call 0x14025fa10
0086C717  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086C720  E8 CB 28 9F FF                  call 0x14025eff0
0086C725  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
0086C729  E8 E2 32 9F FF                  call 0x14025fa10
0086C72E  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086C737  E8 B4 28 9F FF                  call 0x14025eff0
0086C73C  E9 69 FB FF FF                  jmp 0x14086c2aa
0086C741  33 D2                           xor edx, edx
0086C743  48 8B CB                        mov rcx, rbx
0086C746  E8 25 61 31 00                  call 0x140b82870
0086C74B  E9 8E F5 FF FF                  jmp 0x14086bcde
0086C750  48 8D 87 C8 00 00 00            lea rax, [rdi + 0xc8]
0086C757  48 39 00                        cmp qword ptr [rax], rax
0086C75A  0F 84 68 F8 FF FF               je 0x14086bfc8
0086C760  0F 57 C0                        xorps xmm0, xmm0
0086C763  49 8D 44 24 D0                  lea rax, [r12 - 0x30]
0086C768  48 C1 E8 08                     shr rax, 8
0086C76C  0F B6 D0                        movzx edx, al
0086C76F  41 0F B6 44 24 E8               movzx eax, byte ptr [r12 - 0x18]
0086C775  48 33 D0                        xor rdx, rax
0086C778  0F B6 05 CD A6 75 00            movzx eax, byte ptr [rip + 0x75a6cd]
0086C77F  48 33 D0                        xor rdx, rax
0086C782  48 8D 05 77 38 79 FF            lea rax, [rip - 0x86c789]
0086C789  0F 11 85 B8 00 00 00            movups xmmword ptr [rbp + 0xb8], xmm0
0086C790  0F 11 85 C8 00 00 00            movups xmmword ptr [rbp + 0xc8], xmm0
0086C797  48 8B BC D0 00 78 FC 00         mov rdi, qword ptr [rax + rdx*8 + 0xfc7800]
0086C79F  33 D2                           xor edx, edx
0086C7A1  8B CA                           mov ecx, edx
0086C7A3  48 89 55 00                     mov qword ptr [rbp], rdx
0086C7A7  83 E1 FE                        and ecx, 0xfffffffe
0086C7AA  48 89 55 F0                     mov qword ptr [rbp - 0x10], rdx
0086C7AE  0F 11 85 D8 00 00 00            movups xmmword ptr [rbp + 0xd8], xmm0
0086C7B5  8B 47 60                        mov eax, dword ptr [rdi + 0x60]
0086C7B8  23 C3                           and eax, ebx
0086C7BA  4C 89 A5 80 00 00 00            mov qword ptr [rbp + 0x80], r12
0086C7C1  48 89 95 90 00 00 00            mov qword ptr [rbp + 0x90], rdx
0086C7C8  BA 4F 62 43 62                  mov edx, 0x6243624f
0086C7CD  89 45 08                        mov dword ptr [rbp + 8], eax
0086C7D0  48 8D 85 18 01 00 00            lea rax, [rbp + 0x118]
0086C7D7  48 89 85 98 00 00 00            mov qword ptr [rbp + 0x98], rax
0086C7DE  0F B6 45 83                     movzx eax, byte ptr [rbp - 0x7d]
0086C7E2  0B C8                           or ecx, eax
0086C7E4  C7 45 78 01 00 00 00            mov dword ptr [rbp + 0x78], 1
0086C7EB  89 4D 7C                        mov dword ptr [rbp + 0x7c], ecx
0086C7EE  48 8D 8F C8 00 00 00            lea rcx, [rdi + 0xc8]
0086C7F5  F3 0F 7F 85 20 01 00 00         movdqu xmmword ptr [rbp + 0x120], xmm0
0086C7FD  48 89 BD 88 00 00 00            mov qword ptr [rbp + 0x88], rdi
0086C804  89 9D 1C 01 00 00               mov dword ptr [rbp + 0x11c], ebx
0086C80A  89 9D 18 01 00 00               mov dword ptr [rbp + 0x118], ebx
0086C810  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086C819  48 89 4D C8                     mov qword ptr [rbp - 0x38], rcx
0086C81D  48 89 7D 30                     mov qword ptr [rbp + 0x30], rdi
0086C821  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0086C828  90                              nop
0086C829  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
0086C830  E8 DB 3E 9A FF                  call 0x140210710
0086C835  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086C83E  48 8D 8F B8 00 00 00            lea rcx, [rdi + 0xb8]
0086C845  45 33 C0                        xor r8d, r8d
0086C848  48 89 4D A8                     mov qword ptr [rbp - 0x58], rcx
0086C84C  33 D2                           xor edx, edx
0086C84E  66 FF 88 E6 01 00 00            dec word ptr [rax + 0x1e6]
0086C855  90                              nop
0086C856  E8 D5 39 9A FF                  call 0x140210230
0086C85B  4C 8B 55 A8                     mov r10, qword ptr [rbp - 0x58]
0086C85F  48 8B F8                        mov rdi, rax
0086C862  33 C0                           xor eax, eax
0086C864  B9 11 00 00 00                  mov ecx, 0x11
0086C869  F0 49 0F B1 0A                  lock cmpxchg qword ptr [r10], rcx
0086C86E  74 14                           je 0x14086c884
0086C870  4D 8B CA                        mov r9, r10
0086C873  4C 8B C7                        mov r8, rdi
0086C876  33 D2                           xor edx, edx
0086C878  49 8B CA                        mov rcx, r10
0086C87B  E8 CC 3B 9A FF                  call 0x14021044c
0086C880  4C 8B 55 A8                     mov r10, qword ptr [rbp - 0x58]
0086C884  48 85 FF                        test rdi, rdi
0086C887  74 04                           je 0x14086c88d
0086C889  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
0086C88D  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
0086C891  48 8B 38                        mov rdi, qword ptr [rax]
0086C894  48 3B F8                        cmp rdi, rax
0086C897  0F 84 60 01 00 00               je 0x14086c9fd
0086C89D  8B 47 14                        mov eax, dword ptr [rdi + 0x14]
0086C8A0  A8 01                           test al, 1
0086C8A2  0F 84 45 01 00 00               je 0x14086c9ed
0086C8A8  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
0086C8AB  85 45 78                        test dword ptr [rbp + 0x78], eax
0086C8AE  0F 84 39 01 00 00               je 0x14086c9ed
0086C8B4  48 8D 4F 38                     lea rcx, [rdi + 0x38]
0086C8B8  0F 0D 09                        prefetchw byte ptr [rcx]
0086C8BB  48 8B 01                        mov rax, qword ptr [rcx]
0086C8BE  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0086C8C2  48 8D 50 02                     lea rdx, [rax + 2]
0086C8C6  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
0086C8CB  0F 85 31 07 00 00               jne 0x14086d002
0086C8D1  41 0F 0D 0A                     prefetchw byte ptr [r10]
0086C8D5  49 8B 02                        mov rax, qword ptr [r10]
0086C8D8  48 8B C8                        mov rcx, rax
0086C8DB  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0086C8DF  48 83 F9 10                     cmp rcx, 0x10
0086C8E3  B9 00 00 00 00                  mov ecx, 0
0086C8E8  48 8D 50 F0                     lea rdx, [rax - 0x10]
0086C8EC  48 0F 46 D1                     cmovbe rdx, rcx
0086C8F0  A8 02                           test al, 2
0086C8F2  0F 85 A8 03 00 00               jne 0x14086cca0
0086C8F8  F0 49 0F B1 12                  lock cmpxchg qword ptr [r10], rdx
0086C8FD  0F 85 9D 03 00 00               jne 0x14086cca0
0086C903  49 8B CA                        mov rcx, r10
0086C906  E8 F5 4C A7 FF                  call 0x1402e1600
0086C90B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086C914  90                              nop
0086C915  66 83 81 E6 01 00 00 01         add word ptr [rcx + 0x1e6], 1
0086C91D  75 12                           jne 0x14086c931
0086C91F  48 8D 81 98 00 00 00            lea rax, [rcx + 0x98]
0086C926  90                              nop
0086C927  48 39 00                        cmp qword ptr [rax], rax
0086C92A  74 05                           je 0x14086c931
0086C92C  E8 4F 63 A7 FF                  call 0x1402e2c80
0086C931  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
0086C935  48 85 C9                        test rcx, rcx
0086C938  74 1F                           je 0x14086c959
0086C93A  0F 0D 09                        prefetchw byte ptr [rcx]
0086C93D  48 8B 01                        mov rax, qword ptr [rcx]
0086C940  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0086C944  48 8D 50 FE                     lea rdx, [rax - 2]
0086C948  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
0086C94D  0F 85 4D 07 00 00               jne 0x14086d0a0
0086C953  33 C0                           xor eax, eax
0086C955  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0086C959  48 83 7F 30 00                  cmp qword ptr [rdi + 0x30], 0
0086C95E  0F 85 58 01 00 00               jne 0x14086cabc
0086C964  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
0086C968  48 85 C0                        test rax, rax
0086C96B  74 2D                           je 0x14086c99a
0086C96D  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
0086C971  48 8D 55 78                     lea rdx, [rbp + 0x78]
0086C975  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
0086C979  E8 52 E1 E4 FF                  call 0x1406baad0
0086C97E  48 83 7F 30 00                  cmp qword ptr [rdi + 0x30], 0
0086C983  0F 85 9B 01 00 00               jne 0x14086cb24
0086C989  48 8D 47 38                     lea rax, [rdi + 0x38]
0086C98D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0086C991  33 C0                           xor eax, eax
0086C993  48 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], rax
0086C99A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086C9A3  45 33 C0                        xor r8d, r8d
0086C9A6  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
0086C9AA  33 D2                           xor edx, edx
0086C9AC  66 FF 88 E6 01 00 00            dec word ptr [rax + 0x1e6]
0086C9B3  90                              nop
0086C9B4  E8 77 38 9A FF                  call 0x140210230
0086C9B9  48 8B 4D A8                     mov rcx, qword ptr [rbp - 0x58]
0086C9BD  48 8B D0                        mov rdx, rax
0086C9C0  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
0086C9C4  41 B8 11 00 00 00               mov r8d, 0x11
0086C9CA  33 C0                           xor eax, eax
0086C9CC  F0 4C 0F B1 01                  lock cmpxchg qword ptr [rcx], r8
0086C9D1  74 11                           je 0x14086c9e4
0086C9D3  4C 8B C2                        mov r8, rdx
0086C9D6  4C 8B C9                        mov r9, rcx
0086C9D9  33 D2                           xor edx, edx
0086C9DB  E8 6C 3A 9A FF                  call 0x14021044c
0086C9E0  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
0086C9E4  48 85 D2                        test rdx, rdx
0086C9E7  74 04                           je 0x14086c9ed
0086C9E9  C6 42 0A 01                     mov byte ptr [rdx + 0xa], 1
0086C9ED  48 8B 3F                        mov rdi, qword ptr [rdi]
0086C9F0  4C 8B 55 A8                     mov r10, qword ptr [rbp - 0x58]
0086C9F4  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
0086C9F8  E9 97 FE FF FF                  jmp 0x14086c894
0086C9FD  48 8B 7D 30                     mov rdi, qword ptr [rbp + 0x30]
0086CA01  48 81 C7 B8 00 00 00            add rdi, 0xb8
0086CA08  0F 0D 0F                        prefetchw byte ptr [rdi]
0086CA0B  48 8B 07                        mov rax, qword ptr [rdi]
0086CA0E  48 8B C8                        mov rcx, rax
0086CA11  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0086CA15  48 83 F9 10                     cmp rcx, 0x10
0086CA19  B9 00 00 00 00                  mov ecx, 0
0086CA1E  48 8D 50 F0                     lea rdx, [rax - 0x10]
0086CA22  48 0F 46 D1                     cmovbe rdx, rcx
0086CA26  A8 02                           test al, 2
0086CA28  0F 85 AF 02 00 00               jne 0x14086ccdd
0086CA2E  F0 48 0F B1 17                  lock cmpxchg qword ptr [rdi], rdx
0086CA33  0F 85 A4 02 00 00               jne 0x14086ccdd
0086CA39  48 8B CF                        mov rcx, rdi
0086CA3C  E8 BF 4B A7 FF                  call 0x1402e1600
0086CA41  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086CA4A  90                              nop
0086CA4B  66 83 81 E6 01 00 00 01         add word ptr [rcx + 0x1e6], 1
0086CA53  75 12                           jne 0x14086ca67
0086CA55  48 8D 81 98 00 00 00            lea rax, [rcx + 0x98]
0086CA5C  90                              nop
0086CA5D  48 39 00                        cmp qword ptr [rax], rax
0086CA60  74 05                           je 0x14086ca67
0086CA62  E8 19 62 A7 FF                  call 0x1402e2c80
0086CA67  48 8B 55 F0                     mov rdx, qword ptr [rbp - 0x10]
0086CA6B  48 85 D2                        test rdx, rdx
0086CA6E  74 19                           je 0x14086ca89
0086CA70  0F 0D 0A                        prefetchw byte ptr [rdx]
0086CA73  48 8B 02                        mov rax, qword ptr [rdx]
0086CA76  48 83 E0 FE                     and rax, 0xfffffffffffffffe
0086CA7A  48 8D 48 FE                     lea rcx, [rax - 2]
0086CA7E  F0 48 0F B1 0A                  lock cmpxchg qword ptr [rdx], rcx
0086CA83  0F 85 E6 06 00 00               jne 0x14086d16f
0086CA89  48 8D 45 D0                     lea rax, [rbp - 0x30]
0086CA8D  48 39 45 D0                     cmp qword ptr [rbp - 0x30], rax
0086CA91  74 6D                           je 0x14086cb00
0086CA93  80 7D 83 00                     cmp byte ptr [rbp - 0x7d], 0
0086CA97  0F 85 86 09 00 00               jne 0x14086d423
0086CA9D  8B 85 18 01 00 00               mov eax, dword ptr [rbp + 0x118]
0086CAA3  0B 45 08                        or eax, dword ptr [rbp + 8]
0086CAA6  23 D8                           and ebx, eax
0086CAA8  89 5D 84                        mov dword ptr [rbp - 0x7c], ebx
0086CAAB  48 85 F6                        test rsi, rsi
0086CAAE  0F 84 14 F5 FF FF               je 0x14086bfc8
0086CAB4  89 5E 14                        mov dword ptr [rsi + 0x14], ebx
0086CAB7  E9 0C F5 FF FF                  jmp 0x14086bfc8
0086CABC  BA 20 00 00 00                  mov edx, 0x20
0086CAC1  B9 00 01 00 00                  mov ecx, 0x100
0086CAC6  41 B8 4F 62 46 6C               mov r8d, 0x6c46624f
0086CACC  E8 1F 56 31 00                  call 0x140b820f0
0086CAD1  48 89 45 00                     mov qword ptr [rbp], rax
0086CAD5  48 85 C0                        test rax, rax
0086CAD8  0F 84 56 09 00 00               je 0x14086d434
0086CADE  33 C9                           xor ecx, ecx
0086CAE0  48 89 78 10                     mov qword ptr [rax + 0x10], rdi
0086CAE4  48 89 48 18                     mov qword ptr [rax + 0x18], rcx
0086CAE8  48 8D 55 D0                     lea rdx, [rbp - 0x30]
0086CAEC  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
0086CAF0  48 39 11                        cmp qword ptr [rcx], rdx
0086CAF3  0F 84 A8 06 00 00               je 0x14086d1a1
0086CAF9  B9 03 00 00 00                  mov ecx, 3
0086CAFE  CD 29                           int 0x29
0086CB00  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
0086CB07  BA 4F 62 43 62                  mov edx, 0x6243624f
0086CB0C  E8 CF AD A8 FF                  call 0x1402f78e0
0086CB11  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086CB1A  E8 D1 24 9F FF                  call 0x14025eff0
0086CB1F  E9 6F FF FF FF                  jmp 0x14086ca93
0086CB24  48 8B 4D 00                     mov rcx, qword ptr [rbp]
0086CB28  48 8B 85 90 00 00 00            mov rax, qword ptr [rbp + 0x90]
0086CB2F  48 89 41 18                     mov qword ptr [rcx + 0x18], rax
0086CB33  E9 59 FE FF FF                  jmp 0x14086c991
0086CB38  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
0086CB3C  E8 7F 50 9A FF                  call 0x140211bc0
0086CB41  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086CB4A  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0086CB51  90                              nop
0086CB52  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
0086CB56  E9 98 FB FF FF                  jmp 0x14086c6f3
0086CB5B  49 8B 4A 10                     mov rcx, qword ptr [r10 + 0x10]
0086CB5F  BA 00 08 00 00                  mov edx, 0x800
0086CB64  E8 CB 0A 0E 00                  call 0x14094d634
0086CB69  48 8B C8                        mov rcx, rax
0086CB6C  48 85 C0                        test rax, rax
0086CB6F  0F 84 55 06 00 00               je 0x14086d1ca
0086CB75  33 C0                           xor eax, eax
0086CB77  F0 48 0F B1 0B                  lock cmpxchg qword ptr [rbx], rcx
0086CB7C  0F 84 DB 02 00 00               je 0x14086ce5d
0086CB82  48 8B D1                        mov rdx, rcx
0086CB85  41 B8 00 08 00 00               mov r8d, 0x800
0086CB8B  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0086CB8F  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
0086CB93  E8 78 E8 FF FF                  call 0x14086b410
0086CB98  48 8B 0B                        mov rcx, qword ptr [rbx]
0086CB9B  4C 8B 55 90                     mov r10, qword ptr [rbp - 0x70]
0086CB9F  48 85 C9                        test rcx, rcx
0086CBA2  0F 85 EA F8 FF FF               jne 0x14086c492
0086CBA8  4C 89 75 90                     mov qword ptr [rbp - 0x70], r14
0086CBAC  41 83 E6 FC                     and r14d, 0xfffffffc
0086CBB0  41 83 7A 04 00                  cmp dword ptr [r10 + 4], 0
0086CBB5  44 89 75 90                     mov dword ptr [rbp - 0x70], r14d
0086CBB9  0F 84 59 04 00 00               je 0x14086d018
0086CBBF  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
0086CBC3  49 8B CA                        mov rcx, r10
0086CBC6  E8 89 E8 FF FF                  call 0x14086b454
0086CBCB  33 C9                           xor ecx, ecx
0086CBCD  48 85 C0                        test rax, rax
0086CBD0  74 03                           je 0x14086cbd5
0086CBD2  48 89 08                        mov qword ptr [rax], rcx
0086CBD5  48 89 4F 08                     mov qword ptr [rdi + 8], rcx
0086CBD9  41 0F B6 42 2C                  movzx eax, byte ptr [r10 + 0x2c]
0086CBDE  24 01                           and al, 1
0086CBE0  88 45 80                        mov byte ptr [rbp - 0x80], al
0086CBE3  0F 85 4D 01 00 00               jne 0x14086cd36
0086CBE9  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
0086CBF1  8B D8                           mov ebx, eax
0086CBF3  45 33 C0                        xor r8d, r8d
0086CBF6  48 FF C3                        inc rbx
0086CBF9  33 D2                           xor edx, edx
0086CBFB  48 C1 E3 06                     shl rbx, 6
0086CBFF  49 03 DA                        add rbx, r10
0086CC02  48 8B CB                        mov rcx, rbx
0086CC05  E8 26 36 9A FF                  call 0x140210230
0086CC0A  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
0086CC10  4C 8B F0                        mov r14, rax
0086CC13  73 0E                           jae 0x14086cc23
0086CC15  4C 8B C3                        mov r8, rbx
0086CC18  48 8B D0                        mov rdx, rax
0086CC1B  48 8B CB                        mov rcx, rbx
0086CC1E  E8 6D 30 9A FF                  call 0x14020fc90
0086CC23  4D 85 F6                        test r14, r14
0086CC26  74 05                           je 0x14086cc2d
0086CC28  41 C6 46 0A 01                  mov byte ptr [r14 + 0xa], 1
0086CC2D  80 7D 80 00                     cmp byte ptr [rbp - 0x80], 0
0086CC31  0F 85 8C 00 00 00               jne 0x14086ccc3
0086CC37  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0086CC3B  48 89 47 08                     mov qword ptr [rdi + 8], rax
0086CC3F  48 85 C0                        test rax, rax
0086CC42  75 04                           jne 0x14086cc48
0086CC44  48 89 7B 10                     mov qword ptr [rbx + 0x10], rdi
0086CC48  48 89 7B 08                     mov qword ptr [rbx + 8], rdi
0086CC4C  FF 4B 18                        dec dword ptr [rbx + 0x18]
0086CC4F  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
0086CC56  F0 48 0F C1 03                  lock xadd qword ptr [rbx], rax
0086CC5B  24 06                           and al, 6
0086CC5D  3C 02                           cmp al, 2
0086CC5F  0F 84 28 03 00 00               je 0x14086cf8d
0086CC65  48 8B CB                        mov rcx, rbx
0086CC68  E8 93 49 A7 FF                  call 0x1402e1600
0086CC6D  33 C0                           xor eax, eax
0086CC6F  44 8B F0                        mov r14d, eax
0086CC72  E9 E8 F4 FF FF                  jmp 0x14086c15f
0086CC77  41 F6 45 42 08                  test byte ptr [r13 + 0x42], 8
0086CC7C  0F 84 BB 01 00 00               je 0x14086ce3d
0086CC82  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0086CC87  49 8D 54 24 D0                  lea rdx, [r12 - 0x30]
0086CC8C  41 B9 01 00 00 00               mov r9d, 1
0086CC92  4D 8B C5                        mov r8, r13
0086CC95  B9 89 01 00 00                  mov ecx, 0x189
0086CC9A  E8 C1 09 C9 FF                  call 0x1404fd660
0086CC9F  CC                              int3
0086CCA0  49 8B CA                        mov rcx, r10
0086CCA3  E8 28 6C 9F FF                  call 0x1402638d0
0086CCA8  4C 8B 55 A8                     mov r10, qword ptr [rbp - 0x58]
0086CCAC  E9 52 FC FF FF                  jmp 0x14086c903
0086CCB1  41 8B D1                        mov edx, r9d
0086CCB4  E9 89 F3 FF FF                  jmp 0x14086c042
0086CCB9  E8 F2 D1 AD FF                  call 0x140349eb0
0086CCBE  E9 09 F7 FF FF                  jmp 0x14086c3cc
0086CCC3  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0086CCC7  48 85 C0                        test rax, rax
0086CCCA  0F 84 5B 07 00 00               je 0x14086d42b
0086CCD0  48 89 78 08                     mov qword ptr [rax + 8], rdi
0086CCD4  48 89 7B 10                     mov qword ptr [rbx + 0x10], rdi
0086CCD8  E9 6F FF FF FF                  jmp 0x14086cc4c
0086CCDD  48 8B CF                        mov rcx, rdi
0086CCE0  E8 EB 6B 9F FF                  call 0x1402638d0
0086CCE5  E9 4F FD FF FF                  jmp 0x14086ca39
0086CCEA  48 8D 45 18                     lea rax, [rbp + 0x18]
0086CCEE  4C 8B CE                        mov r9, rsi
0086CCF1  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0086CCF6  4C 8D 45 84                     lea r8, [rbp - 0x7c]
0086CCFA  4C 89 6C 24 28                  mov qword ptr [rsp + 0x28], r13
0086CCFF  49 8B D4                        mov rdx, r12
0086CD02  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
0086CD06  48 8B 5D 98                     mov rbx, qword ptr [rbp - 0x68]
0086CD0A  48 8B CB                        mov rcx, rbx
0086CD0D  E8 AE 25 13 00                  call 0x14099f2c0
0086CD12  8B F8                           mov edi, eax
0086CD14  85 C0                           test eax, eax
0086CD16  0F 88 8A F6 FF FF               js 0x14086c3a6
0086CD1C  48 8B 7D 18                     mov rdi, qword ptr [rbp + 0x18]
0086CD20  49 3B FC                        cmp rdi, r12
0086CD23  0F 85 67 03 00 00               jne 0x14086d090
0086CD29  33 C0                           xor eax, eax
0086CD2B  8B F8                           mov edi, eax
0086CD2D  48 89 45 18                     mov qword ptr [rbp + 0x18], rax
0086CD31  E9 4A F1 FF FF                  jmp 0x14086be80
0086CD36  8B C1                           mov eax, ecx
0086CD38  E9 B4 FE FF FF                  jmp 0x14086cbf1
0086CD3D  48 8B 05 BC CD 76 00            mov rax, qword ptr [rip + 0x76cdbc]
0086CD44  48 89 85 38 01 00 00            mov qword ptr [rbp + 0x138], rax
0086CD4B  C7 85 30 01 00 00 01 00 00 00   mov dword ptr [rbp + 0x130], 1
0086CD55  C7 85 34 01 00 00 01 00 00 00   mov dword ptr [rbp + 0x134], 1
0086CD5F  44 89 8D 40 01 00 00            mov dword ptr [rbp + 0x140], r9d
0086CD66  45 84 FF                        test r15b, r15b
0086CD69  0F 84 0D 04 00 00               je 0x14086d17c
0086CD6F  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
0086CD73  48 85 C9                        test rcx, rcx
0086CD76  0F 85 E4 03 00 00               jne 0x14086d160
0086CD7C  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
0086CD80  41 B9 01 00 00 00               mov r9d, 1
0086CD86  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
0086CD8B  45 8B C1                        mov r8d, r9d
0086CD8E  48 8D 95 38 01 00 00            lea rdx, [rbp + 0x138]
0086CD95  E8 16 E9 B9 FF                  call 0x14040b6b0
0086CD9A  84 C0                           test al, al
0086CD9C  0F 85 DA 03 00 00               jne 0x14086d17c
0086CDA2  45 33 C9                        xor r9d, r9d
0086CDA5  4C 8D 85 30 01 00 00            lea r8, [rbp + 0x130]
0086CDAC  48 8D 56 20                     lea rdx, [rsi + 0x20]
0086CDB0  33 C9                           xor ecx, ecx
0086CDB2  E8 F9 4E 00 00                  call 0x140871cb0
0086CDB7  BF 61 00 00 C0                  mov edi, 0xc0000061
0086CDBC  89 7D B4                        mov dword ptr [rbp - 0x4c], edi
0086CDBF  E9 DE F5 FF FF                  jmp 0x14086c3a2
0086CDC4  48 8B CB                        mov rcx, rbx
0086CDC7  E8 04 90 9F FF                  call 0x140265dd0
0086CDCC  E9 17 F3 FF FF                  jmp 0x14086c0e8
0086CDD1  48 3B 3D 80 28 6A 00            cmp rdi, qword ptr [rip + 0x6a2880]
0086CDD8  0F 85 D0 F1 FF FF               jne 0x14086bfae
0086CDDE  80 7D 82 00                     cmp byte ptr [rbp - 0x7e], 0
0086CDE2  0F 85 C6 F1 FF FF               jne 0x14086bfae
0086CDE8  49 8B CC                        mov rcx, r12
0086CDEB  E8 90 1D EE FF                  call 0x14074eb80
0086CDF0  8B 5D 84                        mov ebx, dword ptr [rbp - 0x7c]
0086CDF3  E9 B6 F1 FF FF                  jmp 0x14086bfae
0086CDF8  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
0086CDFC  49 8B D7                        mov rdx, r15
0086CDFF  E8 DC 64 FF FF                  call 0x1408632e0
0086CE04  48 8B 75 A0                     mov rsi, qword ptr [rbp - 0x60]
0086CE08  45 85 ED                        test r13d, r13d
0086CE0B  74 11                           je 0x14086ce1e
0086CE0D  41 B8 4F 62 48 6E               mov r8d, 0x6e48624f
0086CE13  41 8B D5                        mov edx, r13d
0086CE16  48 8B CE                        mov rcx, rsi
0086CE19  E8 A2 FD BC FF                  call 0x14043cbc0
0086CE1E  0F B6 45 83                     movzx eax, byte ptr [rbp - 0x7d]
0086CE22  BF 9A 00 00 C0                  mov edi, 0xc000009a
0086CE27  4C 8B BD A0 00 00 00            mov r15, qword ptr [rbp + 0xa0]
0086CE2E  E9 A4 F4 FF FF                  jmp 0x14086c2d7
0086CE33  E8 78 D0 AD FF                  call 0x140349eb0
0086CE38  E9 04 F6 FF FF                  jmp 0x14086c441
0086CE3D  41 F6 44 24 EA 02               test byte ptr [r12 - 0x16], 2
0086CE43  0F 84 D5 EC FF FF               je 0x14086bb1e
0086CE49  E9 34 FE FF FF                  jmp 0x14086cc82
0086CE4E  8D 04 52                        lea eax, [rdx + rdx*2]
0086CE51  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
0086CE58  E9 98 ED FF FF                  jmp 0x14086bbf5
0086CE5D  4C 8B 55 90                     mov r10, qword ptr [rbp - 0x70]
0086CE61  F0 41 FF 42 04                  lock inc dword ptr [r10 + 4]
0086CE66  8B 55 A8                        mov edx, dword ptr [rbp - 0x58]
0086CE69  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
0086CE6D  48 89 04 D1                     mov qword ptr [rcx + rdx*8], rax
0086CE71  E9 BF F2 FF FF                  jmp 0x14086c135
0086CE76  4D 8B 24 24                     mov r12, qword ptr [r12]
0086CE7A  4D 85 E4                        test r12, r12
0086CE7D  0F 85 C9 02 00 00               jne 0x14086d14c
0086CE83  48 39 55 48                     cmp qword ptr [rbp + 0x48], rdx
0086CE87  0F 85 8D 03 00 00               jne 0x14086d21a
0086CE8D  48 8B 05 4C 9C 75 00            mov rax, qword ptr [rip + 0x759c4c]
0086CE94  48 8D 4F D0                     lea rcx, [rdi - 0x30]
0086CE98  48 C1 E9 08                     shr rcx, 8
0086CE9C  32 4F E8                        xor cl, byte ptr [rdi - 0x18]
0086CE9F  32 0D A7 9F 75 00               xor cl, byte ptr [rip + 0x759fa7]
0086CEA5  3A 48 28                        cmp cl, byte ptr [rax + 0x28]
0086CEA8  75 10                           jne 0x14086ceba
0086CEAA  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
0086CEAE  8B 48 34                        mov ecx, dword ptr [rax + 0x34]
0086CEB1  F6 C1 10                        test cl, 0x10
0086CEB4  0F 85 0F F3 FF FF               jne 0x14086c1c9
0086CEBA  4C 8B 46 48                     mov r8, qword ptr [rsi + 0x48]
0086CEBE  45 32 E4                        xor r12b, r12b
0086CEC1  4D 85 C0                        test r8, r8
0086CEC4  0F 84 D0 00 00 00               je 0x14086cf9a
0086CECA  4D 8B 40 38                     mov r8, qword ptr [r8 + 0x38]
0086CECE  4D 85 C0                        test r8, r8
0086CED1  0F 84 C3 00 00 00               je 0x14086cf9a
0086CED7  41 B4 01                        mov r12b, 1
0086CEDA  E9 BE 00 00 00                  jmp 0x14086cf9d
0086CEDF  83 BB C4 00 00 00 02            cmp dword ptr [rbx + 0xc4], 2
0086CEE6  0F 8C 1E F8 FF FF               jl 0x14086c70a
0086CEEC  48 8B 93 98 00 00 00            mov rdx, qword ptr [rbx + 0x98]
0086CEF3  48 8B 8F 98 00 00 00            mov rcx, qword ptr [rdi + 0x98]
0086CEFA  48 8B 12                        mov rdx, qword ptr [rdx]
0086CEFD  48 8B 09                        mov rcx, qword ptr [rcx]
0086CF00  E8 CB 3B B9 FF                  call 0x140400ad0
0086CF05  48 8B 75 A0                     mov rsi, qword ptr [rbp - 0x60]
0086CF09  84 C0                           test al, al
0086CF0B  0F 85 FD F7 FF FF               jne 0x14086c70e
0086CF11  48 8D 4E D0                     lea rcx, [rsi - 0x30]
0086CF15  E8 26 49 B3 FF                  call 0x1403a1840
0086CF1A  48 85 C0                        test rax, rax
0086CF1D  0F 84 EB F7 FF FF               je 0x14086c70e
0086CF23  4C 8B 05 46 89 69 00            mov r8, qword ptr [rip + 0x698946]
0086CF2A  48 8D 8F 28 03 00 00            lea rcx, [rdi + 0x328]
0086CF31  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
0086CF36  45 33 C9                        xor r9d, r9d
0086CF39  33 D2                           xor edx, edx
0086CF3B  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
0086CF40  E8 9B B6 B5 FF                  call 0x1403c85e0
0086CF45  84 C0                           test al, al
0086CF47  0F 84 C1 F7 FF FF               je 0x14086c70e
0086CF4D  48 8B 8B D8 00 00 00            mov rcx, qword ptr [rbx + 0xd8]
0086CF54  48 8B D6                        mov rdx, rsi
0086CF57  48 81 C1 88 00 00 00            add rcx, 0x88
0086CF5E  E8 1D C3 13 00                  call 0x1409a9280
0086CF63  E9 A6 F7 FF FF                  jmp 0x14086c70e
0086CF68  33 D2                           xor edx, edx
0086CF6A  48 8B CB                        mov rcx, rbx
0086CF6D  E8 FE 58 31 00                  call 0x140b82870
0086CF72  89 7D B4                        mov dword ptr [rbp - 0x4c], edi
0086CF75  85 FF                           test edi, edi
0086CF77  0F 88 25 F4 FF FF               js 0x14086c3a2
0086CF7D  4C 8B 6D A8                     mov r13, qword ptr [rbp - 0x58]
0086CF81  45 33 C9                        xor r9d, r9d
0086CF84  4C 8B 55 98                     mov r10, qword ptr [rbp - 0x68]
0086CF88  E9 98 EE FF FF                  jmp 0x14086be25
0086CF8D  48 8B CB                        mov rcx, rbx
0086CF90  E8 3B 8E 9F FF                  call 0x140265dd0
0086CF95  E9 CB FC FF FF                  jmp 0x14086cc65
0086CF9A  4C 8B C2                        mov r8, rdx
0086CF9D  B8 20 00 00 00                  mov eax, 0x20
0086CFA2  4C 8D 4D 20                     lea r9, [rbp + 0x20]
0086CFA6  8B D0                           mov edx, eax
0086CFA8  48 8B CF                        mov rcx, rdi
0086CFAB  E8 6C 72 00 00                  call 0x14087421c
0086CFB0  85 C0                           test eax, eax
0086CFB2  78 14                           js 0x14086cfc8
0086CFB4  48 8B 5D 20                     mov rbx, qword ptr [rbp + 0x20]
0086CFB8  48 8D 55 20                     lea rdx, [rbp + 0x20]
0086CFBC  45 0F B6 C4                     movzx r8d, r12b
0086CFC0  49 8B CF                        mov rcx, r15
0086CFC3  E8 30 02 05 00                  call 0x1408bd1f8
0086CFC8  33 D2                           xor edx, edx
0086CFCA  E9 FA F1 FF FF                  jmp 0x14086c1c9
0086CFCF  85 FF                           test edi, edi
0086CFD1  0F 88 CB F3 FF FF               js 0x14086c3a2
0086CFD7  4C 8B 4D B8                     mov r9, qword ptr [rbp - 0x48]
0086CFDB  B9 20 11 00 00                  mov ecx, 0x1120
0086CFE0  49 8B 17                        mov rdx, qword ptr [r15]
0086CFE3  4C 8B C6                        mov r8, rsi
0086CFE6  E8 59 DA FF FF                  call 0x14086aa44
0086CFEB  E9 B2 F3 FF FF                  jmp 0x14086c3a2
0086CFF0  BA 01 00 00 00                  mov edx, 1
0086CFF5  48 8B CF                        mov rcx, rdi
0086CFF8  E8 A3 70 00 00                  call 0x1408740a0
0086CFFD  E9 12 EE FF FF                  jmp 0x14086be14
0086D002  E8 49 F0 AD FF                  call 0x14034c050
0086D007  84 C0                           test al, al
0086D009  0F 84 DE F9 FF FF               je 0x14086c9ed
0086D00F  4C 8B 55 A8                     mov r10, qword ptr [rbp - 0x58]
0086D013  E9 B9 F8 FF FF                  jmp 0x14086c8d1
0086D018  33 C9                           xor ecx, ecx
0086D01A  E9 B6 FB FF FF                  jmp 0x14086cbd5
0086D01F  4C 8D 0D 5A 6A 00 00            lea r9, [rip + 0x6a5a]
0086D026  49 3B C1                        cmp rax, r9
0086D029  4C 8B CB                        mov r9, rbx
0086D02C  0F 85 48 09 00 00               jne 0x14086d97a
0086D032  48 8D 45 B0                     lea rax, [rbp - 0x50]
0086D036  49 8B CC                        mov rcx, r12
0086D039  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0086D03E  E8 3D 6A 00 00                  call 0x140873a80
0086D043  E9 FB F4 FF FF                  jmp 0x14086c543
0086D048  4C 8B C7                        mov r8, rdi
0086D04B  49 8D 4C 24 D0                  lea rcx, [r12 - 0x30]
0086D050  E8 F7 77 00 00                  call 0x14087484c
0086D055  48 8B F8                        mov rdi, rax
0086D058  E9 72 ED FF FF                  jmp 0x14086bdcf
0086D05D  33 D2                           xor edx, edx
0086D05F  48 8D 4F D0                     lea rcx, [rdi - 0x30]
0086D063  41 B9 44 66 6C 74               mov r9d, 0x746c6644
0086D069  44 8D 42 01                     lea r8d, [rdx + 1]
0086D06D  E8 72 39 9A FF                  call 0x1402109e4
0086D072  41 B8 01 00 00 00               mov r8d, 1
0086D078  48 8D 4F D0                     lea rcx, [rdi - 0x30]
0086D07C  41 0F B6 D0                     movzx edx, r8b
0086D080  41 B9 4F 62 48 6E               mov r9d, 0x6e48624f
0086D086  E8 59 39 9A FF                  call 0x1402109e4
0086D08B  E9 F6 F0 FF FF                  jmp 0x14086c186
0086D090  4C 8B E7                        mov r12, rdi
0086D093  48 89 7D A0                     mov qword ptr [rbp - 0x60], rdi
0086D097  C6 45 82 01                     mov byte ptr [rbp - 0x7e], 1
0086D09B  E9 E0 ED FF FF                  jmp 0x14086be80
0086D0A0  E8 0B CE AD FF                  call 0x140349eb0
0086D0A5  E9 A9 F8 FF FF                  jmp 0x14086c953
0086D0AA  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0086D0AD  49 8D 78 38                     lea rdi, [r8 + 0x38]
0086D0B1  8B D8                           mov ebx, eax
0086D0B3  C6 45 80 01                     mov byte ptr [rbp - 0x80], 1
0086D0B7  48 FF C0                        inc rax
0086D0BA  89 5D 00                        mov dword ptr [rbp], ebx
0086D0BD  48 C1 E0 06                     shl rax, 6
0086D0C1  33 D2                           xor edx, edx
0086D0C3  49 03 C0                        add rax, r8
0086D0C6  48 8B CF                        mov rcx, rdi
0086D0C9  45 33 C0                        xor r8d, r8d
0086D0CC  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
0086D0D0  E8 5B 31 9A FF                  call 0x140210230
0086D0D5  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
0086D0DB  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
0086D0DF  73 12                           jae 0x14086d0f3
0086D0E1  4C 8B C7                        mov r8, rdi
0086D0E4  48 8B D0                        mov rdx, rax
0086D0E7  48 8B CF                        mov rcx, rdi
0086D0EA  E8 A1 2B 9A FF                  call 0x14020fc90
0086D0EF  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
0086D0F3  48 85 C0                        test rax, rax
0086D0F6  74 04                           je 0x14086d0fc
0086D0F8  C6 40 0A 01                     mov byte ptr [rax + 0xa], 1
0086D0FC  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0086D100  8B 45 A8                        mov eax, dword ptr [rbp - 0x58]
0086D103  3B 01                           cmp eax, dword ptr [rcx]
0086D105  75 0C                           jne 0x14086d113
0086D107  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
0086D10B  E8 EC 01 0E 00                  call 0x14094d2fc
0086D110  88 45 80                        mov byte ptr [rbp - 0x80], al
0086D113  48 C7 C2 FF FF FF FF            mov rdx, 0xffffffffffffffff
0086D11A  F0 48 0F C1 17                  lock xadd qword ptr [rdi], rdx
0086D11F  80 E2 06                        and dl, 6
0086D122  80 FA 02                        cmp dl, 2
0086D125  0F 84 65 08 00 00               je 0x14086d990
0086D12B  48 8B CF                        mov rcx, rdi
0086D12E  E8 CD 44 A7 FF                  call 0x1402e1600
0086D133  44 38 75 80                     cmp byte ptr [rbp - 0x80], r14b
0086D137  0F 84 22 F0 FF FF               je 0x14086c15f
0086D13D  8B 4D 08                        mov ecx, dword ptr [rbp + 8]
0086D140  45 33 C9                        xor r9d, r9d
0086D143  4C 8B 45 90                     mov r8, qword ptr [rbp - 0x70]
0086D147  E9 07 EF FF FF                  jmp 0x14086c053
0086D14C  4C 8B 7E 48                     mov r15, qword ptr [rsi + 0x48]
0086D150  40 32 FF                        xor dil, dil
0086D153  4C 89 75 38                     mov qword ptr [rbp + 0x38], r14
0086D157  48 89 55 10                     mov qword ptr [rbp + 0x10], rdx
0086D15B  E9 90 F0 FF FF                  jmp 0x14086c1f0
0086D160  83 7E 28 02                     cmp dword ptr [rsi + 0x28], 2
0086D164  0F 8D 16 FC FF FF               jge 0x14086cd80
0086D16A  E9 33 FC FF FF                  jmp 0x14086cda2
0086D16F  48 8B CA                        mov rcx, rdx
0086D172  E8 39 CD AD FF                  call 0x140349eb0
0086D177  E9 0D F9 FF FF                  jmp 0x14086ca89
0086D17C  81 66 10 FF FF FF FE            and dword ptr [rsi + 0x10], 0xfeffffff
0086D183  48 8D 95 30 01 00 00            lea rdx, [rbp + 0x130]
0086D18A  81 4E 14 00 00 00 01            or dword ptr [rsi + 0x14], 0x1000000
0086D191  48 8B CE                        mov rcx, rsi
0086D194  E8 E7 A7 16 00                  call 0x1409d7980
0086D199  45 33 C9                        xor r9d, r9d
0086D19C  E9 CA EB FF FF                  jmp 0x14086bd6b
0086D1A1  48 89 48 08                     mov qword ptr [rax + 8], rcx
0086D1A5  48 8D 55 D0                     lea rdx, [rbp - 0x30]
0086D1A9  48 89 10                        mov qword ptr [rax], rdx
0086D1AC  48 89 01                        mov qword ptr [rcx], rax
0086D1AF  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
0086D1B3  E9 AC F7 FF FF                  jmp 0x14086c964
0086D1B8  BA 01 00 00 00                  mov edx, 1
0086D1BD  48 8B CB                        mov rcx, rbx
0086D1C0  E8 DB 6E 00 00                  call 0x1408740a0
0086D1C5  E9 87 ED FF FF                  jmp 0x14086bf51
0086D1CA  4C 8B 55 90                     mov r10, qword ptr [rbp - 0x70]
0086D1CE  E9 D5 F9 FF FF                  jmp 0x14086cba8
0086D1D3  BF 9A 00 00 C0                  mov edi, 0xc000009a
0086D1D8  E9 95 FD FF FF                  jmp 0x14086cf72
0086D1DD  4C 8B C3                        mov r8, rbx
0086D1E0  49 8B CF                        mov rcx, r15
0086D1E3  E8 64 76 00 00                  call 0x14087484c
0086D1E8  48 8B D8                        mov rbx, rax
0086D1EB  E9 22 ED FF FF                  jmp 0x14086bf12
0086D1F0  BA 01 00 00 00                  mov edx, 1
0086D1F5  48 8B CB                        mov rcx, rbx
0086D1F8  E8 A3 6E 00 00                  call 0x1408740a0
0086D1FD  E9 DC EA FF FF                  jmp 0x14086bcde
0086D202  4C 8B C3                        mov r8, rbx
0086D205  49 8D 4C 24 D0                  lea rcx, [r12 - 0x30]
0086D20A  E8 3D 76 00 00                  call 0x14087484c
0086D20F  48 8B D8                        mov rbx, rax
0086D212  45 33 C9                        xor r9d, r9d
0086D215  E9 F7 E8 FF FF                  jmp 0x14086bb11
0086D21A  45 33 C0                        xor r8d, r8d
0086D21D  48 8D 55 48                     lea rdx, [rbp + 0x48]
0086D221  49 8B CF                        mov rcx, r15
0086D224  E8 CF FF 04 00                  call 0x1408bd1f8
0086D229  4C 8B 7E 48                     mov r15, qword ptr [rsi + 0x48]
0086D22D  33 D2                           xor edx, edx
0086D22F  48 89 55 10                     mov qword ptr [rbp + 0x10], rdx
0086D233  40 32 FF                        xor dil, dil
0086D236  4C 89 75 38                     mov qword ptr [rbp + 0x38], r14
0086D23A  E9 A4 EF FF FF                  jmp 0x14086c1e3
0086D23F  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
0086D246  C7 44 24 30 02 00 00 00         mov dword ptr [rsp + 0x30], 2
0086D24E  C7 44 24 28 00 02 00 00         mov dword ptr [rsp + 0x28], 0x200
0086D256  4C 8D 4D 10                     lea r9, [rbp + 0x10]
0086D25A  89 54 24 20                     mov dword ptr [rsp + 0x20], edx
0086D25E  4C 8B C0                        mov r8, rax
0086D261  49 8B D6                        mov rdx, r14
0086D264  48 8B C8                        mov rcx, rax
0086D267  E8 E4 05 E4 FF                  call 0x1406ad850
0086D26C  33 FF                           xor edi, edi
0086D26E  85 C0                           test eax, eax
0086D270  78 30                           js 0x14086d2a2
0086D272  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
0086D276  48 8D 85 A8 00 00 00            lea rax, [rbp + 0xa8]
0086D27D  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
0086D282  45 33 C9                        xor r9d, r9d
0086D285  45 33 C0                        xor r8d, r8d
0086D288  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0086D28D  33 D2                           xor edx, edx
0086D28F  48 89 BD A8 00 00 00            mov qword ptr [rbp + 0xa8], rdi
0086D296  E8 15 BB FF FF                  call 0x140868db0
0086D29B  48 8B 9D A8 00 00 00            mov rbx, qword ptr [rbp + 0xa8]
0086D2A2  48 8D 96 90 00 00 00            lea rdx, [rsi + 0x90]
0086D2A9  45 33 C9                        xor r9d, r9d
0086D2AC  41 B0 01                        mov r8b, 1
0086D2AF  48 8B CB                        mov rcx, rbx
0086D2B2  E8 A9 27 0B 00                  call 0x14091fa60
0086D2B7  66 89 45 80                     mov word ptr [rbp - 0x80], ax
0086D2BB  48 85 DB                        test rbx, rbx
0086D2BE  74 08                           je 0x14086d2c8
0086D2C0  48 8B CB                        mov rcx, rbx
0086D2C3  E8 88 C0 A8 FF                  call 0x1402f9350
0086D2C8  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
0086D2CC  48 85 C9                        test rcx, rcx
0086D2CF  74 09                           je 0x14086d2da
0086D2D1  E8 DA FF E3 FF                  call 0x1406ad2b0
0086D2D6  48 89 7D 10                     mov qword ptr [rbp + 0x10], rdi
0086D2DA  E8 81 62 BC FF                  call 0x140433560
0086D2DF  48 89 B4 24 90 00 00 00         mov qword ptr [rsp + 0x90], rsi
0086D2E7  49 8D 4F 20                     lea rcx, [r15 + 0x20]
0086D2EB  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
0086D2F3  48 8D BE 80 00 00 00            lea rdi, [rsi + 0x80]
0086D2FA  48 8B D8                        mov rbx, rax
0086D2FD  4C 8D 8E 90 00 00 00            lea r9, [rsi + 0x90]
0086D304  33 C0                           xor eax, eax
0086D306  4C 8D 45 38                     lea r8, [rbp + 0x38]
0086D30A  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0086D312  48 8D 15 8F 40 79 FF            lea rdx, [rip - 0x86bf71]
0086D319  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
0086D31D  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0086D322  49 8B 07                        mov rax, qword ptr [r15]
0086D325  C7 44 24 68 02 00 00 00         mov dword ptr [rsp + 0x68], 2
0086D32D  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
0086D332  C6 44 24 58 01                  mov byte ptr [rsp + 0x58], 1
0086D337  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0086D33C  8B 46 14                        mov eax, dword ptr [rsi + 0x14]
0086D33F  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
0086D343  8B 46 18                        mov eax, dword ptr [rsi + 0x18]
0086D346  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
0086D34A  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
0086D34E  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0086D353  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
0086D357  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0086D35C  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
0086D361  44 0F B7 65 80                  movzx r12d, word ptr [rbp - 0x80]
0086D366  41 0F B7 CC                     movzx ecx, r12w
0086D36A  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0086D36F  E8 C8 1E 0B 00                  call 0x14091f23c
0086D374  8B 4E 14                        mov ecx, dword ptr [rsi + 0x14]
0086D377  4C 8D 8E 90 00 00 00            lea r9, [rsi + 0x90]
0086D37E  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
0086D383  4C 8D 45 38                     lea r8, [rbp + 0x38]
0086D387  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
0086D38C  C6 44 24 48 01                  mov byte ptr [rsp + 0x48], 1
0086D391  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
0086D395  8B 4E 18                        mov ecx, dword ptr [rsi + 0x18]
0086D398  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
0086D39C  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
0086D3A0  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0086D3A5  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
0086D3A9  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
0086D3AE  41 0F B7 CC                     movzx ecx, r12w
0086D3B2  88 45 80                        mov byte ptr [rbp - 0x80], al
0086D3B5  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
0086D3BA  E8 89 25 0B 00                  call 0x14091f948
0086D3BF  0F B6 7D 80                     movzx edi, byte ptr [rbp - 0x80]
0086D3C3  E9 40 EE FF FF                  jmp 0x14086c208
0086D3C8  80 7E 7C 00                     cmp byte ptr [rsi + 0x7c], 0
0086D3CC  0F 84 6D FE FF FF               je 0x14086d23f
0086D3D2  49 8B 07                        mov rax, qword ptr [r15]
0086D3D5  4C 8D 86 80 00 00 00            lea r8, [rsi + 0x80]
0086D3DC  C6 44 24 48 01                  mov byte ptr [rsp + 0x48], 1
0086D3E1  48 8D 96 90 00 00 00            lea rdx, [rsi + 0x90]
0086D3E8  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0086D3ED  48 8D 0D B4 3F 79 FF            lea rcx, [rip - 0x86c04c]
0086D3F4  8B 46 14                        mov eax, dword ptr [rsi + 0x14]
0086D3F7  4D 8B CE                        mov r9, r14
0086D3FA  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0086D3FE  48 8B 46 38                     mov rax, qword ptr [rsi + 0x38]
0086D402  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0086D407  48 8B 46 30                     mov rax, qword ptr [rsi + 0x30]
0086D40B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0086D410  48 8B 46 20                     mov rax, qword ptr [rsi + 0x20]
0086D414  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0086D419  E8 D2 0F 00 00                  call 0x14086e3f0
0086D41E  E9 E5 ED FF FF                  jmp 0x14086c208
0086D423  8B 5D 84                        mov ebx, dword ptr [rbp - 0x7c]
0086D426  E9 9D EB FF FF                  jmp 0x14086bfc8
0086D42B  48 89 7B 08                     mov qword ptr [rbx + 8], rdi
0086D42F  E9 A0 F8 FF FF                  jmp 0x14086ccd4
0086D434  48 8D 4F 38                     lea rcx, [rdi + 0x38]
0086D438  E8 43 CA AD FF                  call 0x140349e80
0086D43D  48 8D 45 D0                     lea rax, [rbp - 0x30]
0086D441  48 39 45 D0                     cmp qword ptr [rbp - 0x30], rax
0086D445  0F 84 59 04 00 00               je 0x14086d8a4
0086D44B  33 C0                           xor eax, eax
0086D44D  C7 85 D8 00 00 00 9A 00 00 C0   mov dword ptr [rbp + 0xd8], 0xc000009a
0086D457  48 89 85 D0 00 00 00            mov qword ptr [rbp + 0xd0], rax
0086D45E  48 8D 55 D0                     lea rdx, [rbp - 0x30]
0086D462  48 89 85 DC 00 00 00            mov qword ptr [rbp + 0xdc], rax
0086D469  48 8D 8D B8 00 00 00            lea rcx, [rbp + 0xb8]
0086D470  89 85 E4 00 00 00               mov dword ptr [rbp + 0xe4], eax
0086D476  8B 45 78                        mov eax, dword ptr [rbp + 0x78]
0086D479  89 85 B8 00 00 00               mov dword ptr [rbp + 0xb8], eax
0086D47F  8B 45 7C                        mov eax, dword ptr [rbp + 0x7c]
0086D482  89 85 BC 00 00 00               mov dword ptr [rbp + 0xbc], eax
0086D488  48 8B 85 88 00 00 00            mov rax, qword ptr [rbp + 0x88]
0086D48F  48 89 85 C8 00 00 00            mov qword ptr [rbp + 0xc8], rax
0086D496  48 8B 85 80 00 00 00            mov rax, qword ptr [rbp + 0x80]
0086D49D  48 89 85 C0 00 00 00            mov qword ptr [rbp + 0xc0], rax
0086D4A4  E8 17 A7 13 00                  call 0x1409a7bc0
0086D4A9  0F 57 C0                        xorps xmm0, xmm0
0086D4AC  49 8B C7                        mov rax, r15
0086D4AF  48 C1 E8 08                     shr rax, 8
0086D4B3  BF 9A 00 00 C0                  mov edi, 0xc000009a
0086D4B8  0F B6 C8                        movzx ecx, al
0086D4BB  41 0F B6 47 18                  movzx eax, byte ptr [r15 + 0x18]
0086D4C0  48 33 C8                        xor rcx, rax
0086D4C3  0F B6 05 82 99 75 00            movzx eax, byte ptr [rip + 0x759982]
0086D4CA  48 33 C8                        xor rcx, rax
0086D4CD  48 8D 05 2C 2B 79 FF            lea rax, [rip - 0x86d4d4]
0086D4D4  0F 11 85 48 01 00 00            movups xmmword ptr [rbp + 0x148], xmm0
0086D4DB  0F 11 85 58 01 00 00            movups xmmword ptr [rbp + 0x158], xmm0
0086D4E2  48 8B 9C C8 00 78 FC 00         mov rbx, qword ptr [rax + rcx*8 + 0xfc7800]
0086D4EA  33 C9                           xor ecx, ecx
0086D4EC  0F 11 85 68 01 00 00            movups xmmword ptr [rbp + 0x168], xmm0
0086D4F3  89 4D C8                        mov dword ptr [rbp - 0x38], ecx
0086D4F6  F6 43 42 10                     test byte ptr [rbx + 0x42], 0x10
0086D4FA  0F 85 51 01 00 00               jne 0x14086d651
0086D500  41 F6 47 1B 08                  test byte ptr [r15 + 0x1b], 8
0086D505  0F 85 46 01 00 00               jne 0x14086d651
0086D50B  48 C7 C6 FF FF FF FF            mov rsi, 0xffffffffffffffff
0086D512  F0 49 0F C1 77 08               lock xadd qword ptr [r15 + 8], rsi
0086D518  48 83 BB 80 00 00 00 00         cmp qword ptr [rbx + 0x80], 0
0086D520  0F 84 87 00 00 00               je 0x14086d5ad
0086D526  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086D52F  48 89 4D B8                     mov qword ptr [rbp - 0x48], rcx
0086D533  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
0086D537  C6 45 80 00                     mov byte ptr [rbp - 0x80], 0
0086D53B  48 39 88 B8 00 00 00            cmp qword ptr [rax + 0xb8], rcx
0086D542  74 29                           je 0x14086d56d
0086D544  C6 45 80 01                     mov byte ptr [rbp - 0x80], 1
0086D548  E8 93 E9 BD FF                  call 0x14044bee0
0086D54D  48 8B C8                        mov rcx, rax
0086D550  E8 6B 53 BD FF                  call 0x1404428c0
0086D555  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
0086D559  48 8D 95 48 01 00 00            lea rdx, [rbp + 0x148]
0086D560  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
0086D564  E8 97 92 9A FF                  call 0x140216800
0086D569  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
0086D56D  48 8B 83 80 00 00 00            mov rax, qword ptr [rbx + 0x80]
0086D574  48 8D 15 55 65 FF FF            lea rdx, [rip - 0x9aab]
0086D57B  44 8B 45 C8                     mov r8d, dword ptr [rbp - 0x38]
0086D57F  48 3B C2                        cmp rax, rdx
0086D582  75 5A                           jne 0x14086d5de
0086D584  4C 8B CE                        mov r9, rsi
0086D587  49 8D 57 30                     lea rdx, [r15 + 0x30]
0086D58B  E8 40 65 FF FF                  call 0x140863ad0
0086D590  80 7D 80 00                     cmp byte ptr [rbp - 0x80], 0
0086D594  74 17                           je 0x14086d5ad
0086D596  33 D2                           xor edx, edx
0086D598  48 8D 8D 48 01 00 00            lea rcx, [rbp + 0x148]
0086D59F  E8 8C A7 9A FF                  call 0x140217d30
0086D5A4  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
0086D5A8  E8 13 C5 BD FF                  call 0x140449ac0
0086D5AD  48 83 FE 01                     cmp rsi, 1
0086D5B1  75 08                           jne 0x14086d5bb
0086D5B3  49 8B CF                        mov rcx, r15
0086D5B6  E8 35 CE 02 00                  call 0x14089a3f0
0086D5BB  F0 FF 4B 30                     lock dec dword ptr [rbx + 0x30]
0086D5BF  45 85 ED                        test r13d, r13d
0086D5C2  0F 84 DA ED FF FF               je 0x14086c3a2
0086D5C8  41 B8 44 66 6C 74               mov r8d, 0x746c6644
0086D5CE  41 8B D5                        mov edx, r13d
0086D5D1  49 8B CC                        mov rcx, r12
0086D5D4  E8 E7 F5 BC FF                  call 0x14043cbc0
0086D5D9  E9 C4 ED FF FF                  jmp 0x14086c3a2
0086D5DE  48 8D 15 CB F8 19 00            lea rdx, [rip + 0x19f8cb]
0086D5E5  48 3B C2                        cmp rax, rdx
0086D5E8  0F 85 9A 01 00 00               jne 0x14086d788
0086D5EE  48 83 FE 01                     cmp rsi, 1
0086D5F2  75 9C                           jne 0x14086d590
0086D5F4  41 F6 87 92 00 00 00 02         test byte ptr [r15 + 0x92], 2
0086D5FC  74 44                           je 0x14086d642
0086D5FE  48 8B 0D 3B 22 69 00            mov rcx, qword ptr [rip + 0x69223b]
0086D605  48 8D 15 7C 32 7A FF            lea rdx, [rip - 0x85cd84]
0086D60C  E8 3F 4E B2 FF                  call 0x140392450
0086D611  84 C0                           test al, al
0086D613  74 2D                           je 0x14086d642
0086D615  49 8B 47 50                     mov rax, qword ptr [r15 + 0x50]
0086D619  48 8D 15 68 32 7A FF            lea rdx, [rip - 0x85cd98]
0086D620  48 8B 0D 19 22 69 00            mov rcx, qword ptr [rip + 0x692219]
0086D627  48 83 C0 28                     add rax, 0x28
0086D62B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0086D630  44 8B CE                        mov r9d, esi
0086D633  33 C0                           xor eax, eax
0086D635  45 33 C0                        xor r8d, r8d
0086D638  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0086D63D  E8 D6 66 FF FF                  call 0x140863d18
0086D642  66 F0 41 83 8F 92 00 00 00 20   lock or word ptr [r15 + 0x92], 0x20
0086D64C  E9 3F FF FF FF                  jmp 0x14086d590
0086D651  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086D65A  49 8D 4F 10                     lea rcx, [r15 + 0x10]
0086D65E  45 33 C0                        xor r8d, r8d
0086D661  33 D2                           xor edx, edx
0086D663  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0086D66A  90                              nop
0086D66B  E8 C0 2B 9A FF                  call 0x140210230
0086D670  F0 49 0F BA 6F 10 00            lock bts qword ptr [r15 + 0x10], 0
0086D677  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
0086D67B  73 14                           jae 0x14086d691
0086D67D  4D 8D 47 10                     lea r8, [r15 + 0x10]
0086D681  48 8B D0                        mov rdx, rax
0086D684  49 8D 4F 10                     lea rcx, [r15 + 0x10]
0086D688  E8 03 26 9A FF                  call 0x14020fc90
0086D68D  48 8B 45 E0                     mov rax, qword ptr [rbp - 0x20]
0086D691  48 85 C0                        test rax, rax
0086D694  74 04                           je 0x14086d69a
0086D696  C6 40 0A 01                     mov byte ptr [rax + 0xa], 1
0086D69A  49 8B 77 08                     mov rsi, qword ptr [r15 + 8]
0086D69E  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
0086D6A5  F0 49 0F C1 47 08               lock xadd qword ptr [r15 + 8], rax
0086D6AB  48 8D 15 4E 29 79 FF            lea rdx, [rip - 0x86d6b2]
0086D6B2  48 83 E8 01                     sub rax, 1
0086D6B6  0F 85 ED 00 00 00               jne 0x14086d7a9
0086D6BC  41 0F B6 47 1B                  movzx eax, byte ptr [r15 + 0x1b]
0086D6C1  A8 08                           test al, 8
0086D6C3  0F 84 E0 00 00 00               je 0x14086d7a9
0086D6C9  41 0F B6 47 1A                  movzx eax, byte ptr [r15 + 0x1a]
0086D6CE  49 8B CF                        mov rcx, r15
0086D6D1  83 E0 1F                        and eax, 0x1f
0086D6D4  0F B6 84 10 80 FF F0 00         movzx eax, byte ptr [rax + rdx + 0xf0ff80]
0086D6DC  48 2B C8                        sub rcx, rax
0086D6DF  45 33 D2                        xor r10d, r10d
0086D6E2  4C 89 11                        mov qword ptr [rcx], r10
0086D6E5  0F B6 43 42                     movzx eax, byte ptr [rbx + 0x42]
0086D6E9  A8 10                           test al, 0x10
0086D6EB  74 4E                           je 0x14086d73b
0086D6ED  41 0F B6 47 1A                  movzx eax, byte ptr [r15 + 0x1a]
0086D6F2  A8 04                           test al, 4
0086D6F4  0F 85 B7 00 00 00               jne 0x14086d7b1
0086D6FA  4D 8B C2                        mov r8, r10
0086D6FD  41 F6 47 1B 40                  test byte ptr [r15 + 0x1b], 0x40
0086D702  0F 84 BF 00 00 00               je 0x14086d7c7
0086D708  41 8B 50 08                     mov edx, dword ptr [r8 + 8]
0086D70C  8B CA                           mov ecx, edx
0086D70E  81 E2 FF FF FF 00               and edx, 0xffffff
0086D714  89 55 C8                        mov dword ptr [rbp - 0x38], edx
0086D717  8D 41 FF                        lea eax, [rcx - 1]
0086D71A  33 C1                           xor eax, ecx
0086D71C  25 FF FF FF 00                  and eax, 0xffffff
0086D721  33 C1                           xor eax, ecx
0086D723  41 89 40 08                     mov dword ptr [r8 + 8], eax
0086D727  41 80 78 0B 00                  cmp byte ptr [r8 + 0xb], 0
0086D72C  75 0D                           jne 0x14086d73b
0086D72E  41 F7 40 08 FF FF FF 00         test dword ptr [r8 + 8], 0xffffff
0086D736  75 03                           jne 0x14086d73b
0086D738  4D 89 10                        mov qword ptr [r8], r10
0086D73B  49 8D 57 10                     lea rdx, [r15 + 0x10]
0086D73F  0F 0D 0A                        prefetchw byte ptr [rdx]
0086D742  48 8B 02                        mov rax, qword ptr [rdx]
0086D745  48 8B C8                        mov rcx, rax
0086D748  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0086D74C  48 83 F9 10                     cmp rcx, 0x10
0086D750  4C 8D 40 F0                     lea r8, [rax - 0x10]
0086D754  4D 0F 46 C2                     cmovbe r8, r10
0086D758  A8 02                           test al, 2
0086D75A  0F 85 AA 00 00 00               jne 0x14086d80a
0086D760  F0 4C 0F B1 02                  lock cmpxchg qword ptr [rdx], r8
0086D765  0F 85 9F 00 00 00               jne 0x14086d80a
0086D76B  48 8B CA                        mov rcx, rdx
0086D76E  E8 8D 3E A7 FF                  call 0x1402e1600
0086D773  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086D77C  E8 6F 18 9F FF                  call 0x14025eff0
0086D781  33 C9                           xor ecx, ecx
0086D783  E9 90 FD FF FF                  jmp 0x14086d518
0086D788  48 8D 15 31 69 FF FF            lea rdx, [rip - 0x96cf]
0086D78F  4C 8B CE                        mov r9, rsi
0086D792  48 3B C2                        cmp rax, rdx
0086D795  49 8D 57 30                     lea rdx, [r15 + 0x30]
0086D799  0F 85 7C 00 00 00               jne 0x14086d81b
0086D79F  E8 1C 69 FF FF                  call 0x1408640c0
0086D7A4  E9 E7 FD FF FF                  jmp 0x14086d590
0086D7A9  45 33 D2                        xor r10d, r10d
0086D7AC  E9 34 FF FF FF                  jmp 0x14086d6e5
0086D7B1  83 E0 07                        and eax, 7
0086D7B4  4D 8B C7                        mov r8, r15
0086D7B7  0F B6 84 10 80 FF F0 00         movzx eax, byte ptr [rax + rdx + 0xf0ff80]
0086D7BF  4C 2B C0                        sub r8, rax
0086D7C2  E9 36 FF FF FF                  jmp 0x14086d6fd
0086D7C7  49 8B 00                        mov rax, qword ptr [r8]
0086D7CA  4C 8B 4D 98                     mov r9, qword ptr [rbp - 0x68]
0086D7CE  8B 08                           mov ecx, dword ptr [rax]
0086D7D0  4C 8D 40 08                     lea r8, [rax + 8]
0086D7D4  85 C9                           test ecx, ecx
0086D7D6  0F 84 4B FF FF FF               je 0x14086d727
0086D7DC  41 8B 50 08                     mov edx, dword ptr [r8 + 8]
0086D7E0  8B C2                           mov eax, edx
0086D7E2  25 FF FF FF 00                  and eax, 0xffffff
0086D7E7  74 05                           je 0x14086d7ee
0086D7E9  4D 39 08                        cmp qword ptr [r8], r9
0086D7EC  74 08                           je 0x14086d7f6
0086D7EE  49 83 C0 10                     add r8, 0x10
0086D7F2  FF C9                           dec ecx
0086D7F4  EB DE                           jmp 0x14086d7d4
0086D7F6  89 45 C8                        mov dword ptr [rbp - 0x38], eax
0086D7F9  8D 42 FF                        lea eax, [rdx - 1]
0086D7FC  33 C2                           xor eax, edx
0086D7FE  25 FF FF FF 00                  and eax, 0xffffff
0086D803  33 C2                           xor eax, edx
0086D805  E9 19 FF FF FF                  jmp 0x14086d723
0086D80A  48 8B CA                        mov rcx, rdx
0086D80D  E8 BE 60 9F FF                  call 0x1402638d0
0086D812  49 8D 57 10                     lea rdx, [r15 + 0x10]
0086D816  E9 50 FF FF FF                  jmp 0x14086d76b
0086D81B  E8 B0 D2 E4 FF                  call 0x1406baad0
0086D820  E9 6B FD FF FF                  jmp 0x14086d590
0086D825  33 D2                           xor edx, edx
0086D827  48 8B CB                        mov rcx, rbx
0086D82A  E8 41 50 31 00                  call 0x140b82870
0086D82F  8B 45 B0                        mov eax, dword ptr [rbp - 0x50]
0086D832  B9 00 01 00 00                  mov ecx, 0x100
0086D837  8B D0                           mov edx, eax
0086D839  89 05 4D DB 59 00               mov dword ptr [rip + 0x59db4d], eax
0086D83F  41 B8 4F 62 53 71               mov r8d, 0x7153624f
0086D845  E8 A6 48 31 00                  call 0x140b820f0
0086D84A  48 8B D8                        mov rbx, rax
0086D84D  48 85 C0                        test rax, rax
0086D850  0F 84 47 01 00 00               je 0x14086d99d
0086D856  49 8B 85 98 00 00 00            mov rax, qword ptr [r13 + 0x98]
0086D85D  49 8D 4D 4C                     lea rcx, [r13 + 0x4c]
0086D861  44 88 7C 24 40                  mov byte ptr [rsp + 0x40], r15b
0086D866  4C 8D 45 C0                     lea r8, [rbp - 0x40]
0086D86A  48 89 4C 24 38                  mov qword ptr [rsp + 0x38], rcx
0086D86F  4C 8B CB                        mov r9, rbx
0086D872  41 8B 4D 64                     mov ecx, dword ptr [r13 + 0x64]
0086D876  BA 01 00 00 00                  mov edx, 1
0086D87B  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0086D87F  48 8B 4D B8                     mov rcx, qword ptr [rbp - 0x48]
0086D883  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
0086D888  48 8D 4D B0                     lea rcx, [rbp - 0x50]
0086D88C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0086D891  49 8B CC                        mov rcx, r12
0086D894  C6 45 80 01                     mov byte ptr [rbp - 0x80], 1
0086D898  E8 33 D2 E4 FF                  call 0x1406baad0
0086D89D  8B F8                           mov edi, eax
0086D89F  E9 AC EC FF FF                  jmp 0x14086c550
0086D8A4  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086D8AD  E8 3E 17 9F FF                  call 0x14025eff0
0086D8B2  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
0086D8B9  BA 4F 62 43 62                  mov edx, 0x6243624f
0086D8BE  E8 1D A0 A8 FF                  call 0x1402f78e0
0086D8C3  E9 E1 FB FF FF                  jmp 0x14086d4a9
0086D8C8  B8 08 00 00 00                  mov eax, 8
0086D8CD  45 85 C0                        test r8d, r8d
0086D8D0  0F 84 99 00 00 00               je 0x14086d96f
0086D8D6  43 8D 04 40                     lea eax, [r8 + r8*2]
0086D8DA  8D 0C 85 08 00 00 00            lea ecx, [rax*4 + 8]
0086D8E1  B8 08 00 00 00                  mov eax, 8
0086D8E6  48 85 FF                        test rdi, rdi
0086D8E9  74 10                           je 0x14086d8fb
0086D8EB  85 D2                           test edx, edx
0086D8ED  74 0E                           je 0x14086d8fd
0086D8EF  8D 04 52                        lea eax, [rdx + rdx*2]
0086D8F2  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
0086D8F9  EB 02                           jmp 0x14086d8fd
0086D8FB  33 C0                           xor eax, eax
0086D8FD  8D 14 01                        lea edx, [rcx + rax]
0086D900  41 B8 53 65 50 72               mov r8d, 0x72506553
0086D906  B9 00 01 00 00                  mov ecx, 0x100
0086D90B  E8 E0 47 31 00                  call 0x140b820f0
0086D910  48 89 45 F8                     mov qword ptr [rbp - 8], rax
0086D914  48 8B C8                        mov rcx, rax
0086D917  48 85 C0                        test rax, rax
0086D91A  0F 84 F2 E2 FF FF               je 0x14086bc12
0086D920  48 8B 7D B8                     mov rdi, qword ptr [rbp - 0x48]
0086D924  48 8B 17                        mov rdx, qword ptr [rdi]
0086D927  48 85 D2                        test rdx, rdx
0086D92A  74 4A                           je 0x14086d976
0086D92C  8B 02                           mov eax, dword ptr [rdx]
0086D92E  85 C0                           test eax, eax
0086D930  74 75                           je 0x14086d9a7
0086D932  8D 04 40                        lea eax, [rax + rax*2]
0086D935  8D 04 85 08 00 00 00            lea eax, [rax*4 + 8]
0086D93C  44 8B C0                        mov r8d, eax
0086D93F  E8 FC 8E E5 FF                  call 0x1406c6840
0086D944  4D 8B C4                        mov r8, r12
0086D947  4C 8B 65 F8                     mov r12, qword ptr [rbp - 8]
0086D94B  49 8B CC                        mov rcx, r12
0086D94E  E8 7D A1 16 00                  call 0x1409d7ad0
0086D953  80 7E 0B 00                     cmp byte ptr [rsi + 0xb], 0
0086D957  74 0A                           je 0x14086d963
0086D959  48 8B 0F                        mov rcx, qword ptr [rdi]
0086D95C  33 D2                           xor edx, edx
0086D95E  E8 0D 4F 31 00                  call 0x140b82870
0086D963  4C 89 27                        mov qword ptr [rdi], r12
0086D966  C6 46 0B 01                     mov byte ptr [rsi + 0xb], 1
0086D96A  E9 A3 E2 FF FF                  jmp 0x14086bc12
0086D96F  8B C8                           mov ecx, eax
0086D971  E9 70 FF FF FF                  jmp 0x14086d8e6
0086D976  33 C0                           xor eax, eax
0086D978  EB C2                           jmp 0x14086d93c
0086D97A  48 8D 4D B0                     lea rcx, [rbp - 0x50]
0086D97E  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0086D983  49 8B CC                        mov rcx, r12
0086D986  E8 45 D1 E4 FF                  call 0x1406baad0
0086D98B  E9 B3 EB FF FF                  jmp 0x14086c543
0086D990  48 8B CF                        mov rcx, rdi
0086D993  E8 38 84 9F FF                  call 0x140265dd0
0086D998  E9 8E F7 FF FF                  jmp 0x14086d12b
0086D99D  BF 9A 00 00 C0                  mov edi, 0xc000009a
0086D9A2  E9 CB F5 FF FF                  jmp 0x14086cf72
0086D9A7  B8 08 00 00 00                  mov eax, 8
0086D9AC  EB 8E                           jmp 0x14086d93c
0086D9AE  8B 7D B4                        mov edi, dword ptr [rbp - 0x4c]
0086D9B1  E9 BF F5 FF FF                  jmp 0x14086cf75
0086D9B6  8B 45 C8                        mov eax, dword ptr [rbp - 0x38]
0086D9B9  45 33 C9                        xor r9d, r9d
0086D9BC  8B 4D 08                        mov ecx, dword ptr [rbp + 8]
0086D9BF  4C 8B 45 90                     mov r8, qword ptr [rbp - 0x70]
0086D9C3  8B 5D 00                        mov ebx, dword ptr [rbp]
0086D9C6  FF C0                           inc eax
0086D9C8  FF C3                           inc ebx
0086D9CA  89 45 C8                        mov dword ptr [rbp - 0x38], eax
0086D9CD  3B D9                           cmp ebx, ecx
0086D9CF  41 8B C1                        mov eax, r9d
0086D9D2  0F 45 C3                        cmovne eax, ebx
0086D9D5  8B D8                           mov ebx, eax
0086D9D7  89 45 00                        mov dword ptr [rbp], eax
0086D9DA  8B 45 C8                        mov eax, dword ptr [rbp - 0x38]
0086D9DD  E9 7D E6 FF FF                  jmp 0x14086c05f
0086D9E2  48 8B 8D 78 01 00 00            mov rcx, qword ptr [rbp + 0x178]
0086D9E9  48 33 CC                        xor rcx, rsp
0086D9EC  E8 4F EC E3 FF                  call 0x1406ac640
0086D9F1  48 81 C4 A8 02 00 00            add rsp, 0x2a8
0086D9F8  41 5F                           pop r15
0086D9FA  41 5E                           pop r14
0086D9FC  41 5D                           pop r13
0086D9FE  41 5C                           pop r12
0086DA00  5F                              pop rdi
0086DA01  5E                              pop rsi
0086DA02  5B                              pop rbx
0086DA03  5D                              pop rbp
0086DA04  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObpCreateHandle(int a1, __int64 a2, int a3, __int64 a4, unsigned int a5, unsigned int a6, unsigned __int8 a7, __int64 a8, unsigned int a9, __int64 a10, __int64 a11)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned int v_stack_m10C;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned int v_stack_m14C;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m184;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned int v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned int v_stack_m1D0;
    unsigned int v_stack_m1D8;
    unsigned int v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned int v_stack_m200;
    unsigned int v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned int v_stack_m214;
    unsigned int v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int8 v_stack_m240;
    unsigned int v_stack_m244;
    unsigned __int8 v_stack_m245;
    unsigned __int8 v_stack_m246;
    unsigned __int8 v_stack_m248;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned int v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned int v_stack_m280;
    unsigned __int64 v_stack_m288;
    unsigned __int8 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned __int8 v_stack_m2B0;
    unsigned __int64 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned int v_stack_m2C8;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned int v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m94;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mAC;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned int v_stack_mDC;
    unsigned int v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned __int64 v_stack_mEC;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;

    v_rsp = (v_rsp) - (680);
    result = (*(unsigned __int64 *)(v_rip + 5893581)) ^ (v_rsp);
    v_stack_m50 = result;
    a4 = 0;
    v_stack_m118 = a10;
    v_stack_m128 = a11;
    v_stack_m244 = 0;
    v_stack_m188 = 0;
    v_stack_m184 = (unsigned int)((unsigned int)(a9));
    v_stack_m228 = a2;
    v_stack_m1E0 = a1;
    v_stack_m220 = a8;
    v_stack_m1B0 = 0;
    v_stack_m246 = 0;
    v_stack_m1A8 = 0;
    v_stack_m240 = 0;
    v_stack_m1F8 = v_xmm0;
    v_stack_m230 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    if (condition_is_below) goto loc_0086C4A2;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 586)) == 1) goto loc_0086C560;
loc_0086BA34:
    v_stack_m238 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 768);
loc_0086BA38:
    result = ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 768)) == (*(unsigned __int64 *)(v_rip + 6962041))) ? 1 : 0;
    v_stack_m245 = (unsigned __int8)(result);
    if (0 == 0) goto loc_0086C5F1;
    if ((unsigned __int8)(result) != 0) goto loc_0086C5E7;
loc_0086BA56:
    v_stack_m214 = 0;
    v_r15 = 1;
    if (condition_is_above_or_equal) { v_r15 = a7; }
    if (((unsigned int)((unsigned int)(a1) - 1)) > 1) goto loc_0086BCF3;
    result = (a2 - 48) >> (8);
    a1 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(a2 - 24));
    v_stack_m1A0 = 0;
    a1 = (a1) ^ (*(unsigned __int8 *)(v_rip + 7713712));
    v_stack_m160 = 0;
    v_stack_m218 = 0;
    v_stack_m208 = 0;
    v_stack_m1C0 = *(unsigned __int64 *)(v_rip - 8829610 + a1 * 8 + 16545792);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8829610 + a1 * 8 + 16545792) + 152)) != (v_rip + 321519)) goto loc_0086C4B9;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2 - 8))) & (15)) == 0) goto loc_0086BAF9;
loc_0086BAE2:
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2 - 8))) & (15)) == 0) goto loc_0086BAF9;
    if ((((unsigned __int8)(*(unsigned __int64 *)(a2 - 8))) & (15)) != 0) goto loc_0086BAE2;
loc_0086BAF9:
    a2 = (unsigned int)((*(unsigned __int64 *)(a2 - 8)) & (15));
    v_rbx = (*(unsigned __int64 *)(a2 - 8)) & (-16);
    if (((unsigned int)(a2)) > 1) goto loc_0086BB11;
    if (v_rbx != 0) goto loc_0086D202;
loc_0086BB11:
    v_stack_m248 = 0;
    if (v_rbx == 0) goto loc_0086CC77;
loc_0086BB1E:
loc_0086BB21:
    if (v_rbx == 0) goto loc_0086C665;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 48) + 48), 1, a3, a4);
    if ((*(unsigned __int64 *)(a4 + 32)) != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a2 = 1;
        a1 = *(unsigned __int64 *)(a4 + 32);
        a1 = *(unsigned __int64 *)(a1 + 48);
        result = ExAcquireResourceSharedLite(a1, a2, a3, a4);
    }
    v_stack_m2A0 = v_stack_m214;
    v_stack_m2A8 = v_stack_m1A0;
    v_stack_m2B0 = (unsigned __int8)(v_r15);
    v_stack_m2B8 = *(unsigned __int64 *)(v_rip - 8829610 + a1 * 8 + 16545792) + 76;
    v_stack_m2C0 = v_stack_m160;
    v_stack_m2C8 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 20)));
    result = SeAccessCheck(v_rbx, a4 + 32, 1, (unsigned int)(*(unsigned int *)(a4 + 16)));
    if (v_stack_m160 == 0) goto loc_0086BC1B;
    v_stack_m210 = *(unsigned __int64 *)(a4 + 72);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 72)))) + (unsigned int)(*(unsigned int *)(v_stack_m160)) * 1)) > 3) goto loc_0086D8C8;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 72)) == 0) goto loc_0086C67B;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 72))))) != 0) goto loc_0086CE4E;
loc_0086BBF5:
    a1 = (8) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 72)));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m160)) + (unsigned int)(*(unsigned int *)(v_stack_m160)) * 2) << (2));
    result = memcpy(a1, v_stack_m160 + 8, a3, (unsigned int)(*(unsigned int *)(a4 + 16)));
loc_0086BC12:
    result = CmSiFreeMemory(v_stack_m160, v_stack_m160 + 8, a3, (unsigned int)(*(unsigned int *)(a4 + 16)));
loc_0086BC1B:
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_stack_m1A0;
        a1 = (unsigned int)(~(a1));
    }
    if ((unsigned __int8)(v_r15) != 0) {
        a1 = v_stack_m1C0;
        result = a4 + 10;
        v_stack_m2A0 = result;
        a1 = (a1) + (16);
        result = 0;
        a4 = v_rbx;
        v_stack_m2A8 = 0;
        a3 = 0;
        v_stack_m2B0 = (unsigned __int8)(v_r15);
        a2 = v_stack_m228;
        v_stack_m2B8 = (unsigned __int8)((unsigned __int8)(result));
        v_stack_m2C0 = 0;
        v_stack_m2C8 = a4;
        result = SeOpenObjectAuditAlarmWithTransaction(a1, a2, a3, a4);
    }
    result = ExReleaseResourceLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 48) + 48), a2, a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    if (*(unsigned __int64 *)(a4 + 32) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 32) + 48);
        result = ExReleaseResourceLite(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = KeLeaveCriticalRegionThread(a1, a2, a3, a4);
    }
    if (v_stack_m248 != 0) goto loc_0086C741;
loc_0086BCC1:
    a1 = (*(unsigned __int64 *)(v_stack_m228 - 8)) ^ (v_rbx);
    if (a1 >= 15) goto loc_0086D1F0;
    if (a1 != 15) goto loc_0086BCC1;
loc_0086BCDE:
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_0086D9AE;
    a4 = 0;
    goto loc_0086BE1B;
loc_0086BCF3:
    result = (*(unsigned __int64 *)(v_stack_m228 - 8)) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(v_stack_m228 - 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 7713090));
    if (!(condition_is_above_or_equal)) {
        *(unsigned int *)(a4 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)));
    }
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(a4 + 16)))) & (0xF0000000ULL)) == 0) goto loc_0086BD61;
    result = (unsigned int)(*(unsigned int *)(a4 + 16));
    if (sign_flag) {
        result = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 16))) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip - 8830228 + a2 * 8 + 16545792) + 76)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (unsigned int)((result) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip - 8830228 + a2 * 8 + 16545792) + 80)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (unsigned int)((result) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip - 8830228 + a2 * 8 + 16545792) + 84)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (unsigned int)((result) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip - 8830228 + a2 * 8 + 16545792) + 88)));
    }
    result = (unsigned int)((result) & (0xFFFFFFFULL));
    *(unsigned int *)(a4 + 16) = (unsigned int)(result);
loc_0086BD61:
    if (condition_is_below) goto loc_0086CD3D;
loc_0086BD6B:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a4 + 16))) | (*(unsigned int *)(a4 + 20)));
    *(unsigned int *)(a4 + 20) = a1;
    *(unsigned int *)(a4 + 16) = 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 8830228 + a2 * 8 + 16545792) + 92))) & (a1));
    *(unsigned int *)(a4 + 20) = (unsigned int)(result);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m228 - 8))) & (15)) == 0) goto loc_0086BDB7;
loc_0086BDA0:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m228 - 8))) & (15)) == 0) goto loc_0086BDB7;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m228 - 8))) & (15)) != 0) goto loc_0086BDA0;
loc_0086BDB7:
    a2 = (unsigned int)((*(unsigned __int64 *)(v_stack_m228 - 8)) & (15));
    v_rdi = (*(unsigned __int64 *)(v_stack_m228 - 8)) & (-16);
    if (((unsigned int)(a2)) > 1) goto loc_0086BDCF;
    if (v_rdi != 0) goto loc_0086D048;
loc_0086BDCF:
    result = SeComputeCreatorDeniedRights(a4 + 32, 0, (unsigned int)(*(unsigned int *)(a4 + 20)), v_rdi);
    result = (unsigned int)(~(result));
    if (v_rdi == 0) goto loc_0086BE14;
loc_0086BDF7:
    a1 = (*(unsigned __int64 *)(v_stack_m228 - 8)) ^ (v_rdi);
    if (a1 >= 15) goto loc_0086CFF0;
    if (a1 != 15) goto loc_0086BDF7;
loc_0086BE14:
    a4 = 0;
    v_stack_m214 = 0;
loc_0086BE1B:
    v_stack_m244 = (unsigned int)((unsigned int)(*(unsigned int *)(a4 + 20)));
loc_0086BE25:
    v_stack_m180 = 0;
    result = 0;
    if (v_stack_m220 != 0) {
        result = *(unsigned __int64 *)(v_stack_m220 + 32);
        v_stack_m180 = result;
    }
    v_stack_m2B8 = result;
    v_stack_m2C0 = (unsigned int)((unsigned int)(a6));
    v_stack_m2C8 = a7;
    result = ObpIncrementHandleCountEx((unsigned int)(v_stack_m1E0), v_stack_m244, v_stack_m230, v_stack_m228);
    if (sign_flag) goto loc_0086C3A2;
    if (0 == 0) goto loc_0086C6AC;
    if (v_stack_m220 != 0) goto loc_0086CCEA;
loc_0086BE80:
    v_r14 = (unsigned int)(a6);
    if ((*(unsigned __int8 *)(a4 + 10)) != 0) {
        v_r14 = (unsigned int)(((unsigned int)(a6)) | (4));
    }
    result = (v_stack_m228 - 48) >> (8);
    a1 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(v_stack_m228 - 48 + 24));
    a1 = (a1) ^ (*(unsigned __int8 *)(v_rip + 7712673));
    v_stack_m210 = *(unsigned __int64 *)(v_rip - 8830645 + a1 * 8 + 16545792);
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m244)) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 8830645 + a1 * 8 + 16545792) + 92)))));
    v_stack_m244 = (unsigned int)(v_rbx);
    if (0 == 0) goto loc_0086C5DF;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m228 - 48 + 40))) & (15)) == 0) goto loc_0086BEFA;
loc_0086BEE4:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m228 - 48 + 40))) & (15)) == 0) goto loc_0086BEFA;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m228 - 48 + 40))) & (15)) != 0) goto loc_0086BEE4;
loc_0086BEFA:
    a2 = (unsigned int)((*(unsigned __int64 *)(v_stack_m228 - 48 + 40)) & (15));
    v_rbx = (*(unsigned __int64 *)(v_stack_m228 - 48 + 40)) & (-16);
    if (((unsigned int)(a2)) > 1) goto loc_0086BF12;
    if (v_rbx != 0) goto loc_0086D1DD;
loc_0086BF12:
    result = SeComputeCreatorDeniedRights(a4 + 32, 0, (unsigned int)(v_stack_m244), v_rbx);
    if (v_rbx == 0) goto loc_0086BF51;
loc_0086BF35:
    a1 = (*(unsigned __int64 *)(v_stack_m228 - 48 + 40)) ^ (v_rbx);
    if (a1 >= 15) goto loc_0086D1B8;
    if (a1 != 15) goto loc_0086BF35;
loc_0086BF51:
    v_rdi = (unsigned int)(~((unsigned int)((unsigned int)(result))));
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m244)) & ((unsigned int)(v_rdi)));
    v_stack_m244 = (unsigned int)(v_rbx);
    *(unsigned int *)(a4 + 20) = (unsigned int)(v_rbx);
    v_stack_m188 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 72) + 28)));
loc_0086BF6C:
    v_stack_m1D0 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 72) + 28)));
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 72) + 28));
    if ((unsigned int)((unsigned int)(a5)) != 0) {
        a3 = 0x746C6644ULL;
        a2 = (unsigned int)((unsigned int)(a5));
        a1 = v_stack_m228;
        result = ObReferenceObjectExWithTag(a1, a2, a3, v_rbx);
        v_rbx = v_stack_m244;
    }
    if (v_stack_m1B0 != 0) {
        a1 = v_stack_m1B0;
        result = ObfDereferenceObject(a1, a2, a3, v_rbx);
        v_rbx = v_stack_m244;
    }
    if (v_stack_m220 != 0) goto loc_0086CDD1;
loc_0086BFAE:
    v_stack_m1F0 = v_stack_m1F8;
    v_stack_m1F8 = v_stack_m1F8;
    if (((*(unsigned __int8 *)(v_stack_m210 + 66)) & (64)) != 0) goto loc_0086C750;
loc_0086BFC8:
    a4 = 0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (7));
    v_stack_m170 = 0;
    a1 = (a1) << (17);
    v_rbx = (unsigned int)((v_rbx) & (0x1FFFFFFULL));
    v_stack_m170 = (unsigned int)(v_rbx);
    result = (v_stack_m228 - 48) << (16);
    result = (result) & (0xFFFFFFFFFFF1FFFFULL);
    a1 = (a1) | (result);
    v_stack_m178 = a1;
    if ((((unsigned __int8)(v_r14)) & (8)) != 0) {
    }
    a1 = (a1) | (1);
    v_stack_m170 = (unsigned int)(v_rbx);
    v_stack_m178 = a1;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_m238 + 44))) & (4)) != 0) goto loc_0086C15F;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_m238 + 44))) & (1)) != 0) goto loc_0086CCB1;
loc_0086C042:
    v_stack_m1C8 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))))));
    v_stack_m1D8 = (unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))));
    v_stack_m1C0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 7789264)));
loc_0086C053:
    v_stack_m220 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m238)));
    v_stack_m200 = 0;
loc_0086C05F:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 7789264))))) goto loc_0086D0AA;
    v_rbx = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))))) + 1;
    v_rbx = (v_rbx) << (6);
    v_rbx = (v_rbx) + (v_stack_m238);
    if ((*(unsigned __int64 *)(v_rbx + 8)) == 0) goto loc_0086D9C3;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rbx, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rbx;
        a2 = result;
        a1 = v_rbx;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (*(unsigned __int64 *)(v_rbx + 8) == 0) goto loc_0086C0D2;
    *(unsigned __int64 *)(v_rbx + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8) + 8);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8) + 8) == 0) {
        *(unsigned __int64 *)(v_rbx + 16) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8) + 8);
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 24)))) >= = (*(unsigned int *)(v_rbx + 28))) {
        *(unsigned int *)(v_rbx + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + 24)));
    }
    result = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_0086CDC4;
loc_0086C0E8:
    result = KeAbPostRelease(v_rbx, a2, a3, a4);
    if (*(unsigned __int64 *)(v_rbx + 8) == 0) goto loc_0086D9B6;
    result = (*(unsigned __int64 *)(v_rbx + 8)) & (0xFFFFFFFFFFFFF000ULL);
    a1 = (*(unsigned __int64 *)(v_rbx + 8)) - (result);
    a1 = (a1) >> (4);
    if (v_stack_m1D0 != 0) goto loc_0086C454;
    if (a9 != 0) goto loc_0086C454;
loc_0086C135:
    result = (unsigned int)((unsigned int)(*(unsigned __int64 *)(result + 8) + a1 * 4));
    if ((*(unsigned __int64 *)(v_stack_m238 + 96)) != 0) {
        a4 = 1;
        a3 = *(unsigned __int64 *)(result + 8) + a1 * 4;
        a2 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = v_stack_m238;
        result = ExpUpdateDebugInfo(a1, a2, a3, a4);
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8) + 8) = v_stack_m170;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 8)) = v_stack_m178;
loc_0086C15F:
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    if (*(unsigned __int64 *)(result + 8) + a1 * 4 == 0) goto loc_0086CDF8;
    if ((unsigned int)((unsigned int)(a5)) == 0) goto loc_0086C186;
    if ((*(unsigned int *)(v_rip + 7704208)) != 0) goto loc_0086D05D;
loc_0086C186:
    if (a4 == 0) goto loc_0086C2A6;
    a2 = 0;
    v_stack_m1A8 = 0;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_m228 - 48 + 26))) & (32)) == 0) goto loc_0086C1BE;
    result = (unsigned int)((*(unsigned __int8 *)(v_stack_m228 - 48 + 26)) & (63));
    v_r12 = (v_stack_m228 - 48) - (*(unsigned __int8 *)(result + v_rip - 8831402 * 1 + 15794048));
    if (condition_is_not_equal) goto loc_0086CE76;
loc_0086C1BE:
    v_rbx = 0;
    if (v_stack_m180 != 0) { v_rbx = v_stack_m180; }
loc_0086C1C9:
    v_rdi = 0;
    v_stack_m190 = *(unsigned __int64 *)(result + 8) + a1 * 4;
    v_stack_m1B8 = 0;
    if (v_rbx != 0) goto loc_0086C1F0;
loc_0086C1E3:
    v_r12 = *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 72) + 56);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 72) + 56) == 0) {
        v_r12 = *(unsigned __int64 *)(a4 + 64);
    }
    if ((*(unsigned __int8 *)(a4 + 9)) != 0) goto loc_0086D3C8;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a4 + 72) + 216)) != 0) goto loc_0086D23F;
loc_0086C208:
    *(unsigned __int8 *)(a4 + 10) = 0;
    if ((unsigned int)((unsigned int)(v_stack_m1E0)) != 0) goto loc_0086C274;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 72)) == 0) goto loc_0086C274;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 72)))) <= ((unsigned int)((unsigned int)(v_stack_m1E0)))) goto loc_0086C274;
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != ((unsigned __int8)((unsigned int)(v_stack_m1E0)))) {
        result = *(unsigned int *)(a4 + 20);
        a1 = v_rip - 8826518;
        v_stack_m2A0 = 1;
        a4 = *(unsigned __int64 *)(result + 8) + a1 * 4;
        v_stack_m2A8 = *(unsigned __int64 *)(*(unsigned __int64 *)(a4 + 72));
        a3 = 0;
        v_stack_m2B0 = (unsigned int)(result);
        a2 = 0;
        result = *(unsigned __int64 *)(a4 + 56);
        v_stack_m2B8 = result;
        result = *(unsigned __int64 *)(a4 + 48);
        v_stack_m2C0 = result;
        result = *(unsigned __int64 *)(a4 + 32);
        v_stack_m2C8 = result;
        result = SepAdtPrivilegeObjectAuditAlarm(a1, a2, a3, a4);
    }
    if (v_stack_m1A8 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m1A8, a2, a3, a4);
    }
    if ((unsigned int)((unsigned int)(v_stack_m1E0)) != 0) goto loc_0086C2A6;
    if (v_stack_m210 != (*(unsigned __int64 *)(v_rip + 7710765))) goto loc_0086C69A;
loc_0086C299:
    if (*(unsigned __int64 *)(a4 + 32) != 0) goto loc_0086C6B5;
loc_0086C2A6:
loc_0086C2AA:
    if ((unsigned int)((unsigned int)(a5)) != 0) goto loc_0086C682;
loc_0086C2B3:
    v_rdi = (unsigned int)((v_rdi) & (0x40000000ULL));
    v_r14 = *(unsigned __int64 *)(result + 8) + a1 * 4;
    if ((unsigned __int8)(v_stack_m245) != 0) {
        v_r14 = (*(unsigned __int64 *)(result + 8) + a1 * 4) | (0xFFFFFFFF80000000ULL);
    }
    *(unsigned __int64 *)(v_stack_m128) = v_r14;
loc_0086C2D7:
    if (v_stack_m1F8 == v_stack_m1F8) goto loc_0086C394;
    a4 = 0;
    v_stack_mB8 = v_stack_m168;
    a1 = (unsigned int)((0) & (0xFFFFFFFEULL));
    v_stack_mBC = 0;
    a1 = (unsigned int)((a1) | ((unsigned int)((unsigned __int8)(v_stack_m245))));
    v_stack_mE0 = 1;
    v_stack_mDC = a1;
    result = (v_stack_m228 - 48) >> (8);
    a1 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(v_stack_m228 - 24));
    v_stack_mD8 = v_stack_m228;
    a1 = (a1) ^ (*(unsigned __int8 *)(v_rip + 7711504));
    v_stack_mC8 = 0;
    v_stack_mC0 = (unsigned int)(v_rdi);
    v_stack_mD0 = *(unsigned __int64 *)(v_rip - 8831821 + a1 * 8 + 16545792);
    v_stack_m168 = (unsigned int)((unsigned int)(v_stack_m244));
loc_0086C368:
    if (v_stack_m1F8 != v_stack_m1F8) goto loc_0086C3D4;
    result = ObfDereferenceObjectWithTag(v_stack_mD8, (unsigned int)(0x6243624FULL), v_stack_m1F8, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(0x6243624FULL), v_stack_m1F8, a4);
loc_0086C394:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 7710582)))) & (64)) != 0) goto loc_0086CFCF;
loc_0086C3A2:
loc_0086C3A6:
    if (v_stack_m240 == 0) goto loc_0086C3CC;
    result = (*(unsigned __int64 *)(v_stack_m230 + 488)) & (-2);
    if (condition_is_not_equal) goto loc_0086CCB9;
loc_0086C3CC:
    goto loc_0086D9E2;
loc_0086C3D4:
    if ((*(unsigned __int64 *)(v_stack_m1F0)) != v_stack_m1F8) goto loc_0086CAF9;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1F0 + 8))) != v_stack_m1F0) goto loc_0086CAF9;
    v_stack_m1F0 = *(unsigned __int64 *)(v_stack_m1F0 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1F0 + 8)) = v_stack_m1F8;
    v_stack_mC8 = *(unsigned __int64 *)(v_stack_m1F0 + 24);
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1F0 + 16) + 24) + 8), v_stack_mE0, v_stack_m1F8, a4);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1F0 + 16) + 56)) & (-2);
    if (condition_is_not_equal) goto loc_0086CE33;
loc_0086C441:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m1F0, a2, v_stack_m1F8, a4);
    goto loc_0086C368;
loc_0086C454:
    a1 = (unsigned int)((v_stack_m1F0) & (0xFFFFFC03ULL));
    v_stack_m1D0 = v_r14;
    v_stack_m1D0 = a1;
    result = (unsigned int)((result) >> (2));
    v_stack_m220 = (unsigned int)((unsigned __int8)(result));
    result = ExpLookupHandleTableEntry(v_stack_m238, v_stack_m1D0, v_stack_m1F8, a4);
    if (result == 0) goto loc_0086CBA8;
    if (*(unsigned __int64 *)(result) == 0) goto loc_0086CB5B;
loc_0086C492:
    *(unsigned __int64 *)(*(unsigned __int64 *)(result) + (unsigned int)(v_stack_m220) * 8) = v_stack_m188;
    goto loc_0086C135;
loc_0086C4A2:
    v_stack_m230 = *(unsigned __int64 *)(v_rip + 7710215);
    goto loc_0086BA34;
loc_0086C4B9:
    v_stack_m208 = 447;
    v_stack_m218 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5893837)));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 5893837)))), (unsigned int)(0x7153624FULL), a4);
    if (result == 0) goto loc_0086D1D3;
    v_stack_m2A8 = (unsigned __int8)(v_stack_m128);
    v_stack_m2B0 = (unsigned int)(a5) + 76;
    v_stack_m2B8 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(a5) + 100)));
    v_stack_m2C0 = v_r12 - 8;
    v_stack_m210 = v_r12 - 8;
    v_stack_m248 = 1;
    if ((*(unsigned __int64 *)((unsigned int)(a5) + 152)) != (v_rip + 18361)) goto loc_0086D01F;
    v_stack_m2C8 = v_stack_m218;
    result = CmpSecurityMethod(v_r12, 1, v_stack_m208, result);
loc_0086C543:
    if (((unsigned int)(result)) == 0xC0000023ULL) goto loc_0086D825;
loc_0086C550:
    if (sign_flag) goto loc_0086CF68;
    a4 = 0;
    goto loc_0086BB21;
loc_0086C560:
    v_stack_m238 = 0;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7710215) + 488)) & (-2);
    if (condition_is_not_equal) goto loc_0086C5B7;
loc_0086C580:
    v_stack_m238 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7710215) + 768);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7710215) + 768) != 0) goto loc_0086C5D0;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7710215) + 488)) & (-2);
    if (condition_is_equal) goto loc_0086C5CB;
    result = ExfReleaseRundownProtection(*(unsigned __int64 *)(v_rip + 7710215) + 488, result - 2, v_stack_m208, a4);
loc_0086C5AD:
    goto loc_0086C3CC;
loc_0086C5B7:
    result = ExfAcquireRundownProtection((unsigned int)(0xC000010AULL), result - 2, v_stack_m208, a4);
    if ((unsigned __int8)(result) != 0) goto loc_0086C580;
loc_0086C5CB:
    if (v_stack_m238 == 0) goto loc_0086C5AD;
loc_0086C5D0:
    a4 = 0;
    v_stack_m240 = 1;
    goto loc_0086BA38;
loc_0086C5DF:
    goto loc_0086BF6C;
loc_0086C5E7:
    if ((*(unsigned int *)(v_stack_m1F0 + 24)) != 0) goto loc_0086BA56;
loc_0086C5F1:
    if ((*(unsigned int *)(v_stack_m1F0 + 24)) < 0) {
    }
    if ((((unsigned int)(result)) & (0xF0000000ULL)) == 0) goto loc_0086C65D;
    result = (v_r12 - 48) >> (8);
    a1 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(v_r12 - 24));
    a1 = (a1) ^ (*(unsigned __int8 *)(v_rip + 7710754));
    v_rbx = result;
    if (sign_flag) {
        v_rbx = (unsigned int)((result) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip - 8832518 + a1 * 8 + 16545792) + 76)));
    }
    if (!(condition_is_above_or_equal)) {
        v_rbx = (unsigned int)((v_rbx) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip - 8832518 + a1 * 8 + 16545792) + 80)));
    }
    if (!(condition_is_above_or_equal)) {
        v_rbx = (unsigned int)((v_rbx) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip - 8832518 + a1 * 8 + 16545792) + 84)));
    }
    if (!(condition_is_above_or_equal)) {
        v_rbx = (unsigned int)((v_rbx) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip - 8832518 + a1 * 8 + 16545792) + 88)));
    }
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFFULL));
loc_0086C65D:
    v_stack_m244 = (unsigned int)(v_rbx);
    goto loc_0086BE25;
loc_0086C665:
    *(unsigned int *)(v_stack_m1F0 + 16) = 0;
    v_stack_m214 = (unsigned int)((unsigned int)(0xC000010AULL));
    goto loc_0086BE1B;
loc_0086C67B:
    result = 0;
    goto loc_0086BBF5;
loc_0086C682:
    if (v_stack_m118 == 0) goto loc_0086C2B3;
    *(unsigned __int64 *)(v_stack_m118) = v_stack_m1F0;
    goto loc_0086C2B3;
loc_0086C69A:
    if (v_stack_m118 == (*(unsigned __int64 *)(v_rip + 7709759))) goto loc_0086C299;
    goto loc_0086C2A6;
loc_0086C6AC:
    goto loc_0086BE8A;
loc_0086C6B5:
    if ((*(unsigned __int64 *)(v_stack_m1F0 + 48)) >= v_rbx) goto loc_0086CB38;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1F0 + 48) + 48), 1, v_rip - 8832518, a4);
loc_0086C6F3:
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_rbx + 48), 1, v_rip - 8832518, a4);
    if (((*(unsigned int *)(v_rbx + 200)) & (0x4000ULL)) != 0) goto loc_0086CEDF;
loc_0086C70A:
loc_0086C70E:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1F0 + 48) + 48), 1, v_rip - 8832518, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), 1, v_rip - 8832518, a4);
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_rbx + 48), 1, v_rip - 8832518, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), 1, v_rip - 8832518, a4);
    goto loc_0086C2AA;
loc_0086C741:
    a2 = 0;
    result = ExFreePoolWithTag(v_rbx, a2, v_rip - 8832518, a4);
    goto loc_0086BCDE;
loc_0086C750:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1F0 + 48) + 200)) == (*(unsigned __int64 *)(v_stack_m1F0 + 48) + 200)) goto loc_0086BFC8;
    result = (v_r12 - 48) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(v_r12 - 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 7710413));
    v_stack_m110 = v_xmm0;
    v_stack_m100 = v_xmm0;
    a2 = 0;
    v_stack_m1C8 = 0;
    a1 = (unsigned int)((0) & (0xFFFFFFFEULL));
    v_stack_m1D8 = 0;
    v_stack_mF0 = v_xmm0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip - 8832905 + a2 * 8 + 16545792) + 96))) & ((unsigned int)(v_rbx)));
    v_stack_m148 = v_r12;
    v_stack_m138 = 0;
    v_stack_m1C0 = (unsigned int)(result);
    v_stack_m130 = v_stack_mB0;
    a1 = (unsigned int)((a1) | ((unsigned int)(v_stack_m245)));
    v_stack_m150 = 1;
    v_stack_m14C = a1;
    v_stack_mA8 = v_xmm0;
    v_stack_m140 = *(unsigned __int64 *)(v_rip - 8832905 + a2 * 8 + 16545792);
    v_stack_mAC = (unsigned int)(v_rbx);
    v_stack_mB0 = (unsigned int)(v_rbx);
    v_stack_m200 = *(unsigned __int64 *)(v_rip - 8832905 + a2 * 8 + 16545792) + 200;
    v_stack_m198 = *(unsigned __int64 *)(v_rip - 8832905 + a2 * 8 + 16545792);
    result = ObfReferenceObjectWithTag(v_stack_m148, (unsigned int)(0x6243624FULL), v_rip - 8832518, a4);
    a3 = 0;
    v_stack_m220 = *(unsigned __int64 *)(v_rip - 8832905 + a2 * 8 + 16545792) + 184;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(v_rip - 8832905 + a2 * 8 + 16545792) + 184, a2, a3, a4);
    result = 0;
    v_r10 = v_stack_m220;
    if (!(condition_is_equal)) {
        a4 = v_stack_m220;
        a3 = 0;
        a2 = 0;
        a1 = v_stack_m220;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
        v_r10 = v_stack_m220;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
loc_0086C894:
    if ((*(unsigned __int64 *)(v_stack_m200)) == v_stack_m200) goto loc_0086C9FD;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m200) + 20)))) & (1)) == 0) goto loc_0086C9ED;
    if (((v_stack_m150) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m200) + 16))))) == 0) goto loc_0086C9ED;
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m200) + 56)) & (-2);
    if (condition_is_not_equal) goto loc_0086D002;
loc_0086C8D1:
    a1 = (*(unsigned __int64 *)(v_r10)) & (-16);
    a2 = *(unsigned __int64 *)(v_r10) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r10))) & (2)) != 0) goto loc_0086CCA0;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r10))) & (2)) != 0) goto loc_0086CCA0;
loc_0086C903:
    result = KeAbPostRelease(v_r10, a2, a3, a4);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_r10))) & (2)) != 0) goto loc_0086C931;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    }
    if (v_stack_m1D8 == 0) goto loc_0086C959;
    result = (*(unsigned __int64 *)(v_stack_m1D8)) & (-2);
    if (condition_is_not_equal) goto loc_0086D0A0;
loc_0086C953:
    result = 0;
    v_stack_m1D8 = 0;
loc_0086C959:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m200) + 48)) != 0) goto loc_0086CABC;
loc_0086C964:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m200) + 40) == 0) goto loc_0086C99A;
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m200) + 24) + 8), v_stack_m150, a3, a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m200) + 48)) != 0) goto loc_0086CB24;
    v_stack_m1D8 = *(unsigned __int64 *)(v_stack_m200) + 56;
loc_0086C991:
    result = 0;
    v_stack_m138 = 0;
loc_0086C99A:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_m220, a2, a3, a4);
    v_stack_m1E8 = result;
    result = 0;
    if (!(condition_is_equal)) {
        a3 = 0;
        a4 = v_stack_m220;
        a2 = 0;
        result = ExfAcquirePushLockSharedEx(v_stack_m220, a2, a3, a4);
        a2 = v_stack_m1E8;
    }
    if (a2 != 0) {
        *(unsigned __int8 *)(a2 + 10) = 1;
    }
    goto loc_0086C894;
loc_0086C9FD:
    v_rdi = (v_stack_m198) + (184);
    a1 = (*(unsigned __int64 *)(v_rdi)) & (-16);
    a2 = *(unsigned __int64 *)(v_rdi) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (2)) != 0) goto loc_0086CCDD;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (2)) != 0) goto loc_0086CCDD;
loc_0086CA39:
    result = KeAbPostRelease(v_rdi, a2, a3, a4);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (2)) != 0) goto loc_0086CA67;
    result = *(unsigned __int64 *)(gs_base + (0 + 392)) + 152;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) != (*(unsigned __int64 *)(gs_base + (0 + 392)) + 152)) {
        result = KiCheckForKernelApcDelivery(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    }
    if (v_stack_m1D8 == 0) goto loc_0086CA89;
    result = (*(unsigned __int64 *)(v_stack_m1D8)) & (-2);
    if (condition_is_not_equal) goto loc_0086D16F;
loc_0086CA89:
    if (v_stack_m1F8 == v_stack_m1F8) goto loc_0086CB00;
loc_0086CA93:
    if (v_stack_m245 != 0) goto loc_0086D423;
    result = (unsigned int)(((unsigned int)(v_stack_mB0)) | (v_stack_m1C0));
    v_rbx = (unsigned int)((v_rbx) & ((unsigned int)(result)));
    v_stack_m244 = (unsigned int)(v_rbx);
    if (v_stack_m228 == 0) goto loc_0086BFC8;
    *(unsigned int *)(v_stack_m228 + 20) = (unsigned int)(v_rbx);
    goto loc_0086BFC8;
loc_0086CABC:
    result = ExAllocatePool2(256, 32, (unsigned int)(0x6C46624FULL), a4);
    v_stack_m1C8 = result;
    if (result == 0) goto loc_0086D434;
    a1 = 0;
    *(unsigned __int64 *)(result + 16) = v_rdi;
    *(unsigned __int64 *)(result + 24) = 0;
    if ((*(unsigned __int64 *)(v_stack_m1F0)) == v_stack_m1F8) goto loc_0086D1A1;
loc_0086CAF9:
loc_0086CB00:
    result = ObfDereferenceObjectWithTag(v_stack_m148, (unsigned int)(0x6243624FULL), (unsigned int)(0x6C46624FULL), a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(0x6243624FULL), (unsigned int)(0x6C46624FULL), a4);
    goto loc_0086CA93;
loc_0086CB24:
    *(unsigned __int64 *)(v_stack_m1C8 + 24) = v_stack_m138;
    goto loc_0086C991;
loc_0086CB38:
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_rbx + 48), (unsigned int)(0x6243624FULL), (unsigned int)(0x6C46624FULL), a4);
    goto loc_0086C6F3;
loc_0086CB5B:
    result = ExpAllocateTablePagedPool(*(unsigned __int64 *)(v_stack_m220 + 16), (unsigned int)(0x800ULL), (unsigned int)(0x6C46624FULL), a4);
    if (result == 0) goto loc_0086D1CA;
    result = 0;
    if (condition_is_equal) goto loc_0086CE5D;
    result = ExpFreeTablePagedPool(*(unsigned __int64 *)(v_stack_m238 + 16), 0, (unsigned int)(0x800ULL), a4);
    if (*(unsigned __int64 *)(v_rbx) != 0) goto loc_0086C492;
loc_0086CBA8:
    v_stack_m238 = v_r14;
    v_r14 = (unsigned int)((v_r14) & (0xFFFFFFFCULL));
    v_stack_m238 = (unsigned int)(v_r14);
    if ((*(unsigned int *)(v_stack_m238 + 4)) == 0) goto loc_0086D018;
    result = ExpGetHandleExtraInfo(v_stack_m238, v_stack_m238, (unsigned int)(0x800ULL), a4);
    a1 = 0;
    if (result != 0) {
        *(unsigned __int64 *)(result) = 0;
    }
    *(unsigned __int64 *)(v_rdi + 8) = 0;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_m238 + 44)) & (1));
    v_stack_m248 = (unsigned __int8)(result);
    if (condition_is_not_equal) goto loc_0086CD36;
loc_0086CBF1:
    a3 = 0;
    v_rbx = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))))) + 1;
    a2 = 0;
    v_rbx = (v_rbx) << (6);
    v_rbx = (v_rbx) + (v_stack_m238);
    result = KeAbPreAcquire(v_rbx, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rbx;
        a2 = result;
        a1 = v_rbx;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (v_stack_m248 != 0) goto loc_0086CCC3;
    *(unsigned __int64 *)(v_rdi + 8) = *(unsigned __int64 *)(v_rbx + 8);
    if (*(unsigned __int64 *)(v_rbx + 8) == 0) {
        *(unsigned __int64 *)(v_rbx + 16) = v_rdi;
    }
    *(unsigned __int64 *)(v_rbx + 8) = v_rdi;
loc_0086CC4C:
    result = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_0086CF8D;
loc_0086CC65:
    result = KeAbPostRelease(v_rbx, a2, a3, a4);
    result = 0;
    goto loc_0086C15F;
loc_0086CC77:
    if (((*(unsigned __int8 *)(v_stack_m220 + 66)) & (8)) == 0) goto loc_0086CE3D;
loc_0086CC82:
    v_stack_m2C8 = a4;
    result = KeBugCheckEx(393, v_r12 - 48, v_stack_m220, 1);
loc_0086CCA0:
    result = ExfReleasePushLock(v_stack_m238, v_r12 - 48, v_stack_m220, 1);
    goto loc_0086C903;
loc_0086CCB1:
    goto loc_0086C042;
loc_0086CCB9:
    result = ExfReleaseRundownProtection(v_stack_m238, 1, v_stack_m220, 1);
    goto loc_0086C3CC;
loc_0086CCC3:
    if (*(unsigned __int64 *)(v_rbx + 16) == 0) goto loc_0086D42B;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 16) + 8) = v_rdi;
loc_0086CCD4:
    *(unsigned __int64 *)(v_rbx + 16) = v_rdi;
    goto loc_0086CC4C;
loc_0086CCDD:
    result = ExfReleasePushLock(v_rdi, 1, v_stack_m220, 1);
    goto loc_0086CA39;
loc_0086CCEA:
    v_stack_m2B8 = v_stack_m1B0;
    v_stack_m2C0 = v_stack_m220;
    v_stack_m2C8 = (unsigned __int8)(v_rbx);
    result = ObpInsertOrLocateNamedObject(v_stack_m230, v_r12, v_stack_m244, v_stack_m228);
    if (sign_flag) goto loc_0086C3A6;
    if (v_stack_m1B0 != v_r12) goto loc_0086D090;
    result = 0;
    v_stack_m1B0 = 0;
    goto loc_0086BE80;
loc_0086CD36:
    goto loc_0086CBF1;
loc_0086CD3D:
    v_stack_m90 = *(unsigned __int64 *)(v_rip + 7785916);
    v_stack_m98 = 1;
    v_stack_m94 = 1;
    v_stack_m88 = (unsigned int)(v_stack_m228);
    if ((unsigned __int8)(v_stack_m128) == 0) goto loc_0086D17C;
    if (*(unsigned __int64 *)(v_stack_m228 + 32) != 0) goto loc_0086D160;
loc_0086CD80:
    v_stack_m2C8 = (unsigned __int8)(v_stack_m128);
    result = SepPrivilegeCheck(*(unsigned __int64 *)(v_stack_m228 + 48), v_stack_m90, 1, 1);
    if ((unsigned __int8)(result) != 0) goto loc_0086D17C;
loc_0086CDA2:
    a4 = 0;
    a1 = 0;
    result = SePrivilegedServiceAuditAlarm(a1, v_stack_m228 + 32, v_stack_m98, a4);
    v_stack_m214 = (unsigned int)((unsigned int)(0xC0000061ULL));
    goto loc_0086C3A2;
loc_0086CDC4:
    result = ExfTryToWakePushLock(v_stack_m230, v_stack_m228 + 32, v_stack_m98, a4);
    goto loc_0086C0E8;
loc_0086CDD1:
    if (((unsigned int)(0xC0000061ULL)) != (*(unsigned __int64 *)(v_rip + 6957184))) goto loc_0086BFAE;
    if (v_stack_m246 != 0) goto loc_0086BFAE;
    result = ObpCreateSymbolicLinkName(v_r12, v_stack_m228 + 32, v_stack_m98, a4);
    goto loc_0086BFAE;
loc_0086CDF8:
    result = ObpDecrementHandleCount(v_stack_m230, v_stack_m128, v_stack_m98, a4);
    if ((unsigned int)(v_stack_m220) != 0) {
        a3 = 0x6E48624FULL;
        a2 = (unsigned int)(v_stack_m220);
        a1 = v_stack_m228;
        result = ObDereferenceObjectExWithTag(a1, a2, a3, a4);
    }
    goto loc_0086C2D7;
loc_0086CE33:
    result = ExfReleaseRundownProtection(a1, a2, a3, a4);
    goto loc_0086C441;
loc_0086CE3D:
    if (((*(unsigned __int8 *)(v_r12 - 22)) & (2)) == 0) goto loc_0086BB1E;
    goto loc_0086CC82;
loc_0086CE4E:
    goto loc_0086BBF5;
loc_0086CE5D:
    *(unsigned __int64 *)(a1 + (unsigned int)(v_stack_m220) * 8) = v_stack_m188;
    goto loc_0086C135;
loc_0086CE76:
    if (*(unsigned __int64 *)(v_r12) != 0) goto loc_0086D14C;
    if (v_stack_m180 != ((unsigned int)(v_stack_m220))) goto loc_0086D21A;
    a1 = ((unsigned int)(0xC000009AULL) - 48) >> (8);
    a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)((unsigned int)(0xC000009AULL) - 24)));
    a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(v_rip + 7708583)));
    if (((unsigned __int8)(a1)) != (*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 7707724) + 40))) goto loc_0086CEBA;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL) + 8) + 52)))) & (16)) != 0) goto loc_0086C1C9;
loc_0086CEBA:
    v_r12 = 0;
    if (*(unsigned __int64 *)(v_stack_m228 + 72) == 0) goto loc_0086CF9A;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m228 + 72) + 56) == 0) goto loc_0086CF9A;
    goto loc_0086CF9D;
loc_0086CEDF:
    if ((*(unsigned int *)((unsigned int)(v_stack_m244) + 196)) < 2) goto loc_0086C70A;
    result = RtlEqualSid(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(0xC000009AULL) + 152)), *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m244) + 152)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m228 + 72) + 56), a4);
    if ((unsigned __int8)(result) != 0) goto loc_0086C70E;
    result = OBJECT_HEADER_TO_HANDLE_REVOCATION_INFO(v_stack_m228 - 48, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_m244) + 152)), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m228 + 72) + 56), a4);
    if (result == 0) goto loc_0086C70E;
    v_stack_m2C0 = 0;
    a4 = 0;
    a2 = 0;
    v_stack_m2C8 = 1;
    result = SepSidInTokenSidHash((unsigned int)(0xC000009AULL) + 808, a2, *(unsigned __int64 *)(v_rip + 6916422), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0086C70E;
    a1 = (*(unsigned __int64 *)((unsigned int)(v_stack_m244) + 216)) + (136);
    result = ObHandleRevocationBlockAddObject(a1, v_stack_m228, *(unsigned __int64 *)(v_rip + 6916422), a4);
    goto loc_0086C70E;
loc_0086CF68:
    a2 = 0;
    result = ExFreePoolWithTag((unsigned int)(v_stack_m244), a2, *(unsigned __int64 *)(v_rip + 6916422), a4);
loc_0086CF72:
    v_stack_m214 = (unsigned int)((unsigned int)(0xC000009AULL));
loc_0086CF75:
    if (sign_flag) goto loc_0086C3A2;
    a4 = 0;
    goto loc_0086BE25;
loc_0086CF8D:
    result = ExfTryToWakePushLock((unsigned int)(v_stack_m244), a2, *(unsigned __int64 *)(v_rip + 6916422), a4);
    goto loc_0086CC65;
loc_0086CF9A:
loc_0086CF9D:
    result = ObpAllocateAndQuerySecurityDescriptorInfo((unsigned int)(0xC000009AULL), 32, 0, v_stack_m1A8);
    v_rbx = (unsigned int)(v_stack_m244);
    if (!(sign_flag)) {
        v_rbx = v_stack_m1A8;
        a2 = v_stack_m1A8;
        a3 = 1;
        a1 = v_stack_m128;
        result = ObpSetObjectAuditInfo(a1, a2, a3, v_stack_m1A8);
    }
    a2 = 0;
    goto loc_0086C1C9;
loc_0086CFCF:
    if (sign_flag) goto loc_0086C3A2;
    result = EtwpTraceHandle((unsigned int)(0x1120ULL), *(unsigned __int64 *)(v_stack_m128), v_stack_m228, v_stack_m210);
    goto loc_0086C3A2;
loc_0086CFF0:
    result = ObDereferenceSecurityDescriptor((unsigned int)(0xC000009AULL), 1, v_stack_m228, v_stack_m210);
    goto loc_0086BE14;
loc_0086D002:
    result = ExfAcquireRundownProtection((unsigned int)(0xC000009AULL), 1, v_stack_m228, v_stack_m210);
    if ((unsigned __int8)(result) == 0) goto loc_0086C9ED;
    goto loc_0086C8D1;
loc_0086D018:
    a1 = 0;
    goto loc_0086CBD5;
loc_0086D01F:
    if (result != (v_rip + 27226)) goto loc_0086D97A;
    v_stack_m2C8 = v_stack_m218;
    result = IopGetSetSecurityObject(1, 1, v_stack_m228, v_rbx);
    goto loc_0086C543;
loc_0086D048:
    result = ObpReferenceSecurityDescriptorSlow(1 - 48, 1, (unsigned int)(0xC000009AULL), v_rbx);
    goto loc_0086BDCF;
loc_0086D05D:
    a2 = 0;
    result = ObpPushStackInfo(result - 48, a2, a2 + 1, (unsigned int)(0x746C6644ULL));
    result = ObpPushStackInfo(result - 48, 1, 1, (unsigned int)(0x6E48624FULL));
    goto loc_0086C186;
loc_0086D090:
    v_stack_m228 = result;
    v_stack_m246 = 1;
    goto loc_0086BE80;
loc_0086D0A0:
    result = ExfReleaseRundownProtection(result - 48, 1, 1, (unsigned int)(0x6E48624FULL));
    goto loc_0086C953;
loc_0086D0AA:
    v_stack_m248 = 1;
    result = ((unsigned int)(v_stack_m1D8)) + 1;
    v_stack_m1C8 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m1D8))));
    result = (result) << (6);
    a2 = 0;
    result = (result) + (1);
    a3 = 0;
    v_stack_m1E8 = result;
    result = KeAbPreAcquire(1 + 56, a2, a3, (unsigned int)(0x6E48624FULL));
    v_stack_m198 = result;
    if (!(condition_is_above_or_equal)) {
        a3 = 1 + 56;
        a2 = result;
        a1 = 1 + 56;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, (unsigned int)(0x6E48624FULL));
        result = v_stack_m198;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = (unsigned int)(v_stack_m220);
    if (((unsigned int)((unsigned int)(v_stack_m220))) == (*(unsigned int *)(v_stack_m238))) {
        a2 = v_stack_m1E8;
        result = ExpAllocateHandleTableEntrySlow(v_stack_m238, a2, a3, (unsigned int)(0x6E48624FULL));
        v_stack_m248 = (unsigned __int8)(result);
    }
    a2 = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(a2)) == 2) goto loc_0086D990;
loc_0086D12B:
    result = KeAbPostRelease(1 + 56, a2, a3, (unsigned int)(0x6E48624FULL));
    if (v_stack_m248 == 0) goto loc_0086C15F;
    a4 = 0;
    goto loc_0086C053;
loc_0086D14C:
    v_rdi = 0;
    v_stack_m190 = 0;
    v_stack_m1B8 = a2;
    goto loc_0086C1F0;
loc_0086D160:
    if ((*(unsigned int *)(v_stack_m228 + 40)) >= 2) goto loc_0086CD80;
    goto loc_0086CDA2;
loc_0086D16F:
    result = ExfReleaseRundownProtection(a2, a2, v_stack_m238, a4);
    goto loc_0086CA89;
loc_0086D17C:
    result = SeAppendPrivileges(v_stack_m228, v_stack_m98, v_stack_m238, a4);
    a4 = 0;
    goto loc_0086BD6B;
loc_0086D1A1:
    *(unsigned __int64 *)(result + 8) = v_stack_m228;
    *(unsigned __int64 *)(result) = v_stack_m1F8;
    *(unsigned __int64 *)(v_stack_m228) = result;
    v_stack_m1F0 = result;
    goto loc_0086C964;
loc_0086D1B8:
    result = ObDereferenceSecurityDescriptor((unsigned int)((unsigned int)((unsigned int)(v_stack_m1D8))), 1, v_stack_m238, a4);
    goto loc_0086BF51;
loc_0086D1CA:
    goto loc_0086CBA8;
loc_0086D1D3:
    goto loc_0086CF72;
loc_0086D1DD:
    result = ObpReferenceSecurityDescriptorSlow(*(unsigned __int64 *)(v_stack_m228 + 72), 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1D8))), a4);
    goto loc_0086BF12;
loc_0086D1F0:
    result = ObDereferenceSecurityDescriptor(result, 1, (unsigned int)((unsigned int)((unsigned int)(v_stack_m1D8))), a4);
    goto loc_0086BCDE;
loc_0086D202:
    result = ObpReferenceSecurityDescriptorSlow(result - 48, 1, result, a4);
    a4 = 0;
    goto loc_0086BB11;
loc_0086D21A:
    a3 = 0;
    result = ObpSetObjectAuditInfo(*(unsigned __int64 *)(v_stack_m228 + 72), v_stack_m180, a3, a4);
    a2 = 0;
    v_stack_m1B8 = 0;
    v_rdi = 0;
    v_stack_m190 = 0;
    goto loc_0086C1E3;
loc_0086D23F:
    v_stack_m2B8 = 2;
    v_stack_m2C0 = 512;
    v_stack_m2C8 = 0;
    result = ZwDuplicateObject(-1, 0, -1, v_stack_m1B8);
    v_rdi = 0;
    v_rbx = result;
    if (!(sign_flag)) {
        a1 = v_stack_m1B8;
        result = v_stack_m120;
        v_stack_m2C0 = 0;
        a4 = 0;
        a3 = 0;
        v_stack_m2C8 = result;
        a2 = 0;
        v_stack_m120 = 0;
        result = ObReferenceObjectByHandle(a1, a2, a3, a4);
        v_rbx = v_stack_m120;
    }
    a4 = 0;
    result = SepAdtClassifyObjectIntoSubCategory(v_rbx, v_stack_m228 + 144, 1, a4);
    v_stack_m248 = (unsigned __int16)(result);
    if (v_rbx != 0) {
        a1 = v_rbx;
        result = ObfDereferenceObject(a1, v_stack_m228 + 144, 1, a4);
    }
    if (v_stack_m1B8 != 0) {
        result = ZwClose(v_stack_m1B8, v_stack_m228 + 144, 1, a4);
        v_stack_m1B8 = 0;
    }
    result = PsGetCurrentProcessId(v_stack_m1B8, v_stack_m228 + 144, 1, a4);
    v_stack_m258 = v_stack_m228;
    v_stack_m260 = *(unsigned __int64 *)(v_stack_m228 + 72) + 32;
    result = 0;
    v_stack_m268 = 0;
    v_stack_m270 = 0;
    v_stack_m278 = 0;
    v_stack_m280 = 2;
    v_stack_m288 = 0;
    v_stack_m290 = 1;
    v_stack_m298 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m228 + 72));
    v_stack_m2A0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m228 + 20)));
    v_stack_m2A8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m228 + 24)));
    v_stack_m2B0 = *(unsigned __int64 *)(v_stack_m228 + 48);
    v_stack_m2B8 = *(unsigned __int64 *)(v_stack_m228 + 32);
    v_stack_m2C0 = 0;
    v_stack_m2C8 = v_stack_m228 + 128;
    result = SepAdtOpenObjectAuditAlarm((unsigned __int16)(v_stack_m248), v_rip - 8830833, v_stack_m190, v_stack_m228 + 144);
    v_stack_m290 = v_stack_m228;
    v_stack_m298 = result;
    v_stack_m2A0 = 1;
    v_stack_m2A8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m228 + 20)));
    v_stack_m2B0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m228 + 24)));
    v_stack_m2B8 = *(unsigned __int64 *)(v_stack_m228 + 48);
    v_stack_m2C0 = *(unsigned __int64 *)(v_stack_m228 + 32);
    v_stack_m248 = (unsigned __int8)(result);
    v_stack_m2C8 = v_stack_m228 + 128;
    result = SepAdtStagingEvent((unsigned __int16)(v_stack_m248), v_rip - 8830833, v_stack_m190, v_stack_m228 + 144);
    goto loc_0086C208;
loc_0086D3C8:
    if ((*(unsigned __int8 *)(v_stack_m228 + 124)) == 0) goto loc_0086D23F;
    v_stack_m2A0 = 1;
    v_stack_m2A8 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m228 + 72));
    v_stack_m2B0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m228 + 20)));
    v_stack_m2B8 = *(unsigned __int64 *)(v_stack_m228 + 56);
    v_stack_m2C0 = *(unsigned __int64 *)(v_stack_m228 + 48);
    v_stack_m2C8 = *(unsigned __int64 *)(v_stack_m228 + 32);
    result = SepAdtPrivilegeObjectAuditAlarm(v_rip - 8831052, v_stack_m228 + 144, v_stack_m228 + 128, 0);
    goto loc_0086C208;
loc_0086D423:
    goto loc_0086BFC8;
loc_0086D42B:
    *(unsigned __int64 *)((unsigned int)(v_stack_m244) + 8) = v_stack_m248;
    goto loc_0086CCD4;
loc_0086D434:
    result = ExReleaseRundownProtection(v_stack_m248 + 56, v_stack_m228 + 144, v_stack_m228 + 128, 0);
    if (v_stack_m1F8 == v_stack_m1F8) goto loc_0086D8A4;
    result = 0;
    v_stack_mF0 = 0xC000009AULL;
    v_stack_mF8 = 0;
    v_stack_mEC = 0;
    v_stack_mE4 = 0;
    v_stack_m110 = (unsigned int)((unsigned int)(v_stack_m150));
    v_stack_m10C = (unsigned int)((unsigned int)(v_stack_m14C));
    v_stack_m100 = v_stack_m140;
    v_stack_m108 = v_stack_m148;
    result = ObpCallPostOperationCallbacks(v_stack_m110, v_stack_m1F8, v_stack_m228 + 128, 0);
loc_0086D4A9:
    result = (*(unsigned __int64 *)(v_stack_m228 + 72)) >> (8);
    a1 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m228 + 72) + 24));
    a1 = (a1) ^ (*(unsigned __int8 *)(v_rip + 7707010));
    v_stack_m80 = v_xmm0;
    v_stack_m70 = v_xmm0;
    a1 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m200 = 0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 8836308 + a1 * 8 + 16545792) + 66)) & (16)) != 0) goto loc_0086D651;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m228 + 72) + 27)) & (8)) != 0) goto loc_0086D651;
loc_0086D518:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8836308 + a1 * 8 + 16545792) + 128)) == 0) goto loc_0086D5AD;
    v_stack_m210 = 0;
    v_stack_m248 = 0;
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) != v_stack_m230) {
        v_stack_m248 = 1;
        result = PsGetProcessServerSilo(v_stack_m230, v_stack_m1F8, v_stack_m228 + 128, 0);
        a1 = result;
        result = PsAttachSiloToCurrentThread(a1, v_stack_m1F8, v_stack_m228 + 128, 0);
        a1 = v_stack_m230;
        a2 = v_stack_m80;
        v_stack_m210 = result;
        result = KeStackAttachProcess(a1, a2, v_stack_m228 + 128, 0);
        a1 = v_stack_m230;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8836308 + a1 * 8 + 16545792) + 128)) != (v_rip - 39595)) goto loc_0086D5DE;
    result = CmpCloseKeyObject(a1, *(unsigned __int64 *)(v_stack_m228 + 72) + 48, (unsigned int)(v_stack_m200), -1);
loc_0086D590:
    if (v_stack_m248 != 0) {
        a2 = 0;
        a1 = v_stack_m80;
        result = KiUnstackDetachProcess(a1, a2, (unsigned int)(v_stack_m200), -1);
        a1 = v_stack_m210;
        result = PsDetachSiloFromCurrentThread(a1, a2, (unsigned int)(v_stack_m200), -1);
    }
    if (-1 == 1) {
        a1 = *(unsigned __int64 *)(v_stack_m228 + 72);
        result = ObpDeleteNameCheck(a1, a2, (unsigned int)(v_stack_m200), -1);
    }
    if ((unsigned int)(v_stack_m220) == 0) goto loc_0086C3A2;
    result = ObDereferenceObjectExWithTag(v_stack_m248, (unsigned int)((unsigned int)(v_stack_m220)), (unsigned int)(0x746C6644ULL), -1);
    goto loc_0086C3A2;
loc_0086D5DE:
    if (result != (v_rip + 1702091)) goto loc_0086D788;
    if (-1 != 1) goto loc_0086D590;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m228 + 72) + 146)) & (2)) == 0) goto loc_0086D642;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 6890043), v_rip - 8768900, (unsigned int)(0x746C6644ULL), -1);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m228 + 72) + 80);
        a2 = v_rip - 8768920;
        a1 = *(unsigned __int64 *)(v_rip + 6890009);
        result = (result) + (40);
        v_stack_m2C0 = result;
        a4 = -1;
        result = 0;
        a3 = 0;
        v_stack_m2C8 = 0;
        result = EtwpEventWriteTemplateSessAndProv(a1, a2, a3, a4);
    }
    goto loc_0086D590;
loc_0086D651:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(v_stack_m228 + 72) + 16, a2, a3, a4);
    v_stack_m1E8 = result;
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(v_stack_m228 + 72) + 16;
        a2 = result;
        a1 = *(unsigned __int64 *)(v_stack_m228 + 72) + 16;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
        result = v_stack_m1E8;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = (-1) - (1);
    if (condition_is_not_equal) goto loc_0086D7A9;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m228 + 72) + 27))) & (8)) == 0) goto loc_0086D7A9;
    result = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m228 + 72) + 26)) & (31));
    a1 = (*(unsigned __int64 *)(v_stack_m228 + 72)) - (*(unsigned __int8 *)(result + v_rip - 8836786 * 1 + 15794048));
    v_r10 = 0;
    *(unsigned __int64 *)(a1) = 0;
loc_0086D6E5:
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 8836308 + a1 * 8 + 16545792) + 66))) & (16)) == 0) goto loc_0086D73B;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m228 + 72) + 26))) & (4)) != 0) goto loc_0086D7B1;
loc_0086D6FD:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m228 + 72) + 27)) & (64)) == 0) goto loc_0086D7C7;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 8))) & (0xFFFFFFULL));
    v_stack_m200 = (unsigned int)(a2);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(0 + 8)))) - 1) ^ ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(0 + 8)))))));
    result = (unsigned int)((result) & (0xFFFFFFULL));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(0 + 8)))))));
loc_0086D723:
    *(unsigned int *)(0 + 8) = (unsigned int)(result);
loc_0086D727:
    if ((*(unsigned __int8 *)(0 + 11)) != 0) goto loc_0086D73B;
    if (((*(unsigned int *)(0 + 8)) & (0xFFFFFFULL)) == 0) {
        *(unsigned __int64 *)(0) = 0;
    }
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m228 + 72) + 16)) & (-16);
    a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m228 + 72) + 16) - 16;
    if (a1 <= 16) { a3 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m228 + 72) + 16))) & (2)) != 0) goto loc_0086D80A;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m228 + 72) + 16))) & (2)) != 0) goto loc_0086D80A;
loc_0086D76B:
    result = KeAbPostRelease(*(unsigned __int64 *)(v_stack_m228 + 72) + 16, *(unsigned __int64 *)(v_stack_m228 + 72) + 16, a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(v_stack_m228 + 72) + 16, a3, a4);
    a1 = 0;
    goto loc_0086D518;
loc_0086D788:
    if (result != (v_rip - 38607)) goto loc_0086D81B;
    result = IopCloseFile(a1, *(unsigned __int64 *)(v_stack_m228 + 72) + 48, a3, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m228 + 72) + 8));
    goto loc_0086D590;
loc_0086D7A9:
    v_r10 = 0;
    goto loc_0086D6E5;
loc_0086D7B1:
    result = (unsigned int)((result) & (7));
    a3 = (*(unsigned __int64 *)(v_stack_m228 + 72)) - (*(unsigned __int8 *)(result + *(unsigned __int64 *)(v_stack_m228 + 72) + 48 * 1 + 15794048));
    goto loc_0086D6FD;
loc_0086D7C7:
loc_0086D7D4:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3)))) == 0) goto loc_0086D727;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) + 8 + 8))))) & (0xFFFFFFULL));
    if (condition_is_equal) goto loc_0086D7EE;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a3) + 8)) == v_stack_m230) goto loc_0086D7F6;
loc_0086D7EE:
    a3 = (*(unsigned __int64 *)(a3) + 8) + (16);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3)))) - 1);
    goto loc_0086D7D4;
loc_0086D7F6:
    v_stack_m200 = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) + 8 + 8)) - 1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) + 8 + 8)))));
    result = (unsigned int)((result) & (0xFFFFFFULL));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) + 8 + 8)))));
    goto loc_0086D723;
loc_0086D80A:
    result = ExfReleasePushLock((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) + 8 + 8)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) + 8 + 8)), a3, v_stack_m230);
    goto loc_0086D76B;
loc_0086D81B:
    result = guard_dispatch_icall((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a3) + 8 + 8)), *(unsigned __int64 *)(v_stack_m228 + 72) + 16, a3, v_stack_m230);
    goto loc_0086D590;
loc_0086D825:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rip - 8836308 + a1 * 8 + 16545792), a2, a3, v_stack_m230);
    *(unsigned int *)(v_rip + 5888845) = (unsigned int)((unsigned int)(v_stack_m218));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(v_stack_m218))), (unsigned int)(0x7153624FULL), v_stack_m230);
    if (result == 0) goto loc_0086D99D;
    v_stack_m2A8 = (unsigned __int8)(*(unsigned __int64 *)(v_stack_m228 + 72));
    v_stack_m2B0 = v_stack_m220 + 76;
    v_stack_m2B8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m220 + 100)));
    v_stack_m2C0 = v_stack_m210;
    v_stack_m2C8 = v_stack_m218;
    v_stack_m248 = 1;
    result = guard_dispatch_icall(v_stack_m248, 1, v_stack_m208, result);
    goto loc_0086C550;
loc_0086D8A4:
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), 1, v_stack_m208, result);
    result = ObfDereferenceObjectWithTag(v_stack_m148, (unsigned int)(0x6243624FULL), v_stack_m208, result);
    goto loc_0086D4A9;
loc_0086D8C8:
    if ((unsigned int)(v_stack_m208) == 0) goto loc_0086D96F;
loc_0086D8E6:
    if ((unsigned int)((unsigned int)(result)) == 0) goto loc_0086D8FB;
    if ((unsigned int)((unsigned int)(0x6243624FULL)) == 0) goto loc_0086D8FD;
    goto loc_0086D8FD;
loc_0086D8FB:
    result = 0;
loc_0086D8FD:
    result = ExAllocatePool2(256, v_stack_m208 + v_stack_m208 * 2 * 4 + 8 + result * 1, (unsigned int)(0x72506553ULL), result);
    v_stack_m1D0 = result;
    if (result == 0) goto loc_0086BC12;
    if (*(unsigned __int64 *)(v_stack_m210) == 0) goto loc_0086D976;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m210)))) == 0) goto loc_0086D9A7;
loc_0086D93C:
    result = memcpy(result, *(unsigned __int64 *)(v_stack_m210), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m210))) + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m210))) * 2 * 4 + 8)), result);
    result = SepConcatenatePrivileges(v_stack_m1D0, *(unsigned __int64 *)(v_stack_m210), v_stack_m248, result);
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m228 + 72) + 8) + 11)) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m210);
        a2 = 0;
        result = ExFreePoolWithTag(a1, a2, v_stack_m248, result);
    }
    *(unsigned __int64 *)(v_stack_m210) = v_stack_m1D0;
    *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m228 + 72) + 8) + 11) = 1;
    goto loc_0086BC12;
loc_0086D96F:
    goto loc_0086D8E6;
loc_0086D976:
    result = 0;
    goto loc_0086D93C;
loc_0086D97A:
    v_stack_m2C8 = v_stack_m218;
    result = guard_dispatch_icall(v_stack_m1D0, a2, v_stack_m248, result);
    goto loc_0086C543;
loc_0086D990:
    result = ExfTryToWakePushLock(v_stack_m210, a2, v_stack_m248, result);
    goto loc_0086D12B;
loc_0086D99D:
    goto loc_0086CF72;
loc_0086D9A7:
    goto loc_0086D93C;
loc_0086D9AE:
    goto loc_0086CF75;
loc_0086D9B6:
    a4 = 0;
loc_0086D9C3:
    result = (unsigned int)(((unsigned int)(v_stack_m200)) + 1);
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m1C8)) + 1);
    v_stack_m200 = (unsigned int)(result);
    result = 0;
    if (((unsigned int)(v_rbx)) != ((unsigned int)((unsigned int)(v_stack_m1C0)))) { result = (unsigned int)(v_rbx); }
    v_stack_m1C8 = (unsigned int)(result);
    goto loc_0086C05F;
loc_0086D9E2:
    a1 = (v_stack_m50) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, v_stack_m238, a4);
    v_rsp = (v_rsp) + (680);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ObpCreateHandle(int32_t Arg1, void *Arg2, int32_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6, uint8_t Arg7, int64_t Arg8, uint32_t Arg9, int64_t Arg10, int64_t Arg11)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint32_t v_stack_m10C;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint32_t v_stack_m14C;
    uint32_t v_stack_m150;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint32_t v_stack_m184;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint32_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint32_t v_stack_m1D0;
    uint32_t v_stack_m1D8;
    uint32_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint32_t v_stack_m200;
    uint32_t v_stack_m208;
    uint64_t v_stack_m210;
    uint32_t v_stack_m214;
    uint32_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint8_t v_stack_m240;
    uint32_t v_stack_m244;
    uint8_t v_stack_m245;
    uint8_t v_stack_m246;
    uint8_t v_stack_m248;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint32_t v_stack_m270;
    uint64_t v_stack_m278;
    uint32_t v_stack_m280;
    uint64_t v_stack_m288;
    uint8_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint8_t v_stack_m2B0;
    uint64_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint32_t v_stack_m2C8;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint32_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m94;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mAC;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint32_t v_stack_mDC;
    uint32_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint64_t v_stack_mEC;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;

    local_rsp = (local_rsp) - (680);
    result = (*(uint64_t *)(v_rip + 0x59EDCD)) ^ (local_rsp);
    v_stack_m50 = result;
    Arg4 = 0;
    v_stack_m118 = Arg10;
    v_stack_m128 = Arg11;
    v_stack_m244 = 0;
    v_stack_m188 = 0;
    v_stack_m184 = (uint32_t)((uint32_t)(Arg9));
    v_stack_m228 = Arg2;
    v_stack_m1E0 = Arg1;
    v_stack_m220 = Arg8;
    v_stack_m1B0 = 0;
    v_stack_m246 = 0;
    v_stack_m1A8 = 0;
    v_stack_m240 = 0;
    v_stack_m1F8 = v_xmm0;
    v_stack_m230 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    if (condition_is_below) goto loc_0086C4A2;
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24A)) == 1) goto loc_0086C560;
loc_0086BA34:
    v_stack_m238 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x300);
loc_0086BA38:
    result = ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x300)) == (*(uint64_t *)(v_rip + 0x6A3B79))) ? 1 : 0;
    v_stack_m245 = (uint8_t)(result);
    if (0 == 0) goto loc_0086C5F1;
    if ((uint8_t)(result) != 0) goto loc_0086C5E7;
loc_0086BA56:
    v_stack_m214 = 0;
    local_r15 = 1;
    if (condition_is_above_or_equal) { local_r15 = Arg7; }
    if (((uint32_t)((uint32_t)(Arg1) - 1)) > 1) goto loc_0086BCF3;
    result = (Arg2 - 48) >> (8);
    Arg1 = ((uint8_t)(result)) ^ (*(uint8_t *)(arg2 - 0x18));
    v_stack_m1A0 = 0;
    Arg1 = (Arg1) ^ (*(uint8_t *)(v_rip + 0x75B3B0));
    v_stack_m160 = 0;
    v_stack_m218 = 0;
    v_stack_m208 = 0;
    v_stack_m1C0 = *(uint64_t *)(v_rip - 0x86BAAA + Arg1 * 8 + 0xFC7800);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x86BAAA + Arg1 * 8 + 0xFC7800) + 0x98)) != (v_rip + 321519)) goto loc_0086C4B9;
    if ((((uint8_t)(*(uint64_t *)(arg2 - 0x8))) & (15)) == 0) goto loc_0086BAF9;
loc_0086BAE2:
    if ((((uint8_t)(*(uint64_t *)(arg2 - 0x8))) & (15)) == 0) goto loc_0086BAF9;
    if ((((uint8_t)(*(uint64_t *)(arg2 - 0x8))) & (15)) != 0) goto loc_0086BAE2;
loc_0086BAF9:
    Arg2 = (uint32_t)((*(uint64_t *)(arg2 - 0x8)) & (15));
    local_rbx = (*(uint64_t *)(arg2 - 0x8)) & (-16);
    if (((uint32_t)(Arg2)) > 1) goto loc_0086BB11;
    if (local_rbx != 0) goto loc_0086D202;
loc_0086BB11:
    v_stack_m248 = 0;
    if (local_rbx == 0) goto loc_0086CC77;
loc_0086BB1E:
loc_0086BB21:
    if (local_rbx == 0) goto loc_0086C665;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(*(uint64_t *)(Arg4 + 0x30) + 0x30), 1, Arg3, Arg4);
    if ((*(uint64_t *)(Arg4 + 0x20)) != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg2 = 1;
        Arg1 = *(uint64_t *)(Arg4 + 0x20);
        Arg1 = *(uint64_t *)(Arg1 + 0x30);
        result = ExAcquireResourceSharedLite(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m2A0 = v_stack_m214;
    v_stack_m2A8 = v_stack_m1A0;
    v_stack_m2B0 = (uint8_t)(local_r15);
    v_stack_m2B8 = *(uint64_t *)(v_rip - 0x86BAAA + Arg1 * 8 + 0xFC7800) + 76;
    v_stack_m2C0 = v_stack_m160;
    v_stack_m2C8 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x14)));
    result = SeAccessCheck(local_rbx, Arg4 + 32, 1, (uint32_t)(*(uint32_t *)(Arg4 + 0x10)));
    if (v_stack_m160 == 0) goto loc_0086BC1B;
    v_stack_m210 = *(uint64_t *)(Arg4 + 0x48);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg4 + 0x48)))) + (uint32_t)(*(uint32_t *)(v_stack_m160)) * 1)) > 3) goto loc_0086D8C8;
    if (*(uint64_t *)(*(uint64_t *)(Arg4 + 0x48)) == 0) goto loc_0086C67B;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg4 + 0x48))))) != 0) goto loc_0086CE4E;
loc_0086BBF5:
    Arg1 = (8) + (*(uint64_t *)(*(uint64_t *)(Arg4 + 0x48)));
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m160)) + (uint32_t)(*(uint32_t *)(v_stack_m160)) * 2) << (2));
    result = memcpy(Arg1, v_stack_m160 + 8, Arg3, (uint32_t)(*(uint32_t *)(Arg4 + 0x10)));
loc_0086BC12:
    result = CmSiFreeMemory(v_stack_m160, v_stack_m160 + 8, Arg3, (uint32_t)(*(uint32_t *)(Arg4 + 0x10)));
loc_0086BC1B:
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_stack_m1A0;
        Arg1 = (uint32_t)(~(Arg1));
    }
    if ((uint8_t)(local_r15) != 0) {
        Arg1 = v_stack_m1C0;
        result = Arg4 + 10;
        v_stack_m2A0 = result;
        Arg1 = (Arg1) + (16);
        result = 0;
        Arg4 = local_rbx;
        v_stack_m2A8 = 0;
        Arg3 = 0;
        v_stack_m2B0 = (uint8_t)(local_r15);
        Arg2 = v_stack_m228;
        v_stack_m2B8 = (uint8_t)((uint8_t)(result));
        v_stack_m2C0 = 0;
        v_stack_m2C8 = Arg4;
        result = SeOpenObjectAuditAlarmWithTransaction(Arg1, Arg2, Arg3, Arg4);
    }
    result = ExReleaseResourceLite(*(uint64_t *)(*(uint64_t *)(Arg4 + 0x30) + 0x30), Arg2, Arg3, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    if (*(uint64_t *)(Arg4 + 0x20) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(Arg4 + 0x20) + 0x30);
        result = ExReleaseResourceLite(Arg1, Arg2, Arg3, Arg4);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = KeLeaveCriticalRegionThread(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m248 != 0) goto loc_0086C741;
loc_0086BCC1:
    Arg1 = (*(uint64_t *)(v_stack_m228 - 0x8)) ^ (local_rbx);
    if (Arg1 >= 15) goto loc_0086D1F0;
    if (Arg1 != 15) goto loc_0086BCC1;
loc_0086BCDE:
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_0086D9AE;
    Arg4 = 0;
    goto loc_0086BE1B;
loc_0086BCF3:
    result = (*(uint64_t *)(v_stack_m228 - 0x8)) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(v_stack_m228 - 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0x75B142));
    if (!(condition_is_above_or_equal)) {
        *(uint32_t *)(Arg4 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x10)));
    }
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x10)))) & (0xF0000000ULL)) == 0) goto loc_0086BD61;
    result = (uint32_t)(*(uint32_t *)(Arg4 + 0x10));
    if (sign_flag) {
        result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg4 + 0x10))) | (*(uint32_t *)(*(uint64_t *)(v_rip - 0x86BD14 + arg2 * 8 + 0xFC7800) + 0x4C)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (uint32_t)((result) | (*(uint32_t *)(*(uint64_t *)(v_rip - 0x86BD14 + arg2 * 8 + 0xFC7800) + 0x50)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (uint32_t)((result) | (*(uint32_t *)(*(uint64_t *)(v_rip - 0x86BD14 + arg2 * 8 + 0xFC7800) + 0x54)));
    }
    if (!(condition_is_above_or_equal)) {
        result = (uint32_t)((result) | (*(uint32_t *)(*(uint64_t *)(v_rip - 0x86BD14 + arg2 * 8 + 0xFC7800) + 0x58)));
    }
    result = (uint32_t)((result) & (0xFFFFFFFULL));
    *(uint32_t *)(Arg4 + 0x10) = (uint32_t)(result);
loc_0086BD61:
    if (condition_is_below) goto loc_0086CD3D;
loc_0086BD6B:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg4 + 0x10))) | (*(uint32_t *)(Arg4 + 0x14)));
    *(uint32_t *)(Arg4 + 0x14) = Arg1;
    *(uint32_t *)(Arg4 + 0x10) = 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x86BD14 + arg2 * 8 + 0xFC7800) + 0x5C))) & (Arg1));
    *(uint32_t *)(Arg4 + 0x14) = (uint32_t)(result);
    if ((((uint8_t)(*(uint64_t *)(v_stack_m228 - 0x8))) & (15)) == 0) goto loc_0086BDB7;
loc_0086BDA0:
    if ((((uint8_t)(*(uint64_t *)(v_stack_m228 - 0x8))) & (15)) == 0) goto loc_0086BDB7;
    if ((((uint8_t)(*(uint64_t *)(v_stack_m228 - 0x8))) & (15)) != 0) goto loc_0086BDA0;
loc_0086BDB7:
    Arg2 = (uint32_t)((*(uint64_t *)(v_stack_m228 - 0x8)) & (15));
    local_rdi = (*(uint64_t *)(v_stack_m228 - 0x8)) & (-16);
    if (((uint32_t)(Arg2)) > 1) goto loc_0086BDCF;
    if (local_rdi != 0) goto loc_0086D048;
loc_0086BDCF:
    result = SeComputeCreatorDeniedRights(Arg4 + 32, 0, (uint32_t)(*(uint32_t *)(Arg4 + 0x14)), local_rdi);
    result = (uint32_t)(~(result));
    if (local_rdi == 0) goto loc_0086BE14;
loc_0086BDF7:
    Arg1 = (*(uint64_t *)(v_stack_m228 - 0x8)) ^ (local_rdi);
    if (Arg1 >= 15) goto loc_0086CFF0;
    if (Arg1 != 15) goto loc_0086BDF7;
loc_0086BE14:
    Arg4 = 0;
    v_stack_m214 = 0;
loc_0086BE1B:
    v_stack_m244 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + 0x14)));
loc_0086BE25:
    v_stack_m180 = 0;
    result = 0;
    if (v_stack_m220 != 0) {
        result = *(uint64_t *)(v_stack_m220 + 0x20);
        v_stack_m180 = result;
    }
    v_stack_m2B8 = result;
    v_stack_m2C0 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m2C8 = Arg7;
    result = ObpIncrementHandleCountEx((uint32_t)(v_stack_m1E0), v_stack_m244, v_stack_m230, v_stack_m228);
    if (sign_flag) goto loc_0086C3A2;
    if (0 == 0) goto loc_0086C6AC;
    if (v_stack_m220 != 0) goto loc_0086CCEA;
loc_0086BE80:
    local_r14 = (uint32_t)(Arg6);
    if ((*(uint8_t *)(Arg4 + 0xA)) != 0) {
        local_r14 = (uint32_t)(((uint32_t)(Arg6)) | (4));
    }
    result = (v_stack_m228 - 48) >> (8);
    Arg1 = ((uint8_t)(result)) ^ (*(uint8_t *)(v_stack_m228 - 0x30 + 0x18));
    Arg1 = (Arg1) ^ (*(uint8_t *)(v_rip + 0x75AFA1));
    v_stack_m210 = *(uint64_t *)(v_rip - 0x86BEB5 + Arg1 * 8 + 0xFC7800);
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m244)) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x86BEB5 + Arg1 * 8 + 0xFC7800) + 0x5C)))));
    v_stack_m244 = (uint32_t)(local_rbx);
    if (0 == 0) goto loc_0086C5DF;
    if ((((uint8_t)(*(uint64_t *)(v_stack_m228 - 0x30 + 0x28))) & (15)) == 0) goto loc_0086BEFA;
loc_0086BEE4:
    if ((((uint8_t)(*(uint64_t *)(v_stack_m228 - 0x30 + 0x28))) & (15)) == 0) goto loc_0086BEFA;
    if ((((uint8_t)(*(uint64_t *)(v_stack_m228 - 0x30 + 0x28))) & (15)) != 0) goto loc_0086BEE4;
loc_0086BEFA:
    Arg2 = (uint32_t)((*(uint64_t *)(v_stack_m228 - 0x30 + 0x28)) & (15));
    local_rbx = (*(uint64_t *)(v_stack_m228 - 0x30 + 0x28)) & (-16);
    if (((uint32_t)(Arg2)) > 1) goto loc_0086BF12;
    if (local_rbx != 0) goto loc_0086D1DD;
loc_0086BF12:
    result = SeComputeCreatorDeniedRights(Arg4 + 32, 0, (uint32_t)(v_stack_m244), local_rbx);
    if (local_rbx == 0) goto loc_0086BF51;
loc_0086BF35:
    Arg1 = (*(uint64_t *)(v_stack_m228 - 0x30 + 0x28)) ^ (local_rbx);
    if (Arg1 >= 15) goto loc_0086D1B8;
    if (Arg1 != 15) goto loc_0086BF35;
loc_0086BF51:
    local_rdi = (uint32_t)(~((uint32_t)((uint32_t)(result))));
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m244)) & ((uint32_t)(local_rdi)));
    v_stack_m244 = (uint32_t)(local_rbx);
    *(uint32_t *)(Arg4 + 0x14) = (uint32_t)(local_rbx);
    v_stack_m188 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x48) + 0x1C)));
loc_0086BF6C:
    v_stack_m1D0 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x48) + 0x1C)));
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg4 + 0x48) + 0x1C));
    if ((uint32_t)((uint32_t)(Arg5)) != 0) {
        Arg3 = 0x746C6644ULL;
        Arg2 = (uint32_t)((uint32_t)(Arg5));
        Arg1 = v_stack_m228;
        result = ObReferenceObjectExWithTag(Arg1, Arg2, Arg3, local_rbx);
        local_rbx = v_stack_m244;
    }
    if (v_stack_m1B0 != 0) {
        Arg1 = v_stack_m1B0;
        result = ObfDereferenceObject(Arg1, Arg2, Arg3, local_rbx);
        local_rbx = v_stack_m244;
    }
    if (v_stack_m220 != 0) goto loc_0086CDD1;
loc_0086BFAE:
    v_stack_m1F0 = v_stack_m1F8;
    v_stack_m1F8 = v_stack_m1F8;
    if (((*(uint8_t *)(v_stack_m210 + 0x42)) & (64)) != 0) goto loc_0086C750;
loc_0086BFC8:
    Arg4 = 0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (7));
    v_stack_m170 = 0;
    Arg1 = (Arg1) << (17);
    local_rbx = (uint32_t)((local_rbx) & (0x1FFFFFFULL));
    v_stack_m170 = (uint32_t)(local_rbx);
    result = (v_stack_m228 - 48) << (16);
    result = (result) & (0xFFFFFFFFFFF1FFFFULL);
    Arg1 = (Arg1) | (result);
    v_stack_m178 = Arg1;
    if ((((uint8_t)(local_r14)) & (8)) != 0) {
    }
    Arg1 = (Arg1) | (1);
    v_stack_m170 = (uint32_t)(local_rbx);
    v_stack_m178 = Arg1;
    if ((((uint8_t)(*(uint8_t *)(v_stack_m238 + 0x2C))) & (4)) != 0) goto loc_0086C15F;
    if ((((uint8_t)(*(uint8_t *)(v_stack_m238 + 0x2C))) & (1)) != 0) goto loc_0086CCB1;
loc_0086C042:
    v_stack_m1C8 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))))));
    v_stack_m1D8 = (uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))));
    v_stack_m1C0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x76DAD0)));
loc_0086C053:
    v_stack_m220 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m238)));
    v_stack_m200 = 0;
loc_0086C05F:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x76DAD0))))) goto loc_0086D0AA;
    local_rbx = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))))) + 1;
    local_rbx = (local_rbx) << (6);
    local_rbx = (local_rbx) + (v_stack_m238);
    if ((*(uint64_t *)(local_rbx + 0x8)) == 0) goto loc_0086D9C3;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rbx, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rbx;
        Arg2 = result;
        Arg1 = local_rbx;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (*(uint64_t *)(local_rbx + 0x8) == 0) goto loc_0086C0D2;
    *(uint64_t *)(local_rbx + 0x8) = *(uint64_t *)(*(uint64_t *)(local_rbx + 0x8) + 0x8);
    if (*(uint64_t *)(*(uint64_t *)(local_rbx + 0x8) + 0x8) == 0) {
        *(uint64_t *)(local_rbx + 0x10) = *(uint64_t *)(*(uint64_t *)(local_rbx + 0x8) + 0x8);
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x18)))) >= = (*(uint32_t *)(local_rbx + 0x1C))) {
        *(uint32_t *)(local_rbx + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + 0x18)));
    }
    result = (uint8_t)((-1) & (6));
    if (((uint8_t)(result)) == 2) goto loc_0086CDC4;
loc_0086C0E8:
    result = KeAbPostRelease(local_rbx, Arg2, Arg3, Arg4);
    if (*(uint64_t *)(local_rbx + 0x8) == 0) goto loc_0086D9B6;
    result = (*(uint64_t *)(local_rbx + 0x8)) & (0xFFFFFFFFFFFFF000ULL);
    Arg1 = (*(uint64_t *)(local_rbx + 0x8)) - (result);
    Arg1 = (Arg1) >> (4);
    if (v_stack_m1D0 != 0) goto loc_0086C454;
    if (Arg9 != 0) goto loc_0086C454;
loc_0086C135:
    result = (uint32_t)((uint32_t)(*(uint64_t *)(result + 0x8) + Arg1 * 4));
    if ((*(uint64_t *)(v_stack_m238 + 0x60)) != 0) {
        Arg4 = 1;
        Arg3 = *(uint64_t *)(result + 0x8) + Arg1 * 4;
        Arg2 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = v_stack_m238;
        result = ExpUpdateDebugInfo(Arg1, Arg2, Arg3, Arg4);
    }
    *(uint64_t *)(*(uint64_t *)(local_rbx + 0x8) + 0x8) = v_stack_m170;
    *(uint64_t *)(*(uint64_t *)(local_rbx + 0x8)) = v_stack_m178;
loc_0086C15F:
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    if (*(uint64_t *)(result + 0x8) + Arg1 * 4 == 0) goto loc_0086CDF8;
    if ((uint32_t)((uint32_t)(Arg5)) == 0) goto loc_0086C186;
    if ((*(uint32_t *)(v_rip + 0x758E90)) != 0) goto loc_0086D05D;
loc_0086C186:
    if (Arg4 == 0) goto loc_0086C2A6;
    Arg2 = 0;
    v_stack_m1A8 = 0;
    if ((((uint8_t)(*(uint8_t *)(v_stack_m228 - 0x30 + 0x1A))) & (32)) == 0) goto loc_0086C1BE;
    result = (uint32_t)((*(uint8_t *)(v_stack_m228 - 0x30 + 0x1A)) & (63));
    local_r12 = (v_stack_m228 - 48) - (*(uint8_t *)(result + v_rip - 0x86C1AA * 1 + 0xF0FF80));
    if (condition_is_not_equal) goto loc_0086CE76;
loc_0086C1BE:
    local_rbx = 0;
    if (v_stack_m180 != 0) { local_rbx = v_stack_m180; }
loc_0086C1C9:
    local_rdi = 0;
    v_stack_m190 = *(uint64_t *)(result + 0x8) + Arg1 * 4;
    v_stack_m1B8 = 0;
    if (local_rbx != 0) goto loc_0086C1F0;
loc_0086C1E3:
    local_r12 = *(uint64_t *)(*(uint64_t *)(Arg4 + 0x48) + 0x38);
    if (*(uint64_t *)(*(uint64_t *)(Arg4 + 0x48) + 0x38) == 0) {
        local_r12 = *(uint64_t *)(Arg4 + 0x40);
    }
    if ((*(uint8_t *)(Arg4 + 0x9)) != 0) goto loc_0086D3C8;
    if ((*(uint8_t *)(*(uint64_t *)(Arg4 + 0x48) + 0xD8)) != 0) goto loc_0086D23F;
loc_0086C208:
    *(uint8_t *)(Arg4 + 0xA) = 0;
    if ((uint32_t)((uint32_t)(v_stack_m1E0)) != 0) goto loc_0086C274;
    if (*(uint64_t *)(*(uint64_t *)(Arg4 + 0x48)) == 0) goto loc_0086C274;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(Arg4 + 0x48)))) <= ((uint32_t)((uint32_t)(v_stack_m1E0)))) goto loc_0086C274;
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != ((uint8_t)((uint32_t)(v_stack_m1E0)))) {
        result = *(uint32_t *)(Arg4 + 0x14);
        Arg1 = v_rip - 8826518;
        v_stack_m2A0 = 1;
        Arg4 = *(uint64_t *)(result + 0x8) + Arg1 * 4;
        v_stack_m2A8 = *(uint64_t *)(*(uint64_t *)(Arg4 + 0x48));
        Arg3 = 0;
        v_stack_m2B0 = (uint32_t)(result);
        Arg2 = 0;
        result = *(uint64_t *)(Arg4 + 0x38);
        v_stack_m2B8 = result;
        result = *(uint64_t *)(Arg4 + 0x30);
        v_stack_m2C0 = result;
        result = *(uint64_t *)(Arg4 + 0x20);
        v_stack_m2C8 = result;
        result = SepAdtPrivilegeObjectAuditAlarm(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m1A8 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m1A8, Arg2, Arg3, Arg4);
    }
    if ((uint32_t)((uint32_t)(v_stack_m1E0)) != 0) goto loc_0086C2A6;
    if (v_stack_m210 != (*(uint64_t *)(v_rip + 0x75A82D))) goto loc_0086C69A;
loc_0086C299:
    if (*(uint64_t *)(Arg4 + 0x20) != 0) goto loc_0086C6B5;
loc_0086C2A6:
loc_0086C2AA:
    if ((uint32_t)((uint32_t)(Arg5)) != 0) goto loc_0086C682;
loc_0086C2B3:
    local_rdi = (uint32_t)((local_rdi) & (0x40000000ULL));
    local_r14 = *(uint64_t *)(result + 0x8) + Arg1 * 4;
    if ((uint8_t)(v_stack_m245) != 0) {
        local_r14 = (*(uint64_t *)(result + 0x8) + Arg1 * 4) | (0xFFFFFFFF80000000ULL);
    }
    *(uint64_t *)(v_stack_m128) = local_r14;
loc_0086C2D7:
    if (v_stack_m1F8 == v_stack_m1F8) goto loc_0086C394;
    Arg4 = 0;
    v_stack_mB8 = v_stack_m168;
    Arg1 = (uint32_t)((0) & (0xFFFFFFFEULL));
    v_stack_mBC = 0;
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)((uint8_t)(v_stack_m245))));
    v_stack_mE0 = 1;
    v_stack_mDC = Arg1;
    result = (v_stack_m228 - 48) >> (8);
    Arg1 = ((uint8_t)(result)) ^ (*(uint8_t *)(v_stack_m228 - 0x18));
    v_stack_mD8 = v_stack_m228;
    Arg1 = (Arg1) ^ (*(uint8_t *)(v_rip + 0x75AB10));
    v_stack_mC8 = 0;
    v_stack_mC0 = (uint32_t)(local_rdi);
    v_stack_mD0 = *(uint64_t *)(v_rip - 0x86C34D + Arg1 * 8 + 0xFC7800);
    v_stack_m168 = (uint32_t)((uint32_t)(v_stack_m244));
loc_0086C368:
    if (v_stack_m1F8 != v_stack_m1F8) goto loc_0086C3D4;
    result = ObfDereferenceObjectWithTag(v_stack_mD8, (uint32_t)(0x6243624FULL), v_stack_m1F8, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(0x6243624FULL), v_stack_m1F8, Arg4);
loc_0086C394:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x75A776)))) & (64)) != 0) goto loc_0086CFCF;
loc_0086C3A2:
loc_0086C3A6:
    if (v_stack_m240 == 0) goto loc_0086C3CC;
    result = (*(uint64_t *)(v_stack_m230 + 0x1E8)) & (-2);
    if (condition_is_not_equal) goto loc_0086CCB9;
loc_0086C3CC:
    goto loc_0086D9E2;
loc_0086C3D4:
    if ((*(uint64_t *)(v_stack_m1F0)) != v_stack_m1F8) goto loc_0086CAF9;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m1F0 + 0x8))) != v_stack_m1F0) goto loc_0086CAF9;
    v_stack_m1F0 = *(uint64_t *)(v_stack_m1F0 + 0x8);
    *(uint64_t *)(*(uint64_t *)(v_stack_m1F0 + 0x8)) = v_stack_m1F8;
    v_stack_mC8 = *(uint64_t *)(v_stack_m1F0 + 0x18);
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m1F0 + 0x10) + 0x18) + 0x8), v_stack_mE0, v_stack_m1F8, Arg4);
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m1F0 + 0x10) + 0x38)) & (-2);
    if (condition_is_not_equal) goto loc_0086CE33;
loc_0086C441:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m1F0, Arg2, v_stack_m1F8, Arg4);
    goto loc_0086C368;
loc_0086C454:
    Arg1 = (uint32_t)((v_stack_m1F0) & (0xFFFFFC03ULL));
    v_stack_m1D0 = local_r14;
    v_stack_m1D0 = Arg1;
    result = (uint32_t)((result) >> (2));
    v_stack_m220 = (uint32_t)((uint8_t)(result));
    result = ExpLookupHandleTableEntry(v_stack_m238, v_stack_m1D0, v_stack_m1F8, Arg4);
    if (result == 0) goto loc_0086CBA8;
    if (*(uint64_t *)(result) == 0) goto loc_0086CB5B;
loc_0086C492:
    *(uint64_t *)(*(uint64_t *)(result) + (uint32_t)(v_stack_m220) * 8) = v_stack_m188;
    goto loc_0086C135;
loc_0086C4A2:
    v_stack_m230 = *(uint64_t *)(v_rip + 0x75A607);
    goto loc_0086BA34;
loc_0086C4B9:
    v_stack_m208 = 447;
    v_stack_m218 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x59EECD)));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x59EECD)))), (uint32_t)(0x7153624FULL), Arg4);
    if (result == 0) goto loc_0086D1D3;
    v_stack_m2A8 = (uint8_t)(v_stack_m128);
    v_stack_m2B0 = (uint32_t)(Arg5) + 76;
    v_stack_m2B8 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(Arg5) + 0x64)));
    v_stack_m2C0 = local_r12 - 8;
    v_stack_m210 = local_r12 - 8;
    v_stack_m248 = 1;
    if ((*(uint64_t *)((uint32_t)(Arg5) + 0x98)) != (v_rip + 18361)) goto loc_0086D01F;
    v_stack_m2C8 = v_stack_m218;
    result = CmpSecurityMethod(local_r12, 1, v_stack_m208, result);
loc_0086C543:
    if (((uint32_t)(result)) == 0xC0000023ULL) goto loc_0086D825;
loc_0086C550:
    if (sign_flag) goto loc_0086CF68;
    Arg4 = 0;
    goto loc_0086BB21;
loc_0086C560:
    v_stack_m238 = 0;
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0x75A607) + 0x1E8)) & (-2);
    if (condition_is_not_equal) goto loc_0086C5B7;
loc_0086C580:
    v_stack_m238 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x75A607) + 0x300);
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x75A607) + 0x300) != 0) goto loc_0086C5D0;
    result = (*(uint64_t *)(*(uint64_t *)(v_rip + 0x75A607) + 0x1E8)) & (-2);
    if (condition_is_equal) goto loc_0086C5CB;
    result = ExfReleaseRundownProtection(*(uint64_t *)(v_rip + 0x75A607) + 488, result - 2, v_stack_m208, Arg4);
loc_0086C5AD:
    goto loc_0086C3CC;
loc_0086C5B7:
    result = ExfAcquireRundownProtection((uint32_t)(0xC000010AULL), result - 2, v_stack_m208, Arg4);
    if ((uint8_t)(result) != 0) goto loc_0086C580;
loc_0086C5CB:
    if (v_stack_m238 == 0) goto loc_0086C5AD;
loc_0086C5D0:
    Arg4 = 0;
    v_stack_m240 = 1;
    goto loc_0086BA38;
loc_0086C5DF:
    goto loc_0086BF6C;
loc_0086C5E7:
    if ((*(uint32_t *)(v_stack_m1F0 + 0x18)) != 0) goto loc_0086BA56;
loc_0086C5F1:
    if ((*(uint32_t *)(v_stack_m1F0 + 0x18)) < 0) {
    }
    if ((((uint32_t)(result)) & (0xF0000000ULL)) == 0) goto loc_0086C65D;
    result = (local_r12 - 48) >> (8);
    Arg1 = ((uint8_t)(result)) ^ (*(uint8_t *)(local_r12 - 0x18));
    Arg1 = (Arg1) ^ (*(uint8_t *)(v_rip + 0x75A822));
    local_rbx = result;
    if (sign_flag) {
        local_rbx = (uint32_t)((result) | (*(uint32_t *)(*(uint64_t *)(v_rip - 0x86C606 + Arg1 * 8 + 0xFC7800) + 0x4C)));
    }
    if (!(condition_is_above_or_equal)) {
        local_rbx = (uint32_t)((local_rbx) | (*(uint32_t *)(*(uint64_t *)(v_rip - 0x86C606 + Arg1 * 8 + 0xFC7800) + 0x50)));
    }
    if (!(condition_is_above_or_equal)) {
        local_rbx = (uint32_t)((local_rbx) | (*(uint32_t *)(*(uint64_t *)(v_rip - 0x86C606 + Arg1 * 8 + 0xFC7800) + 0x54)));
    }
    if (!(condition_is_above_or_equal)) {
        local_rbx = (uint32_t)((local_rbx) | (*(uint32_t *)(*(uint64_t *)(v_rip - 0x86C606 + Arg1 * 8 + 0xFC7800) + 0x58)));
    }
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFFULL));
loc_0086C65D:
    v_stack_m244 = (uint32_t)(local_rbx);
    goto loc_0086BE25;
loc_0086C665:
    *(uint32_t *)(v_stack_m1F0 + 0x10) = 0;
    v_stack_m214 = (uint32_t)((uint32_t)(0xC000010AULL));
    goto loc_0086BE1B;
loc_0086C67B:
    result = 0;
    goto loc_0086BBF5;
loc_0086C682:
    if (v_stack_m118 == 0) goto loc_0086C2B3;
    *(uint64_t *)(v_stack_m118) = v_stack_m1F0;
    goto loc_0086C2B3;
loc_0086C69A:
    if (v_stack_m118 == (*(uint64_t *)(v_rip + 0x75A43F))) goto loc_0086C299;
    goto loc_0086C2A6;
loc_0086C6AC:
    goto loc_0086BE8A;
loc_0086C6B5:
    if ((*(uint64_t *)(v_stack_m1F0 + 0x30)) >= local_rbx) goto loc_0086CB38;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(*(uint64_t *)(v_stack_m1F0 + 0x30) + 0x30), 1, v_rip - 8832518, Arg4);
loc_0086C6F3:
    result = ExAcquireResourceSharedLite(*(uint64_t *)(local_rbx + 0x30), 1, v_rip - 8832518, Arg4);
    if (((*(uint32_t *)(local_rbx + 0xC8)) & (0x4000ULL)) != 0) goto loc_0086CEDF;
loc_0086C70A:
loc_0086C70E:
    result = ExReleaseResourceLite(*(uint64_t *)(*(uint64_t *)(v_stack_m1F0 + 0x30) + 0x30), 1, v_rip - 8832518, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), 1, v_rip - 8832518, Arg4);
    result = ExReleaseResourceLite(*(uint64_t *)(local_rbx + 0x30), 1, v_rip - 8832518, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), 1, v_rip - 8832518, Arg4);
    goto loc_0086C2AA;
loc_0086C741:
    Arg2 = 0;
    result = ExFreePoolWithTag(local_rbx, Arg2, v_rip - 8832518, Arg4);
    goto loc_0086BCDE;
loc_0086C750:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m1F0 + 0x30) + 0xC8)) == (*(uint64_t *)(v_stack_m1F0 + 0x30) + 200)) goto loc_0086BFC8;
    result = (local_r12 - 48) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(local_r12 - 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0x75A6CD));
    v_stack_m110 = v_xmm0;
    v_stack_m100 = v_xmm0;
    Arg2 = 0;
    v_stack_m1C8 = 0;
    Arg1 = (uint32_t)((0) & (0xFFFFFFFEULL));
    v_stack_m1D8 = 0;
    v_stack_mF0 = v_xmm0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip - 0x86C789 + arg2 * 8 + 0xFC7800) + 0x60))) & ((uint32_t)(local_rbx)));
    v_stack_m148 = local_r12;
    v_stack_m138 = 0;
    v_stack_m1C0 = (uint32_t)(result);
    v_stack_m130 = v_stack_mB0;
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(v_stack_m245)));
    v_stack_m150 = 1;
    v_stack_m14C = Arg1;
    v_stack_mA8 = v_xmm0;
    v_stack_m140 = *(uint64_t *)(v_rip - 0x86C789 + arg2 * 8 + 0xFC7800);
    v_stack_mAC = (uint32_t)(local_rbx);
    v_stack_mB0 = (uint32_t)(local_rbx);
    v_stack_m200 = *(uint64_t *)(v_rip - 0x86C789 + arg2 * 8 + 0xFC7800) + 200;
    v_stack_m198 = *(uint64_t *)(v_rip - 0x86C789 + arg2 * 8 + 0xFC7800);
    result = ObfReferenceObjectWithTag(v_stack_m148, (uint32_t)(0x6243624FULL), v_rip - 8832518, Arg4);
    Arg3 = 0;
    v_stack_m220 = *(uint64_t *)(v_rip - 0x86C789 + arg2 * 8 + 0xFC7800) + 184;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(v_rip - 0x86C789 + arg2 * 8 + 0xFC7800) + 184, Arg2, Arg3, Arg4);
    result = 0;
    local_r10 = v_stack_m220;
    if (!(condition_is_equal)) {
        Arg4 = v_stack_m220;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_stack_m220;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
        local_r10 = v_stack_m220;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
loc_0086C894:
    if ((*(uint64_t *)(v_stack_m200)) == v_stack_m200) goto loc_0086C9FD;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m200) + 0x14)))) & (1)) == 0) goto loc_0086C9ED;
    if (((v_stack_m150) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m200) + 0x10))))) == 0) goto loc_0086C9ED;
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m200) + 0x38)) & (-2);
    if (condition_is_not_equal) goto loc_0086D002;
loc_0086C8D1:
    Arg1 = (*(uint64_t *)(local_r10)) & (-16);
    Arg2 = *(uint64_t *)(local_r10) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(local_r10))) & (2)) != 0) goto loc_0086CCA0;
    if ((((uint8_t)(*(uint64_t *)(local_r10))) & (2)) != 0) goto loc_0086CCA0;
loc_0086C903:
    result = KeAbPostRelease(local_r10, Arg2, Arg3, Arg4);
    if ((((uint8_t)(*(uint64_t *)(local_r10))) & (2)) != 0) goto loc_0086C931;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    }
    if (v_stack_m1D8 == 0) goto loc_0086C959;
    result = (*(uint64_t *)(v_stack_m1D8)) & (-2);
    if (condition_is_not_equal) goto loc_0086D0A0;
loc_0086C953:
    result = 0;
    v_stack_m1D8 = 0;
loc_0086C959:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m200) + 0x30)) != 0) goto loc_0086CABC;
loc_0086C964:
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m200) + 0x28) == 0) goto loc_0086C99A;
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m200) + 0x18) + 0x8), v_stack_m150, Arg3, Arg4);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m200) + 0x30)) != 0) goto loc_0086CB24;
    v_stack_m1D8 = *(uint64_t *)(v_stack_m200) + 56;
loc_0086C991:
    result = 0;
    v_stack_m138 = 0;
loc_0086C99A:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_m220, Arg2, Arg3, Arg4);
    v_stack_m1E8 = result;
    result = 0;
    if (!(condition_is_equal)) {
        Arg3 = 0;
        Arg4 = v_stack_m220;
        Arg2 = 0;
        result = ExfAcquirePushLockSharedEx(v_stack_m220, Arg2, Arg3, Arg4);
        Arg2 = v_stack_m1E8;
    }
    if (Arg2 != NULL) {
        *(uint8_t *)(arg2 + 0xA) = 1;
    }
    goto loc_0086C894;
loc_0086C9FD:
    local_rdi = (v_stack_m198) + (184);
    Arg1 = (*(uint64_t *)(local_rdi)) & (-16);
    Arg2 = *(uint64_t *)(local_rdi) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (2)) != 0) goto loc_0086CCDD;
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (2)) != 0) goto loc_0086CCDD;
loc_0086CA39:
    result = KeAbPostRelease(local_rdi, Arg2, Arg3, Arg4);
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (2)) != 0) goto loc_0086CA67;
    result = *(uint64_t *)(gs_base + (0 + 0x188)) + 152;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x98)) != (*(uint64_t *)(gs_base + (0 + 0x188)) + 152)) {
        result = KiCheckForKernelApcDelivery(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    }
    if (v_stack_m1D8 == 0) goto loc_0086CA89;
    result = (*(uint64_t *)(v_stack_m1D8)) & (-2);
    if (condition_is_not_equal) goto loc_0086D16F;
loc_0086CA89:
    if (v_stack_m1F8 == v_stack_m1F8) goto loc_0086CB00;
loc_0086CA93:
    if (v_stack_m245 != 0) goto loc_0086D423;
    result = (uint32_t)(((uint32_t)(v_stack_mB0)) | (v_stack_m1C0));
    local_rbx = (uint32_t)((local_rbx) & ((uint32_t)(result)));
    v_stack_m244 = (uint32_t)(local_rbx);
    if (v_stack_m228 == 0) goto loc_0086BFC8;
    *(uint32_t *)(v_stack_m228 + 0x14) = (uint32_t)(local_rbx);
    goto loc_0086BFC8;
loc_0086CABC:
    result = ExAllocatePool2(256, 32, (uint32_t)(0x6C46624FULL), Arg4);
    v_stack_m1C8 = result;
    if (result == 0) goto loc_0086D434;
    Arg1 = 0;
    *(uint64_t *)(result + 0x10) = local_rdi;
    *(uint64_t *)(result + 0x18) = 0;
    if ((*(uint64_t *)(v_stack_m1F0)) == v_stack_m1F8) goto loc_0086D1A1;
loc_0086CAF9:
loc_0086CB00:
    result = ObfDereferenceObjectWithTag(v_stack_m148, (uint32_t)(0x6243624FULL), (uint32_t)(0x6C46624FULL), Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(0x6243624FULL), (uint32_t)(0x6C46624FULL), Arg4);
    goto loc_0086CA93;
loc_0086CB24:
    *(uint64_t *)(v_stack_m1C8 + 0x18) = v_stack_m138;
    goto loc_0086C991;
loc_0086CB38:
    result = ExAcquireResourceSharedLite(*(uint64_t *)(local_rbx + 0x30), (uint32_t)(0x6243624FULL), (uint32_t)(0x6C46624FULL), Arg4);
    goto loc_0086C6F3;
loc_0086CB5B:
    result = ExpAllocateTablePagedPool(*(uint64_t *)(v_stack_m220 + 0x10), (uint32_t)(0x800ULL), (uint32_t)(0x6C46624FULL), Arg4);
    if (result == 0) goto loc_0086D1CA;
    result = 0;
    if (condition_is_equal) goto loc_0086CE5D;
    result = ExpFreeTablePagedPool(*(uint64_t *)(v_stack_m238 + 0x10), 0, (uint32_t)(0x800ULL), Arg4);
    if (*(uint64_t *)(local_rbx) != 0) goto loc_0086C492;
loc_0086CBA8:
    v_stack_m238 = local_r14;
    local_r14 = (uint32_t)((local_r14) & (0xFFFFFFFCULL));
    v_stack_m238 = (uint32_t)(local_r14);
    if ((*(uint32_t *)(v_stack_m238 + 0x4)) == 0) goto loc_0086D018;
    result = ExpGetHandleExtraInfo(v_stack_m238, v_stack_m238, (uint32_t)(0x800ULL), Arg4);
    Arg1 = 0;
    if (result != 0) {
        *(uint64_t *)(result) = 0;
    }
    *(uint64_t *)(local_rdi + 0x8) = 0;
    result = (uint8_t)((*(uint8_t *)(v_stack_m238 + 0x2C)) & (1));
    v_stack_m248 = (uint8_t)(result);
    if (condition_is_not_equal) goto loc_0086CD36;
loc_0086CBF1:
    Arg3 = 0;
    local_rbx = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))))) + 1;
    Arg2 = 0;
    local_rbx = (local_rbx) << (6);
    local_rbx = (local_rbx) + (v_stack_m238);
    result = KeAbPreAcquire(local_rbx, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rbx;
        Arg2 = result;
        Arg1 = local_rbx;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (v_stack_m248 != 0) goto loc_0086CCC3;
    *(uint64_t *)(local_rdi + 0x8) = *(uint64_t *)(local_rbx + 0x8);
    if (*(uint64_t *)(local_rbx + 0x8) == 0) {
        *(uint64_t *)(local_rbx + 0x10) = local_rdi;
    }
    *(uint64_t *)(local_rbx + 0x8) = local_rdi;
loc_0086CC4C:
    result = (uint8_t)((-1) & (6));
    if (((uint8_t)(result)) == 2) goto loc_0086CF8D;
loc_0086CC65:
    result = KeAbPostRelease(local_rbx, Arg2, Arg3, Arg4);
    result = 0;
    goto loc_0086C15F;
loc_0086CC77:
    if (((*(uint8_t *)(v_stack_m220 + 0x42)) & (8)) == 0) goto loc_0086CE3D;
loc_0086CC82:
    v_stack_m2C8 = Arg4;
    result = KeBugCheckEx(393, local_r12 - 48, v_stack_m220, 1);
loc_0086CCA0:
    result = ExfReleasePushLock(v_stack_m238, local_r12 - 48, v_stack_m220, 1);
    goto loc_0086C903;
loc_0086CCB1:
    goto loc_0086C042;
loc_0086CCB9:
    result = ExfReleaseRundownProtection(v_stack_m238, 1, v_stack_m220, 1);
    goto loc_0086C3CC;
loc_0086CCC3:
    if (*(uint64_t *)(local_rbx + 0x10) == 0) goto loc_0086D42B;
    *(uint64_t *)(*(uint64_t *)(local_rbx + 0x10) + 0x8) = local_rdi;
loc_0086CCD4:
    *(uint64_t *)(local_rbx + 0x10) = local_rdi;
    goto loc_0086CC4C;
loc_0086CCDD:
    result = ExfReleasePushLock(local_rdi, 1, v_stack_m220, 1);
    goto loc_0086CA39;
loc_0086CCEA:
    v_stack_m2B8 = v_stack_m1B0;
    v_stack_m2C0 = v_stack_m220;
    v_stack_m2C8 = (uint8_t)(local_rbx);
    result = ObpInsertOrLocateNamedObject(v_stack_m230, local_r12, v_stack_m244, v_stack_m228);
    if (sign_flag) goto loc_0086C3A6;
    if (v_stack_m1B0 != local_r12) goto loc_0086D090;
    result = 0;
    v_stack_m1B0 = 0;
    goto loc_0086BE80;
loc_0086CD36:
    goto loc_0086CBF1;
loc_0086CD3D:
    v_stack_m90 = *(uint64_t *)(v_rip + 0x76CDBC);
    v_stack_m98 = 1;
    v_stack_m94 = 1;
    v_stack_m88 = (uint32_t)(v_stack_m228);
    if ((uint8_t)(v_stack_m128) == 0) goto loc_0086D17C;
    if (*(uint64_t *)(v_stack_m228 + 0x20) != 0) goto loc_0086D160;
loc_0086CD80:
    v_stack_m2C8 = (uint8_t)(v_stack_m128);
    result = SepPrivilegeCheck(*(uint64_t *)(v_stack_m228 + 0x30), v_stack_m90, 1, 1);
    if ((uint8_t)(result) != 0) goto loc_0086D17C;
loc_0086CDA2:
    Arg4 = 0;
    Arg1 = 0;
    result = SePrivilegedServiceAuditAlarm(Arg1, v_stack_m228 + 32, v_stack_m98, Arg4);
    v_stack_m214 = (uint32_t)((uint32_t)(0xC0000061ULL));
    goto loc_0086C3A2;
loc_0086CDC4:
    result = ExfTryToWakePushLock(v_stack_m230, v_stack_m228 + 32, v_stack_m98, Arg4);
    goto loc_0086C0E8;
loc_0086CDD1:
    if (((uint32_t)(0xC0000061ULL)) != (*(uint64_t *)(v_rip + 0x6A2880))) goto loc_0086BFAE;
    if (v_stack_m246 != 0) goto loc_0086BFAE;
    result = ObpCreateSymbolicLinkName(local_r12, v_stack_m228 + 32, v_stack_m98, Arg4);
    goto loc_0086BFAE;
loc_0086CDF8:
    result = ObpDecrementHandleCount(v_stack_m230, v_stack_m128, v_stack_m98, Arg4);
    if ((uint32_t)(v_stack_m220) != 0) {
        Arg3 = 0x6E48624FULL;
        Arg2 = (uint32_t)(v_stack_m220);
        Arg1 = v_stack_m228;
        result = ObDereferenceObjectExWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_0086C2D7;
loc_0086CE33:
    result = ExfReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    goto loc_0086C441;
loc_0086CE3D:
    if (((*(uint8_t *)(local_r12 - 0x16)) & (2)) == 0) goto loc_0086BB1E;
    goto loc_0086CC82;
loc_0086CE4E:
    goto loc_0086BBF5;
loc_0086CE5D:
    *(uint64_t *)(Arg1 + (uint32_t)(v_stack_m220) * 8) = v_stack_m188;
    goto loc_0086C135;
loc_0086CE76:
    if (*(uint64_t *)(local_r12) != 0) goto loc_0086D14C;
    if (v_stack_m180 != ((uint32_t)(v_stack_m220))) goto loc_0086D21A;
    Arg1 = ((uint32_t)(0xC000009AULL) - 48) >> (8);
    Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)((uint32_t)(0xC000009AULL) - 0x18)));
    Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(v_rip + 0x759FA7)));
    if (((uint8_t)(Arg1)) != (*(uint8_t *)(*(uint64_t *)(v_rip + 0x759C4C) + 0x28))) goto loc_0086CEBA;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL) + 0x8) + 0x34)))) & (16)) != 0) goto loc_0086C1C9;
loc_0086CEBA:
    local_r12 = 0;
    if (*(uint64_t *)(v_stack_m228 + 0x48) == 0) goto loc_0086CF9A;
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m228 + 0x48) + 0x38) == 0) goto loc_0086CF9A;
    goto loc_0086CF9D;
loc_0086CEDF:
    if ((*(uint32_t *)((uint32_t)(v_stack_m244) + 0xC4)) < 2) goto loc_0086C70A;
    result = RtlEqualSid(*(uint64_t *)(*(uint64_t *)((uint32_t)(0xC000009AULL) + 0x98)), *(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_m244) + 0x98)), *(uint64_t *)(*(uint64_t *)(v_stack_m228 + 0x48) + 0x38), Arg4);
    if ((uint8_t)(result) != 0) goto loc_0086C70E;
    result = OBJECT_HEADER_TO_HANDLE_REVOCATION_INFO(v_stack_m228 - 48, *(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_m244) + 0x98)), *(uint64_t *)(*(uint64_t *)(v_stack_m228 + 0x48) + 0x38), Arg4);
    if (result == 0) goto loc_0086C70E;
    v_stack_m2C0 = 0;
    Arg4 = 0;
    Arg2 = 0;
    v_stack_m2C8 = 1;
    result = SepSidInTokenSidHash((uint32_t)(0xC000009AULL) + 808, Arg2, *(uint64_t *)(v_rip + 0x698946), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0086C70E;
    Arg1 = (*(uint64_t *)((uint32_t)(v_stack_m244) + 0xD8)) + (136);
    result = ObHandleRevocationBlockAddObject(Arg1, v_stack_m228, *(uint64_t *)(v_rip + 0x698946), Arg4);
    goto loc_0086C70E;
loc_0086CF68:
    Arg2 = 0;
    result = ExFreePoolWithTag((uint32_t)(v_stack_m244), Arg2, *(uint64_t *)(v_rip + 0x698946), Arg4);
loc_0086CF72:
    v_stack_m214 = (uint32_t)((uint32_t)(0xC000009AULL));
loc_0086CF75:
    if (sign_flag) goto loc_0086C3A2;
    Arg4 = 0;
    goto loc_0086BE25;
loc_0086CF8D:
    result = ExfTryToWakePushLock((uint32_t)(v_stack_m244), Arg2, *(uint64_t *)(v_rip + 0x698946), Arg4);
    goto loc_0086CC65;
loc_0086CF9A:
loc_0086CF9D:
    result = ObpAllocateAndQuerySecurityDescriptorInfo((uint32_t)(0xC000009AULL), 32, 0, v_stack_m1A8);
    local_rbx = (uint32_t)(v_stack_m244);
    if (!(sign_flag)) {
        local_rbx = v_stack_m1A8;
        Arg2 = v_stack_m1A8;
        Arg3 = 1;
        Arg1 = v_stack_m128;
        result = ObpSetObjectAuditInfo(Arg1, Arg2, Arg3, v_stack_m1A8);
    }
    Arg2 = 0;
    goto loc_0086C1C9;
loc_0086CFCF:
    if (sign_flag) goto loc_0086C3A2;
    result = EtwpTraceHandle((uint32_t)(0x1120ULL), *(uint64_t *)(v_stack_m128), v_stack_m228, v_stack_m210);
    goto loc_0086C3A2;
loc_0086CFF0:
    result = ObDereferenceSecurityDescriptor((uint32_t)(0xC000009AULL), 1, v_stack_m228, v_stack_m210);
    goto loc_0086BE14;
loc_0086D002:
    result = ExfAcquireRundownProtection((uint32_t)(0xC000009AULL), 1, v_stack_m228, v_stack_m210);
    if ((uint8_t)(result) == 0) goto loc_0086C9ED;
    goto loc_0086C8D1;
loc_0086D018:
    Arg1 = 0;
    goto loc_0086CBD5;
loc_0086D01F:
    if (result != (v_rip + 27226)) goto loc_0086D97A;
    v_stack_m2C8 = v_stack_m218;
    result = IopGetSetSecurityObject(1, 1, v_stack_m228, local_rbx);
    goto loc_0086C543;
loc_0086D048:
    result = ObpReferenceSecurityDescriptorSlow(1 - 48, 1, (uint32_t)(0xC000009AULL), local_rbx);
    goto loc_0086BDCF;
loc_0086D05D:
    Arg2 = 0;
    result = ObpPushStackInfo(result - 48, Arg2, Arg2 + 1, (uint32_t)(0x746C6644ULL));
    result = ObpPushStackInfo(result - 48, 1, 1, (uint32_t)(0x6E48624FULL));
    goto loc_0086C186;
loc_0086D090:
    v_stack_m228 = result;
    v_stack_m246 = 1;
    goto loc_0086BE80;
loc_0086D0A0:
    result = ExfReleaseRundownProtection(result - 48, 1, 1, (uint32_t)(0x6E48624FULL));
    goto loc_0086C953;
loc_0086D0AA:
    v_stack_m248 = 1;
    result = ((uint32_t)(v_stack_m1D8)) + 1;
    v_stack_m1C8 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m1D8))));
    result = (result) << (6);
    Arg2 = 0;
    result = (result) + (1);
    Arg3 = 0;
    v_stack_m1E8 = result;
    result = KeAbPreAcquire(1 + 56, Arg2, Arg3, (uint32_t)(0x6E48624FULL));
    v_stack_m198 = result;
    if (!(condition_is_above_or_equal)) {
        Arg3 = 1 + 56;
        Arg2 = result;
        Arg1 = 1 + 56;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, (uint32_t)(0x6E48624FULL));
        result = v_stack_m198;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = (uint32_t)(v_stack_m220);
    if (((uint32_t)((uint32_t)(v_stack_m220))) == (*(uint32_t *)(v_stack_m238))) {
        Arg2 = v_stack_m1E8;
        result = ExpAllocateHandleTableEntrySlow(v_stack_m238, Arg2, Arg3, (uint32_t)(0x6E48624FULL));
        v_stack_m248 = (uint8_t)(result);
    }
    Arg2 = (uint8_t)((-1) & (6));
    if (((uint8_t)(Arg2)) == 2) goto loc_0086D990;
loc_0086D12B:
    result = KeAbPostRelease(1 + 56, Arg2, Arg3, (uint32_t)(0x6E48624FULL));
    if (v_stack_m248 == 0) goto loc_0086C15F;
    Arg4 = 0;
    goto loc_0086C053;
loc_0086D14C:
    local_rdi = 0;
    v_stack_m190 = 0;
    v_stack_m1B8 = Arg2;
    goto loc_0086C1F0;
loc_0086D160:
    if ((*(uint32_t *)(v_stack_m228 + 0x28)) >= 2) goto loc_0086CD80;
    goto loc_0086CDA2;
loc_0086D16F:
    result = ExfReleaseRundownProtection(Arg2, Arg2, v_stack_m238, Arg4);
    goto loc_0086CA89;
loc_0086D17C:
    result = SeAppendPrivileges(v_stack_m228, v_stack_m98, v_stack_m238, Arg4);
    Arg4 = 0;
    goto loc_0086BD6B;
loc_0086D1A1:
    *(uint64_t *)(result + 0x8) = v_stack_m228;
    *(uint64_t *)(result) = v_stack_m1F8;
    *(uint64_t *)(v_stack_m228) = result;
    v_stack_m1F0 = result;
    goto loc_0086C964;
loc_0086D1B8:
    result = ObDereferenceSecurityDescriptor((uint32_t)((uint32_t)((uint32_t)(v_stack_m1D8))), 1, v_stack_m238, Arg4);
    goto loc_0086BF51;
loc_0086D1CA:
    goto loc_0086CBA8;
loc_0086D1D3:
    goto loc_0086CF72;
loc_0086D1DD:
    result = ObpReferenceSecurityDescriptorSlow(*(uint64_t *)(v_stack_m228 + 0x48), 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1D8))), Arg4);
    goto loc_0086BF12;
loc_0086D1F0:
    result = ObDereferenceSecurityDescriptor(result, 1, (uint32_t)((uint32_t)((uint32_t)(v_stack_m1D8))), Arg4);
    goto loc_0086BCDE;
loc_0086D202:
    result = ObpReferenceSecurityDescriptorSlow(result - 48, 1, result, Arg4);
    Arg4 = 0;
    goto loc_0086BB11;
loc_0086D21A:
    Arg3 = 0;
    result = ObpSetObjectAuditInfo(*(uint64_t *)(v_stack_m228 + 0x48), v_stack_m180, Arg3, Arg4);
    Arg2 = 0;
    v_stack_m1B8 = 0;
    local_rdi = 0;
    v_stack_m190 = 0;
    goto loc_0086C1E3;
loc_0086D23F:
    v_stack_m2B8 = 2;
    v_stack_m2C0 = 512;
    v_stack_m2C8 = 0;
    result = ZwDuplicateObject(-1, 0, -1, v_stack_m1B8);
    local_rdi = 0;
    local_rbx = result;
    if (!(sign_flag)) {
        Arg1 = v_stack_m1B8;
        result = v_stack_m120;
        v_stack_m2C0 = 0;
        Arg4 = 0;
        Arg3 = 0;
        v_stack_m2C8 = result;
        Arg2 = 0;
        v_stack_m120 = 0;
        result = ObReferenceObjectByHandle(Arg1, Arg2, Arg3, Arg4);
        local_rbx = v_stack_m120;
    }
    Arg4 = 0;
    result = SepAdtClassifyObjectIntoSubCategory(local_rbx, v_stack_m228 + 144, 1, Arg4);
    v_stack_m248 = (uint16_t)(result);
    if (local_rbx != 0) {
        Arg1 = local_rbx;
        result = ObfDereferenceObject(Arg1, v_stack_m228 + 144, 1, Arg4);
    }
    if (v_stack_m1B8 != 0) {
        result = ZwClose(v_stack_m1B8, v_stack_m228 + 144, 1, Arg4);
        v_stack_m1B8 = 0;
    }
    result = PsGetCurrentProcessId(v_stack_m1B8, v_stack_m228 + 144, 1, Arg4);
    v_stack_m258 = v_stack_m228;
    v_stack_m260 = *(uint64_t *)(v_stack_m228 + 0x48) + 32;
    result = 0;
    v_stack_m268 = 0;
    v_stack_m270 = 0;
    v_stack_m278 = 0;
    v_stack_m280 = 2;
    v_stack_m288 = 0;
    v_stack_m290 = 1;
    v_stack_m298 = *(uint64_t *)(*(uint64_t *)(v_stack_m228 + 0x48));
    v_stack_m2A0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m228 + 0x14)));
    v_stack_m2A8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m228 + 0x18)));
    v_stack_m2B0 = *(uint64_t *)(v_stack_m228 + 0x30);
    v_stack_m2B8 = *(uint64_t *)(v_stack_m228 + 0x20);
    v_stack_m2C0 = 0;
    v_stack_m2C8 = v_stack_m228 + 128;
    result = SepAdtOpenObjectAuditAlarm((uint16_t)(v_stack_m248), v_rip - 8830833, v_stack_m190, v_stack_m228 + 144);
    v_stack_m290 = v_stack_m228;
    v_stack_m298 = result;
    v_stack_m2A0 = 1;
    v_stack_m2A8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m228 + 0x14)));
    v_stack_m2B0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m228 + 0x18)));
    v_stack_m2B8 = *(uint64_t *)(v_stack_m228 + 0x30);
    v_stack_m2C0 = *(uint64_t *)(v_stack_m228 + 0x20);
    v_stack_m248 = (uint8_t)(result);
    v_stack_m2C8 = v_stack_m228 + 128;
    result = SepAdtStagingEvent((uint16_t)(v_stack_m248), v_rip - 8830833, v_stack_m190, v_stack_m228 + 144);
    goto loc_0086C208;
loc_0086D3C8:
    if ((*(uint8_t *)(v_stack_m228 + 0x7C)) == 0) goto loc_0086D23F;
    v_stack_m2A0 = 1;
    v_stack_m2A8 = *(uint64_t *)(*(uint64_t *)(v_stack_m228 + 0x48));
    v_stack_m2B0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m228 + 0x14)));
    v_stack_m2B8 = *(uint64_t *)(v_stack_m228 + 0x38);
    v_stack_m2C0 = *(uint64_t *)(v_stack_m228 + 0x30);
    v_stack_m2C8 = *(uint64_t *)(v_stack_m228 + 0x20);
    result = SepAdtPrivilegeObjectAuditAlarm(v_rip - 8831052, v_stack_m228 + 144, v_stack_m228 + 128, 0);
    goto loc_0086C208;
loc_0086D423:
    goto loc_0086BFC8;
loc_0086D42B:
    *(uint64_t *)((uint32_t)(v_stack_m244) + 0x8) = v_stack_m248;
    goto loc_0086CCD4;
loc_0086D434:
    result = ExReleaseRundownProtection(v_stack_m248 + 56, v_stack_m228 + 144, v_stack_m228 + 128, 0);
    if (v_stack_m1F8 == v_stack_m1F8) goto loc_0086D8A4;
    result = 0;
    v_stack_mF0 = 0xC000009AULL;
    v_stack_mF8 = 0;
    v_stack_mEC = 0;
    v_stack_mE4 = 0;
    v_stack_m110 = (uint32_t)((uint32_t)(v_stack_m150));
    v_stack_m10C = (uint32_t)((uint32_t)(v_stack_m14C));
    v_stack_m100 = v_stack_m140;
    v_stack_m108 = v_stack_m148;
    result = ObpCallPostOperationCallbacks(v_stack_m110, v_stack_m1F8, v_stack_m228 + 128, 0);
loc_0086D4A9:
    result = (*(uint64_t *)(v_stack_m228 + 0x48)) >> (8);
    Arg1 = ((uint8_t)(result)) ^ (*(uint8_t *)(*(uint64_t *)(v_stack_m228 + 0x48) + 0x18));
    Arg1 = (Arg1) ^ (*(uint8_t *)(v_rip + 0x759982));
    v_stack_m80 = v_xmm0;
    v_stack_m70 = v_xmm0;
    Arg1 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m200 = 0;
    if (((*(uint8_t *)(*(uint64_t *)(v_rip - 0x86D4D4 + Arg1 * 8 + 0xFC7800) + 0x42)) & (16)) != 0) goto loc_0086D651;
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m228 + 0x48) + 0x1B)) & (8)) != 0) goto loc_0086D651;
loc_0086D518:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x86D4D4 + Arg1 * 8 + 0xFC7800) + 0x80)) == 0) goto loc_0086D5AD;
    v_stack_m210 = 0;
    v_stack_m248 = 0;
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) != v_stack_m230) {
        v_stack_m248 = 1;
        result = PsGetProcessServerSilo(v_stack_m230, v_stack_m1F8, v_stack_m228 + 128, 0);
        Arg1 = result;
        result = PsAttachSiloToCurrentThread(Arg1, v_stack_m1F8, v_stack_m228 + 128, 0);
        Arg1 = v_stack_m230;
        Arg2 = v_stack_m80;
        v_stack_m210 = result;
        result = KeStackAttachProcess(Arg1, Arg2, v_stack_m228 + 128, 0);
        Arg1 = v_stack_m230;
    }
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x86D4D4 + Arg1 * 8 + 0xFC7800) + 0x80)) != (v_rip - 39595)) goto loc_0086D5DE;
    result = CmpCloseKeyObject(Arg1, *(uint64_t *)(v_stack_m228 + 0x48) + 48, (uint32_t)(v_stack_m200), -1);
loc_0086D590:
    if (v_stack_m248 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m80;
        result = KiUnstackDetachProcess(Arg1, Arg2, (uint32_t)(v_stack_m200), -1);
        Arg1 = v_stack_m210;
        result = PsDetachSiloFromCurrentThread(Arg1, Arg2, (uint32_t)(v_stack_m200), -1);
    }
    if (-1 == 1) {
        Arg1 = *(uint64_t *)(v_stack_m228 + 0x48);
        result = ObpDeleteNameCheck(Arg1, Arg2, (uint32_t)(v_stack_m200), -1);
    }
    if ((uint32_t)(v_stack_m220) == 0) goto loc_0086C3A2;
    result = ObDereferenceObjectExWithTag(v_stack_m248, (uint32_t)((uint32_t)(v_stack_m220)), (uint32_t)(0x746C6644ULL), -1);
    goto loc_0086C3A2;
loc_0086D5DE:
    if (result != (v_rip + 1702091)) goto loc_0086D788;
    if (-1 != 1) goto loc_0086D590;
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m228 + 0x48) + 0x92)) & (2)) == 0) goto loc_0086D642;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x69223B), v_rip - 8768900, (uint32_t)(0x746C6644ULL), -1);
    if ((uint8_t)(result) != 0) {
        result = *(uint64_t *)(*(uint64_t *)(v_stack_m228 + 0x48) + 0x50);
        Arg2 = v_rip - 8768920;
        Arg1 = *(uint64_t *)(v_rip + 0x692219);
        result = (result) + (40);
        v_stack_m2C0 = result;
        Arg4 = -1;
        result = 0;
        Arg3 = 0;
        v_stack_m2C8 = 0;
        result = EtwpEventWriteTemplateSessAndProv(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_0086D590;
loc_0086D651:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(v_stack_m228 + 0x48) + 16, Arg2, Arg3, Arg4);
    v_stack_m1E8 = result;
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(v_stack_m228 + 0x48) + 16;
        Arg2 = result;
        Arg1 = *(uint64_t *)(v_stack_m228 + 0x48) + 16;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
        result = v_stack_m1E8;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = (-1) - (1);
    if (condition_is_not_equal) goto loc_0086D7A9;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m228 + 0x48) + 0x1B))) & (8)) == 0) goto loc_0086D7A9;
    result = (uint32_t)((*(uint8_t *)(*(uint64_t *)(v_stack_m228 + 0x48) + 0x1A)) & (31));
    Arg1 = (*(uint64_t *)(v_stack_m228 + 0x48)) - (*(uint8_t *)(result + v_rip - 0x86D6B2 * 1 + 0xF0FF80));
    local_r10 = 0;
    *(uint64_t *)(Arg1) = 0;
loc_0086D6E5:
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip - 0x86D4D4 + Arg1 * 8 + 0xFC7800) + 0x42))) & (16)) == 0) goto loc_0086D73B;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m228 + 0x48) + 0x1A))) & (4)) != 0) goto loc_0086D7B1;
loc_0086D6FD:
    if (((*(uint8_t *)(*(uint64_t *)(v_stack_m228 + 0x48) + 0x1B)) & (64)) == 0) goto loc_0086D7C7;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0x8))) & (0xFFFFFFULL));
    v_stack_m200 = (uint32_t)(Arg2);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x8)))) - 1) ^ ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x8)))))));
    result = (uint32_t)((result) & (0xFFFFFFULL));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x8)))))));
loc_0086D723:
    *(uint32_t *)(0 + 0x8) = (uint32_t)(result);
loc_0086D727:
    if ((*(uint8_t *)(0 + 0xB)) != 0) goto loc_0086D73B;
    if (((*(uint32_t *)(0 + 0x8)) & (0xFFFFFFULL)) == 0) {
        *(uint64_t *)(0) = 0;
    }
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m228 + 0x48) + 0x10)) & (-16);
    Arg3 = *(uint64_t *)(*(uint64_t *)(v_stack_m228 + 0x48) + 0x10) - 16;
    if (Arg1 <= 16) { Arg3 = 0; }
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m228 + 0x48) + 0x10))) & (2)) != 0) goto loc_0086D80A;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m228 + 0x48) + 0x10))) & (2)) != 0) goto loc_0086D80A;
loc_0086D76B:
    result = KeAbPostRelease(*(uint64_t *)(v_stack_m228 + 0x48) + 16, *(uint64_t *)(v_stack_m228 + 0x48) + 16, Arg3, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(v_stack_m228 + 0x48) + 16, Arg3, Arg4);
    Arg1 = 0;
    goto loc_0086D518;
loc_0086D788:
    if (result != (v_rip - 38607)) goto loc_0086D81B;
    result = IopCloseFile(Arg1, *(uint64_t *)(v_stack_m228 + 0x48) + 48, Arg3, *(uint64_t *)(*(uint64_t *)(v_stack_m228 + 0x48) + 0x8));
    goto loc_0086D590;
loc_0086D7A9:
    local_r10 = 0;
    goto loc_0086D6E5;
loc_0086D7B1:
    result = (uint32_t)((result) & (7));
    Arg3 = (*(uint64_t *)(v_stack_m228 + 0x48)) - (*(uint8_t *)(result + *(uint64_t *)(v_stack_m228 + 0x48) + 0x30 * 1 + 0xF0FF80));
    goto loc_0086D6FD;
loc_0086D7C7:
loc_0086D7D4:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3)))) == 0) goto loc_0086D727;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) + 0x8 + 0x8))))) & (0xFFFFFFULL));
    if (condition_is_equal) goto loc_0086D7EE;
    if ((*(uint64_t *)(*(uint64_t *)(Arg3) + 0x8)) == v_stack_m230) goto loc_0086D7F6;
loc_0086D7EE:
    Arg3 = (*(uint64_t *)(Arg3) + 8) + (16);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3)))) - 1);
    goto loc_0086D7D4;
loc_0086D7F6:
    v_stack_m200 = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) + 0x8 + 0x8)) - 1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) + 0x8 + 0x8)))));
    result = (uint32_t)((result) & (0xFFFFFFULL));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) + 0x8 + 0x8)))));
    goto loc_0086D723;
loc_0086D80A:
    result = ExfReleasePushLock((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) + 0x8 + 0x8)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) + 0x8 + 0x8)), Arg3, v_stack_m230);
    goto loc_0086D76B;
loc_0086D81B:
    result = guard_dispatch_icall((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg3) + 0x8 + 0x8)), *(uint64_t *)(v_stack_m228 + 0x48) + 16, Arg3, v_stack_m230);
    goto loc_0086D590;
loc_0086D825:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_rip - 0x86D4D4 + Arg1 * 8 + 0xFC7800), Arg2, Arg3, v_stack_m230);
    *(uint32_t *)(v_rip + 0x59DB4D) = (uint32_t)((uint32_t)(v_stack_m218));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(v_stack_m218))), (uint32_t)(0x7153624FULL), v_stack_m230);
    if (result == 0) goto loc_0086D99D;
    v_stack_m2A8 = (uint8_t)(*(uint64_t *)(v_stack_m228 + 0x48));
    v_stack_m2B0 = v_stack_m220 + 76;
    v_stack_m2B8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m220 + 0x64)));
    v_stack_m2C0 = v_stack_m210;
    v_stack_m2C8 = v_stack_m218;
    v_stack_m248 = 1;
    result = guard_dispatch_icall(v_stack_m248, 1, v_stack_m208, result);
    goto loc_0086C550;
loc_0086D8A4:
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), 1, v_stack_m208, result);
    result = ObfDereferenceObjectWithTag(v_stack_m148, (uint32_t)(0x6243624FULL), v_stack_m208, result);
    goto loc_0086D4A9;
loc_0086D8C8:
    if ((uint32_t)(v_stack_m208) == 0) goto loc_0086D96F;
loc_0086D8E6:
    if ((uint32_t)((uint32_t)(result)) == 0) goto loc_0086D8FB;
    if ((uint32_t)((uint32_t)(0x6243624FULL)) == 0) goto loc_0086D8FD;
    goto loc_0086D8FD;
loc_0086D8FB:
    result = 0;
loc_0086D8FD:
    result = ExAllocatePool2(256, v_stack_m208 + v_stack_m208 * 2 * 4 + 8 + result * 1, (uint32_t)(0x72506553ULL), result);
    v_stack_m1D0 = result;
    if (result == 0) goto loc_0086BC12;
    if (*(uint64_t *)(v_stack_m210) == 0) goto loc_0086D976;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m210)))) == 0) goto loc_0086D9A7;
loc_0086D93C:
    result = memcpy(result, *(uint64_t *)(v_stack_m210), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m210))) + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m210))) * 2 * 4 + 8)), result);
    result = SepConcatenatePrivileges(v_stack_m1D0, *(uint64_t *)(v_stack_m210), v_stack_m248, result);
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m228 + 0x48) + 0x8) + 0xB)) != 0) {
        Arg1 = *(uint64_t *)(v_stack_m210);
        Arg2 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m248, result);
    }
    *(uint64_t *)(v_stack_m210) = v_stack_m1D0;
    *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m228 + 0x48) + 0x8) + 0xB) = 1;
    goto loc_0086BC12;
loc_0086D96F:
    goto loc_0086D8E6;
loc_0086D976:
    result = 0;
    goto loc_0086D93C;
loc_0086D97A:
    v_stack_m2C8 = v_stack_m218;
    result = guard_dispatch_icall(v_stack_m1D0, Arg2, v_stack_m248, result);
    goto loc_0086C543;
loc_0086D990:
    result = ExfTryToWakePushLock(v_stack_m210, Arg2, v_stack_m248, result);
    goto loc_0086D12B;
loc_0086D99D:
    goto loc_0086CF72;
loc_0086D9A7:
    goto loc_0086D93C;
loc_0086D9AE:
    goto loc_0086CF75;
loc_0086D9B6:
    Arg4 = 0;
loc_0086D9C3:
    result = (uint32_t)(((uint32_t)(v_stack_m200)) + 1);
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m1C8)) + 1);
    v_stack_m200 = (uint32_t)(result);
    result = 0;
    if (((uint32_t)(local_rbx)) != ((uint32_t)((uint32_t)(v_stack_m1C0)))) { result = (uint32_t)(local_rbx); }
    v_stack_m1C8 = (uint32_t)(result);
    goto loc_0086C05F;
loc_0086D9E2:
    Arg1 = (v_stack_m50) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, v_stack_m238, Arg4);
    local_rsp = (local_rsp) + (680);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `- 0x30` | `64` | `R` |
| `Arg2` | `- 0x18` | `8` | `R` |
| `Arg2` | `- 0x16` | `8` | `R` |
| `Arg2` | `- 0x8` | `8` | `R` |
| `Arg2` | `- 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0086B950&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
