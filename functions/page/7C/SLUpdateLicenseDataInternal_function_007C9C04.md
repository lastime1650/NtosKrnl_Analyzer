# SLUpdateLicenseDataInternal

- RVA: `0x007C9C04`–`0x007CAA9C` (길이 `3,736` bytes)
- VA: `0x00000001407C9C04`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D4F18`
- 디코드: `888`개 명령, `3,736/3,736` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **79**; 고유 호출 대상: **33**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x007C9D7E` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007C9D9E` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x007C9DC6` → [ExpReducedLicenseData](../AB/ExpReducedLicenseData_function_00AB79C0.md) (function, `0x00AB79C0`)
- `0x007C9E4F` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x007C9E77` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x007C9EA7` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x007C9EAF` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x007C9EB4` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x007C9EF2` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007C9F0B` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x007C9F24` → [ExpGetLicenseTamperState](../../text/65/ExpGetLicenseTamperState_function_00657740.md) (function, `0x00657740`)
- `0x007C9FB1` → [ExpLicUpdateChecksum](../../text/65/ExpLicUpdateChecksum_function_006578AC.md) (function, `0x006578AC`)
- `0x007C9FE7` → [ExpLicUpdateChecksum](../../text/65/ExpLicUpdateChecksum_function_006578AC.md) (function, `0x006578AC`)
- `0x007CA055` → [sub_00966DF0](../96/Unknown_function_00966DF0.md) (function, `0x00966DF0`)
- `0x007CA072` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x007CA07A` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x007CA07F` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x007CA08C` → [SLSendPolicyChangeNotifications](SLSendPolicyChangeNotifications_function_007C9BDC.md) (function, `0x007C9BDC`)
- `0x007CA117` → [ZwCreateSection](../../text/6A/ZwCreateSection_function_006ADA10.md) (function, `0x006ADA10`)
- `0x007CA152` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x007CA175` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007CA19C` → [MmMapViewInSessionSpace](../98/MmMapViewInSessionSpace_function_00982480.md) (function, `0x00982480`)
- `0x007CA1CC` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007CA1E2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007CA226` → [sub_007C8C1C](Unknown_function_007C8C1C.md) (function, `0x007C8C1C`)
- `0x007CA25E` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007CA27D` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x007CA2BB` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x007CA2C3` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x007CA2C8` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x007CA2EC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007CA31F` → [sub_007C8C1C](Unknown_function_007C8C1C.md) (function, `0x007C8C1C`)
- `0x007CA33F` → [qsort](../../text/50/qsort_function_005009F0.md) (function, `0x005009F0`)
- `0x007CA3AC` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007CA3C8` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x007CA429` → [sub_007C8730](Unknown_function_007C8730.md) (function, `0x007C8730`)
- `0x007CA4B2` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x007CA513` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x007CA51B` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x007CA520` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x007CA530` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x007CA555` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007CA56E` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x007CA604` → [ExpLicUpdateChecksum](../../text/65/ExpLicUpdateChecksum_function_006578AC.md) (function, `0x006578AC`)
- `0x007CA63A` → [ExpLicUpdateChecksum](../../text/65/ExpLicUpdateChecksum_function_006578AC.md) (function, `0x006578AC`)
- `0x007CA6BB` → [sub_00966DF0](../96/Unknown_function_00966DF0.md) (function, `0x00966DF0`)
- `0x007CA6EB` → [PsGetCurrentServerSilo](../../text/22/PsGetCurrentServerSilo_function_00225710.md) (function, `0x00225710`)
- `0x007CA6F3` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (function, `0x00443B30`)
- `0x007CA709` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007CA737` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007CA75B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007CA776` → [ExpGetLicenseTamperState](../../text/65/ExpGetLicenseTamperState_function_00657740.md) (function, `0x00657740`)
- `0x007CA79A` → [ExpSetLicenseTamperState](../../text/65/ExpSetLicenseTamperState_function_00657AC4.md) (function, `0x00657AC4`)
- `0x007CA7A7` → [ExpGetLicenseTamperState](../../text/65/ExpGetLicenseTamperState_function_00657740.md) (function, `0x00657740`)
- `0x007CA7EC` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x007CA7F4` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x007CA7F9` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x007CA815` → [sub_007C8D5C](Unknown_function_007C8D5C.md) (function, `0x007C8D5C`)
- `0x007CA834` → [SLSendPolicyChangeNotifications](SLSendPolicyChangeNotifications_function_007C9BDC.md) (function, `0x007C9BDC`)
- `0x007CA8B9` → [sub_007C7F80](Unknown_function_007C7F80.md) (function, `0x007C7F80`)
- `0x007CA8E9` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007CA905` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x007CA946` → [sub_00966DF0](../96/Unknown_function_00966DF0.md) (function, `0x00966DF0`)
- `0x007CA95C` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x007CA964` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x007CA969` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x007CA97E` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x007CA98B` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x007CA9A3` → [MiRemoveFromSystemSpace](../../text/29/MiRemoveFromSystemSpace_function_002962FC.md) (function, `0x002962FC`)
- `0x007CA9BB` → [MiRemoveFromSystemSpace](../../text/29/MiRemoveFromSystemSpace_function_002962FC.md) (function, `0x002962FC`)
- `0x007CA9CA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007CAA08` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007CAA21` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x007CAA37` → [ExpGetLicenseTamperState](../../text/65/ExpGetLicenseTamperState_function_00657740.md) (function, `0x00657740`)
- `0x007CAA4B` → [ExpSetLicenseTamperState](../../text/65/ExpSetLicenseTamperState_function_00657AC4.md) (function, `0x00657AC4`)
- `0x007CAA65` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (function, `0x00265DD0`)
- `0x007CAA6D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x007CAA72` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (function, `0x0025D8B0`)
- `0x007CAA7F` → [SLSendPolicyChangeNotifications](SLSendPolicyChangeNotifications_function_007C9BDC.md) (function, `0x007C9BDC`)

### Direct callers
- [sub_009669C4](../96/Unknown_function_009669C4.md) at `0x00966C28`
- [ExUpdateLicenseData](../AB/ExUpdateLicenseData_function_00AB3160.md) at `0x00AB3190`

### Static image references
- `0x007CA32C` → RVA `0x007C8730` (`PAGE`; read)
- `0x007CA8B2` → RVA `0x000232F8` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **65**
  - `0x007C9D7E` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007C9D9E` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x007C9E4F` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (`PAGE` → `.text`)
  - `0x007C9E77` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (`PAGE` → `.text`)
  - `0x007C9EA7` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x007C9EAF` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x007C9EB4` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x007C9EF2` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007C9F0B` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x007C9F24` → [ExpGetLicenseTamperState](../../text/65/ExpGetLicenseTamperState_function_00657740.md) (`PAGE` → `.text`)
  - `0x007C9FB1` → [ExpLicUpdateChecksum](../../text/65/ExpLicUpdateChecksum_function_006578AC.md) (`PAGE` → `.text`)
  - `0x007C9FE7` → [ExpLicUpdateChecksum](../../text/65/ExpLicUpdateChecksum_function_006578AC.md) (`PAGE` → `.text`)
  - `0x007CA072` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x007CA07A` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x007CA07F` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x007CA117` → [ZwCreateSection](../../text/6A/ZwCreateSection_function_006ADA10.md) (`PAGE` → `.text`)
  - `0x007CA175` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007CA1CC` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007CA1E2` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007CA25E` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007CA27D` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x007CA2BB` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x007CA2C3` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x007CA2C8` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x007CA2EC` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007CA33F` → [qsort](../../text/50/qsort_function_005009F0.md) (`PAGE` → `.text`)
  - `0x007CA3AC` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007CA3C8` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x007CA4B2` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x007CA513` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x007CA51B` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x007CA520` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x007CA530` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x007CA555` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007CA56E` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x007CA604` → [ExpLicUpdateChecksum](../../text/65/ExpLicUpdateChecksum_function_006578AC.md) (`PAGE` → `.text`)
  - `0x007CA63A` → [ExpLicUpdateChecksum](../../text/65/ExpLicUpdateChecksum_function_006578AC.md) (`PAGE` → `.text`)
  - `0x007CA6EB` → [PsGetCurrentServerSilo](../../text/22/PsGetCurrentServerSilo_function_00225710.md) (`PAGE` → `.text`)
  - `0x007CA6F3` → [PsIsHostSilo](../../text/44/PsIsHostSilo_function_00443B30.md) (`PAGE` → `.text`)
  - `0x007CA709` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007CA737` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007CA75B` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007CA776` → [ExpGetLicenseTamperState](../../text/65/ExpGetLicenseTamperState_function_00657740.md) (`PAGE` → `.text`)
  - `0x007CA79A` → [ExpSetLicenseTamperState](../../text/65/ExpSetLicenseTamperState_function_00657AC4.md) (`PAGE` → `.text`)
  - `0x007CA7A7` → [ExpGetLicenseTamperState](../../text/65/ExpGetLicenseTamperState_function_00657740.md) (`PAGE` → `.text`)
  - `0x007CA7EC` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x007CA7F4` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x007CA7F9` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x007CA8E9` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007CA905` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x007CA95C` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x007CA964` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x007CA969` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
  - `0x007CA97E` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x007CA98B` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x007CA9A3` → [MiRemoveFromSystemSpace](../../text/29/MiRemoveFromSystemSpace_function_002962FC.md) (`PAGE` → `.text`)
  - `0x007CA9BB` → [MiRemoveFromSystemSpace](../../text/29/MiRemoveFromSystemSpace_function_002962FC.md) (`PAGE` → `.text`)
  - `0x007CA9CA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007CAA08` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007CAA21` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x007CAA37` → [ExpGetLicenseTamperState](../../text/65/ExpGetLicenseTamperState_function_00657740.md) (`PAGE` → `.text`)
  - `0x007CAA4B` → [ExpSetLicenseTamperState](../../text/65/ExpSetLicenseTamperState_function_00657AC4.md) (`PAGE` → `.text`)
  - `0x007CAA65` → [ExfTryToWakePushLock](../../text/26/ExfTryToWakePushLock_function_00265DD0.md) (`PAGE` → `.text`)
  - `0x007CAA6D` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x007CAA72` → [KeLeaveCriticalRegion](../../text/25/KeLeaveCriticalRegion_function_0025D8B0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007C9C04  4C 8B DC                        mov r11, rsp
007C9C07  49 89 4B 08                     mov qword ptr [r11 + 8], rcx
007C9C0B  53                              push rbx
007C9C0C  56                              push rsi
007C9C0D  57                              push rdi
007C9C0E  41 54                           push r12
007C9C10  41 55                           push r13
007C9C12  41 56                           push r14
007C9C14  41 57                           push r15
007C9C16  48 81 EC D0 01 00 00            sub rsp, 0x1d0
007C9C1D  49 8B F8                        mov rdi, r8
007C9C20  44 8B C2                        mov r8d, edx
007C9C23  4C 8B F9                        mov r15, rcx
007C9C26  33 C9                           xor ecx, ecx
007C9C28  88 4C 24 46                     mov byte ptr [rsp + 0x46], cl
007C9C2C  88 4C 24 44                     mov byte ptr [rsp + 0x44], cl
007C9C30  88 8C 24 20 02 00 00            mov byte ptr [rsp + 0x220], cl
007C9C37  49 89 8B 88 FE FF FF            mov qword ptr [r11 - 0x178], rcx
007C9C3E  33 C0                           xor eax, eax
007C9C40  0F 57 C0                        xorps xmm0, xmm0
007C9C43  0F 11 84 24 28 01 00 00         movups xmmword ptr [rsp + 0x128], xmm0
007C9C4B  0F 11 84 24 38 01 00 00         movups xmmword ptr [rsp + 0x138], xmm0
007C9C53  49 89 83 40 FF FF FF            mov qword ptr [r11 - 0xc0], rax
007C9C5A  89 84 24 50 01 00 00            mov dword ptr [rsp + 0x150], eax
007C9C61  49 89 8B 80 FE FF FF            mov qword ptr [r11 - 0x180], rcx
007C9C68  48 89 4C 24 68                  mov qword ptr [rsp + 0x68], rcx
007C9C6D  48 89 8C 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rcx
007C9C75  48 89 8C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rcx
007C9C7D  33 F6                           xor esi, esi
007C9C7F  44 8B E6                        mov r12d, esi
007C9C82  48 89 74 24 58                  mov qword ptr [rsp + 0x58], rsi
007C9C87  89 74 24 48                     mov dword ptr [rsp + 0x48], esi
007C9C8B  44 8B EE                        mov r13d, esi
007C9C8E  48 89 74 24 50                  mov qword ptr [rsp + 0x50], rsi
007C9C93  89 74 24 60                     mov dword ptr [rsp + 0x60], esi
007C9C97  89 74 24 74                     mov dword ptr [rsp + 0x74], esi
007C9C9B  0F 11 84 24 58 01 00 00         movups xmmword ptr [rsp + 0x158], xmm0
007C9CA3  0F 11 84 24 68 01 00 00         movups xmmword ptr [rsp + 0x168], xmm0
007C9CAB  0F 11 84 24 78 01 00 00         movups xmmword ptr [rsp + 0x178], xmm0
007C9CB3  48 85 FF                        test rdi, rdi
007C9CB6  0F 84 D4 0B 00 00               je 0x1407ca890
007C9CBC  8D 42 E7                        lea eax, [rdx - 0x19]
007C9CBF  3D E7 3F 01 00                  cmp eax, 0x13fe7
007C9CC4  0F 87 C6 0B 00 00               ja 0x1407ca890
007C9CCA  40 F6 C7 03                     test dil, 3
007C9CCE  0F 85 BC 0B 00 00               jne 0x1407ca890
007C9CD4  8B 0F                           mov ecx, dword ptr [rdi]
007C9CD6  B8 00 40 01 00                  mov eax, 0x14000
007C9CDB  3B C8                           cmp ecx, eax
007C9CDD  0F 87 99 0B 00 00               ja 0x1407ca87c
007C9CE3  8B 57 04                        mov edx, dword ptr [rdi + 4]
007C9CE6  3B D0                           cmp edx, eax
007C9CE8  0F 87 8E 0B 00 00               ja 0x1407ca87c
007C9CEE  44 8B 4F 08                     mov r9d, dword ptr [rdi + 8]
007C9CF2  44 3B C8                        cmp r9d, eax
007C9CF5  0F 87 81 0B 00 00               ja 0x1407ca87c
007C9CFB  4C 8D 67 14                     lea r12, [rdi + 0x14]
007C9CFF  4C 03 E2                        add r12, rdx
007C9D02  41 F6 C4 03                     test r12b, 3
007C9D06  74 1D                           je 0x1407c9d25
007C9D08  41 BE 01 00 00 00               mov r14d, 1
007C9D0E  C7 44 24 40 0D 00 00 C0         mov dword ptr [rsp + 0x40], 0xc000000d
007C9D16  48 83 CB FF                     or rbx, 0xffffffffffffffff
007C9D1A  4C 8B EE                        mov r13, rsi
007C9D1D  4C 8B E6                        mov r12, rsi
007C9D20  E9 7A 0B 00 00                  jmp 0x1407ca89f
007C9D25  8D 42 14                        lea eax, [rdx + 0x14]
007C9D28  41 03 C1                        add eax, r9d
007C9D2B  3B C1                           cmp eax, ecx
007C9D2D  75 D9                           jne 0x1407c9d08
007C9D2F  41 BE 01 00 00 00               mov r14d, 1
007C9D35  41 3B C8                        cmp ecx, r8d
007C9D38  75 D4                           jne 0x1407c9d0e
007C9D3A  44 39 77 10                     cmp dword ptr [rdi + 0x10], r14d
007C9D3E  75 CE                           jne 0x1407c9d0e
007C9D40  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
007C9D44  41 88 B7 08 B7 00 00            mov byte ptr [r15 + 0xb708], sil
007C9D4B  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
007C9D54  48 89 8C 24 88 01 00 00         mov qword ptr [rsp + 0x188], rcx
007C9D5C  0F B7 81 E4 01 00 00            movzx eax, word ptr [rcx + 0x1e4]
007C9D63  66 41 2B C6                     sub ax, r14w
007C9D67  66 89 81 E4 01 00 00            mov word ptr [rcx + 0x1e4], ax
007C9D6E  90                              nop
007C9D6F  49 8D B7 F8 B6 00 00            lea rsi, [r15 + 0xb6f8]
007C9D76  45 33 C0                        xor r8d, r8d
007C9D79  33 D2                           xor edx, edx
007C9D7B  48 8B CE                        mov rcx, rsi
007C9D7E  E8 AD 64 A4 FF                  call 0x140210230
007C9D83  48 8B D8                        mov rbx, rax
007C9D86  41 8D 4E 10                     lea ecx, [r14 + 0x10]
007C9D8A  33 C0                           xor eax, eax
007C9D8C  F0 48 0F B1 0E                  lock cmpxchg qword ptr [rsi], rcx
007C9D91  74 10                           je 0x1407c9da3
007C9D93  4C 8B CE                        mov r9, rsi
007C9D96  4C 8B C3                        mov r8, rbx
007C9D99  33 D2                           xor edx, edx
007C9D9B  48 8B CE                        mov rcx, rsi
007C9D9E  E8 A9 66 A4 FF                  call 0x14021044c
007C9DA3  33 F6                           xor esi, esi
007C9DA5  48 85 DB                        test rbx, rbx
007C9DA8  74 04                           je 0x1407c9dae
007C9DAA  44 88 73 0A                     mov byte ptr [rbx + 0xa], r14b
007C9DAE  49 8B 1F                        mov rbx, qword ptr [r15]
007C9DB1  48 89 5C 24 78                  mov qword ptr [rsp + 0x78], rbx
007C9DB6  0F B6 44 24 44                  movzx eax, byte ptr [rsp + 0x44]
007C9DBB  48 85 DB                        test rbx, rbx
007C9DBE  41 0F 44 C6                     cmove eax, r14d
007C9DC2  88 44 24 44                     mov byte ptr [rsp + 0x44], al
007C9DC6  E8 F5 DB 2E 00                  call 0x140ab79c0
007C9DCB  84 C0                           test al, al
007C9DCD  74 12                           je 0x1407c9de1
007C9DCF  48 85 DB                        test rbx, rbx
007C9DD2  75 27                           jne 0x1407c9dfb
007C9DD4  C7 44 24 40 01 00 00 C0         mov dword ptr [rsp + 0x40], 0xc0000001
007C9DDC  E9 B0 00 00 00                  jmp 0x1407c9e91
007C9DE1  48 85 DB                        test rbx, rbx
007C9DE4  75 15                           jne 0x1407c9dfb
007C9DE6  8B 47 0C                        mov eax, dword ptr [rdi + 0xc]
007C9DE9  41 84 C6                        test r14b, al
007C9DEC  74 0D                           je 0x1407c9dfb
007C9DEE  C7 44 24 40 0D 00 00 C0         mov dword ptr [rsp + 0x40], 0xc000000d
007C9DF6  E9 96 00 00 00                  jmp 0x1407c9e91
007C9DFB  40 88 74 24 46                  mov byte ptr [rsp + 0x46], sil
007C9E00  48 85 DB                        test rbx, rbx
007C9E03  0F 85 88 00 00 00               jne 0x1407c9e91
007C9E09  49 8B 8F F0 B6 00 00            mov rcx, qword ptr [r15 + 0xb6f0]
007C9E10  48 85 C9                        test rcx, rcx
007C9E13  74 7C                           je 0x1407c9e91
007C9E15  41 38 B7 90 B7 00 00            cmp byte ptr [r15 + 0xb790], sil
007C9E1C  75 73                           jne 0x1407c9e91
007C9E1E  8B 01                           mov eax, dword ptr [rcx]
007C9E20  39 07                           cmp dword ptr [rdi], eax
007C9E22  75 6D                           jne 0x1407c9e91
007C9E24  8B 57 04                        mov edx, dword ptr [rdi + 4]
007C9E27  3B 51 04                        cmp edx, dword ptr [rcx + 4]
007C9E2A  75 65                           jne 0x1407c9e91
007C9E2C  8B 41 08                        mov eax, dword ptr [rcx + 8]
007C9E2F  39 47 08                        cmp dword ptr [rdi + 8], eax
007C9E32  75 5D                           jne 0x1407c9e91
007C9E34  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
007C9E37  39 47 0C                        cmp dword ptr [rdi + 0xc], eax
007C9E3A  75 55                           jne 0x1407c9e91
007C9E3C  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
007C9E3F  39 47 10                        cmp dword ptr [rdi + 0x10], eax
007C9E42  75 4D                           jne 0x1407c9e91
007C9E44  44 8B C2                        mov r8d, edx
007C9E47  48 83 C1 14                     add rcx, 0x14
007C9E4B  48 8D 57 14                     lea rdx, [rdi + 0x14]
007C9E4F  E8 1C 08 EF FF                  call 0x1406ba670
007C9E54  48 8B C8                        mov rcx, rax
007C9E57  8B 47 04                        mov eax, dword ptr [rdi + 4]
007C9E5A  48 3B C8                        cmp rcx, rax
007C9E5D  75 32                           jne 0x1407c9e91
007C9E5F  49 8B 8F F0 B6 00 00            mov rcx, qword ptr [r15 + 0xb6f0]
007C9E66  44 8B 47 08                     mov r8d, dword ptr [rdi + 8]
007C9E6A  8B 41 04                        mov eax, dword ptr [rcx + 4]
007C9E6D  48 83 C1 14                     add rcx, 0x14
007C9E71  48 03 C8                        add rcx, rax
007C9E74  49 8B D4                        mov rdx, r12
007C9E77  E8 F4 07 EF FF                  call 0x1406ba670
007C9E7C  48 8B C8                        mov rcx, rax
007C9E7F  8B 47 08                        mov eax, dword ptr [rdi + 8]
007C9E82  40 0F B6 D6                     movzx edx, sil
007C9E86  48 3B C8                        cmp rcx, rax
007C9E89  41 0F 44 D6                     cmove edx, r14d
007C9E8D  88 54 24 46                     mov byte ptr [rsp + 0x46], dl
007C9E91  49 8D 9F F8 B6 00 00            lea rbx, [r15 + 0xb6f8]
007C9E98  B8 11 00 00 00                  mov eax, 0x11
007C9E9D  F0 48 0F B1 33                  lock cmpxchg qword ptr [rbx], rsi
007C9EA2  74 08                           je 0x1407c9eac
007C9EA4  48 8B CB                        mov rcx, rbx
007C9EA7  E8 94 95 A9 FF                  call 0x140263440
007C9EAC  48 8B CB                        mov rcx, rbx
007C9EAF  E8 4C 77 B1 FF                  call 0x1402e1600
007C9EB4  E8 F7 39 A9 FF                  call 0x14025d8b0
007C9EB9  39 74 24 40                     cmp dword ptr [rsp + 0x40], esi
007C9EBD  0F 8C AB 09 00 00               jl 0x1407ca86e
007C9EC3  44 38 74 24 46                  cmp byte ptr [rsp + 0x46], r14b
007C9EC8  0F 85 D5 01 00 00               jne 0x1407ca0a3
007C9ECE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007C9ED7  48 83 CB FF                     or rbx, 0xffffffffffffffff
007C9EDB  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
007C9EE2  90                              nop
007C9EE3  49 8D B7 F8 B6 00 00            lea rsi, [r15 + 0xb6f8]
007C9EEA  45 33 C0                        xor r8d, r8d
007C9EED  33 D2                           xor edx, edx
007C9EEF  48 8B CE                        mov rcx, rsi
007C9EF2  E8 39 63 A4 FF                  call 0x140210230
007C9EF7  4C 8B E8                        mov r13, rax
007C9EFA  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
007C9F00  73 0E                           jae 0x1407c9f10
007C9F02  4C 8B C6                        mov r8, rsi
007C9F05  48 8B D0                        mov rdx, rax
007C9F08  48 8B CE                        mov rcx, rsi
007C9F0B  E8 80 5D A4 FF                  call 0x14020fc90
007C9F10  45 33 E4                        xor r12d, r12d
007C9F13  4D 85 ED                        test r13, r13
007C9F16  74 04                           je 0x1407c9f1c
007C9F18  45 88 75 0A                     mov byte ptr [r13 + 0xa], r14b
007C9F1C  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
007C9F21  49 8B CF                        mov rcx, r15
007C9F24  E8 17 D8 E8 FF                  call 0x140657740
007C9F29  44 39 64 24 60                  cmp dword ptr [rsp + 0x60], r12d
007C9F2E  40 0F 95 C6                     setne sil
007C9F32  41 8B 97 E8 B6 00 00            mov edx, dword ptr [r15 + 0xb6e8]
007C9F39  4D 8D 4F 18                     lea r9, [r15 + 0x18]
007C9F3D  44 89 A4 24 BC 00 00 00         mov dword ptr [rsp + 0xbc], r12d
007C9F45  44 89 A4 24 D9 00 00 00         mov dword ptr [rsp + 0xd9], r12d
007C9F4D  66 44 89 A4 24 DD 00 00 00      mov word ptr [rsp + 0xdd], r12w
007C9F56  44 88 A4 24 DF 00 00 00         mov byte ptr [rsp + 0xdf], r12b
007C9F5E  85 D2                           test edx, edx
007C9F60  74 0F                           je 0x1407c9f71
007C9F62  4D 85 C9                        test r9, r9
007C9F65  75 0A                           jne 0x1407c9f71
007C9F67  B8 0D 00 00 C0                  mov eax, 0xc000000d
007C9F6C  E9 CC 00 00 00                  jmp 0x1407ca03d
007C9F71  4C 89 A4 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r12
007C9F79  4C 89 A4 24 C0 00 00 00         mov qword ptr [rsp + 0xc0], r12
007C9F81  44 89 A4 24 B8 00 00 00         mov dword ptr [rsp + 0xb8], r12d
007C9F89  4C 89 A4 24 C8 00 00 00         mov qword ptr [rsp + 0xc8], r12
007C9F91  48 C7 84 24 D0 00 00 00 30 2A 00 00  mov qword ptr [rsp + 0xd0], 0x2a30
007C9F9D  44 88 B4 24 D8 00 00 00         mov byte ptr [rsp + 0xd8], r14b
007C9FA5  48 8D 4F 14                     lea rcx, [rdi + 0x14]
007C9FA9  4C 8D 84 24 B0 00 00 00         lea r8, [rsp + 0xb0]
007C9FB1  E8 F6 D8 E8 FF                  call 0x1406578ac
007C9FB6  8B C8                           mov ecx, eax
007C9FB8  85 C0                           test eax, eax
007C9FBA  75 32                           jne 0x1407c9fee
007C9FBC  85 D2                           test edx, edx
007C9FBE  74 2E                           je 0x1407c9fee
007C9FC0  48 8B C2                        mov rax, rdx
007C9FC3  48 C1 E0 04                     shl rax, 4
007C9FC7  BA FF FF FF FF                  mov edx, 0xffffffff
007C9FCC  48 3B D0                        cmp rdx, rax
007C9FCF  1B C9                           sbb ecx, ecx
007C9FD1  81 E1 95 00 00 C0               and ecx, 0xc0000095
007C9FD7  48 3B C2                        cmp rax, rdx
007C9FDA  77 12                           ja 0x1407c9fee
007C9FDC  4C 8D 84 24 B0 00 00 00         lea r8, [rsp + 0xb0]
007C9FE4  49 8B C9                        mov rcx, r9
007C9FE7  E8 C0 D8 E8 FF                  call 0x1406578ac
007C9FEC  8B C8                           mov ecx, eax
007C9FEE  85 C9                           test ecx, ecx
007C9FF0  74 13                           je 0x1407ca005
007C9FF2  4C 89 A4 24 B0 00 00 00         mov qword ptr [rsp + 0xb0], r12
007C9FFA  C7 84 24 B8 00 00 00 04 00 00 00  mov dword ptr [rsp + 0xb8], 4
007CA005  0F 10 84 24 B0 00 00 00         movups xmm0, xmmword ptr [rsp + 0xb0]
007CA00D  0F 11 84 24 58 01 00 00         movups xmmword ptr [rsp + 0x158], xmm0
007CA015  0F 10 8C 24 C0 00 00 00         movups xmm1, xmmword ptr [rsp + 0xc0]
007CA01D  0F 11 8C 24 68 01 00 00         movups xmmword ptr [rsp + 0x168], xmm1
007CA025  0F 10 84 24 D0 00 00 00         movups xmm0, xmmword ptr [rsp + 0xd0]
007CA02D  0F 11 84 24 78 01 00 00         movups xmmword ptr [rsp + 0x178], xmm0
007CA035  41 8B C4                        mov eax, r12d
007CA038  85 C9                           test ecx, ecx
007CA03A  0F 44 C1                        cmove eax, ecx
007CA03D  85 C0                           test eax, eax
007CA03F  78 19                           js 0x1407ca05a
007CA041  45 8B CE                        mov r9d, r14d
007CA044  41 B8 07 00 00 00               mov r8d, 7
007CA04A  48 8D 94 24 58 01 00 00         lea rdx, [rsp + 0x158]
007CA052  49 8B CF                        mov rcx, r15
007CA055  E8 96 CD 19 00                  call 0x140966df0
007CA05A  49 8D BF F8 B6 00 00            lea rdi, [r15 + 0xb6f8]
007CA061  48 8B C3                        mov rax, rbx
007CA064  F0 48 0F C1 07                  lock xadd qword ptr [rdi], rax
007CA069  24 06                           and al, 6
007CA06B  3C 02                           cmp al, 2
007CA06D  75 08                           jne 0x1407ca077
007CA06F  48 8B CF                        mov rcx, rdi
007CA072  E8 59 BD A9 FF                  call 0x140265dd0
007CA077  48 8B CF                        mov rcx, rdi
007CA07A  E8 81 75 B1 FF                  call 0x1402e1600
007CA07F  E8 2C 38 A9 FF                  call 0x14025d8b0
007CA084  40 84 F6                        test sil, sil
007CA087  74 08                           je 0x1407ca091
007CA089  49 8B CF                        mov rcx, r15
007CA08C  E8 4B FB FF FF                  call 0x1407c9bdc
007CA091  C7 44 24 40 00 00 00 40         mov dword ptr [rsp + 0x40], 0x40000000
007CA099  4D 8B EC                        mov r13, r12
007CA09C  33 F6                           xor esi, esi
007CA09E  E9 FC 07 00 00                  jmp 0x1407ca89f
007CA0A3  C7 84 24 28 01 00 00 30 00 00 00  mov dword ptr [rsp + 0x128], 0x30
007CA0AE  48 89 B4 24 30 01 00 00         mov qword ptr [rsp + 0x130], rsi
007CA0B6  C7 84 24 40 01 00 00 20 02 00 00  mov dword ptr [rsp + 0x140], 0x220
007CA0C1  48 89 B4 24 38 01 00 00         mov qword ptr [rsp + 0x138], rsi
007CA0C9  0F 57 C0                        xorps xmm0, xmm0
007CA0CC  F3 0F 7F 84 24 48 01 00 00      movdqu xmmword ptr [rsp + 0x148], xmm0
007CA0D5  8B 07                           mov eax, dword ptr [rdi]
007CA0D7  89 84 24 88 00 00 00            mov dword ptr [rsp + 0x88], eax
007CA0DE  89 B4 24 8C 00 00 00            mov dword ptr [rsp + 0x8c], esi
007CA0E5  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
007CA0EA  C7 44 24 28 00 00 00 08         mov dword ptr [rsp + 0x28], 0x8000000
007CA0F2  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
007CA0FA  4C 8D 8C 24 88 00 00 00         lea r9, [rsp + 0x88]
007CA102  4C 8D 84 24 28 01 00 00         lea r8, [rsp + 0x128]
007CA10A  BA 07 00 0F 00                  mov edx, 0xf0007
007CA10F  48 8D 8C 24 90 00 00 00         lea rcx, [rsp + 0x90]
007CA117  E8 F4 38 EE FF                  call 0x1406ada10
007CA11C  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
007CA120  85 C0                           test eax, eax
007CA122  0F 88 46 07 00 00               js 0x1407ca86e
007CA128  48 89 B4 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], rsi
007CA130  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
007CA135  48 8D 84 24 A0 00 00 00         lea rax, [rsp + 0xa0]
007CA13D  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007CA142  45 33 C9                        xor r9d, r9d
007CA145  45 33 C0                        xor r8d, r8d
007CA148  33 D2                           xor edx, edx
007CA14A  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
007CA152  E8 59 EC 09 00                  call 0x140868db0
007CA157  8B D8                           mov ebx, eax
007CA159  48 8B B4 24 A0 00 00 00         mov rsi, qword ptr [rsp + 0xa0]
007CA161  48 89 B4 24 98 00 00 00         mov qword ptr [rsp + 0x98], rsi
007CA169  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
007CA16D  48 8B 8C 24 90 00 00 00         mov rcx, qword ptr [rsp + 0x90]
007CA175  E8 36 31 EE FF                  call 0x1406ad2b0
007CA17A  33 C0                           xor eax, eax
007CA17C  85 DB                           test ebx, ebx
007CA17E  0F 88 E8 06 00 00               js 0x1407ca86c
007CA184  48 89 84 24 18 01 00 00         mov qword ptr [rsp + 0x118], rax
007CA18C  4C 8D 84 24 18 01 00 00         lea r8, [rsp + 0x118]
007CA194  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
007CA199  48 8B CE                        mov rcx, rsi
007CA19C  E8 DF 82 1B 00                  call 0x140982480
007CA1A1  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
007CA1A5  33 F6                           xor esi, esi
007CA1A7  85 C0                           test eax, eax
007CA1A9  0F 88 BF 06 00 00               js 0x1407ca86e
007CA1AF  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
007CA1B4  0F 10 07                        movups xmm0, xmmword ptr [rdi]
007CA1B7  0F 11 06                        movups xmmword ptr [rsi], xmm0
007CA1BA  8B 47 10                        mov eax, dword ptr [rdi + 0x10]
007CA1BD  89 46 10                        mov dword ptr [rsi + 0x10], eax
007CA1C0  44 8B 47 04                     mov r8d, dword ptr [rdi + 4]
007CA1C4  48 8D 4E 14                     lea rcx, [rsi + 0x14]
007CA1C8  48 8D 57 14                     lea rdx, [rdi + 0x14]
007CA1CC  E8 6F C6 EF FF                  call 0x1406c6840
007CA1D1  44 8B 47 08                     mov r8d, dword ptr [rdi + 8]
007CA1D5  8B 47 04                        mov eax, dword ptr [rdi + 4]
007CA1D8  48 8D 4E 14                     lea rcx, [rsi + 0x14]
007CA1DC  48 03 C8                        add rcx, rax
007CA1DF  49 8B D4                        mov rdx, r12
007CA1E2  E8 59 C6 EF FF                  call 0x1406c6840
007CA1E7  8B 46 04                        mov eax, dword ptr [rsi + 4]
007CA1EA  48 8D 4E 14                     lea rcx, [rsi + 0x14]
007CA1EE  48 03 C8                        add rcx, rax
007CA1F1  83 7E 08 04                     cmp dword ptr [rsi + 8], 4
007CA1F5  0F 85 58 06 00 00               jne 0x1407ca853
007CA1FB  45 33 E4                        xor r12d, r12d
007CA1FE  48 85 C9                        test rcx, rcx
007CA201  0F 84 4C 06 00 00               je 0x1407ca853
007CA207  83 39 45                        cmp dword ptr [rcx], 0x45
007CA20A  0F 85 43 06 00 00               jne 0x1407ca853
007CA210  48 8D 44 24 48                  lea rax, [rsp + 0x48]
007CA215  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007CA21A  45 33 C9                        xor r9d, r9d
007CA21D  45 33 C0                        xor r8d, r8d
007CA220  41 8A D6                        mov dl, r14b
007CA223  48 8B CE                        mov rcx, rsi
007CA226  E8 F1 E9 FF FF                  call 0x1407c8c1c
007CA22B  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
007CA22F  48 83 CB FF                     or rbx, 0xffffffffffffffff
007CA233  3D 23 00 00 C0                  cmp eax, 0xc0000023
007CA238  0F 85 08 01 00 00               jne 0x1407ca346
007CA23E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007CA247  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
007CA24E  90                              nop
007CA24F  49 8D BF F8 B6 00 00            lea rdi, [r15 + 0xb6f8]
007CA256  45 33 C0                        xor r8d, r8d
007CA259  33 D2                           xor edx, edx
007CA25B  48 8B CF                        mov rcx, rdi
007CA25E  E8 CD 5F A4 FF                  call 0x140210230
007CA263  48 8B F0                        mov rsi, rax
007CA266  33 C0                           xor eax, eax
007CA268  8D 4B 12                        lea ecx, [rbx + 0x12]
007CA26B  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
007CA270  74 10                           je 0x1407ca282
007CA272  4C 8B CF                        mov r9, rdi
007CA275  4C 8B C6                        mov r8, rsi
007CA278  33 D2                           xor edx, edx
007CA27A  48 8B CF                        mov rcx, rdi
007CA27D  E8 CA 61 A4 FF                  call 0x14021044c
007CA282  48 85 F6                        test rsi, rsi
007CA285  74 04                           je 0x1407ca28b
007CA287  44 88 76 0A                     mov byte ptr [rsi + 0xa], r14b
007CA28B  B8 6D 0B 00 00                  mov eax, 0xb6d
007CA290  3B 44 24 48                     cmp eax, dword ptr [rsp + 0x48]
007CA294  1B C0                           sbb eax, eax
007CA296  25 0D 00 00 C0                  and eax, 0xc000000d
007CA29B  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
007CA29F  49 8D BF F8 B6 00 00            lea rdi, [r15 + 0xb6f8]
007CA2A6  41 BC 11 00 00 00               mov r12d, 0x11
007CA2AC  41 8B C4                        mov eax, r12d
007CA2AF  33 F6                           xor esi, esi
007CA2B1  F0 48 0F B1 37                  lock cmpxchg qword ptr [rdi], rsi
007CA2B6  74 08                           je 0x1407ca2c0
007CA2B8  48 8B CF                        mov rcx, rdi
007CA2BB  E8 80 91 A9 FF                  call 0x140263440
007CA2C0  48 8B CF                        mov rcx, rdi
007CA2C3  E8 38 73 B1 FF                  call 0x1402e1600
007CA2C8  E8 E3 35 A9 FF                  call 0x14025d8b0
007CA2CD  39 74 24 40                     cmp dword ptr [rsp + 0x40], esi
007CA2D1  0F 8C 43 FA FF FF               jl 0x1407c9d1a
007CA2D7  8B 7C 24 48                     mov edi, dword ptr [rsp + 0x48]
007CA2DB  8B D7                           mov edx, edi
007CA2DD  48 C1 E2 04                     shl rdx, 4
007CA2E1  B9 00 01 00 00                  mov ecx, 0x100
007CA2E6  41 B8 53 4C 53 20               mov r8d, 0x20534c53
007CA2EC  E8 FF 7D 3B 00                  call 0x140b820f0
007CA2F1  4C 8B E8                        mov r13, rax
007CA2F4  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
007CA2F9  48 85 C0                        test rax, rax
007CA2FC  75 0D                           jne 0x1407ca30b
007CA2FE  C7 44 24 40 17 00 00 C0         mov dword ptr [rsp + 0x40], 0xc0000017
007CA306  E9 12 FA FF FF                  jmp 0x1407c9d1d
007CA30B  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
007CA310  44 8B 4C 24 48                  mov r9d, dword ptr [rsp + 0x48]
007CA315  4D 8B C5                        mov r8, r13
007CA318  33 D2                           xor edx, edx
007CA31A  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
007CA31F  E8 F8 E8 FF FF                  call 0x1407c8c1c
007CA324  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
007CA328  85 C0                           test eax, eax
007CA32A  78 23                           js 0x1407ca34f
007CA32C  4C 8D 0D FD E3 FF FF            lea r9, [rip - 0x1c03]
007CA333  41 B8 10 00 00 00               mov r8d, 0x10
007CA339  48 8B D7                        mov rdx, rdi
007CA33C  49 8B CD                        mov rcx, r13
007CA33F  E8 AC 66 D3 FF                  call 0x1405009f0
007CA344  EB 09                           jmp 0x1407ca34f
007CA346  4D 8B EC                        mov r13, r12
007CA349  33 F6                           xor esi, esi
007CA34B  44 8D 66 11                     lea r12d, [rsi + 0x11]
007CA34F  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
007CA353  85 C0                           test eax, eax
007CA355  79 1D                           jns 0x1407ca374
007CA357  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
007CA35C  3D 3E 00 00 C0                  cmp eax, 0xc000003e
007CA361  0F 85 38 05 00 00               jne 0x1407ca89f
007CA367  C7 44 24 40 0D 00 00 C0         mov dword ptr [rsp + 0x40], 0xc000000d
007CA36F  E9 2B 05 00 00                  jmp 0x1407ca89f
007CA374  40 88 74 24 45                  mov byte ptr [rsp + 0x45], sil
007CA379  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
007CA382  48 89 8C 24 90 01 00 00         mov qword ptr [rsp + 0x190], rcx
007CA38A  0F B7 81 E4 01 00 00            movzx eax, word ptr [rcx + 0x1e4]
007CA391  66 41 2B C6                     sub ax, r14w
007CA395  66 89 81 E4 01 00 00            mov word ptr [rcx + 0x1e4], ax
007CA39C  90                              nop
007CA39D  49 8D B7 F8 B6 00 00            lea rsi, [r15 + 0xb6f8]
007CA3A4  45 33 C0                        xor r8d, r8d
007CA3A7  33 D2                           xor edx, edx
007CA3A9  48 8B CE                        mov rcx, rsi
007CA3AC  E8 7F 5E A4 FF                  call 0x140210230
007CA3B1  48 8B F8                        mov rdi, rax
007CA3B4  33 C0                           xor eax, eax
007CA3B6  F0 4C 0F B1 26                  lock cmpxchg qword ptr [rsi], r12
007CA3BB  74 10                           je 0x1407ca3cd
007CA3BD  4C 8B CE                        mov r9, rsi
007CA3C0  4C 8B C7                        mov r8, rdi
007CA3C3  33 D2                           xor edx, edx
007CA3C5  48 8B CE                        mov rcx, rsi
007CA3C8  E8 7F 60 A4 FF                  call 0x14021044c
007CA3CD  33 F6                           xor esi, esi
007CA3CF  48 85 FF                        test rdi, rdi
007CA3D2  74 04                           je 0x1407ca3d8
007CA3D4  44 88 77 0A                     mov byte ptr [rdi + 0xa], r14b
007CA3D8  48 39 74 24 78                  cmp qword ptr [rsp + 0x78], rsi
007CA3DD  0F 85 1C 01 00 00               jne 0x1407ca4ff
007CA3E3  44 8B E6                        mov r12d, esi
007CA3E6  89 74 24 64                     mov dword ptr [rsp + 0x64], esi
007CA3EA  44 8B EE                        mov r13d, esi
007CA3ED  89 74 24 70                     mov dword ptr [rsp + 0x70], esi
007CA3F1  44 3B 64 24 48                  cmp r12d, dword ptr [rsp + 0x48]
007CA3F6  0F 83 C9 00 00 00               jae 0x1407ca4c5
007CA3FC  45 3B AF E8 B6 00 00            cmp r13d, dword ptr [r15 + 0xb6e8]
007CA403  0F 83 BC 00 00 00               jae 0x1407ca4c5
007CA409  41 8B F5                        mov esi, r13d
007CA40C  41 8B FC                        mov edi, r12d
007CA40F  48 C1 E7 04                     shl rdi, 4
007CA413  48 03 7C 24 50                  add rdi, qword ptr [rsp + 0x50]
007CA418  41 8B D5                        mov edx, r13d
007CA41B  48 C1 E2 04                     shl rdx, 4
007CA41F  48 83 C2 18                     add rdx, 0x18
007CA423  49 03 D7                        add rdx, r15
007CA426  48 8B CF                        mov rcx, rdi
007CA429  E8 02 E3 FF FF                  call 0x1407c8730
007CA42E  89 84 24 10 01 00 00            mov dword ptr [rsp + 0x110], eax
007CA435  4C 8B 4F 08                     mov r9, qword ptr [rdi + 8]
007CA439  4C 89 8C 24 20 01 00 00         mov qword ptr [rsp + 0x120], r9
007CA441  48 8D 4E 02                     lea rcx, [rsi + 2]
007CA445  48 03 C9                        add rcx, rcx
007CA448  49 8B 14 CF                     mov rdx, qword ptr [r15 + rcx*8]
007CA44C  48 89 94 24 98 01 00 00         mov qword ptr [rsp + 0x198], rdx
007CA454  33 F6                           xor esi, esi
007CA456  85 C0                           test eax, eax
007CA458  79 1F                           jns 0x1407ca479
007CA45A  41 8B 41 08                     mov eax, dword ptr [r9 + 8]
007CA45E  A8 02                           test al, 2
007CA460  74 0A                           je 0x1407ca46c
007CA462  44 88 74 24 45                  mov byte ptr [rsp + 0x45], r14b
007CA467  E9 8D 00 00 00                  jmp 0x1407ca4f9
007CA46C  45 03 E6                        add r12d, r14d
007CA46F  44 89 64 24 64                  mov dword ptr [rsp + 0x64], r12d
007CA474  E9 78 FF FF FF                  jmp 0x1407ca3f1
007CA479  7E 0A                           jle 0x1407ca485
007CA47B  45 03 EE                        add r13d, r14d
007CA47E  44 89 6C 24 70                  mov dword ptr [rsp + 0x70], r13d
007CA483  EB EF                           jmp 0x1407ca474
007CA485  41 8B 41 08                     mov eax, dword ptr [r9 + 8]
007CA489  A8 02                           test al, 2
007CA48B  74 2E                           je 0x1407ca4bb
007CA48D  0F B7 42 06                     movzx eax, word ptr [rdx + 6]
007CA491  66 41 39 41 06                  cmp word ptr [r9 + 6], ax
007CA496  75 CA                           jne 0x1407ca462
007CA498  44 8B C0                        mov r8d, eax
007CA49B  0F B7 42 02                     movzx eax, word ptr [rdx + 2]
007CA49F  48 83 C0 10                     add rax, 0x10
007CA4A3  48 03 D0                        add rdx, rax
007CA4A6  41 0F B7 49 02                  movzx ecx, word ptr [r9 + 2]
007CA4AB  49 83 C1 10                     add r9, 0x10
007CA4AF  49 03 C9                        add rcx, r9
007CA4B2  E8 59 C6 EF FF                  call 0x1406c6b10
007CA4B7  85 C0                           test eax, eax
007CA4B9  75 A7                           jne 0x1407ca462
007CA4BB  45 03 E6                        add r12d, r14d
007CA4BE  44 89 64 24 64                  mov dword ptr [rsp + 0x64], r12d
007CA4C3  EB B6                           jmp 0x1407ca47b
007CA4C5  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
007CA4CA  44 3B 64 24 48                  cmp r12d, dword ptr [rsp + 0x48]
007CA4CF  73 28                           jae 0x1407ca4f9
007CA4D1  41 8B C4                        mov eax, r12d
007CA4D4  48 03 C0                        add rax, rax
007CA4D7  48 8B 44 C1 08                  mov rax, qword ptr [rcx + rax*8 + 8]
007CA4DC  48 89 84 24 20 01 00 00         mov qword ptr [rsp + 0x120], rax
007CA4E4  8B 40 08                        mov eax, dword ptr [rax + 8]
007CA4E7  A8 02                           test al, 2
007CA4E9  0F 85 73 FF FF FF               jne 0x1407ca462
007CA4EF  45 03 E6                        add r12d, r14d
007CA4F2  44 89 64 24 64                  mov dword ptr [rsp + 0x64], r12d
007CA4F7  EB D1                           jmp 0x1407ca4ca
007CA4F9  41 BC 11 00 00 00               mov r12d, 0x11
007CA4FF  49 8D BF F8 B6 00 00            lea rdi, [r15 + 0xb6f8]
007CA506  49 8B C4                        mov rax, r12
007CA509  F0 48 0F B1 37                  lock cmpxchg qword ptr [rdi], rsi
007CA50E  74 08                           je 0x1407ca518
007CA510  48 8B CF                        mov rcx, rdi
007CA513  E8 28 8F A9 FF                  call 0x140263440
007CA518  48 8B CF                        mov rcx, rdi
007CA51B  E8 E0 70 B1 FF                  call 0x1402e1600
007CA520  E8 8B 33 A9 FF                  call 0x14025d8b0
007CA525  4C 8B A4 24 98 00 00 00         mov r12, qword ptr [rsp + 0x98]
007CA52D  49 8B CC                        mov rcx, r12
007CA530  E8 EB 54 A4 FF                  call 0x14020fa20
007CA535  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007CA53E  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
007CA545  90                              nop
007CA546  49 8D B7 F8 B6 00 00            lea rsi, [r15 + 0xb6f8]
007CA54D  45 33 C0                        xor r8d, r8d
007CA550  33 D2                           xor edx, edx
007CA552  48 8B CE                        mov rcx, rsi
007CA555  E8 D6 5C A4 FF                  call 0x140210230
007CA55A  48 8B F8                        mov rdi, rax
007CA55D  F0 48 0F BA 2E 00               lock bts qword ptr [rsi], 0
007CA563  73 0E                           jae 0x1407ca573
007CA565  4C 8B C6                        mov r8, rsi
007CA568  48 8B D0                        mov rdx, rax
007CA56B  48 8B CE                        mov rcx, rsi
007CA56E  E8 1D 57 A4 FF                  call 0x14020fc90
007CA573  45 33 D2                        xor r10d, r10d
007CA576  48 85 FF                        test rdi, rdi
007CA579  74 04                           je 0x1407ca57f
007CA57B  44 88 77 0A                     mov byte ptr [rdi + 0xa], r14b
007CA57F  44 89 94 24 EC 00 00 00         mov dword ptr [rsp + 0xec], r10d
007CA587  44 89 94 24 09 01 00 00         mov dword ptr [rsp + 0x109], r10d
007CA58F  66 44 89 94 24 0D 01 00 00      mov word ptr [rsp + 0x10d], r10w
007CA598  44 88 94 24 0F 01 00 00         mov byte ptr [rsp + 0x10f], r10b
007CA5A0  4C 8B 6C 24 68                  mov r13, qword ptr [rsp + 0x68]
007CA5A5  4D 85 ED                        test r13, r13
007CA5A8  0F 84 E4 00 00 00               je 0x1407ca692
007CA5AE  8B 74 24 48                     mov esi, dword ptr [rsp + 0x48]
007CA5B2  4C 8B 4C 24 50                  mov r9, qword ptr [rsp + 0x50]
007CA5B7  85 F6                           test esi, esi
007CA5B9  74 09                           je 0x1407ca5c4
007CA5BB  4D 85 C9                        test r9, r9
007CA5BE  0F 84 D2 00 00 00               je 0x1407ca696
007CA5C4  4C 89 94 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r10
007CA5CC  4C 89 94 24 F0 00 00 00         mov qword ptr [rsp + 0xf0], r10
007CA5D4  44 89 94 24 E8 00 00 00         mov dword ptr [rsp + 0xe8], r10d
007CA5DC  4C 89 94 24 F8 00 00 00         mov qword ptr [rsp + 0xf8], r10
007CA5E4  48 C7 84 24 00 01 00 00 30 2A 00 00  mov qword ptr [rsp + 0x100], 0x2a30
007CA5F0  44 88 B4 24 08 01 00 00         mov byte ptr [rsp + 0x108], r14b
007CA5F8  49 8D 4D 14                     lea rcx, [r13 + 0x14]
007CA5FC  4C 8D 84 24 E0 00 00 00         lea r8, [rsp + 0xe0]
007CA604  E8 A3 D2 E8 FF                  call 0x1406578ac
007CA609  8B C8                           mov ecx, eax
007CA60B  85 C0                           test eax, eax
007CA60D  75 32                           jne 0x1407ca641
007CA60F  85 F6                           test esi, esi
007CA611  74 2E                           je 0x1407ca641
007CA613  48 8B C6                        mov rax, rsi
007CA616  48 C1 E0 04                     shl rax, 4
007CA61A  BA FF FF FF FF                  mov edx, 0xffffffff
007CA61F  48 3B D0                        cmp rdx, rax
007CA622  1B C9                           sbb ecx, ecx
007CA624  81 E1 95 00 00 C0               and ecx, 0xc0000095
007CA62A  48 3B C2                        cmp rax, rdx
007CA62D  77 12                           ja 0x1407ca641
007CA62F  4C 8D 84 24 E0 00 00 00         lea r8, [rsp + 0xe0]
007CA637  49 8B C9                        mov rcx, r9
007CA63A  E8 6D D2 E8 FF                  call 0x1406578ac
007CA63F  8B C8                           mov ecx, eax
007CA641  85 C9                           test ecx, ecx
007CA643  74 13                           je 0x1407ca658
007CA645  4C 89 94 24 E0 00 00 00         mov qword ptr [rsp + 0xe0], r10
007CA64D  C7 84 24 E8 00 00 00 04 00 00 00  mov dword ptr [rsp + 0xe8], 4
007CA658  0F 10 84 24 E0 00 00 00         movups xmm0, xmmword ptr [rsp + 0xe0]
007CA660  0F 11 84 24 58 01 00 00         movups xmmword ptr [rsp + 0x158], xmm0
007CA668  0F 10 8C 24 F0 00 00 00         movups xmm1, xmmword ptr [rsp + 0xf0]
007CA670  0F 11 8C 24 68 01 00 00         movups xmmword ptr [rsp + 0x168], xmm1
007CA678  0F 10 84 24 00 01 00 00         movups xmm0, xmmword ptr [rsp + 0x100]
007CA680  0F 11 84 24 78 01 00 00         movups xmmword ptr [rsp + 0x178], xmm0
007CA688  41 8B FA                        mov edi, r10d
007CA68B  85 C9                           test ecx, ecx
007CA68D  0F 44 F9                        cmove edi, ecx
007CA690  EB 09                           jmp 0x1407ca69b
007CA692  8B 74 24 48                     mov esi, dword ptr [rsp + 0x48]
007CA696  BF 0D 00 00 C0                  mov edi, 0xc000000d
007CA69B  89 7C 24 40                     mov dword ptr [rsp + 0x40], edi
007CA69F  85 FF                           test edi, edi
007CA6A1  0F 88 25 01 00 00               js 0x1407ca7cc
007CA6A7  45 8B CE                        mov r9d, r14d
007CA6AA  41 B8 07 00 00 00               mov r8d, 7
007CA6B0  48 8D 94 24 58 01 00 00         lea rdx, [rsp + 0x158]
007CA6B8  49 8B CF                        mov rcx, r15
007CA6BB  E8 30 C7 19 00                  call 0x140966df0
007CA6C0  49 8B 47 10                     mov rax, qword ptr [r15 + 0x10]
007CA6C4  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
007CA6C9  49 8B 87 F0 B6 00 00            mov rax, qword ptr [r15 + 0xb6f0]
007CA6D0  48 89 84 24 A8 00 00 00         mov qword ptr [rsp + 0xa8], rax
007CA6D8  4D 89 67 10                     mov qword ptr [r15 + 0x10], r12
007CA6DC  4D 89 AF F0 B6 00 00            mov qword ptr [r15 + 0xb6f0], r13
007CA6E3  45 33 ED                        xor r13d, r13d
007CA6E6  4C 89 6C 24 68                  mov qword ptr [rsp + 0x68], r13
007CA6EB  E8 20 B0 A5 FF                  call 0x140225710
007CA6F0  48 8B C8                        mov rcx, rax
007CA6F3  E8 38 94 C7 FF                  call 0x140443b30
007CA6F8  84 C0                           test al, al
007CA6FA  75 12                           jne 0x1407ca70e
007CA6FC  49 8B 0F                        mov rcx, qword ptr [r15]
007CA6FF  48 85 C9                        test rcx, rcx
007CA702  74 0A                           je 0x1407ca70e
007CA704  BA 53 4C 53 69                  mov edx, 0x69534c53
007CA709  E8 62 81 3B 00                  call 0x140b82870
007CA70E  4D 89 2F                        mov qword ptr [r15], r13
007CA711  41 8A 87 90 B7 00 00            mov al, byte ptr [r15 + 0xb790]
007CA718  88 84 24 20 02 00 00            mov byte ptr [rsp + 0x220], al
007CA71F  45 88 AF 90 B7 00 00            mov byte ptr [r15 + 0xb790], r13b
007CA726  45 8B 87 E8 B6 00 00            mov r8d, dword ptr [r15 + 0xb6e8]
007CA72D  49 C1 E0 04                     shl r8, 4
007CA731  33 D2                           xor edx, edx
007CA733  49 8D 4F 18                     lea rcx, [r15 + 0x18]
007CA737  E8 04 C5 EF FF                  call 0x1406c6c40
007CA73C  45 89 AF E8 B6 00 00            mov dword ptr [r15 + 0xb6e8], r13d
007CA743  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
007CA748  4D 85 ED                        test r13, r13
007CA74B  74 1A                           je 0x1407ca767
007CA74D  44 8B C6                        mov r8d, esi
007CA750  49 C1 E0 04                     shl r8, 4
007CA754  49 8B D5                        mov rdx, r13
007CA757  49 8D 4F 18                     lea rcx, [r15 + 0x18]
007CA75B  E8 E0 C0 EF FF                  call 0x1406c6840
007CA760  41 89 B7 E8 B6 00 00            mov dword ptr [r15 + 0xb6e8], esi
007CA767  45 88 B7 EC B6 00 00            mov byte ptr [r15 + 0xb6ec], r14b
007CA76E  48 8D 54 24 74                  lea rdx, [rsp + 0x74]
007CA773  49 8B CF                        mov rcx, r15
007CA776  E8 C5 CF E8 FF                  call 0x140657740
007CA77B  49 8B 87 F0 B6 00 00            mov rax, qword ptr [r15 + 0xb6f0]
007CA782  8B 50 0C                        mov edx, dword ptr [rax + 0xc]
007CA785  41 23 D6                        and edx, r14d
007CA788  0F B6 44 24 44                  movzx eax, byte ptr [rsp + 0x44]
007CA78D  41 0F 45 C6                     cmovne eax, r14d
007CA791  88 44 24 44                     mov byte ptr [rsp + 0x44], al
007CA795  03 D2                           add edx, edx
007CA797  49 8B CF                        mov rcx, r15
007CA79A  E8 25 D3 E8 FF                  call 0x140657ac4
007CA79F  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
007CA7A4  49 8B CF                        mov rcx, r15
007CA7A7  E8 94 CF E8 FF                  call 0x140657740
007CA7AC  8B 44 24 74                     mov eax, dword ptr [rsp + 0x74]
007CA7B0  8B 4C 24 60                     mov ecx, dword ptr [rsp + 0x60]
007CA7B4  33 D2                           xor edx, edx
007CA7B6  3B C1                           cmp eax, ecx
007CA7B8  74 0D                           je 0x1407ca7c7
007CA7BA  85 C0                           test eax, eax
007CA7BC  74 04                           je 0x1407ca7c2
007CA7BE  85 C9                           test ecx, ecx
007CA7C0  75 05                           jne 0x1407ca7c7
007CA7C2  45 8A E6                        mov r12b, r14b
007CA7C5  EB 0D                           jmp 0x1407ca7d4
007CA7C7  44 8A E2                        mov r12b, dl
007CA7CA  EB 08                           jmp 0x1407ca7d4
007CA7CC  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
007CA7D1  45 8A E2                        mov r12b, r10b
007CA7D4  49 8D B7 F8 B6 00 00            lea rsi, [r15 + 0xb6f8]
007CA7DB  48 8B C3                        mov rax, rbx
007CA7DE  F0 48 0F C1 06                  lock xadd qword ptr [rsi], rax
007CA7E3  24 06                           and al, 6
007CA7E5  3C 02                           cmp al, 2
007CA7E7  75 08                           jne 0x1407ca7f1
007CA7E9  48 8B CE                        mov rcx, rsi
007CA7EC  E8 DF B5 A9 FF                  call 0x140265dd0
007CA7F1  48 8B CE                        mov rcx, rsi
007CA7F4  E8 07 6E B1 FF                  call 0x1402e1600
007CA7F9  E8 B2 30 A9 FF                  call 0x14025d8b0
007CA7FE  33 F6                           xor esi, esi
007CA800  85 FF                           test edi, edi
007CA802  0F 88 92 00 00 00               js 0x1407ca89a
007CA808  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
007CA80D  48 85 C0                        test rax, rax
007CA810  75 15                           jne 0x1407ca827
007CA812  49 8B CF                        mov rcx, r15
007CA815  E8 42 E5 FF FF                  call 0x1407c8d5c
007CA81A  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
007CA81E  85 C0                           test eax, eax
007CA820  78 78                           js 0x1407ca89a
007CA822  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
007CA827  45 84 E4                        test r12b, r12b
007CA82A  75 05                           jne 0x1407ca831
007CA82C  48 85 C0                        test rax, rax
007CA82F  75 08                           jne 0x1407ca839
007CA831  49 8B CF                        mov rcx, r15
007CA834  E8 A3 F3 FF FF                  call 0x1407c9bdc
007CA839  89 74 24 40                     mov dword ptr [rsp + 0x40], esi
007CA83D  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
007CA842  44 38 74 24 45                  cmp byte ptr [rsp + 0x45], r14b
007CA847  75 56                           jne 0x1407ca89f
007CA849  C7 44 24 40 07 01 00 00         mov dword ptr [rsp + 0x40], 0x107
007CA851  EB 4C                           jmp 0x1407ca89f
007CA853  C7 44 24 40 3F 00 00 C0         mov dword ptr [rsp + 0x40], 0xc000003f
007CA85B  48 83 CB FF                     or rbx, 0xffffffffffffffff
007CA85F  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
007CA864  4D 8B E5                        mov r12, r13
007CA867  E9 30 F8 FF FF                  jmp 0x1407ca09c
007CA86C  33 F6                           xor esi, esi
007CA86E  48 83 CB FF                     or rbx, 0xffffffffffffffff
007CA872  4C 8B 6C 24 50                  mov r13, qword ptr [rsp + 0x50]
007CA877  4D 8B E5                        mov r12, r13
007CA87A  EB 23                           jmp 0x1407ca89f
007CA87C  C7 44 24 40 40 00 00 C0         mov dword ptr [rsp + 0x40], 0xc0000040
007CA884  41 BE 01 00 00 00               mov r14d, 1
007CA88A  48 83 CB FF                     or rbx, 0xffffffffffffffff
007CA88E  EB 0F                           jmp 0x1407ca89f
007CA890  C7 44 24 40 0D 00 00 C0         mov dword ptr [rsp + 0x40], 0xc000000d
007CA898  EB EA                           jmp 0x1407ca884
007CA89A  4C 8B 64 24 58                  mov r12, qword ptr [rsp + 0x58]
007CA89F  40 38 B4 24 20 02 00 00         cmp byte ptr [rsp + 0x220], sil
007CA8A7  74 15                           je 0x1407ca8be
007CA8A9  41 38 B7 90 B7 00 00            cmp byte ptr [r15 + 0xb790], sil
007CA8B0  75 0C                           jne 0x1407ca8be
007CA8B2  48 8D 0D 3F 8A 85 FF            lea rcx, [rip - 0x7a75c1]
007CA8B9  E8 C2 D6 FF FF                  call 0x1407c7f80
007CA8BE  40 38 74 24 44                  cmp byte ptr [rsp + 0x44], sil
007CA8C3  0F 84 A5 00 00 00               je 0x1407ca96e
007CA8C9  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007CA8D2  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
007CA8D9  90                              nop
007CA8DA  49 8D BF F8 B6 00 00            lea rdi, [r15 + 0xb6f8]
007CA8E1  45 33 C0                        xor r8d, r8d
007CA8E4  33 D2                           xor edx, edx
007CA8E6  48 8B CF                        mov rcx, rdi
007CA8E9  E8 42 59 A4 FF                  call 0x140210230
007CA8EE  48 8B F0                        mov rsi, rax
007CA8F1  48 8B C7                        mov rax, rdi
007CA8F4  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
007CA8FA  73 11                           jae 0x1407ca90d
007CA8FC  4C 8B C7                        mov r8, rdi
007CA8FF  48 8B D6                        mov rdx, rsi
007CA902  48 8B CF                        mov rcx, rdi
007CA905  E8 86 53 A4 FF                  call 0x14020fc90
007CA90A  48 8B C7                        mov rax, rdi
007CA90D  48 85 F6                        test rsi, rsi
007CA910  74 07                           je 0x1407ca919
007CA912  44 88 76 0A                     mov byte ptr [rsi + 0xa], r14b
007CA916  48 8B F8                        mov rdi, rax
007CA919  0F 57 C0                        xorps xmm0, xmm0
007CA91C  0F 11 84 24 A0 01 00 00         movups xmmword ptr [rsp + 0x1a0], xmm0
007CA924  0F 11 84 24 B0 01 00 00         movups xmmword ptr [rsp + 0x1b0], xmm0
007CA92C  0F 11 84 24 C0 01 00 00         movups xmmword ptr [rsp + 0x1c0], xmm0
007CA934  45 33 C9                        xor r9d, r9d
007CA937  45 8D 41 20                     lea r8d, [r9 + 0x20]
007CA93B  48 8D 94 24 A0 01 00 00         lea rdx, [rsp + 0x1a0]
007CA943  49 8B CF                        mov rcx, r15
007CA946  E8 A5 C4 19 00                  call 0x140966df0
007CA94B  48 8B C3                        mov rax, rbx
007CA94E  F0 48 0F C1 07                  lock xadd qword ptr [rdi], rax
007CA953  24 06                           and al, 6
007CA955  3C 02                           cmp al, 2
007CA957  75 08                           jne 0x1407ca961
007CA959  48 8B CF                        mov rcx, rdi
007CA95C  E8 6F B4 A9 FF                  call 0x140265dd0
007CA961  48 8B CF                        mov rcx, rdi
007CA964  E8 97 6C B1 FF                  call 0x1402e1600
007CA969  E8 42 2F A9 FF                  call 0x14025d8b0
007CA96E  48 8B 84 24 98 00 00 00         mov rax, qword ptr [rsp + 0x98]
007CA976  48 85 C0                        test rax, rax
007CA979  74 08                           je 0x1407ca983
007CA97B  48 8B C8                        mov rcx, rax
007CA97E  E8 CD E9 B2 FF                  call 0x1402f9350
007CA983  4D 85 E4                        test r12, r12
007CA986  74 08                           je 0x1407ca990
007CA988  49 8B CC                        mov rcx, r12
007CA98B  E8 C0 E9 B2 FF                  call 0x1402f9350
007CA990  48 8B 74 24 68                  mov rsi, qword ptr [rsp + 0x68]
007CA995  45 33 E4                        xor r12d, r12d
007CA998  48 85 F6                        test rsi, rsi
007CA99B  74 0B                           je 0x1407ca9a8
007CA99D  41 8B D6                        mov edx, r14d
007CA9A0  48 8B CE                        mov rcx, rsi
007CA9A3  E8 54 B9 AC FF                  call 0x1402962fc
007CA9A8  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
007CA9B0  48 85 C0                        test rax, rax
007CA9B3  74 0B                           je 0x1407ca9c0
007CA9B5  41 8B D6                        mov edx, r14d
007CA9B8  48 8B C8                        mov rcx, rax
007CA9BB  E8 3C B9 AC FF                  call 0x1402962fc
007CA9C0  4D 85 ED                        test r13, r13
007CA9C3  74 0A                           je 0x1407ca9cf
007CA9C5  33 D2                           xor edx, edx
007CA9C7  49 8B CD                        mov rcx, r13
007CA9CA  E8 A1 7E 3B 00                  call 0x140b82870
007CA9CF  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
007CA9D3  3D 0D 00 00 C0                  cmp eax, 0xc000000d
007CA9D8  74 0E                           je 0x1407ca9e8
007CA9DA  05 C1 FF FF 3F                  add eax, 0x3fffffc1
007CA9DF  41 3B C6                        cmp eax, r14d
007CA9E2  0F 87 9C 00 00 00               ja 0x1407caa84
007CA9E8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007CA9F1  66 01 98 E4 01 00 00            add word ptr [rax + 0x1e4], bx
007CA9F8  90                              nop
007CA9F9  49 8D BF F8 B6 00 00            lea rdi, [r15 + 0xb6f8]
007CAA00  45 33 C0                        xor r8d, r8d
007CAA03  33 D2                           xor edx, edx
007CAA05  48 8B CF                        mov rcx, rdi
007CAA08  E8 23 58 A4 FF                  call 0x140210230
007CAA0D  48 8B F0                        mov rsi, rax
007CAA10  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
007CAA16  73 0E                           jae 0x1407caa26
007CAA18  4C 8B C7                        mov r8, rdi
007CAA1B  48 8B D0                        mov rdx, rax
007CAA1E  48 8B CF                        mov rcx, rdi
007CAA21  E8 6A 52 A4 FF                  call 0x14020fc90
007CAA26  48 85 F6                        test rsi, rsi
007CAA29  74 04                           je 0x1407caa2f
007CAA2B  44 88 76 0A                     mov byte ptr [rsi + 0xa], r14b
007CAA2F  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
007CAA34  49 8B CF                        mov rcx, r15
007CAA37  E8 04 CD E8 FF                  call 0x140657740
007CAA3C  44 39 64 24 60                  cmp dword ptr [rsp + 0x60], r12d
007CAA41  75 0F                           jne 0x1407caa52
007CAA43  BA 05 00 00 00                  mov edx, 5
007CAA48  49 8B CF                        mov rcx, r15
007CAA4B  E8 74 D0 E8 FF                  call 0x140657ac4
007CAA50  EB 03                           jmp 0x1407caa55
007CAA52  45 8A F4                        mov r14b, r12b
007CAA55  F0 48 0F C1 1F                  lock xadd qword ptr [rdi], rbx
007CAA5A  80 E3 06                        and bl, 6
007CAA5D  80 FB 02                        cmp bl, 2
007CAA60  75 08                           jne 0x1407caa6a
007CAA62  48 8B CF                        mov rcx, rdi
007CAA65  E8 66 B3 A9 FF                  call 0x140265dd0
007CAA6A  48 8B CF                        mov rcx, rdi
007CAA6D  E8 8E 6B B1 FF                  call 0x1402e1600
007CAA72  E8 39 2E A9 FF                  call 0x14025d8b0
007CAA77  45 84 F6                        test r14b, r14b
007CAA7A  74 08                           je 0x1407caa84
007CAA7C  49 8B CF                        mov rcx, r15
007CAA7F  E8 58 F1 FF FF                  call 0x1407c9bdc
007CAA84  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
007CAA88  48 81 C4 D0 01 00 00            add rsp, 0x1d0
007CAA8F  41 5F                           pop r15
007CAA91  41 5E                           pop r14
007CAA93  41 5D                           pop r13
007CAA95  41 5C                           pop r12
007CAA97  5F                              pop rdi
007CAA98  5E                              pop rsi
007CAA99  5B                              pop rbx
007CAA9A  C3                              ret
007CAA9B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SLUpdateLicenseDataInternal(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int8 v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m11C;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int8 v_stack_m129;
    unsigned __int16 v_stack_m12B;
    unsigned int v_stack_m12F;
    unsigned __int8 v_stack_m130;
    unsigned __int64 v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned __int64 v_stack_m148;
    unsigned int v_stack_m14C;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned int v_stack_m17C;
    unsigned int v_stack_m180;
    unsigned __int64 v_stack_m190;
    unsigned int v_stack_m194;
    unsigned int v_stack_m198;
    unsigned __int64 v_stack_m1A0;
    unsigned int v_stack_m1A4;
    unsigned int v_stack_m1A8;
    unsigned __int64 v_stack_m1B0;
    unsigned __int64 v_stack_m1B8;
    unsigned int v_stack_m1C0;
    unsigned __int8 v_stack_m1C2;
    unsigned __int8 v_stack_m1C3;
    unsigned __int8 v_stack_m1C4;
    unsigned int v_stack_m1C8;
    unsigned __int64 v_stack_m1D8;
    unsigned int v_stack_m1E0;
    unsigned int v_stack_m1E8;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned int v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned __int64 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned int v_stack_mF8;
    unsigned __int8 v_stack_mF9;
    unsigned __int16 v_stack_mFB;
    unsigned int v_stack_mFF;
    unsigned __int8 v_stack_p18;

    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (464);
    a1 = 0;
    v_stack_m1C2 = 0;
    v_stack_m1C4 = 0;
    v_stack_p18 = 0;
    *(unsigned __int64 *)(v_rsp - 376) = 0;
    result = 0;
    v_stack_mE0 = v_xmm0;
    v_stack_mD0 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 192) = 0;
    v_stack_mB8 = 0;
    *(unsigned __int64 *)(v_rsp - 384) = 0;
    v_stack_m1A0 = 0;
    v_stack_m160 = 0;
    v_stack_m170 = 0;
    v_rsi = 0;
    v_stack_m1B0 = 0;
    v_stack_m1C0 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1A8 = 0;
    v_stack_m194 = 0;
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
    if (a3 == 0) goto loc_007CA890;
    if (((unsigned int)(a2 - 25)) > 0x13FE7ULL) goto loc_007CA890;
    if ((((unsigned __int8)(a3)) & (3)) != 0) goto loc_007CA890;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3)))) > ((unsigned int)((unsigned int)(0x14000ULL)))) goto loc_007CA87C;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4)))) > ((unsigned int)((unsigned int)(0x14000ULL)))) goto loc_007CA87C;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 8)))) > ((unsigned int)((unsigned int)(0x14000ULL)))) goto loc_007CA87C;
    v_r12 = (a3 + 20) + ((unsigned int)(*(unsigned int *)(a3 + 4)));
    if ((((unsigned __int8)(v_r12)) & (3)) == 0) goto loc_007C9D25;
loc_007C9D08:
loc_007C9D0E:
    v_stack_m1C8 = 0xC000000DULL;
    v_rbx = (v_rbx) | (-1);
loc_007C9D1A:
loc_007C9D1D:
    goto loc_007CA89F;
loc_007C9D25:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a3 + 4)) + 20) + ((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 8)))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a3))))) goto loc_007C9D08;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3)))) != ((unsigned int)((unsigned int)((unsigned int)(a2))))) goto loc_007C9D0E;
    if ((*(unsigned int *)(a3 + 16)) != 1) goto loc_007C9D0E;
    v_stack_m1C8 = 0;
    *(unsigned __int8 *)(a1 + 46856) = 0;
    v_stack_m80 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484)) - (1));
    *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484) = (unsigned __int16)(result);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 46840, a2, a3, (unsigned int)(*(unsigned int *)(a3 + 8)));
    result = 0;
    if (!(condition_is_equal)) {
        a4 = a1 + 46840;
        a3 = 0;
        a2 = 0;
        a1 = a1 + 46840;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    v_rsi = 0;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_stack_m190 = *(unsigned __int64 *)(a1);
    result = v_stack_m1C4;
    if (*(unsigned __int64 *)(a1) == 0) { result = 1; }
    v_stack_m1C4 = (unsigned __int8)(result);
    result = ExpReducedLicenseData(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_007C9DE1;
    if (*(unsigned __int64 *)(a1) != 0) goto loc_007C9DFB;
    v_stack_m1C8 = 0xC0000001ULL;
    goto loc_007C9E91;
loc_007C9DE1:
    if (*(unsigned __int64 *)(a1) != 0) goto loc_007C9DFB;
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(a3 + 12))))) == 0) goto loc_007C9DFB;
    v_stack_m1C8 = 0xC000000DULL;
    goto loc_007C9E91;
loc_007C9DFB:
    v_stack_m1C2 = 0;
    if (*(unsigned __int64 *)(a1) != 0) goto loc_007C9E91;
    if (*(unsigned __int64 *)(a1 + 46832) == 0) goto loc_007C9E91;
    if ((*(unsigned __int8 *)(a1 + 46992)) != 0) goto loc_007C9E91;
    if ((*(unsigned int *)(a3)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 46832)))))) goto loc_007C9E91;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4)))) != (*(unsigned int *)(*(unsigned __int64 *)(a1 + 46832) + 4))) goto loc_007C9E91;
    if ((*(unsigned int *)(a3 + 8)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 46832) + 8))))) goto loc_007C9E91;
    if ((*(unsigned int *)(a3 + 12)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 46832) + 12))))) goto loc_007C9E91;
    if ((*(unsigned int *)(a3 + 16)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 46832) + 16))))) goto loc_007C9E91;
    a1 = (*(unsigned __int64 *)(a1 + 46832)) + (20);
    result = RtlCompareMemory(a1, a3 + 20, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4)))), a4);
    result = (unsigned int)(*(unsigned int *)(a3 + 4));
    if (result == ((unsigned int)(*(unsigned int *)(a3 + 4)))) {
        a1 = *(unsigned __int64 *)(a1 + 46832);
        a3 = *(unsigned int *)(a3 + 8);
        result = *(unsigned int *)(a1 + 4);
        a1 = (a1) + (20);
        a1 = (a1) + (result);
        a2 = 0;
        result = RtlCompareMemory(a1, a2, a3, a4);
        a1 = result;
        result = *(unsigned int *)(a3 + 8);
        a2 = 0;
        if (a1 == result) { a2 = 1; }
        v_stack_m1C2 = (unsigned __int8)(a2);
    }
    result = 17;
    if (a1 != result) {
        a1 = a1 + 46840;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(a1 + 46840, a2, a3, a4);
    result = KeLeaveCriticalRegion(a1 + 46840, a2, a3, a4);
    if (v_stack_m1C8 < 0) goto loc_007CA86E;
    if (v_stack_m1C2 != 1) goto loc_007CA0A3;
    v_rbx = (a1 + 46840) | (-1);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 46840, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 46840;
        a2 = result;
        a1 = a1 + 46840;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    v_r12 = 0;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = ExpGetLicenseTamperState(a1, v_stack_m1A8, a3, a4);
    v_rsi = (v_stack_m1A8 != 0) ? 1 : 0;
    v_stack_m14C = 0;
    v_stack_m12F = 0;
    v_stack_m12B = 0;
    v_stack_m129 = 0;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 46824))) == 0) goto loc_007C9F71;
    if (a1 + 24 != 0) goto loc_007C9F71;
    goto loc_007CA03D;
loc_007C9F71:
    v_stack_m158 = 0;
    v_stack_m148 = 0;
    v_stack_m150 = 0;
    v_stack_m140 = 0;
    v_stack_m138 = 0x2A30ULL;
    v_stack_m130 = 1;
    result = ExpLicUpdateChecksum(a3 + 20, (unsigned int)(*(unsigned int *)(a1 + 46824)), v_stack_m158, a1 + 24);
    if ((unsigned int)(result) != 0) goto loc_007C9FEE;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 46824))) == 0) goto loc_007C9FEE;
    result = ((unsigned int)(*(unsigned int *)(a1 + 46824))) << (4);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (0xC0000095ULL));
    if (result <= ((unsigned int)(0xFFFFFFFFULL))) {
        a3 = v_stack_m158;
        a1 = a1 + 24;
        result = ExpLicUpdateChecksum(a1, (unsigned int)(0xFFFFFFFFULL), a3, a1 + 24);
        a1 = (unsigned int)(result);
    }
    if ((unsigned int)(a1) != 0) {
        v_stack_m158 = 0;
        v_stack_m150 = 4;
    }
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = v_xmm1;
    v_stack_m90 = v_xmm0;
    result = 0;
    if ((unsigned int)(a1) == 0) { result = (unsigned int)(a1); }
loc_007CA03D:
    if (!(sign_flag)) {
        a4 = 1;
        a3 = 7;
        a2 = v_stack_mB0;
        a1 = a1;
        result = sub_00966DF0(a1, a2, a3, a4);
    }
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = a1 + 46840;
        result = ExfTryToWakePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(a1 + 46840, a2, a3, a4);
    result = KeLeaveCriticalRegion(a1 + 46840, a2, a3, a4);
    if ((unsigned __int8)(v_rsi) != 0) {
        a1 = a1;
        result = SLSendPolicyChangeNotifications(a1, a2, a3, a4);
    }
    v_stack_m1C8 = 0x40000000ULL;
loc_007CA09C:
    v_rsi = 0;
    goto loc_007CA89F;
loc_007CA0A3:
    v_stack_mE0 = 48;
    v_stack_mD8 = 0;
    v_stack_mC8 = 544;
    v_stack_mD0 = 0;
    v_stack_mC0 = v_xmm0;
    v_stack_m180 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 46840)));
    v_stack_m17C = 0;
    v_stack_m1D8 = 0;
    v_stack_m1E0 = 0x8000000ULL;
    v_stack_m1E8 = 4;
    result = ZwCreateSection(v_stack_m178, (unsigned int)(0xF0007ULL), v_stack_mE0, v_stack_m180);
    v_stack_m1C8 = (unsigned int)(result);
    if (sign_flag) goto loc_007CA86E;
    v_stack_m168 = 0;
    v_stack_m1E0 = 0;
    v_stack_m1E8 = v_stack_m168;
    a4 = 0;
    a3 = 0;
    a2 = 0;
    result = ObReferenceObjectByHandle(v_stack_m178, a2, a3, a4);
    v_stack_m170 = v_stack_m168;
    v_stack_m1C8 = (unsigned int)(result);
    result = ZwClose(v_stack_m178, a2, a3, a4);
    result = 0;
    if (sign_flag) goto loc_007CA86C;
    v_stack_mF0 = 0;
    result = MmMapViewInSessionSpace(v_stack_m168, v_stack_m1A0, v_stack_mF0, a4);
    v_stack_m1C8 = (unsigned int)(result);
    v_rsi = 0;
    if (sign_flag) goto loc_007CA86E;
    *(unsigned __int64 *)(v_stack_m1A0) = v_xmm0;
    *(unsigned int *)(v_stack_m1A0 + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 46840 + 16)));
    result = memcpy(v_stack_m1A0 + 20, a1 + 46840 + 20, (unsigned int)(*(unsigned int *)(a1 + 46840 + 4)), a4);
    a1 = (v_stack_m1A0 + 20) + ((unsigned int)(*(unsigned int *)(a1 + 46840 + 4)));
    result = memcpy(a1, 0, (unsigned int)(*(unsigned int *)(a1 + 46840 + 8)), a4);
    a1 = (v_stack_m1A0 + 20) + ((unsigned int)(*(unsigned int *)(v_stack_m1A0 + 4)));
    if ((*(unsigned int *)(v_stack_m1A0 + 8)) != 4) goto loc_007CA853;
    v_r12 = 0;
    if (a1 == 0) goto loc_007CA853;
    if ((*(unsigned int *)(a1)) != 69) goto loc_007CA853;
    v_stack_m1E8 = v_stack_m1C0;
    a4 = 0;
    a3 = 0;
    result = sub_007C8C1C(v_stack_m1A0, 1, a3, a4);
    v_stack_m1C8 = (unsigned int)(result);
    v_rbx = ((unsigned int)((unsigned int)(result))) | (-1);
    if (((unsigned int)(result)) != 0xC0000023ULL) goto loc_007CA346;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 46840, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = a1 + 46840;
        a3 = 0;
        a2 = 0;
        a1 = a1 + 46840;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = (unsigned int)(((unsigned int)(0xB6DULL)) & (0xC000000DULL));
    v_stack_m1C8 = (unsigned int)(result);
    v_rsi = 0;
    result = 17;
    if (!(condition_is_equal)) {
        a1 = a1 + 46840;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(a1 + 46840, a2, a3, a4);
    result = KeLeaveCriticalRegion(a1 + 46840, a2, a3, a4);
    if (v_stack_m1C8 < 0) goto loc_007C9D1A;
    a2 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m1C0)))) << (4);
    result = ExAllocatePool2(256, a2, (unsigned int)(0x20534C53ULL), a4);
    v_stack_m1B8 = result;
    if (result != 0) goto loc_007CA30B;
    v_stack_m1C8 = 0xC0000017ULL;
    goto loc_007C9D1D;
loc_007CA30B:
    v_stack_m1E8 = 0;
    a2 = 0;
    result = sub_007C8C1C(v_stack_m1A0, a2, result, (unsigned int)(v_stack_m1C0));
    v_stack_m1C8 = (unsigned int)(result);
    if (sign_flag) goto loc_007CA34F;
    result = qsort(result, (unsigned int)(v_stack_m1C0), 16, v_rip - 7171);
    goto loc_007CA34F;
loc_007CA346:
    v_rsi = 0;
loc_007CA34F:
    if (!sign_flag) goto loc_007CA374;
    if (((unsigned int)((unsigned int)(v_stack_m1C8))) != 0xC000003EULL) goto loc_007CA89F;
    v_stack_m1C8 = 0xC000000DULL;
    goto loc_007CA89F;
loc_007CA374:
    v_stack_m1C3 = 0;
    v_stack_m78 = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484)) - (1));
    *(unsigned __int16 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 484) = (unsigned __int16)(result);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 46840, a2, a3, v_rip - 7171);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = a1 + 46840;
        a3 = 0;
        a2 = 0;
        a1 = a1 + 46840;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    v_rsi = 0;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    if (v_stack_m190 != 0) goto loc_007CA4FF;
    v_stack_m1A4 = 0;
    v_stack_m198 = 0;
loc_007CA3F1:
    if (0 >= v_stack_m1C0) goto loc_007CA4C5;
    if (0 >= (*(unsigned int *)(a1 + 46824))) goto loc_007CA4C5;
    v_rdi = (0) << (4);
    v_rdi = (v_rdi) + (v_stack_m1B8);
    a2 = (0) << (4);
    a2 = (a2) + (24);
    a2 = (a2) + (a1);
    result = sub_007C8730(v_rdi, a2, a3, a4);
    v_stack_mF8 = (unsigned int)(result);
    v_stack_mE8 = *(unsigned __int64 *)(v_rdi + 8);
    a1 = (0 + 2) + (0 + 2);
    v_stack_m70 = *(unsigned __int64 *)(a1 + a1 * 8);
    v_rsi = 0;
    if (!sign_flag) goto loc_007CA479;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi + 8) + 8)))) & (2)) == 0) goto loc_007CA46C;
loc_007CA462:
    v_stack_m1C3 = 1;
    goto loc_007CA4F9;
loc_007CA46C:
    v_r12 = (unsigned int)((0) + (1));
    v_stack_m1A4 = (unsigned int)(v_r12);
loc_007CA474:
    goto loc_007CA3F1;
loc_007CA479:
    if (condition_is_less_or_equal) goto loc_007CA485;
loc_007CA47B:
    v_r13 = (unsigned int)((0) + (1));
    v_stack_m198 = (unsigned int)(v_r13);
    goto loc_007CA474;
loc_007CA485:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rdi + 8) + 8)))) & (2)) == 0) goto loc_007CA4BB;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rdi + 8) + 6)) != ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + a1 * 8) + 6)))) goto loc_007CA462;
    result = (*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + a1 * 8) + 2)) + (16);
    a2 = (*(unsigned __int64 *)(a1 + a1 * 8)) + (result);
    a4 = (*(unsigned __int64 *)(v_rdi + 8)) + (16);
    a1 = (*(unsigned __int16 *)(*(unsigned __int64 *)(v_rdi + 8) + 2)) + (a4);
    result = memcmp(a1, a2, (unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + a1 * 8) + 6))), a4);
    if ((unsigned int)(result) != 0) goto loc_007CA462;
loc_007CA4BB:
    v_r12 = (unsigned int)((v_r12) + (1));
    v_stack_m1A4 = (unsigned int)(v_r12);
    goto loc_007CA47B;
loc_007CA4C5:
loc_007CA4CA:
    if (((unsigned int)(v_r12)) >= v_stack_m1C0) goto loc_007CA4F9;
    result = ((unsigned int)((unsigned int)(v_r12))) + ((unsigned int)((unsigned int)(v_r12)));
    v_stack_mE8 = *(unsigned __int64 *)(v_stack_m1B8 + result * 8 + 8);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m1B8 + result * 8 + 8) + 8)))) & (2)) != 0) goto loc_007CA462;
    v_r12 = (unsigned int)((v_r12) + (1));
    v_stack_m1A4 = (unsigned int)(v_r12);
    goto loc_007CA4CA;
loc_007CA4F9:
loc_007CA4FF:
    result = 17;
    if (!(condition_is_equal)) {
        a1 = a1 + 46840;
        result = ExfReleasePushLockShared(a1, a2, (unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + a1 * 8) + 6))), a4);
    }
    result = KeAbPostRelease(a1 + 46840, a2, (unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + a1 * 8) + 6))), a4);
    result = KeLeaveCriticalRegion(a1 + 46840, a2, (unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + a1 * 8) + 6))), a4);
    result = ObfReferenceObject(v_stack_m170, a2, (unsigned int)((unsigned int)(*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + a1 * 8) + 6))), a4);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 46840, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 46840;
        a2 = result;
        a1 = a1 + 46840;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    v_r10 = 0;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_stack_m11C = 0;
    v_stack_mFF = 0;
    v_stack_mFB = 0;
    v_stack_mF9 = 0;
    if (v_stack_m1A0 == 0) goto loc_007CA692;
    if ((unsigned int)((unsigned int)(v_stack_m1C0)) == 0) goto loc_007CA5C4;
    if (v_stack_m1B8 == 0) goto loc_007CA696;
loc_007CA5C4:
    v_stack_m128 = 0;
    v_stack_m118 = 0;
    v_stack_m120 = 0;
    v_stack_m110 = 0;
    v_stack_m108 = 0x2A30ULL;
    v_stack_m100 = 1;
    result = ExpLicUpdateChecksum(v_stack_m1A0 + 20, a2, v_stack_m128, v_stack_m1B8);
    if ((unsigned int)(result) != 0) goto loc_007CA641;
    if ((unsigned int)((unsigned int)(v_stack_m1C0)) == 0) goto loc_007CA641;
    result = ((unsigned int)(v_stack_m1C0)) << (4);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) & (0xC0000095ULL));
    if (result <= ((unsigned int)(0xFFFFFFFFULL))) {
        a3 = v_stack_m128;
        a1 = v_stack_m1B8;
        result = ExpLicUpdateChecksum(a1, (unsigned int)(0xFFFFFFFFULL), a3, v_stack_m1B8);
        a1 = (unsigned int)(result);
    }
    if ((unsigned int)(a1) != 0) {
        v_stack_m128 = 0;
        v_stack_m120 = 4;
    }
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = v_xmm1;
    v_stack_m90 = v_xmm0;
    v_rdi = 0;
    if ((unsigned int)(a1) == 0) { v_rdi = (unsigned int)(a1); }
    goto loc_007CA69B;
loc_007CA692:
loc_007CA696:
loc_007CA69B:
    v_stack_m1C8 = (unsigned int)((unsigned int)(0xC000000DULL));
    if (sign_flag) goto loc_007CA7CC;
    result = sub_00966DF0(a1, v_stack_mB0, 7, 1);
    v_stack_m1B0 = *(unsigned __int64 *)(a1 + 16);
    v_stack_m160 = *(unsigned __int64 *)(a1 + 46832);
    *(unsigned __int64 *)(a1 + 16) = v_stack_m170;
    *(unsigned __int64 *)(a1 + 46832) = v_stack_m1A0;
    v_r13 = 0;
    v_stack_m1A0 = 0;
    result = PsGetCurrentServerSilo(a1, v_stack_mB0, 7, 1);
    result = PsIsHostSilo(result, v_stack_mB0, 7, 1);
    if ((unsigned __int8)(result) != 0) goto loc_007CA70E;
    if (*(unsigned __int64 *)(a1) != 0) {
        a2 = 0x69534C53ULL;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1), a2, 7, 1);
    }
    *(unsigned __int64 *)(a1) = 0;
    v_stack_p18 = (unsigned __int8)(*(unsigned __int8 *)(a1 + 46992));
    *(unsigned __int8 *)(a1 + 46992) = 0;
    a3 = ((unsigned int)(*(unsigned int *)(a1 + 46824))) << (4);
    a2 = 0;
    result = memset(a1 + 24, a2, a3, 1);
    *(unsigned int *)(a1 + 46824) = 0;
    if (v_stack_m1B8 != 0) {
        a3 = (unsigned int)((unsigned int)(v_stack_m1C0));
        a3 = (a3) << (4);
        a2 = v_stack_m1B8;
        a1 = a1 + 24;
        result = memcpy(a1, a2, a3, 1);
        *(unsigned int *)(a1 + 46824) = (unsigned int)((unsigned int)(v_stack_m1C0));
    }
    *(unsigned __int8 *)(a1 + 46828) = 1;
    result = ExpGetLicenseTamperState(a1, v_stack_m194, a3, 1);
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 46832) + 12))) & (1));
    result = v_stack_m1C4;
    if (condition_is_not_equal) { result = 1; }
    v_stack_m1C4 = (unsigned __int8)(result);
    a2 = (unsigned int)((a2) + ((unsigned int)(a2)));
    result = ExpSetLicenseTamperState(a1, a2, a3, 1);
    result = ExpGetLicenseTamperState(a1, v_stack_m1A8, a3, 1);
    a2 = 0;
    if (((unsigned int)((unsigned int)(v_stack_m194))) == ((unsigned int)((unsigned int)(v_stack_m1A8)))) goto loc_007CA7C7;
    if ((unsigned int)((unsigned int)(v_stack_m194)) == 0) goto loc_007CA7C2;
    if ((unsigned int)((unsigned int)(v_stack_m1A8)) != 0) goto loc_007CA7C7;
loc_007CA7C2:
    goto loc_007CA7D4;
loc_007CA7C7:
    goto loc_007CA7D4;
loc_007CA7CC:
loc_007CA7D4:
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = a1 + 46840;
        result = ExfTryToWakePushLock(a1, a2, a3, 1);
    }
    result = KeAbPostRelease(a1 + 46840, a2, a3, 1);
    result = KeLeaveCriticalRegion(a1 + 46840, a2, a3, 1);
    v_rsi = 0;
    if (sign_flag) goto loc_007CA89A;
    if (v_stack_m190 != 0) goto loc_007CA827;
    result = sub_007C8D5C(a1, a2, a3, 1);
    v_stack_m1C8 = (unsigned int)(result);
    if (sign_flag) goto loc_007CA89A;
loc_007CA827:
    if (0 != 0) goto loc_007CA831;
    result = v_stack_m190;
    if (v_stack_m190 == 0) {
        a1 = a1;
        result = SLSendPolicyChangeNotifications(a1, a2, a3, 1);
    }
    v_stack_m1C8 = 0;
    if (v_stack_m1C3 != 1) goto loc_007CA89F;
    v_stack_m1C8 = 263;
    goto loc_007CA89F;
loc_007CA853:
    v_stack_m1C8 = 0xC000003FULL;
    v_rbx = (v_rbx) | (-1);
    goto loc_007CA09C;
loc_007CA86C:
    v_rsi = 0;
loc_007CA86E:
    v_rbx = (v_rbx) | (-1);
    goto loc_007CA89F;
loc_007CA87C:
    v_stack_m1C8 = 0xC0000040ULL;
loc_007CA884:
    v_rbx = (v_rbx) | (-1);
    goto loc_007CA89F;
loc_007CA890:
    v_stack_m1C8 = 0xC000000DULL;
    goto loc_007CA884;
loc_007CA89A:
loc_007CA89F:
    if (v_stack_p18 == 0) goto loc_007CA8BE;
    if ((*(unsigned __int8 *)(a1 + 46992)) == 0) {
        a1 = v_rip - 8025537;
        result = sub_007C7F80(a1, a2, a3, 1);
    }
    if (v_stack_m1C4 == 0) goto loc_007CA96E;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 46840, a2, a3, 1);
    result = a1 + 46840;
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 46840;
        a2 = result;
        a1 = a1 + 46840;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, 1);
        result = a1 + 46840;
    }
    v_rdi = a1 + 46840;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
        v_rdi = result;
    }
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    a4 = 0;
    result = sub_00966DF0(a1, v_stack_m68, a4 + 32, a4);
    result = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(result)) == 2) {
        a1 = v_rdi;
        result = ExfTryToWakePushLock(a1, v_stack_m68, a4 + 32, a4);
    }
    result = KeAbPostRelease(v_rdi, v_stack_m68, a4 + 32, a4);
    result = KeLeaveCriticalRegion(v_rdi, v_stack_m68, a4 + 32, a4);
loc_007CA96E:
    result = v_stack_m170;
    if (v_stack_m170 != 0) {
        a1 = v_stack_m170;
        result = ObfDereferenceObject(a1, v_stack_m68, a4 + 32, a4);
    }
    if (v_stack_m1B0 != 0) {
        a1 = v_stack_m1B0;
        result = ObfDereferenceObject(a1, v_stack_m68, a4 + 32, a4);
    }
    v_r12 = 0;
    if (v_stack_m1A0 != 0) {
        a2 = 1;
        a1 = v_stack_m1A0;
        result = MiRemoveFromSystemSpace(a1, a2, a4 + 32, a4);
    }
    result = v_stack_m160;
    if (v_stack_m160 != 0) {
        a2 = 1;
        a1 = v_stack_m160;
        result = MiRemoveFromSystemSpace(a1, a2, a4 + 32, a4);
    }
    if (v_stack_m1B8 != 0) {
        a2 = 0;
        a1 = v_stack_m1B8;
        result = ExFreePoolWithTag(a1, a2, a4 + 32, a4);
    }
    if (((unsigned int)((unsigned int)(v_stack_m1C8))) == 0xC000000DULL) goto loc_007CA9E8;
    result = (unsigned int)(((unsigned int)(v_stack_m1C8)) + (0x3FFFFFC1ULL));
    if (((unsigned int)(result)) > 1) goto loc_007CAA84;
loc_007CA9E8:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1 + 46840, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1 + 46840;
        a2 = result;
        a1 = a1 + 46840;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = ExpGetLicenseTamperState(a1, v_stack_m1A8, a3, a4);
    if (v_stack_m1A8 != 0) goto loc_007CAA52;
    result = ExpSetLicenseTamperState(a1, 5, a3, a4);
    goto loc_007CAA55;
loc_007CAA52:
loc_007CAA55:
    v_rbx = (unsigned __int8)((v_rbx) & (6));
    if (((unsigned __int8)(v_rbx)) == 2) {
        a1 = a1 + 46840;
        result = ExfTryToWakePushLock(a1, 5, a3, a4);
    }
    result = KeAbPostRelease(a1 + 46840, 5, a3, a4);
    result = KeLeaveCriticalRegion(a1 + 46840, 5, a3, a4);
    if (0 != 0) {
        a1 = a1;
        result = SLSendPolicyChangeNotifications(a1, 5, a3, a4);
    }
    v_rsp = (v_rsp) + (464);
    return (unsigned int)(v_stack_m1C8);
}
```

## 5. (Beta) C Style

```c
int64_t SLUpdateLicenseDataInternal(void *Arg1, void *Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint8_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m11C;
    uint32_t v_stack_m120;
    uint64_t v_stack_m128;
    uint8_t v_stack_m129;
    uint16_t v_stack_m12B;
    uint32_t v_stack_m12F;
    uint8_t v_stack_m130;
    uint64_t v_stack_m138;
    uint64_t v_stack_m140;
    uint64_t v_stack_m148;
    uint32_t v_stack_m14C;
    uint32_t v_stack_m150;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint32_t v_stack_m17C;
    uint32_t v_stack_m180;
    uint64_t v_stack_m190;
    uint32_t v_stack_m194;
    uint32_t v_stack_m198;
    uint64_t v_stack_m1A0;
    uint32_t v_stack_m1A4;
    uint32_t v_stack_m1A8;
    uint64_t v_stack_m1B0;
    uint64_t v_stack_m1B8;
    uint32_t v_stack_m1C0;
    uint8_t v_stack_m1C2;
    uint8_t v_stack_m1C3;
    uint8_t v_stack_m1C4;
    uint32_t v_stack_m1C8;
    uint64_t v_stack_m1D8;
    uint32_t v_stack_m1E0;
    uint32_t v_stack_m1E8;
    uint64_t v_stack_m48;
    uint64_t v_stack_m58;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m90;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint32_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint64_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint32_t v_stack_mF8;
    uint8_t v_stack_mF9;
    uint16_t v_stack_mFB;
    uint32_t v_stack_mFF;
    uint8_t v_stack_p18;

    *(void **)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (464);
    Arg1 = 0;
    v_stack_m1C2 = 0;
    v_stack_m1C4 = 0;
    v_stack_p18 = 0;
    *(uint64_t *)(local_rsp - 0x178) = 0;
    result = 0;
    v_stack_mE0 = v_xmm0;
    v_stack_mD0 = v_xmm0;
    *(uint64_t *)(local_rsp - 0xC0) = 0;
    v_stack_mB8 = 0;
    *(uint64_t *)(local_rsp - 0x180) = 0;
    v_stack_m1A0 = 0;
    v_stack_m160 = 0;
    v_stack_m170 = 0;
    local_rsi = 0;
    v_stack_m1B0 = 0;
    v_stack_m1C0 = 0;
    v_stack_m1B8 = 0;
    v_stack_m1A8 = 0;
    v_stack_m194 = 0;
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = v_xmm0;
    v_stack_m90 = v_xmm0;
    if (Arg3 == 0) goto loc_007CA890;
    if (((uint32_t)(Arg2 - 25)) > 0x13FE7ULL) goto loc_007CA890;
    if ((((uint8_t)(Arg3)) & (3)) != 0) goto loc_007CA890;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))) > ((uint32_t)((uint32_t)(0x14000ULL)))) goto loc_007CA87C;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x4)))) > ((uint32_t)((uint32_t)(0x14000ULL)))) goto loc_007CA87C;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x8)))) > ((uint32_t)((uint32_t)(0x14000ULL)))) goto loc_007CA87C;
    local_r12 = (Arg3 + 20) + ((uint32_t)(*(uint32_t *)(Arg3 + 0x4)));
    if ((((uint8_t)(local_r12)) & (3)) == 0) goto loc_007C9D25;
loc_007C9D08:
loc_007C9D0E:
    v_stack_m1C8 = 0xC000000DULL;
    local_rbx = (local_rbx) | (-1);
loc_007C9D1A:
loc_007C9D1D:
    goto loc_007CA89F;
loc_007C9D25:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3 + 0x4)) + 20) + ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x8)))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3))))) goto loc_007C9D08;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)))) != ((uint32_t)((uint32_t)((uint32_t)(Arg2))))) goto loc_007C9D0E;
    if ((*(uint32_t *)(Arg3 + 0x10)) != 1) goto loc_007C9D0E;
    v_stack_m1C8 = 0;
    *(uint8_t *)(arg1 + 0xB708) = 0;
    v_stack_m80 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4)) - (1));
    *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4) = (uint16_t)(result);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 46840, Arg2, Arg3, (uint32_t)(*(uint32_t *)(Arg3 + 0x8)));
    result = 0;
    if (!(condition_is_equal)) {
        a4 = Arg1 + 46840;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = Arg1 + 46840;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    local_rsi = 0;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    v_stack_m190 = *(uint64_t *)(arg1);
    result = v_stack_m1C4;
    if (*(uint64_t *)(arg1) == 0) { result = 1; }
    v_stack_m1C4 = (uint8_t)(result);
    result = ExpReducedLicenseData(Arg1, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_007C9DE1;
    if (*(uint64_t *)(arg1) != 0) goto loc_007C9DFB;
    v_stack_m1C8 = 0xC0000001ULL;
    goto loc_007C9E91;
loc_007C9DE1:
    if (*(uint64_t *)(arg1) != 0) goto loc_007C9DFB;
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(Arg3 + 0xC))))) == 0) goto loc_007C9DFB;
    v_stack_m1C8 = 0xC000000DULL;
    goto loc_007C9E91;
loc_007C9DFB:
    v_stack_m1C2 = 0;
    if (*(uint64_t *)(arg1) != 0) goto loc_007C9E91;
    if (*(uint64_t *)(arg1 + 0xB6F0) == 0) goto loc_007C9E91;
    if ((*(uint8_t *)(arg1 + 0xB790)) != 0) goto loc_007C9E91;
    if ((*(uint32_t *)(Arg3)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xB6F0)))))) goto loc_007C9E91;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x4)))) != (*(uint32_t *)(*(uint64_t *)(arg1 + 0xB6F0) + 0x4))) goto loc_007C9E91;
    if ((*(uint32_t *)(Arg3 + 0x8)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xB6F0) + 0x8))))) goto loc_007C9E91;
    if ((*(uint32_t *)(Arg3 + 0xC)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xB6F0) + 0xC))))) goto loc_007C9E91;
    if ((*(uint32_t *)(Arg3 + 0x10)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xB6F0) + 0x10))))) goto loc_007C9E91;
    Arg1 = (*(uint64_t *)(arg1 + 0xB6F0)) + (20);
    result = RtlCompareMemory(Arg1, Arg3 + 20, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x4)))), a4);
    result = (uint32_t)(*(uint32_t *)(Arg3 + 0x4));
    if (result == ((uint32_t)(*(uint32_t *)(Arg3 + 0x4)))) {
        Arg1 = *(uint64_t *)(arg1 + 0xB6F0);
        Arg3 = *(uint32_t *)(Arg3 + 0x8);
        result = *(uint32_t *)(arg1 + 0x4);
        Arg1 = (Arg1) + (20);
        Arg1 = (Arg1) + (result);
        Arg2 = 0;
        result = RtlCompareMemory(Arg1, Arg2, Arg3, a4);
        Arg1 = result;
        result = *(uint32_t *)(Arg3 + 0x8);
        Arg2 = 0;
        if (Arg1 == result) { Arg2 = 1; }
        v_stack_m1C2 = (uint8_t)(Arg2);
    }
    result = 17;
    if (Arg1 != result) {
        Arg1 = Arg1 + 46840;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, a4);
    }
    result = KeAbPostRelease(Arg1 + 46840, Arg2, Arg3, a4);
    result = KeLeaveCriticalRegion(Arg1 + 46840, Arg2, Arg3, a4);
    if (v_stack_m1C8 < 0) goto loc_007CA86E;
    if (v_stack_m1C2 != 1) goto loc_007CA0A3;
    local_rbx = (Arg1 + 46840) | (-1);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 46840, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 46840;
        Arg2 = result;
        Arg1 = Arg1 + 46840;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    local_r12 = 0;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = ExpGetLicenseTamperState(Arg1, v_stack_m1A8, Arg3, a4);
    local_rsi = (v_stack_m1A8 != 0) ? 1 : 0;
    v_stack_m14C = 0;
    v_stack_m12F = 0;
    v_stack_m12B = 0;
    v_stack_m129 = 0;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB6E8))) == 0) goto loc_007C9F71;
    if (Arg1 + 24 != 0) goto loc_007C9F71;
    goto loc_007CA03D;
loc_007C9F71:
    v_stack_m158 = 0;
    v_stack_m148 = 0;
    v_stack_m150 = 0;
    v_stack_m140 = 0;
    v_stack_m138 = 0x2A30ULL;
    v_stack_m130 = 1;
    result = ExpLicUpdateChecksum(Arg3 + 20, (uint32_t)(*(uint32_t *)(arg1 + 0xB6E8)), v_stack_m158, Arg1 + 24);
    if ((uint32_t)(result) != 0) goto loc_007C9FEE;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB6E8))) == 0) goto loc_007C9FEE;
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0xB6E8))) << (4);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (0xC0000095ULL));
    if (result <= ((uint32_t)(0xFFFFFFFFULL))) {
        Arg3 = v_stack_m158;
        Arg1 = Arg1 + 24;
        result = ExpLicUpdateChecksum(Arg1, (uint32_t)(0xFFFFFFFFULL), Arg3, Arg1 + 24);
        Arg1 = (uint32_t)(result);
    }
    if ((uint32_t)(Arg1) != 0) {
        v_stack_m158 = 0;
        v_stack_m150 = 4;
    }
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = v_xmm1;
    v_stack_m90 = v_xmm0;
    result = 0;
    if ((uint32_t)(Arg1) == 0) { result = (uint32_t)(Arg1); }
loc_007CA03D:
    if (!(sign_flag)) {
        a4 = 1;
        Arg3 = 7;
        Arg2 = v_stack_mB0;
        Arg1 = Arg1;
        result = sub_00966DF0(Arg1, Arg2, Arg3, a4);
    }
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = Arg1 + 46840;
        result = ExfTryToWakePushLock(Arg1, Arg2, Arg3, a4);
    }
    result = KeAbPostRelease(Arg1 + 46840, Arg2, Arg3, a4);
    result = KeLeaveCriticalRegion(Arg1 + 46840, Arg2, Arg3, a4);
    if ((uint8_t)(local_rsi) != 0) {
        Arg1 = Arg1;
        result = SLSendPolicyChangeNotifications(Arg1, Arg2, Arg3, a4);
    }
    v_stack_m1C8 = 0x40000000ULL;
loc_007CA09C:
    local_rsi = 0;
    goto loc_007CA89F;
loc_007CA0A3:
    v_stack_mE0 = 48;
    v_stack_mD8 = 0;
    v_stack_mC8 = 544;
    v_stack_mD0 = 0;
    v_stack_mC0 = v_xmm0;
    v_stack_m180 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB6F8)));
    v_stack_m17C = 0;
    v_stack_m1D8 = 0;
    v_stack_m1E0 = 0x8000000ULL;
    v_stack_m1E8 = 4;
    result = ZwCreateSection(v_stack_m178, (uint32_t)(0xF0007ULL), v_stack_mE0, v_stack_m180);
    v_stack_m1C8 = (uint32_t)(result);
    if (sign_flag) goto loc_007CA86E;
    v_stack_m168 = 0;
    v_stack_m1E0 = 0;
    v_stack_m1E8 = v_stack_m168;
    a4 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = ObReferenceObjectByHandle(v_stack_m178, Arg2, Arg3, a4);
    v_stack_m170 = v_stack_m168;
    v_stack_m1C8 = (uint32_t)(result);
    result = ZwClose(v_stack_m178, Arg2, Arg3, a4);
    result = 0;
    if (sign_flag) goto loc_007CA86C;
    v_stack_mF0 = 0;
    result = MmMapViewInSessionSpace(v_stack_m168, v_stack_m1A0, v_stack_mF0, a4);
    v_stack_m1C8 = (uint32_t)(result);
    local_rsi = 0;
    if (sign_flag) goto loc_007CA86E;
    *(uint64_t *)(v_stack_m1A0) = v_xmm0;
    *(uint32_t *)(v_stack_m1A0 + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xB6F8 + 0x10)));
    result = memcpy(v_stack_m1A0 + 20, Arg1 + 46840 + 20, (uint32_t)(*(uint32_t *)(arg1 + 0xB6F8 + 0x4)), a4);
    Arg1 = (v_stack_m1A0 + 20) + ((uint32_t)(*(uint32_t *)(arg1 + 0xB6F8 + 0x4)));
    result = memcpy(Arg1, 0, (uint32_t)(*(uint32_t *)(arg1 + 0xB6F8 + 0x8)), a4);
    Arg1 = (v_stack_m1A0 + 20) + ((uint32_t)(*(uint32_t *)(v_stack_m1A0 + 0x4)));
    if ((*(uint32_t *)(v_stack_m1A0 + 0x8)) != 4) goto loc_007CA853;
    local_r12 = 0;
    if (Arg1 == NULL) goto loc_007CA853;
    if ((*(uint32_t *)(arg1)) != 69) goto loc_007CA853;
    v_stack_m1E8 = v_stack_m1C0;
    a4 = 0;
    Arg3 = 0;
    result = sub_007C8C1C(v_stack_m1A0, 1, Arg3, a4);
    v_stack_m1C8 = (uint32_t)(result);
    local_rbx = ((uint32_t)((uint32_t)(result))) | (-1);
    if (((uint32_t)(result)) != 0xC0000023ULL) goto loc_007CA346;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 46840, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = Arg1 + 46840;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = Arg1 + 46840;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = (uint32_t)(((uint32_t)(0xB6DULL)) & (0xC000000DULL));
    v_stack_m1C8 = (uint32_t)(result);
    local_rsi = 0;
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = Arg1 + 46840;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, a4);
    }
    result = KeAbPostRelease(Arg1 + 46840, Arg2, Arg3, a4);
    result = KeLeaveCriticalRegion(Arg1 + 46840, Arg2, Arg3, a4);
    if (v_stack_m1C8 < 0) goto loc_007C9D1A;
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m1C0)))) << (4);
    result = ExAllocatePool2(256, Arg2, (uint32_t)(0x20534C53ULL), a4);
    v_stack_m1B8 = result;
    if (result != 0) goto loc_007CA30B;
    v_stack_m1C8 = 0xC0000017ULL;
    goto loc_007C9D1D;
loc_007CA30B:
    v_stack_m1E8 = 0;
    Arg2 = 0;
    result = sub_007C8C1C(v_stack_m1A0, Arg2, result, (uint32_t)(v_stack_m1C0));
    v_stack_m1C8 = (uint32_t)(result);
    if (sign_flag) goto loc_007CA34F;
    result = qsort(result, (uint32_t)(v_stack_m1C0), 16, v_rip - 7171);
    goto loc_007CA34F;
loc_007CA346:
    local_rsi = 0;
loc_007CA34F:
    if (!sign_flag) goto loc_007CA374;
    if (((uint32_t)((uint32_t)(v_stack_m1C8))) != 0xC000003EULL) goto loc_007CA89F;
    v_stack_m1C8 = 0xC000000DULL;
    goto loc_007CA89F;
loc_007CA374:
    v_stack_m1C3 = 0;
    v_stack_m78 = *(uint64_t *)(gs_base + (0 + 0x188));
    result = (uint16_t)((*(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4)) - (1));
    *(uint16_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x1E4) = (uint16_t)(result);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 46840, Arg2, Arg3, v_rip - 7171);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = Arg1 + 46840;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = Arg1 + 46840;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    local_rsi = 0;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    if (v_stack_m190 != 0) goto loc_007CA4FF;
    v_stack_m1A4 = 0;
    v_stack_m198 = 0;
loc_007CA3F1:
    if (0 >= v_stack_m1C0) goto loc_007CA4C5;
    if (0 >= (*(uint32_t *)(arg1 + 0xB6E8))) goto loc_007CA4C5;
    local_rdi = (0) << (4);
    local_rdi = (local_rdi) + (v_stack_m1B8);
    Arg2 = (0) << (4);
    Arg2 = (Arg2) + (24);
    Arg2 = (Arg2) + (Arg1);
    result = sub_007C8730(local_rdi, Arg2, Arg3, a4);
    v_stack_mF8 = (uint32_t)(result);
    v_stack_mE8 = *(uint64_t *)(local_rdi + 0x8);
    Arg1 = (0 + 2) + (0 + 2);
    v_stack_m70 = *(uint64_t *)(arg1 + arg1 * 8);
    local_rsi = 0;
    if (!sign_flag) goto loc_007CA479;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi + 0x8) + 0x8)))) & (2)) == 0) goto loc_007CA46C;
loc_007CA462:
    v_stack_m1C3 = 1;
    goto loc_007CA4F9;
loc_007CA46C:
    local_r12 = (uint32_t)((0) + (1));
    v_stack_m1A4 = (uint32_t)(local_r12);
loc_007CA474:
    goto loc_007CA3F1;
loc_007CA479:
    if (condition_is_less_or_equal) goto loc_007CA485;
loc_007CA47B:
    local_r13 = (uint32_t)((0) + (1));
    v_stack_m198 = (uint32_t)(local_r13);
    goto loc_007CA474;
loc_007CA485:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rdi + 0x8) + 0x8)))) & (2)) == 0) goto loc_007CA4BB;
    if ((*(uint16_t *)(*(uint64_t *)(local_rdi + 0x8) + 0x6)) != ((uint16_t)(*(uint16_t *)(*(uint64_t *)(arg1 + arg1 * 8) + 0x6)))) goto loc_007CA462;
    result = (*(uint16_t *)(*(uint64_t *)(arg1 + arg1 * 8) + 0x2)) + (16);
    Arg2 = (*(uint64_t *)(arg1 + arg1 * 8)) + (result);
    a4 = (*(uint64_t *)(local_rdi + 0x8)) + (16);
    Arg1 = (*(uint16_t *)(*(uint64_t *)(local_rdi + 0x8) + 0x2)) + (a4);
    result = memcmp(Arg1, Arg2, (uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(arg1 + arg1 * 8) + 0x6))), a4);
    if ((uint32_t)(result) != 0) goto loc_007CA462;
loc_007CA4BB:
    local_r12 = (uint32_t)((local_r12) + (1));
    v_stack_m1A4 = (uint32_t)(local_r12);
    goto loc_007CA47B;
loc_007CA4C5:
loc_007CA4CA:
    if (((uint32_t)(local_r12)) >= v_stack_m1C0) goto loc_007CA4F9;
    result = ((uint32_t)((uint32_t)(local_r12))) + ((uint32_t)((uint32_t)(local_r12)));
    v_stack_mE8 = *(uint64_t *)(v_stack_m1B8 + result * 8 + 0x8);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m1B8 + result * 8 + 0x8) + 0x8)))) & (2)) != 0) goto loc_007CA462;
    local_r12 = (uint32_t)((local_r12) + (1));
    v_stack_m1A4 = (uint32_t)(local_r12);
    goto loc_007CA4CA;
loc_007CA4F9:
loc_007CA4FF:
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = Arg1 + 46840;
        result = ExfReleasePushLockShared(Arg1, Arg2, (uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(arg1 + arg1 * 8) + 0x6))), a4);
    }
    result = KeAbPostRelease(Arg1 + 46840, Arg2, (uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(arg1 + arg1 * 8) + 0x6))), a4);
    result = KeLeaveCriticalRegion(Arg1 + 46840, Arg2, (uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(arg1 + arg1 * 8) + 0x6))), a4);
    result = ObfReferenceObject(v_stack_m170, Arg2, (uint32_t)((uint32_t)(*(uint16_t *)(*(uint64_t *)(arg1 + arg1 * 8) + 0x6))), a4);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 46840, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 46840;
        Arg2 = result;
        Arg1 = Arg1 + 46840;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    local_r10 = 0;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    v_stack_m11C = 0;
    v_stack_mFF = 0;
    v_stack_mFB = 0;
    v_stack_mF9 = 0;
    if (v_stack_m1A0 == 0) goto loc_007CA692;
    if ((uint32_t)((uint32_t)(v_stack_m1C0)) == 0) goto loc_007CA5C4;
    if (v_stack_m1B8 == 0) goto loc_007CA696;
loc_007CA5C4:
    v_stack_m128 = 0;
    v_stack_m118 = 0;
    v_stack_m120 = 0;
    v_stack_m110 = 0;
    v_stack_m108 = 0x2A30ULL;
    v_stack_m100 = 1;
    result = ExpLicUpdateChecksum(v_stack_m1A0 + 20, Arg2, v_stack_m128, v_stack_m1B8);
    if ((uint32_t)(result) != 0) goto loc_007CA641;
    if ((uint32_t)((uint32_t)(v_stack_m1C0)) == 0) goto loc_007CA641;
    result = ((uint32_t)(v_stack_m1C0)) << (4);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) & (0xC0000095ULL));
    if (result <= ((uint32_t)(0xFFFFFFFFULL))) {
        Arg3 = v_stack_m128;
        Arg1 = v_stack_m1B8;
        result = ExpLicUpdateChecksum(Arg1, (uint32_t)(0xFFFFFFFFULL), Arg3, v_stack_m1B8);
        Arg1 = (uint32_t)(result);
    }
    if ((uint32_t)(Arg1) != 0) {
        v_stack_m128 = 0;
        v_stack_m120 = 4;
    }
    v_stack_mB0 = v_xmm0;
    v_stack_mA0 = v_xmm1;
    v_stack_m90 = v_xmm0;
    local_rdi = 0;
    if ((uint32_t)(Arg1) == 0) { local_rdi = (uint32_t)(Arg1); }
    goto loc_007CA69B;
loc_007CA692:
loc_007CA696:
loc_007CA69B:
    v_stack_m1C8 = (uint32_t)((uint32_t)(0xC000000DULL));
    if (sign_flag) goto loc_007CA7CC;
    result = sub_00966DF0(Arg1, v_stack_mB0, 7, 1);
    v_stack_m1B0 = *(uint64_t *)(arg1 + 0x10);
    v_stack_m160 = *(uint64_t *)(arg1 + 0xB6F0);
    *(uint64_t *)(arg1 + 0x10) = v_stack_m170;
    *(uint64_t *)(arg1 + 0xB6F0) = v_stack_m1A0;
    local_r13 = 0;
    v_stack_m1A0 = 0;
    result = PsGetCurrentServerSilo(Arg1, v_stack_mB0, 7, 1);
    result = PsIsHostSilo(result, v_stack_mB0, 7, 1);
    if ((uint8_t)(result) != 0) goto loc_007CA70E;
    if (*(uint64_t *)(arg1) != 0) {
        Arg2 = 0x69534C53ULL;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1), Arg2, 7, 1);
    }
    *(uint64_t *)(arg1) = 0;
    v_stack_p18 = (uint8_t)(*(uint8_t *)(arg1 + 0xB790));
    *(uint8_t *)(arg1 + 0xB790) = 0;
    Arg3 = ((uint32_t)(*(uint32_t *)(arg1 + 0xB6E8))) << (4);
    Arg2 = 0;
    result = memset(Arg1 + 24, Arg2, Arg3, 1);
    *(uint32_t *)(arg1 + 0xB6E8) = 0;
    if (v_stack_m1B8 != 0) {
        Arg3 = (uint32_t)((uint32_t)(v_stack_m1C0));
        Arg3 = (Arg3) << (4);
        Arg2 = v_stack_m1B8;
        Arg1 = Arg1 + 24;
        result = memcpy(Arg1, Arg2, Arg3, 1);
        *(uint32_t *)(arg1 + 0xB6E8) = (uint32_t)((uint32_t)(v_stack_m1C0));
    }
    *(uint8_t *)(arg1 + 0xB6EC) = 1;
    result = ExpGetLicenseTamperState(Arg1, v_stack_m194, Arg3, 1);
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0xB6F0) + 0xC))) & (1));
    result = v_stack_m1C4;
    if (condition_is_not_equal) { result = 1; }
    v_stack_m1C4 = (uint8_t)(result);
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)(Arg2)));
    result = ExpSetLicenseTamperState(Arg1, Arg2, Arg3, 1);
    result = ExpGetLicenseTamperState(Arg1, v_stack_m1A8, Arg3, 1);
    Arg2 = 0;
    if (((uint32_t)((uint32_t)(v_stack_m194))) == ((uint32_t)((uint32_t)(v_stack_m1A8)))) goto loc_007CA7C7;
    if ((uint32_t)((uint32_t)(v_stack_m194)) == 0) goto loc_007CA7C2;
    if ((uint32_t)((uint32_t)(v_stack_m1A8)) != 0) goto loc_007CA7C7;
loc_007CA7C2:
    goto loc_007CA7D4;
loc_007CA7C7:
    goto loc_007CA7D4;
loc_007CA7CC:
loc_007CA7D4:
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = Arg1 + 46840;
        result = ExfTryToWakePushLock(Arg1, Arg2, Arg3, 1);
    }
    result = KeAbPostRelease(Arg1 + 46840, Arg2, Arg3, 1);
    result = KeLeaveCriticalRegion(Arg1 + 46840, Arg2, Arg3, 1);
    local_rsi = 0;
    if (sign_flag) goto loc_007CA89A;
    if (v_stack_m190 != 0) goto loc_007CA827;
    result = sub_007C8D5C(Arg1, Arg2, Arg3, 1);
    v_stack_m1C8 = (uint32_t)(result);
    if (sign_flag) goto loc_007CA89A;
loc_007CA827:
    if (0 != 0) goto loc_007CA831;
    result = v_stack_m190;
    if (v_stack_m190 == 0) {
        Arg1 = Arg1;
        result = SLSendPolicyChangeNotifications(Arg1, Arg2, Arg3, 1);
    }
    v_stack_m1C8 = 0;
    if (v_stack_m1C3 != 1) goto loc_007CA89F;
    v_stack_m1C8 = 263;
    goto loc_007CA89F;
loc_007CA853:
    v_stack_m1C8 = 0xC000003FULL;
    local_rbx = (local_rbx) | (-1);
    goto loc_007CA09C;
loc_007CA86C:
    local_rsi = 0;
loc_007CA86E:
    local_rbx = (local_rbx) | (-1);
    goto loc_007CA89F;
loc_007CA87C:
    v_stack_m1C8 = 0xC0000040ULL;
loc_007CA884:
    local_rbx = (local_rbx) | (-1);
    goto loc_007CA89F;
loc_007CA890:
    v_stack_m1C8 = 0xC000000DULL;
    goto loc_007CA884;
loc_007CA89A:
loc_007CA89F:
    if (v_stack_p18 == 0) goto loc_007CA8BE;
    if ((*(uint8_t *)(arg1 + 0xB790)) == 0) {
        Arg1 = v_rip - 8025537;
        result = sub_007C7F80(Arg1, Arg2, Arg3, 1);
    }
    if (v_stack_m1C4 == 0) goto loc_007CA96E;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 46840, Arg2, Arg3, 1);
    result = Arg1 + 46840;
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 46840;
        Arg2 = result;
        Arg1 = Arg1 + 46840;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, 1);
        result = Arg1 + 46840;
    }
    local_rdi = Arg1 + 46840;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
        local_rdi = result;
    }
    v_stack_m68 = v_xmm0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    a4 = 0;
    result = sub_00966DF0(Arg1, v_stack_m68, a4 + 32, a4);
    result = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(result)) == 2) {
        Arg1 = local_rdi;
        result = ExfTryToWakePushLock(Arg1, v_stack_m68, a4 + 32, a4);
    }
    result = KeAbPostRelease(local_rdi, v_stack_m68, a4 + 32, a4);
    result = KeLeaveCriticalRegion(local_rdi, v_stack_m68, a4 + 32, a4);
loc_007CA96E:
    result = v_stack_m170;
    if (v_stack_m170 != 0) {
        Arg1 = v_stack_m170;
        result = ObfDereferenceObject(Arg1, v_stack_m68, a4 + 32, a4);
    }
    if (v_stack_m1B0 != 0) {
        Arg1 = v_stack_m1B0;
        result = ObfDereferenceObject(Arg1, v_stack_m68, a4 + 32, a4);
    }
    local_r12 = 0;
    if (v_stack_m1A0 != 0) {
        Arg2 = 1;
        Arg1 = v_stack_m1A0;
        result = MiRemoveFromSystemSpace(Arg1, Arg2, a4 + 32, a4);
    }
    result = v_stack_m160;
    if (v_stack_m160 != 0) {
        Arg2 = 1;
        Arg1 = v_stack_m160;
        result = MiRemoveFromSystemSpace(Arg1, Arg2, a4 + 32, a4);
    }
    if (v_stack_m1B8 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m1B8;
        result = ExFreePoolWithTag(Arg1, Arg2, a4 + 32, a4);
    }
    if (((uint32_t)((uint32_t)(v_stack_m1C8))) == 0xC000000DULL) goto loc_007CA9E8;
    result = (uint32_t)(((uint32_t)(v_stack_m1C8)) + (0x3FFFFFC1ULL));
    if (((uint32_t)(result)) > 1) goto loc_007CAA84;
loc_007CA9E8:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1 + 46840, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1 + 46840;
        Arg2 = result;
        Arg1 = Arg1 + 46840;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = ExpGetLicenseTamperState(Arg1, v_stack_m1A8, Arg3, a4);
    if (v_stack_m1A8 != 0) goto loc_007CAA52;
    result = ExpSetLicenseTamperState(Arg1, 5, Arg3, a4);
    goto loc_007CAA55;
loc_007CAA52:
loc_007CAA55:
    local_rbx = (uint8_t)((local_rbx) & (6));
    if (((uint8_t)(local_rbx)) == 2) {
        Arg1 = Arg1 + 46840;
        result = ExfTryToWakePushLock(Arg1, 5, Arg3, a4);
    }
    result = KeAbPostRelease(Arg1 + 46840, 5, Arg3, a4);
    result = KeLeaveCriticalRegion(Arg1 + 46840, 5, Arg3, a4);
    if (0 != 0) {
        Arg1 = Arg1;
        result = SLSendPolicyChangeNotifications(Arg1, 5, Arg3, a4);
    }
    local_rsp = (local_rsp) + (464);
    return (uint32_t)(v_stack_m1C8);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x0 + rcx*8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0xB6E8` | `32` | `R` |
| `Arg1` | `+ 0xB6E8` | `32` | `W` |
| `Arg1` | `+ 0xB6EC` | `8` | `W` |
| `Arg1` | `+ 0xB6F0` | `64` | `R` |
| `Arg1` | `+ 0xB6F0` | `64` | `W` |
| `Arg1` | `+ 0xB6F8` | `64` | `R` |
| `Arg1` | `+ 0xB708` | `8` | `W` |
| `Arg1` | `+ 0xB790` | `8` | `R` |
| `Arg1` | `+ 0xB790` | `8` | `W` |
| `Arg2` | `- 0x19` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007C9C04&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
