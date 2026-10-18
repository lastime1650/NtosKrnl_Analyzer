# sub_00B3C988

- RVA: `0x00B3C988`–`0x00B3D4A2` (길이 `2,842` bytes)
- VA: `0x0000000140B3C988`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B0FC0`
- 디코드: `661`개 명령, `2,842/2,842` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **65**; 고유 호출 대상: **32**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **18**

### Outgoing calls
- `0x00B3C9D4` → [EtwpCheckGuidAccess](../8C/EtwpCheckGuidAccess_function_008C697C.md) (function, `0x008C697C`)
- `0x00B3C9E3` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00B3CA23` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00B3CA5E` → [EtwpCheckGuidAccess](../8C/EtwpCheckGuidAccess_function_008C697C.md) (function, `0x008C697C`)
- `0x00B3CA6D` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00B3CB12` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00B3CB3E` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00B3CB6E` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x00B3CB77` → [NtSetIntervalProfile](../7D/NtSetIntervalProfile_function_007D2260.md) (function, `0x007D2260`)
- `0x00B3CB91` → [KeReleaseMutex](../../text/39/KeReleaseMutex_function_00396810.md) (function, `0x00396810`)
- `0x00B3CBFA` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x00B3CC1A` → [EtwpCheckSystemTraceAccess](../A8/EtwpCheckSystemTraceAccess_function_00A8DE44.md) (function, `0x00A8DE44`)
- `0x00B3CC31` → [EtwpUpdateGroupMasks](../A6/EtwpUpdateGroupMasks_function_00A67530.md) (function, `0x00A67530`)
- `0x00B3CC3E` → [EtwpReleaseLoggerContext](../A0/EtwpReleaseLoggerContext_function_00A04160.md) (function, `0x00A04160`)
- `0x00B3CC66` → [EtwpCheckGuidAccess](../8C/EtwpCheckGuidAccess_function_008C697C.md) (function, `0x008C697C`)
- `0x00B3CC7D` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00B3CC8A` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00B3CCC1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B3CCE1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00B3CCF1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B3CD03` → [EtwpSetPmcProfileSource](../7B/EtwpSetPmcProfileSource_function_007B8900.md) (function, `0x007B8900`)
- `0x00B3CD7A` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00B3CD87` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00B3CDC2` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x00B3CDDB` → [EtwpCheckLoggerControlAccess](../8C/EtwpCheckLoggerControlAccess_function_008C0AE0.md) (function, `0x008C0AE0`)
- `0x00B3CE37` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00B3CE61` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00B3CE9C` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x00B3CEC0` → [EtwpCheckSystemTraceAccess](../A8/EtwpCheckSystemTraceAccess_function_00A8DE44.md) (function, `0x00A8DE44`)
- `0x00B3CF04` → [EtwpUpdateTagFilter](../7B/EtwpUpdateTagFilter_function_007B7D04.md) (function, `0x007B7D04`)
- `0x00B3CF5B` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B3CF6A` → [EtwpUserInAdminOrLogUsersGroup](../7B/EtwpUserInAdminOrLogUsersGroup_function_007B7D50.md) (function, `0x007B7D50`)
- `0x00B3CFC0` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B3D000` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B3D015` → [EtwpGetMicroarchitecturalPmcAffinity](../7B/EtwpGetMicroarchitecturalPmcAffinity_function_007B67CC.md) (function, `0x007B67CC`)
- `0x00B3D027` → [wcsnlen](../../text/50/wcsnlen_function_00501D60.md) (function, `0x00501D60`)
- `0x00B3D044` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B3D065` → [wcsncpy_s](../../text/50/wcsncpy_s_function_00506650.md) (function, `0x00506650`)
- `0x00B3D083` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B3D097` → [EtwpRemoveMicroarchitecturalPmcFromRegistry](../7B/EtwpRemoveMicroarchitecturalPmcFromRegistry_function_007B7ACC.md) (function, `0x007B7ACC`)
- `0x00B3D0A9` → [EtwpUserInAdminOrLogUsersGroup](../7B/EtwpUserInAdminOrLogUsersGroup_function_007B7D50.md) (function, `0x007B7D50`)
- `0x00B3D0FA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00B3D120` → [wcsncpy_s](../../text/50/wcsncpy_s_function_00506650.md) (function, `0x00506650`)
- `0x00B3D14F` → [KiGetCpuVendor](../../pagelk/B7/KiGetCpuVendor_function_00B7D5B4.md) (function, `0x00B7D5B4`)
- `0x00B3D1E8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B3D20A` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00B3D21B` → [EtwpGetMicroarchitecturalPmcAffinity](../7B/EtwpGetMicroarchitecturalPmcAffinity_function_007B67CC.md) (function, `0x007B67CC`)
- `0x00B3D232` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00B3D24B` → [EtwpAddMicroarchitecturalPmcToRegistry](../7B/EtwpAddMicroarchitecturalPmcToRegistry_function_007B5558.md) (function, `0x007B5558`)
- `0x00B3D258` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00B3D2D2` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x00B3D2E9` → [EtwpCheckLoggerControlAccess](../8C/EtwpCheckLoggerControlAccess_function_008C0AE0.md) (function, `0x008C0AE0`)
- `0x00B3D302` → [EtwpUpdateLastBranchTracingConfiguration](../7C/EtwpUpdateLastBranchTracingConfiguration_function_007C0EFC.md) (function, `0x007C0EFC`)
- `0x00B3D328` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x00B3D33F` → [EtwpCheckLoggerControlAccess](../8C/EtwpCheckLoggerControlAccess_function_008C0AE0.md) (function, `0x008C0AE0`)
- `0x00B3D356` → [EtwpUpdateProcessorTraceConfiguration](../7C/EtwpUpdateProcessorTraceConfiguration_function_007C11BC.md) (function, `0x007C11BC`)
- `0x00B3D38D` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x00B3D3E3` → [EtwpAcquireLoggerContextByLoggerId](../93/EtwpAcquireLoggerContextByLoggerId_function_00932920.md) (function, `0x00932920`)
- `0x00B3D3FC` → [EtwpCheckLoggerControlAccess](../8C/EtwpCheckLoggerControlAccess_function_008C0AE0.md) (function, `0x008C0AE0`)
- `0x00B3D418` → [EtwpUpdateContextRegisterTraceEvents](../7B/EtwpUpdateContextRegisterTraceEvents_function_007B7B98.md) (function, `0x007B7B98`)
- `0x00B3D44B` → [EtwpUpdatePmcCounters](../AB/EtwpUpdatePmcCounters_function_00AB63AC.md) (function, `0x00AB63AC`)
- `0x00B3D460` → [EtwpUpdatePmcEvents](../7B/EtwpUpdatePmcEvents_function_007B7C58.md) (function, `0x007B7C58`)
- `0x00B3D475` → [EtwpUpdateLastBranchTracingEvents](../7C/EtwpUpdateLastBranchTracingEvents_function_007C0FA8.md) (function, `0x007C0FA8`)
- `0x00B3D48A` → [EtwpUpdateProcessorTraceEvents](../7C/EtwpUpdateProcessorTraceEvents_function_007C1264.md) (function, `0x007C1264`)
- `0x00B3D497` → [EtwpReleaseLoggerContext](../A0/EtwpReleaseLoggerContext_function_00A04160.md) (function, `0x00A04160`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B3C9CD` → RVA `0x00011F40` (`.rdata`; read)
- `0x00B3CA1C` → RVA `0x00EFF7A0` (`.data`; read)
- `0x00B3CA28` → RVA `0x00E0EB10` (`.data`; write)
- `0x00B3CA2E` → RVA `0x00E0EB18` (`.data`; write)
- `0x00B3CA35` → RVA `0x00E0EB14` (`.data`; write)
- `0x00B3CACB` → RVA `0x00FC50D4` (`ALMOSTRO`; read)
- `0x00B3CB17` → RVA `0x00FC50D4` (`ALMOSTRO`; write)
- `0x00B3CB1D` → RVA `0x00FC5150` (`ALMOSTRO`; write)
- `0x00B3CB24` → RVA `0x00FC5154` (`ALMOSTRO`; write)
- `0x00B3CB2B` → RVA `0x00FC5158` (`ALMOSTRO`; write)
- `0x00B3CB82` → RVA `0x00E0EB28` (`.data`; write)
- `0x00B3CC76` → RVA `0x00FD9B48` (`PAGEDATA`; read)
- `0x00B3CC9F` → RVA `0x00FD810C` (`PAGEDATA`; read)
- `0x00B3CDBB` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)
- `0x00B3CEDE` → RVA `0x00EFF940` (`.data`; read)
- `0x00B3CEE5` → RVA `0x00EFF880` (`.data`; read)
- `0x00B3CFA7` → RVA `0x00E00638` (`.data`; read)
- `0x00B3D06A` → RVA `0x00E00640` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **28**
  - `0x00B3C9E3` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x00B3CA23` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x00B3CA6D` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x00B3CB12` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x00B3CB3E` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x00B3CB6E` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x00B3CB91` → [KeReleaseMutex](../../text/39/KeReleaseMutex_function_00396810.md) (`PAGE` → `.text`)
  - `0x00B3CC8A` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x00B3CCC1` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00B3CCE1` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00B3CCF1` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B3CD87` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x00B3CE37` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
  - `0x00B3CE61` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00B3CF5B` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00B3CFC0` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00B3D000` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00B3D027` → [wcsnlen](../../text/50/wcsnlen_function_00501D60.md) (`PAGE` → `.text`)
  - `0x00B3D044` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00B3D065` → [wcsncpy_s](../../text/50/wcsncpy_s_function_00506650.md) (`PAGE` → `.text`)
  - `0x00B3D083` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00B3D0FA` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00B3D120` → [wcsncpy_s](../../text/50/wcsncpy_s_function_00506650.md) (`PAGE` → `.text`)
  - `0x00B3D14F` → [KiGetCpuVendor](../../pagelk/B7/KiGetCpuVendor_function_00B7D5B4.md) (`PAGE` → `PAGELK`)
  - `0x00B3D1E8` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00B3D20A` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00B3D232` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x00B3D258` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **54**
  - `0x00B3C9AE` → [EtwSetPerformanceTraceInformation + 0x92](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3C9C1` → [EtwSetPerformanceTraceInformation + 0x9C](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3C9DD` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CA09` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CA49` → [EtwSetPerformanceTraceInformation + 0x9C](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CA67` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CA92` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CAAE` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CAC6` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CAF1` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CAF8` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CB38` → [EtwSetPerformanceTraceInformation + 0x9C](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CB54` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CB97` → [EtwSetPerformanceTraceInformation + 0x186](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CBA0` → [EtwSetPerformanceTraceInformation + 0x9C](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CBC6` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CC05` → [EtwSetPerformanceTraceInformation + 0x21E](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CC48` → [EtwSetPerformanceTraceInformation + 0x181](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CC51` → [EtwSetPerformanceTraceInformation + 0x9C](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CC6D` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CCA6` → [EtwSetPerformanceTraceInformation + 0x228](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CCF8` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CD1D` → [EtwSetPerformanceTraceInformation + 0x9C](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CD2B` → [EtwSetPerformanceTraceInformation + 0x228](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CD3D` → [EtwSetPerformanceTraceInformation + 0x228](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CD5F` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CD6B` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CDCD` → [EtwSetPerformanceTraceInformation + 0x21E](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CE15` → [EtwSetPerformanceTraceInformation + 0x9C](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CE23` → [EtwSetPerformanceTraceInformation + 0x228](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CE31` → [EtwSetPerformanceTraceInformation + 0x228](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CE68` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CEA7` → [EtwSetPerformanceTraceInformation + 0x21E](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CF1A` → [EtwSetPerformanceTraceInformation + 0x92](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CF7B` → [EtwSetPerformanceTraceInformation + 0x9C](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CFA2` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3CFC9` → [EtwSetPerformanceTraceInformation + 0x186](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3D0BF` → [EtwSetPerformanceTraceInformation + 0x9C](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3D1EF` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3D25E` → [EtwSetPerformanceTraceInformation + 0x186](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3D268` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3D272` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3D27B` → [EtwSetPerformanceTraceInformation + 0x9C](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3D299` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3D2DD` → [EtwSetPerformanceTraceInformation + 0x21E](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3D333` → [EtwSetPerformanceTraceInformation + 0x21E](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3D36D` → [EtwSetPerformanceTraceInformation + 0x9C](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3D37B` → [EtwSetPerformanceTraceInformation + 0x228](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3D3B4` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3D3EE` → [EtwSetPerformanceTraceInformation + 0x21E](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3D424` → [EtwSetPerformanceTraceInformation + 0x186](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3D42E` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3D438` → [EtwSetPerformanceTraceInformation + 0x188](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)
  - `0x00B3D49D` → [EtwSetPerformanceTraceInformation + 0x181](../A5/EtwSetPerformanceTraceInformation_function_00A53928.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B3C988  0F 84 83 04 00 00               je 0x140b3ce11
00B3C98E  8B CB                           mov ecx, ebx
00B3C990  83 E9 01                        sub ecx, 1
00B3C993  0F 84 03 02 00 00               je 0x140b3cb9c
00B3C999  83 E9 02                        sub ecx, 2
00B3C99C  0F 84 92 01 00 00               je 0x140b3cb34
00B3C9A2  83 E9 02                        sub ecx, 2
00B3C9A5  0F 84 95 00 00 00               je 0x140b3ca40
00B3C9AB  83 E9 01                        sub ecx, 1
00B3C9AE  0F 84 06 70 F1 FF               je 0x140a539ba
00B3C9B4  83 F9 01                        cmp ecx, 1
00B3C9B7  0F 85 62 0A 00 00               jne 0x140b3d41f
00B3C9BD  41 83 FE 10                     cmp r14d, 0x10
00B3C9C1  0F 85 FD 6F F1 FF               jne 0x140a539c4
00B3C9C7  45 33 C0                        xor r8d, r8d
00B3C9CA  8D 51 7F                        lea edx, [rcx + 0x7f]
00B3C9CD  48 8D 0D 6C 55 4D FF            lea rcx, [rip - 0xb2aa94]
00B3C9D4  E8 A3 9F D8 FF                  call 0x1408c697c
00B3C9D9  8B D8                           mov ebx, eax
00B3C9DB  85 C0                           test eax, eax
00B3C9DD  0F 88 CD 70 F1 FF               js 0x140a53ab0
00B3C9E3  E8 F8 98 8F FF                  call 0x1404362e0
00B3C9E8  84 C0                           test al, al
00B3C9EA  0F 85 43 0A 00 00               jne 0x140b3d433
00B3C9F0  8B 77 04                        mov esi, dword ptr [rdi + 4]
00B3C9F3  89 74 24 58                     mov dword ptr [rsp + 0x58], esi
00B3C9F7  44 8B 77 08                     mov r14d, dword ptr [rdi + 8]
00B3C9FB  44 89 74 24 5C                  mov dword ptr [rsp + 0x5c], r14d
00B3CA00  8B 7F 0C                        mov edi, dword ptr [rdi + 0xc]
00B3CA03  89 7C 24 60                     mov dword ptr [rsp + 0x60], edi
00B3CA07  EB 05                           jmp 0x140b3ca0e
00B3CA09  E9 A2 70 F1 FF                  jmp 0x140a53ab0
00B3CA0E  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00B3CA14  45 33 C9                        xor r9d, r9d
00B3CA17  45 33 C0                        xor r8d, r8d
00B3CA1A  33 D2                           xor edx, edx
00B3CA1C  48 8D 0D 7D 2D 3C 00            lea rcx, [rip + 0x3c2d7d]
00B3CA23  E8 88 1C 6D FF                  call 0x14020e6b0
00B3CA28  89 35 E2 20 2D 00               mov dword ptr [rip + 0x2d20e2], esi
00B3CA2E  44 89 35 E3 20 2D 00            mov dword ptr [rip + 0x2d20e3], r14d
00B3CA35  89 3D D9 20 2D 00               mov dword ptr [rip + 0x2d20d9], edi
00B3CA3B  E9 48 01 00 00                  jmp 0x140b3cb88
00B3CA40  41 8D 46 F0                     lea eax, [r14 - 0x10]
00B3CA44  A9 FB FF FF FF                  test eax, 0xfffffffb
00B3CA49  0F 85 75 6F F1 FF               jne 0x140a539c4
00B3CA4F  45 33 C0                        xor r8d, r8d
00B3CA52  BA 80 00 00 00                  mov edx, 0x80
00B3CA57  48 8D 0D E2 54 4D FF            lea rcx, [rip - 0xb2ab1e]
00B3CA5E  E8 19 9F D8 FF                  call 0x1408c697c
00B3CA63  8B D8                           mov ebx, eax
00B3CA65  85 C0                           test eax, eax
00B3CA67  0F 88 43 70 F1 FF               js 0x140a53ab0
00B3CA6D  E8 6E 98 8F FF                  call 0x1404362e0
00B3CA72  84 C0                           test al, al
00B3CA74  0F 85 B9 09 00 00               jne 0x140b3d433
00B3CA7A  44 8B 7F 04                     mov r15d, dword ptr [rdi + 4]
00B3CA7E  44 89 7C 24 64                  mov dword ptr [rsp + 0x64], r15d
00B3CA83  BE 01 00 00 00                  mov esi, 1
00B3CA88  44 3B FE                        cmp r15d, esi
00B3CA8B  73 0A                           jae 0x140b3ca97
00B3CA8D  B8 0D 00 00 C0                  mov eax, 0xc000000d
00B3CA92  E9 19 70 F1 FF                  jmp 0x140a53ab0
00B3CA97  44 8B 67 08                     mov r12d, dword ptr [rdi + 8]
00B3CA9B  44 89 64 24 68                  mov dword ptr [rsp + 0x68], r12d
00B3CAA0  41 81 FC E8 03 00 00            cmp r12d, 0x3e8
00B3CAA7  73 0A                           jae 0x140b3cab3
00B3CAA9  B8 0D 00 00 C0                  mov eax, 0xc000000d
00B3CAAE  E9 FD 6F F1 FF                  jmp 0x140a53ab0
00B3CAB3  44 8B 6F 0C                     mov r13d, dword ptr [rdi + 0xc]
00B3CAB7  44 89 6C 24 6C                  mov dword ptr [rsp + 0x6c], r13d
00B3CABC  44 3B EE                        cmp r13d, esi
00B3CABF  73 0A                           jae 0x140b3cacb
00B3CAC1  B8 0D 00 00 C0                  mov eax, 0xc000000d
00B3CAC6  E9 E5 6F F1 FF                  jmp 0x140a53ab0
00B3CACB  8B 35 03 86 48 00               mov esi, dword ptr [rip + 0x488603]
00B3CAD1  89 74 24 48                     mov dword ptr [rsp + 0x48], esi
00B3CAD5  41 83 FE 14                     cmp r14d, 0x14
00B3CAD9  75 1B                           jne 0x140b3caf6
00B3CADB  8B 77 10                        mov esi, dword ptr [rdi + 0x10]
00B3CADE  89 74 24 48                     mov dword ptr [rsp + 0x48], esi
00B3CAE2  8D 46 FF                        lea eax, [rsi - 1]
00B3CAE5  3D 3E 42 0F 00                  cmp eax, 0xf423e
00B3CAEA  77 0A                           ja 0x140b3caf6
00B3CAEC  B8 0D 00 00 C0                  mov eax, 0xc000000d
00B3CAF1  E9 BA 6F F1 FF                  jmp 0x140a53ab0
00B3CAF6  EB 05                           jmp 0x140b3cafd
00B3CAF8  E9 B3 6F F1 FF                  jmp 0x140a53ab0
00B3CAFD  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00B3CB03  45 33 C9                        xor r9d, r9d
00B3CB06  45 33 C0                        xor r8d, r8d
00B3CB09  33 D2                           xor edx, edx
00B3CB0B  48 8D 0D 8E 2C 3C 00            lea rcx, [rip + 0x3c2c8e]
00B3CB12  E8 99 1B 6D FF                  call 0x14020e6b0
00B3CB17  89 35 B7 85 48 00               mov dword ptr [rip + 0x4885b7], esi
00B3CB1D  44 89 3D 2C 86 48 00            mov dword ptr [rip + 0x48862c], r15d
00B3CB24  44 89 25 29 86 48 00            mov dword ptr [rip + 0x488629], r12d
00B3CB2B  44 89 2D 26 86 48 00            mov dword ptr [rip + 0x488626], r13d
00B3CB32  EB 54                           jmp 0x140b3cb88
00B3CB34  41 83 FE 08                     cmp r14d, 8
00B3CB38  0F 85 86 6E F1 FF               jne 0x140a539c4
00B3CB3E  E8 9D 97 8F FF                  call 0x1404362e0
00B3CB43  84 C0                           test al, al
00B3CB45  0F 85 E8 08 00 00               jne 0x140b3d433
00B3CB4B  8B 7F 04                        mov edi, dword ptr [rdi + 4]
00B3CB4E  89 7C 24 70                     mov dword ptr [rsp + 0x70], edi
00B3CB52  EB 05                           jmp 0x140b3cb59
00B3CB54  E9 57 6F F1 FF                  jmp 0x140a53ab0
00B3CB59  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00B3CB5F  45 33 C9                        xor r9d, r9d
00B3CB62  45 33 C0                        xor r8d, r8d
00B3CB65  33 D2                           xor edx, edx
00B3CB67  48 8D 0D 32 2C 3C 00            lea rcx, [rip + 0x3c2c32]
00B3CB6E  E8 3D 1B 6D FF                  call 0x14020e6b0
00B3CB73  33 D2                           xor edx, edx
00B3CB75  8B CF                           mov ecx, edi
00B3CB77  E8 E4 56 C9 FF                  call 0x1407d2260
00B3CB7C  8B D8                           mov ebx, eax
00B3CB7E  85 C0                           test eax, eax
00B3CB80  78 06                           js 0x140b3cb88
00B3CB82  89 3D A0 1F 2D 00               mov dword ptr [rip + 0x2d1fa0], edi
00B3CB88  33 D2                           xor edx, edx
00B3CB8A  48 8D 0D 0F 2C 3C 00            lea rcx, [rip + 0x3c2c0f]
00B3CB91  E8 7A 9C 85 FF                  call 0x140396810
00B3CB96  90                              nop
00B3CB97  E9 12 6F F1 FF                  jmp 0x140a53aae
00B3CB9C  41 83 FE 30                     cmp r14d, 0x30
00B3CBA0  0F 85 1E 6E F1 FF               jne 0x140a539c4
00B3CBA6  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00B3CBAA  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B3CBAF  0F 10 47 10                     movups xmm0, xmmword ptr [rdi + 0x10]
00B3CBB3  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
00B3CBB8  0F 10 4F 20                     movups xmm1, xmmword ptr [rdi + 0x20]
00B3CBBC  0F 11 8C 24 88 00 00 00         movups xmmword ptr [rsp + 0x88], xmm1
00B3CBC4  EB 05                           jmp 0x140b3cbcb
00B3CBC6  E9 E5 6E F1 FF                  jmp 0x140a53ab0
00B3CBCB  0F B7 D0                        movzx edx, ax
00B3CBCE  81 FA FF FF 00 00               cmp edx, 0xffff
00B3CBD4  75 08                           jne 0x140b3cbde
00B3CBD6  41 0F B6 97 98 11 00 00         movzx edx, byte ptr [r15 + 0x1198]
00B3CBDE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00B3CBE7  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00B3CBEE  90                              nop
00B3CBEF  BE 01 00 00 00                  mov esi, 1
00B3CBF4  44 8A C6                        mov r8b, sil
00B3CBF7  49 8B CF                        mov rcx, r15
00B3CBFA  E8 21 5D DF FF                  call 0x140932920
00B3CBFF  48 8B F8                        mov rdi, rax
00B3CC02  48 85 C0                        test rax, rax
00B3CC05  0F 84 3B 6F F1 FF               je 0x140a53b46
00B3CC0B  48 8B C8                        mov rcx, rax
00B3CC0E  F7 40 0C 00 00 00 02            test dword ptr [rax + 0xc], 0x2000000
00B3CC15  74 24                           je 0x140b3cc3b
00B3CC17  8D 56 7F                        lea edx, [rsi + 0x7f]
00B3CC1A  E8 25 12 F5 FF                  call 0x140a8de44
00B3CC1F  8B D8                           mov ebx, eax
00B3CC21  85 C0                           test eax, eax
00B3CC23  0F 88 68 08 00 00               js 0x140b3d491
00B3CC29  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00B3CC2E  48 8B CF                        mov rcx, rdi
00B3CC31  E8 FA A8 F2 FF                  call 0x140a67530
00B3CC36  E9 54 08 00 00                  jmp 0x140b3d48f
00B3CC3B  40 8A D6                        mov dl, sil
00B3CC3E  E8 1D 75 EC FF                  call 0x140a04160
00B3CC43  BB 0D 00 00 C0                  mov ebx, 0xc000000d
00B3CC48  E9 5C 6E F1 FF                  jmp 0x140a53aa9
00B3CC4D  41 83 FE 10                     cmp r14d, 0x10
00B3CC51  0F 82 6D 6D F1 FF               jb 0x140a539c4
00B3CC57  45 33 C0                        xor r8d, r8d
00B3CC5A  BA 80 00 00 00                  mov edx, 0x80
00B3CC5F  48 8D 0D DA 52 4D FF            lea rcx, [rip - 0xb2ad26]
00B3CC66  E8 11 9D D8 FF                  call 0x1408c697c
00B3CC6B  85 C0                           test eax, eax
00B3CC6D  0F 88 3D 6E F1 FF               js 0x140a53ab0
00B3CC73  41 8A D4                        mov dl, r12b
00B3CC76  48 8B 0D CB CE 49 00            mov rcx, qword ptr [rip + 0x49cecb]
00B3CC7D  E8 9E 51 D3 FF                  call 0x140871e20
00B3CC82  84 C0                           test al, al
00B3CC84  0F 84 9F 07 00 00               je 0x140b3d429
00B3CC8A  E8 51 96 8F FF                  call 0x1404362e0
00B3CC8F  84 C0                           test al, al
00B3CC91  0F 85 9C 07 00 00               jne 0x140b3d433
00B3CC97  41 83 C6 F0                     add r14d, -0x10
00B3CC9B  41 C1 EE 02                     shr r14d, 2
00B3CC9F  44 3B 35 66 B4 49 00            cmp r14d, dword ptr [rip + 0x49b466]
00B3CCA6  0F 87 A4 6E F1 FF               ja 0x140a53b50
00B3CCAC  41 8B DE                        mov ebx, r14d
00B3CCAF  48 C1 E3 02                     shl rbx, 2
00B3CCB3  41 B8 45 74 77 58               mov r8d, 0x58777445
00B3CCB9  48 8B D3                        mov rdx, rbx
00B3CCBC  B9 40 00 00 00                  mov ecx, 0x40
00B3CCC1  E8 2A 54 04 00                  call 0x140b820f0
00B3CCC6  48 8B F0                        mov rsi, rax
00B3CCC9  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B3CCCE  48 85 C0                        test rax, rax
00B3CCD1  0F 84 8C 05 00 00               je 0x140b3d263
00B3CCD7  48 8D 57 10                     lea rdx, [rdi + 0x10]
00B3CCDB  4C 8B C3                        mov r8, rbx
00B3CCDE  48 8B C8                        mov rcx, rax
00B3CCE1  E8 5A 9B B8 FF                  call 0x1406c6840
00B3CCE6  EB 15                           jmp 0x140b3ccfd
00B3CCE8  8B D8                           mov ebx, eax
00B3CCEA  33 D2                           xor edx, edx
00B3CCEC  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00B3CCF1  E8 7A 5B 04 00                  call 0x140b82870
00B3CCF6  8B C3                           mov eax, ebx
00B3CCF8  E9 B3 6D F1 FF                  jmp 0x140a53ab0
00B3CCFD  41 8B D6                        mov edx, r14d
00B3CD00  48 8B CE                        mov rcx, rsi
00B3CD03  E8 F8 BB C7 FF                  call 0x1407b8900
00B3CD08  8B D8                           mov ebx, eax
00B3CD0A  33 D2                           xor edx, edx
00B3CD0C  48 8B CE                        mov rcx, rsi
00B3CD0F  E9 44 05 00 00                  jmp 0x140b3d258
00B3CD14  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
00B3CD19  41 83 FE 10                     cmp r14d, 0x10
00B3CD1D  0F 82 A1 6C F1 FF               jb 0x140a539c4
00B3CD23  41 83 C6 F0                     add r14d, -0x10
00B3CD27  41 F6 C6 03                     test r14b, 3
00B3CD2B  0F 85 1F 6E F1 FF               jne 0x140a53b50
00B3CD31  41 C1 EE 02                     shr r14d, 2
00B3CD35  BE 01 00 00 00                  mov esi, 1
00B3CD3A  44 3B F6                        cmp r14d, esi
00B3CD3D  0F 87 0D 6E F1 FF               ja 0x140a53b50
00B3CD43  48 8B 5F 08                     mov rbx, qword ptr [rdi + 8]
00B3CD47  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
00B3CD4C  45 85 F6                        test r14d, r14d
00B3CD4F  74 18                           je 0x140b3cd69
00B3CD51  81 7F 10 24 05 00 00            cmp dword ptr [rdi + 0x10], 0x524
00B3CD58  74 0A                           je 0x140b3cd64
00B3CD5A  B8 0D 00 00 C0                  mov eax, 0xc000000d
00B3CD5F  E9 4C 6D F1 FF                  jmp 0x140a53ab0
00B3CD64  40 88 74 24 30                  mov byte ptr [rsp + 0x30], sil
00B3CD69  EB 05                           jmp 0x140b3cd70
00B3CD6B  E9 40 6D F1 FF                  jmp 0x140a53ab0
00B3CD70  41 8A D4                        mov dl, r12b
00B3CD73  48 8B 0D CE CD 49 00            mov rcx, qword ptr [rip + 0x49cdce]
00B3CD7A  E8 A1 50 D3 FF                  call 0x140871e20
00B3CD7F  84 C0                           test al, al
00B3CD81  0F 84 A2 06 00 00               je 0x140b3d429
00B3CD87  E8 54 95 8F FF                  call 0x1404362e0
00B3CD8C  84 C0                           test al, al
00B3CD8E  0F 85 9F 06 00 00               jne 0x140b3d433
00B3CD94  0F B7 D3                        movzx edx, bx
00B3CD97  81 FA FF FF 00 00               cmp edx, 0xffff
00B3CD9D  75 08                           jne 0x140b3cda7
00B3CD9F  41 0F B6 97 98 11 00 00         movzx edx, byte ptr [r15 + 0x1198]
00B3CDA7  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00B3CDB0  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00B3CDB7  90                              nop
00B3CDB8  44 8A C6                        mov r8b, sil
00B3CDBB  48 8B 0D E6 9C 48 00            mov rcx, qword ptr [rip + 0x489ce6]
00B3CDC2  E8 59 5B DF FF                  call 0x140932920
00B3CDC7  48 8B F8                        mov rdi, rax
00B3CDCA  48 85 C0                        test rax, rax
00B3CDCD  0F 84 73 6D F1 FF               je 0x140a53b46
00B3CDD3  48 8B D0                        mov rdx, rax
00B3CDD6  B9 80 00 00 00                  mov ecx, 0x80
00B3CDDB  E8 00 3D D8 FF                  call 0x1408c0ae0
00B3CDE0  8B D8                           mov ebx, eax
00B3CDE2  85 C0                           test eax, eax
00B3CDE4  0F 88 A7 06 00 00               js 0x140b3d491
00B3CDEA  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
00B3CDEF  74 10                           je 0x140b3ce01
00B3CDF1  F0 81 8F 30 03 00 00 00 04 00 00  lock or dword ptr [rdi + 0x330], 0x400
00B3CDFC  E9 90 06 00 00                  jmp 0x140b3d491
00B3CE01  F0 81 A7 30 03 00 00 FF FB FF FF  lock and dword ptr [rdi + 0x330], 0xfffffbff
00B3CE0C  E9 80 06 00 00                  jmp 0x140b3d491
00B3CE11  41 83 FE 10                     cmp r14d, 0x10
00B3CE15  0F 82 A9 6B F1 FF               jb 0x140a539c4
00B3CE1B  41 83 C6 F0                     add r14d, -0x10
00B3CE1F  41 F6 C6 03                     test r14b, 3
00B3CE23  0F 85 27 6D F1 FF               jne 0x140a53b50
00B3CE29  41 C1 EE 02                     shr r14d, 2
00B3CE2D  66 44 3B F2                     cmp r14w, dx
00B3CE31  0F 87 19 6D F1 FF               ja 0x140a53b50
00B3CE37  E8 A4 94 8F FF                  call 0x1404362e0
00B3CE3C  84 C0                           test al, al
00B3CE3E  0F 85 EF 05 00 00               jne 0x140b3d433
00B3CE44  48 8B 5F 08                     mov rbx, qword ptr [rdi + 8]
00B3CE48  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
00B3CE4D  45 0F B7 C6                     movzx r8d, r14w
00B3CE51  49 C1 E0 02                     shl r8, 2
00B3CE55  48 8D 57 10                     lea rdx, [rdi + 0x10]
00B3CE59  48 8D 8C 24 B0 01 00 00         lea rcx, [rsp + 0x1b0]
00B3CE61  E8 DA 99 B8 FF                  call 0x1406c6840
00B3CE66  EB 05                           jmp 0x140b3ce6d
00B3CE68  E9 43 6C F1 FF                  jmp 0x140a53ab0
00B3CE6D  0F B7 D3                        movzx edx, bx
00B3CE70  81 FA FF FF 00 00               cmp edx, 0xffff
00B3CE76  75 08                           jne 0x140b3ce80
00B3CE78  41 0F B6 97 98 11 00 00         movzx edx, byte ptr [r15 + 0x1198]
00B3CE80  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00B3CE89  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00B3CE90  90                              nop
00B3CE91  BE 01 00 00 00                  mov esi, 1
00B3CE96  44 8A C6                        mov r8b, sil
00B3CE99  49 8B CF                        mov rcx, r15
00B3CE9C  E8 7F 5A DF FF                  call 0x140932920
00B3CEA1  48 8B F8                        mov rdi, rax
00B3CEA4  48 85 C0                        test rax, rax
00B3CEA7  0F 84 99 6C F1 FF               je 0x140a53b46
00B3CEAD  48 8B C8                        mov rcx, rax
00B3CEB0  F7 40 0C 00 00 00 02            test dword ptr [rax + 0xc], 0x2000000
00B3CEB7  0F 84 7E FD FF FF               je 0x140b3cc3b
00B3CEBD  8D 56 7F                        lea edx, [rsi + 0x7f]
00B3CEC0  E8 7F 0F F5 FF                  call 0x140a8de44
00B3CEC5  8B D8                           mov ebx, eax
00B3CEC7  85 C0                           test eax, eax
00B3CEC9  0F 88 C2 05 00 00               js 0x140b3d491
00B3CECF  0F B6 87 32 03 00 00            movzx eax, byte ptr [rdi + 0x332]
00B3CED6  48 8D 0C 80                     lea rcx, [rax + rax*4]
00B3CEDA  48 C1 E1 02                     shl rcx, 2
00B3CEDE  4C 8D 05 5B 2A 3C 00            lea r8, [rip + 0x3c2a5b]
00B3CEE5  48 8D 15 94 29 3C 00            lea rdx, [rip + 0x3c2994]
00B3CEEC  83 7C 24 44 0A                  cmp dword ptr [rsp + 0x44], 0xa
00B3CEF1  4C 0F 45 C2                     cmovne r8, rdx
00B3CEF5  4C 03 C1                        add r8, rcx
00B3CEF8  41 0F B7 D6                     movzx edx, r14w
00B3CEFC  48 8D 8C 24 B0 01 00 00         lea rcx, [rsp + 0x1b0]
00B3CF04  E8 FB AD C7 FF                  call 0x1407b7d04
00B3CF09  E9 83 05 00 00                  jmp 0x140b3d491
00B3CF0E  83 E9 01                        sub ecx, 1
00B3CF11  0F 84 60 03 00 00               je 0x140b3d277
00B3CF17  83 E9 01                        sub ecx, 1
00B3CF1A  0F 84 9A 6A F1 FF               je 0x140a539ba
00B3CF20  83 E9 01                        sub ecx, 1
00B3CF23  0F 84 7B 01 00 00               je 0x140b3d0a4
00B3CF29  83 F9 01                        cmp ecx, 1
00B3CF2C  0F 85 ED 04 00 00               jne 0x140b3d41f
00B3CF32  0F 57 C0                        xorps xmm0, xmm0
00B3CF35  33 C0                           xor eax, eax
00B3CF37  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
00B3CF3C  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
00B3CF44  89 84 24 A4 00 00 00            mov dword ptr [rsp + 0xa4], eax
00B3CF4B  33 D2                           xor edx, edx
00B3CF4D  41 B8 0C 01 00 00               mov r8d, 0x10c
00B3CF53  48 8D 8C 24 A0 00 00 00         lea rcx, [rsp + 0xa0]
00B3CF5B  E8 E0 9C B8 FF                  call 0x1406c6c40
00B3CF60  83 64 24 38 00                  and dword ptr [rsp + 0x38], 0
00B3CF65  45 84 E4                        test r12b, r12b
00B3CF68  74 0D                           je 0x140b3cf77
00B3CF6A  E8 E1 AD C7 FF                  call 0x1407b7d50
00B3CF6F  84 C0                           test al, al
00B3CF71  0F 84 BC 04 00 00               je 0x140b3d433
00B3CF77  41 83 FE 14                     cmp r14d, 0x14
00B3CF7B  0F 85 43 6A F1 FF               jne 0x140a539c4
00B3CF81  F2 0F 10 47 08                  movsd xmm0, qword ptr [rdi + 8]
00B3CF86  F2 0F 11 84 24 B0 01 00 00      movsd qword ptr [rsp + 0x1b0], xmm0
00B3CF8F  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
00B3CF92  89 84 24 B8 01 00 00            mov dword ptr [rsp + 0x1b8], eax
00B3CF99  8B 47 04                        mov eax, dword ptr [rdi + 4]
00B3CF9C  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
00B3CFA0  EB 05                           jmp 0x140b3cfa7
00B3CFA2  E9 09 6B F1 FF                  jmp 0x140a53ab0
00B3CFA7  48 8B 05 8A 36 2C 00            mov rax, qword ptr [rip + 0x2c368a]
00B3CFAE  4C 8D 4C 24 38                  lea r9, [rsp + 0x38]
00B3CFB3  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
00B3CFB8  BA 18 00 00 00                  mov edx, 0x18
00B3CFBD  8D 4A E9                        lea ecx, [rdx - 0x17]
00B3CFC0  E8 0B DB B7 FF                  call 0x1406baad0
00B3CFC5  8B D8                           mov ebx, eax
00B3CFC7  85 C0                           test eax, eax
00B3CFC9  0F 88 DF 6A F1 FF               js 0x140a53aae
00B3CFCF  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
00B3CFD3  89 84 24 A0 00 00 00            mov dword ptr [rsp + 0xa0], eax
00B3CFDA  C7 84 24 A8 00 00 00 01 00 20 00  mov dword ptr [rsp + 0xa8], 0x200001
00B3CFE5  83 A4 24 AC 00 00 00 00         and dword ptr [rsp + 0xac], 0
00B3CFED  41 BC 00 01 00 00               mov r12d, 0x100
00B3CFF3  45 8B C4                        mov r8d, r12d
00B3CFF6  33 D2                           xor edx, edx
00B3CFF8  48 8D 8C 24 B0 00 00 00         lea rcx, [rsp + 0xb0]
00B3D000  E8 3B 9C B8 FF                  call 0x1406c6c40
00B3D005  48 8D 94 24 A8 00 00 00         lea rdx, [rsp + 0xa8]
00B3D00D  48 8D 8C 24 B0 01 00 00         lea rcx, [rsp + 0x1b0]
00B3D015  E8 B2 97 C7 FF                  call 0x1407b67cc
00B3D01A  41 8D 54 24 FF                  lea edx, [r12 - 1]
00B3D01F  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
00B3D027  E8 34 4D 9C FF                  call 0x140501d60
00B3D02C  48 8B F0                        mov rsi, rax
00B3D02F  8D 48 01                        lea ecx, [rax + 1]
00B3D032  8B D9                           mov ebx, ecx
00B3D034  48 8D 14 09                     lea rdx, [rcx + rcx]
00B3D038  41 BF 45 74 77 50               mov r15d, 0x50777445
00B3D03E  45 8B C7                        mov r8d, r15d
00B3D041  41 8B CC                        mov ecx, r12d
00B3D044  E8 A7 50 04 00                  call 0x140b820f0
00B3D049  48 8B F8                        mov rdi, rax
00B3D04C  48 85 C0                        test rax, rax
00B3D04F  0F 84 0E 02 00 00               je 0x140b3d263
00B3D055  44 8B CE                        mov r9d, esi
00B3D058  4C 8B 84 24 88 00 00 00         mov r8, qword ptr [rsp + 0x88]
00B3D060  8B D3                           mov edx, ebx
00B3D062  48 8B C8                        mov rcx, rax
00B3D065  E8 E6 95 9C FF                  call 0x140506650
00B3D06A  48 8B 05 CF 35 2C 00            mov rax, qword ptr [rip + 0x2c35cf]
00B3D071  4C 8D 84 24 A0 00 00 00         lea r8, [rsp + 0xa0]
00B3D079  41 8D 54 24 10                  lea edx, [r12 + 0x10]
00B3D07E  B9 15 00 00 00                  mov ecx, 0x15
00B3D083  E8 48 DA B7 FF                  call 0x1406baad0
00B3D088  8B D8                           mov ebx, eax
00B3D08A  4C 8D 84 24 B0 01 00 00         lea r8, [rsp + 0x1b0]
00B3D092  8B D6                           mov edx, esi
00B3D094  48 8B CF                        mov rcx, rdi
00B3D097  E8 30 AA C7 FF                  call 0x1407b7acc
00B3D09C  48 8B CF                        mov rcx, rdi
00B3D09F  E9 B1 01 00 00                  jmp 0x140b3d255
00B3D0A4  45 84 E4                        test r12b, r12b
00B3D0A7  74 0D                           je 0x140b3d0b6
00B3D0A9  E8 A2 AC C7 FF                  call 0x1407b7d50
00B3D0AE  84 C0                           test al, al
00B3D0B0  0F 84 7D 03 00 00               je 0x140b3d433
00B3D0B6  41 8D 46 DC                     lea eax, [r14 - 0x24]
00B3D0BA  3D FC 01 00 00                  cmp eax, 0x1fc
00B3D0BF  0F 87 FF 68 F1 FF               ja 0x140a539c4
00B3D0C5  8A 47 04                        mov al, byte ptr [rdi + 4]
00B3D0C8  3C 02                           cmp al, 2
00B3D0CA  0F 82 9D 01 00 00               jb 0x140b3d26d
00B3D0D0  3C 03                           cmp al, 3
00B3D0D2  0F 87 95 01 00 00               ja 0x140b3d26d
00B3D0D8  41 8D 5E DE                     lea ebx, [r14 - 0x22]
00B3D0DC  44 8D AB 18 01 00 00            lea r13d, [rbx + 0x118]
00B3D0E3  D1 EB                           shr ebx, 1
00B3D0E5  41 8B D5                        mov edx, r13d
00B3D0E8  41 BF 45 74 77 50               mov r15d, 0x50777445
00B3D0EE  45 8B C7                        mov r8d, r15d
00B3D0F1  41 BC 00 01 00 00               mov r12d, 0x100
00B3D0F7  41 8B CC                        mov ecx, r12d
00B3D0FA  E8 F1 4F 04 00                  call 0x140b820f0
00B3D0FF  4C 8B F0                        mov r14, rax
00B3D102  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B3D107  48 85 C0                        test rax, rax
00B3D10A  0F 84 53 01 00 00               je 0x140b3d263
00B3D110  8B D3                           mov edx, ebx
00B3D112  4C 8D 47 22                     lea r8, [rdi + 0x22]
00B3D116  48 8D 88 18 01 00 00            lea rcx, [rax + 0x118]
00B3D11D  44 8B CB                        mov r9d, ebx
00B3D120  E8 2B 95 9C FF                  call 0x140506650
00B3D125  F2 0F 10 47 10                  movsd xmm0, qword ptr [rdi + 0x10]
00B3D12A  F2 0F 11 84 24 B0 01 00 00      movsd qword ptr [rsp + 0x1b0], xmm0
00B3D133  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
00B3D136  89 84 24 B8 01 00 00            mov dword ptr [rsp + 0x1b8], eax
00B3D13D  8B 47 1C                        mov eax, dword ptr [rdi + 0x1c]
00B3D140  41 89 46 08                     mov dword ptr [r14 + 8], eax
00B3D144  8A 47 20                        mov al, byte ptr [rdi + 0x20]
00B3D147  88 44 24 31                     mov byte ptr [rsp + 0x31], al
00B3D14B  88 44 24 40                     mov byte ptr [rsp + 0x40], al
00B3D14F  E8 60 04 04 00                  call 0x140b7d5b4
00B3D154  83 F8 02                        cmp eax, 2
00B3D157  75 2F                           jne 0x140b3d188
00B3D159  8A 47 08                        mov al, byte ptr [rdi + 8]
00B3D15C  80 7F 04 02                     cmp byte ptr [rdi + 4], 2
00B3D160  41 88 06                        mov byte ptr [r14], al
00B3D163  8A 47 09                        mov al, byte ptr [rdi + 9]
00B3D166  41 88 46 01                     mov byte ptr [r14 + 1], al
00B3D16A  8A 47 0A                        mov al, byte ptr [rdi + 0xa]
00B3D16D  41 88 46 02                     mov byte ptr [r14 + 2], al
00B3D171  8A 47 0B                        mov al, byte ptr [rdi + 0xb]
00B3D174  41 88 46 03                     mov byte ptr [r14 + 3], al
00B3D178  8A 47 0C                        mov al, byte ptr [rdi + 0xc]
00B3D17B  41 88 46 04                     mov byte ptr [r14 + 4], al
00B3D17F  8A 47 0D                        mov al, byte ptr [rdi + 0xd]
00B3D182  41 88 46 05                     mov byte ptr [r14 + 5], al
00B3D186  EB 52                           jmp 0x140b3d1da
00B3D188  BE 01 00 00 00                  mov esi, 1
00B3D18D  3B C6                           cmp eax, esi
00B3D18F  75 49                           jne 0x140b3d1da
00B3D191  80 7F 04 02                     cmp byte ptr [rdi + 4], 2
00B3D195  74 34                           je 0x140b3d1cb
00B3D197  0F B7 47 08                     movzx eax, word ptr [rdi + 8]
00B3D19B  66 41 89 06                     mov word ptr [r14], ax
00B3D19F  8A 47 0A                        mov al, byte ptr [rdi + 0xa]
00B3D1A2  41 88 46 02                     mov byte ptr [r14 + 2], al
00B3D1A6  8A 47 0B                        mov al, byte ptr [rdi + 0xb]
00B3D1A9  41 88 46 03                     mov byte ptr [r14 + 3], al
00B3D1AD  8A 47 0C                        mov al, byte ptr [rdi + 0xc]
00B3D1B0  41 88 46 04                     mov byte ptr [r14 + 4], al
00B3D1B4  8A 47 0D                        mov al, byte ptr [rdi + 0xd]
00B3D1B7  41 88 46 05                     mov byte ptr [r14 + 5], al
00B3D1BB  8A 47 0E                        mov al, byte ptr [rdi + 0xe]
00B3D1BE  41 88 46 06                     mov byte ptr [r14 + 6], al
00B3D1C2  8A 47 0F                        mov al, byte ptr [rdi + 0xf]
00B3D1C5  41 88 46 07                     mov byte ptr [r14 + 7], al
00B3D1C9  EB 0F                           jmp 0x140b3d1da
00B3D1CB  0F B6 47 08                     movzx eax, byte ptr [rdi + 8]
00B3D1CF  66 41 89 06                     mov word ptr [r14], ax
00B3D1D3  8A 47 09                        mov al, byte ptr [rdi + 9]
00B3D1D6  41 88 46 02                     mov byte ptr [r14 + 2], al
00B3D1DA  EB 18                           jmp 0x140b3d1f4
00B3D1DC  8B D8                           mov ebx, eax
00B3D1DE  BA 45 74 77 50                  mov edx, 0x50777445
00B3D1E3  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00B3D1E8  E8 83 56 04 00                  call 0x140b82870
00B3D1ED  8B C3                           mov eax, ebx
00B3D1EF  E9 BC 68 F1 FF                  jmp 0x140a53ab0
00B3D1F4  41 C7 46 10 01 00 20 00         mov dword ptr [r14 + 0x10], 0x200001
00B3D1FC  41 83 66 14 00                  and dword ptr [r14 + 0x14], 0
00B3D201  49 8D 4E 18                     lea rcx, [r14 + 0x18]
00B3D205  4D 8B C4                        mov r8, r12
00B3D208  33 D2                           xor edx, edx
00B3D20A  E8 31 9A B8 FF                  call 0x1406c6c40
00B3D20F  49 8D 56 10                     lea rdx, [r14 + 0x10]
00B3D213  48 8D 8C 24 B0 01 00 00         lea rcx, [rsp + 0x1b0]
00B3D21B  E8 AC 95 C7 FF                  call 0x1407b67cc
00B3D220  48 8B 05 19 34 2C 00            mov rax, qword ptr [rip + 0x2c3419]
00B3D227  4D 8B C6                        mov r8, r14
00B3D22A  41 8B D5                        mov edx, r13d
00B3D22D  B9 14 00 00 00                  mov ecx, 0x14
00B3D232  E8 99 D8 B7 FF                  call 0x1406baad0
00B3D237  8B D8                           mov ebx, eax
00B3D239  80 7C 24 31 00                  cmp byte ptr [rsp + 0x31], 0
00B3D23E  74 12                           je 0x140b3d252
00B3D240  48 8D 94 24 B0 01 00 00         lea rdx, [rsp + 0x1b0]
00B3D248  49 8B CE                        mov rcx, r14
00B3D24B  E8 08 83 C7 FF                  call 0x1407b5558
00B3D250  8B D8                           mov ebx, eax
00B3D252  49 8B CE                        mov rcx, r14
00B3D255  41 8B D7                        mov edx, r15d
00B3D258  E8 13 56 04 00                  call 0x140b82870
00B3D25D  90                              nop
00B3D25E  E9 4B 68 F1 FF                  jmp 0x140a53aae
00B3D263  B8 17 00 00 C0                  mov eax, 0xc0000017
00B3D268  E9 43 68 F1 FF                  jmp 0x140a53ab0
00B3D26D  B8 59 00 00 C0                  mov eax, 0xc0000059
00B3D272  E9 39 68 F1 FF                  jmp 0x140a53ab0
00B3D277  41 83 FE 18                     cmp r14d, 0x18
00B3D27B  0F 82 43 67 F1 FF               jb 0x140a539c4
00B3D281  0F 10 07                        movups xmm0, xmmword ptr [rdi]
00B3D284  0F 11 44 24 78                  movups xmmword ptr [rsp + 0x78], xmm0
00B3D289  F2 0F 10 4F 10                  movsd xmm1, qword ptr [rdi + 0x10]
00B3D28E  F2 0F 11 8C 24 88 00 00 00      movsd qword ptr [rsp + 0x88], xmm1
00B3D297  EB 05                           jmp 0x140b3d29e
00B3D299  E9 12 68 F1 FF                  jmp 0x140a53ab0
00B3D29E  0F B7 94 24 80 00 00 00         movzx edx, word ptr [rsp + 0x80]
00B3D2A6  81 FA FF FF 00 00               cmp edx, 0xffff
00B3D2AC  75 08                           jne 0x140b3d2b6
00B3D2AE  41 0F B6 97 98 11 00 00         movzx edx, byte ptr [r15 + 0x1198]
00B3D2B6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00B3D2BF  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00B3D2C6  90                              nop
00B3D2C7  BE 01 00 00 00                  mov esi, 1
00B3D2CC  44 8A C6                        mov r8b, sil
00B3D2CF  49 8B CF                        mov rcx, r15
00B3D2D2  E8 49 56 DF FF                  call 0x140932920
00B3D2D7  48 8B F8                        mov rdi, rax
00B3D2DA  48 85 C0                        test rax, rax
00B3D2DD  0F 84 63 68 F1 FF               je 0x140a53b46
00B3D2E3  48 8B D0                        mov rdx, rax
00B3D2E6  8D 4E 7F                        lea ecx, [rsi + 0x7f]
00B3D2E9  E8 F2 37 D8 FF                  call 0x1408c0ae0
00B3D2EE  8B D8                           mov ebx, eax
00B3D2F0  85 C0                           test eax, eax
00B3D2F2  0F 88 99 01 00 00               js 0x140b3d491
00B3D2F8  8B 94 24 88 00 00 00            mov edx, dword ptr [rsp + 0x88]
00B3D2FF  48 8B CF                        mov rcx, rdi
00B3D302  E8 F5 3B C8 FF                  call 0x1407c0efc
00B3D307  E9 83 01 00 00                  jmp 0x140b3d48f
00B3D30C  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00B3D315  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00B3D31C  90                              nop
00B3D31D  BE 01 00 00 00                  mov esi, 1
00B3D322  44 8A C6                        mov r8b, sil
00B3D325  49 8B CF                        mov rcx, r15
00B3D328  E8 F3 55 DF FF                  call 0x140932920
00B3D32D  48 8B F8                        mov rdi, rax
00B3D330  48 85 C0                        test rax, rax
00B3D333  0F 84 0D 68 F1 FF               je 0x140a53b46
00B3D339  48 8B D0                        mov rdx, rax
00B3D33C  8D 4E 7F                        lea ecx, [rsi + 0x7f]
00B3D33F  E8 9C 37 D8 FF                  call 0x1408c0ae0
00B3D344  8B D8                           mov ebx, eax
00B3D346  85 C0                           test eax, eax
00B3D348  0F 88 43 01 00 00               js 0x140b3d491
00B3D34E  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
00B3D353  48 8B CF                        mov rcx, rdi
00B3D356  E8 61 3E C8 FF                  call 0x1407c11bc
00B3D35B  E9 2F 01 00 00                  jmp 0x140b3d48f
00B3D360  83 F9 01                        cmp ecx, 1
00B3D363  0F 85 B6 00 00 00               jne 0x140b3d41f
00B3D369  41 83 FE 14                     cmp r14d, 0x14
00B3D36D  0F 82 51 66 F1 FF               jb 0x140a539c4
00B3D373  41 83 C6 EC                     add r14d, -0x14
00B3D377  41 F6 C6 03                     test r14b, 3
00B3D37B  0F 85 CF 67 F1 FF               jne 0x140a53b50
00B3D381  8B F1                           mov esi, ecx
00B3D383  40 8A D6                        mov dl, sil
00B3D386  48 8B 0D BB C7 49 00            mov rcx, qword ptr [rip + 0x49c7bb]
00B3D38D  E8 8E 4A D3 FF                  call 0x140871e20
00B3D392  84 C0                           test al, al
00B3D394  0F 84 8F 00 00 00               je 0x140b3d429
00B3D39A  41 C1 EE 02                     shr r14d, 2
00B3D39E  4C 8D 67 14                     lea r12, [rdi + 0x14]
00B3D3A2  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
00B3D3A5  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
00B3D3A9  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
00B3D3AD  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
00B3D3B2  EB 05                           jmp 0x140b3d3b9
00B3D3B4  E9 F7 66 F1 FF                  jmp 0x140a53ab0
00B3D3B9  0F B7 D0                        movzx edx, ax
00B3D3BC  81 FA FF FF 00 00               cmp edx, 0xffff
00B3D3C2  75 08                           jne 0x140b3d3cc
00B3D3C4  41 0F B6 97 98 11 00 00         movzx edx, byte ptr [r15 + 0x1198]
00B3D3CC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00B3D3D5  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
00B3D3DC  90                              nop
00B3D3DD  44 8A C6                        mov r8b, sil
00B3D3E0  49 8B CF                        mov rcx, r15
00B3D3E3  E8 38 55 DF FF                  call 0x140932920
00B3D3E8  48 8B F8                        mov rdi, rax
00B3D3EB  48 85 C0                        test rax, rax
00B3D3EE  0F 84 52 67 F1 FF               je 0x140a53b46
00B3D3F4  48 8B D0                        mov rdx, rax
00B3D3F7  B9 80 00 00 00                  mov ecx, 0x80
00B3D3FC  E8 DF 36 D8 FF                  call 0x1408c0ae0
00B3D401  8B D8                           mov ebx, eax
00B3D403  85 C0                           test eax, eax
00B3D405  0F 88 86 00 00 00               js 0x140b3d491
00B3D40B  45 8B CE                        mov r9d, r14d
00B3D40E  4D 8B C4                        mov r8, r12
00B3D411  8B 54 24 4C                     mov edx, dword ptr [rsp + 0x4c]
00B3D415  48 8B CF                        mov rcx, rdi
00B3D418  E8 7B A7 C7 FF                  call 0x1407b7b98
00B3D41D  EB 70                           jmp 0x140b3d48f
00B3D41F  BB 02 00 00 C0                  mov ebx, 0xc0000002
00B3D424  E9 85 66 F1 FF                  jmp 0x140a53aae
00B3D429  B8 61 00 00 C0                  mov eax, 0xc0000061
00B3D42E  E9 7D 66 F1 FF                  jmp 0x140a53ab0
00B3D433  B8 22 00 00 C0                  mov eax, 0xc0000022
00B3D438  E9 73 66 F1 FF                  jmp 0x140a53ab0
00B3D43D  83 F8 0F                        cmp eax, 0xf
00B3D440  75 10                           jne 0x140b3d452
00B3D442  45 8B C6                        mov r8d, r14d
00B3D445  49 8B D4                        mov rdx, r12
00B3D448  48 8B CF                        mov rcx, rdi
00B3D44B  E8 5C 8F F7 FF                  call 0x140ab63ac
00B3D450  EB 3D                           jmp 0x140b3d48f
00B3D452  83 F8 0E                        cmp eax, 0xe
00B3D455  75 10                           jne 0x140b3d467
00B3D457  45 8B C6                        mov r8d, r14d
00B3D45A  49 8B D4                        mov rdx, r12
00B3D45D  48 8B CF                        mov rcx, rdi
00B3D460  E8 F3 A7 C7 FF                  call 0x1407b7c58
00B3D465  EB 28                           jmp 0x140b3d48f
00B3D467  83 F8 14                        cmp eax, 0x14
00B3D46A  75 10                           jne 0x140b3d47c
00B3D46C  45 8B C6                        mov r8d, r14d
00B3D46F  49 8B D4                        mov rdx, r12
00B3D472  48 8B CF                        mov rcx, rdi
00B3D475  E8 2E 3B C8 FF                  call 0x1407c0fa8
00B3D47A  EB 15                           jmp 0x140b3d491
00B3D47C  83 F8 18                        cmp eax, 0x18
00B3D47F  75 10                           jne 0x140b3d491
00B3D481  45 8B C6                        mov r8d, r14d
00B3D484  49 8B D4                        mov rdx, r12
00B3D487  48 8B CF                        mov rcx, rdi
00B3D48A  E8 D5 3D C8 FF                  call 0x1407c1264
00B3D48F  8B D8                           mov ebx, eax
00B3D491  40 8A D6                        mov dl, sil
00B3D494  48 8B CF                        mov rcx, rdi
00B3D497  E8 C4 6C EC FF                  call 0x140a04160
00B3D49C  90                              nop
00B3D49D  E9 07 66 F1 FF                  jmp 0x140a53aa9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B3C988(__int64 a1, __int64 a2, int a3, int a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27, __int64 a28, __int64 a29, __int64 a30, __int64 a31, __int64 a32, __int64 a33, __int64 a34, __int64 a35, __int64 a36, __int64 a37, __int64 a38, __int64 a39, __int64 a40, __int64 a41, __int64 a42, __int64 a43, __int64 a44, __int64 a45, __int64 a46, __int64 a47, __int64 a48, __int64 a49, __int64 a50, __int64 a51, __int64 a52, __int64 a53, __int64 a54)
{
    __int64 result;
    __int64 v_r14;
    unsigned __int64 v_stack_p1B0;
    unsigned int v_stack_p1B8;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned __int8 v_stack_p31;
    unsigned __int64 v_stack_p38;
    unsigned __int8 v_stack_p40;
    unsigned int v_stack_p44;
    unsigned int v_stack_p48;
    unsigned int v_stack_p4C;
    unsigned int v_stack_p58;
    unsigned int v_stack_p5C;
    unsigned int v_stack_p60;
    unsigned int v_stack_p64;
    unsigned int v_stack_p68;
    unsigned int v_stack_p6C;
    unsigned int v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int16 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int64 v_stack_pA0;
    unsigned int v_stack_pA4;
    unsigned int v_stack_pA8;
    unsigned int v_stack_pAC;
    unsigned __int64 v_stack_pB0;

    if (condition_is_equal) goto loc_00B3CE11;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) - (1));
    if (condition_is_equal) goto loc_00B3CB9C;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00B3CB34;
    a1 = (unsigned int)((a1) - (2));
    if (condition_is_equal) goto loc_00B3CA40;
    a1 = (unsigned int)((a1) - (1));
    if (((unsigned int)(a1)) != 1) goto loc_00B3D41F;
    a3 = 0;
    result = EtwpCheckGuidAccess(v_rip - 11709076, a1 + 127, a3, a4);
    result = PsIsCurrentThreadInServerSilo(v_rip - 11709076, a1 + 127, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00B3D433;
    v_stack_p58 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 4)));
    v_stack_p5C = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8)));
    v_stack_p60 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 12)));
    goto loc_00B3CA0E;
loc_00B3CA0E:
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_rip + 3943805, a2, a3, a4);
    *(unsigned int *)(v_rip + 2957538) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 4)));
    *(unsigned int *)(v_rip + 2957539) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8)));
    *(unsigned int *)(v_rip + 2957529) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 12)));
    goto loc_00B3CB88;
loc_00B3CA40:
    a3 = 0;
    result = EtwpCheckGuidAccess(v_rip - 11709214, 128, a3, a4);
    result = PsIsCurrentThreadInServerSilo(v_rip - 11709214, 128, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00B3D433;
    v_stack_p64 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 12)) + 4)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 12)) + 4)))) >= 1) goto loc_00B3CA97;
loc_00B3CA97:
    v_stack_p68 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 12)) + 8)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 12)) + 8)))) >= 1000) goto loc_00B3CAB3;
loc_00B3CAB3:
    v_stack_p6C = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 12)) + 12)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 12)) + 12)))) >= 1) goto loc_00B3CACB;
loc_00B3CACB:
    v_stack_p48 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4752899)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 8)))) != 20) goto loc_00B3CAF6;
    v_stack_p48 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 12)) + 16)));
    if (((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 12)) + 16)) - 1)) > 0xF423EULL) goto loc_00B3CAF6;
loc_00B3CAF6:
    goto loc_00B3CAFD;
loc_00B3CAFD:
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_rip + 3943566, a2, a3, a4);
    *(unsigned int *)(v_rip + 4752823) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 12)) + 16)));
    *(unsigned int *)(v_rip + 4752940) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 12)) + 4)));
    *(unsigned int *)(v_rip + 4752937) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 12)) + 8)));
    *(unsigned int *)(v_rip + 4752934) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 12)) + 12)));
    goto loc_00B3CB88;
loc_00B3CB34:
    result = PsIsCurrentThreadInServerSilo(v_rip + 3943566, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00B3D433;
    v_stack_p70 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 12)) + 4)));
    goto loc_00B3CB59;
loc_00B3CB59:
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_rip + 3943474, a2, a3, a4);
    a2 = 0;
    result = NtSetIntervalProfile((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 12)) + 4)))), a2, a3, a4);
    if (!(sign_flag)) {
        *(unsigned int *)(v_rip + 2957216) = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 12)) + 4)));
    }
    a2 = 0;
    result = KeReleaseMutex(v_rip + 3943439, a2, a3, a4);
loc_00B3CB9C:
    v_stack_p38 = *(unsigned __int64 *)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 12)) + 4)) + 8);
    a15 = v_xmm0;
    a17 = v_xmm1;
    goto loc_00B3CBCB;
loc_00B3CBCB:
    if (((unsigned int)((unsigned __int16)(*(unsigned __int64 *)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 12)) + 4)) + 8)))) == 0xFFFFULL) {
        a2 = *(unsigned __int8 *)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 12)) + 4)) + 4504);
    }
    result = EtwpAcquireLoggerContextByLoggerId((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 12)) + 4)), a2, 1, a4);
    if (((*(unsigned int *)(result + 12)) & (0x2000000ULL)) == 0) goto loc_00B3CC3B;
    result = EtwpCheckSystemTraceAccess(result, 1 + 127, 1, a4);
    if (sign_flag) goto loc_00B3D491;
    result = EtwpUpdateGroupMasks(result, a15, 1, a4);
    goto loc_00B3D48F;
loc_00B3CC3B:
    result = EtwpReleaseLoggerContext(result, 1, 1, a4);
loc_00B3CE11:
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rdi + 8))) + (-16));
    v_r14 = (unsigned int)((v_r14) >> (2));
    result = PsIsCurrentThreadInServerSilo(result, 1, 1, a4);
    if ((unsigned __int8)(result) != 0) goto loc_00B3D433;
    v_stack_p38 = *(unsigned __int64 *)(result + 8);
    a3 = ((unsigned __int16)(v_r14)) << (2);
    result = memcpy(a54, result + 16, a3, a4);
    goto loc_00B3CE6D;
loc_00B3CE6D:
    if (((unsigned int)((unsigned __int16)(*(unsigned __int64 *)(result + 8)))) == 0xFFFFULL) {
        a2 = *(unsigned __int8 *)((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 12)) + 4)) + 4504);
    }
    result = EtwpAcquireLoggerContextByLoggerId((unsigned int)(*(unsigned int *)((unsigned int)(*(unsigned int *)(v_rdi + 12)) + 4)), a2, 1, a4);
    if (((*(unsigned int *)(result + 12)) & (0x2000000ULL)) == 0) goto loc_00B3CC3B;
    result = EtwpCheckSystemTraceAccess(result, 1 + 127, 1, a4);
    if (sign_flag) goto loc_00B3D491;
    a1 = (*(unsigned __int8 *)(result + 818) + *(unsigned __int8 *)(result + 818) * 4) << (2);
    a3 = v_rip + 3943003;
    if (v_stack_p44 != 10) { a3 = v_rip + 3942804; }
    a3 = (a3) + (a1);
    result = EtwpUpdateTagFilter(a54, (unsigned __int16)(v_r14), a3, a4);
    goto loc_00B3D491;
loc_00B3D41F:
loc_00B3D433:
loc_00B3D48F:
loc_00B3D491:
    result = EtwpReleaseLoggerContext(result, 1, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B3C988(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, int64_t Arg15, uint64_t Arg16, int64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, uint64_t Arg24, uint64_t Arg25, uint64_t Arg26, uint64_t Arg27, uint64_t Arg28, uint64_t Arg29, uint64_t Arg30, uint64_t Arg31, uint64_t Arg32, uint64_t Arg33, uint64_t Arg34, uint64_t Arg35, uint64_t Arg36, uint64_t Arg37, uint64_t Arg38, uint64_t Arg39, uint64_t Arg40, uint64_t Arg41, uint64_t Arg42, uint64_t Arg43, uint64_t Arg44, uint64_t Arg45, uint64_t Arg46, uint64_t Arg47, uint64_t Arg48, uint64_t Arg49, uint64_t Arg50, uint64_t Arg51, uint64_t Arg52, uint64_t Arg53, int64_t Arg54)
{
    int64_t result;
    int64_t local_r14;
    uint64_t v_stack_p1B0;
    uint32_t v_stack_p1B8;
    uint64_t v_stack_p20;
    uint8_t v_stack_p30;
    uint8_t v_stack_p31;
    uint64_t v_stack_p38;
    uint8_t v_stack_p40;
    uint32_t v_stack_p44;
    uint32_t v_stack_p48;
    uint32_t v_stack_p4C;
    uint32_t v_stack_p58;
    uint32_t v_stack_p5C;
    uint32_t v_stack_p60;
    uint32_t v_stack_p64;
    uint32_t v_stack_p68;
    uint32_t v_stack_p6C;
    uint32_t v_stack_p70;
    uint64_t v_stack_p78;
    uint16_t v_stack_p80;
    uint64_t v_stack_p88;
    uint64_t v_stack_pA0;
    uint32_t v_stack_pA4;
    uint32_t v_stack_pA8;
    uint32_t v_stack_pAC;
    uint64_t v_stack_pB0;

    if (condition_is_equal) goto loc_00B3CE11;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) - (1));
    if (condition_is_equal) goto loc_00B3CB9C;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00B3CB34;
    Arg1 = (uint32_t)((Arg1) - (2));
    if (condition_is_equal) goto loc_00B3CA40;
    Arg1 = (uint32_t)((Arg1) - (1));
    if (((uint32_t)(Arg1)) != 1) goto loc_00B3D41F;
    Arg3 = 0;
    result = EtwpCheckGuidAccess(v_rip - 11709076, Arg1 + 127, Arg3, Arg4);
    result = PsIsCurrentThreadInServerSilo(v_rip - 11709076, Arg1 + 127, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00B3D433;
    v_stack_p58 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
    v_stack_p5C = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)));
    v_stack_p60 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)));
    goto loc_00B3CA0E;
loc_00B3CA0E:
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_rip + 3943805, Arg2, Arg3, Arg4);
    *(uint32_t *)(v_rip + 0x2D20E2) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x4)));
    *(uint32_t *)(v_rip + 0x2D20E3) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)));
    *(uint32_t *)(v_rip + 0x2D20D9) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)));
    goto loc_00B3CB88;
loc_00B3CA40:
    Arg3 = 0;
    result = EtwpCheckGuidAccess(v_rip - 11709214, 128, Arg3, Arg4);
    result = PsIsCurrentThreadInServerSilo(v_rip - 11709214, 128, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00B3D433;
    v_stack_p64 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 0x4)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 0x4)))) >= 1) goto loc_00B3CA97;
loc_00B3CA97:
    v_stack_p68 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 0x8)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 0x8)))) >= 1000) goto loc_00B3CAB3;
loc_00B3CAB3:
    v_stack_p6C = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 0xC)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 0xC)))) >= 1) goto loc_00B3CACB;
loc_00B3CACB:
    v_stack_p48 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x488603)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x8)))) != 20) goto loc_00B3CAF6;
    v_stack_p48 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 0x10)));
    if (((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 0x10)) - 1)) > 0xF423EULL) goto loc_00B3CAF6;
loc_00B3CAF6:
    goto loc_00B3CAFD;
loc_00B3CAFD:
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_rip + 3943566, Arg2, Arg3, Arg4);
    *(uint32_t *)(v_rip + 0x4885B7) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 0x10)));
    *(uint32_t *)(v_rip + 0x48862C) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 0x4)));
    *(uint32_t *)(v_rip + 0x488629) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 0x8)));
    *(uint32_t *)(v_rip + 0x488626) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 0xC)));
    goto loc_00B3CB88;
loc_00B3CB34:
    result = PsIsCurrentThreadInServerSilo(v_rip + 3943566, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00B3D433;
    v_stack_p70 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 0x4)));
    goto loc_00B3CB59;
loc_00B3CB59:
    Arg4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_rip + 3943474, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = NtSetIntervalProfile((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 0x4)))), Arg2, Arg3, Arg4);
    if (!(sign_flag)) {
        *(uint32_t *)(v_rip + 0x2D1FA0) = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 0x4)));
    }
    Arg2 = 0;
    result = KeReleaseMutex(v_rip + 3943439, Arg2, Arg3, Arg4);
loc_00B3CB9C:
    v_stack_p38 = *(uint64_t *)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 0x4)) + 0x8);
    Arg15 = v_xmm0;
    Arg17 = v_xmm1;
    goto loc_00B3CBCB;
loc_00B3CBCB:
    if (((uint32_t)((uint16_t)(*(uint64_t *)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 0x4)) + 0x8)))) == 0xFFFFULL) {
        Arg2 = *(uint8_t *)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 0x4)) + 0x1198);
    }
    result = EtwpAcquireLoggerContextByLoggerId((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 0x4)), Arg2, 1, Arg4);
    if (((*(uint32_t *)(result + 0xC)) & (0x2000000ULL)) == 0) goto loc_00B3CC3B;
    result = EtwpCheckSystemTraceAccess(result, 1 + 127, 1, Arg4);
    if (sign_flag) goto loc_00B3D491;
    result = EtwpUpdateGroupMasks(result, Arg15, 1, Arg4);
    goto loc_00B3D48F;
loc_00B3CC3B:
    result = EtwpReleaseLoggerContext(result, 1, 1, Arg4);
loc_00B3CE11:
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(local_rdi + 0x8))) + (-16));
    local_r14 = (uint32_t)((local_r14) >> (2));
    result = PsIsCurrentThreadInServerSilo(result, 1, 1, Arg4);
    if ((uint8_t)(result) != 0) goto loc_00B3D433;
    v_stack_p38 = *(uint64_t *)(result + 0x8);
    Arg3 = ((uint16_t)(local_r14)) << (2);
    result = memcpy(Arg54, result + 16, Arg3, Arg4);
    goto loc_00B3CE6D;
loc_00B3CE6D:
    if (((uint32_t)((uint16_t)(*(uint64_t *)(result + 0x8)))) == 0xFFFFULL) {
        Arg2 = *(uint8_t *)((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 0x4)) + 0x1198);
    }
    result = EtwpAcquireLoggerContextByLoggerId((uint32_t)(*(uint32_t *)((uint32_t)(*(uint32_t *)(local_rdi + 0xC)) + 0x4)), Arg2, 1, Arg4);
    if (((*(uint32_t *)(result + 0xC)) & (0x2000000ULL)) == 0) goto loc_00B3CC3B;
    result = EtwpCheckSystemTraceAccess(result, 1 + 127, 1, Arg4);
    if (sign_flag) goto loc_00B3D491;
    Arg1 = (*(uint8_t *)(result + 0x332) + *(uint8_t *)(result + 0x332) * 4) << (2);
    Arg3 = v_rip + 3943003;
    if (v_stack_p44 != 10) { Arg3 = v_rip + 3942804; }
    Arg3 = (Arg3) + (Arg1);
    result = EtwpUpdateTagFilter(Arg54, (uint16_t)(local_r14), Arg3, Arg4);
    goto loc_00B3D491;
loc_00B3D41F:
loc_00B3D433:
loc_00B3D48F:
loc_00B3D491:
    result = EtwpReleaseLoggerContext(result, 1, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B3C988&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
