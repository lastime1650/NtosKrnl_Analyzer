# RtlpNewSecurityObject

- RVA: `0x0092AB50`–`0x0092CD5F` (길이 `8,719` bytes)
- VA: `0x000000014092AB50`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0008DB40`
- 디코드: `2,104`개 명령, `8,719/8,719` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **82**; 고유 호출 대상: **28**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0092ACF8` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x0092AD1E` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (function, `0x00211BC0`)
- `0x0092AD7B` → [SepLocateTokenIntegrity](../../text/41/SepLocateTokenIntegrity_function_0041BF10.md) (function, `0x0041BF10`)
- `0x0092AD90` → [SepLocateTokenTrustLevel](../../text/3E/SepLocateTokenTrustLevel_function_003EDA40.md) (function, `0x003EDA40`)
- `0x0092AE0B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0092AE30` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092AE5D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092AEA7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092AED2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092AF0C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092AF35` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092AF46` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0092AF54` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0092AF65` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0092AF73` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0092B21D` → [RtlFindAceByType](../../text/41/RtlFindAceByType_function_00410AF0.md) (function, `0x00410AF0`)
- `0x0092B296` → [RtlFindAceByType](../../text/41/RtlFindAceByType_function_00410AF0.md) (function, `0x00410AF0`)
- `0x0092B315` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0092B3B6` → [RtlpInheritAcl2](RtlpInheritAcl2_function_0092D4D0.md) (function, `0x0092D4D0`)
- `0x0092B3D5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092B45B` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0092B469` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0092B47A` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (function, `0x0025FA10`)
- `0x0092B488` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0092B4B3` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0092B4D3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092B4F6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092B515` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092B52F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092B57C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092B5A6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0092B647` → [RtlpInheritAcl2](RtlpInheritAcl2_function_0092D4D0.md) (function, `0x0092D4D0`)
- `0x0092B666` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092B6B0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092B6C0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092B70B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092B740` → [RtlFindAceByType](../../text/41/RtlFindAceByType_function_00410AF0.md) (function, `0x00410AF0`)
- `0x0092B78C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092B913` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0092B9A3` → [RtlValidAcl](RtlValidAcl_function_0092A7A0.md) (function, `0x0092A7A0`)
- `0x0092BA34` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092BAD4` → [RtlpCombineAcls](RtlpCombineAcls_function_0092CD70.md) (function, `0x0092CD70`)
- `0x0092BAF8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092BB5B` → [RtlFindAceByType](../../text/41/RtlFindAceByType_function_00410AF0.md) (function, `0x00410AF0`)
- `0x0092BB83` → [RtlSidDominates](../../text/3F/RtlSidDominates_function_003FBD50.md) (function, `0x003FBD50`)
- `0x0092BD8A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0092BDF5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092BEBD` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x0092BF14` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0092C02E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0092C0C9` → [RtlpInheritAcl2](RtlpInheritAcl2_function_0092D4D0.md) (function, `0x0092D4D0`)
- `0x0092C0E7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092C135` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0092C1D3` → [RtlpInheritAcl2](RtlpInheritAcl2_function_0092D4D0.md) (function, `0x0092D4D0`)
- `0x0092C1F2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092C29C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092C2C2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092C30B` → [RtlpCreateServerAcl](../8B/RtlpCreateServerAcl_function_008BCF58.md) (function, `0x008BCF58`)
- `0x0092C391` → [RtlpNewSecurityObject](RtlpNewSecurityObject_function_0092AB50.md) (function, `0x0092AB50`)
- `0x0092C3B9` → [RtlpOwnerAcesPresent](../../text/3F/RtlpOwnerAcesPresent_function_003FB2F0.md) (function, `0x003FB2F0`)
- `0x0092C438` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x0092C4A8` → [RtlpNormalizeAcl](../8B/RtlpNormalizeAcl_function_008BC950.md) (function, `0x008BC950`)
- `0x0092C4FB` → [SepValidOwnerSubjectContext](../A3/SepValidOwnerSubjectContext_function_00A37568.md) (function, `0x00A37568`)
- `0x0092C541` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092C5A1` → [RtlpNormalizeAcl](../8B/RtlpNormalizeAcl_function_008BC950.md) (function, `0x008BC950`)
- `0x0092C5C9` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (function, `0x00456D10`)
- `0x0092C615` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092C695` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (function, `0x003A6BC0`)
- `0x0092C6C3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092C6FC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092C7C0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0092C80C` → [SePrivilegeCheck](../9B/SePrivilegeCheck_function_009BAE70.md) (function, `0x009BAE70`)
- `0x0092C824` → [SePrivilegedServiceAuditAlarm](../87/SePrivilegedServiceAuditAlarm_function_00871CB0.md) (function, `0x00871CB0`)
- `0x0092C860` → [RtlFindAceByType](../../text/41/RtlFindAceByType_function_00410AF0.md) (function, `0x00410AF0`)
- `0x0092C8A3` → [RtlCreateAcl](../91/RtlCreateAcl_function_00916F00.md) (function, `0x00916F00`)
- `0x0092C8CD` → [RtlAddProcessTrustLabelAce](RtlAddProcessTrustLabelAce_function_00929740.md) (function, `0x00929740`)
- `0x0092C937` → [RtlpComputeMergedAcl](../AC/RtlpComputeMergedAcl_function_00AC9B34.md) (function, `0x00AC9B34`)
- `0x0092CA36` → [SePrivilegeCheck](../9B/SePrivilegeCheck_function_009BAE70.md) (function, `0x009BAE70`)
- `0x0092CA4E` → [SePrivilegedServiceAuditAlarm](../87/SePrivilegedServiceAuditAlarm_function_00871CB0.md) (function, `0x00871CB0`)
- `0x0092CB58` → [RtlpValidTrustSubjectContext](../../text/3E/RtlpValidTrustSubjectContext_function_003ED770.md) (function, `0x003ED770`)
- `0x0092CCF5` → [RtlpValidTrustSubjectContext](../../text/3E/RtlpValidTrustSubjectContext_function_003ED770.md) (function, `0x003ED770`)
- `0x0092CD46` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [sub_004E9AEF](../../text/4E/Unknown_function_004E9AEF.md) at `0x004E9B8C`
- [RtlpNewSecurityObject](RtlpNewSecurityObject_function_0092AB50.md) at `0x0092C391`
- [SeAssignSecurity](../94/SeAssignSecurity_function_00949590.md) at `0x009495DA`

### Static image references
- `0x0092AB6C` → RVA `0x00E0A740` (`.data`; read)
- `0x0092C783` → RVA `0x00E67DB0` (`.data`; read)
- `0x0092C7DD` → RVA `0x00FD9B28` (`PAGEDATA`; read)
- `0x0092C9FE` → RVA `0x00FD9B00` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **64**
  - `0x0092ACF8` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x0092AD1E` → [ExAcquireResourceSharedLite](../../text/21/ExAcquireResourceSharedLite_function_00211BC0.md) (`PAGE` → `.text`)
  - `0x0092AD7B` → [SepLocateTokenIntegrity](../../text/41/SepLocateTokenIntegrity_function_0041BF10.md) (`PAGE` → `.text`)
  - `0x0092AD90` → [SepLocateTokenTrustLevel](../../text/3E/SepLocateTokenTrustLevel_function_003EDA40.md) (`PAGE` → `.text`)
  - `0x0092AE0B` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0092AE30` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092AE5D` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092AEA7` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092AED2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092AF0C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092AF35` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092AF46` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x0092AF54` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0092AF65` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x0092AF73` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0092B21D` → [RtlFindAceByType](../../text/41/RtlFindAceByType_function_00410AF0.md) (`PAGE` → `.text`)
  - `0x0092B296` → [RtlFindAceByType](../../text/41/RtlFindAceByType_function_00410AF0.md) (`PAGE` → `.text`)
  - `0x0092B315` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0092B3D5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092B45B` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x0092B469` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0092B47A` → [ExReleaseResourceLite](../../text/25/ExReleaseResourceLite_function_0025FA10.md) (`PAGE` → `.text`)
  - `0x0092B488` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0092B4B3` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0092B4D3` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092B4F6` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092B515` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092B52F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092B57C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092B5A6` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0092B666` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092B6B0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092B6C0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092B70B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092B740` → [RtlFindAceByType](../../text/41/RtlFindAceByType_function_00410AF0.md) (`PAGE` → `.text`)
  - `0x0092B78C` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092B913` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0092BA34` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092BAF8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092BB5B` → [RtlFindAceByType](../../text/41/RtlFindAceByType_function_00410AF0.md) (`PAGE` → `.text`)
  - `0x0092BB83` → [RtlSidDominates](../../text/3F/RtlSidDominates_function_003FBD50.md) (`PAGE` → `.text`)
  - `0x0092BD8A` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0092BDF5` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092BEBD` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x0092BF14` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0092C02E` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0092C0E7` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092C135` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0092C1F2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092C29C` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092C2C2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092C3B9` → [RtlpOwnerAcesPresent](../../text/3F/RtlpOwnerAcesPresent_function_003FB2F0.md) (`PAGE` → `.text`)
  - `0x0092C438` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x0092C541` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092C5C9` → [RtlSubAuthoritySid](../../text/45/RtlSubAuthoritySid_function_00456D10.md) (`PAGE` → `.text`)
  - `0x0092C615` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092C695` → [SeAccessCheck](../../text/3A/SeAccessCheck_function_003A6BC0.md) (`PAGE` → `.text`)
  - `0x0092C6C3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092C6FC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092C7C0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0092C860` → [RtlFindAceByType](../../text/41/RtlFindAceByType_function_00410AF0.md) (`PAGE` → `.text`)
  - `0x0092CB58` → [RtlpValidTrustSubjectContext](../../text/3E/RtlpValidTrustSubjectContext_function_003ED770.md) (`PAGE` → `.text`)
  - `0x0092CCF5` → [RtlpValidTrustSubjectContext](../../text/3E/RtlpValidTrustSubjectContext_function_003ED770.md) (`PAGE` → `.text`)
  - `0x0092CD46` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0092CCE4` → [sub_00B22F46](../B2/Unknown_function_00B22F46.md) (`tail-transfer`)
  - `0x0092CCFC` → [sub_00B22F46 + 0x38](../B2/Unknown_function_00B22F46.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0092AB50  40 55                           push rbp
0092AB52  53                              push rbx
0092AB53  56                              push rsi
0092AB54  57                              push rdi
0092AB55  41 54                           push r12
0092AB57  41 55                           push r13
0092AB59  41 56                           push r14
0092AB5B  41 57                           push r15
0092AB5D  48 8D AC 24 08 FE FF FF         lea rbp, [rsp - 0x1f8]
0092AB65  48 81 EC 08 03 00 00            sub rsp, 0x308
0092AB6C  48 8B 05 CD FB 4D 00            mov rax, qword ptr [rip + 0x4dfbcd]
0092AB73  48 33 C4                        xor rax, rsp
0092AB76  48 89 85 E0 01 00 00            mov qword ptr [rbp + 0x1e0], rax
0092AB7D  48 8B 85 80 02 00 00            mov rax, qword ptr [rbp + 0x280]
0092AB84  0F 57 C0                        xorps xmm0, xmm0
0092AB87  48 8B BD 78 02 00 00            mov rdi, qword ptr [rbp + 0x278]
0092AB8E  48 8B F1                        mov rsi, rcx
0092AB91  48 89 45 00                     mov qword ptr [rbp], rax
0092AB95  4C 8B DA                        mov r11, rdx
0092AB98  48 8B 85 88 02 00 00            mov rax, qword ptr [rbp + 0x288]
0092AB9F  48 89 85 98 00 00 00            mov qword ptr [rbp + 0x98], rax
0092ABA6  48 8B 85 90 02 00 00            mov rax, qword ptr [rbp + 0x290]
0092ABAD  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
0092ABB4  33 C0                           xor eax, eax
0092ABB6  4C 89 85 A0 00 00 00            mov qword ptr [rbp + 0xa0], r8
0092ABBD  45 33 C0                        xor r8d, r8d
0092ABC0  48 89 85 C8 00 00 00            mov qword ptr [rbp + 0xc8], rax
0092ABC7  45 8B F0                        mov r14d, r8d
0092ABCA  88 45 A0                        mov byte ptr [rbp - 0x60], al
0092ABCD  45 8B F8                        mov r15d, r8d
0092ABD0  88 45 BB                        mov byte ptr [rbp - 0x45], al
0092ABD3  45 8B E8                        mov r13d, r8d
0092ABD6  88 45 BA                        mov byte ptr [rbp - 0x46], al
0092ABD9  88 45 80                        mov byte ptr [rbp - 0x80], al
0092ABDC  88 45 B5                        mov byte ptr [rbp - 0x4b], al
0092ABDF  88 45 81                        mov byte ptr [rbp - 0x7f], al
0092ABE2  88 45 D0                        mov byte ptr [rbp - 0x30], al
0092ABE5  88 45 D1                        mov byte ptr [rbp - 0x2f], al
0092ABE8  88 45 B4                        mov byte ptr [rbp - 0x4c], al
0092ABEB  88 45 2C                        mov byte ptr [rbp + 0x2c], al
0092ABEE  88 45 B9                        mov byte ptr [rbp - 0x47], al
0092ABF1  89 85 F0 00 00 00               mov dword ptr [rbp + 0xf0], eax
0092ABF7  48 8D 85 00 01 00 00            lea rax, [rbp + 0x100]
0092ABFE  48 89 4D 18                     mov qword ptr [rbp + 0x18], rcx
0092AC02  8B 8D 70 02 00 00               mov ecx, dword ptr [rbp + 0x270]
0092AC08  4C 89 4D 48                     mov qword ptr [rbp + 0x48], r9
0092AC0C  45 8B C8                        mov r9d, r8d
0092AC0F  48 89 45 58                     mov qword ptr [rbp + 0x58], rax
0092AC13  48 89 55 E0                     mov qword ptr [rbp - 0x20], rdx
0092AC17  48 89 7D F8                     mov qword ptr [rbp - 8], rdi
0092AC1B  4C 89 45 C8                     mov qword ptr [rbp - 0x38], r8
0092AC1F  44 89 45 08                     mov dword ptr [rbp + 8], r8d
0092AC23  4C 89 45 88                     mov qword ptr [rbp - 0x78], r8
0092AC27  4C 89 45 70                     mov qword ptr [rbp + 0x70], r8
0092AC2B  4C 89 45 50                     mov qword ptr [rbp + 0x50], r8
0092AC2F  4C 89 45 10                     mov qword ptr [rbp + 0x10], r8
0092AC33  4C 89 85 90 00 00 00            mov qword ptr [rbp + 0x90], r8
0092AC3A  4C 89 45 20                     mov qword ptr [rbp + 0x20], r8
0092AC3E  4C 89 45 40                     mov qword ptr [rbp + 0x40], r8
0092AC42  4C 89 45 68                     mov qword ptr [rbp + 0x68], r8
0092AC46  4C 89 45 A8                     mov qword ptr [rbp - 0x58], r8
0092AC4A  C6 45 82 01                     mov byte ptr [rbp - 0x7e], 1
0092AC4E  44 89 45 C0                     mov dword ptr [rbp - 0x40], r8d
0092AC52  44 89 45 28                     mov dword ptr [rbp + 0x28], r8d
0092AC56  4C 89 45 30                     mov qword ptr [rbp + 0x30], r8
0092AC5A  4C 89 45 60                     mov qword ptr [rbp + 0x60], r8
0092AC5E  44 88 45 98                     mov byte ptr [rbp - 0x68], r8b
0092AC62  4C 89 45 38                     mov qword ptr [rbp + 0x38], r8
0092AC66  C6 45 B7 01                     mov byte ptr [rbp - 0x49], 1
0092AC6A  4C 89 45 78                     mov qword ptr [rbp + 0x78], r8
0092AC6E  44 88 45 BC                     mov byte ptr [rbp - 0x44], r8b
0092AC72  0F 11 85 A8 00 00 00            movups xmmword ptr [rbp + 0xa8], xmm0
0092AC79  0F 11 85 B8 00 00 00            movups xmmword ptr [rbp + 0xb8], xmm0
0092AC80  0F 11 85 E0 00 00 00            movups xmmword ptr [rbp + 0xe0], xmm0
0092AC87  0F BA E1 0D                     bt ecx, 0xd
0092AC8B  72 13                           jb 0x14092aca0
0092AC8D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0092AC96  0F B6 80 32 02 00 00            movzx eax, byte ptr [rax + 0x232]
0092AC9D  88 45 82                        mov byte ptr [rbp - 0x7e], al
0092ACA0  4D 85 DB                        test r11, r11
0092ACA3  0F 84 D6 04 00 00               je 0x14092b17f
0092ACA9  C6 45 B8 01                     mov byte ptr [rbp - 0x48], 1
0092ACAD  41 0F B7 53 02                  movzx edx, word ptr [r11 + 2]
0092ACB2  41 B8 80 00 00 00               mov r8d, 0x80
0092ACB8  0F B7 C2                        movzx eax, dx
0092ACBB  66 41 23 C0                     and ax, r8w
0092ACBF  0F 95 C3                        setne bl
0092ACC2  45 8D 60 81                     lea r12d, [r8 - 0x7f]
0092ACC6  C0 EA 06                        shr dl, 6
0092ACC9  80 E2 01                        and dl, 1
0092ACCC  89 95 88 00 00 00               mov dword ptr [rbp + 0x88], edx
0092ACD2  48 85 FF                        test rdi, rdi
0092ACD5  0F 84 3F 0B 00 00               je 0x14092b81a
0092ACDB  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0092ACE4  41 0F B6 D4                     movzx edx, r12b
0092ACE8  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0092ACEF  90                              nop
0092ACF0  48 8B 4F 10                     mov rcx, qword ptr [rdi + 0x10]
0092ACF4  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
0092ACF8  E8 C3 6E 8E FF                  call 0x140211bc0
0092ACFD  4C 39 2F                        cmp qword ptr [rdi], r13
0092AD00  74 21                           je 0x14092ad23
0092AD02  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0092AD0B  41 0F B6 D4                     movzx edx, r12b
0092AD0F  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0092AD16  90                              nop
0092AD17  48 8B 0F                        mov rcx, qword ptr [rdi]
0092AD1A  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
0092AD1E  E8 9D 6E 8E FF                  call 0x140211bc0
0092AD23  4C 8B 07                        mov r8, qword ptr [rdi]
0092AD26  88 5D D4                        mov byte ptr [rbp - 0x2c], bl
0092AD29  4D 85 C0                        test r8, r8
0092AD2C  0F 85 7A 1F 00 00               jne 0x14092ccac
0092AD32  4C 8B 47 10                     mov r8, qword ptr [rdi + 0x10]
0092AD36  48 8B 57 10                     mov rdx, qword ptr [rdi + 0x10]
0092AD3A  49 8B 80 98 00 00 00            mov rax, qword ptr [r8 + 0x98]
0092AD41  41 8B 88 90 00 00 00            mov ecx, dword ptr [r8 + 0x90]
0092AD48  49 8B 98 A8 00 00 00            mov rbx, qword ptr [r8 + 0xa8]
0092AD4F  48 03 C9                        add rcx, rcx
0092AD52  49 8B B0 B8 00 00 00            mov rsi, qword ptr [r8 + 0xb8]
0092AD59  48 8B BA A8 00 00 00            mov rdi, qword ptr [rdx + 0xa8]
0092AD60  4C 8B 2C C8                     mov r13, qword ptr [rax + rcx*8]
0092AD64  48 8B 82 98 00 00 00            mov rax, qword ptr [rdx + 0x98]
0092AD6B  8B 8A 90 00 00 00               mov ecx, dword ptr [rdx + 0x90]
0092AD71  48 03 C9                        add rcx, rcx
0092AD74  4C 8B 24 C8                     mov r12, qword ptr [rax + rcx*8]
0092AD78  49 8B C8                        mov rcx, r8
0092AD7B  E8 90 11 AF FF                  call 0x14041bf10
0092AD80  48 85 C0                        test rax, rax
0092AD83  0F 84 FA 19 00 00               je 0x14092c783
0092AD89  4C 8B 38                        mov r15, qword ptr [rax]
0092AD8C  48 8B 4D F8                     mov rcx, qword ptr [rbp - 8]
0092AD90  E8 AB 2C AC FF                  call 0x1403eda40
0092AD95  33 C9                           xor ecx, ecx
0092AD97  4C 8B F0                        mov r14, rax
0092AD9A  48 85 C0                        test rax, rax
0092AD9D  0F 85 9B 06 00 00               jne 0x14092b43e
0092ADA3  8B D1                           mov edx, ecx
0092ADA5  48 85 DB                        test rbx, rbx
0092ADA8  0F 84 DF 1C 00 00               je 0x14092ca8d
0092ADAE  0F B6 43 01                     movzx eax, byte ptr [rbx + 1]
0092ADB2  4C 8D 14 85 08 00 00 00         lea r10, [rax*4 + 8]
0092ADBA  48 85 FF                        test rdi, rdi
0092ADBD  0F 84 15 1C 00 00               je 0x14092c9d8
0092ADC3  0F B6 47 01                     movzx eax, byte ptr [rdi + 1]
0092ADC7  4C 8D 0C 85 20 00 00 00         lea r9, [rax*4 + 0x20]
0092ADCF  48 85 F6                        test rsi, rsi
0092ADD2  0F 84 F8 1B 00 00               je 0x14092c9d0
0092ADD8  44 0F B7 46 02                  movzx r8d, word ptr [rsi + 2]
0092ADDD  41 0F B6 44 24 01               movzx eax, byte ptr [r12 + 1]
0092ADE3  41 0F B6 4D 01                  movzx ecx, byte ptr [r13 + 1]
0092ADE8  48 03 C8                        add rcx, rax
0092ADEB  41 0F B6 47 01                  movzx eax, byte ptr [r15 + 1]
0092ADF0  48 03 C8                        add rcx, rax
0092ADF3  48 8D 14 8A                     lea rdx, [rdx + rcx*4]
0092ADF7  B9 40 00 00 00                  mov ecx, 0x40
0092ADFC  49 03 D2                        add rdx, r10
0092ADFF  49 03 D0                        add rdx, r8
0092AE02  41 B8 53 65 53 64               mov r8d, 0x64536553
0092AE08  49 03 D1                        add rdx, r9
0092AE0B  E8 E0 72 25 00                  call 0x140b820f0
0092AE10  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
0092AE14  48 85 C0                        test rax, rax
0092AE17  0F 84 32 06 00 00               je 0x14092b44f
0092AE1D  45 0F B6 45 01                  movzx r8d, byte ptr [r13 + 1]
0092AE22  49 8B D5                        mov rdx, r13
0092AE25  48 8B C8                        mov rcx, rax
0092AE28  4E 8D 04 85 08 00 00 00         lea r8, [r8*4 + 8]
0092AE30  E8 0B BA D9 FF                  call 0x1406c6840
0092AE35  41 0F B6 45 01                  movzx eax, byte ptr [r13 + 1]
0092AE3A  49 8B D7                        mov rdx, r15
0092AE3D  45 0F B6 47 01                  movzx r8d, byte ptr [r15 + 1]
0092AE42  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
0092AE46  48 83 C1 08                     add rcx, 8
0092AE4A  4E 8D 04 85 08 00 00 00         lea r8, [r8*4 + 8]
0092AE52  4C 8D 2C 81                     lea r13, [rcx + rax*4]
0092AE56  49 8B CD                        mov rcx, r13
0092AE59  4C 89 6D 10                     mov qword ptr [rbp + 0x10], r13
0092AE5D  E8 DE B9 D9 FF                  call 0x1406c6840
0092AE62  41 0F B6 47 01                  movzx eax, byte ptr [r15 + 1]
0092AE67  4C 8D 3C 85 08 00 00 00         lea r15, [rax*4 + 8]
0092AE6F  4D 03 FD                        add r15, r13
0092AE72  4C 89 7D 20                     mov qword ptr [rbp + 0x20], r15
0092AE76  4D 85 F6                        test r14, r14
0092AE79  0F 85 F3 08 00 00               jne 0x14092b772
0092AE7F  33 C9                           xor ecx, ecx
0092AE81  48 89 8D 90 00 00 00            mov qword ptr [rbp + 0x90], rcx
0092AE88  48 85 DB                        test rbx, rbx
0092AE8B  0F 84 F4 1B 00 00               je 0x14092ca85
0092AE91  44 0F B6 43 01                  movzx r8d, byte ptr [rbx + 1]
0092AE96  48 8B D3                        mov rdx, rbx
0092AE99  49 8B CF                        mov rcx, r15
0092AE9C  4D 8B F7                        mov r14, r15
0092AE9F  4E 8D 04 85 08 00 00 00         lea r8, [r8*4 + 8]
0092AEA7  E8 94 B9 D9 FF                  call 0x1406c6840
0092AEAC  0F B6 43 01                     movzx eax, byte ptr [rbx + 1]
0092AEB0  4D 8D 3C 87                     lea r15, [r15 + rax*4]
0092AEB4  49 83 C7 08                     add r15, 8
0092AEB8  4C 89 7D 20                     mov qword ptr [rbp + 0x20], r15
0092AEBC  33 DB                           xor ebx, ebx
0092AEBE  45 0F B6 44 24 01               movzx r8d, byte ptr [r12 + 1]
0092AEC4  49 8B D4                        mov rdx, r12
0092AEC7  49 8B CF                        mov rcx, r15
0092AECA  4E 8D 04 85 08 00 00 00         lea r8, [r8*4 + 8]
0092AED2  E8 69 B9 D9 FF                  call 0x1406c6840
0092AED7  45 0F B6 64 24 01               movzx r12d, byte ptr [r12 + 1]
0092AEDD  49 83 C4 02                     add r12, 2
0092AEE1  4F 8D 24 A7                     lea r12, [r15 + r12*4]
0092AEE5  4C 89 65 68                     mov qword ptr [rbp + 0x68], r12
0092AEE9  48 85 FF                        test rdi, rdi
0092AEEC  0F 84 B4 1B 00 00               je 0x14092caa6
0092AEF2  44 0F B6 47 01                  movzx r8d, byte ptr [rdi + 1]
0092AEF7  48 8B D7                        mov rdx, rdi
0092AEFA  49 8B CC                        mov rcx, r12
0092AEFD  4C 89 65 40                     mov qword ptr [rbp + 0x40], r12
0092AF01  4D 8B EC                        mov r13, r12
0092AF04  4E 8D 04 85 08 00 00 00         lea r8, [r8*4 + 8]
0092AF0C  E8 2F B9 D9 FF                  call 0x1406c6840
0092AF11  0F B6 47 01                     movzx eax, byte ptr [rdi + 1]
0092AF15  4D 8D 24 84                     lea r12, [r12 + rax*4]
0092AF19  49 83 C4 08                     add r12, 8
0092AF1D  4C 89 65 68                     mov qword ptr [rbp + 0x68], r12
0092AF21  48 85 F6                        test rsi, rsi
0092AF24  0F 84 52 1B 00 00               je 0x14092ca7c
0092AF2A  44 0F B7 46 02                  movzx r8d, word ptr [rsi + 2]
0092AF2F  48 8B D6                        mov rdx, rsi
0092AF32  49 8B CC                        mov rcx, r12
0092AF35  E8 06 B9 D9 FF                  call 0x1406c6840
0092AF3A  48 8B 5D F8                     mov rbx, qword ptr [rbp - 8]
0092AF3E  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
0092AF42  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
0092AF46  E8 C5 4A 93 FF                  call 0x14025fa10
0092AF4B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0092AF54  E8 97 40 93 FF                  call 0x14025eff0
0092AF59  48 8B 0B                        mov rcx, qword ptr [rbx]
0092AF5C  48 85 C9                        test rcx, rcx
0092AF5F  74 17                           je 0x14092af78
0092AF61  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
0092AF65  E8 A6 4A 93 FF                  call 0x14025fa10
0092AF6A  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0092AF73  E8 78 40 93 FF                  call 0x14025eff0
0092AF78  4C 8B 4D 50                     mov r9, qword ptr [rbp + 0x50]
0092AF7C  48 8B 75 18                     mov rsi, qword ptr [rbp + 0x18]
0092AF80  44 8B 45 D4                     mov r8d, dword ptr [rbp - 0x2c]
0092AF84  8B 8D 70 02 00 00               mov ecx, dword ptr [rbp + 0x270]
0092AF8A  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
0092AF8E  41 0F B7 53 02                  movzx edx, word ptr [r11 + 2]
0092AF93  66 85 D2                        test dx, dx
0092AF96  78 13                           js 0x14092afab
0092AF98  49 8B 43 08                     mov rax, qword ptr [r11 + 8]
0092AF9C  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0092AFA0  48 85 C0                        test rax, rax
0092AFA3  74 12                           je 0x14092afb7
0092AFA5  C6 45 B5 01                     mov byte ptr [rbp - 0x4b], 1
0092AFA9  EB 2C                           jmp 0x14092afd7
0092AFAB  41 8B 43 04                     mov eax, dword ptr [r11 + 4]
0092AFAF  85 C0                           test eax, eax
0092AFB1  0F 85 AA 08 00 00               jne 0x14092b861
0092AFB7  F6 C1 20                        test cl, 0x20
0092AFBA  0F 85 5F 16 00 00               jne 0x14092c61f
0092AFC0  45 84 C0                        test r8b, r8b
0092AFC3  49 8B C1                        mov rax, r9
0092AFC6  49 0F 45 C7                     cmovne rax, r15
0092AFCA  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0092AFCE  48 85 C0                        test rax, rax
0092AFD1  0F 84 83 07 00 00               je 0x14092b75a
0092AFD7  66 85 D2                        test dx, dx
0092AFDA  0F 88 10 07 00 00               js 0x14092b6f0
0092AFE0  49 8B 5B 10                     mov rbx, qword ptr [r11 + 0x10]
0092AFE4  48 89 5D F0                     mov qword ptr [rbp - 0x10], rbx
0092AFE8  48 85 DB                        test rbx, rbx
0092AFEB  75 20                           jne 0x14092b00d
0092AFED  F6 C1 40                        test cl, 0x40
0092AFF0  0F 85 55 15 00 00               jne 0x14092c54b
0092AFF6  45 84 C0                        test r8b, r8b
0092AFF9  49 8B DE                        mov rbx, r14
0092AFFC  49 0F 45 DD                     cmovne rbx, r13
0092B000  48 89 5D F0                     mov qword ptr [rbp - 0x10], rbx
0092B004  48 85 DB                        test rbx, rbx
0092B007  0F 84 23 08 00 00               je 0x14092b830
0092B00D  44 8B D1                        mov r10d, ecx
0092B010  44 8B E1                        mov r12d, ecx
0092B013  41 83 E2 04                     and r10d, 4
0092B017  0F B7 CA                        movzx ecx, dx
0092B01A  44 8B C2                        mov r8d, edx
0092B01D  44 89 55 B0                     mov dword ptr [rbp - 0x50], r10d
0092B021  41 0F 95 C5                     setne r13b
0092B025  8B FA                           mov edi, edx
0092B027  41 83 E4 02                     and r12d, 2
0092B02B  0F 95 45 B6                     setne byte ptr [rbp - 0x4a]
0092B02F  66 83 E1 10                     and cx, 0x10
0092B033  0F B7 C1                        movzx eax, cx
0092B036  66 F7 D8                        neg ax
0092B039  8B C2                           mov eax, edx
0092B03B  45 1B C9                        sbb r9d, r9d
0092B03E  C1 E8 02                        shr eax, 2
0092B041  41 D1 E8                        shr r8d, 1
0092B044  83 E0 08                        and eax, 8
0092B047  D1 EF                           shr edi, 1
0092B049  41 81 E0 00 04 00 00            and r8d, 0x400
0092B050  81 E7 00 10 00 00               and edi, 0x1000
0092B056  41 83 E1 04                     and r9d, 4
0092B05A  45 33 F6                        xor r14d, r14d
0092B05D  66 85 C9                        test cx, cx
0092B060  0F 85 34 01 00 00               jne 0x14092b19a
0092B066  45 8B FE                        mov r15d, r14d
0092B069  48 85 F6                        test rsi, rsi
0092B06C  0F 85 52 07 00 00               jne 0x14092b7c4
0092B072  49 8B F6                        mov rsi, r14
0092B075  41 0B F8                        or edi, r8d
0092B078  41 8B DE                        mov ebx, r14d
0092B07B  0B F8                           or edi, eax
0092B07D  41 0B F9                        or edi, r9d
0092B080  0F 85 6C 02 00 00               jne 0x14092b2f2
0092B086  48 85 F6                        test rsi, rsi
0092B089  0F 85 63 02 00 00               jne 0x14092b2f2
0092B08F  41 8B C4                        mov eax, r12d
0092B092  40 88 75 81                     mov byte ptr [rbp - 0x7f], sil
0092B096  F7 D8                           neg eax
0092B098  4C 89 75 90                     mov qword ptr [rbp - 0x70], r14
0092B09C  C7 45 9C 0B 00 00 80            mov dword ptr [rbp - 0x64], 0x8000000b
0092B0A3  1B C9                           sbb ecx, ecx
0092B0A5  81 E1 00 04 00 00               and ecx, 0x400
0092B0AB  89 4D C0                        mov dword ptr [rbp - 0x40], ecx
0092B0AE  EB 34                           jmp 0x14092b0e4
0092B0B0  48 8B 55 90                     mov rdx, qword ptr [rbp - 0x70]
0092B0B4  45 33 F6                        xor r14d, r14d
0092B0B7  48 89 55 90                     mov qword ptr [rbp - 0x70], rdx
0092B0BB  85 DB                           test ebx, ebx
0092B0BD  0F 89 A6 07 00 00               jns 0x14092b869
0092B0C3  48 89 55 90                     mov qword ptr [rbp - 0x70], rdx
0092B0C7  81 FB 0B 00 00 80               cmp ebx, 0x8000000b
0092B0CD  0F 85 A3 05 00 00               jne 0x14092b676
0092B0D3  44 0F B6 4D 81                  movzx r9d, byte ptr [rbp - 0x7f]
0092B0D8  44 8B 55 B0                     mov r10d, dword ptr [rbp - 0x50]
0092B0DC  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
0092B0E0  44 88 4D 81                     mov byte ptr [rbp - 0x7f], r9b
0092B0E4  45 0F B7 6B 02                  movzx r13d, word ptr [r11 + 2]
0092B0E9  45 85 E4                        test r12d, r12d
0092B0EC  B8 00 80 00 00                  mov eax, 0x8000
0092B0F1  B9 00 88 00 00                  mov ecx, 0x8800
0092B0F6  0F 44 C8                        cmove ecx, eax
0092B0F9  41 0F B6 C5                     movzx eax, r13b
0092B0FD  24 30                           and al, 0x30
0092B0FF  3C 30                           cmp al, 0x30
0092B101  0F 84 26 16 00 00               je 0x14092c72d
0092B107  44 8B E9                        mov r13d, ecx
0092B10A  89 4D D8                        mov dword ptr [rbp - 0x28], ecx
0092B10D  41 0F B7 53 02                  movzx edx, word ptr [r11 + 2]
0092B112  45 85 D2                        test r10d, r10d
0092B115  0F B7 CA                        movzx ecx, dx
0092B118  8B FA                           mov edi, edx
0092B11A  41 0F 95 C7                     setne r15b
0092B11E  66 83 E1 10                     and cx, 0x10
0092B122  0F B7 C1                        movzx eax, cx
0092B125  66 F7 D8                        neg ax
0092B128  8B C2                           mov eax, edx
0092B12A  45 1B C0                        sbb r8d, r8d
0092B12D  C1 E8 02                        shr eax, 2
0092B130  D1 EF                           shr edi, 1
0092B132  83 E0 08                        and eax, 8
0092B135  81 E7 00 04 00 00               and edi, 0x400
0092B13B  41 83 E0 04                     and r8d, 4
0092B13F  66 85 C9                        test cx, cx
0092B142  0F 85 9D 02 00 00               jne 0x14092b3e5
0092B148  4D 8B E6                        mov r12, r14
0092B14B  48 8B 55 18                     mov rdx, qword ptr [rbp + 0x18]
0092B14F  48 85 D2                        test rdx, rdx
0092B152  0F 85 98 06 00 00               jne 0x14092b7f0
0092B158  49 8B F6                        mov rsi, r14
0092B15B  0B F8                           or edi, eax
0092B15D  41 8B DE                        mov ebx, r14d
0092B160  41 0B F8                        or edi, r8d
0092B163  0F 85 1A 04 00 00               jne 0x14092b583
0092B169  48 85 F6                        test rsi, rsi
0092B16C  0F 85 11 04 00 00               jne 0x14092b583
0092B172  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
0092B176  C7 45 9C 0B 00 00 80            mov dword ptr [rbp - 0x64], 0x8000000b
0092B17D  EB 63                           jmp 0x14092b1e2
0092B17F  4C 8D 9D A8 00 00 00            lea r11, [rbp + 0xa8]
0092B186  44 88 45 B8                     mov byte ptr [rbp - 0x48], r8b
0092B18A  4C 89 5D E0                     mov qword ptr [rbp - 0x20], r11
0092B18E  C6 85 A8 00 00 00 01            mov byte ptr [rbp + 0xa8], 1
0092B195  E9 13 FB FF FF                  jmp 0x14092acad
0092B19A  66 85 D2                        test dx, dx
0092B19D  0F 89 C5 15 00 00               jns 0x14092c768
0092B1A3  41 8B 4B 0C                     mov ecx, dword ptr [r11 + 0xc]
0092B1A7  85 C9                           test ecx, ecx
0092B1A9  0F 84 28 19 00 00               je 0x14092cad7
0092B1AF  4D 8D 3C 0B                     lea r15, [r11 + rcx]
0092B1B3  E9 B1 FE FF FF                  jmp 0x14092b069
0092B1B8  48 8B 55 C8                     mov rdx, qword ptr [rbp - 0x38]
0092B1BC  45 33 F6                        xor r14d, r14d
0092B1BF  48 89 55 C8                     mov qword ptr [rbp - 0x38], rdx
0092B1C3  89 5D 9C                        mov dword ptr [rbp - 0x64], ebx
0092B1C6  85 DB                           test ebx, ebx
0092B1C8  0F 89 12 05 00 00               jns 0x14092b6e0
0092B1CE  48 89 55 C8                     mov qword ptr [rbp - 0x38], rdx
0092B1D2  81 FB 0B 00 00 80               cmp ebx, 0x8000000b
0092B1D8  0F 85 6F 06 00 00               jne 0x14092b84d
0092B1DE  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
0092B1E2  41 0F B7 4B 02                  movzx ecx, word ptr [r11 + 2]
0092B1E7  0F B6 C1                        movzx eax, cl
0092B1EA  24 30                           and al, 0x30
0092B1EC  3C 30                           cmp al, 0x30
0092B1EE  0F 84 62 15 00 00               je 0x14092c756
0092B1F4  4C 8B 75 C8                     mov r14, qword ptr [rbp - 0x38]
0092B1F8  4C 8B A5 90 00 00 00            mov r12, qword ptr [rbp + 0x90]
0092B1FF  33 FF                           xor edi, edi
0092B201  89 7D B0                        mov dword ptr [rbp - 0x50], edi
0092B204  41 0F B7 43 02                  movzx eax, word ptr [r11 + 2]
0092B209  A8 10                           test al, 0x10
0092B20B  0F 85 F2 01 00 00               jne 0x14092b403
0092B211  48 8B CF                        mov rcx, rdi
0092B214  4C 8D 45 B0                     lea r8, [rbp - 0x50]
0092B218  BA 14 00 00 00                  mov edx, 0x14
0092B21D  E8 CE 58 AE FF                  call 0x140410af0
0092B222  48 85 C0                        test rax, rax
0092B225  48 8B D8                        mov rbx, rax
0092B228  48 8D 50 08                     lea rdx, [rax + 8]
0092B22C  48 0F 44 D7                     cmove rdx, rdi
0092B230  48 85 D2                        test rdx, rdx
0092B233  0F 85 18 19 00 00               jne 0x14092cb51
0092B239  FF 45 B0                        inc dword ptr [rbp - 0x50]
0092B23C  48 85 DB                        test rbx, rbx
0092B23F  0F 85 D2 12 00 00               jne 0x14092c517
0092B245  8B B5 70 02 00 00               mov esi, dword ptr [rbp + 0x270]
0092B24B  44 8D 7B 04                     lea r15d, [rbx + 4]
0092B24F  0F BA E6 0B                     bt esi, 0xb
0092B253  0F 82 E7 15 00 00               jb 0x14092c840
0092B259  48 8B 7D E0                     mov rdi, qword ptr [rbp - 0x20]
0092B25D  4C 89 75 78                     mov qword ptr [rbp + 0x78], r14
0092B261  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
0092B265  33 C9                           xor ecx, ecx
0092B267  A8 10                           test al, 0x10
0092B269  0F 85 B2 01 00 00               jne 0x14092b421
0092B26F  8B D9                           mov ebx, ecx
0092B271  89 4D 9C                        mov dword ptr [rbp - 0x64], ecx
0092B274  C7 85 D0 00 00 00 00 00 00 00   mov dword ptr [rbp + 0xd0], 0
0092B27E  66 C7 85 D4 00 00 00 00 01      mov word ptr [rbp + 0xd4], 0x100
0092B287  89 4D B0                        mov dword ptr [rbp - 0x50], ecx
0092B28A  4C 8D 45 B0                     lea r8, [rbp - 0x50]
0092B28E  BA 15 00 00 00                  mov edx, 0x15
0092B293  48 8B CB                        mov rcx, rbx
0092B296  E8 55 58 AE FF                  call 0x140410af0
0092B29B  48 8B C8                        mov rcx, rax
0092B29E  48 85 C0                        test rax, rax
0092B2A1  0F 85 F2 19 00 00               jne 0x14092cc99
0092B2A7  FF 45 B0                        inc dword ptr [rbp - 0x50]
0092B2AA  48 85 C9                        test rcx, rcx
0092B2AD  75 DB                           jne 0x14092b28a
0092B2AF  8B 5D 9C                        mov ebx, dword ptr [rbp - 0x64]
0092B2B2  85 DB                           test ebx, ebx
0092B2B4  0F 88 93 05 00 00               js 0x14092b84d
0092B2BA  8B CE                           mov ecx, esi
0092B2BC  C1 E9 08                        shr ecx, 8
0092B2BF  83 E1 01                        and ecx, 1
0092B2C2  8B D1                           mov edx, ecx
0092B2C4  83 CA 02                        or edx, 2
0092B2C7  0F BA E6 09                     bt esi, 9
0092B2CB  0F 43 D1                        cmovae edx, ecx
0092B2CE  8B DA                           mov ebx, edx
0092B2D0  41 0B DF                        or ebx, r15d
0092B2D3  0F BA E6 0A                     bt esi, 0xa
0092B2D7  0F 43 DA                        cmovae ebx, edx
0092B2DA  85 DB                           test ebx, ebx
0092B2DC  0F 84 49 04 00 00               je 0x14092b72b
0092B2E2  48 8B 75 30                     mov rsi, qword ptr [rbp + 0x30]
0092B2E6  4C 8B F6                        mov r14, rsi
0092B2E9  4C 8B 65 10                     mov r12, qword ptr [rbp + 0x10]
0092B2ED  E9 E5 05 00 00                  jmp 0x14092b8d7
0092B2F2  B8 C8 00 00 00                  mov eax, 0xc8
0092B2F7  89 45 9C                        mov dword ptr [rbp - 0x64], eax
0092B2FA  33 C9                           xor ecx, ecx
0092B2FC  8B D1                           mov edx, ecx
0092B2FE  41 83 FE 02                     cmp r14d, 2
0092B302  0F 83 AC FD FF FF               jae 0x14092b0b4
0092B308  8B D0                           mov edx, eax
0092B30A  B9 00 01 00 00                  mov ecx, 0x100
0092B30F  41 B8 53 65 41 63               mov r8d, 0x63416553
0092B315  E8 D6 6D 25 00                  call 0x140b820f0
0092B31A  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
0092B31E  48 8B D0                        mov rdx, rax
0092B321  48 85 C0                        test rax, rax
0092B324  0F 84 1B 19 00 00               je 0x14092cc45
0092B32A  44 0F B6 8D 68 02 00 00         movzx r9d, byte ptr [rbp + 0x268]
0092B332  48 8D 45 C0                     lea rax, [rbp - 0x40]
0092B336  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
0092B33E  44 8B C7                        mov r8d, edi
0092B341  48 8D 45 81                     lea rax, [rbp - 0x7f]
0092B345  48 8B CE                        mov rcx, rsi
0092B348  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0092B350  48 8D 45 9C                     lea rax, [rbp - 0x64]
0092B354  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
0092B359  49 8B D7                        mov rdx, r15
0092B35C  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0092B361  8B 85 60 02 00 00               mov eax, dword ptr [rbp + 0x260]
0092B367  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
0092B36B  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0092B36F  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0092B374  48 8B 45 00                     mov rax, qword ptr [rbp]
0092B378  C7 44 24 58 02 00 00 00         mov dword ptr [rsp + 0x58], 2
0092B380  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0092B385  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
0092B389  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0092B38E  48 8B 45 20                     mov rax, qword ptr [rbp + 0x20]
0092B392  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0092B397  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
0092B39B  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0092B3A0  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
0092B3A4  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0092B3A9  0F B6 45 B6                     movzx eax, byte ptr [rbp - 0x4a]
0092B3AD  44 88 6C 24 28                  mov byte ptr [rsp + 0x28], r13b
0092B3B2  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0092B3B6  E8 15 21 00 00                  call 0x14092d4d0
0092B3BB  8B D8                           mov ebx, eax
0092B3BD  85 C0                           test eax, eax
0092B3BF  0F 88 F5 02 00 00               js 0x14092b6ba
0092B3C5  83 7D 9C 00                     cmp dword ptr [rbp - 0x64], 0
0092B3C9  0F 85 E1 FC FF FF               jne 0x14092b0b0
0092B3CF  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0092B3D3  33 D2                           xor edx, edx
0092B3D5  E8 96 74 25 00                  call 0x140b82870
0092B3DA  45 33 F6                        xor r14d, r14d
0092B3DD  41 8B D6                        mov edx, r14d
0092B3E0  E9 D2 FC FF FF                  jmp 0x14092b0b7
0092B3E5  66 85 D2                        test dx, dx
0092B3E8  0F 89 D7 16 00 00               jns 0x14092cac5
0092B3EE  41 8B 4B 0C                     mov ecx, dword ptr [r11 + 0xc]
0092B3F2  85 C9                           test ecx, ecx
0092B3F4  0F 84 EE 16 00 00               je 0x14092cae8
0092B3FA  4D 8D 24 0B                     lea r12, [r11 + rcx]
0092B3FE  E9 48 FD FF FF                  jmp 0x14092b14b
0092B403  66 85 C0                        test ax, ax
0092B406  0F 89 83 13 00 00               jns 0x14092c78f
0092B40C  41 8B 43 0C                     mov eax, dword ptr [r11 + 0xc]
0092B410  85 C0                           test eax, eax
0092B412  0F 84 86 16 00 00               je 0x14092ca9e
0092B418  49 8D 0C 03                     lea rcx, [r11 + rax]
0092B41C  E9 F3 FD FF FF                  jmp 0x14092b214
0092B421  66 85 C0                        test ax, ax
0092B424  0F 89 49 16 00 00               jns 0x14092ca73
0092B42A  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
0092B42D  85 C0                           test eax, eax
0092B42F  0F 84 C3 16 00 00               je 0x14092caf8
0092B435  48 8D 1C 07                     lea rbx, [rdi + rax]
0092B439  E9 33 FE FF FF                  jmp 0x14092b271
0092B43E  0F B6 40 01                     movzx eax, byte ptr [rax + 1]
0092B442  48 8D 14 85 08 00 00 00         lea rdx, [rax*4 + 8]
0092B44A  E9 56 F9 FF FF                  jmp 0x14092ada5
0092B44F  48 8B 5D F8                     mov rbx, qword ptr [rbp - 8]
0092B453  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
0092B457  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
0092B45B  E8 B0 45 93 FF                  call 0x14025fa10
0092B460  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0092B469  E8 82 3B 93 FF                  call 0x14025eff0
0092B46E  48 8B 0B                        mov rcx, qword ptr [rbx]
0092B471  48 85 C9                        test rcx, rcx
0092B474  74 17                           je 0x14092b48d
0092B476  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
0092B47A  E8 91 45 93 FF                  call 0x14025fa10
0092B47F  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0092B488  E8 63 3B 93 FF                  call 0x14025eff0
0092B48D  B8 9A 00 00 C0                  mov eax, 0xc000009a
0092B492  E9 A5 18 00 00                  jmp 0x14092cd3c
0092B497  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
0092B49B  44 0F B6 6D 80                  movzx r13d, byte ptr [rbp - 0x80]
0092B4A0  0F B7 4E 02                     movzx ecx, word ptr [rsi + 2]
0092B4A4  3B F9                           cmp edi, ecx
0092B4A6  76 10                           jbe 0x14092b4b8
0092B4A8  44 8B C7                        mov r8d, edi
0092B4AB  33 D2                           xor edx, edx
0092B4AD  44 2B C1                        sub r8d, ecx
0092B4B0  48 03 CB                        add rcx, rbx
0092B4B3  E8 88 B7 D9 FF                  call 0x1406c6c40
0092B4B8  8B C3                           mov eax, ebx
0092B4BA  41 2B C6                        sub eax, r14d
0092B4BD  41 89 46 10                     mov dword ptr [r14 + 0x10], eax
0092B4C1  8B C7                           mov eax, edi
0092B4C3  48 03 D8                        add rbx, rax
0092B4C6  48 8B 55 E8                     mov rdx, qword ptr [rbp - 0x18]
0092B4CA  48 8B CB                        mov rcx, rbx
0092B4CD  45 8B C4                        mov r8d, r12d
0092B4D0  41 8B FC                        mov edi, r12d
0092B4D3  E8 68 B3 D9 FF                  call 0x1406c6840
0092B4D8  8B C3                           mov eax, ebx
0092B4DA  48 03 DF                        add rbx, rdi
0092B4DD  41 2B C6                        sub eax, r14d
0092B4E0  41 89 46 04                     mov dword ptr [r14 + 4], eax
0092B4E4  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
0092B4E8  48 85 C0                        test rax, rax
0092B4EB  74 15                           je 0x14092b502
0092B4ED  45 8B C7                        mov r8d, r15d
0092B4F0  48 8B D0                        mov rdx, rax
0092B4F3  48 8B CB                        mov rcx, rbx
0092B4F6  E8 45 B3 D9 FF                  call 0x1406c6840
0092B4FB  41 2B DE                        sub ebx, r14d
0092B4FE  41 89 5E 08                     mov dword ptr [r14 + 8], ebx
0092B502  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
0092B506  33 C0                           xor eax, eax
0092B508  8B D8                           mov ebx, eax
0092B50A  48 8B 4D 38                     mov rcx, qword ptr [rbp + 0x38]
0092B50E  48 85 C9                        test rcx, rcx
0092B511  74 07                           je 0x14092b51a
0092B513  33 D2                           xor edx, edx
0092B515  E8 56 73 25 00                  call 0x140b82870
0092B51A  80 7D B9 00                     cmp byte ptr [rbp - 0x47], 0
0092B51E  0F 85 E2 10 00 00               jne 0x14092c606
0092B524  48 8B 4D 50                     mov rcx, qword ptr [rbp + 0x50]
0092B528  48 85 C9                        test rcx, rcx
0092B52B  74 07                           je 0x14092b534
0092B52D  33 D2                           xor edx, edx
0092B52F  E8 3C 73 25 00                  call 0x140b82870
0092B534  80 7D A0 00                     cmp byte ptr [rbp - 0x60], 0
0092B538  75 38                           jne 0x14092b572
0092B53A  80 7D BA 00                     cmp byte ptr [rbp - 0x46], 0
0092B53E  75 32                           jne 0x14092b572
0092B540  80 7D BB 00                     cmp byte ptr [rbp - 0x45], 0
0092B544  0F 85 A0 11 00 00               jne 0x14092c6ea
0092B54A  48 8B 4D 78                     mov rcx, qword ptr [rbp + 0x78]
0092B54E  48 85 C9                        test rcx, rcx
0092B551  0F 85 5D 12 00 00               jne 0x14092c7b4
0092B557  45 84 ED                        test r13b, r13b
0092B55A  0F 85 42 01 00 00               jne 0x14092b6a2
0092B560  48 8B 85 A0 00 00 00            mov rax, qword ptr [rbp + 0xa0]
0092B567  4C 89 30                        mov qword ptr [rax], r14
0092B56A  8B C3                           mov eax, ebx
0092B56C  E9 CB 17 00 00                  jmp 0x14092cd3c
0092B571  CC                              int3
0092B572  4D 85 FF                        test r15, r15
0092B575  74 C9                           je 0x14092b540
0092B577  33 D2                           xor edx, edx
0092B579  49 8B CF                        mov rcx, r15
0092B57C  E8 EF 72 25 00                  call 0x140b82870
0092B581  EB BD                           jmp 0x14092b540
0092B583  B8 C8 00 00 00                  mov eax, 0xc8
0092B588  89 45 9C                        mov dword ptr [rbp - 0x64], eax
0092B58B  33 C9                           xor ecx, ecx
0092B58D  8B D1                           mov edx, ecx
0092B58F  41 83 FE 02                     cmp r14d, 2
0092B593  0F 83 23 FC FF FF               jae 0x14092b1bc
0092B599  8B D0                           mov edx, eax
0092B59B  B9 00 01 00 00                  mov ecx, 0x100
0092B5A0  41 B8 53 65 41 63               mov r8d, 0x63416553
0092B5A6  E8 45 6B 25 00                  call 0x140b820f0
0092B5AB  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0092B5AF  48 8B D0                        mov rdx, rax
0092B5B2  48 85 C0                        test rax, rax
0092B5B5  0F 84 8D 02 00 00               je 0x14092b848
0092B5BB  44 0F B6 8D 68 02 00 00         movzx r9d, byte ptr [rbp + 0x268]
0092B5C3  48 8D 45 28                     lea rax, [rbp + 0x28]
0092B5C7  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
0092B5CF  44 8B C7                        mov r8d, edi
0092B5D2  48 8D 45 D0                     lea rax, [rbp - 0x30]
0092B5D6  48 8B CE                        mov rcx, rsi
0092B5D9  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0092B5E1  48 8D 45 9C                     lea rax, [rbp - 0x64]
0092B5E5  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
0092B5EA  49 8B D4                        mov rdx, r12
0092B5ED  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0092B5F2  8B 85 60 02 00 00               mov eax, dword ptr [rbp + 0x260]
0092B5F8  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
0092B5FC  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0092B600  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0092B605  48 8B 45 00                     mov rax, qword ptr [rbp]
0092B609  C7 44 24 58 02 00 00 00         mov dword ptr [rsp + 0x58], 2
0092B611  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0092B616  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
0092B61A  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0092B61F  48 8B 45 20                     mov rax, qword ptr [rbp + 0x20]
0092B623  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0092B628  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
0092B62C  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0092B631  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
0092B635  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0092B63A  0F B6 45 B6                     movzx eax, byte ptr [rbp - 0x4a]
0092B63E  44 88 7C 24 28                  mov byte ptr [rsp + 0x28], r15b
0092B643  88 44 24 20                     mov byte ptr [rsp + 0x20], al
0092B647  E8 84 1E 00 00                  call 0x14092d4d0
0092B64C  8B D8                           mov ebx, eax
0092B64E  85 C0                           test eax, eax
0092B650  0F 88 AF 00 00 00               js 0x14092b705
0092B656  83 7D 9C 00                     cmp dword ptr [rbp - 0x64], 0
0092B65A  0F 85 58 FB FF FF               jne 0x14092b1b8
0092B660  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
0092B664  33 D2                           xor edx, edx
0092B666  E8 05 72 25 00                  call 0x140b82870
0092B66B  45 33 F6                        xor r14d, r14d
0092B66E  41 8B D6                        mov edx, r14d
0092B671  E9 49 FB FF FF                  jmp 0x14092b1bf
0092B676  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0092B67A  4C 8B FA                        mov r15, rdx
0092B67D  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
0092B681  45 32 ED                        xor r13b, r13b
0092B684  E9 81 FE FF FF                  jmp 0x14092b50a
0092B689  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0092B68E  45 32 ED                        xor r13b, r13b
0092B691  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
0092B695  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0092B699  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
0092B69D  E9 68 FE FF FF                  jmp 0x14092b50a
0092B6A2  48 85 F6                        test rsi, rsi
0092B6A5  0F 84 B5 FE FF FF               je 0x14092b560
0092B6AB  33 D2                           xor edx, edx
0092B6AD  48 8B CE                        mov rcx, rsi
0092B6B0  E8 BB 71 25 00                  call 0x140b82870
0092B6B5  E9 A6 FE FF FF                  jmp 0x14092b560
0092B6BA  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
0092B6BE  33 D2                           xor edx, edx
0092B6C0  E8 AB 71 25 00                  call 0x140b82870
0092B6C5  33 C0                           xor eax, eax
0092B6C7  8B D0                           mov edx, eax
0092B6C9  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
0092B6CF  0F 85 DF F9 FF FF               jne 0x14092b0b4
0092B6D5  8B 45 9C                        mov eax, dword ptr [rbp - 0x64]
0092B6D8  41 FF C6                        inc r14d
0092B6DB  E9 1A FC FF FF                  jmp 0x14092b2fa
0092B6E0  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
0092B6E4  4C 8B F2                        mov r14, rdx
0092B6E7  C6 45 BB 01                     mov byte ptr [rbp - 0x45], 1
0092B6EB  E9 08 FB FF FF                  jmp 0x14092b1f8
0092B6F0  41 8B 43 08                     mov eax, dword ptr [r11 + 8]
0092B6F4  85 C0                           test eax, eax
0092B6F6  0F 84 F1 F8 FF FF               je 0x14092afed
0092B6FC  49 8D 1C 03                     lea rbx, [r11 + rax]
0092B700  E9 DF F8 FF FF                  jmp 0x14092afe4
0092B705  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
0092B709  33 D2                           xor edx, edx
0092B70B  E8 60 71 25 00                  call 0x140b82870
0092B710  33 C0                           xor eax, eax
0092B712  8B D0                           mov edx, eax
0092B714  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
0092B71A  0F 85 9C FA FF FF               jne 0x14092b1bc
0092B720  8B 45 9C                        mov eax, dword ptr [rbp - 0x64]
0092B723  41 FF C6                        inc r14d
0092B726  E9 60 FE FF FF                  jmp 0x14092b58b
0092B72B  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
0092B72F  45 33 E4                        xor r12d, r12d
0092B732  A8 10                           test al, 0x10
0092B734  75 71                           jne 0x14092b7a7
0092B736  41 8B CC                        mov ecx, r12d
0092B739  45 33 C0                        xor r8d, r8d
0092B73C  41 8D 50 11                     lea edx, [r8 + 0x11]
0092B740  E8 AB 53 AE FF                  call 0x140410af0
0092B745  4C 8B F0                        mov r14, rax
0092B748  48 85 C0                        test rax, rax
0092B74B  0F 85 55 01 00 00               jne 0x14092b8a6
0092B751  48 8B 75 30                     mov rsi, qword ptr [rbp + 0x30]
0092B755  E9 8F FB FF FF                  jmp 0x14092b2e9
0092B75A  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0092B75E  BB 7C 00 00 C0                  mov ebx, 0xc000007c
0092B763  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
0092B767  4C 8B FE                        mov r15, rsi
0092B76A  45 32 ED                        xor r13b, r13b
0092B76D  E9 98 FD FF FF                  jmp 0x14092b50a
0092B772  45 0F B6 46 01                  movzx r8d, byte ptr [r14 + 1]
0092B777  49 8B D6                        mov rdx, r14
0092B77A  49 8B CF                        mov rcx, r15
0092B77D  4C 89 BD 90 00 00 00            mov qword ptr [rbp + 0x90], r15
0092B784  4E 8D 04 85 08 00 00 00         lea r8, [r8*4 + 8]
0092B78C  E8 AF B0 D9 FF                  call 0x1406c6840
0092B791  41 0F B6 46 01                  movzx eax, byte ptr [r14 + 1]
0092B796  4D 8D 3C 87                     lea r15, [r15 + rax*4]
0092B79A  49 83 C7 08                     add r15, 8
0092B79E  4C 89 7D 20                     mov qword ptr [rbp + 0x20], r15
0092B7A2  E9 E1 F6 FF FF                  jmp 0x14092ae88
0092B7A7  66 85 C0                        test ax, ax
0092B7AA  0F 89 C1 0F 00 00               jns 0x14092c771
0092B7B0  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
0092B7B3  85 C0                           test eax, eax
0092B7B5  0F 84 35 13 00 00               je 0x14092caf0
0092B7BB  48 8D 0C 07                     lea rcx, [rdi + rax]
0092B7BF  E9 75 FF FF FF                  jmp 0x14092b739
0092B7C4  0F B7 4E 02                     movzx ecx, word ptr [rsi + 2]
0092B7C8  F6 C1 10                        test cl, 0x10
0092B7CB  0F 84 A1 F8 FF FF               je 0x14092b072
0092B7D1  66 85 C9                        test cx, cx
0092B7D4  0F 89 42 13 00 00               jns 0x14092cb1c
0092B7DA  8B 4E 0C                        mov ecx, dword ptr [rsi + 0xc]
0092B7DD  85 C9                           test ecx, ecx
0092B7DF  0F 84 8D F8 FF FF               je 0x14092b072
0092B7E5  8B F1                           mov esi, ecx
0092B7E7  48 03 75 18                     add rsi, qword ptr [rbp + 0x18]
0092B7EB  E9 85 F8 FF FF                  jmp 0x14092b075
0092B7F0  0F B7 4A 02                     movzx ecx, word ptr [rdx + 2]
0092B7F4  F6 C1 10                        test cl, 0x10
0092B7F7  0F 84 5B F9 FF FF               je 0x14092b158
0092B7FD  66 85 C9                        test cx, cx
0092B800  0F 89 D9 12 00 00               jns 0x14092cadf
0092B806  8B 4A 0C                        mov ecx, dword ptr [rdx + 0xc]
0092B809  85 C9                           test ecx, ecx
0092B80B  0F 84 47 F9 FF FF               je 0x14092b158
0092B811  48 8D 34 0A                     lea rsi, [rdx + rcx]
0092B815  E9 41 F9 FF FF                  jmp 0x14092b15b
0092B81A  44 0F B6 C3                     movzx r8d, bl
0092B81E  44 89 45 D4                     mov dword ptr [rbp - 0x2c], r8d
0092B822  66 85 C0                        test ax, ax
0092B825  0F 84 63 F7 FF FF               je 0x14092af8e
0092B82B  E9 AB F4 FF FF                  jmp 0x14092acdb
0092B830  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0092B834  BB 5B 00 00 C0                  mov ebx, 0xc000005b
0092B839  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
0092B83D  4C 8B FE                        mov r15, rsi
0092B840  45 32 ED                        xor r13b, r13b
0092B843  E9 C2 FC FF FF                  jmp 0x14092b50a
0092B848  BB 17 00 00 C0                  mov ebx, 0xc0000017
0092B84D  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
0092B851  45 32 ED                        xor r13b, r13b
0092B854  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0092B858  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
0092B85C  E9 A9 FC FF FF                  jmp 0x14092b50a
0092B861  49 03 C3                        add rax, r11
0092B864  E9 33 F7 FF FF                  jmp 0x14092af9c
0092B869  8B 45 C0                        mov eax, dword ptr [rbp - 0x40]
0092B86C  44 8B E8                        mov r13d, eax
0092B86F  44 0F B6 4D 81                  movzx r9d, byte ptr [rbp - 0x7f]
0092B874  41 83 E5 08                     and r13d, 8
0092B878  44 8B 55 B0                     mov r10d, dword ptr [rbp - 0x50]
0092B87C  41 81 CD 04 20 00 00            or r13d, 0x2004
0092B883  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
0092B887  45 03 ED                        add r13d, r13d
0092B88A  25 00 14 00 00                  and eax, 0x1400
0092B88F  C6 45 A0 01                     mov byte ptr [rbp - 0x60], 1
0092B893  44 0B E8                        or r13d, eax
0092B896  44 88 4D 81                     mov byte ptr [rbp - 0x7f], r9b
0092B89A  45 03 ED                        add r13d, r13d
0092B89D  44 89 6D D8                     mov dword ptr [rbp - 0x28], r13d
0092B8A1  E9 67 F8 FF FF                  jmp 0x14092b10d
0092B8A6  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
0092B8AA  48 8D 70 08                     lea rsi, [rax + 8]
0092B8AE  8B 58 04                        mov ebx, dword ptr [rax + 4]
0092B8B1  48 89 75 30                     mov qword ptr [rbp + 0x30], rsi
0092B8B5  88 4D 98                        mov byte ptr [rbp - 0x68], cl
0092B8B8  80 F9 08                        cmp cl, 8
0092B8BB  0F 84 CE 12 00 00               je 0x14092cb8f
0092B8C1  F6 C1 10                        test cl, 0x10
0092B8C4  0F 85 C5 12 00 00               jne 0x14092cb8f
0092B8CA  4C 8B 65 10                     mov r12, qword ptr [rbp + 0x10]
0092B8CE  F6 C1 08                        test cl, 8
0092B8D1  0F 85 E6 0C 00 00               jne 0x14092c5bd
0092B8D7  85 DB                           test ebx, ebx
0092B8D9  0F 84 4F 0B 00 00               je 0x14092c42e
0092B8DF  4C 8B 65 F8                     mov r12, qword ptr [rbp - 8]
0092B8E3  4D 85 F6                        test r14, r14
0092B8E6  75 15                           jne 0x14092b8fd
0092B8E8  4D 85 E4                        test r12, r12
0092B8EB  0F 84 E0 0D 00 00               je 0x14092c6d1
0092B8F1  48 8B 75 10                     mov rsi, qword ptr [rbp + 0x10]
0092B8F5  48 89 75 30                     mov qword ptr [rbp + 0x30], rsi
0092B8F9  44 88 75 98                     mov byte ptr [rbp - 0x68], r14b
0092B8FD  48 85 F6                        test rsi, rsi
0092B900  0F 84 84 09 00 00               je 0x14092c28a
0092B906  33 D2                           xor edx, edx
0092B908  48 8D 8D 08 01 00 00            lea rcx, [rbp + 0x108]
0092B90F  44 8D 42 78                     lea r8d, [rdx + 0x78]
0092B913  E8 28 B3 D9 FF                  call 0x1406c6c40
0092B918  0F B6 55 98                     movzx edx, byte ptr [rbp - 0x68]
0092B91C  48 B8 00 00 FF FF FF 7F 00 00   movabs rax, 0x7fffffff0000
0092B926  48 C7 85 00 01 00 00 02 00 80 00  mov qword ptr [rbp + 0x100], 0x800002
0092B931  C7 85 D8 00 00 00 00 00 00 00   mov dword ptr [rbp + 0xd8], 0
0092B93B  66 C7 85 DC 00 00 00 00 10      mov word ptr [rbp + 0xdc], 0x1000
0092B944  48 3B F0                        cmp rsi, rax
0092B947  0F 86 7C 0B 00 00               jbe 0x14092c4c9
0092B94D  0F B6 06                        movzx eax, byte ptr [rsi]
0092B950  24 0F                           and al, 0xf
0092B952  3C 01                           cmp al, 1
0092B954  0F 85 6F 0B 00 00               jne 0x14092c4c9
0092B95A  80 7E 01 0F                     cmp byte ptr [rsi + 1], 0xf
0092B95E  0F 87 65 0B 00 00               ja 0x14092c4c9
0092B964  8B 4E 02                        mov ecx, dword ptr [rsi + 2]
0092B967  2B 8D D8 00 00 00               sub ecx, dword ptr [rbp + 0xd8]
0092B96D  75 0D                           jne 0x14092b97c
0092B96F  0F B7 4E 06                     movzx ecx, word ptr [rsi + 6]
0092B973  0F B7 85 DC 00 00 00            movzx eax, word ptr [rbp + 0xdc]
0092B97A  2B C8                           sub ecx, eax
0092B97C  85 C9                           test ecx, ecx
0092B97E  0F 85 05 FD FF FF               jne 0x14092b689
0092B984  F7 C2 E0 FF FF FF               test edx, 0xffffffe0
0092B98A  0F 85 84 13 00 00               jne 0x14092cd14
0092B990  F7 C3 F8 FF FF FF               test ebx, 0xfffffff8
0092B996  0F 85 85 13 00 00               jne 0x14092cd21
0092B99C  48 8D 8D 00 01 00 00            lea rcx, [rbp + 0x100]
0092B9A3  E8 F8 ED FF FF                  call 0x14092a7a0
0092B9A8  84 C0                           test al, al
0092B9AA  0F 84 7C 12 00 00               je 0x14092cc2c
0092B9B0  44 0F B7 8D 04 01 00 00         movzx r9d, word ptr [rbp + 0x104]
0092B9B8  48 8D 95 08 01 00 00            lea rdx, [rbp + 0x108]
0092B9BF  44 0F B7 95 02 01 00 00         movzx r10d, word ptr [rbp + 0x102]
0092B9C7  33 C9                           xor ecx, ecx
0092B9C9  44 8B C1                        mov r8d, ecx
0092B9CC  45 3B C1                        cmp r8d, r9d
0092B9CF  0F 82 A8 05 00 00               jb 0x14092bf7d
0092B9D5  0F B6 4E 01                     movzx ecx, byte ptr [rsi + 1]
0092B9D9  4C 8D 85 00 01 00 00            lea r8, [rbp + 0x100]
0092B9E0  4D 03 C2                        add r8, r10
0092B9E3  B8 00 00 00 00                  mov eax, 0
0092B9E8  49 3B D0                        cmp rdx, r8
0092B9EB  48 0F 47 D0                     cmova rdx, rax
0092B9EF  66 41 03 CF                     add cx, r15w
0092B9F3  66 C1 E1 02                     shl cx, 2
0092B9F7  48 85 D2                        test rdx, rdx
0092B9FA  0F 84 6C 0B 00 00               je 0x14092c56c
0092BA00  0F B7 C1                        movzx eax, cx
0092BA03  48 03 C2                        add rax, rdx
0092BA06  49 3B C0                        cmp rax, r8
0092BA09  0F 87 5D 0B 00 00               ja 0x14092c56c
0092BA0F  0F B6 45 98                     movzx eax, byte ptr [rbp - 0x68]
0092BA13  66 89 4A 02                     mov word ptr [rdx + 2], cx
0092BA17  48 8D 4A 08                     lea rcx, [rdx + 8]
0092BA1B  88 42 01                        mov byte ptr [rdx + 1], al
0092BA1E  C6 02 11                        mov byte ptr [rdx], 0x11
0092BA21  89 5A 04                        mov dword ptr [rdx + 4], ebx
0092BA24  48 8B D6                        mov rdx, rsi
0092BA27  44 0F B6 46 01                  movzx r8d, byte ptr [rsi + 1]
0092BA2C  4E 8D 04 85 08 00 00 00         lea r8, [r8*4 + 8]
0092BA34  E8 07 AE D9 FF                  call 0x1406c6840
0092BA39  66 FF 85 04 01 00 00            inc word ptr [rbp + 0x104]
0092BA40  48 8D 8D 00 01 00 00            lea rcx, [rbp + 0x100]
0092BA47  33 D2                           xor edx, edx
0092BA49  C6 85 00 01 00 00 02            mov byte ptr [rbp + 0x100], 2
0092BA50  89 55 9C                        mov dword ptr [rbp - 0x64], edx
0092BA53  8B 85 70 02 00 00               mov eax, dword ptr [rbp + 0x270]
0092BA59  A9 00 07 00 00                  test eax, 0x700
0092BA5E  0F 84 DC 07 00 00               je 0x14092c240
0092BA64  48 8B 4D 18                     mov rcx, qword ptr [rbp + 0x18]
0092BA68  48 85 C9                        test rcx, rcx
0092BA6B  0F 85 94 09 00 00               jne 0x14092c405
0092BA71  48 8B FA                        mov rdi, rdx
0092BA74  8B DA                           mov ebx, edx
0092BA76  45 85 FF                        test r15d, r15d
0092BA79  0F 85 8A 05 00 00               jne 0x14092c009
0092BA7F  48 85 FF                        test rdi, rdi
0092BA82  0F 85 81 05 00 00               jne 0x14092c009
0092BA88  4C 8B 75 58                     mov r14, qword ptr [rbp + 0x58]
0092BA8C  8B FA                           mov edi, edx
0092BA8E  49 8B F6                        mov rsi, r14
0092BA91  89 55 C0                        mov dword ptr [rbp - 0x40], edx
0092BA94  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
0092BA98  48 8D 45 08                     lea rax, [rbp + 8]
0092BA9C  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
0092BAA0  4C 8B C9                        mov r9, rcx
0092BAA3  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0092BAA8  4C 8B C1                        mov r8, rcx
0092BAAB  48 8D 45 60                     lea rax, [rbp + 0x60]
0092BAAF  48 8B D6                        mov rdx, rsi
0092BAB2  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0092BAB7  48 8B 85 80 00 00 00            mov rax, qword ptr [rbp + 0x80]
0092BABE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0092BAC3  48 8B 45 78                     mov rax, qword ptr [rbp + 0x78]
0092BAC7  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
0092BACC  49 8B CF                        mov rcx, r15
0092BACF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0092BAD4  E8 97 12 00 00                  call 0x14092cd70
0092BAD9  8B D8                           mov ebx, eax
0092BADB  41 8B C5                        mov eax, r13d
0092BADE  25 00 20 00 00                  and eax, 0x2000
0092BAE3  C1 E0 11                        shl eax, 0x11
0092BAE6  09 45 08                        or dword ptr [rbp + 8], eax
0092BAE9  48 85 F6                        test rsi, rsi
0092BAEC  74 0F                           je 0x14092bafd
0092BAEE  49 3B F6                        cmp rsi, r14
0092BAF1  74 0A                           je 0x14092bafd
0092BAF3  33 D2                           xor edx, edx
0092BAF5  48 8B CE                        mov rcx, rsi
0092BAF8  E8 73 6D 25 00                  call 0x140b82870
0092BAFD  85 DB                           test ebx, ebx
0092BAFF  0F 88 48 11 00 00               js 0x14092cc4d
0092BB05  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
0092BB09  48 85 C0                        test rax, rax
0092BB0C  74 36                           je 0x14092bb44
0092BB0E  80 7D A0 00                     cmp byte ptr [rbp - 0x60], 0
0092BB12  0F 85 9D 0B 00 00               jne 0x14092c6b5
0092BB18  4C 8B F8                        mov r15, rax
0092BB1B  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
0092BB1F  33 C0                           xor eax, eax
0092BB21  C6 45 BA 01                     mov byte ptr [rbp - 0x46], 1
0092BB25  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
0092BB29  8B C7                           mov eax, edi
0092BB2B  83 E0 08                        and eax, 8
0092BB2E  81 E7 00 14 00 00               and edi, 0x1400
0092BB34  83 C8 04                        or eax, 4
0092BB37  03 C0                           add eax, eax
0092BB39  0B C7                           or eax, edi
0092BB3B  03 C0                           add eax, eax
0092BB3D  44 0B E8                        or r13d, eax
0092BB40  44 89 6D D8                     mov dword ptr [rbp - 0x28], r13d
0092BB44  44 8B 8D 70 02 00 00            mov r9d, dword ptr [rbp + 0x270]
0092BB4B  41 F6 C1 08                     test r9b, 8
0092BB4F  75 5D                           jne 0x14092bbae
0092BB51  45 33 C0                        xor r8d, r8d
0092BB54  49 8B CF                        mov rcx, r15
0092BB57  41 8D 50 11                     lea edx, [r8 + 0x11]
0092BB5B  E8 90 4F AE FF                  call 0x140410af0
0092BB60  48 85 C0                        test rax, rax
0092BB63  0F 84 11 0C 00 00               je 0x14092c77a
0092BB69  48 8D 50 08                     lea rdx, [rax + 8]
0092BB6D  48 85 D2                        test rdx, rdx
0092BB70  74 35                           je 0x14092bba7
0092BB72  4D 85 E4                        test r12, r12
0092BB75  0F 84 2E 10 00 00               je 0x14092cba9
0092BB7B  48 8B 4D 10                     mov rcx, qword ptr [rbp + 0x10]
0092BB7F  4C 8D 45 B7                     lea r8, [rbp - 0x49]
0092BB83  E8 C8 01 AD FF                  call 0x1403fbd50
0092BB88  8B D8                           mov ebx, eax
0092BB8A  85 C0                           test eax, eax
0092BB8C  0F 88 BB 10 00 00               js 0x14092cc4d
0092BB92  8B 45 2C                        mov eax, dword ptr [rbp + 0x2c]
0092BB95  B9 01 00 00 00                  mov ecx, 1
0092BB9A  80 7D B7 00                     cmp byte ptr [rbp - 0x49], 0
0092BB9E  0F B6 C0                        movzx eax, al
0092BBA1  0F 44 C1                        cmove eax, ecx
0092BBA4  89 45 2C                        mov dword ptr [rbp + 0x2c], eax
0092BBA7  44 8B 8D 70 02 00 00            mov r9d, dword ptr [rbp + 0x270]
0092BBAE  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
0092BBB2  41 8B F9                        mov edi, r9d
0092BBB5  C1 EF 02                        shr edi, 2
0092BBB8  45 8B F9                        mov r15d, r9d
0092BBBB  40 80 E7 01                     and dil, 1
0092BBBF  41 83 E7 01                     and r15d, 1
0092BBC3  45 33 DB                        xor r11d, r11d
0092BBC6  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
0092BBCA  A8 04                           test al, 4
0092BBCC  75 72                           jne 0x14092bc40
0092BBCE  45 8B EB                        mov r13d, r11d
0092BBD1  4C 8B 55 18                     mov r10, qword ptr [rbp + 0x18]
0092BBD5  4D 85 D2                        test r10, r10
0092BBD8  0F 85 FC 07 00 00               jne 0x14092c3da
0092BBDE  4D 8B F3                        mov r14, r11
0092BBE1  0F B7 72 02                     movzx esi, word ptr [rdx + 2]
0092BBE5  41 8B DB                        mov ebx, r11d
0092BBE8  81 E6 0C 14 00 00               and esi, 0x140c
0092BBEE  0F 85 1C 05 00 00               jne 0x14092c110
0092BBF4  4D 85 F6                        test r14, r14
0092BBF7  0F 85 13 05 00 00               jne 0x14092c110
0092BBFD  40 32 FF                        xor dil, dil
0092BC00  4C 89 5D 88                     mov qword ptr [rbp - 0x78], r11
0092BC04  4D 8B C3                        mov r8, r11
0092BC07  44 8B 6D D8                     mov r13d, dword ptr [rbp - 0x28]
0092BC0B  41 F6 C1 01                     test r9b, 1
0092BC0F  74 05                           je 0x14092bc16
0092BC11  41 0F BA ED 0A                  bts r13d, 0xa
0092BC16  0F B7 4A 02                     movzx ecx, word ptr [rdx + 2]
0092BC1A  0F B6 C1                        movzx eax, cl
0092BC1D  24 0C                           and al, 0xc
0092BC1F  3C 0C                           cmp al, 0xc
0092BC21  0F 84 DF 0A 00 00               je 0x14092c706
0092BC27  48 8B 45 68                     mov rax, qword ptr [rbp + 0x68]
0092BC2B  48 85 C0                        test rax, rax
0092BC2E  74 0B                           je 0x14092bc3b
0092BC30  4C 8B C0                        mov r8, rax
0092BC33  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
0092BC37  41 83 CD 04                     or r13d, 4
0092BC3B  45 32 FF                        xor r15b, r15b
0092BC3E  EB 45                           jmp 0x14092bc85
0092BC40  66 85 C0                        test ax, ax
0092BC43  0F 89 19 08 00 00               jns 0x14092c462
0092BC49  8B 42 10                        mov eax, dword ptr [rdx + 0x10]
0092BC4C  85 C0                           test eax, eax
0092BC4E  0F 84 31 09 00 00               je 0x14092c585
0092BC54  4C 8D 2C 02                     lea r13, [rdx + rax]
0092BC58  E9 74 FF FF FF                  jmp 0x14092bbd1
0092BC5D  8B 45 C0                        mov eax, dword ptr [rbp - 0x40]
0092BC60  41 B7 01                        mov r15b, 1
0092BC63  44 8B 6D D8                     mov r13d, dword ptr [rbp - 0x28]
0092BC67  25 08 14 00 00                  and eax, 0x1408
0092BC6C  0F B6 7D B4                     movzx edi, byte ptr [rbp - 0x4c]
0092BC70  83 C8 04                        or eax, 4
0092BC73  44 8B 8D 70 02 00 00            mov r9d, dword ptr [rbp + 0x270]
0092BC7A  44 0B E8                        or r13d, eax
0092BC7D  4C 8B 55 18                     mov r10, qword ptr [rbp + 0x18]
0092BC81  44 88 7D 80                     mov byte ptr [rbp - 0x80], r15b
0092BC85  4C 8B 75 F8                     mov r14, qword ptr [rbp - 8]
0092BC89  41 0F BA E1 0C                  bt r9d, 0xc
0092BC8E  72 14                           jb 0x14092bca4
0092BC90  80 7D B8 00                     cmp byte ptr [rbp - 0x48], 0
0092BC94  74 0E                           je 0x14092bca4
0092BC96  4D 85 F6                        test r14, r14
0092BC99  74 09                           je 0x14092bca4
0092BC9B  4D 85 D2                        test r10, r10
0092BC9E  0F 85 9A 06 00 00               jne 0x14092c33e
0092BCA4  0F B6 5D 82                     movzx ebx, byte ptr [rbp - 0x7e]
0092BCA8  41 F6 C1 01                     test r9b, 1
0092BCAC  0F 85 04 08 00 00               jne 0x14092c4b6
0092BCB2  8B 4D 08                        mov ecx, dword ptr [rbp + 8]
0092BCB5  81 E1 FF FD FF FF               and ecx, 0xfffffdff
0092BCBB  0F 84 32 03 00 00               je 0x14092bff3
0092BCC1  8B C1                           mov eax, ecx
0092BCC3  25 B0 01 00 00                  and eax, 0x1b0
0092BCC8  3B C1                           cmp eax, ecx
0092BCCA  0F 85 23 03 00 00               jne 0x14092bff3
0092BCD0  32 C0                           xor al, al
0092BCD2  80 FB 01                        cmp bl, 1
0092BCD5  75 30                           jne 0x14092bd07
0092BCD7  80 7D 81 00                     cmp byte ptr [rbp - 0x7f], 0
0092BCDB  0F 85 02 0D 00 00               jne 0x14092c9e3
0092BCE1  33 F6                           xor esi, esi
0092BCE3  44 8D 66 01                     lea r12d, [rsi + 1]
0092BCE7  80 7D 2C 00                     cmp byte ptr [rbp + 0x2c], 0
0092BCEB  0F 85 D9 0A 00 00               jne 0x14092c7ca
0092BCF1  80 7D B5 00                     cmp byte ptr [rbp - 0x4b], 0
0092BCF5  8B 5D D4                        mov ebx, dword ptr [rbp - 0x2c]
0092BCF8  0F 85 E4 07 00 00               jne 0x14092c4e2
0092BCFE  40 84 FF                        test dil, dil
0092BD01  0F 85 DD 05 00 00               jne 0x14092c2e4
0092BD07  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
0092BD0B  33 D2                           xor edx, edx
0092BD0D  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
0092BD11  0F B6 40 01                     movzx eax, byte ptr [rax + 1]
0092BD15  44 8D 24 85 08 00 00 00         lea r12d, [rax*4 + 8]
0092BD1D  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
0092BD21  48 85 C0                        test rax, rax
0092BD24  0F 84 88 0D 00 00               je 0x14092cab2
0092BD2A  0F B6 40 01                     movzx eax, byte ptr [rax + 1]
0092BD2E  44 8D 3C 85 08 00 00 00         lea r15d, [rax*4 + 8]
0092BD36  41 F6 C5 10                     test r13b, 0x10
0092BD3A  0F 84 36 02 00 00               je 0x14092bf76
0092BD40  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
0092BD44  48 85 C0                        test rax, rax
0092BD47  0F 84 29 02 00 00               je 0x14092bf76
0092BD4D  0F B7 70 02                     movzx esi, word ptr [rax + 2]
0092BD51  83 C6 03                        add esi, 3
0092BD54  83 E6 FC                        and esi, 0xfffffffc
0092BD57  41 F6 C5 04                     test r13b, 4
0092BD5B  0F 84 0B 05 00 00               je 0x14092c26c
0092BD61  48 85 C9                        test rcx, rcx
0092BD64  0F 84 02 05 00 00               je 0x14092c26c
0092BD6A  0F B7 79 02                     movzx edi, word ptr [rcx + 2]
0092BD6E  83 C7 03                        add edi, 3
0092BD71  83 E7 FC                        and edi, 0xfffffffc
0092BD74  8D 57 14                        lea edx, [rdi + 0x14]
0092BD77  B9 00 01 00 00                  mov ecx, 0x100
0092BD7C  03 D6                           add edx, esi
0092BD7E  41 B8 53 65 53 64               mov r8d, 0x64536553
0092BD84  41 03 D7                        add edx, r15d
0092BD87  41 03 D4                        add edx, r12d
0092BD8A  E8 61 63 25 00                  call 0x140b820f0
0092BD8F  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
0092BD93  4C 8B F0                        mov r14, rax
0092BD96  48 85 C0                        test rax, rax
0092BD99  0F 84 D4 04 00 00               je 0x14092c273
0092BD9F  33 C0                           xor eax, eax
0092BDA1  49 8D 5E 14                     lea rbx, [r14 + 0x14]
0092BDA5  0F 57 C0                        xorps xmm0, xmm0
0092BDA8  41 0F 11 06                     movups xmmword ptr [r14], xmm0
0092BDAC  41 89 46 10                     mov dword ptr [r14 + 0x10], eax
0092BDB0  66 45 09 6E 02                  or word ptr [r14 + 2], r13w
0092BDB5  41 C6 06 01                     mov byte ptr [r14], 1
0092BDB9  41 F6 C5 10                     test r13b, 0x10
0092BDBD  0F 84 1F 01 00 00               je 0x14092bee2
0092BDC3  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
0092BDC7  48 85 C0                        test rax, rax
0092BDCA  0F 84 12 01 00 00               je 0x14092bee2
0092BDD0  F7 85 70 02 00 00 00 40 00 00   test dword ptr [rbp + 0x270], 0x4000
0092BDDA  4C 8B F3                        mov r14, rbx
0092BDDD  48 89 9D 80 00 00 00            mov qword ptr [rbp + 0x80], rbx
0092BDE4  48 8B D0                        mov rdx, rax
0092BDE7  0F 85 A0 07 00 00               jne 0x14092c58d
0092BDED  44 0F B7 40 02                  movzx r8d, word ptr [rax + 2]
0092BDF2  48 8B CB                        mov rcx, rbx
0092BDF5  E8 46 AA D9 FF                  call 0x1406c6840
0092BDFA  45 33 C9                        xor r9d, r9d
0092BDFD  44 38 4D A0                     cmp byte ptr [rbp - 0x60], r9b
0092BE01  0F 85 9F 00 00 00               jne 0x14092bea6
0092BE07  48 85 DB                        test rbx, rbx
0092BE0A  0F 84 96 00 00 00               je 0x14092bea6
0092BE10  48 8D 53 08                     lea rdx, [rbx + 8]
0092BE14  45 8B C1                        mov r8d, r9d
0092BE17  66 44 3B 4B 04                  cmp r9w, word ptr [rbx + 4]
0092BE1C  0F 83 84 00 00 00               jae 0x14092bea6
0092BE22  4C 8B 75 00                     mov r14, qword ptr [rbp]
0092BE26  41 BA 73 06 00 00               mov r10d, 0x673
0092BE2C  0F B6 02                        movzx eax, byte ptr [rdx]
0092BE2F  3C 0A                           cmp al, 0xa
0092BE31  0F 87 FA 03 00 00               ja 0x14092c231
0092BE37  F6 42 01 08                     test byte ptr [rdx + 1], 8
0092BE3B  75 4F                           jne 0x14092be8c
0092BE3D  8B 4A 04                        mov ecx, dword ptr [rdx + 4]
0092BE40  85 C9                           test ecx, ecx
0092BE42  79 03                           jns 0x14092be47
0092BE44  41 0B 0E                        or ecx, dword ptr [r14]
0092BE47  0F BA E1 1E                     bt ecx, 0x1e
0092BE4B  73 04                           jae 0x14092be51
0092BE4D  41 0B 4E 04                     or ecx, dword ptr [r14 + 4]
0092BE51  0F BA E1 1D                     bt ecx, 0x1d
0092BE55  73 04                           jae 0x14092be5b
0092BE57  41 0B 4E 08                     or ecx, dword ptr [r14 + 8]
0092BE5B  0F BA E1 1C                     bt ecx, 0x1c
0092BE5F  73 04                           jae 0x14092be65
0092BE61  41 0B 4E 0C                     or ecx, dword ptr [r14 + 0xc]
0092BE65  81 E1 FF FF FF 0F               and ecx, 0xfffffff
0092BE6B  89 4A 04                        mov dword ptr [rdx + 4], ecx
0092BE6E  0F B6 02                        movzx eax, byte ptr [rdx]
0092BE71  3C 0A                           cmp al, 0xa
0092BE73  0F 87 F1 0D 00 00               ja 0x14092cc6a
0092BE79  41 0F A3 C2                     bt r10d, eax
0092BE7D  0F 83 E7 0D 00 00               jae 0x14092cc6a
0092BE83  41 8B 46 0C                     mov eax, dword ptr [r14 + 0xc]
0092BE87  23 C1                           and eax, ecx
0092BE89  89 42 04                        mov dword ptr [rdx + 4], eax
0092BE8C  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
0092BE90  41 FF C0                        inc r8d
0092BE93  48 03 D0                        add rdx, rax
0092BE96  0F B7 43 04                     movzx eax, word ptr [rbx + 4]
0092BE9A  44 3B C0                        cmp r8d, eax
0092BE9D  72 8D                           jb 0x14092be2c
0092BE9F  4C 8B B5 80 00 00 00            mov r14, qword ptr [rbp + 0x80]
0092BEA6  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
0092BEAA  0F B7 48 02                     movzx ecx, word ptr [rax + 2]
0092BEAE  3B F1                           cmp esi, ecx
0092BEB0  76 13                           jbe 0x14092bec5
0092BEB2  44 8B C6                        mov r8d, esi
0092BEB5  33 D2                           xor edx, edx
0092BEB7  44 2B C1                        sub r8d, ecx
0092BEBA  48 03 CB                        add rcx, rbx
0092BEBD  E8 7E AD D9 FF                  call 0x1406c6c40
0092BEC2  45 33 C9                        xor r9d, r9d
0092BEC5  4D 85 F6                        test r14, r14
0092BEC8  0F 84 F0 0C 00 00               je 0x14092cbbe
0092BECE  8B C6                           mov eax, esi
0092BED0  48 03 D8                        add rbx, rax
0092BED3  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
0092BED7  44 2B F0                        sub r14d, eax
0092BEDA  44 89 70 0C                     mov dword ptr [rax + 0xc], r14d
0092BEDE  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
0092BEE2  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0092BEE6  41 F6 C5 04                     test r13b, 4
0092BEEA  0F 84 68 05 00 00               je 0x14092c458
0092BEF0  48 85 F6                        test rsi, rsi
0092BEF3  0F 84 59 05 00 00               je 0x14092c452
0092BEF9  F7 85 70 02 00 00 00 40 00 00   test dword ptr [rbp + 0x270], 0x4000
0092BF03  48 8B D6                        mov rdx, rsi
0092BF06  0F 85 84 05 00 00               jne 0x14092c490
0092BF0C  44 0F B7 46 02                  movzx r8d, word ptr [rsi + 2]
0092BF11  48 8B CB                        mov rcx, rbx
0092BF14  E8 27 A9 D9 FF                  call 0x1406c6840
0092BF19  44 0F B6 6D 80                  movzx r13d, byte ptr [rbp - 0x80]
0092BF1E  45 84 ED                        test r13b, r13b
0092BF21  0F 85 79 F5 FF FF               jne 0x14092b4a0
0092BF27  48 85 DB                        test rbx, rbx
0092BF2A  0F 84 70 F5 FF FF               je 0x14092b4a0
0092BF30  33 C0                           xor eax, eax
0092BF32  48 8D 53 08                     lea rdx, [rbx + 8]
0092BF36  44 8B C0                        mov r8d, eax
0092BF39  66 3B 43 04                     cmp ax, word ptr [rbx + 4]
0092BF3D  0F 83 5D F5 FF FF               jae 0x14092b4a0
0092BF43  4C 8B 75 00                     mov r14, qword ptr [rbp]
0092BF47  41 BD 73 06 00 00               mov r13d, 0x673
0092BF4D  0F B6 02                        movzx eax, byte ptr [rdx]
0092BF50  3C 0A                           cmp al, 0xa
0092BF52  0F 87 A2 00 00 00               ja 0x14092bffa
0092BF58  F6 42 01 08                     test byte ptr [rdx + 1], 8
0092BF5C  74 41                           je 0x14092bf9f
0092BF5E  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
0092BF62  41 FF C0                        inc r8d
0092BF65  48 03 D0                        add rdx, rax
0092BF68  0F B7 43 04                     movzx eax, word ptr [rbx + 4]
0092BF6C  44 3B C0                        cmp r8d, eax
0092BF6F  72 DC                           jb 0x14092bf4d
0092BF71  E9 21 F5 FF FF                  jmp 0x14092b497
0092BF76  8B F2                           mov esi, edx
0092BF78  E9 DA FD FF FF                  jmp 0x14092bd57
0092BF7D  48 8D 8D 00 01 00 00            lea rcx, [rbp + 0x100]
0092BF84  49 03 CA                        add rcx, r10
0092BF87  48 3B D1                        cmp rdx, rcx
0092BF8A  0F 83 9C 0C 00 00               jae 0x14092cc2c
0092BF90  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
0092BF94  41 FF C0                        inc r8d
0092BF97  48 03 D0                        add rdx, rax
0092BF9A  E9 2D FA FF FF                  jmp 0x14092b9cc
0092BF9F  8B 4A 04                        mov ecx, dword ptr [rdx + 4]
0092BFA2  85 C9                           test ecx, ecx
0092BFA4  79 03                           jns 0x14092bfa9
0092BFA6  41 0B 0E                        or ecx, dword ptr [r14]
0092BFA9  0F BA E1 1E                     bt ecx, 0x1e
0092BFAD  73 04                           jae 0x14092bfb3
0092BFAF  41 0B 4E 04                     or ecx, dword ptr [r14 + 4]
0092BFB3  0F BA E1 1D                     bt ecx, 0x1d
0092BFB7  73 04                           jae 0x14092bfbd
0092BFB9  41 0B 4E 08                     or ecx, dword ptr [r14 + 8]
0092BFBD  0F BA E1 1C                     bt ecx, 0x1c
0092BFC1  73 04                           jae 0x14092bfc7
0092BFC3  41 0B 4E 0C                     or ecx, dword ptr [r14 + 0xc]
0092BFC7  81 E1 FF FF FF 0F               and ecx, 0xfffffff
0092BFCD  89 4A 04                        mov dword ptr [rdx + 4], ecx
0092BFD0  0F B6 02                        movzx eax, byte ptr [rdx]
0092BFD3  3C 0A                           cmp al, 0xa
0092BFD5  0F 87 82 0C 00 00               ja 0x14092cc5d
0092BFDB  41 0F A3 C5                     bt r13d, eax
0092BFDF  0F 83 78 0C 00 00               jae 0x14092cc5d
0092BFE5  41 8B 46 0C                     mov eax, dword ptr [r14 + 0xc]
0092BFE9  23 C1                           and eax, ecx
0092BFEB  89 42 04                        mov dword ptr [rdx + 4], eax
0092BFEE  E9 6B FF FF FF                  jmp 0x14092bf5e
0092BFF3  B0 01                           mov al, 1
0092BFF5  E9 D8 FC FF FF                  jmp 0x14092bcd2
0092BFFA  2C 0D                           sub al, 0xd
0092BFFC  3C 01                           cmp al, 1
0092BFFE  0F 87 5A FF FF FF               ja 0x14092bf5e
0092C004  E9 4F FF FF FF                  jmp 0x14092bf58
0092C009  B8 C8 00 00 00                  mov eax, 0xc8
0092C00E  44 8B F2                        mov r14d, edx
0092C011  89 45 9C                        mov dword ptr [rbp - 0x64], eax
0092C014  48 8B F2                        mov rsi, rdx
0092C017  41 83 FE 02                     cmp r14d, 2
0092C01B  0F 83 CF 00 00 00               jae 0x14092c0f0
0092C021  8B D0                           mov edx, eax
0092C023  B9 00 01 00 00                  mov ecx, 0x100
0092C028  41 B8 53 65 41 63               mov r8d, 0x63416553
0092C02E  E8 BD 60 25 00                  call 0x140b820f0
0092C033  48 8B F0                        mov rsi, rax
0092C036  48 85 C0                        test rax, rax
0092C039  0F 84 09 F8 FF FF               je 0x14092b848
0092C03F  44 0F B6 8D 68 02 00 00         movzx r9d, byte ptr [rbp + 0x268]
0092C047  48 8D 45 C0                     lea rax, [rbp - 0x40]
0092C04B  48 8B 55 58                     mov rdx, qword ptr [rbp + 0x58]
0092C04F  45 8B C7                        mov r8d, r15d
0092C052  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
0092C05A  48 8B CF                        mov rcx, rdi
0092C05D  48 8D 45 D1                     lea rax, [rbp - 0x2f]
0092C061  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0092C069  48 8D 45 9C                     lea rax, [rbp - 0x64]
0092C06D  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
0092C072  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0092C077  8B 85 60 02 00 00               mov eax, dword ptr [rbp + 0x260]
0092C07D  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
0092C081  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0092C085  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0092C08A  48 8B 45 00                     mov rax, qword ptr [rbp]
0092C08E  C7 44 24 58 03 00 00 00         mov dword ptr [rsp + 0x58], 3
0092C096  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0092C09B  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
0092C09F  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0092C0A4  48 8B 45 20                     mov rax, qword ptr [rbp + 0x20]
0092C0A8  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0092C0AD  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
0092C0B1  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0092C0B6  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
0092C0BA  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0092C0BF  C6 44 24 28 00                  mov byte ptr [rsp + 0x28], 0
0092C0C4  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
0092C0C9  E8 02 14 00 00                  call 0x14092d4d0
0092C0CE  8B D8                           mov ebx, eax
0092C0D0  85 C0                           test eax, eax
0092C0D2  0F 88 BF 01 00 00               js 0x14092c297
0092C0D8  83 7D 9C 00                     cmp dword ptr [rbp - 0x64], 0
0092C0DC  0F 85 11 05 00 00               jne 0x14092c5f3
0092C0E2  33 D2                           xor edx, edx
0092C0E4  48 8B CE                        mov rcx, rsi
0092C0E7  E8 84 67 25 00                  call 0x140b82870
0092C0EC  33 D2                           xor edx, edx
0092C0EE  8B F2                           mov esi, edx
0092C0F0  81 FB 0B 00 00 80               cmp ebx, 0x8000000b
0092C0F6  0F 84 8C F9 FF FF               je 0x14092ba88
0092C0FC  85 DB                           test ebx, ebx
0092C0FE  0F 88 49 F7 FF FF               js 0x14092b84d
0092C104  8B 7D C0                        mov edi, dword ptr [rbp - 0x40]
0092C107  4C 8B 75 58                     mov r14, qword ptr [rbp + 0x58]
0092C10B  E9 84 F9 FF FF                  jmp 0x14092ba94
0092C110  B8 C8 00 00 00                  mov eax, 0xc8
0092C115  45 8B E3                        mov r12d, r11d
0092C118  89 45 9C                        mov dword ptr [rbp - 0x64], eax
0092C11B  4D 8B C3                        mov r8, r11
0092C11E  41 83 FC 02                     cmp r12d, 2
0092C122  0F 83 D5 00 00 00               jae 0x14092c1fd
0092C128  8B D0                           mov edx, eax
0092C12A  B9 00 01 00 00                  mov ecx, 0x100
0092C12F  41 B8 53 65 41 63               mov r8d, 0x63416553
0092C135  E8 B6 5F 25 00                  call 0x140b820f0
0092C13A  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
0092C13E  4C 8B C0                        mov r8, rax
0092C141  48 85 C0                        test rax, rax
0092C144  0F 84 2D 0B 00 00               je 0x14092cc77
0092C14A  44 0F B6 8D 68 02 00 00         movzx r9d, byte ptr [rbp + 0x268]
0092C152  48 8D 45 C0                     lea rax, [rbp - 0x40]
0092C156  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
0092C15E  49 8B D5                        mov rdx, r13
0092C161  48 8D 45 B4                     lea rax, [rbp - 0x4c]
0092C165  49 8B CE                        mov rcx, r14
0092C168  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
0092C170  48 8D 45 9C                     lea rax, [rbp - 0x64]
0092C174  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
0092C179  44 8B C6                        mov r8d, esi
0092C17C  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0092C181  8B 85 60 02 00 00               mov eax, dword ptr [rbp + 0x260]
0092C187  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
0092C18B  48 8B 45 48                     mov rax, qword ptr [rbp + 0x48]
0092C18F  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0092C194  48 8B 45 00                     mov rax, qword ptr [rbp]
0092C198  C7 44 24 58 01 00 00 00         mov dword ptr [rsp + 0x58], 1
0092C1A0  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0092C1A5  48 8B 45 40                     mov rax, qword ptr [rbp + 0x40]
0092C1A9  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0092C1AE  48 8B 45 20                     mov rax, qword ptr [rbp + 0x20]
0092C1B2  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0092C1B7  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
0092C1BB  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0092C1C0  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
0092C1C4  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0092C1C9  40 88 7C 24 28                  mov byte ptr [rsp + 0x28], dil
0092C1CE  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
0092C1D3  E8 F8 12 00 00                  call 0x14092d4d0
0092C1D8  8B D8                           mov ebx, eax
0092C1DA  85 C0                           test eax, eax
0092C1DC  0F 88 DA 00 00 00               js 0x14092c2bc
0092C1E2  83 7D 9C 00                     cmp dword ptr [rbp - 0x64], 0
0092C1E6  0F 85 0E 04 00 00               jne 0x14092c5fa
0092C1EC  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
0092C1F0  33 D2                           xor edx, edx
0092C1F2  E8 79 66 25 00                  call 0x140b82870
0092C1F7  45 33 DB                        xor r11d, r11d
0092C1FA  45 8B C3                        mov r8d, r11d
0092C1FD  4C 89 45 88                     mov qword ptr [rbp - 0x78], r8
0092C201  85 DB                           test ebx, ebx
0092C203  0F 89 54 FA FF FF               jns 0x14092bc5d
0092C209  4C 89 45 88                     mov qword ptr [rbp - 0x78], r8
0092C20D  81 FB 0B 00 00 80               cmp ebx, 0x8000000b
0092C213  0F 85 07 03 00 00               jne 0x14092c520
0092C219  0F B6 7D B4                     movzx edi, byte ptr [rbp - 0x4c]
0092C21D  48 8B 55 E0                     mov rdx, qword ptr [rbp - 0x20]
0092C221  44 8B 8D 70 02 00 00            mov r9d, dword ptr [rbp + 0x270]
0092C228  4C 8B 55 18                     mov r10, qword ptr [rbp + 0x18]
0092C22C  E9 D6 F9 FF FF                  jmp 0x14092bc07
0092C231  2C 0D                           sub al, 0xd
0092C233  3C 01                           cmp al, 1
0092C235  0F 87 51 FC FF FF               ja 0x14092be8c
0092C23B  E9 F7 FB FF FF                  jmp 0x14092be37
0092C240  4D 85 F6                        test r14, r14
0092C243  75 09                           jne 0x14092c24e
0092C245  48 85 C9                        test rcx, rcx
0092C248  0F 85 E8 00 00 00               jne 0x14092c336
0092C24E  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
0092C252  44 8B F8                        mov r15d, eax
0092C255  25 00 28 00 00                  and eax, 0x2800
0092C25A  41 D1 EF                        shr r15d, 1
0092C25D  41 83 E7 18                     and r15d, 0x18
0092C261  44 0B F8                        or r15d, eax
0092C264  41 D1 EF                        shr r15d, 1
0092C267  E9 F8 F7 FF FF                  jmp 0x14092ba64
0092C26C  8B FA                           mov edi, edx
0092C26E  E9 01 FB FF FF                  jmp 0x14092bd74
0092C273  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0092C277  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0092C27C  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
0092C280  44 0F B6 6D 80                  movzx r13d, byte ptr [rbp - 0x80]
0092C285  E9 80 F2 FF FF                  jmp 0x14092b50a
0092C28A  33 D2                           xor edx, edx
0092C28C  8B CA                           mov ecx, edx
0092C28E  48 89 55 58                     mov qword ptr [rbp + 0x58], rdx
0092C292  E9 BC F7 FF FF                  jmp 0x14092ba53
0092C297  33 D2                           xor edx, edx
0092C299  48 8B CE                        mov rcx, rsi
0092C29C  E8 CF 65 25 00                  call 0x140b82870
0092C2A1  33 D2                           xor edx, edx
0092C2A3  8B F2                           mov esi, edx
0092C2A5  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
0092C2AB  0F 85 3F FE FF FF               jne 0x14092c0f0
0092C2B1  8B 45 9C                        mov eax, dword ptr [rbp - 0x64]
0092C2B4  41 FF C6                        inc r14d
0092C2B7  E9 58 FD FF FF                  jmp 0x14092c014
0092C2BC  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
0092C2C0  33 D2                           xor edx, edx
0092C2C2  E8 A9 65 25 00                  call 0x140b82870
0092C2C7  45 33 DB                        xor r11d, r11d
0092C2CA  45 8B C3                        mov r8d, r11d
0092C2CD  81 FB 23 00 00 C0               cmp ebx, 0xc0000023
0092C2D3  0F 85 24 FF FF FF               jne 0x14092c1fd
0092C2D9  8B 45 9C                        mov eax, dword ptr [rbp - 0x64]
0092C2DC  41 FF C4                        inc r12d
0092C2DF  E9 37 FE FF FF                  jmp 0x14092c11b
0092C2E4  84 DB                           test bl, bl
0092C2E6  0F 84 1B FA FF FF               je 0x14092bd07
0092C2EC  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0092C2F0  48 8D 45 B9                     lea rax, [rbp - 0x47]
0092C2F4  4C 8B 45 20                     mov r8, qword ptr [rbp + 0x20]
0092C2F8  4C 8D 4D 70                     lea r9, [rbp + 0x70]
0092C2FC  0F B6 95 88 00 00 00            movzx edx, byte ptr [rbp + 0x88]
0092C303  48 8B CE                        mov rcx, rsi
0092C306  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0092C30B  E8 48 0C F9 FF                  call 0x1408bcf58
0092C310  8B D8                           mov ebx, eax
0092C312  85 C0                           test eax, eax
0092C314  0F 88 14 0A 00 00               js 0x14092cd2e
0092C31A  45 84 FF                        test r15b, r15b
0092C31D  0F 85 10 02 00 00               jne 0x14092c533
0092C323  48 8B 4D 70                     mov rcx, qword ptr [rbp + 0x70]
0092C327  33 D2                           xor edx, edx
0092C329  48 89 4D 88                     mov qword ptr [rbp - 0x78], rcx
0092C32D  48 89 55 70                     mov qword ptr [rbp + 0x70], rdx
0092C331  E9 D7 F9 FF FF                  jmp 0x14092bd0d
0092C336  44 8B FA                        mov r15d, edx
0092C339  E9 26 F7 FF FF                  jmp 0x14092ba64
0092C33E  48 8B 8D 98 00 00 00            mov rcx, qword ptr [rbp + 0x98]
0092C345  4C 8D 45 38                     lea r8, [rbp + 0x38]
0092C349  48 8B 75 00                     mov rsi, qword ptr [rbp]
0092C34D  41 8B C1                        mov eax, r9d
0092C350  4C 8B 4D 48                     mov r9, qword ptr [rbp + 0x48]
0092C354  83 C8 01                        or eax, 1
0092C357  4C 89 5C 24 50                  mov qword ptr [rsp + 0x50], r11
0092C35C  33 D2                           xor edx, edx
0092C35E  48 89 4C 24 48                  mov qword ptr [rsp + 0x48], rcx
0092C363  49 8B CA                        mov rcx, r10
0092C366  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
0092C36B  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
0092C370  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0092C374  0F B6 85 68 02 00 00            movzx eax, byte ptr [rbp + 0x268]
0092C37B  88 44 24 28                     mov byte ptr [rsp + 0x28], al
0092C37F  8B 85 60 02 00 00               mov eax, dword ptr [rbp + 0x260]
0092C385  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0092C389  44 89 5D 9C                     mov dword ptr [rbp - 0x64], r11d
0092C38D  44 89 5D 28                     mov dword ptr [rbp + 0x28], r11d
0092C391  E8 BA E7 FF FF                  call 0x14092ab50
0092C396  8B D8                           mov ebx, eax
0092C398  85 C0                           test eax, eax
0092C39A  0F 88 6D 01 00 00               js 0x14092c50d
0092C3A0  48 8B 45 38                     mov rax, qword ptr [rbp + 0x38]
0092C3A4  0F B7 48 02                     movzx ecx, word ptr [rax + 2]
0092C3A8  F6 C1 04                        test cl, 4
0092C3AB  0F 85 BA 00 00 00               jne 0x14092c46b
0092C3B1  45 33 E4                        xor r12d, r12d
0092C3B4  41 8B D4                        mov edx, r12d
0092C3B7  B1 10                           mov cl, 0x10
0092C3B9  E8 32 EF AC FF                  call 0x1403fb2f0
0092C3BE  0F B6 5D 82                     movzx ebx, byte ptr [rbp - 0x7e]
0092C3C2  84 C0                           test al, al
0092C3C4  0F 85 96 02 00 00               jne 0x14092c660
0092C3CA  4C 8B 45 88                     mov r8, qword ptr [rbp - 0x78]
0092C3CE  44 8B 8D 70 02 00 00            mov r9d, dword ptr [rbp + 0x270]
0092C3D5  E9 CE F8 FF FF                  jmp 0x14092bca8
0092C3DA  41 0F B7 42 02                  movzx eax, word ptr [r10 + 2]
0092C3DF  A8 04                           test al, 4
0092C3E1  0F 84 F7 F7 FF FF               je 0x14092bbde
0092C3E7  66 85 C0                        test ax, ax
0092C3EA  0F 89 DE 06 00 00               jns 0x14092cace
0092C3F0  41 8B 42 10                     mov eax, dword ptr [r10 + 0x10]
0092C3F4  85 C0                           test eax, eax
0092C3F6  0F 84 E2 F7 FF FF               je 0x14092bbde
0092C3FC  4D 8D 34 02                     lea r14, [r10 + rax]
0092C400  E9 DC F7 FF FF                  jmp 0x14092bbe1
0092C405  0F B7 41 02                     movzx eax, word ptr [rcx + 2]
0092C409  A8 10                           test al, 0x10
0092C40B  0F 84 60 F6 FF FF               je 0x14092ba71
0092C411  66 85 C0                        test ax, ax
0092C414  0F 89 92 02 00 00               jns 0x14092c6ac
0092C41A  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
0092C41D  85 C0                           test eax, eax
0092C41F  0F 84 4C F6 FF FF               je 0x14092ba71
0092C425  48 8D 3C 01                     lea rdi, [rcx + rax]
0092C429  E9 46 F6 FF FF                  jmp 0x14092ba74
0092C42E  4D 85 E4                        test r12, r12
0092C431  74 16                           je 0x14092c449
0092C433  33 D2                           xor edx, edx
0092C435  49 8B CC                        mov rcx, r12
0092C438  E8 D3 A8 B2 FF                  call 0x140456d10
0092C43D  81 38 00 20 00 00               cmp dword ptr [rax], 0x2000
0092C443  0F 82 C1 08 00 00               jb 0x14092cd0a
0092C449  4C 8B 65 F8                     mov r12, qword ptr [rbp - 8]
0092C44D  E9 AB F4 FF FF                  jmp 0x14092b8fd
0092C452  33 C0                           xor eax, eax
0092C454  41 89 46 10                     mov dword ptr [r14 + 0x10], eax
0092C458  44 0F B6 6D 80                  movzx r13d, byte ptr [rbp - 0x80]
0092C45D  E9 64 F0 FF FF                  jmp 0x14092b4c6
0092C462  4C 8B 6A 20                     mov r13, qword ptr [rdx + 0x20]
0092C466  E9 66 F7 FF FF                  jmp 0x14092bbd1
0092C46B  48 8B 45 38                     mov rax, qword ptr [rbp + 0x38]
0092C46F  66 85 C9                        test cx, cx
0092C472  0F 89 F2 05 00 00               jns 0x14092ca6a
0092C478  8B 48 10                        mov ecx, dword ptr [rax + 0x10]
0092C47B  85 C9                           test ecx, ecx
0092C47D  0F 84 50 07 00 00               je 0x14092cbd3
0092C483  8B D1                           mov edx, ecx
0092C485  48 03 D0                        add rdx, rax
0092C488  45 33 E4                        xor r12d, r12d
0092C48B  E9 27 FF FF FF                  jmp 0x14092c3b7
0092C490  44 0F B6 6D 80                  movzx r13d, byte ptr [rbp - 0x80]
0092C495  B9 00 00 00 00                  mov ecx, 0
0092C49A  4C 8B 45 00                     mov r8, qword ptr [rbp]
0092C49E  45 84 ED                        test r13b, r13b
0092C4A1  4C 0F 45 C1                     cmovne r8, rcx
0092C4A5  48 8B CB                        mov rcx, rbx
0092C4A8  E8 A3 04 F9 FF                  call 0x1408bc950
0092C4AD  0F B7 7B 02                     movzx edi, word ptr [rbx + 2]
0092C4B1  E9 02 F0 FF FF                  jmp 0x14092b4b8
0092C4B6  4D 85 C0                        test r8, r8
0092C4B9  0F 85 F3 F7 FF FF               jne 0x14092bcb2
0092C4BF  41 0F BA ED 0C                  bts r13d, 0xc
0092C4C4  E9 E9 F7 FF FF                  jmp 0x14092bcb2
0092C4C9  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
0092C4CD  BB 78 00 00 C0                  mov ebx, 0xc0000078
0092C4D2  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0092C4D6  45 32 ED                        xor r13b, r13b
0092C4D9  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
0092C4DD  E9 28 F0 FF FF                  jmp 0x14092b50a
0092C4E2  8B 85 70 02 00 00               mov eax, dword ptr [rbp + 0x270]
0092C4E8  A8 10                           test al, 0x10
0092C4EA  0F 85 0E F8 FF FF               jne 0x14092bcfe
0092C4F0  48 8B 55 E8                     mov rdx, qword ptr [rbp - 0x18]
0092C4F4  44 0F B6 C3                     movzx r8d, bl
0092C4F8  49 8B CE                        mov rcx, r14
0092C4FB  E8 68 B0 10 00                  call 0x140a37568
0092C500  84 C0                           test al, al
0092C502  0F 85 F6 F7 FF FF               jne 0x14092bcfe
0092C508  BB 5A 00 00 C0                  mov ebx, 0xc000005a
0092C50D  44 0F B6 6D 80                  movzx r13d, byte ptr [rbp - 0x80]
0092C512  E9 7A F1 FF FF                  jmp 0x14092b691
0092C517  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
0092C51B  E9 E4 EC FF FF                  jmp 0x14092b204
0092C520  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
0092C524  49 8B F0                        mov rsi, r8
0092C527  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
0092C52B  45 32 ED                        xor r13b, r13b
0092C52E  E9 D7 EF FF FF                  jmp 0x14092b50a
0092C533  48 85 F6                        test rsi, rsi
0092C536  0F 84 E7 FD FF FF               je 0x14092c323
0092C53C  33 D2                           xor edx, edx
0092C53E  48 8B CE                        mov rcx, rsi
0092C541  E8 2A 63 25 00                  call 0x140b82870
0092C546  E9 D8 FD FF FF                  jmp 0x14092c323
0092C54B  48 85 F6                        test rsi, rsi
0092C54E  0F 85 01 04 00 00               jne 0x14092c955
0092C554  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0092C558  BB 5B 00 00 C0                  mov ebx, 0xc000005b
0092C55D  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
0092C561  4C 8B FE                        mov r15, rsi
0092C564  45 32 ED                        xor r13b, r13b
0092C567  E9 9E EF FF FF                  jmp 0x14092b50a
0092C56C  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
0092C570  BB 99 00 00 C0                  mov ebx, 0xc0000099
0092C575  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0092C579  45 32 ED                        xor r13b, r13b
0092C57C  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
0092C580  E9 85 EF FF FF                  jmp 0x14092b50a
0092C585  4D 8B EB                        mov r13, r11
0092C588  E9 44 F6 FF FF                  jmp 0x14092bbd1
0092C58D  80 7D A0 00                     cmp byte ptr [rbp - 0x60], 0
0092C591  B9 00 00 00 00                  mov ecx, 0
0092C596  4C 8B 45 00                     mov r8, qword ptr [rbp]
0092C59A  4C 0F 45 C1                     cmovne r8, rcx
0092C59E  48 8B CB                        mov rcx, rbx
0092C5A1  E8 AA 03 F9 FF                  call 0x1408bc950
0092C5A6  45 33 C9                        xor r9d, r9d
0092C5A9  66 44 39 4B 04                  cmp word ptr [rbx + 4], r9w
0092C5AE  0F 84 06 05 00 00               je 0x14092caba
0092C5B4  0F B7 73 02                     movzx esi, word ptr [rbx + 2]
0092C5B8  E9 08 F9 FF FF                  jmp 0x14092bec5
0092C5BD  88 4D 98                        mov byte ptr [rbp - 0x68], cl
0092C5C0  33 D2                           xor edx, edx
0092C5C2  49 8B CC                        mov rcx, r12
0092C5C5  48 89 75 30                     mov qword ptr [rbp + 0x30], rsi
0092C5C9  E8 42 A7 B2 FF                  call 0x140456d10
0092C5CE  81 38 00 20 00 00               cmp dword ptr [rax], 0x2000
0092C5D4  0F 83 FD F2 FF FF               jae 0x14092b8d7
0092C5DA  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
0092C5DE  BB 46 04 00 C0                  mov ebx, 0xc0000446
0092C5E3  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0092C5E7  45 32 ED                        xor r13b, r13b
0092C5EA  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
0092C5EE  E9 17 EF FF FF                  jmp 0x14092b50a
0092C5F3  33 D2                           xor edx, edx
0092C5F5  E9 F6 FA FF FF                  jmp 0x14092c0f0
0092C5FA  4C 8B 45 88                     mov r8, qword ptr [rbp - 0x78]
0092C5FE  45 33 DB                        xor r11d, r11d
0092C601  E9 F7 FB FF FF                  jmp 0x14092c1fd
0092C606  48 8B 4D 70                     mov rcx, qword ptr [rbp + 0x70]
0092C60A  48 85 C9                        test rcx, rcx
0092C60D  0F 84 11 EF FF FF               je 0x14092b524
0092C613  33 D2                           xor edx, edx
0092C615  E8 56 62 25 00                  call 0x140b82870
0092C61A  E9 05 EF FF FF                  jmp 0x14092b524
0092C61F  48 85 F6                        test rsi, rsi
0092C622  0F 84 97 06 00 00               je 0x14092ccbf
0092C628  66 83 7E 02 00                  cmp word ptr [rsi + 2], 0
0092C62D  0F 8C CD 04 00 00               jl 0x14092cb00
0092C633  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0092C637  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
0092C63B  C6 45 B5 01                     mov byte ptr [rbp - 0x4b], 1
0092C63F  48 85 C0                        test rax, rax
0092C642  0F 85 8F E9 FF FF               jne 0x14092afd7
0092C648  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0092C64C  BB 5A 00 00 C0                  mov ebx, 0xc000005a
0092C651  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
0092C655  4C 8B FE                        mov r15, rsi
0092C658  45 32 ED                        xor r13b, r13b
0092C65B  E9 AA EE FF FF                  jmp 0x14092b50a
0092C660  48 8B 4D 38                     mov rcx, qword ptr [rbp + 0x38]
0092C664  48 8D 45 28                     lea rax, [rbp + 0x28]
0092C668  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0092C66D  41 B9 00 00 04 00               mov r9d, 0x40000
0092C673  48 8D 45 9C                     lea rax, [rbp - 0x64]
0092C677  45 33 C0                        xor r8d, r8d
0092C67A  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0092C67F  49 8B D6                        mov rdx, r14
0092C682  88 5C 24 38                     mov byte ptr [rsp + 0x38], bl
0092C686  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
0092C68B  4C 89 64 24 28                  mov qword ptr [rsp + 0x28], r12
0092C690  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
0092C695  E8 26 A5 A7 FF                  call 0x1403a6bc0
0092C69A  84 C0                           test al, al
0092C69C  0F 85 28 FD FF FF               jne 0x14092c3ca
0092C6A2  BB 22 00 00 C0                  mov ebx, 0xc0000022
0092C6A7  E9 61 FE FF FF                  jmp 0x14092c50d
0092C6AC  48 8B 79 18                     mov rdi, qword ptr [rcx + 0x18]
0092C6B0  E9 BF F3 FF FF                  jmp 0x14092ba74
0092C6B5  4D 85 FF                        test r15, r15
0092C6B8  0F 84 5A F4 FF FF               je 0x14092bb18
0092C6BE  33 D2                           xor edx, edx
0092C6C0  49 8B CF                        mov rcx, r15
0092C6C3  E8 A8 61 25 00                  call 0x140b82870
0092C6C8  48 8B 45 60                     mov rax, qword ptr [rbp + 0x60]
0092C6CC  E9 47 F4 FF FF                  jmp 0x14092bb18
0092C6D1  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
0092C6D5  BB 7C 00 00 C0                  mov ebx, 0xc000007c
0092C6DA  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0092C6DE  45 32 ED                        xor r13b, r13b
0092C6E1  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
0092C6E5  E9 20 EE FF FF                  jmp 0x14092b50a
0092C6EA  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
0092C6EE  48 85 C0                        test rax, rax
0092C6F1  0F 84 53 EE FF FF               je 0x14092b54a
0092C6F7  33 D2                           xor edx, edx
0092C6F9  48 8B C8                        mov rcx, rax
0092C6FC  E8 6F 61 25 00                  call 0x140b82870
0092C701  E9 44 EE FF FF                  jmp 0x14092b54a
0092C706  F6 C1 04                        test cl, 4
0092C709  0F 85 89 00 00 00               jne 0x14092c798
0092C70F  4D 8B C3                        mov r8, r11
0092C712  81 E1 00 10 00 00               and ecx, 0x1000
0092C718  4C 89 45 88                     mov qword ptr [rbp - 0x78], r8
0092C71C  83 C9 04                        or ecx, 4
0092C71F  40 B7 01                        mov dil, 1
0092C722  44 0B E9                        or r13d, ecx
0092C725  45 32 FF                        xor r15b, r15b
0092C728  E9 58 F5 FF FF                  jmp 0x14092bc85
0092C72D  41 F6 C5 10                     test r13b, 0x10
0092C731  0F 85 3D 02 00 00               jne 0x14092c974
0092C737  4C 89 75 90                     mov qword ptr [rbp - 0x70], r14
0092C73B  41 81 E5 00 20 00 00            and r13d, 0x2000
0092C742  C6 45 81 01                     mov byte ptr [rbp - 0x7f], 1
0092C746  44 0B E9                        or r13d, ecx
0092C749  41 83 CD 10                     or r13d, 0x10
0092C74D  44 89 6D D8                     mov dword ptr [rbp - 0x28], r13d
0092C751  E9 B7 E9 FF FF                  jmp 0x14092b10d
0092C756  F6 C1 10                        test cl, 0x10
0092C759  0F 85 37 02 00 00               jne 0x14092c996
0092C75F  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
0092C763  E9 90 EA FF FF                  jmp 0x14092b1f8
0092C768  4D 8B 7B 18                     mov r15, qword ptr [r11 + 0x18]
0092C76C  E9 F8 E8 FF FF                  jmp 0x14092b069
0092C771  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
0092C775  E9 BF EF FF FF                  jmp 0x14092b739
0092C77A  48 8B 55 30                     mov rdx, qword ptr [rbp + 0x30]
0092C77E  E9 EA F3 FF FF                  jmp 0x14092bb6d
0092C783  4C 8B 3D 26 B6 53 00            mov r15, qword ptr [rip + 0x53b626]
0092C78A  E9 FD E5 FF FF                  jmp 0x14092ad8c
0092C78F  49 8B 4B 18                     mov rcx, qword ptr [r11 + 0x18]
0092C793  E9 7C EA FF FF                  jmp 0x14092b214
0092C798  66 85 C9                        test cx, cx
0092C79B  0F 89 29 04 00 00               jns 0x14092cbca
0092C7A1  8B 42 10                        mov eax, dword ptr [rdx + 0x10]
0092C7A4  85 C0                           test eax, eax
0092C7A6  0F 85 E9 02 00 00               jne 0x14092ca95
0092C7AC  4D 8B C3                        mov r8, r11
0092C7AF  E9 5E FF FF FF                  jmp 0x14092c712
0092C7B4  80 7D BC 00                     cmp byte ptr [rbp - 0x44], 0
0092C7B8  0F 84 99 ED FF FF               je 0x14092b557
0092C7BE  33 D2                           xor edx, edx
0092C7C0  E8 AB 60 25 00                  call 0x140b82870
0092C7C5  E9 8D ED FF FF                  jmp 0x14092b557
0092C7CA  41 F6 C1 08                     test r9b, 8
0092C7CE  0F 85 1D F5 FF FF               jne 0x14092bcf1
0092C7D4  4D 85 F6                        test r14, r14
0092C7D7  0F 84 B2 04 00 00               je 0x14092cc8f
0092C7DD  48 8B 05 44 D3 6A 00            mov rax, qword ptr [rip + 0x6ad344]
0092C7E4  48 8D 8D E0 00 00 00            lea rcx, [rbp + 0xe0]
0092C7EB  41 B0 01                        mov r8b, 1
0092C7EE  48 89 85 E8 00 00 00            mov qword ptr [rbp + 0xe8], rax
0092C7F5  49 8B D6                        mov rdx, r14
0092C7F8  44 89 A5 E0 00 00 00            mov dword ptr [rbp + 0xe0], r12d
0092C7FF  44 89 A5 E4 00 00 00            mov dword ptr [rbp + 0xe4], r12d
0092C806  89 B5 F0 00 00 00               mov dword ptr [rbp + 0xf0], esi
0092C80C  E8 5F E6 08 00                  call 0x1409bae70
0092C811  44 0F B6 C8                     movzx r9d, al
0092C815  4C 8D 85 E0 00 00 00            lea r8, [rbp + 0xe0]
0092C81C  49 8B D6                        mov rdx, r14
0092C81F  33 C9                           xor ecx, ecx
0092C821  0F B6 D8                        movzx ebx, al
0092C824  E8 87 54 F4 FF                  call 0x140871cb0
0092C829  84 DB                           test bl, bl
0092C82B  0F 85 C0 F4 FF FF               jne 0x14092bcf1
0092C831  44 0F B6 6D 80                  movzx r13d, byte ptr [rbp - 0x80]
0092C836  BB 61 00 00 C0                  mov ebx, 0xc0000061
0092C83B  E9 51 EE FF FF                  jmp 0x14092b691
0092C840  89 7D B0                        mov dword ptr [rbp - 0x50], edi
0092C843  48 8B 7D E0                     mov rdi, qword ptr [rbp - 0x20]
0092C847  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
0092C84B  33 DB                           xor ebx, ebx
0092C84D  A8 10                           test al, 0x10
0092C84F  0F 85 5F 01 00 00               jne 0x14092c9b4
0092C855  8B CB                           mov ecx, ebx
0092C857  4C 8D 45 B0                     lea r8, [rbp - 0x50]
0092C85B  BA 14 00 00 00                  mov edx, 0x14
0092C860  E8 8B 42 AE FF                  call 0x140410af0
0092C865  FF 45 B0                        inc dword ptr [rbp - 0x50]
0092C868  48 85 C0                        test rax, rax
0092C86B  0F 85 6D 03 00 00               jne 0x14092cbde
0092C871  4D 85 E4                        test r12, r12
0092C874  0F 84 E3 E9 FF FF               je 0x14092b25d
0092C87A  48 8B 85 98 00 00 00            mov rax, qword ptr [rbp + 0x98]
0092C881  48 85 C0                        test rax, rax
0092C884  0F 84 49 04 00 00               je 0x14092ccd3
0092C88A  8B 78 04                        mov edi, dword ptr [rax + 4]
0092C88D  49 8B F4                        mov rsi, r12
0092C890  44 8B F3                        mov r14d, ebx
0092C893  BA 58 00 00 00                  mov edx, 0x58
0092C898  48 8D 8D 80 01 00 00            lea rcx, [rbp + 0x180]
0092C89F  44 8D 42 AA                     lea r8d, [rdx - 0x56]
0092C8A3  E8 58 A6 FE FF                  call 0x140916f00
0092C8A8  8B D8                           mov ebx, eax
0092C8AA  85 C0                           test eax, eax
0092C8AC  0F 88 9B EF FF FF               js 0x14092b84d
0092C8B2  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
0092C8B6  48 8D 8D 80 01 00 00            lea rcx, [rbp + 0x180]
0092C8BD  4C 8B CE                        mov r9, rsi
0092C8C0  C6 44 24 20 14                  mov byte ptr [rsp + 0x20], 0x14
0092C8C5  45 8B C6                        mov r8d, r14d
0092C8C8  BA 02 00 00 00                  mov edx, 2
0092C8CD  E8 6E CE FF FF                  call 0x140929740
0092C8D2  8B D8                           mov ebx, eax
0092C8D4  85 C0                           test eax, eax
0092C8D6  0F 88 71 EF FF FF               js 0x14092b84d
0092C8DC  48 8B 7D E0                     mov rdi, qword ptr [rbp - 0x20]
0092C8E0  4C 8D 85 80 01 00 00            lea r8, [rbp + 0x180]
0092C8E7  48 8B 4D C8                     mov rcx, qword ptr [rbp - 0x38]
0092C8EB  45 8B CF                        mov r9d, r15d
0092C8EE  0F B7 47 02                     movzx eax, word ptr [rdi + 2]
0092C8F2  8B D0                           mov edx, eax
0092C8F4  25 00 08 00 00                  and eax, 0x800
0092C8F9  D1 EA                           shr edx, 1
0092C8FB  83 E2 18                        and edx, 0x18
0092C8FE  0B D0                           or edx, eax
0092C900  48 8D 45 C0                     lea rax, [rbp - 0x40]
0092C904  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0092C909  48 8D 45 78                     lea rax, [rbp + 0x78]
0092C90D  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0092C912  48 8B 45 00                     mov rax, qword ptr [rbp]
0092C916  C7 44 24 38 02 00 00 00         mov dword ptr [rsp + 0x38], 2
0092C91E  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0092C923  48 8B 45 F0                     mov rax, qword ptr [rbp - 0x10]
0092C927  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0092C92C  48 8B 45 E8                     mov rax, qword ptr [rbp - 0x18]
0092C930  D1 EA                           shr edx, 1
0092C932  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0092C937  E8 F8 D1 19 00                  call 0x140ac9b34
0092C93C  8B D8                           mov ebx, eax
0092C93E  85 C0                           test eax, eax
0092C940  0F 88 07 EF FF FF               js 0x14092b84d
0092C946  8B B5 70 02 00 00               mov esi, dword ptr [rbp + 0x270]
0092C94C  C6 45 BC 01                     mov byte ptr [rbp - 0x44], 1
0092C950  E9 0C E9 FF FF                  jmp 0x14092b261
0092C955  66 83 7E 02 00                  cmp word ptr [rsi + 2], 0
0092C95A  0F 8D B3 01 00 00               jge 0x14092cb13
0092C960  8B 46 08                        mov eax, dword ptr [rsi + 8]
0092C963  85 C0                           test eax, eax
0092C965  0F 84 C5 EE FF FF               je 0x14092b830
0092C96B  48 8D 1C 06                     lea rbx, [rsi + rax]
0092C96F  E9 8C E6 FF FF                  jmp 0x14092b000
0092C974  66 45 85 ED                     test r13w, r13w
0092C978  0F 89 B0 01 00 00               jns 0x14092cb2e
0092C97E  41 8B 43 0C                     mov eax, dword ptr [r11 + 0xc]
0092C982  85 C0                           test eax, eax
0092C984  0F 84 9B 01 00 00               je 0x14092cb25
0092C98A  49 03 C3                        add rax, r11
0092C98D  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
0092C991  E9 A5 FD FF FF                  jmp 0x14092c73b
0092C996  66 85 C9                        test cx, cx
0092C999  0F 89 A5 01 00 00               jns 0x14092cb44
0092C99F  41 8B 43 0C                     mov eax, dword ptr [r11 + 0xc]
0092C9A3  85 C0                           test eax, eax
0092C9A5  0F 85 8C 01 00 00               jne 0x14092cb37
0092C9AB  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
0092C9AF  E9 44 E8 FF FF                  jmp 0x14092b1f8
0092C9B4  66 85 C0                        test ax, ax
0092C9B7  0F 89 C9 01 00 00               jns 0x14092cb86
0092C9BD  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
0092C9C0  85 C0                           test eax, eax
0092C9C2  0F 85 B5 01 00 00               jne 0x14092cb7d
0092C9C8  48 8B CB                        mov rcx, rbx
0092C9CB  E9 87 FE FF FF                  jmp 0x14092c857
0092C9D0  4C 8B C1                        mov r8, rcx
0092C9D3  E9 05 E4 FF FF                  jmp 0x14092addd
0092C9D8  41 B9 18 00 00 00               mov r9d, 0x18
0092C9DE  E9 EC E3 FF FF                  jmp 0x14092adcf
0092C9E3  41 F6 C1 08                     test r9b, 8
0092C9E7  0F 85 F4 F2 FF FF               jne 0x14092bce1
0092C9ED  84 C0                           test al, al
0092C9EF  0F 84 EC F2 FF FF               je 0x14092bce1
0092C9F5  4D 85 F6                        test r14, r14
0092C9F8  0F 84 91 02 00 00               je 0x14092cc8f
0092C9FE  48 8B 05 FB D0 6A 00            mov rax, qword ptr [rip + 0x6ad0fb]
0092CA05  48 8D 8D E0 00 00 00            lea rcx, [rbp + 0xe0]
0092CA0C  41 BC 01 00 00 00               mov r12d, 1
0092CA12  48 89 85 E8 00 00 00            mov qword ptr [rbp + 0xe8], rax
0092CA19  33 F6                           xor esi, esi
0092CA1B  44 89 A5 E0 00 00 00            mov dword ptr [rbp + 0xe0], r12d
0092CA22  45 0F B6 C4                     movzx r8d, r12b
0092CA26  44 89 A5 E4 00 00 00            mov dword ptr [rbp + 0xe4], r12d
0092CA2D  49 8B D6                        mov rdx, r14
0092CA30  89 B5 F0 00 00 00               mov dword ptr [rbp + 0xf0], esi
0092CA36  E8 35 E4 08 00                  call 0x1409bae70
0092CA3B  44 0F B6 C8                     movzx r9d, al
0092CA3F  4C 8D 85 E0 00 00 00            lea r8, [rbp + 0xe0]
0092CA46  49 8B D6                        mov rdx, r14
0092CA49  33 C9                           xor ecx, ecx
0092CA4B  0F B6 D8                        movzx ebx, al
0092CA4E  E8 5D 52 F4 FF                  call 0x140871cb0
0092CA53  84 DB                           test bl, bl
0092CA55  0F 85 C5 01 00 00               jne 0x14092cc20
0092CA5B  44 0F B6 6D 80                  movzx r13d, byte ptr [rbp - 0x80]
0092CA60  BB 61 00 00 C0                  mov ebx, 0xc0000061
0092CA65  E9 27 EC FF FF                  jmp 0x14092b691
0092CA6A  48 8B 50 20                     mov rdx, qword ptr [rax + 0x20]
0092CA6E  E9 15 FA FF FF                  jmp 0x14092c488
0092CA73  48 8B 5F 18                     mov rbx, qword ptr [rdi + 0x18]
0092CA77  E9 F5 E7 FF FF                  jmp 0x14092b271
0092CA7C  48 89 5D 68                     mov qword ptr [rbp + 0x68], rbx
0092CA80  E9 B5 E4 FF FF                  jmp 0x14092af3a
0092CA85  4C 8B F3                        mov r14, rbx
0092CA88  E9 31 E4 FF FF                  jmp 0x14092aebe
0092CA8D  4C 8B D1                        mov r10, rcx
0092CA90  E9 25 E3 FF FF                  jmp 0x14092adba
0092CA95  4C 8D 04 02                     lea r8, [rdx + rax]
0092CA99  E9 74 FC FF FF                  jmp 0x14092c712
0092CA9E  48 8B CF                        mov rcx, rdi
0092CAA1  E9 6E E7 FF FF                  jmp 0x14092b214
0092CAA6  4C 8B EB                        mov r13, rbx
0092CAA9  48 89 5D 40                     mov qword ptr [rbp + 0x40], rbx
0092CAAD  E9 6F E4 FF FF                  jmp 0x14092af21
0092CAB2  44 8B FA                        mov r15d, edx
0092CAB5  E9 7C F2 FF FF                  jmp 0x14092bd36
0092CABA  4D 8B F1                        mov r14, r9
0092CABD  41 8B F1                        mov esi, r9d
0092CAC0  E9 00 F4 FF FF                  jmp 0x14092bec5
0092CAC5  4D 8B 63 18                     mov r12, qword ptr [r11 + 0x18]
0092CAC9  E9 7D E6 FF FF                  jmp 0x14092b14b
0092CACE  4D 8B 72 20                     mov r14, qword ptr [r10 + 0x20]
0092CAD2  E9 0A F1 FF FF                  jmp 0x14092bbe1
0092CAD7  4D 8B FE                        mov r15, r14
0092CADA  E9 8A E5 FF FF                  jmp 0x14092b069
0092CADF  48 8B 72 18                     mov rsi, qword ptr [rdx + 0x18]
0092CAE3  E9 73 E6 FF FF                  jmp 0x14092b15b
0092CAE8  4D 8B E6                        mov r12, r14
0092CAEB  E9 5B E6 FF FF                  jmp 0x14092b14b
0092CAF0  49 8B CC                        mov rcx, r12
0092CAF3  E9 41 EC FF FF                  jmp 0x14092b739
0092CAF8  48 8B D9                        mov rbx, rcx
0092CAFB  E9 71 E7 FF FF                  jmp 0x14092b271
0092CB00  8B 46 04                        mov eax, dword ptr [rsi + 4]
0092CB03  85 C0                           test eax, eax
0092CB05  0F 84 3D FB FF FF               je 0x14092c648
0092CB0B  48 03 C6                        add rax, rsi
0092CB0E  E9 24 FB FF FF                  jmp 0x14092c637
0092CB13  48 8B 5E 10                     mov rbx, qword ptr [rsi + 0x10]
0092CB17  E9 E4 E4 FF FF                  jmp 0x14092b000
0092CB1C  48 8B 76 18                     mov rsi, qword ptr [rsi + 0x18]
0092CB20  E9 50 E5 FF FF                  jmp 0x14092b075
0092CB25  4C 89 75 90                     mov qword ptr [rbp - 0x70], r14
0092CB29  E9 0D FC FF FF                  jmp 0x14092c73b
0092CB2E  49 8B 43 18                     mov rax, qword ptr [r11 + 0x18]
0092CB32  E9 56 FE FF FF                  jmp 0x14092c98d
0092CB37  4D 8D 34 03                     lea r14, [r11 + rax]
0092CB3B  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
0092CB3F  E9 B4 E6 FF FF                  jmp 0x14092b1f8
0092CB44  4D 8B 73 18                     mov r14, qword ptr [r11 + 0x18]
0092CB48  4C 89 75 C8                     mov qword ptr [rbp - 0x38], r14
0092CB4C  E9 A7 E6 FF FF                  jmp 0x14092b1f8
0092CB51  4C 8D 4D 9C                     lea r9, [rbp - 0x64]
0092CB55  49 8B CC                        mov rcx, r12
0092CB58  E8 13 0C AC FF                  call 0x1403ed770
0092CB5D  84 C0                           test al, al
0092CB5F  0F 85 D4 E6 FF FF               jne 0x14092b239
0092CB65  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
0092CB69  BB 22 00 00 C0                  mov ebx, 0xc0000022
0092CB6E  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
0092CB72  48 8B F7                        mov rsi, rdi
0092CB75  45 32 ED                        xor r13b, r13b
0092CB78  E9 8D E9 FF FF                  jmp 0x14092b50a
0092CB7D  48 8D 0C 07                     lea rcx, [rdi + rax]
0092CB81  E9 D1 FC FF FF                  jmp 0x14092c857
0092CB86  48 8B 4F 18                     mov rcx, qword ptr [rdi + 0x18]
0092CB8A  E9 C8 FC FF FF                  jmp 0x14092c857
0092CB8F  4D 8B F4                        mov r14, r12
0092CB92  4C 89 65 30                     mov qword ptr [rbp + 0x30], r12
0092CB96  49 8B F4                        mov rsi, r12
0092CB99  C6 45 98 00                     mov byte ptr [rbp - 0x68], 0
0092CB9D  41 8B DC                        mov ebx, r12d
0092CBA0  4C 8B 65 10                     mov r12, qword ptr [rbp + 0x10]
0092CBA4  E9 2E ED FF FF                  jmp 0x14092b8d7
0092CBA9  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0092CBAD  BB 7C 00 00 C0                  mov ebx, 0xc000007c
0092CBB2  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
0092CBB6  45 32 ED                        xor r13b, r13b
0092CBB9  E9 4C E9 FF FF                  jmp 0x14092b50a
0092CBBE  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
0092CBC2  45 8B F1                        mov r14d, r9d
0092CBC5  E9 10 F3 FF FF                  jmp 0x14092beda
0092CBCA  4C 8B 42 20                     mov r8, qword ptr [rdx + 0x20]
0092CBCE  E9 3F FB FF FF                  jmp 0x14092c712
0092CBD3  45 33 E4                        xor r12d, r12d
0092CBD6  41 8B D4                        mov edx, r12d
0092CBD9  E9 D9 F7 FF FF                  jmp 0x14092c3b7
0092CBDE  0F B6 48 01                     movzx ecx, byte ptr [rax + 1]
0092CBE2  F6 C1 08                        test cl, 8
0092CBE5  0F 85 5C FC FF FF               jne 0x14092c847
0092CBEB  8B 78 04                        mov edi, dword ptr [rax + 4]
0092CBEE  48 8D 70 08                     lea rsi, [rax + 8]
0092CBF2  48 8B 85 98 00 00 00            mov rax, qword ptr [rbp + 0x98]
0092CBF9  44 8B F1                        mov r14d, ecx
0092CBFC  48 85 C0                        test rax, rax
0092CBFF  0F 84 84 EA FF FF               je 0x14092b689
0092CC05  8B 40 04                        mov eax, dword ptr [rax + 4]
0092CC08  23 C7                           and eax, edi
0092CC0A  3B C7                           cmp eax, edi
0092CC0C  0F 85 77 EA FF FF               jne 0x14092b689
0092CC12  48 85 F6                        test rsi, rsi
0092CC15  0F 85 78 FC FF FF               jne 0x14092c893
0092CC1B  E9 69 EA FF FF                  jmp 0x14092b689
0092CC20  44 8B 8D 70 02 00 00            mov r9d, dword ptr [rbp + 0x270]
0092CC27  E9 BB F0 FF FF                  jmp 0x14092bce7
0092CC2C  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
0092CC30  BB 77 00 00 C0                  mov ebx, 0xc0000077
0092CC35  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0092CC39  45 32 ED                        xor r13b, r13b
0092CC3C  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
0092CC40  E9 C5 E8 FF FF                  jmp 0x14092b50a
0092CC45  BB 17 00 00 C0                  mov ebx, 0xc0000017
0092CC4A  4C 8B F8                        mov r15, rax
0092CC4D  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0092CC51  45 32 ED                        xor r13b, r13b
0092CC54  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
0092CC58  E9 AD E8 FF FF                  jmp 0x14092b50a
0092CC5D  41 8B 46 0C                     mov eax, dword ptr [r14 + 0xc]
0092CC61  0F BA E8 18                     bts eax, 0x18
0092CC65  E9 7F F3 FF FF                  jmp 0x14092bfe9
0092CC6A  41 8B 46 0C                     mov eax, dword ptr [r14 + 0xc]
0092CC6E  0F BA E8 18                     bts eax, 0x18
0092CC72  E9 10 F2 FF FF                  jmp 0x14092be87
0092CC77  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
0092CC7B  BB 17 00 00 C0                  mov ebx, 0xc0000017
0092CC80  4C 8B 75 A8                     mov r14, qword ptr [rbp - 0x58]
0092CC84  48 8B F0                        mov rsi, rax
0092CC87  45 32 ED                        xor r13b, r13b
0092CC8A  E9 7B E8 FF FF                  jmp 0x14092b50a
0092CC8F  BB 7C 00 00 C0                  mov ebx, 0xc000007c
0092CC94  E9 74 F8 FF FF                  jmp 0x14092c50d
0092CC99  F7 40 04 00 00 00 FF            test dword ptr [rax + 4], 0xff000000
0092CCA0  74 3E                           je 0x14092cce0
0092CCA2  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0092CCA7  E9 06 E6 FF FF                  jmp 0x14092b2b2
0092CCAC  44 39 67 08                     cmp dword ptr [rdi + 8], r12d
0092CCB0  0F B6 DB                        movzx ebx, bl
0092CCB3  41 0F 44 DC                     cmove ebx, r12d
0092CCB7  89 5D D4                        mov dword ptr [rbp - 0x2c], ebx
0092CCBA  E9 77 E0 FF FF                  jmp 0x14092ad36
0092CCBF  48 8B 75 88                     mov rsi, qword ptr [rbp - 0x78]
0092CCC3  BB 5A 00 00 C0                  mov ebx, 0xc000005a
0092CCC8  4C 8B FE                        mov r15, rsi
0092CCCB  45 32 ED                        xor r13b, r13b
0092CCCE  E9 C6 E9 FF FF                  jmp 0x14092b699
0092CCD3  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0092CCD8  45 32 ED                        xor r13b, r13b
0092CCDB  E9 B1 E9 FF FF                  jmp 0x14092b691
0092CCE0  F6 40 01 40                     test byte ptr [rax + 1], 0x40
0092CCE4  0F 84 5C 62 1F 00               je 0x140b22f46
0092CCEA  4C 8D 4D 9C                     lea r9, [rbp - 0x64]
0092CCEE  49 8B CC                        mov rcx, r12
0092CCF1  48 8D 50 08                     lea rdx, [rax + 8]
0092CCF5  E8 76 0A AC FF                  call 0x1403ed770
0092CCFA  84 C0                           test al, al
0092CCFC  0F 84 7C 62 1F 00               je 0x140b22f7e
0092CD02  FF 45 B0                        inc dword ptr [rbp - 0x50]
0092CD05  E9 80 E5 FF FF                  jmp 0x14092b28a
0092CD0A  BB 01 00 00 00                  mov ebx, 1
0092CD0F  E9 CB EB FF FF                  jmp 0x14092b8df
0092CD14  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0092CD19  45 32 ED                        xor r13b, r13b
0092CD1C  E9 70 E9 FF FF                  jmp 0x14092b691
0092CD21  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0092CD26  45 32 ED                        xor r13b, r13b
0092CD29  E9 63 E9 FF FF                  jmp 0x14092b691
0092CD2E  4C 8B 7D 90                     mov r15, qword ptr [rbp - 0x70]
0092CD32  44 0F B6 6D 80                  movzx r13d, byte ptr [rbp - 0x80]
0092CD37  E9 5D E9 FF FF                  jmp 0x14092b699
0092CD3C  48 8B 8D E0 01 00 00            mov rcx, qword ptr [rbp + 0x1e0]
0092CD43  48 33 CC                        xor rcx, rsp
0092CD46  E8 F5 F8 D7 FF                  call 0x1406ac640
0092CD4B  48 81 C4 08 03 00 00            add rsp, 0x308
0092CD52  41 5F                           pop r15
0092CD54  41 5E                           pop r14
0092CD56  41 5D                           pop r13
0092CD58  41 5C                           pop r12
0092CD5A  5F                              pop rdi
0092CD5B  5E                              pop rsi
0092CD5C  5B                              pop rbx
0092CD5D  5D                              pop rbp
0092CD5E  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpNewSecurityObject(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned __int8 a6, unsigned int a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m130;
    unsigned __int16 v_stack_m134;
    unsigned __int16 v_stack_m136;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m150;
    unsigned int v_stack_m154;
    unsigned __int64 v_stack_m158;
    unsigned __int16 v_stack_m15C;
    unsigned int v_stack_m160;
    unsigned __int16 v_stack_m164;
    unsigned int v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m180;
    unsigned __int64 v_stack_m190;
    unsigned __int64 v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned __int64 v_stack_m1A8;
    unsigned int v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned __int64 v_stack_m1C0;
    unsigned __int64 v_stack_m1C8;
    unsigned __int64 v_stack_m1D0;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E0;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F0;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m200;
    unsigned __int64 v_stack_m208;
    unsigned __int8 v_stack_m20C;
    unsigned int v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned int v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned int v_stack_m260;
    unsigned __int8 v_stack_m264;
    unsigned __int8 v_stack_m267;
    unsigned __int8 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned int v_stack_m278;
    unsigned __int8 v_stack_m27C;
    unsigned __int8 v_stack_m27D;
    unsigned __int8 v_stack_m27E;
    unsigned __int8 v_stack_m27F;
    unsigned __int8 v_stack_m280;
    unsigned __int8 v_stack_m281;
    unsigned __int8 v_stack_m282;
    unsigned __int8 v_stack_m283;
    unsigned __int8 v_stack_m284;
    unsigned int v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int8 v_stack_m298;
    unsigned int v_stack_m29C;
    unsigned __int8 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m2B0;
    unsigned __int8 v_stack_m2B6;
    unsigned __int8 v_stack_m2B7;
    unsigned __int8 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned int v_stack_m2E0;
    unsigned __int64 v_stack_m2E8;
    unsigned int v_stack_m2F0;
    unsigned __int64 v_stack_m2F8;
    unsigned __int64 v_stack_m300;
    unsigned __int64 v_stack_m308;
    unsigned __int64 v_stack_m310;
    unsigned __int64 v_stack_m318;
    unsigned __int8 v_stack_m320;
    unsigned __int8 v_stack_m328;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_mB8;

    v_rsp = (v_rsp) - (776);
    result = (*(unsigned __int64 *)(v_rip + 5110733)) ^ (v_rsp);
    v_stack_m58 = result;
    v_stack_m238 = a9;
    v_stack_m1A0 = a10;
    v_stack_m1B8 = a11;
    result = 0;
    v_stack_m198 = a3;
    a3 = 0;
    v_stack_m170 = 0;
    v_stack_m298 = 0;
    v_stack_m27D = 0;
    v_stack_m27E = 0;
    v_stack_m2B8 = 0;
    v_stack_m283 = 0;
    v_stack_m2B7 = 0;
    v_stack_m268 = 0;
    v_stack_m267 = 0;
    v_stack_m284 = 0;
    v_stack_m20C = 0;
    v_stack_m27F = 0;
    v_stack_m148 = 0;
    v_stack_m220 = a1;
    v_stack_m1F0 = a4;
    v_stack_m1E0 = v_stack_m138;
    v_stack_m258 = a2;
    v_stack_m240 = a8;
    v_stack_m270 = 0;
    v_stack_m230 = 0;
    v_stack_m2B0 = 0;
    v_stack_m1C8 = 0;
    v_stack_m1E8 = 0;
    v_stack_m228 = 0;
    v_stack_m1A8 = 0;
    v_stack_m218 = 0;
    v_stack_m1F8 = 0;
    v_stack_m1D0 = 0;
    v_stack_m290 = 0;
    v_stack_m2B6 = 1;
    v_stack_m278 = 0;
    v_stack_m210 = 0;
    v_stack_m208 = 0;
    v_stack_m1D8 = 0;
    v_stack_m2A0 = 0;
    v_stack_m200 = 0;
    v_stack_m281 = 1;
    v_stack_m1C0 = 0;
    v_stack_m27C = 0;
    v_stack_m190 = v_xmm0;
    v_stack_m180 = v_xmm0;
    v_stack_m158 = v_xmm0;
    result = v_stack_m138;
    if (!(condition_is_below)) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = *(unsigned __int8 *)(result + 562);
        v_stack_m2B6 = (unsigned __int8)(result);
    }
    if (a2 == 0) goto loc_0092B17F;
    v_stack_m280 = 1;
loc_0092ACAD:
    result = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(a2 + 2))) & (128));
    v_rbx = (condition_is_not_equal) ? 1 : 0;
    a2 = (unsigned __int8)((*(unsigned __int16 *)(a2 + 2)) >> (6));
    a2 = (unsigned __int8)((a2) & (1));
    v_stack_m1B0 = (unsigned int)(a2);
    if (a8 == 0) goto loc_0092B81A;
loc_0092ACDB:
    result = ExAcquireResourceSharedLite(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 48), (unsigned __int8)(128 - 127), 128, 0);
    if ((*(unsigned __int64 *)(a8)) != 0) {
        result = *(unsigned __int64 *)(gs_base + (0 + 392));
        a2 = (unsigned __int8)(128 - 127);
        a1 = *(unsigned __int64 *)(a8);
        a1 = *(unsigned __int64 *)(a1 + 48);
        result = ExAcquireResourceSharedLite(a1, a2, 128, 0);
    }
    v_stack_m264 = (unsigned __int8)(v_rbx);
    if (*(unsigned __int64 *)(a8) != 0) goto loc_0092CCAC;
loc_0092AD36:
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a8 + 16) + 144))) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a8 + 16) + 144)));
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a8 + 16) + 144))) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a8 + 16) + 144)));
    result = SepLocateTokenIntegrity(*(unsigned __int64 *)(a8 + 16), *(unsigned __int64 *)(a8 + 16), *(unsigned __int64 *)(a8 + 16), 0);
    if (result == 0) goto loc_0092C783;
loc_0092AD8C:
    result = SepLocateTokenTrustLevel(v_stack_m240, *(unsigned __int64 *)(a8 + 16), *(unsigned __int64 *)(a8 + 16), 0);
    a1 = 0;
    if (result != 0) goto loc_0092B43E;
loc_0092ADA5:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168) == 0) goto loc_0092CA8D;
loc_0092ADBA:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168) == 0) goto loc_0092C9D8;
loc_0092ADCF:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 184) == 0) goto loc_0092C9D0;
loc_0092ADDD:
    a1 = (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 152) + a1 * 8) + 1)) + (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 152) + a1 * 8) + 1));
    a1 = (a1) + (*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1));
    a2 = (0 + a1 * 4) + (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168) + 1) * 4 + 8);
    a2 = (a2) + (*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 184) + 2));
    a2 = (a2) + (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168) + 1) * 4 + 32);
    result = ExAllocatePool2(64, a2, (unsigned int)(0x64536553ULL), *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168) + 1) * 4 + 32);
    v_stack_m1E8 = result;
    if (result == 0) goto loc_0092B44F;
    result = memcpy(result, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 152) + a1 * 8), *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 152) + a1 * 8) + 1) * 4 + 8, *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168) + 1) * 4 + 32);
    a1 = (v_stack_m1E8) + (8);
    v_stack_m228 = a1 + *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 152) + a1 * 8) + 1) * 4;
    result = memcpy(a1 + *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 152) + a1 * 8) + 1) * 4, *(unsigned __int64 *)(result), *(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1) * 4 + 8, *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168) + 1) * 4 + 32);
    v_r15 = (*(unsigned __int8 *)(*(unsigned __int64 *)(result) + 1) * 4 + 8) + (a1 + *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 152) + a1 * 8) + 1) * 4);
    v_stack_m218 = v_r15;
    if (result != 0) goto loc_0092B772;
    a1 = 0;
    v_stack_m1A8 = 0;
loc_0092AE88:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168) == 0) goto loc_0092CA85;
    result = memcpy(v_r15, *(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168), *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168) + 1) * 4 + 8, *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168) + 1) * 4 + 32);
    v_r15 = (v_r15 + *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168) + 1) * 4) + (8);
    v_stack_m218 = v_r15;
    v_rbx = 0;
loc_0092AEBE:
    result = memcpy(v_r15, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 152) + a1 * 8), *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 152) + a1 * 8) + 1) * 4 + 8, *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168) + 1) * 4 + 32);
    v_r12 = (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 152) + a1 * 8) + 1)) + (2);
    v_stack_m1D0 = v_r15 + v_r12 * 4;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168) == 0) goto loc_0092CAA6;
    v_stack_m1F8 = v_r15 + v_r12 * 4;
    result = memcpy(v_r15 + v_r12 * 4, *(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168), *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168) + 1) * 4 + 8, *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168) + 1) * 4 + 32);
    v_r12 = (v_r15 + v_r12 * 4 + *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168) + 1) * 4) + (8);
    v_stack_m1D0 = v_r12;
loc_0092AF21:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 184) == 0) goto loc_0092CA7C;
    result = memcpy(v_r12, *(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 184), *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 184) + 2), *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168) + 1) * 4 + 32);
loc_0092AF3A:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m240 + 16) + 48), *(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 184), *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 184) + 2), *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168) + 1) * 4 + 32);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 184), *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 184) + 2), *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168) + 1) * 4 + 32);
    if (*(unsigned __int64 *)(v_stack_m240) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m240) + 48);
        result = ExReleaseResourceLite(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 184), *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 184) + 2), *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168) + 1) * 4 + 32);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = KeLeaveCriticalRegionThread(a1, *(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 184), *(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 184) + 2), *(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a8 + 16) + 168) + 1) * 4 + 32);
    }
loc_0092AF8E:
    if (sign_flag) goto loc_0092AFAB;
loc_0092AF9C:
    v_stack_m250 = *(unsigned __int64 *)(v_stack_m258 + 8);
    if (*(unsigned __int64 *)(v_stack_m258 + 8) == 0) goto loc_0092AFB7;
    v_stack_m283 = 1;
    goto loc_0092AFD7;
loc_0092AFAB:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m258 + 4))) != 0) goto loc_0092B861;
loc_0092AFB7:
    if ((((unsigned __int8)((unsigned int)(a7))) & (32)) != 0) goto loc_0092C61F;
    result = v_stack_m1E8;
    if ((unsigned __int8)((unsigned int)(v_stack_m264)) != 0) { result = v_r15; }
    v_stack_m250 = result;
    if (result == 0) goto loc_0092B75A;
loc_0092AFD7:
    if (sign_flag) goto loc_0092B6F0;
loc_0092AFE4:
    v_stack_m248 = *(unsigned __int64 *)(v_stack_m258 + 16);
    if (*(unsigned __int64 *)(v_stack_m258 + 16) != 0) goto loc_0092B00D;
loc_0092AFED:
    if ((((unsigned __int8)((unsigned int)(a7))) & (64)) != 0) goto loc_0092C54B;
    v_rbx = v_r15;
    if ((unsigned __int8)((unsigned int)(v_stack_m264)) != 0) { v_rbx = v_r15 + v_r12 * 4; }
loc_0092B000:
    v_stack_m248 = v_rbx;
    if (v_rbx == 0) goto loc_0092B830;
loc_0092B00D:
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a7)))) & (4));
    v_stack_m288 = (unsigned int)(v_r10);
    v_r13 = (condition_is_not_equal) ? 1 : 0;
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a7)))) & (2));
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_stack_m258 + 2))) & (16));
    result = (unsigned __int16)(-((unsigned __int16)(a1)));
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m258 + 2)))) >> (2));
    a3 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m258 + 2)))) >> (1));
    result = (unsigned int)((result) & (8));
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m258 + 2)))) >> (1));
    a3 = (unsigned int)((a3) & (0x400ULL));
    v_rdi = (unsigned int)((v_rdi) & (0x1000ULL));
    a4 = (unsigned int)((v_stack_m1E8) & (4));
    v_r14 = 0;
    if ((unsigned __int16)(a1) != 0) goto loc_0092B19A;
loc_0092B069:
    if (v_stack_m220 != 0) goto loc_0092B7C4;
loc_0092B072:
loc_0092B075:
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(a3)));
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(result)));
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(a4)));
    if (condition_is_not_equal) goto loc_0092B2F2;
    if (0 != 0) goto loc_0092B2F2;
    v_stack_m2B7 = 0;
    result = (unsigned int)(-((unsigned int)((unsigned int)(v_r12))));
    v_stack_m2A8 = 0;
    v_stack_m29C = 0x8000000BULL;
    a1 = (unsigned int)((a1) & (0x400ULL));
    v_stack_m278 = (unsigned int)(a1);
    goto loc_0092B0E4;
loc_0092B0B0:
loc_0092B0B4:
    v_r14 = 0;
loc_0092B0B7:
    v_stack_m2A8 = v_stack_m2A8;
    if (!sign_flag) goto loc_0092B869;
    v_stack_m2A8 = v_stack_m2A8;
    if (0 != 0x8000000BULL) goto loc_0092B676;
    v_stack_m2B7 = (unsigned __int8)(v_stack_m2B7);
loc_0092B0E4:
    a1 = (unsigned int)(0x8800ULL);
    if ((unsigned int)(v_r12) == 0) { a1 = (unsigned int)((unsigned int)(0x8000ULL)); }
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int16 *)(v_stack_m258 + 2))) & (48));
    if (((unsigned __int8)(result)) == 48) goto loc_0092C72D;
    v_stack_m260 = (unsigned int)(a1);
loc_0092B10D:
    v_r15 = ((unsigned int)((unsigned int)(v_stack_m288)) != 0) ? 1 : 0;
    a1 = (unsigned __int16)(((unsigned __int16)(*(unsigned __int16 *)(v_stack_m258 + 2))) & (16));
    result = (unsigned __int16)(-((unsigned __int16)(a1)));
    result = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m258 + 2)))) >> (2));
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m258 + 2)))) >> (1));
    result = (unsigned int)((result) & (8));
    v_rdi = (unsigned int)((v_rdi) & (0x400ULL));
    a3 = (unsigned int)((a3) & (4));
    if ((unsigned __int16)(a1) != 0) goto loc_0092B3E5;
loc_0092B14B:
    if (v_stack_m220 != 0) goto loc_0092B7F0;
loc_0092B158:
loc_0092B15B:
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(result)));
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(a3)));
    if (condition_is_not_equal) goto loc_0092B583;
    if (0 != 0) goto loc_0092B583;
    v_stack_m270 = 0;
    v_stack_m29C = 0x8000000BULL;
    goto loc_0092B1E2;
loc_0092B17F:
    v_stack_m280 = (unsigned __int8)(a3);
    v_stack_m258 = v_stack_m190;
    v_stack_m190 = 1;
    goto loc_0092ACAD;
loc_0092B19A:
    if (!sign_flag) goto loc_0092C768;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m190 + 12))) == 0) goto loc_0092CAD7;
    goto loc_0092B069;
loc_0092B1B8:
loc_0092B1BC:
    v_r14 = 0;
loc_0092B1BF:
    v_stack_m270 = v_stack_m270;
    v_stack_m29C = 0;
    if (!sign_flag) goto loc_0092B6E0;
    v_stack_m270 = v_stack_m270;
    if (0 != 0x8000000BULL) goto loc_0092B84D;
loc_0092B1E2:
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int16 *)(v_stack_m258 + 2))) & (48));
    if (((unsigned __int8)(result)) == 48) goto loc_0092C756;
loc_0092B1F8:
    v_rdi = 0;
    v_stack_m288 = 0;
loc_0092B204:
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_m258 + 2))) & (16)) != 0) goto loc_0092B403;
loc_0092B214:
    result = RtlFindAceByType(0, 20, v_stack_m288, v_stack_m2B7);
    a2 = result + 8;
    if (result == 0) { a2 = 0; }
    if (a2 != 0) goto loc_0092CB51;
loc_0092B239:
    if (result != 0) goto loc_0092C517;
    if (condition_is_below) goto loc_0092C840;
loc_0092B25D:
    v_stack_m1C0 = v_stack_m270;
loc_0092B261:
    a1 = 0;
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_m258 + 2))) & (16)) != 0) goto loc_0092B421;
loc_0092B271:
    v_stack_m29C = 0;
    v_stack_m168 = 0;
    v_stack_m164 = 256;
    v_stack_m288 = 0;
loc_0092B28A:
    result = RtlFindAceByType(0, 21, v_stack_m288, v_stack_m2B7);
    if (result != 0) goto loc_0092CC99;
    if (result != 0) goto loc_0092B28A;
loc_0092B2B2:
    if (sign_flag) goto loc_0092B84D;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a7)))) >> (8));
    a1 = (unsigned int)((a1) & (1));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (2));
    if (condition_is_above_or_equal) { a2 = (unsigned int)(a1); }
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(a2))) | ((unsigned int)(result + 4)));
    if (condition_is_above_or_equal) { v_rbx = (unsigned int)(a2); }
    if ((unsigned int)(v_rbx) == 0) goto loc_0092B72B;
loc_0092B2E9:
    goto loc_0092B8D7;
loc_0092B2F2:
    v_stack_m29C = 200;
loc_0092B2FA:
    a1 = 0;
    if (((unsigned int)(v_stack_m208)) >= 2) goto loc_0092B0B4;
    result = ExAllocatePool2(256, 200, (unsigned int)(0x63416553ULL), v_stack_m2B7);
    v_stack_m2A8 = result;
    if (result == 0) goto loc_0092CC45;
    v_stack_m2C0 = v_stack_m278;
    v_stack_m2C8 = v_stack_m2B7;
    v_stack_m2D0 = result;
    v_stack_m2D8 = v_stack_m29C;
    v_stack_m2E0 = (unsigned int)((unsigned int)(a5));
    v_stack_m2E8 = v_stack_m1F0;
    v_stack_m2F0 = 2;
    v_stack_m2F8 = v_stack_m238;
    v_stack_m300 = v_stack_m1F8;
    v_stack_m308 = v_stack_m218;
    v_stack_m310 = v_stack_m248;
    v_stack_m318 = v_stack_m250;
    v_stack_m320 = (unsigned __int8)((unsigned int)((unsigned int)(a1)));
    v_stack_m328 = (unsigned __int8)(v_stack_m282);
    result = RtlpInheritAcl2(v_stack_m208, result + 4, (unsigned int)((unsigned int)(v_stack_m258)), a6);
    if (sign_flag) goto loc_0092B6BA;
    if (v_stack_m29C != 0) goto loc_0092B0B0;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m2A8, a2, (unsigned int)((unsigned int)(v_stack_m258)), a6);
    v_r14 = 0;
    goto loc_0092B0B7;
loc_0092B3E5:
    if (!sign_flag) goto loc_0092CAC5;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m258 + 12))) == 0) goto loc_0092CAE8;
    goto loc_0092B14B;
loc_0092B403:
    if (!sign_flag) goto loc_0092C78F;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m258 + 12))) == 0) goto loc_0092CA9E;
    goto loc_0092B214;
loc_0092B421:
    if (!sign_flag) goto loc_0092CA73;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m258 + 12))) == 0) goto loc_0092CAF8;
    goto loc_0092B271;
loc_0092B43E:
    goto loc_0092ADA5;
loc_0092B44F:
    result = ExReleaseResourceLite(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m240 + 16) + 48), *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(v_stack_m258 + 12)) + 1) * 4 + 8, (unsigned int)((unsigned int)(v_stack_m258)), a6);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(v_stack_m258 + 12)) + 1) * 4 + 8, (unsigned int)((unsigned int)(v_stack_m258)), a6);
    if (*(unsigned __int64 *)(v_stack_m240) != 0) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m240) + 48);
        result = ExReleaseResourceLite(a1, *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(v_stack_m258 + 12)) + 1) * 4 + 8, (unsigned int)((unsigned int)(v_stack_m258)), a6);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = KeLeaveCriticalRegionThread(a1, *(unsigned __int8 *)((unsigned int)(*(unsigned int *)(v_stack_m258 + 12)) + 1) * 4 + 8, (unsigned int)((unsigned int)(v_stack_m258)), a6);
    }
    goto loc_0092CD3C;
loc_0092B497:
loc_0092B4A0:
    result = (unsigned int)(0xC000009AULL);
    if (((unsigned int)(v_stack_m258)) >= = ((unsigned int)(*(unsigned __int16 *)(v_stack_m208 + 2)))) {
        a3 = (unsigned int)(v_stack_m258);
        a2 = 0;
        a3 = (unsigned int)((a3) - ((unsigned int)(*(unsigned __int16 *)(v_stack_m208 + 2))));
        a1 = (*(unsigned __int16 *)(v_stack_m208 + 2)) + (v_stack_m240);
        result = memset(a1, a2, a3, a6);
    }
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m240))) - ((unsigned int)(v_stack_m290)));
    *(unsigned int *)(v_stack_m290 + 16) = (unsigned int)(result);
    v_rbx = (v_stack_m240) + ((unsigned int)((unsigned int)(v_stack_m258)));
loc_0092B4C6:
    result = memcpy(v_rbx, v_stack_m250, (unsigned int)((unsigned int)(v_stack_m258 + (unsigned int)(*(unsigned int *)(v_stack_m258 + 12)) * 1)), a6);
    v_rbx = (v_rbx) + ((unsigned int)((unsigned int)(v_stack_m258 + (unsigned int)(*(unsigned int *)(v_stack_m258 + 12)) * 1)));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - ((unsigned int)(v_stack_m290)));
    *(unsigned int *)(v_stack_m290 + 4) = (unsigned int)(result);
    result = v_stack_m248;
    if (v_stack_m248 != 0) {
        a3 = (unsigned int)(result + 4);
        a2 = v_stack_m248;
        a1 = v_rbx;
        result = memcpy(a1, a2, a3, a6);
        v_rbx = (unsigned int)((v_rbx) - ((unsigned int)(v_stack_m290)));
        *(unsigned int *)(v_stack_m290 + 8) = (unsigned int)(v_rbx);
    }
    result = 0;
loc_0092B50A:
    if (v_stack_m200 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m200, a2, a3, a6);
    }
    if (v_stack_m27F != 0) goto loc_0092C606;
loc_0092B524:
    if (v_stack_m1E8 != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(v_stack_m1E8, a2, a3, a6);
    }
    if (v_stack_m298 != 0) goto loc_0092B572;
    if (v_stack_m27E != 0) goto loc_0092B572;
loc_0092B540:
    if (v_stack_m27D != 0) goto loc_0092C6EA;
loc_0092B54A:
    if (v_stack_m1C0 != 0) goto loc_0092C7B4;
loc_0092B557:
    if ((unsigned __int8)(v_stack_m2B8) != 0) goto loc_0092B6A2;
loc_0092B560:
    *(unsigned __int64 *)(v_stack_m198) = v_stack_m290;
    goto loc_0092CD3C;
loc_0092B572:
    if (v_stack_m2A8 == 0) goto loc_0092B540;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m2A8, a2, a3, a6);
    goto loc_0092B540;
loc_0092B583:
    v_stack_m29C = 200;
loc_0092B58B:
    a1 = 0;
    if (((unsigned int)(v_stack_m290)) >= 2) goto loc_0092B1BC;
    result = ExAllocatePool2(256, 200, (unsigned int)(0x63416553ULL), a6);
    v_stack_m270 = result;
    if (result == 0) goto loc_0092B848;
    v_stack_m2C0 = v_stack_m210;
    v_stack_m2C8 = v_stack_m268;
    v_stack_m2D0 = result;
    v_stack_m2D8 = v_stack_m29C;
    v_stack_m2E0 = (unsigned int)((unsigned int)(a5));
    v_stack_m2E8 = v_stack_m1F0;
    v_stack_m2F0 = 2;
    v_stack_m2F8 = v_stack_m238;
    v_stack_m300 = v_stack_m1F8;
    v_stack_m308 = v_stack_m218;
    v_stack_m310 = v_stack_m248;
    v_stack_m318 = v_stack_m250;
    v_stack_m320 = (unsigned __int8)(v_stack_m2A8);
    v_stack_m328 = (unsigned __int8)(v_stack_m282);
    result = RtlpInheritAcl2(v_stack_m208, v_stack_m258 + (unsigned int)(*(unsigned int *)(v_stack_m258 + 12)) * 1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m258 + (unsigned int)(*(unsigned int *)(v_stack_m258 + 12)) * 1)))), a6);
    if (sign_flag) goto loc_0092B705;
    if (v_stack_m29C != 0) goto loc_0092B1B8;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m270, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m258 + (unsigned int)(*(unsigned int *)(v_stack_m258 + 12)) * 1)))), a6);
    v_r14 = 0;
    goto loc_0092B1BF;
loc_0092B676:
    v_r13 = 0;
    goto loc_0092B50A;
loc_0092B689:
    v_r13 = 0;
loc_0092B691:
loc_0092B699:
    goto loc_0092B50A;
loc_0092B6A2:
    if (v_stack_m2B0 == 0) goto loc_0092B560;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m2B0, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m258 + (unsigned int)(*(unsigned int *)(v_stack_m258 + 12)) * 1)))), a6);
    goto loc_0092B560;
loc_0092B6BA:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m2A8, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m258 + (unsigned int)(*(unsigned int *)(v_stack_m258 + 12)) * 1)))), a6);
    result = 0;
    if (((unsigned int)((unsigned int)(0xC000000DULL))) != 0xC0000023ULL) goto loc_0092B0B4;
    v_r14 = (unsigned int)((v_stack_m290) + 1);
    goto loc_0092B2FA;
loc_0092B6E0:
    v_stack_m27D = 1;
    goto loc_0092B1F8;
loc_0092B6F0:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m258 + 8))) == 0) goto loc_0092AFED;
    goto loc_0092AFE4;
loc_0092B705:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m270, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_m258 + (unsigned int)(*(unsigned int *)(v_stack_m258 + 12)) * 1)))), a6);
    result = 0;
    if (((unsigned int)(v_stack_m258 + (unsigned int)(*(unsigned int *)(v_stack_m258 + 8)) * 1)) != 0xC0000023ULL) goto loc_0092B1BC;
    v_r14 = (unsigned int)((0) + 1);
    goto loc_0092B58B;
loc_0092B72B:
    v_r12 = 0;
    if ((((unsigned __int8)(*(unsigned __int16 *)((unsigned int)((unsigned int)(v_stack_m258 + (unsigned int)(*(unsigned int *)(v_stack_m258 + 12)) * 1)) + 2))) & (16)) != 0) goto loc_0092B7A7;
loc_0092B739:
    a3 = 0;
    result = RtlFindAceByType(0, a3 + 17, a3, a6);
    if (result != 0) goto loc_0092B8A6;
    goto loc_0092B2E9;
loc_0092B75A:
    v_r13 = 0;
    goto loc_0092B50A;
loc_0092B772:
    v_stack_m1A8 = v_stack_m2B0;
    result = memcpy(v_stack_m2B0, v_stack_m290, *(unsigned __int8 *)(v_stack_m290 + 1) * 4 + 8, a6);
    v_r15 = (v_stack_m2B0 + *(unsigned __int8 *)(v_stack_m290 + 1) * 4) + (8);
    v_stack_m218 = v_r15;
    goto loc_0092AE88;
loc_0092B7A7:
    if (!sign_flag) goto loc_0092C771;
    if ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_stack_m258 + (unsigned int)(*(unsigned int *)(v_stack_m258 + 12)) * 1)) + 12))) == 0) goto loc_0092CAF0;
    goto loc_0092B739;
loc_0092B7C4:
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_m2B0 + 2))) & (16)) == 0) goto loc_0092B072;
    if (!sign_flag) goto loc_0092CB1C;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m2B0 + 12))) == 0) goto loc_0092B072;
    v_rsi = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m2B0 + 12))))) + (v_stack_m220);
    goto loc_0092B075;
loc_0092B7F0:
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_m290 + 2))) & (16)) == 0) goto loc_0092B158;
    if (!sign_flag) goto loc_0092CADF;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m290 + 12))) == 0) goto loc_0092B158;
    goto loc_0092B15B;
loc_0092B81A:
    v_stack_m264 = (unsigned int)((unsigned __int8)((unsigned int)(0xC000007CULL)));
    if ((unsigned __int16)((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_stack_m258 + (unsigned int)(*(unsigned int *)(v_stack_m258 + 12)) * 1)) + 12))) == 0) goto loc_0092AF8E;
    goto loc_0092ACDB;
loc_0092B830:
    v_r13 = 0;
    goto loc_0092B50A;
loc_0092B848:
loc_0092B84D:
    v_r13 = 0;
    goto loc_0092B50A;
loc_0092B861:
    result = ((unsigned int)(*(unsigned int *)((unsigned int)((unsigned int)(v_stack_m258 + (unsigned int)(*(unsigned int *)(v_stack_m258 + 12)) * 1)) + 12))) + (v_stack_m258);
    goto loc_0092AF9C;
loc_0092B869:
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m278)))) & (8));
    v_r13 = (unsigned int)((v_r13) | (0x2004ULL));
    v_r13 = (unsigned int)((v_r13) + ((unsigned int)(v_r13)));
    result = (unsigned int)(((unsigned int)(v_stack_m278)) & (0x1400ULL));
    v_stack_m298 = 1;
    v_r13 = (unsigned int)((v_r13) | ((unsigned int)(result)));
    v_stack_m2B7 = (unsigned __int8)(v_stack_m2B7);
    v_r13 = (unsigned int)((v_r13) + ((unsigned int)(v_r13)));
    v_stack_m260 = (unsigned int)(v_r13);
    goto loc_0092B10D;
loc_0092B8A6:
    v_stack_m208 = result + 8;
    v_stack_m2A0 = (unsigned __int8)(*(unsigned __int8 *)(result + 1));
    if (((unsigned __int8)(*(unsigned __int8 *)(result + 1))) == 8) goto loc_0092CB8F;
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 1))) & (16)) != 0) goto loc_0092CB8F;
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 1))) & (8)) != 0) goto loc_0092C5BD;
loc_0092B8D7:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 4))) == 0) goto loc_0092C42E;
loc_0092B8DF:
    if (v_stack_m290 != 0) goto loc_0092B8FD;
    if (v_stack_m240 == 0) goto loc_0092C6D1;
    v_stack_m208 = v_stack_m228;
    v_stack_m2A0 = (unsigned __int8)(v_stack_m290);
loc_0092B8FD:
    if (v_stack_m228 == 0) goto loc_0092C28A;
    a2 = 0;
    result = memset(v_stack_m130, a2, a2 + 120, v_stack_m2B7);
    v_stack_m138 = 0x800002ULL;
    v_stack_m160 = 0;
    v_stack_m15C = 0x1000ULL;
    if (v_stack_m228 <= result) goto loc_0092C4C9;
    result = (unsigned __int8)((*(unsigned __int8 *)(v_stack_m228)) & (15));
    if (((unsigned __int8)(result)) != 1) goto loc_0092C4C9;
    if ((*(unsigned __int8 *)(v_stack_m228 + 1)) > 15) goto loc_0092C4C9;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m228 + 2))) - (v_stack_m160));
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int16 *)(v_stack_m228 + 6);
        result = v_stack_m15C;
        a1 = (unsigned int)((a1) - ((unsigned int)(result)));
    }
    if ((unsigned int)(a1) != 0) goto loc_0092B689;
    if ((((unsigned int)(v_stack_m2A0)) & (0xFFFFFFE0ULL)) != 0) goto loc_0092CD14;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(result + 4)))) & (0xFFFFFFF8ULL)) != 0) goto loc_0092CD21;
    result = RtlValidAcl(v_stack_m138, v_stack_m2A0, a2 + 120, v_stack_m2B7);
    if ((unsigned __int8)(result) == 0) goto loc_0092CC2C;
    a1 = 0;
loc_0092B9CC:
    if (0 < ((unsigned int)(v_stack_m134))) goto loc_0092BF7D;
    a3 = (v_stack_m138) + (v_stack_m136);
    a2 = v_stack_m130;
    if (v_stack_m130 > a3) { a2 = 0; }
    a1 = (unsigned __int16)((*(unsigned __int8 *)(v_stack_m228 + 1)) + ((unsigned __int16)(v_stack_m2A8)));
    a1 = (unsigned __int16)((a1) << (2));
    if (a2 == 0) goto loc_0092C56C;
    result = ((unsigned __int16)(a1)) + (a2);
    if (result > a3) goto loc_0092C56C;
    *(unsigned __int16 *)(a2 + 2) = (unsigned __int16)(a1);
    *(unsigned __int8 *)(a2 + 1) = (unsigned __int8)(v_stack_m2A0);
    *(unsigned __int8 *)(a2) = 17;
    *(unsigned int *)(a2 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 4)));
    result = memcpy(a2 + 8, v_stack_m228, *(unsigned __int8 *)(v_stack_m228 + 1) * 4 + 8, v_stack_m134);
    a2 = 0;
    v_stack_m138 = 2;
    v_stack_m29C = 0;
loc_0092BA53:
    if ((((unsigned int)((unsigned int)(a7))) & (0x700ULL)) == 0) goto loc_0092C240;
loc_0092BA64:
    if (v_stack_m220 != 0) goto loc_0092C405;
loc_0092BA71:
loc_0092BA74:
    if ((unsigned int)(v_stack_m2A8) != 0) goto loc_0092C009;
    if (0 != 0) goto loc_0092C009;
loc_0092BA88:
    v_stack_m278 = 0;
loc_0092BA94:
    v_stack_m308 = v_stack_m230;
    v_stack_m310 = v_stack_m1D8;
    v_stack_m318 = v_stack_m1B8;
    v_stack_m320 = v_stack_m270;
    v_stack_m328 = v_stack_m1C0;
    result = RtlpCombineAcls(v_stack_m2A8, v_stack_m1E0, v_stack_m270, v_stack_m270);
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r13))) & (0x2000ULL));
    result = (unsigned int)((result) << (17));
    if (v_stack_m1E0 == 0) goto loc_0092BAFD;
    if (v_stack_m1E0 != v_stack_m1E0) {
        a2 = 0;
        a1 = v_stack_m1E0;
        result = ExFreePoolWithTag(a1, a2, v_stack_m270, v_stack_m270);
    }
    if (sign_flag) goto loc_0092CC4D;
    if (v_stack_m1D8 == 0) goto loc_0092BB44;
    if (v_stack_m298 != 0) goto loc_0092C6B5;
loc_0092BB18:
    v_stack_m2A8 = v_stack_m1D8;
    result = 0;
    v_stack_m27E = 1;
    v_stack_m1D8 = 0;
    result = (unsigned int)((0) & (8));
    v_rdi = (unsigned int)((0) & (0x1400ULL));
    result = (unsigned int)((result) | (4));
    result = (unsigned int)((result) + ((unsigned int)(result)));
    result = (unsigned int)((result) | ((unsigned int)(v_rdi)));
    result = (unsigned int)((result) + ((unsigned int)(result)));
    v_r13 = (unsigned int)((v_r13) | ((unsigned int)(result)));
    v_stack_m260 = (unsigned int)(v_r13);
loc_0092BB44:
    if ((((unsigned __int8)((unsigned int)(a7))) & (8)) != 0) goto loc_0092BBAE;
    a3 = 0;
    result = RtlFindAceByType(v_stack_m1D8, a3 + 17, a3, (unsigned int)(a7));
    if (result == 0) goto loc_0092C77A;
loc_0092BB6D:
    if (result + 8 == 0) goto loc_0092BBA7;
    if (v_stack_m240 == 0) goto loc_0092CBA9;
    result = RtlSidDominates(v_stack_m228, result + 8, v_stack_m281, (unsigned int)(a7));
    if (sign_flag) goto loc_0092CC4D;
    result = (unsigned __int8)((unsigned int)(v_stack_m20C));
    if (v_stack_m281 == 0) { result = 1; }
    v_stack_m20C = (unsigned int)(result);
loc_0092BBA7:
loc_0092BBAE:
    v_rdi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a7)))) >> (2));
    v_rdi = (unsigned __int8)((v_rdi) & (1));
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a7)))) & (1));
    v_r11 = 0;
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_m258 + 2))) & (4)) != 0) goto loc_0092BC40;
loc_0092BBD1:
    if (v_stack_m220 != 0) goto loc_0092C3DA;
loc_0092BBDE:
loc_0092BBE1:
    v_rsi = (unsigned int)((*(unsigned __int16 *)(v_stack_m258 + 2)) & (0x140CULL));
    if (condition_is_not_equal) goto loc_0092C110;
    if (0 != 0) goto loc_0092C110;
    v_rdi = 0;
    v_stack_m2B0 = 0;
loc_0092BC07:
    if ((((unsigned __int8)((unsigned int)(a7))) & (1)) != 0) {
    }
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int16 *)(v_stack_m258 + 2))) & (12));
    if (((unsigned __int8)(result)) == 12) goto loc_0092C706;
    v_r13 = (unsigned int)(v_stack_m260);
    if (v_stack_m1D0 != 0) {
        a3 = v_stack_m1D0;
        v_stack_m2B0 = v_stack_m1D0;
        v_r13 = (unsigned int)(((unsigned int)(v_stack_m260)) | (4));
    }
    v_r15 = 0;
    goto loc_0092BC85;
loc_0092BC40:
    if (!sign_flag) goto loc_0092C462;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m258 + 16))) == 0) goto loc_0092C585;
    goto loc_0092BBD1;
loc_0092BC5D:
    result = (unsigned int)(((unsigned int)(v_stack_m278)) & (0x1408ULL));
    result = (unsigned int)((result) | (4));
    v_r13 = (unsigned int)(((unsigned int)(v_stack_m260)) | ((unsigned int)(result)));
    v_stack_m2B8 = 1;
loc_0092BC85:
    if (condition_is_below) goto loc_0092BCA4;
    if (v_stack_m280 == 0) goto loc_0092BCA4;
    if (v_stack_m240 == 0) goto loc_0092BCA4;
    if (v_stack_m220 != 0) goto loc_0092C33E;
loc_0092BCA4:
loc_0092BCA8:
    if ((((unsigned __int8)((unsigned int)(a7))) & (1)) != 0) goto loc_0092C4B6;
loc_0092BCB2:
    a1 = (unsigned int)(((unsigned int)(v_stack_m230)) & (0xFFFFFDFFULL));
    if (condition_is_equal) goto loc_0092BFF3;
    result = (unsigned int)(((unsigned int)((unsigned int)(a1))) & (432));
    if (((unsigned int)(result)) != ((unsigned int)(a1))) goto loc_0092BFF3;
    result = 0;
loc_0092BCD2:
    if (((unsigned __int8)(v_stack_m2B6)) != 1) goto loc_0092BD07;
    if (v_stack_m2B7 != 0) goto loc_0092C9E3;
loc_0092BCE1:
    v_rsi = 0;
loc_0092BCE7:
    if (v_stack_m20C != 0) goto loc_0092C7CA;
loc_0092BCF1:
    if (v_stack_m283 != 0) goto loc_0092C4E2;
loc_0092BCFE:
    if ((unsigned __int8)(v_stack_m284) != 0) goto loc_0092C2E4;
loc_0092BD07:
    a2 = 0;
loc_0092BD0D:
    if (v_stack_m248 == 0) goto loc_0092CAB2;
loc_0092BD36:
    if ((((unsigned __int8)(v_r13)) & (16)) == 0) goto loc_0092BF76;
    if (v_stack_m2A8 == 0) goto loc_0092BF76;
    v_rsi = (unsigned int)((*(unsigned __int16 *)(v_stack_m2A8 + 2)) + (3));
    v_rsi = (unsigned int)((v_rsi) & (0xFFFFFFFCULL));
loc_0092BD57:
    if ((((unsigned __int8)(v_r13)) & (4)) == 0) goto loc_0092C26C;
    if (v_stack_m2B0 == 0) goto loc_0092C26C;
    v_rdi = (unsigned int)((*(unsigned __int16 *)(v_stack_m2B0 + 2)) + (3));
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFFCULL));
loc_0092BD74:
    a2 = (unsigned int)((v_rdi + 20) + ((unsigned int)(v_rsi)));
    a2 = (unsigned int)((a2) + ((unsigned int)(*(unsigned __int8 *)(v_stack_m248 + 1) * 4 + 8)));
    a2 = (unsigned int)((a2) + ((unsigned int)(*(unsigned __int8 *)(v_stack_m250 + 1) * 4 + 8)));
    result = ExAllocatePool2(256, a2, (unsigned int)(0x64536553ULL), (unsigned int)(a7));
    v_stack_m290 = result;
    if (result == 0) goto loc_0092C273;
    result = 0;
    *(unsigned __int64 *)(result) = v_xmm0;
    *(unsigned int *)(result + 16) = 0;
    *(unsigned __int8 *)(result) = 1;
    if ((((unsigned __int8)(v_r13)) & (16)) == 0) goto loc_0092BEE2;
    if (v_stack_m2A8 == 0) goto loc_0092BEE2;
    v_stack_m1B8 = result + 20;
    if (((a7) & (0x4000ULL)) != 0) goto loc_0092C58D;
    result = memcpy(result + 20, v_stack_m2A8, *(unsigned __int16 *)(v_stack_m2A8 + 2), (unsigned int)(a7));
    a4 = 0;
    if (v_stack_m298 != 0) goto loc_0092BEA6;
    if (result + 20 == 0) goto loc_0092BEA6;
    if (0 >= (*(unsigned __int16 *)(result + 20 + 4))) goto loc_0092BEA6;
loc_0092BE2C:
    if (((unsigned __int8)(*(unsigned __int8 *)(result + 20 + 8))) > 10) goto loc_0092C231;
loc_0092BE37:
    if (((*(unsigned __int8 *)(result + 20 + 8 + 1)) & (8)) != 0) goto loc_0092BE8C;
    if (sign_flag) {
        a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 20 + 8 + 4))) | (*(unsigned int *)(v_stack_m238)));
    }
    if (!(condition_is_above_or_equal)) {
        a1 = (unsigned int)((a1) | (*(unsigned int *)(v_stack_m238 + 4)));
    }
    if (!(condition_is_above_or_equal)) {
        a1 = (unsigned int)((a1) | (*(unsigned int *)(v_stack_m238 + 8)));
    }
    if (!(condition_is_above_or_equal)) {
        a1 = (unsigned int)((a1) | (*(unsigned int *)(v_stack_m238 + 12)));
    }
    a1 = (unsigned int)((a1) & (0xFFFFFFFULL));
    *(unsigned int *)(result + 20 + 8 + 4) = (unsigned int)(a1);
    if (((unsigned __int8)(*(unsigned __int8 *)(result + 20 + 8))) > 10) goto loc_0092CC6A;
    if (((unsigned __int8)(*(unsigned __int8 *)(result + 20 + 8))) >= 10) goto loc_0092CC6A;
loc_0092BE87:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m238 + 12))) & ((unsigned int)(a1)));
    *(unsigned int *)(result + 20 + 8 + 4) = (unsigned int)(result);
loc_0092BE8C:
    a3 = (unsigned int)((0) + 1);
    a2 = (result + 20 + 8) + (*(unsigned __int16 *)(result + 20 + 8 + 2));
    if (((unsigned int)(a3)) < ((unsigned int)(*(unsigned __int16 *)(result + 20 + 4)))) goto loc_0092BE2C;
loc_0092BEA6:
    result = v_stack_m2A8;
    if (((unsigned int)(v_rsi)) >= = ((unsigned int)(*(unsigned __int16 *)(v_stack_m2A8 + 2)))) {
        a3 = (unsigned int)(v_rsi);
        a2 = 0;
        a3 = (unsigned int)((a3) - ((unsigned int)(*(unsigned __int16 *)(v_stack_m2A8 + 2))));
        a1 = (*(unsigned __int16 *)(v_stack_m2A8 + 2)) + (result + 20);
        result = memset(a1, a2, a3, a4);
        a4 = 0;
    }
    if (v_stack_m1B8 == 0) goto loc_0092CBBE;
    v_rbx = (result + 20) + ((unsigned int)((unsigned int)(v_rsi)));
    v_r14 = (unsigned int)((v_stack_m1B8) - ((unsigned int)(v_stack_m290)));
loc_0092BEDA:
    *(unsigned int *)(v_stack_m290 + 12) = (unsigned int)(v_r14);
loc_0092BEE2:
    if ((((unsigned __int8)(v_r13)) & (4)) == 0) goto loc_0092C458;
    if (v_stack_m2B0 == 0) goto loc_0092C452;
    if (((a7) & (0x4000ULL)) != 0) goto loc_0092C490;
    result = memcpy(v_rbx, v_stack_m2B0, *(unsigned __int16 *)(v_stack_m2B0 + 2), a4);
    if ((unsigned __int8)(v_stack_m2B8) != 0) goto loc_0092B4A0;
    if (v_rbx == 0) goto loc_0092B4A0;
    result = 0;
    if (0 >= (*(unsigned __int16 *)(v_rbx + 4))) goto loc_0092B4A0;
loc_0092BF4D:
    if (((unsigned __int8)(*(unsigned __int8 *)(v_rbx + 8))) > 10) goto loc_0092BFFA;
loc_0092BF58:
    if (((*(unsigned __int8 *)(v_rbx + 8 + 1)) & (8)) == 0) goto loc_0092BF9F;
loc_0092BF5E:
    a3 = (unsigned int)((0) + 1);
    a2 = (v_rbx + 8) + (*(unsigned __int16 *)(v_rbx + 8 + 2));
    if (((unsigned int)(a3)) < ((unsigned int)(*(unsigned __int16 *)(v_rbx + 4)))) goto loc_0092BF4D;
    goto loc_0092B497;
loc_0092BF76:
    goto loc_0092BD57;
loc_0092BF7D:
    a1 = (v_stack_m138) + ((unsigned int)(0x673ULL));
    if (a2 >= a1) goto loc_0092CC2C;
    a3 = (unsigned int)((a3) + 1);
    a2 = (a2) + (*(unsigned __int16 *)(a2 + 2));
    goto loc_0092B9CC;
loc_0092BF9F:
    if (sign_flag) {
        a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 4))) | (*(unsigned int *)(v_stack_m238)));
    }
    if (!(condition_is_above_or_equal)) {
        a1 = (unsigned int)((a1) | (*(unsigned int *)(v_stack_m238 + 4)));
    }
    if (!(condition_is_above_or_equal)) {
        a1 = (unsigned int)((a1) | (*(unsigned int *)(v_stack_m238 + 8)));
    }
    if (!(condition_is_above_or_equal)) {
        a1 = (unsigned int)((a1) | (*(unsigned int *)(v_stack_m238 + 12)));
    }
    a1 = (unsigned int)((a1) & (0xFFFFFFFULL));
    *(unsigned int *)(a2 + 4) = (unsigned int)(a1);
    if (((unsigned __int8)(*(unsigned __int8 *)(a2))) > 10) goto loc_0092CC5D;
    if (((unsigned __int8)(*(unsigned __int8 *)(a2))) >= 10) goto loc_0092CC5D;
loc_0092BFE9:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m238 + 12))) & ((unsigned int)(a1)));
    *(unsigned int *)(a2 + 4) = (unsigned int)(result);
    goto loc_0092BF5E;
loc_0092BFF3:
    goto loc_0092BCD2;
loc_0092BFFA:
    result = (unsigned __int8)((1) - (13));
    if (((unsigned __int8)(result)) > 1) goto loc_0092BF5E;
    goto loc_0092BF58;
loc_0092C009:
    v_stack_m29C = 200;
loc_0092C014:
    if (((unsigned int)((unsigned int)((unsigned int)(a2)))) >= 2) goto loc_0092C0F0;
    result = ExAllocatePool2(256, 200, (unsigned int)(0x63416553ULL), a4);
    if (result == 0) goto loc_0092B848;
    v_stack_m2C0 = v_stack_m278;
    v_stack_m2C8 = v_stack_m267;
    v_stack_m2D0 = result;
    v_stack_m2D8 = v_stack_m29C;
    v_stack_m2E0 = (unsigned int)((unsigned int)(a5));
    v_stack_m2E8 = v_stack_m1F0;
    v_stack_m2F0 = 3;
    v_stack_m2F8 = v_stack_m238;
    v_stack_m300 = v_stack_m1F8;
    v_stack_m308 = v_stack_m218;
    v_stack_m310 = v_stack_m248;
    v_stack_m318 = v_stack_m250;
    v_stack_m320 = 0;
    v_stack_m328 = 1;
    result = RtlpInheritAcl2(v_rdi, v_stack_m1E0, (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_stack_m248 + 1) * 4 + 8)), a6);
    if (sign_flag) goto loc_0092C297;
    if (v_stack_m29C != 0) goto loc_0092C5F3;
    a2 = 0;
    result = ExFreePoolWithTag(result, a2, (unsigned int)((unsigned int)(*(unsigned __int8 *)(v_stack_m248 + 1) * 4 + 8)), a6);
    a2 = 0;
loc_0092C0F0:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) == 0x8000000BULL) goto loc_0092BA88;
    if (sign_flag) goto loc_0092B84D;
    goto loc_0092BA94;
loc_0092C110:
    v_stack_m29C = 200;
loc_0092C11B:
    if (0 >= 2) goto loc_0092C1FD;
    result = ExAllocatePool2(256, 200, (unsigned int)(0x63416553ULL), a6);
    v_stack_m2B0 = result;
    if (result == 0) goto loc_0092CC77;
    v_stack_m2C0 = v_stack_m278;
    v_stack_m2C8 = v_stack_m284;
    v_stack_m2D0 = result;
    v_stack_m2D8 = v_stack_m29C;
    v_stack_m2E0 = (unsigned int)((unsigned int)(a5));
    v_stack_m2E8 = v_stack_m1F0;
    v_stack_m2F0 = 1;
    v_stack_m2F8 = v_stack_m238;
    v_stack_m300 = v_stack_m1F8;
    v_stack_m308 = v_stack_m218;
    v_stack_m310 = v_stack_m248;
    v_stack_m318 = v_stack_m250;
    v_stack_m320 = (unsigned __int8)((unsigned int)(v_stack_m278));
    v_stack_m328 = (unsigned __int8)(*(unsigned __int8 *)(v_stack_m248 + 1) * 4 + 8);
    result = RtlpInheritAcl2(v_stack_m1E0, (unsigned int)(0x673ULL), 0, a6);
    if (sign_flag) goto loc_0092C2BC;
    if (v_stack_m29C != 0) goto loc_0092C5FA;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m2B0, a2, 0, a6);
    v_r11 = 0;
loc_0092C1FD:
    v_stack_m2B0 = 0;
    if (!sign_flag) goto loc_0092BC5D;
    v_stack_m2B0 = 0;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0x8000000BULL) goto loc_0092C520;
    goto loc_0092BC07;
loc_0092C231:
    result = (unsigned __int8)((result) - (13));
    if (((unsigned __int8)(result)) > 1) goto loc_0092BE8C;
    goto loc_0092BE37;
loc_0092C240:
    if (v_stack_m1E0 != 0) goto loc_0092C24E;
    if (v_stack_m2B0 != 0) goto loc_0092C336;
loc_0092C24E:
    result = (unsigned int)((*(unsigned __int16 *)(v_stack_m284 + 2)) & (0x2800ULL));
    v_r15 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m284 + 2)))) >> (1));
    v_r15 = (unsigned int)((v_r15) & (24));
    v_r15 = (unsigned int)((v_r15) | ((unsigned int)(result)));
    v_r15 = (unsigned int)((v_r15) >> (1));
    goto loc_0092BA64;
loc_0092C26C:
    goto loc_0092BD74;
loc_0092C273:
    goto loc_0092B50A;
loc_0092C28A:
    a2 = 0;
    v_stack_m1E0 = 0;
    goto loc_0092BA53;
loc_0092C297:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m2B0, a2, 0, (unsigned int)(a7));
    a2 = 0;
    if (((unsigned int)((unsigned int)(0xC000009AULL))) != 0xC0000023ULL) goto loc_0092C0F0;
    v_r14 = (unsigned int)((v_stack_m1E0) + 1);
    goto loc_0092C014;
loc_0092C2BC:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m2B0, a2, 0, (unsigned int)(a7));
    v_r11 = 0;
    if (((unsigned int)((unsigned int)(0xC000009AULL))) != 0xC0000023ULL) goto loc_0092C1FD;
    v_r12 = (unsigned int)((0) + 1);
    goto loc_0092C11B;
loc_0092C2E4:
    if ((unsigned __int8)((unsigned int)(0xC000009AULL)) == 0) goto loc_0092BD07;
    v_stack_m328 = v_stack_m27F;
    result = RtlpCreateServerAcl(v_stack_m2B0, v_stack_m1B0, v_stack_m218, v_stack_m1C8);
    if (sign_flag) goto loc_0092CD2E;
    if ((unsigned __int8)(v_stack_m2A8) != 0) goto loc_0092C533;
loc_0092C323:
    a2 = 0;
    v_stack_m2B0 = v_stack_m1C8;
    v_stack_m1C8 = 0;
    goto loc_0092BD0D;
loc_0092C336:
    goto loc_0092BA64;
loc_0092C33E:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_stack_m1C8))) | (1));
    v_stack_m2F8 = 0;
    a2 = 0;
    v_stack_m300 = v_stack_m1A0;
    v_stack_m308 = v_stack_m238;
    v_stack_m310 = v_r14;
    v_stack_m318 = (unsigned int)(result);
    v_stack_m320 = a6;
    v_stack_m328 = (unsigned int)((unsigned int)(a5));
    v_stack_m29C = 0;
    v_stack_m210 = 0;
    result = RtlpNewSecurityObject(v_stack_m220, a2, v_stack_m200, v_stack_m1F0);
    if (sign_flag) goto loc_0092C50D;
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_m200 + 2))) & (4)) != 0) goto loc_0092C46B;
    v_r12 = 0;
loc_0092C3B7:
    result = RtlpOwnerAcesPresent(16, 0, v_stack_m200, v_stack_m1F0);
    if ((unsigned __int8)(result) != 0) goto loc_0092C660;
loc_0092C3CA:
    goto loc_0092BCA8;
loc_0092C3DA:
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_m220 + 2))) & (4)) == 0) goto loc_0092BBDE;
    if (!sign_flag) goto loc_0092CACE;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m220 + 16))) == 0) goto loc_0092BBDE;
    goto loc_0092BBE1;
loc_0092C405:
    if ((((unsigned __int8)(*(unsigned __int16 *)(16 + 2))) & (16)) == 0) goto loc_0092BA71;
    if (!sign_flag) goto loc_0092C6AC;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(16 + 12))) == 0) goto loc_0092BA71;
    goto loc_0092BA74;
loc_0092C42E:
    if (0 == 0) goto loc_0092C449;
    a2 = 0;
    result = RtlSubAuthoritySid(0, a2, v_stack_m2B0, (unsigned int)(a7));
    if ((*(unsigned int *)(result)) < 0x2000ULL) goto loc_0092CD0A;
loc_0092C449:
    goto loc_0092B8FD;
loc_0092C452:
    result = 0;
    *(unsigned int *)(v_stack_m220 + (unsigned int)(*(unsigned int *)(v_stack_m220 + 16)) * 1 + 16) = 0;
loc_0092C458:
    goto loc_0092B4C6;
loc_0092C462:
    goto loc_0092BBD1;
loc_0092C46B:
    if (!sign_flag) goto loc_0092CA6A;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m200 + 16))) == 0) goto loc_0092CBD3;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m200 + 16))))) + (v_stack_m200);
loc_0092C488:
    v_r12 = 0;
    goto loc_0092C3B7;
loc_0092C490:
    a3 = v_stack_m238;
    if ((unsigned __int8)(v_stack_m2B8) != 0) { a3 = 0; }
    result = RtlpNormalizeAcl(v_stack_m2B6, a2, a3, (unsigned int)(a7));
    goto loc_0092B4B8;
loc_0092C4B6:
    if (a3 != 0) goto loc_0092BCB2;
    goto loc_0092BCB2;
loc_0092C4C9:
    v_r13 = 0;
    goto loc_0092B50A;
loc_0092C4E2:
    if ((((unsigned __int8)((unsigned int)(a7))) & (16)) != 0) goto loc_0092BCFE;
    result = SepValidOwnerSubjectContext(v_stack_m290, v_stack_m250, (unsigned __int8)((unsigned int)(0xC0000078ULL)), (unsigned int)(a7));
    if ((unsigned __int8)(result) != 0) goto loc_0092BCFE;
loc_0092C50D:
    goto loc_0092B691;
loc_0092C517:
    goto loc_0092B204;
loc_0092C520:
    v_r13 = 0;
    goto loc_0092B50A;
loc_0092C533:
    if ((unsigned __int8)((unsigned int)(0xC0000078ULL)) == 0) goto loc_0092C323;
    a2 = 0;
    result = ExFreePoolWithTag((unsigned __int8)((unsigned int)(0xC0000078ULL)), a2, (unsigned __int8)((unsigned int)(0xC0000078ULL)), (unsigned int)(a7));
    goto loc_0092C323;
loc_0092C54B:
    if ((unsigned __int8)((unsigned int)(0xC0000078ULL)) != 0) goto loc_0092C955;
    v_r13 = 0;
    goto loc_0092B50A;
loc_0092C56C:
    v_r13 = 0;
    goto loc_0092B50A;
loc_0092C585:
    goto loc_0092BBD1;
loc_0092C58D:
    a3 = v_stack_m238;
    if (v_stack_m298 != 0) { a3 = 0; }
    result = RtlpNormalizeAcl((unsigned int)(0xC0000099ULL), a2, a3, (unsigned int)(a7));
    a4 = 0;
    if ((*(unsigned __int16 *)((unsigned int)(0xC0000099ULL) + 4)) == 0) goto loc_0092CABA;
    goto loc_0092BEC5;
loc_0092C5BD:
    v_stack_m2A0 = (unsigned __int8)((unsigned int)(0xC0000099ULL));
    a2 = 0;
    v_stack_m208 = *(unsigned __int16 *)((unsigned int)(0xC0000099ULL) + 2);
    result = RtlSubAuthoritySid(0, a2, a3, a4);
    if ((*(unsigned int *)(result)) >= 0x2000ULL) goto loc_0092B8D7;
    v_r13 = 0;
    goto loc_0092B50A;
loc_0092C5F3:
    a2 = 0;
    goto loc_0092C0F0;
loc_0092C5FA:
    v_r11 = 0;
    goto loc_0092C1FD;
loc_0092C606:
    if (v_stack_m1C8 == 0) goto loc_0092B524;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m1C8, a2, v_stack_m2B0, a4);
    goto loc_0092B524;
loc_0092C61F:
    if (v_stack_m2B0 == 0) goto loc_0092CCBF;
    if ((*(unsigned __int16 *)(v_stack_m2B0 + 2)) < 0) goto loc_0092CB00;
loc_0092C637:
    v_stack_m250 = *(unsigned __int64 *)(v_stack_m2B0 + 8);
    v_stack_m283 = 1;
    if (*(unsigned __int64 *)(v_stack_m2B0 + 8) != 0) goto loc_0092AFD7;
loc_0092C648:
    v_r13 = 0;
    goto loc_0092B50A;
loc_0092C660:
    v_stack_m300 = v_stack_m210;
    a3 = 0;
    v_stack_m308 = v_stack_m29C;
    v_stack_m310 = (unsigned __int8)((unsigned int)(0xC000005AULL));
    v_stack_m318 = v_stack_m2B0;
    v_stack_m320 = 0;
    v_stack_m328 = 0;
    result = SeAccessCheck(v_stack_m200, v_stack_m290, a3, (unsigned int)(0x40000ULL));
    if ((unsigned __int8)(result) != 0) goto loc_0092C3CA;
    goto loc_0092C50D;
loc_0092C6AC:
    goto loc_0092BA74;
loc_0092C6B5:
    if (v_stack_m2B0 == 0) goto loc_0092BB18;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m2B0, a2, a3, (unsigned int)(0x40000ULL));
    goto loc_0092BB18;
loc_0092C6D1:
    v_r13 = 0;
    goto loc_0092B50A;
loc_0092C6EA:
    if (v_stack_m270 == 0) goto loc_0092B54A;
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m270, a2, a3, (unsigned int)(0x40000ULL));
    goto loc_0092B54A;
loc_0092C706:
    if ((((unsigned __int8)(v_stack_m270)) & (4)) != 0) goto loc_0092C798;
loc_0092C712:
    a1 = (unsigned int)((v_stack_m270) & (0x1000ULL));
    v_stack_m2B0 = 0;
    a1 = (unsigned int)((a1) | (4));
    v_r13 = (unsigned int)((v_r13) | ((unsigned int)(a1)));
    v_r15 = 0;
    goto loc_0092BC85;
loc_0092C72D:
    if ((((unsigned __int8)(v_r13)) & (16)) != 0) goto loc_0092C974;
    v_stack_m2A8 = v_stack_m290;
loc_0092C73B:
    v_r13 = (unsigned int)((v_r13) & (0x2000ULL));
    v_stack_m2B7 = 1;
    v_r13 = (unsigned int)((v_r13) | ((unsigned int)(a1)));
    v_r13 = (unsigned int)((v_r13) | (16));
    v_stack_m260 = (unsigned int)(v_r13);
    goto loc_0092B10D;
loc_0092C756:
    if ((((unsigned __int8)(a1)) & (16)) != 0) goto loc_0092C996;
    v_stack_m270 = v_stack_m290;
    goto loc_0092B1F8;
loc_0092C768:
    goto loc_0092B069;
loc_0092C771:
    goto loc_0092B739;
loc_0092C77A:
    goto loc_0092BB6D;
loc_0092C783:
    goto loc_0092AD8C;
loc_0092C78F:
    goto loc_0092B214;
loc_0092C798:
    if (!sign_flag) goto loc_0092CBCA;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m208 + 16))) != 0) goto loc_0092CA95;
    goto loc_0092C712;
loc_0092C7B4:
    if (v_stack_m27C == 0) goto loc_0092B557;
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_r11 + 24), a2, 0, (unsigned int)(0x40000ULL));
    goto loc_0092B557;
loc_0092C7CA:
    if ((((unsigned __int8)((unsigned int)(0x40000ULL))) & (8)) != 0) goto loc_0092BCF1;
    if (v_stack_m290 == 0) goto loc_0092CC8F;
    v_stack_m150 = *(unsigned __int64 *)(v_rip + 7000900);
    v_stack_m158 = 0;
    v_stack_m154 = 0;
    v_stack_m148 = (unsigned int)(v_stack_m2B0);
    result = SePrivilegeCheck(v_stack_m158, v_stack_m290, 1, (unsigned int)(0x40000ULL));
    a1 = 0;
    result = SePrivilegedServiceAuditAlarm(a1, v_stack_m290, v_stack_m158, (unsigned __int8)(result));
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_0092BCF1;
    goto loc_0092B691;
loc_0092C840:
    v_stack_m288 = 1;
loc_0092C847:
    v_rbx = 0;
    if ((((unsigned __int8)(*(unsigned __int16 *)(v_stack_m258 + 2))) & (16)) != 0) goto loc_0092C9B4;
loc_0092C857:
    result = RtlFindAceByType(0, 20, v_stack_m288, (unsigned __int8)(result));
    if (result != 0) goto loc_0092CBDE;
    if (0 == 0) goto loc_0092B25D;
    if (v_stack_m1A0 == 0) goto loc_0092CCD3;
loc_0092C893:
    result = RtlCreateAcl(v_stack_mB8, 88, 88 - 86, (unsigned __int8)(result));
    if (sign_flag) goto loc_0092B84D;
    v_stack_m320 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m1A0 + 4)));
    v_stack_m328 = 20;
    result = RtlAddProcessTrustLabelAce(v_stack_mB8, 2, 0, 0);
    if (sign_flag) goto loc_0092B84D;
    result = (unsigned int)((*(unsigned __int16 *)(v_stack_m258 + 2)) & (0x800ULL));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_stack_m258 + 2)))) >> (1));
    a2 = (unsigned int)((a2) & (24));
    a2 = (unsigned int)((a2) | ((unsigned int)(result)));
    v_stack_m300 = v_stack_m278;
    v_stack_m308 = v_stack_m1C0;
    v_stack_m310 = 2;
    v_stack_m318 = v_stack_m238;
    v_stack_m320 = v_stack_m248;
    a2 = (unsigned int)((a2) >> (1));
    v_stack_m328 = v_stack_m250;
    result = RtlpComputeMergedAcl(v_stack_m270, a2, v_stack_mB8, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rip + 5486118))));
    if (sign_flag) goto loc_0092B84D;
    v_stack_m27C = 1;
    goto loc_0092B261;
loc_0092C955:
    if ((*(unsigned __int16 *)((unsigned int)(a7) + 2)) >= 0) goto loc_0092CB13;
    if ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(a7) + 8))) == 0) goto loc_0092B830;
    goto loc_0092B000;
loc_0092C974:
    if (!sign_flag) goto loc_0092CB2E;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 12))) == 0) goto loc_0092CB25;
    result = ((unsigned int)(*(unsigned int *)(v_r11 + 12))) + (0);
loc_0092C98D:
    v_stack_m2A8 = result;
    goto loc_0092C73B;
loc_0092C996:
    if (!sign_flag) goto loc_0092CB44;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r11 + 12))) != 0) goto loc_0092CB37;
    v_stack_m270 = 0;
    goto loc_0092B1F8;
loc_0092C9B4:
    if (!sign_flag) goto loc_0092CB86;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m258 + 12))) != 0) goto loc_0092CB7D;
    goto loc_0092C857;
loc_0092C9D0:
    goto loc_0092ADDD;
loc_0092C9D8:
    goto loc_0092ADCF;
loc_0092C9E3:
    if (((24) & (8)) != 0) goto loc_0092BCE1;
    if ((unsigned __int8)((unsigned int)(*(unsigned int *)(v_stack_m258 + 12))) == 0) goto loc_0092BCE1;
    if (0 == 0) goto loc_0092CC8F;
    v_stack_m150 = *(unsigned __int64 *)(v_rip + 7000315);
    v_rsi = 0;
    v_stack_m158 = 1;
    v_stack_m154 = 1;
    v_stack_m148 = 0;
    result = SePrivilegeCheck(v_stack_m158, 0, 1, 24);
    a1 = 0;
    result = SePrivilegedServiceAuditAlarm(a1, 0, v_stack_m158, (unsigned __int8)(result));
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) goto loc_0092CC20;
    goto loc_0092B691;
loc_0092CA6A:
    goto loc_0092C488;
loc_0092CA73:
    goto loc_0092B271;
loc_0092CA7C:
    v_stack_m1D0 = *(unsigned __int64 *)(v_stack_m258 + 24);
    goto loc_0092AF3A;
loc_0092CA85:
    goto loc_0092AEBE;
loc_0092CA8D:
    goto loc_0092ADBA;
loc_0092CA95:
    goto loc_0092C712;
loc_0092CA9E:
    goto loc_0092B214;
loc_0092CAA6:
    v_stack_m1F8 = *(unsigned __int64 *)(v_stack_m258 + 24);
    goto loc_0092AF21;
loc_0092CAB2:
    goto loc_0092BD36;
loc_0092CABA:
    goto loc_0092BEC5;
loc_0092CAC5:
    goto loc_0092B14B;
loc_0092CACE:
    goto loc_0092BBE1;
loc_0092CAD7:
    goto loc_0092B069;
loc_0092CADF:
    goto loc_0092B15B;
loc_0092CAE8:
    goto loc_0092B14B;
loc_0092CAF0:
    goto loc_0092B739;
loc_0092CAF8:
    goto loc_0092B271;
loc_0092CB00:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 24) + 4))) == 0) goto loc_0092C648;
    result = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 24) + 4))) + (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 24));
    goto loc_0092C637;
loc_0092CB13:
    goto loc_0092B000;
loc_0092CB1C:
    goto loc_0092B075;
loc_0092CB25:
    v_stack_m2A8 = *(unsigned __int64 *)(0 + 32);
    goto loc_0092C73B;
loc_0092CB2E:
    goto loc_0092C98D;
loc_0092CB37:
    v_stack_m270 = v_r11 + *(unsigned __int64 *)(v_r11 + 24) * 1;
    goto loc_0092B1F8;
loc_0092CB44:
    v_stack_m270 = *(unsigned __int64 *)(v_r11 + 24);
    goto loc_0092B1F8;
loc_0092CB51:
    result = RtlpValidTrustSubjectContext(*(unsigned __int64 *)(0 + 32), *(unsigned __int64 *)(result + 32), *(unsigned __int64 *)(result + 32) + result * 1, v_stack_m29C);
    if ((unsigned __int8)(result) != 0) goto loc_0092B239;
    v_r13 = 0;
    goto loc_0092B50A;
loc_0092CB7D:
    goto loc_0092C857;
loc_0092CB86:
    goto loc_0092C857;
loc_0092CB8F:
    v_stack_m208 = *(unsigned __int64 *)(0 + 32);
    v_stack_m2A0 = 0;
    goto loc_0092B8D7;
loc_0092CBA9:
    v_r13 = 0;
    goto loc_0092B50A;
loc_0092CBBE:
    goto loc_0092BEDA;
loc_0092CBCA:
    goto loc_0092C712;
loc_0092CBD3:
    v_r12 = 0;
    goto loc_0092C3B7;
loc_0092CBDE:
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_m290 + 1))) & (8)) != 0) goto loc_0092C847;
    if (v_stack_m1A0 == 0) goto loc_0092B689;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m1A0 + 4))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m290 + 4)))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m290 + 4))))) goto loc_0092B689;
    if (v_stack_m290 + 8 != 0) goto loc_0092C893;
    goto loc_0092B689;
loc_0092CC20:
    goto loc_0092BCE7;
loc_0092CC2C:
    v_r13 = 0;
    goto loc_0092B50A;
loc_0092CC45:
loc_0092CC4D:
    v_r13 = 0;
    goto loc_0092B50A;
loc_0092CC5D:
    goto loc_0092BFE9;
loc_0092CC6A:
    goto loc_0092BE87;
loc_0092CC77:
    v_r13 = 0;
    goto loc_0092B50A;
loc_0092CC8F:
    goto loc_0092C50D;
loc_0092CC99:
    if (((*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_m290 + 12)) + 4)) & (0xFF000000ULL)) == 0) goto loc_0092CCE0;
    goto loc_0092B2B2;
loc_0092CCAC:
    v_rbx = (unsigned __int8)((unsigned int)(0xC000000DULL));
    if ((*(unsigned int *)((unsigned int)(*(unsigned int *)(v_stack_m290 + 4)) + 8)) == 0) { v_rbx = 0; }
    v_stack_m264 = (unsigned int)(v_rbx);
    goto loc_0092AD36;
loc_0092CCBF:
    v_r13 = 0;
    goto loc_0092B699;
loc_0092CCD3:
    v_r13 = 0;
    goto loc_0092B691;
loc_0092CCE0:
    result = RtlpValidTrustSubjectContext(0, (unsigned int)(*(unsigned int *)(v_stack_m290 + 12)) + 8, *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 32), v_stack_m29C);
    goto loc_0092B28A;
loc_0092CD0A:
    goto loc_0092B8DF;
loc_0092CD14:
    v_r13 = 0;
    goto loc_0092B691;
loc_0092CD21:
    v_r13 = 0;
    goto loc_0092B691;
loc_0092CD2E:
    goto loc_0092B699;
loc_0092CD3C:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(*(unsigned int *)(v_stack_m290 + 12)) + 8, *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 32), v_stack_m29C);
    v_rsp = (v_rsp) + (776);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpNewSecurityObject(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint8_t Arg6, uint32_t Arg7, int64_t Arg8, int64_t Arg9, int64_t Arg10, int64_t Arg11)
{
    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m130;
    uint16_t v_stack_m134;
    uint16_t v_stack_m136;
    uint64_t v_stack_m138;
    uint32_t v_stack_m148;
    uint64_t v_stack_m150;
    uint32_t v_stack_m154;
    uint64_t v_stack_m158;
    uint16_t v_stack_m15C;
    uint32_t v_stack_m160;
    uint16_t v_stack_m164;
    uint32_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m180;
    uint64_t v_stack_m190;
    uint64_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint64_t v_stack_m1A8;
    uint32_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint64_t v_stack_m1C0;
    uint64_t v_stack_m1C8;
    uint64_t v_stack_m1D0;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E0;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F0;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m200;
    uint64_t v_stack_m208;
    uint8_t v_stack_m20C;
    uint32_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint32_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint32_t v_stack_m260;
    uint8_t v_stack_m264;
    uint8_t v_stack_m267;
    uint8_t v_stack_m268;
    uint64_t v_stack_m270;
    uint32_t v_stack_m278;
    uint8_t v_stack_m27C;
    uint8_t v_stack_m27D;
    uint8_t v_stack_m27E;
    uint8_t v_stack_m27F;
    uint8_t v_stack_m280;
    uint8_t v_stack_m281;
    uint8_t v_stack_m282;
    uint8_t v_stack_m283;
    uint8_t v_stack_m284;
    uint32_t v_stack_m288;
    uint64_t v_stack_m290;
    uint8_t v_stack_m298;
    uint32_t v_stack_m29C;
    uint8_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m2B0;
    uint8_t v_stack_m2B6;
    uint8_t v_stack_m2B7;
    uint8_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint32_t v_stack_m2E0;
    uint64_t v_stack_m2E8;
    uint32_t v_stack_m2F0;
    uint64_t v_stack_m2F8;
    uint64_t v_stack_m300;
    uint64_t v_stack_m308;
    uint64_t v_stack_m310;
    uint64_t v_stack_m318;
    uint8_t v_stack_m320;
    uint8_t v_stack_m328;
    uint64_t v_stack_m58;
    uint64_t v_stack_mB8;

    local_rsp = (local_rsp) - (776);
    result = (*(uint64_t *)(v_rip + 0x4DFBCD)) ^ (local_rsp);
    v_stack_m58 = result;
    v_stack_m238 = Arg9;
    v_stack_m1A0 = Arg10;
    v_stack_m1B8 = Arg11;
    result = 0;
    v_stack_m198 = Arg3;
    Arg3 = 0;
    v_stack_m170 = 0;
    v_stack_m298 = 0;
    v_stack_m27D = 0;
    v_stack_m27E = 0;
    v_stack_m2B8 = 0;
    v_stack_m283 = 0;
    v_stack_m2B7 = 0;
    v_stack_m268 = 0;
    v_stack_m267 = 0;
    v_stack_m284 = 0;
    v_stack_m20C = 0;
    v_stack_m27F = 0;
    v_stack_m148 = 0;
    v_stack_m220 = Arg1;
    v_stack_m1F0 = Arg4;
    v_stack_m1E0 = v_stack_m138;
    v_stack_m258 = Arg2;
    v_stack_m240 = Arg8;
    v_stack_m270 = 0;
    v_stack_m230 = 0;
    v_stack_m2B0 = 0;
    v_stack_m1C8 = 0;
    v_stack_m1E8 = 0;
    v_stack_m228 = 0;
    v_stack_m1A8 = 0;
    v_stack_m218 = 0;
    v_stack_m1F8 = 0;
    v_stack_m1D0 = 0;
    v_stack_m290 = 0;
    v_stack_m2B6 = 1;
    v_stack_m278 = 0;
    v_stack_m210 = 0;
    v_stack_m208 = 0;
    v_stack_m1D8 = 0;
    v_stack_m2A0 = 0;
    v_stack_m200 = 0;
    v_stack_m281 = 1;
    v_stack_m1C0 = 0;
    v_stack_m27C = 0;
    v_stack_m190 = v_xmm0;
    v_stack_m180 = v_xmm0;
    v_stack_m158 = v_xmm0;
    result = v_stack_m138;
    if (!(condition_is_below)) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        result = *(uint8_t *)(result + 0x232);
        v_stack_m2B6 = (uint8_t)(result);
    }
    if (Arg2 == 0) goto loc_0092B17F;
    v_stack_m280 = 1;
loc_0092ACAD:
    result = (uint16_t)(((uint16_t)(*(uint16_t *)(Arg2 + 0x2))) & (128));
    local_rbx = (condition_is_not_equal) ? 1 : 0;
    Arg2 = (uint8_t)((*(uint16_t *)(Arg2 + 0x2)) >> (6));
    Arg2 = (uint8_t)((Arg2) & (1));
    v_stack_m1B0 = (uint32_t)(Arg2);
    if (Arg8 == 0) goto loc_0092B81A;
loc_0092ACDB:
    result = ExAcquireResourceSharedLite(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0x30), (uint8_t)(128 - 127), 128, 0);
    if ((*(uint64_t *)(Arg8)) != 0) {
        result = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg2 = (uint8_t)(128 - 127);
        Arg1 = *(uint64_t *)(Arg8);
        Arg1 = *(uint64_t *)(Arg1 + 0x30);
        result = ExAcquireResourceSharedLite(Arg1, Arg2, 128, 0);
    }
    v_stack_m264 = (uint8_t)(local_rbx);
    if (*(uint64_t *)(Arg8) != 0) goto loc_0092CCAC;
loc_0092AD36:
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg8 + 0x10) + 0x90))) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg8 + 0x10) + 0x90)));
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg8 + 0x10) + 0x90))) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg8 + 0x10) + 0x90)));
    result = SepLocateTokenIntegrity(*(uint64_t *)(Arg8 + 0x10), *(uint64_t *)(Arg8 + 0x10), *(uint64_t *)(Arg8 + 0x10), 0);
    if (result == 0) goto loc_0092C783;
loc_0092AD8C:
    result = SepLocateTokenTrustLevel(v_stack_m240, *(uint64_t *)(Arg8 + 0x10), *(uint64_t *)(Arg8 + 0x10), 0);
    Arg1 = 0;
    if (result != 0) goto loc_0092B43E;
loc_0092ADA5:
    if (*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8) == 0) goto loc_0092CA8D;
loc_0092ADBA:
    if (*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8) == 0) goto loc_0092C9D8;
loc_0092ADCF:
    if (*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xB8) == 0) goto loc_0092C9D0;
loc_0092ADDD:
    Arg1 = (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0x98) + Arg1 * 8) + 0x1)) + (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0x98) + Arg1 * 8) + 0x1));
    Arg1 = (Arg1) + (*(uint8_t *)(*(uint64_t *)(result) + 0x1));
    Arg2 = (0 + Arg1 * 4) + (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8) + 0x1) * 4 + 8);
    Arg2 = (Arg2) + (*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xB8) + 0x2));
    Arg2 = (Arg2) + (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8) + 0x1) * 4 + 32);
    result = ExAllocatePool2(64, Arg2, (uint32_t)(0x64536553ULL), *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8) + 0x1) * 4 + 32);
    v_stack_m1E8 = result;
    if (result == 0) goto loc_0092B44F;
    result = memcpy(result, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0x98) + Arg1 * 8), *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0x98) + Arg1 * 8) + 0x1) * 4 + 8, *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8) + 0x1) * 4 + 32);
    Arg1 = (v_stack_m1E8) + (8);
    v_stack_m228 = Arg1 + *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0x98) + Arg1 * 8) + 0x1) * 4;
    result = memcpy(Arg1 + *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0x98) + Arg1 * 8) + 0x1) * 4, *(uint64_t *)(result), *(uint8_t *)(*(uint64_t *)(result) + 0x1) * 4 + 8, *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8) + 0x1) * 4 + 32);
    local_r15 = (*(uint8_t *)(*(uint64_t *)(result) + 0x1) * 4 + 8) + (Arg1 + *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0x98) + Arg1 * 8) + 0x1) * 4);
    v_stack_m218 = local_r15;
    if (result != 0) goto loc_0092B772;
    Arg1 = 0;
    v_stack_m1A8 = 0;
loc_0092AE88:
    if (*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8) == 0) goto loc_0092CA85;
    result = memcpy(local_r15, *(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8), *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8) + 0x1) * 4 + 8, *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8) + 0x1) * 4 + 32);
    local_r15 = (local_r15 + *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8) + 0x1) * 4) + (8);
    v_stack_m218 = local_r15;
    local_rbx = 0;
loc_0092AEBE:
    result = memcpy(local_r15, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0x98) + Arg1 * 8), *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0x98) + Arg1 * 8) + 0x1) * 4 + 8, *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8) + 0x1) * 4 + 32);
    local_r12 = (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0x98) + Arg1 * 8) + 0x1)) + (2);
    v_stack_m1D0 = local_r15 + local_r12 * 4;
    if (*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8) == 0) goto loc_0092CAA6;
    v_stack_m1F8 = local_r15 + local_r12 * 4;
    result = memcpy(local_r15 + local_r12 * 4, *(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8), *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8) + 0x1) * 4 + 8, *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8) + 0x1) * 4 + 32);
    local_r12 = (local_r15 + local_r12 * 4 + *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8) + 0x1) * 4) + (8);
    v_stack_m1D0 = local_r12;
loc_0092AF21:
    if (*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xB8) == 0) goto loc_0092CA7C;
    result = memcpy(local_r12, *(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xB8), *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xB8) + 0x2), *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8) + 0x1) * 4 + 32);
loc_0092AF3A:
    result = ExReleaseResourceLite(*(uint64_t *)(*(uint64_t *)(v_stack_m240 + 0x10) + 0x30), *(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xB8), *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xB8) + 0x2), *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8) + 0x1) * 4 + 32);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xB8), *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xB8) + 0x2), *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8) + 0x1) * 4 + 32);
    if (*(uint64_t *)(v_stack_m240) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_stack_m240) + 0x30);
        result = ExReleaseResourceLite(Arg1, *(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xB8), *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xB8) + 0x2), *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8) + 0x1) * 4 + 32);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = KeLeaveCriticalRegionThread(Arg1, *(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xB8), *(uint16_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xB8) + 0x2), *(uint8_t *)(*(uint64_t *)(*(uint64_t *)(Arg8 + 0x10) + 0xA8) + 0x1) * 4 + 32);
    }
loc_0092AF8E:
    if (sign_flag) goto loc_0092AFAB;
loc_0092AF9C:
    v_stack_m250 = *(uint64_t *)(v_stack_m258 + 0x8);
    if (*(uint64_t *)(v_stack_m258 + 0x8) == 0) goto loc_0092AFB7;
    v_stack_m283 = 1;
    goto loc_0092AFD7;
loc_0092AFAB:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m258 + 0x4))) != 0) goto loc_0092B861;
loc_0092AFB7:
    if ((((uint8_t)((uint32_t)(Arg7))) & (32)) != 0) goto loc_0092C61F;
    result = v_stack_m1E8;
    if ((uint8_t)((uint32_t)(v_stack_m264)) != 0) { result = local_r15; }
    v_stack_m250 = result;
    if (result == 0) goto loc_0092B75A;
loc_0092AFD7:
    if (sign_flag) goto loc_0092B6F0;
loc_0092AFE4:
    v_stack_m248 = *(uint64_t *)(v_stack_m258 + 0x10);
    if (*(uint64_t *)(v_stack_m258 + 0x10) != 0) goto loc_0092B00D;
loc_0092AFED:
    if ((((uint8_t)((uint32_t)(Arg7))) & (64)) != 0) goto loc_0092C54B;
    local_rbx = local_r15;
    if ((uint8_t)((uint32_t)(v_stack_m264)) != 0) { local_rbx = local_r15 + local_r12 * 4; }
loc_0092B000:
    v_stack_m248 = local_rbx;
    if (local_rbx == 0) goto loc_0092B830;
loc_0092B00D:
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg7)))) & (4));
    v_stack_m288 = (uint32_t)(local_r10);
    local_r13 = (condition_is_not_equal) ? 1 : 0;
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg7)))) & (2));
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(v_stack_m258 + 0x2))) & (16));
    result = (uint16_t)(-((uint16_t)(Arg1)));
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m258 + 0x2)))) >> (2));
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m258 + 0x2)))) >> (1));
    result = (uint32_t)((result) & (8));
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m258 + 0x2)))) >> (1));
    Arg3 = (uint32_t)((Arg3) & (0x400ULL));
    local_rdi = (uint32_t)((local_rdi) & (0x1000ULL));
    Arg4 = (uint32_t)((v_stack_m1E8) & (4));
    local_r14 = 0;
    if ((uint16_t)(Arg1) != 0) goto loc_0092B19A;
loc_0092B069:
    if (v_stack_m220 != 0) goto loc_0092B7C4;
loc_0092B072:
loc_0092B075:
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(Arg3)));
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(result)));
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(Arg4)));
    if (condition_is_not_equal) goto loc_0092B2F2;
    if (0 != 0) goto loc_0092B2F2;
    v_stack_m2B7 = 0;
    result = (uint32_t)(-((uint32_t)((uint32_t)(local_r12))));
    v_stack_m2A8 = 0;
    v_stack_m29C = 0x8000000BULL;
    Arg1 = (uint32_t)((Arg1) & (0x400ULL));
    v_stack_m278 = (uint32_t)(Arg1);
    goto loc_0092B0E4;
loc_0092B0B0:
loc_0092B0B4:
    local_r14 = 0;
loc_0092B0B7:
    v_stack_m2A8 = v_stack_m2A8;
    if (!sign_flag) goto loc_0092B869;
    v_stack_m2A8 = v_stack_m2A8;
    if (0 != 0x8000000BULL) goto loc_0092B676;
    v_stack_m2B7 = (uint8_t)(v_stack_m2B7);
loc_0092B0E4:
    Arg1 = (uint32_t)(0x8800ULL);
    if ((uint32_t)(local_r12) == 0) { Arg1 = (uint32_t)((uint32_t)(0x8000ULL)); }
    result = (uint8_t)(((uint8_t)(*(uint16_t *)(v_stack_m258 + 0x2))) & (48));
    if (((uint8_t)(result)) == 48) goto loc_0092C72D;
    v_stack_m260 = (uint32_t)(Arg1);
loc_0092B10D:
    local_r15 = ((uint32_t)((uint32_t)(v_stack_m288)) != 0) ? 1 : 0;
    Arg1 = (uint16_t)(((uint16_t)(*(uint16_t *)(v_stack_m258 + 0x2))) & (16));
    result = (uint16_t)(-((uint16_t)(Arg1)));
    result = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m258 + 0x2)))) >> (2));
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m258 + 0x2)))) >> (1));
    result = (uint32_t)((result) & (8));
    local_rdi = (uint32_t)((local_rdi) & (0x400ULL));
    Arg3 = (uint32_t)((Arg3) & (4));
    if ((uint16_t)(Arg1) != 0) goto loc_0092B3E5;
loc_0092B14B:
    if (v_stack_m220 != 0) goto loc_0092B7F0;
loc_0092B158:
loc_0092B15B:
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(result)));
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(Arg3)));
    if (condition_is_not_equal) goto loc_0092B583;
    if (0 != 0) goto loc_0092B583;
    v_stack_m270 = 0;
    v_stack_m29C = 0x8000000BULL;
    goto loc_0092B1E2;
loc_0092B17F:
    v_stack_m280 = (uint8_t)(Arg3);
    v_stack_m258 = v_stack_m190;
    v_stack_m190 = 1;
    goto loc_0092ACAD;
loc_0092B19A:
    if (!sign_flag) goto loc_0092C768;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m190 + 0xC))) == 0) goto loc_0092CAD7;
    goto loc_0092B069;
loc_0092B1B8:
loc_0092B1BC:
    local_r14 = 0;
loc_0092B1BF:
    v_stack_m270 = v_stack_m270;
    v_stack_m29C = 0;
    if (!sign_flag) goto loc_0092B6E0;
    v_stack_m270 = v_stack_m270;
    if (0 != 0x8000000BULL) goto loc_0092B84D;
loc_0092B1E2:
    result = (uint8_t)(((uint8_t)(*(uint16_t *)(v_stack_m258 + 0x2))) & (48));
    if (((uint8_t)(result)) == 48) goto loc_0092C756;
loc_0092B1F8:
    local_rdi = 0;
    v_stack_m288 = 0;
loc_0092B204:
    if ((((uint8_t)(*(uint16_t *)(v_stack_m258 + 0x2))) & (16)) != 0) goto loc_0092B403;
loc_0092B214:
    result = RtlFindAceByType(0, 20, v_stack_m288, v_stack_m2B7);
    Arg2 = result + 8;
    if (result == 0) { Arg2 = 0; }
    if (Arg2 != 0) goto loc_0092CB51;
loc_0092B239:
    if (result != 0) goto loc_0092C517;
    if (condition_is_below) goto loc_0092C840;
loc_0092B25D:
    v_stack_m1C0 = v_stack_m270;
loc_0092B261:
    Arg1 = 0;
    if ((((uint8_t)(*(uint16_t *)(v_stack_m258 + 0x2))) & (16)) != 0) goto loc_0092B421;
loc_0092B271:
    v_stack_m29C = 0;
    v_stack_m168 = 0;
    v_stack_m164 = 256;
    v_stack_m288 = 0;
loc_0092B28A:
    result = RtlFindAceByType(0, 21, v_stack_m288, v_stack_m2B7);
    if (result != 0) goto loc_0092CC99;
    if (result != 0) goto loc_0092B28A;
loc_0092B2B2:
    if (sign_flag) goto loc_0092B84D;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg7)))) >> (8));
    Arg1 = (uint32_t)((Arg1) & (1));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (2));
    if (condition_is_above_or_equal) { Arg2 = (uint32_t)(Arg1); }
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(Arg2))) | ((uint32_t)(result + 4)));
    if (condition_is_above_or_equal) { local_rbx = (uint32_t)(Arg2); }
    if ((uint32_t)(local_rbx) == 0) goto loc_0092B72B;
loc_0092B2E9:
    goto loc_0092B8D7;
loc_0092B2F2:
    v_stack_m29C = 200;
loc_0092B2FA:
    Arg1 = 0;
    if (((uint32_t)(v_stack_m208)) >= 2) goto loc_0092B0B4;
    result = ExAllocatePool2(256, 200, (uint32_t)(0x63416553ULL), v_stack_m2B7);
    v_stack_m2A8 = result;
    if (result == 0) goto loc_0092CC45;
    v_stack_m2C0 = v_stack_m278;
    v_stack_m2C8 = v_stack_m2B7;
    v_stack_m2D0 = result;
    v_stack_m2D8 = v_stack_m29C;
    v_stack_m2E0 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m2E8 = v_stack_m1F0;
    v_stack_m2F0 = 2;
    v_stack_m2F8 = v_stack_m238;
    v_stack_m300 = v_stack_m1F8;
    v_stack_m308 = v_stack_m218;
    v_stack_m310 = v_stack_m248;
    v_stack_m318 = v_stack_m250;
    v_stack_m320 = (uint8_t)((uint32_t)((uint32_t)(Arg1)));
    v_stack_m328 = (uint8_t)(v_stack_m282);
    result = RtlpInheritAcl2(v_stack_m208, result + 4, (uint32_t)((uint32_t)(v_stack_m258)), Arg6);
    if (sign_flag) goto loc_0092B6BA;
    if (v_stack_m29C != 0) goto loc_0092B0B0;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m2A8, Arg2, (uint32_t)((uint32_t)(v_stack_m258)), Arg6);
    local_r14 = 0;
    goto loc_0092B0B7;
loc_0092B3E5:
    if (!sign_flag) goto loc_0092CAC5;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m258 + 0xC))) == 0) goto loc_0092CAE8;
    goto loc_0092B14B;
loc_0092B403:
    if (!sign_flag) goto loc_0092C78F;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m258 + 0xC))) == 0) goto loc_0092CA9E;
    goto loc_0092B214;
loc_0092B421:
    if (!sign_flag) goto loc_0092CA73;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m258 + 0xC))) == 0) goto loc_0092CAF8;
    goto loc_0092B271;
loc_0092B43E:
    goto loc_0092ADA5;
loc_0092B44F:
    result = ExReleaseResourceLite(*(uint64_t *)(*(uint64_t *)(v_stack_m240 + 0x10) + 0x30), *(uint8_t *)((uint32_t)(*(uint32_t *)(v_stack_m258 + 0xC)) + 0x1) * 4 + 8, (uint32_t)((uint32_t)(v_stack_m258)), Arg6);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint8_t *)((uint32_t)(*(uint32_t *)(v_stack_m258 + 0xC)) + 0x1) * 4 + 8, (uint32_t)((uint32_t)(v_stack_m258)), Arg6);
    if (*(uint64_t *)(v_stack_m240) != 0) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_stack_m240) + 0x30);
        result = ExReleaseResourceLite(Arg1, *(uint8_t *)((uint32_t)(*(uint32_t *)(v_stack_m258 + 0xC)) + 0x1) * 4 + 8, (uint32_t)((uint32_t)(v_stack_m258)), Arg6);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = KeLeaveCriticalRegionThread(Arg1, *(uint8_t *)((uint32_t)(*(uint32_t *)(v_stack_m258 + 0xC)) + 0x1) * 4 + 8, (uint32_t)((uint32_t)(v_stack_m258)), Arg6);
    }
    goto loc_0092CD3C;
loc_0092B497:
loc_0092B4A0:
    result = (uint32_t)(0xC000009AULL);
    if (((uint32_t)(v_stack_m258)) >= = ((uint32_t)(*(uint16_t *)(v_stack_m208 + 0x2)))) {
        Arg3 = (uint32_t)(v_stack_m258);
        Arg2 = 0;
        Arg3 = (uint32_t)((Arg3) - ((uint32_t)(*(uint16_t *)(v_stack_m208 + 0x2))));
        Arg1 = (*(uint16_t *)(v_stack_m208 + 0x2)) + (v_stack_m240);
        result = memset(Arg1, Arg2, Arg3, Arg6);
    }
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m240))) - ((uint32_t)(v_stack_m290)));
    *(uint32_t *)(v_stack_m290 + 0x10) = (uint32_t)(result);
    local_rbx = (v_stack_m240) + ((uint32_t)((uint32_t)(v_stack_m258)));
loc_0092B4C6:
    result = memcpy(local_rbx, v_stack_m250, (uint32_t)((uint32_t)(v_stack_m258 + (uint32_t)(*(uint32_t *)(v_stack_m258 + 0xC)) * 1)), Arg6);
    local_rbx = (local_rbx) + ((uint32_t)((uint32_t)(v_stack_m258 + (uint32_t)(*(uint32_t *)(v_stack_m258 + 0xC)) * 1)));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - ((uint32_t)(v_stack_m290)));
    *(uint32_t *)(v_stack_m290 + 0x4) = (uint32_t)(result);
    result = v_stack_m248;
    if (v_stack_m248 != 0) {
        Arg3 = (uint32_t)(result + 4);
        Arg2 = v_stack_m248;
        Arg1 = local_rbx;
        result = memcpy(Arg1, Arg2, Arg3, Arg6);
        local_rbx = (uint32_t)((local_rbx) - ((uint32_t)(v_stack_m290)));
        *(uint32_t *)(v_stack_m290 + 0x8) = (uint32_t)(local_rbx);
    }
    result = 0;
loc_0092B50A:
    if (v_stack_m200 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m200, Arg2, Arg3, Arg6);
    }
    if (v_stack_m27F != 0) goto loc_0092C606;
loc_0092B524:
    if (v_stack_m1E8 != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(v_stack_m1E8, Arg2, Arg3, Arg6);
    }
    if (v_stack_m298 != 0) goto loc_0092B572;
    if (v_stack_m27E != 0) goto loc_0092B572;
loc_0092B540:
    if (v_stack_m27D != 0) goto loc_0092C6EA;
loc_0092B54A:
    if (v_stack_m1C0 != 0) goto loc_0092C7B4;
loc_0092B557:
    if ((uint8_t)(v_stack_m2B8) != 0) goto loc_0092B6A2;
loc_0092B560:
    *(uint64_t *)(v_stack_m198) = v_stack_m290;
    goto loc_0092CD3C;
loc_0092B572:
    if (v_stack_m2A8 == 0) goto loc_0092B540;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m2A8, Arg2, Arg3, Arg6);
    goto loc_0092B540;
loc_0092B583:
    v_stack_m29C = 200;
loc_0092B58B:
    Arg1 = 0;
    if (((uint32_t)(v_stack_m290)) >= 2) goto loc_0092B1BC;
    result = ExAllocatePool2(256, 200, (uint32_t)(0x63416553ULL), Arg6);
    v_stack_m270 = result;
    if (result == 0) goto loc_0092B848;
    v_stack_m2C0 = v_stack_m210;
    v_stack_m2C8 = v_stack_m268;
    v_stack_m2D0 = result;
    v_stack_m2D8 = v_stack_m29C;
    v_stack_m2E0 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m2E8 = v_stack_m1F0;
    v_stack_m2F0 = 2;
    v_stack_m2F8 = v_stack_m238;
    v_stack_m300 = v_stack_m1F8;
    v_stack_m308 = v_stack_m218;
    v_stack_m310 = v_stack_m248;
    v_stack_m318 = v_stack_m250;
    v_stack_m320 = (uint8_t)(v_stack_m2A8);
    v_stack_m328 = (uint8_t)(v_stack_m282);
    result = RtlpInheritAcl2(v_stack_m208, v_stack_m258 + (uint32_t)(*(uint32_t *)(v_stack_m258 + 0xC)) * 1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m258 + (uint32_t)(*(uint32_t *)(v_stack_m258 + 0xC)) * 1)))), Arg6);
    if (sign_flag) goto loc_0092B705;
    if (v_stack_m29C != 0) goto loc_0092B1B8;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m270, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m258 + (uint32_t)(*(uint32_t *)(v_stack_m258 + 0xC)) * 1)))), Arg6);
    local_r14 = 0;
    goto loc_0092B1BF;
loc_0092B676:
    local_r13 = 0;
    goto loc_0092B50A;
loc_0092B689:
    local_r13 = 0;
loc_0092B691:
loc_0092B699:
    goto loc_0092B50A;
loc_0092B6A2:
    if (v_stack_m2B0 == 0) goto loc_0092B560;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m2B0, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m258 + (uint32_t)(*(uint32_t *)(v_stack_m258 + 0xC)) * 1)))), Arg6);
    goto loc_0092B560;
loc_0092B6BA:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m2A8, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m258 + (uint32_t)(*(uint32_t *)(v_stack_m258 + 0xC)) * 1)))), Arg6);
    result = 0;
    if (((uint32_t)((uint32_t)(0xC000000DULL))) != 0xC0000023ULL) goto loc_0092B0B4;
    local_r14 = (uint32_t)((v_stack_m290) + 1);
    goto loc_0092B2FA;
loc_0092B6E0:
    v_stack_m27D = 1;
    goto loc_0092B1F8;
loc_0092B6F0:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m258 + 0x8))) == 0) goto loc_0092AFED;
    goto loc_0092AFE4;
loc_0092B705:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m270, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_m258 + (uint32_t)(*(uint32_t *)(v_stack_m258 + 0xC)) * 1)))), Arg6);
    result = 0;
    if (((uint32_t)(v_stack_m258 + (uint32_t)(*(uint32_t *)(v_stack_m258 + 0x8)) * 1)) != 0xC0000023ULL) goto loc_0092B1BC;
    local_r14 = (uint32_t)((0) + 1);
    goto loc_0092B58B;
loc_0092B72B:
    local_r12 = 0;
    if ((((uint8_t)(*(uint16_t *)((uint32_t)((uint32_t)(v_stack_m258 + (uint32_t)(*(uint32_t *)(v_stack_m258 + 0xC)) * 1)) + 0x2))) & (16)) != 0) goto loc_0092B7A7;
loc_0092B739:
    Arg3 = 0;
    result = RtlFindAceByType(0, Arg3 + 17, Arg3, Arg6);
    if (result != 0) goto loc_0092B8A6;
    goto loc_0092B2E9;
loc_0092B75A:
    local_r13 = 0;
    goto loc_0092B50A;
loc_0092B772:
    v_stack_m1A8 = v_stack_m2B0;
    result = memcpy(v_stack_m2B0, v_stack_m290, *(uint8_t *)(v_stack_m290 + 0x1) * 4 + 8, Arg6);
    local_r15 = (v_stack_m2B0 + *(uint8_t *)(v_stack_m290 + 0x1) * 4) + (8);
    v_stack_m218 = local_r15;
    goto loc_0092AE88;
loc_0092B7A7:
    if (!sign_flag) goto loc_0092C771;
    if ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(v_stack_m258 + (uint32_t)(*(uint32_t *)(v_stack_m258 + 0xC)) * 1)) + 0xC))) == 0) goto loc_0092CAF0;
    goto loc_0092B739;
loc_0092B7C4:
    if ((((uint8_t)(*(uint16_t *)(v_stack_m2B0 + 0x2))) & (16)) == 0) goto loc_0092B072;
    if (!sign_flag) goto loc_0092CB1C;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m2B0 + 0xC))) == 0) goto loc_0092B072;
    local_rsi = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m2B0 + 0xC))))) + (v_stack_m220);
    goto loc_0092B075;
loc_0092B7F0:
    if ((((uint8_t)(*(uint16_t *)(v_stack_m290 + 0x2))) & (16)) == 0) goto loc_0092B158;
    if (!sign_flag) goto loc_0092CADF;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m290 + 0xC))) == 0) goto loc_0092B158;
    goto loc_0092B15B;
loc_0092B81A:
    v_stack_m264 = (uint32_t)((uint8_t)((uint32_t)(0xC000007CULL)));
    if ((uint16_t)((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(v_stack_m258 + (uint32_t)(*(uint32_t *)(v_stack_m258 + 0xC)) * 1)) + 0xC))) == 0) goto loc_0092AF8E;
    goto loc_0092ACDB;
loc_0092B830:
    local_r13 = 0;
    goto loc_0092B50A;
loc_0092B848:
loc_0092B84D:
    local_r13 = 0;
    goto loc_0092B50A;
loc_0092B861:
    result = ((uint32_t)(*(uint32_t *)((uint32_t)((uint32_t)(v_stack_m258 + (uint32_t)(*(uint32_t *)(v_stack_m258 + 0xC)) * 1)) + 0xC))) + (v_stack_m258);
    goto loc_0092AF9C;
loc_0092B869:
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m278)))) & (8));
    local_r13 = (uint32_t)((local_r13) | (0x2004ULL));
    local_r13 = (uint32_t)((local_r13) + ((uint32_t)(local_r13)));
    result = (uint32_t)(((uint32_t)(v_stack_m278)) & (0x1400ULL));
    v_stack_m298 = 1;
    local_r13 = (uint32_t)((local_r13) | ((uint32_t)(result)));
    v_stack_m2B7 = (uint8_t)(v_stack_m2B7);
    local_r13 = (uint32_t)((local_r13) + ((uint32_t)(local_r13)));
    v_stack_m260 = (uint32_t)(local_r13);
    goto loc_0092B10D;
loc_0092B8A6:
    v_stack_m208 = result + 8;
    v_stack_m2A0 = (uint8_t)(*(uint8_t *)(result + 0x1));
    if (((uint8_t)(*(uint8_t *)(result + 0x1))) == 8) goto loc_0092CB8F;
    if ((((uint8_t)(*(uint8_t *)(result + 0x1))) & (16)) != 0) goto loc_0092CB8F;
    if ((((uint8_t)(*(uint8_t *)(result + 0x1))) & (8)) != 0) goto loc_0092C5BD;
loc_0092B8D7:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4))) == 0) goto loc_0092C42E;
loc_0092B8DF:
    if (v_stack_m290 != 0) goto loc_0092B8FD;
    if (v_stack_m240 == 0) goto loc_0092C6D1;
    v_stack_m208 = v_stack_m228;
    v_stack_m2A0 = (uint8_t)(v_stack_m290);
loc_0092B8FD:
    if (v_stack_m228 == 0) goto loc_0092C28A;
    Arg2 = 0;
    result = memset(v_stack_m130, Arg2, Arg2 + 120, v_stack_m2B7);
    v_stack_m138 = 0x800002ULL;
    v_stack_m160 = 0;
    v_stack_m15C = 0x1000ULL;
    if (v_stack_m228 <= result) goto loc_0092C4C9;
    result = (uint8_t)((*(uint8_t *)(v_stack_m228)) & (15));
    if (((uint8_t)(result)) != 1) goto loc_0092C4C9;
    if ((*(uint8_t *)(v_stack_m228 + 0x1)) > 15) goto loc_0092C4C9;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m228 + 0x2))) - (v_stack_m160));
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint16_t *)(v_stack_m228 + 0x6);
        result = v_stack_m15C;
        Arg1 = (uint32_t)((Arg1) - ((uint32_t)(result)));
    }
    if ((uint32_t)(Arg1) != 0) goto loc_0092B689;
    if ((((uint32_t)(v_stack_m2A0)) & (0xFFFFFFE0ULL)) != 0) goto loc_0092CD14;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)))) & (0xFFFFFFF8ULL)) != 0) goto loc_0092CD21;
    result = RtlValidAcl(v_stack_m138, v_stack_m2A0, Arg2 + 120, v_stack_m2B7);
    if ((uint8_t)(result) == 0) goto loc_0092CC2C;
    Arg1 = 0;
loc_0092B9CC:
    if (0 < ((uint32_t)(v_stack_m134))) goto loc_0092BF7D;
    Arg3 = (v_stack_m138) + (v_stack_m136);
    Arg2 = v_stack_m130;
    if (v_stack_m130 > Arg3) { Arg2 = 0; }
    Arg1 = (uint16_t)((*(uint8_t *)(v_stack_m228 + 0x1)) + ((uint16_t)(v_stack_m2A8)));
    Arg1 = (uint16_t)((Arg1) << (2));
    if (Arg2 == 0) goto loc_0092C56C;
    result = ((uint16_t)(Arg1)) + (Arg2);
    if (result > Arg3) goto loc_0092C56C;
    *(uint16_t *)(Arg2 + 0x2) = (uint16_t)(Arg1);
    *(uint8_t *)(Arg2 + 0x1) = (uint8_t)(v_stack_m2A0);
    *(uint8_t *)(Arg2) = 17;
    *(uint32_t *)(Arg2 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x4)));
    result = memcpy(Arg2 + 8, v_stack_m228, *(uint8_t *)(v_stack_m228 + 0x1) * 4 + 8, v_stack_m134);
    Arg2 = 0;
    v_stack_m138 = 2;
    v_stack_m29C = 0;
loc_0092BA53:
    if ((((uint32_t)((uint32_t)(Arg7))) & (0x700ULL)) == 0) goto loc_0092C240;
loc_0092BA64:
    if (v_stack_m220 != 0) goto loc_0092C405;
loc_0092BA71:
loc_0092BA74:
    if ((uint32_t)(v_stack_m2A8) != 0) goto loc_0092C009;
    if (0 != 0) goto loc_0092C009;
loc_0092BA88:
    v_stack_m278 = 0;
loc_0092BA94:
    v_stack_m308 = v_stack_m230;
    v_stack_m310 = v_stack_m1D8;
    v_stack_m318 = v_stack_m1B8;
    v_stack_m320 = v_stack_m270;
    v_stack_m328 = v_stack_m1C0;
    result = RtlpCombineAcls(v_stack_m2A8, v_stack_m1E0, v_stack_m270, v_stack_m270);
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r13))) & (0x2000ULL));
    result = (uint32_t)((result) << (17));
    if (v_stack_m1E0 == 0) goto loc_0092BAFD;
    if (v_stack_m1E0 != v_stack_m1E0) {
        Arg2 = 0;
        Arg1 = v_stack_m1E0;
        result = ExFreePoolWithTag(Arg1, Arg2, v_stack_m270, v_stack_m270);
    }
    if (sign_flag) goto loc_0092CC4D;
    if (v_stack_m1D8 == 0) goto loc_0092BB44;
    if (v_stack_m298 != 0) goto loc_0092C6B5;
loc_0092BB18:
    v_stack_m2A8 = v_stack_m1D8;
    result = 0;
    v_stack_m27E = 1;
    v_stack_m1D8 = 0;
    result = (uint32_t)((0) & (8));
    local_rdi = (uint32_t)((0) & (0x1400ULL));
    result = (uint32_t)((result) | (4));
    result = (uint32_t)((result) + ((uint32_t)(result)));
    result = (uint32_t)((result) | ((uint32_t)(local_rdi)));
    result = (uint32_t)((result) + ((uint32_t)(result)));
    local_r13 = (uint32_t)((local_r13) | ((uint32_t)(result)));
    v_stack_m260 = (uint32_t)(local_r13);
loc_0092BB44:
    if ((((uint8_t)((uint32_t)(Arg7))) & (8)) != 0) goto loc_0092BBAE;
    Arg3 = 0;
    result = RtlFindAceByType(v_stack_m1D8, Arg3 + 17, Arg3, (uint32_t)(Arg7));
    if (result == 0) goto loc_0092C77A;
loc_0092BB6D:
    if (result + 8 == 0) goto loc_0092BBA7;
    if (v_stack_m240 == 0) goto loc_0092CBA9;
    result = RtlSidDominates(v_stack_m228, result + 8, v_stack_m281, (uint32_t)(Arg7));
    if (sign_flag) goto loc_0092CC4D;
    result = (uint8_t)((uint32_t)(v_stack_m20C));
    if (v_stack_m281 == 0) { result = 1; }
    v_stack_m20C = (uint32_t)(result);
loc_0092BBA7:
loc_0092BBAE:
    local_rdi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg7)))) >> (2));
    local_rdi = (uint8_t)((local_rdi) & (1));
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg7)))) & (1));
    local_r11 = 0;
    if ((((uint8_t)(*(uint16_t *)(v_stack_m258 + 0x2))) & (4)) != 0) goto loc_0092BC40;
loc_0092BBD1:
    if (v_stack_m220 != 0) goto loc_0092C3DA;
loc_0092BBDE:
loc_0092BBE1:
    local_rsi = (uint32_t)((*(uint16_t *)(v_stack_m258 + 0x2)) & (0x140CULL));
    if (condition_is_not_equal) goto loc_0092C110;
    if (0 != 0) goto loc_0092C110;
    local_rdi = 0;
    v_stack_m2B0 = 0;
loc_0092BC07:
    if ((((uint8_t)((uint32_t)(Arg7))) & (1)) != 0) {
    }
    result = (uint8_t)(((uint8_t)(*(uint16_t *)(v_stack_m258 + 0x2))) & (12));
    if (((uint8_t)(result)) == 12) goto loc_0092C706;
    local_r13 = (uint32_t)(v_stack_m260);
    if (v_stack_m1D0 != 0) {
        Arg3 = v_stack_m1D0;
        v_stack_m2B0 = v_stack_m1D0;
        local_r13 = (uint32_t)(((uint32_t)(v_stack_m260)) | (4));
    }
    local_r15 = 0;
    goto loc_0092BC85;
loc_0092BC40:
    if (!sign_flag) goto loc_0092C462;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m258 + 0x10))) == 0) goto loc_0092C585;
    goto loc_0092BBD1;
loc_0092BC5D:
    result = (uint32_t)(((uint32_t)(v_stack_m278)) & (0x1408ULL));
    result = (uint32_t)((result) | (4));
    local_r13 = (uint32_t)(((uint32_t)(v_stack_m260)) | ((uint32_t)(result)));
    v_stack_m2B8 = 1;
loc_0092BC85:
    if (condition_is_below) goto loc_0092BCA4;
    if (v_stack_m280 == 0) goto loc_0092BCA4;
    if (v_stack_m240 == 0) goto loc_0092BCA4;
    if (v_stack_m220 != 0) goto loc_0092C33E;
loc_0092BCA4:
loc_0092BCA8:
    if ((((uint8_t)((uint32_t)(Arg7))) & (1)) != 0) goto loc_0092C4B6;
loc_0092BCB2:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m230)) & (0xFFFFFDFFULL));
    if (condition_is_equal) goto loc_0092BFF3;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) & (432));
    if (((uint32_t)(result)) != ((uint32_t)(Arg1))) goto loc_0092BFF3;
    result = 0;
loc_0092BCD2:
    if (((uint8_t)(v_stack_m2B6)) != 1) goto loc_0092BD07;
    if (v_stack_m2B7 != 0) goto loc_0092C9E3;
loc_0092BCE1:
    local_rsi = 0;
loc_0092BCE7:
    if (v_stack_m20C != 0) goto loc_0092C7CA;
loc_0092BCF1:
    if (v_stack_m283 != 0) goto loc_0092C4E2;
loc_0092BCFE:
    if ((uint8_t)(v_stack_m284) != 0) goto loc_0092C2E4;
loc_0092BD07:
    Arg2 = 0;
loc_0092BD0D:
    if (v_stack_m248 == 0) goto loc_0092CAB2;
loc_0092BD36:
    if ((((uint8_t)(local_r13)) & (16)) == 0) goto loc_0092BF76;
    if (v_stack_m2A8 == 0) goto loc_0092BF76;
    local_rsi = (uint32_t)((*(uint16_t *)(v_stack_m2A8 + 0x2)) + (3));
    local_rsi = (uint32_t)((local_rsi) & (0xFFFFFFFCULL));
loc_0092BD57:
    if ((((uint8_t)(local_r13)) & (4)) == 0) goto loc_0092C26C;
    if (v_stack_m2B0 == 0) goto loc_0092C26C;
    local_rdi = (uint32_t)((*(uint16_t *)(v_stack_m2B0 + 0x2)) + (3));
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFFCULL));
loc_0092BD74:
    Arg2 = (uint32_t)((local_rdi + 20) + ((uint32_t)(local_rsi)));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(*(uint8_t *)(v_stack_m248 + 0x1) * 4 + 8)));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(*(uint8_t *)(v_stack_m250 + 0x1) * 4 + 8)));
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x64536553ULL), (uint32_t)(Arg7));
    v_stack_m290 = result;
    if (result == 0) goto loc_0092C273;
    result = 0;
    *(uint64_t *)(result) = v_xmm0;
    *(uint32_t *)(result + 0x10) = 0;
    *(uint8_t *)(result) = 1;
    if ((((uint8_t)(local_r13)) & (16)) == 0) goto loc_0092BEE2;
    if (v_stack_m2A8 == 0) goto loc_0092BEE2;
    v_stack_m1B8 = result + 20;
    if (((Arg7) & (0x4000ULL)) != 0) goto loc_0092C58D;
    result = memcpy(result + 20, v_stack_m2A8, *(uint16_t *)(v_stack_m2A8 + 0x2), (uint32_t)(Arg7));
    Arg4 = 0;
    if (v_stack_m298 != 0) goto loc_0092BEA6;
    if (result + 20 == 0) goto loc_0092BEA6;
    if (0 >= (*(uint16_t *)(result + 0x14 + 0x4))) goto loc_0092BEA6;
loc_0092BE2C:
    if (((uint8_t)(*(uint8_t *)(result + 0x14 + 0x8))) > 10) goto loc_0092C231;
loc_0092BE37:
    if (((*(uint8_t *)(result + 0x14 + 0x8 + 0x1)) & (8)) != 0) goto loc_0092BE8C;
    if (sign_flag) {
        Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x14 + 0x8 + 0x4))) | (*(uint32_t *)(v_stack_m238)));
    }
    if (!(condition_is_above_or_equal)) {
        Arg1 = (uint32_t)((Arg1) | (*(uint32_t *)(v_stack_m238 + 0x4)));
    }
    if (!(condition_is_above_or_equal)) {
        Arg1 = (uint32_t)((Arg1) | (*(uint32_t *)(v_stack_m238 + 0x8)));
    }
    if (!(condition_is_above_or_equal)) {
        Arg1 = (uint32_t)((Arg1) | (*(uint32_t *)(v_stack_m238 + 0xC)));
    }
    Arg1 = (uint32_t)((Arg1) & (0xFFFFFFFULL));
    *(uint32_t *)(result + 0x14 + 0x8 + 0x4) = (uint32_t)(Arg1);
    if (((uint8_t)(*(uint8_t *)(result + 0x14 + 0x8))) > 10) goto loc_0092CC6A;
    if (((uint8_t)(*(uint8_t *)(result + 0x14 + 0x8))) >= 10) goto loc_0092CC6A;
loc_0092BE87:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m238 + 0xC))) & ((uint32_t)(Arg1)));
    *(uint32_t *)(result + 0x14 + 0x8 + 0x4) = (uint32_t)(result);
loc_0092BE8C:
    Arg3 = (uint32_t)((0) + 1);
    Arg2 = (result + 20 + 8) + (*(uint16_t *)(result + 0x14 + 0x8 + 0x2));
    if (((uint32_t)(Arg3)) < ((uint32_t)(*(uint16_t *)(result + 0x14 + 0x4)))) goto loc_0092BE2C;
loc_0092BEA6:
    result = v_stack_m2A8;
    if (((uint32_t)(local_rsi)) >= = ((uint32_t)(*(uint16_t *)(v_stack_m2A8 + 0x2)))) {
        Arg3 = (uint32_t)(local_rsi);
        Arg2 = 0;
        Arg3 = (uint32_t)((Arg3) - ((uint32_t)(*(uint16_t *)(v_stack_m2A8 + 0x2))));
        Arg1 = (*(uint16_t *)(v_stack_m2A8 + 0x2)) + (result + 20);
        result = memset(Arg1, Arg2, Arg3, Arg4);
        Arg4 = 0;
    }
    if (v_stack_m1B8 == 0) goto loc_0092CBBE;
    local_rbx = (result + 20) + ((uint32_t)((uint32_t)(local_rsi)));
    local_r14 = (uint32_t)((v_stack_m1B8) - ((uint32_t)(v_stack_m290)));
loc_0092BEDA:
    *(uint32_t *)(v_stack_m290 + 0xC) = (uint32_t)(local_r14);
loc_0092BEE2:
    if ((((uint8_t)(local_r13)) & (4)) == 0) goto loc_0092C458;
    if (v_stack_m2B0 == 0) goto loc_0092C452;
    if (((Arg7) & (0x4000ULL)) != 0) goto loc_0092C490;
    result = memcpy(local_rbx, v_stack_m2B0, *(uint16_t *)(v_stack_m2B0 + 0x2), Arg4);
    if ((uint8_t)(v_stack_m2B8) != 0) goto loc_0092B4A0;
    if (local_rbx == 0) goto loc_0092B4A0;
    result = 0;
    if (0 >= (*(uint16_t *)(local_rbx + 0x4))) goto loc_0092B4A0;
loc_0092BF4D:
    if (((uint8_t)(*(uint8_t *)(local_rbx + 0x8))) > 10) goto loc_0092BFFA;
loc_0092BF58:
    if (((*(uint8_t *)(local_rbx + 0x8 + 0x1)) & (8)) == 0) goto loc_0092BF9F;
loc_0092BF5E:
    Arg3 = (uint32_t)((0) + 1);
    Arg2 = (local_rbx + 8) + (*(uint16_t *)(local_rbx + 0x8 + 0x2));
    if (((uint32_t)(Arg3)) < ((uint32_t)(*(uint16_t *)(local_rbx + 0x4)))) goto loc_0092BF4D;
    goto loc_0092B497;
loc_0092BF76:
    goto loc_0092BD57;
loc_0092BF7D:
    Arg1 = (v_stack_m138) + ((uint32_t)(0x673ULL));
    if (Arg2 >= Arg1) goto loc_0092CC2C;
    Arg3 = (uint32_t)((Arg3) + 1);
    Arg2 = (Arg2) + (*(uint16_t *)(Arg2 + 0x2));
    goto loc_0092B9CC;
loc_0092BF9F:
    if (sign_flag) {
        Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg2 + 0x4))) | (*(uint32_t *)(v_stack_m238)));
    }
    if (!(condition_is_above_or_equal)) {
        Arg1 = (uint32_t)((Arg1) | (*(uint32_t *)(v_stack_m238 + 0x4)));
    }
    if (!(condition_is_above_or_equal)) {
        Arg1 = (uint32_t)((Arg1) | (*(uint32_t *)(v_stack_m238 + 0x8)));
    }
    if (!(condition_is_above_or_equal)) {
        Arg1 = (uint32_t)((Arg1) | (*(uint32_t *)(v_stack_m238 + 0xC)));
    }
    Arg1 = (uint32_t)((Arg1) & (0xFFFFFFFULL));
    *(uint32_t *)(Arg2 + 0x4) = (uint32_t)(Arg1);
    if (((uint8_t)(*(uint8_t *)(Arg2))) > 10) goto loc_0092CC5D;
    if (((uint8_t)(*(uint8_t *)(Arg2))) >= 10) goto loc_0092CC5D;
loc_0092BFE9:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m238 + 0xC))) & ((uint32_t)(Arg1)));
    *(uint32_t *)(Arg2 + 0x4) = (uint32_t)(result);
    goto loc_0092BF5E;
loc_0092BFF3:
    goto loc_0092BCD2;
loc_0092BFFA:
    result = (uint8_t)((1) - (13));
    if (((uint8_t)(result)) > 1) goto loc_0092BF5E;
    goto loc_0092BF58;
loc_0092C009:
    v_stack_m29C = 200;
loc_0092C014:
    if (((uint32_t)((uint32_t)((uint32_t)(Arg2)))) >= 2) goto loc_0092C0F0;
    result = ExAllocatePool2(256, 200, (uint32_t)(0x63416553ULL), Arg4);
    if (result == 0) goto loc_0092B848;
    v_stack_m2C0 = v_stack_m278;
    v_stack_m2C8 = v_stack_m267;
    v_stack_m2D0 = result;
    v_stack_m2D8 = v_stack_m29C;
    v_stack_m2E0 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m2E8 = v_stack_m1F0;
    v_stack_m2F0 = 3;
    v_stack_m2F8 = v_stack_m238;
    v_stack_m300 = v_stack_m1F8;
    v_stack_m308 = v_stack_m218;
    v_stack_m310 = v_stack_m248;
    v_stack_m318 = v_stack_m250;
    v_stack_m320 = 0;
    v_stack_m328 = 1;
    result = RtlpInheritAcl2(local_rdi, v_stack_m1E0, (uint32_t)((uint32_t)(*(uint8_t *)(v_stack_m248 + 0x1) * 4 + 8)), Arg6);
    if (sign_flag) goto loc_0092C297;
    if (v_stack_m29C != 0) goto loc_0092C5F3;
    Arg2 = 0;
    result = ExFreePoolWithTag(result, Arg2, (uint32_t)((uint32_t)(*(uint8_t *)(v_stack_m248 + 0x1) * 4 + 8)), Arg6);
    Arg2 = 0;
loc_0092C0F0:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) == 0x8000000BULL) goto loc_0092BA88;
    if (sign_flag) goto loc_0092B84D;
    goto loc_0092BA94;
loc_0092C110:
    v_stack_m29C = 200;
loc_0092C11B:
    if (0 >= 2) goto loc_0092C1FD;
    result = ExAllocatePool2(256, 200, (uint32_t)(0x63416553ULL), Arg6);
    v_stack_m2B0 = result;
    if (result == 0) goto loc_0092CC77;
    v_stack_m2C0 = v_stack_m278;
    v_stack_m2C8 = v_stack_m284;
    v_stack_m2D0 = result;
    v_stack_m2D8 = v_stack_m29C;
    v_stack_m2E0 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m2E8 = v_stack_m1F0;
    v_stack_m2F0 = 1;
    v_stack_m2F8 = v_stack_m238;
    v_stack_m300 = v_stack_m1F8;
    v_stack_m308 = v_stack_m218;
    v_stack_m310 = v_stack_m248;
    v_stack_m318 = v_stack_m250;
    v_stack_m320 = (uint8_t)((uint32_t)(v_stack_m278));
    v_stack_m328 = (uint8_t)(*(uint8_t *)(v_stack_m248 + 0x1) * 4 + 8);
    result = RtlpInheritAcl2(v_stack_m1E0, (uint32_t)(0x673ULL), 0, Arg6);
    if (sign_flag) goto loc_0092C2BC;
    if (v_stack_m29C != 0) goto loc_0092C5FA;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m2B0, Arg2, 0, Arg6);
    local_r11 = 0;
loc_0092C1FD:
    v_stack_m2B0 = 0;
    if (!sign_flag) goto loc_0092BC5D;
    v_stack_m2B0 = 0;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0x8000000BULL) goto loc_0092C520;
    goto loc_0092BC07;
loc_0092C231:
    result = (uint8_t)((result) - (13));
    if (((uint8_t)(result)) > 1) goto loc_0092BE8C;
    goto loc_0092BE37;
loc_0092C240:
    if (v_stack_m1E0 != 0) goto loc_0092C24E;
    if (v_stack_m2B0 != 0) goto loc_0092C336;
loc_0092C24E:
    result = (uint32_t)((*(uint16_t *)(v_stack_m284 + 0x2)) & (0x2800ULL));
    local_r15 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m284 + 0x2)))) >> (1));
    local_r15 = (uint32_t)((local_r15) & (24));
    local_r15 = (uint32_t)((local_r15) | ((uint32_t)(result)));
    local_r15 = (uint32_t)((local_r15) >> (1));
    goto loc_0092BA64;
loc_0092C26C:
    goto loc_0092BD74;
loc_0092C273:
    goto loc_0092B50A;
loc_0092C28A:
    Arg2 = 0;
    v_stack_m1E0 = 0;
    goto loc_0092BA53;
loc_0092C297:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m2B0, Arg2, 0, (uint32_t)(Arg7));
    Arg2 = 0;
    if (((uint32_t)((uint32_t)(0xC000009AULL))) != 0xC0000023ULL) goto loc_0092C0F0;
    local_r14 = (uint32_t)((v_stack_m1E0) + 1);
    goto loc_0092C014;
loc_0092C2BC:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m2B0, Arg2, 0, (uint32_t)(Arg7));
    local_r11 = 0;
    if (((uint32_t)((uint32_t)(0xC000009AULL))) != 0xC0000023ULL) goto loc_0092C1FD;
    local_r12 = (uint32_t)((0) + 1);
    goto loc_0092C11B;
loc_0092C2E4:
    if ((uint8_t)((uint32_t)(0xC000009AULL)) == 0) goto loc_0092BD07;
    v_stack_m328 = v_stack_m27F;
    result = RtlpCreateServerAcl(v_stack_m2B0, v_stack_m1B0, v_stack_m218, v_stack_m1C8);
    if (sign_flag) goto loc_0092CD2E;
    if ((uint8_t)(v_stack_m2A8) != 0) goto loc_0092C533;
loc_0092C323:
    Arg2 = 0;
    v_stack_m2B0 = v_stack_m1C8;
    v_stack_m1C8 = 0;
    goto loc_0092BD0D;
loc_0092C336:
    goto loc_0092BA64;
loc_0092C33E:
    result = (uint32_t)(((uint32_t)((uint32_t)(v_stack_m1C8))) | (1));
    v_stack_m2F8 = 0;
    Arg2 = 0;
    v_stack_m300 = v_stack_m1A0;
    v_stack_m308 = v_stack_m238;
    v_stack_m310 = local_r14;
    v_stack_m318 = (uint32_t)(result);
    v_stack_m320 = Arg6;
    v_stack_m328 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m29C = 0;
    v_stack_m210 = 0;
    result = RtlpNewSecurityObject(v_stack_m220, Arg2, v_stack_m200, v_stack_m1F0);
    if (sign_flag) goto loc_0092C50D;
    if ((((uint8_t)(*(uint16_t *)(v_stack_m200 + 0x2))) & (4)) != 0) goto loc_0092C46B;
    local_r12 = 0;
loc_0092C3B7:
    result = RtlpOwnerAcesPresent(16, 0, v_stack_m200, v_stack_m1F0);
    if ((uint8_t)(result) != 0) goto loc_0092C660;
loc_0092C3CA:
    goto loc_0092BCA8;
loc_0092C3DA:
    if ((((uint8_t)(*(uint16_t *)(v_stack_m220 + 0x2))) & (4)) == 0) goto loc_0092BBDE;
    if (!sign_flag) goto loc_0092CACE;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m220 + 0x10))) == 0) goto loc_0092BBDE;
    goto loc_0092BBE1;
loc_0092C405:
    if ((((uint8_t)(*(uint16_t *)(16 + 0x2))) & (16)) == 0) goto loc_0092BA71;
    if (!sign_flag) goto loc_0092C6AC;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(16 + 0xC))) == 0) goto loc_0092BA71;
    goto loc_0092BA74;
loc_0092C42E:
    if (0 == 0) goto loc_0092C449;
    Arg2 = 0;
    result = RtlSubAuthoritySid(0, Arg2, v_stack_m2B0, (uint32_t)(Arg7));
    if ((*(uint32_t *)(result)) < 0x2000ULL) goto loc_0092CD0A;
loc_0092C449:
    goto loc_0092B8FD;
loc_0092C452:
    result = 0;
    *(uint32_t *)(v_stack_m220 + (uint32_t)(*(uint32_t *)(v_stack_m220 + 0x10)) * 1 + 0x10) = 0;
loc_0092C458:
    goto loc_0092B4C6;
loc_0092C462:
    goto loc_0092BBD1;
loc_0092C46B:
    if (!sign_flag) goto loc_0092CA6A;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m200 + 0x10))) == 0) goto loc_0092CBD3;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m200 + 0x10))))) + (v_stack_m200);
loc_0092C488:
    local_r12 = 0;
    goto loc_0092C3B7;
loc_0092C490:
    Arg3 = v_stack_m238;
    if ((uint8_t)(v_stack_m2B8) != 0) { Arg3 = 0; }
    result = RtlpNormalizeAcl(v_stack_m2B6, Arg2, Arg3, (uint32_t)(Arg7));
    goto loc_0092B4B8;
loc_0092C4B6:
    if (Arg3 != 0) goto loc_0092BCB2;
    goto loc_0092BCB2;
loc_0092C4C9:
    local_r13 = 0;
    goto loc_0092B50A;
loc_0092C4E2:
    if ((((uint8_t)((uint32_t)(Arg7))) & (16)) != 0) goto loc_0092BCFE;
    result = SepValidOwnerSubjectContext(v_stack_m290, v_stack_m250, (uint8_t)((uint32_t)(0xC0000078ULL)), (uint32_t)(Arg7));
    if ((uint8_t)(result) != 0) goto loc_0092BCFE;
loc_0092C50D:
    goto loc_0092B691;
loc_0092C517:
    goto loc_0092B204;
loc_0092C520:
    local_r13 = 0;
    goto loc_0092B50A;
loc_0092C533:
    if ((uint8_t)((uint32_t)(0xC0000078ULL)) == 0) goto loc_0092C323;
    Arg2 = 0;
    result = ExFreePoolWithTag((uint8_t)((uint32_t)(0xC0000078ULL)), Arg2, (uint8_t)((uint32_t)(0xC0000078ULL)), (uint32_t)(Arg7));
    goto loc_0092C323;
loc_0092C54B:
    if ((uint8_t)((uint32_t)(0xC0000078ULL)) != 0) goto loc_0092C955;
    local_r13 = 0;
    goto loc_0092B50A;
loc_0092C56C:
    local_r13 = 0;
    goto loc_0092B50A;
loc_0092C585:
    goto loc_0092BBD1;
loc_0092C58D:
    Arg3 = v_stack_m238;
    if (v_stack_m298 != 0) { Arg3 = 0; }
    result = RtlpNormalizeAcl((uint32_t)(0xC0000099ULL), Arg2, Arg3, (uint32_t)(Arg7));
    Arg4 = 0;
    if ((*(uint16_t *)((uint32_t)(0xC0000099ULL) + 0x4)) == 0) goto loc_0092CABA;
    goto loc_0092BEC5;
loc_0092C5BD:
    v_stack_m2A0 = (uint8_t)((uint32_t)(0xC0000099ULL));
    Arg2 = 0;
    v_stack_m208 = *(uint16_t *)((uint32_t)(0xC0000099ULL) + 0x2);
    result = RtlSubAuthoritySid(0, Arg2, Arg3, Arg4);
    if ((*(uint32_t *)(result)) >= 0x2000ULL) goto loc_0092B8D7;
    local_r13 = 0;
    goto loc_0092B50A;
loc_0092C5F3:
    Arg2 = 0;
    goto loc_0092C0F0;
loc_0092C5FA:
    local_r11 = 0;
    goto loc_0092C1FD;
loc_0092C606:
    if (v_stack_m1C8 == 0) goto loc_0092B524;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m1C8, Arg2, v_stack_m2B0, Arg4);
    goto loc_0092B524;
loc_0092C61F:
    if (v_stack_m2B0 == 0) goto loc_0092CCBF;
    if ((*(uint16_t *)(v_stack_m2B0 + 0x2)) < 0) goto loc_0092CB00;
loc_0092C637:
    v_stack_m250 = *(uint64_t *)(v_stack_m2B0 + 0x8);
    v_stack_m283 = 1;
    if (*(uint64_t *)(v_stack_m2B0 + 0x8) != 0) goto loc_0092AFD7;
loc_0092C648:
    local_r13 = 0;
    goto loc_0092B50A;
loc_0092C660:
    v_stack_m300 = v_stack_m210;
    Arg3 = 0;
    v_stack_m308 = v_stack_m29C;
    v_stack_m310 = (uint8_t)((uint32_t)(0xC000005AULL));
    v_stack_m318 = v_stack_m2B0;
    v_stack_m320 = 0;
    v_stack_m328 = 0;
    result = SeAccessCheck(v_stack_m200, v_stack_m290, Arg3, (uint32_t)(0x40000ULL));
    if ((uint8_t)(result) != 0) goto loc_0092C3CA;
    goto loc_0092C50D;
loc_0092C6AC:
    goto loc_0092BA74;
loc_0092C6B5:
    if (v_stack_m2B0 == 0) goto loc_0092BB18;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m2B0, Arg2, Arg3, (uint32_t)(0x40000ULL));
    goto loc_0092BB18;
loc_0092C6D1:
    local_r13 = 0;
    goto loc_0092B50A;
loc_0092C6EA:
    if (v_stack_m270 == 0) goto loc_0092B54A;
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m270, Arg2, Arg3, (uint32_t)(0x40000ULL));
    goto loc_0092B54A;
loc_0092C706:
    if ((((uint8_t)(v_stack_m270)) & (4)) != 0) goto loc_0092C798;
loc_0092C712:
    Arg1 = (uint32_t)((v_stack_m270) & (0x1000ULL));
    v_stack_m2B0 = 0;
    Arg1 = (uint32_t)((Arg1) | (4));
    local_r13 = (uint32_t)((local_r13) | ((uint32_t)(Arg1)));
    local_r15 = 0;
    goto loc_0092BC85;
loc_0092C72D:
    if ((((uint8_t)(local_r13)) & (16)) != 0) goto loc_0092C974;
    v_stack_m2A8 = v_stack_m290;
loc_0092C73B:
    local_r13 = (uint32_t)((local_r13) & (0x2000ULL));
    v_stack_m2B7 = 1;
    local_r13 = (uint32_t)((local_r13) | ((uint32_t)(Arg1)));
    local_r13 = (uint32_t)((local_r13) | (16));
    v_stack_m260 = (uint32_t)(local_r13);
    goto loc_0092B10D;
loc_0092C756:
    if ((((uint8_t)(Arg1)) & (16)) != 0) goto loc_0092C996;
    v_stack_m270 = v_stack_m290;
    goto loc_0092B1F8;
loc_0092C768:
    goto loc_0092B069;
loc_0092C771:
    goto loc_0092B739;
loc_0092C77A:
    goto loc_0092BB6D;
loc_0092C783:
    goto loc_0092AD8C;
loc_0092C78F:
    goto loc_0092B214;
loc_0092C798:
    if (!sign_flag) goto loc_0092CBCA;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m208 + 0x10))) != 0) goto loc_0092CA95;
    goto loc_0092C712;
loc_0092C7B4:
    if (v_stack_m27C == 0) goto loc_0092B557;
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_r11 + 0x18), Arg2, 0, (uint32_t)(0x40000ULL));
    goto loc_0092B557;
loc_0092C7CA:
    if ((((uint8_t)((uint32_t)(0x40000ULL))) & (8)) != 0) goto loc_0092BCF1;
    if (v_stack_m290 == 0) goto loc_0092CC8F;
    v_stack_m150 = *(uint64_t *)(v_rip + 0x6AD344);
    v_stack_m158 = 0;
    v_stack_m154 = 0;
    v_stack_m148 = (uint32_t)(v_stack_m2B0);
    result = SePrivilegeCheck(v_stack_m158, v_stack_m290, 1, (uint32_t)(0x40000ULL));
    Arg1 = 0;
    result = SePrivilegedServiceAuditAlarm(Arg1, v_stack_m290, v_stack_m158, (uint8_t)(result));
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_0092BCF1;
    goto loc_0092B691;
loc_0092C840:
    v_stack_m288 = 1;
loc_0092C847:
    local_rbx = 0;
    if ((((uint8_t)(*(uint16_t *)(v_stack_m258 + 0x2))) & (16)) != 0) goto loc_0092C9B4;
loc_0092C857:
    result = RtlFindAceByType(0, 20, v_stack_m288, (uint8_t)(result));
    if (result != 0) goto loc_0092CBDE;
    if (0 == 0) goto loc_0092B25D;
    if (v_stack_m1A0 == 0) goto loc_0092CCD3;
loc_0092C893:
    result = RtlCreateAcl(v_stack_mB8, 88, 88 - 86, (uint8_t)(result));
    if (sign_flag) goto loc_0092B84D;
    v_stack_m320 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m1A0 + 0x4)));
    v_stack_m328 = 20;
    result = RtlAddProcessTrustLabelAce(v_stack_mB8, 2, 0, 0);
    if (sign_flag) goto loc_0092B84D;
    result = (uint32_t)((*(uint16_t *)(v_stack_m258 + 0x2)) & (0x800ULL));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(v_stack_m258 + 0x2)))) >> (1));
    Arg2 = (uint32_t)((Arg2) & (24));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(result)));
    v_stack_m300 = v_stack_m278;
    v_stack_m308 = v_stack_m1C0;
    v_stack_m310 = 2;
    v_stack_m318 = v_stack_m238;
    v_stack_m320 = v_stack_m248;
    Arg2 = (uint32_t)((Arg2) >> (1));
    v_stack_m328 = v_stack_m250;
    result = RtlpComputeMergedAcl(v_stack_m270, Arg2, v_stack_mB8, (uint32_t)((uint32_t)(*(uint64_t *)(v_rip + 0x53B626))));
    if (sign_flag) goto loc_0092B84D;
    v_stack_m27C = 1;
    goto loc_0092B261;
loc_0092C955:
    if ((*(uint16_t *)((uint32_t)(Arg7) + 0x2)) >= 0) goto loc_0092CB13;
    if ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(Arg7) + 0x8))) == 0) goto loc_0092B830;
    goto loc_0092B000;
loc_0092C974:
    if (!sign_flag) goto loc_0092CB2E;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0xC))) == 0) goto loc_0092CB25;
    result = ((uint32_t)(*(uint32_t *)(local_r11 + 0xC))) + (0);
loc_0092C98D:
    v_stack_m2A8 = result;
    goto loc_0092C73B;
loc_0092C996:
    if (!sign_flag) goto loc_0092CB44;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r11 + 0xC))) != 0) goto loc_0092CB37;
    v_stack_m270 = 0;
    goto loc_0092B1F8;
loc_0092C9B4:
    if (!sign_flag) goto loc_0092CB86;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m258 + 0xC))) != 0) goto loc_0092CB7D;
    goto loc_0092C857;
loc_0092C9D0:
    goto loc_0092ADDD;
loc_0092C9D8:
    goto loc_0092ADCF;
loc_0092C9E3:
    if (((24) & (8)) != 0) goto loc_0092BCE1;
    if ((uint8_t)((uint32_t)(*(uint32_t *)(v_stack_m258 + 0xC))) == 0) goto loc_0092BCE1;
    if (0 == 0) goto loc_0092CC8F;
    v_stack_m150 = *(uint64_t *)(v_rip + 0x6AD0FB);
    local_rsi = 0;
    v_stack_m158 = 1;
    v_stack_m154 = 1;
    v_stack_m148 = 0;
    result = SePrivilegeCheck(v_stack_m158, 0, 1, 24);
    Arg1 = 0;
    result = SePrivilegedServiceAuditAlarm(Arg1, 0, v_stack_m158, (uint8_t)(result));
    if ((uint8_t)((uint8_t)(result)) != 0) goto loc_0092CC20;
    goto loc_0092B691;
loc_0092CA6A:
    goto loc_0092C488;
loc_0092CA73:
    goto loc_0092B271;
loc_0092CA7C:
    v_stack_m1D0 = *(uint64_t *)(v_stack_m258 + 0x18);
    goto loc_0092AF3A;
loc_0092CA85:
    goto loc_0092AEBE;
loc_0092CA8D:
    goto loc_0092ADBA;
loc_0092CA95:
    goto loc_0092C712;
loc_0092CA9E:
    goto loc_0092B214;
loc_0092CAA6:
    v_stack_m1F8 = *(uint64_t *)(v_stack_m258 + 0x18);
    goto loc_0092AF21;
loc_0092CAB2:
    goto loc_0092BD36;
loc_0092CABA:
    goto loc_0092BEC5;
loc_0092CAC5:
    goto loc_0092B14B;
loc_0092CACE:
    goto loc_0092BBE1;
loc_0092CAD7:
    goto loc_0092B069;
loc_0092CADF:
    goto loc_0092B15B;
loc_0092CAE8:
    goto loc_0092B14B;
loc_0092CAF0:
    goto loc_0092B739;
loc_0092CAF8:
    goto loc_0092B271;
loc_0092CB00:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x18) + 0x4))) == 0) goto loc_0092C648;
    result = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x18) + 0x4))) + (*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x18));
    goto loc_0092C637;
loc_0092CB13:
    goto loc_0092B000;
loc_0092CB1C:
    goto loc_0092B075;
loc_0092CB25:
    v_stack_m2A8 = *(uint64_t *)(0 + 0x20);
    goto loc_0092C73B;
loc_0092CB2E:
    goto loc_0092C98D;
loc_0092CB37:
    v_stack_m270 = local_r11 + *(uint64_t *)(local_r11 + 0x18) * 1;
    goto loc_0092B1F8;
loc_0092CB44:
    v_stack_m270 = *(uint64_t *)(local_r11 + 0x18);
    goto loc_0092B1F8;
loc_0092CB51:
    result = RtlpValidTrustSubjectContext(*(uint64_t *)(0 + 0x20), *(uint64_t *)(result + 0x20), *(uint64_t *)(result + 0x20) + result * 1, v_stack_m29C);
    if ((uint8_t)(result) != 0) goto loc_0092B239;
    local_r13 = 0;
    goto loc_0092B50A;
loc_0092CB7D:
    goto loc_0092C857;
loc_0092CB86:
    goto loc_0092C857;
loc_0092CB8F:
    v_stack_m208 = *(uint64_t *)(0 + 0x20);
    v_stack_m2A0 = 0;
    goto loc_0092B8D7;
loc_0092CBA9:
    local_r13 = 0;
    goto loc_0092B50A;
loc_0092CBBE:
    goto loc_0092BEDA;
loc_0092CBCA:
    goto loc_0092C712;
loc_0092CBD3:
    local_r12 = 0;
    goto loc_0092C3B7;
loc_0092CBDE:
    if ((((uint8_t)(*(uint8_t *)(v_stack_m290 + 0x1))) & (8)) != 0) goto loc_0092C847;
    if (v_stack_m1A0 == 0) goto loc_0092B689;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m1A0 + 0x4))) & ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m290 + 0x4)))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m290 + 0x4))))) goto loc_0092B689;
    if (v_stack_m290 + 8 != 0) goto loc_0092C893;
    goto loc_0092B689;
loc_0092CC20:
    goto loc_0092BCE7;
loc_0092CC2C:
    local_r13 = 0;
    goto loc_0092B50A;
loc_0092CC45:
loc_0092CC4D:
    local_r13 = 0;
    goto loc_0092B50A;
loc_0092CC5D:
    goto loc_0092BFE9;
loc_0092CC6A:
    goto loc_0092BE87;
loc_0092CC77:
    local_r13 = 0;
    goto loc_0092B50A;
loc_0092CC8F:
    goto loc_0092C50D;
loc_0092CC99:
    if (((*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_m290 + 0xC)) + 0x4)) & (0xFF000000ULL)) == 0) goto loc_0092CCE0;
    goto loc_0092B2B2;
loc_0092CCAC:
    local_rbx = (uint8_t)((uint32_t)(0xC000000DULL));
    if ((*(uint32_t *)((uint32_t)(*(uint32_t *)(v_stack_m290 + 0x4)) + 0x8)) == 0) { local_rbx = 0; }
    v_stack_m264 = (uint32_t)(local_rbx);
    goto loc_0092AD36;
loc_0092CCBF:
    local_r13 = 0;
    goto loc_0092B699;
loc_0092CCD3:
    local_r13 = 0;
    goto loc_0092B691;
loc_0092CCE0:
    result = RtlpValidTrustSubjectContext(0, (uint32_t)(*(uint32_t *)(v_stack_m290 + 0xC)) + 8, *(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x20), v_stack_m29C);
    goto loc_0092B28A;
loc_0092CD0A:
    goto loc_0092B8DF;
loc_0092CD14:
    local_r13 = 0;
    goto loc_0092B691;
loc_0092CD21:
    local_r13 = 0;
    goto loc_0092B691;
loc_0092CD2E:
    goto loc_0092B699;
loc_0092CD3C:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(*(uint32_t *)(v_stack_m290 + 0xC)) + 8, *(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x20), v_stack_m29C);
    local_rsp = (local_rsp) + (776);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0092AB50&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
