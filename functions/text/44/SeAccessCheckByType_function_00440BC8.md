# SeAccessCheckByType

- RVA: `0x00440BC8`–`0x0044279D` (길이 `7,125` bytes)
- VA: `0x0000000140440BC8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A5178`
- 디코드: `1,432`개 명령, `7,125/7,125` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **68**; 고유 호출 대상: **44**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00440F91` → [ProbeForWrite](../../page/8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00440FA7` → [ProbeForWrite](../../page/8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00440FF5` → [ProbeForWrite](../../page/8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x004410EA` → [SepReferenceTokenByHandle](../3E/SepReferenceTokenByHandle_function_003EDAD0.md) (function, `0x003EDAD0`)
- `0x00441173` → [SeCaptureObjectTypeList](../43/SeCaptureObjectTypeList_function_00434320.md) (function, `0x00434320`)
- `0x004411A7` → [SeCaptureSecurityDescriptor](../../page/92/SeCaptureSecurityDescriptor_function_00929F40.md) (function, `0x00929F40`)
- `0x00441277` → [SepTrustLevelCheck](../3E/SepTrustLevelCheck_function_003ED7E0.md) (function, `0x003ED7E0`)
- `0x004412CE` → [SepFilterCheck](../30/SepFilterCheck_function_00301B60.md) (function, `0x00301B60`)
- `0x0044131A` → [SepMandatoryIntegrityCheck](../25/SepMandatoryIntegrityCheck_function_0025F4E0.md) (function, `0x0025F4E0`)
- `0x00441346` → [SepMandatoryToDiscretionary](../41/SepMandatoryToDiscretionary_function_0041BF40.md) (function, `0x0041BF40`)
- `0x0044137F` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x004413B2` → [SepMandatoryAccessCheck](../60/SepMandatoryAccessCheck_function_00608480.md) (function, `0x00608480`)
- `0x00441422` → [SePrivilegePolicyCheck](../3D/SePrivilegePolicyCheck_function_003D1700.md) (function, `0x003D1700`)
- `0x00441590` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004415B1` → [memcpy](../6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x004415BC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004415D2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00441691` → [SeCaptureSid](../../page/92/SeCaptureSid_function_009276D4.md) (function, `0x009276D4`)
- `0x004416B8` → [SeCaptureSubjectContext](../../page/86/SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x004416DD` → [ExAcquireResourceSharedLite](../21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x004416ED` → [SepTokenIsOwner](../3E/SepTokenIsOwner_function_003E5D60.md) (function, `0x003E5D60`)
- `0x004417B1` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x004417B6` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x004417C3` → [SeReleaseSubjectContext](../../page/86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00441836` → [SepGetScopedPolicySid](../3A/SepGetScopedPolicySid_function_003A59AC.md) (function, `0x003A59AC`)
- `0x0044184B` → [SepRmReferenceFindCap](../3A/SepRmReferenceFindCap_function_003A58EC.md) (function, `0x003A58EC`)
- `0x004418C9` → [RtlpOwnerAcesPresent](../3F/RtlpOwnerAcesPresent_function_003FB2F0.md) (function, `0x003FB2F0`)
- `0x00441928` → [Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline](../4E/Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline_function_004EF788.md) (function, `0x004EF788`)
- `0x00441B6A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00441B83` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00441B88` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x00441B95` → [SeReleaseSubjectContext](../../page/86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00441C8B` → [SepAccessCheck](../3D/SepAccessCheck_function_003D0E54.md) (function, `0x003D0E54`)
- `0x00441CCE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00441D61` → [SepCopyObjectTypeList](../60/SepCopyObjectTypeList_function_00606CC0.md) (function, `0x00606CC0`)
- `0x00441DF2` → [AuthzBasepInitializeResourceClaimsFromSacl](../30/AuthzBasepInitializeResourceClaimsFromSacl_function_00302E84.md) (function, `0x00302E84`)
- `0x00441E9B` → [AuthzBasepEvaluateAceCondition](../2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (function, `0x002FEBD0`)
- `0x00441F61` → [AuthzBasepEvaluateAceCondition](../2F/AuthzBasepEvaluateAceCondition_function_002FEBD0.md) (function, `0x002FEBD0`)
- `0x00441FA4` → [SepBuildCapeSecurityDescriptor](../4D/SepBuildCapeSecurityDescriptor_function_004D9E38.md) (function, `0x004D9E38`)
- `0x0044209B` → [SepAccessCheck](../3D/SepAccessCheck_function_003D0E54.md) (function, `0x003D0E54`)
- `0x00442108` → [SepMergeObjectTypeListAccesses](../60/SepMergeObjectTypeListAccesses_function_00607508.md) (function, `0x00607508`)
- `0x0044216B` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00442170` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x0044217D` → [SeReleaseSubjectContext](../../page/86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x00442193` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00442198` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x004421A5` → [SeReleaseSubjectContext](../../page/86/SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x0044221C` → [SepConstrainByMandatory](../43/SepConstrainByMandatory_function_0043FC70.md) (function, `0x0043FC70`)
- `0x00442221` → [Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline](../5C/Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline_function_005CD968.md) (function, `0x005CD968`)
- `0x004423E4` → [SepConstrainByConstraintMask](../43/SepConstrainByConstraintMask_function_0043FDE0.md) (function, `0x0043FDE0`)
- `0x00442418` → [SepConstrainByConstraintMask](../43/SepConstrainByConstraintMask_function_0043FDE0.md) (function, `0x0043FDE0`)
- `0x004425FD` → [ExAcquireResourceSharedLite](../21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x00442655` → [SeLogAccessFailure](SeLogAccessFailure_function_00448550.md) (function, `0x00448550`)
- `0x0044265E` → [ExReleaseResourceLite](../25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x00442663` → [KeLeaveCriticalRegion](../25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x004426A0` → [SepLpacCausedAccessFailure](../46/SepLpacCausedAccessFailure_function_00462484.md) (function, `0x00462484`)
- `0x004426A9` → [SepLogLpacAccessFailure](../41/SepLogLpacAccessFailure_function_0041E8A0.md) (function, `0x0041E8A0`)
- `0x004426BD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004426D4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x004426E6` → [ObfDereferenceObjectWithTag](../2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x004426F8` → [SeFreeCapturedObjectTypeList](../60/SeFreeCapturedObjectTypeList_function_00606CA4.md) (function, `0x00606CA4`)
- `0x00442714` → [SeReleaseSid](../../page/A2/SeReleaseSid_function_00A2EF50.md) (function, `0x00A2EF50`)
- `0x00442733` → [SeReleaseSecurityDescriptor](../../page/97/SeReleaseSecurityDescriptor_function_00975190.md) (function, `0x00975190`)
- `0x0044274A` → [SepRmDereferenceCap](../4B/SepRmDereferenceCap_function_004B1E9C.md) (function, `0x004B1E9C`)
- `0x0044275E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0044276B` → [SepFreeResourceInfo](../30/SepFreeResourceInfo_function_003019F0.md) (function, `0x003019F0`)
- `0x0044277D` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00442796` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)

### Direct callers
- [NtAccessCheckByType](NtAccessCheckByType_function_00440AF0.md) at `0x00440B4F`
- [NtAccessCheck](NtAccessCheck_function_00440B60.md) at `0x00440BB5`
- [NtAccessCheckByTypeResultList](../60/NtAccessCheckByTypeResultList_function_00606C20.md) at `0x00606C7F`

### Static image references
- `0x00440BDB` → RVA `0x00E0A740` (`.data`; read)
- `0x004416FB` → RVA `0x00E0CCB0` (`.data`; read)
- `0x004417CD` → RVA `0x00F04AC5` (`.data`; read)
- `0x0044185A` → RVA `0x00FD80F0` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **21**
  - `0x00440F91` → [ProbeForWrite](../../page/8E/ProbeForWrite_function_008E91C0.md) (`.text` → `PAGE`)
  - `0x00440FA7` → [ProbeForWrite](../../page/8E/ProbeForWrite_function_008E91C0.md) (`.text` → `PAGE`)
  - `0x00440FF5` → [ProbeForWrite](../../page/8E/ProbeForWrite_function_008E91C0.md) (`.text` → `PAGE`)
  - `0x004411A7` → [SeCaptureSecurityDescriptor](../../page/92/SeCaptureSecurityDescriptor_function_00929F40.md) (`.text` → `PAGE`)
  - `0x00441590` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x004415BC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x004415D2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00441691` → [SeCaptureSid](../../page/92/SeCaptureSid_function_009276D4.md) (`.text` → `PAGE`)
  - `0x004416B8` → [SeCaptureSubjectContext](../../page/86/SeCaptureSubjectContext_function_0086B820.md) (`.text` → `PAGE`)
  - `0x004417C3` → [SeReleaseSubjectContext](../../page/86/SeReleaseSubjectContext_function_0086B710.md) (`.text` → `PAGE`)
  - `0x00441B6A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x00441B95` → [SeReleaseSubjectContext](../../page/86/SeReleaseSubjectContext_function_0086B710.md) (`.text` → `PAGE`)
  - `0x00441CCE` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
  - `0x0044217D` → [SeReleaseSubjectContext](../../page/86/SeReleaseSubjectContext_function_0086B710.md) (`.text` → `PAGE`)
  - `0x004421A5` → [SeReleaseSubjectContext](../../page/86/SeReleaseSubjectContext_function_0086B710.md) (`.text` → `PAGE`)
  - `0x004426BD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x004426D4` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00442714` → [SeReleaseSid](../../page/A2/SeReleaseSid_function_00A2EF50.md) (`.text` → `PAGE`)
  - `0x00442733` → [SeReleaseSecurityDescriptor](../../page/97/SeReleaseSecurityDescriptor_function_00975190.md) (`.text` → `PAGE`)
  - `0x0044275E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x00442796` → [ExRaiseDatatypeMisalignment](../../page/89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00440BC8  40 53                           push rbx
00440BCA  56                              push rsi
00440BCB  57                              push rdi
00440BCC  41 54                           push r12
00440BCE  41 55                           push r13
00440BD0  41 56                           push r14
00440BD2  41 57                           push r15
00440BD4  48 81 EC C0 02 00 00            sub rsp, 0x2c0
00440BDB  48 8B 05 5E 9B 9C 00            mov rax, qword ptr [rip + 0x9c9b5e]
00440BE2  48 33 C4                        xor rax, rsp
00440BE5  48 89 84 24 B8 02 00 00         mov qword ptr [rsp + 0x2b8], rax
00440BED  4D 8B E8                        mov r13, r8
00440BF0  48 8B C2                        mov rax, rdx
00440BF3  48 89 94 24 B8 01 00 00         mov qword ptr [rsp + 0x1b8], rdx
00440BFB  44 8B 84 24 28 03 00 00         mov r8d, dword ptr [rsp + 0x328]
00440C03  44 89 84 24 38 01 00 00         mov dword ptr [rsp + 0x138], r8d
00440C0B  4C 8B 9C 24 30 03 00 00         mov r11, qword ptr [rsp + 0x330]
00440C13  4C 89 9C 24 78 01 00 00         mov qword ptr [rsp + 0x178], r11
00440C1B  4C 89 9C 24 48 02 00 00         mov qword ptr [rsp + 0x248], r11
00440C23  48 8B 94 24 48 03 00 00         mov rdx, qword ptr [rsp + 0x348]
00440C2B  48 89 94 24 40 02 00 00         mov qword ptr [rsp + 0x240], rdx
00440C33  4C 8B 94 24 50 03 00 00         mov r10, qword ptr [rsp + 0x350]
00440C3B  4C 89 94 24 38 02 00 00         mov qword ptr [rsp + 0x238], r10
00440C43  4C 8B A4 24 40 03 00 00         mov r12, qword ptr [rsp + 0x340]
00440C4B  4C 89 A4 24 30 02 00 00         mov qword ptr [rsp + 0x230], r12
00440C53  48 89 8C 24 58 02 00 00         mov qword ptr [rsp + 0x258], rcx
00440C5B  48 89 84 24 F8 01 00 00         mov qword ptr [rsp + 0x1f8], rax
00440C63  4C 89 AC 24 00 02 00 00         mov qword ptr [rsp + 0x200], r13
00440C6B  44 89 8C 24 B0 00 00 00         mov dword ptr [rsp + 0xb0], r9d
00440C73  48 8B 84 24 20 03 00 00         mov rax, qword ptr [rsp + 0x320]
00440C7B  48 89 84 24 50 02 00 00         mov qword ptr [rsp + 0x250], rax
00440C83  44 89 84 24 C0 00 00 00         mov dword ptr [rsp + 0xc0], r8d
00440C8B  44 89 84 24 5C 01 00 00         mov dword ptr [rsp + 0x15c], r8d
00440C93  4D 8B F3                        mov r14, r11
00440C96  4C 89 9C 24 28 02 00 00         mov qword ptr [rsp + 0x228], r11
00440C9E  48 8B 9C 24 38 03 00 00         mov rbx, qword ptr [rsp + 0x338]
00440CA6  48 89 9C 24 48 01 00 00         mov qword ptr [rsp + 0x148], rbx
00440CAE  49 8B CC                        mov rcx, r12
00440CB1  48 89 8C 24 B0 01 00 00         mov qword ptr [rsp + 0x1b0], rcx
00440CB9  4C 8B CA                        mov r9, rdx
00440CBC  48 89 94 24 08 01 00 00         mov qword ptr [rsp + 0x108], rdx
00440CC4  48 89 94 24 08 02 00 00         mov qword ptr [rsp + 0x208], rdx
00440CCC  4D 8B DA                        mov r11, r10
00440CCF  4C 89 94 24 18 01 00 00         mov qword ptr [rsp + 0x118], r10
00440CD7  4C 89 94 24 10 02 00 00         mov qword ptr [rsp + 0x210], r10
00440CDF  33 FF                           xor edi, edi
00440CE1  89 BC 24 58 01 00 00            mov dword ptr [rsp + 0x158], edi
00440CE8  48 89 BC 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rdi
00440CF0  89 BC 24 A8 01 00 00            mov dword ptr [rsp + 0x1a8], edi
00440CF7  89 BC 24 A4 01 00 00            mov dword ptr [rsp + 0x1a4], edi
00440CFE  48 89 BC 24 68 01 00 00         mov qword ptr [rsp + 0x168], rdi
00440D06  89 BC 24 A0 01 00 00            mov dword ptr [rsp + 0x1a0], edi
00440D0D  8B C7                           mov eax, edi
00440D0F  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
00440D17  89 BC 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], edi
00440D1E  48 89 BC 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rdi
00440D26  48 89 BC 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rdi
00440D2E  48 89 BC 24 88 01 00 00         mov qword ptr [rsp + 0x188], rdi
00440D36  89 BC 24 F0 00 00 00            mov dword ptr [rsp + 0xf0], edi
00440D3D  44 8B C7                        mov r8d, edi
00440D40  89 BC 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], edi
00440D47  0F 57 C0                        xorps xmm0, xmm0
00440D4A  0F 11 84 24 A8 02 00 00         movups xmmword ptr [rsp + 0x2a8], xmm0
00440D52  48 89 BC 24 80 01 00 00         mov qword ptr [rsp + 0x180], rdi
00440D5A  48 89 BC 24 30 01 00 00         mov qword ptr [rsp + 0x130], rdi
00440D62  0F 11 84 24 C8 01 00 00         movups xmmword ptr [rsp + 0x1c8], xmm0
00440D6A  0F 11 84 24 D8 01 00 00         movups xmmword ptr [rsp + 0x1d8], xmm0
00440D72  0F 11 84 24 18 02 00 00         movups xmmword ptr [rsp + 0x218], xmm0
00440D7A  89 BC 24 00 01 00 00            mov dword ptr [rsp + 0x100], edi
00440D81  44 88 84 24 EC 00 00 00         mov byte ptr [rsp + 0xec], r8b
00440D89  48 89 BC 24 50 01 00 00         mov qword ptr [rsp + 0x150], rdi
00440D91  0F 11 84 24 88 02 00 00         movups xmmword ptr [rsp + 0x288], xmm0
00440D99  48 89 84 24 98 02 00 00         mov qword ptr [rsp + 0x298], rax
00440DA1  89 84 24 A0 02 00 00            mov dword ptr [rsp + 0x2a0], eax
00440DA8  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
00440DB0  0F 11 84 24 60 02 00 00         movups xmmword ptr [rsp + 0x260], xmm0
00440DB8  0F 11 84 24 70 02 00 00         movups xmmword ptr [rsp + 0x270], xmm0
00440DC0  48 89 84 24 80 02 00 00         mov qword ptr [rsp + 0x280], rax
00440DC8  48 89 BC 24 70 01 00 00         mov qword ptr [rsp + 0x170], rdi
00440DD0  40 88 BC 24 B8 00 00 00         mov byte ptr [rsp + 0xb8], dil
00440DD8  88 84 24 A9 00 00 00            mov byte ptr [rsp + 0xa9], al
00440DDF  89 BC 24 28 01 00 00            mov dword ptr [rsp + 0x128], edi
00440DE6  44 8A C7                        mov r8b, dil
00440DE9  40 88 BC 24 A0 00 00 00         mov byte ptr [rsp + 0xa0], dil
00440DF1  48 89 BC 24 98 01 00 00         mov qword ptr [rsp + 0x198], rdi
00440DF9  40 88 BC 24 CE 00 00 00         mov byte ptr [rsp + 0xce], dil
00440E01  40 88 BC 24 CC 00 00 00         mov byte ptr [rsp + 0xcc], dil
00440E09  40 88 BC 24 CD 00 00 00         mov byte ptr [rsp + 0xcd], dil
00440E11  48 89 BC 24 C0 01 00 00         mov qword ptr [rsp + 0x1c0], rdi
00440E19  48 89 BC 24 90 01 00 00         mov qword ptr [rsp + 0x190], rdi
00440E21  C7 84 24 C8 00 00 00 22 00 00 C0  mov dword ptr [rsp + 0xc8], 0xc0000022
00440E2C  89 BC 24 10 01 00 00            mov dword ptr [rsp + 0x110], edi
00440E33  89 BC 24 60 01 00 00            mov dword ptr [rsp + 0x160], edi
00440E3A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00440E43  44 8A B8 32 02 00 00            mov r15b, byte ptr [rax + 0x232]
00440E4A  44 88 BC 24 A8 00 00 00         mov byte ptr [rsp + 0xa8], r15b
00440E52  48 BE 00 00 FF FF FF 7F 00 00   movabs rsi, 0x7fffffff0000
00440E5C  45 84 FF                        test r15b, r15b
00440E5F  75 06                           jne 0x140440e67
00440E61  41 8B 04 24                     mov eax, dword ptr [r12]
00440E65  EB 0D                           jmp 0x140440e74
00440E67  48 8B C6                        mov rax, rsi
00440E6A  48 3B CE                        cmp rcx, rsi
00440E6D  49 0F 42 C4                     cmovb rax, r12
00440E71  90                              nop
00440E72  8B 00                           mov eax, dword ptr [rax]
00440E74  89 84 24 10 01 00 00            mov dword ptr [rsp + 0x110], eax
00440E7B  8B 84 24 A4 00 00 00            mov eax, dword ptr [rsp + 0xa4]
00440E82  4C 8B BC 24 78 01 00 00         mov r15, qword ptr [rsp + 0x178]
00440E8A  E9 91 00 00 00                  jmp 0x140440f20
00440E8F  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
00440E96  33 FF                           xor edi, edi
00440E98  48 BE 00 00 FF FF FF 7F 00 00   movabs rsi, 0x7fffffff0000
00440EA2  8B CF                           mov ecx, edi
00440EA4  48 89 8C 24 20 01 00 00         mov qword ptr [rsp + 0x120], rcx
00440EAC  89 8C 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], ecx
00440EB3  44 8A 84 24 EC 00 00 00         mov r8b, byte ptr [rsp + 0xec]
00440EBB  44 89 84 24 00 01 00 00         mov dword ptr [rsp + 0x100], r8d
00440EC3  48 89 8C 24 40 01 00 00         mov qword ptr [rsp + 0x140], rcx
00440ECB  88 8C 24 A9 00 00 00            mov byte ptr [rsp + 0xa9], cl
00440ED2  48 8B 8C 24 F8 01 00 00         mov rcx, qword ptr [rsp + 0x1f8]
00440EDA  48 89 8C 24 B8 01 00 00         mov qword ptr [rsp + 0x1b8], rcx
00440EE2  4C 8B AC 24 00 02 00 00         mov r13, qword ptr [rsp + 0x200]
00440EEA  4C 8B B4 24 28 02 00 00         mov r14, qword ptr [rsp + 0x228]
00440EF2  48 8B 9C 24 48 01 00 00         mov rbx, qword ptr [rsp + 0x148]
00440EFA  4C 8B A4 24 30 02 00 00         mov r12, qword ptr [rsp + 0x230]
00440F02  4C 8B 94 24 38 02 00 00         mov r10, qword ptr [rsp + 0x238]
00440F0A  48 8B 94 24 40 02 00 00         mov rdx, qword ptr [rsp + 0x240]
00440F12  4C 8B BC 24 48 02 00 00         mov r15, qword ptr [rsp + 0x248]
00440F1A  4C 8B CA                        mov r9, rdx
00440F1D  4D 8B DA                        mov r11, r10
00440F20  85 C0                           test eax, eax
00440F22  0F 88 4A 18 00 00               js 0x140442772
00440F28  83 C8 FF                        or eax, 0xffffffff
00440F2B  89 84 24 78 01 00 00            mov dword ptr [rsp + 0x178], eax
00440F32  89 84 24 90 01 00 00            mov dword ptr [rsp + 0x190], eax
00440F39  40 38 BC 24 A8 00 00 00         cmp byte ptr [rsp + 0xa8], dil
00440F41  75 14                           jne 0x140440f57
00440F43  41 89 3B                        mov dword ptr [r11], edi
00440F46  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
00440F4D  41 89 01                        mov dword ptr [r9], eax
00440F50  33 C0                           xor eax, eax
00440F52  E9 1B 18 00 00                  jmp 0x140442772
00440F57  40 38 BC 24 58 03 00 00         cmp byte ptr [rsp + 0x358], dil
00440F5F  74 55                           je 0x140440fb6
00440F61  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
00440F68  85 C0                           test eax, eax
00440F6A  75 11                           jne 0x140440f7d
00440F6C  B8 0D 00 00 C0                  mov eax, 0xc000000d
00440F71  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
00440F78  E9 B6 00 00 00                  jmp 0x140441033
00440F7D  48 8D 1C 85 00 00 00 00         lea rbx, [rax*4]
00440F85  41 B8 04 00 00 00               mov r8d, 4
00440F8B  48 8B D3                        mov rdx, rbx
00440F8E  49 8B CB                        mov rcx, r11
00440F91  E8 2A 82 4A 00                  call 0x1408e91c0
00440F96  41 B8 04 00 00 00               mov r8d, 4
00440F9C  48 8B D3                        mov rdx, rbx
00440F9F  48 8B 8C 24 08 01 00 00         mov rcx, qword ptr [rsp + 0x108]
00440FA7  E8 14 82 4A 00                  call 0x1408e91c0
00440FAC  48 8B 9C 24 48 01 00 00         mov rbx, qword ptr [rsp + 0x148]
00440FB4  EB 1C                           jmp 0x140440fd2
00440FB6  48 8B CE                        mov rcx, rsi
00440FB9  4C 3B DE                        cmp r11, rsi
00440FBC  49 0F 42 CA                     cmovb rcx, r10
00440FC0  8B 01                           mov eax, dword ptr [rcx]
00440FC2  89 01                           mov dword ptr [rcx], eax
00440FC4  48 8B CE                        mov rcx, rsi
00440FC7  4C 3B CE                        cmp r9, rsi
00440FCA  48 0F 42 CA                     cmovb rcx, rdx
00440FCE  8B 01                           mov eax, dword ptr [rcx]
00440FD0  89 01                           mov dword ptr [rcx], eax
00440FD2  48 8B CE                        mov rcx, rsi
00440FD5  48 39 B4 24 B0 01 00 00         cmp qword ptr [rsp + 0x1b0], rsi
00440FDD  49 0F 42 CC                     cmovb rcx, r12
00440FE1  8B 01                           mov eax, dword ptr [rcx]
00440FE3  89 01                           mov dword ptr [rcx], eax
00440FE5  8B 94 24 10 01 00 00            mov edx, dword ptr [rsp + 0x110]
00440FEC  41 B8 04 00 00 00               mov r8d, 4
00440FF2  48 8B CB                        mov rcx, rbx
00440FF5  E8 C6 81 4A 00                  call 0x1408e91c0
00440FFA  48 85 DB                        test rbx, rbx
00440FFD  74 0C                           je 0x14044100b
00440FFF  83 BC 24 10 01 00 00 14         cmp dword ptr [rsp + 0x110], 0x14
00441007  72 02                           jb 0x14044100b
00441009  89 3B                           mov dword ptr [rbx], edi
0044100B  41 F6 C6 03                     test r14b, 3
0044100F  0F 85 81 17 00 00               jne 0x140442796
00441015  4C 3B F6                        cmp r14, rsi
00441018  49 0F 42 F7                     cmovb rsi, r15
0044101C  90                              nop
0044101D  8A 06                           mov al, byte ptr [rsi]
0044101F  41 0F 10 06                     movups xmm0, xmmword ptr [r14]
00441023  F3 0F 7F 84 24 A8 02 00 00      movdqu xmmword ptr [rsp + 0x2a8], xmm0
0044102C  8B 84 24 A4 00 00 00            mov eax, dword ptr [rsp + 0xa4]
00441033  EB 51                           jmp 0x140441086
00441035  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
0044103C  33 FF                           xor edi, edi
0044103E  8B CF                           mov ecx, edi
00441040  48 89 8C 24 20 01 00 00         mov qword ptr [rsp + 0x120], rcx
00441048  89 8C 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], ecx
0044104F  44 8A 84 24 EC 00 00 00         mov r8b, byte ptr [rsp + 0xec]
00441057  44 89 84 24 00 01 00 00         mov dword ptr [rsp + 0x100], r8d
0044105F  48 89 8C 24 40 01 00 00         mov qword ptr [rsp + 0x140], rcx
00441067  88 8C 24 A9 00 00 00            mov byte ptr [rsp + 0xa9], cl
0044106E  48 8B 8C 24 F8 01 00 00         mov rcx, qword ptr [rsp + 0x1f8]
00441076  48 89 8C 24 B8 01 00 00         mov qword ptr [rsp + 0x1b8], rcx
0044107E  4C 8B AC 24 00 02 00 00         mov r13, qword ptr [rsp + 0x200]
00441086  85 C0                           test eax, eax
00441088  0F 88 E4 16 00 00               js 0x140442772
0044108E  F7 84 24 B0 00 00 00 00 00 00 F0  test dword ptr [rsp + 0xb0], 0xf0000000
00441099  74 18                           je 0x1404410b3
0044109B  BB E6 00 00 C0                  mov ebx, 0xc00000e6
004410A0  41 BE 01 00 00 00               mov r14d, 1
004410A6  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
004410AE  E9 AC 14 00 00                  jmp 0x14044255f
004410B3  48 8D 84 24 C0 01 00 00         lea rax, [rsp + 0x1c0]
004410BB  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
004410C0  48 8D 84 24 CE 00 00 00         lea rax, [rsp + 0xce]
004410C8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
004410CD  48 8D 84 24 E0 00 00 00         lea rax, [rsp + 0xe0]
004410D5  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004410DA  44 8A 84 24 A8 00 00 00         mov r8b, byte ptr [rsp + 0xa8]
004410E2  BA 08 00 00 00                  mov edx, 8
004410E7  49 8B CD                        mov rcx, r13
004410EA  E8 E1 C9 FA FF                  call 0x1403edad0
004410EF  8B D8                           mov ebx, eax
004410F1  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
004410F8  41 BE 01 00 00 00               mov r14d, 1
004410FE  85 C0                           test eax, eax
00441100  79 10                           jns 0x140441112
00441102  48 8B F7                        mov rsi, rdi
00441105  48 89 BC 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rdi
0044110D  E9 54 14 00 00                  jmp 0x140442566
00441112  49 8D 45 06                     lea rax, [r13 + 6]
00441116  8B CF                           mov ecx, edi
00441118  48 83 F8 02                     cmp rax, 2
0044111C  0F 96 C1                        setbe cl
0044111F  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
00441127  85 C9                           test ecx, ecx
00441129  75 26                           jne 0x140441151
0044112B  83 BE C0 00 00 00 02            cmp dword ptr [rsi + 0xc0], 2
00441132  74 0A                           je 0x14044113e
00441134  BB 5C 00 00 C0                  mov ebx, 0xc000005c
00441139  E9 21 14 00 00                  jmp 0x14044255f
0044113E  44 39 B6 C4 00 00 00            cmp dword ptr [rsi + 0xc4], r14d
00441145  7D 0A                           jge 0x140441151
00441147  BB A5 00 00 C0                  mov ebx, 0xc00000a5
0044114C  E9 0E 14 00 00                  jmp 0x14044255f
00441151  4C 8D 8C 24 80 01 00 00         lea r9, [rsp + 0x180]
00441159  44 8A BC 24 A8 00 00 00         mov r15b, byte ptr [rsp + 0xa8]
00441161  45 8A C7                        mov r8b, r15b
00441164  8B 94 24 C0 00 00 00            mov edx, dword ptr [rsp + 0xc0]
0044116B  48 8B 8C 24 50 02 00 00         mov rcx, qword ptr [rsp + 0x250]
00441173  E8 A8 31 FF FF                  call 0x140434320
00441178  8B D8                           mov ebx, eax
0044117A  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
00441181  85 C0                           test eax, eax
00441183  0F 88 DD 13 00 00               js 0x140442566
00441189  48 8D 84 24 F8 00 00 00         lea rax, [rsp + 0xf8]
00441191  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00441196  45 33 C9                        xor r9d, r9d
00441199  45 8B C6                        mov r8d, r14d
0044119C  41 8A D7                        mov dl, r15b
0044119F  48 8B 8C 24 58 02 00 00         mov rcx, qword ptr [rsp + 0x258]
004411A7  E8 94 8D 4E 00                  call 0x140929f40
004411AC  8B D8                           mov ebx, eax
004411AE  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
004411B5  85 C0                           test eax, eax
004411B7  0F 88 A9 13 00 00               js 0x140442566
004411BD  48 39 BC 24 F8 00 00 00         cmp qword ptr [rsp + 0xf8], rdi
004411C5  0F 84 8F 13 00 00               je 0x14044255a
004411CB  4C 8B BC 24 F8 00 00 00         mov r15, qword ptr [rsp + 0xf8]
004411D3  41 0F B7 4F 02                  movzx ecx, word ptr [r15 + 2]
004411D8  66 85 C9                        test cx, cx
004411DB  79 11                           jns 0x1404411ee
004411DD  41 8B 47 04                     mov eax, dword ptr [r15 + 4]
004411E1  85 C0                           test eax, eax
004411E3  0F 84 71 13 00 00               je 0x14044255a
004411E9  49 03 C7                        add rax, r15
004411EC  EB 0C                           jmp 0x1404411fa
004411EE  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
004411F6  48 8B 40 08                     mov rax, qword ptr [rax + 8]
004411FA  48 85 C0                        test rax, rax
004411FD  0F 84 57 13 00 00               je 0x14044255a
00441203  66 85 C9                        test cx, cx
00441206  79 19                           jns 0x140441221
00441208  4C 8B BC 24 F8 00 00 00         mov r15, qword ptr [rsp + 0xf8]
00441210  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
00441214  85 C0                           test eax, eax
00441216  0F 84 3E 13 00 00               je 0x14044255a
0044121C  49 03 C7                        add rax, r15
0044121F  EB 0C                           jmp 0x14044122d
00441221  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
00441229  48 8B 40 10                     mov rax, qword ptr [rax + 0x10]
0044122D  48 85 C0                        test rax, rax
00441230  0F 84 24 13 00 00               je 0x14044255a
00441236  40 38 BC 24 CE 00 00 00         cmp byte ptr [rsp + 0xce], dil
0044123E  48 8B 84 24 C0 01 00 00         mov rax, qword ptr [rsp + 0x1c0]
00441246  75 07                           jne 0x14044124f
00441248  48 8B 86 50 04 00 00            mov rax, qword ptr [rsi + 0x450]
0044124F  48 8D 8C 24 78 01 00 00         lea rcx, [rsp + 0x178]
00441257  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0044125C  44 88 74 24 28                  mov byte ptr [rsp + 0x28], r14b
00441261  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00441266  4C 8B CE                        mov r9, rsi
00441269  45 33 C0                        xor r8d, r8d
0044126C  4C 8B BC 24 F8 00 00 00         mov r15, qword ptr [rsp + 0xf8]
00441274  49 8B D7                        mov rdx, r15
00441277  E8 64 C5 FA FF                  call 0x1403ed7e0
0044127C  8B D8                           mov ebx, eax
0044127E  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
00441285  85 C0                           test eax, eax
00441287  0F 88 D9 12 00 00               js 0x140442566
0044128D  44 8B A4 24 B0 00 00 00         mov r12d, dword ptr [rsp + 0xb0]
00441295  45 8B EC                        mov r13d, r12d
00441298  41 0F BA F5 19                  btr r13d, 0x19
0044129D  41 8B C5                        mov eax, r13d
004412A0  23 84 24 78 01 00 00            and eax, dword ptr [rsp + 0x178]
004412A7  41 3B C5                        cmp eax, r13d
004412AA  0F 85 A8 01 00 00               jne 0x140441458
004412B0  48 8D 84 24 90 01 00 00         lea rax, [rsp + 0x190]
004412B8  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
004412BD  45 8A CE                        mov r9b, r14b
004412C0  4C 8B C6                        mov r8, rsi
004412C3  48 8D 94 24 50 01 00 00         lea rdx, [rsp + 0x150]
004412CB  49 8B CF                        mov rcx, r15
004412CE  E8 8D 08 EC FF                  call 0x140301b60
004412D3  8B D8                           mov ebx, eax
004412D5  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
004412DC  85 C0                           test eax, eax
004412DE  0F 88 82 12 00 00               js 0x140442566
004412E4  41 8B C5                        mov eax, r13d
004412E7  23 84 24 90 01 00 00            and eax, dword ptr [rsp + 0x190]
004412EE  41 3B C5                        cmp eax, r13d
004412F1  0F 85 57 01 00 00               jne 0x14044144e
004412F7  48 8D 84 24 18 02 00 00         lea rax, [rsp + 0x218]
004412FF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00441304  44 88 74 24 20                  mov byte ptr [rsp + 0x20], r14b
00441309  4C 8B CE                        mov r9, rsi
0044130C  45 33 C0                        xor r8d, r8d
0044130F  49 8B D7                        mov rdx, r15
00441312  48 8D 8C 24 A8 02 00 00         lea rcx, [rsp + 0x2a8]
0044131A  E8 C1 E1 E1 FF                  call 0x14025f4e0
0044131F  8B D8                           mov ebx, eax
00441321  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
00441328  85 C0                           test eax, eax
0044132A  0F 88 36 12 00 00               js 0x140442566
00441330  44 8A FF                        mov r15b, dil
00441333  44 89 BC 24 00 01 00 00         mov dword ptr [rsp + 0x100], r15d
0044133B  41 8B D4                        mov edx, r12d
0044133E  48 8D 8C 24 18 02 00 00         lea rcx, [rsp + 0x218]
00441346  E8 F5 AB FD FF                  call 0x14041bf40
0044134B  8B D8                           mov ebx, eax
0044134D  85 C0                           test eax, eax
0044134F  78 07                           js 0x140441358
00441351  41 0F BA E4 19                  bt r12d, 0x19
00441356  73 27                           jae 0x14044137f
00441358  F7 86 C8 00 00 00 00 40 00 00   test dword ptr [rsi + 0xc8], 0x4000
00441362  74 1B                           je 0x14044137f
00441364  45 0F B6 FF                     movzx r15d, r15b
00441368  81 BC 24 24 02 00 00 00 20 00 00  cmp dword ptr [rsp + 0x224], 0x2000
00441373  45 0F 46 FE                     cmovbe r15d, r14d
00441377  44 89 BC 24 00 01 00 00         mov dword ptr [rsp + 0x100], r15d
0044137F  E8 E4 C5 18 00                  call 0x1405cd968
00441384  85 C0                           test eax, eax
00441386  74 63                           je 0x1404413eb
00441388  48 8D 84 24 60 01 00 00         lea rax, [rsp + 0x160]
00441390  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00441395  44 8B A4 24 B0 00 00 00         mov r12d, dword ptr [rsp + 0xb0]
0044139D  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
004413A2  45 8A CE                        mov r9b, r14b
004413A5  4C 8B C6                        mov r8, rsi
004413A8  33 D2                           xor edx, edx
004413AA  48 8B 8C 24 F8 00 00 00         mov rcx, qword ptr [rsp + 0xf8]
004413B2  E8 C9 70 1C 00                  call 0x140608480
004413B7  85 C0                           test eax, eax
004413B9  78 11                           js 0x1404413cc
004413BB  44 23 A4 24 60 01 00 00         and r12d, dword ptr [rsp + 0x160]
004413C3  41 F7 C4 FF FF FF FD            test r12d, 0xfdffffff
004413CA  74 1F                           je 0x1404413eb
004413CC  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
004413D4  89 38                           mov dword ptr [rax], edi
004413D6  BB C0 01 00 C0                  mov ebx, 0xc00001c0
004413DB  4C 8B 8C 24 18 01 00 00         mov r9, qword ptr [rsp + 0x118]
004413E3  41 89 19                        mov dword ptr [r9], ebx
004413E6  E9 74 11 00 00                  jmp 0x14044255f
004413EB  85 DB                           test ebx, ebx
004413ED  79 05                           jns 0x1404413f4
004413EF  45 84 FF                        test r15b, r15b
004413F2  74 52                           je 0x140441446
004413F4  8A 84 24 A8 00 00 00            mov al, byte ptr [rsp + 0xa8]
004413FB  88 44 24 28                     mov byte ptr [rsp + 0x28], al
004413FF  48 8D 84 24 30 01 00 00         lea rax, [rsp + 0x130]
00441407  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0044140C  4C 8B CE                        mov r9, rsi
0044140F  45 33 C0                        xor r8d, r8d
00441412  48 8D 94 24 F0 00 00 00         lea rdx, [rsp + 0xf0]
0044141A  48 8D 8C 24 B0 00 00 00         lea rcx, [rsp + 0xb0]
00441422  E8 D9 02 F9 FF                  call 0x1403d1700
00441427  8B D8                           mov ebx, eax
00441429  39 BC 24 B0 00 00 00            cmp dword ptr [rsp + 0xb0], edi
00441430  75 14                           jne 0x140441446
00441432  39 BC 24 F0 00 00 00            cmp dword ptr [rsp + 0xf0], edi
00441439  74 0B                           je 0x140441446
0044143B  45 8A EE                        mov r13b, r14b
0044143E  41 BC 22 00 00 C0               mov r12d, 0xc0000022
00441444  EB 33                           jmp 0x140441479
00441446  41 BC 22 00 00 C0               mov r12d, 0xc0000022
0044144C  EB 23                           jmp 0x140441471
0044144E  44 88 B4 24 CD 00 00 00         mov byte ptr [rsp + 0xcd], r14b
00441456  EB 08                           jmp 0x140441460
00441458  44 88 B4 24 CC 00 00 00         mov byte ptr [rsp + 0xcc], r14b
00441460  41 BC 22 00 00 C0               mov r12d, 0xc0000022
00441466  44 8B BC 24 00 01 00 00         mov r15d, dword ptr [rsp + 0x100]
0044146E  41 8B DC                        mov ebx, r12d
00441471  44 8A AC 24 A0 00 00 00         mov r13b, byte ptr [rsp + 0xa0]
00441479  85 DB                           test ebx, ebx
0044147B  0F 89 97 00 00 00               jns 0x140441518
00441481  45 84 FF                        test r15b, r15b
00441484  0F 85 8E 00 00 00               jne 0x140441518
0044148A  44 8A BC 24 58 03 00 00         mov r15b, byte ptr [rsp + 0x358]
00441492  4C 8B 8C 24 18 01 00 00         mov r9, qword ptr [rsp + 0x118]
0044149A  45 84 FF                        test r15b, r15b
0044149D  74 28                           je 0x1404414c7
0044149F  8B CF                           mov ecx, edi
004414A1  48 8B 94 24 08 01 00 00         mov rdx, qword ptr [rsp + 0x108]
004414A9  89 8C 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], ecx
004414B0  3B 8C 24 C0 00 00 00            cmp ecx, dword ptr [rsp + 0xc0]
004414B7  73 1B                           jae 0x1404414d4
004414B9  8B C1                           mov eax, ecx
004414BB  41 89 1C 81                     mov dword ptr [r9 + rax*4], ebx
004414BF  89 3C 82                        mov dword ptr [rdx + rax*4], edi
004414C2  41 03 CE                        add ecx, r14d
004414C5  EB E2                           jmp 0x1404414a9
004414C7  41 89 19                        mov dword ptr [r9], ebx
004414CA  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
004414D2  89 38                           mov dword ptr [rax], edi
004414D4  89 9C 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], ebx
004414DB  8B DF                           mov ebx, edi
004414DD  89 9C 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], ebx
004414E4  4C 8B A4 24 D0 00 00 00         mov r12, qword ptr [rsp + 0xd0]
004414EC  E9 85 10 00 00                  jmp 0x140442576
004414F1  8B D8                           mov ebx, eax
004414F3  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
004414FA  33 FF                           xor edi, edi
004414FC  44 8D 77 01                     lea r14d, [rdi + 1]
00441500  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
00441508  44 8B E7                        mov r12d, edi
0044150B  44 8A BC 24 58 03 00 00         mov r15b, byte ptr [rsp + 0x358]
00441513  E9 5E 10 00 00                  jmp 0x140442576
00441518  4C 8B BC 24 30 01 00 00         mov r15, qword ptr [rsp + 0x130]
00441520  4D 85 FF                        test r15, r15
00441523  0F 84 D3 00 00 00               je 0x1404415fc
00441529  41 8B 0F                        mov ecx, dword ptr [r15]
0044152C  8D 04 49                        lea eax, [rcx + rcx*2]
0044152F  C1 E0 02                        shl eax, 2
00441532  41 B8 08 00 00 00               mov r8d, 8
00441538  85 C9                           test ecx, ecx
0044153A  8D 50 08                        lea edx, [rax + 8]
0044153D  75 03                           jne 0x140441542
0044153F  41 8B D0                        mov edx, r8d
00441542  3B 94 24 10 01 00 00            cmp edx, dword ptr [rsp + 0x110]
00441549  76 4F                           jbe 0x14044159a
0044154B  83 C0 08                        add eax, 8
0044154E  85 C9                           test ecx, ecx
00441550  41 0F 44 C0                     cmove eax, r8d
00441554  48 8B 8C 24 B0 01 00 00         mov rcx, qword ptr [rsp + 0x1b0]
0044155C  89 01                           mov dword ptr [rcx], eax
0044155E  BB 23 00 00 C0                  mov ebx, 0xc0000023
00441563  89 9C 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], ebx
0044156A  EB 1F                           jmp 0x14044158b
0044156C  8B D8                           mov ebx, eax
0044156E  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
00441575  33 FF                           xor edi, edi
00441577  44 8D 77 01                     lea r14d, [rdi + 1]
0044157B  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
00441583  4C 8B BC 24 30 01 00 00         mov r15, qword ptr [rsp + 0x130]
0044158B  33 D2                           xor edx, edx
0044158D  49 8B CF                        mov rcx, r15
00441590  E8 DB 12 74 00                  call 0x140b82870
00441595  E9 CC 0F 00 00                  jmp 0x140442566
0044159A  83 C0 08                        add eax, 8
0044159D  85 C9                           test ecx, ecx
0044159F  41 0F 44 C0                     cmove eax, r8d
004415A3  44 8B C0                        mov r8d, eax
004415A6  49 8B D7                        mov rdx, r15
004415A9  48 8B 8C 24 48 01 00 00         mov rcx, qword ptr [rsp + 0x148]
004415B1  E8 8A 52 28 00                  call 0x1406c6840
004415B6  90                              nop
004415B7  33 D2                           xor edx, edx
004415B9  49 8B CF                        mov rcx, r15
004415BC  E8 AF 12 74 00                  call 0x140b82870
004415C1  E9 A2 00 00 00                  jmp 0x140441668
004415C6  8B D8                           mov ebx, eax
004415C8  33 D2                           xor edx, edx
004415CA  48 8B 8C 24 30 01 00 00         mov rcx, qword ptr [rsp + 0x130]
004415D2  E8 99 12 74 00                  call 0x140b82870
004415D7  89 9C 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], ebx
004415DE  33 FF                           xor edi, edi
004415E0  44 8D 77 01                     lea r14d, [rdi + 1]
004415E4  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
004415EC  44 8B E7                        mov r12d, edi
004415EF  44 8A BC 24 58 03 00 00         mov r15b, byte ptr [rsp + 0x358]
004415F7  E9 7A 0F 00 00                  jmp 0x140442576
004415FC  83 BC 24 10 01 00 00 14         cmp dword ptr [rsp + 0x110], 0x14
00441604  73 56                           jae 0x14044165c
00441606  48 8B 84 24 B0 01 00 00         mov rax, qword ptr [rsp + 0x1b0]
0044160E  C7 00 14 00 00 00               mov dword ptr [rax], 0x14
00441614  BB 23 00 00 C0                  mov ebx, 0xc0000023
00441619  89 9C 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], ebx
00441620  4C 8B A4 24 D0 00 00 00         mov r12, qword ptr [rsp + 0xd0]
00441628  44 8A BC 24 58 03 00 00         mov r15b, byte ptr [rsp + 0x358]
00441630  E9 41 0F 00 00                  jmp 0x140442576
00441635  8B D8                           mov ebx, eax
00441637  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
0044163E  33 FF                           xor edi, edi
00441640  44 8D 77 01                     lea r14d, [rdi + 1]
00441644  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
0044164C  44 8B E7                        mov r12d, edi
0044164F  44 8A BC 24 58 03 00 00         mov r15b, byte ptr [rsp + 0x358]
00441657  E9 1A 0F 00 00                  jmp 0x140442576
0044165C  48 8B 84 24 48 01 00 00         mov rax, qword ptr [rsp + 0x148]
00441664  48 83 20 00                     and qword ptr [rax], 0
00441668  48 8B 84 24 B8 01 00 00         mov rax, qword ptr [rsp + 0x1b8]
00441670  48 85 C0                        test rax, rax
00441673  74 3B                           je 0x1404416b0
00441675  48 8D 8C 24 88 01 00 00         lea rcx, [rsp + 0x188]
0044167D  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00441682  44 88 74 24 28                  mov byte ptr [rsp + 0x28], r14b
00441687  8A 94 24 A8 00 00 00            mov dl, byte ptr [rsp + 0xa8]
0044168E  48 8B C8                        mov rcx, rax
00441691  E8 3E 60 4E 00                  call 0x1409276d4
00441696  8B D8                           mov ebx, eax
00441698  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
0044169F  85 C0                           test eax, eax
004416A1  79 0D                           jns 0x1404416b0
004416A3  48 89 BC 24 88 01 00 00         mov qword ptr [rsp + 0x188], rdi
004416AB  E9 B6 0E 00 00                  jmp 0x140442566
004416B0  48 8D 8C 24 C8 01 00 00         lea rcx, [rsp + 0x1c8]
004416B8  E8 63 A1 42 00                  call 0x14086b820
004416BD  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004416C6  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
004416CD  90                              nop
004416CE  41 8A D6                        mov dl, r14b
004416D1  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
004416D9  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
004416DD  E8 DE 04 DD FF                  call 0x140211bc0
004416E2  48 8B 94 24 F8 00 00 00         mov rdx, qword ptr [rsp + 0xf8]
004416EA  48 8B CE                        mov rcx, rsi
004416ED  E8 6E 46 FA FF                  call 0x1403e5d60
004416F2  8A C8                           mov cl, al
004416F4  88 84 24 A0 00 00 00            mov byte ptr [rsp + 0xa0], al
004416FB  80 3D AE B5 9C 00 00            cmp byte ptr [rip + 0x9cb5ae], 0
00441702  0F 85 C5 00 00 00               jne 0x1404417cd
00441708  8B 86 C8 00 00 00               mov eax, dword ptr [rsi + 0xc8]
0044170E  A8 20                           test al, 0x20
00441710  0F 85 B7 00 00 00               jne 0x1404417cd
00441716  48 8B 86 D8 00 00 00            mov rax, qword ptr [rsi + 0xd8]
0044171D  48 85 C0                        test rax, rax
00441720  0F 84 A7 00 00 00               je 0x1404417cd
00441726  8B 40 28                        mov eax, dword ptr [rax + 0x28]
00441729  A8 20                           test al, 0x20
0044172B  0F 84 9C 00 00 00               je 0x1404417cd
00441731  44 8A BC 24 58 03 00 00         mov r15b, byte ptr [rsp + 0x358]
00441739  4C 8B 8C 24 18 01 00 00         mov r9, qword ptr [rsp + 0x118]
00441741  45 84 FF                        test r15b, r15b
00441744  74 28                           je 0x14044176e
00441746  8B CF                           mov ecx, edi
00441748  48 8B 94 24 08 01 00 00         mov rdx, qword ptr [rsp + 0x108]
00441750  89 8C 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], ecx
00441757  3B 8C 24 C0 00 00 00            cmp ecx, dword ptr [rsp + 0xc0]
0044175E  73 1B                           jae 0x14044177b
00441760  8B C1                           mov eax, ecx
00441762  45 89 24 81                     mov dword ptr [r9 + rax*4], r12d
00441766  89 3C 82                        mov dword ptr [rdx + rax*4], edi
00441769  41 03 CE                        add ecx, r14d
0044176C  EB E2                           jmp 0x140441750
0044176E  45 89 21                        mov dword ptr [r9], r12d
00441771  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
00441779  89 38                           mov dword ptr [rax], edi
0044177B  44 89 A4 24 C8 00 00 00         mov dword ptr [rsp + 0xc8], r12d
00441783  8B DF                           mov ebx, edi
00441785  89 9C 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], ebx
0044178C  EB 1F                           jmp 0x1404417ad
0044178E  8B D8                           mov ebx, eax
00441790  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
00441797  33 FF                           xor edi, edi
00441799  44 8D 77 01                     lea r14d, [rdi + 1]
0044179D  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
004417A5  44 8A BC 24 58 03 00 00         mov r15b, byte ptr [rsp + 0x358]
004417AD  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
004417B1  E8 5A E2 E1 FF                  call 0x14025fa10
004417B6  E8 F5 C0 E1 FF                  call 0x14025d8b0
004417BB  48 8D 8C 24 C8 01 00 00         lea rcx, [rsp + 0x1c8]
004417C3  E8 48 9F 42 00                  call 0x14086b710
004417C8  E9 A1 0D 00 00                  jmp 0x14044256e
004417CD  8A 05 F2 32 AC 00               mov al, byte ptr [rip + 0xac32f2]
004417D3  84 C0                           test al, al
004417D5  0F 84 9E 00 00 00               je 0x140441879
004417DB  4C 8B BC 24 F8 00 00 00         mov r15, qword ptr [rsp + 0xf8]
004417E3  41 0F B7 4F 02                  movzx ecx, word ptr [r15 + 2]
004417E8  F6 C1 10                        test cl, 0x10
004417EB  0F 84 81 00 00 00               je 0x140441872
004417F1  44 0F 20 C0                     mov rax, cr8
004417F5  3C 02                           cmp al, 2
004417F7  73 79                           jae 0x140441872
004417F9  66 85 C9                        test cx, cx
004417FC  79 1C                           jns 0x14044181a
004417FE  41 8B 47 0C                     mov eax, dword ptr [r15 + 0xc]
00441802  85 C0                           test eax, eax
00441804  75 0A                           jne 0x140441810
00441806  48 89 BC 24 40 01 00 00         mov qword ptr [rsp + 0x140], rdi
0044180E  EB 62                           jmp 0x140441872
00441810  48 03 84 24 F8 00 00 00         add rax, qword ptr [rsp + 0xf8]
00441818  EB 0C                           jmp 0x140441826
0044181A  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
00441822  48 8B 40 18                     mov rax, qword ptr [rax + 0x18]
00441826  48 89 84 24 40 01 00 00         mov qword ptr [rsp + 0x140], rax
0044182E  48 85 C0                        test rax, rax
00441831  74 3F                           je 0x140441872
00441833  48 8B C8                        mov rcx, rax
00441836  E8 71 41 F6 FF                  call 0x1403a59ac
0044183B  48 85 C0                        test rax, rax
0044183E  74 32                           je 0x140441872
00441840  48 8D 94 24 70 01 00 00         lea rdx, [rsp + 0x170]
00441848  48 8B C8                        mov rcx, rax
0044184B  E8 9C 40 F6 FF                  call 0x1403a58ec
00441850  48 8B 94 24 70 01 00 00         mov rdx, qword ptr [rsp + 0x170]
00441858  85 C0                           test eax, eax
0044185A  48 0F 48 15 8E 68 B9 00         cmovs rdx, qword ptr [rip + 0xb9688e]
00441862  48 89 94 24 70 01 00 00         mov qword ptr [rsp + 0x170], rdx
0044186A  44 88 B4 24 B8 00 00 00         mov byte ptr [rsp + 0xb8], r14b
00441872  8A 8C 24 A0 00 00 00            mov cl, byte ptr [rsp + 0xa0]
00441879  F7 84 24 B0 00 00 00 00 00 06 02  test dword ptr [rsp + 0xb0], 0x2060000
00441884  0F 84 97 00 00 00               je 0x140441921
0044188A  84 C9                           test cl, cl
0044188C  0F 84 8F 00 00 00               je 0x140441921
00441892  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
0044189A  0F B7 48 02                     movzx ecx, word ptr [rax + 2]
0044189E  F6 C1 04                        test cl, 4
004418A1  75 05                           jne 0x1404418a8
004418A3  48 8B D7                        mov rdx, rdi
004418A6  EB 1F                           jmp 0x1404418c7
004418A8  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
004418B0  66 85 C9                        test cx, cx
004418B3  79 0E                           jns 0x1404418c3
004418B5  8B 48 10                        mov ecx, dword ptr [rax + 0x10]
004418B8  85 C9                           test ecx, ecx
004418BA  74 E7                           je 0x1404418a3
004418BC  8B D1                           mov edx, ecx
004418BE  48 03 D0                        add rdx, rax
004418C1  EB 04                           jmp 0x1404418c7
004418C3  48 8B 50 20                     mov rdx, qword ptr [rax + 0x20]
004418C7  33 C9                           xor ecx, ecx
004418C9  E8 22 9A FB FF                  call 0x1403fb2f0
004418CE  84 C0                           test al, al
004418D0  75 4F                           jne 0x140441921
004418D2  F7 84 24 B0 00 00 00 00 00 00 02  test dword ptr [rsp + 0xb0], 0x2000000
004418DD  74 10                           je 0x1404418ef
004418DF  B8 00 00 06 00                  mov eax, 0x60000
004418E4  8B 9C 24 F0 00 00 00            mov ebx, dword ptr [rsp + 0xf0]
004418EB  0B D8                           or ebx, eax
004418ED  EB 17                           jmp 0x140441906
004418EF  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
004418F6  B9 00 00 06 00                  mov ecx, 0x60000
004418FB  23 C1                           and eax, ecx
004418FD  8B D8                           mov ebx, eax
004418FF  0B 9C 24 F0 00 00 00            or ebx, dword ptr [rsp + 0xf0]
00441906  89 84 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], eax
0044190D  89 9C 24 F0 00 00 00            mov dword ptr [rsp + 0xf0], ebx
00441914  81 A4 24 B0 00 00 00 FF FF F9 FF  and dword ptr [rsp + 0xb0], 0xfff9ffff
0044191F  EB 07                           jmp 0x140441928
00441921  8B 9C 24 F0 00 00 00            mov ebx, dword ptr [rsp + 0xf0]
00441928  E8 5B DE 0A 00                  call 0x1404ef788
0044192D  85 C0                           test eax, eax
0044192F  0F 84 05 01 00 00               je 0x140441a3a
00441935  39 BC 24 B0 00 00 00            cmp dword ptr [rsp + 0xb0], edi
0044193C  0F 85 F7 01 00 00               jne 0x140441b39
00441942  40 38 BC 24 B8 00 00 00         cmp byte ptr [rsp + 0xb8], dil
0044194A  74 09                           je 0x140441955
0044194C  45 84 ED                        test r13b, r13b
0044194F  0F 84 E4 01 00 00               je 0x140441b39
00441955  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
0044195D  8B 86 C8 00 00 00               mov eax, dword ptr [rsi + 0xc8]
00441963  25 00 60 00 00                  and eax, 0x6000
00441968  3D 00 20 00 00                  cmp eax, 0x2000
0044196D  74 0D                           je 0x14044197c
0044196F  39 BC 24 D8 00 00 00            cmp dword ptr [rsp + 0xd8], edi
00441976  0F 85 C5 01 00 00               jne 0x140441b41
0044197C  44 8A BC 24 58 03 00 00         mov r15b, byte ptr [rsp + 0x358]
00441984  45 84 FF                        test r15b, r15b
00441987  74 50                           je 0x1404419d9
00441989  8B C7                           mov eax, edi
0044198B  48 8B 94 24 08 02 00 00         mov rdx, qword ptr [rsp + 0x208]
00441993  4C 8B 84 24 10 02 00 00         mov r8, qword ptr [rsp + 0x210]
0044199B  44 8B 8C 24 C0 00 00 00         mov r9d, dword ptr [rsp + 0xc0]
004419A3  89 84 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], eax
004419AA  41 3B C1                        cmp eax, r9d
004419AD  73 59                           jae 0x140441a08
004419AF  8B C8                           mov ecx, eax
004419B1  85 DB                           test ebx, ebx
004419B3  75 11                           jne 0x1404419c6
004419B5  45 89 24 88                     mov dword ptr [r8 + rcx*4], r12d
004419B9  44 89 A4 24 C8 00 00 00         mov dword ptr [rsp + 0xc8], r12d
004419C1  89 3C 8A                        mov dword ptr [rdx + rcx*4], edi
004419C4  EB 0E                           jmp 0x1404419d4
004419C6  41 89 3C 88                     mov dword ptr [r8 + rcx*4], edi
004419CA  89 BC 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], edi
004419D1  89 1C 8A                        mov dword ptr [rdx + rcx*4], ebx
004419D4  41 03 C6                        add eax, r14d
004419D7  EB CA                           jmp 0x1404419a3
004419D9  4C 8B 8C 24 18 01 00 00         mov r9, qword ptr [rsp + 0x118]
004419E1  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
004419E9  85 DB                           test ebx, ebx
004419EB  75 0F                           jne 0x1404419fc
004419ED  45 89 21                        mov dword ptr [r9], r12d
004419F0  44 89 A4 24 C8 00 00 00         mov dword ptr [rsp + 0xc8], r12d
004419F8  89 38                           mov dword ptr [rax], edi
004419FA  EB 0C                           jmp 0x140441a08
004419FC  41 89 39                        mov dword ptr [r9], edi
004419FF  89 BC 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], edi
00441A06  89 18                           mov dword ptr [rax], ebx
00441A08  8B DF                           mov ebx, edi
00441A0A  89 9C 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], ebx
00441A11  E9 97 FD FF FF                  jmp 0x1404417ad
00441A16  8B D8                           mov ebx, eax
00441A18  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
00441A1F  33 FF                           xor edi, edi
00441A21  44 8D 77 01                     lea r14d, [rdi + 1]
00441A25  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
00441A2D  44 8A BC 24 58 03 00 00         mov r15b, byte ptr [rsp + 0x358]
00441A35  E9 73 FD FF FF                  jmp 0x1404417ad
00441A3A  39 BC 24 B0 00 00 00            cmp dword ptr [rsp + 0xb0], edi
00441A41  0F 85 F2 00 00 00               jne 0x140441b39
00441A47  40 38 BC 24 B8 00 00 00         cmp byte ptr [rsp + 0xb8], dil
00441A4F  74 09                           je 0x140441a5a
00441A51  45 84 ED                        test r13b, r13b
00441A54  0F 84 DF 00 00 00               je 0x140441b39
00441A5A  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
00441A62  F7 86 C8 00 00 00 00 20 00 00   test dword ptr [rsi + 0xc8], 0x2000
00441A6C  75 0D                           jne 0x140441a7b
00441A6E  39 BC 24 D8 00 00 00            cmp dword ptr [rsp + 0xd8], edi
00441A75  0F 85 C6 00 00 00               jne 0x140441b41
00441A7B  44 8A BC 24 58 03 00 00         mov r15b, byte ptr [rsp + 0x358]
00441A83  45 84 FF                        test r15b, r15b
00441A86  74 50                           je 0x140441ad8
00441A88  8B C7                           mov eax, edi
00441A8A  48 8B 94 24 08 02 00 00         mov rdx, qword ptr [rsp + 0x208]
00441A92  4C 8B 84 24 10 02 00 00         mov r8, qword ptr [rsp + 0x210]
00441A9A  44 8B 8C 24 C0 00 00 00         mov r9d, dword ptr [rsp + 0xc0]
00441AA2  89 84 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], eax
00441AA9  41 3B C1                        cmp eax, r9d
00441AAC  73 59                           jae 0x140441b07
00441AAE  8B C8                           mov ecx, eax
00441AB0  85 DB                           test ebx, ebx
00441AB2  75 11                           jne 0x140441ac5
00441AB4  45 89 24 88                     mov dword ptr [r8 + rcx*4], r12d
00441AB8  44 89 A4 24 C8 00 00 00         mov dword ptr [rsp + 0xc8], r12d
00441AC0  89 3C 8A                        mov dword ptr [rdx + rcx*4], edi
00441AC3  EB 0E                           jmp 0x140441ad3
00441AC5  41 89 3C 88                     mov dword ptr [r8 + rcx*4], edi
00441AC9  89 BC 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], edi
00441AD0  89 1C 8A                        mov dword ptr [rdx + rcx*4], ebx
00441AD3  41 03 C6                        add eax, r14d
00441AD6  EB CA                           jmp 0x140441aa2
00441AD8  4C 8B 8C 24 18 01 00 00         mov r9, qword ptr [rsp + 0x118]
00441AE0  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
00441AE8  85 DB                           test ebx, ebx
00441AEA  75 0F                           jne 0x140441afb
00441AEC  45 89 21                        mov dword ptr [r9], r12d
00441AEF  44 89 A4 24 C8 00 00 00         mov dword ptr [rsp + 0xc8], r12d
00441AF7  89 38                           mov dword ptr [rax], edi
00441AF9  EB 0C                           jmp 0x140441b07
00441AFB  41 89 39                        mov dword ptr [r9], edi
00441AFE  89 BC 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], edi
00441B05  89 18                           mov dword ptr [rax], ebx
00441B07  8B DF                           mov ebx, edi
00441B09  89 9C 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], ebx
00441B10  E9 98 FC FF FF                  jmp 0x1404417ad
00441B15  8B D8                           mov ebx, eax
00441B17  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
00441B1E  33 FF                           xor edi, edi
00441B20  44 8D 77 01                     lea r14d, [rdi + 1]
00441B24  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
00441B2C  44 8A BC 24 58 03 00 00         mov r15b, byte ptr [rsp + 0x358]
00441B34  E9 74 FC FF FF                  jmp 0x1404417ad
00441B39  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
00441B41  44 8B AC 24 5C 01 00 00         mov r13d, dword ptr [rsp + 0x15c]
00441B49  4E 8D 3C ED 00 00 00 00         lea r15, [r13*8]
00441B51  8A 84 24 58 03 00 00            mov al, byte ptr [rsp + 0x358]
00441B58  84 C0                           test al, al
00441B5A  74 64                           je 0x140441bc0
00441B5C  41 B8 53 65 47 61               mov r8d, 0x61476553
00441B62  49 8B D7                        mov rdx, r15
00441B65  B9 00 01 00 00                  mov ecx, 0x100
00441B6A  E8 81 05 74 00                  call 0x140b820f0
00441B6F  4C 8B E0                        mov r12, rax
00441B72  48 89 84 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], rax
00441B7A  48 85 C0                        test rax, rax
00441B7D  75 34                           jne 0x140441bb3
00441B7F  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00441B83  E8 88 DE E1 FF                  call 0x14025fa10
00441B88  E8 23 BD E1 FF                  call 0x14025d8b0
00441B8D  48 8D 8C 24 C8 01 00 00         lea rcx, [rsp + 0x1c8]
00441B95  E8 76 9B 42 00                  call 0x14086b710
00441B9A  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00441B9F  89 9C 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], ebx
00441BA6  44 8A BC 24 58 03 00 00         mov r15b, byte ptr [rsp + 0x358]
00441BAE  E9 C3 09 00 00                  jmp 0x140442576
00441BB3  4E 8D 2C A8                     lea r13, [rax + r13*4]
00441BB7  8A 84 24 58 03 00 00            mov al, byte ptr [rsp + 0x358]
00441BBE  EB 18                           jmp 0x140441bd8
00441BC0  4C 8D A4 24 58 01 00 00         lea r12, [rsp + 0x158]
00441BC8  4C 89 A4 24 D0 00 00 00         mov qword ptr [rsp + 0xd0], r12
00441BD0  4C 8D AC 24 A8 01 00 00         lea r13, [rsp + 0x1a8]
00441BD8  8B 8C 24 D8 00 00 00            mov ecx, dword ptr [rsp + 0xd8]
00441BDF  89 8C 24 88 02 00 00            mov dword ptr [rsp + 0x288], ecx
00441BE6  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
00441BEE  48 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdi
00441BF6  48 8D 8C 24 50 01 00 00         lea rcx, [rsp + 0x150]
00441BFE  48 89 8C 24 80 00 00 00         mov qword ptr [rsp + 0x80], rcx
00441C06  48 8D 8C 24 88 02 00 00         lea rcx, [rsp + 0x288]
00441C0E  48 89 4C 24 78                  mov qword ptr [rsp + 0x78], rcx
00441C13  8A 8C 24 A0 00 00 00            mov cl, byte ptr [rsp + 0xa0]
00441C1A  88 4C 24 70                     mov byte ptr [rsp + 0x70], cl
00441C1E  88 44 24 68                     mov byte ptr [rsp + 0x68], al
00441C22  4C 89 6C 24 60                  mov qword ptr [rsp + 0x60], r13
00441C27  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
00441C2C  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
00441C31  8A 84 24 A8 00 00 00            mov al, byte ptr [rsp + 0xa8]
00441C38  88 44 24 48                     mov byte ptr [rsp + 0x48], al
00441C3C  89 5C 24 40                     mov dword ptr [rsp + 0x40], ebx
00441C40  48 8D 84 24 A8 02 00 00         lea rax, [rsp + 0x2a8]
00441C48  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00441C4D  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
00441C54  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00441C58  48 8B 84 24 80 01 00 00         mov rax, qword ptr [rsp + 0x180]
00441C60  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00441C65  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
00441C6C  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00441C70  4C 8B CE                        mov r9, rsi
00441C73  4C 8B 84 24 D8 01 00 00         mov r8, qword ptr [rsp + 0x1d8]
00441C7B  48 8B 94 24 88 01 00 00         mov rdx, qword ptr [rsp + 0x188]
00441C83  48 8B 8C 24 F8 00 00 00         mov rcx, qword ptr [rsp + 0xf8]
00441C8B  E8 C4 F1 F8 FF                  call 0x1403d0e54
00441C90  8A 05 2F 2E AC 00               mov al, byte ptr [rip + 0xac2e2f]
00441C96  84 C0                           test al, al
00441C98  0F 84 E9 04 00 00               je 0x140442187
00441C9E  41 39 7D 00                     cmp dword ptr [r13], edi
00441CA2  0F 8C DF 04 00 00               jl 0x140442187
00441CA8  40 38 BC 24 B8 00 00 00         cmp byte ptr [rsp + 0xb8], dil
00441CB0  0F 84 D1 04 00 00               je 0x140442187
00441CB6  40 38 BC 24 58 03 00 00         cmp byte ptr [rsp + 0x358], dil
00441CBE  74 42                           je 0x140441d02
00441CC0  41 B8 53 65 47 61               mov r8d, 0x61476553
00441CC6  49 8B D7                        mov rdx, r15
00441CC9  B9 00 01 00 00                  mov ecx, 0x100
00441CCE  E8 1D 04 74 00                  call 0x140b820f0
00441CD3  48 89 84 24 68 01 00 00         mov qword ptr [rsp + 0x168], rax
00441CDB  48 85 C0                        test rax, rax
00441CDE  75 0D                           jne 0x140441ced
00441CE0  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
00441CE8  E9 92 FE FF FF                  jmp 0x140441b7f
00441CED  8B 8C 24 5C 01 00 00            mov ecx, dword ptr [rsp + 0x15c]
00441CF4  48 8D 0C 88                     lea rcx, [rax + rcx*4]
00441CF8  48 89 8C 24 20 01 00 00         mov qword ptr [rsp + 0x120], rcx
00441D00  EB 20                           jmp 0x140441d22
00441D02  48 8D 84 24 A4 01 00 00         lea rax, [rsp + 0x1a4]
00441D0A  48 89 84 24 68 01 00 00         mov qword ptr [rsp + 0x168], rax
00441D12  48 8D 84 24 A0 01 00 00         lea rax, [rsp + 0x1a0]
00441D1A  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
00441D22  45 8B 55 00                     mov r10d, dword ptr [r13]
00441D26  44 89 94 24 30 01 00 00         mov dword ptr [rsp + 0x130], r10d
00441D2E  45 8B 1C 24                     mov r11d, dword ptr [r12]
00441D32  44 89 9C 24 D8 00 00 00         mov dword ptr [rsp + 0xd8], r11d
00441D3A  40 8A DF                        mov bl, dil
00441D3D  89 9C 24 04 01 00 00            mov dword ptr [rsp + 0x104], ebx
00441D44  8B 84 24 C0 00 00 00            mov eax, dword ptr [rsp + 0xc0]
00441D4B  85 C0                           test eax, eax
00441D4D  74 48                           je 0x140441d97
00441D4F  4C 8D 84 24 98 01 00 00         lea r8, [rsp + 0x198]
00441D57  8B D0                           mov edx, eax
00441D59  48 8B 8C 24 80 01 00 00         mov rcx, qword ptr [rsp + 0x180]
00441D61  E8 5A 4F 1C 00                  call 0x140606cc0
00441D66  8B D8                           mov ebx, eax
00441D68  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
00441D6F  85 C0                           test eax, eax
00441D71  79 0D                           jns 0x140441d80
00441D73  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
00441D7B  E9 26 FE FF FF                  jmp 0x140441ba6
00441D80  44 8B 94 24 30 01 00 00         mov r10d, dword ptr [rsp + 0x130]
00441D88  44 8B 9C 24 D8 00 00 00         mov r11d, dword ptr [rsp + 0xd8]
00441D90  8B 9C 24 04 01 00 00            mov ebx, dword ptr [rsp + 0x104]
00441D97  8B C7                           mov eax, edi
00441D99  89 84 24 48 01 00 00            mov dword ptr [rsp + 0x148], eax
00441DA0  48 8B 8C 24 70 01 00 00         mov rcx, qword ptr [rsp + 0x170]
00441DA8  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
00441DB0  39 79 3C                        cmp dword ptr [rcx + 0x3c], edi
00441DB3  0F 86 92 03 00 00               jbe 0x14044214b
00441DB9  4C 8B A4 24 40 01 00 00         mov r12, qword ptr [rsp + 0x140]
00441DC1  8B C8                           mov ecx, eax
00441DC3  48 8B 84 24 70 01 00 00         mov rax, qword ptr [rsp + 0x170]
00441DCB  4C 8B 7C C8 40                  mov r15, qword ptr [rax + rcx*8 + 0x40]
00441DD0  49 39 7F 18                     cmp qword ptr [r15 + 0x18], rdi
00441DD4  0F 84 B6 01 00 00               je 0x140441f90
00441DDA  4C 8B 84 24 50 01 00 00         mov r8, qword ptr [rsp + 0x150]
00441DE2  4D 85 C0                        test r8, r8
00441DE5  75 28                           jne 0x140441e0f
00441DE7  48 8D 94 24 50 01 00 00         lea rdx, [rsp + 0x150]
00441DEF  49 8B CC                        mov rcx, r12
00441DF2  E8 8D 10 EC FF                  call 0x140302e84
00441DF7  0F B6 DB                        movzx ebx, bl
00441DFA  85 C0                           test eax, eax
00441DFC  41 0F 48 DE                     cmovs ebx, r14d
00441E00  89 9C 24 04 01 00 00            mov dword ptr [rsp + 0x104], ebx
00441E07  4C 8B 84 24 50 01 00 00         mov r8, qword ptr [rsp + 0x150]
00441E0F  48 8B 86 48 04 00 00            mov rax, qword ptr [rsi + 0x448]
00441E16  48 85 C0                        test rax, rax
00441E19  74 09                           je 0x140441e24
00441E1B  4C 8B 90 58 02 00 00            mov r10, qword ptr [rax + 0x258]
00441E22  EB 03                           jmp 0x140441e27
00441E24  4C 8B D7                        mov r10, rdi
00441E27  48 85 C0                        test rax, rax
00441E2A  74 09                           je 0x140441e35
00441E2C  48 8B 90 48 02 00 00            mov rdx, qword ptr [rax + 0x248]
00441E33  EB 03                           jmp 0x140441e38
00441E35  48 8B D7                        mov rdx, rdi
00441E38  48 85 C0                        test rax, rax
00441E3B  74 09                           je 0x140441e46
00441E3D  48 8B 88 50 02 00 00            mov rcx, qword ptr [rax + 0x250]
00441E44  EB 03                           jmp 0x140441e49
00441E46  48 8B CF                        mov rcx, rdi
00441E49  48 85 C0                        test rax, rax
00441E4C  74 09                           je 0x140441e57
00441E4E  4C 8B 88 40 02 00 00            mov r9, qword ptr [rax + 0x240]
00441E55  EB 03                           jmp 0x140441e5a
00441E57  4C 8B CF                        mov r9, rdi
00441E5A  48 8D 84 24 28 01 00 00         lea rax, [rsp + 0x128]
00441E62  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00441E67  40 88 7C 24 50                  mov byte ptr [rsp + 0x50], dil
00441E6C  44 88 74 24 48                  mov byte ptr [rsp + 0x48], r14b
00441E71  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
00441E75  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00441E79  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
00441E7D  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00441E82  4C 89 54 24 30                  mov qword ptr [rsp + 0x30], r10
00441E87  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
00441E8C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00441E91  48 8B 96 08 03 00 00            mov rdx, qword ptr [rsi + 0x308]
00441E98  48 8B CE                        mov rcx, rsi
00441E9B  E8 30 CD EB FF                  call 0x1402febd0
00441EA0  8B D8                           mov ebx, eax
00441EA2  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
00441EA9  44 39 B4 24 28 01 00 00         cmp dword ptr [rsp + 0x128], r14d
00441EB1  0F 84 D9 00 00 00               je 0x140441f90
00441EB7  85 C0                           test eax, eax
00441EB9  0F 88 A8 02 00 00               js 0x140442167
00441EBF  8B 86 C8 00 00 00               mov eax, dword ptr [rsi + 0xc8]
00441EC5  A8 10                           test al, 0x10
00441EC7  0F 84 AA 00 00 00               je 0x140441f77
00441ECD  48 8B 86 48 04 00 00            mov rax, qword ptr [rsi + 0x448]
00441ED4  48 85 C0                        test rax, rax
00441ED7  74 09                           je 0x140441ee2
00441ED9  4C 8B 80 58 02 00 00            mov r8, qword ptr [rax + 0x258]
00441EE0  EB 03                           jmp 0x140441ee5
00441EE2  4C 8B C7                        mov r8, rdi
00441EE5  48 85 C0                        test rax, rax
00441EE8  74 09                           je 0x140441ef3
00441EEA  48 8B 90 48 02 00 00            mov rdx, qword ptr [rax + 0x248]
00441EF1  EB 03                           jmp 0x140441ef6
00441EF3  48 8B D7                        mov rdx, rdi
00441EF6  48 85 C0                        test rax, rax
00441EF9  74 09                           je 0x140441f04
00441EFB  48 8B 88 50 02 00 00            mov rcx, qword ptr [rax + 0x250]
00441F02  EB 03                           jmp 0x140441f07
00441F04  48 8B CF                        mov rcx, rdi
00441F07  48 85 C0                        test rax, rax
00441F0A  74 09                           je 0x140441f15
00441F0C  4C 8B 88 40 02 00 00            mov r9, qword ptr [rax + 0x240]
00441F13  EB 03                           jmp 0x140441f18
00441F15  4C 8B CF                        mov r9, rdi
00441F18  48 8D 84 24 28 01 00 00         lea rax, [rsp + 0x128]
00441F20  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
00441F25  44 88 74 24 50                  mov byte ptr [rsp + 0x50], r14b
00441F2A  44 88 74 24 48                  mov byte ptr [rsp + 0x48], r14b
00441F2F  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
00441F33  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
00441F37  49 8B 47 18                     mov rax, qword ptr [r15 + 0x18]
00441F3B  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00441F40  4C 89 44 24 30                  mov qword ptr [rsp + 0x30], r8
00441F45  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
00441F4A  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00441F4F  4C 8B 84 24 50 01 00 00         mov r8, qword ptr [rsp + 0x150]
00441F57  48 8B 96 08 03 00 00            mov rdx, qword ptr [rsi + 0x308]
00441F5E  48 8B CE                        mov rcx, rsi
00441F61  E8 6A CC EB FF                  call 0x1402febd0
00441F66  8B D8                           mov ebx, eax
00441F68  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
00441F6F  85 C0                           test eax, eax
00441F71  0F 88 F0 01 00 00               js 0x140442167
00441F77  8B 9C 24 04 01 00 00            mov ebx, dword ptr [rsp + 0x104]
00441F7E  84 DB                           test bl, bl
00441F80  75 0E                           jne 0x140441f90
00441F82  44 39 B4 24 28 01 00 00         cmp dword ptr [rsp + 0x128], r14d
00441F8A  0F 85 C5 01 00 00               jne 0x140442155
00441F90  4C 8B 84 24 40 01 00 00         mov r8, qword ptr [rsp + 0x140]
00441F98  49 8B 57 20                     mov rdx, qword ptr [r15 + 0x20]
00441F9C  48 8D 8C 24 60 02 00 00         lea rcx, [rsp + 0x260]
00441FA4  E8 8F 7E 09 00                  call 0x1404d9e38
00441FA9  8B D8                           mov ebx, eax
00441FAB  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
00441FB2  85 C0                           test eax, eax
00441FB4  0F 88 AD 01 00 00               js 0x140442167
00441FBA  41 8B 47 30                     mov eax, dword ptr [r15 + 0x30]
00441FBE  44 8B A4 24 B0 00 00 00         mov r12d, dword ptr [rsp + 0xb0]
00441FC6  41 84 C6                        test r14b, al
00441FC9  74 13                           je 0x140441fde
00441FCB  41 0F BA E4 19                  bt r12d, 0x19
00441FD0  72 08                           jb 0x140441fda
00441FD2  44 0B A4 24 F0 00 00 00         or r12d, dword ptr [rsp + 0xf0]
00441FDA  8B CF                           mov ecx, edi
00441FDC  EB 07                           jmp 0x140441fe5
00441FDE  8B 8C 24 F0 00 00 00            mov ecx, dword ptr [rsp + 0xf0]
00441FE5  48 89 BC 24 90 00 00 00         mov qword ptr [rsp + 0x90], rdi
00441FED  48 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdi
00441FF5  48 8D 84 24 50 01 00 00         lea rax, [rsp + 0x150]
00441FFD  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00442005  48 8D 84 24 88 02 00 00         lea rax, [rsp + 0x288]
0044200D  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
00442012  8A 84 24 A0 00 00 00            mov al, byte ptr [rsp + 0xa0]
00442019  88 44 24 70                     mov byte ptr [rsp + 0x70], al
0044201D  8A 84 24 58 03 00 00            mov al, byte ptr [rsp + 0x358]
00442024  88 44 24 68                     mov byte ptr [rsp + 0x68], al
00442028  48 8B 84 24 20 01 00 00         mov rax, qword ptr [rsp + 0x120]
00442030  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00442035  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
0044203A  4C 8B BC 24 68 01 00 00         mov r15, qword ptr [rsp + 0x168]
00442042  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
00442047  8A 84 24 A8 00 00 00            mov al, byte ptr [rsp + 0xa8]
0044204E  88 44 24 48                     mov byte ptr [rsp + 0x48], al
00442052  89 4C 24 40                     mov dword ptr [rsp + 0x40], ecx
00442056  48 8D 84 24 A8 02 00 00         lea rax, [rsp + 0x2a8]
0044205E  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00442063  8B 9C 24 C0 00 00 00            mov ebx, dword ptr [rsp + 0xc0]
0044206A  89 5C 24 30                     mov dword ptr [rsp + 0x30], ebx
0044206E  48 8B 84 24 98 01 00 00         mov rax, qword ptr [rsp + 0x198]
00442076  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0044207B  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00442080  4C 8B CE                        mov r9, rsi
00442083  4C 8B 84 24 D8 01 00 00         mov r8, qword ptr [rsp + 0x1d8]
0044208B  48 8B 94 24 88 01 00 00         mov rdx, qword ptr [rsp + 0x188]
00442093  48 8D 8C 24 60 02 00 00         lea rcx, [rsp + 0x260]
0044209B  E8 B4 ED F8 FF                  call 0x1403d0e54
004420A0  41 8B 07                        mov eax, dword ptr [r15]
004420A3  40 38 BC 24 A9 00 00 00         cmp byte ptr [rsp + 0xa9], dil
004420AB  75 05                           jne 0x1404420b2
004420AD  44 8B D8                        mov r11d, eax
004420B0  EB 0B                           jmp 0x1404420bd
004420B2  44 8B 9C 24 D8 00 00 00         mov r11d, dword ptr [rsp + 0xd8]
004420BA  44 23 D8                        and r11d, eax
004420BD  44 89 9C 24 D8 00 00 00         mov dword ptr [rsp + 0xd8], r11d
004420C5  45 85 DB                        test r11d, r11d
004420C8  75 08                           jne 0x1404420d2
004420CA  41 BA 22 00 00 C0               mov r10d, 0xc0000022
004420D0  EB 0B                           jmp 0x1404420dd
004420D2  48 8B 84 24 20 01 00 00         mov rax, qword ptr [rsp + 0x120]
004420DA  44 8B 10                        mov r10d, dword ptr [rax]
004420DD  44 89 94 24 30 01 00 00         mov dword ptr [rsp + 0x130], r10d
004420E5  44 88 B4 24 A9 00 00 00         mov byte ptr [rsp + 0xa9], r14b
004420ED  48 8B 8C 24 98 01 00 00         mov rcx, qword ptr [rsp + 0x198]
004420F5  48 85 C9                        test rcx, rcx
004420F8  74 13                           je 0x14044210d
004420FA  44 8B C3                        mov r8d, ebx
004420FD  48 8B D1                        mov rdx, rcx
00442100  48 8B 8C 24 80 01 00 00         mov rcx, qword ptr [rsp + 0x180]
00442108  E8 FB 53 1C 00                  call 0x140607508
0044210D  45 85 D2                        test r10d, r10d
00442110  78 31                           js 0x140442143
00442112  8B 9C 24 04 01 00 00            mov ebx, dword ptr [rsp + 0x104]
00442119  4C 8B A4 24 40 01 00 00         mov r12, qword ptr [rsp + 0x140]
00442121  8B 84 24 48 01 00 00            mov eax, dword ptr [rsp + 0x148]
00442128  41 03 C6                        add eax, r14d
0044212B  89 84 24 48 01 00 00            mov dword ptr [rsp + 0x148], eax
00442132  48 8B 8C 24 70 01 00 00         mov rcx, qword ptr [rsp + 0x170]
0044213A  3B 41 3C                        cmp eax, dword ptr [rcx + 0x3c]
0044213D  0F 82 7E FC FF FF               jb 0x140441dc1
00442143  4C 8B A4 24 D0 00 00 00         mov r12, qword ptr [rsp + 0xd0]
0044214B  45 89 55 00                     mov dword ptr [r13], r10d
0044214F  45 21 1C 24                     and dword ptr [r12], r11d
00442153  EB 3A                           jmp 0x14044218f
00442155  44 8B 94 24 30 01 00 00         mov r10d, dword ptr [rsp + 0x130]
0044215D  44 8B 9C 24 D8 00 00 00         mov r11d, dword ptr [rsp + 0xd8]
00442165  EB BA                           jmp 0x140442121
00442167  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
0044216B  E8 A0 D8 E1 FF                  call 0x14025fa10
00442170  E8 3B B7 E1 FF                  call 0x14025d8b0
00442175  48 8D 8C 24 C8 01 00 00         lea rcx, [rsp + 0x1c8]
0044217D  E8 8E 95 42 00                  call 0x14086b710
00442182  E9 DF 03 00 00                  jmp 0x140442566
00442187  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
0044218F  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
00442193  E8 78 D8 E1 FF                  call 0x14025fa10
00442198  E8 13 B7 E1 FF                  call 0x14025d8b0
0044219D  48 8D 8C 24 C8 01 00 00         lea rcx, [rsp + 0x1c8]
004421A5  E8 66 95 42 00                  call 0x14086b710
004421AA  8B 9C 24 B0 00 00 00            mov ebx, dword ptr [rsp + 0xb0]
004421B1  81 E3 00 00 00 02               and ebx, 0x2000000
004421B7  0F 84 95 00 00 00               je 0x140442252
004421BD  80 BC 24 00 01 00 00 00         cmp byte ptr [rsp + 0x100], 0
004421C5  74 25                           je 0x1404421ec
004421C7  40 38 BC 24 9E 02 00 00         cmp byte ptr [rsp + 0x29e], dil
004421CF  75 50                           jne 0x140442221
004421D1  40 38 BC 24 9D 02 00 00         cmp byte ptr [rsp + 0x29d], dil
004421D9  75 46                           jne 0x140442221
004421DB  8B 86 C8 00 00 00               mov eax, dword ptr [rsi + 0xc8]
004421E1  B9 00 00 00 03                  mov ecx, 0x3000000
004421E6  23 C1                           and eax, ecx
004421E8  3B C1                           cmp eax, ecx
004421EA  74 35                           je 0x140442221
004421EC  8A 84 24 58 03 00 00            mov al, byte ptr [rsp + 0x358]
004421F3  F6 D8                           neg al
004421F5  1B C9                           sbb ecx, ecx
004421F7  23 8C 24 38 01 00 00            and ecx, dword ptr [rsp + 0x138]
004421FE  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
00442202  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00442207  4D 8B CD                        mov r9, r13
0044220A  4D 8B C4                        mov r8, r12
0044220D  8B 94 24 B0 00 00 00            mov edx, dword ptr [rsp + 0xb0]
00442214  48 8D 8C 24 18 02 00 00         lea rcx, [rsp + 0x218]
0044221C  E8 4F DA FF FF                  call 0x14043fc70
00442221  E8 42 B7 18 00                  call 0x1405cd968
00442226  44 8A BC 24 58 03 00 00         mov r15b, byte ptr [rsp + 0x358]
0044222E  8B B4 24 C0 00 00 00            mov esi, dword ptr [rsp + 0xc0]
00442235  85 C0                           test eax, eax
00442237  0F 84 6B 01 00 00               je 0x1404423a8
0044223D  8B 84 24 60 01 00 00            mov eax, dword ptr [rsp + 0x160]
00442244  F7 D0                           not eax
00442246  21 84 24 58 01 00 00            and dword ptr [rsp + 0x158], eax
0044224D  E9 56 01 00 00                  jmp 0x1404423a8
00442252  80 BC 24 00 01 00 00 00         cmp byte ptr [rsp + 0x100], 0
0044225A  0F 84 39 01 00 00               je 0x140442399
00442260  40 38 BC 24 9E 02 00 00         cmp byte ptr [rsp + 0x29e], dil
00442268  0F 85 2B 01 00 00               jne 0x140442399
0044226E  40 38 BC 24 9D 02 00 00         cmp byte ptr [rsp + 0x29d], dil
00442276  0F 85 1D 01 00 00               jne 0x140442399
0044227C  8B 86 C8 00 00 00               mov eax, dword ptr [rsi + 0xc8]
00442282  B9 00 00 00 03                  mov ecx, 0x3000000
00442287  23 C1                           and eax, ecx
00442289  3B C1                           cmp eax, ecx
0044228B  75 75                           jne 0x140442302
0044228D  39 BC 24 94 02 00 00            cmp dword ptr [rsp + 0x294], edi
00442294  75 6C                           jne 0x140442302
00442296  44 88 B4 24 9F 02 00 00         mov byte ptr [rsp + 0x29f], r14b
0044229E  44 8A BC 24 58 03 00 00         mov r15b, byte ptr [rsp + 0x358]
004422A6  45 84 FF                        test r15b, r15b
004422A9  74 3C                           je 0x1404422e7
004422AB  8B B4 24 C0 00 00 00            mov esi, dword ptr [rsp + 0xc0]
004422B2  85 F6                           test esi, esi
004422B4  0F 84 EE 00 00 00               je 0x1404423a8
004422BA  8B 8C 24 B0 00 00 00            mov ecx, dword ptr [rsp + 0xb0]
004422C1  0B 8C 24 F0 00 00 00            or ecx, dword ptr [rsp + 0xf0]
004422C8  49 8B C4                        mov rax, r12
004422CB  49 8B D5                        mov rdx, r13
004422CE  49 2B D4                        sub rdx, r12
004422D1  44 8B C6                        mov r8d, esi
004422D4  89 3C 02                        mov dword ptr [rdx + rax], edi
004422D7  89 08                           mov dword ptr [rax], ecx
004422D9  48 8D 40 04                     lea rax, [rax + 4]
004422DD  4D 2B C6                        sub r8, r14
004422E0  75 F2                           jne 0x1404422d4
004422E2  E9 C1 00 00 00                  jmp 0x1404423a8
004422E7  41 89 7D 00                     mov dword ptr [r13], edi
004422EB  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
004422F2  0B 84 24 F0 00 00 00            or eax, dword ptr [rsp + 0xf0]
004422F9  41 89 04 24                     mov dword ptr [r12], eax
004422FD  E9 9F 00 00 00                  jmp 0x1404423a1
00442302  44 8A BC 24 58 03 00 00         mov r15b, byte ptr [rsp + 0x358]
0044230A  4C 8B 8C 24 18 01 00 00         mov r9, qword ptr [rsp + 0x118]
00442312  45 84 FF                        test r15b, r15b
00442315  74 2C                           je 0x140442343
00442317  8B CF                           mov ecx, edi
00442319  48 8B 94 24 08 01 00 00         mov rdx, qword ptr [rsp + 0x108]
00442321  89 8C 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], ecx
00442328  3B 8C 24 C0 00 00 00            cmp ecx, dword ptr [rsp + 0xc0]
0044232F  73 23                           jae 0x140442354
00442331  8B C1                           mov eax, ecx
00442333  41 C7 04 81 22 00 00 C0         mov dword ptr [r9 + rax*4], 0xc0000022
0044233B  89 3C 82                        mov dword ptr [rdx + rax*4], edi
0044233E  41 03 CE                        add ecx, r14d
00442341  EB DE                           jmp 0x140442321
00442343  41 C7 01 22 00 00 C0            mov dword ptr [r9], 0xc0000022
0044234A  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
00442352  89 38                           mov dword ptr [rax], edi
00442354  C7 84 24 C8 00 00 00 22 00 00 C0  mov dword ptr [rsp + 0xc8], 0xc0000022
0044235F  8B DF                           mov ebx, edi
00442361  89 9C 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], ebx
00442368  E9 09 02 00 00                  jmp 0x140442576
0044236D  8B D8                           mov ebx, eax
0044236F  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
00442376  33 FF                           xor edi, edi
00442378  44 8D 77 01                     lea r14d, [rdi + 1]
0044237C  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
00442384  4C 8B A4 24 D0 00 00 00         mov r12, qword ptr [rsp + 0xd0]
0044238C  44 8A BC 24 58 03 00 00         mov r15b, byte ptr [rsp + 0x358]
00442394  E9 DD 01 00 00                  jmp 0x140442576
00442399  44 8A BC 24 58 03 00 00         mov r15b, byte ptr [rsp + 0x358]
004423A1  8B B4 24 C0 00 00 00            mov esi, dword ptr [rsp + 0xc0]
004423A8  85 DB                           test ebx, ebx
004423AA  74 79                           je 0x140442425
004423AC  41 8A C7                        mov al, r15b
004423AF  F6 D8                           neg al
004423B1  1B DB                           sbb ebx, ebx
004423B3  23 9C 24 38 01 00 00            and ebx, dword ptr [rsp + 0x138]
004423BA  48 8D 84 24 CC 00 00 00         lea rax, [rsp + 0xcc]
004423C2  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
004423C7  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
004423CB  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
004423D0  4D 8B CD                        mov r9, r13
004423D3  4D 8B C4                        mov r8, r12
004423D6  8B 94 24 B0 00 00 00            mov edx, dword ptr [rsp + 0xb0]
004423DD  8B 8C 24 78 01 00 00            mov ecx, dword ptr [rsp + 0x178]
004423E4  E8 F7 D9 FF FF                  call 0x14043fde0
004423E9  48 8D 94 24 CD 00 00 00         lea rdx, [rsp + 0xcd]
004423F1  48 89 54 24 30                  mov qword ptr [rsp + 0x30], rdx
004423F6  89 5C 24 28                     mov dword ptr [rsp + 0x28], ebx
004423FA  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
004423FF  4D 8B CD                        mov r9, r13
00442402  4C 8B 84 24 D0 00 00 00         mov r8, qword ptr [rsp + 0xd0]
0044240A  8B 94 24 B0 00 00 00            mov edx, dword ptr [rsp + 0xb0]
00442411  8B 8C 24 90 01 00 00            mov ecx, dword ptr [rsp + 0x190]
00442418  E8 C3 D9 FF FF                  call 0x14043fde0
0044241D  4C 8B A4 24 D0 00 00 00         mov r12, qword ptr [rsp + 0xd0]
00442425  41 8B 45 00                     mov eax, dword ptr [r13]
00442429  4C 8B 8C 24 18 01 00 00         mov r9, qword ptr [rsp + 0x118]
00442431  41 89 01                        mov dword ptr [r9], eax
00442434  41 8B 04 24                     mov eax, dword ptr [r12]
00442438  4C 8B 84 24 08 01 00 00         mov r8, qword ptr [rsp + 0x108]
00442440  41 89 00                        mov dword ptr [r8], eax
00442443  41 8B 45 00                     mov eax, dword ptr [r13]
00442447  89 84 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], eax
0044244E  8A 05 71 26 AC 00               mov al, byte ptr [rip + 0xac2671]
00442454  8A 8C 24 A9 00 00 00            mov cl, byte ptr [rsp + 0xa9]
0044245B  4C 8B 94 24 20 01 00 00         mov r10, qword ptr [rsp + 0x120]
00442463  84 C0                           test al, al
00442465  74 2E                           je 0x140442495
00442467  84 C9                           test cl, cl
00442469  74 2A                           je 0x140442495
0044246B  41 39 7D 00                     cmp dword ptr [r13], edi
0044246F  7C 24                           jl 0x140442495
00442471  41 8B 02                        mov eax, dword ptr [r10]
00442474  41 89 01                        mov dword ptr [r9], eax
00442477  48 8B 84 24 68 01 00 00         mov rax, qword ptr [rsp + 0x168]
0044247F  8B 08                           mov ecx, dword ptr [rax]
00442481  41 21 08                        and dword ptr [r8], ecx
00442484  41 8B 02                        mov eax, dword ptr [r10]
00442487  89 84 24 C8 00 00 00            mov dword ptr [rsp + 0xc8], eax
0044248E  8A 8C 24 A9 00 00 00            mov cl, byte ptr [rsp + 0xa9]
00442495  45 84 FF                        test r15b, r15b
00442498  74 60                           je 0x1404424fa
0044249A  41 8B C6                        mov eax, r14d
0044249D  89 84 24 E8 00 00 00            mov dword ptr [rsp + 0xe8], eax
004424A4  3B C6                           cmp eax, esi
004424A6  73 52                           jae 0x1404424fa
004424A8  8B D0                           mov edx, eax
004424AA  41 8B 44 95 00                  mov eax, dword ptr [r13 + rdx*4]
004424AF  41 89 04 91                     mov dword ptr [r9 + rdx*4], eax
004424B3  41 8B 04 94                     mov eax, dword ptr [r12 + rdx*4]
004424B7  41 89 04 90                     mov dword ptr [r8 + rdx*4], eax
004424BB  8A 05 04 26 AC 00               mov al, byte ptr [rip + 0xac2604]
004424C1  84 C0                           test al, al
004424C3  74 22                           je 0x1404424e7
004424C5  84 C9                           test cl, cl
004424C7  74 1E                           je 0x1404424e7
004424C9  41 39 7C 95 00                  cmp dword ptr [r13 + rdx*4], edi
004424CE  7C 17                           jl 0x1404424e7
004424D0  41 8B 04 92                     mov eax, dword ptr [r10 + rdx*4]
004424D4  41 89 04 91                     mov dword ptr [r9 + rdx*4], eax
004424D8  48 8B 84 24 68 01 00 00         mov rax, qword ptr [rsp + 0x168]
004424E0  8B 0C 90                        mov ecx, dword ptr [rax + rdx*4]
004424E3  41 21 0C 90                     and dword ptr [r8 + rdx*4], ecx
004424E7  8B 84 24 E8 00 00 00            mov eax, dword ptr [rsp + 0xe8]
004424EE  41 03 C6                        add eax, r14d
004424F1  8A 8C 24 A9 00 00 00            mov cl, byte ptr [rsp + 0xa9]
004424F8  EB A3                           jmp 0x14044249d
004424FA  8B DF                           mov ebx, edi
004424FC  89 9C 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], ebx
00442503  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
0044250B  EB 69                           jmp 0x140442576
0044250D  8B D8                           mov ebx, eax
0044250F  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
00442516  33 FF                           xor edi, edi
00442518  44 8D 77 01                     lea r14d, [rdi + 1]
0044251C  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
00442524  4C 8B A4 24 D0 00 00 00         mov r12, qword ptr [rsp + 0xd0]
0044252C  44 8A BC 24 58 03 00 00         mov r15b, byte ptr [rsp + 0x358]
00442534  EB 40                           jmp 0x140442576
00442536  8B D8                           mov ebx, eax
00442538  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
0044253F  33 FF                           xor edi, edi
00442541  44 8D 77 01                     lea r14d, [rdi + 1]
00442545  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
0044254D  44 8B E7                        mov r12d, edi
00442550  44 8A BC 24 58 03 00 00         mov r15b, byte ptr [rsp + 0x358]
00442558  EB 1C                           jmp 0x140442576
0044255A  BB 79 00 00 C0                  mov ebx, 0xc0000079
0044255F  89 9C 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], ebx
00442566  44 8A BC 24 58 03 00 00         mov r15b, byte ptr [rsp + 0x358]
0044256E  4C 8B A4 24 D0 00 00 00         mov r12, qword ptr [rsp + 0xd0]
00442576  48 39 BC 24 F8 00 00 00         cmp qword ptr [rsp + 0xf8], rdi
0044257E  0F 84 2A 01 00 00               je 0x1404426ae
00442584  48 85 F6                        test rsi, rsi
00442587  0F 84 21 01 00 00               je 0x1404426ae
0044258D  40 38 BC 24 CC 00 00 00         cmp byte ptr [rsp + 0xcc], dil
00442595  75 46                           jne 0x1404425dd
00442597  40 38 BC 24 CD 00 00 00         cmp byte ptr [rsp + 0xcd], dil
0044259F  75 3C                           jne 0x1404425dd
004425A1  39 BC 24 94 02 00 00            cmp dword ptr [rsp + 0x294], edi
004425A8  0F 85 C1 00 00 00               jne 0x14044266f
004425AE  F7 86 C8 00 00 00 00 40 00 00   test dword ptr [rsi + 0xc8], 0x4000
004425B8  0F 84 B1 00 00 00               je 0x14044266f
004425BE  85 DB                           test ebx, ebx
004425C0  0F 88 E8 00 00 00               js 0x1404426ae
004425C6  39 BC 24 C8 00 00 00            cmp dword ptr [rsp + 0xc8], edi
004425CD  7C 0E                           jl 0x1404425dd
004425CF  40 38 BC 24 9F 02 00 00         cmp byte ptr [rsp + 0x29f], dil
004425D7  0F 84 92 00 00 00               je 0x14044266f
004425DD  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
004425E6  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
004425ED  90                              nop
004425EE  48 8B B4 24 E0 00 00 00         mov rsi, qword ptr [rsp + 0xe0]
004425F6  41 8A D6                        mov dl, r14b
004425F9  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
004425FD  E8 BE F5 DC FF                  call 0x140211bc0
00442602  39 BC 24 C8 00 00 00            cmp dword ptr [rsp + 0xc8], edi
00442609  0F 9D C1                        setge cl
0044260C  40 38 BC 24 CE 00 00 00         cmp byte ptr [rsp + 0xce], dil
00442614  4C 8B 8C 24 C0 01 00 00         mov r9, qword ptr [rsp + 0x1c0]
0044261C  75 07                           jne 0x140442625
0044261E  4C 8B 8E 50 04 00 00            mov r9, qword ptr [rsi + 0x450]
00442625  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
0044262C  0B 84 24 F0 00 00 00            or eax, dword ptr [rsp + 0xf0]
00442633  40 88 7C 24 38                  mov byte ptr [rsp + 0x38], dil
00442638  88 4C 24 30                     mov byte ptr [rsp + 0x30], cl
0044263C  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00442640  48 8B 84 24 F8 00 00 00         mov rax, qword ptr [rsp + 0xf8]
00442648  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0044264D  45 33 C0                        xor r8d, r8d
00442650  33 D2                           xor edx, edx
00442652  48 8B CE                        mov rcx, rsi
00442655  E8 F6 5E 00 00                  call 0x140448550
0044265A  48 8B 4E 30                     mov rcx, qword ptr [rsi + 0x30]
0044265E  E8 AD D3 E1 FF                  call 0x14025fa10
00442663  E8 48 B2 E1 FF                  call 0x14025d8b0
00442668  8B 9C 24 A4 00 00 00            mov ebx, dword ptr [rsp + 0xa4]
0044266F  85 DB                           test ebx, ebx
00442671  78 3B                           js 0x1404426ae
00442673  39 BC 24 C8 00 00 00            cmp dword ptr [rsp + 0xc8], edi
0044267A  7D 32                           jge 0x1404426ae
0044267C  39 BC 24 94 02 00 00            cmp dword ptr [rsp + 0x294], edi
00442683  75 29                           jne 0x1404426ae
00442685  F7 86 C8 00 00 00 00 40 00 00   test dword ptr [rsi + 0xc8], 0x4000
0044268F  74 1D                           je 0x1404426ae
00442691  8B 94 24 B0 00 00 00            mov edx, dword ptr [rsp + 0xb0]
00442698  48 8D 8C 24 88 02 00 00         lea rcx, [rsp + 0x288]
004426A0  E8 DF FD 01 00                  call 0x140462484
004426A5  84 C0                           test al, al
004426A7  74 05                           je 0x1404426ae
004426A9  E8 F2 C1 FD FF                  call 0x14041e8a0
004426AE  45 84 FF                        test r15b, r15b
004426B1  74 26                           je 0x1404426d9
004426B3  4D 85 E4                        test r12, r12
004426B6  74 0A                           je 0x1404426c2
004426B8  33 D2                           xor edx, edx
004426BA  49 8B CC                        mov rcx, r12
004426BD  E8 AE 01 74 00                  call 0x140b82870
004426C2  4C 8B BC 24 68 01 00 00         mov r15, qword ptr [rsp + 0x168]
004426CA  4D 85 FF                        test r15, r15
004426CD  74 0A                           je 0x1404426d9
004426CF  33 D2                           xor edx, edx
004426D1  49 8B CF                        mov rcx, r15
004426D4  E8 97 01 74 00                  call 0x140b82870
004426D9  48 85 F6                        test rsi, rsi
004426DC  74 0D                           je 0x1404426eb
004426DE  BA 53 68 72 74                  mov edx, 0x74726853
004426E3  48 8B CE                        mov rcx, rsi
004426E6  E8 F5 51 EB FF                  call 0x1402f78e0
004426EB  48 8B 8C 24 80 01 00 00         mov rcx, qword ptr [rsp + 0x180]
004426F3  48 85 C9                        test rcx, rcx
004426F6  74 05                           je 0x1404426fd
004426F8  E8 A7 45 1C 00                  call 0x140606ca4
004426FD  48 8B 8C 24 88 01 00 00         mov rcx, qword ptr [rsp + 0x188]
00442705  48 85 C9                        test rcx, rcx
00442708  74 0F                           je 0x140442719
0044270A  45 8A C6                        mov r8b, r14b
0044270D  8A 94 24 A8 00 00 00            mov dl, byte ptr [rsp + 0xa8]
00442714  E8 37 C8 5E 00                  call 0x140a2ef50
00442719  4C 8B BC 24 F8 00 00 00         mov r15, qword ptr [rsp + 0xf8]
00442721  4D 85 FF                        test r15, r15
00442724  74 12                           je 0x140442738
00442726  45 33 C0                        xor r8d, r8d
00442729  8A 94 24 A8 00 00 00            mov dl, byte ptr [rsp + 0xa8]
00442730  49 8B CF                        mov rcx, r15
00442733  E8 58 2A 53 00                  call 0x140975190
00442738  40 38 BC 24 B8 00 00 00         cmp byte ptr [rsp + 0xb8], dil
00442740  74 0D                           je 0x14044274f
00442742  48 8B 8C 24 70 01 00 00         mov rcx, qword ptr [rsp + 0x170]
0044274A  E8 4D F7 06 00                  call 0x1404b1e9c
0044274F  48 8B 8C 24 98 01 00 00         mov rcx, qword ptr [rsp + 0x198]
00442757  48 85 C9                        test rcx, rcx
0044275A  74 07                           je 0x140442763
0044275C  33 D2                           xor edx, edx
0044275E  E8 0D 01 74 00                  call 0x140b82870
00442763  48 8B 8C 24 50 01 00 00         mov rcx, qword ptr [rsp + 0x150]
0044276B  E8 80 F2 EB FF                  call 0x1403019f0
00442770  8B C3                           mov eax, ebx
00442772  48 8B 8C 24 B8 02 00 00         mov rcx, qword ptr [rsp + 0x2b8]
0044277A  48 33 CC                        xor rcx, rsp
0044277D  E8 BE 9E 26 00                  call 0x1406ac640
00442782  48 81 C4 C0 02 00 00            add rsp, 0x2c0
00442789  41 5F                           pop r15
0044278B  41 5E                           pop r14
0044278D  41 5D                           pop r13
0044278F  41 5C                           pop r12
00442791  5F                              pop rdi
00442792  5E                              pop rsi
00442793  5B                              pop rbx
00442794  C3                              ret
00442795  CC                              int3
00442796  E8 35 78 45 00                  call 0x140899fd0
0044279B  90                              nop
0044279C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeAccessCheckByType(__int64 a1, __int64 a2, __int64 a3, int a4, __int64 a5, unsigned int a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, unsigned __int8 a12)
{
    __int64 result;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m120;
    unsigned __int64 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned int v_stack_m150;
    unsigned int v_stack_m154;
    unsigned int v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned int v_stack_m198;
    unsigned int v_stack_m19C;
    unsigned int v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned int v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned int v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned int v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned int v_stack_m1F4;
    unsigned int v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned int v_stack_m208;
    unsigned __int8 v_stack_m20C;
    unsigned int v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned int v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned __int8 v_stack_m22A;
    unsigned __int8 v_stack_m22B;
    unsigned __int8 v_stack_m22C;
    unsigned int v_stack_m230;
    unsigned int v_stack_m238;
    unsigned __int8 v_stack_m240;
    unsigned int v_stack_m248;
    unsigned __int8 v_stack_m24F;
    unsigned __int8 v_stack_m250;
    unsigned int v_stack_m254;
    unsigned __int8 v_stack_m258;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned __int8 v_stack_m288;
    unsigned __int8 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned __int8 v_stack_m2B0;
    unsigned int v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int8 v_stack_m59;
    unsigned __int8 v_stack_m5A;
    unsigned __int8 v_stack_m5B;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m64;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned int v_stack_mD4;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned __int8 v_stack_p60;

    v_rsp = (v_rsp) - (704);
    result = (*(unsigned __int64 *)(v_rip + 10263390)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m140 = a2;
    v_stack_m1C0 = (unsigned int)((unsigned int)(a6));
    v_stack_m180 = a7;
    v_stack_mB0 = a7;
    v_stack_mB8 = a10;
    v_stack_mC0 = a11;
    v_stack_mC8 = a9;
    v_stack_mA0 = a1;
    v_stack_m100 = a2;
    v_stack_mF8 = a3;
    v_stack_m248 = a4;
    v_stack_mA8 = a5;
    v_stack_m238 = (unsigned int)((unsigned int)(a6));
    v_stack_m19C = (unsigned int)((unsigned int)(a6));
    v_stack_mD0 = a7;
    v_stack_m1B0 = a8;
    v_stack_m148 = a9;
    v_stack_m1F0 = a10;
    v_stack_mF0 = a10;
    v_stack_m1E0 = a11;
    v_stack_mE8 = a11;
    v_rdi = 0;
    v_stack_m1A0 = 0;
    v_stack_m228 = 0;
    v_stack_m150 = 0;
    v_stack_m154 = 0;
    v_stack_m190 = 0;
    v_stack_m158 = 0;
    v_stack_m1D8 = 0;
    v_stack_m254 = 0;
    v_stack_m218 = 0;
    v_stack_m200 = 0;
    v_stack_m170 = 0;
    v_stack_m208 = 0;
    v_stack_m220 = 0;
    v_stack_m50 = v_xmm0;
    v_stack_m178 = 0;
    v_stack_m1C8 = 0;
    v_stack_m130 = v_xmm0;
    v_stack_m120 = v_xmm0;
    v_stack_mE0 = v_xmm0;
    v_stack_m1F8 = 0;
    v_stack_m20C = 0;
    v_stack_m1A8 = 0;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    v_stack_m1B8 = 0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = 0;
    v_stack_m188 = 0;
    v_stack_m240 = 0;
    v_stack_m24F = 0;
    v_stack_m1D0 = 0;
    v_stack_m258 = 0;
    v_stack_m160 = 0;
    v_stack_m22A = 0;
    v_stack_m22C = 0;
    v_stack_m22B = 0;
    v_stack_m138 = 0;
    v_stack_m168 = 0;
    v_stack_m230 = 0xC0000022ULL;
    v_stack_m1E8 = 0;
    v_stack_m198 = 0;
    v_stack_m250 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) != 0) goto loc_00440E67;
    goto loc_00440E74;
loc_00440E67:
    result = v_rsi;
    if (a9 < v_rsi) { result = a9; }
loc_00440E74:
    v_stack_m1E8 = (unsigned int)((unsigned int)(*(unsigned int *)(result)));
    goto loc_00440F20;
loc_00440F20:
    if (sign_flag) goto loc_00442772;
    result = (unsigned int)(((unsigned int)(v_stack_m254)) | (0xFFFFFFFFULL));
    v_stack_m180 = (unsigned int)(result);
    v_stack_m168 = (unsigned int)(result);
    if (v_stack_m250 != 0) goto loc_00440F57;
    *(unsigned int *)(a11) = 0;
    *(unsigned int *)(a10) = (unsigned int)((unsigned int)(v_stack_m248));
    result = 0;
    goto loc_00442772;
loc_00440F57:
    if (a12 == 0) goto loc_00440FB6;
    if ((unsigned int)((unsigned int)(v_stack_m238)) != 0) goto loc_00440F7D;
    v_stack_m254 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_00441033;
loc_00440F7D:
    result = ProbeForWrite(a11, (unsigned int)(0xC000000DULL) * 4, 4, a10);
    result = ProbeForWrite(v_stack_m1F0, (unsigned int)(0xC000000DULL) * 4, 4, a10);
    goto loc_00440FD2;
loc_00440FB6:
    a1 = v_rsi;
    if (a11 < v_rsi) { a1 = a11; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    a1 = v_rsi;
    if (a10 < v_rsi) { a1 = (unsigned int)(0xC000000DULL) * 4; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
loc_00440FD2:
    a1 = v_rsi;
    if (v_stack_m148 < v_rsi) { a1 = a9; }
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(a1)));
    result = ProbeForWrite(v_stack_m1B0, (unsigned int)(v_stack_m1E8), 4, a10);
    if (v_stack_m1B0 == 0) goto loc_0044100B;
    if (v_stack_m1E8 >= 20) {
        *(unsigned int *)(v_stack_m1B0) = 0;
    }
    if ((((unsigned __int8)(a7)) & (3)) != 0) goto loc_00442796;
    if (a7 < v_rsi) { v_rsi = v_stack_m180; }
    v_stack_m50 = v_xmm0;
loc_00441033:
    goto loc_00441086;
loc_00441086:
    if (sign_flag) goto loc_00442772;
    if (((v_stack_m248) & (0xF0000000ULL)) == 0) goto loc_004410B3;
    goto loc_0044255F;
loc_004410B3:
    v_stack_m2C8 = v_stack_m138;
    v_stack_m2D0 = v_stack_m22A;
    v_stack_m2D8 = v_stack_m218;
    result = SepReferenceTokenByHandle(a3, 8, v_stack_m250, a10);
    v_stack_m254 = (unsigned int)(result);
    if (!sign_flag) goto loc_00441112;
    v_stack_m218 = 0;
    goto loc_00442566;
loc_00441112:
    a1 = ((a3 + 6) <= 2) ? 1 : 0;
    if ((unsigned int)(a1) != 0) goto loc_00441151;
    if ((*(unsigned int *)(v_stack_m218 + 192)) == 2) goto loc_0044113E;
    goto loc_0044255F;
loc_0044113E:
    if ((*(unsigned int *)(v_stack_m218 + 196)) >= 1) goto loc_00441151;
    goto loc_0044255F;
loc_00441151:
    result = SeCaptureObjectTypeList(v_stack_mA8, (unsigned int)(v_stack_m238), (unsigned __int8)(v_stack_m250), v_stack_m178);
    v_stack_m254 = (unsigned int)(result);
    if (sign_flag) goto loc_00442566;
    v_stack_m2D8 = v_stack_m200;
    a4 = 0;
    result = SeCaptureSecurityDescriptor(v_stack_mA0, (unsigned __int8)(v_stack_m250), 1, a4);
    v_stack_m254 = (unsigned int)(result);
    if (sign_flag) goto loc_00442566;
    if (v_stack_m200 == 0) goto loc_0044255A;
    if (!sign_flag) goto loc_004411EE;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m200 + 4))) == 0) goto loc_0044255A;
    result = ((unsigned int)(*(unsigned int *)(v_stack_m200 + 4))) + (v_stack_m200);
    goto loc_004411FA;
loc_004411EE:
loc_004411FA:
    if (*(unsigned __int64 *)(v_stack_m200 + 8) == 0) goto loc_0044255A;
    if (!sign_flag) goto loc_00441221;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m200 + 8))) == 0) goto loc_0044255A;
    result = ((unsigned int)(*(unsigned int *)(v_stack_m200 + 8))) + (v_stack_m200);
    goto loc_0044122D;
loc_00441221:
loc_0044122D:
    if (*(unsigned __int64 *)(v_stack_m200 + 16) == 0) goto loc_0044255A;
    result = v_stack_m138;
    if (v_stack_m22A == 0) {
        result = *(unsigned __int64 *)(v_stack_m218 + 1104);
    }
    v_stack_m2C8 = v_stack_m180;
    v_stack_m2D0 = 1;
    v_stack_m2D8 = result;
    a3 = 0;
    result = SepTrustLevelCheck(v_stack_m180, v_stack_m200, a3, v_stack_m218);
    v_stack_m254 = (unsigned int)(result);
    if (sign_flag) goto loc_00442566;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m248)))))) & (v_stack_m180));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m248)))))) goto loc_00441458;
    v_stack_m2D8 = v_stack_m168;
    result = SepFilterCheck(v_stack_m200, v_stack_m1A8, v_stack_m218, 1);
    v_stack_m254 = (unsigned int)(result);
    if (sign_flag) goto loc_00442566;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m248)))))) & (v_stack_m168));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m248)))))) goto loc_0044144E;
    v_stack_m2D0 = v_stack_mE0;
    v_stack_m2D8 = 1;
    a3 = 0;
    result = SepMandatoryIntegrityCheck(v_stack_m50, v_stack_m200, a3, v_stack_m218);
    v_stack_m254 = (unsigned int)(result);
    if (sign_flag) goto loc_00442566;
    v_stack_m1F8 = 0;
    result = SepMandatoryToDiscretionary(v_stack_mE0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m248))), a3, v_stack_m218);
    if (sign_flag) goto loc_00441358;
    if (condition_is_above_or_equal) goto loc_0044137F;
loc_00441358:
    v_r15 = 0;
    if (((*(unsigned int *)(v_stack_m218 + 200)) & (0x4000ULL)) != 0) {
        v_r15 = 0;
        if (v_stack_mD4 <= 0x2000ULL) { v_r15 = 1; }
        v_stack_m1F8 = (unsigned int)(v_r15);
    }
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(v_stack_mE0, (unsigned int)((unsigned int)((unsigned int)(v_stack_m248))), a3, v_stack_m218);
    if ((unsigned int)(result) == 0) goto loc_004413EB;
    v_stack_m2D0 = v_stack_m198;
    v_stack_m2D8 = (unsigned int)((unsigned int)(v_stack_m248));
    a2 = 0;
    result = SepMandatoryAccessCheck(v_stack_m200, a2, v_stack_m218, 1);
    if (sign_flag) goto loc_004413CC;
    v_r12 = (unsigned int)(((unsigned int)(v_stack_m248)) & (v_stack_m198));
    if ((((unsigned int)(v_r12)) & (0xFDFFFFFFULL)) == 0) goto loc_004413EB;
loc_004413CC:
    *(unsigned int *)(v_stack_m1F0) = 0;
    *(unsigned int *)(v_stack_m1E0) = (unsigned int)((unsigned int)(0xC00001C0ULL));
    goto loc_0044255F;
loc_004413EB:
    if (!sign_flag) goto loc_004413F4;
    if ((unsigned __int8)(v_r15) == 0) goto loc_00441446;
loc_004413F4:
    v_stack_m2D0 = (unsigned __int8)(v_stack_m250);
    v_stack_m2D8 = v_stack_m1C8;
    a3 = 0;
    result = SePrivilegePolicyCheck(v_stack_m248, v_stack_m208, a3, v_stack_m218);
    if (v_stack_m248 != 0) goto loc_00441446;
    if (v_stack_m208 == 0) goto loc_00441446;
    goto loc_00441479;
loc_00441446:
    goto loc_00441471;
loc_0044144E:
    v_stack_m22B = 1;
    goto loc_00441460;
loc_00441458:
    v_stack_m22C = 1;
loc_00441460:
loc_00441471:
loc_00441479:
    if (!sign_flag) goto loc_00441518;
    if ((unsigned __int8)((unsigned int)(v_stack_m1F8)) != 0) goto loc_00441518;
    if (a12 == 0) goto loc_004414C7;
loc_004414A9:
    v_stack_m210 = 0;
    if (0 >= v_stack_m238) goto loc_004414D4;
    *(unsigned int *)(v_stack_m1E0 + 0 * 4) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC0000022ULL))));
    *(unsigned int *)(v_stack_m1F0 + 0 * 4) = 0;
    a1 = (unsigned int)((0) + (1));
    goto loc_004414A9;
loc_004414C7:
    *(unsigned int *)(v_stack_m1E0) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC0000022ULL))));
    *(unsigned int *)(v_stack_m1F0) = 0;
loc_004414D4:
    v_stack_m230 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(0xC0000022ULL))));
    v_stack_m254 = 0;
    goto loc_00442576;
loc_00441518:
    if (v_stack_m1C8 == 0) goto loc_004415FC;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1C8)) + (unsigned int)(*(unsigned int *)(v_stack_m1C8)) * 2) << (2));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1C8))) == 0) {
        a2 = 8;
    }
    if (((unsigned int)(a2)) <= v_stack_m1E8) goto loc_0044159A;
    result = (unsigned int)((result) + (8));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1C8))) == 0) { result = 8; }
    *(unsigned int *)(v_stack_m148) = (unsigned int)(result);
    v_stack_m254 = (unsigned int)((unsigned int)(0xC0000023ULL));
    goto loc_0044158B;
loc_0044158B:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m1C8, a2, 8, v_stack_m1E0);
    goto loc_00442566;
loc_0044159A:
    result = (unsigned int)((result) + (8));
    if ((unsigned int)(v_stack_m1C8) == 0) { result = 8; }
    result = memcpy(v_stack_m1B0, v_stack_m1C8, (unsigned int)((unsigned int)(result)), v_stack_m1E0);
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m1C8, a2, (unsigned int)((unsigned int)(result)), v_stack_m1E0);
    goto loc_00441668;
loc_004415FC:
    if (v_stack_m1E8 >= 20) goto loc_0044165C;
    *(unsigned int *)(v_stack_m148) = 20;
    v_stack_m254 = (unsigned int)((unsigned int)(0xC0000023ULL));
    goto loc_00442576;
loc_0044165C:
loc_00441668:
    if (v_stack_m140 == 0) goto loc_004416B0;
    v_stack_m2C8 = v_stack_m170;
    v_stack_m2D0 = 1;
    result = SeCaptureSid(v_stack_m140, v_stack_m250, (unsigned int)((unsigned int)(result)), v_stack_m1E0);
    v_stack_m254 = (unsigned int)(result);
    if (!sign_flag) goto loc_004416B0;
    v_stack_m170 = 0;
    goto loc_00442566;
loc_004416B0:
    result = SeCaptureSubjectContext(v_stack_m130, v_stack_m250, (unsigned int)((unsigned int)(result)), v_stack_m1E0);
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m218 + 48), 1, (unsigned int)((unsigned int)(result)), v_stack_m1E0);
    result = SepTokenIsOwner(v_stack_m218, v_stack_m200, (unsigned int)((unsigned int)(result)), v_stack_m1E0);
    v_stack_m258 = (unsigned __int8)(result);
    if ((*(unsigned __int8 *)(v_rip + 10270126)) != 0) goto loc_004417CD;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m218 + 200)))) & (32)) != 0) goto loc_004417CD;
    if (*(unsigned __int64 *)(v_stack_m218 + 216) == 0) goto loc_004417CD;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m218 + 216) + 40)))) & (32)) == 0) goto loc_004417CD;
    if (a12 == 0) goto loc_0044176E;
loc_00441750:
    v_stack_m210 = 0;
    if (0 >= v_stack_m238) goto loc_0044177B;
    *(unsigned int *)(v_stack_m1E0 + 0 * 4) = (unsigned int)(v_stack_m228);
    *(unsigned int *)(v_stack_m1F0 + 0 * 4) = 0;
    a1 = (unsigned int)((0) + (1));
    goto loc_00441750;
loc_0044176E:
    *(unsigned int *)(v_stack_m1E0) = (unsigned int)(v_stack_m228);
    *(unsigned int *)(v_stack_m1F0) = 0;
loc_0044177B:
    v_stack_m230 = (unsigned int)(v_stack_m228);
    v_stack_m254 = 0;
    goto loc_004417AD;
loc_004417AD:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m218 + 48), v_stack_m1F0, (unsigned int)((unsigned int)(result)), v_stack_m1E0);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m218 + 48), v_stack_m1F0, (unsigned int)((unsigned int)(result)), v_stack_m1E0);
    result = SeReleaseSubjectContext(v_stack_m130, v_stack_m1F0, (unsigned int)((unsigned int)(result)), v_stack_m1E0);
    goto loc_0044256E;
loc_004417CD:
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11285234)) == 0) goto loc_00441879;
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_m200 + 2))) & (16)) == 0) goto loc_00441872;
    if (((unsigned __int8)(v_cr8)) >= 2) goto loc_00441872;
    if (!sign_flag) goto loc_0044181A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m200 + 12))) != 0) goto loc_00441810;
    v_stack_m1B8 = 0;
    goto loc_00441872;
loc_00441810:
    result = ((unsigned int)(*(unsigned int *)(v_stack_m200 + 12))) + (v_stack_m200);
    goto loc_00441826;
loc_0044181A:
loc_00441826:
    v_stack_m1B8 = *(unsigned __int64 *)(v_stack_m200 + 24);
    if (*(unsigned __int64 *)(v_stack_m200 + 24) == 0) goto loc_00441872;
    result = SepGetScopedPolicySid(*(unsigned __int64 *)(v_stack_m200 + 24), v_stack_m1F0, (unsigned int)((unsigned int)(result)), v_stack_m1E0);
    if (result != 0) {
        a2 = v_stack_m188;
        a1 = result;
        result = SepRmReferenceFindCap(a1, a2, (unsigned int)((unsigned int)(result)), v_stack_m1E0);
        a2 = v_stack_m188;
        if (sign_flag) { a2 = *(unsigned __int64 *)(v_rip + 12150926); }
        v_stack_m188 = a2;
        v_stack_m240 = 1;
    }
loc_00441879:
    if (((v_stack_m248) & (0x2060000ULL)) == 0) goto loc_00441921;
    if ((unsigned __int8)(v_stack_m258) == 0) goto loc_00441921;
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_m200 + 2))) & (4)) != 0) goto loc_004418A8;
loc_004418A3:
    goto loc_004418C7;
loc_004418A8:
    if (!sign_flag) goto loc_004418C3;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m200 + 16))) == 0) goto loc_004418A3;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m200 + 16))))) + (v_stack_m200);
    goto loc_004418C7;
loc_004418C3:
loc_004418C7:
    a1 = 0;
    result = RtlpOwnerAcesPresent(a1, *(unsigned __int64 *)(v_stack_m200 + 32), (unsigned int)((unsigned int)(result)), v_stack_m1E0);
    if ((unsigned __int8)(result) != 0) goto loc_00441921;
    if (((v_stack_m248) & (0x2000000ULL)) == 0) goto loc_004418EF;
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m208)) | ((unsigned int)((unsigned int)(0x60000ULL))));
    goto loc_00441906;
loc_004418EF:
    result = (unsigned int)(((unsigned int)(v_stack_m248)) & ((unsigned int)((unsigned int)(0x60000ULL))));
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(result))) | (v_stack_m208));
loc_00441906:
    v_stack_m220 = (unsigned int)(result);
    v_stack_m208 = (unsigned int)(v_rbx);
    goto loc_00441928;
loc_00441921:
loc_00441928:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline((unsigned int)(0x60000ULL), *(unsigned __int64 *)(v_stack_m200 + 32), (unsigned int)((unsigned int)(result)), v_stack_m1E0);
    if ((unsigned int)(result) == 0) goto loc_00441A3A;
    if (v_stack_m248 != 0) goto loc_00441B39;
    if (v_stack_m240 == 0) goto loc_00441955;
    if ((unsigned __int8)(v_stack_m258) == 0) goto loc_00441B39;
loc_00441955:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m218 + 200))) & (0x6000ULL));
    if (((unsigned int)(result)) == 0x2000ULL) goto loc_0044197C;
    if (v_stack_m220 != 0) goto loc_00441B41;
loc_0044197C:
    if (a12 == 0) goto loc_004419D9;
loc_004419A3:
    v_stack_m210 = 0;
    if (0 >= ((unsigned int)((unsigned int)(v_stack_m238)))) goto loc_00441A08;
    if ((unsigned int)((unsigned int)(v_stack_m208)) != 0) goto loc_004419C6;
    *(unsigned int *)(v_stack_mE8 + 0 * 4) = (unsigned int)(v_stack_m228);
    v_stack_m230 = (unsigned int)(v_stack_m228);
    *(unsigned int *)(v_stack_mF0 + 0 * 4) = 0;
    goto loc_004419D4;
loc_004419C6:
    *(unsigned int *)(v_stack_mE8 + 0 * 4) = 0;
    v_stack_m230 = 0;
    *(unsigned int *)(v_stack_mF0 + 0 * 4) = (unsigned int)((unsigned int)(v_stack_m208));
loc_004419D4:
    result = (unsigned int)((0) + (1));
    goto loc_004419A3;
loc_004419D9:
    if ((unsigned int)((unsigned int)(v_stack_m208)) != 0) goto loc_004419FC;
    *(unsigned int *)(v_stack_m1E0) = (unsigned int)(v_stack_m228);
    v_stack_m230 = (unsigned int)(v_stack_m228);
    *(unsigned int *)(v_stack_m1F0) = 0;
    goto loc_00441A08;
loc_004419FC:
    *(unsigned int *)(v_stack_m1E0) = 0;
    v_stack_m230 = 0;
    *(unsigned int *)(v_stack_m1F0) = (unsigned int)((unsigned int)(v_stack_m208));
loc_00441A08:
    v_stack_m254 = 0;
    goto loc_004417AD;
loc_00441A3A:
    if (v_stack_m248 != 0) goto loc_00441B39;
    if (v_stack_m240 == 0) goto loc_00441A5A;
    if ((unsigned __int8)(v_stack_m258) == 0) goto loc_00441B39;
loc_00441A5A:
    if (((*(unsigned int *)(v_stack_m218 + 200)) & (0x2000ULL)) != 0) goto loc_00441A7B;
    if (v_stack_m220 != 0) goto loc_00441B41;
loc_00441A7B:
    if (a12 == 0) goto loc_00441AD8;
loc_00441AA2:
    v_stack_m210 = 0;
    if (0 >= ((unsigned int)((unsigned int)(v_stack_m238)))) goto loc_00441B07;
    if (0 != 0) goto loc_00441AC5;
    *(unsigned int *)(v_stack_mE8 + 0 * 4) = (unsigned int)(v_stack_m228);
    v_stack_m230 = (unsigned int)(v_stack_m228);
    *(unsigned int *)(v_stack_mF0 + 0 * 4) = 0;
    goto loc_00441AD3;
loc_00441AC5:
    *(unsigned int *)(v_stack_mE8 + 0 * 4) = 0;
    v_stack_m230 = 0;
    *(unsigned int *)(v_stack_mF0 + 0 * 4) = 0;
loc_00441AD3:
    result = (unsigned int)((0) + (1));
    goto loc_00441AA2;
loc_00441AD8:
    if (0 != 0) goto loc_00441AFB;
    *(unsigned int *)(v_stack_m1E0) = (unsigned int)(v_stack_m228);
    v_stack_m230 = (unsigned int)(v_stack_m228);
    *(unsigned int *)(v_stack_m1F0) = 0;
    goto loc_00441B07;
loc_00441AFB:
    *(unsigned int *)(v_stack_m1E0) = 0;
    v_stack_m230 = 0;
    *(unsigned int *)(v_stack_m1F0) = 0;
loc_00441B07:
    v_stack_m254 = 0;
    goto loc_004417AD;
loc_00441B39:
loc_00441B41:
    if (a12 == 0) goto loc_00441BC0;
    result = ExAllocatePool2(256, (unsigned int)(v_stack_m19C) * 8, (unsigned int)(0x61476553ULL), v_stack_m1E0);
    v_stack_m228 = result;
    if (result != 0) goto loc_00441BB3;
loc_00441B7F:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m218 + 48), (unsigned int)(v_stack_m19C) * 8, (unsigned int)(0x61476553ULL), v_stack_m1E0);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m218 + 48), (unsigned int)(v_stack_m19C) * 8, (unsigned int)(0x61476553ULL), v_stack_m1E0);
    result = SeReleaseSubjectContext(v_stack_m130, (unsigned int)(v_stack_m19C) * 8, (unsigned int)(0x61476553ULL), v_stack_m1E0);
    v_stack_m254 = (unsigned int)((unsigned int)(0xC000009AULL));
loc_00441BA6:
    goto loc_00442576;
loc_00441BB3:
    goto loc_00441BD8;
loc_00441BC0:
    v_stack_m228 = v_stack_m1A0;
loc_00441BD8:
    v_stack_m70 = (unsigned int)((unsigned int)(v_stack_m220));
    v_stack_m268 = 0;
    v_stack_m270 = 0;
    v_stack_m278 = v_stack_m1A8;
    v_stack_m280 = v_stack_m70;
    v_stack_m288 = (unsigned __int8)(v_stack_m258);
    v_stack_m290 = a12;
    v_stack_m298 = v_stack_m150;
    v_stack_m2A0 = 0;
    v_stack_m2A8 = v_stack_m1A0;
    v_stack_m2B0 = (unsigned __int8)(v_stack_m250);
    v_stack_m2B8 = (unsigned int)((unsigned int)(0xC000009AULL));
    v_stack_m2C0 = v_stack_m50;
    v_stack_m2C8 = (unsigned int)((unsigned int)(v_stack_m238));
    v_stack_m2D0 = v_stack_m178;
    v_stack_m2D8 = (unsigned int)((unsigned int)(v_stack_m248));
    result = SepAccessCheck(v_stack_m200, v_stack_m170, v_stack_m120, v_stack_m218);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11284015)) == 0) goto loc_00442187;
    if ((*(unsigned int *)(v_stack_m150)) < 0) goto loc_00442187;
    if (v_stack_m240 == 0) goto loc_00442187;
    if (a12 == 0) goto loc_00441D02;
    result = ExAllocatePool2(256, a12, (unsigned int)(0x61476553ULL), v_stack_m218);
    v_stack_m190 = result;
    if (result != 0) goto loc_00441CED;
    goto loc_00441B7F;
loc_00441CED:
    v_stack_m1D8 = result + (unsigned int)(v_stack_m19C) * 4;
    goto loc_00441D22;
loc_00441D02:
    v_stack_m190 = v_stack_m154;
    v_stack_m1D8 = v_stack_m158;
loc_00441D22:
    v_stack_m1C8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m150)));
    v_stack_m220 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1A0)));
    v_stack_m1F4 = 0;
    if ((unsigned int)((unsigned int)(v_stack_m238)) == 0) goto loc_00441D97;
    result = SepCopyObjectTypeList(v_stack_m178, (unsigned int)((unsigned int)((unsigned int)(v_stack_m238))), v_stack_m160, v_stack_m218);
    v_stack_m254 = (unsigned int)(result);
    if (!sign_flag) goto loc_00441D80;
    goto loc_00441BA6;
loc_00441D80:
loc_00441D97:
    v_stack_m1B0 = 0;
    if ((*(unsigned int *)(v_stack_m188 + 60)) <= 0) goto loc_0044214B;
loc_00441DC1:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m188 + 0 * 8 + 64) + 24)) == 0) goto loc_00441F90;
    result = v_stack_m188;
    v_rbx = (unsigned int)(v_stack_m1F4);
    if (v_stack_m1A8 == 0) {
        a2 = v_stack_m1A8;
        a1 = v_stack_m1B8;
        result = AuthzBasepInitializeResourceClaimsFromSacl(a1, a2, v_stack_m1A8, v_stack_m218);
        v_rbx = (unsigned __int8)((unsigned int)(v_stack_m1F4));
        if (sign_flag) { v_rbx = 1; }
        v_stack_m1F4 = (unsigned int)(v_rbx);
        a3 = v_stack_m1A8;
    }
    if (*(unsigned __int64 *)(v_stack_m218 + 1096) == 0) goto loc_00441E24;
    goto loc_00441E27;
loc_00441E24:
loc_00441E27:
    if (*(unsigned __int64 *)(v_stack_m218 + 1096) == 0) goto loc_00441E35;
    goto loc_00441E38;
loc_00441E35:
loc_00441E38:
    if (*(unsigned __int64 *)(v_stack_m218 + 1096) == 0) goto loc_00441E46;
    goto loc_00441E49;
loc_00441E46:
loc_00441E49:
    if (*(unsigned __int64 *)(v_stack_m218 + 1096) == 0) goto loc_00441E57;
    goto loc_00441E5A;
loc_00441E57:
loc_00441E5A:
    v_stack_m2A0 = v_stack_m1D0;
    v_stack_m2A8 = 0;
    v_stack_m2B0 = 1;
    v_stack_m2B8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m188 + 0 * 8 + 64) + 16)));
    v_stack_m2C0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m188 + 0 * 8 + 64) + 24);
    v_stack_m2C8 = 0;
    v_stack_m2D0 = 0;
    v_stack_m2D8 = 0;
    result = AuthzBasepEvaluateAceCondition(v_stack_m218, *(unsigned __int64 *)(v_stack_m218 + 776), a3, 0);
    v_stack_m254 = (unsigned int)(result);
    if (v_stack_m1D0 == 1) goto loc_00441F90;
    if (sign_flag) goto loc_00442167;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m218 + 200)))) & (16)) == 0) goto loc_00441F77;
    if (*(unsigned __int64 *)(v_stack_m218 + 1096) == 0) goto loc_00441EE2;
    goto loc_00441EE5;
loc_00441EE2:
loc_00441EE5:
    if (*(unsigned __int64 *)(v_stack_m218 + 1096) == 0) goto loc_00441EF3;
    goto loc_00441EF6;
loc_00441EF3:
loc_00441EF6:
    if (*(unsigned __int64 *)(v_stack_m218 + 1096) == 0) goto loc_00441F04;
    goto loc_00441F07;
loc_00441F04:
loc_00441F07:
    if (*(unsigned __int64 *)(v_stack_m218 + 1096) == 0) goto loc_00441F15;
    goto loc_00441F18;
loc_00441F15:
loc_00441F18:
    v_stack_m2A0 = v_stack_m1D0;
    v_stack_m2A8 = 1;
    v_stack_m2B0 = 1;
    v_stack_m2B8 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m188 + 0 * 8 + 64) + 16)));
    v_stack_m2C0 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m188 + 0 * 8 + 64) + 24);
    v_stack_m2C8 = 0;
    v_stack_m2D0 = 0;
    v_stack_m2D8 = 0;
    result = AuthzBasepEvaluateAceCondition(v_stack_m218, *(unsigned __int64 *)(v_stack_m218 + 776), v_stack_m1A8, 0);
    v_stack_m254 = (unsigned int)(result);
    if (sign_flag) goto loc_00442167;
loc_00441F77:
    if ((unsigned __int8)((unsigned int)(v_stack_m1F4)) != 0) goto loc_00441F90;
    if (v_stack_m1D0 != 1) goto loc_00442155;
loc_00441F90:
    result = SepBuildCapeSecurityDescriptor(v_stack_m98, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m188 + 0 * 8 + 64) + 32), v_stack_m1B8, 0);
    v_stack_m254 = (unsigned int)(result);
    if (sign_flag) goto loc_00442167;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m188 + 0 * 8 + 64) + 48))))) == 0) goto loc_00441FDE;
    v_r12 = (unsigned int)(v_stack_m248);
    if (!(condition_is_below)) {
        v_r12 = (unsigned int)(((unsigned int)(v_stack_m248)) | (v_stack_m208));
    }
    goto loc_00441FE5;
loc_00441FDE:
loc_00441FE5:
    v_stack_m268 = 0;
    v_stack_m270 = 0;
    v_stack_m278 = v_stack_m1A8;
    v_stack_m280 = v_stack_m70;
    v_stack_m288 = (unsigned __int8)(v_stack_m258);
    v_stack_m290 = a12;
    v_stack_m298 = v_stack_m1D8;
    v_stack_m2A0 = 0;
    v_stack_m2A8 = v_stack_m190;
    v_stack_m2B0 = (unsigned __int8)(v_stack_m250);
    v_stack_m2B8 = (unsigned int)((unsigned int)(v_stack_m208));
    v_stack_m2C0 = v_stack_m50;
    v_stack_m2C8 = (unsigned int)((unsigned int)(v_stack_m238));
    v_stack_m2D0 = v_stack_m160;
    v_stack_m2D8 = (unsigned int)(v_r12);
    result = SepAccessCheck(v_stack_m98, v_stack_m170, v_stack_m120, v_stack_m218);
    if (v_stack_m24F != 0) goto loc_004420B2;
    goto loc_004420BD;
loc_004420B2:
    v_r11 = (unsigned int)(((unsigned int)(v_stack_m220)) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m190)))));
loc_004420BD:
    v_stack_m220 = (unsigned int)(v_r11);
    if ((unsigned int)(v_r11) != 0) goto loc_004420D2;
    goto loc_004420DD;
loc_004420D2:
loc_004420DD:
    v_stack_m1C8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1D8)));
    v_stack_m24F = 1;
    result = v_stack_m1D8;
    if (v_stack_m160 != 0) {
        a3 = (unsigned int)((unsigned int)(v_stack_m238));
        a2 = v_stack_m160;
        a1 = v_stack_m178;
        result = SepMergeObjectTypeListAccesses(a1, a2, a3, v_stack_m218);
    }
    if (sign_flag) goto loc_00442143;
loc_00442121:
    result = (unsigned int)(((unsigned int)(v_stack_m1B0)) + (1));
    v_stack_m1B0 = (unsigned int)(result);
    if (((unsigned int)(result)) < (*(unsigned int *)(v_stack_m188 + 60))) goto loc_00441DC1;
loc_00442143:
loc_0044214B:
    *(unsigned int *)(v_stack_m150) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1D8)));
    goto loc_0044218F;
loc_00442155:
    goto loc_00442121;
loc_00442167:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m218 + 48), a2, a3, v_stack_m218);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m218 + 48), a2, a3, v_stack_m218);
    result = SeReleaseSubjectContext(v_stack_m130, a2, a3, v_stack_m218);
    goto loc_00442566;
loc_00442187:
loc_0044218F:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m218 + 48), a2, a3, v_stack_m218);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m218 + 48), a2, a3, v_stack_m218);
    result = SeReleaseSubjectContext(v_stack_m130, a2, a3, v_stack_m218);
    v_rbx = (unsigned int)(((unsigned int)(v_stack_m248)) & (0x2000000ULL));
    if (condition_is_equal) goto loc_00442252;
    if (v_stack_m1F8 == 0) goto loc_004421EC;
    if (v_stack_m5A != 0) goto loc_00442221;
    if (v_stack_m5B != 0) goto loc_00442221;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m218 + 200))) & ((unsigned int)((unsigned int)(0x3000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x3000000ULL)))) {
        result = a12;
        result = (unsigned __int8)(-(result));
        a1 = (unsigned int)(((unsigned int)(0x3000000ULL)) & (v_stack_m1C0));
        v_stack_m2D0 = (unsigned int)(a1);
        v_stack_m2D8 = 0;
        a4 = v_stack_m150;
        a3 = v_stack_m228;
        a2 = v_stack_m248;
        a1 = v_stack_mE0;
        result = SepConstrainByMandatory(a1, a2, a3, a4);
    }
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_004423A8;
    result = (unsigned int)(~((unsigned int)(v_stack_m198)));
    goto loc_004423A8;
loc_00442252:
    if (v_stack_m1F8 == 0) goto loc_00442399;
    if (v_stack_m5A != 0) goto loc_00442399;
    if (v_stack_m5B != 0) goto loc_00442399;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_m238) + 200))) & ((unsigned int)((unsigned int)(0x3000000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x3000000ULL)))) goto loc_00442302;
    if (v_stack_m64 != 0) goto loc_00442302;
    v_stack_m59 = 1;
    if (a12 == 0) goto loc_004422E7;
    if ((unsigned int)((unsigned int)(v_stack_m238)) == 0) goto loc_004423A8;
    a1 = (unsigned int)(((unsigned int)(v_stack_m248)) | (v_stack_m208));
    a2 = (v_stack_m150) - (v_stack_m228);
loc_004422D4:
    *(unsigned int *)(a2 + v_stack_m228 * 1) = 0;
    *(unsigned int *)(v_stack_m228) = (unsigned int)(a1);
    a3 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m238)))) - (1);
    if (condition_is_not_equal) goto loc_004422D4;
    goto loc_004423A8;
loc_004422E7:
    *(unsigned int *)(v_stack_m150) = 0;
    result = (unsigned int)(((unsigned int)(v_stack_m248)) | (v_stack_m208));
    *(unsigned int *)(v_stack_m228) = (unsigned int)(result);
    goto loc_004423A1;
loc_00442302:
    if (a12 == 0) goto loc_00442343;
loc_00442321:
    v_stack_m210 = 0;
    if (0 >= v_stack_m238) goto loc_00442354;
    *(unsigned int *)(v_stack_m1E0 + 0 * 4) = 0xC0000022ULL;
    *(unsigned int *)(v_stack_m1F0 + 0 * 4) = 0;
    a1 = (unsigned int)((0) + (1));
    goto loc_00442321;
loc_00442343:
    *(unsigned int *)(v_stack_m1E0) = 0xC0000022ULL;
    *(unsigned int *)(v_stack_m1F0) = 0;
loc_00442354:
    v_stack_m230 = 0xC0000022ULL;
    v_stack_m254 = 0;
    goto loc_00442576;
loc_00442399:
loc_004423A1:
loc_004423A8:
    result = v_stack_m1F0;
    v_rbx = 0;
    v_r12 = v_stack_m228;
    if (0 != 0) {
        result = a12;
        result = (unsigned __int8)(-(result));
        v_rbx = (unsigned int)((0) & (v_stack_m1C0));
        result = v_stack_m22C;
        v_stack_m2C8 = result;
        v_stack_m2D0 = (unsigned int)(v_rbx);
        v_stack_m2D8 = 0;
        a4 = v_stack_m150;
        a3 = v_stack_m228;
        a2 = v_stack_m248;
        a1 = v_stack_m180;
        result = SepConstrainByConstraintMask(a1, a2, a3, a4);
        a2 = v_stack_m22B;
        v_stack_m2C8 = a2;
        v_stack_m2D0 = (unsigned int)(v_rbx);
        v_stack_m2D8 = 0;
        a4 = v_stack_m150;
        a3 = v_stack_m228;
        a2 = v_stack_m248;
        a1 = v_stack_m168;
        result = SepConstrainByConstraintMask(a1, a2, a3, a4);
        v_r12 = v_stack_m228;
    }
    *(unsigned int *)(v_stack_m1E0) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m150)));
    *(unsigned int *)(v_stack_m1F0) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r12)));
    v_stack_m230 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m150)));
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11282033)) == 0) goto loc_00442495;
    if ((unsigned __int8)(v_stack_m24F) == 0) goto loc_00442495;
    result = *(unsigned __int8 *)(v_rip + 11282033);
    if ((*(unsigned int *)(v_stack_m150)) >= 0) {
        result = *(unsigned int *)(v_stack_m1D8);
        *(unsigned int *)(v_stack_m1E0) = (unsigned int)(result);
        result = v_stack_m190;
        a1 = *(unsigned int *)(result);
        result = *(unsigned int *)(v_stack_m1D8);
        v_stack_m230 = (unsigned int)(result);
        a1 = v_stack_m24F;
    }
    if (a12 == 0) goto loc_004424FA;
loc_0044249D:
    v_stack_m210 = 1;
    if (1 >= ((unsigned int)((unsigned int)(v_stack_m238)))) goto loc_004424FA;
    *(unsigned int *)(v_stack_m1E0 + 1 * 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m150 + 1 * 4)));
    *(unsigned int *)(v_stack_m1F0 + 1 * 4) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + 1 * 4)));
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 11281924)) == 0) goto loc_004424E7;
    if ((unsigned __int8)(a1) == 0) goto loc_004424E7;
    result = *(unsigned __int8 *)(v_rip + 11281924);
    if ((*(unsigned int *)(v_stack_m150 + 1 * 4)) >= 0) {
        result = *(unsigned int *)(v_stack_m1D8 + 1 * 4);
        *(unsigned int *)(v_stack_m1E0 + 1 * 4) = (unsigned int)(result);
        result = v_stack_m190;
        a1 = *(unsigned int *)(result + 1 * 4);
    }
    result = (unsigned int)(((unsigned int)(v_stack_m210)) + (1));
    goto loc_0044249D;
loc_004424FA:
    v_stack_m254 = 0;
    goto loc_00442576;
loc_0044255A:
loc_0044255F:
    v_stack_m254 = (unsigned int)((unsigned int)(0xC0000079ULL));
loc_00442566:
loc_0044256E:
loc_00442576:
    if (v_stack_m200 == 0) goto loc_004426AE;
    if (v_stack_m218 == 0) goto loc_004426AE;
    if (v_stack_m22C != 0) goto loc_004425DD;
    if (v_stack_m22B != 0) goto loc_004425DD;
    if (v_stack_m64 != 0) goto loc_0044266F;
    if (((*(unsigned int *)(v_stack_m218 + 200)) & (0x4000ULL)) == 0) goto loc_0044266F;
    if (sign_flag) goto loc_004426AE;
    if (v_stack_m230 < 0) goto loc_004425DD;
    if (v_stack_m59 == 0) goto loc_0044266F;
loc_004425DD:
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(v_stack_m218 + 48), 1, v_stack_m1F0, v_stack_m1E0);
    a1 = (v_stack_m230 >= 0) ? 1 : 0;
    if (v_stack_m22A == 0) {
        a4 = *(unsigned __int64 *)(v_stack_m218 + 1104);
    }
    result = (unsigned int)(((unsigned int)(v_stack_m248)) | (v_stack_m208));
    v_stack_m2C0 = 0;
    v_stack_m2C8 = (unsigned __int8)(a1);
    v_stack_m2D0 = (unsigned int)(result);
    v_stack_m2D8 = v_stack_m200;
    a3 = 0;
    a2 = 0;
    result = SeLogAccessFailure(v_stack_m218, a2, a3, a4);
    result = ExReleaseResourceLite(*(unsigned __int64 *)(v_stack_m218 + 48), a2, a3, a4);
    result = KeLeaveCriticalRegion(*(unsigned __int64 *)(v_stack_m218 + 48), a2, a3, a4);
loc_0044266F:
    if (sign_flag) goto loc_004426AE;
    if (v_stack_m230 >= 0) goto loc_004426AE;
    if (v_stack_m64 != 0) goto loc_004426AE;
    if (((*(unsigned int *)(v_stack_m218 + 200)) & (0x4000ULL)) == 0) goto loc_004426AE;
    result = SepLpacCausedAccessFailure(v_stack_m70, (unsigned int)(v_stack_m248), a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = SepLogLpacAccessFailure(v_stack_m70, (unsigned int)(v_stack_m248), a3, a4);
    }
    if (a12 == 0) goto loc_004426D9;
    if (v_stack_m228 != 0) {
        a2 = 0;
        a1 = v_stack_m228;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (v_stack_m190 != 0) {
        a2 = 0;
        a1 = v_stack_m190;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    if (v_stack_m218 != 0) {
        a2 = 0x74726853ULL;
        a1 = v_stack_m218;
        result = ObfDereferenceObjectWithTag(a1, a2, a3, a4);
    }
    if (v_stack_m178 != 0) {
        result = SeFreeCapturedObjectTypeList(v_stack_m178, a2, a3, a4);
    }
    if (v_stack_m170 != 0) {
        a3 = 1;
        a2 = v_stack_m250;
        result = SeReleaseSid(v_stack_m170, a2, a3, a4);
    }
    if (v_stack_m200 != 0) {
        a3 = 0;
        a2 = v_stack_m250;
        a1 = v_stack_m200;
        result = SeReleaseSecurityDescriptor(a1, a2, a3, a4);
    }
    if (v_stack_m240 != 0) {
        a1 = v_stack_m188;
        result = SepRmDereferenceCap(a1, a2, a3, a4);
    }
    if (v_stack_m160 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m160, a2, a3, a4);
    }
    result = SepFreeResourceInfo(v_stack_m1A8, a2, a3, a4);
loc_00442772:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (704);
    return result;
loc_00442796:
    result = ExRaiseDatatypeMisalignment(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SeAccessCheckByType(int64_t Arg1, int64_t Arg2, void *Arg3, int32_t Arg4, int64_t Arg5, uint32_t Arg6, int64_t Arg7, int64_t Arg8, void *Arg9, void *Arg10, void *Arg11, uint8_t Arg12)
{
    uint8_t *arg3 = (uint8_t *)Arg3;
    uint8_t *arg9 = (uint8_t *)Arg9;
    uint8_t *arg10 = (uint8_t *)Arg10;
    uint8_t *arg11 = (uint8_t *)Arg11;

    int64_t result;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m120;
    uint64_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint32_t v_stack_m150;
    uint32_t v_stack_m154;
    uint32_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint32_t v_stack_m198;
    uint32_t v_stack_m19C;
    uint32_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint32_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint32_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint32_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint32_t v_stack_m1F4;
    uint32_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint32_t v_stack_m208;
    uint8_t v_stack_m20C;
    uint32_t v_stack_m210;
    uint64_t v_stack_m218;
    uint32_t v_stack_m220;
    uint64_t v_stack_m228;
    uint8_t v_stack_m22A;
    uint8_t v_stack_m22B;
    uint8_t v_stack_m22C;
    uint32_t v_stack_m230;
    uint32_t v_stack_m238;
    uint8_t v_stack_m240;
    uint32_t v_stack_m248;
    uint8_t v_stack_m24F;
    uint8_t v_stack_m250;
    uint32_t v_stack_m254;
    uint8_t v_stack_m258;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m280;
    uint8_t v_stack_m288;
    uint8_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint8_t v_stack_m2B0;
    uint32_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint8_t v_stack_m59;
    uint8_t v_stack_m5A;
    uint8_t v_stack_m5B;
    uint64_t v_stack_m60;
    uint32_t v_stack_m64;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint32_t v_stack_mD4;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint8_t v_stack_p60;

    local_rsp = (local_rsp) - (704);
    result = (*(uint64_t *)(v_rip + 0x9C9B5E)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m140 = Arg2;
    v_stack_m1C0 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m180 = Arg7;
    v_stack_mB0 = Arg7;
    v_stack_mB8 = Arg10;
    v_stack_mC0 = Arg11;
    v_stack_mC8 = Arg9;
    v_stack_mA0 = Arg1;
    v_stack_m100 = Arg2;
    v_stack_mF8 = Arg3;
    v_stack_m248 = Arg4;
    v_stack_mA8 = Arg5;
    v_stack_m238 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m19C = (uint32_t)((uint32_t)(Arg6));
    v_stack_mD0 = Arg7;
    v_stack_m1B0 = Arg8;
    v_stack_m148 = Arg9;
    v_stack_m1F0 = Arg10;
    v_stack_mF0 = Arg10;
    v_stack_m1E0 = Arg11;
    v_stack_mE8 = Arg11;
    local_rdi = 0;
    v_stack_m1A0 = 0;
    v_stack_m228 = 0;
    v_stack_m150 = 0;
    v_stack_m154 = 0;
    v_stack_m190 = 0;
    v_stack_m158 = 0;
    v_stack_m1D8 = 0;
    v_stack_m254 = 0;
    v_stack_m218 = 0;
    v_stack_m200 = 0;
    v_stack_m170 = 0;
    v_stack_m208 = 0;
    v_stack_m220 = 0;
    v_stack_m50 = v_xmm0;
    v_stack_m178 = 0;
    v_stack_m1C8 = 0;
    v_stack_m130 = v_xmm0;
    v_stack_m120 = v_xmm0;
    v_stack_mE0 = v_xmm0;
    v_stack_m1F8 = 0;
    v_stack_m20C = 0;
    v_stack_m1A8 = 0;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = 0;
    v_stack_m58 = 0;
    v_stack_m1B8 = 0;
    v_stack_m98 = v_xmm0;
    v_stack_m88 = v_xmm0;
    v_stack_m78 = 0;
    v_stack_m188 = 0;
    v_stack_m240 = 0;
    v_stack_m24F = 0;
    v_stack_m1D0 = 0;
    v_stack_m258 = 0;
    v_stack_m160 = 0;
    v_stack_m22A = 0;
    v_stack_m22C = 0;
    v_stack_m22B = 0;
    v_stack_m138 = 0;
    v_stack_m168 = 0;
    v_stack_m230 = 0xC0000022ULL;
    v_stack_m1E8 = 0;
    v_stack_m198 = 0;
    v_stack_m250 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) != 0) goto loc_00440E67;
    goto loc_00440E74;
loc_00440E67:
    result = local_rsi;
    if (Arg9 < local_rsi) { result = Arg9; }
loc_00440E74:
    v_stack_m1E8 = (uint32_t)((uint32_t)(*(uint32_t *)(result)));
    goto loc_00440F20;
loc_00440F20:
    if (sign_flag) goto loc_00442772;
    result = (uint32_t)(((uint32_t)(v_stack_m254)) | (0xFFFFFFFFULL));
    v_stack_m180 = (uint32_t)(result);
    v_stack_m168 = (uint32_t)(result);
    if (v_stack_m250 != 0) goto loc_00440F57;
    *(uint32_t *)(arg11) = 0;
    *(uint32_t *)(arg10) = (uint32_t)((uint32_t)(v_stack_m248));
    result = 0;
    goto loc_00442772;
loc_00440F57:
    if (Arg12 == 0) goto loc_00440FB6;
    if ((uint32_t)((uint32_t)(v_stack_m238)) != 0) goto loc_00440F7D;
    v_stack_m254 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_00441033;
loc_00440F7D:
    result = ProbeForWrite(Arg11, (uint32_t)(0xC000000DULL) * 4, 4, Arg10);
    result = ProbeForWrite(v_stack_m1F0, (uint32_t)(0xC000000DULL) * 4, 4, Arg10);
    goto loc_00440FD2;
loc_00440FB6:
    Arg1 = local_rsi;
    if (Arg11 < local_rsi) { Arg1 = Arg11; }
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    Arg1 = local_rsi;
    if (Arg10 < local_rsi) { Arg1 = (uint32_t)(0xC000000DULL) * 4; }
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
loc_00440FD2:
    Arg1 = local_rsi;
    if (v_stack_m148 < local_rsi) { Arg1 = Arg9; }
    *(uint32_t *)(Arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg1)));
    result = ProbeForWrite(v_stack_m1B0, (uint32_t)(v_stack_m1E8), 4, Arg10);
    if (v_stack_m1B0 == 0) goto loc_0044100B;
    if (v_stack_m1E8 >= 20) {
        *(uint32_t *)(v_stack_m1B0) = 0;
    }
    if ((((uint8_t)(Arg7)) & (3)) != 0) goto loc_00442796;
    if (Arg7 < local_rsi) { local_rsi = v_stack_m180; }
    v_stack_m50 = v_xmm0;
loc_00441033:
    goto loc_00441086;
loc_00441086:
    if (sign_flag) goto loc_00442772;
    if (((v_stack_m248) & (0xF0000000ULL)) == 0) goto loc_004410B3;
    goto loc_0044255F;
loc_004410B3:
    v_stack_m2C8 = v_stack_m138;
    v_stack_m2D0 = v_stack_m22A;
    v_stack_m2D8 = v_stack_m218;
    result = SepReferenceTokenByHandle(Arg3, 8, v_stack_m250, Arg10);
    v_stack_m254 = (uint32_t)(result);
    if (!sign_flag) goto loc_00441112;
    v_stack_m218 = 0;
    goto loc_00442566;
loc_00441112:
    Arg1 = ((Arg3 + 6) <= 2) ? 1 : 0;
    if ((uint32_t)(Arg1) != 0) goto loc_00441151;
    if ((*(uint32_t *)(v_stack_m218 + 0xC0)) == 2) goto loc_0044113E;
    goto loc_0044255F;
loc_0044113E:
    if ((*(uint32_t *)(v_stack_m218 + 0xC4)) >= 1) goto loc_00441151;
    goto loc_0044255F;
loc_00441151:
    result = SeCaptureObjectTypeList(v_stack_mA8, (uint32_t)(v_stack_m238), (uint8_t)(v_stack_m250), v_stack_m178);
    v_stack_m254 = (uint32_t)(result);
    if (sign_flag) goto loc_00442566;
    v_stack_m2D8 = v_stack_m200;
    Arg4 = 0;
    result = SeCaptureSecurityDescriptor(v_stack_mA0, (uint8_t)(v_stack_m250), 1, Arg4);
    v_stack_m254 = (uint32_t)(result);
    if (sign_flag) goto loc_00442566;
    if (v_stack_m200 == 0) goto loc_0044255A;
    if (!sign_flag) goto loc_004411EE;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m200 + 0x4))) == 0) goto loc_0044255A;
    result = ((uint32_t)(*(uint32_t *)(v_stack_m200 + 0x4))) + (v_stack_m200);
    goto loc_004411FA;
loc_004411EE:
loc_004411FA:
    if (*(uint64_t *)(v_stack_m200 + 0x8) == 0) goto loc_0044255A;
    if (!sign_flag) goto loc_00441221;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m200 + 0x8))) == 0) goto loc_0044255A;
    result = ((uint32_t)(*(uint32_t *)(v_stack_m200 + 0x8))) + (v_stack_m200);
    goto loc_0044122D;
loc_00441221:
loc_0044122D:
    if (*(uint64_t *)(v_stack_m200 + 0x10) == 0) goto loc_0044255A;
    result = v_stack_m138;
    if (v_stack_m22A == 0) {
        result = *(uint64_t *)(v_stack_m218 + 0x450);
    }
    v_stack_m2C8 = v_stack_m180;
    v_stack_m2D0 = 1;
    v_stack_m2D8 = result;
    Arg3 = 0;
    result = SepTrustLevelCheck(v_stack_m180, v_stack_m200, Arg3, v_stack_m218);
    v_stack_m254 = (uint32_t)(result);
    if (sign_flag) goto loc_00442566;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m248)))))) & (v_stack_m180));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m248)))))) goto loc_00441458;
    v_stack_m2D8 = v_stack_m168;
    result = SepFilterCheck(v_stack_m200, v_stack_m1A8, v_stack_m218, 1);
    v_stack_m254 = (uint32_t)(result);
    if (sign_flag) goto loc_00442566;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m248)))))) & (v_stack_m168));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m248)))))) goto loc_0044144E;
    v_stack_m2D0 = v_stack_mE0;
    v_stack_m2D8 = 1;
    Arg3 = 0;
    result = SepMandatoryIntegrityCheck(v_stack_m50, v_stack_m200, Arg3, v_stack_m218);
    v_stack_m254 = (uint32_t)(result);
    if (sign_flag) goto loc_00442566;
    v_stack_m1F8 = 0;
    result = SepMandatoryToDiscretionary(v_stack_mE0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m248))), Arg3, v_stack_m218);
    if (sign_flag) goto loc_00441358;
    if (condition_is_above_or_equal) goto loc_0044137F;
loc_00441358:
    local_r15 = 0;
    if (((*(uint32_t *)(v_stack_m218 + 0xC8)) & (0x4000ULL)) != 0) {
        local_r15 = 0;
        if (v_stack_mD4 <= 0x2000ULL) { local_r15 = 1; }
        v_stack_m1F8 = (uint32_t)(local_r15);
    }
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(v_stack_mE0, (uint32_t)((uint32_t)((uint32_t)(v_stack_m248))), Arg3, v_stack_m218);
    if ((uint32_t)(result) == 0) goto loc_004413EB;
    v_stack_m2D0 = v_stack_m198;
    v_stack_m2D8 = (uint32_t)((uint32_t)(v_stack_m248));
    Arg2 = 0;
    result = SepMandatoryAccessCheck(v_stack_m200, Arg2, v_stack_m218, 1);
    if (sign_flag) goto loc_004413CC;
    local_r12 = (uint32_t)(((uint32_t)(v_stack_m248)) & (v_stack_m198));
    if ((((uint32_t)(local_r12)) & (0xFDFFFFFFULL)) == 0) goto loc_004413EB;
loc_004413CC:
    *(uint32_t *)(v_stack_m1F0) = 0;
    *(uint32_t *)(v_stack_m1E0) = (uint32_t)((uint32_t)(0xC00001C0ULL));
    goto loc_0044255F;
loc_004413EB:
    if (!sign_flag) goto loc_004413F4;
    if ((uint8_t)(local_r15) == 0) goto loc_00441446;
loc_004413F4:
    v_stack_m2D0 = (uint8_t)(v_stack_m250);
    v_stack_m2D8 = v_stack_m1C8;
    Arg3 = 0;
    result = SePrivilegePolicyCheck(v_stack_m248, v_stack_m208, Arg3, v_stack_m218);
    if (v_stack_m248 != 0) goto loc_00441446;
    if (v_stack_m208 == 0) goto loc_00441446;
    goto loc_00441479;
loc_00441446:
    goto loc_00441471;
loc_0044144E:
    v_stack_m22B = 1;
    goto loc_00441460;
loc_00441458:
    v_stack_m22C = 1;
loc_00441460:
loc_00441471:
loc_00441479:
    if (!sign_flag) goto loc_00441518;
    if ((uint8_t)((uint32_t)(v_stack_m1F8)) != 0) goto loc_00441518;
    if (Arg12 == 0) goto loc_004414C7;
loc_004414A9:
    v_stack_m210 = 0;
    if (0 >= v_stack_m238) goto loc_004414D4;
    *(uint32_t *)(v_stack_m1E0 + 0x0 * 4) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC0000022ULL))));
    *(uint32_t *)(v_stack_m1F0 + 0x0 * 4) = 0;
    Arg1 = (uint32_t)((0) + (1));
    goto loc_004414A9;
loc_004414C7:
    *(uint32_t *)(v_stack_m1E0) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC0000022ULL))));
    *(uint32_t *)(v_stack_m1F0) = 0;
loc_004414D4:
    v_stack_m230 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(0xC0000022ULL))));
    v_stack_m254 = 0;
    goto loc_00442576;
loc_00441518:
    if (v_stack_m1C8 == 0) goto loc_004415FC;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1C8)) + (uint32_t)(*(uint32_t *)(v_stack_m1C8)) * 2) << (2));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1C8))) == 0) {
        Arg2 = 8;
    }
    if (((uint32_t)(Arg2)) <= v_stack_m1E8) goto loc_0044159A;
    result = (uint32_t)((result) + (8));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1C8))) == 0) { result = 8; }
    *(uint32_t *)(v_stack_m148) = (uint32_t)(result);
    v_stack_m254 = (uint32_t)((uint32_t)(0xC0000023ULL));
    goto loc_0044158B;
loc_0044158B:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m1C8, Arg2, 8, v_stack_m1E0);
    goto loc_00442566;
loc_0044159A:
    result = (uint32_t)((result) + (8));
    if ((uint32_t)(v_stack_m1C8) == 0) { result = 8; }
    result = memcpy(v_stack_m1B0, v_stack_m1C8, (uint32_t)((uint32_t)(result)), v_stack_m1E0);
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m1C8, Arg2, (uint32_t)((uint32_t)(result)), v_stack_m1E0);
    goto loc_00441668;
loc_004415FC:
    if (v_stack_m1E8 >= 20) goto loc_0044165C;
    *(uint32_t *)(v_stack_m148) = 20;
    v_stack_m254 = (uint32_t)((uint32_t)(0xC0000023ULL));
    goto loc_00442576;
loc_0044165C:
loc_00441668:
    if (v_stack_m140 == 0) goto loc_004416B0;
    v_stack_m2C8 = v_stack_m170;
    v_stack_m2D0 = 1;
    result = SeCaptureSid(v_stack_m140, v_stack_m250, (uint32_t)((uint32_t)(result)), v_stack_m1E0);
    v_stack_m254 = (uint32_t)(result);
    if (!sign_flag) goto loc_004416B0;
    v_stack_m170 = 0;
    goto loc_00442566;
loc_004416B0:
    result = SeCaptureSubjectContext(v_stack_m130, v_stack_m250, (uint32_t)((uint32_t)(result)), v_stack_m1E0);
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m218 + 0x30), 1, (uint32_t)((uint32_t)(result)), v_stack_m1E0);
    result = SepTokenIsOwner(v_stack_m218, v_stack_m200, (uint32_t)((uint32_t)(result)), v_stack_m1E0);
    v_stack_m258 = (uint8_t)(result);
    if ((*(uint8_t *)(v_rip + 0x9CB5AE)) != 0) goto loc_004417CD;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m218 + 0xC8)))) & (32)) != 0) goto loc_004417CD;
    if (*(uint64_t *)(v_stack_m218 + 0xD8) == 0) goto loc_004417CD;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m218 + 0xD8) + 0x28)))) & (32)) == 0) goto loc_004417CD;
    if (Arg12 == 0) goto loc_0044176E;
loc_00441750:
    v_stack_m210 = 0;
    if (0 >= v_stack_m238) goto loc_0044177B;
    *(uint32_t *)(v_stack_m1E0 + 0x0 * 4) = (uint32_t)(v_stack_m228);
    *(uint32_t *)(v_stack_m1F0 + 0x0 * 4) = 0;
    Arg1 = (uint32_t)((0) + (1));
    goto loc_00441750;
loc_0044176E:
    *(uint32_t *)(v_stack_m1E0) = (uint32_t)(v_stack_m228);
    *(uint32_t *)(v_stack_m1F0) = 0;
loc_0044177B:
    v_stack_m230 = (uint32_t)(v_stack_m228);
    v_stack_m254 = 0;
    goto loc_004417AD;
loc_004417AD:
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m218 + 0x30), v_stack_m1F0, (uint32_t)((uint32_t)(result)), v_stack_m1E0);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m218 + 0x30), v_stack_m1F0, (uint32_t)((uint32_t)(result)), v_stack_m1E0);
    result = SeReleaseSubjectContext(v_stack_m130, v_stack_m1F0, (uint32_t)((uint32_t)(result)), v_stack_m1E0);
    goto loc_0044256E;
loc_004417CD:
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xAC32F2)) == 0) goto loc_00441879;
    if ((((uint8_t)(*(uint16_t *)(v_stack_m200 + 0x2))) & (16)) == 0) goto loc_00441872;
    if (((uint8_t)(v_cr8)) >= 2) goto loc_00441872;
    if (!sign_flag) goto loc_0044181A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m200 + 0xC))) != 0) goto loc_00441810;
    v_stack_m1B8 = 0;
    goto loc_00441872;
loc_00441810:
    result = ((uint32_t)(*(uint32_t *)(v_stack_m200 + 0xC))) + (v_stack_m200);
    goto loc_00441826;
loc_0044181A:
loc_00441826:
    v_stack_m1B8 = *(uint64_t *)(v_stack_m200 + 0x18);
    if (*(uint64_t *)(v_stack_m200 + 0x18) == 0) goto loc_00441872;
    result = SepGetScopedPolicySid(*(uint64_t *)(v_stack_m200 + 0x18), v_stack_m1F0, (uint32_t)((uint32_t)(result)), v_stack_m1E0);
    if (result != 0) {
        Arg2 = v_stack_m188;
        Arg1 = result;
        result = SepRmReferenceFindCap(Arg1, Arg2, (uint32_t)((uint32_t)(result)), v_stack_m1E0);
        Arg2 = v_stack_m188;
        if (sign_flag) { Arg2 = *(uint64_t *)(v_rip + 0xB9688E); }
        v_stack_m188 = Arg2;
        v_stack_m240 = 1;
    }
loc_00441879:
    if (((v_stack_m248) & (0x2060000ULL)) == 0) goto loc_00441921;
    if ((uint8_t)(v_stack_m258) == 0) goto loc_00441921;
    if ((((uint8_t)(*(uint16_t *)(v_stack_m200 + 0x2))) & (4)) != 0) goto loc_004418A8;
loc_004418A3:
    goto loc_004418C7;
loc_004418A8:
    if (!sign_flag) goto loc_004418C3;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m200 + 0x10))) == 0) goto loc_004418A3;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m200 + 0x10))))) + (v_stack_m200);
    goto loc_004418C7;
loc_004418C3:
loc_004418C7:
    Arg1 = 0;
    result = RtlpOwnerAcesPresent(Arg1, *(uint64_t *)(v_stack_m200 + 0x20), (uint32_t)((uint32_t)(result)), v_stack_m1E0);
    if ((uint8_t)(result) != 0) goto loc_00441921;
    if (((v_stack_m248) & (0x2000000ULL)) == 0) goto loc_004418EF;
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m208)) | ((uint32_t)((uint32_t)(0x60000ULL))));
    goto loc_00441906;
loc_004418EF:
    result = (uint32_t)(((uint32_t)(v_stack_m248)) & ((uint32_t)((uint32_t)(0x60000ULL))));
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(result))) | (v_stack_m208));
loc_00441906:
    v_stack_m220 = (uint32_t)(result);
    v_stack_m208 = (uint32_t)(local_rbx);
    goto loc_00441928;
loc_00441921:
loc_00441928:
    result = Feature_DecoupleAppContainerAndIntegrityLevel__private_IsEnabledDeviceUsageNoInline((uint32_t)(0x60000ULL), *(uint64_t *)(v_stack_m200 + 0x20), (uint32_t)((uint32_t)(result)), v_stack_m1E0);
    if ((uint32_t)(result) == 0) goto loc_00441A3A;
    if (v_stack_m248 != 0) goto loc_00441B39;
    if (v_stack_m240 == 0) goto loc_00441955;
    if ((uint8_t)(v_stack_m258) == 0) goto loc_00441B39;
loc_00441955:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m218 + 0xC8))) & (0x6000ULL));
    if (((uint32_t)(result)) == 0x2000ULL) goto loc_0044197C;
    if (v_stack_m220 != 0) goto loc_00441B41;
loc_0044197C:
    if (Arg12 == 0) goto loc_004419D9;
loc_004419A3:
    v_stack_m210 = 0;
    if (0 >= ((uint32_t)((uint32_t)(v_stack_m238)))) goto loc_00441A08;
    if ((uint32_t)((uint32_t)(v_stack_m208)) != 0) goto loc_004419C6;
    *(uint32_t *)(v_stack_mE8 + 0x0 * 4) = (uint32_t)(v_stack_m228);
    v_stack_m230 = (uint32_t)(v_stack_m228);
    *(uint32_t *)(v_stack_mF0 + 0x0 * 4) = 0;
    goto loc_004419D4;
loc_004419C6:
    *(uint32_t *)(v_stack_mE8 + 0x0 * 4) = 0;
    v_stack_m230 = 0;
    *(uint32_t *)(v_stack_mF0 + 0x0 * 4) = (uint32_t)((uint32_t)(v_stack_m208));
loc_004419D4:
    result = (uint32_t)((0) + (1));
    goto loc_004419A3;
loc_004419D9:
    if ((uint32_t)((uint32_t)(v_stack_m208)) != 0) goto loc_004419FC;
    *(uint32_t *)(v_stack_m1E0) = (uint32_t)(v_stack_m228);
    v_stack_m230 = (uint32_t)(v_stack_m228);
    *(uint32_t *)(v_stack_m1F0) = 0;
    goto loc_00441A08;
loc_004419FC:
    *(uint32_t *)(v_stack_m1E0) = 0;
    v_stack_m230 = 0;
    *(uint32_t *)(v_stack_m1F0) = (uint32_t)((uint32_t)(v_stack_m208));
loc_00441A08:
    v_stack_m254 = 0;
    goto loc_004417AD;
loc_00441A3A:
    if (v_stack_m248 != 0) goto loc_00441B39;
    if (v_stack_m240 == 0) goto loc_00441A5A;
    if ((uint8_t)(v_stack_m258) == 0) goto loc_00441B39;
loc_00441A5A:
    if (((*(uint32_t *)(v_stack_m218 + 0xC8)) & (0x2000ULL)) != 0) goto loc_00441A7B;
    if (v_stack_m220 != 0) goto loc_00441B41;
loc_00441A7B:
    if (Arg12 == 0) goto loc_00441AD8;
loc_00441AA2:
    v_stack_m210 = 0;
    if (0 >= ((uint32_t)((uint32_t)(v_stack_m238)))) goto loc_00441B07;
    if (0 != 0) goto loc_00441AC5;
    *(uint32_t *)(v_stack_mE8 + 0x0 * 4) = (uint32_t)(v_stack_m228);
    v_stack_m230 = (uint32_t)(v_stack_m228);
    *(uint32_t *)(v_stack_mF0 + 0x0 * 4) = 0;
    goto loc_00441AD3;
loc_00441AC5:
    *(uint32_t *)(v_stack_mE8 + 0x0 * 4) = 0;
    v_stack_m230 = 0;
    *(uint32_t *)(v_stack_mF0 + 0x0 * 4) = 0;
loc_00441AD3:
    result = (uint32_t)((0) + (1));
    goto loc_00441AA2;
loc_00441AD8:
    if (0 != 0) goto loc_00441AFB;
    *(uint32_t *)(v_stack_m1E0) = (uint32_t)(v_stack_m228);
    v_stack_m230 = (uint32_t)(v_stack_m228);
    *(uint32_t *)(v_stack_m1F0) = 0;
    goto loc_00441B07;
loc_00441AFB:
    *(uint32_t *)(v_stack_m1E0) = 0;
    v_stack_m230 = 0;
    *(uint32_t *)(v_stack_m1F0) = 0;
loc_00441B07:
    v_stack_m254 = 0;
    goto loc_004417AD;
loc_00441B39:
loc_00441B41:
    if (Arg12 == 0) goto loc_00441BC0;
    result = ExAllocatePool2(256, (uint32_t)(v_stack_m19C) * 8, (uint32_t)(0x61476553ULL), v_stack_m1E0);
    v_stack_m228 = result;
    if (result != 0) goto loc_00441BB3;
loc_00441B7F:
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m218 + 0x30), (uint32_t)(v_stack_m19C) * 8, (uint32_t)(0x61476553ULL), v_stack_m1E0);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m218 + 0x30), (uint32_t)(v_stack_m19C) * 8, (uint32_t)(0x61476553ULL), v_stack_m1E0);
    result = SeReleaseSubjectContext(v_stack_m130, (uint32_t)(v_stack_m19C) * 8, (uint32_t)(0x61476553ULL), v_stack_m1E0);
    v_stack_m254 = (uint32_t)((uint32_t)(0xC000009AULL));
loc_00441BA6:
    goto loc_00442576;
loc_00441BB3:
    goto loc_00441BD8;
loc_00441BC0:
    v_stack_m228 = v_stack_m1A0;
loc_00441BD8:
    v_stack_m70 = (uint32_t)((uint32_t)(v_stack_m220));
    v_stack_m268 = 0;
    v_stack_m270 = 0;
    v_stack_m278 = v_stack_m1A8;
    v_stack_m280 = v_stack_m70;
    v_stack_m288 = (uint8_t)(v_stack_m258);
    v_stack_m290 = Arg12;
    v_stack_m298 = v_stack_m150;
    v_stack_m2A0 = 0;
    v_stack_m2A8 = v_stack_m1A0;
    v_stack_m2B0 = (uint8_t)(v_stack_m250);
    v_stack_m2B8 = (uint32_t)((uint32_t)(0xC000009AULL));
    v_stack_m2C0 = v_stack_m50;
    v_stack_m2C8 = (uint32_t)((uint32_t)(v_stack_m238));
    v_stack_m2D0 = v_stack_m178;
    v_stack_m2D8 = (uint32_t)((uint32_t)(v_stack_m248));
    result = SepAccessCheck(v_stack_m200, v_stack_m170, v_stack_m120, v_stack_m218);
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xAC2E2F)) == 0) goto loc_00442187;
    if ((*(uint32_t *)(v_stack_m150)) < 0) goto loc_00442187;
    if (v_stack_m240 == 0) goto loc_00442187;
    if (Arg12 == 0) goto loc_00441D02;
    result = ExAllocatePool2(256, Arg12, (uint32_t)(0x61476553ULL), v_stack_m218);
    v_stack_m190 = result;
    if (result != 0) goto loc_00441CED;
    goto loc_00441B7F;
loc_00441CED:
    v_stack_m1D8 = result + (uint32_t)(v_stack_m19C) * 4;
    goto loc_00441D22;
loc_00441D02:
    v_stack_m190 = v_stack_m154;
    v_stack_m1D8 = v_stack_m158;
loc_00441D22:
    v_stack_m1C8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m150)));
    v_stack_m220 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1A0)));
    v_stack_m1F4 = 0;
    if ((uint32_t)((uint32_t)(v_stack_m238)) == 0) goto loc_00441D97;
    result = SepCopyObjectTypeList(v_stack_m178, (uint32_t)((uint32_t)((uint32_t)(v_stack_m238))), v_stack_m160, v_stack_m218);
    v_stack_m254 = (uint32_t)(result);
    if (!sign_flag) goto loc_00441D80;
    goto loc_00441BA6;
loc_00441D80:
loc_00441D97:
    v_stack_m1B0 = 0;
    if ((*(uint32_t *)(v_stack_m188 + 0x3C)) <= 0) goto loc_0044214B;
loc_00441DC1:
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m188 + 0x0 * 8 + 0x40) + 0x18)) == 0) goto loc_00441F90;
    result = v_stack_m188;
    local_rbx = (uint32_t)(v_stack_m1F4);
    if (v_stack_m1A8 == 0) {
        Arg2 = v_stack_m1A8;
        Arg1 = v_stack_m1B8;
        result = AuthzBasepInitializeResourceClaimsFromSacl(Arg1, Arg2, v_stack_m1A8, v_stack_m218);
        local_rbx = (uint8_t)((uint32_t)(v_stack_m1F4));
        if (sign_flag) { local_rbx = 1; }
        v_stack_m1F4 = (uint32_t)(local_rbx);
        Arg3 = v_stack_m1A8;
    }
    if (*(uint64_t *)(v_stack_m218 + 0x448) == 0) goto loc_00441E24;
    goto loc_00441E27;
loc_00441E24:
loc_00441E27:
    if (*(uint64_t *)(v_stack_m218 + 0x448) == 0) goto loc_00441E35;
    goto loc_00441E38;
loc_00441E35:
loc_00441E38:
    if (*(uint64_t *)(v_stack_m218 + 0x448) == 0) goto loc_00441E46;
    goto loc_00441E49;
loc_00441E46:
loc_00441E49:
    if (*(uint64_t *)(v_stack_m218 + 0x448) == 0) goto loc_00441E57;
    goto loc_00441E5A;
loc_00441E57:
loc_00441E5A:
    v_stack_m2A0 = v_stack_m1D0;
    v_stack_m2A8 = 0;
    v_stack_m2B0 = 1;
    v_stack_m2B8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m188 + 0x0 * 8 + 0x40) + 0x10)));
    v_stack_m2C0 = *(uint64_t *)(*(uint64_t *)(v_stack_m188 + 0x0 * 8 + 0x40) + 0x18);
    v_stack_m2C8 = 0;
    v_stack_m2D0 = 0;
    v_stack_m2D8 = 0;
    result = AuthzBasepEvaluateAceCondition(v_stack_m218, *(uint64_t *)(v_stack_m218 + 0x308), Arg3, 0);
    v_stack_m254 = (uint32_t)(result);
    if (v_stack_m1D0 == 1) goto loc_00441F90;
    if (sign_flag) goto loc_00442167;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m218 + 0xC8)))) & (16)) == 0) goto loc_00441F77;
    if (*(uint64_t *)(v_stack_m218 + 0x448) == 0) goto loc_00441EE2;
    goto loc_00441EE5;
loc_00441EE2:
loc_00441EE5:
    if (*(uint64_t *)(v_stack_m218 + 0x448) == 0) goto loc_00441EF3;
    goto loc_00441EF6;
loc_00441EF3:
loc_00441EF6:
    if (*(uint64_t *)(v_stack_m218 + 0x448) == 0) goto loc_00441F04;
    goto loc_00441F07;
loc_00441F04:
loc_00441F07:
    if (*(uint64_t *)(v_stack_m218 + 0x448) == 0) goto loc_00441F15;
    goto loc_00441F18;
loc_00441F15:
loc_00441F18:
    v_stack_m2A0 = v_stack_m1D0;
    v_stack_m2A8 = 1;
    v_stack_m2B0 = 1;
    v_stack_m2B8 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m188 + 0x0 * 8 + 0x40) + 0x10)));
    v_stack_m2C0 = *(uint64_t *)(*(uint64_t *)(v_stack_m188 + 0x0 * 8 + 0x40) + 0x18);
    v_stack_m2C8 = 0;
    v_stack_m2D0 = 0;
    v_stack_m2D8 = 0;
    result = AuthzBasepEvaluateAceCondition(v_stack_m218, *(uint64_t *)(v_stack_m218 + 0x308), v_stack_m1A8, 0);
    v_stack_m254 = (uint32_t)(result);
    if (sign_flag) goto loc_00442167;
loc_00441F77:
    if ((uint8_t)((uint32_t)(v_stack_m1F4)) != 0) goto loc_00441F90;
    if (v_stack_m1D0 != 1) goto loc_00442155;
loc_00441F90:
    result = SepBuildCapeSecurityDescriptor(v_stack_m98, *(uint64_t *)(*(uint64_t *)(v_stack_m188 + 0x0 * 8 + 0x40) + 0x20), v_stack_m1B8, 0);
    v_stack_m254 = (uint32_t)(result);
    if (sign_flag) goto loc_00442167;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m188 + 0x0 * 8 + 0x40) + 0x30))))) == 0) goto loc_00441FDE;
    local_r12 = (uint32_t)(v_stack_m248);
    if (!(condition_is_below)) {
        local_r12 = (uint32_t)(((uint32_t)(v_stack_m248)) | (v_stack_m208));
    }
    goto loc_00441FE5;
loc_00441FDE:
loc_00441FE5:
    v_stack_m268 = 0;
    v_stack_m270 = 0;
    v_stack_m278 = v_stack_m1A8;
    v_stack_m280 = v_stack_m70;
    v_stack_m288 = (uint8_t)(v_stack_m258);
    v_stack_m290 = Arg12;
    v_stack_m298 = v_stack_m1D8;
    v_stack_m2A0 = 0;
    v_stack_m2A8 = v_stack_m190;
    v_stack_m2B0 = (uint8_t)(v_stack_m250);
    v_stack_m2B8 = (uint32_t)((uint32_t)(v_stack_m208));
    v_stack_m2C0 = v_stack_m50;
    v_stack_m2C8 = (uint32_t)((uint32_t)(v_stack_m238));
    v_stack_m2D0 = v_stack_m160;
    v_stack_m2D8 = (uint32_t)(local_r12);
    result = SepAccessCheck(v_stack_m98, v_stack_m170, v_stack_m120, v_stack_m218);
    if (v_stack_m24F != 0) goto loc_004420B2;
    goto loc_004420BD;
loc_004420B2:
    local_r11 = (uint32_t)(((uint32_t)(v_stack_m220)) & ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m190)))));
loc_004420BD:
    v_stack_m220 = (uint32_t)(local_r11);
    if ((uint32_t)(local_r11) != 0) goto loc_004420D2;
    goto loc_004420DD;
loc_004420D2:
loc_004420DD:
    v_stack_m1C8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1D8)));
    v_stack_m24F = 1;
    result = v_stack_m1D8;
    if (v_stack_m160 != 0) {
        Arg3 = (uint32_t)((uint32_t)(v_stack_m238));
        Arg2 = v_stack_m160;
        Arg1 = v_stack_m178;
        result = SepMergeObjectTypeListAccesses(Arg1, Arg2, Arg3, v_stack_m218);
    }
    if (sign_flag) goto loc_00442143;
loc_00442121:
    result = (uint32_t)(((uint32_t)(v_stack_m1B0)) + (1));
    v_stack_m1B0 = (uint32_t)(result);
    if (((uint32_t)(result)) < (*(uint32_t *)(v_stack_m188 + 0x3C))) goto loc_00441DC1;
loc_00442143:
loc_0044214B:
    *(uint32_t *)(v_stack_m150) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1D8)));
    goto loc_0044218F;
loc_00442155:
    goto loc_00442121;
loc_00442167:
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m218 + 0x30), Arg2, Arg3, v_stack_m218);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m218 + 0x30), Arg2, Arg3, v_stack_m218);
    result = SeReleaseSubjectContext(v_stack_m130, Arg2, Arg3, v_stack_m218);
    goto loc_00442566;
loc_00442187:
loc_0044218F:
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m218 + 0x30), Arg2, Arg3, v_stack_m218);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m218 + 0x30), Arg2, Arg3, v_stack_m218);
    result = SeReleaseSubjectContext(v_stack_m130, Arg2, Arg3, v_stack_m218);
    local_rbx = (uint32_t)(((uint32_t)(v_stack_m248)) & (0x2000000ULL));
    if (condition_is_equal) goto loc_00442252;
    if (v_stack_m1F8 == 0) goto loc_004421EC;
    if (v_stack_m5A != 0) goto loc_00442221;
    if (v_stack_m5B != 0) goto loc_00442221;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m218 + 0xC8))) & ((uint32_t)((uint32_t)(0x3000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x3000000ULL)))) {
        result = Arg12;
        result = (uint8_t)(-(result));
        Arg1 = (uint32_t)(((uint32_t)(0x3000000ULL)) & (v_stack_m1C0));
        v_stack_m2D0 = (uint32_t)(Arg1);
        v_stack_m2D8 = 0;
        Arg4 = v_stack_m150;
        Arg3 = v_stack_m228;
        Arg2 = v_stack_m248;
        Arg1 = v_stack_mE0;
        result = SepConstrainByMandatory(Arg1, Arg2, Arg3, Arg4);
    }
    result = Feature_OutsideInProtection__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, Arg3, Arg4);
    if ((uint32_t)(result) == 0) goto loc_004423A8;
    result = (uint32_t)(~((uint32_t)(v_stack_m198)));
    goto loc_004423A8;
loc_00442252:
    if (v_stack_m1F8 == 0) goto loc_00442399;
    if (v_stack_m5A != 0) goto loc_00442399;
    if (v_stack_m5B != 0) goto loc_00442399;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_m238) + 0xC8))) & ((uint32_t)((uint32_t)(0x3000000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x3000000ULL)))) goto loc_00442302;
    if (v_stack_m64 != 0) goto loc_00442302;
    v_stack_m59 = 1;
    if (Arg12 == 0) goto loc_004422E7;
    if ((uint32_t)((uint32_t)(v_stack_m238)) == 0) goto loc_004423A8;
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m248)) | (v_stack_m208));
    Arg2 = (v_stack_m150) - (v_stack_m228);
loc_004422D4:
    *(uint32_t *)(Arg2 + v_stack_m228 * 1) = 0;
    *(uint32_t *)(v_stack_m228) = (uint32_t)(Arg1);
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m238)))) - (1);
    if (condition_is_not_equal) goto loc_004422D4;
    goto loc_004423A8;
loc_004422E7:
    *(uint32_t *)(v_stack_m150) = 0;
    result = (uint32_t)(((uint32_t)(v_stack_m248)) | (v_stack_m208));
    *(uint32_t *)(v_stack_m228) = (uint32_t)(result);
    goto loc_004423A1;
loc_00442302:
    if (Arg12 == 0) goto loc_00442343;
loc_00442321:
    v_stack_m210 = 0;
    if (0 >= v_stack_m238) goto loc_00442354;
    *(uint32_t *)(v_stack_m1E0 + 0x0 * 4) = 0xC0000022ULL;
    *(uint32_t *)(v_stack_m1F0 + 0x0 * 4) = 0;
    Arg1 = (uint32_t)((0) + (1));
    goto loc_00442321;
loc_00442343:
    *(uint32_t *)(v_stack_m1E0) = 0xC0000022ULL;
    *(uint32_t *)(v_stack_m1F0) = 0;
loc_00442354:
    v_stack_m230 = 0xC0000022ULL;
    v_stack_m254 = 0;
    goto loc_00442576;
loc_00442399:
loc_004423A1:
loc_004423A8:
    result = v_stack_m1F0;
    local_rbx = 0;
    local_r12 = v_stack_m228;
    if (0 != 0) {
        result = Arg12;
        result = (uint8_t)(-(result));
        local_rbx = (uint32_t)((0) & (v_stack_m1C0));
        result = v_stack_m22C;
        v_stack_m2C8 = result;
        v_stack_m2D0 = (uint32_t)(local_rbx);
        v_stack_m2D8 = 0;
        Arg4 = v_stack_m150;
        Arg3 = v_stack_m228;
        Arg2 = v_stack_m248;
        Arg1 = v_stack_m180;
        result = SepConstrainByConstraintMask(Arg1, Arg2, Arg3, Arg4);
        Arg2 = v_stack_m22B;
        v_stack_m2C8 = Arg2;
        v_stack_m2D0 = (uint32_t)(local_rbx);
        v_stack_m2D8 = 0;
        Arg4 = v_stack_m150;
        Arg3 = v_stack_m228;
        Arg2 = v_stack_m248;
        Arg1 = v_stack_m168;
        result = SepConstrainByConstraintMask(Arg1, Arg2, Arg3, Arg4);
        local_r12 = v_stack_m228;
    }
    *(uint32_t *)(v_stack_m1E0) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m150)));
    *(uint32_t *)(v_stack_m1F0) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r12)));
    v_stack_m230 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m150)));
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xAC2671)) == 0) goto loc_00442495;
    if ((uint8_t)(v_stack_m24F) == 0) goto loc_00442495;
    result = *(uint8_t *)(v_rip + 0xAC2671);
    if ((*(uint32_t *)(v_stack_m150)) >= 0) {
        result = *(uint32_t *)(v_stack_m1D8);
        *(uint32_t *)(v_stack_m1E0) = (uint32_t)(result);
        result = v_stack_m190;
        Arg1 = *(uint32_t *)(result);
        result = *(uint32_t *)(v_stack_m1D8);
        v_stack_m230 = (uint32_t)(result);
        Arg1 = v_stack_m24F;
    }
    if (Arg12 == 0) goto loc_004424FA;
loc_0044249D:
    v_stack_m210 = 1;
    if (1 >= ((uint32_t)((uint32_t)(v_stack_m238)))) goto loc_004424FA;
    *(uint32_t *)(v_stack_m1E0 + 0x1 * 4) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m150 + 0x1 * 4)));
    *(uint32_t *)(v_stack_m1F0 + 0x1 * 4) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + 0x1 * 4)));
    if ((uint8_t)(*(uint8_t *)(v_rip + 0xAC2604)) == 0) goto loc_004424E7;
    if ((uint8_t)(Arg1) == 0) goto loc_004424E7;
    result = *(uint8_t *)(v_rip + 0xAC2604);
    if ((*(uint32_t *)(v_stack_m150 + 0x1 * 4)) >= 0) {
        result = *(uint32_t *)(v_stack_m1D8 + 0x1 * 4);
        *(uint32_t *)(v_stack_m1E0 + 0x1 * 4) = (uint32_t)(result);
        result = v_stack_m190;
        Arg1 = *(uint32_t *)(result + 0x1 * 4);
    }
    result = (uint32_t)(((uint32_t)(v_stack_m210)) + (1));
    goto loc_0044249D;
loc_004424FA:
    v_stack_m254 = 0;
    goto loc_00442576;
loc_0044255A:
loc_0044255F:
    v_stack_m254 = (uint32_t)((uint32_t)(0xC0000079ULL));
loc_00442566:
loc_0044256E:
loc_00442576:
    if (v_stack_m200 == 0) goto loc_004426AE;
    if (v_stack_m218 == 0) goto loc_004426AE;
    if (v_stack_m22C != 0) goto loc_004425DD;
    if (v_stack_m22B != 0) goto loc_004425DD;
    if (v_stack_m64 != 0) goto loc_0044266F;
    if (((*(uint32_t *)(v_stack_m218 + 0xC8)) & (0x4000ULL)) == 0) goto loc_0044266F;
    if (sign_flag) goto loc_004426AE;
    if (v_stack_m230 < 0) goto loc_004425DD;
    if (v_stack_m59 == 0) goto loc_0044266F;
loc_004425DD:
    result = ExAcquireResourceSharedLite(*(uint64_t *)(v_stack_m218 + 0x30), 1, v_stack_m1F0, v_stack_m1E0);
    Arg1 = (v_stack_m230 >= 0) ? 1 : 0;
    if (v_stack_m22A == 0) {
        Arg4 = *(uint64_t *)(v_stack_m218 + 0x450);
    }
    result = (uint32_t)(((uint32_t)(v_stack_m248)) | (v_stack_m208));
    v_stack_m2C0 = 0;
    v_stack_m2C8 = (uint8_t)(Arg1);
    v_stack_m2D0 = (uint32_t)(result);
    v_stack_m2D8 = v_stack_m200;
    Arg3 = 0;
    Arg2 = 0;
    result = SeLogAccessFailure(v_stack_m218, Arg2, Arg3, Arg4);
    result = ExReleaseResourceLite(*(uint64_t *)(v_stack_m218 + 0x30), Arg2, Arg3, Arg4);
    result = KeLeaveCriticalRegion(*(uint64_t *)(v_stack_m218 + 0x30), Arg2, Arg3, Arg4);
loc_0044266F:
    if (sign_flag) goto loc_004426AE;
    if (v_stack_m230 >= 0) goto loc_004426AE;
    if (v_stack_m64 != 0) goto loc_004426AE;
    if (((*(uint32_t *)(v_stack_m218 + 0xC8)) & (0x4000ULL)) == 0) goto loc_004426AE;
    result = SepLpacCausedAccessFailure(v_stack_m70, (uint32_t)(v_stack_m248), Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        result = SepLogLpacAccessFailure(v_stack_m70, (uint32_t)(v_stack_m248), Arg3, Arg4);
    }
    if (Arg12 == 0) goto loc_004426D9;
    if (v_stack_m228 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m228;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m190 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m190;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m218 != 0) {
        Arg2 = 0x74726853ULL;
        Arg1 = v_stack_m218;
        result = ObfDereferenceObjectWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m178 != 0) {
        result = SeFreeCapturedObjectTypeList(v_stack_m178, Arg2, Arg3, Arg4);
    }
    if (v_stack_m170 != 0) {
        Arg3 = 1;
        Arg2 = v_stack_m250;
        result = SeReleaseSid(v_stack_m170, Arg2, Arg3, Arg4);
    }
    if (v_stack_m200 != 0) {
        Arg3 = 0;
        Arg2 = v_stack_m250;
        Arg1 = v_stack_m200;
        result = SeReleaseSecurityDescriptor(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m240 != 0) {
        Arg1 = v_stack_m188;
        result = SepRmDereferenceCap(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m160 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m160, Arg2, Arg3, Arg4);
    }
    result = SepFreeResourceInfo(v_stack_m1A8, Arg2, Arg3, Arg4);
loc_00442772:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (704);
    return result;
loc_00442796:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x6` | `64` | `R` |
| `Arg9` | `+ 0x0` | `32` | `R` |
| `Arg10` | `+ 0x0` | `32` | `W` |
| `Arg11` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00440BC8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
