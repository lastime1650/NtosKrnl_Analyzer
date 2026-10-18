# ObDuplicateObject

- RVA: `0x008C4FA0`–`0x008C5F5C` (길이 `4,028` bytes)
- VA: `0x00000001408C4FA0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00083B64`
- 디코드: `967`개 명령, `4,028/4,028` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **83**; 고유 호출 대상: **39**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x008C500C` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008C5020` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x008C50FB` → [ExpLookupHandleTableEntry](../86/ExpLookupHandleTableEntry_function_00869DB0.md) (function, `0x00869DB0`)
- `0x008C5131` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (function, `0x00430C90`)
- `0x008C514E` → [ExpGetHandleExtraInfo](../86/ExpGetHandleExtraInfo_function_0086B454.md) (function, `0x0086B454`)
- `0x008C51AD` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (function, `0x002A3FE0`)
- `0x008C51B7` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008C51CA` → [ObpTraceObjectReferenceIfActive](../../text/21/ObpTraceObjectReferenceIfActive_function_00210780.md) (function, `0x00210780`)
- `0x008C5324` → [ObpIncrementHandleCountEx](../86/ObpIncrementHandleCountEx_function_0086DA10.md) (function, `0x0086DA10`)
- `0x008C533B` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x008C535A` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (function, `0x00216800`)
- `0x008C5363` → [NtClose](../86/NtClose_function_00868870.md) (function, `0x00868870`)
- `0x008C536E` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x008C5474` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008C548D` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x008C54D9` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008C5536` → [ExpUpdateDebugInfo](../86/ExpUpdateDebugInfo_function_0086B174.md) (function, `0x0086B174`)
- `0x008C555C` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008C55B0` → [SeDeleteAccessState](SeDeleteAccessState_function_008C5F70.md) (function, `0x008C5F70`)
- `0x008C5679` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008C5687` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008C56A7` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x008C5706` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x008C572D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x008C574A` → [ExpBlockOnLockedHandleEntry](../86/ExpBlockOnLockedHandleEntry_function_00868838.md) (function, `0x00868838`)
- `0x008C5757` → [ExfAcquireRundownProtection](../../text/34/ExfAcquireRundownProtection_function_0034C050.md) (function, `0x0034C050`)
- `0x008C5771` → [ExfAcquireRundownProtection](../../text/34/ExfAcquireRundownProtection_function_0034C050.md) (function, `0x0034C050`)
- `0x008C5794` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (function, `0x00216800`)
- `0x008C579D` → [NtClose](../86/NtClose_function_00868870.md) (function, `0x00868870`)
- `0x008C57A8` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x008C57B5` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x008C57C2` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008C57EF` → [ExpLookupHandleTableEntry](../86/ExpLookupHandleTableEntry_function_00869DB0.md) (function, `0x00869DB0`)
- `0x008C5837` → [ObpDecrementHandleCount](../86/ObpDecrementHandleCount_function_008632E0.md) (function, `0x008632E0`)
- `0x008C5849` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008C587E` → [ObpTraceObjectReferenceIfActive](../../text/21/ObpTraceObjectReferenceIfActive_function_00210780.md) (function, `0x00210780`)
- `0x008C5887` → [ObpIncrPointerCount](../../text/43/ObpIncrPointerCount_function_00430BB0.md) (function, `0x00430BB0`)
- `0x008C58EA` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x008C58FB` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x008C5999` → [ObpCallPreOperationCallbacks](ObpCallPreOperationCallbacks_function_008C6570.md) (function, `0x008C6570`)
- `0x008C59D8` → [SeDeleteAccessState](SeDeleteAccessState_function_008C5F70.md) (function, `0x008C5F70`)
- `0x008C59E4` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x008C59F5` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x008C5A02` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008C5A21` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x008C5A66` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (function, `0x00216800`)
- `0x008C5A89` → [SeCreateAccessState](SeCreateAccessState_function_008C6AC0.md) (function, `0x008C6AC0`)
- `0x008C5AC3` → [ObpGrantAccess](../86/ObpGrantAccess_function_0086F250.md) (function, `0x0086F250`)
- `0x008C5ADF` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x008C5AEC` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x008C5B2F` → [ObpTraceObjectReferenceIfActive](../../text/21/ObpTraceObjectReferenceIfActive_function_00210780.md) (function, `0x00210780`)
- `0x008C5B37` → [ObpIncrPointerCount](../../text/43/ObpIncrPointerCount_function_00430BB0.md) (function, `0x00430BB0`)
- `0x008C5B57` → [ExpAllocateTablePagedPool](../94/ExpAllocateTablePagedPool_function_0094D634.md) (function, `0x0094D634`)
- `0x008C5B7E` → [ExpFreeTablePagedPool](../86/ExpFreeTablePagedPool_function_0086B410.md) (function, `0x0086B410`)
- `0x008C5BAA` → [ExpGetHandleExtraInfo](../86/ExpGetHandleExtraInfo_function_0086B454.md) (function, `0x0086B454`)
- `0x008C5BE6` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008C5BFF` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x008C5C42` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008C5C97` → [OBJECT_HEADER_TO_AUDIT_INFO](../../text/41/OBJECT_HEADER_TO_AUDIT_INFO_function_0041BF70.md) (function, `0x0041BF70`)
- `0x008C5CAA` → [SeAuditHandleCreation](../91/SeAuditHandleCreation_function_0091EF90.md) (function, `0x0091EF90`)
- `0x008C5CF6` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)
- `0x008C5D00` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)
- `0x008C5D0D` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x008C5D17` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (function, `0x00349EB0`)
- `0x008C5D49` → [ObpDecrementHandleCount](../86/ObpDecrementHandleCount_function_008632E0.md) (function, `0x008632E0`)
- `0x008C5D56` → [SeDeleteAccessState](SeDeleteAccessState_function_008C5F70.md) (function, `0x008C5F70`)
- `0x008C5D67` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x008C5D73` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x008C5D82` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008C5DA5` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x008C5DDE` → [EtwTraceDuplicateHandle](../A5/EtwTraceDuplicateHandle_function_00A56C5C.md) (function, `0x00A56C5C`)
- `0x008C5E1B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008C5E37` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x008C5E53` → [ExpAllocateHandleTableEntrySlow](../94/ExpAllocateHandleTableEntrySlow_function_0094D2FC.md) (function, `0x0094D2FC`)
- `0x008C5E75` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008C5EAD` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (function, `0x00216800`)
- `0x008C5EB6` → [NtClose](../86/NtClose_function_00868870.md) (function, `0x00868870`)
- `0x008C5EC1` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x008C5ECE` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x008C5EDB` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x008C5EF4` → [SeAuditingWithTokenForSubcategory](../90/SeAuditingWithTokenForSubcategory_function_009047D0.md) (function, `0x009047D0`)
- `0x008C5F15` → [SeAuditHandleDuplication](../AC/SeAuditHandleDuplication_function_00AC1458.md) (function, `0x00AC1458`)
- `0x008C5F49` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)

### Direct callers
- [CmpCreateEmptyHiveClone](../7E/CmpCreateEmptyHiveClone_function_007EE2E0.md) at `0x007EE3C4`
- [MiInitializePartitionSpecialPurposeMemory](../80/MiInitializePartitionSpecialPurposeMemory_function_0080F704.md) at `0x0080F82C`
- [CmpCreateHive](../87/CmpCreateHive_function_00879DF0.md) at `0x0087A344`
- [CmpCreateHive](../87/CmpCreateHive_function_00879DF0.md) at `0x0087A3C3`
- [NtDuplicateObject](NtDuplicateObject_function_008C4DC0.md) at `0x008C4F02`
- [DbgkpOpenHandles](../A4/DbgkpOpenHandles_function_00A4681C.md) at `0x00A46898`
- [PspPropagateHandle](../A6/PspPropagateHandle_function_00A63914.md) at `0x00A63951`
- [IoConvertFileHandleToKernelHandle](../A8/IoConvertFileHandleToKernelHandle_function_00A85680.md) at `0x00A8572E`
- [PspCopyAndFixupParameters](../AE/PspCopyAndFixupParameters_function_00AEB878.md) at `0x00AEB92F`
- [PspCopyAndFixupParameters](../AE/PspCopyAndFixupParameters_function_00AEB878.md) at `0x00AEB9A3`
- [sub_00B1802A](../B1/Unknown_function_00B1802A.md) at `0x00B18090`
- [sub_00B1802A](../B1/Unknown_function_00B1802A.md) at `0x00B180E6`
- [sub_00B3B188](../B3/Unknown_function_00B3B188.md) at `0x00B3B1FB`

### Static image references
- `0x008C4FBC` → RVA `0x00E0A740` (`.data`; read)
- `0x008C5228` → RVA `0x00F0F5B8` (`.data`; read)
- `0x008C5280` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x008C528A` → RVA `0x00FC7800` (`ALMOSTRO`; read)
- `0x008C542C` → RVA `0x00FD9B18` (`PAGEDATA`; read)
- `0x008C568C` → RVA `0x00FC6B10` (`ALMOSTRO`; read)
- `0x008C5A31` → RVA `0x008BA2B0` (`SeDefaultObjectMethod`; read)
- `0x008C5AFF` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **58**
  - `0x008C500C` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008C5020` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x008C5131` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (`PAGE` → `.text`)
  - `0x008C51AD` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (`PAGE` → `.text`)
  - `0x008C51B7` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008C51CA` → [ObpTraceObjectReferenceIfActive](../../text/21/ObpTraceObjectReferenceIfActive_function_00210780.md) (`PAGE` → `.text`)
  - `0x008C533B` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x008C535A` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (`PAGE` → `.text`)
  - `0x008C536E` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x008C5474` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008C548D` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x008C54D9` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008C555C` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008C5679` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008C5687` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008C56A7` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x008C5706` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x008C572D` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x008C5757` → [ExfAcquireRundownProtection](../../text/34/ExfAcquireRundownProtection_function_0034C050.md) (`PAGE` → `.text`)
  - `0x008C5771` → [ExfAcquireRundownProtection](../../text/34/ExfAcquireRundownProtection_function_0034C050.md) (`PAGE` → `.text`)
  - `0x008C5794` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (`PAGE` → `.text`)
  - `0x008C57A8` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x008C57B5` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x008C57C2` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008C5849` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008C587E` → [ObpTraceObjectReferenceIfActive](../../text/21/ObpTraceObjectReferenceIfActive_function_00210780.md) (`PAGE` → `.text`)
  - `0x008C5887` → [ObpIncrPointerCount](../../text/43/ObpIncrPointerCount_function_00430BB0.md) (`PAGE` → `.text`)
  - `0x008C58EA` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x008C58FB` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x008C59E4` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x008C59F5` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x008C5A02` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008C5A21` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x008C5A66` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (`PAGE` → `.text`)
  - `0x008C5ADF` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x008C5AEC` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x008C5B2F` → [ObpTraceObjectReferenceIfActive](../../text/21/ObpTraceObjectReferenceIfActive_function_00210780.md) (`PAGE` → `.text`)
  - `0x008C5B37` → [ObpIncrPointerCount](../../text/43/ObpIncrPointerCount_function_00430BB0.md) (`PAGE` → `.text`)
  - `0x008C5BE6` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008C5BFF` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x008C5C42` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008C5C97` → [OBJECT_HEADER_TO_AUDIT_INFO](../../text/41/OBJECT_HEADER_TO_AUDIT_INFO_function_0041BF70.md) (`PAGE` → `.text`)
  - `0x008C5CF6` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (`PAGE` → `.text`)
  - `0x008C5D00` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (`PAGE` → `.text`)
  - `0x008C5D0D` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x008C5D17` → [ExfReleaseRundownProtection](../../text/34/ExfReleaseRundownProtection_function_00349EB0.md) (`PAGE` → `.text`)
  - `0x008C5D67` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x008C5D73` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x008C5D82` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008C5DA5` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x008C5E1B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008C5E37` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x008C5E75` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008C5EAD` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (`PAGE` → `.text`)
  - `0x008C5EC1` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x008C5ECE` → [ExReleaseRundownProtection](../../text/34/ExReleaseRundownProtection_function_00349E80.md) (`PAGE` → `.text`)
  - `0x008C5EDB` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x008C5F49` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008C4FA0  40 55                           push rbp
008C4FA2  53                              push rbx
008C4FA3  56                              push rsi
008C4FA4  57                              push rdi
008C4FA5  41 54                           push r12
008C4FA7  41 55                           push r13
008C4FA9  41 56                           push r14
008C4FAB  41 57                           push r15
008C4FAD  48 8D AC 24 E8 FD FF FF         lea rbp, [rsp - 0x218]
008C4FB5  48 81 EC 18 03 00 00            sub rsp, 0x318
008C4FBC  48 8B 05 7D 57 54 00            mov rax, qword ptr [rip + 0x54577d]
008C4FC3  48 33 C4                        xor rax, rsp
008C4FC6  48 89 85 00 02 00 00            mov qword ptr [rbp + 0x200], rax
008C4FCD  8B B5 88 02 00 00               mov esi, dword ptr [rbp + 0x288]
008C4FD3  0F 57 C0                        xorps xmm0, xmm0
008C4FD6  49 8B D8                        mov rbx, r8
008C4FD9  48 89 55 80                     mov qword ptr [rbp - 0x80], rdx
008C4FDD  4C 8B F1                        mov r14, rcx
008C4FE0  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
008C4FE5  33 D2                           xor edx, edx
008C4FE7  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
008C4FEC  41 B8 E0 00 00 00               mov r8d, 0xe0
008C4FF2  4C 89 4D C0                     mov qword ptr [rbp - 0x40], r9
008C4FF6  48 8D 8D 20 01 00 00            lea rcx, [rbp + 0x120]
008C4FFD  4D 8B E1                        mov r12, r9
008C5000  0F 11 45 50                     movups xmmword ptr [rbp + 0x50], xmm0
008C5004  0F 11 45 60                     movups xmmword ptr [rbp + 0x60], xmm0
008C5008  0F 11 45 70                     movups xmmword ptr [rbp + 0x70], xmm0
008C500C  E8 2F 1C E0 FF                  call 0x1406c6c40
008C5011  33 D2                           xor edx, edx
008C5013  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
008C501A  41 B8 A0 00 00 00               mov r8d, 0xa0
008C5020  E8 1B 1C E0 FF                  call 0x1406c6c40
008C5025  0F B6 BD 98 02 00 00            movzx edi, byte ptr [rbp + 0x298]
008C502C  45 33 FF                        xor r15d, r15d
008C502F  44 89 7C 24 44                  mov dword ptr [rsp + 0x44], r15d
008C5034  0F 57 C0                        xorps xmm0, xmm0
008C5037  0F 11 45 88                     movups xmmword ptr [rbp - 0x78], xmm0
008C503B  0F BA E6 09                     bt esi, 9
008C503F  0F 82 B1 0A 00 00               jb 0x1408c5af6
008C5045  0F BA F6 09                     btr esi, 9
008C5049  89 74 24 48                     mov dword ptr [rsp + 0x48], esi
008C504D  4D 85 E4                        test r12, r12
008C5050  74 04                           je 0x1408c5056
008C5052  4D 89 3C 24                     mov qword ptr [r12], r15
008C5056  F6 85 90 02 00 00 02            test byte ptr [rbp + 0x290], 2
008C505D  44 8B AD 80 02 00 00            mov r13d, dword ptr [rbp + 0x280]
008C5064  0F 84 44 08 00 00               je 0x1408c58ae
008C506A  41 8B 86 70 01 00 00            mov eax, dword ptr [r14 + 0x170]
008C5071  83 E0 01                        and eax, 1
008C5074  48 85 DB                        test rbx, rbx
008C5077  0F 84 9D 07 00 00               je 0x1408c581a
008C507D  84 C0                           test al, al
008C507F  0F 85 CF 0B 00 00               jne 0x1408c5c54
008C5085  F6 83 70 01 00 00 01            test byte ptr [rbx + 0x170], 1
008C508C  0F 85 C2 0B 00 00               jne 0x1408c5c54
008C5092  49 8D 9E E8 01 00 00            lea rbx, [r14 + 0x1e8]
008C5099  0F 0D 0B                        prefetchw byte ptr [rbx]
008C509C  48 8B 03                        mov rax, qword ptr [rbx]
008C509F  48 83 E0 FE                     and rax, 0xfffffffffffffffe
008C50A3  48 8D 48 02                     lea rcx, [rax + 2]
008C50A7  F0 48 0F B1 0B                  lock cmpxchg qword ptr [rbx], rcx
008C50AC  0F 85 A2 06 00 00               jne 0x1408c5754
008C50B2  4D 8B B6 00 03 00 00            mov r14, qword ptr [r14 + 0x300]
008C50B9  4D 85 F6                        test r14, r14
008C50BC  0F 84 1A 0A 00 00               je 0x1408c5adc
008C50C2  48 8B 45 80                     mov rax, qword ptr [rbp - 0x80]
008C50C6  65 4C 8B 0C 25 88 01 00 00      mov r9, qword ptr gs:[0x188]
008C50CF  4C 8B E0                        mov r12, rax
008C50D2  4C 89 4C 24 58                  mov qword ptr [rsp + 0x58], r9
008C50D7  85 C0                           test eax, eax
008C50D9  0F 88 7A 07 00 00               js 0x1408c5859
008C50DF  66 41 FF 89 E4 01 00 00         dec word ptr [r9 + 0x1e4]
008C50E7  90                              nop
008C50E8  41 F7 C4 FC 03 00 00            test r12d, 0x3fc
008C50EF  0F 84 F2 07 00 00               je 0x1408c58e7
008C50F5  49 8B D4                        mov rdx, r12
008C50F8  49 8B CE                        mov rcx, r14
008C50FB  E8 B0 4C FA FF                  call 0x140869db0
008C5100  48 8B F8                        mov rdi, rax
008C5103  48 85 C0                        test rax, rax
008C5106  0F 84 DB 07 00 00               je 0x1408c58e7
008C510C  0F 1F 40 00                     nop dword ptr [rax]
008C5110  0F 0D 0F                        prefetchw byte ptr [rdi]
008C5113  4C 8B 07                        mov r8, qword ptr [rdi]
008C5116  41 F6 C0 01                     test r8b, 1
008C511A  0F 84 1B 06 00 00               je 0x1408c573b
008C5120  49 8D 48 FF                     lea rcx, [r8 - 1]
008C5124  49 8B C0                        mov rax, r8
008C5127  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
008C512C  75 E2                           jne 0x1408c5110
008C512E  48 8B CF                        mov rcx, rdi
008C5131  E8 5A BB B6 FF                  call 0x140430c90
008C5136  8B 5F 08                        mov ebx, dword ptr [rdi + 8]
008C5139  48 8B F0                        mov rsi, rax
008C513C  81 E3 FF FF FF 01               and ebx, 0x1ffffff
008C5142  45 39 7E 04                     cmp dword ptr [r14 + 4], r15d
008C5146  74 1A                           je 0x1408c5162
008C5148  49 8B D4                        mov rdx, r12
008C514B  49 8B CE                        mov rcx, r14
008C514E  E8 01 63 FA FF                  call 0x14086b454
008C5153  48 85 C0                        test rax, rax
008C5156  74 0A                           je 0x1408c5162
008C5158  48 8B 00                        mov rax, qword ptr [rax]
008C515B  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
008C5160  EB 05                           jmp 0x1408c5167
008C5162  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
008C5167  8B 0F                           mov ecx, dword ptr [rdi]
008C5169  B8 01 00 00 00                  mov eax, 1
008C516E  48 C1 F9 11                     sar rcx, 0x11
008C5172  83 E1 07                        and ecx, 7
008C5175  44 8B E1                        mov r12d, ecx
008C5178  41 83 CC 08                     or r12d, 8
008C517C  F7 47 08 00 00 00 02            test dword ptr [rdi + 8], 0x2000000
008C5183  44 0F 44 E1                     cmove r12d, ecx
008C5187  F0 48 0F C1 06                  lock xadd qword ptr [rsi], rax
008C518C  48 FF C0                        inc rax
008C518F  48 83 F8 01                     cmp rax, 1
008C5193  0F 8E 76 08 00 00               jle 0x1408c5a0f
008C5199  F0 48 FF 07                     lock inc qword ptr [rdi]
008C519D  49 8D 4E 30                     lea rcx, [r14 + 0x30]
008C51A1  F0 44 09 3C 24                  lock or dword ptr [rsp], r15d
008C51A6  4C 39 39                        cmp qword ptr [rcx], r15
008C51A9  74 07                           je 0x1408c51b2
008C51AB  33 D2                           xor edx, edx
008C51AD  E8 2E EE 9D FF                  call 0x1402a3fe0
008C51B2  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008C51B7  E8 34 9E 99 FF                  call 0x14025eff0
008C51BC  BA 01 00 00 00                  mov edx, 1
008C51C1  41 B8 4F 62 48 6E               mov r8d, 0x6e48624f
008C51C7  48 8B CE                        mov rcx, rsi
008C51CA  E8 B1 B5 94 FF                  call 0x140210780
008C51CF  4C 8D 76 30                     lea r14, [rsi + 0x30]
008C51D3  8B 74 24 48                     mov esi, dword ptr [rsp + 0x48]
008C51D7  4C 89 74 24 58                  mov qword ptr [rsp + 0x58], r14
008C51DC  41 8B FF                        mov edi, r15d
008C51DF  41 F6 C4 04                     test r12b, 4
008C51E3  75 05                           jne 0x1408c51ea
008C51E5  44 89 7C 24 70                  mov dword ptr [rsp + 0x70], r15d
008C51EA  4C 8B 7C 24 60                  mov r15, qword ptr [rsp + 0x60]
008C51EF  4D 85 FF                        test r15, r15
008C51F2  0F 84 9B 0C 00 00               je 0x1408c5e93
008C51F8  49 8D BF E8 01 00 00            lea rdi, [r15 + 0x1e8]
008C51FF  0F 0D 0F                        prefetchw byte ptr [rdi]
008C5202  48 8B 07                        mov rax, qword ptr [rdi]
008C5205  48 83 E0 FE                     and rax, 0xfffffffffffffffe
008C5209  48 8D 48 02                     lea rcx, [rax + 2]
008C520D  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
008C5212  0F 85 56 05 00 00               jne 0x1408c576e
008C5218  4D 8B BF 00 03 00 00            mov r15, qword ptr [r15 + 0x300]
008C521F  4D 85 FF                        test r15, r15
008C5222  0F 84 C1 08 00 00               je 0x1408c5ae9
008C5228  4C 3B 3D 89 A3 64 00            cmp r15, qword ptr [rip + 0x64a389]
008C522F  0F 84 91 07 00 00               je 0x1408c59c6
008C5235  C6 44 24 40 00                  mov byte ptr [rsp + 0x40], 0
008C523A  8B 8D 90 02 00 00               mov ecx, dword ptr [rbp + 0x290]
008C5240  F6 C1 02                        test cl, 2
008C5243  44 0F 45 EB                     cmovne r13d, ebx
008C5247  F6 C1 04                        test cl, 4
008C524A  0F 85 F6 08 00 00               jne 0x1408c5b46
008C5250  41 8B C4                        mov eax, r12d
008C5253  83 E0 0C                        and eax, 0xc
008C5256  0B F0                           or esi, eax
008C5258  49 8D 56 D0                     lea rdx, [r14 - 0x30]
008C525C  89 74 24 48                     mov dword ptr [rsp + 0x48], esi
008C5260  83 CE 08                        or esi, 8
008C5263  48 89 55 A8                     mov qword ptr [rbp - 0x58], rdx
008C5267  F6 C1 08                        test cl, 8
008C526A  48 8B C2                        mov rax, rdx
008C526D  0F 44 74 24 48                  cmove esi, dword ptr [rsp + 0x48]
008C5272  48 C1 E8 08                     shr rax, 8
008C5276  0F B6 C8                        movzx ecx, al
008C5279  0F B6 42 18                     movzx eax, byte ptr [rdx + 0x18]
008C527D  48 33 C8                        xor rcx, rax
008C5280  0F B6 05 C5 1B 70 00            movzx eax, byte ptr [rip + 0x701bc5]
008C5287  48 33 C8                        xor rcx, rax
008C528A  48 8D 05 6F 25 70 00            lea rax, [rip + 0x70256f]
008C5291  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
008C5295  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
008C5299  41 F7 C5 00 00 00 F0            test r13d, 0xf0000000
008C52A0  74 31                           je 0x1408c52d3
008C52A2  45 85 ED                        test r13d, r13d
008C52A5  79 04                           jns 0x1408c52ab
008C52A7  44 0B 68 4C                     or r13d, dword ptr [rax + 0x4c]
008C52AB  41 0F BA E5 1E                  bt r13d, 0x1e
008C52B0  73 04                           jae 0x1408c52b6
008C52B2  44 0B 68 50                     or r13d, dword ptr [rax + 0x50]
008C52B6  41 0F BA E5 1D                  bt r13d, 0x1d
008C52BB  73 04                           jae 0x1408c52c1
008C52BD  44 0B 68 54                     or r13d, dword ptr [rax + 0x54]
008C52C1  41 0F BA E5 1C                  bt r13d, 0x1c
008C52C6  73 04                           jae 0x1408c52cc
008C52C8  44 0B 68 58                     or r13d, dword ptr [rax + 0x58]
008C52CC  41 81 E5 FF FF FF 0F            and r13d, 0xfffffff
008C52D3  8B 78 5C                        mov edi, dword ptr [rax + 0x5c]
008C52D6  45 32 F6                        xor r14b, r14b
008C52D9  0F BA EF 18                     bts edi, 0x18
008C52DD  F7 D3                           not ebx
008C52DF  41 23 FD                        and edi, r13d
008C52E2  45 33 ED                        xor r13d, r13d
008C52E5  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
008C52E9  4C 89 6D B8                     mov qword ptr [rbp - 0x48], r13
008C52ED  85 DF                           test edi, ebx
008C52EF  0F 85 32 07 00 00               jne 0x1408c5a27
008C52F5  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
008C52FA  0F B6 85 98 02 00 00            movzx eax, byte ptr [rbp + 0x298]
008C5301  48 8D 54 24 44                  lea rdx, [rsp + 0x44]
008C5306  4C 8B 44 24 60                  mov r8, qword ptr [rsp + 0x60]
008C530B  4C 8B CB                        mov r9, rbx
008C530E  48 C7 44 24 30 00 00 00 00      mov qword ptr [rsp + 0x30], 0
008C5317  B9 02 00 00 00                  mov ecx, 2
008C531C  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
008C5320  88 44 24 20                     mov byte ptr [rsp + 0x20], al
008C5324  E8 E7 86 FA FF                  call 0x14086da10
008C5329  44 8B E0                        mov r12d, eax
008C532C  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
008C5330  45 84 F6                        test r14b, r14b
008C5333  74 0B                           je 0x1408c5340
008C5335  33 D2                           xor edx, edx
008C5337  48 8D 4D 50                     lea rcx, [rbp + 0x50]
008C533B  E8 F0 29 95 FF                  call 0x140217d30
008C5340  8B 7C 24 44                     mov edi, dword ptr [rsp + 0x44]
008C5344  8B 85 90 02 00 00               mov eax, dword ptr [rbp + 0x290]
008C534A  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
008C534F  A8 01                           test al, 1
008C5351  74 24                           je 0x1408c5377
008C5353  48 8D 55 50                     lea rdx, [rbp + 0x50]
008C5357  49 8B CE                        mov rcx, r14
008C535A  E8 A1 14 95 FF                  call 0x140216800
008C535F  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
008C5363  E8 08 35 FA FF                  call 0x140868870
008C5368  33 D2                           xor edx, edx
008C536A  48 8D 4D 50                     lea rcx, [rbp + 0x50]
008C536E  E8 BD 29 95 FF                  call 0x140217d30
008C5373  8B 7C 24 44                     mov edi, dword ptr [rsp + 0x44]
008C5377  45 85 E4                        test r12d, r12d
008C537A  0F 88 50 06 00 00               js 0x1408c59d0
008C5380  89 74 24 48                     mov dword ptr [rsp + 0x48], esi
008C5384  44 8B F6                        mov r14d, esi
008C5387  4D 85 ED                        test r13, r13
008C538A  0F 85 3E 09 00 00               jne 0x1408c5cce
008C5390  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
008C5394  48 8D 45 88                     lea rax, [rbp - 0x78]
008C5398  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
008C539C  48 8D 45 88                     lea rax, [rbp - 0x78]
008C53A0  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
008C53A4  F6 41 42 40                     test byte ptr [rcx + 0x42], 0x40
008C53A8  0F 85 5C 05 00 00               jne 0x1408c590a
008C53AE  4C 8B 65 A8                     mov r12, qword ptr [rbp - 0x58]
008C53B2  41 8B CE                        mov ecx, r14d
008C53B5  83 E1 07                        and ecx, 7
008C53B8  48 C7 45 D0 00 00 00 00         mov qword ptr [rbp - 0x30], 0
008C53C0  48 C1 E1 11                     shl rcx, 0x11
008C53C4  81 E7 FF FF FF 01               and edi, 0x1ffffff
008C53CA  49 8B C4                        mov rax, r12
008C53CD  89 7D D0                        mov dword ptr [rbp - 0x30], edi
008C53D0  48 C1 E0 10                     shl rax, 0x10
008C53D4  48 25 FF FF F1 FF               and rax, 0xfffffffffff1ffff
008C53DA  48 0B C8                        or rcx, rax
008C53DD  48 89 4D C8                     mov qword ptr [rbp - 0x38], rcx
008C53E1  41 F6 C6 08                     test r14b, 8
008C53E5  74 04                           je 0x1408c53eb
008C53E7  0F BA EF 19                     bts edi, 0x19
008C53EB  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008C53F4  48 83 C9 01                     or rcx, 1
008C53F8  89 7D D0                        mov dword ptr [rbp - 0x30], edi
008C53FB  33 FF                           xor edi, edi
008C53FD  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
008C5401  8B F7                           mov esi, edi
008C5403  48 89 4D C8                     mov qword ptr [rbp - 0x38], rcx
008C5407  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008C540E  90                              nop
008C540F  41 0F B6 47 2C                  movzx eax, byte ptr [r15 + 0x2c]
008C5414  A8 04                           test al, 4
008C5416  0F 85 37 0B 00 00               jne 0x1408c5f53
008C541C  A8 01                           test al, 1
008C541E  0F 85 66 08 00 00               jne 0x1408c5c8a
008C5424  65 8B 0C 25 A4 01 00 00         mov ecx, dword ptr gs:[0x1a4]
008C542C  8B 05 E6 46 71 00               mov eax, dword ptr [rip + 0x7146e6]
008C5432  44 8B E1                        mov r12d, ecx
008C5435  89 44 24 78                     mov dword ptr [rsp + 0x78], eax
008C5439  48 C7 C3 FF FF FF FF            mov rbx, 0xffffffffffffffff
008C5440  89 4D 98                        mov dword ptr [rbp - 0x68], ecx
008C5443  41 8B 0F                        mov ecx, dword ptr [r15]
008C5446  44 8B EF                        mov r13d, edi
008C5449  89 4D D8                        mov dword ptr [rbp - 0x28], ecx
008C544C  44 3B E8                        cmp r13d, eax
008C544F  0F 83 A8 09 00 00               jae 0x1408c5dfd
008C5455  41 8B FC                        mov edi, r12d
008C5458  48 FF C7                        inc rdi
008C545B  48 C1 E7 06                     shl rdi, 6
008C545F  49 03 FF                        add rdi, r15
008C5462  48 39 77 08                     cmp qword ptr [rdi + 8], rsi
008C5466  0F 84 25 04 00 00               je 0x1408c5891
008C546C  45 33 C0                        xor r8d, r8d
008C546F  33 D2                           xor edx, edx
008C5471  48 8B CF                        mov rcx, rdi
008C5474  E8 B7 AD 94 FF                  call 0x140210230
008C5479  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
008C547F  4C 8B F0                        mov r14, rax
008C5482  73 0E                           jae 0x1408c5492
008C5484  4C 8B C7                        mov r8, rdi
008C5487  48 8B D0                        mov rdx, rax
008C548A  48 8B CF                        mov rcx, rdi
008C548D  E8 FE A7 94 FF                  call 0x14020fc90
008C5492  4D 85 F6                        test r14, r14
008C5495  74 05                           je 0x1408c549c
008C5497  41 C6 46 0A 01                  mov byte ptr [r14 + 0xa], 1
008C549C  4C 8B 77 08                     mov r14, qword ptr [rdi + 8]
008C54A0  4D 85 F6                        test r14, r14
008C54A3  74 1F                           je 0x1408c54c4
008C54A5  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
008C54A9  48 89 47 08                     mov qword ptr [rdi + 8], rax
008C54AD  48 85 C0                        test rax, rax
008C54B0  75 04                           jne 0x1408c54b6
008C54B2  48 89 77 10                     mov qword ptr [rdi + 0x10], rsi
008C54B6  FF 47 18                        inc dword ptr [rdi + 0x18]
008C54B9  8B 47 18                        mov eax, dword ptr [rdi + 0x18]
008C54BC  3B 47 1C                        cmp eax, dword ptr [rdi + 0x1c]
008C54BF  7E 03                           jle 0x1408c54c4
008C54C1  89 47 1C                        mov dword ptr [rdi + 0x1c], eax
008C54C4  48 8B C3                        mov rax, rbx
008C54C7  F0 48 0F C1 07                  lock xadd qword ptr [rdi], rax
008C54CC  24 06                           and al, 6
008C54CE  3C 02                           cmp al, 2
008C54D0  0F 84 34 08 00 00               je 0x1408c5d0a
008C54D6  48 8B CF                        mov rcx, rdi
008C54D9  E8 22 C1 A1 FF                  call 0x1402e1600
008C54DE  4D 85 F6                        test r14, r14
008C54E1  0F 84 AA 03 00 00               je 0x1408c5891
008C54E7  49 8B C6                        mov rax, r14
008C54EA  49 8B CE                        mov rcx, r14
008C54ED  48 25 00 F0 FF FF               and rax, 0xfffffffffffff000
008C54F3  48 2B C8                        sub rcx, rax
008C54F6  48 C1 F9 04                     sar rcx, 4
008C54FA  83 7C 24 70 00                  cmp dword ptr [rsp + 0x70], 0
008C54FF  48 8B 40 08                     mov rax, qword ptr [rax + 8]
008C5503  48 8D 34 88                     lea rsi, [rax + rcx*4]
008C5507  8B C6                           mov eax, esi
008C5509  8B CE                           mov ecx, esi
008C550B  0F 85 C0 02 00 00               jne 0x1408c57d1
008C5511  83 7C 24 74 00                  cmp dword ptr [rsp + 0x74], 0
008C5516  0F 85 B5 02 00 00               jne 0x1408c57d1
008C551C  49 83 7F 60 00                  cmp qword ptr [r15 + 0x60], 0
008C5521  48 8B 5D A0                     mov rbx, qword ptr [rbp - 0x60]
008C5525  74 14                           je 0x1408c553b
008C5527  41 B9 01 00 00 00               mov r9d, 1
008C552D  4C 8B C6                        mov r8, rsi
008C5530  48 8B D3                        mov rdx, rbx
008C5533  49 8B CF                        mov rcx, r15
008C5536  E8 39 5C FA FF                  call 0x14086b174
008C553B  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
008C553F  33 FF                           xor edi, edi
008C5541  49 89 46 08                     mov qword ptr [r14 + 8], rax
008C5545  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
008C5549  49 89 06                        mov qword ptr [r14], rax
008C554C  4C 8B 6D B8                     mov r13, qword ptr [rbp - 0x48]
008C5550  44 8B 74 24 48                  mov r14d, dword ptr [rsp + 0x48]
008C5555  4C 8B 65 A8                     mov r12, qword ptr [rbp - 0x58]
008C5559  48 8B CB                        mov rcx, rbx
008C555C  E8 8F 9A 99 FF                  call 0x14025eff0
008C5561  48 85 F6                        test rsi, rsi
008C5564  0F 84 C2 02 00 00               je 0x1408c582c
008C556A  4D 85 ED                        test r13, r13
008C556D  0F 85 1E 07 00 00               jne 0x1408c5c91
008C5573  41 F6 C6 04                     test r14b, 4
008C5577  0F 85 6A 09 00 00               jne 0x1408c5ee7
008C557D  4C 8B 64 24 60                  mov r12, qword ptr [rsp + 0x60]
008C5582  44 8B 74 24 4C                  mov r14d, dword ptr [rsp + 0x4c]
008C5587  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
008C558C  0F B6 5C 24 40                  movzx ebx, byte ptr [rsp + 0x40]
008C5591  84 DB                           test bl, bl
008C5593  74 07                           je 0x1408c559c
008C5595  48 81 CE 00 00 00 80            or rsi, 0xffffffff80000000
008C559C  48 8B 45 C0                     mov rax, qword ptr [rbp - 0x40]
008C55A0  48 85 C0                        test rax, rax
008C55A3  74 03                           je 0x1408c55a8
008C55A5  48 89 30                        mov qword ptr [rax], rsi
008C55A8  4D 85 ED                        test r13, r13
008C55AB  74 08                           je 0x1408c55b5
008C55AD  49 8B CD                        mov rcx, r13
008C55B0  E8 BB 09 00 00                  call 0x1408c5f70
008C55B5  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
008C55BA  49 8D 8D E8 01 00 00            lea rcx, [r13 + 0x1e8]
008C55C1  0F 0D 09                        prefetchw byte ptr [rcx]
008C55C4  48 8B 01                        mov rax, qword ptr [rcx]
008C55C7  48 83 E0 FE                     and rax, 0xfffffffffffffffe
008C55CB  48 8D 50 FE                     lea rdx, [rax - 2]
008C55CF  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
008C55D4  0F 85 1C 07 00 00               jne 0x1408c5cf6
008C55DA  49 8D 8C 24 E8 01 00 00         lea rcx, [r12 + 0x1e8]
008C55E2  0F 0D 09                        prefetchw byte ptr [rcx]
008C55E5  48 8B 01                        mov rax, qword ptr [rcx]
008C55E8  48 83 E0 FE                     and rax, 0xfffffffffffffffe
008C55EC  48 8D 50 FE                     lea rdx, [rax - 2]
008C55F0  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
008C55F5  0F 85 05 07 00 00               jne 0x1408c5d00
008C55FB  4C 8B 45 88                     mov r8, qword ptr [rbp - 0x78]
008C55FF  48 8D 45 88                     lea rax, [rbp - 0x78]
008C5603  4C 3B C0                        cmp r8, rax
008C5606  0F 84 80 00 00 00               je 0x1408c568c
008C560C  48 8D 44 24 50                  lea rax, [rsp + 0x50]
008C5611  48 89 7D 10                     mov qword ptr [rbp + 0x10], rdi
008C5615  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
008C5619  49 8D 47 D0                     lea rax, [r15 - 0x30]
008C561D  48 C1 E8 08                     shr rax, 8
008C5621  0F B6 C8                        movzx ecx, al
008C5624  41 0F B6 47 E8                  movzx eax, byte ptr [r15 - 0x18]
008C5629  48 33 C8                        xor rcx, rax
008C562C  89 7D 1C                        mov dword ptr [rbp + 0x1c], edi
008C562F  0F B6 05 16 18 70 00            movzx eax, byte ptr [rip + 0x701816]
008C5636  83 E7 FE                        and edi, 0xfffffffe
008C5639  0B FB                           or edi, ebx
008C563B  C7 45 F8 02 00 00 00            mov dword ptr [rbp - 8], 2
008C5642  48 33 C8                        xor rcx, rax
008C5645  89 7D FC                        mov dword ptr [rbp - 4], edi
008C5648  48 8D 05 B1 21 70 00            lea rax, [rip + 0x7021b1]
008C564F  4C 89 7D 00                     mov qword ptr [rbp], r15
008C5653  44 89 75 18                     mov dword ptr [rbp + 0x18], r14d
008C5657  48 8B 04 C8                     mov rax, qword ptr [rax + rcx*8]
008C565B  48 89 45 08                     mov qword ptr [rbp + 8], rax
008C565F  8B 44 24 44                     mov eax, dword ptr [rsp + 0x44]
008C5663  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
008C5667  48 8D 45 88                     lea rax, [rbp - 0x78]
008C566B  4C 3B C0                        cmp r8, rax
008C566E  75 51                           jne 0x1408c56c1
008C5670  48 8B 4D 00                     mov rcx, qword ptr [rbp]
008C5674  BA 4F 62 43 62                  mov edx, 0x6243624f
008C5679  E8 62 22 A3 FF                  call 0x1402f78e0
008C567E  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
008C5687  E8 64 99 99 FF                  call 0x14025eff0
008C568C  8B 05 7E 14 70 00               mov eax, dword ptr [rip + 0x70147e]
008C5692  A8 40                           test al, 0x40
008C5694  0F 85 15 07 00 00               jne 0x1408c5daf
008C569A  41 8B C6                        mov eax, r14d
008C569D  48 8B 8D 00 02 00 00            mov rcx, qword ptr [rbp + 0x200]
008C56A4  48 33 CC                        xor rcx, rsp
008C56A7  E8 94 6F DE FF                  call 0x1406ac640
008C56AC  48 81 C4 18 03 00 00            add rsp, 0x318
008C56B3  41 5F                           pop r15
008C56B5  41 5E                           pop r14
008C56B7  41 5D                           pop r13
008C56B9  41 5C                           pop r12
008C56BB  5F                              pop rdi
008C56BC  5E                              pop rsi
008C56BD  5B                              pop rbx
008C56BE  5D                              pop rbp
008C56BF  C3                              ret
008C56C0  CC                              int3
008C56C1  48 8B 7D 90                     mov rdi, qword ptr [rbp - 0x70]
008C56C5  48 8D 4D 88                     lea rcx, [rbp - 0x78]
008C56C9  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008C56CD  48 39 0F                        cmp qword ptr [rdi], rcx
008C56D0  0F 85 49 08 00 00               jne 0x1408c5f1f
008C56D6  48 39 38                        cmp qword ptr [rax], rdi
008C56D9  0F 85 40 08 00 00               jne 0x1408c5f1f
008C56DF  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
008C56E3  48 8D 4D 88                     lea rcx, [rbp - 0x78]
008C56E7  48 89 08                        mov qword ptr [rax], rcx
008C56EA  48 8D 55 F8                     lea rdx, [rbp - 8]
008C56EE  48 8B 5F 10                     mov rbx, qword ptr [rdi + 0x10]
008C56F2  48 8B 47 18                     mov rax, qword ptr [rdi + 0x18]
008C56F6  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
008C56FA  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
008C56FE  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
008C5702  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
008C5706  E8 C5 53 DF FF                  call 0x1406baad0
008C570B  48 8D 4B 38                     lea rcx, [rbx + 0x38]
008C570F  0F 0D 09                        prefetchw byte ptr [rcx]
008C5712  48 8B 01                        mov rax, qword ptr [rcx]
008C5715  48 83 E0 FE                     and rax, 0xfffffffffffffffe
008C5719  48 8D 50 FE                     lea rdx, [rax - 2]
008C571D  F0 48 0F B1 11                  lock cmpxchg qword ptr [rcx], rdx
008C5722  0F 85 EF 05 00 00               jne 0x1408c5d17
008C5728  33 D2                           xor edx, edx
008C572A  48 8B CF                        mov rcx, rdi
008C572D  E8 3E D1 2B 00                  call 0x140b82870
008C5732  4C 8B 45 88                     mov r8, qword ptr [rbp - 0x78]
008C5736  E9 2C FF FF FF                  jmp 0x1408c5667
008C573B  4D 85 C0                        test r8, r8
008C573E  0F 84 9E 01 00 00               je 0x1408c58e2
008C5744  48 8B D7                        mov rdx, rdi
008C5747  49 8B CE                        mov rcx, r14
008C574A  E8 E9 30 FA FF                  call 0x140868838
008C574F  E9 BC F9 FF FF                  jmp 0x1408c5110
008C5754  48 8B CB                        mov rcx, rbx
008C5757  E8 F4 68 A8 FF                  call 0x14034c050
008C575C  84 C0                           test al, al
008C575E  0F 85 4E F9 FF FF               jne 0x1408c50b2
008C5764  B8 0A 01 00 C0                  mov eax, 0xc000010a
008C5769  E9 2F FF FF FF                  jmp 0x1408c569d
008C576E  48 8B CF                        mov rcx, rdi
008C5771  E8 DA 68 A8 FF                  call 0x14034c050
008C5776  84 C0                           test al, al
008C5778  0F 85 9A FA FF FF               jne 0x1408c5218
008C577E  8B 85 90 02 00 00               mov eax, dword ptr [rbp + 0x290]
008C5784  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
008C5789  A8 01                           test al, 1
008C578B  74 20                           je 0x1408c57ad
008C578D  48 8D 55 50                     lea rdx, [rbp + 0x50]
008C5791  49 8B CC                        mov rcx, r12
008C5794  E8 67 10 95 FF                  call 0x140216800
008C5799  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
008C579D  E8 CE 30 FA FF                  call 0x140868870
008C57A2  33 D2                           xor edx, edx
008C57A4  48 8D 4D 50                     lea rcx, [rbp + 0x50]
008C57A8  E8 83 25 95 FF                  call 0x140217d30
008C57AD  49 8D 8C 24 E8 01 00 00         lea rcx, [r12 + 0x1e8]
008C57B5  E8 C6 46 A8 FF                  call 0x140349e80
008C57BA  BA 4F 62 48 6E                  mov edx, 0x6e48624f
008C57BF  49 8B CE                        mov rcx, r14
008C57C2  E8 19 21 A3 FF                  call 0x1402f78e0
008C57C7  B8 0A 01 00 C0                  mov eax, 0xc000010a
008C57CC  E9 CC FE FF FF                  jmp 0x1408c569d
008C57D1  81 E1 03 FC FF FF               and ecx, 0xfffffc03
008C57D7  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
008C57DC  89 4C 24 68                     mov dword ptr [rsp + 0x68], ecx
008C57E0  49 8B CF                        mov rcx, r15
008C57E3  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
008C57E8  C1 E8 02                        shr eax, 2
008C57EB  44 0F B6 E0                     movzx r12d, al
008C57EF  E8 BC 45 FA FF                  call 0x140869db0
008C57F4  48 8B F8                        mov rdi, rax
008C57F7  48 85 C0                        test rax, rax
008C57FA  0F 84 8F 03 00 00               je 0x1408c5b8f
008C5800  48 8B 08                        mov rcx, qword ptr [rax]
008C5803  48 85 C9                        test rcx, rcx
008C5806  0F 84 42 03 00 00               je 0x1408c5b4e
008C580C  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
008C5811  4A 89 04 E1                     mov qword ptr [rcx + r12*8], rax
008C5815  E9 02 FD FF FF                  jmp 0x1408c551c
008C581A  84 C0                           test al, al
008C581C  0F 84 70 F8 FF FF               je 0x1408c5092
008C5822  B8 22 00 00 C0                  mov eax, 0xc0000022
008C5827  E9 71 FE FF FF                  jmp 0x1408c569d
008C582C  49 8B D4                        mov rdx, r12
008C582F  4C 8B 64 24 60                  mov r12, qword ptr [rsp + 0x60]
008C5834  49 8B CC                        mov rcx, r12
008C5837  E8 A4 DA F9 FF                  call 0x1408632e0
008C583C  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
008C5841  BA 4F 62 48 6E                  mov edx, 0x6e48624f
008C5846  49 8B CF                        mov rcx, r15
008C5849  E8 92 20 A3 FF                  call 0x1402f78e0
008C584E  41 BE 9A 00 00 C0               mov r14d, 0xc000009a
008C5854  E9 33 FD FF FF                  jmp 0x1408c558c
008C5859  48 83 F8 FF                     cmp rax, -1
008C585D  75 61                           jne 0x1408c58c0
008C585F  4C 8B 74 24 50                  mov r14, qword ptr [rsp + 0x50]
008C5864  8D 50 02                        lea edx, [rax + 2]
008C5867  41 B8 4F 62 48 6E               mov r8d, 0x6e48624f
008C586D  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
008C5872  BB FF FF 1F 00                  mov ebx, 0x1fffff
008C5877  45 8B E7                        mov r12d, r15d
008C587A  49 8D 4E D0                     lea rcx, [r14 - 0x30]
008C587E  E8 FD AE 94 FF                  call 0x140210780
008C5883  49 8D 4E D0                     lea rcx, [r14 - 0x30]
008C5887  E8 24 B3 B6 FF                  call 0x140430bb0
008C588C  E9 46 F9 FF FF                  jmp 0x1408c51d7
008C5891  41 FF C4                        inc r12d
008C5894  33 C0                           xor eax, eax
008C5896  41 FF C5                        inc r13d
008C5899  44 3B 64 24 78                  cmp r12d, dword ptr [rsp + 0x78]
008C589E  41 0F 45 C4                     cmovne eax, r12d
008C58A2  44 8B E0                        mov r12d, eax
008C58A5  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
008C58A9  E9 9E FB FF FF                  jmp 0x1408c544c
008C58AE  41 F7 C5 00 00 E0 0C            test r13d, 0xce00000
008C58B5  0F 84 AF F7 FF FF               je 0x1408c506a
008C58BB  E9 62 FF FF FF                  jmp 0x1408c5822
008C58C0  48 83 F8 FE                     cmp rax, -2
008C58C4  0F 84 46 02 00 00               je 0x1408c5b10
008C58CA  40 84 FF                        test dil, dil
008C58CD  75 20                           jne 0x1408c58ef
008C58CF  4C 8B 35 E2 9C 64 00            mov r14, qword ptr [rip + 0x649ce2]
008C58D6  49 81 F4 00 00 00 80            xor r12, 0xffffffff80000000
008C58DD  E9 FD F7 FF FF                  jmp 0x1408c50df
008C58E2  4C 8B 4C 24 58                  mov r9, qword ptr [rsp + 0x58]
008C58E7  49 8B C9                        mov rcx, r9
008C58EA  E8 01 97 99 FF                  call 0x14025eff0
008C58EF  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
008C58F4  48 81 C1 E8 01 00 00            add rcx, 0x1e8
008C58FB  E8 80 45 A8 FF                  call 0x140349e80
008C5900  B8 08 00 00 C0                  mov eax, 0xc0000008
008C5905  E9 93 FD FF FF                  jmp 0x1408c569d
008C590A  48 8D 81 C8 00 00 00            lea rax, [rcx + 0xc8]
008C5911  48 39 00                        cmp qword ptr [rax], rax
008C5914  0F 84 94 FA FF FF               je 0x1408c53ae
008C591A  0F B6 74 24 40                  movzx esi, byte ptr [rsp + 0x40]
008C591F  48 8D 43 D0                     lea rax, [rbx - 0x30]
008C5923  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
008C5928  48 8D 0D D1 1E 70 00            lea rcx, [rip + 0x701ed1]
008C592F  48 C1 E8 08                     shr rax, 8
008C5933  45 33 C0                        xor r8d, r8d
008C5936  0F B6 D0                        movzx edx, al
008C5939  0F B6 43 E8                     movzx eax, byte ptr [rbx - 0x18]
008C593D  48 33 D0                        xor rdx, rax
008C5940  0F B6 05 05 15 70 00            movzx eax, byte ptr [rip + 0x701505]
008C5947  48 33 D0                        xor rdx, rax
008C594A  48 8D 45 E0                     lea rax, [rbp - 0x20]
008C594E  48 8B 0C D1                     mov rcx, qword ptr [rcx + rdx*8]
008C5952  41 8B D0                        mov edx, r8d
008C5955  83 E2 FE                        and edx, 0xfffffffe
008C5958  0B D6                           or edx, esi
008C595A  8B 59 60                        mov ebx, dword ptr [rcx + 0x60]
008C595D  48 89 45 48                     mov qword ptr [rbp + 0x48], rax
008C5961  23 DF                           and ebx, edi
008C5963  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
008C5968  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
008C596C  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
008C5971  89 55 2C                        mov dword ptr [rbp + 0x2c], edx
008C5974  48 8D 55 28                     lea rdx, [rbp + 0x28]
008C5978  4C 89 45 40                     mov qword ptr [rbp + 0x40], r8
008C597C  4C 8D 45 88                     lea r8, [rbp - 0x78]
008C5980  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
008C5984  C7 45 28 02 00 00 00            mov dword ptr [rbp + 0x28], 2
008C598B  48 89 4D 38                     mov qword ptr [rbp + 0x38], rcx
008C598F  89 7D E4                        mov dword ptr [rbp - 0x1c], edi
008C5992  89 7D E0                        mov dword ptr [rbp - 0x20], edi
008C5995  4C 89 65 E8                     mov qword ptr [rbp - 0x18], r12
008C5999  E8 D2 0B 00 00                  call 0x1408c6570
008C599E  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
008C59A2  44 8B E0                        mov r12d, eax
008C59A5  85 C0                           test eax, eax
008C59A7  0F 88 74 03 00 00               js 0x1408c5d21
008C59AD  40 84 F6                        test sil, sil
008C59B0  0F 85 6B 03 00 00               jne 0x1408c5d21
008C59B6  8B 45 E0                        mov eax, dword ptr [rbp - 0x20]
008C59B9  0B C3                           or eax, ebx
008C59BB  23 F8                           and edi, eax
008C59BD  89 7C 24 44                     mov dword ptr [rsp + 0x44], edi
008C59C1  E9 E8 F9 FF FF                  jmp 0x1408c53ae
008C59C6  C6 44 24 40 01                  mov byte ptr [rsp + 0x40], 1
008C59CB  E9 6A F8 FF FF                  jmp 0x1408c523a
008C59D0  4D 85 ED                        test r13, r13
008C59D3  74 08                           je 0x1408c59dd
008C59D5  49 8B CD                        mov rcx, r13
008C59D8  E8 93 05 00 00                  call 0x1408c5f70
008C59DD  49 8D 8E E8 01 00 00            lea rcx, [r14 + 0x1e8]
008C59E4  E8 97 44 A8 FF                  call 0x140349e80
008C59E9  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
008C59EE  48 81 C1 E8 01 00 00            add rcx, 0x1e8
008C59F5  E8 86 44 A8 FF                  call 0x140349e80
008C59FA  BA 4F 62 48 6E                  mov edx, 0x6e48624f
008C59FF  48 8B CB                        mov rcx, rbx
008C5A02  E8 D9 1E A3 FF                  call 0x1402f78e0
008C5A07  41 8B C4                        mov eax, r12d
008C5A0A  E9 8E FC FF FF                  jmp 0x1408c569d
008C5A0F  33 D2                           xor edx, edx
008C5A11  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008C5A16  4C 8D 46 30                     lea r8, [rsi + 0x30]
008C5A1A  8D 4A 18                        lea ecx, [rdx + 0x18]
008C5A1D  44 8D 4A 10                     lea r9d, [rdx + 0x10]
008C5A21  E8 3A 7C C3 FF                  call 0x1404fd660
008C5A26  CC                              int3
008C5A27  41 F6 C4 08                     test r12b, 8
008C5A2B  0F 85 B7 03 00 00               jne 0x1408c5de8
008C5A31  48 8D 0D 78 48 FF FF            lea rcx, [rip - 0xb788]
008C5A38  48 39 88 98 00 00 00            cmp qword ptr [rax + 0x98], rcx
008C5A3F  0F 85 A3 03 00 00               jne 0x1408c5de8
008C5A45  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008C5A4E  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
008C5A55  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
008C5A5A  48 3B C8                        cmp rcx, rax
008C5A5D  74 0F                           je 0x1408c5a6e
008C5A5F  48 8D 55 50                     lea rdx, [rbp + 0x50]
008C5A63  48 8B C8                        mov rcx, rax
008C5A66  E8 95 0D 95 FF                  call 0x140216800
008C5A6B  41 B6 01                        mov r14b, 1
008C5A6E  4C 8B 4D B0                     mov r9, qword ptr [rbp - 0x50]
008C5A72  48 8D 95 20 01 00 00            lea rdx, [rbp + 0x120]
008C5A79  44 8B 44 24 44                  mov r8d, dword ptr [rsp + 0x44]
008C5A7E  48 8D 8D 80 00 00 00            lea rcx, [rbp + 0x80]
008C5A85  49 83 C1 4C                     add r9, 0x4c
008C5A89  E8 32 10 00 00                  call 0x1408c6ac0
008C5A8E  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
008C5A93  48 8D 44 24 44                  lea rax, [rsp + 0x44]
008C5A98  44 0F B6 8D 98 02 00 00         movzx r9d, byte ptr [rbp + 0x298]
008C5AA0  4C 8D AD 80 00 00 00            lea r13, [rbp + 0x80]
008C5AA7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008C5AAC  4C 8D 85 80 00 00 00            lea r8, [rbp + 0x80]
008C5AB3  48 8B D3                        mov rdx, rbx
008C5AB6  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
008C5ABA  B9 02 00 00 00                  mov ecx, 2
008C5ABF  4C 89 6D B8                     mov qword ptr [rbp - 0x48], r13
008C5AC3  E8 88 97 FA FF                  call 0x14086f250
008C5AC8  89 44 24 4C                     mov dword ptr [rsp + 0x4c], eax
008C5ACC  44 8B E0                        mov r12d, eax
008C5ACF  85 C0                           test eax, eax
008C5AD1  0F 89 23 F8 FF FF               jns 0x1408c52fa
008C5AD7  E9 54 F8 FF FF                  jmp 0x1408c5330
008C5ADC  48 8B CB                        mov rcx, rbx
008C5ADF  E8 9C 43 A8 FF                  call 0x140349e80
008C5AE4  E9 7B FC FF FF                  jmp 0x1408c5764
008C5AE9  48 8B CF                        mov rcx, rdi
008C5AEC  E8 8F 43 A8 FF                  call 0x140349e80
008C5AF1  E9 88 FC FF FF                  jmp 0x1408c577e
008C5AF6  40 84 FF                        test dil, dil
008C5AF9  0F 85 46 F5 FF FF               jne 0x1408c5045
008C5AFF  48 8B 1D AA 0F 70 00            mov rbx, qword ptr [rip + 0x700faa]
008C5B06  48 89 5C 24 60                  mov qword ptr [rsp + 0x60], rbx
008C5B0B  E9 35 F5 FF FF                  jmp 0x1408c5045
008C5B10  49 8D 79 D0                     lea rdi, [r9 - 0x30]
008C5B14  4C 89 7C 24 70                  mov qword ptr [rsp + 0x70], r15
008C5B19  48 8B CF                        mov rcx, rdi
008C5B1C  BA 01 00 00 00                  mov edx, 1
008C5B21  41 B8 4F 62 48 6E               mov r8d, 0x6e48624f
008C5B27  BB FF FF 1F 00                  mov ebx, 0x1fffff
008C5B2C  45 8B E7                        mov r12d, r15d
008C5B2F  E8 4C AC 94 FF                  call 0x140210780
008C5B34  48 8B CF                        mov rcx, rdi
008C5B37  E8 74 B0 B6 FF                  call 0x140430bb0
008C5B3C  4C 8B 74 24 58                  mov r14, qword ptr [rsp + 0x58]
008C5B41  E9 96 F6 FF FF                  jmp 0x1408c51dc
008C5B46  41 8B F4                        mov esi, r12d
008C5B49  E9 0A F7 FF FF                  jmp 0x1408c5258
008C5B4E  49 8B 4F 10                     mov rcx, qword ptr [r15 + 0x10]
008C5B52  BA 00 08 00 00                  mov edx, 0x800
008C5B57  E8 D8 7A 08 00                  call 0x14094d634
008C5B5C  48 8B C8                        mov rcx, rax
008C5B5F  48 85 C0                        test rax, rax
008C5B62  74 2B                           je 0x1408c5b8f
008C5B64  33 C0                           xor eax, eax
008C5B66  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
008C5B6B  0F 84 1E 02 00 00               je 0x1408c5d8f
008C5B71  48 8B D1                        mov rdx, rcx
008C5B74  41 B8 00 08 00 00               mov r8d, 0x800
008C5B7A  49 8B 4F 10                     mov rcx, qword ptr [r15 + 0x10]
008C5B7E  E8 8D 58 FA FF                  call 0x14086b410
008C5B83  48 8B 0F                        mov rcx, qword ptr [rdi]
008C5B86  48 85 C9                        test rcx, rcx
008C5B89  0F 85 7D FC FF FF               jne 0x1408c580c
008C5B8F  48 89 74 24 68                  mov qword ptr [rsp + 0x68], rsi
008C5B94  83 E6 FC                        and esi, 0xfffffffc
008C5B97  41 83 7F 04 00                  cmp dword ptr [r15 + 4], 0
008C5B9C  89 74 24 68                     mov dword ptr [rsp + 0x68], esi
008C5BA0  74 17                           je 0x1408c5bb9
008C5BA2  48 8B 54 24 68                  mov rdx, qword ptr [rsp + 0x68]
008C5BA7  49 8B CF                        mov rcx, r15
008C5BAA  E8 A5 58 FA FF                  call 0x14086b454
008C5BAF  48 85 C0                        test rax, rax
008C5BB2  74 05                           je 0x1408c5bb9
008C5BB4  33 C9                           xor ecx, ecx
008C5BB6  48 89 08                        mov qword ptr [rax], rcx
008C5BB9  33 C0                           xor eax, eax
008C5BBB  49 89 46 08                     mov qword ptr [r14 + 8], rax
008C5BBF  45 0F B6 67 2C                  movzx r12d, byte ptr [r15 + 0x2c]
008C5BC4  41 80 E4 01                     and r12b, 1
008C5BC8  75 08                           jne 0x1408c5bd2
008C5BCA  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
008C5BD2  8B F8                           mov edi, eax
008C5BD4  45 33 C0                        xor r8d, r8d
008C5BD7  48 FF C7                        inc rdi
008C5BDA  33 D2                           xor edx, edx
008C5BDC  48 C1 E7 06                     shl rdi, 6
008C5BE0  49 03 FF                        add rdi, r15
008C5BE3  48 8B CF                        mov rcx, rdi
008C5BE6  E8 45 A6 94 FF                  call 0x140210230
008C5BEB  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
008C5BF1  48 8B F0                        mov rsi, rax
008C5BF4  73 0E                           jae 0x1408c5c04
008C5BF6  4C 8B C7                        mov r8, rdi
008C5BF9  48 8B D0                        mov rdx, rax
008C5BFC  48 8B CF                        mov rcx, rdi
008C5BFF  E8 8C A0 94 FF                  call 0x14020fc90
008C5C04  48 85 F6                        test rsi, rsi
008C5C07  74 04                           je 0x1408c5c0d
008C5C09  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
008C5C0D  45 84 E4                        test r12b, r12b
008C5C10  0F 85 9E 00 00 00               jne 0x1408c5cb4
008C5C16  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
008C5C1A  49 89 46 08                     mov qword ptr [r14 + 8], rax
008C5C1E  48 85 C0                        test rax, rax
008C5C21  75 04                           jne 0x1408c5c27
008C5C23  4C 89 77 10                     mov qword ptr [rdi + 0x10], r14
008C5C27  4C 89 77 08                     mov qword ptr [rdi + 8], r14
008C5C2B  FF 4F 18                        dec dword ptr [rdi + 0x18]
008C5C2E  F0 48 0F C1 1F                  lock xadd qword ptr [rdi], rbx
008C5C33  80 E3 06                        and bl, 6
008C5C36  80 FB 02                        cmp bl, 2
008C5C39  0F 84 63 01 00 00               je 0x1408c5da2
008C5C3F  48 8B CF                        mov rcx, rdi
008C5C42  E8 B9 B9 A1 FF                  call 0x1402e1600
008C5C47  33 FF                           xor edi, edi
008C5C49  8B F7                           mov esi, edi
008C5C4B  48 8B 5D A0                     mov rbx, qword ptr [rbp - 0x60]
008C5C4F  E9 F8 F8 FF FF                  jmp 0x1408c554c
008C5C54  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008C5C5D  4C 3B B0 B8 00 00 00            cmp r14, qword ptr [rax + 0xb8]
008C5C64  0F 85 B8 FB FF FF               jne 0x1408c5822
008C5C6A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008C5C73  48 3B 98 B8 00 00 00            cmp rbx, qword ptr [rax + 0xb8]
008C5C7A  0F 84 12 F4 FF FF               je 0x1408c5092
008C5C80  B8 22 00 00 C0                  mov eax, 0xc0000022
008C5C85  E9 13 FA FF FF                  jmp 0x1408c569d
008C5C8A  8B CF                           mov ecx, edi
008C5C8C  E9 9B F7 FF FF                  jmp 0x1408c542c
008C5C91  49 8B CC                        mov rcx, r12
008C5C94  4C 8B C7                        mov r8, rdi
008C5C97  E8 D4 62 B5 FF                  call 0x14041bf70
008C5C9C  48 85 C0                        test rax, rax
008C5C9F  74 03                           je 0x1408c5ca4
008C5CA1  4C 8B 00                        mov r8, qword ptr [rax]
008C5CA4  48 8B D6                        mov rdx, rsi
008C5CA7  49 8B CD                        mov rcx, r13
008C5CAA  E8 E1 92 05 00                  call 0x14091ef90
008C5CAF  E9 BF F8 FF FF                  jmp 0x1408c5573
008C5CB4  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
008C5CB8  48 85 C0                        test rax, rax
008C5CBB  0F 84 65 02 00 00               je 0x1408c5f26
008C5CC1  4C 89 70 08                     mov qword ptr [rax + 8], r14
008C5CC5  4C 89 77 10                     mov qword ptr [rdi + 0x10], r14
008C5CC9  E9 5D FF FF FF                  jmp 0x1408c5c2b
008C5CCE  41 80 7D 0A 00                  cmp byte ptr [r13 + 0xa], 0
008C5CD3  89 74 24 48                     mov dword ptr [rsp + 0x48], esi
008C5CD7  0F 84 B3 F6 FF FF               je 0x1408c5390
008C5CDD  49 8B 45 48                     mov rax, qword ptr [r13 + 0x48]
008C5CE1  41 83 CE 04                     or r14d, 4
008C5CE5  44 89 74 24 48                  mov dword ptr [rsp + 0x48], r14d
008C5CEA  8B 40 1C                        mov eax, dword ptr [rax + 0x1c]
008C5CED  89 44 24 70                     mov dword ptr [rsp + 0x70], eax
008C5CF1  E9 9A F6 FF FF                  jmp 0x1408c5390
008C5CF6  E8 B5 41 A8 FF                  call 0x140349eb0
008C5CFB  E9 DA F8 FF FF                  jmp 0x1408c55da
008C5D00  E8 AB 41 A8 FF                  call 0x140349eb0
008C5D05  E9 F1 F8 FF FF                  jmp 0x1408c55fb
008C5D0A  48 8B CF                        mov rcx, rdi
008C5D0D  E8 BE 00 9A FF                  call 0x140265dd0
008C5D12  E9 BF F7 FF FF                  jmp 0x1408c54d6
008C5D17  E8 94 41 A8 FF                  call 0x140349eb0
008C5D1C  E9 07 FA FF FF                  jmp 0x1408c5728
008C5D21  45 85 E4                        test r12d, r12d
008C5D24  78 17                           js 0x1408c5d3d
008C5D26  44 89 64 24 4C                  mov dword ptr [rsp + 0x4c], r12d
008C5D2B  40 84 F6                        test sil, sil
008C5D2E  0F 84 89 FC FF FF               je 0x1408c59bd
008C5D34  8B 7C 24 44                     mov edi, dword ptr [rsp + 0x44]
008C5D38  E9 71 F6 FF FF                  jmp 0x1408c53ae
008C5D3D  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
008C5D42  48 8B 55 A8                     mov rdx, qword ptr [rbp - 0x58]
008C5D46  48 8B CB                        mov rcx, rbx
008C5D49  E8 92 D5 F9 FF                  call 0x1408632e0
008C5D4E  4D 85 ED                        test r13, r13
008C5D51  74 08                           je 0x1408c5d5b
008C5D53  49 8B CD                        mov rcx, r13
008C5D56  E8 15 02 00 00                  call 0x1408c5f70
008C5D5B  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
008C5D60  48 81 C1 E8 01 00 00            add rcx, 0x1e8
008C5D67  E8 14 41 A8 FF                  call 0x140349e80
008C5D6C  48 8D 8B E8 01 00 00            lea rcx, [rbx + 0x1e8]
008C5D73  E8 08 41 A8 FF                  call 0x140349e80
008C5D78  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
008C5D7D  BA 4F 62 48 6E                  mov edx, 0x6e48624f
008C5D82  E8 59 1B A3 FF                  call 0x1402f78e0
008C5D87  41 8B C4                        mov eax, r12d
008C5D8A  E9 0E F9 FF FF                  jmp 0x1408c569d
008C5D8F  F0 41 FF 47 04                  lock inc dword ptr [r15 + 4]
008C5D94  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
008C5D99  4A 89 04 E1                     mov qword ptr [rcx + r12*8], rax
008C5D9D  E9 7A F7 FF FF                  jmp 0x1408c551c
008C5DA2  48 8B CF                        mov rcx, rdi
008C5DA5  E8 26 00 9A FF                  call 0x140265dd0
008C5DAA  E9 90 FE FF FF                  jmp 0x1408c5c3f
008C5DAF  45 85 F6                        test r14d, r14d
008C5DB2  0F 88 E2 F8 FF FF               js 0x1408c569a
008C5DB8  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
008C5DBC  4D 8B C7                        mov r8, r15
008C5DBF  45 8B 8D D0 01 00 00            mov r9d, dword ptr [r13 + 0x1d0]
008C5DC6  48 8B D6                        mov rdx, rsi
008C5DC9  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
008C5DCD  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
008C5DD2  41 8B 84 24 D0 01 00 00         mov eax, dword ptr [r12 + 0x1d0]
008C5DDA  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
008C5DDE  E8 79 0E 19 00                  call 0x140a56c5c
008C5DE3  E9 B2 F8 FF FF                  jmp 0x1408c569a
008C5DE8  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
008C5DED  41 BC 22 00 00 C0               mov r12d, 0xc0000022
008C5DF3  44 89 64 24 4C                  mov dword ptr [rsp + 0x4c], r12d
008C5DF8  E9 47 F5 FF FF                  jmp 0x1408c5344
008C5DFD  8B 45 98                        mov eax, dword ptr [rbp - 0x68]
008C5E00  49 8D 4F 38                     lea rcx, [r15 + 0x38]
008C5E04  45 33 C0                        xor r8d, r8d
008C5E07  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
008C5E0B  33 D2                           xor edx, edx
008C5E0D  41 B5 01                        mov r13b, 1
008C5E10  4C 8D 60 01                     lea r12, [rax + 1]
008C5E14  49 C1 E4 06                     shl r12, 6
008C5E18  4D 03 E7                        add r12, r15
008C5E1B  E8 10 A4 94 FF                  call 0x140210230
008C5E20  F0 49 0F BA 6F 38 00            lock bts qword ptr [r15 + 0x38], 0
008C5E27  4C 8B F0                        mov r14, rax
008C5E2A  73 10                           jae 0x1408c5e3c
008C5E2C  4D 8D 47 38                     lea r8, [r15 + 0x38]
008C5E30  48 8B D0                        mov rdx, rax
008C5E33  49 8D 4F 38                     lea rcx, [r15 + 0x38]
008C5E37  E8 54 9E 94 FF                  call 0x14020fc90
008C5E3C  4D 85 F6                        test r14, r14
008C5E3F  74 04                           je 0x1408c5e45
008C5E41  45 88 6E 0A                     mov byte ptr [r14 + 0xa], r13b
008C5E45  8B 45 D8                        mov eax, dword ptr [rbp - 0x28]
008C5E48  41 3B 07                        cmp eax, dword ptr [r15]
008C5E4B  75 0F                           jne 0x1408c5e5c
008C5E4D  49 8B D4                        mov rdx, r12
008C5E50  49 8B CF                        mov rcx, r15
008C5E53  E8 A4 74 08 00                  call 0x14094d2fc
008C5E58  44 0F B6 E8                     movzx r13d, al
008C5E5C  48 8B D3                        mov rdx, rbx
008C5E5F  F0 49 0F C1 57 38               lock xadd qword ptr [r15 + 0x38], rdx
008C5E65  80 E2 06                        and dl, 6
008C5E68  80 FA 02                        cmp dl, 2
008C5E6B  0F 84 D4 00 00 00               je 0x1408c5f45
008C5E71  49 8D 4F 38                     lea rcx, [r15 + 0x38]
008C5E75  E8 86 B7 A1 FF                  call 0x1402e1600
008C5E7A  33 FF                           xor edi, edi
008C5E7C  45 84 ED                        test r13b, r13b
008C5E7F  0F 84 C6 FD FF FF               je 0x1408c5c4b
008C5E85  44 8B 64 24 68                  mov r12d, dword ptr [rsp + 0x68]
008C5E8A  8B 44 24 78                     mov eax, dword ptr [rsp + 0x78]
008C5E8E  E9 B0 F5 FF FF                  jmp 0x1408c5443
008C5E93  8B 85 90 02 00 00               mov eax, dword ptr [rbp + 0x290]
008C5E99  4C 8B 64 24 50                  mov r12, qword ptr [rsp + 0x50]
008C5E9E  A8 01                           test al, 1
008C5EA0  0F 84 89 00 00 00               je 0x1408c5f2f
008C5EA6  48 8D 55 50                     lea rdx, [rbp + 0x50]
008C5EAA  49 8B CC                        mov rcx, r12
008C5EAD  E8 4E 09 95 FF                  call 0x140216800
008C5EB2  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
008C5EB6  E8 B5 29 FA FF                  call 0x140868870
008C5EBB  33 D2                           xor edx, edx
008C5EBD  48 8D 4D 50                     lea rcx, [rbp + 0x50]
008C5EC1  E8 6A 1E 95 FF                  call 0x140217d30
008C5EC6  49 8D 8C 24 E8 01 00 00         lea rcx, [r12 + 0x1e8]
008C5ECE  E8 AD 3F A8 FF                  call 0x140349e80
008C5ED3  BA 4F 62 48 6E                  mov edx, 0x6e48624f
008C5ED8  49 8B CE                        mov rcx, r14
008C5EDB  E8 00 1A A3 FF                  call 0x1402f78e0
008C5EE0  8B C7                           mov eax, edi
008C5EE2  E9 B6 F7 FF FF                  jmp 0x1408c569d
008C5EE7  4D 85 ED                        test r13, r13
008C5EEA  75 4A                           jne 0x1408c5f36
008C5EEC  48 8B D7                        mov rdx, rdi
008C5EEF  B9 7C 00 00 00                  mov ecx, 0x7c
008C5EF4  E8 D7 E8 03 00                  call 0x1409047d0
008C5EF9  4C 8B 64 24 60                  mov r12, qword ptr [rsp + 0x60]
008C5EFE  84 C0                           test al, al
008C5F00  0F 84 7C F6 FF FF               je 0x1408c5582
008C5F06  4C 8B 44 24 50                  mov r8, qword ptr [rsp + 0x50]
008C5F0B  4D 8B CC                        mov r9, r12
008C5F0E  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
008C5F12  48 8B D6                        mov rdx, rsi
008C5F15  E8 3E B5 1F 00                  call 0x140ac1458
008C5F1A  E9 63 F6 FF FF                  jmp 0x1408c5582
008C5F1F  B9 03 00 00 00                  mov ecx, 3
008C5F24  CD 29                           int 0x29
008C5F26  4C 89 77 08                     mov qword ptr [rdi + 8], r14
008C5F2A  E9 96 FD FF FF                  jmp 0x1408c5cc5
008C5F2F  BF 0D 00 00 C0                  mov edi, 0xc000000d
008C5F34  EB 90                           jmp 0x1408c5ec6
008C5F36  49 8B 55 20                     mov rdx, qword ptr [r13 + 0x20]
008C5F3A  48 85 D2                        test rdx, rdx
008C5F3D  75 B0                           jne 0x1408c5eef
008C5F3F  49 8B 55 30                     mov rdx, qword ptr [r13 + 0x30]
008C5F43  EB AA                           jmp 0x1408c5eef
008C5F45  49 8D 4F 38                     lea rcx, [r15 + 0x38]
008C5F49  E8 82 FE 99 FF                  call 0x140265dd0
008C5F4E  E9 1E FF FF FF                  jmp 0x1408c5e71
008C5F53  48 8B 5D A0                     mov rbx, qword ptr [rbp - 0x60]
008C5F57  E9 FD F5 FF FF                  jmp 0x1408c5559
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObDuplicateObject(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6, unsigned __int8 a7, unsigned __int8 a8)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m1D8;
    unsigned __int64 v_stack_m1E8;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m228;
    unsigned int v_stack_m22C;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned int v_stack_m23C;
    unsigned int v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned int v_stack_m25C;
    unsigned int v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned int v_stack_m274;
    unsigned __int64 v_stack_m278;
    unsigned int v_stack_m280;
    unsigned __int64 v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m2B0;
    unsigned __int64 v_stack_m2B8;
    unsigned int v_stack_m2C0;
    unsigned __int64 v_stack_m2C8;
    unsigned __int64 v_stack_m2D0;
    unsigned __int64 v_stack_m2D8;
    unsigned int v_stack_m2E0;
    unsigned int v_stack_m2E4;
    unsigned __int64 v_stack_m2E8;
    unsigned __int64 v_stack_m2F8;
    unsigned __int64 v_stack_m300;
    unsigned __int64 v_stack_m308;
    unsigned int v_stack_m30C;
    unsigned int v_stack_m310;
    unsigned int v_stack_m314;
    unsigned __int8 v_stack_m318;
    unsigned __int64 v_stack_m328;
    unsigned int v_stack_m330;
    unsigned __int8 v_stack_m338;
    unsigned int v_stack_m358;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p40;
    unsigned int v_stack_p44;
    unsigned int v_stack_p48;
    unsigned int v_stack_p4C;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned int v_stack_p78;

    v_rsp = (v_rsp) - (792);
    result = (*(unsigned __int64 *)(v_rip + 5527421)) ^ (v_rsp);
    v_stack_m58 = result;
    v_stack_m2D8 = a2;
    v_stack_m308 = a1;
    a2 = 0;
    v_stack_m2F8 = a3;
    v_stack_m298 = a4;
    v_stack_m208 = v_xmm0;
    v_stack_m1F8 = v_xmm0;
    v_stack_m1E8 = v_xmm0;
    result = memset(v_stack_m138, a2, 224, a4);
    a2 = 0;
    result = memset(v_stack_m1D8, a2, 160, a4);
    v_r15 = 0;
    v_stack_m314 = 0;
    v_stack_m2D0 = v_xmm0;
    if (condition_is_below) goto loc_008C5AF6;
loc_008C5045:
    v_stack_m310 = (unsigned int)((unsigned int)(a6));
    if (a4 != 0) {
        *(unsigned __int64 *)(a4) = 0;
    }
    if (((a7) & (2)) == 0) goto loc_008C58AE;
loc_008C506A:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 368))) & (1));
    if (a3 == 0) goto loc_008C581A;
    if ((unsigned __int8)(result) != 0) goto loc_008C5C54;
    if (((*(unsigned __int8 *)(a3 + 368)) & (1)) != 0) goto loc_008C5C54;
loc_008C5092:
    result = (*(unsigned __int64 *)(a1 + 488)) & (-2);
    if (condition_is_not_equal) goto loc_008C5754;
loc_008C50B2:
    if (*(unsigned __int64 *)(a1 + 768) == 0) goto loc_008C5ADC;
    v_stack_m300 = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (sign_flag) goto loc_008C5859;
loc_008C50DF:
    if ((((unsigned int)(v_stack_m2D8)) & (0x3FCULL)) == 0) goto loc_008C58E7;
    result = ExpLookupHandleTableEntry(*(unsigned __int64 *)(a1 + 768), v_stack_m2D8, 160, *(unsigned __int64 *)(gs_base + (0 + 392)));
    if (result == 0) goto loc_008C58E7;
loc_008C5110:
    if ((((unsigned __int8)(*(unsigned __int64 *)(result))) & (1)) == 0) goto loc_008C573B;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result))) & (1)) != 0) goto loc_008C5110;
    result = ExGetHandlePointer(result, v_stack_m2D8, *(unsigned __int64 *)(result), *(unsigned __int64 *)(gs_base + (0 + 392)));
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 8))) & (0x1FFFFFFULL));
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 768) + 4)) == 0) goto loc_008C5162;
    result = ExpGetHandleExtraInfo(*(unsigned __int64 *)(a1 + 768), v_stack_m2D8, *(unsigned __int64 *)(result), *(unsigned __int64 *)(gs_base + (0 + 392)));
    if (result == 0) goto loc_008C5162;
    v_stack_m2E8 = *(unsigned __int64 *)(result);
    goto loc_008C5167;
loc_008C5162:
    v_stack_m2E8 = 0;
loc_008C5167:
    a1 = ((unsigned int)(*(unsigned int *)(result))) >> (17);
    a1 = (unsigned int)((a1) & (7));
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(a1))) | (8));
    if (((*(unsigned int *)(result + 8)) & (0x2000000ULL)) == 0) { v_r12 = (unsigned int)(a1); }
    result = (1) + 1;
    if (result <= 1) goto loc_008C5A0F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 768) + 48)) != 0) {
        a2 = 0;
        result = ExfUnblockPushLock(*(unsigned __int64 *)(a1 + 768) + 48, a2, *(unsigned __int64 *)(result), *(unsigned __int64 *)(gs_base + (0 + 392)));
    }
    result = KeLeaveCriticalRegionThread(v_stack_m300, a2, *(unsigned __int64 *)(result), *(unsigned __int64 *)(gs_base + (0 + 392)));
    result = ObpTraceObjectReferenceIfActive(result, 1, (unsigned int)(0x6E48624FULL), *(unsigned __int64 *)(gs_base + (0 + 392)));
loc_008C51D7:
    v_stack_m300 = result + 48;
loc_008C51DC:
    if ((((unsigned __int8)(v_r12)) & (4)) == 0) {
        v_stack_m2E8 = 0;
    }
    if (v_stack_m2F8 == 0) goto loc_008C5E93;
    result = (*(unsigned __int64 *)(v_stack_m2F8 + 488)) & (-2);
    if (condition_is_not_equal) goto loc_008C576E;
loc_008C5218:
    if (*(unsigned __int64 *)(v_stack_m2F8 + 768) == 0) goto loc_008C5AE9;
    if ((*(unsigned __int64 *)(v_stack_m2F8 + 768)) == (*(unsigned __int64 *)(v_rip + 6595465))) goto loc_008C59C6;
    v_stack_m318 = 0;
loc_008C523A:
    v_r13 = (unsigned int)(a5);
    if ((((unsigned __int8)((unsigned int)(a7))) & (2)) != 0) { v_r13 = (unsigned int)(v_rbx); }
    if ((((unsigned __int8)((unsigned int)(a7))) & (4)) != 0) goto loc_008C5B46;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r12))) & (12));
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m310)) | ((unsigned int)(result)));
loc_008C5258:
    v_stack_m310 = (unsigned int)(v_rsi);
    v_rsi = (unsigned int)((v_rsi) | (8));
    v_stack_m2B0 = result + 48 - 48;
    if ((((unsigned __int8)((unsigned int)(a7))) & (8)) == 0) { v_rsi = v_stack_m310; }
    result = (result + 48 - 48) >> (8);
    a1 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(result + 48 - 48 + 24));
    a1 = (a1) ^ (*(unsigned __int8 *)(v_rip + 7347141));
    v_stack_m2A8 = *(unsigned __int64 *)(v_rip + 7349615 + a1 * 8);
    if ((((unsigned int)(v_r13)) & (0xF0000000ULL)) == 0) goto loc_008C52D3;
    if (sign_flag) {
        v_r13 = (unsigned int)((v_r13) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7349615 + a1 * 8) + 76)));
    }
    if (!(condition_is_above_or_equal)) {
        v_r13 = (unsigned int)((v_r13) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7349615 + a1 * 8) + 80)));
    }
    if (!(condition_is_above_or_equal)) {
        v_r13 = (unsigned int)((v_r13) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7349615 + a1 * 8) + 84)));
    }
    if (!(condition_is_above_or_equal)) {
        v_r13 = (unsigned int)((v_r13) | (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7349615 + a1 * 8) + 88)));
    }
    v_r13 = (unsigned int)((v_r13) & (0xFFFFFFFULL));
loc_008C52D3:
    v_r14 = 0;
    v_rbx = (unsigned int)(~(v_rbx));
    v_rdi = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7349615 + a1 * 8) + 92))) & ((unsigned int)(v_r13)));
    v_r13 = 0;
    v_stack_m314 = (unsigned int)(v_rdi);
    v_stack_m2A0 = 0;
    if ((((unsigned int)(v_rdi)) & ((unsigned int)(v_rbx))) != 0) goto loc_008C5A27;
loc_008C52FA:
    v_stack_m328 = 0;
    v_stack_m330 = (unsigned int)(v_rsi);
    v_stack_m338 = a8;
    result = ObpIncrementHandleCountEx(2, v_stack_m314, v_stack_m2F8, v_stack_m300);
    v_stack_m30C = (unsigned int)(result);
loc_008C5330:
    if (0 != 0) {
        a2 = 0;
        a1 = v_stack_m208;
        result = KiUnstackDetachProcess(a1, a2, v_stack_m2F8, v_stack_m300);
    }
loc_008C5344:
    result = (unsigned int)(a7);
    v_rdi = (unsigned int)(v_stack_m314);
    if ((((unsigned __int8)((unsigned int)(a7))) & (1)) != 0) {
        a2 = v_stack_m208;
        a1 = v_stack_m308;
        result = KeStackAttachProcess(a1, a2, v_stack_m2F8, v_stack_m300);
        a1 = v_stack_m2D8;
        result = NtClose(a1, a2, v_stack_m2F8, v_stack_m300);
        a2 = 0;
        a1 = v_stack_m208;
        result = KiUnstackDetachProcess(a1, a2, v_stack_m2F8, v_stack_m300);
        v_rdi = v_stack_m314;
    }
    if (sign_flag) goto loc_008C59D0;
    v_stack_m310 = (unsigned int)(v_rsi);
    if (0 != 0) goto loc_008C5CCE;
loc_008C5390:
    v_stack_m2C8 = v_stack_m2D0;
    v_stack_m2D0 = v_stack_m2D0;
    if (((*(unsigned __int8 *)(v_stack_m2A8 + 66)) & (64)) != 0) goto loc_008C590A;
loc_008C53AE:
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi))))) & (7));
    v_stack_m288 = 0;
    a1 = (a1) << (17);
    v_rdi = (unsigned int)((v_rdi) & (0x1FFFFFFULL));
    v_stack_m288 = (unsigned int)(v_rdi);
    result = (v_stack_m2B0) << (16);
    result = (result) & (0xFFFFFFFFFFF1FFFFULL);
    a1 = (a1) | (result);
    v_stack_m290 = a1;
    if ((((unsigned __int8)((unsigned int)((unsigned int)(v_rsi)))) & (8)) != 0) {
    }
    a1 = (a1) | (1);
    v_stack_m288 = (unsigned int)(v_rdi);
    v_rdi = 0;
    v_stack_m2B8 = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m290 = a1;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m2F8 + 768) + 44))) & (4)) != 0) goto loc_008C5F53;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m2F8 + 768) + 44))) & (1)) != 0) goto loc_008C5C8A;
loc_008C542C:
    v_stack_m2E0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 7423718)));
    v_stack_m2C0 = (unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420))));
loc_008C5443:
    v_stack_m280 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m2F8 + 768))));
loc_008C544C:
    if (0 >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 7423718))))) goto loc_008C5DFD;
    v_rdi = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))))))) + 1;
    v_rdi = (v_rdi) << (6);
    v_rdi = (v_rdi) + (*(unsigned __int64 *)(v_stack_m2F8 + 768));
    if ((*(unsigned __int64 *)(v_rdi + 8)) == 0) goto loc_008C5891;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rdi, a2, a3, v_stack_m300);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rdi;
        a2 = result;
        a1 = v_rdi;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, v_stack_m300);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (*(unsigned __int64 *)(v_rdi + 8) == 0) goto loc_008C54C4;
    *(unsigned __int64 *)(v_rdi + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 8) + 8);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 8) + 8) == 0) {
        *(unsigned __int64 *)(v_rdi + 16) = 0;
    }
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 24)))) >= = (*(unsigned int *)(v_rdi + 28))) {
        *(unsigned int *)(v_rdi + 28) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rdi + 24)));
    }
    result = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_008C5D0A;
loc_008C54D6:
    result = KeAbPostRelease(v_rdi, a2, a3, v_stack_m300);
    if (*(unsigned __int64 *)(v_rdi + 8) == 0) goto loc_008C5891;
    result = (*(unsigned __int64 *)(v_rdi + 8)) & (0xFFFFFFFFFFFFF000ULL);
    a1 = (*(unsigned __int64 *)(v_rdi + 8)) - (result);
    a1 = (a1) >> (4);
    if (v_stack_m2E8 != 0) goto loc_008C57D1;
    if (v_stack_m2E4 != 0) goto loc_008C57D1;
loc_008C551C:
    result = (unsigned int)((unsigned int)(*(unsigned __int64 *)(result + 8) + a1 * 4));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2F8 + 768) + 96)) != 0) {
        a4 = 1;
        a3 = *(unsigned __int64 *)(result + 8) + a1 * 4;
        a2 = v_stack_m2B8;
        a1 = *(unsigned __int64 *)(v_stack_m2F8 + 768);
        result = ExpUpdateDebugInfo(a1, a2, a3, a4);
    }
    v_rdi = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 8) + 8) = v_stack_m288;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 8)) = v_stack_m290;
loc_008C554C:
loc_008C5559:
    result = KeLeaveCriticalRegionThread(v_stack_m2B8, a2, a3, a4);
    if (*(unsigned __int64 *)(result + 8) + a1 * 4 == 0) goto loc_008C582C;
    if (v_stack_m2A0 != 0) goto loc_008C5C91;
loc_008C5573:
    if ((((unsigned __int8)((unsigned int)(v_stack_m310))) & (4)) != 0) goto loc_008C5EE7;
loc_008C5582:
loc_008C558C:
    v_rsi = *(unsigned __int64 *)(result + 8) + a1 * 4;
    if ((unsigned __int8)(v_stack_m318) != 0) {
        v_rsi = (*(unsigned __int64 *)(result + 8) + a1 * 4) | (0xFFFFFFFF80000000ULL);
    }
    if (v_stack_m298 != 0) {
        *(unsigned __int64 *)(v_stack_m298) = v_rsi;
    }
    result = v_stack_m298;
    if (v_stack_m2A0 != 0) {
        a1 = v_stack_m2A0;
        result = SeDeleteAccessState(a1, a2, a3, a4);
    }
    result = (*(unsigned __int64 *)(v_stack_m308 + 488)) & (-2);
    if (condition_is_not_equal) goto loc_008C5CF6;
loc_008C55DA:
    result = (*(unsigned __int64 *)(v_stack_m2F8 + 488)) & (-2);
    if (condition_is_not_equal) goto loc_008C5D00;
loc_008C55FB:
    if (v_stack_m2D0 == v_stack_m2D0) goto loc_008C568C;
    v_stack_m248 = 0;
    v_stack_m238 = v_stack_m308;
    result = (v_stack_m300 - 48) >> (8);
    a1 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(v_stack_m300 - 24));
    v_stack_m23C = 0;
    v_rdi = (unsigned int)((v_rdi) & (0xFFFFFFFEULL));
    v_rdi = (unsigned int)((v_rdi) | ((unsigned int)(v_stack_m318)));
    v_stack_m260 = 2;
    a1 = (a1) ^ (*(unsigned __int8 *)(v_rip + 7346198));
    v_stack_m25C = (unsigned int)(v_rdi);
    v_stack_m258 = v_stack_m300;
    v_stack_m240 = (unsigned int)((unsigned int)(v_stack_m30C));
    v_stack_m250 = *(unsigned __int64 *)(v_rip + 7348657 + a1 * 8);
    v_stack_m308 = (unsigned int)((unsigned int)(v_stack_m314));
loc_008C5667:
    if (v_stack_m2D0 != v_stack_m2D0) goto loc_008C56C1;
    result = ObfDereferenceObjectWithTag(v_stack_m258, (unsigned int)(0x6243624FULL), v_stack_m2D0, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(0x6243624FULL), v_stack_m2D0, a4);
loc_008C568C:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 7345278)))) & (64)) != 0) goto loc_008C5DAF;
loc_008C569A:
loc_008C569D:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(0x6243624FULL), v_stack_m2D0, a4);
    v_rsp = (v_rsp) + (792);
    return result;
loc_008C56C1:
    if ((*(unsigned __int64 *)(v_stack_m2C8)) != v_stack_m2D0) goto loc_008C5F1F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2C8 + 8))) != v_stack_m2C8) goto loc_008C5F1F;
    v_stack_m2C8 = *(unsigned __int64 *)(v_stack_m2C8 + 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2C8 + 8)) = v_stack_m2D0;
    v_stack_m248 = *(unsigned __int64 *)(v_stack_m2C8 + 24);
    result = guard_dispatch_icall(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2C8 + 16) + 24) + 8), v_stack_m260, v_stack_m2D0, a4);
    result = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m2C8 + 16) + 56)) & (-2);
    if (condition_is_not_equal) goto loc_008C5D17;
loc_008C5728:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_m2C8, a2, v_stack_m2D0, a4);
    goto loc_008C5667;
loc_008C573B:
    if (v_stack_m2D0 == 0) goto loc_008C58E2;
    result = ExpBlockOnLockedHandleEntry((unsigned int)(v_stack_m30C), v_stack_m2C8, v_stack_m2D0, a4);
    goto loc_008C5110;
loc_008C5754:
    result = ExfAcquireRundownProtection(*(unsigned __int64 *)(v_stack_m2C8 + 16), v_stack_m2C8, v_stack_m2D0, a4);
    if ((unsigned __int8)(result) != 0) goto loc_008C50B2;
loc_008C5764:
    goto loc_008C569D;
loc_008C576E:
    result = ExfAcquireRundownProtection(v_stack_m2C8, v_stack_m2C8, v_stack_m2D0, a4);
    if ((unsigned __int8)(result) != 0) goto loc_008C5218;
loc_008C577E:
    result = (unsigned int)(a7);
    if ((((unsigned __int8)((unsigned int)(a7))) & (1)) != 0) {
        a2 = v_stack_m208;
        a1 = v_stack_p50;
        result = KeStackAttachProcess(a1, a2, v_stack_m2D0, a4);
        a1 = v_stack_m2D8;
        result = NtClose(a1, a2, v_stack_m2D0, a4);
        a2 = 0;
        a1 = v_stack_m208;
        result = KiUnstackDetachProcess(a1, a2, v_stack_m2D0, a4);
    }
    result = ExReleaseRundownProtection(v_stack_p50 + 488, a2, v_stack_m2D0, a4);
    result = ObfDereferenceObjectWithTag((unsigned int)(v_stack_m30C), (unsigned int)(0x6E48624FULL), v_stack_m2D0, a4);
    goto loc_008C569D;
loc_008C57D1:
    a1 = (unsigned int)(((unsigned int)(v_stack_m30C)) & (0xFFFFFC03ULL));
    v_stack_p68 = v_rsi;
    v_stack_p68 = (unsigned int)(a1);
    result = (unsigned int)(((unsigned int)(0xC000010AULL)) >> (2));
    result = ExpLookupHandleTableEntry(v_stack_m300, v_stack_p68, v_stack_m2D0, a4);
    if (result == 0) goto loc_008C5B8F;
    if (*(unsigned __int64 *)(result) == 0) goto loc_008C5B4E;
loc_008C580C:
    *(unsigned __int64 *)(*(unsigned __int64 *)(result) + (unsigned __int8)(result) * 8) = v_stack_p70;
    goto loc_008C551C;
loc_008C581A:
    if ((unsigned __int8)(v_stack_p70) == 0) goto loc_008C5092;
loc_008C5822:
    goto loc_008C569D;
loc_008C582C:
    result = ObpDecrementHandleCount(v_stack_p60, (unsigned __int8)(result), v_stack_m2D0, a4);
    result = ObfDereferenceObjectWithTag(v_stack_p58, (unsigned int)(0x6E48624FULL), v_stack_m2D0, a4);
    goto loc_008C558C;
loc_008C5859:
    if (result != -1) goto loc_008C58C0;
    v_stack_p70 = v_stack_p58;
    result = ObpTraceObjectReferenceIfActive(v_stack_p50 - 48, result + 2, (unsigned int)(0x6E48624FULL), a4);
    result = ObpIncrPointerCount(v_stack_p50 - 48, result + 2, (unsigned int)(0x6E48624FULL), a4);
    goto loc_008C51D7;
loc_008C5891:
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)(v_stack_p58))) + 1);
    result = 0;
    v_r13 = (unsigned int)((v_stack_m308) + 1);
    if (((unsigned int)(v_r12)) != v_stack_p78) { result = (unsigned int)(v_r12); }
    goto loc_008C544C;
loc_008C58AE:
    if ((((unsigned int)(v_r13)) & (0xCE00000ULL)) == 0) goto loc_008C506A;
    goto loc_008C5822;
loc_008C58C0:
    if (((unsigned int)(v_stack_p78)) == -2) goto loc_008C5B10;
    if ((unsigned __int8)(result) != 0) goto loc_008C58EF;
    v_r12 = ((unsigned int)((unsigned int)(result))) ^ (0xFFFFFFFF80000000ULL);
    goto loc_008C50DF;
loc_008C58E2:
loc_008C58E7:
    result = KeLeaveCriticalRegionThread(v_stack_p58, result + 2, (unsigned int)(0x6E48624FULL), v_stack_p58);
loc_008C58EF:
    a1 = (v_stack_p50) + (488);
    result = ExReleaseRundownProtection(a1, result + 2, (unsigned int)(0x6E48624FULL), v_stack_p58);
    goto loc_008C569D;
loc_008C590A:
    if ((*(unsigned __int64 *)(a1 + 200)) == (a1 + 200)) goto loc_008C53AE;
    result = ((unsigned int)(0x1FFFFFULL) - 48) >> (8);
    a3 = 0;
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)((unsigned int)(0x1FFFFFULL) - 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 7345413));
    a2 = (unsigned int)((0) & (0xFFFFFFFEULL));
    a2 = (unsigned int)((a2) | ((unsigned int)(v_stack_p40)));
    v_stack_m210 = v_stack_m278;
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7347921 + a2 * 8) + 96))) & ((unsigned int)(result)));
    v_stack_m228 = v_stack_p58;
    v_stack_m22C = (unsigned int)(a2);
    v_stack_m218 = 0;
    v_stack_m268 = v_stack_p60;
    v_stack_m230 = 2;
    v_stack_m220 = *(unsigned __int64 *)(v_rip + 7347921 + a2 * 8);
    v_stack_m274 = (unsigned int)(result);
    v_stack_m278 = (unsigned int)(result);
    v_stack_m270 = v_stack_p50;
    result = ObpCallPreOperationCallbacks(*(unsigned __int64 *)(v_rip + 7347921 + a2 * 8), v_stack_m230, v_stack_m2D0, v_stack_p58);
    v_stack_p4C = (unsigned int)(result);
    if (sign_flag) goto loc_008C5D21;
    if ((unsigned __int8)(v_stack_p40) != 0) goto loc_008C5D21;
    result = (unsigned int)(((unsigned int)(v_stack_m278)) | ((unsigned int)(v_rbx)));
    v_rdi = (unsigned int)((result) & ((unsigned int)(result)));
loc_008C59BD:
    v_stack_p44 = (unsigned int)(v_rdi);
    goto loc_008C53AE;
loc_008C59C6:
    v_stack_p40 = 1;
    goto loc_008C523A;
loc_008C59D0:
    if (v_r13 != 0) {
        a1 = v_r13;
        result = SeDeleteAccessState(a1, v_stack_m230, v_stack_m2D0, v_stack_p58);
    }
    result = ExReleaseRundownProtection(*(unsigned __int64 *)(v_rip + 6593762) + 488, v_stack_m230, v_stack_m2D0, v_stack_p58);
    a1 = (v_stack_p60) + (488);
    result = ExReleaseRundownProtection(a1, v_stack_m230, v_stack_m2D0, v_stack_p58);
    result = ObfDereferenceObjectWithTag(v_rbx, (unsigned int)(0x6E48624FULL), v_stack_m2D0, v_stack_p58);
    goto loc_008C569D;
loc_008C5A0F:
    a2 = 0;
    v_stack_p20 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
    result = KeBugCheckEx(a2 + 24, a2, v_stack_p40 + 48, a2 + 16);
loc_008C5A27:
    if ((((unsigned __int8)((unsigned int)((unsigned int)(result)))) & (8)) != 0) goto loc_008C5DE8;
    if ((*(unsigned __int64 *)(result + 152)) != (v_rip - 46984)) goto loc_008C5DE8;
    result = v_stack_p60;
    v_r14 = *(unsigned __int64 *)(v_rip + 6593762);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) != v_stack_p60) {
        a2 = v_stack_m208;
        a1 = v_stack_p60;
        result = KeStackAttachProcess(a1, a2, v_stack_p40 + 48, a2 + 16);
        v_r14 = 1;
    }
    a4 = (v_stack_m2A8) + (76);
    result = SeCreateAccessState(v_stack_m1D8, v_stack_m138, (unsigned int)(v_stack_p44), a4);
    v_stack_p28 = v_stack_p44;
    v_stack_p20 = (unsigned int)(v_stack_p40);
    v_stack_m2A0 = v_stack_m1D8;
    result = ObpGrantAccess(2, v_stack_p58, v_stack_m1D8, a8);
    v_stack_p4C = (unsigned int)(result);
    if (!sign_flag) goto loc_008C52FA;
    goto loc_008C5330;
loc_008C5ADC:
    result = ExReleaseRundownProtection(v_stack_p58, v_stack_p58, v_stack_m1D8, a8);
    goto loc_008C5764;
loc_008C5AE9:
    result = ExReleaseRundownProtection(v_rdi, v_stack_p58, v_stack_m1D8, a8);
    goto loc_008C577E;
loc_008C5AF6:
    if ((unsigned __int8)(v_rdi) != 0) goto loc_008C5045;
    v_stack_p60 = *(unsigned __int64 *)(v_rip + 7344042);
    goto loc_008C5045;
loc_008C5B10:
    v_stack_p70 = v_stack_p58;
    result = ObpTraceObjectReferenceIfActive(a8 - 48, 1, (unsigned int)(0x6E48624FULL), a8);
    result = ObpIncrPointerCount(a8 - 48, 1, (unsigned int)(0x6E48624FULL), a8);
    goto loc_008C51DC;
loc_008C5B46:
    goto loc_008C5258;
loc_008C5B4E:
    result = ExpAllocateTablePagedPool(*(unsigned __int64 *)(v_stack_p58 + 16), (unsigned int)(0x800ULL), (unsigned int)(0x6E48624FULL), a8);
    if (result == 0) goto loc_008C5B8F;
    result = 0;
    if (condition_is_equal) goto loc_008C5D8F;
    result = ExpFreeTablePagedPool(*(unsigned __int64 *)(v_stack_p58 + 16), 0, (unsigned int)(0x800ULL), a8);
    if (*(unsigned __int64 *)(a8 - 48) != 0) goto loc_008C580C;
loc_008C5B8F:
    v_stack_p68 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p58))));
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p58))))) & (0xFFFFFFFCULL));
    v_stack_p68 = (unsigned int)(v_rsi);
    if ((*(unsigned int *)(v_stack_p58 + 4)) == 0) goto loc_008C5BB9;
    result = ExpGetHandleExtraInfo(v_stack_p58, v_stack_p68, (unsigned int)(0x800ULL), a8);
    if (result != 0) {
        a1 = 0;
        *(unsigned __int64 *)(result) = 0;
    }
    result = 0;
    *(unsigned __int64 *)(v_stack_p58 + 8) = 0;
    v_r12 = (unsigned __int8)((*(unsigned __int8 *)(v_stack_p58 + 44)) & (1));
    if (!(condition_is_not_equal)) {
        result = *(unsigned int *)(gs_base + (0 + 420));
    }
    a3 = 0;
    v_rdi = ((unsigned int)((unsigned int)(result))) + 1;
    a2 = 0;
    v_rdi = (v_rdi) << (6);
    v_rdi = (v_rdi) + (v_stack_p58);
    result = KeAbPreAcquire(v_rdi, a2, a3, a8);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rdi;
        a2 = result;
        a1 = v_rdi;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a8);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((unsigned __int8)(v_r12) != 0) goto loc_008C5CB4;
    *(unsigned __int64 *)(v_stack_p58 + 8) = *(unsigned __int64 *)(v_rdi + 8);
    if (*(unsigned __int64 *)(v_rdi + 8) == 0) {
        *(unsigned __int64 *)(v_rdi + 16) = v_stack_p58;
    }
    *(unsigned __int64 *)(v_rdi + 8) = v_stack_p58;
loc_008C5C2B:
    v_rbx = (unsigned __int8)(((unsigned int)(0x1FFFFFULL)) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) goto loc_008C5DA2;
loc_008C5C3F:
    result = KeAbPostRelease(v_rdi, a2, a3, a8);
    v_rdi = 0;
loc_008C5C4B:
    goto loc_008C554C;
loc_008C5C54:
    if (v_stack_p58 != (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184))) goto loc_008C5822;
    if (v_stack_m2B8 == (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184))) goto loc_008C5092;
    goto loc_008C569D;
loc_008C5C8A:
    goto loc_008C542C;
loc_008C5C91:
    result = OBJECT_HEADER_TO_AUDIT_INFO(v_r12, a2, 0, a8);
    if (result != 0) {
        a3 = *(unsigned __int64 *)(result);
    }
    result = SeAuditHandleCreation(v_stack_m1D8, 0, a3, a8);
    goto loc_008C5573;
loc_008C5CB4:
    if (*(unsigned __int64 *)(v_rdi + 16) == 0) goto loc_008C5F26;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rdi + 16) + 8) = v_stack_p58;
loc_008C5CC5:
    *(unsigned __int64 *)(v_rdi + 16) = v_stack_p58;
    goto loc_008C5C2B;
loc_008C5CCE:
    v_stack_p48 = 0;
    if ((*(unsigned __int8 *)(v_stack_m1D8 + 10)) == 0) goto loc_008C5390;
    v_r14 = (unsigned int)((v_stack_p58) | (4));
    v_stack_p48 = (unsigned int)(v_r14);
    v_stack_p70 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m1D8 + 72) + 28)));
    goto loc_008C5390;
loc_008C5CF6:
    result = ExfReleaseRundownProtection(v_stack_m1D8, 0, a3, a8);
    goto loc_008C55DA;
loc_008C5D00:
    result = ExfReleaseRundownProtection(v_stack_m1D8, 0, a3, a8);
    goto loc_008C55FB;
loc_008C5D0A:
    result = ExfTryToWakePushLock(0, 0, a3, a8);
    goto loc_008C54D6;
loc_008C5D17:
    result = ExfReleaseRundownProtection(0, 0, a3, a8);
    goto loc_008C5728;
loc_008C5D21:
    if (sign_flag) goto loc_008C5D3D;
    v_stack_p4C = (unsigned int)(v_r12);
    if (0 == 0) goto loc_008C59BD;
    goto loc_008C53AE;
loc_008C5D3D:
    result = ObpDecrementHandleCount(v_stack_p60, v_stack_m2B0, a3, a8);
    if (v_stack_m1D8 != 0) {
        a1 = v_stack_m1D8;
        result = SeDeleteAccessState(a1, v_stack_m2B0, a3, a8);
    }
    a1 = (v_stack_p50) + (488);
    result = ExReleaseRundownProtection(a1, v_stack_m2B0, a3, a8);
    result = ExReleaseRundownProtection(v_stack_p60 + 488, v_stack_m2B0, a3, a8);
    result = ObfDereferenceObjectWithTag(v_stack_p58, (unsigned int)(0x6E48624FULL), a3, a8);
    goto loc_008C569D;
loc_008C5D8F:
    *(unsigned __int64 *)(v_stack_p58 + v_r12 * 8) = v_stack_p70;
    goto loc_008C551C;
loc_008C5DA2:
    result = ExfTryToWakePushLock((unsigned int)(v_stack_p44), (unsigned int)(0x6E48624FULL), a3, a8);
    goto loc_008C5C3F;
loc_008C5DAF:
    if (sign_flag) goto loc_008C569A;
    v_stack_p28 = v_stack_m2A8;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r12 + 464)));
    result = EtwTraceDuplicateHandle(v_stack_m2D8, 0, v_stack_p58, (unsigned int)(*(unsigned int *)(v_stack_m1D8 + 464)));
    goto loc_008C569A;
loc_008C5DE8:
    v_stack_p4C = (unsigned int)((unsigned int)(0xC0000022ULL));
    goto loc_008C5344;
loc_008C5DFD:
    a3 = 0;
    v_stack_p68 = (unsigned int)((unsigned int)(v_stack_m2C0));
    a2 = 0;
    v_r12 = ((unsigned int)(v_stack_m2C0) + 1) << (6);
    v_r12 = (v_r12) + (v_stack_p58);
    result = KeAbPreAcquire(v_stack_p58 + 56, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m1D8 + 464)));
    if (!(condition_is_above_or_equal)) {
        a3 = v_stack_p58 + 56;
        a2 = result;
        a1 = v_stack_p58 + 56;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m1D8 + 464)));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = (unsigned int)(v_stack_m280);
    v_r13 = 1;
    if (((unsigned int)((unsigned int)(v_stack_m280))) == (*(unsigned int *)(v_stack_p58))) {
        a2 = v_r12;
        a1 = v_stack_p58;
        result = ExpAllocateHandleTableEntrySlow(a1, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m1D8 + 464)));
        v_r13 = (unsigned __int8)(result);
    }
    a2 = (unsigned __int8)((v_stack_p58) & (6));
    if (((unsigned __int8)(a2)) == 2) goto loc_008C5F45;
loc_008C5E71:
    result = KeAbPostRelease(v_stack_p58 + 56, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m1D8 + 464)));
    v_rdi = 0;
    if ((unsigned __int8)(v_r13) == 0) goto loc_008C5C4B;
    goto loc_008C5443;
loc_008C5E93:
    if ((((unsigned __int8)((unsigned int)(a7))) & (1)) == 0) goto loc_008C5F2F;
    result = KeStackAttachProcess(v_stack_p50, v_stack_m208, a3, (unsigned int)(*(unsigned int *)(v_stack_m1D8 + 464)));
    result = NtClose(v_stack_m2D8, v_stack_m208, a3, (unsigned int)(*(unsigned int *)(v_stack_m1D8 + 464)));
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_m208, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m1D8 + 464)));
loc_008C5EC6:
    result = ExReleaseRundownProtection(v_stack_p50 + 488, a2, a3, (unsigned int)(*(unsigned int *)(v_stack_m1D8 + 464)));
    result = ObfDereferenceObjectWithTag(result, (unsigned int)(0x6E48624FULL), a3, (unsigned int)(*(unsigned int *)(v_stack_m1D8 + 464)));
    goto loc_008C569D;
loc_008C5EE7:
    if (v_r13 != 0) goto loc_008C5F36;
loc_008C5EEF:
    result = SeAuditingWithTokenForSubcategory(124, 0, a3, (unsigned int)(*(unsigned int *)(v_stack_m1D8 + 464)));
    if ((unsigned __int8)(result) == 0) goto loc_008C5582;
    result = SeAuditHandleDuplication(v_stack_m2D8, 0, v_stack_p50, v_stack_p60);
    goto loc_008C5582;
loc_008C5F1F:
loc_008C5F26:
    *(unsigned __int64 *)(v_rdi + 8) = result;
    goto loc_008C5CC5;
loc_008C5F2F:
    goto loc_008C5EC6;
loc_008C5F36:
    if (*(unsigned __int64 *)(v_r13 + 32) != 0) goto loc_008C5EEF;
    goto loc_008C5EEF;
loc_008C5F45:
    result = ExfTryToWakePushLock(v_stack_p58 + 56, *(unsigned __int64 *)(v_r13 + 48), v_stack_p50, v_stack_p60);
    goto loc_008C5E71;
loc_008C5F53:
    goto loc_008C5559;
}
```

## 5. (Beta) C Style

```c
int64_t ObDuplicateObject(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6, uint8_t Arg7, uint8_t Arg8)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m138;
    uint64_t v_stack_m1D8;
    uint64_t v_stack_m1E8;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m228;
    uint32_t v_stack_m22C;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint32_t v_stack_m23C;
    uint32_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint32_t v_stack_m25C;
    uint32_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint32_t v_stack_m274;
    uint64_t v_stack_m278;
    uint32_t v_stack_m280;
    uint64_t v_stack_m288;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m2B0;
    uint64_t v_stack_m2B8;
    uint32_t v_stack_m2C0;
    uint64_t v_stack_m2C8;
    uint64_t v_stack_m2D0;
    uint64_t v_stack_m2D8;
    uint32_t v_stack_m2E0;
    uint32_t v_stack_m2E4;
    uint64_t v_stack_m2E8;
    uint64_t v_stack_m2F8;
    uint64_t v_stack_m300;
    uint64_t v_stack_m308;
    uint32_t v_stack_m30C;
    uint32_t v_stack_m310;
    uint32_t v_stack_m314;
    uint8_t v_stack_m318;
    uint64_t v_stack_m328;
    uint32_t v_stack_m330;
    uint8_t v_stack_m338;
    uint32_t v_stack_m358;
    uint64_t v_stack_m58;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p40;
    uint32_t v_stack_p44;
    uint32_t v_stack_p48;
    uint32_t v_stack_p4C;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint32_t v_stack_p78;

    local_rsp = (local_rsp) - (792);
    result = (*(uint64_t *)(v_rip + 0x54577D)) ^ (local_rsp);
    v_stack_m58 = result;
    v_stack_m2D8 = Arg2;
    v_stack_m308 = Arg1;
    Arg2 = 0;
    v_stack_m2F8 = Arg3;
    v_stack_m298 = Arg4;
    v_stack_m208 = v_xmm0;
    v_stack_m1F8 = v_xmm0;
    v_stack_m1E8 = v_xmm0;
    result = memset(v_stack_m138, Arg2, 224, Arg4);
    Arg2 = 0;
    result = memset(v_stack_m1D8, Arg2, 160, Arg4);
    local_r15 = 0;
    v_stack_m314 = 0;
    v_stack_m2D0 = v_xmm0;
    if (condition_is_below) goto loc_008C5AF6;
loc_008C5045:
    v_stack_m310 = (uint32_t)((uint32_t)(Arg6));
    if (Arg4 != 0) {
        *(uint64_t *)(Arg4) = 0;
    }
    if (((Arg7) & (2)) == 0) goto loc_008C58AE;
loc_008C506A:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x170))) & (1));
    if (Arg3 == 0) goto loc_008C581A;
    if ((uint8_t)(result) != 0) goto loc_008C5C54;
    if (((*(uint8_t *)(Arg3 + 0x170)) & (1)) != 0) goto loc_008C5C54;
loc_008C5092:
    result = (*(uint64_t *)(arg1 + 0x1E8)) & (-2);
    if (condition_is_not_equal) goto loc_008C5754;
loc_008C50B2:
    if (*(uint64_t *)(arg1 + 0x300) == 0) goto loc_008C5ADC;
    v_stack_m300 = *(uint64_t *)(gs_base + (0 + 0x188));
    if (sign_flag) goto loc_008C5859;
loc_008C50DF:
    if ((((uint32_t)(v_stack_m2D8)) & (0x3FCULL)) == 0) goto loc_008C58E7;
    result = ExpLookupHandleTableEntry(*(uint64_t *)(arg1 + 0x300), v_stack_m2D8, 160, *(uint64_t *)(gs_base + (0 + 0x188)));
    if (result == 0) goto loc_008C58E7;
loc_008C5110:
    if ((((uint8_t)(*(uint64_t *)(result))) & (1)) == 0) goto loc_008C573B;
    if ((((uint8_t)(*(uint64_t *)(result))) & (1)) != 0) goto loc_008C5110;
    result = ExGetHandlePointer(result, v_stack_m2D8, *(uint64_t *)(result), *(uint64_t *)(gs_base + (0 + 0x188)));
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x8))) & (0x1FFFFFFULL));
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x300) + 0x4)) == 0) goto loc_008C5162;
    result = ExpGetHandleExtraInfo(*(uint64_t *)(arg1 + 0x300), v_stack_m2D8, *(uint64_t *)(result), *(uint64_t *)(gs_base + (0 + 0x188)));
    if (result == 0) goto loc_008C5162;
    v_stack_m2E8 = *(uint64_t *)(result);
    goto loc_008C5167;
loc_008C5162:
    v_stack_m2E8 = 0;
loc_008C5167:
    Arg1 = ((uint32_t)(*(uint32_t *)(result))) >> (17);
    Arg1 = (uint32_t)((Arg1) & (7));
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(Arg1))) | (8));
    if (((*(uint32_t *)(result + 0x8)) & (0x2000000ULL)) == 0) { local_r12 = (uint32_t)(Arg1); }
    result = (1) + 1;
    if (result <= 1) goto loc_008C5A0F;
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x300) + 0x30)) != 0) {
        Arg2 = 0;
        result = ExfUnblockPushLock(*(uint64_t *)(arg1 + 0x300) + 48, Arg2, *(uint64_t *)(result), *(uint64_t *)(gs_base + (0 + 0x188)));
    }
    result = KeLeaveCriticalRegionThread(v_stack_m300, Arg2, *(uint64_t *)(result), *(uint64_t *)(gs_base + (0 + 0x188)));
    result = ObpTraceObjectReferenceIfActive(result, 1, (uint32_t)(0x6E48624FULL), *(uint64_t *)(gs_base + (0 + 0x188)));
loc_008C51D7:
    v_stack_m300 = result + 48;
loc_008C51DC:
    if ((((uint8_t)(local_r12)) & (4)) == 0) {
        v_stack_m2E8 = 0;
    }
    if (v_stack_m2F8 == 0) goto loc_008C5E93;
    result = (*(uint64_t *)(v_stack_m2F8 + 0x1E8)) & (-2);
    if (condition_is_not_equal) goto loc_008C576E;
loc_008C5218:
    if (*(uint64_t *)(v_stack_m2F8 + 0x300) == 0) goto loc_008C5AE9;
    if ((*(uint64_t *)(v_stack_m2F8 + 0x300)) == (*(uint64_t *)(v_rip + 0x64A389))) goto loc_008C59C6;
    v_stack_m318 = 0;
loc_008C523A:
    local_r13 = (uint32_t)(Arg5);
    if ((((uint8_t)((uint32_t)(Arg7))) & (2)) != 0) { local_r13 = (uint32_t)(local_rbx); }
    if ((((uint8_t)((uint32_t)(Arg7))) & (4)) != 0) goto loc_008C5B46;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r12))) & (12));
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m310)) | ((uint32_t)(result)));
loc_008C5258:
    v_stack_m310 = (uint32_t)(local_rsi);
    local_rsi = (uint32_t)((local_rsi) | (8));
    v_stack_m2B0 = result + 48 - 48;
    if ((((uint8_t)((uint32_t)(Arg7))) & (8)) == 0) { local_rsi = v_stack_m310; }
    result = (result + 48 - 48) >> (8);
    Arg1 = ((uint8_t)(result)) ^ (*(uint8_t *)(result + 0x30 - 0x30 + 0x18));
    Arg1 = (Arg1) ^ (*(uint8_t *)(v_rip + 0x701BC5));
    v_stack_m2A8 = *(uint64_t *)(v_rip + 0x70256F + arg1 * 8);
    if ((((uint32_t)(local_r13)) & (0xF0000000ULL)) == 0) goto loc_008C52D3;
    if (sign_flag) {
        local_r13 = (uint32_t)((local_r13) | (*(uint32_t *)(*(uint64_t *)(v_rip + 0x70256F + arg1 * 8) + 0x4C)));
    }
    if (!(condition_is_above_or_equal)) {
        local_r13 = (uint32_t)((local_r13) | (*(uint32_t *)(*(uint64_t *)(v_rip + 0x70256F + arg1 * 8) + 0x50)));
    }
    if (!(condition_is_above_or_equal)) {
        local_r13 = (uint32_t)((local_r13) | (*(uint32_t *)(*(uint64_t *)(v_rip + 0x70256F + arg1 * 8) + 0x54)));
    }
    if (!(condition_is_above_or_equal)) {
        local_r13 = (uint32_t)((local_r13) | (*(uint32_t *)(*(uint64_t *)(v_rip + 0x70256F + arg1 * 8) + 0x58)));
    }
    local_r13 = (uint32_t)((local_r13) & (0xFFFFFFFULL));
loc_008C52D3:
    local_r14 = 0;
    local_rbx = (uint32_t)(~(local_rbx));
    local_rdi = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x70256F + arg1 * 8) + 0x5C))) & ((uint32_t)(local_r13)));
    local_r13 = 0;
    v_stack_m314 = (uint32_t)(local_rdi);
    v_stack_m2A0 = 0;
    if ((((uint32_t)(local_rdi)) & ((uint32_t)(local_rbx))) != 0) goto loc_008C5A27;
loc_008C52FA:
    v_stack_m328 = 0;
    v_stack_m330 = (uint32_t)(local_rsi);
    v_stack_m338 = Arg8;
    result = ObpIncrementHandleCountEx(2, v_stack_m314, v_stack_m2F8, v_stack_m300);
    v_stack_m30C = (uint32_t)(result);
loc_008C5330:
    if (0 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m208;
        result = KiUnstackDetachProcess(Arg1, Arg2, v_stack_m2F8, v_stack_m300);
    }
loc_008C5344:
    result = (uint32_t)(Arg7);
    local_rdi = (uint32_t)(v_stack_m314);
    if ((((uint8_t)((uint32_t)(Arg7))) & (1)) != 0) {
        Arg2 = v_stack_m208;
        Arg1 = v_stack_m308;
        result = KeStackAttachProcess(Arg1, Arg2, v_stack_m2F8, v_stack_m300);
        Arg1 = v_stack_m2D8;
        result = NtClose(Arg1, Arg2, v_stack_m2F8, v_stack_m300);
        Arg2 = 0;
        Arg1 = v_stack_m208;
        result = KiUnstackDetachProcess(Arg1, Arg2, v_stack_m2F8, v_stack_m300);
        local_rdi = v_stack_m314;
    }
    if (sign_flag) goto loc_008C59D0;
    v_stack_m310 = (uint32_t)(local_rsi);
    if (0 != 0) goto loc_008C5CCE;
loc_008C5390:
    v_stack_m2C8 = v_stack_m2D0;
    v_stack_m2D0 = v_stack_m2D0;
    if (((*(uint8_t *)(v_stack_m2A8 + 0x42)) & (64)) != 0) goto loc_008C590A;
loc_008C53AE:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi))))) & (7));
    v_stack_m288 = 0;
    Arg1 = (Arg1) << (17);
    local_rdi = (uint32_t)((local_rdi) & (0x1FFFFFFULL));
    v_stack_m288 = (uint32_t)(local_rdi);
    result = (v_stack_m2B0) << (16);
    result = (result) & (0xFFFFFFFFFFF1FFFFULL);
    Arg1 = (Arg1) | (result);
    v_stack_m290 = Arg1;
    if ((((uint8_t)((uint32_t)((uint32_t)(local_rsi)))) & (8)) != 0) {
    }
    Arg1 = (Arg1) | (1);
    v_stack_m288 = (uint32_t)(local_rdi);
    local_rdi = 0;
    v_stack_m2B8 = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m290 = Arg1;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m2F8 + 0x300) + 0x2C))) & (4)) != 0) goto loc_008C5F53;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_stack_m2F8 + 0x300) + 0x2C))) & (1)) != 0) goto loc_008C5C8A;
loc_008C542C:
    v_stack_m2E0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x7146E6)));
    v_stack_m2C0 = (uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4))));
loc_008C5443:
    v_stack_m280 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m2F8 + 0x300))));
loc_008C544C:
    if (0 >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x7146E6))))) goto loc_008C5DFD;
    local_rdi = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))))))) + 1;
    local_rdi = (local_rdi) << (6);
    local_rdi = (local_rdi) + (*(uint64_t *)(v_stack_m2F8 + 0x300));
    if ((*(uint64_t *)(local_rdi + 0x8)) == 0) goto loc_008C5891;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_rdi, Arg2, Arg3, v_stack_m300);
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rdi;
        Arg2 = result;
        Arg1 = local_rdi;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, v_stack_m300);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (*(uint64_t *)(local_rdi + 0x8) == 0) goto loc_008C54C4;
    *(uint64_t *)(local_rdi + 0x8) = *(uint64_t *)(*(uint64_t *)(local_rdi + 0x8) + 0x8);
    if (*(uint64_t *)(*(uint64_t *)(local_rdi + 0x8) + 0x8) == 0) {
        *(uint64_t *)(local_rdi + 0x10) = 0;
    }
    if (((uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x18)))) >= = (*(uint32_t *)(local_rdi + 0x1C))) {
        *(uint32_t *)(local_rdi + 0x1C) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rdi + 0x18)));
    }
    result = (uint8_t)((-1) & (6));
    if (((uint8_t)(result)) == 2) goto loc_008C5D0A;
loc_008C54D6:
    result = KeAbPostRelease(local_rdi, Arg2, Arg3, v_stack_m300);
    if (*(uint64_t *)(local_rdi + 0x8) == 0) goto loc_008C5891;
    result = (*(uint64_t *)(local_rdi + 0x8)) & (0xFFFFFFFFFFFFF000ULL);
    Arg1 = (*(uint64_t *)(local_rdi + 0x8)) - (result);
    Arg1 = (Arg1) >> (4);
    if (v_stack_m2E8 != 0) goto loc_008C57D1;
    if (v_stack_m2E4 != 0) goto loc_008C57D1;
loc_008C551C:
    result = (uint32_t)((uint32_t)(*(uint64_t *)(result + 0x8) + Arg1 * 4));
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m2F8 + 0x300) + 0x60)) != 0) {
        Arg4 = 1;
        Arg3 = *(uint64_t *)(result + 0x8) + Arg1 * 4;
        Arg2 = v_stack_m2B8;
        Arg1 = *(uint64_t *)(v_stack_m2F8 + 0x300);
        result = ExpUpdateDebugInfo(Arg1, Arg2, Arg3, Arg4);
    }
    local_rdi = 0;
    *(uint64_t *)(*(uint64_t *)(local_rdi + 0x8) + 0x8) = v_stack_m288;
    *(uint64_t *)(*(uint64_t *)(local_rdi + 0x8)) = v_stack_m290;
loc_008C554C:
loc_008C5559:
    result = KeLeaveCriticalRegionThread(v_stack_m2B8, Arg2, Arg3, Arg4);
    if (*(uint64_t *)(result + 0x8) + Arg1 * 4 == 0) goto loc_008C582C;
    if (v_stack_m2A0 != 0) goto loc_008C5C91;
loc_008C5573:
    if ((((uint8_t)((uint32_t)(v_stack_m310))) & (4)) != 0) goto loc_008C5EE7;
loc_008C5582:
loc_008C558C:
    local_rsi = *(uint64_t *)(result + 0x8) + Arg1 * 4;
    if ((uint8_t)(v_stack_m318) != 0) {
        local_rsi = (*(uint64_t *)(result + 0x8) + Arg1 * 4) | (0xFFFFFFFF80000000ULL);
    }
    if (v_stack_m298 != 0) {
        *(uint64_t *)(v_stack_m298) = local_rsi;
    }
    result = v_stack_m298;
    if (v_stack_m2A0 != 0) {
        Arg1 = v_stack_m2A0;
        result = SeDeleteAccessState(Arg1, Arg2, Arg3, Arg4);
    }
    result = (*(uint64_t *)(v_stack_m308 + 0x1E8)) & (-2);
    if (condition_is_not_equal) goto loc_008C5CF6;
loc_008C55DA:
    result = (*(uint64_t *)(v_stack_m2F8 + 0x1E8)) & (-2);
    if (condition_is_not_equal) goto loc_008C5D00;
loc_008C55FB:
    if (v_stack_m2D0 == v_stack_m2D0) goto loc_008C568C;
    v_stack_m248 = 0;
    v_stack_m238 = v_stack_m308;
    result = (v_stack_m300 - 48) >> (8);
    Arg1 = ((uint8_t)(result)) ^ (*(uint8_t *)(v_stack_m300 - 0x18));
    v_stack_m23C = 0;
    local_rdi = (uint32_t)((local_rdi) & (0xFFFFFFFEULL));
    local_rdi = (uint32_t)((local_rdi) | ((uint32_t)(v_stack_m318)));
    v_stack_m260 = 2;
    Arg1 = (Arg1) ^ (*(uint8_t *)(v_rip + 0x701816));
    v_stack_m25C = (uint32_t)(local_rdi);
    v_stack_m258 = v_stack_m300;
    v_stack_m240 = (uint32_t)((uint32_t)(v_stack_m30C));
    v_stack_m250 = *(uint64_t *)(v_rip + 0x7021B1 + arg1 * 8);
    v_stack_m308 = (uint32_t)((uint32_t)(v_stack_m314));
loc_008C5667:
    if (v_stack_m2D0 != v_stack_m2D0) goto loc_008C56C1;
    result = ObfDereferenceObjectWithTag(v_stack_m258, (uint32_t)(0x6243624FULL), v_stack_m2D0, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(0x6243624FULL), v_stack_m2D0, Arg4);
loc_008C568C:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x70147E)))) & (64)) != 0) goto loc_008C5DAF;
loc_008C569A:
loc_008C569D:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(0x6243624FULL), v_stack_m2D0, Arg4);
    local_rsp = (local_rsp) + (792);
    return result;
loc_008C56C1:
    if ((*(uint64_t *)(v_stack_m2C8)) != v_stack_m2D0) goto loc_008C5F1F;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m2C8 + 0x8))) != v_stack_m2C8) goto loc_008C5F1F;
    v_stack_m2C8 = *(uint64_t *)(v_stack_m2C8 + 0x8);
    *(uint64_t *)(*(uint64_t *)(v_stack_m2C8 + 0x8)) = v_stack_m2D0;
    v_stack_m248 = *(uint64_t *)(v_stack_m2C8 + 0x18);
    result = guard_dispatch_icall(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_m2C8 + 0x10) + 0x18) + 0x8), v_stack_m260, v_stack_m2D0, Arg4);
    result = (*(uint64_t *)(*(uint64_t *)(v_stack_m2C8 + 0x10) + 0x38)) & (-2);
    if (condition_is_not_equal) goto loc_008C5D17;
loc_008C5728:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_m2C8, Arg2, v_stack_m2D0, Arg4);
    goto loc_008C5667;
loc_008C573B:
    if (v_stack_m2D0 == 0) goto loc_008C58E2;
    result = ExpBlockOnLockedHandleEntry((uint32_t)(v_stack_m30C), v_stack_m2C8, v_stack_m2D0, Arg4);
    goto loc_008C5110;
loc_008C5754:
    result = ExfAcquireRundownProtection(*(uint64_t *)(v_stack_m2C8 + 0x10), v_stack_m2C8, v_stack_m2D0, Arg4);
    if ((uint8_t)(result) != 0) goto loc_008C50B2;
loc_008C5764:
    goto loc_008C569D;
loc_008C576E:
    result = ExfAcquireRundownProtection(v_stack_m2C8, v_stack_m2C8, v_stack_m2D0, Arg4);
    if ((uint8_t)(result) != 0) goto loc_008C5218;
loc_008C577E:
    result = (uint32_t)(Arg7);
    if ((((uint8_t)((uint32_t)(Arg7))) & (1)) != 0) {
        Arg2 = v_stack_m208;
        Arg1 = v_stack_p50;
        result = KeStackAttachProcess(Arg1, Arg2, v_stack_m2D0, Arg4);
        Arg1 = v_stack_m2D8;
        result = NtClose(Arg1, Arg2, v_stack_m2D0, Arg4);
        Arg2 = 0;
        Arg1 = v_stack_m208;
        result = KiUnstackDetachProcess(Arg1, Arg2, v_stack_m2D0, Arg4);
    }
    result = ExReleaseRundownProtection(v_stack_p50 + 488, Arg2, v_stack_m2D0, Arg4);
    result = ObfDereferenceObjectWithTag((uint32_t)(v_stack_m30C), (uint32_t)(0x6E48624FULL), v_stack_m2D0, Arg4);
    goto loc_008C569D;
loc_008C57D1:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m30C)) & (0xFFFFFC03ULL));
    v_stack_p68 = local_rsi;
    v_stack_p68 = (uint32_t)(Arg1);
    result = (uint32_t)(((uint32_t)(0xC000010AULL)) >> (2));
    result = ExpLookupHandleTableEntry(v_stack_m300, v_stack_p68, v_stack_m2D0, Arg4);
    if (result == 0) goto loc_008C5B8F;
    if (*(uint64_t *)(result) == 0) goto loc_008C5B4E;
loc_008C580C:
    *(uint64_t *)(*(uint64_t *)(result) + (uint8_t)(result) * 8) = v_stack_p70;
    goto loc_008C551C;
loc_008C581A:
    if ((uint8_t)(v_stack_p70) == 0) goto loc_008C5092;
loc_008C5822:
    goto loc_008C569D;
loc_008C582C:
    result = ObpDecrementHandleCount(v_stack_p60, (uint8_t)(result), v_stack_m2D0, Arg4);
    result = ObfDereferenceObjectWithTag(v_stack_p58, (uint32_t)(0x6E48624FULL), v_stack_m2D0, Arg4);
    goto loc_008C558C;
loc_008C5859:
    if (result != -1) goto loc_008C58C0;
    v_stack_p70 = v_stack_p58;
    result = ObpTraceObjectReferenceIfActive(v_stack_p50 - 48, result + 2, (uint32_t)(0x6E48624FULL), Arg4);
    result = ObpIncrPointerCount(v_stack_p50 - 48, result + 2, (uint32_t)(0x6E48624FULL), Arg4);
    goto loc_008C51D7;
loc_008C5891:
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)(v_stack_p58))) + 1);
    result = 0;
    local_r13 = (uint32_t)((v_stack_m308) + 1);
    if (((uint32_t)(local_r12)) != v_stack_p78) { result = (uint32_t)(local_r12); }
    goto loc_008C544C;
loc_008C58AE:
    if ((((uint32_t)(local_r13)) & (0xCE00000ULL)) == 0) goto loc_008C506A;
    goto loc_008C5822;
loc_008C58C0:
    if (((uint32_t)(v_stack_p78)) == -2) goto loc_008C5B10;
    if ((uint8_t)(result) != 0) goto loc_008C58EF;
    local_r12 = ((uint32_t)((uint32_t)(result))) ^ (0xFFFFFFFF80000000ULL);
    goto loc_008C50DF;
loc_008C58E2:
loc_008C58E7:
    result = KeLeaveCriticalRegionThread(v_stack_p58, result + 2, (uint32_t)(0x6E48624FULL), v_stack_p58);
loc_008C58EF:
    Arg1 = (v_stack_p50) + (488);
    result = ExReleaseRundownProtection(Arg1, result + 2, (uint32_t)(0x6E48624FULL), v_stack_p58);
    goto loc_008C569D;
loc_008C590A:
    if ((*(uint64_t *)(arg1 + 0xC8)) == (Arg1 + 200)) goto loc_008C53AE;
    result = ((uint32_t)(0x1FFFFFULL) - 48) >> (8);
    Arg3 = 0;
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)((uint32_t)(0x1FFFFFULL) - 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0x701505));
    Arg2 = (uint32_t)((0) & (0xFFFFFFFEULL));
    Arg2 = (uint32_t)((Arg2) | ((uint32_t)(v_stack_p40)));
    v_stack_m210 = v_stack_m278;
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x701ED1 + Arg2 * 8) + 0x60))) & ((uint32_t)(result)));
    v_stack_m228 = v_stack_p58;
    v_stack_m22C = (uint32_t)(Arg2);
    v_stack_m218 = 0;
    v_stack_m268 = v_stack_p60;
    v_stack_m230 = 2;
    v_stack_m220 = *(uint64_t *)(v_rip + 0x701ED1 + Arg2 * 8);
    v_stack_m274 = (uint32_t)(result);
    v_stack_m278 = (uint32_t)(result);
    v_stack_m270 = v_stack_p50;
    result = ObpCallPreOperationCallbacks(*(uint64_t *)(v_rip + 0x701ED1 + Arg2 * 8), v_stack_m230, v_stack_m2D0, v_stack_p58);
    v_stack_p4C = (uint32_t)(result);
    if (sign_flag) goto loc_008C5D21;
    if ((uint8_t)(v_stack_p40) != 0) goto loc_008C5D21;
    result = (uint32_t)(((uint32_t)(v_stack_m278)) | ((uint32_t)(local_rbx)));
    local_rdi = (uint32_t)((result) & ((uint32_t)(result)));
loc_008C59BD:
    v_stack_p44 = (uint32_t)(local_rdi);
    goto loc_008C53AE;
loc_008C59C6:
    v_stack_p40 = 1;
    goto loc_008C523A;
loc_008C59D0:
    if (local_r13 != 0) {
        Arg1 = local_r13;
        result = SeDeleteAccessState(Arg1, v_stack_m230, v_stack_m2D0, v_stack_p58);
    }
    result = ExReleaseRundownProtection(*(uint64_t *)(v_rip + 0x649CE2) + 488, v_stack_m230, v_stack_m2D0, v_stack_p58);
    Arg1 = (v_stack_p60) + (488);
    result = ExReleaseRundownProtection(Arg1, v_stack_m230, v_stack_m2D0, v_stack_p58);
    result = ObfDereferenceObjectWithTag(local_rbx, (uint32_t)(0x6E48624FULL), v_stack_m2D0, v_stack_p58);
    goto loc_008C569D;
loc_008C5A0F:
    Arg2 = 0;
    v_stack_p20 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
    result = KeBugCheckEx(Arg2 + 24, Arg2, v_stack_p40 + 48, Arg2 + 16);
loc_008C5A27:
    if ((((uint8_t)((uint32_t)((uint32_t)(result)))) & (8)) != 0) goto loc_008C5DE8;
    if ((*(uint64_t *)(result + 0x98)) != (v_rip - 46984)) goto loc_008C5DE8;
    result = v_stack_p60;
    local_r14 = *(uint64_t *)(v_rip + 0x649CE2);
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) != v_stack_p60) {
        Arg2 = v_stack_m208;
        Arg1 = v_stack_p60;
        result = KeStackAttachProcess(Arg1, Arg2, v_stack_p40 + 48, Arg2 + 16);
        local_r14 = 1;
    }
    Arg4 = (v_stack_m2A8) + (76);
    result = SeCreateAccessState(v_stack_m1D8, v_stack_m138, (uint32_t)(v_stack_p44), Arg4);
    v_stack_p28 = v_stack_p44;
    v_stack_p20 = (uint32_t)(v_stack_p40);
    v_stack_m2A0 = v_stack_m1D8;
    result = ObpGrantAccess(2, v_stack_p58, v_stack_m1D8, Arg8);
    v_stack_p4C = (uint32_t)(result);
    if (!sign_flag) goto loc_008C52FA;
    goto loc_008C5330;
loc_008C5ADC:
    result = ExReleaseRundownProtection(v_stack_p58, v_stack_p58, v_stack_m1D8, Arg8);
    goto loc_008C5764;
loc_008C5AE9:
    result = ExReleaseRundownProtection(local_rdi, v_stack_p58, v_stack_m1D8, Arg8);
    goto loc_008C577E;
loc_008C5AF6:
    if ((uint8_t)(local_rdi) != 0) goto loc_008C5045;
    v_stack_p60 = *(uint64_t *)(v_rip + 0x700FAA);
    goto loc_008C5045;
loc_008C5B10:
    v_stack_p70 = v_stack_p58;
    result = ObpTraceObjectReferenceIfActive(Arg8 - 48, 1, (uint32_t)(0x6E48624FULL), Arg8);
    result = ObpIncrPointerCount(Arg8 - 48, 1, (uint32_t)(0x6E48624FULL), Arg8);
    goto loc_008C51DC;
loc_008C5B46:
    goto loc_008C5258;
loc_008C5B4E:
    result = ExpAllocateTablePagedPool(*(uint64_t *)(v_stack_p58 + 0x10), (uint32_t)(0x800ULL), (uint32_t)(0x6E48624FULL), Arg8);
    if (result == 0) goto loc_008C5B8F;
    result = 0;
    if (condition_is_equal) goto loc_008C5D8F;
    result = ExpFreeTablePagedPool(*(uint64_t *)(v_stack_p58 + 0x10), 0, (uint32_t)(0x800ULL), Arg8);
    if (*(uint64_t *)(Arg8 - 0x30) != 0) goto loc_008C580C;
loc_008C5B8F:
    v_stack_p68 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p58))));
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p58))))) & (0xFFFFFFFCULL));
    v_stack_p68 = (uint32_t)(local_rsi);
    if ((*(uint32_t *)(v_stack_p58 + 0x4)) == 0) goto loc_008C5BB9;
    result = ExpGetHandleExtraInfo(v_stack_p58, v_stack_p68, (uint32_t)(0x800ULL), Arg8);
    if (result != 0) {
        Arg1 = 0;
        *(uint64_t *)(result) = 0;
    }
    result = 0;
    *(uint64_t *)(v_stack_p58 + 0x8) = 0;
    local_r12 = (uint8_t)((*(uint8_t *)(v_stack_p58 + 0x2C)) & (1));
    if (!(condition_is_not_equal)) {
        result = *(uint32_t *)(gs_base + (0 + 0x1A4));
    }
    Arg3 = 0;
    local_rdi = ((uint32_t)((uint32_t)(result))) + 1;
    Arg2 = 0;
    local_rdi = (local_rdi) << (6);
    local_rdi = (local_rdi) + (v_stack_p58);
    result = KeAbPreAcquire(local_rdi, Arg2, Arg3, Arg8);
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rdi;
        Arg2 = result;
        Arg1 = local_rdi;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg8);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((uint8_t)(local_r12) != 0) goto loc_008C5CB4;
    *(uint64_t *)(v_stack_p58 + 0x8) = *(uint64_t *)(local_rdi + 0x8);
    if (*(uint64_t *)(local_rdi + 0x8) == 0) {
        *(uint64_t *)(local_rdi + 0x10) = v_stack_p58;
    }
    *(uint64_t *)(local_rdi + 0x8) = v_stack_p58;
loc_008C5C2B:
    local_rbx = (uint8_t)(((uint32_t)(0x1FFFFFULL)) & (6));
    if (((uint8_t)(local_rbx)) == 2) goto loc_008C5DA2;
loc_008C5C3F:
    result = KeAbPostRelease(local_rdi, Arg2, Arg3, Arg8);
    local_rdi = 0;
loc_008C5C4B:
    goto loc_008C554C;
loc_008C5C54:
    if (v_stack_p58 != (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8))) goto loc_008C5822;
    if (v_stack_m2B8 == (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8))) goto loc_008C5092;
    goto loc_008C569D;
loc_008C5C8A:
    goto loc_008C542C;
loc_008C5C91:
    result = OBJECT_HEADER_TO_AUDIT_INFO(local_r12, Arg2, 0, Arg8);
    if (result != 0) {
        Arg3 = *(uint64_t *)(result);
    }
    result = SeAuditHandleCreation(v_stack_m1D8, 0, Arg3, Arg8);
    goto loc_008C5573;
loc_008C5CB4:
    if (*(uint64_t *)(local_rdi + 0x10) == 0) goto loc_008C5F26;
    *(uint64_t *)(*(uint64_t *)(local_rdi + 0x10) + 0x8) = v_stack_p58;
loc_008C5CC5:
    *(uint64_t *)(local_rdi + 0x10) = v_stack_p58;
    goto loc_008C5C2B;
loc_008C5CCE:
    v_stack_p48 = 0;
    if ((*(uint8_t *)(v_stack_m1D8 + 0xA)) == 0) goto loc_008C5390;
    local_r14 = (uint32_t)((v_stack_p58) | (4));
    v_stack_p48 = (uint32_t)(local_r14);
    v_stack_p70 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m1D8 + 0x48) + 0x1C)));
    goto loc_008C5390;
loc_008C5CF6:
    result = ExfReleaseRundownProtection(v_stack_m1D8, 0, Arg3, Arg8);
    goto loc_008C55DA;
loc_008C5D00:
    result = ExfReleaseRundownProtection(v_stack_m1D8, 0, Arg3, Arg8);
    goto loc_008C55FB;
loc_008C5D0A:
    result = ExfTryToWakePushLock(0, 0, Arg3, Arg8);
    goto loc_008C54D6;
loc_008C5D17:
    result = ExfReleaseRundownProtection(0, 0, Arg3, Arg8);
    goto loc_008C5728;
loc_008C5D21:
    if (sign_flag) goto loc_008C5D3D;
    v_stack_p4C = (uint32_t)(local_r12);
    if (0 == 0) goto loc_008C59BD;
    goto loc_008C53AE;
loc_008C5D3D:
    result = ObpDecrementHandleCount(v_stack_p60, v_stack_m2B0, Arg3, Arg8);
    if (v_stack_m1D8 != 0) {
        Arg1 = v_stack_m1D8;
        result = SeDeleteAccessState(Arg1, v_stack_m2B0, Arg3, Arg8);
    }
    Arg1 = (v_stack_p50) + (488);
    result = ExReleaseRundownProtection(Arg1, v_stack_m2B0, Arg3, Arg8);
    result = ExReleaseRundownProtection(v_stack_p60 + 488, v_stack_m2B0, Arg3, Arg8);
    result = ObfDereferenceObjectWithTag(v_stack_p58, (uint32_t)(0x6E48624FULL), Arg3, Arg8);
    goto loc_008C569D;
loc_008C5D8F:
    *(uint64_t *)(v_stack_p58 + local_r12 * 8) = v_stack_p70;
    goto loc_008C551C;
loc_008C5DA2:
    result = ExfTryToWakePushLock((uint32_t)(v_stack_p44), (uint32_t)(0x6E48624FULL), Arg3, Arg8);
    goto loc_008C5C3F;
loc_008C5DAF:
    if (sign_flag) goto loc_008C569A;
    v_stack_p28 = v_stack_m2A8;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r12 + 0x1D0)));
    result = EtwTraceDuplicateHandle(v_stack_m2D8, 0, v_stack_p58, (uint32_t)(*(uint32_t *)(v_stack_m1D8 + 0x1D0)));
    goto loc_008C569A;
loc_008C5DE8:
    v_stack_p4C = (uint32_t)((uint32_t)(0xC0000022ULL));
    goto loc_008C5344;
loc_008C5DFD:
    Arg3 = 0;
    v_stack_p68 = (uint32_t)((uint32_t)(v_stack_m2C0));
    Arg2 = 0;
    local_r12 = ((uint32_t)(v_stack_m2C0) + 1) << (6);
    local_r12 = (local_r12) + (v_stack_p58);
    result = KeAbPreAcquire(v_stack_p58 + 56, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m1D8 + 0x1D0)));
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_stack_p58 + 56;
        Arg2 = result;
        Arg1 = v_stack_p58 + 56;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m1D8 + 0x1D0)));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = (uint32_t)(v_stack_m280);
    local_r13 = 1;
    if (((uint32_t)((uint32_t)(v_stack_m280))) == (*(uint32_t *)(v_stack_p58))) {
        Arg2 = local_r12;
        Arg1 = v_stack_p58;
        result = ExpAllocateHandleTableEntrySlow(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m1D8 + 0x1D0)));
        local_r13 = (uint8_t)(result);
    }
    Arg2 = (uint8_t)((v_stack_p58) & (6));
    if (((uint8_t)(Arg2)) == 2) goto loc_008C5F45;
loc_008C5E71:
    result = KeAbPostRelease(v_stack_p58 + 56, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m1D8 + 0x1D0)));
    local_rdi = 0;
    if ((uint8_t)(local_r13) == 0) goto loc_008C5C4B;
    goto loc_008C5443;
loc_008C5E93:
    if ((((uint8_t)((uint32_t)(Arg7))) & (1)) == 0) goto loc_008C5F2F;
    result = KeStackAttachProcess(v_stack_p50, v_stack_m208, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m1D8 + 0x1D0)));
    result = NtClose(v_stack_m2D8, v_stack_m208, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m1D8 + 0x1D0)));
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_m208, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m1D8 + 0x1D0)));
loc_008C5EC6:
    result = ExReleaseRundownProtection(v_stack_p50 + 488, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m1D8 + 0x1D0)));
    result = ObfDereferenceObjectWithTag(result, (uint32_t)(0x6E48624FULL), Arg3, (uint32_t)(*(uint32_t *)(v_stack_m1D8 + 0x1D0)));
    goto loc_008C569D;
loc_008C5EE7:
    if (local_r13 != 0) goto loc_008C5F36;
loc_008C5EEF:
    result = SeAuditingWithTokenForSubcategory(124, 0, Arg3, (uint32_t)(*(uint32_t *)(v_stack_m1D8 + 0x1D0)));
    if ((uint8_t)(result) == 0) goto loc_008C5582;
    result = SeAuditHandleDuplication(v_stack_m2D8, 0, v_stack_p50, v_stack_p60);
    goto loc_008C5582;
loc_008C5F1F:
loc_008C5F26:
    *(uint64_t *)(local_rdi + 0x8) = result;
    goto loc_008C5CC5;
loc_008C5F2F:
    goto loc_008C5EC6;
loc_008C5F36:
    if (*(uint64_t *)(local_r13 + 0x20) != 0) goto loc_008C5EEF;
    goto loc_008C5EEF;
loc_008C5F45:
    result = ExfTryToWakePushLock(v_stack_p58 + 56, *(uint64_t *)(local_r13 + 0x30), v_stack_p50, v_stack_p60);
    goto loc_008C5E71;
loc_008C5F53:
    goto loc_008C5559;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x170` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008C4FA0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
