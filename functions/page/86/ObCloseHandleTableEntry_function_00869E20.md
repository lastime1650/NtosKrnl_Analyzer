# ObCloseHandleTableEntry

- RVA: `0x00869E20`–`0x0086AA3D` (길이 `3,101` bytes)
- VA: `0x0000000140869E20`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006BEBC`
- 디코드: `735`개 명령, `3,101/3,101` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **77**; 고유 호출 대상: **39**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **15**

### Outgoing calls
- `0x00869E6A` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (function, `0x00430C90`)
- `0x00869EF6` → [EtwpTraceHandle](EtwpTraceHandle_function_0086AA44.md) (function, `0x0086AA44`)
- `0x00869F24` → [ExpUpdateDebugInfo](ExpUpdateDebugInfo_function_0086B174.md) (function, `0x0086B174`)
- `0x00869F4C` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (function, `0x002A3FE0`)
- `0x00869F6E` → [ExpGetHandleExtraInfo](ExpGetHandleExtraInfo_function_0086B454.md) (function, `0x0086B454`)
- `0x00869FAD` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00869FC6` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0086A00E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0086A025` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086A042` → [SeCaptureSubjectContext](SeCaptureSubjectContext_function_0086B820.md) (function, `0x0086B820`)
- `0x0086A063` → [SepAdtCloseObjectAuditAlarm](SepAdtCloseObjectAuditAlarm_function_0086B4E8.md) (function, `0x0086B4E8`)
- `0x0086A06D` → [SeReleaseSubjectContext](SeReleaseSubjectContext_function_0086B710.md) (function, `0x0086B710`)
- `0x0086A107` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (function, `0x0044BEE0`)
- `0x0086A10F` → [PsAttachSiloToCurrentThread](../../text/44/PsAttachSiloToCurrentThread_function_004428C0.md) (function, `0x004428C0`)
- `0x0086A122` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (function, `0x00216800`)
- `0x0086A150` → [CmpCloseKeyObject](CmpCloseKeyObject_function_00863AD0.md) (function, `0x00863AD0`)
- `0x0086A162` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x0086A16C` → [PsDetachSiloFromCurrentThread](../../text/44/PsDetachSiloFromCurrentThread_function_00449AC0.md) (function, `0x00449AC0`)
- `0x0086A1AF` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x0086A1CC` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0086A1DA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0086A227` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x0086A256` → [EtwpEventWriteTemplateSessAndProv](EtwpEventWriteTemplateSessAndProv_function_00863D18.md) (function, `0x00863D18`)
- `0x0086A28A` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0086A2A6` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0086A306` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0086A314` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086A338` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0086A356` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0086A425` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0086A433` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086A457` → [IopCloseFile](IopCloseFile_function_008640C0.md) (function, `0x008640C0`)
- `0x0086A4A6` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0086A51B` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (function, `0x00216800`)
- `0x0086A54F` → [ExpWin32OkayToCloseProcedure](../90/ExpWin32OkayToCloseProcedure_function_009050A0.md) (function, `0x009050A0`)
- `0x0086A5A6` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (function, `0x002A3FE0`)
- `0x0086A5B3` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0086A5C9` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0086A5D6` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x0086A5F6` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (function, `0x002A3FE0`)
- `0x0086A604` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086A613` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x0086A642` → [ExUnlockHandleTableEntry](../94/ExUnlockHandleTableEntry_function_0094D2D0.md) (function, `0x0094D2D0`)
- `0x0086A650` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086A661` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x0086A6AE` → [KeRaiseUserException](../../text/4D/KeRaiseUserException_function_004D7750.md) (function, `0x004D7750`)
- `0x0086A6D6` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0086A714` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0086A777` → [ObpDeleteSymbolicLinkName](../A7/ObpDeleteSymbolicLinkName_function_00A7BC80.md) (function, `0x00A7BC80`)
- `0x0086A787` → [ObpLookupDirectoryEntry](../85/ObpLookupDirectoryEntry_function_0085D5B0.md) (function, `0x0085D5B0`)
- `0x0086A7EE` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0086A7FC` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086A814` → [ObpUnlockDirectory](../99/ObpUnlockDirectory_function_0099F8A0.md) (function, `0x0099F8A0`)
- `0x0086A81E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0086A82B` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0086A85A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0086A864` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (function, `0x00263D30`)
- `0x0086A872` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0086A88C` → [KeAbPostReleaseEx](../../text/26/KeAbPostReleaseEx_function_00262210.md) (function, `0x00262210`)
- `0x0086A89A` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086A8A2` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x0086A8DA` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0086A8E8` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086A90B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0086A92B` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0086A958` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0086A976` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0086A993` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (function, `0x00263D30`)
- `0x0086A9C3` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0086A9D1` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0086A9D9` → [HalPutDmaAdapter](../../text/48/HalPutDmaAdapter_function_0048E530.md) (function, `0x0048E530`)
- `0x0086A9E7` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0086A9F5` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0086AA0C` → [HalPutDmaAdapter](../../text/48/HalPutDmaAdapter_function_0048E530.md) (function, `0x0048E530`)
- `0x0086AA16` → [ObpDeleteDirectoryName](../99/ObpDeleteDirectoryName_function_0099EF94.md) (function, `0x0099EF94`)
- `0x0086AA20` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (function, `0x00263D30`)
- `0x0086AA2A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [ObpCloseHandle](ObpCloseHandle_function_008685B0.md) at `0x00868673`
- [NtClose](NtClose_function_00868870.md) at `0x00868954`
- [ExSweepHandleTable](../90/ExSweepHandleTable_function_00904D3C.md) at `0x00904E03`

### Static image references
- `0x00869E39` → RVA `0x00E0A740` (`.data`; read)
- `0x00869E82` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00869E90` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x00869ECD` → RVA `0x00FC6B10` (`ALMOSTRO`; read)
- `0x00869ED7` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x0086A05C` → RVA `0x000013A8` (`.rdata`; read)
- `0x0086A133` → RVA `0x00863AD0` (`CmpCloseKeyObject`; read)
- `0x0086A1F4` → RVA `0x00A0CEB0` (`EtwpCloseRegistrationObject`; read)
- `0x0086A219` → RVA `0x00EFF840` (`.data`; read)
- `0x0086A220` → RVA `0x00010888` (`.rdata`; read)
- `0x0086A43D` → RVA `0x008640C0` (`IopCloseFile`; read)
- `0x0086A531` → RVA `0x009050A0` (`ExpWin32OkayToCloseProcedure`; read)
- `0x0086A678` → RVA `0x00FC42C0` (`.data`; read)
- `0x0086A762` → RVA `0x00F0F658` (`.data`; read)
- `0x0086A830` → RVA `0x00F0F650` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **62**
  - `0x00869E6A` → [ExGetHandlePointer](../../text/43/ExGetHandlePointer_function_00430C90.md) (`PAGE` → `.text`)
  - `0x00869F4C` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (`PAGE` → `.text`)
  - `0x00869FAD` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00869FC6` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0086A00E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0086A025` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086A107` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (`PAGE` → `.text`)
  - `0x0086A10F` → [PsAttachSiloToCurrentThread](../../text/44/PsAttachSiloToCurrentThread_function_004428C0.md) (`PAGE` → `.text`)
  - `0x0086A122` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (`PAGE` → `.text`)
  - `0x0086A162` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x0086A16C` → [PsDetachSiloFromCurrentThread](../../text/44/PsDetachSiloFromCurrentThread_function_00449AC0.md) (`PAGE` → `.text`)
  - `0x0086A1AF` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x0086A1CC` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0086A1DA` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0086A227` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x0086A28A` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0086A2A6` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0086A306` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0086A314` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086A338` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0086A356` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0086A425` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0086A433` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086A4A6` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x0086A51B` → [KeStackAttachProcess](../../text/21/KeStackAttachProcess_function_00216800.md) (`PAGE` → `.text`)
  - `0x0086A5A6` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (`PAGE` → `.text`)
  - `0x0086A5B3` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x0086A5C9` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0086A5D6` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x0086A5F6` → [ExfUnblockPushLock](../../text/2A/ExfUnblockPushLock_function_002A3FE0.md) (`PAGE` → `.text`)
  - `0x0086A604` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086A613` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x0086A650` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086A661` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x0086A6AE` → [KeRaiseUserException](../../text/4D/KeRaiseUserException_function_004D7750.md) (`PAGE` → `.text`)
  - `0x0086A6D6` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x0086A714` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0086A7EE` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0086A7FC` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086A81E` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0086A82B` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0086A85A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0086A864` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (`PAGE` → `.text`)
  - `0x0086A872` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x0086A88C` → [KeAbPostReleaseEx](../../text/26/KeAbPostReleaseEx_function_00262210.md) (`PAGE` → `.text`)
  - `0x0086A89A` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086A8A2` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x0086A8DA` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0086A8E8` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086A90B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0086A92B` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0086A958` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0086A976` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0086A993` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (`PAGE` → `.text`)
  - `0x0086A9C3` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0086A9D1` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0086A9D9` → [HalPutDmaAdapter](../../text/48/HalPutDmaAdapter_function_0048E530.md) (`PAGE` → `.text`)
  - `0x0086A9E7` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x0086A9F5` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x0086AA0C` → [HalPutDmaAdapter](../../text/48/HalPutDmaAdapter_function_0048E530.md) (`PAGE` → `.text`)
  - `0x0086AA20` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (`PAGE` → `.text`)
  - `0x0086AA2A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00869E20  40 55                           push rbp
00869E22  53                              push rbx
00869E23  56                              push rsi
00869E24  57                              push rdi
00869E25  41 54                           push r12
00869E27  41 55                           push r13
00869E29  41 56                           push r14
00869E2B  41 57                           push r15
00869E2D  48 8D 6C 24 F8                  lea rbp, [rsp - 8]
00869E32  48 81 EC 08 01 00 00            sub rsp, 0x108
00869E39  48 8B 05 00 09 5A 00            mov rax, qword ptr [rip + 0x5a0900]
00869E40  48 33 C4                        xor rax, rsp
00869E43  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00869E47  0F 57 C0                        xorps xmm0, xmm0
00869E4A  4C 89 44 24 40                  mov qword ptr [rsp + 0x40], r8
00869E4F  4C 8B F9                        mov r15, rcx
00869E52  4D 8B F1                        mov r14, r9
00869E55  48 8B CA                        mov rcx, rdx
00869E58  4D 8B E8                        mov r13, r8
00869E5B  0F 11 45 90                     movups xmmword ptr [rbp - 0x70], xmm0
00869E5F  4C 8B E2                        mov r12, rdx
00869E62  0F 11 45 A0                     movups xmmword ptr [rbp - 0x60], xmm0
00869E66  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
00869E6A  E8 21 6E BC FF                  call 0x140430c90
00869E6F  48 8B C8                        mov rcx, rax
00869E72  48 8B F8                        mov rdi, rax
00869E75  48 C1 E9 08                     shr rcx, 8
00869E79  32 DB                           xor bl, bl
00869E7B  0F B6 D1                        movzx edx, cl
00869E7E  0F B6 48 18                     movzx ecx, byte ptr [rax + 0x18]
00869E82  48 8D 05 77 61 79 FF            lea rax, [rip - 0x869e89]
00869E89  48 33 D1                        xor rdx, rcx
00869E8C  88 5C 24 31                     mov byte ptr [rsp + 0x31], bl
00869E90  0F B6 0D B5 CF 75 00            movzx ecx, byte ptr [rip + 0x75cfb5]
00869E97  4C 8D 57 30                     lea r10, [rdi + 0x30]
00869E9B  48 33 D1                        xor rdx, rcx
00869E9E  48 8B B4 D0 00 78 FC 00         mov rsi, qword ptr [rax + rdx*8 + 0xfc7800]
00869EA6  48 83 BE A8 00 00 00 00         cmp qword ptr [rsi + 0xa8], 0
00869EAE  0F 85 4E 06 00 00               jne 0x14086a502
00869EB4  49 8B 04 24                     mov rax, qword ptr [r12]
00869EB8  0F B6 5D 78                     movzx ebx, byte ptr [rbp + 0x78]
00869EBC  48 C1 F8 11                     sar rax, 0x11
00869EC0  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00869EC5  A8 01                           test al, 1
00869EC7  0F 85 5E 07 00 00               jne 0x14086a62b
00869ECD  8B 05 3D CC 75 00               mov eax, dword ptr [rip + 0x75cc3d]
00869ED3  A8 40                           test al, 0x40
00869ED5  74 24                           je 0x140869efb
00869ED7  4C 3B 2D D2 CB 75 00            cmp r13, qword ptr [rip + 0x75cbd2]
00869EDE  49 8B D6                        mov rdx, r14
00869EE1  75 08                           jne 0x140869eeb
00869EE3  B8 00 00 00 80                  mov eax, 0x80000000
00869EE8  48 0B D0                        or rdx, rax
00869EEB  B9 21 11 00 00                  mov ecx, 0x1121
00869EF0  4C 8B CE                        mov r9, rsi
00869EF3  4D 8B C2                        mov r8, r10
00869EF6  E8 49 0B 00 00                  call 0x14086aa44
00869EFB  48 C7 C6 FF FF FF FF            mov rsi, 0xffffffffffffffff
00869F02  84 DB                           test bl, bl
00869F04  0F 85 7A 06 00 00               jne 0x14086a584
00869F0A  49 83 7F 60 00                  cmp qword ptr [r15 + 0x60], 0
00869F0F  74 18                           je 0x140869f29
00869F11  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
00869F1A  44 8D 4E 03                     lea r9d, [rsi + 3]
00869F1E  4D 8B C6                        mov r8, r14
00869F21  49 8B CF                        mov rcx, r15
00869F24  E8 4B 12 00 00                  call 0x14086b174
00869F29  49 8B 04 24                     mov rax, qword ptr [r12]
00869F2D  49 8D 4F 30                     lea rcx, [r15 + 0x30]
00869F31  48 D1 E8                        shr rax, 1
00869F34  45 33 ED                        xor r13d, r13d
00869F37  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
00869F3C  4D 89 2C 24                     mov qword ptr [r12], r13
00869F40  F0 44 09 2C 24                  lock or dword ptr [rsp], r13d
00869F45  4C 39 29                        cmp qword ptr [rcx], r13
00869F48  74 07                           je 0x140869f51
00869F4A  33 D2                           xor edx, edx
00869F4C  E8 8F A0 A3 FF                  call 0x1402a3fe0
00869F51  41 8B C6                        mov eax, r14d
00869F54  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
00869F59  83 E0 FC                        and eax, 0xfffffffc
00869F5C  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00869F60  45 39 6F 04                     cmp dword ptr [r15 + 4], r13d
00869F64  74 15                           je 0x140869f7b
00869F66  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
00869F6B  49 8B CF                        mov rcx, r15
00869F6E  E8 E1 14 00 00                  call 0x14086b454
00869F73  48 85 C0                        test rax, rax
00869F76  74 03                           je 0x140869f7b
00869F78  4C 89 28                        mov qword ptr [rax], r13
00869F7B  4D 89 6C 24 08                  mov qword ptr [r12 + 8], r13
00869F80  41 0F B6 47 2C                  movzx eax, byte ptr [r15 + 0x2c]
00869F85  24 01                           and al, 1
00869F87  88 44 24 30                     mov byte ptr [rsp + 0x30], al
00869F8B  0F 85 D4 05 00 00               jne 0x14086a565
00869F91  65 8B 04 25 A4 01 00 00         mov eax, dword ptr gs:[0x1a4]
00869F99  8B D8                           mov ebx, eax
00869F9B  45 33 C0                        xor r8d, r8d
00869F9E  48 FF C3                        inc rbx
00869FA1  33 D2                           xor edx, edx
00869FA3  48 C1 E3 06                     shl rbx, 6
00869FA7  49 03 DF                        add rbx, r15
00869FAA  48 8B CB                        mov rcx, rbx
00869FAD  E8 7E 62 9A FF                  call 0x140210230
00869FB2  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
00869FB8  4C 8B F8                        mov r15, rax
00869FBB  73 0E                           jae 0x140869fcb
00869FBD  4C 8B C3                        mov r8, rbx
00869FC0  48 8B D0                        mov rdx, rax
00869FC3  48 8B CB                        mov rcx, rbx
00869FC6  E8 C5 5C 9A FF                  call 0x14020fc90
00869FCB  4D 85 FF                        test r15, r15
00869FCE  74 05                           je 0x140869fd5
00869FD0  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
00869FD5  44 38 6C 24 30                  cmp byte ptr [rsp + 0x30], r13b
00869FDA  0F 85 08 05 00 00               jne 0x14086a4e8
00869FE0  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
00869FE4  49 89 44 24 08                  mov qword ptr [r12 + 8], rax
00869FE9  48 85 C0                        test rax, rax
00869FEC  75 04                           jne 0x140869ff2
00869FEE  4C 89 63 10                     mov qword ptr [rbx + 0x10], r12
00869FF2  4C 89 63 08                     mov qword ptr [rbx + 8], r12
00869FF6  FF 4B 18                        dec dword ptr [rbx + 0x18]
00869FF9  48 8B C6                        mov rax, rsi
00869FFC  F0 48 0F C1 03                  lock xadd qword ptr [rbx], rax
0086A001  24 06                           and al, 6
0086A003  3C 02                           cmp al, 2
0086A005  0F 84 C8 05 00 00               je 0x14086a5d3
0086A00B  48 8B CB                        mov rcx, rbx
0086A00E  E8 ED 75 A7 FF                  call 0x1402e1600
0086A013  48 8B 5C 24 68                  mov rbx, qword ptr [rsp + 0x68]
0086A018  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086A021  44 0F B7 FB                     movzx r15d, bx
0086A025  E8 C6 4F 9F FF                  call 0x14025eff0
0086A02A  F6 44 24 48 04                  test byte ptr [rsp + 0x48], 4
0086A02F  74 41                           je 0x14086a072
0086A031  0F 57 C0                        xorps xmm0, xmm0
0086A034  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
0086A039  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
0086A03E  0F 11 45 80                     movups xmmword ptr [rbp - 0x80], xmm0
0086A042  E8 D9 17 00 00                  call 0x14086b820
0086A047  49 83 E6 FC                     and r14, 0xfffffffffffffffc
0086A04B  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
0086A050  49 8B D6                        mov rdx, r14
0086A053  4C 8D 4F 30                     lea r9, [rdi + 0x30]
0086A057  4C 8D 44 24 70                  lea r8, [rsp + 0x70]
0086A05C  48 8D 0D 45 73 79 FF            lea rcx, [rip - 0x868cbb]
0086A063  E8 80 14 00 00                  call 0x14086b4e8
0086A068  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
0086A06D  E8 9E 16 00 00                  call 0x14086b710
0086A072  0F 57 C0                        xorps xmm0, xmm0
0086A075  48 8B C7                        mov rax, rdi
0086A078  48 C1 E8 08                     shr rax, 8
0086A07C  0F B6 C8                        movzx ecx, al
0086A07F  0F B6 47 18                     movzx eax, byte ptr [rdi + 0x18]
0086A083  48 33 C8                        xor rcx, rax
0086A086  0F B6 05 BF CD 75 00            movzx eax, byte ptr [rip + 0x75cdbf]
0086A08D  48 33 C8                        xor rcx, rax
0086A090  48 8D 05 69 5F 79 FF            lea rax, [rip - 0x86a097]
0086A097  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
0086A09B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0086A09F  4C 8B B4 C8 00 78 FC 00         mov r14, qword ptr [rax + rcx*8 + 0xfc7800]
0086A0A7  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0086A0AB  41 0F B6 46 42                  movzx eax, byte ptr [r14 + 0x42]
0086A0B0  A8 10                           test al, 0x10
0086A0B2  0F 85 66 02 00 00               jne 0x14086a31e
0086A0B8  0F B6 47 1B                     movzx eax, byte ptr [rdi + 0x1b]
0086A0BC  A8 08                           test al, 8
0086A0BE  0F 85 5A 02 00 00               jne 0x14086a31e
0086A0C4  F0 48 0F C1 77 08               lock xadd qword ptr [rdi + 8], rsi
0086A0CA  48 8B DE                        mov rbx, rsi
0086A0CD  41 8B F5                        mov esi, r13d
0086A0D0  49 83 BE 80 00 00 00 00         cmp qword ptr [r14 + 0x80], 0
0086A0D8  0F 84 93 00 00 00               je 0x14086a171
0086A0DE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086A0E7  4C 8B 54 24 40                  mov r10, qword ptr [rsp + 0x40]
0086A0EC  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
0086A0F1  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
0086A0F6  4C 39 90 B8 00 00 00            cmp qword ptr [rax + 0xb8], r10
0086A0FD  74 2D                           je 0x14086a12c
0086A0FF  49 8B CA                        mov rcx, r10
0086A102  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
0086A107  E8 D4 1D BE FF                  call 0x14044bee0
0086A10C  48 8B C8                        mov rcx, rax
0086A10F  E8 AC 87 BD FF                  call 0x1404428c0
0086A114  48 8B 4C 24 40                  mov rcx, qword ptr [rsp + 0x40]
0086A119  48 8D 55 C0                     lea rdx, [rbp - 0x40]
0086A11D  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0086A122  E8 D9 C6 9A FF                  call 0x140216800
0086A127  4C 8B 54 24 40                  mov r10, qword ptr [rsp + 0x40]
0086A12C  49 8B 86 80 00 00 00            mov rax, qword ptr [r14 + 0x80]
0086A133  48 8D 0D 96 99 FF FF            lea rcx, [rip - 0x666a]
0086A13A  44 8B C6                        mov r8d, esi
0086A13D  48 3B C1                        cmp rax, rcx
0086A140  0F 85 AE 00 00 00               jne 0x14086a1f4
0086A146  4C 8B CB                        mov r9, rbx
0086A149  48 8D 57 30                     lea rdx, [rdi + 0x30]
0086A14D  49 8B CA                        mov rcx, r10
0086A150  E8 7B 99 FF FF                  call 0x140863ad0
0086A155  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
0086A15A  74 15                           je 0x14086a171
0086A15C  33 D2                           xor edx, edx
0086A15E  48 8D 4D C0                     lea rcx, [rbp - 0x40]
0086A162  E8 C9 DB 9A FF                  call 0x140217d30
0086A167  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0086A16C  E8 4F F9 BD FF                  call 0x140449ac0
0086A171  48 83 FB 01                     cmp rbx, 1
0086A175  75 26                           jne 0x14086a19d
0086A177  0F B6 47 1A                     movzx eax, byte ptr [rdi + 0x1a]
0086A17B  A8 02                           test al, 2
0086A17D  74 1E                           je 0x14086a19d
0086A17F  83 E0 03                        and eax, 3
0086A182  48 8D 0D 77 5E 79 FF            lea rcx, [rip - 0x86a189]
0086A189  48 8B DF                        mov rbx, rdi
0086A18C  0F B6 84 08 80 FF F0 00         movzx eax, byte ptr [rax + rcx + 0xf0ff80]
0086A194  48 2B D8                        sub rbx, rax
0086A197  0F 85 D3 00 00 00               jne 0x14086a270
0086A19D  F0 41 FF 4E 30                  lock dec dword ptr [r14 + 0x30]
0086A1A2  80 7C 24 31 00                  cmp byte ptr [rsp + 0x31], 0
0086A1A7  74 0B                           je 0x14086a1b4
0086A1A9  33 D2                           xor edx, edx
0086A1AB  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0086A1AF  E8 7C DB 9A FF                  call 0x140217d30
0086A1B4  45 85 FF                        test r15d, r15d
0086A1B7  74 0A                           je 0x14086a1c3
0086A1B9  41 F7 DF                        neg r15d
0086A1BC  49 63 C7                        movsxd rax, r15d
0086A1BF  F0 48 01 07                     lock add qword ptr [rdi], rax
0086A1C3  BA 4F 62 48 6E                  mov edx, 0x6e48624f
0086A1C8  48 8D 4F 30                     lea rcx, [rdi + 0x30]
0086A1CC  E8 0F D7 A8 FF                  call 0x1402f78e0
0086A1D1  33 C0                           xor eax, eax
0086A1D3  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
0086A1D7  48 33 CC                        xor rcx, rsp
0086A1DA  E8 61 24 E4 FF                  call 0x1406ac640
0086A1DF  48 81 C4 08 01 00 00            add rsp, 0x108
0086A1E6  41 5F                           pop r15
0086A1E8  41 5E                           pop r14
0086A1EA  41 5D                           pop r13
0086A1EC  41 5C                           pop r12
0086A1EE  5F                              pop rdi
0086A1EF  5E                              pop rsi
0086A1F0  5B                              pop rbx
0086A1F1  5D                              pop rbp
0086A1F2  C3                              ret
0086A1F3  CC                              int3
0086A1F4  48 8D 0D B5 2C 1A 00            lea rcx, [rip + 0x1a2cb5]
0086A1FB  48 3B C1                        cmp rax, rcx
0086A1FE  0F 85 39 02 00 00               jne 0x14086a43d
0086A204  48 83 FB 01                     cmp rbx, 1
0086A208  0F 85 47 FF FF FF               jne 0x14086a155
0086A20E  0F B6 87 92 00 00 00            movzx eax, byte ptr [rdi + 0x92]
0086A215  A8 02                           test al, 2
0086A217  74 42                           je 0x14086a25b
0086A219  48 8B 0D 20 56 69 00            mov rcx, qword ptr [rip + 0x695620]
0086A220  48 8D 15 61 66 7A FF            lea rdx, [rip - 0x85999f]
0086A227  E8 24 82 B2 FF                  call 0x140392450
0086A22C  84 C0                           test al, al
0086A22E  74 2B                           je 0x14086a25b
0086A230  48 8B 47 50                     mov rax, qword ptr [rdi + 0x50]
0086A234  48 8D 15 4D 66 7A FF            lea rdx, [rip - 0x8599b3]
0086A23B  48 8B 0D FE 55 69 00            mov rcx, qword ptr [rip + 0x6955fe]
0086A242  48 83 C0 28                     add rax, 0x28
0086A246  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0086A24B  44 8B CB                        mov r9d, ebx
0086A24E  45 33 C0                        xor r8d, r8d
0086A251  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0086A256  E8 BD 9A FF FF                  call 0x140863d18
0086A25B  66 F0 83 8F 92 00 00 00 20      lock or word ptr [rdi + 0x92], 0x20
0086A264  E9 EC FE FF FF                  jmp 0x14086a155
0086A269  0F 1F 80 00 00 00 00            nop dword ptr [rax]
0086A270  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086A279  48 8D 4F 10                     lea rcx, [rdi + 0x10]
0086A27D  45 33 C0                        xor r8d, r8d
0086A280  33 D2                           xor edx, edx
0086A282  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0086A289  90                              nop
0086A28A  E8 A1 5F 9A FF                  call 0x140210230
0086A28F  F0 48 0F BA 6F 10 00            lock bts qword ptr [rdi + 0x10], 0
0086A296  4C 8B E0                        mov r12, rax
0086A299  73 10                           jae 0x14086a2ab
0086A29B  4C 8D 47 10                     lea r8, [rdi + 0x10]
0086A29F  48 8B D0                        mov rdx, rax
0086A2A2  48 8D 4F 10                     lea rcx, [rdi + 0x10]
0086A2A6  E8 E5 59 9A FF                  call 0x14020fc90
0086A2AB  4D 85 E4                        test r12, r12
0086A2AE  74 06                           je 0x14086a2b6
0086A2B0  41 C6 44 24 0A 01               mov byte ptr [r12 + 0xa], 1
0086A2B6  4C 8B 23                        mov r12, qword ptr [rbx]
0086A2B9  4D 85 E4                        test r12, r12
0086A2BC  0F 84 B5 01 00 00               je 0x14086a477
0086A2C2  F6 47 1B 10                     test byte ptr [rdi + 0x1b], 0x10
0086A2C6  75 0B                           jne 0x14086a2d3
0086A2C8  48 83 7F 08 00                  cmp qword ptr [rdi + 8], 0
0086A2CD  0F 84 09 04 00 00               je 0x14086a6dc
0086A2D3  0F 0D 4F 10                     prefetchw byte ptr [rdi + 0x10]
0086A2D7  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0086A2DB  48 8B C8                        mov rcx, rax
0086A2DE  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0086A2E2  48 83 F9 10                     cmp rcx, 0x10
0086A2E6  48 8D 50 F0                     lea rdx, [rax - 0x10]
0086A2EA  49 0F 46 D5                     cmovbe rdx, r13
0086A2EE  A8 02                           test al, 2
0086A2F0  0F 85 AC 01 00 00               jne 0x14086a4a2
0086A2F6  F0 48 0F B1 57 10               lock cmpxchg qword ptr [rdi + 0x10], rdx
0086A2FC  0F 85 A0 01 00 00               jne 0x14086a4a2
0086A302  48 8D 4F 10                     lea rcx, [rdi + 0x10]
0086A306  E8 F5 72 A7 FF                  call 0x1402e1600
0086A30B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086A314  E8 D7 4C 9F FF                  call 0x14025eff0
0086A319  E9 7F FE FF FF                  jmp 0x14086a19d
0086A31E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086A327  48 8D 4F 10                     lea rcx, [rdi + 0x10]
0086A32B  45 33 C0                        xor r8d, r8d
0086A32E  33 D2                           xor edx, edx
0086A330  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0086A337  90                              nop
0086A338  E8 F3 5E 9A FF                  call 0x140210230
0086A33D  F0 48 0F BA 6F 10 00            lock bts qword ptr [rdi + 0x10], 0
0086A344  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0086A349  73 15                           jae 0x14086a360
0086A34B  4C 8D 47 10                     lea r8, [rdi + 0x10]
0086A34F  48 8B D0                        mov rdx, rax
0086A352  48 8D 4F 10                     lea rcx, [rdi + 0x10]
0086A356  E8 35 59 9A FF                  call 0x14020fc90
0086A35B  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0086A360  48 85 C0                        test rax, rax
0086A363  74 04                           je 0x14086a369
0086A365  C6 40 0A 01                     mov byte ptr [rax + 0xa], 1
0086A369  48 8B 5F 08                     mov rbx, qword ptr [rdi + 8]
0086A36D  F0 48 0F C1 77 08               lock xadd qword ptr [rdi + 8], rsi
0086A373  48 8D 15 86 5C 79 FF            lea rdx, [rip - 0x86a37a]
0086A37A  48 83 FE 01                     cmp rsi, 1
0086A37E  75 20                           jne 0x14086a3a0
0086A380  0F B6 47 1B                     movzx eax, byte ptr [rdi + 0x1b]
0086A384  A8 08                           test al, 8
0086A386  74 18                           je 0x14086a3a0
0086A388  0F B6 47 1A                     movzx eax, byte ptr [rdi + 0x1a]
0086A38C  48 8B CF                        mov rcx, rdi
0086A38F  83 E0 1F                        and eax, 0x1f
0086A392  0F B6 84 10 80 FF F0 00         movzx eax, byte ptr [rax + rdx + 0xf0ff80]
0086A39A  48 2B C8                        sub rcx, rax
0086A39D  4C 89 29                        mov qword ptr [rcx], r13
0086A3A0  41 0F B6 46 42                  movzx eax, byte ptr [r14 + 0x42]
0086A3A5  A8 10                           test al, 0x10
0086A3A7  0F 84 0B 03 00 00               je 0x14086a6b8
0086A3AD  0F B6 47 1A                     movzx eax, byte ptr [rdi + 0x1a]
0086A3B1  A8 04                           test al, 4
0086A3B3  0F 85 A8 00 00 00               jne 0x14086a461
0086A3B9  49 8B D5                        mov rdx, r13
0086A3BC  F6 47 1B 40                     test byte ptr [rdi + 0x1b], 0x40
0086A3C0  0F 84 EA 00 00 00               je 0x14086a4b0
0086A3C6  8B 72 08                        mov esi, dword ptr [rdx + 8]
0086A3C9  8B CE                           mov ecx, esi
0086A3CB  81 E6 FF FF FF 00               and esi, 0xffffff
0086A3D1  8D 41 FF                        lea eax, [rcx - 1]
0086A3D4  33 C1                           xor eax, ecx
0086A3D6  25 FF FF FF 00                  and eax, 0xffffff
0086A3DB  33 C1                           xor eax, ecx
0086A3DD  89 42 08                        mov dword ptr [rdx + 8], eax
0086A3E0  80 7A 0B 00                     cmp byte ptr [rdx + 0xb], 0
0086A3E4  75 0C                           jne 0x14086a3f2
0086A3E6  F7 42 08 FF FF FF 00            test dword ptr [rdx + 8], 0xffffff
0086A3ED  75 03                           jne 0x14086a3f2
0086A3EF  4C 89 2A                        mov qword ptr [rdx], r13
0086A3F2  48 8D 57 10                     lea rdx, [rdi + 0x10]
0086A3F6  0F 0D 0A                        prefetchw byte ptr [rdx]
0086A3F9  48 8B 02                        mov rax, qword ptr [rdx]
0086A3FC  48 8B C8                        mov rcx, rax
0086A3FF  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0086A403  48 83 F9 10                     cmp rcx, 0x10
0086A407  4C 8D 40 F0                     lea r8, [rax - 0x10]
0086A40B  4D 0F 46 C5                     cmovbe r8, r13
0086A40F  A8 02                           test al, 2
0086A411  0F 85 99 01 00 00               jne 0x14086a5b0
0086A417  F0 4C 0F B1 02                  lock cmpxchg qword ptr [rdx], r8
0086A41C  0F 85 8E 01 00 00               jne 0x14086a5b0
0086A422  48 8B CA                        mov rcx, rdx
0086A425  E8 D6 71 A7 FF                  call 0x1402e1600
0086A42A  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086A433  E8 B8 4B 9F FF                  call 0x14025eff0
0086A438  E9 93 FC FF FF                  jmp 0x14086a0d0
0086A43D  48 8D 0D 7C 9C FF FF            lea rcx, [rip - 0x6384]
0086A444  4C 8B CB                        mov r9, rbx
0086A447  48 3B C1                        cmp rax, rcx
0086A44A  48 8D 57 30                     lea rdx, [rdi + 0x30]
0086A44E  49 8B CA                        mov rcx, r10
0086A451  0F 85 72 01 00 00               jne 0x14086a5c9
0086A457  E8 64 9C FF FF                  call 0x1408640c0
0086A45C  E9 F4 FC FF FF                  jmp 0x14086a155
0086A461  83 E0 07                        and eax, 7
0086A464  0F B6 84 10 80 FF F0 00         movzx eax, byte ptr [rax + rdx + 0xf0ff80]
0086A46C  48 8B D7                        mov rdx, rdi
0086A46F  48 2B D0                        sub rdx, rax
0086A472  E9 45 FF FF FF                  jmp 0x14086a3bc
0086A477  0F 0D 4F 10                     prefetchw byte ptr [rdi + 0x10]
0086A47B  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0086A47F  48 8B C8                        mov rcx, rax
0086A482  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0086A486  48 83 F9 10                     cmp rcx, 0x10
0086A48A  48 8D 50 F0                     lea rdx, [rax - 0x10]
0086A48E  49 0F 46 D5                     cmovbe rdx, r13
0086A492  A8 02                           test al, 2
0086A494  75 0C                           jne 0x14086a4a2
0086A496  F0 48 0F B1 57 10               lock cmpxchg qword ptr [rdi + 0x10], rdx
0086A49C  0F 84 60 FE FF FF               je 0x14086a302
0086A4A2  48 8D 4F 10                     lea rcx, [rdi + 0x10]
0086A4A6  E8 25 94 9F FF                  call 0x1402638d0
0086A4AB  E9 52 FE FF FF                  jmp 0x14086a302
0086A4B0  48 8B 02                        mov rax, qword ptr [rdx]
0086A4B3  8B 08                           mov ecx, dword ptr [rax]
0086A4B5  48 8D 50 08                     lea rdx, [rax + 8]
0086A4B9  48 8B 44 24 40                  mov rax, qword ptr [rsp + 0x40]
0086A4BE  66 90                           nop
0086A4C0  85 C9                           test ecx, ecx
0086A4C2  0F 84 F9 00 00 00               je 0x14086a5c1
0086A4C8  44 8B 42 08                     mov r8d, dword ptr [rdx + 8]
0086A4CC  41 8B F0                        mov esi, r8d
0086A4CF  81 E6 FF FF FF 00               and esi, 0xffffff
0086A4D5  74 09                           je 0x14086a4e0
0086A4D7  48 39 02                        cmp qword ptr [rdx], rax
0086A4DA  0F 84 8D 00 00 00               je 0x14086a56d
0086A4E0  48 83 C2 10                     add rdx, 0x10
0086A4E4  FF C9                           dec ecx
0086A4E6  EB D8                           jmp 0x14086a4c0
0086A4E8  48 8B 43 10                     mov rax, qword ptr [rbx + 0x10]
0086A4EC  48 85 C0                        test rax, rax
0086A4EF  0F 84 2D 01 00 00               je 0x14086a622
0086A4F5  4C 89 60 08                     mov qword ptr [rax + 8], r12
0086A4F9  4C 89 63 10                     mov qword ptr [rbx + 0x10], r12
0086A4FD  E9 F4 FA FF FF                  jmp 0x140869ff6
0086A502  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086A50B  4C 39 A8 B8 00 00 00            cmp qword ptr [rax + 0xb8], r13
0086A512  74 16                           je 0x14086a52a
0086A514  48 8D 55 90                     lea rdx, [rbp - 0x70]
0086A518  49 8B CD                        mov rcx, r13
0086A51B  E8 E0 C2 9A FF                  call 0x140216800
0086A520  B3 01                           mov bl, 1
0086A522  4C 8D 57 30                     lea r10, [rdi + 0x30]
0086A526  88 5C 24 31                     mov byte ptr [rsp + 0x31], bl
0086A52A  48 8B 86 A8 00 00 00            mov rax, qword ptr [rsi + 0xa8]
0086A531  48 8D 0D 68 AB 09 00            lea rcx, [rip + 0x9ab68]
0086A538  44 0F B6 4D 70                  movzx r9d, byte ptr [rbp + 0x70]
0086A53D  48 3B C1                        cmp rax, rcx
0086A540  49 8B CD                        mov rcx, r13
0086A543  4D 8B C6                        mov r8, r14
0086A546  49 8B D2                        mov rdx, r10
0086A549  0F 85 DB 04 00 00               jne 0x14086aa2a
0086A54F  E8 4C AB 09 00                  call 0x1409050a0
0086A554  84 C0                           test al, al
0086A556  0F 84 84 00 00 00               je 0x14086a5e0
0086A55C  4C 8D 57 30                     lea r10, [rdi + 0x30]
0086A560  E9 4F F9 FF FF                  jmp 0x140869eb4
0086A565  41 8B C5                        mov eax, r13d
0086A568  E9 2C FA FF FF                  jmp 0x140869f99
0086A56D  41 8D 40 FF                     lea eax, [r8 - 1]
0086A571  41 33 C0                        xor eax, r8d
0086A574  25 FF FF FF 00                  and eax, 0xffffff
0086A579  41 33 C0                        xor eax, r8d
0086A57C  89 42 08                        mov dword ptr [rdx + 8], eax
0086A57F  E9 5C FE FF FF                  jmp 0x14086a3e0
0086A584  49 8B 1C 24                     mov rbx, qword ptr [r12]
0086A588  49 8D 4F 30                     lea rcx, [r15 + 0x30]
0086A58C  48 D1 EB                        shr rbx, 1
0086A58F  45 33 ED                        xor r13d, r13d
0086A592  4D 89 2C 24                     mov qword ptr [r12], r13
0086A596  F0 44 09 2C 24                  lock or dword ptr [rsp], r13d
0086A59B  4C 39 29                        cmp qword ptr [rcx], r13
0086A59E  0F 84 74 FA FF FF               je 0x14086a018
0086A5A4  33 D2                           xor edx, edx
0086A5A6  E8 35 9A A3 FF                  call 0x1402a3fe0
0086A5AB  E9 68 FA FF FF                  jmp 0x14086a018
0086A5B0  48 8B CA                        mov rcx, rdx
0086A5B3  E8 18 93 9F FF                  call 0x1402638d0
0086A5B8  48 8D 57 10                     lea rdx, [rdi + 0x10]
0086A5BC  E9 61 FE FF FF                  jmp 0x14086a422
0086A5C1  41 8B F5                        mov esi, r13d
0086A5C4  E9 17 FE FF FF                  jmp 0x14086a3e0
0086A5C9  E8 02 05 E5 FF                  call 0x1406baad0
0086A5CE  E9 82 FB FF FF                  jmp 0x14086a155
0086A5D3  48 8B CB                        mov rcx, rbx
0086A5D6  E8 F5 B7 9F FF                  call 0x140265dd0
0086A5DB  E9 2B FA FF FF                  jmp 0x14086a00b
0086A5E0  F0 49 FF 04 24                  lock inc qword ptr [r12]
0086A5E5  49 8D 4F 30                     lea rcx, [r15 + 0x30]
0086A5E9  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
0086A5EE  48 83 39 00                     cmp qword ptr [rcx], 0
0086A5F2  74 07                           je 0x14086a5fb
0086A5F4  33 D2                           xor edx, edx
0086A5F6  E8 E5 99 A3 FF                  call 0x1402a3fe0
0086A5FB  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086A604  E8 E7 49 9F FF                  call 0x14025eff0
0086A609  84 DB                           test bl, bl
0086A60B  74 0B                           je 0x14086a618
0086A60D  33 D2                           xor edx, edx
0086A60F  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0086A613  E8 18 D7 9A FF                  call 0x140217d30
0086A618  B8 35 02 00 C0                  mov eax, 0xc0000235
0086A61D  E9 B1 FB FF FF                  jmp 0x14086a1d3
0086A622  4C 89 63 08                     mov qword ptr [rbx + 8], r12
0086A626  E9 CE FE FF FF                  jmp 0x14086a4f9
0086A62B  84 DB                           test bl, bl
0086A62D  0F 85 9A F8 FF FF               jne 0x140869ecd
0086A633  38 5D 70                        cmp byte ptr [rbp + 0x70], bl
0086A636  0F 84 84 00 00 00               je 0x14086a6c0
0086A63C  49 8B D4                        mov rdx, r12
0086A63F  49 8B CF                        mov rcx, r15
0086A642  E8 89 2C 0E 00                  call 0x14094d2d0
0086A647  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086A650  E8 9B 49 9F FF                  call 0x14025eff0
0086A655  38 5C 24 31                     cmp byte ptr [rsp + 0x31], bl
0086A659  74 0B                           je 0x14086a666
0086A65B  33 D2                           xor edx, edx
0086A65D  48 8D 4D 90                     lea rcx, [rbp - 0x70]
0086A661  E8 CA D6 9A FF                  call 0x140217d30
0086A666  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086A66F  80 B8 4A 02 00 00 01            cmp byte ptr [rax + 0x24a], 1
0086A676  74 A0                           je 0x14086a618
0086A678  F7 05 3E 9C 75 00 00 00 40 00   test dword ptr [rip + 0x759c3e], 0x400000
0086A682  75 25                           jne 0x14086a6a9
0086A684  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086A68D  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
0086A694  48 83 B9 08 03 00 00 00         cmp qword ptr [rcx + 0x308], 0
0086A69C  75 0B                           jne 0x14086a6a9
0086A69E  49 83 7F 60 00                  cmp qword ptr [r15 + 0x60], 0
0086A6A3  0F 84 6F FF FF FF               je 0x14086a618
0086A6A9  B9 35 02 00 C0                  mov ecx, 0xc0000235
0086A6AE  E8 9D D0 C6 FF                  call 0x1404d7750
0086A6B3  E9 1B FB FF FF                  jmp 0x14086a1d3
0086A6B8  41 8B F5                        mov esi, r13d
0086A6BB  E9 32 FD FF FF                  jmp 0x14086a3f2
0086A6C0  45 33 ED                        xor r13d, r13d
0086A6C3  45 33 C9                        xor r9d, r9d
0086A6C6  45 33 C0                        xor r8d, r8d
0086A6C9  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
0086A6CE  49 8B D6                        mov rdx, r14
0086A6D1  B9 93 00 00 00                  mov ecx, 0x93
0086A6D6  E8 85 2F C9 FF                  call 0x1404fd660
0086A6DB  CC                              int3
0086A6DC  33 C0                           xor eax, eax
0086A6DE  49 8D 8C 24 28 01 00 00         lea rcx, [r12 + 0x128]
0086A6E6  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
0086A6EB  33 D2                           xor edx, edx
0086A6ED  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086A6F6  0F 57 C0                        xorps xmm0, xmm0
0086A6F9  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
0086A6FE  4C 89 64 24 50                  mov qword ptr [rsp + 0x50], r12
0086A703  44 8D 42 01                     lea r8d, [rdx + 1]
0086A707  C6 44 24 65 01                  mov byte ptr [rsp + 0x65], 1
0086A70C  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0086A713  90                              nop
0086A714  E8 17 5B 9A FF                  call 0x140210230
0086A719  49 8D 8C 24 28 01 00 00         lea rcx, [r12 + 0x128]
0086A721  F0 48 0F BA 29 00               lock bts qword ptr [rcx], 0
0086A727  0F 82 57 01 00 00               jb 0x14086a884
0086A72D  48 85 C0                        test rax, rax
0086A730  0F 85 FE 02 00 00               jne 0x14086aa34
0086A736  83 7B 18 00                     cmp dword ptr [rbx + 0x18], 0
0086A73A  0F 85 3C 01 00 00               jne 0x14086a87c
0086A740  48 8B C7                        mov rax, rdi
0086A743  4C 8D 25 B6 58 79 FF            lea r12, [rip - 0x86a74a]
0086A74A  48 C1 E8 08                     shr rax, 8
0086A74E  0F B6 C8                        movzx ecx, al
0086A751  0F B6 47 18                     movzx eax, byte ptr [rdi + 0x18]
0086A755  48 33 C8                        xor rcx, rax
0086A758  0F B6 05 ED C6 75 00            movzx eax, byte ptr [rip + 0x75c6ed]
0086A75F  48 33 C8                        xor rcx, rax
0086A762  48 8B 05 EF 4E 6A 00            mov rax, qword ptr [rip + 0x6a4eef]
0086A769  49 39 84 CC 00 78 FC 00         cmp qword ptr [r12 + rcx*8 + 0xfc7800], rax
0086A771  75 09                           jne 0x14086a77c
0086A773  48 8D 4F 30                     lea rcx, [rdi + 0x30]
0086A777  E8 04 15 21 00                  call 0x140a7bc80
0086A77C  48 8D 4B 08                     lea rcx, [rbx + 8]
0086A780  33 D2                           xor edx, edx
0086A782  4C 8D 44 24 50                  lea r8, [rsp + 0x50]
0086A787  E8 24 2E FF FF                  call 0x14085d5b0
0086A78C  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0086A791  48 8B 32                        mov rsi, qword ptr [rdx]
0086A794  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
0086A798  48 83 E9 30                     sub rcx, 0x30
0086A79C  0F B6 41 1A                     movzx eax, byte ptr [rcx + 0x1a]
0086A7A0  83 E0 03                        and eax, 3
0086A7A3  42 0F B6 84 20 80 FF F0 00      movzx eax, byte ptr [rax + r12 + 0xf0ff80]
0086A7AC  48 2B C8                        sub rcx, rax
0086A7AF  4C 89 29                        mov qword ptr [rcx], r13
0086A7B2  48 8B 06                        mov rax, qword ptr [rsi]
0086A7B5  48 89 02                        mov qword ptr [rdx], rax
0086A7B8  4C 89 2E                        mov qword ptr [rsi], r13
0086A7BB  0F 0D 4F 10                     prefetchw byte ptr [rdi + 0x10]
0086A7BF  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0086A7C3  48 8B C8                        mov rcx, rax
0086A7C6  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0086A7CA  48 83 F9 10                     cmp rcx, 0x10
0086A7CE  48 8D 50 F0                     lea rdx, [rax - 0x10]
0086A7D2  49 0F 46 D5                     cmovbe rdx, r13
0086A7D6  A8 02                           test al, 2
0086A7D8  0F 85 90 00 00 00               jne 0x14086a86e
0086A7DE  F0 48 0F B1 57 10               lock cmpxchg qword ptr [rdi + 0x10], rdx
0086A7E4  0F 85 84 00 00 00               jne 0x14086a86e
0086A7EA  48 8D 4F 10                     lea rcx, [rdi + 0x10]
0086A7EE  E8 0D 6E A7 FF                  call 0x1402e1600
0086A7F3  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086A7FC  E8 EF 47 9F FF                  call 0x14025eff0
0086A801  48 85 F6                        test rsi, rsi
0086A804  74 59                           je 0x14086a85f
0086A806  4C 8B 6E 08                     mov r13, qword ptr [rsi + 8]
0086A80A  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0086A80F  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0086A814  E8 87 50 13 00                  call 0x14099f8a0
0086A819  33 D2                           xor edx, edx
0086A81B  48 8B CE                        mov rcx, rsi
0086A81E  E8 4D 80 31 00                  call 0x140b82870
0086A823  BA 4F 62 44 69                  mov edx, 0x6944624f
0086A828  48 8B CB                        mov rcx, rbx
0086A82B  E8 B0 D0 A8 FF                  call 0x1402f78e0
0086A830  48 8B 05 19 4E 6A 00            mov rax, qword ptr [rip + 0x6a4e19]
0086A837  49 8D 55 D0                     lea rdx, [r13 - 0x30]
0086A83B  48 C1 EA 08                     shr rdx, 8
0086A83F  49 8B CD                        mov rcx, r13
0086A842  41 32 55 E8                     xor dl, byte ptr [r13 - 0x18]
0086A846  32 15 00 C6 75 00               xor dl, byte ptr [rip + 0x75c600]
0086A84C  3A 50 28                        cmp dl, byte ptr [rax + 0x28]
0086A84F  0F 84 C1 01 00 00               je 0x14086aa16
0086A855  BA 4F 62 44 69                  mov edx, 0x6944624f
0086A85A  E8 81 D0 A8 FF                  call 0x1402f78e0
0086A85F  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0086A864  E8 C7 94 9F FF                  call 0x140263d30
0086A869  E9 2F F9 FF FF                  jmp 0x14086a19d
0086A86E  48 8D 4F 10                     lea rcx, [rdi + 0x10]
0086A872  E8 59 90 9F FF                  call 0x1402638d0
0086A877  E9 6E FF FF FF                  jmp 0x14086a7ea
0086A87C  49 8B F5                        mov rsi, r13
0086A87F  E9 37 FF FF FF                  jmp 0x14086a7bb
0086A884  48 85 C0                        test rax, rax
0086A887  74 08                           je 0x14086a891
0086A889  48 8B D0                        mov rdx, rax
0086A88C  E8 7F 79 9F FF                  call 0x140262210
0086A891  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086A89A  E8 51 47 9F FF                  call 0x14025eff0
0086A89F  49 8B CC                        mov rcx, r12
0086A8A2  E8 79 51 9A FF                  call 0x14020fa20
0086A8A7  0F 0D 4F 10                     prefetchw byte ptr [rdi + 0x10]
0086A8AB  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0086A8AF  48 8B C8                        mov rcx, rax
0086A8B2  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0086A8B6  48 83 F9 10                     cmp rcx, 0x10
0086A8BA  48 8D 50 F0                     lea rdx, [rax - 0x10]
0086A8BE  49 0F 46 D5                     cmovbe rdx, r13
0086A8C2  A8 02                           test al, 2
0086A8C4  0F 85 19 01 00 00               jne 0x14086a9e3
0086A8CA  F0 48 0F B1 57 10               lock cmpxchg qword ptr [rdi + 0x10], rdx
0086A8D0  0F 85 0D 01 00 00               jne 0x14086a9e3
0086A8D6  48 8D 4F 10                     lea rcx, [rdi + 0x10]
0086A8DA  E8 21 6D A7 FF                  call 0x1402e1600
0086A8DF  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086A8E8  E8 03 47 9F FF                  call 0x14025eff0
0086A8ED  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086A8F6  49 8D 8C 24 28 01 00 00         lea rcx, [r12 + 0x128]
0086A8FE  45 33 C0                        xor r8d, r8d
0086A901  33 D2                           xor edx, edx
0086A903  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0086A90A  90                              nop
0086A90B  E8 20 59 9A FF                  call 0x140210230
0086A910  49 8D 8C 24 28 01 00 00         lea rcx, [r12 + 0x128]
0086A918  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0086A91D  F0 48 0F BA 29 00               lock bts qword ptr [rcx], 0
0086A923  73 10                           jae 0x14086a935
0086A925  4C 8B C1                        mov r8, rcx
0086A928  48 8B D0                        mov rdx, rax
0086A92B  E8 60 53 9A FF                  call 0x14020fc90
0086A930  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0086A935  48 85 C0                        test rax, rax
0086A938  74 04                           je 0x14086a93e
0086A93A  C6 40 0A 01                     mov byte ptr [rax + 0xa], 1
0086A93E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0086A947  48 8D 4F 10                     lea rcx, [rdi + 0x10]
0086A94B  45 33 C0                        xor r8d, r8d
0086A94E  33 D2                           xor edx, edx
0086A950  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0086A957  90                              nop
0086A958  E8 D3 58 9A FF                  call 0x140210230
0086A95D  F0 48 0F BA 6F 10 00            lock bts qword ptr [rdi + 0x10], 0
0086A964  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0086A969  73 15                           jae 0x14086a980
0086A96B  4C 8D 47 10                     lea r8, [rdi + 0x10]
0086A96F  48 8B D0                        mov rdx, rax
0086A972  48 8D 4F 10                     lea rcx, [rdi + 0x10]
0086A976  E8 15 53 9A FF                  call 0x14020fc90
0086A97B  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
0086A980  48 85 C0                        test rax, rax
0086A983  74 04                           je 0x14086a989
0086A985  C6 40 0A 01                     mov byte ptr [rax + 0xa], 1
0086A989  4C 39 23                        cmp qword ptr [rbx], r12
0086A98C  74 6E                           je 0x14086a9fc
0086A98E  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0086A993  E8 98 93 9F FF                  call 0x140263d30
0086A998  0F 0D 4F 10                     prefetchw byte ptr [rdi + 0x10]
0086A99C  48 8B 47 10                     mov rax, qword ptr [rdi + 0x10]
0086A9A0  48 8B C8                        mov rcx, rax
0086A9A3  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0086A9A7  48 83 F9 10                     cmp rcx, 0x10
0086A9AB  48 8D 50 F0                     lea rdx, [rax - 0x10]
0086A9AF  49 0F 46 D5                     cmovbe rdx, r13
0086A9B3  A8 02                           test al, 2
0086A9B5  75 3A                           jne 0x14086a9f1
0086A9B7  F0 48 0F B1 57 10               lock cmpxchg qword ptr [rdi + 0x10], rdx
0086A9BD  75 32                           jne 0x14086a9f1
0086A9BF  48 8D 4F 10                     lea rcx, [rdi + 0x10]
0086A9C3  E8 38 6C A7 FF                  call 0x1402e1600
0086A9C8  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0086A9D1  E8 1A 46 9F FF                  call 0x14025eff0
0086A9D6  49 8B CC                        mov rcx, r12
0086A9D9  E8 52 3B C2 FF                  call 0x14048e530
0086A9DE  E9 8D F8 FF FF                  jmp 0x14086a270
0086A9E3  48 8D 4F 10                     lea rcx, [rdi + 0x10]
0086A9E7  E8 E4 8E 9F FF                  call 0x1402638d0
0086A9EC  E9 E5 FE FF FF                  jmp 0x14086a8d6
0086A9F1  48 8D 4F 10                     lea rcx, [rdi + 0x10]
0086A9F5  E8 D6 8E 9F FF                  call 0x1402638d0
0086A9FA  EB C3                           jmp 0x14086a9bf
0086A9FC  F6 47 1B 10                     test byte ptr [rdi + 0x1b], 0x10
0086AA00  75 8C                           jne 0x14086a98e
0086AA02  48 83 7F 08 00                  cmp qword ptr [rdi + 8], 0
0086AA07  75 85                           jne 0x14086a98e
0086AA09  49 8B CC                        mov rcx, r12
0086AA0C  E8 1F 3B C2 FF                  call 0x14048e530
0086AA11  E9 20 FD FF FF                  jmp 0x14086a736
0086AA16  E8 79 45 13 00                  call 0x14099ef94
0086AA1B  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
0086AA20  E8 0B 93 9F FF                  call 0x140263d30
0086AA25  E9 73 F7 FF FF                  jmp 0x14086a19d
0086AA2A  E8 A1 00 E5 FF                  call 0x1406baad0
0086AA2F  E9 20 FB FF FF                  jmp 0x14086a554
0086AA34  C6 40 0A 01                     mov byte ptr [rax + 0xa], 1
0086AA38  E9 F9 FC FF FF                  jmp 0x14086a736
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObCloseHandleTableEntry(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned __int8 a5, unsigned __int8 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int8 v_stack_m117;
    unsigned __int8 v_stack_m118;
    unsigned __int8 v_stack_m128;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_p0;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int8 v_stack_p31;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned __int64 v_stack_p60;
    unsigned __int8 v_stack_p65;

    v_rsp = (v_rsp) - (264);
    result = (*(unsigned __int64 *)(v_rip + 5900544)) ^ (v_rsp);
    v_stack_m58 = result;
    v_stack_m108 = a3;
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    result = ExGetHandlePointer(a2, a2, a3, a4);
    a1 = (result) >> (8);
    v_rbx = 0;
    a2 = ((unsigned __int8)(a1)) ^ (*(unsigned __int8 *)(result + 24));
    v_stack_m117 = 0;
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 7720885));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8822409 + a2 * 8 + 16545792) + 168)) != 0) goto loc_0086A502;
loc_00869EB4:
    result = (*(unsigned __int64 *)(a2)) >> (17);
    v_stack_m100 = result;
    if ((((unsigned __int8)(result)) & (1)) != 0) goto loc_0086A62B;
loc_00869ECD:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 7719997)))) & (64)) == 0) goto loc_00869EFB;
    result = (unsigned int)(*(unsigned int *)(v_rip + 7719997));
    if (a3 == (*(unsigned __int64 *)(v_rip + 7719890))) {
        result = 0x80000000ULL;
        a2 = (a4) | (result);
    }
    result = EtwpTraceHandle((unsigned int)(0x1121ULL), a2, result + 48, *(unsigned __int64 *)(v_rip - 8822409 + a2 * 8 + 16545792));
loc_00869EFB:
    if (a6 != 0) goto loc_0086A584;
    if ((*(unsigned __int64 *)(a1 + 96)) != 0) {
        a2 = *(unsigned __int64 *)(gs_base + (0 + 392));
        a4 = -1 + 3;
        a3 = a4;
        a1 = a1;
        result = ExpUpdateDebugInfo(a1, a2, a3, a4);
    }
    result = (*(unsigned __int64 *)(a2)) >> (1);
    v_r13 = 0;
    v_stack_mE0 = result;
    *(unsigned __int64 *)(a2) = 0;
    if ((*(unsigned __int64 *)(a1 + 48)) != 0) {
        a2 = 0;
        result = ExfUnblockPushLock(a1 + 48, a2, a3, a4);
    }
    v_stack_m110 = a4;
    result = (unsigned int)(((unsigned int)((unsigned int)(a4))) & (0xFFFFFFFCULL));
    v_stack_m110 = (unsigned int)(result);
    if ((*(unsigned int *)(a1 + 4)) == 0) goto loc_00869F7B;
    result = ExpGetHandleExtraInfo(a1, v_stack_m110, a3, a4);
    if (result != 0) {
        *(unsigned __int64 *)(result) = 0;
    }
    *(unsigned __int64 *)(a2 + 8) = 0;
    result = (unsigned __int8)((*(unsigned __int8 *)(a1 + 44)) & (1));
    v_stack_m118 = (unsigned __int8)(result);
    if (condition_is_not_equal) goto loc_0086A565;
loc_00869F99:
    a3 = 0;
    v_rbx = ((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(gs_base + (0 + 420)))))) + 1;
    a2 = 0;
    v_rbx = (v_rbx) << (6);
    v_rbx = (v_rbx) + (a1);
    result = KeAbPreAcquire(v_rbx, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rbx;
        a2 = result;
        a1 = v_rbx;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (v_stack_m118 != 0) goto loc_0086A4E8;
    *(unsigned __int64 *)(a2 + 8) = *(unsigned __int64 *)(v_rbx + 8);
    if (*(unsigned __int64 *)(v_rbx + 8) == 0) {
        *(unsigned __int64 *)(v_rbx + 16) = a2;
    }
    *(unsigned __int64 *)(v_rbx + 8) = a2;
loc_00869FF6:
    result = (unsigned __int8)((-1) & (6));
    if (((unsigned __int8)(result)) == 2) goto loc_0086A5D3;
loc_0086A00B:
    result = KeAbPostRelease(v_rbx, a2, a3, a4);
loc_0086A018:
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    v_r14 = a4;
    if (((v_stack_m100) & (4)) != 0) {
        a1 = v_stack_mD8;
        v_stack_mD8 = v_xmm0;
        v_stack_mC8 = v_xmm0;
        result = SeCaptureSubjectContext(a1, a2, a3, a4);
        v_r14 = (a4) & (-4);
        v_stack_m128 = 1;
        a2 = v_r14;
        a4 = result + 48;
        a3 = v_stack_mD8;
        a1 = v_rip - 8817851;
        result = SepAdtCloseObjectAuditAlarm(a1, a2, a3, a4);
        a1 = v_stack_mD8;
        result = SeReleaseSubjectContext(a1, a2, a3, a4);
    }
    result = (result) >> (8);
    a1 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(result + 24));
    a1 = (a1) ^ (*(unsigned __int8 *)(v_rip + 7720383));
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = v_xmm0;
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 8822935 + a1 * 8 + 16545792) + 66))) & (16)) != 0) goto loc_0086A31E;
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 27))) & (8)) != 0) goto loc_0086A31E;
loc_0086A0D0:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8822935 + a1 * 8 + 16545792) + 128)) == 0) goto loc_0086A171;
    v_stack_m118 = 0;
    v_stack_m110 = 0;
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_r10 = v_stack_m108;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) != v_stack_m108) {
        a1 = v_stack_m108;
        v_stack_m118 = 1;
        result = PsGetProcessServerSilo(a1, a2, a3, a4);
        a1 = result;
        result = PsAttachSiloToCurrentThread(a1, a2, a3, a4);
        a1 = v_stack_m108;
        a2 = v_stack_m88;
        v_stack_m110 = result;
        result = KeStackAttachProcess(a1, a2, a3, a4);
        v_r10 = v_stack_m108;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 8822935 + a1 * 8 + 16545792) + 128)) != (v_rip - 26218)) goto loc_0086A1F4;
    result = CmpCloseKeyObject(v_r10, result + 48, 0, -1);
loc_0086A155:
    if (v_stack_m118 != 0) {
        a2 = 0;
        a1 = v_stack_m88;
        result = KiUnstackDetachProcess(a1, a2, 0, -1);
        a1 = v_stack_m110;
        result = PsDetachSiloFromCurrentThread(a1, a2, 0, -1);
    }
    if (-1 != 1) goto loc_0086A19D;
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 26))) & (2)) == 0) goto loc_0086A19D;
    result = (unsigned int)((*(unsigned __int8 *)(result + 26)) & (3));
    v_rbx = (result) - (*(unsigned __int8 *)(result + v_rip - 8823177 * 1 + 15794048));
    if (condition_is_not_equal) goto loc_0086A270;
loc_0086A19D:
    result = *(unsigned __int8 *)(result + v_rip - 8823177 * 1 + 15794048);
    if (v_stack_m117 != 0) {
        a2 = 0;
        a1 = v_stack_mB8;
        result = KiUnstackDetachProcess(a1, a2, 0, -1);
    }
    v_r15 = (unsigned __int16)(v_stack_mE0);
    if ((unsigned int)((unsigned __int16)(v_stack_mE0)) != 0) {
        v_r15 = (unsigned int)(-((unsigned __int16)(v_stack_mE0)));
        result = (int)((unsigned int)(v_r15));
    }
    result = ObfDereferenceObjectWithTag(result + 48, (unsigned int)(0x6E48624FULL), 0, -1);
    result = 0;
loc_0086A1D3:
    a1 = (v_stack_m58) ^ (v_rsp);
    result = _security_check_cookie(a1, (unsigned int)(0x6E48624FULL), 0, -1);
    v_rsp = (v_rsp) + (264);
    return result;
loc_0086A1F4:
    if (result != (v_rip + 1715381)) goto loc_0086A43D;
    if (v_rbx != 1) goto loc_0086A155;
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 146))) & (2)) == 0) goto loc_0086A25B;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 6903328), v_rip - 8755615, 0, -1);
    if ((unsigned __int8)(result) != 0) {
        result = *(unsigned __int64 *)(result + 80);
        a2 = v_rip - 8755635;
        a1 = *(unsigned __int64 *)(v_rip + 6903294);
        result = (result) + (40);
        v_stack_p28 = result;
        a4 = (unsigned int)(v_rbx);
        a3 = 0;
        v_stack_p20 = 0;
        result = EtwpEventWriteTemplateSessAndProv(a1, a2, a3, a4);
    }
    goto loc_0086A155;
loc_0086A270:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 16, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = result + 16;
        a2 = result;
        a1 = result + 16;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (*(unsigned __int64 *)(v_rbx) == 0) goto loc_0086A477;
    if (((*(unsigned __int8 *)(result + 27)) & (16)) != 0) goto loc_0086A2D3;
    if ((*(unsigned __int64 *)(result + 8)) == 0) goto loc_0086A6DC;
loc_0086A2D3:
    a1 = (*(unsigned __int64 *)(result + 16)) & (-16);
    a2 = *(unsigned __int64 *)(result + 16) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 16))) & (2)) != 0) goto loc_0086A4A2;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 16))) & (2)) != 0) goto loc_0086A4A2;
loc_0086A302:
    result = KeAbPostRelease(result + 16, a2, a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    goto loc_0086A19D;
loc_0086A31E:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 16, a2, a3, a4);
    v_stack_p48 = result;
    if (!(condition_is_above_or_equal)) {
        a3 = result + 16;
        a2 = result;
        a1 = result + 16;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
        result = v_stack_p48;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (0 != 1) goto loc_0086A3A0;
    result = *(unsigned __int8 *)(result + 27);
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 27))) & (8)) != 0) {
        result = *(unsigned __int8 *)(result + 26);
        a1 = result;
        result = (unsigned int)((result) & (31));
        result = *(unsigned __int8 *)(result + v_rip - 8823674 * 1 + 15794048);
        a1 = (a1) - (result);
        *(unsigned __int64 *)(a1) = 0;
    }
    if ((((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 8822935 + a1 * 8 + 16545792) + 66))) & (16)) == 0) goto loc_0086A6B8;
    if ((((unsigned __int8)(*(unsigned __int8 *)(result + 26))) & (4)) != 0) goto loc_0086A461;
loc_0086A3BC:
    if (((*(unsigned __int8 *)(result + 27)) & (64)) == 0) goto loc_0086A4B0;
    v_rsi = (unsigned int)(((unsigned int)(*(unsigned int *)(0 + 8))) & (0xFFFFFFULL));
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(0 + 8)))) - 1) ^ ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(0 + 8)))))));
    result = (unsigned int)((result) & (0xFFFFFFULL));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(0 + 8)))))));
    *(unsigned int *)(0 + 8) = (unsigned int)(result);
loc_0086A3E0:
    if ((*(unsigned __int8 *)(0 + 11)) != 0) goto loc_0086A3F2;
    if (((*(unsigned int *)(0 + 8)) & (0xFFFFFFULL)) == 0) {
        *(unsigned __int64 *)(0) = 0;
    }
    a1 = (*(unsigned __int64 *)(result + 16)) & (-16);
    a3 = *(unsigned __int64 *)(result + 16) - 16;
    if (a1 <= 16) { a3 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 16))) & (2)) != 0) goto loc_0086A5B0;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 16))) & (2)) != 0) goto loc_0086A5B0;
loc_0086A422:
    result = KeAbPostRelease(result + 16, result + 16, a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), result + 16, a3, a4);
    goto loc_0086A0D0;
loc_0086A43D:
    if (result != (v_rip - 25476)) goto loc_0086A5C9;
    result = IopCloseFile(v_r10, result + 48, a3, *(unsigned __int64 *)(result + 8));
    goto loc_0086A155;
loc_0086A461:
    result = (unsigned int)((result) & (7));
    a2 = (result) - (*(unsigned __int8 *)(result + result + 48 * 1 + 15794048));
    goto loc_0086A3BC;
loc_0086A477:
    a1 = (*(unsigned __int64 *)(result + 16)) & (-16);
    a2 = *(unsigned __int64 *)(result + 16) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 16))) & (2)) != 0) goto loc_0086A4A2;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 16))) & (2)) == 0) goto loc_0086A302;
loc_0086A4A2:
    result = ExfReleasePushLock(result + 16, a2, a3, *(unsigned __int64 *)(result + 8));
    goto loc_0086A302;
loc_0086A4B0:
loc_0086A4C0:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2)))) == 0) goto loc_0086A5C1;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 8 + 8))))) & (0xFFFFFFULL));
    if (condition_is_equal) goto loc_0086A4E0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 8)) == v_stack_p40) goto loc_0086A56D;
loc_0086A4E0:
    a2 = (*(unsigned __int64 *)(a2) + 8) + (16);
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2)))) - 1);
    goto loc_0086A4C0;
loc_0086A4E8:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 16) == 0) goto loc_0086A622;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 16) + 8) = *(unsigned __int64 *)(v_rbx);
loc_0086A4F9:
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8) + 16) = *(unsigned __int64 *)(v_rbx);
    goto loc_00869FF6;
loc_0086A502:
    result = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_rbx = *(unsigned __int64 *)(result + 8);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184)) != 0) {
        a2 = v_stack_mB8;
        a1 = 0;
        result = KeStackAttachProcess(a1, a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 8 + 8)), *(unsigned __int64 *)(result + 8));
        v_rbx = 1;
        v_r10 = result + 48;
        v_stack_p31 = (unsigned __int8)(v_rbx);
    }
    if ((*(unsigned __int64 *)(v_rsi + 168)) != (v_rip + 633704)) goto loc_0086AA2A;
    result = ExpWin32OkayToCloseProcedure(0, v_r10, *(unsigned __int64 *)(v_rip - 8822935 + a1 * 8 + 16545792), a5);
loc_0086A554:
    if ((unsigned __int8)(result) == 0) goto loc_0086A5E0;
    goto loc_00869EB4;
loc_0086A565:
    goto loc_00869F99;
loc_0086A56D:
    result = (unsigned int)((*(unsigned __int64 *)(v_rip - 8822935 + a1 * 8 + 16545792) - 1) ^ ((unsigned int)(*(unsigned __int64 *)(v_rip - 8822935 + a1 * 8 + 16545792))));
    result = (unsigned int)((result) & (0xFFFFFFULL));
    result = (unsigned int)((result) ^ ((unsigned int)(*(unsigned __int64 *)(v_rip - 8822935 + a1 * 8 + 16545792))));
    *(unsigned int *)(v_r10 + 8) = (unsigned int)(result);
    goto loc_0086A3E0;
loc_0086A584:
    v_rbx = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx))) >> (1);
    v_r13 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx)) = 0;
    if ((*(unsigned __int64 *)(v_r15 + 48)) == 0) goto loc_0086A018;
    a2 = 0;
    result = ExfUnblockPushLock(v_r15 + 48, a2, *(unsigned __int64 *)(v_rip - 8822935 + a1 * 8 + 16545792), a5);
    goto loc_0086A018;
loc_0086A5B0:
    result = ExfReleasePushLock(0, a2, *(unsigned __int64 *)(v_rip - 8822935 + a1 * 8 + 16545792), a5);
    goto loc_0086A422;
loc_0086A5C1:
    goto loc_0086A3E0;
loc_0086A5C9:
    result = guard_dispatch_icall(0, result + 16, *(unsigned __int64 *)(v_rip - 8822935 + a1 * 8 + 16545792), a5);
    goto loc_0086A155;
loc_0086A5D3:
    result = ExfTryToWakePushLock(v_rbx, result + 16, *(unsigned __int64 *)(v_rip - 8822935 + a1 * 8 + 16545792), a5);
    goto loc_0086A00B;
loc_0086A5E0:
    if ((*(unsigned __int64 *)(v_r15 + 48)) != 0) {
        a2 = 0;
        result = ExfUnblockPushLock(v_r15 + 48, a2, *(unsigned __int64 *)(v_rip - 8822935 + a1 * 8 + 16545792), a5);
    }
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, *(unsigned __int64 *)(v_rip - 8822935 + a1 * 8 + 16545792), a5);
    if ((unsigned __int8)(v_rbx) != 0) {
        a2 = 0;
        a1 = v_stack_mB8;
        result = KiUnstackDetachProcess(a1, a2, *(unsigned __int64 *)(v_rip - 8822935 + a1 * 8 + 16545792), a5);
    }
    goto loc_0086A1D3;
loc_0086A622:
    *(unsigned __int64 *)(v_rbx + 8) = *(unsigned __int64 *)(v_rbx);
    goto loc_0086A4F9;
loc_0086A62B:
    if ((unsigned __int8)(v_rbx) != 0) goto loc_00869ECD;
    if (a5 == ((unsigned __int8)(v_rbx))) goto loc_0086A6C0;
    result = ExUnlockHandleTableEntry(v_r15, *(unsigned __int64 *)(v_rbx), *(unsigned __int64 *)(v_rip - 8822935 + a1 * 8 + 16545792), a5);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(v_rbx), *(unsigned __int64 *)(v_rip - 8822935 + a1 * 8 + 16545792), a5);
    if (v_stack_p31 != ((unsigned __int8)(v_rbx))) {
        a2 = 0;
        a1 = v_stack_mB8;
        result = KiUnstackDetachProcess(a1, a2, *(unsigned __int64 *)(v_rip - 8822935 + a1 * 8 + 16545792), a5);
    }
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 586)) == 1) goto loc_0086A618;
    if (((*(unsigned int *)(v_rip + 7707710)) & (0x400000ULL)) != 0) goto loc_0086A6A9;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 776)) != 0) goto loc_0086A6A9;
    if ((*(unsigned __int64 *)(v_r15 + 96)) == 0) goto loc_0086A618;
loc_0086A6A9:
    result = KeRaiseUserException((unsigned int)(0xC0000235ULL), a2, *(unsigned __int64 *)(v_rip - 8822935 + a1 * 8 + 16545792), a5);
    goto loc_0086A1D3;
loc_0086A6B8:
    goto loc_0086A3F2;
loc_0086A6C0:
    v_r13 = 0;
    a4 = 0;
    a3 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(147, *(unsigned __int64 *)(v_rip - 8822935 + a1 * 8 + 16545792), a3, a4);
loc_0086A6DC:
    result = 0;
    v_stack_p60 = 0;
    a2 = 0;
    v_stack_p50 = v_xmm0;
    v_stack_p50 = *(unsigned __int64 *)(v_rbx);
    v_stack_p65 = 1;
    result = KeAbPreAcquire(*(unsigned __int64 *)(v_rbx) + 296, a2, a2 + 1, a4);
    if (condition_is_below) goto loc_0086A884;
    if (result != 0) goto loc_0086AA34;
loc_0086A736:
    if ((*(unsigned int *)(v_rbx + 24)) != 0) goto loc_0086A87C;
    result = (result) >> (8);
    a1 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(result + 24));
    a1 = (a1) ^ (*(unsigned __int8 *)(v_rip + 7718637));
    result = *(unsigned __int64 *)(v_rip + 6967023);
    if ((*(unsigned __int64 *)(v_rip - 8824650 + a1 * 8 + 16545792)) == (*(unsigned __int64 *)(v_rip + 6967023))) {
        a1 = result + 48;
        result = ObpDeleteSymbolicLinkName(a1, a2, a2 + 1, a4);
    }
    a2 = 0;
    result = ObpLookupDirectoryEntry(v_rbx + 8, a2, v_stack_p50, a4);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58) + 8)) - (48);
    result = (unsigned int)((*(unsigned __int8 *)(a1 + 26)) & (3));
    a1 = (a1) - (*(unsigned __int8 *)(result + v_rip - 8824650 * 1 + 15794048));
    *(unsigned __int64 *)(a1) = 0;
    *(unsigned __int64 *)(v_stack_p58) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58)) = 0;
loc_0086A7BB:
    a1 = (*(unsigned __int64 *)(result + 16)) & (-16);
    a2 = *(unsigned __int64 *)(result + 16) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 16))) & (2)) != 0) goto loc_0086A86E;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 16))) & (2)) != 0) goto loc_0086A86E;
loc_0086A7EA:
    result = KeAbPostRelease(result + 16, a2, v_stack_p50, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, v_stack_p50, a4);
    if (*(unsigned __int64 *)(v_stack_p58) == 0) goto loc_0086A85F;
    result = ObpUnlockDirectory(v_stack_p50, a2, v_stack_p50, a4);
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_stack_p58), a2, v_stack_p50, a4);
    result = ObfDereferenceObjectWithTag(v_stack_p50, (unsigned int)(0x6944624FULL), v_stack_p50, a4);
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58) + 8) - 48) >> (8);
    a2 = (unsigned __int8)((a2) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58) + 8) - 24)));
    a2 = (unsigned __int8)((a2) ^ (*(unsigned __int8 *)(v_rip + 7718400)));
    if (((unsigned __int8)(a2)) == (*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 6966809) + 40))) goto loc_0086AA16;
    result = ObfDereferenceObjectWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58) + 8), (unsigned int)(0x6944624FULL), v_stack_p50, a4);
loc_0086A85F:
    result = ObpReleaseLookupContext(v_stack_p50, (unsigned int)(0x6944624FULL), v_stack_p50, a4);
    goto loc_0086A19D;
loc_0086A86E:
    result = ExfReleasePushLock(result + 16, (unsigned int)(0x6944624FULL), v_stack_p50, a4);
    goto loc_0086A7EA;
loc_0086A87C:
    goto loc_0086A7BB;
loc_0086A884:
    if (result != 0) {
        a2 = result;
        result = KeAbPostReleaseEx(result + 16, a2, v_stack_p50, a4);
    }
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, v_stack_p50, a4);
    result = ObfReferenceObject(v_rip - 8824650, a2, v_stack_p50, a4);
    a1 = (*(unsigned __int64 *)(result + 16)) & (-16);
    a2 = *(unsigned __int64 *)(result + 16) - 16;
    if (a1 <= 16) { a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58) + 8); }
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 16))) & (2)) != 0) goto loc_0086A9E3;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 16))) & (2)) != 0) goto loc_0086A9E3;
loc_0086A8D6:
    result = KeAbPostRelease(result + 16, a2, v_stack_p50, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, v_stack_p50, a4);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip - 8824650 + 296, a2, a3, a4);
    v_stack_p48 = result;
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip - 8824650 + 296;
        a2 = result;
        result = ExfAcquirePushLockExclusiveEx(v_rip - 8824650 + 296, a2, a3, a4);
        result = v_stack_p48;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 16, a2, a3, a4);
    v_stack_p48 = result;
    if (!(condition_is_above_or_equal)) {
        a3 = result + 16;
        a2 = result;
        a1 = result + 16;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
        result = v_stack_p48;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if ((*(unsigned __int64 *)(v_stack_p50)) == (v_rip - 8824650)) goto loc_0086A9FC;
loc_0086A98E:
    result = ObpReleaseLookupContext(v_stack_p50, a2, a3, a4);
    a1 = (*(unsigned __int64 *)(result + 16)) & (-16);
    a2 = *(unsigned __int64 *)(result + 16) - 16;
    if (a1 <= 16) { a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p58) + 8); }
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 16))) & (2)) != 0) goto loc_0086A9F1;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result + 16))) & (2)) != 0) goto loc_0086A9F1;
loc_0086A9BF:
    result = KeAbPostRelease(result + 16, a2, a3, a4);
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a3, a4);
    result = HalPutDmaAdapter(v_rip - 8824650, a2, a3, a4);
    goto loc_0086A270;
loc_0086A9E3:
    result = ExfReleasePushLock(result + 16, a2, a3, a4);
    goto loc_0086A8D6;
loc_0086A9F1:
    result = ExfReleasePushLock(result + 16, a2, a3, a4);
    goto loc_0086A9BF;
loc_0086A9FC:
    if (((*(unsigned __int8 *)(result + 27)) & (16)) != 0) goto loc_0086A98E;
    if ((*(unsigned __int64 *)(result + 8)) != 0) goto loc_0086A98E;
    result = HalPutDmaAdapter(v_rip - 8824650, a2, a3, a4);
    goto loc_0086A736;
loc_0086AA16:
    result = ObpDeleteDirectoryName(v_rip - 8824650, a2, a3, a4);
    result = ObpReleaseLookupContext(v_stack_p50, a2, a3, a4);
    goto loc_0086A19D;
loc_0086AA2A:
    result = guard_dispatch_icall(v_stack_p50, a2, a3, a4);
    goto loc_0086A554;
loc_0086AA34:
    *(unsigned __int8 *)(result + 10) = 1;
    goto loc_0086A736;
}
```

## 5. (Beta) C Style

```c
int64_t ObCloseHandleTableEntry(void *Arg1, void *Arg2, int64_t Arg3, int64_t Arg4, uint8_t Arg5, uint8_t Arg6)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint8_t v_stack_m117;
    uint8_t v_stack_m118;
    uint8_t v_stack_m128;
    uint32_t v_stack_m148;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint64_t v_stack_m88;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_p0;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint8_t v_stack_p31;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;
    uint64_t v_stack_p60;
    uint8_t v_stack_p65;

    local_rsp = (local_rsp) - (264);
    result = (*(uint64_t *)(v_rip + 0x5A0900)) ^ (local_rsp);
    v_stack_m58 = result;
    v_stack_m108 = Arg3;
    v_stack_mB8 = v_xmm0;
    v_stack_mA8 = v_xmm0;
    v_stack_m98 = v_xmm0;
    result = ExGetHandlePointer(Arg2, Arg2, Arg3, Arg4);
    Arg1 = (result) >> (8);
    local_rbx = 0;
    Arg2 = ((uint8_t)(Arg1)) ^ (*(uint8_t *)(result + 0x18));
    v_stack_m117 = 0;
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0x75CFB5));
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x869E89 + arg2 * 8 + 0xFC7800) + 0xA8)) != 0) goto loc_0086A502;
loc_00869EB4:
    result = (*(uint64_t *)(arg2)) >> (17);
    v_stack_m100 = result;
    if ((((uint8_t)(result)) & (1)) != 0) goto loc_0086A62B;
loc_00869ECD:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x75CC3D)))) & (64)) == 0) goto loc_00869EFB;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x75CC3D));
    if (Arg3 == (*(uint64_t *)(v_rip + 0x75CBD2))) {
        result = 0x80000000ULL;
        Arg2 = (Arg4) | (result);
    }
    result = EtwpTraceHandle((uint32_t)(0x1121ULL), Arg2, result + 48, *(uint64_t *)(v_rip - 0x869E89 + arg2 * 8 + 0xFC7800));
loc_00869EFB:
    if (Arg6 != 0) goto loc_0086A584;
    if ((*(uint64_t *)(arg1 + 0x60)) != 0) {
        Arg2 = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg4 = -1 + 3;
        Arg3 = Arg4;
        Arg1 = Arg1;
        result = ExpUpdateDebugInfo(Arg1, Arg2, Arg3, Arg4);
    }
    result = (*(uint64_t *)(arg2)) >> (1);
    local_r13 = 0;
    v_stack_mE0 = result;
    *(uint64_t *)(arg2) = 0;
    if ((*(uint64_t *)(arg1 + 0x30)) != 0) {
        Arg2 = 0;
        result = ExfUnblockPushLock(Arg1 + 48, Arg2, Arg3, Arg4);
    }
    v_stack_m110 = Arg4;
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) & (0xFFFFFFFCULL));
    v_stack_m110 = (uint32_t)(result);
    if ((*(uint32_t *)(arg1 + 0x4)) == 0) goto loc_00869F7B;
    result = ExpGetHandleExtraInfo(Arg1, v_stack_m110, Arg3, Arg4);
    if (result != 0) {
        *(uint64_t *)(result) = 0;
    }
    *(uint64_t *)(arg2 + 0x8) = 0;
    result = (uint8_t)((*(uint8_t *)(arg1 + 0x2C)) & (1));
    v_stack_m118 = (uint8_t)(result);
    if (condition_is_not_equal) goto loc_0086A565;
loc_00869F99:
    Arg3 = 0;
    local_rbx = ((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(gs_base + (0 + 0x1A4)))))) + 1;
    Arg2 = 0;
    local_rbx = (local_rbx) << (6);
    local_rbx = (local_rbx) + (Arg1);
    result = KeAbPreAcquire(local_rbx, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rbx;
        Arg2 = result;
        Arg1 = local_rbx;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (v_stack_m118 != 0) goto loc_0086A4E8;
    *(uint64_t *)(arg2 + 0x8) = *(uint64_t *)(local_rbx + 0x8);
    if (*(uint64_t *)(local_rbx + 0x8) == 0) {
        *(void **)(local_rbx + 0x10) = Arg2;
    }
    *(void **)(local_rbx + 0x8) = Arg2;
loc_00869FF6:
    result = (uint8_t)((-1) & (6));
    if (((uint8_t)(result)) == 2) goto loc_0086A5D3;
loc_0086A00B:
    result = KeAbPostRelease(local_rbx, Arg2, Arg3, Arg4);
loc_0086A018:
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    local_r14 = Arg4;
    if (((v_stack_m100) & (4)) != 0) {
        Arg1 = v_stack_mD8;
        v_stack_mD8 = v_xmm0;
        v_stack_mC8 = v_xmm0;
        result = SeCaptureSubjectContext(Arg1, Arg2, Arg3, Arg4);
        local_r14 = (Arg4) & (-4);
        v_stack_m128 = 1;
        Arg2 = local_r14;
        Arg4 = result + 48;
        Arg3 = v_stack_mD8;
        Arg1 = v_rip - 8817851;
        result = SepAdtCloseObjectAuditAlarm(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_mD8;
        result = SeReleaseSubjectContext(Arg1, Arg2, Arg3, Arg4);
    }
    result = (result) >> (8);
    Arg1 = ((uint8_t)(result)) ^ (*(uint8_t *)(result + 0x18));
    Arg1 = (Arg1) ^ (*(uint8_t *)(v_rip + 0x75CDBF));
    v_stack_m88 = v_xmm0;
    v_stack_m78 = v_xmm0;
    v_stack_m68 = v_xmm0;
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip - 0x86A097 + arg1 * 8 + 0xFC7800) + 0x42))) & (16)) != 0) goto loc_0086A31E;
    if ((((uint8_t)(*(uint8_t *)(result + 0x1B))) & (8)) != 0) goto loc_0086A31E;
loc_0086A0D0:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x86A097 + arg1 * 8 + 0xFC7800) + 0x80)) == 0) goto loc_0086A171;
    v_stack_m118 = 0;
    v_stack_m110 = 0;
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    local_r10 = v_stack_m108;
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) != v_stack_m108) {
        Arg1 = v_stack_m108;
        v_stack_m118 = 1;
        result = PsGetProcessServerSilo(Arg1, Arg2, Arg3, Arg4);
        Arg1 = result;
        result = PsAttachSiloToCurrentThread(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_m108;
        Arg2 = v_stack_m88;
        v_stack_m110 = result;
        result = KeStackAttachProcess(Arg1, Arg2, Arg3, Arg4);
        local_r10 = v_stack_m108;
    }
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x86A097 + arg1 * 8 + 0xFC7800) + 0x80)) != (v_rip - 26218)) goto loc_0086A1F4;
    result = CmpCloseKeyObject(local_r10, result + 48, 0, -1);
loc_0086A155:
    if (v_stack_m118 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m88;
        result = KiUnstackDetachProcess(Arg1, Arg2, 0, -1);
        Arg1 = v_stack_m110;
        result = PsDetachSiloFromCurrentThread(Arg1, Arg2, 0, -1);
    }
    if (-1 != 1) goto loc_0086A19D;
    if ((((uint8_t)(*(uint8_t *)(result + 0x1A))) & (2)) == 0) goto loc_0086A19D;
    result = (uint32_t)((*(uint8_t *)(result + 0x1A)) & (3));
    local_rbx = (result) - (*(uint8_t *)(result + v_rip - 0x86A189 * 1 + 0xF0FF80));
    if (condition_is_not_equal) goto loc_0086A270;
loc_0086A19D:
    result = *(uint8_t *)(result + v_rip - 0x86A189 * 1 + 0xF0FF80);
    if (v_stack_m117 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_mB8;
        result = KiUnstackDetachProcess(Arg1, Arg2, 0, -1);
    }
    local_r15 = (uint16_t)(v_stack_mE0);
    if ((uint32_t)((uint16_t)(v_stack_mE0)) != 0) {
        local_r15 = (uint32_t)(-((uint16_t)(v_stack_mE0)));
        result = (int32_t)((uint32_t)(local_r15));
    }
    result = ObfDereferenceObjectWithTag(result + 48, (uint32_t)(0x6E48624FULL), 0, -1);
    result = 0;
loc_0086A1D3:
    Arg1 = (v_stack_m58) ^ (local_rsp);
    result = _security_check_cookie(Arg1, (uint32_t)(0x6E48624FULL), 0, -1);
    local_rsp = (local_rsp) + (264);
    return result;
loc_0086A1F4:
    if (result != (v_rip + 1715381)) goto loc_0086A43D;
    if (local_rbx != 1) goto loc_0086A155;
    if ((((uint8_t)(*(uint8_t *)(result + 0x92))) & (2)) == 0) goto loc_0086A25B;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x695620), v_rip - 8755615, 0, -1);
    if ((uint8_t)(result) != 0) {
        result = *(uint64_t *)(result + 0x50);
        Arg2 = v_rip - 8755635;
        Arg1 = *(uint64_t *)(v_rip + 0x6955FE);
        result = (result) + (40);
        v_stack_p28 = result;
        Arg4 = (uint32_t)(local_rbx);
        Arg3 = 0;
        v_stack_p20 = 0;
        result = EtwpEventWriteTemplateSessAndProv(Arg1, Arg2, Arg3, Arg4);
    }
    goto loc_0086A155;
loc_0086A270:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result + 16, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = result + 16;
        Arg2 = result;
        Arg1 = result + 16;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (*(uint64_t *)(local_rbx) == 0) goto loc_0086A477;
    if (((*(uint8_t *)(result + 0x1B)) & (16)) != 0) goto loc_0086A2D3;
    if ((*(uint64_t *)(result + 0x8)) == 0) goto loc_0086A6DC;
loc_0086A2D3:
    Arg1 = (*(uint64_t *)(result + 0x10)) & (-16);
    Arg2 = *(uint64_t *)(result + 0x10) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(result + 0x10))) & (2)) != 0) goto loc_0086A4A2;
    if ((((uint8_t)(*(uint64_t *)(result + 0x10))) & (2)) != 0) goto loc_0086A4A2;
loc_0086A302:
    result = KeAbPostRelease(result + 16, Arg2, Arg3, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    goto loc_0086A19D;
loc_0086A31E:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result + 16, Arg2, Arg3, Arg4);
    v_stack_p48 = result;
    if (!(condition_is_above_or_equal)) {
        Arg3 = result + 16;
        Arg2 = result;
        Arg1 = result + 16;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
        result = v_stack_p48;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (0 != 1) goto loc_0086A3A0;
    result = *(uint8_t *)(result + 0x1B);
    if ((((uint8_t)(*(uint8_t *)(result + 0x1B))) & (8)) != 0) {
        result = *(uint8_t *)(result + 0x1A);
        Arg1 = result;
        result = (uint32_t)((result) & (31));
        result = *(uint8_t *)(result + v_rip - 0x86A37A * 1 + 0xF0FF80);
        Arg1 = (Arg1) - (result);
        *(uint64_t *)(arg1) = 0;
    }
    if ((((uint8_t)(*(uint8_t *)(*(uint64_t *)(v_rip - 0x86A097 + arg1 * 8 + 0xFC7800) + 0x42))) & (16)) == 0) goto loc_0086A6B8;
    if ((((uint8_t)(*(uint8_t *)(result + 0x1A))) & (4)) != 0) goto loc_0086A461;
loc_0086A3BC:
    if (((*(uint8_t *)(result + 0x1B)) & (64)) == 0) goto loc_0086A4B0;
    local_rsi = (uint32_t)(((uint32_t)(*(uint32_t *)(0 + 0x8))) & (0xFFFFFFULL));
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x8)))) - 1) ^ ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x8)))))));
    result = (uint32_t)((result) & (0xFFFFFFULL));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(0 + 0x8)))))));
    *(uint32_t *)(0 + 0x8) = (uint32_t)(result);
loc_0086A3E0:
    if ((*(uint8_t *)(0 + 0xB)) != 0) goto loc_0086A3F2;
    if (((*(uint32_t *)(0 + 0x8)) & (0xFFFFFFULL)) == 0) {
        *(uint64_t *)(0) = 0;
    }
    Arg1 = (*(uint64_t *)(result + 0x10)) & (-16);
    Arg3 = *(uint64_t *)(result + 0x10) - 16;
    if (Arg1 <= 16) { Arg3 = 0; }
    if ((((uint8_t)(*(uint64_t *)(result + 0x10))) & (2)) != 0) goto loc_0086A5B0;
    if ((((uint8_t)(*(uint64_t *)(result + 0x10))) & (2)) != 0) goto loc_0086A5B0;
loc_0086A422:
    result = KeAbPostRelease(result + 16, result + 16, Arg3, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), result + 16, Arg3, Arg4);
    goto loc_0086A0D0;
loc_0086A43D:
    if (result != (v_rip - 25476)) goto loc_0086A5C9;
    result = IopCloseFile(local_r10, result + 48, Arg3, *(uint64_t *)(result + 0x8));
    goto loc_0086A155;
loc_0086A461:
    result = (uint32_t)((result) & (7));
    Arg2 = (result) - (*(uint8_t *)(result + result + 0x30 * 1 + 0xF0FF80));
    goto loc_0086A3BC;
loc_0086A477:
    Arg1 = (*(uint64_t *)(result + 0x10)) & (-16);
    Arg2 = *(uint64_t *)(result + 0x10) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(result + 0x10))) & (2)) != 0) goto loc_0086A4A2;
    if ((((uint8_t)(*(uint64_t *)(result + 0x10))) & (2)) == 0) goto loc_0086A302;
loc_0086A4A2:
    result = ExfReleasePushLock(result + 16, Arg2, Arg3, *(uint64_t *)(result + 0x8));
    goto loc_0086A302;
loc_0086A4B0:
loc_0086A4C0:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2)))) == 0) goto loc_0086A5C1;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x8 + 0x8))))) & (0xFFFFFFULL));
    if (condition_is_equal) goto loc_0086A4E0;
    if ((*(uint64_t *)(*(uint64_t *)(arg2) + 0x8)) == v_stack_p40) goto loc_0086A56D;
loc_0086A4E0:
    Arg2 = (*(uint64_t *)(arg2) + 8) + (16);
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2)))) - 1);
    goto loc_0086A4C0;
loc_0086A4E8:
    if (*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x10) == 0) goto loc_0086A622;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x10) + 0x8) = *(uint64_t *)(local_rbx);
loc_0086A4F9:
    *(uint64_t *)(*(uint64_t *)(result + 0x8) + 0x10) = *(uint64_t *)(local_rbx);
    goto loc_00869FF6;
loc_0086A502:
    result = *(uint64_t *)(gs_base + (0 + 0x188));
    local_rbx = *(uint64_t *)(result + 0x8);
    if ((*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8)) != 0) {
        Arg2 = v_stack_mB8;
        Arg1 = 0;
        result = KeStackAttachProcess(Arg1, Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x8 + 0x8)), *(uint64_t *)(result + 0x8));
        local_rbx = 1;
        local_r10 = result + 48;
        v_stack_p31 = (uint8_t)(local_rbx);
    }
    if ((*(uint64_t *)(local_rsi + 0xA8)) != (v_rip + 633704)) goto loc_0086AA2A;
    result = ExpWin32OkayToCloseProcedure(0, local_r10, *(uint64_t *)(v_rip - 0x86A097 + arg1 * 8 + 0xFC7800), Arg5);
loc_0086A554:
    if ((uint8_t)(result) == 0) goto loc_0086A5E0;
    goto loc_00869EB4;
loc_0086A565:
    goto loc_00869F99;
loc_0086A56D:
    result = (uint32_t)((*(uint64_t *)(v_rip - 0x86A097 + arg1 * 8 + 0xFC7800) - 1) ^ ((uint32_t)(*(uint64_t *)(v_rip - 0x86A097 + arg1 * 8 + 0xFC7800))));
    result = (uint32_t)((result) & (0xFFFFFFULL));
    result = (uint32_t)((result) ^ ((uint32_t)(*(uint64_t *)(v_rip - 0x86A097 + arg1 * 8 + 0xFC7800))));
    *(uint32_t *)(local_r10 + 0x8) = (uint32_t)(result);
    goto loc_0086A3E0;
loc_0086A584:
    local_rbx = (*(uint64_t *)(*(uint64_t *)(local_rbx))) >> (1);
    local_r13 = 0;
    *(uint64_t *)(*(uint64_t *)(local_rbx)) = 0;
    if ((*(uint64_t *)(local_r15 + 0x30)) == 0) goto loc_0086A018;
    Arg2 = 0;
    result = ExfUnblockPushLock(local_r15 + 48, Arg2, *(uint64_t *)(v_rip - 0x86A097 + arg1 * 8 + 0xFC7800), Arg5);
    goto loc_0086A018;
loc_0086A5B0:
    result = ExfReleasePushLock(0, Arg2, *(uint64_t *)(v_rip - 0x86A097 + arg1 * 8 + 0xFC7800), Arg5);
    goto loc_0086A422;
loc_0086A5C1:
    goto loc_0086A3E0;
loc_0086A5C9:
    result = guard_dispatch_icall(0, result + 16, *(uint64_t *)(v_rip - 0x86A097 + arg1 * 8 + 0xFC7800), Arg5);
    goto loc_0086A155;
loc_0086A5D3:
    result = ExfTryToWakePushLock(local_rbx, result + 16, *(uint64_t *)(v_rip - 0x86A097 + arg1 * 8 + 0xFC7800), Arg5);
    goto loc_0086A00B;
loc_0086A5E0:
    if ((*(uint64_t *)(local_r15 + 0x30)) != 0) {
        Arg2 = 0;
        result = ExfUnblockPushLock(local_r15 + 48, Arg2, *(uint64_t *)(v_rip - 0x86A097 + arg1 * 8 + 0xFC7800), Arg5);
    }
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, *(uint64_t *)(v_rip - 0x86A097 + arg1 * 8 + 0xFC7800), Arg5);
    if ((uint8_t)(local_rbx) != 0) {
        Arg2 = 0;
        Arg1 = v_stack_mB8;
        result = KiUnstackDetachProcess(Arg1, Arg2, *(uint64_t *)(v_rip - 0x86A097 + arg1 * 8 + 0xFC7800), Arg5);
    }
    goto loc_0086A1D3;
loc_0086A622:
    *(uint64_t *)(local_rbx + 0x8) = *(uint64_t *)(local_rbx);
    goto loc_0086A4F9;
loc_0086A62B:
    if ((uint8_t)(local_rbx) != 0) goto loc_00869ECD;
    if (Arg5 == ((uint8_t)(local_rbx))) goto loc_0086A6C0;
    result = ExUnlockHandleTableEntry(local_r15, *(uint64_t *)(local_rbx), *(uint64_t *)(v_rip - 0x86A097 + arg1 * 8 + 0xFC7800), Arg5);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(local_rbx), *(uint64_t *)(v_rip - 0x86A097 + arg1 * 8 + 0xFC7800), Arg5);
    if (v_stack_p31 != ((uint8_t)(local_rbx))) {
        Arg2 = 0;
        Arg1 = v_stack_mB8;
        result = KiUnstackDetachProcess(Arg1, Arg2, *(uint64_t *)(v_rip - 0x86A097 + arg1 * 8 + 0xFC7800), Arg5);
    }
    if ((*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x24A)) == 1) goto loc_0086A618;
    if (((*(uint32_t *)(v_rip + 0x759C3E)) & (0x400000ULL)) != 0) goto loc_0086A6A9;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x308)) != 0) goto loc_0086A6A9;
    if ((*(uint64_t *)(local_r15 + 0x60)) == 0) goto loc_0086A618;
loc_0086A6A9:
    result = KeRaiseUserException((uint32_t)(0xC0000235ULL), Arg2, *(uint64_t *)(v_rip - 0x86A097 + arg1 * 8 + 0xFC7800), Arg5);
    goto loc_0086A1D3;
loc_0086A6B8:
    goto loc_0086A3F2;
loc_0086A6C0:
    local_r13 = 0;
    Arg4 = 0;
    Arg3 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(147, *(uint64_t *)(v_rip - 0x86A097 + arg1 * 8 + 0xFC7800), Arg3, Arg4);
loc_0086A6DC:
    result = 0;
    v_stack_p60 = 0;
    Arg2 = 0;
    v_stack_p50 = v_xmm0;
    v_stack_p50 = *(uint64_t *)(local_rbx);
    v_stack_p65 = 1;
    result = KeAbPreAcquire(*(uint64_t *)(local_rbx) + 296, Arg2, Arg2 + 1, Arg4);
    if (condition_is_below) goto loc_0086A884;
    if (result != 0) goto loc_0086AA34;
loc_0086A736:
    if ((*(uint32_t *)(local_rbx + 0x18)) != 0) goto loc_0086A87C;
    result = (result) >> (8);
    Arg1 = ((uint8_t)(result)) ^ (*(uint8_t *)(result + 0x18));
    Arg1 = (Arg1) ^ (*(uint8_t *)(v_rip + 0x75C6ED));
    result = *(uint64_t *)(v_rip + 0x6A4EEF);
    if ((*(uint64_t *)(v_rip - 0x86A74A + arg1 * 8 + 0xFC7800)) == (*(uint64_t *)(v_rip + 0x6A4EEF))) {
        Arg1 = result + 48;
        result = ObpDeleteSymbolicLinkName(Arg1, Arg2, Arg2 + 1, Arg4);
    }
    Arg2 = 0;
    result = ObpLookupDirectoryEntry(local_rbx + 8, Arg2, v_stack_p50, Arg4);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_p58) + 0x8)) - (48);
    result = (uint32_t)((*(uint8_t *)(arg1 + 0x1A)) & (3));
    Arg1 = (Arg1) - (*(uint8_t *)(result + v_rip - 0x86A74A * 1 + 0xF0FF80));
    *(uint64_t *)(arg1) = 0;
    *(uint64_t *)(v_stack_p58) = *(uint64_t *)(*(uint64_t *)(v_stack_p58));
    *(uint64_t *)(*(uint64_t *)(v_stack_p58)) = 0;
loc_0086A7BB:
    Arg1 = (*(uint64_t *)(result + 0x10)) & (-16);
    Arg2 = *(uint64_t *)(result + 0x10) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(result + 0x10))) & (2)) != 0) goto loc_0086A86E;
    if ((((uint8_t)(*(uint64_t *)(result + 0x10))) & (2)) != 0) goto loc_0086A86E;
loc_0086A7EA:
    result = KeAbPostRelease(result + 16, Arg2, v_stack_p50, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, v_stack_p50, Arg4);
    if (*(uint64_t *)(v_stack_p58) == 0) goto loc_0086A85F;
    result = ObpUnlockDirectory(v_stack_p50, Arg2, v_stack_p50, Arg4);
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(v_stack_p58), Arg2, v_stack_p50, Arg4);
    result = ObfDereferenceObjectWithTag(v_stack_p50, (uint32_t)(0x6944624FULL), v_stack_p50, Arg4);
    Arg2 = (*(uint64_t *)(*(uint64_t *)(v_stack_p58) + 0x8) - 48) >> (8);
    Arg2 = (uint8_t)((Arg2) ^ (*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_p58) + 0x8) - 0x18)));
    Arg2 = (uint8_t)((Arg2) ^ (*(uint8_t *)(v_rip + 0x75C600)));
    if (((uint8_t)(Arg2)) == (*(uint8_t *)(*(uint64_t *)(v_rip + 0x6A4E19) + 0x28))) goto loc_0086AA16;
    result = ObfDereferenceObjectWithTag(*(uint64_t *)(*(uint64_t *)(v_stack_p58) + 0x8), (uint32_t)(0x6944624FULL), v_stack_p50, Arg4);
loc_0086A85F:
    result = ObpReleaseLookupContext(v_stack_p50, (uint32_t)(0x6944624FULL), v_stack_p50, Arg4);
    goto loc_0086A19D;
loc_0086A86E:
    result = ExfReleasePushLock(result + 16, (uint32_t)(0x6944624FULL), v_stack_p50, Arg4);
    goto loc_0086A7EA;
loc_0086A87C:
    goto loc_0086A7BB;
loc_0086A884:
    if (result != 0) {
        Arg2 = result;
        result = KeAbPostReleaseEx(result + 16, Arg2, v_stack_p50, Arg4);
    }
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, v_stack_p50, Arg4);
    result = ObfReferenceObject(v_rip - 8824650, Arg2, v_stack_p50, Arg4);
    Arg1 = (*(uint64_t *)(result + 0x10)) & (-16);
    Arg2 = *(uint64_t *)(result + 0x10) - 16;
    if (Arg1 <= 16) { Arg2 = *(uint64_t *)(*(uint64_t *)(v_stack_p58) + 0x8); }
    if ((((uint8_t)(*(uint64_t *)(result + 0x10))) & (2)) != 0) goto loc_0086A9E3;
    if ((((uint8_t)(*(uint64_t *)(result + 0x10))) & (2)) != 0) goto loc_0086A9E3;
loc_0086A8D6:
    result = KeAbPostRelease(result + 16, Arg2, v_stack_p50, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, v_stack_p50, Arg4);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip - 8824650 + 296, Arg2, Arg3, Arg4);
    v_stack_p48 = result;
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip - 8824650 + 296;
        Arg2 = result;
        result = ExfAcquirePushLockExclusiveEx(v_rip - 8824650 + 296, Arg2, Arg3, Arg4);
        result = v_stack_p48;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result + 16, Arg2, Arg3, Arg4);
    v_stack_p48 = result;
    if (!(condition_is_above_or_equal)) {
        Arg3 = result + 16;
        Arg2 = result;
        Arg1 = result + 16;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
        result = v_stack_p48;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if ((*(uint64_t *)(v_stack_p50)) == (v_rip - 8824650)) goto loc_0086A9FC;
loc_0086A98E:
    result = ObpReleaseLookupContext(v_stack_p50, Arg2, Arg3, Arg4);
    Arg1 = (*(uint64_t *)(result + 0x10)) & (-16);
    Arg2 = *(uint64_t *)(result + 0x10) - 16;
    if (Arg1 <= 16) { Arg2 = *(uint64_t *)(*(uint64_t *)(v_stack_p58) + 0x8); }
    if ((((uint8_t)(*(uint64_t *)(result + 0x10))) & (2)) != 0) goto loc_0086A9F1;
    if ((((uint8_t)(*(uint64_t *)(result + 0x10))) & (2)) != 0) goto loc_0086A9F1;
loc_0086A9BF:
    result = KeAbPostRelease(result + 16, Arg2, Arg3, Arg4);
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg3, Arg4);
    result = HalPutDmaAdapter(v_rip - 8824650, Arg2, Arg3, Arg4);
    goto loc_0086A270;
loc_0086A9E3:
    result = ExfReleasePushLock(result + 16, Arg2, Arg3, Arg4);
    goto loc_0086A8D6;
loc_0086A9F1:
    result = ExfReleasePushLock(result + 16, Arg2, Arg3, Arg4);
    goto loc_0086A9BF;
loc_0086A9FC:
    if (((*(uint8_t *)(result + 0x1B)) & (16)) != 0) goto loc_0086A98E;
    if ((*(uint64_t *)(result + 0x8)) != 0) goto loc_0086A98E;
    result = HalPutDmaAdapter(v_rip - 8824650, Arg2, Arg3, Arg4);
    goto loc_0086A736;
loc_0086AA16:
    result = ObpDeleteDirectoryName(v_rip - 8824650, Arg2, Arg3, Arg4);
    result = ObpReleaseLookupContext(v_stack_p50, Arg2, Arg3, Arg4);
    goto loc_0086A19D;
loc_0086AA2A:
    result = guard_dispatch_icall(v_stack_p50, Arg2, Arg3, Arg4);
    goto loc_0086A554;
loc_0086AA34:
    *(uint8_t *)(result + 0xA) = 1;
    goto loc_0086A736;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x2C` | `8` | `R` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x60` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R/W` |
| `Arg2` | `+ 0x0` | `64` | `W` |
| `Arg2` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00869E20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
