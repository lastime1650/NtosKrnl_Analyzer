# ObpLookupObjectName

- RVA: `0x0089BE90`–`0x0089DDB3` (길이 `7,971` bytes)
- VA: `0x000000014089BE90`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0007E7EC`
- 디코드: `1,848`개 명령, `7,971/7,971` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **119**; 고유 호출 대상: **58**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **19**

### Outgoing calls
- `0x0089BFFF` → [PsGetPermanentSiloContext](../../text/3E/PsGetPermanentSiloContext_function_003EE100.md) (function, `0x003EE100`)
- `0x0089C05B` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x0089C0D8` → [SeSetLearningModeObjectInformation](../../text/4C/SeSetLearningModeObjectInformation_function_004C7098.md) (function, `0x004C7098`)
- `0x0089C10A` → [PsGetPermanentSiloContext](../../text/3E/PsGetPermanentSiloContext_function_003EE100.md) (function, `0x003EE100`)
- `0x0089C186` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (function, `0x0044BEE0`)
- `0x0089C191` → [PsGetThreadServerSilo](../../text/22/PsGetThreadServerSilo_function_002247B0.md) (function, `0x002247B0`)
- `0x0089C1E8` → [PspLockThreadSecurityShared](../../text/3C/PspLockThreadSecurityShared_function_003C4720.md) (function, `0x003C4720`)
- `0x0089C21A` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0089C225` → [PspUnlockThreadSecurityShared](../../text/3C/PspUnlockThreadSecurityShared_function_003C2E40.md) (function, `0x003C2E40`)
- `0x0089C251` → [SeGetTokenDeviceMap](../96/SeGetTokenDeviceMap_function_0096CE8C.md) (function, `0x0096CE8C`)
- `0x0089C26A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0089C2CB` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x0089C2F0` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0089C311` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0089C347` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0089C34C` → [KeLeaveGuardedRegion](../../text/2E/KeLeaveGuardedRegion_function_002E2C40.md) (function, `0x002E2C40`)
- `0x0089C44E` → [ObpTraceObjectReferenceIfActive](../../text/21/ObpTraceObjectReferenceIfActive_function_00210780.md) (function, `0x00210780`)
- `0x0089C4F8` → [ObpParseSymbolicLinkEx](../8B/ObpParseSymbolicLinkEx_function_008B35C0.md) (function, `0x008B35C0`)
- `0x0089C523` → [RtlGetNtSystemRoot](../A1/RtlGetNtSystemRoot_function_00A1DCD0.md) (function, `0x00A1DCD0`)
- `0x0089C52B` → [RtlUpcaseUnicodeChar](../85/RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0089C53B` → [RtlUpcaseUnicodeChar](../85/RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0089C663` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x0089C6A7` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0089C6BD` → [ObDereferenceObjectDeferDeleteWithTag](../../text/26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)
- `0x0089C6DB` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0089C75E` → [CmpParseKey](CmpParseKey_function_0089DDC0.md) (function, `0x0089DDC0`)
- `0x0089C76A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0089C78B` → [ObDereferenceObjectDeferDelete](../../text/3F/ObDereferenceObjectDeferDelete_function_003FCE40.md) (function, `0x003FCE40`)
- `0x0089C86E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0089C884` → [ObDereferenceObjectDeferDeleteWithTag](../../text/26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)
- `0x0089C8A2` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)
- `0x0089C9C0` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0089C9EB` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0089CA58` → [IopParseDevice](IopParseDevice_function_0089E510.md) (function, `0x0089E510`)
- `0x0089CAA2` → [ObpFastReplenishReference](../../text/42/ObpFastReplenishReference_function_00428130.md) (function, `0x00428130`)
- `0x0089CB10` → [ObpParseSymbolicLinkEx](../8B/ObpParseSymbolicLinkEx_function_008B35C0.md) (function, `0x008B35C0`)
- `0x0089CB20` → [IopParseDevice](IopParseDevice_function_0089E510.md) (function, `0x0089E510`)
- `0x0089CB63` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (function, `0x002109E4`)
- `0x0089CC46` → [PsGetPermanentSiloContext](../../text/3E/PsGetPermanentSiloContext_function_003EE100.md) (function, `0x003EE100`)
- `0x0089CC6A` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0089CC86` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0089CC9B` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (function, `0x00263D30`)
- `0x0089CCB6` → [ObDereferenceObjectDeferDelete](../../text/3F/ObDereferenceObjectDeferDelete_function_003FCE40.md) (function, `0x003FCE40`)
- `0x0089CCBB` → [SeClearLearningModeObjectInformation](../../text/40/SeClearLearningModeObjectInformation_function_0040D470.md) (function, `0x0040D470`)
- `0x0089CD42` → [OBP_GET_SILO_ROOT_DIRECTORY_FROM_SILO](../../text/40/OBP_GET_SILO_ROOT_DIRECTORY_FROM_SILO_function_00409500.md) (function, `0x00409500`)
- `0x0089CD6A` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x0089CD97` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0089CDAD` → [ObDereferenceObjectDeferDeleteWithTag](../../text/26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)
- `0x0089CEFD` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0089CF2A` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0089CF62` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x0089CFA1` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x0089D137` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0089D17B` → [ObDereferenceDeviceMap](../96/ObDereferenceDeviceMap_function_0096D0E8.md) (function, `0x0096D0E8`)
- `0x0089D188` → [RtlUpcaseUnicodeChar](../85/RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0089D1EB` → [IopParseFile](../9F/IopParseFile_function_009FDB60.md) (function, `0x009FDB60`)
- `0x0089D229` → [ObpCheckTraverseAccess](../8C/ObpCheckTraverseAccess_function_008C6CE4.md) (function, `0x008C6CE4`)
- `0x0089D278` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0089D2A0` → [RtlUpcaseUnicodeChar](../85/RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x0089D2EE` → [ObpReferenceCurrentDeviceMap](../96/ObpReferenceCurrentDeviceMap_function_0096CBD0.md) (function, `0x0096CBD0`)
- `0x0089D320` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (function, `0x00438D00`)
- `0x0089D393` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (function, `0x00438D00`)
- `0x0089D452` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0089D498` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0089D4FC` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x0089D51E` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0089D53F` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0089D572` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0089D57A` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0089D57F` → [KeLeaveGuardedRegion](../../text/2E/KeLeaveGuardedRegion_function_002E2C40.md) (function, `0x002E2C40`)
- `0x0089D5A0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0089D5A8` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (function, `0x002250A0`)
- `0x0089D5BA` → [ObDereferenceDeviceMap](../96/ObDereferenceDeviceMap_function_0096D0E8.md) (function, `0x0096D0E8`)
- `0x0089D5CA` → [ObpLockDirectoryExclusive](../99/ObpLockDirectoryExclusive_function_0099F24C.md) (function, `0x0099F24C`)
- `0x0089D60A` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (function, `0x00438D00`)
- `0x0089D61C` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0089D638` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (function, `0x002250A0`)
- `0x0089D65D` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0089D67E` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0089D694` → [ObFastReferenceObjectLocked](../../text/38/ObFastReferenceObjectLocked_function_00381DA0.md) (function, `0x00381DA0`)
- `0x0089D6B1` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0089D6B6` → [KeLeaveGuardedRegion](../../text/2E/KeLeaveGuardedRegion_function_002E2C40.md) (function, `0x002E2C40`)
- `0x0089D6F5` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0089D753` → [ExpWin32ParseProcedure](../90/ExpWin32ParseProcedure_function_00905400.md) (function, `0x00905400`)
- `0x0089D7A1` → [ObpSetCurrentProcessDeviceMap](../96/ObpSetCurrentProcessDeviceMap_function_0096CF6C.md) (function, `0x0096CF6C`)
- `0x0089D7BA` → [ObDereferenceDeviceMap](../96/ObDereferenceDeviceMap_function_0096D0E8.md) (function, `0x0096D0E8`)
- `0x0089D7C7` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0089D816` → [ObCheckCreateObjectAccess](../8C/ObCheckCreateObjectAccess_function_008C6340.md) (function, `0x008C6340`)
- `0x0089D843` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x0089D85D` → [ObpInsertDirectoryEntry](../A1/ObpInsertDirectoryEntry_function_00A18AC0.md) (function, `0x00A18AC0`)
- `0x0089D874` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0089D8A2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0089D8F6` → [PsGetCurrentProcessSessionId](../../text/23/PsGetCurrentProcessSessionId_function_002303D0.md) (function, `0x002303D0`)
- `0x0089D90E` → [SeSinglePrivilegeCheck](../87/SeSinglePrivilegeCheck_function_00871E20.md) (function, `0x00871E20`)
- `0x0089D92B` → [ObpIsUnsecureName](../A7/ObpIsUnsecureName_function_00A714C0.md) (function, `0x00A714C0`)
- `0x0089D947` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x0089D981` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (function, `0x002FE1F0`)
- `0x0089D9C3` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (function, `0x006BA670`)
- `0x0089DAD5` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x0089DAEE` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0089DB00` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)
- `0x0089DB1F` → [ExfTryAcquirePushLockSharedEx](../../text/3F/ExfTryAcquirePushLockSharedEx_function_003FC210.md) (function, `0x003FC210`)
- `0x0089DB3E` → [ObDereferenceObjectDeferDelete](../../text/3F/ObDereferenceObjectDeferDelete_function_003FCE40.md) (function, `0x003FCE40`)
- `0x0089DB72` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (function, `0x00438D00`)
- `0x0089DB9F` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (function, `0x00210710`)
- `0x0089DBC1` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0089DBCD` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x0089DBDE` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0089DC0B` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0089DC3E` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (function, `0x00438D00`)
- `0x0089DC62` → [ObDereferenceDeviceMap](../96/ObDereferenceDeviceMap_function_0096D0E8.md) (function, `0x0096D0E8`)
- `0x0089DC8F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x0089DCA1` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (function, `0x00263440`)
- `0x0089DCB5` → [KeAbPostReleaseEx](../../text/26/KeAbPostReleaseEx_function_00262210.md) (function, `0x00262210`)
- `0x0089DCCC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0089DCF7` → [SeSetLearningModeObjectInformation](../../text/4C/SeSetLearningModeObjectInformation_function_004C7098.md) (function, `0x004C7098`)
- `0x0089DD49` → [RtlIsSandboxedToken](../8B/RtlIsSandboxedToken_function_008B3AB0.md) (function, `0x008B3AB0`)
- `0x0089DD77` → [ObDereferenceObjectDeferDeleteWithTag](../../text/26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (function, `0x00263EA0`)
- `0x0089DD8E` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [sub_0089A903](Unknown_function_0089A903.md) at `0x0089AABF`
- [ObReferenceObjectByNameEx](../8B/ObReferenceObjectByNameEx_function_008BD524.md) at `0x008BD6BA`
- [ObReferenceObjectByName](../8C/ObReferenceObjectByName_function_008C4A00.md) at `0x008C4B83`
- [ObpInsertOrLocateNamedObject](../99/ObpInsertOrLocateNamedObject_function_0099F2C0.md) at `0x0099F3D7`

### Static image references
- `0x0089BF23` → RVA `0x00E0B378` (`.data`; read)
- `0x0089BFE8` → RVA `0x00FC5068` (`ALMOSTRO`; read)
- `0x0089C00C` → RVA `0x00F0F668` (`.data`; read)
- `0x0089C093` → RVA `0x00FD9AD8` (`PAGEDATA`; read)
- `0x0089C15E` → RVA `0x00FC6AE0` (`ALMOSTRO`; read)
- `0x0089C47A` → RVA `0x00FC6EE0` (`ALMOSTRO`; read)
- `0x0089C4A4` → RVA `0x00FC6E4C` (`ALMOSTRO`; read)
- `0x0089C543` → RVA `0x00E0B37C` (`.data`; read)
- `0x0089C5E2` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x0089C5EE` → RVA `0x008B35C0` (`ObpParseSymbolicLinkEx`; read)
- `0x0089C701` → RVA `0x0089DDC0` (`CmpParseKey`; read)
- `0x0089C8F1` → RVA `0x00F0F650` (`.data`; read)
- `0x0089CA05` → RVA `0x0089E510` (`IopParseDevice`; read)
- `0x0089CB4A` → RVA `0x00FC5010` (`ALMOSTRO`; read)
- `0x0089D198` → RVA `0x009FDB60` (`IopParseFile`; read)
- `0x0089D706` → RVA `0x00905400` (`ExpWin32ParseProcedure`; read)
- `0x0089D8E0` → RVA `0x00FC6BD8` (`ALMOSTRO`; read)
- `0x0089D8E9` → RVA `0x00F0F658` (`.data`; read)
- `0x0089D903` → RVA `0x00FD9C98` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **92**
  - `0x0089BFFF` → [PsGetPermanentSiloContext](../../text/3E/PsGetPermanentSiloContext_function_003EE100.md) (`PAGE` → `.text`)
  - `0x0089C0D8` → [SeSetLearningModeObjectInformation](../../text/4C/SeSetLearningModeObjectInformation_function_004C7098.md) (`PAGE` → `.text`)
  - `0x0089C10A` → [PsGetPermanentSiloContext](../../text/3E/PsGetPermanentSiloContext_function_003EE100.md) (`PAGE` → `.text`)
  - `0x0089C186` → [PsGetProcessServerSilo](../../text/44/PsGetProcessServerSilo_function_0044BEE0.md) (`PAGE` → `.text`)
  - `0x0089C191` → [PsGetThreadServerSilo](../../text/22/PsGetThreadServerSilo_function_002247B0.md) (`PAGE` → `.text`)
  - `0x0089C1E8` → [PspLockThreadSecurityShared](../../text/3C/PspLockThreadSecurityShared_function_003C4720.md) (`PAGE` → `.text`)
  - `0x0089C21A` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x0089C225` → [PspUnlockThreadSecurityShared](../../text/3C/PspUnlockThreadSecurityShared_function_003C2E40.md) (`PAGE` → `.text`)
  - `0x0089C26A` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0089C2CB` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x0089C2F0` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0089C311` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0089C347` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0089C34C` → [KeLeaveGuardedRegion](../../text/2E/KeLeaveGuardedRegion_function_002E2C40.md) (`PAGE` → `.text`)
  - `0x0089C44E` → [ObpTraceObjectReferenceIfActive](../../text/21/ObpTraceObjectReferenceIfActive_function_00210780.md) (`PAGE` → `.text`)
  - `0x0089C663` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x0089C6A7` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0089C6BD` → [ObDereferenceObjectDeferDeleteWithTag](../../text/26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (`PAGE` → `.text`)
  - `0x0089C6DB` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0089C76A` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0089C78B` → [ObDereferenceObjectDeferDelete](../../text/3F/ObDereferenceObjectDeferDelete_function_003FCE40.md) (`PAGE` → `.text`)
  - `0x0089C86E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0089C884` → [ObDereferenceObjectDeferDeleteWithTag](../../text/26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (`PAGE` → `.text`)
  - `0x0089C8A2` → [KeLeaveCriticalRegionThread](../../text/25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (`PAGE` → `.text`)
  - `0x0089C9C0` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0089C9EB` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0089CAA2` → [ObpFastReplenishReference](../../text/42/ObpFastReplenishReference_function_00428130.md) (`PAGE` → `.text`)
  - `0x0089CB63` → [ObpPushStackInfo](../../text/21/ObpPushStackInfo_function_002109E4.md) (`PAGE` → `.text`)
  - `0x0089CC46` → [PsGetPermanentSiloContext](../../text/3E/PsGetPermanentSiloContext_function_003EE100.md) (`PAGE` → `.text`)
  - `0x0089CC6A` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x0089CC86` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x0089CC9B` → [ObpReleaseLookupContext](../../text/26/ObpReleaseLookupContext_function_00263D30.md) (`PAGE` → `.text`)
  - `0x0089CCB6` → [ObDereferenceObjectDeferDelete](../../text/3F/ObDereferenceObjectDeferDelete_function_003FCE40.md) (`PAGE` → `.text`)
  - `0x0089CCBB` → [SeClearLearningModeObjectInformation](../../text/40/SeClearLearningModeObjectInformation_function_0040D470.md) (`PAGE` → `.text`)
  - `0x0089CD42` → [OBP_GET_SILO_ROOT_DIRECTORY_FROM_SILO](../../text/40/OBP_GET_SILO_ROOT_DIRECTORY_FROM_SILO_function_00409500.md) (`PAGE` → `.text`)
  - `0x0089CD6A` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x0089CD97` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0089CDAD` → [ObDereferenceObjectDeferDeleteWithTag](../../text/26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (`PAGE` → `.text`)
  - `0x0089CEFD` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0089CF2A` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0089CF62` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x0089CFA1` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (`PAGE` → `.text`)
  - `0x0089D137` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0089D278` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0089D320` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (`PAGE` → `.text`)
  - `0x0089D393` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (`PAGE` → `.text`)
  - `0x0089D452` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0089D498` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0089D4FC` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x0089D51E` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0089D53F` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0089D572` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0089D57A` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0089D57F` → [KeLeaveGuardedRegion](../../text/2E/KeLeaveGuardedRegion_function_002E2C40.md) (`PAGE` → `.text`)
  - `0x0089D5A0` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0089D5A8` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (`PAGE` → `.text`)
  - `0x0089D60A` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (`PAGE` → `.text`)
  - `0x0089D61C` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0089D638` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (`PAGE` → `.text`)
  - `0x0089D65D` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0089D67E` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0089D694` → [ObFastReferenceObjectLocked](../../text/38/ObFastReferenceObjectLocked_function_00381DA0.md) (`PAGE` → `.text`)
  - `0x0089D6B1` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0089D6B6` → [KeLeaveGuardedRegion](../../text/2E/KeLeaveGuardedRegion_function_002E2C40.md) (`PAGE` → `.text`)
  - `0x0089D6F5` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0089D7C7` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0089D843` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x0089D874` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0089D8A2` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0089D8F6` → [PsGetCurrentProcessSessionId](../../text/23/PsGetCurrentProcessSessionId_function_002303D0.md) (`PAGE` → `.text`)
  - `0x0089D947` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x0089D981` → [PsGetCurrentServerSiloGlobals](../../text/2F/PsGetCurrentServerSiloGlobals_function_002FE1F0.md) (`PAGE` → `.text`)
  - `0x0089D9C3` → [RtlCompareMemory](../../text/6B/RtlCompareMemory_function_006BA670.md) (`PAGE` → `.text`)
  - `0x0089DAD5` → [memcmp](../../text/6C/memcmp_function_006C6B10.md) (`PAGE` → `.text`)
  - `0x0089DAEE` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0089DB00` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
  - `0x0089DB1F` → [ExfTryAcquirePushLockSharedEx](../../text/3F/ExfTryAcquirePushLockSharedEx_function_003FC210.md) (`PAGE` → `.text`)
  - `0x0089DB3E` → [ObDereferenceObjectDeferDelete](../../text/3F/ObDereferenceObjectDeferDelete_function_003FCE40.md) (`PAGE` → `.text`)
  - `0x0089DB72` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (`PAGE` → `.text`)
  - `0x0089DB9F` → [ObfReferenceObjectWithTag](../../text/21/ObfReferenceObjectWithTag_function_00210710.md) (`PAGE` → `.text`)
  - `0x0089DBC1` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0089DBCD` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0089DBDE` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0089DC0B` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0089DC3E` → [ObReferenceObjectByPointer](../../text/43/ObReferenceObjectByPointer_function_00438D00.md) (`PAGE` → `.text`)
  - `0x0089DC8F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x0089DCA1` → [ExfReleasePushLockShared](../../text/26/ExfReleasePushLockShared_function_00263440.md) (`PAGE` → `.text`)
  - `0x0089DCB5` → [KeAbPostReleaseEx](../../text/26/KeAbPostReleaseEx_function_00262210.md) (`PAGE` → `.text`)
  - `0x0089DCCC` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
  - `0x0089DCF7` → [SeSetLearningModeObjectInformation](../../text/4C/SeSetLearningModeObjectInformation_function_004C7098.md) (`PAGE` → `.text`)
  - `0x0089DD77` → [ObDereferenceObjectDeferDeleteWithTag](../../text/26/ObDereferenceObjectDeferDeleteWithTag_function_00263EA0.md) (`PAGE` → `.text`)
  - `0x0089DD8E` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0089DD50` → [sub_00B19BD0](../B1/Unknown_function_00B19BD0.md) (`tail-transfer`)
  - `0x0089DD5A` → [sub_00B19BD0 + 0x4](../B1/Unknown_function_00B19BD0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0089BE90  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0089BE95  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
0089BE9A  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
0089BE9F  55                              push rbp
0089BEA0  53                              push rbx
0089BEA1  56                              push rsi
0089BEA2  57                              push rdi
0089BEA3  41 54                           push r12
0089BEA5  41 55                           push r13
0089BEA7  41 56                           push r14
0089BEA9  41 57                           push r15
0089BEAB  48 8D 6C 24 98                  lea rbp, [rsp - 0x68]
0089BEB0  48 81 EC 68 01 00 00            sub rsp, 0x168
0089BEB7  4C 8B A5 00 01 00 00            mov r12, qword ptr [rbp + 0x100]
0089BEBE  45 33 FF                        xor r15d, r15d
0089BEC1  33 C0                           xor eax, eax
0089BEC3  4C 89 7D F0                     mov qword ptr [rbp - 0x10], r15
0089BEC7  0F 57 C0                        xorps xmm0, xmm0
0089BECA  48 89 45 58                     mov qword ptr [rbp + 0x58], rax
0089BECE  0F 57 C9                        xorps xmm1, xmm1
0089BED1  66 44 89 7D C2                  mov word ptr [rbp - 0x3e], r15w
0089BED6  41 0F 11 0C 24                  movups xmmword ptr [r12], xmm1
0089BEDB  49 89 44 24 10                  mov qword ptr [r12 + 0x10], rax
0089BEE0  48 8B F2                        mov rsi, rdx
0089BEE3  48 8B 85 08 01 00 00            mov rax, qword ptr [rbp + 0x108]
0089BEEA  45 8B F0                        mov r14d, r8d
0089BEED  0F B6 95 D0 00 00 00            movzx edx, byte ptr [rbp + 0xd0]
0089BEF4  48 8B D9                        mov rbx, rcx
0089BEF7  4C 89 7D 10                     mov qword ptr [rbp + 0x10], r15
0089BEFB  4C 89 7D 98                     mov qword ptr [rbp - 0x68], r15
0089BEFF  4C 89 7D A0                     mov qword ptr [rbp - 0x60], r15
0089BF03  C7 45 A8 40 00 00 00            mov dword ptr [rbp - 0x58], 0x40
0089BF0A  0F 11 45 28                     movups xmmword ptr [rbp + 0x28], xmm0
0089BF0E  0F 11 45 38                     movups xmmword ptr [rbp + 0x38], xmm0
0089BF12  0F 11 45 48                     movups xmmword ptr [rbp + 0x48], xmm0
0089BF16  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
0089BF1B  48 85 C0                        test rax, rax
0089BF1E  74 03                           je 0x14089bf23
0089BF20  44 89 38                        mov dword ptr [rax], r15d
0089BF23  44 39 3D 4E F4 56 00            cmp dword ptr [rip + 0x56f44e], r15d
0089BF2A  49 8B FF                        mov rdi, r15
0089BF2D  48 8B 85 10 01 00 00            mov rax, qword ptr [rbp + 0x110]
0089BF34  4C 8B 95 F0 00 00 00            mov r10, qword ptr [rbp + 0xf0]
0089BF3B  44 89 7C 24 60                  mov dword ptr [rsp + 0x60], r15d
0089BF40  44 89 7D AC                     mov dword ptr [rbp - 0x54], r15d
0089BF44  4C 89 38                        mov qword ptr [rax], r15
0089BF47  B8 10 00 00 00                  mov eax, 0x10
0089BF4C  66 89 45 C0                     mov word ptr [rbp - 0x40], ax
0089BF50  C6 85 B0 00 00 00 01            mov byte ptr [rbp + 0xb0], 1
0089BF57  4C 89 7D 90                     mov qword ptr [rbp - 0x70], r15
0089BF5B  4C 89 7D 80                     mov qword ptr [rbp - 0x80], r15
0089BF5F  C7 45 C4 FF FF FF FF            mov dword ptr [rbp - 0x3c], 0xffffffff
0089BF66  4C 89 55 C8                     mov qword ptr [rbp - 0x38], r10
0089BF6A  74 27                           je 0x14089bf93
0089BF6C  41 F6 41 42 01                  test byte ptr [r9 + 0x42], 1
0089BF71  74 20                           je 0x14089bf93
0089BF73  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0089BF7C  8B 80 A0 05 00 00               mov eax, dword ptr [rax + 0x5a0]
0089BF82  0F BA E0 13                     bt eax, 0x13
0089BF86  72 0B                           jb 0x14089bf93
0089BF88  41 83 CE 40                     or r14d, 0x40
0089BF8C  44 89 B5 C0 00 00 00            mov dword ptr [rbp + 0xc0], r14d
0089BF93  4C 8B AD E8 00 00 00            mov r13, qword ptr [rbp + 0xe8]
0089BF9A  41 0F BA E6 0A                  bt r14d, 0xa
0089BF9F  B9 01 00 00 00                  mov ecx, 1
0089BFA4  41 8B C6                        mov eax, r14d
0089BFA7  0F 43 CA                        cmovae ecx, edx
0089BFAA  83 E0 40                        and eax, 0x40
0089BFAD  89 4C 24 64                     mov dword ptr [rsp + 0x64], ecx
0089BFB1  8B C8                           mov ecx, eax
0089BFB3  83 C9 01                        or ecx, 1
0089BFB6  4D 85 ED                        test r13, r13
0089BFB9  0F 45 C8                        cmovne ecx, eax
0089BFBC  89 4D 88                        mov dword ptr [rbp - 0x78], ecx
0089BFBF  48 85 DB                        test rbx, rbx
0089BFC2  75 6C                           jne 0x14089c030
0089BFC4  0F B7 16                        movzx edx, word ptr [rsi]
0089BFC7  66 85 D2                        test dx, dx
0089BFCA  0F 84 6C 11 00 00               je 0x14089d13c
0089BFD0  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0089BFD4  66 83 38 5C                     cmp word ptr [rax], 0x5c
0089BFD8  0F 85 5E 11 00 00               jne 0x14089d13c
0089BFDE  66 83 FA 02                     cmp dx, 2
0089BFE2  0F 85 D3 00 00 00               jne 0x14089c0bb
0089BFE8  8B 15 7A 90 72 00               mov edx, dword ptr [rip + 0x72907a]
0089BFEE  4C 8D 85 E8 00 00 00            lea r8, [rbp + 0xe8]
0089BFF5  49 8B CA                        mov rcx, r10
0089BFF8  4C 89 BD E8 00 00 00            mov qword ptr [rbp + 0xe8], r15
0089BFFF  E8 FC 20 B5 FF                  call 0x1403ee100
0089C004  85 C0                           test eax, eax
0089C006  0F 89 FE 1A 00 00               jns 0x14089db0a
0089C00C  48 8B 1D 55 36 67 00            mov rbx, qword ptr [rip + 0x673655]
0089C013  48 85 DB                        test rbx, rbx
0089C016  0F 85 42 1B 00 00               jne 0x14089db5e
0089C01C  4D 85 ED                        test r13, r13
0089C01F  0F 85 05 1C 00 00               jne 0x14089dc2a
0089C025  B8 0D 00 00 C0                  mov eax, 0xc000000d
0089C02A  E9 70 1D 00 00                  jmp 0x14089dd9f
0089C02F  CC                              int3
0089C030  48 8D 45 10                     lea rax, [rbp + 0x10]
0089C034  44 0F B6 CA                     movzx r9d, dl
0089C038  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0089C03D  45 33 C0                        xor r8d, r8d
0089C040  48 8D 45 F0                     lea rax, [rbp - 0x10]
0089C044  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0089C049  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0089C04E  33 D2                           xor edx, edx
0089C050  48 8B CB                        mov rcx, rbx
0089C053  C7 44 24 20 44 66 6C 74         mov dword ptr [rsp + 0x20], 0x746c6644
0089C05B  E8 F0 D5 FC FF                  call 0x140869650
0089C060  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
0089C064  85 C0                           test eax, eax
0089C066  0F 88 33 1D 00 00               js 0x14089dd9f
0089C06C  8B 45 14                        mov eax, dword ptr [rbp + 0x14]
0089C06F  85 C0                           test eax, eax
0089C071  0F 85 F5 1B 00 00               jne 0x14089dc6c
0089C077  4C 8B 6D F0                     mov r13, qword ptr [rbp - 0x10]
0089C07B  66 44 39 3E                     cmp word ptr [rsi], r15w
0089C07F  0F 84 4F 15 00 00               je 0x14089d5d4
0089C085  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0089C089  66 83 38 5C                     cmp word ptr [rax], 0x5c
0089C08D  0F 84 7F 10 00 00               je 0x14089d112
0089C093  44 39 3D 3E DA 73 00            cmp dword ptr [rip + 0x73da3e], r15d
0089C09A  0F 10 0E                        movups xmm1, xmmword ptr [rsi]
0089C09D  0F 29 4C 24 70                  movaps xmmword ptr [rsp + 0x70], xmm1
0089C0A2  0F 85 34 1C 00 00               jne 0x14089dcdc
0089C0A8  66 0F 6F C1                     movdqa xmm0, xmm1
0089C0AC  66 0F 73 D8 08                  psrldq xmm0, 8
0089C0B1  66 49 0F 7E C0                  movq r8, xmm0
0089C0B6  E9 18 08 00 00                  jmp 0x14089c8d3
0089C0BB  44 39 3D 16 DA 73 00            cmp dword ptr [rip + 0x73da16], r15d
0089C0C2  74 70                           je 0x14089c134
0089C0C4  49 8D 41 10                     lea rax, [r9 + 0x10]
0089C0C8  48 89 75 40                     mov qword ptr [rbp + 0x40], rsi
0089C0CC  48 8D 4D 28                     lea rcx, [rbp + 0x28]
0089C0D0  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
0089C0D4  4C 89 7D 48                     mov qword ptr [rbp + 0x48], r15
0089C0D8  E8 BB AF C2 FF                  call 0x1404c7098
0089C0DD  EB 4E                           jmp 0x14089c12d
0089C0DF  66 83 F9 5C                     cmp cx, 0x5c
0089C0E3  0F 85 A7 0B 00 00               jne 0x14089cc90
0089C0E9  81 FA 68 03 00 00               cmp edx, 0x368
0089C0EF  0F 84 6C 11 00 00               je 0x14089d261
0089C0F5  8B 15 6D 8F 72 00               mov edx, dword ptr [rip + 0x728f6d]
0089C0FB  4C 8D 45 08                     lea r8, [rbp + 8]
0089C0FF  48 8B 8D F0 00 00 00            mov rcx, qword ptr [rbp + 0xf0]
0089C106  4C 89 7D 08                     mov qword ptr [rbp + 8], r15
0089C10A  E8 F1 1F B5 FF                  call 0x1403ee100
0089C10F  85 C0                           test eax, eax
0089C111  0F 89 1B 1A 00 00               jns 0x14089db32
0089C117  48 8B 05 4A 35 67 00            mov rax, qword ptr [rip + 0x67354a]
0089C11E  48 89 45 08                     mov qword ptr [rbp + 8], rax
0089C122  44 8B B5 C0 00 00 00            mov r14d, dword ptr [rbp + 0xc0]
0089C129  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0089C12D  4C 8B 8D C8 00 00 00            mov r9, qword ptr [rbp + 0xc8]
0089C134  41 BA 3F 00 00 00               mov r10d, 0x3f
0089C13A  49 B8 5C 00 3F 00 3F 00 5C 00   movabs r8, 0x5c003f003f005c
0089C144  0F B7 16                        movzx edx, word ptr [rsi]
0089C147  66 83 FA 08                     cmp dx, 8
0089C14B  0F 82 D9 0B 00 00               jb 0x14089cd2a
0089C151  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0089C155  4C 39 00                        cmp qword ptr [rax], r8
0089C158  0F 85 CC 0B 00 00               jne 0x14089cd2a
0089C15E  4C 3B 0D 7B A9 72 00            cmp r9, qword ptr [rip + 0x72a97b]
0089C165  0F 84 97 03 00 00               je 0x14089c502
0089C16B  65 48 8B 3C 25 88 01 00 00      mov rdi, qword ptr gs:[0x188]
0089C174  4C 89 7D 98                     mov qword ptr [rbp - 0x68], r15
0089C178  4C 89 7D A0                     mov qword ptr [rbp - 0x60], r15
0089C17C  48 8B 9F 20 02 00 00            mov rbx, qword ptr [rdi + 0x220]
0089C183  48 8B CB                        mov rcx, rbx
0089C186  E8 55 FD BA FF                  call 0x14044bee0
0089C18B  48 8B CF                        mov rcx, rdi
0089C18E  48 8B F0                        mov rsi, rax
0089C191  E8 1A 86 98 FF                  call 0x1402247b0
0089C196  48 3B F0                        cmp rsi, rax
0089C199  4C 8B E8                        mov r13, rax
0089C19C  8B 87 A0 05 00 00               mov eax, dword ptr [rdi + 0x5a0]
0089C1A2  41 0F 95 C6                     setne r14b
0089C1A6  A8 08                           test al, 8
0089C1A8  45 0F B6 FE                     movzx r15d, r14b
0089C1AC  0F 95 C1                        setne cl
0089C1AF  0F BA A5 C0 00 00 00 0B         bt dword ptr [rbp + 0xc0], 0xb
0089C1B7  0F 93 C0                        setae al
0089C1BA  84 C8                           test al, cl
0089C1BC  0F 84 BA 00 00 00               je 0x14089c27c
0089C1C2  49 3B F5                        cmp rsi, r13
0089C1C5  0F 85 B1 00 00 00               jne 0x14089c27c
0089C1CB  8B 87 A0 05 00 00               mov eax, dword ptr [rdi + 0x5a0]
0089C1D1  A8 08                           test al, 8
0089C1D3  0F 84 A3 00 00 00               je 0x14089c27c
0089C1D9  65 4C 8B 3C 25 88 01 00 00      mov r15, qword ptr gs:[0x188]
0089C1E2  48 8B CF                        mov rcx, rdi
0089C1E5  49 8B D7                        mov rdx, r15
0089C1E8  E8 33 85 B2 FF                  call 0x1403c4720
0089C1ED  8B 87 A0 05 00 00               mov eax, dword ptr [rdi + 0x5a0]
0089C1F3  A8 08                           test al, 8
0089C1F5  0F 84 5E 17 00 00               je 0x14089d959
0089C1FB  48 8B B7 48 06 00 00            mov rsi, qword ptr [rdi + 0x648]
0089C202  48 85 F6                        test rsi, rsi
0089C205  75 0B                           jne 0x14089c212
0089C207  48 8B B7 38 05 00 00            mov rsi, qword ptr [rdi + 0x538]
0089C20E  48 83 E6 F8                     and rsi, 0xfffffffffffffff8
0089C212  BA 44 66 6C 74                  mov edx, 0x746c6644
0089C217  48 8B CE                        mov rcx, rsi
0089C21A  E8 F1 44 97 FF                  call 0x140210710
0089C21F  49 8B D7                        mov rdx, r15
0089C222  48 8B CF                        mov rcx, rdi
0089C225  E8 16 6C B2 FF                  call 0x1403c2e40
0089C22A  45 0F B6 FE                     movzx r15d, r14b
0089C22E  48 85 F6                        test rsi, rsi
0089C231  74 49                           je 0x14089c27c
0089C233  48 8B 46 18                     mov rax, qword ptr [rsi + 0x18]
0089C237  3D E7 03 00 00                  cmp eax, 0x3e7
0089C23C  0F 84 47 13 00 00               je 0x14089d589
0089C242  48 8D 55 18                     lea rdx, [rbp + 0x18]
0089C246  48 C7 45 18 00 00 00 00         mov qword ptr [rbp + 0x18], 0
0089C24E  48 8B CE                        mov rcx, rsi
0089C251  E8 36 0C 0D 00                  call 0x14096ce8c
0089C256  85 C0                           test eax, eax
0089C258  78 08                           js 0x14089c262
0089C25A  4C 8B 45 18                     mov r8, qword ptr [rbp + 0x18]
0089C25E  4C 89 45 98                     mov qword ptr [rbp - 0x68], r8
0089C262  BA 44 66 6C 74                  mov edx, 0x746c6644
0089C267  48 8B CE                        mov rcx, rsi
0089C26A  E8 71 B6 A5 FF                  call 0x1402f78e0
0089C26F  4C 8B 75 98                     mov r14, qword ptr [rbp - 0x68]
0089C273  4D 85 F6                        test r14, r14
0089C276  0F 85 DE 00 00 00               jne 0x14089c35a
0089C27C  45 84 FF                        test r15b, r15b
0089C27F  0F 85 20 13 00 00               jne 0x14089d5a5
0089C285  48 8D 83 18 03 00 00            lea rax, [rbx + 0x318]
0089C28C  48 8B C8                        mov rcx, rax
0089C28F  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
0089C293  0F 0D 08                        prefetchw byte ptr [rax]
0089C296  48 8B 10                        mov rdx, qword ptr [rax]
0089C299  F6 C2 0F                        test dl, 0xf
0089C29C  74 19                           je 0x14089c2b7
0089C29E  4C 8B 45 A0                     mov r8, qword ptr [rbp - 0x60]
0089C2A2  48 8D 4A FF                     lea rcx, [rdx - 1]
0089C2A6  48 8B C2                        mov rax, rdx
0089C2A9  F0 49 0F B1 08                  lock cmpxchg qword ptr [r8], rcx
0089C2AE  74 07                           je 0x14089c2b7
0089C2B0  48 8B D0                        mov rdx, rax
0089C2B3  A8 0F                           test al, 0xf
0089C2B5  75 E7                           jne 0x14089c29e
0089C2B7  4C 8B F2                        mov r14, rdx
0089C2BA  49 83 E6 F0                     and r14, 0xfffffffffffffff0
0089C2BE  4C 89 75 98                     mov qword ptr [rbp - 0x68], r14
0089C2C2  F6 C2 0F                        test dl, 0xf
0089C2C5  0F 85 86 00 00 00               jne 0x14089c351
0089C2CB  E8 20 1F A6 FF                  call 0x1402fe1f0
0089C2D0  48 8B F8                        mov rdi, rax
0089C2D3  45 33 C0                        xor r8d, r8d
0089C2D6  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0089C2DF  48 83 C7 78                     add rdi, 0x78
0089C2E3  33 D2                           xor edx, edx
0089C2E5  48 8B CF                        mov rcx, rdi
0089C2E8  66 FF 88 E6 01 00 00            dec word ptr [rax + 0x1e6]
0089C2EF  90                              nop
0089C2F0  E8 3B 3F 97 FF                  call 0x140210230
0089C2F5  48 8B D8                        mov rbx, rax
0089C2F8  BE 11 00 00 00                  mov esi, 0x11
0089C2FD  33 C0                           xor eax, eax
0089C2FF  F0 48 0F B1 37                  lock cmpxchg qword ptr [rdi], rsi
0089C304  74 10                           je 0x14089c316
0089C306  4C 8B CF                        mov r9, rdi
0089C309  4C 8B C3                        mov r8, rbx
0089C30C  33 D2                           xor edx, edx
0089C30E  48 8B CF                        mov rcx, rdi
0089C311  E8 36 41 97 FF                  call 0x14021044c
0089C316  48 85 DB                        test rbx, rbx
0089C319  74 04                           je 0x14089c31f
0089C31B  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
0089C31F  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
0089C323  4C 8B 30                        mov r14, qword ptr [rax]
0089C326  49 83 E6 F0                     and r14, 0xfffffffffffffff0
0089C32A  4C 89 75 98                     mov qword ptr [rbp - 0x68], r14
0089C32E  0F 85 51 02 00 00               jne 0x14089c585
0089C334  48 8B C6                        mov rax, rsi
0089C337  33 C9                           xor ecx, ecx
0089C339  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
0089C33E  0F 85 80 14 00 00               jne 0x14089d7c4
0089C344  48 8B CF                        mov rcx, rdi
0089C347  E8 B4 52 A4 FF                  call 0x1402e1600
0089C34C  E8 EF 68 A4 FF                  call 0x1402e2c40
0089C351  4D 85 F6                        test r14, r14
0089C354  0F 84 37 14 00 00               je 0x14089d791
0089C35A  45 33 FF                        xor r15d, r15d
0089C35D  48 8B B5 B8 00 00 00            mov rsi, qword ptr [rbp + 0xb8]
0089C364  4D 85 F6                        test r14, r14
0089C367  0F 84 C7 09 00 00               je 0x14089cd34
0089C36D  49 83 3E 00                     cmp qword ptr [r14], 0
0089C371  0F 84 BD 09 00 00               je 0x14089cd34
0089C377  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
0089C37B  0F B7 06                        movzx eax, word ptr [rsi]
0089C37E  44 0F B7 56 02                  movzx r10d, word ptr [rsi + 2]
0089C383  66 83 E8 08                     sub ax, 8
0089C387  48 8B BD C8 00 00 00            mov rdi, qword ptr [rbp + 0xc8]
0089C38E  66 41 83 EA 08                  sub r10w, 8
0089C393  48 3B 3D 46 A7 72 00            cmp rdi, qword ptr [rip + 0x72a746]
0089C39A  4C 8D 41 08                     lea r8, [rcx + 8]
0089C39E  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
0089C3A3  44 0F B7 C8                     movzx r9d, ax
0089C3A7  66 89 44 24 70                  mov word ptr [rsp + 0x70], ax
0089C3AC  66 44 89 54 24 72               mov word ptr [rsp + 0x72], r10w
0089C3B2  0F 85 27 02 00 00               jne 0x14089c5df
0089C3B8  F6 45 88 01                     test byte ptr [rbp - 0x78], 1
0089C3BC  0F 84 1D 02 00 00               je 0x14089c5df
0089C3C2  66 83 F8 06                     cmp ax, 6
0089C3C6  0F 82 13 02 00 00               jb 0x14089c5df
0089C3CC  66 83 79 0A 3A                  cmp word ptr [rcx + 0xa], 0x3a
0089C3D1  0F 85 08 02 00 00               jne 0x14089c5df
0089C3D7  66 83 79 0C 5C                  cmp word ptr [rcx + 0xc], 0x5c
0089C3DC  0F 85 FD 01 00 00               jne 0x14089c5df
0089C3E2  41 0F B7 00                     movzx eax, word ptr [r8]
0089C3E6  83 C8 20                        or eax, 0x20
0089C3E9  83 E8 61                        sub eax, 0x61
0089C3EC  83 F8 1A                        cmp eax, 0x1a
0089C3EF  0F 83 EA 01 00 00               jae 0x14089c5df
0089C3F5  4C 8D 3C C5 20 00 00 00         lea r15, [rax*8 + 0x20]
0089C3FD  4B 83 3C 37 00                  cmp qword ptr [r15 + r14], 0
0089C402  4B 8D 1C 37                     lea rbx, [r15 + r14]
0089C406  0F 84 B8 12 00 00               je 0x14089d6c4
0089C40C  0F 0D 0B                        prefetchw byte ptr [rbx]
0089C40F  48 8B 13                        mov rdx, qword ptr [rbx]
0089C412  F6 C2 0F                        test dl, 0xf
0089C415  74 15                           je 0x14089c42c
0089C417  48 8D 4A FF                     lea rcx, [rdx - 1]
0089C41B  48 8B C2                        mov rax, rdx
0089C41E  F0 48 0F B1 0B                  lock cmpxchg qword ptr [rbx], rcx
0089C423  74 07                           je 0x14089c42c
0089C425  48 8B D0                        mov rdx, rax
0089C428  A8 0F                           test al, 0xf
0089C42A  75 EB                           jne 0x14089c417
0089C42C  4C 8B EA                        mov r13, rdx
0089C42F  83 E2 0F                        and edx, 0xf
0089C432  49 83 E5 F0                     and r13, 0xfffffffffffffff0
0089C436  83 FA 01                        cmp edx, 1
0089C439  0F 86 55 06 00 00               jbe 0x14089ca94
0089C43F  49 8D 4D D0                     lea rcx, [r13 - 0x30]
0089C443  BA 01 00 00 00                  mov edx, 1
0089C448  41 B8 4F 62 4C 55               mov r8d, 0x554c624f
0089C44E  E8 2D 43 97 FF                  call 0x140210780
0089C453  4D 85 ED                        test r13, r13
0089C456  0F 84 D8 11 00 00               je 0x14089d634
0089C45C  48 83 44 24 78 04               add qword ptr [rsp + 0x78], 4
0089C462  49 8D 4D D0                     lea rcx, [r13 - 0x30]
0089C466  48 8B B5 B8 00 00 00            mov rsi, qword ptr [rbp + 0xb8]
0089C46D  B8 FC FF 00 00                  mov eax, 0xfffc
0089C472  66 01 44 24 70                  add word ptr [rsp + 0x70], ax
0089C477  45 33 FF                        xor r15d, r15d
0089C47A  48 8B 05 5F AA 72 00            mov rax, qword ptr [rip + 0x72aa5f]
0089C481  44 8B B5 C0 00 00 00            mov r14d, dword ptr [rbp + 0xc0]
0089C488  44 0F B6 4C 24 64               movzx r9d, byte ptr [rsp + 0x64]
0089C48E  4C 8B 85 F8 00 00 00            mov r8, qword ptr [rbp + 0xf8]
0089C495  48 8B 95 C8 00 00 00            mov rdx, qword ptr [rbp + 0xc8]
0089C49C  48 C1 E9 08                     shr rcx, 8
0089C4A0  41 32 4D E8                     xor cl, byte ptr [r13 - 0x18]
0089C4A4  32 0D A2 A9 72 00               xor cl, byte ptr [rip + 0x72a9a2]
0089C4AA  4C 89 7D F8                     mov qword ptr [rbp - 8], r15
0089C4AE  3A 48 28                        cmp cl, byte ptr [rax + 0x28]
0089C4B1  48 8D 45 F8                     lea rax, [rbp - 8]
0089C4B5  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0089C4BA  49 8B CD                        mov rcx, r13
0089C4BD  48 8D 45 C0                     lea rax, [rbp - 0x40]
0089C4C1  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0089C4C6  48 8B 85 E0 00 00 00            mov rax, qword ptr [rbp + 0xe0]
0089C4CD  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0089C4D2  48 8B 85 D8 00 00 00            mov rax, qword ptr [rbp + 0xd8]
0089C4D9  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0089C4DE  48 8D 44 24 70                  lea rax, [rsp + 0x70]
0089C4E3  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0089C4E8  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
0089C4ED  44 89 74 24 20                  mov dword ptr [rsp + 0x20], r14d
0089C4F2  0F 84 28 06 00 00               je 0x14089cb20
0089C4F8  E8 C3 70 01 00                  call 0x1408b35c0
0089C4FD  E9 23 06 00 00                  jmp 0x14089cb25
0089C502  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0089C50B  8B 80 A0 05 00 00               mov eax, dword ptr [rax + 0x5a0]
0089C511  A8 08                           test al, 8
0089C513  0F 84 52 FC FF FF               je 0x14089c16b
0089C519  66 83 3E 0E                     cmp word ptr [rsi], 0xe
0089C51D  0F 82 48 FC FF FF               jb 0x14089c16b
0089C523  E8 A8 17 18 00                  call 0x140a1dcd0
0089C528  0F B7 08                        movzx ecx, word ptr [rax]
0089C52B  E8 C0 2B FC FF                  call 0x14085f0f0
0089C530  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
0089C534  0F B7 D8                        movzx ebx, ax
0089C537  0F B7 49 08                     movzx ecx, word ptr [rcx + 8]
0089C53B  E8 B0 2B FC FF                  call 0x14085f0f0
0089C540  0F B7 D0                        movzx edx, ax
0089C543  8B 05 33 EE 56 00               mov eax, dword ptr [rip + 0x56ee33]
0089C549  A8 01                           test al, 1
0089C54B  0F 84 1A FC FF FF               je 0x14089c16b
0089C551  48 8B 4E 08                     mov rcx, qword ptr [rsi + 8]
0089C555  66 3B DA                        cmp bx, dx
0089C558  0F 85 0D FC FF FF               jne 0x14089c16b
0089C55E  66 83 79 0A 3A                  cmp word ptr [rcx + 0xa], 0x3a
0089C563  0F 85 02 FC FF FF               jne 0x14089c16b
0089C569  66 83 79 0C 5C                  cmp word ptr [rcx + 0xc], 0x5c
0089C56E  0F 85 F7 FB FF FF               jne 0x14089c16b
0089C574  41 0F BA EE 0B                  bts r14d, 0xb
0089C579  44 89 B5 C0 00 00 00            mov dword ptr [rbp + 0xc0], r14d
0089C580  E9 E6 FB FF FF                  jmp 0x14089c16b
0089C585  B8 0F 00 00 00                  mov eax, 0xf
0089C58A  F0 49 0F C1 86 F0 00 00 00      lock xadd qword ptr [r14 + 0xf0], rax
0089C593  48 85 C0                        test rax, rax
0089C596  0F 8E 38 13 00 00               jle 0x14089d8d4
0089C59C  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
0089C5A0  0F 0D 08                        prefetchw byte ptr [rax]
0089C5A3  48 8B 00                        mov rax, qword ptr [rax]
0089C5A6  48 8B C8                        mov rcx, rax
0089C5A9  83 E1 0F                        and ecx, 0xf
0089C5AC  48 83 C1 0E                     add rcx, 0xe
0089C5B0  48 83 F9 0F                     cmp rcx, 0xf
0089C5B4  0F 87 A0 16 00 00               ja 0x14089dc5a
0089C5BA  48 8B C8                        mov rcx, rax
0089C5BD  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0089C5C1  4C 3B F1                        cmp r14, rcx
0089C5C4  0F 85 90 16 00 00               jne 0x14089dc5a
0089C5CA  48 8B 55 A0                     mov rdx, qword ptr [rbp - 0x60]
0089C5CE  48 8D 48 0E                     lea rcx, [rax + 0xe]
0089C5D2  F0 48 0F B1 0A                  lock cmpxchg qword ptr [rdx], rcx
0089C5D7  0F 84 57 FD FF FF               je 0x14089c334
0089C5DD  EB C7                           jmp 0x14089c5a6
0089C5DF  4D 8B 2E                        mov r13, qword ptr [r14]
0089C5E2  48 8D 1D 17 3A 76 FF            lea rbx, [rip - 0x89c5e9]
0089C5E9  0F 28 4C 24 70                  movaps xmm1, xmmword ptr [rsp + 0x70]
0089C5EE  48 8D 3D CB 6F 01 00            lea rdi, [rip + 0x16fcb]
0089C5F5  41 BB FE FF 00 00               mov r11d, 0xfffe
0089C5FB  49 BE DF FF DF FF DF FF DF FF   movabs r14, 0xffdfffdfffdfffdf
0089C605  66 66 66 0F 1F 84 00 00 00 00 00  nop word ptr [rax + rax]
0089C610  49 8D 45 D0                     lea rax, [r13 - 0x30]
0089C614  48 C1 E8 08                     shr rax, 8
0089C618  0F B6 D0                        movzx edx, al
0089C61B  41 0F B6 45 E8                  movzx eax, byte ptr [r13 - 0x18]
0089C620  48 33 D0                        xor rdx, rax
0089C623  0F B6 05 22 A8 72 00            movzx eax, byte ptr [rip + 0x72a822]
0089C62A  48 33 D0                        xor rdx, rax
0089C62D  48 8B B4 D3 00 78 FC 00         mov rsi, qword ptr [rbx + rdx*8 + 0xfc7800]
0089C635  48 8B 9E 90 00 00 00            mov rbx, qword ptr [rsi + 0x90]
0089C63C  48 85 DB                        test rbx, rbx
0089C63F  0F 84 AC 02 00 00               je 0x14089c8f1
0089C645  4C 89 7D B8                     mov qword ptr [rbp - 0x48], r15
0089C649  48 3B DF                        cmp rbx, rdi
0089C64C  0F 84 5A 04 00 00               je 0x14089caac
0089C652  48 83 BD E8 00 00 00 00         cmp qword ptr [rbp + 0xe8], 0
0089C65A  0F 85 67 12 00 00               jne 0x14089d8c7
0089C660  49 8B CD                        mov rcx, r13
0089C663  E8 B8 33 97 FF                  call 0x14020fa20
0089C668  49 8B 3C 24                     mov rdi, qword ptr [r12]
0089C66C  48 85 FF                        test rdi, rdi
0089C66F  74 6F                           je 0x14089c6e0
0089C671  48 81 C7 28 01 00 00            add rdi, 0x128
0089C678  0F 0D 0F                        prefetchw byte ptr [rdi]
0089C67B  48 8B 07                        mov rax, qword ptr [rdi]
0089C67E  48 8B C8                        mov rcx, rax
0089C681  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0089C685  48 83 F9 10                     cmp rcx, 0x10
0089C689  48 8D 50 F0                     lea rdx, [rax - 0x10]
0089C68D  49 0F 46 D7                     cmovbe rdx, r15
0089C691  A8 02                           test al, 2
0089C693  0F 85 EA 05 00 00               jne 0x14089cc83
0089C699  F0 48 0F B1 17                  lock cmpxchg qword ptr [rdi], rdx
0089C69E  0F 85 DF 05 00 00               jne 0x14089cc83
0089C6A4  48 8B CF                        mov rcx, rdi
0089C6A7  E8 54 4F A4 FF                  call 0x1402e1600
0089C6AC  41 80 7C 24 16 00               cmp byte ptr [r12 + 0x16], 0
0089C6B2  74 14                           je 0x14089c6c8
0089C6B4  49 8B 0C 24                     mov rcx, qword ptr [r12]
0089C6B8  BA 4F 62 4C 55                  mov edx, 0x554c624f
0089C6BD  E8 DE 77 9C FF                  call 0x140263ea0
0089C6C2  41 C6 44 24 16 00               mov byte ptr [r12 + 0x16], 0
0089C6C8  4D 89 3C 24                     mov qword ptr [r12], r15
0089C6CC  41 C6 44 24 15 00               mov byte ptr [r12 + 0x15], 0
0089C6D2  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0089C6DB  E8 10 29 9C FF                  call 0x14025eff0
0089C6E0  F6 46 43 01                     test byte ptr [rsi + 0x43], 1
0089C6E4  49 8B CD                        mov rcx, r13
0089C6E7  48 8B B5 B8 00 00 00            mov rsi, qword ptr [rbp + 0xb8]
0089C6EE  44 0F B6 4C 24 64               movzx r9d, byte ptr [rsp + 0x64]
0089C6F4  48 8B 95 C8 00 00 00            mov rdx, qword ptr [rbp + 0xc8]
0089C6FB  0F 84 FE 0F 00 00               je 0x14089d6ff
0089C701  4C 8D 35 B8 16 00 00            lea r14, [rip + 0x16b8]
0089C708  49 3B DE                        cmp rbx, r14
0089C70B  4C 8B B5 F8 00 00 00            mov r14, qword ptr [rbp + 0xf8]
0089C712  4D 8B C6                        mov r8, r14
0089C715  0F 85 EA 02 00 00               jne 0x14089ca05
0089C71B  8B 9D C0 00 00 00               mov ebx, dword ptr [rbp + 0xc0]
0089C721  48 8D 45 B8                     lea rax, [rbp - 0x48]
0089C725  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0089C72A  48 8D 45 C0                     lea rax, [rbp - 0x40]
0089C72E  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0089C733  48 8B 85 E0 00 00 00            mov rax, qword ptr [rbp + 0xe0]
0089C73A  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0089C73F  48 8B 85 D8 00 00 00            mov rax, qword ptr [rbp + 0xd8]
0089C746  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0089C74B  48 8D 44 24 70                  lea rax, [rsp + 0x70]
0089C750  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0089C755  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
0089C75A  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0089C75E  E8 5D 16 00 00                  call 0x14089ddc0
0089C763  49 8B CD                        mov rcx, r13
0089C766  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
0089C76A  E8 E1 CB A5 FF                  call 0x1402f9350
0089C76F  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
0089C773  48 8B 7D 90                     mov rdi, qword ptr [rbp - 0x70]
0089C777  85 D2                           test edx, edx
0089C779  0F 88 19 05 00 00               js 0x14089cc98
0089C77F  4C 8B 6D B8                     mov r13, qword ptr [rbp - 0x48]
0089C783  48 85 FF                        test rdi, rdi
0089C786  74 13                           je 0x14089c79b
0089C788  48 8B CF                        mov rcx, rdi
0089C78B  E8 B0 06 B6 FF                  call 0x1403fce40
0089C790  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
0089C794  49 8B FF                        mov rdi, r15
0089C797  4C 89 7D 90                     mov qword ptr [rbp - 0x70], r15
0089C79B  81 FA 04 01 00 00               cmp edx, 0x104
0089C7A1  74 0E                           je 0x14089c7b1
0089C7A3  81 FA 68 03 00 00               cmp edx, 0x368
0089C7A9  49 0F 45 FD                     cmovne rdi, r13
0089C7AD  48 89 7D 90                     mov qword ptr [rbp - 0x70], rdi
0089C7B1  41 8B 4E 18                     mov ecx, dword ptr [r14 + 0x18]
0089C7B5  8B C1                           mov eax, ecx
0089C7B7  23 45 C4                        and eax, dword ptr [rbp - 0x3c]
0089C7BA  3B C1                           cmp eax, ecx
0089C7BC  0F 85 76 11 00 00               jne 0x14089d938
0089C7C2  81 FA 18 01 00 00               cmp edx, 0x118
0089C7C8  0F 85 94 02 00 00               jne 0x14089ca62
0089C7CE  0F BA E3 0C                     bt ebx, 0xc
0089C7D2  0F 82 AB 0F 00 00               jb 0x14089d783
0089C7D8  83 45 A8 FF                     add dword ptr [rbp - 0x58], -1
0089C7DC  0F 84 DD 0B 00 00               je 0x14089d3bf
0089C7E2  66 83 3E 00                     cmp word ptr [rsi], 0
0089C7E6  0F 84 A4 04 00 00               je 0x14089cc90
0089C7EC  4C 8B 75 98                     mov r14, qword ptr [rbp - 0x68]
0089C7F0  4D 85 F6                        test r14, r14
0089C7F3  74 3A                           je 0x14089c82f
0089C7F5  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
0089C7F9  48 85 C0                        test rax, rax
0089C7FC  0F 84 71 09 00 00               je 0x14089d173
0089C802  0F 0D 08                        prefetchw byte ptr [rax]
0089C805  48 8B 00                        mov rax, qword ptr [rax]
0089C808  48 8B C8                        mov rcx, rax
0089C80B  49 33 CE                        xor rcx, r14
0089C80E  48 83 F9 0F                     cmp rcx, 0xf
0089C812  0F 83 5B 09 00 00               jae 0x14089d173
0089C818  48 8B 55 A0                     mov rdx, qword ptr [rbp - 0x60]
0089C81C  48 8D 48 01                     lea rcx, [rax + 1]
0089C820  F0 48 0F B1 0A                  lock cmpxchg qword ptr [rdx], rcx
0089C825  75 E1                           jne 0x14089c808
0089C827  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
0089C82B  4C 89 7D 98                     mov qword ptr [rbp - 0x68], r15
0089C82F  49 8B 1C 24                     mov rbx, qword ptr [r12]
0089C833  48 85 DB                        test rbx, rbx
0089C836  74 73                           je 0x14089c8ab
0089C838  48 81 C3 28 01 00 00            add rbx, 0x128
0089C83F  0F 0D 0B                        prefetchw byte ptr [rbx]
0089C842  48 8B 03                        mov rax, qword ptr [rbx]
0089C845  48 8B C8                        mov rcx, rax
0089C848  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0089C84C  48 83 F9 10                     cmp rcx, 0x10
0089C850  48 8D 50 F0                     lea rdx, [rax - 0x10]
0089C854  49 0F 46 D7                     cmovbe rdx, r15
0089C858  A8 02                           test al, 2
0089C85A  0F 85 07 04 00 00               jne 0x14089cc67
0089C860  F0 48 0F B1 13                  lock cmpxchg qword ptr [rbx], rdx
0089C865  0F 85 FC 03 00 00               jne 0x14089cc67
0089C86B  48 8B CB                        mov rcx, rbx
0089C86E  E8 8D 4D A4 FF                  call 0x1402e1600
0089C873  41 80 7C 24 16 00               cmp byte ptr [r12 + 0x16], 0
0089C879  74 14                           je 0x14089c88f
0089C87B  49 8B 0C 24                     mov rcx, qword ptr [r12]
0089C87F  BA 4F 62 4C 55                  mov edx, 0x554c624f
0089C884  E8 17 76 9C FF                  call 0x140263ea0
0089C889  41 C6 44 24 16 00               mov byte ptr [r12 + 0x16], 0
0089C88F  4D 89 3C 24                     mov qword ptr [r12], r15
0089C893  41 C6 44 24 15 00               mov byte ptr [r12 + 0x15], 0
0089C899  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0089C8A2  E8 49 27 9C FF                  call 0x14025eff0
0089C8A7  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
0089C8AB  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0089C8AF  0F B7 08                        movzx ecx, word ptr [rax]
0089C8B2  81 FA 18 01 00 00               cmp edx, 0x118
0089C8B8  0F 85 21 F8 FF FF               jne 0x14089c0df
0089C8BE  66 83 F9 5C                     cmp cx, 0x5c
0089C8C2  0F 84 C8 03 00 00               je 0x14089cc90
0089C8C8  4C 8B C0                        mov r8, rax
0089C8CB  0F 10 0E                        movups xmm1, xmmword ptr [rsi]
0089C8CE  0F 29 4C 24 70                  movaps xmmword ptr [rsp + 0x70], xmm1
0089C8D3  66 41 0F 7E C9                  movd r9d, xmm1
0089C8D8  66 44 0F C5 D1 01               pextrw r10d, xmm1, 1
0089C8DE  48 8D 1D 1B 37 76 FF            lea rbx, [rip - 0x89c8e5]
0089C8E5  48 8D 3D D4 6C 01 00            lea rdi, [rip + 0x16cd4]
0089C8EC  E9 04 FD FF FF                  jmp 0x14089c5f5
0089C8F1  48 3B 35 58 2D 67 00            cmp rsi, qword ptr [rip + 0x672d58]
0089C8F8  0F 85 C9 0F 00 00               jne 0x14089d8c7
0089C8FE  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0089C902  66 45 85 C9                     test r9w, r9w
0089C906  74 29                           je 0x14089c931
0089C908  66 41 83 38 5C                  cmp word ptr [r8], 0x5c
0089C90D  75 22                           jne 0x14089c931
0089C90F  49 83 C0 02                     add r8, 2
0089C913  66 45 03 CB                     add r9w, r11w
0089C917  66 45 03 D3                     add r10w, r11w
0089C91B  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
0089C920  66 44 89 54 24 72               mov word ptr [rsp + 0x72], r10w
0089C926  66 44 89 4C 24 70               mov word ptr [rsp + 0x70], r9w
0089C92C  0F 28 4C 24 70                  movaps xmm1, xmmword ptr [rsp + 0x70]
0089C931  66 0F 7F 4D D0                  movdqa xmmword ptr [rbp - 0x30], xmm1
0089C936  66 45 85 C9                     test r9w, r9w
0089C93A  74 20                           je 0x14089c95c
0089C93C  0F 1F 40 00                     nop dword ptr [rax]
0089C940  66 41 83 38 5C                  cmp word ptr [r8], 0x5c
0089C945  74 15                           je 0x14089c95c
0089C947  49 83 C0 02                     add r8, 2
0089C94B  66 45 03 CB                     add r9w, r11w
0089C94F  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
0089C954  66 44 89 4C 24 70               mov word ptr [rsp + 0x70], r9w
0089C95A  75 E4                           jne 0x14089c940
0089C95C  0F B7 45 D0                     movzx eax, word ptr [rbp - 0x30]
0089C960  66 41 2B C1                     sub ax, r9w
0089C964  66 44 2B D0                     sub r10w, ax
0089C968  66 89 45 D0                     mov word ptr [rbp - 0x30], ax
0089C96C  66 44 89 54 24 72               mov word ptr [rsp + 0x72], r10w
0089C972  66 85 C0                        test ax, ax
0089C975  0F 84 15 03 00 00               je 0x14089cc90
0089C97B  8B 54 24 64                     mov edx, dword ptr [rsp + 0x64]
0089C97F  84 D2                           test dl, dl
0089C981  74 12                           je 0x14089c995
0089C983  48 8B 8D F8 00 00 00            mov rcx, qword ptr [rbp + 0xf8]
0089C98A  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
0089C98D  A8 01                           test al, 1
0089C98F  0F 84 81 08 00 00               je 0x14089d216
0089C995  48 83 BD E8 00 00 00 00         cmp qword ptr [rbp + 0xe8], 0
0089C99D  0F 85 60 07 00 00               jne 0x14089d103
0089C9A3  40 32 F6                        xor sil, sil
0089C9A6  49 83 3C 24 00                  cmp qword ptr [r12], 0
0089C9AB  0F 84 1D 05 00 00               je 0x14089cece
0089C9B1  49 8D 9D 28 01 00 00            lea rbx, [r13 + 0x128]
0089C9B8  45 33 C0                        xor r8d, r8d
0089C9BB  48 8B CB                        mov rcx, rbx
0089C9BE  33 D2                           xor edx, edx
0089C9C0  E8 6B 38 97 FF                  call 0x140210230
0089C9C5  48 8B F8                        mov rdi, rax
0089C9C8  40 84 F6                        test sil, sil
0089C9CB  0F 85 88 03 00 00               jne 0x14089cd59
0089C9D1  33 C0                           xor eax, eax
0089C9D3  41 BC 11 00 00 00               mov r12d, 0x11
0089C9D9  F0 4C 0F B1 23                  lock cmpxchg qword ptr [rbx], r12
0089C9DE  74 10                           je 0x14089c9f0
0089C9E0  4C 8B CB                        mov r9, rbx
0089C9E3  4C 8B C7                        mov r8, rdi
0089C9E6  33 D2                           xor edx, edx
0089C9E8  48 8B CB                        mov rcx, rbx
0089C9EB  E8 5C 3A 97 FF                  call 0x14021044c
0089C9F0  48 85 FF                        test rdi, rdi
0089C9F3  74 04                           je 0x14089c9f9
0089C9F5  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
0089C9F9  4C 8B A5 00 01 00 00            mov r12, qword ptr [rbp + 0x100]
0089CA00  E9 73 03 00 00                  jmp 0x14089cd78
0089CA05  48 8D 05 04 1B 00 00            lea rax, [rip + 0x1b04]
0089CA0C  48 3B D8                        cmp rbx, rax
0089CA0F  0F 85 83 07 00 00               jne 0x14089d198
0089CA15  8B 9D C0 00 00 00               mov ebx, dword ptr [rbp + 0xc0]
0089CA1B  48 8D 45 B8                     lea rax, [rbp - 0x48]
0089CA1F  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0089CA24  48 8D 45 C0                     lea rax, [rbp - 0x40]
0089CA28  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0089CA2D  48 8B 85 E0 00 00 00            mov rax, qword ptr [rbp + 0xe0]
0089CA34  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0089CA39  48 8B 85 D8 00 00 00            mov rax, qword ptr [rbp + 0xd8]
0089CA40  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0089CA45  48 8D 44 24 70                  lea rax, [rsp + 0x70]
0089CA4A  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0089CA4F  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
0089CA54  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0089CA58  E8 B3 1A 00 00                  call 0x14089e510
0089CA5D  E9 01 FD FF FF                  jmp 0x14089c763
0089CA62  81 FA 04 01 00 00               cmp edx, 0x104
0089CA68  0F 84 60 FD FF FF               je 0x14089c7ce
0089CA6E  81 FA 68 03 00 00               cmp edx, 0x368
0089CA74  0F 84 54 FD FF FF               je 0x14089c7ce
0089CA7A  4D 85 ED                        test r13, r13
0089CA7D  75 09                           jne 0x14089ca88
0089CA7F  BA 34 00 00 C0                  mov edx, 0xc0000034
0089CA84  89 54 24 60                     mov dword ptr [rsp + 0x60], edx
0089CA88  49 8B FF                        mov rdi, r15
0089CA8B  4C 89 7D 90                     mov qword ptr [rbp - 0x70], r15
0089CA8F  E9 75 07 00 00                  jmp 0x14089d209
0089CA94  85 D2                           test edx, edx
0089CA96  0F 84 98 0B 00 00               je 0x14089d634
0089CA9C  49 8B D5                        mov rdx, r13
0089CA9F  48 8B CB                        mov rcx, rbx
0089CAA2  E8 89 B6 B8 FF                  call 0x140428130
0089CAA7  E9 93 F9 FF FF                  jmp 0x14089c43f
0089CAAC  48 8B B5 B8 00 00 00            mov rsi, qword ptr [rbp + 0xb8]
0089CAB3  48 8D 45 B8                     lea rax, [rbp - 0x48]
0089CAB7  4C 8B B5 F8 00 00 00            mov r14, qword ptr [rbp + 0xf8]
0089CABE  49 8B CD                        mov rcx, r13
0089CAC1  8B 9D C0 00 00 00               mov ebx, dword ptr [rbp + 0xc0]
0089CAC7  4D 8B C6                        mov r8, r14
0089CACA  44 0F B6 4C 24 64               movzx r9d, byte ptr [rsp + 0x64]
0089CAD0  48 8B 95 C8 00 00 00            mov rdx, qword ptr [rbp + 0xc8]
0089CAD7  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0089CADC  48 8D 45 C0                     lea rax, [rbp - 0x40]
0089CAE0  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0089CAE5  48 8B 85 E0 00 00 00            mov rax, qword ptr [rbp + 0xe0]
0089CAEC  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0089CAF1  48 8B 85 D8 00 00 00            mov rax, qword ptr [rbp + 0xd8]
0089CAF8  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0089CAFD  48 8D 44 24 70                  lea rax, [rsp + 0x70]
0089CB02  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0089CB07  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
0089CB0C  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0089CB10  E8 AB 6A 01 00                  call 0x1408b35c0
0089CB15  8B D0                           mov edx, eax
0089CB17  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
0089CB1B  E9 53 FC FF FF                  jmp 0x14089c773
0089CB20  E8 EB 19 00 00                  call 0x14089e510
0089CB25  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
0089CB29  0F 0D 0B                        prefetchw byte ptr [rbx]
0089CB2C  48 8B 03                        mov rax, qword ptr [rbx]
0089CB2F  48 8B C8                        mov rcx, rax
0089CB32  49 33 CD                        xor rcx, r13
0089CB35  48 83 F9 0F                     cmp rcx, 0xf
0089CB39  0F 83 B9 0F 00 00               jae 0x14089daf8
0089CB3F  48 8D 48 01                     lea rcx, [rax + 1]
0089CB43  F0 48 0F B1 0B                  lock cmpxchg qword ptr [rbx], rcx
0089CB48  75 E5                           jne 0x14089cb2f
0089CB4A  44 39 3D BF 84 72 00            cmp dword ptr [rip + 0x7284bf], r15d
0089CB51  74 15                           je 0x14089cb68
0089CB53  33 D2                           xor edx, edx
0089CB55  49 8D 4D D0                     lea rcx, [r13 - 0x30]
0089CB59  41 B9 4F 62 4C 55               mov r9d, 0x554c624f
0089CB5F  44 8D 42 01                     lea r8d, [rdx + 1]
0089CB63  E8 7C 3E 97 FF                  call 0x1402109e4
0089CB68  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
0089CB6C  48 8B 7D 90                     mov rdi, qword ptr [rbp - 0x70]
0089CB70  85 D2                           test edx, edx
0089CB72  0F 88 20 01 00 00               js 0x14089cc98
0089CB78  4C 8B 6D F8                     mov r13, qword ptr [rbp - 8]
0089CB7C  81 FA 04 01 00 00               cmp edx, 0x104
0089CB82  74 0E                           je 0x14089cb92
0089CB84  81 FA 68 03 00 00               cmp edx, 0x368
0089CB8A  49 0F 45 FD                     cmovne rdi, r13
0089CB8E  48 89 7D 90                     mov qword ptr [rbp - 0x70], rdi
0089CB92  48 8B 85 F8 00 00 00            mov rax, qword ptr [rbp + 0xf8]
0089CB99  8B 48 18                        mov ecx, dword ptr [rax + 0x18]
0089CB9C  8B C1                           mov eax, ecx
0089CB9E  23 45 C4                        and eax, dword ptr [rbp - 0x3c]
0089CBA1  3B C1                           cmp eax, ecx
0089CBA3  0F 85 8F 0D 00 00               jne 0x14089d938
0089CBA9  81 FA 18 01 00 00               cmp edx, 0x118
0089CBAF  0F 85 A1 05 00 00               jne 0x14089d156
0089CBB5  41 0F BA E6 0C                  bt r14d, 0xc
0089CBBA  0F 82 AA 0B 00 00               jb 0x14089d76a
0089CBC0  83 45 A8 FF                     add dword ptr [rbp - 0x58], -1
0089CBC4  0F 84 F5 07 00 00               je 0x14089d3bf
0089CBCA  66 44 39 3E                     cmp word ptr [rsi], r15w
0089CBCE  0F 84 BC 00 00 00               je 0x14089cc90
0089CBD4  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
0089CBD8  4C 8B 45 98                     mov r8, qword ptr [rbp - 0x68]
0089CBDC  48 85 C0                        test rax, rax
0089CBDF  0F 84 CD 09 00 00               je 0x14089d5b2
0089CBE5  0F 0D 08                        prefetchw byte ptr [rax]
0089CBE8  48 8B 00                        mov rax, qword ptr [rax]
0089CBEB  48 8B C8                        mov rcx, rax
0089CBEE  49 33 C8                        xor rcx, r8
0089CBF1  48 83 F9 0F                     cmp rcx, 0xf
0089CBF5  0F 83 B7 09 00 00               jae 0x14089d5b2
0089CBFB  48 8B 55 A0                     mov rdx, qword ptr [rbp - 0x60]
0089CBFF  48 8D 48 01                     lea rcx, [rax + 1]
0089CC03  F0 48 0F B1 0A                  lock cmpxchg qword ptr [rdx], rcx
0089CC08  75 E1                           jne 0x14089cbeb
0089CC0A  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0089CC0E  4C 89 7D 98                     mov qword ptr [rbp - 0x68], r15
0089CC12  0F B7 08                        movzx ecx, word ptr [rax]
0089CC15  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
0089CC19  3D 18 01 00 00                  cmp eax, 0x118
0089CC1E  74 54                           je 0x14089cc74
0089CC20  66 83 F9 5C                     cmp cx, 0x5c
0089CC24  75 6A                           jne 0x14089cc90
0089CC26  3D 68 03 00 00                  cmp eax, 0x368
0089CC2B  0F 84 15 05 00 00               je 0x14089d146
0089CC31  8B 15 31 84 72 00               mov edx, dword ptr [rip + 0x728431]
0089CC37  4C 8D 45 00                     lea r8, [rbp]
0089CC3B  48 8B 8D F0 00 00 00            mov rcx, qword ptr [rbp + 0xf0]
0089CC42  4C 89 7D 00                     mov qword ptr [rbp], r15
0089CC46  E8 B5 14 B5 FF                  call 0x1403ee100
0089CC4B  85 C0                           test eax, eax
0089CC4D  0F 89 CE 0F 00 00               jns 0x14089dc21
0089CC53  48 8B 05 0E 2A 67 00            mov rax, qword ptr [rip + 0x672a0e]
0089CC5A  48 89 45 00                     mov qword ptr [rbp], rax
0089CC5E  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0089CC62  E9 C6 F4 FF FF                  jmp 0x14089c12d
0089CC67  48 8B CB                        mov rcx, rbx
0089CC6A  E8 61 6C 9C FF                  call 0x1402638d0
0089CC6F  E9 F7 FB FF FF                  jmp 0x14089c86b
0089CC74  66 83 F9 5C                     cmp cx, 0x5c
0089CC78  74 16                           je 0x14089cc90
0089CC7A  4C 8B 46 08                     mov r8, qword ptr [rsi + 8]
0089CC7E  E9 48 FC FF FF                  jmp 0x14089c8cb
0089CC83  48 8B CF                        mov rcx, rdi
0089CC86  E8 45 6C 9C FF                  call 0x1402638d0
0089CC8B  E9 14 FA FF FF                  jmp 0x14089c6a4
0089CC90  C7 44 24 60 33 00 00 C0         mov dword ptr [rsp + 0x60], 0xc0000033
0089CC98  49 8B CC                        mov rcx, r12
0089CC9B  E8 90 70 9C FF                  call 0x140263d30
0089CCA0  48 8B 7D 90                     mov rdi, qword ptr [rbp - 0x70]
0089CCA4  48 85 FF                        test rdi, rdi
0089CCA7  0F 85 8E 0E 00 00               jne 0x14089db3b
0089CCAD  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
0089CCB1  48 85 C9                        test rcx, rcx
0089CCB4  74 05                           je 0x14089ccbb
0089CCB6  E8 85 01 B6 FF                  call 0x1403fce40
0089CCBB  E8 B0 07 B7 FF                  call 0x14040d470
0089CCC0  4C 8B 45 98                     mov r8, qword ptr [rbp - 0x68]
0089CCC4  4D 85 C0                        test r8, r8
0089CCC7  74 32                           je 0x14089ccfb
0089CCC9  48 8B 45 A0                     mov rax, qword ptr [rbp - 0x60]
0089CCCD  48 85 C0                        test rax, rax
0089CCD0  0F 84 DC 0A 00 00               je 0x14089d7b2
0089CCD6  0F 0D 08                        prefetchw byte ptr [rax]
0089CCD9  48 8B 00                        mov rax, qword ptr [rax]
0089CCDC  48 8B C8                        mov rcx, rax
0089CCDF  49 33 C8                        xor rcx, r8
0089CCE2  48 83 F9 0F                     cmp rcx, 0xf
0089CCE6  0F 83 C6 0A 00 00               jae 0x14089d7b2
0089CCEC  48 8B 55 A0                     mov rdx, qword ptr [rbp - 0x60]
0089CCF0  48 8D 48 01                     lea rcx, [rax + 1]
0089CCF4  F0 48 0F B1 0A                  lock cmpxchg qword ptr [rdx], rcx
0089CCF9  75 E1                           jne 0x14089ccdc
0089CCFB  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
0089CCFF  85 C0                           test eax, eax
0089CD01  78 51                           js 0x14089cd54
0089CD03  48 8B 95 08 01 00 00            mov rdx, qword ptr [rbp + 0x108]
0089CD0A  48 85 D2                        test rdx, rdx
0089CD0D  74 0C                           je 0x14089cd1b
0089CD0F  8B 4D C4                        mov ecx, dword ptr [rbp - 0x3c]
0089CD12  83 F9 FF                        cmp ecx, -1
0089CD15  0F 85 7D 10 00 00               jne 0x14089dd98
0089CD1B  48 8B 8D 10 01 00 00            mov rcx, qword ptr [rbp + 0x110]
0089CD22  4C 89 29                        mov qword ptr [rcx], r13
0089CD25  E9 75 10 00 00                  jmp 0x14089dd9f
0089CD2A  66 83 FA 06                     cmp dx, 6
0089CD2E  0F 84 93 05 00 00               je 0x14089d2c7
0089CD34  48 83 7D 80 00                  cmp qword ptr [rbp - 0x80], 0
0089CD39  75 10                           jne 0x14089cd4b
0089CD3B  48 8B 8D F0 00 00 00            mov rcx, qword ptr [rbp + 0xf0]
0089CD42  E8 B9 C7 B6 FF                  call 0x140409500
0089CD47  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0089CD4B  4C 8B 6D 80                     mov r13, qword ptr [rbp - 0x80]
0089CD4F  E9 26 FF FF FF                  jmp 0x14089cc7a
0089CD54  45 33 ED                        xor r13d, r13d
0089CD57  EB C2                           jmp 0x14089cd1b
0089CD59  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
0089CD5F  73 0E                           jae 0x14089cd6f
0089CD61  4C 8B C3                        mov r8, rbx
0089CD64  48 8B D7                        mov rdx, rdi
0089CD67  48 8B CB                        mov rcx, rbx
0089CD6A  E8 21 2F 97 FF                  call 0x14020fc90
0089CD6F  48 85 FF                        test rdi, rdi
0089CD72  74 04                           je 0x14089cd78
0089CD74  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
0089CD78  49 8B 1C 24                     mov rbx, qword ptr [r12]
0089CD7C  B8 11 00 00 00                  mov eax, 0x11
0089CD81  F0 4C 0F B1 BB 28 01 00 00      lock cmpxchg qword ptr [rbx + 0x128], r15
0089CD8A  0F 85 5E 09 00 00               jne 0x14089d6ee
0089CD90  48 8D 8B 28 01 00 00            lea rcx, [rbx + 0x128]
0089CD97  E8 64 48 A4 FF                  call 0x1402e1600
0089CD9C  41 80 7C 24 16 00               cmp byte ptr [r12 + 0x16], 0
0089CDA2  74 14                           je 0x14089cdb8
0089CDA4  49 8B 0C 24                     mov rcx, qword ptr [r12]
0089CDA8  BA 4F 62 4C 55                  mov edx, 0x554c624f
0089CDAD  E8 EE 70 9C FF                  call 0x140263ea0
0089CDB2  41 C6 44 24 16 00               mov byte ptr [r12 + 0x16], 0
0089CDB8  4D 89 2C 24                     mov qword ptr [r12], r13
0089CDBC  41 88 74 24 15                  mov byte ptr [r12 + 0x15], sil
0089CDC1  0F B7 75 D0                     movzx esi, word ptr [rbp - 0x30]
0089CDC5  4C 8B 7D D8                     mov r15, qword ptr [rbp - 0x28]
0089CDC9  D1 EE                           shr esi, 1
0089CDCB  83 FE 04                        cmp esi, 4
0089CDCE  0F 82 AE 02 00 00               jb 0x14089d082
0089CDD4  33 DB                           xor ebx, ebx
0089CDD6  49 BC 80 FF 80 FF 80 FF 80 FF   movabs r12, 0xff80ff80ff80ff80
0089CDE0  49 8B 3F                        mov rdi, qword ptr [r15]
0089CDE3  49 85 FC                        test r12, rdi
0089CDE6  0F 85 9E 04 00 00               jne 0x14089d28a
0089CDEC  49 23 FE                        and rdi, r14
0089CDEF  48 8B C3                        mov rax, rbx
0089CDF2  49 83 C7 08                     add r15, 8
0089CDF6  48 D1 E8                        shr rax, 1
0089CDF9  48 8D 1C 5B                     lea rbx, [rbx + rbx*2]
0089CDFD  48 03 C7                        add rax, rdi
0089CE00  83 C6 FC                        add esi, -4
0089CE03  48 03 D8                        add rbx, rax
0089CE06  83 FE 04                        cmp esi, 4
0089CE09  73 D5                           jae 0x14089cde0
0089CE0B  4C 8B A5 00 01 00 00            mov r12, qword ptr [rbp + 0x100]
0089CE12  4C 8B F3                        mov r14, rbx
0089CE15  49 C1 EE 20                     shr r14, 0x20
0089CE19  44 03 F3                        add r14d, ebx
0089CE1C  85 F6                           test esi, esi
0089CE1E  74 2F                           je 0x14089ce4f
0089CE20  41 0F B7 17                     movzx edx, word ptr [r15]
0089CE24  4D 8D 7F 02                     lea r15, [r15 + 2]
0089CE28  41 8B CE                        mov ecx, r14d
0089CE2B  FF CE                           dec esi
0089CE2D  D1 E9                           shr ecx, 1
0089CE2F  47 8D 34 76                     lea r14d, [r14 + r14*2]
0089CE33  44 03 F1                        add r14d, ecx
0089CE36  83 FA 61                        cmp edx, 0x61
0089CE39  72 0D                           jb 0x14089ce48
0089CE3B  83 FA 7A                        cmp edx, 0x7a
0089CE3E  0F 87 41 03 00 00               ja 0x14089d185
0089CE44  41 83 C6 E0                     add r14d, -0x20
0089CE48  44 03 F2                        add r14d, edx
0089CE4B  85 F6                           test esi, esi
0089CE4D  75 D1                           jne 0x14089ce20
0089CE4F  44 8B 45 88                     mov r8d, dword ptr [rbp - 0x78]
0089CE53  49 8D 7C 24 10                  lea rdi, [r12 + 0x10]
0089CE58  B8 4D 91 CF BA                  mov eax, 0xbacf914d
0089CE5D  44 89 37                        mov dword ptr [rdi], r14d
0089CE60  41 F7 E6                        mul r14d
0089CE63  41 8B C6                        mov eax, r14d
0089CE66  41 83 E0 40                     and r8d, 0x40
0089CE6A  2B C2                           sub eax, edx
0089CE6C  44 89 45 80                     mov dword ptr [rbp - 0x80], r8d
0089CE70  D1 E8                           shr eax, 1
0089CE72  03 C2                           add eax, edx
0089CE74  49 8D 54 24 14                  lea rdx, [r12 + 0x14]
0089CE79  C1 E8 05                        shr eax, 5
0089CE7C  0F B6 C0                        movzx eax, al
0089CE7F  6B C8 25                        imul ecx, eax, 0x25
0089CE82  41 0F B6 C6                     movzx eax, r14b
0089CE86  2A C1                           sub al, cl
0089CE88  0F B6 C8                        movzx ecx, al
0089CE8B  49 8B 04 24                     mov rax, qword ptr [r12]
0089CE8F  48 8D 34 C8                     lea rsi, [rax + rcx*8]
0089CE93  88 0A                           mov byte ptr [rdx], cl
0089CE95  48 8B 1E                        mov rbx, qword ptr [rsi]
0089CE98  48 85 DB                        test rbx, rbx
0089CE9B  74 23                           je 0x14089cec0
0089CE9D  0F 1F 00                        nop dword ptr [rax]
0089CEA0  8B 07                           mov eax, dword ptr [rdi]
0089CEA2  39 43 10                        cmp dword ptr [rbx + 0x10], eax
0089CEA5  0F 84 96 00 00 00               je 0x14089cf41
0089CEAB  48 8B F3                        mov rsi, rbx
0089CEAE  48 8B 1B                        mov rbx, qword ptr [rbx]
0089CEB1  48 85 DB                        test rbx, rbx
0089CEB4  75 EA                           jne 0x14089cea0
0089CEB6  49 8D 54 24 14                  lea rdx, [r12 + 0x14]
0089CEBB  49 8D 7C 24 10                  lea rdi, [r12 + 0x10]
0089CEC0  33 C0                           xor eax, eax
0089CEC2  48 8B DA                        mov rbx, rdx
0089CEC5  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0089CEC9  E9 FE 04 00 00                  jmp 0x14089d3cc
0089CECE  40 84 F6                        test sil, sil
0089CED1  0F 85 ED 06 00 00               jne 0x14089d5c4
0089CED7  4D 89 2C 24                     mov qword ptr [r12], r13
0089CEDB  49 8D 8D 28 01 00 00            lea rcx, [r13 + 0x128]
0089CEE2  41 88 74 24 15                  mov byte ptr [r12 + 0x15], sil
0089CEE7  45 33 C0                        xor r8d, r8d
0089CEEA  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0089CEF3  33 D2                           xor edx, edx
0089CEF5  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0089CEFC  90                              nop
0089CEFD  E8 2E 33 97 FF                  call 0x140210230
0089CF02  48 8B F8                        mov rdi, rax
0089CF05  B9 11 00 00 00                  mov ecx, 0x11
0089CF0A  33 C0                           xor eax, eax
0089CF0C  F0 49 0F B1 8D 28 01 00 00      lock cmpxchg qword ptr [r13 + 0x128], rcx
0089CF15  74 18                           je 0x14089cf2f
0089CF17  4D 8D 8D 28 01 00 00            lea r9, [r13 + 0x128]
0089CF1E  4C 8B C7                        mov r8, rdi
0089CF21  33 D2                           xor edx, edx
0089CF23  49 8D 8D 28 01 00 00            lea rcx, [r13 + 0x128]
0089CF2A  E8 1D 35 97 FF                  call 0x14021044c
0089CF2F  48 85 FF                        test rdi, rdi
0089CF32  0F 84 89 FE FF FF               je 0x14089cdc1
0089CF38  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
0089CF3C  E9 80 FE FF FF                  jmp 0x14089cdc1
0089CF41  48 8B 53 08                     mov rdx, qword ptr [rbx + 8]
0089CF45  48 8D 0D B4 30 76 FF            lea rcx, [rip - 0x89cf4c]
0089CF4C  48 83 EA 30                     sub rdx, 0x30
0089CF50  0F B6 42 1A                     movzx eax, byte ptr [rdx + 0x1a]
0089CF54  83 E0 03                        and eax, 3
0089CF57  0F B6 84 08 80 FF F0 00         movzx eax, byte ptr [rax + rcx + 0xf0ff80]
0089CF5F  48 2B D0                        sub rdx, rax
0089CF62  E8 89 12 A6 FF                  call 0x1402fe1f0
0089CF67  48 8B 80 B0 04 00 00            mov rax, qword ptr [rax + 0x4b0]
0089CF6E  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
0089CF72  0F B7 45 D0                     movzx eax, word ptr [rbp - 0x30]
0089CF76  66 3B 42 08                     cmp ax, word ptr [rdx + 8]
0089CF7A  0F 85 2B FF FF FF               jne 0x14089ceab
0089CF80  4C 8B 72 10                     mov r14, qword ptr [rdx + 0x10]
0089CF84  44 8B F8                        mov r15d, eax
0089CF87  48 8B 45 D8                     mov rax, qword ptr [rbp - 0x28]
0089CF8B  45 85 C0                        test r8d, r8d
0089CF8E  49 8B D6                        mov rdx, r14
0089CF91  48 8B C8                        mov rcx, rax
0089CF94  45 8B C7                        mov r8d, r15d
0089CF97  4D 8D 2C 07                     lea r13, [r15 + rax]
0089CF9B  0F 84 D7 02 00 00               je 0x14089d278
0089CFA1  E8 CA D6 E1 FF                  call 0x1406ba670
0089CFA6  49 3B C7                        cmp rax, r15
0089CFA9  74 32                           je 0x14089cfdd
0089CFAB  4C 8B 45 D8                     mov r8, qword ptr [rbp - 0x28]
0089CFAF  4C 8B 5D E0                     mov r11, qword ptr [rbp - 0x20]
0089CFB3  48 D1 E8                        shr rax, 1
0089CFB6  48 03 C0                        add rax, rax
0089CFB9  4C 03 C0                        add r8, rax
0089CFBC  4C 03 F0                        add r14, rax
0089CFBF  90                              nop
0089CFC0  4D 3B C5                        cmp r8, r13
0089CFC3  73 18                           jae 0x14089cfdd
0089CFC5  45 0F B7 08                     movzx r9d, word ptr [r8]
0089CFC9  45 0F B7 16                     movzx r10d, word ptr [r14]
0089CFCD  66 45 3B CA                     cmp r9w, r10w
0089CFD1  75 7A                           jne 0x14089d04d
0089CFD3  49 83 C0 02                     add r8, 2
0089CFD7  49 83 C6 02                     add r14, 2
0089CFDB  EB E3                           jmp 0x14089cfc0
0089CFDD  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
0089CFE1  49 8D 7C 24 10                  lea rdi, [r12 + 0x10]
0089CFE6  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0089CFEA  49 8D 5C 24 14                  lea rbx, [r12 + 0x14]
0089CFEF  49 89 74 24 08                  mov qword ptr [r12 + 8], rsi
0089CFF4  48 85 C0                        test rax, rax
0089CFF7  0F 84 CF 03 00 00               je 0x14089d3cc
0089CFFD  80 BD B0 00 00 00 00            cmp byte ptr [rbp + 0xb0], 0
0089D004  4C 8B 6D 80                     mov r13, qword ptr [rbp - 0x80]
0089D008  0F 84 E7 01 00 00               je 0x14089d1f5
0089D00E  4D 85 ED                        test r13, r13
0089D011  0F 84 8C 03 00 00               je 0x14089d3a3
0089D017  44 0F B7 4C 24 70               movzx r9d, word ptr [rsp + 0x70]
0089D01D  48 8D 1D DC 2F 76 FF            lea rbx, [rip - 0x89d024]
0089D024  66 45 85 C9                     test r9w, r9w
0089D028  0F 84 02 03 00 00               je 0x14089d330
0089D02E  48 8D 3D 8B 65 01 00            lea rdi, [rip + 0x1658b]
0089D035  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
0089D03A  45 33 FF                        xor r15d, r15d
0089D03D  44 0F B7 54 24 72               movzx r10d, word ptr [rsp + 0x72]
0089D043  0F 28 4C 24 70                  movaps xmm1, xmmword ptr [rsp + 0x70]
0089D048  E9 A8 F5 FF FF                  jmp 0x14089c5f5
0089D04D  41 83 F9 61                     cmp r9d, 0x61
0089D051  72 0B                           jb 0x14089d05e
0089D053  41 83 F9 7A                     cmp r9d, 0x7a
0089D057  77 31                           ja 0x14089d08a
0089D059  66 41 83 E9 20                  sub r9w, 0x20
0089D05E  41 83 FA 61                     cmp r10d, 0x61
0089D062  72 0B                           jb 0x14089d06f
0089D064  41 83 FA 7A                     cmp r10d, 0x7a
0089D068  77 5B                           ja 0x14089d0c5
0089D06A  66 41 83 EA 20                  sub r10w, 0x20
0089D06F  66 45 3B CA                     cmp r9w, r10w
0089D073  0F 84 5A FF FF FF               je 0x14089cfd3
0089D079  44 8B 45 80                     mov r8d, dword ptr [rbp - 0x80]
0089D07D  E9 29 FE FF FF                  jmp 0x14089ceab
0089D082  45 33 F6                        xor r14d, r14d
0089D085  E9 92 FD FF FF                  jmp 0x14089ce1c
0089D08A  4D 85 DB                        test r11, r11
0089D08D  74 CF                           je 0x14089d05e
0089D08F  B8 C0 00 00 00                  mov eax, 0xc0
0089D094  66 44 3B C8                     cmp r9w, ax
0089D098  72 C4                           jb 0x14089d05e
0089D09A  49 8B C1                        mov rax, r9
0089D09D  41 8B D1                        mov edx, r9d
0089D0A0  48 C1 E8 08                     shr rax, 8
0089D0A4  83 E2 0F                        and edx, 0xf
0089D0A7  41 0F B7 0C 43                  movzx ecx, word ptr [r11 + rax*2]
0089D0AC  41 8B C1                        mov eax, r9d
0089D0AF  C1 E8 04                        shr eax, 4
0089D0B2  83 E0 0F                        and eax, 0xf
0089D0B5  03 C8                           add ecx, eax
0089D0B7  41 0F B7 0C 4B                  movzx ecx, word ptr [r11 + rcx*2]
0089D0BC  03 CA                           add ecx, edx
0089D0BE  66 45 03 0C 4B                  add r9w, word ptr [r11 + rcx*2]
0089D0C3  EB 99                           jmp 0x14089d05e
0089D0C5  4D 85 DB                        test r11, r11
0089D0C8  74 A5                           je 0x14089d06f
0089D0CA  B8 C0 00 00 00                  mov eax, 0xc0
0089D0CF  66 44 3B D0                     cmp r10w, ax
0089D0D3  72 9A                           jb 0x14089d06f
0089D0D5  49 8B C2                        mov rax, r10
0089D0D8  41 8B D2                        mov edx, r10d
0089D0DB  48 C1 E8 08                     shr rax, 8
0089D0DF  83 E2 0F                        and edx, 0xf
0089D0E2  41 0F B7 0C 43                  movzx ecx, word ptr [r11 + rax*2]
0089D0E7  41 8B C2                        mov eax, r10d
0089D0EA  C1 E8 04                        shr eax, 4
0089D0ED  83 E0 0F                        and eax, 0xf
0089D0F0  03 C8                           add ecx, eax
0089D0F2  41 0F B7 0C 4B                  movzx ecx, word ptr [r11 + rcx*2]
0089D0F7  03 CA                           add ecx, edx
0089D0F9  66 45 03 14 4B                  add r10w, word ptr [r11 + rcx*2]
0089D0FE  E9 6C FF FF FF                  jmp 0x14089d06f
0089D103  66 45 85 C9                     test r9w, r9w
0089D107  0F 85 96 F8 FF FF               jne 0x14089c9a3
0089D10D  E9 47 01 00 00                  jmp 0x14089d259
0089D112  48 8B 05 C7 99 72 00            mov rax, qword ptr [rip + 0x7299c7]
0089D119  49 8D 4D D0                     lea rcx, [r13 - 0x30]
0089D11D  48 C1 E9 08                     shr rcx, 8
0089D121  41 32 4D E8                     xor cl, byte ptr [r13 - 0x18]
0089D125  32 0D 21 9D 72 00               xor cl, byte ptr [rip + 0x729d21]
0089D12B  3A 48 28                        cmp cl, byte ptr [rax + 0x28]
0089D12E  0F 84 5F EF FF FF               je 0x14089c093
0089D134  49 8B CD                        mov rcx, r13
0089D137  E8 14 C2 A5 FF                  call 0x1402f9350
0089D13C  B8 3B 00 00 C0                  mov eax, 0xc000003b
0089D141  E9 59 0C 00 00                  jmp 0x14089dd9f
0089D146  48 8B 05 1B 25 67 00            mov rax, qword ptr [rip + 0x67251b]
0089D14D  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0089D151  E9 D7 EF FF FF                  jmp 0x14089c12d
0089D156  81 FA 04 01 00 00               cmp edx, 0x104
0089D15C  0F 84 53 FA FF FF               je 0x14089cbb5
0089D162  81 FA 68 03 00 00               cmp edx, 0x368
0089D168  0F 84 47 FA FF FF               je 0x14089cbb5
0089D16E  E9 07 F9 FF FF                  jmp 0x14089ca7a
0089D173  BA 01 00 00 00                  mov edx, 1
0089D178  49 8B CE                        mov rcx, r14
0089D17B  E8 68 FF 0C 00                  call 0x14096d0e8
0089D180  E9 A2 F6 FF FF                  jmp 0x14089c827
0089D185  0F B7 CA                        movzx ecx, dx
0089D188  E8 63 1F FC FF                  call 0x14085f0f0
0089D18D  0F B7 C0                        movzx eax, ax
0089D190  44 03 F0                        add r14d, eax
0089D193  E9 B3 FC FF FF                  jmp 0x14089ce4b
0089D198  48 8D 05 C1 09 16 00            lea rax, [rip + 0x1609c1]
0089D19F  48 3B D8                        cmp rbx, rax
0089D1A2  48 8D 45 B8                     lea rax, [rbp - 0x48]
0089D1A6  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0089D1AB  48 8D 45 C0                     lea rax, [rbp - 0x40]
0089D1AF  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0089D1B4  48 8B 85 E0 00 00 00            mov rax, qword ptr [rbp + 0xe0]
0089D1BB  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0089D1C0  48 8B 85 D8 00 00 00            mov rax, qword ptr [rbp + 0xd8]
0089D1C7  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0089D1CC  48 8D 44 24 70                  lea rax, [rsp + 0x70]
0089D1D1  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0089D1D6  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
0089D1DB  0F 85 DE 0A 00 00               jne 0x14089dcbf
0089D1E1  8B 9D C0 00 00 00               mov ebx, dword ptr [rbp + 0xc0]
0089D1E7  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0089D1EB  E8 70 09 16 00                  call 0x1409fdb60
0089D1F0  E9 6E F5 FF FF                  jmp 0x14089c763
0089D1F5  4D 85 ED                        test r13, r13
0089D1F8  0F 84 A5 01 00 00               je 0x14089d3a3
0089D1FE  8B 55 AC                        mov edx, dword ptr [rbp - 0x54]
0089D201  89 54 24 60                     mov dword ptr [rsp + 0x60], edx
0089D205  48 8B 7D 90                     mov rdi, qword ptr [rbp - 0x70]
0089D209  85 D2                           test edx, edx
0089D20B  0F 89 93 FA FF FF               jns 0x14089cca4
0089D211  E9 82 FA FF FF                  jmp 0x14089cc98
0089D216  48 8D 45 AC                     lea rax, [rbp - 0x54]
0089D21A  4C 8B C1                        mov r8, rcx
0089D21D  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0089D222  49 8B CD                        mov rcx, r13
0089D225  88 54 24 20                     mov byte ptr [rsp + 0x20], dl
0089D229  E8 B6 9A 02 00                  call 0x1408c6ce4
0089D22E  88 85 B0 00 00 00               mov byte ptr [rbp + 0xb0], al
0089D234  84 C0                           test al, al
0089D236  0F 85 E8 0A 00 00               jne 0x14089dd24
0089D23C  8B 55 AC                        mov edx, dword ptr [rbp - 0x54]
0089D23F  85 D2                           test edx, edx
0089D241  0F 89 D0 0A 00 00               jns 0x14089dd17
0089D247  66 83 7C 24 70 00               cmp word ptr [rsp + 0x70], 0
0089D24D  75 B2                           jne 0x14089d201
0089D24F  48 83 BD E8 00 00 00 00         cmp qword ptr [rbp + 0xe8], 0
0089D257  74 A8                           je 0x14089d201
0089D259  40 B6 01                        mov sil, 1
0089D25C  E9 45 F7 FF FF                  jmp 0x14089c9a6
0089D261  48 8B 05 00 24 67 00            mov rax, qword ptr [rip + 0x672400]
0089D268  44 8B B5 C0 00 00 00            mov r14d, dword ptr [rbp + 0xc0]
0089D26F  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0089D273  E9 B5 EE FF FF                  jmp 0x14089c12d
0089D278  E8 93 98 E2 FF                  call 0x1406c6b10
0089D27D  85 C0                           test eax, eax
0089D27F  0F 84 58 FD FF FF               je 0x14089cfdd
0089D285  E9 EF FD FF FF                  jmp 0x14089d079
0089D28A  41 BE 04 00 00 00               mov r14d, 4
0089D290  0F B7 C7                        movzx eax, di
0089D293  83 F8 61                        cmp eax, 0x61
0089D296  72 10                           jb 0x14089d2a8
0089D298  83 F8 7A                        cmp eax, 0x7a
0089D29B  76 25                           jbe 0x14089d2c2
0089D29D  0F B7 C8                        movzx ecx, ax
0089D2A0  E8 4B 1E FC FF                  call 0x14085f0f0
0089D2A5  0F B7 C0                        movzx eax, ax
0089D2A8  48 0F AC C7 10                  shrd rdi, rax, 0x10
0089D2AD  49 83 EE 01                     sub r14, 1
0089D2B1  75 DD                           jne 0x14089d290
0089D2B3  49 BE DF FF DF FF DF FF DF FF   movabs r14, 0xffdfffdfffdfffdf
0089D2BD  E9 2D FB FF FF                  jmp 0x14089cdef
0089D2C2  83 C0 E0                        add eax, -0x20
0089D2C5  EB E1                           jmp 0x14089d2a8
0089D2C7  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0089D2CB  8B 08                           mov ecx, dword ptr [rax]
0089D2CD  81 E9 5C 00 3F 00               sub ecx, 0x3f005c
0089D2D3  75 0A                           jne 0x14089d2df
0089D2D5  0F B7 48 04                     movzx ecx, word ptr [rax + 4]
0089D2D9  41 0F B7 C2                     movzx eax, r10w
0089D2DD  2B C8                           sub ecx, eax
0089D2DF  85 C9                           test ecx, ecx
0089D2E1  0F 85 4D FA FF FF               jne 0x14089cd34
0089D2E7  48 8D 55 A0                     lea rdx, [rbp - 0x60]
0089D2EB  41 8B CE                        mov ecx, r14d
0089D2EE  E8 DD F8 0C 00                  call 0x14096cbd0
0089D2F3  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
0089D2F7  48 85 C0                        test rax, rax
0089D2FA  0F 84 34 FA FF FF               je 0x14089cd34
0089D300  48 8B 08                        mov rcx, qword ptr [rax]
0089D303  48 85 C9                        test rcx, rcx
0089D306  0F 84 28 FA FF FF               je 0x14089cd34
0089D30C  44 0F B6 8D D0 00 00 00         movzx r9d, byte ptr [rbp + 0xd0]
0089D314  33 D2                           xor edx, edx
0089D316  4C 8B 85 C8 00 00 00            mov r8, qword ptr [rbp + 0xc8]
0089D31D  4C 8B E9                        mov r13, rcx
0089D320  E8 DB B9 B9 FF                  call 0x140438d00
0089D325  8B D0                           mov edx, eax
0089D327  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
0089D32B  E9 D9 FE FF FF                  jmp 0x14089d209
0089D330  49 8D 45 D0                     lea rax, [r13 - 0x30]
0089D334  48 C1 E8 08                     shr rax, 8
0089D338  0F B6 D0                        movzx edx, al
0089D33B  41 0F B6 45 E8                  movzx eax, byte ptr [r13 - 0x18]
0089D340  48 33 D0                        xor rdx, rax
0089D343  0F B6 05 02 9B 72 00            movzx eax, byte ptr [rip + 0x729b02]
0089D34A  48 33 D0                        xor rdx, rax
0089D34D  48 8B 84 D3 00 78 FC 00         mov rax, qword ptr [rbx + rdx*8 + 0xfc7800]
0089D355  48 8B 80 90 00 00 00            mov rax, qword ptr [rax + 0x90]
0089D35C  48 85 C0                        test rax, rax
0089D35F  74 1E                           je 0x14089d37f
0089D361  48 8D 3D 58 62 01 00            lea rdi, [rip + 0x16258]
0089D368  48 3B C7                        cmp rax, rdi
0089D36B  0F 84 C4 FC FF FF               je 0x14089d035
0089D371  48 83 BD E8 00 00 00 00         cmp qword ptr [rbp + 0xe8], 0
0089D379  0F 84 B6 FC FF FF               je 0x14089d035
0089D37F  44 0F B6 8D D0 00 00 00         movzx r9d, byte ptr [rbp + 0xd0]
0089D387  33 D2                           xor edx, edx
0089D389  4C 8B 85 C8 00 00 00            mov r8, qword ptr [rbp + 0xc8]
0089D390  49 8B CD                        mov rcx, r13
0089D393  E8 68 B9 B9 FF                  call 0x140438d00
0089D398  8B D0                           mov edx, eax
0089D39A  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
0089D39E  E9 62 FE FF FF                  jmp 0x14089d205
0089D3A3  66 83 7C 24 70 00               cmp word ptr [rsp + 0x70], 0
0089D3A9  0F 85 AE 03 00 00               jne 0x14089d75d
0089D3AF  4C 8B B5 E8 00 00 00            mov r14, qword ptr [rbp + 0xe8]
0089D3B6  4D 85 F6                        test r14, r14
0089D3B9  0F 85 12 04 00 00               jne 0x14089d7d1
0089D3BF  C7 44 24 60 34 00 00 C0         mov dword ptr [rsp + 0x60], 0xc0000034
0089D3C7  E9 CC F8 FF FF                  jmp 0x14089cc98
0089D3CC  44 8B 75 88                     mov r14d, dword ptr [rbp - 0x78]
0089D3D0  41 F6 C6 01                     test r14b, 1
0089D3D4  0F 84 23 FC FF FF               je 0x14089cffd
0089D3DA  4D 8B 2C 24                     mov r13, qword ptr [r12]
0089D3DE  66 90                           nop
0089D3E0  48 8B F0                        mov rsi, rax
0089D3E3  41 8B 85 50 01 00 00            mov eax, dword ptr [r13 + 0x150]
0089D3EA  A8 04                           test al, 4
0089D3EC  75 23                           jne 0x14089d411
0089D3EE  49 8B 85 30 01 00 00            mov rax, qword ptr [r13 + 0x130]
0089D3F5  48 85 C0                        test rax, rax
0089D3F8  0F 84 FF FB FF FF               je 0x14089cffd
0089D3FE  48 8B 4D 98                     mov rcx, qword ptr [rbp - 0x68]
0089D402  48 3B C1                        cmp rax, rcx
0089D405  0F 85 F1 00 00 00               jne 0x14089d4fc
0089D40B  4C 8B 69 08                     mov r13, qword ptr [rcx + 8]
0089D40F  EB 21                           jmp 0x14089d432
0089D411  A8 10                           test al, 0x10
0089D413  0F 85 16 09 00 00               jne 0x14089dd2f
0089D419  41 8B 85 50 01 00 00            mov eax, dword ptr [r13 + 0x150]
0089D420  A8 10                           test al, 0x10
0089D422  0F 85 37 09 00 00               jne 0x14089dd5f
0089D428  49 8B B5 38 01 00 00            mov rsi, qword ptr [r13 + 0x138]
0089D42F  4C 8B EE                        mov r13, rsi
0089D432  4C 89 6D E0                     mov qword ptr [rbp - 0x20], r13
0089D436  4D 85 ED                        test r13, r13
0089D439  0F 84 BE FB FF FF               je 0x14089cffd
0089D43F  45 0F B6 7C 24 16               movzx r15d, byte ptr [r12 + 0x16]
0089D445  49 8D 8D 28 01 00 00            lea rcx, [r13 + 0x128]
0089D44C  33 D2                           xor edx, edx
0089D44E  44 8D 42 01                     lea r8d, [rdx + 1]
0089D452  E8 D9 2D 97 FF                  call 0x140210230
0089D457  48 8B F0                        mov rsi, rax
0089D45A  B9 11 00 00 00                  mov ecx, 0x11
0089D45F  33 C0                           xor eax, eax
0089D461  F0 49 0F B1 8D 28 01 00 00      lock cmpxchg qword ptr [r13 + 0x128], rcx
0089D46A  0F 85 A6 06 00 00               jne 0x14089db16
0089D470  48 85 F6                        test rsi, rsi
0089D473  74 04                           je 0x14089d479
0089D475  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
0089D479  49 8B 34 24                     mov rsi, qword ptr [r12]
0089D47D  48 8B C1                        mov rax, rcx
0089D480  33 C9                           xor ecx, ecx
0089D482  F0 48 0F B1 8E 28 01 00 00      lock cmpxchg qword ptr [rsi + 0x128], rcx
0089D48B  0F 85 56 06 00 00               jne 0x14089dae7
0089D491  48 8D 8E 28 01 00 00            lea rcx, [rsi + 0x128]
0089D498  E8 63 41 A4 FF                  call 0x1402e1600
0089D49D  32 C0                           xor al, al
0089D49F  41 88 44 24 16                  mov byte ptr [r12 + 0x16], al
0089D4A4  45 84 FF                        test r15b, r15b
0089D4A7  0F 85 C1 08 00 00               jne 0x14089dd6e
0089D4AD  0F B6 03                        movzx eax, byte ptr [rbx]
0089D4B0  44 8B 45 88                     mov r8d, dword ptr [rbp - 0x78]
0089D4B4  41 83 E0 40                     and r8d, 0x40
0089D4B8  4D 89 2C 24                     mov qword ptr [r12], r13
0089D4BC  44 89 45 80                     mov dword ptr [rbp - 0x80], r8d
0089D4C0  4C 8D 34 C5 00 00 00 00         lea r14, [rax*8]
0089D4C8  4D 03 F5                        add r14, r13
0089D4CB  49 8B 36                        mov rsi, qword ptr [r14]
0089D4CE  48 85 F6                        test rsi, rsi
0089D4D1  74 1A                           je 0x14089d4ed
0089D4D3  8B 07                           mov eax, dword ptr [rdi]
0089D4D5  39 46 10                        cmp dword ptr [rsi + 0x10], eax
0089D4D8  0F 84 82 04 00 00               je 0x14089d960
0089D4DE  4C 8B F6                        mov r14, rsi
0089D4E1  48 8B 36                        mov rsi, qword ptr [rsi]
0089D4E4  48 85 F6                        test rsi, rsi
0089D4E7  75 EA                           jne 0x14089d4d3
0089D4E9  4C 8B 6D E0                     mov r13, qword ptr [rbp - 0x20]
0089D4ED  44 8B 75 88                     mov r14d, dword ptr [rbp - 0x78]
0089D4F1  33 C0                           xor eax, eax
0089D4F3  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0089D4F7  E9 E4 FE FF FF                  jmp 0x14089d3e0
0089D4FC  E8 EF 0C A6 FF                  call 0x1402fe1f0
0089D501  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
0089D50A  45 33 C0                        xor r8d, r8d
0089D50D  33 D2                           xor edx, edx
0089D50F  4C 8D 78 78                     lea r15, [rax + 0x78]
0089D513  66 FF 89 E6 01 00 00            dec word ptr [rcx + 0x1e6]
0089D51A  49 8B CF                        mov rcx, r15
0089D51D  90                              nop
0089D51E  E8 0D 2D 97 FF                  call 0x140210230
0089D523  4C 8B F0                        mov r14, rax
0089D526  B9 11 00 00 00                  mov ecx, 0x11
0089D52B  33 C0                           xor eax, eax
0089D52D  F0 49 0F B1 0F                  lock cmpxchg qword ptr [r15], rcx
0089D532  74 15                           je 0x14089d549
0089D534  4D 8B CF                        mov r9, r15
0089D537  4D 8B C6                        mov r8, r14
0089D53A  33 D2                           xor edx, edx
0089D53C  49 8B CF                        mov rcx, r15
0089D53F  E8 08 2F 97 FF                  call 0x14021044c
0089D544  B9 11 00 00 00                  mov ecx, 0x11
0089D549  4D 85 F6                        test r14, r14
0089D54C  74 05                           je 0x14089d553
0089D54E  41 C6 46 0A 01                  mov byte ptr [r14 + 0xa], 1
0089D553  49 8B 85 30 01 00 00            mov rax, qword ptr [r13 + 0x130]
0089D55A  48 85 C0                        test rax, rax
0089D55D  74 04                           je 0x14089d563
0089D55F  48 8B 70 08                     mov rsi, qword ptr [rax + 8]
0089D563  48 8B C1                        mov rax, rcx
0089D566  33 C9                           xor ecx, ecx
0089D568  F0 49 0F B1 0F                  lock cmpxchg qword ptr [r15], rcx
0089D56D  74 08                           je 0x14089d577
0089D56F  49 8B CF                        mov rcx, r15
0089D572  E8 C9 5E 9C FF                  call 0x140263440
0089D577  49 8B CF                        mov rcx, r15
0089D57A  E8 81 40 A4 FF                  call 0x1402e1600
0089D57F  E8 BC 56 A4 FF                  call 0x1402e2c40
0089D584  E9 A6 FE FF FF                  jmp 0x14089d42f
0089D589  48 C1 E8 20                     shr rax, 0x20
0089D58D  85 C0                           test eax, eax
0089D58F  0F 85 AD EC FF FF               jne 0x14089c242
0089D595  BA 44 66 6C 74                  mov edx, 0x746c6644
0089D59A  48 8B CE                        mov rcx, rsi
0089D59D  41 B7 01                        mov r15b, 1
0089D5A0  E8 3B A3 A5 FF                  call 0x1402f78e0
0089D5A5  49 8B CD                        mov rcx, r13
0089D5A8  E8 F3 7A 98 FF                  call 0x1402250a0
0089D5AD  E9 DA EC FF FF                  jmp 0x14089c28c
0089D5B2  BA 01 00 00 00                  mov edx, 1
0089D5B7  49 8B C8                        mov rcx, r8
0089D5BA  E8 29 FB 0C 00                  call 0x14096d0e8
0089D5BF  E9 46 F6 FF FF                  jmp 0x14089cc0a
0089D5C4  49 8B D5                        mov rdx, r13
0089D5C7  49 8B CC                        mov rcx, r12
0089D5CA  E8 7D 1C 10 00                  call 0x14099f24c
0089D5CF  E9 ED F7 FF FF                  jmp 0x14089cdc1
0089D5D4  48 8B 05 75 20 67 00            mov rax, qword ptr [rip + 0x672075]
0089D5DB  49 8D 4D D0                     lea rcx, [r13 - 0x30]
0089D5DF  48 C1 E9 08                     shr rcx, 8
0089D5E3  41 32 4D E8                     xor cl, byte ptr [r13 - 0x18]
0089D5E7  32 0D 5F 98 72 00               xor cl, byte ptr [rip + 0x72985f]
0089D5ED  3A 48 28                        cmp cl, byte ptr [rax + 0x28]
0089D5F0  0F 85 9D EA FF FF               jne 0x14089c093
0089D5F6  44 0F B6 8D D0 00 00 00         movzx r9d, byte ptr [rbp + 0xd0]
0089D5FE  33 D2                           xor edx, edx
0089D600  4C 8B 85 C8 00 00 00            mov r8, qword ptr [rbp + 0xc8]
0089D607  49 8B CD                        mov rcx, r13
0089D60A  E8 F1 B6 B9 FF                  call 0x140438d00
0089D60F  85 C0                           test eax, eax
0089D611  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
0089D615  49 8B CD                        mov rcx, r13
0089D618  4D 0F 49 FD                     cmovns r15, r13
0089D61C  E8 2F BD A5 FF                  call 0x1402f9350
0089D621  48 8B 85 10 01 00 00            mov rax, qword ptr [rbp + 0x110]
0089D628  4C 89 38                        mov qword ptr [rax], r15
0089D62B  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
0089D62F  E9 6B 07 00 00                  jmp 0x14089dd9f
0089D634  49 8B 4E 10                     mov rcx, qword ptr [r14 + 0x10]
0089D638  E8 63 7A 98 FF                  call 0x1402250a0
0089D63D  48 8B F8                        mov rdi, rax
0089D640  45 33 C0                        xor r8d, r8d
0089D643  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0089D64C  48 83 C7 78                     add rdi, 0x78
0089D650  33 D2                           xor edx, edx
0089D652  48 8B CF                        mov rcx, rdi
0089D655  66 FF 88 E6 01 00 00            dec word ptr [rax + 0x1e6]
0089D65C  90                              nop
0089D65D  E8 CE 2B 97 FF                  call 0x140210230
0089D662  48 8B F0                        mov rsi, rax
0089D665  B9 11 00 00 00                  mov ecx, 0x11
0089D66A  33 C0                           xor eax, eax
0089D66C  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
0089D671  74 10                           je 0x14089d683
0089D673  4C 8B CF                        mov r9, rdi
0089D676  4C 8B C6                        mov r8, rsi
0089D679  33 D2                           xor edx, edx
0089D67B  48 8B CF                        mov rcx, rdi
0089D67E  E8 C9 2D 97 FF                  call 0x14021044c
0089D683  48 85 F6                        test rsi, rsi
0089D686  74 04                           je 0x14089d68c
0089D688  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
0089D68C  BA 4F 62 4C 55                  mov edx, 0x554c624f
0089D691  48 8B CB                        mov rcx, rbx
0089D694  E8 07 47 AE FF                  call 0x140381da0
0089D699  4C 8B E8                        mov r13, rax
0089D69C  33 C9                           xor ecx, ecx
0089D69E  B8 11 00 00 00                  mov eax, 0x11
0089D6A3  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
0089D6A8  0F 85 F0 05 00 00               jne 0x14089dc9e
0089D6AE  48 8B CF                        mov rcx, rdi
0089D6B1  E8 4A 3F A4 FF                  call 0x1402e1600
0089D6B6  E8 85 55 A4 FF                  call 0x1402e2c40
0089D6BB  4D 85 ED                        test r13, r13
0089D6BE  0F 85 98 ED FF FF               jne 0x14089c45c
0089D6C4  4D 8B 76 18                     mov r14, qword ptr [r14 + 0x18]
0089D6C8  4D 85 F6                        test r14, r14
0089D6CB  0F 85 2C ED FF FF               jne 0x14089c3fd
0089D6D1  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
0089D6D6  45 33 FF                        xor r15d, r15d
0089D6D9  44 0F B7 54 24 72               movzx r10d, word ptr [rsp + 0x72]
0089D6DF  44 0F B7 4C 24 70               movzx r9d, word ptr [rsp + 0x70]
0089D6E5  4C 8B 75 98                     mov r14, qword ptr [rbp - 0x68]
0089D6E9  E9 F1 EE FF FF                  jmp 0x14089c5df
0089D6EE  48 8D 8B 28 01 00 00            lea rcx, [rbx + 0x128]
0089D6F5  E8 46 5D 9C FF                  call 0x140263440
0089D6FA  E9 91 F6 FF FF                  jmp 0x14089cd90
0089D6FF  4C 8B B5 F8 00 00 00            mov r14, qword ptr [rbp + 0xf8]
0089D706  48 8D 05 F3 7C 06 00            lea rax, [rip + 0x67cf3]
0089D70D  48 3B D8                        cmp rbx, rax
0089D710  4D 8B C6                        mov r8, r14
0089D713  48 8D 45 B8                     lea rax, [rbp - 0x48]
0089D717  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
0089D71C  48 8B 85 E0 00 00 00            mov rax, qword ptr [rbp + 0xe0]
0089D723  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0089D728  48 8B 85 D8 00 00 00            mov rax, qword ptr [rbp + 0xd8]
0089D72F  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0089D734  48 8D 44 24 70                  lea rax, [rsp + 0x70]
0089D739  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0089D73E  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
0089D743  0F 85 38 06 00 00               jne 0x14089dd81
0089D749  8B 9D C0 00 00 00               mov ebx, dword ptr [rbp + 0xc0]
0089D74F  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
0089D753  E8 A8 7C 06 00                  call 0x140905400
0089D758  E9 06 F0 FF FF                  jmp 0x14089c763
0089D75D  C7 44 24 60 3A 00 00 C0         mov dword ptr [rsp + 0x60], 0xc000003a
0089D765  E9 2E F5 FF FF                  jmp 0x14089cc98
0089D76A  81 FA 68 03 00 00               cmp edx, 0x368
0089D770  0F 84 4A F4 FF FF               je 0x14089cbc0
0089D776  C7 44 24 60 0B 05 00 C0         mov dword ptr [rsp + 0x60], 0xc000050b
0089D77E  E9 15 F5 FF FF                  jmp 0x14089cc98
0089D783  81 FA 68 03 00 00               cmp edx, 0x368
0089D789  0F 84 49 F0 FF FF               je 0x14089c7d8
0089D78F  EB E5                           jmp 0x14089d776
0089D791  45 84 FF                        test r15b, r15b
0089D794  0F 85 C0 EB FF FF               jne 0x14089c35a
0089D79A  45 33 FF                        xor r15d, r15d
0089D79D  4C 89 7D A0                     mov qword ptr [rbp - 0x60], r15
0089D7A1  E8 C6 F7 0C 00                  call 0x14096cf6c
0089D7A6  4C 8B F0                        mov r14, rax
0089D7A9  48 89 45 98                     mov qword ptr [rbp - 0x68], rax
0089D7AD  E9 AB EB FF FF                  jmp 0x14089c35d
0089D7B2  BA 01 00 00 00                  mov edx, 1
0089D7B7  49 8B C8                        mov rcx, r8
0089D7BA  E8 29 F9 0C 00                  call 0x14096d0e8
0089D7BF  E9 37 F5 FF FF                  jmp 0x14089ccfb
0089D7C4  48 8B CF                        mov rcx, rdi
0089D7C7  E8 74 5C 9C FF                  call 0x140263440
0089D7CC  E9 73 EB FF FF                  jmp 0x14089c344
0089D7D1  4C 8B BD C8 00 00 00            mov r15, qword ptr [rbp + 0xc8]
0089D7D8  4C 8D 4D D0                     lea r9, [rbp - 0x30]
0089D7DC  4C 3B 3D 6D 1E 67 00            cmp r15, qword ptr [rip + 0x671e6d]
0089D7E3  B9 08 00 00 00                  mov ecx, 8
0089D7E8  48 8B 75 E8                     mov rsi, qword ptr [rbp - 0x18]
0089D7EC  BA 04 00 00 00                  mov edx, 4
0089D7F1  8B 7C 24 64                     mov edi, dword ptr [rsp + 0x64]
0089D7F5  0F 44 D1                        cmove edx, ecx
0089D7F8  4C 8B 85 F8 00 00 00            mov r8, qword ptr [rbp + 0xf8]
0089D7FF  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
0089D804  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
0089D809  48 8B CE                        mov rcx, rsi
0089D80C  40 88 7C 24 28                  mov byte ptr [rsp + 0x28], dil
0089D811  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
0089D816  E8 25 8B 02 00                  call 0x1408c6340
0089D81B  84 C0                           test al, al
0089D81D  0F 84 25 03 00 00               je 0x14089db48
0089D823  8B 9E 54 01 00 00               mov ebx, dword ptr [rsi + 0x154]
0089D829  83 FB FF                        cmp ebx, -1
0089D82C  0F 85 AE 00 00 00               jne 0x14089d8e0
0089D832  0F B7 5D D0                     movzx ebx, word ptr [rbp - 0x30]
0089D836  41 B8 4F 62 4E 6D               mov r8d, 0x6d4e624f
0089D83C  8B D3                           mov edx, ebx
0089D83E  B9 00 01 00 00                  mov ecx, 0x100
0089D843  E8 A8 48 2E 00                  call 0x140b820f0
0089D848  48 8B F8                        mov rdi, rax
0089D84B  48 85 C0                        test rax, rax
0089D84E  0F 84 F8 00 00 00               je 0x14089d94c
0089D854  4D 8B C4                        mov r8, r12
0089D857  49 8B D6                        mov rdx, r14
0089D85A  48 8B CE                        mov rcx, rsi
0089D85D  E8 5E B2 17 00                  call 0x140a18ac0
0089D862  48 8B CF                        mov rcx, rdi
0089D865  84 C0                           test al, al
0089D867  0F 84 D8 00 00 00               je 0x14089d945
0089D86D  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
0089D871  44 8B C3                        mov r8d, ebx
0089D874  E8 C7 8F E2 FF                  call 0x1406c6840
0089D879  41 0F B6 46 EA                  movzx eax, byte ptr [r14 - 0x16]
0089D87E  49 8D 5E D0                     lea rbx, [r14 - 0x30]
0089D882  83 E0 03                        and eax, 3
0089D885  48 8D 0D 74 27 76 FF            lea rcx, [rip - 0x89d88c]
0089D88C  0F B6 84 08 80 FF F0 00         movzx eax, byte ptr [rax + rcx + 0xf0ff80]
0089D894  48 2B D8                        sub rbx, rax
0089D897  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
0089D89B  48 85 C9                        test rcx, rcx
0089D89E  74 07                           je 0x14089d8a7
0089D8A0  33 D2                           xor edx, edx
0089D8A2  E8 C9 4F 2E 00                  call 0x140b82870
0089D8A7  0F B7 45 D0                     movzx eax, word ptr [rbp - 0x30]
0089D8AB  4D 8B EE                        mov r13, r14
0089D8AE  66 89 43 08                     mov word ptr [rbx + 8], ax
0089D8B2  66 89 43 0A                     mov word ptr [rbx + 0xa], ax
0089D8B6  48 89 7B 10                     mov qword ptr [rbx + 0x10], rdi
0089D8BA  C7 44 24 60 00 00 00 00         mov dword ptr [rsp + 0x60], 0
0089D8C2  E9 D9 F3 FF FF                  jmp 0x14089cca0
0089D8C7  C7 44 24 60 24 00 00 C0         mov dword ptr [rsp + 0x60], 0xc0000024
0089D8CF  E9 C4 F3 FF FF                  jmp 0x14089cc98
0089D8D4  B9 0E 00 00 00                  mov ecx, 0xe
0089D8D9  CD 29                           int 0x29
0089D8DB  E9 BC EC FF FF                  jmp 0x14089c59c
0089D8E0  4C 3B 3D F1 92 72 00            cmp r15, qword ptr [rip + 0x7292f1]
0089D8E7  74 0D                           je 0x14089d8f6
0089D8E9  4C 3B 3D 68 1D 67 00            cmp r15, qword ptr [rip + 0x671d68]
0089D8F0  0F 85 3C FF FF FF               jne 0x14089d832
0089D8F6  E8 D5 2A 99 FF                  call 0x1402303d0
0089D8FB  3B D8                           cmp ebx, eax
0089D8FD  0F 84 2F FF FF FF               je 0x14089d832
0089D903  48 8B 0D 8E C3 73 00            mov rcx, qword ptr [rip + 0x73c38e]
0089D90A  40 0F B6 D7                     movzx edx, dil
0089D90E  E8 0D 45 FD FF                  call 0x140871e20
0089D913  84 C0                           test al, al
0089D915  0F 85 17 FF FF FF               jne 0x14089d832
0089D91B  8B 95 C0 00 00 00               mov edx, dword ptr [rbp + 0xc0]
0089D921  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0089D925  C1 EA 06                        shr edx, 6
0089D928  80 E2 01                        and dl, 1
0089D92B  E8 90 3B 1D 00                  call 0x140a714c0
0089D930  84 C0                           test al, al
0089D932  0F 85 FA FE FF FF               jne 0x14089d832
0089D938  C7 44 24 60 22 00 00 C0         mov dword ptr [rsp + 0x60], 0xc0000022
0089D940  E9 53 F3 FF FF                  jmp 0x14089cc98
0089D945  33 D2                           xor edx, edx
0089D947  E8 24 4F 2E 00                  call 0x140b82870
0089D94C  C7 44 24 60 9A 00 00 C0         mov dword ptr [rsp + 0x60], 0xc000009a
0089D954  E9 3F F3 FF FF                  jmp 0x14089cc98
0089D959  33 F6                           xor esi, esi
0089D95B  E9 BF E8 FF FF                  jmp 0x14089c21f
0089D960  48 8B 56 08                     mov rdx, qword ptr [rsi + 8]
0089D964  48 8D 0D 95 26 76 FF            lea rcx, [rip - 0x89d96b]
0089D96B  48 83 EA 30                     sub rdx, 0x30
0089D96F  0F B6 42 1A                     movzx eax, byte ptr [rdx + 0x1a]
0089D973  83 E0 03                        and eax, 3
0089D976  0F B6 84 08 80 FF F0 00         movzx eax, byte ptr [rax + rcx + 0xf0ff80]
0089D97E  48 2B D0                        sub rdx, rax
0089D981  E8 6A 08 A6 FF                  call 0x1402fe1f0
0089D986  0F B7 4D D0                     movzx ecx, word ptr [rbp - 0x30]
0089D98A  48 8B 80 B0 04 00 00            mov rax, qword ptr [rax + 0x4b0]
0089D991  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
0089D995  0F B7 42 08                     movzx eax, word ptr [rdx + 8]
0089D999  3B C8                           cmp ecx, eax
0089D99B  0F 85 3D FB FF FF               jne 0x14089d4de
0089D9A1  4C 8B 7A 10                     mov r15, qword ptr [rdx + 0x10]
0089D9A5  44 8B E9                        mov r13d, ecx
0089D9A8  48 8B 4D D8                     mov rcx, qword ptr [rbp - 0x28]
0089D9AC  45 85 C0                        test r8d, r8d
0089D9AF  49 8B D7                        mov rdx, r15
0089D9B2  45 8B C5                        mov r8d, r13d
0089D9B5  4A 8D 04 29                     lea rax, [rcx + r13]
0089D9B9  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
0089D9BD  0F 84 12 01 00 00               je 0x14089dad5
0089D9C3  E8 A8 CC E1 FF                  call 0x1406ba670
0089D9C8  49 3B C5                        cmp rax, r13
0089D9CB  74 35                           je 0x14089da02
0089D9CD  4C 8B 45 D8                     mov r8, qword ptr [rbp - 0x28]
0089D9D1  4C 8B 5D 20                     mov r11, qword ptr [rbp + 0x20]
0089D9D5  4C 8B 6D B0                     mov r13, qword ptr [rbp - 0x50]
0089D9D9  48 D1 E8                        shr rax, 1
0089D9DC  48 03 C0                        add rax, rax
0089D9DF  4C 03 C0                        add r8, rax
0089D9E2  4C 03 F8                        add r15, rax
0089D9E5  4D 3B C3                        cmp r8, r11
0089D9E8  73 18                           jae 0x14089da02
0089D9EA  45 0F B7 08                     movzx r9d, word ptr [r8]
0089D9EE  45 0F B7 17                     movzx r10d, word ptr [r15]
0089D9F2  66 45 3B CA                     cmp r9w, r10w
0089D9F6  75 2D                           jne 0x14089da25
0089D9F8  49 83 C0 02                     add r8, 2
0089D9FC  49 83 C7 02                     add r15, 2
0089DA00  EB E3                           jmp 0x14089d9e5
0089DA02  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
0089DA06  48 89 45 80                     mov qword ptr [rbp - 0x80], rax
0089DA0A  4D 89 74 24 08                  mov qword ptr [r12 + 8], r14
0089DA0F  48 85 C0                        test rax, rax
0089DA12  0F 85 E5 F5 FF FF               jne 0x14089cffd
0089DA18  4C 8B 6D E0                     mov r13, qword ptr [rbp - 0x20]
0089DA1C  44 8B 75 88                     mov r14d, dword ptr [rbp - 0x78]
0089DA20  E9 BB F9 FF FF                  jmp 0x14089d3e0
0089DA25  41 83 F9 61                     cmp r9d, 0x61
0089DA29  72 0B                           jb 0x14089da36
0089DA2B  41 83 F9 7A                     cmp r9d, 0x7a
0089DA2F  77 25                           ja 0x14089da56
0089DA31  66 41 83 E9 20                  sub r9w, 0x20
0089DA36  41 83 FA 61                     cmp r10d, 0x61
0089DA3A  72 0B                           jb 0x14089da47
0089DA3C  41 83 FA 7A                     cmp r10d, 0x7a
0089DA40  77 52                           ja 0x14089da94
0089DA42  66 41 83 EA 20                  sub r10w, 0x20
0089DA47  66 45 3B CA                     cmp r9w, r10w
0089DA4B  74 AB                           je 0x14089d9f8
0089DA4D  44 8B 45 80                     mov r8d, dword ptr [rbp - 0x80]
0089DA51  E9 88 FA FF FF                  jmp 0x14089d4de
0089DA56  4D 85 ED                        test r13, r13
0089DA59  74 DB                           je 0x14089da36
0089DA5B  B8 C0 00 00 00                  mov eax, 0xc0
0089DA60  66 44 3B C8                     cmp r9w, ax
0089DA64  72 D0                           jb 0x14089da36
0089DA66  49 8B C1                        mov rax, r9
0089DA69  41 8B D1                        mov edx, r9d
0089DA6C  48 C1 E8 08                     shr rax, 8
0089DA70  83 E2 0F                        and edx, 0xf
0089DA73  41 0F B7 4C 45 00               movzx ecx, word ptr [r13 + rax*2]
0089DA79  41 8B C1                        mov eax, r9d
0089DA7C  C1 E8 04                        shr eax, 4
0089DA7F  83 E0 0F                        and eax, 0xf
0089DA82  03 C8                           add ecx, eax
0089DA84  41 0F B7 4C 4D 00               movzx ecx, word ptr [r13 + rcx*2]
0089DA8A  03 CA                           add ecx, edx
0089DA8C  66 45 03 4C 4D 00               add r9w, word ptr [r13 + rcx*2]
0089DA92  EB A2                           jmp 0x14089da36
0089DA94  4D 85 ED                        test r13, r13
0089DA97  74 AE                           je 0x14089da47
0089DA99  B8 C0 00 00 00                  mov eax, 0xc0
0089DA9E  66 44 3B D0                     cmp r10w, ax
0089DAA2  72 A3                           jb 0x14089da47
0089DAA4  49 8B C2                        mov rax, r10
0089DAA7  41 8B D2                        mov edx, r10d
0089DAAA  48 C1 E8 08                     shr rax, 8
0089DAAE  83 E2 0F                        and edx, 0xf
0089DAB1  41 0F B7 4C 45 00               movzx ecx, word ptr [r13 + rax*2]
0089DAB7  41 8B C2                        mov eax, r10d
0089DABA  C1 E8 04                        shr eax, 4
0089DABD  83 E0 0F                        and eax, 0xf
0089DAC0  03 C8                           add ecx, eax
0089DAC2  41 0F B7 4C 4D 00               movzx ecx, word ptr [r13 + rcx*2]
0089DAC8  03 CA                           add ecx, edx
0089DACA  66 45 03 54 4D 00               add r10w, word ptr [r13 + rcx*2]
0089DAD0  E9 72 FF FF FF                  jmp 0x14089da47
0089DAD5  E8 36 90 E2 FF                  call 0x1406c6b10
0089DADA  85 C0                           test eax, eax
0089DADC  0F 84 20 FF FF FF               je 0x14089da02
0089DAE2  E9 66 FF FF FF                  jmp 0x14089da4d
0089DAE7  48 8D 8E 28 01 00 00            lea rcx, [rsi + 0x128]
0089DAEE  E8 4D 59 9C FF                  call 0x140263440
0089DAF3  E9 99 F9 FF FF                  jmp 0x14089d491
0089DAF8  BA 4F 62 4C 55                  mov edx, 0x554c624f
0089DAFD  49 8B CD                        mov rcx, r13
0089DB00  E8 DB 9D A5 FF                  call 0x1402f78e0
0089DB05  E9 5E F0 FF FF                  jmp 0x14089cb68
0089DB0A  48 8B 9D E8 00 00 00            mov rbx, qword ptr [rbp + 0xe8]
0089DB11  E9 FD E4 FF FF                  jmp 0x14089c013
0089DB16  33 D2                           xor edx, edx
0089DB18  49 8D 8D 28 01 00 00            lea rcx, [r13 + 0x128]
0089DB1F  E8 EC E6 B5 FF                  call 0x1403fc210
0089DB24  84 C0                           test al, al
0089DB26  74 66                           je 0x14089db8e
0089DB28  B9 11 00 00 00                  mov ecx, 0x11
0089DB2D  E9 3E F9 FF FF                  jmp 0x14089d470
0089DB32  48 8B 45 08                     mov rax, qword ptr [rbp + 8]
0089DB36  E9 E7 E5 FF FF                  jmp 0x14089c122
0089DB3B  48 8B CF                        mov rcx, rdi
0089DB3E  E8 FD F2 B5 FF                  call 0x1403fce40
0089DB43  E9 65 F1 FF FF                  jmp 0x14089ccad
0089DB48  8B 54 24 60                     mov edx, dword ptr [rsp + 0x60]
0089DB4C  85 D2                           test edx, edx
0089DB4E  0F 88 B1 F6 FF FF               js 0x14089d205
0089DB54  BA 34 00 00 C0                  mov edx, 0xc0000034
0089DB59  E9 A3 F6 FF FF                  jmp 0x14089d201
0089DB5E  44 0F B6 8D D0 00 00 00         movzx r9d, byte ptr [rbp + 0xd0]
0089DB66  33 D2                           xor edx, edx
0089DB68  4C 8B 85 C8 00 00 00            mov r8, qword ptr [rbp + 0xc8]
0089DB6F  48 8B CB                        mov rcx, rbx
0089DB72  E8 89 B1 B9 FF                  call 0x140438d00
0089DB77  85 C0                           test eax, eax
0089DB79  0F 88 20 02 00 00               js 0x14089dd9f
0089DB7F  48 8B 8D 10 01 00 00            mov rcx, qword ptr [rbp + 0x110]
0089DB86  48 89 19                        mov qword ptr [rcx], rbx
0089DB89  E9 11 02 00 00                  jmp 0x14089dd9f
0089DB8E  48 85 F6                        test rsi, rsi
0089DB91  0F 85 14 01 00 00               jne 0x14089dcab
0089DB97  BA 4F 62 4C 55                  mov edx, 0x554c624f
0089DB9C  49 8B CD                        mov rcx, r13
0089DB9F  E8 6C 2B 97 FF                  call 0x140210710
0089DBA4  49 8B 34 24                     mov rsi, qword ptr [r12]
0089DBA8  B8 11 00 00 00                  mov eax, 0x11
0089DBAD  33 C9                           xor ecx, ecx
0089DBAF  F0 48 0F B1 8E 28 01 00 00      lock cmpxchg qword ptr [rsi + 0x128], rcx
0089DBB8  74 0C                           je 0x14089dbc6
0089DBBA  48 8D 8E 28 01 00 00            lea rcx, [rsi + 0x128]
0089DBC1  E8 7A 58 9C FF                  call 0x140263440
0089DBC6  48 8D 8E 28 01 00 00            lea rcx, [rsi + 0x128]
0089DBCD  E8 2E 3A A4 FF                  call 0x1402e1600
0089DBD2  45 33 C0                        xor r8d, r8d
0089DBD5  49 8D 8D 28 01 00 00            lea rcx, [r13 + 0x128]
0089DBDC  33 D2                           xor edx, edx
0089DBDE  E8 4D 26 97 FF                  call 0x140210230
0089DBE3  4C 8B F0                        mov r14, rax
0089DBE6  B9 11 00 00 00                  mov ecx, 0x11
0089DBEB  33 C0                           xor eax, eax
0089DBED  F0 49 0F B1 8D 28 01 00 00      lock cmpxchg qword ptr [r13 + 0x128], rcx
0089DBF6  74 18                           je 0x14089dc10
0089DBF8  4D 8D 8D 28 01 00 00            lea r9, [r13 + 0x128]
0089DBFF  4D 8B C6                        mov r8, r14
0089DC02  33 D2                           xor edx, edx
0089DC04  49 8D 8D 28 01 00 00            lea rcx, [r13 + 0x128]
0089DC0B  E8 3C 28 97 FF                  call 0x14021044c
0089DC10  4D 85 F6                        test r14, r14
0089DC13  74 05                           je 0x14089dc1a
0089DC15  41 C6 46 0A 01                  mov byte ptr [r14 + 0xa], 1
0089DC1A  B0 01                           mov al, 1
0089DC1C  E9 7E F8 FF FF                  jmp 0x14089d49f
0089DC21  48 8B 45 00                     mov rax, qword ptr [rbp]
0089DC25  E9 34 F0 FF FF                  jmp 0x14089cc5e
0089DC2A  44 0F B6 8D D0 00 00 00         movzx r9d, byte ptr [rbp + 0xd0]
0089DC32  33 D2                           xor edx, edx
0089DC34  4C 8B 85 C8 00 00 00            mov r8, qword ptr [rbp + 0xc8]
0089DC3B  49 8B CD                        mov rcx, r13
0089DC3E  E8 BD B0 B9 FF                  call 0x140438d00
0089DC43  85 C0                           test eax, eax
0089DC45  0F 88 54 01 00 00               js 0x14089dd9f
0089DC4B  48 8B 8D 10 01 00 00            mov rcx, qword ptr [rbp + 0x110]
0089DC52  4C 89 29                        mov qword ptr [rcx], r13
0089DC55  E9 45 01 00 00                  jmp 0x14089dd9f
0089DC5A  BA 0E 00 00 00                  mov edx, 0xe
0089DC5F  49 8B CE                        mov rcx, r14
0089DC62  E8 81 F4 0C 00                  call 0x14096d0e8
0089DC67  E9 C8 E6 FF FF                  jmp 0x14089c334
0089DC6C  8B 55 C4                        mov edx, dword ptr [rbp - 0x3c]
0089DC6F  4C 8B 85 F8 00 00 00            mov r8, qword ptr [rbp + 0xf8]
0089DC76  23 D0                           and edx, eax
0089DC78  89 55 C4                        mov dword ptr [rbp - 0x3c], edx
0089DC7B  41 8B 48 18                     mov ecx, dword ptr [r8 + 0x18]
0089DC7F  8B C1                           mov eax, ecx
0089DC81  23 C2                           and eax, edx
0089DC83  3B C1                           cmp eax, ecx
0089DC85  0F 84 EC E3 FF FF               je 0x14089c077
0089DC8B  48 8B 4D F0                     mov rcx, qword ptr [rbp - 0x10]
0089DC8F  E8 BC B6 A5 FF                  call 0x1402f9350
0089DC94  B8 22 00 00 C0                  mov eax, 0xc0000022
0089DC99  E9 01 01 00 00                  jmp 0x14089dd9f
0089DC9E  48 8B CF                        mov rcx, rdi
0089DCA1  E8 9A 57 9C FF                  call 0x140263440
0089DCA6  E9 03 FA FF FF                  jmp 0x14089d6ae
0089DCAB  48 8B D6                        mov rdx, rsi
0089DCAE  49 8D 8D 28 01 00 00            lea rcx, [r13 + 0x128]
0089DCB5  E8 56 45 9C FF                  call 0x140262210
0089DCBA  E9 D8 FE FF FF                  jmp 0x14089db97
0089DCBF  8B 85 C0 00 00 00               mov eax, dword ptr [rbp + 0xc0]
0089DCC5  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0089DCC9  48 8B C3                        mov rax, rbx
0089DCCC  E8 FF CD E1 FF                  call 0x1406baad0
0089DCD1  8B 9D C0 00 00 00               mov ebx, dword ptr [rbp + 0xc0]
0089DCD7  E9 87 EA FF FF                  jmp 0x14089c763
0089DCDC  48 8B 85 C8 00 00 00            mov rax, qword ptr [rbp + 0xc8]
0089DCE3  48 8D 4D 28                     lea rcx, [rbp + 0x28]
0089DCE7  48 83 C0 10                     add rax, 0x10
0089DCEB  48 89 75 40                     mov qword ptr [rbp + 0x40], rsi
0089DCEF  48 89 45 38                     mov qword ptr [rbp + 0x38], rax
0089DCF3  48 89 5D 48                     mov qword ptr [rbp + 0x48], rbx
0089DCF7  E8 9C 93 C2 FF                  call 0x1404c7098
0089DCFC  4C 8B 44 24 78                  mov r8, qword ptr [rsp + 0x78]
0089DD01  44 0F B7 54 24 72               movzx r10d, word ptr [rsp + 0x72]
0089DD07  44 0F B7 4C 24 70               movzx r9d, word ptr [rsp + 0x70]
0089DD0D  0F 28 4C 24 70                  movaps xmm1, xmmword ptr [rsp + 0x70]
0089DD12  E9 C7 EB FF FF                  jmp 0x14089c8de
0089DD17  BA 34 00 00 C0                  mov edx, 0xc0000034
0089DD1C  89 55 AC                        mov dword ptr [rbp - 0x54], edx
0089DD1F  E9 23 F5 FF FF                  jmp 0x14089d247
0089DD24  44 0F B7 4C 24 70               movzx r9d, word ptr [rsp + 0x70]
0089DD2A  E9 66 EC FF FF                  jmp 0x14089c995
0089DD2F  41 F6 C6 06                     test r14b, 6
0089DD33  0F 85 E0 F6 FF FF               jne 0x14089d419
0089DD39  48 8B 8D F8 00 00 00            mov rcx, qword ptr [rbp + 0xf8]
0089DD40  0F B6 54 24 64                  movzx edx, byte ptr [rsp + 0x64]
0089DD45  48 83 C1 20                     add rcx, 0x20
0089DD49  E8 62 5D 01 00                  call 0x1408b3ab0
0089DD4E  84 C0                           test al, al
0089DD50  0F 84 7A BE 27 00               je 0x140b19bd0
0089DD56  41 83 CE 02                     or r14d, 2
0089DD5A  E9 75 BE 27 00                  jmp 0x140b19bd4
0089DD5F  41 F6 C6 02                     test r14b, 2
0089DD63  0F 84 C6 F6 FF FF               je 0x14089d42f
0089DD69  E9 BA F6 FF FF                  jmp 0x14089d428
0089DD6E  49 8B 0C 24                     mov rcx, qword ptr [r12]
0089DD72  BA 4F 62 4C 55                  mov edx, 0x554c624f
0089DD77  E8 24 61 9C FF                  call 0x140263ea0
0089DD7C  E9 2C F7 FF FF                  jmp 0x14089d4ad
0089DD81  8B 85 C0 00 00 00               mov eax, dword ptr [rbp + 0xc0]
0089DD87  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
0089DD8B  48 8B C3                        mov rax, rbx
0089DD8E  E8 3D CD E1 FF                  call 0x1406baad0
0089DD93  E9 39 FF FF FF                  jmp 0x14089dcd1
0089DD98  89 0A                           mov dword ptr [rdx], ecx
0089DD9A  E9 7C EF FF FF                  jmp 0x14089cd1b
0089DD9F  48 81 C4 68 01 00 00            add rsp, 0x168
0089DDA6  41 5F                           pop r15
0089DDA8  41 5E                           pop r14
0089DDAA  41 5D                           pop r13
0089DDAC  41 5C                           pop r12
0089DDAE  5F                              pop rdi
0089DDAF  5E                              pop rsi
0089DDB0  5B                              pop rbx
0089DDB1  5D                              pop rbp
0089DDB2  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ObpLookupObjectName(__int64 a1, __int64 a2, int a3, __int64 a4, unsigned __int8 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m100;
    unsigned __int64 v_stack_m108;
    unsigned __int64 v_stack_m110;
    unsigned __int64 v_stack_m118;
    unsigned int v_stack_m120;
    unsigned __int64 v_stack_m128;
    unsigned __int64 v_stack_m130;
    unsigned __int16 v_stack_m136;
    unsigned __int64 v_stack_m138;
    unsigned int v_stack_m144;
    unsigned int v_stack_m148;
    unsigned __int64 v_stack_m158;
    unsigned __int64 v_stack_m160;
    unsigned __int64 v_stack_m168;
    unsigned __int64 v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m180;
    unsigned int v_stack_m188;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m94;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned __int64 v_stack_mB0;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_mC0;
    unsigned __int64 v_stack_mC8;
    unsigned __int64 v_stack_mD0;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE4;
    unsigned __int16 v_stack_mE6;
    unsigned __int16 v_stack_mE8;
    unsigned __int64 v_stack_mF0;
    unsigned __int64 v_stack_mF8;
    unsigned int v_stack_mFC;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p40;
    unsigned __int8 v_stack_p8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (360);
    v_r15 = 0;
    result = 0;
    v_stack_mB8 = 0;
    v_stack_m50 = 0;
    v_stack_mE6 = 0;
    *(unsigned __int64 *)(a11) = v_xmm1;
    *(unsigned __int64 *)(a11 + 16) = 0;
    v_stack_m98 = 0;
    v_stack_m110 = 0;
    v_stack_m108 = 0;
    v_stack_m100 = 64;
    v_stack_m80 = v_xmm0;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m138 = v_xmm0;
    if (a12 != 0) {
        *(unsigned int *)(a12) = 0;
    }
    v_stack_m148 = 0;
    v_stack_mFC = 0;
    *(unsigned __int64 *)(a13) = 0;
    v_stack_mE8 = 16;
    v_stack_p8 = 1;
    v_stack_m118 = 0;
    v_stack_m128 = 0;
    v_stack_mE4 = 0xFFFFFFFFULL;
    v_stack_mE0 = a9;
    if ((*(unsigned int *)(v_rip + 5698638)) == 0) goto loc_0089BF93;
    if (((*(unsigned __int8 *)(a4 + 66)) & (1)) == 0) goto loc_0089BF93;
    v_r14 = (unsigned int)(a3);
    if (!(condition_is_below)) {
        v_r14 = (unsigned int)(((unsigned int)(a3)) | (64));
        v_stack_p18 = (unsigned int)(v_r14);
    }
    a1 = 1;
    if (condition_is_above_or_equal) { a1 = a5; }
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (64));
    v_stack_m144 = (unsigned int)(a1);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(result))) | (1));
    if (a8 != 0) { a1 = (unsigned int)(result); }
    v_stack_m120 = (unsigned int)(a1);
    if (a1 != 0) goto loc_0089C030;
    if ((unsigned __int16)(*(unsigned __int16 *)(a2)) == 0) goto loc_0089D13C;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 8))) != 92) goto loc_0089D13C;
    if (((unsigned __int16)(*(unsigned __int16 *)(a2))) != 2) goto loc_0089C0BB;
    v_stack_p40 = 0;
    result = PsGetPermanentSiloContext(a9, (unsigned int)(*(unsigned int *)(v_rip + 7508090)), a8, a4);
    if (!sign_flag) goto loc_0089DB0A;
loc_0089C013:
    if (*(unsigned __int64 *)(v_rip + 6764117) != 0) goto loc_0089DB5E;
    if (a8 != 0) goto loc_0089DC2A;
    goto loc_0089DD9F;
loc_0089C030:
    v_stack_m170 = v_stack_m98;
    a3 = 0;
    v_stack_m178 = 0;
    v_stack_m180 = v_stack_mB8;
    a2 = 0;
    v_stack_m188 = 0x746C6644ULL;
    result = ObpReferenceObjectByHandleWithTag(*(unsigned __int64 *)(v_rip + 6764117), a2, a3, (unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 7508090))));
    v_stack_m148 = (unsigned int)(result);
    if (sign_flag) goto loc_0089DD9F;
    if ((unsigned int)((unsigned int)(v_stack_m94)) != 0) goto loc_0089DC6C;
loc_0089C077:
    if ((*(unsigned __int16 *)(a2)) == 0) goto loc_0089D5D4;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 8))) == 92) goto loc_0089D112;
loc_0089C093:
    v_stack_m138 = v_xmm1;
    if ((*(unsigned int *)(v_rip + 7592510)) != 0) goto loc_0089DCDC;
    goto loc_0089C8D3;
loc_0089C0BB:
    if ((*(unsigned int *)(v_rip + 7592470)) == 0) goto loc_0089C134;
    v_stack_m68 = 0;
    v_stack_m70 = (unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 7508090))) + 16;
    v_stack_m60 = 0;
    result = SeSetLearningModeObjectInformation(v_stack_m80, a2, a3, (unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 7508090))));
    goto loc_0089C12D;
loc_0089C0DF:
    if (((unsigned __int16)(v_stack_m80)) != 92) goto loc_0089CC90;
    if (0 == 872) goto loc_0089D261;
    v_stack_mA0 = 0;
    result = PsGetPermanentSiloContext(a9, (unsigned int)(*(unsigned int *)(v_rip + 7507821)), v_stack_mA0, (unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 7508090))));
    if (!sign_flag) goto loc_0089DB32;
    v_stack_mA0 = *(unsigned __int64 *)(v_rip + 6763850);
loc_0089C122:
    v_stack_m128 = *(unsigned __int64 *)(v_rip + 6763850);
loc_0089C12D:
loc_0089C134:
    if (((unsigned __int16)(*(unsigned __int16 *)(a2))) < 8) goto loc_0089CD2A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 8))) != v_stack_mA0) goto loc_0089CD2A;
    if (v_stack_p20 == (*(unsigned __int64 *)(v_rip + 7514491))) goto loc_0089C502;
loc_0089C16B:
    v_stack_m110 = 0;
    v_stack_m108 = 0;
    result = PsGetProcessServerSilo(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544), *(unsigned __int16 *)(a2), v_stack_mA0, v_stack_p20);
    result = PsGetThreadServerSilo(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int16 *)(a2), v_stack_mA0, v_stack_p20);
    v_r14 = (result != result) ? 1 : 0;
    a1 = ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (8)) != 0) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_0089C27C;
    if (result != result) goto loc_0089C27C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (8)) == 0) goto loc_0089C27C;
    result = PspLockThreadSecurityShared(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_mA0, v_stack_p20);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (8)) == 0) goto loc_0089D959;
    v_rsi = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1608);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1608) == 0) {
        v_rsi = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1336);
        v_rsi = (v_rsi) & (-8);
    }
    result = ObfReferenceObjectWithTag(v_rsi, (unsigned int)(0x746C6644ULL), v_stack_mA0, v_stack_p20);
loc_0089C21F:
    result = PspUnlockThreadSecurityShared(*(unsigned __int64 *)(gs_base + (0 + 392)), *(unsigned __int64 *)(gs_base + (0 + 392)), v_stack_mA0, v_stack_p20);
    if (v_rsi == 0) goto loc_0089C27C;
    if (((unsigned int)(*(unsigned __int64 *)(v_rsi + 24))) == 999) goto loc_0089D589;
loc_0089C242:
    v_stack_m90 = 0;
    result = SeGetTokenDeviceMap(v_rsi, v_stack_m90, v_stack_mA0, v_stack_p20);
    if (!(sign_flag)) {
        a3 = v_stack_m90;
        v_stack_m110 = a3;
    }
    result = ObfDereferenceObjectWithTag(v_rsi, (unsigned int)(0x746C6644ULL), a3, v_stack_p20);
    if (v_stack_m110 != 0) goto loc_0089C35A;
loc_0089C27C:
    if ((unsigned __int8)((unsigned __int8)(v_r14)) != 0) goto loc_0089D5A5;
loc_0089C28C:
    v_stack_m108 = *(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 792;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 792))) & (15)) == 0) goto loc_0089C2B7;
loc_0089C29E:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 792))) & (15)) == 0) goto loc_0089C2B7;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 792))) & (15)) != 0) goto loc_0089C29E;
loc_0089C2B7:
    v_r14 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 792)) & (-16);
    v_stack_m110 = v_r14;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 792))) & (15)) != 0) goto loc_0089C351;
    result = PsGetCurrentServerSiloGlobals(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 792) - 1, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 544) + 792), v_stack_m108, v_stack_p20);
    a3 = 0;
    v_rdi = (result) + (120);
    a2 = 0;
    result = KeAbPreAcquire(v_rdi, a2, a3, v_stack_p20);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rdi;
        a3 = 0;
        a2 = 0;
        a1 = v_rdi;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_r14 = (*(unsigned __int64 *)(v_stack_m108)) & (-16);
    v_stack_m110 = v_r14;
    if (condition_is_not_equal) goto loc_0089C585;
loc_0089C334:
    a1 = 0;
    if (condition_is_not_equal) goto loc_0089D7C4;
loc_0089C344:
    result = KeAbPostRelease(v_rdi, a2, a3, a4);
    result = KeLeaveGuardedRegion(v_rdi, a2, a3, a4);
loc_0089C351:
    if (v_r14 == 0) goto loc_0089D791;
loc_0089C35A:
    v_r15 = 0;
loc_0089C35D:
    if (v_r14 == 0) goto loc_0089CD34;
    if ((*(unsigned __int64 *)(v_r14)) == 0) goto loc_0089CD34;
    result = (unsigned __int16)((*(unsigned __int16 *)(v_stack_p10)) - (8));
    v_r10 = (unsigned __int16)((*(unsigned __int16 *)(v_stack_p10 + 2)) - (8));
    v_stack_m130 = *(unsigned __int64 *)(v_stack_p10 + 8) + 8;
    v_stack_m138 = (unsigned __int16)(result);
    v_stack_m136 = (unsigned __int16)(v_r10);
    if (v_stack_p20 != (*(unsigned __int64 *)(v_rip + 7513926))) goto loc_0089C5DF;
    if (((v_stack_m120) & (1)) == 0) goto loc_0089C5DF;
    if (((unsigned __int16)(result)) < 6) goto loc_0089C5DF;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10 + 8) + 10)) != 58) goto loc_0089C5DF;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10 + 8) + 12)) != 92) goto loc_0089C5DF;
    result = (unsigned int)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10 + 8) + 8)) | (32));
    result = (unsigned int)((result) - (97));
    if (((unsigned int)(result)) >= 26) goto loc_0089C5DF;
loc_0089C3FD:
    if ((*(unsigned __int64 *)(result * 8 + 32 + v_r14 * 1)) == 0) goto loc_0089D6C4;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result * 8 + 32 + v_r14 * 1))) & (15)) == 0) goto loc_0089C42C;
loc_0089C417:
    if ((((unsigned __int8)(*(unsigned __int64 *)(result * 8 + 32 + v_r14 * 1))) & (15)) == 0) goto loc_0089C42C;
    if ((((unsigned __int8)(*(unsigned __int64 *)(result * 8 + 32 + v_r14 * 1))) & (15)) != 0) goto loc_0089C417;
loc_0089C42C:
    a2 = (unsigned int)((*(unsigned __int64 *)(result * 8 + 32 + v_r14 * 1)) & (15));
    v_r13 = (*(unsigned __int64 *)(result * 8 + 32 + v_r14 * 1)) & (-16);
    if (((unsigned int)(a2)) <= 1) goto loc_0089CA94;
loc_0089C43F:
    result = ObpTraceObjectReferenceIfActive(v_r13 - 48, 1, (unsigned int)(0x554C624FULL), (unsigned __int16)(result));
    if (v_r13 == 0) goto loc_0089D634;
loc_0089C45C:
    v_r15 = 0;
    a1 = (v_r13 - 48) >> (8);
    a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(v_r13 - 24)));
    a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(v_rip + 7514530)));
    v_stack_mB0 = 0;
    v_stack_m158 = v_stack_mB0;
    v_stack_m160 = v_stack_mE8;
    v_stack_m168 = a7;
    v_stack_m170 = a6;
    v_stack_m178 = v_stack_m138;
    v_stack_m180 = v_stack_p10;
    v_stack_m188 = (unsigned int)((unsigned int)(v_stack_p18));
    if (((unsigned __int8)(a1)) == (*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 7514719) + 40))) goto loc_0089CB20;
    result = ObpParseSymbolicLinkEx(v_r13, v_stack_p20, a10, v_stack_m144);
    goto loc_0089CB25;
loc_0089C502:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 1440)))) & (8)) == 0) goto loc_0089C16B;
    if ((*(unsigned __int16 *)(v_stack_p10)) < 14) goto loc_0089C16B;
    result = RtlGetNtSystemRoot(v_r13, v_stack_p20, a10, v_stack_m144);
    result = RtlUpcaseUnicodeChar(*(unsigned __int16 *)(result), v_stack_p20, a10, v_stack_m144);
    result = RtlUpcaseUnicodeChar(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10 + 8) + 8), v_stack_p20, a10, v_stack_m144);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 5697075)))) & (1)) == 0) goto loc_0089C16B;
    if (((unsigned __int16)((unsigned __int16)(result))) != ((unsigned __int16)((unsigned __int16)(result)))) goto loc_0089C16B;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10 + 8) + 10)) != 58) goto loc_0089C16B;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10 + 8) + 12)) != 92) goto loc_0089C16B;
    v_stack_p18 = (unsigned int)((unsigned int)(v_stack_p18));
    goto loc_0089C16B;
loc_0089C585:
    if (condition_is_less_or_equal) goto loc_0089D8D4;
loc_0089C59C:
loc_0089C5A6:
    a1 = (unsigned int)((*(unsigned __int64 *)(v_stack_m108)) & (15));
    a1 = (a1) + (14);
    if (a1 > 15) goto loc_0089DC5A;
    a1 = (*(unsigned __int64 *)(v_stack_m108)) & (-16);
    if (((unsigned int)(v_stack_p18)) != a1) goto loc_0089DC5A;
    if (((unsigned int)(v_stack_p18)) == a1) goto loc_0089C334;
    goto loc_0089C5A6;
loc_0089C5DF:
loc_0089C5F5:
    result = (*(unsigned __int64 *)((unsigned int)(v_stack_p18)) - 48) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)((unsigned int)(v_stack_p18)) - 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 7514146));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9029097 + a2 * 8 + 16545792) + 144) == 0) goto loc_0089C8F1;
    v_stack_mF0 = 0;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9029097 + a2 * 8 + 16545792) + 144)) == (v_rip + 94155)) goto loc_0089CAAC;
    if (a8 != 0) goto loc_0089D8C7;
    result = ObfReferenceObject(*(unsigned __int64 *)((unsigned int)(v_stack_p18)), a2, a10, v_stack_m144);
    if (*(unsigned __int64 *)(a11) == 0) goto loc_0089C6E0;
    v_rdi = (*(unsigned __int64 *)(a11)) + (296);
    a1 = (*(unsigned __int64 *)(v_rdi)) & (-16);
    a2 = *(unsigned __int64 *)(v_rdi) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (2)) != 0) goto loc_0089CC83;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (2)) != 0) goto loc_0089CC83;
loc_0089C6A4:
    result = KeAbPostRelease(v_rdi, a2, a10, v_stack_m144);
    if ((*(unsigned __int8 *)(a11 + 22)) != 0) {
        a1 = *(unsigned __int64 *)(a11);
        a2 = 0x554C624FULL;
        result = ObDereferenceObjectDeferDeleteWithTag(a1, a2, a10, v_stack_m144);
        *(unsigned __int8 *)(a11 + 22) = 0;
    }
    *(unsigned __int64 *)(a11) = 0;
    *(unsigned __int8 *)(a11 + 21) = 0;
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a10, v_stack_m144);
loc_0089C6E0:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip - 9029097 + a2 * 8 + 16545792) + 67)) & (1)) == 0) goto loc_0089D6FF;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip - 9029097 + a2 * 8 + 16545792) + 144)) != (v_rip + 5816)) goto loc_0089CA05;
    v_stack_m158 = v_stack_mF0;
    v_stack_m160 = v_stack_mE8;
    v_stack_m168 = a7;
    v_stack_m170 = a6;
    v_stack_m178 = v_stack_m138;
    v_stack_m180 = v_stack_p10;
    v_stack_m188 = (unsigned int)((unsigned int)(v_stack_p18));
    result = CmpParseKey(*(unsigned __int64 *)((unsigned int)(v_stack_p18)), v_stack_p20, a10, v_stack_m144);
loc_0089C763:
    v_stack_m148 = (unsigned int)(result);
    result = ObfDereferenceObject(*(unsigned __int64 *)((unsigned int)(v_stack_p18)), v_stack_p20, a10, v_stack_m144);
loc_0089C773:
    if (sign_flag) goto loc_0089CC98;
    v_rdi = v_stack_m118;
    if (v_stack_m118 != 0) {
        a1 = v_stack_m118;
        result = ObDereferenceObjectDeferDelete(a1, (unsigned int)(v_stack_m148), a10, v_stack_m144);
        a2 = v_stack_m148;
        v_rdi = 0;
        v_stack_m118 = 0;
    }
    if (((unsigned int)(a2)) != 260) {
        if (((unsigned int)(a2)) != 872) { v_rdi = v_stack_mF0; }
        v_stack_m118 = v_rdi;
    }
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a10 + 24))))) & (v_stack_mE4));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a10 + 24))))) goto loc_0089D938;
    if (((unsigned int)(a2)) != 280) goto loc_0089CA62;
loc_0089C7CE:
    if (((unsigned int)(a2)) < 280) goto loc_0089D783;
loc_0089C7D8:
    if (((unsigned int)(a2)) == 280) goto loc_0089D3BF;
    if ((*(unsigned __int16 *)(v_stack_p10)) == 0) goto loc_0089CC90;
    if (v_stack_m110 == 0) goto loc_0089C82F;
    if (v_stack_m108 == 0) goto loc_0089D173;
loc_0089C808:
    a1 = (*(unsigned __int64 *)(v_stack_m108)) ^ (v_stack_m110);
    if (a1 >= 15) goto loc_0089D173;
    if (a1 != 15) goto loc_0089C808;
loc_0089C827:
    v_stack_m110 = 0;
loc_0089C82F:
    if (*(unsigned __int64 *)(a11) == 0) goto loc_0089C8AB;
    v_rbx = (*(unsigned __int64 *)(a11)) + (296);
    a1 = (*(unsigned __int64 *)(v_rbx)) & (-16);
    a2 = *(unsigned __int64 *)(v_rbx) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbx))) & (2)) != 0) goto loc_0089CC67;
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rbx))) & (2)) != 0) goto loc_0089CC67;
loc_0089C86B:
    result = KeAbPostRelease(v_rbx, a2, a10, v_stack_m144);
    if ((*(unsigned __int8 *)(a11 + 22)) != 0) {
        a1 = *(unsigned __int64 *)(a11);
        a2 = 0x554C624FULL;
        result = ObDereferenceObjectDeferDeleteWithTag(a1, a2, a10, v_stack_m144);
        *(unsigned __int8 *)(a11 + 22) = 0;
    }
    *(unsigned __int64 *)(a11) = 0;
    *(unsigned __int8 *)(a11 + 21) = 0;
    result = KeLeaveCriticalRegionThread(*(unsigned __int64 *)(gs_base + (0 + 392)), a2, a10, v_stack_m144);
loc_0089C8AB:
    if (((unsigned int)((unsigned int)(v_stack_m148))) != 280) goto loc_0089C0DF;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10 + 8)))) == 92) goto loc_0089CC90;
loc_0089C8CB:
    v_stack_m138 = v_xmm1;
loc_0089C8D3:
loc_0089C8DE:
    goto loc_0089C5F5;
loc_0089C8F1:
    if (v_stack_p10 != (*(unsigned __int64 *)(v_rip + 6761816))) goto loc_0089D8C7;
    v_stack_mC0 = v_stack_mF0;
    if ((unsigned __int16)(v_stack_m144) == 0) goto loc_0089C931;
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10 + 8))) == 92) {
        a3 = (*(unsigned __int64 *)(v_stack_p10 + 8)) + (2);
        a4 = (unsigned __int16)((v_stack_m144) + ((unsigned __int16)((unsigned int)(0xFFFEULL))));
        v_r10 = (unsigned __int16)((v_r10) + ((unsigned __int16)((unsigned int)(0xFFFEULL))));
        v_stack_m130 = a3;
        v_stack_m136 = (unsigned __int16)(v_r10);
        v_stack_m138 = (unsigned __int16)(a4);
    }
    v_stack_mD8 = v_xmm1;
    if ((unsigned __int16)(a4) == 0) goto loc_0089C95C;
loc_0089C940:
    if ((*(unsigned __int16 *)(a3)) == 92) goto loc_0089C95C;
    a3 = (a3) + (2);
    a4 = (unsigned __int16)((a4) + ((unsigned __int16)((unsigned int)(0xFFFEULL))));
    v_stack_m130 = a3;
    v_stack_m138 = (unsigned __int16)(a4);
    if (condition_is_not_equal) goto loc_0089C940;
loc_0089C95C:
    result = (unsigned __int16)((v_stack_mD8) - ((unsigned __int16)(a4)));
    v_r10 = (unsigned __int16)((v_r10) - ((unsigned __int16)(result)));
    v_stack_mD8 = (unsigned __int16)(result);
    v_stack_m136 = (unsigned __int16)(v_r10);
    if ((unsigned __int16)(result) == 0) goto loc_0089CC90;
    if ((unsigned __int8)((unsigned int)(v_stack_m144)) == 0) goto loc_0089C995;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a10 + 12)))) & (1)) == 0) goto loc_0089D216;
loc_0089C995:
    if (a8 != 0) goto loc_0089D103;
loc_0089C9A3:
    v_rsi = 0;
loc_0089C9A6:
    if ((*(unsigned __int64 *)(a11)) == 0) goto loc_0089CECE;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_mF0 + 296, a2, a3, a4);
    if (0 != 0) goto loc_0089CD59;
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_stack_mF0 + 296;
        a3 = 0;
        a2 = 0;
        a1 = v_stack_mF0 + 296;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    goto loc_0089CD78;
loc_0089CA05:
    if ((v_stack_mF0 + 296) != (v_rip + 6916)) goto loc_0089D198;
    v_stack_m158 = v_stack_mF0;
    v_stack_m160 = v_stack_mE8;
    v_stack_m168 = a7;
    v_stack_m170 = a6;
    v_stack_m178 = v_stack_m138;
    v_stack_m180 = 0;
    v_stack_m188 = (unsigned int)((unsigned int)(v_stack_p18));
    result = IopParseDevice(a1, a2, a3, a4);
    goto loc_0089C763;
loc_0089CA62:
    if (0 == 260) goto loc_0089C7CE;
    if (0 == 872) goto loc_0089C7CE;
loc_0089CA7A:
    if (v_stack_mF0 == 0) {
        a2 = 0xC0000034ULL;
        v_stack_m148 = (unsigned int)(a2);
    }
    v_stack_m118 = 0;
    goto loc_0089D209;
loc_0089CA94:
    if ((unsigned int)(a2) == 0) goto loc_0089D634;
    result = ObpFastReplenishReference((unsigned int)(v_stack_p18), v_stack_mF0, a3, a4);
    goto loc_0089C43F;
loc_0089CAAC:
    v_stack_m158 = v_stack_mF0;
    v_stack_m160 = v_stack_mE8;
    v_stack_m168 = a7;
    v_stack_m170 = a6;
    v_stack_m178 = v_stack_m138;
    v_stack_m180 = v_stack_p10;
    v_stack_m188 = (unsigned int)((unsigned int)(v_stack_p18));
    result = ObpParseSymbolicLinkEx(v_stack_mF0, v_stack_p20, a10, v_stack_m144);
    v_stack_m148 = (unsigned int)(result);
    goto loc_0089C773;
loc_0089CB20:
    result = IopParseDevice(v_stack_mF0, (unsigned int)((unsigned int)(result)), a10, v_stack_m144);
loc_0089CB25:
    v_stack_m148 = (unsigned int)(result);
loc_0089CB2F:
    a1 = (*(unsigned __int64 *)((unsigned int)(v_stack_p18))) ^ (v_stack_mF0);
    if (a1 >= 15) goto loc_0089DAF8;
    if (a1 != 15) goto loc_0089CB2F;
    result = *(unsigned __int64 *)((unsigned int)(v_stack_p18));
    if ((*(unsigned int *)(v_rip + 7505087)) != 0) {
        a2 = 0;
        a1 = v_stack_mF0 - 48;
        a4 = 0x554C624FULL;
        a3 = a2 + 1;
        result = ObpPushStackInfo(a1, a2, a3, a4);
    }
    if (sign_flag) goto loc_0089CC98;
    v_rdi = v_stack_m118;
    if (((unsigned int)((unsigned int)(v_stack_m148))) != 260) {
        v_rdi = v_stack_m118;
        if (((unsigned int)((unsigned int)(v_stack_m148))) != 872) { v_rdi = v_stack_mB0; }
        v_stack_m118 = v_rdi;
    }
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a10 + 24))))) & (v_stack_mE4));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a10 + 24))))) goto loc_0089D938;
    if (((unsigned int)((unsigned int)(v_stack_m148))) != 280) goto loc_0089D156;
loc_0089CBB5:
    if (((unsigned int)((unsigned int)(v_stack_m148))) < 280) goto loc_0089D76A;
loc_0089CBC0:
    if (((unsigned int)((unsigned int)(v_stack_m148))) == 280) goto loc_0089D3BF;
    if ((*(unsigned __int16 *)(v_stack_p10)) == 0) goto loc_0089CC90;
    if (v_stack_m108 == 0) goto loc_0089D5B2;
loc_0089CBEB:
    a1 = (*(unsigned __int64 *)(v_stack_m108)) ^ (v_stack_m110);
    if (a1 >= 15) goto loc_0089D5B2;
    if (a1 != 15) goto loc_0089CBEB;
loc_0089CC0A:
    v_stack_m110 = 0;
    if (((unsigned int)((unsigned int)(v_stack_m148))) == 280) goto loc_0089CC74;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_p10 + 8)))) != 92) goto loc_0089CC90;
    if (((unsigned int)((unsigned int)(v_stack_m148))) == 872) goto loc_0089D146;
    v_stack_mA8 = 0;
    result = PsGetPermanentSiloContext(a9, (unsigned int)(*(unsigned int *)(v_rip + 7504945)), v_stack_mA8, a4);
    if (!sign_flag) goto loc_0089DC21;
    v_stack_mA8 = *(unsigned __int64 *)(v_rip + 6760974);
loc_0089CC5E:
    v_stack_m128 = *(unsigned __int64 *)(v_rip + 6760974);
    goto loc_0089C12D;
loc_0089CC67:
    result = ExfReleasePushLock((unsigned int)(v_stack_p18), (unsigned int)(*(unsigned int *)(v_rip + 7504945)), v_stack_mA8, a4);
    goto loc_0089C86B;
loc_0089CC74:
    if (((unsigned __int16)((unsigned int)(v_stack_p18))) == 92) goto loc_0089CC90;
loc_0089CC7A:
    goto loc_0089C8CB;
loc_0089CC83:
    result = ExfReleasePushLock(v_rdi, (unsigned int)(*(unsigned int *)(v_rip + 7504945)), *(unsigned __int64 *)(v_stack_p10 + 8), a4);
    goto loc_0089C6A4;
loc_0089CC90:
    v_stack_m148 = 0xC0000033ULL;
loc_0089CC98:
    result = ObpReleaseLookupContext(a11, (unsigned int)(*(unsigned int *)(v_rip + 7504945)), *(unsigned __int64 *)(v_stack_p10 + 8), a4);
loc_0089CCA0:
loc_0089CCA4:
    if (v_stack_m118 != 0) goto loc_0089DB3B;
loc_0089CCAD:
    if (v_stack_mB8 != 0) {
        result = ObDereferenceObjectDeferDelete(v_stack_mB8, (unsigned int)(*(unsigned int *)(v_rip + 7504945)), *(unsigned __int64 *)(v_stack_p10 + 8), a4);
    }
    result = SeClearLearningModeObjectInformation(v_stack_mB8, (unsigned int)(*(unsigned int *)(v_rip + 7504945)), *(unsigned __int64 *)(v_stack_p10 + 8), a4);
    if (v_stack_m110 == 0) goto loc_0089CCFB;
    if (v_stack_m108 == 0) goto loc_0089D7B2;
loc_0089CCDC:
    a1 = (*(unsigned __int64 *)(v_stack_m108)) ^ (v_stack_m110);
    if (a1 >= 15) goto loc_0089D7B2;
    if (a1 != 15) goto loc_0089CCDC;
loc_0089CCFB:
    if (sign_flag) goto loc_0089CD54;
    if (a12 == 0) goto loc_0089CD1B;
    if (((unsigned int)((unsigned int)(v_stack_mE4))) != -1) goto loc_0089DD98;
loc_0089CD1B:
    *(unsigned __int64 *)(a13) = v_stack_mB0;
    goto loc_0089DD9F;
loc_0089CD2A:
    if (((unsigned __int16)(a12)) == 6) goto loc_0089D2C7;
loc_0089CD34:
    result = (unsigned int)(v_stack_m148);
    if (v_stack_m128 == 0) {
        a1 = a9;
        result = OBP_GET_SILO_ROOT_DIRECTORY_FROM_SILO(a1, a12, v_stack_m110, a4);
        v_stack_m128 = result;
    }
    goto loc_0089CC7A;
loc_0089CD54:
    v_r13 = 0;
    goto loc_0089CD1B;
loc_0089CD59:
    if (!(condition_is_above_or_equal)) {
        a3 = (unsigned int)(v_stack_p18);
        a2 = v_stack_m118;
        a1 = (unsigned int)(v_stack_p18);
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (v_stack_m118 != 0) {
        *(unsigned __int8 *)(v_stack_m118 + 10) = 1;
    }
    if (v_stack_m118 != 0) goto loc_0089D6EE;
loc_0089CD90:
    result = KeAbPostRelease(*(unsigned __int64 *)(a11) + 296, a2, a3, a4);
    if ((*(unsigned __int8 *)(a11 + 22)) != 0) {
        a1 = *(unsigned __int64 *)(a11);
        a2 = 0x554C624FULL;
        result = ObDereferenceObjectDeferDeleteWithTag(a1, a2, a3, a4);
        *(unsigned __int8 *)(a11 + 22) = 0;
    }
    *(unsigned __int64 *)(a11) = 0;
    *(unsigned __int8 *)(a11 + 21) = (unsigned __int8)(v_stack_p10);
loc_0089CDC1:
    v_rsi = (unsigned int)((v_stack_mD8) >> (1));
    if (((unsigned int)(v_rsi)) < 4) goto loc_0089D082;
    v_rbx = 0;
loc_0089CDE0:
    if (((a11) & (*(unsigned __int64 *)(v_stack_mD0))) != 0) goto loc_0089D28A;
    v_rdi = (*(unsigned __int64 *)(v_stack_mD0)) & (a10);
loc_0089CDEF:
    v_r15 = (v_stack_mD0) + (8);
    result = (0) >> (1);
    result = (result) + (v_rdi);
    v_rsi = (unsigned int)((v_rsi) + (-4));
    v_rbx = (v_rbx + v_rbx * 2) + (result);
    if (((unsigned int)(v_rsi)) >= 4) goto loc_0089CDE0;
    v_r14 = (v_rbx) >> (32);
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(v_rbx)));
loc_0089CE1C:
    if ((unsigned int)(v_rsi) == 0) goto loc_0089CE4F;
loc_0089CE20:
    v_rsi = (unsigned int)((v_rsi) - 1);
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) >> (1));
    v_r14 = (unsigned int)((v_r14 + v_r14 * 2) + ((unsigned int)(a1)));
    if (((unsigned int)(*(unsigned __int16 *)(v_r15))) < 97) goto loc_0089CE48;
    if (((unsigned int)(*(unsigned __int16 *)(v_r15))) > 122) goto loc_0089D185;
    v_r14 = (unsigned int)((v_r14) + (-32));
loc_0089CE48:
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)(*(unsigned __int16 *)(v_r15))));
loc_0089CE4B:
    if ((unsigned int)(v_rsi) != 0) goto loc_0089CE20;
loc_0089CE4F:
    *(unsigned int *)(a11 + 16) = (unsigned int)(v_r14);
    a3 = (unsigned int)(((unsigned int)(v_stack_m120)) & (64));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) - ((unsigned int)(*(unsigned __int16 *)(v_r15))));
    v_stack_m128 = a3;
    result = (unsigned int)((result) >> (1));
    result = (unsigned int)((result) + ((unsigned int)(*(unsigned __int16 *)(v_r15))));
    result = (unsigned int)((result) >> (5));
    a1 = (unsigned int)((a1) * ((unsigned int)((unsigned __int8)(result))));
    result = (unsigned __int8)(((unsigned __int8)(v_r14)) - ((unsigned __int8)(a1)));
    *(unsigned __int8 *)(a11 + 20) = (unsigned __int8)((unsigned __int8)(result));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a11) + (unsigned __int8)(result) * 8) == 0) goto loc_0089CEC0;
loc_0089CEA0:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a11) + (unsigned __int8)(result) * 8) + 16)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a11 + 16))))) goto loc_0089CF41;
loc_0089CEAB:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a11) + (unsigned __int8)(result) * 8)) != 0) goto loc_0089CEA0;
loc_0089CEC0:
    result = 0;
    v_stack_m128 = 0;
    goto loc_0089D3CC;
loc_0089CECE:
    if ((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a11) + (unsigned __int8)(result) * 8)) != 0) goto loc_0089D5C4;
    *(unsigned __int64 *)(a11) = 0;
    *(unsigned __int8 *)(a11 + 21) = (unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a11) + (unsigned __int8)(result) * 8));
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_r13 + 296, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_r13 + 296;
        a3 = 0;
        a2 = 0;
        a1 = v_r13 + 296;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result == 0) goto loc_0089CDC1;
    *(unsigned __int8 *)(result + 10) = 1;
    goto loc_0089CDC1;
loc_0089CF41:
    a2 = (*(unsigned __int64 *)(a11 + 20 + 8)) - (48);
    result = (unsigned int)((*(unsigned __int8 *)(a2 + 26)) & (3));
    a2 = (a2) - (*(unsigned __int8 *)(result + v_rip - 9031500 * 1 + 15794048));
    result = PsGetCurrentServerSiloGlobals(v_rip - 9031500, a2, a3, a4);
    v_stack_mC8 = *(unsigned __int64 *)(result + 1200);
    if (((unsigned __int16)(v_stack_mD8)) != (*(unsigned __int16 *)(a2 + 8))) goto loc_0089CEAB;
    if (a3 == 0) goto loc_0089D278;
    result = RtlCompareMemory(v_stack_mD0, *(unsigned __int64 *)(a2 + 16), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_mD8)))), a4);
    if (result == ((unsigned int)((unsigned int)(v_stack_mD8)))) goto loc_0089CFDD;
    result = (result) >> (1);
    result = (result) + (result);
    a3 = (v_stack_mD0) + (result);
    v_r14 = (*(unsigned __int64 *)(a2 + 16)) + (result);
loc_0089CFC0:
    if (a3 >= ((unsigned int)((unsigned int)(v_stack_mD8)) + v_stack_mD0 * 1)) goto loc_0089CFDD;
    if (((unsigned __int16)(*(unsigned __int16 *)(a3))) != ((unsigned __int16)(*(unsigned __int16 *)(v_r14)))) goto loc_0089D04D;
loc_0089CFD3:
    a3 = (a3) + (2);
    v_r14 = (v_r14) + (2);
    goto loc_0089CFC0;
loc_0089CFDD:
    v_stack_m128 = *(unsigned __int64 *)(a11 + 20 + 8);
    *(unsigned __int64 *)(a11 + 8) = *(unsigned __int64 *)(*(unsigned __int64 *)(a11) + (unsigned __int8)(result) * 8);
    if (*(unsigned __int64 *)(a11 + 20 + 8) == 0) goto loc_0089D3CC;
loc_0089CFFD:
    if (v_stack_p8 == 0) goto loc_0089D1F5;
    if (v_stack_m128 == 0) goto loc_0089D3A3;
    if ((unsigned __int16)(v_stack_m138) == 0) goto loc_0089D330;
loc_0089D035:
    v_r15 = 0;
    goto loc_0089C5F5;
loc_0089D04D:
    if (((unsigned int)(v_stack_m138)) < 97) goto loc_0089D05E;
    if (((unsigned int)(v_stack_m138)) > 122) goto loc_0089D08A;
    a4 = (unsigned __int16)((v_stack_m138) - (32));
loc_0089D05E:
    if (((unsigned int)(v_stack_m136)) < 97) goto loc_0089D06F;
    if (((unsigned int)(v_stack_m136)) > 122) goto loc_0089D0C5;
    v_r10 = (unsigned __int16)((v_stack_m136) - (32));
loc_0089D06F:
    if (((unsigned __int16)(a4)) == ((unsigned __int16)(v_r10))) goto loc_0089CFD3;
loc_0089D079:
    goto loc_0089CEAB;
loc_0089D082:
    v_r14 = 0;
    goto loc_0089CE1C;
loc_0089D08A:
    if (v_stack_mC8 == 0) goto loc_0089D05E;
    if (((unsigned __int16)(a4)) < 192) goto loc_0089D05E;
    result = (a4) >> (8);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a4))) & (15));
    result = (unsigned int)(((unsigned int)((unsigned int)(a4))) >> (4));
    result = (unsigned int)((result) & (15));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_mC8 + result * 2)) + ((unsigned int)(result)));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_mC8 + a1 * 2)) + ((unsigned int)(a2)));
    a4 = (unsigned __int16)((a4) + (*(unsigned __int16 *)(v_stack_mC8 + a1 * 2)));
    goto loc_0089D05E;
loc_0089D0C5:
    if (v_stack_mC8 == 0) goto loc_0089D06F;
    if (((unsigned __int16)(v_r10)) < 192) goto loc_0089D06F;
    result = (v_r10) >> (8);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) & (15));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) >> (4));
    result = (unsigned int)((result) & (15));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_mC8 + result * 2)) + ((unsigned int)(result)));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_mC8 + a1 * 2)) + ((unsigned int)(a2)));
    v_r10 = (unsigned __int16)((v_r10) + (*(unsigned __int16 *)(v_stack_mC8 + a1 * 2)));
    goto loc_0089D06F;
loc_0089D103:
    if ((unsigned __int16)(a4) != 0) goto loc_0089C9A3;
    goto loc_0089D259;
loc_0089D112:
    a1 = (v_stack_m128 - 48) >> (8);
    a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(v_stack_m128 - 24)));
    a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(v_rip + 7511329)));
    if (((unsigned __int8)(a1)) == (*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 7510471) + 40))) goto loc_0089C093;
    result = ObfDereferenceObject(v_stack_m128, a2, (unsigned int)(v_stack_m128), a4);
loc_0089D13C:
    goto loc_0089DD9F;
loc_0089D146:
    v_stack_m128 = *(unsigned __int64 *)(v_rip + 6759707);
    goto loc_0089C12D;
loc_0089D156:
    if (((unsigned int)(a2)) == 260) goto loc_0089CBB5;
    if (((unsigned int)(a2)) == 872) goto loc_0089CBB5;
    goto loc_0089CA7A;
loc_0089D173:
    result = ObDereferenceDeviceMap(0, 1, (unsigned int)(v_stack_m128), a4);
    goto loc_0089C827;
loc_0089D185:
    result = RtlUpcaseUnicodeChar(1, 1, (unsigned int)(v_stack_m128), a4);
    v_r14 = (unsigned int)((v_r14) + ((unsigned int)((unsigned __int16)(result))));
    goto loc_0089CE4B;
loc_0089D198:
    v_stack_m158 = v_stack_mF0;
    v_stack_m160 = v_stack_mE8;
    v_stack_m168 = a7;
    v_stack_m170 = a6;
    v_stack_m178 = v_stack_m138;
    v_stack_m180 = *(unsigned __int64 *)(*(unsigned __int64 *)(a11) + (unsigned __int8)(result) * 8);
    if ((v_rip - 9031716) != (v_rip + 1444289)) goto loc_0089DCBF;
    v_stack_m188 = (unsigned int)((unsigned int)(v_stack_p18));
    result = IopParseFile(1, 1, (unsigned int)(v_stack_m128), a4);
    goto loc_0089C763;
loc_0089D1F5:
    if (v_stack_m128 == 0) goto loc_0089D3A3;
loc_0089D201:
    v_stack_m148 = (unsigned int)((unsigned int)(v_stack_mFC));
loc_0089D205:
loc_0089D209:
    if (!sign_flag) goto loc_0089CCA4;
    goto loc_0089CC98;
loc_0089D216:
    v_stack_m180 = v_stack_mFC;
    v_stack_m188 = (unsigned __int8)((unsigned int)(v_stack_mFC));
    result = ObpCheckTraverseAccess(v_stack_m128, (unsigned int)(v_stack_mFC), 1, a4);
    v_stack_p8 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) != 0) goto loc_0089DD24;
    if (!sign_flag) goto loc_0089DD17;
loc_0089D247:
    if (v_stack_m138 != 0) goto loc_0089D201;
    if (a8 == 0) goto loc_0089D201;
loc_0089D259:
    goto loc_0089C9A6;
loc_0089D261:
    v_stack_m128 = *(unsigned __int64 *)(v_rip + 6759424);
    goto loc_0089C12D;
loc_0089D278:
    result = memcmp(v_stack_m128, (unsigned int)(v_stack_mFC), 1, a4);
    if ((unsigned int)(result) == 0) goto loc_0089CFDD;
    goto loc_0089D079;
loc_0089D28A:
loc_0089D290:
    if (((unsigned int)((unsigned __int16)(v_stack_m118))) < 97) goto loc_0089D2A8;
    if (((unsigned int)((unsigned __int16)(v_stack_m118))) <= 122) goto loc_0089D2C2;
    result = RtlUpcaseUnicodeChar((unsigned __int16)((unsigned __int16)(v_stack_m118)), (unsigned int)(v_stack_mFC), 1, a4);
loc_0089D2A8:
    v_r14 = (4) - (1);
    if (condition_is_not_equal) goto loc_0089D290;
    goto loc_0089CDEF;
loc_0089D2C2:
    result = (unsigned int)(((unsigned __int16)(result)) + (-32));
    goto loc_0089D2A8;
loc_0089D2C7:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(1 + 8)))) - (0x3F005CULL));
    result = *(unsigned __int64 *)(1 + 8);
    if (!(condition_is_not_equal)) {
        a1 = *(unsigned __int16 *)(*(unsigned __int64 *)(1 + 8) + 4);
        result = (unsigned __int16)(v_r10);
        a1 = (unsigned int)((a1) - ((unsigned int)(result)));
    }
    if ((unsigned int)(a1) != 0) goto loc_0089CD34;
    result = ObpReferenceCurrentDeviceMap((unsigned int)((unsigned int)(v_r14)), v_stack_m108, 1, a4);
    v_stack_m110 = result;
    if (result == 0) goto loc_0089CD34;
    if (*(unsigned __int64 *)(result) == 0) goto loc_0089CD34;
    a2 = 0;
    result = ObReferenceObjectByPointer(*(unsigned __int64 *)(result), a2, v_stack_p20, a5);
    v_stack_m148 = (unsigned int)(result);
    goto loc_0089D209;
loc_0089D330:
    result = (*(unsigned __int64 *)(result) - 48) >> (8);
    a2 = ((unsigned __int8)(result)) ^ (*(unsigned __int8 *)(*(unsigned __int64 *)(result) - 24));
    a2 = (a2) ^ (*(unsigned __int8 *)(v_rip + 7510786));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_p18) + a2 * 8 + 16545792) + 144) == 0) goto loc_0089D37F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)((unsigned int)(v_stack_p18) + a2 * 8 + 16545792) + 144)) == (v_rip + 90712)) goto loc_0089D035;
    if (a8 == 0) goto loc_0089D035;
loc_0089D37F:
    a2 = 0;
    result = ObReferenceObjectByPointer(*(unsigned __int64 *)(result), a2, v_stack_p20, a5);
    v_stack_m148 = (unsigned int)(result);
    goto loc_0089D205;
loc_0089D3A3:
    if (v_stack_m138 != 0) goto loc_0089D75D;
    if (a8 != 0) goto loc_0089D7D1;
loc_0089D3BF:
    v_stack_m148 = 0xC0000034ULL;
    goto loc_0089CC98;
loc_0089D3CC:
    if ((((unsigned __int8)((unsigned int)(v_stack_m120))) & (1)) == 0) goto loc_0089CFFD;
loc_0089D3E0:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a11) + 336)))) & (4)) != 0) goto loc_0089D411;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(a11) + 304) == 0) goto loc_0089CFFD;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a11) + 304)) != v_stack_m110) goto loc_0089D4FC;
    goto loc_0089D432;
loc_0089D411:
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(a11) + 304))) & (16)) != 0) goto loc_0089DD2F;
loc_0089D419:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m110 + 8) + 336)))) & (16)) != 0) goto loc_0089DD5F;
loc_0089D428:
loc_0089D42F:
loc_0089D432:
    v_stack_mC8 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m110 + 8) + 312);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m110 + 8) + 312) == 0) goto loc_0089CFFD;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m110 + 8) + 312) + 296, a2, a2 + 1, a5);
    result = 0;
    if (condition_is_not_equal) goto loc_0089DB16;
loc_0089D470:
    if (0 != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a1 = 0;
    if (condition_is_not_equal) goto loc_0089DAE7;
loc_0089D491:
    result = KeAbPostRelease(*(unsigned __int64 *)(a11) + 296, a2, a2 + 1, a5);
    result = 0;
loc_0089D49F:
    *(unsigned __int8 *)(a11 + 22) = 0;
    if ((unsigned __int8)(*(unsigned __int8 *)(a11 + 22)) != 0) goto loc_0089DD6E;
loc_0089D4AD:
    a3 = (unsigned int)(((unsigned int)(v_stack_m120)) & (64));
    *(unsigned __int64 *)(a11) = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m110 + 8) + 312);
    v_stack_m128 = a3;
    v_r14 = (*(unsigned __int8 *)((unsigned int)(v_stack_p18)) * 8) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m110 + 8) + 312));
    if (*(unsigned __int64 *)(v_r14) == 0) goto loc_0089D4ED;
loc_0089D4D3:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_r14) + 16)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 90712))))) goto loc_0089D960;
loc_0089D4DE:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_r14)) != 0) goto loc_0089D4D3;
loc_0089D4ED:
    result = 0;
    v_stack_m128 = 0;
    goto loc_0089D3E0;
loc_0089D4FC:
    result = PsGetCurrentServerSiloGlobals(*(unsigned __int64 *)(a11) + 296, a2, a3, a5);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 120, a2, a3, a5);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = result + 120;
        a3 = 0;
        a2 = 0;
        a1 = result + 120;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
        a1 = 17;
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rsi = *(unsigned __int64 *)(*(unsigned __int64 *)(v_r14));
    if (*(unsigned __int64 *)(v_stack_mC8 + 304) != 0) {
        v_rsi = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mC8 + 304) + 8);
    }
    a1 = 0;
    result = a1;
    if (!(condition_is_equal)) {
        a1 = result + 120;
        result = ExfReleasePushLockShared(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(result + 120, a2, a3, a4);
    result = KeLeaveGuardedRegion(result + 120, a2, a3, a4);
    goto loc_0089D42F;
loc_0089D589:
    result = (result) >> (32);
    if ((unsigned int)(result) != 0) goto loc_0089C242;
    result = ObfDereferenceObjectWithTag(v_rsi, (unsigned int)(0x746C6644ULL), a3, a4);
loc_0089D5A5:
    result = PsGetServerSiloGlobals(v_stack_mC8, (unsigned int)(0x746C6644ULL), a3, a4);
    goto loc_0089C28C;
loc_0089D5B2:
    result = ObDereferenceDeviceMap(a3, 1, a3, a4);
    goto loc_0089CC0A;
loc_0089D5C4:
    result = ObpLockDirectoryExclusive(a11, v_stack_mC8, a3, a4);
    goto loc_0089CDC1;
loc_0089D5D4:
    a1 = (v_stack_mC8 - 48) >> (8);
    a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(v_stack_mC8 - 24)));
    a1 = (unsigned __int8)((a1) ^ (*(unsigned __int8 *)(v_rip + 7510111)));
    if (((unsigned __int8)(a1)) != (*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 6758517) + 40))) goto loc_0089C093;
    a2 = 0;
    result = ObReferenceObjectByPointer(v_stack_mC8, a2, v_stack_p20, a5);
    v_stack_m148 = (unsigned int)(result);
    v_r15 = 1;
    if (!sign_flag) { v_r15 = v_stack_mC8; }
    result = ObfDereferenceObject(v_stack_mC8, a2, v_stack_p20, a5);
    *(unsigned __int64 *)(a13) = v_r15;
    goto loc_0089DD9F;
loc_0089D634:
    result = PsGetServerSiloGlobals(*(unsigned __int64 *)(result + 16), a2, v_stack_p20, a5);
    a3 = 0;
    v_rdi = (result) + (120);
    a2 = 0;
    result = KeAbPreAcquire(v_rdi, a2, a3, a5);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_rdi;
        a3 = 0;
        a2 = 0;
        a1 = v_rdi;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    result = ObFastReferenceObjectLocked((unsigned int)(v_stack_p18), (unsigned int)(0x554C624FULL), a3, a4);
    a1 = 0;
    if (condition_is_not_equal) goto loc_0089DC9E;
loc_0089D6AE:
    result = KeAbPostRelease(v_rdi, (unsigned int)(0x554C624FULL), a3, a4);
    result = KeLeaveGuardedRegion(v_rdi, (unsigned int)(0x554C624FULL), a3, a4);
    if (result != 0) goto loc_0089C45C;
loc_0089D6C4:
    if (*(unsigned __int64 *)(result + 24) != 0) goto loc_0089C3FD;
    v_r15 = 0;
    goto loc_0089C5DF;
loc_0089D6EE:
    result = ExfReleasePushLockShared((unsigned int)(v_stack_p18) + 296, (unsigned int)(0x554C624FULL), v_stack_m130, v_stack_m138);
    goto loc_0089CD90;
loc_0089D6FF:
    v_stack_m160 = v_stack_mF0;
    v_stack_m168 = a7;
    v_stack_m170 = a6;
    v_stack_m178 = v_stack_m138;
    v_stack_m180 = result;
    if (((unsigned int)(v_stack_p18)) != (v_rip + 425203)) goto loc_0089DD81;
    v_stack_m188 = (unsigned int)((unsigned int)(v_stack_p18));
    result = ExpWin32ParseProcedure((unsigned int)(v_stack_p18) + 296, (unsigned int)(0x554C624FULL), a10, v_stack_m138);
    goto loc_0089C763;
loc_0089D75D:
    v_stack_m148 = 0xC000003AULL;
    goto loc_0089CC98;
loc_0089D76A:
    if (((unsigned int)((unsigned int)(0x554C624FULL))) == 872) goto loc_0089CBC0;
loc_0089D776:
    v_stack_m148 = 0xC000050BULL;
    goto loc_0089CC98;
loc_0089D783:
    if (((unsigned int)((unsigned int)(0x554C624FULL))) == 872) goto loc_0089C7D8;
    goto loc_0089D776;
loc_0089D791:
    if (0 != 0) goto loc_0089C35A;
    v_r15 = 0;
    v_stack_m108 = 0;
    result = ObpSetCurrentProcessDeviceMap((unsigned int)(v_stack_p18) + 296, (unsigned int)(0x554C624FULL), a10, v_stack_m138);
    v_stack_m110 = result;
    goto loc_0089C35D;
loc_0089D7B2:
    result = ObDereferenceDeviceMap(a10, 1, a10, v_stack_m138);
    goto loc_0089CCFB;
loc_0089D7C4:
    result = ExfReleasePushLockShared(v_rdi, 1, a10, v_stack_m138);
    goto loc_0089C344;
loc_0089D7D1:
    a2 = 4;
    if (v_stack_p20 == (*(unsigned __int64 *)(v_rip + 6757997))) { a2 = 8; }
    v_stack_m178 = v_stack_m148;
    v_stack_m180 = (unsigned __int8)((unsigned int)(v_stack_m144));
    v_stack_m188 = 0;
    result = ObCheckCreateObjectAccess(v_stack_mC0, a2, a10, v_stack_mD8);
    if ((unsigned __int8)(result) == 0) goto loc_0089DB48;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mC0 + 340)))) != -1) goto loc_0089D8E0;
loc_0089D832:
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)(v_stack_mD8)), (unsigned int)(0x6D4E624FULL), v_stack_mD8);
    if (result == 0) goto loc_0089D94C;
    result = ObpInsertDirectoryEntry(v_stack_mC0, result, a11, v_stack_mD8);
    if ((unsigned __int8)(result) == 0) goto loc_0089D945;
    result = memcpy(result, v_stack_mD0, (unsigned int)((unsigned int)(v_stack_mD8)), v_stack_mD8);
    result = (unsigned int)((*(unsigned __int8 *)(result - 22)) & (3));
    v_rbx = (result - 48) - (*(unsigned __int8 *)(result + v_rip - 9033868 * 1 + 15794048));
    result = *(unsigned __int8 *)(result + v_rip - 9033868 * 1 + 15794048);
    if (*(unsigned __int64 *)(v_rbx + 16) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rbx + 16), a2, (unsigned int)((unsigned int)(v_stack_mD8)), v_stack_mD8);
    }
    *(unsigned __int16 *)(v_rbx + 8) = (unsigned __int16)(v_stack_mD8);
    *(unsigned __int16 *)(v_rbx + 10) = (unsigned __int16)(v_stack_mD8);
    *(unsigned __int64 *)(v_rbx + 16) = result;
    v_stack_m148 = 0;
    goto loc_0089CCA0;
loc_0089D8C7:
    v_stack_m148 = 0xC0000024ULL;
    goto loc_0089CC98;
loc_0089D8D4:
    goto loc_0089C59C;
loc_0089D8E0:
    if (v_stack_p20 == (*(unsigned __int64 *)(v_rip + 7508721))) goto loc_0089D8F6;
    if (v_stack_p20 != (*(unsigned __int64 *)(v_rip + 6757736))) goto loc_0089D832;
loc_0089D8F6:
    result = PsGetCurrentProcessSessionId(14, a2, (unsigned int)((unsigned int)(v_stack_mD8)), v_stack_mD8);
    if (((unsigned int)(v_rbx)) == ((unsigned int)(result))) goto loc_0089D832;
    result = SeSinglePrivilegeCheck(*(unsigned __int64 *)(v_rip + 7586702), (unsigned __int8)(result), (unsigned int)((unsigned int)(v_stack_mD8)), v_stack_mD8);
    if ((unsigned __int8)(result) != 0) goto loc_0089D832;
    a2 = (unsigned int)(((unsigned int)(v_stack_p18)) >> (6));
    a2 = (unsigned __int8)((a2) & (1));
    result = ObpIsUnsecureName(v_stack_mD8, a2, (unsigned int)((unsigned int)(v_stack_mD8)), v_stack_mD8);
    if ((unsigned __int8)(result) != 0) goto loc_0089D832;
loc_0089D938:
    v_stack_m148 = 0xC0000022ULL;
    goto loc_0089CC98;
loc_0089D945:
    a2 = 0;
    result = ExFreePoolWithTag(v_stack_mD8, a2, (unsigned int)((unsigned int)(v_stack_mD8)), v_stack_mD8);
loc_0089D94C:
    v_stack_m148 = 0xC000009AULL;
    goto loc_0089CC98;
loc_0089D959:
    v_rsi = 0;
    goto loc_0089C21F;
loc_0089D960:
    a2 = (*(unsigned __int64 *)(v_rsi + 8)) - (48);
    result = (unsigned int)((*(unsigned __int8 *)(a2 + 26)) & (3));
    a2 = (a2) - (*(unsigned __int8 *)(result + v_rip - 9034091 * 1 + 15794048));
    result = PsGetCurrentServerSiloGlobals(v_rip - 9034091, a2, (unsigned int)((unsigned int)(v_stack_mD8)), v_stack_mD8);
    v_stack_mF8 = *(unsigned __int64 *)(result + 1200);
    if (((unsigned int)(v_stack_mD8)) != ((unsigned int)(*(unsigned __int16 *)(a2 + 8)))) goto loc_0089D4DE;
    v_stack_m88 = v_stack_mD0 + (unsigned int)((unsigned int)(v_stack_mD8)) * 1;
    if ((unsigned int)((unsigned int)((unsigned int)(v_stack_mD8))) == 0) goto loc_0089DAD5;
    result = RtlCompareMemory(v_stack_mD0, *(unsigned __int64 *)(a2 + 16), (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_mD8)))), v_stack_mD8);
    if (result == ((unsigned int)((unsigned int)(v_stack_mD8)))) goto loc_0089DA02;
    result = (result) >> (1);
    result = (result) + (result);
    a3 = (v_stack_mD0) + (result);
    v_r15 = (*(unsigned __int64 *)(a2 + 16)) + (result);
loc_0089D9E5:
    if (a3 >= v_stack_m88) goto loc_0089DA02;
    if (((unsigned __int16)(*(unsigned __int16 *)(a3))) != ((unsigned __int16)(*(unsigned __int16 *)(v_r15)))) goto loc_0089DA25;
loc_0089D9F8:
    a3 = (a3) + (2);
    v_r15 = (v_r15) + (2);
    goto loc_0089D9E5;
loc_0089DA02:
    v_stack_m128 = *(unsigned __int64 *)(v_rsi + 8);
    *(unsigned __int64 *)(a11 + 8) = result;
    if (*(unsigned __int64 *)(v_rsi + 8) != 0) goto loc_0089CFFD;
    goto loc_0089D3E0;
loc_0089DA25:
    if (((unsigned int)(*(unsigned __int16 *)(a3))) < 97) goto loc_0089DA36;
    if (((unsigned int)(*(unsigned __int16 *)(a3))) > 122) goto loc_0089DA56;
    a4 = (unsigned __int16)((*(unsigned __int16 *)(a3)) - (32));
loc_0089DA36:
    if (((unsigned int)(*(unsigned __int16 *)(v_r15))) < 97) goto loc_0089DA47;
    if (((unsigned int)(*(unsigned __int16 *)(v_r15))) > 122) goto loc_0089DA94;
    v_r10 = (unsigned __int16)((*(unsigned __int16 *)(v_r15)) - (32));
loc_0089DA47:
    if (((unsigned __int16)(a4)) == ((unsigned __int16)(v_r10))) goto loc_0089D9F8;
loc_0089DA4D:
    goto loc_0089D4DE;
loc_0089DA56:
    if (v_stack_mC8 == 0) goto loc_0089DA36;
    if (((unsigned __int16)(a4)) < 192) goto loc_0089DA36;
    result = (a4) >> (8);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(a4))) & (15));
    result = (unsigned int)(((unsigned int)((unsigned int)(a4))) >> (4));
    result = (unsigned int)((result) & (15));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_mC8 + result * 2)) + ((unsigned int)(result)));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_mC8 + a1 * 2)) + ((unsigned int)(a2)));
    a4 = (unsigned __int16)((a4) + (*(unsigned __int16 *)(v_stack_mC8 + a1 * 2)));
    goto loc_0089DA36;
loc_0089DA94:
    if (v_stack_mC8 == 0) goto loc_0089DA47;
    if (((unsigned __int16)(v_r10)) < 192) goto loc_0089DA47;
    result = (v_r10) >> (8);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) & (15));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) >> (4));
    result = (unsigned int)((result) & (15));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_mC8 + result * 2)) + ((unsigned int)(result)));
    a1 = (unsigned int)((*(unsigned __int16 *)(v_stack_mC8 + a1 * 2)) + ((unsigned int)(a2)));
    v_r10 = (unsigned __int16)((v_r10) + (*(unsigned __int16 *)(v_stack_mC8 + a1 * 2)));
    goto loc_0089DA47;
loc_0089DAD5:
    result = memcmp(a1, a2, (unsigned int)(v_stack_m128), a4);
    if ((unsigned int)(result) == 0) goto loc_0089DA02;
    goto loc_0089DA4D;
loc_0089DAE7:
    result = ExfReleasePushLockShared(v_rsi + 296, a2, (unsigned int)(v_stack_m128), a4);
    goto loc_0089D491;
loc_0089DAF8:
    result = ObfDereferenceObjectWithTag(v_stack_mC8, (unsigned int)(0x554C624FULL), (unsigned int)(v_stack_m128), a4);
    goto loc_0089CB68;
loc_0089DB0A:
    goto loc_0089C013;
loc_0089DB16:
    a2 = 0;
    result = ExfTryAcquirePushLockSharedEx(v_stack_mC8 + 296, a2, (unsigned int)(v_stack_m128), a4);
    if ((unsigned __int8)(result) == 0) goto loc_0089DB8E;
    goto loc_0089D470;
loc_0089DB32:
    goto loc_0089C122;
loc_0089DB3B:
    result = ObDereferenceObjectDeferDelete(result, a2, (unsigned int)(v_stack_m128), a4);
    goto loc_0089CCAD;
loc_0089DB48:
    if (sign_flag) goto loc_0089D205;
    goto loc_0089D201;
loc_0089DB5E:
    a2 = 0;
    result = ObReferenceObjectByPointer(a8, a2, v_stack_p20, a5);
    if (sign_flag) goto loc_0089DD9F;
    *(unsigned __int64 *)(a13) = a8;
    goto loc_0089DD9F;
loc_0089DB8E:
    if (0 != 0) goto loc_0089DCAB;
loc_0089DB97:
    result = ObfReferenceObjectWithTag(v_stack_mC8, (unsigned int)(0x554C624FULL), v_stack_p20, a5);
    a1 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        a1 = *(unsigned __int64 *)(a11) + 296;
        result = ExfReleasePushLockShared(a1, (unsigned int)(0x554C624FULL), v_stack_p20, a5);
    }
    result = KeAbPostRelease(*(unsigned __int64 *)(a11) + 296, (unsigned int)(0x554C624FULL), v_stack_p20, a5);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_stack_mC8 + 296, a2, a3, a5);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = v_stack_mC8 + 296;
        a3 = 0;
        a2 = 0;
        a1 = v_stack_mC8 + 296;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    goto loc_0089D49F;
loc_0089DC21:
    goto loc_0089CC5E;
loc_0089DC2A:
    a2 = 0;
    result = ObReferenceObjectByPointer(v_stack_mC8, a2, v_stack_p20, a5);
    if (sign_flag) goto loc_0089DD9F;
    *(unsigned __int64 *)(a13) = v_stack_mC8;
    goto loc_0089DD9F;
loc_0089DC5A:
    result = ObDereferenceDeviceMap(result, 14, v_stack_p20, a5);
    goto loc_0089C334;
loc_0089DC6C:
    a2 = (unsigned int)(((unsigned int)(v_stack_mE4)) & ((unsigned int)(result)));
    v_stack_mE4 = (unsigned int)(a2);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a10 + 24))))) & ((unsigned int)(a2)));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a10 + 24))))) goto loc_0089C077;
    result = ObfDereferenceObject(v_stack_mB8, a2, a10, a5);
    goto loc_0089DD9F;
loc_0089DC9E:
    result = ExfReleasePushLockShared(result, a2, a10, a5);
    goto loc_0089D6AE;
loc_0089DCAB:
    result = KeAbPostReleaseEx(v_stack_mC8 + 296, *(unsigned __int64 *)(a11), a10, a5);
    goto loc_0089DB97;
loc_0089DCBF:
    v_stack_m188 = (unsigned int)((unsigned int)(v_stack_p18));
    result = guard_dispatch_icall(v_stack_mC8 + 296, *(unsigned __int64 *)(a11), a10, a5);
loc_0089DCD1:
    goto loc_0089C763;
loc_0089DCDC:
    result = (v_stack_p20) + (16);
    v_stack_m68 = *(unsigned __int64 *)(a11);
    v_stack_m70 = result;
    v_stack_m60 = (unsigned int)(v_stack_p18);
    result = SeSetLearningModeObjectInformation(v_stack_m80, *(unsigned __int64 *)(a11), a10, a5);
    goto loc_0089C8DE;
loc_0089DD17:
    v_stack_mFC = (unsigned int)((unsigned int)(0xC0000034ULL));
    goto loc_0089D247;
loc_0089DD24:
    goto loc_0089C995;
loc_0089DD2F:
    if ((((unsigned __int8)(result)) & (6)) != 0) goto loc_0089D419;
    a1 = (a10) + (32);
    result = RtlIsSandboxedToken(a1, v_stack_m144, v_stack_m130, v_stack_m138);
    v_r14 = (unsigned int)((result) | (2));
loc_0089DD5F:
    if ((((unsigned __int8)(v_r14)) & (2)) == 0) goto loc_0089D42F;
    goto loc_0089D428;
loc_0089DD6E:
    result = ObDereferenceObjectDeferDeleteWithTag(*(unsigned __int64 *)(a11), (unsigned int)(0x554C624FULL), v_stack_m130, v_stack_m138);
    goto loc_0089D4AD;
loc_0089DD81:
    v_stack_m188 = (unsigned int)((unsigned int)(v_stack_p18));
    result = guard_dispatch_icall(*(unsigned __int64 *)(a11), (unsigned int)(0x554C624FULL), v_stack_m130, v_stack_m138);
    goto loc_0089DCD1;
loc_0089DD98:
    *(unsigned int *)((unsigned int)(0x554C624FULL)) = (unsigned int)(*(unsigned __int64 *)(a11));
    goto loc_0089CD1B;
loc_0089DD9F:
    v_rsp = (v_rsp) + (360);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ObpLookupObjectName(int64_t Arg1, void *Arg2, int32_t Arg3, void *Arg4, uint8_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8, int64_t Arg9, void *Arg10, void *Arg11, int64_t Arg12, void *Arg13)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg4 = (uint8_t *)Arg4;
    uint8_t *arg10 = (uint8_t *)Arg10;
    uint8_t *arg11 = (uint8_t *)Arg11;
    uint8_t *arg13 = (uint8_t *)Arg13;

    int64_t result;
    int64_t local_r10;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m100;
    uint64_t v_stack_m108;
    uint64_t v_stack_m110;
    uint64_t v_stack_m118;
    uint32_t v_stack_m120;
    uint64_t v_stack_m128;
    uint64_t v_stack_m130;
    uint16_t v_stack_m136;
    uint64_t v_stack_m138;
    uint32_t v_stack_m144;
    uint32_t v_stack_m148;
    uint64_t v_stack_m158;
    uint64_t v_stack_m160;
    uint64_t v_stack_m168;
    uint64_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m180;
    uint32_t v_stack_m188;
    uint64_t v_stack_m50;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint32_t v_stack_m94;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint64_t v_stack_mB0;
    uint64_t v_stack_mB8;
    uint64_t v_stack_mC0;
    uint64_t v_stack_mC8;
    uint64_t v_stack_mD0;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE4;
    uint16_t v_stack_mE6;
    uint16_t v_stack_mE8;
    uint64_t v_stack_mF0;
    uint64_t v_stack_mF8;
    uint32_t v_stack_mFC;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p40;
    uint8_t v_stack_p8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (360);
    local_r15 = 0;
    result = 0;
    v_stack_mB8 = 0;
    v_stack_m50 = 0;
    v_stack_mE6 = 0;
    *(uint64_t *)(arg11) = v_xmm1;
    *(uint64_t *)(arg11 + 0x10) = 0;
    v_stack_m98 = 0;
    v_stack_m110 = 0;
    v_stack_m108 = 0;
    v_stack_m100 = 64;
    v_stack_m80 = v_xmm0;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m138 = v_xmm0;
    if (Arg12 != 0) {
        *(uint32_t *)(Arg12) = 0;
    }
    v_stack_m148 = 0;
    v_stack_mFC = 0;
    *(uint64_t *)(arg13) = 0;
    v_stack_mE8 = 16;
    v_stack_p8 = 1;
    v_stack_m118 = 0;
    v_stack_m128 = 0;
    v_stack_mE4 = 0xFFFFFFFFULL;
    v_stack_mE0 = Arg9;
    if ((*(uint32_t *)(v_rip + 0x56F44E)) == 0) goto loc_0089BF93;
    if (((*(uint8_t *)(arg4 + 0x42)) & (1)) == 0) goto loc_0089BF93;
    local_r14 = (uint32_t)(Arg3);
    if (!(condition_is_below)) {
        local_r14 = (uint32_t)(((uint32_t)(Arg3)) | (64));
        v_stack_p18 = (uint32_t)(local_r14);
    }
    Arg1 = 1;
    if (condition_is_above_or_equal) { Arg1 = Arg5; }
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (64));
    v_stack_m144 = (uint32_t)(Arg1);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(result))) | (1));
    if (Arg8 != 0) { Arg1 = (uint32_t)(result); }
    v_stack_m120 = (uint32_t)(Arg1);
    if (Arg1 != 0) goto loc_0089C030;
    if ((uint16_t)(*(uint16_t *)(arg2)) == 0) goto loc_0089D13C;
    if ((*(uint16_t *)(*(uint64_t *)(arg2 + 0x8))) != 92) goto loc_0089D13C;
    if (((uint16_t)(*(uint16_t *)(arg2))) != 2) goto loc_0089C0BB;
    v_stack_p40 = 0;
    result = PsGetPermanentSiloContext(Arg9, (uint32_t)(*(uint32_t *)(v_rip + 0x72907A)), Arg8, Arg4);
    if (!sign_flag) goto loc_0089DB0A;
loc_0089C013:
    if (*(uint64_t *)(v_rip + 0x673655) != 0) goto loc_0089DB5E;
    if (Arg8 != 0) goto loc_0089DC2A;
    goto loc_0089DD9F;
loc_0089C030:
    v_stack_m170 = v_stack_m98;
    Arg3 = 0;
    v_stack_m178 = 0;
    v_stack_m180 = v_stack_mB8;
    Arg2 = 0;
    v_stack_m188 = 0x746C6644ULL;
    result = ObpReferenceObjectByHandleWithTag(*(uint64_t *)(v_rip + 0x673655), Arg2, Arg3, (uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x72907A))));
    v_stack_m148 = (uint32_t)(result);
    if (sign_flag) goto loc_0089DD9F;
    if ((uint32_t)((uint32_t)(v_stack_m94)) != 0) goto loc_0089DC6C;
loc_0089C077:
    if ((*(uint16_t *)(arg2)) == 0) goto loc_0089D5D4;
    if ((*(uint16_t *)(*(uint64_t *)(arg2 + 0x8))) == 92) goto loc_0089D112;
loc_0089C093:
    v_stack_m138 = v_xmm1;
    if ((*(uint32_t *)(v_rip + 0x73DA3E)) != 0) goto loc_0089DCDC;
    goto loc_0089C8D3;
loc_0089C0BB:
    if ((*(uint32_t *)(v_rip + 0x73DA16)) == 0) goto loc_0089C134;
    v_stack_m68 = 0;
    v_stack_m70 = (uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x72907A))) + 16;
    v_stack_m60 = 0;
    result = SeSetLearningModeObjectInformation(v_stack_m80, Arg2, Arg3, (uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x72907A))));
    goto loc_0089C12D;
loc_0089C0DF:
    if (((uint16_t)(v_stack_m80)) != 92) goto loc_0089CC90;
    if (0 == 872) goto loc_0089D261;
    v_stack_mA0 = 0;
    result = PsGetPermanentSiloContext(Arg9, (uint32_t)(*(uint32_t *)(v_rip + 0x728F6D)), v_stack_mA0, (uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x72907A))));
    if (!sign_flag) goto loc_0089DB32;
    v_stack_mA0 = *(uint64_t *)(v_rip + 0x67354A);
loc_0089C122:
    v_stack_m128 = *(uint64_t *)(v_rip + 0x67354A);
loc_0089C12D:
loc_0089C134:
    if (((uint16_t)(*(uint16_t *)(arg2))) < 8) goto loc_0089CD2A;
    if ((*(uint64_t *)(*(uint64_t *)(arg2 + 0x8))) != v_stack_mA0) goto loc_0089CD2A;
    if (v_stack_p20 == (*(uint64_t *)(v_rip + 0x72A97B))) goto loc_0089C502;
loc_0089C16B:
    v_stack_m110 = 0;
    v_stack_m108 = 0;
    result = PsGetProcessServerSilo(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220), *(uint16_t *)(arg2), v_stack_mA0, v_stack_p20);
    result = PsGetThreadServerSilo(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint16_t *)(arg2), v_stack_mA0, v_stack_p20);
    local_r14 = (result != result) ? 1 : 0;
    Arg1 = ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (8)) != 0) ? 1 : 0;
    result = (condition_is_above_or_equal) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_0089C27C;
    if (result != result) goto loc_0089C27C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (8)) == 0) goto loc_0089C27C;
    result = PspLockThreadSecurityShared(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(gs_base + (0 + 0x188)), v_stack_mA0, v_stack_p20);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (8)) == 0) goto loc_0089D959;
    local_rsi = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x648);
    if (*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x648) == 0) {
        local_rsi = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x538);
        local_rsi = (local_rsi) & (-8);
    }
    result = ObfReferenceObjectWithTag(local_rsi, (uint32_t)(0x746C6644ULL), v_stack_mA0, v_stack_p20);
loc_0089C21F:
    result = PspUnlockThreadSecurityShared(*(uint64_t *)(gs_base + (0 + 0x188)), *(uint64_t *)(gs_base + (0 + 0x188)), v_stack_mA0, v_stack_p20);
    if (local_rsi == 0) goto loc_0089C27C;
    if (((uint32_t)(*(uint64_t *)(local_rsi + 0x18))) == 999) goto loc_0089D589;
loc_0089C242:
    v_stack_m90 = 0;
    result = SeGetTokenDeviceMap(local_rsi, v_stack_m90, v_stack_mA0, v_stack_p20);
    if (!(sign_flag)) {
        Arg3 = v_stack_m90;
        v_stack_m110 = Arg3;
    }
    result = ObfDereferenceObjectWithTag(local_rsi, (uint32_t)(0x746C6644ULL), Arg3, v_stack_p20);
    if (v_stack_m110 != 0) goto loc_0089C35A;
loc_0089C27C:
    if ((uint8_t)((uint8_t)(local_r14)) != 0) goto loc_0089D5A5;
loc_0089C28C:
    v_stack_m108 = *(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 792;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x318))) & (15)) == 0) goto loc_0089C2B7;
loc_0089C29E:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x318))) & (15)) == 0) goto loc_0089C2B7;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x318))) & (15)) != 0) goto loc_0089C29E;
loc_0089C2B7:
    local_r14 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x318)) & (-16);
    v_stack_m110 = local_r14;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x318))) & (15)) != 0) goto loc_0089C351;
    result = PsGetCurrentServerSiloGlobals(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x318) - 1, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x220) + 0x318), v_stack_m108, v_stack_p20);
    Arg3 = 0;
    local_rdi = (result) + (120);
    Arg2 = 0;
    result = KeAbPreAcquire(local_rdi, Arg2, Arg3, v_stack_p20);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = local_rdi;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = local_rdi;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_r14 = (*(uint64_t *)(v_stack_m108)) & (-16);
    v_stack_m110 = local_r14;
    if (condition_is_not_equal) goto loc_0089C585;
loc_0089C334:
    Arg1 = 0;
    if (condition_is_not_equal) goto loc_0089D7C4;
loc_0089C344:
    result = KeAbPostRelease(local_rdi, Arg2, Arg3, Arg4);
    result = KeLeaveGuardedRegion(local_rdi, Arg2, Arg3, Arg4);
loc_0089C351:
    if (local_r14 == 0) goto loc_0089D791;
loc_0089C35A:
    local_r15 = 0;
loc_0089C35D:
    if (local_r14 == 0) goto loc_0089CD34;
    if ((*(uint64_t *)(local_r14)) == 0) goto loc_0089CD34;
    result = (uint16_t)((*(uint16_t *)(v_stack_p10)) - (8));
    local_r10 = (uint16_t)((*(uint16_t *)(v_stack_p10 + 0x2)) - (8));
    v_stack_m130 = *(uint64_t *)(v_stack_p10 + 0x8) + 8;
    v_stack_m138 = (uint16_t)(result);
    v_stack_m136 = (uint16_t)(local_r10);
    if (v_stack_p20 != (*(uint64_t *)(v_rip + 0x72A746))) goto loc_0089C5DF;
    if (((v_stack_m120) & (1)) == 0) goto loc_0089C5DF;
    if (((uint16_t)(result)) < 6) goto loc_0089C5DF;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_p10 + 0x8) + 0xA)) != 58) goto loc_0089C5DF;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_p10 + 0x8) + 0xC)) != 92) goto loc_0089C5DF;
    result = (uint32_t)((*(uint16_t *)(*(uint64_t *)(v_stack_p10 + 0x8) + 0x8)) | (32));
    result = (uint32_t)((result) - (97));
    if (((uint32_t)(result)) >= 26) goto loc_0089C5DF;
loc_0089C3FD:
    if ((*(uint64_t *)(result * 8 + 0x20 + local_r14 * 1)) == 0) goto loc_0089D6C4;
    if ((((uint8_t)(*(uint64_t *)(result * 8 + 0x20 + local_r14 * 1))) & (15)) == 0) goto loc_0089C42C;
loc_0089C417:
    if ((((uint8_t)(*(uint64_t *)(result * 8 + 0x20 + local_r14 * 1))) & (15)) == 0) goto loc_0089C42C;
    if ((((uint8_t)(*(uint64_t *)(result * 8 + 0x20 + local_r14 * 1))) & (15)) != 0) goto loc_0089C417;
loc_0089C42C:
    Arg2 = (uint32_t)((*(uint64_t *)(result * 8 + 0x20 + local_r14 * 1)) & (15));
    local_r13 = (*(uint64_t *)(result * 8 + 0x20 + local_r14 * 1)) & (-16);
    if (((uint32_t)(Arg2)) <= 1) goto loc_0089CA94;
loc_0089C43F:
    result = ObpTraceObjectReferenceIfActive(local_r13 - 48, 1, (uint32_t)(0x554C624FULL), (uint16_t)(result));
    if (local_r13 == 0) goto loc_0089D634;
loc_0089C45C:
    local_r15 = 0;
    Arg1 = (local_r13 - 48) >> (8);
    Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(local_r13 - 0x18)));
    Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(v_rip + 0x72A9A2)));
    v_stack_mB0 = 0;
    v_stack_m158 = v_stack_mB0;
    v_stack_m160 = v_stack_mE8;
    v_stack_m168 = Arg7;
    v_stack_m170 = Arg6;
    v_stack_m178 = v_stack_m138;
    v_stack_m180 = v_stack_p10;
    v_stack_m188 = (uint32_t)((uint32_t)(v_stack_p18));
    if (((uint8_t)(Arg1)) == (*(uint8_t *)(*(uint64_t *)(v_rip + 0x72AA5F) + 0x28))) goto loc_0089CB20;
    result = ObpParseSymbolicLinkEx(local_r13, v_stack_p20, Arg10, v_stack_m144);
    goto loc_0089CB25;
loc_0089C502:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x5A0)))) & (8)) == 0) goto loc_0089C16B;
    if ((*(uint16_t *)(v_stack_p10)) < 14) goto loc_0089C16B;
    result = RtlGetNtSystemRoot(local_r13, v_stack_p20, Arg10, v_stack_m144);
    result = RtlUpcaseUnicodeChar(*(uint16_t *)(result), v_stack_p20, Arg10, v_stack_m144);
    result = RtlUpcaseUnicodeChar(*(uint16_t *)(*(uint64_t *)(v_stack_p10 + 0x8) + 0x8), v_stack_p20, Arg10, v_stack_m144);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x56EE33)))) & (1)) == 0) goto loc_0089C16B;
    if (((uint16_t)((uint16_t)(result))) != ((uint16_t)((uint16_t)(result)))) goto loc_0089C16B;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_p10 + 0x8) + 0xA)) != 58) goto loc_0089C16B;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_p10 + 0x8) + 0xC)) != 92) goto loc_0089C16B;
    v_stack_p18 = (uint32_t)((uint32_t)(v_stack_p18));
    goto loc_0089C16B;
loc_0089C585:
    if (condition_is_less_or_equal) goto loc_0089D8D4;
loc_0089C59C:
loc_0089C5A6:
    Arg1 = (uint32_t)((*(uint64_t *)(v_stack_m108)) & (15));
    Arg1 = (Arg1) + (14);
    if (Arg1 > 15) goto loc_0089DC5A;
    Arg1 = (*(uint64_t *)(v_stack_m108)) & (-16);
    if (((uint32_t)(v_stack_p18)) != Arg1) goto loc_0089DC5A;
    if (((uint32_t)(v_stack_p18)) == Arg1) goto loc_0089C334;
    goto loc_0089C5A6;
loc_0089C5DF:
loc_0089C5F5:
    result = (*(uint64_t *)((uint32_t)(v_stack_p18)) - 48) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(*(uint64_t *)((uint32_t)(v_stack_p18)) - 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0x72A822));
    if (*(uint64_t *)(*(uint64_t *)(v_rip - 0x89C5E9 + arg2 * 8 + 0xFC7800) + 0x90) == 0) goto loc_0089C8F1;
    v_stack_mF0 = 0;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x89C5E9 + arg2 * 8 + 0xFC7800) + 0x90)) == (v_rip + 94155)) goto loc_0089CAAC;
    if (Arg8 != 0) goto loc_0089D8C7;
    result = ObfReferenceObject(*(uint64_t *)((uint32_t)(v_stack_p18)), Arg2, Arg10, v_stack_m144);
    if (*(uint64_t *)(arg11) == 0) goto loc_0089C6E0;
    local_rdi = (*(uint64_t *)(arg11)) + (296);
    Arg1 = (*(uint64_t *)(local_rdi)) & (-16);
    Arg2 = *(uint64_t *)(local_rdi) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (2)) != 0) goto loc_0089CC83;
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (2)) != 0) goto loc_0089CC83;
loc_0089C6A4:
    result = KeAbPostRelease(local_rdi, Arg2, Arg10, v_stack_m144);
    if ((*(uint8_t *)(arg11 + 0x16)) != 0) {
        Arg1 = *(uint64_t *)(arg11);
        Arg2 = 0x554C624FULL;
        result = ObDereferenceObjectDeferDeleteWithTag(Arg1, Arg2, Arg10, v_stack_m144);
        *(uint8_t *)(arg11 + 0x16) = 0;
    }
    *(uint64_t *)(arg11) = 0;
    *(uint8_t *)(arg11 + 0x15) = 0;
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg10, v_stack_m144);
loc_0089C6E0:
    if (((*(uint8_t *)(*(uint64_t *)(v_rip - 0x89C5E9 + arg2 * 8 + 0xFC7800) + 0x43)) & (1)) == 0) goto loc_0089D6FF;
    if ((*(uint64_t *)(*(uint64_t *)(v_rip - 0x89C5E9 + arg2 * 8 + 0xFC7800) + 0x90)) != (v_rip + 5816)) goto loc_0089CA05;
    v_stack_m158 = v_stack_mF0;
    v_stack_m160 = v_stack_mE8;
    v_stack_m168 = Arg7;
    v_stack_m170 = Arg6;
    v_stack_m178 = v_stack_m138;
    v_stack_m180 = v_stack_p10;
    v_stack_m188 = (uint32_t)((uint32_t)(v_stack_p18));
    result = CmpParseKey(*(uint64_t *)((uint32_t)(v_stack_p18)), v_stack_p20, Arg10, v_stack_m144);
loc_0089C763:
    v_stack_m148 = (uint32_t)(result);
    result = ObfDereferenceObject(*(uint64_t *)((uint32_t)(v_stack_p18)), v_stack_p20, Arg10, v_stack_m144);
loc_0089C773:
    if (sign_flag) goto loc_0089CC98;
    local_rdi = v_stack_m118;
    if (v_stack_m118 != 0) {
        Arg1 = v_stack_m118;
        result = ObDereferenceObjectDeferDelete(Arg1, (uint32_t)(v_stack_m148), Arg10, v_stack_m144);
        Arg2 = v_stack_m148;
        local_rdi = 0;
        v_stack_m118 = 0;
    }
    if (((uint32_t)(Arg2)) != 260) {
        if (((uint32_t)(Arg2)) != 872) { local_rdi = v_stack_mF0; }
        v_stack_m118 = local_rdi;
    }
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg10 + 0x18))))) & (v_stack_mE4));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg10 + 0x18))))) goto loc_0089D938;
    if (((uint32_t)(Arg2)) != 280) goto loc_0089CA62;
loc_0089C7CE:
    if (((uint32_t)(Arg2)) < 280) goto loc_0089D783;
loc_0089C7D8:
    if (((uint32_t)(Arg2)) == 280) goto loc_0089D3BF;
    if ((*(uint16_t *)(v_stack_p10)) == 0) goto loc_0089CC90;
    if (v_stack_m110 == 0) goto loc_0089C82F;
    if (v_stack_m108 == 0) goto loc_0089D173;
loc_0089C808:
    Arg1 = (*(uint64_t *)(v_stack_m108)) ^ (v_stack_m110);
    if (Arg1 >= 15) goto loc_0089D173;
    if (Arg1 != 15) goto loc_0089C808;
loc_0089C827:
    v_stack_m110 = 0;
loc_0089C82F:
    if (*(uint64_t *)(arg11) == 0) goto loc_0089C8AB;
    local_rbx = (*(uint64_t *)(arg11)) + (296);
    Arg1 = (*(uint64_t *)(local_rbx)) & (-16);
    Arg2 = *(uint64_t *)(local_rbx) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(local_rbx))) & (2)) != 0) goto loc_0089CC67;
    if ((((uint8_t)(*(uint64_t *)(local_rbx))) & (2)) != 0) goto loc_0089CC67;
loc_0089C86B:
    result = KeAbPostRelease(local_rbx, Arg2, Arg10, v_stack_m144);
    if ((*(uint8_t *)(arg11 + 0x16)) != 0) {
        Arg1 = *(uint64_t *)(arg11);
        Arg2 = 0x554C624FULL;
        result = ObDereferenceObjectDeferDeleteWithTag(Arg1, Arg2, Arg10, v_stack_m144);
        *(uint8_t *)(arg11 + 0x16) = 0;
    }
    *(uint64_t *)(arg11) = 0;
    *(uint8_t *)(arg11 + 0x15) = 0;
    result = KeLeaveCriticalRegionThread(*(uint64_t *)(gs_base + (0 + 0x188)), Arg2, Arg10, v_stack_m144);
loc_0089C8AB:
    if (((uint32_t)((uint32_t)(v_stack_m148))) != 280) goto loc_0089C0DF;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p10 + 0x8)))) == 92) goto loc_0089CC90;
loc_0089C8CB:
    v_stack_m138 = v_xmm1;
loc_0089C8D3:
loc_0089C8DE:
    goto loc_0089C5F5;
loc_0089C8F1:
    if (v_stack_p10 != (*(uint64_t *)(v_rip + 0x672D58))) goto loc_0089D8C7;
    v_stack_mC0 = v_stack_mF0;
    if ((uint16_t)(v_stack_m144) == 0) goto loc_0089C931;
    if ((*(uint16_t *)(*(uint64_t *)(v_stack_p10 + 0x8))) == 92) {
        Arg3 = (*(uint64_t *)(v_stack_p10 + 0x8)) + (2);
        Arg4 = (uint16_t)((v_stack_m144) + ((uint16_t)((uint32_t)(0xFFFEULL))));
        local_r10 = (uint16_t)((local_r10) + ((uint16_t)((uint32_t)(0xFFFEULL))));
        v_stack_m130 = Arg3;
        v_stack_m136 = (uint16_t)(local_r10);
        v_stack_m138 = (uint16_t)(Arg4);
    }
    v_stack_mD8 = v_xmm1;
    if ((uint16_t)(Arg4) == 0) goto loc_0089C95C;
loc_0089C940:
    if ((*(uint16_t *)(Arg3)) == 92) goto loc_0089C95C;
    Arg3 = (Arg3) + (2);
    Arg4 = (uint16_t)((Arg4) + ((uint16_t)((uint32_t)(0xFFFEULL))));
    v_stack_m130 = Arg3;
    v_stack_m138 = (uint16_t)(Arg4);
    if (condition_is_not_equal) goto loc_0089C940;
loc_0089C95C:
    result = (uint16_t)((v_stack_mD8) - ((uint16_t)(Arg4)));
    local_r10 = (uint16_t)((local_r10) - ((uint16_t)(result)));
    v_stack_mD8 = (uint16_t)(result);
    v_stack_m136 = (uint16_t)(local_r10);
    if ((uint16_t)(result) == 0) goto loc_0089CC90;
    if ((uint8_t)((uint32_t)(v_stack_m144)) == 0) goto loc_0089C995;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg10 + 0xC)))) & (1)) == 0) goto loc_0089D216;
loc_0089C995:
    if (Arg8 != 0) goto loc_0089D103;
loc_0089C9A3:
    local_rsi = 0;
loc_0089C9A6:
    if ((*(uint64_t *)(arg11)) == 0) goto loc_0089CECE;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_mF0 + 296, Arg2, Arg3, Arg4);
    if (0 != 0) goto loc_0089CD59;
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = v_stack_mF0 + 296;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_stack_mF0 + 296;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    goto loc_0089CD78;
loc_0089CA05:
    if ((v_stack_mF0 + 296) != (v_rip + 6916)) goto loc_0089D198;
    v_stack_m158 = v_stack_mF0;
    v_stack_m160 = v_stack_mE8;
    v_stack_m168 = Arg7;
    v_stack_m170 = Arg6;
    v_stack_m178 = v_stack_m138;
    v_stack_m180 = 0;
    v_stack_m188 = (uint32_t)((uint32_t)(v_stack_p18));
    result = IopParseDevice(Arg1, Arg2, Arg3, Arg4);
    goto loc_0089C763;
loc_0089CA62:
    if (0 == 260) goto loc_0089C7CE;
    if (0 == 872) goto loc_0089C7CE;
loc_0089CA7A:
    if (v_stack_mF0 == 0) {
        Arg2 = 0xC0000034ULL;
        v_stack_m148 = (uint32_t)(Arg2);
    }
    v_stack_m118 = 0;
    goto loc_0089D209;
loc_0089CA94:
    if ((uint32_t)(Arg2) == 0) goto loc_0089D634;
    result = ObpFastReplenishReference((uint32_t)(v_stack_p18), v_stack_mF0, Arg3, Arg4);
    goto loc_0089C43F;
loc_0089CAAC:
    v_stack_m158 = v_stack_mF0;
    v_stack_m160 = v_stack_mE8;
    v_stack_m168 = Arg7;
    v_stack_m170 = Arg6;
    v_stack_m178 = v_stack_m138;
    v_stack_m180 = v_stack_p10;
    v_stack_m188 = (uint32_t)((uint32_t)(v_stack_p18));
    result = ObpParseSymbolicLinkEx(v_stack_mF0, v_stack_p20, Arg10, v_stack_m144);
    v_stack_m148 = (uint32_t)(result);
    goto loc_0089C773;
loc_0089CB20:
    result = IopParseDevice(v_stack_mF0, (uint32_t)((uint32_t)(result)), Arg10, v_stack_m144);
loc_0089CB25:
    v_stack_m148 = (uint32_t)(result);
loc_0089CB2F:
    Arg1 = (*(uint64_t *)((uint32_t)(v_stack_p18))) ^ (v_stack_mF0);
    if (Arg1 >= 15) goto loc_0089DAF8;
    if (Arg1 != 15) goto loc_0089CB2F;
    result = *(uint64_t *)((uint32_t)(v_stack_p18));
    if ((*(uint32_t *)(v_rip + 0x7284BF)) != 0) {
        Arg2 = 0;
        Arg1 = v_stack_mF0 - 48;
        Arg4 = 0x554C624FULL;
        Arg3 = Arg2 + 1;
        result = ObpPushStackInfo(Arg1, Arg2, Arg3, Arg4);
    }
    if (sign_flag) goto loc_0089CC98;
    local_rdi = v_stack_m118;
    if (((uint32_t)((uint32_t)(v_stack_m148))) != 260) {
        local_rdi = v_stack_m118;
        if (((uint32_t)((uint32_t)(v_stack_m148))) != 872) { local_rdi = v_stack_mB0; }
        v_stack_m118 = local_rdi;
    }
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg10 + 0x18))))) & (v_stack_mE4));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg10 + 0x18))))) goto loc_0089D938;
    if (((uint32_t)((uint32_t)(v_stack_m148))) != 280) goto loc_0089D156;
loc_0089CBB5:
    if (((uint32_t)((uint32_t)(v_stack_m148))) < 280) goto loc_0089D76A;
loc_0089CBC0:
    if (((uint32_t)((uint32_t)(v_stack_m148))) == 280) goto loc_0089D3BF;
    if ((*(uint16_t *)(v_stack_p10)) == 0) goto loc_0089CC90;
    if (v_stack_m108 == 0) goto loc_0089D5B2;
loc_0089CBEB:
    Arg1 = (*(uint64_t *)(v_stack_m108)) ^ (v_stack_m110);
    if (Arg1 >= 15) goto loc_0089D5B2;
    if (Arg1 != 15) goto loc_0089CBEB;
loc_0089CC0A:
    v_stack_m110 = 0;
    if (((uint32_t)((uint32_t)(v_stack_m148))) == 280) goto loc_0089CC74;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(v_stack_p10 + 0x8)))) != 92) goto loc_0089CC90;
    if (((uint32_t)((uint32_t)(v_stack_m148))) == 872) goto loc_0089D146;
    v_stack_mA8 = 0;
    result = PsGetPermanentSiloContext(Arg9, (uint32_t)(*(uint32_t *)(v_rip + 0x728431)), v_stack_mA8, Arg4);
    if (!sign_flag) goto loc_0089DC21;
    v_stack_mA8 = *(uint64_t *)(v_rip + 0x672A0E);
loc_0089CC5E:
    v_stack_m128 = *(uint64_t *)(v_rip + 0x672A0E);
    goto loc_0089C12D;
loc_0089CC67:
    result = ExfReleasePushLock((uint32_t)(v_stack_p18), (uint32_t)(*(uint32_t *)(v_rip + 0x728431)), v_stack_mA8, Arg4);
    goto loc_0089C86B;
loc_0089CC74:
    if (((uint16_t)((uint32_t)(v_stack_p18))) == 92) goto loc_0089CC90;
loc_0089CC7A:
    goto loc_0089C8CB;
loc_0089CC83:
    result = ExfReleasePushLock(local_rdi, (uint32_t)(*(uint32_t *)(v_rip + 0x728431)), *(uint64_t *)(v_stack_p10 + 0x8), Arg4);
    goto loc_0089C6A4;
loc_0089CC90:
    v_stack_m148 = 0xC0000033ULL;
loc_0089CC98:
    result = ObpReleaseLookupContext(Arg11, (uint32_t)(*(uint32_t *)(v_rip + 0x728431)), *(uint64_t *)(v_stack_p10 + 0x8), Arg4);
loc_0089CCA0:
loc_0089CCA4:
    if (v_stack_m118 != 0) goto loc_0089DB3B;
loc_0089CCAD:
    if (v_stack_mB8 != 0) {
        result = ObDereferenceObjectDeferDelete(v_stack_mB8, (uint32_t)(*(uint32_t *)(v_rip + 0x728431)), *(uint64_t *)(v_stack_p10 + 0x8), Arg4);
    }
    result = SeClearLearningModeObjectInformation(v_stack_mB8, (uint32_t)(*(uint32_t *)(v_rip + 0x728431)), *(uint64_t *)(v_stack_p10 + 0x8), Arg4);
    if (v_stack_m110 == 0) goto loc_0089CCFB;
    if (v_stack_m108 == 0) goto loc_0089D7B2;
loc_0089CCDC:
    Arg1 = (*(uint64_t *)(v_stack_m108)) ^ (v_stack_m110);
    if (Arg1 >= 15) goto loc_0089D7B2;
    if (Arg1 != 15) goto loc_0089CCDC;
loc_0089CCFB:
    if (sign_flag) goto loc_0089CD54;
    if (Arg12 == 0) goto loc_0089CD1B;
    if (((uint32_t)((uint32_t)(v_stack_mE4))) != -1) goto loc_0089DD98;
loc_0089CD1B:
    *(uint64_t *)(arg13) = v_stack_mB0;
    goto loc_0089DD9F;
loc_0089CD2A:
    if (((uint16_t)(Arg12)) == 6) goto loc_0089D2C7;
loc_0089CD34:
    result = (uint32_t)(v_stack_m148);
    if (v_stack_m128 == 0) {
        Arg1 = Arg9;
        result = OBP_GET_SILO_ROOT_DIRECTORY_FROM_SILO(Arg1, Arg12, v_stack_m110, Arg4);
        v_stack_m128 = result;
    }
    goto loc_0089CC7A;
loc_0089CD54:
    local_r13 = 0;
    goto loc_0089CD1B;
loc_0089CD59:
    if (!(condition_is_above_or_equal)) {
        Arg3 = (uint32_t)(v_stack_p18);
        Arg2 = v_stack_m118;
        Arg1 = (uint32_t)(v_stack_p18);
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m118 != 0) {
        *(uint8_t *)(v_stack_m118 + 0xA) = 1;
    }
    if (v_stack_m118 != 0) goto loc_0089D6EE;
loc_0089CD90:
    result = KeAbPostRelease(*(uint64_t *)(arg11) + 296, Arg2, Arg3, Arg4);
    if ((*(uint8_t *)(arg11 + 0x16)) != 0) {
        Arg1 = *(uint64_t *)(arg11);
        Arg2 = 0x554C624FULL;
        result = ObDereferenceObjectDeferDeleteWithTag(Arg1, Arg2, Arg3, Arg4);
        *(uint8_t *)(arg11 + 0x16) = 0;
    }
    *(uint64_t *)(arg11) = 0;
    *(uint8_t *)(arg11 + 0x15) = (uint8_t)(v_stack_p10);
loc_0089CDC1:
    local_rsi = (uint32_t)((v_stack_mD8) >> (1));
    if (((uint32_t)(local_rsi)) < 4) goto loc_0089D082;
    local_rbx = 0;
loc_0089CDE0:
    if (((Arg11) & (*(uint64_t *)(v_stack_mD0))) != 0) goto loc_0089D28A;
    local_rdi = (*(uint64_t *)(v_stack_mD0)) & (Arg10);
loc_0089CDEF:
    local_r15 = (v_stack_mD0) + (8);
    result = (0) >> (1);
    result = (result) + (local_rdi);
    local_rsi = (uint32_t)((local_rsi) + (-4));
    local_rbx = (local_rbx + local_rbx * 2) + (result);
    if (((uint32_t)(local_rsi)) >= 4) goto loc_0089CDE0;
    local_r14 = (local_rbx) >> (32);
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(local_rbx)));
loc_0089CE1C:
    if ((uint32_t)(local_rsi) == 0) goto loc_0089CE4F;
loc_0089CE20:
    local_rsi = (uint32_t)((local_rsi) - 1);
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) >> (1));
    local_r14 = (uint32_t)((local_r14 + local_r14 * 2) + ((uint32_t)(Arg1)));
    if (((uint32_t)(*(uint16_t *)(local_r15))) < 97) goto loc_0089CE48;
    if (((uint32_t)(*(uint16_t *)(local_r15))) > 122) goto loc_0089D185;
    local_r14 = (uint32_t)((local_r14) + (-32));
loc_0089CE48:
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)(*(uint16_t *)(local_r15))));
loc_0089CE4B:
    if ((uint32_t)(local_rsi) != 0) goto loc_0089CE20;
loc_0089CE4F:
    *(uint32_t *)(arg11 + 0x10) = (uint32_t)(local_r14);
    Arg3 = (uint32_t)(((uint32_t)(v_stack_m120)) & (64));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) - ((uint32_t)(*(uint16_t *)(local_r15))));
    v_stack_m128 = Arg3;
    result = (uint32_t)((result) >> (1));
    result = (uint32_t)((result) + ((uint32_t)(*(uint16_t *)(local_r15))));
    result = (uint32_t)((result) >> (5));
    Arg1 = (uint32_t)((Arg1) * ((uint32_t)((uint8_t)(result))));
    result = (uint8_t)(((uint8_t)(local_r14)) - ((uint8_t)(Arg1)));
    *(uint8_t *)(arg11 + 0x14) = (uint8_t)((uint8_t)(result));
    if (*(uint64_t *)(*(uint64_t *)(arg11) + (uint8_t)(result) * 8) == 0) goto loc_0089CEC0;
loc_0089CEA0:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg11) + (uint8_t)(result) * 8) + 0x10)) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg11 + 0x10))))) goto loc_0089CF41;
loc_0089CEAB:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg11) + (uint8_t)(result) * 8)) != 0) goto loc_0089CEA0;
loc_0089CEC0:
    result = 0;
    v_stack_m128 = 0;
    goto loc_0089D3CC;
loc_0089CECE:
    if ((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg11) + (uint8_t)(result) * 8)) != 0) goto loc_0089D5C4;
    *(uint64_t *)(arg11) = 0;
    *(uint8_t *)(arg11 + 0x15) = (uint8_t)(*(uint64_t *)(*(uint64_t *)(arg11) + (uint8_t)(result) * 8));
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(local_r13 + 296, Arg2, Arg3, Arg4);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = local_r13 + 296;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = local_r13 + 296;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result == 0) goto loc_0089CDC1;
    *(uint8_t *)(result + 0xA) = 1;
    goto loc_0089CDC1;
loc_0089CF41:
    Arg2 = (*(uint64_t *)(arg11 + 0x14 + 0x8)) - (48);
    result = (uint32_t)((*(uint8_t *)(arg2 + 0x1A)) & (3));
    Arg2 = (Arg2) - (*(uint8_t *)(result + v_rip - 0x89CF4C * 1 + 0xF0FF80));
    result = PsGetCurrentServerSiloGlobals(v_rip - 9031500, Arg2, Arg3, Arg4);
    v_stack_mC8 = *(uint64_t *)(result + 0x4B0);
    if (((uint16_t)(v_stack_mD8)) != (*(uint16_t *)(arg2 + 0x8))) goto loc_0089CEAB;
    if (Arg3 == 0) goto loc_0089D278;
    result = RtlCompareMemory(v_stack_mD0, *(uint64_t *)(arg2 + 0x10), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mD8)))), Arg4);
    if (result == ((uint32_t)((uint32_t)(v_stack_mD8)))) goto loc_0089CFDD;
    result = (result) >> (1);
    result = (result) + (result);
    Arg3 = (v_stack_mD0) + (result);
    local_r14 = (*(uint64_t *)(arg2 + 0x10)) + (result);
loc_0089CFC0:
    if (Arg3 >= ((uint32_t)((uint32_t)(v_stack_mD8)) + v_stack_mD0 * 1)) goto loc_0089CFDD;
    if (((uint16_t)(*(uint16_t *)(Arg3))) != ((uint16_t)(*(uint16_t *)(local_r14)))) goto loc_0089D04D;
loc_0089CFD3:
    Arg3 = (Arg3) + (2);
    local_r14 = (local_r14) + (2);
    goto loc_0089CFC0;
loc_0089CFDD:
    v_stack_m128 = *(uint64_t *)(arg11 + 0x14 + 0x8);
    *(uint64_t *)(arg11 + 0x8) = *(uint64_t *)(*(uint64_t *)(arg11) + (uint8_t)(result) * 8);
    if (*(uint64_t *)(arg11 + 0x14 + 0x8) == 0) goto loc_0089D3CC;
loc_0089CFFD:
    if (v_stack_p8 == 0) goto loc_0089D1F5;
    if (v_stack_m128 == 0) goto loc_0089D3A3;
    if ((uint16_t)(v_stack_m138) == 0) goto loc_0089D330;
loc_0089D035:
    local_r15 = 0;
    goto loc_0089C5F5;
loc_0089D04D:
    if (((uint32_t)(v_stack_m138)) < 97) goto loc_0089D05E;
    if (((uint32_t)(v_stack_m138)) > 122) goto loc_0089D08A;
    Arg4 = (uint16_t)((v_stack_m138) - (32));
loc_0089D05E:
    if (((uint32_t)(v_stack_m136)) < 97) goto loc_0089D06F;
    if (((uint32_t)(v_stack_m136)) > 122) goto loc_0089D0C5;
    local_r10 = (uint16_t)((v_stack_m136) - (32));
loc_0089D06F:
    if (((uint16_t)(Arg4)) == ((uint16_t)(local_r10))) goto loc_0089CFD3;
loc_0089D079:
    goto loc_0089CEAB;
loc_0089D082:
    local_r14 = 0;
    goto loc_0089CE1C;
loc_0089D08A:
    if (v_stack_mC8 == 0) goto loc_0089D05E;
    if (((uint16_t)(Arg4)) < 192) goto loc_0089D05E;
    result = (Arg4) >> (8);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) & (15));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) >> (4));
    result = (uint32_t)((result) & (15));
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_mC8 + result * 2)) + ((uint32_t)(result)));
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_mC8 + Arg1 * 2)) + ((uint32_t)(Arg2)));
    Arg4 = (uint16_t)((Arg4) + (*(uint16_t *)(v_stack_mC8 + Arg1 * 2)));
    goto loc_0089D05E;
loc_0089D0C5:
    if (v_stack_mC8 == 0) goto loc_0089D06F;
    if (((uint16_t)(local_r10)) < 192) goto loc_0089D06F;
    result = (local_r10) >> (8);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) & (15));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) >> (4));
    result = (uint32_t)((result) & (15));
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_mC8 + result * 2)) + ((uint32_t)(result)));
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_mC8 + Arg1 * 2)) + ((uint32_t)(Arg2)));
    local_r10 = (uint16_t)((local_r10) + (*(uint16_t *)(v_stack_mC8 + Arg1 * 2)));
    goto loc_0089D06F;
loc_0089D103:
    if ((uint16_t)(Arg4) != 0) goto loc_0089C9A3;
    goto loc_0089D259;
loc_0089D112:
    Arg1 = (v_stack_m128 - 48) >> (8);
    Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(v_stack_m128 - 0x18)));
    Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(v_rip + 0x729D21)));
    if (((uint8_t)(Arg1)) == (*(uint8_t *)(*(uint64_t *)(v_rip + 0x7299C7) + 0x28))) goto loc_0089C093;
    result = ObfDereferenceObject(v_stack_m128, Arg2, (uint32_t)(v_stack_m128), Arg4);
loc_0089D13C:
    goto loc_0089DD9F;
loc_0089D146:
    v_stack_m128 = *(uint64_t *)(v_rip + 0x67251B);
    goto loc_0089C12D;
loc_0089D156:
    if (((uint32_t)(Arg2)) == 260) goto loc_0089CBB5;
    if (((uint32_t)(Arg2)) == 872) goto loc_0089CBB5;
    goto loc_0089CA7A;
loc_0089D173:
    result = ObDereferenceDeviceMap(0, 1, (uint32_t)(v_stack_m128), Arg4);
    goto loc_0089C827;
loc_0089D185:
    result = RtlUpcaseUnicodeChar(1, 1, (uint32_t)(v_stack_m128), Arg4);
    local_r14 = (uint32_t)((local_r14) + ((uint32_t)((uint16_t)(result))));
    goto loc_0089CE4B;
loc_0089D198:
    v_stack_m158 = v_stack_mF0;
    v_stack_m160 = v_stack_mE8;
    v_stack_m168 = Arg7;
    v_stack_m170 = Arg6;
    v_stack_m178 = v_stack_m138;
    v_stack_m180 = *(uint64_t *)(*(uint64_t *)(arg11) + (uint8_t)(result) * 8);
    if ((v_rip - 9031716) != (v_rip + 1444289)) goto loc_0089DCBF;
    v_stack_m188 = (uint32_t)((uint32_t)(v_stack_p18));
    result = IopParseFile(1, 1, (uint32_t)(v_stack_m128), Arg4);
    goto loc_0089C763;
loc_0089D1F5:
    if (v_stack_m128 == 0) goto loc_0089D3A3;
loc_0089D201:
    v_stack_m148 = (uint32_t)((uint32_t)(v_stack_mFC));
loc_0089D205:
loc_0089D209:
    if (!sign_flag) goto loc_0089CCA4;
    goto loc_0089CC98;
loc_0089D216:
    v_stack_m180 = v_stack_mFC;
    v_stack_m188 = (uint8_t)((uint32_t)(v_stack_mFC));
    result = ObpCheckTraverseAccess(v_stack_m128, (uint32_t)(v_stack_mFC), 1, Arg4);
    v_stack_p8 = (uint8_t)(result);
    if ((uint8_t)(result) != 0) goto loc_0089DD24;
    if (!sign_flag) goto loc_0089DD17;
loc_0089D247:
    if (v_stack_m138 != 0) goto loc_0089D201;
    if (Arg8 == 0) goto loc_0089D201;
loc_0089D259:
    goto loc_0089C9A6;
loc_0089D261:
    v_stack_m128 = *(uint64_t *)(v_rip + 0x672400);
    goto loc_0089C12D;
loc_0089D278:
    result = memcmp(v_stack_m128, (uint32_t)(v_stack_mFC), 1, Arg4);
    if ((uint32_t)(result) == 0) goto loc_0089CFDD;
    goto loc_0089D079;
loc_0089D28A:
loc_0089D290:
    if (((uint32_t)((uint16_t)(v_stack_m118))) < 97) goto loc_0089D2A8;
    if (((uint32_t)((uint16_t)(v_stack_m118))) <= 122) goto loc_0089D2C2;
    result = RtlUpcaseUnicodeChar((uint16_t)((uint16_t)(v_stack_m118)), (uint32_t)(v_stack_mFC), 1, Arg4);
loc_0089D2A8:
    local_r14 = (4) - (1);
    if (condition_is_not_equal) goto loc_0089D290;
    goto loc_0089CDEF;
loc_0089D2C2:
    result = (uint32_t)(((uint16_t)(result)) + (-32));
    goto loc_0089D2A8;
loc_0089D2C7:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(1 + 0x8)))) - (0x3F005CULL));
    result = *(uint64_t *)(1 + 0x8);
    if (!(condition_is_not_equal)) {
        Arg1 = *(uint16_t *)(*(uint64_t *)(1 + 0x8) + 0x4);
        result = (uint16_t)(local_r10);
        Arg1 = (uint32_t)((Arg1) - ((uint32_t)(result)));
    }
    if ((uint32_t)(Arg1) != 0) goto loc_0089CD34;
    result = ObpReferenceCurrentDeviceMap((uint32_t)((uint32_t)(local_r14)), v_stack_m108, 1, Arg4);
    v_stack_m110 = result;
    if (result == 0) goto loc_0089CD34;
    if (*(uint64_t *)(result) == 0) goto loc_0089CD34;
    Arg2 = 0;
    result = ObReferenceObjectByPointer(*(uint64_t *)(result), Arg2, v_stack_p20, Arg5);
    v_stack_m148 = (uint32_t)(result);
    goto loc_0089D209;
loc_0089D330:
    result = (*(uint64_t *)(result) - 48) >> (8);
    Arg2 = ((uint8_t)(result)) ^ (*(uint8_t *)(*(uint64_t *)(result) - 0x18));
    Arg2 = (Arg2) ^ (*(uint8_t *)(v_rip + 0x729B02));
    if (*(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_p18) + arg2 * 8 + 0xFC7800) + 0x90) == 0) goto loc_0089D37F;
    if ((*(uint64_t *)(*(uint64_t *)((uint32_t)(v_stack_p18) + arg2 * 8 + 0xFC7800) + 0x90)) == (v_rip + 90712)) goto loc_0089D035;
    if (Arg8 == 0) goto loc_0089D035;
loc_0089D37F:
    Arg2 = 0;
    result = ObReferenceObjectByPointer(*(uint64_t *)(result), Arg2, v_stack_p20, Arg5);
    v_stack_m148 = (uint32_t)(result);
    goto loc_0089D205;
loc_0089D3A3:
    if (v_stack_m138 != 0) goto loc_0089D75D;
    if (Arg8 != 0) goto loc_0089D7D1;
loc_0089D3BF:
    v_stack_m148 = 0xC0000034ULL;
    goto loc_0089CC98;
loc_0089D3CC:
    if ((((uint8_t)((uint32_t)(v_stack_m120))) & (1)) == 0) goto loc_0089CFFD;
loc_0089D3E0:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg11) + 0x150)))) & (4)) != 0) goto loc_0089D411;
    if (*(uint64_t *)(*(uint64_t *)(arg11) + 0x130) == 0) goto loc_0089CFFD;
    if ((*(uint64_t *)(*(uint64_t *)(arg11) + 0x130)) != v_stack_m110) goto loc_0089D4FC;
    goto loc_0089D432;
loc_0089D411:
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(arg11) + 0x130))) & (16)) != 0) goto loc_0089DD2F;
loc_0089D419:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m110 + 0x8) + 0x150)))) & (16)) != 0) goto loc_0089DD5F;
loc_0089D428:
loc_0089D42F:
loc_0089D432:
    v_stack_mC8 = *(uint64_t *)(*(uint64_t *)(v_stack_m110 + 0x8) + 0x138);
    if (*(uint64_t *)(*(uint64_t *)(v_stack_m110 + 0x8) + 0x138) == 0) goto loc_0089CFFD;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(v_stack_m110 + 0x8) + 0x138) + 296, Arg2, Arg2 + 1, Arg5);
    result = 0;
    if (condition_is_not_equal) goto loc_0089DB16;
loc_0089D470:
    if (0 != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    Arg1 = 0;
    if (condition_is_not_equal) goto loc_0089DAE7;
loc_0089D491:
    result = KeAbPostRelease(*(uint64_t *)(arg11) + 296, Arg2, Arg2 + 1, Arg5);
    result = 0;
loc_0089D49F:
    *(uint8_t *)(arg11 + 0x16) = 0;
    if ((uint8_t)(*(uint8_t *)(arg11 + 0x16)) != 0) goto loc_0089DD6E;
loc_0089D4AD:
    Arg3 = (uint32_t)(((uint32_t)(v_stack_m120)) & (64));
    *(uint64_t *)(arg11) = *(uint64_t *)(*(uint64_t *)(v_stack_m110 + 0x8) + 0x138);
    v_stack_m128 = Arg3;
    local_r14 = (*(uint8_t *)((uint32_t)(v_stack_p18)) * 8) + (*(uint64_t *)(*(uint64_t *)(v_stack_m110 + 0x8) + 0x138));
    if (*(uint64_t *)(local_r14) == 0) goto loc_0089D4ED;
loc_0089D4D3:
    if ((*(uint32_t *)(*(uint64_t *)(local_r14) + 0x10)) == ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x16258))))) goto loc_0089D960;
loc_0089D4DE:
    if (*(uint64_t *)(*(uint64_t *)(local_r14)) != 0) goto loc_0089D4D3;
loc_0089D4ED:
    result = 0;
    v_stack_m128 = 0;
    goto loc_0089D3E0;
loc_0089D4FC:
    result = PsGetCurrentServerSiloGlobals(*(uint64_t *)(arg11) + 296, Arg2, Arg3, Arg5);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result + 120, Arg2, Arg3, Arg5);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = result + 120;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = result + 120;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
        Arg1 = 17;
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsi = *(uint64_t *)(*(uint64_t *)(local_r14));
    if (*(uint64_t *)(v_stack_mC8 + 0x130) != 0) {
        local_rsi = *(uint64_t *)(*(uint64_t *)(v_stack_mC8 + 0x130) + 0x8);
    }
    Arg1 = 0;
    result = Arg1;
    if (!(condition_is_equal)) {
        Arg1 = result + 120;
        result = ExfReleasePushLockShared(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(result + 120, Arg2, Arg3, Arg4);
    result = KeLeaveGuardedRegion(result + 120, Arg2, Arg3, Arg4);
    goto loc_0089D42F;
loc_0089D589:
    result = (result) >> (32);
    if ((uint32_t)(result) != 0) goto loc_0089C242;
    result = ObfDereferenceObjectWithTag(local_rsi, (uint32_t)(0x746C6644ULL), Arg3, Arg4);
loc_0089D5A5:
    result = PsGetServerSiloGlobals(v_stack_mC8, (uint32_t)(0x746C6644ULL), Arg3, Arg4);
    goto loc_0089C28C;
loc_0089D5B2:
    result = ObDereferenceDeviceMap(Arg3, 1, Arg3, Arg4);
    goto loc_0089CC0A;
loc_0089D5C4:
    result = ObpLockDirectoryExclusive(Arg11, v_stack_mC8, Arg3, Arg4);
    goto loc_0089CDC1;
loc_0089D5D4:
    Arg1 = (v_stack_mC8 - 48) >> (8);
    Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(v_stack_mC8 - 0x18)));
    Arg1 = (uint8_t)((Arg1) ^ (*(uint8_t *)(v_rip + 0x72985F)));
    if (((uint8_t)(Arg1)) != (*(uint8_t *)(*(uint64_t *)(v_rip + 0x672075) + 0x28))) goto loc_0089C093;
    Arg2 = 0;
    result = ObReferenceObjectByPointer(v_stack_mC8, Arg2, v_stack_p20, Arg5);
    v_stack_m148 = (uint32_t)(result);
    local_r15 = 1;
    if (!sign_flag) { local_r15 = v_stack_mC8; }
    result = ObfDereferenceObject(v_stack_mC8, Arg2, v_stack_p20, Arg5);
    *(uint64_t *)(arg13) = local_r15;
    goto loc_0089DD9F;
loc_0089D634:
    result = PsGetServerSiloGlobals(*(uint64_t *)(result + 0x10), Arg2, v_stack_p20, Arg5);
    Arg3 = 0;
    local_rdi = (result) + (120);
    Arg2 = 0;
    result = KeAbPreAcquire(local_rdi, Arg2, Arg3, Arg5);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = local_rdi;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = local_rdi;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    result = ObFastReferenceObjectLocked((uint32_t)(v_stack_p18), (uint32_t)(0x554C624FULL), Arg3, Arg4);
    Arg1 = 0;
    if (condition_is_not_equal) goto loc_0089DC9E;
loc_0089D6AE:
    result = KeAbPostRelease(local_rdi, (uint32_t)(0x554C624FULL), Arg3, Arg4);
    result = KeLeaveGuardedRegion(local_rdi, (uint32_t)(0x554C624FULL), Arg3, Arg4);
    if (result != 0) goto loc_0089C45C;
loc_0089D6C4:
    if (*(uint64_t *)(result + 0x18) != 0) goto loc_0089C3FD;
    local_r15 = 0;
    goto loc_0089C5DF;
loc_0089D6EE:
    result = ExfReleasePushLockShared((uint32_t)(v_stack_p18) + 296, (uint32_t)(0x554C624FULL), v_stack_m130, v_stack_m138);
    goto loc_0089CD90;
loc_0089D6FF:
    v_stack_m160 = v_stack_mF0;
    v_stack_m168 = Arg7;
    v_stack_m170 = Arg6;
    v_stack_m178 = v_stack_m138;
    v_stack_m180 = result;
    if (((uint32_t)(v_stack_p18)) != (v_rip + 425203)) goto loc_0089DD81;
    v_stack_m188 = (uint32_t)((uint32_t)(v_stack_p18));
    result = ExpWin32ParseProcedure((uint32_t)(v_stack_p18) + 296, (uint32_t)(0x554C624FULL), Arg10, v_stack_m138);
    goto loc_0089C763;
loc_0089D75D:
    v_stack_m148 = 0xC000003AULL;
    goto loc_0089CC98;
loc_0089D76A:
    if (((uint32_t)((uint32_t)(0x554C624FULL))) == 872) goto loc_0089CBC0;
loc_0089D776:
    v_stack_m148 = 0xC000050BULL;
    goto loc_0089CC98;
loc_0089D783:
    if (((uint32_t)((uint32_t)(0x554C624FULL))) == 872) goto loc_0089C7D8;
    goto loc_0089D776;
loc_0089D791:
    if (0 != 0) goto loc_0089C35A;
    local_r15 = 0;
    v_stack_m108 = 0;
    result = ObpSetCurrentProcessDeviceMap((uint32_t)(v_stack_p18) + 296, (uint32_t)(0x554C624FULL), Arg10, v_stack_m138);
    v_stack_m110 = result;
    goto loc_0089C35D;
loc_0089D7B2:
    result = ObDereferenceDeviceMap(Arg10, 1, Arg10, v_stack_m138);
    goto loc_0089CCFB;
loc_0089D7C4:
    result = ExfReleasePushLockShared(local_rdi, 1, Arg10, v_stack_m138);
    goto loc_0089C344;
loc_0089D7D1:
    Arg2 = 4;
    if (v_stack_p20 == (*(uint64_t *)(v_rip + 0x671E6D))) { Arg2 = 8; }
    v_stack_m178 = v_stack_m148;
    v_stack_m180 = (uint8_t)((uint32_t)(v_stack_m144));
    v_stack_m188 = 0;
    result = ObCheckCreateObjectAccess(v_stack_mC0, Arg2, Arg10, v_stack_mD8);
    if ((uint8_t)(result) == 0) goto loc_0089DB48;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mC0 + 0x154)))) != -1) goto loc_0089D8E0;
loc_0089D832:
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)(v_stack_mD8)), (uint32_t)(0x6D4E624FULL), v_stack_mD8);
    if (result == 0) goto loc_0089D94C;
    result = ObpInsertDirectoryEntry(v_stack_mC0, result, Arg11, v_stack_mD8);
    if ((uint8_t)(result) == 0) goto loc_0089D945;
    result = memcpy(result, v_stack_mD0, (uint32_t)((uint32_t)(v_stack_mD8)), v_stack_mD8);
    result = (uint32_t)((*(uint8_t *)(result - 0x16)) & (3));
    local_rbx = (result - 48) - (*(uint8_t *)(result + v_rip - 0x89D88C * 1 + 0xF0FF80));
    result = *(uint8_t *)(result + v_rip - 0x89D88C * 1 + 0xF0FF80);
    if (*(uint64_t *)(local_rbx + 0x10) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(local_rbx + 0x10), Arg2, (uint32_t)((uint32_t)(v_stack_mD8)), v_stack_mD8);
    }
    *(uint16_t *)(local_rbx + 0x8) = (uint16_t)(v_stack_mD8);
    *(uint16_t *)(local_rbx + 0xA) = (uint16_t)(v_stack_mD8);
    *(uint64_t *)(local_rbx + 0x10) = result;
    v_stack_m148 = 0;
    goto loc_0089CCA0;
loc_0089D8C7:
    v_stack_m148 = 0xC0000024ULL;
    goto loc_0089CC98;
loc_0089D8D4:
    goto loc_0089C59C;
loc_0089D8E0:
    if (v_stack_p20 == (*(uint64_t *)(v_rip + 0x7292F1))) goto loc_0089D8F6;
    if (v_stack_p20 != (*(uint64_t *)(v_rip + 0x671D68))) goto loc_0089D832;
loc_0089D8F6:
    result = PsGetCurrentProcessSessionId(14, Arg2, (uint32_t)((uint32_t)(v_stack_mD8)), v_stack_mD8);
    if (((uint32_t)(local_rbx)) == ((uint32_t)(result))) goto loc_0089D832;
    result = SeSinglePrivilegeCheck(*(uint64_t *)(v_rip + 0x73C38E), (uint8_t)(result), (uint32_t)((uint32_t)(v_stack_mD8)), v_stack_mD8);
    if ((uint8_t)(result) != 0) goto loc_0089D832;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_p18)) >> (6));
    Arg2 = (uint8_t)((Arg2) & (1));
    result = ObpIsUnsecureName(v_stack_mD8, Arg2, (uint32_t)((uint32_t)(v_stack_mD8)), v_stack_mD8);
    if ((uint8_t)(result) != 0) goto loc_0089D832;
loc_0089D938:
    v_stack_m148 = 0xC0000022ULL;
    goto loc_0089CC98;
loc_0089D945:
    Arg2 = 0;
    result = ExFreePoolWithTag(v_stack_mD8, Arg2, (uint32_t)((uint32_t)(v_stack_mD8)), v_stack_mD8);
loc_0089D94C:
    v_stack_m148 = 0xC000009AULL;
    goto loc_0089CC98;
loc_0089D959:
    local_rsi = 0;
    goto loc_0089C21F;
loc_0089D960:
    Arg2 = (*(uint64_t *)(local_rsi + 0x8)) - (48);
    result = (uint32_t)((*(uint8_t *)(arg2 + 0x1A)) & (3));
    Arg2 = (Arg2) - (*(uint8_t *)(result + v_rip - 0x89D96B * 1 + 0xF0FF80));
    result = PsGetCurrentServerSiloGlobals(v_rip - 9034091, Arg2, (uint32_t)((uint32_t)(v_stack_mD8)), v_stack_mD8);
    v_stack_mF8 = *(uint64_t *)(result + 0x4B0);
    if (((uint32_t)(v_stack_mD8)) != ((uint32_t)(*(uint16_t *)(arg2 + 0x8)))) goto loc_0089D4DE;
    v_stack_m88 = v_stack_mD0 + (uint32_t)((uint32_t)(v_stack_mD8)) * 1;
    if ((uint32_t)((uint32_t)((uint32_t)(v_stack_mD8))) == 0) goto loc_0089DAD5;
    result = RtlCompareMemory(v_stack_mD0, *(uint64_t *)(arg2 + 0x10), (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_mD8)))), v_stack_mD8);
    if (result == ((uint32_t)((uint32_t)(v_stack_mD8)))) goto loc_0089DA02;
    result = (result) >> (1);
    result = (result) + (result);
    Arg3 = (v_stack_mD0) + (result);
    local_r15 = (*(uint64_t *)(arg2 + 0x10)) + (result);
loc_0089D9E5:
    if (Arg3 >= v_stack_m88) goto loc_0089DA02;
    if (((uint16_t)(*(uint16_t *)(Arg3))) != ((uint16_t)(*(uint16_t *)(local_r15)))) goto loc_0089DA25;
loc_0089D9F8:
    Arg3 = (Arg3) + (2);
    local_r15 = (local_r15) + (2);
    goto loc_0089D9E5;
loc_0089DA02:
    v_stack_m128 = *(uint64_t *)(local_rsi + 0x8);
    *(uint64_t *)(arg11 + 0x8) = result;
    if (*(uint64_t *)(local_rsi + 0x8) != 0) goto loc_0089CFFD;
    goto loc_0089D3E0;
loc_0089DA25:
    if (((uint32_t)(*(uint16_t *)(Arg3))) < 97) goto loc_0089DA36;
    if (((uint32_t)(*(uint16_t *)(Arg3))) > 122) goto loc_0089DA56;
    Arg4 = (uint16_t)((*(uint16_t *)(Arg3)) - (32));
loc_0089DA36:
    if (((uint32_t)(*(uint16_t *)(local_r15))) < 97) goto loc_0089DA47;
    if (((uint32_t)(*(uint16_t *)(local_r15))) > 122) goto loc_0089DA94;
    local_r10 = (uint16_t)((*(uint16_t *)(local_r15)) - (32));
loc_0089DA47:
    if (((uint16_t)(Arg4)) == ((uint16_t)(local_r10))) goto loc_0089D9F8;
loc_0089DA4D:
    goto loc_0089D4DE;
loc_0089DA56:
    if (v_stack_mC8 == 0) goto loc_0089DA36;
    if (((uint16_t)(Arg4)) < 192) goto loc_0089DA36;
    result = (Arg4) >> (8);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) & (15));
    result = (uint32_t)(((uint32_t)((uint32_t)(Arg4))) >> (4));
    result = (uint32_t)((result) & (15));
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_mC8 + result * 2)) + ((uint32_t)(result)));
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_mC8 + Arg1 * 2)) + ((uint32_t)(Arg2)));
    Arg4 = (uint16_t)((Arg4) + (*(uint16_t *)(v_stack_mC8 + Arg1 * 2)));
    goto loc_0089DA36;
loc_0089DA94:
    if (v_stack_mC8 == 0) goto loc_0089DA47;
    if (((uint16_t)(local_r10)) < 192) goto loc_0089DA47;
    result = (local_r10) >> (8);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) & (15));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) >> (4));
    result = (uint32_t)((result) & (15));
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_mC8 + result * 2)) + ((uint32_t)(result)));
    Arg1 = (uint32_t)((*(uint16_t *)(v_stack_mC8 + Arg1 * 2)) + ((uint32_t)(Arg2)));
    local_r10 = (uint16_t)((local_r10) + (*(uint16_t *)(v_stack_mC8 + Arg1 * 2)));
    goto loc_0089DA47;
loc_0089DAD5:
    result = memcmp(Arg1, Arg2, (uint32_t)(v_stack_m128), Arg4);
    if ((uint32_t)(result) == 0) goto loc_0089DA02;
    goto loc_0089DA4D;
loc_0089DAE7:
    result = ExfReleasePushLockShared(local_rsi + 296, Arg2, (uint32_t)(v_stack_m128), Arg4);
    goto loc_0089D491;
loc_0089DAF8:
    result = ObfDereferenceObjectWithTag(v_stack_mC8, (uint32_t)(0x554C624FULL), (uint32_t)(v_stack_m128), Arg4);
    goto loc_0089CB68;
loc_0089DB0A:
    goto loc_0089C013;
loc_0089DB16:
    Arg2 = 0;
    result = ExfTryAcquirePushLockSharedEx(v_stack_mC8 + 296, Arg2, (uint32_t)(v_stack_m128), Arg4);
    if ((uint8_t)(result) == 0) goto loc_0089DB8E;
    goto loc_0089D470;
loc_0089DB32:
    goto loc_0089C122;
loc_0089DB3B:
    result = ObDereferenceObjectDeferDelete(result, Arg2, (uint32_t)(v_stack_m128), Arg4);
    goto loc_0089CCAD;
loc_0089DB48:
    if (sign_flag) goto loc_0089D205;
    goto loc_0089D201;
loc_0089DB5E:
    Arg2 = 0;
    result = ObReferenceObjectByPointer(Arg8, Arg2, v_stack_p20, Arg5);
    if (sign_flag) goto loc_0089DD9F;
    *(uint64_t *)(arg13) = Arg8;
    goto loc_0089DD9F;
loc_0089DB8E:
    if (0 != 0) goto loc_0089DCAB;
loc_0089DB97:
    result = ObfReferenceObjectWithTag(v_stack_mC8, (uint32_t)(0x554C624FULL), v_stack_p20, Arg5);
    Arg1 = 0;
    result = 17;
    if (!(condition_is_equal)) {
        Arg1 = *(uint64_t *)(arg11) + 296;
        result = ExfReleasePushLockShared(Arg1, (uint32_t)(0x554C624FULL), v_stack_p20, Arg5);
    }
    result = KeAbPostRelease(*(uint64_t *)(arg11) + 296, (uint32_t)(0x554C624FULL), v_stack_p20, Arg5);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_stack_mC8 + 296, Arg2, Arg3, Arg5);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = v_stack_mC8 + 296;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = v_stack_mC8 + 296;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    goto loc_0089D49F;
loc_0089DC21:
    goto loc_0089CC5E;
loc_0089DC2A:
    Arg2 = 0;
    result = ObReferenceObjectByPointer(v_stack_mC8, Arg2, v_stack_p20, Arg5);
    if (sign_flag) goto loc_0089DD9F;
    *(uint64_t *)(arg13) = v_stack_mC8;
    goto loc_0089DD9F;
loc_0089DC5A:
    result = ObDereferenceDeviceMap(result, 14, v_stack_p20, Arg5);
    goto loc_0089C334;
loc_0089DC6C:
    Arg2 = (uint32_t)(((uint32_t)(v_stack_mE4)) & ((uint32_t)(result)));
    v_stack_mE4 = (uint32_t)(Arg2);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg10 + 0x18))))) & ((uint32_t)(Arg2)));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(*(uint32_t *)(arg10 + 0x18))))) goto loc_0089C077;
    result = ObfDereferenceObject(v_stack_mB8, Arg2, Arg10, Arg5);
    goto loc_0089DD9F;
loc_0089DC9E:
    result = ExfReleasePushLockShared(result, Arg2, Arg10, Arg5);
    goto loc_0089D6AE;
loc_0089DCAB:
    result = KeAbPostReleaseEx(v_stack_mC8 + 296, *(uint64_t *)(arg11), Arg10, Arg5);
    goto loc_0089DB97;
loc_0089DCBF:
    v_stack_m188 = (uint32_t)((uint32_t)(v_stack_p18));
    result = guard_dispatch_icall(v_stack_mC8 + 296, *(uint64_t *)(arg11), Arg10, Arg5);
loc_0089DCD1:
    goto loc_0089C763;
loc_0089DCDC:
    result = (v_stack_p20) + (16);
    v_stack_m68 = *(uint64_t *)(arg11);
    v_stack_m70 = result;
    v_stack_m60 = (uint32_t)(v_stack_p18);
    result = SeSetLearningModeObjectInformation(v_stack_m80, *(uint64_t *)(arg11), Arg10, Arg5);
    goto loc_0089C8DE;
loc_0089DD17:
    v_stack_mFC = (uint32_t)((uint32_t)(0xC0000034ULL));
    goto loc_0089D247;
loc_0089DD24:
    goto loc_0089C995;
loc_0089DD2F:
    if ((((uint8_t)(result)) & (6)) != 0) goto loc_0089D419;
    Arg1 = (Arg10) + (32);
    result = RtlIsSandboxedToken(Arg1, v_stack_m144, v_stack_m130, v_stack_m138);
    local_r14 = (uint32_t)((result) | (2));
loc_0089DD5F:
    if ((((uint8_t)(local_r14)) & (2)) == 0) goto loc_0089D42F;
    goto loc_0089D428;
loc_0089DD6E:
    result = ObDereferenceObjectDeferDeleteWithTag(*(uint64_t *)(arg11), (uint32_t)(0x554C624FULL), v_stack_m130, v_stack_m138);
    goto loc_0089D4AD;
loc_0089DD81:
    v_stack_m188 = (uint32_t)((uint32_t)(v_stack_p18));
    result = guard_dispatch_icall(*(uint64_t *)(arg11), (uint32_t)(0x554C624FULL), v_stack_m130, v_stack_m138);
    goto loc_0089DCD1;
loc_0089DD98:
    *(uint32_t *)((uint32_t)(0x554C624FULL)) = (uint32_t)(*(uint64_t *)(arg11));
    goto loc_0089CD1B;
loc_0089DD9F:
    local_rsp = (local_rsp) + (360);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `16` | `R` |
| `Arg2` | `+ 0x0` | `128` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x10` | `64` | `R` |
| `Arg4` | `+ 0x42` | `8` | `R` |
| `Arg10` | `+ 0xC` | `32` | `R` |
| `Arg10` | `+ 0x18` | `32` | `R` |
| `Arg11` | `+ 0x0` | `8` | `R` |
| `Arg11` | `+ 0x0` | `8` | `W` |
| `Arg11` | `+ 0x0` | `32` | `R` |
| `Arg11` | `+ 0x0` | `32` | `W` |
| `Arg11` | `+ 0x0` | `64` | `R` |
| `Arg11` | `+ 0x0` | `64` | `W` |
| `Arg11` | `+ 0x0` | `128` | `R` |
| `Arg11` | `+ 0x8` | `64` | `W` |
| `Arg11` | `+ 0x10` | `64` | `R` |
| `Arg11` | `+ 0x10` | `64` | `W` |
| `Arg11` | `+ 0x14` | `64` | `R` |
| `Arg11` | `+ 0x15` | `8` | `W` |
| `Arg11` | `+ 0x16` | `8` | `R` |
| `Arg11` | `+ 0x16` | `8` | `W` |
| `Arg13` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0089BE90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
