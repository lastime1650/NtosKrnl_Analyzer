# PspAllocateProcess

- RVA: `0x00A13B3C`–`0x00A163A8` (길이 `10,348` bytes)
- VA: `0x0000000140A13B3C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9A84`
- 디코드: `2,078`개 명령, `10,348/10,348` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **144**; 고유 호출 대상: **106**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **27**

### Outgoing calls
- `0x00A13C62` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A13D02` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A13DF1` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A13FA3` → [PoEnergyEstimationEnabled](../../text/45/PoEnergyEstimationEnabled_function_00450000.md) (function, `0x00450000`)
- `0x00A13FCC` → [KeQueryMaximumGroupCount](../../text/48/KeQueryMaximumGroupCount_function_0048B760.md) (function, `0x0048B760`)
- `0x00A14026` → [KeSizeOfKProcessExtension](../../text/4B/KeSizeOfKProcessExtension_function_004B794C.md) (function, `0x004B794C`)
- `0x00A14070` → [ObCreateObjectEx](../89/ObCreateObjectEx_function_0089B1E0.md) (function, `0x0089B1E0`)
- `0x00A1408E` → [ObRetagReferences](../9D/ObRetagReferences_function_009DB880.md) (function, `0x009DB880`)
- `0x00A1409B` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A1429E` → [PoEnergyContextInitialize](../A6/PoEnergyContextInitialize_function_00A6E5E4.md) (function, `0x00A6E5E4`)
- `0x00A1432B` → [KeQueryHeteroCpuPolicyThread](../../text/48/KeQueryHeteroCpuPolicyThread_function_00488A70.md) (function, `0x00488A70`)
- `0x00A14377` → [PsReferencePartitionSafe](../../text/3B/PsReferencePartitionSafe_function_003BA6C0.md) (function, `0x003BA6C0`)
- `0x00A143E5` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x00A1441F` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00A14440` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x00A14448` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00A144D3` → [MmGetSectionInformation](../92/MmGetSectionInformation_function_00921910.md) (function, `0x00921910`)
- `0x00A1454D` → [PspUpdateCreateInfo](../AE/PspUpdateCreateInfo_function_00AEC060.md) (function, `0x00AEC060`)
- `0x00A14572` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x00A145A3` → [RtlpOpenImageFileOptionsKeyEx](../A3/RtlpOpenImageFileOptionsKeyEx_function_00A3B8A8.md) (function, `0x00A3B8A8`)
- `0x00A145CE` → [PspSelectMachineForProcess](PspSelectMachineForProcess_function_00A1FFBC.md) (function, `0x00A1FFBC`)
- `0x00A14658` → [RtlQueryImageFileKeyOption](../A2/RtlQueryImageFileKeyOption_function_00A2D110.md) (function, `0x00A2D110`)
- `0x00A146A6` → [RtlQueryImageFileKeyOption](../A2/RtlQueryImageFileKeyOption_function_00A2D110.md) (function, `0x00A2D110`)
- `0x00A146F2` → [RtlQueryImageFileKeyOption](../A2/RtlQueryImageFileKeyOption_function_00A2D110.md) (function, `0x00A2D110`)
- `0x00A14784` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x00A147BC` → [RtlQueryImageFileKeyOption](../A2/RtlQueryImageFileKeyOption_function_00A2D110.md) (function, `0x00A2D110`)
- `0x00A147EC` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x00A14814` → [PspReadIFEONodeOptions](../A2/PspReadIFEONodeOptions_function_00A2CEB8.md) (function, `0x00A2CEB8`)
- `0x00A14842` → [RtlQueryImageFileKeyOption](../A2/RtlQueryImageFileKeyOption_function_00A2D110.md) (function, `0x00A2D110`)
- `0x00A14882` → [RtlQueryImageFileKeyOption](../A2/RtlQueryImageFileKeyOption_function_00A2D110.md) (function, `0x00A2D110`)
- `0x00A148BC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A14900` → [RtlQueryImageFileKeyOption](../A2/RtlQueryImageFileKeyOption_function_00A2D110.md) (function, `0x00A2D110`)
- `0x00A14982` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (function, `0x006AD310`)
- `0x00A1499B` → [PspReadIFEOPerfOptions](../78/PspReadIFEOPerfOptions_function_007845F0.md) (function, `0x007845F0`)
- `0x00A149AA` → [ObCloseHandle](../8A/ObCloseHandle_function_008A1870.md) (function, `0x008A1870`)
- `0x00A149D6` → [RtlQueryImageFileKeyOption](../A2/RtlQueryImageFileKeyOption_function_00A2D110.md) (function, `0x00A2D110`)
- `0x00A14A53` → [MmGetSectionInformation](../92/MmGetSectionInformation_function_00921910.md) (function, `0x00921910`)
- `0x00A14B0B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A14B3D` → [PspWow64PickBestNtdll](../../text/4A/PspWow64PickBestNtdll_function_004A1088.md) (function, `0x004A1088`)
- `0x00A14BA7` → [SeQueryInformationToken](../8B/SeQueryInformationToken_function_008B5090.md) (function, `0x008B5090`)
- `0x00A14C2D` → [PspIsSessionLeaderProcess](../A8/PspIsSessionLeaderProcess_function_00A8F728.md) (function, `0x00A8F728`)
- `0x00A14C89` → [RtlAcquirePrivilege](../87/RtlAcquirePrivilege_function_00879120.md) (function, `0x00879120`)
- `0x00A14CC3` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00A14CE3` → [RtlReleasePrivilege](../A6/RtlReleasePrivilege_function_00A685A0.md) (function, `0x00A685A0`)
- `0x00A14D01` → [PspRundownSingleProcess](../90/PspRundownSingleProcess_function_00906D50.md) (function, `0x00906D50`)
- `0x00A14D0E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00A14D28` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A14D2D` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x00A14D43` → [SeFreeAntiTamperPolicy](../../text/60/SeFreeAntiTamperPolicy_function_006095A0.md) (function, `0x006095A0`)
- `0x00A14D5C` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A14D91` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A14DFA` → [PspSelectNodeForProcess](../A8/PspSelectNodeForProcess_function_00A89BDC.md) (function, `0x00A89BDC`)
- `0x00A14E0A` → [KeSelectGroupFromNode](../../text/49/KeSelectGroupFromNode_function_00491270.md) (function, `0x00491270`)
- `0x00A14E23` → [KeQueryActiveGroupCount](../../text/48/KeQueryActiveGroupCount_function_0048C600.md) (function, `0x0048C600`)
- `0x00A14E5E` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (function, `0x0025B6F0`)
- `0x00A14E6D` → [KeSelectGroupFromNode](../../text/49/KeSelectGroupFromNode_function_00491270.md) (function, `0x00491270`)
- `0x00A14E94` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (function, `0x002CE860`)
- `0x00A14EE4` → [KeSelectNodeForAffinity](../../text/3C/KeSelectNodeForAffinity_function_003C09EC.md) (function, `0x003C09EC`)
- `0x00A14F0E` → [KeQueryAffinityProcess](../../text/2C/KeQueryAffinityProcess_function_002CE710.md) (function, `0x002CE710`)
- `0x00A14F9D` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00A14FC1` → [SeIsTokenAssignableToProcess](../A3/SeIsTokenAssignableToProcess_function_00A3B2C0.md) (function, `0x00A3B2C0`)
- `0x00A14FFB` → [SeQuerySessionIdToken](../A0/SeQuerySessionIdToken_function_00A04490.md) (function, `0x00A04490`)
- `0x00A15012` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x00A15066` → [PspAttachSession](../78/PspAttachSession_function_00788EB0.md) (function, `0x00788EB0`)
- `0x00A15081` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x00A15097` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (function, `0x0022F8F0`)
- `0x00A150D6` → [PspAssignProcessQuotaBlock](../AE/PspAssignProcessQuotaBlock_function_00AE3124.md) (function, `0x00AE3124`)
- `0x00A150FA` → [PspDetachSession](../../text/22/PspDetachSession_function_0022480C.md) (function, `0x0022480C`)
- `0x00A1511E` → [PspInheritQuota](../A6/PspInheritQuota_function_00A6F084.md) (function, `0x00A6F084`)
- `0x00A1517E` → [MmCreateProcessAddressSpace](../A5/MmCreateProcessAddressSpace_function_00A5EE5C.md) (function, `0x00A5EE5C`)
- `0x00A151B0` → [PspDetachSession](../../text/22/PspDetachSession_function_0022480C.md) (function, `0x0022480C`)
- `0x00A151C8` → [PspInheritQuota](../A6/PspInheritQuota_function_00A6F084.md) (function, `0x00A6F084`)
- `0x00A151D4` → [MmInitializeHandBuiltProcess](../7F/MmInitializeHandBuiltProcess_function_007F83EC.md) (function, `0x007F83EC`)
- `0x00A15229` → [PsGetSessionSchedulingGroupByProcess](../A6/PsGetSessionSchedulingGroupByProcess_function_00A6EC60.md) (function, `0x00A6EC60`)
- `0x00A15260` → [KeInitializeProcess](../A6/KeInitializeProcess_function_00A63CF4.md) (function, `0x00A63CF4`)
- `0x00A15306` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00A153B1` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x00A15469` → [PspInitializeProcessSecurity](../AA/PspInitializeProcessSecurity_function_00AAD368.md) (function, `0x00AAD368`)
- `0x00A154D3` → [ObInitProcess](../94/ObInitProcess_function_0094C62C.md) (function, `0x0094C62C`)
- `0x00A154F3` → [MmInitializeHandBuiltProcess2](../AC/MmInitializeHandBuiltProcess2_function_00AC1138.md) (function, `0x00AC1138`)
- `0x00A15522` → [PspApplyIFEOPerfOptions](../78/PspApplyIFEOPerfOptions_function_00783ED8.md) (function, `0x00783ED8`)
- `0x00A15547` → [KeSetCpuSetsProcess](../../text/5C/KeSetCpuSetsProcess_function_005C10D4.md) (function, `0x005C10D4`)
- `0x00A15560` → [KeSetExpectedConcurrencyCountProcess](../../text/5C/KeSetExpectedConcurrencyCountProcess_function_005C1AC0.md) (function, `0x005C1AC0`)
- `0x00A15582` → [PspSetProcessPriorityClass](../9F/PspSetProcessPriorityClass_function_009F61E4.md) (function, `0x009F61E4`)
- `0x00A155A6` → [PspComputeQuantumAndPriority](../A3/PspComputeQuantumAndPriority_function_00A3BFB0.md) (function, `0x00A3BFB0`)
- `0x00A155D2` → [PspReadIFEOMitigationOptions](../A2/PspReadIFEOMitigationOptions_function_00A2CFEC.md) (function, `0x00A2CFEC`)
- `0x00A15631` → [PspInheritMitigationOptions](PspInheritMitigationOptions_function_00A16F64.md) (function, `0x00A16F64`)
- `0x00A15641` → [PspReadIFEOMitigationAuditOptions](../A2/PspReadIFEOMitigationAuditOptions_function_00A2CF64.md) (function, `0x00A2CF64`)
- `0x00A156A0` → [PspInheritMitigationAuditOptions](PspInheritMitigationAuditOptions_function_00A16C84.md) (function, `0x00A16C84`)
- `0x00A15727` → [PspInheritMitigationOptions](PspInheritMitigationOptions_function_00A16F64.md) (function, `0x00A16F64`)
- `0x00A15798` → [PspInheritMitigationAuditOptions](PspInheritMitigationAuditOptions_function_00A16C84.md) (function, `0x00A16C84`)
- `0x00A157C9` → [PspHardenMitigationOptions](../A7/PspHardenMitigationOptions_function_00A78BC0.md) (function, `0x00A78BC0`)
- `0x00A157CE` → [KeIsUserCetAllowed](../../text/4A/KeIsUserCetAllowed_function_004A22B4.md) (function, `0x004A22B4`)
- `0x00A15964` → [KeIsCoreIsolationMitigationPolicyEnforceable](../../text/4A/KeIsCoreIsolationMitigationPolicyEnforceable_function_004A7388.md) (function, `0x004A7388`)
- `0x00A1597F` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x00A159AF` → [PspReadIFEOAntiTamperOptions](../78/PspReadIFEOAntiTamperOptions_function_0078453C.md) (function, `0x0078453C`)
- `0x00A159FA` → [PspApplyMitigationOptions](../A6/PspApplyMitigationOptions_function_00A699AC.md) (function, `0x00A699AC`)
- `0x00A15AFA` → [AppModelPolicy_GetPolicy_Internal](../../text/49/AppModelPolicy_GetPolicy_Internal_function_0049FAEC.md) (function, `0x0049FAEC`)
- `0x00A15B3A` → [SmProcessCreateNotification](../A5/SmProcessCreateNotification_function_00A50B04.md) (function, `0x00A50B04`)
- `0x00A15B4F` → [KeInitializeProcessUserCetLogging](../A9/KeInitializeProcessUserCetLogging_function_00A9D734.md) (function, `0x00A9D734`)
- `0x00A15B70` → [PspIsSessionLeaderProcess](../A8/PspIsSessionLeaderProcess_function_00A8F728.md) (function, `0x00A8F728`)
- `0x00A15B87` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00A15BAC` → [PspInitializeFullProcessImageName](../A4/PspInitializeFullProcessImageName_function_00A4345C.md) (function, `0x00A4345C`)
- `0x00A15BD7` → [MmInitializeProcessAddressSpace](../8C/MmInitializeProcessAddressSpace_function_008CF6B0.md) (function, `0x008CF6B0`)
- `0x00A15BFA` → [MiSectionControlArea](../../text/29/MiSectionControlArea_function_00294CB0.md) (function, `0x00294CB0`)
- `0x00A15C55` → [MmInitializeProcessAddressSpace](../8C/MmInitializeProcessAddressSpace_function_008CF6B0.md) (function, `0x008CF6B0`)
- `0x00A15C81` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A15CAE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00A15D03` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00A15D49` → [RtlReleasePrivilege](../A6/RtlReleasePrivilege_function_00A685A0.md) (function, `0x00A685A0`)
- `0x00A15D80` → [PspSetupReservedUserMappings](../A5/PspSetupReservedUserMappings_function_00A575F0.md) (function, `0x00A575F0`)
- `0x00A15DA6` → [PsQueryProcessAttributes](../9D/PsQueryProcessAttributes_function_009DB630.md) (function, `0x009DB630`)
- `0x00A15E56` → [MmCreatePeb](../98/MmCreatePeb_function_00980FB4.md) (function, `0x00980FB4`)
- `0x00A15EA6` → [PspSetProcessAffinitySafe](../A6/PspSetProcessAffinitySafe_function_00A60904.md) (function, `0x00A60904`)
- `0x00A15EDE` → [PspSetupUserProcessAddressSpace](../AE/PspSetupUserProcessAddressSpace_function_00AEBDC8.md) (function, `0x00AEBDC8`)
- `0x00A15F1E` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x00A15F31` → [MmSecureVirtualMemory](../9F/MmSecureVirtualMemory_function_009F55F0.md) (function, `0x009F55F0`)
- `0x00A16007` → [MmSecureVirtualMemory](../9F/MmSecureVirtualMemory_function_009F55F0.md) (function, `0x009F55F0`)
- `0x00A1609E` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x00A160DD` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x00A160E5` → [KeCopyXfdMaskToPeb](../../text/4B/KeCopyXfdMaskToPeb_function_004B23C4.md) (function, `0x004B23C4`)
- `0x00A160F5` → [PspUpdatePebForAffinityChange](../A5/PspUpdatePebForAffinityChange_function_00A50790.md) (function, `0x00A50790`)
- `0x00A16101` → [MmMapApiSetView](../98/MmMapApiSetView_function_00980E98.md) (function, `0x00980E98`)
- `0x00A1610F` → [PspMapSiloSharedDataView](../A6/PspMapSiloSharedDataView_function_00A6F850.md) (function, `0x00A6F850`)
- `0x00A1611E` → [PspPrepareSystemDllInitBlock](../8C/PspPrepareSystemDllInitBlock_function_008CE128.md) (function, `0x008CE128`)
- `0x00A16135` → [PsWow64GetProcessNtdllType](../8C/PsWow64GetProcessNtdllType_function_008CE464.md) (function, `0x008CE464`)
- `0x00A1613E` → [PspPrepareSystemDllInitBlock](../8C/PspPrepareSystemDllInitBlock_function_008CE128.md) (function, `0x008CE128`)
- `0x00A1614F` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x00A1615C` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x00A16191` → [SeConstructAntiTamperPolicy](../../text/60/SeConstructAntiTamperPolicy_function_0060A094.md) (function, `0x0060A094`)
- `0x00A161D0` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (function, `0x0020FF80`)
- `0x00A161F3` → [SeSetTokenTamperProtection](../../text/60/SeSetTokenTamperProtection_function_00609644.md) (function, `0x00609644`)
- `0x00A1620E` → [ObFastDereferenceObject](../../text/3E/ObFastDereferenceObject_function_003ED5F0.md) (function, `0x003ED5F0`)
- `0x00A16218` → [ObFastDereferenceObject](../../text/3E/ObFastDereferenceObject_function_003ED5F0.md) (function, `0x003ED5F0`)
- `0x00A1622B` → [PspLockProcessExclusive](../../text/46/PspLockProcessExclusive_function_00460164.md) (function, `0x00460164`)
- `0x00A16245` → [ExCreateHandleEx](../86/ExCreateHandleEx_function_0086ACB0.md) (function, `0x0086ACB0`)
- `0x00A16260` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (function, `0x004601C0`)
- `0x00A1628C` → [MmGetSectionStrongImageReference](../70/MmGetSectionStrongImageReference_function_00701DF0.md) (function, `0x00701DF0`)
- `0x00A1629D` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (function, `0x004601C0`)
- `0x00A162E2` → [KeSecureProcess](../../text/5B/KeSecureProcess_function_005B988C.md) (function, `0x005B988C`)
- `0x00A162FA` → [KeQuerySystemTimeUnsafe](../../text/48/KeQuerySystemTimeUnsafe_function_00484438.md) (function, `0x00484438`)
- `0x00A1630B` → [KeQuerySystemTimePrecise](../../text/37/KeQuerySystemTimePrecise_function_0037DA40.md) (function, `0x0037DA40`)
- `0x00A16346` → [KiQueryUnbiasedInterruptTime](../../text/42/KiQueryUnbiasedInterruptTime_function_0042D180.md) (function, `0x0042D180`)
- `0x00A1638F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PsCreateMinimalProcess](../78/PsCreateMinimalProcess_function_00786D14.md) at `0x00786F00`
- [PspCreateProcess](PspCreateProcess_function_00A12758.md) at `0x00A12C00`
- [NtCreateUserProcess](../AE/NtCreateUserProcess_function_00AEA680.md) at `0x00AEB246`

### Static image references
- `0x00A13B51` → RVA `0x00E0A740` (`.data`; read)
- `0x00A13EC9` → RVA `0x00FCF6C0` (`CACHEALI`; read)
- `0x00A13F6E` → RVA `0x00FC6E30` (`ALMOSTRO`; read)
- `0x00A14036` → RVA `0x00FC6A98` (`ALMOSTRO`; read)
- `0x00A1438A` → RVA `0x00FC6EA0` (`ALMOSTRO`; read)
- `0x00A14651` → RVA `0x00B04E80` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A14698` → RVA `0x00B04E40` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A146E4` → RVA `0x00B04F10` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A14756` → RVA `0x00B4BE68` (`PspLargePageDLLKeyName`; read)
- `0x00A147AD` → RVA `0x00B04EF0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A14834` → RVA `0x00B04ED0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A14874` → RVA `0x00B04EB0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A14954` → RVA `0x00B4BE58` (`PspPerfOptionsKeyName`; read)
- `0x00A149C8` → RVA `0x00B04D30` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00A14CBC` → RVA `0x00FD9A78` (`PAGEDATA`; read)
- `0x00A14D48` → RVA `0x00F04F08` (`.data`; read)
- `0x00A14E1A` → RVA `0x00FC6AF2` (`ALMOSTRO`; read)
- `0x00A14E7D` → RVA `0x00FC7120` (`ALMOSTRO`; read)
- `0x00A14F96` → RVA `0x00FD9BC8` (`PAGEDATA`; read)
- `0x00A1513E` → RVA `0x00FD8248` (`PAGEDATA`; read)
- `0x00A152EE` → RVA `0x00F04F00` (`.data`; read)
- `0x00A155F9` → RVA `0x00FC7108` (`ALMOSTRO`; read)
- `0x00A15608` → RVA `0x00FC7118` (`ALMOSTRO`; read)
- `0x00A15668` → RVA `0x00FC7370` (`ALMOSTRO`; read)
- `0x00A15677` → RVA `0x00FC7380` (`ALMOSTRO`; read)
- `0x00A15B80` → RVA `0x00FD9B20` (`PAGEDATA`; read)
- `0x00A16230` → RVA `0x00FC6CA8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **68**
  - `0x00A13C62` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A13D02` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A13DF1` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A13FA3` → [PoEnergyEstimationEnabled](../../text/45/PoEnergyEstimationEnabled_function_00450000.md) (`PAGE` → `.text`)
  - `0x00A13FCC` → [KeQueryMaximumGroupCount](../../text/48/KeQueryMaximumGroupCount_function_0048B760.md) (`PAGE` → `.text`)
  - `0x00A14026` → [KeSizeOfKProcessExtension](../../text/4B/KeSizeOfKProcessExtension_function_004B794C.md) (`PAGE` → `.text`)
  - `0x00A1409B` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A1432B` → [KeQueryHeteroCpuPolicyThread](../../text/48/KeQueryHeteroCpuPolicyThread_function_00488A70.md) (`PAGE` → `.text`)
  - `0x00A14377` → [PsReferencePartitionSafe](../../text/3B/PsReferencePartitionSafe_function_003BA6C0.md) (`PAGE` → `.text`)
  - `0x00A143E5` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x00A1441F` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x00A14440` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x00A14448` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x00A14572` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x00A14784` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x00A148BC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A14982` → [ZwOpenKey](../../text/6A/ZwOpenKey_function_006AD310.md) (`PAGE` → `.text`)
  - `0x00A14B0B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A14B3D` → [PspWow64PickBestNtdll](../../text/4A/PspWow64PickBestNtdll_function_004A1088.md) (`PAGE` → `.text`)
  - `0x00A14D0E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00A14D28` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A14D2D` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (`PAGE` → `.text`)
  - `0x00A14D43` → [SeFreeAntiTamperPolicy](../../text/60/SeFreeAntiTamperPolicy_function_006095A0.md) (`PAGE` → `.text`)
  - `0x00A14D5C` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A14D91` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A14E0A` → [KeSelectGroupFromNode](../../text/49/KeSelectGroupFromNode_function_00491270.md) (`PAGE` → `.text`)
  - `0x00A14E23` → [KeQueryActiveGroupCount](../../text/48/KeQueryActiveGroupCount_function_0048C600.md) (`PAGE` → `.text`)
  - `0x00A14E5E` → [KeAddProcessorAffinityEx](../../text/25/KeAddProcessorAffinityEx_function_0025B6F0.md) (`PAGE` → `.text`)
  - `0x00A14E6D` → [KeSelectGroupFromNode](../../text/49/KeSelectGroupFromNode_function_00491270.md) (`PAGE` → `.text`)
  - `0x00A14E94` → [KiCopyAffinityEx](../../text/2C/KiCopyAffinityEx_function_002CE860.md) (`PAGE` → `.text`)
  - `0x00A14EE4` → [KeSelectNodeForAffinity](../../text/3C/KeSelectNodeForAffinity_function_003C09EC.md) (`PAGE` → `.text`)
  - `0x00A14F0E` → [KeQueryAffinityProcess](../../text/2C/KeQueryAffinityProcess_function_002CE710.md) (`PAGE` → `.text`)
  - `0x00A15012` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x00A15081` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x00A15097` → [PsGetProcessSessionIdEx](../../text/22/PsGetProcessSessionIdEx_function_0022F8F0.md) (`PAGE` → `.text`)
  - `0x00A150FA` → [PspDetachSession](../../text/22/PspDetachSession_function_0022480C.md) (`PAGE` → `.text`)
  - `0x00A151B0` → [PspDetachSession](../../text/22/PspDetachSession_function_0022480C.md) (`PAGE` → `.text`)
  - `0x00A15306` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00A153B1` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (`PAGE` → `.text`)
  - `0x00A15547` → [KeSetCpuSetsProcess](../../text/5C/KeSetCpuSetsProcess_function_005C10D4.md) (`PAGE` → `.text`)
  - `0x00A15560` → [KeSetExpectedConcurrencyCountProcess](../../text/5C/KeSetExpectedConcurrencyCountProcess_function_005C1AC0.md) (`PAGE` → `.text`)
  - `0x00A157CE` → [KeIsUserCetAllowed](../../text/4A/KeIsUserCetAllowed_function_004A22B4.md) (`PAGE` → `.text`)
  - `0x00A15964` → [KeIsCoreIsolationMitigationPolicyEnforceable](../../text/4A/KeIsCoreIsolationMitigationPolicyEnforceable_function_004A7388.md) (`PAGE` → `.text`)
  - `0x00A1597F` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (`PAGE` → `.text`)
  - `0x00A15AFA` → [AppModelPolicy_GetPolicy_Internal](../../text/49/AppModelPolicy_GetPolicy_Internal_function_0049FAEC.md) (`PAGE` → `.text`)
  - `0x00A15BFA` → [MiSectionControlArea](../../text/29/MiSectionControlArea_function_00294CB0.md) (`PAGE` → `.text`)
  - `0x00A15C81` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A15CAE` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00A15D03` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00A15F1E` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x00A1609E` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x00A160DD` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x00A160E5` → [KeCopyXfdMaskToPeb](../../text/4B/KeCopyXfdMaskToPeb_function_004B23C4.md) (`PAGE` → `.text`)
  - `0x00A1614F` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x00A1615C` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (`PAGE` → `.text`)
  - `0x00A16191` → [SeConstructAntiTamperPolicy](../../text/60/SeConstructAntiTamperPolicy_function_0060A094.md) (`PAGE` → `.text`)
  - `0x00A161D0` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (`PAGE` → `.text`)
  - `0x00A161F3` → [SeSetTokenTamperProtection](../../text/60/SeSetTokenTamperProtection_function_00609644.md) (`PAGE` → `.text`)
  - `0x00A1620E` → [ObFastDereferenceObject](../../text/3E/ObFastDereferenceObject_function_003ED5F0.md) (`PAGE` → `.text`)
  - `0x00A16218` → [ObFastDereferenceObject](../../text/3E/ObFastDereferenceObject_function_003ED5F0.md) (`PAGE` → `.text`)
  - `0x00A1622B` → [PspLockProcessExclusive](../../text/46/PspLockProcessExclusive_function_00460164.md) (`PAGE` → `.text`)
  - `0x00A16260` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (`PAGE` → `.text`)
  - `0x00A1629D` → [PspUnlockProcessExclusive](../../text/46/PspUnlockProcessExclusive_function_004601C0.md) (`PAGE` → `.text`)
  - `0x00A162E2` → [KeSecureProcess](../../text/5B/KeSecureProcess_function_005B988C.md) (`PAGE` → `.text`)
  - `0x00A162FA` → [KeQuerySystemTimeUnsafe](../../text/48/KeQuerySystemTimeUnsafe_function_00484438.md) (`PAGE` → `.text`)
  - `0x00A1630B` → [KeQuerySystemTimePrecise](../../text/37/KeQuerySystemTimePrecise_function_0037DA40.md) (`PAGE` → `.text`)
  - `0x00A16346` → [KiQueryUnbiasedInterruptTime](../../text/42/KiQueryUnbiasedInterruptTime_function_0042D180.md) (`PAGE` → `.text`)
  - `0x00A1638F` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A13B3C  4C 8B DC                        mov r11, rsp
00A13B3F  53                              push rbx
00A13B40  56                              push rsi
00A13B41  57                              push rdi
00A13B42  41 54                           push r12
00A13B44  41 55                           push r13
00A13B46  41 56                           push r14
00A13B48  41 57                           push r15
00A13B4A  48 81 EC 30 08 00 00            sub rsp, 0x830
00A13B51  48 8B 05 E8 6B 3F 00            mov rax, qword ptr [rip + 0x3f6be8]
00A13B58  48 33 C4                        xor rax, rsp
00A13B5B  48 89 84 24 20 08 00 00         mov qword ptr [rsp + 0x820], rax
00A13B63  41 8A F9                        mov dil, r9b
00A13B66  4C 89 84 24 28 01 00 00         mov qword ptr [rsp + 0x128], r8
00A13B6E  88 94 24 80 00 00 00            mov byte ptr [rsp + 0x80], dl
00A13B75  4C 8B F1                        mov r14, rcx
00A13B78  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
00A13B80  48 89 8C 24 E8 01 00 00         mov qword ptr [rsp + 0x1e8], rcx
00A13B88  4C 8B A4 24 A0 08 00 00         mov r12, qword ptr [rsp + 0x8a0]
00A13B90  4C 89 A4 24 08 01 00 00         mov qword ptr [rsp + 0x108], r12
00A13B98  48 8B 84 24 A8 08 00 00         mov rax, qword ptr [rsp + 0x8a8]
00A13BA0  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
00A13BA8  4C 8B BC 24 C0 08 00 00         mov r15, qword ptr [rsp + 0x8c0]
00A13BB0  4C 89 BC 24 F0 01 00 00         mov qword ptr [rsp + 0x1f0], r15
00A13BB8  48 8B 8C 24 D0 08 00 00         mov rcx, qword ptr [rsp + 0x8d0]
00A13BC0  48 89 8C 24 48 01 00 00         mov qword ptr [rsp + 0x148], rcx
00A13BC8  48 8B 84 24 D8 08 00 00         mov rax, qword ptr [rsp + 0x8d8]
00A13BD0  48 89 84 24 20 02 00 00         mov qword ptr [rsp + 0x220], rax
00A13BD8  48 8B 84 24 E0 08 00 00         mov rax, qword ptr [rsp + 0x8e0]
00A13BE0  48 89 84 24 38 02 00 00         mov qword ptr [rsp + 0x238], rax
00A13BE8  33 F6                           xor esi, esi
00A13BEA  89 B4 24 6C 01 00 00            mov dword ptr [rsp + 0x16c], esi
00A13BF1  0F 57 C0                        xorps xmm0, xmm0
00A13BF4  0F 11 84 24 60 04 00 00         movups xmmword ptr [rsp + 0x460], xmm0
00A13BFC  0F 11 84 24 70 04 00 00         movups xmmword ptr [rsp + 0x470], xmm0
00A13C04  0F 11 84 24 80 04 00 00         movups xmmword ptr [rsp + 0x480], xmm0
00A13C0C  49 89 B3 C8 FB FF FF            mov qword ptr [r11 - 0x438], rsi
00A13C13  33 C0                           xor eax, eax
00A13C15  89 84 24 AC 07 00 00            mov dword ptr [rsp + 0x7ac], eax
00A13C1C  0F 11 84 24 50 02 00 00         movups xmmword ptr [rsp + 0x250], xmm0
00A13C24  0F 11 84 24 60 02 00 00         movups xmmword ptr [rsp + 0x260], xmm0
00A13C2C  49 89 83 08 FA FF FF            mov qword ptr [r11 - 0x5f8], rax
00A13C33  89 84 24 78 02 00 00            mov dword ptr [rsp + 0x278], eax
00A13C3A  89 B4 24 3C 01 00 00            mov dword ptr [rsp + 0x13c], esi
00A13C41  0F 11 84 24 10 02 00 00         movups xmmword ptr [rsp + 0x210], xmm0
00A13C49  49 89 B3 10 F9 FF FF            mov qword ptr [r11 - 0x6f0], rsi
00A13C50  41 BD 00 01 00 00               mov r13d, 0x100
00A13C56  45 8B C5                        mov r8d, r13d
00A13C59  33 D2                           xor edx, edx
00A13C5B  49 8D 8B 30 FC FF FF            lea rcx, [r11 - 0x3d0]
00A13C62  E8 D9 2F CB FF                  call 0x1406c6c40
00A13C67  8B DE                           mov ebx, esi
00A13C69  89 9C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ebx
00A13C70  89 B4 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], esi
00A13C77  89 B4 24 D0 00 00 00            mov dword ptr [rsp + 0xd0], esi
00A13C7E  0F 57 C0                        xorps xmm0, xmm0
00A13C81  33 C0                           xor eax, eax
00A13C83  0F 11 84 24 00 04 00 00         movups xmmword ptr [rsp + 0x400], xmm0
00A13C8B  48 89 84 24 10 04 00 00         mov qword ptr [rsp + 0x410], rax
00A13C93  0F 57 C9                        xorps xmm1, xmm1
00A13C96  0F 11 8C 24 18 04 00 00         movups xmmword ptr [rsp + 0x418], xmm1
00A13C9E  48 89 84 24 28 04 00 00         mov qword ptr [rsp + 0x428], rax
00A13CA6  40 88 B4 24 95 00 00 00         mov byte ptr [rsp + 0x95], sil
00A13CAE  0F 11 84 24 80 02 00 00         movups xmmword ptr [rsp + 0x280], xmm0
00A13CB6  0F 11 84 24 90 02 00 00         movups xmmword ptr [rsp + 0x290], xmm0
00A13CBE  48 89 84 24 A0 02 00 00         mov qword ptr [rsp + 0x2a0], rax
00A13CC6  89 84 24 A8 02 00 00            mov dword ptr [rsp + 0x2a8], eax
00A13CCD  48 89 B4 24 80 01 00 00         mov qword ptr [rsp + 0x180], rsi
00A13CD5  48 89 B4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rsi
00A13CDD  40 88 B4 24 94 00 00 00         mov byte ptr [rsp + 0x94], sil
00A13CE5  66 89 B4 24 C0 00 00 00         mov word ptr [rsp + 0xc0], si
00A13CED  89 B4 24 AC 00 00 00            mov dword ptr [rsp + 0xac], esi
00A13CF4  33 D2                           xor edx, edx
00A13CF6  44 8D 46 48                     lea r8d, [rsi + 0x48]
00A13CFA  48 8D 8C 24 B0 03 00 00         lea rcx, [rsp + 0x3b0]
00A13D02  E8 39 2F CB FF                  call 0x1406c6c40
00A13D07  89 B4 24 E4 00 00 00            mov dword ptr [rsp + 0xe4], esi
00A13D0E  48 89 B4 24 08 02 00 00         mov qword ptr [rsp + 0x208], rsi
00A13D16  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A13D1F  48 89 84 24 00 02 00 00         mov qword ptr [rsp + 0x200], rax
00A13D27  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
00A13D2E  48 89 84 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rax
00A13D36  48 89 B4 24 60 01 00 00         mov qword ptr [rsp + 0x160], rsi
00A13D3E  48 89 B4 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rsi
00A13D46  48 89 B4 24 90 01 00 00         mov qword ptr [rsp + 0x190], rsi
00A13D4E  48 89 B4 24 F8 01 00 00         mov qword ptr [rsp + 0x1f8], rsi
00A13D56  8B C6                           mov eax, esi
00A13D58  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
00A13D60  48 89 B4 24 A0 01 00 00         mov qword ptr [rsp + 0x1a0], rsi
00A13D68  89 B4 24 C4 00 00 00            mov dword ptr [rsp + 0xc4], esi
00A13D6F  89 B4 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], esi
00A13D76  89 B4 24 B4 00 00 00            mov dword ptr [rsp + 0xb4], esi
00A13D7D  89 B4 24 DC 00 00 00            mov dword ptr [rsp + 0xdc], esi
00A13D84  89 B4 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], esi
00A13D8B  C7 84 24 CC 00 00 00 64 86 00 00  mov dword ptr [rsp + 0xcc], 0x8664
00A13D96  89 B4 24 18 01 00 00            mov dword ptr [rsp + 0x118], esi
00A13D9D  89 B4 24 24 01 00 00            mov dword ptr [rsp + 0x124], esi
00A13DA4  89 B4 24 20 01 00 00            mov dword ptr [rsp + 0x120], esi
00A13DAB  89 B4 24 D4 00 00 00            mov dword ptr [rsp + 0xd4], esi
00A13DB2  48 89 B4 24 C8 01 00 00         mov qword ptr [rsp + 0x1c8], rsi
00A13DBA  89 B4 24 1C 01 00 00            mov dword ptr [rsp + 0x11c], esi
00A13DC1  48 89 B4 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], rsi
00A13DC9  66 89 B4 24 A8 00 00 00         mov word ptr [rsp + 0xa8], si
00A13DD1  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
00A13DD9  48 89 B4 24 B8 01 00 00         mov qword ptr [rsp + 0x1b8], rsi
00A13DE1  33 D2                           xor edx, edx
00A13DE3  41 B8 18 02 00 00               mov r8d, 0x218
00A13DE9  48 8D 8C 24 A0 05 00 00         lea rcx, [rsp + 0x5a0]
00A13DF1  E8 4A 2E CB FF                  call 0x1406c6c40
00A13DF6  8B 8C 24 B0 08 00 00            mov ecx, dword ptr [rsp + 0x8b0]
00A13DFD  89 8C 24 90 00 00 00            mov dword ptr [rsp + 0x90], ecx
00A13E04  0F BA E1 0B                     bt ecx, 0xb
00A13E08  73 29                           jae 0x140a13e33
00A13E0A  8D 5E 02                        lea ebx, [rsi + 2]
00A13E0D  89 9C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ebx
00A13E14  0F BA E1 0D                     bt ecx, 0xd
00A13E18  73 3B                           jae 0x140a13e55
00A13E1A  8D 5E 06                        lea ebx, [rsi + 6]
00A13E1D  89 9C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ebx
00A13E24  44 8D 66 01                     lea r12d, [rsi + 1]
00A13E28  0F BA E1 0E                     bt ecx, 0xe
00A13E2C  73 2D                           jae 0x140a13e5b
00A13E2E  8D 5E 0E                        lea ebx, [rsi + 0xe]
00A13E31  EB 19                           jmp 0x140a13e4c
00A13E33  4D 85 E4                        test r12, r12
00A13E36  75 1D                           jne 0x140a13e55
00A13E38  49 8B C6                        mov rax, r14
00A13E3B  48 F7 D8                        neg rax
00A13E3E  1B DB                           sbb ebx, ebx
00A13E40  83 E3 03                        and ebx, 3
00A13E43  41 BC 01 00 00 00               mov r12d, 1
00A13E49  41 03 DC                        add ebx, r12d
00A13E4C  89 9C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ebx
00A13E53  EB 06                           jmp 0x140a13e5b
00A13E55  41 BC 01 00 00 00               mov r12d, 1
00A13E5B  F6 C3 04                        test bl, 4
00A13E5E  74 29                           je 0x140a13e89
00A13E60  39 B4 24 C8 08 00 00            cmp dword ptr [rsp + 0x8c8], esi
00A13E67  74 09                           je 0x140a13e72
00A13E69  F6 C3 02                        test bl, 2
00A13E6C  0F 84 0D 25 00 00               je 0x140a1637f
00A13E72  41 F7 86 FC 05 00 00 00 10 00 00  test dword ptr [r14 + 0x5fc], 0x1000
00A13E7D  74 14                           je 0x140a13e93
00A13E7F  B8 0D 00 00 C0                  mov eax, 0xc000000d
00A13E84  E9 FB 24 00 00                  jmp 0x140a16384
00A13E89  0F BA E1 0C                     bt ecx, 0xc
00A13E8D  0F 82 EC 24 00 00               jb 0x140a1637f
00A13E93  8B C1                           mov eax, ecx
00A13E95  41 23 C5                        and eax, r13d
00A13E98  F7 D8                           neg eax
00A13E9A  48 1B C9                        sbb rcx, rcx
00A13E9D  49 23 CE                        and rcx, r14
00A13EA0  48 89 8C 24 40 01 00 00         mov qword ptr [rsp + 0x140], rcx
00A13EA8  4D 85 FF                        test r15, r15
00A13EAB  74 39                           je 0x140a13ee6
00A13EAD  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
00A13EB1  48 0F BA E0 0D                  bt rax, 0xd
00A13EB6  73 2E                           jae 0x140a13ee6
00A13EB8  48 85 C9                        test rcx, rcx
00A13EBB  0F 85 BE 24 00 00               jne 0x140a1637f
00A13EC1  41 0F B7 87 AA 00 00 00         movzx eax, word ptr [r15 + 0xaa]
00A13EC9  48 8D 15 F0 B7 5B 00            lea rdx, [rip + 0x5bb7f0]
00A13ED0  48 8B 04 C2                     mov rax, qword ptr [rdx + rax*8]
00A13ED4  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
00A13EDC  48 89 8C 24 40 01 00 00         mov qword ptr [rsp + 0x140], rcx
00A13EE4  EB 2D                           jmp 0x140a13f13
00A13EE6  4D 85 F6                        test r14, r14
00A13EE9  74 28                           je 0x140a13f13
00A13EEB  48 89 8C 24 40 01 00 00         mov qword ptr [rsp + 0x140], rcx
00A13EF3  41 F7 86 F0 01 00 00 00 00 20 00  test dword ptr [r14 + 0x1f0], 0x200000
00A13EFE  74 13                           je 0x140a13f13
00A13F00  4C 89 B4 24 40 01 00 00         mov qword ptr [rsp + 0x140], r14
00A13F08  C7 84 24 B4 00 00 00 00 00 20 00  mov dword ptr [rsp + 0xb4], 0x200000
00A13F13  4D 85 FF                        test r15, r15
00A13F16  74 1B                           je 0x140a13f33
00A13F18  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
00A13F1C  48 0F BA E0 12                  bt rax, 0x12
00A13F21  73 10                           jae 0x140a13f33
00A13F23  0F BA EB 10                     bts ebx, 0x10
00A13F27  89 9C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ebx
00A13F2E  41 80 67 10 EF                  and byte ptr [r15 + 0x10], 0xef
00A13F33  0F 57 C0                        xorps xmm0, xmm0
00A13F36  33 C0                           xor eax, eax
00A13F38  0F 11 84 24 38 04 00 00         movups xmmword ptr [rsp + 0x438], xmm0
00A13F40  0F 11 84 24 48 04 00 00         movups xmmword ptr [rsp + 0x448], xmm0
00A13F48  48 89 84 24 58 04 00 00         mov qword ptr [rsp + 0x458], rax
00A13F50  48 89 B4 24 98 01 00 00         mov qword ptr [rsp + 0x198], rsi
00A13F58  BA 40 08 00 00                  mov edx, 0x840
00A13F5D  8B CA                           mov ecx, edx
00A13F5F  89 B4 24 30 01 00 00            mov dword ptr [rsp + 0x130], esi
00A13F66  48 89 B4 24 D0 01 00 00         mov qword ptr [rsp + 0x1d0], rsi
00A13F6E  39 05 BC 2E 5B 00               cmp dword ptr [rip + 0x5b2ebc], eax
00A13F74  75 16                           jne 0x140a13f8c
00A13F76  8D 4A 28                        lea ecx, [rdx + 0x28]
00A13F79  0F BA EB 0F                     bts ebx, 0xf
00A13F7D  89 9C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ebx
00A13F84  48 89 94 24 D0 01 00 00         mov qword ptr [rsp + 0x1d0], rdx
00A13F8C  8D 41 07                        lea eax, [rcx + 7]
00A13F8F  41 BD F8 FF FF FF               mov r13d, 0xfffffff8
00A13F95  41 23 C5                        and eax, r13d
00A13F98  89 84 24 70 01 00 00            mov dword ptr [rsp + 0x170], eax
00A13F9F  44 8D 70 10                     lea r14d, [rax + 0x10]
00A13FA3  E8 58 C0 A3 FF                  call 0x140450000
00A13FA8  84 C0                           test al, al
00A13FAA  74 20                           je 0x140a13fcc
00A13FAC  41 8D 46 07                     lea eax, [r14 + 7]
00A13FB0  41 23 C5                        and eax, r13d
00A13FB3  89 84 24 30 01 00 00            mov dword ptr [rsp + 0x130], eax
00A13FBA  44 8D B0 E8 01 00 00            lea r14d, [rax + 0x1e8]
00A13FC1  0F BA EB 11                     bts ebx, 0x11
00A13FC5  89 9C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ebx
00A13FCC  E8 8F 77 A7 FF                  call 0x14048b760
00A13FD1  66 89 84 24 F0 00 00 00         mov word ptr [rsp + 0xf0], ax
00A13FD9  44 8B EE                        mov r13d, esi
00A13FDC  66 41 3B C4                     cmp ax, r12w
00A13FE0  76 14                           jbe 0x140a13ff6
00A13FE2  41 83 C6 07                     add r14d, 7
00A13FE6  41 83 E6 F8                     and r14d, 0xfffffff8
00A13FEA  45 8B EE                        mov r13d, r14d
00A13FED  0F B7 C8                        movzx ecx, ax
00A13FF0  C1 E1 04                        shl ecx, 4
00A13FF3  44 03 F1                        add r14d, ecx
00A13FF6  8B CE                           mov ecx, esi
00A13FF8  89 8C 24 F8 00 00 00            mov dword ptr [rsp + 0xf8], ecx
00A13FFF  F7 C3 02 00 01 00               test ebx, 0x10002
00A14005  75 17                           jne 0x140a1401e
00A14007  48 39 B4 24 98 00 00 00         cmp qword ptr [rsp + 0x98], rsi
00A1400F  B8 04 00 00 00                  mov eax, 4
00A14014  0F 45 C8                        cmovne ecx, eax
00A14017  89 8C 24 F8 00 00 00            mov dword ptr [rsp + 0xf8], ecx
00A1401E  45 8D 66 07                     lea r12d, [r14 + 7]
00A14022  41 83 E4 F8                     and r12d, 0xfffffff8
00A14026  E8 21 39 AA FF                  call 0x1404b794c
00A1402B  44 89 A4 24 68 01 00 00         mov dword ptr [rsp + 0x168], r12d
00A14033  44 03 E0                        add r12d, eax
00A14036  48 8B 15 5B 2A 5B 00            mov rdx, qword ptr [rip + 0x5b2a5b]
00A1403D  48 89 74 24 48                  mov qword ptr [rsp + 0x48], rsi
00A14042  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
00A1404A  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00A1404F  44 89 64 24 38                  mov dword ptr [rsp + 0x38], r12d
00A14054  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
00A14058  44 89 64 24 28                  mov dword ptr [rsp + 0x28], r12d
00A1405D  44 8A 8C 24 80 00 00 00         mov r9b, byte ptr [rsp + 0x80]
00A14065  4C 8B 84 24 28 01 00 00         mov r8, qword ptr [rsp + 0x128]
00A1406D  41 8A C9                        mov cl, r9b
00A14070  E8 6B 71 E8 FF                  call 0x14089b1e0
00A14075  85 C0                           test eax, eax
00A14077  0F 88 07 23 00 00               js 0x140a16384
00A1407D  41 B8 50 73 43 72               mov r8d, 0x72437350
00A14083  4C 8B B4 24 A0 00 00 00         mov r14, qword ptr [rsp + 0xa0]
00A1408B  49 8B CE                        mov rcx, r14
00A1408E  E8 ED 77 FC FF                  call 0x1409db880
00A14093  45 8B C4                        mov r8d, r12d
00A14096  33 D2                           xor edx, edx
00A14098  49 8B CE                        mov rcx, r14
00A1409B  E8 A0 2B CB FF                  call 0x1406c6c40
00A140A0  0F 57 C0                        xorps xmm0, xmm0
00A140A3  41 0F 11 86 80 05 00 00         movups xmmword ptr [r14 + 0x580], xmm0
00A140AB  41 0F 11 86 90 05 00 00         movups xmmword ptr [r14 + 0x590], xmm0
00A140B3  49 89 B6 80 05 00 00            mov qword ptr [r14 + 0x580], rsi
00A140BA  49 8D 86 88 05 00 00            lea rax, [r14 + 0x588]
00A140C1  48 89 40 08                     mov qword ptr [rax + 8], rax
00A140C5  48 89 00                        mov qword ptr [rax], rax
00A140C8  49 89 B6 E8 01 00 00            mov qword ptr [r14 + 0x1e8], rsi
00A140CF  49 89 B6 C8 01 00 00            mov qword ptr [r14 + 0x1c8], rsi
00A140D6  49 8D 86 70 03 00 00            lea rax, [r14 + 0x370]
00A140DD  48 89 40 08                     mov qword ptr [rax + 8], rax
00A140E1  48 89 00                        mov qword ptr [rax], rax
00A140E4  49 8D 86 20 06 00 00            lea rax, [r14 + 0x620]
00A140EB  48 89 40 08                     mov qword ptr [rax + 8], rax
00A140EF  48 89 00                        mov qword ptr [rax], rax
00A140F2  49 8D 86 10 07 00 00            lea rax, [r14 + 0x710]
00A140F9  48 89 40 08                     mov qword ptr [rax + 8], rax
00A140FD  48 89 00                        mov qword ptr [rax], rax
00A14100  41 88 BE FA 05 00 00            mov byte ptr [r14 + 0x5fa], dil
00A14107  8A 84 24 90 08 00 00            mov al, byte ptr [rsp + 0x890]
00A1410E  41 88 86 F8 05 00 00            mov byte ptr [r14 + 0x5f8], al
00A14115  8A 84 24 98 08 00 00            mov al, byte ptr [rsp + 0x898]
00A1411C  41 88 86 F9 05 00 00            mov byte ptr [r14 + 0x5f9], al
00A14123  B8 01 00 00 00                  mov eax, 1
00A14128  49 89 86 28 08 00 00            mov qword ptr [r14 + 0x828], rax
00A1412F  49 89 B6 58 06 00 00            mov qword ptr [r14 + 0x658], rsi
00A14136  49 89 B6 88 07 00 00            mov qword ptr [r14 + 0x788], rsi
00A1413D  49 89 B6 80 07 00 00            mov qword ptr [r14 + 0x780], rsi
00A14144  49 89 B6 98 07 00 00            mov qword ptr [r14 + 0x798], rsi
00A1414B  49 89 B6 90 07 00 00            mov qword ptr [r14 + 0x790], rsi
00A14152  49 89 B6 A8 07 00 00            mov qword ptr [r14 + 0x7a8], rsi
00A14159  49 89 B6 18 08 00 00            mov qword ptr [r14 + 0x818], rsi
00A14160  F6 C3 02                        test bl, 2
00A14163  74 07                           je 0x140a1416c
00A14165  41 09 86 FC 05 00 00            or dword ptr [r14 + 0x5fc], eax
00A1416C  44 8B 84 24 90 00 00 00         mov r8d, dword ptr [rsp + 0x90]
00A14174  41 0F BA E0 0F                  bt r8d, 0xf
00A14179  73 15                           jae 0x140a14190
00A1417B  B8 20 00 00 00                  mov eax, 0x20
00A14180  89 84 24 28 01 00 00            mov dword ptr [rsp + 0x128], eax
00A14187  41 09 86 FC 05 00 00            or dword ptr [r14 + 0x5fc], eax
00A1418E  EB 0B                           jmp 0x140a1419b
00A14190  C7 84 24 28 01 00 00 20 00 00 00  mov dword ptr [rsp + 0x128], 0x20
00A1419B  BF 04 00 00 00                  mov edi, 4
00A141A0  41 0F BA E0 13                  bt r8d, 0x13
00A141A5  73 20                           jae 0x140a141c7
00A141A7  F0 41 09 BE DC 07 00 00         lock or dword ptr [r14 + 0x7dc], edi
00A141AF  44 8B 84 24 B0 08 00 00         mov r8d, dword ptr [rsp + 0x8b0]
00A141B7  44 89 84 24 90 00 00 00         mov dword ptr [rsp + 0x90], r8d
00A141BF  4C 8B B4 24 A0 00 00 00         mov r14, qword ptr [rsp + 0xa0]
00A141C7  45 85 ED                        test r13d, r13d
00A141CA  74 29                           je 0x140a141f5
00A141CC  41 0F BA AE FC 05 00 00 07      bts dword ptr [r14 + 0x5fc], 7
00A141D5  41 8B CD                        mov ecx, r13d
00A141D8  49 03 CE                        add rcx, r14
00A141DB  49 89 8E C8 06 00 00            mov qword ptr [r14 + 0x6c8], rcx
00A141E2  0F B7 84 24 F0 00 00 00         movzx eax, word ptr [rsp + 0xf0]
00A141EA  48 8D 0C C1                     lea rcx, [rcx + rax*8]
00A141EE  49 89 8E D0 06 00 00            mov qword ptr [r14 + 0x6d0], rcx
00A141F5  8B 84 24 B8 08 00 00            mov eax, dword ptr [rsp + 0x8b8]
00A141FC  41 BD 01 00 00 00               mov r13d, 1
00A14202  41 84 C5                        test r13b, al
00A14205  74 09                           je 0x140a14210
00A14207  41 0F BA AE FC 05 00 00 0C      bts dword ptr [r14 + 0x5fc], 0xc
00A14210  40 84 C7                        test dil, al
00A14213  74 09                           je 0x140a1421e
00A14215  41 0F BA AE FC 05 00 00 17      bts dword ptr [r14 + 0x5fc], 0x17
00A1421E  A8 08                           test al, 8
00A14220  74 09                           je 0x140a1422b
00A14222  41 0F BA AE FC 05 00 00 1B      bts dword ptr [r14 + 0x5fc], 0x1b
00A1422B  A8 10                           test al, 0x10
00A1422D  74 09                           je 0x140a14238
00A1422F  41 0F BA AE FC 05 00 00 1E      bts dword ptr [r14 + 0x5fc], 0x1e
00A14238  48 8B 94 24 E8 00 00 00         mov rdx, qword ptr [rsp + 0xe8]
00A14240  48 8B 92 D0 01 00 00            mov rdx, qword ptr [rdx + 0x1d0]
00A14247  48 8B C2                        mov rax, rdx
00A1424A  48 83 C8 02                     or rax, 2
00A1424E  41 0F BA E0 09                  bt r8d, 9
00A14253  48 0F 42 C2                     cmovb rax, rdx
00A14257  49 89 86 D8 02 00 00            mov qword ptr [r14 + 0x2d8], rax
00A1425E  0F BA E3 0F                     bt ebx, 0xf
00A14262  73 12                           jae 0x140a14276
00A14264  48 8B 84 24 D0 01 00 00         mov rax, qword ptr [rsp + 0x1d0]
00A1426C  49 03 C6                        add rax, r14
00A1426F  49 89 86 38 06 00 00            mov qword ptr [r14 + 0x638], rax
00A14276  8B 84 24 70 01 00 00            mov eax, dword ptr [rsp + 0x170]
00A1427D  49 03 C6                        add rax, r14
00A14280  49 89 86 F0 07 00 00            mov qword ptr [r14 + 0x7f0], rax
00A14287  0F BA E3 11                     bt ebx, 0x11
00A1428B  73 16                           jae 0x140a142a3
00A1428D  8B 8C 24 30 01 00 00            mov ecx, dword ptr [rsp + 0x130]
00A14294  49 03 CE                        add rcx, r14
00A14297  49 89 8E 68 06 00 00            mov qword ptr [r14 + 0x668], rcx
00A1429E  E8 41 A3 05 00                  call 0x140a6e5e4
00A142A3  4D 85 FF                        test r15, r15
00A142A6  74 1C                           je 0x140a142c4
00A142A8  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
00A142AC  48 0F BA E0 09                  bt rax, 9
00A142B1  73 11                           jae 0x140a142c4
00A142B3  41 8B 87 3C 01 00 00            mov eax, dword ptr [r15 + 0x13c]
00A142BA  4C 8B A4 24 98 00 00 00         mov r12, qword ptr [rsp + 0x98]
00A142C2  EB 1C                           jmp 0x140a142e0
00A142C4  4C 8B A4 24 98 00 00 00         mov r12, qword ptr [rsp + 0x98]
00A142CC  4D 85 E4                        test r12, r12
00A142CF  74 0A                           je 0x140a142db
00A142D1  41 8B 84 24 88 03 00 00         mov eax, dword ptr [r12 + 0x388]
00A142D9  EB 05                           jmp 0x140a142e0
00A142DB  B8 05 00 00 00                  mov eax, 5
00A142E0  41 89 86 88 03 00 00            mov dword ptr [r14 + 0x388], eax
00A142E7  41 C7 86 54 05 00 00 03 01 00 00  mov dword ptr [r14 + 0x554], 0x103
00A142F2  4D 85 E4                        test r12, r12
00A142F5  74 2F                           je 0x140a14326
00A142F7  41 8B 94 24 F4 01 00 00         mov edx, dword ptr [r12 + 0x1f4]
00A142FF  C1 EA 1B                        shr edx, 0x1b
00A14302  83 E2 07                        and edx, 7
00A14305  45 8B 84 24 F0 01 00 00         mov r8d, dword ptr [r12 + 0x1f0]
00A1430D  41 C1 E8 0C                     shr r8d, 0xc
00A14311  41 83 E0 07                     and r8d, 7
00A14315  49 8B 84 24 D0 01 00 00         mov rax, qword ptr [r12 + 0x1d0]
00A1431D  49 89 86 D0 02 00 00            mov qword ptr [r14 + 0x2d0], rax
00A14324  EB 0D                           jmp 0x140a14333
00A14326  BA 02 00 00 00                  mov edx, 2
00A1432B  E8 40 47 A7 FF                  call 0x140488a70
00A14330  44 8B C0                        mov r8d, eax
00A14333  C1 E2 1B                        shl edx, 0x1b
00A14336  41 8B 8E F4 01 00 00            mov ecx, dword ptr [r14 + 0x1f4]
00A1433D  81 E1 FF FF FF C7               and ecx, 0xc7ffffff
00A14343  0B D1                           or edx, ecx
00A14345  41 89 96 F4 01 00 00            mov dword ptr [r14 + 0x1f4], edx
00A1434C  41 8B 8E F0 01 00 00            mov ecx, dword ptr [r14 + 0x1f0]
00A14353  81 E1 FF 8F FF FF               and ecx, 0xffff8fff
00A14359  41 C1 E0 0C                     shl r8d, 0xc
00A1435D  41 0B C8                        or ecx, r8d
00A14360  41 89 8E F0 01 00 00            mov dword ptr [r14 + 0x1f0], ecx
00A14367  48 8B 84 24 48 01 00 00         mov rax, qword ptr [rsp + 0x148]
00A1436F  48 85 C0                        test rax, rax
00A14372  74 16                           je 0x140a1438a
00A14374  48 8B C8                        mov rcx, rax
00A14377  E8 44 63 9A FF                  call 0x1403ba6c0
00A1437C  84 C0                           test al, al
00A1437E  75 49                           jne 0x140a143c9
00A14380  BF A0 04 00 C0                  mov edi, 0xc00004a0
00A14385  E9 5E 09 00 00                  jmp 0x140a14ce8
00A1438A  48 8B 15 0F 2B 5B 00            mov rdx, qword ptr [rip + 0x5b2b0f]
00A14391  48 89 94 24 48 01 00 00         mov qword ptr [rsp + 0x148], rdx
00A14399  49 8B C5                        mov rax, r13
00A1439C  F0 48 0F C1 42 28               lock xadd qword ptr [rdx + 0x28], rax
00A143A2  49 03 C5                        add rax, r13
00A143A5  49 3B C5                        cmp rax, r13
00A143A8  7F 07                           jg 0x140a143b1
00A143AA  B9 0E 00 00 00                  mov ecx, 0xe
00A143AF  CD 29                           int 0x29
00A143B1  8B 84 24 B0 08 00 00            mov eax, dword ptr [rsp + 0x8b0]
00A143B8  89 84 24 90 00 00 00            mov dword ptr [rsp + 0x90], eax
00A143BF  4C 8B B4 24 A0 00 00 00         mov r14, qword ptr [rsp + 0xa0]
00A143C7  EB 08                           jmp 0x140a143d1
00A143C9  48 8B 94 24 48 01 00 00         mov rdx, qword ptr [rsp + 0x148]
00A143D1  49 89 96 58 07 00 00            mov qword ptr [r14 + 0x758], rdx
00A143D8  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
00A143E0  48 85 C9                        test rcx, rcx
00A143E3  74 0D                           je 0x140a143f2
00A143E5  E8 36 B6 7F FF                  call 0x14020fa20
00A143EA  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
00A143F2  40 84 DF                        test dil, bl
00A143F5  0F 84 A8 00 00 00               je 0x140a144a3
00A143FB  41 0F B7 84 24 EC 06 00 00      movzx eax, word ptr [r12 + 0x6ec]
00A14404  89 84 24 CC 00 00 00            mov dword ptr [rsp + 0xcc], eax
00A1440B  F6 C3 02                        test bl, 2
00A1440E  0F 85 8F 00 00 00               jne 0x140a144a3
00A14414  49 8D BC 24 E8 01 00 00         lea rdi, [r12 + 0x1e8]
00A1441C  48 8B CF                        mov rcx, rdi
00A1441F  E8 FC 21 80 FF                  call 0x140216620
00A14424  84 C0                           test al, al
00A14426  74 25                           je 0x140a1444d
00A14428  49 8B 84 24 A8 02 00 00         mov rax, qword ptr [r12 + 0x2a8]
00A14430  48 89 84 24 08 01 00 00         mov qword ptr [rsp + 0x108], rax
00A14438  48 85 C0                        test rax, rax
00A1443B  74 08                           je 0x140a14445
00A1443D  48 8B C8                        mov rcx, rax
00A14440  E8 DB B5 7F FF                  call 0x14020fa20
00A14445  48 8B CF                        mov rcx, rdi
00A14448  E8 33 5A 93 FF                  call 0x140349e80
00A1444D  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
00A14455  48 85 C9                        test rcx, rcx
00A14458  75 0A                           jne 0x140a14464
00A1445A  BF 0A 01 00 C0                  mov edi, 0xc000010a
00A1445F  E9 84 08 00 00                  jmp 0x140a14ce8
00A14464  49 8B 84 24 10 03 00 00         mov rax, qword ptr [r12 + 0x310]
00A1446C  48 85 C0                        test rax, rax
00A1446F  74 14                           je 0x140a14485
00A14471  83 CB 40                        or ebx, 0x40
00A14474  89 9C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ebx
00A1447B  8B 40 08                        mov eax, dword ptr [rax + 8]
00A1447E  89 84 24 18 01 00 00            mov dword ptr [rsp + 0x118], eax
00A14485  BA 00 00 02 00                  mov edx, 0x20000
00A1448A  41 85 94 24 F4 01 00 00         test dword ptr [r12 + 0x1f4], edx
00A14492  8B C6                           mov eax, esi
00A14494  0F 45 C2                        cmovne eax, edx
00A14497  89 84 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], eax
00A1449E  BF 04 00 00 00                  mov edi, 4
00A144A3  44 8B E3                        mov r12d, ebx
00A144A6  49 89 8E A8 02 00 00            mov qword ptr [r14 + 0x2a8], rcx
00A144AD  4D 85 FF                        test r15, r15
00A144B0  0F 84 83 05 00 00               je 0x140a14a39
00A144B6  F6 C3 02                        test bl, 2
00A144B9  0F 85 7A 05 00 00               jne 0x140a14a39
00A144BF  49 8B 87 A8 01 00 00            mov rax, qword ptr [r15 + 0x1a8]
00A144C6  49 89 86 F0 05 00 00            mov qword ptr [r14 + 0x5f0], rax
00A144CD  4D 8D 47 38                     lea r8, [r15 + 0x38]
00A144D1  8B D7                           mov edx, edi
00A144D3  E8 38 D4 F0 FF                  call 0x140921910
00A144D8  8B F8                           mov edi, eax
00A144DA  85 C0                           test eax, eax
00A144DC  0F 88 06 08 00 00               js 0x140a14ce8
00A144E2  41 8B 47 78                     mov eax, dword ptr [r15 + 0x78]
00A144E6  41 0F B6 4F 6B                  movzx ecx, byte ptr [r15 + 0x6b]
00A144EB  8B D8                           mov ebx, eax
00A144ED  81 E3 FA 00 00 00               and ebx, 0xfa
00A144F3  03 DB                           add ebx, ebx
00A144F5  41 23 C5                        and eax, r13d
00A144F8  0B D8                           or ebx, eax
00A144FA  C1 E3 05                        shl ebx, 5
00A144FD  8B C1                           mov eax, ecx
00A144FF  83 E0 02                        and eax, 2
00A14502  0B D8                           or ebx, eax
00A14504  C1 E3 02                        shl ebx, 2
00A14507  83 E1 04                        and ecx, 4
00A1450A  0B D9                           or ebx, ecx
00A1450C  C1 E3 0B                        shl ebx, 0xb
00A1450F  41 0B DC                        or ebx, r12d
00A14512  89 9C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ebx
00A14519  41 0F B7 4F 5E                  movzx ecx, word ptr [r15 + 0x5e]
00A1451E  89 8C 24 DC 00 00 00            mov dword ptr [rsp + 0xdc], ecx
00A14525  41 0F B7 4F 5C                  movzx ecx, word ptr [r15 + 0x5c]
00A1452A  89 8C 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], ecx
00A14531  41 0F B7 47 64                  movzx eax, word ptr [r15 + 0x64]
00A14536  66 41 85 47 12                  test word ptr [r15 + 0x12], ax
00A1453B  74 1A                           je 0x140a14557
00A1453D  BF 7B 00 00 C0                  mov edi, 0xc000007b
00A14542  B9 03 00 00 00                  mov ecx, 3
00A14547  45 33 C0                        xor r8d, r8d
00A1454A  49 8B D7                        mov rdx, r15
00A1454D  E8 0E 7B 0D 00                  call 0x140aec060
00A14552  E9 91 07 00 00                  jmp 0x140a14ce8
00A14557  41 BC 04 00 00 00               mov r12d, 4
00A1455D  41 84 DC                        test r12b, bl
00A14560  0F 85 86 05 00 00               jne 0x140a14aec
00A14566  BA 50 73 43 72                  mov edx, 0x72437350
00A1456B  49 8B 8F B8 00 00 00            mov rcx, qword ptr [r15 + 0xb8]
00A14572  E8 99 C1 7F FF                  call 0x140210710
00A14577  49 8B 87 B8 00 00 00            mov rax, qword ptr [r15 + 0xb8]
00A1457E  49 89 86 30 03 00 00            mov qword ptr [r14 + 0x330], rax
00A14585  41 0F B7 47 66                  movzx eax, word ptr [r15 + 0x66]
00A1458A  66 89 84 24 A8 00 00 00         mov word ptr [rsp + 0xa8], ax
00A14592  49 8D BF C8 00 00 00            lea rdi, [r15 + 0xc8]
00A14599  49 8D 8F F0 00 00 00            lea rcx, [r15 + 0xf0]
00A145A0  4C 8B CF                        mov r9, rdi
00A145A3  E8 00 73 02 00                  call 0x140a3b8a8
00A145A8  85 C0                           test eax, eax
00A145AA  79 0F                           jns 0x140a145bb
00A145AC  3D 34 00 00 C0                  cmp eax, 0xc0000034
00A145B1  75 05                           jne 0x140a145b8
00A145B3  41 80 4F 10 40                  or byte ptr [r15 + 0x10], 0x40
00A145B8  48 89 37                        mov qword ptr [rdi], rsi
00A145BB  4C 8D 84 24 D0 00 00 00         lea r8, [rsp + 0xd0]
00A145C3  49 8B D7                        mov rdx, r15
00A145C6  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00A145CE  E8 E9 B9 00 00                  call 0x140a1ffbc
00A145D3  8B F8                           mov edi, eax
00A145D5  85 C0                           test eax, eax
00A145D7  79 08                           jns 0x140a145e1
00A145D9  41 8B CC                        mov ecx, r12d
00A145DC  E9 66 FF FF FF                  jmp 0x140a14547
00A145E1  0F B7 84 24 D0 00 00 00         movzx eax, word ptr [rsp + 0xd0]
00A145E9  89 84 24 CC 00 00 00            mov dword ptr [rsp + 0xcc], eax
00A145F0  40 38 B4 24 D2 00 00 00         cmp byte ptr [rsp + 0xd2], sil
00A145F8  74 0A                           je 0x140a14604
00A145FA  83 CB 40                        or ebx, 0x40
00A145FD  89 9C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ebx
00A14604  40 38 B4 24 D3 00 00 00         cmp byte ptr [rsp + 0xd3], sil
00A1460C  74 09                           je 0x140a14617
00A1460E  0F BA AC 24 B0 00 00 00 11      bts dword ptr [rsp + 0xb0], 0x11
00A14617  49 8B 8F C8 00 00 00            mov rcx, qword ptr [r15 + 0xc8]
00A1461E  48 85 C9                        test rcx, rcx
00A14621  0F 84 C5 04 00 00               je 0x140a14aec
00A14627  41 38 77 10                     cmp byte ptr [r15 + 0x10], sil
00A1462B  0F 8C 97 00 00 00               jl 0x140a146c8
00A14631  48 8D 84 24 AC 00 00 00         lea rax, [rsp + 0xac]
00A14639  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A1463E  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
00A14646  4C 8D 8C 24 C0 00 00 00         lea r9, [rsp + 0xc0]
00A1464E  45 8B C5                        mov r8d, r13d
00A14651  48 8D 15 28 08 0F 00            lea rdx, [rip + 0xf0828]
00A14658  E8 B3 8A 01 00                  call 0x140a2d110
00A1465D  3D 05 00 00 80                  cmp eax, 0x80000005
00A14662  74 55                           je 0x140a146b9
00A14664  85 C0                           test eax, eax
00A14666  78 14                           js 0x140a1467c
00A14668  83 BC 24 AC 00 00 00 02         cmp dword ptr [rsp + 0xac], 2
00A14670  75 0A                           jne 0x140a1467c
00A14672  66 39 B4 24 C0 00 00 00         cmp word ptr [rsp + 0xc0], si
00A1467A  75 3D                           jne 0x140a146b9
00A1467C  89 B4 24 34 01 00 00            mov dword ptr [rsp + 0x134], esi
00A14683  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00A14688  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00A1468D  4C 8D 8C 24 34 01 00 00         lea r9, [rsp + 0x134]
00A14695  45 8B C4                        mov r8d, r12d
00A14698  48 8D 15 A1 07 0F 00            lea rdx, [rip + 0xf07a1]
00A1469F  49 8B 8F C8 00 00 00            mov rcx, qword ptr [r15 + 0xc8]
00A146A6  E8 65 8A 01 00                  call 0x140a2d110
00A146AB  85 C0                           test eax, eax
00A146AD  78 19                           js 0x140a146c8
00A146AF  44 39 AC 24 34 01 00 00         cmp dword ptr [rsp + 0x134], r13d
00A146B7  75 0F                           jne 0x140a146c8
00A146B9  BF 39 00 00 C0                  mov edi, 0xc0000039
00A146BE  B9 05 00 00 00                  mov ecx, 5
00A146C3  E9 7F FE FF FF                  jmp 0x140a14547
00A146C8  89 B4 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], esi
00A146CF  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00A146D4  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00A146D9  4C 8D 8C 24 C8 00 00 00         lea r9, [rsp + 0xc8]
00A146E1  45 8B C4                        mov r8d, r12d
00A146E4  48 8D 15 25 08 0F 00            lea rdx, [rip + 0xf0825]
00A146EB  49 8B 8F C8 00 00 00            mov rcx, qword ptr [r15 + 0xc8]
00A146F2  E8 19 8A 01 00                  call 0x140a2d110
00A146F7  44 8B A4 24 90 00 00 00         mov r12d, dword ptr [rsp + 0x90]
00A146FF  85 C0                           test eax, eax
00A14701  0F 88 EC 00 00 00               js 0x140a147f3
00A14707  39 B4 24 C8 00 00 00            cmp dword ptr [rsp + 0xc8], esi
00A1470E  0F 84 DF 00 00 00               je 0x140a147f3
00A14714  41 83 CC 10                     or r12d, 0x10
00A14718  44 89 A4 24 90 00 00 00         mov dword ptr [rsp + 0x90], r12d
00A14720  44 89 A4 24 B0 08 00 00         mov dword ptr [rsp + 0x8b0], r12d
00A14728  F6 C3 40                        test bl, 0x40
00A1472B  0F 85 C2 00 00 00               jne 0x140a147f3
00A14731  C7 84 24 50 02 00 00 30 00 00 00  mov dword ptr [rsp + 0x250], 0x30
00A1473C  49 8B 87 C8 00 00 00            mov rax, qword ptr [r15 + 0xc8]
00A14743  48 89 84 24 58 02 00 00         mov qword ptr [rsp + 0x258], rax
00A1474B  C7 84 24 68 02 00 00 40 02 00 00  mov dword ptr [rsp + 0x268], 0x240
00A14756  48 8D 05 0B 77 13 00            lea rax, [rip + 0x13770b]
00A1475D  48 89 84 24 60 02 00 00         mov qword ptr [rsp + 0x260], rax
00A14765  0F 57 C0                        xorps xmm0, xmm0
00A14768  F3 0F 7F 84 24 70 02 00 00      movdqu xmmword ptr [rsp + 0x270], xmm0
00A14771  4C 8D 84 24 50 02 00 00         lea r8, [rsp + 0x250]
00A14779  41 8B D5                        mov edx, r13d
00A1477C  48 8D 8C 24 78 01 00 00         lea rcx, [rsp + 0x178]
00A14784  E8 87 8B C9 FF                  call 0x1406ad310
00A14789  BF 04 00 00 00                  mov edi, 4
00A1478E  85 C0                           test eax, eax
00A14790  78 66                           js 0x140a147f8
00A14792  89 B4 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], esi
00A14799  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00A1479E  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00A147A2  4C 8D 8C 24 C8 00 00 00         lea r9, [rsp + 0xc8]
00A147AA  44 8B C7                        mov r8d, edi
00A147AD  48 8D 15 3C 07 0F 00            lea rdx, [rip + 0xf073c]
00A147B4  48 8B 8C 24 78 01 00 00         mov rcx, qword ptr [rsp + 0x178]
00A147BC  E8 4F 89 01 00                  call 0x140a2d110
00A147C1  85 C0                           test eax, eax
00A147C3  78 1D                           js 0x140a147e2
00A147C5  39 B4 24 C8 00 00 00            cmp dword ptr [rsp + 0xc8], esi
00A147CC  74 14                           je 0x140a147e2
00A147CE  41 83 CC 20                     or r12d, 0x20
00A147D2  44 89 A4 24 90 00 00 00         mov dword ptr [rsp + 0x90], r12d
00A147DA  44 89 A4 24 B0 08 00 00         mov dword ptr [rsp + 0x8b0], r12d
00A147E2  33 D2                           xor edx, edx
00A147E4  48 8B 8C 24 78 01 00 00         mov rcx, qword ptr [rsp + 0x178]
00A147EC  E8 7F D0 E8 FF                  call 0x1408a1870
00A147F1  EB 05                           jmp 0x140a147f8
00A147F3  BF 04 00 00 00                  mov edi, 4
00A147F8  48 39 B4 24 40 01 00 00         cmp qword ptr [rsp + 0x140], rsi
00A14800  75 17                           jne 0x140a14819
00A14802  4C 8D 84 24 B8 00 00 00         lea r8, [rsp + 0xb8]
00A1480A  49 8B 97 C8 00 00 00            mov rdx, qword ptr [r15 + 0xc8]
00A14811  49 8B CE                        mov rcx, r14
00A14814  E8 9F 86 01 00                  call 0x140a2ceb8
00A14819  89 B4 24 38 01 00 00            mov dword ptr [rsp + 0x138], esi
00A14820  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00A14825  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00A14829  4C 8D 8C 24 38 01 00 00         lea r9, [rsp + 0x138]
00A14831  44 8B C7                        mov r8d, edi
00A14834  48 8D 15 95 06 0F 00            lea rdx, [rip + 0xf0695]
00A1483B  49 8B 8F C8 00 00 00            mov rcx, qword ptr [r15 + 0xc8]
00A14842  E8 C9 88 01 00                  call 0x140a2d110
00A14847  85 C0                           test eax, eax
00A14849  78 11                           js 0x140a1485c
00A1484B  39 B4 24 38 01 00 00            cmp dword ptr [rsp + 0x138], esi
00A14852  74 08                           je 0x140a1485c
00A14854  83 8C 24 B4 00 00 00 40         or dword ptr [rsp + 0xb4], 0x40
00A1485C  48 8D 84 24 AC 00 00 00         lea rax, [rsp + 0xac]
00A14864  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A14869  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
00A1486D  45 33 C9                        xor r9d, r9d
00A14870  45 8D 41 03                     lea r8d, [r9 + 3]
00A14874  48 8D 15 35 06 0F 00            lea rdx, [rip + 0xf0635]
00A1487B  49 8B 8F C8 00 00 00            mov rcx, qword ptr [r15 + 0xc8]
00A14882  E8 89 88 01 00                  call 0x140a2d110
00A14887  3D 05 00 00 80                  cmp eax, 0x80000005
00A1488C  0F 85 9D 00 00 00               jne 0x140a1492f
00A14892  8B BC 24 AC 00 00 00            mov edi, dword ptr [rsp + 0xac]
00A14899  81 FF 00 01 00 00               cmp edi, 0x100
00A1489F  0F 87 8A 00 00 00               ja 0x140a1492f
00A148A5  40 F6 C7 07                     test dil, 7
00A148A9  0F 85 80 00 00 00               jne 0x140a1492f
00A148AF  8B D7                           mov edx, edi
00A148B1  B9 40 00 00 00                  mov ecx, 0x40
00A148B6  41 B8 50 73 43 73               mov r8d, 0x73437350
00A148BC  E8 2F D8 16 00                  call 0x140b820f0
00A148C1  48 89 84 24 A0 01 00 00         mov qword ptr [rsp + 0x1a0], rax
00A148C9  48 85 C0                        test rax, rax
00A148CC  75 0A                           jne 0x140a148d8
00A148CE  BF 17 00 00 C0                  mov edi, 0xc0000017
00A148D3  E9 10 04 00 00                  jmp 0x140a14ce8
00A148D8  48 8D 8C 24 AC 00 00 00         lea rcx, [rsp + 0xac]
00A148E0  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00A148E5  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00A148E9  4C 8B C8                        mov r9, rax
00A148EC  41 B8 03 00 00 00               mov r8d, 3
00A148F2  48 8D 15 B7 05 0F 00            lea rdx, [rip + 0xf05b7]
00A148F9  49 8B 8F C8 00 00 00            mov rcx, qword ptr [r15 + 0xc8]
00A14900  E8 0B 88 01 00                  call 0x140a2d110
00A14905  85 C0                           test eax, eax
00A14907  78 26                           js 0x140a1492f
00A14909  F6 84 24 AC 00 00 00 07         test byte ptr [rsp + 0xac], 7
00A14911  75 1C                           jne 0x140a1492f
00A14913  0F BA EB 15                     bts ebx, 0x15
00A14917  89 9C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ebx
00A1491E  8B 84 24 AC 00 00 00            mov eax, dword ptr [rsp + 0xac]
00A14925  C1 E8 03                        shr eax, 3
00A14928  89 84 24 C4 00 00 00            mov dword ptr [rsp + 0xc4], eax
00A1492F  C7 84 24 80 02 00 00 30 00 00 00  mov dword ptr [rsp + 0x280], 0x30
00A1493A  49 8B 87 C8 00 00 00            mov rax, qword ptr [r15 + 0xc8]
00A14941  48 89 84 24 88 02 00 00         mov qword ptr [rsp + 0x288], rax
00A14949  C7 84 24 98 02 00 00 40 02 00 00  mov dword ptr [rsp + 0x298], 0x240
00A14954  48 8D 05 FD 74 13 00            lea rax, [rip + 0x1374fd]
00A1495B  48 89 84 24 90 02 00 00         mov qword ptr [rsp + 0x290], rax
00A14963  0F 57 C0                        xorps xmm0, xmm0
00A14966  F3 0F 7F 84 24 A0 02 00 00      movdqu xmmword ptr [rsp + 0x2a0], xmm0
00A1496F  4C 8D 84 24 80 02 00 00         lea r8, [rsp + 0x280]
00A14977  41 8B D5                        mov edx, r13d
00A1497A  48 8D 8C 24 80 01 00 00         lea rcx, [rsp + 0x180]
00A14982  E8 89 89 C9 FF                  call 0x1406ad310
00A14987  85 C0                           test eax, eax
00A14989  78 24                           js 0x140a149af
00A1498B  48 8D 94 24 38 04 00 00         lea rdx, [rsp + 0x438]
00A14993  48 8B 8C 24 80 01 00 00         mov rcx, qword ptr [rsp + 0x180]
00A1499B  E8 50 FC D6 FF                  call 0x1407845f0
00A149A0  33 D2                           xor edx, edx
00A149A2  48 8B 8C 24 80 01 00 00         mov rcx, qword ptr [rsp + 0x180]
00A149AA  E8 C1 CE E8 FF                  call 0x1408a1870
00A149AF  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00A149B4  BF 04 00 00 00                  mov edi, 4
00A149B9  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00A149BD  4C 8D 8C 24 3C 01 00 00         lea r9, [rsp + 0x13c]
00A149C5  44 8B C7                        mov r8d, edi
00A149C8  48 8D 15 61 03 0F 00            lea rdx, [rip + 0xf0361]
00A149CF  49 8B 8F C8 00 00 00            mov rcx, qword ptr [r15 + 0xc8]
00A149D6  E8 35 87 01 00                  call 0x140a2d110
00A149DB  85 C0                           test eax, eax
00A149DD  78 2A                           js 0x140a14a09
00A149DF  83 BC 24 3C 01 00 00 02         cmp dword ptr [rsp + 0x13c], 2
00A149E7  75 20                           jne 0x140a14a09
00A149E9  F0 41 09 BE DC 07 00 00         lock or dword ptr [r14 + 0x7dc], edi
00A149F1  44 8B A4 24 B0 08 00 00         mov r12d, dword ptr [rsp + 0x8b0]
00A149F9  44 89 A4 24 90 00 00 00         mov dword ptr [rsp + 0x90], r12d
00A14A01  4C 8B B4 24 A0 00 00 00         mov r14, qword ptr [rsp + 0xa0]
00A14A09  41 0F BA E4 13                  bt r12d, 0x13
00A14A0E  0F 83 E0 00 00 00               jae 0x140a14af4
00A14A14  F0 41 09 BE DC 07 00 00         lock or dword ptr [r14 + 0x7dc], edi
00A14A1C  44 8B A4 24 B0 08 00 00         mov r12d, dword ptr [rsp + 0x8b0]
00A14A24  44 89 A4 24 90 00 00 00         mov dword ptr [rsp + 0x90], r12d
00A14A2C  4C 8B B4 24 A0 00 00 00         mov r14, qword ptr [rsp + 0xa0]
00A14A34  E9 BB 00 00 00                  jmp 0x140a14af4
00A14A39  48 85 C9                        test rcx, rcx
00A14A3C  0F 84 AA 00 00 00               je 0x140a14aec
00A14A42  4C 8D 84 24 B0 03 00 00         lea r8, [rsp + 0x3b0]
00A14A4A  41 BC 04 00 00 00               mov r12d, 4
00A14A50  41 8B D4                        mov edx, r12d
00A14A53  E8 B8 CE F0 FF                  call 0x140921910
00A14A58  8B F8                           mov edi, eax
00A14A5A  85 C0                           test eax, eax
00A14A5C  0F 88 86 02 00 00               js 0x140a14ce8
00A14A62  0F B6 8C 24 E3 03 00 00         movzx ecx, byte ptr [rsp + 0x3e3]
00A14A6A  8B 84 24 F0 03 00 00            mov eax, dword ptr [rsp + 0x3f0]
00A14A71  8B D0                           mov edx, eax
00A14A73  81 E2 FA 00 00 00               and edx, 0xfa
00A14A79  03 D2                           add edx, edx
00A14A7B  41 23 C5                        and eax, r13d
00A14A7E  0B D0                           or edx, eax
00A14A80  C1 E2 05                        shl edx, 5
00A14A83  8B C1                           mov eax, ecx
00A14A85  83 E0 02                        and eax, 2
00A14A88  0B D0                           or edx, eax
00A14A8A  C1 E2 02                        shl edx, 2
00A14A8D  41 23 CC                        and ecx, r12d
00A14A90  0B D1                           or edx, ecx
00A14A92  C1 E2 0B                        shl edx, 0xb
00A14A95  8B C3                           mov eax, ebx
00A14A97  25 FF 9F 2B F8                  and eax, 0xf82b9fff
00A14A9C  8B DA                           mov ebx, edx
00A14A9E  0B D8                           or ebx, eax
00A14AA0  89 9C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ebx
00A14AA7  0F B7 84 24 DE 03 00 00         movzx eax, word ptr [rsp + 0x3de]
00A14AAF  66 89 84 24 A8 00 00 00         mov word ptr [rsp + 0xa8], ax
00A14AB7  0F B7 84 24 D6 03 00 00         movzx eax, word ptr [rsp + 0x3d6]
00A14ABF  89 84 24 DC 00 00 00            mov dword ptr [rsp + 0xdc], eax
00A14AC6  0F B7 84 24 D4 03 00 00         movzx eax, word ptr [rsp + 0x3d4]
00A14ACE  89 84 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], eax
00A14AD5  41 84 DC                        test r12b, bl
00A14AD8  74 12                           je 0x140a14aec
00A14ADA  83 8C 24 B0 00 00 00 08         or dword ptr [rsp + 0xb0], 8
00A14AE2  83 CB 18                        or ebx, 0x18
00A14AE5  89 9C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ebx
00A14AEC  44 8B A4 24 90 00 00 00         mov r12d, dword ptr [rsp + 0x90]
00A14AF4  F6 C3 40                        test bl, 0x40
00A14AF7  0F 84 85 00 00 00               je 0x140a14b82
00A14AFD  BA 10 00 00 00                  mov edx, 0x10
00A14B02  8D 4A 30                        lea ecx, [rdx + 0x30]
00A14B05  41 B8 57 6F 77 50               mov r8d, 0x50776f57
00A14B0B  E8 E0 D5 16 00                  call 0x140b820f0
00A14B10  4C 8B D0                        mov r10, rax
00A14B13  49 89 86 10 03 00 00            mov qword ptr [r14 + 0x310], rax
00A14B1A  48 85 C0                        test rax, rax
00A14B1D  0F 84 AB FD FF FF               je 0x140a148ce
00A14B23  8B 84 24 18 01 00 00            mov eax, dword ptr [rsp + 0x118]
00A14B2A  44 8B 9C 24 CC 00 00 00         mov r11d, dword ptr [rsp + 0xcc]
00A14B32  85 C0                           test eax, eax
00A14B34  75 0C                           jne 0x140a14b42
00A14B36  41 0F B7 D3                     movzx edx, r11w
00A14B3A  49 8B CF                        mov rcx, r15
00A14B3D  E8 46 C5 A8 FF                  call 0x1404a1088
00A14B42  41 89 42 08                     mov dword ptr [r10 + 8], eax
00A14B46  49 8B 86 10 03 00 00            mov rax, qword ptr [r14 + 0x310]
00A14B4D  48 85 C0                        test rax, rax
00A14B50  74 03                           je 0x140a14b55
00A14B52  4C 89 28                        mov qword ptr [rax], r13
00A14B55  41 0F BA E4 17                  bt r12d, 0x17
00A14B5A  73 2E                           jae 0x140a14b8a
00A14B5C  F0 41 81 8E F4 01 00 00 00 02 00 00  lock or dword ptr [r14 + 0x1f4], 0x200
00A14B68  44 8B A4 24 B0 08 00 00         mov r12d, dword ptr [rsp + 0x8b0]
00A14B70  44 89 A4 24 90 00 00 00         mov dword ptr [rsp + 0x90], r12d
00A14B78  4C 8B B4 24 A0 00 00 00         mov r14, qword ptr [rsp + 0xa0]
00A14B80  EB 08                           jmp 0x140a14b8a
00A14B82  44 8B 9C 24 CC 00 00 00         mov r11d, dword ptr [rsp + 0xcc]
00A14B8A  66 45 89 9E EC 06 00 00         mov word ptr [r14 + 0x6ec], r11w
00A14B92  4C 8D 84 24 E4 00 00 00         lea r8, [rsp + 0xe4]
00A14B9A  BA 1D 00 00 00                  mov edx, 0x1d
00A14B9F  48 8B 8C 24 00 01 00 00         mov rcx, qword ptr [rsp + 0x100]
00A14BA7  E8 E4 04 EA FF                  call 0x1408b5090
00A14BAC  8B F8                           mov edi, eax
00A14BAE  85 C0                           test eax, eax
00A14BB0  0F 88 32 01 00 00               js 0x140a14ce8
00A14BB6  44 8B D6                        mov r10d, esi
00A14BB9  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
00A14BC0  84 C0                           test al, al
00A14BC2  0F 84 E5 00 00 00               je 0x140a14cad
00A14BC8  4D 85 FF                        test r15, r15
00A14BCB  74 20                           je 0x140a14bed
00A14BCD  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
00A14BD1  48 0F BA E0 08                  bt rax, 8
00A14BD6  73 15                           jae 0x140a14bed
00A14BD8  41 80 7F 02 04                  cmp byte ptr [r15 + 2], 4
00A14BDD  75 0E                           jne 0x140a14bed
00A14BDF  C7 84 24 C0 07 00 00 0E 00 00 00  mov dword ptr [rsp + 0x7c0], 0xe
00A14BEA  45 8B D5                        mov r10d, r13d
00A14BED  8B 8C 24 C8 08 00 00            mov ecx, dword ptr [rsp + 0x8c8]
00A14BF4  85 C9                           test ecx, ecx
00A14BF6  74 11                           je 0x140a14c09
00A14BF8  41 8B C2                        mov eax, r10d
00A14BFB  C7 84 84 C0 07 00 00 03 00 00 00  mov dword ptr [rsp + rax*4 + 0x7c0], 3
00A14C06  45 03 D5                        add r10d, r13d
00A14C09  41 F6 C4 30                     test r12b, 0x30
00A14C0D  74 11                           je 0x140a14c20
00A14C0F  41 8B C2                        mov eax, r10d
00A14C12  C7 84 84 C0 07 00 00 04 00 00 00  mov dword ptr [rsp + rax*4 + 0x7c0], 4
00A14C1D  45 03 D5                        add r10d, r13d
00A14C20  45 84 E4                        test r12b, r12b
00A14C23  79 29                           jns 0x140a14c4e
00A14C25  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
00A14C2D  E8 F6 AA 07 00                  call 0x140a8f728
00A14C32  8B 8C 24 C8 08 00 00            mov ecx, dword ptr [rsp + 0x8c8]
00A14C39  85 C0                           test eax, eax
00A14C3B  75 11                           jne 0x140a14c4e
00A14C3D  41 8B C2                        mov eax, r10d
00A14C40  C7 84 84 C0 07 00 00 0A 00 00 00  mov dword ptr [rsp + rax*4 + 0x7c0], 0xa
00A14C4B  45 03 D5                        add r10d, r13d
00A14C4E  41 F7 C4 00 84 00 00            test r12d, 0x8400
00A14C55  74 11                           je 0x140a14c68
00A14C57  41 8B C2                        mov eax, r10d
00A14C5A  C7 84 84 C0 07 00 00 07 00 00 00  mov dword ptr [rsp + rax*4 + 0x7c0], 7
00A14C65  45 03 D5                        add r10d, r13d
00A14C68  45 85 D2                        test r10d, r10d
00A14C6B  74 39                           je 0x140a14ca6
00A14C6D  44 8B C6                        mov r8d, esi
00A14C70  85 C9                           test ecx, ecx
00A14C72  41 0F 95 C0                     setne r8b
00A14C76  4C 8D 8C 24 98 01 00 00         lea r9, [rsp + 0x198]
00A14C7E  41 8B D2                        mov edx, r10d
00A14C81  48 8D 8C 24 C0 07 00 00         lea rcx, [rsp + 0x7c0]
00A14C89  E8 92 44 E6 FF                  call 0x140879120
00A14C8E  85 C0                           test eax, eax
00A14C90  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
00A14C97  78 14                           js 0x140a14cad
00A14C99  0F BA EB 0A                     bts ebx, 0xa
00A14C9D  89 9C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ebx
00A14CA4  EB 07                           jmp 0x140a14cad
00A14CA6  8A 84 24 80 00 00 00            mov al, byte ptr [rsp + 0x80]
00A14CAD  41 F7 C4 00 84 00 00            test r12d, 0x8400
00A14CB4  0F 84 AE 00 00 00               je 0x140a14d68
00A14CBA  8A D0                           mov dl, al
00A14CBC  48 8B 0D B5 4D 5C 00            mov rcx, qword ptr [rip + 0x5c4db5]
00A14CC3  E8 58 D1 E5 FF                  call 0x140871e20
00A14CC8  84 C0                           test al, al
00A14CCA  0F 85 98 00 00 00               jne 0x140a14d68
00A14CD0  BF 61 00 00 C0                  mov edi, 0xc0000061
00A14CD5  0F BA E3 0A                     bt ebx, 0xa
00A14CD9  73 0D                           jae 0x140a14ce8
00A14CDB  48 8B 8C 24 98 01 00 00         mov rcx, qword ptr [rsp + 0x198]
00A14CE3  E8 B8 38 05 00                  call 0x140a685a0
00A14CE8  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
00A14CF0  48 85 C0                        test rax, rax
00A14CF3  74 07                           je 0x140a14cfc
00A14CF5  49 89 86 D0 01 00 00            mov qword ptr [r14 + 0x1d0], rax
00A14CFC  33 D2                           xor edx, edx
00A14CFE  49 8B CE                        mov rcx, r14
00A14D01  E8 4A 20 EF FF                  call 0x140906d50
00A14D06  BA 50 73 43 72                  mov edx, 0x72437350
00A14D0B  49 8B CE                        mov rcx, r14
00A14D0E  E8 CD 2B 8E FF                  call 0x1402f78e0
00A14D13  48 8B 84 24 A0 01 00 00         mov rax, qword ptr [rsp + 0x1a0]
00A14D1B  48 85 C0                        test rax, rax
00A14D1E  74 0D                           je 0x140a14d2d
00A14D20  BA 50 73 43 73                  mov edx, 0x73437350
00A14D25  48 8B C8                        mov rcx, rax
00A14D28  E8 43 DB 16 00                  call 0x140b82870
00A14D2D  E8 36 8C BB FF                  call 0x1405cd968
00A14D32  85 C0                           test eax, eax
00A14D34  74 12                           je 0x140a14d48
00A14D36  48 8B 8C 24 60 01 00 00         mov rcx, qword ptr [rsp + 0x160]
00A14D3E  48 85 C9                        test rcx, rcx
00A14D41  74 05                           je 0x140a14d48
00A14D43  E8 58 48 BF FF                  call 0x1406095a0
00A14D48  48 8B 05 B9 01 4F 00            mov rax, qword ptr [rip + 0x4f01b9]
00A14D4F  48 85 C0                        test rax, rax
00A14D52  74 0D                           je 0x140a14d61
00A14D54  48 8D 8C 24 A0 05 00 00         lea rcx, [rsp + 0x5a0]
00A14D5C  E8 6F 5D CA FF                  call 0x1406baad0
00A14D61  8B C7                           mov eax, edi
00A14D63  E9 1C 16 00 00                  jmp 0x140a16384
00A14D68  B8 FF FF 00 00                  mov eax, 0xffff
00A14D6D  66 89 84 24 8C 00 00 00         mov word ptr [rsp + 0x8c], ax
00A14D75  48 C7 84 24 90 04 00 00 01 00 20 00  mov qword ptr [rsp + 0x490], 0x200001
00A14D81  33 D2                           xor edx, edx
00A14D83  41 B8 00 01 00 00               mov r8d, 0x100
00A14D89  48 8D 8C 24 98 04 00 00         lea rcx, [rsp + 0x498]
00A14D91  E8 AA 1E CB FF                  call 0x1406c6c40
00A14D96  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
00A14D9E  48 85 C0                        test rax, rax
00A14DA1  0F 85 44 01 00 00               jne 0x140a14eeb
00A14DA7  48 39 B4 24 B8 00 00 00         cmp qword ptr [rsp + 0xb8], rsi
00A14DAF  0F 85 B0 00 00 00               jne 0x140a14e65
00A14DB5  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00A14DBD  48 85 C9                        test rcx, rcx
00A14DC0  0F 84 83 00 00 00               je 0x140a14e49
00A14DC6  F7 81 F0 01 00 00 00 00 10 00   test dword ptr [rcx + 0x1f0], 0x100000
00A14DD0  74 28                           je 0x140a14dfa
00A14DD2  0F BA AC 24 B4 00 00 00 14      bts dword ptr [rsp + 0xb4], 0x14
00A14DDB  0F B7 81 04 01 00 00            movzx eax, word ptr [rcx + 0x104]
00A14DE2  48 8D 0D D7 A8 5B 00            lea rcx, [rip + 0x5ba8d7]
00A14DE9  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
00A14DED  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
00A14DF5  48 8B C8                        mov rcx, rax
00A14DF8  EB 73                           jmp 0x140a14e6d
00A14DFA  E8 DD 4D 07 00                  call 0x140a89bdc
00A14DFF  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
00A14E07  48 8B C8                        mov rcx, rax
00A14E0A  E8 61 C4 A7 FF                  call 0x140491270
00A14E0F  0F B7 F8                        movzx edi, ax
00A14E12  66 89 84 24 8C 00 00 00         mov word ptr [rsp + 0x8c], ax
00A14E1A  40 38 35 D1 1C 5B 00            cmp byte ptr [rip + 0x5b1cd1], sil
00A14E21  74 5A                           je 0x140a14e7d
00A14E23  E8 D8 77 A7 FF                  call 0x14048c600
00A14E28  66 41 3B C5                     cmp ax, r13w
00A14E2C  76 4F                           jbe 0x140a14e7d
00A14E2E  66 85 FF                        test di, di
00A14E31  75 4A                           jne 0x140a14e7d
00A14E33  48 89 B4 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rsi
00A14E3B  41 8B FD                        mov edi, r13d
00A14E3E  66 44 89 AC 24 8C 00 00 00      mov word ptr [rsp + 0x8c], r13w
00A14E47  EB 34                           jmp 0x140a14e7d
00A14E49  0F B7 FE                        movzx edi, si
00A14E4C  66 89 B4 24 8C 00 00 00         mov word ptr [rsp + 0x8c], si
00A14E54  33 D2                           xor edx, edx
00A14E56  48 8D 8C 24 90 04 00 00         lea rcx, [rsp + 0x490]
00A14E5E  E8 8D 68 84 FF                  call 0x14025b6f0
00A14E63  EB 18                           jmp 0x140a14e7d
00A14E65  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
00A14E6D  E8 FE C3 A7 FF                  call 0x140491270
00A14E72  66 89 84 24 8C 00 00 00         mov word ptr [rsp + 0x8c], ax
00A14E7A  0F B7 F8                        movzx edi, ax
00A14E7D  4C 8D 05 9C 22 5B 00            lea r8, [rip + 0x5b229c]
00A14E84  0F B7 94 24 92 04 00 00         movzx edx, word ptr [rsp + 0x492]
00A14E8C  48 8D 8C 24 90 04 00 00         lea rcx, [rsp + 0x490]
00A14E94  E8 C7 99 8B FF                  call 0x1402ce860
00A14E99  48 39 B4 24 B8 00 00 00         cmp qword ptr [rsp + 0xb8], rsi
00A14EA1  0F 85 8F 00 00 00               jne 0x140a14f36
00A14EA7  0F 57 C0                        xorps xmm0, xmm0
00A14EAA  0F 11 84 24 40 02 00 00         movups xmmword ptr [rsp + 0x240], xmm0
00A14EB2  66 89 BC 24 48 02 00 00         mov word ptr [rsp + 0x248], di
00A14EBA  66 3B BC 24 90 04 00 00         cmp di, word ptr [rsp + 0x490]
00A14EC2  73 0D                           jae 0x140a14ed1
00A14EC4  0F B7 C7                        movzx eax, di
00A14EC7  48 8B 8C C4 98 04 00 00         mov rcx, qword ptr [rsp + rax*8 + 0x498]
00A14ECF  EB 03                           jmp 0x140a14ed4
00A14ED1  48 8B CE                        mov rcx, rsi
00A14ED4  48 89 8C 24 40 02 00 00         mov qword ptr [rsp + 0x240], rcx
00A14EDC  48 8D 8C 24 40 02 00 00         lea rcx, [rsp + 0x240]
00A14EE4  E8 03 BB 9A FF                  call 0x1403c09ec
00A14EE9  EB 43                           jmp 0x140a14f2e
00A14EEB  48 8D 8C 24 8C 00 00 00         lea rcx, [rsp + 0x8c]
00A14EF3  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00A14EF8  4C 8D 8C 24 E0 07 00 00         lea r9, [rsp + 0x7e0]
00A14F00  45 33 C0                        xor r8d, r8d
00A14F03  48 8D 94 24 90 04 00 00         lea rdx, [rsp + 0x490]
00A14F0B  48 8B C8                        mov rcx, rax
00A14F0E  E8 FD 97 8B FF                  call 0x1402ce710
00A14F13  0F B7 84 24 8C 00 00 00         movzx eax, word ptr [rsp + 0x8c]
00A14F1B  0F B7 84 44 E0 07 00 00         movzx eax, word ptr [rsp + rax*2 + 0x7e0]
00A14F23  48 8D 0D 96 A7 5B 00            lea rcx, [rip + 0x5ba796]
00A14F2A  48 8B 04 C1                     mov rax, qword ptr [rcx + rax*8]
00A14F2E  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
00A14F36  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
00A14F3D  41 09 86 F4 01 00 00            or dword ptr [r14 + 0x1f4], eax
00A14F44  8B 84 24 B4 00 00 00            mov eax, dword ptr [rsp + 0xb4]
00A14F4B  41 09 86 F0 01 00 00            or dword ptr [r14 + 0x1f0], eax
00A14F52  4C 8B A4 24 98 00 00 00         mov r12, qword ptr [rsp + 0x98]
00A14F5A  4D 85 E4                        test r12, r12
00A14F5D  0F 84 60 02 00 00               je 0x140a151c3
00A14F63  48 89 B4 24 88 01 00 00         mov qword ptr [rsp + 0x188], rsi
00A14F6B  8B FE                           mov edi, esi
00A14F6D  89 B4 24 F4 00 00 00            mov dword ptr [rsp + 0xf4], esi
00A14F74  83 E3 DF                        and ebx, 0xffffffdf
00A14F77  44 8A EE                        mov r13b, sil
00A14F7A  40 88 B4 24 88 00 00 00         mov byte ptr [rsp + 0x88], sil
00A14F82  39 B4 24 C8 08 00 00            cmp dword ptr [rsp + 0x8c8], esi
00A14F89  0F 84 EA 00 00 00               je 0x140a15079
00A14F8F  8A 94 24 80 00 00 00            mov dl, byte ptr [rsp + 0x80]
00A14F96  48 8B 0D 2B 4C 5C 00            mov rcx, qword ptr [rip + 0x5c4c2b]
00A14F9D  E8 7E CE E5 FF                  call 0x140871e20
00A14FA2  8B CB                           mov ecx, ebx
00A14FA4  0F BA F1 09                     btr ecx, 9
00A14FA8  0F BA EB 09                     bts ebx, 9
00A14FAC  84 C0                           test al, al
00A14FAE  0F 44 D9                        cmove ebx, ecx
00A14FB1  48 8D 94 24 88 00 00 00         lea rdx, [rsp + 0x88]
00A14FB9  48 8B 8C 24 00 01 00 00         mov rcx, qword ptr [rsp + 0x100]
00A14FC1  E8 FA 62 02 00                  call 0x140a3b2c0
00A14FC6  8B F8                           mov edi, eax
00A14FC8  85 C0                           test eax, eax
00A14FCA  0F 88 05 FD FF FF               js 0x140a14cd5
00A14FD0  44 8B EB                        mov r13d, ebx
00A14FD3  41 C1 ED 09                     shr r13d, 9
00A14FD7  40 38 B4 24 88 00 00 00         cmp byte ptr [rsp + 0x88], sil
00A14FDF  75 0A                           jne 0x140a14feb
00A14FE1  41 F6 C5 01                     test r13b, 1
00A14FE5  0F 84 E5 FC FF FF               je 0x140a14cd0
00A14FEB  48 8D 94 24 F4 00 00 00         lea rdx, [rsp + 0xf4]
00A14FF3  48 8B 8C 24 00 01 00 00         mov rcx, qword ptr [rsp + 0x100]
00A14FFB  E8 90 F4 FE FF                  call 0x140a04490
00A15000  8B F8                           mov edi, eax
00A15002  85 C0                           test eax, eax
00A15004  0F 88 CB FC FF FF               js 0x140a14cd5
00A1500A  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
00A15012  E8 D9 A8 81 FF                  call 0x14022f8f0
00A15017  8B BC 24 F4 00 00 00            mov edi, dword ptr [rsp + 0xf4]
00A1501E  3B F8                           cmp edi, eax
00A15020  74 21                           je 0x140a15043
00A15022  41 F6 C5 01                     test r13b, 1
00A15026  0F 84 A4 FC FF FF               je 0x140a14cd0
00A1502C  F6 84 24 90 00 00 00 80         test byte ptr [rsp + 0x90], 0x80
00A15034  74 0A                           je 0x140a15040
00A15036  BF 0D 00 00 C0                  mov edi, 0xc000000d
00A1503B  E9 95 FC FF FF                  jmp 0x140a14cd5
00A15040  83 CB 20                        or ebx, 0x20
00A15043  44 8A AC 24 88 00 00 00         mov r13b, byte ptr [rsp + 0x88]
00A1504B  44 8B E3                        mov r12d, ebx
00A1504E  41 83 E4 20                     and r12d, 0x20
00A15052  74 67                           je 0x140a150bb
00A15054  4C 8D 84 24 88 01 00 00         lea r8, [rsp + 0x188]
00A1505C  48 8D 94 24 60 04 00 00         lea rdx, [rsp + 0x460]
00A15064  8B CF                           mov ecx, edi
00A15066  E8 45 3E D7 FF                  call 0x140788eb0
00A1506B  8B F8                           mov edi, eax
00A1506D  85 C0                           test eax, eax
00A1506F  79 41                           jns 0x140a150b2
00A15071  83 E3 DF                        and ebx, 0xffffffdf
00A15074  E9 5C FC FF FF                  jmp 0x140a14cd5
00A15079  F6 C3 04                        test bl, 4
00A1507C  74 CD                           je 0x140a1504b
00A1507E  49 8B CC                        mov rcx, r12
00A15081  E8 6A A8 81 FF                  call 0x14022f8f0
00A15086  8B F8                           mov edi, eax
00A15088  89 84 24 F4 00 00 00            mov dword ptr [rsp + 0xf4], eax
00A1508F  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
00A15097  E8 54 A8 81 FF                  call 0x14022f8f0
00A1509C  8B CF                           mov ecx, edi
00A1509E  2B C8                           sub ecx, eax
00A150A0  F7 D9                           neg ecx
00A150A2  1B D2                           sbb edx, edx
00A150A4  83 E2 20                        and edx, 0x20
00A150A7  8B C3                           mov eax, ebx
00A150A9  83 E0 DF                        and eax, 0xffffffdf
00A150AC  8B DA                           mov ebx, edx
00A150AE  0B D8                           or ebx, eax
00A150B0  EB 99                           jmp 0x140a1504b
00A150B2  41 0F BA AE F0 01 00 00 07      bts dword ptr [r14 + 0x1f0], 7
00A150BB  39 B4 24 C8 08 00 00            cmp dword ptr [rsp + 0x8c8], esi
00A150C2  74 40                           je 0x140a15104
00A150C4  45 84 ED                        test r13b, r13b
00A150C7  75 3B                           jne 0x140a15104
00A150C9  4C 8B 84 24 00 01 00 00         mov r8, qword ptr [rsp + 0x100]
00A150D1  49 8B D6                        mov rdx, r14
00A150D4  33 C9                           xor ecx, ecx
00A150D6  E8 49 E0 0C 00                  call 0x140ae3124
00A150DB  8B F8                           mov edi, eax
00A150DD  85 C0                           test eax, eax
00A150DF  79 44                           jns 0x140a15125
00A150E1  45 85 E4                        test r12d, r12d
00A150E4  0F 84 EB FB FF FF               je 0x140a14cd5
00A150EA  48 8D 94 24 60 04 00 00         lea rdx, [rsp + 0x460]
00A150F2  48 8B 8C 24 88 01 00 00         mov rcx, qword ptr [rsp + 0x188]
00A150FA  E8 0D F7 80 FF                  call 0x14022480c
00A150FF  E9 D1 FB FF FF                  jmp 0x140a14cd5
00A15104  4C 8B A4 24 98 00 00 00         mov r12, qword ptr [rsp + 0x98]
00A1510C  49 8B D4                        mov rdx, r12
00A1510F  45 84 ED                        test r13b, r13b
00A15112  48 0F 45 94 24 E8 00 00 00      cmovne rdx, qword ptr [rsp + 0xe8]
00A1511B  49 8B CE                        mov rcx, r14
00A1511E  E8 61 9F 05 00                  call 0x140a6f084
00A15123  EB 08                           jmp 0x140a1512d
00A15125  4C 8B A4 24 98 00 00 00         mov r12, qword ptr [rsp + 0x98]
00A1512D  44 8B 8C 24 3C 04 00 00         mov r9d, dword ptr [rsp + 0x43c]
00A15135  41 BD 01 00 00 00               mov r13d, 1
00A1513B  45 23 CD                        and r9d, r13d
00A1513E  4C 8B 05 03 31 5C 00            mov r8, qword ptr [rip + 0x5c3103]
00A15145  4C 0F 45 84 24 50 04 00 00      cmovne r8, qword ptr [rsp + 0x450]
00A1514E  F7 84 24 90 00 00 00 00 00 40 00  test dword ptr [rsp + 0x90], 0x400000
00A15159  74 04                           je 0x140a1515f
00A1515B  41 83 C9 10                     or r9d, 0x10
00A1515F  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
00A15167  0F B7 08                        movzx ecx, word ptr [rax]
00A1516A  41 03 CD                        add ecx, r13d
00A1516D  4C 89 74 24 28                  mov qword ptr [rsp + 0x28], r14
00A15172  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00A15176  48 8B 8C 24 48 01 00 00         mov rcx, qword ptr [rsp + 0x148]
00A1517E  E8 D9 9C 04 00                  call 0x140a5ee5c
00A15183  0F B6 C0                        movzx eax, al
00A15186  C1 E0 0B                        shl eax, 0xb
00A15189  33 C3                           xor eax, ebx
00A1518B  BF 00 08 00 00                  mov edi, 0x800
00A15190  23 C7                           and eax, edi
00A15192  33 D8                           xor ebx, eax
00A15194  89 9C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ebx
00A1519B  F6 C3 20                        test bl, 0x20
00A1519E  74 15                           je 0x140a151b5
00A151A0  48 8D 94 24 60 04 00 00         lea rdx, [rsp + 0x460]
00A151A8  48 8B 8C 24 88 01 00 00         mov rcx, qword ptr [rsp + 0x188]
00A151B0  E8 57 F6 80 FF                  call 0x14022480c
00A151B5  85 DF                           test edi, ebx
00A151B7  75 2A                           jne 0x140a151e3
00A151B9  BF 9A 00 00 C0                  mov edi, 0xc000009a
00A151BE  E9 12 FB FF FF                  jmp 0x140a14cd5
00A151C3  33 D2                           xor edx, edx
00A151C5  49 8B CE                        mov rcx, r14
00A151C8  E8 B7 9E 05 00                  call 0x140a6f084
00A151CD  45 88 AE 60 01 00 00            mov byte ptr [r14 + 0x160], r13b
00A151D4  E8 13 32 DE FF                  call 0x1407f83ec
00A151D9  8B F8                           mov edi, eax
00A151DB  85 C0                           test eax, eax
00A151DD  0F 88 F2 FA FF FF               js 0x140a14cd5
00A151E3  F0 41 81 8E F4 01 00 00 00 00 04 00  lock or dword ptr [r14 + 0x1f4], 0x40000
00A151EF  4C 8B B4 24 A0 00 00 00         mov r14, qword ptr [rsp + 0xa0]
00A151F7  41 8B 86 88 03 00 00            mov eax, dword ptr [r14 + 0x388]
00A151FE  8B 8C 24 F8 00 00 00            mov ecx, dword ptr [rsp + 0xf8]
00A15205  A8 04                           test al, 4
00A15207  74 03                           je 0x140a1520c
00A15209  41 0B CD                        or ecx, r13d
00A1520C  44 8B 8C 24 68 01 00 00         mov r9d, dword ptr [rsp + 0x168]
00A15214  4D 03 CE                        add r9, r14
00A15217  44 8B C1                        mov r8d, ecx
00A1521A  41 83 C8 02                     or r8d, 2
00A1521E  0F BA E3 10                     bt ebx, 0x10
00A15222  44 0F 43 C1                     cmovae r8d, ecx
00A15226  49 8B CE                        mov rcx, r14
00A15229  E8 32 9A 05 00                  call 0x140a6ec60
00A1522E  4C 89 4C 24 40                  mov qword ptr [rsp + 0x40], r9
00A15233  44 89 44 24 38                  mov dword ptr [rsp + 0x38], r8d
00A15238  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A1523D  48 8B 84 24 B8 00 00 00         mov rax, qword ptr [rsp + 0xb8]
00A15245  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A1524A  4C 8D 8C 24 90 04 00 00         lea r9, [rsp + 0x490]
00A15252  44 0F B7 84 24 8C 00 00 00      movzx r8d, word ptr [rsp + 0x8c]
00A1525B  BA 08 00 00 00                  mov edx, 8
00A15260  E8 8F EA 04 00                  call 0x140a63cf4
00A15265  8B F8                           mov edi, eax
00A15267  85 C0                           test eax, eax
00A15269  0F 88 66 FA FF FF               js 0x140a14cd5
00A1526F  4D 85 FF                        test r15, r15
00A15272  0F 84 36 01 00 00               je 0x140a153ae
00A15278  F6 C3 02                        test bl, 2
00A1527B  0F 85 2D 01 00 00               jne 0x140a153ae
00A15281  41 8B 87 80 01 00 00            mov eax, dword ptr [r15 + 0x180]
00A15288  89 84 24 24 01 00 00            mov dword ptr [rsp + 0x124], eax
00A1528F  41 8B 87 84 01 00 00            mov eax, dword ptr [r15 + 0x184]
00A15296  89 84 24 20 01 00 00            mov dword ptr [rsp + 0x120], eax
00A1529D  49 8B 87 98 01 00 00            mov rax, qword ptr [r15 + 0x198]
00A152A4  48 89 84 24 C8 01 00 00         mov qword ptr [rsp + 0x1c8], rax
00A152AC  41 8B 87 88 01 00 00            mov eax, dword ptr [r15 + 0x188]
00A152B3  89 84 24 1C 01 00 00            mov dword ptr [rsp + 0x11c], eax
00A152BA  49 8B 87 D8 00 00 00            mov rax, qword ptr [r15 + 0xd8]
00A152C1  48 89 84 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], rax
00A152C9  49 8B BF 90 01 00 00            mov rdi, qword ptr [r15 + 0x190]
00A152D0  41 8B 87 8C 01 00 00            mov eax, dword ptr [r15 + 0x18c]
00A152D7  89 84 24 D4 00 00 00            mov dword ptr [rsp + 0xd4], eax
00A152DE  49 8B 8F B8 00 00 00            mov rcx, qword ptr [r15 + 0xb8]
00A152E5  48 85 C9                        test rcx, rcx
00A152E8  0F 84 C3 00 00 00               je 0x140a153b1
00A152EE  48 8B 05 0B FC 4E 00            mov rax, qword ptr [rip + 0x4efc0b]
00A152F5  48 85 C0                        test rax, rax
00A152F8  0F 84 B3 00 00 00               je 0x140a153b1
00A152FE  48 8D 94 24 A0 05 00 00         lea rdx, [rsp + 0x5a0]
00A15306  E8 C5 57 CA FF                  call 0x1406baad0
00A1530B  85 C0                           test eax, eax
00A1530D  0F 88 9E 00 00 00               js 0x140a153b1
00A15313  39 B4 24 A0 05 00 00            cmp dword ptr [rsp + 0x5a0], esi
00A1531A  75 7D                           jne 0x140a15399
00A1531C  48 85 FF                        test rdi, rdi
00A1531F  74 78                           je 0x140a15399
00A15321  81 BC 24 D4 00 00 00 0C 02 00 00  cmp dword ptr [rsp + 0xd4], 0x20c
00A1532C  75 6B                           jne 0x140a15399
00A1532E  48 8D 8C 24 A0 05 00 00         lea rcx, [rsp + 0x5a0]
00A15336  B8 04 00 00 00                  mov eax, 4
00A1533B  0F 10 07                        movups xmm0, xmmword ptr [rdi]
00A1533E  0F 11 01                        movups xmmword ptr [rcx], xmm0
00A15341  0F 10 4F 10                     movups xmm1, xmmword ptr [rdi + 0x10]
00A15345  0F 11 49 10                     movups xmmword ptr [rcx + 0x10], xmm1
00A15349  0F 10 47 20                     movups xmm0, xmmword ptr [rdi + 0x20]
00A1534D  0F 11 41 20                     movups xmmword ptr [rcx + 0x20], xmm0
00A15351  0F 10 4F 30                     movups xmm1, xmmword ptr [rdi + 0x30]
00A15355  0F 11 49 30                     movups xmmword ptr [rcx + 0x30], xmm1
00A15359  0F 10 47 40                     movups xmm0, xmmword ptr [rdi + 0x40]
00A1535D  0F 11 41 40                     movups xmmword ptr [rcx + 0x40], xmm0
00A15361  0F 10 4F 50                     movups xmm1, xmmword ptr [rdi + 0x50]
00A15365  0F 11 49 50                     movups xmmword ptr [rcx + 0x50], xmm1
00A15369  0F 10 47 60                     movups xmm0, xmmword ptr [rdi + 0x60]
00A1536D  0F 11 41 60                     movups xmmword ptr [rcx + 0x60], xmm0
00A15371  48 8D 89 80 00 00 00            lea rcx, [rcx + 0x80]
00A15378  0F 10 4F 70                     movups xmm1, xmmword ptr [rdi + 0x70]
00A1537C  0F 11 49 F0                     movups xmmword ptr [rcx - 0x10], xmm1
00A15380  48 8D BF 80 00 00 00            lea rdi, [rdi + 0x80]
00A15387  48 83 E8 01                     sub rax, 1
00A1538B  75 AE                           jne 0x140a1533b
00A1538D  48 8B 07                        mov rax, qword ptr [rdi]
00A15390  48 89 01                        mov qword ptr [rcx], rax
00A15393  8B 47 08                        mov eax, dword ptr [rdi + 8]
00A15396  89 41 08                        mov dword ptr [rcx + 8], eax
00A15399  48 8D BC 24 A0 05 00 00         lea rdi, [rsp + 0x5a0]
00A153A1  C7 84 24 D4 00 00 00 18 02 00 00  mov dword ptr [rsp + 0xd4], 0x218
00A153AC  EB 03                           jmp 0x140a153b1
00A153AE  48 8B FE                        mov rdi, rsi
00A153B1  E8 D2 A3 AD FF                  call 0x1404ef788
00A153B6  85 C0                           test eax, eax
00A153B8  74 1C                           je 0x140a153d6
00A153BA  4D 85 FF                        test r15, r15
00A153BD  74 17                           je 0x140a153d6
00A153BF  49 0F BA 67 08 23               bt qword ptr [r15 + 8], 0x23
00A153C5  73 0F                           jae 0x140a153d6
00A153C7  49 8D 87 F0 01 00 00            lea rax, [r15 + 0x1f0]
00A153CE  48 89 84 24 B8 01 00 00         mov qword ptr [rsp + 0x1b8], rax
00A153D6  8B CB                           mov ecx, ebx
00A153D8  C1 E9 10                        shr ecx, 0x10
00A153DB  41 23 CD                        and ecx, r13d
00A153DE  8B C3                           mov eax, ebx
00A153E0  C1 E8 04                        shr eax, 4
00A153E3  41 23 C5                        and eax, r13d
00A153E6  48 8B 94 24 20 02 00 00         mov rdx, qword ptr [rsp + 0x220]
00A153EE  48 89 54 24 70                  mov qword ptr [rsp + 0x70], rdx
00A153F3  48 8B 94 24 B8 01 00 00         mov rdx, qword ptr [rsp + 0x1b8]
00A153FB  48 89 54 24 68                  mov qword ptr [rsp + 0x68], rdx
00A15400  48 8B 94 24 C0 01 00 00         mov rdx, qword ptr [rsp + 0x1c0]
00A15408  48 89 54 24 60                  mov qword ptr [rsp + 0x60], rdx
00A1540D  8B 94 24 1C 01 00 00            mov edx, dword ptr [rsp + 0x11c]
00A15414  89 54 24 58                     mov dword ptr [rsp + 0x58], edx
00A15418  48 8B 94 24 C8 01 00 00         mov rdx, qword ptr [rsp + 0x1c8]
00A15420  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
00A15425  8B 94 24 D4 00 00 00            mov edx, dword ptr [rsp + 0xd4]
00A1542C  89 54 24 48                     mov dword ptr [rsp + 0x48], edx
00A15430  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
00A15435  8B 94 24 20 01 00 00            mov edx, dword ptr [rsp + 0x120]
00A1543C  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
00A15440  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00A15444  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00A15448  8B 84 24 24 01 00 00            mov eax, dword ptr [rsp + 0x124]
00A1544F  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00A15453  44 8B 8C 24 C8 08 00 00         mov r9d, dword ptr [rsp + 0x8c8]
00A1545B  4C 8B 84 24 00 01 00 00         mov r8, qword ptr [rsp + 0x100]
00A15463  49 8B D6                        mov rdx, r14
00A15466  49 8B CC                        mov rcx, r12
00A15469  E8 FA 7E 09 00                  call 0x140aad368
00A1546E  8B F8                           mov edi, eax
00A15470  85 C0                           test eax, eax
00A15472  0F 88 5D F8 FF FF               js 0x140a14cd5
00A15478  41 C6 86 47 03 00 00 02         mov byte ptr [r14 + 0x347], 2
00A15480  4D 85 E4                        test r12, r12
00A15483  74 55                           je 0x140a154da
00A15485  41 8A 8C 24 47 03 00 00         mov cl, byte ptr [r12 + 0x347]
00A1548D  8A C1                           mov al, cl
00A1548F  41 2A C5                        sub al, r13b
00A15492  A8 FB                           test al, 0xfb
00A15494  75 07                           jne 0x140a1549d
00A15496  41 88 8E 47 03 00 00            mov byte ptr [r14 + 0x347], cl
00A1549D  4D 85 FF                        test r15, r15
00A154A0  74 09                           je 0x140a154ab
00A154A2  4D 8B 8F 28 01 00 00            mov r9, qword ptr [r15 + 0x128]
00A154A9  EB 03                           jmp 0x140a154ae
00A154AB  4C 8B CE                        mov r9, rsi
00A154AE  4D 85 FF                        test r15, r15
00A154B1  74 09                           je 0x140a154bc
00A154B3  45 8B 87 24 01 00 00            mov r8d, dword ptr [r15 + 0x124]
00A154BA  EB 03                           jmp 0x140a154bf
00A154BC  44 8B C6                        mov r8d, esi
00A154BF  8B 84 24 B0 08 00 00            mov eax, dword ptr [rsp + 0x8b0]
00A154C6  24 04                           and al, 4
00A154C8  F6 D8                           neg al
00A154CA  48 1B C9                        sbb rcx, rcx
00A154CD  49 23 CC                        and rcx, r12
00A154D0  49 8B D6                        mov rdx, r14
00A154D3  E8 54 71 F3 FF                  call 0x14094c62c
00A154D8  EB 1E                           jmp 0x140a154f8
00A154DA  48 8B 84 24 E8 00 00 00         mov rax, qword ptr [rsp + 0xe8]
00A154E2  48 8B 80 00 03 00 00            mov rax, qword ptr [rax + 0x300]
00A154E9  49 89 86 00 03 00 00            mov qword ptr [r14 + 0x300], rax
00A154F0  49 8B CE                        mov rcx, r14
00A154F3  E8 40 BC 0A 00                  call 0x140ac1138
00A154F8  85 C0                           test eax, eax
00A154FA  8B F8                           mov edi, eax
00A154FC  0F 88 D3 F7 FF FF               js 0x140a14cd5
00A15502  40 8A BC 24 80 00 00 00         mov dil, byte ptr [rsp + 0x80]
00A1550A  F6 84 24 38 04 00 00 07         test byte ptr [rsp + 0x438], 7
00A15512  74 13                           je 0x140a15527
00A15514  44 8A C7                        mov r8b, dil
00A15517  48 8D 94 24 38 04 00 00         lea rdx, [rsp + 0x438]
00A1551F  49 8B CE                        mov rcx, r14
00A15522  E8 B1 E9 D6 FF                  call 0x140783ed8
00A15527  0F BA E3 15                     bt ebx, 0x15
00A1552B  73 1F                           jae 0x140a1554c
00A1552D  40 88 74 24 20                  mov byte ptr [rsp + 0x20], sil
00A15532  45 8A CD                        mov r9b, r13b
00A15535  4C 8B 84 24 A0 01 00 00         mov r8, qword ptr [rsp + 0x1a0]
00A1553D  8B 94 24 C4 00 00 00            mov edx, dword ptr [rsp + 0xc4]
00A15544  49 8B CE                        mov rcx, r14
00A15547  E8 88 BB BA FF                  call 0x1405c10d4
00A1554C  F6 84 24 3C 04 00 00 02         test byte ptr [rsp + 0x43c], 2
00A15554  74 0F                           je 0x140a15565
00A15556  8B 94 24 58 04 00 00            mov edx, dword ptr [rsp + 0x458]
00A1555D  49 8B CE                        mov rcx, r14
00A15560  E8 5B C5 BA FF                  call 0x1405c1ac0
00A15565  4D 85 FF                        test r15, r15
00A15568  74 27                           je 0x140a15591
00A1556A  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
00A1556E  48 0F BA E0 08                  bt rax, 8
00A15573  73 1C                           jae 0x140a15591
00A15575  44 8A CF                        mov r9b, dil
00A15578  45 33 C0                        xor r8d, r8d
00A1557B  41 8A 57 02                     mov dl, byte ptr [r15 + 2]
00A1557F  49 8B CE                        mov rcx, r14
00A15582  E8 5D 0C FE FF                  call 0x1409f61e4
00A15587  8B F8                           mov edi, eax
00A15589  85 C0                           test eax, eax
00A1558B  0F 88 44 F7 FF FF               js 0x140a14cd5
00A15591  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00A15596  45 33 C9                        xor r9d, r9d
00A15599  4C 8D 84 24 94 00 00 00         lea r8, [rsp + 0x94]
00A155A1  33 D2                           xor edx, edx
00A155A3  49 8B CE                        mov rcx, r14
00A155A6  E8 05 6A 02 00                  call 0x140a3bfb0
00A155AB  41 88 86 90 00 00 00            mov byte ptr [r14 + 0x90], al
00A155B2  8A 84 24 94 00 00 00            mov al, byte ptr [rsp + 0x94]
00A155B9  41 88 86 91 00 00 00            mov byte ptr [r14 + 0x91], al
00A155C0  89 B4 24 C4 00 00 00            mov dword ptr [rsp + 0xc4], esi
00A155C7  48 8D 94 24 00 04 00 00         lea rdx, [rsp + 0x400]
00A155CF  49 8B CF                        mov rcx, r15
00A155D2  E8 15 7A 01 00                  call 0x140a2cfec
00A155D7  0F 10 84 24 00 04 00 00         movups xmm0, xmmword ptr [rsp + 0x400]
00A155DF  0F 29 84 24 B0 02 00 00         movaps xmmword ptr [rsp + 0x2b0], xmm0
00A155E7  F2 0F 10 84 24 10 04 00 00      movsd xmm0, qword ptr [rsp + 0x410]
00A155F0  F2 0F 11 84 24 C0 02 00 00      movsd qword ptr [rsp + 0x2c0], xmm0
00A155F9  0F 10 0D 08 1B 5B 00            movups xmm1, xmmword ptr [rip + 0x5b1b08]
00A15600  0F 29 8C 24 D0 02 00 00         movaps xmmword ptr [rsp + 0x2d0], xmm1
00A15608  F2 0F 10 05 08 1B 5B 00         movsd xmm0, qword ptr [rip + 0x5b1b08]
00A15610  F2 0F 11 84 24 E0 02 00 00      movsd qword ptr [rsp + 0x2e0], xmm0
00A15619  4C 8D 84 24 00 04 00 00         lea r8, [rsp + 0x400]
00A15621  48 8D 94 24 B0 02 00 00         lea rdx, [rsp + 0x2b0]
00A15629  48 8D 8C 24 D0 02 00 00         lea rcx, [rsp + 0x2d0]
00A15631  E8 2E 19 00 00                  call 0x140a16f64
00A15636  48 8D 94 24 18 04 00 00         lea rdx, [rsp + 0x418]
00A1563E  49 8B CF                        mov rcx, r15
00A15641  E8 1E 79 01 00                  call 0x140a2cf64
00A15646  0F 10 84 24 18 04 00 00         movups xmm0, xmmword ptr [rsp + 0x418]
00A1564E  0F 29 84 24 F0 02 00 00         movaps xmmword ptr [rsp + 0x2f0], xmm0
00A15656  F2 0F 10 84 24 28 04 00 00      movsd xmm0, qword ptr [rsp + 0x428]
00A1565F  F2 0F 11 84 24 00 03 00 00      movsd qword ptr [rsp + 0x300], xmm0
00A15668  0F 10 0D 01 1D 5B 00            movups xmm1, xmmword ptr [rip + 0x5b1d01]
00A1566F  0F 29 8C 24 10 03 00 00         movaps xmmword ptr [rsp + 0x310], xmm1
00A15677  F2 0F 10 05 01 1D 5B 00         movsd xmm0, qword ptr [rip + 0x5b1d01]
00A1567F  F2 0F 11 84 24 20 03 00 00      movsd qword ptr [rsp + 0x320], xmm0
00A15688  4C 8D 84 24 18 04 00 00         lea r8, [rsp + 0x418]
00A15690  48 8D 94 24 F0 02 00 00         lea rdx, [rsp + 0x2f0]
00A15698  48 8D 8C 24 10 03 00 00         lea rcx, [rsp + 0x310]
00A156A0  E8 DF 15 00 00                  call 0x140a16c84
00A156A5  48 8B BC 24 00 04 00 00         mov rdi, qword ptr [rsp + 0x400]
00A156AD  48 C1 EF 30                     shr rdi, 0x30
00A156B1  83 E7 03                        and edi, 3
00A156B4  C1 E7 0E                        shl edi, 0xe
00A156B7  4D 85 FF                        test r15, r15
00A156BA  0F 84 DD 00 00 00               je 0x140a1579d
00A156C0  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
00A156C4  48 0F BA E0 10                  bt rax, 0x10
00A156C9  73 61                           jae 0x140a1572c
00A156CB  41 0F 10 87 50 01 00 00         movups xmm0, xmmword ptr [r15 + 0x150]
00A156D3  0F 29 84 24 30 03 00 00         movaps xmmword ptr [rsp + 0x330], xmm0
00A156DB  F2 41 0F 10 8F 60 01 00 00      movsd xmm1, qword ptr [r15 + 0x160]
00A156E4  F2 0F 11 8C 24 40 03 00 00      movsd qword ptr [rsp + 0x340], xmm1
00A156ED  0F 10 84 24 00 04 00 00         movups xmm0, xmmword ptr [rsp + 0x400]
00A156F5  0F 29 84 24 50 03 00 00         movaps xmmword ptr [rsp + 0x350], xmm0
00A156FD  F2 0F 10 84 24 10 04 00 00      movsd xmm0, qword ptr [rsp + 0x410]
00A15706  F2 0F 11 84 24 60 03 00 00      movsd qword ptr [rsp + 0x360], xmm0
00A1570F  4C 8D 84 24 00 04 00 00         lea r8, [rsp + 0x400]
00A15717  48 8D 94 24 30 03 00 00         lea rdx, [rsp + 0x330]
00A1571F  48 8D 8C 24 50 03 00 00         lea rcx, [rsp + 0x350]
00A15727  E8 38 18 00 00                  call 0x140a16f64
00A1572C  4D 85 FF                        test r15, r15
00A1572F  74 6C                           je 0x140a1579d
00A15731  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
00A15735  48 0F BA E0 1B                  bt rax, 0x1b
00A1573A  73 61                           jae 0x140a1579d
00A1573C  41 0F 10 87 C0 01 00 00         movups xmm0, xmmword ptr [r15 + 0x1c0]
00A15744  0F 29 84 24 70 03 00 00         movaps xmmword ptr [rsp + 0x370], xmm0
00A1574C  F2 41 0F 10 8F D0 01 00 00      movsd xmm1, qword ptr [r15 + 0x1d0]
00A15755  F2 0F 11 8C 24 80 03 00 00      movsd qword ptr [rsp + 0x380], xmm1
00A1575E  0F 10 84 24 18 04 00 00         movups xmm0, xmmword ptr [rsp + 0x418]
00A15766  0F 29 84 24 90 03 00 00         movaps xmmword ptr [rsp + 0x390], xmm0
00A1576E  F2 0F 10 84 24 28 04 00 00      movsd xmm0, qword ptr [rsp + 0x428]
00A15777  F2 0F 11 84 24 A0 03 00 00      movsd qword ptr [rsp + 0x3a0], xmm0
00A15780  4C 8D 84 24 18 04 00 00         lea r8, [rsp + 0x418]
00A15788  48 8D 94 24 70 03 00 00         lea rdx, [rsp + 0x370]
00A15790  48 8D 8C 24 90 03 00 00         lea rcx, [rsp + 0x390]
00A15798  E8 E7 14 00 00                  call 0x140a16c84
00A1579D  39 B4 24 E4 00 00 00            cmp dword ptr [rsp + 0xe4], esi
00A157A4  74 03                           je 0x140a157a9
00A157A6  83 CF 04                        or edi, 4
00A157A9  44 8B DF                        mov r11d, edi
00A157AC  41 83 CB 40                     or r11d, 0x40
00A157B0  40 F6 C7 04                     test dil, 4
00A157B4  44 0F 44 DF                     cmove r11d, edi
00A157B8  41 F7 C3 C0 3F 00 00            test r11d, 0x3fc0
00A157BF  74 0D                           je 0x140a157ce
00A157C1  48 8D 8C 24 00 04 00 00         lea rcx, [rsp + 0x400]
00A157C9  E8 F2 33 06 00                  call 0x140a78bc0
00A157CE  E8 E1 CA A8 FF                  call 0x1404a22b4
00A157D3  49 B9 FF FF FF FF FF FF FF EF   movabs r9, 0xefffffffffffffff
00A157DD  49 BA 00 00 00 00 00 00 00 20   movabs r10, 0x2000000000000000
00A157E7  84 C0                           test al, al
00A157E9  75 16                           jne 0x140a15801
00A157EB  48 8B 84 24 08 04 00 00         mov rax, qword ptr [rsp + 0x408]
00A157F3  49 23 C1                        and rax, r9
00A157F6  49 0B C2                        or rax, r10
00A157F9  48 89 84 24 08 04 00 00         mov qword ptr [rsp + 0x408], rax
00A15801  0F B7 8C 24 A8 00 00 00         movzx ecx, word ptr [rsp + 0xa8]
00A15809  0F B7 D1                        movzx edx, cx
00A1580C  B8 00 40 00 00                  mov eax, 0x4000
00A15811  66 23 D0                        and dx, ax
00A15814  F7 C3 00 60 00 00               test ebx, 0x6000
00A1581A  44 8B C6                        mov r8d, esi
00A1581D  41 0F 95 C0                     setne r8b
00A15821  8B C1                           mov eax, ecx
00A15823  C1 E8 04                        shr eax, 4
00A15826  83 E0 02                        and eax, 2
00A15829  44 0B C0                        or r8d, eax
00A1582C  0F B7 C2                        movzx eax, dx
00A1582F  66 F7 D8                        neg ax
00A15832  1B C9                           sbb ecx, ecx
00A15834  83 E1 08                        and ecx, 8
00A15837  44 0B C1                        or r8d, ecx
00A1583A  45 0B C3                        or r8d, r11d
00A1583D  66 85 D2                        test dx, dx
00A15840  74 06                           je 0x140a15848
00A15842  0F BA E3 12                     bt ebx, 0x12
00A15846  72 07                           jb 0x140a1584f
00A15848  89 B4 24 28 01 00 00            mov dword ptr [rsp + 0x128], esi
00A1584F  8B CB                           mov ecx, ebx
00A15851  D1 E9                           shr ecx, 1
00A15853  8B F9                           mov edi, ecx
00A15855  81 E7 00 00 E0 03               and edi, 0x3e00000
00A1585B  8B C3                           mov eax, ebx
00A1585D  25 00 00 10 00                  and eax, 0x100000
00A15862  0B F8                           or edi, eax
00A15864  C1 EF 04                        shr edi, 4
00A15867  41 0B F8                        or edi, r8d
00A1586A  0B BC 24 28 01 00 00            or edi, dword ptr [rsp + 0x128]
00A15871  41 84 CD                        test r13b, cl
00A15874  0F 84 8C 00 00 00               je 0x140a15906
00A1587A  48 8B 8C 24 00 04 00 00         mov rcx, qword ptr [rsp + 0x400]
00A15882  48 B8 FF FF FF FF FF FE FF FF   movabs rax, 0xfffffeffffffffff
00A1588C  48 23 C8                        and rcx, rax
00A1588F  48 B8 00 00 00 00 00 02 00 00   movabs rax, 0x20000000000
00A15899  48 0B C8                        or rcx, rax
00A1589C  48 89 8C 24 00 04 00 00         mov qword ptr [rsp + 0x400], rcx
00A158A4  48 8B 84 24 08 04 00 00         mov rax, qword ptr [rsp + 0x408]
00A158AC  48 BA FE FF FF FF FF FF FF EF   movabs rdx, 0xeffffffffffffffe
00A158B6  48 23 C2                        and rax, rdx
00A158B9  48 BA 02 00 00 00 00 00 00 20   movabs rdx, 0x2000000000000002
00A158C3  48 0B C2                        or rax, rdx
00A158C6  48 89 84 24 08 04 00 00         mov qword ptr [rsp + 0x408], rax
00A158CE  48 81 E1 FF FF FC FF            and rcx, 0xfffffffffffcffff
00A158D5  F6 84 24 B8 08 00 00 02         test byte ptr [rsp + 0x8b8], 2
00A158DD  74 0E                           je 0x140a158ed
00A158DF  48 0F BA F1 14                  btr rcx, 0x14
00A158E4  48 81 C9 00 00 22 00            or rcx, 0x220000
00A158EB  EB 11                           jmp 0x140a158fe
00A158ED  48 0F BA E9 10                  bts rcx, 0x10
00A158F2  48 81 E1 FF FF CF FF            and rcx, 0xffffffffffcfffff
00A158F9  48 0F BA E9 14                  bts rcx, 0x14
00A158FE  48 89 8C 24 00 04 00 00         mov qword ptr [rsp + 0x400], rcx
00A15906  F6 C3 04                        test bl, 4
00A15909  74 24                           je 0x140a1592f
00A1590B  41 F7 84 24 54 07 00 00 00 40 00 00  test dword ptr [r12 + 0x754], 0x4000
00A15917  75 16                           jne 0x140a1592f
00A15919  48 8B 84 24 08 04 00 00         mov rax, qword ptr [rsp + 0x408]
00A15921  49 23 C1                        and rax, r9
00A15924  49 0B C2                        or rax, r10
00A15927  48 89 84 24 08 04 00 00         mov qword ptr [rsp + 0x408], rax
00A1592F  F6 C3 40                        test bl, 0x40
00A15932  74 16                           je 0x140a1594a
00A15934  48 8B 84 24 08 04 00 00         mov rax, qword ptr [rsp + 0x408]
00A1593C  49 23 C1                        and rax, r9
00A1593F  49 0B C2                        or rax, r10
00A15942  48 89 84 24 08 04 00 00         mov qword ptr [rsp + 0x408], rax
00A1594A  48 8B 8C 24 10 04 00 00         mov rcx, qword ptr [rsp + 0x410]
00A15952  48 0F BA F1 0C                  btr rcx, 0xc
00A15957  48 0F BA E9 0D                  bts rcx, 0xd
00A1595C  48 89 8C 24 10 04 00 00         mov qword ptr [rsp + 0x410], rcx
00A15964  E8 1F 1A A9 FF                  call 0x1404a7388
00A15969  84 C0                           test al, al
00A1596B  75 12                           jne 0x140a1597f
00A1596D  48 0F BA F1 18                  btr rcx, 0x18
00A15972  48 0F BA E9 19                  bts rcx, 0x19
00A15977  48 89 8C 24 10 04 00 00         mov qword ptr [rsp + 0x410], rcx
00A1597F  E8 E4 7F BB FF                  call 0x1405cd968
00A15984  85 C0                           test eax, eax
00A15986  74 42                           je 0x140a159ca
00A15988  4D 85 FF                        test r15, r15
00A1598B  74 17                           je 0x140a159a4
00A1598D  49 0F BA 67 08 24               bt qword ptr [r15 + 8], 0x24
00A15993  73 0F                           jae 0x140a159a4
00A15995  49 8D 87 10 02 00 00            lea rax, [r15 + 0x210]
00A1599C  48 89 84 24 F8 01 00 00         mov qword ptr [rsp + 0x1f8], rax
00A159A4  48 8D 94 24 30 04 00 00         lea rdx, [rsp + 0x430]
00A159AC  49 8B CF                        mov rcx, r15
00A159AF  E8 88 EB D6 FF                  call 0x14078453c
00A159B4  48 8D 8C 24 30 04 00 00         lea rcx, [rsp + 0x430]
00A159BC  85 C0                           test eax, eax
00A159BE  48 0F 48 CE                     cmovs rcx, rsi
00A159C2  48 89 8C 24 90 01 00 00         mov qword ptr [rsp + 0x190], rcx
00A159CA  8B 84 24 D8 00 00 00            mov eax, dword ptr [rsp + 0xd8]
00A159D1  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A159D5  8B 84 24 DC 00 00 00            mov eax, dword ptr [rsp + 0xdc]
00A159DC  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00A159E0  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00A159E4  4C 8D 8C 24 18 04 00 00         lea r9, [rsp + 0x418]
00A159EC  4C 8D 84 24 00 04 00 00         lea r8, [rsp + 0x400]
00A159F4  49 8B D4                        mov rdx, r12
00A159F7  49 8B CE                        mov rcx, r14
00A159FA  E8 AD 3F 05 00                  call 0x140a699ac
00A159FF  4D 85 FF                        test r15, r15
00A15A02  0F 84 BA 00 00 00               je 0x140a15ac2
00A15A08  49 8B 87 B0 01 00 00            mov rax, qword ptr [r15 + 0x1b0]
00A15A0F  48 85 C0                        test rax, rax
00A15A12  74 4B                           je 0x140a15a5f
00A15A14  8B 00                           mov eax, dword ptr [rax]
00A15A16  49 8D 96 50 07 00 00            lea rdx, [r14 + 0x750]
00A15A1D  41 84 C5                        test r13b, al
00A15A20  74 0F                           je 0x140a15a31
00A15A22  F0 81 0A 00 40 00 00            lock or dword ptr [rdx], 0x4000
00A15A29  4C 8B B4 24 A0 00 00 00         mov r14, qword ptr [rsp + 0xa0]
00A15A31  49 8B 87 B0 01 00 00            mov rax, qword ptr [r15 + 0x1b0]
00A15A38  8B 08                           mov ecx, dword ptr [rax]
00A15A3A  F6 C1 02                        test cl, 2
00A15A3D  74 0F                           je 0x140a15a4e
00A15A3F  F0 81 0A 00 80 00 00            lock or dword ptr [rdx], 0x8000
00A15A46  4C 8B B4 24 A0 00 00 00         mov r14, qword ptr [rsp + 0xa0]
00A15A4E  49 8B 87 B0 01 00 00            mov rax, qword ptr [r15 + 0x1b0]
00A15A55  8B 48 04                        mov ecx, dword ptr [rax + 4]
00A15A58  41 89 8E E8 06 00 00            mov dword ptr [r14 + 0x6e8], ecx
00A15A5F  4D 85 FF                        test r15, r15
00A15A62  74 5E                           je 0x140a15ac2
00A15A64  49 8B 87 B8 01 00 00            mov rax, qword ptr [r15 + 0x1b8]
00A15A6B  48 85 C0                        test rax, rax
00A15A6E  74 09                           je 0x140a15a79
00A15A70  8B 00                           mov eax, dword ptr [rax]
00A15A72  41 89 86 A0 07 00 00            mov dword ptr [r14 + 0x7a0], eax
00A15A79  4D 85 FF                        test r15, r15
00A15A7C  74 44                           je 0x140a15ac2
00A15A7E  0F 10 84 24 00 04 00 00         movups xmm0, xmmword ptr [rsp + 0x400]
00A15A86  41 0F 11 87 50 01 00 00         movups xmmword ptr [r15 + 0x150], xmm0
00A15A8E  F2 0F 10 84 24 10 04 00 00      movsd xmm0, qword ptr [rsp + 0x410]
00A15A97  F2 41 0F 11 87 60 01 00 00      movsd qword ptr [r15 + 0x160], xmm0
00A15AA0  0F 10 8C 24 18 04 00 00         movups xmm1, xmmword ptr [rsp + 0x418]
00A15AA8  41 0F 11 8F C0 01 00 00         movups xmmword ptr [r15 + 0x1c0], xmm1
00A15AB0  F2 0F 10 84 24 28 04 00 00      movsd xmm0, qword ptr [rsp + 0x428]
00A15AB9  F2 41 0F 11 87 D0 01 00 00      movsd qword ptr [r15 + 0x1d0], xmm0
00A15AC2  48 89 B4 24 28 02 00 00         mov qword ptr [rsp + 0x228], rsi
00A15ACA  48 89 B4 24 30 02 00 00         mov qword ptr [rsp + 0x230], rsi
00A15AD2  48 8D 84 24 28 02 00 00         lea rax, [rsp + 0x228]
00A15ADA  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A15ADF  4C 8D 8C 24 30 02 00 00         lea r9, [rsp + 0x230]
00A15AE7  4C 8D 84 24 E0 00 00 00         lea r8, [rsp + 0xe0]
00A15AEF  41 8B D5                        mov edx, r13d
00A15AF2  48 8B 8C 24 00 01 00 00         mov rcx, qword ptr [rsp + 0x100]
00A15AFA  E8 ED 9F A8 FF                  call 0x14049faec
00A15AFF  8B F8                           mov edi, eax
00A15B01  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
00A15B08  85 FF                           test edi, edi
00A15B0A  B9 00 00 01 00                  mov ecx, 0x10000
00A15B0F  0F 48 C1                        cmovs eax, ecx
00A15B12  89 84 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], eax
00A15B19  8B CE                           mov ecx, esi
00A15B1B  3D 01 00 01 00                  cmp eax, 0x10001
00A15B20  41 0F 44 CD                     cmove ecx, r13d
00A15B24  8B D1                           mov edx, ecx
00A15B26  83 CA 02                        or edx, 2
00A15B29  F7 84 24 B0 08 00 00 00 00 02 00  test dword ptr [rsp + 0x8b0], 0x20000
00A15B34  0F 44 D1                        cmove edx, ecx
00A15B37  49 8B CE                        mov rcx, r14
00A15B3A  E8 C5 AF 03 00                  call 0x140a50b04
00A15B3F  41 F7 86 54 07 00 00 00 40 00 00  test dword ptr [r14 + 0x754], 0x4000
00A15B4A  74 12                           je 0x140a15b5e
00A15B4C  49 8B CE                        mov rcx, r14
00A15B4F  E8 E0 7B 08 00                  call 0x140a9d734
00A15B54  8B F8                           mov edi, eax
00A15B56  85 C0                           test eax, eax
00A15B58  0F 88 77 F1 FF FF               js 0x140a14cd5
00A15B5E  F6 84 24 B0 08 00 00 80         test byte ptr [rsp + 0x8b0], 0x80
00A15B66  74 2C                           je 0x140a15b94
00A15B68  48 8B 8C 24 E8 00 00 00         mov rcx, qword ptr [rsp + 0xe8]
00A15B70  E8 B3 9B 07 00                  call 0x140a8f728
00A15B75  85 C0                           test eax, eax
00A15B77  75 1B                           jne 0x140a15b94
00A15B79  8A 94 24 80 00 00 00            mov dl, byte ptr [rsp + 0x80]
00A15B80  48 8B 0D 99 3F 5C 00            mov rcx, qword ptr [rip + 0x5c3f99]
00A15B87  E8 94 C2 E5 FF                  call 0x140871e20
00A15B8C  84 C0                           test al, al
00A15B8E  0F 84 3C F1 FF FF               je 0x140a14cd0
00A15B94  41 84 DD                        test r13b, bl
00A15B97  0F 85 9E 01 00 00               jne 0x140a15d3b
00A15B9D  F6 C3 04                        test bl, 4
00A15BA0  0F 85 83 00 00 00               jne 0x140a15c29
00A15BA6  49 8B D6                        mov rdx, r14
00A15BA9  49 8B CF                        mov rcx, r15
00A15BAC  E8 AB D8 02 00                  call 0x140a4345c
00A15BB1  8B F8                           mov edi, eax
00A15BB3  85 C0                           test eax, eax
00A15BB5  0F 88 1A F1 FF FF               js 0x140a14cd5
00A15BBB  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
00A15BBF  4C 8D 8C 24 B0 08 00 00         lea r9, [rsp + 0x8b0]
00A15BC7  4C 8B A4 24 08 01 00 00         mov r12, qword ptr [rsp + 0x108]
00A15BCF  4D 8B C4                        mov r8, r12
00A15BD2  33 D2                           xor edx, edx
00A15BD4  49 8B CE                        mov rcx, r14
00A15BD7  E8 D4 9A EB FF                  call 0x1408cf6b0
00A15BDC  8B F8                           mov edi, eax
00A15BDE  85 C0                           test eax, eax
00A15BE0  0F 88 EF F0 FF FF               js 0x140a14cd5
00A15BE6  89 84 24 C4 00 00 00            mov dword ptr [rsp + 0xc4], eax
00A15BED  4D 85 FF                        test r15, r15
00A15BF0  74 27                           je 0x140a15c19
00A15BF2  F6 C3 02                        test bl, 2
00A15BF5  75 22                           jne 0x140a15c19
00A15BF7  49 8B CC                        mov rcx, r12
00A15BFA  E8 B1 F0 87 FF                  call 0x140294cb0
00A15BFF  48 8B 08                        mov rcx, qword ptr [rax]
00A15C02  48 8B 51 20                     mov rdx, qword ptr [rcx + 0x20]
00A15C06  49 8B 86 B0 02 00 00            mov rax, qword ptr [r14 + 0x2b0]
00A15C0D  48 3B D0                        cmp rdx, rax
00A15C10  74 07                           je 0x140a15c19
00A15C12  48 2B C2                        sub rax, rdx
00A15C15  49 01 47 38                     add qword ptr [r15 + 0x38], rax
00A15C19  0F BA EB 07                     bts ebx, 7
00A15C1D  89 9C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ebx
00A15C24  E9 DF 00 00 00                  jmp 0x140a15d08
00A15C29  49 8B 84 24 B0 02 00 00         mov rax, qword ptr [r12 + 0x2b0]
00A15C31  49 89 86 B0 02 00 00            mov qword ptr [r14 + 0x2b0], rax
00A15C38  8B C3                           mov eax, ebx
00A15C3A  C1 E8 03                        shr eax, 3
00A15C3D  41 23 C5                        and eax, r13d
00A15C40  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00A15C44  4C 8D 8C 24 B0 08 00 00         lea r9, [rsp + 0x8b0]
00A15C4C  45 33 C0                        xor r8d, r8d
00A15C4F  49 8B D4                        mov rdx, r12
00A15C52  49 8B CE                        mov rcx, r14
00A15C55  E8 56 9A EB FF                  call 0x1408cf6b0
00A15C5A  8B F8                           mov edi, eax
00A15C5C  85 C0                           test eax, eax
00A15C5E  0F 88 71 F0 FF FF               js 0x140a14cd5
00A15C64  49 8B 84 24 50 03 00 00         mov rax, qword ptr [r12 + 0x350]
00A15C6C  44 0F B7 60 02                  movzx r12d, word ptr [rax + 2]
00A15C71  41 B8 53 65 50 61               mov r8d, 0x61506553
00A15C77  49 8D 54 24 10                  lea rdx, [r12 + 0x10]
00A15C7C  B9 40 00 00 00                  mov ecx, 0x40
00A15C81  E8 6A C4 16 00                  call 0x140b820f0
00A15C86  49 89 86 50 03 00 00            mov qword ptr [r14 + 0x350], rax
00A15C8D  48 85 C0                        test rax, rax
00A15C90  0F 84 23 F5 FF FF               je 0x140a151b9
00A15C96  4D 8D 44 24 10                  lea r8, [r12 + 0x10]
00A15C9B  4C 8B A4 24 98 00 00 00         mov r12, qword ptr [rsp + 0x98]
00A15CA3  49 8B 94 24 50 03 00 00         mov rdx, qword ptr [r12 + 0x350]
00A15CAB  48 8B C8                        mov rcx, rax
00A15CAE  E8 8D 0B CB FF                  call 0x1406c6840
00A15CB3  49 8B 8E 50 03 00 00            mov rcx, qword ptr [r14 + 0x350]
00A15CBA  48 8D 41 10                     lea rax, [rcx + 0x10]
00A15CBE  48 89 41 08                     mov qword ptr [rcx + 8], rax
00A15CC2  41 8B 84 24 B8 02 00 00         mov eax, dword ptr [r12 + 0x2b8]
00A15CCA  41 89 86 B8 02 00 00            mov dword ptr [r14 + 0x2b8], eax
00A15CD1  B9 00 00 00 01                  mov ecx, 0x1000000
00A15CD6  41 85 8C 24 F0 01 00 00         test dword ptr [r12 + 0x1f0], ecx
00A15CDE  74 07                           je 0x140a15ce7
00A15CE0  41 09 8E F0 01 00 00            or dword ptr [r14 + 0x1f0], ecx
00A15CE7  F7 84 24 B0 08 00 00 00 10 00 00  test dword ptr [rsp + 0x8b0], 0x1000
00A15CF2  74 14                           je 0x140a15d08
00A15CF4  49 89 B6 A8 02 00 00            mov qword ptr [r14 + 0x2a8], rsi
00A15CFB  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
00A15D03  E8 48 36 8E FF                  call 0x1402f9350
00A15D08  41 84 DD                        test r13b, bl
00A15D0B  75 2E                           jne 0x140a15d3b
00A15D0D  8B 8C 24 B0 08 00 00            mov ecx, dword ptr [rsp + 0x8b0]
00A15D14  83 E1 10                        and ecx, 0x10
00A15D17  C1 E1 08                        shl ecx, 8
00A15D1A  8B C3                           mov eax, ebx
00A15D1C  0F BA F0 0C                     btr eax, 0xc
00A15D20  8B D9                           mov ebx, ecx
00A15D22  0B D8                           or ebx, eax
00A15D24  89 9C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ebx
00A15D2B  F6 C3 02                        test bl, 2
00A15D2E  75 0B                           jne 0x140a15d3b
00A15D30  0F BA EB 08                     bts ebx, 8
00A15D34  89 9C 24 84 00 00 00            mov dword ptr [rsp + 0x84], ebx
00A15D3B  0F BA E3 0A                     bt ebx, 0xa
00A15D3F  73 0D                           jae 0x140a15d4e
00A15D41  48 8B 8C 24 98 01 00 00         mov rcx, qword ptr [rsp + 0x198]
00A15D49  E8 52 28 05 00                  call 0x140a685a0
00A15D4E  B8 4C 01 00 00                  mov eax, 0x14c
00A15D53  66 41 39 86 EC 06 00 00         cmp word ptr [r14 + 0x6ec], ax
00A15D5B  75 07                           jne 0x140a15d64
00A15D5D  45 09 AE 88 00 00 00            or dword ptr [r14 + 0x88], r13d
00A15D64  84 DB                           test bl, bl
00A15D66  79 27                           jns 0x140a15d8f
00A15D68  4D 85 FF                        test r15, r15
00A15D6B  74 22                           je 0x140a15d8f
00A15D6D  F6 C3 02                        test bl, 2
00A15D70  75 1D                           jne 0x140a15d8f
00A15D72  4D 8B C7                        mov r8, r15
00A15D75  48 8D 94 24 60 04 00 00         lea rdx, [rsp + 0x460]
00A15D7D  49 8B CE                        mov rcx, r14
00A15D80  E8 6B 18 04 00                  call 0x140a575f0
00A15D85  8B F8                           mov edi, eax
00A15D87  85 C0                           test eax, eax
00A15D89  0F 88 59 EF FF FF               js 0x140a14ce8
00A15D8F  0F BA E3 08                     bt ebx, 8
00A15D93  0F 83 12 01 00 00               jae 0x140a15eab
00A15D99  4C 8D 84 24 95 00 00 00         lea r8, [rsp + 0x95]
00A15DA1  33 D2                           xor edx, edx
00A15DA3  49 8B CE                        mov rcx, r14
00A15DA6  E8 85 58 FC FF                  call 0x1409db630
00A15DAB  33 C0                           xor eax, eax
00A15DAD  48 89 84 24 A8 01 00 00         mov qword ptr [rsp + 0x1a8], rax
00A15DB5  48 83 8C 24 B0 01 00 00 FF      or qword ptr [rsp + 0x1b0], 0xffffffffffffffff
00A15DBE  41 8A 86 FA 05 00 00            mov al, byte ptr [r14 + 0x5fa]
00A15DC5  24 07                           and al, 7
00A15DC7  8B D3                           mov edx, ebx
00A15DC9  C1 EA 0C                        shr edx, 0xc
00A15DCC  41 22 D5                        and dl, r13b
00A15DCF  40 3A F0                        cmp sil, al
00A15DD2  1A C9                           sbb cl, cl
00A15DD4  80 E1 02                        and cl, 2
00A15DD7  0A D1                           or dl, cl
00A15DD9  8A 8C 24 AB 01 00 00            mov cl, byte ptr [rsp + 0x1ab]
00A15DE0  80 E1 FC                        and cl, 0xfc
00A15DE3  0A D1                           or dl, cl
00A15DE5  80 E2 BB                        and dl, 0xbb
00A15DE8  8B CB                           mov ecx, ebx
00A15DEA  C1 E9 0D                        shr ecx, 0xd
00A15DED  41 22 CD                        and cl, r13b
00A15DF0  41 3A C5                        cmp al, r13b
00A15DF3  0F 95 C0                        setne al
00A15DF6  41 2A C5                        sub al, r13b
00A15DF9  24 10                           and al, 0x10
00A15DFB  0A C8                           or cl, al
00A15DFD  C0 E1 02                        shl cl, 2
00A15E00  0A D1                           or dl, cl
00A15E02  8B 84 24 E4 00 00 00            mov eax, dword ptr [rsp + 0xe4]
00A15E09  F7 D8                           neg eax
00A15E0B  1A C9                           sbb cl, cl
00A15E0D  80 E1 02                        and cl, 2
00A15E10  44 8A A4 24 95 00 00 00         mov r12b, byte ptr [rsp + 0x95]
00A15E18  45 22 E5                        and r12b, r13b
00A15E1B  44 0A E1                        or r12b, cl
00A15E1E  41 C0 E4 04                     shl r12b, 4
00A15E22  80 E2 CF                        and dl, 0xcf
00A15E25  44 0A E2                        or r12b, dl
00A15E28  44 88 A4 24 AB 01 00 00         mov byte ptr [rsp + 0x1ab], r12b
00A15E30  F6 C3 04                        test bl, 4
00A15E33  0F 85 B1 00 00 00               jne 0x140a15eea
00A15E39  4D 8D A6 E0 02 00 00            lea r12, [r14 + 0x2e0]
00A15E40  4C 8D 8C 24 10 02 00 00         lea r9, [rsp + 0x210]
00A15E48  4D 8B C4                        mov r8, r12
00A15E4B  48 8D 94 24 A8 01 00 00         lea rdx, [rsp + 0x1a8]
00A15E53  49 8B CE                        mov rcx, r14
00A15E56  E8 59 B1 F6 FF                  call 0x140980fb4
00A15E5B  8B F8                           mov edi, eax
00A15E5D  85 C0                           test eax, eax
00A15E5F  79 09                           jns 0x140a15e6a
00A15E61  49 89 34 24                     mov qword ptr [r12], rsi
00A15E65  E9 7E EE FF FF                  jmp 0x140a14ce8
00A15E6A  48 39 B4 24 10 02 00 00         cmp qword ptr [rsp + 0x210], rsi
00A15E72  74 37                           je 0x140a15eab
00A15E74  F0 41 81 A6 F0 01 00 00 FF FF CF FF  lock and dword ptr [r14 + 0x1f0], 0xffcfffff
00A15E80  48 8D 84 24 6C 01 00 00         lea rax, [rsp + 0x16c]
00A15E88  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A15E8D  4C 8D 8C 24 10 02 00 00         lea r9, [rsp + 0x210]
00A15E95  45 33 C0                        xor r8d, r8d
00A15E98  41 8B D5                        mov edx, r13d
00A15E9B  4C 8B B4 24 A0 00 00 00         mov r14, qword ptr [rsp + 0xa0]
00A15EA3  49 8B CE                        mov rcx, r14
00A15EA6  E8 59 AA 04 00                  call 0x140a60904
00A15EAB  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00A15EB3  84 DB                           test bl, bl
00A15EB5  0F 89 00 02 00 00               jns 0x140a160bb
00A15EBB  4D 85 FF                        test r15, r15
00A15EBE  0F 84 F7 01 00 00               je 0x140a160bb
00A15EC4  F6 C3 02                        test bl, 2
00A15EC7  0F 85 EE 01 00 00               jne 0x140a160bb
00A15ECD  4D 8B CF                        mov r9, r15
00A15ED0  4C 8D 84 24 60 04 00 00         lea r8, [rsp + 0x460]
00A15ED8  49 8B D6                        mov rdx, r14
00A15EDB  48 8B C8                        mov rcx, rax
00A15EDE  E8 E5 5E 0D 00                  call 0x140aebdc8
00A15EE3  8B F8                           mov edi, eax
00A15EE5  E9 6A 02 00 00                  jmp 0x140a16154
00A15EEA  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00A15EF2  4C 8B A8 E0 02 00 00            mov r13, qword ptr [rax + 0x2e0]
00A15EF9  4D 89 AE E0 02 00 00            mov qword ptr [r14 + 0x2e0], r13
00A15F00  F6 C3 10                        test bl, 0x10
00A15F03  0F 85 A7 01 00 00               jne 0x140a160b0
00A15F09  C6 84 24 A8 01 00 00 01         mov byte ptr [rsp + 0x1a8], 1
00A15F11  4C 8D 84 24 60 04 00 00         lea r8, [rsp + 0x460]
00A15F19  33 D2                           xor edx, edx
00A15F1B  49 8B CE                        mov rcx, r14
00A15F1E  E8 FD 08 80 FF                  call 0x140216820
00A15F23  BA D8 07 00 00                  mov edx, 0x7d8
00A15F28  41 B8 04 00 00 00               mov r8d, 4
00A15F2E  49 8B CD                        mov rcx, r13
00A15F31  E8 BA F6 FD FF                  call 0x1409f55f0
00A15F36  48 85 C0                        test rax, rax
00A15F39  74 71                           je 0x140a15fac
00A15F3B  0F 10 84 24 A8 01 00 00         movups xmm0, xmmword ptr [rsp + 0x1a8]
00A15F43  F3 41 0F 7F 45 00               movdqu xmmword ptr [r13], xmm0
00A15F49  B8 4C 01 00 00                  mov eax, 0x14c
00A15F4E  BA 01 00 00 00                  mov edx, 1
00A15F53  44 8D 42 03                     lea r8d, [rdx + 3]
00A15F57  EB 66                           jmp 0x140a15fbf
00A15F59  8B F8                           mov edi, eax
00A15F5B  33 F6                           xor esi, esi
00A15F5D  8D 56 01                        lea edx, [rsi + 1]
00A15F60  B8 4C 01 00 00                  mov eax, 0x14c
00A15F65  44 8D 46 04                     lea r8d, [rsi + 4]
00A15F69  8B CE                           mov ecx, esi
00A15F6B  48 89 8C 24 50 01 00 00         mov qword ptr [rsp + 0x150], rcx
00A15F73  44 8A A4 24 AB 01 00 00         mov r12b, byte ptr [rsp + 0x1ab]
00A15F7B  8B 9C 24 84 00 00 00            mov ebx, dword ptr [rsp + 0x84]
00A15F82  4C 8B B4 24 A0 00 00 00         mov r14, qword ptr [rsp + 0xa0]
00A15F8A  48 89 8C 24 10 01 00 00         mov qword ptr [rsp + 0x110], rcx
00A15F92  48 8B 8C 24 E8 01 00 00         mov rcx, qword ptr [rsp + 0x1e8]
00A15F9A  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
00A15FA2  4C 8B BC 24 F0 01 00 00         mov r15, qword ptr [rsp + 0x1f0]
00A15FAA  EB 13                           jmp 0x140a15fbf
00A15FAC  BF 41 01 00 C0                  mov edi, 0xc0000141
00A15FB1  B8 4C 01 00 00                  mov eax, 0x14c
00A15FB6  BA 01 00 00 00                  mov edx, 1
00A15FBB  44 8D 42 03                     lea r8d, [rdx + 3]
00A15FBF  85 FF                           test edi, edi
00A15FC1  0F 88 C7 00 00 00               js 0x140a1608e
00A15FC7  4D 8B AE 10 03 00 00            mov r13, qword ptr [r14 + 0x310]
00A15FCE  4D 85 ED                        test r13, r13
00A15FD1  0F 84 B7 00 00 00               je 0x140a1608e
00A15FD7  41 0F B7 8E EC 06 00 00         movzx ecx, word ptr [r14 + 0x6ec]
00A15FDF  66 3B C8                        cmp cx, ax
00A15FE2  74 0D                           je 0x140a15ff1
00A15FE4  B8 C4 01 00 00                  mov eax, 0x1c4
00A15FE9  66 3B C8                        cmp cx, ax
00A15FEC  40 8A C6                        mov al, sil
00A15FEF  75 02                           jne 0x140a15ff3
00A15FF1  8A C2                           mov al, dl
00A15FF3  84 C0                           test al, al
00A15FF5  0F 84 93 00 00 00               je 0x140a1608e
00A15FFB  4D 8B 6D 00                     mov r13, qword ptr [r13]
00A15FFF  BA 90 04 00 00                  mov edx, 0x490
00A16004  49 8B CD                        mov rcx, r13
00A16007  E8 E4 F5 FD FF                  call 0x1409f55f0
00A1600C  48 85 C0                        test rax, rax
00A1600F  74 78                           je 0x140a16089
00A16011  33 C0                           xor eax, eax
00A16013  89 84 24 58 01 00 00            mov dword ptr [rsp + 0x158], eax
00A1601A  83 8C 24 5C 01 00 00 FF         or dword ptr [rsp + 0x15c], 0xffffffff
00A16022  C6 84 24 58 01 00 00 01         mov byte ptr [rsp + 0x158], 1
00A1602A  44 88 A4 24 5B 01 00 00         mov byte ptr [rsp + 0x15b], r12b
00A16032  48 8B 84 24 58 01 00 00         mov rax, qword ptr [rsp + 0x158]
00A1603A  49 89 45 00                     mov qword ptr [r13], rax
00A1603E  41 BD 01 00 00 00               mov r13d, 1
00A16044  EB 4E                           jmp 0x140a16094
00A16046  8B F8                           mov edi, eax
00A16048  33 F6                           xor esi, esi
00A1604A  44 8D 6E 01                     lea r13d, [rsi + 1]
00A1604E  8B C6                           mov eax, esi
00A16050  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
00A16058  8B 9C 24 84 00 00 00            mov ebx, dword ptr [rsp + 0x84]
00A1605F  4C 8B B4 24 A0 00 00 00         mov r14, qword ptr [rsp + 0xa0]
00A16067  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
00A1606F  48 8B 84 24 E8 01 00 00         mov rax, qword ptr [rsp + 0x1e8]
00A16077  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
00A1607F  4C 8B BC 24 F0 01 00 00         mov r15, qword ptr [rsp + 0x1f0]
00A16087  EB 0B                           jmp 0x140a16094
00A16089  BF 41 01 00 C0                  mov edi, 0xc0000141
00A1608E  41 BD 01 00 00 00               mov r13d, 1
00A16094  33 D2                           xor edx, edx
00A16096  48 8D 8C 24 60 04 00 00         lea rcx, [rsp + 0x460]
00A1609E  E8 8D 1C 80 FF                  call 0x140217d30
00A160A3  85 FF                           test edi, edi
00A160A5  0F 88 3D EC FF FF               js 0x140a14ce8
00A160AB  E9 FB FD FF FF                  jmp 0x140a15eab
00A160B0  41 BD 01 00 00 00               mov r13d, 1
00A160B6  E9 F8 FD FF FF                  jmp 0x140a15eb3
00A160BB  0F BA E3 08                     bt ebx, 8
00A160BF  0F 83 8F 00 00 00               jae 0x140a16154
00A160C5  F6 C3 10                        test bl, 0x10
00A160C8  0F 85 86 00 00 00               jne 0x140a16154
00A160CE  8B FE                           mov edi, esi
00A160D0  4C 8D 84 24 60 04 00 00         lea r8, [rsp + 0x460]
00A160D8  33 D2                           xor edx, edx
00A160DA  49 8B CE                        mov rcx, r14
00A160DD  E8 3E 07 80 FF                  call 0x140216820
00A160E2  49 8B CE                        mov rcx, r14
00A160E5  E8 DA C2 A9 FF                  call 0x1404b23c4
00A160EA  49 8B D6                        mov rdx, r14
00A160ED  48 8B 8C 24 00 02 00 00         mov rcx, qword ptr [rsp + 0x200]
00A160F5  E8 96 A6 03 00                  call 0x140a50790
00A160FA  84 DB                           test bl, bl
00A160FC  79 47                           jns 0x140a16145
00A160FE  49 8B CE                        mov rcx, r14
00A16101  E8 92 AD F6 FF                  call 0x140980e98
00A16106  8B F8                           mov edi, eax
00A16108  85 C0                           test eax, eax
00A1610A  78 39                           js 0x140a16145
00A1610C  49 8B CE                        mov rcx, r14
00A1610F  E8 3C 97 05 00                  call 0x140a6f850
00A16114  8B F8                           mov edi, eax
00A16116  85 C0                           test eax, eax
00A16118  78 2B                           js 0x140a16145
00A1611A  33 D2                           xor edx, edx
00A1611C  33 C9                           xor ecx, ecx
00A1611E  E8 05 80 EB FF                  call 0x1408ce128
00A16123  8B F8                           mov edi, eax
00A16125  85 C0                           test eax, eax
00A16127  78 1C                           js 0x140a16145
00A16129  49 39 B6 10 03 00 00            cmp qword ptr [r14 + 0x310], rsi
00A16130  74 13                           je 0x140a16145
00A16132  49 8B CE                        mov rcx, r14
00A16135  E8 2A 83 EB FF                  call 0x1408ce464
00A1613A  33 D2                           xor edx, edx
00A1613C  8B C8                           mov ecx, eax
00A1613E  E8 E5 7F EB FF                  call 0x1408ce128
00A16143  8B F8                           mov edi, eax
00A16145  33 D2                           xor edx, edx
00A16147  48 8D 8C 24 60 04 00 00         lea rcx, [rsp + 0x460]
00A1614F  E8 DC 1B 80 FF                  call 0x140217d30
00A16154  85 FF                           test edi, edi
00A16156  0F 88 8C EB FF FF               js 0x140a14ce8
00A1615C  E8 07 78 BB FF                  call 0x1405cd968
00A16161  85 C0                           test eax, eax
00A16163  0F 84 B4 00 00 00               je 0x140a1621d
00A16169  48 8D 84 24 60 01 00 00         lea rax, [rsp + 0x160]
00A16171  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A16176  45 33 C9                        xor r9d, r9d
00A16179  4C 8B 84 24 F8 01 00 00         mov r8, qword ptr [rsp + 0x1f8]
00A16181  48 8B 94 24 90 01 00 00         mov rdx, qword ptr [rsp + 0x190]
00A16189  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00A16191  E8 FE 3E BF FF                  call 0x14060a094
00A16196  8B F8                           mov edi, eax
00A16198  85 C0                           test eax, eax
00A1619A  0F 88 48 EB FF FF               js 0x140a14ce8
00A161A0  48 8B 84 24 60 01 00 00         mov rax, qword ptr [rsp + 0x160]
00A161A8  48 85 C0                        test rax, rax
00A161AB  74 70                           je 0x140a1621d
00A161AD  8B 00                           mov eax, dword ptr [rax]
00A161AF  41 84 C5                        test r13b, al
00A161B2  74 69                           je 0x140a1621d
00A161B4  4D 85 FF                        test r15, r15
00A161B7  74 0F                           je 0x140a161c8
00A161B9  49 8B 87 B0 00 00 00            mov rax, qword ptr [r15 + 0xb0]
00A161C0  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
00A161C8  BA 44 66 6C 74                  mov edx, 0x746c6644
00A161CD  49 8B CE                        mov rcx, r14
00A161D0  E8 AB 9D 7F FF                  call 0x14020ff80
00A161D5  4C 8B E0                        mov r12, rax
00A161D8  4C 8B C8                        mov r9, rax
00A161DB  4C 8B 84 24 60 01 00 00         mov r8, qword ptr [rsp + 0x160]
00A161E3  48 8B 94 24 50 01 00 00         mov rdx, qword ptr [rsp + 0x150]
00A161EB  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00A161F3  E8 4C 34 BF FF                  call 0x140609644
00A161F8  8B F8                           mov edi, eax
00A161FA  49 8D 8E 48 02 00 00            lea rcx, [r14 + 0x248]
00A16201  41 B8 44 66 6C 74               mov r8d, 0x746c6644
00A16207  49 8B D4                        mov rdx, r12
00A1620A  85 C0                           test eax, eax
00A1620C  79 0A                           jns 0x140a16218
00A1620E  E8 DD 73 9D FF                  call 0x1403ed5f0
00A16213  E9 D0 EA FF FF                  jmp 0x140a14ce8
00A16218  E8 D3 73 9D FF                  call 0x1403ed5f0
00A1621D  4C 8B A4 24 00 02 00 00         mov r12, qword ptr [rsp + 0x200]
00A16225  49 8B D4                        mov rdx, r12
00A16228  49 8B CE                        mov rcx, r14
00A1622B  E8 34 9F A4 FF                  call 0x140460164
00A16230  48 8B 0D 71 0A 5B 00            mov rcx, qword ptr [rip + 0x5b0a71]
00A16237  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00A1623C  45 33 C9                        xor r9d, r9d
00A1623F  45 33 C0                        xor r8d, r8d
00A16242  49 8B D6                        mov rdx, r14
00A16245  E8 66 4A E5 FF                  call 0x14086acb0
00A1624A  48 8B F8                        mov rdi, rax
00A1624D  48 89 84 24 10 01 00 00         mov qword ptr [rsp + 0x110], rax
00A16255  48 85 C0                        test rax, rax
00A16258  75 15                           jne 0x140a1626f
00A1625A  49 8B D4                        mov rdx, r12
00A1625D  49 8B CE                        mov rcx, r14
00A16260  E8 5B 9F A4 FF                  call 0x1404601c0
00A16265  BF 9A 00 00 C0                  mov edi, 0xc000009a
00A1626A  E9 79 EA FF FF                  jmp 0x140a14ce8
00A1626F  0F BA E3 10                     bt ebx, 0x10
00A16273  0F 83 81 00 00 00               jae 0x140a162fa
00A16279  4C 8D 8C 24 08 02 00 00         lea r9, [rsp + 0x208]
00A16281  4D 8B 86 A8 02 00 00            mov r8, qword ptr [r14 + 0x2a8]
00A16288  33 D2                           xor edx, edx
00A1628A  33 C9                           xor ecx, ecx
00A1628C  E8 5F BB CE FF                  call 0x140701df0
00A16291  8B F8                           mov edi, eax
00A16293  49 8B CE                        mov rcx, r14
00A16296  85 C0                           test eax, eax
00A16298  79 0D                           jns 0x140a162a7
00A1629A  49 8B D4                        mov rdx, r12
00A1629D  E8 1E 9F A4 FF                  call 0x1404601c0
00A162A2  E9 41 EA FF FF                  jmp 0x140a14ce8
00A162A7  41 8B 87 78 01 00 00            mov eax, dword ptr [r15 + 0x178]
00A162AE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A162B3  49 8B 87 68 01 00 00            mov rax, qword ptr [r15 + 0x168]
00A162BA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A162BF  48 8B 84 24 08 02 00 00         mov rax, qword ptr [rsp + 0x208]
00A162C7  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A162CC  4D 8B 8F C0 00 00 00            mov r9, qword ptr [r15 + 0xc0]
00A162D3  4C 8B 84 24 10 01 00 00         mov r8, qword ptr [rsp + 0x110]
00A162DB  49 8B 96 E0 02 00 00            mov rdx, qword ptr [r14 + 0x2e0]
00A162E2  E8 A5 35 BA FF                  call 0x1405b988c
00A162E7  8B F8                           mov edi, eax
00A162E9  85 C0                           test eax, eax
00A162EB  79 05                           jns 0x140a162f2
00A162ED  49 8B CE                        mov rcx, r14
00A162F0  EB A8                           jmp 0x140a1629a
00A162F2  48 8B BC 24 10 01 00 00         mov rdi, qword ptr [rsp + 0x110]
00A162FA  E8 39 E1 A6 FF                  call 0x140484438
00A162FF  48 85 C0                        test rax, rax
00A16302  74 0E                           je 0x140a16312
00A16304  49 8D 8E F8 01 00 00            lea rcx, [r14 + 0x1f8]
00A1630B  E8 30 77 96 FF                  call 0x14037da40
00A16310  EB 19                           jmp 0x140a1632b
00A16312  48 A1 14 00 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000014]
00A1631C  4C 8B B4 24 A0 00 00 00         mov r14, qword ptr [rsp + 0xa0]
00A16324  49 89 86 F8 01 00 00            mov qword ptr [r14 + 0x1f8], rax
00A1632B  49 89 BE D0 01 00 00            mov qword ptr [r14 + 0x1d0], rdi
00A16332  48 A1 08 00 00 00 80 F7 FF FF   movabs rax, qword ptr [0xfffff78000000008]
00A1633C  49 89 86 80 06 00 00            mov qword ptr [r14 + 0x680], rax
00A16343  41 8A CD                        mov cl, r13b
00A16346  E8 35 6E A1 FF                  call 0x14042d180
00A1634B  48 8B 8C 24 A0 00 00 00         mov rcx, qword ptr [rsp + 0xa0]
00A16353  48 89 81 88 06 00 00            mov qword ptr [rcx + 0x688], rax
00A1635A  49 8B 86 80 06 00 00            mov rax, qword ptr [r14 + 0x680]
00A16361  48 89 81 98 06 00 00            mov qword ptr [rcx + 0x698], rax
00A16368  48 8B 84 24 38 02 00 00         mov rax, qword ptr [rsp + 0x238]
00A16370  48 89 08                        mov qword ptr [rax], rcx
00A16373  8B BC 24 C4 00 00 00            mov edi, dword ptr [rsp + 0xc4]
00A1637A  E9 94 E9 FF FF                  jmp 0x140a14d13
00A1637F  B8 30 00 00 C0                  mov eax, 0xc0000030
00A16384  48 8B 8C 24 20 08 00 00         mov rcx, qword ptr [rsp + 0x820]
00A1638C  48 33 CC                        xor rcx, rsp
00A1638F  E8 AC 62 C9 FF                  call 0x1406ac640
00A16394  48 81 C4 30 08 00 00            add rsp, 0x830
00A1639B  41 5F                           pop r15
00A1639D  41 5E                           pop r14
00A1639F  41 5D                           pop r13
00A163A1  41 5C                           pop r12
00A163A3  5F                              pop rdi
00A163A4  5E                              pop rsi
00A163A5  5B                              pop rbx
00A163A6  C3                              ret
00A163A7  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspAllocateProcess(__int64 a1, int a2, __int64 a3, unsigned __int8 a4, unsigned __int8 a5, unsigned __int8 a6, __int64 a7, __int64 a8, unsigned __int8 a9, unsigned __int8 a10, __int64 a11, unsigned int a12, __int64 a13, __int64 a14, __int64 a15)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m3D0;
    unsigned __int16 v_stack_m3D6;
    unsigned __int64 v_stack_m3D8;
    unsigned __int64 v_stack_m3E8;
    unsigned __int64 v_stack_m3F8;
    unsigned __int64 v_stack_m408;
    unsigned __int64 v_stack_m410;
    unsigned __int64 v_stack_m418;
    unsigned __int64 v_stack_m420;
    unsigned int v_stack_m42C;
    unsigned __int64 v_stack_m430;
    unsigned __int64 v_stack_m438;
    unsigned __int64 v_stack_m440;
    unsigned __int64 v_stack_m450;
    unsigned __int64 v_stack_m458;
    unsigned __int64 v_stack_m460;
    unsigned __int64 v_stack_m468;
    unsigned int v_stack_m478;
    unsigned __int64 v_stack_m48;
    unsigned __int8 v_stack_m485;
    unsigned __int16 v_stack_m48A;
    unsigned __int16 v_stack_m492;
    unsigned __int16 v_stack_m494;
    unsigned __int64 v_stack_m4B8;
    unsigned __int64 v_stack_m4C8;
    unsigned __int64 v_stack_m4D8;
    unsigned __int64 v_stack_m4E8;
    unsigned __int64 v_stack_m4F8;
    unsigned __int64 v_stack_m508;
    unsigned __int64 v_stack_m518;
    unsigned __int64 v_stack_m528;
    unsigned __int64 v_stack_m538;
    unsigned __int64 v_stack_m548;
    unsigned __int64 v_stack_m558;
    unsigned __int64 v_stack_m568;
    unsigned __int64 v_stack_m578;
    unsigned __int64 v_stack_m588;
    unsigned __int64 v_stack_m598;
    unsigned __int64 v_stack_m5A8;
    unsigned __int64 v_stack_m5B8;
    unsigned int v_stack_m5C0;
    unsigned __int64 v_stack_m5C8;
    unsigned int v_stack_m5D0;
    unsigned __int64 v_stack_m5D8;
    unsigned __int64 v_stack_m5E0;
    unsigned __int64 v_stack_m5E8;
    unsigned int v_stack_m5F0;
    unsigned __int64 v_stack_m5F8;
    unsigned int v_stack_m600;
    unsigned __int64 v_stack_m608;
    unsigned __int64 v_stack_m610;
    unsigned __int64 v_stack_m618;
    unsigned __int16 v_stack_m620;
    unsigned __int64 v_stack_m628;
    unsigned __int64 v_stack_m630;
    unsigned __int64 v_stack_m638;
    unsigned __int64 v_stack_m640;
    unsigned __int64 v_stack_m648;
    unsigned __int64 v_stack_m658;
    unsigned __int64 v_stack_m660;
    unsigned __int64 v_stack_m668;
    unsigned __int64 v_stack_m670;
    unsigned __int64 v_stack_m678;
    unsigned __int64 v_stack_m680;
    unsigned __int64 v_stack_m698;
    unsigned __int64 v_stack_m6A0;
    unsigned __int64 v_stack_m6A8;
    unsigned __int64 v_stack_m6B0;
    unsigned __int64 v_stack_m6B8;
    unsigned __int8 v_stack_m6BD;
    unsigned __int64 v_stack_m6C0;
    unsigned __int64 v_stack_m6C8;
    unsigned __int64 v_stack_m6D0;
    unsigned __int64 v_stack_m6D8;
    unsigned __int64 v_stack_m6E0;
    unsigned __int64 v_stack_m6E8;
    unsigned __int64 v_stack_m6F0;
    unsigned int v_stack_m6F8;
    unsigned int v_stack_m6FC;
    unsigned int v_stack_m700;
    unsigned __int64 v_stack_m708;
    unsigned int v_stack_m70C;
    unsigned __int8 v_stack_m70D;
    unsigned int v_stack_m710;
    unsigned __int64 v_stack_m718;
    unsigned __int64 v_stack_m720;
    unsigned __int64 v_stack_m728;
    unsigned int v_stack_m72C;
    unsigned int v_stack_m730;
    unsigned int v_stack_m734;
    unsigned int v_stack_m738;
    unsigned __int64 v_stack_m740;
    unsigned int v_stack_m744;
    unsigned int v_stack_m748;
    unsigned int v_stack_m74C;
    unsigned int v_stack_m750;
    unsigned __int64 v_stack_m758;
    unsigned __int64 v_stack_m760;
    unsigned __int64 v_stack_m768;
    unsigned int v_stack_m770;
    unsigned int v_stack_m774;
    unsigned __int16 v_stack_m778;
    unsigned __int64 v_stack_m780;
    unsigned int v_stack_m784;
    unsigned int v_stack_m788;
    unsigned int v_stack_m78C;
    unsigned int v_stack_m790;
    unsigned int v_stack_m794;
    unsigned __int8 v_stack_m795;
    unsigned __int8 v_stack_m796;
    unsigned int v_stack_m798;
    unsigned int v_stack_m79C;
    unsigned int v_stack_m7A0;
    unsigned int v_stack_m7A4;
    unsigned __int16 v_stack_m7A8;
    unsigned __int64 v_stack_m7B0;
    unsigned int v_stack_m7B4;
    unsigned int v_stack_m7B8;
    unsigned int v_stack_m7BC;
    unsigned __int16 v_stack_m7C0;
    unsigned __int64 v_stack_m7C8;
    unsigned __int64 v_stack_m7D0;
    unsigned __int8 v_stack_m7D3;
    unsigned __int8 v_stack_m7D4;
    unsigned int v_stack_m7D8;
    unsigned __int16 v_stack_m7DC;
    unsigned __int8 v_stack_m7E0;
    unsigned int v_stack_m7E4;
    unsigned __int8 v_stack_m7E8;
    unsigned __int64 v_stack_m7F8;
    unsigned __int64 v_stack_m800;
    unsigned __int64 v_stack_m808;
    unsigned int v_stack_m810;
    unsigned __int64 v_stack_m818;
    unsigned __int64 v_stack_m820;
    unsigned __int64 v_stack_m828;
    unsigned int v_stack_m830;
    unsigned int v_stack_m838;
    unsigned int v_stack_m840;
    unsigned int v_stack_m848;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_mA8;
    unsigned int v_stack_mBC;
    unsigned int v_stack_p48;

    v_rsp = (v_rsp) - (0x830ULL);
    result = (*(unsigned __int64 *)(v_rip + 4156392)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m740 = a3;
    v_stack_m7E8 = (unsigned __int8)(a2);
    v_stack_m7D0 = a1;
    v_stack_m680 = a1;
    v_stack_m760 = a7;
    v_stack_m768 = a8;
    v_stack_m678 = a11;
    v_stack_m720 = a13;
    v_stack_m648 = a14;
    v_stack_m630 = a15;
    v_rsi = 0;
    v_stack_m6FC = 0;
    v_stack_m408 = v_xmm0;
    v_stack_m3F8 = v_xmm0;
    v_stack_m3E8 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 1080) = 0;
    result = 0;
    v_stack_mBC = 0;
    v_stack_m618 = v_xmm0;
    v_stack_m608 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 1528) = 0;
    v_stack_m5F0 = 0;
    v_stack_m72C = 0;
    v_stack_m658 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 1776) = 0;
    a2 = 0;
    result = memset(v_rsp - 976, a2, 256, a4);
    v_stack_m7E4 = 0;
    v_stack_m788 = 0;
    v_stack_m798 = 0;
    result = 0;
    v_stack_m468 = v_xmm0;
    v_stack_m458 = 0;
    v_stack_m450 = v_xmm1;
    v_stack_m440 = 0;
    v_stack_m7D3 = 0;
    v_stack_m5E8 = v_xmm0;
    v_stack_m5D8 = v_xmm0;
    v_stack_m5C8 = 0;
    v_stack_m5C0 = 0;
    v_stack_m6E8 = 0;
    v_stack_m7C8 = 0;
    v_stack_m7D4 = 0;
    v_stack_m7A8 = 0;
    v_stack_m7BC = 0;
    a2 = 0;
    result = memset(v_stack_m4B8, a2, v_rsi + 72, a4);
    v_stack_m784 = 0;
    v_stack_m660 = 0;
    v_stack_m668 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m780 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184);
    v_stack_m708 = 0;
    v_stack_m7B0 = 0;
    v_stack_m6D8 = 0;
    v_stack_m670 = 0;
    v_stack_m718 = 0;
    v_stack_m6C8 = 0;
    v_stack_m7A4 = 0;
    v_stack_m7B8 = 0;
    v_stack_m7B4 = 0;
    v_stack_m78C = 0;
    v_stack_m790 = 0;
    v_stack_m79C = 0x8664ULL;
    v_stack_m750 = 0;
    v_stack_m744 = 0;
    v_stack_m748 = 0;
    v_stack_m794 = 0;
    v_stack_m6A0 = 0;
    v_stack_m74C = 0;
    v_stack_m6A8 = 0;
    v_stack_m7C0 = 0;
    v_stack_m758 = 0;
    v_stack_m6B0 = 0;
    a2 = 0;
    result = memset(v_stack_m2C8, a2, 536, a4);
    v_stack_m7D8 = (unsigned int)((unsigned int)(a9));
    if (condition_is_above_or_equal) goto loc_00A13E33;
    v_stack_m7E4 = (unsigned int)(v_rsi + 2);
    if (condition_is_above_or_equal) goto loc_00A13E55;
    v_stack_m7E4 = (unsigned int)(v_rsi + 6);
    if (condition_is_above_or_equal) goto loc_00A13E5B;
    goto loc_00A13E4C;
loc_00A13E33:
    if (v_rsi + 1 != 0) goto loc_00A13E55;
    result = -(a1);
    v_rbx = (unsigned int)((v_rsi + 14) & (3));
    v_rbx = (unsigned int)((v_rbx) + (1));
loc_00A13E4C:
    v_stack_m7E4 = (unsigned int)(v_rbx);
    goto loc_00A13E5B;
loc_00A13E55:
loc_00A13E5B:
    if ((((unsigned __int8)(v_rbx)) & (4)) == 0) goto loc_00A13E89;
    if (a12 == 0) goto loc_00A13E72;
    if ((((unsigned __int8)(v_rbx)) & (2)) == 0) goto loc_00A1637F;
loc_00A13E72:
    if (((*(unsigned int *)(a1 + 1532)) & (0x1000ULL)) == 0) goto loc_00A13E93;
    goto loc_00A16384;
loc_00A13E89:
    if (condition_is_below) goto loc_00A1637F;
loc_00A13E93:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a9)))) & (256));
    result = (unsigned int)(-(result));
    a1 = ((unsigned int)(a9)) & (a1);
    v_stack_m728 = a1;
    if (a11 == 0) goto loc_00A13EE6;
    if (condition_is_above_or_equal) goto loc_00A13EE6;
    if (a1 != 0) goto loc_00A1637F;
    v_stack_m7B0 = *(unsigned __int64 *)(v_rip + 6010864 + *(unsigned __int16 *)(a11 + 170) * 8);
    v_stack_m728 = a1;
    goto loc_00A13F13;
loc_00A13EE6:
    if (a1 == 0) goto loc_00A13F13;
    v_stack_m728 = a1;
    if (((*(unsigned int *)(a1 + 496)) & (0x200000ULL)) != 0) {
        v_stack_m728 = a1;
        v_stack_m7B4 = 0x200000ULL;
    }
    if (a11 == 0) goto loc_00A13F33;
    if (!(condition_is_above_or_equal)) {
        v_stack_m7E4 = (unsigned int)(v_rbx);
    }
    result = 0;
    v_stack_m430 = v_xmm0;
    v_stack_m420 = v_xmm0;
    v_stack_m410 = 0;
    v_stack_m6D0 = 0;
    v_stack_m738 = 0;
    v_stack_m698 = 0;
    if ((*(unsigned int *)(v_rip + 5975740)) == 0) {
        a1 = (unsigned int)(0x840ULL) + 40;
        v_stack_m7E4 = (unsigned int)(v_rbx);
        v_stack_m698 = (unsigned int)(0x840ULL);
    }
    result = (unsigned int)((a1 + 7) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    v_stack_m6F8 = (unsigned int)(result);
    result = PoEnergyEstimationEnabled(a1, (unsigned int)(0x840ULL), 536, a4);
    v_r14 = result + 16;
    if ((unsigned __int8)(result) != 0) {
        result = result + 16 + 7;
        result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
        v_stack_m738 = (unsigned int)(result);
        v_r14 = result + 488;
        v_stack_m7E4 = (unsigned int)(v_rbx);
    }
    result = KeQueryMaximumGroupCount(a1, (unsigned int)(0x840ULL), 536, a4);
    v_stack_m778 = (unsigned __int16)(result);
    v_r13 = 0;
    if (((unsigned __int16)(result)) >= = 1) {
        v_r14 = (unsigned int)((v_r14) + (7));
        v_r14 = (unsigned int)((v_r14) & (0xFFFFFFF8ULL));
        v_r13 = (unsigned int)(v_r14);
        a1 = (unsigned __int16)(result);
        a1 = (unsigned int)((a1) << (4));
        v_r14 = (unsigned int)((v_r14) + ((unsigned int)(a1)));
    }
    v_stack_m770 = 0;
    if ((((unsigned int)(v_rbx)) & (0x10002ULL)) == 0) {
        result = 4;
        a1 = 0;
        if (v_stack_m7D0 != 0) { a1 = (unsigned int)(result); }
        v_stack_m770 = (unsigned int)(a1);
    }
    v_r12 = (unsigned int)((v_r14 + 7) & (0xFFFFFFF8ULL));
    result = KeSizeOfKProcessExtension(a1, (unsigned int)(0x840ULL), 536, a4);
    v_stack_m700 = (unsigned int)(v_r12);
    v_r12 = (unsigned int)((v_r12) + ((unsigned int)(result)));
    v_stack_m820 = 0;
    v_stack_m828 = v_stack_m7C8;
    v_stack_m830 = (unsigned int)(v_r12);
    v_stack_m838 = 0;
    v_stack_m840 = (unsigned int)(v_r12);
    result = ObCreateObjectEx((unsigned __int8)(v_stack_m7E8), *(unsigned __int64 *)(v_rip + 5974619), v_stack_m740, v_stack_m7E8);
    if (sign_flag) goto loc_00A16384;
    result = ObRetagReferences(v_stack_m7C8, *(unsigned __int64 *)(v_rip + 5974619), (unsigned int)(0x72437350ULL), v_stack_m7E8);
    a2 = 0;
    result = memset(v_stack_m7C8, a2, (unsigned int)((unsigned int)(v_r12)), v_stack_m7E8);
    *(unsigned __int64 *)(v_stack_m7C8 + 1408) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m7C8 + 1424) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m7C8 + 1408) = 0;
    *(unsigned __int64 *)(v_stack_m7C8 + 1416 + 8) = v_stack_m7C8 + 1416;
    *(unsigned __int64 *)(v_stack_m7C8 + 1416) = v_stack_m7C8 + 1416;
    *(unsigned __int64 *)(v_stack_m7C8 + 488) = 0;
    *(unsigned __int64 *)(v_stack_m7C8 + 456) = 0;
    *(unsigned __int64 *)(v_stack_m7C8 + 880 + 8) = v_stack_m7C8 + 880;
    *(unsigned __int64 *)(v_stack_m7C8 + 880) = v_stack_m7C8 + 880;
    *(unsigned __int64 *)(v_stack_m7C8 + 1568 + 8) = v_stack_m7C8 + 1568;
    *(unsigned __int64 *)(v_stack_m7C8 + 1568) = v_stack_m7C8 + 1568;
    *(unsigned __int64 *)(v_stack_m7C8 + 1808 + 8) = v_stack_m7C8 + 1808;
    *(unsigned __int64 *)(v_stack_m7C8 + 1808) = v_stack_m7C8 + 1808;
    *(unsigned __int8 *)(v_stack_m7C8 + 1530) = a4;
    *(unsigned __int8 *)(v_stack_m7C8 + 1528) = a5;
    *(unsigned __int8 *)(v_stack_m7C8 + 1529) = a6;
    *(unsigned __int64 *)(v_stack_m7C8 + 2088) = 1;
    *(unsigned __int64 *)(v_stack_m7C8 + 1624) = 0;
    *(unsigned __int64 *)(v_stack_m7C8 + 1928) = 0;
    *(unsigned __int64 *)(v_stack_m7C8 + 1920) = 0;
    *(unsigned __int64 *)(v_stack_m7C8 + 1944) = 0;
    *(unsigned __int64 *)(v_stack_m7C8 + 1936) = 0;
    *(unsigned __int64 *)(v_stack_m7C8 + 1960) = 0;
    *(unsigned __int64 *)(v_stack_m7C8 + 2072) = 0;
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) {
    }
    if (condition_is_above_or_equal) goto loc_00A14190;
    v_stack_m740 = 32;
    goto loc_00A1419B;
loc_00A14190:
    v_stack_m740 = 32;
loc_00A1419B:
    v_r14 = v_stack_m7C8;
    if (!(condition_is_above_or_equal)) {
        a3 = a9;
        v_stack_m7D8 = (unsigned int)(a3);
        v_r14 = v_stack_m7C8;
    }
    result = 32;
    if ((unsigned int)(v_r13) != 0) {
        a1 = (unsigned int)(v_r13);
        a1 = (a1) + (v_r14);
        *(unsigned __int64 *)(v_r14 + 1736) = a1;
        result = v_stack_m778;
        a1 = a1 + result * 8;
        *(unsigned __int64 *)(v_r14 + 1744) = a1;
    }
    if (((1) & ((unsigned __int8)((unsigned int)(a10)))) != 0) {
    }
    if (((4) & ((unsigned __int8)((unsigned int)(a10)))) != 0) {
    }
    if ((((unsigned __int8)((unsigned int)(a10))) & (8)) != 0) {
    }
    if ((((unsigned __int8)((unsigned int)(a10))) & (16)) != 0) {
    }
    result = (*(unsigned __int64 *)(v_stack_m780 + 464)) | (2);
    if (condition_is_below) { result = *(unsigned __int64 *)(v_stack_m780 + 464); }
    *(unsigned __int64 *)(v_r14 + 728) = result;
    if (!(condition_is_above_or_equal)) {
        result = v_stack_m698;
        result = (result) + (v_r14);
        *(unsigned __int64 *)(v_r14 + 1592) = result;
    }
    result = ((unsigned int)(v_stack_m6F8)) + (v_r14);
    *(unsigned __int64 *)(v_r14 + 2032) = result;
    if (!(condition_is_above_or_equal)) {
        a1 = v_stack_m738;
        a1 = (a1) + (v_r14);
        *(unsigned __int64 *)(v_r14 + 1640) = a1;
        result = PoEnergyContextInitialize(a1, *(unsigned __int64 *)(v_stack_m780 + 464), a3, v_stack_m7E8);
    }
    if (a11 == 0) goto loc_00A142C4;
    if (condition_is_above_or_equal) goto loc_00A142C4;
    goto loc_00A142E0;
loc_00A142C4:
    if (v_stack_m7D0 == 0) goto loc_00A142DB;
    goto loc_00A142E0;
loc_00A142DB:
loc_00A142E0:
    *(unsigned int *)(v_r14 + 904) = 5;
    *(unsigned int *)(v_r14 + 1364) = 259;
    if (v_stack_m7D0 == 0) goto loc_00A14326;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m7D0 + 500))) >> (27));
    a2 = (unsigned int)((a2) & (7));
    a3 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m7D0 + 496))) >> (12));
    a3 = (unsigned int)((a3) & (7));
    *(unsigned __int64 *)(v_r14 + 720) = *(unsigned __int64 *)(v_stack_m7D0 + 464);
    goto loc_00A14333;
loc_00A14326:
    result = KeQueryHeteroCpuPolicyThread(a1, 2, a3, v_stack_m7E8);
loc_00A14333:
    a2 = (unsigned int)((2) << (27));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 500))) & (0xC7FFFFFFULL));
    a2 = (unsigned int)((a2) | ((unsigned int)(a1)));
    *(unsigned int *)(v_r14 + 500) = a2;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_r14 + 496))) & (0xFFFF8FFFULL));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(result))) << (12));
    a1 = (unsigned int)((a1) | ((unsigned int)(a3)));
    *(unsigned int *)(v_r14 + 496) = (unsigned int)(a1);
    if (v_stack_m720 == 0) goto loc_00A1438A;
    result = PsReferencePartitionSafe(v_stack_m720, a2, a3, v_stack_m7E8);
    if ((unsigned __int8)(result) != 0) goto loc_00A143C9;
    goto loc_00A14CE8;
loc_00A1438A:
    v_stack_m720 = *(unsigned __int64 *)(v_rip + 5974799);
    result = (1) + (1);
    if (result <= 1) {
        a1 = 14;
    }
    v_stack_m7D8 = (unsigned int)((unsigned int)(a9));
    goto loc_00A143D1;
loc_00A143C9:
loc_00A143D1:
    *(unsigned __int64 *)(v_stack_m7C8 + 1880) = v_stack_m720;
    result = (unsigned int)(a9);
    if (v_stack_m760 != 0) {
        result = ObfReferenceObject(v_stack_m760, v_stack_m720, a3, v_stack_m7E8);
        a1 = v_stack_m760;
    }
    if ((((unsigned __int8)((unsigned int)(0xC00004A0ULL))) & ((unsigned __int8)(v_rbx))) == 0) goto loc_00A144A3;
    v_stack_m79C = (unsigned int)(*(unsigned __int16 *)(v_stack_m7D0 + 1772));
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) goto loc_00A144A3;
    result = ExAcquireRundownProtection(v_stack_m7D0 + 488, v_stack_m720, a3, v_stack_m7E8);
    if ((unsigned __int8)(result) == 0) goto loc_00A1444D;
    v_stack_m760 = *(unsigned __int64 *)(v_stack_m7D0 + 680);
    result = *(unsigned __int64 *)(v_stack_m7D0 + 680);
    if (*(unsigned __int64 *)(v_stack_m7D0 + 680) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m7D0 + 680);
        result = ObfReferenceObject(a1, v_stack_m720, a3, v_stack_m7E8);
    }
    result = ExReleaseRundownProtection(v_stack_m7D0 + 488, v_stack_m720, a3, v_stack_m7E8);
loc_00A1444D:
    if (v_stack_m760 != 0) goto loc_00A14464;
    goto loc_00A14CE8;
loc_00A14464:
    result = *(unsigned __int64 *)(v_stack_m7D0 + 784);
    if (*(unsigned __int64 *)(v_stack_m7D0 + 784) != 0) {
        v_rbx = (unsigned int)((v_rbx) | (64));
        v_stack_m7E4 = (unsigned int)(v_rbx);
        result = *(unsigned int *)(*(unsigned __int64 *)(v_stack_m7D0 + 784) + 8);
        v_stack_m750 = (unsigned int)(result);
    }
    result = 0;
    if (((*(unsigned int *)(v_stack_m7D0 + 500)) & ((unsigned int)((unsigned int)(0x20000ULL)))) != 0) { result = (unsigned int)((unsigned int)(0x20000ULL)); }
    v_stack_m7B8 = (unsigned int)(result);
loc_00A144A3:
    *(unsigned __int64 *)(v_stack_m7C8 + 680) = v_stack_m760;
    if (a11 == 0) goto loc_00A14A39;
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) goto loc_00A14A39;
    *(unsigned __int64 *)(v_stack_m7C8 + 1520) = *(unsigned __int64 *)(a11 + 424);
    result = MmGetSectionInformation(v_stack_m760, 4, a11 + 56, v_stack_m7E8);
    if (sign_flag) goto loc_00A14CE8;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a11 + 120))))) & (250));
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)(v_rbx)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a11 + 120))) & (1));
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(result)));
    v_rbx = (unsigned int)((v_rbx) << (5));
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(a11 + 107)))) & (2));
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(result)));
    v_rbx = (unsigned int)((v_rbx) << (2));
    a1 = (unsigned int)((*(unsigned __int8 *)(a11 + 107)) & (4));
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)(a1)));
    v_rbx = (unsigned int)((v_rbx) << (11));
    v_rbx = (unsigned int)((v_rbx) | ((unsigned int)((unsigned int)((unsigned int)(v_rbx)))));
    v_stack_m7E4 = (unsigned int)(v_rbx);
    v_stack_m78C = (unsigned int)(*(unsigned __int16 *)(a11 + 94));
    v_stack_m790 = (unsigned int)(*(unsigned __int16 *)(a11 + 92));
    if (((*(unsigned __int16 *)(a11 + 18)) & ((unsigned __int16)(*(unsigned __int16 *)(a11 + 100)))) == 0) goto loc_00A14557;
loc_00A14547:
    a3 = 0;
    result = PspUpdateCreateInfo(3, a11, a3, v_stack_m7E8);
    goto loc_00A14CE8;
loc_00A14557:
    if (((4) & ((unsigned __int8)(v_rbx))) != 0) goto loc_00A14AEC;
    result = ObfReferenceObjectWithTag(*(unsigned __int64 *)(a11 + 184), (unsigned int)(0x72437350ULL), a3, v_stack_m7E8);
    *(unsigned __int64 *)(v_stack_m7C8 + 816) = *(unsigned __int64 *)(a11 + 184);
    v_stack_m7C0 = (unsigned __int16)(*(unsigned __int16 *)(a11 + 102));
    result = RtlpOpenImageFileOptionsKeyEx(a11 + 240, (unsigned int)(0x72437350ULL), a3, a11 + 200);
    if (!sign_flag) goto loc_00A145BB;
    if (((unsigned int)(result)) == 0xC0000034ULL) {
    }
    *(unsigned __int64 *)(a11 + 200) = 0;
loc_00A145BB:
    result = PspSelectMachineForProcess(v_stack_m7D0, a11, v_stack_m798, a11 + 200);
    if (!sign_flag) goto loc_00A145E1;
    goto loc_00A14547;
loc_00A145E1:
    v_stack_m79C = (unsigned int)(v_stack_m798);
    if (v_stack_m796 != 0) {
        v_rbx = (unsigned int)((v_rbx) | (64));
        v_stack_m7E4 = (unsigned int)(v_rbx);
    }
    if (v_stack_m795 != 0) {
    }
    if (*(unsigned __int64 *)(a11 + 200) == 0) goto loc_00A14AEC;
    if ((*(unsigned __int8 *)(a11 + 16)) < 0) goto loc_00A146C8;
    v_stack_m840 = v_stack_m7BC;
    v_stack_m848 = 2;
    result = RtlQueryImageFileKeyOption(*(unsigned __int64 *)(a11 + 200), v_rip + 985128, 1, v_stack_m7A8);
    if (((unsigned int)(result)) == 0x80000005ULL) goto loc_00A146B9;
    if (sign_flag) goto loc_00A1467C;
    if (v_stack_m7BC != 2) goto loc_00A1467C;
    if (v_stack_m7A8 != 0) goto loc_00A146B9;
loc_00A1467C:
    v_stack_m734 = 0;
    v_stack_m840 = 0;
    v_stack_m848 = 4;
    result = RtlQueryImageFileKeyOption(*(unsigned __int64 *)(a11 + 200), v_rip + 984993, 4, v_stack_m734);
    if (sign_flag) goto loc_00A146C8;
    if (v_stack_m734 != 1) goto loc_00A146C8;
loc_00A146B9:
    goto loc_00A14547;
loc_00A146C8:
    v_stack_m7A0 = 0;
    v_stack_m840 = 0;
    v_stack_m848 = 4;
    result = RtlQueryImageFileKeyOption(*(unsigned __int64 *)(a11 + 200), v_rip + 985125, 4, v_stack_m7A0);
    if (sign_flag) goto loc_00A147F3;
    if (v_stack_m7A0 == 0) goto loc_00A147F3;
    v_r12 = (unsigned int)(((unsigned int)(v_stack_m7D8)) | (16));
    v_stack_m7D8 = (unsigned int)(v_r12);
    v_stack_p48 = (unsigned int)(v_r12);
    if ((((unsigned __int8)(v_rbx)) & (64)) != 0) goto loc_00A147F3;
    v_stack_m618 = 48;
    v_stack_m610 = *(unsigned __int64 *)(a11 + 200);
    v_stack_m600 = 576;
    v_stack_m608 = v_rip + 1275659;
    v_stack_m5F8 = v_xmm0;
    result = ZwOpenKey(v_stack_m6F0, 1, v_stack_m618, v_stack_m7A0);
    if (sign_flag) goto loc_00A147F8;
    v_stack_m7A0 = 0;
    v_stack_m840 = 0;
    v_stack_m848 = 4;
    result = RtlQueryImageFileKeyOption(v_stack_m6F0, v_rip + 984892, 4, v_stack_m7A0);
    if (sign_flag) goto loc_00A147E2;
    if (v_stack_m7A0 != 0) {
        v_r12 = (unsigned int)((v_r12) | (32));
        v_stack_m7D8 = (unsigned int)(v_r12);
        v_stack_p48 = (unsigned int)(v_r12);
    }
    a2 = 0;
    result = ObCloseHandle(v_stack_m6F0, a2, 4, v_stack_m7A0);
    goto loc_00A147F8;
loc_00A147F3:
loc_00A147F8:
    if (v_stack_m728 == 0) {
        a3 = v_stack_m7B0;
        a2 = *(unsigned __int64 *)(a11 + 200);
        a1 = v_stack_m7C8;
        result = PspReadIFEONodeOptions(a1, a2, a3, v_stack_m7A0);
    }
    v_stack_m730 = 0;
    v_stack_m840 = 0;
    v_stack_m848 = 4;
    result = RtlQueryImageFileKeyOption(*(unsigned __int64 *)(a11 + 200), v_rip + 984725, 4, v_stack_m730);
    if (sign_flag) goto loc_00A1485C;
    if (v_stack_m730 != 0) {
    }
    v_stack_m840 = v_stack_m7BC;
    v_stack_m848 = 0;
    a4 = 0;
    result = RtlQueryImageFileKeyOption(*(unsigned __int64 *)(a11 + 200), v_rip + 984629, a4 + 3, a4);
    if (((unsigned int)(result)) != 0x80000005ULL) goto loc_00A1492F;
    if (((unsigned int)((unsigned int)(v_stack_m7BC))) > 256) goto loc_00A1492F;
    if ((((unsigned __int8)((unsigned int)(v_stack_m7BC))) & (7)) != 0) goto loc_00A1492F;
    result = ExAllocatePool2(64, (unsigned int)((unsigned int)((unsigned int)(v_stack_m7BC))), (unsigned int)(0x73437350ULL), a4);
    v_stack_m6C8 = result;
    if (result != 0) goto loc_00A148D8;
loc_00A148CE:
    goto loc_00A14CE8;
loc_00A148D8:
    v_stack_m840 = v_stack_m7BC;
    v_stack_m848 = (unsigned int)((unsigned int)(0xC0000017ULL));
    result = RtlQueryImageFileKeyOption(*(unsigned __int64 *)(a11 + 200), v_rip + 984503, 3, result);
    if (sign_flag) goto loc_00A1492F;
    if (((v_stack_m7BC) & (7)) == 0) {
        v_stack_m7E4 = (unsigned int)(v_rbx);
        result = v_stack_m7BC;
        result = (unsigned int)((result) >> (3));
        v_stack_m7A4 = (unsigned int)(result);
    }
    v_stack_m5E8 = 48;
    v_stack_m5E0 = *(unsigned __int64 *)(a11 + 200);
    v_stack_m5D0 = 576;
    v_stack_m5D8 = v_rip + 1275133;
    v_stack_m5C8 = v_xmm0;
    result = ZwOpenKey(v_stack_m6E8, 1, v_stack_m5E8, result);
    if (!(sign_flag)) {
        a2 = v_stack_m430;
        a1 = v_stack_m6E8;
        result = PspReadIFEOPerfOptions(a1, a2, v_stack_m5E8, result);
        a2 = 0;
        a1 = v_stack_m6E8;
        result = ObCloseHandle(a1, a2, v_stack_m5E8, result);
    }
    v_stack_m840 = 0;
    v_stack_m848 = 4;
    result = RtlQueryImageFileKeyOption(*(unsigned __int64 *)(a11 + 200), v_rip + 983905, 4, v_stack_m72C);
    if (sign_flag) goto loc_00A14A09;
    v_r14 = v_stack_m7C8;
    if (v_stack_m72C == 2) {
        v_r12 = a9;
        v_stack_m7D8 = (unsigned int)(v_r12);
        v_r14 = v_stack_m7C8;
    }
    if (v_stack_m72C >= 2) goto loc_00A14AF4;
    v_stack_m7D8 = (unsigned int)((unsigned int)(a9));
    goto loc_00A14AF4;
loc_00A14A39:
    if (*(unsigned __int64 *)(a11 + 200) == 0) goto loc_00A14AEC;
    result = MmGetSectionInformation(*(unsigned __int64 *)(a11 + 200), 4, v_stack_m4B8, v_stack_m72C);
    if (sign_flag) goto loc_00A14CE8;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m478)))) & (250));
    a2 = (unsigned int)((a2) + (a2));
    result = (unsigned int)(((unsigned int)(v_stack_m478)) & (1));
    a2 = (unsigned int)((a2) | ((unsigned int)(result)));
    a2 = (unsigned int)((a2) << (5));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m485))) & (2));
    a2 = (unsigned int)((a2) | ((unsigned int)(result)));
    a2 = (unsigned int)((a2) << (2));
    a1 = (unsigned int)((v_stack_m485) & (4));
    a2 = (unsigned int)((a2) | ((unsigned int)(a1)));
    a2 = (unsigned int)((a2) << (11));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (0xF82B9FFFULL));
    v_rbx = (unsigned int)(((unsigned int)(a2)) | ((unsigned int)(result)));
    v_stack_m7E4 = (unsigned int)(v_rbx);
    v_stack_m7C0 = (unsigned __int16)(v_stack_m48A);
    v_stack_m78C = (unsigned int)(v_stack_m492);
    v_stack_m790 = (unsigned int)(v_stack_m494);
    if (((4) & ((unsigned __int8)(v_rbx))) != 0) {
        v_rbx = (unsigned int)((v_rbx) | (24));
        v_stack_m7E4 = (unsigned int)(v_rbx);
    }
loc_00A14AF4:
    if ((((unsigned __int8)(v_rbx)) & (64)) == 0) goto loc_00A14B82;
    result = ExAllocatePool2(16 + 48, 16, (unsigned int)(0x50776F57ULL), v_stack_m72C);
    *(unsigned __int64 *)(v_stack_m7C8 + 784) = result;
    if (result == 0) goto loc_00A148CE;
    result = (unsigned int)(v_stack_m750);
    if ((unsigned int)((unsigned int)(v_stack_m750)) == 0) {
        a2 = (unsigned __int16)((unsigned int)(v_stack_m79C));
        a1 = a11;
        result = PspWow64PickBestNtdll(a1, a2, (unsigned int)(0x50776F57ULL), v_stack_m72C);
    }
    *(unsigned int *)(result + 8) = (unsigned int)(result);
    if (*(unsigned __int64 *)(v_stack_m7C8 + 784) != 0) {
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m7C8 + 784)) = 1;
    }
    if (condition_is_above_or_equal) goto loc_00A14B8A;
    v_stack_m7D8 = (unsigned int)((unsigned int)(a9));
    goto loc_00A14B8A;
loc_00A14B82:
loc_00A14B8A:
    *(unsigned __int16 *)(v_stack_m7C8 + 1772) = (unsigned __int16)((unsigned int)(v_stack_m79C));
    result = SeQueryInformationToken(v_stack_m768, 29, v_stack_m784, v_stack_m72C);
    if (sign_flag) goto loc_00A14CE8;
    if ((unsigned __int8)(v_stack_m7E8) == 0) goto loc_00A14CAD;
    if (a11 == 0) goto loc_00A14BED;
    if (condition_is_above_or_equal) goto loc_00A14BED;
    v_r10 = 0;
    if ((*(unsigned __int8 *)(a11 + 2)) == 4) {
        v_stack_mA8 = 14;
        v_r10 = 1;
    }
    result = (unsigned int)(*(unsigned int *)(a11 + 8));
    if ((unsigned int)((unsigned int)(a12)) != 0) {
        result = (unsigned int)(v_r10);
        *(unsigned int *)(v_rsp + result * 4 + 1984) = 3;
        v_r10 = (unsigned int)((v_r10) + (1));
    }
    if ((((unsigned __int8)((unsigned int)(a9))) & (48)) != 0) {
        result = (unsigned int)(v_r10);
        *(unsigned int *)(v_rsp + result * 4 + 1984) = 4;
        v_r10 = (unsigned int)((v_r10) + (1));
    }
    if (!sign_flag) goto loc_00A14C4E;
    result = PspIsSessionLeaderProcess(v_stack_m780, 29, v_stack_m784, v_stack_m72C);
    if ((unsigned int)(result) == 0) {
        result = (unsigned int)(v_r10);
        *(unsigned int *)(v_rsp + result * 4 + 1984) = 10;
        v_r10 = (unsigned int)((v_r10) + (1));
    }
    if ((((unsigned int)((unsigned int)(a9))) & (0x8400ULL)) != 0) {
        result = (unsigned int)(v_r10);
        *(unsigned int *)(v_rsp + result * 4 + 1984) = 7;
        v_r10 = (unsigned int)((v_r10) + (1));
    }
    if ((unsigned int)(v_r10) == 0) goto loc_00A14CA6;
    a3 = ((unsigned int)((unsigned int)(a12)) != 0) ? 1 : 0;
    result = RtlAcquirePrivilege(v_stack_mA8, (unsigned int)((unsigned int)(v_r10)), a3, v_stack_m6D0);
    if (sign_flag) goto loc_00A14CAD;
    v_stack_m7E4 = (unsigned int)(v_rbx);
    goto loc_00A14CAD;
loc_00A14CA6:
loc_00A14CAD:
    if ((((unsigned int)((unsigned int)(a9))) & (0x8400ULL)) == 0) goto loc_00A14D68;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 6049205), (unsigned __int8)(v_stack_m7E8), a3, v_stack_m6D0);
    if ((unsigned __int8)(result) != 0) goto loc_00A14D68;
loc_00A14CD0:
loc_00A14CD5:
    if (!(condition_is_above_or_equal)) {
        a1 = v_stack_m6D0;
        result = RtlReleasePrivilege(a1, (unsigned __int8)(v_stack_m7E8), a3, v_stack_m6D0);
    }
    if (v_stack_m758 != 0) {
        *(unsigned __int64 *)(v_stack_m7C8 + 464) = v_stack_m758;
    }
    a2 = 0;
    result = PspRundownSingleProcess(v_stack_m7C8, a2, a3, v_stack_m6D0);
    result = ObfDereferenceObjectWithTag(v_stack_m7C8, (unsigned int)(0x72437350ULL), a3, v_stack_m6D0);
loc_00A14D13:
    result = v_stack_m6C8;
    if (v_stack_m6C8 != 0) {
        a2 = 0x73437350ULL;
        a1 = v_stack_m6C8;
        result = ExFreePoolWithTag(a1, a2, a3, v_stack_m6D0);
    }
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, v_stack_m6D0);
    if ((unsigned int)(result) == 0) goto loc_00A14D48;
    if (v_stack_m708 != 0) {
        result = SeFreeAntiTamperPolicy(v_stack_m708, a2, a3, v_stack_m6D0);
    }
    result = *(unsigned __int64 *)(v_rip + 5177785);
    if (*(unsigned __int64 *)(v_rip + 5177785) != 0) {
        a1 = v_stack_m2C8;
        result = guard_dispatch_icall(a1, a2, a3, v_stack_m6D0);
    }
    goto loc_00A16384;
loc_00A14D68:
    v_stack_m7DC = (unsigned __int16)((unsigned int)(0xFFFFULL));
    v_stack_m3D8 = 0x200001ULL;
    a2 = 0;
    result = memset(v_stack_m3D0, a2, 256, v_stack_m6D0);
    if (v_stack_m728 != 0) goto loc_00A14EEB;
    if (v_stack_m7B0 != 0) goto loc_00A14E65;
    if (v_stack_m7D0 == 0) goto loc_00A14E49;
    if (((*(unsigned int *)(v_stack_m7D0 + 496)) & (0x100000ULL)) == 0) goto loc_00A14DFA;
    v_stack_m7B0 = *(unsigned __int64 *)(v_rip + 6006999 + *(unsigned __int16 *)(v_stack_m7D0 + 260) * 8);
    goto loc_00A14E6D;
loc_00A14DFA:
    result = PspSelectNodeForProcess(*(unsigned __int64 *)(v_rip + 6006999 + *(unsigned __int16 *)(v_stack_m7D0 + 260) * 8), a2, 256, v_stack_m6D0);
    v_stack_m7B0 = result;
    result = KeSelectGroupFromNode(result, a2, 256, v_stack_m6D0);
    v_stack_m7DC = (unsigned __int16)(result);
    if ((*(unsigned __int8 *)(v_rip + 5971153)) == 0) goto loc_00A14E7D;
    result = KeQueryActiveGroupCount(result, a2, 256, v_stack_m6D0);
    if (((unsigned __int16)(result)) <= 1) goto loc_00A14E7D;
    if ((unsigned __int16)((unsigned __int16)(result)) != 0) goto loc_00A14E7D;
    v_stack_m7B0 = 0;
    v_stack_m7DC = 1;
    goto loc_00A14E7D;
loc_00A14E49:
    v_stack_m7DC = 0;
    a2 = 0;
    result = KeAddProcessorAffinityEx(v_stack_m3D8, a2, 256, v_stack_m6D0);
    goto loc_00A14E7D;
loc_00A14E65:
loc_00A14E6D:
    result = KeSelectGroupFromNode(v_stack_m7B0, a2, 256, v_stack_m6D0);
    v_stack_m7DC = (unsigned __int16)(result);
loc_00A14E7D:
    result = KiCopyAffinityEx(v_stack_m3D8, v_stack_m3D6, v_rip + 5972636, v_stack_m6D0);
    if (v_stack_m7B0 != 0) goto loc_00A14F36;
    v_stack_m628 = v_xmm0;
    v_stack_m620 = (unsigned __int16)((unsigned __int16)(result));
    if (((unsigned __int16)((unsigned __int16)(result))) >= v_stack_m3D8) goto loc_00A14ED1;
    goto loc_00A14ED4;
loc_00A14ED1:
loc_00A14ED4:
    v_stack_m628 = 0;
    result = KeSelectNodeForAffinity(v_stack_m628, v_stack_m3D6, v_rip + 5972636, v_stack_m6D0);
    goto loc_00A14F2E;
loc_00A14EEB:
    v_stack_m848 = v_stack_m7DC;
    a3 = 0;
    result = KeQueryAffinityProcess(result, v_stack_m3D8, a3, v_stack_m88);
loc_00A14F2E:
    v_stack_m7B0 = *(unsigned __int64 *)(v_rip + 6006678 + *(unsigned __int16 *)(v_rsp + v_stack_m7DC * 2 + 2016) * 8);
loc_00A14F36:
    if (v_stack_m7D0 == 0) goto loc_00A151C3;
    v_stack_m6E0 = 0;
    v_stack_m774 = 0;
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFDFULL));
    v_stack_m7E0 = 0;
    if (a12 == 0) goto loc_00A15079;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 6048811), v_stack_m7E8, a3, v_stack_m88);
    if ((unsigned __int8)(result) == 0) { v_rbx = (unsigned int)((unsigned int)((unsigned int)(v_rbx))); }
    result = SeIsTokenAssignableToProcess(v_stack_m768, v_stack_m7E0, a3, v_stack_m88);
    if (sign_flag) goto loc_00A14CD5;
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (9));
    if (v_stack_m7E0 != 0) goto loc_00A14FEB;
    if ((((unsigned __int8)(v_r13)) & (1)) == 0) goto loc_00A14CD0;
loc_00A14FEB:
    result = SeQuerySessionIdToken(v_stack_m768, v_stack_m774, a3, v_stack_m88);
    if (sign_flag) goto loc_00A14CD5;
    result = PsGetProcessSessionIdEx(v_stack_m780, v_stack_m774, a3, v_stack_m88);
    if (((unsigned int)((unsigned int)(v_stack_m774))) == ((unsigned int)(result))) goto loc_00A15043;
    if ((((unsigned __int8)(v_r13)) & (1)) == 0) goto loc_00A14CD0;
    if (((v_stack_m7D8) & (128)) == 0) goto loc_00A15040;
    goto loc_00A14CD5;
loc_00A15040:
    v_rbx = (unsigned int)((v_rbx) | (32));
loc_00A15043:
loc_00A1504B:
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (32));
    if (condition_is_equal) goto loc_00A150BB;
    result = PspAttachSession((unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))), v_stack_m408, v_stack_m6E0, v_stack_m88);
    if (!sign_flag) goto loc_00A150B2;
    v_rbx = (unsigned int)((v_rbx) & (0xFFFFFFDFULL));
    goto loc_00A14CD5;
loc_00A15079:
    if ((((unsigned __int8)(v_rbx)) & (4)) == 0) goto loc_00A1504B;
    result = PsGetProcessSessionIdEx(v_r12, v_stack_m408, v_stack_m6E0, v_stack_m88);
    v_stack_m774 = (unsigned int)(result);
    result = PsGetProcessSessionIdEx(v_stack_m780, v_stack_m408, v_stack_m6E0, v_stack_m88);
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))))) - ((unsigned int)(result)));
    a1 = (unsigned int)(-(a1));
    a2 = (unsigned int)((v_stack_m408) & (32));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (0xFFFFFFDFULL));
    v_rbx = (unsigned int)(((unsigned int)(a2)) | ((unsigned int)(result)));
    goto loc_00A1504B;
loc_00A150B2:
loc_00A150BB:
    if (a12 == 0) goto loc_00A15104;
    if ((unsigned __int8)(v_stack_m7E0) != 0) goto loc_00A15104;
    a1 = 0;
    result = PspAssignProcessQuotaBlock(a1, v_stack_m7C8, v_stack_m768, v_stack_m88);
    if (!sign_flag) goto loc_00A15125;
    if ((unsigned int)(v_r12) == 0) goto loc_00A14CD5;
    result = PspDetachSession(v_stack_m6E0, v_stack_m408, v_stack_m768, v_stack_m88);
    goto loc_00A14CD5;
loc_00A15104:
    a2 = v_stack_m7D0;
    if ((unsigned __int8)(v_stack_m7E0) != 0) { a2 = v_stack_m780; }
    result = PspInheritQuota(v_stack_m7C8, a2, v_stack_m768, v_stack_m88);
    goto loc_00A1512D;
loc_00A15125:
loc_00A1512D:
    a4 = (unsigned int)(((unsigned int)(v_stack_m42C)) & (1));
    a3 = *(unsigned __int64 *)(v_rip + 6041859);
    if (condition_is_not_equal) { a3 = v_stack_m418; }
    if (((v_stack_m7D8) & (0x400000ULL)) != 0) {
        a4 = (unsigned int)((a4) | (16));
    }
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_m7B0)) + (1));
    v_stack_m840 = v_stack_m7C8;
    v_stack_m848 = (unsigned int)(a1);
    result = MmCreateProcessAddressSpace(v_stack_m720, a2, a3, a4);
    result = (unsigned int)(((unsigned __int8)(result)) << (11));
    result = (unsigned int)((result) ^ ((unsigned int)(v_rbx)));
    result = (unsigned int)((result) & ((unsigned int)((unsigned int)(0x800ULL))));
    v_rbx = (unsigned int)((v_rbx) ^ ((unsigned int)(result)));
    v_stack_m7E4 = (unsigned int)(v_rbx);
    if ((((unsigned __int8)(v_rbx)) & (32)) != 0) {
        a2 = v_stack_m408;
        a1 = v_stack_m6E0;
        result = PspDetachSession(a1, a2, a3, a4);
    }
    if ((((unsigned int)((unsigned int)(0x800ULL))) & ((unsigned int)(v_rbx))) != 0) goto loc_00A151E3;
loc_00A151B9:
    goto loc_00A14CD5;
loc_00A151C3:
    a2 = 0;
    result = PspInheritQuota(v_stack_m7C8, a2, a3, a4);
    *(unsigned __int8 *)(v_stack_m7C8 + 352) = 1;
    result = MmInitializeHandBuiltProcess(v_stack_m7C8, a2, a3, a4);
    if (sign_flag) goto loc_00A14CD5;
loc_00A151E3:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m7C8 + 904)))) & (4)) != 0) {
        a1 = (unsigned int)(((unsigned int)(v_stack_m770)) | (1));
    }
    a4 = ((unsigned int)(v_stack_m700)) + (v_stack_m7C8);
    a3 = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (2));
    if (condition_is_above_or_equal) { a3 = (unsigned int)(a1); }
    result = PsGetSessionSchedulingGroupByProcess(v_stack_m7C8, a2, a3, a4);
    v_stack_m828 = a4;
    v_stack_m830 = (unsigned int)(a3);
    v_stack_m840 = result;
    v_stack_m848 = v_stack_m7B0;
    result = KeInitializeProcess(v_stack_m7C8, 8, v_stack_m7DC, v_stack_m3D8);
    if (sign_flag) goto loc_00A14CD5;
    if (a11 == 0) goto loc_00A153AE;
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) goto loc_00A153AE;
    v_stack_m744 = (unsigned int)((unsigned int)(*(unsigned int *)(a11 + 384)));
    v_stack_m748 = (unsigned int)((unsigned int)(*(unsigned int *)(a11 + 388)));
    v_stack_m6A0 = *(unsigned __int64 *)(a11 + 408);
    v_stack_m74C = (unsigned int)((unsigned int)(*(unsigned int *)(a11 + 392)));
    v_stack_m6A8 = *(unsigned __int64 *)(a11 + 216);
    v_stack_m794 = (unsigned int)((unsigned int)(*(unsigned int *)(a11 + 396)));
    if (*(unsigned __int64 *)(a11 + 184) == 0) goto loc_00A153B1;
    if (*(unsigned __int64 *)(v_rip + 5176331) == 0) goto loc_00A153B1;
    result = guard_dispatch_icall(*(unsigned __int64 *)(a11 + 184), v_stack_m2C8, v_stack_m7DC, v_stack_m3D8);
    if (sign_flag) goto loc_00A153B1;
    if (v_stack_m2C8 != 0) goto loc_00A15399;
    if (*(unsigned __int64 *)(a11 + 400) == 0) goto loc_00A15399;
    if (v_stack_m794 != 524) goto loc_00A15399;
loc_00A1533B:
    *(unsigned __int64 *)(v_stack_m2C8) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m2C8 + 16) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m2C8 + 32) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m2C8 + 48) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m2C8 + 64) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m2C8 + 80) = v_xmm1;
    *(unsigned __int64 *)(v_stack_m2C8 + 96) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m2C8 + 128 - 16) = v_xmm1;
    result = (4) - (1);
    if (condition_is_not_equal) goto loc_00A1533B;
    *(unsigned __int64 *)(v_stack_m2C8 + 128) = *(unsigned __int64 *)(*(unsigned __int64 *)(a11 + 400) + 128);
    *(unsigned int *)(v_stack_m2C8 + 128 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a11 + 400) + 128 + 8)));
loc_00A15399:
    v_stack_m794 = 536;
    goto loc_00A153B1;
loc_00A153AE:
loc_00A153B1:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(v_stack_m2C8 + 128, v_stack_m2C8, v_stack_m7DC, v_stack_m3D8);
    if ((unsigned int)(result) == 0) goto loc_00A153D6;
    if (a11 == 0) goto loc_00A153D6;
    if (!(condition_is_above_or_equal)) {
        result = a11 + 496;
        v_stack_m6B0 = result;
    }
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (16));
    a1 = (unsigned int)((a1) & (1));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (4));
    result = (unsigned int)((result) & (1));
    v_stack_m7F8 = v_stack_m648;
    v_stack_m800 = v_stack_m6B0;
    v_stack_m808 = v_stack_m6A8;
    v_stack_m810 = (unsigned int)((unsigned int)(v_stack_m74C));
    v_stack_m818 = v_stack_m6A0;
    v_stack_m820 = (unsigned int)((unsigned int)(v_stack_m794));
    v_stack_m828 = 0;
    v_stack_m830 = (unsigned int)((unsigned int)(v_stack_m748));
    v_stack_m838 = (unsigned int)(a1);
    v_stack_m840 = (unsigned int)(result);
    v_stack_m848 = (unsigned int)((unsigned int)(v_stack_m744));
    result = PspInitializeProcessSecurity(v_stack_m7D0, v_stack_m7C8, v_stack_m768, (unsigned int)(a12));
    if (sign_flag) goto loc_00A14CD5;
    *(unsigned __int8 *)(v_stack_m7C8 + 839) = 2;
    if (v_stack_m7D0 == 0) goto loc_00A154DA;
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_stack_m7D0 + 839))) - (1));
    if ((((unsigned __int8)(result)) & (251)) == 0) {
        *(unsigned __int8 *)(v_stack_m7C8 + 839) = (unsigned __int8)(*(unsigned __int8 *)(v_stack_m7D0 + 839));
    }
    if (a11 == 0) goto loc_00A154AB;
    goto loc_00A154AE;
loc_00A154AB:
loc_00A154AE:
    if (a11 == 0) goto loc_00A154BC;
    goto loc_00A154BF;
loc_00A154BC:
loc_00A154BF:
    result = (unsigned __int8)(((unsigned int)(a9)) & (4));
    result = (unsigned __int8)(-(result));
    a1 = (*(unsigned __int8 *)(v_stack_m7D0 + 839)) & (v_stack_m7D0);
    result = ObInitProcess(a1, v_stack_m7C8, 0, 0);
    goto loc_00A154F8;
loc_00A154DA:
    *(unsigned __int64 *)(v_stack_m7C8 + 768) = *(unsigned __int64 *)(v_stack_m780 + 768);
    result = MmInitializeHandBuiltProcess2(v_stack_m7C8, v_stack_m7C8, 0, 0);
loc_00A154F8:
    if (sign_flag) goto loc_00A14CD5;
    if (((v_stack_m430) & (7)) != 0) {
        a3 = (unsigned __int8)(v_stack_m7E8);
        a2 = v_stack_m430;
        a1 = v_stack_m7C8;
        result = PspApplyIFEOPerfOptions(a1, a2, a3, 0);
    }
    if (!(condition_is_above_or_equal)) {
        v_stack_m848 = 0;
        a4 = 1;
        a3 = v_stack_m6C8;
        a2 = v_stack_m7A4;
        a1 = v_stack_m7C8;
        result = KeSetCpuSetsProcess(a1, a2, a3, a4);
    }
    if (((v_stack_m42C) & (2)) != 0) {
        a2 = v_stack_m410;
        a1 = v_stack_m7C8;
        result = KeSetExpectedConcurrencyCountProcess(a1, a2, a3, a4);
    }
    if (a11 == 0) goto loc_00A15591;
    if (condition_is_above_or_equal) goto loc_00A15591;
    a3 = 0;
    result = PspSetProcessPriorityClass(v_stack_m7C8, *(unsigned __int8 *)(a11 + 2), a3, (unsigned __int8)(v_stack_m7E8));
    if (sign_flag) goto loc_00A14CD5;
loc_00A15591:
    v_stack_m848 = 0;
    a4 = 0;
    a2 = 0;
    result = PspComputeQuantumAndPriority(v_stack_m7C8, a2, v_stack_m7D4, a4);
    *(unsigned __int8 *)(v_stack_m7C8 + 144) = (unsigned __int8)(result);
    *(unsigned __int8 *)(v_stack_m7C8 + 145) = (unsigned __int8)(v_stack_m7D4);
    v_stack_m7A4 = 0;
    result = PspReadIFEOMitigationOptions(a11, v_stack_m468, v_stack_m7D4, a4);
    v_stack_m5B8 = v_xmm0;
    v_stack_m5A8 = v_xmm0;
    v_stack_m598 = v_xmm1;
    v_stack_m588 = v_xmm0;
    result = PspInheritMitigationOptions(v_stack_m598, v_stack_m5B8, v_stack_m468, a4);
    result = PspReadIFEOMitigationAuditOptions(a11, v_stack_m450, v_stack_m468, a4);
    v_stack_m578 = v_xmm0;
    v_stack_m568 = v_xmm0;
    v_stack_m558 = v_xmm1;
    v_stack_m548 = v_xmm0;
    result = PspInheritMitigationAuditOptions(v_stack_m558, v_stack_m578, v_stack_m450, a4);
    v_rdi = (v_stack_m468) >> (48);
    v_rdi = (unsigned int)((v_rdi) & (3));
    v_rdi = (unsigned int)((v_rdi) << (14));
    if (a11 == 0) goto loc_00A1579D;
    result = (unsigned int)(*(unsigned int *)(a11 + 8));
    if (!(condition_is_above_or_equal)) {
        v_stack_m538 = v_xmm0;
        v_stack_m528 = v_xmm1;
        v_stack_m518 = v_xmm0;
        v_stack_m508 = v_xmm0;
        a3 = v_stack_m468;
        a2 = v_stack_m538;
        a1 = v_stack_m518;
        result = PspInheritMitigationOptions(a1, a2, a3, a4);
    }
    if (a11 == 0) goto loc_00A1579D;
    result = (unsigned int)(*(unsigned int *)(a11 + 8));
    if (!(condition_is_above_or_equal)) {
        v_stack_m4F8 = v_xmm0;
        v_stack_m4E8 = v_xmm1;
        v_stack_m4D8 = v_xmm0;
        v_stack_m4C8 = v_xmm0;
        a3 = v_stack_m450;
        a2 = v_stack_m4F8;
        a1 = v_stack_m4D8;
        result = PspInheritMitigationAuditOptions(a1, a2, a3, a4);
    }
    if (v_stack_m784 != 0) {
        v_rdi = (unsigned int)((v_rdi) | (4));
    }
    v_r11 = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) | (64));
    if ((((unsigned __int8)(v_rdi)) & (4)) == 0) { v_r11 = (unsigned int)(v_rdi); }
    if ((((unsigned int)(v_r11)) & (0x3FC0ULL)) != 0) {
        a1 = v_stack_m468;
        result = PspHardenMitigationOptions(a1, a2, a3, a4);
    }
    result = KeIsUserCetAllowed(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        result = v_stack_m460;
        result = (result) & (0);
        result = (result) | (v_r10);
        v_stack_m460 = result;
    }
    a2 = (unsigned __int16)(((unsigned __int16)(v_stack_m7C0)) & ((unsigned __int16)((unsigned int)(0x4000ULL))));
    a3 = ((((unsigned int)(v_rbx)) & (0x6000ULL)) != 0) ? 1 : 0;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m7C0))) >> (4));
    result = (unsigned int)((result) & (2));
    a3 = (unsigned int)((a3) | ((unsigned int)(result)));
    result = (unsigned __int16)(-((unsigned __int16)(a2)));
    a1 = (unsigned int)((v_stack_m7C0) & (8));
    a3 = (unsigned int)((a3) | ((unsigned int)(a1)));
    a3 = (unsigned int)((a3) | ((unsigned int)(v_r11)));
    if ((unsigned __int16)(a2) == 0) goto loc_00A15848;
    if (!(condition_is_below)) {
        v_stack_m740 = 0;
    }
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (1));
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (0x3E00000ULL));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) & (0x100000ULL));
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(result)));
    v_rdi = (unsigned int)((v_rdi) >> (4));
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(a3)));
    v_rdi = (unsigned int)((v_rdi) | (v_stack_m740));
    if (((1) & ((unsigned __int8)(a1))) == 0) goto loc_00A15906;
    a1 = (v_stack_m468) & (result);
    a1 = (a1) | (result);
    v_stack_m468 = a1;
    result = (v_stack_m460) & (a2);
    result = (result) | (a2);
    v_stack_m460 = result;
    a1 = (a1) & (0xFFFFFFFFFFFCFFFFULL);
    if (((a10) & (2)) == 0) goto loc_00A158ED;
    a1 = (a1) | (0x220000ULL);
    goto loc_00A158FE;
loc_00A158ED:
    a1 = (a1) & (0xFFFFFFFFFFCFFFFFULL);
loc_00A158FE:
    v_stack_m468 = a1;
loc_00A15906:
    if ((((unsigned __int8)(v_rbx)) & (4)) == 0) goto loc_00A1592F;
    if (((*(unsigned int *)(v_stack_m7D0 + 1876)) & (0x4000ULL)) == 0) {
        result = v_stack_m460;
        result = (result) & (0);
        result = (result) | (v_r10);
        v_stack_m460 = result;
    }
    if ((((unsigned __int8)(v_rbx)) & (64)) != 0) {
        result = v_stack_m460;
        result = (result) & (0);
        result = (result) | (v_r10);
        v_stack_m460 = result;
    }
    v_stack_m458 = v_stack_m458;
    result = KeIsCoreIsolationMitigationPolicyEnforceable(v_stack_m458, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        v_stack_m458 = v_stack_m458;
    }
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(v_stack_m458, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00A159CA;
    if (a11 == 0) goto loc_00A159A4;
    if (!(condition_is_above_or_equal)) {
        result = a11 + 528;
        v_stack_m670 = result;
    }
    result = PspReadIFEOAntiTamperOptions(a11, v_stack_m438, a3, a4);
    a1 = v_stack_m438;
    if (sign_flag) { a1 = 0; }
    v_stack_m6D8 = a1;
loc_00A159CA:
    v_stack_m838 = (unsigned int)((unsigned int)(v_stack_m790));
    v_stack_m840 = (unsigned int)((unsigned int)(v_stack_m78C));
    v_stack_m848 = (unsigned int)(v_rdi);
    result = PspApplyMitigationOptions(v_stack_m7C8, v_stack_m7D0, v_stack_m468, v_stack_m450);
    if (a11 == 0) goto loc_00A15AC2;
    if (*(unsigned __int64 *)(a11 + 432) == 0) goto loc_00A15A5F;
    v_r14 = v_stack_m7C8;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a11 + 432)))))) != 0) {
        v_r14 = v_stack_m7C8;
    }
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a11 + 432))))) & (2)) != 0) {
        v_r14 = v_stack_m7C8;
    }
    *(unsigned int *)(v_r14 + 1768) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a11 + 432) + 4)));
loc_00A15A5F:
    if (a11 == 0) goto loc_00A15AC2;
    result = *(unsigned __int64 *)(a11 + 440);
    if (*(unsigned __int64 *)(a11 + 440) != 0) {
        result = *(unsigned int *)(*(unsigned __int64 *)(a11 + 440));
        *(unsigned int *)(v_r14 + 1952) = (unsigned int)(result);
    }
    if (a11 != 0) {
        *(unsigned __int64 *)(a11 + 336) = v_xmm0;
        *(unsigned __int64 *)(a11 + 352) = v_xmm0;
        *(unsigned __int64 *)(a11 + 448) = v_xmm1;
        *(unsigned __int64 *)(a11 + 464) = v_xmm0;
    }
    v_stack_m640 = 0;
    v_stack_m638 = 0;
    v_stack_m848 = v_stack_m640;
    result = AppModelPolicy_GetPolicy_Internal(v_stack_m768, 1, v_stack_m788, v_stack_m638);
    result = (unsigned int)(v_stack_m788);
    if (sign_flag) { result = (unsigned int)((unsigned int)(0x10000ULL)); }
    v_stack_m788 = (unsigned int)(result);
    a1 = 0;
    if (((unsigned int)(result)) == 0x10001ULL) { a1 = 1; }
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (2));
    if (((a9) & (0x20000ULL)) == 0) { a2 = (unsigned int)(a1); }
    result = SmProcessCreateNotification(v_r14, a2, v_stack_m788, v_stack_m638);
    if (((*(unsigned int *)(v_r14 + 1876)) & (0x4000ULL)) == 0) goto loc_00A15B5E;
    result = KeInitializeProcessUserCetLogging(v_r14, a2, v_stack_m788, v_stack_m638);
    if (sign_flag) goto loc_00A14CD5;
loc_00A15B5E:
    if (((a9) & (128)) == 0) goto loc_00A15B94;
    result = PspIsSessionLeaderProcess(v_stack_m780, a2, v_stack_m788, v_stack_m638);
    if ((unsigned int)(result) != 0) goto loc_00A15B94;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 6045593), v_stack_m7E8, v_stack_m788, v_stack_m638);
    if ((unsigned __int8)(result) == 0) goto loc_00A14CD0;
loc_00A15B94:
    if (((1) & ((unsigned __int8)(v_rbx))) != 0) goto loc_00A15D3B;
    if ((((unsigned __int8)(v_rbx)) & (4)) != 0) goto loc_00A15C29;
    result = PspInitializeFullProcessImageName(a11, v_r14, v_stack_m788, v_stack_m638);
    if (sign_flag) goto loc_00A14CD5;
    v_stack_m848 = 0;
    a2 = 0;
    result = MmInitializeProcessAddressSpace(v_r14, a2, v_stack_m760, a9);
    if (sign_flag) goto loc_00A14CD5;
    v_stack_m7A4 = (unsigned int)(result);
    if (a11 == 0) goto loc_00A15C19;
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) goto loc_00A15C19;
    result = MiSectionControlArea(v_stack_m760, a2, v_stack_m760, a9);
    result = *(unsigned __int64 *)(v_r14 + 688);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 32)) != (*(unsigned __int64 *)(v_r14 + 688))) {
        result = (*(unsigned __int64 *)(v_r14 + 688)) - (*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 32));
    }
    v_stack_m7E4 = (unsigned int)(v_rbx);
    goto loc_00A15D08;
loc_00A15C29:
    *(unsigned __int64 *)(v_r14 + 688) = *(unsigned __int64 *)(v_stack_m760 + 688);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (3));
    result = (unsigned int)((result) & (1));
    v_stack_m848 = (unsigned int)(result);
    a3 = 0;
    result = MmInitializeProcessAddressSpace(v_r14, v_stack_m760, a3, a9);
    if (sign_flag) goto loc_00A14CD5;
    result = ExAllocatePool2(64, *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m760 + 848) + 2) + 16, (unsigned int)(0x61506553ULL), a9);
    *(unsigned __int64 *)(v_r14 + 848) = result;
    if (result == 0) goto loc_00A151B9;
    result = memcpy(result, *(unsigned __int64 *)(v_stack_m7D0 + 848), *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m760 + 848) + 2) + 16, a9);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + 848) + 8) = *(unsigned __int64 *)(v_r14 + 848) + 16;
    *(unsigned int *)(v_r14 + 696) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m7D0 + 696)));
    if (((*(unsigned int *)(v_stack_m7D0 + 496)) & ((unsigned int)((unsigned int)(0x1000000ULL)))) != 0) {
    }
    result = (unsigned int)(*(unsigned int *)(v_stack_m7D0 + 696));
    if (((a9) & (0x1000ULL)) != 0) {
        *(unsigned __int64 *)(v_r14 + 680) = 0;
        a1 = v_stack_m760;
        result = ObfDereferenceObject(a1, *(unsigned __int64 *)(v_stack_m7D0 + 848), *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m760 + 848) + 2) + 16, a9);
    }
    if (((1) & ((unsigned __int8)(v_rbx))) != 0) goto loc_00A15D3B;
    a1 = (unsigned int)(((unsigned int)(a9)) & (16));
    a1 = (unsigned int)((a1) << (8));
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(a1))) | ((unsigned int)((unsigned int)((unsigned int)(v_rbx)))));
    v_stack_m7E4 = (unsigned int)(v_rbx);
    if ((((unsigned __int8)(v_rbx)) & (2)) == 0) {
        v_stack_m7E4 = (unsigned int)(v_rbx);
    }
    result = (unsigned int)((unsigned int)(v_rbx));
    if (!(condition_is_above_or_equal)) {
        a1 = v_stack_m6D0;
        result = RtlReleasePrivilege(a1, *(unsigned __int64 *)(v_stack_m7D0 + 848), *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m760 + 848) + 2) + 16, a9);
    }
    if ((*(unsigned __int16 *)(v_r14 + 1772)) == 332) {
    }
    if (!sign_flag) goto loc_00A15D8F;
    if (a11 == 0) goto loc_00A15D8F;
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) goto loc_00A15D8F;
    result = PspSetupReservedUserMappings(v_r14, v_stack_m408, a11, a9);
    if (sign_flag) goto loc_00A14CE8;
loc_00A15D8F:
    if (condition_is_above_or_equal) goto loc_00A15EAB;
    a2 = 0;
    result = PsQueryProcessAttributes(v_r14, a2, v_stack_m7D3, a9);
    result = 0;
    v_stack_m6C0 = 0;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_r14 + 1530)) & (7));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (12));
    a2 = (unsigned __int8)((a2) & (1));
    a1 = (unsigned __int8)((v_r14) & (2));
    a2 = (unsigned __int8)((a2) | ((unsigned __int8)(a1)));
    a1 = (unsigned __int8)((v_stack_m6BD) & (252));
    a2 = (unsigned __int8)((a2) | ((unsigned __int8)(a1)));
    a2 = (unsigned __int8)((a2) & (187));
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (13));
    a1 = (unsigned __int8)((a1) & (1));
    result = (((unsigned __int8)(result)) != 1) ? 1 : 0;
    result = (unsigned __int8)((result) - (1));
    result = (unsigned __int8)((result) & (16));
    a1 = (unsigned __int8)((a1) | ((unsigned __int8)(result)));
    a1 = (unsigned __int8)((a1) << (2));
    a2 = (unsigned __int8)((a2) | ((unsigned __int8)(a1)));
    result = (unsigned int)(-((unsigned int)(v_stack_m784)));
    a1 = (unsigned __int8)((a1) & (2));
    v_r12 = (unsigned __int8)((v_stack_m7D3) & (1));
    v_r12 = (unsigned __int8)((v_r12) | ((unsigned __int8)(a1)));
    v_r12 = (unsigned __int8)((v_r12) << (4));
    a2 = (unsigned __int8)((a2) & (207));
    v_r12 = (unsigned __int8)((v_r12) | ((unsigned __int8)(a2)));
    v_stack_m6BD = (unsigned __int8)(v_r12);
    if ((((unsigned __int8)(v_rbx)) & (4)) != 0) goto loc_00A15EEA;
    result = MmCreatePeb(v_r14, v_stack_m6C0, v_r14 + 736, v_stack_m658);
    if (!sign_flag) goto loc_00A15E6A;
    *(unsigned __int64 *)(v_r14 + 736) = 0;
    goto loc_00A14CE8;
loc_00A15E6A:
    if (v_stack_m658 != 0) {
        result = v_stack_m6FC;
        v_stack_m848 = result;
        a4 = v_stack_m658;
        a3 = 0;
        a2 = 1;
        v_r14 = v_stack_m7C8;
        a1 = v_r14;
        result = PspSetProcessAffinitySafe(a1, a2, a3, a4);
    }
loc_00A15EB3:
    if (!sign_flag) goto loc_00A160BB;
    if (a11 == 0) goto loc_00A160BB;
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) goto loc_00A160BB;
    result = PspSetupUserProcessAddressSpace(v_stack_m7D0, v_r14, v_stack_m408, a11);
    goto loc_00A16154;
loc_00A15EEA:
    *(unsigned __int64 *)(v_r14 + 736) = *(unsigned __int64 *)(v_stack_m7D0 + 736);
    if ((((unsigned __int8)(v_rbx)) & (16)) != 0) goto loc_00A160B0;
    v_stack_m6C0 = 1;
    a2 = 0;
    result = KiStackAttachProcess(v_r14, a2, v_stack_m408, a11);
    result = MmSecureVirtualMemory(*(unsigned __int64 *)(v_stack_m7D0 + 736), (unsigned int)(0x7D8ULL), 4, a11);
    if (result == 0) goto loc_00A15FAC;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m7D0 + 736)) = v_xmm0;
    goto loc_00A15FBF;
loc_00A15FAC:
loc_00A15FBF:
    if (sign_flag) goto loc_00A1608E;
    if (*(unsigned __int64 *)(v_r14 + 784) == 0) goto loc_00A1608E;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r14 + 1772))) == 332) goto loc_00A15FF1;
    result = 0;
    if (((unsigned __int16)(*(unsigned __int16 *)(v_r14 + 1772))) == 452) {
        result = 1;
    }
    if ((unsigned __int8)(result) == 0) goto loc_00A1608E;
    result = MmSecureVirtualMemory(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + 784)), (unsigned int)(0x490ULL), 1 + 3, a11);
    if (result == 0) goto loc_00A16089;
    result = 0;
    v_stack_m710 = 0;
    v_stack_m710 = 1;
    v_stack_m70D = (unsigned __int8)(v_r14 + 736);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_r14 + 784))) = v_stack_m710;
    goto loc_00A16094;
loc_00A16089:
loc_00A1608E:
loc_00A16094:
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_m408, a2, 1 + 3, a11);
    if (sign_flag) goto loc_00A14CE8;
    goto loc_00A15EAB;
loc_00A160B0:
    goto loc_00A15EB3;
loc_00A160BB:
    if (condition_is_above_or_equal) goto loc_00A16154;
    if ((((unsigned __int8)(v_rbx)) & (16)) != 0) goto loc_00A16154;
    a2 = 0;
    result = KiStackAttachProcess(v_r14, a2, v_stack_m408, a11);
    result = KeCopyXfdMaskToPeb(v_r14, a2, v_stack_m408, a11);
    result = PspUpdatePebForAffinityChange(v_stack_m668, v_r14, v_stack_m408, a11);
    if (!sign_flag) goto loc_00A16145;
    result = MmMapApiSetView(v_r14, v_r14, v_stack_m408, a11);
    if (sign_flag) goto loc_00A16145;
    result = PspMapSiloSharedDataView(v_r14, v_r14, v_stack_m408, a11);
    if (sign_flag) goto loc_00A16145;
    a2 = 0;
    a1 = 0;
    result = PspPrepareSystemDllInitBlock(a1, a2, v_stack_m408, a11);
    if (sign_flag) goto loc_00A16145;
    v_rdi = (unsigned int)((unsigned int)(result));
    if ((*(unsigned __int64 *)(v_r14 + 784)) != 0) {
        a1 = v_r14;
        result = PsWow64GetProcessNtdllType(a1, a2, v_stack_m408, a11);
        a2 = 0;
        a1 = (unsigned int)(result);
        result = PspPrepareSystemDllInitBlock(a1, a2, v_stack_m408, a11);
        v_rdi = (unsigned int)(result);
    }
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_m408, a2, v_stack_m408, a11);
loc_00A16154:
    if (sign_flag) goto loc_00A14CE8;
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(v_stack_m408, a2, v_stack_m408, a11);
    if ((unsigned int)(result) == 0) goto loc_00A1621D;
    v_stack_m848 = v_stack_m708;
    a4 = 0;
    result = SeConstructAntiTamperPolicy(v_stack_m7D0, v_stack_m6D8, v_stack_m670, a4);
    if (sign_flag) goto loc_00A14CE8;
    if (v_stack_m708 == 0) goto loc_00A1621D;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m708))))) == 0) goto loc_00A1621D;
    result = (unsigned int)(*(unsigned int *)(v_stack_m708));
    if (a11 != 0) {
        result = *(unsigned __int64 *)(a11 + 176);
        v_stack_m718 = result;
    }
    result = PsReferencePrimaryTokenWithTag(v_r14, (unsigned int)(0x746C6644ULL), v_stack_m670, a4);
    result = SeSetTokenTamperProtection(v_stack_m7D0, v_stack_m718, v_stack_m708, result);
    if (!sign_flag) goto loc_00A16218;
    result = ObFastDereferenceObject(v_r14 + 584, result, (unsigned int)(0x746C6644ULL), result);
    goto loc_00A14CE8;
loc_00A16218:
    result = ObFastDereferenceObject(v_r14 + 584, result, (unsigned int)(0x746C6644ULL), result);
loc_00A1621D:
    result = PspLockProcessExclusive(v_r14, v_stack_m668, (unsigned int)(0x746C6644ULL), result);
    v_stack_m848 = 0;
    a4 = 0;
    a3 = 0;
    result = ExCreateHandleEx(*(unsigned __int64 *)(v_rip + 5966449), v_r14, a3, a4);
    v_stack_m758 = result;
    if (result != 0) goto loc_00A1626F;
    result = PspUnlockProcessExclusive(v_r14, v_stack_m668, a3, a4);
    goto loc_00A14CE8;
loc_00A1626F:
    if (condition_is_above_or_equal) goto loc_00A162FA;
    a2 = 0;
    a1 = 0;
    result = MmGetSectionStrongImageReference(a1, a2, *(unsigned __int64 *)(v_r14 + 680), v_stack_m660);
    if (!sign_flag) goto loc_00A162A7;
loc_00A1629A:
    result = PspUnlockProcessExclusive(v_r14, v_stack_m668, *(unsigned __int64 *)(v_r14 + 680), v_stack_m660);
    goto loc_00A14CE8;
loc_00A162A7:
    v_stack_m838 = (unsigned int)(*(unsigned int *)(a11 + 376));
    v_stack_m840 = *(unsigned __int64 *)(a11 + 360);
    v_stack_m848 = v_stack_m660;
    result = KeSecureProcess(v_r14, *(unsigned __int64 *)(v_r14 + 736), v_stack_m758, *(unsigned __int64 *)(a11 + 192));
    if (!sign_flag) goto loc_00A162F2;
    goto loc_00A1629A;
loc_00A162F2:
loc_00A162FA:
    result = KeQuerySystemTimeUnsafe(v_r14, *(unsigned __int64 *)(v_r14 + 736), v_stack_m758, *(unsigned __int64 *)(a11 + 192));
    if (result == 0) goto loc_00A16312;
    result = KeQuerySystemTimePrecise(v_r14 + 504, *(unsigned __int64 *)(v_r14 + 736), v_stack_m758, *(unsigned __int64 *)(a11 + 192));
    goto loc_00A1632B;
loc_00A16312:
    *(unsigned __int64 *)(v_stack_m7C8 + 504) = result;
loc_00A1632B:
    *(unsigned __int64 *)(v_stack_m7C8 + 464) = v_stack_m758;
    *(unsigned __int64 *)(v_stack_m7C8 + 1664) = result;
    result = KiQueryUnbiasedInterruptTime(1, *(unsigned __int64 *)(v_r14 + 736), v_stack_m758, *(unsigned __int64 *)(a11 + 192));
    *(unsigned __int64 *)(v_stack_m7C8 + 1672) = result;
    *(unsigned __int64 *)(v_stack_m7C8 + 1688) = *(unsigned __int64 *)(v_stack_m7C8 + 1664);
    *(unsigned __int64 *)(v_stack_m630) = v_stack_m7C8;
    goto loc_00A14D13;
loc_00A1637F:
loc_00A16384:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(v_r14 + 736), v_stack_m758, *(unsigned __int64 *)(a11 + 192));
    v_rsp = (v_rsp) + (0x830ULL);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PspAllocateProcess(void *Arg1, int32_t Arg2, int64_t Arg3, uint8_t Arg4, uint8_t Arg5, uint8_t Arg6, int64_t Arg7, int64_t Arg8, uint8_t Arg9, uint8_t Arg10, int64_t Arg11, uint32_t Arg12, int64_t Arg13, int64_t Arg14, int64_t Arg15)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m3D0;
    uint16_t v_stack_m3D6;
    uint64_t v_stack_m3D8;
    uint64_t v_stack_m3E8;
    uint64_t v_stack_m3F8;
    uint64_t v_stack_m408;
    uint64_t v_stack_m410;
    uint64_t v_stack_m418;
    uint64_t v_stack_m420;
    uint32_t v_stack_m42C;
    uint64_t v_stack_m430;
    uint64_t v_stack_m438;
    uint64_t v_stack_m440;
    uint64_t v_stack_m450;
    uint64_t v_stack_m458;
    uint64_t v_stack_m460;
    uint64_t v_stack_m468;
    uint32_t v_stack_m478;
    uint64_t v_stack_m48;
    uint8_t v_stack_m485;
    uint16_t v_stack_m48A;
    uint16_t v_stack_m492;
    uint16_t v_stack_m494;
    uint64_t v_stack_m4B8;
    uint64_t v_stack_m4C8;
    uint64_t v_stack_m4D8;
    uint64_t v_stack_m4E8;
    uint64_t v_stack_m4F8;
    uint64_t v_stack_m508;
    uint64_t v_stack_m518;
    uint64_t v_stack_m528;
    uint64_t v_stack_m538;
    uint64_t v_stack_m548;
    uint64_t v_stack_m558;
    uint64_t v_stack_m568;
    uint64_t v_stack_m578;
    uint64_t v_stack_m588;
    uint64_t v_stack_m598;
    uint64_t v_stack_m5A8;
    uint64_t v_stack_m5B8;
    uint32_t v_stack_m5C0;
    uint64_t v_stack_m5C8;
    uint32_t v_stack_m5D0;
    uint64_t v_stack_m5D8;
    uint64_t v_stack_m5E0;
    uint64_t v_stack_m5E8;
    uint32_t v_stack_m5F0;
    uint64_t v_stack_m5F8;
    uint32_t v_stack_m600;
    uint64_t v_stack_m608;
    uint64_t v_stack_m610;
    uint64_t v_stack_m618;
    uint16_t v_stack_m620;
    uint64_t v_stack_m628;
    uint64_t v_stack_m630;
    uint64_t v_stack_m638;
    uint64_t v_stack_m640;
    uint64_t v_stack_m648;
    uint64_t v_stack_m658;
    uint64_t v_stack_m660;
    uint64_t v_stack_m668;
    uint64_t v_stack_m670;
    uint64_t v_stack_m678;
    uint64_t v_stack_m680;
    uint64_t v_stack_m698;
    uint64_t v_stack_m6A0;
    uint64_t v_stack_m6A8;
    uint64_t v_stack_m6B0;
    uint64_t v_stack_m6B8;
    uint8_t v_stack_m6BD;
    uint64_t v_stack_m6C0;
    uint64_t v_stack_m6C8;
    uint64_t v_stack_m6D0;
    uint64_t v_stack_m6D8;
    uint64_t v_stack_m6E0;
    uint64_t v_stack_m6E8;
    uint64_t v_stack_m6F0;
    uint32_t v_stack_m6F8;
    uint32_t v_stack_m6FC;
    uint32_t v_stack_m700;
    uint64_t v_stack_m708;
    uint32_t v_stack_m70C;
    uint8_t v_stack_m70D;
    uint32_t v_stack_m710;
    uint64_t v_stack_m718;
    uint64_t v_stack_m720;
    uint64_t v_stack_m728;
    uint32_t v_stack_m72C;
    uint32_t v_stack_m730;
    uint32_t v_stack_m734;
    uint32_t v_stack_m738;
    uint64_t v_stack_m740;
    uint32_t v_stack_m744;
    uint32_t v_stack_m748;
    uint32_t v_stack_m74C;
    uint32_t v_stack_m750;
    uint64_t v_stack_m758;
    uint64_t v_stack_m760;
    uint64_t v_stack_m768;
    uint32_t v_stack_m770;
    uint32_t v_stack_m774;
    uint16_t v_stack_m778;
    uint64_t v_stack_m780;
    uint32_t v_stack_m784;
    uint32_t v_stack_m788;
    uint32_t v_stack_m78C;
    uint32_t v_stack_m790;
    uint32_t v_stack_m794;
    uint8_t v_stack_m795;
    uint8_t v_stack_m796;
    uint32_t v_stack_m798;
    uint32_t v_stack_m79C;
    uint32_t v_stack_m7A0;
    uint32_t v_stack_m7A4;
    uint16_t v_stack_m7A8;
    uint64_t v_stack_m7B0;
    uint32_t v_stack_m7B4;
    uint32_t v_stack_m7B8;
    uint32_t v_stack_m7BC;
    uint16_t v_stack_m7C0;
    uint64_t v_stack_m7C8;
    uint64_t v_stack_m7D0;
    uint8_t v_stack_m7D3;
    uint8_t v_stack_m7D4;
    uint32_t v_stack_m7D8;
    uint16_t v_stack_m7DC;
    uint8_t v_stack_m7E0;
    uint32_t v_stack_m7E4;
    uint8_t v_stack_m7E8;
    uint64_t v_stack_m7F8;
    uint64_t v_stack_m800;
    uint64_t v_stack_m808;
    uint32_t v_stack_m810;
    uint64_t v_stack_m818;
    uint64_t v_stack_m820;
    uint64_t v_stack_m828;
    uint32_t v_stack_m830;
    uint32_t v_stack_m838;
    uint32_t v_stack_m840;
    uint32_t v_stack_m848;
    uint64_t v_stack_m88;
    uint32_t v_stack_mA8;
    uint32_t v_stack_mBC;
    uint32_t v_stack_p48;

    local_rsp = (local_rsp) - (0x830ULL);
    result = (*(uint64_t *)(v_rip + 0x3F6BE8)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m740 = Arg3;
    v_stack_m7E8 = (uint8_t)(Arg2);
    v_stack_m7D0 = Arg1;
    v_stack_m680 = Arg1;
    v_stack_m760 = Arg7;
    v_stack_m768 = Arg8;
    v_stack_m678 = Arg11;
    v_stack_m720 = Arg13;
    v_stack_m648 = Arg14;
    v_stack_m630 = Arg15;
    local_rsi = 0;
    v_stack_m6FC = 0;
    v_stack_m408 = v_xmm0;
    v_stack_m3F8 = v_xmm0;
    v_stack_m3E8 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x438) = 0;
    result = 0;
    v_stack_mBC = 0;
    v_stack_m618 = v_xmm0;
    v_stack_m608 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x5F8) = 0;
    v_stack_m5F0 = 0;
    v_stack_m72C = 0;
    v_stack_m658 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x6F0) = 0;
    Arg2 = 0;
    result = memset(local_rsp - 976, Arg2, 256, Arg4);
    v_stack_m7E4 = 0;
    v_stack_m788 = 0;
    v_stack_m798 = 0;
    result = 0;
    v_stack_m468 = v_xmm0;
    v_stack_m458 = 0;
    v_stack_m450 = v_xmm1;
    v_stack_m440 = 0;
    v_stack_m7D3 = 0;
    v_stack_m5E8 = v_xmm0;
    v_stack_m5D8 = v_xmm0;
    v_stack_m5C8 = 0;
    v_stack_m5C0 = 0;
    v_stack_m6E8 = 0;
    v_stack_m7C8 = 0;
    v_stack_m7D4 = 0;
    v_stack_m7A8 = 0;
    v_stack_m7BC = 0;
    Arg2 = 0;
    result = memset(v_stack_m4B8, Arg2, local_rsi + 72, Arg4);
    v_stack_m784 = 0;
    v_stack_m660 = 0;
    v_stack_m668 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m780 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8);
    v_stack_m708 = 0;
    v_stack_m7B0 = 0;
    v_stack_m6D8 = 0;
    v_stack_m670 = 0;
    v_stack_m718 = 0;
    v_stack_m6C8 = 0;
    v_stack_m7A4 = 0;
    v_stack_m7B8 = 0;
    v_stack_m7B4 = 0;
    v_stack_m78C = 0;
    v_stack_m790 = 0;
    v_stack_m79C = 0x8664ULL;
    v_stack_m750 = 0;
    v_stack_m744 = 0;
    v_stack_m748 = 0;
    v_stack_m794 = 0;
    v_stack_m6A0 = 0;
    v_stack_m74C = 0;
    v_stack_m6A8 = 0;
    v_stack_m7C0 = 0;
    v_stack_m758 = 0;
    v_stack_m6B0 = 0;
    Arg2 = 0;
    result = memset(v_stack_m2C8, Arg2, 536, Arg4);
    v_stack_m7D8 = (uint32_t)((uint32_t)(Arg9));
    if (condition_is_above_or_equal) goto loc_00A13E33;
    v_stack_m7E4 = (uint32_t)(local_rsi + 2);
    if (condition_is_above_or_equal) goto loc_00A13E55;
    v_stack_m7E4 = (uint32_t)(local_rsi + 6);
    if (condition_is_above_or_equal) goto loc_00A13E5B;
    goto loc_00A13E4C;
loc_00A13E33:
    if (local_rsi + 1 != 0) goto loc_00A13E55;
    result = -(Arg1);
    local_rbx = (uint32_t)((local_rsi + 14) & (3));
    local_rbx = (uint32_t)((local_rbx) + (1));
loc_00A13E4C:
    v_stack_m7E4 = (uint32_t)(local_rbx);
    goto loc_00A13E5B;
loc_00A13E55:
loc_00A13E5B:
    if ((((uint8_t)(local_rbx)) & (4)) == 0) goto loc_00A13E89;
    if (Arg12 == 0) goto loc_00A13E72;
    if ((((uint8_t)(local_rbx)) & (2)) == 0) goto loc_00A1637F;
loc_00A13E72:
    if (((*(uint32_t *)(arg1 + 0x5FC)) & (0x1000ULL)) == 0) goto loc_00A13E93;
    goto loc_00A16384;
loc_00A13E89:
    if (condition_is_below) goto loc_00A1637F;
loc_00A13E93:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg9)))) & (256));
    result = (uint32_t)(-(result));
    Arg1 = ((uint32_t)(Arg9)) & (Arg1);
    v_stack_m728 = Arg1;
    if (Arg11 == 0) goto loc_00A13EE6;
    if (condition_is_above_or_equal) goto loc_00A13EE6;
    if (Arg1 != NULL) goto loc_00A1637F;
    v_stack_m7B0 = *(uint64_t *)(v_rip + 0x5BB7F0 + *(uint16_t *)(Arg11 + 0xAA) * 8);
    v_stack_m728 = Arg1;
    goto loc_00A13F13;
loc_00A13EE6:
    if (Arg1 == NULL) goto loc_00A13F13;
    v_stack_m728 = Arg1;
    if (((*(uint32_t *)(arg1 + 0x1F0)) & (0x200000ULL)) != 0) {
        v_stack_m728 = Arg1;
        v_stack_m7B4 = 0x200000ULL;
    }
    if (Arg11 == 0) goto loc_00A13F33;
    if (!(condition_is_above_or_equal)) {
        v_stack_m7E4 = (uint32_t)(local_rbx);
    }
    result = 0;
    v_stack_m430 = v_xmm0;
    v_stack_m420 = v_xmm0;
    v_stack_m410 = 0;
    v_stack_m6D0 = 0;
    v_stack_m738 = 0;
    v_stack_m698 = 0;
    if ((*(uint32_t *)(v_rip + 0x5B2EBC)) == 0) {
        Arg1 = (uint32_t)(0x840ULL) + 40;
        v_stack_m7E4 = (uint32_t)(local_rbx);
        v_stack_m698 = (uint32_t)(0x840ULL);
    }
    result = (uint32_t)((Arg1 + 7) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    v_stack_m6F8 = (uint32_t)(result);
    result = PoEnergyEstimationEnabled(Arg1, (uint32_t)(0x840ULL), 536, Arg4);
    local_r14 = result + 16;
    if ((uint8_t)(result) != 0) {
        result = result + 16 + 7;
        result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
        v_stack_m738 = (uint32_t)(result);
        local_r14 = result + 488;
        v_stack_m7E4 = (uint32_t)(local_rbx);
    }
    result = KeQueryMaximumGroupCount(Arg1, (uint32_t)(0x840ULL), 536, Arg4);
    v_stack_m778 = (uint16_t)(result);
    local_r13 = 0;
    if (((uint16_t)(result)) >= = 1) {
        local_r14 = (uint32_t)((local_r14) + (7));
        local_r14 = (uint32_t)((local_r14) & (0xFFFFFFF8ULL));
        local_r13 = (uint32_t)(local_r14);
        Arg1 = (uint16_t)(result);
        Arg1 = (uint32_t)((Arg1) << (4));
        local_r14 = (uint32_t)((local_r14) + ((uint32_t)(Arg1)));
    }
    v_stack_m770 = 0;
    if ((((uint32_t)(local_rbx)) & (0x10002ULL)) == 0) {
        result = 4;
        Arg1 = 0;
        if (v_stack_m7D0 != 0) { Arg1 = (uint32_t)(result); }
        v_stack_m770 = (uint32_t)(Arg1);
    }
    local_r12 = (uint32_t)((local_r14 + 7) & (0xFFFFFFF8ULL));
    result = KeSizeOfKProcessExtension(Arg1, (uint32_t)(0x840ULL), 536, Arg4);
    v_stack_m700 = (uint32_t)(local_r12);
    local_r12 = (uint32_t)((local_r12) + ((uint32_t)(result)));
    v_stack_m820 = 0;
    v_stack_m828 = v_stack_m7C8;
    v_stack_m830 = (uint32_t)(local_r12);
    v_stack_m838 = 0;
    v_stack_m840 = (uint32_t)(local_r12);
    result = ObCreateObjectEx((uint8_t)(v_stack_m7E8), *(uint64_t *)(v_rip + 0x5B2A5B), v_stack_m740, v_stack_m7E8);
    if (sign_flag) goto loc_00A16384;
    result = ObRetagReferences(v_stack_m7C8, *(uint64_t *)(v_rip + 0x5B2A5B), (uint32_t)(0x72437350ULL), v_stack_m7E8);
    Arg2 = 0;
    result = memset(v_stack_m7C8, Arg2, (uint32_t)((uint32_t)(local_r12)), v_stack_m7E8);
    *(uint64_t *)(v_stack_m7C8 + 0x580) = v_xmm0;
    *(uint64_t *)(v_stack_m7C8 + 0x590) = v_xmm0;
    *(uint64_t *)(v_stack_m7C8 + 0x580) = 0;
    *(uint64_t *)(v_stack_m7C8 + 0x588 + 0x8) = v_stack_m7C8 + 1416;
    *(uint64_t *)(v_stack_m7C8 + 0x588) = v_stack_m7C8 + 1416;
    *(uint64_t *)(v_stack_m7C8 + 0x1E8) = 0;
    *(uint64_t *)(v_stack_m7C8 + 0x1C8) = 0;
    *(uint64_t *)(v_stack_m7C8 + 0x370 + 0x8) = v_stack_m7C8 + 880;
    *(uint64_t *)(v_stack_m7C8 + 0x370) = v_stack_m7C8 + 880;
    *(uint64_t *)(v_stack_m7C8 + 0x620 + 0x8) = v_stack_m7C8 + 1568;
    *(uint64_t *)(v_stack_m7C8 + 0x620) = v_stack_m7C8 + 1568;
    *(uint64_t *)(v_stack_m7C8 + 0x710 + 0x8) = v_stack_m7C8 + 1808;
    *(uint64_t *)(v_stack_m7C8 + 0x710) = v_stack_m7C8 + 1808;
    *(uint8_t *)(v_stack_m7C8 + 0x5FA) = Arg4;
    *(uint8_t *)(v_stack_m7C8 + 0x5F8) = Arg5;
    *(uint8_t *)(v_stack_m7C8 + 0x5F9) = Arg6;
    *(uint64_t *)(v_stack_m7C8 + 0x828) = 1;
    *(uint64_t *)(v_stack_m7C8 + 0x658) = 0;
    *(uint64_t *)(v_stack_m7C8 + 0x788) = 0;
    *(uint64_t *)(v_stack_m7C8 + 0x780) = 0;
    *(uint64_t *)(v_stack_m7C8 + 0x798) = 0;
    *(uint64_t *)(v_stack_m7C8 + 0x790) = 0;
    *(uint64_t *)(v_stack_m7C8 + 0x7A8) = 0;
    *(uint64_t *)(v_stack_m7C8 + 0x818) = 0;
    if ((((uint8_t)(local_rbx)) & (2)) != 0) {
    }
    if (condition_is_above_or_equal) goto loc_00A14190;
    v_stack_m740 = 32;
    goto loc_00A1419B;
loc_00A14190:
    v_stack_m740 = 32;
loc_00A1419B:
    local_r14 = v_stack_m7C8;
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg9;
        v_stack_m7D8 = (uint32_t)(Arg3);
        local_r14 = v_stack_m7C8;
    }
    result = 32;
    if ((uint32_t)(local_r13) != 0) {
        Arg1 = (uint32_t)(local_r13);
        Arg1 = (Arg1) + (local_r14);
        *(void **)(local_r14 + 0x6C8) = Arg1;
        result = v_stack_m778;
        Arg1 = Arg1 + result * 8;
        *(void **)(local_r14 + 0x6D0) = Arg1;
    }
    if (((1) & ((uint8_t)((uint32_t)(Arg10)))) != 0) {
    }
    if (((4) & ((uint8_t)((uint32_t)(Arg10)))) != 0) {
    }
    if ((((uint8_t)((uint32_t)(Arg10))) & (8)) != 0) {
    }
    if ((((uint8_t)((uint32_t)(Arg10))) & (16)) != 0) {
    }
    result = (*(uint64_t *)(v_stack_m780 + 0x1D0)) | (2);
    if (condition_is_below) { result = *(uint64_t *)(v_stack_m780 + 0x1D0); }
    *(uint64_t *)(local_r14 + 0x2D8) = result;
    if (!(condition_is_above_or_equal)) {
        result = v_stack_m698;
        result = (result) + (local_r14);
        *(uint64_t *)(local_r14 + 0x638) = result;
    }
    result = ((uint32_t)(v_stack_m6F8)) + (local_r14);
    *(uint64_t *)(local_r14 + 0x7F0) = result;
    if (!(condition_is_above_or_equal)) {
        Arg1 = v_stack_m738;
        Arg1 = (Arg1) + (local_r14);
        *(void **)(local_r14 + 0x668) = Arg1;
        result = PoEnergyContextInitialize(Arg1, *(uint64_t *)(v_stack_m780 + 0x1D0), Arg3, v_stack_m7E8);
    }
    if (Arg11 == 0) goto loc_00A142C4;
    if (condition_is_above_or_equal) goto loc_00A142C4;
    goto loc_00A142E0;
loc_00A142C4:
    if (v_stack_m7D0 == 0) goto loc_00A142DB;
    goto loc_00A142E0;
loc_00A142DB:
loc_00A142E0:
    *(uint32_t *)(local_r14 + 0x388) = 5;
    *(uint32_t *)(local_r14 + 0x554) = 259;
    if (v_stack_m7D0 == 0) goto loc_00A14326;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m7D0 + 0x1F4))) >> (27));
    Arg2 = (uint32_t)((Arg2) & (7));
    Arg3 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m7D0 + 0x1F0))) >> (12));
    Arg3 = (uint32_t)((Arg3) & (7));
    *(uint64_t *)(local_r14 + 0x2D0) = *(uint64_t *)(v_stack_m7D0 + 0x1D0);
    goto loc_00A14333;
loc_00A14326:
    result = KeQueryHeteroCpuPolicyThread(Arg1, 2, Arg3, v_stack_m7E8);
loc_00A14333:
    Arg2 = (uint32_t)((2) << (27));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x1F4))) & (0xC7FFFFFFULL));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(Arg1)));
    *(uint32_t *)(local_r14 + 0x1F4) = Arg2;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_r14 + 0x1F0))) & (0xFFFF8FFFULL));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(result))) << (12));
    Arg1 = (uint32_t)((Arg1) | ((uint32_t)(Arg3)));
    *(uint32_t *)(local_r14 + 0x1F0) = (uint32_t)(Arg1);
    if (v_stack_m720 == 0) goto loc_00A1438A;
    result = PsReferencePartitionSafe(v_stack_m720, Arg2, Arg3, v_stack_m7E8);
    if ((uint8_t)(result) != 0) goto loc_00A143C9;
    goto loc_00A14CE8;
loc_00A1438A:
    v_stack_m720 = *(uint64_t *)(v_rip + 0x5B2B0F);
    result = (1) + (1);
    if (result <= 1) {
        Arg1 = 14;
    }
    v_stack_m7D8 = (uint32_t)((uint32_t)(Arg9));
    goto loc_00A143D1;
loc_00A143C9:
loc_00A143D1:
    *(uint64_t *)(v_stack_m7C8 + 0x758) = v_stack_m720;
    result = (uint32_t)(Arg9);
    if (v_stack_m760 != 0) {
        result = ObfReferenceObject(v_stack_m760, v_stack_m720, Arg3, v_stack_m7E8);
        Arg1 = v_stack_m760;
    }
    if ((((uint8_t)((uint32_t)(0xC00004A0ULL))) & ((uint8_t)(local_rbx))) == 0) goto loc_00A144A3;
    v_stack_m79C = (uint32_t)(*(uint16_t *)(v_stack_m7D0 + 0x6EC));
    if ((((uint8_t)(local_rbx)) & (2)) != 0) goto loc_00A144A3;
    result = ExAcquireRundownProtection(v_stack_m7D0 + 488, v_stack_m720, Arg3, v_stack_m7E8);
    if ((uint8_t)(result) == 0) goto loc_00A1444D;
    v_stack_m760 = *(uint64_t *)(v_stack_m7D0 + 0x2A8);
    result = *(uint64_t *)(v_stack_m7D0 + 0x2A8);
    if (*(uint64_t *)(v_stack_m7D0 + 0x2A8) != 0) {
        Arg1 = *(uint64_t *)(v_stack_m7D0 + 0x2A8);
        result = ObfReferenceObject(Arg1, v_stack_m720, Arg3, v_stack_m7E8);
    }
    result = ExReleaseRundownProtection(v_stack_m7D0 + 488, v_stack_m720, Arg3, v_stack_m7E8);
loc_00A1444D:
    if (v_stack_m760 != 0) goto loc_00A14464;
    goto loc_00A14CE8;
loc_00A14464:
    result = *(uint64_t *)(v_stack_m7D0 + 0x310);
    if (*(uint64_t *)(v_stack_m7D0 + 0x310) != 0) {
        local_rbx = (uint32_t)((local_rbx) | (64));
        v_stack_m7E4 = (uint32_t)(local_rbx);
        result = *(uint32_t *)(*(uint64_t *)(v_stack_m7D0 + 0x310) + 0x8);
        v_stack_m750 = (uint32_t)(result);
    }
    result = 0;
    if (((*(uint32_t *)(v_stack_m7D0 + 0x1F4)) & ((uint32_t)((uint32_t)(0x20000ULL)))) != 0) { result = (uint32_t)((uint32_t)(0x20000ULL)); }
    v_stack_m7B8 = (uint32_t)(result);
loc_00A144A3:
    *(uint64_t *)(v_stack_m7C8 + 0x2A8) = v_stack_m760;
    if (Arg11 == 0) goto loc_00A14A39;
    if ((((uint8_t)(local_rbx)) & (2)) != 0) goto loc_00A14A39;
    *(uint64_t *)(v_stack_m7C8 + 0x5F0) = *(uint64_t *)(Arg11 + 0x1A8);
    result = MmGetSectionInformation(v_stack_m760, 4, Arg11 + 56, v_stack_m7E8);
    if (sign_flag) goto loc_00A14CE8;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg11 + 0x78))))) & (250));
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)(local_rbx)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg11 + 0x78))) & (1));
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(result)));
    local_rbx = (uint32_t)((local_rbx) << (5));
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(Arg11 + 0x6B)))) & (2));
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(result)));
    local_rbx = (uint32_t)((local_rbx) << (2));
    Arg1 = (uint32_t)((*(uint8_t *)(Arg11 + 0x6B)) & (4));
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)(Arg1)));
    local_rbx = (uint32_t)((local_rbx) << (11));
    local_rbx = (uint32_t)((local_rbx) | ((uint32_t)((uint32_t)((uint32_t)(local_rbx)))));
    v_stack_m7E4 = (uint32_t)(local_rbx);
    v_stack_m78C = (uint32_t)(*(uint16_t *)(Arg11 + 0x5E));
    v_stack_m790 = (uint32_t)(*(uint16_t *)(Arg11 + 0x5C));
    if (((*(uint16_t *)(Arg11 + 0x12)) & ((uint16_t)(*(uint16_t *)(Arg11 + 0x64)))) == 0) goto loc_00A14557;
loc_00A14547:
    Arg3 = 0;
    result = PspUpdateCreateInfo(3, Arg11, Arg3, v_stack_m7E8);
    goto loc_00A14CE8;
loc_00A14557:
    if (((4) & ((uint8_t)(local_rbx))) != 0) goto loc_00A14AEC;
    result = ObfReferenceObjectWithTag(*(uint64_t *)(Arg11 + 0xB8), (uint32_t)(0x72437350ULL), Arg3, v_stack_m7E8);
    *(uint64_t *)(v_stack_m7C8 + 0x330) = *(uint64_t *)(Arg11 + 0xB8);
    v_stack_m7C0 = (uint16_t)(*(uint16_t *)(Arg11 + 0x66));
    result = RtlpOpenImageFileOptionsKeyEx(Arg11 + 240, (uint32_t)(0x72437350ULL), Arg3, Arg11 + 200);
    if (!sign_flag) goto loc_00A145BB;
    if (((uint32_t)(result)) == 0xC0000034ULL) {
    }
    *(uint64_t *)(Arg11 + 0xC8) = 0;
loc_00A145BB:
    result = PspSelectMachineForProcess(v_stack_m7D0, Arg11, v_stack_m798, Arg11 + 200);
    if (!sign_flag) goto loc_00A145E1;
    goto loc_00A14547;
loc_00A145E1:
    v_stack_m79C = (uint32_t)(v_stack_m798);
    if (v_stack_m796 != 0) {
        local_rbx = (uint32_t)((local_rbx) | (64));
        v_stack_m7E4 = (uint32_t)(local_rbx);
    }
    if (v_stack_m795 != 0) {
    }
    if (*(uint64_t *)(Arg11 + 0xC8) == 0) goto loc_00A14AEC;
    if ((*(uint8_t *)(Arg11 + 0x10)) < 0) goto loc_00A146C8;
    v_stack_m840 = v_stack_m7BC;
    v_stack_m848 = 2;
    result = RtlQueryImageFileKeyOption(*(uint64_t *)(Arg11 + 0xC8), v_rip + 985128, 1, v_stack_m7A8);
    if (((uint32_t)(result)) == 0x80000005ULL) goto loc_00A146B9;
    if (sign_flag) goto loc_00A1467C;
    if (v_stack_m7BC != 2) goto loc_00A1467C;
    if (v_stack_m7A8 != 0) goto loc_00A146B9;
loc_00A1467C:
    v_stack_m734 = 0;
    v_stack_m840 = 0;
    v_stack_m848 = 4;
    result = RtlQueryImageFileKeyOption(*(uint64_t *)(Arg11 + 0xC8), v_rip + 984993, 4, v_stack_m734);
    if (sign_flag) goto loc_00A146C8;
    if (v_stack_m734 != 1) goto loc_00A146C8;
loc_00A146B9:
    goto loc_00A14547;
loc_00A146C8:
    v_stack_m7A0 = 0;
    v_stack_m840 = 0;
    v_stack_m848 = 4;
    result = RtlQueryImageFileKeyOption(*(uint64_t *)(Arg11 + 0xC8), v_rip + 985125, 4, v_stack_m7A0);
    if (sign_flag) goto loc_00A147F3;
    if (v_stack_m7A0 == 0) goto loc_00A147F3;
    local_r12 = (uint32_t)(((uint32_t)(v_stack_m7D8)) | (16));
    v_stack_m7D8 = (uint32_t)(local_r12);
    v_stack_p48 = (uint32_t)(local_r12);
    if ((((uint8_t)(local_rbx)) & (64)) != 0) goto loc_00A147F3;
    v_stack_m618 = 48;
    v_stack_m610 = *(uint64_t *)(Arg11 + 0xC8);
    v_stack_m600 = 576;
    v_stack_m608 = v_rip + 1275659;
    v_stack_m5F8 = v_xmm0;
    result = ZwOpenKey(v_stack_m6F0, 1, v_stack_m618, v_stack_m7A0);
    if (sign_flag) goto loc_00A147F8;
    v_stack_m7A0 = 0;
    v_stack_m840 = 0;
    v_stack_m848 = 4;
    result = RtlQueryImageFileKeyOption(v_stack_m6F0, v_rip + 984892, 4, v_stack_m7A0);
    if (sign_flag) goto loc_00A147E2;
    if (v_stack_m7A0 != 0) {
        local_r12 = (uint32_t)((local_r12) | (32));
        v_stack_m7D8 = (uint32_t)(local_r12);
        v_stack_p48 = (uint32_t)(local_r12);
    }
    Arg2 = 0;
    result = ObCloseHandle(v_stack_m6F0, Arg2, 4, v_stack_m7A0);
    goto loc_00A147F8;
loc_00A147F3:
loc_00A147F8:
    if (v_stack_m728 == 0) {
        Arg3 = v_stack_m7B0;
        Arg2 = *(uint64_t *)(Arg11 + 0xC8);
        Arg1 = v_stack_m7C8;
        result = PspReadIFEONodeOptions(Arg1, Arg2, Arg3, v_stack_m7A0);
    }
    v_stack_m730 = 0;
    v_stack_m840 = 0;
    v_stack_m848 = 4;
    result = RtlQueryImageFileKeyOption(*(uint64_t *)(Arg11 + 0xC8), v_rip + 984725, 4, v_stack_m730);
    if (sign_flag) goto loc_00A1485C;
    if (v_stack_m730 != 0) {
    }
    v_stack_m840 = v_stack_m7BC;
    v_stack_m848 = 0;
    Arg4 = 0;
    result = RtlQueryImageFileKeyOption(*(uint64_t *)(Arg11 + 0xC8), v_rip + 984629, Arg4 + 3, Arg4);
    if (((uint32_t)(result)) != 0x80000005ULL) goto loc_00A1492F;
    if (((uint32_t)((uint32_t)(v_stack_m7BC))) > 256) goto loc_00A1492F;
    if ((((uint8_t)((uint32_t)(v_stack_m7BC))) & (7)) != 0) goto loc_00A1492F;
    result = ExAllocatePool2(64, (uint32_t)((uint32_t)((uint32_t)(v_stack_m7BC))), (uint32_t)(0x73437350ULL), Arg4);
    v_stack_m6C8 = result;
    if (result != 0) goto loc_00A148D8;
loc_00A148CE:
    goto loc_00A14CE8;
loc_00A148D8:
    v_stack_m840 = v_stack_m7BC;
    v_stack_m848 = (uint32_t)((uint32_t)(0xC0000017ULL));
    result = RtlQueryImageFileKeyOption(*(uint64_t *)(Arg11 + 0xC8), v_rip + 984503, 3, result);
    if (sign_flag) goto loc_00A1492F;
    if (((v_stack_m7BC) & (7)) == 0) {
        v_stack_m7E4 = (uint32_t)(local_rbx);
        result = v_stack_m7BC;
        result = (uint32_t)((result) >> (3));
        v_stack_m7A4 = (uint32_t)(result);
    }
    v_stack_m5E8 = 48;
    v_stack_m5E0 = *(uint64_t *)(Arg11 + 0xC8);
    v_stack_m5D0 = 576;
    v_stack_m5D8 = v_rip + 1275133;
    v_stack_m5C8 = v_xmm0;
    result = ZwOpenKey(v_stack_m6E8, 1, v_stack_m5E8, result);
    if (!(sign_flag)) {
        Arg2 = v_stack_m430;
        Arg1 = v_stack_m6E8;
        result = PspReadIFEOPerfOptions(Arg1, Arg2, v_stack_m5E8, result);
        Arg2 = 0;
        Arg1 = v_stack_m6E8;
        result = ObCloseHandle(Arg1, Arg2, v_stack_m5E8, result);
    }
    v_stack_m840 = 0;
    v_stack_m848 = 4;
    result = RtlQueryImageFileKeyOption(*(uint64_t *)(Arg11 + 0xC8), v_rip + 983905, 4, v_stack_m72C);
    if (sign_flag) goto loc_00A14A09;
    local_r14 = v_stack_m7C8;
    if (v_stack_m72C == 2) {
        local_r12 = Arg9;
        v_stack_m7D8 = (uint32_t)(local_r12);
        local_r14 = v_stack_m7C8;
    }
    if (v_stack_m72C >= 2) goto loc_00A14AF4;
    v_stack_m7D8 = (uint32_t)((uint32_t)(Arg9));
    goto loc_00A14AF4;
loc_00A14A39:
    if (*(uint64_t *)(Arg11 + 0xC8) == 0) goto loc_00A14AEC;
    result = MmGetSectionInformation(*(uint64_t *)(Arg11 + 0xC8), 4, v_stack_m4B8, v_stack_m72C);
    if (sign_flag) goto loc_00A14CE8;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m478)))) & (250));
    Arg2 = (uint32_t)((Arg2) + (Arg2));
    result = (uint32_t)(((uint32_t)(v_stack_m478)) & (1));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(result)));
    Arg2 = (uint32_t)((Arg2) << (5));
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m485))) & (2));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(result)));
    Arg2 = (uint32_t)((Arg2) << (2));
    Arg1 = (uint32_t)((v_stack_m485) & (4));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) << (11));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (0xF82B9FFFULL));
    local_rbx = (uint32_t)(((uint32_t)(Arg2)) | ((uint32_t)(result)));
    v_stack_m7E4 = (uint32_t)(local_rbx);
    v_stack_m7C0 = (uint16_t)(v_stack_m48A);
    v_stack_m78C = (uint32_t)(v_stack_m492);
    v_stack_m790 = (uint32_t)(v_stack_m494);
    if (((4) & ((uint8_t)(local_rbx))) != 0) {
        local_rbx = (uint32_t)((local_rbx) | (24));
        v_stack_m7E4 = (uint32_t)(local_rbx);
    }
loc_00A14AF4:
    if ((((uint8_t)(local_rbx)) & (64)) == 0) goto loc_00A14B82;
    result = ExAllocatePool2(16 + 48, 16, (uint32_t)(0x50776F57ULL), v_stack_m72C);
    *(uint64_t *)(v_stack_m7C8 + 0x310) = result;
    if (result == 0) goto loc_00A148CE;
    result = (uint32_t)(v_stack_m750);
    if ((uint32_t)((uint32_t)(v_stack_m750)) == 0) {
        Arg2 = (uint16_t)((uint32_t)(v_stack_m79C));
        Arg1 = Arg11;
        result = PspWow64PickBestNtdll(Arg1, Arg2, (uint32_t)(0x50776F57ULL), v_stack_m72C);
    }
    *(uint32_t *)(result + 0x8) = (uint32_t)(result);
    if (*(uint64_t *)(v_stack_m7C8 + 0x310) != 0) {
        *(uint64_t *)(*(uint64_t *)(v_stack_m7C8 + 0x310)) = 1;
    }
    if (condition_is_above_or_equal) goto loc_00A14B8A;
    v_stack_m7D8 = (uint32_t)((uint32_t)(Arg9));
    goto loc_00A14B8A;
loc_00A14B82:
loc_00A14B8A:
    *(uint16_t *)(v_stack_m7C8 + 0x6EC) = (uint16_t)((uint32_t)(v_stack_m79C));
    result = SeQueryInformationToken(v_stack_m768, 29, v_stack_m784, v_stack_m72C);
    if (sign_flag) goto loc_00A14CE8;
    if ((uint8_t)(v_stack_m7E8) == 0) goto loc_00A14CAD;
    if (Arg11 == 0) goto loc_00A14BED;
    if (condition_is_above_or_equal) goto loc_00A14BED;
    local_r10 = 0;
    if ((*(uint8_t *)(Arg11 + 0x2)) == 4) {
        v_stack_mA8 = 14;
        local_r10 = 1;
    }
    result = (uint32_t)(*(uint32_t *)(Arg11 + 0x8));
    if ((uint32_t)((uint32_t)(Arg12)) != 0) {
        result = (uint32_t)(local_r10);
        *(uint32_t *)(local_rsp + result * 4 + 0x7C0) = 3;
        local_r10 = (uint32_t)((local_r10) + (1));
    }
    if ((((uint8_t)((uint32_t)(Arg9))) & (48)) != 0) {
        result = (uint32_t)(local_r10);
        *(uint32_t *)(local_rsp + result * 4 + 0x7C0) = 4;
        local_r10 = (uint32_t)((local_r10) + (1));
    }
    if (!sign_flag) goto loc_00A14C4E;
    result = PspIsSessionLeaderProcess(v_stack_m780, 29, v_stack_m784, v_stack_m72C);
    if ((uint32_t)(result) == 0) {
        result = (uint32_t)(local_r10);
        *(uint32_t *)(local_rsp + result * 4 + 0x7C0) = 10;
        local_r10 = (uint32_t)((local_r10) + (1));
    }
    if ((((uint32_t)((uint32_t)(Arg9))) & (0x8400ULL)) != 0) {
        result = (uint32_t)(local_r10);
        *(uint32_t *)(local_rsp + result * 4 + 0x7C0) = 7;
        local_r10 = (uint32_t)((local_r10) + (1));
    }
    if ((uint32_t)(local_r10) == 0) goto loc_00A14CA6;
    Arg3 = ((uint32_t)((uint32_t)(Arg12)) != 0) ? 1 : 0;
    result = RtlAcquirePrivilege(v_stack_mA8, (uint32_t)((uint32_t)(local_r10)), Arg3, v_stack_m6D0);
    if (sign_flag) goto loc_00A14CAD;
    v_stack_m7E4 = (uint32_t)(local_rbx);
    goto loc_00A14CAD;
loc_00A14CA6:
loc_00A14CAD:
    if ((((uint32_t)((uint32_t)(Arg9))) & (0x8400ULL)) == 0) goto loc_00A14D68;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x5C4DB5), (uint8_t)(v_stack_m7E8), Arg3, v_stack_m6D0);
    if ((uint8_t)(result) != 0) goto loc_00A14D68;
loc_00A14CD0:
loc_00A14CD5:
    if (!(condition_is_above_or_equal)) {
        Arg1 = v_stack_m6D0;
        result = RtlReleasePrivilege(Arg1, (uint8_t)(v_stack_m7E8), Arg3, v_stack_m6D0);
    }
    if (v_stack_m758 != 0) {
        *(uint64_t *)(v_stack_m7C8 + 0x1D0) = v_stack_m758;
    }
    Arg2 = 0;
    result = PspRundownSingleProcess(v_stack_m7C8, Arg2, Arg3, v_stack_m6D0);
    result = ObfDereferenceObjectWithTag(v_stack_m7C8, (uint32_t)(0x72437350ULL), Arg3, v_stack_m6D0);
loc_00A14D13:
    result = v_stack_m6C8;
    if (v_stack_m6C8 != 0) {
        Arg2 = 0x73437350ULL;
        Arg1 = v_stack_m6C8;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, v_stack_m6D0);
    }
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, v_stack_m6D0);
    if ((uint32_t)(result) == 0) goto loc_00A14D48;
    if (v_stack_m708 != 0) {
        result = SeFreeAntiTamperPolicy(v_stack_m708, Arg2, Arg3, v_stack_m6D0);
    }
    result = *(uint64_t *)(v_rip + 0x4F01B9);
    if (*(uint64_t *)(v_rip + 0x4F01B9) != 0) {
        Arg1 = v_stack_m2C8;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, v_stack_m6D0);
    }
    goto loc_00A16384;
loc_00A14D68:
    v_stack_m7DC = (uint16_t)((uint32_t)(0xFFFFULL));
    v_stack_m3D8 = 0x200001ULL;
    Arg2 = 0;
    result = memset(v_stack_m3D0, Arg2, 256, v_stack_m6D0);
    if (v_stack_m728 != 0) goto loc_00A14EEB;
    if (v_stack_m7B0 != 0) goto loc_00A14E65;
    if (v_stack_m7D0 == 0) goto loc_00A14E49;
    if (((*(uint32_t *)(v_stack_m7D0 + 0x1F0)) & (0x100000ULL)) == 0) goto loc_00A14DFA;
    v_stack_m7B0 = *(uint64_t *)(v_rip + 0x5BA8D7 + *(uint16_t *)(v_stack_m7D0 + 0x104) * 8);
    goto loc_00A14E6D;
loc_00A14DFA:
    result = PspSelectNodeForProcess(*(uint64_t *)(v_rip + 0x5BA8D7 + *(uint16_t *)(v_stack_m7D0 + 0x104) * 8), Arg2, 256, v_stack_m6D0);
    v_stack_m7B0 = result;
    result = KeSelectGroupFromNode(result, Arg2, 256, v_stack_m6D0);
    v_stack_m7DC = (uint16_t)(result);
    if ((*(uint8_t *)(v_rip + 0x5B1CD1)) == 0) goto loc_00A14E7D;
    result = KeQueryActiveGroupCount(result, Arg2, 256, v_stack_m6D0);
    if (((uint16_t)(result)) <= 1) goto loc_00A14E7D;
    if ((uint16_t)((uint16_t)(result)) != 0) goto loc_00A14E7D;
    v_stack_m7B0 = 0;
    v_stack_m7DC = 1;
    goto loc_00A14E7D;
loc_00A14E49:
    v_stack_m7DC = 0;
    Arg2 = 0;
    result = KeAddProcessorAffinityEx(v_stack_m3D8, Arg2, 256, v_stack_m6D0);
    goto loc_00A14E7D;
loc_00A14E65:
loc_00A14E6D:
    result = KeSelectGroupFromNode(v_stack_m7B0, Arg2, 256, v_stack_m6D0);
    v_stack_m7DC = (uint16_t)(result);
loc_00A14E7D:
    result = KiCopyAffinityEx(v_stack_m3D8, v_stack_m3D6, v_rip + 5972636, v_stack_m6D0);
    if (v_stack_m7B0 != 0) goto loc_00A14F36;
    v_stack_m628 = v_xmm0;
    v_stack_m620 = (uint16_t)((uint16_t)(result));
    if (((uint16_t)((uint16_t)(result))) >= v_stack_m3D8) goto loc_00A14ED1;
    goto loc_00A14ED4;
loc_00A14ED1:
loc_00A14ED4:
    v_stack_m628 = 0;
    result = KeSelectNodeForAffinity(v_stack_m628, v_stack_m3D6, v_rip + 5972636, v_stack_m6D0);
    goto loc_00A14F2E;
loc_00A14EEB:
    v_stack_m848 = v_stack_m7DC;
    Arg3 = 0;
    result = KeQueryAffinityProcess(result, v_stack_m3D8, Arg3, v_stack_m88);
loc_00A14F2E:
    v_stack_m7B0 = *(uint64_t *)(v_rip + 0x5BA796 + *(uint16_t *)(local_rsp + v_stack_m7DC * 2 + 0x7E0) * 8);
loc_00A14F36:
    if (v_stack_m7D0 == 0) goto loc_00A151C3;
    v_stack_m6E0 = 0;
    v_stack_m774 = 0;
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFDFULL));
    v_stack_m7E0 = 0;
    if (Arg12 == 0) goto loc_00A15079;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x5C4C2B), v_stack_m7E8, Arg3, v_stack_m88);
    if ((uint8_t)(result) == 0) { local_rbx = (uint32_t)((uint32_t)((uint32_t)(local_rbx))); }
    result = SeIsTokenAssignableToProcess(v_stack_m768, v_stack_m7E0, Arg3, v_stack_m88);
    if (sign_flag) goto loc_00A14CD5;
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (9));
    if (v_stack_m7E0 != 0) goto loc_00A14FEB;
    if ((((uint8_t)(local_r13)) & (1)) == 0) goto loc_00A14CD0;
loc_00A14FEB:
    result = SeQuerySessionIdToken(v_stack_m768, v_stack_m774, Arg3, v_stack_m88);
    if (sign_flag) goto loc_00A14CD5;
    result = PsGetProcessSessionIdEx(v_stack_m780, v_stack_m774, Arg3, v_stack_m88);
    if (((uint32_t)((uint32_t)(v_stack_m774))) == ((uint32_t)(result))) goto loc_00A15043;
    if ((((uint8_t)(local_r13)) & (1)) == 0) goto loc_00A14CD0;
    if (((v_stack_m7D8) & (128)) == 0) goto loc_00A15040;
    goto loc_00A14CD5;
loc_00A15040:
    local_rbx = (uint32_t)((local_rbx) | (32));
loc_00A15043:
loc_00A1504B:
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (32));
    if (condition_is_equal) goto loc_00A150BB;
    result = PspAttachSession((uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))), v_stack_m408, v_stack_m6E0, v_stack_m88);
    if (!sign_flag) goto loc_00A150B2;
    local_rbx = (uint32_t)((local_rbx) & (0xFFFFFFDFULL));
    goto loc_00A14CD5;
loc_00A15079:
    if ((((uint8_t)(local_rbx)) & (4)) == 0) goto loc_00A1504B;
    result = PsGetProcessSessionIdEx(local_r12, v_stack_m408, v_stack_m6E0, v_stack_m88);
    v_stack_m774 = (uint32_t)(result);
    result = PsGetProcessSessionIdEx(v_stack_m780, v_stack_m408, v_stack_m6E0, v_stack_m88);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))))) - ((uint32_t)(result)));
    Arg1 = (uint32_t)(-(Arg1));
    Arg2 = (uint32_t)((v_stack_m408) & (32));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (0xFFFFFFDFULL));
    local_rbx = (uint32_t)(((uint32_t)(Arg2)) | ((uint32_t)(result)));
    goto loc_00A1504B;
loc_00A150B2:
loc_00A150BB:
    if (Arg12 == 0) goto loc_00A15104;
    if ((uint8_t)(v_stack_m7E0) != 0) goto loc_00A15104;
    Arg1 = 0;
    result = PspAssignProcessQuotaBlock(Arg1, v_stack_m7C8, v_stack_m768, v_stack_m88);
    if (!sign_flag) goto loc_00A15125;
    if ((uint32_t)(local_r12) == 0) goto loc_00A14CD5;
    result = PspDetachSession(v_stack_m6E0, v_stack_m408, v_stack_m768, v_stack_m88);
    goto loc_00A14CD5;
loc_00A15104:
    Arg2 = v_stack_m7D0;
    if ((uint8_t)(v_stack_m7E0) != 0) { Arg2 = v_stack_m780; }
    result = PspInheritQuota(v_stack_m7C8, Arg2, v_stack_m768, v_stack_m88);
    goto loc_00A1512D;
loc_00A15125:
loc_00A1512D:
    Arg4 = (uint32_t)(((uint32_t)(v_stack_m42C)) & (1));
    Arg3 = *(uint64_t *)(v_rip + 0x5C3103);
    if (condition_is_not_equal) { Arg3 = v_stack_m418; }
    if (((v_stack_m7D8) & (0x400000ULL)) != 0) {
        Arg4 = (uint32_t)((Arg4) | (16));
    }
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_m7B0)) + (1));
    v_stack_m840 = v_stack_m7C8;
    v_stack_m848 = (uint32_t)(Arg1);
    result = MmCreateProcessAddressSpace(v_stack_m720, Arg2, Arg3, Arg4);
    result = (uint32_t)(((uint8_t)(result)) << (11));
    result = (uint32_t)((result) ^ ((uint32_t)(local_rbx)));
    result = (uint32_t)((result) & ((uint32_t)((uint32_t)(0x800ULL))));
    local_rbx = (uint32_t)((local_rbx) ^ ((uint32_t)(result)));
    v_stack_m7E4 = (uint32_t)(local_rbx);
    if ((((uint8_t)(local_rbx)) & (32)) != 0) {
        Arg2 = v_stack_m408;
        Arg1 = v_stack_m6E0;
        result = PspDetachSession(Arg1, Arg2, Arg3, Arg4);
    }
    if ((((uint32_t)((uint32_t)(0x800ULL))) & ((uint32_t)(local_rbx))) != 0) goto loc_00A151E3;
loc_00A151B9:
    goto loc_00A14CD5;
loc_00A151C3:
    Arg2 = 0;
    result = PspInheritQuota(v_stack_m7C8, Arg2, Arg3, Arg4);
    *(uint8_t *)(v_stack_m7C8 + 0x160) = 1;
    result = MmInitializeHandBuiltProcess(v_stack_m7C8, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00A14CD5;
loc_00A151E3:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m7C8 + 0x388)))) & (4)) != 0) {
        Arg1 = (uint32_t)(((uint32_t)(v_stack_m770)) | (1));
    }
    Arg4 = ((uint32_t)(v_stack_m700)) + (v_stack_m7C8);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (2));
    if (condition_is_above_or_equal) { Arg3 = (uint32_t)(Arg1); }
    result = PsGetSessionSchedulingGroupByProcess(v_stack_m7C8, Arg2, Arg3, Arg4);
    v_stack_m828 = Arg4;
    v_stack_m830 = (uint32_t)(Arg3);
    v_stack_m840 = result;
    v_stack_m848 = v_stack_m7B0;
    result = KeInitializeProcess(v_stack_m7C8, 8, v_stack_m7DC, v_stack_m3D8);
    if (sign_flag) goto loc_00A14CD5;
    if (Arg11 == 0) goto loc_00A153AE;
    if ((((uint8_t)(local_rbx)) & (2)) != 0) goto loc_00A153AE;
    v_stack_m744 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg11 + 0x180)));
    v_stack_m748 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg11 + 0x184)));
    v_stack_m6A0 = *(uint64_t *)(Arg11 + 0x198);
    v_stack_m74C = (uint32_t)((uint32_t)(*(uint32_t *)(Arg11 + 0x188)));
    v_stack_m6A8 = *(uint64_t *)(Arg11 + 0xD8);
    v_stack_m794 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg11 + 0x18C)));
    if (*(uint64_t *)(Arg11 + 0xB8) == 0) goto loc_00A153B1;
    if (*(uint64_t *)(v_rip + 0x4EFC0B) == 0) goto loc_00A153B1;
    result = guard_dispatch_icall(*(uint64_t *)(Arg11 + 0xB8), v_stack_m2C8, v_stack_m7DC, v_stack_m3D8);
    if (sign_flag) goto loc_00A153B1;
    if (v_stack_m2C8 != 0) goto loc_00A15399;
    if (*(uint64_t *)(Arg11 + 0x190) == 0) goto loc_00A15399;
    if (v_stack_m794 != 524) goto loc_00A15399;
loc_00A1533B:
    *(uint64_t *)(v_stack_m2C8) = v_xmm0;
    *(uint64_t *)(v_stack_m2C8 + 0x10) = v_xmm1;
    *(uint64_t *)(v_stack_m2C8 + 0x20) = v_xmm0;
    *(uint64_t *)(v_stack_m2C8 + 0x30) = v_xmm1;
    *(uint64_t *)(v_stack_m2C8 + 0x40) = v_xmm0;
    *(uint64_t *)(v_stack_m2C8 + 0x50) = v_xmm1;
    *(uint64_t *)(v_stack_m2C8 + 0x60) = v_xmm0;
    *(uint64_t *)(v_stack_m2C8 + 0x80 - 0x10) = v_xmm1;
    result = (4) - (1);
    if (condition_is_not_equal) goto loc_00A1533B;
    *(uint64_t *)(v_stack_m2C8 + 0x80) = *(uint64_t *)(*(uint64_t *)(Arg11 + 0x190) + 0x80);
    *(uint32_t *)(v_stack_m2C8 + 0x80 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg11 + 0x190) + 0x80 + 0x8)));
loc_00A15399:
    v_stack_m794 = 536;
    goto loc_00A153B1;
loc_00A153AE:
loc_00A153B1:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(v_stack_m2C8 + 128, v_stack_m2C8, v_stack_m7DC, v_stack_m3D8);
    if ((uint32_t)(result) == 0) goto loc_00A153D6;
    if (Arg11 == 0) goto loc_00A153D6;
    if (!(condition_is_above_or_equal)) {
        result = Arg11 + 496;
        v_stack_m6B0 = result;
    }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (16));
    Arg1 = (uint32_t)((Arg1) & (1));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (4));
    result = (uint32_t)((result) & (1));
    v_stack_m7F8 = v_stack_m648;
    v_stack_m800 = v_stack_m6B0;
    v_stack_m808 = v_stack_m6A8;
    v_stack_m810 = (uint32_t)((uint32_t)(v_stack_m74C));
    v_stack_m818 = v_stack_m6A0;
    v_stack_m820 = (uint32_t)((uint32_t)(v_stack_m794));
    v_stack_m828 = 0;
    v_stack_m830 = (uint32_t)((uint32_t)(v_stack_m748));
    v_stack_m838 = (uint32_t)(Arg1);
    v_stack_m840 = (uint32_t)(result);
    v_stack_m848 = (uint32_t)((uint32_t)(v_stack_m744));
    result = PspInitializeProcessSecurity(v_stack_m7D0, v_stack_m7C8, v_stack_m768, (uint32_t)(Arg12));
    if (sign_flag) goto loc_00A14CD5;
    *(uint8_t *)(v_stack_m7C8 + 0x347) = 2;
    if (v_stack_m7D0 == 0) goto loc_00A154DA;
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(v_stack_m7D0 + 0x347))) - (1));
    if ((((uint8_t)(result)) & (251)) == 0) {
        *(uint8_t *)(v_stack_m7C8 + 0x347) = (uint8_t)(*(uint8_t *)(v_stack_m7D0 + 0x347));
    }
    if (Arg11 == 0) goto loc_00A154AB;
    goto loc_00A154AE;
loc_00A154AB:
loc_00A154AE:
    if (Arg11 == 0) goto loc_00A154BC;
    goto loc_00A154BF;
loc_00A154BC:
loc_00A154BF:
    result = (uint8_t)(((uint32_t)(Arg9)) & (4));
    result = (uint8_t)(-(result));
    Arg1 = (*(uint8_t *)(v_stack_m7D0 + 0x347)) & (v_stack_m7D0);
    result = ObInitProcess(Arg1, v_stack_m7C8, 0, 0);
    goto loc_00A154F8;
loc_00A154DA:
    *(uint64_t *)(v_stack_m7C8 + 0x300) = *(uint64_t *)(v_stack_m780 + 0x300);
    result = MmInitializeHandBuiltProcess2(v_stack_m7C8, v_stack_m7C8, 0, 0);
loc_00A154F8:
    if (sign_flag) goto loc_00A14CD5;
    if (((v_stack_m430) & (7)) != 0) {
        Arg3 = (uint8_t)(v_stack_m7E8);
        Arg2 = v_stack_m430;
        Arg1 = v_stack_m7C8;
        result = PspApplyIFEOPerfOptions(Arg1, Arg2, Arg3, 0);
    }
    if (!(condition_is_above_or_equal)) {
        v_stack_m848 = 0;
        Arg4 = 1;
        Arg3 = v_stack_m6C8;
        Arg2 = v_stack_m7A4;
        Arg1 = v_stack_m7C8;
        result = KeSetCpuSetsProcess(Arg1, Arg2, Arg3, Arg4);
    }
    if (((v_stack_m42C) & (2)) != 0) {
        Arg2 = v_stack_m410;
        Arg1 = v_stack_m7C8;
        result = KeSetExpectedConcurrencyCountProcess(Arg1, Arg2, Arg3, Arg4);
    }
    if (Arg11 == 0) goto loc_00A15591;
    if (condition_is_above_or_equal) goto loc_00A15591;
    Arg3 = 0;
    result = PspSetProcessPriorityClass(v_stack_m7C8, *(uint8_t *)(Arg11 + 0x2), Arg3, (uint8_t)(v_stack_m7E8));
    if (sign_flag) goto loc_00A14CD5;
loc_00A15591:
    v_stack_m848 = 0;
    Arg4 = 0;
    Arg2 = 0;
    result = PspComputeQuantumAndPriority(v_stack_m7C8, Arg2, v_stack_m7D4, Arg4);
    *(uint8_t *)(v_stack_m7C8 + 0x90) = (uint8_t)(result);
    *(uint8_t *)(v_stack_m7C8 + 0x91) = (uint8_t)(v_stack_m7D4);
    v_stack_m7A4 = 0;
    result = PspReadIFEOMitigationOptions(Arg11, v_stack_m468, v_stack_m7D4, Arg4);
    v_stack_m5B8 = v_xmm0;
    v_stack_m5A8 = v_xmm0;
    v_stack_m598 = v_xmm1;
    v_stack_m588 = v_xmm0;
    result = PspInheritMitigationOptions(v_stack_m598, v_stack_m5B8, v_stack_m468, Arg4);
    result = PspReadIFEOMitigationAuditOptions(Arg11, v_stack_m450, v_stack_m468, Arg4);
    v_stack_m578 = v_xmm0;
    v_stack_m568 = v_xmm0;
    v_stack_m558 = v_xmm1;
    v_stack_m548 = v_xmm0;
    result = PspInheritMitigationAuditOptions(v_stack_m558, v_stack_m578, v_stack_m450, Arg4);
    local_rdi = (v_stack_m468) >> (48);
    local_rdi = (uint32_t)((local_rdi) & (3));
    local_rdi = (uint32_t)((local_rdi) << (14));
    if (Arg11 == 0) goto loc_00A1579D;
    result = (uint32_t)(*(uint32_t *)(Arg11 + 0x8));
    if (!(condition_is_above_or_equal)) {
        v_stack_m538 = v_xmm0;
        v_stack_m528 = v_xmm1;
        v_stack_m518 = v_xmm0;
        v_stack_m508 = v_xmm0;
        Arg3 = v_stack_m468;
        Arg2 = v_stack_m538;
        Arg1 = v_stack_m518;
        result = PspInheritMitigationOptions(Arg1, Arg2, Arg3, Arg4);
    }
    if (Arg11 == 0) goto loc_00A1579D;
    result = (uint32_t)(*(uint32_t *)(Arg11 + 0x8));
    if (!(condition_is_above_or_equal)) {
        v_stack_m4F8 = v_xmm0;
        v_stack_m4E8 = v_xmm1;
        v_stack_m4D8 = v_xmm0;
        v_stack_m4C8 = v_xmm0;
        Arg3 = v_stack_m450;
        Arg2 = v_stack_m4F8;
        Arg1 = v_stack_m4D8;
        result = PspInheritMitigationAuditOptions(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m784 != 0) {
        local_rdi = (uint32_t)((local_rdi) | (4));
    }
    local_r11 = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) | (64));
    if ((((uint8_t)(local_rdi)) & (4)) == 0) { local_r11 = (uint32_t)(local_rdi); }
    if ((((uint32_t)(local_r11)) & (0x3FC0ULL)) != 0) {
        Arg1 = v_stack_m468;
        result = PspHardenMitigationOptions(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeIsUserCetAllowed(Arg1, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) {
        result = v_stack_m460;
        result = (result) & (0);
        result = (result) | (local_r10);
        v_stack_m460 = result;
    }
    Arg2 = (uint16_t)(((uint16_t)(v_stack_m7C0)) & ((uint16_t)((uint32_t)(0x4000ULL))));
    Arg3 = ((((uint32_t)(local_rbx)) & (0x6000ULL)) != 0) ? 1 : 0;
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m7C0))) >> (4));
    result = (uint32_t)((result) & (2));
    Arg3 = (uint32_t)((Arg3) | ((uint32_t)(result)));
    result = (uint16_t)(-((uint16_t)(Arg2)));
    Arg1 = (uint32_t)((v_stack_m7C0) & (8));
    Arg3 = (uint32_t)((Arg3) | ((uint32_t)(Arg1)));
    Arg3 = (uint32_t)((Arg3) | ((uint32_t)(local_r11)));
    if ((uint16_t)(Arg2) == 0) goto loc_00A15848;
    if (!(condition_is_below)) {
        v_stack_m740 = 0;
    }
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (1));
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (0x3E00000ULL));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) & (0x100000ULL));
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(result)));
    local_rdi = (uint32_t)((local_rdi) >> (4));
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(Arg3)));
    local_rdi = (uint32_t)((local_rdi) | (v_stack_m740));
    if (((1) & ((uint8_t)(Arg1))) == 0) goto loc_00A15906;
    Arg1 = (v_stack_m468) & (result);
    Arg1 = (Arg1) | (result);
    v_stack_m468 = Arg1;
    result = (v_stack_m460) & (Arg2);
    result = (result) | (Arg2);
    v_stack_m460 = result;
    Arg1 = (Arg1) & (0xFFFFFFFFFFFCFFFFULL);
    if (((Arg10) & (2)) == 0) goto loc_00A158ED;
    Arg1 = (Arg1) | (0x220000ULL);
    goto loc_00A158FE;
loc_00A158ED:
    Arg1 = (Arg1) & (0xFFFFFFFFFFCFFFFFULL);
loc_00A158FE:
    v_stack_m468 = Arg1;
loc_00A15906:
    if ((((uint8_t)(local_rbx)) & (4)) == 0) goto loc_00A1592F;
    if (((*(uint32_t *)(v_stack_m7D0 + 0x754)) & (0x4000ULL)) == 0) {
        result = v_stack_m460;
        result = (result) & (0);
        result = (result) | (local_r10);
        v_stack_m460 = result;
    }
    if ((((uint8_t)(local_rbx)) & (64)) != 0) {
        result = v_stack_m460;
        result = (result) & (0);
        result = (result) | (local_r10);
        v_stack_m460 = result;
    }
    v_stack_m458 = v_stack_m458;
    result = KeIsCoreIsolationMitigationPolicyEnforceable(v_stack_m458, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) {
        v_stack_m458 = v_stack_m458;
    }
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(v_stack_m458, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00A159CA;
    if (Arg11 == 0) goto loc_00A159A4;
    if (!(condition_is_above_or_equal)) {
        result = Arg11 + 528;
        v_stack_m670 = result;
    }
    result = PspReadIFEOAntiTamperOptions(Arg11, v_stack_m438, Arg3, Arg4);
    Arg1 = v_stack_m438;
    if (sign_flag) { Arg1 = 0; }
    v_stack_m6D8 = Arg1;
loc_00A159CA:
    v_stack_m838 = (uint32_t)((uint32_t)(v_stack_m790));
    v_stack_m840 = (uint32_t)((uint32_t)(v_stack_m78C));
    v_stack_m848 = (uint32_t)(local_rdi);
    result = PspApplyMitigationOptions(v_stack_m7C8, v_stack_m7D0, v_stack_m468, v_stack_m450);
    if (Arg11 == 0) goto loc_00A15AC2;
    if (*(uint64_t *)(Arg11 + 0x1B0) == 0) goto loc_00A15A5F;
    local_r14 = v_stack_m7C8;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg11 + 0x1B0)))))) != 0) {
        local_r14 = v_stack_m7C8;
    }
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg11 + 0x1B0))))) & (2)) != 0) {
        local_r14 = v_stack_m7C8;
    }
    *(uint32_t *)(local_r14 + 0x6E8) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg11 + 0x1B0) + 0x4)));
loc_00A15A5F:
    if (Arg11 == 0) goto loc_00A15AC2;
    result = *(uint64_t *)(Arg11 + 0x1B8);
    if (*(uint64_t *)(Arg11 + 0x1B8) != 0) {
        result = *(uint32_t *)(*(uint64_t *)(Arg11 + 0x1B8));
        *(uint32_t *)(local_r14 + 0x7A0) = (uint32_t)(result);
    }
    if (Arg11 != 0) {
        *(uint64_t *)(Arg11 + 0x150) = v_xmm0;
        *(uint64_t *)(Arg11 + 0x160) = v_xmm0;
        *(uint64_t *)(Arg11 + 0x1C0) = v_xmm1;
        *(uint64_t *)(Arg11 + 0x1D0) = v_xmm0;
    }
    v_stack_m640 = 0;
    v_stack_m638 = 0;
    v_stack_m848 = v_stack_m640;
    result = AppModelPolicy_GetPolicy_Internal(v_stack_m768, 1, v_stack_m788, v_stack_m638);
    result = (uint32_t)(v_stack_m788);
    if (sign_flag) { result = (uint32_t)((uint32_t)(0x10000ULL)); }
    v_stack_m788 = (uint32_t)(result);
    Arg1 = 0;
    if (((uint32_t)(result)) == 0x10001ULL) { Arg1 = 1; }
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (2));
    if (((Arg9) & (0x20000ULL)) == 0) { Arg2 = (uint32_t)(Arg1); }
    result = SmProcessCreateNotification(local_r14, Arg2, v_stack_m788, v_stack_m638);
    if (((*(uint32_t *)(local_r14 + 0x754)) & (0x4000ULL)) == 0) goto loc_00A15B5E;
    result = KeInitializeProcessUserCetLogging(local_r14, Arg2, v_stack_m788, v_stack_m638);
    if (sign_flag) goto loc_00A14CD5;
loc_00A15B5E:
    if (((Arg9) & (128)) == 0) goto loc_00A15B94;
    result = PspIsSessionLeaderProcess(v_stack_m780, Arg2, v_stack_m788, v_stack_m638);
    if ((uint32_t)(result) != 0) goto loc_00A15B94;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x5C3F99), v_stack_m7E8, v_stack_m788, v_stack_m638);
    if ((uint8_t)(result) == 0) goto loc_00A14CD0;
loc_00A15B94:
    if (((1) & ((uint8_t)(local_rbx))) != 0) goto loc_00A15D3B;
    if ((((uint8_t)(local_rbx)) & (4)) != 0) goto loc_00A15C29;
    result = PspInitializeFullProcessImageName(Arg11, local_r14, v_stack_m788, v_stack_m638);
    if (sign_flag) goto loc_00A14CD5;
    v_stack_m848 = 0;
    Arg2 = 0;
    result = MmInitializeProcessAddressSpace(local_r14, Arg2, v_stack_m760, Arg9);
    if (sign_flag) goto loc_00A14CD5;
    v_stack_m7A4 = (uint32_t)(result);
    if (Arg11 == 0) goto loc_00A15C19;
    if ((((uint8_t)(local_rbx)) & (2)) != 0) goto loc_00A15C19;
    result = MiSectionControlArea(v_stack_m760, Arg2, v_stack_m760, Arg9);
    result = *(uint64_t *)(local_r14 + 0x2B0);
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x20)) != (*(uint64_t *)(local_r14 + 0x2B0))) {
        result = (*(uint64_t *)(local_r14 + 0x2B0)) - (*(uint64_t *)(*(uint64_t *)(result) + 0x20));
    }
    v_stack_m7E4 = (uint32_t)(local_rbx);
    goto loc_00A15D08;
loc_00A15C29:
    *(uint64_t *)(local_r14 + 0x2B0) = *(uint64_t *)(v_stack_m760 + 0x2B0);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (3));
    result = (uint32_t)((result) & (1));
    v_stack_m848 = (uint32_t)(result);
    Arg3 = 0;
    result = MmInitializeProcessAddressSpace(local_r14, v_stack_m760, Arg3, Arg9);
    if (sign_flag) goto loc_00A14CD5;
    result = ExAllocatePool2(64, *(uint16_t *)(*(uint64_t *)(v_stack_m760 + 0x350) + 0x2) + 16, (uint32_t)(0x61506553ULL), Arg9);
    *(uint64_t *)(local_r14 + 0x350) = result;
    if (result == 0) goto loc_00A151B9;
    result = memcpy(result, *(uint64_t *)(v_stack_m7D0 + 0x350), *(uint16_t *)(*(uint64_t *)(v_stack_m760 + 0x350) + 0x2) + 16, Arg9);
    *(uint64_t *)(*(uint64_t *)(local_r14 + 0x350) + 0x8) = *(uint64_t *)(local_r14 + 0x350) + 16;
    *(uint32_t *)(local_r14 + 0x2B8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m7D0 + 0x2B8)));
    if (((*(uint32_t *)(v_stack_m7D0 + 0x1F0)) & ((uint32_t)((uint32_t)(0x1000000ULL)))) != 0) {
    }
    result = (uint32_t)(*(uint32_t *)(v_stack_m7D0 + 0x2B8));
    if (((Arg9) & (0x1000ULL)) != 0) {
        *(uint64_t *)(local_r14 + 0x2A8) = 0;
        Arg1 = v_stack_m760;
        result = ObfDereferenceObject(Arg1, *(uint64_t *)(v_stack_m7D0 + 0x350), *(uint16_t *)(*(uint64_t *)(v_stack_m760 + 0x350) + 0x2) + 16, Arg9);
    }
    if (((1) & ((uint8_t)(local_rbx))) != 0) goto loc_00A15D3B;
    Arg1 = (uint32_t)(((uint32_t)(Arg9)) & (16));
    Arg1 = (uint32_t)((Arg1) << (8));
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | ((uint32_t)((uint32_t)((uint32_t)(local_rbx)))));
    v_stack_m7E4 = (uint32_t)(local_rbx);
    if ((((uint8_t)(local_rbx)) & (2)) == 0) {
        v_stack_m7E4 = (uint32_t)(local_rbx);
    }
    result = (uint32_t)((uint32_t)(local_rbx));
    if (!(condition_is_above_or_equal)) {
        Arg1 = v_stack_m6D0;
        result = RtlReleasePrivilege(Arg1, *(uint64_t *)(v_stack_m7D0 + 0x350), *(uint16_t *)(*(uint64_t *)(v_stack_m760 + 0x350) + 0x2) + 16, Arg9);
    }
    if ((*(uint16_t *)(local_r14 + 0x6EC)) == 332) {
    }
    if (!sign_flag) goto loc_00A15D8F;
    if (Arg11 == 0) goto loc_00A15D8F;
    if ((((uint8_t)(local_rbx)) & (2)) != 0) goto loc_00A15D8F;
    result = PspSetupReservedUserMappings(local_r14, v_stack_m408, Arg11, Arg9);
    if (sign_flag) goto loc_00A14CE8;
loc_00A15D8F:
    if (condition_is_above_or_equal) goto loc_00A15EAB;
    Arg2 = 0;
    result = PsQueryProcessAttributes(local_r14, Arg2, v_stack_m7D3, Arg9);
    result = 0;
    v_stack_m6C0 = 0;
    result = (uint8_t)((*(uint8_t *)(local_r14 + 0x5FA)) & (7));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (12));
    Arg2 = (uint8_t)((Arg2) & (1));
    Arg1 = (uint8_t)((local_r14) & (2));
    Arg2 = (uint8_t)((Arg2) | ((uint8_t)(Arg1)));
    Arg1 = (uint8_t)((v_stack_m6BD) & (252));
    Arg2 = (uint8_t)((Arg2) | ((uint8_t)(Arg1)));
    Arg2 = (uint8_t)((Arg2) & (187));
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (13));
    Arg1 = (uint8_t)((Arg1) & (1));
    result = (((uint8_t)(result)) != 1) ? 1 : 0;
    result = (uint8_t)((result) - (1));
    result = (uint8_t)((result) & (16));
    Arg1 = (uint8_t)((Arg1) | ((uint8_t)(result)));
    Arg1 = (uint8_t)((Arg1) << (2));
    Arg2 = (uint8_t)((Arg2) | ((uint8_t)(Arg1)));
    result = (uint32_t)(-((uint32_t)(v_stack_m784)));
    Arg1 = (uint8_t)((Arg1) & (2));
    local_r12 = (uint8_t)((v_stack_m7D3) & (1));
    local_r12 = (uint8_t)((local_r12) | ((uint8_t)(Arg1)));
    local_r12 = (uint8_t)((local_r12) << (4));
    Arg2 = (uint8_t)((Arg2) & (207));
    local_r12 = (uint8_t)((local_r12) | ((uint8_t)(Arg2)));
    v_stack_m6BD = (uint8_t)(local_r12);
    if ((((uint8_t)(local_rbx)) & (4)) != 0) goto loc_00A15EEA;
    result = MmCreatePeb(local_r14, v_stack_m6C0, local_r14 + 736, v_stack_m658);
    if (!sign_flag) goto loc_00A15E6A;
    *(uint64_t *)(local_r14 + 0x2E0) = 0;
    goto loc_00A14CE8;
loc_00A15E6A:
    if (v_stack_m658 != 0) {
        result = v_stack_m6FC;
        v_stack_m848 = result;
        Arg4 = v_stack_m658;
        Arg3 = 0;
        Arg2 = 1;
        local_r14 = v_stack_m7C8;
        Arg1 = local_r14;
        result = PspSetProcessAffinitySafe(Arg1, Arg2, Arg3, Arg4);
    }
loc_00A15EB3:
    if (!sign_flag) goto loc_00A160BB;
    if (Arg11 == 0) goto loc_00A160BB;
    if ((((uint8_t)(local_rbx)) & (2)) != 0) goto loc_00A160BB;
    result = PspSetupUserProcessAddressSpace(v_stack_m7D0, local_r14, v_stack_m408, Arg11);
    goto loc_00A16154;
loc_00A15EEA:
    *(uint64_t *)(local_r14 + 0x2E0) = *(uint64_t *)(v_stack_m7D0 + 0x2E0);
    if ((((uint8_t)(local_rbx)) & (16)) != 0) goto loc_00A160B0;
    v_stack_m6C0 = 1;
    Arg2 = 0;
    result = KiStackAttachProcess(local_r14, Arg2, v_stack_m408, Arg11);
    result = MmSecureVirtualMemory(*(uint64_t *)(v_stack_m7D0 + 0x2E0), (uint32_t)(0x7D8ULL), 4, Arg11);
    if (result == 0) goto loc_00A15FAC;
    *(uint64_t *)(*(uint64_t *)(v_stack_m7D0 + 0x2E0)) = v_xmm0;
    goto loc_00A15FBF;
loc_00A15FAC:
loc_00A15FBF:
    if (sign_flag) goto loc_00A1608E;
    if (*(uint64_t *)(local_r14 + 0x310) == 0) goto loc_00A1608E;
    if (((uint16_t)(*(uint16_t *)(local_r14 + 0x6EC))) == 332) goto loc_00A15FF1;
    result = 0;
    if (((uint16_t)(*(uint16_t *)(local_r14 + 0x6EC))) == 452) {
        result = 1;
    }
    if ((uint8_t)(result) == 0) goto loc_00A1608E;
    result = MmSecureVirtualMemory(*(uint64_t *)(*(uint64_t *)(local_r14 + 0x310)), (uint32_t)(0x490ULL), 1 + 3, Arg11);
    if (result == 0) goto loc_00A16089;
    result = 0;
    v_stack_m710 = 0;
    v_stack_m710 = 1;
    v_stack_m70D = (uint8_t)(local_r14 + 736);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(local_r14 + 0x310))) = v_stack_m710;
    goto loc_00A16094;
loc_00A16089:
loc_00A1608E:
loc_00A16094:
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_m408, Arg2, 1 + 3, Arg11);
    if (sign_flag) goto loc_00A14CE8;
    goto loc_00A15EAB;
loc_00A160B0:
    goto loc_00A15EB3;
loc_00A160BB:
    if (condition_is_above_or_equal) goto loc_00A16154;
    if ((((uint8_t)(local_rbx)) & (16)) != 0) goto loc_00A16154;
    Arg2 = 0;
    result = KiStackAttachProcess(local_r14, Arg2, v_stack_m408, Arg11);
    result = KeCopyXfdMaskToPeb(local_r14, Arg2, v_stack_m408, Arg11);
    result = PspUpdatePebForAffinityChange(v_stack_m668, local_r14, v_stack_m408, Arg11);
    if (!sign_flag) goto loc_00A16145;
    result = MmMapApiSetView(local_r14, local_r14, v_stack_m408, Arg11);
    if (sign_flag) goto loc_00A16145;
    result = PspMapSiloSharedDataView(local_r14, local_r14, v_stack_m408, Arg11);
    if (sign_flag) goto loc_00A16145;
    Arg2 = 0;
    Arg1 = 0;
    result = PspPrepareSystemDllInitBlock(Arg1, Arg2, v_stack_m408, Arg11);
    if (sign_flag) goto loc_00A16145;
    local_rdi = (uint32_t)((uint32_t)(result));
    if ((*(uint64_t *)(local_r14 + 0x310)) != 0) {
        Arg1 = local_r14;
        result = PsWow64GetProcessNtdllType(Arg1, Arg2, v_stack_m408, Arg11);
        Arg2 = 0;
        Arg1 = (uint32_t)(result);
        result = PspPrepareSystemDllInitBlock(Arg1, Arg2, v_stack_m408, Arg11);
        local_rdi = (uint32_t)(result);
    }
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_m408, Arg2, v_stack_m408, Arg11);
loc_00A16154:
    if (sign_flag) goto loc_00A14CE8;
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(v_stack_m408, Arg2, v_stack_m408, Arg11);
    if ((uint32_t)(result) == 0) goto loc_00A1621D;
    v_stack_m848 = v_stack_m708;
    Arg4 = 0;
    result = SeConstructAntiTamperPolicy(v_stack_m7D0, v_stack_m6D8, v_stack_m670, Arg4);
    if (sign_flag) goto loc_00A14CE8;
    if (v_stack_m708 == 0) goto loc_00A1621D;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m708))))) == 0) goto loc_00A1621D;
    result = (uint32_t)(*(uint32_t *)(v_stack_m708));
    if (Arg11 != 0) {
        result = *(uint64_t *)(Arg11 + 0xB0);
        v_stack_m718 = result;
    }
    result = PsReferencePrimaryTokenWithTag(local_r14, (uint32_t)(0x746C6644ULL), v_stack_m670, Arg4);
    result = SeSetTokenTamperProtection(v_stack_m7D0, v_stack_m718, v_stack_m708, result);
    if (!sign_flag) goto loc_00A16218;
    result = ObFastDereferenceObject(local_r14 + 584, result, (uint32_t)(0x746C6644ULL), result);
    goto loc_00A14CE8;
loc_00A16218:
    result = ObFastDereferenceObject(local_r14 + 584, result, (uint32_t)(0x746C6644ULL), result);
loc_00A1621D:
    result = PspLockProcessExclusive(local_r14, v_stack_m668, (uint32_t)(0x746C6644ULL), result);
    v_stack_m848 = 0;
    Arg4 = 0;
    Arg3 = 0;
    result = ExCreateHandleEx(*(uint64_t *)(v_rip + 0x5B0A71), local_r14, Arg3, Arg4);
    v_stack_m758 = result;
    if (result != 0) goto loc_00A1626F;
    result = PspUnlockProcessExclusive(local_r14, v_stack_m668, Arg3, Arg4);
    goto loc_00A14CE8;
loc_00A1626F:
    if (condition_is_above_or_equal) goto loc_00A162FA;
    Arg2 = 0;
    Arg1 = 0;
    result = MmGetSectionStrongImageReference(Arg1, Arg2, *(uint64_t *)(local_r14 + 0x2A8), v_stack_m660);
    if (!sign_flag) goto loc_00A162A7;
loc_00A1629A:
    result = PspUnlockProcessExclusive(local_r14, v_stack_m668, *(uint64_t *)(local_r14 + 0x2A8), v_stack_m660);
    goto loc_00A14CE8;
loc_00A162A7:
    v_stack_m838 = (uint32_t)(*(uint32_t *)(Arg11 + 0x178));
    v_stack_m840 = *(uint64_t *)(Arg11 + 0x168);
    v_stack_m848 = v_stack_m660;
    result = KeSecureProcess(local_r14, *(uint64_t *)(local_r14 + 0x2E0), v_stack_m758, *(uint64_t *)(Arg11 + 0xC0));
    if (!sign_flag) goto loc_00A162F2;
    goto loc_00A1629A;
loc_00A162F2:
loc_00A162FA:
    result = KeQuerySystemTimeUnsafe(local_r14, *(uint64_t *)(local_r14 + 0x2E0), v_stack_m758, *(uint64_t *)(Arg11 + 0xC0));
    if (result == 0) goto loc_00A16312;
    result = KeQuerySystemTimePrecise(local_r14 + 504, *(uint64_t *)(local_r14 + 0x2E0), v_stack_m758, *(uint64_t *)(Arg11 + 0xC0));
    goto loc_00A1632B;
loc_00A16312:
    *(uint64_t *)(v_stack_m7C8 + 0x1F8) = result;
loc_00A1632B:
    *(uint64_t *)(v_stack_m7C8 + 0x1D0) = v_stack_m758;
    *(uint64_t *)(v_stack_m7C8 + 0x680) = result;
    result = KiQueryUnbiasedInterruptTime(1, *(uint64_t *)(local_r14 + 0x2E0), v_stack_m758, *(uint64_t *)(Arg11 + 0xC0));
    *(uint64_t *)(v_stack_m7C8 + 0x688) = result;
    *(uint64_t *)(v_stack_m7C8 + 0x698) = *(uint64_t *)(v_stack_m7C8 + 0x680);
    *(uint64_t *)(v_stack_m630) = v_stack_m7C8;
    goto loc_00A14D13;
loc_00A1637F:
loc_00A16384:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(local_r14 + 0x2E0), v_stack_m758, *(uint64_t *)(Arg11 + 0xC0));
    local_rsp = (local_rsp) + (0x830ULL);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x5FC` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A13B3C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
