# SepAccessCheckAndAuditAlarm

- RVA: `0x00A1AF4C`–`0x00A1D860` (길이 `10,516` bytes)
- VA: `0x0000000140A1AF4C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AA4FC`
- 디코드: `2,013`개 명령, `10,516/10,516` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **98**; 고유 호출 대상: **58**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00A1B286` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x00A1B333` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00A1B349` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00A1B4F8` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00A1B58B` → [SeCheckAuditPrivilege](../97/SeCheckAuditPrivilege_function_00974E48.md) (function, `0x00974E48`)
- `0x00A1B5E0` → [SeCaptureSecurityDescriptor](../92/SeCaptureSecurityDescriptor_function_00929F40.md) (function, `0x00929F40`)
- `0x00A1B692` → [SepProbeAndCaptureString_U](../97/SepProbeAndCaptureString_U_function_00975070.md) (function, `0x00975070`)
- `0x00A1B6B4` → [SepProbeAndCaptureString_U](../97/SepProbeAndCaptureString_U_function_00975070.md) (function, `0x00975070`)
- `0x00A1B6D6` → [SepProbeAndCaptureString_U](../97/SepProbeAndCaptureString_U_function_00975070.md) (function, `0x00975070`)
- `0x00A1B7C8` → [SeCaptureSid](../92/SeCaptureSid_function_009276D4.md) (function, `0x009276D4`)
- `0x00A1B802` → [SeCaptureObjectTypeList](../../text/43/SeCaptureObjectTypeList_function_00434320.md) (function, `0x00434320`)
- `0x00A1B83A` → [SepTrustLevelCheck](../../text/3E/SepTrustLevelCheck_function_003ED7E0.md) (function, `0x003ED7E0`)
- `0x00A1B858` → [SepFilterToDiscretionary](../../text/41/SepFilterToDiscretionary_function_0041ECC0.md) (function, `0x0041ECC0`)
- `0x00A1B8A4` → [SepFilterCheck](../../text/30/SepFilterCheck_function_00301B60.md) (function, `0x00301B60`)
- `0x00A1B8BE` → [SepFilterToDiscretionary](../../text/41/SepFilterToDiscretionary_function_0041ECC0.md) (function, `0x0041ECC0`)
- `0x00A1B917` → [SepMandatoryIntegrityCheck](../../text/25/SepMandatoryIntegrityCheck_function_0025F4E0.md) (function, `0x0025F4E0`)
- `0x00A1B931` → [SepMandatoryToDiscretionary](../../text/41/SepMandatoryToDiscretionary_function_0041BF40.md) (function, `0x0041BF40`)
- `0x00A1B976` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x00A1B9A7` → [SepMandatoryAccessCheck](../../text/60/SepMandatoryAccessCheck_function_00608480.md) (function, `0x00608480`)
- `0x00A1BA23` → [SePrivilegePolicyCheck](../../text/3D/SePrivilegePolicyCheck_function_003D1700.md) (function, `0x003D1700`)
- `0x00A1BA67` → [SeLockSubjectContext](../8C/SeLockSubjectContext_function_008C64C0.md) (function, `0x008C64C0`)
- `0x00A1BAB4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A1BAD1` → [SeUnlockSubjectContext](../8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x00A1BB2E` → [SepTokenIsOwner](../../text/3E/SepTokenIsOwner_function_003E5D60.md) (function, `0x003E5D60`)
- `0x00A1BBF0` → [SepGetScopedPolicySid](../../text/3A/SepGetScopedPolicySid_function_003A59AC.md) (function, `0x003A59AC`)
- `0x00A1BC09` → [SepRmReferenceFindCap](../../text/3A/SepRmReferenceFindCap_function_003A58EC.md) (function, `0x003A58EC`)
- `0x00A1BC71` → [RtlOwnerAcesPresent](../../text/3F/RtlOwnerAcesPresent_function_003FDA10.md) (function, `0x003FDA10`)
- `0x00A1BCC1` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x00A1BD68` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A1BD8A` → [SeUnlockSubjectContext](../8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x00A1BE06` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A1BF15` → [SepAccessCheck](../../text/3D/SepAccessCheck_function_003D0E54.md) (function, `0x003D0E54`)
- `0x00A1BF58` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A1BF75` → [SeUnlockSubjectContext](../8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x00A1BF82` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00A1BFDC` → [SepCopyObjectTypeList](../../text/60/SepCopyObjectTypeList_function_00606CC0.md) (function, `0x00606CC0`)
- `0x00A1C063` → [AuthzBasepInitializeResourceClaimsFromSacl](../../text/30/AuthzBasepInitializeResourceClaimsFromSacl_function_00302E84.md) (function, `0x00302E84`)
- `0x00A1C11A` → [AuthzBasepEvaluateAceCondition](../../text/2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (function, `0x002FEBD0`)
- `0x00A1C146` → [SeTokenIsRestricted](../../text/43/SeTokenIsRestricted_function_00438CE0.md) (function, `0x00438CE0`)
- `0x00A1C1EE` → [AuthzBasepEvaluateAceCondition](../../text/2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (function, `0x002FEBD0`)
- `0x00A1C270` → [SepBuildCapeSecurityDescriptor](../../text/4D/SepBuildCapeSecurityDescriptor_function_004D9E38.md) (function, `0x004D9E38`)
- `0x00A1C357` → [SepAccessCheck](../../text/3D/SepAccessCheck_function_003D0E54.md) (function, `0x003D0E54`)
- `0x00A1C3A0` → [SepMergeObjectTypeListAccesses](../../text/60/SepMergeObjectTypeListAccesses_function_00607508.md) (function, `0x00607508`)
- `0x00A1C46A` → [SeIsPermissiveLearningModeEnabled](../../text/46/SeIsPermissiveLearningModeEnabled_function_0046A4E0.md) (function, `0x0046A4E0`)
- `0x00A1C49F` → [SepConstrainByMandatory](../../text/43/SepConstrainByMandatory_function_0043FC70.md) (function, `0x0043FC70`)
- `0x00A1C4A4` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x00A1C4F8` → [SeIsPermissiveLearningModeEnabled](../../text/46/SeIsPermissiveLearningModeEnabled_function_0046A4E0.md) (function, `0x0046A4E0`)
- `0x00A1C632` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A1C6DA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A1C7E9` → [SepAccessCheck](../../text/3D/SepAccessCheck_function_003D0E54.md) (function, `0x003D0E54`)
- `0x00A1C82C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00A1C890` → [SepCopyObjectTypeList](../../text/60/SepCopyObjectTypeList_function_00606CC0.md) (function, `0x00606CC0`)
- `0x00A1C916` → [AuthzBasepInitializeResourceClaimsFromSacl](../../text/30/AuthzBasepInitializeResourceClaimsFromSacl_function_00302E84.md) (function, `0x00302E84`)
- `0x00A1C9CD` → [AuthzBasepEvaluateAceCondition](../../text/2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (function, `0x002FEBD0`)
- `0x00A1C9F9` → [SeTokenIsRestricted](../../text/43/SeTokenIsRestricted_function_00438CE0.md) (function, `0x00438CE0`)
- `0x00A1CAA1` → [AuthzBasepEvaluateAceCondition](../../text/2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (function, `0x002FEBD0`)
- `0x00A1CB23` → [SepBuildCapeSecurityDescriptor](../../text/4D/SepBuildCapeSecurityDescriptor_function_004D9E38.md) (function, `0x004D9E38`)
- `0x00A1CC0A` → [SepAccessCheck](../../text/3D/SepAccessCheck_function_003D0E54.md) (function, `0x003D0E54`)
- `0x00A1CC53` → [SepMergeObjectTypeListAccesses](../../text/60/SepMergeObjectTypeListAccesses_function_00607508.md) (function, `0x00607508`)
- `0x00A1CD21` → [SeIsPermissiveLearningModeEnabled](../../text/46/SeIsPermissiveLearningModeEnabled_function_0046A4E0.md) (function, `0x0046A4E0`)
- `0x00A1CD5A` → [SepConstrainByMandatory](../../text/43/SepConstrainByMandatory_function_0043FC70.md) (function, `0x0043FC70`)
- `0x00A1CD92` → [SeIsPermissiveLearningModeEnabled](../../text/46/SeIsPermissiveLearningModeEnabled_function_0046A4E0.md) (function, `0x0046A4E0`)
- `0x00A1CE43` → [SepConstrainByConstraintMask](../../text/43/SepConstrainByConstraintMask_function_0043FDE0.md) (function, `0x0043FDE0`)
- `0x00A1CE6E` → [SepConstrainByConstraintMask](../../text/43/SepConstrainByConstraintMask_function_0043FDE0.md) (function, `0x0043FDE0`)
- `0x00A1CEEC` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00A1CF15` → [SepLocateTokenTrustLevel](../../text/3E/SepLocateTokenTrustLevel_function_003EDA40.md) (function, `0x003EDA40`)
- `0x00A1CF47` → [SeLogAccessFailure](../../text/44/SeLogAccessFailure_function_00448550.md) (function, `0x00448550`)
- `0x00A1CF50` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00A1CF55` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00A1CF8E` → [SepLpacCausedAccessFailure](../../text/46/SepLpacCausedAccessFailure_function_00462484.md) (function, `0x00462484`)
- `0x00A1CF97` → [SepLogLpacAccessFailure](../../text/41/SepLogLpacAccessFailure_function_0041E8A0.md) (function, `0x0041E8A0`)
- `0x00A1CFF2` → [SepAdtAuditObjectAccessWithContext](../86/SepAdtAuditObjectAccessWithContext_function_0086EEF0.md) (function, `0x0086EEF0`)
- `0x00A1D03E` → [SepAdtAuditObjectAccessWithContext](../86/SepAdtAuditObjectAccessWithContext_function_0086EEF0.md) (function, `0x0086EEF0`)
- `0x00A1D06C` → [SepAdtAuditThisEventWithContext](../87/SepAdtAuditThisEventWithContext_function_00870AC0.md) (function, `0x00870AC0`)
- `0x00A1D099` → [SepAdtAuditThisEventWithContext](../87/SepAdtAuditThisEventWithContext_function_00870AC0.md) (function, `0x00870AC0`)
- `0x00A1D1A5` → [SepExamineSaclEx](../A2/SepExamineSaclEx_function_00A2F39C.md) (function, `0x00A2F39C`)
- `0x00A1D255` → [SepExamineGlobalSaclEx](../../text/46/SepExamineGlobalSaclEx_function_0046B550.md) (function, `0x0046B550`)
- `0x00A1D324` → [SepAdtPrivilegeObjectAuditAlarm](../86/SepAdtPrivilegeObjectAuditAlarm_function_0086E3F0.md) (function, `0x0086E3F0`)
- `0x00A1D43D` → [SepAdtOpenObjectAuditAlarm](../91/SepAdtOpenObjectAuditAlarm_function_0091F23C.md) (function, `0x0091F23C`)
- `0x00A1D537` → [SepAdtOpenObjectAuditAlarm](../91/SepAdtOpenObjectAuditAlarm_function_0091F23C.md) (function, `0x0091F23C`)
- `0x00A1D54B` → [SeUnlockSubjectContext](../8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x00A1D70B` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00A1D72F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A1D73C` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00A1D74F` → [SeReleaseSecurityDescriptor](../97/SeReleaseSecurityDescriptor_function_00975190.md) (function, `0x00975190`)
- `0x00A1D763` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A1D777` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A1D78B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A1D7A3` → [SeReleaseSid](../A2/SeReleaseSid_function_00A2EF50.md) (function, `0x00A2EF50`)
- `0x00A1D7B5` → [SeFreeCapturedObjectTypeList](../../text/60/SeFreeCapturedObjectTypeList_function_00606CA4.md) (function, `0x00606CA4`)
- `0x00A1D7CE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A1D7DD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A1D7F4` → [SepRmDereferenceCap](../../text/4B/SepRmDereferenceCap_function_004B1E9C.md) (function, `0x004B1E9C`)
- `0x00A1D808` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A1D815` → [SepFreeResourceInfo](../../text/30/SepFreeResourceInfo_function_003019F0.md) (function, `0x003019F0`)
- `0x00A1D82E` → [SepAuditFailed](../86/SepAuditFailed_function_0086EE20.md) (function, `0x0086EE20`)
- `0x00A1D840` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A1D859` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)

### Direct callers
- [NtAccessCheckByTypeResultListAndAuditAlarm](../7A/NtAccessCheckByTypeResultListAndAuditAlarm_function_007A0250.md) at `0x007A02E9`
- [NtAccessCheckByTypeResultListAndAuditAlarmByHandle](../7A/NtAccessCheckByTypeResultListAndAuditAlarmByHandle_function_007A0300.md) at `0x007A03A3`
- [NtAccessCheckByTypeAndAuditAlarm](NtAccessCheckByTypeAndAuditAlarm_function_00A1AE10.md) at `0x00A1AEA9`
- [NtAccessCheckAndAuditAlarm](NtAccessCheckAndAuditAlarm_function_00A1AEC0.md) at `0x00A1AF36`

### Static image references
- `0x00A1AF5F` → RVA `0x00E0A740` (`.data`; read)
- `0x00A1B4C3` → RVA `0x00FD8020` (`PAGEDATA`; read)
- `0x00A1BB3A` → RVA `0x00F04AC5` (`.data`; read)
- `0x00A1BC18` → RVA `0x00FD80F0` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **69**
  - `0x00A1B802` → [SeCaptureObjectTypeList](../../text/43/SeCaptureObjectTypeList_function_00434320.md) (`PAGE` → `.text`)
  - `0x00A1B83A` → [SepTrustLevelCheck](../../text/3E/SepTrustLevelCheck_function_003ED7E0.md) (`PAGE` → `.text`)
  - `0x00A1B858` → [SepFilterToDiscretionary](../../text/41/SepFilterToDiscretionary_function_0041ECC0.md) (`PAGE` → `.text`)
  - `0x00A1B8A4` → [SepFilterCheck](../../text/30/SepFilterCheck_function_00301B60.md) (`PAGE` → `.text`)
  - `0x00A1B8BE` → [SepFilterToDiscretionary](../../text/41/SepFilterToDiscretionary_function_0041ECC0.md) (`PAGE` → `.text`)
  - `0x00A1B917` → [SepMandatoryIntegrityCheck](../../text/25/SepMandatoryIntegrityCheck_function_0025F4E0.md) (`PAGE` → `.text`)
  - `0x00A1B931` → [SepMandatoryToDiscretionary](../../text/41/SepMandatoryToDiscretionary_function_0041BF40.md) (`PAGE` → `.text`)
  - `0x00A1B976` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (`PAGE` → `.text`)
  - `0x00A1B9A7` → [SepMandatoryAccessCheck](../../text/60/SepMandatoryAccessCheck_function_00608480.md) (`PAGE` → `.text`)
  - `0x00A1BA23` → [SePrivilegePolicyCheck](../../text/3D/SePrivilegePolicyCheck_function_003D1700.md) (`PAGE` → `.text`)
  - `0x00A1BAB4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A1BB2E` → [SepTokenIsOwner](../../text/3E/SepTokenIsOwner_function_003E5D60.md) (`PAGE` → `.text`)
  - `0x00A1BBF0` → [SepGetScopedPolicySid](../../text/3A/SepGetScopedPolicySid_function_003A59AC.md) (`PAGE` → `.text`)
  - `0x00A1BC09` → [SepRmReferenceFindCap](../../text/3A/SepRmReferenceFindCap_function_003A58EC.md) (`PAGE` → `.text`)
  - `0x00A1BC71` → [RtlOwnerAcesPresent](../../text/3F/RtlOwnerAcesPresent_function_003FDA10.md) (`PAGE` → `.text`)
  - `0x00A1BCC1` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (`PAGE` → `.text`)
  - `0x00A1BD68` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A1BE06` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A1BF15` → [SepAccessCheck](../../text/3D/SepAccessCheck_function_003D0E54.md) (`PAGE` → `.text`)
  - `0x00A1BF58` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A1BFDC` → [SepCopyObjectTypeList](../../text/60/SepCopyObjectTypeList_function_00606CC0.md) (`PAGE` → `.text`)
  - `0x00A1C063` → [AuthzBasepInitializeResourceClaimsFromSacl](../../text/30/AuthzBasepInitializeResourceClaimsFromSacl_function_00302E84.md) (`PAGE` → `.text`)
  - `0x00A1C11A` → [AuthzBasepEvaluateAceCondition](../../text/2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (`PAGE` → `.text`)
  - `0x00A1C146` → [SeTokenIsRestricted](../../text/43/SeTokenIsRestricted_function_00438CE0.md) (`PAGE` → `.text`)
  - `0x00A1C1EE` → [AuthzBasepEvaluateAceCondition](../../text/2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (`PAGE` → `.text`)
  - `0x00A1C270` → [SepBuildCapeSecurityDescriptor](../../text/4D/SepBuildCapeSecurityDescriptor_function_004D9E38.md) (`PAGE` → `.text`)
  - `0x00A1C357` → [SepAccessCheck](../../text/3D/SepAccessCheck_function_003D0E54.md) (`PAGE` → `.text`)
  - `0x00A1C3A0` → [SepMergeObjectTypeListAccesses](../../text/60/SepMergeObjectTypeListAccesses_function_00607508.md) (`PAGE` → `.text`)
  - `0x00A1C46A` → [SeIsPermissiveLearningModeEnabled](../../text/46/SeIsPermissiveLearningModeEnabled_function_0046A4E0.md) (`PAGE` → `.text`)
  - `0x00A1C49F` → [SepConstrainByMandatory](../../text/43/SepConstrainByMandatory_function_0043FC70.md) (`PAGE` → `.text`)
  - `0x00A1C4A4` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../../text/5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (`PAGE` → `.text`)
  - `0x00A1C4F8` → [SeIsPermissiveLearningModeEnabled](../../text/46/SeIsPermissiveLearningModeEnabled_function_0046A4E0.md) (`PAGE` → `.text`)
  - `0x00A1C632` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A1C6DA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A1C7E9` → [SepAccessCheck](../../text/3D/SepAccessCheck_function_003D0E54.md) (`PAGE` → `.text`)
  - `0x00A1C82C` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00A1C890` → [SepCopyObjectTypeList](../../text/60/SepCopyObjectTypeList_function_00606CC0.md) (`PAGE` → `.text`)
  - `0x00A1C916` → [AuthzBasepInitializeResourceClaimsFromSacl](../../text/30/AuthzBasepInitializeResourceClaimsFromSacl_function_00302E84.md) (`PAGE` → `.text`)
  - `0x00A1C9CD` → [AuthzBasepEvaluateAceCondition](../../text/2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (`PAGE` → `.text`)
  - `0x00A1C9F9` → [SeTokenIsRestricted](../../text/43/SeTokenIsRestricted_function_00438CE0.md) (`PAGE` → `.text`)
  - `0x00A1CAA1` → [AuthzBasepEvaluateAceCondition](../../text/2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (`PAGE` → `.text`)
  - `0x00A1CB23` → [SepBuildCapeSecurityDescriptor](../../text/4D/SepBuildCapeSecurityDescriptor_function_004D9E38.md) (`PAGE` → `.text`)
  - `0x00A1CC0A` → [SepAccessCheck](../../text/3D/SepAccessCheck_function_003D0E54.md) (`PAGE` → `.text`)
  - `0x00A1CC53` → [SepMergeObjectTypeListAccesses](../../text/60/SepMergeObjectTypeListAccesses_function_00607508.md) (`PAGE` → `.text`)
  - `0x00A1CD21` → [SeIsPermissiveLearningModeEnabled](../../text/46/SeIsPermissiveLearningModeEnabled_function_0046A4E0.md) (`PAGE` → `.text`)
  - `0x00A1CD5A` → [SepConstrainByMandatory](../../text/43/SepConstrainByMandatory_function_0043FC70.md) (`PAGE` → `.text`)
  - `0x00A1CD92` → [SeIsPermissiveLearningModeEnabled](../../text/46/SeIsPermissiveLearningModeEnabled_function_0046A4E0.md) (`PAGE` → `.text`)
  - `0x00A1CE43` → [SepConstrainByConstraintMask](../../text/43/SepConstrainByConstraintMask_function_0043FDE0.md) (`PAGE` → `.text`)
  - `0x00A1CE6E` → [SepConstrainByConstraintMask](../../text/43/SepConstrainByConstraintMask_function_0043FDE0.md) (`PAGE` → `.text`)
  - `0x00A1CEEC` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00A1CF15` → [SepLocateTokenTrustLevel](../../text/3E/SepLocateTokenTrustLevel_function_003EDA40.md) (`PAGE` → `.text`)
  - `0x00A1CF47` → [SeLogAccessFailure](../../text/44/SeLogAccessFailure_function_00448550.md) (`PAGE` → `.text`)
  - `0x00A1CF50` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00A1CF55` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00A1CF8E` → [SepLpacCausedAccessFailure](../../text/46/SepLpacCausedAccessFailure_function_00462484.md) (`PAGE` → `.text`)
  - `0x00A1CF97` → [SepLogLpacAccessFailure](../../text/41/SepLogLpacAccessFailure_function_0041E8A0.md) (`PAGE` → `.text`)
  - `0x00A1D255` → [SepExamineGlobalSaclEx](../../text/46/SepExamineGlobalSaclEx_function_0046B550.md) (`PAGE` → `.text`)
  - `0x00A1D70B` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00A1D72F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A1D763` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A1D777` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A1D78B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A1D7B5` → [SeFreeCapturedObjectTypeList](../../text/60/SeFreeCapturedObjectTypeList_function_00606CA4.md) (`PAGE` → `.text`)
  - `0x00A1D7CE` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A1D7DD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A1D7F4` → [SepRmDereferenceCap](../../text/4B/SepRmDereferenceCap_function_004B1E9C.md) (`PAGE` → `.text`)
  - `0x00A1D808` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A1D815` → [SepFreeResourceInfo](../../text/30/SepFreeResourceInfo_function_003019F0.md) (`PAGE` → `.text`)
  - `0x00A1D840` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A1AF4C  40 53                           push rbx
00A1AF4E  56                              push rsi
00A1AF4F  57                              push rdi
00A1AF50  41 54                           push r12
00A1AF52  41 55                           push r13
00A1AF54  41 56                           push r14
00A1AF56  41 57                           push r15
00A1AF58  48 81 EC 00 03 00 00            sub rsp, 0x300
00A1AF5F  48 8B 05 DA F7 3E 00            mov rax, qword ptr [rip + 0x3ef7da]
00A1AF66  48 33 C4                        xor rax, rsp
00A1AF69  48 89 84 24 F0 02 00 00         mov qword ptr [rsp + 0x2f0], rax
00A1AF71  49 8B C1                        mov rax, r9
00A1AF74  48 89 84 24 18 02 00 00         mov qword ptr [rsp + 0x218], rax
00A1AF7C  4D 8B E8                        mov r13, r8
00A1AF7F  4C 8B C1                        mov r8, rcx
00A1AF82  48 89 8C 24 78 02 00 00         mov qword ptr [rsp + 0x278], rcx
00A1AF8A  44 8B 94 24 98 03 00 00         mov r10d, dword ptr [rsp + 0x398]
00A1AF92  44 89 94 24 28 01 00 00         mov dword ptr [rsp + 0x128], r10d
00A1AF9A  48 8B 8C 24 B8 03 00 00         mov rcx, qword ptr [rsp + 0x3b8]
00A1AFA2  48 89 8C 24 60 02 00 00         mov qword ptr [rsp + 0x260], rcx
00A1AFAA  48 8B BC 24 A0 03 00 00         mov rdi, qword ptr [rsp + 0x3a0]
00A1AFB2  4C 8B 8C 24 A8 03 00 00         mov r9, qword ptr [rsp + 0x3a8]
00A1AFBA  4C 89 8C 24 A8 01 00 00         mov qword ptr [rsp + 0x1a8], r9
00A1AFC2  4C 8B 9C 24 B0 03 00 00         mov r11, qword ptr [rsp + 0x3b0]
00A1AFCA  4C 89 9C 24 A0 01 00 00         mov qword ptr [rsp + 0x1a0], r11
00A1AFD2  4C 89 84 24 90 02 00 00         mov qword ptr [rsp + 0x290], r8
00A1AFDA  48 89 94 24 08 02 00 00         mov qword ptr [rsp + 0x208], rdx
00A1AFE2  4C 89 AC 24 80 02 00 00         mov qword ptr [rsp + 0x280], r13
00A1AFEA  48 89 84 24 88 02 00 00         mov qword ptr [rsp + 0x288], rax
00A1AFF2  48 8B 84 24 60 03 00 00         mov rax, qword ptr [rsp + 0x360]
00A1AFFA  48 89 84 24 20 02 00 00         mov qword ptr [rsp + 0x220], rax
00A1B002  48 8B 9C 24 68 03 00 00         mov rbx, qword ptr [rsp + 0x368]
00A1B00A  48 89 9C 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rbx
00A1B012  48 89 9C 24 F0 01 00 00         mov qword ptr [rsp + 0x1f0], rbx
00A1B01A  48 8B 84 24 70 03 00 00         mov rax, qword ptr [rsp + 0x370]
00A1B022  48 89 84 24 00 02 00 00         mov qword ptr [rsp + 0x200], rax
00A1B02A  48 8B 84 24 90 03 00 00         mov rax, qword ptr [rsp + 0x390]
00A1B032  48 89 84 24 F8 01 00 00         mov qword ptr [rsp + 0x1f8], rax
00A1B03A  45 8B FA                        mov r15d, r10d
00A1B03D  44 89 BC 24 C0 00 00 00         mov dword ptr [rsp + 0xc0], r15d
00A1B045  44 89 94 24 68 01 00 00         mov dword ptr [rsp + 0x168], r10d
00A1B04D  4C 89 8C 24 38 02 00 00         mov qword ptr [rsp + 0x238], r9
00A1B055  4C 89 9C 24 40 02 00 00         mov qword ptr [rsp + 0x240], r11
00A1B05D  48 89 8C 24 48 02 00 00         mov qword ptr [rsp + 0x248], rcx
00A1B065  0F 57 C0                        xorps xmm0, xmm0
00A1B068  0F 11 84 24 48 01 00 00         movups xmmword ptr [rsp + 0x148], xmm0
00A1B070  0F 11 84 24 58 01 00 00         movups xmmword ptr [rsp + 0x158], xmm0
00A1B078  33 F6                           xor esi, esi
00A1B07A  89 B4 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], esi
00A1B081  89 B4 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], esi
00A1B088  44 8B E6                        mov r12d, esi
00A1B08B  40 88 B4 24 AE 00 00 00         mov byte ptr [rsp + 0xae], sil
00A1B093  C7 84 24 B0 00 00 00 01 00 00 C0  mov dword ptr [rsp + 0xb0], 0xc0000001
00A1B09E  89 B4 24 C8 01 00 00            mov dword ptr [rsp + 0x1c8], esi
00A1B0A5  48 89 B4 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rsi
00A1B0AD  89 B4 24 CC 01 00 00            mov dword ptr [rsp + 0x1cc], esi
00A1B0B4  8B C6                           mov eax, esi
00A1B0B6  48 89 84 24 38 01 00 00         mov qword ptr [rsp + 0x138], rax
00A1B0BE  89 84 24 08 01 00 00            mov dword ptr [rsp + 0x108], eax
00A1B0C5  89 84 24 0C 01 00 00            mov dword ptr [rsp + 0x10c], eax
00A1B0CC  88 84 24 F8 00 00 00            mov byte ptr [rsp + 0xf8], al
00A1B0D3  48 89 B4 24 E0 01 00 00         mov qword ptr [rsp + 0x1e0], rsi
00A1B0DB  48 89 B4 24 B0 01 00 00         mov qword ptr [rsp + 0x1b0], rsi
00A1B0E3  48 89 B4 24 E8 01 00 00         mov qword ptr [rsp + 0x1e8], rsi
00A1B0EB  48 89 B4 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rsi
00A1B0F3  48 89 B4 24 90 01 00 00         mov qword ptr [rsp + 0x190], rsi
00A1B0FB  48 89 B4 24 40 01 00 00         mov qword ptr [rsp + 0x140], rsi
00A1B103  89 B4 24 E4 00 00 00            mov dword ptr [rsp + 0xe4], esi
00A1B10A  0F 11 84 24 E0 02 00 00         movups xmmword ptr [rsp + 0x2e0], xmm0
00A1B112  48 89 B4 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], rsi
00A1B11A  40 88 B4 24 A1 00 00 00         mov byte ptr [rsp + 0xa1], sil
00A1B122  40 88 B4 24 A2 00 00 00         mov byte ptr [rsp + 0xa2], sil
00A1B12A  40 88 B4 24 CA 00 00 00         mov byte ptr [rsp + 0xca], sil
00A1B132  40 88 B4 24 CB 00 00 00         mov byte ptr [rsp + 0xcb], sil
00A1B13A  40 88 B4 24 05 01 00 00         mov byte ptr [rsp + 0x105], sil
00A1B142  40 8A C6                        mov al, sil
00A1B145  88 84 24 AD 00 00 00            mov byte ptr [rsp + 0xad], al
00A1B14C  88 84 24 AC 00 00 00            mov byte ptr [rsp + 0xac], al
00A1B153  44 8D 76 01                     lea r14d, [rsi + 1]
00A1B157  44 88 B4 24 C8 00 00 00         mov byte ptr [rsp + 0xc8], r14b
00A1B15F  40 88 B4 24 C9 00 00 00         mov byte ptr [rsp + 0xc9], sil
00A1B167  48 89 B4 24 10 02 00 00         mov qword ptr [rsp + 0x210], rsi
00A1B16F  48 89 B4 24 50 02 00 00         mov qword ptr [rsp + 0x250], rsi
00A1B177  40 88 B4 24 FC 00 00 00         mov byte ptr [rsp + 0xfc], sil
00A1B17F  0F 11 84 24 68 02 00 00         movups xmmword ptr [rsp + 0x268], xmm0
00A1B187  48 89 B4 24 D8 01 00 00         mov qword ptr [rsp + 0x1d8], rsi
00A1B18F  8B C6                           mov eax, esi
00A1B191  48 89 84 24 88 01 00 00         mov qword ptr [rsp + 0x188], rax
00A1B199  0F 11 84 24 98 02 00 00         movups xmmword ptr [rsp + 0x298], xmm0
00A1B1A1  0F 11 84 24 A8 02 00 00         movups xmmword ptr [rsp + 0x2a8], xmm0
00A1B1A9  48 89 84 24 B8 02 00 00         mov qword ptr [rsp + 0x2b8], rax
00A1B1B1  48 89 B4 24 78 01 00 00         mov qword ptr [rsp + 0x178], rsi
00A1B1B9  40 88 B4 24 A5 00 00 00         mov byte ptr [rsp + 0xa5], sil
00A1B1C1  88 84 24 A4 00 00 00            mov byte ptr [rsp + 0xa4], al
00A1B1C8  88 84 24 A3 00 00 00            mov byte ptr [rsp + 0xa3], al
00A1B1CF  40 88 B4 24 07 01 00 00         mov byte ptr [rsp + 0x107], sil
00A1B1D7  B8 E7 03 00 00                  mov eax, 0x3e7
00A1B1DC  66 89 84 24 E8 00 00 00         mov word ptr [rsp + 0xe8], ax
00A1B1E4  33 C0                           xor eax, eax
00A1B1E6  0F 11 84 24 C0 02 00 00         movups xmmword ptr [rsp + 0x2c0], xmm0
00A1B1EE  48 89 84 24 D0 02 00 00         mov qword ptr [rsp + 0x2d0], rax
00A1B1F6  89 84 24 D8 02 00 00            mov dword ptr [rsp + 0x2d8], eax
00A1B1FD  89 84 24 00 01 00 00            mov dword ptr [rsp + 0x100], eax
00A1B204  88 84 24 FD 00 00 00            mov byte ptr [rsp + 0xfd], al
00A1B20B  8B C6                           mov eax, esi
00A1B20D  89 84 24 EC 00 00 00            mov dword ptr [rsp + 0xec], eax
00A1B214  48 89 B4 24 20 01 00 00         mov qword ptr [rsp + 0x120], rsi
00A1B21C  89 B4 24 14 01 00 00            mov dword ptr [rsp + 0x114], esi
00A1B223  89 84 24 D0 01 00 00            mov dword ptr [rsp + 0x1d0], eax
00A1B22A  88 84 24 04 01 00 00            mov byte ptr [rsp + 0x104], al
00A1B231  40 88 B4 24 B4 00 00 00         mov byte ptr [rsp + 0xb4], sil
00A1B239  40 88 B4 24 B5 00 00 00         mov byte ptr [rsp + 0xb5], sil
00A1B241  48 89 B4 24 B8 01 00 00         mov qword ptr [rsp + 0x1b8], rsi
00A1B249  89 B4 24 18 01 00 00            mov dword ptr [rsp + 0x118], esi
00A1B250  83 C8 FF                        or eax, 0xffffffff
00A1B253  89 84 24 98 01 00 00            mov dword ptr [rsp + 0x198], eax
00A1B25A  89 84 24 D8 01 00 00            mov dword ptr [rsp + 0x1d8], eax
00A1B261  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A1B26A  8A 80 32 02 00 00               mov al, byte ptr [rax + 0x232]
00A1B270  88 84 24 A0 00 00 00            mov byte ptr [rsp + 0xa0], al
00A1B277  88 84 24 E0 00 00 00            mov byte ptr [rsp + 0xe0], al
00A1B27E  48 8D 8C 24 48 01 00 00         lea rcx, [rsp + 0x148]
00A1B286  E8 95 05 E5 FF                  call 0x14086b820
00A1B28B  39 B4 24 80 03 00 00            cmp dword ptr [rsp + 0x380], esi
00A1B292  75 0D                           jne 0x140a1b2a1
00A1B294  C7 84 24 6C 01 00 00 02 00 00 00  mov dword ptr [rsp + 0x16c], 2
00A1B29F  EB 19                           jmp 0x140a1b2ba
00A1B2A1  44 39 B4 24 80 03 00 00         cmp dword ptr [rsp + 0x380], r14d
00A1B2A9  0F 85 3A 24 00 00               jne 0x140a1d6e9
00A1B2AF  C7 84 24 6C 01 00 00 07 00 00 00  mov dword ptr [rsp + 0x16c], 7
00A1B2BA  4D 85 ED                        test r13, r13
00A1B2BD  75 28                           jne 0x140a1b2e7
00A1B2BF  48 39 B4 24 48 01 00 00         cmp qword ptr [rsp + 0x148], rsi
00A1B2C7  75 0A                           jne 0x140a1b2d3
00A1B2C9  BF 5C 00 00 C0                  mov edi, 0xc000005c
00A1B2CE  E9 1B 24 00 00                  jmp 0x140a1d6ee
00A1B2D3  44 39 B4 24 50 01 00 00         cmp dword ptr [rsp + 0x150], r14d
00A1B2DB  7D 0A                           jge 0x140a1b2e7
00A1B2DD  BF A5 00 00 C0                  mov edi, 0xc00000a5
00A1B2E2  E9 07 24 00 00                  jmp 0x140a1d6ee
00A1B2E7  40 38 B4 24 C0 03 00 00         cmp byte ptr [rsp + 0x3c0], sil
00A1B2EF  74 71                           je 0x140a1b362
00A1B2F1  45 85 FF                        test r15d, r15d
00A1B2F4  75 1B                           jne 0x140a1b311
00A1B2F6  BF 0D 00 00 C0                  mov edi, 0xc000000d
00A1B2FB  89 BC 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], edi
00A1B302  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
00A1B30C  E9 B5 00 00 00                  jmp 0x140a1b3c6
00A1B311  41 81 FF 00 10 00 00            cmp r15d, 0x1000
00A1B318  77 DC                           ja 0x140a1b2f6
00A1B31A  4A 8D 1C BD 00 00 00 00         lea rbx, [r15*4]
00A1B322  41 B8 04 00 00 00               mov r8d, 4
00A1B328  48 8B D3                        mov rdx, rbx
00A1B32B  48 8B 8C 24 A0 01 00 00         mov rcx, qword ptr [rsp + 0x1a0]
00A1B333  E8 88 DE EC FF                  call 0x1408e91c0
00A1B338  41 B8 04 00 00 00               mov r8d, 4
00A1B33E  48 8B D3                        mov rdx, rbx
00A1B341  48 8B 8C 24 A8 01 00 00         mov rcx, qword ptr [rsp + 0x1a8]
00A1B349  E8 72 DE EC FF                  call 0x1408e91c0
00A1B34E  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
00A1B358  48 8B 9C 24 F0 00 00 00         mov rbx, qword ptr [rsp + 0xf0]
00A1B360  EB 3A                           jmp 0x140a1b39c
00A1B362  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
00A1B36C  49 8B CF                        mov rcx, r15
00A1B36F  4C 39 BC 24 A0 01 00 00         cmp qword ptr [rsp + 0x1a0], r15
00A1B377  48 0F 42 8C 24 A0 01 00 00      cmovb rcx, qword ptr [rsp + 0x1a0]
00A1B380  8B 01                           mov eax, dword ptr [rcx]
00A1B382  89 01                           mov dword ptr [rcx], eax
00A1B384  49 8B CF                        mov rcx, r15
00A1B387  4C 39 BC 24 A8 01 00 00         cmp qword ptr [rsp + 0x1a8], r15
00A1B38F  48 0F 42 8C 24 A8 01 00 00      cmovb rcx, qword ptr [rsp + 0x1a8]
00A1B398  8B 01                           mov eax, dword ptr [rcx]
00A1B39A  89 01                           mov dword ptr [rcx], eax
00A1B39C  40 F6 C7 03                     test dil, 3
00A1B3A0  0F 85 B3 24 00 00               jne 0x140a1d859
00A1B3A6  49 8B C7                        mov rax, r15
00A1B3A9  49 3B FF                        cmp rdi, r15
00A1B3AC  48 0F 42 C7                     cmovb rax, rdi
00A1B3B0  90                              nop
00A1B3B1  8A 00                           mov al, byte ptr [rax]
00A1B3B3  0F 10 07                        movups xmm0, xmmword ptr [rdi]
00A1B3B6  F3 0F 7F 84 24 E0 02 00 00      movdqu xmmword ptr [rsp + 0x2e0], xmm0
00A1B3BF  8B BC 24 A8 00 00 00            mov edi, dword ptr [rsp + 0xa8]
00A1B3C6  E9 E7 00 00 00                  jmp 0x140a1b4b2
00A1B3CB  8B F8                           mov edi, eax
00A1B3CD  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00A1B3D4  33 F6                           xor esi, esi
00A1B3D6  44 8D 76 01                     lea r14d, [rsi + 1]
00A1B3DA  49 BF 00 00 FF FF FF 7F 00 00   movabs r15, 0x7fffffff0000
00A1B3E4  44 8B E6                        mov r12d, esi
00A1B3E7  8B C6                           mov eax, esi
00A1B3E9  48 89 84 24 38 01 00 00         mov qword ptr [rsp + 0x138], rax
00A1B3F1  89 84 24 08 01 00 00            mov dword ptr [rsp + 0x108], eax
00A1B3F8  8A 8C 24 F8 00 00 00            mov cl, byte ptr [rsp + 0xf8]
00A1B3FF  89 8C 24 0C 01 00 00            mov dword ptr [rsp + 0x10c], ecx
00A1B406  8A 84 24 E0 00 00 00            mov al, byte ptr [rsp + 0xe0]
00A1B40D  88 84 24 A0 00 00 00            mov byte ptr [rsp + 0xa0], al
00A1B414  40 8A C6                        mov al, sil
00A1B417  88 84 24 AD 00 00 00            mov byte ptr [rsp + 0xad], al
00A1B41E  88 84 24 AC 00 00 00            mov byte ptr [rsp + 0xac], al
00A1B425  8B C6                           mov eax, esi
00A1B427  48 89 84 24 88 01 00 00         mov qword ptr [rsp + 0x188], rax
00A1B42F  88 84 24 A4 00 00 00            mov byte ptr [rsp + 0xa4], al
00A1B436  88 84 24 A3 00 00 00            mov byte ptr [rsp + 0xa3], al
00A1B43D  8A 84 24 FD 00 00 00            mov al, byte ptr [rsp + 0xfd]
00A1B444  89 84 24 00 01 00 00            mov dword ptr [rsp + 0x100], eax
00A1B44B  8B C6                           mov eax, esi
00A1B44D  89 84 24 EC 00 00 00            mov dword ptr [rsp + 0xec], eax
00A1B454  8A 84 24 04 01 00 00            mov al, byte ptr [rsp + 0x104]
00A1B45B  89 84 24 D0 01 00 00            mov dword ptr [rsp + 0x1d0], eax
00A1B462  48 8B 84 24 90 02 00 00         mov rax, qword ptr [rsp + 0x290]
00A1B46A  48 89 84 24 78 02 00 00         mov qword ptr [rsp + 0x278], rax
00A1B472  4C 8B AC 24 80 02 00 00         mov r13, qword ptr [rsp + 0x280]
00A1B47A  48 8B 84 24 88 02 00 00         mov rax, qword ptr [rsp + 0x288]
00A1B482  48 89 84 24 18 02 00 00         mov qword ptr [rsp + 0x218], rax
00A1B48A  48 8B 9C 24 F0 01 00 00         mov rbx, qword ptr [rsp + 0x1f0]
00A1B492  48 8B 84 24 38 02 00 00         mov rax, qword ptr [rsp + 0x238]
00A1B49A  48 89 84 24 A8 01 00 00         mov qword ptr [rsp + 0x1a8], rax
00A1B4A2  48 8B 84 24 40 02 00 00         mov rax, qword ptr [rsp + 0x240]
00A1B4AA  48 89 84 24 A0 01 00 00         mov qword ptr [rsp + 0x1a0], rax
00A1B4B2  85 FF                           test edi, edi
00A1B4B4  0F 88 21 03 00 00               js 0x140a1b7db
00A1B4BA  4D 85 ED                        test r13, r13
00A1B4BD  0F 84 94 00 00 00               je 0x140a1b557
00A1B4C3  4C 8B 05 56 CB 5B 00            mov r8, qword ptr [rip + 0x5bcb56]
00A1B4CA  49 8B 4D 00                     mov rcx, qword ptr [r13]
00A1B4CE  48 89 B4 24 58 02 00 00         mov qword ptr [rsp + 0x258], rsi
00A1B4D6  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
00A1B4DB  48 8D 84 24 58 02 00 00         lea rax, [rsp + 0x258]
00A1B4E3  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A1B4E8  44 8A AC 24 A0 00 00 00         mov r13b, byte ptr [rsp + 0xa0]
00A1B4F0  45 8A CD                        mov r9b, r13b
00A1B4F3  BA 08 00 00 00                  mov edx, 8
00A1B4F8  E8 B3 D8 E4 FF                  call 0x140868db0
00A1B4FD  8B F8                           mov edi, eax
00A1B4FF  48 8B 8C 24 58 02 00 00         mov rcx, qword ptr [rsp + 0x258]
00A1B507  48 89 8C 24 10 02 00 00         mov qword ptr [rsp + 0x210], rcx
00A1B50F  85 C0                           test eax, eax
00A1B511  79 22                           jns 0x140a1b535
00A1B513  48 89 B4 24 10 02 00 00         mov qword ptr [rsp + 0x210], rsi
00A1B51B  3D 08 00 00 C0                  cmp eax, 0xc0000008
00A1B520  0F 95 84 24 07 01 00 00         setne byte ptr [rsp + 0x107]
00A1B528  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
00A1B530  E9 C4 21 00 00                  jmp 0x140a1d6f9
00A1B535  48 8B 84 24 48 01 00 00         mov rax, qword ptr [rsp + 0x148]
00A1B53D  48 89 84 24 50 02 00 00         mov qword ptr [rsp + 0x250], rax
00A1B545  48 89 8C 24 48 01 00 00         mov qword ptr [rsp + 0x148], rcx
00A1B54D  44 88 B4 24 FC 00 00 00         mov byte ptr [rsp + 0xfc], r14b
00A1B555  EB 08                           jmp 0x140a1b55f
00A1B557  44 8A AC 24 A0 00 00 00         mov r13b, byte ptr [rsp + 0xa0]
00A1B55F  48 8B 84 24 58 01 00 00         mov rax, qword ptr [rsp + 0x158]
00A1B567  48 39 B4 24 48 01 00 00         cmp qword ptr [rsp + 0x148], rsi
00A1B56F  48 0F 45 84 24 48 01 00 00      cmovne rax, qword ptr [rsp + 0x148]
00A1B578  48 89 84 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], rax
00A1B580  41 8A D5                        mov dl, r13b
00A1B583  48 8D 8C 24 48 01 00 00         lea rcx, [rsp + 0x148]
00A1B58B  E8 B8 98 F5 FF                  call 0x140974e48
00A1B590  84 C0                           test al, al
00A1B592  75 12                           jne 0x140a1b5a6
00A1B594  44 84 B4 24 88 03 00 00         test byte ptr [rsp + 0x388], r14b
00A1B59C  74 1F                           je 0x140a1b5bd
00A1B59E  44 88 B4 24 05 01 00 00         mov byte ptr [rsp + 0x105], r14b
00A1B5A6  F7 84 24 78 03 00 00 00 00 00 F0  test dword ptr [rsp + 0x378], 0xf0000000
00A1B5B1  74 14                           je 0x140a1b5c7
00A1B5B3  BF E6 00 00 C0                  mov edi, 0xc00000e6
00A1B5B8  E9 6B FF FF FF                  jmp 0x140a1b528
00A1B5BD  BF 61 00 00 C0                  mov edi, 0xc0000061
00A1B5C2  E9 61 FF FF FF                  jmp 0x140a1b528
00A1B5C7  48 8D 84 24 D8 00 00 00         lea rax, [rsp + 0xd8]
00A1B5CF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A1B5D4  45 33 C9                        xor r9d, r9d
00A1B5D7  45 8B C6                        mov r8d, r14d
00A1B5DA  41 8A D5                        mov dl, r13b
00A1B5DD  48 8B CB                        mov rcx, rbx
00A1B5E0  E8 5B E9 F0 FF                  call 0x140929f40
00A1B5E5  8B F8                           mov edi, eax
00A1B5E7  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00A1B5EE  85 C0                           test eax, eax
00A1B5F0  79 0D                           jns 0x140a1b5ff
00A1B5F2  48 89 B4 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rsi
00A1B5FA  E9 29 FF FF FF                  jmp 0x140a1b528
00A1B5FF  48 39 B4 24 D8 00 00 00         cmp qword ptr [rsp + 0xd8], rsi
00A1B607  75 0A                           jne 0x140a1b613
00A1B609  BF 79 00 00 C0                  mov edi, 0xc0000079
00A1B60E  E9 15 FF FF FF                  jmp 0x140a1b528
00A1B613  48 8B 9C 24 D8 00 00 00         mov rbx, qword ptr [rsp + 0xd8]
00A1B61B  0F B7 4B 02                     movzx ecx, word ptr [rbx + 2]
00A1B61F  66 85 C9                        test cx, cx
00A1B622  79 0C                           jns 0x140a1b630
00A1B624  8B 43 04                        mov eax, dword ptr [rbx + 4]
00A1B627  85 C0                           test eax, eax
00A1B629  74 DE                           je 0x140a1b609
00A1B62B  48 03 C3                        add rax, rbx
00A1B62E  EB 0C                           jmp 0x140a1b63c
00A1B630  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00A1B638  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00A1B63C  48 85 C0                        test rax, rax
00A1B63F  74 C8                           je 0x140a1b609
00A1B641  66 85 C9                        test cx, cx
00A1B644  79 14                           jns 0x140a1b65a
00A1B646  48 8B 9C 24 D8 00 00 00         mov rbx, qword ptr [rsp + 0xd8]
00A1B64E  8B 43 08                        mov eax, dword ptr [rbx + 8]
00A1B651  85 C0                           test eax, eax
00A1B653  74 B4                           je 0x140a1b609
00A1B655  48 03 C3                        add rax, rbx
00A1B658  EB 0C                           jmp 0x140a1b666
00A1B65A  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00A1B662  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
00A1B666  48 85 C0                        test rax, rax
00A1B669  74 9E                           je 0x140a1b609
00A1B66B  4C 39 BC 24 48 02 00 00         cmp qword ptr [rsp + 0x248], r15
00A1B673  4C 0F 42 BC 24 60 02 00 00      cmovb r15, qword ptr [rsp + 0x260]
00A1B67C  41 8A 07                        mov al, byte ptr [r15]
00A1B67F  41 88 07                        mov byte ptr [r15], al
00A1B682  48 8D 94 24 E0 01 00 00         lea rdx, [rsp + 0x1e0]
00A1B68A  48 8B 8C 24 78 02 00 00         mov rcx, qword ptr [rsp + 0x278]
00A1B692  E8 D9 99 F5 FF                  call 0x140975070
00A1B697  8B F8                           mov edi, eax
00A1B699  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00A1B6A0  85 C0                           test eax, eax
00A1B6A2  78 40                           js 0x140a1b6e4
00A1B6A4  48 8D 94 24 B0 01 00 00         lea rdx, [rsp + 0x1b0]
00A1B6AC  48 8B 8C 24 18 02 00 00         mov rcx, qword ptr [rsp + 0x218]
00A1B6B4  E8 B7 99 F5 FF                  call 0x140975070
00A1B6B9  8B F8                           mov edi, eax
00A1B6BB  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00A1B6C2  85 C0                           test eax, eax
00A1B6C4  78 1E                           js 0x140a1b6e4
00A1B6C6  48 8D 94 24 E8 01 00 00         lea rdx, [rsp + 0x1e8]
00A1B6CE  48 8B 8C 24 20 02 00 00         mov rcx, qword ptr [rsp + 0x220]
00A1B6D6  E8 95 99 F5 FF                  call 0x140975070
00A1B6DB  8B F8                           mov edi, eax
00A1B6DD  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00A1B6E4  48 8B 84 24 00 02 00 00         mov rax, qword ptr [rsp + 0x200]
00A1B6EC  44 8B AC 24 D0 01 00 00         mov r13d, dword ptr [rsp + 0x1d0]
00A1B6F4  8A 9C 24 A0 00 00 00            mov bl, byte ptr [rsp + 0xa0]
00A1B6FB  E9 A8 00 00 00                  jmp 0x140a1b7a8
00A1B700  8B F8                           mov edi, eax
00A1B702  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00A1B709  33 F6                           xor esi, esi
00A1B70B  44 8D 76 01                     lea r14d, [rsi + 1]
00A1B70F  44 8B E6                        mov r12d, esi
00A1B712  8B C6                           mov eax, esi
00A1B714  48 89 84 24 38 01 00 00         mov qword ptr [rsp + 0x138], rax
00A1B71C  89 84 24 08 01 00 00            mov dword ptr [rsp + 0x108], eax
00A1B723  8A 8C 24 F8 00 00 00            mov cl, byte ptr [rsp + 0xf8]
00A1B72A  89 8C 24 0C 01 00 00            mov dword ptr [rsp + 0x10c], ecx
00A1B731  8A 9C 24 E0 00 00 00            mov bl, byte ptr [rsp + 0xe0]
00A1B738  88 9C 24 A0 00 00 00            mov byte ptr [rsp + 0xa0], bl
00A1B73F  88 84 24 AD 00 00 00            mov byte ptr [rsp + 0xad], al
00A1B746  88 84 24 AC 00 00 00            mov byte ptr [rsp + 0xac], al
00A1B74D  48 89 84 24 88 01 00 00         mov qword ptr [rsp + 0x188], rax
00A1B755  88 84 24 A4 00 00 00            mov byte ptr [rsp + 0xa4], al
00A1B75C  88 84 24 A3 00 00 00            mov byte ptr [rsp + 0xa3], al
00A1B763  8A 84 24 FD 00 00 00            mov al, byte ptr [rsp + 0xfd]
00A1B76A  89 84 24 00 01 00 00            mov dword ptr [rsp + 0x100], eax
00A1B771  89 B4 24 EC 00 00 00            mov dword ptr [rsp + 0xec], esi
00A1B778  44 8A AC 24 04 01 00 00         mov r13b, byte ptr [rsp + 0x104]
00A1B780  48 8B 84 24 00 02 00 00         mov rax, qword ptr [rsp + 0x200]
00A1B788  48 8B 8C 24 38 02 00 00         mov rcx, qword ptr [rsp + 0x238]
00A1B790  48 89 8C 24 A8 01 00 00         mov qword ptr [rsp + 0x1a8], rcx
00A1B798  48 8B 8C 24 40 02 00 00         mov rcx, qword ptr [rsp + 0x240]
00A1B7A0  48 89 8C 24 A0 01 00 00         mov qword ptr [rsp + 0x1a0], rcx
00A1B7A8  85 FF                           test edi, edi
00A1B7AA  78 2F                           js 0x140a1b7db
00A1B7AC  48 85 C0                        test rax, rax
00A1B7AF  74 37                           je 0x140a1b7e8
00A1B7B1  48 8D 8C 24 90 01 00 00         lea rcx, [rsp + 0x190]
00A1B7B9  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00A1B7BE  44 88 74 24 28                  mov byte ptr [rsp + 0x28], r14b
00A1B7C3  8A D3                           mov dl, bl
00A1B7C5  48 8B C8                        mov rcx, rax
00A1B7C8  E8 07 BF F0 FF                  call 0x1409276d4
00A1B7CD  8B F8                           mov edi, eax
00A1B7CF  85 C0                           test eax, eax
00A1B7D1  79 15                           jns 0x140a1b7e8
00A1B7D3  48 89 B4 24 90 01 00 00         mov qword ptr [rsp + 0x190], rsi
00A1B7DB  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
00A1B7E3  E9 09 1F 00 00                  jmp 0x140a1d6f1
00A1B7E8  4C 8D 8C 24 40 01 00 00         lea r9, [rsp + 0x140]
00A1B7F0  44 8A C3                        mov r8b, bl
00A1B7F3  8B 94 24 C0 00 00 00            mov edx, dword ptr [rsp + 0xc0]
00A1B7FA  48 8B 8C 24 F8 01 00 00         mov rcx, qword ptr [rsp + 0x1f8]
00A1B802  E8 19 8B A1 FF                  call 0x140434320
00A1B807  8B F8                           mov edi, eax
00A1B809  85 C0                           test eax, eax
00A1B80B  78 CE                           js 0x140a1b7db
00A1B80D  48 8D 84 24 98 01 00 00         lea rax, [rsp + 0x198]
00A1B815  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A1B81A  44 88 74 24 28                  mov byte ptr [rsp + 0x28], r14b
00A1B81F  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00A1B824  45 33 C9                        xor r9d, r9d
00A1B827  4C 8D 84 24 48 01 00 00         lea r8, [rsp + 0x148]
00A1B82F  48 8B 9C 24 D8 00 00 00         mov rbx, qword ptr [rsp + 0xd8]
00A1B837  48 8B D3                        mov rdx, rbx
00A1B83A  E8 A1 1F 9D FF                  call 0x1403ed7e0
00A1B83F  8B F8                           mov edi, eax
00A1B841  85 C0                           test eax, eax
00A1B843  78 96                           js 0x140a1b7db
00A1B845  44 8B BC 24 78 03 00 00         mov r15d, dword ptr [rsp + 0x378]
00A1B84D  41 8B D7                        mov edx, r15d
00A1B850  48 8D 8C 24 98 01 00 00         lea rcx, [rsp + 0x198]
00A1B858  E8 63 34 A0 FF                  call 0x14041ecc0
00A1B85D  8B F8                           mov edi, eax
00A1B85F  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00A1B866  0F B6 84 24 B4 00 00 00         movzx eax, byte ptr [rsp + 0xb4]
00A1B86E  85 FF                           test edi, edi
00A1B870  41 0F 48 C6                     cmovs eax, r14d
00A1B874  88 84 24 B4 00 00 00            mov byte ptr [rsp + 0xb4], al
00A1B87B  0F 88 CE 01 00 00               js 0x140a1ba4f
00A1B881  48 8D 84 24 D8 01 00 00         lea rax, [rsp + 0x1d8]
00A1B889  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A1B88E  45 8A CE                        mov r9b, r14b
00A1B891  4C 8B 84 24 F0 00 00 00         mov r8, qword ptr [rsp + 0xf0]
00A1B899  48 8D 94 24 20 01 00 00         lea rdx, [rsp + 0x120]
00A1B8A1  48 8B CB                        mov rcx, rbx
00A1B8A4  E8 B7 62 8E FF                  call 0x140301b60
00A1B8A9  8B F8                           mov edi, eax
00A1B8AB  85 C0                           test eax, eax
00A1B8AD  0F 88 28 FF FF FF               js 0x140a1b7db
00A1B8B3  41 8B D7                        mov edx, r15d
00A1B8B6  48 8D 8C 24 D8 01 00 00         lea rcx, [rsp + 0x1d8]
00A1B8BE  E8 FD 33 A0 FF                  call 0x14041ecc0
00A1B8C3  8B F8                           mov edi, eax
00A1B8C5  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00A1B8CC  0F B6 84 24 B5 00 00 00         movzx eax, byte ptr [rsp + 0xb5]
00A1B8D4  85 FF                           test edi, edi
00A1B8D6  41 0F 48 C6                     cmovs eax, r14d
00A1B8DA  88 84 24 B5 00 00 00            mov byte ptr [rsp + 0xb5], al
00A1B8E1  0F 88 68 01 00 00               js 0x140a1ba4f
00A1B8E7  48 8D 84 24 68 02 00 00         lea rax, [rsp + 0x268]
00A1B8EF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A1B8F4  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
00A1B8F9  48 8B 9C 24 F0 00 00 00         mov rbx, qword ptr [rsp + 0xf0]
00A1B901  4C 8B CB                        mov r9, rbx
00A1B904  45 33 C0                        xor r8d, r8d
00A1B907  48 8B 94 24 D8 00 00 00         mov rdx, qword ptr [rsp + 0xd8]
00A1B90F  48 8D 8C 24 E0 02 00 00         lea rcx, [rsp + 0x2e0]
00A1B917  E8 C4 3B 84 FF                  call 0x14025f4e0
00A1B91C  8B F8                           mov edi, eax
00A1B91E  85 C0                           test eax, eax
00A1B920  0F 88 B5 FE FF FF               js 0x140a1b7db
00A1B926  41 8B D7                        mov edx, r15d
00A1B929  48 8D 8C 24 68 02 00 00         lea rcx, [rsp + 0x268]
00A1B931  E8 0A 06 A0 FF                  call 0x14041bf40
00A1B936  8B F8                           mov edi, eax
00A1B938  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00A1B93F  85 C0                           test eax, eax
00A1B941  78 07                           js 0x140a1b94a
00A1B943  41 0F BA E7 19                  bt r15d, 0x19
00A1B948  73 2C                           jae 0x140a1b976
00A1B94A  F7 83 C8 00 00 00 00 40 00 00   test dword ptr [rbx + 0xc8], 0x4000
00A1B954  74 20                           je 0x140a1b976
00A1B956  8B 84 24 00 01 00 00            mov eax, dword ptr [rsp + 0x100]
00A1B95D  0F B6 C0                        movzx eax, al
00A1B960  81 BC 24 74 02 00 00 00 20 00 00  cmp dword ptr [rsp + 0x274], 0x2000
00A1B96B  41 0F 46 C6                     cmovbe eax, r14d
00A1B96F  89 84 24 00 01 00 00            mov dword ptr [rsp + 0x100], eax
00A1B976  E8 ED 1F BB FF                  call 0x1405cd968
00A1B97B  85 C0                           test eax, eax
00A1B97D  74 60                           je 0x140a1b9df
00A1B97F  48 8D 84 24 18 01 00 00         lea rax, [rsp + 0x118]
00A1B987  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A1B98C  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
00A1B991  45 8A CE                        mov r9b, r14b
00A1B994  45 33 C0                        xor r8d, r8d
00A1B997  48 8D 94 24 48 01 00 00         lea rdx, [rsp + 0x148]
00A1B99F  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
00A1B9A7  E8 D4 CA BE FF                  call 0x140608480
00A1B9AC  85 C0                           test eax, eax
00A1B9AE  78 11                           js 0x140a1b9c1
00A1B9B0  8B 84 24 18 01 00 00            mov eax, dword ptr [rsp + 0x118]
00A1B9B7  41 23 C7                        and eax, r15d
00A1B9BA  A9 FF FF FF FD                  test eax, 0xfdffffff
00A1B9BF  74 1E                           je 0x140a1b9df
00A1B9C1  48 8B 84 24 A8 01 00 00         mov rax, qword ptr [rsp + 0x1a8]
00A1B9C9  89 30                           mov dword ptr [rax], esi
00A1B9CB  BF C0 01 00 C0                  mov edi, 0xc00001c0
00A1B9D0  48 8B 84 24 A0 01 00 00         mov rax, qword ptr [rsp + 0x1a0]
00A1B9D8  89 38                           mov dword ptr [rax], edi
00A1B9DA  E9 FC FD FF FF                  jmp 0x140a1b7db
00A1B9DF  44 8B A4 24 00 01 00 00         mov r12d, dword ptr [rsp + 0x100]
00A1B9E7  85 FF                           test edi, edi
00A1B9E9  79 05                           jns 0x140a1b9f0
00A1B9EB  45 84 E4                        test r12b, r12b
00A1B9EE  74 6F                           je 0x140a1ba5f
00A1B9F0  8A 84 24 A0 00 00 00            mov al, byte ptr [rsp + 0xa0]
00A1B9F7  88 44 24 28                     mov byte ptr [rsp + 0x28], al
00A1B9FB  48 8D 84 24 C0 01 00 00         lea rax, [rsp + 0x1c0]
00A1BA03  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A1BA08  45 33 C9                        xor r9d, r9d
00A1BA0B  4C 8D 84 24 48 01 00 00         lea r8, [rsp + 0x148]
00A1BA13  48 8D 94 24 E4 00 00 00         lea rdx, [rsp + 0xe4]
00A1BA1B  48 8D 8C 24 78 03 00 00         lea rcx, [rsp + 0x378]
00A1BA23  E8 D8 5C 9B FF                  call 0x1403d1700
00A1BA28  8B F8                           mov edi, eax
00A1BA2A  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00A1BA31  44 8B BC 24 78 03 00 00         mov r15d, dword ptr [rsp + 0x378]
00A1BA39  45 85 FF                        test r15d, r15d
00A1BA3C  75 21                           jne 0x140a1ba5f
00A1BA3E  45 0F B6 ED                     movzx r13d, r13b
00A1BA42  39 B4 24 E4 00 00 00            cmp dword ptr [rsp + 0xe4], esi
00A1BA49  45 0F 45 EE                     cmovne r13d, r14d
00A1BA4D  EB 10                           jmp 0x140a1ba5f
00A1BA4F  48 8B 9C 24 F0 00 00 00         mov rbx, qword ptr [rsp + 0xf0]
00A1BA57  44 8B A4 24 00 01 00 00         mov r12d, dword ptr [rsp + 0x100]
00A1BA5F  48 8D 8C 24 48 01 00 00         lea rcx, [rsp + 0x148]
00A1BA67  E8 54 AA EA FF                  call 0x1408c64c0
00A1BA6C  85 FF                           test edi, edi
00A1BA6E  0F 89 AF 00 00 00               jns 0x140a1bb23
00A1BA74  45 84 E4                        test r12b, r12b
00A1BA77  0F 85 A6 00 00 00               jne 0x140a1bb23
00A1BA7D  44 88 B4 24 A2 00 00 00         mov byte ptr [rsp + 0xa2], r14b
00A1BA85  89 BC 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], edi
00A1BA8C  44 38 A4 24 C0 03 00 00         cmp byte ptr [rsp + 0x3c0], r12b
00A1BA94  0F 84 F4 0B 00 00               je 0x140a1c68e
00A1BA9A  8B 9C 24 C0 00 00 00            mov ebx, dword ptr [rsp + 0xc0]
00A1BAA1  48 8D 14 DD 00 00 00 00         lea rdx, [rbx*8]
00A1BAA9  B9 00 01 00 00                  mov ecx, 0x100
00A1BAAE  41 B8 53 65 47 61               mov r8d, 0x61476553
00A1BAB4  E8 37 66 16 00                  call 0x140b820f0
00A1BAB9  4C 8B E0                        mov r12, rax
00A1BABC  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
00A1BAC4  48 85 C0                        test rax, rax
00A1BAC7  75 17                           jne 0x140a1bae0
00A1BAC9  48 8D 8C 24 48 01 00 00         lea rcx, [rsp + 0x148]
00A1BAD1  E8 4A AA EA FF                  call 0x1408c6520
00A1BAD6  BF 9A 00 00 C0                  mov edi, 0xc000009a
00A1BADB  E9 FB FC FF FF                  jmp 0x140a1b7db
00A1BAE0  44 88 B4 24 AE 00 00 00         mov byte ptr [rsp + 0xae], r14b
00A1BAE8  4C 8D 2C 98                     lea r13, [rax + rbx*4]
00A1BAEC  39 B4 24 C0 00 00 00            cmp dword ptr [rsp + 0xc0], esi
00A1BAF3  0F 86 7A 13 00 00               jbe 0x140a1ce73
00A1BAF9  49 8B CD                        mov rcx, r13
00A1BAFC  48 8B D0                        mov rdx, rax
00A1BAFF  49 2B D5                        sub rdx, r13
00A1BB02  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
00A1BB09  89 04 0A                        mov dword ptr [rdx + rcx], eax
00A1BB0C  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
00A1BB13  89 01                           mov dword ptr [rcx], eax
00A1BB15  48 8D 49 04                     lea rcx, [rcx + 4]
00A1BB19  49 2B DE                        sub rbx, r14
00A1BB1C  75 E4                           jne 0x140a1bb02
00A1BB1E  E9 50 13 00 00                  jmp 0x140a1ce73
00A1BB23  48 8B 94 24 D8 00 00 00         mov rdx, qword ptr [rsp + 0xd8]
00A1BB2B  48 8B CB                        mov rcx, rbx
00A1BB2E  E8 2D A2 9C FF                  call 0x1403e5d60
00A1BB33  88 84 24 A3 00 00 00            mov byte ptr [rsp + 0xa3], al
00A1BB3A  8A 0D 85 8F 4E 00               mov cl, byte ptr [rip + 0x4e8f85]
00A1BB40  84 C9                           test cl, cl
00A1BB42  74 3D                           je 0x140a1bb81
00A1BB44  48 8B 9C 24 D8 00 00 00         mov rbx, qword ptr [rsp + 0xd8]
00A1BB4C  0F B7 53 02                     movzx edx, word ptr [rbx + 2]
00A1BB50  F6 C2 10                        test dl, 0x10
00A1BB53  74 24                           je 0x140a1bb79
00A1BB55  44 0F 20 C1                     mov rcx, cr8
00A1BB59  80 F9 02                        cmp cl, 2
00A1BB5C  73 1B                           jae 0x140a1bb79
00A1BB5E  66 85 D2                        test dx, dx
00A1BB61  79 71                           jns 0x140a1bbd4
00A1BB63  8B 43 0C                        mov eax, dword ptr [rbx + 0xc]
00A1BB66  85 C0                           test eax, eax
00A1BB68  75 60                           jne 0x140a1bbca
00A1BB6A  48 89 B4 24 88 01 00 00         mov qword ptr [rsp + 0x188], rsi
00A1BB72  8A 84 24 A3 00 00 00            mov al, byte ptr [rsp + 0xa3]
00A1BB79  48 8B 9C 24 F0 00 00 00         mov rbx, qword ptr [rsp + 0xf0]
00A1BB81  44 8A A4 24 A5 00 00 00         mov r12b, byte ptr [rsp + 0xa5]
00A1BB89  8B BC 24 A8 00 00 00            mov edi, dword ptr [rsp + 0xa8]
00A1BB90  44 8B BC 24 78 03 00 00         mov r15d, dword ptr [rsp + 0x378]
00A1BB98  41 F7 C7 00 00 06 02            test r15d, 0x2060000
00A1BB9F  0F 84 1C 01 00 00               je 0x140a1bcc1
00A1BBA5  84 C0                           test al, al
00A1BBA7  0F 84 14 01 00 00               je 0x140a1bcc1
00A1BBAD  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00A1BBB5  0F B7 48 02                     movzx ecx, word ptr [rax + 2]
00A1BBB9  F6 C1 04                        test cl, 4
00A1BBBC  0F 85 8E 00 00 00               jne 0x140a1bc50
00A1BBC2  48 8B CE                        mov rcx, rsi
00A1BBC5  E9 A7 00 00 00                  jmp 0x140a1bc71
00A1BBCA  48 03 84 24 D8 00 00 00         add rax, qword ptr [rsp + 0xd8]
00A1BBD2  EB 0C                           jmp 0x140a1bbe0
00A1BBD4  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00A1BBDC  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
00A1BBE0  48 89 84 24 88 01 00 00         mov qword ptr [rsp + 0x188], rax
00A1BBE8  48 85 C0                        test rax, rax
00A1BBEB  74 85                           je 0x140a1bb72
00A1BBED  48 8B C8                        mov rcx, rax
00A1BBF0  E8 B7 9D 98 FF                  call 0x1403a59ac
00A1BBF5  48 85 C0                        test rax, rax
00A1BBF8  0F 84 74 FF FF FF               je 0x140a1bb72
00A1BBFE  48 8D 94 24 78 01 00 00         lea rdx, [rsp + 0x178]
00A1BC06  48 8B C8                        mov rcx, rax
00A1BC09  E8 DE 9C 98 FF                  call 0x1403a58ec
00A1BC0E  48 8B 94 24 78 01 00 00         mov rdx, qword ptr [rsp + 0x178]
00A1BC16  85 C0                           test eax, eax
00A1BC18  48 0F 48 15 D0 C4 5B 00         cmovs rdx, qword ptr [rip + 0x5bc4d0]
00A1BC20  48 89 94 24 78 01 00 00         mov qword ptr [rsp + 0x178], rdx
00A1BC28  8B FE                           mov edi, esi
00A1BC2A  89 B4 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], esi
00A1BC31  45 8A E6                        mov r12b, r14b
00A1BC34  44 88 B4 24 A5 00 00 00         mov byte ptr [rsp + 0xa5], r14b
00A1BC3C  48 8B 9C 24 F0 00 00 00         mov rbx, qword ptr [rsp + 0xf0]
00A1BC44  8A 84 24 A3 00 00 00            mov al, byte ptr [rsp + 0xa3]
00A1BC4B  E9 40 FF FF FF                  jmp 0x140a1bb90
00A1BC50  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00A1BC58  66 85 C9                        test cx, cx
00A1BC5B  79 10                           jns 0x140a1bc6d
00A1BC5D  8B 48 10                        mov ecx, dword ptr [rax + 0x10]
00A1BC60  85 C9                           test ecx, ecx
00A1BC62  0F 84 5A FF FF FF               je 0x140a1bbc2
00A1BC68  48 03 C8                        add rcx, rax
00A1BC6B  EB 04                           jmp 0x140a1bc71
00A1BC6D  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
00A1BC71  E8 9A 1D 9E FF                  call 0x1403fda10
00A1BC76  84 C0                           test al, al
00A1BC78  75 47                           jne 0x140a1bcc1
00A1BC7A  B9 00 00 06 00                  mov ecx, 0x60000
00A1BC7F  41 0F BA E7 19                  bt r15d, 0x19
00A1BC84  73 12                           jae 0x140a1bc98
00A1BC86  89 8C 24 EC 00 00 00            mov dword ptr [rsp + 0xec], ecx
00A1BC8D  8B 84 24 E4 00 00 00            mov eax, dword ptr [rsp + 0xe4]
00A1BC94  0B C1                           or eax, ecx
00A1BC96  EB 13                           jmp 0x140a1bcab
00A1BC98  41 8B C7                        mov eax, r15d
00A1BC9B  23 C1                           and eax, ecx
00A1BC9D  89 84 24 EC 00 00 00            mov dword ptr [rsp + 0xec], eax
00A1BCA4  0B 84 24 E4 00 00 00            or eax, dword ptr [rsp + 0xe4]
00A1BCAB  89 84 24 E4 00 00 00            mov dword ptr [rsp + 0xe4], eax
00A1BCB2  41 81 E7 FF FF F9 FF            and r15d, 0xfff9ffff
00A1BCB9  44 89 BC 24 78 03 00 00         mov dword ptr [rsp + 0x378], r15d
00A1BCC1  E8 C2 3A AD FF                  call 0x1404ef788
00A1BCC6  85 C0                           test eax, eax
00A1BCC8  0F 84 D4 08 00 00               je 0x140a1c5a2
00A1BCCE  45 85 FF                        test r15d, r15d
00A1BCD1  0F 85 00 01 00 00               jne 0x140a1bdd7
00A1BCD7  45 84 E4                        test r12b, r12b
00A1BCDA  74 09                           je 0x140a1bce5
00A1BCDC  45 84 ED                        test r13b, r13b
00A1BCDF  0F 84 F2 00 00 00               je 0x140a1bdd7
00A1BCE5  8B 83 C8 00 00 00               mov eax, dword ptr [rbx + 0xc8]
00A1BCEB  25 00 60 00 00                  and eax, 0x6000
00A1BCF0  3D 00 20 00 00                  cmp eax, 0x2000
00A1BCF5  74 0D                           je 0x140a1bd04
00A1BCF7  39 B4 24 EC 00 00 00            cmp dword ptr [rsp + 0xec], esi
00A1BCFE  0F 85 D3 00 00 00               jne 0x140a1bdd7
00A1BD04  8B 84 24 E4 00 00 00            mov eax, dword ptr [rsp + 0xe4]
00A1BD0B  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
00A1BD12  85 C0                           test eax, eax
00A1BD14  75 0D                           jne 0x140a1bd23
00A1BD16  BA 22 00 00 C0                  mov edx, 0xc0000022
00A1BD1B  41 8A C6                        mov al, r14b
00A1BD1E  40 8A CE                        mov cl, sil
00A1BD21  EB 08                           jmp 0x140a1bd2b
00A1BD23  8B D6                           mov edx, esi
00A1BD25  40 8A C6                        mov al, sil
00A1BD28  41 8A CE                        mov cl, r14b
00A1BD2B  88 8C 24 A1 00 00 00            mov byte ptr [rsp + 0xa1], cl
00A1BD32  88 84 24 A2 00 00 00            mov byte ptr [rsp + 0xa2], al
00A1BD39  89 94 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], edx
00A1BD40  40 38 B4 24 C0 03 00 00         cmp byte ptr [rsp + 0x3c0], sil
00A1BD48  0F 84 40 09 00 00               je 0x140a1c68e
00A1BD4E  8B 9C 24 C0 00 00 00            mov ebx, dword ptr [rsp + 0xc0]
00A1BD55  48 8D 14 DD 00 00 00 00         lea rdx, [rbx*8]
00A1BD5D  B9 00 01 00 00                  mov ecx, 0x100
00A1BD62  41 B8 53 65 47 61               mov r8d, 0x61476553
00A1BD68  E8 83 63 16 00                  call 0x140b820f0
00A1BD6D  4C 8B E0                        mov r12, rax
00A1BD70  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
00A1BD78  48 85 C0                        test rax, rax
00A1BD7B  75 17                           jne 0x140a1bd94
00A1BD7D  BF 9A 00 00 C0                  mov edi, 0xc000009a
00A1BD82  48 8D 8C 24 48 01 00 00         lea rcx, [rsp + 0x148]
00A1BD8A  E8 91 A7 EA FF                  call 0x1408c6520
00A1BD8F  E9 47 FA FF FF                  jmp 0x140a1b7db
00A1BD94  44 88 B4 24 AE 00 00 00         mov byte ptr [rsp + 0xae], r14b
00A1BD9C  4C 8D 2C 98                     lea r13, [rax + rbx*4]
00A1BDA0  39 B4 24 C0 00 00 00            cmp dword ptr [rsp + 0xc0], esi
00A1BDA7  0F 86 C6 10 00 00               jbe 0x140a1ce73
00A1BDAD  49 8B CD                        mov rcx, r13
00A1BDB0  48 8B D0                        mov rdx, rax
00A1BDB3  49 2B D5                        sub rdx, r13
00A1BDB6  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
00A1BDBD  89 04 11                        mov dword ptr [rcx + rdx], eax
00A1BDC0  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
00A1BDC7  89 01                           mov dword ptr [rcx], eax
00A1BDC9  48 8D 49 04                     lea rcx, [rcx + 4]
00A1BDCD  49 2B DE                        sub rbx, r14
00A1BDD0  75 E4                           jne 0x140a1bdb6
00A1BDD2  E9 9C 10 00 00                  jmp 0x140a1ce73
00A1BDD7  8B BC 24 68 01 00 00            mov edi, dword ptr [rsp + 0x168]
00A1BDDE  48 89 BC 24 F0 01 00 00         mov qword ptr [rsp + 0x1f0], rdi
00A1BDE6  48 8D 1C FD 00 00 00 00         lea rbx, [rdi*8]
00A1BDEE  40 38 B4 24 C0 03 00 00         cmp byte ptr [rsp + 0x3c0], sil
00A1BDF6  74 35                           je 0x140a1be2d
00A1BDF8  41 B8 53 65 47 61               mov r8d, 0x61476553
00A1BDFE  48 8B D3                        mov rdx, rbx
00A1BE01  B9 00 01 00 00                  mov ecx, 0x100
00A1BE06  E8 E5 62 16 00                  call 0x140b820f0
00A1BE0B  4C 8B E0                        mov r12, rax
00A1BE0E  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
00A1BE16  48 85 C0                        test rax, rax
00A1BE19  0F 84 5E FF FF FF               je 0x140a1bd7d
00A1BE1F  44 88 B4 24 AE 00 00 00         mov byte ptr [rsp + 0xae], r14b
00A1BE27  4C 8D 2C B8                     lea r13, [rax + rdi*4]
00A1BE2B  EB 18                           jmp 0x140a1be45
00A1BE2D  4C 8D A4 24 B8 00 00 00         lea r12, [rsp + 0xb8]
00A1BE35  4C 89 A4 24 30 01 00 00         mov qword ptr [rsp + 0x130], r12
00A1BE3D  4C 8D AC 24 B0 00 00 00         lea r13, [rsp + 0xb0]
00A1BE45  8B 84 24 EC 00 00 00            mov eax, dword ptr [rsp + 0xec]
00A1BE4C  89 84 24 C0 02 00 00            mov dword ptr [rsp + 0x2c0], eax
00A1BE53  48 8D 84 24 A2 00 00 00         lea rax, [rsp + 0xa2]
00A1BE5B  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00A1BE63  48 8D 84 24 A1 00 00 00         lea rax, [rsp + 0xa1]
00A1BE6B  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00A1BE73  48 8D 84 24 20 01 00 00         lea rax, [rsp + 0x120]
00A1BE7B  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00A1BE83  48 8D 84 24 C0 02 00 00         lea rax, [rsp + 0x2c0]
00A1BE8B  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00A1BE90  8A 84 24 A3 00 00 00            mov al, byte ptr [rsp + 0xa3]
00A1BE97  88 44 24 70                     mov byte ptr [rsp + 0x70], al
00A1BE9B  8A 84 24 C0 03 00 00            mov al, byte ptr [rsp + 0x3c0]
00A1BEA2  88 44 24 68                     mov byte ptr [rsp + 0x68], al
00A1BEA6  4C 89 6C 24 60                  mov qword ptr [rsp + 0x60], r13
00A1BEAB  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
00A1BEB0  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
00A1BEB5  8A 84 24 A0 00 00 00            mov al, byte ptr [rsp + 0xa0]
00A1BEBC  88 44 24 48                     mov byte ptr [rsp + 0x48], al
00A1BEC0  8B 84 24 E4 00 00 00            mov eax, dword ptr [rsp + 0xe4]
00A1BEC7  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A1BECB  48 8D 84 24 E0 02 00 00         lea rax, [rsp + 0x2e0]
00A1BED3  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A1BED8  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
00A1BEDF  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A1BEE3  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
00A1BEEB  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A1BEF0  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
00A1BEF5  4C 8B 8C 24 F0 00 00 00         mov r9, qword ptr [rsp + 0xf0]
00A1BEFD  4C 8B 84 24 58 01 00 00         mov r8, qword ptr [rsp + 0x158]
00A1BF05  48 8B 94 24 90 01 00 00         mov rdx, qword ptr [rsp + 0x190]
00A1BF0D  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
00A1BF15  E8 3A 4F 9B FF                  call 0x1403d0e54
00A1BF1A  8A 05 A5 8B 4E 00               mov al, byte ptr [rip + 0x4e8ba5]
00A1BF20  84 C0                           test al, al
00A1BF22  0F 84 F9 04 00 00               je 0x140a1c421
00A1BF28  41 39 75 00                     cmp dword ptr [r13], esi
00A1BF2C  0F 8C EF 04 00 00               jl 0x140a1c421
00A1BF32  40 38 B4 24 A5 00 00 00         cmp byte ptr [rsp + 0xa5], sil
00A1BF3A  0F 84 E1 04 00 00               je 0x140a1c421
00A1BF40  40 38 B4 24 C0 03 00 00         cmp byte ptr [rsp + 0x3c0], sil
00A1BF48  74 55                           je 0x140a1bf9f
00A1BF4A  41 B8 53 65 47 61               mov r8d, 0x61476553
00A1BF50  48 8B D3                        mov rdx, rbx
00A1BF53  B9 00 01 00 00                  mov ecx, 0x100
00A1BF58  E8 93 61 16 00                  call 0x140b820f0
00A1BF5D  48 8B D8                        mov rbx, rax
00A1BF60  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
00A1BF68  48 85 C0                        test rax, rax
00A1BF6B  75 24                           jne 0x140a1bf91
00A1BF6D  48 8D 8C 24 48 01 00 00         lea rcx, [rsp + 0x148]
00A1BF75  E8 A6 A5 EA FF                  call 0x1408c6520
00A1BF7A  48 8D 8C 24 48 01 00 00         lea rcx, [rsp + 0x148]
00A1BF82  E8 89 F7 E4 FF                  call 0x14086b710
00A1BF87  BF 9A 00 00 C0                  mov edi, 0xc000009a
00A1BF8C  E9 60 17 00 00                  jmp 0x140a1d6f1
00A1BF91  48 8D 0C B8                     lea rcx, [rax + rdi*4]
00A1BF95  48 89 8C 24 38 01 00 00         mov qword ptr [rsp + 0x138], rcx
00A1BF9D  EB 20                           jmp 0x140a1bfbf
00A1BF9F  48 8D 84 24 C8 01 00 00         lea rax, [rsp + 0x1c8]
00A1BFA7  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
00A1BFAF  48 8D 84 24 CC 01 00 00         lea rax, [rsp + 0x1cc]
00A1BFB7  48 89 84 24 38 01 00 00         mov qword ptr [rsp + 0x138], rax
00A1BFBF  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
00A1BFC6  85 C0                           test eax, eax
00A1BFC8  74 2A                           je 0x140a1bff4
00A1BFCA  4C 8D 84 24 B8 01 00 00         lea r8, [rsp + 0x1b8]
00A1BFD2  8B D0                           mov edx, eax
00A1BFD4  48 8B 8C 24 40 01 00 00         mov rcx, qword ptr [rsp + 0x140]
00A1BFDC  E8 DF AC BE FF                  call 0x140606cc0
00A1BFE1  8B F8                           mov edi, eax
00A1BFE3  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00A1BFEA  85 C0                           test eax, eax
00A1BFEC  0F 88 E9 F7 FF FF               js 0x140a1b7db
00A1BFF2  EB 07                           jmp 0x140a1bffb
00A1BFF4  8B BC 24 A8 00 00 00            mov edi, dword ptr [rsp + 0xa8]
00A1BFFB  40 88 B4 24 EC 00 00 00         mov byte ptr [rsp + 0xec], sil
00A1C003  8B C6                           mov eax, esi
00A1C005  89 84 24 70 01 00 00            mov dword ptr [rsp + 0x170], eax
00A1C00C  48 8B 8C 24 78 01 00 00         mov rcx, qword ptr [rsp + 0x178]
00A1C014  44 8B BC 24 78 03 00 00         mov r15d, dword ptr [rsp + 0x378]
00A1C01C  39 71 3C                        cmp dword ptr [rcx + 0x3c], esi
00A1C01F  0F 86 AA 03 00 00               jbe 0x140a1c3cf
00A1C025  8B C8                           mov ecx, eax
00A1C027  48 8B 84 24 78 01 00 00         mov rax, qword ptr [rsp + 0x178]
00A1C02F  48 8B 5C C8 40                  mov rbx, qword ptr [rax + rcx*8 + 0x40]
00A1C034  48 89 9C 24 F8 01 00 00         mov qword ptr [rsp + 0x1f8], rbx
00A1C03C  48 39 73 18                     cmp qword ptr [rbx + 0x18], rsi
00A1C040  0F 84 D6 01 00 00               je 0x140a1c21c
00A1C046  4C 8B 84 24 20 01 00 00         mov r8, qword ptr [rsp + 0x120]
00A1C04E  4D 85 C0                        test r8, r8
00A1C051  75 34                           jne 0x140a1c087
00A1C053  48 8D 94 24 20 01 00 00         lea rdx, [rsp + 0x120]
00A1C05B  48 8B 8C 24 88 01 00 00         mov rcx, qword ptr [rsp + 0x188]
00A1C063  E8 1C 6E 8E FF                  call 0x140302e84
00A1C068  8B 94 24 EC 00 00 00            mov edx, dword ptr [rsp + 0xec]
00A1C06F  0F B6 D2                        movzx edx, dl
00A1C072  85 C0                           test eax, eax
00A1C074  41 0F 48 D6                     cmovs edx, r14d
00A1C078  89 94 24 EC 00 00 00            mov dword ptr [rsp + 0xec], edx
00A1C07F  4C 8B 84 24 20 01 00 00         mov r8, qword ptr [rsp + 0x120]
00A1C087  4C 8B 9C 24 F0 00 00 00         mov r11, qword ptr [rsp + 0xf0]
00A1C08F  49 8B 83 48 04 00 00            mov rax, qword ptr [r11 + 0x448]
00A1C096  48 85 C0                        test rax, rax
00A1C099  74 09                           je 0x140a1c0a4
00A1C09B  4C 8B 90 58 02 00 00            mov r10, qword ptr [rax + 0x258]
00A1C0A2  EB 03                           jmp 0x140a1c0a7
00A1C0A4  4C 8B D6                        mov r10, rsi
00A1C0A7  48 85 C0                        test rax, rax
00A1C0AA  74 09                           je 0x140a1c0b5
00A1C0AC  48 8B 90 48 02 00 00            mov rdx, qword ptr [rax + 0x248]
00A1C0B3  EB 03                           jmp 0x140a1c0b8
00A1C0B5  48 8B D6                        mov rdx, rsi
00A1C0B8  48 85 C0                        test rax, rax
00A1C0BB  74 09                           je 0x140a1c0c6
00A1C0BD  48 8B 88 50 02 00 00            mov rcx, qword ptr [rax + 0x250]
00A1C0C4  EB 03                           jmp 0x140a1c0c9
00A1C0C6  48 8B CE                        mov rcx, rsi
00A1C0C9  48 85 C0                        test rax, rax
00A1C0CC  74 09                           je 0x140a1c0d7
00A1C0CE  4C 8B 88 40 02 00 00            mov r9, qword ptr [rax + 0x240]
00A1C0D5  EB 03                           jmp 0x140a1c0da
00A1C0D7  4C 8B CE                        mov r9, rsi
00A1C0DA  48 8D 84 24 14 01 00 00         lea rax, [rsp + 0x114]
00A1C0E2  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00A1C0E7  40 88 74 24 50                  mov byte ptr [rsp + 0x50], sil
00A1C0EC  44 88 74 24 48                  mov byte ptr [rsp + 0x48], r14b
00A1C0F1  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
00A1C0F4  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A1C0F8  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00A1C0FC  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A1C101  4C 89 54 24 30                  mov qword ptr [rsp + 0x30], r10
00A1C106  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
00A1C10B  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00A1C110  49 8B 93 08 03 00 00            mov rdx, qword ptr [r11 + 0x308]
00A1C117  49 8B CB                        mov rcx, r11
00A1C11A  E8 B1 2A 8E FF                  call 0x1402febd0
00A1C11F  8B F8                           mov edi, eax
00A1C121  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00A1C128  44 39 B4 24 14 01 00 00         cmp dword ptr [rsp + 0x114], r14d
00A1C130  0F 84 E6 00 00 00               je 0x140a1c21c
00A1C136  85 C0                           test eax, eax
00A1C138  0F 88 9D F6 FF FF               js 0x140a1b7db
00A1C13E  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00A1C146  E8 95 CB A1 FF                  call 0x140438ce0
00A1C14B  84 C0                           test al, al
00A1C14D  0F 84 B1 00 00 00               je 0x140a1c204
00A1C153  4C 8B 94 24 F0 00 00 00         mov r10, qword ptr [rsp + 0xf0]
00A1C15B  49 8B 82 48 04 00 00            mov rax, qword ptr [r10 + 0x448]
00A1C162  48 85 C0                        test rax, rax
00A1C165  74 09                           je 0x140a1c170
00A1C167  4C 8B 80 58 02 00 00            mov r8, qword ptr [rax + 0x258]
00A1C16E  EB 03                           jmp 0x140a1c173
00A1C170  4C 8B C6                        mov r8, rsi
00A1C173  48 85 C0                        test rax, rax
00A1C176  74 09                           je 0x140a1c181
00A1C178  48 8B 90 48 02 00 00            mov rdx, qword ptr [rax + 0x248]
00A1C17F  EB 03                           jmp 0x140a1c184
00A1C181  48 8B D6                        mov rdx, rsi
00A1C184  48 85 C0                        test rax, rax
00A1C187  74 09                           je 0x140a1c192
00A1C189  48 8B 88 50 02 00 00            mov rcx, qword ptr [rax + 0x250]
00A1C190  EB 03                           jmp 0x140a1c195
00A1C192  48 8B CE                        mov rcx, rsi
00A1C195  48 85 C0                        test rax, rax
00A1C198  74 09                           je 0x140a1c1a3
00A1C19A  4C 8B 88 40 02 00 00            mov r9, qword ptr [rax + 0x240]
00A1C1A1  EB 03                           jmp 0x140a1c1a6
00A1C1A3  4C 8B CE                        mov r9, rsi
00A1C1A6  48 8D 84 24 14 01 00 00         lea rax, [rsp + 0x114]
00A1C1AE  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00A1C1B3  44 88 74 24 50                  mov byte ptr [rsp + 0x50], r14b
00A1C1B8  44 88 74 24 48                  mov byte ptr [rsp + 0x48], r14b
00A1C1BD  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
00A1C1C0  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A1C1C4  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00A1C1C8  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A1C1CD  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
00A1C1D2  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
00A1C1D7  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00A1C1DC  4C 8B 84 24 20 01 00 00         mov r8, qword ptr [rsp + 0x120]
00A1C1E4  49 8B 92 08 03 00 00            mov rdx, qword ptr [r10 + 0x308]
00A1C1EB  49 8B CA                        mov rcx, r10
00A1C1EE  E8 DD 29 8E FF                  call 0x1402febd0
00A1C1F3  8B F8                           mov edi, eax
00A1C1F5  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00A1C1FC  85 C0                           test eax, eax
00A1C1FE  0F 88 D7 F5 FF FF               js 0x140a1b7db
00A1C204  40 38 B4 24 EC 00 00 00         cmp byte ptr [rsp + 0xec], sil
00A1C20C  75 0E                           jne 0x140a1c21c
00A1C20E  44 39 B4 24 14 01 00 00         cmp dword ptr [rsp + 0x114], r14d
00A1C216  0F 85 91 01 00 00               jne 0x140a1c3ad
00A1C21C  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
00A1C21F  41 84 C6                        test r14b, al
00A1C222  74 1F                           je 0x140a1c243
00A1C224  41 0F BA E7 19                  bt r15d, 0x19
00A1C229  73 05                           jae 0x140a1c230
00A1C22B  41 8B DF                        mov ebx, r15d
00A1C22E  EB 0A                           jmp 0x140a1c23a
00A1C230  8B 9C 24 E4 00 00 00            mov ebx, dword ptr [rsp + 0xe4]
00A1C237  41 0B DF                        or ebx, r15d
00A1C23A  89 B4 24 10 01 00 00            mov dword ptr [rsp + 0x110], esi
00A1C241  EB 11                           jmp 0x140a1c254
00A1C243  41 8B DF                        mov ebx, r15d
00A1C246  8B 84 24 E4 00 00 00            mov eax, dword ptr [rsp + 0xe4]
00A1C24D  89 84 24 10 01 00 00            mov dword ptr [rsp + 0x110], eax
00A1C254  4C 8B 84 24 88 01 00 00         mov r8, qword ptr [rsp + 0x188]
00A1C25C  48 8B 94 24 F8 01 00 00         mov rdx, qword ptr [rsp + 0x1f8]
00A1C264  48 8B 52 20                     mov rdx, qword ptr [rdx + 0x20]
00A1C268  48 8D 8C 24 98 02 00 00         lea rcx, [rsp + 0x298]
00A1C270  E8 C3 DB AB FF                  call 0x1404d9e38
00A1C275  8B F8                           mov edi, eax
00A1C277  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00A1C27E  85 C0                           test eax, eax
00A1C280  0F 88 55 F5 FF FF               js 0x140a1b7db
00A1C286  48 8D 84 24 C9 00 00 00         lea rax, [rsp + 0xc9]
00A1C28E  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00A1C296  48 8D 84 24 C8 00 00 00         lea rax, [rsp + 0xc8]
00A1C29E  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00A1C2A6  48 8D 84 24 20 01 00 00         lea rax, [rsp + 0x120]
00A1C2AE  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00A1C2B6  48 8D 84 24 C0 02 00 00         lea rax, [rsp + 0x2c0]
00A1C2BE  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00A1C2C3  8A 84 24 A3 00 00 00            mov al, byte ptr [rsp + 0xa3]
00A1C2CA  88 44 24 70                     mov byte ptr [rsp + 0x70], al
00A1C2CE  8A 84 24 C0 03 00 00            mov al, byte ptr [rsp + 0x3c0]
00A1C2D5  88 44 24 68                     mov byte ptr [rsp + 0x68], al
00A1C2D9  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
00A1C2E1  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00A1C2E6  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
00A1C2EB  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00A1C2F3  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00A1C2F8  8A 84 24 A0 00 00 00            mov al, byte ptr [rsp + 0xa0]
00A1C2FF  88 44 24 48                     mov byte ptr [rsp + 0x48], al
00A1C303  8B 84 24 10 01 00 00            mov eax, dword ptr [rsp + 0x110]
00A1C30A  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A1C30E  48 8D 84 24 E0 02 00 00         lea rax, [rsp + 0x2e0]
00A1C316  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A1C31B  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
00A1C322  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A1C326  48 8B 84 24 B8 01 00 00         mov rax, qword ptr [rsp + 0x1b8]
00A1C32E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A1C333  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00A1C337  4C 8B 8C 24 48 01 00 00         mov r9, qword ptr [rsp + 0x148]
00A1C33F  4C 8B 84 24 58 01 00 00         mov r8, qword ptr [rsp + 0x158]
00A1C347  48 8B 94 24 90 01 00 00         mov rdx, qword ptr [rsp + 0x190]
00A1C34F  48 8D 8C 24 98 02 00 00         lea rcx, [rsp + 0x298]
00A1C357  E8 F8 4A 9B FF                  call 0x1403d0e54
00A1C35C  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
00A1C364  8B 01                           mov eax, dword ptr [rcx]
00A1C366  80 BC 24 A4 00 00 00 00         cmp byte ptr [rsp + 0xa4], 0
00A1C36E  75 09                           jne 0x140a1c379
00A1C370  89 84 24 08 01 00 00            mov dword ptr [rsp + 0x108], eax
00A1C377  EB 07                           jmp 0x140a1c380
00A1C379  21 84 24 08 01 00 00            and dword ptr [rsp + 0x108], eax
00A1C380  48 8B 8C 24 B8 01 00 00         mov rcx, qword ptr [rsp + 0x1b8]
00A1C388  48 85 C9                        test rcx, rcx
00A1C38B  74 18                           je 0x140a1c3a5
00A1C38D  44 8B 84 24 C0 00 00 00         mov r8d, dword ptr [rsp + 0xc0]
00A1C395  48 8B D1                        mov rdx, rcx
00A1C398  48 8B 8C 24 40 01 00 00         mov rcx, qword ptr [rsp + 0x140]
00A1C3A0  E8 63 B1 BE FF                  call 0x140607508
00A1C3A5  44 88 B4 24 A4 00 00 00         mov byte ptr [rsp + 0xa4], r14b
00A1C3AD  8B 84 24 70 01 00 00            mov eax, dword ptr [rsp + 0x170]
00A1C3B4  41 03 C6                        add eax, r14d
00A1C3B7  89 84 24 70 01 00 00            mov dword ptr [rsp + 0x170], eax
00A1C3BE  48 8B 8C 24 78 01 00 00         mov rcx, qword ptr [rsp + 0x178]
00A1C3C6  3B 41 3C                        cmp eax, dword ptr [rcx + 0x3c]
00A1C3C9  0F 82 56 FC FF FF               jb 0x140a1c025
00A1C3CF  8A 84 24 C8 00 00 00            mov al, byte ptr [rsp + 0xc8]
00A1C3D6  88 84 24 A1 00 00 00            mov byte ptr [rsp + 0xa1], al
00A1C3DD  8A 84 24 C9 00 00 00            mov al, byte ptr [rsp + 0xc9]
00A1C3E4  88 84 24 A2 00 00 00            mov byte ptr [rsp + 0xa2], al
00A1C3EB  8B 84 24 08 01 00 00            mov eax, dword ptr [rsp + 0x108]
00A1C3F2  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
00A1C3FA  21 01                           and dword ptr [rcx], eax
00A1C3FC  BA 22 00 00 C0                  mov edx, 0xc0000022
00A1C401  85 C0                           test eax, eax
00A1C403  75 30                           jne 0x140a1c435
00A1C405  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
00A1C40D  89 10                           mov dword ptr [rax], edx
00A1C40F  40 88 B4 24 A1 00 00 00         mov byte ptr [rsp + 0xa1], sil
00A1C417  44 88 B4 24 A2 00 00 00         mov byte ptr [rsp + 0xa2], r14b
00A1C41F  EB 14                           jmp 0x140a1c435
00A1C421  BA 22 00 00 C0                  mov edx, 0xc0000022
00A1C426  44 8B BC 24 78 03 00 00         mov r15d, dword ptr [rsp + 0x378]
00A1C42E  8B BC 24 A8 00 00 00            mov edi, dword ptr [rsp + 0xa8]
00A1C435  41 8B DF                        mov ebx, r15d
00A1C438  81 E3 00 00 00 02               and ebx, 0x2000000
00A1C43E  0F 84 82 00 00 00               je 0x140a1c4c6
00A1C444  40 38 B4 24 00 01 00 00         cmp byte ptr [rsp + 0x100], sil
00A1C44C  74 25                           je 0x140a1c473
00A1C44E  40 38 B4 24 D6 02 00 00         cmp byte ptr [rsp + 0x2d6], sil
00A1C456  75 4C                           jne 0x140a1c4a4
00A1C458  40 38 B4 24 D5 02 00 00         cmp byte ptr [rsp + 0x2d5], sil
00A1C460  75 42                           jne 0x140a1c4a4
00A1C462  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00A1C46A  E8 71 E0 A4 FF                  call 0x14046a4e0
00A1C46F  84 C0                           test al, al
00A1C471  75 31                           jne 0x140a1c4a4
00A1C473  8A 84 24 C0 03 00 00            mov al, byte ptr [rsp + 0x3c0]
00A1C47A  F6 D8                           neg al
00A1C47C  1B C9                           sbb ecx, ecx
00A1C47E  23 8C 24 28 01 00 00            and ecx, dword ptr [rsp + 0x128]
00A1C485  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
00A1C489  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00A1C48E  4D 8B CD                        mov r9, r13
00A1C491  4D 8B C4                        mov r8, r12
00A1C494  41 8B D7                        mov edx, r15d
00A1C497  48 8D 8C 24 68 02 00 00         lea rcx, [rsp + 0x268]
00A1C49F  E8 CC 37 A2 FF                  call 0x14043fc70
00A1C4A4  E8 BF 14 BB FF                  call 0x1405cd968
00A1C4A9  85 C0                           test eax, eax
00A1C4AB  0F 84 56 09 00 00               je 0x140a1ce07
00A1C4B1  8B 84 24 18 01 00 00            mov eax, dword ptr [rsp + 0x118]
00A1C4B8  F7 D0                           not eax
00A1C4BA  21 84 24 B8 00 00 00            and dword ptr [rsp + 0xb8], eax
00A1C4C1  E9 41 09 00 00                  jmp 0x140a1ce07
00A1C4C6  40 38 B4 24 00 01 00 00         cmp byte ptr [rsp + 0x100], sil
00A1C4CE  0F 84 33 09 00 00               je 0x140a1ce07
00A1C4D4  40 38 B4 24 D6 02 00 00         cmp byte ptr [rsp + 0x2d6], sil
00A1C4DC  0F 85 25 09 00 00               jne 0x140a1ce07
00A1C4E2  40 38 B4 24 D5 02 00 00         cmp byte ptr [rsp + 0x2d5], sil
00A1C4EA  0F 85 17 09 00 00               jne 0x140a1ce07
00A1C4F0  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00A1C4F8  E8 E3 DF A4 FF                  call 0x14046a4e0
00A1C4FD  84 C0                           test al, al
00A1C4FF  74 35                           je 0x140a1c536
00A1C501  39 B4 24 CC 02 00 00            cmp dword ptr [rsp + 0x2cc], esi
00A1C508  75 2C                           jne 0x140a1c536
00A1C50A  44 88 B4 24 D7 02 00 00         mov byte ptr [rsp + 0x2d7], r14b
00A1C512  44 88 B4 24 A1 00 00 00         mov byte ptr [rsp + 0xa1], r14b
00A1C51A  40 88 B4 24 A2 00 00 00         mov byte ptr [rsp + 0xa2], sil
00A1C522  44 89 BC 24 B8 00 00 00         mov dword ptr [rsp + 0xb8], r15d
00A1C52A  89 B4 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], esi
00A1C531  E9 D1 08 00 00                  jmp 0x140a1ce07
00A1C536  40 88 B4 24 A1 00 00 00         mov byte ptr [rsp + 0xa1], sil
00A1C53E  44 88 B4 24 A2 00 00 00         mov byte ptr [rsp + 0xa2], r14b
00A1C546  89 B4 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], esi
00A1C54D  89 94 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], edx
00A1C554  8A 84 24 C0 03 00 00            mov al, byte ptr [rsp + 0x3c0]
00A1C55B  84 C0                           test al, al
00A1C55D  0F 84 AB 08 00 00               je 0x140a1ce0e
00A1C563  39 B4 24 C0 00 00 00            cmp dword ptr [rsp + 0xc0], esi
00A1C56A  0F 86 9E 08 00 00               jbe 0x140a1ce0e
00A1C570  49 8B CD                        mov rcx, r13
00A1C573  49 8B D4                        mov rdx, r12
00A1C576  49 2B D5                        sub rdx, r13
00A1C579  4C 8B 84 24 F0 01 00 00         mov r8, qword ptr [rsp + 0x1f0]
00A1C581  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
00A1C588  89 04 11                        mov dword ptr [rcx + rdx], eax
00A1C58B  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
00A1C592  89 01                           mov dword ptr [rcx], eax
00A1C594  48 8D 49 04                     lea rcx, [rcx + 4]
00A1C598  4D 2B C6                        sub r8, r14
00A1C59B  75 E4                           jne 0x140a1c581
00A1C59D  E9 65 08 00 00                  jmp 0x140a1ce07
00A1C5A2  45 85 FF                        test r15d, r15d
00A1C5A5  0F 85 00 01 00 00               jne 0x140a1c6ab
00A1C5AB  45 84 E4                        test r12b, r12b
00A1C5AE  74 09                           je 0x140a1c5b9
00A1C5B0  45 84 ED                        test r13b, r13b
00A1C5B3  0F 84 F2 00 00 00               je 0x140a1c6ab
00A1C5B9  F7 83 C8 00 00 00 00 20 00 00   test dword ptr [rbx + 0xc8], 0x2000
00A1C5C3  75 0D                           jne 0x140a1c5d2
00A1C5C5  39 B4 24 EC 00 00 00            cmp dword ptr [rsp + 0xec], esi
00A1C5CC  0F 85 D9 00 00 00               jne 0x140a1c6ab
00A1C5D2  8B 84 24 E4 00 00 00            mov eax, dword ptr [rsp + 0xe4]
00A1C5D9  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
00A1C5E0  85 C0                           test eax, eax
00A1C5E2  75 0D                           jne 0x140a1c5f1
00A1C5E4  BA 22 00 00 C0                  mov edx, 0xc0000022
00A1C5E9  41 8A C6                        mov al, r14b
00A1C5EC  40 8A CE                        mov cl, sil
00A1C5EF  EB 08                           jmp 0x140a1c5f9
00A1C5F1  8B D6                           mov edx, esi
00A1C5F3  40 8A C6                        mov al, sil
00A1C5F6  41 8A CE                        mov cl, r14b
00A1C5F9  88 8C 24 A1 00 00 00            mov byte ptr [rsp + 0xa1], cl
00A1C600  88 84 24 A2 00 00 00            mov byte ptr [rsp + 0xa2], al
00A1C607  89 94 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], edx
00A1C60E  40 38 B4 24 C0 03 00 00         cmp byte ptr [rsp + 0x3c0], sil
00A1C616  74 76                           je 0x140a1c68e
00A1C618  8B 9C 24 C0 00 00 00            mov ebx, dword ptr [rsp + 0xc0]
00A1C61F  48 8D 14 DD 00 00 00 00         lea rdx, [rbx*8]
00A1C627  B9 00 01 00 00                  mov ecx, 0x100
00A1C62C  41 B8 53 65 47 61               mov r8d, 0x61476553
00A1C632  E8 B9 5A 16 00                  call 0x140b820f0
00A1C637  4C 8B E0                        mov r12, rax
00A1C63A  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
00A1C642  48 85 C0                        test rax, rax
00A1C645  0F 84 32 F7 FF FF               je 0x140a1bd7d
00A1C64B  44 88 B4 24 AE 00 00 00         mov byte ptr [rsp + 0xae], r14b
00A1C653  4C 8D 2C 98                     lea r13, [rax + rbx*4]
00A1C657  39 B4 24 C0 00 00 00            cmp dword ptr [rsp + 0xc0], esi
00A1C65E  0F 86 0F 08 00 00               jbe 0x140a1ce73
00A1C664  49 8B CD                        mov rcx, r13
00A1C667  48 8B D0                        mov rdx, rax
00A1C66A  49 2B D5                        sub rdx, r13
00A1C66D  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
00A1C674  89 04 11                        mov dword ptr [rcx + rdx], eax
00A1C677  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
00A1C67E  89 01                           mov dword ptr [rcx], eax
00A1C680  48 8D 49 04                     lea rcx, [rcx + 4]
00A1C684  49 2B DE                        sub rbx, r14
00A1C687  75 E4                           jne 0x140a1c66d
00A1C689  E9 E5 07 00 00                  jmp 0x140a1ce73
00A1C68E  4C 8D A4 24 B8 00 00 00         lea r12, [rsp + 0xb8]
00A1C696  4C 89 A4 24 30 01 00 00         mov qword ptr [rsp + 0x130], r12
00A1C69E  4C 8D AC 24 B0 00 00 00         lea r13, [rsp + 0xb0]
00A1C6A6  E9 C8 07 00 00                  jmp 0x140a1ce73
00A1C6AB  8B BC 24 68 01 00 00            mov edi, dword ptr [rsp + 0x168]
00A1C6B2  48 89 BC 24 F0 01 00 00         mov qword ptr [rsp + 0x1f0], rdi
00A1C6BA  48 8D 1C FD 00 00 00 00         lea rbx, [rdi*8]
00A1C6C2  40 38 B4 24 C0 03 00 00         cmp byte ptr [rsp + 0x3c0], sil
00A1C6CA  74 35                           je 0x140a1c701
00A1C6CC  41 B8 53 65 47 61               mov r8d, 0x61476553
00A1C6D2  48 8B D3                        mov rdx, rbx
00A1C6D5  B9 00 01 00 00                  mov ecx, 0x100
00A1C6DA  E8 11 5A 16 00                  call 0x140b820f0
00A1C6DF  4C 8B E0                        mov r12, rax
00A1C6E2  48 89 84 24 30 01 00 00         mov qword ptr [rsp + 0x130], rax
00A1C6EA  48 85 C0                        test rax, rax
00A1C6ED  0F 84 8A F6 FF FF               je 0x140a1bd7d
00A1C6F3  44 88 B4 24 AE 00 00 00         mov byte ptr [rsp + 0xae], r14b
00A1C6FB  4C 8D 2C B8                     lea r13, [rax + rdi*4]
00A1C6FF  EB 18                           jmp 0x140a1c719
00A1C701  4C 8D A4 24 B8 00 00 00         lea r12, [rsp + 0xb8]
00A1C709  4C 89 A4 24 30 01 00 00         mov qword ptr [rsp + 0x130], r12
00A1C711  4C 8D AC 24 B0 00 00 00         lea r13, [rsp + 0xb0]
00A1C719  8B 84 24 EC 00 00 00            mov eax, dword ptr [rsp + 0xec]
00A1C720  89 84 24 C0 02 00 00            mov dword ptr [rsp + 0x2c0], eax
00A1C727  48 8D 84 24 A2 00 00 00         lea rax, [rsp + 0xa2]
00A1C72F  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00A1C737  48 8D 84 24 A1 00 00 00         lea rax, [rsp + 0xa1]
00A1C73F  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00A1C747  48 8D 84 24 20 01 00 00         lea rax, [rsp + 0x120]
00A1C74F  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00A1C757  48 8D 84 24 C0 02 00 00         lea rax, [rsp + 0x2c0]
00A1C75F  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00A1C764  8A 84 24 A3 00 00 00            mov al, byte ptr [rsp + 0xa3]
00A1C76B  88 44 24 70                     mov byte ptr [rsp + 0x70], al
00A1C76F  8A 84 24 C0 03 00 00            mov al, byte ptr [rsp + 0x3c0]
00A1C776  88 44 24 68                     mov byte ptr [rsp + 0x68], al
00A1C77A  4C 89 6C 24 60                  mov qword ptr [rsp + 0x60], r13
00A1C77F  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
00A1C784  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
00A1C789  8A 84 24 A0 00 00 00            mov al, byte ptr [rsp + 0xa0]
00A1C790  88 44 24 48                     mov byte ptr [rsp + 0x48], al
00A1C794  8B 84 24 E4 00 00 00            mov eax, dword ptr [rsp + 0xe4]
00A1C79B  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A1C79F  48 8D 84 24 E0 02 00 00         lea rax, [rsp + 0x2e0]
00A1C7A7  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A1C7AC  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
00A1C7B3  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A1C7B7  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
00A1C7BF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A1C7C4  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
00A1C7C9  4C 8B 8C 24 F0 00 00 00         mov r9, qword ptr [rsp + 0xf0]
00A1C7D1  4C 8B 84 24 58 01 00 00         mov r8, qword ptr [rsp + 0x158]
00A1C7D9  48 8B 94 24 90 01 00 00         mov rdx, qword ptr [rsp + 0x190]
00A1C7E1  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
00A1C7E9  E8 66 46 9B FF                  call 0x1403d0e54
00A1C7EE  8A 05 D1 82 4E 00               mov al, byte ptr [rip + 0x4e82d1]
00A1C7F4  84 C0                           test al, al
00A1C7F6  0F 84 D8 04 00 00               je 0x140a1ccd4
00A1C7FC  41 39 75 00                     cmp dword ptr [r13], esi
00A1C800  0F 8C CE 04 00 00               jl 0x140a1ccd4
00A1C806  40 38 B4 24 A5 00 00 00         cmp byte ptr [rsp + 0xa5], sil
00A1C80E  0F 84 C0 04 00 00               je 0x140a1ccd4
00A1C814  40 38 B4 24 C0 03 00 00         cmp byte ptr [rsp + 0x3c0], sil
00A1C81C  74 35                           je 0x140a1c853
00A1C81E  41 B8 53 65 47 61               mov r8d, 0x61476553
00A1C824  48 8B D3                        mov rdx, rbx
00A1C827  B9 00 01 00 00                  mov ecx, 0x100
00A1C82C  E8 BF 58 16 00                  call 0x140b820f0
00A1C831  48 8B D8                        mov rbx, rax
00A1C834  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
00A1C83C  48 85 C0                        test rax, rax
00A1C83F  0F 84 28 F7 FF FF               je 0x140a1bf6d
00A1C845  48 8D 0C B8                     lea rcx, [rax + rdi*4]
00A1C849  48 89 8C 24 38 01 00 00         mov qword ptr [rsp + 0x138], rcx
00A1C851  EB 20                           jmp 0x140a1c873
00A1C853  48 8D 84 24 C8 01 00 00         lea rax, [rsp + 0x1c8]
00A1C85B  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
00A1C863  48 8D 84 24 CC 01 00 00         lea rax, [rsp + 0x1cc]
00A1C86B  48 89 84 24 38 01 00 00         mov qword ptr [rsp + 0x138], rax
00A1C873  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
00A1C87A  85 C0                           test eax, eax
00A1C87C  74 29                           je 0x140a1c8a7
00A1C87E  4C 8D 84 24 B8 01 00 00         lea r8, [rsp + 0x1b8]
00A1C886  8B D0                           mov edx, eax
00A1C888  48 8B 8C 24 40 01 00 00         mov rcx, qword ptr [rsp + 0x140]
00A1C890  E8 2B A4 BE FF                  call 0x140606cc0
00A1C895  8B F8                           mov edi, eax
00A1C897  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00A1C89E  85 C0                           test eax, eax
00A1C8A0  79 0C                           jns 0x140a1c8ae
00A1C8A2  E9 34 EF FF FF                  jmp 0x140a1b7db
00A1C8A7  8B BC 24 A8 00 00 00            mov edi, dword ptr [rsp + 0xa8]
00A1C8AE  40 88 B4 24 18 01 00 00         mov byte ptr [rsp + 0x118], sil
00A1C8B6  8B C6                           mov eax, esi
00A1C8B8  89 84 24 10 01 00 00            mov dword ptr [rsp + 0x110], eax
00A1C8BF  48 8B 8C 24 78 01 00 00         mov rcx, qword ptr [rsp + 0x178]
00A1C8C7  44 8B BC 24 78 03 00 00         mov r15d, dword ptr [rsp + 0x378]
00A1C8CF  39 71 3C                        cmp dword ptr [rcx + 0x3c], esi
00A1C8D2  0F 86 AA 03 00 00               jbe 0x140a1cc82
00A1C8D8  8B C8                           mov ecx, eax
00A1C8DA  48 8B 84 24 78 01 00 00         mov rax, qword ptr [rsp + 0x178]
00A1C8E2  48 8B 5C C8 40                  mov rbx, qword ptr [rax + rcx*8 + 0x40]
00A1C8E7  48 89 9C 24 F8 01 00 00         mov qword ptr [rsp + 0x1f8], rbx
00A1C8EF  48 39 73 18                     cmp qword ptr [rbx + 0x18], rsi
00A1C8F3  0F 84 D6 01 00 00               je 0x140a1cacf
00A1C8F9  4C 8B 84 24 20 01 00 00         mov r8, qword ptr [rsp + 0x120]
00A1C901  4D 85 C0                        test r8, r8
00A1C904  75 34                           jne 0x140a1c93a
00A1C906  48 8D 94 24 20 01 00 00         lea rdx, [rsp + 0x120]
00A1C90E  48 8B 8C 24 88 01 00 00         mov rcx, qword ptr [rsp + 0x188]
00A1C916  E8 69 65 8E FF                  call 0x140302e84
00A1C91B  8B 94 24 18 01 00 00            mov edx, dword ptr [rsp + 0x118]
00A1C922  0F B6 D2                        movzx edx, dl
00A1C925  85 C0                           test eax, eax
00A1C927  41 0F 48 D6                     cmovs edx, r14d
00A1C92B  89 94 24 18 01 00 00            mov dword ptr [rsp + 0x118], edx
00A1C932  4C 8B 84 24 20 01 00 00         mov r8, qword ptr [rsp + 0x120]
00A1C93A  4C 8B 9C 24 F0 00 00 00         mov r11, qword ptr [rsp + 0xf0]
00A1C942  49 8B 83 48 04 00 00            mov rax, qword ptr [r11 + 0x448]
00A1C949  48 85 C0                        test rax, rax
00A1C94C  74 09                           je 0x140a1c957
00A1C94E  4C 8B 90 58 02 00 00            mov r10, qword ptr [rax + 0x258]
00A1C955  EB 03                           jmp 0x140a1c95a
00A1C957  4C 8B D6                        mov r10, rsi
00A1C95A  48 85 C0                        test rax, rax
00A1C95D  74 09                           je 0x140a1c968
00A1C95F  48 8B 90 48 02 00 00            mov rdx, qword ptr [rax + 0x248]
00A1C966  EB 03                           jmp 0x140a1c96b
00A1C968  48 8B D6                        mov rdx, rsi
00A1C96B  48 85 C0                        test rax, rax
00A1C96E  74 09                           je 0x140a1c979
00A1C970  48 8B 88 50 02 00 00            mov rcx, qword ptr [rax + 0x250]
00A1C977  EB 03                           jmp 0x140a1c97c
00A1C979  48 8B CE                        mov rcx, rsi
00A1C97C  48 85 C0                        test rax, rax
00A1C97F  74 09                           je 0x140a1c98a
00A1C981  4C 8B 88 40 02 00 00            mov r9, qword ptr [rax + 0x240]
00A1C988  EB 03                           jmp 0x140a1c98d
00A1C98A  4C 8B CE                        mov r9, rsi
00A1C98D  48 8D 84 24 14 01 00 00         lea rax, [rsp + 0x114]
00A1C995  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00A1C99A  40 88 74 24 50                  mov byte ptr [rsp + 0x50], sil
00A1C99F  44 88 74 24 48                  mov byte ptr [rsp + 0x48], r14b
00A1C9A4  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
00A1C9A7  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A1C9AB  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00A1C9AF  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A1C9B4  4C 89 54 24 30                  mov qword ptr [rsp + 0x30], r10
00A1C9B9  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
00A1C9BE  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00A1C9C3  49 8B 93 08 03 00 00            mov rdx, qword ptr [r11 + 0x308]
00A1C9CA  49 8B CB                        mov rcx, r11
00A1C9CD  E8 FE 21 8E FF                  call 0x1402febd0
00A1C9D2  8B F8                           mov edi, eax
00A1C9D4  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00A1C9DB  44 39 B4 24 14 01 00 00         cmp dword ptr [rsp + 0x114], r14d
00A1C9E3  0F 84 E6 00 00 00               je 0x140a1cacf
00A1C9E9  85 C0                           test eax, eax
00A1C9EB  0F 88 EA ED FF FF               js 0x140a1b7db
00A1C9F1  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00A1C9F9  E8 E2 C2 A1 FF                  call 0x140438ce0
00A1C9FE  84 C0                           test al, al
00A1CA00  0F 84 B1 00 00 00               je 0x140a1cab7
00A1CA06  4C 8B 94 24 F0 00 00 00         mov r10, qword ptr [rsp + 0xf0]
00A1CA0E  49 8B 82 48 04 00 00            mov rax, qword ptr [r10 + 0x448]
00A1CA15  48 85 C0                        test rax, rax
00A1CA18  74 09                           je 0x140a1ca23
00A1CA1A  4C 8B 80 58 02 00 00            mov r8, qword ptr [rax + 0x258]
00A1CA21  EB 03                           jmp 0x140a1ca26
00A1CA23  4C 8B C6                        mov r8, rsi
00A1CA26  48 85 C0                        test rax, rax
00A1CA29  74 09                           je 0x140a1ca34
00A1CA2B  48 8B 90 48 02 00 00            mov rdx, qword ptr [rax + 0x248]
00A1CA32  EB 03                           jmp 0x140a1ca37
00A1CA34  48 8B D6                        mov rdx, rsi
00A1CA37  48 85 C0                        test rax, rax
00A1CA3A  74 09                           je 0x140a1ca45
00A1CA3C  48 8B 88 50 02 00 00            mov rcx, qword ptr [rax + 0x250]
00A1CA43  EB 03                           jmp 0x140a1ca48
00A1CA45  48 8B CE                        mov rcx, rsi
00A1CA48  48 85 C0                        test rax, rax
00A1CA4B  74 09                           je 0x140a1ca56
00A1CA4D  4C 8B 88 40 02 00 00            mov r9, qword ptr [rax + 0x240]
00A1CA54  EB 03                           jmp 0x140a1ca59
00A1CA56  4C 8B CE                        mov r9, rsi
00A1CA59  48 8D 84 24 14 01 00 00         lea rax, [rsp + 0x114]
00A1CA61  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00A1CA66  44 88 74 24 50                  mov byte ptr [rsp + 0x50], r14b
00A1CA6B  44 88 74 24 48                  mov byte ptr [rsp + 0x48], r14b
00A1CA70  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
00A1CA73  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A1CA77  48 8B 43 18                     mov rax, qword ptr [rbx + 0x18]
00A1CA7B  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A1CA80  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
00A1CA85  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
00A1CA8A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00A1CA8F  4C 8B 84 24 20 01 00 00         mov r8, qword ptr [rsp + 0x120]
00A1CA97  49 8B 92 08 03 00 00            mov rdx, qword ptr [r10 + 0x308]
00A1CA9E  49 8B CA                        mov rcx, r10
00A1CAA1  E8 2A 21 8E FF                  call 0x1402febd0
00A1CAA6  8B F8                           mov edi, eax
00A1CAA8  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00A1CAAF  85 C0                           test eax, eax
00A1CAB1  0F 88 24 ED FF FF               js 0x140a1b7db
00A1CAB7  40 38 B4 24 18 01 00 00         cmp byte ptr [rsp + 0x118], sil
00A1CABF  75 0E                           jne 0x140a1cacf
00A1CAC1  44 39 B4 24 14 01 00 00         cmp dword ptr [rsp + 0x114], r14d
00A1CAC9  0F 85 91 01 00 00               jne 0x140a1cc60
00A1CACF  8B 43 30                        mov eax, dword ptr [rbx + 0x30]
00A1CAD2  41 84 C6                        test r14b, al
00A1CAD5  74 1F                           je 0x140a1caf6
00A1CAD7  41 0F BA E7 19                  bt r15d, 0x19
00A1CADC  73 05                           jae 0x140a1cae3
00A1CADE  41 8B DF                        mov ebx, r15d
00A1CAE1  EB 0A                           jmp 0x140a1caed
00A1CAE3  8B 9C 24 E4 00 00 00            mov ebx, dword ptr [rsp + 0xe4]
00A1CAEA  41 0B DF                        or ebx, r15d
00A1CAED  89 B4 24 68 01 00 00            mov dword ptr [rsp + 0x168], esi
00A1CAF4  EB 11                           jmp 0x140a1cb07
00A1CAF6  41 8B DF                        mov ebx, r15d
00A1CAF9  8B 84 24 E4 00 00 00            mov eax, dword ptr [rsp + 0xe4]
00A1CB00  89 84 24 68 01 00 00            mov dword ptr [rsp + 0x168], eax
00A1CB07  4C 8B 84 24 88 01 00 00         mov r8, qword ptr [rsp + 0x188]
00A1CB0F  48 8B 94 24 F8 01 00 00         mov rdx, qword ptr [rsp + 0x1f8]
00A1CB17  48 8B 52 20                     mov rdx, qword ptr [rdx + 0x20]
00A1CB1B  48 8D 8C 24 98 02 00 00         lea rcx, [rsp + 0x298]
00A1CB23  E8 10 D3 AB FF                  call 0x1404d9e38
00A1CB28  8B F8                           mov edi, eax
00A1CB2A  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00A1CB31  85 C0                           test eax, eax
00A1CB33  0F 88 A2 EC FF FF               js 0x140a1b7db
00A1CB39  48 8D 84 24 C9 00 00 00         lea rax, [rsp + 0xc9]
00A1CB41  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00A1CB49  48 8D 84 24 C8 00 00 00         lea rax, [rsp + 0xc8]
00A1CB51  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00A1CB59  48 8D 84 24 20 01 00 00         lea rax, [rsp + 0x120]
00A1CB61  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00A1CB69  48 8D 84 24 C0 02 00 00         lea rax, [rsp + 0x2c0]
00A1CB71  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00A1CB76  8A 84 24 A3 00 00 00            mov al, byte ptr [rsp + 0xa3]
00A1CB7D  88 44 24 70                     mov byte ptr [rsp + 0x70], al
00A1CB81  8A 84 24 C0 03 00 00            mov al, byte ptr [rsp + 0x3c0]
00A1CB88  88 44 24 68                     mov byte ptr [rsp + 0x68], al
00A1CB8C  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
00A1CB94  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00A1CB99  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
00A1CB9E  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00A1CBA6  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00A1CBAB  8A 84 24 A0 00 00 00            mov al, byte ptr [rsp + 0xa0]
00A1CBB2  88 44 24 48                     mov byte ptr [rsp + 0x48], al
00A1CBB6  8B 84 24 68 01 00 00            mov eax, dword ptr [rsp + 0x168]
00A1CBBD  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A1CBC1  48 8D 84 24 E0 02 00 00         lea rax, [rsp + 0x2e0]
00A1CBC9  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A1CBCE  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
00A1CBD5  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00A1CBD9  48 8B 84 24 B8 01 00 00         mov rax, qword ptr [rsp + 0x1b8]
00A1CBE1  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A1CBE6  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
00A1CBEA  4C 8B 8C 24 48 01 00 00         mov r9, qword ptr [rsp + 0x148]
00A1CBF2  4C 8B 84 24 58 01 00 00         mov r8, qword ptr [rsp + 0x158]
00A1CBFA  48 8B 94 24 90 01 00 00         mov rdx, qword ptr [rsp + 0x190]
00A1CC02  48 8D 8C 24 98 02 00 00         lea rcx, [rsp + 0x298]
00A1CC0A  E8 45 42 9B FF                  call 0x1403d0e54
00A1CC0F  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
00A1CC17  8B 01                           mov eax, dword ptr [rcx]
00A1CC19  80 BC 24 A4 00 00 00 00         cmp byte ptr [rsp + 0xa4], 0
00A1CC21  75 09                           jne 0x140a1cc2c
00A1CC23  89 84 24 08 01 00 00            mov dword ptr [rsp + 0x108], eax
00A1CC2A  EB 07                           jmp 0x140a1cc33
00A1CC2C  21 84 24 08 01 00 00            and dword ptr [rsp + 0x108], eax
00A1CC33  48 8B 8C 24 B8 01 00 00         mov rcx, qword ptr [rsp + 0x1b8]
00A1CC3B  48 85 C9                        test rcx, rcx
00A1CC3E  74 18                           je 0x140a1cc58
00A1CC40  44 8B 84 24 C0 00 00 00         mov r8d, dword ptr [rsp + 0xc0]
00A1CC48  48 8B D1                        mov rdx, rcx
00A1CC4B  48 8B 8C 24 40 01 00 00         mov rcx, qword ptr [rsp + 0x140]
00A1CC53  E8 B0 A8 BE FF                  call 0x140607508
00A1CC58  44 88 B4 24 A4 00 00 00         mov byte ptr [rsp + 0xa4], r14b
00A1CC60  8B 84 24 10 01 00 00            mov eax, dword ptr [rsp + 0x110]
00A1CC67  41 03 C6                        add eax, r14d
00A1CC6A  89 84 24 10 01 00 00            mov dword ptr [rsp + 0x110], eax
00A1CC71  48 8B 8C 24 78 01 00 00         mov rcx, qword ptr [rsp + 0x178]
00A1CC79  3B 41 3C                        cmp eax, dword ptr [rcx + 0x3c]
00A1CC7C  0F 82 56 FC FF FF               jb 0x140a1c8d8
00A1CC82  8A 84 24 C8 00 00 00            mov al, byte ptr [rsp + 0xc8]
00A1CC89  88 84 24 A1 00 00 00            mov byte ptr [rsp + 0xa1], al
00A1CC90  8A 84 24 C9 00 00 00            mov al, byte ptr [rsp + 0xc9]
00A1CC97  88 84 24 A2 00 00 00            mov byte ptr [rsp + 0xa2], al
00A1CC9E  8B 84 24 08 01 00 00            mov eax, dword ptr [rsp + 0x108]
00A1CCA5  48 8B 8C 24 D0 00 00 00         mov rcx, qword ptr [rsp + 0xd0]
00A1CCAD  21 01                           and dword ptr [rcx], eax
00A1CCAF  BA 22 00 00 C0                  mov edx, 0xc0000022
00A1CCB4  85 C0                           test eax, eax
00A1CCB6  75 30                           jne 0x140a1cce8
00A1CCB8  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
00A1CCC0  89 10                           mov dword ptr [rax], edx
00A1CCC2  40 88 B4 24 A1 00 00 00         mov byte ptr [rsp + 0xa1], sil
00A1CCCA  44 88 B4 24 A2 00 00 00         mov byte ptr [rsp + 0xa2], r14b
00A1CCD2  EB 14                           jmp 0x140a1cce8
00A1CCD4  BA 22 00 00 C0                  mov edx, 0xc0000022
00A1CCD9  44 8B BC 24 78 03 00 00         mov r15d, dword ptr [rsp + 0x378]
00A1CCE1  8B BC 24 A8 00 00 00            mov edi, dword ptr [rsp + 0xa8]
00A1CCE8  41 8B DF                        mov ebx, r15d
00A1CCEB  81 E3 00 00 00 02               and ebx, 0x2000000
00A1CCF1  74 71                           je 0x140a1cd64
00A1CCF3  40 38 B4 24 00 01 00 00         cmp byte ptr [rsp + 0x100], sil
00A1CCFB  74 31                           je 0x140a1cd2e
00A1CCFD  40 38 B4 24 D6 02 00 00         cmp byte ptr [rsp + 0x2d6], sil
00A1CD05  0F 85 FC 00 00 00               jne 0x140a1ce07
00A1CD0B  40 38 B4 24 D5 02 00 00         cmp byte ptr [rsp + 0x2d5], sil
00A1CD13  0F 85 EE 00 00 00               jne 0x140a1ce07
00A1CD19  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00A1CD21  E8 BA D7 A4 FF                  call 0x14046a4e0
00A1CD26  84 C0                           test al, al
00A1CD28  0F 85 D9 00 00 00               jne 0x140a1ce07
00A1CD2E  8A 84 24 C0 03 00 00            mov al, byte ptr [rsp + 0x3c0]
00A1CD35  F6 D8                           neg al
00A1CD37  1B C9                           sbb ecx, ecx
00A1CD39  23 8C 24 28 01 00 00            and ecx, dword ptr [rsp + 0x128]
00A1CD40  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
00A1CD44  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00A1CD49  4D 8B CD                        mov r9, r13
00A1CD4C  4D 8B C4                        mov r8, r12
00A1CD4F  41 8B D7                        mov edx, r15d
00A1CD52  48 8D 8C 24 68 02 00 00         lea rcx, [rsp + 0x268]
00A1CD5A  E8 11 2F A2 FF                  call 0x14043fc70
00A1CD5F  E9 A3 00 00 00                  jmp 0x140a1ce07
00A1CD64  40 38 B4 24 00 01 00 00         cmp byte ptr [rsp + 0x100], sil
00A1CD6C  0F 84 95 00 00 00               je 0x140a1ce07
00A1CD72  40 38 B4 24 D6 02 00 00         cmp byte ptr [rsp + 0x2d6], sil
00A1CD7A  0F 85 87 00 00 00               jne 0x140a1ce07
00A1CD80  40 38 B4 24 D5 02 00 00         cmp byte ptr [rsp + 0x2d5], sil
00A1CD88  75 7D                           jne 0x140a1ce07
00A1CD8A  48 8B 8C 24 F0 00 00 00         mov rcx, qword ptr [rsp + 0xf0]
00A1CD92  E8 49 D7 A4 FF                  call 0x14046a4e0
00A1CD97  84 C0                           test al, al
00A1CD99  74 0D                           je 0x140a1cda8
00A1CD9B  39 B4 24 CC 02 00 00            cmp dword ptr [rsp + 0x2cc], esi
00A1CDA2  0F 84 62 F7 FF FF               je 0x140a1c50a
00A1CDA8  40 88 B4 24 A1 00 00 00         mov byte ptr [rsp + 0xa1], sil
00A1CDB0  44 88 B4 24 A2 00 00 00         mov byte ptr [rsp + 0xa2], r14b
00A1CDB8  89 B4 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], esi
00A1CDBF  89 94 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], edx
00A1CDC6  8A 84 24 C0 03 00 00            mov al, byte ptr [rsp + 0x3c0]
00A1CDCD  84 C0                           test al, al
00A1CDCF  74 3D                           je 0x140a1ce0e
00A1CDD1  39 B4 24 C0 00 00 00            cmp dword ptr [rsp + 0xc0], esi
00A1CDD8  76 34                           jbe 0x140a1ce0e
00A1CDDA  49 8B CD                        mov rcx, r13
00A1CDDD  49 8B D4                        mov rdx, r12
00A1CDE0  49 2B D5                        sub rdx, r13
00A1CDE3  4C 8B 84 24 F0 01 00 00         mov r8, qword ptr [rsp + 0x1f0]
00A1CDEB  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
00A1CDF2  89 04 11                        mov dword ptr [rcx + rdx], eax
00A1CDF5  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
00A1CDFC  89 01                           mov dword ptr [rcx], eax
00A1CDFE  48 8D 49 04                     lea rcx, [rcx + 4]
00A1CE02  4D 2B C6                        sub r8, r14
00A1CE05  75 E4                           jne 0x140a1cdeb
00A1CE07  8A 84 24 C0 03 00 00            mov al, byte ptr [rsp + 0x3c0]
00A1CE0E  85 DB                           test ebx, ebx
00A1CE10  74 61                           je 0x140a1ce73
00A1CE12  F6 D8                           neg al
00A1CE14  48 8D 84 24 B4 00 00 00         lea rax, [rsp + 0xb4]
00A1CE1C  1B DB                           sbb ebx, ebx
00A1CE1E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A1CE23  23 9C 24 28 01 00 00            and ebx, dword ptr [rsp + 0x128]
00A1CE2A  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
00A1CE2E  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00A1CE33  4D 8B CD                        mov r9, r13
00A1CE36  4D 8B C4                        mov r8, r12
00A1CE39  41 8B D7                        mov edx, r15d
00A1CE3C  8B 8C 24 98 01 00 00            mov ecx, dword ptr [rsp + 0x198]
00A1CE43  E8 98 2F A2 FF                  call 0x14043fde0
00A1CE48  48 8D 94 24 B5 00 00 00         lea rdx, [rsp + 0xb5]
00A1CE50  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
00A1CE55  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
00A1CE59  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00A1CE5E  4D 8B CD                        mov r9, r13
00A1CE61  4D 8B C4                        mov r8, r12
00A1CE64  41 8B D7                        mov edx, r15d
00A1CE67  8B 8C 24 D8 01 00 00            mov ecx, dword ptr [rsp + 0x1d8]
00A1CE6E  E8 6D 2F A2 FF                  call 0x14043fde0
00A1CE73  48 8B 9C 24 F0 00 00 00         mov rbx, qword ptr [rsp + 0xf0]
00A1CE7B  48 85 DB                        test rbx, rbx
00A1CE7E  0F 84 18 01 00 00               je 0x140a1cf9c
00A1CE84  40 38 B4 24 B4 00 00 00         cmp byte ptr [rsp + 0xb4], sil
00A1CE8C  75 46                           jne 0x140a1ced4
00A1CE8E  40 38 B4 24 B5 00 00 00         cmp byte ptr [rsp + 0xb5], sil
00A1CE96  75 3C                           jne 0x140a1ced4
00A1CE98  39 B4 24 CC 02 00 00            cmp dword ptr [rsp + 0x2cc], esi
00A1CE9F  0F 85 BC 00 00 00               jne 0x140a1cf61
00A1CEA5  F7 83 C8 00 00 00 00 40 00 00   test dword ptr [rbx + 0xc8], 0x4000
00A1CEAF  0F 84 AC 00 00 00               je 0x140a1cf61
00A1CEB5  85 FF                           test edi, edi
00A1CEB7  0F 88 DF 00 00 00               js 0x140a1cf9c
00A1CEBD  39 B4 24 B0 00 00 00            cmp dword ptr [rsp + 0xb0], esi
00A1CEC4  7C 0E                           jl 0x140a1ced4
00A1CEC6  40 38 B4 24 D7 02 00 00         cmp byte ptr [rsp + 0x2d7], sil
00A1CECE  0F 84 8D 00 00 00               je 0x140a1cf61
00A1CED4  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A1CEDD  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00A1CEE4  90                              nop
00A1CEE5  41 8A D6                        mov dl, r14b
00A1CEE8  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00A1CEEC  E8 CF 4C 7F FF                  call 0x140211bc0
00A1CEF1  39 B4 24 B0 00 00 00            cmp dword ptr [rsp + 0xb0], esi
00A1CEF8  0F 9D C3                        setge bl
00A1CEFB  8B BC 24 E4 00 00 00            mov edi, dword ptr [rsp + 0xe4]
00A1CF02  44 8B BC 24 78 03 00 00         mov r15d, dword ptr [rsp + 0x378]
00A1CF0A  41 0B FF                        or edi, r15d
00A1CF0D  48 8D 8C 24 48 01 00 00         lea rcx, [rsp + 0x148]
00A1CF15  E8 26 0B 9D FF                  call 0x1403eda40
00A1CF1A  4C 8B C8                        mov r9, rax
00A1CF1D  40 88 74 24 38                  mov byte ptr [rsp + 0x38], sil
00A1CF22  88 5C 24 30                     mov byte ptr [rsp + 0x30], bl
00A1CF26  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
00A1CF2A  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00A1CF32  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A1CF37  45 33 C0                        xor r8d, r8d
00A1CF3A  33 D2                           xor edx, edx
00A1CF3C  48 8B 9C 24 F0 00 00 00         mov rbx, qword ptr [rsp + 0xf0]
00A1CF44  48 8B CB                        mov rcx, rbx
00A1CF47  E8 04 B6 A2 FF                  call 0x140448550
00A1CF4C  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00A1CF50  E8 BB 2A 84 FF                  call 0x14025fa10
00A1CF55  E8 56 09 84 FF                  call 0x14025d8b0
00A1CF5A  8B BC 24 A8 00 00 00            mov edi, dword ptr [rsp + 0xa8]
00A1CF61  85 FF                           test edi, edi
00A1CF63  78 37                           js 0x140a1cf9c
00A1CF65  39 B4 24 B0 00 00 00            cmp dword ptr [rsp + 0xb0], esi
00A1CF6C  7D 2E                           jge 0x140a1cf9c
00A1CF6E  39 B4 24 CC 02 00 00            cmp dword ptr [rsp + 0x2cc], esi
00A1CF75  75 25                           jne 0x140a1cf9c
00A1CF77  F7 83 C8 00 00 00 00 40 00 00   test dword ptr [rbx + 0xc8], 0x4000
00A1CF81  74 19                           je 0x140a1cf9c
00A1CF83  41 8B D7                        mov edx, r15d
00A1CF86  48 8D 8C 24 C0 02 00 00         lea rcx, [rsp + 0x2c0]
00A1CF8E  E8 F1 54 A4 FF                  call 0x140462484
00A1CF93  84 C0                           test al, al
00A1CF95  74 05                           je 0x140a1cf9c
00A1CF97  E8 04 19 A0 FF                  call 0x14041e8a0
00A1CF9C  40 38 B4 24 05 01 00 00         cmp byte ptr [rsp + 0x105], sil
00A1CFA4  0F 85 92 05 00 00               jne 0x140a1d53c
00A1CFAA  8A 8C 24 A1 00 00 00            mov cl, byte ptr [rsp + 0xa1]
00A1CFB1  83 BC 24 6C 01 00 00 02         cmp dword ptr [rsp + 0x16c], 2
00A1CFB9  0F 85 8D 00 00 00               jne 0x140a1d04c
00A1CFBF  84 C9                           test cl, cl
00A1CFC1  74 3B                           je 0x140a1cffe
00A1CFC3  48 8D 84 24 E8 00 00 00         lea rax, [rsp + 0xe8]
00A1CFCB  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A1CFD0  40 88 74 24 28                  mov byte ptr [rsp + 0x28], sil
00A1CFD5  48 8D 84 24 48 01 00 00         lea rax, [rsp + 0x148]
00A1CFDD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A1CFE2  45 33 C9                        xor r9d, r9d
00A1CFE5  44 8A C1                        mov r8b, cl
00A1CFE8  48 8B 94 24 B0 01 00 00         mov rdx, qword ptr [rsp + 0x1b0]
00A1CFF0  33 C9                           xor ecx, ecx
00A1CFF2  E8 F9 1E E5 FF                  call 0x14086eef0
00A1CFF7  88 84 24 AD 00 00 00            mov byte ptr [rsp + 0xad], al
00A1CFFE  44 8A 84 24 A2 00 00 00         mov r8b, byte ptr [rsp + 0xa2]
00A1D006  45 84 C0                        test r8b, r8b
00A1D009  0F 84 91 00 00 00               je 0x140a1d0a0
00A1D00F  48 8D 84 24 E8 00 00 00         lea rax, [rsp + 0xe8]
00A1D017  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A1D01C  40 88 74 24 28                  mov byte ptr [rsp + 0x28], sil
00A1D021  48 8D 84 24 48 01 00 00         lea rax, [rsp + 0x148]
00A1D029  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A1D02E  45 8A C8                        mov r9b, r8b
00A1D031  45 33 C0                        xor r8d, r8d
00A1D034  48 8B 94 24 B0 01 00 00         mov rdx, qword ptr [rsp + 0x1b0]
00A1D03C  33 C9                           xor ecx, ecx
00A1D03E  E8 AD 1E E5 FF                  call 0x14086eef0
00A1D043  88 84 24 AC 00 00 00            mov byte ptr [rsp + 0xac], al
00A1D04A  EB 5B                           jmp 0x140a1d0a7
00A1D04C  BB 98 00 00 00                  mov ebx, 0x98
00A1D051  84 C9                           test cl, cl
00A1D053  74 23                           je 0x140a1d078
00A1D055  66 89 9C 24 E8 00 00 00         mov word ptr [rsp + 0xe8], bx
00A1D05D  4C 8D 8C 24 48 01 00 00         lea r9, [rsp + 0x148]
00A1D065  45 33 C0                        xor r8d, r8d
00A1D068  8A D1                           mov dl, cl
00A1D06A  8B CB                           mov ecx, ebx
00A1D06C  E8 4F 3A E5 FF                  call 0x140870ac0
00A1D071  88 84 24 AD 00 00 00            mov byte ptr [rsp + 0xad], al
00A1D078  44 8A 84 24 A2 00 00 00         mov r8b, byte ptr [rsp + 0xa2]
00A1D080  45 84 C0                        test r8b, r8b
00A1D083  74 1B                           je 0x140a1d0a0
00A1D085  66 89 9C 24 E8 00 00 00         mov word ptr [rsp + 0xe8], bx
00A1D08D  4C 8D 8C 24 48 01 00 00         lea r9, [rsp + 0x148]
00A1D095  33 D2                           xor edx, edx
00A1D097  8B CB                           mov ecx, ebx
00A1D099  E8 22 3A E5 FF                  call 0x140870ac0
00A1D09E  EB A3                           jmp 0x140a1d043
00A1D0A0  8A 84 24 AC 00 00 00            mov al, byte ptr [rsp + 0xac]
00A1D0A7  8A 94 24 AD 00 00 00            mov dl, byte ptr [rsp + 0xad]
00A1D0AE  84 D2                           test dl, dl
00A1D0B0  75 08                           jne 0x140a1d0ba
00A1D0B2  84 C0                           test al, al
00A1D0B4  0F 84 A9 01 00 00               je 0x140a1d263
00A1D0BA  4C 8B 94 24 58 01 00 00         mov r10, qword ptr [rsp + 0x158]
00A1D0C2  48 39 B4 24 48 01 00 00         cmp qword ptr [rsp + 0x148], rsi
00A1D0CA  4C 0F 45 94 24 48 01 00 00      cmovne r10, qword ptr [rsp + 0x148]
00A1D0D3  48 8B BC 24 D8 00 00 00         mov rdi, qword ptr [rsp + 0xd8]
00A1D0DB  0F B7 4F 02                     movzx ecx, word ptr [rdi + 2]
00A1D0DF  44 0F B7 C1                     movzx r8d, cx
00A1D0E3  66 41 83 E0 10                  and r8w, 0x10
00A1D0E8  75 05                           jne 0x140a1d0ef
00A1D0EA  48 8B D6                        mov rdx, rsi
00A1D0ED  EB 1D                           jmp 0x140a1d10c
00A1D0EF  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00A1D0F7  66 85 C9                        test cx, cx
00A1D0FA  79 0C                           jns 0x140a1d108
00A1D0FC  8B 50 0C                        mov edx, dword ptr [rax + 0xc]
00A1D0FF  85 D2                           test edx, edx
00A1D101  74 E7                           je 0x140a1d0ea
00A1D103  48 03 D0                        add rdx, rax
00A1D106  EB 04                           jmp 0x140a1d10c
00A1D108  48 8B 50 18                     mov rdx, qword ptr [rax + 0x18]
00A1D10C  66 45 85 C0                     test r8w, r8w
00A1D110  75 05                           jne 0x140a1d117
00A1D112  48 8B CE                        mov rcx, rsi
00A1D115  EB 1D                           jmp 0x140a1d134
00A1D117  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00A1D11F  66 85 C9                        test cx, cx
00A1D122  79 0C                           jns 0x140a1d130
00A1D124  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00A1D127  85 C9                           test ecx, ecx
00A1D129  74 E7                           je 0x140a1d112
00A1D12B  48 03 C8                        add rcx, rax
00A1D12E  EB 04                           jmp 0x140a1d134
00A1D130  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
00A1D134  8B 9C 24 E4 00 00 00            mov ebx, dword ptr [rsp + 0xe4]
00A1D13B  41 0B DF                        or ebx, r15d
00A1D13E  48 8D 84 24 CB 00 00 00         lea rax, [rsp + 0xcb]
00A1D146  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00A1D14B  48 8D 84 24 CA 00 00 00         lea rax, [rsp + 0xca]
00A1D153  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00A1D158  8A 84 24 A3 00 00 00            mov al, byte ptr [rsp + 0xa3]
00A1D15F  88 44 24 50                     mov byte ptr [rsp + 0x50], al
00A1D163  48 8B 84 24 90 01 00 00         mov rax, qword ptr [rsp + 0x190]
00A1D16B  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A1D170  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00A1D175  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
00A1D17A  8A 84 24 C0 03 00 00            mov al, byte ptr [rsp + 0x3c0]
00A1D181  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00A1D185  44 8B BC 24 C0 00 00 00         mov r15d, dword ptr [rsp + 0xc0]
00A1D18D  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00A1D192  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
00A1D19A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A1D19F  44 8B CB                        mov r9d, ebx
00A1D1A2  4D 8B C2                        mov r8, r10
00A1D1A5  E8 F2 21 01 00                  call 0x140a2f39c
00A1D1AA  4C 8B 84 24 58 01 00 00         mov r8, qword ptr [rsp + 0x158]
00A1D1B2  48 39 B4 24 48 01 00 00         cmp qword ptr [rsp + 0x148], rsi
00A1D1BA  4C 0F 45 84 24 48 01 00 00      cmovne r8, qword ptr [rsp + 0x148]
00A1D1C3  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
00A1D1C7  A8 10                           test al, 0x10
00A1D1C9  75 05                           jne 0x140a1d1d0
00A1D1CB  48 8B D6                        mov rdx, rsi
00A1D1CE  EB 1F                           jmp 0x140a1d1ef
00A1D1D0  66 85 C0                        test ax, ax
00A1D1D3  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00A1D1DB  79 0E                           jns 0x140a1d1eb
00A1D1DD  8B 48 0C                        mov ecx, dword ptr [rax + 0xc]
00A1D1E0  85 C9                           test ecx, ecx
00A1D1E2  74 E7                           je 0x140a1d1cb
00A1D1E4  8B D1                           mov edx, ecx
00A1D1E6  48 03 D0                        add rdx, rax
00A1D1E9  EB 04                           jmp 0x140a1d1ef
00A1D1EB  48 8B 50 18                     mov rdx, qword ptr [rax + 0x18]
00A1D1EF  48 8D 84 24 CB 00 00 00         lea rax, [rsp + 0xcb]
00A1D1F7  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00A1D1FC  48 8D 84 24 CA 00 00 00         lea rax, [rsp + 0xca]
00A1D204  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00A1D209  8A 84 24 A3 00 00 00            mov al, byte ptr [rsp + 0xa3]
00A1D210  88 44 24 50                     mov byte ptr [rsp + 0x50], al
00A1D214  48 8B 84 24 90 01 00 00         mov rax, qword ptr [rsp + 0x190]
00A1D21C  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00A1D221  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
00A1D226  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
00A1D22B  40 8A BC 24 C0 03 00 00         mov dil, byte ptr [rsp + 0x3c0]
00A1D233  40 88 7C 24 30                  mov byte ptr [rsp + 0x30], dil
00A1D238  44 89 7C 24 28                  mov dword ptr [rsp + 0x28], r15d
00A1D23D  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
00A1D245  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A1D24A  44 8B CB                        mov r9d, ebx
00A1D24D  48 8B 8C 24 B0 01 00 00         mov rcx, qword ptr [rsp + 0x1b0]
00A1D255  E8 F6 E2 A4 FF                  call 0x14046b550
00A1D25A  8A 94 24 AD 00 00 00            mov dl, byte ptr [rsp + 0xad]
00A1D261  EB 10                           jmp 0x140a1d273
00A1D263  44 8B BC 24 C0 00 00 00         mov r15d, dword ptr [rsp + 0xc0]
00A1D26B  40 8A BC 24 C0 03 00 00         mov dil, byte ptr [rsp + 0x3c0]
00A1D273  40 38 B4 24 CA 00 00 00         cmp byte ptr [rsp + 0xca], sil
00A1D27B  0F 85 B0 00 00 00               jne 0x140a1d331
00A1D281  40 38 B4 24 CB 00 00 00         cmp byte ptr [rsp + 0xcb], sil
00A1D289  0F 85 A2 00 00 00               jne 0x140a1d331
00A1D28F  48 39 B4 24 C0 01 00 00         cmp qword ptr [rsp + 0x1c0], rsi
00A1D297  0F 84 9F 02 00 00               je 0x140a1d53c
00A1D29D  40 38 B4 24 A1 00 00 00         cmp byte ptr [rsp + 0xa1], sil
00A1D2A5  0F 84 91 02 00 00               je 0x140a1d53c
00A1D2AB  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A1D2B4  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00A1D2BB  8A 84 24 A1 00 00 00            mov al, byte ptr [rsp + 0xa1]
00A1D2C2  88 44 24 48                     mov byte ptr [rsp + 0x48], al
00A1D2C6  48 8B 84 24 C0 01 00 00         mov rax, qword ptr [rsp + 0x1c0]
00A1D2CE  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00A1D2D3  8B 84 24 78 03 00 00            mov eax, dword ptr [rsp + 0x378]
00A1D2DA  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00A1D2DE  48 8B 81 D0 01 00 00            mov rax, qword ptr [rcx + 0x1d0]
00A1D2E5  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A1D2EA  48 8B 84 24 58 01 00 00         mov rax, qword ptr [rsp + 0x158]
00A1D2F2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A1D2F7  48 8B 84 24 48 01 00 00         mov rax, qword ptr [rsp + 0x148]
00A1D2FF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A1D304  4C 8D 8C 24 08 02 00 00         lea r9, [rsp + 0x208]
00A1D30C  4C 8B 84 24 E8 01 00 00         mov r8, qword ptr [rsp + 0x1e8]
00A1D314  48 8B 94 24 B0 01 00 00         mov rdx, qword ptr [rsp + 0x1b0]
00A1D31C  48 8B 8C 24 E0 01 00 00         mov rcx, qword ptr [rsp + 0x1e0]
00A1D324  E8 C7 10 E5 FF                  call 0x14086e3f0
00A1D329  40 8A FE                        mov dil, sil
00A1D32C  E9 12 02 00 00                  jmp 0x140a1d543
00A1D331  8B 84 24 0C 01 00 00            mov eax, dword ptr [rsp + 0x10c]
00A1D338  0F B6 C0                        movzx eax, al
00A1D33B  8A 8C 24 A1 00 00 00            mov cl, byte ptr [rsp + 0xa1]
00A1D342  84 C9                           test cl, cl
00A1D344  41 0F 45 C6                     cmovne eax, r14d
00A1D348  89 84 24 0C 01 00 00            mov dword ptr [rsp + 0x10c], eax
00A1D34F  8B 9C 24 6C 01 00 00            mov ebx, dword ptr [rsp + 0x16c]
00A1D356  40 38 B4 24 CA 00 00 00         cmp byte ptr [rsp + 0xca], sil
00A1D35E  0F 84 DE 00 00 00               je 0x140a1d442
00A1D364  84 D2                           test dl, dl
00A1D366  0F 84 D6 00 00 00               je 0x140a1d442
00A1D36C  40 8A C7                        mov al, dil
00A1D36F  F6 D8                           neg al
00A1D371  48 1B D2                        sbb rdx, rdx
00A1D374  49 23 D4                        and rdx, r12
00A1D377  F6 D9                           neg cl
00A1D379  4D 1B C0                        sbb r8, r8
00A1D37C  48 8D 84 24 08 02 00 00         lea rax, [rsp + 0x208]
00A1D384  4C 23 C0                        and r8, rax
00A1D387  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A1D390  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00A1D397  45 8B 0C 24                     mov r9d, dword ptr [r12]
00A1D39B  48 89 B4 24 90 00 00 00         mov qword ptr [rsp + 0x90], rsi
00A1D3A3  48 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], rsi
00A1D3AB  48 89 94 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdx
00A1D3B3  44 89 7C 24 78                  mov dword ptr [rsp + 0x78], r15d
00A1D3B8  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
00A1D3C0  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00A1D3C5  89 5C 24 68                     mov dword ptr [rsp + 0x68], ebx
00A1D3C9  48 8B 81 D0 01 00 00            mov rax, qword ptr [rcx + 0x1d0]
00A1D3D0  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00A1D3D5  44 88 74 24 58                  mov byte ptr [rsp + 0x58], r14b
00A1D3DA  48 8B 84 24 C0 01 00 00         mov rax, qword ptr [rsp + 0x1c0]
00A1D3E2  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00A1D3E7  44 89 4C 24 48                  mov dword ptr [rsp + 0x48], r9d
00A1D3EC  44 89 4C 24 40                  mov dword ptr [rsp + 0x40], r9d
00A1D3F1  48 8B 84 24 58 01 00 00         mov rax, qword ptr [rsp + 0x158]
00A1D3F9  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A1D3FE  48 8B 84 24 48 01 00 00         mov rax, qword ptr [rsp + 0x148]
00A1D406  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A1D40B  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00A1D413  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A1D418  48 8B 84 24 E8 01 00 00         mov rax, qword ptr [rsp + 0x1e8]
00A1D420  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A1D425  4C 8B 8C 24 B0 01 00 00         mov r9, qword ptr [rsp + 0x1b0]
00A1D42D  48 8B 94 24 E0 01 00 00         mov rdx, qword ptr [rsp + 0x1e0]
00A1D435  0F B7 8C 24 E8 00 00 00         movzx ecx, word ptr [rsp + 0xe8]
00A1D43D  E8 FA 1D F0 FF                  call 0x14091f23c
00A1D442  40 38 B4 24 CB 00 00 00         cmp byte ptr [rsp + 0xcb], sil
00A1D44A  0F 84 EC 00 00 00               je 0x140a1d53c
00A1D450  80 BC 24 AC 00 00 00 00         cmp byte ptr [rsp + 0xac], 0
00A1D458  0F 84 DE 00 00 00               je 0x140a1d53c
00A1D45E  40 8A C7                        mov al, dil
00A1D461  F6 D8                           neg al
00A1D463  48 1B D2                        sbb rdx, rdx
00A1D466  49 23 D4                        and rdx, r12
00A1D469  8A 84 24 A1 00 00 00            mov al, byte ptr [rsp + 0xa1]
00A1D470  F6 D8                           neg al
00A1D472  4D 1B C0                        sbb r8, r8
00A1D475  48 8D 84 24 08 02 00 00         lea rax, [rsp + 0x208]
00A1D47D  4C 23 C0                        and r8, rax
00A1D480  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A1D489  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00A1D490  48 89 B4 24 90 00 00 00         mov qword ptr [rsp + 0x90], rsi
00A1D498  48 89 B4 24 88 00 00 00         mov qword ptr [rsp + 0x88], rsi
00A1D4A0  48 89 94 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdx
00A1D4A8  44 89 7C 24 78                  mov dword ptr [rsp + 0x78], r15d
00A1D4AD  48 8B 84 24 40 01 00 00         mov rax, qword ptr [rsp + 0x140]
00A1D4B5  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00A1D4BA  89 5C 24 68                     mov dword ptr [rsp + 0x68], ebx
00A1D4BE  48 8B 81 D0 01 00 00            mov rax, qword ptr [rcx + 0x1d0]
00A1D4C5  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00A1D4CA  40 88 74 24 58                  mov byte ptr [rsp + 0x58], sil
00A1D4CF  48 8B 84 24 C0 01 00 00         mov rax, qword ptr [rsp + 0x1c0]
00A1D4D7  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00A1D4DC  8B 84 24 78 03 00 00            mov eax, dword ptr [rsp + 0x378]
00A1D4E3  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00A1D4E7  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00A1D4EB  48 8B 84 24 58 01 00 00         mov rax, qword ptr [rsp + 0x158]
00A1D4F3  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00A1D4F8  48 8B 84 24 48 01 00 00         mov rax, qword ptr [rsp + 0x148]
00A1D500  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A1D505  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00A1D50D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A1D512  48 8B 84 24 E8 01 00 00         mov rax, qword ptr [rsp + 0x1e8]
00A1D51A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00A1D51F  4C 8B 8C 24 B0 01 00 00         mov r9, qword ptr [rsp + 0x1b0]
00A1D527  48 8B 94 24 E0 01 00 00         mov rdx, qword ptr [rsp + 0x1e0]
00A1D52F  0F B7 8C 24 E8 00 00 00         movzx ecx, word ptr [rsp + 0xe8]
00A1D537  E8 00 1D F0 FF                  call 0x14091f23c
00A1D53C  8B BC 24 0C 01 00 00            mov edi, dword ptr [rsp + 0x10c]
00A1D543  48 8D 8C 24 48 01 00 00         lea rcx, [rsp + 0x148]
00A1D54B  E8 D0 8F EA FF                  call 0x1408c6520
00A1D550  90                              nop
00A1D551  40 38 B4 24 C0 03 00 00         cmp byte ptr [rsp + 0x3c0], sil
00A1D559  0F 84 E2 00 00 00               je 0x140a1d641
00A1D55F  89 B4 24 80 01 00 00            mov dword ptr [rsp + 0x180], esi
00A1D566  4C 8B 84 24 A8 01 00 00         mov r8, qword ptr [rsp + 0x1a8]
00A1D56E  4C 8B 8C 24 A0 01 00 00         mov r9, qword ptr [rsp + 0x1a0]
00A1D576  44 8A 94 24 A4 00 00 00         mov r10b, byte ptr [rsp + 0xa4]
00A1D57E  4D 85 ED                        test r13, r13
00A1D581  75 5C                           jne 0x140a1d5df
00A1D583  8B CE                           mov ecx, esi
00A1D585  89 8C 24 80 01 00 00            mov dword ptr [rsp + 0x180], ecx
00A1D58C  3B 8C 24 C0 00 00 00            cmp ecx, dword ptr [rsp + 0xc0]
00A1D593  0F 83 01 01 00 00               jae 0x140a1d69a
00A1D599  8B D1                           mov edx, ecx
00A1D59B  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
00A1D5A2  41 89 04 91                     mov dword ptr [r9 + rdx*4], eax
00A1D5A6  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
00A1D5AD  41 89 04 90                     mov dword ptr [r8 + rdx*4], eax
00A1D5B1  8A 05 0E 75 4E 00               mov al, byte ptr [rip + 0x4e750e]
00A1D5B7  84 C0                           test al, al
00A1D5B9  74 1F                           je 0x140a1d5da
00A1D5BB  45 84 D2                        test r10b, r10b
00A1D5BE  74 1A                           je 0x140a1d5da
00A1D5C0  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
00A1D5C7  85 C0                           test eax, eax
00A1D5C9  78 0F                           js 0x140a1d5da
00A1D5CB  41 89 04 91                     mov dword ptr [r9 + rdx*4], eax
00A1D5CF  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
00A1D5D6  41 21 04 90                     and dword ptr [r8 + rdx*4], eax
00A1D5DA  41 03 CE                        add ecx, r14d
00A1D5DD  EB A6                           jmp 0x140a1d585
00A1D5DF  8B D6                           mov edx, esi
00A1D5E1  89 94 24 80 01 00 00            mov dword ptr [rsp + 0x180], edx
00A1D5E8  3B 94 24 C0 00 00 00            cmp edx, dword ptr [rsp + 0xc0]
00A1D5EF  0F 83 A5 00 00 00               jae 0x140a1d69a
00A1D5F5  8B CA                           mov ecx, edx
00A1D5F7  41 8B 44 8D 00                  mov eax, dword ptr [r13 + rcx*4]
00A1D5FC  41 89 04 89                     mov dword ptr [r9 + rcx*4], eax
00A1D600  41 8B 04 8C                     mov eax, dword ptr [r12 + rcx*4]
00A1D604  41 89 04 88                     mov dword ptr [r8 + rcx*4], eax
00A1D608  8A 05 B7 74 4E 00               mov al, byte ptr [rip + 0x4e74b7]
00A1D60E  84 C0                           test al, al
00A1D610  74 2A                           je 0x140a1d63c
00A1D612  45 84 D2                        test r10b, r10b
00A1D615  74 25                           je 0x140a1d63c
00A1D617  41 39 74 8D 00                  cmp dword ptr [r13 + rcx*4], esi
00A1D61C  7C 1E                           jl 0x140a1d63c
00A1D61E  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
00A1D626  8B 04 88                        mov eax, dword ptr [rax + rcx*4]
00A1D629  41 89 04 89                     mov dword ptr [r9 + rcx*4], eax
00A1D62D  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00A1D635  8B 04 88                        mov eax, dword ptr [rax + rcx*4]
00A1D638  41 21 04 88                     and dword ptr [r8 + rcx*4], eax
00A1D63C  41 03 D6                        add edx, r14d
00A1D63F  EB A0                           jmp 0x140a1d5e1
00A1D641  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
00A1D648  48 8B 94 24 A0 01 00 00         mov rdx, qword ptr [rsp + 0x1a0]
00A1D650  89 02                           mov dword ptr [rdx], eax
00A1D652  8B 84 24 B8 00 00 00            mov eax, dword ptr [rsp + 0xb8]
00A1D659  48 8B 8C 24 A8 01 00 00         mov rcx, qword ptr [rsp + 0x1a8]
00A1D661  89 01                           mov dword ptr [rcx], eax
00A1D663  8A 05 5C 74 4E 00               mov al, byte ptr [rip + 0x4e745c]
00A1D669  84 C0                           test al, al
00A1D66B  74 2D                           je 0x140a1d69a
00A1D66D  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
00A1D675  80 BC 24 A4 00 00 00 00         cmp byte ptr [rsp + 0xa4], 0
00A1D67D  74 23                           je 0x140a1d6a2
00A1D67F  39 B4 24 B0 00 00 00            cmp dword ptr [rsp + 0xb0], esi
00A1D686  7C 1A                           jl 0x140a1d6a2
00A1D688  48 8B 84 24 38 01 00 00         mov rax, qword ptr [rsp + 0x138]
00A1D690  8B 00                           mov eax, dword ptr [rax]
00A1D692  89 02                           mov dword ptr [rdx], eax
00A1D694  8B 03                           mov eax, dword ptr [rbx]
00A1D696  21 01                           and dword ptr [rcx], eax
00A1D698  EB 08                           jmp 0x140a1d6a2
00A1D69A  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
00A1D6A2  48 8B 84 24 48 02 00 00         mov rax, qword ptr [rsp + 0x248]
00A1D6AA  40 88 38                        mov byte ptr [rax], dil
00A1D6AD  8B FE                           mov edi, esi
00A1D6AF  89 B4 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], esi
00A1D6B6  44 8A AC 24 A0 00 00 00         mov r13b, byte ptr [rsp + 0xa0]
00A1D6BE  EB 39                           jmp 0x140a1d6f9
00A1D6C0  8B F8                           mov edi, eax
00A1D6C2  89 84 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], eax
00A1D6C9  33 F6                           xor esi, esi
00A1D6CB  44 8D 76 01                     lea r14d, [rsi + 1]
00A1D6CF  4C 8B A4 24 30 01 00 00         mov r12, qword ptr [rsp + 0x130]
00A1D6D7  44 8A AC 24 E0 00 00 00         mov r13b, byte ptr [rsp + 0xe0]
00A1D6DF  48 8B 9C 24 D0 00 00 00         mov rbx, qword ptr [rsp + 0xd0]
00A1D6E7  EB 10                           jmp 0x140a1d6f9
00A1D6E9  BF 0D 00 00 C0                  mov edi, 0xc000000d
00A1D6EE  48 8B DE                        mov rbx, rsi
00A1D6F1  44 8A AC 24 A0 00 00 00         mov r13b, byte ptr [rsp + 0xa0]
00A1D6F9  40 38 B4 24 FC 00 00 00         cmp byte ptr [rsp + 0xfc], sil
00A1D701  74 1D                           je 0x140a1d720
00A1D703  48 8B 8C 24 10 02 00 00         mov rcx, qword ptr [rsp + 0x210]
00A1D70B  E8 40 BC 8D FF                  call 0x1402f9350
00A1D710  48 8B 84 24 50 02 00 00         mov rax, qword ptr [rsp + 0x250]
00A1D718  48 89 84 24 48 01 00 00         mov qword ptr [rsp + 0x148], rax
00A1D720  48 8B 8C 24 C0 01 00 00         mov rcx, qword ptr [rsp + 0x1c0]
00A1D728  48 85 C9                        test rcx, rcx
00A1D72B  74 07                           je 0x140a1d734
00A1D72D  33 D2                           xor edx, edx
00A1D72F  E8 3C 51 16 00                  call 0x140b82870
00A1D734  48 8D 8C 24 48 01 00 00         lea rcx, [rsp + 0x148]
00A1D73C  E8 CF DF E4 FF                  call 0x14086b710
00A1D741  45 33 C0                        xor r8d, r8d
00A1D744  41 8A D5                        mov dl, r13b
00A1D747  48 8B 8C 24 D8 00 00 00         mov rcx, qword ptr [rsp + 0xd8]
00A1D74F  E8 3C 7A F5 FF                  call 0x140975190
00A1D754  48 8B 8C 24 E0 01 00 00         mov rcx, qword ptr [rsp + 0x1e0]
00A1D75C  48 85 C9                        test rcx, rcx
00A1D75F  74 07                           je 0x140a1d768
00A1D761  33 D2                           xor edx, edx
00A1D763  E8 08 51 16 00                  call 0x140b82870
00A1D768  48 8B 8C 24 B0 01 00 00         mov rcx, qword ptr [rsp + 0x1b0]
00A1D770  48 85 C9                        test rcx, rcx
00A1D773  74 07                           je 0x140a1d77c
00A1D775  33 D2                           xor edx, edx
00A1D777  E8 F4 50 16 00                  call 0x140b82870
00A1D77C  48 8B 8C 24 E8 01 00 00         mov rcx, qword ptr [rsp + 0x1e8]
00A1D784  48 85 C9                        test rcx, rcx
00A1D787  74 07                           je 0x140a1d790
00A1D789  33 D2                           xor edx, edx
00A1D78B  E8 E0 50 16 00                  call 0x140b82870
00A1D790  48 8B 8C 24 90 01 00 00         mov rcx, qword ptr [rsp + 0x190]
00A1D798  48 85 C9                        test rcx, rcx
00A1D79B  74 0B                           je 0x140a1d7a8
00A1D79D  45 8A C6                        mov r8b, r14b
00A1D7A0  41 8A D5                        mov dl, r13b
00A1D7A3  E8 A8 17 01 00                  call 0x140a2ef50
00A1D7A8  48 8B 8C 24 40 01 00 00         mov rcx, qword ptr [rsp + 0x140]
00A1D7B0  48 85 C9                        test rcx, rcx
00A1D7B3  74 05                           je 0x140a1d7ba
00A1D7B5  E8 EA 94 BE FF                  call 0x140606ca4
00A1D7BA  40 38 B4 24 AE 00 00 00         cmp byte ptr [rsp + 0xae], sil
00A1D7C2  74 1E                           je 0x140a1d7e2
00A1D7C4  4D 85 E4                        test r12, r12
00A1D7C7  74 0A                           je 0x140a1d7d3
00A1D7C9  33 D2                           xor edx, edx
00A1D7CB  49 8B CC                        mov rcx, r12
00A1D7CE  E8 9D 50 16 00                  call 0x140b82870
00A1D7D3  48 85 DB                        test rbx, rbx
00A1D7D6  74 0A                           je 0x140a1d7e2
00A1D7D8  33 D2                           xor edx, edx
00A1D7DA  48 8B CB                        mov rcx, rbx
00A1D7DD  E8 8E 50 16 00                  call 0x140b82870
00A1D7E2  40 38 B4 24 A5 00 00 00         cmp byte ptr [rsp + 0xa5], sil
00A1D7EA  74 0D                           je 0x140a1d7f9
00A1D7EC  48 8B 8C 24 78 01 00 00         mov rcx, qword ptr [rsp + 0x178]
00A1D7F4  E8 A3 46 A9 FF                  call 0x1404b1e9c
00A1D7F9  48 8B 8C 24 B8 01 00 00         mov rcx, qword ptr [rsp + 0x1b8]
00A1D801  48 85 C9                        test rcx, rcx
00A1D804  74 07                           je 0x140a1d80d
00A1D806  33 D2                           xor edx, edx
00A1D808  E8 63 50 16 00                  call 0x140b82870
00A1D80D  48 8B 8C 24 20 01 00 00         mov rcx, qword ptr [rsp + 0x120]
00A1D815  E8 D6 41 8E FF                  call 0x1403019f0
00A1D81A  81 FF 9A 00 00 C0               cmp edi, 0xc000009a
00A1D820  74 0A                           je 0x140a1d82c
00A1D822  40 38 B4 24 07 01 00 00         cmp byte ptr [rsp + 0x107], sil
00A1D82A  74 07                           je 0x140a1d833
00A1D82C  8B CF                           mov ecx, edi
00A1D82E  E8 ED 15 E5 FF                  call 0x14086ee20
00A1D833  8B C7                           mov eax, edi
00A1D835  48 8B 8C 24 F0 02 00 00         mov rcx, qword ptr [rsp + 0x2f0]
00A1D83D  48 33 CC                        xor rcx, rsp
00A1D840  E8 FB ED C8 FF                  call 0x1406ac640
00A1D845  48 81 C4 00 03 00 00            add rsp, 0x300
00A1D84C  41 5F                           pop r15
00A1D84E  41 5E                           pop r14
00A1D850  41 5D                           pop r13
00A1D852  41 5C                           pop r12
00A1D854  5F                              pop rdi
00A1D855  5E                              pop rsi
00A1D856  5B                              pop rbx
00A1D857  C3                              ret
00A1D858  CC                              int3
00A1D859  E8 72 C7 E7 FF                  call 0x140899fd0
00A1D85E  90                              nop
00A1D85F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepAccessCheckAndAuditAlarm(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, unsigned int a8, unsigned int a9, __int64 a10, __int64 a11, unsigned int a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, unsigned __int8 a17)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned int v_stack_m168;
    unsigned int v_stack_m16C;
    unsigned int v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned int v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned int v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned int v_stack_m1C8;
    unsigned int v_stack_m1CC;
    unsigned int v_stack_m1D0;
    unsigned __int64 v_stack_m1E0;
    unsigned int v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned int v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned int v_stack_m220;
    unsigned int v_stack_m224;
    unsigned int v_stack_m228;
    unsigned int v_stack_m22C;
    unsigned int v_stack_m230;
    unsigned __int8 v_stack_m231;
    unsigned __int8 v_stack_m233;
    unsigned __int8 v_stack_m234;
    unsigned int v_stack_m238;
    unsigned __int8 v_stack_m23B;
    unsigned __int8 v_stack_m23C;
    unsigned __int8 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned int v_stack_m24C;
    unsigned __int16 v_stack_m250;
    unsigned int v_stack_m254;
    unsigned __int8 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int8 v_stack_m26D;
    unsigned __int8 v_stack_m26E;
    unsigned __int8 v_stack_m26F;
    unsigned __int8 v_stack_m270;
    unsigned int v_stack_m278;
    unsigned int v_stack_m280;
    unsigned __int8 v_stack_m283;
    unsigned __int8 v_stack_m284;
    unsigned int v_stack_m288;
    unsigned __int8 v_stack_m28A;
    unsigned __int8 v_stack_m28B;
    unsigned __int8 v_stack_m28C;
    unsigned int v_stack_m290;
    unsigned __int8 v_stack_m293;
    unsigned __int8 v_stack_m294;
    unsigned __int8 v_stack_m295;
    unsigned __int8 v_stack_m296;
    unsigned __int8 v_stack_m297;
    unsigned __int8 v_stack_m298;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m2B0;
    unsigned __int64 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned __int8 v_stack_m2C8;
    unsigned __int8 v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned __int64 v_stack_m2E0;
    unsigned __int64 v_stack_m2E8;
    unsigned __int8 v_stack_m2F0;
    unsigned int v_stack_m2F8;
    unsigned __int64 v_stack_m300;
    unsigned __int64 v_stack_m308;
    unsigned __int64 v_stack_m310;
    unsigned __int64 v_stack_m318;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned __int8 v_stack_m61;
    unsigned __int8 v_stack_m62;
    unsigned __int8 v_stack_m63;
    unsigned __int64 v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC4;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_p40;
    unsigned __int8 v_stack_p50;

    v_rsp = (v_rsp) - (768);
    result = (*(unsigned __int64 *)(v_rip + 4126682)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m120 = a4;
    v_stack_mC0 = a1;
    v_stack_m210 = (unsigned int)((unsigned int)(a12));
    v_stack_mD8 = a16;
    v_stack_m190 = a14;
    v_stack_m198 = a15;
    v_stack_mA8 = a1;
    v_stack_m130 = a2;
    v_stack_mB8 = a3;
    v_stack_mB0 = a4;
    v_stack_m118 = a5;
    v_stack_m248 = a6;
    v_stack_m148 = a6;
    v_stack_m138 = a7;
    v_stack_m140 = a11;
    v_stack_m278 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a12))));
    v_stack_m1D0 = (unsigned int)((unsigned int)(a12));
    v_stack_m100 = a14;
    v_stack_mF8 = a15;
    v_stack_mF0 = a16;
    v_stack_m1F0 = v_xmm0;
    v_stack_m1E0 = v_xmm0;
    v_rsi = 0;
    v_stack_m290 = 0;
    v_stack_m280 = 0;
    v_stack_m28A = 0;
    v_stack_m288 = 0xC0000001ULL;
    v_stack_m170 = 0;
    v_stack_m268 = 0;
    v_stack_m16C = 0;
    v_stack_m200 = 0;
    v_stack_m230 = 0;
    v_stack_m22C = 0;
    v_stack_m240 = 0;
    v_stack_m158 = 0;
    v_stack_m188 = 0;
    v_stack_m150 = 0;
    v_stack_m260 = 0;
    v_stack_m1A8 = 0;
    v_stack_m1F8 = 0;
    v_stack_m254 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m178 = 0;
    v_stack_m297 = 0;
    v_stack_m296 = 0;
    v_stack_m26E = 0;
    v_stack_m26D = 0;
    v_stack_m233 = 0;
    v_stack_m28B = 0;
    v_stack_m28C = 0;
    v_stack_m270 = (unsigned __int8)(v_rsi + 1);
    v_stack_m26F = 0;
    v_stack_m128 = 0;
    v_stack_mE8 = 0;
    v_stack_m23C = 0;
    v_stack_mD0 = v_xmm0;
    v_stack_m160 = 0;
    v_stack_m1B0 = 0;
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = 0;
    v_stack_m1C0 = 0;
    v_stack_m293 = 0;
    v_stack_m294 = 0;
    v_stack_m295 = 0;
    v_stack_m231 = 0;
    v_stack_m250 = 999;
    result = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    v_stack_m238 = 0;
    v_stack_m23B = 0;
    v_stack_m24C = 0;
    v_stack_m218 = 0;
    v_stack_m224 = 0;
    v_stack_m168 = 0;
    v_stack_m234 = 0;
    v_stack_m284 = 0;
    v_stack_m283 = 0;
    v_stack_m180 = 0;
    v_stack_m220 = 0;
    result = (unsigned int)((0) | (0xFFFFFFFFULL));
    v_stack_m1A0 = (unsigned int)(result);
    v_stack_m160 = (unsigned int)(result);
    v_stack_m298 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m258 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    result = SeCaptureSubjectContext(v_stack_m1F0, a2, a1, a14);
    if (a9 != 0) goto loc_00A1B2A1;
    v_stack_m1CC = 2;
    goto loc_00A1B2BA;
loc_00A1B2A1:
    if (a9 != ((unsigned int)(v_rsi + 1))) goto loc_00A1D6E9;
    v_stack_m1CC = 7;
loc_00A1B2BA:
    if (a3 != 0) goto loc_00A1B2E7;
    if (v_stack_m1F0 != 0) goto loc_00A1B2D3;
    goto loc_00A1D6EE;
loc_00A1B2D3:
    if (v_stack_m1E8 >= ((unsigned int)(v_rsi + 1))) goto loc_00A1B2E7;
    goto loc_00A1D6EE;
loc_00A1B2E7:
    if (a17 == 0) goto loc_00A1B362;
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a12)))) != 0) goto loc_00A1B311;
loc_00A1B2F6:
    v_stack_m290 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_00A1B3C6;
loc_00A1B311:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a12))))) > 0x1000ULL) goto loc_00A1B2F6;
    result = ProbeForWrite(v_stack_m198, (unsigned int)((unsigned int)((unsigned int)(a12))) * 4, 4, a14);
    result = ProbeForWrite(v_stack_m190, (unsigned int)((unsigned int)((unsigned int)(a12))) * 4, 4, a14);
    goto loc_00A1B39C;
loc_00A1B362:
    a1 = (unsigned int)((unsigned int)((unsigned int)(a12)));
    if (v_stack_m198 < ((unsigned int)((unsigned int)((unsigned int)(a12))))) { a1 = v_stack_m198; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    a1 = (unsigned int)((unsigned int)((unsigned int)(a12)));
    if (v_stack_m190 < ((unsigned int)((unsigned int)((unsigned int)(a12))))) { a1 = v_stack_m190; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
loc_00A1B39C:
    if ((((unsigned __int8)((unsigned int)(0xC000000DULL))) & (3)) != 0) goto loc_00A1D859;
    result = (unsigned int)((unsigned int)((unsigned int)(a12)));
    if (((unsigned int)(0xC000000DULL)) < ((unsigned int)((unsigned int)((unsigned int)(a12))))) { result = (unsigned int)(0xC000000DULL); }
    v_stack_m58 = v_xmm0;
loc_00A1B3C6:
    goto loc_00A1B4B2;
loc_00A1B4B2:
    if (sign_flag) goto loc_00A1B7DB;
    if (a3 == 0) goto loc_00A1B557;
    v_stack_mE0 = 0;
    v_stack_m310 = 0;
    v_stack_m318 = v_stack_mE0;
    result = ObReferenceObjectByHandle(*(unsigned __int64 *)(a3), 8, *(unsigned __int64 *)(v_rip + 6015830), (unsigned __int8)(v_stack_m298));
    v_stack_m128 = v_stack_mE0;
    if (!sign_flag) goto loc_00A1B535;
    v_stack_m128 = 0;
loc_00A1B528:
    goto loc_00A1D6F9;
loc_00A1B535:
    v_stack_mE8 = v_stack_m1F0;
    v_stack_m1F0 = v_stack_mE0;
    v_stack_m23C = (unsigned __int8)(v_rsi + 1);
    goto loc_00A1B55F;
loc_00A1B557:
loc_00A1B55F:
    result = v_stack_m1E0;
    if (v_stack_m1F0 != 0) { result = v_stack_m1F0; }
    v_stack_m248 = result;
    result = SeCheckAuditPrivilege(v_stack_m1F0, (unsigned __int8)(v_stack_m298), *(unsigned __int64 *)(v_rip + 6015830), (unsigned __int8)(v_stack_m298));
    if ((unsigned __int8)(result) != 0) goto loc_00A1B5A6;
    if (((v_stack_p50) & ((unsigned __int8)(v_rsi + 1))) == 0) goto loc_00A1B5BD;
    v_stack_m233 = (unsigned __int8)(v_rsi + 1);
loc_00A1B5A6:
    if (((a8) & (0xF0000000ULL)) == 0) goto loc_00A1B5C7;
    goto loc_00A1B528;
loc_00A1B5BD:
    goto loc_00A1B528;
loc_00A1B5C7:
    v_stack_m318 = v_stack_m260;
    a4 = 0;
    result = SeCaptureSecurityDescriptor(v_stack_m268, (unsigned __int8)(v_stack_m298), (unsigned int)((unsigned int)(v_rsi + 1)), a4);
    v_stack_m290 = (unsigned int)(result);
    if (!sign_flag) goto loc_00A1B5FF;
    v_stack_m260 = 0;
    goto loc_00A1B528;
loc_00A1B5FF:
    if (v_stack_m260 != 0) goto loc_00A1B613;
loc_00A1B609:
    goto loc_00A1B528;
loc_00A1B613:
    if (!sign_flag) goto loc_00A1B630;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m260 + 4))) == 0) goto loc_00A1B609;
    result = ((unsigned int)(*(unsigned int *)(v_stack_m260 + 4))) + (v_stack_m260);
    goto loc_00A1B63C;
loc_00A1B630:
loc_00A1B63C:
    if (*(unsigned __int64 *)(v_stack_m260 + 8) == 0) goto loc_00A1B609;
    if (!sign_flag) goto loc_00A1B65A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m260 + 8))) == 0) goto loc_00A1B609;
    result = ((unsigned int)(*(unsigned int *)(v_stack_m260 + 8))) + (v_stack_m260);
    goto loc_00A1B666;
loc_00A1B65A:
loc_00A1B666:
    if (*(unsigned __int64 *)(v_stack_m260 + 16) == 0) goto loc_00A1B609;
    v_r15 = (unsigned int)((unsigned int)((unsigned int)(a12)));
    if (v_stack_mF0 < ((unsigned int)((unsigned int)((unsigned int)(a12))))) { v_r15 = v_stack_mD8; }
    *(unsigned __int8 *)(v_r15) = (unsigned __int8)(*(unsigned __int8 *)(v_r15));
    result = SepProbeAndCaptureString_U(v_stack_mC0, v_stack_m158, (unsigned int)((unsigned int)(v_rsi + 1)), a4);
    v_stack_m290 = (unsigned int)(result);
    if (sign_flag) goto loc_00A1B6E4;
    result = SepProbeAndCaptureString_U(v_stack_m120, v_stack_m188, (unsigned int)((unsigned int)(v_rsi + 1)), a4);
    v_stack_m290 = (unsigned int)(result);
    v_rdi = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        a2 = v_stack_m150;
        a1 = v_stack_m118;
        result = SepProbeAndCaptureString_U(a1, a2, (unsigned int)((unsigned int)(v_rsi + 1)), a4);
        v_rdi = (unsigned int)(result);
        v_stack_m290 = (unsigned int)(result);
    }
    goto loc_00A1B7A8;
loc_00A1B7A8:
    if (sign_flag) goto loc_00A1B7DB;
    if (v_stack_m138 == 0) goto loc_00A1B7E8;
    v_stack_m308 = v_stack_m1A8;
    v_stack_m310 = (unsigned __int8)(v_rsi + 1);
    result = SeCaptureSid(v_stack_m138, (unsigned __int8)(v_stack_m298), (unsigned int)((unsigned int)(v_rsi + 1)), a4);
    if (!sign_flag) goto loc_00A1B7E8;
    v_stack_m1A8 = 0;
loc_00A1B7DB:
    goto loc_00A1D6F1;
loc_00A1B7E8:
    result = SeCaptureObjectTypeList(v_stack_m140, (unsigned int)(v_stack_m278), (unsigned __int8)(v_stack_m268), v_stack_m1F8);
    if (sign_flag) goto loc_00A1B7DB;
    v_stack_m308 = v_stack_m1A0;
    v_stack_m310 = (unsigned __int8)(v_rsi + 1);
    v_stack_m318 = 0;
    a4 = 0;
    result = SepTrustLevelCheck(v_stack_m140, v_stack_m260, v_stack_m1F0, a4);
    if (sign_flag) goto loc_00A1B7DB;
    result = SepFilterToDiscretionary(v_stack_m1A0, (unsigned int)((unsigned int)((unsigned int)(a8))), v_stack_m1F0, a4);
    v_stack_m290 = (unsigned int)(result);
    result = v_stack_m284;
    if (sign_flag) { result = (unsigned int)(v_rsi + 1); }
    v_stack_m284 = (unsigned __int8)(result);
    if (sign_flag) goto loc_00A1BA4F;
    v_stack_m318 = v_stack_m160;
    result = SepFilterCheck(v_stack_m260, v_stack_m218, v_stack_m248, (unsigned __int8)(v_rsi + 1));
    if (sign_flag) goto loc_00A1B7DB;
    result = SepFilterToDiscretionary(v_stack_m160, (unsigned int)((unsigned int)((unsigned int)(a8))), v_stack_m248, (unsigned __int8)(v_rsi + 1));
    v_stack_m290 = (unsigned int)(result);
    result = v_stack_m283;
    if (sign_flag) { result = (unsigned int)(v_rsi + 1); }
    v_stack_m283 = (unsigned __int8)(result);
    if (sign_flag) goto loc_00A1BA4F;
    v_stack_m310 = v_stack_mD0;
    v_stack_m318 = (unsigned __int8)(v_rsi + 1);
    a3 = 0;
    result = SepMandatoryIntegrityCheck(v_stack_m58, v_stack_m260, a3, v_stack_m248);
    if (sign_flag) goto loc_00A1B7DB;
    result = SepMandatoryToDiscretionary(v_stack_mD0, (unsigned int)((unsigned int)((unsigned int)(a8))), a3, v_stack_m248);
    v_stack_m290 = (unsigned int)(result);
    if (sign_flag) goto loc_00A1B94A;
    if (condition_is_above_or_equal) goto loc_00A1B976;
loc_00A1B94A:
    if (((*(unsigned int *)(v_stack_m248 + 200)) & (0x4000ULL)) != 0) {
        result = v_stack_m238;
        result = (unsigned __int8)(result);
        if (v_stack_mC4 <= 0x2000ULL) { result = (unsigned int)(v_rsi + 1); }
        v_stack_m238 = (unsigned int)(result);
    }
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(v_stack_mD0, (unsigned int)((unsigned int)((unsigned int)(a8))), a3, v_stack_m248);
    if ((unsigned int)(result) == 0) goto loc_00A1B9DF;
    v_stack_m310 = v_stack_m220;
    v_stack_m318 = (unsigned int)((unsigned int)(a8));
    a3 = 0;
    result = SepMandatoryAccessCheck(v_stack_m260, v_stack_m1F0, a3, (unsigned __int8)(v_rsi + 1));
    if (sign_flag) goto loc_00A1B9C1;
    result = (unsigned int)(((unsigned int)(v_stack_m220)) & ((unsigned int)((unsigned int)(a8))));
    if ((((unsigned int)(result)) & (0xFDFFFFFFULL)) == 0) goto loc_00A1B9DF;
loc_00A1B9C1:
    *(unsigned int *)(v_stack_m190) = 0;
    *(unsigned int *)(v_stack_m198) = (unsigned int)((unsigned int)(0xC00001C0ULL));
    goto loc_00A1B7DB;
loc_00A1B9DF:
    if (!sign_flag) goto loc_00A1B9F0;
    if ((unsigned __int8)((unsigned int)(v_stack_m238)) == 0) goto loc_00A1BA5F;
loc_00A1B9F0:
    v_stack_m310 = (unsigned __int8)(v_stack_m298);
    v_stack_m318 = v_stack_m178;
    a4 = 0;
    result = SePrivilegePolicyCheck(a8, v_stack_m254, v_stack_m1F0, a4);
    v_stack_m290 = (unsigned int)(result);
    if ((unsigned int)((unsigned int)(a8)) != 0) goto loc_00A1BA5F;
    v_r13 = (unsigned __int8)((unsigned int)(v_stack_m168));
    if (v_stack_m254 != 0) { v_r13 = (unsigned int)(v_rsi + 1); }
    goto loc_00A1BA5F;
loc_00A1BA4F:
loc_00A1BA5F:
    result = SeLockSubjectContext(v_stack_m1F0, v_stack_m254, v_stack_m1F0, a4);
    if (!sign_flag) goto loc_00A1BB23;
    if ((unsigned __int8)((unsigned int)(v_stack_m238)) != 0) goto loc_00A1BB23;
    v_stack_m296 = (unsigned __int8)(v_rsi + 1);
    v_stack_m288 = (unsigned int)((unsigned int)((unsigned int)(result)));
    if (a17 == ((unsigned __int8)((unsigned int)(v_stack_m238)))) goto loc_00A1C68E;
    result = ExAllocatePool2(256, (unsigned int)(v_stack_m278) * 8, (unsigned int)(0x61476553ULL), a4);
    v_stack_m208 = result;
    if (result != 0) goto loc_00A1BAE0;
    result = SeUnlockSubjectContext(v_stack_m1F0, (unsigned int)(v_stack_m278) * 8, (unsigned int)(0x61476553ULL), a4);
    goto loc_00A1B7DB;
loc_00A1BAE0:
    v_stack_m28A = (unsigned __int8)(v_rsi + 1);
    if (v_stack_m278 <= 0) goto loc_00A1CE73;
    a2 = (result) - (result + (unsigned int)(v_stack_m278) * 4);
loc_00A1BB02:
    *(unsigned int *)(a2 + result + (unsigned int)(v_stack_m278) * 4 * 1) = (unsigned int)((unsigned int)(v_stack_m280));
    *(unsigned int *)(result + (unsigned int)(v_stack_m278) * 4) = (unsigned int)((unsigned int)(v_stack_m288));
    v_rbx = ((unsigned int)(v_stack_m278)) - (v_rsi + 1);
    if (condition_is_not_equal) goto loc_00A1BB02;
    goto loc_00A1CE73;
loc_00A1BB23:
    result = SepTokenIsOwner(v_rbx, v_stack_m260, (unsigned int)(0x61476553ULL), a4);
    v_stack_m295 = (unsigned __int8)(result);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 5148549)) == 0) goto loc_00A1BB81;
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_m260 + 2))) & (16)) == 0) goto loc_00A1BB79;
    if (((unsigned __int8)(v_cr8)) >= 2) goto loc_00A1BB79;
    if (!sign_flag) goto loc_00A1BBD4;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m260 + 12))) != 0) goto loc_00A1BBCA;
    v_stack_m1B0 = 0;
loc_00A1BB72:
loc_00A1BB79:
loc_00A1BB81:
loc_00A1BB90:
    if ((((unsigned int)((unsigned int)(a8))) & (0x2060000ULL)) == 0) goto loc_00A1BCC1;
    if ((unsigned __int8)(v_stack_m295) == 0) goto loc_00A1BCC1;
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_m260 + 2))) & (4)) != 0) goto loc_00A1BC50;
loc_00A1BBC2:
    goto loc_00A1BC71;
loc_00A1BBCA:
    result = (v_stack_m260) + (v_stack_m260);
    goto loc_00A1BBE0;
loc_00A1BBD4:
loc_00A1BBE0:
    v_stack_m1B0 = *(unsigned __int64 *)(v_stack_m260 + 24);
    if (*(unsigned __int64 *)(v_stack_m260 + 24) == 0) goto loc_00A1BB72;
    result = SepGetScopedPolicySid(*(unsigned __int64 *)(v_stack_m260 + 24), *(unsigned __int16 *)(v_stack_m260 + 2), (unsigned int)(0x61476553ULL), a4);
    if (result == 0) goto loc_00A1BB72;
    result = SepRmReferenceFindCap(result, v_stack_m1C0, (unsigned int)(0x61476553ULL), a4);
    a2 = v_stack_m1C0;
    if (sign_flag) { a2 = *(unsigned __int64 *)(v_rip + 6014160); }
    v_stack_m1C0 = a2;
    v_stack_m290 = 0;
    v_stack_m293 = (unsigned __int8)(v_rsi + 1);
    goto loc_00A1BB90;
loc_00A1BC50:
    if (!sign_flag) goto loc_00A1BC6D;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m260 + 16))) == 0) goto loc_00A1BBC2;
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_m260 + 16))) + (v_stack_m260);
    goto loc_00A1BC71;
loc_00A1BC6D:
loc_00A1BC71:
    result = RtlOwnerAcesPresent(*(unsigned __int64 *)(v_stack_m260 + 32), a2, (unsigned int)(0x61476553ULL), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00A1BCC1;
    if (condition_is_above_or_equal) goto loc_00A1BC98;
    v_stack_m24C = (unsigned int)((unsigned int)(0x60000ULL));
    result = (unsigned int)(((unsigned int)(v_stack_m254)) | ((unsigned int)((unsigned int)(0x60000ULL))));
    goto loc_00A1BCAB;
loc_00A1BC98:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a8)))) & ((unsigned int)((unsigned int)(0x60000ULL))));
    v_stack_m24C = (unsigned int)(result);
    result = (unsigned int)((result) | (v_stack_m254));
loc_00A1BCAB:
    v_stack_m254 = (unsigned int)(result);
    v_r15 = (unsigned int)(((unsigned int)(a8)) & (0xFFF9FFFFULL));
    v_stack_p40 = (unsigned int)(v_r15);
loc_00A1BCC1:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline((unsigned int)(0x60000ULL), a2, (unsigned int)(0x61476553ULL), a4);
    if ((unsigned int)(result) == 0) goto loc_00A1C5A2;
    if ((unsigned int)(v_r15) != 0) goto loc_00A1BDD7;
    if ((unsigned __int8)((unsigned __int8)(v_rsi + 1)) == 0) goto loc_00A1BCE5;
    if ((unsigned __int8)(result + (unsigned int)(v_stack_m278) * 4) == 0) goto loc_00A1BDD7;
loc_00A1BCE5:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m248 + 200))) & (0x6000ULL));
    if (((unsigned int)(result)) == 0x2000ULL) goto loc_00A1BD04;
    if (v_stack_m24C != 0) goto loc_00A1BDD7;
loc_00A1BD04:
    v_stack_m280 = (unsigned int)((unsigned int)(v_stack_m254));
    if ((unsigned int)((unsigned int)(v_stack_m254)) != 0) goto loc_00A1BD23;
    goto loc_00A1BD2B;
loc_00A1BD23:
loc_00A1BD2B:
    v_stack_m297 = (unsigned __int8)((unsigned __int8)(v_rsi + 1));
    v_stack_m296 = 0;
    v_stack_m288 = 0;
    if (a17 == 0) goto loc_00A1C68E;
    result = ExAllocatePool2(256, (unsigned int)(v_stack_m278) * 8, (unsigned int)(0x61476553ULL), a4);
    v_stack_m208 = result;
    if (result != 0) goto loc_00A1BD94;
loc_00A1BD7D:
    result = SeUnlockSubjectContext(v_stack_m1F0, (unsigned int)(v_stack_m278) * 8, (unsigned int)(0x61476553ULL), a4);
    goto loc_00A1B7DB;
loc_00A1BD94:
    v_stack_m28A = (unsigned __int8)(v_rsi + 1);
    if (v_stack_m278 <= 0) goto loc_00A1CE73;
    a2 = (result) - (result + (unsigned int)(v_stack_m278) * 4);
loc_00A1BDB6:
    *(unsigned int *)(result + (unsigned int)(v_stack_m278) * 4 + a2 * 1) = (unsigned int)((unsigned int)(v_stack_m280));
    *(unsigned int *)(result + (unsigned int)(v_stack_m278) * 4) = (unsigned int)((unsigned int)(v_stack_m288));
    v_rbx = ((unsigned int)(v_stack_m278)) - (v_rsi + 1);
    if (condition_is_not_equal) goto loc_00A1BDB6;
    goto loc_00A1CE73;
loc_00A1BDD7:
    v_stack_m148 = (unsigned int)(v_stack_m1D0);
    if (a17 == 0) goto loc_00A1BE2D;
    result = ExAllocatePool2(256, (unsigned int)(v_stack_m1D0) * 8, (unsigned int)(0x61476553ULL), a4);
    v_stack_m208 = result;
    if (result == 0) goto loc_00A1BD7D;
    v_stack_m28A = (unsigned __int8)(v_rsi + 1);
    goto loc_00A1BE45;
loc_00A1BE2D:
    v_stack_m208 = v_stack_m280;
loc_00A1BE45:
    v_stack_m78 = (unsigned int)((unsigned int)(v_stack_m24C));
    v_stack_m2A8 = v_stack_m296;
    v_stack_m2B0 = v_stack_m297;
    v_stack_m2B8 = v_stack_m218;
    v_stack_m2C0 = v_stack_m78;
    v_stack_m2C8 = (unsigned __int8)(v_stack_m295);
    v_stack_m2D0 = a17;
    v_stack_m2D8 = v_stack_m288;
    v_stack_m2E0 = 0;
    v_stack_m2E8 = v_stack_m280;
    v_stack_m2F0 = (unsigned __int8)(v_stack_m298);
    v_stack_m2F8 = (unsigned int)((unsigned int)(v_stack_m254));
    v_stack_m300 = v_stack_m58;
    v_stack_m308 = (unsigned int)((unsigned int)(v_stack_m278));
    v_stack_m310 = v_stack_m1F8;
    v_stack_m318 = (unsigned int)(v_r15);
    result = SepAccessCheck(v_stack_m260, v_stack_m1A8, v_stack_m1E0, v_stack_m248);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 5147557)) == 0) goto loc_00A1C421;
    if ((*(unsigned int *)(v_stack_m288)) < 0) goto loc_00A1C421;
    if (v_stack_m293 == 0) goto loc_00A1C421;
    if (a17 == 0) goto loc_00A1BF9F;
    result = ExAllocatePool2(256, (unsigned int)(v_stack_m1D0) * 8, (unsigned int)(0x61476553ULL), v_stack_m248);
    v_stack_m268 = result;
    if (result != 0) goto loc_00A1BF91;
loc_00A1BF6D:
    result = SeUnlockSubjectContext(v_stack_m1F0, (unsigned int)(v_stack_m1D0) * 8, (unsigned int)(0x61476553ULL), v_stack_m248);
    result = SeReleaseSubjectContext(v_stack_m1F0, (unsigned int)(v_stack_m1D0) * 8, (unsigned int)(0x61476553ULL), v_stack_m248);
    goto loc_00A1D6F1;
loc_00A1BF91:
    v_stack_m200 = result + (unsigned int)(0xC000009AULL) * 4;
    goto loc_00A1BFBF;
loc_00A1BF9F:
    v_stack_m268 = v_stack_m170;
    v_stack_m200 = v_stack_m16C;
loc_00A1BFBF:
    if ((unsigned int)((unsigned int)(v_stack_m278)) == 0) goto loc_00A1BFF4;
    result = SepCopyObjectTypeList(v_stack_m1F8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m278))), v_stack_m180, v_stack_m248);
    v_stack_m290 = (unsigned int)(result);
    if (sign_flag) goto loc_00A1B7DB;
    goto loc_00A1BFFB;
loc_00A1BFF4:
loc_00A1BFFB:
    v_stack_m24C = 0;
    v_stack_m1C8 = 0;
    if ((*(unsigned int *)(v_stack_m1C0 + 60)) <= 0) goto loc_00A1C3CF;
loc_00A1C025:
    v_stack_m140 = *(unsigned __int64 *)(v_stack_m1C0 + 0 * 8 + 64);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1C0 + 0 * 8 + 64) + 24)) == 0) goto loc_00A1C21C;
    result = v_stack_m1C0;
    if (v_stack_m218 == 0) {
        a2 = v_stack_m218;
        a1 = v_stack_m1B0;
        result = AuthzBasepInitializeResourceClaimsFromSacl(a1, a2, v_stack_m218, v_stack_m248);
        a2 = v_stack_m24C;
        a2 = (unsigned __int8)(a2);
        if (sign_flag) { a2 = (unsigned int)(v_rsi + 1); }
        v_stack_m24C = (unsigned int)(a2);
        a3 = v_stack_m218;
    }
    if (*(unsigned __int64 *)(v_stack_m248 + 1096) == 0) goto loc_00A1C0A4;
    goto loc_00A1C0A7;
loc_00A1C0A4:
loc_00A1C0A7:
    if (*(unsigned __int64 *)(v_stack_m248 + 1096) == 0) goto loc_00A1C0B5;
    goto loc_00A1C0B8;
loc_00A1C0B5:
loc_00A1C0B8:
    if (*(unsigned __int64 *)(v_stack_m248 + 1096) == 0) goto loc_00A1C0C6;
    goto loc_00A1C0C9;
loc_00A1C0C6:
loc_00A1C0C9:
    if (*(unsigned __int64 *)(v_stack_m248 + 1096) == 0) goto loc_00A1C0D7;
    goto loc_00A1C0DA;
loc_00A1C0D7:
loc_00A1C0DA:
    v_stack_m2E0 = v_stack_m224;
    v_stack_m2E8 = 0;
    v_stack_m2F0 = (unsigned __int8)(v_rsi + 1);
    v_stack_m2F8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m1C0 + 0 * 8 + 64) + 16)));
    v_stack_m300 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1C0 + 0 * 8 + 64) + 24);
    v_stack_m308 = 0;
    v_stack_m310 = 0;
    v_stack_m318 = 0;
    result = AuthzBasepEvaluateAceCondition(v_stack_m248, *(unsigned __int64 *)(v_stack_m248 + 776), a3, 0);
    v_stack_m290 = (unsigned int)(result);
    if (v_stack_m224 == ((unsigned int)(v_rsi + 1))) goto loc_00A1C21C;
    if (sign_flag) goto loc_00A1B7DB;
    result = SeTokenIsRestricted(v_stack_m248, *(unsigned __int64 *)(v_stack_m248 + 776), a3, 0);
    if ((unsigned __int8)(result) == 0) goto loc_00A1C204;
    if (*(unsigned __int64 *)(v_stack_m248 + 1096) == 0) goto loc_00A1C170;
    goto loc_00A1C173;
loc_00A1C170:
loc_00A1C173:
    if (*(unsigned __int64 *)(v_stack_m248 + 1096) == 0) goto loc_00A1C181;
    goto loc_00A1C184;
loc_00A1C181:
loc_00A1C184:
    if (*(unsigned __int64 *)(v_stack_m248 + 1096) == 0) goto loc_00A1C192;
    goto loc_00A1C195;
loc_00A1C192:
loc_00A1C195:
    if (*(unsigned __int64 *)(v_stack_m248 + 1096) == 0) goto loc_00A1C1A3;
    goto loc_00A1C1A6;
loc_00A1C1A3:
loc_00A1C1A6:
    v_stack_m2E0 = v_stack_m224;
    v_stack_m2E8 = (unsigned __int8)(v_rsi + 1);
    v_stack_m2F0 = (unsigned __int8)(v_rsi + 1);
    v_stack_m2F8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m1C0 + 0 * 8 + 64) + 16)));
    v_stack_m300 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1C0 + 0 * 8 + 64) + 24);
    v_stack_m308 = 0;
    v_stack_m310 = 0;
    v_stack_m318 = 0;
    result = AuthzBasepEvaluateAceCondition(v_stack_m248, *(unsigned __int64 *)(v_stack_m248 + 776), v_stack_m218, 0);
    v_stack_m290 = (unsigned int)(result);
    if (sign_flag) goto loc_00A1B7DB;
loc_00A1C204:
    if (v_stack_m24C != 0) goto loc_00A1C21C;
    if (v_stack_m224 != ((unsigned int)(v_rsi + 1))) goto loc_00A1C3AD;
loc_00A1C21C:
    if ((((unsigned __int8)(v_rsi + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m1C0 + 0 * 8 + 64) + 48))))) == 0) goto loc_00A1C243;
    if (condition_is_above_or_equal) goto loc_00A1C230;
    goto loc_00A1C23A;
loc_00A1C230:
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m254)) | ((unsigned int)((unsigned int)(a8))));
loc_00A1C23A:
    v_stack_m228 = 0;
    goto loc_00A1C254;
loc_00A1C243:
    v_stack_m228 = (unsigned int)((unsigned int)(v_stack_m254));
loc_00A1C254:
    result = SepBuildCapeSecurityDescriptor(v_stack_mA0, *(unsigned __int64 *)(v_stack_m140 + 32), v_stack_m1B0, 0);
    v_stack_m290 = (unsigned int)(result);
    if (sign_flag) goto loc_00A1B7DB;
    v_stack_m2A8 = v_stack_m26F;
    v_stack_m2B0 = v_stack_m270;
    v_stack_m2B8 = v_stack_m218;
    v_stack_m2C0 = v_stack_m78;
    v_stack_m2C8 = (unsigned __int8)(v_stack_m295);
    v_stack_m2D0 = a17;
    v_stack_m2D8 = v_stack_m200;
    v_stack_m2E0 = 0;
    v_stack_m2E8 = v_stack_m268;
    v_stack_m2F0 = (unsigned __int8)(v_stack_m298);
    v_stack_m2F8 = (unsigned int)((unsigned int)(v_stack_m228));
    v_stack_m300 = v_stack_m58;
    v_stack_m308 = (unsigned int)((unsigned int)(v_stack_m278));
    v_stack_m310 = v_stack_m180;
    v_stack_m318 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a8))));
    result = SepAccessCheck(v_stack_mA0, v_stack_m1A8, v_stack_m1E0, v_stack_m1F0);
    if (v_stack_m294 != 0) goto loc_00A1C379;
    v_stack_m230 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m268)));
    goto loc_00A1C380;
loc_00A1C379:
loc_00A1C380:
    result = (unsigned int)(*(unsigned int *)(v_stack_m268));
    if (v_stack_m180 != 0) {
        a3 = v_stack_m278;
        a2 = v_stack_m180;
        a1 = v_stack_m1F8;
        result = SepMergeObjectTypeListAccesses(a1, a2, a3, v_stack_m1F0);
    }
    v_stack_m294 = (unsigned __int8)(v_rsi + 1);
loc_00A1C3AD:
    result = (unsigned int)(((unsigned int)(v_stack_m1C8)) + ((unsigned int)(v_rsi + 1)));
    v_stack_m1C8 = (unsigned int)(result);
    if (((unsigned int)(result)) < (*(unsigned int *)(v_stack_m1C0 + 60))) goto loc_00A1C025;
loc_00A1C3CF:
    v_stack_m297 = (unsigned __int8)(v_stack_m270);
    v_stack_m296 = (unsigned __int8)(v_stack_m26F);
    if ((unsigned int)((unsigned int)(v_stack_m230)) != 0) goto loc_00A1C435;
    *(unsigned int *)(v_stack_m200) = (unsigned int)((unsigned int)(0xC0000022ULL));
    v_stack_m297 = 0;
    v_stack_m296 = (unsigned __int8)(v_rsi + 1);
    goto loc_00A1C435;
loc_00A1C421:
loc_00A1C435:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a8)))) & (0x2000000ULL));
    if (condition_is_equal) goto loc_00A1C4C6;
    if (v_stack_m238 == 0) goto loc_00A1C473;
    if (v_stack_m62 != 0) goto loc_00A1C4A4;
    if (v_stack_m63 != 0) goto loc_00A1C4A4;
    result = SeIsPermissiveLearningModeEnabled(v_stack_m248, (unsigned int)(0xC0000022ULL), a3, v_stack_m1F0);
    if ((unsigned __int8)(result) == 0) {
        result = a17;
        result = (unsigned __int8)(-(result));
        a1 = (unsigned int)((v_stack_m248) & (v_stack_m210));
        v_stack_m310 = (unsigned int)(a1);
        v_stack_m318 = 0;
        a4 = v_stack_m288;
        a3 = v_stack_m280;
        a2 = (unsigned int)((unsigned int)(a8));
        a1 = v_stack_mD0;
        result = SepConstrainByMandatory(a1, a2, a3, a4);
    }
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00A1CE07;
    result = (unsigned int)(~((unsigned int)(v_stack_m220)));
    goto loc_00A1CE07;
loc_00A1C4C6:
    if (v_stack_m238 == 0) goto loc_00A1CE07;
    if (v_stack_m62 != 0) goto loc_00A1CE07;
    if (v_stack_m63 != 0) goto loc_00A1CE07;
    result = SeIsPermissiveLearningModeEnabled(v_stack_m248, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00A1C536;
    if (v_stack_m6C != 0) goto loc_00A1C536;
loc_00A1C50A:
    v_stack_m61 = (unsigned __int8)(v_rsi + 1);
    v_stack_m297 = (unsigned __int8)(v_rsi + 1);
    v_stack_m296 = 0;
    v_stack_m280 = (unsigned int)((unsigned int)(a8));
    v_stack_m288 = 0;
    goto loc_00A1CE07;
loc_00A1C536:
    v_stack_m297 = 0;
    v_stack_m296 = (unsigned __int8)(v_rsi + 1);
    v_stack_m280 = 0;
    v_stack_m288 = (unsigned int)(a2);
    if (a17 == 0) goto loc_00A1CE0E;
    if (v_stack_m278 <= 0) goto loc_00A1CE0E;
    a2 = (v_stack_m280) - (v_stack_m288);
loc_00A1C581:
    *(unsigned int *)(v_stack_m288 + a2 * 1) = (unsigned int)((unsigned int)(v_stack_m280));
    *(unsigned int *)(v_stack_m288) = (unsigned int)((unsigned int)(v_stack_m288));
    a3 = (v_stack_m148) - (v_rsi + 1);
    if (condition_is_not_equal) goto loc_00A1C581;
    goto loc_00A1CE07;
loc_00A1C5A2:
    if ((unsigned int)((unsigned int)(a8)) != 0) goto loc_00A1C6AB;
    if ((unsigned __int8)(v_stack_m280) == 0) goto loc_00A1C5B9;
    if ((unsigned __int8)(v_stack_m288) == 0) goto loc_00A1C6AB;
loc_00A1C5B9:
    if (((*(unsigned int *)(v_rbx + 200)) & (0x2000ULL)) != 0) goto loc_00A1C5D2;
    if (v_stack_m24C != 0) goto loc_00A1C6AB;
loc_00A1C5D2:
    v_stack_m280 = (unsigned int)((unsigned int)(v_stack_m254));
    if ((unsigned int)((unsigned int)(v_stack_m254)) != 0) goto loc_00A1C5F1;
    goto loc_00A1C5F9;
loc_00A1C5F1:
loc_00A1C5F9:
    v_stack_m297 = (unsigned __int8)((unsigned __int8)(v_rsi + 1));
    v_stack_m296 = 0;
    v_stack_m288 = 0;
    if (a17 == 0) goto loc_00A1C68E;
    result = ExAllocatePool2(256, (unsigned int)(v_stack_m278) * 8, (unsigned int)(0x61476553ULL), a4);
    v_stack_m208 = result;
    if (result == 0) goto loc_00A1BD7D;
    v_stack_m28A = (unsigned __int8)(v_rsi + 1);
    if (v_stack_m278 <= 0) goto loc_00A1CE73;
    a2 = (result) - (result + (unsigned int)(v_stack_m278) * 4);
loc_00A1C66D:
    *(unsigned int *)(result + (unsigned int)(v_stack_m278) * 4 + a2 * 1) = (unsigned int)((unsigned int)(v_stack_m280));
    *(unsigned int *)(result + (unsigned int)(v_stack_m278) * 4) = (unsigned int)((unsigned int)(v_stack_m288));
    v_rbx = ((unsigned int)(v_stack_m278)) - (v_rsi + 1);
    if (condition_is_not_equal) goto loc_00A1C66D;
    goto loc_00A1CE73;
loc_00A1C68E:
    v_stack_m208 = v_stack_m280;
    goto loc_00A1CE73;
loc_00A1C6AB:
    v_stack_m148 = (unsigned int)(v_stack_m1D0);
    if (a17 == 0) goto loc_00A1C701;
    result = ExAllocatePool2(256, (unsigned int)(v_stack_m1D0) * 8, (unsigned int)(0x61476553ULL), a4);
    v_stack_m208 = result;
    if (result == 0) goto loc_00A1BD7D;
    v_stack_m28A = (unsigned __int8)(v_rsi + 1);
    goto loc_00A1C719;
loc_00A1C701:
    v_stack_m208 = v_stack_m280;
loc_00A1C719:
    v_stack_m78 = (unsigned int)((unsigned int)(v_stack_m24C));
    v_stack_m2A8 = v_stack_m296;
    v_stack_m2B0 = v_stack_m297;
    v_stack_m2B8 = v_stack_m218;
    v_stack_m2C0 = v_stack_m78;
    v_stack_m2C8 = (unsigned __int8)(v_stack_m295);
    v_stack_m2D0 = a17;
    v_stack_m2D8 = v_stack_m288;
    v_stack_m2E0 = 0;
    v_stack_m2E8 = v_stack_m280;
    v_stack_m2F0 = (unsigned __int8)(v_stack_m298);
    v_stack_m2F8 = (unsigned int)((unsigned int)(v_stack_m254));
    v_stack_m300 = v_stack_m58;
    v_stack_m308 = (unsigned int)((unsigned int)(v_stack_m278));
    v_stack_m310 = v_stack_m1F8;
    v_stack_m318 = (unsigned int)((unsigned int)(a8));
    result = SepAccessCheck(v_stack_m260, v_stack_m1A8, v_stack_m1E0, v_stack_m248);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 5145297)) == 0) goto loc_00A1CCD4;
    if ((*(unsigned int *)(v_stack_m288)) < 0) goto loc_00A1CCD4;
    if (v_stack_m293 == 0) goto loc_00A1CCD4;
    if (a17 == 0) goto loc_00A1C853;
    result = ExAllocatePool2(256, (unsigned int)(v_stack_m1D0) * 8, (unsigned int)(0x61476553ULL), v_stack_m248);
    v_stack_m268 = result;
    if (result == 0) goto loc_00A1BF6D;
    v_stack_m200 = result + (unsigned int)(v_stack_m1D0) * 4;
    goto loc_00A1C873;
loc_00A1C853:
    v_stack_m268 = v_stack_m170;
    v_stack_m200 = v_stack_m16C;
loc_00A1C873:
    if ((unsigned int)((unsigned int)(v_stack_m278)) == 0) goto loc_00A1C8A7;
    result = SepCopyObjectTypeList(v_stack_m1F8, (unsigned int)((unsigned int)((unsigned int)(v_stack_m278))), v_stack_m180, v_stack_m248);
    v_stack_m290 = (unsigned int)(result);
    if (!sign_flag) goto loc_00A1C8AE;
    goto loc_00A1B7DB;
loc_00A1C8A7:
loc_00A1C8AE:
    v_stack_m220 = 0;
    v_stack_m228 = 0;
    if ((*(unsigned int *)(v_stack_m1C0 + 60)) <= 0) goto loc_00A1CC82;
loc_00A1C8D8:
    v_stack_m140 = *(unsigned __int64 *)(v_stack_m1C0 + 0 * 8 + 64);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1C0 + 0 * 8 + 64) + 24)) == 0) goto loc_00A1CACF;
    result = v_stack_m1C0;
    if (v_stack_m218 == 0) {
        a2 = v_stack_m218;
        a1 = v_stack_m1B0;
        result = AuthzBasepInitializeResourceClaimsFromSacl(a1, a2, v_stack_m218, v_stack_m248);
        a2 = v_stack_m220;
        a2 = (unsigned __int8)(a2);
        if (sign_flag) { a2 = (unsigned int)(v_rsi + 1); }
        v_stack_m220 = (unsigned int)(a2);
        a3 = v_stack_m218;
    }
    if (*(unsigned __int64 *)(v_stack_m248 + 1096) == 0) goto loc_00A1C957;
    goto loc_00A1C95A;
loc_00A1C957:
loc_00A1C95A:
    if (*(unsigned __int64 *)(v_stack_m248 + 1096) == 0) goto loc_00A1C968;
    goto loc_00A1C96B;
loc_00A1C968:
loc_00A1C96B:
    if (*(unsigned __int64 *)(v_stack_m248 + 1096) == 0) goto loc_00A1C979;
    goto loc_00A1C97C;
loc_00A1C979:
loc_00A1C97C:
    if (*(unsigned __int64 *)(v_stack_m248 + 1096) == 0) goto loc_00A1C98A;
    goto loc_00A1C98D;
loc_00A1C98A:
loc_00A1C98D:
    v_stack_m2E0 = v_stack_m224;
    v_stack_m2E8 = 0;
    v_stack_m2F0 = (unsigned __int8)(v_rsi + 1);
    v_stack_m2F8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m1C0 + 0 * 8 + 64) + 16)));
    v_stack_m300 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1C0 + 0 * 8 + 64) + 24);
    v_stack_m308 = 0;
    v_stack_m310 = 0;
    v_stack_m318 = 0;
    result = AuthzBasepEvaluateAceCondition(v_stack_m248, *(unsigned __int64 *)(v_stack_m248 + 776), a3, 0);
    v_stack_m290 = (unsigned int)(result);
    if (v_stack_m224 == ((unsigned int)(v_rsi + 1))) goto loc_00A1CACF;
    if (sign_flag) goto loc_00A1B7DB;
    result = SeTokenIsRestricted(v_stack_m248, *(unsigned __int64 *)(v_stack_m248 + 776), a3, 0);
    if ((unsigned __int8)(result) == 0) goto loc_00A1CAB7;
    if (*(unsigned __int64 *)(v_stack_m248 + 1096) == 0) goto loc_00A1CA23;
    goto loc_00A1CA26;
loc_00A1CA23:
loc_00A1CA26:
    if (*(unsigned __int64 *)(v_stack_m248 + 1096) == 0) goto loc_00A1CA34;
    goto loc_00A1CA37;
loc_00A1CA34:
loc_00A1CA37:
    if (*(unsigned __int64 *)(v_stack_m248 + 1096) == 0) goto loc_00A1CA45;
    goto loc_00A1CA48;
loc_00A1CA45:
loc_00A1CA48:
    if (*(unsigned __int64 *)(v_stack_m248 + 1096) == 0) goto loc_00A1CA56;
    goto loc_00A1CA59;
loc_00A1CA56:
loc_00A1CA59:
    v_stack_m2E0 = v_stack_m224;
    v_stack_m2E8 = (unsigned __int8)(v_rsi + 1);
    v_stack_m2F0 = (unsigned __int8)(v_rsi + 1);
    v_stack_m2F8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m1C0 + 0 * 8 + 64) + 16)));
    v_stack_m300 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m1C0 + 0 * 8 + 64) + 24);
    v_stack_m308 = 0;
    v_stack_m310 = 0;
    v_stack_m318 = 0;
    result = AuthzBasepEvaluateAceCondition(v_stack_m248, *(unsigned __int64 *)(v_stack_m248 + 776), v_stack_m218, 0);
    v_stack_m290 = (unsigned int)(result);
    if (sign_flag) goto loc_00A1B7DB;
loc_00A1CAB7:
    if (v_stack_m220 != 0) goto loc_00A1CACF;
    if (v_stack_m224 != ((unsigned int)(v_rsi + 1))) goto loc_00A1CC60;
loc_00A1CACF:
    if ((((unsigned __int8)(v_rsi + 1)) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m1C0 + 0 * 8 + 64) + 48))))) == 0) goto loc_00A1CAF6;
    if (condition_is_above_or_equal) goto loc_00A1CAE3;
    goto loc_00A1CAED;
loc_00A1CAE3:
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m254)) | ((unsigned int)((unsigned int)(a8))));
loc_00A1CAED:
    v_stack_m1D0 = 0;
    goto loc_00A1CB07;
loc_00A1CAF6:
    v_stack_m1D0 = (unsigned int)((unsigned int)(v_stack_m254));
loc_00A1CB07:
    result = SepBuildCapeSecurityDescriptor(v_stack_mA0, *(unsigned __int64 *)(v_stack_m140 + 32), v_stack_m1B0, 0);
    v_stack_m290 = (unsigned int)(result);
    if (sign_flag) goto loc_00A1B7DB;
    v_stack_m2A8 = v_stack_m26F;
    v_stack_m2B0 = v_stack_m270;
    v_stack_m2B8 = v_stack_m218;
    v_stack_m2C0 = v_stack_m78;
    v_stack_m2C8 = (unsigned __int8)(v_stack_m295);
    v_stack_m2D0 = a17;
    v_stack_m2D8 = v_stack_m200;
    v_stack_m2E0 = 0;
    v_stack_m2E8 = v_stack_m268;
    v_stack_m2F0 = (unsigned __int8)(v_stack_m298);
    v_stack_m2F8 = (unsigned int)((unsigned int)(v_stack_m1D0));
    v_stack_m300 = v_stack_m58;
    v_stack_m308 = (unsigned int)((unsigned int)(v_stack_m278));
    v_stack_m310 = v_stack_m180;
    v_stack_m318 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a8))));
    result = SepAccessCheck(v_stack_mA0, v_stack_m1A8, v_stack_m1E0, v_stack_m1F0);
    if (v_stack_m294 != 0) goto loc_00A1CC2C;
    v_stack_m230 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m268)));
    goto loc_00A1CC33;
loc_00A1CC2C:
loc_00A1CC33:
    result = (unsigned int)(*(unsigned int *)(v_stack_m268));
    if (v_stack_m180 != 0) {
        a3 = v_stack_m278;
        a2 = v_stack_m180;
        a1 = v_stack_m1F8;
        result = SepMergeObjectTypeListAccesses(a1, a2, a3, v_stack_m1F0);
    }
    v_stack_m294 = (unsigned __int8)(v_rsi + 1);
loc_00A1CC60:
    result = (unsigned int)(((unsigned int)(v_stack_m228)) + ((unsigned int)(v_rsi + 1)));
    v_stack_m228 = (unsigned int)(result);
    if (((unsigned int)(result)) < (*(unsigned int *)(v_stack_m1C0 + 60))) goto loc_00A1C8D8;
loc_00A1CC82:
    v_stack_m297 = (unsigned __int8)(v_stack_m270);
    v_stack_m296 = (unsigned __int8)(v_stack_m26F);
    if ((unsigned int)((unsigned int)(v_stack_m230)) != 0) goto loc_00A1CCE8;
    *(unsigned int *)(v_stack_m200) = (unsigned int)((unsigned int)(0xC0000022ULL));
    v_stack_m297 = 0;
    v_stack_m296 = (unsigned __int8)(v_rsi + 1);
    goto loc_00A1CCE8;
loc_00A1CCD4:
loc_00A1CCE8:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a8)))) & (0x2000000ULL));
    if (condition_is_equal) goto loc_00A1CD64;
    if (v_stack_m238 == 0) goto loc_00A1CD2E;
    if (v_stack_m62 != 0) goto loc_00A1CE07;
    if (v_stack_m63 != 0) goto loc_00A1CE07;
    result = SeIsPermissiveLearningModeEnabled(v_stack_m248, (unsigned int)(0xC0000022ULL), a3, v_stack_m1F0);
    if ((unsigned __int8)(result) != 0) goto loc_00A1CE07;
loc_00A1CD2E:
    result = (unsigned __int8)(-(a17));
    a1 = (unsigned int)((v_stack_m248) & (v_stack_m210));
    v_stack_m310 = (unsigned int)(a1);
    v_stack_m318 = 0;
    result = SepConstrainByMandatory(v_stack_mD0, (unsigned int)((unsigned int)((unsigned int)(a8))), v_stack_m280, v_stack_m288);
    goto loc_00A1CE07;
loc_00A1CD64:
    if (v_stack_m238 == 0) goto loc_00A1CE07;
    if (v_stack_m62 != 0) goto loc_00A1CE07;
    if (v_stack_m63 != 0) goto loc_00A1CE07;
    result = SeIsPermissiveLearningModeEnabled(v_stack_m248, (unsigned int)((unsigned int)((unsigned int)(a8))), v_stack_m280, v_stack_m288);
    if ((unsigned __int8)(result) == 0) goto loc_00A1CDA8;
    if (v_stack_m6C == 0) goto loc_00A1C50A;
loc_00A1CDA8:
    v_stack_m297 = 0;
    v_stack_m296 = (unsigned __int8)(v_rsi + 1);
    v_stack_m280 = 0;
    v_stack_m288 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a8))));
    if (a17 == 0) goto loc_00A1CE0E;
    if (v_stack_m278 <= 0) goto loc_00A1CE0E;
    a2 = (v_stack_m280) - (v_stack_m288);
loc_00A1CDEB:
    *(unsigned int *)(v_stack_m288 + a2 * 1) = (unsigned int)((unsigned int)(v_stack_m280));
    *(unsigned int *)(v_stack_m288) = (unsigned int)((unsigned int)(v_stack_m288));
    a3 = (v_stack_m148) - (v_rsi + 1);
    if (condition_is_not_equal) goto loc_00A1CDEB;
loc_00A1CE07:
loc_00A1CE0E:
    result = a17;
    if ((unsigned int)(v_rbx) != 0) {
        result = (unsigned __int8)(-(a17));
        result = v_stack_m284;
        v_stack_m308 = result;
        v_rbx = (unsigned int)((v_rbx) & (v_stack_m210));
        v_stack_m310 = (unsigned int)(v_rbx);
        v_stack_m318 = 0;
        a4 = v_stack_m288;
        a3 = v_stack_m280;
        a2 = (unsigned int)((unsigned int)(a8));
        a1 = v_stack_m1A0;
        result = SepConstrainByConstraintMask(a1, a2, a3, a4);
        a2 = v_stack_m283;
        v_stack_m308 = a2;
        v_stack_m310 = (unsigned int)(v_rbx);
        v_stack_m318 = 0;
        a4 = v_stack_m288;
        a3 = v_stack_m280;
        a2 = (unsigned int)((unsigned int)(a8));
        a1 = v_stack_m160;
        result = SepConstrainByConstraintMask(a1, a2, a3, a4);
    }
    if (v_stack_m248 == 0) goto loc_00A1CF9C;
    if (v_stack_m284 != 0) goto loc_00A1CED4;
    if (v_stack_m283 != 0) goto loc_00A1CED4;
    if (v_stack_m6C != 0) goto loc_00A1CF61;
    if (((*(unsigned int *)(v_stack_m248 + 200)) & (0x4000ULL)) == 0) goto loc_00A1CF61;
    if (sign_flag) goto loc_00A1CF9C;
    if (v_stack_m288 < 0) goto loc_00A1CED4;
    v_rbx = v_stack_m248;
    v_rdi = (unsigned int)(v_stack_m290);
    v_r15 = (unsigned int)(a8);
    if (v_stack_m61 != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a2 = (unsigned __int8)(v_rsi + 1);
        a1 = *(unsigned __int64 *)(v_stack_m248 + 48);
        result = ExAcquireResourceSharedLite(a1, a2, a3, a4);
        v_rbx = (v_stack_m288 >= 0) ? 1 : 0;
        v_rdi = v_stack_m254;
        v_r15 = a8;
        v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(v_r15)));
        a1 = v_stack_m1F0;
        result = SepLocateTokenTrustLevel(a1, a2, a3, a4);
        a4 = result;
        v_stack_m300 = 0;
        v_stack_m308 = (unsigned __int8)(v_rbx);
        v_stack_m310 = (unsigned int)(v_rdi);
        result = v_stack_m260;
        v_stack_m318 = result;
        a3 = 0;
        a2 = 0;
        v_rbx = v_stack_m248;
        a1 = v_rbx;
        result = SeLogAccessFailure(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(v_rbx + 48);
        result = ExReleaseResourceLite(a1, a2, a3, a4);
        result = KeLeaveCriticalRegion(a1, a2, a3, a4);
        v_rdi = v_stack_m290;
    }
    if (sign_flag) goto loc_00A1CF9C;
    if (v_stack_m288 >= 0) goto loc_00A1CF9C;
    if (v_stack_m6C != 0) goto loc_00A1CF9C;
    if (((*(unsigned int *)(v_rbx + 200)) & (0x4000ULL)) == 0) goto loc_00A1CF9C;
    result = SepLpacCausedAccessFailure(v_stack_m78, (unsigned int)((unsigned int)(v_r15)), a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = SepLogLpacAccessFailure(v_stack_m78, (unsigned int)((unsigned int)(v_r15)), a3, a4);
    }
    if (v_stack_m233 != 0) goto loc_00A1D53C;
    if (v_stack_m1CC != 2) goto loc_00A1D04C;
    if ((unsigned __int8)(v_stack_m297) != 0) {
        result = v_stack_m250;
        v_stack_m308 = result;
        v_stack_m310 = 0;
        result = v_stack_m1F0;
        v_stack_m318 = result;
        a4 = 0;
        a3 = (unsigned __int8)(v_stack_m297);
        a2 = v_stack_m188;
        a1 = 0;
        result = SepAdtAuditObjectAccessWithContext(a1, a2, a3, a4);
        v_stack_m28B = (unsigned __int8)(result);
    }
    if ((unsigned __int8)(v_stack_m296) == 0) goto loc_00A1D0A0;
    v_stack_m308 = v_stack_m250;
    v_stack_m310 = 0;
    v_stack_m318 = v_stack_m1F0;
    a3 = 0;
    a1 = 0;
    result = SepAdtAuditObjectAccessWithContext(a1, v_stack_m188, a3, (unsigned __int8)(v_stack_m296));
loc_00A1D043:
    v_stack_m28C = (unsigned __int8)(result);
    goto loc_00A1D0A7;
loc_00A1D04C:
    if (0 != 0) {
        v_stack_m250 = 152;
        a4 = v_stack_m1F0;
        a3 = 0;
        a2 = 0;
        a1 = 152;
        result = SepAdtAuditThisEventWithContext(a1, a2, a3, a4);
        v_stack_m28B = (unsigned __int8)(result);
    }
    if ((unsigned __int8)(v_stack_m296) == 0) goto loc_00A1D0A0;
    v_stack_m250 = 152;
    a2 = 0;
    result = SepAdtAuditThisEventWithContext(152, a2, v_stack_m296, v_stack_m1F0);
    goto loc_00A1D043;
loc_00A1D0A0:
loc_00A1D0A7:
    if ((unsigned __int8)(v_stack_m28B) != 0) goto loc_00A1D0BA;
    if ((unsigned __int8)(v_stack_m28C) == 0) goto loc_00A1D263;
loc_00A1D0BA:
    v_r10 = v_stack_m1E0;
    if (v_stack_m1F0 != 0) { v_r10 = v_stack_m1F0; }
    a3 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_stack_m260 + 2))) & (16));
    if (condition_is_not_equal) goto loc_00A1D0EF;
loc_00A1D0EA:
    goto loc_00A1D10C;
loc_00A1D0EF:
    if (!sign_flag) goto loc_00A1D108;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m260 + 12))) == 0) goto loc_00A1D0EA;
    a2 = ((unsigned int)(*(unsigned int *)(v_stack_m260 + 12))) + (v_stack_m260);
    goto loc_00A1D10C;
loc_00A1D108:
loc_00A1D10C:
    if ((unsigned __int16)(a3) != 0) goto loc_00A1D117;
loc_00A1D112:
    goto loc_00A1D134;
loc_00A1D117:
    if (!sign_flag) goto loc_00A1D130;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m260 + 12))) == 0) goto loc_00A1D112;
    a1 = ((unsigned int)(*(unsigned int *)(v_stack_m260 + 12))) + (v_stack_m260);
    goto loc_00A1D134;
loc_00A1D130:
loc_00A1D134:
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m254)) | ((unsigned int)(v_r15)));
    v_stack_m2D8 = v_stack_m26D;
    v_stack_m2E0 = v_stack_m26E;
    v_stack_m2E8 = (unsigned __int8)(v_stack_m295);
    v_stack_m2F0 = v_stack_m1A8;
    v_stack_m2F8 = v_stack_m280;
    v_stack_m300 = v_stack_m288;
    v_stack_m308 = a17;
    v_stack_m310 = (unsigned int)((unsigned int)(v_stack_m278));
    v_stack_m318 = v_stack_m1F8;
    result = SepExamineSaclEx(*(unsigned __int64 *)(v_stack_m260 + 24), *(unsigned __int64 *)(v_stack_m260 + 24), v_r10, (unsigned int)((unsigned int)(v_rbx)));
    a3 = v_stack_m1E0;
    if (v_stack_m1F0 != 0) { a3 = v_stack_m1F0; }
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_m260 + 2))) & (16)) != 0) goto loc_00A1D1D0;
loc_00A1D1CB:
    goto loc_00A1D1EF;
loc_00A1D1D0:
    if (!sign_flag) goto loc_00A1D1EB;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m260 + 12))) == 0) goto loc_00A1D1CB;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m260 + 12))))) + (v_stack_m260);
    goto loc_00A1D1EF;
loc_00A1D1EB:
loc_00A1D1EF:
    v_stack_m2D8 = v_stack_m26D;
    v_stack_m2E0 = v_stack_m26E;
    v_stack_m2E8 = (unsigned __int8)(v_stack_m295);
    v_stack_m2F0 = v_stack_m1A8;
    v_stack_m2F8 = v_stack_m280;
    v_stack_m300 = v_stack_m288;
    v_stack_m308 = a17;
    v_stack_m310 = (unsigned int)((unsigned int)(v_stack_m278));
    v_stack_m318 = v_stack_m1F8;
    result = SepExamineGlobalSaclEx(v_stack_m188, *(unsigned __int64 *)(v_stack_m260 + 24), a3, (unsigned int)((unsigned int)(v_rbx)));
    goto loc_00A1D273;
loc_00A1D263:
loc_00A1D273:
    if (v_stack_m26E != 0) goto loc_00A1D331;
    if (v_stack_m26D != 0) goto loc_00A1D331;
    if (v_stack_m178 == 0) goto loc_00A1D53C;
    if (v_stack_m297 == 0) goto loc_00A1D53C;
    v_stack_m2F0 = (unsigned __int8)(v_stack_m297);
    v_stack_m2F8 = v_stack_m178;
    v_stack_m300 = (unsigned int)((unsigned int)(a8));
    v_stack_m308 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 464);
    v_stack_m310 = v_stack_m1E0;
    v_stack_m318 = v_stack_m1F0;
    result = SepAdtPrivilegeObjectAuditAlarm(v_stack_m158, v_stack_m188, v_stack_m150, v_stack_m130);
    goto loc_00A1D543;
loc_00A1D331:
    result = (unsigned __int8)((unsigned int)(v_stack_m22C));
    if ((unsigned __int8)(v_stack_m297) != 0) { result = (unsigned int)(v_rsi + 1); }
    v_stack_m22C = (unsigned int)(result);
    if (v_stack_m26E == 0) goto loc_00A1D442;
    if ((unsigned __int8)(v_stack_m188) != 0) {
        result = 0;
        result = (unsigned __int8)(-(result));
        a2 = (v_stack_m188) & (v_stack_m280);
        a1 = (unsigned __int8)(-(v_stack_m297));
        result = v_stack_m130;
        a3 = (v_stack_m150) & (result);
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(result + 184);
        a4 = *(unsigned int *)(v_stack_m280);
        v_stack_m2A8 = 0;
        v_stack_m2B0 = 0;
        v_stack_m2B8 = a2;
        v_stack_m2C0 = (unsigned int)((unsigned int)(v_stack_m278));
        result = v_stack_m1F8;
        v_stack_m2C8 = result;
        v_stack_m2D0 = (unsigned int)((unsigned int)(v_stack_m1CC));
        result = *(unsigned __int64 *)(a1 + 464);
        v_stack_m2D8 = result;
        v_stack_m2E0 = (unsigned __int8)(v_rsi + 1);
        result = v_stack_m178;
        v_stack_m2E8 = result;
        v_stack_m2F0 = (unsigned int)(a4);
        v_stack_m2F8 = (unsigned int)(a4);
        result = v_stack_m1E0;
        v_stack_m300 = result;
        result = v_stack_m1F0;
        v_stack_m308 = result;
        result = v_stack_m260;
        v_stack_m310 = result;
        result = v_stack_m150;
        v_stack_m318 = result;
        a4 = v_stack_m188;
        a2 = v_stack_m158;
        a1 = v_stack_m250;
        result = SepAdtOpenObjectAuditAlarm(a1, a2, a3, a4);
    }
    if (v_stack_m26D == 0) goto loc_00A1D53C;
    if (v_stack_m28C != 0) {
        result = 0;
        result = (unsigned __int8)(-(result));
        a2 = (a2) & (v_stack_m280);
        result = v_stack_m297;
        result = (unsigned __int8)(-(result));
        result = v_stack_m130;
        a3 = (a3) & (result);
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a1 = *(unsigned __int64 *)(result + 184);
        v_stack_m2A8 = 0;
        v_stack_m2B0 = 0;
        v_stack_m2B8 = a2;
        v_stack_m2C0 = (unsigned int)((unsigned int)(v_stack_m278));
        result = v_stack_m1F8;
        v_stack_m2C8 = result;
        v_stack_m2D0 = (unsigned int)((unsigned int)(v_stack_m1CC));
        result = *(unsigned __int64 *)(a1 + 464);
        v_stack_m2D8 = result;
        v_stack_m2E0 = 0;
        result = v_stack_m178;
        v_stack_m2E8 = result;
        result = a8;
        v_stack_m2F0 = (unsigned int)(result);
        v_stack_m2F8 = (unsigned int)(result);
        result = v_stack_m1E0;
        v_stack_m300 = result;
        result = v_stack_m1F0;
        v_stack_m308 = result;
        result = v_stack_m260;
        v_stack_m310 = result;
        result = v_stack_m150;
        v_stack_m318 = result;
        a4 = v_stack_m188;
        a2 = v_stack_m158;
        a1 = v_stack_m250;
        result = SepAdtOpenObjectAuditAlarm(a1, a2, a3, a4);
    }
loc_00A1D543:
    result = SeUnlockSubjectContext(v_stack_m1F0, a2, a3, a4);
    if (a17 == 0) goto loc_00A1D641;
    v_stack_m1B8 = 0;
    if (v_stack_m288 != 0) goto loc_00A1D5DF;
loc_00A1D585:
    v_stack_m1B8 = 0;
    if (0 >= v_stack_m278) goto loc_00A1D69A;
    *(unsigned int *)(v_stack_m198 + 0 * 4) = (unsigned int)((unsigned int)(v_stack_m288));
    *(unsigned int *)(v_stack_m190 + 0 * 4) = (unsigned int)((unsigned int)(v_stack_m280));
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 5141774)) == 0) goto loc_00A1D5DA;
    if ((unsigned __int8)(v_stack_m294) == 0) goto loc_00A1D5DA;
    result = (unsigned int)(v_stack_m288);
    if (!(sign_flag)) {
        *(unsigned int *)(v_stack_m198 + 0 * 4) = (unsigned int)((unsigned int)(v_stack_m288));
        result = v_stack_m280;
    }
    a1 = (unsigned int)((0) + ((unsigned int)(v_rsi + 1)));
    goto loc_00A1D585;
loc_00A1D5DF:
loc_00A1D5E1:
    v_stack_m1B8 = 0;
    if (0 >= v_stack_m278) goto loc_00A1D69A;
    *(unsigned int *)(v_stack_m198 + 0 * 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m288 + 0 * 4)));
    *(unsigned int *)(v_stack_m190 + 0 * 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m280 + 0 * 4)));
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 5141687)) == 0) goto loc_00A1D63C;
    if ((unsigned __int8)(v_stack_m294) == 0) goto loc_00A1D63C;
    result = *(unsigned __int8 *)(v_rip + 5141687);
    if ((*(unsigned int *)(v_stack_m288 + 0 * 4)) >= 0) {
        result = v_stack_m200;
        result = *(unsigned int *)(result + 0 * 4);
        *(unsigned int *)(v_stack_m198 + 0 * 4) = (unsigned int)(result);
        result = v_stack_m268;
        result = *(unsigned int *)(result + 0 * 4);
    }
    a2 = (unsigned int)((0) + ((unsigned int)(v_rsi + 1)));
    goto loc_00A1D5E1;
loc_00A1D641:
    *(unsigned int *)(v_stack_m198) = (unsigned int)((unsigned int)(v_stack_m288));
    *(unsigned int *)(v_stack_m190) = (unsigned int)((unsigned int)(v_stack_m280));
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 5141596)) == 0) goto loc_00A1D69A;
    if (v_stack_m294 == 0) goto loc_00A1D6A2;
    if (v_stack_m288 < 0) goto loc_00A1D6A2;
    *(unsigned int *)(v_stack_m198) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m200)));
    goto loc_00A1D6A2;
loc_00A1D69A:
loc_00A1D6A2:
    *(unsigned __int8 *)(v_stack_mF0) = (unsigned __int8)((unsigned int)(v_stack_m22C));
    v_stack_m290 = 0;
    goto loc_00A1D6F9;
loc_00A1D6E9:
loc_00A1D6EE:
loc_00A1D6F1:
loc_00A1D6F9:
    result = v_stack_mF0;
    if (v_stack_m23C != 0) {
        a1 = v_stack_m128;
        result = ObfDereferenceObject(a1, v_stack_m198, v_stack_m190, v_stack_m198);
        result = v_stack_mE8;
        v_stack_m1F0 = result;
    }
    if (v_stack_m178 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m178, a2, v_stack_m190, v_stack_m198);
    }
    result = SeReleaseSubjectContext(v_stack_m1F0, a2, v_stack_m190, v_stack_m198);
    a3 = 0;
    result = SeReleaseSecurityDescriptor(v_stack_m260, (unsigned __int8)(v_stack_m298), a3, v_stack_m198);
    if (v_stack_m158 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m158, a2, a3, v_stack_m198);
    }
    if (v_stack_m188 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m188, a2, a3, v_stack_m198);
    }
    if (v_stack_m150 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m150, a2, a3, v_stack_m198);
    }
    if (v_stack_m1A8 != 0) {
        a3 = (unsigned __int8)(v_rsi + 1);
        a2 = (unsigned __int8)(v_stack_m298);
        result = SeReleaseSid(v_stack_m1A8, a2, a3, v_stack_m198);
    }
    if (v_stack_m1F8 != 0) {
        result = SeFreeCapturedObjectTypeList(v_stack_m1F8, a2, a3, v_stack_m198);
    }
    if (v_stack_m28A == 0) goto loc_00A1D7E2;
    if (v_stack_m280 != 0) {
        a2 = 0;
        a1 = v_stack_m280;
        result = ExFreePoolWithTag(a1, a2, a3, v_stack_m198);
    }
    if (0 != 0) {
        a2 = 0;
        a1 = 0;
        result = ExFreePoolWithTag(a1, a2, a3, v_stack_m198);
    }
    if (v_stack_m293 != 0) {
        a1 = v_stack_m1C0;
        result = SepRmDereferenceCap(a1, a2, a3, v_stack_m198);
    }
    if (v_stack_m180 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m180, a2, a3, v_stack_m198);
    }
    result = SepFreeResourceInfo(v_stack_m218, a2, a3, v_stack_m198);
    if (((unsigned int)((unsigned int)(0xC000000DULL))) == 0xC000009AULL) goto loc_00A1D82C;
    if (v_stack_m231 != 0) {
        a1 = (unsigned int)((unsigned int)(0xC000000DULL));
        result = SepAuditFailed(a1, a2, a3, v_stack_m198);
    }
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, v_stack_m198);
    v_rsp = (v_rsp) + (768);
    return result;
loc_00A1D859:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, v_stack_m198);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SepAccessCheckAndAuditAlarm(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, uint32_t Arg8, uint32_t Arg9, uint64_t Arg10, int64_t Arg11, uint32_t Arg12, int64_t Arg13, int64_t Arg14, int64_t Arg15, int64_t Arg16, uint8_t Arg17)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint32_t v_stack_m168;
    uint32_t v_stack_m16C;
    uint32_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint32_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint32_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint32_t v_stack_m1C8;
    uint32_t v_stack_m1CC;
    uint32_t v_stack_m1D0;
    uint64_t v_stack_m1E0;
    uint32_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint32_t v_stack_m210;
    uint64_t v_stack_m218;
    uint32_t v_stack_m220;
    uint32_t v_stack_m224;
    uint32_t v_stack_m228;
    uint32_t v_stack_m22C;
    uint32_t v_stack_m230;
    uint8_t v_stack_m231;
    uint8_t v_stack_m233;
    uint8_t v_stack_m234;
    uint32_t v_stack_m238;
    uint8_t v_stack_m23B;
    uint8_t v_stack_m23C;
    uint8_t v_stack_m240;
    uint64_t v_stack_m248;
    uint32_t v_stack_m24C;
    uint16_t v_stack_m250;
    uint32_t v_stack_m254;
    uint8_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint8_t v_stack_m26D;
    uint8_t v_stack_m26E;
    uint8_t v_stack_m26F;
    uint8_t v_stack_m270;
    uint32_t v_stack_m278;
    uint32_t v_stack_m280;
    uint8_t v_stack_m283;
    uint8_t v_stack_m284;
    uint32_t v_stack_m288;
    uint8_t v_stack_m28A;
    uint8_t v_stack_m28B;
    uint8_t v_stack_m28C;
    uint32_t v_stack_m290;
    uint8_t v_stack_m293;
    uint8_t v_stack_m294;
    uint8_t v_stack_m295;
    uint8_t v_stack_m296;
    uint8_t v_stack_m297;
    uint8_t v_stack_m298;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m2B0;
    uint64_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint8_t v_stack_m2C8;
    uint8_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint64_t v_stack_m2E0;
    uint64_t v_stack_m2E8;
    uint8_t v_stack_m2F0;
    uint32_t v_stack_m2F8;
    uint64_t v_stack_m300;
    uint64_t v_stack_m308;
    uint64_t v_stack_m310;
    uint64_t v_stack_m318;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint8_t v_stack_m61;
    uint8_t v_stack_m62;
    uint8_t v_stack_m63;
    uint64_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC4;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_p40;
    uint8_t v_stack_p50;

    local_rsp = (local_rsp) - (768);
    result = (*(uint64_t *)(v_rip + 0x3EF7DA)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m120 = Arg4;
    v_stack_mC0 = Arg1;
    v_stack_m210 = (uint32_t)((uint32_t)(Arg12));
    v_stack_mD8 = Arg16;
    v_stack_m190 = Arg14;
    v_stack_m198 = Arg15;
    v_stack_mA8 = Arg1;
    v_stack_m130 = Arg2;
    v_stack_mB8 = Arg3;
    v_stack_mB0 = Arg4;
    v_stack_m118 = Arg5;
    v_stack_m248 = Arg6;
    v_stack_m148 = Arg6;
    v_stack_m138 = Arg7;
    v_stack_m140 = Arg11;
    v_stack_m278 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg12))));
    v_stack_m1D0 = (uint32_t)((uint32_t)(Arg12));
    v_stack_m100 = Arg14;
    v_stack_mF8 = Arg15;
    v_stack_mF0 = Arg16;
    v_stack_m1F0 = v_xmm0;
    v_stack_m1E0 = v_xmm0;
    local_rsi = 0;
    v_stack_m290 = 0;
    v_stack_m280 = 0;
    v_stack_m28A = 0;
    v_stack_m288 = 0xC0000001ULL;
    v_stack_m170 = 0;
    v_stack_m268 = 0;
    v_stack_m16C = 0;
    v_stack_m200 = 0;
    v_stack_m230 = 0;
    v_stack_m22C = 0;
    v_stack_m240 = 0;
    v_stack_m158 = 0;
    v_stack_m188 = 0;
    v_stack_m150 = 0;
    v_stack_m260 = 0;
    v_stack_m1A8 = 0;
    v_stack_m1F8 = 0;
    v_stack_m254 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m178 = 0;
    v_stack_m297 = 0;
    v_stack_m296 = 0;
    v_stack_m26E = 0;
    v_stack_m26D = 0;
    v_stack_m233 = 0;
    v_stack_m28B = 0;
    v_stack_m28C = 0;
    v_stack_m270 = (uint8_t)(local_rsi + 1);
    v_stack_m26F = 0;
    v_stack_m128 = 0;
    v_stack_mE8 = 0;
    v_stack_m23C = 0;
    v_stack_mD0 = v_xmm0;
    v_stack_m160 = 0;
    v_stack_m1B0 = 0;
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
    v_stack_m80 = 0;
    v_stack_m1C0 = 0;
    v_stack_m293 = 0;
    v_stack_m294 = 0;
    v_stack_m295 = 0;
    v_stack_m231 = 0;
    v_stack_m250 = 999;
    result = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = 0;
    v_stack_m60 = 0;
    v_stack_m238 = 0;
    v_stack_m23B = 0;
    v_stack_m24C = 0;
    v_stack_m218 = 0;
    v_stack_m224 = 0;
    v_stack_m168 = 0;
    v_stack_m234 = 0;
    v_stack_m284 = 0;
    v_stack_m283 = 0;
    v_stack_m180 = 0;
    v_stack_m220 = 0;
    result = (uint32_t)((0) | (0xFFFFFFFFULL));
    v_stack_m1A0 = (uint32_t)(result);
    v_stack_m160 = (uint32_t)(result);
    v_stack_m298 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m258 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    result = SeCaptureSubjectContext(v_stack_m1F0, Arg2, Arg1, Arg14);
    if (Arg9 != 0) goto loc_00A1B2A1;
    v_stack_m1CC = 2;
    goto loc_00A1B2BA;
loc_00A1B2A1:
    if (Arg9 != ((uint32_t)(local_rsi + 1))) goto loc_00A1D6E9;
    v_stack_m1CC = 7;
loc_00A1B2BA:
    if (Arg3 != 0) goto loc_00A1B2E7;
    if (v_stack_m1F0 != 0) goto loc_00A1B2D3;
    goto loc_00A1D6EE;
loc_00A1B2D3:
    if (v_stack_m1E8 >= ((uint32_t)(local_rsi + 1))) goto loc_00A1B2E7;
    goto loc_00A1D6EE;
loc_00A1B2E7:
    if (Arg17 == 0) goto loc_00A1B362;
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg12)))) != 0) goto loc_00A1B311;
loc_00A1B2F6:
    v_stack_m290 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_00A1B3C6;
loc_00A1B311:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg12))))) > 0x1000ULL) goto loc_00A1B2F6;
    result = ProbeForWrite(v_stack_m198, (uint32_t)((uint32_t)((uint32_t)(Arg12))) * 4, 4, Arg14);
    result = ProbeForWrite(v_stack_m190, (uint32_t)((uint32_t)((uint32_t)(Arg12))) * 4, 4, Arg14);
    goto loc_00A1B39C;
loc_00A1B362:
    Arg1 = (uint32_t)((uint32_t)((uint32_t)(Arg12)));
    if (v_stack_m198 < ((uint32_t)((uint32_t)((uint32_t)(Arg12))))) { Arg1 = v_stack_m198; }
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    Arg1 = (uint32_t)((uint32_t)((uint32_t)(Arg12)));
    if (v_stack_m190 < ((uint32_t)((uint32_t)((uint32_t)(Arg12))))) { Arg1 = v_stack_m190; }
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
loc_00A1B39C:
    if ((((uint8_t)((uint32_t)(0xC000000DULL))) & (3)) != 0) goto loc_00A1D859;
    result = (uint32_t)((uint32_t)((uint32_t)(Arg12)));
    if (((uint32_t)(0xC000000DULL)) < ((uint32_t)((uint32_t)((uint32_t)(Arg12))))) { result = (uint32_t)(0xC000000DULL); }
    v_stack_m58 = v_xmm0;
loc_00A1B3C6:
    goto loc_00A1B4B2;
loc_00A1B4B2:
    if (sign_flag) goto loc_00A1B7DB;
    if (Arg3 == 0) goto loc_00A1B557;
    v_stack_mE0 = 0;
    v_stack_m310 = 0;
    v_stack_m318 = v_stack_mE0;
    result = ObReferenceObjectByHandle(*(uint64_t *)(Arg3), 8, *(uint64_t *)(v_rip + 0x5BCB56), (uint8_t)(v_stack_m298));
    v_stack_m128 = v_stack_mE0;
    if (!sign_flag) goto loc_00A1B535;
    v_stack_m128 = 0;
loc_00A1B528:
    goto loc_00A1D6F9;
loc_00A1B535:
    v_stack_mE8 = v_stack_m1F0;
    v_stack_m1F0 = v_stack_mE0;
    v_stack_m23C = (uint8_t)(local_rsi + 1);
    goto loc_00A1B55F;
loc_00A1B557:
loc_00A1B55F:
    result = v_stack_m1E0;
    if (v_stack_m1F0 != 0) { result = v_stack_m1F0; }
    v_stack_m248 = result;
    result = SeCheckAuditPrivilege(v_stack_m1F0, (uint8_t)(v_stack_m298), *(uint64_t *)(v_rip + 0x5BCB56), (uint8_t)(v_stack_m298));
    if ((uint8_t)(result) != 0) goto loc_00A1B5A6;
    if (((v_stack_p50) & ((uint8_t)(local_rsi + 1))) == 0) goto loc_00A1B5BD;
    v_stack_m233 = (uint8_t)(local_rsi + 1);
loc_00A1B5A6:
    if (((Arg8) & (0xF0000000ULL)) == 0) goto loc_00A1B5C7;
    goto loc_00A1B528;
loc_00A1B5BD:
    goto loc_00A1B528;
loc_00A1B5C7:
    v_stack_m318 = v_stack_m260;
    Arg4 = 0;
    result = SeCaptureSecurityDescriptor(v_stack_m268, (uint8_t)(v_stack_m298), (uint32_t)((uint32_t)(local_rsi + 1)), Arg4);
    v_stack_m290 = (uint32_t)(result);
    if (!sign_flag) goto loc_00A1B5FF;
    v_stack_m260 = 0;
    goto loc_00A1B528;
loc_00A1B5FF:
    if (v_stack_m260 != 0) goto loc_00A1B613;
loc_00A1B609:
    goto loc_00A1B528;
loc_00A1B613:
    if (!sign_flag) goto loc_00A1B630;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m260 + 0x4))) == 0) goto loc_00A1B609;
    result = ((uint32_t)(*(uint32_t *)(v_stack_m260 + 0x4))) + (v_stack_m260);
    goto loc_00A1B63C;
loc_00A1B630:
loc_00A1B63C:
    if (*(uint64_t *)(v_stack_m260 + 0x8) == 0) goto loc_00A1B609;
    if (!sign_flag) goto loc_00A1B65A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m260 + 0x8))) == 0) goto loc_00A1B609;
    result = ((uint32_t)(*(uint32_t *)(v_stack_m260 + 0x8))) + (v_stack_m260);
    goto loc_00A1B666;
loc_00A1B65A:
loc_00A1B666:
    if (*(uint64_t *)(v_stack_m260 + 0x10) == 0) goto loc_00A1B609;
    local_r15 = (uint32_t)((uint32_t)((uint32_t)(Arg12)));
    if (v_stack_mF0 < ((uint32_t)((uint32_t)((uint32_t)(Arg12))))) { local_r15 = v_stack_mD8; }
    *(uint8_t *)(local_r15) = (uint8_t)(*(uint8_t *)(local_r15));
    result = SepProbeAndCaptureString_U(v_stack_mC0, v_stack_m158, (uint32_t)((uint32_t)(local_rsi + 1)), Arg4);
    v_stack_m290 = (uint32_t)(result);
    if (sign_flag) goto loc_00A1B6E4;
    result = SepProbeAndCaptureString_U(v_stack_m120, v_stack_m188, (uint32_t)((uint32_t)(local_rsi + 1)), Arg4);
    v_stack_m290 = (uint32_t)(result);
    local_rdi = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        Arg2 = v_stack_m150;
        Arg1 = v_stack_m118;
        result = SepProbeAndCaptureString_U(Arg1, Arg2, (uint32_t)((uint32_t)(local_rsi + 1)), Arg4);
        local_rdi = (uint32_t)(result);
        v_stack_m290 = (uint32_t)(result);
    }
    goto loc_00A1B7A8;
loc_00A1B7A8:
    if (sign_flag) goto loc_00A1B7DB;
    if (v_stack_m138 == 0) goto loc_00A1B7E8;
    v_stack_m308 = v_stack_m1A8;
    v_stack_m310 = (uint8_t)(local_rsi + 1);
    result = SeCaptureSid(v_stack_m138, (uint8_t)(v_stack_m298), (uint32_t)((uint32_t)(local_rsi + 1)), Arg4);
    if (!sign_flag) goto loc_00A1B7E8;
    v_stack_m1A8 = 0;
loc_00A1B7DB:
    goto loc_00A1D6F1;
loc_00A1B7E8:
    result = SeCaptureObjectTypeList(v_stack_m140, (uint32_t)(v_stack_m278), (uint8_t)(v_stack_m268), v_stack_m1F8);
    if (sign_flag) goto loc_00A1B7DB;
    v_stack_m308 = v_stack_m1A0;
    v_stack_m310 = (uint8_t)(local_rsi + 1);
    v_stack_m318 = 0;
    Arg4 = 0;
    result = SepTrustLevelCheck(v_stack_m140, v_stack_m260, v_stack_m1F0, Arg4);
    if (sign_flag) goto loc_00A1B7DB;
    result = SepFilterToDiscretionary(v_stack_m1A0, (uint32_t)((uint32_t)((uint32_t)(Arg8))), v_stack_m1F0, Arg4);
    v_stack_m290 = (uint32_t)(result);
    result = v_stack_m284;
    if (sign_flag) { result = (uint32_t)(local_rsi + 1); }
    v_stack_m284 = (uint8_t)(result);
    if (sign_flag) goto loc_00A1BA4F;
    v_stack_m318 = v_stack_m160;
    result = SepFilterCheck(v_stack_m260, v_stack_m218, v_stack_m248, (uint8_t)(local_rsi + 1));
    if (sign_flag) goto loc_00A1B7DB;
    result = SepFilterToDiscretionary(v_stack_m160, (uint32_t)((uint32_t)((uint32_t)(Arg8))), v_stack_m248, (uint8_t)(local_rsi + 1));
    v_stack_m290 = (uint32_t)(result);
    result = v_stack_m283;
    if (sign_flag) { result = (uint32_t)(local_rsi + 1); }
    v_stack_m283 = (uint8_t)(result);
    if (sign_flag) goto loc_00A1BA4F;
    v_stack_m310 = v_stack_mD0;
    v_stack_m318 = (uint8_t)(local_rsi + 1);
    Arg3 = 0;
    result = SepMandatoryIntegrityCheck(v_stack_m58, v_stack_m260, Arg3, v_stack_m248);
    if (sign_flag) goto loc_00A1B7DB;
    result = SepMandatoryToDiscretionary(v_stack_mD0, (uint32_t)((uint32_t)((uint32_t)(Arg8))), Arg3, v_stack_m248);
    v_stack_m290 = (uint32_t)(result);
    if (sign_flag) goto loc_00A1B94A;
    if (condition_is_above_or_equal) goto loc_00A1B976;
loc_00A1B94A:
    if (((*(uint32_t *)(v_stack_m248 + 0xC8)) & (0x4000ULL)) != 0) {
        result = v_stack_m238;
        result = (uint8_t)(result);
        if (v_stack_mC4 <= 0x2000ULL) { result = (uint32_t)(local_rsi + 1); }
        v_stack_m238 = (uint32_t)(result);
    }
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(v_stack_mD0, (uint32_t)((uint32_t)((uint32_t)(Arg8))), Arg3, v_stack_m248);
    if ((uint32_t)(result) == 0) goto loc_00A1B9DF;
    v_stack_m310 = v_stack_m220;
    v_stack_m318 = (uint32_t)((uint32_t)(Arg8));
    Arg3 = 0;
    result = SepMandatoryAccessCheck(v_stack_m260, v_stack_m1F0, Arg3, (uint8_t)(local_rsi + 1));
    if (sign_flag) goto loc_00A1B9C1;
    result = (uint32_t)(((uint32_t)(v_stack_m220)) & ((uint32_t)((uint32_t)(Arg8))));
    if ((((uint32_t)(result)) & (0xFDFFFFFFULL)) == 0) goto loc_00A1B9DF;
loc_00A1B9C1:
    *(uint32_t *)(v_stack_m190) = 0;
    *(uint32_t *)(v_stack_m198) = (uint32_t)((uint32_t)(0xC00001C0ULL));
    goto loc_00A1B7DB;
loc_00A1B9DF:
    if (!sign_flag) goto loc_00A1B9F0;
    if ((uint8_t)((uint32_t)(v_stack_m238)) == 0) goto loc_00A1BA5F;
loc_00A1B9F0:
    v_stack_m310 = (uint8_t)(v_stack_m298);
    v_stack_m318 = v_stack_m178;
    Arg4 = 0;
    result = SePrivilegePolicyCheck(Arg8, v_stack_m254, v_stack_m1F0, Arg4);
    v_stack_m290 = (uint32_t)(result);
    if ((uint32_t)((uint32_t)(Arg8)) != 0) goto loc_00A1BA5F;
    local_r13 = (uint8_t)((uint32_t)(v_stack_m168));
    if (v_stack_m254 != 0) { local_r13 = (uint32_t)(local_rsi + 1); }
    goto loc_00A1BA5F;
loc_00A1BA4F:
loc_00A1BA5F:
    result = SeLockSubjectContext(v_stack_m1F0, v_stack_m254, v_stack_m1F0, Arg4);
    if (!sign_flag) goto loc_00A1BB23;
    if ((uint8_t)((uint32_t)(v_stack_m238)) != 0) goto loc_00A1BB23;
    v_stack_m296 = (uint8_t)(local_rsi + 1);
    v_stack_m288 = (uint32_t)((uint32_t)((uint32_t)(result)));
    if (Arg17 == ((uint8_t)((uint32_t)(v_stack_m238)))) goto loc_00A1C68E;
    result = ExAllocatePool2(256, (uint32_t)(v_stack_m278) * 8, (uint32_t)(0x61476553ULL), Arg4);
    v_stack_m208 = result;
    if (result != 0) goto loc_00A1BAE0;
    result = SeUnlockSubjectContext(v_stack_m1F0, (uint32_t)(v_stack_m278) * 8, (uint32_t)(0x61476553ULL), Arg4);
    goto loc_00A1B7DB;
loc_00A1BAE0:
    v_stack_m28A = (uint8_t)(local_rsi + 1);
    if (v_stack_m278 <= 0) goto loc_00A1CE73;
    Arg2 = (result) - (result + (uint32_t)(v_stack_m278) * 4);
loc_00A1BB02:
    *(uint32_t *)(Arg2 + result + (uint32_t)(v_stack_m278) * 4 * 1) = (uint32_t)((uint32_t)(v_stack_m280));
    *(uint32_t *)(result + (uint32_t)(v_stack_m278) * 4) = (uint32_t)((uint32_t)(v_stack_m288));
    local_rbx = ((uint32_t)(v_stack_m278)) - (local_rsi + 1);
    if (condition_is_not_equal) goto loc_00A1BB02;
    goto loc_00A1CE73;
loc_00A1BB23:
    result = SepTokenIsOwner(local_rbx, v_stack_m260, (uint32_t)(0x61476553ULL), Arg4);
    v_stack_m295 = (uint8_t)(result);
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x4E8F85)) == 0) goto loc_00A1BB81;
    if ((((uint8_t)(*(uint16_t *)(v_stack_m260 + 0x2))) & (16)) == 0) goto loc_00A1BB79;
    if (((uint8_t)(v_cr8)) >= 2) goto loc_00A1BB79;
    if (!sign_flag) goto loc_00A1BBD4;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m260 + 0xC))) != 0) goto loc_00A1BBCA;
    v_stack_m1B0 = 0;
loc_00A1BB72:
loc_00A1BB79:
loc_00A1BB81:
loc_00A1BB90:
    if ((((uint32_t)((uint32_t)(Arg8))) & (0x2060000ULL)) == 0) goto loc_00A1BCC1;
    if ((uint8_t)(v_stack_m295) == 0) goto loc_00A1BCC1;
    if ((((uint8_t)(*(uint16_t *)(v_stack_m260 + 0x2))) & (4)) != 0) goto loc_00A1BC50;
loc_00A1BBC2:
    goto loc_00A1BC71;
loc_00A1BBCA:
    result = (v_stack_m260) + (v_stack_m260);
    goto loc_00A1BBE0;
loc_00A1BBD4:
loc_00A1BBE0:
    v_stack_m1B0 = *(uint64_t *)(v_stack_m260 + 0x18);
    if (*(uint64_t *)(v_stack_m260 + 0x18) == 0) goto loc_00A1BB72;
    result = SepGetScopedPolicySid(*(uint64_t *)(v_stack_m260 + 0x18), *(uint16_t *)(v_stack_m260 + 0x2), (uint32_t)(0x61476553ULL), Arg4);
    if (result == 0) goto loc_00A1BB72;
    result = SepRmReferenceFindCap(result, v_stack_m1C0, (uint32_t)(0x61476553ULL), Arg4);
    Arg2 = v_stack_m1C0;
    if (sign_flag) { Arg2 = *(uint64_t *)(v_rip + 0x5BC4D0); }
    v_stack_m1C0 = Arg2;
    v_stack_m290 = 0;
    v_stack_m293 = (uint8_t)(local_rsi + 1);
    goto loc_00A1BB90;
loc_00A1BC50:
    if (!sign_flag) goto loc_00A1BC6D;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m260 + 0x10))) == 0) goto loc_00A1BBC2;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_m260 + 0x10))) + (v_stack_m260);
    goto loc_00A1BC71;
loc_00A1BC6D:
loc_00A1BC71:
    result = RtlOwnerAcesPresent(*(uint64_t *)(v_stack_m260 + 0x20), Arg2, (uint32_t)(0x61476553ULL), Arg4);
    if ((uint8_t)(result) != 0) goto loc_00A1BCC1;
    if (condition_is_above_or_equal) goto loc_00A1BC98;
    v_stack_m24C = (uint32_t)((uint32_t)(0x60000ULL));
    result = (uint32_t)(((uint32_t)(v_stack_m254)) | ((uint32_t)((uint32_t)(0x60000ULL))));
    goto loc_00A1BCAB;
loc_00A1BC98:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg8)))) & ((uint32_t)((uint32_t)(0x60000ULL))));
    v_stack_m24C = (uint32_t)(result);
    result = (uint32_t)((result) | (v_stack_m254));
loc_00A1BCAB:
    v_stack_m254 = (uint32_t)(result);
    local_r15 = (uint32_t)(((uint32_t)(Arg8)) & (0xFFF9FFFFULL));
    v_stack_p40 = (uint32_t)(local_r15);
loc_00A1BCC1:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline((uint32_t)(0x60000ULL), Arg2, (uint32_t)(0x61476553ULL), Arg4);
    if ((uint32_t)(result) == 0) goto loc_00A1C5A2;
    if ((uint32_t)(local_r15) != 0) goto loc_00A1BDD7;
    if ((uint8_t)((uint8_t)(local_rsi + 1)) == 0) goto loc_00A1BCE5;
    if ((uint8_t)(result + (uint32_t)(v_stack_m278) * 4) == 0) goto loc_00A1BDD7;
loc_00A1BCE5:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m248 + 0xC8))) & (0x6000ULL));
    if (((uint32_t)(result)) == 0x2000ULL) goto loc_00A1BD04;
    if (v_stack_m24C != 0) goto loc_00A1BDD7;
loc_00A1BD04:
    v_stack_m280 = (uint32_t)((uint32_t)(v_stack_m254));
    if ((uint32_t)((uint32_t)(v_stack_m254)) != 0) goto loc_00A1BD23;
    goto loc_00A1BD2B;
loc_00A1BD23:
loc_00A1BD2B:
    v_stack_m297 = (uint8_t)((uint8_t)(local_rsi + 1));
    v_stack_m296 = 0;
    v_stack_m288 = 0;
    if (Arg17 == 0) goto loc_00A1C68E;
    result = ExAllocatePool2(256, (uint32_t)(v_stack_m278) * 8, (uint32_t)(0x61476553ULL), Arg4);
    v_stack_m208 = result;
    if (result != 0) goto loc_00A1BD94;
loc_00A1BD7D:
    result = SeUnlockSubjectContext(v_stack_m1F0, (uint32_t)(v_stack_m278) * 8, (uint32_t)(0x61476553ULL), Arg4);
    goto loc_00A1B7DB;
loc_00A1BD94:
    v_stack_m28A = (uint8_t)(local_rsi + 1);
    if (v_stack_m278 <= 0) goto loc_00A1CE73;
    Arg2 = (result) - (result + (uint32_t)(v_stack_m278) * 4);
loc_00A1BDB6:
    *(uint32_t *)(result + (uint32_t)(v_stack_m278) * 4 + Arg2 * 1) = (uint32_t)((uint32_t)(v_stack_m280));
    *(uint32_t *)(result + (uint32_t)(v_stack_m278) * 4) = (uint32_t)((uint32_t)(v_stack_m288));
    local_rbx = ((uint32_t)(v_stack_m278)) - (local_rsi + 1);
    if (condition_is_not_equal) goto loc_00A1BDB6;
    goto loc_00A1CE73;
loc_00A1BDD7:
    v_stack_m148 = (uint32_t)(v_stack_m1D0);
    if (Arg17 == 0) goto loc_00A1BE2D;
    result = ExAllocatePool2(256, (uint32_t)(v_stack_m1D0) * 8, (uint32_t)(0x61476553ULL), Arg4);
    v_stack_m208 = result;
    if (result == 0) goto loc_00A1BD7D;
    v_stack_m28A = (uint8_t)(local_rsi + 1);
    goto loc_00A1BE45;
loc_00A1BE2D:
    v_stack_m208 = v_stack_m280;
loc_00A1BE45:
    v_stack_m78 = (uint32_t)((uint32_t)(v_stack_m24C));
    v_stack_m2A8 = v_stack_m296;
    v_stack_m2B0 = v_stack_m297;
    v_stack_m2B8 = v_stack_m218;
    v_stack_m2C0 = v_stack_m78;
    v_stack_m2C8 = (uint8_t)(v_stack_m295);
    v_stack_m2D0 = Arg17;
    v_stack_m2D8 = v_stack_m288;
    v_stack_m2E0 = 0;
    v_stack_m2E8 = v_stack_m280;
    v_stack_m2F0 = (uint8_t)(v_stack_m298);
    v_stack_m2F8 = (uint32_t)((uint32_t)(v_stack_m254));
    v_stack_m300 = v_stack_m58;
    v_stack_m308 = (uint32_t)((uint32_t)(v_stack_m278));
    v_stack_m310 = v_stack_m1F8;
    v_stack_m318 = (uint32_t)(local_r15);
    result = SepAccessCheck(v_stack_m260, v_stack_m1A8, v_stack_m1E0, v_stack_m248);
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x4E8BA5)) == 0) goto loc_00A1C421;
    if ((*(uint32_t *)(v_stack_m288)) < 0) goto loc_00A1C421;
    if (v_stack_m293 == 0) goto loc_00A1C421;
    if (Arg17 == 0) goto loc_00A1BF9F;
    result = ExAllocatePool2(256, (uint32_t)(v_stack_m1D0) * 8, (uint32_t)(0x61476553ULL), v_stack_m248);
    v_stack_m268 = result;
    if (result != 0) goto loc_00A1BF91;
loc_00A1BF6D:
    result = SeUnlockSubjectContext(v_stack_m1F0, (uint32_t)(v_stack_m1D0) * 8, (uint32_t)(0x61476553ULL), v_stack_m248);
    result = SeReleaseSubjectContext(v_stack_m1F0, (uint32_t)(v_stack_m1D0) * 8, (uint32_t)(0x61476553ULL), v_stack_m248);
    goto loc_00A1D6F1;
loc_00A1BF91:
    v_stack_m200 = result + (uint32_t)(0xC000009AULL) * 4;
    goto loc_00A1BFBF;
loc_00A1BF9F:
    v_stack_m268 = v_stack_m170;
    v_stack_m200 = v_stack_m16C;
loc_00A1BFBF:
    if ((uint32_t)((uint32_t)(v_stack_m278)) == 0) goto loc_00A1BFF4;
    result = SepCopyObjectTypeList(v_stack_m1F8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m278))), v_stack_m180, v_stack_m248);
    v_stack_m290 = (uint32_t)(result);
    if (sign_flag) goto loc_00A1B7DB;
    goto loc_00A1BFFB;
loc_00A1BFF4:
loc_00A1BFFB:
    v_stack_m24C = 0;
    v_stack_m1C8 = 0;
    if ((*(uint32_t *)(v_stack_m1C0 + 0x3C)) <= 0) goto loc_00A1C3CF;
loc_00A1C025:
    v_stack_m140 = *(uint64_t *)(v_stack_m1C0 + 0x0 * 8 + 0x40);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m1C0 + 0x0 * 8 + 0x40) + 0x18)) == 0) goto loc_00A1C21C;
    result = v_stack_m1C0;
    if (v_stack_m218 == 0) {
        Arg2 = v_stack_m218;
        Arg1 = v_stack_m1B0;
        result = AuthzBasepInitializeResourceClaimsFromSacl(Arg1, Arg2, v_stack_m218, v_stack_m248);
        Arg2 = v_stack_m24C;
        Arg2 = (uint8_t)(Arg2);
        if (sign_flag) { Arg2 = (uint32_t)(local_rsi + 1); }
        v_stack_m24C = (uint32_t)(Arg2);
        Arg3 = v_stack_m218;
    }
    if (*(uint64_t *)(v_stack_m248 + 0x448) == 0) goto loc_00A1C0A4;
    goto loc_00A1C0A7;
loc_00A1C0A4:
loc_00A1C0A7:
    if (*(uint64_t *)(v_stack_m248 + 0x448) == 0) goto loc_00A1C0B5;
    goto loc_00A1C0B8;
loc_00A1C0B5:
loc_00A1C0B8:
    if (*(uint64_t *)(v_stack_m248 + 0x448) == 0) goto loc_00A1C0C6;
    goto loc_00A1C0C9;
loc_00A1C0C6:
loc_00A1C0C9:
    if (*(uint64_t *)(v_stack_m248 + 0x448) == 0) goto loc_00A1C0D7;
    goto loc_00A1C0DA;
loc_00A1C0D7:
loc_00A1C0DA:
    v_stack_m2E0 = v_stack_m224;
    v_stack_m2E8 = 0;
    v_stack_m2F0 = (uint8_t)(local_rsi + 1);
    v_stack_m2F8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m1C0 + 0x0 * 8 + 0x40) + 0x10)));
    v_stack_m300 = *(uint64_t *)(*(uint64_t *)(v_stack_m1C0 + 0x0 * 8 + 0x40) + 0x18);
    v_stack_m308 = 0;
    v_stack_m310 = 0;
    v_stack_m318 = 0;
    result = AuthzBasepEvaluateAceCondition(v_stack_m248, *(uint64_t *)(v_stack_m248 + 0x308), Arg3, 0);
    v_stack_m290 = (uint32_t)(result);
    if (v_stack_m224 == ((uint32_t)(local_rsi + 1))) goto loc_00A1C21C;
    if (sign_flag) goto loc_00A1B7DB;
    result = SeTokenIsRestricted(v_stack_m248, *(uint64_t *)(v_stack_m248 + 0x308), Arg3, 0);
    if ((uint8_t)(result) == 0) goto loc_00A1C204;
    if (*(uint64_t *)(v_stack_m248 + 0x448) == 0) goto loc_00A1C170;
    goto loc_00A1C173;
loc_00A1C170:
loc_00A1C173:
    if (*(uint64_t *)(v_stack_m248 + 0x448) == 0) goto loc_00A1C181;
    goto loc_00A1C184;
loc_00A1C181:
loc_00A1C184:
    if (*(uint64_t *)(v_stack_m248 + 0x448) == 0) goto loc_00A1C192;
    goto loc_00A1C195;
loc_00A1C192:
loc_00A1C195:
    if (*(uint64_t *)(v_stack_m248 + 0x448) == 0) goto loc_00A1C1A3;
    goto loc_00A1C1A6;
loc_00A1C1A3:
loc_00A1C1A6:
    v_stack_m2E0 = v_stack_m224;
    v_stack_m2E8 = (uint8_t)(local_rsi + 1);
    v_stack_m2F0 = (uint8_t)(local_rsi + 1);
    v_stack_m2F8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m1C0 + 0x0 * 8 + 0x40) + 0x10)));
    v_stack_m300 = *(uint64_t *)(*(uint64_t *)(v_stack_m1C0 + 0x0 * 8 + 0x40) + 0x18);
    v_stack_m308 = 0;
    v_stack_m310 = 0;
    v_stack_m318 = 0;
    result = AuthzBasepEvaluateAceCondition(v_stack_m248, *(uint64_t *)(v_stack_m248 + 0x308), v_stack_m218, 0);
    v_stack_m290 = (uint32_t)(result);
    if (sign_flag) goto loc_00A1B7DB;
loc_00A1C204:
    if (v_stack_m24C != 0) goto loc_00A1C21C;
    if (v_stack_m224 != ((uint32_t)(local_rsi + 1))) goto loc_00A1C3AD;
loc_00A1C21C:
    if ((((uint8_t)(local_rsi + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m1C0 + 0x0 * 8 + 0x40) + 0x30))))) == 0) goto loc_00A1C243;
    if (condition_is_above_or_equal) goto loc_00A1C230;
    goto loc_00A1C23A;
loc_00A1C230:
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m254)) | ((uint32_t)((uint32_t)(Arg8))));
loc_00A1C23A:
    v_stack_m228 = 0;
    goto loc_00A1C254;
loc_00A1C243:
    v_stack_m228 = (uint32_t)((uint32_t)(v_stack_m254));
loc_00A1C254:
    result = SepBuildCapeSecurityDescriptor(v_stack_mA0, *(uint64_t *)(v_stack_m140 + 0x20), v_stack_m1B0, 0);
    v_stack_m290 = (uint32_t)(result);
    if (sign_flag) goto loc_00A1B7DB;
    v_stack_m2A8 = v_stack_m26F;
    v_stack_m2B0 = v_stack_m270;
    v_stack_m2B8 = v_stack_m218;
    v_stack_m2C0 = v_stack_m78;
    v_stack_m2C8 = (uint8_t)(v_stack_m295);
    v_stack_m2D0 = Arg17;
    v_stack_m2D8 = v_stack_m200;
    v_stack_m2E0 = 0;
    v_stack_m2E8 = v_stack_m268;
    v_stack_m2F0 = (uint8_t)(v_stack_m298);
    v_stack_m2F8 = (uint32_t)((uint32_t)(v_stack_m228));
    v_stack_m300 = v_stack_m58;
    v_stack_m308 = (uint32_t)((uint32_t)(v_stack_m278));
    v_stack_m310 = v_stack_m180;
    v_stack_m318 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg8))));
    result = SepAccessCheck(v_stack_mA0, v_stack_m1A8, v_stack_m1E0, v_stack_m1F0);
    if (v_stack_m294 != 0) goto loc_00A1C379;
    v_stack_m230 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m268)));
    goto loc_00A1C380;
loc_00A1C379:
loc_00A1C380:
    result = (uint32_t)(*(uint32_t *)(v_stack_m268));
    if (v_stack_m180 != 0) {
        Arg3 = v_stack_m278;
        Arg2 = v_stack_m180;
        Arg1 = v_stack_m1F8;
        result = SepMergeObjectTypeListAccesses(Arg1, Arg2, Arg3, v_stack_m1F0);
    }
    v_stack_m294 = (uint8_t)(local_rsi + 1);
loc_00A1C3AD:
    result = (uint32_t)(((uint32_t)(v_stack_m1C8)) + ((uint32_t)(local_rsi + 1)));
    v_stack_m1C8 = (uint32_t)(result);
    if (((uint32_t)(result)) < (*(uint32_t *)(v_stack_m1C0 + 0x3C))) goto loc_00A1C025;
loc_00A1C3CF:
    v_stack_m297 = (uint8_t)(v_stack_m270);
    v_stack_m296 = (uint8_t)(v_stack_m26F);
    if ((uint32_t)((uint32_t)(v_stack_m230)) != 0) goto loc_00A1C435;
    *(uint32_t *)(v_stack_m200) = (uint32_t)((uint32_t)(0xC0000022ULL));
    v_stack_m297 = 0;
    v_stack_m296 = (uint8_t)(local_rsi + 1);
    goto loc_00A1C435;
loc_00A1C421:
loc_00A1C435:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg8)))) & (0x2000000ULL));
    if (condition_is_equal) goto loc_00A1C4C6;
    if (v_stack_m238 == 0) goto loc_00A1C473;
    if (v_stack_m62 != 0) goto loc_00A1C4A4;
    if (v_stack_m63 != 0) goto loc_00A1C4A4;
    result = SeIsPermissiveLearningModeEnabled(v_stack_m248, (uint32_t)(0xC0000022ULL), Arg3, v_stack_m1F0);
    if ((uint8_t)(result) == 0) {
        result = Arg17;
        result = (uint8_t)(-(result));
        Arg1 = (uint32_t)((v_stack_m248) & (v_stack_m210));
        v_stack_m310 = (uint32_t)(Arg1);
        v_stack_m318 = 0;
        Arg4 = v_stack_m288;
        Arg3 = v_stack_m280;
        Arg2 = (uint32_t)((uint32_t)(Arg8));
        Arg1 = v_stack_mD0;
        result = SepConstrainByMandatory(Arg1, Arg2, Arg3, Arg4);
    }
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00A1CE07;
    result = (uint32_t)(~((uint32_t)(v_stack_m220)));
    goto loc_00A1CE07;
loc_00A1C4C6:
    if (v_stack_m238 == 0) goto loc_00A1CE07;
    if (v_stack_m62 != 0) goto loc_00A1CE07;
    if (v_stack_m63 != 0) goto loc_00A1CE07;
    result = SeIsPermissiveLearningModeEnabled(v_stack_m248, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00A1C536;
    if (v_stack_m6C != 0) goto loc_00A1C536;
loc_00A1C50A:
    v_stack_m61 = (uint8_t)(local_rsi + 1);
    v_stack_m297 = (uint8_t)(local_rsi + 1);
    v_stack_m296 = 0;
    v_stack_m280 = (uint32_t)((uint32_t)(Arg8));
    v_stack_m288 = 0;
    goto loc_00A1CE07;
loc_00A1C536:
    v_stack_m297 = 0;
    v_stack_m296 = (uint8_t)(local_rsi + 1);
    v_stack_m280 = 0;
    v_stack_m288 = (uint32_t)(Arg2);
    if (Arg17 == 0) goto loc_00A1CE0E;
    if (v_stack_m278 <= 0) goto loc_00A1CE0E;
    Arg2 = (v_stack_m280) - (v_stack_m288);
loc_00A1C581:
    *(uint32_t *)(v_stack_m288 + Arg2 * 1) = (uint32_t)((uint32_t)(v_stack_m280));
    *(uint32_t *)(v_stack_m288) = (uint32_t)((uint32_t)(v_stack_m288));
    Arg3 = (v_stack_m148) - (local_rsi + 1);
    if (condition_is_not_equal) goto loc_00A1C581;
    goto loc_00A1CE07;
loc_00A1C5A2:
    if ((uint32_t)((uint32_t)(Arg8)) != 0) goto loc_00A1C6AB;
    if ((uint8_t)(v_stack_m280) == 0) goto loc_00A1C5B9;
    if ((uint8_t)(v_stack_m288) == 0) goto loc_00A1C6AB;
loc_00A1C5B9:
    if (((*(uint32_t *)(local_rbx + 0xC8)) & (0x2000ULL)) != 0) goto loc_00A1C5D2;
    if (v_stack_m24C != 0) goto loc_00A1C6AB;
loc_00A1C5D2:
    v_stack_m280 = (uint32_t)((uint32_t)(v_stack_m254));
    if ((uint32_t)((uint32_t)(v_stack_m254)) != 0) goto loc_00A1C5F1;
    goto loc_00A1C5F9;
loc_00A1C5F1:
loc_00A1C5F9:
    v_stack_m297 = (uint8_t)((uint8_t)(local_rsi + 1));
    v_stack_m296 = 0;
    v_stack_m288 = 0;
    if (Arg17 == 0) goto loc_00A1C68E;
    result = ExAllocatePool2(256, (uint32_t)(v_stack_m278) * 8, (uint32_t)(0x61476553ULL), Arg4);
    v_stack_m208 = result;
    if (result == 0) goto loc_00A1BD7D;
    v_stack_m28A = (uint8_t)(local_rsi + 1);
    if (v_stack_m278 <= 0) goto loc_00A1CE73;
    Arg2 = (result) - (result + (uint32_t)(v_stack_m278) * 4);
loc_00A1C66D:
    *(uint32_t *)(result + (uint32_t)(v_stack_m278) * 4 + Arg2 * 1) = (uint32_t)((uint32_t)(v_stack_m280));
    *(uint32_t *)(result + (uint32_t)(v_stack_m278) * 4) = (uint32_t)((uint32_t)(v_stack_m288));
    local_rbx = ((uint32_t)(v_stack_m278)) - (local_rsi + 1);
    if (condition_is_not_equal) goto loc_00A1C66D;
    goto loc_00A1CE73;
loc_00A1C68E:
    v_stack_m208 = v_stack_m280;
    goto loc_00A1CE73;
loc_00A1C6AB:
    v_stack_m148 = (uint32_t)(v_stack_m1D0);
    if (Arg17 == 0) goto loc_00A1C701;
    result = ExAllocatePool2(256, (uint32_t)(v_stack_m1D0) * 8, (uint32_t)(0x61476553ULL), Arg4);
    v_stack_m208 = result;
    if (result == 0) goto loc_00A1BD7D;
    v_stack_m28A = (uint8_t)(local_rsi + 1);
    goto loc_00A1C719;
loc_00A1C701:
    v_stack_m208 = v_stack_m280;
loc_00A1C719:
    v_stack_m78 = (uint32_t)((uint32_t)(v_stack_m24C));
    v_stack_m2A8 = v_stack_m296;
    v_stack_m2B0 = v_stack_m297;
    v_stack_m2B8 = v_stack_m218;
    v_stack_m2C0 = v_stack_m78;
    v_stack_m2C8 = (uint8_t)(v_stack_m295);
    v_stack_m2D0 = Arg17;
    v_stack_m2D8 = v_stack_m288;
    v_stack_m2E0 = 0;
    v_stack_m2E8 = v_stack_m280;
    v_stack_m2F0 = (uint8_t)(v_stack_m298);
    v_stack_m2F8 = (uint32_t)((uint32_t)(v_stack_m254));
    v_stack_m300 = v_stack_m58;
    v_stack_m308 = (uint32_t)((uint32_t)(v_stack_m278));
    v_stack_m310 = v_stack_m1F8;
    v_stack_m318 = (uint32_t)((uint32_t)(Arg8));
    result = SepAccessCheck(v_stack_m260, v_stack_m1A8, v_stack_m1E0, v_stack_m248);
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x4E82D1)) == 0) goto loc_00A1CCD4;
    if ((*(uint32_t *)(v_stack_m288)) < 0) goto loc_00A1CCD4;
    if (v_stack_m293 == 0) goto loc_00A1CCD4;
    if (Arg17 == 0) goto loc_00A1C853;
    result = ExAllocatePool2(256, (uint32_t)(v_stack_m1D0) * 8, (uint32_t)(0x61476553ULL), v_stack_m248);
    v_stack_m268 = result;
    if (result == 0) goto loc_00A1BF6D;
    v_stack_m200 = result + (uint32_t)(v_stack_m1D0) * 4;
    goto loc_00A1C873;
loc_00A1C853:
    v_stack_m268 = v_stack_m170;
    v_stack_m200 = v_stack_m16C;
loc_00A1C873:
    if ((uint32_t)((uint32_t)(v_stack_m278)) == 0) goto loc_00A1C8A7;
    result = SepCopyObjectTypeList(v_stack_m1F8, (uint32_t)((uint32_t)((uint32_t)(v_stack_m278))), v_stack_m180, v_stack_m248);
    v_stack_m290 = (uint32_t)(result);
    if (!sign_flag) goto loc_00A1C8AE;
    goto loc_00A1B7DB;
loc_00A1C8A7:
loc_00A1C8AE:
    v_stack_m220 = 0;
    v_stack_m228 = 0;
    if ((*(uint32_t *)(v_stack_m1C0 + 0x3C)) <= 0) goto loc_00A1CC82;
loc_00A1C8D8:
    v_stack_m140 = *(uint64_t *)(v_stack_m1C0 + 0x0 * 8 + 0x40);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m1C0 + 0x0 * 8 + 0x40) + 0x18)) == 0) goto loc_00A1CACF;
    result = v_stack_m1C0;
    if (v_stack_m218 == 0) {
        Arg2 = v_stack_m218;
        Arg1 = v_stack_m1B0;
        result = AuthzBasepInitializeResourceClaimsFromSacl(Arg1, Arg2, v_stack_m218, v_stack_m248);
        Arg2 = v_stack_m220;
        Arg2 = (uint8_t)(Arg2);
        if (sign_flag) { Arg2 = (uint32_t)(local_rsi + 1); }
        v_stack_m220 = (uint32_t)(Arg2);
        Arg3 = v_stack_m218;
    }
    if (*(uint64_t *)(v_stack_m248 + 0x448) == 0) goto loc_00A1C957;
    goto loc_00A1C95A;
loc_00A1C957:
loc_00A1C95A:
    if (*(uint64_t *)(v_stack_m248 + 0x448) == 0) goto loc_00A1C968;
    goto loc_00A1C96B;
loc_00A1C968:
loc_00A1C96B:
    if (*(uint64_t *)(v_stack_m248 + 0x448) == 0) goto loc_00A1C979;
    goto loc_00A1C97C;
loc_00A1C979:
loc_00A1C97C:
    if (*(uint64_t *)(v_stack_m248 + 0x448) == 0) goto loc_00A1C98A;
    goto loc_00A1C98D;
loc_00A1C98A:
loc_00A1C98D:
    v_stack_m2E0 = v_stack_m224;
    v_stack_m2E8 = 0;
    v_stack_m2F0 = (uint8_t)(local_rsi + 1);
    v_stack_m2F8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m1C0 + 0x0 * 8 + 0x40) + 0x10)));
    v_stack_m300 = *(uint64_t *)(*(uint64_t *)(v_stack_m1C0 + 0x0 * 8 + 0x40) + 0x18);
    v_stack_m308 = 0;
    v_stack_m310 = 0;
    v_stack_m318 = 0;
    result = AuthzBasepEvaluateAceCondition(v_stack_m248, *(uint64_t *)(v_stack_m248 + 0x308), Arg3, 0);
    v_stack_m290 = (uint32_t)(result);
    if (v_stack_m224 == ((uint32_t)(local_rsi + 1))) goto loc_00A1CACF;
    if (sign_flag) goto loc_00A1B7DB;
    result = SeTokenIsRestricted(v_stack_m248, *(uint64_t *)(v_stack_m248 + 0x308), Arg3, 0);
    if ((uint8_t)(result) == 0) goto loc_00A1CAB7;
    if (*(uint64_t *)(v_stack_m248 + 0x448) == 0) goto loc_00A1CA23;
    goto loc_00A1CA26;
loc_00A1CA23:
loc_00A1CA26:
    if (*(uint64_t *)(v_stack_m248 + 0x448) == 0) goto loc_00A1CA34;
    goto loc_00A1CA37;
loc_00A1CA34:
loc_00A1CA37:
    if (*(uint64_t *)(v_stack_m248 + 0x448) == 0) goto loc_00A1CA45;
    goto loc_00A1CA48;
loc_00A1CA45:
loc_00A1CA48:
    if (*(uint64_t *)(v_stack_m248 + 0x448) == 0) goto loc_00A1CA56;
    goto loc_00A1CA59;
loc_00A1CA56:
loc_00A1CA59:
    v_stack_m2E0 = v_stack_m224;
    v_stack_m2E8 = (uint8_t)(local_rsi + 1);
    v_stack_m2F0 = (uint8_t)(local_rsi + 1);
    v_stack_m2F8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m1C0 + 0x0 * 8 + 0x40) + 0x10)));
    v_stack_m300 = *(uint64_t *)(*(uint64_t *)(v_stack_m1C0 + 0x0 * 8 + 0x40) + 0x18);
    v_stack_m308 = 0;
    v_stack_m310 = 0;
    v_stack_m318 = 0;
    result = AuthzBasepEvaluateAceCondition(v_stack_m248, *(uint64_t *)(v_stack_m248 + 0x308), v_stack_m218, 0);
    v_stack_m290 = (uint32_t)(result);
    if (sign_flag) goto loc_00A1B7DB;
loc_00A1CAB7:
    if (v_stack_m220 != 0) goto loc_00A1CACF;
    if (v_stack_m224 != ((uint32_t)(local_rsi + 1))) goto loc_00A1CC60;
loc_00A1CACF:
    if ((((uint8_t)(local_rsi + 1)) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m1C0 + 0x0 * 8 + 0x40) + 0x30))))) == 0) goto loc_00A1CAF6;
    if (condition_is_above_or_equal) goto loc_00A1CAE3;
    goto loc_00A1CAED;
loc_00A1CAE3:
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m254)) | ((uint32_t)((uint32_t)(Arg8))));
loc_00A1CAED:
    v_stack_m1D0 = 0;
    goto loc_00A1CB07;
loc_00A1CAF6:
    v_stack_m1D0 = (uint32_t)((uint32_t)(v_stack_m254));
loc_00A1CB07:
    result = SepBuildCapeSecurityDescriptor(v_stack_mA0, *(uint64_t *)(v_stack_m140 + 0x20), v_stack_m1B0, 0);
    v_stack_m290 = (uint32_t)(result);
    if (sign_flag) goto loc_00A1B7DB;
    v_stack_m2A8 = v_stack_m26F;
    v_stack_m2B0 = v_stack_m270;
    v_stack_m2B8 = v_stack_m218;
    v_stack_m2C0 = v_stack_m78;
    v_stack_m2C8 = (uint8_t)(v_stack_m295);
    v_stack_m2D0 = Arg17;
    v_stack_m2D8 = v_stack_m200;
    v_stack_m2E0 = 0;
    v_stack_m2E8 = v_stack_m268;
    v_stack_m2F0 = (uint8_t)(v_stack_m298);
    v_stack_m2F8 = (uint32_t)((uint32_t)(v_stack_m1D0));
    v_stack_m300 = v_stack_m58;
    v_stack_m308 = (uint32_t)((uint32_t)(v_stack_m278));
    v_stack_m310 = v_stack_m180;
    v_stack_m318 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg8))));
    result = SepAccessCheck(v_stack_mA0, v_stack_m1A8, v_stack_m1E0, v_stack_m1F0);
    if (v_stack_m294 != 0) goto loc_00A1CC2C;
    v_stack_m230 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m268)));
    goto loc_00A1CC33;
loc_00A1CC2C:
loc_00A1CC33:
    result = (uint32_t)(*(uint32_t *)(v_stack_m268));
    if (v_stack_m180 != 0) {
        Arg3 = v_stack_m278;
        Arg2 = v_stack_m180;
        Arg1 = v_stack_m1F8;
        result = SepMergeObjectTypeListAccesses(Arg1, Arg2, Arg3, v_stack_m1F0);
    }
    v_stack_m294 = (uint8_t)(local_rsi + 1);
loc_00A1CC60:
    result = (uint32_t)(((uint32_t)(v_stack_m228)) + ((uint32_t)(local_rsi + 1)));
    v_stack_m228 = (uint32_t)(result);
    if (((uint32_t)(result)) < (*(uint32_t *)(v_stack_m1C0 + 0x3C))) goto loc_00A1C8D8;
loc_00A1CC82:
    v_stack_m297 = (uint8_t)(v_stack_m270);
    v_stack_m296 = (uint8_t)(v_stack_m26F);
    if ((uint32_t)((uint32_t)(v_stack_m230)) != 0) goto loc_00A1CCE8;
    *(uint32_t *)(v_stack_m200) = (uint32_t)((uint32_t)(0xC0000022ULL));
    v_stack_m297 = 0;
    v_stack_m296 = (uint8_t)(local_rsi + 1);
    goto loc_00A1CCE8;
loc_00A1CCD4:
loc_00A1CCE8:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg8)))) & (0x2000000ULL));
    if (condition_is_equal) goto loc_00A1CD64;
    if (v_stack_m238 == 0) goto loc_00A1CD2E;
    if (v_stack_m62 != 0) goto loc_00A1CE07;
    if (v_stack_m63 != 0) goto loc_00A1CE07;
    result = SeIsPermissiveLearningModeEnabled(v_stack_m248, (uint32_t)(0xC0000022ULL), Arg3, v_stack_m1F0);
    if ((uint8_t)(result) != 0) goto loc_00A1CE07;
loc_00A1CD2E:
    result = (uint8_t)(-(Arg17));
    Arg1 = (uint32_t)((v_stack_m248) & (v_stack_m210));
    v_stack_m310 = (uint32_t)(Arg1);
    v_stack_m318 = 0;
    result = SepConstrainByMandatory(v_stack_mD0, (uint32_t)((uint32_t)((uint32_t)(Arg8))), v_stack_m280, v_stack_m288);
    goto loc_00A1CE07;
loc_00A1CD64:
    if (v_stack_m238 == 0) goto loc_00A1CE07;
    if (v_stack_m62 != 0) goto loc_00A1CE07;
    if (v_stack_m63 != 0) goto loc_00A1CE07;
    result = SeIsPermissiveLearningModeEnabled(v_stack_m248, (uint32_t)((uint32_t)((uint32_t)(Arg8))), v_stack_m280, v_stack_m288);
    if ((uint8_t)(result) == 0) goto loc_00A1CDA8;
    if (v_stack_m6C == 0) goto loc_00A1C50A;
loc_00A1CDA8:
    v_stack_m297 = 0;
    v_stack_m296 = (uint8_t)(local_rsi + 1);
    v_stack_m280 = 0;
    v_stack_m288 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg8))));
    if (Arg17 == 0) goto loc_00A1CE0E;
    if (v_stack_m278 <= 0) goto loc_00A1CE0E;
    Arg2 = (v_stack_m280) - (v_stack_m288);
loc_00A1CDEB:
    *(uint32_t *)(v_stack_m288 + Arg2 * 1) = (uint32_t)((uint32_t)(v_stack_m280));
    *(uint32_t *)(v_stack_m288) = (uint32_t)((uint32_t)(v_stack_m288));
    Arg3 = (v_stack_m148) - (local_rsi + 1);
    if (condition_is_not_equal) goto loc_00A1CDEB;
loc_00A1CE07:
loc_00A1CE0E:
    result = Arg17;
    if ((uint32_t)(local_rbx) != 0) {
        result = (uint8_t)(-(Arg17));
        result = v_stack_m284;
        v_stack_m308 = result;
        local_rbx = (uint32_t)((local_rbx) & (v_stack_m210));
        v_stack_m310 = (uint32_t)(local_rbx);
        v_stack_m318 = 0;
        Arg4 = v_stack_m288;
        Arg3 = v_stack_m280;
        Arg2 = (uint32_t)((uint32_t)(Arg8));
        Arg1 = v_stack_m1A0;
        result = SepConstrainByConstraintMask(Arg1, Arg2, Arg3, Arg4);
        Arg2 = v_stack_m283;
        v_stack_m308 = Arg2;
        v_stack_m310 = (uint32_t)(local_rbx);
        v_stack_m318 = 0;
        Arg4 = v_stack_m288;
        Arg3 = v_stack_m280;
        Arg2 = (uint32_t)((uint32_t)(Arg8));
        Arg1 = v_stack_m160;
        result = SepConstrainByConstraintMask(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m248 == 0) goto loc_00A1CF9C;
    if (v_stack_m284 != 0) goto loc_00A1CED4;
    if (v_stack_m283 != 0) goto loc_00A1CED4;
    if (v_stack_m6C != 0) goto loc_00A1CF61;
    if (((*(uint32_t *)(v_stack_m248 + 0xC8)) & (0x4000ULL)) == 0) goto loc_00A1CF61;
    if (sign_flag) goto loc_00A1CF9C;
    if (v_stack_m288 < 0) goto loc_00A1CED4;
    local_rbx = v_stack_m248;
    local_rdi = (uint32_t)(v_stack_m290);
    local_r15 = (uint32_t)(Arg8);
    if (v_stack_m61 != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg2 = (uint8_t)(local_rsi + 1);
        Arg1 = *(uint64_t *)(v_stack_m248 + 0x30);
        result = ExAcquireResourceSharedLite(Arg1, Arg2, Arg3, Arg4);
        local_rbx = (v_stack_m288 >= 0) ? 1 : 0;
        local_rdi = v_stack_m254;
        local_r15 = Arg8;
        local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(local_r15)));
        Arg1 = v_stack_m1F0;
        result = SepLocateTokenTrustLevel(Arg1, Arg2, Arg3, Arg4);
        Arg4 = result;
        v_stack_m300 = 0;
        v_stack_m308 = (uint8_t)(local_rbx);
        v_stack_m310 = (uint32_t)(local_rdi);
        result = v_stack_m260;
        v_stack_m318 = result;
        Arg3 = 0;
        Arg2 = 0;
        local_rbx = v_stack_m248;
        Arg1 = local_rbx;
        result = SeLogAccessFailure(Arg1, Arg2, Arg3, Arg4);
        Arg1 = *(uint64_t *)(local_rbx + 0x30);
        result = ExReleaseResourceLite(Arg1, Arg2, Arg3, Arg4);
        result = KeLeaveCriticalRegion(Arg1, Arg2, Arg3, Arg4);
        local_rdi = v_stack_m290;
    }
    if (sign_flag) goto loc_00A1CF9C;
    if (v_stack_m288 >= 0) goto loc_00A1CF9C;
    if (v_stack_m6C != 0) goto loc_00A1CF9C;
    if (((*(uint32_t *)(local_rbx + 0xC8)) & (0x4000ULL)) == 0) goto loc_00A1CF9C;
    result = SepLpacCausedAccessFailure(v_stack_m78, (uint32_t)((uint32_t)(local_r15)), Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = SepLogLpacAccessFailure(v_stack_m78, (uint32_t)((uint32_t)(local_r15)), Arg3, Arg4);
    }
    if (v_stack_m233 != 0) goto loc_00A1D53C;
    if (v_stack_m1CC != 2) goto loc_00A1D04C;
    if ((uint8_t)(v_stack_m297) != 0) {
        result = v_stack_m250;
        v_stack_m308 = result;
        v_stack_m310 = 0;
        result = v_stack_m1F0;
        v_stack_m318 = result;
        Arg4 = 0;
        Arg3 = (uint8_t)(v_stack_m297);
        Arg2 = v_stack_m188;
        Arg1 = 0;
        result = SepAdtAuditObjectAccessWithContext(Arg1, Arg2, Arg3, Arg4);
        v_stack_m28B = (uint8_t)(result);
    }
    if ((uint8_t)(v_stack_m296) == 0) goto loc_00A1D0A0;
    v_stack_m308 = v_stack_m250;
    v_stack_m310 = 0;
    v_stack_m318 = v_stack_m1F0;
    Arg3 = 0;
    Arg1 = 0;
    result = SepAdtAuditObjectAccessWithContext(Arg1, v_stack_m188, Arg3, (uint8_t)(v_stack_m296));
loc_00A1D043:
    v_stack_m28C = (uint8_t)(result);
    goto loc_00A1D0A7;
loc_00A1D04C:
    if (0 != 0) {
        v_stack_m250 = 152;
        Arg4 = v_stack_m1F0;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = 152;
        result = SepAdtAuditThisEventWithContext(Arg1, Arg2, Arg3, Arg4);
        v_stack_m28B = (uint8_t)(result);
    }
    if ((uint8_t)(v_stack_m296) == 0) goto loc_00A1D0A0;
    v_stack_m250 = 152;
    Arg2 = 0;
    result = SepAdtAuditThisEventWithContext(152, Arg2, v_stack_m296, v_stack_m1F0);
    goto loc_00A1D043;
loc_00A1D0A0:
loc_00A1D0A7:
    if ((uint8_t)(v_stack_m28B) != 0) goto loc_00A1D0BA;
    if ((uint8_t)(v_stack_m28C) == 0) goto loc_00A1D263;
loc_00A1D0BA:
    local_r10 = v_stack_m1E0;
    if (v_stack_m1F0 != 0) { local_r10 = v_stack_m1F0; }
    Arg3 = (uint16_t)(((uint16_t)(*(uint16_t *)(v_stack_m260 + 0x2))) & (16));
    if (condition_is_not_equal) goto loc_00A1D0EF;
loc_00A1D0EA:
    goto loc_00A1D10C;
loc_00A1D0EF:
    if (!sign_flag) goto loc_00A1D108;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m260 + 0xC))) == 0) goto loc_00A1D0EA;
    Arg2 = ((uint32_t)(*(uint32_t *)(v_stack_m260 + 0xC))) + (v_stack_m260);
    goto loc_00A1D10C;
loc_00A1D108:
loc_00A1D10C:
    if ((uint16_t)(Arg3) != 0) goto loc_00A1D117;
loc_00A1D112:
    goto loc_00A1D134;
loc_00A1D117:
    if (!sign_flag) goto loc_00A1D130;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m260 + 0xC))) == 0) goto loc_00A1D112;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_stack_m260 + 0xC))) + (v_stack_m260);
    goto loc_00A1D134;
loc_00A1D130:
loc_00A1D134:
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m254)) | ((uint32_t)(local_r15)));
    v_stack_m2D8 = v_stack_m26D;
    v_stack_m2E0 = v_stack_m26E;
    v_stack_m2E8 = (uint8_t)(v_stack_m295);
    v_stack_m2F0 = v_stack_m1A8;
    v_stack_m2F8 = v_stack_m280;
    v_stack_m300 = v_stack_m288;
    v_stack_m308 = Arg17;
    v_stack_m310 = (uint32_t)((uint32_t)(v_stack_m278));
    v_stack_m318 = v_stack_m1F8;
    result = SepExamineSaclEx(*(uint64_t *)(v_stack_m260 + 0x18), *(uint64_t *)(v_stack_m260 + 0x18), local_r10, (uint32_t)((uint32_t)(local_rbx)));
    Arg3 = v_stack_m1E0;
    if (v_stack_m1F0 != 0) { Arg3 = v_stack_m1F0; }
    if ((((uint8_t)(*(uint16_t *)(v_stack_m260 + 0x2))) & (16)) != 0) goto loc_00A1D1D0;
loc_00A1D1CB:
    goto loc_00A1D1EF;
loc_00A1D1D0:
    if (!sign_flag) goto loc_00A1D1EB;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m260 + 0xC))) == 0) goto loc_00A1D1CB;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m260 + 0xC))))) + (v_stack_m260);
    goto loc_00A1D1EF;
loc_00A1D1EB:
loc_00A1D1EF:
    v_stack_m2D8 = v_stack_m26D;
    v_stack_m2E0 = v_stack_m26E;
    v_stack_m2E8 = (uint8_t)(v_stack_m295);
    v_stack_m2F0 = v_stack_m1A8;
    v_stack_m2F8 = v_stack_m280;
    v_stack_m300 = v_stack_m288;
    v_stack_m308 = Arg17;
    v_stack_m310 = (uint32_t)((uint32_t)(v_stack_m278));
    v_stack_m318 = v_stack_m1F8;
    result = SepExamineGlobalSaclEx(v_stack_m188, *(uint64_t *)(v_stack_m260 + 0x18), Arg3, (uint32_t)((uint32_t)(local_rbx)));
    goto loc_00A1D273;
loc_00A1D263:
loc_00A1D273:
    if (v_stack_m26E != 0) goto loc_00A1D331;
    if (v_stack_m26D != 0) goto loc_00A1D331;
    if (v_stack_m178 == 0) goto loc_00A1D53C;
    if (v_stack_m297 == 0) goto loc_00A1D53C;
    v_stack_m2F0 = (uint8_t)(v_stack_m297);
    v_stack_m2F8 = v_stack_m178;
    v_stack_m300 = (uint32_t)((uint32_t)(Arg8));
    v_stack_m308 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x1D0);
    v_stack_m310 = v_stack_m1E0;
    v_stack_m318 = v_stack_m1F0;
    result = SepAdtPrivilegeObjectAuditAlarm(v_stack_m158, v_stack_m188, v_stack_m150, v_stack_m130);
    goto loc_00A1D543;
loc_00A1D331:
    result = (uint8_t)((uint32_t)(v_stack_m22C));
    if ((uint8_t)(v_stack_m297) != 0) { result = (uint32_t)(local_rsi + 1); }
    v_stack_m22C = (uint32_t)(result);
    if (v_stack_m26E == 0) goto loc_00A1D442;
    if ((uint8_t)(v_stack_m188) != 0) {
        result = 0;
        result = (uint8_t)(-(result));
        Arg2 = (v_stack_m188) & (v_stack_m280);
        Arg1 = (uint8_t)(-(v_stack_m297));
        result = v_stack_m130;
        Arg3 = (v_stack_m150) & (result);
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(result + 0xB8);
        Arg4 = *(uint32_t *)(v_stack_m280);
        v_stack_m2A8 = 0;
        v_stack_m2B0 = 0;
        v_stack_m2B8 = Arg2;
        v_stack_m2C0 = (uint32_t)((uint32_t)(v_stack_m278));
        result = v_stack_m1F8;
        v_stack_m2C8 = result;
        v_stack_m2D0 = (uint32_t)((uint32_t)(v_stack_m1CC));
        result = *(uint64_t *)(Arg1 + 0x1D0);
        v_stack_m2D8 = result;
        v_stack_m2E0 = (uint8_t)(local_rsi + 1);
        result = v_stack_m178;
        v_stack_m2E8 = result;
        v_stack_m2F0 = (uint32_t)(Arg4);
        v_stack_m2F8 = (uint32_t)(Arg4);
        result = v_stack_m1E0;
        v_stack_m300 = result;
        result = v_stack_m1F0;
        v_stack_m308 = result;
        result = v_stack_m260;
        v_stack_m310 = result;
        result = v_stack_m150;
        v_stack_m318 = result;
        Arg4 = v_stack_m188;
        Arg2 = v_stack_m158;
        Arg1 = v_stack_m250;
        result = SepAdtOpenObjectAuditAlarm(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m26D == 0) goto loc_00A1D53C;
    if (v_stack_m28C != 0) {
        result = 0;
        result = (uint8_t)(-(result));
        Arg2 = (Arg2) & (v_stack_m280);
        result = v_stack_m297;
        result = (uint8_t)(-(result));
        result = v_stack_m130;
        Arg3 = (Arg3) & (result);
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg1 = *(uint64_t *)(result + 0xB8);
        v_stack_m2A8 = 0;
        v_stack_m2B0 = 0;
        v_stack_m2B8 = Arg2;
        v_stack_m2C0 = (uint32_t)((uint32_t)(v_stack_m278));
        result = v_stack_m1F8;
        v_stack_m2C8 = result;
        v_stack_m2D0 = (uint32_t)((uint32_t)(v_stack_m1CC));
        result = *(uint64_t *)(Arg1 + 0x1D0);
        v_stack_m2D8 = result;
        v_stack_m2E0 = 0;
        result = v_stack_m178;
        v_stack_m2E8 = result;
        result = Arg8;
        v_stack_m2F0 = (uint32_t)(result);
        v_stack_m2F8 = (uint32_t)(result);
        result = v_stack_m1E0;
        v_stack_m300 = result;
        result = v_stack_m1F0;
        v_stack_m308 = result;
        result = v_stack_m260;
        v_stack_m310 = result;
        result = v_stack_m150;
        v_stack_m318 = result;
        Arg4 = v_stack_m188;
        Arg2 = v_stack_m158;
        Arg1 = v_stack_m250;
        result = SepAdtOpenObjectAuditAlarm(Arg1, Arg2, Arg3, Arg4);
    }
loc_00A1D543:
    result = SeUnlockSubjectContext(v_stack_m1F0, Arg2, Arg3, Arg4);
    if (Arg17 == 0) goto loc_00A1D641;
    v_stack_m1B8 = 0;
    if (v_stack_m288 != 0) goto loc_00A1D5DF;
loc_00A1D585:
    v_stack_m1B8 = 0;
    if (0 >= v_stack_m278) goto loc_00A1D69A;
    *(uint32_t *)(v_stack_m198 + 0x0 * 4) = (uint32_t)((uint32_t)(v_stack_m288));
    *(uint32_t *)(v_stack_m190 + 0x0 * 4) = (uint32_t)((uint32_t)(v_stack_m280));
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x4E750E)) == 0) goto loc_00A1D5DA;
    if ((uint8_t)(v_stack_m294) == 0) goto loc_00A1D5DA;
    result = (uint32_t)(v_stack_m288);
    if (!(sign_flag)) {
        *(uint32_t *)(v_stack_m198 + 0x0 * 4) = (uint32_t)((uint32_t)(v_stack_m288));
        result = v_stack_m280;
    }
    Arg1 = (uint32_t)((0) + ((uint32_t)(local_rsi + 1)));
    goto loc_00A1D585;
loc_00A1D5DF:
loc_00A1D5E1:
    v_stack_m1B8 = 0;
    if (0 >= v_stack_m278) goto loc_00A1D69A;
    *(uint32_t *)(v_stack_m198 + 0x0 * 4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m288 + 0x0 * 4)));
    *(uint32_t *)(v_stack_m190 + 0x0 * 4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m280 + 0x0 * 4)));
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x4E74B7)) == 0) goto loc_00A1D63C;
    if ((uint8_t)(v_stack_m294) == 0) goto loc_00A1D63C;
    result = *(uint8_t *)(v_rip + 0x4E74B7);
    if ((*(uint32_t *)(v_stack_m288 + 0x0 * 4)) >= 0) {
        result = v_stack_m200;
        result = *(uint32_t *)(result + 0x0 * 4);
        *(uint32_t *)(v_stack_m198 + 0x0 * 4) = (uint32_t)(result);
        result = v_stack_m268;
        result = *(uint32_t *)(result + 0x0 * 4);
    }
    Arg2 = (uint32_t)((0) + ((uint32_t)(local_rsi + 1)));
    goto loc_00A1D5E1;
loc_00A1D641:
    *(uint32_t *)(v_stack_m198) = (uint32_t)((uint32_t)(v_stack_m288));
    *(uint32_t *)(v_stack_m190) = (uint32_t)((uint32_t)(v_stack_m280));
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x4E745C)) == 0) goto loc_00A1D69A;
    if (v_stack_m294 == 0) goto loc_00A1D6A2;
    if (v_stack_m288 < 0) goto loc_00A1D6A2;
    *(uint32_t *)(v_stack_m198) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m200)));
    goto loc_00A1D6A2;
loc_00A1D69A:
loc_00A1D6A2:
    *(uint8_t *)(v_stack_mF0) = (uint8_t)((uint32_t)(v_stack_m22C));
    v_stack_m290 = 0;
    goto loc_00A1D6F9;
loc_00A1D6E9:
loc_00A1D6EE:
loc_00A1D6F1:
loc_00A1D6F9:
    result = v_stack_mF0;
    if (v_stack_m23C != 0) {
        Arg1 = v_stack_m128;
        result = ObfDereferenceObject(Arg1, v_stack_m198, v_stack_m190, v_stack_m198);
        result = v_stack_mE8;
        v_stack_m1F0 = result;
    }
    if (v_stack_m178 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m178, Arg2, v_stack_m190, v_stack_m198);
    }
    result = SeReleaseSubjectContext(v_stack_m1F0, Arg2, v_stack_m190, v_stack_m198);
    Arg3 = 0;
    result = SeReleaseSecurityDescriptor(v_stack_m260, (uint8_t)(v_stack_m298), Arg3, v_stack_m198);
    if (v_stack_m158 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m158, Arg2, Arg3, v_stack_m198);
    }
    if (v_stack_m188 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m188, Arg2, Arg3, v_stack_m198);
    }
    if (v_stack_m150 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m150, Arg2, Arg3, v_stack_m198);
    }
    if (v_stack_m1A8 != 0) {
        Arg3 = (uint8_t)(local_rsi + 1);
        Arg2 = (uint8_t)(v_stack_m298);
        result = SeReleaseSid(v_stack_m1A8, Arg2, Arg3, v_stack_m198);
    }
    if (v_stack_m1F8 != 0) {
        result = SeFreeCapturedObjectTypeList(v_stack_m1F8, Arg2, Arg3, v_stack_m198);
    }
    if (v_stack_m28A == 0) goto loc_00A1D7E2;
    if (v_stack_m280 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m280;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, v_stack_m198);
    }
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = 0;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, v_stack_m198);
    }
    if (v_stack_m293 != 0) {
        Arg1 = v_stack_m1C0;
        result = SepRmDereferenceCap(Arg1, Arg2, Arg3, v_stack_m198);
    }
    if (v_stack_m180 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m180, Arg2, Arg3, v_stack_m198);
    }
    result = SepFreeResourceInfo(v_stack_m218, Arg2, Arg3, v_stack_m198);
    if (((uint32_t)((uint32_t)(0xC000000DULL))) == 0xC000009AULL) goto loc_00A1D82C;
    if (v_stack_m231 != 0) {
        Arg1 = (uint32_t)((uint32_t)(0xC000000DULL));
        result = SepAuditFailed(Arg1, Arg2, Arg3, v_stack_m198);
    }
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, v_stack_m198);
    local_rsp = (local_rsp) + (768);
    return result;
loc_00A1D859:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, v_stack_m198);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A1AF4C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
