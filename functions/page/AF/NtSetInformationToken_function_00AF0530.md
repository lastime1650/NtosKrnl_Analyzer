# NtSetInformationToken

- RVA: `0x00AF0530`–`0x00AF1F04` (길이 `6,612` bytes)
- VA: `0x0000000140AF0530`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D0D94`
- 디코드: `1,524`개 명령, `6,612/6,612` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **206**; 고유 호출 대상: **60**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00AF05EB` → [Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline](../../text/4C/Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline_function_004C78E8.md) (function, `0x004C78E8`)
- `0x00AF0601` → [RtlQueryElevationFlags](../A6/RtlQueryElevationFlags_function_00A60CB0.md) (function, `0x00A60CB0`)
- `0x00AF0625` → [Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline_function_004F2D58.md) (function, `0x004F2D58`)
- `0x00AF0678` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00AF06F7` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF070F` → [SeSetSessionIdToken](SeSetSessionIdToken_function_00AF1F0C.md) (function, `0x00AF1F0C`)
- `0x00AF0722` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF0764` → [SeCaptureAcl](../9C/SeCaptureAcl_function_009C6A58.md) (function, `0x009C6A58`)
- `0x00AF079F` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00AF07D6` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF07DB` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF07E5` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF07F7` → [SeReleaseAcl](../9C/SeReleaseAcl_function_009C7C64.md) (function, `0x009C7C64`)
- `0x00AF0809` → [SepExpandDynamic](../A6/SepExpandDynamic_function_00A665F0.md) (function, `0x00A665F0`)
- `0x00AF081E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF0823` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF082D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF083F` → [SeReleaseAcl](../9C/SeReleaseAcl_function_009C7C64.md) (function, `0x009C7C64`)
- `0x00AF087D` → [SeCaptureAcl](../9C/SeCaptureAcl_function_009C6A58.md) (function, `0x009C6A58`)
- `0x00AF088D` → [SepFreeDefaultDacl](../A7/SepFreeDefaultDacl_function_00A772D8.md) (function, `0x00A772D8`)
- `0x00AF08A2` → [SepAppendDefaultDacl](../A7/SepAppendDefaultDacl_function_00A745F0.md) (function, `0x00A745F0`)
- `0x00AF08BF` → [SeTokenDefaultDaclChangedAuditAlarm](../92/SeTokenDefaultDaclChangedAuditAlarm_function_00920570.md) (function, `0x00920570`)
- `0x00AF08EC` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF08F1` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF08FB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF090D` → [SeReleaseAcl](../9C/SeReleaseAcl_function_009C7C64.md) (function, `0x009C7C64`)
- `0x00AF0921` → [SeReleaseAcl](../9C/SeReleaseAcl_function_009C7C64.md) (function, `0x009C7C64`)
- `0x00AF0934` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF096A` → [SeCaptureSid](../92/SeCaptureSid_function_009276D4.md) (function, `0x009276D4`)
- `0x00AF0988` → [SepIdAssignableAsGroup](../7A/SepIdAssignableAsGroup_function_007A01A0.md) (function, `0x007A01A0`)
- `0x00AF09CE` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00AF0A02` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF0A07` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF0A1A` → [SepExpandDynamic](../A6/SepExpandDynamic_function_00A665F0.md) (function, `0x00A665F0`)
- `0x00AF0A2F` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF0A34` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF0A42` → [SepFreePrimaryGroup](../79/SepFreePrimaryGroup_function_0079D180.md) (function, `0x0079D180`)
- `0x00AF0A52` → [SepAppendPrimaryGroup](../79/SepAppendPrimaryGroup_function_0079D114.md) (function, `0x0079D114`)
- `0x00AF0A7F` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF0A84` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF0A91` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF0AA4` → [SeReleaseSid](../A2/SeReleaseSid_function_00A2EF50.md) (function, `0x00A2EF50`)
- `0x00AF0AB7` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF0ACC` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF0AFB` → [SeCaptureSid](../92/SeCaptureSid_function_009276D4.md) (function, `0x009276D4`)
- `0x00AF0B0D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF0B37` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00AF0B61` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (function, `0x00400AD0`)
- `0x00AF0B77` → [SepIdAssignableAsOwner](../A3/SepIdAssignableAsOwner_function_00A37678.md) (function, `0x00A37678`)
- `0x00AF0BD4` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF0BD9` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF0BE1` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF0BF4` → [SeReleaseSid](../A2/SeReleaseSid_function_00A2EF50.md) (function, `0x00A2EF50`)
- `0x00AF0C4D` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF0C52` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF0C5A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF0C6E` → [SeReleaseSid](../A2/SeReleaseSid_function_00A2EF50.md) (function, `0x00A2EF50`)
- `0x00AF0C82` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF0C87` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF0C8F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF0CA2` → [SeReleaseSid](../A2/SeReleaseSid_function_00A2EF50.md) (function, `0x00A2EF50`)
- `0x00AF0CB8` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF0CDF` → [SepOneWayLinkLogonSessions](../../text/60/SepOneWayLinkLogonSessions_function_006068D8.md) (function, `0x006068D8`)
- `0x00AF0CF0` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF0D1A` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF0D51` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00AF0D75` → [SepRemoveTokenLogonSession](../7A/SepRemoveTokenLogonSession_function_007A19C8.md) (function, `0x007A19C8`)
- `0x00AF0D7D` → [SepStopReferencingLogonSession](../A8/SepStopReferencingLogonSession_function_00A8E35C.md) (function, `0x00A8E35C`)
- `0x00AF0D96` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF0D9B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF0DAE` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF0DFB` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF0E24` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00AF0E7E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF0E83` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF0E96` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF0EC3` → [SepLinkLogonSessions](../../text/4A/SepLinkLogonSessions_function_004AAE78.md) (function, `0x004AAE78`)
- `0x00AF0ED4` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF0EFB` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF0F24` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00AF0F83` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF0FA1` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF0FCA` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AF0FD6` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF0FDB` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF1004` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00AF103E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF1043` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF1067` → [SepCaptureAuditPolicy](../79/SepCaptureAuditPolicy_function_0079FC80.md) (function, `0x0079FC80`)
- `0x00AF108F` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00AF10FB` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF1100` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF110A` → [SepModifyTokenPolicyCounter](../79/SepModifyTokenPolicyCounter_function_0079D1E0.md) (function, `0x0079D1E0`)
- `0x00AF1114` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF1124` → [SepReleaseAuditPolicy](../7A/SepReleaseAuditPolicy_function_007A017C.md) (function, `0x007A017C`)
- `0x00AF1135` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF1146` → [SepReleaseAuditPolicy](../7A/SepReleaseAuditPolicy_function_007A017C.md) (function, `0x007A017C`)
- `0x00AF1169` → [SeSetVirtualizationToken](../AA/SeSetVirtualizationToken_function_00AA28B4.md) (function, `0x00AA28B4`)
- `0x00AF117A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF11DD` → [Feature_AgentId2__private_IsEnabledDeviceUsageNoInline](../../text/60/Feature_AgentId2__private_IsEnabledDeviceUsageNoInline_function_006066CC.md) (function, `0x006066CC`)
- `0x00AF124A` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF1265` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AF12AB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AF12E7` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00AF1300` → [SepAddAgentIdClaimToToken](../7A/SepAddAgentIdClaimToToken_function_007A0B30.md) (function, `0x007A0B30`)
- `0x00AF1340` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF1345` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF134F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AF1362` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AF136C` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF138C` → [Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline_function_004F2D58.md) (function, `0x004F2D58`)
- `0x00AF13A7` → [RtlReadULongFromUser](../70/RtlReadULongFromUser_function_00705E08.md) (function, `0x00705E08`)
- `0x00AF13D1` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00AF1405` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF141B` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF1470` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00AF14AE` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF14B3` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF14C9` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF14F3` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF1505` → [SeSetPrivateNameSpaceToken](../79/SeSetPrivateNameSpaceToken_function_0079CED8.md) (function, `0x0079CED8`)
- `0x00AF1516` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF154B` → [SepCaptureTokenSecurityAttributesAndOperationsInformation](../97/SepCaptureTokenSecurityAttributesAndOperationsInformation_function_00971E0C.md) (function, `0x00971E0C`)
- `0x00AF1569` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF158E` → [SepReleaseTokenSecurityAttributesAndOperationsInformation](../A4/SepReleaseTokenSecurityAttributesAndOperationsInformation_function_00A4D0E4.md) (function, `0x00A4D0E4`)
- `0x00AF15A4` → [SepShouldSetDelinkFlags](../A5/SepShouldSetDelinkFlags_function_00A5030C.md) (function, `0x00A5030C`)
- `0x00AF15C8` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00AF15EC` → [AuthzBasepSetSecurityAttributesToken](../../text/3A/AuthzBasepSetSecurityAttributesToken_function_003A8D1C.md) (function, `0x003A8D1C`)
- `0x00AF162E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF1633` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF1643` → [SepReleaseTokenSecurityAttributesAndOperationsInformation](../A4/SepReleaseTokenSecurityAttributesAndOperationsInformation_function_00A4D0E4.md) (function, `0x00A4D0E4`)
- `0x00AF1651` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x00AF1670` → [RtlReadULongFromUser](../70/RtlReadULongFromUser_function_00705E08.md) (function, `0x00705E08`)
- `0x00AF16BB` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF16E4` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00AF16FC` → [SepRemoveAceFromTokenDefaultDacl](../../text/40/SepRemoveAceFromTokenDefaultDacl_function_0040018C.md) (function, `0x0040018C`)
- `0x00AF1717` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AF1731` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AF1752` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AF1766` → [SepDereferenceLowBoxNumberEntry](../A5/SepDereferenceLowBoxNumberEntry_function_00A55DBC.md) (function, `0x00A55DBC`)
- `0x00AF178E` → [SepDereferenceCachedHandlesEntryInternal](../A1/SepDereferenceCachedHandlesEntryInternal_function_00A19424.md) (function, `0x00A19424`)
- `0x00AF17AE` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF17D8` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF1803` → [SeSetMandatoryPolicyToken](../A5/SeSetMandatoryPolicyToken_function_00A5EDCC.md) (function, `0x00A5EDCC`)
- `0x00AF1814` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF1842` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF186B` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00AF18C5` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF18CA` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF18DD` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF1921` → [SeCaptureSidAndAttributesArray](../9C/SeCaptureSidAndAttributesArray_function_009C9D70.md) (function, `0x009C9D70`)
- `0x00AF1965` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF1970` → [SeReleaseLuidAndAttributesArray](../9C/SeReleaseLuidAndAttributesArray_function_009C7C40.md) (function, `0x009C7C40`)
- `0x00AF1982` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (function, `0x00468F10`)
- `0x00AF1999` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x00AF19CE` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)
- `0x00AF19DF` → [SepLocateTokenIntegrity](../../text/41/SepLocateTokenIntegrity_function_0041BF10.md) (function, `0x0041BF10`)
- `0x00AF1A01` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (function, `0x00468F10`)
- `0x00AF1A22` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x00AF1A3F` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00AF1A79` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x00AF1A89` → [Feature_871661881__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_871661881__private_IsEnabledDeviceUsageNoInline_function_004F4D24.md) (function, `0x004F4D24`)
- `0x00AF1AA5` → [RtlQueryElevationFlags](../A6/RtlQueryElevationFlags_function_00A60CB0.md) (function, `0x00A60CB0`)
- `0x00AF1AC2` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (function, `0x00468F10`)
- `0x00AF1AD8` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x00AF1B04` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x00AF1B28` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00AF1B30` → [SepLocateTokenIntegrity](../../text/41/SepLocateTokenIntegrity_function_0041BF10.md) (function, `0x0041BF10`)
- `0x00AF1B3B` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (function, `0x00468F10`)
- `0x00AF1B51` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x00AF1B63` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF1B68` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF1B75` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00AF1B84` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF1B89` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF1B96` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00AF1BA8` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x00AF1BBC` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (function, `0x00468F10`)
- `0x00AF1BD2` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x00AF1BF9` → [SeCaptureSubjectContext](../86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x00AF1C06` → [SeLockSubjectContext](../8C/SeLockSubjectContext_function_008C64C0.md) (function, `0x008C64C0`)
- `0x00AF1C22` → [SeUnlockSubjectContext](../8C/SeUnlockSubjectContext_function_008C6520.md) (function, `0x008C6520`)
- `0x00AF1C2F` → [SeReleaseSubjectContext](../86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00AF1C52` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x00AF1C9E` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x00AF1CD2` → [SepRemoveAceFromTokenDefaultDacl](../../text/40/SepRemoveAceFromTokenDefaultDacl_function_0040018C.md) (function, `0x0040018C`)
- `0x00AF1CED` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AF1D07` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AF1D28` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AF1D3C` → [SepDereferenceLowBoxNumberEntry](../A5/SepDereferenceLowBoxNumberEntry_function_00A55DBC.md) (function, `0x00A55DBC`)
- `0x00AF1D64` → [SepDereferenceCachedHandlesEntryInternal](../A1/SepDereferenceCachedHandlesEntryInternal_function_00A19424.md) (function, `0x00A19424`)
- `0x00AF1D77` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (function, `0x00468F10`)
- `0x00AF1D8D` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x00AF1DBE` → [SepRemoveAceFromTokenDefaultDacl](../../text/40/SepRemoveAceFromTokenDefaultDacl_function_0040018C.md) (function, `0x0040018C`)
- `0x00AF1DD9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AF1DF3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AF1E14` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AF1E28` → [SepDereferenceLowBoxNumberEntry](../A5/SepDereferenceLowBoxNumberEntry_function_00A55DBC.md) (function, `0x00A55DBC`)
- `0x00AF1E50` → [SepDereferenceCachedHandlesEntryInternal](../A1/SepDereferenceCachedHandlesEntryInternal_function_00A19424.md) (function, `0x00A19424`)
- `0x00AF1E9B` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00AF1EA0` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00AF1EAA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF1EBA` → [SeReleaseLuidAndAttributesArray](../9C/SeReleaseLuidAndAttributesArray_function_009C7C40.md) (function, `0x009C7C40`)
- `0x00AF1ECB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AF1EF7` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x00AF1EFD` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00AF0657` → RVA `0x00FD8020` (`PAGEDATA`; read)
- `0x00AF06F0` → RVA `0x00FD9A78` (`PAGEDATA`; read)
- `0x00AF08C4` → RVA `0x00012D08` (`.rdata`; read)
- `0x00AF08CE` → RVA `0x00E0EBF0` (`.data`; read/write)
- `0x00AF0D69` → RVA `0x00FD8010` (`PAGEDATA`; read)
- `0x00AF0DF4` → RVA `0x00FD9B80` (`PAGEDATA`; read)
- `0x00AF193E` → RVA `0x00F05818` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **134**
  - `0x00AF05EB` → [Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline](../../text/4C/Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline_function_004C78E8.md) (`PAGE` → `.text`)
  - `0x00AF0625` → [Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline_function_004F2D58.md) (`PAGE` → `.text`)
  - `0x00AF0722` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF079F` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00AF07D6` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF07DB` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF07E5` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF081E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF0823` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF082D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF08EC` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF08F1` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF08FB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF0934` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF09CE` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00AF0A02` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF0A07` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF0A2F` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF0A34` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF0A7F` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF0A84` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF0A91` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF0AB7` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF0ACC` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF0B0D` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF0B37` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00AF0B61` → [RtlEqualSid](../../text/40/RtlEqualSid_function_00400AD0.md) (`PAGE` → `.text`)
  - `0x00AF0BD4` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF0BD9` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF0BE1` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF0C4D` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF0C52` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF0C5A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF0C82` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF0C87` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF0C8F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF0CB8` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF0CDF` → [SepOneWayLinkLogonSessions](../../text/60/SepOneWayLinkLogonSessions_function_006068D8.md) (`PAGE` → `.text`)
  - `0x00AF0CF0` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF0D51` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00AF0D96` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF0D9B` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF0DAE` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF0E24` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00AF0E7E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF0E83` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF0E96` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF0EC3` → [SepLinkLogonSessions](../../text/4A/SepLinkLogonSessions_function_004AAE78.md) (`PAGE` → `.text`)
  - `0x00AF0ED4` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF0F24` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00AF0F83` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF0FCA` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AF0FD6` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF0FDB` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF1004` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00AF103E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF1043` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF108F` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00AF10FB` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF1100` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF1114` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF1135` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF117A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF11DD` → [Feature_AgentId2__private_IsEnabledDeviceUsageNoInline](../../text/60/Feature_AgentId2__private_IsEnabledDeviceUsageNoInline_function_006066CC.md) (`PAGE` → `.text`)
  - `0x00AF1265` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AF12AB` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AF12E7` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00AF1340` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF1345` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF134F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AF1362` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AF136C` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF138C` → [Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline_function_004F2D58.md) (`PAGE` → `.text`)
  - `0x00AF13D1` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00AF1405` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF1470` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00AF14AE` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF14B3` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF14C9` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF1516` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF15C8` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00AF15EC` → [AuthzBasepSetSecurityAttributesToken](../../text/3A/AuthzBasepSetSecurityAttributesToken_function_003A8D1C.md) (`PAGE` → `.text`)
  - `0x00AF162E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF1633` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF1651` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (`PAGE` → `.text`)
  - `0x00AF16E4` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00AF16FC` → [SepRemoveAceFromTokenDefaultDacl](../../text/40/SepRemoveAceFromTokenDefaultDacl_function_0040018C.md) (`PAGE` → `.text`)
  - `0x00AF1717` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AF1731` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AF1752` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AF17AE` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF1814` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF186B` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00AF18C5` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF18CA` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF18DD` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF1965` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF1982` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (`PAGE` → `.text`)
  - `0x00AF1999` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x00AF19CE` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
  - `0x00AF19DF` → [SepLocateTokenIntegrity](../../text/41/SepLocateTokenIntegrity_function_0041BF10.md) (`PAGE` → `.text`)
  - `0x00AF1A01` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (`PAGE` → `.text`)
  - `0x00AF1A22` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x00AF1A79` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x00AF1A89` → [Feature_871661881__private_IsEnabledDeviceUsageNoInline](../../text/4F/Feature_871661881__private_IsEnabledDeviceUsageNoInline_function_004F4D24.md) (`PAGE` → `.text`)
  - `0x00AF1AC2` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (`PAGE` → `.text`)
  - `0x00AF1AD8` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x00AF1B28` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x00AF1B30` → [SepLocateTokenIntegrity](../../text/41/SepLocateTokenIntegrity_function_0041BF10.md) (`PAGE` → `.text`)
  - `0x00AF1B3B` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (`PAGE` → `.text`)
  - `0x00AF1B51` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x00AF1B63` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF1B68` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF1B84` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF1B89` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF1BA8` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (`PAGE` → `.text`)
  - `0x00AF1BBC` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (`PAGE` → `.text`)
  - `0x00AF1BD2` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x00AF1C52` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x00AF1C9E` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../../text/4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (`PAGE` → `.text`)
  - `0x00AF1CD2` → [SepRemoveAceFromTokenDefaultDacl](../../text/40/SepRemoveAceFromTokenDefaultDacl_function_0040018C.md) (`PAGE` → `.text`)
  - `0x00AF1CED` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AF1D07` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AF1D28` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AF1D77` → [RtlSubAuthorityCountSid](../../text/46/RtlSubAuthorityCountSid_function_00468F10.md) (`PAGE` → `.text`)
  - `0x00AF1D8D` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x00AF1DBE` → [SepRemoveAceFromTokenDefaultDacl](../../text/40/SepRemoveAceFromTokenDefaultDacl_function_0040018C.md) (`PAGE` → `.text`)
  - `0x00AF1DD9` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AF1DF3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AF1E14` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AF1E9B` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x00AF1EA0` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x00AF1EAA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AF1ECB` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AF0530  48 8B C4                        mov rax, rsp
00AF0533  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00AF0537  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00AF053B  48 89 48 08                     mov qword ptr [rax + 8], rcx
00AF053F  57                              push rdi
00AF0540  41 54                           push r12
00AF0542  41 55                           push r13
00AF0544  41 56                           push r14
00AF0546  41 57                           push r15
00AF0548  48 81 EC 60 01 00 00            sub rsp, 0x160
00AF054F  45 8B E1                        mov r12d, r9d
00AF0552  4D 8B F0                        mov r14, r8
00AF0555  48 63 DA                        movsxd rbx, edx
00AF0558  48 8B F1                        mov rsi, rcx
00AF055B  33 FF                           xor edi, edi
00AF055D  40 88 7C 24 5C                  mov byte ptr [rsp + 0x5c], dil
00AF0562  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
00AF0566  48 89 B8 38 FF FF FF            mov qword ptr [rax - 0xc8], rdi
00AF056D  48 89 B8 40 FF FF FF            mov qword ptr [rax - 0xc0], rdi
00AF0574  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF057D  44 8A B8 32 02 00 00            mov r15b, byte ptr [rax + 0x232]
00AF0584  44 88 7C 24 5D                  mov byte ptr [rsp + 0x5d], r15b
00AF0589  45 84 FF                        test r15b, r15b
00AF058C  74 3E                           je 0x140af05cc
00AF058E  45 85 C9                        test r9d, r9d
00AF0591  74 28                           je 0x140af05bb
00AF0593  41 F6 C6 03                     test r14b, 3
00AF0597  0F 85 5A 19 00 00               jne 0x140af1ef7
00AF059D  4B 8D 0C 20                     lea rcx, [r8 + r12]
00AF05A1  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
00AF05AB  49 3B CD                        cmp rcx, r13
00AF05AE  77 05                           ja 0x140af05b5
00AF05B0  49 3B CE                        cmp rcx, r14
00AF05B3  73 10                           jae 0x140af05c5
00AF05B5  41 8A 45 00                     mov al, byte ptr [r13]
00AF05B9  EB 0A                           jmp 0x140af05c5
00AF05BB  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
00AF05C5  EB 0F                           jmp 0x140af05d6
00AF05C7  E9 0D 19 00 00                  jmp 0x140af1ed9
00AF05CC  49 BD 00 00 FF FF FF 7F 00 00   movabs r13, 0x7fffffff0000
00AF05D6  83 FB 3A                        cmp ebx, 0x3a
00AF05D9  77 10                           ja 0x140af05eb
00AF05DB  48 B9 70 50 8B 2F 80 24 10 04   movabs rcx, 0x41024802f8b5070
00AF05E5  48 0F A3 D9                     bt rcx, rbx
00AF05E9  72 3A                           jb 0x140af0625
00AF05EB  E8 F8 72 9D FF                  call 0x1404c78e8
00AF05F0  85 C0                           test eax, eax
00AF05F2  0F 84 DC 18 00 00               je 0x140af1ed4
00AF05F8  89 7C 24 78                     mov dword ptr [rsp + 0x78], edi
00AF05FC  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
00AF0601  E8 AA 06 F7 FF                  call 0x140a60cb0
00AF0606  85 C0                           test eax, eax
00AF0608  0F 88 C6 18 00 00               js 0x140af1ed4
00AF060E  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00AF0612  24 18                           and al, 0x18
00AF0614  3C 10                           cmp al, 0x10
00AF0616  0F 85 B8 18 00 00               jne 0x140af1ed4
00AF061C  83 FB FE                        cmp ebx, -2
00AF061F  0F 85 AF 18 00 00               jne 0x140af1ed4
00AF0625  E8 2E 27 A0 FF                  call 0x1404f2d58
00AF062A  85 C0                           test eax, eax
00AF062C  75 09                           jne 0x140af0637
00AF062E  83 FB 34                        cmp ebx, 0x34
00AF0631  0F 84 9D 18 00 00               je 0x140af1ed4
00AF0637  BA 80 00 00 00                  mov edx, 0x80
00AF063C  83 FB 0C                        cmp ebx, 0xc
00AF063F  75 07                           jne 0x140af0648
00AF0641  BA 80 01 00 00                  mov edx, 0x180
00AF0646  EB 0F                           jmp 0x140af0657
00AF0648  83 FB 13                        cmp ebx, 0x13
00AF064B  74 05                           je 0x140af0652
00AF064D  83 FB FE                        cmp ebx, -2
00AF0650  75 05                           jne 0x140af0657
00AF0652  BA 88 00 00 00                  mov edx, 0x88
00AF0657  4C 8B 05 C2 79 4E 00            mov r8, qword ptr [rip + 0x4e79c2]
00AF065E  48 89 7C 24 50                  mov qword ptr [rsp + 0x50], rdi
00AF0663  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00AF0668  48 8D 44 24 50                  lea rax, [rsp + 0x50]
00AF066D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AF0672  45 8A CF                        mov r9b, r15b
00AF0675  48 8B CE                        mov rcx, rsi
00AF0678  E8 33 87 D7 FF                  call 0x140868db0
00AF067D  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00AF0682  48 89 B4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rsi
00AF068A  85 C0                           test eax, eax
00AF068C  0F 88 47 18 00 00               js 0x140af1ed9
00AF0692  83 FB 18                        cmp ebx, 0x18
00AF0695  0F 8F EB 0A 00 00               jg 0x140af1186
00AF069B  0F 84 B1 0A 00 00               je 0x140af1152
00AF06A1  83 FB 0E                        cmp ebx, 0xe
00AF06A4  0F 8F 10 07 00 00               jg 0x140af0dba
00AF06AA  0F 84 4C 06 00 00               je 0x140af0cfc
00AF06B0  83 FB FE                        cmp ebx, -2
00AF06B3  0F 84 0B 06 00 00               je 0x140af0cc4
00AF06B9  83 FB 04                        cmp ebx, 4
00AF06BC  0F 84 01 04 00 00               je 0x140af0ac3
00AF06C2  83 FB 05                        cmp ebx, 5
00AF06C5  0F 84 75 02 00 00               je 0x140af0940
00AF06CB  83 FB 06                        cmp ebx, 6
00AF06CE  74 5E                           je 0x140af072e
00AF06D0  83 FB 0C                        cmp ebx, 0xc
00AF06D3  0F 85 FA 0A 00 00               jne 0x140af11d3
00AF06D9  41 83 FC 04                     cmp r12d, 4
00AF06DD  0F 85 E6 03 00 00               jne 0x140af0ac9
00AF06E3  41 8B 1E                        mov ebx, dword ptr [r14]
00AF06E6  89 9C 24 F0 00 00 00            mov dword ptr [rsp + 0xf0], ebx
00AF06ED  41 8A D7                        mov dl, r15b
00AF06F0  48 8B 0D 81 93 4E 00            mov rcx, qword ptr [rip + 0x4e9381]
00AF06F7  E8 24 17 D8 FF                  call 0x140871e20
00AF06FC  84 C0                           test al, al
00AF06FE  75 0A                           jne 0x140af070a
00AF0700  BB 61 00 00 C0                  mov ebx, 0xc0000061
00AF0705  E9 00 04 00 00                  jmp 0x140af0b0a
00AF070A  8B D3                           mov edx, ebx
00AF070C  48 8B CE                        mov rcx, rsi
00AF070F  E8 F8 17 00 00                  call 0x140af1f0c
00AF0714  8B D8                           mov ebx, eax
00AF0716  E9 EF 03 00 00                  jmp 0x140af0b0a
00AF071B  8B D8                           mov ebx, eax
00AF071D  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF0722  E8 29 8C 80 FF                  call 0x1402f9350
00AF0727  8B C3                           mov eax, ebx
00AF0729  E9 AB 17 00 00                  jmp 0x140af1ed9
00AF072E  41 83 FC 08                     cmp r12d, 8
00AF0732  0F 82 91 03 00 00               jb 0x140af0ac9
00AF0738  49 8B 0E                        mov rcx, qword ptr [r14]
00AF073B  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
00AF0740  48 85 C9                        test rcx, rcx
00AF0743  74 2C                           je 0x140af0771
00AF0745  48 8D 44 24 60                  lea rax, [rsp + 0x60]
00AF074A  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AF074F  48 8D 44 24 68                  lea rax, [rsp + 0x68]
00AF0754  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AF0759  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
00AF0761  41 8A D7                        mov dl, r15b
00AF0764  E8 EF 62 ED FF                  call 0x1409c6a58
00AF0769  8B D8                           mov ebx, eax
00AF076B  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AF076F  EB 0A                           jmp 0x140af077b
00AF0771  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
00AF0775  8B DF                           mov ebx, edi
00AF0777  89 5C 24 58                     mov dword ptr [rsp + 0x58], ebx
00AF077B  85 DB                           test ebx, ebx
00AF077D  0F 88 87 03 00 00               js 0x140af0b0a
00AF0783  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF078C  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF0793  90                              nop
00AF0794  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00AF0799  B2 01                           mov dl, 1
00AF079B  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AF079F  E8 7C 46 72 FF                  call 0x140214e20
00AF07A4  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF07A8  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00AF07AD  48 8B 83 A8 00 00 00            mov rax, qword ptr [rbx + 0xa8]
00AF07B4  0F B6 50 01                     movzx edx, byte ptr [rax + 1]
00AF07B8  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
00AF07BC  83 C0 08                        add eax, 8
00AF07BF  8D 14 90                        lea edx, [rax + rdx*4]
00AF07C2  89 54 24 60                     mov dword ptr [rsp + 0x60], edx
00AF07C6  3B 93 88 00 00 00               cmp edx, dword ptr [rbx + 0x88]
00AF07CC  76 38                           jbe 0x140af0806
00AF07CE  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF07D2  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AF07D6  E8 35 F2 76 FF                  call 0x14025fa10
00AF07DB  E8 D0 D0 76 FF                  call 0x14025d8b0
00AF07E0  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF07E5  E8 66 8B 80 FF                  call 0x1402f9350
00AF07EA  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00AF07EF  48 85 C9                        test rcx, rcx
00AF07F2  74 08                           je 0x140af07fc
00AF07F4  41 8A D7                        mov dl, r15b
00AF07F7  E8 68 74 ED FF                  call 0x1409c7c64
00AF07FC  B8 99 00 00 C0                  mov eax, 0xc0000099
00AF0801  E9 D3 16 00 00                  jmp 0x140af1ed9
00AF0806  48 8B CB                        mov rcx, rbx
00AF0809  E8 E2 5D F7 FF                  call 0x140a665f0
00AF080E  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AF0812  85 C0                           test eax, eax
00AF0814  79 37                           jns 0x140af084d
00AF0816  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF081A  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AF081E  E8 ED F1 76 FF                  call 0x14025fa10
00AF0823  E8 88 D0 76 FF                  call 0x14025d8b0
00AF0828  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF082D  E8 1E 8B 80 FF                  call 0x1402f9350
00AF0832  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00AF0837  48 85 C9                        test rcx, rcx
00AF083A  74 08                           je 0x140af0844
00AF083C  41 8A D7                        mov dl, r15b
00AF083F  E8 20 74 ED FF                  call 0x1409c7c64
00AF0844  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
00AF0848  E9 8C 16 00 00                  jmp 0x140af1ed9
00AF084D  48 8B 8B B8 00 00 00            mov rcx, qword ptr [rbx + 0xb8]
00AF0854  48 85 C9                        test rcx, rcx
00AF0857  74 31                           je 0x140af088a
00AF0859  48 8D 84 24 F4 00 00 00         lea rax, [rsp + 0xf4]
00AF0861  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AF0866  48 8D 84 24 C0 00 00 00         lea rax, [rsp + 0xc0]
00AF086E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AF0873  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
00AF087B  33 D2                           xor edx, edx
00AF087D  E8 D6 61 ED FF                  call 0x1409c6a58
00AF0882  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AF0886  85 C0                           test eax, eax
00AF0888  78 8C                           js 0x140af0816
00AF088A  48 8B CB                        mov rcx, rbx
00AF088D  E8 46 6A F8 FF                  call 0x140a772d8
00AF0892  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
00AF0897  4D 85 F6                        test r14, r14
00AF089A  74 0B                           je 0x140af08a7
00AF089C  49 8B D6                        mov rdx, r14
00AF089F  48 8B CB                        mov rcx, rbx
00AF08A2  E8 49 3D F8 FF                  call 0x140a745f0
00AF08A7  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00AF08AC  4C 8B 8C 24 C0 00 00 00         mov r9, qword ptr [rsp + 0xc0]
00AF08B4  4C 8B 84 24 90 01 00 00         mov r8, qword ptr [rsp + 0x190]
00AF08BC  48 8B D3                        mov rdx, rbx
00AF08BF  E8 AC FC E2 FF                  call 0x140920570
00AF08C4  48 8B 0D 3D 24 52 FF            mov rcx, qword ptr [rip - 0xaddbc3]
00AF08CB  48 8B C1                        mov rax, rcx
00AF08CE  F0 48 0F C1 05 19 E3 31 00      lock xadd qword ptr [rip + 0x31e319], rax
00AF08D7  48 03 C1                        add rax, rcx
00AF08DA  89 43 38                        mov dword ptr [rbx + 0x38], eax
00AF08DD  48 C1 E8 20                     shr rax, 0x20
00AF08E1  89 43 3C                        mov dword ptr [rbx + 0x3c], eax
00AF08E4  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF08E8  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AF08EC  E8 1F F1 76 FF                  call 0x14025fa10
00AF08F1  E8 BA CF 76 FF                  call 0x14025d8b0
00AF08F6  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF08FB  E8 50 8A 80 FF                  call 0x1402f9350
00AF0900  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
00AF0905  48 85 C9                        test rcx, rcx
00AF0908  74 08                           je 0x140af0912
00AF090A  41 8A D7                        mov dl, r15b
00AF090D  E8 52 73 ED FF                  call 0x1409c7c64
00AF0912  48 8B 8C 24 C0 00 00 00         mov rcx, qword ptr [rsp + 0xc0]
00AF091A  48 85 C9                        test rcx, rcx
00AF091D  74 07                           je 0x140af0926
00AF091F  33 D2                           xor edx, edx
00AF0921  E8 3E 73 ED FF                  call 0x1409c7c64
00AF0926  33 C0                           xor eax, eax
00AF0928  E9 AC 15 00 00                  jmp 0x140af1ed9
00AF092D  8B D8                           mov ebx, eax
00AF092F  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF0934  E8 17 8A 80 FF                  call 0x1402f9350
00AF0939  8B C3                           mov eax, ebx
00AF093B  E9 99 15 00 00                  jmp 0x140af1ed9
00AF0940  41 83 FC 08                     cmp r12d, 8
00AF0944  0F 82 7F 01 00 00               jb 0x140af0ac9
00AF094A  49 8B 0E                        mov rcx, qword ptr [r14]
00AF094D  48 89 8C 24 88 00 00 00         mov qword ptr [rsp + 0x88], rcx
00AF0955  48 8D 84 24 88 00 00 00         lea rax, [rsp + 0x88]
00AF095D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AF0962  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
00AF0967  41 8A D7                        mov dl, r15b
00AF096A  E8 65 6D E3 FF                  call 0x1409276d4
00AF096F  8B D8                           mov ebx, eax
00AF0971  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AF0975  48 8B CE                        mov rcx, rsi
00AF0978  85 DB                           test ebx, ebx
00AF097A  0F 88 8D 01 00 00               js 0x140af0b0d
00AF0980  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
00AF0988  E8 13 F8 CA FF                  call 0x1407a01a0
00AF098D  84 C0                           test al, al
00AF098F  75 0A                           jne 0x140af099b
00AF0991  BF 5B 00 00 C0                  mov edi, 0xc000005b
00AF0996  E9 F3 00 00 00                  jmp 0x140af0a8e
00AF099B  48 8B 84 24 88 00 00 00         mov rax, qword ptr [rsp + 0x88]
00AF09A3  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
00AF09A7  8D 34 8D 08 00 00 00            lea esi, [rcx*4 + 8]
00AF09AE  89 74 24 60                     mov dword ptr [rsp + 0x60], esi
00AF09B2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF09BB  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF09C2  90                              nop
00AF09C3  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
00AF09C8  B2 01                           mov dl, 1
00AF09CA  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AF09CE  E8 4D 44 72 FF                  call 0x140214e20
00AF09D3  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF09D7  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00AF09DC  48 8B 83 B8 00 00 00            mov rax, qword ptr [rbx + 0xb8]
00AF09E3  48 85 C0                        test rax, rax
00AF09E6  74 0A                           je 0x140af09f2
00AF09E8  0F B7 40 02                     movzx eax, word ptr [rax + 2]
00AF09EC  03 F0                           add esi, eax
00AF09EE  89 74 24 60                     mov dword ptr [rsp + 0x60], esi
00AF09F2  3B B3 88 00 00 00               cmp esi, dword ptr [rbx + 0x88]
00AF09F8  76 19                           jbe 0x140af0a13
00AF09FA  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF09FE  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AF0A02  E8 09 F0 76 FF                  call 0x14025fa10
00AF0A07  E8 A4 CE 76 FF                  call 0x14025d8b0
00AF0A0C  BF 99 00 00 C0                  mov edi, 0xc0000099
00AF0A11  EB 76                           jmp 0x140af0a89
00AF0A13  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
00AF0A17  48 8B CB                        mov rcx, rbx
00AF0A1A  E8 D1 5B F7 FF                  call 0x140a665f0
00AF0A1F  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AF0A23  85 C0                           test eax, eax
00AF0A25  79 18                           jns 0x140af0a3f
00AF0A27  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF0A2B  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AF0A2F  E8 DC EF 76 FF                  call 0x14025fa10
00AF0A34  E8 77 CE 76 FF                  call 0x14025d8b0
00AF0A39  8B 7C 24 58                     mov edi, dword ptr [rsp + 0x58]
00AF0A3D  EB 4A                           jmp 0x140af0a89
00AF0A3F  48 8B CB                        mov rcx, rbx
00AF0A42  E8 39 C7 CA FF                  call 0x14079d180
00AF0A47  48 8B 94 24 88 00 00 00         mov rdx, qword ptr [rsp + 0x88]
00AF0A4F  48 8B CB                        mov rcx, rbx
00AF0A52  E8 BD C6 CA FF                  call 0x14079d114
00AF0A57  48 8B 0D AA 22 52 FF            mov rcx, qword ptr [rip - 0xaddd56]
00AF0A5E  48 8B C1                        mov rax, rcx
00AF0A61  F0 48 0F C1 05 86 E1 31 00      lock xadd qword ptr [rip + 0x31e186], rax
00AF0A6A  48 03 C1                        add rax, rcx
00AF0A6D  89 43 38                        mov dword ptr [rbx + 0x38], eax
00AF0A70  48 C1 E8 20                     shr rax, 0x20
00AF0A74  89 43 3C                        mov dword ptr [rbx + 0x3c], eax
00AF0A77  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF0A7B  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AF0A7F  E8 8C EF 76 FF                  call 0x14025fa10
00AF0A84  E8 27 CE 76 FF                  call 0x14025d8b0
00AF0A89  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00AF0A8E  48 8B CE                        mov rcx, rsi
00AF0A91  E8 BA 88 80 FF                  call 0x1402f9350
00AF0A96  41 B0 01                        mov r8b, 1
00AF0A99  41 8A D7                        mov dl, r15b
00AF0A9C  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00AF0AA4  E8 A7 E4 F3 FF                  call 0x140a2ef50
00AF0AA9  8B C7                           mov eax, edi
00AF0AAB  E9 29 14 00 00                  jmp 0x140af1ed9
00AF0AB0  8B D8                           mov ebx, eax
00AF0AB2  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF0AB7  E8 94 88 80 FF                  call 0x1402f9350
00AF0ABC  8B C3                           mov eax, ebx
00AF0ABE  E9 16 14 00 00                  jmp 0x140af1ed9
00AF0AC3  41 83 FC 08                     cmp r12d, 8
00AF0AC7  73 12                           jae 0x140af0adb
00AF0AC9  48 8B CE                        mov rcx, rsi
00AF0ACC  E8 7F 88 80 FF                  call 0x1402f9350
00AF0AD1  B8 04 00 00 C0                  mov eax, 0xc0000004
00AF0AD6  E9 FE 13 00 00                  jmp 0x140af1ed9
00AF0ADB  49 8B 0E                        mov rcx, qword ptr [r14]
00AF0ADE  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
00AF0AE6  48 8D 84 24 90 00 00 00         lea rax, [rsp + 0x90]
00AF0AEE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AF0AF3  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
00AF0AF8  41 8A D7                        mov dl, r15b
00AF0AFB  E8 D4 6B E3 FF                  call 0x1409276d4
00AF0B00  8B D8                           mov ebx, eax
00AF0B02  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AF0B06  85 DB                           test ebx, ebx
00AF0B08  79 0F                           jns 0x140af0b19
00AF0B0A  48 8B CE                        mov rcx, rsi
00AF0B0D  E8 3E 88 80 FF                  call 0x1402f9350
00AF0B12  8B C3                           mov eax, ebx
00AF0B14  E9 C0 13 00 00                  jmp 0x140af1ed9
00AF0B19  8B DF                           mov ebx, edi
00AF0B1B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF0B24  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF0B2B  90                              nop
00AF0B2C  B2 01                           mov dl, 1
00AF0B2E  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF0B33  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
00AF0B37  E8 E4 42 72 FF                  call 0x140214e20
00AF0B3C  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF0B40  3B 5E 7C                        cmp ebx, dword ptr [rsi + 0x7c]
00AF0B43  0F 83 31 01 00 00               jae 0x140af0c7a
00AF0B49  8B C3                           mov eax, ebx
00AF0B4B  48 03 C0                        add rax, rax
00AF0B4E  48 8B 96 98 00 00 00            mov rdx, qword ptr [rsi + 0x98]
00AF0B55  48 8B 14 C2                     mov rdx, qword ptr [rdx + rax*8]
00AF0B59  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00AF0B61  E8 6A FF 90 FF                  call 0x140400ad0
00AF0B66  88 44 24 64                     mov byte ptr [rsp + 0x64], al
00AF0B6A  84 C0                           test al, al
00AF0B6C  0F 84 90 00 00 00               je 0x140af0c02
00AF0B72  8B D3                           mov edx, ebx
00AF0B74  48 8B CE                        mov rcx, rsi
00AF0B77  E8 FC 6A F4 FF                  call 0x140a37678
00AF0B7C  84 C0                           test al, al
00AF0B7E  74 12                           je 0x140af0b92
00AF0B80  89 9E 90 00 00 00               mov dword ptr [rsi + 0x90], ebx
00AF0B86  B0 01                           mov al, 1
00AF0B88  88 44 24 5C                     mov byte ptr [rsp + 0x5c], al
00AF0B8C  89 7C 24 58                     mov dword ptr [rsp + 0x58], edi
00AF0B90  EB 0C                           jmp 0x140af0b9e
00AF0B92  C7 44 24 58 5A 00 00 C0         mov dword ptr [rsp + 0x58], 0xc000005a
00AF0B9A  8A 44 24 5C                     mov al, byte ptr [rsp + 0x5c]
00AF0B9E  84 C0                           test al, al
00AF0BA0  74 2A                           je 0x140af0bcc
00AF0BA2  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
00AF0BA7  48 8B 15 5A 21 52 FF            mov rdx, qword ptr [rip - 0xaddea6]
00AF0BAE  48 8B C2                        mov rax, rdx
00AF0BB1  F0 48 0F C1 05 36 E0 31 00      lock xadd qword ptr [rip + 0x31e036], rax
00AF0BBA  48 03 C2                        add rax, rdx
00AF0BBD  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00AF0BC2  89 46 38                        mov dword ptr [rsi + 0x38], eax
00AF0BC5  48 C1 E8 20                     shr rax, 0x20
00AF0BC9  89 46 3C                        mov dword ptr [rsi + 0x3c], eax
00AF0BCC  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF0BD0  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AF0BD4  E8 37 EE 76 FF                  call 0x14025fa10
00AF0BD9  E8 D2 CC 76 FF                  call 0x14025d8b0
00AF0BDE  48 8B CE                        mov rcx, rsi
00AF0BE1  E8 6A 87 80 FF                  call 0x1402f9350
00AF0BE6  41 B0 01                        mov r8b, 1
00AF0BE9  41 8A D7                        mov dl, r15b
00AF0BEC  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00AF0BF4  E8 57 E3 F3 FF                  call 0x140a2ef50
00AF0BF9  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
00AF0BFD  E9 D7 12 00 00                  jmp 0x140af1ed9
00AF0C02  FF C3                           inc ebx
00AF0C04  E9 37 FF FF FF                  jmp 0x140af0b40
00AF0C09  8B F8                           mov edi, eax
00AF0C0B  80 7C 24 5C 00                  cmp byte ptr [rsp + 0x5c], 0
00AF0C10  74 2A                           je 0x140af0c3c
00AF0C12  4C 8B 84 24 A0 00 00 00         mov r8, qword ptr [rsp + 0xa0]
00AF0C1A  48 8B 15 E7 20 52 FF            mov rdx, qword ptr [rip - 0xaddf19]
00AF0C21  48 8B CA                        mov rcx, rdx
00AF0C24  F0 48 0F C1 0D C3 DF 31 00      lock xadd qword ptr [rip + 0x31dfc3], rcx
00AF0C2D  48 03 CA                        add rcx, rdx
00AF0C30  41 89 48 38                     mov dword ptr [r8 + 0x38], ecx
00AF0C34  48 C1 E9 20                     shr rcx, 0x20
00AF0C38  41 89 48 3C                     mov dword ptr [r8 + 0x3c], ecx
00AF0C3C  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
00AF0C41  48 8B 9C 24 A0 00 00 00         mov rbx, qword ptr [rsp + 0xa0]
00AF0C49  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AF0C4D  E8 BE ED 76 FF                  call 0x14025fa10
00AF0C52  E8 59 CC 76 FF                  call 0x14025d8b0
00AF0C57  48 8B CB                        mov rcx, rbx
00AF0C5A  E8 F1 86 80 FF                  call 0x1402f9350
00AF0C5F  41 B0 01                        mov r8b, 1
00AF0C62  8A 54 24 5D                     mov dl, byte ptr [rsp + 0x5d]
00AF0C66  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00AF0C6E  E8 DD E2 F3 FF                  call 0x140a2ef50
00AF0C73  8B C7                           mov eax, edi
00AF0C75  E9 5F 12 00 00                  jmp 0x140af1ed9
00AF0C7A  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF0C7E  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AF0C82  E8 89 ED 76 FF                  call 0x14025fa10
00AF0C87  E8 24 CC 76 FF                  call 0x14025d8b0
00AF0C8C  48 8B CE                        mov rcx, rsi
00AF0C8F  E8 BC 86 80 FF                  call 0x1402f9350
00AF0C94  41 B0 01                        mov r8b, 1
00AF0C97  41 8A D7                        mov dl, r15b
00AF0C9A  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
00AF0CA2  E8 A9 E2 F3 FF                  call 0x140a2ef50
00AF0CA7  B8 5A 00 00 C0                  mov eax, 0xc000005a
00AF0CAC  E9 28 12 00 00                  jmp 0x140af1ed9
00AF0CB1  8B D8                           mov ebx, eax
00AF0CB3  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF0CB8  E8 93 86 80 FF                  call 0x1402f9350
00AF0CBD  8B C3                           mov eax, ebx
00AF0CBF  E9 15 12 00 00                  jmp 0x140af1ed9
00AF0CC4  41 83 FC 08                     cmp r12d, 8
00AF0CC8  0F 85 DA 01 00 00               jne 0x140af0ea8
00AF0CCE  49 8B 16                        mov rdx, qword ptr [r14]
00AF0CD1  48 89 94 24 58 01 00 00         mov qword ptr [rsp + 0x158], rdx
00AF0CD9  45 8A C7                        mov r8b, r15b
00AF0CDC  48 8B CE                        mov rcx, rsi
00AF0CDF  E8 F4 5B B1 FF                  call 0x1406068d8
00AF0CE4  E9 2B FA FF FF                  jmp 0x140af0714
00AF0CE9  8B D8                           mov ebx, eax
00AF0CEB  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF0CF0  E8 5B 86 80 FF                  call 0x1402f9350
00AF0CF5  8B C3                           mov eax, ebx
00AF0CF7  E9 DD 11 00 00                  jmp 0x140af1ed9
00AF0CFC  41 83 FC 04                     cmp r12d, 4
00AF0D00  0F 85 A2 01 00 00               jne 0x140af0ea8
00AF0D06  41 8B 1E                        mov ebx, dword ptr [r14]
00AF0D09  89 9C 24 08 01 00 00            mov dword ptr [rsp + 0x108], ebx
00AF0D10  41 8A D7                        mov dl, r15b
00AF0D13  48 8B 0D 5E 8D 4E 00            mov rcx, qword ptr [rip + 0x4e8d5e]
00AF0D1A  E8 01 11 D8 FF                  call 0x140871e20
00AF0D1F  84 C0                           test al, al
00AF0D21  0F 84 D9 F9 FF FF               je 0x140af0700
00AF0D27  85 DB                           test ebx, ebx
00AF0D29  74 0A                           je 0x140af0d35
00AF0D2B  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AF0D30  E9 D5 FD FF FF                  jmp 0x140af0b0a
00AF0D35  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF0D3E  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF0D45  90                              nop
00AF0D46  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00AF0D4B  B2 01                           mov dl, 1
00AF0D4D  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AF0D51  E8 CA 40 72 FF                  call 0x140214e20
00AF0D56  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF0D5A  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00AF0D5F  8B 86 C8 00 00 00               mov eax, dword ptr [rsi + 0xc8]
00AF0D65  A8 20                           test al, 0x20
00AF0D67  75 25                           jne 0x140af0d8e
00AF0D69  83 3D A0 72 4E 00 00            cmp dword ptr [rip + 0x4e72a0], 0
00AF0D70  74 08                           je 0x140af0d7a
00AF0D72  48 8B CE                        mov rcx, rsi
00AF0D75  E8 4E 0C CB FF                  call 0x1407a19c8
00AF0D7A  48 8B CE                        mov rcx, rsi
00AF0D7D  E8 DA D5 F9 FF                  call 0x140a8e35c
00AF0D82  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AF0D86  85 C0                           test eax, eax
00AF0D88  0F 88 86 F9 FF FF               js 0x140af0714
00AF0D8E  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF0D92  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AF0D96  E8 75 EC 76 FF                  call 0x14025fa10
00AF0D9B  E8 10 CB 76 FF                  call 0x14025d8b0
00AF0DA0  33 DB                           xor ebx, ebx
00AF0DA2  E9 A3 02 00 00                  jmp 0x140af104a
00AF0DA7  8B D8                           mov ebx, eax
00AF0DA9  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF0DAE  E8 9D 85 80 FF                  call 0x1402f9350
00AF0DB3  8B C3                           mov eax, ebx
00AF0DB5  E9 1F 11 00 00                  jmp 0x140af1ed9
00AF0DBA  83 EB 10                        sub ebx, 0x10
00AF0DBD  0F 84 CC 01 00 00               je 0x140af0f8f
00AF0DC3  83 EB 01                        sub ebx, 1
00AF0DC6  0F 84 14 01 00 00               je 0x140af0ee0
00AF0DCC  83 EB 02                        sub ebx, 2
00AF0DCF  0F 84 CD 00 00 00               je 0x140af0ea2
00AF0DD5  83 FB 04                        cmp ebx, 4
00AF0DD8  0F 85 F5 03 00 00               jne 0x140af11d3
00AF0DDE  44 3B E3                        cmp r12d, ebx
00AF0DE1  0F 85 C1 00 00 00               jne 0x140af0ea8
00AF0DE7  41 8B 06                        mov eax, dword ptr [r14]
00AF0DEA  89 84 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], eax
00AF0DF1  41 8A D7                        mov dl, r15b
00AF0DF4  48 8B 0D 85 8D 4E 00            mov rcx, qword ptr [rip + 0x4e8d85]
00AF0DFB  E8 20 10 D8 FF                  call 0x140871e20
00AF0E00  84 C0                           test al, al
00AF0E02  0F 84 F8 F8 FF FF               je 0x140af0700
00AF0E08  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF0E11  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF0E18  90                              nop
00AF0E19  B2 01                           mov dl, 1
00AF0E1B  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF0E20  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
00AF0E24  E8 F7 3F 72 FF                  call 0x140214e20
00AF0E29  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF0E2D  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
00AF0E32  8B 82 C8 00 00 00               mov eax, dword ptr [rdx + 0xc8]
00AF0E38  39 BC 24 B0 00 00 00            cmp dword ptr [rsp + 0xb0], edi
00AF0E3F  74 06                           je 0x140af0e47
00AF0E41  0F BA E8 09                     bts eax, 9
00AF0E45  EB 04                           jmp 0x140af0e4b
00AF0E47  0F BA F0 09                     btr eax, 9
00AF0E4B  89 82 C8 00 00 00               mov dword ptr [rdx + 0xc8], eax
00AF0E51  48 8B 0D B0 1E 52 FF            mov rcx, qword ptr [rip - 0xade150]
00AF0E58  48 8B C1                        mov rax, rcx
00AF0E5B  F0 48 0F C1 05 8C DD 31 00      lock xadd qword ptr [rip + 0x31dd8c], rax
00AF0E64  48 03 C1                        add rax, rcx
00AF0E67  89 42 38                        mov dword ptr [rdx + 0x38], eax
00AF0E6A  48 C1 E8 20                     shr rax, 0x20
00AF0E6E  89 42 3C                        mov dword ptr [rdx + 0x3c], eax
00AF0E71  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF0E75  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00AF0E7A  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AF0E7E  E8 8D EB 76 FF                  call 0x14025fa10
00AF0E83  E8 28 CA 76 FF                  call 0x14025d8b0
00AF0E88  33 DB                           xor ebx, ebx
00AF0E8A  E9 7B FC FF FF                  jmp 0x140af0b0a
00AF0E8F  8B D8                           mov ebx, eax
00AF0E91  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF0E96  E8 B5 84 80 FF                  call 0x1402f9350
00AF0E9B  8B C3                           mov eax, ebx
00AF0E9D  E9 37 10 00 00                  jmp 0x140af1ed9
00AF0EA2  41 83 FC 08                     cmp r12d, 8
00AF0EA6  74 0A                           je 0x140af0eb2
00AF0EA8  BB 04 00 00 C0                  mov ebx, 0xc0000004
00AF0EAD  E9 58 FC FF FF                  jmp 0x140af0b0a
00AF0EB2  49 8B 16                        mov rdx, qword ptr [r14]
00AF0EB5  48 89 94 24 50 01 00 00         mov qword ptr [rsp + 0x150], rdx
00AF0EBD  45 8A C7                        mov r8b, r15b
00AF0EC0  48 8B CE                        mov rcx, rsi
00AF0EC3  E8 B0 9F 9B FF                  call 0x1404aae78
00AF0EC8  E9 47 F8 FF FF                  jmp 0x140af0714
00AF0ECD  8B D8                           mov ebx, eax
00AF0ECF  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF0ED4  E8 77 84 80 FF                  call 0x1402f9350
00AF0ED9  8B C3                           mov eax, ebx
00AF0EDB  E9 F9 0F 00 00                  jmp 0x140af1ed9
00AF0EE0  41 83 FC 08                     cmp r12d, 8
00AF0EE4  75 C2                           jne 0x140af0ea8
00AF0EE6  49 8B 06                        mov rax, qword ptr [r14]
00AF0EE9  48 89 84 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rax
00AF0EF1  41 8A D7                        mov dl, r15b
00AF0EF4  48 8B 0D 7D 8B 4E 00            mov rcx, qword ptr [rip + 0x4e8b7d]
00AF0EFB  E8 20 0F D8 FF                  call 0x140871e20
00AF0F00  84 C0                           test al, al
00AF0F02  0F 84 F8 F7 FF FF               je 0x140af0700
00AF0F08  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF0F11  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF0F18  90                              nop
00AF0F19  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00AF0F1E  B2 01                           mov dl, 1
00AF0F20  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AF0F24  E8 F7 3E 72 FF                  call 0x140214e20
00AF0F29  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF0F2D  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
00AF0F32  8B 82 E4 00 00 00               mov eax, dword ptr [rdx + 0xe4]
00AF0F38  0B 82 E0 00 00 00               or eax, dword ptr [rdx + 0xe0]
00AF0F3E  75 0F                           jne 0x140af0f4f
00AF0F40  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
00AF0F48  48 89 82 E0 00 00 00            mov qword ptr [rdx + 0xe0], rax
00AF0F4F  48 8B 0D B2 1D 52 FF            mov rcx, qword ptr [rip - 0xade24e]
00AF0F56  48 8B C1                        mov rax, rcx
00AF0F59  F0 48 0F C1 05 8E DC 31 00      lock xadd qword ptr [rip + 0x31dc8e], rax
00AF0F62  48 03 C1                        add rax, rcx
00AF0F65  89 42 38                        mov dword ptr [rdx + 0x38], eax
00AF0F68  48 C1 E8 20                     shr rax, 0x20
00AF0F6C  89 42 3C                        mov dword ptr [rdx + 0x3c], eax
00AF0F6F  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF0F73  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AF0F77  E9 C2 00 00 00                  jmp 0x140af103e
00AF0F7C  8B D8                           mov ebx, eax
00AF0F7E  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF0F83  E8 C8 83 80 FF                  call 0x1402f9350
00AF0F88  8B C3                           mov eax, ebx
00AF0F8A  E9 4A 0F 00 00                  jmp 0x140af1ed9
00AF0F8F  48 89 BC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdi
00AF0F97  41 8A D7                        mov dl, r15b
00AF0F9A  48 8B 0D D7 8A 4E 00            mov rcx, qword ptr [rip + 0x4e8ad7]
00AF0FA1  E8 7A 0E D8 FF                  call 0x140871e20
00AF0FA6  84 C0                           test al, al
00AF0FA8  0F 84 52 F7 FF FF               je 0x140af0700
00AF0FAE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF0FB7  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF0FBE  90                              nop
00AF0FBF  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00AF0FC4  B2 01                           mov dl, 1
00AF0FC6  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AF0FCA  E8 F1 0B 72 FF                  call 0x140211bc0
00AF0FCF  8A 5E 77                        mov bl, byte ptr [rsi + 0x77]
00AF0FD2  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AF0FD6  E8 35 EA 76 FF                  call 0x14025fa10
00AF0FDB  E8 D0 C8 76 FF                  call 0x14025d8b0
00AF0FE0  84 DB                           test bl, bl
00AF0FE2  0F 85 43 FD FF FF               jne 0x140af0d2b
00AF0FE8  4D 85 F6                        test r14, r14
00AF0FEB  75 67                           jne 0x140af1054
00AF0FED  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF0FF6  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF0FFD  90                              nop
00AF0FFE  B2 01                           mov dl, 1
00AF1000  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AF1004  E8 17 3E 72 FF                  call 0x140214e20
00AF1009  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF100D  C6 46 77 01                     mov byte ptr [rsi + 0x77], 1
00AF1011  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
00AF1016  48 8B 0D EB 1C 52 FF            mov rcx, qword ptr [rip - 0xade315]
00AF101D  48 8B C1                        mov rax, rcx
00AF1020  F0 48 0F C1 05 C7 DB 31 00      lock xadd qword ptr [rip + 0x31dbc7], rax
00AF1029  48 03 C1                        add rax, rcx
00AF102C  89 42 38                        mov dword ptr [rdx + 0x38], eax
00AF102F  48 C1 E8 20                     shr rax, 0x20
00AF1033  89 42 3C                        mov dword ptr [rdx + 0x3c], eax
00AF1036  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF103A  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AF103E  E8 CD E9 76 FF                  call 0x14025fa10
00AF1043  E8 68 C8 76 FF                  call 0x14025d8b0
00AF1048  8B DF                           mov ebx, edi
00AF104A  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00AF104F  E9 B6 FA FF FF                  jmp 0x140af0b0a
00AF1054  48 8D 84 24 A8 00 00 00         lea rax, [rsp + 0xa8]
00AF105C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AF1061  41 8A D7                        mov dl, r15b
00AF1064  49 8B CE                        mov rcx, r14
00AF1067  E8 14 EC CA FF                  call 0x14079fc80
00AF106C  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AF1070  85 C0                           test eax, eax
00AF1072  0F 88 9C F6 FF FF               js 0x140af0714
00AF1078  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF1081  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF1088  90                              nop
00AF1089  B2 01                           mov dl, 1
00AF108B  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AF108F  E8 8C 3D 72 FF                  call 0x140214e20
00AF1094  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF1098  C6 46 77 02                     mov byte ptr [rsi + 0x77], 2
00AF109C  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
00AF10A1  49 8D 58 58                     lea rbx, [r8 + 0x58]
00AF10A5  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
00AF10AD  0F 10 01                        movups xmm0, xmmword ptr [rcx]
00AF10B0  0F 11 03                        movups xmmword ptr [rbx], xmm0
00AF10B3  F2 0F 10 49 10                  movsd xmm1, qword ptr [rcx + 0x10]
00AF10B8  F2 0F 11 4B 10                  movsd qword ptr [rbx + 0x10], xmm1
00AF10BD  8B 41 18                        mov eax, dword ptr [rcx + 0x18]
00AF10C0  89 43 18                        mov dword ptr [rbx + 0x18], eax
00AF10C3  0F B7 41 1C                     movzx eax, word ptr [rcx + 0x1c]
00AF10C7  66 89 43 1C                     mov word ptr [rbx + 0x1c], ax
00AF10CB  8A 41 1E                        mov al, byte ptr [rcx + 0x1e]
00AF10CE  88 43 1E                        mov byte ptr [rbx + 0x1e], al
00AF10D1  48 8B 15 30 1C 52 FF            mov rdx, qword ptr [rip - 0xade3d0]
00AF10D8  48 8B C2                        mov rax, rdx
00AF10DB  F0 48 0F C1 05 0C DB 31 00      lock xadd qword ptr [rip + 0x31db0c], rax
00AF10E4  48 03 C2                        add rax, rdx
00AF10E7  41 89 40 38                     mov dword ptr [r8 + 0x38], eax
00AF10EB  48 C1 E8 20                     shr rax, 0x20
00AF10EF  41 89 40 3C                     mov dword ptr [r8 + 0x3c], eax
00AF10F3  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF10F7  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AF10FB  E8 10 E9 76 FF                  call 0x14025fa10
00AF1100  E8 AB C7 76 FF                  call 0x14025d8b0
00AF1105  B2 01                           mov dl, 1
00AF1107  48 8B CB                        mov rcx, rbx
00AF110A  E8 D1 C0 CA FF                  call 0x14079d1e0
00AF110F  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF1114  E8 37 82 80 FF                  call 0x1402f9350
00AF1119  41 8A D7                        mov dl, r15b
00AF111C  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
00AF1124  E8 53 F0 CA FF                  call 0x1407a017c
00AF1129  E9 F8 F7 FF FF                  jmp 0x140af0926
00AF112E  8B D8                           mov ebx, eax
00AF1130  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF1135  E8 16 82 80 FF                  call 0x1402f9350
00AF113A  8A 54 24 5D                     mov dl, byte ptr [rsp + 0x5d]
00AF113E  48 8B 8C 24 A8 00 00 00         mov rcx, qword ptr [rsp + 0xa8]
00AF1146  E8 31 F0 CA FF                  call 0x1407a017c
00AF114B  8B C3                           mov eax, ebx
00AF114D  E9 87 0D 00 00                  jmp 0x140af1ed9
00AF1152  41 83 FC 04                     cmp r12d, 4
00AF1156  0F 85 4C FD FF FF               jne 0x140af0ea8
00AF115C  41 8B 16                        mov edx, dword ptr [r14]
00AF115F  89 94 24 E0 00 00 00            mov dword ptr [rsp + 0xe0], edx
00AF1166  48 8B CE                        mov rcx, rsi
00AF1169  E8 46 17 FB FF                  call 0x140aa28b4
00AF116E  E9 15 FD FF FF                  jmp 0x140af0e88
00AF1173  8B D8                           mov ebx, eax
00AF1175  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF117A  E8 D1 81 80 FF                  call 0x1402f9350
00AF117F  8B C3                           mov eax, ebx
00AF1181  E9 53 0D 00 00                  jmp 0x140af1ed9
00AF1186  83 EB 19                        sub ebx, 0x19
00AF1189  0F 84 5A 07 00 00               je 0x140af18e9
00AF118F  83 EB 01                        sub ebx, 1
00AF1192  0F 84 88 06 00 00               je 0x140af1820
00AF1198  83 EB 01                        sub ebx, 1
00AF119B  0F 84 19 06 00 00               je 0x140af17ba
00AF11A1  83 EB 02                        sub ebx, 2
00AF11A4  0F 84 A7 04 00 00               je 0x140af1651
00AF11AA  83 EB 0A                        sub ebx, 0xa
00AF11AD  0F 84 6F 03 00 00               je 0x140af1522
00AF11B3  83 EB 03                        sub ebx, 3
00AF11B6  0F 84 19 03 00 00               je 0x140af14d5
00AF11BC  83 EB 03                        sub ebx, 3
00AF11BF  0F 84 4C 02 00 00               je 0x140af1411
00AF11C5  83 EB 07                        sub ebx, 7
00AF11C8  0F 84 BE 01 00 00               je 0x140af138c
00AF11CE  83 FB 06                        cmp ebx, 6
00AF11D1  74 0A                           je 0x140af11dd
00AF11D3  B8 0D 00 00 C0                  mov eax, 0xc000000d
00AF11D8  E9 FC 0C 00 00                  jmp 0x140af1ed9
00AF11DD  E8 EA 54 B1 FF                  call 0x1406066cc
00AF11E2  85 C0                           test eax, eax
00AF11E4  0F 84 98 01 00 00               je 0x140af1382
00AF11EA  89 BC 24 D4 00 00 00            mov dword ptr [rsp + 0xd4], edi
00AF11F1  4D 85 F6                        test r14, r14
00AF11F4  0F 84 31 FB FF FF               je 0x140af0d2b
00AF11FA  45 85 E4                        test r12d, r12d
00AF11FD  0F 84 28 FB FF FF               je 0x140af0d2b
00AF1203  41 F6 C4 01                     test r12b, 1
00AF1207  0F 85 1E FB FF FF               jne 0x140af0d2b
00AF120D  41 81 FC FC FF 00 00            cmp r12d, 0xfffc
00AF1214  0F 87 11 FB FF FF               ja 0x140af0d2b
00AF121A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF1223  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
00AF122A  8A 80 FA 05 00 00               mov al, byte ptr [rax + 0x5fa]
00AF1230  8A C8                           mov cl, al
00AF1232  80 E1 07                        and cl, 7
00AF1235  80 F9 01                        cmp cl, 1
00AF1238  72 06                           jb 0x140af1240
00AF123A  24 F0                           and al, 0xf0
00AF123C  3C 30                           cmp al, 0x30
00AF123E  74 17                           je 0x140af1257
00AF1240  41 8A D7                        mov dl, r15b
00AF1243  48 8B 0D 2E 88 4E 00            mov rcx, qword ptr [rip + 0x4e882e]
00AF124A  E8 D1 0B D8 FF                  call 0x140871e20
00AF124F  84 C0                           test al, al
00AF1251  0F 84 21 01 00 00               je 0x140af1378
00AF1257  41 B8 53 65 20 20               mov r8d, 0x20206553
00AF125D  49 8B D4                        mov rdx, r12
00AF1260  B9 00 01 00 00                  mov ecx, 0x100
00AF1265  E8 86 0E 09 00                  call 0x140b820f0
00AF126A  48 8B F0                        mov rsi, rax
00AF126D  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00AF1272  48 85 C0                        test rax, rax
00AF1275  75 0A                           jne 0x140af1281
00AF1277  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00AF127C  E9 C9 FD FF FF                  jmp 0x140af104a
00AF1281  45 84 FF                        test r15b, r15b
00AF1284  74 1C                           je 0x140af12a2
00AF1286  41 F6 C6 01                     test r14b, 1
00AF128A  0F 85 6D 0C 00 00               jne 0x140af1efd
00AF1290  4B 8D 04 34                     lea rax, [r12 + r14]
00AF1294  49 3B C5                        cmp rax, r13
00AF1297  77 05                           ja 0x140af129e
00AF1299  49 3B C6                        cmp rax, r14
00AF129C  73 04                           jae 0x140af12a2
00AF129E  41 8A 45 00                     mov al, byte ptr [r13]
00AF12A2  4D 8B C4                        mov r8, r12
00AF12A5  49 8B D6                        mov rdx, r14
00AF12A8  48 8B CE                        mov rcx, rsi
00AF12AB  E8 90 55 BD FF                  call 0x1406c6840
00AF12B0  90                              nop
00AF12B1  48 89 B4 24 D8 00 00 00         mov qword ptr [rsp + 0xd8], rsi
00AF12B9  66 44 89 A4 24 D0 00 00 00      mov word ptr [rsp + 0xd0], r12w
00AF12C2  66 44 89 A4 24 D2 00 00 00      mov word ptr [rsp + 0xd2], r12w
00AF12CB  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF12D4  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF12DB  90                              nop
00AF12DC  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
00AF12E1  B2 01                           mov dl, 1
00AF12E3  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AF12E7  E8 34 3B 72 FF                  call 0x140214e20
00AF12EC  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF12F0  48 8D 94 24 D0 00 00 00         lea rdx, [rsp + 0xd0]
00AF12F8  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00AF12FD  48 8B CB                        mov rcx, rbx
00AF1300  E8 2B F8 CA FF                  call 0x1407a0b30
00AF1305  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AF1309  85 C0                           test eax, eax
00AF130B  78 2B                           js 0x140af1338
00AF130D  83 8B 90 04 00 00 02            or dword ptr [rbx + 0x490], 2
00AF1314  85 C0                           test eax, eax
00AF1316  78 20                           js 0x140af1338
00AF1318  48 8B 0D E9 19 52 FF            mov rcx, qword ptr [rip - 0xade617]
00AF131F  48 8B C1                        mov rax, rcx
00AF1322  F0 48 0F C1 05 C5 D8 31 00      lock xadd qword ptr [rip + 0x31d8c5], rax
00AF132B  48 03 C1                        add rax, rcx
00AF132E  89 43 38                        mov dword ptr [rbx + 0x38], eax
00AF1331  48 C1 E8 20                     shr rax, 0x20
00AF1335  89 43 3C                        mov dword ptr [rbx + 0x3c], eax
00AF1338  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF133C  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AF1340  E8 CB E6 76 FF                  call 0x14025fa10
00AF1345  E8 66 C5 76 FF                  call 0x14025d8b0
00AF134A  33 D2                           xor edx, edx
00AF134C  48 8B CE                        mov rcx, rsi
00AF134F  E8 1C 15 09 00                  call 0x140b82870
00AF1354  E9 EF 02 00 00                  jmp 0x140af1648
00AF1359  8B D8                           mov ebx, eax
00AF135B  33 D2                           xor edx, edx
00AF135D  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00AF1362  E8 09 15 09 00                  call 0x140b82870
00AF1367  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF136C  E8 DF 7F 80 FF                  call 0x1402f9350
00AF1371  8B C3                           mov eax, ebx
00AF1373  E9 61 0B 00 00                  jmp 0x140af1ed9
00AF1378  BB 61 00 00 C0                  mov ebx, 0xc0000061
00AF137D  E9 C8 FC FF FF                  jmp 0x140af104a
00AF1382  BB 03 00 00 C0                  mov ebx, 0xc0000003
00AF1387  E9 7E F7 FF FF                  jmp 0x140af0b0a
00AF138C  E8 C7 19 A0 FF                  call 0x1404f2d58
00AF1391  85 C0                           test eax, eax
00AF1393  74 ED                           je 0x140af1382
00AF1395  41 83 FC 04                     cmp r12d, 4
00AF1399  0F 85 09 FB FF FF               jne 0x140af0ea8
00AF139F  45 84 FF                        test r15b, r15b
00AF13A2  74 0A                           je 0x140af13ae
00AF13A4  49 8B CE                        mov rcx, r14
00AF13A7  E8 5C 4A C1 FF                  call 0x140705e08
00AF13AC  EB 03                           jmp 0x140af13b1
00AF13AE  41 8B 06                        mov eax, dword ptr [r14]
00AF13B1  89 44 24 7C                     mov dword ptr [rsp + 0x7c], eax
00AF13B5  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF13BE  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF13C5  90                              nop
00AF13C6  B2 01                           mov dl, 1
00AF13C8  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF13CD  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
00AF13D1  E8 4A 3A 72 FF                  call 0x140214e20
00AF13D6  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF13DA  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
00AF13DF  8B 82 90 04 00 00               mov eax, dword ptr [rdx + 0x490]
00AF13E5  39 7C 24 7C                     cmp dword ptr [rsp + 0x7c], edi
00AF13E9  74 05                           je 0x140af13f0
00AF13EB  83 C8 01                        or eax, 1
00AF13EE  EB 03                           jmp 0x140af13f3
00AF13F0  83 E0 FE                        and eax, 0xfffffffe
00AF13F3  89 82 90 04 00 00               mov dword ptr [rdx + 0x490], eax
00AF13F9  E9 53 FA FF FF                  jmp 0x140af0e51
00AF13FE  8B D8                           mov ebx, eax
00AF1400  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF1405  E8 46 7F 80 FF                  call 0x1402f9350
00AF140A  8B C3                           mov eax, ebx
00AF140C  E9 C8 0A 00 00                  jmp 0x140af1ed9
00AF1411  41 8A D7                        mov dl, r15b
00AF1414  48 8B 0D 5D 86 4E 00            mov rcx, qword ptr [rip + 0x4e865d]
00AF141B  E8 00 0A D8 FF                  call 0x140871e20
00AF1420  84 C0                           test al, al
00AF1422  0F 84 D8 F2 FF FF               je 0x140af0700
00AF1428  41 83 FC 04                     cmp r12d, 4
00AF142C  0F 85 76 FA FF FF               jne 0x140af0ea8
00AF1432  41 8B 06                        mov eax, dword ptr [r14]
00AF1435  89 84 24 E4 00 00 00            mov dword ptr [rsp + 0xe4], eax
00AF143C  85 C0                           test eax, eax
00AF143E  0F 85 8B 04 00 00               jne 0x140af18cf
00AF1444  F7 86 C8 00 00 00 00 00 08 00   test dword ptr [rsi + 0xc8], 0x80000
00AF144E  0F 84 7B 04 00 00               je 0x140af18cf
00AF1454  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF145D  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF1464  90                              nop
00AF1465  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00AF146A  B2 01                           mov dl, 1
00AF146C  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AF1470  E8 AB 39 72 FF                  call 0x140214e20
00AF1475  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF1479  0F BA B6 C8 00 00 00 13         btr dword ptr [rsi + 0xc8], 0x13
00AF1481  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
00AF1486  48 8B 0D 7B 18 52 FF            mov rcx, qword ptr [rip - 0xade785]
00AF148D  48 8B C1                        mov rax, rcx
00AF1490  F0 48 0F C1 05 57 D7 31 00      lock xadd qword ptr [rip + 0x31d757], rax
00AF1499  48 03 C1                        add rax, rcx
00AF149C  89 42 38                        mov dword ptr [rdx + 0x38], eax
00AF149F  48 C1 E8 20                     shr rax, 0x20
00AF14A3  89 42 3C                        mov dword ptr [rdx + 0x3c], eax
00AF14A6  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF14AA  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AF14AE  E8 5D E5 76 FF                  call 0x14025fa10
00AF14B3  E8 F8 C3 76 FF                  call 0x14025d8b0
00AF14B8  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00AF14BD  E9 0D 04 00 00                  jmp 0x140af18cf
00AF14C2  8B D8                           mov ebx, eax
00AF14C4  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF14C9  E8 82 7E 80 FF                  call 0x1402f9350
00AF14CE  8B C3                           mov eax, ebx
00AF14D0  E9 04 0A 00 00                  jmp 0x140af1ed9
00AF14D5  41 83 FC 04                     cmp r12d, 4
00AF14D9  0F 85 C9 F9 FF FF               jne 0x140af0ea8
00AF14DF  41 8B 1E                        mov ebx, dword ptr [r14]
00AF14E2  89 9C 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], ebx
00AF14E9  41 8A D7                        mov dl, r15b
00AF14EC  48 8B 0D 85 85 4E 00            mov rcx, qword ptr [rip + 0x4e8585]
00AF14F3  E8 28 09 D8 FF                  call 0x140871e20
00AF14F8  84 C0                           test al, al
00AF14FA  0F 84 00 F2 FF FF               je 0x140af0700
00AF1500  8B D3                           mov edx, ebx
00AF1502  48 8B CE                        mov rcx, rsi
00AF1505  E8 CE B9 CA FF                  call 0x14079ced8
00AF150A  E9 05 F2 FF FF                  jmp 0x140af0714
00AF150F  8B D8                           mov ebx, eax
00AF1511  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF1516  E8 35 7E 80 FF                  call 0x1402f9350
00AF151B  8B C3                           mov eax, ebx
00AF151D  E9 B7 09 00 00                  jmp 0x140af1ed9
00AF1522  48 89 BC 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdi
00AF152A  4D 85 F6                        test r14, r14
00AF152D  0F 84 75 F9 FF FF               je 0x140af0ea8
00AF1533  41 83 FC 10                     cmp r12d, 0x10
00AF1537  0F 82 6B F9 FF FF               jb 0x140af0ea8
00AF153D  4C 8D 84 24 98 00 00 00         lea r8, [rsp + 0x98]
00AF1545  41 8A D7                        mov dl, r15b
00AF1548  49 8B CE                        mov rcx, r14
00AF154B  E8 BC 08 E8 FF                  call 0x140971e0c
00AF1550  44 8B F0                        mov r14d, eax
00AF1553  85 C0                           test eax, eax
00AF1555  79 08                           jns 0x140af155f
00AF1557  41 8B DE                        mov ebx, r14d
00AF155A  E9 AB F5 FF FF                  jmp 0x140af0b0a
00AF155F  41 8A D7                        mov dl, r15b
00AF1562  48 8B 0D 0F 85 4E 00            mov rcx, qword ptr [rip + 0x4e850f]
00AF1569  E8 B2 08 D8 FF                  call 0x140871e20
00AF156E  BB 61 00 00 C0                  mov ebx, 0xc0000061
00AF1573  84 C0                           test al, al
00AF1575  44 0F 44 F3                     cmove r14d, ebx
00AF1579  44 89 74 24 58                  mov dword ptr [rsp + 0x58], r14d
00AF157E  45 85 F6                        test r14d, r14d
00AF1581  79 12                           jns 0x140af1595
00AF1583  41 8A D7                        mov dl, r15b
00AF1586  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00AF158E  E8 51 BB F5 FF                  call 0x140a4d0e4
00AF1593  EB C2                           jmp 0x140af1557
00AF1595  48 8B 9C 24 98 00 00 00         mov rbx, qword ptr [rsp + 0x98]
00AF159D  48 8B 13                        mov rdx, qword ptr [rbx]
00AF15A0  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
00AF15A4  E8 63 ED F5 FF                  call 0x140a5030c
00AF15A9  44 8A F0                        mov r14b, al
00AF15AC  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
00AF15B5  66 FF 89 E4 01 00 00            dec word ptr [rcx + 0x1e4]
00AF15BC  90                              nop
00AF15BD  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00AF15C2  B2 01                           mov dl, 1
00AF15C4  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AF15C8  E8 53 38 72 FF                  call 0x140214e20
00AF15CD  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF15D1  4C 8B 84 24 98 00 00 00         mov r8, qword ptr [rsp + 0x98]
00AF15D9  4D 8B 00                        mov r8, qword ptr [r8]
00AF15DC  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
00AF15E0  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00AF15E5  48 8B 8B 08 03 00 00            mov rcx, qword ptr [rbx + 0x308]
00AF15EC  E8 2B 77 8B FF                  call 0x1403a8d1c
00AF15F1  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AF15F5  85 C0                           test eax, eax
00AF15F7  78 0D                           js 0x140af1606
00AF15F9  45 84 F6                        test r14b, r14b
00AF15FC  74 08                           je 0x140af1606
00AF15FE  0F BA AB C8 00 00 00 11         bts dword ptr [rbx + 0xc8], 0x11
00AF1606  48 8B 0D FB 16 52 FF            mov rcx, qword ptr [rip - 0xade905]
00AF160D  48 8B C1                        mov rax, rcx
00AF1610  F0 48 0F C1 05 D7 D5 31 00      lock xadd qword ptr [rip + 0x31d5d7], rax
00AF1619  48 03 C1                        add rax, rcx
00AF161C  89 43 38                        mov dword ptr [rbx + 0x38], eax
00AF161F  48 C1 E8 20                     shr rax, 0x20
00AF1623  89 43 3C                        mov dword ptr [rbx + 0x3c], eax
00AF1626  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF162A  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AF162E  E8 DD E3 76 FF                  call 0x14025fa10
00AF1633  E8 78 C2 76 FF                  call 0x14025d8b0
00AF1638  41 8A D7                        mov dl, r15b
00AF163B  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
00AF1643  E8 9C BA F5 FF                  call 0x140a4d0e4
00AF1648  8B 5C 24 58                     mov ebx, dword ptr [rsp + 0x58]
00AF164C  E9 F9 F9 FF FF                  jmp 0x140af104a
00AF1651  E8 32 E1 9F FF                  call 0x1404ef788
00AF1656  85 C0                           test eax, eax
00AF1658  0F 84 24 FD FF FF               je 0x140af1382
00AF165E  41 83 FC 04                     cmp r12d, 4
00AF1662  0F 85 40 F8 FF FF               jne 0x140af0ea8
00AF1668  45 84 FF                        test r15b, r15b
00AF166B  74 11                           je 0x140af167e
00AF166D  49 8B CE                        mov rcx, r14
00AF1670  E8 93 47 C1 FF                  call 0x140705e08
00AF1675  89 84 24 B4 00 00 00            mov dword ptr [rsp + 0xb4], eax
00AF167C  EB 0F                           jmp 0x140af168d
00AF167E  41 8B 06                        mov eax, dword ptr [r14]
00AF1681  89 84 24 B4 00 00 00            mov dword ptr [rsp + 0xb4], eax
00AF1688  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00AF168D  85 C0                           test eax, eax
00AF168F  74 0A                           je 0x140af169b
00AF1691  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00AF1696  E9 6F F4 FF FF                  jmp 0x140af0b0a
00AF169B  F7 86 C8 00 00 00 00 40 00 00   test dword ptr [rsi + 0xc8], 0x4000
00AF16A5  75 0A                           jne 0x140af16b1
00AF16A7  BB 00 A2 00 C0                  mov ebx, 0xc000a200
00AF16AC  E9 59 F4 FF FF                  jmp 0x140af0b0a
00AF16B1  41 8A D7                        mov dl, r15b
00AF16B4  48 8B 0D BD 83 4E 00            mov rcx, qword ptr [rip + 0x4e83bd]
00AF16BB  E8 60 07 D8 FF                  call 0x140871e20
00AF16C0  84 C0                           test al, al
00AF16C2  0F 84 38 F0 FF FF               je 0x140af0700
00AF16C8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF16D1  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF16D8  90                              nop
00AF16D9  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
00AF16DE  B2 01                           mov dl, 1
00AF16E0  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AF16E4  E8 37 37 72 FF                  call 0x140214e20
00AF16E9  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF16ED  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00AF16F2  48 8B 93 10 03 00 00            mov rdx, qword ptr [rbx + 0x310]
00AF16F9  48 8B CB                        mov rcx, rbx
00AF16FC  E8 8B EA 90 FF                  call 0x14040018c
00AF1701  0F BA B6 C8 00 00 00 0E         btr dword ptr [rsi + 0xc8], 0xe
00AF1709  48 8B 8B 10 03 00 00            mov rcx, qword ptr [rbx + 0x310]
00AF1710  48 85 C9                        test rcx, rcx
00AF1713  74 0E                           je 0x140af1723
00AF1715  33 D2                           xor edx, edx
00AF1717  E8 54 11 09 00                  call 0x140b82870
00AF171C  48 89 BB 10 03 00 00            mov qword ptr [rbx + 0x310], rdi
00AF1723  48 8B 8B 18 03 00 00            mov rcx, qword ptr [rbx + 0x318]
00AF172A  48 85 C9                        test rcx, rcx
00AF172D  74 28                           je 0x140af1757
00AF172F  33 D2                           xor edx, edx
00AF1731  E8 3A 11 09 00                  call 0x140b82870
00AF1736  48 89 BB 18 03 00 00            mov qword ptr [rbx + 0x318], rdi
00AF173D  89 BB 20 03 00 00               mov dword ptr [rbx + 0x320], edi
00AF1743  48 8D 8B 28 03 00 00            lea rcx, [rbx + 0x328]
00AF174A  33 D2                           xor edx, edx
00AF174C  41 B8 10 01 00 00               mov r8d, 0x110
00AF1752  E8 E9 54 BD FF                  call 0x1406c6c40
00AF1757  48 8B 93 38 04 00 00            mov rdx, qword ptr [rbx + 0x438]
00AF175E  48 85 D2                        test rdx, rdx
00AF1761  74 0F                           je 0x140af1772
00AF1763  8B 4B 78                        mov ecx, dword ptr [rbx + 0x78]
00AF1766  E8 51 46 F6 FF                  call 0x140a55dbc
00AF176B  48 89 BB 38 04 00 00            mov qword ptr [rbx + 0x438], rdi
00AF1772  4C 8B 83 40 04 00 00            mov r8, qword ptr [rbx + 0x440]
00AF1779  4D 85 C0                        test r8, r8
00AF177C  74 1C                           je 0x140af179a
00AF177E  48 8B 8B D8 00 00 00            mov rcx, qword ptr [rbx + 0xd8]
00AF1785  48 83 C1 60                     add rcx, 0x60
00AF1789  45 33 C9                        xor r9d, r9d
00AF178C  33 D2                           xor edx, edx
00AF178E  E8 91 7C F2 FF                  call 0x140a19424
00AF1793  48 89 BB 40 04 00 00            mov qword ptr [rbx + 0x440], rdi
00AF179A  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF179E  49 8B 4E 30                     mov rcx, qword ptr [r14 + 0x30]
00AF17A2  E9 EF F5 FF FF                  jmp 0x140af0d96
00AF17A7  8B D8                           mov ebx, eax
00AF17A9  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF17AE  E8 9D 7B 80 FF                  call 0x1402f9350
00AF17B3  8B C3                           mov eax, ebx
00AF17B5  E9 1F 07 00 00                  jmp 0x140af1ed9
00AF17BA  41 83 FC 04                     cmp r12d, 4
00AF17BE  0F 85 E4 F6 FF FF               jne 0x140af0ea8
00AF17C4  41 8B 06                        mov eax, dword ptr [r14]
00AF17C7  89 84 24 B8 00 00 00            mov dword ptr [rsp + 0xb8], eax
00AF17CE  41 8A D7                        mov dl, r15b
00AF17D1  48 8B 0D A0 82 4E 00            mov rcx, qword ptr [rip + 0x4e82a0]
00AF17D8  E8 43 06 D8 FF                  call 0x140871e20
00AF17DD  84 C0                           test al, al
00AF17DF  0F 84 1B EF FF FF               je 0x140af0700
00AF17E5  40 38 BE CC 00 00 00            cmp byte ptr [rsi + 0xcc], dil
00AF17EC  74 0A                           je 0x140af17f8
00AF17EE  BB 2B 01 00 C0                  mov ebx, 0xc000012b
00AF17F3  E9 12 F3 FF FF                  jmp 0x140af0b0a
00AF17F8  48 8D 94 24 B8 00 00 00         lea rdx, [rsp + 0xb8]
00AF1800  48 8B CE                        mov rcx, rsi
00AF1803  E8 C4 D5 F6 FF                  call 0x140a5edcc
00AF1808  E9 07 EF FF FF                  jmp 0x140af0714
00AF180D  8B D8                           mov ebx, eax
00AF180F  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF1814  E8 37 7B 80 FF                  call 0x1402f9350
00AF1819  8B C3                           mov eax, ebx
00AF181B  E9 B9 06 00 00                  jmp 0x140af1ed9
00AF1820  41 83 FC 04                     cmp r12d, 4
00AF1824  0F 85 7E F6 FF FF               jne 0x140af0ea8
00AF182A  41 8B 06                        mov eax, dword ptr [r14]
00AF182D  89 84 24 BC 00 00 00            mov dword ptr [rsp + 0xbc], eax
00AF1834  85 C0                           test eax, eax
00AF1836  74 17                           je 0x140af184f
00AF1838  41 8A D7                        mov dl, r15b
00AF183B  48 8B 0D 36 82 4E 00            mov rcx, qword ptr [rip + 0x4e8236]
00AF1842  E8 D9 05 D8 FF                  call 0x140871e20
00AF1847  84 C0                           test al, al
00AF1849  0F 84 B1 EE FF FF               je 0x140af0700
00AF184F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF1858  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF185F  90                              nop
00AF1860  B2 01                           mov dl, 1
00AF1862  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF1867  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
00AF186B  E8 B0 35 72 FF                  call 0x140214e20
00AF1870  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF1874  48 8B 54 24 50                  mov rdx, qword ptr [rsp + 0x50]
00AF1879  8B 82 C8 00 00 00               mov eax, dword ptr [rdx + 0xc8]
00AF187F  39 BC 24 BC 00 00 00            cmp dword ptr [rsp + 0xbc], edi
00AF1886  74 06                           je 0x140af188e
00AF1888  0F BA E8 0C                     bts eax, 0xc
00AF188C  EB 04                           jmp 0x140af1892
00AF188E  0F BA F0 0C                     btr eax, 0xc
00AF1892  89 82 C8 00 00 00               mov dword ptr [rdx + 0xc8], eax
00AF1898  48 8B 0D 69 14 52 FF            mov rcx, qword ptr [rip - 0xadeb97]
00AF189F  48 8B C1                        mov rax, rcx
00AF18A2  F0 48 0F C1 05 45 D3 31 00      lock xadd qword ptr [rip + 0x31d345], rax
00AF18AB  48 03 C1                        add rax, rcx
00AF18AE  89 42 38                        mov dword ptr [rdx + 0x38], eax
00AF18B1  48 C1 E8 20                     shr rax, 0x20
00AF18B5  89 42 3C                        mov dword ptr [rdx + 0x3c], eax
00AF18B8  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF18BC  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00AF18C1  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00AF18C5  E8 46 E1 76 FF                  call 0x14025fa10
00AF18CA  E8 E1 BF 76 FF                  call 0x14025d8b0
00AF18CF  8B DF                           mov ebx, edi
00AF18D1  E9 34 F2 FF FF                  jmp 0x140af0b0a
00AF18D6  8B D8                           mov ebx, eax
00AF18D8  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF18DD  E8 6E 7A 80 FF                  call 0x1402f9350
00AF18E2  8B C3                           mov eax, ebx
00AF18E4  E9 F0 05 00 00                  jmp 0x140af1ed9
00AF18E9  44 8A EF                        mov r13b, dil
00AF18EC  41 83 FC 10                     cmp r12d, 0x10
00AF18F0  0F 82 B2 F5 FF FF               jb 0x140af0ea8
00AF18F6  48 8D 84 24 EC 00 00 00         lea rax, [rsp + 0xec]
00AF18FE  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
00AF1903  48 8D 84 24 C8 00 00 00         lea rax, [rsp + 0xc8]
00AF190B  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00AF1910  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
00AF1914  45 33 C9                        xor r9d, r9d
00AF1917  45 8A C7                        mov r8b, r15b
00AF191A  41 8D 51 01                     lea edx, [r9 + 1]
00AF191E  49 8B CE                        mov rcx, r14
00AF1921  E8 4A 84 ED FF                  call 0x1409c9d70
00AF1926  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00AF192A  85 C0                           test eax, eax
00AF192C  0F 88 E2 ED FF FF               js 0x140af0714
00AF1932  4C 8B A4 24 C8 00 00 00         mov r12, qword ptr [rsp + 0xc8]
00AF193A  49 8B 1C 24                     mov rbx, qword ptr [r12]
00AF193E  48 8B 15 D3 3E 41 00            mov rdx, qword ptr [rip + 0x413ed3]
00AF1945  8B 4B 02                        mov ecx, dword ptr [rbx + 2]
00AF1948  2B 4A 02                        sub ecx, dword ptr [rdx + 2]
00AF194B  75 0A                           jne 0x140af1957
00AF194D  0F B7 4B 06                     movzx ecx, word ptr [rbx + 6]
00AF1951  0F B7 42 06                     movzx eax, word ptr [rdx + 6]
00AF1955  2B C8                           sub ecx, eax
00AF1957  8B C7                           mov eax, edi
00AF1959  85 C9                           test ecx, ecx
00AF195B  0F 94 C0                        sete al
00AF195E  85 C0                           test eax, eax
00AF1960  75 1D                           jne 0x140af197f
00AF1962  48 8B CE                        mov rcx, rsi
00AF1965  E8 E6 79 80 FF                  call 0x1402f9350
00AF196A  41 8A D7                        mov dl, r15b
00AF196D  49 8B CC                        mov rcx, r12
00AF1970  E8 CB 62 ED FF                  call 0x1409c7c40
00AF1975  B8 46 04 00 C0                  mov eax, 0xc0000446
00AF197A  E9 5A 05 00 00                  jmp 0x140af1ed9
00AF197F  48 8B CB                        mov rcx, rbx
00AF1982  E8 89 75 97 FF                  call 0x140468f10
00AF1987  0F B6 08                        movzx ecx, byte ptr [rax]
00AF198A  84 C9                           test cl, cl
00AF198C  75 05                           jne 0x140af1993
00AF198E  44 8B F7                        mov r14d, edi
00AF1991  EB 17                           jmp 0x140af19aa
00AF1993  8D 51 FF                        lea edx, [rcx - 1]
00AF1996  48 8B CB                        mov rcx, rbx
00AF1999  E8 72 53 96 FF                  call 0x140456d10
00AF199E  44 8B 30                        mov r14d, dword ptr [rax]
00AF19A1  41 81 FE 00 40 00 00            cmp r14d, 0x4000
00AF19A8  77 B8                           ja 0x140af1962
00AF19AA  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF19B3  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF19BA  90                              nop
00AF19BB  48 8B 44 24 50                  mov rax, qword ptr [rsp + 0x50]
00AF19C0  48 89 84 24 00 01 00 00         mov qword ptr [rsp + 0x100], rax
00AF19C8  B2 01                           mov dl, 1
00AF19CA  48 8B 48 30                     mov rcx, qword ptr [rax + 0x30]
00AF19CE  E8 4D 34 72 FF                  call 0x140214e20
00AF19D3  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF19D7  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00AF19DC  48 8B CB                        mov rcx, rbx
00AF19DF  E8 2C A5 92 FF                  call 0x14041bf10
00AF19E4  4C 8B E0                        mov r12, rax
00AF19E7  48 85 C0                        test rax, rax
00AF19EA  75 0A                           jne 0x140af19f6
00AF19EC  BB 46 04 00 C0                  mov ebx, 0xc0000446
00AF19F1  E9 95 04 00 00                  jmp 0x140af1e8b
00AF19F6  48 8B 00                        mov rax, qword ptr [rax]
00AF19F9  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
00AF19FE  48 8B C8                        mov rcx, rax
00AF1A01  E8 0A 75 97 FF                  call 0x140468f10
00AF1A06  0F B6 00                        movzx eax, byte ptr [rax]
00AF1A09  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
00AF1A10  8B F0                           mov esi, eax
00AF1A12  84 C0                           test al, al
00AF1A14  75 04                           jne 0x140af1a1a
00AF1A16  8B CF                           mov ecx, edi
00AF1A18  EB 16                           jmp 0x140af1a30
00AF1A1A  8D 56 FF                        lea edx, [rsi - 1]
00AF1A1D  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00AF1A22  E8 E9 52 96 FF                  call 0x140456d10
00AF1A27  8B 08                           mov ecx, dword ptr [rax]
00AF1A29  8B 84 24 A0 00 00 00            mov eax, dword ptr [rsp + 0xa0]
00AF1A30  44 3B F1                        cmp r14d, ecx
00AF1A33  76 34                           jbe 0x140af1a69
00AF1A35  41 8A D7                        mov dl, r15b
00AF1A38  48 8B 0D 39 80 4E 00            mov rcx, qword ptr [rip + 0x4e8039]
00AF1A3F  E8 DC 03 D8 FF                  call 0x140871e20
00AF1A44  84 C0                           test al, al
00AF1A46  75 0A                           jne 0x140af1a52
00AF1A48  BB 61 00 00 C0                  mov ebx, 0xc0000061
00AF1A4D  E9 39 04 00 00                  jmp 0x140af1e8b
00AF1A52  40 38 BB CC 00 00 00            cmp byte ptr [rbx + 0xcc], dil
00AF1A59  0F 84 49 01 00 00               je 0x140af1ba8
00AF1A5F  BB 2B 01 00 C0                  mov ebx, 0xc000012b
00AF1A64  E9 22 04 00 00                  jmp 0x140af1e8b
00AF1A69  84 C0                           test al, al
00AF1A6B  75 04                           jne 0x140af1a71
00AF1A6D  8B C7                           mov eax, edi
00AF1A6F  EB 0F                           jmp 0x140af1a80
00AF1A71  8D 56 FF                        lea edx, [rsi - 1]
00AF1A74  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
00AF1A79  E8 92 52 96 FF                  call 0x140456d10
00AF1A7E  8B 00                           mov eax, dword ptr [rax]
00AF1A80  44 3B F0                        cmp r14d, eax
00AF1A83  0F 83 1F 01 00 00               jae 0x140af1ba8
00AF1A89  E8 96 32 A0 FF                  call 0x1404f4d24
00AF1A8E  85 C0                           test eax, eax
00AF1A90  0F 84 0A 01 00 00               je 0x140af1ba0
00AF1A96  89 BC 24 80 00 00 00            mov dword ptr [rsp + 0x80], edi
00AF1A9D  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
00AF1AA5  E8 06 F2 F6 FF                  call 0x140a60cb0
00AF1AAA  8B 84 24 80 00 00 00            mov eax, dword ptr [rsp + 0x80]
00AF1AB1  24 18                           and al, 0x18
00AF1AB3  3C 10                           cmp al, 0x10
00AF1AB5  0F 85 E5 00 00 00               jne 0x140af1ba0
00AF1ABB  49 8B 34 24                     mov rsi, qword ptr [r12]
00AF1ABF  48 8B CE                        mov rcx, rsi
00AF1AC2  E8 49 74 97 FF                  call 0x140468f10
00AF1AC7  0F B6 08                        movzx ecx, byte ptr [rax]
00AF1ACA  84 C9                           test cl, cl
00AF1ACC  0F 84 CE 00 00 00               je 0x140af1ba0
00AF1AD2  8D 51 FF                        lea edx, [rcx - 1]
00AF1AD5  48 8B CE                        mov rcx, rsi
00AF1AD8  E8 33 52 96 FF                  call 0x140456d10
00AF1ADD  81 38 00 30 00 00               cmp dword ptr [rax], 0x3000
00AF1AE3  0F 82 B7 00 00 00               jb 0x140af1ba0
00AF1AE9  0F 57 C0                        xorps xmm0, xmm0
00AF1AEC  0F 11 84 24 30 01 00 00         movups xmmword ptr [rsp + 0x130], xmm0
00AF1AF4  0F 11 84 24 40 01 00 00         movups xmmword ptr [rsp + 0x140], xmm0
00AF1AFC  48 8D 8C 24 30 01 00 00         lea rcx, [rsp + 0x130]
00AF1B04  E8 17 9D D7 FF                  call 0x14086b820
00AF1B09  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AF1B12  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00AF1B19  90                              nop
00AF1B1A  48 8B 9C 24 40 01 00 00         mov rbx, qword ptr [rsp + 0x140]
00AF1B22  B2 01                           mov dl, 1
00AF1B24  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AF1B28  E8 93 00 72 FF                  call 0x140211bc0
00AF1B2D  48 8B CB                        mov rcx, rbx
00AF1B30  E8 DB A3 92 FF                  call 0x14041bf10
00AF1B35  48 8B 30                        mov rsi, qword ptr [rax]
00AF1B38  48 8B CE                        mov rcx, rsi
00AF1B3B  E8 D0 73 97 FF                  call 0x140468f10
00AF1B40  0F B6 08                        movzx ecx, byte ptr [rax]
00AF1B43  84 C9                           test cl, cl
00AF1B45  75 04                           jne 0x140af1b4b
00AF1B47  8B C7                           mov eax, edi
00AF1B49  EB 0D                           jmp 0x140af1b58
00AF1B4B  8D 51 FF                        lea edx, [rcx - 1]
00AF1B4E  48 8B CE                        mov rcx, rsi
00AF1B51  E8 BA 51 96 FF                  call 0x140456d10
00AF1B56  8B 00                           mov eax, dword ptr [rax]
00AF1B58  48 8B 4B 30                     mov rcx, qword ptr [rbx + 0x30]
00AF1B5C  3D 00 30 00 00                  cmp eax, 0x3000
00AF1B61  73 21                           jae 0x140af1b84
00AF1B63  E8 A8 DE 76 FF                  call 0x14025fa10
00AF1B68  E8 43 BD 76 FF                  call 0x14025d8b0
00AF1B6D  48 8D 8C 24 30 01 00 00         lea rcx, [rsp + 0x130]
00AF1B75  E8 96 9B D7 FF                  call 0x14086b710
00AF1B7A  BB 22 00 00 C0                  mov ebx, 0xc0000022
00AF1B7F  E9 07 03 00 00                  jmp 0x140af1e8b
00AF1B84  E8 87 DE 76 FF                  call 0x14025fa10
00AF1B89  E8 22 BD 76 FF                  call 0x14025d8b0
00AF1B8E  48 8D 8C 24 30 01 00 00         lea rcx, [rsp + 0x130]
00AF1B96  E8 75 9B D7 FF                  call 0x14086b710
00AF1B9B  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00AF1BA0  0F BA B3 C8 00 00 00 0C         btr dword ptr [rbx + 0xc8], 0xc
00AF1BA8  E8 DB DB 9F FF                  call 0x1404ef788
00AF1BAD  85 C0                           test eax, eax
00AF1BAF  0F 84 8A 00 00 00               je 0x140af1c3f
00AF1BB5  49 8B 34 24                     mov rsi, qword ptr [r12]
00AF1BB9  48 8B CE                        mov rcx, rsi
00AF1BBC  E8 4F 73 97 FF                  call 0x140468f10
00AF1BC1  0F B6 08                        movzx ecx, byte ptr [rax]
00AF1BC4  84 C9                           test cl, cl
00AF1BC6  75 04                           jne 0x140af1bcc
00AF1BC8  8B C7                           mov eax, edi
00AF1BCA  EB 0D                           jmp 0x140af1bd9
00AF1BCC  8D 51 FF                        lea edx, [rcx - 1]
00AF1BCF  48 8B CE                        mov rcx, rsi
00AF1BD2  E8 39 51 96 FF                  call 0x140456d10
00AF1BD7  8B 00                           mov eax, dword ptr [rax]
00AF1BD9  44 3B F0                        cmp r14d, eax
00AF1BDC  72 61                           jb 0x140af1c3f
00AF1BDE  0F 57 C0                        xorps xmm0, xmm0
00AF1BE1  0F 11 84 24 10 01 00 00         movups xmmword ptr [rsp + 0x110], xmm0
00AF1BE9  0F 11 84 24 20 01 00 00         movups xmmword ptr [rsp + 0x120], xmm0
00AF1BF1  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
00AF1BF9  E8 22 9C D7 FF                  call 0x14086b820
00AF1BFE  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
00AF1C06  E8 B5 48 DD FF                  call 0x1408c64c0
00AF1C0B  48 8B 84 24 20 01 00 00         mov rax, qword ptr [rsp + 0x120]
00AF1C13  44 8B A8 C8 00 00 00            mov r13d, dword ptr [rax + 0xc8]
00AF1C1A  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
00AF1C22  E8 F9 48 DD FF                  call 0x1408c6520
00AF1C27  48 8D 8C 24 10 01 00 00         lea rcx, [rsp + 0x110]
00AF1C2F  E8 DC 9A D7 FF                  call 0x14086b710
00AF1C34  41 C1 ED 0E                     shr r13d, 0xe
00AF1C38  41 F6 D5                        not r13b
00AF1C3B  41 80 E5 01                     and r13b, 1
00AF1C3F  49 8B 0C 24                     mov rcx, qword ptr [r12]
00AF1C43  0F B6 41 01                     movzx eax, byte ptr [rcx + 1]
00AF1C47  84 C0                           test al, al
00AF1C49  0F 84 37 02 00 00               je 0x140af1e86
00AF1C4F  8D 50 FF                        lea edx, [rax - 1]
00AF1C52  E8 B9 50 96 FF                  call 0x140456d10
00AF1C57  44 89 30                        mov dword ptr [rax], r14d
00AF1C5A  41 81 FE 00 30 00 00            cmp r14d, 0x3000
00AF1C61  73 12                           jae 0x140af1c75
00AF1C63  48 B8 7B F9 E9 DF EE FF FF FF   movabs rax, 0xffffffeedfe9f97b
00AF1C6D  48 21 43 48                     and qword ptr [rbx + 0x48], rax
00AF1C71  48 21 43 50                     and qword ptr [rbx + 0x50], rax
00AF1C75  BE 00 20 00 00                  mov esi, 0x2000
00AF1C7A  44 3B F6                        cmp r14d, esi
00AF1C7D  73 1F                           jae 0x140af1c9e
00AF1C7F  48 B8 00 00 80 02 02 00 00 00   movabs rax, 0x202800000
00AF1C89  48 21 43 48                     and qword ptr [rbx + 0x48], rax
00AF1C8D  48 21 43 50                     and qword ptr [rbx + 0x50], rax
00AF1C91  0F BA B3 C8 00 00 00 0D         btr dword ptr [rbx + 0xc8], 0xd
00AF1C99  E9 C4 01 00 00                  jmp 0x140af1e62
00AF1C9E  E8 E5 DA 9F FF                  call 0x1404ef788
00AF1CA3  8B 8B C8 00 00 00               mov ecx, dword ptr [rbx + 0xc8]
00AF1CA9  81 E1 00 40 00 00               and ecx, 0x4000
00AF1CAF  85 C0                           test eax, eax
00AF1CB1  0F 84 F5 00 00 00               je 0x140af1dac
00AF1CB7  85 C9                           test ecx, ecx
00AF1CB9  0F 84 B1 00 00 00               je 0x140af1d70
00AF1CBF  45 84 ED                        test r13b, r13b
00AF1CC2  0F 84 A8 00 00 00               je 0x140af1d70
00AF1CC8  48 8B 93 10 03 00 00            mov rdx, qword ptr [rbx + 0x310]
00AF1CCF  48 8B CB                        mov rcx, rbx
00AF1CD2  E8 B5 E4 90 FF                  call 0x14040018c
00AF1CD7  0F BA B3 C8 00 00 00 0E         btr dword ptr [rbx + 0xc8], 0xe
00AF1CDF  48 8B 8B 10 03 00 00            mov rcx, qword ptr [rbx + 0x310]
00AF1CE6  48 85 C9                        test rcx, rcx
00AF1CE9  74 0E                           je 0x140af1cf9
00AF1CEB  33 D2                           xor edx, edx
00AF1CED  E8 7E 0B 09 00                  call 0x140b82870
00AF1CF2  48 89 BB 10 03 00 00            mov qword ptr [rbx + 0x310], rdi
00AF1CF9  48 8B 8B 18 03 00 00            mov rcx, qword ptr [rbx + 0x318]
00AF1D00  48 85 C9                        test rcx, rcx
00AF1D03  74 28                           je 0x140af1d2d
00AF1D05  33 D2                           xor edx, edx
00AF1D07  E8 64 0B 09 00                  call 0x140b82870
00AF1D0C  48 89 BB 18 03 00 00            mov qword ptr [rbx + 0x318], rdi
00AF1D13  89 BB 20 03 00 00               mov dword ptr [rbx + 0x320], edi
00AF1D19  48 8D 8B 28 03 00 00            lea rcx, [rbx + 0x328]
00AF1D20  33 D2                           xor edx, edx
00AF1D22  41 B8 10 01 00 00               mov r8d, 0x110
00AF1D28  E8 13 4F BD FF                  call 0x1406c6c40
00AF1D2D  48 8B 93 38 04 00 00            mov rdx, qword ptr [rbx + 0x438]
00AF1D34  48 85 D2                        test rdx, rdx
00AF1D37  74 0F                           je 0x140af1d48
00AF1D39  8B 4B 78                        mov ecx, dword ptr [rbx + 0x78]
00AF1D3C  E8 7B 40 F6 FF                  call 0x140a55dbc
00AF1D41  48 89 BB 38 04 00 00            mov qword ptr [rbx + 0x438], rdi
00AF1D48  4C 8B 83 40 04 00 00            mov r8, qword ptr [rbx + 0x440]
00AF1D4F  4D 85 C0                        test r8, r8
00AF1D52  74 1C                           je 0x140af1d70
00AF1D54  48 8B 8B D8 00 00 00            mov rcx, qword ptr [rbx + 0xd8]
00AF1D5B  48 83 C1 60                     add rcx, 0x60
00AF1D5F  45 33 C9                        xor r9d, r9d
00AF1D62  33 D2                           xor edx, edx
00AF1D64  E8 BB 76 F2 FF                  call 0x140a19424
00AF1D69  48 89 BB 40 04 00 00            mov qword ptr [rbx + 0x440], rdi
00AF1D70  49 8B 34 24                     mov rsi, qword ptr [r12]
00AF1D74  48 8B CE                        mov rcx, rsi
00AF1D77  E8 94 71 97 FF                  call 0x140468f10
00AF1D7C  0F B6 08                        movzx ecx, byte ptr [rax]
00AF1D7F  84 C9                           test cl, cl
00AF1D81  0F 84 DB 00 00 00               je 0x140af1e62
00AF1D87  8D 51 FF                        lea edx, [rcx - 1]
00AF1D8A  48 8B CE                        mov rcx, rsi
00AF1D8D  E8 7E 4F 96 FF                  call 0x140456d10
00AF1D92  8B 08                           mov ecx, dword ptr [rax]
00AF1D94  B8 00 20 00 00                  mov eax, 0x2000
00AF1D99  3B C8                           cmp ecx, eax
00AF1D9B  0F 82 C1 00 00 00               jb 0x140af1e62
00AF1DA1  09 83 C8 00 00 00               or dword ptr [rbx + 0xc8], eax
00AF1DA7  E9 B6 00 00 00                  jmp 0x140af1e62
00AF1DAC  85 C9                           test ecx, ecx
00AF1DAE  0F 84 A8 00 00 00               je 0x140af1e5c
00AF1DB4  48 8B 93 10 03 00 00            mov rdx, qword ptr [rbx + 0x310]
00AF1DBB  48 8B CB                        mov rcx, rbx
00AF1DBE  E8 C9 E3 90 FF                  call 0x14040018c
00AF1DC3  0F BA B3 C8 00 00 00 0E         btr dword ptr [rbx + 0xc8], 0xe
00AF1DCB  48 8B 8B 10 03 00 00            mov rcx, qword ptr [rbx + 0x310]
00AF1DD2  48 85 C9                        test rcx, rcx
00AF1DD5  74 0E                           je 0x140af1de5
00AF1DD7  33 D2                           xor edx, edx
00AF1DD9  E8 92 0A 09 00                  call 0x140b82870
00AF1DDE  48 89 BB 10 03 00 00            mov qword ptr [rbx + 0x310], rdi
00AF1DE5  48 8B 8B 18 03 00 00            mov rcx, qword ptr [rbx + 0x318]
00AF1DEC  48 85 C9                        test rcx, rcx
00AF1DEF  74 28                           je 0x140af1e19
00AF1DF1  33 D2                           xor edx, edx
00AF1DF3  E8 78 0A 09 00                  call 0x140b82870
00AF1DF8  48 89 BB 18 03 00 00            mov qword ptr [rbx + 0x318], rdi
00AF1DFF  89 BB 20 03 00 00               mov dword ptr [rbx + 0x320], edi
00AF1E05  48 8D 8B 28 03 00 00            lea rcx, [rbx + 0x328]
00AF1E0C  33 D2                           xor edx, edx
00AF1E0E  41 B8 10 01 00 00               mov r8d, 0x110
00AF1E14  E8 27 4E BD FF                  call 0x1406c6c40
00AF1E19  48 8B 93 38 04 00 00            mov rdx, qword ptr [rbx + 0x438]
00AF1E20  48 85 D2                        test rdx, rdx
00AF1E23  74 0F                           je 0x140af1e34
00AF1E25  8B 4B 78                        mov ecx, dword ptr [rbx + 0x78]
00AF1E28  E8 8F 3F F6 FF                  call 0x140a55dbc
00AF1E2D  48 89 BB 38 04 00 00            mov qword ptr [rbx + 0x438], rdi
00AF1E34  4C 8B 83 40 04 00 00            mov r8, qword ptr [rbx + 0x440]
00AF1E3B  4D 85 C0                        test r8, r8
00AF1E3E  74 1C                           je 0x140af1e5c
00AF1E40  48 8B 8B D8 00 00 00            mov rcx, qword ptr [rbx + 0xd8]
00AF1E47  48 83 C1 60                     add rcx, 0x60
00AF1E4B  45 33 C9                        xor r9d, r9d
00AF1E4E  33 D2                           xor edx, edx
00AF1E50  E8 CF 75 F2 FF                  call 0x140a19424
00AF1E55  48 89 BB 40 04 00 00            mov qword ptr [rbx + 0x440], rdi
00AF1E5C  09 B3 C8 00 00 00               or dword ptr [rbx + 0xc8], esi
00AF1E62  48 8B 0D 9F 0E 52 FF            mov rcx, qword ptr [rip - 0xadf161]
00AF1E69  48 8B C1                        mov rax, rcx
00AF1E6C  F0 48 0F C1 05 7B CD 31 00      lock xadd qword ptr [rip + 0x31cd7b], rax
00AF1E75  48 03 C1                        add rax, rcx
00AF1E78  89 43 38                        mov dword ptr [rbx + 0x38], eax
00AF1E7B  48 C1 E8 20                     shr rax, 0x20
00AF1E7F  89 43 3C                        mov dword ptr [rbx + 0x3c], eax
00AF1E82  8B DF                           mov ebx, edi
00AF1E84  EB 05                           jmp 0x140af1e8b
00AF1E86  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00AF1E8B  F0 09 3C 24                     lock or dword ptr [rsp], edi
00AF1E8F  48 8B 8C 24 00 01 00 00         mov rcx, qword ptr [rsp + 0x100]
00AF1E97  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
00AF1E9B  E8 70 DB 76 FF                  call 0x14025fa10
00AF1EA0  E8 0B BA 76 FF                  call 0x14025d8b0
00AF1EA5  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF1EAA  E8 A1 74 80 FF                  call 0x1402f9350
00AF1EAF  41 8A D7                        mov dl, r15b
00AF1EB2  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
00AF1EBA  E8 81 5D ED FF                  call 0x1409c7c40
00AF1EBF  E9 4E EC FF FF                  jmp 0x140af0b12
00AF1EC4  8B D8                           mov ebx, eax
00AF1EC6  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00AF1ECB  E8 80 74 80 FF                  call 0x1402f9350
00AF1ED0  8B C3                           mov eax, ebx
00AF1ED2  EB 05                           jmp 0x140af1ed9
00AF1ED4  B8 03 00 00 C0                  mov eax, 0xc0000003
00AF1ED9  4C 8D 9C 24 60 01 00 00         lea r11, [rsp + 0x160]
00AF1EE1  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00AF1EE5  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00AF1EE9  49 8B E3                        mov rsp, r11
00AF1EEC  41 5F                           pop r15
00AF1EEE  41 5E                           pop r14
00AF1EF0  41 5D                           pop r13
00AF1EF2  41 5C                           pop r12
00AF1EF4  5F                              pop rdi
00AF1EF5  C3                              ret
00AF1EF6  CC                              int3
00AF1EF7  E8 D4 80 DA FF                  call 0x140899fd0
00AF1EFC  90                              nop
00AF1EFD  E8 CE 80 DA FF                  call 0x140899fd0
00AF1F02  90                              nop
00AF1F03  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtSetInformationToken(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned int v_stack_m108;
    unsigned int v_stack_m10C;
    unsigned int v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned __int64 v_stack_m120;
    unsigned __int8 v_stack_m124;
    unsigned int v_stack_m128;
    unsigned __int8 v_stack_m12B;
    unsigned __int8 v_stack_m12C;
    unsigned int v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned int v_stack_m188;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m94;
    unsigned int v_stack_m98;
    unsigned __int64 v_stack_m9C;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA4;
    unsigned int v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned __int16 v_stack_mB6;
    unsigned __int16 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned int v_stack_mCC;
    unsigned int v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned int v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (352);
    v_rdi = 0;
    v_stack_m12C = 0;
    v_stack_m128 = 0;
    *(unsigned __int64 *)(v_rsp - 200) = 0;
    *(unsigned __int64 *)(v_rsp - 192) = 0;
    v_stack_m12B = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AF05CC;
    if (a4 == 0) goto loc_00AF05BB;
    if ((((unsigned __int8)(a3)) & (3)) != 0) goto loc_00AF1EF7;
    if ((a3 + (unsigned int)(a4) * 1) > v_r13) goto loc_00AF05B5;
    if ((a3 + (unsigned int)(a4) * 1) >= a3) goto loc_00AF05C5;
loc_00AF05B5:
    goto loc_00AF05C5;
loc_00AF05BB:
loc_00AF05C5:
    goto loc_00AF05D6;
loc_00AF05CC:
loc_00AF05D6:
    if (((unsigned int)((int)(a2))) > 58) goto loc_00AF05EB;
    if (((unsigned int)((int)(a2))) < 58) goto loc_00AF0625;
loc_00AF05EB:
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(a3 + (unsigned int)(a4) * 1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00AF1ED4;
    v_stack_m110 = 0;
    result = RtlQueryElevationFlags(v_stack_m110, a2, a3, a4);
    if (sign_flag) goto loc_00AF1ED4;
    result = (unsigned __int8)(((unsigned int)(v_stack_m110)) & (24));
    if (((unsigned __int8)(result)) != 16) goto loc_00AF1ED4;
    if (((unsigned int)((int)(a2))) != -2) goto loc_00AF1ED4;
loc_00AF0625:
    result = Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline(v_stack_m110, a2, a3, a4);
    if ((unsigned int)(result) != 0) goto loc_00AF0637;
    if (((unsigned int)((int)(a2))) == 52) goto loc_00AF1ED4;
loc_00AF0637:
    if (((unsigned int)((int)(a2))) != 12) goto loc_00AF0648;
    goto loc_00AF0657;
loc_00AF0648:
    if (((unsigned int)((int)(a2))) == 19) goto loc_00AF0652;
    if (((unsigned int)((int)(a2))) == -2) {
        a2 = 136;
    }
    v_stack_m138 = 0;
    v_stack_m160 = 0;
    v_stack_m168 = v_stack_m138;
    result = ObReferenceObjectByHandle(a1, a2, *(unsigned __int64 *)(v_rip + 5142978), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_stack_mE8 = v_stack_m138;
    if (sign_flag) goto loc_00AF1ED9;
    if (((unsigned int)((int)(a2))) > 24) goto loc_00AF1186;
    if (((unsigned int)((int)(a2))) == 24) goto loc_00AF1152;
    if (((unsigned int)((int)(a2))) > 14) goto loc_00AF0DBA;
    if (((unsigned int)((int)(a2))) == 14) goto loc_00AF0CFC;
    if (((unsigned int)((int)(a2))) == -2) goto loc_00AF0CC4;
    if (((unsigned int)((int)(a2))) == 4) goto loc_00AF0AC3;
    if (((unsigned int)((int)(a2))) == 5) goto loc_00AF0940;
    if (((unsigned int)((int)(a2))) == 6) goto loc_00AF072E;
    if (((unsigned int)((int)(a2))) != 12) goto loc_00AF11D3;
    if (((unsigned int)((unsigned int)(a4))) != 4) goto loc_00AF0AC9;
    v_stack_m98 = (unsigned int)((unsigned int)(*(unsigned int *)(a3)));
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5149569), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), *(unsigned __int64 *)(v_rip + 5142978), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if ((unsigned __int8)(result) != 0) goto loc_00AF070A;
loc_00AF0700:
    goto loc_00AF0B0A;
loc_00AF070A:
    result = SeSetSessionIdToken(v_stack_m138, (unsigned int)((unsigned int)((unsigned int)(0xC0000061ULL))), *(unsigned __int64 *)(v_rip + 5142978), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
loc_00AF0714:
    goto loc_00AF0B0A;
loc_00AF072E:
    if (((unsigned int)((unsigned int)(a4))) < 8) goto loc_00AF0AC9;
    v_stack_m120 = *(unsigned __int64 *)(a3);
    if (*(unsigned __int64 *)(a3) == 0) goto loc_00AF0771;
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m120;
    v_stack_m168 = 1;
    result = SeCaptureAcl(*(unsigned __int64 *)(a3), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), *(unsigned __int64 *)(v_rip + 5142978), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_stack_m130 = (unsigned int)(result);
    goto loc_00AF077B;
loc_00AF0771:
    v_stack_m128 = 0;
    v_stack_m130 = 0;
loc_00AF077B:
    if (sign_flag) goto loc_00AF0B0A;
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_stack_m138 + 48), 1, *(unsigned __int64 *)(v_rip + 5142978), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    result = (unsigned int)(((unsigned int)(v_stack_m128)) + (8));
    v_stack_m128 = (unsigned int)(result + *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m138 + 168) + 1) * 4);
    if (((unsigned int)(result + *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m138 + 168) + 1) * 4)) <= (*(unsigned int *)(v_stack_m138 + 136))) goto loc_00AF0806;
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m138 + 48), result + *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m138 + 168) + 1) * 4, *(unsigned __int64 *)(v_rip + 5142978), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m138 + 48), result + *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m138 + 168) + 1) * 4, *(unsigned __int64 *)(v_rip + 5142978), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    result = ObfDereferenceObject(v_stack_m138, result + *(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m138 + 168) + 1) * 4, *(unsigned __int64 *)(v_rip + 5142978), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (v_stack_m120 != 0) {
        a2 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        result = SeReleaseAcl(v_stack_m120, a2, *(unsigned __int64 *)(v_rip + 5142978), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    }
    goto loc_00AF1ED9;
loc_00AF0806:
    result = SepExpandDynamic(v_stack_m138, a2, *(unsigned __int64 *)(v_rip + 5142978), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_stack_m130 = (unsigned int)(result);
    if (!sign_flag) goto loc_00AF084D;
loc_00AF0816:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m138 + 48), a2, *(unsigned __int64 *)(v_rip + 5142978), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m138 + 48), a2, *(unsigned __int64 *)(v_rip + 5142978), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    result = ObfDereferenceObject(v_stack_m138, a2, *(unsigned __int64 *)(v_rip + 5142978), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (v_stack_m120 != 0) {
        a2 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        result = SeReleaseAcl(v_stack_m120, a2, *(unsigned __int64 *)(v_rip + 5142978), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    }
    goto loc_00AF1ED9;
loc_00AF084D:
    if (*(unsigned __int64 *)(v_stack_m138 + 184) == 0) goto loc_00AF088A;
    v_stack_m150 = v_stack_m94;
    v_stack_m158 = v_stack_mC8;
    v_stack_m168 = 1;
    a2 = 0;
    result = SeCaptureAcl(*(unsigned __int64 *)(v_stack_m138 + 184), a2, *(unsigned __int64 *)(v_rip + 5142978), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    v_stack_m130 = (unsigned int)(result);
    if (sign_flag) goto loc_00AF0816;
loc_00AF088A:
    result = SepFreeDefaultDacl(v_stack_m138, a2, *(unsigned __int64 *)(v_rip + 5142978), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (v_stack_m120 != 0) {
        a2 = v_stack_m120;
        a1 = v_stack_m138;
        result = SepAppendDefaultDacl(a1, a2, *(unsigned __int64 *)(v_rip + 5142978), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    }
    v_stack_m168 = v_stack_m120;
    result = SeTokenDefaultDaclChangedAuditAlarm(a1, v_stack_m138, v_stack_p8, v_stack_mC8);
    result = (*(unsigned __int64 *)(v_rip - 11393987)) + (*(unsigned __int64 *)(v_rip - 11393987));
    *(unsigned int *)(v_stack_m138 + 56) = (unsigned int)(result);
    result = (result) >> (32);
    *(unsigned int *)(v_stack_m138 + 60) = (unsigned int)(result);
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m138 + 48), v_stack_m138, v_stack_p8, v_stack_mC8);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m138 + 48), v_stack_m138, v_stack_p8, v_stack_mC8);
    result = ObfDereferenceObject(v_stack_m138, v_stack_m138, v_stack_p8, v_stack_mC8);
    if (v_stack_m120 != 0) {
        a2 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        result = SeReleaseAcl(v_stack_m120, a2, v_stack_p8, v_stack_mC8);
    }
    if (v_stack_mC8 != 0) {
        a2 = 0;
        result = SeReleaseAcl(v_stack_mC8, a2, v_stack_p8, v_stack_mC8);
    }
    result = 0;
    goto loc_00AF1ED9;
loc_00AF0940:
    if (((unsigned int)((unsigned int)(a4))) < 8) goto loc_00AF0AC9;
    v_stack_m100 = *(unsigned __int64 *)(v_stack_m120);
    v_stack_m158 = v_stack_m100;
    v_stack_m160 = 1;
    result = SeCaptureSid(*(unsigned __int64 *)(v_stack_m120), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_p8, v_stack_mC8);
    v_stack_m130 = (unsigned int)(result);
    if (sign_flag) goto loc_00AF0B0D;
    result = SepIdAssignableAsGroup(v_stack_m138, v_stack_m100, v_stack_p8, v_stack_mC8);
    if ((unsigned __int8)(result) != 0) goto loc_00AF099B;
    goto loc_00AF0A8E;
loc_00AF099B:
    v_stack_m128 = (unsigned int)(*(unsigned __int8 *)(v_stack_m100 + 1) * 4 + 8);
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_stack_m138 + 48), 1, v_stack_p8, v_stack_mC8);
    result = *(unsigned __int64 *)(v_stack_m138 + 184);
    v_rsi = *(unsigned __int8 *)(v_stack_m100 + 1) * 4 + 8;
    if (*(unsigned __int64 *)(v_stack_m138 + 184) != 0) {
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_m138 + 184) + 2);
        v_rsi = (unsigned int)((*(unsigned __int8 *)(v_stack_m100 + 1) * 4 + 8) + ((unsigned int)(result)));
        v_stack_m128 = (unsigned int)(v_rsi);
    }
    if (((unsigned int)(v_rsi)) <= (*(unsigned int *)(v_stack_m138 + 136))) goto loc_00AF0A13;
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m138 + 48), 1, v_stack_p8, v_stack_mC8);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m138 + 48), 1, v_stack_p8, v_stack_mC8);
    goto loc_00AF0A89;
loc_00AF0A13:
    result = SepExpandDynamic(v_stack_m138, (unsigned int)(v_stack_m128), v_stack_p8, v_stack_mC8);
    v_stack_m130 = (unsigned int)(result);
    if (!sign_flag) goto loc_00AF0A3F;
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m138 + 48), (unsigned int)(v_stack_m128), v_stack_p8, v_stack_mC8);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m138 + 48), (unsigned int)(v_stack_m128), v_stack_p8, v_stack_mC8);
    goto loc_00AF0A89;
loc_00AF0A3F:
    result = SepFreePrimaryGroup(v_stack_m138, (unsigned int)(v_stack_m128), v_stack_p8, v_stack_mC8);
    result = SepAppendPrimaryGroup(v_stack_m138, v_stack_m100, v_stack_p8, v_stack_mC8);
    result = (*(unsigned __int64 *)(v_rip - 11394390)) + (*(unsigned __int64 *)(v_rip - 11394390));
    *(unsigned int *)(v_stack_m138 + 56) = (unsigned int)(result);
    result = (result) >> (32);
    *(unsigned int *)(v_stack_m138 + 60) = (unsigned int)(result);
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m138 + 48), v_stack_m100, v_stack_p8, v_stack_mC8);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m138 + 48), v_stack_m100, v_stack_p8, v_stack_mC8);
loc_00AF0A89:
loc_00AF0A8E:
    result = ObfDereferenceObject(v_stack_m138, v_stack_m100, v_stack_p8, v_stack_mC8);
    result = SeReleaseSid(v_stack_m100, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), 1, v_stack_mC8);
    goto loc_00AF1ED9;
loc_00AF0AC3:
    if (((unsigned int)((unsigned int)(a4))) >= 8) goto loc_00AF0ADB;
loc_00AF0AC9:
    result = ObfDereferenceObject(v_stack_m138, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), 1, v_stack_mC8);
    goto loc_00AF1ED9;
loc_00AF0ADB:
    v_stack_mF8 = *(unsigned __int64 *)(v_stack_m138);
    v_stack_m158 = v_stack_mF8;
    v_stack_m160 = 1;
    result = SeCaptureSid(*(unsigned __int64 *)(v_stack_m138), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), 1, v_stack_mC8);
    v_stack_m130 = (unsigned int)(result);
    if (!sign_flag) goto loc_00AF0B19;
loc_00AF0B0A:
loc_00AF0B0D:
    result = ObfDereferenceObject(v_stack_m138, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), 1, v_stack_mC8);
loc_00AF0B12:
    goto loc_00AF1ED9;
loc_00AF0B19:
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_stack_m138 + 48), 1, 1, v_stack_mC8);
loc_00AF0B40:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m130))))) >= (*(unsigned int *)(v_stack_m138 + 124))) goto loc_00AF0C7A;
    result = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m130)))))) + ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m130))))));
    result = RtlEqualSid(v_stack_mF8, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m138 + 152) + result * 8), 1, v_stack_mC8);
    v_stack_m124 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) == 0) goto loc_00AF0C02;
    result = SepIdAssignableAsOwner(v_stack_m138, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m130))))), 1, v_stack_mC8);
    if ((unsigned __int8)(result) == 0) goto loc_00AF0B92;
    *(unsigned int *)(v_stack_m138 + 144) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m130))));
    v_stack_m12C = 1;
    v_stack_m130 = (unsigned int)((unsigned int)(v_stack_m130));
    goto loc_00AF0B9E;
loc_00AF0B92:
    v_stack_m130 = 0xC000005AULL;
loc_00AF0B9E:
    result = v_stack_m12C;
    if ((unsigned __int8)(v_stack_m12C) != 0) {
        v_stack_m118 = (unsigned int)(v_stack_m130);
        a2 = *(unsigned __int64 *)(v_rip - 11394726);
        result = a2;
        result = (result) + (a2);
        v_stack_m118 = result;
        *(unsigned int *)(v_stack_m138 + 56) = (unsigned int)(result);
        result = (result) >> (32);
        *(unsigned int *)(v_stack_m138 + 60) = (unsigned int)(result);
    }
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m138 + 48), a2, 1, v_stack_mC8);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m138 + 48), a2, 1, v_stack_mC8);
    result = ObfDereferenceObject(v_stack_m138, a2, 1, v_stack_mC8);
    result = SeReleaseSid(v_stack_mF8, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), 1, v_stack_mC8);
    goto loc_00AF1ED9;
loc_00AF0C02:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m130)))) + 1);
    goto loc_00AF0B40;
loc_00AF0C7A:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m138 + 48), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), 1, v_stack_mC8);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m138 + 48), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), 1, v_stack_mC8);
    result = ObfDereferenceObject(v_stack_m138, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), 1, v_stack_mC8);
    result = SeReleaseSid(v_stack_mF8, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), 1, v_stack_mC8);
    goto loc_00AF1ED9;
loc_00AF0CC4:
    if (((unsigned int)((unsigned int)(a4))) != 8) goto loc_00AF0EA8;
    v_stack_m30 = *(unsigned __int64 *)(v_stack_m138);
    result = SepOneWayLinkLogonSessions(v_stack_m138, *(unsigned __int64 *)(v_stack_m138), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
    goto loc_00AF0714;
loc_00AF0CFC:
    if (((unsigned int)((unsigned int)(a4))) != 4) goto loc_00AF0EA8;
    v_stack_m80 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m138)));
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5147998), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
    if ((unsigned __int8)(result) == 0) goto loc_00AF0700;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m138))) == 0) goto loc_00AF0D35;
loc_00AF0D2B:
    goto loc_00AF0B0A;
loc_00AF0D35:
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_stack_m138 + 48), 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m138 + 200)))) & (32)) != 0) goto loc_00AF0D8E;
    result = (unsigned int)(*(unsigned int *)(v_stack_m138 + 200));
    if ((*(unsigned int *)(v_rip + 5141152)) != 0) {
        a1 = v_stack_m138;
        result = SepRemoveTokenLogonSession(a1, 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
    }
    result = SepStopReferencingLogonSession(v_stack_m138, 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
    v_stack_m130 = (unsigned int)(result);
    if (sign_flag) goto loc_00AF0714;
loc_00AF0D8E:
loc_00AF0D96:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m138 + 48), 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m138 + 48), 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
    v_rbx = 0;
    goto loc_00AF104A;
loc_00AF0DBA:
    v_rbx = (unsigned int)((v_rbx) - (16));
    if (condition_is_equal) goto loc_00AF0F8F;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00AF0EE0;
    v_rbx = (unsigned int)((v_rbx) - (2));
    if (condition_is_equal) goto loc_00AF0EA2;
    if (((unsigned int)(v_rbx)) != 4) goto loc_00AF11D3;
    if (((unsigned int)((unsigned int)(a4))) != ((unsigned int)(v_rbx))) goto loc_00AF0EA8;
    v_stack_mD8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m138)));
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5148037), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
    if ((unsigned __int8)(result) == 0) goto loc_00AF0700;
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_stack_m138 + 48), 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
    if (v_stack_mD8 == ((unsigned int)((unsigned int)(v_stack_m130)))) goto loc_00AF0E47;
    goto loc_00AF0E4B;
loc_00AF0E47:
loc_00AF0E4B:
    *(unsigned int *)(v_stack_m138 + 200) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m138 + 200)));
loc_00AF0E51:
    result = (*(unsigned __int64 *)(v_rip - 11395408)) + (*(unsigned __int64 *)(v_rip - 11395408));
    *(unsigned int *)(v_stack_m138 + 56) = (unsigned int)(result);
    result = (result) >> (32);
    *(unsigned int *)(v_stack_m138 + 60) = (unsigned int)(result);
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m138 + 48), v_stack_m138, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m138 + 48), v_stack_m138, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
loc_00AF0E88:
    v_rbx = 0;
    goto loc_00AF0B0A;
loc_00AF0EA2:
    if (((unsigned int)((unsigned int)(a4))) == 8) goto loc_00AF0EB2;
loc_00AF0EA8:
    goto loc_00AF0B0A;
loc_00AF0EB2:
    v_stack_m38 = *(unsigned __int64 *)(v_stack_m138);
    result = SepLinkLogonSessions(v_stack_m138, *(unsigned __int64 *)(v_stack_m138), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
    goto loc_00AF0714;
loc_00AF0EE0:
    if (((unsigned int)((unsigned int)(a4))) != 8) goto loc_00AF0EA8;
    v_stack_m90 = *(unsigned __int64 *)(v_stack_m138);
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5147517), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
    if ((unsigned __int8)(result) == 0) goto loc_00AF0700;
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_stack_m138 + 48), 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m138 + 228))) | (*(unsigned int *)(v_stack_m138 + 224)));
    if (!(condition_is_not_equal)) {
        result = v_stack_m90;
        *(unsigned __int64 *)(v_stack_m138 + 224) = result;
    }
    result = (*(unsigned __int64 *)(v_rip - 11395662)) + (*(unsigned __int64 *)(v_rip - 11395662));
    *(unsigned int *)(v_stack_m138 + 56) = (unsigned int)(result);
    result = (result) >> (32);
    *(unsigned int *)(v_stack_m138 + 60) = (unsigned int)(result);
    goto loc_00AF103E;
loc_00AF0F8F:
    v_stack_mE0 = (unsigned int)(v_stack_m130);
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5147351), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
    if ((unsigned __int8)(result) == 0) goto loc_00AF0700;
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m138 + 48), 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m138 + 48), 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m138 + 48), 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_stack_m138 + 119)) != 0) goto loc_00AF0D2B;
    if (v_stack_m138 != 0) goto loc_00AF1054;
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_stack_m138 + 48), 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
    *(unsigned __int8 *)(v_stack_m138 + 119) = 1;
    result = (*(unsigned __int64 *)(v_rip - 11395861)) + (*(unsigned __int64 *)(v_rip - 11395861));
    *(unsigned int *)(v_stack_m138 + 56) = (unsigned int)(result);
    result = (result) >> (32);
    *(unsigned int *)(v_stack_m138 + 60) = (unsigned int)(result);
loc_00AF103E:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m138 + 48), v_stack_m138, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m138 + 48), v_stack_m138, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
loc_00AF104A:
    goto loc_00AF0B0A;
loc_00AF1054:
    v_stack_m158 = v_stack_mE0;
    result = SepCaptureAuditPolicy(v_stack_m138, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
    v_stack_m130 = (unsigned int)(result);
    if (sign_flag) goto loc_00AF0714;
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_stack_m138 + 48), 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mC8);
    *(unsigned __int8 *)(v_stack_m138 + 119) = 2;
    *(unsigned __int64 *)(v_stack_m138 + 88) = v_xmm0;
    *(unsigned __int64 *)(v_stack_m138 + 88 + 16) = v_xmm1;
    *(unsigned int *)(v_stack_m138 + 88 + 24) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mE0 + 24)));
    *(unsigned __int16 *)(v_stack_m138 + 88 + 28) = (unsigned __int16)(*(unsigned __int16 *)(v_stack_mE0 + 28));
    *(unsigned __int8 *)(v_stack_m138 + 88 + 30) = (unsigned __int8)(*(unsigned __int8 *)(v_stack_mE0 + 30));
    result = (*(unsigned __int64 *)(v_rip - 11396048)) + (*(unsigned __int64 *)(v_rip - 11396048));
    *(unsigned int *)(v_stack_m138 + 56) = (unsigned int)(result);
    result = (result) >> (32);
    *(unsigned int *)(v_stack_m138 + 60) = (unsigned int)(result);
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m138 + 48), *(unsigned __int64 *)(v_rip - 11396048), v_stack_m138, v_stack_mC8);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m138 + 48), *(unsigned __int64 *)(v_rip - 11396048), v_stack_m138, v_stack_mC8);
    result = SepModifyTokenPolicyCounter(v_stack_m138 + 88, 1, v_stack_m138, v_stack_mC8);
    result = ObfDereferenceObject(v_stack_m138, 1, v_stack_m138, v_stack_mC8);
    result = SepReleaseAuditPolicy(v_stack_mE0, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_m138, v_stack_mC8);
    goto loc_00AF0926;
loc_00AF1152:
    if (((unsigned int)((unsigned int)(a4))) != 4) goto loc_00AF0EA8;
    v_stack_mA8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m138)));
    result = SeSetVirtualizationToken(v_stack_m138, (unsigned int)(*(unsigned int *)(v_stack_m138)), v_stack_m138, v_stack_mC8);
    goto loc_00AF0E88;
loc_00AF1186:
    v_rbx = (unsigned int)((v_stack_m138 + 88) - (25));
    if (condition_is_equal) goto loc_00AF18E9;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00AF1820;
    v_rbx = (unsigned int)((v_rbx) - (1));
    if (condition_is_equal) goto loc_00AF17BA;
    v_rbx = (unsigned int)((v_rbx) - (2));
    if (condition_is_equal) goto loc_00AF1651;
    v_rbx = (unsigned int)((v_rbx) - (10));
    if (condition_is_equal) goto loc_00AF1522;
    v_rbx = (unsigned int)((v_rbx) - (3));
    if (condition_is_equal) goto loc_00AF14D5;
    v_rbx = (unsigned int)((v_rbx) - (3));
    if (condition_is_equal) goto loc_00AF1411;
    v_rbx = (unsigned int)((v_rbx) - (7));
    if (condition_is_equal) goto loc_00AF138C;
    if (((unsigned int)(v_rbx)) == 6) goto loc_00AF11DD;
loc_00AF11D3:
    goto loc_00AF1ED9;
loc_00AF11DD:
    result = Feature_AgentId2__private_IsEnabledDeviceUsageNoInline(v_stack_m138, (unsigned int)(*(unsigned int *)(v_stack_m138)), v_stack_m138, v_stack_mC8);
    if ((unsigned int)(result) == 0) goto loc_00AF1382;
    v_stack_mB4 = (unsigned int)((unsigned int)(v_stack_m130));
    if (v_stack_m138 == 0) goto loc_00AF0D2B;
    if ((unsigned int)((unsigned int)(a4)) == 0) goto loc_00AF0D2B;
    if ((((unsigned __int8)((unsigned int)(a4))) & (1)) != 0) goto loc_00AF0D2B;
    if (((unsigned int)((unsigned int)(a4))) > 0xFFFCULL) goto loc_00AF0D2B;
    a1 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1530))) & (7));
    if (((unsigned __int8)(a1)) < 1) goto loc_00AF1240;
    result = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1530)) & (240));
    if (((unsigned __int8)(result)) == 48) goto loc_00AF1257;
loc_00AF1240:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5146670), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_m138, v_stack_mC8);
    if ((unsigned __int8)(result) == 0) goto loc_00AF1378;
loc_00AF1257:
    result = ExAllocatePool2(256, (unsigned int)(a4), (unsigned int)(0x20206553ULL), v_stack_mC8);
    v_stack_m118 = result;
    if (result != 0) goto loc_00AF1281;
    goto loc_00AF104A;
loc_00AF1281:
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AF12A2;
    if ((((unsigned __int8)(v_stack_m138)) & (1)) != 0) goto loc_00AF1EFD;
    if (((unsigned int)(a4) + v_stack_m138 * 1) > v_r13) goto loc_00AF129E;
    result = (unsigned int)(a4) + v_stack_m138 * 1;
    if (((unsigned int)(a4) + v_stack_m138 * 1) < v_stack_m138) {
        result = *(unsigned __int8 *)(v_r13);
    }
    result = memcpy(result, v_stack_m138, (unsigned int)(a4), v_stack_mC8);
    v_stack_mB0 = result;
    v_stack_mB8 = (unsigned __int16)((unsigned int)(a4));
    v_stack_mB6 = (unsigned __int16)((unsigned int)(a4));
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_stack_m138 + 48), 1, (unsigned int)(a4), v_stack_mC8);
    result = SepAddAgentIdClaimToToken(v_stack_m138, v_stack_mB8, (unsigned int)(a4), v_stack_mC8);
    v_stack_m130 = (unsigned int)(result);
    if (sign_flag) goto loc_00AF1338;
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(v_rip - 11396631);
        result = a1;
        result = (result) + (a1);
        *(unsigned int *)(v_stack_m138 + 56) = (unsigned int)(result);
        result = (result) >> (32);
        *(unsigned int *)(v_stack_m138 + 60) = (unsigned int)(result);
    }
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m138 + 48), v_stack_mB8, (unsigned int)(a4), v_stack_mC8);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m138 + 48), v_stack_mB8, (unsigned int)(a4), v_stack_mC8);
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)(a4), v_stack_mC8);
    goto loc_00AF1648;
loc_00AF1378:
    goto loc_00AF104A;
loc_00AF1382:
    goto loc_00AF0B0A;
loc_00AF138C:
    result = Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline(result, a2, (unsigned int)(a4), v_stack_mC8);
    if ((unsigned int)(result) == 0) goto loc_00AF1382;
    if (((unsigned int)((unsigned int)(a4))) != 4) goto loc_00AF0EA8;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AF13AE;
    result = RtlReadULongFromUser(v_stack_m138, a2, (unsigned int)(a4), v_stack_mC8);
    goto loc_00AF13B1;
loc_00AF13AE:
loc_00AF13B1:
    v_stack_m10C = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m138)));
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_stack_m138 + 48), 1, (unsigned int)(a4), v_stack_mC8);
    if (v_stack_m10C == ((unsigned int)((unsigned int)(v_stack_m130)))) goto loc_00AF13F0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m138 + 1168))) | (1));
    goto loc_00AF13F3;
loc_00AF13F0:
    result = (unsigned int)((result) & (0xFFFFFFFEULL));
loc_00AF13F3:
    *(unsigned int *)(v_stack_m138 + 1168) = (unsigned int)(result);
    goto loc_00AF0E51;
loc_00AF1411:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5146205), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned int)(a4), v_stack_mC8);
    if ((unsigned __int8)(result) == 0) goto loc_00AF0700;
    if (((unsigned int)((unsigned int)(a4))) != 4) goto loc_00AF0EA8;
    v_stack_mA4 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m138)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m138))) != 0) goto loc_00AF18CF;
    if (((*(unsigned int *)(result + 200)) & (0x80000ULL)) == 0) goto loc_00AF18CF;
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_stack_m138 + 48), 1, (unsigned int)(a4), v_stack_mC8);
    result = (*(unsigned __int64 *)(v_rip - 11396997)) + (*(unsigned __int64 *)(v_rip - 11396997));
    *(unsigned int *)(v_stack_m138 + 56) = (unsigned int)(result);
    result = (result) >> (32);
    *(unsigned int *)(v_stack_m138 + 60) = (unsigned int)(result);
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m138 + 48), v_stack_m138, (unsigned int)(a4), v_stack_mC8);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m138 + 48), v_stack_m138, (unsigned int)(a4), v_stack_mC8);
    goto loc_00AF18CF;
loc_00AF14D5:
    if (((unsigned int)((unsigned int)(a4))) != 4) goto loc_00AF0EA8;
    v_stack_mA0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m138)));
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5145989), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned int)(a4), v_stack_mC8);
    if ((unsigned __int8)(result) == 0) goto loc_00AF0700;
    result = SeSetPrivateNameSpaceToken(v_stack_m138, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m138)))), (unsigned int)(a4), v_stack_mC8);
    goto loc_00AF0714;
loc_00AF1522:
    v_stack_mF0 = (unsigned int)(v_stack_m130);
    if (v_stack_m138 == 0) goto loc_00AF0EA8;
    if (((unsigned int)((unsigned int)(a4))) < 16) goto loc_00AF0EA8;
    result = SepCaptureTokenSecurityAttributesAndOperationsInformation(v_stack_m138, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mF0, v_stack_mC8);
    if (!sign_flag) goto loc_00AF155F;
loc_00AF1557:
    goto loc_00AF0B0A;
loc_00AF155F:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5145871), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mF0, v_stack_mC8);
    v_r14 = (unsigned int)((unsigned int)(result));
    if ((unsigned __int8)(result) == 0) { v_r14 = (unsigned int)((unsigned int)(0xC0000061ULL)); }
    v_stack_m130 = (unsigned int)(v_r14);
    if (!sign_flag) goto loc_00AF1595;
    result = SepReleaseTokenSecurityAttributesAndOperationsInformation(v_stack_mF0, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), v_stack_mF0, v_stack_mC8);
    goto loc_00AF1557;
loc_00AF1595:
    result = SepShouldSetDelinkFlags(*(unsigned __int64 *)(v_stack_mF0 + 8), *(unsigned __int64 *)(v_stack_mF0), v_stack_mF0, v_stack_mC8);
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_stack_m138 + 48), 1, v_stack_mF0, v_stack_mC8);
    result = AuthzBasepSetSecurityAttributesToken(*(unsigned __int64 *)(v_stack_m138 + 776), *(unsigned __int64 *)(v_stack_mF0 + 8), *(unsigned __int64 *)(v_stack_mF0), v_stack_mC8);
    v_stack_m130 = (unsigned int)(result);
    if (sign_flag) goto loc_00AF1606;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
    }
    result = (*(unsigned __int64 *)(v_rip - 11397381)) + (*(unsigned __int64 *)(v_rip - 11397381));
    *(unsigned int *)(v_stack_m138 + 56) = (unsigned int)(result);
    result = (result) >> (32);
    *(unsigned int *)(v_stack_m138 + 60) = (unsigned int)(result);
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m138 + 48), *(unsigned __int64 *)(v_stack_mF0 + 8), *(unsigned __int64 *)(v_stack_mF0), v_stack_mC8);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m138 + 48), *(unsigned __int64 *)(v_stack_mF0 + 8), *(unsigned __int64 *)(v_stack_mF0), v_stack_mC8);
    result = SepReleaseTokenSecurityAttributesAndOperationsInformation(v_stack_mF0, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), *(unsigned __int64 *)(v_stack_mF0), v_stack_mC8);
loc_00AF1648:
    goto loc_00AF104A;
loc_00AF1651:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(v_stack_mF0, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), *(unsigned __int64 *)(v_stack_mF0), v_stack_mC8);
    if ((unsigned int)(result) == 0) goto loc_00AF1382;
    if (((unsigned int)((unsigned int)(a4))) != 4) goto loc_00AF0EA8;
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AF167E;
    result = RtlReadULongFromUser((unsigned __int8)(result), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), *(unsigned __int64 *)(v_stack_mF0), v_stack_mC8);
    v_stack_mD4 = (unsigned int)(result);
    goto loc_00AF168D;
loc_00AF167E:
    v_stack_mD4 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned __int8)(result))));
loc_00AF168D:
    if ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned __int8)(result)))) == 0) goto loc_00AF169B;
    goto loc_00AF0B0A;
loc_00AF169B:
    if (((*(unsigned int *)(v_stack_m138 + 200)) & (0x4000ULL)) != 0) goto loc_00AF16B1;
    goto loc_00AF0B0A;
loc_00AF16B1:
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5145533), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), *(unsigned __int64 *)(v_stack_mF0), v_stack_mC8);
    if ((unsigned __int8)(result) == 0) goto loc_00AF0700;
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_stack_m138 + 48), 1, *(unsigned __int64 *)(v_stack_mF0), v_stack_mC8);
    result = SepRemoveAceFromTokenDefaultDacl(v_stack_m138, *(unsigned __int64 *)(v_stack_m138 + 784), *(unsigned __int64 *)(v_stack_mF0), v_stack_mC8);
    if (*(unsigned __int64 *)(v_stack_m138 + 784) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m138 + 784), a2, *(unsigned __int64 *)(v_stack_mF0), v_stack_mC8);
        *(unsigned __int64 *)(v_stack_m138 + 784) = (unsigned int)(v_stack_m130);
    }
    if (*(unsigned __int64 *)(v_stack_m138 + 792) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m138 + 792), a2, *(unsigned __int64 *)(v_stack_mF0), v_stack_mC8);
        *(unsigned __int64 *)(v_stack_m138 + 792) = (unsigned int)(v_stack_m130);
        *(unsigned int *)(v_stack_m138 + 800) = (unsigned int)((unsigned int)(v_stack_m130));
        a1 = v_stack_m138 + 808;
        a2 = 0;
        a3 = 272;
        result = memset(a1, a2, a3, v_stack_mC8);
    }
    if (*(unsigned __int64 *)(v_stack_m138 + 1080) != 0) {
        a1 = *(unsigned int *)(v_stack_m138 + 120);
        result = SepDereferenceLowBoxNumberEntry(a1, *(unsigned __int64 *)(v_stack_m138 + 1080), a3, v_stack_mC8);
        *(unsigned __int64 *)(v_stack_m138 + 1080) = (unsigned int)(v_stack_m130);
    }
    if (*(unsigned __int64 *)(v_stack_m138 + 1088) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m138 + 216);
        a1 = (a1) + (96);
        a4 = 0;
        a2 = 0;
        result = SepDereferenceCachedHandlesEntryInternal(a1, a2, *(unsigned __int64 *)(v_stack_m138 + 1088), a4);
        *(unsigned __int64 *)(v_stack_m138 + 1088) = (unsigned int)(v_stack_m130);
    }
    goto loc_00AF0D96;
loc_00AF17BA:
    if (((unsigned int)((unsigned int)(a4))) != 4) goto loc_00AF0EA8;
    v_stack_mD0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m138)));
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5145248), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), *(unsigned __int64 *)(v_stack_m138 + 1088), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AF0700;
    if ((*(unsigned __int8 *)(v_stack_m138 + 204)) == ((unsigned __int8)((unsigned int)(v_stack_m130)))) goto loc_00AF17F8;
    goto loc_00AF0B0A;
loc_00AF17F8:
    result = SeSetMandatoryPolicyToken(v_stack_m138, v_stack_mD0, *(unsigned __int64 *)(v_stack_m138 + 1088), a4);
    goto loc_00AF0714;
loc_00AF1820:
    if (((unsigned int)((unsigned int)(a4))) != 4) goto loc_00AF0EA8;
    v_stack_mCC = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m138)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m138))) == 0) goto loc_00AF184F;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5145142), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), *(unsigned __int64 *)(v_stack_m138 + 1088), a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AF0700;
loc_00AF184F:
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_stack_m138 + 48), 1, *(unsigned __int64 *)(v_stack_m138 + 1088), a4);
    if (v_stack_mCC == ((unsigned int)((unsigned int)(v_stack_m130)))) goto loc_00AF188E;
    goto loc_00AF1892;
loc_00AF188E:
loc_00AF1892:
    *(unsigned int *)(v_stack_m138 + 200) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m138 + 200)));
    result = (*(unsigned __int64 *)(v_rip - 11398039)) + (*(unsigned __int64 *)(v_rip - 11398039));
    *(unsigned int *)(v_stack_m138 + 56) = (unsigned int)(result);
    result = (result) >> (32);
    *(unsigned int *)(v_stack_m138 + 60) = (unsigned int)(result);
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m138 + 48), v_stack_m138, *(unsigned __int64 *)(v_stack_m138 + 1088), a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m138 + 48), v_stack_m138, *(unsigned __int64 *)(v_stack_m138 + 1088), a4);
loc_00AF18CF:
    goto loc_00AF0B0A;
loc_00AF18E9:
    if (((unsigned int)((unsigned int)(a4))) < 16) goto loc_00AF0EA8;
    v_stack_m148 = v_stack_m9C;
    v_stack_m150 = v_stack_mC0;
    v_stack_m168 = (unsigned int)((unsigned int)(v_stack_m130));
    a4 = 0;
    result = SeCaptureSidAndAttributesArray(v_stack_m138, a4 + 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    v_stack_m130 = (unsigned int)(result);
    if (sign_flag) goto loc_00AF0714;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mC0) + 2))) - (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4275923) + 2)));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_mC0) + 6);
        result = *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 4275923) + 6);
        a1 = (unsigned int)((a1) - ((unsigned int)(result)));
    }
    result = ((unsigned int)(a1) == 0) ? 1 : 0;
    if ((unsigned int)(result) != 0) goto loc_00AF197F;
loc_00AF1962:
    result = ObfDereferenceObject(v_stack_m138, *(unsigned __int64 *)(v_rip + 4275923), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    result = SeReleaseLuidAndAttributesArray(v_stack_mC0, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    goto loc_00AF1ED9;
loc_00AF197F:
    result = RtlSubAuthorityCountSid(*(unsigned __int64 *)(v_stack_mC0), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    if ((unsigned __int8)(*(unsigned __int8 *)(result)) != 0) goto loc_00AF1993;
    goto loc_00AF19AA;
loc_00AF1993:
    result = RtlSubAuthoritySid(*(unsigned __int64 *)(v_stack_mC0), *(unsigned __int8 *)(result) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result)))) > 0x4000ULL) goto loc_00AF1962;
loc_00AF19AA:
    v_stack_m88 = v_stack_m138;
    result = ExAcquireResourceExclusiveLite(*(unsigned __int64 *)(v_stack_m138 + 48), 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    result = SepLocateTokenIntegrity(v_stack_m138, 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    if (result != 0) goto loc_00AF19F6;
    goto loc_00AF1E8B;
loc_00AF19F6:
    v_stack_m118 = *(unsigned __int64 *)(result);
    result = RtlSubAuthorityCountSid(*(unsigned __int64 *)(result), 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    v_stack_mE8 = (unsigned int)(*(unsigned __int8 *)(result));
    if ((unsigned __int8)(*(unsigned __int8 *)(result)) != 0) goto loc_00AF1A1A;
    goto loc_00AF1A30;
loc_00AF1A1A:
    result = RtlSubAuthoritySid(v_stack_m118, (unsigned int)((unsigned int)(*(unsigned __int8 *)(result))) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
loc_00AF1A30:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(result))))) goto loc_00AF1A69;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 5144633), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    if ((unsigned __int8)(result) != 0) goto loc_00AF1A52;
    goto loc_00AF1E8B;
loc_00AF1A52:
    if ((*(unsigned __int8 *)((unsigned int)(0xC0000061ULL) + 204)) == ((unsigned __int8)((unsigned int)(v_stack_m130)))) goto loc_00AF1BA8;
    goto loc_00AF1E8B;
loc_00AF1A69:
    if ((unsigned __int8)(result) != 0) goto loc_00AF1A71;
    goto loc_00AF1A80;
loc_00AF1A71:
    result = RtlSubAuthoritySid(v_stack_m118, (unsigned int)((unsigned int)(*(unsigned __int8 *)(result))) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
loc_00AF1A80:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(result))))) goto loc_00AF1BA8;
    result = Feature_871661881__private_IsEnabledDeviceUsageNoInline(v_stack_m118, (unsigned int)((unsigned int)(*(unsigned __int8 *)(result))) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    if ((unsigned int)(result) == 0) goto loc_00AF1BA0;
    v_stack_m108 = (unsigned int)((unsigned int)(v_stack_m130));
    result = RtlQueryElevationFlags(v_stack_m108, (unsigned int)((unsigned int)(*(unsigned __int8 *)(result))) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    result = (unsigned __int8)(((unsigned int)(v_stack_m108)) & (24));
    if (((unsigned __int8)(result)) != 16) goto loc_00AF1BA0;
    result = RtlSubAuthorityCountSid(*(unsigned __int64 *)(result), (unsigned int)((unsigned int)(*(unsigned __int8 *)(result))) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    if ((unsigned __int8)(*(unsigned __int8 *)(result)) == 0) goto loc_00AF1BA0;
    result = RtlSubAuthoritySid(*(unsigned __int64 *)(result), *(unsigned __int8 *)(result) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    if ((*(unsigned int *)(result)) < 0x3000ULL) goto loc_00AF1BA0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = SeCaptureSubjectContext(v_stack_m58, *(unsigned __int8 *)(result) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m48 + 48), 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    result = SepLocateTokenIntegrity(v_stack_m48, 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    result = RtlSubAuthorityCountSid(*(unsigned __int64 *)(result), 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    if ((unsigned __int8)(*(unsigned __int8 *)(result)) != 0) goto loc_00AF1B4B;
    goto loc_00AF1B58;
loc_00AF1B4B:
    result = RtlSubAuthoritySid(*(unsigned __int64 *)(result), *(unsigned __int8 *)(result) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
loc_00AF1B58:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result)))) >= 0x3000ULL) goto loc_00AF1B84;
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m48 + 48), *(unsigned __int8 *)(result) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m48 + 48), *(unsigned __int8 *)(result) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    result = SeReleaseSubjectContext(v_stack_m58, *(unsigned __int8 *)(result) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    goto loc_00AF1E8B;
loc_00AF1B84:
    result = ExReleaseResourceLite(v_stack_m58, *(unsigned __int8 *)(result) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    result = KeLeaveCriticalRegion(v_stack_m58, *(unsigned __int8 *)(result) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    result = SeReleaseSubjectContext(v_stack_m58, *(unsigned __int8 *)(result) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
loc_00AF1BA0:
loc_00AF1BA8:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(v_stack_m58, *(unsigned __int8 *)(result) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    if ((unsigned int)(result) == 0) goto loc_00AF1C3F;
    result = RtlSubAuthorityCountSid(*(unsigned __int64 *)(result), *(unsigned __int8 *)(result) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    if ((unsigned __int8)(*(unsigned __int8 *)(result)) != 0) goto loc_00AF1BCC;
    goto loc_00AF1BD9;
loc_00AF1BCC:
    result = RtlSubAuthoritySid(*(unsigned __int64 *)(result), *(unsigned __int8 *)(result) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
loc_00AF1BD9:
    result = (unsigned int)(*(unsigned int *)(result));
    v_r13 = (unsigned __int8)((unsigned int)(v_stack_m130));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(result))))) {
        v_stack_m78 = v_xmm0;
        v_stack_m68 = v_xmm0;
        a1 = v_stack_m78;
        result = SeCaptureSubjectContext(a1, *(unsigned __int8 *)(result) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
        a1 = v_stack_m78;
        result = SeLockSubjectContext(a1, *(unsigned __int8 *)(result) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
        result = v_stack_m68;
        v_r13 = *(unsigned int *)(result + 200);
        a1 = v_stack_m78;
        result = SeUnlockSubjectContext(a1, *(unsigned __int8 *)(result) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
        a1 = v_stack_m78;
        result = SeReleaseSubjectContext(a1, *(unsigned __int8 *)(result) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
        v_r13 = (unsigned int)((v_r13) >> (14));
        v_r13 = (unsigned __int8)(~(v_r13));
        v_r13 = (unsigned __int8)((v_r13) & (1));
    }
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1)) == 0) goto loc_00AF1E86;
    result = RtlSubAuthoritySid(*(unsigned __int64 *)(result), *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    *(unsigned int *)(result) = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result)))) < 0x3000ULL) {
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result)))) >= ((unsigned int)((unsigned int)(0x2000ULL)))) goto loc_00AF1C9E;
    goto loc_00AF1E62;
loc_00AF1C9E:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(*(unsigned __int64 *)(result), *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1) - 1, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m138 + 200))) & (0x4000ULL));
    if ((unsigned int)(result) == 0) goto loc_00AF1DAC;
    if ((unsigned int)(a1) == 0) goto loc_00AF1D70;
    if ((unsigned __int8)(v_r13) == 0) goto loc_00AF1D70;
    result = SepRemoveAceFromTokenDefaultDacl(v_stack_m138, *(unsigned __int64 *)(v_stack_m138 + 784), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
    if (*(unsigned __int64 *)(v_stack_m138 + 784) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m138 + 784), a2, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
        *(unsigned __int64 *)(v_stack_m138 + 784) = (unsigned int)(v_stack_m130);
    }
    if (*(unsigned __int64 *)(v_stack_m138 + 792) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m138 + 792), a2, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), a4);
        *(unsigned __int64 *)(v_stack_m138 + 792) = (unsigned int)(v_stack_m130);
        *(unsigned int *)(v_stack_m138 + 800) = (unsigned int)((unsigned int)(v_stack_m130));
        a1 = v_stack_m138 + 808;
        a2 = 0;
        a3 = 272;
        result = memset(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_stack_m138 + 1080) != 0) {
        a1 = *(unsigned int *)(v_stack_m138 + 120);
        result = SepDereferenceLowBoxNumberEntry(a1, *(unsigned __int64 *)(v_stack_m138 + 1080), a3, a4);
        *(unsigned __int64 *)(v_stack_m138 + 1080) = (unsigned int)(v_stack_m130);
    }
    if (*(unsigned __int64 *)(v_stack_m138 + 1088) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m138 + 216);
        a1 = (a1) + (96);
        a4 = 0;
        a2 = 0;
        result = SepDereferenceCachedHandlesEntryInternal(a1, a2, *(unsigned __int64 *)(v_stack_m138 + 1088), a4);
        *(unsigned __int64 *)(v_stack_m138 + 1088) = (unsigned int)(v_stack_m130);
    }
    result = RtlSubAuthorityCountSid(*(unsigned __int64 *)(result), a2, *(unsigned __int64 *)(v_stack_m138 + 1088), a4);
    if ((unsigned __int8)(*(unsigned __int8 *)(result)) == 0) goto loc_00AF1E62;
    result = RtlSubAuthoritySid(*(unsigned __int64 *)(result), *(unsigned __int8 *)(result) - 1, *(unsigned __int64 *)(v_stack_m138 + 1088), a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result)))) < ((unsigned int)((unsigned int)(0x2000ULL)))) goto loc_00AF1E62;
    goto loc_00AF1E62;
loc_00AF1DAC:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result))) == 0) goto loc_00AF1E5C;
    result = SepRemoveAceFromTokenDefaultDacl(v_stack_m138, *(unsigned __int64 *)(v_stack_m138 + 784), *(unsigned __int64 *)(v_stack_m138 + 1088), a4);
    if (*(unsigned __int64 *)(v_stack_m138 + 784) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m138 + 784), a2, *(unsigned __int64 *)(v_stack_m138 + 1088), a4);
        *(unsigned __int64 *)(v_stack_m138 + 784) = (unsigned int)(v_stack_m130);
    }
    if (*(unsigned __int64 *)(v_stack_m138 + 792) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_m138 + 792), a2, *(unsigned __int64 *)(v_stack_m138 + 1088), a4);
        *(unsigned __int64 *)(v_stack_m138 + 792) = (unsigned int)(v_stack_m130);
        *(unsigned int *)(v_stack_m138 + 800) = (unsigned int)((unsigned int)(v_stack_m130));
        a1 = v_stack_m138 + 808;
        a2 = 0;
        a3 = 272;
        result = memset(a1, a2, a3, a4);
    }
    if (*(unsigned __int64 *)(v_stack_m138 + 1080) != 0) {
        a1 = *(unsigned int *)(v_stack_m138 + 120);
        result = SepDereferenceLowBoxNumberEntry(a1, *(unsigned __int64 *)(v_stack_m138 + 1080), a3, a4);
        *(unsigned __int64 *)(v_stack_m138 + 1080) = (unsigned int)(v_stack_m130);
    }
    if (*(unsigned __int64 *)(v_stack_m138 + 1088) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m138 + 216);
        a1 = (a1) + (96);
        a4 = 0;
        a2 = 0;
        result = SepDereferenceCachedHandlesEntryInternal(a1, a2, *(unsigned __int64 *)(v_stack_m138 + 1088), a4);
        *(unsigned __int64 *)(v_stack_m138 + 1088) = (unsigned int)(v_stack_m130);
    }
loc_00AF1E62:
    result = (*(unsigned __int64 *)(v_rip - 11399521)) + (*(unsigned __int64 *)(v_rip - 11399521));
    *(unsigned int *)(v_stack_m138 + 56) = (unsigned int)(result);
    result = (result) >> (32);
    *(unsigned int *)(v_stack_m138 + 60) = (unsigned int)(result);
    goto loc_00AF1E8B;
loc_00AF1E86:
loc_00AF1E8B:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m88 + 48), a2, *(unsigned __int64 *)(v_stack_m138 + 1088), a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m88 + 48), a2, *(unsigned __int64 *)(v_stack_m138 + 1088), a4);
    result = ObfDereferenceObject(v_stack_m138, a2, *(unsigned __int64 *)(v_stack_m138 + 1088), a4);
    result = SeReleaseLuidAndAttributesArray(v_stack_mC0, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), *(unsigned __int64 *)(v_stack_m138 + 1088), a4);
    goto loc_00AF0B12;
loc_00AF1ED4:
loc_00AF1ED9:
    return (unsigned int)(0xC0000003ULL);
loc_00AF1EF7:
    result = ExRaiseDatatypeMisalignment(v_stack_mC0, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), *(unsigned __int64 *)(v_stack_m138 + 1088), a4);
loc_00AF1EFD:
    result = ExRaiseDatatypeMisalignment(v_stack_mC0, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), *(unsigned __int64 *)(v_stack_m138 + 1088), a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtSetInformationToken(int64_t Arg1, int32_t Arg2, void *Arg3, int32_t Arg4)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint32_t v_stack_m108;
    uint32_t v_stack_m10C;
    uint32_t v_stack_m110;
    uint64_t v_stack_m118;
    uint64_t v_stack_m120;
    uint8_t v_stack_m124;
    uint32_t v_stack_m128;
    uint8_t v_stack_m12B;
    uint8_t v_stack_m12C;
    uint32_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m148;
    uint64_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint32_t v_stack_m188;
    uint64_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint32_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m94;
    uint32_t v_stack_m98;
    uint64_t v_stack_m9C;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA4;
    uint32_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint16_t v_stack_mB6;
    uint16_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint32_t v_stack_mCC;
    uint32_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint32_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (352);
    local_rdi = 0;
    v_stack_m12C = 0;
    v_stack_m128 = 0;
    *(uint64_t *)(local_rsp - 0xC8) = 0;
    *(uint64_t *)(local_rsp - 0xC0) = 0;
    v_stack_m12B = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AF05CC;
    if (Arg4 == 0) goto loc_00AF05BB;
    if ((((uint8_t)(Arg3)) & (3)) != 0) goto loc_00AF1EF7;
    if ((Arg3 + (uint32_t)(Arg4) * 1) > local_r13) goto loc_00AF05B5;
    if ((Arg3 + (uint32_t)(Arg4) * 1) >= Arg3) goto loc_00AF05C5;
loc_00AF05B5:
    goto loc_00AF05C5;
loc_00AF05BB:
loc_00AF05C5:
    goto loc_00AF05D6;
loc_00AF05CC:
loc_00AF05D6:
    if (((uint32_t)((int32_t)(Arg2))) > 58) goto loc_00AF05EB;
    if (((uint32_t)((int32_t)(Arg2))) < 58) goto loc_00AF0625;
loc_00AF05EB:
    result = Feature_ShadowAdmin__private_IsEnabledDeviceUsageNoInline(Arg3 + (uint32_t)(Arg4) * 1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_00AF1ED4;
    v_stack_m110 = 0;
    result = RtlQueryElevationFlags(v_stack_m110, Arg2, Arg3, Arg4);
    if (sign_flag) goto loc_00AF1ED4;
    result = (uint8_t)(((uint32_t)(v_stack_m110)) & (24));
    if (((uint8_t)(result)) != 16) goto loc_00AF1ED4;
    if (((uint32_t)((int32_t)(Arg2))) != -2) goto loc_00AF1ED4;
loc_00AF0625:
    result = Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline(v_stack_m110, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) != 0) goto loc_00AF0637;
    if (((uint32_t)((int32_t)(Arg2))) == 52) goto loc_00AF1ED4;
loc_00AF0637:
    if (((uint32_t)((int32_t)(Arg2))) != 12) goto loc_00AF0648;
    goto loc_00AF0657;
loc_00AF0648:
    if (((uint32_t)((int32_t)(Arg2))) == 19) goto loc_00AF0652;
    if (((uint32_t)((int32_t)(Arg2))) == -2) {
        Arg2 = 136;
    }
    v_stack_m138 = 0;
    v_stack_m160 = 0;
    v_stack_m168 = v_stack_m138;
    result = ObReferenceObjectByHandle(Arg1, Arg2, *(uint64_t *)(v_rip + 0x4E79C2), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    v_stack_mE8 = v_stack_m138;
    if (sign_flag) goto loc_00AF1ED9;
    if (((uint32_t)((int32_t)(Arg2))) > 24) goto loc_00AF1186;
    if (((uint32_t)((int32_t)(Arg2))) == 24) goto loc_00AF1152;
    if (((uint32_t)((int32_t)(Arg2))) > 14) goto loc_00AF0DBA;
    if (((uint32_t)((int32_t)(Arg2))) == 14) goto loc_00AF0CFC;
    if (((uint32_t)((int32_t)(Arg2))) == -2) goto loc_00AF0CC4;
    if (((uint32_t)((int32_t)(Arg2))) == 4) goto loc_00AF0AC3;
    if (((uint32_t)((int32_t)(Arg2))) == 5) goto loc_00AF0940;
    if (((uint32_t)((int32_t)(Arg2))) == 6) goto loc_00AF072E;
    if (((uint32_t)((int32_t)(Arg2))) != 12) goto loc_00AF11D3;
    if (((uint32_t)((uint32_t)(Arg4))) != 4) goto loc_00AF0AC9;
    v_stack_m98 = (uint32_t)((uint32_t)(*(uint32_t *)(arg3)));
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E9381), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), *(uint64_t *)(v_rip + 0x4E79C2), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if ((uint8_t)(result) != 0) goto loc_00AF070A;
loc_00AF0700:
    goto loc_00AF0B0A;
loc_00AF070A:
    result = SeSetSessionIdToken(v_stack_m138, (uint32_t)((uint32_t)((uint32_t)(0xC0000061ULL))), *(uint64_t *)(v_rip + 0x4E79C2), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
loc_00AF0714:
    goto loc_00AF0B0A;
loc_00AF072E:
    if (((uint32_t)((uint32_t)(Arg4))) < 8) goto loc_00AF0AC9;
    v_stack_m120 = *(uint64_t *)(arg3);
    if (*(uint64_t *)(arg3) == 0) goto loc_00AF0771;
    v_stack_m150 = v_stack_m128;
    v_stack_m158 = v_stack_m120;
    v_stack_m168 = 1;
    result = SeCaptureAcl(*(uint64_t *)(arg3), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), *(uint64_t *)(v_rip + 0x4E79C2), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    v_stack_m130 = (uint32_t)(result);
    goto loc_00AF077B;
loc_00AF0771:
    v_stack_m128 = 0;
    v_stack_m130 = 0;
loc_00AF077B:
    if (sign_flag) goto loc_00AF0B0A;
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_stack_m138 + 0x30), 1, *(uint64_t *)(v_rip + 0x4E79C2), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    result = (uint32_t)(((uint32_t)(v_stack_m128)) + (8));
    v_stack_m128 = (uint32_t)(result + *(uint8_t *)(*(uint64_t *)(v_stack_m138 + 0xA8) + 0x1) * 4);
    if (((uint32_t)(result + *(uint8_t *)(*(uint64_t *)(v_stack_m138 + 0xA8) + 0x1) * 4)) <= (*(uint32_t *)(v_stack_m138 + 0x88))) goto loc_00AF0806;
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m138 + 0x30), result + *(uint8_t *)(*(uint64_t *)(v_stack_m138 + 0xA8) + 0x1) * 4, *(uint64_t *)(v_rip + 0x4E79C2), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m138 + 0x30), result + *(uint8_t *)(*(uint64_t *)(v_stack_m138 + 0xA8) + 0x1) * 4, *(uint64_t *)(v_rip + 0x4E79C2), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    result = ObfDereferenceObject(v_stack_m138, result + *(uint8_t *)(*(uint64_t *)(v_stack_m138 + 0xA8) + 0x1) * 4, *(uint64_t *)(v_rip + 0x4E79C2), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (v_stack_m120 != 0) {
        Arg2 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        result = SeReleaseAcl(v_stack_m120, Arg2, *(uint64_t *)(v_rip + 0x4E79C2), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    }
    goto loc_00AF1ED9;
loc_00AF0806:
    result = SepExpandDynamic(v_stack_m138, Arg2, *(uint64_t *)(v_rip + 0x4E79C2), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    v_stack_m130 = (uint32_t)(result);
    if (!sign_flag) goto loc_00AF084D;
loc_00AF0816:
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m138 + 0x30), Arg2, *(uint64_t *)(v_rip + 0x4E79C2), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m138 + 0x30), Arg2, *(uint64_t *)(v_rip + 0x4E79C2), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    result = ObfDereferenceObject(v_stack_m138, Arg2, *(uint64_t *)(v_rip + 0x4E79C2), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (v_stack_m120 != 0) {
        Arg2 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        result = SeReleaseAcl(v_stack_m120, Arg2, *(uint64_t *)(v_rip + 0x4E79C2), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    }
    goto loc_00AF1ED9;
loc_00AF084D:
    if (*(uint64_t *)(v_stack_m138 + 0xB8) == 0) goto loc_00AF088A;
    v_stack_m150 = v_stack_m94;
    v_stack_m158 = v_stack_mC8;
    v_stack_m168 = 1;
    Arg2 = 0;
    result = SeCaptureAcl(*(uint64_t *)(v_stack_m138 + 0xB8), Arg2, *(uint64_t *)(v_rip + 0x4E79C2), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    v_stack_m130 = (uint32_t)(result);
    if (sign_flag) goto loc_00AF0816;
loc_00AF088A:
    result = SepFreeDefaultDacl(v_stack_m138, Arg2, *(uint64_t *)(v_rip + 0x4E79C2), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (v_stack_m120 != 0) {
        Arg2 = v_stack_m120;
        Arg1 = v_stack_m138;
        result = SepAppendDefaultDacl(Arg1, Arg2, *(uint64_t *)(v_rip + 0x4E79C2), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    }
    v_stack_m168 = v_stack_m120;
    result = SeTokenDefaultDaclChangedAuditAlarm(Arg1, v_stack_m138, v_stack_p8, v_stack_mC8);
    result = (*(uint64_t *)(v_rip - 0xADDBC3)) + (*(uint64_t *)(v_rip - 0xADDBC3));
    *(uint32_t *)(v_stack_m138 + 0x38) = (uint32_t)(result);
    result = (result) >> (32);
    *(uint32_t *)(v_stack_m138 + 0x3C) = (uint32_t)(result);
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m138 + 0x30), v_stack_m138, v_stack_p8, v_stack_mC8);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m138 + 0x30), v_stack_m138, v_stack_p8, v_stack_mC8);
    result = ObfDereferenceObject(v_stack_m138, v_stack_m138, v_stack_p8, v_stack_mC8);
    if (v_stack_m120 != 0) {
        Arg2 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        result = SeReleaseAcl(v_stack_m120, Arg2, v_stack_p8, v_stack_mC8);
    }
    if (v_stack_mC8 != 0) {
        Arg2 = 0;
        result = SeReleaseAcl(v_stack_mC8, Arg2, v_stack_p8, v_stack_mC8);
    }
    result = 0;
    goto loc_00AF1ED9;
loc_00AF0940:
    if (((uint32_t)((uint32_t)(Arg4))) < 8) goto loc_00AF0AC9;
    v_stack_m100 = *(uint64_t *)(v_stack_m120);
    v_stack_m158 = v_stack_m100;
    v_stack_m160 = 1;
    result = SeCaptureSid(*(uint64_t *)(v_stack_m120), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_p8, v_stack_mC8);
    v_stack_m130 = (uint32_t)(result);
    if (sign_flag) goto loc_00AF0B0D;
    result = SepIdAssignableAsGroup(v_stack_m138, v_stack_m100, v_stack_p8, v_stack_mC8);
    if ((uint8_t)(result) != 0) goto loc_00AF099B;
    goto loc_00AF0A8E;
loc_00AF099B:
    v_stack_m128 = (uint32_t)(*(uint8_t *)(v_stack_m100 + 0x1) * 4 + 8);
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_stack_m138 + 0x30), 1, v_stack_p8, v_stack_mC8);
    result = *(uint64_t *)(v_stack_m138 + 0xB8);
    local_rsi = *(uint8_t *)(v_stack_m100 + 0x1) * 4 + 8;
    if (*(uint64_t *)(v_stack_m138 + 0xB8) != 0) {
        result = *(uint16_t *)(*(uint64_t *)(v_stack_m138 + 0xB8) + 0x2);
        local_rsi = (uint32_t)((*(uint8_t *)(v_stack_m100 + 0x1) * 4 + 8) + ((uint32_t)(result)));
        v_stack_m128 = (uint32_t)(local_rsi);
    }
    if (((uint32_t)(local_rsi)) <= (*(uint32_t *)(v_stack_m138 + 0x88))) goto loc_00AF0A13;
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m138 + 0x30), 1, v_stack_p8, v_stack_mC8);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m138 + 0x30), 1, v_stack_p8, v_stack_mC8);
    goto loc_00AF0A89;
loc_00AF0A13:
    result = SepExpandDynamic(v_stack_m138, (uint32_t)(v_stack_m128), v_stack_p8, v_stack_mC8);
    v_stack_m130 = (uint32_t)(result);
    if (!sign_flag) goto loc_00AF0A3F;
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m138 + 0x30), (uint32_t)(v_stack_m128), v_stack_p8, v_stack_mC8);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m138 + 0x30), (uint32_t)(v_stack_m128), v_stack_p8, v_stack_mC8);
    goto loc_00AF0A89;
loc_00AF0A3F:
    result = SepFreePrimaryGroup(v_stack_m138, (uint32_t)(v_stack_m128), v_stack_p8, v_stack_mC8);
    result = SepAppendPrimaryGroup(v_stack_m138, v_stack_m100, v_stack_p8, v_stack_mC8);
    result = (*(uint64_t *)(v_rip - 0xADDD56)) + (*(uint64_t *)(v_rip - 0xADDD56));
    *(uint32_t *)(v_stack_m138 + 0x38) = (uint32_t)(result);
    result = (result) >> (32);
    *(uint32_t *)(v_stack_m138 + 0x3C) = (uint32_t)(result);
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m138 + 0x30), v_stack_m100, v_stack_p8, v_stack_mC8);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m138 + 0x30), v_stack_m100, v_stack_p8, v_stack_mC8);
loc_00AF0A89:
loc_00AF0A8E:
    result = ObfDereferenceObject(v_stack_m138, v_stack_m100, v_stack_p8, v_stack_mC8);
    result = SeReleaseSid(v_stack_m100, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), 1, v_stack_mC8);
    goto loc_00AF1ED9;
loc_00AF0AC3:
    if (((uint32_t)((uint32_t)(Arg4))) >= 8) goto loc_00AF0ADB;
loc_00AF0AC9:
    result = ObfDereferenceObject(v_stack_m138, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), 1, v_stack_mC8);
    goto loc_00AF1ED9;
loc_00AF0ADB:
    v_stack_mF8 = *(uint64_t *)(v_stack_m138);
    v_stack_m158 = v_stack_mF8;
    v_stack_m160 = 1;
    result = SeCaptureSid(*(uint64_t *)(v_stack_m138), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), 1, v_stack_mC8);
    v_stack_m130 = (uint32_t)(result);
    if (!sign_flag) goto loc_00AF0B19;
loc_00AF0B0A:
loc_00AF0B0D:
    result = ObfDereferenceObject(v_stack_m138, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), 1, v_stack_mC8);
loc_00AF0B12:
    goto loc_00AF1ED9;
loc_00AF0B19:
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_stack_m138 + 0x30), 1, 1, v_stack_mC8);
loc_00AF0B40:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m130))))) >= (*(uint32_t *)(v_stack_m138 + 0x7C))) goto loc_00AF0C7A;
    result = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m130)))))) + ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m130))))));
    result = RtlEqualSid(v_stack_mF8, *(uint64_t *)(*(uint64_t *)(v_stack_m138 + 0x98) + result * 8), 1, v_stack_mC8);
    v_stack_m124 = (uint8_t)(result);
    if ((uint8_t)(result) == 0) goto loc_00AF0C02;
    result = SepIdAssignableAsOwner(v_stack_m138, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m130))))), 1, v_stack_mC8);
    if ((uint8_t)(result) == 0) goto loc_00AF0B92;
    *(uint32_t *)(v_stack_m138 + 0x90) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m130))));
    v_stack_m12C = 1;
    v_stack_m130 = (uint32_t)((uint32_t)(v_stack_m130));
    goto loc_00AF0B9E;
loc_00AF0B92:
    v_stack_m130 = 0xC000005AULL;
loc_00AF0B9E:
    result = v_stack_m12C;
    if ((uint8_t)(v_stack_m12C) != 0) {
        v_stack_m118 = (uint32_t)(v_stack_m130);
        Arg2 = *(uint64_t *)(v_rip - 0xADDEA6);
        result = Arg2;
        result = (result) + (Arg2);
        v_stack_m118 = result;
        *(uint32_t *)(v_stack_m138 + 0x38) = (uint32_t)(result);
        result = (result) >> (32);
        *(uint32_t *)(v_stack_m138 + 0x3C) = (uint32_t)(result);
    }
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m138 + 0x30), Arg2, 1, v_stack_mC8);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m138 + 0x30), Arg2, 1, v_stack_mC8);
    result = ObfDereferenceObject(v_stack_m138, Arg2, 1, v_stack_mC8);
    result = SeReleaseSid(v_stack_mF8, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), 1, v_stack_mC8);
    goto loc_00AF1ED9;
loc_00AF0C02:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m130)))) + 1);
    goto loc_00AF0B40;
loc_00AF0C7A:
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m138 + 0x30), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), 1, v_stack_mC8);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m138 + 0x30), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), 1, v_stack_mC8);
    result = ObfDereferenceObject(v_stack_m138, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), 1, v_stack_mC8);
    result = SeReleaseSid(v_stack_mF8, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), 1, v_stack_mC8);
    goto loc_00AF1ED9;
loc_00AF0CC4:
    if (((uint32_t)((uint32_t)(Arg4))) != 8) goto loc_00AF0EA8;
    v_stack_m30 = *(uint64_t *)(v_stack_m138);
    result = SepOneWayLinkLogonSessions(v_stack_m138, *(uint64_t *)(v_stack_m138), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
    goto loc_00AF0714;
loc_00AF0CFC:
    if (((uint32_t)((uint32_t)(Arg4))) != 4) goto loc_00AF0EA8;
    v_stack_m80 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m138)));
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E8D5E), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
    if ((uint8_t)(result) == 0) goto loc_00AF0700;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m138))) == 0) goto loc_00AF0D35;
loc_00AF0D2B:
    goto loc_00AF0B0A;
loc_00AF0D35:
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_stack_m138 + 0x30), 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m138 + 0xC8)))) & (32)) != 0) goto loc_00AF0D8E;
    result = (uint32_t)(*(uint32_t *)(v_stack_m138 + 0xC8));
    if ((*(uint32_t *)(v_rip + 0x4E72A0)) != 0) {
        Arg1 = v_stack_m138;
        result = SepRemoveTokenLogonSession(Arg1, 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
    }
    result = SepStopReferencingLogonSession(v_stack_m138, 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
    v_stack_m130 = (uint32_t)(result);
    if (sign_flag) goto loc_00AF0714;
loc_00AF0D8E:
loc_00AF0D96:
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m138 + 0x30), 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m138 + 0x30), 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
    local_rbx = 0;
    goto loc_00AF104A;
loc_00AF0DBA:
    local_rbx = (uint32_t)((local_rbx) - (16));
    if (condition_is_equal) goto loc_00AF0F8F;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00AF0EE0;
    local_rbx = (uint32_t)((local_rbx) - (2));
    if (condition_is_equal) goto loc_00AF0EA2;
    if (((uint32_t)(local_rbx)) != 4) goto loc_00AF11D3;
    if (((uint32_t)((uint32_t)(Arg4))) != ((uint32_t)(local_rbx))) goto loc_00AF0EA8;
    v_stack_mD8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m138)));
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E8D85), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
    if ((uint8_t)(result) == 0) goto loc_00AF0700;
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_stack_m138 + 0x30), 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
    if (v_stack_mD8 == ((uint32_t)((uint32_t)(v_stack_m130)))) goto loc_00AF0E47;
    goto loc_00AF0E4B;
loc_00AF0E47:
loc_00AF0E4B:
    *(uint32_t *)(v_stack_m138 + 0xC8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m138 + 0xC8)));
loc_00AF0E51:
    result = (*(uint64_t *)(v_rip - 0xADE150)) + (*(uint64_t *)(v_rip - 0xADE150));
    *(uint32_t *)(v_stack_m138 + 0x38) = (uint32_t)(result);
    result = (result) >> (32);
    *(uint32_t *)(v_stack_m138 + 0x3C) = (uint32_t)(result);
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m138 + 0x30), v_stack_m138, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m138 + 0x30), v_stack_m138, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
loc_00AF0E88:
    local_rbx = 0;
    goto loc_00AF0B0A;
loc_00AF0EA2:
    if (((uint32_t)((uint32_t)(Arg4))) == 8) goto loc_00AF0EB2;
loc_00AF0EA8:
    goto loc_00AF0B0A;
loc_00AF0EB2:
    v_stack_m38 = *(uint64_t *)(v_stack_m138);
    result = SepLinkLogonSessions(v_stack_m138, *(uint64_t *)(v_stack_m138), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
    goto loc_00AF0714;
loc_00AF0EE0:
    if (((uint32_t)((uint32_t)(Arg4))) != 8) goto loc_00AF0EA8;
    v_stack_m90 = *(uint64_t *)(v_stack_m138);
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E8B7D), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
    if ((uint8_t)(result) == 0) goto loc_00AF0700;
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_stack_m138 + 0x30), 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m138 + 0xE4))) | (*(uint32_t *)(v_stack_m138 + 0xE0)));
    if (!(condition_is_not_equal)) {
        result = v_stack_m90;
        *(uint64_t *)(v_stack_m138 + 0xE0) = result;
    }
    result = (*(uint64_t *)(v_rip - 0xADE24E)) + (*(uint64_t *)(v_rip - 0xADE24E));
    *(uint32_t *)(v_stack_m138 + 0x38) = (uint32_t)(result);
    result = (result) >> (32);
    *(uint32_t *)(v_stack_m138 + 0x3C) = (uint32_t)(result);
    goto loc_00AF103E;
loc_00AF0F8F:
    v_stack_mE0 = (uint32_t)(v_stack_m130);
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E8AD7), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
    if ((uint8_t)(result) == 0) goto loc_00AF0700;
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m138 + 0x30), 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m138 + 0x30), 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m138 + 0x30), 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
    if ((uint8_t)(*(uint8_t *)(v_stack_m138 + 0x77)) != 0) goto loc_00AF0D2B;
    if (v_stack_m138 != 0) goto loc_00AF1054;
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_stack_m138 + 0x30), 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
    *(uint8_t *)(v_stack_m138 + 0x77) = 1;
    result = (*(uint64_t *)(v_rip - 0xADE315)) + (*(uint64_t *)(v_rip - 0xADE315));
    *(uint32_t *)(v_stack_m138 + 0x38) = (uint32_t)(result);
    result = (result) >> (32);
    *(uint32_t *)(v_stack_m138 + 0x3C) = (uint32_t)(result);
loc_00AF103E:
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m138 + 0x30), v_stack_m138, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m138 + 0x30), v_stack_m138, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
loc_00AF104A:
    goto loc_00AF0B0A;
loc_00AF1054:
    v_stack_m158 = v_stack_mE0;
    result = SepCaptureAuditPolicy(v_stack_m138, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
    v_stack_m130 = (uint32_t)(result);
    if (sign_flag) goto loc_00AF0714;
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_stack_m138 + 0x30), 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mC8);
    *(uint8_t *)(v_stack_m138 + 0x77) = 2;
    *(uint64_t *)(v_stack_m138 + 0x58) = v_xmm0;
    *(uint64_t *)(v_stack_m138 + 0x58 + 0x10) = v_xmm1;
    *(uint32_t *)(v_stack_m138 + 0x58 + 0x18) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mE0 + 0x18)));
    *(uint16_t *)(v_stack_m138 + 0x58 + 0x1C) = (uint16_t)(*(uint16_t *)(v_stack_mE0 + 0x1C));
    *(uint8_t *)(v_stack_m138 + 0x58 + 0x1E) = (uint8_t)(*(uint8_t *)(v_stack_mE0 + 0x1E));
    result = (*(uint64_t *)(v_rip - 0xADE3D0)) + (*(uint64_t *)(v_rip - 0xADE3D0));
    *(uint32_t *)(v_stack_m138 + 0x38) = (uint32_t)(result);
    result = (result) >> (32);
    *(uint32_t *)(v_stack_m138 + 0x3C) = (uint32_t)(result);
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m138 + 0x30), *(uint64_t *)(v_rip - 0xADE3D0), v_stack_m138, v_stack_mC8);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m138 + 0x30), *(uint64_t *)(v_rip - 0xADE3D0), v_stack_m138, v_stack_mC8);
    result = SepModifyTokenPolicyCounter(v_stack_m138 + 88, 1, v_stack_m138, v_stack_mC8);
    result = ObfDereferenceObject(v_stack_m138, 1, v_stack_m138, v_stack_mC8);
    result = SepReleaseAuditPolicy(v_stack_mE0, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_m138, v_stack_mC8);
    goto loc_00AF0926;
loc_00AF1152:
    if (((uint32_t)((uint32_t)(Arg4))) != 4) goto loc_00AF0EA8;
    v_stack_mA8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m138)));
    result = SeSetVirtualizationToken(v_stack_m138, (uint32_t)(*(uint32_t *)(v_stack_m138)), v_stack_m138, v_stack_mC8);
    goto loc_00AF0E88;
loc_00AF1186:
    local_rbx = (uint32_t)((v_stack_m138 + 88) - (25));
    if (condition_is_equal) goto loc_00AF18E9;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00AF1820;
    local_rbx = (uint32_t)((local_rbx) - (1));
    if (condition_is_equal) goto loc_00AF17BA;
    local_rbx = (uint32_t)((local_rbx) - (2));
    if (condition_is_equal) goto loc_00AF1651;
    local_rbx = (uint32_t)((local_rbx) - (10));
    if (condition_is_equal) goto loc_00AF1522;
    local_rbx = (uint32_t)((local_rbx) - (3));
    if (condition_is_equal) goto loc_00AF14D5;
    local_rbx = (uint32_t)((local_rbx) - (3));
    if (condition_is_equal) goto loc_00AF1411;
    local_rbx = (uint32_t)((local_rbx) - (7));
    if (condition_is_equal) goto loc_00AF138C;
    if (((uint32_t)(local_rbx)) == 6) goto loc_00AF11DD;
loc_00AF11D3:
    goto loc_00AF1ED9;
loc_00AF11DD:
    result = Feature_AgentId2__private_IsEnabledDeviceUsageNoInline(v_stack_m138, (uint32_t)(*(uint32_t *)(v_stack_m138)), v_stack_m138, v_stack_mC8);
    if ((uint32_t)(result) == 0) goto loc_00AF1382;
    v_stack_mB4 = (uint32_t)((uint32_t)(v_stack_m130));
    if (v_stack_m138 == 0) goto loc_00AF0D2B;
    if ((uint32_t)((uint32_t)(Arg4)) == 0) goto loc_00AF0D2B;
    if ((((uint8_t)((uint32_t)(Arg4))) & (1)) != 0) goto loc_00AF0D2B;
    if (((uint32_t)((uint32_t)(Arg4))) > 0xFFFCULL) goto loc_00AF0D2B;
    Arg1 = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x5FA))) & (7));
    if (((uint8_t)(Arg1)) < 1) goto loc_00AF1240;
    result = (uint8_t)((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x5FA)) & (240));
    if (((uint8_t)(result)) == 48) goto loc_00AF1257;
loc_00AF1240:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E882E), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_m138, v_stack_mC8);
    if ((uint8_t)(result) == 0) goto loc_00AF1378;
loc_00AF1257:
    result = ExAllocatePool2(256, (uint32_t)(Arg4), (uint32_t)(0x20206553ULL), v_stack_mC8);
    v_stack_m118 = result;
    if (result != 0) goto loc_00AF1281;
    goto loc_00AF104A;
loc_00AF1281:
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AF12A2;
    if ((((uint8_t)(v_stack_m138)) & (1)) != 0) goto loc_00AF1EFD;
    if (((uint32_t)(Arg4) + v_stack_m138 * 1) > local_r13) goto loc_00AF129E;
    result = (uint32_t)(Arg4) + v_stack_m138 * 1;
    if (((uint32_t)(Arg4) + v_stack_m138 * 1) < v_stack_m138) {
        result = *(uint8_t *)(local_r13);
    }
    result = memcpy(result, v_stack_m138, (uint32_t)(Arg4), v_stack_mC8);
    v_stack_mB0 = result;
    v_stack_mB8 = (uint16_t)((uint32_t)(Arg4));
    v_stack_mB6 = (uint16_t)((uint32_t)(Arg4));
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_stack_m138 + 0x30), 1, (uint32_t)(Arg4), v_stack_mC8);
    result = SepAddAgentIdClaimToToken(v_stack_m138, v_stack_mB8, (uint32_t)(Arg4), v_stack_mC8);
    v_stack_m130 = (uint32_t)(result);
    if (sign_flag) goto loc_00AF1338;
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(v_rip - 0xADE617);
        result = Arg1;
        result = (result) + (Arg1);
        *(uint32_t *)(v_stack_m138 + 0x38) = (uint32_t)(result);
        result = (result) >> (32);
        *(uint32_t *)(v_stack_m138 + 0x3C) = (uint32_t)(result);
    }
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m138 + 0x30), v_stack_mB8, (uint32_t)(Arg4), v_stack_mC8);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m138 + 0x30), v_stack_mB8, (uint32_t)(Arg4), v_stack_mC8);
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)(Arg4), v_stack_mC8);
    goto loc_00AF1648;
loc_00AF1378:
    goto loc_00AF104A;
loc_00AF1382:
    goto loc_00AF0B0A;
loc_00AF138C:
    result = Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline(result, Arg2, (uint32_t)(Arg4), v_stack_mC8);
    if ((uint32_t)(result) == 0) goto loc_00AF1382;
    if (((uint32_t)((uint32_t)(Arg4))) != 4) goto loc_00AF0EA8;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AF13AE;
    result = RtlReadULongFromUser(v_stack_m138, Arg2, (uint32_t)(Arg4), v_stack_mC8);
    goto loc_00AF13B1;
loc_00AF13AE:
loc_00AF13B1:
    v_stack_m10C = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m138)));
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_stack_m138 + 0x30), 1, (uint32_t)(Arg4), v_stack_mC8);
    if (v_stack_m10C == ((uint32_t)((uint32_t)(v_stack_m130)))) goto loc_00AF13F0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m138 + 0x490))) | (1));
    goto loc_00AF13F3;
loc_00AF13F0:
    result = (uint32_t)((result) & (0xFFFFFFFEULL));
loc_00AF13F3:
    *(uint32_t *)(v_stack_m138 + 0x490) = (uint32_t)(result);
    goto loc_00AF0E51;
loc_00AF1411:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E865D), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint32_t)(Arg4), v_stack_mC8);
    if ((uint8_t)(result) == 0) goto loc_00AF0700;
    if (((uint32_t)((uint32_t)(Arg4))) != 4) goto loc_00AF0EA8;
    v_stack_mA4 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m138)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m138))) != 0) goto loc_00AF18CF;
    if (((*(uint32_t *)(result + 0xC8)) & (0x80000ULL)) == 0) goto loc_00AF18CF;
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_stack_m138 + 0x30), 1, (uint32_t)(Arg4), v_stack_mC8);
    result = (*(uint64_t *)(v_rip - 0xADE785)) + (*(uint64_t *)(v_rip - 0xADE785));
    *(uint32_t *)(v_stack_m138 + 0x38) = (uint32_t)(result);
    result = (result) >> (32);
    *(uint32_t *)(v_stack_m138 + 0x3C) = (uint32_t)(result);
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m138 + 0x30), v_stack_m138, (uint32_t)(Arg4), v_stack_mC8);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m138 + 0x30), v_stack_m138, (uint32_t)(Arg4), v_stack_mC8);
    goto loc_00AF18CF;
loc_00AF14D5:
    if (((uint32_t)((uint32_t)(Arg4))) != 4) goto loc_00AF0EA8;
    v_stack_mA0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m138)));
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E8585), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint32_t)(Arg4), v_stack_mC8);
    if ((uint8_t)(result) == 0) goto loc_00AF0700;
    result = SeSetPrivateNameSpaceToken(v_stack_m138, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m138)))), (uint32_t)(Arg4), v_stack_mC8);
    goto loc_00AF0714;
loc_00AF1522:
    v_stack_mF0 = (uint32_t)(v_stack_m130);
    if (v_stack_m138 == 0) goto loc_00AF0EA8;
    if (((uint32_t)((uint32_t)(Arg4))) < 16) goto loc_00AF0EA8;
    result = SepCaptureTokenSecurityAttributesAndOperationsInformation(v_stack_m138, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mF0, v_stack_mC8);
    if (!sign_flag) goto loc_00AF155F;
loc_00AF1557:
    goto loc_00AF0B0A;
loc_00AF155F:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E850F), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mF0, v_stack_mC8);
    local_r14 = (uint32_t)((uint32_t)(result));
    if ((uint8_t)(result) == 0) { local_r14 = (uint32_t)((uint32_t)(0xC0000061ULL)); }
    v_stack_m130 = (uint32_t)(local_r14);
    if (!sign_flag) goto loc_00AF1595;
    result = SepReleaseTokenSecurityAttributesAndOperationsInformation(v_stack_mF0, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), v_stack_mF0, v_stack_mC8);
    goto loc_00AF1557;
loc_00AF1595:
    result = SepShouldSetDelinkFlags(*(uint64_t *)(v_stack_mF0 + 0x8), *(uint64_t *)(v_stack_mF0), v_stack_mF0, v_stack_mC8);
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_stack_m138 + 0x30), 1, v_stack_mF0, v_stack_mC8);
    result = AuthzBasepSetSecurityAttributesToken(*(uint64_t *)(v_stack_m138 + 0x308), *(uint64_t *)(v_stack_mF0 + 0x8), *(uint64_t *)(v_stack_mF0), v_stack_mC8);
    v_stack_m130 = (uint32_t)(result);
    if (sign_flag) goto loc_00AF1606;
    if ((uint8_t)((uint8_t)(result)) != 0) {
    }
    result = (*(uint64_t *)(v_rip - 0xADE905)) + (*(uint64_t *)(v_rip - 0xADE905));
    *(uint32_t *)(v_stack_m138 + 0x38) = (uint32_t)(result);
    result = (result) >> (32);
    *(uint32_t *)(v_stack_m138 + 0x3C) = (uint32_t)(result);
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m138 + 0x30), *(uint64_t *)(v_stack_mF0 + 0x8), *(uint64_t *)(v_stack_mF0), v_stack_mC8);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m138 + 0x30), *(uint64_t *)(v_stack_mF0 + 0x8), *(uint64_t *)(v_stack_mF0), v_stack_mC8);
    result = SepReleaseTokenSecurityAttributesAndOperationsInformation(v_stack_mF0, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), *(uint64_t *)(v_stack_mF0), v_stack_mC8);
loc_00AF1648:
    goto loc_00AF104A;
loc_00AF1651:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(v_stack_mF0, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), *(uint64_t *)(v_stack_mF0), v_stack_mC8);
    if ((uint32_t)(result) == 0) goto loc_00AF1382;
    if (((uint32_t)((uint32_t)(Arg4))) != 4) goto loc_00AF0EA8;
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AF167E;
    result = RtlReadULongFromUser((uint8_t)(result), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), *(uint64_t *)(v_stack_mF0), v_stack_mC8);
    v_stack_mD4 = (uint32_t)(result);
    goto loc_00AF168D;
loc_00AF167E:
    v_stack_mD4 = (uint32_t)((uint32_t)(*(uint32_t *)((uint8_t)(result))));
loc_00AF168D:
    if ((uint32_t)((uint32_t)(*(uint32_t *)((uint8_t)(result)))) == 0) goto loc_00AF169B;
    goto loc_00AF0B0A;
loc_00AF169B:
    if (((*(uint32_t *)(v_stack_m138 + 0xC8)) & (0x4000ULL)) != 0) goto loc_00AF16B1;
    goto loc_00AF0B0A;
loc_00AF16B1:
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E83BD), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), *(uint64_t *)(v_stack_mF0), v_stack_mC8);
    if ((uint8_t)(result) == 0) goto loc_00AF0700;
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_stack_m138 + 0x30), 1, *(uint64_t *)(v_stack_mF0), v_stack_mC8);
    result = SepRemoveAceFromTokenDefaultDacl(v_stack_m138, *(uint64_t *)(v_stack_m138 + 0x310), *(uint64_t *)(v_stack_mF0), v_stack_mC8);
    if (*(uint64_t *)(v_stack_m138 + 0x310) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m138 + 0x310), Arg2, *(uint64_t *)(v_stack_mF0), v_stack_mC8);
        *(uint64_t *)(v_stack_m138 + 0x310) = (uint32_t)(v_stack_m130);
    }
    if (*(uint64_t *)(v_stack_m138 + 0x318) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m138 + 0x318), Arg2, *(uint64_t *)(v_stack_mF0), v_stack_mC8);
        *(uint64_t *)(v_stack_m138 + 0x318) = (uint32_t)(v_stack_m130);
        *(uint32_t *)(v_stack_m138 + 0x320) = (uint32_t)((uint32_t)(v_stack_m130));
        Arg1 = v_stack_m138 + 808;
        Arg2 = 0;
        Arg3 = 272;
        result = memset(Arg1, Arg2, Arg3, v_stack_mC8);
    }
    if (*(uint64_t *)(v_stack_m138 + 0x438) != 0) {
        Arg1 = *(uint32_t *)(v_stack_m138 + 0x78);
        result = SepDereferenceLowBoxNumberEntry(Arg1, *(uint64_t *)(v_stack_m138 + 0x438), Arg3, v_stack_mC8);
        *(uint64_t *)(v_stack_m138 + 0x438) = (uint32_t)(v_stack_m130);
    }
    if (*(uint64_t *)(v_stack_m138 + 0x440) != 0) {
        Arg1 = *(uint64_t *)(v_stack_m138 + 0xD8);
        Arg1 = (Arg1) + (96);
        Arg4 = 0;
        Arg2 = 0;
        result = SepDereferenceCachedHandlesEntryInternal(Arg1, Arg2, *(uint64_t *)(v_stack_m138 + 0x440), Arg4);
        *(uint64_t *)(v_stack_m138 + 0x440) = (uint32_t)(v_stack_m130);
    }
    goto loc_00AF0D96;
loc_00AF17BA:
    if (((uint32_t)((uint32_t)(Arg4))) != 4) goto loc_00AF0EA8;
    v_stack_mD0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m138)));
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E82A0), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), *(uint64_t *)(v_stack_m138 + 0x440), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00AF0700;
    if ((*(uint8_t *)(v_stack_m138 + 0xCC)) == ((uint8_t)((uint32_t)(v_stack_m130)))) goto loc_00AF17F8;
    goto loc_00AF0B0A;
loc_00AF17F8:
    result = SeSetMandatoryPolicyToken(v_stack_m138, v_stack_mD0, *(uint64_t *)(v_stack_m138 + 0x440), Arg4);
    goto loc_00AF0714;
loc_00AF1820:
    if (((uint32_t)((uint32_t)(Arg4))) != 4) goto loc_00AF0EA8;
    v_stack_mCC = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m138)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m138))) == 0) goto loc_00AF184F;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E8236), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), *(uint64_t *)(v_stack_m138 + 0x440), Arg4);
    if ((uint8_t)(result) == 0) goto loc_00AF0700;
loc_00AF184F:
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_stack_m138 + 0x30), 1, *(uint64_t *)(v_stack_m138 + 0x440), Arg4);
    if (v_stack_mCC == ((uint32_t)((uint32_t)(v_stack_m130)))) goto loc_00AF188E;
    goto loc_00AF1892;
loc_00AF188E:
loc_00AF1892:
    *(uint32_t *)(v_stack_m138 + 0xC8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m138 + 0xC8)));
    result = (*(uint64_t *)(v_rip - 0xADEB97)) + (*(uint64_t *)(v_rip - 0xADEB97));
    *(uint32_t *)(v_stack_m138 + 0x38) = (uint32_t)(result);
    result = (result) >> (32);
    *(uint32_t *)(v_stack_m138 + 0x3C) = (uint32_t)(result);
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m138 + 0x30), v_stack_m138, *(uint64_t *)(v_stack_m138 + 0x440), Arg4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m138 + 0x30), v_stack_m138, *(uint64_t *)(v_stack_m138 + 0x440), Arg4);
loc_00AF18CF:
    goto loc_00AF0B0A;
loc_00AF18E9:
    if (((uint32_t)((uint32_t)(Arg4))) < 16) goto loc_00AF0EA8;
    v_stack_m148 = v_stack_m9C;
    v_stack_m150 = v_stack_mC0;
    v_stack_m168 = (uint32_t)((uint32_t)(v_stack_m130));
    Arg4 = 0;
    result = SeCaptureSidAndAttributesArray(v_stack_m138, Arg4 + 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    v_stack_m130 = (uint32_t)(result);
    if (sign_flag) goto loc_00AF0714;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mC0) + 0x2))) - (*(uint32_t *)(*(uint64_t *)(v_rip + 0x413ED3) + 0x2)));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint16_t *)(*(uint64_t *)(v_stack_mC0) + 0x6);
        result = *(uint16_t *)(*(uint64_t *)(v_rip + 0x413ED3) + 0x6);
        Arg1 = (uint32_t)((Arg1) - ((uint32_t)(result)));
    }
    result = ((uint32_t)(Arg1) == 0) ? 1 : 0;
    if ((uint32_t)(result) != 0) goto loc_00AF197F;
loc_00AF1962:
    result = ObfDereferenceObject(v_stack_m138, *(uint64_t *)(v_rip + 0x413ED3), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    result = SeReleaseLuidAndAttributesArray(v_stack_mC0, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    goto loc_00AF1ED9;
loc_00AF197F:
    result = RtlSubAuthorityCountSid(*(uint64_t *)(v_stack_mC0), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    if ((uint8_t)(*(uint8_t *)(result)) != 0) goto loc_00AF1993;
    goto loc_00AF19AA;
loc_00AF1993:
    result = RtlSubAuthoritySid(*(uint64_t *)(v_stack_mC0), *(uint8_t *)(result) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result)))) > 0x4000ULL) goto loc_00AF1962;
loc_00AF19AA:
    v_stack_m88 = v_stack_m138;
    result = ExAcquireResourceExclusiveLite(*(uint64_t *)(v_stack_m138 + 0x30), 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    result = SepLocateTokenIntegrity(v_stack_m138, 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    if (result != 0) goto loc_00AF19F6;
    goto loc_00AF1E8B;
loc_00AF19F6:
    v_stack_m118 = *(uint64_t *)(result);
    result = RtlSubAuthorityCountSid(*(uint64_t *)(result), 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    v_stack_mE8 = (uint32_t)(*(uint8_t *)(result));
    if ((uint8_t)(*(uint8_t *)(result)) != 0) goto loc_00AF1A1A;
    goto loc_00AF1A30;
loc_00AF1A1A:
    result = RtlSubAuthoritySid(v_stack_m118, (uint32_t)((uint32_t)(*(uint8_t *)(result))) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
loc_00AF1A30:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(result))))) goto loc_00AF1A69;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x4E8039), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    if ((uint8_t)(result) != 0) goto loc_00AF1A52;
    goto loc_00AF1E8B;
loc_00AF1A52:
    if ((*(uint8_t *)((uint32_t)(0xC0000061ULL) + 0xCC)) == ((uint8_t)((uint32_t)(v_stack_m130)))) goto loc_00AF1BA8;
    goto loc_00AF1E8B;
loc_00AF1A69:
    if ((uint8_t)(result) != 0) goto loc_00AF1A71;
    goto loc_00AF1A80;
loc_00AF1A71:
    result = RtlSubAuthoritySid(v_stack_m118, (uint32_t)((uint32_t)(*(uint8_t *)(result))) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
loc_00AF1A80:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(result))))) goto loc_00AF1BA8;
    result = Feature_871661881__private_IsEnabledDeviceUsageNoInline(v_stack_m118, (uint32_t)((uint32_t)(*(uint8_t *)(result))) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    if ((uint32_t)(result) == 0) goto loc_00AF1BA0;
    v_stack_m108 = (uint32_t)((uint32_t)(v_stack_m130));
    result = RtlQueryElevationFlags(v_stack_m108, (uint32_t)((uint32_t)(*(uint8_t *)(result))) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    result = (uint8_t)(((uint32_t)(v_stack_m108)) & (24));
    if (((uint8_t)(result)) != 16) goto loc_00AF1BA0;
    result = RtlSubAuthorityCountSid(*(uint64_t *)(result), (uint32_t)((uint32_t)(*(uint8_t *)(result))) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    if ((uint8_t)(*(uint8_t *)(result)) == 0) goto loc_00AF1BA0;
    result = RtlSubAuthoritySid(*(uint64_t *)(result), *(uint8_t *)(result) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    if ((*(uint32_t *)(result)) < 0x3000ULL) goto loc_00AF1BA0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = SeCaptureSubjectContext(v_stack_m58, *(uint8_t *)(result) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m48 + 0x30), 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    result = SepLocateTokenIntegrity(v_stack_m48, 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    result = RtlSubAuthorityCountSid(*(uint64_t *)(result), 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    if ((uint8_t)(*(uint8_t *)(result)) != 0) goto loc_00AF1B4B;
    goto loc_00AF1B58;
loc_00AF1B4B:
    result = RtlSubAuthoritySid(*(uint64_t *)(result), *(uint8_t *)(result) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
loc_00AF1B58:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result)))) >= 0x3000ULL) goto loc_00AF1B84;
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m48 + 0x30), *(uint8_t *)(result) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m48 + 0x30), *(uint8_t *)(result) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    result = SeReleaseSubjectContext(v_stack_m58, *(uint8_t *)(result) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    goto loc_00AF1E8B;
loc_00AF1B84:
    result = ExReleaseResourceLite(v_stack_m58, *(uint8_t *)(result) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    result = KeLeaveCriticalRegion(v_stack_m58, *(uint8_t *)(result) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    result = SeReleaseSubjectContext(v_stack_m58, *(uint8_t *)(result) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
loc_00AF1BA0:
loc_00AF1BA8:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(v_stack_m58, *(uint8_t *)(result) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    if ((uint32_t)(result) == 0) goto loc_00AF1C3F;
    result = RtlSubAuthorityCountSid(*(uint64_t *)(result), *(uint8_t *)(result) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    if ((uint8_t)(*(uint8_t *)(result)) != 0) goto loc_00AF1BCC;
    goto loc_00AF1BD9;
loc_00AF1BCC:
    result = RtlSubAuthoritySid(*(uint64_t *)(result), *(uint8_t *)(result) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
loc_00AF1BD9:
    result = (uint32_t)(*(uint32_t *)(result));
    local_r13 = (uint8_t)((uint32_t)(v_stack_m130));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(result))))) {
        v_stack_m78 = v_xmm0;
        v_stack_m68 = v_xmm0;
        Arg1 = v_stack_m78;
        result = SeCaptureSubjectContext(Arg1, *(uint8_t *)(result) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
        Arg1 = v_stack_m78;
        result = SeLockSubjectContext(Arg1, *(uint8_t *)(result) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
        result = v_stack_m68;
        local_r13 = *(uint32_t *)(result + 0xC8);
        Arg1 = v_stack_m78;
        result = SeUnlockSubjectContext(Arg1, *(uint8_t *)(result) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
        Arg1 = v_stack_m78;
        result = SeReleaseSubjectContext(Arg1, *(uint8_t *)(result) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
        local_r13 = (uint32_t)((local_r13) >> (14));
        local_r13 = (uint8_t)(~(local_r13));
        local_r13 = (uint8_t)((local_r13) & (1));
    }
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(result) + 0x1)) == 0) goto loc_00AF1E86;
    result = RtlSubAuthoritySid(*(uint64_t *)(result), *(uint8_t *)(*(uint64_t *)(result) + 0x1) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    *(uint32_t *)(result) = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result)))) < 0x3000ULL) {
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result)))) >= ((uint32_t)((uint32_t)(0x2000ULL)))) goto loc_00AF1C9E;
    goto loc_00AF1E62;
loc_00AF1C9E:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline(*(uint64_t *)(result), *(uint8_t *)(*(uint64_t *)(result) + 0x1) - 1, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m138 + 0xC8))) & (0x4000ULL));
    if ((uint32_t)(result) == 0) goto loc_00AF1DAC;
    if ((uint32_t)(Arg1) == 0) goto loc_00AF1D70;
    if ((uint8_t)(local_r13) == 0) goto loc_00AF1D70;
    result = SepRemoveAceFromTokenDefaultDacl(v_stack_m138, *(uint64_t *)(v_stack_m138 + 0x310), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
    if (*(uint64_t *)(v_stack_m138 + 0x310) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m138 + 0x310), Arg2, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
        *(uint64_t *)(v_stack_m138 + 0x310) = (uint32_t)(v_stack_m130);
    }
    if (*(uint64_t *)(v_stack_m138 + 0x318) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m138 + 0x318), Arg2, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), Arg4);
        *(uint64_t *)(v_stack_m138 + 0x318) = (uint32_t)(v_stack_m130);
        *(uint32_t *)(v_stack_m138 + 0x320) = (uint32_t)((uint32_t)(v_stack_m130));
        Arg1 = v_stack_m138 + 808;
        Arg2 = 0;
        Arg3 = 272;
        result = memset(Arg1, Arg2, Arg3, Arg4);
    }
    if (*(uint64_t *)(v_stack_m138 + 0x438) != 0) {
        Arg1 = *(uint32_t *)(v_stack_m138 + 0x78);
        result = SepDereferenceLowBoxNumberEntry(Arg1, *(uint64_t *)(v_stack_m138 + 0x438), Arg3, Arg4);
        *(uint64_t *)(v_stack_m138 + 0x438) = (uint32_t)(v_stack_m130);
    }
    if (*(uint64_t *)(v_stack_m138 + 0x440) != 0) {
        Arg1 = *(uint64_t *)(v_stack_m138 + 0xD8);
        Arg1 = (Arg1) + (96);
        Arg4 = 0;
        Arg2 = 0;
        result = SepDereferenceCachedHandlesEntryInternal(Arg1, Arg2, *(uint64_t *)(v_stack_m138 + 0x440), Arg4);
        *(uint64_t *)(v_stack_m138 + 0x440) = (uint32_t)(v_stack_m130);
    }
    result = RtlSubAuthorityCountSid(*(uint64_t *)(result), Arg2, *(uint64_t *)(v_stack_m138 + 0x440), Arg4);
    if ((uint8_t)(*(uint8_t *)(result)) == 0) goto loc_00AF1E62;
    result = RtlSubAuthoritySid(*(uint64_t *)(result), *(uint8_t *)(result) - 1, *(uint64_t *)(v_stack_m138 + 0x440), Arg4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result)))) < ((uint32_t)((uint32_t)(0x2000ULL)))) goto loc_00AF1E62;
    goto loc_00AF1E62;
loc_00AF1DAC:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result))) == 0) goto loc_00AF1E5C;
    result = SepRemoveAceFromTokenDefaultDacl(v_stack_m138, *(uint64_t *)(v_stack_m138 + 0x310), *(uint64_t *)(v_stack_m138 + 0x440), Arg4);
    if (*(uint64_t *)(v_stack_m138 + 0x310) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m138 + 0x310), Arg2, *(uint64_t *)(v_stack_m138 + 0x440), Arg4);
        *(uint64_t *)(v_stack_m138 + 0x310) = (uint32_t)(v_stack_m130);
    }
    if (*(uint64_t *)(v_stack_m138 + 0x318) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(v_stack_m138 + 0x318), Arg2, *(uint64_t *)(v_stack_m138 + 0x440), Arg4);
        *(uint64_t *)(v_stack_m138 + 0x318) = (uint32_t)(v_stack_m130);
        *(uint32_t *)(v_stack_m138 + 0x320) = (uint32_t)((uint32_t)(v_stack_m130));
        Arg1 = v_stack_m138 + 808;
        Arg2 = 0;
        Arg3 = 272;
        result = memset(Arg1, Arg2, Arg3, Arg4);
    }
    if (*(uint64_t *)(v_stack_m138 + 0x438) != 0) {
        Arg1 = *(uint32_t *)(v_stack_m138 + 0x78);
        result = SepDereferenceLowBoxNumberEntry(Arg1, *(uint64_t *)(v_stack_m138 + 0x438), Arg3, Arg4);
        *(uint64_t *)(v_stack_m138 + 0x438) = (uint32_t)(v_stack_m130);
    }
    if (*(uint64_t *)(v_stack_m138 + 0x440) != 0) {
        Arg1 = *(uint64_t *)(v_stack_m138 + 0xD8);
        Arg1 = (Arg1) + (96);
        Arg4 = 0;
        Arg2 = 0;
        result = SepDereferenceCachedHandlesEntryInternal(Arg1, Arg2, *(uint64_t *)(v_stack_m138 + 0x440), Arg4);
        *(uint64_t *)(v_stack_m138 + 0x440) = (uint32_t)(v_stack_m130);
    }
loc_00AF1E62:
    result = (*(uint64_t *)(v_rip - 0xADF161)) + (*(uint64_t *)(v_rip - 0xADF161));
    *(uint32_t *)(v_stack_m138 + 0x38) = (uint32_t)(result);
    result = (result) >> (32);
    *(uint32_t *)(v_stack_m138 + 0x3C) = (uint32_t)(result);
    goto loc_00AF1E8B;
loc_00AF1E86:
loc_00AF1E8B:
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m88 + 0x30), Arg2, *(uint64_t *)(v_stack_m138 + 0x440), Arg4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m88 + 0x30), Arg2, *(uint64_t *)(v_stack_m138 + 0x440), Arg4);
    result = ObfDereferenceObject(v_stack_m138, Arg2, *(uint64_t *)(v_stack_m138 + 0x440), Arg4);
    result = SeReleaseLuidAndAttributesArray(v_stack_mC0, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), *(uint64_t *)(v_stack_m138 + 0x440), Arg4);
    goto loc_00AF0B12;
loc_00AF1ED4:
loc_00AF1ED9:
    return (uint32_t)(0xC0000003ULL);
loc_00AF1EF7:
    result = ExRaiseDatatypeMisalignment(v_stack_mC0, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), *(uint64_t *)(v_stack_m138 + 0x440), Arg4);
loc_00AF1EFD:
    result = ExRaiseDatatypeMisalignment(v_stack_mC0, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), *(uint64_t *)(v_stack_m138 + 0x440), Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0 + r12*1` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AF0530&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
