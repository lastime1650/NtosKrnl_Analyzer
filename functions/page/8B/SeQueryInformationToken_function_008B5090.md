# SeQueryInformationToken

- RVA: `0x008B5090`–`0x008B63EE` (길이 `4,958` bytes)
- VA: `0x00000001408B5090`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082A48`
- 디코드: `1,188`개 명령, `4,958/4,958` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **105**; 고유 호출 대상: **29**
- 직접 호출자로 확인된 함수: **29**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008B513C` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B5162` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B5173` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008B5194` → [RtlCopySid](../9A/RtlCopySid_function_009A9A50.md) (function, `0x009A9A50`)
- `0x008B519D` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008B51A2` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008B51C9` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B51FC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B524B` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B5253` → [SepTokenPrivilegeCount](../../text/43/SepTokenPrivilegeCount_function_00432EC0.md) (function, `0x00432EC0`)
- `0x008B527B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B5292` → [SepConvertTokenPrivileges](../../text/46/SepConvertTokenPrivileges_function_00463EF8.md) (function, `0x00463EF8`)
- `0x008B52BA` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B530E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B5368` → [RtlCopySidAndAttributesArray](../9A/RtlCopySidAndAttributesArray_function_009A8BE0.md) (function, `0x009A8BE0`)
- `0x008B5371` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008B5376` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008B53A1` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B53CA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B53DB` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008B53E0` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008B541A` → [RtlCopySidAndAttributesArray](../9A/RtlCopySidAndAttributesArray_function_009A8BE0.md) (function, `0x009A8BE0`)
- `0x008B543E` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B5469` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B549A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008B54D6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B5532` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B558B` → [SepTokenPrivilegeCount](../../text/43/SepTokenPrivilegeCount_function_00432EC0.md) (function, `0x00432EC0`)
- `0x008B55A2` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008B55A7` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008B55D1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B5602` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B562B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B564B` → [SeQuerySessionIdToken](../A0/SeQuerySessionIdToken_function_00A04490.md) (function, `0x00A04490`)
- `0x008B56D0` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B56DC` → [SepCopyTokenIntegrity](../../text/41/SepCopyTokenIntegrity_function_00419D10.md) (function, `0x00419D10`)
- `0x008B56E5` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (function, `0x00468F10`)
- `0x008B56FE` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x008B570C` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008B574B` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B57AD` → [SepGetTokenAccessInformationBufferSize](../9E/SepGetTokenAccessInformationBufferSize_function_009E995C.md) (function, `0x009E995C`)
- `0x008B57C2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B5828` → [SepCopyTokenAccessInformation](../9E/SepCopyTokenAccessInformation_function_009E9C0C.md) (function, `0x009E9C0C`)
- `0x008B5882` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B58AD` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B58B5` → [SepGetTokenElevation](../../text/44/SepGetTokenElevation_function_0044F3C8.md) (function, `0x0044F3C8`)
- `0x008B58C0` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008B58C5` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008B58E1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B58F5` → [SepGetTokenElevationType](../../text/47/SepGetTokenElevationType_function_0047B1C4.md) (function, `0x0047B1C4`)
- `0x008B5922` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B592A` → [SepTokenPrivilegeCount](../../text/43/SepTokenPrivilegeCount_function_00432EC0.md) (function, `0x00432EC0`)
- `0x008B59D1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B5A6E` → [RtlCopySidAndAttributesArray](../9A/RtlCopySidAndAttributesArray_function_009A8BE0.md) (function, `0x009A8BE0`)
- `0x008B5AAD` → [RtlCopySidAndAttributesArray](../9A/RtlCopySidAndAttributesArray_function_009A8BE0.md) (function, `0x009A8BE0`)
- `0x008B5AB9` → [SepConvertTokenPrivilegesToLuidAndAttributes](../../text/42/SepConvertTokenPrivilegesToLuidAndAttributes_function_0042A870.md) (function, `0x0042A870`)
- `0x008B5B5B` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B5BA5` → [AuthzBasepQueryClaimAttributesToken](../A1/AuthzBasepQueryClaimAttributesToken_function_00A1830C.md) (function, `0x00A1830C`)
- `0x008B5BE8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B5C0B` → [AuthzBasepQueryClaimAttributesToken](../A1/AuthzBasepQueryClaimAttributesToken_function_00A1830C.md) (function, `0x00A1830C`)
- `0x008B5C16` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008B5C1B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008B5C29` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008B5C54` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B5C6C` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008B5C71` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008B5C98` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B5CC9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B5CF0` → [RtlCopySid](../9A/RtlCopySid_function_009A9A50.md) (function, `0x009A9A50`)
- `0x008B5D1C` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B5D6E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B5DDE` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B5E48` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B5EAA` → [RtlCopySidAndAttributesArray](../9A/RtlCopySidAndAttributesArray_function_009A8BE0.md) (function, `0x009A8BE0`)
- `0x008B5EB3` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008B5EB8` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008B5EF1` → [SepCanTokenMatchAllPackageSid](../../text/2F/SepCanTokenMatchAllPackageSid_function_002FFE90.md) (function, `0x002FFE90`)
- `0x008B5F29` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B5F53` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B5FBE` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B5FEF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B6068` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x008B608F` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B60B1` → [SepIsAppSuiteSid](../../text/60/SepIsAppSuiteSid_function_006083A0.md) (function, `0x006083A0`)
- `0x008B60DF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B6106` → [RtlCopySid](../9A/RtlCopySid_function_009A9A50.md) (function, `0x009A9A50`)
- `0x008B6123` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B6139` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x008B6160` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B61AB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B61D5` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x008B61FC` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B623D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B626A` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008B6274` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x008B62A6` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008B62C3` → [SepGetTokenLoggingInformationBufferSize](../A8/SepGetTokenLoggingInformationBufferSize_function_00A86380.md) (function, `0x00A86380`)
- `0x008B62D5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008B6305` → [SepCopyTokenLoggingInformation](../9A/SepCopyTokenLoggingInformation_function_009A8618.md) (function, `0x009A8618`)
- `0x008B6330` → [SepSidInTokenSidHash](../../text/3C/SepSidInTokenSidHash_function_003C85E0.md) (function, `0x003C85E0`)
- `0x008B6357` → [SepIsSandboxedToken](../../text/45/SepIsSandboxedToken_function_00458704.md) (function, `0x00458704`)
- `0x008B6366` → [Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline_function_004F2D58.md) (function, `0x004F2D58`)
- `0x008B6383` → [Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline_function_004F2D58.md) (function, `0x004F2D58`)
- `0x008B63A2` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x008B63B2` → [SeHasTamperProtection](../../text/60/SeHasTamperProtection_function_0060777C.md) (function, `0x0060777C`)

### Direct callers
- [RtlCheckTokenCapability](../../text/3A/RtlCheckTokenCapability_function_003A5520.md) at `0x003A5874`
- [RtlpQueryLowBoxId](../../text/43/RtlpQueryLowBoxId_function_00438A50.md) at `0x00438AB3`
- [RtlpQueryLowBoxId](../../text/43/RtlpQueryLowBoxId_function_00438A50.md) at `0x00438B69`
- [FsRtlpOplockGetThreadIntegrityLevel](../6F/FsRtlpOplockGetThreadIntegrityLevel_function_006FD814.md) at `0x006FD8B0`
- [RtlpIsAppContainer](../78/RtlpIsAppContainer_function_0078F37C.md) at `0x0078F49D`
- [CmpCreateRegistryProcessToken](../7E/CmpCreateRegistryProcessToken_function_007E7F6C.md) at `0x007E7FB2`
- [CmpCreateRegistryProcessToken](../7E/CmpCreateRegistryProcessToken_function_007E7F6C.md) at `0x007E7FCB`
- [CmpGenerateAppHiveSecurityDescriptor](../7E/CmpGenerateAppHiveSecurityDescriptor_function_007ECEAC.md) at `0x007ECF35`
- [CmpGenerateAppHiveSecurityDescriptor](../7E/CmpGenerateAppHiveSecurityDescriptor_function_007ECEAC.md) at `0x007ECF4D`
- [EtwpPsProvTraceProcess](../8A/EtwpPsProvTraceProcess_function_008A3954.md) at `0x008A3B51`
- [EtwpPsProvTraceProcess](../8A/EtwpPsProvTraceProcess_function_008A3954.md) at `0x008A3B96`
- [EtwpPsProvTraceProcess](../8A/EtwpPsProvTraceProcess_function_008A3954.md) at `0x008A3D91`
- [EtwpPsProvTraceProcess](../8A/EtwpPsProvTraceProcess_function_008A3954.md) at `0x008A3DBB`
- [EtwpBuildProcessEvent](../8A/EtwpBuildProcessEvent_function_008A552C.md) at `0x008A561A`
- [ObpParseSymbolicLinkEx](ObpParseSymbolicLinkEx_function_008B35C0.md) at `0x008B3818`
- [RtlIsSandboxedToken](RtlIsSandboxedToken_function_008B3AB0.md) at `0x008B3AF1`
- [sub_008B4839](Unknown_function_008B4839.md) at `0x008B48C4`
- [sub_008B4EDF](Unknown_function_008B4EDF.md) at `0x008B4EFC`
- [NtDuplicateToken](NtDuplicateToken_function_008B6DF0.md) at `0x008B6F2C`
- [EtwTiLogImpersonateClient](../8C/EtwTiLogImpersonateClient_function_008CC9D0.md) at `0x008CCAA6`
- [EtwTiLogImpersonateClient](../8C/EtwTiLogImpersonateClient_function_008CC9D0.md) at `0x008CCABD`
- [SeCompareTokens](../8F/SeCompareTokens_function_008F6F40.md) at `0x008F6FB7`
- [SeCompareTokens](../8F/SeCompareTokens_function_008F6F40.md) at `0x008F6FD1`
- [PspAllocateAndQueryNotificationChannel](../91/PspAllocateAndQueryNotificationChannel_function_00917EE4.md) at `0x00918103`
- [PiDqOpenUserObjectRegKey](../99/PiDqOpenUserObjectRegKey_function_00990444.md) at `0x00990516`
- [CmpBuildAdminInformation](../9A/CmpBuildAdminInformation_function_009A8884.md) at `0x009A88BE`
- [ObpCaptureBoundaryDescriptor](../9C/ObpCaptureBoundaryDescriptor_function_009C9738.md) at `0x009C986B`
- [ObpCaptureBoundaryDescriptor](../9C/ObpCaptureBoundaryDescriptor_function_009C9738.md) at `0x009C99DA`
- [ObpVerifyCreatorAccessCheck](../9C/ObpVerifyCreatorAccessCheck_function_009CA524.md) at `0x009CA5B9`
- [ObpVerifyCreatorAccessCheck](../9C/ObpVerifyCreatorAccessCheck_function_009CA524.md) at `0x009CA5D4`
- [ObpVerifyCreatorAccessCheck](../9C/ObpVerifyCreatorAccessCheck_function_009CA524.md) at `0x009CA699`
- [SeQuerySigningPolicyWorker](../A1/SeQuerySigningPolicyWorker_function_00A13788.md) at `0x00A139DF`
- [PspAllocateProcess](../A1/PspAllocateProcess_function_00A13B3C.md) at `0x00A14BA7`
- [SeTokenIsElevated](../A2/SeTokenIsElevated_function_00A220FC.md) at `0x00A2212E`
- [AlpcpCheckConnectionSecurity](../A2/AlpcpCheckConnectionSecurity_function_00A227A0.md) at `0x00A2280F`
- [ObpGetIntegrityLevel](../A3/ObpGetIntegrityLevel_function_00A33F50.md) at `0x00A33F93`
- [PsIsProcessAppContainer](../A3/PsIsProcessAppContainer_function_00A38C44.md) at `0x00A38C71`
- [EtwpAcquireTokenAccessInformation](../A8/EtwpAcquireTokenAccessInformation_function_00A83AC0.md) at `0x00A83B4F`
- [EtwpTiQueryTokenIdentity](../A8/EtwpTiQueryTokenIdentity_function_00A87A7C.md) at `0x00A87A9F`
- [SepCheckCapabilities](../AA/SepCheckCapabilities_function_00AA4A10.md) at `0x00AA4A5B`
- [SepCheckCapabilities](../AA/SepCheckCapabilities_function_00AA4A10.md) at `0x00AA4A84`
- [SepCheckCapabilities](../AA/SepCheckCapabilities_function_00AA4A10.md) at `0x00AA4A9F`
- [SepCheckCapabilities](../AA/SepCheckCapabilities_function_00AA4A10.md) at `0x00AA4B92`

### Static image references
- `0x008B6314` → RVA `0x00E67BD8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **90**
  - `0x008B513C` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B5162` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B5173` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008B519D` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008B51A2` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008B51C9` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B51FC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B524B` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B5253` → [SepTokenPrivilegeCount](../../text/43/SepTokenPrivilegeCount_function_00432EC0.md) (`PAGE` → `.text`)
  - `0x008B527B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B5292` → [SepConvertTokenPrivileges](../../text/46/SepConvertTokenPrivileges_function_00463EF8.md) (`PAGE` → `.text`)
  - `0x008B52BA` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B530E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B5371` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008B5376` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008B53A1` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B53CA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B53DB` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008B53E0` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008B543E` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B5469` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B549A` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008B54D6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B5532` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B558B` → [SepTokenPrivilegeCount](../../text/43/SepTokenPrivilegeCount_function_00432EC0.md) (`PAGE` → `.text`)
  - `0x008B55A2` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008B55A7` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008B55D1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B5602` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B562B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B56D0` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B56DC` → [SepCopyTokenIntegrity](../../text/41/SepCopyTokenIntegrity_function_00419D10.md) (`PAGE` → `.text`)
  - `0x008B56E5` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (`PAGE` → `.text`)
  - `0x008B56FE` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x008B570C` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008B574B` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B57C2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B5882` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B58AD` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B58B5` → [SepGetTokenElevation](../../text/44/SepGetTokenElevation_function_0044F3C8.md) (`PAGE` → `.text`)
  - `0x008B58C0` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008B58C5` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008B58E1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B58F5` → [SepGetTokenElevationType](../../text/47/SepGetTokenElevationType_function_0047B1C4.md) (`PAGE` → `.text`)
  - `0x008B5922` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B592A` → [SepTokenPrivilegeCount](../../text/43/SepTokenPrivilegeCount_function_00432EC0.md) (`PAGE` → `.text`)
  - `0x008B59D1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B5AB9` → [SepConvertTokenPrivilegesToLuidAndAttributes](../../text/42/SepConvertTokenPrivilegesToLuidAndAttributes_function_0042A870.md) (`PAGE` → `.text`)
  - `0x008B5B5B` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B5BE8` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B5C16` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008B5C1B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008B5C29` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008B5C54` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B5C6C` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008B5C71` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008B5C98` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B5CC9` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B5D1C` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B5D6E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B5DDE` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B5E48` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B5EB3` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008B5EB8` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008B5EF1` → [SepCanTokenMatchAllPackageSid](../../text/2F/SepCanTokenMatchAllPackageSid_function_002FFE90.md) (`PAGE` → `.text`)
  - `0x008B5F29` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B5F53` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B5FBE` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B5FEF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B6068` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (`PAGE` → `.text`)
  - `0x008B608F` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B60B1` → [SepIsAppSuiteSid](../../text/60/SepIsAppSuiteSid_function_006083A0.md) (`PAGE` → `.text`)
  - `0x008B60DF` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B6123` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B6139` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (`PAGE` → `.text`)
  - `0x008B6160` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B61AB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B61D5` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (`PAGE` → `.text`)
  - `0x008B61FC` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B623D` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B626A` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008B6274` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x008B62A6` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008B62D5` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008B6330` → [SepSidInTokenSidHash](../../text/3C/SepSidInTokenSidHash_function_003C85E0.md) (`PAGE` → `.text`)
  - `0x008B6357` → [SepIsSandboxedToken](../../text/45/SepIsSandboxedToken_function_00458704.md) (`PAGE` → `.text`)
  - `0x008B6366` → [Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline_function_004F2D58.md) (`PAGE` → `.text`)
  - `0x008B6383` → [Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline_function_004F2D58.md) (`PAGE` → `.text`)
  - `0x008B63A2` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (`PAGE` → `.text`)
  - `0x008B63B2` → [SeHasTamperProtection](../../text/60/SeHasTamperProtection_function_0060777C.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008B5090  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
008B5095  55                              push rbp
008B5096  56                              push rsi
008B5097  57                              push rdi
008B5098  41 54                           push r12
008B509A  41 55                           push r13
008B509C  41 56                           push r14
008B509E  41 57                           push r15
008B50A0  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
008B50A5  48 81 EC E0 00 00 00            sub rsp, 0xe0
008B50AC  33 DB                           xor ebx, ebx
008B50AE  0F 57 C0                        xorps xmm0, xmm0
008B50B1  89 5D 6F                        mov dword ptr [rbp + 0x6f], ebx
008B50B4  4D 8B F8                        mov r15, r8
008B50B7  89 5D C7                        mov dword ptr [rbp - 0x39], ebx
008B50BA  8B F2                           mov esi, edx
008B50BC  48 8B F9                        mov rdi, rcx
008B50BF  0F 11 45 E7                     movups xmmword ptr [rbp - 0x19], xmm0
008B50C3  0F 11 45 F7                     movups xmmword ptr [rbp - 9], xmm0
008B50C7  0F 11 45 07                     movups xmmword ptr [rbp + 7], xmm0
008B50CB  83 FA 1D                        cmp edx, 0x1d
008B50CE  0F 8F 1D 0A 00 00               jg 0x1408b5af1
008B50D4  0F 84 E9 09 00 00               je 0x1408b5ac3
008B50DA  83 FA 0C                        cmp edx, 0xc
008B50DD  0F 8F 72 05 00 00               jg 0x1408b5655
008B50E3  0F 84 5F 05 00 00               je 0x1408b5648
008B50E9  83 FA 06                        cmp edx, 6
008B50EC  0F 8F B2 03 00 00               jg 0x1408b54a4
008B50F2  0F 84 2C 03 00 00               je 0x1408b5424
008B50F8  83 EE 01                        sub esi, 1
008B50FB  0F 84 82 02 00 00               je 0x1408b5383
008B5101  83 EE 01                        sub esi, 1
008B5104  0F 84 92 01 00 00               je 0x1408b529c
008B510A  83 EE 01                        sub esi, 1
008B510D  0F 84 1A 01 00 00               je 0x1408b522d
008B5113  83 EE 01                        sub esi, 1
008B5116  0F 84 93 00 00 00               je 0x1408b51af
008B511C  83 FE 01                        cmp esi, 1
008B511F  0F 85 7F 05 00 00               jne 0x1408b56a4
008B5125  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B512E  8B D6                           mov edx, esi
008B5130  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B5137  90                              nop
008B5138  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
008B513C  E8 7F CA 95 FF                  call 0x140211bc0
008B5141  48 8B 87 A8 00 00 00            mov rax, qword ptr [rdi + 0xa8]
008B5148  41 B8 53 65 20 20               mov r8d, 0x20206553
008B514E  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
008B5152  44 8D 34 8D 10 00 00 00         lea r14d, [rcx*4 + 0x10]
008B515A  B9 00 01 00 00                  mov ecx, 0x100
008B515F  41 8B D6                        mov edx, r14d
008B5162  E8 89 CF 2C 00                  call 0x140b820f0
008B5167  48 8B F0                        mov rsi, rax
008B516A  48 85 C0                        test rax, rax
008B516D  75 13                           jne 0x1408b5182
008B516F  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B5173  E8 98 A8 9A FF                  call 0x14025fa10
008B5178  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008B517D  E9 F2 10 00 00                  jmp 0x1408b6274
008B5182  48 8D 50 08                     lea rdx, [rax + 8]
008B5186  48 89 10                        mov qword ptr [rax], rdx
008B5189  4C 8B 87 A8 00 00 00            mov r8, qword ptr [rdi + 0xa8]
008B5190  41 8D 4E F8                     lea ecx, [r14 - 8]
008B5194  E8 B7 48 0F 00                  call 0x1409a9a50
008B5199  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B519D  E8 6E A8 9A FF                  call 0x14025fa10
008B51A2  E8 09 87 9A FF                  call 0x14025d8b0
008B51A7  49 89 37                        mov qword ptr [r15], rsi
008B51AA  E9 21 12 00 00                  jmp 0x1408b63d0
008B51AF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B51B8  BA 01 00 00 00                  mov edx, 1
008B51BD  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B51C4  90                              nop
008B51C5  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
008B51C9  E8 F2 C9 95 FF                  call 0x140211bc0
008B51CE  48 8B 87 98 00 00 00            mov rax, qword ptr [rdi + 0x98]
008B51D5  41 B8 53 65 20 20               mov r8d, 0x20206553
008B51DB  8B 8F 90 00 00 00               mov ecx, dword ptr [rdi + 0x90]
008B51E1  48 03 C9                        add rcx, rcx
008B51E4  48 8B 0C C8                     mov rcx, qword ptr [rax + rcx*8]
008B51E8  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
008B51EC  B9 00 01 00 00                  mov ecx, 0x100
008B51F1  44 8D 34 85 10 00 00 00         lea r14d, [rax*4 + 0x10]
008B51F9  41 8B D6                        mov edx, r14d
008B51FC  E8 EF CE 2C 00                  call 0x140b820f0
008B5201  48 8B F0                        mov rsi, rax
008B5204  48 85 C0                        test rax, rax
008B5207  0F 84 CA 01 00 00               je 0x1408b53d7
008B520D  48 8D 50 08                     lea rdx, [rax + 8]
008B5211  48 89 10                        mov qword ptr [rax], rdx
008B5214  8B 87 90 00 00 00               mov eax, dword ptr [rdi + 0x90]
008B521A  4C 8B 87 98 00 00 00            mov r8, qword ptr [rdi + 0x98]
008B5221  48 03 C0                        add rax, rax
008B5224  4D 8B 04 C0                     mov r8, qword ptr [r8 + rax*8]
008B5228  E9 63 FF FF FF                  jmp 0x1408b5190
008B522D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B5236  41 BE 01 00 00 00               mov r14d, 1
008B523C  41 8A D6                        mov dl, r14b
008B523F  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B5246  90                              nop
008B5247  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
008B524B  E8 70 C9 95 FF                  call 0x140211bc0
008B5250  48 8B CF                        mov rcx, rdi
008B5253  E8 68 DC B7 FF                  call 0x140432ec0
008B5258  41 3B C6                        cmp eax, r14d
008B525B  76 0C                           jbe 0x1408b5269
008B525D  8D 04 40                        lea eax, [rax + rax*2]
008B5260  8D 34 85 04 00 00 00            lea esi, [rax*4 + 4]
008B5267  EB 05                           jmp 0x1408b526e
008B5269  BE 10 00 00 00                  mov esi, 0x10
008B526E  8B D6                           mov edx, esi
008B5270  B9 00 01 00 00                  mov ecx, 0x100
008B5275  41 B8 53 65 20 20               mov r8d, 0x20206553
008B527B  E8 70 CE 2C 00                  call 0x140b820f0
008B5280  48 8B F0                        mov rsi, rax
008B5283  48 85 C0                        test rax, rax
008B5286  0F 84 4B 01 00 00               je 0x1408b53d7
008B528C  48 8B D0                        mov rdx, rax
008B528F  48 8B CF                        mov rcx, rdi
008B5292  E8 61 EC BA FF                  call 0x140463ef8
008B5297  E9 FD FE FF FF                  jmp 0x1408b5199
008B529C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B52A5  41 BE 01 00 00 00               mov r14d, 1
008B52AB  41 8A D6                        mov dl, r14b
008B52AE  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B52B5  90                              nop
008B52B6  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
008B52BA  E8 01 C9 95 FF                  call 0x140211bc0
008B52BF  8B 4F 7C                        mov ecx, dword ptr [rdi + 0x7c]
008B52C2  41 8D 76 0F                     lea esi, [r14 + 0xf]
008B52C6  44 8B E1                        mov r12d, ecx
008B52C9  41 C1 E4 04                     shl r12d, 4
008B52CD  41 83 C4 F8                     add r12d, -8
008B52D1  41 8B C4                        mov eax, r12d
008B52D4  41 3B CE                        cmp ecx, r14d
008B52D7  76 28                           jbe 0x1408b5301
008B52D9  48 8B 97 98 00 00 00            mov rdx, qword ptr [rdi + 0x98]
008B52E0  44 8D 41 FF                     lea r8d, [rcx - 1]
008B52E4  48 03 D6                        add rdx, rsi
008B52E7  48 8B 02                        mov rax, qword ptr [rdx]
008B52EA  48 03 D6                        add rdx, rsi
008B52ED  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
008B52F1  45 8D 24 8C                     lea r12d, [r12 + rcx*4]
008B52F5  41 83 C4 08                     add r12d, 8
008B52F9  41 8B C4                        mov eax, r12d
008B52FC  4D 2B C6                        sub r8, r14
008B52FF  75 E6                           jne 0x1408b52e7
008B5301  8B D0                           mov edx, eax
008B5303  B9 00 01 00 00                  mov ecx, 0x100
008B5308  41 B8 53 65 20 20               mov r8d, 0x20206553
008B530E  E8 DD CD 2C 00                  call 0x140b820f0
008B5313  4C 8B E8                        mov r13, rax
008B5316  48 85 C0                        test rax, rax
008B5319  0F 84 B8 00 00 00               je 0x1408b53d7
008B531F  8B 47 7C                        mov eax, dword ptr [rdi + 0x7c]
008B5322  4D 8D 4D 08                     lea r9, [r13 + 8]
008B5326  41 2B C6                        sub eax, r14d
008B5329  45 8B C4                        mov r8d, r12d
008B532C  41 89 45 00                     mov dword ptr [r13], eax
008B5330  48 8D 45 67                     lea rax, [rbp + 0x67]
008B5334  8B 4F 7C                        mov ecx, dword ptr [rdi + 0x7c]
008B5337  44 8B D1                        mov r10d, ecx
008B533A  48 8B 97 98 00 00 00            mov rdx, qword ptr [rdi + 0x98]
008B5341  41 C1 E2 04                     shl r10d, 4
008B5345  48 03 D6                        add rdx, rsi
008B5348  41 83 EA 20                     sub r10d, 0x20
008B534C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008B5351  49 83 C2 18                     add r10, 0x18
008B5355  48 8D 45 67                     lea rax, [rbp + 0x67]
008B5359  4D 03 D5                        add r10, r13
008B535C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008B5361  FF C9                           dec ecx
008B5363  4C 89 54 24 20                  mov qword ptr [rsp + 0x20], r10
008B5368  E8 73 38 0F 00                  call 0x1409a8be0
008B536D  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B5371  E8 9A A6 9A FF                  call 0x14025fa10
008B5376  E8 35 85 9A FF                  call 0x14025d8b0
008B537B  4D 89 2F                        mov qword ptr [r15], r13
008B537E  E9 4D 10 00 00                  jmp 0x1408b63d0
008B5383  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B538C  41 BE 01 00 00 00               mov r14d, 1
008B5392  41 8A D6                        mov dl, r14b
008B5395  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B539C  90                              nop
008B539D  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
008B53A1  E8 1A C8 95 FF                  call 0x140211bc0
008B53A6  48 8B 87 98 00 00 00            mov rax, qword ptr [rdi + 0x98]
008B53AD  41 B8 53 65 20 20               mov r8d, 0x20206553
008B53B3  48 8B 08                        mov rcx, qword ptr [rax]
008B53B6  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
008B53BA  B9 00 01 00 00                  mov ecx, 0x100
008B53BF  44 8D 24 85 18 00 00 00         lea r12d, [rax*4 + 0x18]
008B53C7  41 8B D4                        mov edx, r12d
008B53CA  E8 21 CD 2C 00                  call 0x140b820f0
008B53CF  48 8B F0                        mov rsi, rax
008B53D2  48 85 C0                        test rax, rax
008B53D5  75 18                           jne 0x1408b53ef
008B53D7  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B53DB  E8 30 A6 9A FF                  call 0x14025fa10
008B53E0  E8 CB 84 9A FF                  call 0x14025d8b0
008B53E5  B8 9A 00 00 C0                  mov eax, 0xc000009a
008B53EA  E9 E3 0F 00 00                  jmp 0x1408b63d2
008B53EF  48 8B 97 98 00 00 00            mov rdx, qword ptr [rdi + 0x98]
008B53F6  48 8D 4D 67                     lea rcx, [rbp + 0x67]
008B53FA  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
008B53FF  48 83 C0 10                     add rax, 0x10
008B5403  48 8D 4D 67                     lea rcx, [rbp + 0x67]
008B5407  4C 8B CE                        mov r9, rsi
008B540A  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
008B540F  41 8B CE                        mov ecx, r14d
008B5412  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B5417  45 8B C4                        mov r8d, r12d
008B541A  E8 C1 37 0F 00                  call 0x1409a8be0
008B541F  E9 75 FD FF FF                  jmp 0x1408b5199
008B5424  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B542D  BA 01 00 00 00                  mov edx, 1
008B5432  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B5439  90                              nop
008B543A  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
008B543E  E8 7D C7 95 FF                  call 0x140211bc0
008B5443  48 8B 87 B8 00 00 00            mov rax, qword ptr [rdi + 0xb8]
008B544A  BE 08 00 00 00                  mov esi, 8
008B544F  48 85 C0                        test rax, rax
008B5452  74 07                           je 0x1408b545b
008B5454  0F B7 40 02                     movzx eax, word ptr [rax + 2]
008B5458  48 03 F0                        add rsi, rax
008B545B  41 B8 53 65 20 20               mov r8d, 0x20206553
008B5461  48 8B D6                        mov rdx, rsi
008B5464  B9 00 01 00 00                  mov ecx, 0x100
008B5469  E8 82 CC 2C 00                  call 0x140b820f0
008B546E  48 8B F0                        mov rsi, rax
008B5471  48 85 C0                        test rax, rax
008B5474  0F 84 F5 FC FF FF               je 0x1408b516f
008B547A  48 8D 48 08                     lea rcx, [rax + 8]
008B547E  48 39 9F B8 00 00 00            cmp qword ptr [rdi + 0xb8], rbx
008B5485  0F 84 05 0B 00 00               je 0x1408b5f90
008B548B  48 89 08                        mov qword ptr [rax], rcx
008B548E  48 8B 97 B8 00 00 00            mov rdx, qword ptr [rdi + 0xb8]
008B5495  44 0F B7 42 02                  movzx r8d, word ptr [rdx + 2]
008B549A  E8 A1 13 E1 FF                  call 0x1406c6840
008B549F  E9 F5 FC FF FF                  jmp 0x1408b5199
008B54A4  83 EE 07                        sub esi, 7
008B54A7  0F 84 6E 01 00 00               je 0x1408b561b
008B54AD  83 EE 01                        sub esi, 1
008B54B0  0F 84 3C 01 00 00               je 0x1408b55f2
008B54B6  83 EE 01                        sub esi, 1
008B54B9  0F 84 F5 00 00 00               je 0x1408b55b4
008B54BF  83 FE 01                        cmp esi, 1
008B54C2  0F 85 DC 01 00 00               jne 0x1408b56a4
008B54C8  8D 56 37                        lea edx, [rsi + 0x37]
008B54CB  B9 00 01 00 00                  mov ecx, 0x100
008B54D0  41 B8 53 65 20 20               mov r8d, 0x20206553
008B54D6  E8 15 CC 2C 00                  call 0x140b820f0
008B54DB  4C 8B E0                        mov r12, rax
008B54DE  48 85 C0                        test rax, rax
008B54E1  0F 84 FE FE FF FF               je 0x1408b53e5
008B54E7  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
008B54EB  44 8B F6                        mov r14d, esi
008B54EE  49 89 04 24                     mov qword ptr [r12], rax
008B54F2  41 8A D6                        mov dl, r14b
008B54F5  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
008B54F9  49 89 44 24 08                  mov qword ptr [r12 + 8], rax
008B54FE  8B 87 C0 00 00 00               mov eax, dword ptr [rdi + 0xc0]
008B5504  41 89 44 24 18                  mov dword ptr [r12 + 0x18], eax
008B5509  8B 87 C4 00 00 00               mov eax, dword ptr [rdi + 0xc4]
008B550F  41 89 44 24 1C                  mov dword ptr [r12 + 0x1c], eax
008B5514  48 8B 47 28                     mov rax, qword ptr [rdi + 0x28]
008B5518  49 89 44 24 10                  mov qword ptr [r12 + 0x10], rax
008B551D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B5526  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B552D  90                              nop
008B552E  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B5532  E8 89 C6 95 FF                  call 0x140211bc0
008B5537  8B 87 88 00 00 00               mov eax, dword ptr [rdi + 0x88]
008B553D  41 89 44 24 20                  mov dword ptr [r12 + 0x20], eax
008B5542  48 8B 87 A8 00 00 00            mov rax, qword ptr [rdi + 0xa8]
008B5549  8B 97 88 00 00 00               mov edx, dword ptr [rdi + 0x88]
008B554F  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
008B5553  48 8B 87 B8 00 00 00            mov rax, qword ptr [rdi + 0xb8]
008B555A  C1 E1 02                        shl ecx, 2
008B555D  2B D1                           sub edx, ecx
008B555F  83 EA 08                        sub edx, 8
008B5562  48 85 C0                        test rax, rax
008B5565  74 06                           je 0x1408b556d
008B5567  0F B7 40 02                     movzx eax, word ptr [rax + 2]
008B556B  2B D0                           sub edx, eax
008B556D  41 89 54 24 24                  mov dword ptr [r12 + 0x24], edx
008B5572  48 8B CF                        mov rcx, rdi
008B5575  8B 87 8C 00 00 00               mov eax, dword ptr [rdi + 0x8c]
008B557B  41 89 44 24 24                  mov dword ptr [r12 + 0x24], eax
008B5580  8B 47 7C                        mov eax, dword ptr [rdi + 0x7c]
008B5583  41 2B C6                        sub eax, r14d
008B5586  41 89 44 24 28                  mov dword ptr [r12 + 0x28], eax
008B558B  E8 30 D9 B7 FF                  call 0x140432ec0
008B5590  41 89 44 24 2C                  mov dword ptr [r12 + 0x2c], eax
008B5595  48 8B 47 38                     mov rax, qword ptr [rdi + 0x38]
008B5599  49 89 44 24 30                  mov qword ptr [r12 + 0x30], rax
008B559E  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B55A2  E8 69 A4 9A FF                  call 0x14025fa10
008B55A7  E8 04 83 9A FF                  call 0x14025d8b0
008B55AC  4D 89 27                        mov qword ptr [r15], r12
008B55AF  E9 1C 0E 00 00                  jmp 0x1408b63d0
008B55B4  83 B9 C0 00 00 00 02            cmp dword ptr [rcx + 0xc0], 2
008B55BB  0F 85 E3 00 00 00               jne 0x1408b56a4
008B55C1  BA 04 00 00 00                  mov edx, 4
008B55C6  B9 00 01 00 00                  mov ecx, 0x100
008B55CB  41 B8 53 65 20 20               mov r8d, 0x20206553
008B55D1  E8 1A CB 2C 00                  call 0x140b820f0
008B55D6  48 8B C8                        mov rcx, rax
008B55D9  48 85 C0                        test rax, rax
008B55DC  0F 84 03 FE FF FF               je 0x1408b53e5
008B55E2  8B 87 C4 00 00 00               mov eax, dword ptr [rdi + 0xc4]
008B55E8  89 01                           mov dword ptr [rcx], eax
008B55EA  49 89 0F                        mov qword ptr [r15], rcx
008B55ED  E9 DE 0D 00 00                  jmp 0x1408b63d0
008B55F2  BA 04 00 00 00                  mov edx, 4
008B55F7  B9 00 01 00 00                  mov ecx, 0x100
008B55FC  41 B8 53 65 20 20               mov r8d, 0x20206553
008B5602  E8 E9 CA 2C 00                  call 0x140b820f0
008B5607  48 8B C8                        mov rcx, rax
008B560A  48 85 C0                        test rax, rax
008B560D  0F 84 D2 FD FF FF               je 0x1408b53e5
008B5613  8B 87 C0 00 00 00               mov eax, dword ptr [rdi + 0xc0]
008B5619  EB CD                           jmp 0x1408b55e8
008B561B  BA 10 00 00 00                  mov edx, 0x10
008B5620  B9 00 01 00 00                  mov ecx, 0x100
008B5625  41 B8 53 65 20 20               mov r8d, 0x20206553
008B562B  E8 C0 CA 2C 00                  call 0x140b820f0
008B5630  48 85 C0                        test rax, rax
008B5633  0F 84 AC FD FF FF               je 0x1408b53e5
008B5639  0F 10 07                        movups xmm0, xmmword ptr [rdi]
008B563C  F3 0F 7F 00                     movdqu xmmword ptr [rax], xmm0
008B5640  49 89 07                        mov qword ptr [r15], rax
008B5643  E9 88 0D 00 00                  jmp 0x1408b63d0
008B5648  49 8B D7                        mov rdx, r15
008B564B  E8 40 EE 14 00                  call 0x140a04490
008B5650  E9 7B 0D 00 00                  jmp 0x1408b63d0
008B5655  8B CE                           mov ecx, esi
008B5657  83 E9 0D                        sub ecx, 0xd
008B565A  0F 84 A4 02 00 00               je 0x1408b5904
008B5660  83 E9 05                        sub ecx, 5
008B5663  0F 84 68 02 00 00               je 0x1408b58d1
008B5669  83 E9 02                        sub ecx, 2
008B566C  0F 84 00 02 00 00               je 0x1408b5872
008B5672  83 E9 01                        sub ecx, 1
008B5675  0F 84 B7 01 00 00               je 0x1408b5832
008B567B  83 E9 01                        sub ecx, 1
008B567E  0F 84 92 00 00 00               je 0x1408b5716
008B5684  83 E9 01                        sub ecx, 1
008B5687  0F 84 A5 01 00 00               je 0x1408b5832
008B568D  83 E9 01                        sub ecx, 1
008B5690  0F 84 9C 01 00 00               je 0x1408b5832
008B5696  83 E9 01                        sub ecx, 1
008B5699  74 13                           je 0x1408b56ae
008B569B  83 F9 01                        cmp ecx, 1
008B569E  0F 84 8E 01 00 00               je 0x1408b5832
008B56A4  B8 03 00 00 C0                  mov eax, 0xc0000003
008B56A9  E9 24 0D 00 00                  jmp 0x1408b63d2
008B56AE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B56B7  41 BE 01 00 00 00               mov r14d, 1
008B56BD  41 8A D6                        mov dl, r14b
008B56C0  0F 11 45 17                     movups xmmword ptr [rbp + 0x17], xmm0
008B56C4  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B56CB  90                              nop
008B56CC  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B56D0  E8 EB C4 95 FF                  call 0x140211bc0
008B56D5  48 8D 55 17                     lea rdx, [rbp + 0x17]
008B56D9  48 8B CF                        mov rcx, rdi
008B56DC  E8 2F 46 B6 FF                  call 0x140419d10
008B56E1  48 8B 4D 17                     mov rcx, qword ptr [rbp + 0x17]
008B56E5  E8 26 38 BB FF                  call 0x140468f10
008B56EA  0F B6 08                        movzx ecx, byte ptr [rax]
008B56ED  84 C9                           test cl, cl
008B56EF  75 04                           jne 0x1408b56f5
008B56F1  8B C3                           mov eax, ebx
008B56F3  EB 10                           jmp 0x1408b5705
008B56F5  8B D1                           mov edx, ecx
008B56F7  48 8B 4D 17                     mov rcx, qword ptr [rbp + 0x17]
008B56FB  41 2B D6                        sub edx, r14d
008B56FE  E8 0D 16 BA FF                  call 0x140456d10
008B5703  8B 00                           mov eax, dword ptr [rax]
008B5705  41 89 07                        mov dword ptr [r15], eax
008B5708  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B570C  E8 FF A2 9A FF                  call 0x14025fa10
008B5711  E9 5E 0B 00 00                  jmp 0x1408b6274
008B5716  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B571F  BA 01 00 00 00                  mov edx, 1
008B5724  89 5D DF                        mov dword ptr [rbp - 0x21], ebx
008B5727  89 5D DB                        mov dword ptr [rbp - 0x25], ebx
008B572A  89 5D D7                        mov dword ptr [rbp - 0x29], ebx
008B572D  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B5734  90                              nop
008B5735  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B5739  89 5D D3                        mov dword ptr [rbp - 0x2d], ebx
008B573C  89 5D CF                        mov dword ptr [rbp - 0x31], ebx
008B573F  89 5D CB                        mov dword ptr [rbp - 0x35], ebx
008B5742  89 5D 7F                        mov dword ptr [rbp + 0x7f], ebx
008B5745  89 5D 67                        mov dword ptr [rbp + 0x67], ebx
008B5748  89 5D 6F                        mov dword ptr [rbp + 0x6f], ebx
008B574B  E8 70 C4 95 FF                  call 0x140211bc0
008B5750  48 8D 45 6F                     lea rax, [rbp + 0x6f]
008B5754  45 33 C0                        xor r8d, r8d
008B5757  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
008B575C  4C 8D 4D C7                     lea r9, [rbp - 0x39]
008B5760  48 8D 45 67                     lea rax, [rbp + 0x67]
008B5764  33 D2                           xor edx, edx
008B5766  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
008B576B  48 8B CF                        mov rcx, rdi
008B576E  48 8D 45 7F                     lea rax, [rbp + 0x7f]
008B5772  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
008B5777  48 8D 45 CB                     lea rax, [rbp - 0x35]
008B577B  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008B5780  48 8D 45 CF                     lea rax, [rbp - 0x31]
008B5784  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
008B5789  48 8D 45 D3                     lea rax, [rbp - 0x2d]
008B578D  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
008B5792  48 8D 45 D7                     lea rax, [rbp - 0x29]
008B5796  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008B579B  48 8D 45 DB                     lea rax, [rbp - 0x25]
008B579F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008B57A4  48 8D 45 DF                     lea rax, [rbp - 0x21]
008B57A8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B57AD  E8 AA 41 13 00                  call 0x1409e995c
008B57B2  8B D0                           mov edx, eax
008B57B4  B9 00 01 00 00                  mov ecx, 0x100
008B57B9  41 B8 53 65 20 20               mov r8d, 0x20206553
008B57BF  44 8B F0                        mov r14d, eax
008B57C2  E8 29 C9 2C 00                  call 0x140b820f0
008B57C7  48 8B F0                        mov rsi, rax
008B57CA  48 85 C0                        test rax, rax
008B57CD  0F 84 04 FC FF FF               je 0x1408b53d7
008B57D3  8B 45 6F                        mov eax, dword ptr [rbp + 0x6f]
008B57D6  45 8B C6                        mov r8d, r14d
008B57D9  44 8B 4D C7                     mov r9d, dword ptr [rbp - 0x39]
008B57DD  48 8B D6                        mov rdx, rsi
008B57E0  48 89 5C 24 70                  mov qword ptr [rsp + 0x70], rbx
008B57E5  48 8B CF                        mov rcx, rdi
008B57E8  88 5C 24 68                     mov byte ptr [rsp + 0x68], bl
008B57EC  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
008B57F0  8B 45 67                        mov eax, dword ptr [rbp + 0x67]
008B57F3  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
008B57F7  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
008B57FA  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008B57FE  8B 45 CB                        mov eax, dword ptr [rbp - 0x35]
008B5801  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
008B5805  8B 45 CF                        mov eax, dword ptr [rbp - 0x31]
008B5808  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
008B580C  8B 45 D3                        mov eax, dword ptr [rbp - 0x2d]
008B580F  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
008B5813  8B 45 D7                        mov eax, dword ptr [rbp - 0x29]
008B5816  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
008B581A  8B 45 DB                        mov eax, dword ptr [rbp - 0x25]
008B581D  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
008B5821  8B 45 DF                        mov eax, dword ptr [rbp - 0x21]
008B5824  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008B5828  E8 DF 43 13 00                  call 0x1409e9c0c
008B582D  E9 67 F9 FF FF                  jmp 0x1408b5199
008B5832  83 FE 17                        cmp esi, 0x17
008B5835  75 11                           jne 0x1408b5848
008B5837  8B 87 C8 00 00 00               mov eax, dword ptr [rdi + 0xc8]
008B583D  C1 E8 09                        shr eax, 9
008B5840  83 E0 01                        and eax, 1
008B5843  E9 85 0B 00 00                  jmp 0x1408b63cd
008B5848  41 BC 18 00 00 00               mov r12d, 0x18
008B584E  41 3B F4                        cmp esi, r12d
008B5851  75 0B                           jne 0x1408b585e
008B5853  8B 87 C8 00 00 00               mov eax, dword ptr [rdi + 0xc8]
008B5859  C1 E8 0A                        shr eax, 0xa
008B585C  EB E2                           jmp 0x1408b5840
008B585E  83 FE 1A                        cmp esi, 0x1a
008B5861  0F 85 5C 02 00 00               jne 0x1408b5ac3
008B5867  8B 87 C8 00 00 00               mov eax, dword ptr [rdi + 0xc8]
008B586D  C1 E8 0C                        shr eax, 0xc
008B5870  EB CE                           jmp 0x1408b5840
008B5872  BA 04 00 00 00                  mov edx, 4
008B5877  B9 00 01 00 00                  mov ecx, 0x100
008B587C  41 B8 53 65 20 20               mov r8d, 0x20206553
008B5882  E8 69 C8 2C 00                  call 0x140b820f0
008B5887  48 8B F0                        mov rsi, rax
008B588A  48 85 C0                        test rax, rax
008B588D  0F 84 52 FB FF FF               je 0x1408b53e5
008B5893  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B589C  BA 01 00 00 00                  mov edx, 1
008B58A1  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B58A8  90                              nop
008B58A9  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B58AD  E8 0E C3 95 FF                  call 0x140211bc0
008B58B2  48 8B CF                        mov rcx, rdi
008B58B5  E8 0E 9B B9 FF                  call 0x14044f3c8
008B58BA  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B58BE  8B D8                           mov ebx, eax
008B58C0  E8 4B A1 9A FF                  call 0x14025fa10
008B58C5  E8 E6 7F 9A FF                  call 0x14025d8b0
008B58CA  89 1E                           mov dword ptr [rsi], ebx
008B58CC  E9 D6 F8 FF FF                  jmp 0x1408b51a7
008B58D1  BA 04 00 00 00                  mov edx, 4
008B58D6  B9 00 01 00 00                  mov ecx, 0x100
008B58DB  41 B8 53 65 20 20               mov r8d, 0x20206553
008B58E1  E8 0A C8 2C 00                  call 0x140b820f0
008B58E6  48 8B D0                        mov rdx, rax
008B58E9  48 85 C0                        test rax, rax
008B58EC  0F 84 F3 FA FF FF               je 0x1408b53e5
008B58F2  48 8B CF                        mov rcx, rdi
008B58F5  E8 CA 58 BC FF                  call 0x14047b1c4
008B58FA  89 02                           mov dword ptr [rdx], eax
008B58FC  49 89 17                        mov qword ptr [r15], rdx
008B58FF  E9 CC 0A 00 00                  jmp 0x1408b63d0
008B5904  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B590D  41 BE 01 00 00 00               mov r14d, 1
008B5913  41 8A D6                        mov dl, r14b
008B5916  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B591D  90                              nop
008B591E  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B5922  E8 99 C2 95 FF                  call 0x140211bc0
008B5927  48 8B CF                        mov rcx, rdi
008B592A  E8 91 D5 B7 FF                  call 0x140432ec0
008B592F  8B 4F 7C                        mov ecx, dword ptr [rdi + 0x7c]
008B5932  41 8D 76 0F                     lea esi, [r14 + 0xf]
008B5936  89 45 67                        mov dword ptr [rbp + 0x67], eax
008B5939  41 BA F8 FF FF FF               mov r10d, 0xfffffff8
008B593F  44 8D 0C 40                     lea r9d, [rax + rax*2]
008B5943  8B C1                           mov eax, ecx
008B5945  C1 E0 04                        shl eax, 4
008B5948  41 C1 E1 02                     shl r9d, 2
008B594C  44 8B E8                        mov r13d, eax
008B594F  44 89 4D 6F                     mov dword ptr [rbp + 0x6f], r9d
008B5953  89 45 7F                        mov dword ptr [rbp + 0x7f], eax
008B5956  85 C9                           test ecx, ecx
008B5958  74 26                           je 0x1408b5980
008B595A  48 8B 97 98 00 00 00            mov rdx, qword ptr [rdi + 0x98]
008B5961  44 8B C1                        mov r8d, ecx
008B5964  48 8B 02                        mov rax, qword ptr [rdx]
008B5967  48 03 D6                        add rdx, rsi
008B596A  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
008B596E  8D 0C 8D 0F 00 00 00            lea ecx, [rcx*4 + 0xf]
008B5975  41 23 CA                        and ecx, r10d
008B5978  44 03 E9                        add r13d, ecx
008B597B  4D 2B C6                        sub r8, r14
008B597E  75 E4                           jne 0x1408b5964
008B5980  8B 8F 80 00 00 00               mov ecx, dword ptr [rdi + 0x80]
008B5986  8B C1                           mov eax, ecx
008B5988  C1 E0 04                        shl eax, 4
008B598B  89 45 C7                        mov dword ptr [rbp - 0x39], eax
008B598E  44 8B E0                        mov r12d, eax
008B5991  85 C9                           test ecx, ecx
008B5993  74 26                           je 0x1408b59bb
008B5995  48 8B 97 A0 00 00 00            mov rdx, qword ptr [rdi + 0xa0]
008B599C  44 8B C1                        mov r8d, ecx
008B599F  48 8B 02                        mov rax, qword ptr [rdx]
008B59A2  48 03 D6                        add rdx, rsi
008B59A5  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
008B59A9  8D 0C 8D 0F 00 00 00            lea ecx, [rcx*4 + 0xf]
008B59B0  41 23 CA                        and ecx, r10d
008B59B3  44 03 E1                        add r12d, ecx
008B59B6  4D 2B C6                        sub r8, r14
008B59B9  75 E4                           jne 0x1408b599f
008B59BB  43 8D 14 2C                     lea edx, [r12 + r13]
008B59BF  41 83 C1 38                     add r9d, 0x38
008B59C3  41 03 D1                        add edx, r9d
008B59C6  B9 00 01 00 00                  mov ecx, 0x100
008B59CB  41 B8 53 65 20 20               mov r8d, 0x20206553
008B59D1  E8 1A C7 2C 00                  call 0x140b820f0
008B59D6  48 8B F0                        mov rsi, rax
008B59D9  48 85 C0                        test rax, rax
008B59DC  0F 84 F5 F9 FF FF               je 0x1408b53d7
008B59E2  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
008B59E6  4C 8D 4E 38                     lea r9, [rsi + 0x38]
008B59EA  48 89 46 30                     mov qword ptr [rsi + 0x30], rax
008B59EE  44 89 6E 04                     mov dword ptr [rsi + 4], r13d
008B59F2  8B 47 7C                        mov eax, dword ptr [rdi + 0x7c]
008B59F5  89 06                           mov dword ptr [rsi], eax
008B59F7  4C 89 4E 08                     mov qword ptr [rsi + 8], r9
008B59FB  44 89 66 14                     mov dword ptr [rsi + 0x14], r12d
008B59FF  8B 87 80 00 00 00               mov eax, dword ptr [rdi + 0x80]
008B5A05  89 46 10                        mov dword ptr [rsi + 0x10], eax
008B5A08  41 8B CD                        mov ecx, r13d
008B5A0B  39 9F 80 00 00 00               cmp dword ptr [rdi + 0x80], ebx
008B5A11  74 0D                           je 0x1408b5a20
008B5A13  48 8D 41 07                     lea rax, [rcx + 7]
008B5A17  48 83 E0 F8                     and rax, 0xfffffffffffffff8
008B5A1B  49 03 C1                        add rax, r9
008B5A1E  EB 03                           jmp 0x1408b5a23
008B5A20  48 8B C3                        mov rax, rbx
008B5A23  48 89 46 18                     mov qword ptr [rsi + 0x18], rax
008B5A27  8B 45 6F                        mov eax, dword ptr [rbp + 0x6f]
008B5A2A  89 46 24                        mov dword ptr [rsi + 0x24], eax
008B5A2D  8B 45 67                        mov eax, dword ptr [rbp + 0x67]
008B5A30  89 46 20                        mov dword ptr [rsi + 0x20], eax
008B5A33  41 8B C4                        mov eax, r12d
008B5A36  48 03 C1                        add rax, rcx
008B5A39  8B 4D 7F                        mov ecx, dword ptr [rbp + 0x7f]
008B5A3C  44 2B E9                        sub r13d, ecx
008B5A3F  49 03 C1                        add rax, r9
008B5A42  48 89 46 28                     mov qword ptr [rsi + 0x28], rax
008B5A46  45 8B C5                        mov r8d, r13d
008B5A49  48 8B 97 98 00 00 00            mov rdx, qword ptr [rdi + 0x98]
008B5A50  49 8D 04 09                     lea rax, [r9 + rcx]
008B5A54  48 8D 4D 67                     lea rcx, [rbp + 0x67]
008B5A58  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
008B5A5D  48 8D 4D 67                     lea rcx, [rbp + 0x67]
008B5A61  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
008B5A66  8B 4F 7C                        mov ecx, dword ptr [rdi + 0x7c]
008B5A69  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B5A6E  E8 6D 31 0F 00                  call 0x1409a8be0
008B5A73  39 5E 10                        cmp dword ptr [rsi + 0x10], ebx
008B5A76  76 3A                           jbe 0x1408b5ab2
008B5A78  8B 4D C7                        mov ecx, dword ptr [rbp - 0x39]
008B5A7B  4C 8B 4E 18                     mov r9, qword ptr [rsi + 0x18]
008B5A7F  44 2B E1                        sub r12d, ecx
008B5A82  48 8B 97 A0 00 00 00            mov rdx, qword ptr [rdi + 0xa0]
008B5A89  45 8B C4                        mov r8d, r12d
008B5A8C  49 8D 04 09                     lea rax, [r9 + rcx]
008B5A90  48 8D 4D 67                     lea rcx, [rbp + 0x67]
008B5A94  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
008B5A99  48 8D 4D 67                     lea rcx, [rbp + 0x67]
008B5A9D  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
008B5AA2  8B 8F 80 00 00 00               mov ecx, dword ptr [rdi + 0x80]
008B5AA8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B5AAD  E8 2E 31 0F 00                  call 0x1409a8be0
008B5AB2  48 8B 56 28                     mov rdx, qword ptr [rsi + 0x28]
008B5AB6  48 8B CF                        mov rcx, rdi
008B5AB9  E8 B2 4D B7 FF                  call 0x14042a870
008B5ABE  E9 D6 F6 FF FF                  jmp 0x1408b5199
008B5AC3  83 FE 1D                        cmp esi, 0x1d
008B5AC6  75 0E                           jne 0x1408b5ad6
008B5AC8  8B 87 C8 00 00 00               mov eax, dword ptr [rdi + 0xc8]
008B5ACE  C1 E8 0E                        shr eax, 0xe
008B5AD1  E9 6A FD FF FF                  jmp 0x1408b5840
008B5AD6  83 FE 15                        cmp esi, 0x15
008B5AD9  0F 85 E0 08 00 00               jne 0x1408b63bf
008B5ADF  F7 87 C8 00 00 00 10 08 00 00   test dword ptr [rdi + 0xc8], 0x810
008B5AE9  0F 95 C0                        setne al
008B5AEC  E9 6B 08 00 00                  jmp 0x1408b635c
008B5AF1  83 FE 2F                        cmp esi, 0x2f
008B5AF4  0F 8F 1B 05 00 00               jg 0x1408b6015
008B5AFA  0F 84 45 08 00 00               je 0x1408b6345
008B5B00  83 FE 25                        cmp esi, 0x25
008B5B03  0F 8F BC 03 00 00               jg 0x1408b5ec5
008B5B09  0F 84 B1 02 00 00               je 0x1408b5dc0
008B5B0F  8B CE                           mov ecx, esi
008B5B11  83 E9 1E                        sub ecx, 0x1e
008B5B14  0F 84 E4 01 00 00               je 0x1408b5cfe
008B5B1A  83 E9 01                        sub ecx, 1
008B5B1D  0F 84 5B 01 00 00               je 0x1408b5c7e
008B5B23  83 E9 01                        sub ecx, 1
008B5B26  0F 84 0E 01 00 00               je 0x1408b5c3a
008B5B2C  83 E9 01                        sub ecx, 1
008B5B2F  74 09                           je 0x1408b5b3a
008B5B31  83 F9 01                        cmp ecx, 1
008B5B34  0F 85 6A FB FF FF               jne 0x1408b56a4
008B5B3A  49 89 18                        mov qword ptr [r8], rbx
008B5B3D  4C 8D 67 30                     lea r12, [rdi + 0x30]
008B5B41  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B5B4A  BA 01 00 00 00                  mov edx, 1
008B5B4F  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B5B56  90                              nop
008B5B57  49 8B 0C 24                     mov rcx, qword ptr [r12]
008B5B5B  E8 60 C0 95 FF                  call 0x140211bc0
008B5B60  48 8B 87 48 04 00 00            mov rax, qword ptr [rdi + 0x448]
008B5B67  48 85 C0                        test rax, rax
008B5B6A  74 43                           je 0x1408b5baf
008B5B6C  48 8B 88 40 02 00 00            mov rcx, qword ptr [rax + 0x240]
008B5B73  48 85 C9                        test rcx, rcx
008B5B76  75 09                           jne 0x1408b5b81
008B5B78  83 FE 21                        cmp esi, 0x21
008B5B7B  74 32                           je 0x1408b5baf
008B5B7D  4C 8D 67 30                     lea r12, [rdi + 0x30]
008B5B81  48 8B B8 48 02 00 00            mov rdi, qword ptr [rax + 0x248]
008B5B88  48 85 FF                        test rdi, rdi
008B5B8B  75 05                           jne 0x1408b5b92
008B5B8D  83 FE 22                        cmp esi, 0x22
008B5B90  74 1D                           je 0x1408b5baf
008B5B92  83 FE 21                        cmp esi, 0x21
008B5B95  4C 8D 4D 6F                     lea r9, [rbp + 0x6f]
008B5B99  48 0F 44 F9                     cmove rdi, rcx
008B5B9D  45 33 C0                        xor r8d, r8d
008B5BA0  48 8B CF                        mov rcx, rdi
008B5BA3  33 D2                           xor edx, edx
008B5BA5  E8 62 27 16 00                  call 0x140a1830c
008B5BAA  8B 75 6F                        mov esi, dword ptr [rbp + 0x6f]
008B5BAD  EB 2C                           jmp 0x1408b5bdb
008B5BAF  48 8D 45 EF                     lea rax, [rbp - 0x11]
008B5BB3  89 5D FF                        mov dword ptr [rbp - 1], ebx
008B5BB6  48 89 45 F7                     mov qword ptr [rbp - 9], rax
008B5BBA  48 8D 7D E7                     lea rdi, [rbp - 0x19]
008B5BBE  48 8D 45 EF                     lea rax, [rbp - 0x11]
008B5BC2  BE 10 00 00 00                  mov esi, 0x10
008B5BC7  48 89 45 EF                     mov qword ptr [rbp - 0x11], rax
008B5BCB  48 8D 45 07                     lea rax, [rbp + 7]
008B5BCF  48 89 45 0F                     mov qword ptr [rbp + 0xf], rax
008B5BD3  48 8D 45 07                     lea rax, [rbp + 7]
008B5BD7  48 89 45 07                     mov qword ptr [rbp + 7], rax
008B5BDB  8B D6                           mov edx, esi
008B5BDD  B9 00 01 00 00                  mov ecx, 0x100
008B5BE2  41 B8 53 65 20 20               mov r8d, 0x20206553
008B5BE8  E8 03 C5 2C 00                  call 0x140b820f0
008B5BED  4C 8B F0                        mov r14, rax
008B5BF0  48 85 C0                        test rax, rax
008B5BF3  75 09                           jne 0x1408b5bfe
008B5BF5  49 8B 0C 24                     mov rcx, qword ptr [r12]
008B5BF9  E9 75 F5 FF FF                  jmp 0x1408b5173
008B5BFE  4C 8D 4D 6F                     lea r9, [rbp + 0x6f]
008B5C02  44 8B C6                        mov r8d, esi
008B5C05  49 8B D6                        mov rdx, r14
008B5C08  48 8B CF                        mov rcx, rdi
008B5C0B  E8 FC 26 16 00                  call 0x140a1830c
008B5C10  49 8B 0C 24                     mov rcx, qword ptr [r12]
008B5C14  8B F8                           mov edi, eax
008B5C16  E8 F5 9D 9A FF                  call 0x14025fa10
008B5C1B  E8 90 7C 9A FF                  call 0x14025d8b0
008B5C20  85 FF                           test edi, edi
008B5C22  79 11                           jns 0x1408b5c35
008B5C24  33 D2                           xor edx, edx
008B5C26  49 8B CE                        mov rcx, r14
008B5C29  E8 42 CC 2C 00                  call 0x140b82870
008B5C2E  8B C7                           mov eax, edi
008B5C30  E9 9D 07 00 00                  jmp 0x1408b63d2
008B5C35  4D 89 37                        mov qword ptr [r15], r14
008B5C38  EB F4                           jmp 0x1408b5c2e
008B5C3A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B5C43  BA 01 00 00 00                  mov edx, 1
008B5C48  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B5C4F  90                              nop
008B5C50  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B5C54  E8 67 BF 95 FF                  call 0x140211bc0
008B5C59  48 8B 87 38 04 00 00            mov rax, qword ptr [rdi + 0x438]
008B5C60  48 85 C0                        test rax, rax
008B5C63  74 03                           je 0x1408b5c68
008B5C65  8B 58 28                        mov ebx, dword ptr [rax + 0x28]
008B5C68  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B5C6C  E8 9F 9D 9A FF                  call 0x14025fa10
008B5C71  E8 3A 7C 9A FF                  call 0x14025d8b0
008B5C76  41 89 1F                        mov dword ptr [r15], ebx
008B5C79  E9 52 07 00 00                  jmp 0x1408b63d0
008B5C7E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B5C87  BA 01 00 00 00                  mov edx, 1
008B5C8C  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B5C93  90                              nop
008B5C94  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B5C98  E8 23 BF 95 FF                  call 0x140211bc0
008B5C9D  4C 8B B7 10 03 00 00            mov r14, qword ptr [rdi + 0x310]
008B5CA4  4D 85 F6                        test r14, r14
008B5CA7  74 0E                           je 0x1408b5cb7
008B5CA9  41 0F B6 46 01                  movzx eax, byte ptr [r14 + 1]
008B5CAE  8D 34 85 10 00 00 00            lea esi, [rax*4 + 0x10]
008B5CB5  EB 05                           jmp 0x1408b5cbc
008B5CB7  BE 08 00 00 00                  mov esi, 8
008B5CBC  8B D6                           mov edx, esi
008B5CBE  B9 00 01 00 00                  mov ecx, 0x100
008B5CC3  41 B8 53 65 20 20               mov r8d, 0x20206553
008B5CC9  E8 22 C4 2C 00                  call 0x140b820f0
008B5CCE  4C 8B E0                        mov r12, rax
008B5CD1  48 85 C0                        test rax, rax
008B5CD4  0F 84 95 F4 FF FF               je 0x1408b516f
008B5CDA  4D 85 F6                        test r14, r14
008B5CDD  74 16                           je 0x1408b5cf5
008B5CDF  4C 8B 87 10 03 00 00            mov r8, qword ptr [rdi + 0x310]
008B5CE6  4C 8D 70 08                     lea r14, [rax + 8]
008B5CEA  49 8B D6                        mov rdx, r14
008B5CED  8D 4E F8                        lea ecx, [rsi - 8]
008B5CF0  E8 5B 3D 0F 00                  call 0x1409a9a50
008B5CF5  4D 89 34 24                     mov qword ptr [r12], r14
008B5CF9  E9 A0 F8 FF FF                  jmp 0x1408b559e
008B5CFE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B5D07  41 BE 01 00 00 00               mov r14d, 1
008B5D0D  41 8A D6                        mov dl, r14b
008B5D10  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B5D17  90                              nop
008B5D18  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B5D1C  E8 9F BE 95 FF                  call 0x140211bc0
008B5D21  8B 8F 20 03 00 00               mov ecx, dword ptr [rdi + 0x320]
008B5D27  44 8B E1                        mov r12d, ecx
008B5D2A  41 C1 E4 04                     shl r12d, 4
008B5D2E  41 83 C4 18                     add r12d, 0x18
008B5D32  41 8B C4                        mov eax, r12d
008B5D35  85 C9                           test ecx, ecx
008B5D37  74 28                           je 0x1408b5d61
008B5D39  48 8B 97 18 03 00 00            mov rdx, qword ptr [rdi + 0x318]
008B5D40  41 8D 76 0F                     lea esi, [r14 + 0xf]
008B5D44  44 8B C1                        mov r8d, ecx
008B5D47  48 8B 02                        mov rax, qword ptr [rdx]
008B5D4A  48 03 D6                        add rdx, rsi
008B5D4D  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
008B5D51  45 8D 24 8C                     lea r12d, [r12 + rcx*4]
008B5D55  41 83 C4 08                     add r12d, 8
008B5D59  41 8B C4                        mov eax, r12d
008B5D5C  4D 2B C6                        sub r8, r14
008B5D5F  75 E6                           jne 0x1408b5d47
008B5D61  8B D0                           mov edx, eax
008B5D63  B9 00 01 00 00                  mov ecx, 0x100
008B5D68  41 B8 53 65 20 20               mov r8d, 0x20206553
008B5D6E  E8 7D C3 2C 00                  call 0x140b820f0
008B5D73  48 8B F0                        mov rsi, rax
008B5D76  48 85 C0                        test rax, rax
008B5D79  0F 84 F0 F3 FF FF               je 0x1408b516f
008B5D7F  8B 87 20 03 00 00               mov eax, dword ptr [rdi + 0x320]
008B5D85  4C 8D 4E 08                     lea r9, [rsi + 8]
008B5D89  89 06                           mov dword ptr [rsi], eax
008B5D8B  48 8D 45 67                     lea rax, [rbp + 0x67]
008B5D8F  8B 8F 20 03 00 00               mov ecx, dword ptr [rdi + 0x320]
008B5D95  8B D1                           mov edx, ecx
008B5D97  C1 E2 04                        shl edx, 4
008B5D9A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008B5D9F  48 83 C2 18                     add rdx, 0x18
008B5DA3  48 03 D6                        add rdx, rsi
008B5DA6  48 8D 45 67                     lea rax, [rbp + 0x67]
008B5DAA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008B5DAF  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
008B5DB4  48 8B 97 18 03 00 00            mov rdx, qword ptr [rdi + 0x318]
008B5DBB  E9 57 F6 FF FF                  jmp 0x1408b5417
008B5DC0  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B5DC9  41 BE 01 00 00 00               mov r14d, 1
008B5DCF  41 8A D6                        mov dl, r14b
008B5DD2  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B5DD9  90                              nop
008B5DDA  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
008B5DDE  E8 DD BD 95 FF                  call 0x140211bc0
008B5DE3  48 8B 87 48 04 00 00            mov rax, qword ptr [rdi + 0x448]
008B5DEA  48 85 C0                        test rax, rax
008B5DED  74 15                           je 0x1408b5e04
008B5DEF  44 8B 28                        mov r13d, dword ptr [rax]
008B5DF2  45 85 ED                        test r13d, r13d
008B5DF5  74 0D                           je 0x1408b5e04
008B5DF7  45 8B E5                        mov r12d, r13d
008B5DFA  41 C1 E4 04                     shl r12d, 4
008B5DFE  41 83 C4 08                     add r12d, 8
008B5E02  EB 09                           jmp 0x1408b5e0d
008B5E04  44 8B EB                        mov r13d, ebx
008B5E07  41 BC 18 00 00 00               mov r12d, 0x18
008B5E0D  41 8B CC                        mov ecx, r12d
008B5E10  BE 10 00 00 00                  mov esi, 0x10
008B5E15  45 85 ED                        test r13d, r13d
008B5E18  74 21                           je 0x1408b5e3b
008B5E1A  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
008B5E1E  45 8B C5                        mov r8d, r13d
008B5E21  48 8B 02                        mov rax, qword ptr [rdx]
008B5E24  48 03 D6                        add rdx, rsi
008B5E27  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
008B5E2B  45 8D 24 8C                     lea r12d, [r12 + rcx*4]
008B5E2F  41 83 C4 08                     add r12d, 8
008B5E33  4D 2B C6                        sub r8, r14
008B5E36  75 E9                           jne 0x1408b5e21
008B5E38  41 8B CC                        mov ecx, r12d
008B5E3B  8B D1                           mov edx, ecx
008B5E3D  41 B8 53 65 20 20               mov r8d, 0x20206553
008B5E43  B9 00 01 00 00                  mov ecx, 0x100
008B5E48  E8 A3 C2 2C 00                  call 0x140b820f0
008B5E4D  4C 8B F0                        mov r14, rax
008B5E50  48 85 C0                        test rax, rax
008B5E53  0F 84 16 F3 FF FF               je 0x1408b516f
008B5E59  33 C0                           xor eax, eax
008B5E5B  0F 57 C0                        xorps xmm0, xmm0
008B5E5E  41 0F 11 06                     movups xmmword ptr [r14], xmm0
008B5E62  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
008B5E66  45 89 2E                        mov dword ptr [r14], r13d
008B5E69  45 85 ED                        test r13d, r13d
008B5E6C  74 41                           je 0x1408b5eaf
008B5E6E  48 8B 8F 48 04 00 00            mov rcx, qword ptr [rdi + 0x448]
008B5E75  48 8D 45 67                     lea rax, [rbp + 0x67]
008B5E79  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
008B5E7E  4D 8D 4E 08                     lea r9, [r14 + 8]
008B5E82  41 C1 E5 04                     shl r13d, 4
008B5E86  48 8D 45 67                     lea rax, [rbp + 0x67]
008B5E8A  44 2B EE                        sub r13d, esi
008B5E8D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008B5E92  41 8B D5                        mov edx, r13d
008B5E95  45 8B C4                        mov r8d, r12d
008B5E98  48 83 C2 18                     add rdx, 0x18
008B5E9C  49 03 D6                        add rdx, r14
008B5E9F  48 89 54 24 20                  mov qword ptr [rsp + 0x20], rdx
008B5EA4  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
008B5EA8  8B 09                           mov ecx, dword ptr [rcx]
008B5EAA  E8 31 2D 0F 00                  call 0x1409a8be0
008B5EAF  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B5EB3  E8 58 9B 9A FF                  call 0x14025fa10
008B5EB8  E8 F3 79 9A FF                  call 0x14025d8b0
008B5EBD  4D 89 37                        mov qword ptr [r15], r14
008B5EC0  E9 0B 05 00 00                  jmp 0x1408b63d0
008B5EC5  83 EE 29                        sub esi, 0x29
008B5EC8  0F 84 D6 00 00 00               je 0x1408b5fa4
008B5ECE  83 EE 01                        sub esi, 1
008B5ED1  0F 84 C1 00 00 00               je 0x1408b5f98
008B5ED7  83 EE 02                        sub esi, 2
008B5EDA  74 2F                           je 0x1408b5f0b
008B5EDC  83 FE 02                        cmp esi, 2
008B5EDF  0F 85 BF F7 FF FF               jne 0x1408b56a4
008B5EE5  F7 81 C8 00 00 00 00 40 00 00   test dword ptr [rcx + 0xc8], 0x4000
008B5EEF  74 0F                           je 0x1408b5f00
008B5EF1  E8 9A 9F A4 FF                  call 0x1402ffe90
008B5EF6  84 C0                           test al, al
008B5EF8  75 06                           jne 0x1408b5f00
008B5EFA  44 8D 76 FF                     lea r14d, [rsi - 1]
008B5EFE  EB 03                           jmp 0x1408b5f03
008B5F00  44 8B F3                        mov r14d, ebx
008B5F03  45 89 37                        mov dword ptr [r15], r14d
008B5F06  E9 C5 04 00 00                  jmp 0x1408b63d0
008B5F0B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B5F14  41 BE 01 00 00 00               mov r14d, 1
008B5F1A  41 8A D6                        mov dl, r14b
008B5F1D  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B5F24  90                              nop
008B5F25  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
008B5F29  E8 92 BC 95 FF                  call 0x140211bc0
008B5F2E  48 8B 87 80 04 00 00            mov rax, qword ptr [rdi + 0x480]
008B5F35  41 8D 76 0F                     lea esi, [r14 + 0xf]
008B5F39  48 85 C0                        test rax, rax
008B5F3C  74 07                           je 0x1408b5f45
008B5F3E  0F B7 40 2A                     movzx eax, word ptr [rax + 0x2a]
008B5F42  48 03 F0                        add rsi, rax
008B5F45  41 B8 53 65 20 20               mov r8d, 0x20206553
008B5F4B  48 8B D6                        mov rdx, rsi
008B5F4E  B9 00 01 00 00                  mov ecx, 0x100
008B5F53  E8 98 C1 2C 00                  call 0x140b820f0
008B5F58  48 8B F0                        mov rsi, rax
008B5F5B  48 85 C0                        test rax, rax
008B5F5E  0F 84 0B F2 FF FF               je 0x1408b516f
008B5F64  48 39 9F 80 04 00 00            cmp qword ptr [rdi + 0x480], rbx
008B5F6B  74 20                           je 0x1408b5f8d
008B5F6D  44 88 70 08                     mov byte ptr [rax + 8], r14b
008B5F71  48 8D 48 10                     lea rcx, [rax + 0x10]
008B5F75  48 89 08                        mov qword ptr [rax], rcx
008B5F78  48 8B 97 80 04 00 00            mov rdx, qword ptr [rdi + 0x480]
008B5F7F  44 0F B7 42 2A                  movzx r8d, word ptr [rdx + 0x2a]
008B5F84  48 8B 52 30                     mov rdx, qword ptr [rdx + 0x30]
008B5F88  E9 0D F5 FF FF                  jmp 0x1408b549a
008B5F8D  88 58 08                        mov byte ptr [rax + 8], bl
008B5F90  48 89 18                        mov qword ptr [rax], rbx
008B5F93  E9 01 F2 FF FF                  jmp 0x1408b5199
008B5F98  0F B7 81 CA 00 00 00            movzx eax, word ptr [rcx + 0xca]
008B5F9F  E9 9C F8 FF FF                  jmp 0x1408b5840
008B5FA4  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B5FAD  BA 01 00 00 00                  mov edx, 1
008B5FB2  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B5FB9  90                              nop
008B5FBA  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
008B5FBE  E8 FD BB 95 FF                  call 0x140211bc0
008B5FC3  4C 8B B7 50 04 00 00            mov r14, qword ptr [rdi + 0x450]
008B5FCA  4D 85 F6                        test r14, r14
008B5FCD  74 0E                           je 0x1408b5fdd
008B5FCF  41 0F B6 46 01                  movzx eax, byte ptr [r14 + 1]
008B5FD4  8D 34 85 10 00 00 00            lea esi, [rax*4 + 0x10]
008B5FDB  EB 05                           jmp 0x1408b5fe2
008B5FDD  BE 08 00 00 00                  mov esi, 8
008B5FE2  8B D6                           mov edx, esi
008B5FE4  B9 00 01 00 00                  mov ecx, 0x100
008B5FE9  41 B8 53 65 20 20               mov r8d, 0x20206553
008B5FEF  E8 FC C0 2C 00                  call 0x140b820f0
008B5FF4  4C 8B E0                        mov r12, rax
008B5FF7  48 85 C0                        test rax, rax
008B5FFA  0F 84 6F F1 FF FF               je 0x1408b516f
008B6000  4D 85 F6                        test r14, r14
008B6003  0F 84 EC FC FF FF               je 0x1408b5cf5
008B6009  4C 8B 87 50 04 00 00            mov r8, qword ptr [rdi + 0x450]
008B6010  E9 D1 FC FF FF                  jmp 0x1408b5ce6
008B6015  8B CE                           mov ecx, esi
008B6017  83 E9 30                        sub ecx, 0x30
008B601A  0F 84 EF 02 00 00               je 0x1408b630f
008B6020  83 E9 01                        sub ecx, 1
008B6023  0F 84 57 02 00 00               je 0x1408b6280
008B6029  83 E9 01                        sub ecx, 1
008B602C  0F 84 DD 02 00 00               je 0x1408b630f
008B6032  83 E9 01                        sub ecx, 1
008B6035  0F 84 D4 02 00 00               je 0x1408b630f
008B603B  83 E9 01                        sub ecx, 1
008B603E  0F 84 CB 02 00 00               je 0x1408b630f
008B6044  83 E9 01                        sub ecx, 1
008B6047  0F 84 C2 02 00 00               je 0x1408b630f
008B604D  83 E9 01                        sub ecx, 1
008B6050  0F 84 7F 01 00 00               je 0x1408b61d5
008B6056  83 E9 01                        sub ecx, 1
008B6059  0F 84 DA 00 00 00               je 0x1408b6139
008B605F  83 F9 01                        cmp ecx, 1
008B6062  0F 85 3C F6 FF FF               jne 0x1408b56a4
008B6068  E8 FB 78 D1 FF                  call 0x1405cd968
008B606D  85 C0                           test eax, eax
008B606F  0F 84 2F F6 FF FF               je 0x1408b56a4
008B6075  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B607E  BA 01 00 00 00                  mov edx, 1
008B6083  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B608A  90                              nop
008B608B  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B608F  E8 2C BB 95 FF                  call 0x140211bc0
008B6094  48 8B 8F 98 04 00 00            mov rcx, qword ptr [rdi + 0x498]
008B609B  48 85 C9                        test rcx, rcx
008B609E  0F 84 C2 01 00 00               je 0x1408b6266
008B60A4  83 BF A0 04 00 00 03            cmp dword ptr [rdi + 0x4a0], 3
008B60AB  72 66                           jb 0x1408b6113
008B60AD  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
008B60B1  E8 EA 22 D5 FF                  call 0x1406083a0
008B60B6  84 C0                           test al, al
008B60B8  74 59                           je 0x1408b6113
008B60BA  48 8B 87 98 04 00 00            mov rax, qword ptr [rdi + 0x498]
008B60C1  41 B8 53 65 20 20               mov r8d, 0x20206553
008B60C7  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
008B60CB  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
008B60CF  B9 00 01 00 00                  mov ecx, 0x100
008B60D4  44 8D 34 85 10 00 00 00         lea r14d, [rax*4 + 0x10]
008B60DC  41 8B D6                        mov edx, r14d
008B60DF  E8 0C C0 2C 00                  call 0x140b820f0
008B60E4  48 8B F0                        mov rsi, rax
008B60E7  48 85 C0                        test rax, rax
008B60EA  0F 84 7F F0 FF FF               je 0x1408b516f
008B60F0  4C 8B 87 98 04 00 00            mov r8, qword ptr [rdi + 0x498]
008B60F7  48 8D 58 08                     lea rbx, [rax + 8]
008B60FB  41 8D 4E F8                     lea ecx, [r14 - 8]
008B60FF  48 8B D3                        mov rdx, rbx
008B6102  4D 8B 40 20                     mov r8, qword ptr [r8 + 0x20]
008B6106  E8 45 39 0F 00                  call 0x1409a9a50
008B610B  48 89 1E                        mov qword ptr [rsi], rbx
008B610E  E9 86 F0 FF FF                  jmp 0x1408b5199
008B6113  BA 08 00 00 00                  mov edx, 8
008B6118  B9 00 01 00 00                  mov ecx, 0x100
008B611D  41 B8 53 65 20 20               mov r8d, 0x20206553
008B6123  E8 C8 BF 2C 00                  call 0x140b820f0
008B6128  48 8B F0                        mov rsi, rax
008B612B  48 85 C0                        test rax, rax
008B612E  0F 85 5C FE FF FF               jne 0x1408b5f90
008B6134  E9 36 F0 FF FF                  jmp 0x1408b516f
008B6139  E8 2A 78 D1 FF                  call 0x1405cd968
008B613E  85 C0                           test eax, eax
008B6140  0F 84 5E F5 FF FF               je 0x1408b56a4
008B6146  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B614F  BA 01 00 00 00                  mov edx, 1
008B6154  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B615B  90                              nop
008B615C  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B6160  E8 5B BA 95 FF                  call 0x140211bc0
008B6165  4C 8B B7 98 04 00 00            mov r14, qword ptr [rdi + 0x498]
008B616C  4D 85 F6                        test r14, r14
008B616F  0F 84 F1 00 00 00               je 0x1408b6266
008B6175  83 BF A0 04 00 00 02            cmp dword ptr [rdi + 0x4a0], 2
008B617C  0F 82 E4 00 00 00               jb 0x1408b6266
008B6182  4D 8B 76 10                     mov r14, qword ptr [r14 + 0x10]
008B6186  4D 85 F6                        test r14, r14
008B6189  74 0E                           je 0x1408b6199
008B618B  41 0F B6 46 01                  movzx eax, byte ptr [r14 + 1]
008B6190  8D 34 85 10 00 00 00            lea esi, [rax*4 + 0x10]
008B6197  EB 05                           jmp 0x1408b619e
008B6199  BE 08 00 00 00                  mov esi, 8
008B619E  8B D6                           mov edx, esi
008B61A0  B9 00 01 00 00                  mov ecx, 0x100
008B61A5  41 B8 53 65 20 20               mov r8d, 0x20206553
008B61AB  E8 40 BF 2C 00                  call 0x140b820f0
008B61B0  4C 8B E0                        mov r12, rax
008B61B3  48 85 C0                        test rax, rax
008B61B6  0F 84 B3 EF FF FF               je 0x1408b516f
008B61BC  4D 85 F6                        test r14, r14
008B61BF  0F 84 30 FB FF FF               je 0x1408b5cf5
008B61C5  4C 8B 87 98 04 00 00            mov r8, qword ptr [rdi + 0x498]
008B61CC  4D 8B 40 10                     mov r8, qword ptr [r8 + 0x10]
008B61D0  E9 11 FB FF FF                  jmp 0x1408b5ce6
008B61D5  E8 8E 77 D1 FF                  call 0x1405cd968
008B61DA  85 C0                           test eax, eax
008B61DC  0F 84 C2 F4 FF FF               je 0x1408b56a4
008B61E2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B61EB  BA 01 00 00 00                  mov edx, 1
008B61F0  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B61F7  90                              nop
008B61F8  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B61FC  E8 BF B9 95 FF                  call 0x140211bc0
008B6201  4C 8B B7 98 04 00 00            mov r14, qword ptr [rdi + 0x498]
008B6208  4D 85 F6                        test r14, r14
008B620B  74 59                           je 0x1408b6266
008B620D  39 9F A0 04 00 00               cmp dword ptr [rdi + 0x4a0], ebx
008B6213  74 51                           je 0x1408b6266
008B6215  4D 8B 36                        mov r14, qword ptr [r14]
008B6218  4D 85 F6                        test r14, r14
008B621B  74 0E                           je 0x1408b622b
008B621D  41 0F B6 46 01                  movzx eax, byte ptr [r14 + 1]
008B6222  8D 34 85 10 00 00 00            lea esi, [rax*4 + 0x10]
008B6229  EB 05                           jmp 0x1408b6230
008B622B  BE 08 00 00 00                  mov esi, 8
008B6230  8B D6                           mov edx, esi
008B6232  B9 00 01 00 00                  mov ecx, 0x100
008B6237  41 B8 53 65 20 20               mov r8d, 0x20206553
008B623D  E8 AE BE 2C 00                  call 0x140b820f0
008B6242  4C 8B E0                        mov r12, rax
008B6245  48 85 C0                        test rax, rax
008B6248  0F 84 21 EF FF FF               je 0x1408b516f
008B624E  4D 85 F6                        test r14, r14
008B6251  0F 84 9E FA FF FF               je 0x1408b5cf5
008B6257  4C 8B 87 98 04 00 00            mov r8, qword ptr [rdi + 0x498]
008B625E  4D 8B 00                        mov r8, qword ptr [r8]
008B6261  E9 80 FA FF FF                  jmp 0x1408b5ce6
008B6266  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B626A  E8 A1 97 9A FF                  call 0x14025fa10
008B626F  BB 0D 00 00 C0                  mov ebx, 0xc000000d
008B6274  E8 37 76 9A FF                  call 0x14025d8b0
008B6279  8B C3                           mov eax, ebx
008B627B  E9 52 01 00 00                  jmp 0x1408b63d2
008B6280  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008B6289  BA 01 00 00 00                  mov edx, 1
008B628E  89 5D C7                        mov dword ptr [rbp - 0x39], ebx
008B6291  89 5D 7F                        mov dword ptr [rbp + 0x7f], ebx
008B6294  89 5D 67                        mov dword ptr [rbp + 0x67], ebx
008B6297  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008B629E  90                              nop
008B629F  48 8B 4F 30                     mov rcx, qword ptr [rdi + 0x30]
008B62A3  89 5D 6F                        mov dword ptr [rbp + 0x6f], ebx
008B62A6  E8 15 B9 95 FF                  call 0x140211bc0
008B62AB  48 8D 45 6F                     lea rax, [rbp + 0x6f]
008B62AF  48 8B CF                        mov rcx, rdi
008B62B2  4C 8D 4D 67                     lea r9, [rbp + 0x67]
008B62B6  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008B62BB  4C 8D 45 7F                     lea r8, [rbp + 0x7f]
008B62BF  48 8D 55 C7                     lea rdx, [rbp - 0x39]
008B62C3  E8 B8 00 1D 00                  call 0x140a86380
008B62C8  8B D0                           mov edx, eax
008B62CA  B9 00 01 00 00                  mov ecx, 0x100
008B62CF  41 B8 53 65 20 20               mov r8d, 0x20206553
008B62D5  E8 16 BE 2C 00                  call 0x140b820f0
008B62DA  48 8B F0                        mov rsi, rax
008B62DD  48 85 C0                        test rax, rax
008B62E0  0F 84 F1 F0 FF FF               je 0x1408b53d7
008B62E6  8B 45 6F                        mov eax, dword ptr [rbp + 0x6f]
008B62E9  48 8B D6                        mov rdx, rsi
008B62EC  44 8B 4D C7                     mov r9d, dword ptr [rbp - 0x39]
008B62F0  48 8B CF                        mov rcx, rdi
008B62F3  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
008B62F7  8B 45 67                        mov eax, dword ptr [rbp + 0x67]
008B62FA  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
008B62FE  8B 45 7F                        mov eax, dword ptr [rbp + 0x7f]
008B6301  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008B6305  E8 0E 23 0F 00                  call 0x1409a8618
008B630A  E9 8A EE FF FF                  jmp 0x1408b5199
008B630F  83 FE 30                        cmp esi, 0x30
008B6312  75 2C                           jne 0x1408b6340
008B6314  4C 8B 05 BD 18 5B 00            mov r8, qword ptr [rip + 0x5b18bd]
008B631B  48 8D 8F 28 03 00 00            lea rcx, [rdi + 0x328]
008B6322  88 5C 24 28                     mov byte ptr [rsp + 0x28], bl
008B6326  45 33 C9                        xor r9d, r9d
008B6329  33 D2                           xor edx, edx
008B632B  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
008B6330  E8 AB 22 B1 FF                  call 0x1403c85e0
008B6335  0F B6 C0                        movzx eax, al
008B6338  41 89 07                        mov dword ptr [r15], eax
008B633B  E9 90 00 00 00                  jmp 0x1408b63d0
008B6340  83 FE 2F                        cmp esi, 0x2f
008B6343  75 1C                           jne 0x1408b6361
008B6345  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
008B634E  48 8B CF                        mov rcx, rdi
008B6351  8A 92 32 02 00 00               mov dl, byte ptr [rdx + 0x232]
008B6357  E8 A8 23 BA FF                  call 0x140458704
008B635C  41 88 00                        mov byte ptr [r8], al
008B635F  EB 6F                           jmp 0x1408b63d0
008B6361  83 FE 33                        cmp esi, 0x33
008B6364  75 18                           jne 0x1408b637e
008B6366  E8 ED C9 C3 FF                  call 0x1404f2d58
008B636B  85 C0                           test eax, eax
008B636D  0F 84 31 F3 FF FF               je 0x1408b56a4
008B6373  8B 87 C8 00 00 00               mov eax, dword ptr [rdi + 0xc8]
008B6379  C1 E8 1B                        shr eax, 0x1b
008B637C  EB 18                           jmp 0x1408b6396
008B637E  83 FE 34                        cmp esi, 0x34
008B6381  75 1A                           jne 0x1408b639d
008B6383  E8 D0 C9 C3 FF                  call 0x1404f2d58
008B6388  85 C0                           test eax, eax
008B638A  0F 84 14 F3 FF FF               je 0x1408b56a4
008B6390  8A 87 90 04 00 00               mov al, byte ptr [rdi + 0x490]
008B6396  24 01                           and al, 1
008B6398  41 88 07                        mov byte ptr [r15], al
008B639B  EB 33                           jmp 0x1408b63d0
008B639D  83 FE 35                        cmp esi, 0x35
008B63A0  75 1D                           jne 0x1408b63bf
008B63A2  E8 C1 75 D1 FF                  call 0x1405cd968
008B63A7  85 C0                           test eax, eax
008B63A9  0F 84 F5 F2 FF FF               je 0x1408b56a4
008B63AF  48 8B CF                        mov rcx, rdi
008B63B2  E8 C5 13 D5 FF                  call 0x14060777c
008B63B7  0F B6 C8                        movzx ecx, al
008B63BA  41 89 0F                        mov dword ptr [r15], ecx
008B63BD  EB 11                           jmp 0x1408b63d0
008B63BF  8B 87 C8 00 00 00               mov eax, dword ptr [rdi + 0xc8]
008B63C5  25 00 00 00 03                  and eax, 0x3000000
008B63CA  C1 E8 18                        shr eax, 0x18
008B63CD  41 89 00                        mov dword ptr [r8], eax
008B63D0  33 C0                           xor eax, eax
008B63D2  48 8B 9C 24 30 01 00 00         mov rbx, qword ptr [rsp + 0x130]
008B63DA  48 81 C4 E0 00 00 00            add rsp, 0xe0
008B63E1  41 5F                           pop r15
008B63E3  41 5E                           pop r14
008B63E5  41 5D                           pop r13
008B63E7  41 5C                           pop r12
008B63E9  5F                              pop rdi
008B63EA  5E                              pop rsi
008B63EB  5D                              pop rbp
008B63EC  C3                              ret
008B63ED  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeQueryInformationToken(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned int v_stack_m84;
    unsigned int v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned int v_stack_m90;
    unsigned int v_stack_m94;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int8 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (224);
    v_rbx = 0;
    v_stack_p10 = 0;
    v_stack_m98 = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    if (a2 > 29) goto loc_008B5AF1;
    if (a2 == 29) goto loc_008B5AC3;
    if (a2 > 12) goto loc_008B5655;
    if (a2 == 12) goto loc_008B5648;
    if (a2 > 6) goto loc_008B54A4;
    if (a2 == 6) goto loc_008B5424;
    v_rsi = (unsigned int)(((unsigned int)(a2)) - (1));
    if (condition_is_equal) goto loc_008B5383;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_008B529C;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_008B522D;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_008B51AF;
    if (((unsigned int)(v_rsi)) != 1) goto loc_008B56A4;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(a1 + 48), (unsigned int)((unsigned int)(v_rsi)), a3, a4);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 168) + 1) * 4 + 16)), (unsigned int)(0x20206553ULL), a4);
    if (result != 0) goto loc_008B5182;
loc_008B516F:
loc_008B5173:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(a1 + 48), (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 168) + 1) * 4 + 16)), (unsigned int)(0x20206553ULL), a4);
    goto loc_008B6274;
loc_008B5182:
    *(unsigned __int64 *)(result) = result + 8;
loc_008B5190:
    result = RtlCopySid(*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 168) + 1) * 4 + 16 - 8, result + 8, *(unsigned __int64 *)(a1 + 168), a4);
loc_008B5199:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(a1 + 48), result + 8, *(unsigned __int64 *)(a1 + 168), a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(a1 + 48), result + 8, *(unsigned __int64 *)(a1 + 168), a4);
loc_008B51A7:
    *(unsigned __int64 *)(a3) = result;
    goto loc_008B63D0;
loc_008B51AF:
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 48), 1, *(unsigned __int64 *)(a1 + 168), a4);
    a1 = ((unsigned int)(*(unsigned int *)(a1 + 144))) + ((unsigned int)(*(unsigned int *)(a1 + 144)));
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152) + a1 * 8) + 1) * 4 + 16)), (unsigned int)(0x20206553ULL), a4);
    if (result == 0) goto loc_008B53D7;
    *(unsigned __int64 *)(result) = result + 8;
    result = ((unsigned int)(*(unsigned int *)(a1 + 144))) + ((unsigned int)(*(unsigned int *)(a1 + 144)));
    goto loc_008B5190;
loc_008B522D:
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(256 + 48), 1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152) + result * 8), a4);
    result = SepTokenPrivilegeCount(a1, 1, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152) + result * 8), a4);
    if (((unsigned int)(result)) <= 1) goto loc_008B5269;
    goto loc_008B526E;
loc_008B5269:
loc_008B526E:
    result = ExAllocatePool2(256, 16, (unsigned int)(0x20206553ULL), a4);
    if (result == 0) goto loc_008B53D7;
    result = SepConvertTokenPrivileges(a1, result, (unsigned int)(0x20206553ULL), a4);
    goto loc_008B5199;
loc_008B529C:
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(a1 + 48), 1, (unsigned int)(0x20206553ULL), a4);
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124))))) << (4));
    v_r12 = (unsigned int)((v_r12) + (-8));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124)))) <= 1) goto loc_008B5301;
    a2 = (*(unsigned __int64 *)(a1 + 152)) + (1 + 15);
loc_008B52E7:
    a2 = (a2) + (1 + 15);
    v_r12 = (unsigned int)((v_r12 + *(unsigned __int8 *)(*(unsigned __int64 *)(a2) + 1) * 4) + (8));
    a3 = ((unsigned int)(*(unsigned int *)(a1 + 124)) - 1) - (1);
    if (condition_is_not_equal) goto loc_008B52E7;
loc_008B5301:
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))), (unsigned int)(0x20206553ULL), a4);
    if (result == 0) goto loc_008B53D7;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 124))) - (1));
    *(unsigned int *)(result) = (unsigned int)(result);
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124))))) << (4));
    a2 = (*(unsigned __int64 *)(a1 + 152)) + (1 + 15);
    v_r10 = (unsigned int)((v_r10) - (32));
    v_stack_mE8 = v_stack_p8;
    v_r10 = (v_r10) + (24);
    v_r10 = (v_r10) + (result);
    v_stack_mF0 = v_stack_p8;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 124))) - 1);
    v_stack_mF8 = v_r10;
    result = RtlCopySidAndAttributesArray(a1, a2, (unsigned int)((unsigned int)(v_r12)), result + 8);
    result = ExReleaseResourceLite(*(unsigned __int64 *)(a1 + 48), a2, (unsigned int)((unsigned int)(v_r12)), result + 8);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(a1 + 48), a2, (unsigned int)((unsigned int)(v_r12)), result + 8);
    *(unsigned __int64 *)(a3) = result;
    goto loc_008B63D0;
loc_008B5383:
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 48) + 48), 1, (unsigned int)((unsigned int)(v_r12)), result + 8);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152)) + 1) * 4 + 24)), (unsigned int)(0x20206553ULL), result + 8);
    if (result != 0) goto loc_008B53EF;
loc_008B53D7:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(a1 + 48), (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152)) + 1) * 4 + 24)), (unsigned int)(0x20206553ULL), result + 8);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(a1 + 48), (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152)) + 1) * 4 + 24)), (unsigned int)(0x20206553ULL), result + 8);
loc_008B53E5:
    goto loc_008B63D2;
loc_008B53EF:
    v_stack_mE8 = v_stack_p8;
    result = ((unsigned int)(0xC000009AULL)) + (16);
    v_stack_mF0 = v_stack_p8;
    v_stack_mF8 = result;
loc_008B5417:
    result = RtlCopySidAndAttributesArray(1, *(unsigned __int64 *)(a1 + 152), (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152)) + 1) * 4 + 24)), result);
    goto loc_008B5199;
loc_008B5424:
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(1 + 48), 1, (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152)) + 1) * 4 + 24)), result);
    result = *(unsigned __int64 *)(a1 + 184);
    v_rsi = 8;
    if (*(unsigned __int64 *)(a1 + 184) != 0) {
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 184) + 2);
        v_rsi = (8) + (result);
    }
    result = ExAllocatePool2(256, v_rsi, (unsigned int)(0x20206553ULL), result);
    if (result == 0) goto loc_008B516F;
    if ((*(unsigned __int64 *)(a1 + 184)) == ((unsigned int)(0xC000009AULL))) goto loc_008B5F90;
    *(unsigned __int64 *)(result) = result + 8;
loc_008B549A:
    result = memcpy(result + 8, *(unsigned __int64 *)(a1 + 184), *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 184) + 2), result);
    goto loc_008B5199;
loc_008B54A4:
    v_rsi = (unsigned int)((result) - (7));
    if (condition_is_equal) goto loc_008B561B;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_008B55F2;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_008B55B4;
    if (((unsigned int)(v_rsi)) != 1) goto loc_008B56A4;
    result = ExAllocatePool2(256, v_rsi + 55, (unsigned int)(0x20206553ULL), result);
    if (result == 0) goto loc_008B53E5;
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(a1 + 16);
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(a1 + 24);
    *(unsigned int *)(result + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 192)));
    *(unsigned int *)(result + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 196)));
    *(unsigned __int64 *)(result + 16) = *(unsigned __int64 *)(a1 + 40);
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(a1 + 48), (unsigned __int8)((unsigned int)((unsigned int)(v_rsi))), (unsigned int)(0x20206553ULL), result);
    *(unsigned int *)(result + 32) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 136)));
    a1 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 168) + 1)) << (2));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 136))) - ((unsigned int)(a1)));
    a2 = (unsigned int)((a2) - (8));
    result = *(unsigned __int64 *)(a1 + 184);
    if (*(unsigned __int64 *)(a1 + 184) != 0) {
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 184) + 2);
        a2 = (unsigned int)((a2) - ((unsigned int)(result)));
    }
    *(unsigned int *)(result + 36) = a2;
    *(unsigned int *)(result + 36) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 140)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 124))) - ((unsigned int)((unsigned int)((unsigned int)(v_rsi)))));
    *(unsigned int *)(result + 40) = (unsigned int)(result);
    result = SepTokenPrivilegeCount(a1, a2, (unsigned int)(0x20206553ULL), result);
    *(unsigned int *)(result + 44) = (unsigned int)(result);
    *(unsigned __int64 *)(result + 48) = *(unsigned __int64 *)(a1 + 56);
loc_008B559E:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(a1 + 48), a2, (unsigned int)(0x20206553ULL), result);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(a1 + 48), a2, (unsigned int)(0x20206553ULL), result);
    *(unsigned __int64 *)(a3) = result;
    goto loc_008B63D0;
loc_008B55B4:
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 48) + 192)) != 2) goto loc_008B56A4;
    result = ExAllocatePool2(256, 4, (unsigned int)(0x20206553ULL), result);
    if (result == 0) goto loc_008B53E5;
loc_008B55E8:
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 196)));
    *(unsigned __int64 *)(a3) = result;
    goto loc_008B63D0;
loc_008B55F2:
    result = ExAllocatePool2(256, 4, (unsigned int)(0x20206553ULL), result);
    if (result == 0) goto loc_008B53E5;
    goto loc_008B55E8;
loc_008B561B:
    result = ExAllocatePool2(256, 16, (unsigned int)(0x20206553ULL), result);
    if (result == 0) goto loc_008B53E5;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(a3) = result;
    goto loc_008B63D0;
loc_008B5648:
    result = SeQuerySessionIdToken(256, a3, (unsigned int)(0x20206553ULL), result);
    goto loc_008B63D0;
loc_008B5655:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) - (13));
    if (condition_is_equal) goto loc_008B5904;
    a1 = (unsigned int)((a1) - (5));
    if (condition_is_equal) goto loc_008B58D1;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_008B5872;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008B5832;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008B5716;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008B5832;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008B5832;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008B56AE;
    if (((unsigned int)(a1)) == 1) goto loc_008B5832;
loc_008B56A4:
    goto loc_008B63D2;
loc_008B56AE:
    v_stack_m48 = v_xmm0;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(a1 + 48), 1, (unsigned int)(0x20206553ULL), result);
    result = SepCopyTokenIntegrity(a1, v_stack_m48, (unsigned int)(0x20206553ULL), result);
    result = RtlSubAuthorityCountSid(v_stack_m48, v_stack_m48, (unsigned int)(0x20206553ULL), result);
    if ((unsigned __int8)(*(unsigned __int8 *)(result)) != 0) goto loc_008B56F5;
    goto loc_008B5705;
loc_008B56F5:
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int8 *)(result)))) - (1));
    result = RtlSubAuthoritySid(v_stack_m48, a2, (unsigned int)(0x20206553ULL), result);
loc_008B5705:
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    result = ExReleaseResourceLite(*(unsigned __int64 *)(a1 + 48), a2, (unsigned int)(0x20206553ULL), result);
    goto loc_008B6274;
loc_008B5716:
    v_stack_m80 = (unsigned int)((unsigned int)(0xC000009AULL));
    v_stack_m84 = (unsigned int)((unsigned int)(0xC000009AULL));
    v_stack_m88 = (unsigned int)((unsigned int)(0xC000009AULL));
    v_stack_m8C = (unsigned int)((unsigned int)(0xC000009AULL));
    v_stack_m90 = (unsigned int)((unsigned int)(0xC000009AULL));
    v_stack_m94 = (unsigned int)((unsigned int)(0xC000009AULL));
    v_stack_p20 = (unsigned int)((unsigned int)(0xC000009AULL));
    v_stack_p8 = (unsigned int)((unsigned int)(0xC000009AULL));
    v_stack_p10 = (unsigned int)((unsigned int)(0xC000009AULL));
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(a1 + 48), 1, (unsigned int)(0x20206553ULL), result);
    a3 = 0;
    v_stack_mB8 = v_stack_p10;
    a2 = 0;
    v_stack_mC0 = v_stack_p8;
    v_stack_mC8 = v_stack_p20;
    v_stack_mD0 = v_stack_m94;
    v_stack_mD8 = v_stack_m90;
    v_stack_mE0 = v_stack_m8C;
    v_stack_mE8 = v_stack_m88;
    v_stack_mF0 = v_stack_m84;
    v_stack_mF8 = v_stack_m80;
    result = SepGetTokenAccessInformationBufferSize(a1, a2, a3, v_stack_m98);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result)), (unsigned int)(0x20206553ULL), v_stack_m98);
    if (result == 0) goto loc_008B53D7;
    v_stack_mA8 = (unsigned int)(0xC000009AULL);
    v_stack_mB0 = (unsigned __int8)((unsigned int)(0xC000009AULL));
    v_stack_mB8 = (unsigned int)((unsigned int)(v_stack_p10));
    v_stack_mC0 = (unsigned int)((unsigned int)(v_stack_p8));
    v_stack_mC8 = (unsigned int)((unsigned int)(v_stack_p20));
    v_stack_mD0 = (unsigned int)((unsigned int)(v_stack_m94));
    v_stack_mD8 = (unsigned int)((unsigned int)(v_stack_m90));
    v_stack_mE0 = (unsigned int)((unsigned int)(v_stack_m8C));
    v_stack_mE8 = (unsigned int)((unsigned int)(v_stack_m88));
    v_stack_mF0 = (unsigned int)((unsigned int)(v_stack_m84));
    v_stack_mF8 = (unsigned int)((unsigned int)(v_stack_m80));
    result = SepCopyTokenAccessInformation(a1, result, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)(v_stack_m98));
    goto loc_008B5199;
loc_008B5832:
    if (((unsigned int)(result)) != 23) goto loc_008B5848;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 200))) >> (9));
loc_008B5840:
    result = (unsigned int)((result) & (1));
    goto loc_008B63CD;
loc_008B5848:
    if (((unsigned int)(result)) != 24) goto loc_008B585E;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 200))) >> (10));
    goto loc_008B5840;
loc_008B585E:
    if (((unsigned int)(result)) != 26) goto loc_008B5AC3;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 200))) >> (12));
    goto loc_008B5840;
loc_008B5872:
    result = ExAllocatePool2(256, 4, (unsigned int)(0x20206553ULL), (unsigned int)(v_stack_m98));
    if (result == 0) goto loc_008B53E5;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(a1 + 48), 1, (unsigned int)(0x20206553ULL), (unsigned int)(v_stack_m98));
    result = SepGetTokenElevation(a1, 1, (unsigned int)(0x20206553ULL), (unsigned int)(v_stack_m98));
    result = ExReleaseResourceLite(*(unsigned __int64 *)(a1 + 48), 1, (unsigned int)(0x20206553ULL), (unsigned int)(v_stack_m98));
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(a1 + 48), 1, (unsigned int)(0x20206553ULL), (unsigned int)(v_stack_m98));
    *(unsigned int *)(result) = (unsigned int)((unsigned int)((unsigned int)(result)));
    goto loc_008B51A7;
loc_008B58D1:
    result = ExAllocatePool2(256, 4, (unsigned int)(0x20206553ULL), (unsigned int)(v_stack_m98));
    if (result == 0) goto loc_008B53E5;
    result = SepGetTokenElevationType(a1, result, (unsigned int)(0x20206553ULL), (unsigned int)(v_stack_m98));
    *(unsigned int *)(result) = (unsigned int)(result);
    *(unsigned __int64 *)(a3) = result;
    goto loc_008B63D0;
loc_008B5904:
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(a1 + 48), 1, (unsigned int)(0x20206553ULL), (unsigned int)(v_stack_m98));
    result = SepTokenPrivilegeCount(a1, 1, (unsigned int)(0x20206553ULL), (unsigned int)(v_stack_m98));
    v_stack_p8 = (unsigned int)(result);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124))))) << (4));
    a4 = (unsigned int)((result + result * 2) << (2));
    v_stack_p10 = (unsigned int)(a4);
    v_stack_p20 = (unsigned int)(result);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124))) == 0) goto loc_008B5980;
loc_008B5964:
    a2 = (*(unsigned __int64 *)(a1 + 152)) + (1 + 15);
    a1 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152)) + 1) * 4 + 15) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)(result))) + ((unsigned int)(a1)));
    a3 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124))))) - (1);
    if (condition_is_not_equal) goto loc_008B5964;
loc_008B5980:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 128))))) << (4));
    v_stack_m98 = (unsigned int)(result);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 128))) == 0) goto loc_008B59BB;
loc_008B599F:
    a2 = (*(unsigned __int64 *)(a1 + 160)) + (1 + 15);
    a1 = (unsigned int)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 160)) + 1) * 4 + 15) & ((unsigned int)((unsigned int)(0xFFFFFFF8ULL))));
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(result))) + ((unsigned int)(a1)));
    a3 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 128))))) - (1);
    if (condition_is_not_equal) goto loc_008B599F;
loc_008B59BB:
    a4 = (unsigned int)((a4) + (56));
    a2 = (unsigned int)((v_r12 + v_r13 * 1) + ((unsigned int)(a4)));
    result = ExAllocatePool2(256, a2, (unsigned int)(0x20206553ULL), a4);
    if (result == 0) goto loc_008B53D7;
    *(unsigned __int64 *)(result + 48) = *(unsigned __int64 *)(a1 + 24);
    *(unsigned int *)(result + 4) = (unsigned int)(v_r13);
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 124)));
    *(unsigned __int64 *)(result + 8) = result + 56;
    *(unsigned int *)(result + 20) = (unsigned int)(v_r12);
    *(unsigned int *)(result + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 128)));
    if ((*(unsigned int *)(a1 + 128)) == ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_008B5A20;
    result = ((unsigned int)((unsigned int)(v_r13)) + 7) & (-8);
    result = (result) + (result + 56);
    goto loc_008B5A23;
loc_008B5A20:
loc_008B5A23:
    *(unsigned __int64 *)(result + 24) = (unsigned int)((unsigned int)(result));
    *(unsigned int *)(result + 36) = (unsigned int)((unsigned int)(v_stack_p10));
    *(unsigned int *)(result + 32) = (unsigned int)((unsigned int)(v_stack_p8));
    result = ((unsigned int)((unsigned int)(v_r12))) + ((unsigned int)((unsigned int)(v_r13)));
    v_r13 = (unsigned int)((v_r13) - ((unsigned int)((unsigned int)(v_stack_p20))));
    result = (result) + (result + 56);
    *(unsigned __int64 *)(result + 40) = result;
    v_stack_mE8 = v_stack_p8;
    v_stack_mF0 = v_stack_p8;
    v_stack_mF8 = result + 56 + (unsigned int)(v_stack_p20) * 1;
    result = RtlCopySidAndAttributesArray((unsigned int)(*(unsigned int *)(a1 + 124)), *(unsigned __int64 *)(a1 + 152), (unsigned int)((unsigned int)(v_r13)), result + 56);
    if ((*(unsigned int *)(result + 16)) >= = ((unsigned int)((unsigned int)((unsigned int)(result))))) {
        a1 = v_stack_m98;
        a4 = *(unsigned __int64 *)(result + 24);
        v_r12 = (unsigned int)((v_r12) - ((unsigned int)(a1)));
        a2 = *(unsigned __int64 *)(a1 + 160);
        a3 = (unsigned int)(v_r12);
        result = a4 + a1 * 1;
        a1 = v_stack_p8;
        v_stack_mE8 = a1;
        a1 = v_stack_p8;
        v_stack_mF0 = a1;
        a1 = *(unsigned int *)(a1 + 128);
        v_stack_mF8 = result;
        result = RtlCopySidAndAttributesArray(a1, a2, a3, a4);
    }
    result = SepConvertTokenPrivilegesToLuidAndAttributes(a1, *(unsigned __int64 *)(result + 40), a3, a4);
    goto loc_008B5199;
loc_008B5AC3:
    if (((unsigned int)(result)) != 29) goto loc_008B5AD6;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 200))) >> (14));
    goto loc_008B5840;
loc_008B5AD6:
    if (((unsigned int)(result)) != 21) goto loc_008B63BF;
    result = (((*(unsigned int *)(a1 + 200)) & (0x810ULL)) != 0) ? 1 : 0;
    goto loc_008B635C;
loc_008B5AF1:
    if (((unsigned int)(result)) > 47) goto loc_008B6015;
    if (((unsigned int)(result)) == 47) goto loc_008B6345;
    if (((unsigned int)(result)) > 37) goto loc_008B5EC5;
    if (((unsigned int)(result)) == 37) goto loc_008B5DC0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) - (30));
    if (condition_is_equal) goto loc_008B5CFE;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008B5C7E;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008B5C3A;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008B5B3A;
    if (((unsigned int)(a1)) != 1) goto loc_008B56A4;
loc_008B5B3A:
    *(unsigned __int64 *)(a3) = (unsigned int)((unsigned int)(result));
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(a1 + 48), 1, a3, a4);
    if (*(unsigned __int64 *)(a1 + 1096) == 0) goto loc_008B5BAF;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1096) + 576) != 0) goto loc_008B5B81;
    if (((unsigned int)(result)) == 33) goto loc_008B5BAF;
loc_008B5B81:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1096) + 584) != 0) goto loc_008B5B92;
    if (((unsigned int)(result)) == 34) goto loc_008B5BAF;
loc_008B5B92:
    v_rdi = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1096) + 584);
    if (((unsigned int)(result)) == 33) { v_rdi = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 1096) + 576); }
    a3 = 0;
    a2 = 0;
    result = AuthzBasepQueryClaimAttributesToken(v_rdi, a2, a3, v_stack_p10);
    goto loc_008B5BDB;
loc_008B5BAF:
    v_stack_m60 = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_m68 = v_stack_m70;
    v_stack_m70 = v_stack_m70;
    v_stack_m50 = v_stack_m58;
    v_stack_m58 = v_stack_m58;
loc_008B5BDB:
    result = ExAllocatePool2(256, 16, (unsigned int)(0x20206553ULL), v_stack_p10);
    if (result != 0) goto loc_008B5BFE;
    goto loc_008B5173;
loc_008B5BFE:
    result = AuthzBasepQueryClaimAttributesToken(v_stack_m78, result, 16, v_stack_p10);
    result = ExReleaseResourceLite(*(unsigned __int64 *)(a1 + 48), result, 16, v_stack_p10);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(a1 + 48), result, 16, v_stack_p10);
    if (!sign_flag) goto loc_008B5C35;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, 16, v_stack_p10);
loc_008B5C2E:
    goto loc_008B63D2;
loc_008B5C35:
    *(unsigned __int64 *)(a3) = result;
    goto loc_008B5C2E;
loc_008B5C3A:
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 48), 1, 16, v_stack_p10);
    v_rbx = (unsigned int)((unsigned int)(result));
    if (*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1080) != 0) {
        v_rbx = *(unsigned int *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1080) + 40);
    }
    result = ExReleaseResourceLite(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 48), 1, 16, v_stack_p10);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 48), 1, 16, v_stack_p10);
    *(unsigned int *)(a3) = (unsigned int)(v_rbx);
    goto loc_008B63D0;
loc_008B5C7E:
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 48), 1, 16, v_stack_p10);
    if (*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 784) == 0) goto loc_008B5CB7;
    goto loc_008B5CBC;
loc_008B5CB7:
loc_008B5CBC:
    result = ExAllocatePool2(256, 8, (unsigned int)(0x20206553ULL), v_stack_p10);
    if (result == 0) goto loc_008B516F;
    if (*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 784) == 0) goto loc_008B5CF5;
loc_008B5CE6:
    result = RtlCopySid(8 - 8, result + 8, *(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 784), v_stack_p10);
loc_008B5CF5:
    *(unsigned __int64 *)(result) = result + 8;
    goto loc_008B559E;
loc_008B5CFE:
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 48), 1, *(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 784), v_stack_p10);
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(result)) + 800))))) << (4));
    v_r12 = (unsigned int)((v_r12) + (24));
    if ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(result)) + 800))) == 0) goto loc_008B5D61;
loc_008B5D47:
    a2 = (*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 792)) + (1 + 15);
    v_r12 = (unsigned int)((v_r12 + *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 792)) + 1) * 4) + (8));
    a3 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(result)) + 800))))) - (1);
    if (condition_is_not_equal) goto loc_008B5D47;
loc_008B5D61:
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))), (unsigned int)(0x20206553ULL), v_stack_p10);
    if (result == 0) goto loc_008B516F;
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(result)) + 800)));
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(result)) + 800))))) << (4));
    v_stack_mE8 = v_stack_p8;
    a2 = (a2) + (24);
    a2 = (a2) + (result);
    v_stack_mF0 = v_stack_p8;
    v_stack_mF8 = a2;
    goto loc_008B5417;
loc_008B5DC0:
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(result)) + 800)) + 48), 1, (unsigned int)(0x20206553ULL), result + 8);
    if (*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1096) == 0) goto loc_008B5E04;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1096)))) == 0) goto loc_008B5E04;
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1096)))))) << (4));
    v_r12 = (unsigned int)((v_r12) + (8));
    goto loc_008B5E0D;
loc_008B5E04:
loc_008B5E0D:
    if ((unsigned int)((unsigned int)((unsigned int)(v_rbx))) == 0) goto loc_008B5E3B;
loc_008B5E21:
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1096) + 8)) + (16);
    v_r12 = (unsigned int)((24 + *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1096) + 8)) + 1) * 4) + (8));
    a3 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rbx))))) - (1);
    if (condition_is_not_equal) goto loc_008B5E21;
loc_008B5E3B:
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r12)))), (unsigned int)(0x20206553ULL), result + 8);
    if (result == 0) goto loc_008B516F;
    result = 0;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned __int64 *)(result + 16) = 0;
    *(unsigned int *)(result) = (unsigned int)((unsigned int)((unsigned int)(v_rbx)));
    v_r13 = (unsigned int)((unsigned int)(v_rbx));
    if ((unsigned int)((unsigned int)((unsigned int)(v_rbx))) != 0) {
        a1 = *(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1096);
        result = v_stack_p8;
        v_stack_mE8 = result;
        a4 = result + 8;
        v_r13 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) << (4));
        result = v_stack_p8;
        v_r13 = (unsigned int)((v_r13) - (16));
        v_stack_mF0 = result;
        a2 = (unsigned int)(v_r13);
        a3 = (unsigned int)(v_r12);
        a2 = (a2) + (24);
        a2 = (a2) + (result);
        v_stack_mF8 = a2;
        a2 = *(unsigned __int64 *)(a1 + 8);
        a1 = *(unsigned int *)(a1);
        result = RtlCopySidAndAttributesArray(a1, a2, a3, a4);
    }
    result = ExReleaseResourceLite(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 48), a2, a3, a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 48), a2, a3, a4);
    *(unsigned __int64 *)(a3) = result;
    goto loc_008B63D0;
loc_008B5EC5:
    v_rsi = (unsigned int)((16) - (41));
    if (condition_is_equal) goto loc_008B5FA4;
    v_rsi = (unsigned int)((v_rsi) - (1));
    if (condition_is_equal) goto loc_008B5F98;
    v_rsi = (unsigned int)((v_rsi) - (2));
    if (condition_is_equal) goto loc_008B5F0B;
    if (((unsigned int)(v_rsi)) != 2) goto loc_008B56A4;
    if (((*(unsigned int *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 48) + 200)) & (0x4000ULL)) == 0) goto loc_008B5F00;
    result = SepCanTokenMatchAllPackageSid(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 48), a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_008B5F00;
    goto loc_008B5F03;
loc_008B5F00:
loc_008B5F03:
    *(unsigned int *)(a3) = (unsigned int)((unsigned int)((unsigned int)(v_rbx)));
    goto loc_008B63D0;
loc_008B5F0B:
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 48) + 48), 1, a3, a4);
    result = *(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1152);
    v_rsi = 1 + 15;
    if (*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1152) != 0) {
        result = *(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1152) + 42);
        v_rsi = (1 + 15) + (result);
    }
    result = ExAllocatePool2(256, v_rsi, (unsigned int)(0x20206553ULL), a4);
    if (result == 0) goto loc_008B516F;
    if ((*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1152)) == v_rbx) goto loc_008B5F8D;
    *(unsigned __int8 *)(result + 8) = 1;
    *(unsigned __int64 *)(result) = result + 16;
    goto loc_008B549A;
loc_008B5F8D:
    *(unsigned __int8 *)(result + 8) = (unsigned __int8)(v_rbx);
loc_008B5F90:
    *(unsigned __int64 *)(result) = v_rbx;
    goto loc_008B5199;
loc_008B5F98:
    goto loc_008B5840;
loc_008B5FA4:
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(result + 16 + 48), 1, *(unsigned __int16 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1152) + 42), a4);
    if (*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1104) == 0) goto loc_008B5FDD;
    goto loc_008B5FE2;
loc_008B5FDD:
loc_008B5FE2:
    result = ExAllocatePool2(256, 8, (unsigned int)(0x20206553ULL), a4);
    if (result == 0) goto loc_008B516F;
    if (*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1104) == 0) goto loc_008B5CF5;
    goto loc_008B5CE6;
loc_008B6015:
    a1 = (unsigned int)((8) - (48));
    if (condition_is_equal) goto loc_008B630F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008B6280;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008B630F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008B630F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008B630F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008B630F;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008B61D5;
    a1 = (unsigned int)((a1) - (1));
    if (condition_is_equal) goto loc_008B6139;
    if (((unsigned int)(a1)) != 1) goto loc_008B56A4;
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(a1, 8, *(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1104), a4);
    if ((unsigned int)(result) == 0) goto loc_008B56A4;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 48), 1, *(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1104), a4);
    if (*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1176) == 0) goto loc_008B6266;
    if ((*(unsigned int *)((unsigned int)((unsigned int)(result)) + 1184)) < 3) goto loc_008B6113;
    result = SepIsAppSuiteSid(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1176) + 32), 1, *(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1104), a4);
    if ((unsigned __int8)(result) == 0) goto loc_008B6113;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1176) + 32) + 1) * 4 + 16)), (unsigned int)(0x20206553ULL), a4);
    if (result == 0) goto loc_008B516F;
    result = RtlCopySid(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1176) + 32) + 1) * 4 + 16 - 8, result + 8, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1176) + 32), a4);
    *(unsigned __int64 *)(result) = result + 8;
    goto loc_008B5199;
loc_008B6113:
    result = ExAllocatePool2(256, 8, (unsigned int)(0x20206553ULL), a4);
    if (result != 0) goto loc_008B5F90;
    goto loc_008B516F;
loc_008B6139:
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(256, 8, (unsigned int)(0x20206553ULL), a4);
    if ((unsigned int)(result) == 0) goto loc_008B56A4;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 48), 1, (unsigned int)(0x20206553ULL), a4);
    if (*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1176) == 0) goto loc_008B6266;
    if ((*(unsigned int *)((unsigned int)((unsigned int)(result)) + 1184)) < 2) goto loc_008B6266;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1176) + 16) == 0) goto loc_008B6199;
    goto loc_008B619E;
loc_008B6199:
loc_008B619E:
    result = ExAllocatePool2(256, 8, (unsigned int)(0x20206553ULL), a4);
    if (result == 0) goto loc_008B516F;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1176) + 16) == 0) goto loc_008B5CF5;
    goto loc_008B5CE6;
loc_008B61D5:
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(256, 8, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1176) + 16), a4);
    if ((unsigned int)(result) == 0) goto loc_008B56A4;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 48), 1, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1176) + 16), a4);
    if (*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1176) == 0) goto loc_008B6266;
    if ((*(unsigned int *)((unsigned int)((unsigned int)(result)) + 1184)) == ((unsigned int)(result + 8))) goto loc_008B6266;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1176)) == 0) goto loc_008B622B;
    goto loc_008B6230;
loc_008B622B:
loc_008B6230:
    result = ExAllocatePool2(256, 8, (unsigned int)(0x20206553ULL), a4);
    if (result == 0) goto loc_008B516F;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1176)) == 0) goto loc_008B5CF5;
    goto loc_008B5CE6;
loc_008B6266:
    result = ExReleaseResourceLite(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 48), 8, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1176)), a4);
loc_008B6274:
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 48), 8, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1176)), a4);
    goto loc_008B63D2;
loc_008B6280:
    v_stack_m98 = (unsigned int)((unsigned int)(0xC000000DULL));
    v_stack_p20 = (unsigned int)((unsigned int)(0xC000000DULL));
    v_stack_p8 = (unsigned int)((unsigned int)(0xC000000DULL));
    v_stack_p10 = (unsigned int)((unsigned int)(0xC000000DULL));
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 48), 1, *(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)((unsigned int)(result)) + 1176)), a4);
    v_stack_mF8 = v_stack_p10;
    result = SepGetTokenLoggingInformationBufferSize((unsigned int)((unsigned int)(result)), v_stack_m98, v_stack_p20, v_stack_p8);
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(result)), (unsigned int)(0x20206553ULL), v_stack_p8);
    if (result == 0) goto loc_008B53D7;
    v_stack_mE8 = (unsigned int)((unsigned int)(v_stack_p10));
    v_stack_mF0 = (unsigned int)((unsigned int)(v_stack_p8));
    v_stack_mF8 = (unsigned int)((unsigned int)(v_stack_p20));
    result = SepCopyTokenLoggingInformation((unsigned int)((unsigned int)(result)), result, (unsigned int)(0x20206553ULL), (unsigned int)(v_stack_m98));
    goto loc_008B5199;
loc_008B630F:
    if (((unsigned int)(result)) != 48) goto loc_008B6340;
    v_stack_mF0 = (unsigned __int8)((unsigned int)(0xC000000DULL));
    a4 = 0;
    a2 = 0;
    v_stack_mF8 = 1;
    result = SepSidInTokenSidHash((unsigned int)((unsigned int)(result)) + 808, a2, *(unsigned __int64 *)(v_rip + 5970109), a4);
    *(unsigned int *)(a3) = (unsigned int)((unsigned __int8)(result));
    goto loc_008B63D0;
loc_008B6340:
    if (((unsigned int)(result)) != 47) goto loc_008B6361;
loc_008B6345:
    result = SepIsSandboxedToken((unsigned int)((unsigned int)(result)), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), *(unsigned __int64 *)(v_rip + 5970109), a4);
loc_008B635C:
    *(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 5970109)) = (unsigned __int8)(result);
    goto loc_008B63D0;
loc_008B6361:
    if (((unsigned int)(result)) != 51) goto loc_008B637E;
    result = Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline((unsigned int)((unsigned int)(result)), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), *(unsigned __int64 *)(v_rip + 5970109), a4);
    if ((unsigned int)(result) == 0) goto loc_008B56A4;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(result)) + 200))) >> (27));
    goto loc_008B6396;
loc_008B637E:
    if (((unsigned int)(result)) != 52) goto loc_008B639D;
    result = Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline((unsigned int)((unsigned int)(result)), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), *(unsigned __int64 *)(v_rip + 5970109), a4);
    if ((unsigned int)(result) == 0) goto loc_008B56A4;
loc_008B6396:
    result = (unsigned __int8)((*(unsigned __int8 *)((unsigned int)((unsigned int)(result)) + 1168)) & (1));
    *(unsigned __int8 *)(a3) = (unsigned __int8)(result);
    goto loc_008B63D0;
loc_008B639D:
    if (((unsigned int)(result)) != 53) goto loc_008B63BF;
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline((unsigned int)((unsigned int)(result)), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), *(unsigned __int64 *)(v_rip + 5970109), a4);
    if ((unsigned int)(result) == 0) goto loc_008B56A4;
    result = SeHasTamperProtection((unsigned int)((unsigned int)(result)), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562), *(unsigned __int64 *)(v_rip + 5970109), a4);
    *(unsigned int *)(a3) = (unsigned int)((unsigned __int8)(result));
    goto loc_008B63D0;
loc_008B63BF:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(result)) + 200))) & (0x3000000ULL));
    result = (unsigned int)((result) >> (24));
loc_008B63CD:
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 5970109)) = (unsigned int)(result);
loc_008B63D0:
    result = 0;
loc_008B63D2:
    v_rsp = (v_rsp) + (224);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SeQueryInformationToken(void *Arg1, int32_t Arg2, void *Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint32_t v_stack_m84;
    uint32_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint32_t v_stack_m90;
    uint32_t v_stack_m94;
    uint32_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint8_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (224);
    local_rbx = 0;
    v_stack_p10 = 0;
    v_stack_m98 = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    if (Arg2 > 29) goto loc_008B5AF1;
    if (Arg2 == 29) goto loc_008B5AC3;
    if (Arg2 > 12) goto loc_008B5655;
    if (Arg2 == 12) goto loc_008B5648;
    if (Arg2 > 6) goto loc_008B54A4;
    if (Arg2 == 6) goto loc_008B5424;
    local_rsi = (uint32_t)(((uint32_t)(Arg2)) - (1));
    if (condition_is_equal) goto loc_008B5383;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_008B529C;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_008B522D;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_008B51AF;
    if (((uint32_t)(local_rsi)) != 1) goto loc_008B56A4;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(arg1 + 0x30), (uint32_t)((uint32_t)(local_rsi)), Arg3, a4);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x1) * 4 + 16)), (uint32_t)(0x20206553ULL), a4);
    if (result != 0) goto loc_008B5182;
loc_008B516F:
loc_008B5173:
    result = ExReleaseResourceLite(*(uint64_t *)(arg1 + 0x30), (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x1) * 4 + 16)), (uint32_t)(0x20206553ULL), a4);
    goto loc_008B6274;
loc_008B5182:
    *(uint64_t *)(result) = result + 8;
loc_008B5190:
    result = RtlCopySid(*(uint8_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x1) * 4 + 16 - 8, result + 8, *(uint64_t *)(arg1 + 0xA8), a4);
loc_008B5199:
    result = ExReleaseResourceLite(*(uint64_t *)(arg1 + 0x30), result + 8, *(uint64_t *)(arg1 + 0xA8), a4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(arg1 + 0x30), result + 8, *(uint64_t *)(arg1 + 0xA8), a4);
loc_008B51A7:
    *(uint64_t *)(arg3) = result;
    goto loc_008B63D0;
loc_008B51AF:
    result = ExAcquireResourceSharedLite(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x30), 1, *(uint64_t *)(arg1 + 0xA8), a4);
    Arg1 = ((uint32_t)(*(uint32_t *)(arg1 + 0x90))) + ((uint32_t)(*(uint32_t *)(arg1 + 0x90)));
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x98) + arg1 * 8) + 0x1) * 4 + 16)), (uint32_t)(0x20206553ULL), a4);
    if (result == 0) goto loc_008B53D7;
    *(uint64_t *)(result) = result + 8;
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x90))) + ((uint32_t)(*(uint32_t *)(arg1 + 0x90)));
    goto loc_008B5190;
loc_008B522D:
    result = ExAcquireResourceSharedLite(*(uint64_t *)(256 + 0x30), 1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x98) + result * 8), a4);
    result = SepTokenPrivilegeCount(Arg1, 1, *(uint64_t *)(*(uint64_t *)(arg1 + 0x98) + result * 8), a4);
    if (((uint32_t)(result)) <= 1) goto loc_008B5269;
    goto loc_008B526E;
loc_008B5269:
loc_008B526E:
    result = ExAllocatePool2(256, 16, (uint32_t)(0x20206553ULL), a4);
    if (result == 0) goto loc_008B53D7;
    result = SepConvertTokenPrivileges(Arg1, result, (uint32_t)(0x20206553ULL), a4);
    goto loc_008B5199;
loc_008B529C:
    result = ExAcquireResourceSharedLite(*(uint64_t *)(arg1 + 0x30), 1, (uint32_t)(0x20206553ULL), a4);
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C))))) << (4));
    local_r12 = (uint32_t)((local_r12) + (-8));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C)))) <= 1) goto loc_008B5301;
    Arg2 = (*(uint64_t *)(arg1 + 0x98)) + (1 + 15);
loc_008B52E7:
    Arg2 = (Arg2) + (1 + 15);
    local_r12 = (uint32_t)((local_r12 + *(uint8_t *)(*(uint64_t *)(Arg2) + 0x1) * 4) + (8));
    Arg3 = ((uint32_t)(*(uint32_t *)(arg1 + 0x7C)) - 1) - (1);
    if (condition_is_not_equal) goto loc_008B52E7;
loc_008B5301:
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))), (uint32_t)(0x20206553ULL), a4);
    if (result == 0) goto loc_008B53D7;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x7C))) - (1));
    *(uint32_t *)(result) = (uint32_t)(result);
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C))))) << (4));
    Arg2 = (*(uint64_t *)(arg1 + 0x98)) + (1 + 15);
    local_r10 = (uint32_t)((local_r10) - (32));
    v_stack_mE8 = v_stack_p8;
    local_r10 = (local_r10) + (24);
    local_r10 = (local_r10) + (result);
    v_stack_mF0 = v_stack_p8;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x7C))) - 1);
    v_stack_mF8 = local_r10;
    result = RtlCopySidAndAttributesArray(Arg1, Arg2, (uint32_t)((uint32_t)(local_r12)), result + 8);
    result = ExReleaseResourceLite(*(uint64_t *)(arg1 + 0x30), Arg2, (uint32_t)((uint32_t)(local_r12)), result + 8);
    result = KeLeaveCriticalRegion(*(uint64_t *)(arg1 + 0x30), Arg2, (uint32_t)((uint32_t)(local_r12)), result + 8);
    *(uint64_t *)(arg3) = result;
    goto loc_008B63D0;
loc_008B5383:
    result = ExAcquireResourceSharedLite(*(uint64_t *)(*(uint64_t *)(arg1 + 0x30) + 0x30), 1, (uint32_t)((uint32_t)(local_r12)), result + 8);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x98)) + 0x1) * 4 + 24)), (uint32_t)(0x20206553ULL), result + 8);
    if (result != 0) goto loc_008B53EF;
loc_008B53D7:
    result = ExReleaseResourceLite(*(uint64_t *)(arg1 + 0x30), (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x98)) + 0x1) * 4 + 24)), (uint32_t)(0x20206553ULL), result + 8);
    result = KeLeaveCriticalRegion(*(uint64_t *)(arg1 + 0x30), (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x98)) + 0x1) * 4 + 24)), (uint32_t)(0x20206553ULL), result + 8);
loc_008B53E5:
    goto loc_008B63D2;
loc_008B53EF:
    v_stack_mE8 = v_stack_p8;
    result = ((uint32_t)(0xC000009AULL)) + (16);
    v_stack_mF0 = v_stack_p8;
    v_stack_mF8 = result;
loc_008B5417:
    result = RtlCopySidAndAttributesArray(1, *(uint64_t *)(arg1 + 0x98), (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x98)) + 0x1) * 4 + 24)), result);
    goto loc_008B5199;
loc_008B5424:
    result = ExAcquireResourceSharedLite(*(uint64_t *)(1 + 0x30), 1, (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x98)) + 0x1) * 4 + 24)), result);
    result = *(uint64_t *)(arg1 + 0xB8);
    local_rsi = 8;
    if (*(uint64_t *)(arg1 + 0xB8) != 0) {
        result = *(uint16_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x2);
        local_rsi = (8) + (result);
    }
    result = ExAllocatePool2(256, local_rsi, (uint32_t)(0x20206553ULL), result);
    if (result == 0) goto loc_008B516F;
    if ((*(uint64_t *)(arg1 + 0xB8)) == ((uint32_t)(0xC000009AULL))) goto loc_008B5F90;
    *(uint64_t *)(result) = result + 8;
loc_008B549A:
    result = memcpy(result + 8, *(uint64_t *)(arg1 + 0xB8), *(uint16_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x2), result);
    goto loc_008B5199;
loc_008B54A4:
    local_rsi = (uint32_t)((result) - (7));
    if (condition_is_equal) goto loc_008B561B;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_008B55F2;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_008B55B4;
    if (((uint32_t)(local_rsi)) != 1) goto loc_008B56A4;
    result = ExAllocatePool2(256, local_rsi + 55, (uint32_t)(0x20206553ULL), result);
    if (result == 0) goto loc_008B53E5;
    *(uint64_t *)(result) = *(uint64_t *)(arg1 + 0x10);
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(arg1 + 0x18);
    *(uint32_t *)(result + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC0)));
    *(uint32_t *)(result + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC4)));
    *(uint64_t *)(result + 0x10) = *(uint64_t *)(arg1 + 0x28);
    result = ExAcquireResourceSharedLite(*(uint64_t *)(arg1 + 0x30), (uint8_t)((uint32_t)((uint32_t)(local_rsi))), (uint32_t)(0x20206553ULL), result);
    *(uint32_t *)(result + 0x20) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x88)));
    Arg1 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(arg1 + 0xA8) + 0x1)) << (2));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x88))) - ((uint32_t)(Arg1)));
    Arg2 = (uint32_t)((Arg2) - (8));
    result = *(uint64_t *)(arg1 + 0xB8);
    if (*(uint64_t *)(arg1 + 0xB8) != 0) {
        result = *(uint16_t *)(*(uint64_t *)(arg1 + 0xB8) + 0x2);
        Arg2 = (uint32_t)((Arg2) - ((uint32_t)(result)));
    }
    *(uint32_t *)(result + 0x24) = Arg2;
    *(uint32_t *)(result + 0x24) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8C)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x7C))) - ((uint32_t)((uint32_t)((uint32_t)(local_rsi)))));
    *(uint32_t *)(result + 0x28) = (uint32_t)(result);
    result = SepTokenPrivilegeCount(Arg1, Arg2, (uint32_t)(0x20206553ULL), result);
    *(uint32_t *)(result + 0x2C) = (uint32_t)(result);
    *(uint64_t *)(result + 0x30) = *(uint64_t *)(arg1 + 0x38);
loc_008B559E:
    result = ExReleaseResourceLite(*(uint64_t *)(arg1 + 0x30), Arg2, (uint32_t)(0x20206553ULL), result);
    result = KeLeaveCriticalRegion(*(uint64_t *)(arg1 + 0x30), Arg2, (uint32_t)(0x20206553ULL), result);
    *(uint64_t *)(arg3) = result;
    goto loc_008B63D0;
loc_008B55B4:
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x30) + 0xC0)) != 2) goto loc_008B56A4;
    result = ExAllocatePool2(256, 4, (uint32_t)(0x20206553ULL), result);
    if (result == 0) goto loc_008B53E5;
loc_008B55E8:
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC4)));
    *(uint64_t *)(arg3) = result;
    goto loc_008B63D0;
loc_008B55F2:
    result = ExAllocatePool2(256, 4, (uint32_t)(0x20206553ULL), result);
    if (result == 0) goto loc_008B53E5;
    goto loc_008B55E8;
loc_008B561B:
    result = ExAllocatePool2(256, 16, (uint32_t)(0x20206553ULL), result);
    if (result == 0) goto loc_008B53E5;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(arg3) = result;
    goto loc_008B63D0;
loc_008B5648:
    result = SeQuerySessionIdToken(256, Arg3, (uint32_t)(0x20206553ULL), result);
    goto loc_008B63D0;
loc_008B5655:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) - (13));
    if (condition_is_equal) goto loc_008B5904;
    Arg1 = (uint32_t)((Arg1) - (5));
    if (condition_is_equal) goto loc_008B58D1;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_008B5872;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008B5832;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008B5716;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008B5832;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008B5832;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008B56AE;
    if (((uint32_t)(Arg1)) == 1) goto loc_008B5832;
loc_008B56A4:
    goto loc_008B63D2;
loc_008B56AE:
    v_stack_m48 = v_xmm0;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(arg1 + 0x30), 1, (uint32_t)(0x20206553ULL), result);
    result = SepCopyTokenIntegrity(Arg1, v_stack_m48, (uint32_t)(0x20206553ULL), result);
    result = RtlSubAuthorityCountSid(v_stack_m48, v_stack_m48, (uint32_t)(0x20206553ULL), result);
    if ((uint8_t)(*(uint8_t *)(result)) != 0) goto loc_008B56F5;
    goto loc_008B5705;
loc_008B56F5:
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint8_t *)(result)))) - (1));
    result = RtlSubAuthoritySid(v_stack_m48, Arg2, (uint32_t)(0x20206553ULL), result);
loc_008B5705:
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    result = ExReleaseResourceLite(*(uint64_t *)(arg1 + 0x30), Arg2, (uint32_t)(0x20206553ULL), result);
    goto loc_008B6274;
loc_008B5716:
    v_stack_m80 = (uint32_t)((uint32_t)(0xC000009AULL));
    v_stack_m84 = (uint32_t)((uint32_t)(0xC000009AULL));
    v_stack_m88 = (uint32_t)((uint32_t)(0xC000009AULL));
    v_stack_m8C = (uint32_t)((uint32_t)(0xC000009AULL));
    v_stack_m90 = (uint32_t)((uint32_t)(0xC000009AULL));
    v_stack_m94 = (uint32_t)((uint32_t)(0xC000009AULL));
    v_stack_p20 = (uint32_t)((uint32_t)(0xC000009AULL));
    v_stack_p8 = (uint32_t)((uint32_t)(0xC000009AULL));
    v_stack_p10 = (uint32_t)((uint32_t)(0xC000009AULL));
    result = ExAcquireResourceSharedLite(*(uint64_t *)(arg1 + 0x30), 1, (uint32_t)(0x20206553ULL), result);
    Arg3 = 0;
    v_stack_mB8 = v_stack_p10;
    Arg2 = 0;
    v_stack_mC0 = v_stack_p8;
    v_stack_mC8 = v_stack_p20;
    v_stack_mD0 = v_stack_m94;
    v_stack_mD8 = v_stack_m90;
    v_stack_mE0 = v_stack_m8C;
    v_stack_mE8 = v_stack_m88;
    v_stack_mF0 = v_stack_m84;
    v_stack_mF8 = v_stack_m80;
    result = SepGetTokenAccessInformationBufferSize(Arg1, Arg2, Arg3, v_stack_m98);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result)), (uint32_t)(0x20206553ULL), v_stack_m98);
    if (result == 0) goto loc_008B53D7;
    v_stack_mA8 = (uint32_t)(0xC000009AULL);
    v_stack_mB0 = (uint8_t)((uint32_t)(0xC000009AULL));
    v_stack_mB8 = (uint32_t)((uint32_t)(v_stack_p10));
    v_stack_mC0 = (uint32_t)((uint32_t)(v_stack_p8));
    v_stack_mC8 = (uint32_t)((uint32_t)(v_stack_p20));
    v_stack_mD0 = (uint32_t)((uint32_t)(v_stack_m94));
    v_stack_mD8 = (uint32_t)((uint32_t)(v_stack_m90));
    v_stack_mE0 = (uint32_t)((uint32_t)(v_stack_m8C));
    v_stack_mE8 = (uint32_t)((uint32_t)(v_stack_m88));
    v_stack_mF0 = (uint32_t)((uint32_t)(v_stack_m84));
    v_stack_mF8 = (uint32_t)((uint32_t)(v_stack_m80));
    result = SepCopyTokenAccessInformation(Arg1, result, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)(v_stack_m98));
    goto loc_008B5199;
loc_008B5832:
    if (((uint32_t)(result)) != 23) goto loc_008B5848;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xC8))) >> (9));
loc_008B5840:
    result = (uint32_t)((result) & (1));
    goto loc_008B63CD;
loc_008B5848:
    if (((uint32_t)(result)) != 24) goto loc_008B585E;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xC8))) >> (10));
    goto loc_008B5840;
loc_008B585E:
    if (((uint32_t)(result)) != 26) goto loc_008B5AC3;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xC8))) >> (12));
    goto loc_008B5840;
loc_008B5872:
    result = ExAllocatePool2(256, 4, (uint32_t)(0x20206553ULL), (uint32_t)(v_stack_m98));
    if (result == 0) goto loc_008B53E5;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(arg1 + 0x30), 1, (uint32_t)(0x20206553ULL), (uint32_t)(v_stack_m98));
    result = SepGetTokenElevation(Arg1, 1, (uint32_t)(0x20206553ULL), (uint32_t)(v_stack_m98));
    result = ExReleaseResourceLite(*(uint64_t *)(arg1 + 0x30), 1, (uint32_t)(0x20206553ULL), (uint32_t)(v_stack_m98));
    result = KeLeaveCriticalRegion(*(uint64_t *)(arg1 + 0x30), 1, (uint32_t)(0x20206553ULL), (uint32_t)(v_stack_m98));
    *(uint32_t *)(result) = (uint32_t)((uint32_t)((uint32_t)(result)));
    goto loc_008B51A7;
loc_008B58D1:
    result = ExAllocatePool2(256, 4, (uint32_t)(0x20206553ULL), (uint32_t)(v_stack_m98));
    if (result == 0) goto loc_008B53E5;
    result = SepGetTokenElevationType(Arg1, result, (uint32_t)(0x20206553ULL), (uint32_t)(v_stack_m98));
    *(uint32_t *)(result) = (uint32_t)(result);
    *(uint64_t *)(arg3) = result;
    goto loc_008B63D0;
loc_008B5904:
    result = ExAcquireResourceSharedLite(*(uint64_t *)(arg1 + 0x30), 1, (uint32_t)(0x20206553ULL), (uint32_t)(v_stack_m98));
    result = SepTokenPrivilegeCount(Arg1, 1, (uint32_t)(0x20206553ULL), (uint32_t)(v_stack_m98));
    v_stack_p8 = (uint32_t)(result);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C))))) << (4));
    a4 = (uint32_t)((result + result * 2) << (2));
    v_stack_p10 = (uint32_t)(a4);
    v_stack_p20 = (uint32_t)(result);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C))) == 0) goto loc_008B5980;
loc_008B5964:
    Arg2 = (*(uint64_t *)(arg1 + 0x98)) + (1 + 15);
    Arg1 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x98)) + 0x1) * 4 + 15) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)(result))) + ((uint32_t)(Arg1)));
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C))))) - (1);
    if (condition_is_not_equal) goto loc_008B5964;
loc_008B5980:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x80))))) << (4));
    v_stack_m98 = (uint32_t)(result);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x80))) == 0) goto loc_008B59BB;
loc_008B599F:
    Arg2 = (*(uint64_t *)(arg1 + 0xA0)) + (1 + 15);
    Arg1 = (uint32_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0xA0)) + 0x1) * 4 + 15) & ((uint32_t)((uint32_t)(0xFFFFFFF8ULL))));
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(result))) + ((uint32_t)(Arg1)));
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x80))))) - (1);
    if (condition_is_not_equal) goto loc_008B599F;
loc_008B59BB:
    a4 = (uint32_t)((a4) + (56));
    Arg2 = (uint32_t)((local_r12 + local_r13 * 1) + ((uint32_t)(a4)));
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x20206553ULL), a4);
    if (result == 0) goto loc_008B53D7;
    *(uint64_t *)(result + 0x30) = *(uint64_t *)(arg1 + 0x18);
    *(uint32_t *)(result + 0x4) = (uint32_t)(local_r13);
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x7C)));
    *(uint64_t *)(result + 0x8) = result + 56;
    *(uint32_t *)(result + 0x14) = (uint32_t)(local_r12);
    *(uint32_t *)(result + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x80)));
    if ((*(uint32_t *)(arg1 + 0x80)) == ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_008B5A20;
    result = ((uint32_t)((uint32_t)(local_r13)) + 7) & (-8);
    result = (result) + (result + 56);
    goto loc_008B5A23;
loc_008B5A20:
loc_008B5A23:
    *(uint64_t *)(result + 0x18) = (uint32_t)((uint32_t)(result));
    *(uint32_t *)(result + 0x24) = (uint32_t)((uint32_t)(v_stack_p10));
    *(uint32_t *)(result + 0x20) = (uint32_t)((uint32_t)(v_stack_p8));
    result = ((uint32_t)((uint32_t)(local_r12))) + ((uint32_t)((uint32_t)(local_r13)));
    local_r13 = (uint32_t)((local_r13) - ((uint32_t)((uint32_t)(v_stack_p20))));
    result = (result) + (result + 56);
    *(uint64_t *)(result + 0x28) = result;
    v_stack_mE8 = v_stack_p8;
    v_stack_mF0 = v_stack_p8;
    v_stack_mF8 = result + 56 + (uint32_t)(v_stack_p20) * 1;
    result = RtlCopySidAndAttributesArray((uint32_t)(*(uint32_t *)(arg1 + 0x7C)), *(uint64_t *)(arg1 + 0x98), (uint32_t)((uint32_t)(local_r13)), result + 56);
    if ((*(uint32_t *)(result + 0x10)) >= = ((uint32_t)((uint32_t)((uint32_t)(result))))) {
        Arg1 = v_stack_m98;
        a4 = *(uint64_t *)(result + 0x18);
        local_r12 = (uint32_t)((local_r12) - ((uint32_t)(Arg1)));
        Arg2 = *(uint64_t *)(arg1 + 0xA0);
        Arg3 = (uint32_t)(local_r12);
        result = a4 + Arg1 * 1;
        Arg1 = v_stack_p8;
        v_stack_mE8 = Arg1;
        Arg1 = v_stack_p8;
        v_stack_mF0 = Arg1;
        Arg1 = *(uint32_t *)(arg1 + 0x80);
        v_stack_mF8 = result;
        result = RtlCopySidAndAttributesArray(Arg1, Arg2, Arg3, a4);
    }
    result = SepConvertTokenPrivilegesToLuidAndAttributes(Arg1, *(uint64_t *)(result + 0x28), Arg3, a4);
    goto loc_008B5199;
loc_008B5AC3:
    if (((uint32_t)(result)) != 29) goto loc_008B5AD6;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0xC8))) >> (14));
    goto loc_008B5840;
loc_008B5AD6:
    if (((uint32_t)(result)) != 21) goto loc_008B63BF;
    result = (((*(uint32_t *)(arg1 + 0xC8)) & (0x810ULL)) != 0) ? 1 : 0;
    goto loc_008B635C;
loc_008B5AF1:
    if (((uint32_t)(result)) > 47) goto loc_008B6015;
    if (((uint32_t)(result)) == 47) goto loc_008B6345;
    if (((uint32_t)(result)) > 37) goto loc_008B5EC5;
    if (((uint32_t)(result)) == 37) goto loc_008B5DC0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) - (30));
    if (condition_is_equal) goto loc_008B5CFE;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008B5C7E;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008B5C3A;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008B5B3A;
    if (((uint32_t)(Arg1)) != 1) goto loc_008B56A4;
loc_008B5B3A:
    *(uint64_t *)(arg3) = (uint32_t)((uint32_t)(result));
    result = ExAcquireResourceSharedLite(*(uint64_t *)(arg1 + 0x30), 1, Arg3, a4);
    if (*(uint64_t *)(arg1 + 0x448) == 0) goto loc_008B5BAF;
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x448) + 0x240) != 0) goto loc_008B5B81;
    if (((uint32_t)(result)) == 33) goto loc_008B5BAF;
loc_008B5B81:
    if (*(uint64_t *)(*(uint64_t *)(arg1 + 0x448) + 0x248) != 0) goto loc_008B5B92;
    if (((uint32_t)(result)) == 34) goto loc_008B5BAF;
loc_008B5B92:
    local_rdi = *(uint64_t *)(*(uint64_t *)(arg1 + 0x448) + 0x248);
    if (((uint32_t)(result)) == 33) { local_rdi = *(uint64_t *)(*(uint64_t *)(arg1 + 0x448) + 0x240); }
    Arg3 = 0;
    Arg2 = 0;
    result = AuthzBasepQueryClaimAttributesToken(local_rdi, Arg2, Arg3, v_stack_p10);
    goto loc_008B5BDB;
loc_008B5BAF:
    v_stack_m60 = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_m68 = v_stack_m70;
    v_stack_m70 = v_stack_m70;
    v_stack_m50 = v_stack_m58;
    v_stack_m58 = v_stack_m58;
loc_008B5BDB:
    result = ExAllocatePool2(256, 16, (uint32_t)(0x20206553ULL), v_stack_p10);
    if (result != 0) goto loc_008B5BFE;
    goto loc_008B5173;
loc_008B5BFE:
    result = AuthzBasepQueryClaimAttributesToken(v_stack_m78, result, 16, v_stack_p10);
    result = ExReleaseResourceLite(*(uint64_t *)(arg1 + 0x30), result, 16, v_stack_p10);
    result = KeLeaveCriticalRegion(*(uint64_t *)(arg1 + 0x30), result, 16, v_stack_p10);
    if (!sign_flag) goto loc_008B5C35;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, 16, v_stack_p10);
loc_008B5C2E:
    goto loc_008B63D2;
loc_008B5C35:
    *(uint64_t *)(arg3) = result;
    goto loc_008B5C2E;
loc_008B5C3A:
    result = ExAcquireResourceSharedLite(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x30), 1, 16, v_stack_p10);
    local_rbx = (uint32_t)((uint32_t)(result));
    if (*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x438) != 0) {
        local_rbx = *(uint32_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x438) + 0x28);
    }
    result = ExReleaseResourceLite(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x30), 1, 16, v_stack_p10);
    result = KeLeaveCriticalRegion(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x30), 1, 16, v_stack_p10);
    *(uint32_t *)(arg3) = (uint32_t)(local_rbx);
    goto loc_008B63D0;
loc_008B5C7E:
    result = ExAcquireResourceSharedLite(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x30), 1, 16, v_stack_p10);
    if (*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x310) == 0) goto loc_008B5CB7;
    goto loc_008B5CBC;
loc_008B5CB7:
loc_008B5CBC:
    result = ExAllocatePool2(256, 8, (uint32_t)(0x20206553ULL), v_stack_p10);
    if (result == 0) goto loc_008B516F;
    if (*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x310) == 0) goto loc_008B5CF5;
loc_008B5CE6:
    result = RtlCopySid(8 - 8, result + 8, *(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x310), v_stack_p10);
loc_008B5CF5:
    *(uint64_t *)(result) = result + 8;
    goto loc_008B559E;
loc_008B5CFE:
    result = ExAcquireResourceSharedLite(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x30), 1, *(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x310), v_stack_p10);
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x320))))) << (4));
    local_r12 = (uint32_t)((local_r12) + (24));
    if ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x320))) == 0) goto loc_008B5D61;
loc_008B5D47:
    Arg2 = (*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x318)) + (1 + 15);
    local_r12 = (uint32_t)((local_r12 + *(uint8_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x318)) + 0x1) * 4) + (8));
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x320))))) - (1);
    if (condition_is_not_equal) goto loc_008B5D47;
loc_008B5D61:
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))), (uint32_t)(0x20206553ULL), v_stack_p10);
    if (result == 0) goto loc_008B516F;
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x320)));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x320))))) << (4));
    v_stack_mE8 = v_stack_p8;
    Arg2 = (Arg2) + (24);
    Arg2 = (Arg2) + (result);
    v_stack_mF0 = v_stack_p8;
    v_stack_mF8 = Arg2;
    goto loc_008B5417;
loc_008B5DC0:
    result = ExAcquireResourceSharedLite(*(uint64_t *)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x320)) + 0x30), 1, (uint32_t)(0x20206553ULL), result + 8);
    if (*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x448) == 0) goto loc_008B5E04;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x448)))) == 0) goto loc_008B5E04;
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x448)))))) << (4));
    local_r12 = (uint32_t)((local_r12) + (8));
    goto loc_008B5E0D;
loc_008B5E04:
loc_008B5E0D:
    if ((uint32_t)((uint32_t)((uint32_t)(local_rbx))) == 0) goto loc_008B5E3B;
loc_008B5E21:
    Arg2 = (*(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x448) + 0x8)) + (16);
    local_r12 = (uint32_t)((24 + *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x448) + 0x8)) + 0x1) * 4) + (8));
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rbx))))) - (1);
    if (condition_is_not_equal) goto loc_008B5E21;
loc_008B5E3B:
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r12)))), (uint32_t)(0x20206553ULL), result + 8);
    if (result == 0) goto loc_008B516F;
    result = 0;
    *(uint64_t *)(result) = v_xmm0;
    *(uint64_t *)(result + 0x10) = 0;
    *(uint32_t *)(result) = (uint32_t)((uint32_t)((uint32_t)(local_rbx)));
    local_r13 = (uint32_t)((uint32_t)(local_rbx));
    if ((uint32_t)((uint32_t)((uint32_t)(local_rbx))) != 0) {
        Arg1 = *(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x448);
        result = v_stack_p8;
        v_stack_mE8 = result;
        a4 = result + 8;
        local_r13 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) << (4));
        result = v_stack_p8;
        local_r13 = (uint32_t)((local_r13) - (16));
        v_stack_mF0 = result;
        Arg2 = (uint32_t)(local_r13);
        Arg3 = (uint32_t)(local_r12);
        Arg2 = (Arg2) + (24);
        Arg2 = (Arg2) + (result);
        v_stack_mF8 = Arg2;
        Arg2 = *(uint64_t *)(arg1 + 0x8);
        Arg1 = *(uint32_t *)(arg1);
        result = RtlCopySidAndAttributesArray(Arg1, Arg2, Arg3, a4);
    }
    result = ExReleaseResourceLite(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x30), Arg2, Arg3, a4);
    result = KeLeaveCriticalRegion(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x30), Arg2, Arg3, a4);
    *(uint64_t *)(arg3) = result;
    goto loc_008B63D0;
loc_008B5EC5:
    local_rsi = (uint32_t)((16) - (41));
    if (condition_is_equal) goto loc_008B5FA4;
    local_rsi = (uint32_t)((local_rsi) - (1));
    if (condition_is_equal) goto loc_008B5F98;
    local_rsi = (uint32_t)((local_rsi) - (2));
    if (condition_is_equal) goto loc_008B5F0B;
    if (((uint32_t)(local_rsi)) != 2) goto loc_008B56A4;
    if (((*(uint32_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x30) + 0xC8)) & (0x4000ULL)) == 0) goto loc_008B5F00;
    result = SepCanTokenMatchAllPackageSid(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x30), Arg2, Arg3, a4);
    if ((uint8_t)(result) != 0) goto loc_008B5F00;
    goto loc_008B5F03;
loc_008B5F00:
loc_008B5F03:
    *(uint32_t *)(arg3) = (uint32_t)((uint32_t)((uint32_t)(local_rbx)));
    goto loc_008B63D0;
loc_008B5F0B:
    result = ExAcquireResourceSharedLite(*(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x30) + 0x30), 1, Arg3, a4);
    result = *(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x480);
    local_rsi = 1 + 15;
    if (*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x480) != 0) {
        result = *(uint16_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x480) + 0x2A);
        local_rsi = (1 + 15) + (result);
    }
    result = ExAllocatePool2(256, local_rsi, (uint32_t)(0x20206553ULL), a4);
    if (result == 0) goto loc_008B516F;
    if ((*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x480)) == local_rbx) goto loc_008B5F8D;
    *(uint8_t *)(result + 0x8) = 1;
    *(uint64_t *)(result) = result + 16;
    goto loc_008B549A;
loc_008B5F8D:
    *(uint8_t *)(result + 0x8) = (uint8_t)(local_rbx);
loc_008B5F90:
    *(uint64_t *)(result) = local_rbx;
    goto loc_008B5199;
loc_008B5F98:
    goto loc_008B5840;
loc_008B5FA4:
    result = ExAcquireResourceSharedLite(*(uint64_t *)(result + 0x10 + 0x30), 1, *(uint16_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x480) + 0x2A), a4);
    if (*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x450) == 0) goto loc_008B5FDD;
    goto loc_008B5FE2;
loc_008B5FDD:
loc_008B5FE2:
    result = ExAllocatePool2(256, 8, (uint32_t)(0x20206553ULL), a4);
    if (result == 0) goto loc_008B516F;
    if (*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x450) == 0) goto loc_008B5CF5;
    goto loc_008B5CE6;
loc_008B6015:
    Arg1 = (uint32_t)((8) - (48));
    if (condition_is_equal) goto loc_008B630F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008B6280;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008B630F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008B630F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008B630F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008B630F;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008B61D5;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (condition_is_equal) goto loc_008B6139;
    if (((uint32_t)(Arg1)) != 1) goto loc_008B56A4;
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(Arg1, 8, *(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x450), a4);
    if ((uint32_t)(result) == 0) goto loc_008B56A4;
    result = ExAcquireResourceSharedLite(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x30), 1, *(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x450), a4);
    if (*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x498) == 0) goto loc_008B6266;
    if ((*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x4A0)) < 3) goto loc_008B6113;
    result = SepIsAppSuiteSid(*(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x498) + 0x20), 1, *(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x450), a4);
    if ((uint8_t)(result) == 0) goto loc_008B6113;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x498) + 0x20) + 0x1) * 4 + 16)), (uint32_t)(0x20206553ULL), a4);
    if (result == 0) goto loc_008B516F;
    result = RtlCopySid(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x498) + 0x20) + 0x1) * 4 + 16 - 8, result + 8, *(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x498) + 0x20), a4);
    *(uint64_t *)(result) = result + 8;
    goto loc_008B5199;
loc_008B6113:
    result = ExAllocatePool2(256, 8, (uint32_t)(0x20206553ULL), a4);
    if (result != 0) goto loc_008B5F90;
    goto loc_008B516F;
loc_008B6139:
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(256, 8, (uint32_t)(0x20206553ULL), a4);
    if ((uint32_t)(result) == 0) goto loc_008B56A4;
    result = ExAcquireResourceSharedLite(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x30), 1, (uint32_t)(0x20206553ULL), a4);
    if (*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x498) == 0) goto loc_008B6266;
    if ((*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x4A0)) < 2) goto loc_008B6266;
    if (*(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x498) + 0x10) == 0) goto loc_008B6199;
    goto loc_008B619E;
loc_008B6199:
loc_008B619E:
    result = ExAllocatePool2(256, 8, (uint32_t)(0x20206553ULL), a4);
    if (result == 0) goto loc_008B516F;
    if (*(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x498) + 0x10) == 0) goto loc_008B5CF5;
    goto loc_008B5CE6;
loc_008B61D5:
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(256, 8, *(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x498) + 0x10), a4);
    if ((uint32_t)(result) == 0) goto loc_008B56A4;
    result = ExAcquireResourceSharedLite(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x30), 1, *(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x498) + 0x10), a4);
    if (*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x498) == 0) goto loc_008B6266;
    if ((*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0x4A0)) == ((uint32_t)(result + 8))) goto loc_008B6266;
    if (*(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x498)) == 0) goto loc_008B622B;
    goto loc_008B6230;
loc_008B622B:
loc_008B6230:
    result = ExAllocatePool2(256, 8, (uint32_t)(0x20206553ULL), a4);
    if (result == 0) goto loc_008B516F;
    if (*(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x498)) == 0) goto loc_008B5CF5;
    goto loc_008B5CE6;
loc_008B6266:
    result = ExReleaseResourceLite(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x30), 8, *(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x498)), a4);
loc_008B6274:
    result = KeLeaveCriticalRegion(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x30), 8, *(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x498)), a4);
    goto loc_008B63D2;
loc_008B6280:
    v_stack_m98 = (uint32_t)((uint32_t)(0xC000000DULL));
    v_stack_p20 = (uint32_t)((uint32_t)(0xC000000DULL));
    v_stack_p8 = (uint32_t)((uint32_t)(0xC000000DULL));
    v_stack_p10 = (uint32_t)((uint32_t)(0xC000000DULL));
    result = ExAcquireResourceSharedLite(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x30), 1, *(uint64_t *)(*(uint64_t *)((uint32_t)((uint32_t)(result)) + 0x498)), a4);
    v_stack_mF8 = v_stack_p10;
    result = SepGetTokenLoggingInformationBufferSize((uint32_t)((uint32_t)(result)), v_stack_m98, v_stack_p20, v_stack_p8);
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(result)), (uint32_t)(0x20206553ULL), v_stack_p8);
    if (result == 0) goto loc_008B53D7;
    v_stack_mE8 = (uint32_t)((uint32_t)(v_stack_p10));
    v_stack_mF0 = (uint32_t)((uint32_t)(v_stack_p8));
    v_stack_mF8 = (uint32_t)((uint32_t)(v_stack_p20));
    result = SepCopyTokenLoggingInformation((uint32_t)((uint32_t)(result)), result, (uint32_t)(0x20206553ULL), (uint32_t)(v_stack_m98));
    goto loc_008B5199;
loc_008B630F:
    if (((uint32_t)(result)) != 48) goto loc_008B6340;
    v_stack_mF0 = (uint8_t)((uint32_t)(0xC000000DULL));
    a4 = 0;
    Arg2 = 0;
    v_stack_mF8 = 1;
    result = SepSidInTokenSidHash((uint32_t)((uint32_t)(result)) + 808, Arg2, *(uint64_t *)(v_rip + 0x5B18BD), a4);
    *(uint32_t *)(arg3) = (uint32_t)((uint8_t)(result));
    goto loc_008B63D0;
loc_008B6340:
    if (((uint32_t)(result)) != 47) goto loc_008B6361;
loc_008B6345:
    result = SepIsSandboxedToken((uint32_t)((uint32_t)(result)), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), *(uint64_t *)(v_rip + 0x5B18BD), a4);
loc_008B635C:
    *(uint8_t *)(*(uint64_t *)(v_rip + 0x5B18BD)) = (uint8_t)(result);
    goto loc_008B63D0;
loc_008B6361:
    if (((uint32_t)(result)) != 51) goto loc_008B637E;
    result = Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline((uint32_t)((uint32_t)(result)), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), *(uint64_t *)(v_rip + 0x5B18BD), a4);
    if ((uint32_t)(result) == 0) goto loc_008B56A4;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0xC8))) >> (27));
    goto loc_008B6396;
loc_008B637E:
    if (((uint32_t)(result)) != 52) goto loc_008B639D;
    result = Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline((uint32_t)((uint32_t)(result)), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), *(uint64_t *)(v_rip + 0x5B18BD), a4);
    if ((uint32_t)(result) == 0) goto loc_008B56A4;
loc_008B6396:
    result = (uint8_t)((*(uint8_t *)((uint32_t)((uint32_t)(result)) + 0x490)) & (1));
    *(uint8_t *)(arg3) = (uint8_t)(result);
    goto loc_008B63D0;
loc_008B639D:
    if (((uint32_t)(result)) != 53) goto loc_008B63BF;
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline((uint32_t)((uint32_t)(result)), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), *(uint64_t *)(v_rip + 0x5B18BD), a4);
    if ((uint32_t)(result) == 0) goto loc_008B56A4;
    result = SeHasTamperProtection((uint32_t)((uint32_t)(result)), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232), *(uint64_t *)(v_rip + 0x5B18BD), a4);
    *(uint32_t *)(arg3) = (uint32_t)((uint8_t)(result));
    goto loc_008B63D0;
loc_008B63BF:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(result)) + 0xC8))) & (0x3000000ULL));
    result = (uint32_t)((result) >> (24));
loc_008B63CD:
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x5B18BD)) = (uint32_t)(result);
loc_008B63D0:
    result = 0;
loc_008B63D2:
    local_rsp = (local_rsp) + (224);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x7C` | `32` | `R` |
| `Arg1` | `+ 0x80` | `32` | `R` |
| `Arg1` | `+ 0x88` | `32` | `R` |
| `Arg1` | `+ 0x8C` | `32` | `R` |
| `Arg1` | `+ 0x90` | `32` | `R` |
| `Arg1` | `+ 0x98` | `64` | `R` |
| `Arg1` | `+ 0xA0` | `64` | `R` |
| `Arg1` | `+ 0xA8` | `64` | `R` |
| `Arg1` | `+ 0xB8` | `64` | `R` |
| `Arg1` | `+ 0xC0` | `32` | `R` |
| `Arg1` | `+ 0xC4` | `32` | `R` |
| `Arg1` | `+ 0xC8` | `32` | `R` |
| `Arg1` | `+ 0xCA` | `16` | `R` |
| `Arg1` | `+ 0x310` | `64` | `R` |
| `Arg1` | `+ 0x318` | `64` | `R` |
| `Arg1` | `+ 0x320` | `32` | `R` |
| `Arg1` | `+ 0x328` | `64` | `R` |
| `Arg1` | `+ 0x438` | `64` | `R` |
| `Arg1` | `+ 0x448` | `64` | `R` |
| `Arg1` | `+ 0x450` | `64` | `R` |
| `Arg1` | `+ 0x480` | `64` | `R` |
| `Arg1` | `+ 0x490` | `8` | `R` |
| `Arg1` | `+ 0x498` | `64` | `R` |
| `Arg1` | `+ 0x4A0` | `32` | `R` |
| `Arg3` | `+ 0x0` | `8` | `W` |

추가 오프셋 2개는 표에서 생략했습니다.

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008B5090&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
