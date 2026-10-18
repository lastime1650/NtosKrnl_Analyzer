# NtSetInformationProcess

- RVA: `0x00AE5370`–`0x00AEA1C4` (길이 `20,052` bytes)
- VA: `0x0000000140AE5370`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CE44C`
- 디코드: `4,524`개 명령, `20,052/20,052` bytes 표시
- 미해석 바이트: `14` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **291**; 고유 호출 대상: **116**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **19**

### Outgoing calls
- `0x00AE5709` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE5720` → [PsChargeProcessNonPagedPoolQuota](../../text/2A/PsChargeProcessNonPagedPoolQuota_function_002A7B80.md) (function, `0x002A7B80`)
- `0x00AE573B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AE5763` → [KeInitializeGate](../../text/49/KeInitializeGate_function_004953F8.md) (function, `0x004953F8`)
- `0x00AE5783` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AE5797` → [PsReturnProcessNonPagedPoolQuota](../../text/41/PsReturnProcessNonPagedPoolQuota_function_0041C200.md) (function, `0x0041C200`)
- `0x00AE57A6` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE5812` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE5851` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE58C5` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE58F6` → [SeCheckPrivilegedObject](../9F/SeCheckPrivilegedObject_function_009F62CC.md) (function, `0x009F62CC`)
- `0x00AE5909` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE5925` → [KeSetPriorityAndQuantumProcess](../../text/3C/KeSetPriorityAndQuantumProcess_function_003C2EC0.md) (function, `0x003C2EC0`)
- `0x00AE5933` → [MmSetMemoryPriorityProcess](../../text/49/MmSetMemoryPriorityProcess_function_00494EF4.md) (function, `0x00494EF4`)
- `0x00AE593D` → [PspEnqueueProcessQosChangeNotification](../../text/5E/PspEnqueueProcessQosChangeNotification_function_005E2ED0.md) (function, `0x005E2ED0`)
- `0x00AE598F` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE59B0` → [PspSetProcessPriorityClass](../9F/PspSetProcessPriorityClass_function_009F61E4.md) (function, `0x009F61E4`)
- `0x00AE5A75` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00AE5A7A` → [Feature_ForegroundBoost_ApiRemoval__private_IsEnabledDeviceUsageNoInline](../../text/4B/Feature_ForegroundBoost_ApiRemoval__private_IsEnabledDeviceUsageNoInline_function_004B7A58.md) (function, `0x004B7A58`)
- `0x00AE5A91` → [PspSetProcessForegroundBackgroundRequest](../A4/PspSetProcessForegroundBackgroundRequest_function_00A45DCC.md) (function, `0x00A45DCC`)
- `0x00AE5AA0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE5B09` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE5BE9` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00AE5C07` → [PspSetProcessPriorityClass](../9F/PspSetProcessPriorityClass_function_009F61E4.md) (function, `0x009F61E4`)
- `0x00AE5C16` → [Feature_ForegroundBoost_ApiRemoval__private_IsEnabledDeviceUsageNoInline](../../text/4B/Feature_ForegroundBoost_ApiRemoval__private_IsEnabledDeviceUsageNoInline_function_004B7A58.md) (function, `0x004B7A58`)
- `0x00AE5C34` → [PspSetProcessPriorityByClassIgnoreForegroundBoost](PspSetProcessPriorityByClassIgnoreForegroundBoost_function_00AEA1CC.md) (function, `0x00AEA1CC`)
- `0x00AE5C85` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE5D48` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00AE5D4D` → [Feature_ForegroundBoost_ApiRemoval__private_IsEnabledDeviceUsageNoInline](../../text/4B/Feature_ForegroundBoost_ApiRemoval__private_IsEnabledDeviceUsageNoInline_function_004B7A58.md) (function, `0x004B7A58`)
- `0x00AE5D67` → [PspSetProcessForegroundBackgroundRequest](../A4/PspSetProcessForegroundBackgroundRequest_function_00A45DCC.md) (function, `0x00A45DCC`)
- `0x00AE5DB7` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE5DD2` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00AE5DE2` → [PsGetNextProcessThread](../8C/PsGetNextProcessThread_function_008C9CF0.md) (function, `0x008C9CF0`)
- `0x00AE5DF5` → [KeBoostPriorityThread](../../text/4D/KeBoostPriorityThread_function_004D37F8.md) (function, `0x004D37F8`)
- `0x00AE5E02` → [PsGetNextProcessThread](../8C/PsGetNextProcessThread_function_008C9CF0.md) (function, `0x008C9CF0`)
- `0x00AE5E1B` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00AE5E75` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE5E8F` → [PspSetProcessDefaultHardErrorMode](../A0/PspSetProcessDefaultHardErrorMode_function_00A041A8.md) (function, `0x00A041A8`)
- `0x00AE5EAB` → [PspSetQuotaLimits](../9B/PspSetQuotaLimits_function_009BA8A8.md) (function, `0x009BA8A8`)
- `0x00AE5F1C` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AE5F53` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00AE5F9F` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE5FAD` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AE602D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AE603E` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AE60EB` → [LpcRequestPort](../88/LpcRequestPort_function_0088A940.md) (function, `0x0088A940`)
- `0x00AE6103` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (function, `0x00209550`)
- `0x00AE6114` → [PspLockUnlockProcessExclusive](../../text/41/PspLockUnlockProcessExclusive_function_00419B48.md) (function, `0x00419B48`)
- `0x00AE611C` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AE614C` → [PspAssignPrimaryToken](../78/PspAssignPrimaryToken_function_00784870.md) (function, `0x00784870`)
- `0x00AE618A` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE61A2` → [BvgaSetVirtualFrameBuffer](../../text/4F/BvgaSetVirtualFrameBuffer_function_004FC600.md) (function, `0x004FC600`)
- `0x00AE61B3` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE61EE` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE6206` → [BvgaSetVirtualFrameBuffer](../../text/4F/BvgaSetVirtualFrameBuffer_function_004FC600.md) (function, `0x004FC600`)
- `0x00AE623C` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE6254` → [BvgaSetVirtualFrameBuffer](../../text/4F/BvgaSetVirtualFrameBuffer_function_004FC600.md) (function, `0x004FC600`)
- `0x00AE6269` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AE62A5` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE62BC` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE630A` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE6324` → [PspLockProcessExclusive](../../text/46/PspLockProcessExclusive_function_00460164.md) (function, `0x00460164`)
- `0x00AE638A` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (function, `0x004601C0`)
- `0x00AE63A5` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (function, `0x004601C0`)
- `0x00AE63D1` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AE640D` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE6435` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE64A2` → [KeVerifyGroupAffinity](../../text/47/KeVerifyGroupAffinity_function_0047B1F0.md) (function, `0x0047B1F0`)
- `0x00AE64DE` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE6506` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE6517` → [KeQueryPrimaryGroupProcess](../../text/2C/KeQueryPrimaryGroupProcess_function_002CF958.md) (function, `0x002CF958`)
- `0x00AE657A` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00AE658C` → [PspLockProcessSharedUnsafe](../../text/4A/PspLockProcessSharedUnsafe_function_004AD874.md) (function, `0x004AD874`)
- `0x00AE65B0` → [PspSetProcessAffinitySafe](../A6/PspSetProcessAffinitySafe_function_00A60904.md) (function, `0x00A60904`)
- `0x00AE65BC` → [PspUnlockProcessSharedUnsafe](../../text/4B/PspUnlockProcessSharedUnsafe_function_004B2800.md) (function, `0x004B2800`)
- `0x00AE65CD` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00AE65E8` → [PspUpdatePebForAffinityChange](../A5/PspUpdatePebForAffinityChange_function_00A50790.md) (function, `0x00A50790`)
- `0x00AE6600` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x00AE6612` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (function, `0x0025F010`)
- `0x00AE666A` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE6685` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00AE6699` → [KeSetDisableBoostProcess](../../text/3C/KeSetDisableBoostProcess_function_003C18B4.md) (function, `0x003C18B4`)
- `0x00AE66E0` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE6755` → [RtlIsSandboxedToken](../8B/RtlIsSandboxedToken_function_008B3AB0.md) (function, `0x008B3AB0`)
- `0x00AE6791` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE67A6` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (function, `0x0044BEE0`)
- `0x00AE67C5` → [ObpSetDeviceMap](../A9/ObpSetDeviceMap_function_00A925D0.md) (function, `0x00A925D0`)
- `0x00AE67F1` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AE682D` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE683F` → [PsGetProcessSessionId](../../text/22/PsGetProcessSessionId_function_002233A0.md) (function, `0x002233A0`)
- `0x00AE6859` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE6888` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AE68C4` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE6976` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE6991` → [PsSetProcessHandleTracingInformation](../78/PsSetProcessHandleTracingInformation_function_00781BB8.md) (function, `0x00781BB8`)
- `0x00AE699D` → [PsSetProcessHandleTracingInformation](../78/PsSetProcessHandleTracingInformation_function_00781BB8.md) (function, `0x00781BB8`)
- `0x00AE6A08` → [SeCheckPrivilegedObject](../9F/SeCheckPrivilegedObject_function_009F62CC.md) (function, `0x009F62CC`)
- `0x00AE6A44` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE6A5F` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00AE6A79` → [PspLockProcessExclusive](../../text/46/PspLockProcessExclusive_function_00460164.md) (function, `0x00460164`)
- `0x00AE6AF7` → [IoBoostThreadIoPriority](../../text/21/IoBoostThreadIoPriority_function_00216110.md) (function, `0x00216110`)
- `0x00AE6B06` → [PsSetIoPriorityThread](../../text/3C/PsSetIoPriorityThread_function_003C3FBC.md) (function, `0x003C3FBC`)
- `0x00AE6B22` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (function, `0x004601C0`)
- `0x00AE6B66` → [KeSetExecuteOptions](../../text/3C/KeSetExecuteOptions_function_003C1F54.md) (function, `0x003C1F54`)
- `0x00AE6B81` → [MmRemoveExecuteGrants](../../text/4A/MmRemoveExecuteGrants_function_004A8B60.md) (function, `0x004A8B60`)
- `0x00AE6BA4` → [KeQueryHeteroCpuPolicyThread](../../text/48/KeQueryHeteroCpuPolicyThread_function_00488A70.md) (function, `0x00488A70`)
- `0x00AE6BB1` → [Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting](../../text/22/Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting_function_00222FE0.md) (function, `0x00222FE0`)
- `0x00AE6BED` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE6C08` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00AE6C22` → [PspLockProcessExclusive](../../text/46/PspLockProcessExclusive_function_00460164.md) (function, `0x00460164`)
- `0x00AE6C89` → [PsSetPagePriorityThread](../../text/3C/PsSetPagePriorityThread_function_003C4138.md) (function, `0x003C4138`)
- `0x00AE6CA5` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (function, `0x004601C0`)
- `0x00AE6D4C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AE6E7C` → [PsGetNextProcessThread](../8C/PsGetNextProcessThread_function_008C9CF0.md) (function, `0x008C9CF0`)
- `0x00AE6ECC` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00AE6F14` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AE6FE1` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00AE6FFE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AE7220` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x00AE72D4` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00AE7304` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE7336` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AE7409` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE7431` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AE744F` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00AE7462` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE74DA` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x00AE74EC` → [MmValidateUserCallTarget](../AC/MmValidateUserCallTarget_function_00AC0950.md) (function, `0x00AC0950`)
- `0x00AE7508` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x00AE7522` → [PspLockProcessExclusive](../../text/46/PspLockProcessExclusive_function_00460164.md) (function, `0x00460164`)
- `0x00AE7584` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (function, `0x004601C0`)
- `0x00AE75B9` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x00AE75C1` → [MmGetMaximumUserAddress](../../text/44/MmGetMaximumUserAddress_function_004455B0.md) (function, `0x004455B0`)
- `0x00AE75E2` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x00AE75F1` → [MmValidateUserCallTarget](../AC/MmValidateUserCallTarget_function_00AC0950.md) (function, `0x00AC0950`)
- `0x00AE762A` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x00AE7640` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00AE7742` → [MmAllocateUserStack](../88/MmAllocateUserStack_function_00882B30.md) (function, `0x00882B30`)
- `0x00AE7781` → [KeIsUserCetAllowed](../../text/4A/KeIsUserCetAllowed_function_004A22B4.md) (function, `0x004A22B4`)
- `0x00AE77D5` → [PspSetupUserFiberShadowStack](../88/PspSetupUserFiberShadowStack_function_008824F0.md) (function, `0x008824F0`)
- `0x00AE7807` → [KeIsUserCetAllowed](../../text/4A/KeIsUserCetAllowed_function_004A22B4.md) (function, `0x004A22B4`)
- `0x00AE7833` → [PspFreeUserFiberShadowStack](../87/PspFreeUserFiberShadowStack_function_0087F9A0.md) (function, `0x0087F9A0`)
- `0x00AE786E` → [PspSetProcessAffinityUpdateMode](../78/PspSetProcessAffinityUpdateMode_function_007828D8.md) (function, `0x007828D8`)
- `0x00AE78CA` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE7947` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE795E` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (function, `0x0020FF80`)
- `0x00AE796B` → [SeSetVirtualizationToken](../AA/SeSetVirtualizationToken_function_00AA28B4.md) (function, `0x00AA28B4`)
- `0x00AE7973` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AE7B1E` → [ObReferenceProcessHandleTable](../89/ObReferenceProcessHandleTable_function_00893B70.md) (function, `0x00893B70`)
- `0x00AE7B42` → [ExEnableHandleExceptions](../A7/ExEnableHandleExceptions_function_00A7580C.md) (function, `0x00A7580C`)
- `0x00AE7B56` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00AE7CE7` → [PsIsSystemWideMitigationOptionSet](../AB/PsIsSystemWideMitigationOptionSet_function_00AB1B7C.md) (function, `0x00AB1B7C`)
- `0x00AE7D0C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE7D51` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE7DAF` → [SeCaptureSubjectContextEx](../8C/SeCaptureSubjectContextEx_function_008C4C90.md) (function, `0x008C4C90`)
- `0x00AE7DC0` → [RtlIsSandboxedToken](../8B/RtlIsSandboxedToken_function_008B3AB0.md) (function, `0x008B3AB0`)
- `0x00AE7DD0` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00AE7DDB` → [RtlIsSandboxedToken](../8B/RtlIsSandboxedToken_function_008B3AB0.md) (function, `0x008B3AB0`)
- `0x00AE7E3E` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AE7F89` → [RtlInterlockedSetClearBits](../../text/49/RtlInterlockedSetClearBits_function_00497378.md) (function, `0x00497378`)
- `0x00AE80E4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AE8115` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AE8151` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AE8175` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AE81DA` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AE820A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AE823F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AE8267` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AE82C6` → [RtlInterlockedSetClearBits](../../text/49/RtlInterlockedSetClearBits_function_00497378.md) (function, `0x00497378`)
- `0x00AE8342` → [RtlInterlockedSetClearBits](../../text/49/RtlInterlockedSetClearBits_function_00497378.md) (function, `0x00497378`)
- `0x00AE836C` → [RtlInterlockedSetClearBits](../../text/49/RtlInterlockedSetClearBits_function_00497378.md) (function, `0x00497378`)
- `0x00AE8494` → [RtlInterlockedSetClearBits](../../text/49/RtlInterlockedSetClearBits_function_00497378.md) (function, `0x00497378`)
- `0x00AE84E1` → [PspGetNoChildProcessRestrictedPolicy](../A1/PspGetNoChildProcessRestrictedPolicy_function_00A172B8.md) (function, `0x00A172B8`)
- `0x00AE8558` → [PspSetNoChildProcessRestrictedPolicy](../AB/PspSetNoChildProcessRestrictedPolicy_function_00AB1BE0.md) (function, `0x00AB1BE0`)
- `0x00AE856F` → [PspSetNoChildProcessRestrictedPolicy](../AB/PspSetNoChildProcessRestrictedPolicy_function_00AB1BE0.md) (function, `0x00AB1BE0`)
- `0x00AE858F` → [PspSetNoChildProcessRestrictedPolicy](../AB/PspSetNoChildProcessRestrictedPolicy_function_00AB1BE0.md) (function, `0x00AB1BE0`)
- `0x00AE85C7` → [PspGetRedirectionTrustPolicy](../A7/PspGetRedirectionTrustPolicy_function_00A769A8.md) (function, `0x00A769A8`)
- `0x00AE8623` → [PspSetRedirectionTrustPolicy](../A7/PspSetRedirectionTrustPolicy_function_00A7C2D4.md) (function, `0x00A7C2D4`)
- `0x00AE86C8` → [KeIsCoreIsolationMitigationPolicyEnforceable](../../text/4A/KeIsCoreIsolationMitigationPolicyEnforceable_function_004A7388.md) (function, `0x004A7388`)
- `0x00AE873D` → [KeSynchronizeSecurityDomain](../../text/4B/KeSynchronizeSecurityDomain_function_004B0FE0.md) (function, `0x004B0FE0`)
- `0x00AE8747` → [PspSynchronizeThreadIsolationDomains](../../text/3C/PspSynchronizeThreadIsolationDomains_function_003C479C.md) (function, `0x003C479C`)
- `0x00AE8795` → [PspApplyCoreIsolationPolicy](../78/PspApplyCoreIsolationPolicy_function_00783E48.md) (function, `0x00783E48`)
- `0x00AE8A31` → [RtlInsertDynamicUserFunctionTable](../../text/45/RtlInsertDynamicUserFunctionTable_function_004513C4.md) (function, `0x004513C4`)
- `0x00AE8A3B` → [RtlRemoveDynamicUserFunctionTable](../../text/46/RtlRemoveDynamicUserFunctionTable_function_00466514.md) (function, `0x00466514`)
- `0x00AE8A97` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE8AA9` → [ObReferenceProcessHandleTable](../89/ObReferenceProcessHandleTable_function_00893B70.md) (function, `0x00893B70`)
- `0x00AE8ABC` → [ExEnableHandleExceptions](../A7/ExEnableHandleExceptions_function_00A7580C.md) (function, `0x00A7580C`)
- `0x00AE8ACD` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00AE8B5D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AE8B90` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AE8BC0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AE8BFB` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE8C14` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AE8C28` → [IoRevokeHandlesForProcess](../../text/59/IoRevokeHandlesForProcess_function_005981A8.md) (function, `0x005981A8`)
- `0x00AE8C3D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AE8C54` → [MmProcessWorkingSetControl](../A6/MmProcessWorkingSetControl_function_00A616C4.md) (function, `0x00A616C4`)
- `0x00AE8C96` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE8CDE` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AE8D55` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE8D9E` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE8DBD` → [PsSetProcessFaultInformation](../A7/PsSetProcessFaultInformation_function_00A75400.md) (function, `0x00A75400`)
- `0x00AE8DD3` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE8E17` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE8E4F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE8EA7` → [MmSetCommitReleaseEligibility](../../text/66/MmSetCommitReleaseEligibility_function_0066FF84.md) (function, `0x0066FF84`)
- `0x00AE8EBC` → [MmReleaseCommitForMemResetPages](../../text/66/MmReleaseCommitForMemResetPages_function_0066FDCC.md) (function, `0x0066FDCC`)
- `0x00AE8ED0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE8EEB` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE8F1B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AE8F35` → [ExCpuSetResourceManagerAccessCheck](../../text/3A/ExCpuSetResourceManagerAccessCheck_function_003A5444.md) (function, `0x003A5444`)
- `0x00AE8F71` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE8F9A` → [KeSetCpuSetsProcess](../../text/5C/KeSetCpuSetsProcess_function_005C10D4.md) (function, `0x005C10D4`)
- `0x00AE8FAD` → [ExCpuSetResourceManagerAccessCheck](../../text/3A/ExCpuSetResourceManagerAccessCheck_function_003A5444.md) (function, `0x003A5444`)
- `0x00AE8FFC` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE9022` → [KeRecomputeCpuSetAffinityProcess](../../text/5C/KeRecomputeCpuSetAffinityProcess_function_005C1078.md) (function, `0x005C1078`)
- `0x00AE903C` → [KeRecomputeCpuSetAffinityProcess](../../text/5C/KeRecomputeCpuSetAffinityProcess_function_005C1078.md) (function, `0x005C1078`)
- `0x00AE9096` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00AE90BF` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AE90FA` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE910C` → [EtwTraceProcessSetInPrivateMode](../../text/64/EtwTraceProcessSetInPrivateMode_function_0064FF38.md) (function, `0x0064FF38`)
- `0x00AE9167` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE9179` → [ObReferenceProcessHandleTable](../89/ObReferenceProcessHandleTable_function_00893B70.md) (function, `0x00893B70`)
- `0x00AE918C` → [ExEnableRaiseUMExceptionOnInvalidHandleClose](../A6/ExEnableRaiseUMExceptionOnInvalidHandleClose_function_00A6A868.md) (function, `0x00A6A868`)
- `0x00AE91A4` → [PsIumEnableOnDemandDebugWithResponse](../78/PsIumEnableOnDemandDebugWithResponse_function_00787C30.md) (function, `0x00787C30`)
- `0x00AE91CC` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AE9208` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE92AA` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (function, `0x00428814`)
- `0x00AE92EA` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE92FC` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (function, `0x00456DC0`)
- `0x00AE9319` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00AE932A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE9336` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (function, `0x00456DC0`)
- `0x00AE93B0` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AE93E5` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE93FF` → [PoSetProcessEnergyTrackingState](../98/PoSetProcessEnergyTrackingState_function_0098C904.md) (function, `0x0098C904`)
- `0x00AE9418` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE94A1` → [RtlStringCbCopyA](../../text/46/RtlStringCbCopyA_function_0046143C.md) (function, `0x0046143C`)
- `0x00AE94D6` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE9508` → [EtwSetProcessTelemetryCoverage](../98/EtwSetProcessTelemetryCoverage_function_009804E0.md) (function, `0x009804E0`)
- `0x00AE9519` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE957E` → [RtlTestProtectedAccess](../A1/RtlTestProtectedAccess_function_00A100C8.md) (function, `0x00A100C8`)
- `0x00AE9596` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AE95AA` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AE961B` → [ObReferenceObjectByHandleWithTag](../86/ObReferenceObjectByHandleWithTag_function_00869610.md) (function, `0x00869610`)
- `0x00AE96E8` → [SeCodeIntegritySetInformationProcess](../79/SeCodeIntegritySetInformationProcess_function_0079B808.md) (function, `0x0079B808`)
- `0x00AE971B` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AE9752` → [ObReferenceObjectByHandleWithTag](../86/ObReferenceObjectByHandleWithTag_function_00869610.md) (function, `0x00869610`)
- `0x00AE976D` → [PspSetProcessForegroundBackgroundRequest](../A4/PspSetProcessForegroundBackgroundRequest_function_00A45DCC.md) (function, `0x00A45DCC`)
- `0x00AE97BA` → [ObReferenceObjectByHandleWithTag](../86/ObReferenceObjectByHandleWithTag_function_00869610.md) (function, `0x00869610`)
- `0x00AE97F4` → [ObReferenceObjectByHandleWithTag](../86/ObReferenceObjectByHandleWithTag_function_00869610.md) (function, `0x00869610`)
- `0x00AE9810` → [PspCombineSecurityDomains](../8A/PspCombineSecurityDomains_function_008A18C0.md) (function, `0x008A18C0`)
- `0x00AE9824` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE985D` → [PsGetCurrentProcess](../../text/41/PsGetCurrentProcess_function_0041B550.md) (function, `0x0041B550`)
- `0x00AE992A` → [ObReferenceObjectByHandleWithTag](../86/ObReferenceObjectByHandleWithTag_function_00869610.md) (function, `0x00869610`)
- `0x00AE9944` → [PspSyscallProviderOptIn](../77/PspSyscallProviderOptIn_function_0077E79C.md) (function, `0x0077E79C`)
- `0x00AE999D` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00AE99F7` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00AE9A11` → [PsGetCurrentProcess](../../text/41/PsGetCurrentProcess_function_0041B550.md) (function, `0x0041B550`)
- `0x00AE9A5A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AE9A84` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AE9AA0` → [PspProcessDynamicEHContinuationTargets](../78/PspProcessDynamicEHContinuationTargets_function_00782348.md) (function, `0x00782348`)
- `0x00AE9AFB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AE9B0E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AE9B71` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00AE9BCB` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00AE9BE5` → [PsGetCurrentProcess](../../text/41/PsGetCurrentProcess_function_0041B550.md) (function, `0x0041B550`)
- `0x00AE9C2E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AE9C5B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AE9C83` → [PspProcessDynamicEnforcedAddressRanges](../78/PspProcessDynamicEnforcedAddressRanges_function_00782624.md) (function, `0x00782624`)
- `0x00AE9D69` → [ObReferenceObjectByHandleWithTag](../86/ObReferenceObjectByHandleWithTag_function_00869610.md) (function, `0x00869610`)
- `0x00AE9D80` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE9D85` → [PsGetCurrentProcess](../../text/41/PsGetCurrentProcess_function_0041B550.md) (function, `0x0041B550`)
- `0x00AE9D95` → [PsGetCurrentProcess](../../text/41/PsGetCurrentProcess_function_0041B550.md) (function, `0x0041B550`)
- `0x00AE9DB0` → [PsIsSystemProcess](../../text/41/PsIsSystemProcess_function_004188B0.md) (function, `0x004188B0`)
- `0x00AE9DC5` → [PspEnableProcessOptionalXStateFeatures](../78/PspEnableProcessOptionalXStateFeatures_function_00781EF0.md) (function, `0x00781EF0`)
- `0x00AE9DE1` → [PfSnSetAltPrefetchParam](../75/PfSnSetAltPrefetchParam_function_00752424.md) (function, `0x00752424`)
- `0x00AE9E0C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AE9E34` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AE9E7C` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00AE9EAA` → [PspAssignCpuPartitionsToProcess](../78/PspAssignCpuPartitionsToProcess_function_00783FB4.md) (function, `0x00783FB4`)
- `0x00AE9ECE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AE9EE1` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AE9F25` → [ObReferenceObjectByHandleWithTag](../86/ObReferenceObjectByHandleWithTag_function_00869610.md) (function, `0x00869610`)
- `0x00AE9F3A` → [PspSchedulerSharedDataRegionCreate](../98/PspSchedulerSharedDataRegionCreate_function_009825DC.md) (function, `0x009825DC`)
- `0x00AE9F77` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x00AE9F8F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE9FAE` → [KeChangeMemoryAttributes](../../text/30/KeChangeMemoryAttributes_function_00304D08.md) (function, `0x00304D08`)
- `0x00AE9FCE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00AE9FE7` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00AE9FED` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00AE9FF3` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00AE5383` → RVA `0x00E0A740` (`.data`; read)
- `0x00AE56BB` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00AE56DA` → RVA `0x00FC6A98` (`ALMOSTRO`; read)
- `0x00AE574F` → RVA `0x00F06629` (`.data`; write)
- `0x00AE58EF` → RVA `0x00FD9AE8` (`PAGEDATA`; read)
- `0x00AE59BF` → RVA `0x00E08640` (`.data`; read)
- `0x00AE59D6` → RVA `0x00E08650` (`.data`; read)
- `0x00AE59DF` → RVA `0x00E08658` (`.data`; read)
- `0x00AE5A67` → RVA `0x00052C71` (`.rdata`; read)
- `0x00AE5BDB` → RVA `0x00052BB1` (`.rdata`; read)
- `0x00AE5D3A` → RVA `0x00052C0E` (`.rdata`; read)
- `0x00AE5F15` → RVA `0x00FD9A78` (`PAGEDATA`; read)
- `0x00AE5F29` → RVA `0x00FC6F70` (`ALMOSTRO`; read)
- `0x00AE60F8` → RVA `0x000118C8` (`.rdata`; read)
- `0x00AE6881` → RVA `0x00FD9A80` (`PAGEDATA`; read)
- `0x00AE80D6` → RVA `0x00F04E80` (`.data`; read)
- `0x00AE8719` → RVA `0x00E0C590` (`.data`; read/write)
- `0x00AE92A3` → RVA `0x00FC6CA0` (`ALMOSTRO`; read)
- `0x00AEA01B` → RVA `0x-2550B17D` (`image boundary/outside`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **158**
  - `0x00AE5720` → [PsChargeProcessNonPagedPoolQuota](../../text/2A/PsChargeProcessNonPagedPoolQuota_function_002A7B80.md) (`PAGE` → `.text`)
  - `0x00AE573B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AE5763` → [KeInitializeGate](../../text/49/KeInitializeGate_function_004953F8.md) (`PAGE` → `.text`)
  - `0x00AE5783` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AE5797` → [PsReturnProcessNonPagedPoolQuota](../../text/41/PsReturnProcessNonPagedPoolQuota_function_0041C200.md) (`PAGE` → `.text`)
  - `0x00AE57A6` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE5851` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE5909` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE5925` → [KeSetPriorityAndQuantumProcess](../../text/3C/KeSetPriorityAndQuantumProcess_function_003C2EC0.md) (`PAGE` → `.text`)
  - `0x00AE5933` → [MmSetMemoryPriorityProcess](../../text/49/MmSetMemoryPriorityProcess_function_00494EF4.md) (`PAGE` → `.text`)
  - `0x00AE593D` → [PspEnqueueProcessQosChangeNotification](../../text/5E/PspEnqueueProcessQosChangeNotification_function_005E2ED0.md) (`PAGE` → `.text`)
  - `0x00AE5A75` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00AE5A7A` → [Feature_ForegroundBoost_ApiRemoval__private_IsEnabledDeviceUsageNoInline](../../text/4B/Feature_ForegroundBoost_ApiRemoval__private_IsEnabledDeviceUsageNoInline_function_004B7A58.md) (`PAGE` → `.text`)
  - `0x00AE5AA0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE5BE9` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00AE5C16` → [Feature_ForegroundBoost_ApiRemoval__private_IsEnabledDeviceUsageNoInline](../../text/4B/Feature_ForegroundBoost_ApiRemoval__private_IsEnabledDeviceUsageNoInline_function_004B7A58.md) (`PAGE` → `.text`)
  - `0x00AE5D48` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00AE5D4D` → [Feature_ForegroundBoost_ApiRemoval__private_IsEnabledDeviceUsageNoInline](../../text/4B/Feature_ForegroundBoost_ApiRemoval__private_IsEnabledDeviceUsageNoInline_function_004B7A58.md) (`PAGE` → `.text`)
  - `0x00AE5DD2` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x00AE5DF5` → [KeBoostPriorityThread](../../text/4D/KeBoostPriorityThread_function_004D37F8.md) (`PAGE` → `.text`)
  - `0x00AE5E1B` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x00AE5FAD` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AE602D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AE603E` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AE6103` → [KeDelayExecutionThread](../../text/20/KeDelayExecutionThread_function_00209550.md) (`PAGE` → `.text`)
  - `0x00AE6114` → [PspLockUnlockProcessExclusive](../../text/41/PspLockUnlockProcessExclusive_function_00419B48.md) (`PAGE` → `.text`)
  - `0x00AE611C` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AE61A2` → [BvgaSetVirtualFrameBuffer](../../text/4F/BvgaSetVirtualFrameBuffer_function_004FC600.md) (`PAGE` → `.text`)
  - `0x00AE61B3` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE6206` → [BvgaSetVirtualFrameBuffer](../../text/4F/BvgaSetVirtualFrameBuffer_function_004FC600.md) (`PAGE` → `.text`)
  - `0x00AE6254` → [BvgaSetVirtualFrameBuffer](../../text/4F/BvgaSetVirtualFrameBuffer_function_004FC600.md) (`PAGE` → `.text`)
  - `0x00AE62BC` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE6324` → [PspLockProcessExclusive](../../text/46/PspLockProcessExclusive_function_00460164.md) (`PAGE` → `.text`)
  - `0x00AE638A` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (`PAGE` → `.text`)
  - `0x00AE63A5` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (`PAGE` → `.text`)
  - `0x00AE6435` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE64A2` → [KeVerifyGroupAffinity](../../text/47/KeVerifyGroupAffinity_function_0047B1F0.md) (`PAGE` → `.text`)
  - `0x00AE6506` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE6517` → [KeQueryPrimaryGroupProcess](../../text/2C/KeQueryPrimaryGroupProcess_function_002CF958.md) (`PAGE` → `.text`)
  - `0x00AE657A` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x00AE658C` → [PspLockProcessSharedUnsafe](../../text/4A/PspLockProcessSharedUnsafe_function_004AD874.md) (`PAGE` → `.text`)
  - `0x00AE65BC` → [PspUnlockProcessSharedUnsafe](../../text/4B/PspUnlockProcessSharedUnsafe_function_004B2800.md) (`PAGE` → `.text`)
  - `0x00AE65CD` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x00AE6600` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x00AE6612` → [KiLeaveCriticalRegionUnsafe](../../text/25/KiLeaveCriticalRegionUnsafe_function_0025F010.md) (`PAGE` → `.text`)
  - `0x00AE6685` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x00AE6699` → [KeSetDisableBoostProcess](../../text/3C/KeSetDisableBoostProcess_function_003C18B4.md) (`PAGE` → `.text`)
  - `0x00AE67A6` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (`PAGE` → `.text`)
  - `0x00AE683F` → [PsGetProcessSessionId](../../text/22/PsGetProcessSessionId_function_002233A0.md) (`PAGE` → `.text`)
  - `0x00AE6859` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE6A5F` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x00AE6A79` → [PspLockProcessExclusive](../../text/46/PspLockProcessExclusive_function_00460164.md) (`PAGE` → `.text`)
  - `0x00AE6AF7` → [IoBoostThreadIoPriority](../../text/21/IoBoostThreadIoPriority_function_00216110.md) (`PAGE` → `.text`)
  - `0x00AE6B06` → [PsSetIoPriorityThread](../../text/3C/PsSetIoPriorityThread_function_003C3FBC.md) (`PAGE` → `.text`)
  - `0x00AE6B22` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (`PAGE` → `.text`)
  - `0x00AE6B66` → [KeSetExecuteOptions](../../text/3C/KeSetExecuteOptions_function_003C1F54.md) (`PAGE` → `.text`)
  - `0x00AE6B81` → [MmRemoveExecuteGrants](../../text/4A/MmRemoveExecuteGrants_function_004A8B60.md) (`PAGE` → `.text`)
  - `0x00AE6BA4` → [KeQueryHeteroCpuPolicyThread](../../text/48/KeQueryHeteroCpuPolicyThread_function_00488A70.md) (`PAGE` → `.text`)
  - `0x00AE6BB1` → [Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting](../../text/22/Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting_function_00222FE0.md) (`PAGE` → `.text`)
  - `0x00AE6C08` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x00AE6C22` → [PspLockProcessExclusive](../../text/46/PspLockProcessExclusive_function_00460164.md) (`PAGE` → `.text`)
  - `0x00AE6C89` → [PsSetPagePriorityThread](../../text/3C/PsSetPagePriorityThread_function_003C4138.md) (`PAGE` → `.text`)
  - `0x00AE6CA5` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (`PAGE` → `.text`)
  - `0x00AE6D4C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AE6ECC` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x00AE6F14` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AE6FFE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AE7220` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x00AE72D4` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x00AE7304` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE7336` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AE744F` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x00AE7462` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE74DA` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x00AE7508` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x00AE7522` → [PspLockProcessExclusive](../../text/46/PspLockProcessExclusive_function_00460164.md) (`PAGE` → `.text`)
  - `0x00AE7584` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (`PAGE` → `.text`)
  - `0x00AE75B9` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x00AE75C1` → [MmGetMaximumUserAddress](../../text/44/MmGetMaximumUserAddress_function_004455B0.md) (`PAGE` → `.text`)
  - `0x00AE75E2` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x00AE762A` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x00AE7640` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x00AE7781` → [KeIsUserCetAllowed](../../text/4A/KeIsUserCetAllowed_function_004A22B4.md) (`PAGE` → `.text`)
  - `0x00AE7807` → [KeIsUserCetAllowed](../../text/4A/KeIsUserCetAllowed_function_004A22B4.md) (`PAGE` → `.text`)
  - `0x00AE795E` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (`PAGE` → `.text`)
  - `0x00AE7973` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AE7B56` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x00AE7D0C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE7F89` → [RtlInterlockedSetClearBits](../../text/49/RtlInterlockedSetClearBits_function_00497378.md) (`PAGE` → `.text`)
  - `0x00AE80E4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AE8115` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AE8151` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AE8175` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AE81DA` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AE820A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AE823F` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AE8267` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AE82C6` → [RtlInterlockedSetClearBits](../../text/49/RtlInterlockedSetClearBits_function_00497378.md) (`PAGE` → `.text`)
  - `0x00AE8342` → [RtlInterlockedSetClearBits](../../text/49/RtlInterlockedSetClearBits_function_00497378.md) (`PAGE` → `.text`)
  - `0x00AE836C` → [RtlInterlockedSetClearBits](../../text/49/RtlInterlockedSetClearBits_function_00497378.md) (`PAGE` → `.text`)
  - `0x00AE8494` → [RtlInterlockedSetClearBits](../../text/49/RtlInterlockedSetClearBits_function_00497378.md) (`PAGE` → `.text`)
  - `0x00AE86C8` → [KeIsCoreIsolationMitigationPolicyEnforceable](../../text/4A/KeIsCoreIsolationMitigationPolicyEnforceable_function_004A7388.md) (`PAGE` → `.text`)
  - `0x00AE873D` → [KeSynchronizeSecurityDomain](../../text/4B/KeSynchronizeSecurityDomain_function_004B0FE0.md) (`PAGE` → `.text`)
  - `0x00AE8747` → [PspSynchronizeThreadIsolationDomains](../../text/3C/PspSynchronizeThreadIsolationDomains_function_003C479C.md) (`PAGE` → `.text`)
  - `0x00AE8A31` → [RtlInsertDynamicUserFunctionTable](../../text/45/RtlInsertDynamicUserFunctionTable_function_004513C4.md) (`PAGE` → `.text`)
  - `0x00AE8A3B` → [RtlRemoveDynamicUserFunctionTable](../../text/46/RtlRemoveDynamicUserFunctionTable_function_00466514.md) (`PAGE` → `.text`)
  - `0x00AE8ACD` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x00AE8B5D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AE8B90` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AE8BC0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AE8C14` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AE8C28` → [IoRevokeHandlesForProcess](../../text/59/IoRevokeHandlesForProcess_function_005981A8.md) (`PAGE` → `.text`)
  - `0x00AE8C3D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AE8D55` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE8DD3` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE8E4F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE8EA7` → [MmSetCommitReleaseEligibility](../../text/66/MmSetCommitReleaseEligibility_function_0066FF84.md) (`PAGE` → `.text`)
  - `0x00AE8EBC` → [MmReleaseCommitForMemResetPages](../../text/66/MmReleaseCommitForMemResetPages_function_0066FDCC.md) (`PAGE` → `.text`)
  - `0x00AE8ED0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE8EEB` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE8F1B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AE8F35` → [ExCpuSetResourceManagerAccessCheck](../../text/3A/ExCpuSetResourceManagerAccessCheck_function_003A5444.md) (`PAGE` → `.text`)
  - `0x00AE8F9A` → [KeSetCpuSetsProcess](../../text/5C/KeSetCpuSetsProcess_function_005C10D4.md) (`PAGE` → `.text`)
  - `0x00AE8FAD` → [ExCpuSetResourceManagerAccessCheck](../../text/3A/ExCpuSetResourceManagerAccessCheck_function_003A5444.md) (`PAGE` → `.text`)
  - `0x00AE9022` → [KeRecomputeCpuSetAffinityProcess](../../text/5C/KeRecomputeCpuSetAffinityProcess_function_005C1078.md) (`PAGE` → `.text`)
  - `0x00AE903C` → [KeRecomputeCpuSetAffinityProcess](../../text/5C/KeRecomputeCpuSetAffinityProcess_function_005C1078.md) (`PAGE` → `.text`)
  - `0x00AE90BF` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AE910C` → [EtwTraceProcessSetInPrivateMode](../../text/64/EtwTraceProcessSetInPrivateMode_function_0064FF38.md) (`PAGE` → `.text`)
  - `0x00AE92AA` → [ExGetExtensionTable](../../text/42/ExGetExtensionTable_function_00428814.md) (`PAGE` → `.text`)
  - `0x00AE92FC` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (`PAGE` → `.text`)
  - `0x00AE9319` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00AE932A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE9336` → [ExReleaseExtensionTable](../../text/45/ExReleaseExtensionTable_function_00456DC0.md) (`PAGE` → `.text`)
  - `0x00AE93B0` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AE9418` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE94A1` → [RtlStringCbCopyA](../../text/46/RtlStringCbCopyA_function_0046143C.md) (`PAGE` → `.text`)
  - `0x00AE9519` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE9824` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE985D` → [PsGetCurrentProcess](../../text/41/PsGetCurrentProcess_function_0041B550.md) (`PAGE` → `.text`)
  - `0x00AE9A11` → [PsGetCurrentProcess](../../text/41/PsGetCurrentProcess_function_0041B550.md) (`PAGE` → `.text`)
  - `0x00AE9A5A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AE9A84` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AE9AFB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AE9B0E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AE9BE5` → [PsGetCurrentProcess](../../text/41/PsGetCurrentProcess_function_0041B550.md) (`PAGE` → `.text`)
  - `0x00AE9C2E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AE9C5B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AE9D80` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE9D85` → [PsGetCurrentProcess](../../text/41/PsGetCurrentProcess_function_0041B550.md) (`PAGE` → `.text`)
  - `0x00AE9D95` → [PsGetCurrentProcess](../../text/41/PsGetCurrentProcess_function_0041B550.md) (`PAGE` → `.text`)
  - `0x00AE9DB0` → [PsIsSystemProcess](../../text/41/PsIsSystemProcess_function_004188B0.md) (`PAGE` → `.text`)
  - `0x00AE9E0C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AE9E34` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AE9ECE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AE9EE1` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AE9F8F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE9FAE` → [KeChangeMemoryAttributes](../../text/30/KeChangeMemoryAttributes_function_00304D08.md) (`PAGE` → `.text`)
  - `0x00AE9FCE` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AE5370  40 53                           push rbx
00AE5372  56                              push rsi
00AE5373  57                              push rdi
00AE5374  41 54                           push r12
00AE5376  41 55                           push r13
00AE5378  41 56                           push r14
00AE537A  41 57                           push r15
00AE537C  48 81 EC D0 04 00 00            sub rsp, 0x4d0
00AE5383  48 8B 05 B6 53 32 00            mov rax, qword ptr [rip + 0x3253b6]
00AE538A  48 33 C4                        xor rax, rsp
00AE538D  48 89 84 24 C0 04 00 00         mov qword ptr [rsp + 0x4c0], rax
00AE5395  41 8B F9                        mov edi, r9d
00AE5398  49 8B D8                        mov rbx, r8
00AE539B  44 8B D2                        mov r10d, edx
00AE539E  89 94 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], edx
00AE53A5  48 8B F1                        mov rsi, rcx
00AE53A8  48 89 9C 24 10 01 00 00         mov qword ptr [rsp + 0x110], rbx
00AE53B0  89 BC 24 80 00 00 00            mov dword ptr [rsp + 0x80], edi
00AE53B7  45 33 F6                        xor r14d, r14d
00AE53BA  4C 89 74 24 40                  mov qword ptr [rsp + 0x40], r14
00AE53BF  0F 57 C0                        xorps xmm0, xmm0
00AE53C2  0F 11 84 24 20 02 00 00         movups xmmword ptr [rsp + 0x220], xmm0
00AE53CA  44 89 74 24 4C                  mov dword ptr [rsp + 0x4c], r14d
00AE53CF  66 44 89 B4 24 98 00 00 00      mov word ptr [rsp + 0x98], r14w
00AE53D8  44 89 B4 24 B4 00 00 00         mov dword ptr [rsp + 0xb4], r14d
00AE53E0  4C 89 B4 24 28 01 00 00         mov qword ptr [rsp + 0x128], r14
00AE53E8  4C 89 B4 24 30 01 00 00         mov qword ptr [rsp + 0x130], r14
00AE53F0  4C 89 B4 24 80 01 00 00         mov qword ptr [rsp + 0x180], r14
00AE53F8  44 89 B4 24 D4 00 00 00         mov dword ptr [rsp + 0xd4], r14d
00AE5400  0F 11 84 24 30 02 00 00         movups xmmword ptr [rsp + 0x230], xmm0
00AE5408  66 44 89 74 24 78               mov word ptr [rsp + 0x78], r14w
00AE540E  65 4C 8B 1C 25 88 01 00 00      mov r11, qword ptr gs:[0x188]
00AE5417  4C 89 5C 24 68                  mov qword ptr [rsp + 0x68], r11
00AE541C  45 0F B6 A3 32 02 00 00         movzx r12d, byte ptr [r11 + 0x232]
00AE5424  44 88 64 24 74                  mov byte ptr [rsp + 0x74], r12b
00AE5429  45 84 E4                        test r12b, r12b
00AE542C  0F 84 67 02 00 00               je 0x140ae5699
00AE5432  83 FA 05                        cmp edx, 5
00AE5435  75 0C                           jne 0x140ae5443
00AE5437  8D 42 FF                        lea eax, [rdx - 1]
00AE543A  44 8D 7A 03                     lea r15d, [rdx + 3]
00AE543E  E9 0F 02 00 00                  jmp 0x140ae5652
00AE5443  41 83 FA 11                     cmp r10d, 0x11
00AE5447  0F 84 B0 01 00 00               je 0x140ae55fd
00AE544D  41 83 FA 19                     cmp r10d, 0x19
00AE5451  0F 84 A6 01 00 00               je 0x140ae55fd
00AE5457  41 83 FA 12                     cmp r10d, 0x12
00AE545B  0F 84 9C 01 00 00               je 0x140ae55fd
00AE5461  41 83 FA 6C                     cmp r10d, 0x6c
00AE5465  75 0D                           jne 0x140ae5474
00AE5467  41 8D 42 96                     lea eax, [r10 - 0x6a]
00AE546B  45 8D 7A 9C                     lea r15d, [r10 - 0x64]
00AE546F  E9 DE 01 00 00                  jmp 0x140ae5652
00AE5474  41 83 FA 15                     cmp r10d, 0x15
00AE5478  75 0E                           jne 0x140ae5488
00AE547A  41 BF 08 00 00 00               mov r15d, 8
00AE5480  41 8B C7                        mov eax, r15d
00AE5483  E9 CA 01 00 00                  jmp 0x140ae5652
00AE5488  41 83 FA 21                     cmp r10d, 0x21
00AE548C  75 0D                           jne 0x140ae549b
00AE548E  41 8D 42 E3                     lea eax, [r10 - 0x1d]
00AE5492  45 8D 7A E7                     lea r15d, [r10 - 0x19]
00AE5496  E9 B7 01 00 00                  jmp 0x140ae5652
00AE549B  41 83 FA 27                     cmp r10d, 0x27
00AE549F  75 0D                           jne 0x140ae54ae
00AE54A1  41 8D 42 DD                     lea eax, [r10 - 0x23]
00AE54A5  45 8D 7A E1                     lea r15d, [r10 - 0x1f]
00AE54A9  E9 A4 01 00 00                  jmp 0x140ae5652
00AE54AE  41 83 FA 23                     cmp r10d, 0x23
00AE54B2  75 0E                           jne 0x140ae54c2
00AE54B4  41 BF 08 00 00 00               mov r15d, 8
00AE54BA  41 8B C7                        mov eax, r15d
00AE54BD  E9 90 01 00 00                  jmp 0x140ae5652
00AE54C2  41 83 FA 08                     cmp r10d, 8
00AE54C6  75 0E                           jne 0x140ae54d6
00AE54C8  41 BF 08 00 00 00               mov r15d, 8
00AE54CE  41 8B C7                        mov eax, r15d
00AE54D1  E9 7C 01 00 00                  jmp 0x140ae5652
00AE54D6  41 83 FA 28                     cmp r10d, 0x28
00AE54DA  75 0E                           jne 0x140ae54ea
00AE54DC  41 BF 08 00 00 00               mov r15d, 8
00AE54E2  41 8B C7                        mov eax, r15d
00AE54E5  E9 68 01 00 00                  jmp 0x140ae5652
00AE54EA  41 83 FA 29                     cmp r10d, 0x29
00AE54EE  75 0E                           jne 0x140ae54fe
00AE54F0  41 BF 08 00 00 00               mov r15d, 8
00AE54F6  41 8B C7                        mov eax, r15d
00AE54F9  E9 54 01 00 00                  jmp 0x140ae5652
00AE54FE  41 83 FA 62                     cmp r10d, 0x62
00AE5502  75 0E                           jne 0x140ae5512
00AE5504  41 BF 08 00 00 00               mov r15d, 8
00AE550A  41 8B C7                        mov eax, r15d
00AE550D  E9 40 01 00 00                  jmp 0x140ae5652
00AE5512  41 83 FA 63                     cmp r10d, 0x63
00AE5516  75 0E                           jne 0x140ae5526
00AE5518  41 BF 08 00 00 00               mov r15d, 8
00AE551E  41 8B C7                        mov eax, r15d
00AE5521  E9 2C 01 00 00                  jmp 0x140ae5652
00AE5526  41 83 FA 2D                     cmp r10d, 0x2d
00AE552A  75 0D                           jne 0x140ae5539
00AE552C  41 8D 42 D7                     lea eax, [r10 - 0x29]
00AE5530  45 8D 7A DB                     lea r15d, [r10 - 0x25]
00AE5534  E9 19 01 00 00                  jmp 0x140ae5652
00AE5539  41 83 FA 2E                     cmp r10d, 0x2e
00AE553D  75 0D                           jne 0x140ae554c
00AE553F  41 8D 42 D6                     lea eax, [r10 - 0x2a]
00AE5543  45 8D 7A DA                     lea r15d, [r10 - 0x26]
00AE5547  E9 06 01 00 00                  jmp 0x140ae5652
00AE554C  41 83 FA 31                     cmp r10d, 0x31
00AE5550  75 0E                           jne 0x140ae5560
00AE5552  41 BF 08 00 00 00               mov r15d, 8
00AE5558  41 8B C7                        mov eax, r15d
00AE555B  E9 F2 00 00 00                  jmp 0x140ae5652
00AE5560  41 83 FA 35                     cmp r10d, 0x35
00AE5564  75 0E                           jne 0x140ae5574
00AE5566  41 BF 08 00 00 00               mov r15d, 8
00AE556C  41 8B C7                        mov eax, r15d
00AE556F  E9 DE 00 00 00                  jmp 0x140ae5652
00AE5574  41 83 FA 38                     cmp r10d, 0x38
00AE5578  75 0E                           jne 0x140ae5588
00AE557A  41 BF 08 00 00 00               mov r15d, 8
00AE5580  41 8B C7                        mov eax, r15d
00AE5583  E9 CA 00 00 00                  jmp 0x140ae5652
00AE5588  41 83 FA 3E                     cmp r10d, 0x3e
00AE558C  75 0E                           jne 0x140ae559c
00AE558E  41 BF 08 00 00 00               mov r15d, 8
00AE5594  41 8B C7                        mov eax, r15d
00AE5597  E9 B6 00 00 00                  jmp 0x140ae5652
00AE559C  41 83 FA 41                     cmp r10d, 0x41
00AE55A0  75 0E                           jne 0x140ae55b0
00AE55A2  41 BF 08 00 00 00               mov r15d, 8
00AE55A8  41 8B C7                        mov eax, r15d
00AE55AB  E9 A2 00 00 00                  jmp 0x140ae5652
00AE55B0  41 83 FA 46                     cmp r10d, 0x46
00AE55B4  74 47                           je 0x140ae55fd
00AE55B6  41 83 FA 4A                     cmp r10d, 0x4a
00AE55BA  74 41                           je 0x140ae55fd
00AE55BC  41 83 FA 53                     cmp r10d, 0x53
00AE55C0  75 0E                           jne 0x140ae55d0
00AE55C2  41 BF 08 00 00 00               mov r15d, 8
00AE55C8  41 8B C7                        mov eax, r15d
00AE55CB  E9 82 00 00 00                  jmp 0x140ae5652
00AE55D0  41 83 FA 5A                     cmp r10d, 0x5a
00AE55D4  74 27                           je 0x140ae55fd
00AE55D6  41 83 FA 5B                     cmp r10d, 0x5b
00AE55DA  75 0A                           jne 0x140ae55e6
00AE55DC  41 8D 42 A9                     lea eax, [r10 - 0x57]
00AE55E0  45 8D 7A AD                     lea r15d, [r10 - 0x53]
00AE55E4  EB 6C                           jmp 0x140ae5652
00AE55E6  41 83 FA 5F                     cmp r10d, 0x5f
00AE55EA  75 0B                           jne 0x140ae55f7
00AE55EC  41 BF 08 00 00 00               mov r15d, 8
00AE55F2  41 8B C7                        mov eax, r15d
00AE55F5  EB 5B                           jmp 0x140ae5652
00AE55F7  41 83 FA 57                     cmp r10d, 0x57
00AE55FB  75 0F                           jne 0x140ae560c
00AE55FD  41 B8 01 00 00 00               mov r8d, 1
00AE5603  41 8B C0                        mov eax, r8d
00AE5606  45 8D 78 07                     lea r15d, [r8 + 7]
00AE560A  EB 4C                           jmp 0x140ae5658
00AE560C  41 BF 08 00 00 00               mov r15d, 8
00AE5612  41 83 FA 64                     cmp r10d, 0x64
00AE5616  75 06                           jne 0x140ae561e
00AE5618  41 8D 47 FC                     lea eax, [r15 - 4]
00AE561C  EB 34                           jmp 0x140ae5652
00AE561E  41 83 FA 65                     cmp r10d, 0x65
00AE5622  75 05                           jne 0x140ae5629
00AE5624  41 8B C7                        mov eax, r15d
00AE5627  EB 29                           jmp 0x140ae5652
00AE5629  41 83 FA 66                     cmp r10d, 0x66
00AE562D  75 05                           jne 0x140ae5634
00AE562F  41 8B C7                        mov eax, r15d
00AE5632  EB 1E                           jmp 0x140ae5652
00AE5634  41 83 FA 69                     cmp r10d, 0x69
00AE5638  75 05                           jne 0x140ae563f
00AE563A  41 8B C7                        mov eax, r15d
00AE563D  EB 13                           jmp 0x140ae5652
00AE563F  B8 04 00 00 00                  mov eax, 4
00AE5644  41 83 FA 6A                     cmp r10d, 0x6a
00AE5648  74 08                           je 0x140ae5652
00AE564A  41 83 FA 6B                     cmp r10d, 0x6b
00AE564E  41 0F 44 C7                     cmove eax, r15d
00AE5652  41 B8 01 00 00 00               mov r8d, 1
00AE5658  45 85 C9                        test r9d, r9d
00AE565B  74 2B                           je 0x140ae5688
00AE565D  8D 48 FF                        lea ecx, [rax - 1]
00AE5660  48 85 CB                        test rbx, rcx
00AE5663  0F 85 7E 49 00 00               jne 0x140ae9fe7
00AE5669  48 8D 0C 3B                     lea rcx, [rbx + rdi]
00AE566D  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
00AE5677  49 3B CD                        cmp rcx, r13
00AE567A  77 05                           ja 0x140ae5681
00AE567C  48 3B CB                        cmp rcx, rbx
00AE567F  73 11                           jae 0x140ae5692
00AE5681  41 0F B6 45 00                  movzx eax, byte ptr [r13]
00AE5686  EB 0A                           jmp 0x140ae5692
00AE5688  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
00AE5692  EB 19                           jmp 0x140ae56ad
00AE5694  E9 2A 49 00 00                  jmp 0x140ae9fc3
00AE5699  41 B8 01 00 00 00               mov r8d, 1
00AE569F  45 8D 78 07                     lea r15d, [r8 + 7]
00AE56A3  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
00AE56AD  8D 42 FF                        lea eax, [rdx - 1]
00AE56B0  83 F8 70                        cmp eax, 0x70
00AE56B3  0F 87 05 49 00 00               ja 0x140ae9fbe
00AE56B9  48 98                           cdqe
00AE56BB  48 8D 0D 3E A9 51 FF            lea rcx, [rip - 0xae56c2]
00AE56C2  0F B6 84 01 10 A1 AE 00         movzx eax, byte ptr [rcx + rax + 0xaea110]
00AE56CA  8B 94 81 FC 9F AE 00            mov edx, dword ptr [rcx + rax*4 + 0xae9ffc]
00AE56D1  48 03 D1                        add rdx, rcx
00AE56D4  FF E2                           jmp rdx
00AE56D6  CC                              int3
00AE56D7  CC                              int3
00AE56D8  CC                              int3
00AE56D9  CC                              int3
00AE56DA  4C 8B 05 B7 13 4E 00            mov r8, qword ptr [rip + 0x4e13b7]
00AE56E1  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE56E6  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE56EB  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE56F0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE56F5  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE56FD  45 0F B6 CC                     movzx r9d, r12b
00AE5701  BA 00 02 00 00                  mov edx, 0x200
00AE5706  48 8B CE                        mov rcx, rsi
00AE5709  E8 42 3F D8 FF                  call 0x140869650
00AE570E  85 C0                           test eax, eax
00AE5710  0F 88 AD 48 00 00               js 0x140ae9fc3
00AE5716  BA 28 60 00 00                  mov edx, 0x6028
00AE571B  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE5720  E8 5B 24 7C FF                  call 0x1402a7b80
00AE5725  8B F0                           mov esi, eax
00AE5727  85 C0                           test eax, eax
00AE5729  78 71                           js 0x140ae579c
00AE572B  BA 28 60 00 00                  mov edx, 0x6028
00AE5730  B9 40 00 00 00                  mov ecx, 0x40
00AE5735  41 B8 50 73 57 73               mov r8d, 0x73577350
00AE573B  E8 B0 C9 09 00                  call 0x140b820f0
00AE5740  48 8B D8                        mov rbx, rax
00AE5743  48 85 C0                        test rax, rax
00AE5746  75 07                           jne 0x140ae574f
00AE5748  BE 17 00 00 C0                  mov esi, 0xc0000017
00AE574D  EB 3E                           jmp 0x140ae578d
00AE574F  C6 05 D3 0E 42 00 01            mov byte ptr [rip + 0x420ed3], 1
00AE5756  44 89 30                        mov dword ptr [rax], r14d
00AE5759  4C 89 70 08                     mov qword ptr [rax + 8], r14
00AE575D  48 8D 48 10                     lea rcx, [rax + 0x10]
00AE5761  33 D2                           xor edx, edx
00AE5763  E8 90 FC 9A FF                  call 0x1404953f8
00AE5768  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE576D  33 C0                           xor eax, eax
00AE576F  F0 48 0F B1 99 C0 02 00 00      lock cmpxchg qword ptr [rcx + 0x2c0], rbx
00AE5778  0F 84 A3 09 00 00               je 0x140ae6121
00AE577E  33 D2                           xor edx, edx
00AE5780  48 8B CB                        mov rcx, rbx
00AE5783  E8 E8 D0 09 00                  call 0x140b82870
00AE5788  BE 48 00 00 C0                  mov esi, 0xc0000048
00AE578D  BA 28 60 00 00                  mov edx, 0x6028
00AE5792  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE5797  E8 64 6A 93 FF                  call 0x14041c200
00AE579C  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE57A1  BA 50 73 51 79                  mov edx, 0x79517350
00AE57A6  E8 35 21 81 FF                  call 0x1402f78e0
00AE57AB  8B C6                           mov eax, esi
00AE57AD  E9 11 48 00 00                  jmp 0x140ae9fc3
00AE57B2  83 FF 10                        cmp edi, 0x10
00AE57B5  0F 85 E2 47 00 00               jne 0x140ae9f9d
00AE57BB  0F 10 03                        movups xmm0, xmmword ptr [rbx]
00AE57BE  0F 11 84 24 30 02 00 00         movups xmmword ptr [rsp + 0x230], xmm0
00AE57C6  66 83 BC 24 30 02 00 00 01      cmp word ptr [rsp + 0x230], 1
00AE57CF  0F 85 00 37 00 00               jne 0x140ae8ed5
00AE57D5  83 BC 24 34 02 00 00 00         cmp dword ptr [rsp + 0x234], 0
00AE57DD  0F 85 F2 36 00 00               jne 0x140ae8ed5
00AE57E3  4C 8B 05 AE 12 4E 00            mov r8, qword ptr [rip + 0x4e12ae]
00AE57EA  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE57EF  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE57F4  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE57F9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE57FE  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE5806  45 0F B6 CC                     movzx r9d, r12b
00AE580A  BA 00 02 00 00                  mov edx, 0x200
00AE580F  48 8B CE                        mov rcx, rsi
00AE5812  E8 39 3E D8 FF                  call 0x140869650
00AE5817  85 C0                           test eax, eax
00AE5819  0F 88 A4 47 00 00               js 0x140ae9fc3
00AE581F  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE5824  48 83 BC 24 38 02 00 00 00      cmp qword ptr [rsp + 0x238], 0
00AE582D  74 0D                           je 0x140ae583c
00AE582F  F0 81 88 F4 01 00 00 00 01 00 00  lock or dword ptr [rax + 0x1f4], 0x100
00AE583A  EB 0B                           jmp 0x140ae5847
00AE583C  F0 81 A0 F4 01 00 00 FF FE FF FF  lock and dword ptr [rax + 0x1f4], 0xfffffeff
00AE5847  BA 50 73 51 79                  mov edx, 0x79517350
00AE584C  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE5851  E8 8A 20 81 FF                  call 0x1402f78e0
00AE5856  33 C0                           xor eax, eax
00AE5858  E9 66 47 00 00                  jmp 0x140ae9fc3
00AE585D  E9 61 47 00 00                  jmp 0x140ae9fc3
00AE5862  83 FF 04                        cmp edi, 4
00AE5865  0F 85 32 47 00 00               jne 0x140ae9f9d
00AE586B  8B 1B                           mov ebx, dword ptr [rbx]
00AE586D  89 9C 24 50 01 00 00            mov dword ptr [rsp + 0x150], ebx
00AE5874  8B C3                           mov eax, ebx
00AE5876  25 00 00 00 80                  and eax, 0x80000000
00AE587B  74 04                           je 0x140ae5881
00AE587D  0F BA F3 1F                     btr ebx, 0x1f
00AE5881  F7 D8                           neg eax
00AE5883  40 1A FF                        sbb dil, dil
00AE5886  40 80 E7 02                     and dil, 2
00AE588A  8D 43 FF                        lea eax, [rbx - 1]
00AE588D  83 F8 1E                        cmp eax, 0x1e
00AE5890  0F 87 3F 36 00 00               ja 0x140ae8ed5
00AE5896  4C 8B 05 FB 11 4E 00            mov r8, qword ptr [rip + 0x4e11fb]
00AE589D  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE58A2  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE58A7  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE58AC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE58B1  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE58B9  45 0F B6 CC                     movzx r9d, r12b
00AE58BD  BA 00 02 00 00                  mov edx, 0x200
00AE58C2  48 8B CE                        mov rcx, rsi
00AE58C5  E8 86 3D D8 FF                  call 0x140869650
00AE58CA  85 C0                           test eax, eax
00AE58CC  0F 88 F1 46 00 00               js 0x140ae9fc3
00AE58D2  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE58D7  0F BE 81 90 00 00 00            movsx eax, byte ptr [rcx + 0x90]
00AE58DE  3B D8                           cmp ebx, eax
00AE58E0  7E 36                           jle 0x140ae5918
00AE58E2  45 0F B6 CC                     movzx r9d, r12b
00AE58E6  41 B8 00 02 00 00               mov r8d, 0x200
00AE58EC  48 8B D6                        mov rdx, rsi
00AE58EF  48 8B 0D F2 41 4F 00            mov rcx, qword ptr [rip + 0x4f41f2]
00AE58F6  E8 D1 09 F1 FF                  call 0x1409f62cc
00AE58FB  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE5900  84 C0                           test al, al
00AE5902  75 14                           jne 0x140ae5918
00AE5904  BA 50 73 51 79                  mov edx, 0x79517350
00AE5909  E8 D2 1F 81 FF                  call 0x1402f78e0
00AE590E  B8 61 00 00 C0                  mov eax, 0xc0000061
00AE5913  E9 AB 46 00 00                  jmp 0x140ae9fc3
00AE5918  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
00AE591D  45 33 C9                        xor r9d, r9d
00AE5920  45 33 C0                        xor r8d, r8d
00AE5923  8B D3                           mov edx, ebx
00AE5925  E8 96 D5 8D FF                  call 0x1403c2ec0
00AE592A  40 0F B6 D7                     movzx edx, dil
00AE592E  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE5933  E8 BC F5 9A FF                  call 0x140494ef4
00AE5938  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE593D  E8 8E D5 AF FF                  call 0x1405e2ed0
00AE5942  E9 00 FF FF FF                  jmp 0x140ae5847
00AE5947  E9 77 46 00 00                  jmp 0x140ae9fc3
00AE594C  83 FF 02                        cmp edi, 2
00AE594F  0F 85 48 46 00 00               jne 0x140ae9f9d
00AE5955  0F B7 1B                        movzx ebx, word ptr [rbx]
00AE5958  66 89 9C 24 98 00 00 00         mov word ptr [rsp + 0x98], bx
00AE5960  4C 8B 05 31 11 4E 00            mov r8, qword ptr [rip + 0x4e1131]
00AE5967  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE596C  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE5971  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE5976  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE597B  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE5983  45 0F B6 CC                     movzx r9d, r12b
00AE5987  BA 00 02 00 00                  mov edx, 0x200
00AE598C  48 8B CE                        mov rcx, rsi
00AE598F  E8 BC 3C D8 FF                  call 0x140869650
00AE5994  85 C0                           test eax, eax
00AE5996  0F 88 27 46 00 00               js 0x140ae9fc3
00AE599C  45 0F B6 CC                     movzx r9d, r12b
00AE59A0  4C 8B C6                        mov r8, rsi
00AE59A3  0F B6 94 24 99 00 00 00         movzx edx, byte ptr [rsp + 0x99]
00AE59AB  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE59B0  E8 2F 08 F1 FF                  call 0x1409f61e4
00AE59B5  8B F8                           mov edi, eax
00AE59B7  85 C0                           test eax, eax
00AE59B9  0F 88 D7 00 00 00               js 0x140ae5a96
00AE59BF  83 3D 7A 2C 32 00 05            cmp dword ptr [rip + 0x322c7a], 5
00AE59C6  0F 86 AE 00 00 00               jbe 0x140ae5a7a
00AE59CC  49 B8 00 00 00 00 00 40 00 00   movabs r8, 0x400000000000
00AE59D6  4C 85 05 73 2C 32 00            test qword ptr [rip + 0x322c73], r8
00AE59DD  74 17                           je 0x140ae59f6
00AE59DF  48 8B 0D 72 2C 32 00            mov rcx, qword ptr [rip + 0x322c72]
00AE59E6  49 23 C8                        and rcx, r8
00AE59E9  48 3B 0D 68 2C 32 00            cmp rcx, qword ptr [rip + 0x322c68]
00AE59F0  75 04                           jne 0x140ae59f6
00AE59F2  B0 01                           mov al, 1
00AE59F4  EB 02                           jmp 0x140ae59f8
00AE59F6  32 C0                           xor al, al
00AE59F8  84 C0                           test al, al
00AE59FA  74 7E                           je 0x140ae5a7a
00AE59FC  88 5C 24 48                     mov byte ptr [rsp + 0x48], bl
00AE5A00  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00AE5A05  48 89 84 24 50 03 00 00         mov qword ptr [rsp + 0x350], rax
00AE5A0D  C7 84 24 58 03 00 00 01 00 00 00  mov dword ptr [rsp + 0x358], 1
00AE5A18  44 89 B4 24 5C 03 00 00         mov dword ptr [rsp + 0x35c], r14d
00AE5A20  48 C7 84 24 88 00 00 00 00 00 00 01  mov qword ptr [rsp + 0x88], 0x1000000
00AE5A2C  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AE5A34  48 89 84 24 60 03 00 00         mov qword ptr [rsp + 0x360], rax
00AE5A3C  44 89 BC 24 68 03 00 00         mov dword ptr [rsp + 0x368], r15d
00AE5A44  44 89 B4 24 6C 03 00 00         mov dword ptr [rsp + 0x36c], r14d
00AE5A4C  48 8D 84 24 30 03 00 00         lea rax, [rsp + 0x330]
00AE5A54  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE5A59  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
00AE5A61  45 33 C9                        xor r9d, r9d
00AE5A64  45 33 C0                        xor r8d, r8d
00AE5A67  48 8D 15 03 D2 56 FF            lea rdx, [rip - 0xa92dfd]
00AE5A6E  48 8D 0D CB 2B 32 00            lea rcx, [rip + 0x322bcb]
00AE5A75  E8 66 06 94 FF                  call 0x1404260e0
00AE5A7A  E8 D9 1F 9D FF                  call 0x1404b7a58
00AE5A7F  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE5A84  85 C0                           test eax, eax
00AE5A86  0F 85 A8 01 00 00               jne 0x140ae5c34
00AE5A8C  45 33 C0                        xor r8d, r8d
00AE5A8F  B2 01                           mov dl, 1
00AE5A91  E8 36 03 F6 FF                  call 0x140a45dcc
00AE5A96  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE5A9B  BA 50 73 51 79                  mov edx, 0x79517350
00AE5AA0  E8 3B 1E 81 FF                  call 0x1402f78e0
00AE5AA5  8B C7                           mov eax, edi
00AE5AA7  E9 17 45 00 00                  jmp 0x140ae9fc3
00AE5AAC  E9 12 45 00 00                  jmp 0x140ae9fc3
00AE5AB1  83 FF 04                        cmp edi, 4
00AE5AB4  0F 85 E3 44 00 00               jne 0x140ae9f9d
00AE5ABA  8B 1B                           mov ebx, dword ptr [rbx]
00AE5ABC  89 9C 24 B4 00 00 00            mov dword ptr [rsp + 0xb4], ebx
00AE5AC3  66 85 DB                        test bx, bx
00AE5AC6  0F 84 09 34 00 00               je 0x140ae8ed5
00AE5ACC  0F B7 C3                        movzx eax, bx
00AE5ACF  A9 FC FF FF FF                  test eax, 0xfffffffc
00AE5AD4  0F 85 FB 33 00 00               jne 0x140ae8ed5
00AE5ADA  4C 8B 05 B7 0F 4E 00            mov r8, qword ptr [rip + 0x4e0fb7]
00AE5AE1  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE5AE6  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE5AEB  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE5AF0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE5AF5  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE5AFD  45 0F B6 CC                     movzx r9d, r12b
00AE5B01  BA 00 02 00 00                  mov edx, 0x200
00AE5B06  48 8B CE                        mov rcx, rsi
00AE5B09  E8 42 3B D8 FF                  call 0x140869650
00AE5B0E  8B F8                           mov edi, eax
00AE5B10  85 C0                           test eax, eax
00AE5B12  0F 88 AB 44 00 00               js 0x140ae9fc3
00AE5B18  44 0F B7 EB                     movzx r13d, bx
00AE5B1C  66 41 83 E5 01                  and r13w, 1
00AE5B21  0F 84 C7 00 00 00               je 0x140ae5bee
00AE5B27  83 3D 12 2B 32 00 05            cmp dword ptr [rip + 0x322b12], 5
00AE5B2E  0F 86 BA 00 00 00               jbe 0x140ae5bee
00AE5B34  49 B8 00 00 00 00 00 40 00 00   movabs r8, 0x400000000000
00AE5B3E  4C 85 05 0B 2B 32 00            test qword ptr [rip + 0x322b0b], r8
00AE5B45  74 17                           je 0x140ae5b5e
00AE5B47  48 8B 05 0A 2B 32 00            mov rax, qword ptr [rip + 0x322b0a]
00AE5B4E  49 23 C0                        and rax, r8
00AE5B51  48 3B 05 00 2B 32 00            cmp rax, qword ptr [rip + 0x322b00]
00AE5B58  75 04                           jne 0x140ae5b5e
00AE5B5A  B0 01                           mov al, 1
00AE5B5C  EB 02                           jmp 0x140ae5b60
00AE5B5E  32 C0                           xor al, al
00AE5B60  84 C0                           test al, al
00AE5B62  0F 84 86 00 00 00               je 0x140ae5bee
00AE5B68  0F B6 84 24 B7 00 00 00         movzx eax, byte ptr [rsp + 0xb7]
00AE5B70  88 44 24 48                     mov byte ptr [rsp + 0x48], al
00AE5B74  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00AE5B79  48 89 84 24 50 03 00 00         mov qword ptr [rsp + 0x350], rax
00AE5B81  C7 84 24 58 03 00 00 01 00 00 00  mov dword ptr [rsp + 0x358], 1
00AE5B8C  44 89 B4 24 5C 03 00 00         mov dword ptr [rsp + 0x35c], r14d
00AE5B94  48 C7 84 24 88 00 00 00 00 00 00 01  mov qword ptr [rsp + 0x88], 0x1000000
00AE5BA0  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AE5BA8  48 89 84 24 60 03 00 00         mov qword ptr [rsp + 0x360], rax
00AE5BB0  44 89 BC 24 68 03 00 00         mov dword ptr [rsp + 0x368], r15d
00AE5BB8  44 89 B4 24 6C 03 00 00         mov dword ptr [rsp + 0x36c], r14d
00AE5BC0  48 8D 84 24 30 03 00 00         lea rax, [rsp + 0x330]
00AE5BC8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE5BCD  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
00AE5BD5  45 33 C9                        xor r9d, r9d
00AE5BD8  45 33 C0                        xor r8d, r8d
00AE5BDB  48 8D 15 CF CF 56 FF            lea rdx, [rip - 0xa93031]
00AE5BE2  48 8D 0D 57 2A 32 00            lea rcx, [rip + 0x322a57]
00AE5BE9  E8 F2 04 94 FF                  call 0x1404260e0
00AE5BEE  F6 C3 02                        test bl, 2
00AE5BF1  74 23                           je 0x140ae5c16
00AE5BF3  45 0F B6 CC                     movzx r9d, r12b
00AE5BF7  4C 8B C6                        mov r8, rsi
00AE5BFA  0F B6 94 24 B6 00 00 00         movzx edx, byte ptr [rsp + 0xb6]
00AE5C02  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE5C07  E8 D8 05 F1 FF                  call 0x1409f61e4
00AE5C0C  8B F8                           mov edi, eax
00AE5C0E  85 C0                           test eax, eax
00AE5C10  0F 88 80 FE FF FF               js 0x140ae5a96
00AE5C16  E8 3D 1E 9D FF                  call 0x1404b7a58
00AE5C1B  85 C0                           test eax, eax
00AE5C1D  75 10                           jne 0x140ae5c2f
00AE5C1F  66 45 85 ED                     test r13w, r13w
00AE5C23  74 0A                           je 0x140ae5c2f
00AE5C25  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE5C2A  E9 5D FE FF FF                  jmp 0x140ae5a8c
00AE5C2F  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE5C34  E8 93 45 00 00                  call 0x140aea1cc
00AE5C39  E9 58 FE FF FF                  jmp 0x140ae5a96
00AE5C3E  E9 80 43 00 00                  jmp 0x140ae9fc3
00AE5C43  83 FF 01                        cmp edi, 1
00AE5C46  0F 85 51 43 00 00               jne 0x140ae9f9d
00AE5C4C  0F B6 1B                        movzx ebx, byte ptr [rbx]
00AE5C4F  88 9C 24 B0 00 00 00            mov byte ptr [rsp + 0xb0], bl
00AE5C56  4C 8B 05 3B 0E 4E 00            mov r8, qword ptr [rip + 0x4e0e3b]
00AE5C5D  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE5C62  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE5C67  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE5C6C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE5C71  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE5C79  45 0F B6 CC                     movzx r9d, r12b
00AE5C7D  BA 00 20 00 00                  mov edx, 0x2000
00AE5C82  48 8B CE                        mov rcx, rsi
00AE5C85  E8 C6 39 D8 FF                  call 0x140869650
00AE5C8A  85 C0                           test eax, eax
00AE5C8C  0F 88 31 43 00 00               js 0x140ae9fc3
00AE5C92  83 3D A7 29 32 00 05            cmp dword ptr [rip + 0x3229a7], 5
00AE5C99  0F 86 AE 00 00 00               jbe 0x140ae5d4d
00AE5C9F  49 B8 00 00 00 00 00 40 00 00   movabs r8, 0x400000000000
00AE5CA9  4C 85 05 A0 29 32 00            test qword ptr [rip + 0x3229a0], r8
00AE5CB0  74 17                           je 0x140ae5cc9
00AE5CB2  48 8B 05 9F 29 32 00            mov rax, qword ptr [rip + 0x32299f]
00AE5CB9  49 23 C0                        and rax, r8
00AE5CBC  48 3B 05 95 29 32 00            cmp rax, qword ptr [rip + 0x322995]
00AE5CC3  75 04                           jne 0x140ae5cc9
00AE5CC5  B0 01                           mov al, 1
00AE5CC7  EB 02                           jmp 0x140ae5ccb
00AE5CC9  32 C0                           xor al, al
00AE5CCB  84 C0                           test al, al
00AE5CCD  74 7E                           je 0x140ae5d4d
00AE5CCF  88 5C 24 48                     mov byte ptr [rsp + 0x48], bl
00AE5CD3  48 8D 44 24 48                  lea rax, [rsp + 0x48]
00AE5CD8  48 89 84 24 50 03 00 00         mov qword ptr [rsp + 0x350], rax
00AE5CE0  C7 84 24 58 03 00 00 01 00 00 00  mov dword ptr [rsp + 0x358], 1
00AE5CEB  44 89 B4 24 5C 03 00 00         mov dword ptr [rsp + 0x35c], r14d
00AE5CF3  48 C7 84 24 88 00 00 00 00 00 00 01  mov qword ptr [rsp + 0x88], 0x1000000
00AE5CFF  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AE5D07  48 89 84 24 60 03 00 00         mov qword ptr [rsp + 0x360], rax
00AE5D0F  44 89 BC 24 68 03 00 00         mov dword ptr [rsp + 0x368], r15d
00AE5D17  44 89 B4 24 6C 03 00 00         mov dword ptr [rsp + 0x36c], r14d
00AE5D1F  48 8D 84 24 30 03 00 00         lea rax, [rsp + 0x330]
00AE5D27  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE5D2C  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
00AE5D34  45 33 C9                        xor r9d, r9d
00AE5D37  45 33 C0                        xor r8d, r8d
00AE5D3A  48 8D 15 CD CE 56 FF            lea rdx, [rip - 0xa93133]
00AE5D41  48 8D 0D F8 28 32 00            lea rcx, [rip + 0x3228f8]
00AE5D48  E8 93 03 94 FF                  call 0x1404260e0
00AE5D4D  E8 06 1D 9D FF                  call 0x1404b7a58
00AE5D52  85 C0                           test eax, eax
00AE5D54  0F 85 ED FA FF FF               jne 0x140ae5847
00AE5D5A  84 DB                           test bl, bl
00AE5D5C  0F 95 C2                        setne dl
00AE5D5F  45 33 C0                        xor r8d, r8d
00AE5D62  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE5D67  E8 60 00 F6 FF                  call 0x140a45dcc
00AE5D6C  E9 D6 FA FF FF                  jmp 0x140ae5847
00AE5D71  E9 4D 42 00 00                  jmp 0x140ae9fc3
00AE5D76  83 FF 04                        cmp edi, 4
00AE5D79  0F 85 1E 42 00 00               jne 0x140ae9f9d
00AE5D7F  8B 3B                           mov edi, dword ptr [rbx]
00AE5D81  89 BC 24 54 01 00 00            mov dword ptr [rsp + 0x154], edi
00AE5D88  4C 8B 05 09 0D 4E 00            mov r8, qword ptr [rip + 0x4e0d09]
00AE5D8F  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE5D94  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE5D99  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE5D9E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE5DA3  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE5DAB  45 0F B6 CC                     movzx r9d, r12b
00AE5DAF  BA 00 02 00 00                  mov edx, 0x200
00AE5DB4  48 8B CE                        mov rcx, rsi
00AE5DB7  E8 94 38 D8 FF                  call 0x140869650
00AE5DBC  8B F0                           mov esi, eax
00AE5DBE  85 C0                           test eax, eax
00AE5DC0  0F 88 FD 41 00 00               js 0x140ae9fc3
00AE5DC6  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE5DCB  48 81 C1 E8 01 00 00            add rcx, 0x1e8
00AE5DD2  E8 49 08 73 FF                  call 0x140216620
00AE5DD7  84 C0                           test al, al
00AE5DD9  74 4A                           je 0x140ae5e25
00AE5DDB  33 D2                           xor edx, edx
00AE5DDD  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE5DE2  E8 09 3F DE FF                  call 0x1408c9cf0
00AE5DE7  48 8B D8                        mov rbx, rax
00AE5DEA  48 85 C0                        test rax, rax
00AE5DED  74 20                           je 0x140ae5e0f
00AE5DEF  90                              nop
00AE5DF0  8B D7                           mov edx, edi
00AE5DF2  48 8B CB                        mov rcx, rbx
00AE5DF5  E8 FE D9 9E FF                  call 0x1404d37f8
00AE5DFA  48 8B D3                        mov rdx, rbx
00AE5DFD  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE5E02  E8 E9 3E DE FF                  call 0x1408c9cf0
00AE5E07  48 8B D8                        mov rbx, rax
00AE5E0A  48 85 C0                        test rax, rax
00AE5E0D  75 E1                           jne 0x140ae5df0
00AE5E0F  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE5E14  48 81 C1 E8 01 00 00            add rcx, 0x1e8
00AE5E1B  E8 60 40 86 FF                  call 0x140349e80
00AE5E20  E9 77 F9 FF FF                  jmp 0x140ae579c
00AE5E25  BE 0A 01 00 C0                  mov esi, 0xc000010a
00AE5E2A  E9 6D F9 FF FF                  jmp 0x140ae579c
00AE5E2F  E9 8F 41 00 00                  jmp 0x140ae9fc3
00AE5E34  83 FF 04                        cmp edi, 4
00AE5E37  0F 85 60 41 00 00               jne 0x140ae9f9d
00AE5E3D  8B 1B                           mov ebx, dword ptr [rbx]
00AE5E3F  89 9C 24 58 01 00 00            mov dword ptr [rsp + 0x158], ebx
00AE5E46  4C 8B 05 4B 0C 4E 00            mov r8, qword ptr [rip + 0x4e0c4b]
00AE5E4D  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE5E52  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE5E57  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE5E5C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE5E61  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE5E69  45 0F B6 CC                     movzx r9d, r12b
00AE5E6D  BA 00 02 00 00                  mov edx, 0x200
00AE5E72  48 8B CE                        mov rcx, rsi
00AE5E75  E8 D6 37 D8 FF                  call 0x140869650
00AE5E7A  85 C0                           test eax, eax
00AE5E7C  0F 88 41 41 00 00               js 0x140ae9fc3
00AE5E82  44 8B C3                        mov r8d, ebx
00AE5E85  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
00AE5E8A  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE5E8F  E8 14 E3 F1 FF                  call 0x140a041a8
00AE5E94  E9 AE F9 FF FF                  jmp 0x140ae5847
00AE5E99  E9 25 41 00 00                  jmp 0x140ae9fc3
00AE5E9E  45 0F B6 CC                     movzx r9d, r12b
00AE5EA2  44 8B C7                        mov r8d, edi
00AE5EA5  48 8B D3                        mov rdx, rbx
00AE5EA8  48 8B CE                        mov rcx, rsi
00AE5EAB  E8 F8 49 ED FF                  call 0x1409ba8a8
00AE5EB0  E9 0E 41 00 00                  jmp 0x140ae9fc3
00AE5EB5  83 FF 08                        cmp edi, 8
00AE5EB8  75 1A                           jne 0x140ae5ed4
00AE5EBA  44 89 B4 24 D0 00 00 00         mov dword ptr [rsp + 0xd0], r14d
00AE5EC2  4C 8B 2B                        mov r13, qword ptr [rbx]
00AE5EC5  4C 89 AC 24 78 01 00 00         mov qword ptr [rsp + 0x178], r13
00AE5ECD  EB 42                           jmp 0x140ae5f11
00AE5ECF  E9 EF 40 00 00                  jmp 0x140ae9fc3
00AE5ED4  83 FF 10                        cmp edi, 0x10
00AE5ED7  0F 85 C0 40 00 00               jne 0x140ae9f9d
00AE5EDD  48 8B 03                        mov rax, qword ptr [rbx]
00AE5EE0  48 89 84 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], rax
00AE5EE8  48 89 84 24 78 01 00 00         mov qword ptr [rsp + 0x178], rax
00AE5EF0  44 8B 6B 08                     mov r13d, dword ptr [rbx + 8]
00AE5EF4  44 89 AC 24 D0 00 00 00         mov dword ptr [rsp + 0xd0], r13d
00AE5EFC  49 F7 C5 F8 FF FF FF            test r13, -8
00AE5F03  0F 85 CC 2F 00 00               jne 0x140ae8ed5
00AE5F09  4C 8B AC 24 C8 00 00 00         mov r13, qword ptr [rsp + 0xc8]
00AE5F11  41 0F B6 D4                     movzx edx, r12b
00AE5F15  48 8B 0D 5C 3B 4F 00            mov rcx, qword ptr [rip + 0x4f3b5c]
00AE5F1C  E8 FF BE D8 FF                  call 0x140871e20
00AE5F21  84 C0                           test al, al
00AE5F23  0F 84 E5 F9 FF FF               je 0x140ae590e
00AE5F29  4C 8B 05 40 10 4E 00            mov r8, qword ptr [rip + 0x4e1040]
00AE5F30  4C 89 B4 24 38 01 00 00         mov qword ptr [rsp + 0x138], r14
00AE5F38  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00AE5F3D  48 8D 84 24 38 01 00 00         lea rax, [rsp + 0x138]
00AE5F45  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AE5F4A  45 0F B6 CC                     movzx r9d, r12b
00AE5F4E  33 D2                           xor edx, edx
00AE5F50  49 8B CD                        mov rcx, r13
00AE5F53  E8 58 2E D8 FF                  call 0x140868db0
00AE5F58  4C 8B AC 24 38 01 00 00         mov r13, qword ptr [rsp + 0x138]
00AE5F60  4C 89 AC 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r13
00AE5F68  85 C0                           test eax, eax
00AE5F6A  0F 88 53 40 00 00               js 0x140ae9fc3
00AE5F70  4C 8B 05 21 0B 4E 00            mov r8, qword ptr [rip + 0x4e0b21]
00AE5F77  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE5F7C  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE5F81  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE5F86  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE5F8B  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE5F93  45 0F B6 CC                     movzx r9d, r12b
00AE5F97  BA 00 08 00 00                  mov edx, 0x800
00AE5F9C  48 8B CE                        mov rcx, rsi
00AE5F9F  E8 AC 36 D8 FF                  call 0x140869650
00AE5FA4  8B F0                           mov esi, eax
00AE5FA6  85 C0                           test eax, eax
00AE5FA8  79 0F                           jns 0x140ae5fb9
00AE5FAA  49 8B CD                        mov rcx, r13
00AE5FAD  E8 9E 33 81 FF                  call 0x1402f9350
00AE5FB2  8B C6                           mov eax, esi
00AE5FB4  E9 0A 40 00 00                  jmp 0x140ae9fc3
00AE5FB9  8B 94 24 D0 00 00 00            mov edx, dword ptr [rsp + 0xd0]
00AE5FC0  49 0B D5                        or rdx, r13
00AE5FC3  48 89 94 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rdx
00AE5FCB  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE5FD0  0F 0D 88 40 02 00 00            prefetchw byte ptr [rax + 0x240]
00AE5FD7  4C 8B A0 40 02 00 00            mov r12, qword ptr [rax + 0x240]
00AE5FDE  4C 89 A4 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], r12
00AE5FE6  41 8B C4                        mov eax, r12d
00AE5FE9  83 E0 07                        and eax, 7
00AE5FEC  83 FF 10                        cmp edi, 0x10
00AE5FEF  75 46                           jne 0x140ae6037
00AE5FF1  89 43 08                        mov dword ptr [rbx + 8], eax
00AE5FF4  EB 30                           jmp 0x140ae6026
00AE5FF6  8B F0                           mov esi, eax
00AE5FF8  45 33 F6                        xor r14d, r14d
00AE5FFB  45 8D 7E 08                     lea r15d, [r14 + 8]
00AE5FFF  4C 8B AC 24 C8 00 00 00         mov r13, qword ptr [rsp + 0xc8]
00AE6007  4C 8B A4 24 A8 00 00 00         mov r12, qword ptr [rsp + 0xa8]
00AE600F  48 8B 94 24 F8 00 00 00         mov rdx, qword ptr [rsp + 0xf8]
00AE6017  48 8B 9C 24 10 01 00 00         mov rbx, qword ptr [rsp + 0x110]
00AE601F  8B BC 24 80 00 00 00            mov edi, dword ptr [rsp + 0x80]
00AE6026  85 F6                           test esi, esi
00AE6028  79 23                           jns 0x140ae604d
00AE602A  49 8B CD                        mov rcx, r13
00AE602D  E8 1E 33 81 FF                  call 0x1402f9350
00AE6032  E9 65 F7 FF FF                  jmp 0x140ae579c
00AE6037  85 C0                           test eax, eax
00AE6039  74 12                           je 0x140ae604d
00AE603B  49 8B CD                        mov rcx, r13
00AE603E  E8 0D 33 81 FF                  call 0x1402f9350
00AE6043  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE6048  E9 4F F7 FF FF                  jmp 0x140ae579c
00AE604D  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE6052  49 8B C4                        mov rax, r12
00AE6055  F0 48 0F B1 91 40 02 00 00      lock cmpxchg qword ptr [rcx + 0x240], rdx
00AE605E  4C 8B E0                        mov r12, rax
00AE6061  0F 85 77 FF FF FF               jne 0x140ae5fde
00AE6067  48 85 C0                        test rax, rax
00AE606A  0F 84 B1 00 00 00               je 0x140ae6121
00AE6070  0F 57 C0                        xorps xmm0, xmm0
00AE6073  F3 0F 7F 84 24 38 03 00 00      movdqu xmmword ptr [rsp + 0x338], xmm0
00AE607C  0F 57 C9                        xorps xmm1, xmm1
00AE607F  F3 0F 7F 8C 24 48 03 00 00      movdqu xmmword ptr [rsp + 0x348], xmm1
00AE6088  49 83 E4 F8                     and r12, 0xfffffffffffffff8
00AE608C  B8 30 00 00 00                  mov eax, 0x30
00AE6091  66 89 84 24 32 03 00 00         mov word ptr [rsp + 0x332], ax
00AE6099  66 44 89 BC 24 30 03 00 00      mov word ptr [rsp + 0x330], r15w
00AE60A2  B8 0D 00 00 00                  mov eax, 0xd
00AE60A7  66 89 84 24 34 03 00 00         mov word ptr [rsp + 0x334], ax
00AE60AF  66 44 89 B4 24 36 03 00 00      mov word ptr [rsp + 0x336], r14w
00AE60B8  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE60BD  48 8B 88 D0 01 00 00            mov rcx, qword ptr [rax + 0x1d0]
00AE60C4  48 89 8C 24 58 03 00 00         mov qword ptr [rsp + 0x358], rcx
00AE60CC  BE 17 00 00 C0                  mov esi, 0xc0000017
00AE60D1  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00AE60D6  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
00AE60E0  48 8D 94 24 30 03 00 00         lea rdx, [rsp + 0x330]
00AE60E8  49 8B CC                        mov rcx, r12
00AE60EB  E8 50 48 DA FF                  call 0x14088a940
00AE60F0  3B C6                           cmp eax, esi
00AE60F2  74 04                           je 0x140ae60f8
00AE60F4  3B C3                           cmp eax, ebx
00AE60F6  75 12                           jne 0x140ae610a
00AE60F8  4C 8D 05 C9 B7 52 FF            lea r8, [rip - 0xad4837]
00AE60FF  33 D2                           xor edx, edx
00AE6101  33 C9                           xor ecx, ecx
00AE6103  E8 48 34 72 FF                  call 0x140209550
00AE6108  EB D6                           jmp 0x140ae60e0
00AE610A  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
00AE610F  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE6114  E8 2F 3A 93 FF                  call 0x140419b48
00AE6119  49 8B CC                        mov rcx, r12
00AE611C  E8 2F 32 81 FF                  call 0x1402f9350
00AE6121  41 8B F6                        mov esi, r14d
00AE6124  E9 73 F6 FF FF                  jmp 0x140ae579c
00AE6129  E9 95 3E 00 00                  jmp 0x140ae9fc3
00AE612E  83 FF 10                        cmp edi, 0x10
00AE6131  0F 85 66 3E 00 00               jne 0x140ae9f9d
00AE6137  4C 8B 0B                        mov r9, qword ptr [rbx]
00AE613A  4C 89 8C 24 00 02 00 00         mov qword ptr [rsp + 0x200], r9
00AE6142  4C 8B C6                        mov r8, rsi
00AE6145  41 0F B6 D4                     movzx edx, r12b
00AE6149  49 8B CB                        mov rcx, r11
00AE614C  E8 1F E7 C9 FF                  call 0x140784870
00AE6151  E9 6D 3E 00 00                  jmp 0x140ae9fc3
00AE6156  E9 68 3E 00 00                  jmp 0x140ae9fc3
00AE615B  4C 8B 05 36 09 4E 00            mov r8, qword ptr [rip + 0x4e0936]
00AE6162  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE6167  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE616C  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE6171  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE6176  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE617E  45 0F B6 CC                     movzx r9d, r12b
00AE6182  BA 20 02 00 00                  mov edx, 0x220
00AE6187  48 8B CE                        mov rcx, rsi
00AE618A  E8 C1 34 D8 FF                  call 0x140869650
00AE618F  85 C0                           test eax, eax
00AE6191  0F 88 2C 3E 00 00               js 0x140ae9fc3
00AE6197  44 8B C7                        mov r8d, edi
00AE619A  48 8B D3                        mov rdx, rbx
00AE619D  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE61A2  E8 59 64 A1 FF                  call 0x1404fc600
00AE61A7  8B D8                           mov ebx, eax
00AE61A9  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE61AE  BA 50 73 51 79                  mov edx, 0x79517350
00AE61B3  E8 28 17 81 FF                  call 0x1402f78e0
00AE61B8  8B C3                           mov eax, ebx
00AE61BA  E9 04 3E 00 00                  jmp 0x140ae9fc3
00AE61BF  4C 8B 05 D2 08 4E 00            mov r8, qword ptr [rip + 0x4e08d2]
00AE61C6  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE61CB  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE61D0  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE61D5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE61DA  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE61E2  45 0F B6 CC                     movzx r9d, r12b
00AE61E6  BA 20 02 00 00                  mov edx, 0x220
00AE61EB  48 8B CE                        mov rcx, rsi
00AE61EE  E8 5D 34 D8 FF                  call 0x140869650
00AE61F3  85 C0                           test eax, eax
00AE61F5  0F 88 C8 3D 00 00               js 0x140ae9fc3
00AE61FB  44 8B C7                        mov r8d, edi
00AE61FE  48 8B D3                        mov rdx, rbx
00AE6201  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE6206  E8 F5 63 A1 FF                  call 0x1404fc600
00AE620B  EB 9A                           jmp 0x140ae61a7
00AE620D  4C 8B 05 84 08 4E 00            mov r8, qword ptr [rip + 0x4e0884]
00AE6214  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE6219  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE621E  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE6223  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE6228  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE6230  45 0F B6 CC                     movzx r9d, r12b
00AE6234  BA 00 02 00 00                  mov edx, 0x200
00AE6239  48 8B CE                        mov rcx, rsi
00AE623C  E8 0F 34 D8 FF                  call 0x140869650
00AE6241  85 C0                           test eax, eax
00AE6243  0F 88 7A 3D 00 00               js 0x140ae9fc3
00AE6249  44 8B C7                        mov r8d, edi
00AE624C  48 8B D3                        mov rdx, rbx
00AE624F  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE6254  E8 A7 63 A1 FF                  call 0x1404fc600
00AE6259  E9 49 FF FF FF                  jmp 0x140ae61a7
00AE625E  41 0F B6 D4                     movzx edx, r12b
00AE6262  48 8B 0D 0F 38 4F 00            mov rcx, qword ptr [rip + 0x4f380f]
00AE6269  E8 B2 BB D8 FF                  call 0x140871e20
00AE626E  84 C0                           test al, al
00AE6270  0F 84 98 F6 FF FF               je 0x140ae590e
00AE6276  4C 8B 05 1B 08 4E 00            mov r8, qword ptr [rip + 0x4e081b]
00AE627D  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE6282  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE6287  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE628C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE6291  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE6299  45 0F B6 CC                     movzx r9d, r12b
00AE629D  BA 00 02 00 00                  mov edx, 0x200
00AE62A2  48 8B CE                        mov rcx, rsi
00AE62A5  E8 A6 33 D8 FF                  call 0x140869650
00AE62AA  85 C0                           test eax, eax
00AE62AC  0F 88 11 3D 00 00               js 0x140ae9fc3
00AE62B2  BA 50 73 51 79                  mov edx, 0x79517350
00AE62B7  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE62BC  E8 1F 16 81 FF                  call 0x1402f78e0
00AE62C1  B8 02 00 00 C0                  mov eax, 0xc0000002
00AE62C6  E9 F8 3C 00 00                  jmp 0x140ae9fc3
00AE62CB  83 FF 01                        cmp edi, 1
00AE62CE  0F 85 C9 3C 00 00               jne 0x140ae9f9d
00AE62D4  0F B6 1B                        movzx ebx, byte ptr [rbx]
00AE62D7  88 5C 24 71                     mov byte ptr [rsp + 0x71], bl
00AE62DB  4C 8B 05 B6 07 4E 00            mov r8, qword ptr [rip + 0x4e07b6]
00AE62E2  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE62E7  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE62EC  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE62F1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE62F6  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE62FE  45 0F B6 CC                     movzx r9d, r12b
00AE6302  BA 00 02 00 00                  mov edx, 0x200
00AE6307  48 8B CE                        mov rcx, rsi
00AE630A  E8 41 33 D8 FF                  call 0x140869650
00AE630F  85 C0                           test eax, eax
00AE6311  0F 88 AC 3C 00 00               js 0x140ae9fc3
00AE6317  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
00AE631C  49 8B D7                        mov rdx, r15
00AE631F  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE6324  E8 3B 9E 97 FF                  call 0x140460164
00AE6329  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE632E  84 DB                           test bl, bl
00AE6330  74 09                           je 0x140ae633b
00AE6332  83 88 88 03 00 00 04            or dword ptr [rax + 0x388], 4
00AE6339  EB 07                           jmp 0x140ae6342
00AE633B  83 A0 88 03 00 00 FB            and dword ptr [rax + 0x388], 0xfffffffb
00AE6342  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE6347  48 83 B9 10 03 00 00 00         cmp qword ptr [rcx + 0x310], 0
00AE634F  74 24                           je 0x140ae6375
00AE6351  44 0F B7 81 EC 06 00 00         movzx r8d, word ptr [rcx + 0x6ec]
00AE6359  BA 4C 01 00 00                  mov edx, 0x14c
00AE635E  66 44 3B C2                     cmp r8w, dx
00AE6362  74 0B                           je 0x140ae636f
00AE6364  B8 C4 01 00 00                  mov eax, 0x1c4
00AE6369  66 44 3B C0                     cmp r8w, ax
00AE636D  75 06                           jne 0x140ae6375
00AE636F  B3 01                           mov bl, 1
00AE6371  88 5C 24 71                     mov byte ptr [rsp + 0x71], bl
00AE6375  84 DB                           test bl, bl
00AE6377  74 1B                           je 0x140ae6394
00AE6379  F0 0F BA A9 88 00 00 00 00      lock bts dword ptr [rcx + 0x88], 0
00AE6382  49 8B D7                        mov rdx, r15
00AE6385  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE638A  E8 31 9E 97 FF                  call 0x1404601c0
00AE638F  E9 B3 F4 FF FF                  jmp 0x140ae5847
00AE6394  F0 0F BA B1 88 00 00 00 00      lock btr dword ptr [rcx + 0x88], 0
00AE639D  49 8B D7                        mov rdx, r15
00AE63A0  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE63A5  E8 16 9E 97 FF                  call 0x1404601c0
00AE63AA  E9 98 F4 FF FF                  jmp 0x140ae5847
00AE63AF  E9 0F 3C 00 00                  jmp 0x140ae9fc3
00AE63B4  83 FF 04                        cmp edi, 4
00AE63B7  0F 85 E0 3B 00 00               jne 0x140ae9f9d
00AE63BD  8B 1B                           mov ebx, dword ptr [rbx]
00AE63BF  89 9C 24 5C 01 00 00            mov dword ptr [rsp + 0x15c], ebx
00AE63C6  41 0F B6 D4                     movzx edx, r12b
00AE63CA  48 8B 0D A7 36 4F 00            mov rcx, qword ptr [rip + 0x4f36a7]
00AE63D1  E8 4A BA D8 FF                  call 0x140871e20
00AE63D6  84 C0                           test al, al
00AE63D8  0F 84 30 F5 FF FF               je 0x140ae590e
00AE63DE  4C 8B 05 B3 06 4E 00            mov r8, qword ptr [rip + 0x4e06b3]
00AE63E5  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE63EA  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE63EF  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE63F4  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE63F9  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE6401  45 0F B6 CC                     movzx r9d, r12b
00AE6405  BA 00 02 00 00                  mov edx, 0x200
00AE640A  48 8B CE                        mov rcx, rsi
00AE640D  E8 3E 32 D8 FF                  call 0x140869650
00AE6412  8B F0                           mov esi, eax
00AE6414  85 C0                           test eax, eax
00AE6416  0F 88 8F F3 FF FF               js 0x140ae57ab
00AE641C  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE6421  48 83 B9 40 06 00 00 00         cmp qword ptr [rcx + 0x640], 0
00AE6429  74 16                           je 0x140ae6441
00AE642B  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE6430  BA 50 73 51 79                  mov edx, 0x79517350
00AE6435  E8 A6 14 81 FF                  call 0x1402f78e0
00AE643A  8B C6                           mov eax, esi
00AE643C  E9 82 3B 00 00                  jmp 0x140ae9fc3
00AE6441  85 DB                           test ebx, ebx
00AE6443  74 10                           je 0x140ae6455
00AE6445  F0 81 89 F4 01 00 00 00 00 00 01  lock or dword ptr [rcx + 0x1f4], 0x1000000
00AE6450  E9 47 F3 FF FF                  jmp 0x140ae579c
00AE6455  F0 81 A1 F4 01 00 00 FF FF FF FE  lock and dword ptr [rcx + 0x1f4], 0xfeffffff
00AE6460  E9 37 F3 FF FF                  jmp 0x140ae579c
00AE6465  E9 59 3B 00 00                  jmp 0x140ae9fc3
00AE646A  83 FF 08                        cmp edi, 8
00AE646D  75 15                           jne 0x140ae6484
00AE646F  48 8B 03                        mov rax, qword ptr [rbx]
00AE6472  48 89 84 24 20 02 00 00         mov qword ptr [rsp + 0x220], rax
00AE647A  48 85 C0                        test rax, rax
00AE647D  EB 2A                           jmp 0x140ae64a9
00AE647F  E9 3F 3B 00 00                  jmp 0x140ae9fc3
00AE6484  83 FF 10                        cmp edi, 0x10
00AE6487  0F 85 10 3B 00 00               jne 0x140ae9f9d
00AE648D  0F 10 03                        movups xmm0, xmmword ptr [rbx]
00AE6490  0F 11 84 24 20 02 00 00         movups xmmword ptr [rsp + 0x220], xmm0
00AE6498  33 D2                           xor edx, edx
00AE649A  48 8D 8C 24 20 02 00 00         lea rcx, [rsp + 0x220]
00AE64A2  E8 49 4D 99 FF                  call 0x14047b1f0
00AE64A7  84 C0                           test al, al
00AE64A9  0F 84 26 2A 00 00               je 0x140ae8ed5
00AE64AF  4C 8B 05 E2 05 4E 00            mov r8, qword ptr [rip + 0x4e05e2]
00AE64B6  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE64BB  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE64C0  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE64C5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE64CA  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE64D2  45 0F B6 CC                     movzx r9d, r12b
00AE64D6  BA 00 02 00 00                  mov edx, 0x200
00AE64DB  48 8B CE                        mov rcx, rsi
00AE64DE  E8 6D 31 D8 FF                  call 0x140869650
00AE64E3  85 C0                           test eax, eax
00AE64E5  0F 88 D8 3A 00 00               js 0x140ae9fc3
00AE64EB  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE64F0  F7 81 88 00 00 00 00 10 00 00   test dword ptr [rcx + 0x88], 0x1000
00AE64FA  74 16                           je 0x140ae6512
00AE64FC  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE6501  BA 50 73 51 79                  mov edx, 0x79517350
00AE6506  E8 D5 13 81 FF                  call 0x1402f78e0
00AE650B  8B C6                           mov eax, esi
00AE650D  E9 B1 3A 00 00                  jmp 0x140ae9fc3
00AE6512  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00AE6517  E8 3C 94 7E FF                  call 0x1402cf958
00AE651C  83 FF 08                        cmp edi, 8
00AE651F  75 3F                           jne 0x140ae6560
00AE6521  0F B7 44 24 78                  movzx eax, word ptr [rsp + 0x78]
00AE6526  48 8D 15 D3 9A 51 FF            lea rdx, [rip - 0xae652d]
00AE652D  48 8B 8C C2 28 71 FC 00         mov rcx, qword ptr [rdx + rax*8 + 0xfc7128]
00AE6535  48 23 8C 24 20 02 00 00         and rcx, qword ptr [rsp + 0x220]
00AE653D  48 3B 8C 24 20 02 00 00         cmp rcx, qword ptr [rsp + 0x220]
00AE6545  0F 85 F8 FA FF FF               jne 0x140ae6043
00AE654B  0F B7 44 24 78                  movzx eax, word ptr [rsp + 0x78]
00AE6550  66 89 84 24 28 02 00 00         mov word ptr [rsp + 0x228], ax
00AE6558  48 89 8C 24 20 02 00 00         mov qword ptr [rsp + 0x220], rcx
00AE6560  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
00AE6565  66 41 FF 8F E4 01 00 00         dec word ptr [r15 + 0x1e4]
00AE656D  90                              nop
00AE656E  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE6573  48 81 C1 E8 01 00 00            add rcx, 0x1e8
00AE657A  E8 A1 00 73 FF                  call 0x140216620
00AE657F  84 C0                           test al, al
00AE6581  0F 84 83 00 00 00               je 0x140ae660a
00AE6587  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE658C  E8 E3 72 9C FF                  call 0x1404ad874
00AE6591  48 8D 84 24 D4 00 00 00         lea rax, [rsp + 0xd4]
00AE6599  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AE659E  4C 8D 8C 24 20 02 00 00         lea r9, [rsp + 0x220]
00AE65A6  45 33 C0                        xor r8d, r8d
00AE65A9  33 D2                           xor edx, edx
00AE65AB  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE65B0  E8 4F A3 F7 FF                  call 0x140a60904
00AE65B5  8B F0                           mov esi, eax
00AE65B7  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE65BC  E8 3F C2 9C FF                  call 0x1404b2800
00AE65C1  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE65C6  48 81 C1 E8 01 00 00            add rcx, 0x1e8
00AE65CD  E8 AE 38 86 FF                  call 0x140349e80
00AE65D2  85 F6                           test esi, esi
00AE65D4  78 39                           js 0x140ae660f
00AE65D6  83 BC 24 D4 00 00 00 00         cmp dword ptr [rsp + 0xd4], 0
00AE65DE  74 0D                           je 0x140ae65ed
00AE65E0  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
00AE65E5  49 8B CF                        mov rcx, r15
00AE65E8  E8 A3 A1 F6 FF                  call 0x140a50790
00AE65ED  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE65F2  F0 81 88 F0 01 00 00 00 00 20 00  lock or dword ptr [rax + 0x1f0], 0x200000
00AE65FD  49 8B CF                        mov rcx, r15
00AE6600  E8 0B 8A 77 FF                  call 0x14025f010
00AE6605  E9 92 F1 FF FF                  jmp 0x140ae579c
00AE660A  BE 0A 01 00 C0                  mov esi, 0xc000010a
00AE660F  49 8B CF                        mov rcx, r15
00AE6612  E8 F9 89 77 FF                  call 0x14025f010
00AE6617  E9 80 F1 FF FF                  jmp 0x140ae579c
00AE661C  E9 A2 39 00 00                  jmp 0x140ae9fc3
00AE6621  83 FF 04                        cmp edi, 4
00AE6624  0F 85 73 39 00 00               jne 0x140ae9f9d
00AE662A  8B 03                           mov eax, dword ptr [rbx]
00AE662C  89 84 24 98 01 00 00            mov dword ptr [rsp + 0x198], eax
00AE6633  41 8B DE                        mov ebx, r14d
00AE6636  85 C0                           test eax, eax
00AE6638  0F 95 C3                        setne bl
00AE663B  4C 8B 05 56 04 4E 00            mov r8, qword ptr [rip + 0x4e0456]
00AE6642  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE6647  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE664C  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE6651  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE6656  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE665E  45 0F B6 CC                     movzx r9d, r12b
00AE6662  BA 00 02 00 00                  mov edx, 0x200
00AE6667  48 8B CE                        mov rcx, rsi
00AE666A  E8 E1 2F D8 FF                  call 0x140869650
00AE666F  8B F0                           mov esi, eax
00AE6671  85 C0                           test eax, eax
00AE6673  0F 88 4A 39 00 00               js 0x140ae9fc3
00AE6679  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE667E  48 81 C1 E8 01 00 00            add rcx, 0x1e8
00AE6685  E8 96 FF 72 FF                  call 0x140216620
00AE668A  84 C0                           test al, al
00AE668C  0F 84 93 F7 FF FF               je 0x140ae5e25
00AE6692  8B D3                           mov edx, ebx
00AE6694  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE6699  E8 16 B2 8D FF                  call 0x1403c18b4
00AE669E  E9 6C F7 FF FF                  jmp 0x140ae5e0f
00AE66A3  E9 1B 39 00 00                  jmp 0x140ae9fc3
00AE66A8  83 FF 04                        cmp edi, 4
00AE66AB  0F 85 EC 38 00 00               jne 0x140ae9f9d
00AE66B1  4C 8B 05 E0 03 4E 00            mov r8, qword ptr [rip + 0x4e03e0]
00AE66B8  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE66BD  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE66C2  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE66C7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE66CC  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE66D4  45 0F B6 CC                     movzx r9d, r12b
00AE66D8  BA 00 02 00 00                  mov edx, 0x200
00AE66DD  48 8B CE                        mov rcx, rsi
00AE66E0  E8 6B 2F D8 FF                  call 0x140869650
00AE66E5  8B F0                           mov esi, eax
00AE66E7  85 C0                           test eax, eax
00AE66E9  0F 88 D4 38 00 00               js 0x140ae9fc3
00AE66EF  8B 03                           mov eax, dword ptr [rbx]
00AE66F1  89 84 24 18 01 00 00            mov dword ptr [rsp + 0x118], eax
00AE66F8  EB 0B                           jmp 0x140ae6705
00AE66FA  8B F0                           mov esi, eax
00AE66FC  33 C0                           xor eax, eax
00AE66FE  89 84 24 18 01 00 00            mov dword ptr [rsp + 0x118], eax
00AE6705  85 F6                           test esi, esi
00AE6707  0F 88 8F F0 FF FF               js 0x140ae579c
00AE670D  A9 FE FF FF FF                  test eax, 0xfffffffe
00AE6712  0F 85 2B F9 FF FF               jne 0x140ae6043
00AE6718  A8 01                           test al, 1
00AE671A  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE671F  74 0D                           je 0x140ae672e
00AE6721  F0 83 A0 F4 01 00 00 FD         lock and dword ptr [rax + 0x1f4], 0xfffffffd
00AE6729  E9 6E F0 FF FF                  jmp 0x140ae579c
00AE672E  F0 83 88 F4 01 00 00 02         lock or dword ptr [rax + 0x1f4], 2
00AE6736  E9 61 F0 FF FF                  jmp 0x140ae579c
00AE673B  83 FF 08                        cmp edi, 8
00AE673E  0F 85 59 38 00 00               jne 0x140ae9f9d
00AE6744  48 8B 3B                        mov rdi, qword ptr [rbx]
00AE6747  48 89 BC 24 08 02 00 00         mov qword ptr [rsp + 0x208], rdi
00AE674F  41 0F B6 D4                     movzx edx, r12b
00AE6753  33 C9                           xor ecx, ecx
00AE6755  E8 56 D3 DC FF                  call 0x1408b3ab0
00AE675A  84 C0                           test al, al
00AE675C  0F 85 CE 35 00 00               jne 0x140ae9d30
00AE6762  4C 8B 05 2F 03 4E 00            mov r8, qword ptr [rip + 0x4e032f]
00AE6769  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE676E  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE6773  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE6778  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE677D  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE6785  45 0F B6 CC                     movzx r9d, r12b
00AE6789  BA 00 02 00 00                  mov edx, 0x200
00AE678E  48 8B CE                        mov rcx, rsi
00AE6791  E8 BA 2E D8 FF                  call 0x140869650
00AE6796  85 C0                           test eax, eax
00AE6798  0F 88 25 38 00 00               js 0x140ae9fc3
00AE679E  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AE67A3  48 8B CB                        mov rcx, rbx
00AE67A6  E8 35 57 96 FF                  call 0x14044bee0
00AE67AB  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00AE67B0  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
00AE67B8  45 0F B6 CC                     movzx r9d, r12b
00AE67BC  4C 8B C7                        mov r8, rdi
00AE67BF  48 8B D3                        mov rdx, rbx
00AE67C2  48 8B C8                        mov rcx, rax
00AE67C5  E8 06 BE FA FF                  call 0x140a925d0
00AE67CA  E9 D8 F9 FF FF                  jmp 0x140ae61a7
00AE67CF  E9 EF 37 00 00                  jmp 0x140ae9fc3
00AE67D4  83 FF 04                        cmp edi, 4
00AE67D7  0F 85 C0 37 00 00               jne 0x140ae9f9d
00AE67DD  8B 1B                           mov ebx, dword ptr [rbx]
00AE67DF  89 9C 24 60 01 00 00            mov dword ptr [rsp + 0x160], ebx
00AE67E6  41 0F B6 D4                     movzx edx, r12b
00AE67EA  48 8B 0D 87 32 4F 00            mov rcx, qword ptr [rip + 0x4f3287]
00AE67F1  E8 2A B6 D8 FF                  call 0x140871e20
00AE67F6  84 C0                           test al, al
00AE67F8  0F 84 10 F1 FF FF               je 0x140ae590e
00AE67FE  4C 8B 05 93 02 4E 00            mov r8, qword ptr [rip + 0x4e0293]
00AE6805  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE680A  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE680F  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE6814  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE6819  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE6821  45 0F B6 CC                     movzx r9d, r12b
00AE6825  BA 04 02 00 00                  mov edx, 0x204
00AE682A  48 8B CE                        mov rcx, rsi
00AE682D  E8 1E 2E D8 FF                  call 0x140869650
00AE6832  85 C0                           test eax, eax
00AE6834  0F 88 89 37 00 00               js 0x140ae9fc3
00AE683A  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE683F  E8 5C CB 73 FF                  call 0x1402233a0
00AE6844  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE6849  3B D8                           cmp ebx, eax
00AE684B  44 0F 45 F6                     cmovne r14d, esi
00AE684F  BA 50 73 51 79                  mov edx, 0x79517350
00AE6854  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE6859  E8 82 10 81 FF                  call 0x1402f78e0
00AE685E  41 8B C6                        mov eax, r14d
00AE6861  E9 5D 37 00 00                  jmp 0x140ae9fc3
00AE6866  E9 58 37 00 00                  jmp 0x140ae9fc3
00AE686B  83 FF 04                        cmp edi, 4
00AE686E  0F 85 29 37 00 00               jne 0x140ae9f9d
00AE6874  8B 1B                           mov ebx, dword ptr [rbx]
00AE6876  89 9C 24 64 01 00 00            mov dword ptr [rsp + 0x164], ebx
00AE687D  41 0F B6 D4                     movzx edx, r12b
00AE6881  48 8B 0D F8 31 4F 00            mov rcx, qword ptr [rip + 0x4f31f8]
00AE6888  E8 93 B5 D8 FF                  call 0x140871e20
00AE688D  84 C0                           test al, al
00AE688F  0F 84 79 F0 FF FF               je 0x140ae590e
00AE6895  4C 8B 05 FC 01 4E 00            mov r8, qword ptr [rip + 0x4e01fc]
00AE689C  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE68A1  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE68A6  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE68AB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE68B0  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE68B8  45 0F B6 CC                     movzx r9d, r12b
00AE68BC  BA 00 02 00 00                  mov edx, 0x200
00AE68C1  48 8B CE                        mov rcx, rsi
00AE68C4  E8 87 2D D8 FF                  call 0x140869650
00AE68C9  85 C0                           test eax, eax
00AE68CB  0F 88 F2 36 00 00               js 0x140ae9fc3
00AE68D1  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE68D6  85 DB                           test ebx, ebx
00AE68D8  74 10                           je 0x140ae68ea
00AE68DA  F0 81 88 F4 01 00 00 00 20 00 00  lock or dword ptr [rax + 0x1f4], 0x2000
00AE68E5  E9 5D EF FF FF                  jmp 0x140ae5847
00AE68EA  F0 81 A0 F4 01 00 00 FF DF FF FF  lock and dword ptr [rax + 0x1f4], 0xffffdfff
00AE68F5  E9 4D EF FF FF                  jmp 0x140ae5847
00AE68FA  E9 C4 36 00 00                  jmp 0x140ae9fc3
00AE68FF  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
00AE6904  45 85 C9                        test r9d, r9d
00AE6907  74 3E                           je 0x140ae6947
00AE6909  8D 47 FC                        lea eax, [rdi - 4]
00AE690C  A9 FB FF FF FF                  test eax, 0xfffffffb
00AE6911  0F 85 86 36 00 00               jne 0x140ae9f9d
00AE6917  8B 0B                           mov ecx, dword ptr [rbx]
00AE6919  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
00AE691D  83 FF 08                        cmp edi, 8
00AE6920  75 09                           jne 0x140ae692b
00AE6922  8B 43 04                        mov eax, dword ptr [rbx + 4]
00AE6925  89 44 24 64                     mov dword ptr [rsp + 0x64], eax
00AE6929  EB 05                           jmp 0x140ae6930
00AE692B  44 89 74 24 64                  mov dword ptr [rsp + 0x64], r14d
00AE6930  85 C9                           test ecx, ecx
00AE6932  74 13                           je 0x140ae6947
00AE6934  F7 C1 F0 FF FF FF               test ecx, 0xfffffff0
00AE693A  0F 85 95 25 00 00               jne 0x140ae8ed5
00AE6940  EB 05                           jmp 0x140ae6947
00AE6942  E9 7C 36 00 00                  jmp 0x140ae9fc3
00AE6947  4C 8B 05 4A 01 4E 00            mov r8, qword ptr [rip + 0x4e014a]
00AE694E  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE6953  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE6958  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE695D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE6962  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE696A  45 0F B6 CC                     movzx r9d, r12b
00AE696E  BA 00 02 00 00                  mov edx, 0x200
00AE6973  48 8B CE                        mov rcx, rsi
00AE6976  E8 D5 2C D8 FF                  call 0x140869650
00AE697B  85 C0                           test eax, eax
00AE697D  0F 88 40 36 00 00               js 0x140ae9fc3
00AE6983  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE6988  85 FF                           test edi, edi
00AE698A  74 0F                           je 0x140ae699b
00AE698C  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00AE6991  E8 22 B2 C9 FF                  call 0x140781bb8
00AE6996  E9 0C F8 FF FF                  jmp 0x140ae61a7
00AE699B  33 D2                           xor edx, edx
00AE699D  E8 16 B2 C9 FF                  call 0x140781bb8
00AE69A2  E9 00 F8 FF FF                  jmp 0x140ae61a7
00AE69A7  8D 47 FC                        lea eax, [rdi - 4]
00AE69AA  A9 FB FF FF FF                  test eax, 0xfffffffb
00AE69AF  0F 85 E8 35 00 00               jne 0x140ae9f9d
00AE69B5  83 FF 04                        cmp edi, 4
00AE69B8  75 13                           jne 0x140ae69cd
00AE69BA  8B 03                           mov eax, dword ptr [rbx]
00AE69BC  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
00AE69C3  45 32 ED                        xor r13b, r13b
00AE69C6  EB 1E                           jmp 0x140ae69e6
00AE69C8  E9 F6 35 00 00                  jmp 0x140ae9fc3
00AE69CD  48 8B 03                        mov rax, qword ptr [rbx]
00AE69D0  48 89 84 24 80 01 00 00         mov qword ptr [rsp + 0x180], rax
00AE69D8  4C 8B E8                        mov r13, rax
00AE69DB  49 C1 ED 20                     shr r13, 0x20
00AE69DF  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
00AE69E6  83 F8 04                        cmp eax, 4
00AE69E9  0F 83 E6 24 00 00               jae 0x140ae8ed5
00AE69EF  83 F8 03                        cmp eax, 3
00AE69F2  72 21                           jb 0x140ae6a15
00AE69F4  45 0F B6 CC                     movzx r9d, r12b
00AE69F8  41 B8 00 02 00 00               mov r8d, 0x200
00AE69FE  48 8B D6                        mov rdx, rsi
00AE6A01  48 8B 0D E0 30 4F 00            mov rcx, qword ptr [rip + 0x4f30e0]
00AE6A08  E8 BF F8 F0 FF                  call 0x1409f62cc
00AE6A0D  84 C0                           test al, al
00AE6A0F  0F 84 F9 EE FF FF               je 0x140ae590e
00AE6A15  4C 8B 05 7C 00 4E 00            mov r8, qword ptr [rip + 0x4e007c]
00AE6A1C  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE6A21  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE6A26  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE6A2B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE6A30  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE6A38  45 0F B6 CC                     movzx r9d, r12b
00AE6A3C  BA 00 02 00 00                  mov edx, 0x200
00AE6A41  48 8B CE                        mov rcx, rsi
00AE6A44  E8 07 2C D8 FF                  call 0x140869650
00AE6A49  8B F0                           mov esi, eax
00AE6A4B  85 C0                           test eax, eax
00AE6A4D  0F 88 70 35 00 00               js 0x140ae9fc3
00AE6A53  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE6A58  48 81 C1 E8 01 00 00            add rcx, 0x1e8
00AE6A5F  E8 BC FB 72 FF                  call 0x140216620
00AE6A64  84 C0                           test al, al
00AE6A66  0F 84 B9 F3 FF FF               je 0x140ae5e25
00AE6A6C  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
00AE6A71  49 8B D7                        mov rdx, r15
00AE6A74  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE6A79  E8 E6 96 97 FF                  call 0x140460164
00AE6A7E  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00AE6A83  41 8B 80 F4 01 00 00            mov eax, dword ptr [r8 + 0x1f4]
00AE6A8A  44 8B 8C 24 B8 00 00 00         mov r9d, dword ptr [rsp + 0xb8]
00AE6A92  41 C1 E1 1B                     shl r9d, 0x1b
00AE6A96  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
00AE6AA0  8B D0                           mov edx, eax
00AE6AA2  8B C8                           mov ecx, eax
00AE6AA4  81 E1 FF FF FF C7               and ecx, 0xc7ffffff
00AE6AAA  41 0B C9                        or ecx, r9d
00AE6AAD  F0 41 0F B1 88 F4 01 00 00      lock cmpxchg dword ptr [r8 + 0x1f4], ecx
00AE6AB6  3B C2                           cmp eax, edx
00AE6AB8  75 E6                           jne 0x140ae6aa0
00AE6ABA  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE6ABF  48 8D 81 70 03 00 00            lea rax, [rcx + 0x370]
00AE6AC6  48 8B 18                        mov rbx, qword ptr [rax]
00AE6AC9  48 3B D8                        cmp rbx, rax
00AE6ACC  74 51                           je 0x140ae6b1f
00AE6ACE  44 8B B4 24 B8 00 00 00         mov r14d, dword ptr [rsp + 0xb8]
00AE6AD6  41 80 FD 01                     cmp r13b, 1
00AE6ADA  75 20                           jne 0x140ae6afc
00AE6ADC  8B 43 28                        mov eax, dword ptr [rbx + 0x28]
00AE6ADF  C1 E8 09                        shr eax, 9
00AE6AE2  83 E0 07                        and eax, 7
00AE6AE5  41 3B C6                        cmp eax, r14d
00AE6AE8  7D 12                           jge 0x140ae6afc
00AE6AEA  45 33 C0                        xor r8d, r8d
00AE6AED  41 8B D6                        mov edx, r14d
00AE6AF0  48 8D 8B 88 FA FF FF            lea rcx, [rbx - 0x578]
00AE6AF7  E8 14 F6 72 FF                  call 0x140216110
00AE6AFC  41 8B D6                        mov edx, r14d
00AE6AFF  48 8D 8B 88 FA FF FF            lea rcx, [rbx - 0x578]
00AE6B06  E8 B1 D4 8D FF                  call 0x1403c3fbc
00AE6B0B  48 8B 1B                        mov rbx, qword ptr [rbx]
00AE6B0E  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE6B13  48 8D 81 70 03 00 00            lea rax, [rcx + 0x370]
00AE6B1A  48 3B D8                        cmp rbx, rax
00AE6B1D  75 B7                           jne 0x140ae6ad6
00AE6B1F  49 8B D7                        mov rdx, r15
00AE6B22  E8 99 96 97 FF                  call 0x1404601c0
00AE6B27  E9 E3 F2 FF FF                  jmp 0x140ae5e0f
00AE6B2C  E9 92 34 00 00                  jmp 0x140ae9fc3
00AE6B31  83 FF 04                        cmp edi, 4
00AE6B34  0F 85 63 34 00 00               jne 0x140ae9f9d
00AE6B3A  48 83 FE FF                     cmp rsi, -1
00AE6B3E  0F 85 91 23 00 00               jne 0x140ae8ed5
00AE6B44  8B 03                           mov eax, dword ptr [rbx]
00AE6B46  89 84 24 1C 01 00 00            mov dword ptr [rsp + 0x11c], eax
00AE6B4D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AE6B56  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00AE6B5D  8B 9C 24 1C 01 00 00            mov ebx, dword ptr [rsp + 0x11c]
00AE6B64  8B D3                           mov edx, ebx
00AE6B66  E8 E9 B3 8D FF                  call 0x1403c1f54
00AE6B6B  8B F8                           mov edi, eax
00AE6B6D  85 C0                           test eax, eax
00AE6B6F  0F 88 30 EF FF FF               js 0x140ae5aa5
00AE6B75  80 E3 03                        and bl, 3
00AE6B78  80 FB 01                        cmp bl, 1
00AE6B7B  0F 85 24 EF FF FF               jne 0x140ae5aa5
00AE6B81  E8 DA 1F 9C FF                  call 0x1404a8b60
00AE6B86  8B C7                           mov eax, edi
00AE6B88  E9 36 34 00 00                  jmp 0x140ae9fc3
00AE6B8D  E9 31 34 00 00                  jmp 0x140ae9fc3
00AE6B92  83 FF 04                        cmp edi, 4
00AE6B95  0F 85 02 34 00 00               jne 0x140ae9f9d
00AE6B9B  8B 1B                           mov ebx, dword ptr [rbx]
00AE6B9D  89 9C 24 20 01 00 00            mov dword ptr [rsp + 0x120], ebx
00AE6BA4  E8 C7 1E 9A FF                  call 0x140488a70
00AE6BA9  3B D8                           cmp ebx, eax
00AE6BAB  0F 87 24 23 00 00               ja 0x140ae8ed5
00AE6BB1  E8 2A C4 73 FF                  call 0x140222fe0
00AE6BB6  3B D8                           cmp ebx, eax
00AE6BB8  0F 82 17 23 00 00               jb 0x140ae8ed5
00AE6BBE  4C 8B 05 D3 FE 4D 00            mov r8, qword ptr [rip + 0x4dfed3]
00AE6BC5  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE6BCA  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE6BCF  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE6BD4  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE6BD9  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE6BE1  45 0F B6 CC                     movzx r9d, r12b
00AE6BE5  BA 00 02 00 00                  mov edx, 0x200
00AE6BEA  48 8B CE                        mov rcx, rsi
00AE6BED  E8 5E 2A D8 FF                  call 0x140869650
00AE6BF2  8B F0                           mov esi, eax
00AE6BF4  85 C0                           test eax, eax
00AE6BF6  0F 88 C7 33 00 00               js 0x140ae9fc3
00AE6BFC  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE6C01  48 81 C1 E8 01 00 00            add rcx, 0x1e8
00AE6C08  E8 13 FA 72 FF                  call 0x140216620
00AE6C0D  84 C0                           test al, al
00AE6C0F  0F 84 10 F2 FF FF               je 0x140ae5e25
00AE6C15  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
00AE6C1A  49 8B D7                        mov rdx, r15
00AE6C1D  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE6C22  E8 3D 95 97 FF                  call 0x140460164
00AE6C27  C1 E3 0C                        shl ebx, 0xc
00AE6C2A  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00AE6C2F  41 8B 80 F0 01 00 00            mov eax, dword ptr [r8 + 0x1f0]
00AE6C36  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
00AE6C40  8B D0                           mov edx, eax
00AE6C42  8B C8                           mov ecx, eax
00AE6C44  81 E1 FF 8F FF FF               and ecx, 0xffff8fff
00AE6C4A  0B CB                           or ecx, ebx
00AE6C4C  F0 41 0F B1 88 F0 01 00 00      lock cmpxchg dword ptr [r8 + 0x1f0], ecx
00AE6C55  3B C2                           cmp eax, edx
00AE6C57  75 E7                           jne 0x140ae6c40
00AE6C59  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE6C5E  48 8D 81 70 03 00 00            lea rax, [rcx + 0x370]
00AE6C65  48 8B 38                        mov rdi, qword ptr [rax]
00AE6C68  48 3B F8                        cmp rdi, rax
00AE6C6B  74 35                           je 0x140ae6ca2
00AE6C6D  8B 9C 24 20 01 00 00            mov ebx, dword ptr [rsp + 0x120]
00AE6C74  0F 1F 40 00                     nop dword ptr [rax]
00AE6C78  0F 1F 84 00 00 00 00 00         nop dword ptr [rax + rax]
00AE6C80  48 8D 8F 88 FA FF FF            lea rcx, [rdi - 0x578]
00AE6C87  8B D3                           mov edx, ebx
00AE6C89  E8 AA D4 8D FF                  call 0x1403c4138
00AE6C8E  48 8B 3F                        mov rdi, qword ptr [rdi]
00AE6C91  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE6C96  48 8D 81 70 03 00 00            lea rax, [rcx + 0x370]
00AE6C9D  48 3B F8                        cmp rdi, rax
00AE6CA0  75 DE                           jne 0x140ae6c80
00AE6CA2  49 8B D7                        mov rdx, r15
00AE6CA5  E8 16 95 97 FF                  call 0x1404601c0
00AE6CAA  E9 60 F1 FF FF                  jmp 0x140ae5e0f
00AE6CAF  E9 0F 33 00 00                  jmp 0x140ae9fc3
00AE6CB4  33 C0                           xor eax, eax
00AE6CB6  0F 11 84 24 70 02 00 00         movups xmmword ptr [rsp + 0x270], xmm0
00AE6CBE  0F 11 84 24 80 02 00 00         movups xmmword ptr [rsp + 0x280], xmm0
00AE6CC6  48 89 84 24 90 02 00 00         mov qword ptr [rsp + 0x290], rax
00AE6CCE  4C 89 B4 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r14
00AE6CD6  4C 89 B4 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], r14
00AE6CDE  48 83 FE FF                     cmp rsi, -1
00AE6CE2  0F 85 ED 21 00 00               jne 0x140ae8ed5
00AE6CE8  41 80 FC 01                     cmp r12b, 1
00AE6CEC  0F 85 02 0B 00 00               jne 0x140ae77f4
00AE6CF2  83 FF 28                        cmp edi, 0x28
00AE6CF5  0F 82 A2 32 00 00               jb 0x140ae9f9d
00AE6CFB  8D 77 F0                        lea esi, [rdi - 0x10]
00AE6CFE  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00AE6D08  48 F7 E6                        mul rsi
00AE6D0B  48 C1 EA 04                     shr rdx, 4
00AE6D0F  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
00AE6D13  48 C1 E1 03                     shl rcx, 3
00AE6D17  48 3B F1                        cmp rsi, rcx
00AE6D1A  0F 85 7D 32 00 00               jne 0x140ae9f9d
00AE6D20  83 FF 28                        cmp edi, 0x28
00AE6D23  0F 85 DD 01 00 00               jne 0x140ae6f06
00AE6D29  48 8D 84 24 70 02 00 00         lea rax, [rsp + 0x270]
00AE6D31  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00AE6D36  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
00AE6D3B  4C 89 8C 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r9
00AE6D43  4C 8B C7                        mov r8, rdi
00AE6D46  48 8B D3                        mov rdx, rbx
00AE6D49  49 8B C9                        mov rcx, r9
00AE6D4C  E8 EF FA BD FF                  call 0x1406c6840
00AE6D51  90                              nop
00AE6D52  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
00AE6D57  49 8D 49 04                     lea rcx, [r9 + 4]
00AE6D5B  48 89 8C 24 90 01 00 00         mov qword ptr [rsp + 0x190], rcx
00AE6D63  83 39 02                        cmp dword ptr [rcx], 2
00AE6D66  0F 83 A6 05 00 00               jae 0x140ae7312
00AE6D6C  41 F7 01 FE FF FF FF            test dword ptr [r9], 0xfffffffe
00AE6D73  0F 85 99 05 00 00               jne 0x140ae7312
00AE6D79  49 8D 49 08                     lea rcx, [r9 + 8]
00AE6D7D  48 89 8C 24 88 01 00 00         mov qword ptr [rsp + 0x188], rcx
00AE6D85  44 8B 01                        mov r8d, dword ptr [rcx]
00AE6D88  41 83 F8 01                     cmp r8d, 1
00AE6D8C  0F 82 80 05 00 00               jb 0x140ae7312
00AE6D92  48 B8 AB AA AA AA AA AA AA AA   movabs rax, 0xaaaaaaaaaaaaaaab
00AE6D9C  48 F7 E6                        mul rsi
00AE6D9F  48 C1 EA 04                     shr rdx, 4
00AE6DA3  49 3B D0                        cmp rdx, r8
00AE6DA6  0F 85 66 05 00 00               jne 0x140ae7312
00AE6DAC  41 8B CE                        mov ecx, r14d
00AE6DAF  89 4C 24 4C                     mov dword ptr [rsp + 0x4c], ecx
00AE6DB3  48 8D 51 01                     lea rdx, [rcx + 1]
00AE6DB7  48 8D 14 51                     lea rdx, [rcx + rdx*2]
00AE6DBB  49 8D 14 D1                     lea rdx, [r9 + rdx*8]
00AE6DBF  90                              nop
00AE6DC0  83 3A 00                        cmp dword ptr [rdx], 0
00AE6DC3  0F 85 42 05 00 00               jne 0x140ae730b
00AE6DC9  FF C1                           inc ecx
00AE6DCB  89 4C 24 4C                     mov dword ptr [rsp + 0x4c], ecx
00AE6DCF  48 83 C2 18                     add rdx, 0x18
00AE6DD3  41 3B C8                        cmp ecx, r8d
00AE6DD6  72 E8                           jb 0x140ae6dc0
00AE6DD8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AE6DE1  4C 8B 80 B8 00 00 00            mov r8, qword ptr [rax + 0xb8]
00AE6DE8  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
00AE6DED  44 89 B4 24 80 00 00 00         mov dword ptr [rsp + 0x80], r14d
00AE6DF5  49 8B C1                        mov rax, r9
00AE6DF8  8B 08                           mov ecx, dword ptr [rax]
00AE6DFA  F6 C1 01                        test cl, 1
00AE6DFD  74 39                           je 0x140ae6e38
00AE6DFF  49 83 B8 10 03 00 00 00         cmp qword ptr [r8 + 0x310], 0
00AE6E07  0F 84 FE 04 00 00               je 0x140ae730b
00AE6E0D  41 0F B7 88 EC 06 00 00         movzx ecx, word ptr [r8 + 0x6ec]
00AE6E15  BA 4C 01 00 00                  mov edx, 0x14c
00AE6E1A  66 3B CA                        cmp cx, dx
00AE6E1D  74 0E                           je 0x140ae6e2d
00AE6E1F  B8 C4 01 00 00                  mov eax, 0x1c4
00AE6E24  66 3B C8                        cmp cx, ax
00AE6E27  0F 85 DE 04 00 00               jne 0x140ae730b
00AE6E2D  C7 84 24 80 00 00 00 01 00 00 00  mov dword ptr [rsp + 0x80], 1
00AE6E38  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
00AE6E3F  83 F0 01                        xor eax, 1
00AE6E42  8B D0                           mov edx, eax
00AE6E44  8D 04 85 04 00 00 00            lea eax, [rax*4 + 4]
00AE6E4B  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
00AE6E52  48 8D 04 95 04 00 00 00         lea rax, [rdx*4 + 4]
00AE6E5A  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
00AE6E62  48 89 9C 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rbx
00AE6E6A  44 89 74 24 4C                  mov dword ptr [rsp + 0x4c], r14d
00AE6E6F  41 8B F6                        mov esi, r14d
00AE6E72  44 89 74 24 58                  mov dword ptr [rsp + 0x58], r14d
00AE6E77  33 D2                           xor edx, edx
00AE6E79  49 8B C8                        mov rcx, r8
00AE6E7C  E8 6F 2E DE FF                  call 0x1408c9cf0
00AE6E81  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
00AE6E89  8B 7C 24 4C                     mov edi, dword ptr [rsp + 0x4c]
00AE6E8D  89 BC 24 24 01 00 00            mov dword ptr [rsp + 0x124], edi
00AE6E94  48 8B D8                        mov rbx, rax
00AE6E97  48 85 C0                        test rax, rax
00AE6E9A  0F 84 4F 04 00 00               je 0x140ae72ef
00AE6EA0  48 8B 84 24 88 01 00 00         mov rax, qword ptr [rsp + 0x188]
00AE6EA8  3B 38                           cmp edi, dword ptr [rax]
00AE6EAA  0F 83 3F 04 00 00               jae 0x140ae72ef
00AE6EB0  F7 43 74 00 04 00 00            test dword ptr [rbx + 0x74], 0x400
00AE6EB7  0F 85 20 04 00 00               jne 0x140ae72dd
00AE6EBD  48 8D 8B 88 05 00 00            lea rcx, [rbx + 0x588]
00AE6EC4  48 89 8C 24 A0 01 00 00         mov qword ptr [rsp + 0x1a0], rcx
00AE6ECC  E8 4F F7 72 FF                  call 0x140216620
00AE6ED1  84 C0                           test al, al
00AE6ED3  0F 84 04 04 00 00               je 0x140ae72dd
00AE6ED9  4C 8B 8B F0 00 00 00            mov r9, qword ptr [rbx + 0xf0]
00AE6EE0  4C 89 8C 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], r9
00AE6EE8  83 BC 24 80 00 00 00 00         cmp dword ptr [rsp + 0x80], 0
00AE6EF0  74 3F                           je 0x140ae6f31
00AE6EF2  49 8D 89 2C 20 00 00            lea rcx, [r9 + 0x202c]
00AE6EF9  48 89 8C 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rcx
00AE6F01  44 8B 21                        mov r12d, dword ptr [rcx]
00AE6F04  EB 3A                           jmp 0x140ae6f40
00AE6F06  41 B8 50 54 6C 73               mov r8d, 0x736c5450
00AE6F0C  48 8B D7                        mov rdx, rdi
00AE6F0F  B9 01 01 00 00                  mov ecx, 0x101
00AE6F14  E8 D7 B1 09 00                  call 0x140b820f0
00AE6F19  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00AE6F1E  48 85 C0                        test rax, rax
00AE6F21  0F 85 0F FE FF FF               jne 0x140ae6d36
00AE6F27  B8 9A 00 00 C0                  mov eax, 0xc000009a
00AE6F2C  E9 92 30 00 00                  jmp 0x140ae9fc3
00AE6F31  49 8D 49 58                     lea rcx, [r9 + 0x58]
00AE6F35  48 89 8C 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rcx
00AE6F3D  4C 8B 21                        mov r12, qword ptr [rcx]
00AE6F40  4C 89 A4 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r12
00AE6F48  4D 85 E4                        test r12, r12
00AE6F4B  0F 84 7B 03 00 00               je 0x140ae72cc
00AE6F51  48 8B 84 24 90 01 00 00         mov rax, qword ptr [rsp + 0x190]
00AE6F59  83 38 01                        cmp dword ptr [rax], 1
00AE6F5C  0F 85 F5 01 00 00               jne 0x140ae7157
00AE6F62  4C 3B E1                        cmp r12, rcx
00AE6F65  0F 84 D2 00 00 00               je 0x140ae703d
00AE6F6B  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
00AE6F70  41 8B 50 0C                     mov edx, dword ptr [r8 + 0xc]
00AE6F74  48 0F AF 94 24 10 01 00 00      imul rdx, qword ptr [rsp + 0x110]
00AE6F7D  48 85 D2                        test rdx, rdx
00AE6F80  74 2D                           je 0x140ae6faf
00AE6F82  8B 8C 24 A0 00 00 00            mov ecx, dword ptr [rsp + 0xa0]
00AE6F89  FF C9                           dec ecx
00AE6F8B  49 85 CC                        test r12, rcx
00AE6F8E  0F 85 59 30 00 00               jne 0x140ae9fed
00AE6F94  4A 8D 04 22                     lea rax, [rdx + r12]
00AE6F98  49 3B C5                        cmp rax, r13
00AE6F9B  77 05                           ja 0x140ae6fa2
00AE6F9D  49 3B C4                        cmp rax, r12
00AE6FA0  73 0D                           jae 0x140ae6faf
00AE6FA2  41 0F B6 45 00                  movzx eax, byte ptr [r13]
00AE6FA7  4C 8B A4 24 C0 00 00 00         mov r12, qword ptr [rsp + 0xc0]
00AE6FAF  8B 44 24 4C                     mov eax, dword ptr [rsp + 0x4c]
00AE6FB3  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
00AE6FBB  48 FF C0                        inc rax
00AE6FBE  48 8D 0C 40                     lea rcx, [rax + rax*2]
00AE6FC2  49 8B C0                        mov rax, r8
00AE6FC5  48 8D 3C C8                     lea rdi, [rax + rcx*8]
00AE6FC9  41 8B 50 0C                     mov edx, dword ptr [r8 + 0xc]
00AE6FCD  48 0F AF 94 24 10 01 00 00      imul rdx, qword ptr [rsp + 0x110]
00AE6FD6  44 8B 84 24 A0 00 00 00         mov r8d, dword ptr [rsp + 0xa0]
00AE6FDE  48 8B 0F                        mov rcx, qword ptr [rdi]
00AE6FE1  E8 DA 21 E0 FF                  call 0x1408e91c0
00AE6FE6  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00AE6FEB  44 8B 40 0C                     mov r8d, dword ptr [rax + 0xc]
00AE6FEF  4C 0F AF 84 24 10 01 00 00      imul r8, qword ptr [rsp + 0x110]
00AE6FF8  49 8B D4                        mov rdx, r12
00AE6FFB  48 8B 0F                        mov rcx, qword ptr [rdi]
00AE6FFE  E8 3D F8 BD FF                  call 0x1406c6840
00AE7003  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
00AE7008  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00AE7010  4C 8B 8C 24 F0 00 00 00         mov r9, qword ptr [rsp + 0xf0]
00AE7018  8B BC 24 24 01 00 00            mov edi, dword ptr [rsp + 0x124]
00AE701F  EB 27                           jmp 0x140ae7048
00AE7021  8B F0                           mov esi, eax
00AE7023  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AE7027  45 33 F6                        xor r14d, r14d
00AE702A  45 8D 7E 08                     lea r15d, [r14 + 8]
00AE702E  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
00AE7038  E9 8F 02 00 00                  jmp 0x140ae72cc
00AE703D  4C 89 B4 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r14
00AE7045  48 8B C7                        mov rax, rdi
00AE7048  48 8D 0C 40                     lea rcx, [rax + rax*2]
00AE704C  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
00AE7054  4C 8D 04 C8                     lea r8, [rax + rcx*8]
00AE7058  4C 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r8
00AE7060  49 8D 50 10                     lea rdx, [r8 + 0x10]
00AE7064  48 89 94 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rdx
00AE706C  8B 02                           mov eax, dword ptr [rdx]
00AE706E  83 C8 01                        or eax, 1
00AE7071  89 02                           mov dword ptr [rdx], eax
00AE7073  8B C7                           mov eax, edi
00AE7075  48 FF C0                        inc rax
00AE7078  48 8D 0C 40                     lea rcx, [rax + rax*2]
00AE707C  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
00AE7084  48 8D 04 C8                     lea rax, [rax + rcx*8]
00AE7088  83 BC 24 80 00 00 00 00         cmp dword ptr [rsp + 0x80], 0
00AE7090  74 12                           je 0x140ae70a4
00AE7092  8B 00                           mov eax, dword ptr [rax]
00AE7094  89 84 24 68 01 00 00            mov dword ptr [rsp + 0x168], eax
00AE709B  41 89 81 2C 20 00 00            mov dword ptr [r9 + 0x202c], eax
00AE70A2  EB 07                           jmp 0x140ae70ab
00AE70A4  48 8B 00                        mov rax, qword ptr [rax]
00AE70A7  49 89 41 58                     mov qword ptr [r9 + 0x58], rax
00AE70AB  EB 27                           jmp 0x140ae70d4
00AE70AD  8B F0                           mov esi, eax
00AE70AF  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AE70B3  45 33 F6                        xor r14d, r14d
00AE70B6  45 8D 7E 08                     lea r15d, [r14 + 8]
00AE70BA  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
00AE70C4  48 8B 94 24 F0 00 00 00         mov rdx, qword ptr [rsp + 0xf0]
00AE70CC  4C 8B 84 24 E0 00 00 00         mov r8, qword ptr [rsp + 0xe0]
00AE70D4  85 F6                           test esi, esi
00AE70D6  78 44                           js 0x140ae711c
00AE70D8  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
00AE70E0  48 8B 88 10 05 00 00            mov rcx, qword ptr [rax + 0x510]
00AE70E7  49 89 48 20                     mov qword ptr [r8 + 0x20], rcx
00AE70EB  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
00AE70F3  49 89 40 18                     mov qword ptr [r8 + 0x18], rax
00AE70F7  83 32 03                        xor dword ptr [rdx], 3
00AE70FA  FF 44 24 4C                     inc dword ptr [rsp + 0x4c]
00AE70FE  EB 17                           jmp 0x140ae7117
00AE7100  8B F0                           mov esi, eax
00AE7102  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AE7106  45 33 F6                        xor r14d, r14d
00AE7109  45 8D 7E 08                     lea r15d, [r14 + 8]
00AE710D  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
00AE7117  E9 B0 01 00 00                  jmp 0x140ae72cc
00AE711C  83 22 FE                        and dword ptr [rdx], 0xfffffffe
00AE711F  EB 15                           jmp 0x140ae7136
00AE7121  45 33 F6                        xor r14d, r14d
00AE7124  45 8D 7E 08                     lea r15d, [r14 + 8]
00AE7128  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
00AE7132  8B 74 24 58                     mov esi, dword ptr [rsp + 0x58]
00AE7136  E9 91 01 00 00                  jmp 0x140ae72cc
00AE713B  8B F0                           mov esi, eax
00AE713D  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AE7141  45 33 F6                        xor r14d, r14d
00AE7144  45 8D 7E 08                     lea r15d, [r14 + 8]
00AE7148  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
00AE7152  E9 75 01 00 00                  jmp 0x140ae72cc
00AE7157  8B 44 24 4C                     mov eax, dword ptr [rsp + 0x4c]
00AE715B  48 8D 0C 40                     lea rcx, [rax + rax*2]
00AE715F  48 8D 14 CD 00 00 00 00         lea rdx, [rcx*8]
00AE7167  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
00AE716F  48 03 C2                        add rax, rdx
00AE7172  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
00AE717A  48 8D 58 10                     lea rbx, [rax + 0x10]
00AE717E  48 89 9C 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rbx
00AE7186  8B 03                           mov eax, dword ptr [rbx]
00AE7188  83 C8 01                        or eax, 1
00AE718B  89 03                           mov dword ptr [rbx], eax
00AE718D  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
00AE7195  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
00AE7198  90                              nop
00AE7199  83 BC 24 80 00 00 00 00         cmp dword ptr [rsp + 0x80], 0
00AE71A1  74 42                           je 0x140ae71e5
00AE71A3  49 8D 04 84                     lea rax, [r12 + rax*4]
00AE71A7  49 3B C5                        cmp rax, r13
00AE71AA  49 0F 43 C5                     cmovae rax, r13
00AE71AE  8B 00                           mov eax, dword ptr [rax]
00AE71B0  8B F8                           mov edi, eax
00AE71B2  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
00AE71BA  48 8B C1                        mov rax, rcx
00AE71BD  44 8B 44 11 18                  mov r8d, dword ptr [rcx + rdx + 0x18]
00AE71C2  44 89 84 24 6C 01 00 00         mov dword ptr [rsp + 0x16c], r8d
00AE71CA  8B 49 0C                        mov ecx, dword ptr [rcx + 0xc]
00AE71CD  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
00AE71D5  48 8D 14 88                     lea rdx, [rax + rcx*4]
00AE71D9  49 3B D5                        cmp rdx, r13
00AE71DC  49 0F 43 D5                     cmovae rdx, r13
00AE71E0  44 89 02                        mov dword ptr [rdx], r8d
00AE71E3  EB 40                           jmp 0x140ae7225
00AE71E5  49 8D 04 C4                     lea rax, [r12 + rax*8]
00AE71E9  49 3B C5                        cmp rax, r13
00AE71EC  49 0F 43 C5                     cmovae rax, r13
00AE71F0  48 8B 38                        mov rdi, qword ptr [rax]
00AE71F3  48 89 BC 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rdi
00AE71FB  8B 49 0C                        mov ecx, dword ptr [rcx + 0xc]
00AE71FE  48 8B 84 24 C0 00 00 00         mov rax, qword ptr [rsp + 0xc0]
00AE7206  48 8D 0C C8                     lea rcx, [rax + rcx*8]
00AE720A  49 3B CD                        cmp rcx, r13
00AE720D  49 0F 43 CD                     cmovae rcx, r13
00AE7211  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
00AE7216  48 83 C0 18                     add rax, 0x18
00AE721A  48 03 D0                        add rdx, rax
00AE721D  4D 8B C7                        mov r8, r15
00AE7220  E8 AB 57 BD FF                  call 0x1406bc9d0
00AE7225  EB 27                           jmp 0x140ae724e
00AE7227  8B F0                           mov esi, eax
00AE7229  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AE722D  45 33 F6                        xor r14d, r14d
00AE7230  45 8D 7E 08                     lea r15d, [r14 + 8]
00AE7234  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
00AE723E  48 8B BC 24 E8 00 00 00         mov rdi, qword ptr [rsp + 0xe8]
00AE7246  48 8B 9C 24 F0 00 00 00         mov rbx, qword ptr [rsp + 0xf0]
00AE724E  85 F6                           test esi, esi
00AE7250  78 2E                           js 0x140ae7280
00AE7252  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
00AE725A  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
00AE725E  83 33 03                        xor dword ptr [rbx], 3
00AE7261  FF 44 24 4C                     inc dword ptr [rsp + 0x4c]
00AE7265  EB 17                           jmp 0x140ae727e
00AE7267  8B F0                           mov esi, eax
00AE7269  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AE726D  45 33 F6                        xor r14d, r14d
00AE7270  45 8D 7E 08                     lea r15d, [r14 + 8]
00AE7274  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
00AE727E  EB 4C                           jmp 0x140ae72cc
00AE7280  83 23 FE                        and dword ptr [rbx], 0xfffffffe
00AE7283  EB 47                           jmp 0x140ae72cc
00AE7285  45 33 F6                        xor r14d, r14d
00AE7288  45 8D 7E 08                     lea r15d, [r14 + 8]
00AE728C  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
00AE7296  8B 74 24 58                     mov esi, dword ptr [rsp + 0x58]
00AE729A  EB 30                           jmp 0x140ae72cc
00AE729C  8B F0                           mov esi, eax
00AE729E  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AE72A2  45 33 F6                        xor r14d, r14d
00AE72A5  45 8D 7E 08                     lea r15d, [r14 + 8]
00AE72A9  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
00AE72B3  EB 17                           jmp 0x140ae72cc
00AE72B5  8B F0                           mov esi, eax
00AE72B7  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AE72BB  45 33 F6                        xor r14d, r14d
00AE72BE  45 8D 7E 08                     lea r15d, [r14 + 8]
00AE72C2  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
00AE72CC  48 8B 8C 24 A0 01 00 00         mov rcx, qword ptr [rsp + 0x1a0]
00AE72D4  E8 A7 2B 86 FF                  call 0x140349e80
00AE72D9  85 F6                           test esi, esi
00AE72DB  78 12                           js 0x140ae72ef
00AE72DD  48 8B 94 24 A8 00 00 00         mov rdx, qword ptr [rsp + 0xa8]
00AE72E5  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE72EA  E9 8D FB FF FF                  jmp 0x140ae6e7c
00AE72EF  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
00AE72F7  48 85 DB                        test rbx, rbx
00AE72FA  74 1F                           je 0x140ae731b
00AE72FC  BA 50 73 45 6E                  mov edx, 0x6e457350
00AE7301  48 8B CB                        mov rcx, rbx
00AE7304  E8 D7 05 81 FF                  call 0x1402f78e0
00AE7309  EB 10                           jmp 0x140ae731b
00AE730B  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE7310  EB 09                           jmp 0x140ae731b
00AE7312  BE 04 00 00 C0                  mov esi, 0xc0000004
00AE7317  EB 02                           jmp 0x140ae731b
00AE7319  8B F0                           mov esi, eax
00AE731B  48 8D 84 24 70 02 00 00         lea rax, [rsp + 0x270]
00AE7323  4C 8B 4C 24 68                  mov r9, qword ptr [rsp + 0x68]
00AE7328  4C 3B C8                        cmp r9, rax
00AE732B  0F 84 7A E4 FF FF               je 0x140ae57ab
00AE7331  33 D2                           xor edx, edx
00AE7333  49 8B C9                        mov rcx, r9
00AE7336  E8 35 B5 09 00                  call 0x140b82870
00AE733B  8B C6                           mov eax, esi
00AE733D  E9 81 2C 00 00                  jmp 0x140ae9fc3
00AE7342  0F 11 84 24 40 02 00 00         movups xmmword ptr [rsp + 0x240], xmm0
00AE734A  0F 11 84 24 50 02 00 00         movups xmmword ptr [rsp + 0x250], xmm0
00AE7352  0F 11 84 24 60 02 00 00         movups xmmword ptr [rsp + 0x260], xmm0
00AE735A  8D 47 F8                        lea eax, [rdi - 8]
00AE735D  A9 F7 FF FF FF                  test eax, 0xfffffff7
00AE7362  0F 85 35 2C 00 00               jne 0x140ae9f9d
00AE7368  83 FF 08                        cmp edi, 8
00AE736B  75 1D                           jne 0x140ae738a
00AE736D  44 89 B4 24 00 01 00 00         mov dword ptr [rsp + 0x100], r14d
00AE7375  44 89 B4 24 04 01 00 00         mov dword ptr [rsp + 0x104], r14d
00AE737D  48 8B 0B                        mov rcx, qword ptr [rbx]
00AE7380  48 89 8C 24 08 01 00 00         mov qword ptr [rsp + 0x108], rcx
00AE7388  EB 15                           jmp 0x140ae739f
00AE738A  0F 10 03                        movups xmm0, xmmword ptr [rbx]
00AE738D  0F 11 84 24 00 01 00 00         movups xmmword ptr [rsp + 0x100], xmm0
00AE7395  66 0F 73 D8 08                  psrldq xmm0, 8
00AE739A  66 48 0F 7E C1                  movq rcx, xmm0
00AE739F  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
00AE73A7  48 C1 E8 20                     shr rax, 0x20
00AE73AB  85 C0                           test eax, eax
00AE73AD  0F 85 22 1B 00 00               jne 0x140ae8ed5
00AE73B3  39 84 24 00 01 00 00            cmp dword ptr [rsp + 0x100], eax
00AE73BA  74 0A                           je 0x140ae73c6
00AE73BC  B8 58 00 00 C0                  mov eax, 0xc0000058
00AE73C1  E9 FD 2B 00 00                  jmp 0x140ae9fc3
00AE73C6  48 8B C1                        mov rax, rcx
00AE73C9  48 C1 E0 10                     shl rax, 0x10
00AE73CD  48 C1 F8 10                     sar rax, 0x10
00AE73D1  48 3B C8                        cmp rcx, rax
00AE73D4  0F 85 FB 1A 00 00               jne 0x140ae8ed5
00AE73DA  4C 8B 05 B7 F6 4D 00            mov r8, qword ptr [rip + 0x4df6b7]
00AE73E1  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE73E6  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE73EB  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE73F0  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE73F5  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE73FD  45 0F B6 CC                     movzx r9d, r12b
00AE7401  BA 00 02 00 00                  mov edx, 0x200
00AE7406  48 8B CE                        mov rcx, rsi
00AE7409  E8 42 22 D8 FF                  call 0x140869650
00AE740E  85 C0                           test eax, eax
00AE7410  0F 88 AD 2B 00 00               js 0x140ae9fc3
00AE7416  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AE741F  48 8B 98 B8 00 00 00            mov rbx, qword ptr [rax + 0xb8]
00AE7426  41 0F B6 D4                     movzx edx, r12b
00AE742A  48 8B 0D 4F 26 4F 00            mov rcx, qword ptr [rip + 0x4f264f]
00AE7431  E8 EA A9 D8 FF                  call 0x140871e20
00AE7436  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE743B  84 C0                           test al, al
00AE743D  75 09                           jne 0x140ae7448
00AE743F  48 3B CB                        cmp rcx, rbx
00AE7442  0F 85 BC E4 FF FF               jne 0x140ae5904
00AE7448  48 81 C1 E8 01 00 00            add rcx, 0x1e8
00AE744F  E8 CC F1 72 FF                  call 0x140216620
00AE7454  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE7459  84 C0                           test al, al
00AE745B  75 14                           jne 0x140ae7471
00AE745D  BA 50 73 51 79                  mov edx, 0x79517350
00AE7462  E8 79 04 81 FF                  call 0x1402f78e0
00AE7467  B8 0A 01 00 C0                  mov eax, 0xc000010a
00AE746C  E9 52 2B 00 00                  jmp 0x140ae9fc3
00AE7471  BA 4C 01 00 00                  mov edx, 0x14c
00AE7476  8D 42 78                        lea eax, [rdx + 0x78]
00AE7479  48 83 B9 10 03 00 00 00         cmp qword ptr [rcx + 0x310], 0
00AE7481  74 19                           je 0x140ae749c
00AE7483  44 0F B7 81 EC 06 00 00         movzx r8d, word ptr [rcx + 0x6ec]
00AE748B  66 44 3B C2                     cmp r8w, dx
00AE748F  74 06                           je 0x140ae7497
00AE7491  66 44 3B C0                     cmp r8w, ax
00AE7495  75 05                           jne 0x140ae749c
00AE7497  41 B1 01                        mov r9b, 1
00AE749A  EB 03                           jmp 0x140ae749f
00AE749C  45 32 C9                        xor r9b, r9b
00AE749F  4C 8B 83 10 03 00 00            mov r8, qword ptr [rbx + 0x310]
00AE74A6  45 84 C9                        test r9b, r9b
00AE74A9  0F 85 DF 00 00 00               jne 0x140ae758e
00AE74AF  4D 85 C0                        test r8, r8
00AE74B2  74 1C                           je 0x140ae74d0
00AE74B4  44 0F B7 83 EC 06 00 00         movzx r8d, word ptr [rbx + 0x6ec]
00AE74BC  66 44 3B C2                     cmp r8w, dx
00AE74C0  0F 84 6E 01 00 00               je 0x140ae7634
00AE74C6  66 44 3B C0                     cmp r8w, ax
00AE74CA  0F 84 64 01 00 00               je 0x140ae7634
00AE74D0  4C 8D 84 24 40 02 00 00         lea r8, [rsp + 0x240]
00AE74D8  33 D2                           xor edx, edx
00AE74DA  E8 41 F3 72 FF                  call 0x140216820
00AE74DF  33 D2                           xor edx, edx
00AE74E1  48 8B BC 24 08 01 00 00         mov rdi, qword ptr [rsp + 0x108]
00AE74E9  48 8B CF                        mov rcx, rdi
00AE74EC  E8 5F 94 FD FF                  call 0x140ac0950
00AE74F1  8B D8                           mov ebx, eax
00AE74F3  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE74F8  85 C0                           test eax, eax
00AE74FA  41 0F 45 F6                     cmovne esi, r14d
00AE74FE  33 D2                           xor edx, edx
00AE7500  48 8D 8C 24 40 02 00 00         lea rcx, [rsp + 0x240]
00AE7508  E8 23 08 73 FF                  call 0x140217d30
00AE750D  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE7512  85 DB                           test ebx, ebx
00AE7514  0F 84 FA E8 FF FF               je 0x140ae5e14
00AE751A  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
00AE751F  49 8B D7                        mov rdx, r15
00AE7522  E8 3D 8C 97 FF                  call 0x140460164
00AE7527  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE752C  48 89 B8 68 01 00 00            mov qword ptr [rax + 0x168], rdi
00AE7533  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00AE7538  49 8D 80 70 03 00 00            lea rax, [r8 + 0x370]
00AE753F  48 8B 08                        mov rcx, qword ptr [rax]
00AE7542  48 3B C8                        cmp rcx, rax
00AE7545  74 37                           je 0x140ae757e
00AE7547  48 85 FF                        test rdi, rdi
00AE754A  74 0B                           je 0x140ae7557
00AE754C  F0 0F BA A9 88 FA FF FF 19      lock bts dword ptr [rcx - 0x578], 0x19
00AE7555  EB 09                           jmp 0x140ae7560
00AE7557  F0 0F BA B1 88 FA FF FF 19      lock btr dword ptr [rcx - 0x578], 0x19
00AE7560  48 8B 09                        mov rcx, qword ptr [rcx]
00AE7563  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00AE7568  49 8D 80 70 03 00 00            lea rax, [r8 + 0x370]
00AE756F  48 3B C8                        cmp rcx, rax
00AE7572  74 0A                           je 0x140ae757e
00AE7574  48 8B BC 24 08 01 00 00         mov rdi, qword ptr [rsp + 0x108]
00AE757C  EB C9                           jmp 0x140ae7547
00AE757E  49 8B D7                        mov rdx, r15
00AE7581  49 8B C8                        mov rcx, r8
00AE7584  E8 37 8C 97 FF                  call 0x1404601c0
00AE7589  E9 81 E8 FF FF                  jmp 0x140ae5e0f
00AE758E  4D 85 C0                        test r8, r8
00AE7591  0F 84 9D 00 00 00               je 0x140ae7634
00AE7597  44 0F B7 83 EC 06 00 00         movzx r8d, word ptr [rbx + 0x6ec]
00AE759F  66 44 3B C2                     cmp r8w, dx
00AE75A3  74 0A                           je 0x140ae75af
00AE75A5  66 44 3B C0                     cmp r8w, ax
00AE75A9  0F 85 85 00 00 00               jne 0x140ae7634
00AE75AF  4C 8D 84 24 40 02 00 00         lea r8, [rsp + 0x240]
00AE75B7  33 D2                           xor edx, edx
00AE75B9  E8 62 F2 72 FF                  call 0x140216820
00AE75BE  41 8B F6                        mov esi, r14d
00AE75C1  E8 EA DF 95 FF                  call 0x1404455b0
00AE75C6  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
00AE75CE  48 3B C8                        cmp rcx, rax
00AE75D1  72 19                           jb 0x140ae75ec
00AE75D3  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE75D8  33 D2                           xor edx, edx
00AE75DA  48 8D 8C 24 40 02 00 00         lea rcx, [rsp + 0x240]
00AE75E2  E8 49 07 73 FF                  call 0x140217d30
00AE75E7  E9 23 E8 FF FF                  jmp 0x140ae5e0f
00AE75EC  BA 01 00 00 00                  mov edx, 1
00AE75F1  E8 5A 93 FD FF                  call 0x140ac0950
00AE75F6  85 C0                           test eax, eax
00AE75F8  74 D9                           je 0x140ae75d3
00AE75FA  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE75FF  48 8B 88 10 03 00 00            mov rcx, qword ptr [rax + 0x310]
00AE7606  48 85 C9                        test rcx, rcx
00AE7609  74 03                           je 0x140ae760e
00AE760B  4C 8B 31                        mov r14, qword ptr [rcx]
00AE760E  8B 84 24 08 01 00 00            mov eax, dword ptr [rsp + 0x108]
00AE7615  41 89 86 98 04 00 00            mov dword ptr [r14 + 0x498], eax
00AE761C  EB 02                           jmp 0x140ae7620
00AE761E  8B F0                           mov esi, eax
00AE7620  33 D2                           xor edx, edx
00AE7622  48 8D 8C 24 40 02 00 00         lea rcx, [rsp + 0x240]
00AE762A  E8 01 07 73 FF                  call 0x140217d30
00AE762F  E9 DB E7 FF FF                  jmp 0x140ae5e0f
00AE7634  BE BB 00 00 C0                  mov esi, 0xc00000bb
00AE7639  48 81 C1 E8 01 00 00            add rcx, 0x1e8
00AE7640  E8 3B 28 86 FF                  call 0x140349e80
00AE7645  E9 52 E1 FF FF                  jmp 0x140ae579c
00AE764A  E9 74 29 00 00                  jmp 0x140ae9fc3
00AE764F  33 C0                           xor eax, eax
00AE7651  0F 11 84 24 B0 01 00 00         movups xmmword ptr [rsp + 0x1b0], xmm0
00AE7659  0F 11 84 24 C0 01 00 00         movups xmmword ptr [rsp + 0x1c0], xmm0
00AE7661  48 89 84 24 D0 01 00 00         mov qword ptr [rsp + 0x1d0], rax
00AE7669  48 83 FE FF                     cmp rsi, -1
00AE766D  0F 85 62 18 00 00               jne 0x140ae8ed5
00AE7673  49 8B F6                        mov rsi, r14
00AE7676  83 FF 28                        cmp edi, 0x28
00AE7679  75 5F                           jne 0x140ae76da
00AE767B  45 84 E4                        test r12b, r12b
00AE767E  74 38                           je 0x140ae76b8
00AE7680  0F 10 03                        movups xmm0, xmmword ptr [rbx]
00AE7683  0F 11 84 24 B0 01 00 00         movups xmmword ptr [rsp + 0x1b0], xmm0
00AE768B  0F 10 4B 10                     movups xmm1, xmmword ptr [rbx + 0x10]
00AE768F  0F 11 8C 24 C0 01 00 00         movups xmmword ptr [rsp + 0x1c0], xmm1
00AE7697  F2 0F 10 43 20                  movsd xmm0, qword ptr [rbx + 0x20]
00AE769C  F2 0F 11 84 24 D0 01 00 00      movsd qword ptr [rsp + 0x1d0], xmm0
00AE76A5  48 8D 73 20                     lea rsi, [rbx + 0x20]
00AE76A9  48 8D 9C 24 B0 01 00 00         lea rbx, [rsp + 0x1b0]
00AE76B1  EB 05                           jmp 0x140ae76b8
00AE76B3  E9 0B 29 00 00                  jmp 0x140ae9fc3
00AE76B8  44 8B 0B                        mov r9d, dword ptr [rbx]
00AE76BB  41 83 F9 40                     cmp r9d, 0x40
00AE76BF  0F 87 10 18 00 00               ja 0x140ae8ed5
00AE76C5  8B 4B 0C                        mov ecx, dword ptr [rbx + 0xc]
00AE76C8  0B 4B 08                        or ecx, dword ptr [rbx + 8]
00AE76CB  0B 4B 04                        or ecx, dword ptr [rbx + 4]
00AE76CE  0F 85 01 18 00 00               jne 0x140ae8ed5
00AE76D4  48 83 C3 10                     add rbx, 0x10
00AE76D8  EB 3B                           jmp 0x140ae7715
00AE76DA  83 FF 18                        cmp edi, 0x18
00AE76DD  0F 85 BA 28 00 00               jne 0x140ae9f9d
00AE76E3  45 8B CE                        mov r9d, r14d
00AE76E6  45 84 E4                        test r12b, r12b
00AE76E9  74 2A                           je 0x140ae7715
00AE76EB  48 8B 03                        mov rax, qword ptr [rbx]
00AE76EE  48 89 84 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], rax
00AE76F6  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00AE76FA  48 89 84 24 C8 01 00 00         mov qword ptr [rsp + 0x1c8], rax
00AE7702  48 8D 73 10                     lea rsi, [rbx + 0x10]
00AE7706  48 8D 9C 24 C0 01 00 00         lea rbx, [rsp + 0x1c0]
00AE770E  EB 05                           jmp 0x140ae7715
00AE7710  E9 AE 28 00 00                  jmp 0x140ae9fc3
00AE7715  48 8B 03                        mov rax, qword ptr [rbx]
00AE7718  48 85 C0                        test rax, rax
00AE771B  0F 84 B4 17 00 00               je 0x140ae8ed5
00AE7721  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00AE7729  4C 89 73 10                     mov qword ptr [rbx + 0x10], r14
00AE772D  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
00AE7732  4C 8D 84 24 88 00 00 00         lea r8, [rsp + 0x88]
00AE773A  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
00AE773E  48 8D 4B 10                     lea rcx, [rbx + 0x10]
00AE7742  E8 E9 B3 D9 FF                  call 0x140882b30
00AE7747  8B C8                           mov ecx, eax
00AE7749  85 C0                           test eax, eax
00AE774B  0F 88 72 28 00 00               js 0x140ae9fc3
00AE7751  45 84 E4                        test r12b, r12b
00AE7754  74 0B                           je 0x140ae7761
00AE7756  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
00AE775A  48 89 06                        mov qword ptr [rsi], rax
00AE775D  EB 02                           jmp 0x140ae7761
00AE775F  8B C8                           mov ecx, eax
00AE7761  8B C1                           mov eax, ecx
00AE7763  E9 5B 28 00 00                  jmp 0x140ae9fc3
00AE7768  48 83 FE FF                     cmp rsi, -1
00AE776C  0F 85 63 17 00 00               jne 0x140ae8ed5
00AE7772  41 80 FC 01                     cmp r12b, 1
00AE7776  75 7C                           jne 0x140ae77f4
00AE7778  83 FF 20                        cmp edi, 0x20
00AE777B  0F 85 1C 28 00 00               jne 0x140ae9f9d
00AE7781  E8 2E AB 9B FF                  call 0x1404a22b4
00AE7786  84 C0                           test al, al
00AE7788  0F 84 29 28 00 00               je 0x140ae9fb7
00AE778E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AE7797  0F BA 60 74 14                  bt dword ptr [rax + 0x74], 0x14
00AE779C  0F 83 15 28 00 00               jae 0x140ae9fb7
00AE77A2  0F 10 03                        movups xmm0, xmmword ptr [rbx]
00AE77A5  0F 11 84 24 30 03 00 00         movups xmmword ptr [rsp + 0x330], xmm0
00AE77AD  0F 10 4B 10                     movups xmm1, xmmword ptr [rbx + 0x10]
00AE77B1  0F 11 8C 24 40 03 00 00         movups xmmword ptr [rsp + 0x340], xmm1
00AE77B9  4C 8D 4B 18                     lea r9, [rbx + 0x18]
00AE77BD  44 8B 84 24 40 03 00 00         mov r8d, dword ptr [rsp + 0x340]
00AE77C5  48 8B 94 24 38 03 00 00         mov rdx, qword ptr [rsp + 0x338]
00AE77CD  48 8B 8C 24 30 03 00 00         mov rcx, qword ptr [rsp + 0x330]
00AE77D5  E8 16 AD D9 FF                  call 0x1408824f0
00AE77DA  E9 E4 27 00 00                  jmp 0x140ae9fc3
00AE77DF  E9 DF 27 00 00                  jmp 0x140ae9fc3
00AE77E4  48 83 FE FF                     cmp rsi, -1
00AE77E8  0F 85 E7 16 00 00               jne 0x140ae8ed5
00AE77EE  41 80 FC 01                     cmp r12b, 1
00AE77F2  74 0A                           je 0x140ae77fe
00AE77F4  B8 01 00 00 C0                  mov eax, 0xc0000001
00AE77F9  E9 C5 27 00 00                  jmp 0x140ae9fc3
00AE77FE  83 FF 08                        cmp edi, 8
00AE7801  0F 85 96 27 00 00               jne 0x140ae9f9d
00AE7807  E8 A8 AA 9B FF                  call 0x1404a22b4
00AE780C  84 C0                           test al, al
00AE780E  0F 84 A3 27 00 00               je 0x140ae9fb7
00AE7814  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AE781D  0F BA 60 74 14                  bt dword ptr [rax + 0x74], 0x14
00AE7822  0F 83 8F 27 00 00               jae 0x140ae9fb7
00AE7828  48 8B 0B                        mov rcx, qword ptr [rbx]
00AE782B  48 89 8C 24 D8 01 00 00         mov qword ptr [rsp + 0x1d8], rcx
00AE7833  E8 68 81 D9 FF                  call 0x14087f9a0
00AE7838  E9 86 27 00 00                  jmp 0x140ae9fc3
00AE783D  E9 81 27 00 00                  jmp 0x140ae9fc3
00AE7842  48 83 FE FF                     cmp rsi, -1
00AE7846  0F 85 89 16 00 00               jne 0x140ae8ed5
00AE784C  83 FF 04                        cmp edi, 4
00AE784F  0F 85 48 27 00 00               jne 0x140ae9f9d
00AE7855  8B 03                           mov eax, dword ptr [rbx]
00AE7857  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00AE785B  A9 FC FF FF FF                  test eax, 0xfffffffc
00AE7860  0F 85 6F 16 00 00               jne 0x140ae8ed5
00AE7866  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00AE786B  49 8B CB                        mov rcx, r11
00AE786E  E8 65 B0 C9 FF                  call 0x1407828d8
00AE7873  E9 4B 27 00 00                  jmp 0x140ae9fc3
00AE7878  E9 46 27 00 00                  jmp 0x140ae9fc3
00AE787D  83 FF 04                        cmp edi, 4
00AE7880  0F 85 17 27 00 00               jne 0x140ae9f9d
00AE7886  8B 1B                           mov ebx, dword ptr [rbx]
00AE7888  89 9C 24 9C 01 00 00            mov dword ptr [rsp + 0x19c], ebx
00AE788F  F7 C3 FE FF FF FF               test ebx, 0xfffffffe
00AE7895  0F 85 3A 16 00 00               jne 0x140ae8ed5
00AE789B  4C 8B 05 F6 F1 4D 00            mov r8, qword ptr [rip + 0x4df1f6]
00AE78A2  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE78A7  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE78AC  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE78B1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE78B6  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE78BE  45 0F B6 CC                     movzx r9d, r12b
00AE78C2  BA 00 02 00 00                  mov edx, 0x200
00AE78C7  48 8B CE                        mov rcx, rsi
00AE78CA  E8 81 1D D8 FF                  call 0x140869650
00AE78CF  85 C0                           test eax, eax
00AE78D1  0F 88 EC 26 00 00               js 0x140ae9fc3
00AE78D7  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE78DC  F6 C3 01                        test bl, 1
00AE78DF  74 10                           je 0x140ae78f1
00AE78E1  F0 81 88 F4 01 00 00 00 00 20 00  lock or dword ptr [rax + 0x1f4], 0x200000
00AE78EC  E9 56 DF FF FF                  jmp 0x140ae5847
00AE78F1  F0 81 A0 F4 01 00 00 FF FF DF FF  lock and dword ptr [rax + 0x1f4], 0xffdfffff
00AE78FC  E9 46 DF FF FF                  jmp 0x140ae5847
00AE7901  E9 BD 26 00 00                  jmp 0x140ae9fc3
00AE7906  83 FF 04                        cmp edi, 4
00AE7909  0F 85 8E 26 00 00               jne 0x140ae9f9d
00AE790F  8B 3B                           mov edi, dword ptr [rbx]
00AE7911  89 BC 24 A8 01 00 00            mov dword ptr [rsp + 0x1a8], edi
00AE7918  4C 8B 05 79 F1 4D 00            mov r8, qword ptr [rip + 0x4df179]
00AE791F  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE7924  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE7929  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE792E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE7933  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE793B  45 0F B6 CC                     movzx r9d, r12b
00AE793F  BA 00 02 00 00                  mov edx, 0x200
00AE7944  48 8B CE                        mov rcx, rsi
00AE7947  E8 04 1D D8 FF                  call 0x140869650
00AE794C  85 C0                           test eax, eax
00AE794E  0F 88 6F 26 00 00               js 0x140ae9fc3
00AE7954  BA 44 66 6C 74                  mov edx, 0x746c6644
00AE7959  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE795E  E8 1D 86 72 FF                  call 0x14020ff80
00AE7963  48 8B D8                        mov rbx, rax
00AE7966  8B D7                           mov edx, edi
00AE7968  48 8B C8                        mov rcx, rax
00AE796B  E8 44 AF FB FF                  call 0x140aa28b4
00AE7970  48 8B CB                        mov rcx, rbx
00AE7973  E8 D8 19 81 FF                  call 0x1402f9350
00AE7978  E9 CA DE FF FF                  jmp 0x140ae5847
00AE797D  E9 41 26 00 00                  jmp 0x140ae9fc3
00AE7982  83 FF 08                        cmp edi, 8
00AE7985  0F 85 12 26 00 00               jne 0x140ae9f9d
00AE798B  48 83 FE FF                     cmp rsi, -1
00AE798F  0F 85 40 15 00 00               jne 0x140ae8ed5
00AE7995  48 8B 13                        mov rdx, qword ptr [rbx]
00AE7998  48 89 94 24 E0 01 00 00         mov qword ptr [rsp + 0x1e0], rdx
00AE79A0  0F B6 C2                        movzx eax, dl
00AE79A3  24 03                           and al, 3
00AE79A5  3C 01                           cmp al, 1
00AE79A7  0F 85 28 15 00 00               jne 0x140ae8ed5
00AE79AD  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AE79B6  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00AE79BD  48 89 91 D8 02 00 00            mov qword ptr [rcx + 0x2d8], rdx
00AE79C4  33 C0                           xor eax, eax
00AE79C6  E9 F8 25 00 00                  jmp 0x140ae9fc3
00AE79CB  E9 F3 25 00 00                  jmp 0x140ae9fc3
00AE79D0  45 32 ED                        xor r13b, r13b
00AE79D3  83 FF 08                        cmp edi, 8
00AE79D6  0F 85 C1 25 00 00               jne 0x140ae9f9d
00AE79DC  48 8B 03                        mov rax, qword ptr [rbx]
00AE79DF  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00AE79E4  48 83 FE FF                     cmp rsi, -1
00AE79E8  74 0B                           je 0x140ae79f5
00AE79EA  83 7C 24 50 02                  cmp dword ptr [rsp + 0x50], 2
00AE79EF  0F 85 E0 14 00 00               jne 0x140ae8ed5
00AE79F5  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AE79FE  4C 8B 88 B8 00 00 00            mov r9, qword ptr [rax + 0xb8]
00AE7A05  4C 89 4C 24 40                  mov qword ptr [rsp + 0x40], r9
00AE7A0A  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
00AE7A0E  FF C8                           dec eax
00AE7A10  83 F8 0F                        cmp eax, 0xf
00AE7A13  0F 87 DC 02 00 00               ja 0x140ae7cf5
00AE7A19  48 98                           cdqe
00AE7A1B  8B 8C 81 84 A1 AE 00            mov ecx, dword ptr [rcx + rax*4 + 0xaea184]
00AE7A22  48 8D 15 D7 85 51 FF            lea rdx, [rip - 0xae7a29]
00AE7A29  48 03 CA                        add rcx, rdx
00AE7A2C  FF E1                           jmp rcx
00AE7A2E  CC                              int3
00AE7A2F  CC                              int3
00AE7A30  CC                              int3
00AE7A31  CC                              int3
00AE7A32  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AE7A37  48 C1 E9 20                     shr rcx, 0x20
00AE7A3B  83 F9 10                        cmp ecx, 0x10
00AE7A3E  72 0A                           jb 0x140ae7a4a
00AE7A40  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE7A45  E9 B0 02 00 00                  jmp 0x140ae7cfa
00AE7A4A  F6 C1 02                        test cl, 2
00AE7A4D  75 0B                           jne 0x140ae7a5a
00AE7A4F  41 8B 81 50 07 00 00            mov eax, dword ptr [r9 + 0x750]
00AE7A56  A8 10                           test al, 0x10
00AE7A58  75 22                           jne 0x140ae7a7c
00AE7A5A  8B D1                           mov edx, ecx
00AE7A5C  83 E2 01                        and edx, 1
00AE7A5F  75 0B                           jne 0x140ae7a6c
00AE7A61  41 8B 81 50 07 00 00            mov eax, dword ptr [r9 + 0x750]
00AE7A68  A8 40                           test al, 0x40
00AE7A6A  74 10                           je 0x140ae7a7c
00AE7A6C  F6 C1 08                        test cl, 8
00AE7A6F  75 1A                           jne 0x140ae7a8b
00AE7A71  41 8B 81 50 07 00 00            mov eax, dword ptr [r9 + 0x750]
00AE7A78  A8 08                           test al, 8
00AE7A7A  74 0A                           je 0x140ae7a86
00AE7A7C  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE7A81  E9 74 02 00 00                  jmp 0x140ae7cfa
00AE7A86  F6 C1 08                        test cl, 8
00AE7A89  74 0F                           je 0x140ae7a9a
00AE7A8B  F6 C1 02                        test cl, 2
00AE7A8E  75 0F                           jne 0x140ae7a9f
00AE7A90  BE 30 00 00 C0                  mov esi, 0xc0000030
00AE7A95  E9 60 02 00 00                  jmp 0x140ae7cfa
00AE7A9A  F6 C1 02                        test cl, 2
00AE7A9D  74 0E                           je 0x140ae7aad
00AE7A9F  F0 41 83 89 50 07 00 00 10      lock or dword ptr [r9 + 0x750], 0x10
00AE7AA8  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE7AAD  85 D2                           test edx, edx
00AE7AAF  74 0E                           je 0x140ae7abf
00AE7AB1  F0 41 83 A1 50 07 00 00 BF      lock and dword ptr [r9 + 0x750], 0xffffffbf
00AE7ABA  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE7ABF  F6 C1 08                        test cl, 8
00AE7AC2  74 0E                           je 0x140ae7ad2
00AE7AC4  F0 41 83 89 50 07 00 00 08      lock or dword ptr [r9 + 0x750], 8
00AE7ACD  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE7AD2  41 8B F6                        mov esi, r14d
00AE7AD5  E9 20 02 00 00                  jmp 0x140ae7cfa
00AE7ADA  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00AE7ADF  48 C1 E8 20                     shr rax, 0x20
00AE7AE3  83 F8 04                        cmp eax, 4
00AE7AE6  72 0A                           jb 0x140ae7af2
00AE7AE8  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE7AED  E9 08 02 00 00                  jmp 0x140ae7cfa
00AE7AF2  8B C8                           mov ecx, eax
00AE7AF4  83 E1 01                        and ecx, 1
00AE7AF7  A8 02                           test al, 2
00AE7AF9  75 12                           jne 0x140ae7b0d
00AE7AFB  85 C9                           test ecx, ecx
00AE7AFD  74 0A                           je 0x140ae7b09
00AE7AFF  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE7B04  E9 F1 01 00 00                  jmp 0x140ae7cfa
00AE7B09  A8 02                           test al, 2
00AE7B0B  74 0E                           je 0x140ae7b1b
00AE7B0D  85 C9                           test ecx, ecx
00AE7B0F  75 0A                           jne 0x140ae7b1b
00AE7B11  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE7B16  E9 DF 01 00 00                  jmp 0x140ae7cfa
00AE7B1B  49 8B C9                        mov rcx, r9
00AE7B1E  E8 4D C0 DA FF                  call 0x140893b70
00AE7B23  48 85 C0                        test rax, rax
00AE7B26  75 0F                           jne 0x140ae7b37
00AE7B28  BE 0A 01 00 C0                  mov esi, 0xc000010a
00AE7B2D  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE7B32  E9 C3 01 00 00                  jmp 0x140ae7cfa
00AE7B37  0F B6 54 24 54                  movzx edx, byte ptr [rsp + 0x54]
00AE7B3C  80 E2 01                        and dl, 1
00AE7B3F  48 8B C8                        mov rcx, rax
00AE7B42  E8 C5 DC F8 FF                  call 0x140a7580c
00AE7B47  0F B6 D8                        movzx ebx, al
00AE7B4A  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE7B4F  48 81 C1 E8 01 00 00            add rcx, 0x1e8
00AE7B56  E8 25 23 86 FF                  call 0x140349e80
00AE7B5B  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE7B60  84 DB                           test bl, bl
00AE7B62  44 0F 44 F6                     cmove r14d, esi
00AE7B66  41 8B F6                        mov esi, r14d
00AE7B69  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE7B6E  E9 87 01 00 00                  jmp 0x140ae7cfa
00AE7B73  8B 4C 24 54                     mov ecx, dword ptr [rsp + 0x54]
00AE7B77  F7 C1 F0 FF FF FF               test ecx, 0xfffffff0
00AE7B7D  74 0A                           je 0x140ae7b89
00AE7B7F  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE7B84  E9 71 01 00 00                  jmp 0x140ae7cfa
00AE7B89  F6 C1 01                        test cl, 1
00AE7B8C  74 0C                           je 0x140ae7b9a
00AE7B8E  F6 C1 02                        test cl, 2
00AE7B91  74 07                           je 0x140ae7b9a
00AE7B93  83 E1 FD                        and ecx, 0xfffffffd
00AE7B96  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
00AE7B9A  F6 C1 04                        test cl, 4
00AE7B9D  74 0C                           je 0x140ae7bab
00AE7B9F  F6 C1 08                        test cl, 8
00AE7BA2  74 07                           je 0x140ae7bab
00AE7BA4  83 E1 F7                        and ecx, 0xfffffff7
00AE7BA7  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
00AE7BAB  44 8B D1                        mov r10d, ecx
00AE7BAE  41 83 E2 01                     and r10d, 1
00AE7BB2  75 17                           jne 0x140ae7bcb
00AE7BB4  41 F7 81 50 07 00 00 00 10 00 00  test dword ptr [r9 + 0x750], 0x1000
00AE7BBF  74 0A                           je 0x140ae7bcb
00AE7BC1  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE7BC6  E9 2F 01 00 00                  jmp 0x140ae7cfa
00AE7BCB  8B D1                           mov edx, ecx
00AE7BCD  C1 EA 02                        shr edx, 2
00AE7BD0  83 E2 01                        and edx, 1
00AE7BD3  75 15                           jne 0x140ae7bea
00AE7BD5  41 8B 81 D8 07 00 00            mov eax, dword ptr [r9 + 0x7d8]
00AE7BDC  A8 02                           test al, 2
00AE7BDE  74 0A                           je 0x140ae7bea
00AE7BE0  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE7BE5  E9 10 01 00 00                  jmp 0x140ae7cfa
00AE7BEA  44 8B C1                        mov r8d, ecx
00AE7BED  41 D1 E8                        shr r8d, 1
00AE7BF0  41 83 E0 01                     and r8d, 1
00AE7BF4  75 1C                           jne 0x140ae7c12
00AE7BF6  45 85 D2                        test r10d, r10d
00AE7BF9  75 17                           jne 0x140ae7c12
00AE7BFB  41 F7 81 50 07 00 00 00 20 00 00  test dword ptr [r9 + 0x750], 0x2000
00AE7C06  74 0A                           je 0x140ae7c12
00AE7C08  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE7C0D  E9 E8 00 00 00                  jmp 0x140ae7cfa
00AE7C12  C1 E9 03                        shr ecx, 3
00AE7C15  83 E1 01                        and ecx, 1
00AE7C18  75 19                           jne 0x140ae7c33
00AE7C1A  85 D2                           test edx, edx
00AE7C1C  75 15                           jne 0x140ae7c33
00AE7C1E  41 8B 81 D8 07 00 00            mov eax, dword ptr [r9 + 0x7d8]
00AE7C25  A8 04                           test al, 4
00AE7C27  74 0A                           je 0x140ae7c33
00AE7C29  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE7C2E  E9 C7 00 00 00                  jmp 0x140ae7cfa
00AE7C33  45 85 D2                        test r10d, r10d
00AE7C36  75 05                           jne 0x140ae7c3d
00AE7C38  45 85 C0                        test r8d, r8d
00AE7C3B  74 12                           je 0x140ae7c4f
00AE7C3D  41 8B 43 78                     mov eax, dword ptr [r11 + 0x78]
00AE7C41  84 C0                           test al, al
00AE7C43  79 0A                           jns 0x140ae7c4f
00AE7C45  BE 89 01 00 C0                  mov esi, 0xc0000189
00AE7C4A  E9 AB 00 00 00                  jmp 0x140ae7cfa
00AE7C4F  41 8B F6                        mov esi, r14d
00AE7C52  45 85 D2                        test r10d, r10d
00AE7C55  74 0E                           je 0x140ae7c65
00AE7C57  F0 41 81 89 50 07 00 00 00 30 00 00  lock or dword ptr [r9 + 0x750], 0x3000
00AE7C63  EB 11                           jmp 0x140ae7c76
00AE7C65  45 85 C0                        test r8d, r8d
00AE7C68  74 11                           je 0x140ae7c7b
00AE7C6A  F0 41 81 89 50 07 00 00 00 20 00 00  lock or dword ptr [r9 + 0x750], 0x2000
00AE7C76  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE7C7B  85 D2                           test edx, edx
00AE7C7D  74 10                           je 0x140ae7c8f
00AE7C7F  F0 41 83 89 D8 07 00 00 06      lock or dword ptr [r9 + 0x7d8], 6
00AE7C88  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE7C8D  EB 6B                           jmp 0x140ae7cfa
00AE7C8F  85 C9                           test ecx, ecx
00AE7C91  74 67                           je 0x140ae7cfa
00AE7C93  F0 41 83 89 D8 07 00 00 04      lock or dword ptr [r9 + 0x7d8], 4
00AE7C9C  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE7CA1  EB 57                           jmp 0x140ae7cfa
00AE7CA3  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
00AE7CA7  F7 C3 F0 FF FF FF               test ebx, 0xfffffff0
00AE7CAD  74 07                           je 0x140ae7cb6
00AE7CAF  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE7CB4  EB 44                           jmp 0x140ae7cfa
00AE7CB6  F6 C3 01                        test bl, 1
00AE7CB9  74 0C                           je 0x140ae7cc7
00AE7CBB  F6 C3 08                        test bl, 8
00AE7CBE  74 07                           je 0x140ae7cc7
00AE7CC0  83 E3 F7                        and ebx, 0xfffffff7
00AE7CC3  89 5C 24 54                     mov dword ptr [rsp + 0x54], ebx
00AE7CC7  8B FB                           mov edi, ebx
00AE7CC9  83 E7 01                        and edi, 1
00AE7CCC  75 11                           jne 0x140ae7cdf
00AE7CCE  F6 C3 02                        test bl, 2
00AE7CD1  75 05                           jne 0x140ae7cd8
00AE7CD3  F6 C3 04                        test bl, 4
00AE7CD6  74 07                           je 0x140ae7cdf
00AE7CD8  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE7CDD  EB 1B                           jmp 0x140ae7cfa
00AE7CDF  BA 02 00 00 00                  mov edx, 2
00AE7CE4  8D 4A 07                        lea ecx, [rdx + 7]
00AE7CE7  E8 90 9E FC FF                  call 0x140ab1b7c
00AE7CEC  85 C0                           test eax, eax
00AE7CEE  74 28                           je 0x140ae7d18
00AE7CF0  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE7CF5  BE BB 00 00 C0                  mov esi, 0xc00000bb
00AE7CFA  41 80 FD 01                     cmp r13b, 1
00AE7CFE  0F 85 A7 DA FF FF               jne 0x140ae57ab
00AE7D04  49 8B C9                        mov rcx, r9
00AE7D07  BA 50 73 51 79                  mov edx, 0x79517350
00AE7D0C  E8 CF FB 80 FF                  call 0x1402f78e0
00AE7D11  8B C6                           mov eax, esi
00AE7D13  E9 AB 22 00 00                  jmp 0x140ae9fc3
00AE7D18  48 83 FE FF                     cmp rsi, -1
00AE7D1C  0F 84 88 01 00 00               je 0x140ae7eaa
00AE7D22  4C 8B 05 6F ED 4D 00            mov r8, qword ptr [rip + 0x4ded6f]
00AE7D29  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE7D2E  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE7D33  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE7D38  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE7D3D  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE7D45  45 0F B6 CC                     movzx r9d, r12b
00AE7D49  BA 00 02 00 00                  mov edx, 0x200
00AE7D4E  48 8B CE                        mov rcx, rsi
00AE7D51  E8 FA 18 D8 FF                  call 0x140869650
00AE7D56  8B F0                           mov esi, eax
00AE7D58  85 C0                           test eax, eax
00AE7D5A  0F 88 CD FD FF FF               js 0x140ae7b2d
00AE7D60  41 B5 01                        mov r13b, 1
00AE7D63  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AE7D6C  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE7D71  4C 3B 88 B8 00 00 00            cmp r9, qword ptr [rax + 0xb8]
00AE7D78  0F 84 26 01 00 00               je 0x140ae7ea4
00AE7D7E  41 8B 81 50 07 00 00            mov eax, dword ptr [r9 + 0x750]
00AE7D85  0F BA E0 08                     bt eax, 8
00AE7D89  0F 83 C7 00 00 00               jae 0x140ae7e56
00AE7D8F  0F 57 C0                        xorps xmm0, xmm0
00AE7D92  0F 11 84 24 30 03 00 00         movups xmmword ptr [rsp + 0x330], xmm0
00AE7D9A  0F 11 84 24 40 03 00 00         movups xmmword ptr [rsp + 0x340], xmm0
00AE7DA2  4C 8D 84 24 30 03 00 00         lea r8, [rsp + 0x330]
00AE7DAA  49 8B D1                        mov rdx, r9
00AE7DAD  33 C9                           xor ecx, ecx
00AE7DAF  E8 DC CE DD FF                  call 0x1408c4c90
00AE7DB4  41 0F B6 D5                     movzx edx, r13b
00AE7DB8  48 8D 8C 24 30 03 00 00         lea rcx, [rsp + 0x330]
00AE7DC0  E8 EB BC DC FF                  call 0x1408b3ab0
00AE7DC5  0F B6 D8                        movzx ebx, al
00AE7DC8  48 8D 8C 24 30 03 00 00         lea rcx, [rsp + 0x330]
00AE7DD0  E8 3B 39 D8 FF                  call 0x14086b710
00AE7DD5  41 0F B6 D4                     movzx edx, r12b
00AE7DD9  33 C9                           xor ecx, ecx
00AE7DDB  E8 D0 BC DC FF                  call 0x1408b3ab0
00AE7DE0  84 C0                           test al, al
00AE7DE2  75 4F                           jne 0x140ae7e33
00AE7DE4  84 DB                           test bl, bl
00AE7DE6  74 4B                           je 0x140ae7e33
00AE7DE8  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE7DED  41 F7 81 50 07 00 00 00 04 00 00  test dword ptr [r9 + 0x750], 0x400
00AE7DF8  74 39                           je 0x140ae7e33
00AE7DFA  44 8B 54 24 54                  mov r10d, dword ptr [rsp + 0x54]
00AE7DFF  BA 00 08 00 00                  mov edx, 0x800
00AE7E04  45 8B C6                        mov r8d, r14d
00AE7E07  B8 00 09 00 00                  mov eax, 0x900
00AE7E0C  85 FF                           test edi, edi
00AE7E0E  44 0F 44 C0                     cmove r8d, eax
00AE7E12  F7 DF                           neg edi
00AE7E14  1B C9                           sbb ecx, ecx
00AE7E16  23 C8                           and ecx, eax
00AE7E18  44 8B D9                        mov r11d, ecx
00AE7E1B  44 0B DA                        or r11d, edx
00AE7E1E  41 F6 C2 08                     test r10b, 8
00AE7E22  44 0F 44 D9                     cmove r11d, ecx
00AE7E26  41 F6 C2 02                     test r10b, 2
00AE7E2A  74 4C                           je 0x140ae7e78
00AE7E2C  41 0F BA EB 09                  bts r11d, 9
00AE7E31  EB 4A                           jmp 0x140ae7e7d
00AE7E33  41 0F B6 D4                     movzx edx, r12b
00AE7E37  48 8B 0D 42 1C 4F 00            mov rcx, qword ptr [rip + 0x4f1c42]
00AE7E3E  E8 DD 9F D8 FF                  call 0x140871e20
00AE7E43  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE7E48  84 C0                           test al, al
00AE7E4A  75 AE                           jne 0x140ae7dfa
00AE7E4C  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE7E51  E9 A4 FE FF FF                  jmp 0x140ae7cfa
00AE7E56  44 8B 54 24 54                  mov r10d, dword ptr [rsp + 0x54]
00AE7E5B  41 F6 C2 08                     test r10b, 8
00AE7E5F  75 9E                           jne 0x140ae7dff
00AE7E61  85 FF                           test edi, edi
00AE7E63  75 9A                           jne 0x140ae7dff
00AE7E65  BA 00 08 00 00                  mov edx, 0x800
00AE7E6A  85 C2                           test edx, eax
00AE7E6C  74 96                           je 0x140ae7e04
00AE7E6E  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE7E73  E9 82 FE FF FF                  jmp 0x140ae7cfa
00AE7E78  41 0F BA E8 09                  bts r8d, 9
00AE7E7D  41 C1 EA 02                     shr r10d, 2
00AE7E81  41 8B D3                        mov edx, r11d
00AE7E84  0F BA EA 0A                     bts edx, 0xa
00AE7E88  41 0F BA E2 00                  bt r10d, 0
00AE7E8D  41 0F 43 D3                     cmovae edx, r11d
00AE7E91  41 8B C0                        mov eax, r8d
00AE7E94  0F BA E8 0A                     bts eax, 0xa
00AE7E98  41 F7 C2 01 00 00 00            test r10d, 1
00AE7E9F  E9 DA 00 00 00                  jmp 0x140ae7f7e
00AE7EA4  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
00AE7EA8  EB 05                           jmp 0x140ae7eaf
00AE7EAA  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE7EAF  85 FF                           test edi, edi
00AE7EB1  75 17                           jne 0x140ae7eca
00AE7EB3  41 F7 81 50 07 00 00 00 01 00 00  test dword ptr [r9 + 0x750], 0x100
00AE7EBE  74 0A                           je 0x140ae7eca
00AE7EC0  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE7EC5  E9 30 FE FF FF                  jmp 0x140ae7cfa
00AE7ECA  44 8B C3                        mov r8d, ebx
00AE7ECD  41 C1 E8 03                     shr r8d, 3
00AE7ED1  41 83 E0 01                     and r8d, 1
00AE7ED5  75 1C                           jne 0x140ae7ef3
00AE7ED7  85 FF                           test edi, edi
00AE7ED9  75 18                           jne 0x140ae7ef3
00AE7EDB  BA 00 08 00 00                  mov edx, 0x800
00AE7EE0  41 85 91 50 07 00 00            test dword ptr [r9 + 0x750], edx
00AE7EE7  74 0F                           je 0x140ae7ef8
00AE7EE9  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE7EEE  E9 07 FE FF FF                  jmp 0x140ae7cfa
00AE7EF3  BA 00 08 00 00                  mov edx, 0x800
00AE7EF8  8B CB                           mov ecx, ebx
00AE7EFA  D1 E9                           shr ecx, 1
00AE7EFC  83 E1 01                        and ecx, 1
00AE7EFF  74 1D                           je 0x140ae7f1e
00AE7F01  41 8B 81 50 07 00 00            mov eax, dword ptr [r9 + 0x750]
00AE7F08  25 00 03 00 00                  and eax, 0x300
00AE7F0D  3D 00 01 00 00                  cmp eax, 0x100
00AE7F12  75 0A                           jne 0x140ae7f1e
00AE7F14  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE7F19  E9 DC FD FF FF                  jmp 0x140ae7cfa
00AE7F1E  C1 EB 02                        shr ebx, 2
00AE7F21  83 E3 01                        and ebx, 1
00AE7F24  74 1D                           je 0x140ae7f43
00AE7F26  41 8B 81 50 07 00 00            mov eax, dword ptr [r9 + 0x750]
00AE7F2D  25 00 05 00 00                  and eax, 0x500
00AE7F32  3D 00 01 00 00                  cmp eax, 0x100
00AE7F37  75 0A                           jne 0x140ae7f43
00AE7F39  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE7F3E  E9 B7 FD FF FF                  jmp 0x140ae7cfa
00AE7F43  85 FF                           test edi, edi
00AE7F45  74 07                           je 0x140ae7f4e
00AE7F47  B8 00 09 00 00                  mov eax, 0x900
00AE7F4C  EB 09                           jmp 0x140ae7f57
00AE7F4E  41 8B C6                        mov eax, r14d
00AE7F51  45 85 C0                        test r8d, r8d
00AE7F54  0F 45 C2                        cmovne eax, edx
00AE7F57  44 8B C1                        mov r8d, ecx
00AE7F5A  41 83 F0 01                     xor r8d, 1
00AE7F5E  41 C1 E0 09                     shl r8d, 9
00AE7F62  8B D0                           mov edx, eax
00AE7F64  0F BA EA 09                     bts edx, 9
00AE7F68  85 C9                           test ecx, ecx
00AE7F6A  0F 44 D0                        cmove edx, eax
00AE7F6D  85 DB                           test ebx, ebx
00AE7F6F  74 04                           je 0x140ae7f75
00AE7F71  0F BA EA 0A                     bts edx, 0xa
00AE7F75  41 8B C0                        mov eax, r8d
00AE7F78  0F BA E8 0A                     bts eax, 0xa
00AE7F7C  85 DB                           test ebx, ebx
00AE7F7E  44 0F 44 C0                     cmove r8d, eax
00AE7F82  49 8D 89 50 07 00 00            lea rcx, [r9 + 0x750]
00AE7F89  E8 EA F3 9A FF                  call 0x140497378
00AE7F8E  41 8B F6                        mov esi, r14d
00AE7F91  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE7F96  E9 5F FD FF FF                  jmp 0x140ae7cfa
00AE7F9B  8B 4C 24 54                     mov ecx, dword ptr [rsp + 0x54]
00AE7F9F  F7 C1 FE FF FF FF               test ecx, 0xfffffffe
00AE7FA5  74 0A                           je 0x140ae7fb1
00AE7FA7  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE7FAC  E9 49 FD FF FF                  jmp 0x140ae7cfa
00AE7FB1  83 E1 01                        and ecx, 1
00AE7FB4  75 15                           jne 0x140ae7fcb
00AE7FB6  41 8B 81 50 07 00 00            mov eax, dword ptr [r9 + 0x750]
00AE7FBD  84 C0                           test al, al
00AE7FBF  79 0A                           jns 0x140ae7fcb
00AE7FC1  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE7FC6  E9 2F FD FF FF                  jmp 0x140ae7cfa
00AE7FCB  41 8B F6                        mov esi, r14d
00AE7FCE  85 C9                           test ecx, ecx
00AE7FD0  0F 84 24 FD FF FF               je 0x140ae7cfa
00AE7FD6  F0 41 81 89 50 07 00 00 80 00 00 00  lock or dword ptr [r9 + 0x750], 0x80
00AE7FE2  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE7FE7  E9 0E FD FF FF                  jmp 0x140ae7cfa
00AE7FEC  8B 4C 24 54                     mov ecx, dword ptr [rsp + 0x54]
00AE7FF0  F6 C1 08                        test cl, 8
00AE7FF3  0F 85 FC FC FF FF               jne 0x140ae7cf5
00AE7FF9  F6 C1 10                        test cl, 0x10
00AE7FFC  0F 85 F3 FC FF FF               jne 0x140ae7cf5
00AE8002  F7 C1 E0 FF FF FF               test ecx, 0xffffffe0
00AE8008  74 0A                           je 0x140ae8014
00AE800A  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE800F  E9 E6 FC FF FF                  jmp 0x140ae7cfa
00AE8014  41 8B 81 50 07 00 00            mov eax, dword ptr [r9 + 0x750]
00AE801B  A8 01                           test al, 1
00AE801D  75 0A                           jne 0x140ae8029
00AE801F  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE8024  E9 D1 FC FF FF                  jmp 0x140ae7cfa
00AE8029  F6 C1 04                        test cl, 4
00AE802C  75 0A                           jne 0x140ae8038
00AE802E  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE8033  E9 C2 FC FF FF                  jmp 0x140ae7cfa
00AE8038  F0 41 83 89 50 07 00 00 04      lock or dword ptr [r9 + 0x750], 4
00AE8041  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE8046  41 8B F6                        mov esi, r14d
00AE8049  E9 AC FC FF FF                  jmp 0x140ae7cfa
00AE804E  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
00AE8052  F7 C3 E0 FF FF FF               test ebx, 0xffffffe0
00AE8058  74 0A                           je 0x140ae8064
00AE805A  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE805F  E9 96 FC FF FF                  jmp 0x140ae7cfa
00AE8064  F6 C3 01                        test bl, 1
00AE8067  74 0D                           je 0x140ae8076
00AE8069  F6 C3 08                        test bl, 8
00AE806C  75 05                           jne 0x140ae8073
00AE806E  F6 C3 10                        test bl, 0x10
00AE8071  74 03                           je 0x140ae8076
00AE8073  83 E3 E7                        and ebx, 0xffffffe7
00AE8076  F6 C3 02                        test bl, 2
00AE8079  74 08                           je 0x140ae8083
00AE807B  F6 C3 10                        test bl, 0x10
00AE807E  74 03                           je 0x140ae8083
00AE8080  83 E3 EF                        and ebx, 0xffffffef
00AE8083  44 8B E3                        mov r12d, ebx
00AE8086  41 C1 EC 03                     shr r12d, 3
00AE808A  41 83 E4 01                     and r12d, 1
00AE808E  74 0F                           je 0x140ae809f
00AE8090  F6 C3 10                        test bl, 0x10
00AE8093  74 0A                           je 0x140ae809f
00AE8095  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE809A  E9 5B FC FF FF                  jmp 0x140ae7cfa
00AE809F  8B FB                           mov edi, ebx
00AE80A1  D1 EF                           shr edi, 1
00AE80A3  83 E7 01                        and edi, 1
00AE80A6  44 8B FB                        mov r15d, ebx
00AE80A9  41 83 E7 01                     and r15d, 1
00AE80AD  42 8D 04 3F                     lea eax, [rdi + r15]
00AE80B1  83 F8 01                        cmp eax, 1
00AE80B4  76 0A                           jbe 0x140ae80c0
00AE80B6  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE80BB  E9 3A FC FF FF                  jmp 0x140ae7cfa
00AE80C0  45 85 FF                        test r15d, r15d
00AE80C3  0F 85 C9 00 00 00               jne 0x140ae8192
00AE80C9  41 0F B6 91 F8 05 00 00         movzx edx, byte ptr [r9 + 0x5f8]
00AE80D1  80 FA 08                        cmp dl, 8
00AE80D4  74 1C                           je 0x140ae80f2
00AE80D6  48 8B 05 A3 CD 41 00            mov rax, qword ptr [rip + 0x41cda3]
00AE80DD  48 85 C0                        test rax, rax
00AE80E0  74 10                           je 0x140ae80f2
00AE80E2  B1 08                           mov cl, 8
00AE80E4  E8 E7 29 BD FF                  call 0x1406baad0
00AE80E9  85 C0                           test eax, eax
00AE80EB  75 40                           jne 0x140ae812d
00AE80ED  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE80F2  41 0F B6 91 F9 05 00 00         movzx edx, byte ptr [r9 + 0x5f9]
00AE80FA  80 FA 08                        cmp dl, 8
00AE80FD  0F 84 79 F9 FF FF               je 0x140ae7a7c
00AE8103  48 8B 05 76 CD 41 00            mov rax, qword ptr [rip + 0x41cd76]
00AE810A  48 85 C0                        test rax, rax
00AE810D  0F 84 69 F9 FF FF               je 0x140ae7a7c
00AE8113  B1 08                           mov cl, 8
00AE8115  E8 B6 29 BD FF                  call 0x1406baad0
00AE811A  85 C0                           test eax, eax
00AE811C  75 0F                           jne 0x140ae812d
00AE811E  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE8123  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE8128  E9 CD FB FF FF                  jmp 0x140ae7cfa
00AE812D  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE8132  45 85 FF                        test r15d, r15d
00AE8135  75 5B                           jne 0x140ae8192
00AE8137  85 FF                           test edi, edi
00AE8139  75 57                           jne 0x140ae8192
00AE813B  41 0F B6 89 F8 05 00 00         movzx ecx, byte ptr [r9 + 0x5f8]
00AE8143  48 8B 05 36 CD 41 00            mov rax, qword ptr [rip + 0x41cd36]
00AE814A  48 85 C0                        test rax, rax
00AE814D  74 43                           je 0x140ae8192
00AE814F  B2 06                           mov dl, 6
00AE8151  E8 7A 29 BD FF                  call 0x1406baad0
00AE8156  85 C0                           test eax, eax
00AE8158  74 33                           je 0x140ae818d
00AE815A  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE815F  41 0F B6 89 F9 05 00 00         movzx ecx, byte ptr [r9 + 0x5f9]
00AE8167  48 8B 05 12 CD 41 00            mov rax, qword ptr [rip + 0x41cd12]
00AE816E  48 85 C0                        test rax, rax
00AE8171  74 1F                           je 0x140ae8192
00AE8173  B2 06                           mov dl, 6
00AE8175  E8 56 29 BD FF                  call 0x1406baad0
00AE817A  85 C0                           test eax, eax
00AE817C  74 0F                           je 0x140ae818d
00AE817E  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE8183  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE8188  E9 6D FB FF FF                  jmp 0x140ae7cfa
00AE818D  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE8192  41 F7 81 50 07 00 00 00 00 00 03  test dword ptr [r9 + 0x750], 0x3000000
00AE819D  74 1D                           je 0x140ae81bc
00AE819F  F6 C3 10                        test bl, 0x10
00AE81A2  75 18                           jne 0x140ae81bc
00AE81A4  85 FF                           test edi, edi
00AE81A6  75 14                           jne 0x140ae81bc
00AE81A8  45 85 E4                        test r12d, r12d
00AE81AB  75 0F                           jne 0x140ae81bc
00AE81AD  45 85 FF                        test r15d, r15d
00AE81B0  75 0A                           jne 0x140ae81bc
00AE81B2  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE81B7  E9 3E FB FF FF                  jmp 0x140ae7cfa
00AE81BC  41 8B F6                        mov esi, r14d
00AE81BF  45 85 FF                        test r15d, r15d
00AE81C2  74 5D                           je 0x140ae8221
00AE81C4  41 0F B6 91 F8 05 00 00         movzx edx, byte ptr [r9 + 0x5f8]
00AE81CC  48 8B 05 AD CC 41 00            mov rax, qword ptr [rip + 0x41ccad]
00AE81D3  48 85 C0                        test rax, rax
00AE81D6  74 1C                           je 0x140ae81f4
00AE81D8  B1 08                           mov cl, 8
00AE81DA  E8 F1 28 BD FF                  call 0x1406baad0
00AE81DF  85 C0                           test eax, eax
00AE81E1  74 0C                           je 0x140ae81ef
00AE81E3  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE81E8  C6 80 F8 05 00 00 08            mov byte ptr [rax + 0x5f8], 8
00AE81EF  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE81F4  41 0F B6 91 F9 05 00 00         movzx edx, byte ptr [r9 + 0x5f9]
00AE81FC  48 8B 05 7D CC 41 00            mov rax, qword ptr [rip + 0x41cc7d]
00AE8203  48 85 C0                        test rax, rax
00AE8206  74 79                           je 0x140ae8281
00AE8208  B1 08                           mov cl, 8
00AE820A  E8 C1 28 BD FF                  call 0x1406baad0
00AE820F  85 C0                           test eax, eax
00AE8211  74 69                           je 0x140ae827c
00AE8213  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE8218  C6 80 F9 05 00 00 08            mov byte ptr [rax + 0x5f9], 8
00AE821F  EB 5B                           jmp 0x140ae827c
00AE8221  85 FF                           test edi, edi
00AE8223  74 5C                           je 0x140ae8281
00AE8225  41 0F B6 89 F8 05 00 00         movzx ecx, byte ptr [r9 + 0x5f8]
00AE822D  48 8B 05 4C CC 41 00            mov rax, qword ptr [rip + 0x41cc4c]
00AE8234  48 85 C0                        test rax, rax
00AE8237  0F 84 3F F8 FF FF               je 0x140ae7a7c
00AE823D  B2 06                           mov dl, 6
00AE823F  E8 8C 28 BD FF                  call 0x1406baad0
00AE8244  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE8249  85 C0                           test eax, eax
00AE824B  0F 84 2B F8 FF FF               je 0x140ae7a7c
00AE8251  41 0F B6 91 F9 05 00 00         movzx edx, byte ptr [r9 + 0x5f9]
00AE8259  48 8B 05 20 CC 41 00            mov rax, qword ptr [rip + 0x41cc20]
00AE8260  48 85 C0                        test rax, rax
00AE8263  74 1C                           je 0x140ae8281
00AE8265  B1 06                           mov cl, 6
00AE8267  E8 64 28 BD FF                  call 0x1406baad0
00AE826C  85 C0                           test eax, eax
00AE826E  74 0C                           je 0x140ae827c
00AE8270  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE8275  C6 80 F9 05 00 00 06            mov byte ptr [rax + 0x5f9], 6
00AE827C  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE8281  41 BB 00 00 80 00               mov r11d, 0x800000
00AE8287  85 DB                           test ebx, ebx
00AE8289  45 0F 45 F3                     cmovne r14d, r11d
00AE828D  45 8B C4                        mov r8d, r12d
00AE8290  41 83 F0 01                     xor r8d, 1
00AE8294  41 C1 E0 18                     shl r8d, 0x18
00AE8298  41 8B D6                        mov edx, r14d
00AE829B  0F BA EA 18                     bts edx, 0x18
00AE829F  45 85 E4                        test r12d, r12d
00AE82A2  41 0F 44 D6                     cmove edx, r14d
00AE82A6  C1 EB 04                        shr ebx, 4
00AE82A9  83 E3 01                        and ebx, 1
00AE82AC  74 04                           je 0x140ae82b2
00AE82AE  0F BA EA 19                     bts edx, 0x19
00AE82B2  41 8B C0                        mov eax, r8d
00AE82B5  0F BA E8 19                     bts eax, 0x19
00AE82B9  85 DB                           test ebx, ebx
00AE82BB  44 0F 44 C0                     cmove r8d, eax
00AE82BF  49 8D 89 50 07 00 00            lea rcx, [r9 + 0x750]
00AE82C6  E8 AD F0 9A FF                  call 0x140497378
00AE82CB  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE82D0  E9 25 FA FF FF                  jmp 0x140ae7cfa
00AE82D5  8B 54 24 54                     mov edx, dword ptr [rsp + 0x54]
00AE82D9  F7 C2 FC FF FF FF               test edx, 0xfffffffc
00AE82DF  74 0A                           je 0x140ae82eb
00AE82E1  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE82E6  E9 0F FA FF FF                  jmp 0x140ae7cfa
00AE82EB  8B CA                           mov ecx, edx
00AE82ED  83 E1 01                        and ecx, 1
00AE82F0  75 17                           jne 0x140ae8309
00AE82F2  41 F7 81 50 07 00 00 00 00 01 00  test dword ptr [r9 + 0x750], 0x10000
00AE82FD  74 0A                           je 0x140ae8309
00AE82FF  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE8304  E9 F1 F9 FF FF                  jmp 0x140ae7cfa
00AE8309  85 C9                           test ecx, ecx
00AE830B  75 1C                           jne 0x140ae8329
00AE830D  F6 C2 02                        test dl, 2
00AE8310  75 17                           jne 0x140ae8329
00AE8312  41 F7 81 50 07 00 00 00 00 02 00  test dword ptr [r9 + 0x750], 0x20000
00AE831D  74 0A                           je 0x140ae8329
00AE831F  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE8324  E9 D1 F9 FF FF                  jmp 0x140ae7cfa
00AE8329  41 8B F6                        mov esi, r14d
00AE832C  85 C9                           test ecx, ecx
00AE832E  74 21                           je 0x140ae8351
00AE8330  49 8D 89 50 07 00 00            lea rcx, [r9 + 0x750]
00AE8337  BA 00 00 01 00                  mov edx, 0x10000
00AE833C  41 B8 00 00 02 00               mov r8d, 0x20000
00AE8342  E8 31 F0 9A FF                  call 0x140497378
00AE8347  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE834C  E9 A9 F9 FF FF                  jmp 0x140ae7cfa
00AE8351  F6 C2 02                        test dl, 2
00AE8354  0F 84 A0 F9 FF FF               je 0x140ae7cfa
00AE835A  49 8D 89 50 07 00 00            lea rcx, [r9 + 0x750]
00AE8361  BA 00 00 02 00                  mov edx, 0x20000
00AE8366  41 B8 00 00 01 00               mov r8d, 0x10000
00AE836C  E8 07 F0 9A FF                  call 0x140497378
00AE8371  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE8376  E9 7F F9 FF FF                  jmp 0x140ae7cfa
00AE837B  8B 4C 24 54                     mov ecx, dword ptr [rsp + 0x54]
00AE837F  F7 C1 E0 FF FF FF               test ecx, 0xffffffe0
00AE8385  74 0A                           je 0x140ae8391
00AE8387  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE838C  E9 69 F9 FF FF                  jmp 0x140ae7cfa
00AE8391  F6 C1 01                        test cl, 1
00AE8394  74 08                           je 0x140ae839e
00AE8396  F6 C1 08                        test cl, 8
00AE8399  74 03                           je 0x140ae839e
00AE839B  83 E1 F7                        and ecx, 0xfffffff7
00AE839E  F6 C1 02                        test cl, 2
00AE83A1  74 08                           je 0x140ae83ab
00AE83A3  F6 C1 10                        test cl, 0x10
00AE83A6  74 03                           je 0x140ae83ab
00AE83A8  83 E1 EF                        and ecx, 0xffffffef
00AE83AB  8B F9                           mov edi, ecx
00AE83AD  83 E7 01                        and edi, 1
00AE83B0  41 B8 00 00 08 00               mov r8d, 0x80000
00AE83B6  75 0D                           jne 0x140ae83c5
00AE83B8  45 85 81 50 07 00 00            test dword ptr [r9 + 0x750], r8d
00AE83BF  0F 85 B7 F6 FF FF               jne 0x140ae7a7c
00AE83C5  8B D1                           mov edx, ecx
00AE83C7  D1 EA                           shr edx, 1
00AE83C9  83 E2 01                        and edx, 1
00AE83CC  75 11                           jne 0x140ae83df
00AE83CE  41 F7 81 50 07 00 00 00 00 20 00  test dword ptr [r9 + 0x750], 0x200000
00AE83D9  0F 85 9D F6 FF FF               jne 0x140ae7a7c
00AE83DF  8B D9                           mov ebx, ecx
00AE83E1  C1 EB 02                        shr ebx, 2
00AE83E4  83 E3 01                        and ebx, 1
00AE83E7  75 17                           jne 0x140ae8400
00AE83E9  41 F7 81 50 07 00 00 00 00 04 00  test dword ptr [r9 + 0x750], 0x40000
00AE83F4  74 0A                           je 0x140ae8400
00AE83F6  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE83FB  E9 FA F8 FF FF                  jmp 0x140ae7cfa
00AE8400  44 8B D9                        mov r11d, ecx
00AE8403  41 C1 EB 03                     shr r11d, 3
00AE8407  41 83 E3 01                     and r11d, 1
00AE840B  75 19                           jne 0x140ae8426
00AE840D  85 FF                           test edi, edi
00AE840F  75 15                           jne 0x140ae8426
00AE8411  41 BA 00 00 10 00               mov r10d, 0x100000
00AE8417  45 85 91 50 07 00 00            test dword ptr [r9 + 0x750], r10d
00AE841E  0F 85 58 F6 FF FF               jne 0x140ae7a7c
00AE8424  EB 06                           jmp 0x140ae842c
00AE8426  41 BA 00 00 10 00               mov r10d, 0x100000
00AE842C  C1 E9 04                        shr ecx, 4
00AE842F  83 E1 01                        and ecx, 1
00AE8432  75 1B                           jne 0x140ae844f
00AE8434  85 D2                           test edx, edx
00AE8436  75 17                           jne 0x140ae844f
00AE8438  41 F7 81 50 07 00 00 00 00 40 00  test dword ptr [r9 + 0x750], 0x400000
00AE8443  74 0A                           je 0x140ae844f
00AE8445  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE844A  E9 AB F8 FF FF                  jmp 0x140ae7cfa
00AE844F  41 8B C6                        mov eax, r14d
00AE8452  85 FF                           test edi, edi
00AE8454  74 05                           je 0x140ae845b
00AE8456  41 8B C2                        mov eax, r10d
00AE8459  EB 0A                           jmp 0x140ae8465
00AE845B  45 8B C6                        mov r8d, r14d
00AE845E  45 85 DB                        test r11d, r11d
00AE8461  45 0F 45 C2                     cmovne r8d, r10d
00AE8465  85 D2                           test edx, edx
00AE8467  74 0B                           je 0x140ae8474
00AE8469  41 0F BA E8 15                  bts r8d, 0x15
00AE846E  0F BA E8 16                     bts eax, 0x16
00AE8472  EB 09                           jmp 0x140ae847d
00AE8474  85 C9                           test ecx, ecx
00AE8476  74 05                           je 0x140ae847d
00AE8478  41 0F BA E8 16                  bts r8d, 0x16
00AE847D  41 8B D0                        mov edx, r8d
00AE8480  0F BA EA 12                     bts edx, 0x12
00AE8484  85 DB                           test ebx, ebx
00AE8486  41 0F 44 D0                     cmove edx, r8d
00AE848A  49 8D 89 50 07 00 00            lea rcx, [r9 + 0x750]
00AE8491  44 8B C0                        mov r8d, eax
00AE8494  E8 DF EE 9A FF                  call 0x140497378
00AE8499  41 8B F6                        mov esi, r14d
00AE849C  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE84A1  E9 54 F8 FF FF                  jmp 0x140ae7cfa
00AE84A6  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
00AE84AA  F7 C3 F8 FF FF FF               test ebx, 0xfffffff8
00AE84B0  74 0A                           je 0x140ae84bc
00AE84B2  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE84B7  E9 3E F8 FF FF                  jmp 0x140ae7cfa
00AE84BC  8B C3                           mov eax, ebx
00AE84BE  83 E0 01                        and eax, 1
00AE84C1  75 0F                           jne 0x140ae84d2
00AE84C3  F6 C3 04                        test bl, 4
00AE84C6  74 0A                           je 0x140ae84d2
00AE84C8  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE84CD  E9 28 F8 FF FF                  jmp 0x140ae7cfa
00AE84D2  85 C0                           test eax, eax
00AE84D4  74 08                           je 0x140ae84de
00AE84D6  F6 C3 02                        test bl, 2
00AE84D9  74 03                           je 0x140ae84de
00AE84DB  83 E3 FD                        and ebx, 0xfffffffd
00AE84DE  49 8B C9                        mov rcx, r9
00AE84E1  E8 D2 ED F2 FF                  call 0x140a172b8
00AE84E6  44 8B C0                        mov r8d, eax
00AE84E9  8B D3                           mov edx, ebx
00AE84EB  83 E2 01                        and edx, 1
00AE84EE  75 17                           jne 0x140ae8507
00AE84F0  8D 48 FF                        lea ecx, [rax - 1]
00AE84F3  83 F9 01                        cmp ecx, 1
00AE84F6  77 0F                           ja 0x140ae8507
00AE84F8  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE84FD  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE8502  E9 F3 F7 FF FF                  jmp 0x140ae7cfa
00AE8507  8B C3                           mov eax, ebx
00AE8509  C1 E8 02                        shr eax, 2
00AE850C  83 E0 01                        and eax, 1
00AE850F  74 15                           je 0x140ae8526
00AE8511  41 83 F8 01                     cmp r8d, 1
00AE8515  75 0F                           jne 0x140ae8526
00AE8517  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE851C  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE8521  E9 D4 F7 FF FF                  jmp 0x140ae7cfa
00AE8526  D1 EB                           shr ebx, 1
00AE8528  83 E3 01                        and ebx, 1
00AE852B  75 19                           jne 0x140ae8546
00AE852D  85 D2                           test edx, edx
00AE852F  75 19                           jne 0x140ae854a
00AE8531  41 83 F8 03                     cmp r8d, 3
00AE8535  75 0F                           jne 0x140ae8546
00AE8537  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE853C  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE8541  E9 B4 F7 FF FF                  jmp 0x140ae7cfa
00AE8546  85 D2                           test edx, edx
00AE8548  74 37                           je 0x140ae8581
00AE854A  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE854F  85 C0                           test eax, eax
00AE8551  74 17                           je 0x140ae856a
00AE8553  BA 02 00 00 00                  mov edx, 2
00AE8558  E8 83 96 FC FF                  call 0x140ab1be0
00AE855D  41 8B F6                        mov esi, r14d
00AE8560  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE8565  E9 90 F7 FF FF                  jmp 0x140ae7cfa
00AE856A  BA 01 00 00 00                  mov edx, 1
00AE856F  E8 6C 96 FC FF                  call 0x140ab1be0
00AE8574  41 8B F6                        mov esi, r14d
00AE8577  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE857C  E9 79 F7 FF FF                  jmp 0x140ae7cfa
00AE8581  85 DB                           test ebx, ebx
00AE8583  74 0F                           je 0x140ae8594
00AE8585  BA 03 00 00 00                  mov edx, 3
00AE858A  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE858F  E8 4C 96 FC FF                  call 0x140ab1be0
00AE8594  41 8B F6                        mov esi, r14d
00AE8597  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE859C  E9 59 F7 FF FF                  jmp 0x140ae7cfa
00AE85A1  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
00AE85A5  F7 C3 FC FF FF FF               test ebx, 0xfffffffc
00AE85AB  74 0A                           je 0x140ae85b7
00AE85AD  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE85B2  E9 43 F7 FF FF                  jmp 0x140ae7cfa
00AE85B7  F6 C3 01                        test bl, 1
00AE85BA  74 08                           je 0x140ae85c4
00AE85BC  F6 C3 02                        test bl, 2
00AE85BF  74 03                           je 0x140ae85c4
00AE85C1  83 E3 FD                        and ebx, 0xfffffffd
00AE85C4  49 8B C9                        mov rcx, r9
00AE85C7  E8 DC E3 F8 FF                  call 0x140a769a8
00AE85CC  8B CB                           mov ecx, ebx
00AE85CE  83 E1 01                        and ecx, 1
00AE85D1  75 14                           jne 0x140ae85e7
00AE85D3  83 F8 01                        cmp eax, 1
00AE85D6  75 0F                           jne 0x140ae85e7
00AE85D8  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE85DD  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE85E2  E9 13 F7 FF FF                  jmp 0x140ae7cfa
00AE85E7  D1 EB                           shr ebx, 1
00AE85E9  83 E3 01                        and ebx, 1
00AE85EC  75 18                           jne 0x140ae8606
00AE85EE  85 C9                           test ecx, ecx
00AE85F0  75 18                           jne 0x140ae860a
00AE85F2  83 F8 02                        cmp eax, 2
00AE85F5  75 0F                           jne 0x140ae8606
00AE85F7  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE85FC  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE8601  E9 F4 F6 FF FF                  jmp 0x140ae7cfa
00AE8606  85 C9                           test ecx, ecx
00AE8608  74 07                           je 0x140ae8611
00AE860A  BA 01 00 00 00                  mov edx, 1
00AE860F  EB 0D                           jmp 0x140ae861e
00AE8611  85 DB                           test ebx, ebx
00AE8613  0F 84 7B FF FF FF               je 0x140ae8594
00AE8619  BA 02 00 00 00                  mov edx, 2
00AE861E  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE8623  E8 AC 3C F9 FF                  call 0x140a7c2d4
00AE8628  41 8B F6                        mov esi, r14d
00AE862B  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE8630  E9 C5 F6 FF FF                  jmp 0x140ae7cfa
00AE8635  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
00AE8639  F7 C3 E0 FF FF FF               test ebx, 0xffffffe0
00AE863F  74 0A                           je 0x140ae864b
00AE8641  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE8646  E9 AF F6 FF FF                  jmp 0x140ae7cfa
00AE864B  8B F3                           mov esi, ebx
00AE864D  83 E6 01                        and esi, 1
00AE8650  75 11                           jne 0x140ae8663
00AE8652  41 F7 81 50 07 00 00 00 00 00 40  test dword ptr [r9 + 0x750], 0x40000000
00AE865D  0F 85 19 F4 FF FF               jne 0x140ae7a7c
00AE8663  8B FB                           mov edi, ebx
00AE8665  D1 EF                           shr edi, 1
00AE8667  83 E7 01                        and edi, 1
00AE866A  75 0D                           jne 0x140ae8679
00AE866C  41 39 B9 50 07 00 00            cmp dword ptr [r9 + 0x750], edi
00AE8673  0F 8C 03 F4 FF FF               jl 0x140ae7a7c
00AE8679  F6 C3 08                        test bl, 8
00AE867C  75 11                           jne 0x140ae868f
00AE867E  41 F7 81 54 07 00 00 00 20 00 00  test dword ptr [r9 + 0x754], 0x2000
00AE8689  0F 85 ED F3 FF FF               jne 0x140ae7a7c
00AE868F  F6 C3 04                        test bl, 4
00AE8692  75 11                           jne 0x140ae86a5
00AE8694  41 F7 81 54 07 00 00 00 10 00 00  test dword ptr [r9 + 0x754], 0x1000
00AE869F  0F 85 D7 F3 FF FF               jne 0x140ae7a7c
00AE86A5  8B CB                           mov ecx, ebx
00AE86A7  C1 E9 04                        shr ecx, 4
00AE86AA  83 E1 01                        and ecx, 1
00AE86AD  75 15                           jne 0x140ae86c4
00AE86AF  41 8B 81 D8 07 00 00            mov eax, dword ptr [r9 + 0x7d8]
00AE86B6  A8 01                           test al, 1
00AE86B8  74 0A                           je 0x140ae86c4
00AE86BA  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE86BF  E9 36 F6 FF FF                  jmp 0x140ae7cfa
00AE86C4  85 C9                           test ecx, ecx
00AE86C6  74 18                           je 0x140ae86e0
00AE86C8  E8 BB EC 9B FF                  call 0x1404a7388
00AE86CD  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE86D2  84 C0                           test al, al
00AE86D4  0F 84 1B F6 FF FF               je 0x140ae7cf5
00AE86DA  41 B8 01 00 00 00               mov r8d, 1
00AE86E0  85 F6                           test esi, esi
00AE86E2  74 15                           je 0x140ae86f9
00AE86E4  F0 41 81 89 50 07 00 00 00 00 00 40  lock or dword ptr [r9 + 0x750], 0x40000000
00AE86F0  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE86F5  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
00AE86F9  85 FF                           test edi, edi
00AE86FB  74 58                           je 0x140ae8755
00AE86FD  F0 41 81 89 50 07 00 00 00 00 00 80  lock or dword ptr [r9 + 0x750], 0x80000000
00AE8709  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE870E  F0 81 88 FC 05 00 00 00 00 20 00  lock or dword ptr [rax + 0x5fc], 0x200000
00AE8719  F0 4C 0F C1 05 6E 3E 32 00      lock xadd qword ptr [rip + 0x323e6e], r8
00AE8722  49 FF C0                        inc r8
00AE8725  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE872A  4C 89 80 60 07 00 00            mov qword ptr [rax + 0x760], r8
00AE8731  4C 89 80 68 07 00 00            mov qword ptr [rax + 0x768], r8
00AE8738  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE873D  E8 9E 88 9C FF                  call 0x1404b0fe0
00AE8742  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE8747  E8 50 C0 8D FF                  call 0x1403c479c
00AE874C  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE8751  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
00AE8755  F6 C3 04                        test bl, 4
00AE8758  74 15                           je 0x140ae876f
00AE875A  F0 41 81 89 54 07 00 00 00 10 00 00  lock or dword ptr [r9 + 0x754], 0x1000
00AE8766  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE876B  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
00AE876F  F6 C3 08                        test bl, 8
00AE8772  74 15                           je 0x140ae8789
00AE8774  F0 41 81 89 54 07 00 00 00 20 00 00  lock or dword ptr [r9 + 0x754], 0x2000
00AE8780  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE8785  8B 5C 24 54                     mov ebx, dword ptr [rsp + 0x54]
00AE8789  F6 C3 10                        test bl, 0x10
00AE878C  0F 84 40 F3 FF FF               je 0x140ae7ad2
00AE8792  49 8B C9                        mov rcx, r9
00AE8795  E8 AE B6 C9 FF                  call 0x140783e48
00AE879A  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE879F  41 8B F6                        mov esi, r14d
00AE87A2  E9 53 F5 FF FF                  jmp 0x140ae7cfa
00AE87A7  8B 4C 24 54                     mov ecx, dword ptr [rsp + 0x54]
00AE87AB  F7 C1 00 FC FF FF               test ecx, 0xfffffc00
00AE87B1  74 0A                           je 0x140ae87bd
00AE87B3  BE 0D 00 00 C0                  mov esi, 0xc000000d
00AE87B8  E9 3D F5 FF FF                  jmp 0x140ae7cfa
00AE87BD  F6 C1 10                        test cl, 0x10
00AE87C0  74 07                           je 0x140ae87c9
00AE87C2  83 C9 01                        or ecx, 1
00AE87C5  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
00AE87C9  0F BA E1 09                     bt ecx, 9
00AE87CD  73 07                           jae 0x140ae87d6
00AE87CF  83 C9 04                        or ecx, 4
00AE87D2  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
00AE87D6  F6 C1 40                        test cl, 0x40
00AE87D9  74 07                           je 0x140ae87e2
00AE87DB  83 C9 20                        or ecx, 0x20
00AE87DE  89 4C 24 54                     mov dword ptr [rsp + 0x54], ecx
00AE87E2  44 8B C1                        mov r8d, ecx
00AE87E5  41 C1 E8 04                     shr r8d, 4
00AE87E9  41 83 E0 01                     and r8d, 1
00AE87ED  41 BA 00 00 10 00               mov r10d, 0x100000
00AE87F3  75 0D                           jne 0x140ae8802
00AE87F5  45 85 91 54 07 00 00            test dword ptr [r9 + 0x754], r10d
00AE87FC  0F 85 7A F2 FF FF               jne 0x140ae7a7c
00AE8802  8B D1                           mov edx, ecx
00AE8804  83 E2 01                        and edx, 1
00AE8807  75 11                           jne 0x140ae881a
00AE8809  41 F7 81 54 07 00 00 00 40 00 00  test dword ptr [r9 + 0x754], 0x4000
00AE8814  0F 85 62 F2 FF FF               jne 0x140ae7a7c
00AE881A  85 D2                           test edx, edx
00AE881C  74 17                           je 0x140ae8835
00AE881E  41 F7 81 54 07 00 00 00 40 00 00  test dword ptr [r9 + 0x754], 0x4000
00AE8829  75 0A                           jne 0x140ae8835
00AE882B  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE8830  E9 C5 F4 FF FF                  jmp 0x140ae7cfa
00AE8835  8B D9                           mov ebx, ecx
00AE8837  C1 EB 09                        shr ebx, 9
00AE883A  83 E3 01                        and ebx, 1
00AE883D  74 0E                           je 0x140ae884d
00AE883F  41 83 B9 54 07 00 00 00         cmp dword ptr [r9 + 0x754], 0
00AE8847  0F 8D 2F F2 FF FF               jge 0x140ae7a7c
00AE884D  8B D1                           mov edx, ecx
00AE884F  C1 EA 02                        shr edx, 2
00AE8852  83 E2 01                        and edx, 1
00AE8855  75 11                           jne 0x140ae8868
00AE8857  41 F7 81 54 07 00 00 00 00 02 00  test dword ptr [r9 + 0x754], 0x20000
00AE8862  0F 85 14 F2 FF FF               jne 0x140ae7a7c
00AE8868  85 D2                           test edx, edx
00AE886A  74 17                           je 0x140ae8883
00AE886C  41 F7 81 54 07 00 00 00 00 02 00  test dword ptr [r9 + 0x754], 0x20000
00AE8877  75 0A                           jne 0x140ae8883
00AE8879  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE887E  E9 77 F4 FF FF                  jmp 0x140ae7cfa
00AE8883  8B F9                           mov edi, ecx
00AE8885  C1 EF 06                        shr edi, 6
00AE8888  83 E7 01                        and edi, 1
00AE888B  75 11                           jne 0x140ae889e
00AE888D  41 F7 81 54 07 00 00 00 00 40 00  test dword ptr [r9 + 0x754], 0x400000
00AE8898  0F 85 DE F1 FF FF               jne 0x140ae7a7c
00AE889E  8B F1                           mov esi, ecx
00AE88A0  C1 EE 05                        shr esi, 5
00AE88A3  83 E6 01                        and esi, 1
00AE88A6  75 17                           jne 0x140ae88bf
00AE88A8  41 F7 81 54 07 00 00 00 00 20 00  test dword ptr [r9 + 0x754], 0x200000
00AE88B3  74 0A                           je 0x140ae88bf
00AE88B5  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE88BA  E9 3B F4 FF FF                  jmp 0x140ae7cfa
00AE88BF  44 8B F9                        mov r15d, ecx
00AE88C2  41 C1 EF 08                     shr r15d, 8
00AE88C6  41 83 E7 01                     and r15d, 1
00AE88CA  75 17                           jne 0x140ae88e3
00AE88CC  41 F7 81 54 07 00 00 00 00 00 40  test dword ptr [r9 + 0x754], 0x40000000
00AE88D7  74 0A                           je 0x140ae88e3
00AE88D9  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE88DE  E9 17 F4 FF FF                  jmp 0x140ae7cfa
00AE88E3  44 8B E1                        mov r12d, ecx
00AE88E6  41 D1 EC                        shr r12d, 1
00AE88E9  41 83 E4 01                     and r12d, 1
00AE88ED  74 11                           je 0x140ae8900
00AE88EF  41 F7 81 54 07 00 00 00 80 00 00  test dword ptr [r9 + 0x754], 0x8000
00AE88FA  0F 84 7C F1 FF FF               je 0x140ae7a7c
00AE8900  44 8B D9                        mov r11d, ecx
00AE8903  41 C1 EB 03                     shr r11d, 3
00AE8907  41 83 E3 01                     and r11d, 1
00AE890B  75 11                           jne 0x140ae891e
00AE890D  41 F7 81 54 07 00 00 00 00 04 00  test dword ptr [r9 + 0x754], 0x40000
00AE8918  0F 85 5E F1 FF FF               jne 0x140ae7a7c
00AE891E  45 85 DB                        test r11d, r11d
00AE8921  74 11                           je 0x140ae8934
00AE8923  41 F7 81 54 07 00 00 00 00 04 00  test dword ptr [r9 + 0x754], 0x40000
00AE892E  0F 84 48 F1 FF FF               je 0x140ae7a7c
00AE8934  C1 E9 07                        shr ecx, 7
00AE8937  83 E1 01                        and ecx, 1
00AE893A  41 BB 00 00 80 00               mov r11d, 0x800000
00AE8940  75 0D                           jne 0x140ae894f
00AE8942  45 85 99 54 07 00 00            test dword ptr [r9 + 0x754], r11d
00AE8949  0F 85 2D F1 FF FF               jne 0x140ae7a7c
00AE894F  85 C9                           test ecx, ecx
00AE8951  74 13                           je 0x140ae8966
00AE8953  45 85 99 54 07 00 00            test dword ptr [r9 + 0x754], r11d
00AE895A  75 0A                           jne 0x140ae8966
00AE895C  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE8961  E9 94 F3 FF FF                  jmp 0x140ae7cfa
00AE8966  45 85 C0                        test r8d, r8d
00AE8969  74 0D                           je 0x140ae8978
00AE896B  F0 45 09 91 54 07 00 00         lock or dword ptr [r9 + 0x754], r10d
00AE8973  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE8978  85 DB                           test ebx, ebx
00AE897A  75 15                           jne 0x140ae8991
00AE897C  85 D2                           test edx, edx
00AE897E  74 11                           je 0x140ae8991
00AE8980  F0 41 81 A1 54 07 00 00 FF FF FF 7F  lock and dword ptr [r9 + 0x754], 0x7fffffff
00AE898C  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE8991  85 FF                           test edi, edi
00AE8993  74 1E                           je 0x140ae89b3
00AE8995  F0 41 81 89 54 07 00 00 00 00 20 00  lock or dword ptr [r9 + 0x754], 0x200000
00AE89A1  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE89A6  F0 81 88 54 07 00 00 00 00 40 00  lock or dword ptr [rax + 0x754], 0x400000
00AE89B1  EB 10                           jmp 0x140ae89c3
00AE89B3  85 F6                           test esi, esi
00AE89B5  74 11                           je 0x140ae89c8
00AE89B7  F0 41 81 89 54 07 00 00 00 00 20 00  lock or dword ptr [r9 + 0x754], 0x200000
00AE89C3  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE89C8  45 85 FF                        test r15d, r15d
00AE89CB  74 11                           je 0x140ae89de
00AE89CD  F0 41 81 89 54 07 00 00 00 00 00 40  lock or dword ptr [r9 + 0x754], 0x40000000
00AE89D9  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE89DE  45 85 E4                        test r12d, r12d
00AE89E1  75 11                           jne 0x140ae89f4
00AE89E3  F0 41 81 A1 54 07 00 00 FF 7F FF FF  lock and dword ptr [r9 + 0x754], 0xffff7fff
00AE89EF  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE89F4  41 8B F6                        mov esi, r14d
00AE89F7  E9 FE F2 FF FF                  jmp 0x140ae7cfa
00AE89FC  E9 C2 15 00 00                  jmp 0x140ae9fc3
00AE8A01  48 83 FE FF                     cmp rsi, -1
00AE8A05  0F 85 CA 04 00 00               jne 0x140ae8ed5
00AE8A0B  83 FF 10                        cmp edi, 0x10
00AE8A0E  0F 85 89 15 00 00               jne 0x140ae9f9d
00AE8A14  0F 10 03                        movups xmm0, xmmword ptr [rbx]
00AE8A17  0F 11 84 24 30 03 00 00         movups xmmword ptr [rsp + 0x330], xmm0
00AE8A1F  48 8B 8C 24 30 03 00 00         mov rcx, qword ptr [rsp + 0x330]
00AE8A27  80 BC 24 38 03 00 00 00         cmp byte ptr [rsp + 0x338], 0
00AE8A2F  75 0A                           jne 0x140ae8a3b
00AE8A31  E8 8E 89 96 FF                  call 0x1404513c4
00AE8A36  E9 88 15 00 00                  jmp 0x140ae9fc3
00AE8A3B  E8 D4 DA 97 FF                  call 0x140466514
00AE8A40  E9 7E 15 00 00                  jmp 0x140ae9fc3
00AE8A45  E9 79 15 00 00                  jmp 0x140ae9fc3
00AE8A4A  83 FF 04                        cmp edi, 4
00AE8A4D  0F 85 4A 15 00 00               jne 0x140ae9f9d
00AE8A53  8B 1B                           mov ebx, dword ptr [rbx]
00AE8A55  89 9C 24 AC 01 00 00            mov dword ptr [rsp + 0x1ac], ebx
00AE8A5C  F7 C3 FE FF FF FF               test ebx, 0xfffffffe
00AE8A62  0F 85 6D 04 00 00               jne 0x140ae8ed5
00AE8A68  4C 8B 05 29 E0 4D 00            mov r8, qword ptr [rip + 0x4de029]
00AE8A6F  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE8A74  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE8A79  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE8A7E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE8A83  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE8A8B  45 0F B6 CC                     movzx r9d, r12b
00AE8A8F  BA 00 02 00 00                  mov edx, 0x200
00AE8A94  48 8B CE                        mov rcx, rsi
00AE8A97  E8 B4 0B D8 FF                  call 0x140869650
00AE8A9C  85 C0                           test eax, eax
00AE8A9E  0F 88 1F 15 00 00               js 0x140ae9fc3
00AE8AA4  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE8AA9  E8 C2 B0 DA FF                  call 0x140893b70
00AE8AAE  48 85 C0                        test rax, rax
00AE8AB1  74 24                           je 0x140ae8ad7
00AE8AB3  80 E3 01                        and bl, 1
00AE8AB6  0F B6 D3                        movzx edx, bl
00AE8AB9  48 8B C8                        mov rcx, rax
00AE8ABC  E8 4B CD F8 FF                  call 0x140a7580c
00AE8AC1  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE8AC6  48 81 C1 E8 01 00 00            add rcx, 0x1e8
00AE8ACD  E8 AE 13 86 FF                  call 0x140349e80
00AE8AD2  E9 78 DD FF FF                  jmp 0x140ae684f
00AE8AD7  41 BE 0A 01 00 C0               mov r14d, 0xc000010a
00AE8ADD  E9 6D DD FF FF                  jmp 0x140ae684f
00AE8AE2  E9 DC 14 00 00                  jmp 0x140ae9fc3
00AE8AE7  0F 11 84 24 88 00 00 00         movups xmmword ptr [rsp + 0x88], xmm0
00AE8AEF  49 8B FE                        mov rdi, r14
00AE8AF2  4C 89 B4 24 40 01 00 00         mov qword ptr [rsp + 0x140], r14
00AE8AFA  41 80 FC 01                     cmp r12b, 1
00AE8AFE  0F 85 C8 00 00 00               jne 0x140ae8bcc
00AE8B04  49 8B C5                        mov rax, r13
00AE8B07  49 3B DD                        cmp rbx, r13
00AE8B0A  48 0F 42 C3                     cmovb rax, rbx
00AE8B0E  90                              nop
00AE8B0F  8B 10                           mov edx, dword ptr [rax]
00AE8B11  89 94 24 88 00 00 00            mov dword ptr [rsp + 0x88], edx
00AE8B18  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
00AE8B1C  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
00AE8B24  66 85 D2                        test dx, dx
00AE8B27  75 0A                           jne 0x140ae8b33
00AE8B29  B8 0D 00 00 C0                  mov eax, 0xc000000d
00AE8B2E  E9 90 14 00 00                  jmp 0x140ae9fc3
00AE8B33  F6 C1 01                        test cl, 1
00AE8B36  0F 85 B7 14 00 00               jne 0x140ae9ff3
00AE8B3C  0F B7 D2                        movzx edx, dx
00AE8B3F  48 8D 04 0A                     lea rax, [rdx + rcx]
00AE8B43  49 3B C5                        cmp rax, r13
00AE8B46  77 05                           ja 0x140ae8b4d
00AE8B48  48 3B C1                        cmp rax, rcx
00AE8B4B  73 05                           jae 0x140ae8b52
00AE8B4D  41 0F B6 45 00                  movzx eax, byte ptr [r13]
00AE8B52  B9 40 00 00 00                  mov ecx, 0x40
00AE8B57  41 B8 50 73 49 6E               mov r8d, 0x6e497350
00AE8B5D  E8 8E 95 09 00                  call 0x140b820f0
00AE8B62  48 8B F8                        mov rdi, rax
00AE8B65  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
00AE8B6D  48 85 C0                        test rax, rax
00AE8B70  75 0A                           jne 0x140ae8b7c
00AE8B72  B8 9A 00 00 C0                  mov eax, 0xc000009a
00AE8B77  E9 47 14 00 00                  jmp 0x140ae9fc3
00AE8B7C  44 0F B7 84 24 88 00 00 00      movzx r8d, word ptr [rsp + 0x88]
00AE8B85  48 8B 94 24 90 00 00 00         mov rdx, qword ptr [rsp + 0x90]
00AE8B8D  48 8B CF                        mov rcx, rdi
00AE8B90  E8 AB DC BD FF                  call 0x1406c6840
00AE8B95  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
00AE8B9D  48 8D 9C 24 88 00 00 00         lea rbx, [rsp + 0x88]
00AE8BA5  48 89 9C 24 E8 01 00 00         mov qword ptr [rsp + 0x1e8], rbx
00AE8BAD  EB 1D                           jmp 0x140ae8bcc
00AE8BAF  8B D8                           mov ebx, eax
00AE8BB1  48 8B 8C 24 40 01 00 00         mov rcx, qword ptr [rsp + 0x140]
00AE8BB9  48 85 C9                        test rcx, rcx
00AE8BBC  74 07                           je 0x140ae8bc5
00AE8BBE  33 D2                           xor edx, edx
00AE8BC0  E8 AB 9C 09 00                  call 0x140b82870
00AE8BC5  8B C3                           mov eax, ebx
00AE8BC7  E9 F7 13 00 00                  jmp 0x140ae9fc3
00AE8BCC  4C 8B 05 C5 DE 4D 00            mov r8, qword ptr [rip + 0x4ddec5]
00AE8BD3  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE8BD8  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE8BDD  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE8BE2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE8BE7  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE8BEF  45 0F B6 CC                     movzx r9d, r12b
00AE8BF3  BA 00 20 00 00                  mov edx, 0x2000
00AE8BF8  48 8B CE                        mov rcx, rsi
00AE8BFB  E8 50 0A D8 FF                  call 0x140869650
00AE8C00  8B F0                           mov esi, eax
00AE8C02  85 C0                           test eax, eax
00AE8C04  79 1A                           jns 0x140ae8c20
00AE8C06  48 85 FF                        test rdi, rdi
00AE8C09  0F 84 9C CB FF FF               je 0x140ae57ab
00AE8C0F  33 D2                           xor edx, edx
00AE8C11  48 8B CF                        mov rcx, rdi
00AE8C14  E8 57 9C 09 00                  call 0x140b82870
00AE8C19  8B C6                           mov eax, esi
00AE8C1B  E9 A3 13 00 00                  jmp 0x140ae9fc3
00AE8C20  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
00AE8C25  48 8B CB                        mov rcx, rbx
00AE8C28  E8 7B F5 AA FF                  call 0x1405981a8
00AE8C2D  8B D8                           mov ebx, eax
00AE8C2F  48 85 FF                        test rdi, rdi
00AE8C32  0F 84 71 D5 FF FF               je 0x140ae61a9
00AE8C38  33 D2                           xor edx, edx
00AE8C3A  48 8B CF                        mov rcx, rdi
00AE8C3D  E8 2E 9C 09 00                  call 0x140b82870
00AE8C42  E9 62 D5 FF FF                  jmp 0x140ae61a9
00AE8C47  45 0F B6 CC                     movzx r9d, r12b
00AE8C4B  44 8B C7                        mov r8d, edi
00AE8C4E  48 8B D3                        mov rdx, rbx
00AE8C51  48 8B CE                        mov rcx, rsi
00AE8C54  E8 6B 8A F7 FF                  call 0x140a616c4
00AE8C59  E9 65 13 00 00                  jmp 0x140ae9fc3
00AE8C5E  83 FF 04                        cmp edi, 4
00AE8C61  0F 85 36 13 00 00               jne 0x140ae9f9d
00AE8C67  4C 8B 05 2A DE 4D 00            mov r8, qword ptr [rip + 0x4dde2a]
00AE8C6E  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE8C73  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE8C78  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE8C7D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE8C82  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE8C8A  45 0F B6 CC                     movzx r9d, r12b
00AE8C8E  BA 00 02 00 00                  mov edx, 0x200
00AE8C93  48 8B CE                        mov rcx, rsi
00AE8C96  E8 B5 09 D8 FF                  call 0x140869650
00AE8C9B  85 C0                           test eax, eax
00AE8C9D  0F 88 20 13 00 00               js 0x140ae9fc3
00AE8CA3  41 8B C6                        mov eax, r14d
00AE8CA6  39 03                           cmp dword ptr [rbx], eax
00AE8CA8  0F 95 C0                        setne al
00AE8CAB  89 84 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], eax
00AE8CB2  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00AE8CBB  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE8CC0  48 39 81 B8 00 00 00            cmp qword ptr [rcx + 0xb8], rax
00AE8CC7  75 0A                           jne 0x140ae8cd3
00AE8CC9  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE8CCE  E9 C9 CA FF FF                  jmp 0x140ae579c
00AE8CD3  41 0F B6 D4                     movzx edx, r12b
00AE8CD7  48 8B 0D A2 0D 4F 00            mov rcx, qword ptr [rip + 0x4f0da2]
00AE8CDE  E8 3D 91 D8 FF                  call 0x140871e20
00AE8CE3  84 C0                           test al, al
00AE8CE5  75 0A                           jne 0x140ae8cf1
00AE8CE7  BE 61 00 00 C0                  mov esi, 0xc0000061
00AE8CEC  E9 AB CA FF FF                  jmp 0x140ae579c
00AE8CF1  41 8B F6                        mov esi, r14d
00AE8CF4  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE8CF9  44 39 B4 24 D8 00 00 00         cmp dword ptr [rsp + 0xd8], r14d
00AE8D01  74 0B                           je 0x140ae8d0e
00AE8D03  F0 0F BA A8 88 00 00 00 05      lock bts dword ptr [rax + 0x88], 5
00AE8D0C  EB 09                           jmp 0x140ae8d17
00AE8D0E  F0 0F BA B0 88 00 00 00 05      lock btr dword ptr [rax + 0x88], 5
00AE8D17  39 B4 24 D8 00 00 00            cmp dword ptr [rsp + 0xd8], esi
00AE8D1E  0F 85 78 CA FF FF               jne 0x140ae579c
00AE8D24  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE8D29  F7 81 F0 01 00 00 00 00 02 00   test dword ptr [rcx + 0x1f0], 0x20000
00AE8D33  0F 84 63 CA FF FF               je 0x140ae579c
00AE8D39  F0 81 A1 F0 01 00 00 FF FF FD FF  lock and dword ptr [rcx + 0x1f0], 0xfffdffff
00AE8D44  E9 53 CA FF FF                  jmp 0x140ae579c
00AE8D49  8B D8                           mov ebx, eax
00AE8D4B  BA 50 73 51 79                  mov edx, 0x79517350
00AE8D50  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE8D55  E8 86 EB 80 FF                  call 0x1402f78e0
00AE8D5A  8B C3                           mov eax, ebx
00AE8D5C  E9 62 12 00 00                  jmp 0x140ae9fc3
00AE8D61  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
00AE8D66  83 FF 08                        cmp edi, 8
00AE8D69  0F 85 2E 12 00 00               jne 0x140ae9f9d
00AE8D6F  4C 8B 05 22 DD 4D 00            mov r8, qword ptr [rip + 0x4ddd22]
00AE8D76  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE8D7B  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE8D80  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE8D85  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE8D8A  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE8D92  45 0F B6 CC                     movzx r9d, r12b
00AE8D96  BA 00 02 00 00                  mov edx, 0x200
00AE8D9B  48 8B CE                        mov rcx, rsi
00AE8D9E  E8 AD 08 D8 FF                  call 0x140869650
00AE8DA3  85 C0                           test eax, eax
00AE8DA5  0F 88 18 12 00 00               js 0x140ae9fc3
00AE8DAB  48 8B 03                        mov rax, qword ptr [rbx]
00AE8DAE  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00AE8DB3  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00AE8DB8  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE8DBD  E8 3E C6 F8 FF                  call 0x140a75400
00AE8DC2  E9 E0 D3 FF FF                  jmp 0x140ae61a7
00AE8DC7  8B D8                           mov ebx, eax
00AE8DC9  BA 50 73 51 79                  mov edx, 0x79517350
00AE8DCE  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE8DD3  E8 08 EB 80 FF                  call 0x1402f78e0
00AE8DD8  8B C3                           mov eax, ebx
00AE8DDA  E9 E4 11 00 00                  jmp 0x140ae9fc3
00AE8DDF  83 FF 20                        cmp edi, 0x20
00AE8DE2  0F 85 B5 11 00 00               jne 0x140ae9f9d
00AE8DE8  4C 8B 05 A9 DC 4D 00            mov r8, qword ptr [rip + 0x4ddca9]
00AE8DEF  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE8DF4  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE8DF9  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE8DFE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE8E03  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE8E0B  45 0F B6 CC                     movzx r9d, r12b
00AE8E0F  BA 01 20 00 00                  mov edx, 0x2001
00AE8E14  48 8B CE                        mov rcx, rsi
00AE8E17  E8 34 08 D8 FF                  call 0x140869650
00AE8E1C  85 C0                           test eax, eax
00AE8E1E  0F 88 9F 11 00 00               js 0x140ae9fc3
00AE8E24  0F 10 03                        movups xmm0, xmmword ptr [rbx]
00AE8E27  0F 11 84 24 30 03 00 00         movups xmmword ptr [rsp + 0x330], xmm0
00AE8E2F  0F 10 4B 10                     movups xmm1, xmmword ptr [rbx + 0x10]
00AE8E33  0F 11 8C 24 40 03 00 00         movups xmmword ptr [rsp + 0x340], xmm1
00AE8E3B  83 BC 24 30 03 00 00 03         cmp dword ptr [rsp + 0x330], 3
00AE8E43  74 19                           je 0x140ae8e5e
00AE8E45  BA 50 73 51 79                  mov edx, 0x79517350
00AE8E4A  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE8E4F  E8 8C EA 80 FF                  call 0x1402f78e0
00AE8E54  B8 59 00 00 C0                  mov eax, 0xc0000059
00AE8E59  E9 65 11 00 00                  jmp 0x140ae9fc3
00AE8E5E  8B 94 24 34 03 00 00            mov edx, dword ptr [rsp + 0x334]
00AE8E65  F7 C2 F8 FF FF FF               test edx, 0xfffffff8
00AE8E6B  75 59                           jne 0x140ae8ec6
00AE8E6D  48 83 BC 24 38 03 00 00 00      cmp qword ptr [rsp + 0x338], 0
00AE8E76  75 4E                           jne 0x140ae8ec6
00AE8E78  48 83 BC 24 40 03 00 00 00      cmp qword ptr [rsp + 0x340], 0
00AE8E81  75 43                           jne 0x140ae8ec6
00AE8E83  8B C2                           mov eax, edx
00AE8E85  D1 E8                           shr eax, 1
00AE8E87  83 E0 01                        and eax, 1
00AE8E8A  75 05                           jne 0x140ae8e91
00AE8E8C  F6 C2 04                        test dl, 4
00AE8E8F  74 05                           je 0x140ae8e96
00AE8E91  F6 C2 01                        test dl, 1
00AE8E94  74 30                           je 0x140ae8ec6
00AE8E96  85 C0                           test eax, eax
00AE8E98  75 17                           jne 0x140ae8eb1
00AE8E9A  F6 C2 04                        test dl, 4
00AE8E9D  75 12                           jne 0x140ae8eb1
00AE8E9F  83 E2 01                        and edx, 1
00AE8EA2  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE8EA7  E8 D8 70 B8 FF                  call 0x14066ff84
00AE8EAC  E9 F6 D2 FF FF                  jmp 0x140ae61a7
00AE8EB1  C1 EA 02                        shr edx, 2
00AE8EB4  83 E2 01                        and edx, 1
00AE8EB7  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE8EBC  E8 0B 6F B8 FF                  call 0x14066fdcc
00AE8EC1  E9 E1 D2 FF FF                  jmp 0x140ae61a7
00AE8EC6  BA 50 73 51 79                  mov edx, 0x79517350
00AE8ECB  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE8ED0  E8 0B EA 80 FF                  call 0x1402f78e0
00AE8ED5  B8 0D 00 00 C0                  mov eax, 0xc000000d
00AE8EDA  E9 E4 10 00 00                  jmp 0x140ae9fc3
00AE8EDF  8B D8                           mov ebx, eax
00AE8EE1  BA 50 73 51 79                  mov edx, 0x79517350
00AE8EE6  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE8EEB  E8 F0 E9 80 FF                  call 0x1402f78e0
00AE8EF0  8B C3                           mov eax, ebx
00AE8EF2  E9 CC 10 00 00                  jmp 0x140ae9fc3
00AE8EF7  40 F6 C7 07                     test dil, 7
00AE8EFB  0F 85 9C 10 00 00               jne 0x140ae9f9d
00AE8F01  81 FF 00 01 00 00               cmp edi, 0x100
00AE8F07  0F 87 90 10 00 00               ja 0x140ae9f9d
00AE8F0D  4C 8B C7                        mov r8, rdi
00AE8F10  48 8B D3                        mov rdx, rbx
00AE8F13  48 8D 8C 24 70 03 00 00         lea rcx, [rsp + 0x370]
00AE8F1B  E8 20 D9 BD FF                  call 0x1406c6840
00AE8F20  90                              nop
00AE8F21  C1 EF 03                        shr edi, 3
00AE8F24  83 BC 24 A0 00 00 00 43         cmp dword ptr [rsp + 0xa0], 0x43
00AE8F2C  0F 94 C3                        sete bl
00AE8F2F  75 11                           jne 0x140ae8f42
00AE8F31  41 0F B6 CC                     movzx ecx, r12b
00AE8F35  E8 0A C5 8B FF                  call 0x1403a5444
00AE8F3A  85 C0                           test eax, eax
00AE8F3C  0F 88 81 10 00 00               js 0x140ae9fc3
00AE8F42  4C 8B 05 4F DB 4D 00            mov r8, qword ptr [rip + 0x4ddb4f]
00AE8F49  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE8F4E  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE8F53  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE8F58  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE8F5D  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE8F65  45 0F B6 CC                     movzx r9d, r12b
00AE8F69  BA 00 20 00 00                  mov edx, 0x2000
00AE8F6E  48 8B CE                        mov rcx, rsi
00AE8F71  E8 DA 06 D8 FF                  call 0x140869650
00AE8F76  85 C0                           test eax, eax
00AE8F78  0F 88 45 10 00 00               js 0x140ae9fc3
00AE8F7E  0F B6 C3                        movzx eax, bl
00AE8F81  34 01                           xor al, 1
00AE8F83  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00AE8F87  44 0F B6 CB                     movzx r9d, bl
00AE8F8B  4C 8D 84 24 70 03 00 00         lea r8, [rsp + 0x370]
00AE8F93  8B D7                           mov edx, edi
00AE8F95  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE8F9A  E8 35 81 AD FF                  call 0x1405c10d4
00AE8F9F  E9 03 D2 FF FF                  jmp 0x140ae61a7
00AE8FA4  E9 1A 10 00 00                  jmp 0x140ae9fc3
00AE8FA9  41 0F B6 CC                     movzx ecx, r12b
00AE8FAD  E8 92 C4 8B FF                  call 0x1403a5444
00AE8FB2  85 C0                           test eax, eax
00AE8FB4  0F 88 09 10 00 00               js 0x140ae9fc3
00AE8FBA  83 FF 01                        cmp edi, 1
00AE8FBD  0F 85 DA 0F 00 00               jne 0x140ae9f9d
00AE8FC3  0F B6 1B                        movzx ebx, byte ptr [rbx]
00AE8FC6  88 9C 24 B1 00 00 00            mov byte ptr [rsp + 0xb1], bl
00AE8FCD  4C 8B 05 C4 DA 4D 00            mov r8, qword ptr [rip + 0x4ddac4]
00AE8FD4  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE8FD9  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE8FDE  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE8FE3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE8FE8  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE8FF0  45 0F B6 CC                     movzx r9d, r12b
00AE8FF4  BA 00 20 00 00                  mov edx, 0x2000
00AE8FF9  48 8B CE                        mov rcx, rsi
00AE8FFC  E8 4F 06 D8 FF                  call 0x140869650
00AE9001  85 C0                           test eax, eax
00AE9003  0F 88 BA 0F 00 00               js 0x140ae9fc3
00AE9009  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE900E  84 DB                           test bl, bl
00AE9010  74 1A                           je 0x140ae902c
00AE9012  F0 81 88 F0 01 00 00 00 00 00 08  lock or dword ptr [rax + 0x1f0], 0x8000000
00AE901D  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE9022  E8 51 80 AD FF                  call 0x1405c1078
00AE9027  E9 1B C8 FF FF                  jmp 0x140ae5847
00AE902C  F0 81 A0 F0 01 00 00 FF FF FF F7  lock and dword ptr [rax + 0x1f0], 0xf7ffffff
00AE9037  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE903C  E8 37 80 AD FF                  call 0x1405c1078
00AE9041  E9 01 C8 FF FF                  jmp 0x140ae5847
00AE9046  E9 78 0F 00 00                  jmp 0x140ae9fc3
00AE904B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AE9054  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00AE905B  8B 81 DC 07 00 00               mov eax, dword ptr [rcx + 0x7dc]
00AE9061  A8 08                           test al, 8
00AE9063  0F 84 A5 C8 FF FF               je 0x140ae590e
00AE9069  4C 8B 05 28 DA 4D 00            mov r8, qword ptr [rip + 0x4dda28]
00AE9070  4C 89 B4 24 48 01 00 00         mov qword ptr [rsp + 0x148], r14
00AE9078  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00AE907D  48 8D 84 24 48 01 00 00         lea rax, [rsp + 0x148]
00AE9085  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AE908A  45 0F B6 CC                     movzx r9d, r12b
00AE908E  BA 00 02 00 00                  mov edx, 0x200
00AE9093  48 8B CE                        mov rcx, rsi
00AE9096  E8 15 FD D7 FF                  call 0x140868db0
00AE909B  8B D8                           mov ebx, eax
00AE909D  48 8B 84 24 48 01 00 00         mov rax, qword ptr [rsp + 0x148]
00AE90A5  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00AE90AA  85 DB                           test ebx, ebx
00AE90AC  0F 88 06 D1 FF FF               js 0x140ae61b8
00AE90B2  F0 83 88 FC 05 00 00 40         lock or dword ptr [rax + 0x5fc], 0x40
00AE90BA  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE90BF  E8 8C 02 81 FF                  call 0x1402f9350
00AE90C4  8B C3                           mov eax, ebx
00AE90C6  E9 F8 0E 00 00                  jmp 0x140ae9fc3
00AE90CB  4C 8B 05 C6 D9 4D 00            mov r8, qword ptr [rip + 0x4dd9c6]
00AE90D2  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE90D7  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE90DC  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE90E1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE90E6  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE90EE  45 0F B6 CC                     movzx r9d, r12b
00AE90F2  BA 00 02 00 00                  mov edx, 0x200
00AE90F7  48 8B CE                        mov rcx, rsi
00AE90FA  E8 51 05 D8 FF                  call 0x140869650
00AE90FF  85 C0                           test eax, eax
00AE9101  0F 88 BC 0E 00 00               js 0x140ae9fc3
00AE9107  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE910C  E8 27 6E B6 FF                  call 0x14064ff38
00AE9111  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE9116  F0 81 88 F0 01 00 00 00 00 00 80  lock or dword ptr [rax + 0x1f0], 0x80000000
00AE9121  E9 21 C7 FF FF                  jmp 0x140ae5847
00AE9126  83 FF 04                        cmp edi, 4
00AE9129  0F 85 6E 0E 00 00               jne 0x140ae9f9d
00AE912F  8B 1B                           mov ebx, dword ptr [rbx]
00AE9131  89 9C 24 74 01 00 00            mov dword ptr [rsp + 0x174], ebx
00AE9138  4C 8B 05 59 D9 4D 00            mov r8, qword ptr [rip + 0x4dd959]
00AE913F  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE9144  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE9149  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE914E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE9153  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE915B  45 0F B6 CC                     movzx r9d, r12b
00AE915F  BA 00 02 00 00                  mov edx, 0x200
00AE9164  48 8B CE                        mov rcx, rsi
00AE9167  E8 E4 04 D8 FF                  call 0x140869650
00AE916C  85 C0                           test eax, eax
00AE916E  0F 88 4F 0E 00 00               js 0x140ae9fc3
00AE9174  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE9179  E8 F2 A9 DA FF                  call 0x140893b70
00AE917E  48 85 C0                        test rax, rax
00AE9181  0F 84 50 F9 FF FF               je 0x140ae8ad7
00AE9187  8B D3                           mov edx, ebx
00AE9189  48 8B C8                        mov rcx, rax
00AE918C  E8 D7 16 F8 FF                  call 0x140a6a868
00AE9191  E9 2B F9 FF FF                  jmp 0x140ae8ac1
00AE9196  E9 28 0E 00 00                  jmp 0x140ae9fc3
00AE919B  44 8B C7                        mov r8d, edi
00AE919E  48 8B D3                        mov rdx, rbx
00AE91A1  48 8B CE                        mov rcx, rsi
00AE91A4  E8 87 EA C9 FF                  call 0x140787c30
00AE91A9  E9 15 0E 00 00                  jmp 0x140ae9fc3
00AE91AE  83 FF 01                        cmp edi, 1
00AE91B1  0F 85 E6 0D 00 00               jne 0x140ae9f9d
00AE91B7  0F B6 1B                        movzx ebx, byte ptr [rbx]
00AE91BA  88 9C 24 B2 00 00 00            mov byte ptr [rsp + 0xb2], bl
00AE91C1  41 0F B6 D4                     movzx edx, r12b
00AE91C5  48 8B 0D AC 08 4F 00            mov rcx, qword ptr [rip + 0x4f08ac]
00AE91CC  E8 4F 8C D8 FF                  call 0x140871e20
00AE91D1  84 C0                           test al, al
00AE91D3  0F 84 35 C7 FF FF               je 0x140ae590e
00AE91D9  4C 8B 05 B8 D8 4D 00            mov r8, qword ptr [rip + 0x4dd8b8]
00AE91E0  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE91E5  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE91EA  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE91EF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE91F4  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE91FC  45 0F B6 CC                     movzx r9d, r12b
00AE9200  BA 00 20 00 00                  mov edx, 0x2000
00AE9205  48 8B CE                        mov rcx, rsi
00AE9208  E8 43 04 D8 FF                  call 0x140869650
00AE920D  85 C0                           test eax, eax
00AE920F  0F 88 AE 0D 00 00               js 0x140ae9fc3
00AE9215  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE921A  84 DB                           test bl, bl
00AE921C  74 10                           je 0x140ae922e
00AE921E  F0 81 88 FC 05 00 00 00 02 00 00  lock or dword ptr [rax + 0x5fc], 0x200
00AE9229  E9 19 C6 FF FF                  jmp 0x140ae5847
00AE922E  F0 81 A0 FC 05 00 00 FF FD FF FF  lock and dword ptr [rax + 0x5fc], 0xfffffdff
00AE9239  E9 09 C6 FF FF                  jmp 0x140ae5847
00AE923E  E9 80 0D 00 00                  jmp 0x140ae9fc3
00AE9243  33 C0                           xor eax, eax
00AE9245  48 89 84 24 10 02 00 00         mov qword ptr [rsp + 0x210], rax
00AE924D  89 84 24 18 02 00 00            mov dword ptr [rsp + 0x218], eax
00AE9254  83 FF 0C                        cmp edi, 0xc
00AE9257  0F 85 40 0D 00 00               jne 0x140ae9f9d
00AE925D  F2 0F 10 03                     movsd xmm0, qword ptr [rbx]
00AE9261  F2 0F 11 84 24 10 02 00 00      movsd qword ptr [rsp + 0x210], xmm0
00AE926A  8B 4B 08                        mov ecx, dword ptr [rbx + 8]
00AE926D  89 8C 24 18 02 00 00            mov dword ptr [rsp + 0x218], ecx
00AE9274  83 BC 24 10 02 00 00 01         cmp dword ptr [rsp + 0x210], 1
00AE927C  0F 85 53 FC FF FF               jne 0x140ae8ed5
00AE9282  48 8B 84 24 10 02 00 00         mov rax, qword ptr [rsp + 0x210]
00AE928A  48 C1 E8 20                     shr rax, 0x20
00AE928E  A9 F8 FF FF FF                  test eax, 0xfffffff8
00AE9293  0F 85 3C FC FF FF               jne 0x140ae8ed5
00AE9299  F7 D0                           not eax
00AE929B  85 C1                           test ecx, eax
00AE929D  0F 85 32 FC FF FF               jne 0x140ae8ed5
00AE92A3  48 8B 0D F6 D9 4D 00            mov rcx, qword ptr [rip + 0x4dd9f6]
00AE92AA  E8 65 F5 93 FF                  call 0x140428814
00AE92AF  48 8B D8                        mov rbx, rax
00AE92B2  48 85 C0                        test rax, rax
00AE92B5  0F 84 06 D0 FF FF               je 0x140ae62c1
00AE92BB  4C 8B 05 D6 D7 4D 00            mov r8, qword ptr [rip + 0x4dd7d6]
00AE92C2  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE92C7  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE92CC  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE92D1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE92D6  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE92DE  45 0F B6 CC                     movzx r9d, r12b
00AE92E2  BA 00 20 00 00                  mov edx, 0x2000
00AE92E7  48 8B CE                        mov rcx, rsi
00AE92EA  E8 61 03 D8 FF                  call 0x140869650
00AE92EF  8B F8                           mov edi, eax
00AE92F1  85 C0                           test eax, eax
00AE92F3  79 13                           jns 0x140ae9308
00AE92F5  48 8B 0D A4 D9 4D 00            mov rcx, qword ptr [rip + 0x4dd9a4]
00AE92FC  E8 BF DA 96 FF                  call 0x140456dc0
00AE9301  8B C7                           mov eax, edi
00AE9303  E9 BB 0C 00 00                  jmp 0x140ae9fc3
00AE9308  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00AE930C  48 8D 94 24 10 02 00 00         lea rdx, [rsp + 0x210]
00AE9314  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE9319  E8 B2 17 BD FF                  call 0x1406baad0
00AE931E  8B D8                           mov ebx, eax
00AE9320  BA 50 73 51 79                  mov edx, 0x79517350
00AE9325  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE932A  E8 B1 E5 80 FF                  call 0x1402f78e0
00AE932F  48 8B 0D 6A D9 4D 00            mov rcx, qword ptr [rip + 0x4dd96a]
00AE9336  E8 85 DA 96 FF                  call 0x140456dc0
00AE933B  8B C3                           mov eax, ebx
00AE933D  E9 81 0C 00 00                  jmp 0x140ae9fc3
00AE9342  E9 7C 0C 00 00                  jmp 0x140ae9fc3
00AE9347  83 FF 08                        cmp edi, 8
00AE934A  0F 82 4D 0C 00 00               jb 0x140ae9f9d
00AE9350  0F 11 84 24 A0 02 00 00         movups xmmword ptr [rsp + 0x2a0], xmm0
00AE9358  0F 11 84 24 B0 02 00 00         movups xmmword ptr [rsp + 0x2b0], xmm0
00AE9360  0F 11 84 24 C0 02 00 00         movups xmmword ptr [rsp + 0x2c0], xmm0
00AE9368  0F 11 84 24 D0 02 00 00         movups xmmword ptr [rsp + 0x2d0], xmm0
00AE9370  0F 11 84 24 E0 02 00 00         movups xmmword ptr [rsp + 0x2e0], xmm0
00AE9378  0F 11 84 24 F0 02 00 00         movups xmmword ptr [rsp + 0x2f0], xmm0
00AE9380  0F 11 84 24 00 03 00 00         movups xmmword ptr [rsp + 0x300], xmm0
00AE9388  0F 11 84 24 10 03 00 00         movups xmmword ptr [rsp + 0x310], xmm0
00AE9390  0F 11 84 24 20 03 00 00         movups xmmword ptr [rsp + 0x320], xmm0
00AE9398  B8 90 00 00 00                  mov eax, 0x90
00AE939D  3B F8                           cmp edi, eax
00AE939F  0F 43 F8                        cmovae edi, eax
00AE93A2  44 8B C7                        mov r8d, edi
00AE93A5  48 8B D3                        mov rdx, rbx
00AE93A8  48 8D 8C 24 A0 02 00 00         lea rcx, [rsp + 0x2a0]
00AE93B0  E8 8B D4 BD FF                  call 0x1406c6840
00AE93B5  90                              nop
00AE93B6  4C 8B 05 DB D6 4D 00            mov r8, qword ptr [rip + 0x4dd6db]
00AE93BD  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE93C2  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE93C7  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE93CC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE93D1  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE93D9  45 0F B6 CC                     movzx r9d, r12b
00AE93DD  BA 00 02 00 00                  mov edx, 0x200
00AE93E2  48 8B CE                        mov rcx, rsi
00AE93E5  E8 66 02 D8 FF                  call 0x140869650
00AE93EA  85 C0                           test eax, eax
00AE93EC  0F 88 D1 0B 00 00               js 0x140ae9fc3
00AE93F2  48 8D 94 24 A0 02 00 00         lea rdx, [rsp + 0x2a0]
00AE93FA  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE93FF  E8 00 35 EA FF                  call 0x14098c904
00AE9404  8B D8                           mov ebx, eax
00AE9406  BA 50 73 51 79                  mov edx, 0x79517350
00AE940B  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE9410  85 C0                           test eax, eax
00AE9412  0F 89 39 C4 FF FF               jns 0x140ae5851
00AE9418  E8 C3 E4 80 FF                  call 0x1402f78e0
00AE941D  8B C3                           mov eax, ebx
00AE941F  E9 9F 0B 00 00                  jmp 0x140ae9fc3
00AE9424  E9 9A 0B 00 00                  jmp 0x140ae9fc3
00AE9429  83 FF 18                        cmp edi, 0x18
00AE942C  0F 85 6B 0B 00 00               jne 0x140ae9f9d
00AE9432  33 C0                           xor eax, eax
00AE9434  0F 11 84 24 70 04 00 00         movups xmmword ptr [rsp + 0x470], xmm0
00AE943C  0F 11 84 24 80 04 00 00         movups xmmword ptr [rsp + 0x480], xmm0
00AE9444  0F 11 84 24 90 04 00 00         movups xmmword ptr [rsp + 0x490], xmm0
00AE944C  0F 11 84 24 A0 04 00 00         movups xmmword ptr [rsp + 0x4a0], xmm0
00AE9454  88 84 24 B0 04 00 00            mov byte ptr [rsp + 0x4b0], al
00AE945B  0F 10 0B                        movups xmm1, xmmword ptr [rbx]
00AE945E  0F 11 8C 24 30 03 00 00         movups xmmword ptr [rsp + 0x330], xmm1
00AE9466  F2 0F 10 43 10                  movsd xmm0, qword ptr [rbx + 0x10]
00AE946B  F2 0F 11 84 24 40 03 00 00      movsd qword ptr [rsp + 0x340], xmm0
00AE9474  66 49 0F 7E C8                  movq r8, xmm1
00AE9479  49 8D 40 41                     lea rax, [r8 + 0x41]
00AE947D  49 3B C5                        cmp rax, r13
00AE9480  77 05                           ja 0x140ae9487
00AE9482  49 3B C0                        cmp rax, r8
00AE9485  73 0D                           jae 0x140ae9494
00AE9487  41 0F B6 45 00                  movzx eax, byte ptr [r13]
00AE948C  4C 8B 84 24 30 03 00 00         mov r8, qword ptr [rsp + 0x330]
00AE9494  BA 41 00 00 00                  mov edx, 0x41
00AE9499  48 8D 8C 24 70 04 00 00         lea rcx, [rsp + 0x470]
00AE94A1  E8 96 7F 97 FF                  call 0x14046143c
00AE94A6  90                              nop
00AE94A7  4C 8B 05 EA D5 4D 00            mov r8, qword ptr [rip + 0x4dd5ea]
00AE94AE  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00AE94B3  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE94B8  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE94BD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE94C2  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE94CA  45 0F B6 CC                     movzx r9d, r12b
00AE94CE  BA 20 02 00 00                  mov edx, 0x220
00AE94D3  48 8B CE                        mov rcx, rsi
00AE94D6  E8 75 01 D8 FF                  call 0x140869650
00AE94DB  85 C0                           test eax, eax
00AE94DD  0F 88 E0 0A 00 00               js 0x140ae9fc3
00AE94E3  48 8D 84 24 70 04 00 00         lea rax, [rsp + 0x470]
00AE94EB  48 89 84 24 30 03 00 00         mov qword ptr [rsp + 0x330], rax
00AE94F3  C6 84 24 B0 04 00 00 00         mov byte ptr [rsp + 0x4b0], 0
00AE94FB  48 8D 94 24 30 03 00 00         lea rdx, [rsp + 0x330]
00AE9503  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE9508  E8 D3 6F E9 FF                  call 0x1409804e0
00AE950D  8B F8                           mov edi, eax
00AE950F  BA 50 73 51 79                  mov edx, 0x79517350
00AE9514  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE9519  E8 C2 E3 80 FF                  call 0x1402f78e0
00AE951E  90                              nop
00AE951F  8B 8C 24 3C 03 00 00            mov ecx, dword ptr [rsp + 0x33c]
00AE9526  89 4B 0C                        mov dword ptr [rbx + 0xc], ecx
00AE9529  8B 8C 24 40 03 00 00            mov ecx, dword ptr [rsp + 0x340]
00AE9530  89 4B 10                        mov dword ptr [rbx + 0x10], ecx
00AE9533  E9 6D C5 FF FF                  jmp 0x140ae5aa5
00AE9538  E9 86 0A 00 00                  jmp 0x140ae9fc3
00AE953D  E9 81 0A 00 00                  jmp 0x140ae9fc3
00AE9542  41 83 FA 57                     cmp r10d, 0x57
00AE9546  75 09                           jne 0x140ae9551
00AE9548  83 FF 01                        cmp edi, 1
00AE954B  0F 82 4C 0A 00 00               jb 0x140ae9f9d
00AE9551  41 83 FA 60                     cmp r10d, 0x60
00AE9555  75 09                           jne 0x140ae9560
00AE9557  83 FF 04                        cmp edi, 4
00AE955A  0F 82 3D 0A 00 00               jb 0x140ae9f9d
00AE9560  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AE9569  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00AE9570  45 84 E4                        test r12b, r12b
00AE9573  74 16                           je 0x140ae958b
00AE9575  0F B6 89 FA 05 00 00            movzx ecx, byte ptr [rcx + 0x5fa]
00AE957C  B2 31                           mov dl, 0x31
00AE957E  E8 45 6B F2 FF                  call 0x140a100c8
00AE9583  84 C0                           test al, al
00AE9585  0F 84 A5 07 00 00               je 0x140ae9d30
00AE958B  41 0F B6 D4                     movzx edx, r12b
00AE958F  48 8B 0D EA 04 4F 00            mov rcx, qword ptr [rip + 0x4f04ea]
00AE9596  E8 85 88 D8 FF                  call 0x140871e20
00AE959B  84 C0                           test al, al
00AE959D  75 18                           jne 0x140ae95b7
00AE959F  41 0F B6 D4                     movzx edx, r12b
00AE95A3  48 8B 0D CE 04 4F 00            mov rcx, qword ptr [rip + 0x4f04ce]
00AE95AA  E8 71 88 D8 FF                  call 0x140871e20
00AE95AF  84 C0                           test al, al
00AE95B1  0F 84 57 C3 FF FF               je 0x140ae590e
00AE95B7  44 89 B4 24 9C 00 00 00         mov dword ptr [rsp + 0x9c], r14d
00AE95BF  83 BC 24 A0 00 00 00 57         cmp dword ptr [rsp + 0xa0], 0x57
00AE95C7  75 14                           jne 0x140ae95dd
00AE95C9  0F B6 03                        movzx eax, byte ptr [rbx]
00AE95CC  8B C8                           mov ecx, eax
00AE95CE  83 E1 01                        and ecx, 1
00AE95D1  89 8C 24 9C 00 00 00            mov dword ptr [rsp + 0x9c], ecx
00AE95D8  83 E0 03                        and eax, 3
00AE95DB  EB 02                           jmp 0x140ae95df
00AE95DD  8B 03                           mov eax, dword ptr [rbx]
00AE95DF  89 84 24 9C 00 00 00            mov dword ptr [rsp + 0x9c], eax
00AE95E6  A9 80 FF FF FF                  test eax, 0xffffff80
00AE95EB  0F 85 E4 F8 FF FF               jne 0x140ae8ed5
00AE95F1  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE95F6  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE95FB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE9600  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE9608  45 0F B6 CC                     movzx r9d, r12b
00AE960C  4C 8B 05 85 D4 4D 00            mov r8, qword ptr [rip + 0x4dd485]
00AE9613  BA 00 20 00 00                  mov edx, 0x2000
00AE9618  48 8B CE                        mov rcx, rsi
00AE961B  E8 F0 FF D7 FF                  call 0x140869610
00AE9620  85 C0                           test eax, eax
00AE9622  0F 88 9B 09 00 00               js 0x140ae9fc3
00AE9628  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE962D  F0 81 A0 FC 05 00 00 FF FF E7 4F  lock and dword ptr [rax + 0x5fc], 0x4fe7ffff
00AE9638  8B 84 24 9C 00 00 00            mov eax, dword ptr [rsp + 0x9c]
00AE963F  8B D0                           mov edx, eax
00AE9641  C1 EA 02                        shr edx, 2
00AE9644  83 E2 01                        and edx, 1
00AE9647  C1 E2 13                        shl edx, 0x13
00AE964A  44 8B C2                        mov r8d, edx
00AE964D  41 BA 00 00 10 00               mov r10d, 0x100000
00AE9653  45 0B C2                        or r8d, r10d
00AE9656  A8 08                           test al, 8
00AE9658  44 0F 44 C2                     cmove r8d, edx
00AE965C  41 8B D0                        mov edx, r8d
00AE965F  0F BA EA 1D                     bts edx, 0x1d
00AE9663  A8 10                           test al, 0x10
00AE9665  41 0F 44 D0                     cmove edx, r8d
00AE9669  44 8B C2                        mov r8d, edx
00AE966C  41 0F BA E8 1C                  bts r8d, 0x1c
00AE9671  A8 20                           test al, 0x20
00AE9673  44 0F 44 C2                     cmove r8d, edx
00AE9677  41 8B C8                        mov ecx, r8d
00AE967A  81 C9 00 00 00 80               or ecx, 0x80000000
00AE9680  F6 84 24 9C 00 00 00 40         test byte ptr [rsp + 0x9c], 0x40
00AE9688  41 0F 44 C8                     cmove ecx, r8d
00AE968C  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE9691  F0 09 88 FC 05 00 00            lock or dword ptr [rax + 0x5fc], ecx
00AE9698  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE969D  F0 81 A0 F0 01 00 00 FF FF FF FC  lock and dword ptr [rax + 0x1f0], 0xfcffffff
00AE96A8  8B 94 24 9C 00 00 00            mov edx, dword ptr [rsp + 0x9c]
00AE96AF  83 E2 01                        and edx, 1
00AE96B2  C1 E2 18                        shl edx, 0x18
00AE96B5  8B CA                           mov ecx, edx
00AE96B7  0F BA E9 19                     bts ecx, 0x19
00AE96BB  F6 84 24 9C 00 00 00 02         test byte ptr [rsp + 0x9c], 2
00AE96C3  0F 44 CA                        cmove ecx, edx
00AE96C6  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE96CB  F0 09 88 F0 01 00 00            lock or dword ptr [rax + 0x1f0], ecx
00AE96D2  E9 70 C1 FF FF                  jmp 0x140ae5847
00AE96D7  E9 E7 08 00 00                  jmp 0x140ae9fc3
00AE96DC  44 8B CF                        mov r9d, edi
00AE96DF  4C 8B C3                        mov r8, rbx
00AE96E2  41 8B D2                        mov edx, r10d
00AE96E5  48 8B CE                        mov rcx, rsi
00AE96E8  E8 1B 21 CB FF                  call 0x14079b808
00AE96ED  E9 D1 08 00 00                  jmp 0x140ae9fc3
00AE96F2  83 FF 04                        cmp edi, 4
00AE96F5  0F 85 A2 08 00 00               jne 0x140ae9f9d
00AE96FB  8B 1B                           mov ebx, dword ptr [rbx]
00AE96FD  89 9C 24 70 01 00 00            mov dword ptr [rsp + 0x170], ebx
00AE9704  F7 C3 FE FF FF FF               test ebx, 0xfffffffe
00AE970A  0F 85 C5 F7 FF FF               jne 0x140ae8ed5
00AE9710  41 0F B6 D4                     movzx edx, r12b
00AE9714  48 8B 0D 5D 03 4F 00            mov rcx, qword ptr [rip + 0x4f035d]
00AE971B  E8 00 87 D8 FF                  call 0x140871e20
00AE9720  84 C0                           test al, al
00AE9722  0F 84 E6 C1 FF FF               je 0x140ae590e
00AE9728  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE972D  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE9732  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE9737  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE973F  45 0F B6 CC                     movzx r9d, r12b
00AE9743  4C 8B 05 4E D3 4D 00            mov r8, qword ptr [rip + 0x4dd34e]
00AE974A  BA 00 20 00 00                  mov edx, 0x2000
00AE974F  48 8B CE                        mov rcx, rsi
00AE9752  E8 B9 FE D7 FF                  call 0x140869610
00AE9757  85 C0                           test eax, eax
00AE9759  0F 88 64 08 00 00               js 0x140ae9fc3
00AE975F  80 E3 01                        and bl, 1
00AE9762  41 B0 01                        mov r8b, 1
00AE9765  0F B6 D3                        movzx edx, bl
00AE9768  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE976D  E8 5A C6 F5 FF                  call 0x140a45dcc
00AE9772  E9 D0 C0 FF FF                  jmp 0x140ae5847
00AE9777  E9 47 08 00 00                  jmp 0x140ae9fc3
00AE977C  83 FF 08                        cmp edi, 8
00AE977F  0F 85 18 08 00 00               jne 0x140ae9f9d
00AE9785  48 8B 1B                        mov rbx, qword ptr [rbx]
00AE9788  48 89 9C 24 F0 01 00 00         mov qword ptr [rsp + 0x1f0], rbx
00AE9790  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE9795  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE979A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE979F  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE97A7  45 0F B6 CC                     movzx r9d, r12b
00AE97AB  4C 8B 05 E6 D2 4D 00            mov r8, qword ptr [rip + 0x4dd2e6]
00AE97B2  BA 00 20 00 00                  mov edx, 0x2000
00AE97B7  48 8B CE                        mov rcx, rsi
00AE97BA  E8 51 FE D7 FF                  call 0x140869610
00AE97BF  85 C0                           test eax, eax
00AE97C1  0F 88 FC 07 00 00               js 0x140ae9fc3
00AE97C7  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE97CC  48 8D 84 24 30 01 00 00         lea rax, [rsp + 0x130]
00AE97D4  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE97D9  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE97E1  45 0F B6 CC                     movzx r9d, r12b
00AE97E5  4C 8B 05 AC D2 4D 00            mov r8, qword ptr [rip + 0x4dd2ac]
00AE97EC  BA 00 10 00 00                  mov edx, 0x1000
00AE97F1  48 8B CB                        mov rcx, rbx
00AE97F4  E8 17 FE D7 FF                  call 0x140869610
00AE97F9  8B D8                           mov ebx, eax
00AE97FB  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE9800  85 C0                           test eax, eax
00AE9802  0F 88 A6 C9 FF FF               js 0x140ae61ae
00AE9808  48 8B 94 24 30 01 00 00         mov rdx, qword ptr [rsp + 0x130]
00AE9810  E8 AB 80 DB FF                  call 0x1408a18c0
00AE9815  8B D8                           mov ebx, eax
00AE9817  BA 50 73 51 79                  mov edx, 0x79517350
00AE981C  48 8B 8C 24 30 01 00 00         mov rcx, qword ptr [rsp + 0x130]
00AE9824  E8 B7 E0 80 FF                  call 0x1402f78e0
00AE9829  E9 7B C9 FF FF                  jmp 0x140ae61a9
00AE982E  E9 90 07 00 00                  jmp 0x140ae9fc3
00AE9833  83 FF 08                        cmp edi, 8
00AE9836  0F 85 61 07 00 00               jne 0x140ae9f9d
00AE983C  48 8B 1B                        mov rbx, qword ptr [rbx]
00AE983F  48 89 9C 24 28 01 00 00         mov qword ptr [rsp + 0x128], rbx
00AE9847  F7 C3 FE FF FF FF               test ebx, 0xfffffffe
00AE984D  0F 85 82 F6 FF FF               jne 0x140ae8ed5
00AE9853  48 83 FE FF                     cmp rsi, -1
00AE9857  0F 85 78 F6 FF FF               jne 0x140ae8ed5
00AE985D  E8 EE 1C 93 FF                  call 0x14041b550
00AE9862  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00AE9867  48 8B 90 E0 02 00 00            mov rdx, qword ptr [rax + 0x2e0]
00AE986E  48 85 D2                        test rdx, rdx
00AE9871  0F 84 B9 04 00 00               je 0x140ae9d30
00AE9877  49 8B CE                        mov rcx, r14
00AE987A  4C 8B 80 10 03 00 00            mov r8, qword ptr [rax + 0x310]
00AE9881  4D 85 C0                        test r8, r8
00AE9884  74 03                           je 0x140ae9889
00AE9886  49 8B 08                        mov rcx, qword ptr [r8]
00AE9889  83 E3 01                        and ebx, 1
00AE988C  8B 82 C0 07 00 00               mov eax, dword ptr [rdx + 0x7c0]
00AE9892  74 05                           je 0x140ae9899
00AE9894  83 C8 01                        or eax, 1
00AE9897  EB 03                           jmp 0x140ae989c
00AE9899  83 E0 FE                        and eax, 0xfffffffe
00AE989C  89 82 C0 07 00 00               mov dword ptr [rdx + 0x7c0], eax
00AE98A2  48 85 C9                        test rcx, rcx
00AE98A5  74 18                           je 0x140ae98bf
00AE98A7  8B 81 74 04 00 00               mov eax, dword ptr [rcx + 0x474]
00AE98AD  85 DB                           test ebx, ebx
00AE98AF  74 05                           je 0x140ae98b6
00AE98B1  83 C8 01                        or eax, 1
00AE98B4  EB 03                           jmp 0x140ae98b9
00AE98B6  83 E0 FE                        and eax, 0xfffffffe
00AE98B9  89 81 74 04 00 00               mov dword ptr [rcx + 0x474], eax
00AE98BF  E9 9A CF FF FF                  jmp 0x140ae685e
00AE98C4  44 8B F0                        mov r14d, eax
00AE98C7  E9 92 CF FF FF                  jmp 0x140ae685e
00AE98CC  E9 F2 06 00 00                  jmp 0x140ae9fc3
00AE98D1  33 C0                           xor eax, eax
00AE98D3  0F 11 84 24 30 03 00 00         movups xmmword ptr [rsp + 0x330], xmm0
00AE98DB  89 84 24 40 03 00 00            mov dword ptr [rsp + 0x340], eax
00AE98E2  83 FF 14                        cmp edi, 0x14
00AE98E5  0F 85 B2 06 00 00               jne 0x140ae9f9d
00AE98EB  0F 10 03                        movups xmm0, xmmword ptr [rbx]
00AE98EE  0F 11 84 24 30 03 00 00         movups xmmword ptr [rsp + 0x330], xmm0
00AE98F6  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
00AE98F9  89 84 24 40 03 00 00            mov dword ptr [rsp + 0x340], eax
00AE9900  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE9905  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE990A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE990F  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE9917  45 0F B6 CC                     movzx r9d, r12b
00AE991B  4C 8B 05 76 D1 4D 00            mov r8, qword ptr [rip + 0x4dd176]
00AE9922  BA 20 00 00 00                  mov edx, 0x20
00AE9927  48 8B CE                        mov rcx, rsi
00AE992A  E8 E1 FC D7 FF                  call 0x140869610
00AE992F  85 C0                           test eax, eax
00AE9931  0F 88 8C 06 00 00               js 0x140ae9fc3
00AE9937  48 8D 94 24 30 03 00 00         lea rdx, [rsp + 0x330]
00AE993F  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE9944  E8 53 4E C9 FF                  call 0x14077e79c
00AE9949  E9 59 C8 FF FF                  jmp 0x140ae61a7
00AE994E  E9 70 06 00 00                  jmp 0x140ae9fc3
00AE9953  44 89 74 24 60                  mov dword ptr [rsp + 0x60], r14d
00AE9958  4D 8B EE                        mov r13, r14
00AE995B  83 FF 10                        cmp edi, 0x10
00AE995E  0F 85 39 06 00 00               jne 0x140ae9f9d
00AE9964  0F 10 03                        movups xmm0, xmmword ptr [rbx]
00AE9967  0F 11 84 24 30 03 00 00         movups xmmword ptr [rsp + 0x330], xmm0
00AE996F  0F B7 84 24 30 03 00 00         movzx eax, word ptr [rsp + 0x330]
00AE9977  C1 E0 04                        shl eax, 4
00AE997A  85 C0                           test eax, eax
00AE997C  0F 84 53 F5 FF FF               je 0x140ae8ed5
00AE9982  48 8B 9C 24 38 03 00 00         mov rbx, qword ptr [rsp + 0x338]
00AE998A  48 85 DB                        test rbx, rbx
00AE998D  0F 84 42 F5 FF FF               je 0x140ae8ed5
00AE9993  8B F8                           mov edi, eax
00AE9995  45 8B C7                        mov r8d, r15d
00AE9998  8B D0                           mov edx, eax
00AE999A  48 8B CB                        mov rcx, rbx
00AE999D  E8 1E F8 DF FF                  call 0x1408e91c0
00AE99A2  90                              nop
00AE99A3  66 83 BC 24 32 03 00 00 00      cmp word ptr [rsp + 0x332], 0
00AE99AC  0F 85 23 F5 FF FF               jne 0x140ae8ed5
00AE99B2  83 BC 24 34 03 00 00 00         cmp dword ptr [rsp + 0x334], 0
00AE99BA  0F 85 15 F5 FF FF               jne 0x140ae8ed5
00AE99C0  41 80 FC 01                     cmp r12b, 1
00AE99C4  0F 85 66 03 00 00               jne 0x140ae9d30
00AE99CA  4C 8B 05 C7 D0 4D 00            mov r8, qword ptr [rip + 0x4dd0c7]
00AE99D1  4C 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], r14
00AE99D9  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00AE99DE  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AE99E6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AE99EB  45 0F B6 CC                     movzx r9d, r12b
00AE99EF  BA 00 02 00 00                  mov edx, 0x200
00AE99F4  48 8B CE                        mov rcx, rsi
00AE99F7  E8 B4 F3 D7 FF                  call 0x140868db0
00AE99FC  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AE9A04  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00AE9A09  85 C0                           test eax, eax
00AE9A0B  0F 88 B2 05 00 00               js 0x140ae9fc3
00AE9A11  E8 3A 1B 93 FF                  call 0x14041b550
00AE9A16  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE9A1B  48 3B C8                        cmp rcx, rax
00AE9A1E  75 16                           jne 0x140ae9a36
00AE9A20  F7 81 54 07 00 00 00 00 00 40   test dword ptr [rcx + 0x754], 0x40000000
00AE9A2A  74 0A                           je 0x140ae9a36
00AE9A2C  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE9A31  E9 C0 00 00 00                  jmp 0x140ae9af6
00AE9A36  F7 81 54 07 00 00 00 40 00 00   test dword ptr [rcx + 0x754], 0x4000
00AE9A40  75 0A                           jne 0x140ae9a4c
00AE9A42  BE BB 00 00 C0                  mov esi, 0xc00000bb
00AE9A47  E9 AA 00 00 00                  jmp 0x140ae9af6
00AE9A4C  41 B8 44 45 48 4E               mov r8d, 0x4e484544
00AE9A52  48 8B D7                        mov rdx, rdi
00AE9A55  B9 01 01 00 00                  mov ecx, 0x101
00AE9A5A  E8 91 86 09 00                  call 0x140b820f0
00AE9A5F  4C 8B E8                        mov r13, rax
00AE9A62  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00AE9A6A  48 85 C0                        test rax, rax
00AE9A6D  75 0C                           jne 0x140ae9a7b
00AE9A6F  BE 17 00 00 C0                  mov esi, 0xc0000017
00AE9A74  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE9A79  EB 7B                           jmp 0x140ae9af6
00AE9A7B  4C 8B C7                        mov r8, rdi
00AE9A7E  48 8B D3                        mov rdx, rbx
00AE9A81  49 8B CD                        mov rcx, r13
00AE9A84  E8 B7 CD BD FF                  call 0x1406c6840
00AE9A89  90                              nop
00AE9A8A  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
00AE9A8F  44 0F B7 84 24 30 03 00 00      movzx r8d, word ptr [rsp + 0x330]
00AE9A98  49 8B D5                        mov rdx, r13
00AE9A9B  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE9AA0  E8 A3 88 C9 FF                  call 0x140782348
00AE9AA5  8B F0                           mov esi, eax
00AE9AA7  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AE9AAB  44 89 74 24 4C                  mov dword ptr [rsp + 0x4c], r14d
00AE9AB0  44 3B 74 24 60                  cmp r14d, dword ptr [rsp + 0x60]
00AE9AB5  73 BD                           jae 0x140ae9a74
00AE9AB7  41 8B CE                        mov ecx, r14d
00AE9ABA  48 03 C9                        add rcx, rcx
00AE9ABD  49 8B 44 CD 08                  mov rax, qword ptr [r13 + rcx*8 + 8]
00AE9AC2  48 89 44 CB 08                  mov qword ptr [rbx + rcx*8 + 8], rax
00AE9AC7  EB 19                           jmp 0x140ae9ae2
00AE9AC9  8B 74 24 58                     mov esi, dword ptr [rsp + 0x58]
00AE9ACD  44 8B 74 24 4C                  mov r14d, dword ptr [rsp + 0x4c]
00AE9AD2  4C 8B AC 24 88 00 00 00         mov r13, qword ptr [rsp + 0x88]
00AE9ADA  48 8B 9C 24 38 03 00 00         mov rbx, qword ptr [rsp + 0x338]
00AE9AE2  41 FF C6                        inc r14d
00AE9AE5  EB C4                           jmp 0x140ae9aab
00AE9AE7  8B F0                           mov esi, eax
00AE9AE9  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE9AEE  4C 8B AC 24 88 00 00 00         mov r13, qword ptr [rsp + 0x88]
00AE9AF6  48 85 C9                        test rcx, rcx
00AE9AF9  74 05                           je 0x140ae9b00
00AE9AFB  E8 50 F8 80 FF                  call 0x1402f9350
00AE9B00  4D 85 ED                        test r13, r13
00AE9B03  0F 84 A2 BC FF FF               je 0x140ae57ab
00AE9B09  33 D2                           xor edx, edx
00AE9B0B  49 8B CD                        mov rcx, r13
00AE9B0E  E8 5D 8D 09 00                  call 0x140b82870
00AE9B13  8B C6                           mov eax, esi
00AE9B15  E9 A9 04 00 00                  jmp 0x140ae9fc3
00AE9B1A  E9 A4 04 00 00                  jmp 0x140ae9fc3
00AE9B1F  E9 9F 04 00 00                  jmp 0x140ae9fc3
00AE9B24  44 89 74 24 60                  mov dword ptr [rsp + 0x60], r14d
00AE9B29  4D 8B EE                        mov r13, r14
00AE9B2C  83 FF 10                        cmp edi, 0x10
00AE9B2F  0F 85 68 04 00 00               jne 0x140ae9f9d
00AE9B35  0F 10 03                        movups xmm0, xmmword ptr [rbx]
00AE9B38  0F 11 84 24 30 03 00 00         movups xmmword ptr [rsp + 0x330], xmm0
00AE9B40  0F B7 84 24 30 03 00 00         movzx eax, word ptr [rsp + 0x330]
00AE9B48  8D 0C 40                        lea ecx, [rax + rax*2]
00AE9B4B  C1 E1 03                        shl ecx, 3
00AE9B4E  85 C9                           test ecx, ecx
00AE9B50  0F 84 7F F3 FF FF               je 0x140ae8ed5
00AE9B56  48 8B 9C 24 38 03 00 00         mov rbx, qword ptr [rsp + 0x338]
00AE9B5E  48 85 DB                        test rbx, rbx
00AE9B61  0F 84 6E F3 FF FF               je 0x140ae8ed5
00AE9B67  8B F9                           mov edi, ecx
00AE9B69  45 8B C7                        mov r8d, r15d
00AE9B6C  8B D1                           mov edx, ecx
00AE9B6E  48 8B CB                        mov rcx, rbx
00AE9B71  E8 4A F6 DF FF                  call 0x1408e91c0
00AE9B76  90                              nop
00AE9B77  66 83 BC 24 32 03 00 00 00      cmp word ptr [rsp + 0x332], 0
00AE9B80  0F 85 4F F3 FF FF               jne 0x140ae8ed5
00AE9B86  83 BC 24 34 03 00 00 00         cmp dword ptr [rsp + 0x334], 0
00AE9B8E  0F 85 41 F3 FF FF               jne 0x140ae8ed5
00AE9B94  41 80 FC 01                     cmp r12b, 1
00AE9B98  0F 85 92 01 00 00               jne 0x140ae9d30
00AE9B9E  4C 8B 05 F3 CE 4D 00            mov r8, qword ptr [rip + 0x4dcef3]
00AE9BA5  4C 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], r14
00AE9BAD  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00AE9BB2  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AE9BBA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AE9BBF  45 0F B6 CC                     movzx r9d, r12b
00AE9BC3  BA 00 02 00 00                  mov edx, 0x200
00AE9BC8  48 8B CE                        mov rcx, rsi
00AE9BCB  E8 E0 F1 D7 FF                  call 0x140868db0
00AE9BD0  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AE9BD8  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00AE9BDD  85 C0                           test eax, eax
00AE9BDF  0F 88 DE 03 00 00               js 0x140ae9fc3
00AE9BE5  E8 66 19 93 FF                  call 0x14041b550
00AE9BEA  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE9BEF  48 3B C8                        cmp rcx, rax
00AE9BF2  75 16                           jne 0x140ae9c0a
00AE9BF4  F7 81 54 07 00 00 00 00 00 40   test dword ptr [rcx + 0x754], 0x40000000
00AE9BFE  74 0A                           je 0x140ae9c0a
00AE9C00  BE 22 00 00 C0                  mov esi, 0xc0000022
00AE9C05  E9 EC FE FF FF                  jmp 0x140ae9af6
00AE9C0A  F7 81 54 07 00 00 00 40 00 00   test dword ptr [rcx + 0x754], 0x4000
00AE9C14  75 0A                           jne 0x140ae9c20
00AE9C16  BE BB 00 00 C0                  mov esi, 0xc00000bb
00AE9C1B  E9 D6 FE FF FF                  jmp 0x140ae9af6
00AE9C20  41 B8 44 45 41 52               mov r8d, 0x52414544
00AE9C26  48 8B D7                        mov rdx, rdi
00AE9C29  B9 01 01 00 00                  mov ecx, 0x101
00AE9C2E  E8 BD 84 09 00                  call 0x140b820f0
00AE9C33  4C 8B E8                        mov r13, rax
00AE9C36  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00AE9C3E  48 85 C0                        test rax, rax
00AE9C41  75 0F                           jne 0x140ae9c52
00AE9C43  BE 17 00 00 C0                  mov esi, 0xc0000017
00AE9C48  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE9C4D  E9 A4 FE FF FF                  jmp 0x140ae9af6
00AE9C52  4C 8B C7                        mov r8, rdi
00AE9C55  48 8B D3                        mov rdx, rbx
00AE9C58  49 8B CD                        mov rcx, r13
00AE9C5B  E8 E0 CB BD FF                  call 0x1406c6840
00AE9C60  90                              nop
00AE9C61  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE9C66  48 8D 91 90 07 00 00            lea rdx, [rcx + 0x790]
00AE9C6D  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00AE9C72  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AE9C77  44 0F B7 8C 24 30 03 00 00      movzx r9d, word ptr [rsp + 0x330]
00AE9C80  4D 8B C5                        mov r8, r13
00AE9C83  E8 9C 89 C9 FF                  call 0x140782624
00AE9C88  8B F0                           mov esi, eax
00AE9C8A  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AE9C8E  44 89 74 24 4C                  mov dword ptr [rsp + 0x4c], r14d
00AE9C93  44 3B 74 24 60                  cmp r14d, dword ptr [rsp + 0x60]
00AE9C98  73 AE                           jae 0x140ae9c48
00AE9C9A  41 8B CE                        mov ecx, r14d
00AE9C9D  48 8D 04 49                     lea rax, [rcx + rcx*2]
00AE9CA1  48 8D 0C C5 00 00 00 00         lea rcx, [rax*8]
00AE9CA9  42 8B 44 29 10                  mov eax, dword ptr [rcx + r13 + 0x10]
00AE9CAE  89 44 0B 10                     mov dword ptr [rbx + rcx + 0x10], eax
00AE9CB2  EB 19                           jmp 0x140ae9ccd
00AE9CB4  8B 74 24 58                     mov esi, dword ptr [rsp + 0x58]
00AE9CB8  44 8B 74 24 4C                  mov r14d, dword ptr [rsp + 0x4c]
00AE9CBD  4C 8B AC 24 88 00 00 00         mov r13, qword ptr [rsp + 0x88]
00AE9CC5  48 8B 9C 24 38 03 00 00         mov rbx, qword ptr [rsp + 0x338]
00AE9CCD  41 FF C6                        inc r14d
00AE9CD0  EB BC                           jmp 0x140ae9c8e
00AE9CD2  8B F0                           mov esi, eax
00AE9CD4  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE9CD9  4C 8B AC 24 88 00 00 00         mov r13, qword ptr [rsp + 0x88]
00AE9CE1  E9 10 FE FF FF                  jmp 0x140ae9af6
00AE9CE6  E9 D8 02 00 00                  jmp 0x140ae9fc3
00AE9CEB  E9 D3 02 00 00                  jmp 0x140ae9fc3
00AE9CF0  83 FF 08                        cmp edi, 8
00AE9CF3  0F 85 A4 02 00 00               jne 0x140ae9f9d
00AE9CF9  48 8B 1B                        mov rbx, qword ptr [rbx]
00AE9CFC  48 89 9C 24 F8 01 00 00         mov qword ptr [rsp + 0x1f8], rbx
00AE9D04  48 B9 08 07 00 00 80 F7 FF FF   movabs rcx, 0xfffff78000000708
00AE9D0E  48 B8 D8 03 00 00 80 F7 FF FF   movabs rax, 0xfffff780000003d8
00AE9D18  48 8B 09                        mov rcx, qword ptr [rcx]
00AE9D1B  48 0B 08                        or rcx, qword ptr [rax]
00AE9D1E  48 F7 D1                        not rcx
00AE9D21  48 85 CB                        test rbx, rcx
00AE9D24  0F 85 AB F1 FF FF               jne 0x140ae8ed5
00AE9D2A  41 80 FC 01                     cmp r12b, 1
00AE9D2E  74 0A                           je 0x140ae9d3a
00AE9D30  B8 22 00 00 C0                  mov eax, 0xc0000022
00AE9D35  E9 89 02 00 00                  jmp 0x140ae9fc3
00AE9D3A  48 83 FE FF                     cmp rsi, -1
00AE9D3E  74 55                           je 0x140ae9d95
00AE9D40  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE9D45  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE9D4A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE9D4F  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE9D57  41 B1 01                        mov r9b, 1
00AE9D5A  4C 8B 05 37 CD 4D 00            mov r8, qword ptr [rip + 0x4dcd37]
00AE9D61  BA 00 02 00 00                  mov edx, 0x200
00AE9D66  48 8B CE                        mov rcx, rsi
00AE9D69  E8 A2 F8 D7 FF                  call 0x140869610
00AE9D6E  85 C0                           test eax, eax
00AE9D70  0F 88 4D 02 00 00               js 0x140ae9fc3
00AE9D76  BA 50 73 51 79                  mov edx, 0x79517350
00AE9D7B  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE9D80  E8 5B DB 80 FF                  call 0x1402f78e0
00AE9D85  E8 C6 17 93 FF                  call 0x14041b550
00AE9D8A  48 39 44 24 40                  cmp qword ptr [rsp + 0x40], rax
00AE9D8F  0F 85 40 F1 FF FF               jne 0x140ae8ed5
00AE9D95  E8 B6 17 93 FF                  call 0x14041b550
00AE9D9A  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00AE9D9F  48 83 B8 10 03 00 00 00         cmp qword ptr [rax + 0x310], 0
00AE9DA7  0F 85 28 F1 FF FF               jne 0x140ae8ed5
00AE9DAD  48 8B C8                        mov rcx, rax
00AE9DB0  E8 FB EA 92 FF                  call 0x1404188b0
00AE9DB5  84 C0                           test al, al
00AE9DB7  0F 85 FA 01 00 00               jne 0x140ae9fb7
00AE9DBD  48 8B D3                        mov rdx, rbx
00AE9DC0  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE9DC5  E8 26 81 C9 FF                  call 0x140781ef0
00AE9DCA  E9 F4 01 00 00                  jmp 0x140ae9fc3
00AE9DCF  E9 EF 01 00 00                  jmp 0x140ae9fc3
00AE9DD4  45 0F B6 CC                     movzx r9d, r12b
00AE9DD8  44 8B C7                        mov r8d, edi
00AE9DDB  48 8B D3                        mov rdx, rbx
00AE9DDE  48 8B CE                        mov rcx, rsi
00AE9DE1  E8 3E 86 C6 FF                  call 0x140752424
00AE9DE6  E9 D8 01 00 00                  jmp 0x140ae9fc3
00AE9DEB  83 FF 10                        cmp edi, 0x10
00AE9DEE  0F 82 A9 01 00 00               jb 0x140ae9f9d
00AE9DF4  40 F6 C7 07                     test dil, 7
00AE9DF8  0F 85 9F 01 00 00               jne 0x140ae9f9d
00AE9DFE  41 B8 50 73 70 50               mov r8d, 0x50707350
00AE9E04  48 8B D7                        mov rdx, rdi
00AE9E07  B9 01 01 00 00                  mov ecx, 0x101
00AE9E0C  E8 DF 82 09 00                  call 0x140b820f0
00AE9E11  4C 8B F8                        mov r15, rax
00AE9E14  48 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], rax
00AE9E1C  48 85 C0                        test rax, rax
00AE9E1F  75 0A                           jne 0x140ae9e2b
00AE9E21  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00AE9E26  E9 99 00 00 00                  jmp 0x140ae9ec4
00AE9E2B  4C 8B C7                        mov r8, rdi
00AE9E2E  48 8B D3                        mov rdx, rbx
00AE9E31  49 8B CF                        mov rcx, r15
00AE9E34  E8 07 CA BD FF                  call 0x1406c6840
00AE9E39  90                              nop
00AE9E3A  8D 47 F8                        lea eax, [rdi - 8]
00AE9E3D  C1 E8 03                        shr eax, 3
00AE9E40  41 3B 47 04                     cmp eax, dword ptr [r15 + 4]
00AE9E44  72 79                           jb 0x140ae9ebf
00AE9E46  41 F7 07 FE FF FF FF            test dword ptr [r15], 0xfffffffe
00AE9E4D  75 70                           jne 0x140ae9ebf
00AE9E4F  4C 8B 05 42 CC 4D 00            mov r8, qword ptr [rip + 0x4dcc42]
00AE9E56  4C 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], r14
00AE9E5E  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00AE9E63  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AE9E6B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AE9E70  45 0F B6 CC                     movzx r9d, r12b
00AE9E74  BA 00 02 00 00                  mov edx, 0x200
00AE9E79  48 8B CE                        mov rcx, rsi
00AE9E7C  E8 2F EF D7 FF                  call 0x140868db0
00AE9E81  8B D8                           mov ebx, eax
00AE9E83  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AE9E8B  48 89 4C 24 40                  mov qword ptr [rsp + 0x40], rcx
00AE9E90  85 C0                           test eax, eax
00AE9E92  78 30                           js 0x140ae9ec4
00AE9E94  41 0F B6 07                     movzx eax, byte ptr [r15]
00AE9E98  24 01                           and al, 1
00AE9E9A  4D 8D 47 08                     lea r8, [r15 + 8]
00AE9E9E  88 44 24 20                     mov byte ptr [rsp + 0x20], al
00AE9EA2  45 8B 4F 04                     mov r9d, dword ptr [r15 + 4]
00AE9EA6  41 0F B6 D4                     movzx edx, r12b
00AE9EAA  E8 05 A1 C9 FF                  call 0x140783fb4
00AE9EAF  8B D8                           mov ebx, eax
00AE9EB1  EB 11                           jmp 0x140ae9ec4
00AE9EB3  8B D8                           mov ebx, eax
00AE9EB5  4C 8B BC 24 28 01 00 00         mov r15, qword ptr [rsp + 0x128]
00AE9EBD  EB 05                           jmp 0x140ae9ec4
00AE9EBF  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AE9EC4  4D 85 FF                        test r15, r15
00AE9EC7  74 0A                           je 0x140ae9ed3
00AE9EC9  33 D2                           xor edx, edx
00AE9ECB  49 8B CF                        mov rcx, r15
00AE9ECE  E8 9D 89 09 00                  call 0x140b82870
00AE9ED3  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE9ED8  48 85 C9                        test rcx, rcx
00AE9EDB  0F 84 D7 C2 FF FF               je 0x140ae61b8
00AE9EE1  E8 6A F4 80 FF                  call 0x1402f9350
00AE9EE6  8B C3                           mov eax, ebx
00AE9EE8  E9 D6 00 00 00                  jmp 0x140ae9fc3
00AE9EED  83 FF 08                        cmp edi, 8
00AE9EF0  0F 85 A7 00 00 00               jne 0x140ae9f9d
00AE9EF6  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
00AE9EFB  4C 89 74 24 30                  mov qword ptr [rsp + 0x30], r14
00AE9F00  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE9F05  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE9F0A  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE9F12  45 0F B6 CC                     movzx r9d, r12b
00AE9F16  4C 8B 05 7B CB 4D 00            mov r8, qword ptr [rip + 0x4dcb7b]
00AE9F1D  BA 00 02 00 00                  mov edx, 0x200
00AE9F22  48 8B CE                        mov rcx, rsi
00AE9F25  E8 E6 F6 D7 FF                  call 0x140869610
00AE9F2A  8B F8                           mov edi, eax
00AE9F2C  85 C0                           test eax, eax
00AE9F2E  78 36                           js 0x140ae9f66
00AE9F30  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00AE9F35  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE9F3A  E8 9D 86 E9 FF                  call 0x1409825dc
00AE9F3F  8B F8                           mov edi, eax
00AE9F41  85 C0                           test eax, eax
00AE9F43  78 21                           js 0x140ae9f66
00AE9F45  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
00AE9F4A  48 89 03                        mov qword ptr [rbx], rax
00AE9F4D  4C 89 74 24 60                  mov qword ptr [rsp + 0x60], r14
00AE9F52  41 8B FE                        mov edi, r14d
00AE9F55  EB 14                           jmp 0x140ae9f6b
00AE9F57  8B F8                           mov edi, eax
00AE9F59  44 0F B6 64 24 74               movzx r12d, byte ptr [rsp + 0x74]
00AE9F5F  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
00AE9F64  EB 05                           jmp 0x140ae9f6b
00AE9F66  4C 8B 74 24 60                  mov r14, qword ptr [rsp + 0x60]
00AE9F6B  4D 85 F6                        test r14, r14
00AE9F6E  74 0C                           je 0x140ae9f7c
00AE9F70  41 0F B6 D4                     movzx edx, r12b
00AE9F74  49 8B CE                        mov rcx, r14
00AE9F77  E8 F4 78 DB FF                  call 0x1408a1870
00AE9F7C  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE9F81  48 85 C9                        test rcx, rcx
00AE9F84  0F 84 1B BB FF FF               je 0x140ae5aa5
00AE9F8A  BA 50 73 51 79                  mov edx, 0x79517350
00AE9F8F  E8 4C D9 80 FF                  call 0x1402f78e0
00AE9F94  8B C7                           mov eax, edi
00AE9F96  EB 2B                           jmp 0x140ae9fc3
00AE9F98  45 85 C9                        test r9d, r9d
00AE9F9B  74 07                           je 0x140ae9fa4
00AE9F9D  B8 04 00 00 C0                  mov eax, 0xc0000004
00AE9FA2  EB 1F                           jmp 0x140ae9fc3
00AE9FA4  48 83 FE FF                     cmp rsi, -1
00AE9FA8  75 0D                           jne 0x140ae9fb7
00AE9FAA  41 0F B6 CC                     movzx ecx, r12b
00AE9FAE  E8 55 AD 81 FF                  call 0x140304d08
00AE9FB3  33 C0                           xor eax, eax
00AE9FB5  EB 0C                           jmp 0x140ae9fc3
00AE9FB7  B8 BB 00 00 C0                  mov eax, 0xc00000bb
00AE9FBC  EB 05                           jmp 0x140ae9fc3
00AE9FBE  B8 03 00 00 C0                  mov eax, 0xc0000003
00AE9FC3  48 8B 8C 24 C0 04 00 00         mov rcx, qword ptr [rsp + 0x4c0]
00AE9FCB  48 33 CC                        xor rcx, rsp
00AE9FCE  E8 6D 26 BC FF                  call 0x1406ac640
00AE9FD3  48 81 C4 D0 04 00 00            add rsp, 0x4d0
00AE9FDA  41 5F                           pop r15
00AE9FDC  41 5E                           pop r14
00AE9FDE  41 5D                           pop r13
00AE9FE0  41 5C                           pop r12
00AE9FE2  5F                              pop rdi
00AE9FE3  5E                              pop rsi
00AE9FE4  5B                              pop rbx
00AE9FE5  C3                              ret
00AE9FE6  CC                              int3
00AE9FE7  E8 E4 FF DA FF                  call 0x140899fd0
00AE9FEC  90                              nop
00AE9FED  E8 DE FF DA FF                  call 0x140899fd0
00AE9FF2  90                              nop
00AE9FF3  E8 D8 FF DA FF                  call 0x140899fd0
00AE9FF8  90                              nop
00AE9FF9  0F 1F 00                        nop dword ptr [rax]
00AE9FFC  9E                              sahf
00AE9FFD  5E                              pop rsi
00AE9FFE  AE                              scasb al, byte ptr [rdi]
00AE9FFF  00 62 58                        add byte ptr [rdx + 0x58], ah
00AEA002  AE                              scasb al, byte ptr [rdi]
00AEA003  00 76 5D                        add byte ptr [rsi + 0x5d], dh
00AEA006  AE                              scasb al, byte ptr [rdi]
00AEA007  00 B5 5E AE 00 2E               add byte ptr [rbp + 0x2e00ae5e], dh
00AEA00D  61                              .byte 0x61
00AEA00E  AE                              scasb al, byte ptr [rdi]
00AEA00F  00 5B 61                        add byte ptr [rbx + 0x61], bl
00AEA012  AE                              scasb al, byte ptr [rdi]
00AEA013  00 BF 61 AE 00 34               add byte ptr [rdi + 0x3400ae61], bh
00AEA019  5E                              pop rsi
00AEA01A  AE                              scasb al, byte ptr [rdi]
00AEA01B  00 0D 62 AE 00 DA               add byte ptr [rip - 0x25ff519e], cl
00AEA021  56                              push rsi
00AEA022  AE                              scasb al, byte ptr [rdi]
00AEA023  00 5E 62                        add byte ptr [rsi + 0x62], bl
00AEA026  AE                              scasb al, byte ptr [rdi]
00AEA027  00 CB                           add bl, cl
00AEA029  62                              .byte 0x62
00AEA02A  AE                              scasb al, byte ptr [rdi]
00AEA02B  00 4C 59 AE                     add byte ptr [rcx + rbx*2 - 0x52], cl
00AEA02F  00 B4 63 AE 00 6A 64            add byte ptr [rbx + riz*2 + 0x646a00ae], dh
00AEA036  AE                              scasb al, byte ptr [rdi]
00AEA037  00 21                           add byte ptr [rcx], ah
00AEA039  66 AE                           scasb al, byte ptr [rdi]
00AEA03B  00 3B                           add byte ptr [rbx], bh
00AEA03D  67 AE                           scasb al, byte ptr [edi]
00AEA03F  00 D4                           add ah, dl
00AEA041  67 AE                           scasb al, byte ptr [edi]
00AEA043  00 43 5C                        add byte ptr [rbx + 0x5c], al
00AEA046  AE                              scasb al, byte ptr [rdi]
00AEA047  00 6B 68                        add byte ptr [rbx + 0x68], ch
00AEA04A  AE                              scasb al, byte ptr [rdi]
00AEA04B  00 A8 66 AE 00 FF               add byte ptr [rax - 0xff519a], ch
00AEA051  68 AE 00 A7 69                  push 0x69a700ae
00AEA056  AE                              scasb al, byte ptr [rdi]
00AEA057  00 31                           add byte ptr [rcx], dh
00AEA059  6B AE 00 B4 6C AE 00            imul ebp, dword ptr [rsi - 0x51934c00], 0
00AEA060  92                              xchg edx, eax
00AEA061  6B AE 00 42 73 AE 00            imul ebp, dword ptr [rsi - 0x518cbe00], 0
00AEA068  4F 76 AE                        jbe 0x140aea019
00AEA06B  00 42 78                        add byte ptr [rdx + 0x78], al
00AEA06E  AE                              scasb al, byte ptr [rdi]
00AEA06F  00 7D 78                        add byte ptr [rbp + 0x78], bh
00AEA072  AE                              scasb al, byte ptr [rdi]
00AEA073  00 06                           add byte ptr [rsi], al
00AEA075  79 AE                           jns 0x140aea025
00AEA077  00 82 79 AE 00 D0               add byte ptr [rdx - 0x2fff5187], al
00AEA07D  79 AE                           jns 0x140aea02d
00AEA07F  00 01                           add byte ptr [rcx], al
00AEA081  8A AE 00 4A 8A AE               mov ch, byte ptr [rsi - 0x5175b600]
00AEA087  00 E7                           add bh, ah
00AEA089  8A AE 00 47 8C AE               mov ch, byte ptr [rsi - 0x5173b900]
00AEA08F  00 5E 8C                        add byte ptr [rsi - 0x74], bl
00AEA092  AE                              scasb al, byte ptr [rdi]
00AEA093  00 B2 57 AE 00 61               add byte ptr [rdx + 0x6100ae57], dh
00AEA099  8D AE 00 DF 8D AE               lea ebp, [rsi - 0x51722100]
00AEA09F  00 F7                           add bh, dh
00AEA0A1  8E AE 00 4B 90 AE               mov gs, word ptr [rsi - 0x516fb500]
00AEA0A7  00 CB                           add bl, cl
00AEA0A9  90                              nop
00AEA0AA  AE                              scasb al, byte ptr [rdi]
00AEA0AB  00 26                           add byte ptr [rsi], ah
00AEA0AD  91                              xchg ecx, eax
00AEA0AE  AE                              scasb al, byte ptr [rdi]
00AEA0AF  00 9B 91 AE 00 AE               add byte ptr [rbx - 0x51ff516f], bl
00AEA0B5  91                              xchg ecx, eax
00AEA0B6  AE                              scasb al, byte ptr [rdi]
00AEA0B7  00 43 92                        add byte ptr [rbx - 0x6e], al
00AEA0BA  AE                              scasb al, byte ptr [rdi]
00AEA0BB  00 A9 8F AE 00 47               add byte ptr [rcx + 0x4700ae8f], ch
00AEA0C1  93                              xchg ebx, eax
00AEA0C2  AE                              scasb al, byte ptr [rdi]
00AEA0C3  00 B7 9F AE 00 29               add byte ptr [rdi + 0x2900ae9f], dh
00AEA0C9  94                              xchg esp, eax
00AEA0CA  AE                              scasb al, byte ptr [rdi]
00AEA0CB  00 42 95                        add byte ptr [rdx - 0x6b], al
00AEA0CE  AE                              scasb al, byte ptr [rdi]
00AEA0CF  00 DC                           add ah, bl
00AEA0D1  96                              xchg esi, eax
00AEA0D2  AE                              scasb al, byte ptr [rdi]
00AEA0D3  00 F2                           add dl, dh
00AEA0D5  96                              xchg esi, eax
00AEA0D6  AE                              scasb al, byte ptr [rdi]
00AEA0D7  00 7C 97 AE                     add byte ptr [rdi + rdx*4 - 0x52], bh
00AEA0DB  00 33                           add byte ptr [rbx], dh
00AEA0DD  98                              cwde
00AEA0DE  AE                              scasb al, byte ptr [rdi]
00AEA0DF  00 68 77                        add byte ptr [rax + 0x77], ch
00AEA0E2  AE                              scasb al, byte ptr [rdi]
00AEA0E3  00 E4                           add ah, ah
00AEA0E5  77 AE                           ja 0x140aea095
00AEA0E7  00 D1                           add cl, dl
00AEA0E9  98                              cwde
00AEA0EA  AE                              scasb al, byte ptr [rdi]
00AEA0EB  00 53 99                        add byte ptr [rbx - 0x67], dl
00AEA0EE  AE                              scasb al, byte ptr [rdi]
00AEA0EF  00 24 9B                        add byte ptr [rbx + rbx*4], ah
00AEA0F2  AE                              scasb al, byte ptr [rdi]
00AEA0F3  00 F0                           add al, dh
00AEA0F5  9C                              pushfq
00AEA0F6  AE                              scasb al, byte ptr [rdi]
00AEA0F7  00 D4                           add ah, dl
00AEA0F9  9D                              popfq
00AEA0FA  AE                              scasb al, byte ptr [rdi]
00AEA0FB  00 EB                           add bl, ch
00AEA0FD  9D                              popfq
00AEA0FE  AE                              scasb al, byte ptr [rdi]
00AEA0FF  00 B1 5A AE 00 ED               add byte ptr [rcx - 0x12ff51a6], dh
00AEA105  9E                              sahf
00AEA106  AE                              scasb al, byte ptr [rdi]
00AEA107  00 98 9F AE 00 BE               add byte ptr [rax - 0x41ff5161], bl
00AEA10D  9F                              lahf
00AEA10E  AE                              scasb al, byte ptr [rdi]
00AEA10F  00 00                           add byte ptr [rax], al
00AEA111  44 44 44 01 02                  add dword ptr [rdx], r8d
00AEA116  44 03 04 05 06 07 08 44         add r8d, dword ptr [rax + 0x44080706]
00AEA11E  09 0A                           or dword ptr [rdx], ecx
00AEA120  0B 0C 0D 44 0E 0F 10            or ecx, dword ptr [rcx + 0x100f0e44]
00AEA127  11 12                           adc dword ptr [rdx], edx
00AEA129  44 44 44 13 44 14 15            adc r8d, dword ptr [rsp + rdx + 0x15]
00AEA130  16                              .byte 0x16
00AEA131  17                              .byte 0x17
00AEA132  18 44 44 44                     sbb byte ptr [rsp + rax*2 + 0x44], al
00AEA136  19 1A                           sbb dword ptr [rdx], ebx
00AEA138  1B 09                           sbb ecx, dword ptr [rcx]
00AEA13A  44 44 1C 1D                     sbb al, 0x1d
00AEA13E  44                              .byte 0x44
00AEA13F  1E                              .byte 0x1e
00AEA140  1F                              .byte 0x1f
00AEA141  44 44 20 21                     and byte ptr [rcx], r12b
00AEA145  22 44 23 24                     and al, byte ptr [rbx + riz + 0x24]
00AEA149  44 25 44 44 26 27               and eax, 0x27264444
00AEA14F  44 28 29                        sub byte ptr [rcx], r13b
00AEA152  29 2A                           sub dword ptr [rdx], ebp
00AEA154  44 2B 2C 2D 44 2E 44 44         sub r13d, dword ptr [rbp + 0x44442e44]
00AEA15C  2F                              .byte 0x2f
00AEA15D  44 44 30 44 31 32               xor byte ptr [rcx + rsi + 0x32], r8b
00AEA163  44 33 44 34 44                  xor r8d, dword ptr [rsp + rsi + 0x44]
00AEA168  44 35 36 44 44 44               xor eax, 0x44444436
00AEA16E  37                              .byte 0x37
00AEA16F  34 38                           xor al, 0x38
00AEA171  39 3A                           cmp dword ptr [rdx], edi
00AEA173  3B 3C 3D 44 44 3E 3F            cmp edi, dword ptr [rdi + 0x3f3e4444]
00AEA17A  40 41 44 44 44 42 43 0F 1F 00   nop dword ptr [r8]
00AEA184  32 7A AE                        xor bh, byte ptr [rdx - 0x52]
00AEA187  00 A3 7C AE 00 DA               add byte ptr [rbx - 0x25ff5184], ah
00AEA18D  7A AE                           jp 0x140aea13d
00AEA18F  00 73 7B                        add byte ptr [rbx + 0x7b], dh
00AEA192  AE                              scasb al, byte ptr [rdi]
00AEA193  00 F5                           add ch, dh
00AEA195  7C AE                           jl 0x140aea145
00AEA197  00 9B 7F AE 00 EC               add byte ptr [rbx - 0x13ff5181], bl
00AEA19D  7F AE                           jg 0x140aea14d
00AEA19F  00 4E 80                        add byte ptr [rsi - 0x80], cl
00AEA1A2  AE                              scasb al, byte ptr [rdi]
00AEA1A3  00 D5                           add ch, dl
00AEA1A5  82                              .byte 0x82
00AEA1A6  AE                              scasb al, byte ptr [rdi]
00AEA1A7  00 7B 83                        add byte ptr [rbx - 0x7d], bh
00AEA1AA  AE                              scasb al, byte ptr [rdi]
00AEA1AB  00 F5                           add ch, dh
00AEA1AD  7C AE                           jl 0x140aea15d
00AEA1AF  00 F5                           add ch, dh
00AEA1B1  7C AE                           jl 0x140aea161
00AEA1B3  00 A6 84 AE 00 35               add byte ptr [rsi + 0x3500ae84], ah
00AEA1B9  86 AE 00 A7 87 AE               xchg byte ptr [rsi - 0x51785900], ch
00AEA1BF  00                              .byte 0x00
00AEA1C0  A1                              .byte 0xa1
00AEA1C1  85                              .byte 0x85
00AEA1C2  AE                              scasb al, byte ptr [rdi]
00AEA1C3  00                              .byte 0x00
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtSetInformationProcess(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m198;
    unsigned int v_stack_m19C;
    unsigned int v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned int v_stack_m1AC;
    unsigned int v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned int v_stack_m1CC;
    unsigned __int64 v_stack_m1D0;
    unsigned __int16 v_stack_m1D2;
    unsigned __int16 v_stack_m1D4;
    unsigned __int16 v_stack_m1D6;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m2B8;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m2D0;
    unsigned int v_stack_m2D4;
    unsigned __int64 v_stack_m2D8;
    unsigned __int16 v_stack_m2E0;
    unsigned __int64 v_stack_m2E8;
    unsigned int v_stack_m2F0;
    unsigned __int64 v_stack_m2F8;
    unsigned __int64 v_stack_m300;
    unsigned __int64 v_stack_m308;
    unsigned __int64 v_stack_m310;
    unsigned __int64 v_stack_m318;
    unsigned __int64 v_stack_m320;
    unsigned __int64 v_stack_m328;
    unsigned __int64 v_stack_m330;
    unsigned __int64 v_stack_m338;
    unsigned __int64 v_stack_m340;
    unsigned __int64 v_stack_m348;
    unsigned __int64 v_stack_m358;
    unsigned int v_stack_m35C;
    unsigned int v_stack_m360;
    unsigned __int64 v_stack_m368;
    unsigned int v_stack_m36C;
    unsigned int v_stack_m370;
    unsigned __int64 v_stack_m378;
    unsigned __int64 v_stack_m380;
    unsigned __int64 v_stack_m388;
    unsigned __int64 v_stack_m390;
    unsigned int v_stack_m394;
    unsigned int v_stack_m398;
    unsigned int v_stack_m39C;
    unsigned int v_stack_m3A0;
    unsigned int v_stack_m3A4;
    unsigned int v_stack_m3A8;
    unsigned int v_stack_m3AC;
    unsigned int v_stack_m3B0;
    unsigned int v_stack_m3B4;
    unsigned int v_stack_m3B8;
    unsigned __int64 v_stack_m3C0;
    unsigned __int64 v_stack_m3C8;
    unsigned __int64 v_stack_m3D0;
    unsigned __int64 v_stack_m3D8;
    unsigned __int64 v_stack_m3E0;
    unsigned int v_stack_m3E4;
    unsigned int v_stack_m3E8;
    unsigned int v_stack_m3EC;
    unsigned int v_stack_m3F0;
    unsigned __int64 v_stack_m3F8;
    unsigned __int64 v_stack_m400;
    unsigned int v_stack_m404;
    unsigned int v_stack_m408;
    unsigned __int64 v_stack_m410;
    unsigned __int64 v_stack_m418;
    unsigned __int64 v_stack_m420;
    unsigned __int64 v_stack_m428;
    unsigned int v_stack_m430;
    unsigned int v_stack_m434;
    unsigned int v_stack_m438;
    unsigned __int64 v_stack_m440;
    unsigned __int64 v_stack_m448;
    unsigned int v_stack_m450;
    unsigned __int8 v_stack_m451;
    unsigned __int8 v_stack_m452;
    unsigned int v_stack_m454;
    unsigned __int8 v_stack_m456;
    unsigned __int8 v_stack_m457;
    unsigned __int8 v_stack_m458;
    unsigned __int64 v_stack_m460;
    unsigned int v_stack_m468;
    unsigned int v_stack_m46C;
    unsigned __int8 v_stack_m46F;
    unsigned __int16 v_stack_m470;
    unsigned __int64 v_stack_m478;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m480;
    unsigned int v_stack_m488;
    unsigned __int16 v_stack_m490;
    unsigned __int8 v_stack_m494;
    unsigned __int8 v_stack_m497;
    unsigned __int64 v_stack_m4A0;
    unsigned int v_stack_m4A4;
    unsigned __int64 v_stack_m4A8;
    unsigned int v_stack_m4B0;
    unsigned __int8 v_stack_m4B4;
    unsigned __int64 v_stack_m4B8;
    unsigned int v_stack_m4BC;
    unsigned __int8 v_stack_m4C0;
    unsigned __int64 v_stack_m4C8;
    unsigned __int64 v_stack_m4D0;
    unsigned __int64 v_stack_m4D8;
    unsigned __int64 v_stack_m4E0;
    unsigned int v_stack_m4E8;
    unsigned int v_stack_m508;
    unsigned __int8 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;

    v_rsp = (v_rsp) - (0x4D0ULL);
    result = (*(unsigned __int64 *)(v_rip + 3298230)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m468 = (unsigned int)(a2);
    v_stack_m3F8 = a3;
    v_stack_m488 = (unsigned int)((unsigned int)(a4));
    v_r14 = 0;
    v_stack_m4C8 = 0;
    v_stack_m2E8 = v_xmm0;
    v_stack_m4BC = 0;
    v_stack_m470 = 0;
    v_stack_m454 = 0;
    v_stack_m3E0 = 0;
    v_stack_m3D8 = 0;
    v_stack_m388 = 0;
    v_stack_m434 = 0;
    v_stack_m2D8 = v_xmm0;
    v_stack_m490 = 0;
    v_stack_m4A0 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m494 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AE5699;
    if (((unsigned int)(a2)) != 5) goto loc_00AE5443;
    goto loc_00AE5652;
loc_00AE5443:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) == 17) goto loc_00AE55FD;
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) == 25) goto loc_00AE55FD;
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) == 18) goto loc_00AE55FD;
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 108) goto loc_00AE5474;
    goto loc_00AE5652;
loc_00AE5474:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 21) goto loc_00AE5488;
    goto loc_00AE5652;
loc_00AE5488:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 33) goto loc_00AE549B;
    goto loc_00AE5652;
loc_00AE549B:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 39) goto loc_00AE54AE;
    goto loc_00AE5652;
loc_00AE54AE:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 35) goto loc_00AE54C2;
    goto loc_00AE5652;
loc_00AE54C2:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 8) goto loc_00AE54D6;
    goto loc_00AE5652;
loc_00AE54D6:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 40) goto loc_00AE54EA;
    goto loc_00AE5652;
loc_00AE54EA:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 41) goto loc_00AE54FE;
    goto loc_00AE5652;
loc_00AE54FE:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 98) goto loc_00AE5512;
    goto loc_00AE5652;
loc_00AE5512:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 99) goto loc_00AE5526;
    goto loc_00AE5652;
loc_00AE5526:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 45) goto loc_00AE5539;
    goto loc_00AE5652;
loc_00AE5539:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 46) goto loc_00AE554C;
    goto loc_00AE5652;
loc_00AE554C:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 49) goto loc_00AE5560;
    goto loc_00AE5652;
loc_00AE5560:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 53) goto loc_00AE5574;
    goto loc_00AE5652;
loc_00AE5574:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 56) goto loc_00AE5588;
    goto loc_00AE5652;
loc_00AE5588:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 62) goto loc_00AE559C;
    goto loc_00AE5652;
loc_00AE559C:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 65) goto loc_00AE55B0;
    goto loc_00AE5652;
loc_00AE55B0:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) == 70) goto loc_00AE55FD;
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) == 74) goto loc_00AE55FD;
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 83) goto loc_00AE55D0;
    goto loc_00AE5652;
loc_00AE55D0:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) == 90) goto loc_00AE55FD;
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 91) goto loc_00AE55E6;
    goto loc_00AE5652;
loc_00AE55E6:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 95) goto loc_00AE55F7;
    goto loc_00AE5652;
loc_00AE55F7:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 87) goto loc_00AE560C;
loc_00AE55FD:
    goto loc_00AE5658;
loc_00AE560C:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 100) goto loc_00AE561E;
    goto loc_00AE5652;
loc_00AE561E:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 101) goto loc_00AE5629;
    goto loc_00AE5652;
loc_00AE5629:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 102) goto loc_00AE5634;
    goto loc_00AE5652;
loc_00AE5634:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 105) goto loc_00AE563F;
    goto loc_00AE5652;
loc_00AE563F:
    result = 4;
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) != 106) {
        result = 4;
        if (((unsigned int)((unsigned int)((unsigned int)(a2)))) == 107) { result = 8; }
    }
loc_00AE5658:
    if (a4 == 0) goto loc_00AE5688;
    if (((a3) & (result - 1)) != 0) goto loc_00AE9FE7;
    if ((a3 + (unsigned int)(a4) * 1) > v_r13) goto loc_00AE5681;
    if ((a3 + (unsigned int)(a4) * 1) >= a3) goto loc_00AE5692;
loc_00AE5681:
    goto loc_00AE5692;
loc_00AE5688:
loc_00AE5692:
    goto loc_00AE56AD;
loc_00AE5699:
loc_00AE56AD:
    if (((unsigned int)(a2 - 1)) > 112) goto loc_00AE9FBE;
    a2 = ((unsigned int)(*(unsigned int *)(v_rip - 11425474 + *(unsigned __int8 *)(v_rip - 11425474 + a2 - 1 * 1 + 11444496) * 4 + 11444220))) + (v_rip - 11425474);
loc_00AE9FBE:
loc_00AE9FC3:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 1, a4);
    v_rsp = (v_rsp) + (0x4D0ULL);
    return result;
loc_00AE9FE7:
    result = ExRaiseDatatypeMisalignment(a1, a2, 1, a4);
loc_00AE9FED:
    result = ExRaiseDatatypeMisalignment(a1, a2, 1, a4);
loc_00AE9FF3:
    result = ExRaiseDatatypeMisalignment(a1, a2, 1, a4);
loc_00AEA019:
    v_rbx = (unsigned __int8)((a3) + ((unsigned __int8)(a1)));
    result = (unsigned __int8)((result) + ((unsigned __int8)(a2)));
    v_rbp = (unsigned int)((v_rbp) * (*(unsigned int *)(a1 - 1368607744)));
    v_rbp = (unsigned int)((v_rbp) * (*(unsigned int *)(a1 - 1368178176)));
    if (condition_is_below_or_equal) goto loc_00AEA019;
    v_rbx = (unsigned __int8)((v_rbx) + ((unsigned __int8)(result)));
    v_rbx = (unsigned __int8)((v_rbx) + ((unsigned __int8)(a2)));
    v_rbx = (unsigned __int8)((v_rbx) + ((unsigned __int8)(*(unsigned __int8 *)(a1 - 1366538496))));
    result = (unsigned __int8)((result) + ((unsigned __int8)(v_rbx)));
    a2 = (unsigned __int8)((a2) + ((unsigned __int8)(a2)));
    result = (unsigned __int8)((result) + ((unsigned __int8)(result)));
    a1 = (unsigned __int8)((*(unsigned __int8 *)(a1 - 1366538496)) + ((unsigned __int8)(a2)));
    result = (unsigned __int8)((result) + ((unsigned __int8)(a2)));
    result = (unsigned __int8)((result) + ((unsigned __int8)(a2)));
    v_rbx = (unsigned __int8)((v_rbx) + ((unsigned __int8)(a1)));
    a3 = (unsigned int)((1) + (*(unsigned int *)(result * 1 + 1141376774)));
    a1 = (unsigned int)((a1) | (*(unsigned int *)(a1 * 1 + 269422148)));
loc_00AEA145:
    result = (unsigned __int8)((result) & (*(unsigned __int8 *)(v_rbx + v_riz * 1 + 36)));
    result = (unsigned int)((result) & (0x27264444ULL));
    v_r13 = (unsigned int)((v_r13) - (*(unsigned int *)(a1 - 1366434048 * 1 + 1145318980)));
loc_00AEA15D:
    a3 = (unsigned int)((a3) ^ (*(unsigned int *)(v_rsp + a1 * 1 + 68)));
    result = (unsigned int)((result) ^ (0x44444436ULL));
    result = (unsigned __int8)((result) ^ (56));
    v_rbx = (unsigned __int8)((v_rbx) ^ (*(unsigned __int8 *)(a2 - 82)));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a2)));
    if (condition_is_less) goto loc_00AEA145;
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a2)));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a2)));
    if (condition_is_less) goto loc_00AEA15D;
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a2)));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtSetInformationProcess(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m198;
    uint32_t v_stack_m19C;
    uint32_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint32_t v_stack_m1AC;
    uint32_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint32_t v_stack_m1CC;
    uint64_t v_stack_m1D0;
    uint16_t v_stack_m1D2;
    uint16_t v_stack_m1D4;
    uint16_t v_stack_m1D6;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m208;
    uint64_t v_stack_m218;
    uint64_t v_stack_m228;
    uint64_t v_stack_m238;
    uint64_t v_stack_m248;
    uint64_t v_stack_m258;
    uint64_t v_stack_m268;
    uint64_t v_stack_m278;
    uint64_t v_stack_m288;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m2B8;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m2D0;
    uint32_t v_stack_m2D4;
    uint64_t v_stack_m2D8;
    uint16_t v_stack_m2E0;
    uint64_t v_stack_m2E8;
    uint32_t v_stack_m2F0;
    uint64_t v_stack_m2F8;
    uint64_t v_stack_m300;
    uint64_t v_stack_m308;
    uint64_t v_stack_m310;
    uint64_t v_stack_m318;
    uint64_t v_stack_m320;
    uint64_t v_stack_m328;
    uint64_t v_stack_m330;
    uint64_t v_stack_m338;
    uint64_t v_stack_m340;
    uint64_t v_stack_m348;
    uint64_t v_stack_m358;
    uint32_t v_stack_m35C;
    uint32_t v_stack_m360;
    uint64_t v_stack_m368;
    uint32_t v_stack_m36C;
    uint32_t v_stack_m370;
    uint64_t v_stack_m378;
    uint64_t v_stack_m380;
    uint64_t v_stack_m388;
    uint64_t v_stack_m390;
    uint32_t v_stack_m394;
    uint32_t v_stack_m398;
    uint32_t v_stack_m39C;
    uint32_t v_stack_m3A0;
    uint32_t v_stack_m3A4;
    uint32_t v_stack_m3A8;
    uint32_t v_stack_m3AC;
    uint32_t v_stack_m3B0;
    uint32_t v_stack_m3B4;
    uint32_t v_stack_m3B8;
    uint64_t v_stack_m3C0;
    uint64_t v_stack_m3C8;
    uint64_t v_stack_m3D0;
    uint64_t v_stack_m3D8;
    uint64_t v_stack_m3E0;
    uint32_t v_stack_m3E4;
    uint32_t v_stack_m3E8;
    uint32_t v_stack_m3EC;
    uint32_t v_stack_m3F0;
    uint64_t v_stack_m3F8;
    uint64_t v_stack_m400;
    uint32_t v_stack_m404;
    uint32_t v_stack_m408;
    uint64_t v_stack_m410;
    uint64_t v_stack_m418;
    uint64_t v_stack_m420;
    uint64_t v_stack_m428;
    uint32_t v_stack_m430;
    uint32_t v_stack_m434;
    uint32_t v_stack_m438;
    uint64_t v_stack_m440;
    uint64_t v_stack_m448;
    uint32_t v_stack_m450;
    uint8_t v_stack_m451;
    uint8_t v_stack_m452;
    uint32_t v_stack_m454;
    uint8_t v_stack_m456;
    uint8_t v_stack_m457;
    uint8_t v_stack_m458;
    uint64_t v_stack_m460;
    uint32_t v_stack_m468;
    uint32_t v_stack_m46C;
    uint8_t v_stack_m46F;
    uint16_t v_stack_m470;
    uint64_t v_stack_m478;
    uint64_t v_stack_m48;
    uint64_t v_stack_m480;
    uint32_t v_stack_m488;
    uint16_t v_stack_m490;
    uint8_t v_stack_m494;
    uint8_t v_stack_m497;
    uint64_t v_stack_m4A0;
    uint32_t v_stack_m4A4;
    uint64_t v_stack_m4A8;
    uint32_t v_stack_m4B0;
    uint8_t v_stack_m4B4;
    uint64_t v_stack_m4B8;
    uint32_t v_stack_m4BC;
    uint8_t v_stack_m4C0;
    uint64_t v_stack_m4C8;
    uint64_t v_stack_m4D0;
    uint64_t v_stack_m4D8;
    uint64_t v_stack_m4E0;
    uint32_t v_stack_m4E8;
    uint32_t v_stack_m508;
    uint8_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;

    local_rsp = (local_rsp) - (0x4D0ULL);
    result = (*(uint64_t *)(v_rip + 0x3253B6)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m468 = (uint32_t)(Arg2);
    v_stack_m3F8 = Arg3;
    v_stack_m488 = (uint32_t)((uint32_t)(Arg4));
    local_r14 = 0;
    v_stack_m4C8 = 0;
    v_stack_m2E8 = v_xmm0;
    v_stack_m4BC = 0;
    v_stack_m470 = 0;
    v_stack_m454 = 0;
    v_stack_m3E0 = 0;
    v_stack_m3D8 = 0;
    v_stack_m388 = 0;
    v_stack_m434 = 0;
    v_stack_m2D8 = v_xmm0;
    v_stack_m490 = 0;
    v_stack_m4A0 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m494 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AE5699;
    if (((uint32_t)(Arg2)) != 5) goto loc_00AE5443;
    goto loc_00AE5652;
loc_00AE5443:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) == 17) goto loc_00AE55FD;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) == 25) goto loc_00AE55FD;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) == 18) goto loc_00AE55FD;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 108) goto loc_00AE5474;
    goto loc_00AE5652;
loc_00AE5474:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 21) goto loc_00AE5488;
    goto loc_00AE5652;
loc_00AE5488:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 33) goto loc_00AE549B;
    goto loc_00AE5652;
loc_00AE549B:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 39) goto loc_00AE54AE;
    goto loc_00AE5652;
loc_00AE54AE:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 35) goto loc_00AE54C2;
    goto loc_00AE5652;
loc_00AE54C2:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 8) goto loc_00AE54D6;
    goto loc_00AE5652;
loc_00AE54D6:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 40) goto loc_00AE54EA;
    goto loc_00AE5652;
loc_00AE54EA:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 41) goto loc_00AE54FE;
    goto loc_00AE5652;
loc_00AE54FE:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 98) goto loc_00AE5512;
    goto loc_00AE5652;
loc_00AE5512:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 99) goto loc_00AE5526;
    goto loc_00AE5652;
loc_00AE5526:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 45) goto loc_00AE5539;
    goto loc_00AE5652;
loc_00AE5539:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 46) goto loc_00AE554C;
    goto loc_00AE5652;
loc_00AE554C:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 49) goto loc_00AE5560;
    goto loc_00AE5652;
loc_00AE5560:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 53) goto loc_00AE5574;
    goto loc_00AE5652;
loc_00AE5574:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 56) goto loc_00AE5588;
    goto loc_00AE5652;
loc_00AE5588:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 62) goto loc_00AE559C;
    goto loc_00AE5652;
loc_00AE559C:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 65) goto loc_00AE55B0;
    goto loc_00AE5652;
loc_00AE55B0:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) == 70) goto loc_00AE55FD;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) == 74) goto loc_00AE55FD;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 83) goto loc_00AE55D0;
    goto loc_00AE5652;
loc_00AE55D0:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) == 90) goto loc_00AE55FD;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 91) goto loc_00AE55E6;
    goto loc_00AE5652;
loc_00AE55E6:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 95) goto loc_00AE55F7;
    goto loc_00AE5652;
loc_00AE55F7:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 87) goto loc_00AE560C;
loc_00AE55FD:
    goto loc_00AE5658;
loc_00AE560C:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 100) goto loc_00AE561E;
    goto loc_00AE5652;
loc_00AE561E:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 101) goto loc_00AE5629;
    goto loc_00AE5652;
loc_00AE5629:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 102) goto loc_00AE5634;
    goto loc_00AE5652;
loc_00AE5634:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 105) goto loc_00AE563F;
    goto loc_00AE5652;
loc_00AE563F:
    result = 4;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) != 106) {
        result = 4;
        if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) == 107) { result = 8; }
    }
loc_00AE5658:
    if (Arg4 == NULL) goto loc_00AE5688;
    if (((Arg3) & (result - 1)) != 0) goto loc_00AE9FE7;
    if ((Arg3 + (uint32_t)(Arg4) * 1) > local_r13) goto loc_00AE5681;
    if ((Arg3 + (uint32_t)(Arg4) * 1) >= Arg3) goto loc_00AE5692;
loc_00AE5681:
    goto loc_00AE5692;
loc_00AE5688:
loc_00AE5692:
    goto loc_00AE56AD;
loc_00AE5699:
loc_00AE56AD:
    if (((uint32_t)(Arg2 - 1)) > 112) goto loc_00AE9FBE;
    Arg2 = ((uint32_t)(*(uint32_t *)(v_rip - 0xAE56C2 + *(uint8_t *)(v_rip - 0xAE56C2 + Arg2 - 0x1 * 1 + 0xAEA110) * 4 + 0xAE9FFC))) + (v_rip - 11425474);
loc_00AE9FBE:
loc_00AE9FC3:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, 1, Arg4);
    local_rsp = (local_rsp) + (0x4D0ULL);
    return result;
loc_00AE9FE7:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, 1, Arg4);
loc_00AE9FED:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, 1, Arg4);
loc_00AE9FF3:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, 1, Arg4);
loc_00AEA019:
    local_rbx = (uint8_t)((Arg3) + ((uint8_t)(Arg1)));
    result = (uint8_t)((result) + ((uint8_t)(Arg2)));
    local_rbp = (uint32_t)((local_rbp) * (*(uint32_t *)(Arg1 - 0x51934C00)));
    local_rbp = (uint32_t)((local_rbp) * (*(uint32_t *)(Arg1 - 0x518CBE00)));
    if (condition_is_below_or_equal) goto loc_00AEA019;
    local_rbx = (uint8_t)((local_rbx) + ((uint8_t)(result)));
    local_rbx = (uint8_t)((local_rbx) + ((uint8_t)(Arg2)));
    local_rbx = (uint8_t)((local_rbx) + ((uint8_t)(*(uint8_t *)(Arg1 - 0x5173B900))));
    result = (uint8_t)((result) + ((uint8_t)(local_rbx)));
    Arg2 = (uint8_t)((Arg2) + ((uint8_t)(Arg2)));
    result = (uint8_t)((result) + ((uint8_t)(result)));
    Arg1 = (uint8_t)((*(uint8_t *)(Arg1 - 0x5173B900)) + ((uint8_t)(Arg2)));
    result = (uint8_t)((result) + ((uint8_t)(Arg2)));
    result = (uint8_t)((result) + ((uint8_t)(Arg2)));
    local_rbx = (uint8_t)((local_rbx) + ((uint8_t)(Arg1)));
    Arg3 = (uint32_t)((1) + (*(uint32_t *)(result * 1 + 0x44080706)));
    Arg1 = (uint32_t)((Arg1) | (*(uint32_t *)(Arg1 * 1 + 0x100F0E44)));
loc_00AEA145:
    result = (uint8_t)((result) & (*(uint8_t *)(local_rbx + v_riz * 1 + 0x24)));
    result = (uint32_t)((result) & (0x27264444ULL));
    local_r13 = (uint32_t)((local_r13) - (*(uint32_t *)(Arg1 - 0x51722100 * 1 + 0x44442E44)));
loc_00AEA15D:
    Arg3 = (uint32_t)((Arg3) ^ (*(uint32_t *)(local_rsp + Arg1 * 1 + 0x44)));
    result = (uint32_t)((result) ^ (0x44444436ULL));
    result = (uint8_t)((result) ^ (56));
    local_rbx = (uint8_t)((local_rbx) ^ (*(uint8_t *)(Arg2 - 0x52)));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(Arg2)));
    if (condition_is_less) goto loc_00AEA145;
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(Arg2)));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(Arg2)));
    if (condition_is_less) goto loc_00AEA15D;
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(Arg2)));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `- 0x52 + rdx*4` | `8` | `R/W` |
| `Arg4` | `+ 0x0` | `8` | `R` |
| `Arg4` | `+ 0x2900AE9F` | `8` | `R/W` |
| `Arg4` | `+ 0x3400AE61` | `8` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AE5370&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
