# NtQueryInformationThread

- RVA: `0x00AE3760`–`0x00AE5360` (길이 `7,168` bytes)
- VA: `0x0000000140AE3760`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000CEAB4`
- 디코드: `1,702`개 명령, `7,168/7,168` bytes 표시
- 미해석 바이트: `4` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **102**; 고유 호출 대상: **39**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x00AE381B` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AE3960` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE397B` → [PsGetThreadExitStatus](../A6/PsGetThreadExitStatus_function_00A65500.md) (function, `0x00A65500`)
- `0x00AE39A6` → [IoThreadToProcess](../../text/44/IoThreadToProcess_function_00448540.md) (function, `0x00448540`)
- `0x00AE3A18` → [VslpEnterIumSecureMode](../../text/23/VslpEnterIumSecureMode_function_00235E50.md) (function, `0x00235E50`)
- `0x00AE3A68` → [KeQueryBasePriorityThread](../../text/41/KeQueryBasePriorityThread_function_0041E500.md) (function, `0x0041E500`)
- `0x00AE3A7C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE3AEE` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE3B0C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE3B60` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE3B8C` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00AE3BA1` → [KeQueryUserAffinityThread](../../text/49/KeQueryUserAffinityThread_function_00496234.md) (function, `0x00496234`)
- `0x00AE3BF8` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE3C3E` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE3C84` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE3CDE` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE3CEB` → [BvgaSetVirtualFrameBuffer](../../text/4F/BvgaSetVirtualFrameBuffer_function_004FC600.md) (function, `0x004FC600`)
- `0x00AE3CFC` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE3D40` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE3D5C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE3DAC` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE3DC5` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE3E4C` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE3E6E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE3EC1` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE3EE6` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE3F39` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE3F5C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE3FB0` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE3FD5` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE4028` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE4093` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE40AE` → [PspQueryLastCallThread](../A6/PspQueryLastCallThread_function_00A62CE8.md) (function, `0x00A62CE8`)
- `0x00AE40F1` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE4122` → [PsGetIoPriorityThread](../../text/34/PsGetIoPriorityThread_function_00343930.md) (function, `0x00343930`)
- `0x00AE4146` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE4198` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE41BF` → [KeQueryTotalCycleTimeThread](../../text/37/KeQueryTotalCycleTimeThread_function_0037EF20.md) (function, `0x0037EF20`)
- `0x00AE4206` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE424B` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE4278` → [PsGetPagePriorityThread](../../text/3C/PsGetPagePriorityThread_function_003C3E80.md) (function, `0x003C3E80`)
- `0x00AE42B9` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (function, `0x006BC9D0`)
- `0x00AE42D1` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x00AE4315` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE433D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE4381` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE43E9` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00AE43FA` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE449F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AE44E7` → [MiCopyVirtualMemory](../9B/MiCopyVirtualMemory_function_009BBB50.md) (function, `0x009BBB50`)
- `0x00AE44F7` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00AE4504` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE4565` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE45A5` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE45FE` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE4622` → [KeSetIdealProcessorThreadByNumber](../../text/2D/KeSetIdealProcessorThreadByNumber_function_002DD200.md) (function, `0x002DD200`)
- `0x00AE4631` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE467D` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE4699` → [PspWow64GetContextThread](../A1/PspWow64GetContextThread_function_00A11E90.md) (function, `0x00A11E90`)
- `0x00AE46AA` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE4707` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE477F` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE478E` → [Feature_SuspendThread2__private_IsEnabledNoReportingNoInline](../../text/5C/Feature_SuspendThread2__private_IsEnabledNoReportingNoInline_function_005C357C.md) (function, `0x005C357C`)
- `0x00AE479F` → [KeQueryTotalSuspendCountThread](../../text/5B/KeQueryTotalSuspendCountThread_function_005B8EF8.md) (function, `0x005B8EF8`)
- `0x00AE47D9` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE481E` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE4839` → [KeQueryHeteroCpuPolicyThread](../../text/48/KeQueryHeteroCpuPolicyThread_function_00488A70.md) (function, `0x00488A70`)
- `0x00AE487A` → [PsGetEffectiveContainerId](../../text/44/PsGetEffectiveContainerId_function_004497A0.md) (function, `0x004497A0`)
- `0x00AE48E8` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE4909` → [KeQueryCpuSetsThread](../../text/3C/KeQueryCpuSetsThread_function_003C7F9C.md) (function, `0x003C7F9C`)
- `0x00AE491F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE4948` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AE4993` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE49B7` → [KeQueryValuesThread](../../text/30/KeQueryValuesThread_function_0030EE30.md) (function, `0x0030EE30`)
- `0x00AE4AFF` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE4B1E` → [KeQueryPrimaryGroupAffinityThread](../../text/3C/KeQueryPrimaryGroupAffinityThread_function_003C7238.md) (function, `0x003C7238`)
- `0x00AE4B49` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE4B8E` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE4C03` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE4C2F` → [PspLockThreadSecurityShared](../../text/3C/PspLockThreadSecurityShared_function_003C4720.md) (function, `0x003C4720`)
- `0x00AE4C90` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x00AE4CD0` → [PspUnlockThreadSecurityShared](../../text/3C/PspUnlockThreadSecurityShared_function_003C2E40.md) (function, `0x003C2E40`)
- `0x00AE4CE4` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE4D2A` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE4D8F` → [PsGetWorkOnBehalfThread](../../text/43/PsGetWorkOnBehalfThread_function_00439560.md) (function, `0x00439560`)
- `0x00AE4DAC` → [PsEncodeThreadWorkOnBehalfTicket](../../text/44/PsEncodeThreadWorkOnBehalfTicket_function_0044BC70.md) (function, `0x0044BC70`)
- `0x00AE4DBB` → [PsEncodeThreadWorkOnBehalfTicket](../../text/44/PsEncodeThreadWorkOnBehalfTicket_function_0044BC70.md) (function, `0x0044BC70`)
- `0x00AE4DC7` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x00AE4E29` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE4EEB` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE4F00` → [KeGetThreadPpmPolicy](../../text/4F/KeGetThreadPpmPolicy_function_004FD358.md) (function, `0x004FD358`)
- `0x00AE4FB8` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE500B` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE50C4` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE510F` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00AE5167` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AE518B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00AE51AA` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (function, `0x006BA570`)
- `0x00AE51CB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x00AE522D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x00AE5246` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00AE5267` → [ExRaiseDatatypeMisalignment](../89/ExRaiseDatatypeMisalignment_function_00899FD0.md) (function, `0x00899FD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00AE377B` → RVA `0x00E0A740` (`.data`; read)
- `0x00AE3910` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00AE3931` → RVA `0x00FC6AC8` (`ALMOSTRO`; read)
- `0x00AE3C4B` → RVA `0x00FC6AA0` (`ALMOSTRO`; read)
- `0x00AE4C45` → RVA `0x00AFCAD0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE4E45` → RVA `0x00F06570` (`.data`; read)
- `0x00AE52EF` → RVA `0x-3A50FEC6` (`image boundary/outside`; read/write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **63**
  - `0x00AE381B` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AE39A6` → [IoThreadToProcess](../../text/44/IoThreadToProcess_function_00448540.md) (`PAGE` → `.text`)
  - `0x00AE3A18` → [VslpEnterIumSecureMode](../../text/23/VslpEnterIumSecureMode_function_00235E50.md) (`PAGE` → `.text`)
  - `0x00AE3A68` → [KeQueryBasePriorityThread](../../text/41/KeQueryBasePriorityThread_function_0041E500.md) (`PAGE` → `.text`)
  - `0x00AE3A7C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE3B0C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE3B8C` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00AE3BA1` → [KeQueryUserAffinityThread](../../text/49/KeQueryUserAffinityThread_function_00496234.md) (`PAGE` → `.text`)
  - `0x00AE3BF8` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE3C84` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE3CEB` → [BvgaSetVirtualFrameBuffer](../../text/4F/BvgaSetVirtualFrameBuffer_function_004FC600.md) (`PAGE` → `.text`)
  - `0x00AE3CFC` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE3D5C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE3DC5` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE3E6E` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE3EE6` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE3F5C` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE3FD5` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE4122` → [PsGetIoPriorityThread](../../text/34/PsGetIoPriorityThread_function_00343930.md) (`PAGE` → `.text`)
  - `0x00AE4146` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE41BF` → [KeQueryTotalCycleTimeThread](../../text/37/KeQueryTotalCycleTimeThread_function_0037EF20.md) (`PAGE` → `.text`)
  - `0x00AE4206` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE4278` → [PsGetPagePriorityThread](../../text/3C/PsGetPagePriorityThread_function_003C3E80.md) (`PAGE` → `.text`)
  - `0x00AE42B9` → [RtlCopyVolatileMemory](../../text/6B/RtlCopyVolatileMemory_function_006BC9D0.md) (`PAGE` → `.text`)
  - `0x00AE433D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE4381` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE43E9` → [ExAcquireRundownProtection](../../text/21/ExAcquireRundownProtection_function_00216620.md) (`PAGE` → `.text`)
  - `0x00AE43FA` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE449F` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AE44F7` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x00AE4504` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE45A5` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE4622` → [KeSetIdealProcessorThreadByNumber](../../text/2D/KeSetIdealProcessorThreadByNumber_function_002DD200.md) (`PAGE` → `.text`)
  - `0x00AE4631` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE46AA` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE478E` → [Feature_SuspendThread2__private_IsEnabledNoReportingNoInline](../../text/5C/Feature_SuspendThread2__private_IsEnabledNoReportingNoInline_function_005C357C.md) (`PAGE` → `.text`)
  - `0x00AE479F` → [KeQueryTotalSuspendCountThread](../../text/5B/KeQueryTotalSuspendCountThread_function_005B8EF8.md) (`PAGE` → `.text`)
  - `0x00AE47D9` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE4839` → [KeQueryHeteroCpuPolicyThread](../../text/48/KeQueryHeteroCpuPolicyThread_function_00488A70.md) (`PAGE` → `.text`)
  - `0x00AE487A` → [PsGetEffectiveContainerId](../../text/44/PsGetEffectiveContainerId_function_004497A0.md) (`PAGE` → `.text`)
  - `0x00AE4909` → [KeQueryCpuSetsThread](../../text/3C/KeQueryCpuSetsThread_function_003C7F9C.md) (`PAGE` → `.text`)
  - `0x00AE491F` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE4948` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AE49B7` → [KeQueryValuesThread](../../text/30/KeQueryValuesThread_function_0030EE30.md) (`PAGE` → `.text`)
  - `0x00AE4B1E` → [KeQueryPrimaryGroupAffinityThread](../../text/3C/KeQueryPrimaryGroupAffinityThread_function_003C7238.md) (`PAGE` → `.text`)
  - `0x00AE4B49` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE4C2F` → [PspLockThreadSecurityShared](../../text/3C/PspLockThreadSecurityShared_function_003C4720.md) (`PAGE` → `.text`)
  - `0x00AE4C90` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00AE4CD0` → [PspUnlockThreadSecurityShared](../../text/3C/PspUnlockThreadSecurityShared_function_003C2E40.md) (`PAGE` → `.text`)
  - `0x00AE4CE4` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE4D8F` → [PsGetWorkOnBehalfThread](../../text/43/PsGetWorkOnBehalfThread_function_00439560.md) (`PAGE` → `.text`)
  - `0x00AE4DAC` → [PsEncodeThreadWorkOnBehalfTicket](../../text/44/PsEncodeThreadWorkOnBehalfTicket_function_0044BC70.md) (`PAGE` → `.text`)
  - `0x00AE4DBB` → [PsEncodeThreadWorkOnBehalfTicket](../../text/44/PsEncodeThreadWorkOnBehalfTicket_function_0044BC70.md) (`PAGE` → `.text`)
  - `0x00AE4DC7` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x00AE4F00` → [KeGetThreadPpmPolicy](../../text/4F/KeGetThreadPpmPolicy_function_004FD358.md) (`PAGE` → `.text`)
  - `0x00AE4FB8` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE50C4` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE5167` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AE518B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00AE51AA` → [ExpInterlockedPopEntrySList](../../text/6B/ExpInterlockedPopEntrySList_function_006BA570.md) (`PAGE` → `.text`)
  - `0x00AE51CB` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x00AE522D` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x00AE5246` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AE3760  40 53                           push rbx
00AE3762  56                              push rsi
00AE3763  57                              push rdi
00AE3764  41 54                           push r12
00AE3766  41 55                           push r13
00AE3768  41 56                           push r14
00AE376A  41 57                           push r15
00AE376C  48 81 EC 20 04 00 00            sub rsp, 0x420
00AE3773  0F 29 B4 24 10 04 00 00         movaps xmmword ptr [rsp + 0x410], xmm6
00AE377B  48 8B 05 BE 6F 32 00            mov rax, qword ptr [rip + 0x326fbe]
00AE3782  48 33 C4                        xor rax, rsp
00AE3785  48 89 84 24 00 04 00 00         mov qword ptr [rsp + 0x400], rax
00AE378D  45 8B F9                        mov r15d, r9d
00AE3790  4D 8B F0                        mov r14, r8
00AE3793  44 8B EA                        mov r13d, edx
00AE3796  89 54 24 54                     mov dword ptr [rsp + 0x54], edx
00AE379A  48 8B D9                        mov rbx, rcx
00AE379D  48 8B B4 24 80 04 00 00         mov rsi, qword ptr [rsp + 0x480]
00AE37A5  48 89 8C 24 90 00 00 00         mov qword ptr [rsp + 0x90], rcx
00AE37AD  48 89 B4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rsi
00AE37B5  33 C0                           xor eax, eax
00AE37B7  89 84 24 14 01 00 00            mov dword ptr [rsp + 0x114], eax
00AE37BE  33 FF                           xor edi, edi
00AE37C0  48 89 BC 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], rdi
00AE37C8  0F 57 C0                        xorps xmm0, xmm0
00AE37CB  0F 11 84 24 40 01 00 00         movups xmmword ptr [rsp + 0x140], xmm0
00AE37D3  89 84 24 50 01 00 00            mov dword ptr [rsp + 0x150], eax
00AE37DA  0F 11 84 24 A8 00 00 00         movups xmmword ptr [rsp + 0xa8], xmm0
00AE37E2  0F 57 C9                        xorps xmm1, xmm1
00AE37E5  0F 11 8C 24 C8 00 00 00         movups xmmword ptr [rsp + 0xc8], xmm1
00AE37ED  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00AE37F2  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00AE37F6  0F 11 84 24 58 01 00 00         movups xmmword ptr [rsp + 0x158], xmm0
00AE37FE  0F 11 84 24 68 01 00 00         movups xmmword ptr [rsp + 0x168], xmm0
00AE3806  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
00AE380B  33 D2                           xor edx, edx
00AE380D  41 B8 00 01 00 00               mov r8d, 0x100
00AE3813  48 8D 8C 24 F8 01 00 00         lea rcx, [rsp + 0x1f8]
00AE381B  E8 20 34 BE FF                  call 0x1406c6c40
00AE3820  48 89 BC 24 98 00 00 00         mov qword ptr [rsp + 0x98], rdi
00AE3828  0F 57 C0                        xorps xmm0, xmm0
00AE382B  0F 11 84 24 F0 00 00 00         movups xmmword ptr [rsp + 0xf0], xmm0
00AE3833  0F 11 84 24 00 01 00 00         movups xmmword ptr [rsp + 0x100], xmm0
00AE383B  65 4C 8B 14 25 88 01 00 00      mov r10, qword ptr gs:[0x188]
00AE3844  4C 89 94 24 80 00 00 00         mov qword ptr [rsp + 0x80], r10
00AE384C  4C 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], r10
00AE3854  45 0F B6 A2 32 02 00 00         movzx r12d, byte ptr [r10 + 0x232]
00AE385C  45 84 E4                        test r12b, r12b
00AE385F  0F 84 83 00 00 00               je 0x140ae38e8
00AE3865  44 8D 4F 04                     lea r9d, [rdi + 4]
00AE3869  41 83 FD 26                     cmp r13d, 0x26
00AE386D  74 1D                           je 0x140ae388c
00AE386F  41 83 FD 31                     cmp r13d, 0x31
00AE3873  44 8D 6F 08                     lea r13d, [rdi + 8]
00AE3877  74 0E                           je 0x140ae3887
00AE3879  B8 01 00 00 00                  mov eax, 1
00AE387E  45 3B F9                        cmp r15d, r9d
00AE3881  41 0F 43 C1                     cmovae eax, r9d
00AE3885  EB 0E                           jmp 0x140ae3895
00AE3887  41 8B C1                        mov eax, r9d
00AE388A  EB 09                           jmp 0x140ae3895
00AE388C  41 BD 08 00 00 00               mov r13d, 8
00AE3892  41 8B C5                        mov eax, r13d
00AE3895  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
00AE3899  45 85 FF                        test r15d, r15d
00AE389C  74 29                           je 0x140ae38c7
00AE389E  8D 48 FF                        lea ecx, [rax - 1]
00AE38A1  49 85 CE                        test r14, rcx
00AE38A4  0F 85 BD 19 00 00               jne 0x140ae5267
00AE38AA  4B 8D 14 3E                     lea rdx, [r14 + r15]
00AE38AE  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
00AE38B8  48 3B D1                        cmp rdx, rcx
00AE38BB  77 05                           ja 0x140ae38c2
00AE38BD  49 3B D6                        cmp rdx, r14
00AE38C0  73 0F                           jae 0x140ae38d1
00AE38C2  0F B6 01                        movzx eax, byte ptr [rcx]
00AE38C5  EB 0A                           jmp 0x140ae38d1
00AE38C7  48 B9 00 00 FF FF FF 7F 00 00   movabs rcx, 0x7fffffff0000
00AE38D1  48 85 F6                        test rsi, rsi
00AE38D4  74 0B                           je 0x140ae38e1
00AE38D6  48 3B F1                        cmp rsi, rcx
00AE38D9  48 0F 42 CE                     cmovb rcx, rsi
00AE38DD  8B 01                           mov eax, dword ptr [rcx]
00AE38DF  89 01                           mov dword ptr [rcx], eax
00AE38E1  EB 0F                           jmp 0x140ae38f2
00AE38E3  E9 53 19 00 00                  jmp 0x140ae523b
00AE38E8  41 B9 04 00 00 00               mov r9d, 4
00AE38EE  45 8D 69 04                     lea r13d, [r9 + 4]
00AE38F2  89 BC 24 14 01 00 00            mov dword ptr [rsp + 0x114], edi
00AE38F9  F3 0F 7F 84 24 20 01 00 00      movdqu xmmword ptr [rsp + 0x120], xmm0
00AE3902  48 63 44 24 54                  movsxd rax, dword ptr [rsp + 0x54]
00AE3907  83 F8 3B                        cmp eax, 0x3b
00AE390A  0F 87 26 19 00 00               ja 0x140ae5236
00AE3910  48 8D 15 E9 C6 51 FF            lea rdx, [rip - 0xae3917]
00AE3917  8B 8C 82 70 52 AE 00            mov ecx, dword ptr [rdx + rax*4 + 0xae5270]
00AE391E  48 03 CA                        add rcx, rdx
00AE3921  FF E1                           jmp rcx
00AE3923  CC                              int3
00AE3924  CC                              int3
00AE3925  CC                              int3
00AE3926  CC                              int3
00AE3927  41 83 FF 30                     cmp r15d, 0x30
00AE392B  0F 85 A5 17 00 00               jne 0x140ae50d6
00AE3931  4C 8B 05 90 31 4E 00            mov r8, qword ptr [rip + 0x4e3190]
00AE3938  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE393D  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE3942  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE3947  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE394C  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE3954  45 0F B6 CC                     movzx r9d, r12b
00AE3958  BA 00 08 00 00                  mov edx, 0x800
00AE395D  48 8B CB                        mov rcx, rbx
00AE3960  E8 EB 5C D8 FF                  call 0x140869650
00AE3965  85 C0                           test eax, eax
00AE3967  0F 88 CE 18 00 00               js 0x140ae523b
00AE396D  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AE3972  80 7B 04 00                     cmp byte ptr [rbx + 4], 0
00AE3976  74 11                           je 0x140ae3989
00AE3978  48 8B CB                        mov rcx, rbx
00AE397B  E8 80 1B F8 FF                  call 0x140a65500
00AE3980  89 84 24 10 01 00 00            mov dword ptr [rsp + 0x110], eax
00AE3987  EB 0B                           jmp 0x140ae3994
00AE3989  C7 84 24 10 01 00 00 03 01 00 00  mov dword ptr [rsp + 0x110], 0x103
00AE3994  4C 8B BB F0 00 00 00            mov r15, qword ptr [rbx + 0xf0]
00AE399B  4C 89 BC 24 18 01 00 00         mov qword ptr [rsp + 0x118], r15
00AE39A3  48 8B CB                        mov rcx, rbx
00AE39A6  E8 95 4B 96 FF                  call 0x140448540
00AE39AB  F6 80 70 01 00 00 01            test byte ptr [rax + 0x170], 1
00AE39B2  74 7C                           je 0x140ae3a30
00AE39B4  0F 57 C0                        xorps xmm0, xmm0
00AE39B7  33 C0                           xor eax, eax
00AE39B9  0F 11 84 24 80 01 00 00         movups xmmword ptr [rsp + 0x180], xmm0
00AE39C1  0F 11 84 24 90 01 00 00         movups xmmword ptr [rsp + 0x190], xmm0
00AE39C9  0F 11 84 24 A0 01 00 00         movups xmmword ptr [rsp + 0x1a0], xmm0
00AE39D1  0F 11 84 24 B0 01 00 00         movups xmmword ptr [rsp + 0x1b0], xmm0
00AE39D9  0F 11 84 24 C0 01 00 00         movups xmmword ptr [rsp + 0x1c0], xmm0
00AE39E1  0F 11 84 24 D0 01 00 00         movups xmmword ptr [rsp + 0x1d0], xmm0
00AE39E9  48 89 84 24 E0 01 00 00         mov qword ptr [rsp + 0x1e0], rax
00AE39F1  8B 83 1C 03 00 00               mov eax, dword ptr [rbx + 0x31c]
00AE39F7  48 89 84 24 88 01 00 00         mov qword ptr [rsp + 0x188], rax
00AE39FF  48 89 9C 24 90 01 00 00         mov qword ptr [rsp + 0x190], rbx
00AE3A07  4C 8D 8C 24 80 01 00 00         lea r9, [rsp + 0x180]
00AE3A0F  45 33 C0                        xor r8d, r8d
00AE3A12  66 BA 0D 00                     mov dx, 0xd
00AE3A16  B1 02                           mov cl, 2
00AE3A18  E8 33 24 75 FF                  call 0x140235e50
00AE3A1D  85 C0                           test eax, eax
00AE3A1F  4C 0F 49 BC 24 90 01 00 00      cmovns r15, qword ptr [rsp + 0x190]
00AE3A28  4C 89 BC 24 18 01 00 00         mov qword ptr [rsp + 0x118], r15
00AE3A30  0F 10 B3 08 05 00 00            movups xmm6, xmmword ptr [rbx + 0x508]
00AE3A37  0F B7 83 30 02 00 00            movzx eax, word ptr [rbx + 0x230]
00AE3A3E  48 8B 8B 28 02 00 00            mov rcx, qword ptr [rbx + 0x228]
00AE3A45  66 3B 01                        cmp ax, word ptr [rcx]
00AE3A48  73 05                           jae 0x140ae3a4f
00AE3A4A  48 8B 7C C1 08                  mov rdi, qword ptr [rcx + rax*8 + 8]
00AE3A4F  48 89 BC 24 30 01 00 00         mov qword ptr [rsp + 0x130], rdi
00AE3A57  0F BE 83 C3 00 00 00            movsx eax, byte ptr [rbx + 0xc3]
00AE3A5E  89 84 24 38 01 00 00            mov dword ptr [rsp + 0x138], eax
00AE3A65  48 8B CB                        mov rcx, rbx
00AE3A68  E8 93 AA 93 FF                  call 0x14041e500
00AE3A6D  89 84 24 3C 01 00 00            mov dword ptr [rsp + 0x13c], eax
00AE3A74  BA 50 73 51 79                  mov edx, 0x79517350
00AE3A79  48 8B CB                        mov rcx, rbx
00AE3A7C  E8 5F 3E 81 FF                  call 0x1402f78e0
00AE3A81  90                              nop
00AE3A82  0F 10 84 24 10 01 00 00         movups xmm0, xmmword ptr [rsp + 0x110]
00AE3A8A  41 0F 11 06                     movups xmmword ptr [r14], xmm0
00AE3A8E  41 0F 11 76 10                  movups xmmword ptr [r14 + 0x10], xmm6
00AE3A93  0F 10 84 24 30 01 00 00         movups xmm0, xmmword ptr [rsp + 0x130]
00AE3A9B  41 0F 11 46 20                  movups xmmword ptr [r14 + 0x20], xmm0
00AE3AA0  48 85 F6                        test rsi, rsi
00AE3AA3  74 06                           je 0x140ae3aab
00AE3AA5  C7 06 30 00 00 00               mov dword ptr [rsi], 0x30
00AE3AAB  E9 34 13 00 00                  jmp 0x140ae4de4
00AE3AB0  E9 86 17 00 00                  jmp 0x140ae523b
00AE3AB5  41 83 FF 04                     cmp r15d, 4
00AE3AB9  0F 85 17 16 00 00               jne 0x140ae50d6
00AE3ABF  4C 8B 05 02 30 4E 00            mov r8, qword ptr [rip + 0x4e3002]
00AE3AC6  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE3ACB  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE3AD0  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE3AD5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE3ADA  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE3AE2  45 0F B6 CC                     movzx r9d, r12b
00AE3AE6  BA 00 08 00 00                  mov edx, 0x800
00AE3AEB  48 8B CB                        mov rcx, rbx
00AE3AEE  E8 5D 5B D8 FF                  call 0x140869650
00AE3AF3  85 C0                           test eax, eax
00AE3AF5  0F 88 40 17 00 00               js 0x140ae523b
00AE3AFB  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE3B00  0F BE 99 33 02 00 00            movsx ebx, byte ptr [rcx + 0x233]
00AE3B07  BA 50 73 51 79                  mov edx, 0x79517350
00AE3B0C  E8 CF 3D 81 FF                  call 0x1402f78e0
00AE3B11  90                              nop
00AE3B12  41 89 1E                        mov dword ptr [r14], ebx
00AE3B15  48 85 F6                        test rsi, rsi
00AE3B18  74 03                           je 0x140ae3b1d
00AE3B1A  44 89 3E                        mov dword ptr [rsi], r15d
00AE3B1D  E9 C2 12 00 00                  jmp 0x140ae4de4
00AE3B22  E9 14 17 00 00                  jmp 0x140ae523b
00AE3B27  41 83 FF 10                     cmp r15d, 0x10
00AE3B2B  0F 85 A5 15 00 00               jne 0x140ae50d6
00AE3B31  4C 8B 05 90 2F 4E 00            mov r8, qword ptr [rip + 0x4e2f90]
00AE3B38  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE3B3D  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE3B42  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE3B47  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE3B4C  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE3B54  45 0F B6 CC                     movzx r9d, r12b
00AE3B58  BA 00 08 00 00                  mov edx, 0x800
00AE3B5D  48 8B CB                        mov rcx, rbx
00AE3B60  E8 EB 5A D8 FF                  call 0x140869650
00AE3B65  44 8B F8                        mov r15d, eax
00AE3B68  85 C0                           test eax, eax
00AE3B6A  0F 88 CB 16 00 00               js 0x140ae523b
00AE3B70  48 C7 84 24 F0 01 00 00 01 00 20 00  mov qword ptr [rsp + 0x1f0], 0x200001
00AE3B7C  33 D2                           xor edx, edx
00AE3B7E  41 B8 00 01 00 00               mov r8d, 0x100
00AE3B84  48 8D 8C 24 F8 01 00 00         lea rcx, [rsp + 0x1f8]
00AE3B8C  E8 AF 30 BE FF                  call 0x1406c6c40
00AE3B91  48 8D 94 24 F0 01 00 00         lea rdx, [rsp + 0x1f0]
00AE3B99  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AE3B9E  48 8B CB                        mov rcx, rbx
00AE3BA1  E8 8E 26 9B FF                  call 0x140496234
00AE3BA6  0F B7 83 30 02 00 00            movzx eax, word ptr [rbx + 0x230]
00AE3BAD  66 89 84 24 B0 00 00 00         mov word ptr [rsp + 0xb0], ax
00AE3BB5  66 3B 84 24 F0 01 00 00         cmp ax, word ptr [rsp + 0x1f0]
00AE3BBD  73 08                           jae 0x140ae3bc7
00AE3BBF  48 8B BC C4 F8 01 00 00         mov rdi, qword ptr [rsp + rax*8 + 0x1f8]
00AE3BC7  48 89 BC 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rdi
00AE3BCF  0F 10 84 24 A8 00 00 00         movups xmm0, xmmword ptr [rsp + 0xa8]
00AE3BD7  41 0F 11 06                     movups xmmword ptr [r14], xmm0
00AE3BDB  48 85 F6                        test rsi, rsi
00AE3BDE  74 06                           je 0x140ae3be6
00AE3BE0  C7 06 10 00 00 00               mov dword ptr [rsi], 0x10
00AE3BE6  EB 08                           jmp 0x140ae3bf0
00AE3BE8  44 8B F8                        mov r15d, eax
00AE3BEB  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AE3BF0  BA 50 73 51 79                  mov edx, 0x79517350
00AE3BF5  48 8B CB                        mov rcx, rbx
00AE3BF8  E8 E3 3C 81 FF                  call 0x1402f78e0
00AE3BFD  41 8B C7                        mov eax, r15d
00AE3C00  E9 36 16 00 00                  jmp 0x140ae523b
00AE3C05  41 83 FF 20                     cmp r15d, 0x20
00AE3C09  0F 85 C7 14 00 00               jne 0x140ae50d6
00AE3C0F  4C 8B 05 B2 2E 4E 00            mov r8, qword ptr [rip + 0x4e2eb2]
00AE3C16  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE3C1B  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE3C20  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE3C25  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE3C2A  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE3C32  45 0F B6 CC                     movzx r9d, r12b
00AE3C36  BA 00 08 00 00                  mov edx, 0x800
00AE3C3B  48 8B CB                        mov rcx, rbx
00AE3C3E  E8 0D 5A D8 FF                  call 0x140869650
00AE3C43  85 C0                           test eax, eax
00AE3C45  0F 88 F0 15 00 00               js 0x140ae523b
00AE3C4B  8B 05 4F 2E 4E 00               mov eax, dword ptr [rip + 0x4e2e4f]
00AE3C51  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE3C56  8B 99 8C 02 00 00               mov ebx, dword ptr [rcx + 0x28c]
00AE3C5C  48 0F AF D8                     imul rbx, rax
00AE3C60  44 8B B9 DC 02 00 00            mov r15d, dword ptr [rcx + 0x2dc]
00AE3C67  4C 0F AF F8                     imul r15, rax
00AE3C6B  4C 8B A1 C0 04 00 00            mov r12, qword ptr [rcx + 0x4c0]
00AE3C72  80 79 04 00                     cmp byte ptr [rcx + 4], 0
00AE3C76  74 07                           je 0x140ae3c7f
00AE3C78  48 8B B9 C8 04 00 00            mov rdi, qword ptr [rcx + 0x4c8]
00AE3C7F  BA 50 73 51 79                  mov edx, 0x79517350
00AE3C84  E8 57 3C 81 FF                  call 0x1402f78e0
00AE3C89  90                              nop
00AE3C8A  4D 89 26                        mov qword ptr [r14], r12
00AE3C8D  49 89 7E 08                     mov qword ptr [r14 + 8], rdi
00AE3C91  49 89 5E 10                     mov qword ptr [r14 + 0x10], rbx
00AE3C95  4D 89 7E 18                     mov qword ptr [r14 + 0x18], r15
00AE3C99  48 85 F6                        test rsi, rsi
00AE3C9C  74 07                           je 0x140ae3ca5
00AE3C9E  BB 20 00 00 00                  mov ebx, 0x20
00AE3CA3  89 1E                           mov dword ptr [rsi], ebx
00AE3CA5  E9 3A 11 00 00                  jmp 0x140ae4de4
00AE3CAA  E9 8C 15 00 00                  jmp 0x140ae523b
00AE3CAF  4C 8B 05 12 2E 4E 00            mov r8, qword ptr [rip + 0x4e2e12]
00AE3CB6  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE3CBB  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE3CC0  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE3CC5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE3CCA  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE3CD2  45 0F B6 CC                     movzx r9d, r12b
00AE3CD6  BA 40 00 00 00                  mov edx, 0x40
00AE3CDB  48 8B CB                        mov rcx, rbx
00AE3CDE  E8 6D 59 D8 FF                  call 0x140869650
00AE3CE3  85 C0                           test eax, eax
00AE3CE5  0F 88 50 15 00 00               js 0x140ae523b
00AE3CEB  E8 10 89 A1 FF                  call 0x1404fc600
00AE3CF0  8B D8                           mov ebx, eax
00AE3CF2  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE3CF7  BA 50 73 51 79                  mov edx, 0x79517350
00AE3CFC  E8 DF 3B 81 FF                  call 0x1402f78e0
00AE3D01  8B C3                           mov eax, ebx
00AE3D03  E9 33 15 00 00                  jmp 0x140ae523b
00AE3D08  41 83 FF 08                     cmp r15d, 8
00AE3D0C  0F 85 C4 13 00 00               jne 0x140ae50d6
00AE3D12  4C 8B 05 AF 2D 4E 00            mov r8, qword ptr [rip + 0x4e2daf]
00AE3D19  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE3D1E  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE3D23  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE3D28  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE3D2D  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE3D35  45 0F B6 CC                     movzx r9d, r12b
00AE3D39  41 8D 57 38                     lea edx, [r15 + 0x38]
00AE3D3D  48 8B CB                        mov rcx, rbx
00AE3D40  E8 0B 59 D8 FF                  call 0x140869650
00AE3D45  8B D8                           mov ebx, eax
00AE3D47  85 C0                           test eax, eax
00AE3D49  78 B6                           js 0x140ae3d01
00AE3D4B  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE3D50  48 8B B9 60 05 00 00            mov rdi, qword ptr [rcx + 0x560]
00AE3D57  BA 50 73 51 79                  mov edx, 0x79517350
00AE3D5C  E8 7F 3B 81 FF                  call 0x1402f78e0
00AE3D61  90                              nop
00AE3D62  49 89 3E                        mov qword ptr [r14], rdi
00AE3D65  48 85 F6                        test rsi, rsi
00AE3D68  74 03                           je 0x140ae3d6d
00AE3D6A  44 89 2E                        mov dword ptr [rsi], r13d
00AE3D6D  EB 92                           jmp 0x140ae3d01
00AE3D6F  E9 C7 14 00 00                  jmp 0x140ae523b
00AE3D74  41 83 FF 08                     cmp r15d, 8
00AE3D78  0F 85 58 13 00 00               jne 0x140ae50d6
00AE3D7E  4C 8B 05 43 2D 4E 00            mov r8, qword ptr [rip + 0x4e2d43]
00AE3D85  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE3D8A  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE3D8F  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE3D94  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE3D99  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE3DA1  45 0F B6 CC                     movzx r9d, r12b
00AE3DA5  41 8D 57 38                     lea edx, [r15 + 0x38]
00AE3DA9  48 8B CB                        mov rcx, rbx
00AE3DAC  E8 9F 58 D8 FF                  call 0x140869650
00AE3DB1  8B D8                           mov ebx, eax
00AE3DB3  85 C0                           test eax, eax
00AE3DB5  0F 88 46 FF FF FF               js 0x140ae3d01
00AE3DBB  BA 50 73 51 79                  mov edx, 0x79517350
00AE3DC0  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE3DC5  E8 16 3B 81 FF                  call 0x1402f78e0
00AE3DCA  90                              nop
00AE3DCB  49 89 3E                        mov qword ptr [r14], rdi
00AE3DCE  48 85 F6                        test rsi, rsi
00AE3DD1  74 03                           je 0x140ae3dd6
00AE3DD3  44 89 2E                        mov dword ptr [rsi], r13d
00AE3DD6  E9 26 FF FF FF                  jmp 0x140ae3d01
00AE3DDB  E9 5B 14 00 00                  jmp 0x140ae523b
00AE3DE0  41 83 FF 04                     cmp r15d, 4
00AE3DE4  0F 85 EC 12 00 00               jne 0x140ae50d6
00AE3DEA  49 8B 82 20 02 00 00            mov rax, qword ptr [r10 + 0x220]
00AE3DF1  8B 88 80 03 00 00               mov ecx, dword ptr [rax + 0x380]
00AE3DF7  83 F9 01                        cmp ecx, 1
00AE3DFA  40 0F 94 C7                     sete dil
00AE3DFE  41 89 3E                        mov dword ptr [r14], edi
00AE3E01  48 85 F6                        test rsi, rsi
00AE3E04  74 03                           je 0x140ae3e09
00AE3E06  44 89 0E                        mov dword ptr [rsi], r9d
00AE3E09  E9 D6 0F 00 00                  jmp 0x140ae4de4
00AE3E0E  E9 28 14 00 00                  jmp 0x140ae523b
00AE3E13  41 83 FF 04                     cmp r15d, 4
00AE3E17  0F 85 B9 12 00 00               jne 0x140ae50d6
00AE3E1D  4C 8B 05 A4 2C 4E 00            mov r8, qword ptr [rip + 0x4e2ca4]
00AE3E24  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE3E29  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE3E2E  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE3E33  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE3E38  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE3E40  45 0F B6 CC                     movzx r9d, r12b
00AE3E44  BA 00 08 00 00                  mov edx, 0x800
00AE3E49  48 8B CB                        mov rcx, rbx
00AE3E4C  E8 FF 57 D8 FF                  call 0x140869650
00AE3E51  8B F8                           mov edi, eax
00AE3E53  85 C0                           test eax, eax
00AE3E55  0F 88 B0 03 00 00               js 0x140ae420b
00AE3E5B  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE3E60  8B 59 78                        mov ebx, dword ptr [rcx + 0x78]
00AE3E63  C1 EB 03                        shr ebx, 3
00AE3E66  83 E3 01                        and ebx, 1
00AE3E69  BA 50 73 51 79                  mov edx, 0x79517350
00AE3E6E  E8 6D 3A 81 FF                  call 0x1402f78e0
00AE3E73  90                              nop
00AE3E74  41 89 1E                        mov dword ptr [r14], ebx
00AE3E77  48 85 F6                        test rsi, rsi
00AE3E7A  74 03                           je 0x140ae3e7f
00AE3E7C  44 89 3E                        mov dword ptr [rsi], r15d
00AE3E7F  E9 87 03 00 00                  jmp 0x140ae420b
00AE3E84  E9 B2 13 00 00                  jmp 0x140ae523b
00AE3E89  41 83 FF 04                     cmp r15d, 4
00AE3E8D  0F 85 43 12 00 00               jne 0x140ae50d6
00AE3E93  4C 8B 05 2E 2C 4E 00            mov r8, qword ptr [rip + 0x4e2c2e]
00AE3E9A  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE3E9F  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE3EA4  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE3EA9  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE3EAE  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE3EB6  45 0F B6 CC                     movzx r9d, r12b
00AE3EBA  41 8D 57 3C                     lea edx, [r15 + 0x3c]
00AE3EBE  48 8B CB                        mov rcx, rbx
00AE3EC1  E8 8A 57 D8 FF                  call 0x140869650
00AE3EC6  85 C0                           test eax, eax
00AE3EC8  0F 88 6D 13 00 00               js 0x140ae523b
00AE3ECE  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE3ED3  48 8D 81 40 05 00 00            lea rax, [rcx + 0x540]
00AE3EDA  48 39 00                        cmp qword ptr [rax], rax
00AE3EDD  40 0F 95 C7                     setne dil
00AE3EE1  BA 50 73 51 79                  mov edx, 0x79517350
00AE3EE6  E8 F5 39 81 FF                  call 0x1402f78e0
00AE3EEB  90                              nop
00AE3EEC  41 89 3E                        mov dword ptr [r14], edi
00AE3EEF  48 85 F6                        test rsi, rsi
00AE3EF2  74 03                           je 0x140ae3ef7
00AE3EF4  44 89 3E                        mov dword ptr [rsi], r15d
00AE3EF7  E9 E8 0E 00 00                  jmp 0x140ae4de4
00AE3EFC  E9 3A 13 00 00                  jmp 0x140ae523b
00AE3F01  41 83 FF 04                     cmp r15d, 4
00AE3F05  0F 85 CB 11 00 00               jne 0x140ae50d6
00AE3F0B  4C 8B 05 B6 2B 4E 00            mov r8, qword ptr [rip + 0x4e2bb6]
00AE3F12  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE3F17  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE3F1C  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE3F21  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE3F26  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE3F2E  45 0F B6 CC                     movzx r9d, r12b
00AE3F32  41 8D 57 3C                     lea edx, [r15 + 0x3c]
00AE3F36  48 8B CB                        mov rcx, rbx
00AE3F39  E8 12 57 D8 FF                  call 0x140869650
00AE3F3E  85 C0                           test eax, eax
00AE3F40  0F 88 F5 12 00 00               js 0x140ae523b
00AE3F46  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE3F4B  8B 99 A0 05 00 00               mov ebx, dword ptr [rcx + 0x5a0]
00AE3F51  C1 EB 05                        shr ebx, 5
00AE3F54  83 E3 01                        and ebx, 1
00AE3F57  BA 50 73 51 79                  mov edx, 0x79517350
00AE3F5C  E8 7F 39 81 FF                  call 0x1402f78e0
00AE3F61  90                              nop
00AE3F62  41 89 1E                        mov dword ptr [r14], ebx
00AE3F65  48 85 F6                        test rsi, rsi
00AE3F68  74 03                           je 0x140ae3f6d
00AE3F6A  44 89 3E                        mov dword ptr [rsi], r15d
00AE3F6D  E9 72 0E 00 00                  jmp 0x140ae4de4
00AE3F72  E9 C4 12 00 00                  jmp 0x140ae523b
00AE3F77  41 83 FF 04                     cmp r15d, 4
00AE3F7B  0F 85 55 11 00 00               jne 0x140ae50d6
00AE3F81  4C 8B 05 40 2B 4E 00            mov r8, qword ptr [rip + 0x4e2b40]
00AE3F88  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE3F8D  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE3F92  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE3F97  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE3F9C  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE3FA4  45 0F B6 CC                     movzx r9d, r12b
00AE3FA8  BA 00 08 00 00                  mov edx, 0x800
00AE3FAD  48 8B CB                        mov rcx, rbx
00AE3FB0  E8 9B 56 D8 FF                  call 0x140869650
00AE3FB5  85 C0                           test eax, eax
00AE3FB7  0F 88 7E 12 00 00               js 0x140ae523b
00AE3FBD  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE3FC2  8B 98 A0 05 00 00               mov ebx, dword ptr [rax + 0x5a0]
00AE3FC8  83 E3 01                        and ebx, 1
00AE3FCB  BA 50 73 51 79                  mov edx, 0x79517350
00AE3FD0  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE3FD5  E8 06 39 81 FF                  call 0x1402f78e0
00AE3FDA  90                              nop
00AE3FDB  41 89 1E                        mov dword ptr [r14], ebx
00AE3FDE  48 85 F6                        test rsi, rsi
00AE3FE1  74 03                           je 0x140ae3fe6
00AE3FE3  44 89 3E                        mov dword ptr [rsi], r15d
00AE3FE6  E9 F9 0D 00 00                  jmp 0x140ae4de4
00AE3FEB  E9 4B 12 00 00                  jmp 0x140ae523b
00AE3FF0  41 83 FF 01                     cmp r15d, 1
00AE3FF4  0F 85 DC 10 00 00               jne 0x140ae50d6
00AE3FFA  4C 8B 05 C7 2A 4E 00            mov r8, qword ptr [rip + 0x4e2ac7]
00AE4001  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE4006  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE400B  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE4010  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE4015  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE401D  45 0F B6 CC                     movzx r9d, r12b
00AE4021  41 8D 57 3F                     lea edx, [r15 + 0x3f]
00AE4025  48 8B CB                        mov rcx, rbx
00AE4028  E8 23 56 D8 FF                  call 0x140869650
00AE402D  8B D8                           mov ebx, eax
00AE402F  85 C0                           test eax, eax
00AE4031  0F 88 04 12 00 00               js 0x140ae523b
00AE4037  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE403C  8B 81 A0 05 00 00               mov eax, dword ptr [rcx + 0x5a0]
00AE4042  C1 E8 02                        shr eax, 2
00AE4045  41 22 C7                        and al, r15b
00AE4048  41 88 06                        mov byte ptr [r14], al
00AE404B  48 85 F6                        test rsi, rsi
00AE404E  74 05                           je 0x140ae4055
00AE4050  41 8B C7                        mov eax, r15d
00AE4053  89 06                           mov dword ptr [rsi], eax
00AE4055  E9 9D FC FF FF                  jmp 0x140ae3cf7
00AE405A  8B D8                           mov ebx, eax
00AE405C  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE4061  E9 91 FC FF FF                  jmp 0x140ae3cf7
00AE4066  4C 8B 05 5B 2A 4E 00            mov r8, qword ptr [rip + 0x4e2a5b]
00AE406D  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE4072  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE4077  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE407C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE4081  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE4089  45 0F B6 CC                     movzx r9d, r12b
00AE408D  41 8B D5                        mov edx, r13d
00AE4090  48 8B CB                        mov rcx, rbx
00AE4093  E8 B8 55 D8 FF                  call 0x140869650
00AE4098  85 C0                           test eax, eax
00AE409A  0F 88 9B 11 00 00               js 0x140ae523b
00AE40A0  4C 8B CE                        mov r9, rsi
00AE40A3  45 8B C7                        mov r8d, r15d
00AE40A6  49 8B D6                        mov rdx, r14
00AE40A9  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE40AE  E8 35 EC F7 FF                  call 0x140a62ce8
00AE40B3  E9 38 FC FF FF                  jmp 0x140ae3cf0
00AE40B8  41 83 FF 04                     cmp r15d, 4
00AE40BC  0F 85 14 10 00 00               jne 0x140ae50d6
00AE40C2  4C 8B 05 FF 29 4E 00            mov r8, qword ptr [rip + 0x4e29ff]
00AE40C9  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE40CE  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE40D3  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE40D8  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE40DD  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE40E5  45 0F B6 CC                     movzx r9d, r12b
00AE40E9  BA 00 08 00 00                  mov edx, 0x800
00AE40EE  48 8B CB                        mov rcx, rbx
00AE40F1  E8 5A 55 D8 FF                  call 0x140869650
00AE40F6  8B D8                           mov ebx, eax
00AE40F8  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00AE40FC  85 C0                           test eax, eax
00AE40FE  0F 88 37 11 00 00               js 0x140ae523b
00AE4104  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE4109  83 7C 24 54 16                  cmp dword ptr [rsp + 0x54], 0x16
00AE410E  75 0F                           jne 0x140ae411f
00AE4110  41 8B 81 A0 05 00 00            mov eax, dword ptr [r9 + 0x5a0]
00AE4117  C1 E8 09                        shr eax, 9
00AE411A  83 E0 07                        and eax, 7
00AE411D  EB 08                           jmp 0x140ae4127
00AE411F  49 8B C9                        mov rcx, r9
00AE4122  E8 09 F8 85 FF                  call 0x140343930
00AE4127  41 89 06                        mov dword ptr [r14], eax
00AE412A  48 85 F6                        test rsi, rsi
00AE412D  74 06                           je 0x140ae4135
00AE412F  C7 06 04 00 00 00               mov dword ptr [rsi], 4
00AE4135  EB 07                           jmp 0x140ae413e
00AE4137  8B D8                           mov ebx, eax
00AE4139  4C 8B 4C 24 40                  mov r9, qword ptr [rsp + 0x40]
00AE413E  49 8B C9                        mov rcx, r9
00AE4141  BA 50 73 51 79                  mov edx, 0x79517350
00AE4146  E8 95 37 81 FF                  call 0x1402f78e0
00AE414B  8B C3                           mov eax, ebx
00AE414D  E9 E9 10 00 00                  jmp 0x140ae523b
00AE4152  41 83 FF 10                     cmp r15d, 0x10
00AE4156  0F 85 7A 0F 00 00               jne 0x140ae50d6
00AE415C  48 83 FB FE                     cmp rbx, -2
00AE4160  75 07                           jne 0x140ae4169
00AE4162  4C 89 54 24 40                  mov qword ptr [rsp + 0x40], r10
00AE4167  EB 4B                           jmp 0x140ae41b4
00AE4169  4C 8B 05 58 29 4E 00            mov r8, qword ptr [rip + 0x4e2958]
00AE4170  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE4175  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE417A  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE417F  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE4184  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE418C  45 0F B6 CC                     movzx r9d, r12b
00AE4190  BA 00 08 00 00                  mov edx, 0x800
00AE4195  48 8B CB                        mov rcx, rbx
00AE4198  E8 B3 54 D8 FF                  call 0x140869650
00AE419D  8B F8                           mov edi, eax
00AE419F  85 C0                           test eax, eax
00AE41A1  0F 88 94 10 00 00               js 0x140ae523b
00AE41A7  4C 8B 54 24 40                  mov r10, qword ptr [rsp + 0x40]
00AE41AC  4C 89 94 24 80 00 00 00         mov qword ptr [rsp + 0x80], r10
00AE41B4  48 8D 94 24 98 00 00 00         lea rdx, [rsp + 0x98]
00AE41BC  49 8B CA                        mov rcx, r10
00AE41BF  E8 5C AD 89 FF                  call 0x14037ef20
00AE41C4  90                              nop
00AE41C5  49 89 06                        mov qword ptr [r14], rax
00AE41C8  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
00AE41D0  49 89 46 08                     mov qword ptr [r14 + 8], rax
00AE41D4  48 85 F6                        test rsi, rsi
00AE41D7  74 06                           je 0x140ae41df
00AE41D9  C7 06 10 00 00 00               mov dword ptr [rsi], 0x10
00AE41DF  4C 8B AC 24 80 00 00 00         mov r13, qword ptr [rsp + 0x80]
00AE41E7  EB 0F                           jmp 0x140ae41f8
00AE41E9  8B F8                           mov edi, eax
00AE41EB  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
00AE41F0  48 8B 9C 24 90 00 00 00         mov rbx, qword ptr [rsp + 0x90]
00AE41F8  48 83 FB FE                     cmp rbx, -2
00AE41FC  74 0D                           je 0x140ae420b
00AE41FE  BA 50 73 51 79                  mov edx, 0x79517350
00AE4203  49 8B CD                        mov rcx, r13
00AE4206  E8 D5 36 81 FF                  call 0x1402f78e0
00AE420B  8B C7                           mov eax, edi
00AE420D  E9 29 10 00 00                  jmp 0x140ae523b
00AE4212  41 83 FF 04                     cmp r15d, 4
00AE4216  0F 85 BA 0E 00 00               jne 0x140ae50d6
00AE421C  4C 8B 05 A5 28 4E 00            mov r8, qword ptr [rip + 0x4e28a5]
00AE4223  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE4228  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE422D  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE4232  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE4237  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE423F  45 0F B6 CC                     movzx r9d, r12b
00AE4243  BA 00 08 00 00                  mov edx, 0x800
00AE4248  48 8B CB                        mov rcx, rbx
00AE424B  E8 00 54 D8 FF                  call 0x140869650
00AE4250  8B D8                           mov ebx, eax
00AE4252  85 C0                           test eax, eax
00AE4254  0F 88 E1 0F 00 00               js 0x140ae523b
00AE425A  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00AE425F  83 7C 24 54 18                  cmp dword ptr [rsp + 0x54], 0x18
00AE4264  75 0F                           jne 0x140ae4275
00AE4266  41 8B 80 A0 05 00 00            mov eax, dword ptr [r8 + 0x5a0]
00AE426D  C1 E8 0C                        shr eax, 0xc
00AE4270  83 E0 07                        and eax, 7
00AE4273  EB 08                           jmp 0x140ae427d
00AE4275  49 8B C8                        mov rcx, r8
00AE4278  E8 03 FC 8D FF                  call 0x1403c3e80
00AE427D  41 89 06                        mov dword ptr [r14], eax
00AE4280  48 85 F6                        test rsi, rsi
00AE4283  74 06                           je 0x140ae428b
00AE4285  C7 06 04 00 00 00               mov dword ptr [rsi], 4
00AE428B  E9 2C 0E 00 00                  jmp 0x140ae50bc
00AE4290  8B D8                           mov ebx, eax
00AE4292  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00AE4297  E9 20 0E 00 00                  jmp 0x140ae50bc
00AE429C  41 83 FF 10                     cmp r15d, 0x10
00AE42A0  0F 85 30 0E 00 00               jne 0x140ae50d6
00AE42A6  45 84 E4                        test r12b, r12b
00AE42A9  74 3B                           je 0x140ae42e6
00AE42AB  45 8B C7                        mov r8d, r15d
00AE42AE  49 8B D6                        mov rdx, r14
00AE42B1  48 8D 8C 24 C8 00 00 00         lea rcx, [rsp + 0xc8]
00AE42B9  E8 12 87 BD FF                  call 0x1406bc9d0
00AE42BE  8B 94 24 D4 00 00 00            mov edx, dword ptr [rsp + 0xd4]
00AE42C5  45 8D 47 F1                     lea r8d, [r15 - 0xf]
00AE42C9  48 8B 8C 24 C8 00 00 00         mov rcx, qword ptr [rsp + 0xc8]
00AE42D1  E8 EA 4E E0 FF                  call 0x1408e91c0
00AE42D6  90                              nop
00AE42D7  4C 8D B4 24 C8 00 00 00         lea r14, [rsp + 0xc8]
00AE42DF  EB 05                           jmp 0x140ae42e6
00AE42E1  E9 55 0F 00 00                  jmp 0x140ae523b
00AE42E6  4C 8B 05 DB 27 4E 00            mov r8, qword ptr [rip + 0x4e27db]
00AE42ED  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE42F2  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE42F7  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE42FC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE4301  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE4309  45 0F B6 CC                     movzx r9d, r12b
00AE430D  BA 18 00 00 00                  mov edx, 0x18
00AE4312  48 8B CB                        mov rcx, rbx
00AE4315  E8 36 53 D8 FF                  call 0x140869650
00AE431A  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00AE431E  85 C0                           test eax, eax
00AE4320  0F 88 15 0F 00 00               js 0x140ae523b
00AE4326  4C 8B 6C 24 40                  mov r13, qword ptr [rsp + 0x40]
00AE432B  41 F7 45 74 00 04 00 00         test dword ptr [r13 + 0x74], 0x400
00AE4333  74 17                           je 0x140ae434c
00AE4335  BA 50 73 51 79                  mov edx, 0x79517350
00AE433A  49 8B CD                        mov rcx, r13
00AE433D  E8 9E 35 81 FF                  call 0x1402f78e0
00AE4342  B8 08 00 00 C0                  mov eax, 0xc0000008
00AE4347  E9 EF 0E 00 00                  jmp 0x140ae523b
00AE434C  4D 8B AD 20 02 00 00            mov r13, qword ptr [r13 + 0x220]
00AE4353  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AE435C  48 8B 80 B8 00 00 00            mov rax, qword ptr [rax + 0xb8]
00AE4363  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
00AE436B  83 7C 24 54 3A                  cmp dword ptr [rsp + 0x54], 0x3a
00AE4370  75 1E                           jne 0x140ae4390
00AE4372  4C 3B E8                        cmp r13, rax
00AE4375  74 19                           je 0x140ae4390
00AE4377  BA 50 73 51 79                  mov edx, 0x79517350
00AE437C  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE4381  E8 5A 35 81 FF                  call 0x1402f78e0
00AE4386  B8 0D 00 00 C0                  mov eax, 0xc000000d
00AE438B  E9 AB 0E 00 00                  jmp 0x140ae523b
00AE4390  B9 78 18 00 00                  mov ecx, 0x1878
00AE4395  49 83 BD 10 03 00 00 00         cmp qword ptr [r13 + 0x310], 0
00AE439D  74 1A                           je 0x140ae43b9
00AE439F  B9 38 30 00 00                  mov ecx, 0x3038
00AE43A4  BA 78 38 00 00                  mov edx, 0x3878
00AE43A9  B8 64 86 00 00                  mov eax, 0x8664
00AE43AE  66 41 39 85 EC 06 00 00         cmp word ptr [r13 + 0x6ec], ax
00AE43B6  0F 44 CA                        cmove ecx, edx
00AE43B9  4D 8D 7E 0C                     lea r15, [r14 + 0xc]
00AE43BD  4C 89 BC 24 88 00 00 00         mov qword ptr [rsp + 0x88], r15
00AE43C5  41 8B 07                        mov eax, dword ptr [r15]
00AE43C8  85 C0                           test eax, eax
00AE43CA  74 AB                           je 0x140ae4377
00AE43CC  41 8B 56 08                     mov edx, dword ptr [r14 + 8]
00AE43D0  48 3B D1                        cmp rdx, rcx
00AE43D3  73 A2                           jae 0x140ae4377
00AE43D5  48 2B CA                        sub rcx, rdx
00AE43D8  48 3B C1                        cmp rax, rcx
00AE43DB  77 9A                           ja 0x140ae4377
00AE43DD  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AE43E2  48 8D 8B 88 05 00 00            lea rcx, [rbx + 0x588]
00AE43E9  E8 32 22 73 FF                  call 0x140216620
00AE43EE  84 C0                           test al, al
00AE43F0  75 17                           jne 0x140ae4409
00AE43F2  BA 50 73 51 79                  mov edx, 0x79517350
00AE43F7  48 8B CB                        mov rcx, rbx
00AE43FA  E8 E1 34 81 FF                  call 0x1402f78e0
00AE43FF  B8 4B 00 00 C0                  mov eax, 0xc000004b
00AE4404  E9 32 0E 00 00                  jmp 0x140ae523b
00AE4409  4C 8B 84 24 90 00 00 00         mov r8, qword ptr [rsp + 0x90]
00AE4411  41 8B 56 08                     mov edx, dword ptr [r14 + 8]
00AE4415  48 03 93 F0 00 00 00            add rdx, qword ptr [rbx + 0xf0]
00AE441C  4D 3B E8                        cmp r13, r8
00AE441F  0F 85 9E 00 00 00               jne 0x140ae44c3
00AE4425  41 8B 07                        mov eax, dword ptr [r15]
00AE4428  83 7C 24 54 3A                  cmp dword ptr [rsp + 0x54], 0x3a
00AE442D  75 6A                           jne 0x140ae4499
00AE442F  83 F8 01                        cmp eax, 1
00AE4432  75 0F                           jne 0x140ae4443
00AE4434  0F B6 0A                        movzx ecx, byte ptr [rdx]
00AE4437  49 8B 06                        mov rax, qword ptr [r14]
00AE443A  88 08                           mov byte ptr [rax], cl
00AE443C  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AE4441  EB 61                           jmp 0x140ae44a4
00AE4443  83 F8 02                        cmp eax, 2
00AE4446  75 15                           jne 0x140ae445d
00AE4448  F6 C2 01                        test dl, 1
00AE444B  75 10                           jne 0x140ae445d
00AE444D  0F B7 0A                        movzx ecx, word ptr [rdx]
00AE4450  49 8B 06                        mov rax, qword ptr [r14]
00AE4453  66 89 08                        mov word ptr [rax], cx
00AE4456  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AE445B  EB 47                           jmp 0x140ae44a4
00AE445D  83 F8 04                        cmp eax, 4
00AE4460  75 13                           jne 0x140ae4475
00AE4462  F6 C2 03                        test dl, 3
00AE4465  75 0E                           jne 0x140ae4475
00AE4467  8B 0A                           mov ecx, dword ptr [rdx]
00AE4469  49 8B 06                        mov rax, qword ptr [r14]
00AE446C  89 08                           mov dword ptr [rax], ecx
00AE446E  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AE4473  EB 2F                           jmp 0x140ae44a4
00AE4475  83 F8 08                        cmp eax, 8
00AE4478  75 15                           jne 0x140ae448f
00AE447A  F6 C2 07                        test dl, 7
00AE447D  75 10                           jne 0x140ae448f
00AE447F  48 8B 0A                        mov rcx, qword ptr [rdx]
00AE4482  49 8B 06                        mov rax, qword ptr [r14]
00AE4485  48 89 08                        mov qword ptr [rax], rcx
00AE4488  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AE448D  EB 15                           jmp 0x140ae44a4
00AE448F  C7 44 24 48 0D 00 00 C0         mov dword ptr [rsp + 0x48], 0xc000000d
00AE4497  EB 0B                           jmp 0x140ae44a4
00AE4499  4C 8B C0                        mov r8, rax
00AE449C  49 8B 0E                        mov rcx, qword ptr [r14]
00AE449F  E8 9C 23 BE FF                  call 0x1406c6840
00AE44A4  EB 4A                           jmp 0x140ae44f0
00AE44A6  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00AE44AA  33 FF                           xor edi, edi
00AE44AC  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AE44B1  48 8B B4 24 A0 00 00 00         mov rsi, qword ptr [rsp + 0xa0]
00AE44B9  4C 8B BC 24 88 00 00 00         mov r15, qword ptr [rsp + 0x88]
00AE44C1  EB 2D                           jmp 0x140ae44f0
00AE44C3  41 8B 07                        mov eax, dword ptr [r15]
00AE44C6  4D 8B 0E                        mov r9, qword ptr [r14]
00AE44C9  89 7C 24 38                     mov dword ptr [rsp + 0x38], edi
00AE44CD  48 8D 8C 24 E0 00 00 00         lea rcx, [rsp + 0xe0]
00AE44D5  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00AE44DA  44 88 64 24 28                  mov byte ptr [rsp + 0x28], r12b
00AE44DF  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00AE44E4  49 8B CD                        mov rcx, r13
00AE44E7  E8 64 76 ED FF                  call 0x1409bbb50
00AE44EC  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00AE44F0  48 8D 8B 88 05 00 00            lea rcx, [rbx + 0x588]
00AE44F7  E8 84 59 86 FF                  call 0x140349e80
00AE44FC  BA 50 73 51 79                  mov edx, 0x79517350
00AE4501  48 8B CB                        mov rcx, rbx
00AE4504  E8 D7 33 81 FF                  call 0x1402f78e0
00AE4509  83 7C 24 48 00                  cmp dword ptr [rsp + 0x48], 0
00AE450E  7C 14                           jl 0x140ae4524
00AE4510  48 85 F6                        test rsi, rsi
00AE4513  74 05                           je 0x140ae451a
00AE4515  41 8B 07                        mov eax, dword ptr [r15]
00AE4518  89 06                           mov dword ptr [rsi], eax
00AE451A  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
00AE451E  EB 04                           jmp 0x140ae4524
00AE4520  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00AE4524  8B 44 24 48                     mov eax, dword ptr [rsp + 0x48]
00AE4528  E9 0E 0D 00 00                  jmp 0x140ae523b
00AE452D  41 83 FF 01                     cmp r15d, 1
00AE4531  0F 85 9F 0B 00 00               jne 0x140ae50d6
00AE4537  4C 8B 05 8A 25 4E 00            mov r8, qword ptr [rip + 0x4e258a]
00AE453E  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE4543  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE4548  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE454D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE4552  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE455A  45 0F B6 CC                     movzx r9d, r12b
00AE455E  41 8D 57 3F                     lea edx, [r15 + 0x3f]
00AE4562  48 8B CB                        mov rcx, rbx
00AE4565  E8 E6 50 D8 FF                  call 0x140869650
00AE456A  8B F8                           mov edi, eax
00AE456C  85 C0                           test eax, eax
00AE456E  0F 88 C7 0C 00 00               js 0x140ae523b
00AE4574  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE4579  48 83 B9 68 01 00 00 00         cmp qword ptr [rcx + 0x168], 0
00AE4581  0F 95 C0                        setne al
00AE4584  41 88 06                        mov byte ptr [r14], al
00AE4587  41 8B DF                        mov ebx, r15d
00AE458A  EB 14                           jmp 0x140ae45a0
00AE458C  8B F8                           mov edi, eax
00AE458E  BB 01 00 00 00                  mov ebx, 1
00AE4593  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE4598  48 8B B4 24 A0 00 00 00         mov rsi, qword ptr [rsp + 0xa0]
00AE45A0  BA 50 73 51 79                  mov edx, 0x79517350
00AE45A5  E8 36 33 81 FF                  call 0x1402f78e0
00AE45AA  85 FF                           test edi, edi
00AE45AC  0F 88 59 FC FF FF               js 0x140ae420b
00AE45B2  48 85 F6                        test rsi, rsi
00AE45B5  74 02                           je 0x140ae45b9
00AE45B7  89 1E                           mov dword ptr [rsi], ebx
00AE45B9  E9 4D FC FF FF                  jmp 0x140ae420b
00AE45BE  8B F8                           mov edi, eax
00AE45C0  E9 46 FC FF FF                  jmp 0x140ae420b
00AE45C5  41 83 FF 04                     cmp r15d, 4
00AE45C9  0F 85 07 0B 00 00               jne 0x140ae50d6
00AE45CF  4C 8B 05 F2 24 4E 00            mov r8, qword ptr [rip + 0x4e24f2]
00AE45D6  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE45DB  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE45E0  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE45E5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE45EA  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE45F2  45 0F B6 CC                     movzx r9d, r12b
00AE45F6  BA 00 08 00 00                  mov edx, 0x800
00AE45FB  48 8B CB                        mov rcx, rbx
00AE45FE  E8 4D 50 D8 FF                  call 0x140869650
00AE4603  85 C0                           test eax, eax
00AE4605  0F 88 30 0C 00 00               js 0x140ae523b
00AE460B  C7 44 24 58 00 00 40 00         mov dword ptr [rsp + 0x58], 0x400000
00AE4613  4C 8D 44 24 58                  lea r8, [rsp + 0x58]
00AE4618  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
00AE461D  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE4622  E8 D9 8B 7F FF                  call 0x1402dd200
00AE4627  BA 50 73 51 79                  mov edx, 0x79517350
00AE462C  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE4631  E8 AA 32 81 FF                  call 0x1402f78e0
00AE4636  90                              nop
00AE4637  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
00AE463B  41 89 06                        mov dword ptr [r14], eax
00AE463E  48 85 F6                        test rsi, rsi
00AE4641  74 03                           je 0x140ae4646
00AE4643  44 89 3E                        mov dword ptr [rsi], r15d
00AE4646  E9 99 07 00 00                  jmp 0x140ae4de4
00AE464B  E9 EB 0B 00 00                  jmp 0x140ae523b
00AE4650  4C 8B 05 71 24 4E 00            mov r8, qword ptr [rip + 0x4e2471]
00AE4657  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE465C  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE4661  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE4666  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE466B  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE4673  45 0F B6 CC                     movzx r9d, r12b
00AE4677  41 8B D5                        mov edx, r13d
00AE467A  48 8B CB                        mov rcx, rbx
00AE467D  E8 CE 4F D8 FF                  call 0x140869650
00AE4682  85 C0                           test eax, eax
00AE4684  0F 88 B1 0B 00 00               js 0x140ae523b
00AE468A  45 0F B6 CC                     movzx r9d, r12b
00AE468E  45 8B C7                        mov r8d, r15d
00AE4691  49 8B D6                        mov rdx, r14
00AE4694  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE4699  E8 F2 D7 F2 FF                  call 0x140a11e90
00AE469E  8B F8                           mov edi, eax
00AE46A0  BA 50 73 51 79                  mov edx, 0x79517350
00AE46A5  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE46AA  E8 31 32 81 FF                  call 0x1402f78e0
00AE46AF  85 FF                           test edi, edi
00AE46B1  0F 88 54 FB FF FF               js 0x140ae420b
00AE46B7  48 85 F6                        test rsi, rsi
00AE46BA  74 06                           je 0x140ae46c2
00AE46BC  C7 06 CC 02 00 00               mov dword ptr [rsi], 0x2cc
00AE46C2  E9 44 FB FF FF                  jmp 0x140ae420b
00AE46C7  8B F8                           mov edi, eax
00AE46C9  E9 3D FB FF FF                  jmp 0x140ae420b
00AE46CE  41 83 FF 01                     cmp r15d, 1
00AE46D2  0F 82 FE 09 00 00               jb 0x140ae50d6
00AE46D8  4C 8B 05 E9 23 4E 00            mov r8, qword ptr [rip + 0x4e23e9]
00AE46DF  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE46E4  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE46E9  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE46EE  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE46F3  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE46FB  45 0F B6 CC                     movzx r9d, r12b
00AE46FF  BA 40 00 00 00                  mov edx, 0x40
00AE4704  48 8B CB                        mov rcx, rbx
00AE4707  E8 44 4F D8 FF                  call 0x140869650
00AE470C  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00AE4710  85 C0                           test eax, eax
00AE4712  0F 88 23 0B 00 00               js 0x140ae523b
00AE4718  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE471D  48 8B 48 68                     mov rcx, qword ptr [rax + 0x68]
00AE4721  48 85 C9                        test rcx, rcx
00AE4724  0F 95 C0                        setne al
00AE4727  41 88 06                        mov byte ptr [r14], al
00AE472A  48 85 F6                        test rsi, rsi
00AE472D  74 07                           je 0x140ae4736
00AE472F  B8 01 00 00 00                  mov eax, 1
00AE4734  89 06                           mov dword ptr [rsi], eax
00AE4736  8B 5C 24 48                     mov ebx, dword ptr [rsp + 0x48]
00AE473A  E9 B3 F5 FF FF                  jmp 0x140ae3cf2
00AE473F  8B D8                           mov ebx, eax
00AE4741  E9 AC F5 FF FF                  jmp 0x140ae3cf2
00AE4746  41 83 FF 04                     cmp r15d, 4
00AE474A  0F 85 86 09 00 00               jne 0x140ae50d6
00AE4750  4C 8B 05 71 23 4E 00            mov r8, qword ptr [rip + 0x4e2371]
00AE4757  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE475C  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE4761  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE4766  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE476B  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE4773  45 0F B6 CC                     movzx r9d, r12b
00AE4777  BA 00 08 00 00                  mov edx, 0x800
00AE477C  48 8B CB                        mov rcx, rbx
00AE477F  E8 CC 4E D8 FF                  call 0x140869650
00AE4784  8B F8                           mov edi, eax
00AE4786  85 C0                           test eax, eax
00AE4788  0F 88 AD 0A 00 00               js 0x140ae523b
00AE478E  E8 E9 ED AD FF                  call 0x1405c357c
00AE4793  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AE4798  85 C0                           test eax, eax
00AE479A  74 0C                           je 0x140ae47a8
00AE479C  48 8B CB                        mov rcx, rbx
00AE479F  E8 54 47 AD FF                  call 0x1405b8ef8
00AE47A4  8B C8                           mov ecx, eax
00AE47A6  EB 12                           jmp 0x140ae47ba
00AE47A8  8B 4B 78                        mov ecx, dword ptr [rbx + 0x78]
00AE47AB  C1 E9 0E                        shr ecx, 0xe
00AE47AE  83 E1 01                        and ecx, 1
00AE47B1  0F BE 83 84 02 00 00            movsx eax, byte ptr [rbx + 0x284]
00AE47B8  03 C8                           add ecx, eax
00AE47BA  41 89 0E                        mov dword ptr [r14], ecx
00AE47BD  48 85 F6                        test rsi, rsi
00AE47C0  74 06                           je 0x140ae47c8
00AE47C2  C7 06 04 00 00 00               mov dword ptr [rsi], 4
00AE47C8  EB 07                           jmp 0x140ae47d1
00AE47CA  8B F8                           mov edi, eax
00AE47CC  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AE47D1  BA 50 73 51 79                  mov edx, 0x79517350
00AE47D6  48 8B CB                        mov rcx, rbx
00AE47D9  E8 02 31 81 FF                  call 0x1402f78e0
00AE47DE  8B C7                           mov eax, edi
00AE47E0  E9 56 0A 00 00                  jmp 0x140ae523b
00AE47E5  41 83 FF 04                     cmp r15d, 4
00AE47E9  0F 85 E7 08 00 00               jne 0x140ae50d6
00AE47EF  4C 8B 05 D2 22 4E 00            mov r8, qword ptr [rip + 0x4e22d2]
00AE47F6  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE47FB  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE4800  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE4805  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE480A  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE4812  45 0F B6 CC                     movzx r9d, r12b
00AE4816  BA 00 08 00 00                  mov edx, 0x800
00AE481B  48 8B CB                        mov rcx, rbx
00AE481E  E8 2D 4E D8 FF                  call 0x140869650
00AE4823  8B F8                           mov edi, eax
00AE4825  85 C0                           test eax, eax
00AE4827  0F 88 DE F9 FF FF               js 0x140ae420b
00AE482D  41 8D 57 FD                     lea edx, [r15 - 3]
00AE4831  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AE4836  48 8B CB                        mov rcx, rbx
00AE4839  E8 32 42 9A FF                  call 0x140488a70
00AE483E  90                              nop
00AE483F  41 89 06                        mov dword ptr [r14], eax
00AE4842  48 85 F6                        test rsi, rsi
00AE4845  74 03                           je 0x140ae484a
00AE4847  44 89 3E                        mov dword ptr [rsi], r15d
00AE484A  EB 85                           jmp 0x140ae47d1
00AE484C  8B F8                           mov edi, eax
00AE484E  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AE4853  E9 79 FF FF FF                  jmp 0x140ae47d1
00AE4858  41 83 FF 10                     cmp r15d, 0x10
00AE485C  0F 85 74 08 00 00               jne 0x140ae50d6
00AE4862  48 83 FB FE                     cmp rbx, -2
00AE4866  0F 85 1A FB FF FF               jne 0x140ae4386
00AE486C  4C 8D 84 24 40 01 00 00         lea r8, [rsp + 0x140]
00AE4874  49 8B D2                        mov rdx, r10
00AE4877  41 8B C9                        mov ecx, r9d
00AE487A  E8 21 4F 96 FF                  call 0x1404497a0
00AE487F  85 C0                           test eax, eax
00AE4881  0F 88 B4 09 00 00               js 0x140ae523b
00AE4887  0F 10 84 24 40 01 00 00         movups xmm0, xmmword ptr [rsp + 0x140]
00AE488F  41 0F 11 06                     movups xmmword ptr [r14], xmm0
00AE4893  48 85 F6                        test rsi, rsi
00AE4896  74 03                           je 0x140ae489b
00AE4898  44 89 3E                        mov dword ptr [rsi], r15d
00AE489B  EB 00                           jmp 0x140ae489d
00AE489D  E9 99 09 00 00                  jmp 0x140ae523b
00AE48A2  41 F6 C7 07                     test r15b, 7
00AE48A6  0F 85 2A 08 00 00               jne 0x140ae50d6
00AE48AC  41 81 FF 00 01 00 00            cmp r15d, 0x100
00AE48B3  0F 87 1D 08 00 00               ja 0x140ae50d6
00AE48B9  4C 8B 05 08 22 4E 00            mov r8, qword ptr [rip + 0x4e2208]
00AE48C0  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE48C5  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE48CA  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE48CF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE48D4  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE48DC  45 0F B6 CC                     movzx r9d, r12b
00AE48E0  BA 00 08 00 00                  mov edx, 0x800
00AE48E5  48 8B CB                        mov rcx, rbx
00AE48E8  E8 63 4D D8 FF                  call 0x140869650
00AE48ED  44 8B E0                        mov r12d, eax
00AE48F0  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00AE48F4  85 C0                           test eax, eax
00AE48F6  0F 88 ED 03 00 00               js 0x140ae4ce9
00AE48FC  48 8D 94 24 00 03 00 00         lea rdx, [rsp + 0x300]
00AE4904  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE4909  E8 8E 36 8E FF                  call 0x1403c7f9c
00AE490E  8D 1C C5 00 00 00 00            lea ebx, [rax*8]
00AE4915  BA 50 73 51 79                  mov edx, 0x79517350
00AE491A  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE491F  E8 BC 2F 81 FF                  call 0x1402f78e0
00AE4924  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
00AE4928  48 85 F6                        test rsi, rsi
00AE492B  74 02                           je 0x140ae492f
00AE492D  89 1E                           mov dword ptr [rsi], ebx
00AE492F  41 3B DF                        cmp ebx, r15d
00AE4932  41 0F 43 DF                     cmovae ebx, r15d
00AE4936  89 5C 24 60                     mov dword ptr [rsp + 0x60], ebx
00AE493A  44 8B C3                        mov r8d, ebx
00AE493D  48 8D 94 24 00 03 00 00         lea rdx, [rsp + 0x300]
00AE4945  49 8B CE                        mov rcx, r14
00AE4948  E8 F3 1E BE FF                  call 0x1406c6840
00AE494D  E9 97 03 00 00                  jmp 0x140ae4ce9
00AE4952  44 8B E0                        mov r12d, eax
00AE4955  E9 8F 03 00 00                  jmp 0x140ae4ce9
00AE495A  41 83 FF 50                     cmp r15d, 0x50
00AE495E  0F 85 72 07 00 00               jne 0x140ae50d6
00AE4964  4C 8B 05 5D 21 4E 00            mov r8, qword ptr [rip + 0x4e215d]
00AE496B  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE4970  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE4975  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE497A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE497F  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE4987  45 0F B6 CC                     movzx r9d, r12b
00AE498B  BA 00 08 00 00                  mov edx, 0x800
00AE4990  48 8B CB                        mov rcx, rbx
00AE4993  E8 B8 4C D8 FF                  call 0x140869650
00AE4998  44 8B F8                        mov r15d, eax
00AE499B  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00AE499F  85 C0                           test eax, eax
00AE49A1  0F 88 94 08 00 00               js 0x140ae523b
00AE49A7  48 8D 94 24 F0 00 00 00         lea rdx, [rsp + 0xf0]
00AE49AF  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AE49B4  48 8B CB                        mov rcx, rbx
00AE49B7  E8 74 A4 82 FF                  call 0x14030ee30
00AE49BC  F7 43 74 00 04 00 00            test dword ptr [rbx + 0x74], 0x400
00AE49C3  75 4B                           jne 0x140ae4a10
00AE49C5  8B 83 A8 05 00 00               mov eax, dword ptr [rbx + 0x5a8]
00AE49CB  A8 08                           test al, 8
00AE49CD  75 32                           jne 0x140ae4a01
00AE49CF  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE49D4  48 8B 90 E0 04 00 00            mov rdx, qword ptr [rax + 0x4e0]
00AE49DB  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
00AE49E0  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE49E5  8B 88 A8 05 00 00               mov ecx, dword ptr [rax + 0x5a8]
00AE49EB  F6 C1 08                        test cl, 8
00AE49EE  48 8B C7                        mov rax, rdi
00AE49F1  48 0F 44 C2                     cmove rax, rdx
00AE49F5  44 8B 7C 24 48                  mov r15d, dword ptr [rsp + 0x48]
00AE49FA  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AE49FF  EB 16                           jmp 0x140ae4a17
00AE4A01  48 8B C7                        mov rax, rdi
00AE4A04  44 8B 7C 24 48                  mov r15d, dword ptr [rsp + 0x48]
00AE4A09  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AE4A0E  EB 07                           jmp 0x140ae4a17
00AE4A10  48 8B 83 60 05 00 00            mov rax, qword ptr [rbx + 0x560]
00AE4A17  48 B9 FF FF FE FF FF 7F 00 00   movabs rcx, 0x7ffffffeffff
00AE4A21  48 3B C1                        cmp rax, rcx
00AE4A24  48 0F 46 F8                     cmovbe rdi, rax
00AE4A28  0F B6 84 24 F8 00 00 00         movzx eax, byte ptr [rsp + 0xf8]
00AE4A30  41 89 46 44                     mov dword ptr [r14 + 0x44], eax
00AE4A34  0F B6 84 24 F9 00 00 00         movzx eax, byte ptr [rsp + 0xf9]
00AE4A3C  41 89 46 48                     mov dword ptr [r14 + 0x48], eax
00AE4A40  0F BE 84 24 FB 00 00 00         movsx eax, byte ptr [rsp + 0xfb]
00AE4A48  41 89 46 3C                     mov dword ptr [r14 + 0x3c], eax
00AE4A4C  0F BE 84 24 FA 00 00 00         movsx eax, byte ptr [rsp + 0xfa]
00AE4A54  41 89 46 38                     mov dword ptr [r14 + 0x38], eax
00AE4A58  8B 84 24 F0 00 00 00            mov eax, dword ptr [rsp + 0xf0]
00AE4A5F  41 89 46 18                     mov dword ptr [r14 + 0x18], eax
00AE4A63  8B 0D 37 20 4E 00               mov ecx, dword ptr [rip + 0x4e2037]
00AE4A69  8B 83 8C 02 00 00               mov eax, dword ptr [rbx + 0x28c]
00AE4A6F  48 0F AF C1                     imul rax, rcx
00AE4A73  49 89 06                        mov qword ptr [r14], rax
00AE4A76  8B 83 DC 02 00 00               mov eax, dword ptr [rbx + 0x2dc]
00AE4A7C  48 0F AF C1                     imul rax, rcx
00AE4A80  49 89 46 08                     mov qword ptr [r14 + 8], rax
00AE4A84  48 8B 83 C0 04 00 00            mov rax, qword ptr [rbx + 0x4c0]
00AE4A8B  49 89 46 10                     mov qword ptr [r14 + 0x10], rax
00AE4A8F  8B 83 54 01 00 00               mov eax, dword ptr [rbx + 0x154]
00AE4A95  41 89 46 40                     mov dword ptr [r14 + 0x40], eax
00AE4A99  0F 10 83 08 05 00 00            movups xmm0, xmmword ptr [rbx + 0x508]
00AE4AA0  41 0F 11 46 28                  movups xmmword ptr [r14 + 0x28], xmm0
00AE4AA5  49 89 7E 20                     mov qword ptr [r14 + 0x20], rdi
00AE4AA9  48 85 F6                        test rsi, rsi
00AE4AAC  74 06                           je 0x140ae4ab4
00AE4AAE  C7 06 50 00 00 00               mov dword ptr [rsi], 0x50
00AE4AB4  E9 37 F1 FF FF                  jmp 0x140ae3bf0
00AE4AB9  44 8B F8                        mov r15d, eax
00AE4ABC  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AE4AC1  E9 2A F1 FF FF                  jmp 0x140ae3bf0
00AE4AC6  41 83 FF 10                     cmp r15d, 0x10
00AE4ACA  0F 85 06 06 00 00               jne 0x140ae50d6
00AE4AD0  4C 8B 05 F1 1F 4E 00            mov r8, qword ptr [rip + 0x4e1ff1]
00AE4AD7  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE4ADC  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE4AE1  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE4AE6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE4AEB  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE4AF3  45 0F B6 CC                     movzx r9d, r12b
00AE4AF7  BA 00 08 00 00                  mov edx, 0x800
00AE4AFC  48 8B CB                        mov rcx, rbx
00AE4AFF  E8 4C 4B D8 FF                  call 0x140869650
00AE4B04  8B D8                           mov ebx, eax
00AE4B06  85 C0                           test eax, eax
00AE4B08  0F 88 2D 07 00 00               js 0x140ae523b
00AE4B0E  48 8D 94 24 A8 00 00 00         lea rdx, [rsp + 0xa8]
00AE4B16  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00AE4B1B  48 8B CF                        mov rcx, rdi
00AE4B1E  E8 15 27 8E FF                  call 0x1403c7238
00AE4B23  90                              nop
00AE4B24  0F 10 84 24 A8 00 00 00         movups xmm0, xmmword ptr [rsp + 0xa8]
00AE4B2C  41 0F 11 06                     movups xmmword ptr [r14], xmm0
00AE4B30  48 85 F6                        test rsi, rsi
00AE4B33  74 03                           je 0x140ae4b38
00AE4B35  44 89 3E                        mov dword ptr [rsi], r15d
00AE4B38  EB 07                           jmp 0x140ae4b41
00AE4B3A  8B D8                           mov ebx, eax
00AE4B3C  48 8B 7C 24 40                  mov rdi, qword ptr [rsp + 0x40]
00AE4B41  48 8B CF                        mov rcx, rdi
00AE4B44  BA 50 73 51 79                  mov edx, 0x79517350
00AE4B49  E8 92 2D 81 FF                  call 0x1402f78e0
00AE4B4E  8B C3                           mov eax, ebx
00AE4B50  E9 E6 06 00 00                  jmp 0x140ae523b
00AE4B55  41 83 FF 04                     cmp r15d, 4
00AE4B59  0F 85 77 05 00 00               jne 0x140ae50d6
00AE4B5F  4C 8B 05 62 1F 4E 00            mov r8, qword ptr [rip + 0x4e1f62]
00AE4B66  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE4B6B  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE4B70  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE4B75  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE4B7A  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE4B82  45 0F B6 CC                     movzx r9d, r12b
00AE4B86  BA 00 08 00 00                  mov edx, 0x800
00AE4B8B  48 8B CB                        mov rcx, rbx
00AE4B8E  E8 BD 4A D8 FF                  call 0x140869650
00AE4B93  8B D8                           mov ebx, eax
00AE4B95  85 C0                           test eax, eax
00AE4B97  0F 88 9E 06 00 00               js 0x140ae523b
00AE4B9D  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE4BA2  8B 81 A0 05 00 00               mov eax, dword ptr [rcx + 0x5a0]
00AE4BA8  C1 E8 12                        shr eax, 0x12
00AE4BAB  83 E0 01                        and eax, 1
00AE4BAE  41 89 06                        mov dword ptr [r14], eax
00AE4BB1  48 85 F6                        test rsi, rsi
00AE4BB4  74 03                           je 0x140ae4bb9
00AE4BB6  44 89 3E                        mov dword ptr [rsi], r15d
00AE4BB9  E9 39 F1 FF FF                  jmp 0x140ae3cf7
00AE4BBE  8B D8                           mov ebx, eax
00AE4BC0  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE4BC5  E9 2D F1 FF FF                  jmp 0x140ae3cf7
00AE4BCA  C6 44 24 4D 00                  mov byte ptr [rsp + 0x4d], 0
00AE4BCF  C6 44 24 4C 00                  mov byte ptr [rsp + 0x4c], 0
00AE4BD4  4C 8B 05 ED 1E 4E 00            mov r8, qword ptr [rip + 0x4e1eed]
00AE4BDB  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE4BE0  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE4BE5  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE4BEA  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE4BEF  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE4BF7  45 0F B6 CC                     movzx r9d, r12b
00AE4BFB  BA 00 08 00 00                  mov edx, 0x800
00AE4C00  48 8B CB                        mov rcx, rbx
00AE4C03  E8 48 4A D8 FF                  call 0x140869650
00AE4C08  44 8B E0                        mov r12d, eax
00AE4C0B  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00AE4C0F  4C 8B AC 24 80 00 00 00         mov r13, qword ptr [rsp + 0x80]
00AE4C17  85 C0                           test eax, eax
00AE4C19  0F 88 9F 00 00 00               js 0x140ae4cbe
00AE4C1F  C6 44 24 4D 01                  mov byte ptr [rsp + 0x4d], 1
00AE4C24  49 8B D5                        mov rdx, r13
00AE4C27  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AE4C2C  48 8B CB                        mov rcx, rbx
00AE4C2F  E8 EC FA 8D FF                  call 0x1403c4720
00AE4C34  C6 44 24 4C 01                  mov byte ptr [rsp + 0x4c], 1
00AE4C39  48 8B 83 A0 06 00 00            mov rax, qword ptr [rbx + 0x6a0]
00AE4C40  48 85 C0                        test rax, rax
00AE4C43  75 09                           jne 0x140ae4c4e
00AE4C45  48 8D 15 84 7E 01 00            lea rdx, [rip + 0x17e84]
00AE4C4C  EB 07                           jmp 0x140ae4c55
00AE4C4E  48 8B 50 08                     mov rdx, qword ptr [rax + 8]
00AE4C52  0F B7 38                        movzx edi, word ptr [rax]
00AE4C55  66 89 7C 24 5C                  mov word ptr [rsp + 0x5c], di
00AE4C5A  48 89 94 24 E8 00 00 00         mov qword ptr [rsp + 0xe8], rdx
00AE4C62  0F B7 C7                        movzx eax, di
00AE4C65  83 C0 10                        add eax, 0x10
00AE4C68  89 44 24 54                     mov dword ptr [rsp + 0x54], eax
00AE4C6C  89 84 24 D8 00 00 00            mov dword ptr [rsp + 0xd8], eax
00AE4C73  41 3B C7                        cmp eax, r15d
00AE4C76  76 0D                           jbe 0x140ae4c85
00AE4C78  41 BC 23 00 00 C0               mov r12d, 0xc0000023
00AE4C7E  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
00AE4C83  EB 21                           jmp 0x140ae4ca6
00AE4C85  49 8D 5E 10                     lea rbx, [r14 + 0x10]
00AE4C89  44 0F B7 C7                     movzx r8d, di
00AE4C8D  48 8B CB                        mov rcx, rbx
00AE4C90  E8 AB 1B BE FF                  call 0x1406c6840
00AE4C95  66 41 89 3E                     mov word ptr [r14], di
00AE4C99  66 41 89 7E 02                  mov word ptr [r14 + 2], di
00AE4C9E  49 89 5E 08                     mov qword ptr [r14 + 8], rbx
00AE4CA2  8B 44 24 54                     mov eax, dword ptr [rsp + 0x54]
00AE4CA6  48 85 F6                        test rsi, rsi
00AE4CA9  74 02                           je 0x140ae4cad
00AE4CAB  89 06                           mov dword ptr [rsi], eax
00AE4CAD  EB 0F                           jmp 0x140ae4cbe
00AE4CAF  44 8B E0                        mov r12d, eax
00AE4CB2  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00AE4CB6  4C 8B AC 24 88 00 00 00         mov r13, qword ptr [rsp + 0x88]
00AE4CBE  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00AE4CC3  80 7C 24 4C 00                  cmp byte ptr [rsp + 0x4c], 0
00AE4CC8  74 0B                           je 0x140ae4cd5
00AE4CCA  49 8B D5                        mov rdx, r13
00AE4CCD  48 8B CB                        mov rcx, rbx
00AE4CD0  E8 6B E1 8D FF                  call 0x1403c2e40
00AE4CD5  80 7C 24 4D 00                  cmp byte ptr [rsp + 0x4d], 0
00AE4CDA  74 0D                           je 0x140ae4ce9
00AE4CDC  BA 50 73 51 79                  mov edx, 0x79517350
00AE4CE1  48 8B CB                        mov rcx, rbx
00AE4CE4  E8 F7 2B 81 FF                  call 0x1402f78e0
00AE4CE9  41 8B C4                        mov eax, r12d
00AE4CEC  E9 4A 05 00 00                  jmp 0x140ae523b
00AE4CF1  41 83 FF 04                     cmp r15d, 4
00AE4CF5  0F 85 DB 03 00 00               jne 0x140ae50d6
00AE4CFB  4C 8B 05 C6 1D 4E 00            mov r8, qword ptr [rip + 0x4e1dc6]
00AE4D02  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE4D07  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE4D0C  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE4D11  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE4D16  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE4D1E  45 0F B6 CC                     movzx r9d, r12b
00AE4D22  BA 00 08 00 00                  mov edx, 0x800
00AE4D27  48 8B CB                        mov rcx, rbx
00AE4D2A  E8 21 49 D8 FF                  call 0x140869650
00AE4D2F  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00AE4D33  85 C0                           test eax, eax
00AE4D35  0F 88 00 05 00 00               js 0x140ae523b
00AE4D3B  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE4D40  8B 88 A0 05 00 00               mov ecx, dword ptr [rax + 0x5a0]
00AE4D46  C1 E9 13                        shr ecx, 0x13
00AE4D49  83 E1 01                        and ecx, 1
00AE4D4C  41 89 0E                        mov dword ptr [r14], ecx
00AE4D4F  48 85 F6                        test rsi, rsi
00AE4D52  74 03                           je 0x140ae4d57
00AE4D54  44 89 3E                        mov dword ptr [rsi], r15d
00AE4D57  8B 5C 24 48                     mov ebx, dword ptr [rsp + 0x48]
00AE4D5B  E9 92 EF FF FF                  jmp 0x140ae3cf2
00AE4D60  8B D8                           mov ebx, eax
00AE4D62  E9 8B EF FF FF                  jmp 0x140ae3cf2
00AE4D67  89 7C 24 7C                     mov dword ptr [rsp + 0x7c], edi
00AE4D6B  41 83 FF 10                     cmp r15d, 0x10
00AE4D6F  0F 85 61 03 00 00               jne 0x140ae50d6
00AE4D75  48 83 FB FE                     cmp rbx, -2
00AE4D79  0F 85 07 F6 FF FF               jne 0x140ae4386
00AE4D7F  0F 11 84 24 B8 00 00 00         movups xmmword ptr [rsp + 0xb8], xmm0
00AE4D87  48 8D 54 24 7C                  lea rdx, [rsp + 0x7c]
00AE4D8C  49 8B CA                        mov rcx, r10
00AE4D8F  E8 CC 47 95 FF                  call 0x140439560
00AE4D94  48 8B C8                        mov rcx, rax
00AE4D97  48 8D 94 24 B8 00 00 00         lea rdx, [rsp + 0xb8]
00AE4D9F  48 85 C0                        test rax, rax
00AE4DA2  75 17                           jne 0x140ae4dbb
00AE4DA4  48 8B 8C 24 80 00 00 00         mov rcx, qword ptr [rsp + 0x80]
00AE4DAC  E8 BF 6E 96 FF                  call 0x14044bc70
00AE4DB1  83 8C 24 C0 00 00 00 01         or dword ptr [rsp + 0xc0], 1
00AE4DB9  EB 12                           jmp 0x140ae4dcd
00AE4DBB  E8 B0 6E 96 FF                  call 0x14044bc70
00AE4DC0  83 7C 24 7C 00                  cmp dword ptr [rsp + 0x7c], 0
00AE4DC5  74 06                           je 0x140ae4dcd
00AE4DC7  E8 84 45 81 FF                  call 0x1402f9350
00AE4DCC  90                              nop
00AE4DCD  0F 10 84 24 B8 00 00 00         movups xmm0, xmmword ptr [rsp + 0xb8]
00AE4DD5  41 0F 11 06                     movups xmmword ptr [r14], xmm0
00AE4DD9  48 85 F6                        test rsi, rsi
00AE4DDC  74 06                           je 0x140ae4de4
00AE4DDE  C7 06 10 00 00 00               mov dword ptr [rsi], 0x10
00AE4DE4  33 C0                           xor eax, eax
00AE4DE6  E9 50 04 00 00                  jmp 0x140ae523b
00AE4DEB  E9 4B 04 00 00                  jmp 0x140ae523b
00AE4DF0  41 83 FF 04                     cmp r15d, 4
00AE4DF4  0F 85 DC 02 00 00               jne 0x140ae50d6
00AE4DFA  4C 8B 05 C7 1C 4E 00            mov r8, qword ptr [rip + 0x4e1cc7]
00AE4E01  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE4E06  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE4E0B  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE4E10  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE4E15  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE4E1D  45 0F B6 CC                     movzx r9d, r12b
00AE4E21  BA 00 08 00 00                  mov edx, 0x800
00AE4E26  48 8B CB                        mov rcx, rbx
00AE4E29  E8 22 48 D8 FF                  call 0x140869650
00AE4E2E  8B D8                           mov ebx, eax
00AE4E30  85 C0                           test eax, eax
00AE4E32  0F 88 03 04 00 00               js 0x140ae523b
00AE4E38  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE4E3D  48 83 B9 70 06 00 00 00         cmp qword ptr [rcx + 0x670], 0
00AE4E45  0F 45 3D 24 17 42 00            cmovne edi, dword ptr [rip + 0x421724]
00AE4E4C  41 89 3E                        mov dword ptr [r14], edi
00AE4E4F  48 85 F6                        test rsi, rsi
00AE4E52  74 03                           je 0x140ae4e57
00AE4E54  44 89 3E                        mov dword ptr [rsi], r15d
00AE4E57  E9 9B EE FF FF                  jmp 0x140ae3cf7
00AE4E5C  8B D8                           mov ebx, eax
00AE4E5E  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE4E63  E9 8F EE FF FF                  jmp 0x140ae3cf7
00AE4E68  41 83 FF 04                     cmp r15d, 4
00AE4E6C  73 15                           jae 0x140ae4e83
00AE4E6E  48 85 F6                        test rsi, rsi
00AE4E71  74 06                           je 0x140ae4e79
00AE4E73  C7 06 0C 00 00 00               mov dword ptr [rsi], 0xc
00AE4E79  B8 04 00 00 C0                  mov eax, 0xc0000004
00AE4E7E  E9 B8 03 00 00                  jmp 0x140ae523b
00AE4E83  F2 41 0F 10 06                  movsd xmm0, qword ptr [r14]
00AE4E88  F2 0F 11 44 24 68               movsd qword ptr [rsp + 0x68], xmm0
00AE4E8E  41 8B 46 08                     mov eax, dword ptr [r14 + 8]
00AE4E92  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
00AE4E96  83 7C 24 68 01                  cmp dword ptr [rsp + 0x68], 1
00AE4E9B  0F 85 23 01 00 00               jne 0x140ae4fc4
00AE4EA1  48 85 F6                        test rsi, rsi
00AE4EA4  74 06                           je 0x140ae4eac
00AE4EA6  C7 06 0C 00 00 00               mov dword ptr [rsi], 0xc
00AE4EAC  41 83 FF 0C                     cmp r15d, 0xc
00AE4EB0  74 0A                           je 0x140ae4ebc
00AE4EB2  B8 04 00 00 C0                  mov eax, 0xc0000004
00AE4EB7  E9 7F 03 00 00                  jmp 0x140ae523b
00AE4EBC  4C 8B 05 05 1C 4E 00            mov r8, qword ptr [rip + 0x4e1c05]
00AE4EC3  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE4EC8  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE4ECD  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE4ED2  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE4ED7  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE4EDF  45 0F B6 CC                     movzx r9d, r12b
00AE4EE3  BA 40 00 00 00                  mov edx, 0x40
00AE4EE8  48 8B CB                        mov rcx, rbx
00AE4EEB  E8 60 47 D8 FF                  call 0x140869650
00AE4EF0  85 C0                           test eax, eax
00AE4EF2  0F 88 43 03 00 00               js 0x140ae523b
00AE4EF8  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00AE4EFD  49 8B C8                        mov rcx, r8
00AE4F00  E8 53 84 A1 FF                  call 0x1404fd358
00AE4F05  85 C0                           test eax, eax
00AE4F07  74 34                           je 0x140ae4f3d
00AE4F09  83 E8 01                        sub eax, 1
00AE4F0C  74 27                           je 0x140ae4f35
00AE4F0E  83 E8 01                        sub eax, 1
00AE4F11  74 1A                           je 0x140ae4f2d
00AE4F13  83 E8 01                        sub eax, 1
00AE4F16  74 0D                           je 0x140ae4f25
00AE4F18  83 F8 01                        cmp eax, 1
00AE4F1B  74 23                           je 0x140ae4f40
00AE4F1D  41 BD 0A 00 00 00               mov r13d, 0xa
00AE4F23  EB 1B                           jmp 0x140ae4f40
00AE4F25  41 BD 03 00 00 00               mov r13d, 3
00AE4F2B  EB 13                           jmp 0x140ae4f40
00AE4F2D  41 BD 02 00 00 00               mov r13d, 2
00AE4F33  EB 0B                           jmp 0x140ae4f40
00AE4F35  41 BD 01 00 00 00               mov r13d, 1
00AE4F3B  EB 03                           jmp 0x140ae4f40
00AE4F3D  44 8B EF                        mov r13d, edi
00AE4F40  45 85 ED                        test r13d, r13d
00AE4F43  74 3B                           je 0x140ae4f80
00AE4F45  41 83 ED 01                     sub r13d, 1
00AE4F49  74 35                           je 0x140ae4f80
00AE4F4B  41 83 ED 01                     sub r13d, 1
00AE4F4F  74 2F                           je 0x140ae4f80
00AE4F51  41 83 ED 01                     sub r13d, 1
00AE4F55  74 19                           je 0x140ae4f70
00AE4F57  41 83 FD 05                     cmp r13d, 5
00AE4F5B  75 2F                           jne 0x140ae4f8c
00AE4F5D  C7 44 24 6C 01 00 00 00         mov dword ptr [rsp + 0x6c], 1
00AE4F65  B8 01 00 00 00                  mov eax, 1
00AE4F6A  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00AE4F6E  EB 20                           jmp 0x140ae4f90
00AE4F70  C7 44 24 6C 01 00 00 00         mov dword ptr [rsp + 0x6c], 1
00AE4F78  8B C7                           mov eax, edi
00AE4F7A  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00AE4F7E  EB 10                           jmp 0x140ae4f90
00AE4F80  89 7C 24 6C                     mov dword ptr [rsp + 0x6c], edi
00AE4F84  8B C7                           mov eax, edi
00AE4F86  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
00AE4F8A  EB 04                           jmp 0x140ae4f90
00AE4F8C  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
00AE4F90  F2 0F 10 44 24 68               movsd xmm0, qword ptr [rsp + 0x68]
00AE4F96  F2 41 0F 11 06                  movsd qword ptr [r14], xmm0
00AE4F9B  41 89 46 08                     mov dword ptr [r14 + 8], eax
00AE4F9F  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
00AE4FA3  EB 0B                           jmp 0x140ae4fb0
00AE4FA5  8B F8                           mov edi, eax
00AE4FA7  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00AE4FAB  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00AE4FB0  BA 50 73 51 79                  mov edx, 0x79517350
00AE4FB5  49 8B C8                        mov rcx, r8
00AE4FB8  E8 23 29 81 FF                  call 0x1402f78e0
00AE4FBD  8B C7                           mov eax, edi
00AE4FBF  E9 77 02 00 00                  jmp 0x140ae523b
00AE4FC4  B8 0D 00 00 C0                  mov eax, 0xc000000d
00AE4FC9  E9 6D 02 00 00                  jmp 0x140ae523b
00AE4FCE  E9 68 02 00 00                  jmp 0x140ae523b
00AE4FD3  41 83 FF 08                     cmp r15d, 8
00AE4FD7  0F 85 F9 00 00 00               jne 0x140ae50d6
00AE4FDD  4C 8B 05 E4 1A 4E 00            mov r8, qword ptr [rip + 0x4e1ae4]
00AE4FE4  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE4FE9  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE4FEE  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE4FF3  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE4FF8  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE5000  45 0F B6 CC                     movzx r9d, r12b
00AE5004  41 8D 57 38                     lea edx, [r15 + 0x38]
00AE5008  48 8B CB                        mov rcx, rbx
00AE500B  E8 40 46 D8 FF                  call 0x140869650
00AE5010  8B D8                           mov ebx, eax
00AE5012  85 C0                           test eax, eax
00AE5014  0F 88 94 00 00 00               js 0x140ae50ae
00AE501A  48 8B CF                        mov rcx, rdi
00AE501D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AE5026  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00AE502B  4C 3B C0                        cmp r8, rax
00AE502E  74 07                           je 0x140ae5037
00AE5030  BB BB 00 00 C0                  mov ebx, 0xc00000bb
00AE5035  EB 5D                           jmp 0x140ae5094
00AE5037  4D 8B 88 E0 06 00 00            mov r9, qword ptr [r8 + 0x6e0]
00AE503E  4D 85 C9                        test r9, r9
00AE5041  75 04                           jne 0x140ae5047
00AE5043  8B DF                           mov ebx, edi
00AE5045  EB 4D                           jmp 0x140ae5094
00AE5047  49 8B 90 68 04 00 00            mov rdx, qword ptr [r8 + 0x468]
00AE504E  48 85 D2                        test rdx, rdx
00AE5051  74 3C                           je 0x140ae508f
00AE5053  41 8B 88 64 04 00 00            mov ecx, dword ptr [r8 + 0x464]
00AE505A  49 2B D1                        sub rdx, r9
00AE505D  48 B8 67 66 66 66 66 66 66 66   movabs rax, 0x6666666666666667
00AE5067  48 F7 EA                        imul rdx
00AE506A  48 C1 FA 05                     sar rdx, 5
00AE506E  48 8B C2                        mov rax, rdx
00AE5071  48 C1 E8 3F                     shr rax, 0x3f
00AE5075  48 03 D0                        add rdx, rax
00AE5078  C1 E2 06                        shl edx, 6
00AE507B  C1 E9 06                        shr ecx, 6
00AE507E  03 CA                           add ecx, edx
00AE5080  48 C1 E1 06                     shl rcx, 6
00AE5084  49 03 89 B8 00 00 00            add rcx, qword ptr [r9 + 0xb8]
00AE508B  8B DF                           mov ebx, edi
00AE508D  EB 05                           jmp 0x140ae5094
00AE508F  BB 25 02 00 C0                  mov ebx, 0xc0000225
00AE5094  85 DB                           test ebx, ebx
00AE5096  78 1B                           js 0x140ae50b3
00AE5098  49 89 0E                        mov qword ptr [r14], rcx
00AE509B  48 85 F6                        test rsi, rsi
00AE509E  74 03                           je 0x140ae50a3
00AE50A0  44 89 2E                        mov dword ptr [rsi], r13d
00AE50A3  EB 0E                           jmp 0x140ae50b3
00AE50A5  8B D8                           mov ebx, eax
00AE50A7  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00AE50AC  EB 05                           jmp 0x140ae50b3
00AE50AE  4C 8B 44 24 40                  mov r8, qword ptr [rsp + 0x40]
00AE50B3  4D 85 C0                        test r8, r8
00AE50B6  0F 84 45 EC FF FF               je 0x140ae3d01
00AE50BC  49 8B C8                        mov rcx, r8
00AE50BF  BA 50 73 51 79                  mov edx, 0x79517350
00AE50C4  E8 17 28 81 FF                  call 0x1402f78e0
00AE50C9  8B C3                           mov eax, ebx
00AE50CB  E9 6B 01 00 00                  jmp 0x140ae523b
00AE50D0  41 83 FF 08                     cmp r15d, 8
00AE50D4  74 0A                           je 0x140ae50e0
00AE50D6  B8 04 00 00 C0                  mov eax, 0xc0000004
00AE50DB  E9 5B 01 00 00                  jmp 0x140ae523b
00AE50E0  4C 8B 05 E1 19 4E 00            mov r8, qword ptr [rip + 0x4e19e1]
00AE50E7  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00AE50EC  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
00AE50F1  48 8D 44 24 40                  lea rax, [rsp + 0x40]
00AE50F6  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE50FB  C7 44 24 20 50 73 51 79         mov dword ptr [rsp + 0x20], 0x79517350
00AE5103  45 0F B6 CC                     movzx r9d, r12b
00AE5107  BA 00 08 00 00                  mov edx, 0x800
00AE510C  48 8B CB                        mov rcx, rbx
00AE510F  E8 3C 45 D8 FF                  call 0x140869650
00AE5114  8B D8                           mov ebx, eax
00AE5116  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
00AE511A  85 C0                           test eax, eax
00AE511C  0F 88 F8 00 00 00               js 0x140ae521a
00AE5122  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00AE512B  48 3B 44 24 40                  cmp rax, qword ptr [rsp + 0x40]
00AE5130  74 0A                           je 0x140ae513c
00AE5132  BB 22 00 00 C0                  mov ebx, 0xc0000022
00AE5137  E9 DE 00 00 00                  jmp 0x140ae521a
00AE513C  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
00AE5141  4C 8B A0 20 02 00 00            mov r12, qword ptr [rax + 0x220]
00AE5148  4D 8B BC 24 00 08 00 00         mov r15, qword ptr [r12 + 0x800]
00AE5150  BB 20 00 00 00                  mov ebx, 0x20
00AE5155  4D 85 FF                        test r15, r15
00AE5158  75 3B                           jne 0x140ae5195
00AE515A  41 B8 50 73 54 69               mov r8d, 0x69547350
00AE5160  8B D3                           mov edx, ebx
00AE5162  B9 00 01 00 00                  mov ecx, 0x100
00AE5167  E8 84 CF 09 00                  call 0x140b820f0
00AE516C  48 8B C8                        mov rcx, rax
00AE516F  48 85 C0                        test rax, rax
00AE5172  0F 84 9D 00 00 00               je 0x140ae5215
00AE5178  33 C0                           xor eax, eax
00AE517A  F0 49 0F B1 8C 24 00 08 00 00   lock cmpxchg qword ptr [r12 + 0x800], rcx
00AE5184  4C 8B F8                        mov r15, rax
00AE5187  74 09                           je 0x140ae5192
00AE5189  33 D2                           xor edx, edx
00AE518B  E8 E0 D6 09 00                  call 0x140b82870
00AE5190  EB 03                           jmp 0x140ae5195
00AE5192  4C 8B F9                        mov r15, rcx
00AE5195  4C 8B 64 24 40                  mov r12, qword ptr [rsp + 0x40]
00AE519A  49 8B 8C 24 80 07 00 00         mov rcx, qword ptr [r12 + 0x780]
00AE51A2  48 85 C9                        test rcx, rcx
00AE51A5  75 51                           jne 0x140ae51f8
00AE51A7  49 8B CF                        mov rcx, r15
00AE51AA  E8 C1 53 BD FF                  call 0x1406ba570
00AE51AF  48 8B C8                        mov rcx, rax
00AE51B2  48 85 C0                        test rax, rax
00AE51B5  74 06                           je 0x140ae51bd
00AE51B7  F0 FF 40 14                     lock inc dword ptr [rax + 0x14]
00AE51BB  EB 33                           jmp 0x140ae51f0
00AE51BD  41 B8 50 73 54 69               mov r8d, 0x69547350
00AE51C3  48 8B D3                        mov rdx, rbx
00AE51C6  B9 00 01 00 00                  mov ecx, 0x100
00AE51CB  E8 20 CF 09 00                  call 0x140b820f0
00AE51D0  48 8B C8                        mov rcx, rax
00AE51D3  48 85 C0                        test rax, rax
00AE51D6  74 3D                           je 0x140ae5215
00AE51D8  B8 01 00 00 00                  mov eax, 1
00AE51DD  89 41 14                        mov dword ptr [rcx + 0x14], eax
00AE51E0  F0 41 0F C1 47 10               lock xadd dword ptr [r15 + 0x10], eax
00AE51E6  FF C0                           inc eax
00AE51E8  89 41 10                        mov dword ptr [rcx + 0x10], eax
00AE51EB  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
00AE51F0  49 89 8C 24 80 07 00 00         mov qword ptr [r12 + 0x780], rcx
00AE51F8  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
00AE51FB  8B 51 14                        mov edx, dword ptr [rcx + 0x14]
00AE51FE  8B DF                           mov ebx, edi
00AE5200  41 89 06                        mov dword ptr [r14], eax
00AE5203  41 89 56 04                     mov dword ptr [r14 + 4], edx
00AE5207  48 85 F6                        test rsi, rsi
00AE520A  74 03                           je 0x140ae520f
00AE520C  44 89 2E                        mov dword ptr [rsi], r13d
00AE520F  EB 09                           jmp 0x140ae521a
00AE5211  8B D8                           mov ebx, eax
00AE5213  EB 05                           jmp 0x140ae521a
00AE5215  BB 9A 00 00 C0                  mov ebx, 0xc000009a
00AE521A  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
00AE521F  48 85 C9                        test rcx, rcx
00AE5222  0F 84 D9 EA FF FF               je 0x140ae3d01
00AE5228  BA 50 73 51 79                  mov edx, 0x79517350
00AE522D  E8 AE 26 81 FF                  call 0x1402f78e0
00AE5232  8B C3                           mov eax, ebx
00AE5234  EB 05                           jmp 0x140ae523b
00AE5236  B8 03 00 00 C0                  mov eax, 0xc0000003
00AE523B  48 8B 8C 24 00 04 00 00         mov rcx, qword ptr [rsp + 0x400]
00AE5243  48 33 CC                        xor rcx, rsp
00AE5246  E8 F5 73 BC FF                  call 0x1406ac640
00AE524B  0F 28 B4 24 10 04 00 00         movaps xmm6, xmmword ptr [rsp + 0x410]
00AE5253  48 81 C4 20 04 00 00            add rsp, 0x420
00AE525A  41 5F                           pop r15
00AE525C  41 5E                           pop r14
00AE525E  41 5D                           pop r13
00AE5260  41 5C                           pop r12
00AE5262  5F                              pop rdi
00AE5263  5E                              pop rsi
00AE5264  5B                              pop rbx
00AE5265  C3                              ret
00AE5266  CC                              int3
00AE5267  E8 64 4D DB FF                  call 0x140899fd0
00AE526C  90                              nop
00AE526D  0F 1F 00                        nop dword ptr [rax]
00AE5270  27                              .byte 0x27
00AE5271  39 AE 00 05 3C AE               cmp dword ptr [rsi - 0x51c3fb00], ebp
00AE5277  00 36                           add byte ptr [rsi], dh
00AE5279  52                              push rdx
00AE527A  AE                              scasb al, byte ptr [rdi]
00AE527B  00 36                           add byte ptr [rsi], dh
00AE527D  52                              push rdx
00AE527E  AE                              scasb al, byte ptr [rdi]
00AE527F  00 36                           add byte ptr [rsi], dh
00AE5281  52                              push rdx
00AE5282  AE                              scasb al, byte ptr [rdi]
00AE5283  00 36                           add byte ptr [rsi], dh
00AE5285  52                              push rdx
00AE5286  AE                              scasb al, byte ptr [rdi]
00AE5287  00 AF 3C AE 00 36               add byte ptr [rdi + 0x3600ae3c], ch
00AE528D  52                              push rdx
00AE528E  AE                              scasb al, byte ptr [rdi]
00AE528F  00 36                           add byte ptr [rsi], dh
00AE5291  52                              push rdx
00AE5292  AE                              scasb al, byte ptr [rdi]
00AE5293  00 08                           add byte ptr [rax], cl
00AE5295  3D AE 00 36 52                  cmp eax, 0x523600ae
00AE529A  AE                              scasb al, byte ptr [rdi]
00AE529B  00 74 3D AE                     add byte ptr [rbp + rdi - 0x52], dh
00AE529F  00 E0                           add al, ah
00AE52A1  3D AE 00 36 52                  cmp eax, 0x523600ae
00AE52A6  AE                              scasb al, byte ptr [rdi]
00AE52A7  00 13                           add byte ptr [rbx], dl
00AE52A9  3E AE                           scasb al, byte ptr [rdi]
00AE52AB  00 36                           add byte ptr [rsi], dh
00AE52AD  52                              push rdx
00AE52AE  AE                              scasb al, byte ptr [rdi]
00AE52AF  00 89 3E AE 00 F0               add byte ptr [rcx - 0xfff51c2], cl
00AE52B5  3F                              .byte 0x3f
00AE52B6  AE                              scasb al, byte ptr [rdi]
00AE52B7  00 01                           add byte ptr [rcx], al
00AE52B9  3F                              .byte 0x3f
00AE52BA  AE                              scasb al, byte ptr [rdi]
00AE52BB  00 36                           add byte ptr [rsi], dh
00AE52BD  52                              push rdx
00AE52BE  AE                              scasb al, byte ptr [rdi]
00AE52BF  00 77 3F                        add byte ptr [rdi + 0x3f], dh
00AE52C2  AE                              scasb al, byte ptr [rdi]
00AE52C3  00 66 40                        add byte ptr [rsi + 0x40], ah
00AE52C6  AE                              scasb al, byte ptr [rdi]
00AE52C7  00 B8 40 AE 00 52               add byte ptr [rax + 0x5200ae40], bh
00AE52CD  41 AE                           scasb al, byte ptr [rdi]
00AE52CF  00 12                           add byte ptr [rdx], dl
00AE52D1  42 AE                           scasb al, byte ptr [rdi]
00AE52D3  00 B5 3A AE 00 9C               add byte ptr [rbp - 0x63ff51c6], dh
00AE52D9  42 AE                           scasb al, byte ptr [rdi]
00AE52DB  00 36                           add byte ptr [rsi], dh
00AE52DD  52                              push rdx
00AE52DE  AE                              scasb al, byte ptr [rdi]
00AE52DF  00 36                           add byte ptr [rsi], dh
00AE52E1  52                              push rdx
00AE52E2  AE                              scasb al, byte ptr [rdi]
00AE52E3  00 50 46                        add byte ptr [rax + 0x46], dl
00AE52E6  AE                              scasb al, byte ptr [rdi]
00AE52E7  00 27                           add byte ptr [rdi], ah
00AE52E9  3B AE 00 36 52 AE               cmp ebp, dword ptr [rsi - 0x51adca00]
00AE52EF  00 2D 45 AE 00 C5               add byte ptr [rip - 0x3aff51bb], ch
00AE52F5  45 AE                           scasb al, byte ptr [rdi]
00AE52F7  00 CE                           add dh, cl
00AE52F9  46 AE                           scasb al, byte ptr [rdi]
00AE52FB  00 46 47                        add byte ptr [rsi + 0x47], al
00AE52FE  AE                              scasb al, byte ptr [rdi]
00AE52FF  00 E5                           add ch, ah
00AE5301  47 AE                           scasb al, byte ptr [rdi]
00AE5303  00 58 48                        add byte ptr [rax + 0x48], bl
00AE5306  AE                              scasb al, byte ptr [rdi]
00AE5307  00 CA                           add dl, cl
00AE5309  4B AE                           scasb al, byte ptr [rdi]
00AE530B  00 A2 48 AE 00 5A               add byte ptr [rdx + 0x5a00ae48], ah
00AE5311  49 AE                           scasb al, byte ptr [rdi]
00AE5313  00 C6                           add dh, al
00AE5315  4A AE                           scasb al, byte ptr [rdi]
00AE5317  00 55 4B                        add byte ptr [rbp + 0x4b], dl
00AE531A  AE                              scasb al, byte ptr [rdi]
00AE531B  00 F1                           add cl, dh
00AE531D  4C AE                           scasb al, byte ptr [rdi]
00AE531F  00 67 4D                        add byte ptr [rdi + 0x4d], ah
00AE5322  AE                              scasb al, byte ptr [rdi]
00AE5323  00 F0                           add al, dh
00AE5325  4D AE                           scasb al, byte ptr [rdi]
00AE5327  00 36                           add byte ptr [rsi], dh
00AE5329  52                              push rdx
00AE532A  AE                              scasb al, byte ptr [rdi]
00AE532B  00 36                           add byte ptr [rsi], dh
00AE532D  52                              push rdx
00AE532E  AE                              scasb al, byte ptr [rdi]
00AE532F  00 36                           add byte ptr [rsi], dh
00AE5331  52                              push rdx
00AE5332  AE                              scasb al, byte ptr [rdi]
00AE5333  00 68 4E                        add byte ptr [rax + 0x4e], ch
00AE5336  AE                              scasb al, byte ptr [rdi]
00AE5337  00 36                           add byte ptr [rsi], dh
00AE5339  52                              push rdx
00AE533A  AE                              scasb al, byte ptr [rdi]
00AE533B  00 36                           add byte ptr [rsi], dh
00AE533D  52                              push rdx
00AE533E  AE                              scasb al, byte ptr [rdi]
00AE533F  00 36                           add byte ptr [rsi], dh
00AE5341  52                              push rdx
00AE5342  AE                              scasb al, byte ptr [rdi]
00AE5343  00 36                           add byte ptr [rsi], dh
00AE5345  52                              push rdx
00AE5346  AE                              scasb al, byte ptr [rdi]
00AE5347  00 B8 40 AE 00 12               add byte ptr [rax + 0x1200ae40], bh
00AE534D  42 AE                           scasb al, byte ptr [rdi]
00AE534F  00 36                           add byte ptr [rsi], dh
00AE5351  52                              push rdx
00AE5352  AE                              scasb al, byte ptr [rdi]
00AE5353  00 D3                           add bl, dl
00AE5355  4F AE                           scasb al, byte ptr [rdi]
00AE5357  00 9C 42 AE 00 D0 50            add byte ptr [rdx + rax*2 + 0x50d000ae], bl
00AE535E  AE                              scasb al, byte ptr [rdi]
00AE535F  00                              .byte 0x00
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtQueryInformationThread(__int64 a1, int a2, __int64 a3, int a4, __int64 a5)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m2B8;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned __int64 v_stack_m2F0;
    unsigned __int64 v_stack_m300;
    unsigned int v_stack_m308;
    unsigned __int64 v_stack_m318;
    unsigned int v_stack_m31C;
    unsigned int v_stack_m320;
    unsigned __int64 v_stack_m328;
    unsigned __int64 v_stack_m338;
    unsigned __int64 v_stack_m340;
    unsigned int v_stack_m344;
    unsigned int v_stack_m348;
    unsigned __int64 v_stack_m358;
    unsigned __int8 v_stack_m35D;
    unsigned __int8 v_stack_m35E;
    unsigned __int8 v_stack_m35F;
    unsigned __int8 v_stack_m360;
    unsigned __int64 v_stack_m368;
    unsigned __int64 v_stack_m370;
    unsigned __int64 v_stack_m378;
    unsigned int v_stack_m380;
    unsigned int v_stack_m384;
    unsigned __int64 v_stack_m390;
    unsigned int v_stack_m398;
    unsigned __int64 v_stack_m3A0;
    unsigned __int16 v_stack_m3A8;
    unsigned __int64 v_stack_m3B0;
    unsigned __int64 v_stack_m3B8;
    unsigned __int64 v_stack_m3C0;
    unsigned __int64 v_stack_m3C8;
    unsigned __int64 v_stack_m3D0;
    unsigned __int64 v_stack_m3D8;
    unsigned int v_stack_m3DC;
    unsigned int v_stack_m3E0;
    unsigned int v_stack_m3E8;
    unsigned int v_stack_m3EC;
    unsigned __int64 v_stack_m3F0;
    unsigned int v_stack_m3F8;
    unsigned __int16 v_stack_m3FC;
    unsigned int v_stack_m400;
    unsigned int v_stack_m404;
    unsigned __int8 v_stack_m40B;
    unsigned __int8 v_stack_m40C;
    unsigned int v_stack_m410;
    unsigned __int64 v_stack_m418;
    unsigned __int64 v_stack_m420;
    unsigned __int64 v_stack_m428;
    unsigned __int64 v_stack_m430;
    unsigned int v_stack_m438;
    unsigned int v_stack_m458;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;

    v_rsp = (v_rsp) - (0x420ULL);
    v_stack_m48 = v_xmm6;
    result = (*(unsigned __int64 *)(v_rip + 3305406)) ^ (v_rsp);
    v_stack_m58 = result;
    v_stack_m404 = a2;
    v_stack_m3C8 = a1;
    v_stack_m3B8 = a5;
    result = 0;
    v_stack_m344 = 0;
    v_rdi = 0;
    v_stack_m378 = 0;
    v_stack_m318 = v_xmm0;
    v_stack_m308 = 0;
    v_stack_m3B0 = v_xmm0;
    v_stack_m390 = v_xmm1;
    v_stack_m3F0 = 0;
    v_stack_m3E8 = 0;
    v_stack_m300 = v_xmm0;
    v_stack_m2F0 = v_xmm0;
    v_stack_m418 = 0;
    a2 = 0;
    result = memset(v_stack_m260, a2, 256, a4);
    v_stack_m3C0 = 0;
    v_stack_m368 = v_xmm0;
    v_stack_m358 = v_xmm0;
    v_stack_m3D8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m3D0 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_00AE38E8;
    if (((unsigned int)((unsigned int)(a2))) == 38) goto loc_00AE388C;
    if (((unsigned int)((unsigned int)(a2))) == 49) goto loc_00AE3887;
    result = 1;
    if (((unsigned int)((unsigned int)(a4))) >= ((unsigned int)(v_rdi + 4))) { result = (unsigned int)(v_rdi + 4); }
    goto loc_00AE3895;
loc_00AE3887:
    goto loc_00AE3895;
loc_00AE388C:
loc_00AE3895:
    v_stack_m3E0 = 8;
    if ((unsigned int)((unsigned int)(a4)) == 0) goto loc_00AE38C7;
    if (((a3) & (8 - 1)) != 0) goto loc_00AE5267;
    if ((a3 + (unsigned int)(a4) * 1) > (8 - 1)) goto loc_00AE38C2;
    if ((a3 + (unsigned int)(a4) * 1) >= a3) goto loc_00AE38D1;
loc_00AE38C2:
    goto loc_00AE38D1;
loc_00AE38C7:
loc_00AE38D1:
    result = *(unsigned __int8 *)(8 - 1);
    if (a5 != 0) {
        a1 = 8 - 1;
        if (a5 < (8 - 1)) { a1 = a5; }
        result = *(unsigned int *)(a1);
        *(unsigned int *)(a1) = (unsigned int)(result);
    }
    goto loc_00AE38F2;
loc_00AE38E8:
loc_00AE38F2:
    v_stack_m344 = 0;
    v_stack_m338 = v_xmm0;
    if (((unsigned int)((int)(v_stack_m404))) > 59) goto loc_00AE5236;
    a1 = ((unsigned int)(*(unsigned int *)(v_rip - 11417879 + (int)(v_stack_m404) * 4 + 11424368))) + (v_rip - 11417879);
loc_00AE5236:
loc_00AE523B:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, v_rip - 11417879, 256, 4);
    v_rsp = (v_rsp) + (0x420ULL);
    return result;
loc_00AE5267:
    result = ExRaiseDatatypeMisalignment(a1, v_rip - 11417879, 256, 4);
    result = (unsigned __int8)((result) + ((unsigned __int8)(result)));
    a2 = (unsigned __int8)((v_rip - 11417879) + ((unsigned __int8)(a1)));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(result)));
    a2 = (unsigned __int8)((a2) + ((unsigned __int8)(a1)));
    a2 = (unsigned __int8)((a2) + ((unsigned __int8)(result)));
    a1 = (unsigned __int8)((a1) + ((unsigned __int8)(a2)));
    result = (unsigned __int8)((result) + ((unsigned __int8)(a2)));
    v_rbx = (unsigned __int8)((a1) + ((unsigned __int8)(a2)));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtQueryInformationThread(void *Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, void *Arg5)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg5 = (uint8_t *)Arg5;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m158;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m278;
    uint64_t v_stack_m288;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m2B8;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint64_t v_stack_m2F0;
    uint64_t v_stack_m300;
    uint32_t v_stack_m308;
    uint64_t v_stack_m318;
    uint32_t v_stack_m31C;
    uint32_t v_stack_m320;
    uint64_t v_stack_m328;
    uint64_t v_stack_m338;
    uint64_t v_stack_m340;
    uint32_t v_stack_m344;
    uint32_t v_stack_m348;
    uint64_t v_stack_m358;
    uint8_t v_stack_m35D;
    uint8_t v_stack_m35E;
    uint8_t v_stack_m35F;
    uint8_t v_stack_m360;
    uint64_t v_stack_m368;
    uint64_t v_stack_m370;
    uint64_t v_stack_m378;
    uint32_t v_stack_m380;
    uint32_t v_stack_m384;
    uint64_t v_stack_m390;
    uint32_t v_stack_m398;
    uint64_t v_stack_m3A0;
    uint16_t v_stack_m3A8;
    uint64_t v_stack_m3B0;
    uint64_t v_stack_m3B8;
    uint64_t v_stack_m3C0;
    uint64_t v_stack_m3C8;
    uint64_t v_stack_m3D0;
    uint64_t v_stack_m3D8;
    uint32_t v_stack_m3DC;
    uint32_t v_stack_m3E0;
    uint32_t v_stack_m3E8;
    uint32_t v_stack_m3EC;
    uint64_t v_stack_m3F0;
    uint32_t v_stack_m3F8;
    uint16_t v_stack_m3FC;
    uint32_t v_stack_m400;
    uint32_t v_stack_m404;
    uint8_t v_stack_m40B;
    uint8_t v_stack_m40C;
    uint32_t v_stack_m410;
    uint64_t v_stack_m418;
    uint64_t v_stack_m420;
    uint64_t v_stack_m428;
    uint64_t v_stack_m430;
    uint32_t v_stack_m438;
    uint32_t v_stack_m458;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;

    local_rsp = (local_rsp) - (0x420ULL);
    v_stack_m48 = v_xmm6;
    result = (*(uint64_t *)(v_rip + 0x326FBE)) ^ (local_rsp);
    v_stack_m58 = result;
    v_stack_m404 = Arg2;
    v_stack_m3C8 = Arg1;
    v_stack_m3B8 = Arg5;
    result = 0;
    v_stack_m344 = 0;
    local_rdi = 0;
    v_stack_m378 = 0;
    v_stack_m318 = v_xmm0;
    v_stack_m308 = 0;
    v_stack_m3B0 = v_xmm0;
    v_stack_m390 = v_xmm1;
    v_stack_m3F0 = 0;
    v_stack_m3E8 = 0;
    v_stack_m300 = v_xmm0;
    v_stack_m2F0 = v_xmm0;
    v_stack_m418 = 0;
    Arg2 = 0;
    result = memset(v_stack_m260, Arg2, 256, Arg4);
    v_stack_m3C0 = 0;
    v_stack_m368 = v_xmm0;
    v_stack_m358 = v_xmm0;
    v_stack_m3D8 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m3D0 = *(uint64_t *)(gs_base + (0 + 0x188));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_00AE38E8;
    if (((uint32_t)((uint32_t)(Arg2))) == 38) goto loc_00AE388C;
    if (((uint32_t)((uint32_t)(Arg2))) == 49) goto loc_00AE3887;
    result = 1;
    if (((uint32_t)((uint32_t)(Arg4))) >= ((uint32_t)(local_rdi + 4))) { result = (uint32_t)(local_rdi + 4); }
    goto loc_00AE3895;
loc_00AE3887:
    goto loc_00AE3895;
loc_00AE388C:
loc_00AE3895:
    v_stack_m3E0 = 8;
    if ((uint32_t)((uint32_t)(Arg4)) == 0) goto loc_00AE38C7;
    if (((Arg3) & (8 - 1)) != 0) goto loc_00AE5267;
    if ((Arg3 + (uint32_t)(Arg4) * 1) > (8 - 1)) goto loc_00AE38C2;
    if ((Arg3 + (uint32_t)(Arg4) * 1) >= Arg3) goto loc_00AE38D1;
loc_00AE38C2:
    goto loc_00AE38D1;
loc_00AE38C7:
loc_00AE38D1:
    result = *(uint8_t *)(8 - 0x1);
    if (Arg5 != NULL) {
        Arg1 = 8 - 1;
        if (Arg5 < (8 - 1)) { Arg1 = Arg5; }
        result = *(uint32_t *)(arg1);
        *(uint32_t *)(arg1) = (uint32_t)(result);
    }
    goto loc_00AE38F2;
loc_00AE38E8:
loc_00AE38F2:
    v_stack_m344 = 0;
    v_stack_m338 = v_xmm0;
    if (((uint32_t)((int32_t)(v_stack_m404))) > 59) goto loc_00AE5236;
    Arg1 = ((uint32_t)(*(uint32_t *)(v_rip - 0xAE3917 + (int32_t)(v_stack_m404) * 4 + 0xAE5270))) + (v_rip - 11417879);
loc_00AE5236:
loc_00AE523B:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_rip - 11417879, 256, 4);
    local_rsp = (local_rsp) + (0x420ULL);
    return result;
loc_00AE5267:
    result = ExRaiseDatatypeMisalignment(Arg1, v_rip - 11417879, 256, 4);
    result = (uint8_t)((result) + ((uint8_t)(result)));
    Arg2 = (uint8_t)((v_rip - 11417879) + ((uint8_t)(Arg1)));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(result)));
    Arg2 = (uint8_t)((Arg2) + ((uint8_t)(Arg1)));
    Arg2 = (uint8_t)((Arg2) + ((uint8_t)(result)));
    Arg1 = (uint8_t)((Arg1) + ((uint8_t)(Arg2)));
    result = (uint8_t)((result) + ((uint8_t)(Arg2)));
    local_rbx = (uint8_t)((Arg1) + ((uint8_t)(Arg2)));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R/W` |
| `Arg5` | `- 0x51C3FB00` | `32` | `R` |
| `Arg5` | `- 0x51ADCA00` | `32` | `R` |
| `Arg5` | `+ 0x0` | `8` | `R/W` |
| `Arg5` | `+ 0x40` | `8` | `R/W` |
| `Arg5` | `+ 0x47` | `8` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AE3760&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
