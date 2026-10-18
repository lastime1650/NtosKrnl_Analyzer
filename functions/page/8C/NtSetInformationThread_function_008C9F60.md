# NtSetInformationThread

- RVA: `0x008C9F60`–`0x008CB9A6` (길이 `6,726` bytes)
- VA: `0x00000001408C9F60`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00084210`
- 디코드: `1,476`개 명령, `6,726/6,726` bytes 표시
- 미해석 바이트: `19` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **105**; 고유 호출 대상: **49**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x008C9FBE` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008CA0ED` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x008CA109` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x008CA1CA` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CA1F3` → [KeSetActualBasePriorityThread](../../text/3C/KeSetActualBasePriorityThread_function_003C4370.md) (function, `0x003C4370`)
- `0x008CA200` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CA256` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CA292` → [PsImpersonateClient](PsImpersonateClient_function_008CBE10.md) (function, `0x008CBE10`)
- `0x008CA2A1` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CA348` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CA37B` → [PspThreadFromTicket](PspThreadFromTicket_function_008CB9B0.md) (function, `0x008CB9B0`)
- `0x008CA39D` → [PspUpdateContainerImpersonation](../../text/39/PspUpdateContainerImpersonation_function_003931EC.md) (function, `0x003931EC`)
- `0x008CA3AA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008CA3B7` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CA441` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CA455` → [KeSetPriorityThread](../../text/2C/KeSetPriorityThread_function_002C76E0.md) (function, `0x002C76E0`)
- `0x008CA464` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CA49E` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x008CA4DA` → [PsImpersonateClient](PsImpersonateClient_function_008CBE10.md) (function, `0x008CBE10`)
- `0x008CA4E4` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008CA55B` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CA590` → [KeAbUserModeEntryFree](../../text/47/KeAbUserModeEntryFree_function_004744D0.md) (function, `0x004744D0`)
- `0x008CA5D6` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CA5EF` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x008CA60B` → [PspWow64SetContextThread](PspWow64SetContextThread_function_008CCC88.md) (function, `0x008CCC88`)
- `0x008CA619` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x008CA626` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CA67B` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CA6E1` → [KeSetBasePriorityThread](../../text/3C/KeSetBasePriorityThread_function_003C6EB0.md) (function, `0x003C6EB0`)
- `0x008CA6F2` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CA71A` → [KeQueryHeteroCpuPolicyThread](../../text/48/KeQueryHeteroCpuPolicyThread_function_00488A70.md) (function, `0x00488A70`)
- `0x008CA727` → [Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting](../../text/22/Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting_function_00222FE0.md) (function, `0x00222FE0`)
- `0x008CA761` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CA775` → [PsSetPagePriorityThread](../../text/3C/PsSetPagePriorityThread_function_003C4138.md) (function, `0x003C4138`)
- `0x008CA7D3` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CA865` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)
- `0x008CA8C4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x008CA8F7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x008CA926` → [PspLockThreadSecurityExclusive](../../text/4E/PspLockThreadSecurityExclusive_function_004E96E0.md) (function, `0x004E96E0`)
- `0x008CA954` → [EtwTraceThreadSetName](../A1/EtwTraceThreadSetName_function_00A1DBD8.md) (function, `0x00A1DBD8`)
- `0x008CA9AA` → [PspUnlockThreadSecurityExclusive](../../text/4E/PspUnlockThreadSecurityExclusive_function_004E97C0.md) (function, `0x004E97C0`)
- `0x008CA9C0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CA9D7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008CA9ED` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008CAA56` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CAA76` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x008CAA89` → [KiSetLegacyAffinityThread](../../text/2C/KiSetLegacyAffinityThread_function_002CDD94.md) (function, `0x002CDD94`)
- `0x008CAA98` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x008CAAB0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CAB1A` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CAB6C` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CAB8C` → [PspSchedulerSharedDataRegionSlotAllocate](../A2/PspSchedulerSharedDataRegionSlotAllocate_function_00A268C8.md) (function, `0x00A268C8`)
- `0x008CABC6` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CAC41` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CAC56` → [KeSetIdealProcessorThread](../../text/2D/KeSetIdealProcessorThread_function_002DD150.md) (function, `0x002DD150`)
- `0x008CAC68` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CAC8D` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x008CACA7` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CACB6` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x008CAD5E` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CAD73` → [PspSetThreadPpmPolicy](../A5/PspSetThreadPpmPolicy_function_00A56460.md) (function, `0x00A56460`)
- `0x008CADDA` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CADF6` → [KeSetDisableBoostThread](../../text/3C/KeSetDisableBoostThread_function_003C19BC.md) (function, `0x003C19BC`)
- `0x008CAE05` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CAE4C` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CAE6D` → [PsSetIoPriorityThread](../../text/3C/PsSetIoPriorityThread_function_003C3FBC.md) (function, `0x003C3FBC`)
- `0x008CAE7A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CAEEA` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CAF0B` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CAF2C` → [PsGetNextProcessThread](PsGetNextProcessThread_function_008C9CF0.md) (function, `0x008C9CF0`)
- `0x008CAF55` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x008CB0AB` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x008CB0B6` → [PsGetNextProcessThread](PsGetNextProcessThread_function_008C9CF0.md) (function, `0x008C9CF0`)
- `0x008CB0DE` → [KeQueryActiveGroupCount](../../text/48/KeQueryActiveGroupCount_function_0048C600.md) (function, `0x0048C600`)
- `0x008CB16F` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CB198` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008CB1CD` → [PspLockProcessShared](../../text/40/PspLockProcessShared_function_004016D0.md) (function, `0x004016D0`)
- `0x008CB1EC` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x008CB20C` → [KeSetUserAffinityThread](../../text/2C/KeSetUserAffinityThread_function_002CFA2C.md) (function, `0x002CFA2C`)
- `0x008CB219` → [KeQueryPrimaryGroupProcess](../../text/2C/KeQueryPrimaryGroupProcess_function_002CF958.md) (function, `0x002CF958`)
- `0x008CB297` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CB2B6` → [KeSetIdealProcessorThreadByNumber](../../text/2D/KeSetIdealProcessorThreadByNumber_function_002DD200.md) (function, `0x002DD200`)
- `0x008CB2CD` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CB30E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x008CB319` → [PspUnlockProcessShared](../../text/26/PspUnlockProcessShared_function_00263950.md) (function, `0x00263950`)
- `0x008CB332` → [KeIsSubsetAffinityEx](../../text/2C/KeIsSubsetAffinityEx_function_002CDC80.md) (function, `0x002CDC80`)
- `0x008CB3B1` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CB3E4` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CB427` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CB449` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (function, `0x002250A0`)
- `0x008CB482` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CB4EF` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x008CB52F` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CB593` → [SeCheckPrivilegedObject](../9F/SeCheckPrivilegedObject_function_009F62CC.md) (function, `0x009F62CC`)
- `0x008CB5B4` → [SeCheckPrivilegedObject](../9F/SeCheckPrivilegedObject_function_009F62CC.md) (function, `0x009F62CC`)
- `0x008CB615` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CB686` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CB6B5` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CB6DD` → [IoBoostThreadIoPriority](../../text/21/IoBoostThreadIoPriority_function_00216110.md) (function, `0x00216110`)
- `0x008CB730` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x008CB7B5` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008CB81C` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x008CB83F` → [RtlTestProtectedAccess](../A1/RtlTestProtectedAccess_function_00A100C8.md) (function, `0x00A100C8`)
- `0x008CB86C` → [PspSchedulerSharedDataRegionSlotFree](../90/PspSchedulerSharedDataRegionSlotFree_function_00905AD4.md) (function, `0x00905AD4`)
- `0x008CB97E` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [EtwpLogger](../9B/EtwpLogger_function_009BE310.md) at `0x009BE39E`
- [EtwpLogger](../9B/EtwpLogger_function_009BE310.md) at `0x009BE7FD`

### Static image references
- `0x008C9F7D` → RVA `0x00E0A740` (`.data`; read)
- `0x008CA047` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x008CA19D` → RVA `0x00FC6AC8` (`ALMOSTRO`; read)
- `0x008CA478` → RVA `0x00FD8020` (`PAGEDATA`; read)
- `0x008CAB35` → RVA `0x00FC7030` (`ALMOSTRO`; read)
- `0x008CAC86` → RVA `0x00FD9AE8` (`PAGEDATA`; read)
- `0x008CB4E8` → RVA `0x00FD9A80` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **60**
  - `0x008C9FBE` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008CA1F3` → [KeSetActualBasePriorityThread](../../text/3C/KeSetActualBasePriorityThread_function_003C4370.md) (`PAGE` → `.text`)
  - `0x008CA200` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CA2A1` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CA39D` → [PspUpdateContainerImpersonation](../../text/39/PspUpdateContainerImpersonation_function_003931EC.md) (`PAGE` → `.text`)
  - `0x008CA3AA` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008CA3B7` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CA455` → [KeSetPriorityThread](../../text/2C/KeSetPriorityThread_function_002C76E0.md) (`PAGE` → `.text`)
  - `0x008CA464` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CA4E4` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008CA590` → [KeAbUserModeEntryFree](../../text/47/KeAbUserModeEntryFree_function_004744D0.md) (`PAGE` → `.text`)
  - `0x008CA5EF` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x008CA619` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x008CA626` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CA6E1` → [KeSetBasePriorityThread](../../text/3C/KeSetBasePriorityThread_function_003C6EB0.md) (`PAGE` → `.text`)
  - `0x008CA6F2` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CA71A` → [KeQueryHeteroCpuPolicyThread](../../text/48/KeQueryHeteroCpuPolicyThread_function_00488A70.md) (`PAGE` → `.text`)
  - `0x008CA727` → [Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting](../../text/22/Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledPreCheckWithReporting_function_00222FE0.md) (`PAGE` → `.text`)
  - `0x008CA775` → [PsSetPagePriorityThread](../../text/3C/PsSetPagePriorityThread_function_003C4138.md) (`PAGE` → `.text`)
  - `0x008CA8C4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x008CA8F7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x008CA926` → [PspLockThreadSecurityExclusive](../../text/4E/PspLockThreadSecurityExclusive_function_004E96E0.md) (`PAGE` → `.text`)
  - `0x008CA9AA` → [PspUnlockThreadSecurityExclusive](../../text/4E/PspUnlockThreadSecurityExclusive_function_004E97C0.md) (`PAGE` → `.text`)
  - `0x008CA9C0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CA9D7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008CA9ED` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008CAA76` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x008CAA89` → [KiSetLegacyAffinityThread](../../text/2C/KiSetLegacyAffinityThread_function_002CDD94.md) (`PAGE` → `.text`)
  - `0x008CAA98` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x008CAAB0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CABC6` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CAC56` → [KeSetIdealProcessorThread](../../text/2D/KeSetIdealProcessorThread_function_002DD150.md) (`PAGE` → `.text`)
  - `0x008CAC68` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CACA7` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CACB6` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x008CADF6` → [KeSetDisableBoostThread](../../text/3C/KeSetDisableBoostThread_function_003C19BC.md) (`PAGE` → `.text`)
  - `0x008CAE05` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CAE6D` → [PsSetIoPriorityThread](../../text/3C/PsSetIoPriorityThread_function_003C3FBC.md) (`PAGE` → `.text`)
  - `0x008CAE7A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CAF0B` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CAF55` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x008CB0AB` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x008CB0DE` → [KeQueryActiveGroupCount](../../text/48/KeQueryActiveGroupCount_function_0048C600.md) (`PAGE` → `.text`)
  - `0x008CB198` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008CB1CD` → [PspLockProcessShared](../../text/40/PspLockProcessShared_function_004016D0.md) (`PAGE` → `.text`)
  - `0x008CB1EC` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x008CB20C` → [KeSetUserAffinityThread](../../text/2C/KeSetUserAffinityThread_function_002CFA2C.md) (`PAGE` → `.text`)
  - `0x008CB219` → [KeQueryPrimaryGroupProcess](../../text/2C/KeQueryPrimaryGroupProcess_function_002CF958.md) (`PAGE` → `.text`)
  - `0x008CB2B6` → [KeSetIdealProcessorThreadByNumber](../../text/2D/KeSetIdealProcessorThreadByNumber_function_002DD200.md) (`PAGE` → `.text`)
  - `0x008CB2CD` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CB30E` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x008CB319` → [PspUnlockProcessShared](../../text/26/PspUnlockProcessShared_function_00263950.md) (`PAGE` → `.text`)
  - `0x008CB332` → [KeIsSubsetAffinityEx](../../text/2C/KeIsSubsetAffinityEx_function_002CDC80.md) (`PAGE` → `.text`)
  - `0x008CB3E4` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CB449` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (`PAGE` → `.text`)
  - `0x008CB482` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CB6B5` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CB6DD` → [IoBoostThreadIoPriority](../../text/21/IoBoostThreadIoPriority_function_00216110.md) (`PAGE` → `.text`)
  - `0x008CB7B5` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008CB97E` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x008CB7EA` → [sub_00B1B2E4 + 0x285](../B1/Unknown_function_00B1B2E4.md) (`tail-transfer`)
  - `0x008CB7FA` → [sub_00B1B2E4 + 0x4D1](../B1/Unknown_function_00B1B2E4.md) (`tail-transfer`)
  - `0x008CB846` → [sub_00B1B2E4 + 0x4D1](../B1/Unknown_function_00B1B2E4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008C9F60  48 8B C4                        mov rax, rsp
008C9F63  53                              push rbx
008C9F64  56                              push rsi
008C9F65  57                              push rdi
008C9F66  41 54                           push r12
008C9F68  41 55                           push r13
008C9F6A  41 56                           push r14
008C9F6C  41 57                           push r15
008C9F6E  48 81 EC F0 03 00 00            sub rsp, 0x3f0
008C9F75  0F 29 70 B8                     movaps xmmword ptr [rax - 0x48], xmm6
008C9F79  0F 29 78 A8                     movaps xmmword ptr [rax - 0x58], xmm7
008C9F7D  48 8B 05 BC 07 54 00            mov rax, qword ptr [rip + 0x5407bc]
008C9F84  48 33 C4                        xor rax, rsp
008C9F87  48 89 84 24 C0 03 00 00         mov qword ptr [rsp + 0x3c0], rax
008C9F8F  45 8B F9                        mov r15d, r9d
008C9F92  4D 8B E0                        mov r12, r8
008C9F95  8B DA                           mov ebx, edx
008C9F97  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
008C9F9C  33 FF                           xor edi, edi
008C9F9E  48 89 7C 24 48                  mov qword ptr [rsp + 0x48], rdi
008C9FA3  0F 57 C0                        xorps xmm0, xmm0
008C9FA6  0F 11 84 24 C0 00 00 00         movups xmmword ptr [rsp + 0xc0], xmm0
008C9FAE  33 D2                           xor edx, edx
008C9FB0  41 B8 08 01 00 00               mov r8d, 0x108
008C9FB6  48 8D 8C 24 B0 01 00 00         lea rcx, [rsp + 0x1b0]
008C9FBE  E8 7D CC DF FF                  call 0x1406c6c40
008C9FC3  66 89 7C 24 74                  mov word ptr [rsp + 0x74], di
008C9FC8  89 BC 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], edi
008C9FCF  89 7C 24 64                     mov dword ptr [rsp + 0x64], edi
008C9FD3  89 BC 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], edi
008C9FDA  48 89 BC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdi
008C9FE2  48 89 BC 24 38 01 00 00         mov qword ptr [rsp + 0x138], rdi
008C9FEA  0F 57 C0                        xorps xmm0, xmm0
008C9FED  33 C0                           xor eax, eax
008C9FEF  0F 11 84 24 D0 00 00 00         movups xmmword ptr [rsp + 0xd0], xmm0
008C9FF7  48 89 84 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rax
008C9FFF  0F 11 84 24 58 01 00 00         movups xmmword ptr [rsp + 0x158], xmm0
008CA007  89 7C 24 78                     mov dword ptr [rsp + 0x78], edi
008CA00B  48 89 BC 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rdi
008CA013  0F 11 84 24 00 01 00 00         movups xmmword ptr [rsp + 0x100], xmm0
008CA01B  48 89 BC 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rdi
008CA023  65 4C 8B 04 25 88 01 00 00      mov r8, qword ptr gs:[0x188]
008CA02C  4C 89 44 24 68                  mov qword ptr [rsp + 0x68], r8
008CA031  45 0F B6 88 32 02 00 00         movzx r9d, byte ptr [r8 + 0x232]
008CA039  44 88 4C 24 40                  mov byte ptr [rsp + 0x40], r9b
008CA03E  45 84 C9                        test r9b, r9b
008CA041  0F 84 7C 03 00 00               je 0x1408ca3c3
008CA047  48 8D 35 B2 5F 73 FF            lea rsi, [rip - 0x8ca04e]
008CA04E  83 FB 02                        cmp ebx, 2
008CA051  75 51                           jne 0x1408ca0a4
008CA053  41 B8 04 00 00 00               mov r8d, 4
008CA059  44 89 44 24 64                  mov dword ptr [rsp + 0x64], r8d
008CA05E  45 8D 70 04                     lea r14d, [r8 + 4]
008CA062  41 BD 01 00 00 00               mov r13d, 1
008CA068  45 85 FF                        test r15d, r15d
008CA06B  74 2B                           je 0x1408ca098
008CA06D  41 8D 48 FF                     lea ecx, [r8 - 1]
008CA071  49 85 CC                        test r12, rcx
008CA074  75 77                           jne 0x1408ca0ed
008CA076  4B 8D 0C 3C                     lea rcx, [r12 + r15]
008CA07A  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
008CA084  49 3B CC                        cmp rcx, r12
008CA087  72 05                           jb 0x1408ca08e
008CA089  48 3B CA                        cmp rcx, rdx
008CA08C  76 64                           jbe 0x1408ca0f2
008CA08E  0F B6 02                        movzx eax, byte ptr [rdx]
008CA091  44 8B 44 24 64                  mov r8d, dword ptr [rsp + 0x64]
008CA096  EB 5A                           jmp 0x1408ca0f2
008CA098  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
008CA0A2  EB 4E                           jmp 0x1408ca0f2
008CA0A4  8D 43 FC                        lea eax, [rbx - 4]
008CA0A7  83 F8 34                        cmp eax, 0x34
008CA0AA  77 A7                           ja 0x1408ca053
008CA0AC  48 98                           cdqe
008CA0AE  0F B6 84 06 88 B8 8C 00         movzx eax, byte ptr [rsi + rax + 0x8cb888]
008CA0B6  8B 8C 86 78 B8 8C 00            mov ecx, dword ptr [rsi + rax*4 + 0x8cb878]
008CA0BD  48 03 CE                        add rcx, rsi
008CA0C0  FF E1                           jmp rcx
008CA0C2  CC                              int3
008CA0C3  CC                              int3
008CA0C4  CC                              int3
008CA0C5  CC                              int3
008CA0C6  41 BE 08 00 00 00               mov r14d, 8
008CA0CC  45 8B C6                        mov r8d, r14d
008CA0CF  44 89 74 24 64                  mov dword ptr [rsp + 0x64], r14d
008CA0D4  EB 8C                           jmp 0x1408ca062
008CA0D6  41 BD 01 00 00 00               mov r13d, 1
008CA0DC  45 8B C5                        mov r8d, r13d
008CA0DF  44 89 6C 24 64                  mov dword ptr [rsp + 0x64], r13d
008CA0E4  45 8D 75 07                     lea r14d, [r13 + 7]
008CA0E8  E9 7B FF FF FF                  jmp 0x1408ca068
008CA0ED  E8 DE FE FC FF                  call 0x140899fd0
008CA0F2  EB 05                           jmp 0x1408ca0f9
008CA0F4  E9 7A 18 00 00                  jmp 0x1408cb973
008CA0F9  83 FB 39                        cmp ebx, 0x39
008CA0FC  74 05                           je 0x1408ca103
008CA0FE  83 FB 30                        cmp ebx, 0x30
008CA101  75 1B                           jne 0x1408ca11e
008CA103  49 8B D7                        mov rdx, r15
008CA106  49 8B CC                        mov rcx, r12
008CA109  E8 B2 F0 01 00                  call 0x1408e91c0
008CA10E  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
008CA118  44 0F B6 4C 24 40               movzx r9d, byte ptr [rsp + 0x40]
008CA11E  4C 8B 44 24 68                  mov r8, qword ptr [rsp + 0x68]
008CA123  EB 05                           jmp 0x1408ca12a
008CA125  E9 49 18 00 00                  jmp 0x1408cb973
008CA12A  83 FB 05                        cmp ebx, 5
008CA12D  0F 84 D9 00 00 00               je 0x1408ca20c
008CA133  83 FB 2C                        cmp ebx, 0x2c
008CA136  0F 84 B8 01 00 00               je 0x1408ca2f4
008CA13C  83 FB 02                        cmp ebx, 2
008CA13F  0F 84 9E 02 00 00               je 0x1408ca3e3
008CA145  83 FB 09                        cmp ebx, 9
008CA148  0F 84 9B 01 00 00               je 0x1408ca2e9
008CA14E  83 C3 FD                        add ebx, -3
008CA151  83 FB 36                        cmp ebx, 0x36
008CA154  0F 87 1D 14 00 00               ja 0x1408cb577
008CA15A  48 63 C3                        movsxd rax, ebx
008CA15D  0F B6 84 06 3C B9 8C 00         movzx eax, byte ptr [rsi + rax + 0x8cb93c]
008CA165  8B 8C 86 C0 B8 8C 00            mov ecx, dword ptr [rsi + rax*4 + 0x8cb8c0]
008CA16C  48 03 CE                        add rcx, rsi
008CA16F  FF E1                           jmp rcx
008CA171  CC                              int3
008CA172  CC                              int3
008CA173  CC                              int3
008CA174  CC                              int3
008CA175  41 83 FF 04                     cmp r15d, 4
008CA179  0F 85 79 03 00 00               jne 0x1408ca4f8
008CA17F  41 8B 1C 24                     mov ebx, dword ptr [r12]
008CA183  89 9C 24 94 00 00 00            mov dword ptr [rsp + 0x94], ebx
008CA18A  EB 05                           jmp 0x1408ca191
008CA18C  E9 E2 17 00 00                  jmp 0x1408cb973
008CA191  8D 43 FF                        lea eax, [rbx - 1]
008CA194  83 F8 1E                        cmp eax, 0x1e
008CA197  0F 87 4C 01 00 00               ja 0x1408ca2e9
008CA19D  4C 8B 05 24 C9 6F 00            mov r8, qword ptr [rip + 0x6fc924]
008CA1A4  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CA1A9  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CA1AE  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CA1B3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CA1B8  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CA1C0  BA 00 04 00 00                  mov edx, 0x400
008CA1C5  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CA1CA  E8 81 F4 F9 FF                  call 0x140869650
008CA1CF  8B F0                           mov esi, eax
008CA1D1  85 C0                           test eax, eax
008CA1D3  0F 88 9A 17 00 00               js 0x1408cb973
008CA1D9  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
008CA1DE  48 8B 87 20 02 00 00            mov rax, qword ptr [rdi + 0x220]
008CA1E5  83 FB 10                        cmp ebx, 0x10
008CA1E8  0F 8D 86 0A 00 00               jge 0x1408cac74
008CA1EE  8B D3                           mov edx, ebx
008CA1F0  48 8B CF                        mov rcx, rdi
008CA1F3  E8 78 A1 AF FF                  call 0x1403c4370
008CA1F8  48 8B CF                        mov rcx, rdi
008CA1FB  BA 50 73 51 79                  mov edx, 0x79517350
008CA200  E8 DB D6 A2 FF                  call 0x1402f78e0
008CA205  8B C6                           mov eax, esi
008CA207  E9 67 17 00 00                  jmp 0x1408cb973
008CA20C  41 83 FF 08                     cmp r15d, 8
008CA210  0F 85 E2 02 00 00               jne 0x1408ca4f8
008CA216  49 8B 04 24                     mov rax, qword ptr [r12]
008CA21A  48 89 84 24 50 01 00 00         mov qword ptr [rsp + 0x150], rax
008CA222  EB 05                           jmp 0x1408ca229
008CA224  E9 4A 17 00 00                  jmp 0x1408cb973
008CA229  4C 8B 05 98 C8 6F 00            mov r8, qword ptr [rip + 0x6fc898]
008CA230  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CA235  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CA23A  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CA23F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CA244  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CA24C  BA 80 00 00 00                  mov edx, 0x80
008CA251  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CA256  E8 F5 F3 F9 FF                  call 0x140869650
008CA25B  85 C0                           test eax, eax
008CA25D  0F 88 10 17 00 00               js 0x1408cb973
008CA263  65 4C 8B 0C 25 88 01 00 00      mov r9, qword ptr gs:[0x188]
008CA26C  48 8B 8C 24 50 01 00 00         mov rcx, qword ptr [rsp + 0x150]
008CA274  48 85 C9                        test rcx, rcx
008CA277  0F 85 F3 01 00 00               jne 0x1408ca470
008CA27D  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
008CA285  45 33 C9                        xor r9d, r9d
008CA288  45 33 C0                        xor r8d, r8d
008CA28B  33 D2                           xor edx, edx
008CA28D  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008CA292  E8 79 1B 00 00                  call 0x1408cbe10
008CA297  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008CA29C  BA 50 73 51 79                  mov edx, 0x79517350
008CA2A1  E8 3A D6 A2 FF                  call 0x1402f78e0
008CA2A6  8B C7                           mov eax, edi
008CA2A8  E9 C6 16 00 00                  jmp 0x1408cb973
008CA2AD  41 8D 47 FC                     lea eax, [r15 - 4]
008CA2B1  A9 FB FF FF FF                  test eax, 0xfffffffb
008CA2B6  0F 85 3C 02 00 00               jne 0x1408ca4f8
008CA2BC  41 83 FF 04                     cmp r15d, 4
008CA2C0  0F 84 C0 0B 00 00               je 0x1408cae86
008CA2C6  49 8B 1C 24                     mov rbx, qword ptr [r12]
008CA2CA  48 89 9C 24 38 01 00 00         mov qword ptr [rsp + 0x138], rbx
008CA2D2  4C 8B F3                        mov r14, rbx
008CA2D5  49 C1 EE 20                     shr r14, 0x20
008CA2D9  EB 05                           jmp 0x1408ca2e0
008CA2DB  E9 93 16 00 00                  jmp 0x1408cb973
008CA2E0  83 FB 04                        cmp ebx, 4
008CA2E3  0F 82 28 0B 00 00               jb 0x1408cae11
008CA2E9  B8 0D 00 00 C0                  mov eax, 0xc000000d
008CA2EE  E9 80 16 00 00                  jmp 0x1408cb973
008CA2F3  CC                              int3
008CA2F4  48 83 7C 24 58 FE               cmp qword ptr [rsp + 0x58], -2
008CA2FA  75 ED                           jne 0x1408ca2e9
008CA2FC  41 83 FF 08                     cmp r15d, 8
008CA300  0F 85 F2 01 00 00               jne 0x1408ca4f8
008CA306  49 8B 1C 24                     mov rbx, qword ptr [r12]
008CA30A  48 89 9C 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], rbx
008CA312  EB 05                           jmp 0x1408ca319
008CA314  E9 5A 16 00 00                  jmp 0x1408cb973
008CA319  4C 8B 05 A8 C7 6F 00            mov r8, qword ptr [rip + 0x6fc7a8]
008CA320  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CA325  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CA32A  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CA32F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CA334  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CA33C  BA 00 04 00 00                  mov edx, 0x400
008CA341  48 C7 C1 FE FF FF FF            mov rcx, 0xfffffffffffffffe
008CA348  E8 03 F3 F9 FF                  call 0x140869650
008CA34D  8B F0                           mov esi, eax
008CA34F  85 C0                           test eax, eax
008CA351  0F 88 1C 16 00 00               js 0x1408cb973
008CA357  48 89 BC 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdi
008CA35F  48 85 DB                        test rbx, rbx
008CA362  8B C7                           mov eax, edi
008CA364  0F 94 C0                        sete al
008CA367  85 C0                           test eax, eax
008CA369  75 27                           jne 0x1408ca392
008CA36B  48 8D 94 24 80 00 00 00         lea rdx, [rsp + 0x80]
008CA373  48 8D 8C 24 F8 00 00 00         lea rcx, [rsp + 0xf8]
008CA37B  E8 30 16 00 00                  call 0x1408cb9b0
008CA380  8B F0                           mov esi, eax
008CA382  48 8B BC 24 80 00 00 00         mov rdi, qword ptr [rsp + 0x80]
008CA38A  85 C0                           test eax, eax
008CA38C  0F 88 67 06 00 00               js 0x1408ca9f9
008CA392  48 8B D7                        mov rdx, rdi
008CA395  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008CA39A  48 8B CB                        mov rcx, rbx
008CA39D  E8 4A 8E AC FF                  call 0x1403931ec
008CA3A2  48 85 FF                        test rdi, rdi
008CA3A5  74 08                           je 0x1408ca3af
008CA3A7  48 8B CF                        mov rcx, rdi
008CA3AA  E8 A1 EF A2 FF                  call 0x1402f9350
008CA3AF  48 8B CB                        mov rcx, rbx
008CA3B2  BA 50 73 51 79                  mov edx, 0x79517350
008CA3B7  E8 24 D5 A2 FF                  call 0x1402f78e0
008CA3BC  8B C6                           mov eax, esi
008CA3BE  E9 B0 15 00 00                  jmp 0x1408cb973
008CA3C3  48 8D 35 36 5C 73 FF            lea rsi, [rip - 0x8ca3ca]
008CA3CA  48 BA 00 00 FF FF FF 7F 00 00   movabs rdx, 0x7fffffff0000
008CA3D4  41 BE 08 00 00 00               mov r14d, 8
008CA3DA  45 8D 6E F9                     lea r13d, [r14 - 7]
008CA3DE  E9 47 FD FF FF                  jmp 0x1408ca12a
008CA3E3  41 83 FF 04                     cmp r15d, 4
008CA3E7  0F 85 0B 01 00 00               jne 0x1408ca4f8
008CA3ED  41 8B 1C 24                     mov ebx, dword ptr [r12]
008CA3F1  89 9C 24 20 01 00 00            mov dword ptr [rsp + 0x120], ebx
008CA3F8  EB 05                           jmp 0x1408ca3ff
008CA3FA  E9 74 15 00 00                  jmp 0x1408cb973
008CA3FF  8D 43 FF                        lea eax, [rbx - 1]
008CA402  83 F8 1E                        cmp eax, 0x1e
008CA405  0F 87 DE FE FF FF               ja 0x1408ca2e9
008CA40B  83 FB 10                        cmp ebx, 0x10
008CA40E  0F 8D 6D 11 00 00               jge 0x1408cb581
008CA414  4C 8B 05 AD C6 6F 00            mov r8, qword ptr [rip + 0x6fc6ad]
008CA41B  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CA420  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CA425  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CA42A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CA42F  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CA437  BA 00 04 00 00                  mov edx, 0x400
008CA43C  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CA441  E8 0A F2 F9 FF                  call 0x140869650
008CA446  85 C0                           test eax, eax
008CA448  0F 88 25 15 00 00               js 0x1408cb973
008CA44E  8B D3                           mov edx, ebx
008CA450  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008CA455  E8 86 D2 9F FF                  call 0x1402c76e0
008CA45A  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008CA45F  BA 50 73 51 79                  mov edx, 0x79517350
008CA464  E8 77 D4 A2 FF                  call 0x1402f78e0
008CA469  33 C0                           xor eax, eax
008CA46B  E9 03 15 00 00                  jmp 0x1408cb973
008CA470  45 0F B6 89 32 02 00 00         movzx r9d, byte ptr [r9 + 0x232]
008CA478  4C 8B 05 A1 DB 70 00            mov r8, qword ptr [rip + 0x70dba1]
008CA47F  48 89 BC 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdi
008CA487  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
008CA48C  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
008CA494  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008CA499  BA 04 00 00 00                  mov edx, 4
008CA49E  E8 0D E9 F9 FF                  call 0x140868db0
008CA4A3  8B F8                           mov edi, eax
008CA4A5  85 C0                           test eax, eax
008CA4A7  0F 88 EA FD FF FF               js 0x1408ca297
008CA4AD  48 8B 9C 24 80 00 00 00         mov rbx, qword ptr [rsp + 0x80]
008CA4B5  83 BB C0 00 00 00 02            cmp dword ptr [rbx + 0xc0], 2
008CA4BC  0F 85 F1 07 00 00               jne 0x1408cacb3
008CA4C2  8B 83 C4 00 00 00               mov eax, dword ptr [rbx + 0xc4]
008CA4C8  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008CA4CC  45 33 C9                        xor r9d, r9d
008CA4CF  45 33 C0                        xor r8d, r8d
008CA4D2  48 8B D3                        mov rdx, rbx
008CA4D5  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008CA4DA  E8 31 19 00 00                  call 0x1408cbe10
008CA4DF  8B F8                           mov edi, eax
008CA4E1  48 8B CB                        mov rcx, rbx
008CA4E4  E8 67 EE A2 FF                  call 0x1402f9350
008CA4E9  E9 A9 FD FF FF                  jmp 0x1408ca297
008CA4EE  41 83 FF 18                     cmp r15d, 0x18
008CA4F2  0F 84 C4 05 00 00               je 0x1408caabc
008CA4F8  B8 04 00 00 C0                  mov eax, 0xc0000004
008CA4FD  E9 71 14 00 00                  jmp 0x1408cb973
008CA502  41 83 FF 10                     cmp r15d, 0x10
008CA506  75 F0                           jne 0x1408ca4f8
008CA508  41 0F 10 04 24                  movups xmm0, xmmword ptr [r12]
008CA50D  0F 11 84 24 58 01 00 00         movups xmmword ptr [rsp + 0x158], xmm0
008CA515  EB 09                           jmp 0x1408ca520
008CA517  8B F0                           mov esi, eax
008CA519  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008CA51E  EB 79                           jmp 0x1408ca599
008CA520  83 BC 24 60 01 00 00 00         cmp dword ptr [rsp + 0x160], 0
008CA528  0F 85 4F 08 00 00               jne 0x1408cad7d
008CA52E  4C 8B 05 93 C5 6F 00            mov r8, qword ptr [rip + 0x6fc593]
008CA535  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CA53A  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CA53F  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CA544  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CA549  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CA551  BA 20 00 00 00                  mov edx, 0x20
008CA556  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CA55B  E8 F0 F0 F9 FF                  call 0x140869650
008CA560  8B F0                           mov esi, eax
008CA562  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008CA566  85 C0                           test eax, eax
008CA568  0F 88 14 08 00 00               js 0x1408cad82
008CA56E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008CA577  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008CA57C  48 3B D8                        cmp rbx, rax
008CA57F  0F 85 2F 0F 00 00               jne 0x1408cb4b4
008CA585  48 8B 94 24 58 01 00 00         mov rdx, qword ptr [rsp + 0x158]
008CA58D  48 8B CB                        mov rcx, rbx
008CA590  E8 3B 9F BA FF                  call 0x1404744d0
008CA595  8B 74 24 50                     mov esi, dword ptr [rsp + 0x50]
008CA599  48 85 DB                        test rbx, rbx
008CA59C  0F 85 0D FE FF FF               jne 0x1408ca3af
008CA5A2  8B C6                           mov eax, esi
008CA5A4  E9 CA 13 00 00                  jmp 0x1408cb973
008CA5A9  4C 8B 05 18 C5 6F 00            mov r8, qword ptr [rip + 0x6fc518]
008CA5B0  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CA5B5  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CA5BA  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CA5BF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CA5C4  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CA5CC  BA 10 00 00 00                  mov edx, 0x10
008CA5D1  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CA5D6  E8 75 F0 F9 FF                  call 0x140869650
008CA5DB  85 C0                           test eax, eax
008CA5DD  0F 88 90 13 00 00               js 0x1408cb973
008CA5E3  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
008CA5E8  48 8D 8F 88 05 00 00            lea rcx, [rdi + 0x588]
008CA5EF  E8 2C C0 94 FF                  call 0x140216620
008CA5F4  48 8B CF                        mov rcx, rdi
008CA5F7  84 C0                           test al, al
008CA5F9  0F 84 B1 11 00 00               je 0x1408cb7b0
008CA5FF  44 0F B6 4C 24 40               movzx r9d, byte ptr [rsp + 0x40]
008CA605  45 8B C7                        mov r8d, r15d
008CA608  49 8B D4                        mov rdx, r12
008CA60B  E8 78 26 00 00                  call 0x1408ccc88
008CA610  8B D8                           mov ebx, eax
008CA612  48 8D 8F 88 05 00 00            lea rcx, [rdi + 0x588]
008CA619  E8 62 F8 A7 FF                  call 0x140349e80
008CA61E  BA 50 73 51 79                  mov edx, 0x79517350
008CA623  48 8B CF                        mov rcx, rdi
008CA626  E8 B5 D2 A2 FF                  call 0x1402f78e0
008CA62B  8B C3                           mov eax, ebx
008CA62D  E9 41 13 00 00                  jmp 0x1408cb973
008CA632  41 83 FF 04                     cmp r15d, 4
008CA636  0F 85 BC FE FF FF               jne 0x1408ca4f8
008CA63C  41 8B 34 24                     mov esi, dword ptr [r12]
008CA640  89 B4 24 94 00 00 00            mov dword ptr [rsp + 0x94], esi
008CA647  EB 05                           jmp 0x1408ca64e
008CA649  E9 25 13 00 00                  jmp 0x1408cb973
008CA64E  4C 8B 05 73 C4 6F 00            mov r8, qword ptr [rip + 0x6fc473]
008CA655  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CA65A  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CA65F  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CA664  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CA669  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CA671  BA 00 04 00 00                  mov edx, 0x400
008CA676  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CA67B  E8 D0 EF F9 FF                  call 0x140869650
008CA680  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008CA684  85 C0                           test eax, eax
008CA686  0F 88 E7 12 00 00               js 0x1408cb973
008CA68C  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008CA691  48 8B 93 20 02 00 00            mov rdx, qword ptr [rbx + 0x220]
008CA698  8D 46 10                        lea eax, [rsi + 0x10]
008CA69B  83 F8 20                        cmp eax, 0x20
008CA69E  0F 87 A3 0D 00 00               ja 0x1408cb447
008CA6A4  48 B9 01 C0 07 00 01 00 00 00   movabs rcx, 0x10007c001
008CA6AE  48 0F A3 C1                     bt rcx, rax
008CA6B2  0F 83 8F 0D 00 00               jae 0x1408cb447
008CA6B8  48 8B 82 A0 02 00 00            mov rax, qword ptr [rdx + 0x2a0]
008CA6BF  48 85 C0                        test rax, rax
008CA6C2  74 0E                           je 0x1408ca6d2
008CA6C4  8B 80 20 04 00 00               mov eax, dword ptr [rax + 0x420]
008CA6CA  A8 20                           test al, 0x20
008CA6CC  0F 85 BC 0D 00 00               jne 0x1408cb48e
008CA6D2  8B 94 24 94 00 00 00            mov edx, dword ptr [rsp + 0x94]
008CA6D9  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008CA6DE  48 8B CB                        mov rcx, rbx
008CA6E1  E8 CA C7 AF FF                  call 0x1403c6eb0
008CA6E6  8B 74 24 50                     mov esi, dword ptr [rsp + 0x50]
008CA6EA  48 8B CB                        mov rcx, rbx
008CA6ED  BA 50 73 51 79                  mov edx, 0x79517350
008CA6F2  E8 E9 D1 A2 FF                  call 0x1402f78e0
008CA6F7  8B C6                           mov eax, esi
008CA6F9  E9 75 12 00 00                  jmp 0x1408cb973
008CA6FE  41 83 FF 04                     cmp r15d, 4
008CA702  0F 85 F0 FD FF FF               jne 0x1408ca4f8
008CA708  41 8B 1C 24                     mov ebx, dword ptr [r12]
008CA70C  89 9C 24 1C 01 00 00            mov dword ptr [rsp + 0x11c], ebx
008CA713  EB 05                           jmp 0x1408ca71a
008CA715  E9 59 12 00 00                  jmp 0x1408cb973
008CA71A  E8 51 E3 BB FF                  call 0x140488a70
008CA71F  3B D8                           cmp ebx, eax
008CA721  0F 87 C2 FB FF FF               ja 0x1408ca2e9
008CA727  E8 B4 88 95 FF                  call 0x140222fe0
008CA72C  3B D8                           cmp ebx, eax
008CA72E  0F 82 B5 FB FF FF               jb 0x1408ca2e9
008CA734  4C 8B 05 8D C3 6F 00            mov r8, qword ptr [rip + 0x6fc38d]
008CA73B  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CA740  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CA745  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CA74A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CA74F  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CA757  BA 20 00 00 00                  mov edx, 0x20
008CA75C  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CA761  E8 EA EE F9 FF                  call 0x140869650
008CA766  85 C0                           test eax, eax
008CA768  0F 88 05 12 00 00               js 0x1408cb973
008CA76E  8B D3                           mov edx, ebx
008CA770  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008CA775  E8 BE 99 AF FF                  call 0x1403c4138
008CA77A  E9 DB FC FF FF                  jmp 0x1408ca45a
008CA77F  C6 44 24 61 00                  mov byte ptr [rsp + 0x61], 0
008CA784  4C 8B F7                        mov r14, rdi
008CA787  48 89 BC 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdi
008CA78F  48 89 BC 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rdi
008CA797  44 88 74 24 60                  mov byte ptr [rsp + 0x60], r14b
008CA79C  41 83 FF 10                     cmp r15d, 0x10
008CA7A0  0F 85 E7 01 00 00               jne 0x1408ca98d
008CA7A6  4C 8B 05 1B C3 6F 00            mov r8, qword ptr [rip + 0x6fc31b]
008CA7AD  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CA7B2  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CA7B7  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CA7BC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CA7C1  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CA7C9  BA 00 04 00 00                  mov edx, 0x400
008CA7CE  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CA7D3  E8 78 EE F9 FF                  call 0x140869650
008CA7D8  8B F0                           mov esi, eax
008CA7DA  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008CA7DE  85 C0                           test eax, eax
008CA7E0  0F 88 90 01 00 00               js 0x1408ca976
008CA7E6  C6 44 24 61 01                  mov byte ptr [rsp + 0x61], 1
008CA7EB  80 7C 24 40 00                  cmp byte ptr [rsp + 0x40], 0
008CA7F0  0F 84 65 01 00 00               je 0x1408ca95b
008CA7F6  0F 57 C0                        xorps xmm0, xmm0
008CA7F9  0F 11 84 24 70 01 00 00         movups xmmword ptr [rsp + 0x170], xmm0
008CA801  49 B9 00 00 FF FF FF 7F 00 00   movabs r9, 0x7fffffff0000
008CA80B  49 8B C9                        mov rcx, r9
008CA80E  4D 3B E1                        cmp r12, r9
008CA811  49 0F 42 CC                     cmovb rcx, r12
008CA815  90                              nop
008CA816  8B 01                           mov eax, dword ptr [rcx]
008CA818  89 84 24 70 01 00 00            mov dword ptr [rsp + 0x170], eax
008CA81F  48 8B 51 08                     mov rdx, qword ptr [rcx + 8]
008CA823  48 89 94 24 78 01 00 00         mov qword ptr [rsp + 0x178], rdx
008CA82B  0F 28 84 24 70 01 00 00         movaps xmm0, xmmword ptr [rsp + 0x170]
008CA833  66 0F 7F 84 24 00 01 00 00      movdqa xmmword ptr [rsp + 0x100], xmm0
008CA83C  66 0F 7E C0                     movd eax, xmm0
008CA840  66 85 C0                        test ax, ax
008CA843  74 25                           je 0x1408ca86a
008CA845  F6 C2 01                        test dl, 1
008CA848  75 1B                           jne 0x1408ca865
008CA84A  0F B7 C0                        movzx eax, ax
008CA84D  4C 8D 04 10                     lea r8, [rax + rdx]
008CA851  48 8D 0C 02                     lea rcx, [rdx + rax]
008CA855  49 3B C9                        cmp rcx, r9
008CA858  77 05                           ja 0x1408ca85f
008CA85A  4C 3B C2                        cmp r8, rdx
008CA85D  73 0B                           jae 0x1408ca86a
008CA85F  41 0F B6 01                     movzx eax, byte ptr [r9]
008CA863  EB 05                           jmp 0x1408ca86a
008CA865  E8 66 F7 FC FF                  call 0x140899fd0
008CA86A  8B 74 24 50                     mov esi, dword ptr [rsp + 0x50]
008CA86E  4C 8B B4 24 98 00 00 00         mov r14, qword ptr [rsp + 0x98]
008CA876  EB 18                           jmp 0x1408ca890
008CA878  8B F0                           mov esi, eax
008CA87A  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008CA87E  4C 8B B4 24 98 00 00 00         mov r14, qword ptr [rsp + 0x98]
008CA886  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
008CA88B  E9 0B 01 00 00                  jmp 0x1408ca99b
008CA890  48 8B 9C 24 00 01 00 00         mov rbx, qword ptr [rsp + 0x100]
008CA898  F6 C3 01                        test bl, 1
008CA89B  0F 85 CC 00 00 00               jne 0x1408ca96d
008CA8A1  48 8B C3                        mov rax, rbx
008CA8A4  48 C1 E8 10                     shr rax, 0x10
008CA8A8  66 3B D8                        cmp bx, ax
008CA8AB  0F 87 BC 00 00 00               ja 0x1408ca96d
008CA8B1  44 0F B7 FB                     movzx r15d, bx
008CA8B5  49 8D 57 10                     lea rdx, [r15 + 0x10]
008CA8B9  B9 40 00 00 00                  mov ecx, 0x40
008CA8BE  41 B8 54 68 4E 6D               mov r8d, 0x6d4e6854
008CA8C4  E8 27 78 2B 00                  call 0x140b820f0
008CA8C9  4C 8B F0                        mov r14, rax
008CA8CC  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
008CA8D4  48 85 C0                        test rax, rax
008CA8D7  0F 84 A0 00 00 00               je 0x1408ca97d
008CA8DD  48 8D 48 10                     lea rcx, [rax + 0x10]
008CA8E1  48 89 48 08                     mov qword ptr [rax + 8], rcx
008CA8E5  66 89 18                        mov word ptr [rax], bx
008CA8E8  66 89 58 02                     mov word ptr [rax + 2], bx
008CA8EC  45 8B C7                        mov r8d, r15d
008CA8EF  48 8B 94 24 08 01 00 00         mov rdx, qword ptr [rsp + 0x108]
008CA8F7  E8 44 BF DF FF                  call 0x1406c6840
008CA8FC  EB 18                           jmp 0x1408ca916
008CA8FE  8B F0                           mov esi, eax
008CA900  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008CA904  4C 8B B4 24 98 00 00 00         mov r14, qword ptr [rsp + 0x98]
008CA90C  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
008CA911  E9 85 00 00 00                  jmp 0x1408ca99b
008CA916  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
008CA91B  49 8B D4                        mov rdx, r12
008CA91E  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008CA923  48 8B CB                        mov rcx, rbx
008CA926  E8 B5 ED C1 FF                  call 0x1404e96e0
008CA92B  C6 44 24 60 01                  mov byte ptr [rsp + 0x60], 1
008CA930  48 8B 83 A0 06 00 00            mov rax, qword ptr [rbx + 0x6a0]
008CA937  48 89 84 24 B8 00 00 00         mov qword ptr [rsp + 0xb8], rax
008CA93F  4C 89 B3 A0 06 00 00            mov qword ptr [rbx + 0x6a0], r14
008CA946  4C 8B F7                        mov r14, rdi
008CA949  48 89 BC 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdi
008CA951  48 8B CB                        mov rcx, rbx
008CA954  E8 7F 32 15 00                  call 0x140a1dbd8
008CA959  EB 40                           jmp 0x1408ca99b
008CA95B  41 0F 10 04 24                  movups xmm0, xmmword ptr [r12]
008CA960  0F 11 84 24 00 01 00 00         movups xmmword ptr [rsp + 0x100], xmm0
008CA968  E9 23 FF FF FF                  jmp 0x1408ca890
008CA96D  BE 0D 00 00 C0                  mov esi, 0xc000000d
008CA972  89 74 24 50                     mov dword ptr [rsp + 0x50], esi
008CA976  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
008CA97B  EB 1E                           jmp 0x1408ca99b
008CA97D  BE 9A 00 00 C0                  mov esi, 0xc000009a
008CA982  89 74 24 50                     mov dword ptr [rsp + 0x50], esi
008CA986  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
008CA98B  EB 0E                           jmp 0x1408ca99b
008CA98D  BE 04 00 00 C0                  mov esi, 0xc0000004
008CA992  89 74 24 50                     mov dword ptr [rsp + 0x50], esi
008CA996  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
008CA99B  80 7C 24 60 00                  cmp byte ptr [rsp + 0x60], 0
008CA9A0  74 0D                           je 0x1408ca9af
008CA9A2  49 8B D4                        mov rdx, r12
008CA9A5  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008CA9AA  E8 11 EE C1 FF                  call 0x1404e97c0
008CA9AF  80 7C 24 61 00                  cmp byte ptr [rsp + 0x61], 0
008CA9B4  74 0F                           je 0x1408ca9c5
008CA9B6  BA 50 73 51 79                  mov edx, 0x79517350
008CA9BB  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008CA9C0  E8 1B CF A2 FF                  call 0x1402f78e0
008CA9C5  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
008CA9CD  48 85 C9                        test rcx, rcx
008CA9D0  74 0A                           je 0x1408ca9dc
008CA9D2  BA 54 68 4E 6D                  mov edx, 0x6d4e6854
008CA9D7  E8 94 7E 2B 00                  call 0x140b82870
008CA9DC  4D 85 F6                        test r14, r14
008CA9DF  0F 84 D7 F9 FF FF               je 0x1408ca3bc
008CA9E5  BA 54 68 4E 6D                  mov edx, 0x6d4e6854
008CA9EA  49 8B CE                        mov rcx, r14
008CA9ED  E8 7E 7E 2B 00                  call 0x140b82870
008CA9F2  8B C6                           mov eax, esi
008CA9F4  E9 7A 0F 00 00                  jmp 0x1408cb973
008CA9F9  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008CA9FE  E9 9F F9 FF FF                  jmp 0x1408ca3a2
008CAA03  41 83 FF 08                     cmp r15d, 8
008CAA07  0F 85 EB FA FF FF               jne 0x1408ca4f8
008CAA0D  49 8B 1C 24                     mov rbx, qword ptr [r12]
008CAA11  48 89 9C 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], rbx
008CAA19  EB 05                           jmp 0x1408caa20
008CAA1B  E9 53 0F 00 00                  jmp 0x1408cb973
008CAA20  48 85 DB                        test rbx, rbx
008CAA23  0F 84 C0 F8 FF FF               je 0x1408ca2e9
008CAA29  4C 8B 05 98 C0 6F 00            mov r8, qword ptr [rip + 0x6fc098]
008CAA30  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CAA35  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CAA3A  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CAA3F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CAA44  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CAA4C  BA 00 04 00 00                  mov edx, 0x400
008CAA51  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CAA56  E8 F5 EB F9 FF                  call 0x140869650
008CAA5B  85 C0                           test eax, eax
008CAA5D  0F 88 10 0F 00 00               js 0x1408cb973
008CAA63  4C 8B 74 24 48                  mov r14, qword ptr [rsp + 0x48]
008CAA68  49 8B B6 20 02 00 00            mov rsi, qword ptr [r14 + 0x220]
008CAA6F  48 8D 8E E8 01 00 00            lea rcx, [rsi + 0x1e8]
008CAA76  E8 A5 BB 94 FF                  call 0x140216620
008CAA7B  84 C0                           test al, al
008CAA7D  0F 84 1D 04 00 00               je 0x1408caea0
008CAA83  48 8B D3                        mov rdx, rbx
008CAA86  49 8B CE                        mov rcx, r14
008CAA89  E8 06 33 A0 FF                  call 0x1402cdd94
008CAA8E  48 8B D8                        mov rbx, rax
008CAA91  48 8D 8E E8 01 00 00            lea rcx, [rsi + 0x1e8]
008CAA98  E8 E3 F3 A7 FF                  call 0x140349e80
008CAA9D  BE 0D 00 00 C0                  mov esi, 0xc000000d
008CAAA2  48 85 DB                        test rbx, rbx
008CAAA5  0F 44 FE                        cmove edi, esi
008CAAA8  BA 50 73 51 79                  mov edx, 0x79517350
008CAAAD  49 8B CE                        mov rcx, r14
008CAAB0  E8 2B CE A2 FF                  call 0x1402f78e0
008CAAB5  8B C7                           mov eax, edi
008CAAB7  E9 B7 0E 00 00                  jmp 0x1408cb973
008CAABC  48 89 BC 24 80 00 00 00         mov qword ptr [rsp + 0x80], rdi
008CAAC4  41 0F 10 34 24                  movups xmm6, xmmword ptr [r12]
008CAAC9  0F 11 B4 24 80 01 00 00         movups xmmword ptr [rsp + 0x180], xmm6
008CAAD1  F2 41 0F 10 44 24 10            movsd xmm0, qword ptr [r12 + 0x10]
008CAAD8  0F 28 F8                        movaps xmm7, xmm0
008CAADB  F2 0F 11 84 24 90 01 00 00      movsd qword ptr [rsp + 0x190], xmm0
008CAAE4  EB 07                           jmp 0x1408caaed
008CAAE6  8B F0                           mov esi, eax
008CAAE8  E9 C7 00 00 00                  jmp 0x1408cabb4
008CAAED  4C 8B 05 D4 BF 6F 00            mov r8, qword ptr [rip + 0x6fbfd4]
008CAAF4  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CAAF9  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CAAFE  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CAB03  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CAB08  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CAB10  BA 20 00 00 00                  mov edx, 0x20
008CAB15  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CAB1A  E8 31 EB F9 FF                  call 0x140869650
008CAB1F  8B F0                           mov esi, eax
008CAB21  85 C0                           test eax, eax
008CAB23  0F 88 8B 00 00 00               js 0x1408cabb4
008CAB29  66 0F 7E F1                     movd ecx, xmm6
008CAB2D  85 C9                           test ecx, ecx
008CAB2F  0F 85 2F 0A 00 00               jne 0x1408cb564
008CAB35  4C 8B 05 F4 C4 6F 00            mov r8, qword ptr [rip + 0x6fc4f4]
008CAB3C  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CAB41  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CAB46  48 8D 84 24 80 00 00 00         lea rax, [rsp + 0x80]
008CAB4E  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CAB53  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CAB5B  44 0F B6 4C 24 40               movzx r9d, byte ptr [rsp + 0x40]
008CAB61  41 8B D5                        mov edx, r13d
008CAB64  48 8B 8C 24 88 01 00 00         mov rcx, qword ptr [rsp + 0x188]
008CAB6C  E8 DF EA F9 FF                  call 0x140869650
008CAB71  8B F0                           mov esi, eax
008CAB73  85 C0                           test eax, eax
008CAB75  78 3D                           js 0x1408cabb4
008CAB77  4C 8D 84 24 90 01 00 00         lea r8, [rsp + 0x190]
008CAB7F  48 8B 94 24 80 00 00 00         mov rdx, qword ptr [rsp + 0x80]
008CAB87  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008CAB8C  E8 37 BD 15 00                  call 0x140a268c8
008CAB91  F2 0F 10 BC 24 90 01 00 00      movsd xmm7, qword ptr [rsp + 0x190]
008CAB9A  0F 10 B4 24 80 01 00 00         movups xmm6, xmmword ptr [rsp + 0x180]
008CABA2  8B F0                           mov esi, eax
008CABA4  41 0F 11 34 24                  movups xmmword ptr [r12], xmm6
008CABA9  F2 41 0F 11 7C 24 10            movsd qword ptr [r12 + 0x10], xmm7
008CABB0  EB 02                           jmp 0x1408cabb4
008CABB2  8B F0                           mov esi, eax
008CABB4  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
008CABBC  48 85 C9                        test rcx, rcx
008CABBF  74 0A                           je 0x1408cabcb
008CABC1  BA 50 73 51 79                  mov edx, 0x79517350
008CABC6  E8 15 CD A2 FF                  call 0x1402f78e0
008CABCB  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008CABD0  48 85 C9                        test rcx, rcx
008CABD3  0F 85 D9 F7 FF FF               jne 0x1408ca3b2
008CABD9  8B C6                           mov eax, esi
008CABDB  E9 93 0D 00 00                  jmp 0x1408cb973
008CABE0  41 83 FF 04                     cmp r15d, 4
008CABE4  0F 85 0E F9 FF FF               jne 0x1408ca4f8
008CABEA  E9 AC 01 00 00                  jmp 0x1408cad9b
008CABEF  41 83 FF 04                     cmp r15d, 4
008CABF3  0F 85 FF F8 FF FF               jne 0x1408ca4f8
008CABF9  41 8B 1C 24                     mov ebx, dword ptr [r12]
008CABFD  89 9C 24 B0 00 00 00            mov dword ptr [rsp + 0xb0], ebx
008CAC04  EB 05                           jmp 0x1408cac0b
008CAC06  E9 68 0D 00 00                  jmp 0x1408cb973
008CAC0B  83 FB 40                        cmp ebx, 0x40
008CAC0E  0F 87 D5 F6 FF FF               ja 0x1408ca2e9
008CAC14  4C 8B 05 AD BE 6F 00            mov r8, qword ptr [rip + 0x6fbead]
008CAC1B  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CAC20  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CAC25  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CAC2A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CAC2F  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CAC37  BA 20 00 00 00                  mov edx, 0x20
008CAC3C  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CAC41  E8 0A EA F9 FF                  call 0x140869650
008CAC46  85 C0                           test eax, eax
008CAC48  0F 88 25 0D 00 00               js 0x1408cb973
008CAC4E  0F B6 D3                        movzx edx, bl
008CAC51  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008CAC56  E8 F5 24 A1 FF                  call 0x1402dd150
008CAC5B  0F B6 D8                        movzx ebx, al
008CAC5E  BA 50 73 51 79                  mov edx, 0x79517350
008CAC63  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008CAC68  E8 73 CC A2 FF                  call 0x1402f78e0
008CAC6D  8B C3                           mov eax, ebx
008CAC6F  E9 FF 0C 00 00                  jmp 0x1408cb973
008CAC74  80 B8 47 03 00 00 04            cmp byte ptr [rax + 0x347], 4
008CAC7B  0F 84 6D F5 FF FF               je 0x1408ca1ee
008CAC81  0F B6 54 24 40                  movzx edx, byte ptr [rsp + 0x40]
008CAC86  48 8B 0D 5B EE 70 00            mov rcx, qword ptr [rip + 0x70ee5b]
008CAC8D  E8 8E 71 FA FF                  call 0x140871e20
008CAC92  84 C0                           test al, al
008CAC94  0F 85 54 F5 FF FF               jne 0x1408ca1ee
008CAC9A  BE 61 00 00 C0                  mov esi, 0xc0000061
008CAC9F  48 8B CF                        mov rcx, rdi
008CACA2  BA 50 73 51 79                  mov edx, 0x79517350
008CACA7  E8 34 CC A2 FF                  call 0x1402f78e0
008CACAC  8B C6                           mov eax, esi
008CACAE  E9 C0 0C 00 00                  jmp 0x1408cb973
008CACB3  48 8B CB                        mov rcx, rbx
008CACB6  E8 95 E6 A2 FF                  call 0x1402f9350
008CACBB  BF A8 00 00 C0                  mov edi, 0xc00000a8
008CACC0  E9 D2 F5 FF FF                  jmp 0x1408ca297
008CACC5  41 83 FF 0C                     cmp r15d, 0xc
008CACC9  0F 85 29 F8 FF FF               jne 0x1408ca4f8
008CACCF  F2 41 0F 10 04 24               movsd xmm0, qword ptr [r12]
008CACD5  F2 0F 11 84 24 80 00 00 00      movsd qword ptr [rsp + 0x80], xmm0
008CACDE  41 8B 54 24 08                  mov edx, dword ptr [r12 + 8]
008CACE3  EB 05                           jmp 0x1408cacea
008CACE5  E9 89 0C 00 00                  jmp 0x1408cb973
008CACEA  83 BC 24 80 00 00 00 01         cmp dword ptr [rsp + 0x80], 1
008CACF2  0F 85 F1 F5 FF FF               jne 0x1408ca2e9
008CACF8  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
008CAD00  48 C1 E9 20                     shr rcx, 0x20
008CAD04  F7 C1 FE FF FF FF               test ecx, 0xfffffffe
008CAD0A  0F 85 D9 F5 FF FF               jne 0x1408ca2e9
008CAD10  8B C1                           mov eax, ecx
008CAD12  F7 D0                           not eax
008CAD14  85 C2                           test edx, eax
008CAD16  0F 85 CD F5 FF FF               jne 0x1408ca2e9
008CAD1C  F6 C1 01                        test cl, 1
008CAD1F  0F 84 B4 05 00 00               je 0x1408cb2d9
008CAD25  F6 C2 01                        test dl, 1
008CAD28  B8 03 00 00 00                  mov eax, 3
008CAD2D  44 0F 44 F0                     cmove r14d, eax
008CAD31  4C 8B 05 90 BD 6F 00            mov r8, qword ptr [rip + 0x6fbd90]
008CAD38  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CAD3D  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CAD42  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CAD47  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CAD4C  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CAD54  BA 20 00 00 00                  mov edx, 0x20
008CAD59  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CAD5E  E8 ED E8 F9 FF                  call 0x140869650
008CAD63  85 C0                           test eax, eax
008CAD65  0F 88 08 0C 00 00               js 0x1408cb973
008CAD6B  41 8B D6                        mov edx, r14d
008CAD6E  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008CAD73  E8 E8 B6 18 00                  call 0x140a56460
008CAD78  E9 DD F6 FF FF                  jmp 0x1408ca45a
008CAD7D  BE 0D 00 00 C0                  mov esi, 0xc000000d
008CAD82  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008CAD87  E9 0D F8 FF FF                  jmp 0x1408ca599
008CAD8C  41 83 FF 04                     cmp r15d, 4
008CAD90  0F 85 62 F7 FF FF               jne 0x1408ca4f8
008CAD96  E9 0F 01 00 00                  jmp 0x1408caeaa
008CAD9B  41 8B 1C 24                     mov ebx, dword ptr [r12]
008CAD9F  89 9C 24 10 01 00 00            mov dword ptr [rsp + 0x110], ebx
008CADA6  EB 05                           jmp 0x1408cadad
008CADA8  E9 C6 0B 00 00                  jmp 0x1408cb973
008CADAD  4C 8B 05 14 BD 6F 00            mov r8, qword ptr [rip + 0x6fbd14]
008CADB4  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CADB9  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CADBE  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CADC3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CADC8  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CADD0  BA 00 04 00 00                  mov edx, 0x400
008CADD5  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CADDA  E8 71 E8 F9 FF                  call 0x140869650
008CADDF  8B F0                           mov esi, eax
008CADE1  85 C0                           test eax, eax
008CADE3  0F 88 8A 0B 00 00               js 0x1408cb973
008CADE9  85 DB                           test ebx, ebx
008CADEB  40 0F 95 C7                     setne dil
008CADEF  8B D7                           mov edx, edi
008CADF1  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008CADF6  E8 C1 6B AF FF                  call 0x1403c19bc
008CADFB  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008CAE00  BA 50 73 51 79                  mov edx, 0x79517350
008CAE05  E8 D6 CA A2 FF                  call 0x1402f78e0
008CAE0A  8B C6                           mov eax, esi
008CAE0C  E9 62 0B 00 00                  jmp 0x1408cb973
008CAE11  BE 20 00 00 00                  mov esi, 0x20
008CAE16  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
008CAE1B  83 FB 03                        cmp ebx, 3
008CAE1E  0F 83 83 07 00 00               jae 0x1408cb5a7
008CAE24  4C 8B 05 9D BC 6F 00            mov r8, qword ptr [rip + 0x6fbc9d]
008CAE2B  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CAE30  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CAE35  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CAE3A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CAE3F  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CAE47  8B D6                           mov edx, esi
008CAE49  49 8B CF                        mov rcx, r15
008CAE4C  E8 FF E7 F9 FF                  call 0x140869650
008CAE51  85 C0                           test eax, eax
008CAE53  0F 88 1A 0B 00 00               js 0x1408cb973
008CAE59  48 8B 7C 24 48                  mov rdi, qword ptr [rsp + 0x48]
008CAE5E  41 80 FE 01                     cmp r14b, 1
008CAE62  0F 84 59 08 00 00               je 0x1408cb6c1
008CAE68  8B D3                           mov edx, ebx
008CAE6A  48 8B CF                        mov rcx, rdi
008CAE6D  E8 4A 91 AF FF                  call 0x1403c3fbc
008CAE72  48 8B CF                        mov rcx, rdi
008CAE75  BA 50 73 51 79                  mov edx, 0x79517350
008CAE7A  E8 61 CA A2 FF                  call 0x1402f78e0
008CAE7F  33 C0                           xor eax, eax
008CAE81  E9 ED 0A 00 00                  jmp 0x1408cb973
008CAE86  41 8B 1C 24                     mov ebx, dword ptr [r12]
008CAE8A  89 9C 24 18 01 00 00            mov dword ptr [rsp + 0x118], ebx
008CAE91  EB 05                           jmp 0x1408cae98
008CAE93  E9 DB 0A 00 00                  jmp 0x1408cb973
008CAE98  45 32 F6                        xor r14b, r14b
008CAE9B  E9 40 F4 FF FF                  jmp 0x1408ca2e0
008CAEA0  BF 0A 01 00 C0                  mov edi, 0xc000010a
008CAEA5  E9 FE FB FF FF                  jmp 0x1408caaa8
008CAEAA  45 8B 34 24                     mov r14d, dword ptr [r12]
008CAEAE  44 89 B4 24 A0 00 00 00         mov dword ptr [rsp + 0xa0], r14d
008CAEB6  EB 05                           jmp 0x1408caebd
008CAEB8  E9 B6 0A 00 00                  jmp 0x1408cb973
008CAEBD  4C 8B 05 04 BC 6F 00            mov r8, qword ptr [rip + 0x6fbc04]
008CAEC4  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CAEC9  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CAECE  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CAED3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CAED8  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CAEE0  BA 20 00 00 00                  mov edx, 0x20
008CAEE5  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CAEEA  E8 61 E7 F9 FF                  call 0x140869650
008CAEEF  44 8B E8                        mov r13d, eax
008CAEF2  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008CAEF6  85 C0                           test eax, eax
008CAEF8  0F 88 75 0A 00 00               js 0x1408cb973
008CAEFE  BA 50 73 51 79                  mov edx, 0x79517350
008CAF03  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
008CAF08  49 8B CF                        mov rcx, r15
008CAF0B  E8 D0 C9 A2 FF                  call 0x1402f78e0
008CAF10  4C 3B 7C 24 68                  cmp r15, qword ptr [rsp + 0x68]
008CAF15  0F 85 CE F3 FF FF               jne 0x1408ca2e9
008CAF1B  4D 8B BF 20 02 00 00            mov r15, qword ptr [r15 + 0x220]
008CAF22  4C 89 7C 24 68                  mov qword ptr [rsp + 0x68], r15
008CAF27  33 D2                           xor edx, edx
008CAF29  49 8B CF                        mov rcx, r15
008CAF2C  E8 BF ED FF FF                  call 0x1408c9cf0
008CAF31  41 BC 4C 01 00 00               mov r12d, 0x14c
008CAF37  48 8B F0                        mov rsi, rax
008CAF3A  48 8B C8                        mov rcx, rax
008CAF3D  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
008CAF42  48 8B D8                        mov rbx, rax
008CAF45  48 85 C0                        test rax, rax
008CAF48  0F 84 FB 02 00 00               je 0x1408cb249
008CAF4E  48 81 C1 88 05 00 00            add rcx, 0x588
008CAF55  E8 C6 B6 94 FF                  call 0x140216620
008CAF5A  84 C0                           test al, al
008CAF5C  0F 84 4E 01 00 00               je 0x1408cb0b0
008CAF62  48 8B 8B F0 00 00 00            mov rcx, qword ptr [rbx + 0xf0]
008CAF69  48 85 C9                        test rcx, rcx
008CAF6C  0F 84 32 01 00 00               je 0x1408cb0a4
008CAF72  48 8B D7                        mov rdx, rdi
008CAF75  49 8B 87 10 03 00 00            mov rax, qword ptr [r15 + 0x310]
008CAF7C  48 85 C0                        test rax, rax
008CAF7F  74 19                           je 0x1408caf9a
008CAF81  45 0F B7 87 EC 06 00 00         movzx r8d, word ptr [r15 + 0x6ec]
008CAF89  66 45 3B C4                     cmp r8w, r12w
008CAF8D  0F 85 B5 00 00 00               jne 0x1408cb048
008CAF93  48 8D 91 00 20 00 00            lea rdx, [rcx + 0x2000]
008CAF9A  41 83 FE 40                     cmp r14d, 0x40
008CAF9E  72 4B                           jb 0x1408cafeb
008CAFA0  41 81 FE 40 04 00 00            cmp r14d, 0x440
008CAFA7  0F 83 D4 00 00 00               jae 0x1408cb081
008CAFAD  48 85 C0                        test rax, rax
008CAFB0  75 4E                           jne 0x1408cb000
008CAFB2  48 8B 91 80 17 00 00            mov rdx, qword ptr [rcx + 0x1780]
008CAFB9  48 89 94 24 98 01 00 00         mov qword ptr [rsp + 0x198], rdx
008CAFC1  48 85 D2                        test rdx, rdx
008CAFC4  0F 84 B7 00 00 00               je 0x1408cb081
008CAFCA  41 8D 46 C0                     lea eax, [r14 - 0x40]
008CAFCE  48 8D 04 C2                     lea rax, [rdx + rax*8]
008CAFD2  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
008CAFDC  48 3B C1                        cmp rax, rcx
008CAFDF  48 0F 43 C1                     cmovae rax, rcx
008CAFE3  48 89 38                        mov qword ptr [rax], rdi
008CAFE6  E9 96 00 00 00                  jmp 0x1408cb081
008CAFEB  48 85 C0                        test rax, rax
008CAFEE  75 39                           jne 0x1408cb029
008CAFF0  41 8B C6                        mov eax, r14d
008CAFF3  48 89 BC C1 80 14 00 00         mov qword ptr [rcx + rax*8 + 0x1480], rdi
008CAFFB  E9 81 00 00 00                  jmp 0x1408cb081
008CB000  41 0F B7 87 EC 06 00 00         movzx eax, word ptr [r15 + 0x6ec]
008CB008  66 41 3B C4                     cmp ax, r12w
008CB00C  75 4F                           jne 0x1408cb05d
008CB00E  48 85 D2                        test rdx, rdx
008CB011  74 6E                           je 0x1408cb081
008CB013  44 8B 82 94 0F 00 00            mov r8d, dword ptr [rdx + 0xf94]
008CB01A  45 85 C0                        test r8d, r8d
008CB01D  74 62                           je 0x1408cb081
008CB01F  41 8D 46 C0                     lea eax, [r14 - 0x40]
008CB023  41 89 3C 80                     mov dword ptr [r8 + rax*4], edi
008CB027  EB 58                           jmp 0x1408cb081
008CB029  41 0F B7 87 EC 06 00 00         movzx eax, word ptr [r15 + 0x6ec]
008CB031  66 41 3B C4                     cmp ax, r12w
008CB035  75 38                           jne 0x1408cb06f
008CB037  48 85 D2                        test rdx, rdx
008CB03A  74 45                           je 0x1408cb081
008CB03C  41 8B C6                        mov eax, r14d
008CB03F  89 BC 82 10 0E 00 00            mov dword ptr [rdx + rax*4 + 0xe10], edi
008CB046  EB 39                           jmp 0x1408cb081
008CB048  41 B9 C4 01 00 00               mov r9d, 0x1c4
008CB04E  66 45 3B C1                     cmp r8w, r9w
008CB052  0F 85 42 FF FF FF               jne 0x1408caf9a
008CB058  E9 36 FF FF FF                  jmp 0x1408caf93
008CB05D  41 B8 C4 01 00 00               mov r8d, 0x1c4
008CB063  66 41 3B C0                     cmp ax, r8w
008CB067  0F 85 45 FF FF FF               jne 0x1408cafb2
008CB06D  EB 9F                           jmp 0x1408cb00e
008CB06F  41 B8 C4 01 00 00               mov r8d, 0x1c4
008CB075  66 41 3B C0                     cmp ax, r8w
008CB079  0F 85 71 FF FF FF               jne 0x1408caff0
008CB07F  EB B6                           jmp 0x1408cb037
008CB081  EB 21                           jmp 0x1408cb0a4
008CB083  44 8B E8                        mov r13d, eax
008CB086  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008CB08A  33 FF                           xor edi, edi
008CB08C  41 BC 4C 01 00 00               mov r12d, 0x14c
008CB092  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008CB097  4C 8B 7C 24 68                  mov r15, qword ptr [rsp + 0x68]
008CB09C  44 8B B4 24 A0 00 00 00         mov r14d, dword ptr [rsp + 0xa0]
008CB0A4  48 8D 8B 88 05 00 00            lea rcx, [rbx + 0x588]
008CB0AB  E8 D0 ED A7 FF                  call 0x140349e80
008CB0B0  48 8B D3                        mov rdx, rbx
008CB0B3  49 8B CF                        mov rcx, r15
008CB0B6  E8 35 EC FF FF                  call 0x1408c9cf0
008CB0BB  E9 77 FE FF FF                  jmp 0x1408caf37
008CB0C0  41 83 FF 10                     cmp r15d, 0x10
008CB0C4  0F 85 2E F4 FF FF               jne 0x1408ca4f8
008CB0CA  41 0F 10 04 24                  movups xmm0, xmmword ptr [r12]
008CB0CF  0F 11 84 24 C0 00 00 00         movups xmmword ptr [rsp + 0xc0], xmm0
008CB0D7  EB 05                           jmp 0x1408cb0de
008CB0D9  E9 95 08 00 00                  jmp 0x1408cb973
008CB0DE  E8 1D 15 BC FF                  call 0x14048c600
008CB0E3  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
008CB0EB  66 3B C8                        cmp cx, ax
008CB0EE  0F 83 F5 F1 FF FF               jae 0x1408ca2e9
008CB0F4  0F B7 C1                        movzx eax, cx
008CB0F7  48 8B 8C C6 28 71 FC 00         mov rcx, qword ptr [rsi + rax*8 + 0xfc7128]
008CB0FF  4C 8B B4 24 C0 00 00 00         mov r14, qword ptr [rsp + 0xc0]
008CB107  49 23 CE                        and rcx, r14
008CB10A  49 3B CE                        cmp rcx, r14
008CB10D  0F 85 D6 F1 FF FF               jne 0x1408ca2e9
008CB113  48 8B 9C 24 C8 00 00 00         mov rbx, qword ptr [rsp + 0xc8]
008CB11B  48 8B CB                        mov rcx, rbx
008CB11E  48 C1 E9 30                     shr rcx, 0x30
008CB122  48 8B C3                        mov rax, rbx
008CB125  48 C1 E8 20                     shr rax, 0x20
008CB129  66 0B C8                        or cx, ax
008CB12C  48 8B C3                        mov rax, rbx
008CB12F  48 C1 E8 10                     shr rax, 0x10
008CB133  66 0B C8                        or cx, ax
008CB136  0F 85 AD F1 FF FF               jne 0x1408ca2e9
008CB13C  4C 8B 05 85 B9 6F 00            mov r8, qword ptr [rip + 0x6fb985]
008CB143  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CB148  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CB14D  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CB152  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CB157  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CB15F  44 0F B6 4C 24 40               movzx r9d, byte ptr [rsp + 0x40]
008CB165  BA 20 00 00 00                  mov edx, 0x20
008CB16A  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CB16F  E8 DC E4 F9 FF                  call 0x140869650
008CB174  85 C0                           test eax, eax
008CB176  0F 88 F7 07 00 00               js 0x1408cb973
008CB17C  48 C7 84 24 B0 01 00 00 01 00 20 00  mov qword ptr [rsp + 0x1b0], 0x200001
008CB188  33 D2                           xor edx, edx
008CB18A  41 B8 00 01 00 00               mov r8d, 0x100
008CB190  48 8D 8C 24 B8 01 00 00         lea rcx, [rsp + 0x1b8]
008CB198  E8 A3 BA DF FF                  call 0x1406c6c40
008CB19D  66 39 9C 24 B0 01 00 00         cmp word ptr [rsp + 0x1b0], bx
008CB1A5  0F 86 CC 05 00 00               jbe 0x1408cb777
008CB1AB  0F B7 C3                        movzx eax, bx
008CB1AE  4C 09 B4 C4 B8 01 00 00         or qword ptr [rsp + rax*8 + 0x1b8], r14
008CB1B6  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
008CB1BB  48 8B B0 20 02 00 00            mov rsi, qword ptr [rax + 0x220]
008CB1C2  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
008CB1C7  49 8B D4                        mov rdx, r12
008CB1CA  48 8B CE                        mov rcx, rsi
008CB1CD  E8 FE 64 B3 FF                  call 0x1404016d0
008CB1D2  48 8B 9E A0 02 00 00            mov rbx, qword ptr [rsi + 0x2a0]
008CB1D9  48 89 9C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rbx
008CB1E1  48 85 DB                        test rbx, rbx
008CB1E4  74 19                           je 0x1408cb1ff
008CB1E6  48 8D 4B 38                     lea rcx, [rbx + 0x38]
008CB1EA  B2 01                           mov dl, 1
008CB1EC  E8 CF 69 94 FF                  call 0x140211bc0
008CB1F1  8B 83 20 04 00 00               mov eax, dword ptr [rbx + 0x420]
008CB1F7  A8 10                           test al, 0x10
008CB1F9  0F 85 24 01 00 00               jne 0x1408cb323
008CB1FF  48 8D 94 24 B0 01 00 00         lea rdx, [rsp + 0x1b0]
008CB207  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008CB20C  E8 1B 48 A0 FF                  call 0x1402cfa2c
008CB211  48 8D 54 24 74                  lea rdx, [rsp + 0x74]
008CB216  48 8B CE                        mov rcx, rsi
008CB219  E8 3A 47 A0 FF                  call 0x1402cf958
008CB21E  0F B7 CF                        movzx ecx, di
008CB221  0F B7 94 24 B0 01 00 00         movzx edx, word ptr [rsp + 0x1b0]
008CB229  66 3B CA                        cmp cx, dx
008CB22C  0F 83 D3 00 00 00               jae 0x1408cb305
008CB232  0F B7 C1                        movzx eax, cx
008CB235  48 83 BC C4 B8 01 00 00 00      cmp qword ptr [rsp + rax*8 + 0x1b8], 0
008CB23E  0F 85 9D 00 00 00               jne 0x1408cb2e1
008CB244  66 FF C1                        inc cx
008CB247  EB E0                           jmp 0x1408cb229
008CB249  41 8B C5                        mov eax, r13d
008CB24C  E9 22 07 00 00                  jmp 0x1408cb973
008CB251  41 83 FF 04                     cmp r15d, 4
008CB255  0F 85 9D F2 FF FF               jne 0x1408ca4f8
008CB25B  41 8B 04 24                     mov eax, dword ptr [r12]
008CB25F  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
008CB263  EB 05                           jmp 0x1408cb26a
008CB265  E9 09 07 00 00                  jmp 0x1408cb973
008CB26A  4C 8B 05 57 B8 6F 00            mov r8, qword ptr [rip + 0x6fb857]
008CB271  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CB276  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CB27B  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CB280  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CB285  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CB28D  BA 20 00 00 00                  mov edx, 0x20
008CB292  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CB297  E8 B4 E3 F9 FF                  call 0x140869650
008CB29C  85 C0                           test eax, eax
008CB29E  0F 88 CF 06 00 00               js 0x1408cb973
008CB2A4  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
008CB2A9  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
008CB2AE  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008CB2B3  48 8B CB                        mov rcx, rbx
008CB2B6  E8 45 1F A1 FF                  call 0x1402dd200
008CB2BB  8B F8                           mov edi, eax
008CB2BD  85 C0                           test eax, eax
008CB2BF  0F 89 81 00 00 00               jns 0x1408cb346
008CB2C5  48 8B CB                        mov rcx, rbx
008CB2C8  BA 50 73 51 79                  mov edx, 0x79517350
008CB2CD  E8 0E C6 A2 FF                  call 0x1402f78e0
008CB2D2  8B C7                           mov eax, edi
008CB2D4  E9 9A 06 00 00                  jmp 0x1408cb973
008CB2D9  44 8B F7                        mov r14d, edi
008CB2DC  E9 50 FA FF FF                  jmp 0x1408cad31
008CB2E1  89 7C 24 50                     mov dword ptr [rsp + 0x50], edi
008CB2E5  0F B7 84 24 C8 00 00 00         movzx eax, word ptr [rsp + 0xc8]
008CB2ED  66 39 44 24 74                  cmp word ptr [rsp + 0x74], ax
008CB2F2  74 11                           je 0x1408cb305
008CB2F4  F0 0F BA AE 88 00 00 00 0C      lock bts dword ptr [rsi + 0x88], 0xc
008CB2FD  48 8B 9C 24 A8 00 00 00         mov rbx, qword ptr [rsp + 0xa8]
008CB305  48 85 DB                        test rbx, rbx
008CB308  74 09                           je 0x1408cb313
008CB30A  48 8D 4B 38                     lea rcx, [rbx + 0x38]
008CB30E  E8 FD 46 99 FF                  call 0x14025fa10
008CB313  49 8B D4                        mov rdx, r12
008CB316  48 8B CE                        mov rcx, rsi
008CB319  E8 32 86 99 FF                  call 0x140263950
008CB31E  E9 74 EF FF FF                  jmp 0x1408ca297
008CB323  48 8D 93 D8 02 00 00            lea rdx, [rbx + 0x2d8]
008CB32A  48 8D 8C 24 B0 01 00 00         lea rcx, [rsp + 0x1b0]
008CB332  E8 49 29 A0 FF                  call 0x1402cdc80
008CB337  85 C0                           test eax, eax
008CB339  0F 85 C0 FE FF FF               jne 0x1408cb1ff
008CB33F  BF 01 00 00 C0                  mov edi, 0xc0000001
008CB344  EB BF                           jmp 0x1408cb305
008CB346  8B 4C 24 78                     mov ecx, dword ptr [rsp + 0x78]
008CB34A  41 89 0C 24                     mov dword ptr [r12], ecx
008CB34E  E9 72 FF FF FF                  jmp 0x1408cb2c5
008CB353  8B F8                           mov edi, eax
008CB355  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008CB35A  E9 66 FF FF FF                  jmp 0x1408cb2c5
008CB35F  41 83 FF 04                     cmp r15d, 4
008CB363  0F 85 8F F1 FF FF               jne 0x1408ca4f8
008CB369  41 8B 1C 24                     mov ebx, dword ptr [r12]
008CB36D  89 9C 24 30 01 00 00            mov dword ptr [rsp + 0x130], ebx
008CB374  EB 05                           jmp 0x1408cb37b
008CB376  E9 F8 05 00 00                  jmp 0x1408cb973
008CB37B  45 84 C9                        test r9b, r9b
008CB37E  0F 85 8D 04 00 00               jne 0x1408cb811
008CB384  4C 8B 05 3D B7 6F 00            mov r8, qword ptr [rip + 0x6fb73d]
008CB38B  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CB390  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CB395  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CB39A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CB39F  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CB3A7  BA 20 00 00 00                  mov edx, 0x20
008CB3AC  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CB3B1  E8 9A E2 F9 FF                  call 0x140869650
008CB3B6  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008CB3BA  85 C0                           test eax, eax
008CB3BC  0F 88 B1 05 00 00               js 0x1408cb973
008CB3C2  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
008CB3C7  85 DB                           test ebx, ebx
008CB3C9  0F 84 C6 03 00 00               je 0x1408cb795
008CB3CF  F0 81 88 A0 05 00 00 00 00 08 00  lock or dword ptr [rax + 0x5a0], 0x80000
008CB3DA  BA 50 73 51 79                  mov edx, 0x79517350
008CB3DF  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008CB3E4  E8 F7 C4 A2 FF                  call 0x1402f78e0
008CB3E9  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
008CB3ED  E9 81 05 00 00                  jmp 0x1408cb973
008CB3F2  45 85 FF                        test r15d, r15d
008CB3F5  0F 85 FD F0 FF FF               jne 0x1408ca4f8
008CB3FB  4C 8B 05 C6 B6 6F 00            mov r8, qword ptr [rip + 0x6fb6c6]
008CB402  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CB407  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CB40C  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CB411  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CB416  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CB41E  41 8D 57 20                     lea edx, [r15 + 0x20]
008CB422  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CB427  E8 24 E2 F9 FF                  call 0x140869650
008CB42C  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008CB430  85 C0                           test eax, eax
008CB432  0F 88 3B 05 00 00               js 0x1408cb973
008CB438  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
008CB43D  F0 83 88 A0 05 00 00 04         lock or dword ptr [rax + 0x5a0], 4
008CB445  EB 93                           jmp 0x1408cb3da
008CB447  33 C9                           xor ecx, ecx
008CB449  E8 52 9C 95 FF                  call 0x1402250a0
008CB44E  48 8B 88 50 03 00 00            mov rcx, qword ptr [rax + 0x350]
008CB455  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
008CB45A  49 39 8C 24 B8 00 00 00         cmp qword ptr [r12 + 0xb8], rcx
008CB462  0F 84 50 F2 FF FF               je 0x1408ca6b8
008CB468  80 BA 47 03 00 00 04            cmp byte ptr [rdx + 0x347], 4
008CB46F  0F 84 43 F2 FF FF               je 0x1408ca6b8
008CB475  BE 0D 00 00 C0                  mov esi, 0xc000000d
008CB47A  48 8B CB                        mov rcx, rbx
008CB47D  BA 50 73 51 79                  mov edx, 0x79517350
008CB482  E8 59 C4 A2 FF                  call 0x1402f78e0
008CB487  8B C6                           mov eax, esi
008CB489  E9 E5 04 00 00                  jmp 0x1408cb973
008CB48E  80 BA 47 03 00 00 04            cmp byte ptr [rdx + 0x347], 4
008CB495  0F 84 37 F2 FF FF               je 0x1408ca6d2
008CB49B  8B 94 24 94 00 00 00            mov edx, dword ptr [rsp + 0x94]
008CB4A2  85 D2                           test edx, edx
008CB4A4  0F 8E 2F F2 FF FF               jle 0x1408ca6d9
008CB4AA  48 8B 5C 24 48                  mov rbx, qword ptr [rsp + 0x48]
008CB4AF  E9 32 F2 FF FF                  jmp 0x1408ca6e6
008CB4B4  BE BB 00 00 C0                  mov esi, 0xc00000bb
008CB4B9  E9 DB F0 FF FF                  jmp 0x1408ca599
008CB4BE  B8 02 00 00 C0                  mov eax, 0xc0000002
008CB4C3  E9 AB 04 00 00                  jmp 0x1408cb973
008CB4C8  41 83 FF 04                     cmp r15d, 4
008CB4CC  0F 85 26 F0 FF FF               jne 0x1408ca4f8
008CB4D2  41 8B 1C 24                     mov ebx, dword ptr [r12]
008CB4D6  89 9C 24 14 01 00 00            mov dword ptr [rsp + 0x114], ebx
008CB4DD  EB 05                           jmp 0x1408cb4e4
008CB4DF  E9 8F 04 00 00                  jmp 0x1408cb973
008CB4E4  41 0F B6 D1                     movzx edx, r9b
008CB4E8  48 8B 0D 91 E5 70 00            mov rcx, qword ptr [rip + 0x70e591]
008CB4EF  E8 2C 69 FA FF                  call 0x140871e20
008CB4F4  84 C0                           test al, al
008CB4F6  0F 84 C5 00 00 00               je 0x1408cb5c1
008CB4FC  4C 8B 05 C5 B5 6F 00            mov r8, qword ptr [rip + 0x6fb5c5]
008CB503  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CB508  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CB50D  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CB512  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CB517  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CB51F  44 0F B6 4C 24 40               movzx r9d, byte ptr [rsp + 0x40]
008CB525  BA 20 00 00 00                  mov edx, 0x20
008CB52A  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CB52F  E8 1C E1 F9 FF                  call 0x140869650
008CB534  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008CB538  85 C0                           test eax, eax
008CB53A  0F 88 33 04 00 00               js 0x1408cb973
008CB540  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
008CB545  85 DB                           test ebx, ebx
008CB547  0F 85 F1 00 00 00               jne 0x1408cb63e
008CB54D  F0 83 A0 A0 05 00 00 DF         lock and dword ptr [rax + 0x5a0], 0xffffffdf
008CB555  E9 00 EF FF FF                  jmp 0x1408ca45a
008CB55A  B8 BB 00 00 C0                  mov eax, 0xc00000bb
008CB55F  E9 0F 04 00 00                  jmp 0x1408cb973
008CB564  83 F9 01                        cmp ecx, 1
008CB567  0F 84 FA 02 00 00               je 0x1408cb867
008CB56D  BE BB 00 00 C0                  mov esi, 0xc00000bb
008CB572  E9 2D F6 FF FF                  jmp 0x1408caba4
008CB577  B8 03 00 00 C0                  mov eax, 0xc0000003
008CB57C  E9 F2 03 00 00                  jmp 0x1408cb973
008CB581  41 B8 00 04 00 00               mov r8d, 0x400
008CB587  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
008CB58C  48 8B 0D 55 E5 70 00            mov rcx, qword ptr [rip + 0x70e555]
008CB593  E8 34 AD 12 00                  call 0x1409f62cc
008CB598  84 C0                           test al, al
008CB59A  74 25                           je 0x1408cb5c1
008CB59C  44 0F B6 4C 24 40               movzx r9d, byte ptr [rsp + 0x40]
008CB5A2  E9 6D EE FF FF                  jmp 0x1408ca414
008CB5A7  44 8B C6                        mov r8d, esi
008CB5AA  49 8B D7                        mov rdx, r15
008CB5AD  48 8B 0D 34 E5 70 00            mov rcx, qword ptr [rip + 0x70e534]
008CB5B4  E8 13 AD 12 00                  call 0x1409f62cc
008CB5B9  84 C0                           test al, al
008CB5BB  0F 85 E4 01 00 00               jne 0x1408cb7a5
008CB5C1  B8 61 00 00 C0                  mov eax, 0xc0000061
008CB5C6  E9 A8 03 00 00                  jmp 0x1408cb973
008CB5CB  41 83 FF 01                     cmp r15d, 1
008CB5CF  0F 85 23 EF FF FF               jne 0x1408ca4f8
008CB5D5  41 0F B6 1C 24                  movzx ebx, byte ptr [r12]
008CB5DA  88 9C 24 90 00 00 00            mov byte ptr [rsp + 0x90], bl
008CB5E1  EB 05                           jmp 0x1408cb5e8
008CB5E3  E9 8B 03 00 00                  jmp 0x1408cb973
008CB5E8  4C 8B 05 D9 B4 6F 00            mov r8, qword ptr [rip + 0x6fb4d9]
008CB5EF  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CB5F4  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CB5F9  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CB5FE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CB603  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CB60B  BA 20 00 00 00                  mov edx, 0x20
008CB610  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CB615  E8 36 E0 F9 FF                  call 0x140869650
008CB61A  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008CB61E  85 C0                           test eax, eax
008CB620  0F 88 4D 03 00 00               js 0x1408cb973
008CB626  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
008CB62B  84 DB                           test bl, bl
008CB62D  0F 85 2B 01 00 00               jne 0x1408cb75e
008CB633  F0 0F BA 70 78 02               lock btr dword ptr [rax + 0x78], 2
008CB639  E9 1C EE FF FF                  jmp 0x1408ca45a
008CB63E  F0 83 88 A0 05 00 00 20         lock or dword ptr [rax + 0x5a0], 0x20
008CB646  E9 0F EE FF FF                  jmp 0x1408ca45a
008CB64B  48 83 7C 24 58 FE               cmp qword ptr [rsp + 0x58], -2
008CB651  0F 85 92 EC FF FF               jne 0x1408ca2e9
008CB657  4C 8B 05 6A B4 6F 00            mov r8, qword ptr [rip + 0x6fb46a]
008CB65E  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CB663  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CB668  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CB66D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CB672  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CB67A  BA 20 00 00 00                  mov edx, 0x20
008CB67F  48 C7 C1 FE FF FF FF            mov rcx, 0xfffffffffffffffe
008CB686  E8 C5 DF F9 FF                  call 0x140869650
008CB68B  85 C0                           test eax, eax
008CB68D  0F 88 E0 02 00 00               js 0x1408cb973
008CB693  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008CB698  48 B8 D8 03 00 00 80 F7 FF FF   movabs rax, 0xfffff780000003d8
008CB6A2  48 8B 00                        mov rax, qword ptr [rax]
008CB6A5  48 83 C8 03                     or rax, 3
008CB6A9  48 09 81 50 02 00 00            or qword ptr [rcx + 0x250], rax
008CB6B0  BA 50 73 51 79                  mov edx, 0x79517350
008CB6B5  E8 26 C2 A2 FF                  call 0x1402f78e0
008CB6BA  33 C0                           xor eax, eax
008CB6BC  E9 B2 02 00 00                  jmp 0x1408cb973
008CB6C1  8B 87 A0 05 00 00               mov eax, dword ptr [rdi + 0x5a0]
008CB6C7  C1 E8 09                        shr eax, 9
008CB6CA  83 E0 07                        and eax, 7
008CB6CD  3B C3                           cmp eax, ebx
008CB6CF  0F 8D 93 F7 FF FF               jge 0x1408cae68
008CB6D5  45 33 C0                        xor r8d, r8d
008CB6D8  8B D3                           mov edx, ebx
008CB6DA  48 8B CF                        mov rcx, rdi
008CB6DD  E8 2E AA 94 FF                  call 0x140216110
008CB6E2  E9 81 F7 FF FF                  jmp 0x1408cae68
008CB6E7  41 83 FF 04                     cmp r15d, 4
008CB6EB  0F 85 07 EE FF FF               jne 0x1408ca4f8
008CB6F1  41 8B 1C 24                     mov ebx, dword ptr [r12]
008CB6F5  89 9C 24 2C 01 00 00            mov dword ptr [rsp + 0x12c], ebx
008CB6FC  EB 05                           jmp 0x1408cb703
008CB6FE  E9 70 02 00 00                  jmp 0x1408cb973
008CB703  4C 8B 05 BE B3 6F 00            mov r8, qword ptr [rip + 0x6fb3be]
008CB70A  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
008CB70F  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
008CB714  48 8D 44 24 48                  lea rax, [rsp + 0x48]
008CB719  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008CB71E  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
008CB726  BA 20 00 00 00                  mov edx, 0x20
008CB72B  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008CB730  E8 1B DF F9 FF                  call 0x140869650
008CB735  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008CB739  85 C0                           test eax, eax
008CB73B  0F 88 32 02 00 00               js 0x1408cb973
008CB741  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
008CB746  85 DB                           test ebx, ebx
008CB748  0F 84 09 01 00 00               je 0x1408cb857
008CB74E  F0 81 88 A0 05 00 00 00 00 20 00  lock or dword ptr [rax + 0x5a0], 0x200000
008CB759  E9 7C FC FF FF                  jmp 0x1408cb3da
008CB75E  F0 0F BA 68 78 02               lock bts dword ptr [rax + 0x78], 2
008CB764  E9 F1 EC FF FF                  jmp 0x1408ca45a
008CB769  48 83 7C 24 58 FE               cmp qword ptr [rsp + 0x58], -2
008CB76F  0F 85 74 EB FF FF               jne 0x1408ca2e9
008CB775  EB 4D                           jmp 0x1408cb7c4
008CB777  66 39 9C 24 B2 01 00 00         cmp word ptr [rsp + 0x1b2], bx
008CB77F  0F 86 31 FA FF FF               jbe 0x1408cb1b6
008CB785  8D 43 01                        lea eax, [rbx + 1]
008CB788  66 89 84 24 B0 01 00 00         mov word ptr [rsp + 0x1b0], ax
008CB790  E9 16 FA FF FF                  jmp 0x1408cb1ab
008CB795  F0 81 A0 A0 05 00 00 FF FF F7 FF  lock and dword ptr [rax + 0x5a0], 0xfff7ffff
008CB7A0  E9 35 FC FF FF                  jmp 0x1408cb3da
008CB7A5  44 0F B6 4C 24 40               movzx r9d, byte ptr [rsp + 0x40]
008CB7AB  E9 74 F6 FF FF                  jmp 0x1408cae24
008CB7B0  BA 50 73 51 79                  mov edx, 0x79517350
008CB7B5  E8 26 C1 A2 FF                  call 0x1402f78e0
008CB7BA  B8 4B 00 00 C0                  mov eax, 0xc000004b
008CB7BF  E9 AF 01 00 00                  jmp 0x1408cb973
008CB7C4  41 83 FF 04                     cmp r15d, 4
008CB7C8  0F 85 2A ED FF FF               jne 0x1408ca4f8
008CB7CE  41 8B 04 24                     mov eax, dword ptr [r12]
008CB7D2  89 84 24 34 01 00 00            mov dword ptr [rsp + 0x134], eax
008CB7D9  EB 05                           jmp 0x1408cb7e0
008CB7DB  E9 93 01 00 00                  jmp 0x1408cb973
008CB7E0  49 8B 88 20 02 00 00            mov rcx, qword ptr [r8 + 0x220]
008CB7E7  83 F8 01                        cmp eax, 1
008CB7EA  0F 85 79 FD 24 00               jne 0x140b1b569
008CB7F0  F7 81 50 07 00 00 00 02 00 00   test dword ptr [rcx + 0x750], 0x200
008CB7FA  0F 84 B5 FF 24 00               je 0x140b1b7b5
008CB800  F0 41 81 88 A0 05 00 00 00 00 04 00  lock or dword ptr [r8 + 0x5a0], 0x40000
008CB80C  E9 58 EC FF FF                  jmp 0x1408ca469
008CB811  41 0F B6 D1                     movzx edx, r9b
008CB815  48 8B 0D 64 E2 70 00            mov rcx, qword ptr [rip + 0x70e264]
008CB81C  E8 FF 65 FA FF                  call 0x140871e20
008CB821  84 C0                           test al, al
008CB823  0F 84 98 FD FF FF               je 0x1408cb5c1
008CB829  4C 8B 64 24 68                  mov r12, qword ptr [rsp + 0x68]
008CB82E  49 8B 8C 24 20 02 00 00         mov rcx, qword ptr [r12 + 0x220]
008CB836  B2 51                           mov dl, 0x51
008CB838  0F B6 89 FA 05 00 00            movzx ecx, byte ptr [rcx + 0x5fa]
008CB83F  E8 84 48 14 00                  call 0x140a100c8
008CB844  84 C0                           test al, al
008CB846  0F 84 69 FF 24 00               je 0x140b1b7b5
008CB84C  44 0F B6 4C 24 40               movzx r9d, byte ptr [rsp + 0x40]
008CB852  E9 2D FB FF FF                  jmp 0x1408cb384
008CB857  F0 81 A0 A0 05 00 00 FF FF DF FF  lock and dword ptr [rax + 0x5a0], 0xffdfffff
008CB862  E9 73 FB FF FF                  jmp 0x1408cb3da
008CB867  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
008CB86C  E8 63 A2 03 00                  call 0x140905ad4
008CB871  E9 2C F3 FF FF                  jmp 0x1408caba2
008CB876  90                              nop
008CB877  90                              nop
008CB878  C6                              .byte 0xc6
008CB879  A0 8C 00 D6 A0 8C 00 53 A0      movabs al, byte ptr [0xa053008ca0d6008c]
008CB882  8C 00                           mov word ptr [rax], es
008CB884  53                              push rbx
008CB885  A0 8C 00 00 03 03 01 03 03      movabs al, byte ptr [0x30301030300008c]
008CB88E  03 03                           add eax, dword ptr [rbx]
008CB890  03 03                           add eax, dword ptr [rbx]
008CB892  03 03                           add eax, dword ptr [rbx]
008CB894  03 03                           add eax, dword ptr [rbx]
008CB896  03 03                           add eax, dword ptr [rbx]
008CB898  03 03                           add eax, dword ptr [rbx]
008CB89A  02 03                           add al, byte ptr [rbx]
008CB89C  02 03                           add al, byte ptr [rbx]
008CB89E  03 03                           add eax, dword ptr [rbx]
008CB8A0  03 03                           add eax, dword ptr [rbx]
008CB8A2  00 03                           add byte ptr [rbx], al
008CB8A4  01 03                           add dword ptr [rbx], eax
008CB8A6  00 03                           add byte ptr [rbx], al
008CB8A8  03 03                           add eax, dword ptr [rbx]
008CB8AA  00 03                           add byte ptr [rbx], al
008CB8AC  03 03                           add eax, dword ptr [rbx]
008CB8AE  03 03                           add eax, dword ptr [rbx]
008CB8B0  03 03                           add eax, dword ptr [rbx]
008CB8B2  03 03                           add eax, dword ptr [rbx]
008CB8B4  00 02                           add byte ptr [rdx], al
008CB8B6  03 03                           add eax, dword ptr [rbx]
008CB8B8  03 03                           add eax, dword ptr [rbx]
008CB8BA  03 03                           add eax, dword ptr [rbx]
008CB8BC  00 0F                           add byte ptr [rdi], cl
008CB8BE  1F                              .byte 0x1f
008CB8BF  00 32                           add byte ptr [rdx], dh
008CB8C1  A6                              cmpsb byte ptr [rsi], byte ptr [rdi]
008CB8C2  8C 00                           mov word ptr [rax], es
008CB8C4  03 AA 8C 00 CB B5               add ebp, dword ptr [rdx - 0x4a34ff74]
008CB8CA  8C 00                           mov word ptr [rax], es
008CB8CC  8C AD 8C 00 EF AB               mov word ptr [rbp - 0x5410ff74], gs
008CB8D2  8C 00                           mov word ptr [rax], es
008CB8D4  E0 AB                           loopne 0x1408cb881
008CB8D6  8C 00                           mov word ptr [rax], es
008CB8D8  BE B4 8C 00 F2                  mov esi, 0xf2008cb4
008CB8DD  B3 8C                           mov bl, 0x8c
008CB8DF  00 C8                           add al, cl
008CB8E1  B4 8C                           mov ah, 0x8c
008CB8E3  00 4B B6                        add byte ptr [rbx - 0x4a], cl
008CB8E6  8C 00                           mov word ptr [rax], es
008CB8E8  AD                              lodsd eax, dword ptr [rsi]
008CB8E9  A2 8C 00 FE A6 8C 00 75 A1      movabs byte ptr [0xa175008ca6fe008c], al
008CB8F2  8C 00                           mov word ptr [rax], es
008CB8F4  A9 A5 8C 00 C0                  test eax, 0xc0008ca5
008CB8F9  B0 8C                           mov al, 0x8c
008CB8FB  00 E4                           add ah, ah
008CB8FD  B2 B1                           mov dl, 0xb1
008CB8FF  00 51 B2                        add byte ptr [rcx - 0x4e], dl
008CB902  8C 00                           mov word ptr [rax], es
008CB904  D4                              .byte 0xd4
008CB905  B3 B1                           mov bl, 0xb1
008CB907  00 5A B5                        add byte ptr [rdx - 0x4b], bl
008CB90A  8C 00                           mov word ptr [rax], es
008CB90C  7F A7                           jg 0x1408cb8b5
008CB90E  8C 00                           mov word ptr [rax], es
008CB910  D8 B4 B1 00 69 B7 8C            fdiv dword ptr [rcx + rsi*4 - 0x73489700]
008CB917  00 5F B3                        add byte ptr [rdi - 0x4d], bl
008CB91A  8C 00                           mov word ptr [rax], es
008CB91C  E7 B6                           out 0xb6, eax
008CB91E  8C 00                           mov word ptr [rax], es
008CB920  82                              .byte 0x82
008CB921  B5 B1                           mov ch, 0xb1
008CB923  00 C5                           add ch, al
008CB925  AC                              lodsb al, byte ptr [rsi]
008CB926  8C 00                           mov word ptr [rax], es
008CB928  C2 B6 B1                        ret 0xb1b6
008CB92B  00 29                           add byte ptr [rcx], ch
008CB92D  B7 B1                           mov bh, 0xb1
008CB92F  00 02                           add byte ptr [rdx], al
008CB931  A5                              movsd dword ptr [rdi], dword ptr [rsi]
008CB932  8C 00                           mov word ptr [rax], es
008CB934  EE                              out dx, al
008CB935  A4                              movsb byte ptr [rdi], byte ptr [rsi]
008CB936  8C 00                           mov word ptr [rax], es
008CB938  77 B5                           ja 0x1408cb8ef
008CB93A  8C 00                           mov word ptr [rax], es
008CB93C  00 01                           add byte ptr [rcx], al
008CB93E  1E                              .byte 0x1e
008CB93F  1E                              .byte 0x1e
008CB940  02 1E                           add bl, byte ptr [rsi]
008CB942  1E                              .byte 0x1e
008CB943  03 1E                           add ebx, dword ptr [rsi]
008CB945  1E                              .byte 0x1e
008CB946  04 05                           add al, 5
008CB948  06                              .byte 0x06
008CB949  1E                              .byte 0x1e
008CB94A  07                              .byte 0x07
008CB94B  08 09                           or byte ptr [rcx], cl
008CB94D  1E                              .byte 0x1e
008CB94E  1E                              .byte 0x1e
008CB94F  0A 1E                           or bl, byte ptr [rsi]
008CB951  0B 0C 1E                        or ecx, dword ptr [rsi + rbx]
008CB954  1E                              .byte 0x1e
008CB955  1E                              .byte 0x1e
008CB956  0D 0E 1E 0F 10                  or eax, 0x100f1e0e
008CB95B  11 1E                           adc dword ptr [rsi], ebx
008CB95D  12 1E                           adc bl, byte ptr [rsi]
008CB95F  13 14 1E                        adc edx, dword ptr [rsi + rbx]
008CB962  1E                              .byte 0x1e
008CB963  15 16 1E 1E 17                  adc eax, 0x171e1e16
008CB968  18 12                           sbb byte ptr [rdx], dl
008CB96A  19 1A                           sbb dword ptr [rdx], ebx
008CB96C  1E                              .byte 0x1e
008CB96D  1E                              .byte 0x1e
008CB96E  1B 1E                           sbb ebx, dword ptr [rsi]
008CB970  1E                              .byte 0x1e
008CB971  1C 1D                           sbb al, 0x1d
008CB973  48 8B 8C 24 C0 03 00 00         mov rcx, qword ptr [rsp + 0x3c0]
008CB97B  48 33 CC                        xor rcx, rsp
008CB97E  E8 BD 0C DE FF                  call 0x1406ac640
008CB983  0F 28 B4 24 E0 03 00 00         movaps xmm6, xmmword ptr [rsp + 0x3e0]
008CB98B  0F 28 BC 24 D0 03 00 00         movaps xmm7, xmmword ptr [rsp + 0x3d0]
008CB993  48 81 C4 F0 03 00 00            add rsp, 0x3f0
008CB99A  41 5F                           pop r15
008CB99C  41 5E                           pop r14
008CB99E  41 5D                           pop r13
008CB9A0  41 5C                           pop r12
008CB9A2  5F                              pop rdi
008CB9A3  5E                              pop rsi
008CB9A4  5B                              pop rbx
008CB9A5  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtSetInformationThread(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m270;
    unsigned __int16 v_stack_m276;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m2B0;
    unsigned __int64 v_stack_m2B8;
    unsigned int v_stack_m2C8;
    unsigned __int64 v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned __int64 v_stack_m2F0;
    unsigned int v_stack_m2F4;
    unsigned int v_stack_m2F8;
    unsigned int v_stack_m2FC;
    unsigned int v_stack_m308;
    unsigned int v_stack_m30C;
    unsigned int v_stack_m310;
    unsigned int v_stack_m314;
    unsigned int v_stack_m318;
    unsigned __int64 v_stack_m320;
    unsigned __int64 v_stack_m328;
    unsigned __int64 v_stack_m330;
    unsigned __int64 v_stack_m340;
    unsigned __int64 v_stack_m348;
    unsigned __int64 v_stack_m358;
    unsigned __int64 v_stack_m360;
    unsigned __int64 v_stack_m368;
    unsigned __int64 v_stack_m370;
    unsigned int v_stack_m378;
    unsigned __int64 v_stack_m380;
    unsigned int v_stack_m388;
    unsigned __int64 v_stack_m390;
    unsigned int v_stack_m394;
    unsigned __int8 v_stack_m398;
    unsigned __int64 v_stack_m3A8;
    unsigned int v_stack_m3B0;
    unsigned __int16 v_stack_m3B4;
    unsigned __int64 v_stack_m3C0;
    unsigned int v_stack_m3C4;
    unsigned __int8 v_stack_m3C7;
    unsigned __int8 v_stack_m3C8;
    unsigned __int64 v_stack_m3D0;
    unsigned int v_stack_m3D8;
    unsigned __int64 v_stack_m3E0;
    unsigned __int8 v_stack_m3E8;
    unsigned __int64 v_stack_m3F0;
    unsigned __int64 v_stack_m3F8;
    unsigned __int64 v_stack_m400;
    unsigned int v_stack_m408;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;

    v_rsp = (v_rsp) - (0x3F0ULL);
    *(unsigned __int64 *)(v_rsp - 72) = v_xmm6;
    *(unsigned __int64 *)(v_rsp - 88) = v_xmm7;
    result = (*(unsigned __int64 *)(v_rip + 5507004)) ^ (v_rsp);
    v_stack_m68 = result;
    v_stack_m3D0 = a1;
    v_rdi = 0;
    v_stack_m3E0 = 0;
    v_stack_m368 = v_xmm0;
    a2 = 0;
    result = memset(v_stack_m278, a2, 264, a4);
    v_stack_m3B4 = 0;
    v_stack_m388 = 0;
    v_stack_m3C4 = 0;
    v_stack_m378 = 0;
    v_stack_m380 = 0;
    v_stack_m2F0 = 0;
    result = 0;
    v_stack_m358 = v_xmm0;
    v_stack_m348 = 0;
    v_stack_m2D0 = v_xmm0;
    v_stack_m3B0 = 0;
    v_stack_m340 = 0;
    v_stack_m328 = v_xmm0;
    v_stack_m330 = 0;
    v_stack_m3C0 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m3E8 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_008CA3C3;
    if (((unsigned int)((unsigned int)(a2))) != 2) goto loc_008CA0A4;
loc_008CA053:
    v_stack_m3C4 = 4;
loc_008CA062:
loc_008CA068:
    if ((unsigned int)((unsigned int)(a4)) == 0) goto loc_008CA098;
    if (((a3) & (4 - 1)) != 0) goto loc_008CA0ED;
    if ((a3 + (unsigned int)(a4) * 1) < a3) goto loc_008CA08E;
    if ((a3 + (unsigned int)(a4) * 1) <= 0) goto loc_008CA0F2;
loc_008CA08E:
    goto loc_008CA0F2;
loc_008CA098:
    goto loc_008CA0F2;
loc_008CA0A4:
    if (((unsigned int)((unsigned int)(a2) - 4)) > 52) goto loc_008CA053;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip - 9216078 + *(unsigned __int8 *)(v_rip - 9216078 + (unsigned int)(a2) - 4 * 1 + 9222280) * 4 + 9222264))) + (v_rip - 9216078);
loc_008CA0ED:
    result = ExRaiseDatatypeMisalignment(a1, a2, (unsigned int)(v_stack_m3C4), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
loc_008CA0F2:
    goto loc_008CA0F9;
loc_008CA0F9:
    if (((unsigned int)((unsigned int)(a2))) == 57) goto loc_008CA103;
    if (((unsigned int)((unsigned int)(a2))) == 48) {
        a2 = (unsigned int)(a4);
        a1 = a3;
        result = ProbeForWrite(a1, a2, (unsigned int)(v_stack_m3C4), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
        a4 = v_stack_m3E8;
    }
    goto loc_008CA12A;
loc_008CA12A:
    if (((unsigned int)((unsigned int)(a2))) == 5) goto loc_008CA20C;
    if (((unsigned int)((unsigned int)(a2))) == 44) goto loc_008CA2F4;
    if (((unsigned int)((unsigned int)(a2))) == 2) goto loc_008CA3E3;
    if (((unsigned int)((unsigned int)(a2))) == 9) goto loc_008CA2E9;
    v_rbx = (unsigned int)(((unsigned int)(a2)) + (-3));
    if (((unsigned int)(v_rbx)) > 54) goto loc_008CB577;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip - 9216078 + *(unsigned __int8 *)(v_rip - 9216078 + (int)((unsigned int)(v_rbx)) * 1 + 9222460) * 4 + 9222336))) + (v_rip - 9216078);
loc_008CA20C:
    if (((unsigned int)((unsigned int)(a4))) != 8) goto loc_008CA4F8;
    v_stack_m2D8 = *(unsigned __int64 *)(a3);
    goto loc_008CA229;
loc_008CA229:
    v_stack_m3F0 = 0;
    v_stack_m3F8 = 0;
    v_stack_m400 = v_stack_m3E0;
    v_stack_m408 = 0x79517350ULL;
    result = ObpReferenceObjectByHandleWithTag(v_stack_m3D0, 128, *(unsigned __int64 *)(v_rip + 7325848), a4);
    if (sign_flag) goto loc_008CB973;
    if (v_stack_m2D8 != 0) goto loc_008CA470;
    v_stack_m408 = 2;
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = PsImpersonateClient(v_stack_m3E0, a2, a3, a4);
loc_008CA297:
    result = ObfDereferenceObjectWithTag(v_stack_m3E0, (unsigned int)(0x79517350ULL), a3, a4);
    goto loc_008CB973;
loc_008CA2E9:
    goto loc_008CB973;
loc_008CA2F4:
    if (v_stack_m3D0 != -2) goto loc_008CA2E9;
    if (((unsigned int)((unsigned int)(a4))) != 8) goto loc_008CA4F8;
    v_stack_m330 = *(unsigned __int64 *)(a3);
    goto loc_008CA319;
loc_008CA319:
    v_stack_m3F0 = 0;
    v_stack_m3F8 = 0;
    v_stack_m400 = v_stack_m3E0;
    v_stack_m408 = 0x79517350ULL;
    result = ObpReferenceObjectByHandleWithTag(-2, (unsigned int)(0x400ULL), *(unsigned __int64 *)(v_rip + 7325608), a4);
    if (sign_flag) goto loc_008CB973;
    v_stack_m3A8 = 0;
    result = (*(unsigned __int64 *)(a3) == 0) ? 1 : 0;
    if ((unsigned int)(result) != 0) goto loc_008CA392;
    result = PspThreadFromTicket(v_stack_m330, v_stack_m3A8, *(unsigned __int64 *)(v_rip + 7325608), a4);
    if (sign_flag) goto loc_008CA9F9;
loc_008CA392:
    result = PspUpdateContainerImpersonation(v_stack_m3E0, v_stack_m3A8, *(unsigned __int64 *)(v_rip + 7325608), a4);
loc_008CA3A2:
    if (v_stack_m3A8 != 0) {
        a1 = v_stack_m3A8;
        result = ObfDereferenceObject(a1, v_stack_m3A8, *(unsigned __int64 *)(v_rip + 7325608), a4);
    }
loc_008CA3B2:
    result = ObfDereferenceObjectWithTag(v_stack_m3E0, (unsigned int)(0x79517350ULL), *(unsigned __int64 *)(v_rip + 7325608), a4);
loc_008CA3BC:
    goto loc_008CB973;
loc_008CA3C3:
    goto loc_008CA12A;
loc_008CA3E3:
    if (((unsigned int)((unsigned int)(a4))) != 4) goto loc_008CA4F8;
    v_stack_m308 = (unsigned int)((unsigned int)(*(unsigned int *)(a3)));
    goto loc_008CA3FF;
loc_008CA3FF:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3)) - 1)) > 30) goto loc_008CA2E9;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3)))) >= 16) goto loc_008CB581;
loc_008CA414:
    v_stack_m3F0 = v_stack_m3A8;
    v_stack_m3F8 = v_stack_m3A8;
    v_stack_m400 = v_stack_m3E0;
    v_stack_m408 = 0x79517350ULL;
    result = ObpReferenceObjectByHandleWithTag(v_stack_m3D0, (unsigned int)(0x400ULL), *(unsigned __int64 *)(v_rip + 7325357), a4);
    if (sign_flag) goto loc_008CB973;
    result = KeSetPriorityThread(v_stack_m3E0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3)))), *(unsigned __int64 *)(v_rip + 7325357), a4);
loc_008CA45A:
    result = ObfDereferenceObjectWithTag(v_stack_m3E0, (unsigned int)(0x79517350ULL), *(unsigned __int64 *)(v_rip + 7325357), a4);
loc_008CA469:
    result = 0;
    goto loc_008CB973;
loc_008CA470:
    v_stack_m3A8 = v_stack_m3A8;
    v_stack_m400 = v_stack_m3A8;
    v_stack_m408 = v_stack_m3A8;
    result = ObReferenceObjectByHandle(v_stack_m3E0, 4, *(unsigned __int64 *)(v_rip + 7396257), *(unsigned __int8 *)(a4 + 562));
    if (sign_flag) goto loc_008CA297;
    if ((*(unsigned int *)(v_stack_m3A8 + 192)) != 2) goto loc_008CACB3;
    v_stack_m408 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m3A8 + 196)));
    a4 = 0;
    a3 = 0;
    result = PsImpersonateClient(v_stack_m3E0, v_stack_m3A8, a3, a4);
    result = ObfDereferenceObject(v_stack_m3A8, v_stack_m3A8, a3, a4);
    goto loc_008CA297;
loc_008CA4F8:
    goto loc_008CB973;
loc_008CA9F9:
    goto loc_008CA3A2;
loc_008CACB3:
    result = ObfDereferenceObject(v_stack_m3E0, v_stack_m3A8, a3, a4);
    goto loc_008CA297;
loc_008CB577:
    goto loc_008CB973;
loc_008CB581:
    result = SeCheckPrivilegedObject(*(unsigned __int64 *)(v_rip + 7398741), v_stack_m3D0, (unsigned int)(0x400ULL), a4);
    if ((unsigned __int8)(result) == 0) goto loc_008CB5C1;
    goto loc_008CA414;
loc_008CB5C1:
    goto loc_008CB973;
loc_008CB973:
    a1 = (v_stack_m70) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m3D0, (unsigned int)(0x400ULL), v_stack_m3E8);
    v_rsp = (v_rsp) + (0x3F0ULL);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtSetInformationThread(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m270;
    uint16_t v_stack_m276;
    uint64_t v_stack_m278;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m2B0;
    uint64_t v_stack_m2B8;
    uint32_t v_stack_m2C8;
    uint64_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint64_t v_stack_m2F0;
    uint32_t v_stack_m2F4;
    uint32_t v_stack_m2F8;
    uint32_t v_stack_m2FC;
    uint32_t v_stack_m308;
    uint32_t v_stack_m30C;
    uint32_t v_stack_m310;
    uint32_t v_stack_m314;
    uint32_t v_stack_m318;
    uint64_t v_stack_m320;
    uint64_t v_stack_m328;
    uint64_t v_stack_m330;
    uint64_t v_stack_m340;
    uint64_t v_stack_m348;
    uint64_t v_stack_m358;
    uint64_t v_stack_m360;
    uint64_t v_stack_m368;
    uint64_t v_stack_m370;
    uint32_t v_stack_m378;
    uint64_t v_stack_m380;
    uint32_t v_stack_m388;
    uint64_t v_stack_m390;
    uint32_t v_stack_m394;
    uint8_t v_stack_m398;
    uint64_t v_stack_m3A8;
    uint32_t v_stack_m3B0;
    uint16_t v_stack_m3B4;
    uint64_t v_stack_m3C0;
    uint32_t v_stack_m3C4;
    uint8_t v_stack_m3C7;
    uint8_t v_stack_m3C8;
    uint64_t v_stack_m3D0;
    uint32_t v_stack_m3D8;
    uint64_t v_stack_m3E0;
    uint8_t v_stack_m3E8;
    uint64_t v_stack_m3F0;
    uint64_t v_stack_m3F8;
    uint64_t v_stack_m400;
    uint32_t v_stack_m408;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;

    local_rsp = (local_rsp) - (0x3F0ULL);
    *(uint64_t *)(local_rsp - 0x48) = v_xmm6;
    *(uint64_t *)(local_rsp - 0x58) = v_xmm7;
    result = (*(uint64_t *)(v_rip + 0x5407BC)) ^ (local_rsp);
    v_stack_m68 = result;
    v_stack_m3D0 = Arg1;
    local_rdi = 0;
    v_stack_m3E0 = 0;
    v_stack_m368 = v_xmm0;
    Arg2 = 0;
    result = memset(v_stack_m278, Arg2, 264, Arg4);
    v_stack_m3B4 = 0;
    v_stack_m388 = 0;
    v_stack_m3C4 = 0;
    v_stack_m378 = 0;
    v_stack_m380 = 0;
    v_stack_m2F0 = 0;
    result = 0;
    v_stack_m358 = v_xmm0;
    v_stack_m348 = 0;
    v_stack_m2D0 = v_xmm0;
    v_stack_m3B0 = 0;
    v_stack_m340 = 0;
    v_stack_m328 = v_xmm0;
    v_stack_m330 = 0;
    v_stack_m3C0 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m3E8 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_008CA3C3;
    if (((uint32_t)((uint32_t)(Arg2))) != 2) goto loc_008CA0A4;
loc_008CA053:
    v_stack_m3C4 = 4;
loc_008CA062:
loc_008CA068:
    if ((uint32_t)((uint32_t)(Arg4)) == 0) goto loc_008CA098;
    if (((Arg3) & (4 - 1)) != 0) goto loc_008CA0ED;
    if ((Arg3 + (uint32_t)(Arg4) * 1) < Arg3) goto loc_008CA08E;
    if ((Arg3 + (uint32_t)(Arg4) * 1) <= 0) goto loc_008CA0F2;
loc_008CA08E:
    goto loc_008CA0F2;
loc_008CA098:
    goto loc_008CA0F2;
loc_008CA0A4:
    if (((uint32_t)((uint32_t)(Arg2) - 4)) > 52) goto loc_008CA053;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip - 0x8CA04E + *(uint8_t *)(v_rip - 0x8CA04E + (uint32_t)(Arg2) - 0x4 * 1 + 0x8CB888) * 4 + 0x8CB878))) + (v_rip - 9216078);
loc_008CA0ED:
    result = ExRaiseDatatypeMisalignment(Arg1, Arg2, (uint32_t)(v_stack_m3C4), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
loc_008CA0F2:
    goto loc_008CA0F9;
loc_008CA0F9:
    if (((uint32_t)((uint32_t)(Arg2))) == 57) goto loc_008CA103;
    if (((uint32_t)((uint32_t)(Arg2))) == 48) {
        Arg2 = (uint32_t)(Arg4);
        Arg1 = Arg3;
        result = ProbeForWrite(Arg1, Arg2, (uint32_t)(v_stack_m3C4), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
        Arg4 = v_stack_m3E8;
    }
    goto loc_008CA12A;
loc_008CA12A:
    if (((uint32_t)((uint32_t)(Arg2))) == 5) goto loc_008CA20C;
    if (((uint32_t)((uint32_t)(Arg2))) == 44) goto loc_008CA2F4;
    if (((uint32_t)((uint32_t)(Arg2))) == 2) goto loc_008CA3E3;
    if (((uint32_t)((uint32_t)(Arg2))) == 9) goto loc_008CA2E9;
    local_rbx = (uint32_t)(((uint32_t)(Arg2)) + (-3));
    if (((uint32_t)(local_rbx)) > 54) goto loc_008CB577;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip - 0x8CA04E + *(uint8_t *)(v_rip - 0x8CA04E + (int32_t)((uint32_t)(local_rbx)) * 1 + 0x8CB93C) * 4 + 0x8CB8C0))) + (v_rip - 9216078);
loc_008CA20C:
    if (((uint32_t)((uint32_t)(Arg4))) != 8) goto loc_008CA4F8;
    v_stack_m2D8 = *(uint64_t *)(Arg3);
    goto loc_008CA229;
loc_008CA229:
    v_stack_m3F0 = 0;
    v_stack_m3F8 = 0;
    v_stack_m400 = v_stack_m3E0;
    v_stack_m408 = 0x79517350ULL;
    result = ObpReferenceObjectByHandleWithTag(v_stack_m3D0, 128, *(uint64_t *)(v_rip + 0x6FC898), Arg4);
    if (sign_flag) goto loc_008CB973;
    if (v_stack_m2D8 != 0) goto loc_008CA470;
    v_stack_m408 = 2;
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = PsImpersonateClient(v_stack_m3E0, Arg2, Arg3, Arg4);
loc_008CA297:
    result = ObfDereferenceObjectWithTag(v_stack_m3E0, (uint32_t)(0x79517350ULL), Arg3, Arg4);
    goto loc_008CB973;
loc_008CA2E9:
    goto loc_008CB973;
loc_008CA2F4:
    if (v_stack_m3D0 != -2) goto loc_008CA2E9;
    if (((uint32_t)((uint32_t)(Arg4))) != 8) goto loc_008CA4F8;
    v_stack_m330 = *(uint64_t *)(Arg3);
    goto loc_008CA319;
loc_008CA319:
    v_stack_m3F0 = 0;
    v_stack_m3F8 = 0;
    v_stack_m400 = v_stack_m3E0;
    v_stack_m408 = 0x79517350ULL;
    result = ObpReferenceObjectByHandleWithTag(-2, (uint32_t)(0x400ULL), *(uint64_t *)(v_rip + 0x6FC7A8), Arg4);
    if (sign_flag) goto loc_008CB973;
    v_stack_m3A8 = 0;
    result = (*(uint64_t *)(Arg3) == 0) ? 1 : 0;
    if ((uint32_t)(result) != 0) goto loc_008CA392;
    result = PspThreadFromTicket(v_stack_m330, v_stack_m3A8, *(uint64_t *)(v_rip + 0x6FC7A8), Arg4);
    if (sign_flag) goto loc_008CA9F9;
loc_008CA392:
    result = PspUpdateContainerImpersonation(v_stack_m3E0, v_stack_m3A8, *(uint64_t *)(v_rip + 0x6FC7A8), Arg4);
loc_008CA3A2:
    if (v_stack_m3A8 != 0) {
        Arg1 = v_stack_m3A8;
        result = ObfDereferenceObject(Arg1, v_stack_m3A8, *(uint64_t *)(v_rip + 0x6FC7A8), Arg4);
    }
loc_008CA3B2:
    result = ObfDereferenceObjectWithTag(v_stack_m3E0, (uint32_t)(0x79517350ULL), *(uint64_t *)(v_rip + 0x6FC7A8), Arg4);
loc_008CA3BC:
    goto loc_008CB973;
loc_008CA3C3:
    goto loc_008CA12A;
loc_008CA3E3:
    if (((uint32_t)((uint32_t)(Arg4))) != 4) goto loc_008CA4F8;
    v_stack_m308 = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3)));
    goto loc_008CA3FF;
loc_008CA3FF:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)) - 1)) > 30) goto loc_008CA2E9;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))) >= 16) goto loc_008CB581;
loc_008CA414:
    v_stack_m3F0 = v_stack_m3A8;
    v_stack_m3F8 = v_stack_m3A8;
    v_stack_m400 = v_stack_m3E0;
    v_stack_m408 = 0x79517350ULL;
    result = ObpReferenceObjectByHandleWithTag(v_stack_m3D0, (uint32_t)(0x400ULL), *(uint64_t *)(v_rip + 0x6FC6AD), Arg4);
    if (sign_flag) goto loc_008CB973;
    result = KeSetPriorityThread(v_stack_m3E0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))), *(uint64_t *)(v_rip + 0x6FC6AD), Arg4);
loc_008CA45A:
    result = ObfDereferenceObjectWithTag(v_stack_m3E0, (uint32_t)(0x79517350ULL), *(uint64_t *)(v_rip + 0x6FC6AD), Arg4);
loc_008CA469:
    result = 0;
    goto loc_008CB973;
loc_008CA470:
    v_stack_m3A8 = v_stack_m3A8;
    v_stack_m400 = v_stack_m3A8;
    v_stack_m408 = v_stack_m3A8;
    result = ObReferenceObjectByHandle(v_stack_m3E0, 4, *(uint64_t *)(v_rip + 0x70DBA1), *(uint8_t *)(Arg4 + 0x232));
    if (sign_flag) goto loc_008CA297;
    if ((*(uint32_t *)(v_stack_m3A8 + 0xC0)) != 2) goto loc_008CACB3;
    v_stack_m408 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m3A8 + 0xC4)));
    Arg4 = 0;
    Arg3 = 0;
    result = PsImpersonateClient(v_stack_m3E0, v_stack_m3A8, Arg3, Arg4);
    result = ObfDereferenceObject(v_stack_m3A8, v_stack_m3A8, Arg3, Arg4);
    goto loc_008CA297;
loc_008CA4F8:
    goto loc_008CB973;
loc_008CA9F9:
    goto loc_008CA3A2;
loc_008CACB3:
    result = ObfDereferenceObject(v_stack_m3E0, v_stack_m3A8, Arg3, Arg4);
    goto loc_008CA297;
loc_008CB577:
    goto loc_008CB973;
loc_008CB581:
    result = SeCheckPrivilegedObject(*(uint64_t *)(v_rip + 0x70E555), v_stack_m3D0, (uint32_t)(0x400ULL), Arg4);
    if ((uint8_t)(result) == 0) goto loc_008CB5C1;
    goto loc_008CA414;
loc_008CB5C1:
    goto loc_008CB973;
loc_008CB973:
    Arg1 = (v_stack_m70) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m3D0, (uint32_t)(0x400ULL), v_stack_m3E8);
    local_rsp = (local_rsp) + (0x3F0ULL);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008C9F60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
