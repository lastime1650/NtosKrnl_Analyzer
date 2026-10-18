# NtNotifyChangeMultipleKeys

- RVA: `0x009DC6B0`–`0x009DD302` (길이 `3,154` bytes)
- VA: `0x00000001409DC6B0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A3778`
- 디코드: `759`개 명령, `3,154/3,154` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **91**; 고유 호출 대상: **34**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x009DC747` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x009DC75E` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (function, `0x003FBE70`)
- `0x009DC763` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (function, `0x00BC9400`)
- `0x009DC778` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)
- `0x009DC84C` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x009DC861` → [ProbeForWrite](../8E/ProbeForWrite_function_008E91C0.md) (function, `0x008E91C0`)
- `0x009DC8A6` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (function, `0x00BC9880`)
- `0x009DC8B3` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)
- `0x009DC8D7` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (function, `0x00BC9880`)
- `0x009DC8E4` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)
- `0x009DC92E` → [CmObReferenceObjectByHandle](../../pagecmrc/BC/CmObReferenceObjectByHandle_function_00BC9350.md) (function, `0x00BC9350`)
- `0x009DC959` → [CmpInitializeParseContext](../87/CmpInitializeParseContext_function_008767F0.md) (function, `0x008767F0`)
- `0x009DC989` → [CmObReferenceObjectByName](../../pagecmrc/BC/CmObReferenceObjectByName_function_00BC9E94.md) (function, `0x00BC9E94`)
- `0x009DC99A` → [CmpCleanupParseContext](../87/CmpCleanupParseContext_function_00876910.md) (function, `0x00876910`)
- `0x009DC9C6` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009DC9EB` → [CmpAllocatePostBlock](../AA/CmpAllocatePostBlock_function_00AA77F8.md) (function, `0x00AA77F8`)
- `0x009DCA06` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009DCA27` → [CmpAllocatePostBlock](../AA/CmpAllocatePostBlock_function_00AA77F8.md) (function, `0x00AA77F8`)
- `0x009DCA3F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009DCA47` → [CmpFreePostBlock](../84/CmpFreePostBlock_function_00848560.md) (function, `0x00848560`)
- `0x009DCA97` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x009DCAB5` → [CmpFreePostBlock](../84/CmpFreePostBlock_function_00848560.md) (function, `0x00848560`)
- `0x009DCABD` → [CmpFreePostBlock](../84/CmpFreePostBlock_function_00848560.md) (function, `0x00848560`)
- `0x009DCACA` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (function, `0x00248350`)
- `0x009DCB5B` → [KeInitializeApc](../../text/42/KeInitializeApc_function_00428510.md) (function, `0x00428510`)
- `0x009DCB99` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x009DCBAC` → [CmpLockTwoKcbsShared](../84/CmpLockTwoKcbsShared_function_008485B4.md) (function, `0x008485B4`)
- `0x009DCBB3` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (function, `0x00BC9A1C`)
- `0x009DCBBD` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x009DCBD5` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x009DCBFE` → [CmLockHive](../85/CmLockHive_function_008512B4.md) (function, `0x008512B4`)
- `0x009DCC0B` → [CmLockHive](../85/CmLockHive_function_008512B4.md) (function, `0x008512B4`)
- `0x009DCC22` → [CmLockHive](../85/CmLockHive_function_008512B4.md) (function, `0x008512B4`)
- `0x009DCC2F` → [CmLockHive](../85/CmLockHive_function_008512B4.md) (function, `0x008512B4`)
- `0x009DCC51` → [CmLockHive](../85/CmLockHive_function_008512B4.md) (function, `0x008512B4`)
- `0x009DCC63` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (function, `0x003F3720`)
- `0x009DCC84` → [CmpNotifyChangeKey](../A4/CmpNotifyChangeKey_function_00A43C80.md) (function, `0x00A43C80`)
- `0x009DCC9A` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x009DCCBA` → [CmUnlockHive](../85/CmUnlockHive_function_00851D6C.md) (function, `0x00851D6C`)
- `0x009DCCD7` → [CmUnlockHive](../85/CmUnlockHive_function_00851D6C.md) (function, `0x00851D6C`)
- `0x009DCCE1` → [CmUnlockHive](../85/CmUnlockHive_function_00851D6C.md) (function, `0x00851D6C`)
- `0x009DCCF4` → [CmpUnlockTwoKcbs](../84/CmpUnlockTwoKcbs_function_0084869C.md) (function, `0x0084869C`)
- `0x009DCCFB` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x009DCD00` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x009DCD0F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009DCD21` → [CmpFreePostBlock](../84/CmpFreePostBlock_function_00848560.md) (function, `0x00848560`)
- `0x009DCD41` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (function, `0x0020FA20`)
- `0x009DCD4D` → [CmpFreePostBlock](../84/CmpFreePostBlock_function_00848560.md) (function, `0x00848560`)
- `0x009DCD77` → [CmpNotifyChangeKey](../A4/CmpNotifyChangeKey_function_00A43C80.md) (function, `0x00A43C80`)
- `0x009DCDD2` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x009DCE12` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x009DCE30` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x009DCE50` → [CmUnlockHive](../85/CmUnlockHive_function_00851D6C.md) (function, `0x00851D6C`)
- `0x009DCE6D` → [CmUnlockHive](../85/CmUnlockHive_function_00851D6C.md) (function, `0x00851D6C`)
- `0x009DCE77` → [CmUnlockHive](../85/CmUnlockHive_function_00851D6C.md) (function, `0x00851D6C`)
- `0x009DCE8A` → [CmpUnlockTwoKcbs](../84/CmpUnlockTwoKcbs_function_0084869C.md) (function, `0x0084869C`)
- `0x009DCE91` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x009DCE96` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x009DCEA3` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009DCEBB` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (function, `0x00BC9880`)
- `0x009DCEE4` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x009DCF01` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x009DCF0D` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (function, `0x003F3720`)
- `0x009DCF2E` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x009DCF42` → [Feature_2602282298__private_IsEnabledDeviceUsageNoInline](../../text/66/Feature_2602282298__private_IsEnabledDeviceUsageNoInline_function_0066A3E8.md) (function, `0x0066A3E8`)
- `0x009DD054` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x009DD067` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x009DD06C` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x009DD0C0` → [CmpFreePostBlock](../84/CmpFreePostBlock_function_00848560.md) (function, `0x00848560`)
- `0x009DD0C8` → [CmpFreePostBlock](../84/CmpFreePostBlock_function_00848560.md) (function, `0x00848560`)
- `0x009DD0D2` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x009DD0DE` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (function, `0x003F3720`)
- `0x009DD100` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x009DD114` → [Feature_2602282298__private_IsEnabledDeviceUsageNoInline](../../text/66/Feature_2602282298__private_IsEnabledDeviceUsageNoInline_function_0066A3E8.md) (function, `0x0066A3E8`)
- `0x009DD217` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (function, `0x004F5698`)
- `0x009DD22B` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (function, `0x002503A0`)
- `0x009DD230` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x009DD23D` → [CmpFreePostBlock](../84/CmpFreePostBlock_function_00848560.md) (function, `0x00848560`)
- `0x009DD245` → [CmpFreePostBlock](../84/CmpFreePostBlock_function_00848560.md) (function, `0x00848560`)
- `0x009DD25A` → [CmpFreePostBlock](../84/CmpFreePostBlock_function_00848560.md) (function, `0x00848560`)
- `0x009DD269` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009DD27E` → [CmpUnlockTwoKcbs](../84/CmpUnlockTwoKcbs_function_0084869C.md) (function, `0x0084869C`)
- `0x009DD285` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x009DD28A` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x009DD297` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009DD2A5` → [CmpFreePostBlock](../84/CmpFreePostBlock_function_00848560.md) (function, `0x00848560`)
- `0x009DD2AD` → [CmpFreePostBlock](../84/CmpFreePostBlock_function_00848560.md) (function, `0x00848560`)
- `0x009DD2C0` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)
- `0x009DD2CA` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (function, `0x00BC9880`)
- `0x009DD2D7` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)
- `0x009DD2E9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [ExpWatchProductTypeWork](../6F/ExpWatchProductTypeWork_function_006FFCA0.md) at `0x00700203`
- [ExpWatchProductTypeWork](../6F/ExpWatchProductTypeWork_function_006FFCA0.md) at `0x0070027C`
- [SepAdtOpenRegAndSetupNotification](../7A/SepAdtOpenRegAndSetupNotification_function_007A4A80.md) at `0x007A4B06`
- [SepAdtRegNotificationCallback](../7A/SepAdtRegNotificationCallback_function_007A4B20.md) at `0x007A4B7F`
- [ExpWatchLicenseInfoWork](../7C/ExpWatchLicenseInfoWork_function_007C6DB0.md) at `0x007C718A`
- [WheaInitializeRegChangeNotify](../7D/WheaInitializeRegChangeNotify_function_007D89BC.md) at `0x007D8A30`
- [WheaRegChangeNotifyCallback](../7D/WheaRegChangeNotifyCallback_function_007D8A50.md) at `0x007D8ADB`
- [NtNotifyChangeKey](NtNotifyChangeKey_function_009DC640.md) at `0x009DC69E`

### Static image references
- `0x009DC6C3` → RVA `0x00E0A740` (`.data`; read)
- `0x009DCA70` → RVA `0x00FC6B80` (`ALMOSTRO`; read)
- `0x009DCB1B` → RVA `0x00A64D60` (`AlpcConnectionCleanupProcedure`; read)
- `0x009DCB45` → RVA `0x007E1F90` (`CmpPostApcRunDown`; read)
- `0x009DCB51` → RVA `0x00AF78F0` (`CmpPostApc`; read)
- `0x009DCC5C` → RVA `0x00EF5940` (`.data`; read)
- `0x009DCDC2` → RVA `0x00FC6D20` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **55**
  - `0x009DC747` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x009DC75E` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (`PAGE` → `.text`)
  - `0x009DC763` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (`PAGE` → `PAGECMRC`)
  - `0x009DC778` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
  - `0x009DC8A6` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (`PAGE` → `PAGECMRC`)
  - `0x009DC8B3` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
  - `0x009DC8D7` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (`PAGE` → `PAGECMRC`)
  - `0x009DC8E4` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
  - `0x009DC92E` → [CmObReferenceObjectByHandle](../../pagecmrc/BC/CmObReferenceObjectByHandle_function_00BC9350.md) (`PAGE` → `PAGECMRC`)
  - `0x009DC989` → [CmObReferenceObjectByName](../../pagecmrc/BC/CmObReferenceObjectByName_function_00BC9E94.md) (`PAGE` → `PAGECMRC`)
  - `0x009DC9C6` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009DCA06` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009DCA3F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009DCACA` → [KeResetEvent](../../text/24/KeResetEvent_function_00248350.md) (`PAGE` → `.text`)
  - `0x009DCB5B` → [KeInitializeApc](../../text/42/KeInitializeApc_function_00428510.md) (`PAGE` → `.text`)
  - `0x009DCB99` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x009DCBB3` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (`PAGE` → `PAGECMRC`)
  - `0x009DCBBD` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x009DCBD5` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x009DCC63` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (`PAGE` → `.text`)
  - `0x009DCC9A` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (`PAGE` → `.text`)
  - `0x009DCCFB` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x009DCD00` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x009DCD0F` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009DCD41` → [ObfReferenceObject](../../text/20/ObfReferenceObject_function_0020FA20.md) (`PAGE` → `.text`)
  - `0x009DCDD2` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (`PAGE` → `.text`)
  - `0x009DCE12` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (`PAGE` → `.text`)
  - `0x009DCE30` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (`PAGE` → `.text`)
  - `0x009DCE91` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x009DCE96` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x009DCEA3` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009DCEBB` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (`PAGE` → `PAGECMRC`)
  - `0x009DCEE4` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x009DCF01` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x009DCF0D` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (`PAGE` → `.text`)
  - `0x009DCF2E` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (`PAGE` → `.text`)
  - `0x009DCF42` → [Feature_2602282298__private_IsEnabledDeviceUsageNoInline](../../text/66/Feature_2602282298__private_IsEnabledDeviceUsageNoInline_function_0066A3E8.md) (`PAGE` → `.text`)
  - `0x009DD054` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (`PAGE` → `.text`)
  - `0x009DD067` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (`PAGE` → `.text`)
  - `0x009DD06C` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x009DD0D2` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x009DD0DE` → [ExAcquireFastMutexUnsafe](../../text/3F/ExAcquireFastMutexUnsafe_function_003F3720.md) (`PAGE` → `.text`)
  - `0x009DD100` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (`PAGE` → `.text`)
  - `0x009DD114` → [Feature_2602282298__private_IsEnabledDeviceUsageNoInline](../../text/66/Feature_2602282298__private_IsEnabledDeviceUsageNoInline_function_0066A3E8.md) (`PAGE` → `.text`)
  - `0x009DD217` → [KiLowerIrqlProcessIrqlFlags](../../text/4F/KiLowerIrqlProcessIrqlFlags_function_004F5698.md) (`PAGE` → `.text`)
  - `0x009DD22B` → [ExReleaseFastMutexUnsafe](../../text/25/ExReleaseFastMutexUnsafe_function_002503A0.md) (`PAGE` → `.text`)
  - `0x009DD230` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x009DD269` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009DD285` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x009DD28A` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x009DD297` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009DD2C0` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
  - `0x009DD2CA` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (`PAGE` → `PAGECMRC`)
  - `0x009DD2D7` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
  - `0x009DD2E9` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009DC6B0  40 53                           push rbx
009DC6B2  56                              push rsi
009DC6B3  57                              push rdi
009DC6B4  41 54                           push r12
009DC6B6  41 55                           push r13
009DC6B8  41 56                           push r14
009DC6BA  41 57                           push r15
009DC6BC  48 81 EC 90 02 00 00            sub rsp, 0x290
009DC6C3  48 8B 05 76 E0 42 00            mov rax, qword ptr [rip + 0x42e076]
009DC6CA  48 33 C4                        xor rax, rsp
009DC6CD  48 89 84 24 80 02 00 00         mov qword ptr [rsp + 0x280], rax
009DC6D5  4D 8B F9                        mov r15, r9
009DC6D8  4C 89 8C 24 A0 00 00 00         mov qword ptr [rsp + 0xa0], r9
009DC6E0  4C 89 44 24 78                  mov qword ptr [rsp + 0x78], r8
009DC6E5  44 8B E2                        mov r12d, edx
009DC6E8  48 89 4C 24 58                  mov qword ptr [rsp + 0x58], rcx
009DC6ED  4C 8B B4 24 00 03 00 00         mov r14, qword ptr [rsp + 0x300]
009DC6F5  4C 89 74 24 70                  mov qword ptr [rsp + 0x70], r14
009DC6FA  48 8B BC 24 18 03 00 00         mov rdi, qword ptr [rsp + 0x318]
009DC702  0F 57 C0                        xorps xmm0, xmm0
009DC705  33 C0                           xor eax, eax
009DC707  0F 11 84 24 80 00 00 00         movups xmmword ptr [rsp + 0x80], xmm0
009DC70F  48 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], rax
009DC717  45 33 ED                        xor r13d, r13d
009DC71A  4C 89 6C 24 68                  mov qword ptr [rsp + 0x68], r13
009DC71F  4C 89 6C 24 50                  mov qword ptr [rsp + 0x50], r13
009DC724  41 8B F5                        mov esi, r13d
009DC727  4C 89 AC 24 98 00 00 00         mov qword ptr [rsp + 0x98], r13
009DC72F  C7 44 24 48 01 00 00 00         mov dword ptr [rsp + 0x48], 1
009DC737  33 D2                           xor edx, edx
009DC739  41 B8 D0 01 00 00               mov r8d, 0x1d0
009DC73F  48 8D 8C 24 B0 00 00 00         lea rcx, [rsp + 0xb0]
009DC747  E8 F4 A4 CE FF                  call 0x1406c6c40
009DC74C  40 88 74 24 44                  mov byte ptr [rsp + 0x44], sil
009DC751  4C 89 6C 24 60                  mov qword ptr [rsp + 0x60], r13
009DC756  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
009DC75E  E8 0D F7 A1 FF                  call 0x1403fbe70
009DC763  E8 98 CC 1E 00                  call 0x140bc9400
009DC768  88 44 24 40                     mov byte ptr [rsp + 0x40], al
009DC76C  84 C0                           test al, al
009DC76E  75 17                           jne 0x1409dc787
009DC770  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
009DC778  E8 D3 35 A4 FF                  call 0x14041fd50
009DC77D  B8 89 01 00 C0                  mov eax, 0xc0000189
009DC782  E9 57 0B 00 00                  jmp 0x1409dd2de
009DC787  41 83 FC 01                     cmp r12d, 1
009DC78B  0F 87 46 01 00 00               ja 0x1409dc8d7
009DC791  0F 94 44 24 43                  sete byte ptr [rsp + 0x43]
009DC796  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009DC79F  0F B6 88 32 02 00 00            movzx ecx, byte ptr [rax + 0x232]
009DC7A6  88 4C 24 41                     mov byte ptr [rsp + 0x41], cl
009DC7AA  84 C9                           test cl, cl
009DC7AC  0F 84 0D 01 00 00               je 0x1409dc8bf
009DC7B2  8B 9C 24 08 03 00 00            mov ebx, dword ptr [rsp + 0x308]
009DC7B9  0F BA E3 1C                     bt ebx, 0x1c
009DC7BD  73 33                           jae 0x1409dc7f2
009DC7BF  40 38 B4 24 28 03 00 00         cmp byte ptr [rsp + 0x328], sil
009DC7C7  0F 84 0A 01 00 00               je 0x1409dc8d7
009DC7CD  48 39 B4 24 F0 02 00 00         cmp qword ptr [rsp + 0x2f0], rsi
009DC7D5  0F 85 FC 00 00 00               jne 0x1409dc8d7
009DC7DB  4D 85 FF                        test r15, r15
009DC7DE  0F 84 F3 00 00 00               je 0x1409dc8d7
009DC7E4  BF 04 00 00 00                  mov edi, 4
009DC7E9  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
009DC7ED  E9 0C 01 00 00                  jmp 0x1409dc8fe
009DC7F2  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
009DC7FB  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
009DC802  48 39 B1 10 03 00 00            cmp qword ptr [rcx + 0x310], rsi
009DC809  74 20                           je 0x1409dc82b
009DC80B  0F B7 81 EC 06 00 00            movzx eax, word ptr [rcx + 0x6ec]
009DC812  B9 4C 01 00 00                  mov ecx, 0x14c
009DC817  66 3B C1                        cmp ax, cx
009DC81A  74 0A                           je 0x1409dc826
009DC81C  B9 C4 01 00 00                  mov ecx, 0x1c4
009DC821  66 3B C1                        cmp ax, cx
009DC824  75 05                           jne 0x1409dc82b
009DC826  41 B7 01                        mov r15b, 1
009DC829  EB 03                           jmp 0x1409dc82e
009DC82B  45 32 FF                        xor r15b, r15b
009DC82E  44 88 7C 24 44                  mov byte ptr [rsp + 0x44], r15b
009DC833  41 0F B6 D7                     movzx edx, r15b
009DC837  48 83 F2 01                     xor rdx, 1
009DC83B  48 8D 14 D5 08 00 00 00         lea rdx, [rdx*8 + 8]
009DC843  41 B8 04 00 00 00               mov r8d, 4
009DC849  49 8B CE                        mov rcx, r14
009DC84C  E8 6F C9 F0 FF                  call 0x1408e91c0
009DC851  8B 94 24 20 03 00 00            mov edx, dword ptr [rsp + 0x320]
009DC858  41 B8 04 00 00 00               mov r8d, 4
009DC85E  48 8B CF                        mov rcx, rdi
009DC861  E8 5A C9 F0 FF                  call 0x1408e91c0
009DC866  45 84 FF                        test r15b, r15b
009DC869  74 09                           je 0x1409dc874
009DC86B  49 C7 06 03 01 00 00            mov qword ptr [r14], 0x103
009DC872  EB 0B                           jmp 0x1409dc87f
009DC874  41 C7 06 03 01 00 00            mov dword ptr [r14], 0x103
009DC87B  4D 89 6E 08                     mov qword ptr [r14 + 8], r13
009DC87F  41 BD 02 00 00 00               mov r13d, 2
009DC885  0F B6 4C 24 41                  movzx ecx, byte ptr [rsp + 0x41]
009DC88A  80 BC 24 28 03 00 00 00         cmp byte ptr [rsp + 0x328], 0
009DC892  74 0A                           je 0x1409dc89e
009DC894  41 8B FD                        mov edi, r13d
009DC897  44 89 6C 24 48                  mov dword ptr [rsp + 0x48], r13d
009DC89C  EB 66                           jmp 0x1409dc904
009DC89E  8B 7C 24 48                     mov edi, dword ptr [rsp + 0x48]
009DC8A2  EB 60                           jmp 0x1409dc904
009DC8A4  8B D8                           mov ebx, eax
009DC8A6  E8 D5 CF 1E 00                  call 0x140bc9880
009DC8AB  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
009DC8B3  E8 98 34 A4 FF                  call 0x14041fd50
009DC8B8  8B C3                           mov eax, ebx
009DC8BA  E9 1F 0A 00 00                  jmp 0x1409dd2de
009DC8BF  40 38 B4 24 28 03 00 00         cmp byte ptr [rsp + 0x328], sil
009DC8C7  74 2A                           je 0x1409dc8f3
009DC8C9  BF 03 00 00 00                  mov edi, 3
009DC8CE  89 7C 24 48                     mov dword ptr [rsp + 0x48], edi
009DC8D2  45 85 E4                        test r12d, r12d
009DC8D5  74 20                           je 0x1409dc8f7
009DC8D7  E8 A4 CF 1E 00                  call 0x140bc9880
009DC8DC  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
009DC8E4  E8 67 34 A4 FF                  call 0x14041fd50
009DC8E9  B8 0D 00 00 C0                  mov eax, 0xc000000d
009DC8EE  E9 EB 09 00 00                  jmp 0x1409dd2de
009DC8F3  8B 7C 24 48                     mov edi, dword ptr [rsp + 0x48]
009DC8F7  8B 9C 24 08 03 00 00            mov ebx, dword ptr [rsp + 0x308]
009DC8FE  41 BD 02 00 00 00               mov r13d, 2
009DC904  8B C3                           mov eax, ebx
009DC906  25 0F 00 00 10                  and eax, 0x1000000f
009DC90B  3B D8                           cmp ebx, eax
009DC90D  75 C8                           jne 0x1409dc8d7
009DC90F  33 D2                           xor edx, edx
009DC911  48 89 54 24 28                  mov qword ptr [rsp + 0x28], rdx
009DC916  48 8D 44 24 68                  lea rax, [rsp + 0x68]
009DC91B  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009DC920  44 0F B6 C9                     movzx r9d, cl
009DC924  BA 10 00 00 00                  mov edx, 0x10
009DC929  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
009DC92E  E8 1D CA 1E 00                  call 0x140bc9350
009DC933  8B D8                           mov ebx, eax
009DC935  85 C0                           test eax, eax
009DC937  0F 88 8D 09 00 00               js 0x1409dd2ca
009DC93D  33 DB                           xor ebx, ebx
009DC93F  44 8B FB                        mov r15d, ebx
009DC942  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
009DC947  41 83 FC 01                     cmp r12d, 1
009DC94B  0F 85 84 00 00 00               jne 0x1409dc9d5
009DC951  48 8D 8C 24 B0 00 00 00         lea rcx, [rsp + 0xb0]
009DC959  E8 92 9E E9 FF                  call 0x1408767f0
009DC95E  48 8D 44 24 58                  lea rax, [rsp + 0x58]
009DC963  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
009DC968  48 8D 84 24 B0 00 00 00         lea rax, [rsp + 0xb0]
009DC970  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009DC975  0F B6 44 24 41                  movzx eax, byte ptr [rsp + 0x41]
009DC97A  88 44 24 20                     mov byte ptr [rsp + 0x20], al
009DC97E  33 D2                           xor edx, edx
009DC980  44 8D 43 10                     lea r8d, [rbx + 0x10]
009DC984  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
009DC989  E8 06 D5 1E 00                  call 0x140bc9e94
009DC98E  8B D8                           mov ebx, eax
009DC990  33 D2                           xor edx, edx
009DC992  48 8D 8C 24 B0 00 00 00         lea rcx, [rsp + 0xb0]
009DC99A  E8 71 9F E9 FF                  call 0x140876910
009DC99F  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
009DC9A4  85 DB                           test ebx, ebx
009DC9A6  0F 88 0B 09 00 00               js 0x1409dd2b7
009DC9AC  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
009DC9B1  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
009DC9B5  49 8B 56 08                     mov rdx, qword ptr [r14 + 8]
009DC9B9  48 8B 40 20                     mov rax, qword ptr [rax + 0x20]
009DC9BD  48 39 42 20                     cmp qword ptr [rdx + 0x20], rax
009DC9C1  75 19                           jne 0x1409dc9dc
009DC9C3  49 8B CF                        mov rcx, r15
009DC9C6  E8 85 C9 91 FF                  call 0x1402f9350
009DC9CB  BB 0D 00 00 C0                  mov ebx, 0xc000000d
009DC9D0  E9 E2 08 00 00                  jmp 0x1409dd2b7
009DC9D5  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
009DC9DA  EB 02                           jmp 0x1409dc9de
009DC9DC  33 DB                           xor ebx, ebx
009DC9DE  45 33 C9                        xor r9d, r9d
009DC9E1  45 33 C0                        xor r8d, r8d
009DC9E4  BA 00 00 01 00                  mov edx, 0x10000
009DC9E9  8B CF                           mov ecx, edi
009DC9EB  E8 08 AE 0C 00                  call 0x140aa77f8
009DC9F0  48 8B F8                        mov rdi, rax
009DC9F3  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
009DC9F8  48 85 C0                        test rax, rax
009DC9FB  75 18                           jne 0x1409dca15
009DC9FD  41 83 FC 01                     cmp r12d, 1
009DCA01  75 08                           jne 0x1409dca0b
009DCA03  49 8B CF                        mov rcx, r15
009DCA06  E8 45 C9 91 FF                  call 0x1402f9350
009DCA0B  BB 9A 00 00 C0                  mov ebx, 0xc000009a
009DCA10  E9 A2 08 00 00                  jmp 0x1409dd2b7
009DCA15  41 83 FC 01                     cmp r12d, 1
009DCA19  75 3B                           jne 0x1409dca56
009DCA1B  4C 8B CF                        mov r9, rdi
009DCA1E  4D 8B C7                        mov r8, r15
009DCA21  33 D2                           xor edx, edx
009DCA23  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
009DCA27  E8 CC AD 0C 00                  call 0x140aa77f8
009DCA2C  48 8B F0                        mov rsi, rax
009DCA2F  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
009DCA37  48 85 C0                        test rax, rax
009DCA3A  75 1A                           jne 0x1409dca56
009DCA3C  49 8B CF                        mov rcx, r15
009DCA3F  E8 0C C9 91 FF                  call 0x1402f9350
009DCA44  48 8B CF                        mov rcx, rdi
009DCA47  E8 14 BB E6 FF                  call 0x140848560
009DCA4C  BB 9A 00 00 C0                  mov ebx, 0xc000009a
009DCA51  E9 61 08 00 00                  jmp 0x1409dd2b7
009DCA56  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
009DCA5A  83 F9 01                        cmp ecx, 1
009DCA5D  0F 84 31 01 00 00               je 0x1409dcb94
009DCA63  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
009DCA6B  48 85 C0                        test rax, rax
009DCA6E  74 65                           je 0x1409dcad5
009DCA70  4C 8B 05 09 A1 5E 00            mov r8, qword ptr [rip + 0x5ea109]
009DCA77  48 89 5C 24 50                  mov qword ptr [rsp + 0x50], rbx
009DCA7C  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
009DCA81  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
009DCA86  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
009DCA8B  44 0F B6 4C 24 41               movzx r9d, byte ptr [rsp + 0x41]
009DCA91  41 8B D5                        mov edx, r13d
009DCA94  48 8B C8                        mov rcx, rax
009DCA97  E8 14 C3 E8 FF                  call 0x140868db0
009DCA9C  8B D8                           mov ebx, eax
009DCA9E  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
009DCAA3  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
009DCAA8  85 C0                           test eax, eax
009DCAAA  79 1B                           jns 0x1409dcac7
009DCAAC  41 83 FC 01                     cmp r12d, 1
009DCAB0  75 08                           jne 0x1409dcaba
009DCAB2  48 8B CE                        mov rcx, rsi
009DCAB5  E8 A6 BA E6 FF                  call 0x140848560
009DCABA  48 8B CF                        mov rcx, rdi
009DCABD  E8 9E BA E6 FF                  call 0x140848560
009DCAC2  E9 F0 07 00 00                  jmp 0x1409dd2b7
009DCAC7  48 8B D9                        mov rbx, rcx
009DCACA  E8 81 B8 86 FF                  call 0x140248350
009DCACF  8B 4C 24 48                     mov ecx, dword ptr [rsp + 0x48]
009DCAD3  EB 05                           jmp 0x1409dcada
009DCAD5  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
009DCADA  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
009DCADE  83 F9 02                        cmp ecx, 2
009DCAE1  0F 85 85 00 00 00               jne 0x1409dcb6c
009DCAE7  48 8B 4C 24 70                  mov rcx, qword ptr [rsp + 0x70]
009DCAEC  48 89 48 68                     mov qword ptr [rax + 0x68], rcx
009DCAF0  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
009DCAF4  48 89 58 08                     mov qword ptr [rax + 8], rbx
009DCAF8  44 0F B6 4C 24 41               movzx r9d, byte ptr [rsp + 0x41]
009DCAFE  48 8B 84 24 F0 02 00 00         mov rax, qword ptr [rsp + 0x2f0]
009DCB06  48 85 C0                        test rax, rax
009DCB09  BA 00 00 00 00                  mov edx, 0
009DCB0E  44 0F 44 CA                     cmove r9d, edx
009DCB12  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
009DCB1B  4C 8D 05 3E 82 08 00            lea r8, [rip + 0x8823e]
009DCB22  4C 0F 45 C0                     cmovne r8, rax
009DCB26  48 8B 4F 40                     mov rcx, qword ptr [rdi + 0x40]
009DCB2A  48 83 C1 10                     add rcx, 0x10
009DCB2E  48 8B 84 24 F8 02 00 00         mov rax, qword ptr [rsp + 0x2f8]
009DCB36  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
009DCB3B  44 88 4C 24 30                  mov byte ptr [rsp + 0x30], r9b
009DCB40  4C 89 44 24 28                  mov qword ptr [rsp + 0x28], r8
009DCB45  48 8D 05 44 54 E0 FF            lea rax, [rip - 0x1fabbc]
009DCB4C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
009DCB51  4C 8D 0D 98 AD 11 00            lea r9, [rip + 0x11ad98]
009DCB58  45 8B C5                        mov r8d, r13d
009DCB5B  E8 B0 B9 A4 FF                  call 0x140428510
009DCB60  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
009DCB65  4C 8B 7C 24 58                  mov r15, qword ptr [rsp + 0x58]
009DCB6A  EB 2D                           jmp 0x1409dcb99
009DCB6C  48 89 18                        mov qword ptr [rax], rbx
009DCB6F  83 F9 04                        cmp ecx, 4
009DCB72  74 25                           je 0x1409dcb99
009DCB74  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
009DCB78  48 8B 8C 24 F0 02 00 00         mov rcx, qword ptr [rsp + 0x2f0]
009DCB80  48 89 48 08                     mov qword ptr [rax + 8], rcx
009DCB84  48 8B 4F 40                     mov rcx, qword ptr [rdi + 0x40]
009DCB88  8B 84 24 F8 02 00 00            mov eax, dword ptr [rsp + 0x2f8]
009DCB8F  89 41 10                        mov dword ptr [rcx + 0x10], eax
009DCB92  EB 05                           jmp 0x1409dcb99
009DCB94  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
009DCB99  E8 96 CF 1E 00                  call 0x140bc9b34
009DCB9E  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
009DCBA2  41 83 FC 01                     cmp r12d, 1
009DCBA6  75 0B                           jne 0x1409dcbb3
009DCBA8  49 8B 57 08                     mov rdx, qword ptr [r15 + 8]
009DCBAC  E8 03 BA E6 FF                  call 0x1408485b4
009DCBB1  EB 05                           jmp 0x1409dcbb8
009DCBB3  E8 64 CE 1E 00                  call 0x140bc9a1c
009DCBB8  33 D2                           xor edx, edx
009DCBBA  49 8B CE                        mov rcx, r14
009DCBBD  E8 BE C8 1E 00                  call 0x140bc9480
009DCBC2  84 C0                           test al, al
009DCBC4  0F 85 A6 06 00 00               jne 0x1409dd270
009DCBCA  41 83 FC 01                     cmp r12d, 1
009DCBCE  75 79                           jne 0x1409dcc49
009DCBD0  33 D2                           xor edx, edx
009DCBD2  49 8B CF                        mov rcx, r15
009DCBD5  E8 A6 C8 1E 00                  call 0x140bc9480
009DCBDA  84 C0                           test al, al
009DCBDC  0F 85 8E 06 00 00               jne 0x1409dd270
009DCBE2  45 3B E4                        cmp r12d, r12d
009DCBE5  75 62                           jne 0x1409dcc49
009DCBE7  49 8B 46 08                     mov rax, qword ptr [r14 + 8]
009DCBEB  48 8B 48 20                     mov rcx, qword ptr [rax + 0x20]
009DCBEF  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
009DCBF3  48 8B 50 20                     mov rdx, qword ptr [rax + 0x20]
009DCBF7  48 3B CA                        cmp rcx, rdx
009DCBFA  74 4D                           je 0x1409dcc49
009DCBFC  73 21                           jae 0x1409dcc1f
009DCBFE  E8 B1 46 E7 FF                  call 0x1408512b4
009DCC03  49 8B 4F 08                     mov rcx, qword ptr [r15 + 8]
009DCC07  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
009DCC0B  E8 A4 46 E7 FF                  call 0x1408512b4
009DCC10  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
009DCC14  48 8B 40 20                     mov rax, qword ptr [rax + 0x20]
009DCC18  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
009DCC1D  EB 3D                           jmp 0x1409dcc5c
009DCC1F  48 8B CA                        mov rcx, rdx
009DCC22  E8 8D 46 E7 FF                  call 0x1408512b4
009DCC27  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
009DCC2B  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
009DCC2F  E8 80 46 E7 FF                  call 0x1408512b4
009DCC34  41 BD 03 00 00 00               mov r13d, 3
009DCC3A  49 8B 47 08                     mov rax, qword ptr [r15 + 8]
009DCC3E  48 8B 40 20                     mov rax, qword ptr [rax + 0x20]
009DCC42  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
009DCC47  EB 13                           jmp 0x1409dcc5c
009DCC49  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
009DCC4D  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
009DCC51  E8 5E 46 E7 FF                  call 0x1408512b4
009DCC56  41 BD 01 00 00 00               mov r13d, 1
009DCC5C  48 8D 0D DD 8C 51 00            lea rcx, [rip + 0x518cdd]
009DCC63  E8 B8 6A A1 FF                  call 0x1403f3720
009DCC68  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
009DCC6D  44 0F B6 8C 24 10 03 00 00      movzx r9d, byte ptr [rsp + 0x310]
009DCC76  44 8B 84 24 08 03 00 00         mov r8d, dword ptr [rsp + 0x308]
009DCC7E  48 8B D7                        mov rdx, rdi
009DCC81  49 8B CE                        mov rcx, r14
009DCC84  E8 F7 6F 06 00                  call 0x140a43c80
009DCC89  8B D8                           mov ebx, eax
009DCC8B  85 C0                           test eax, eax
009DCC8D  0F 89 98 00 00 00               jns 0x1409dcd2b
009DCC93  48 8D 0D A6 8C 51 00            lea rcx, [rip + 0x518ca6]
009DCC9A  E8 01 37 87 FF                  call 0x1402503a0
009DCC9F  41 83 FD 01                     cmp r13d, 1
009DCCA3  75 0A                           jne 0x1409dccaf
009DCCA5  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
009DCCA9  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
009DCCAD  EB 32                           jmp 0x1409dcce1
009DCCAF  41 83 FD 02                     cmp r13d, 2
009DCCB3  75 14                           jne 0x1409dccc9
009DCCB5  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
009DCCBA  E8 AD 50 E7 FF                  call 0x140851d6c
009DCCBF  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
009DCCC3  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
009DCCC7  EB 18                           jmp 0x1409dcce1
009DCCC9  41 83 FD 03                     cmp r13d, 3
009DCCCD  75 17                           jne 0x1409dcce6
009DCCCF  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
009DCCD3  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
009DCCD7  E8 90 50 E7 FF                  call 0x140851d6c
009DCCDC  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
009DCCE1  E8 86 50 E7 FF                  call 0x140851d6c
009DCCE6  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
009DCCEA  41 83 FC 01                     cmp r12d, 1
009DCCEE  75 0B                           jne 0x1409dccfb
009DCCF0  49 8B 57 08                     mov rdx, qword ptr [r15 + 8]
009DCCF4  E8 A3 B9 E6 FF                  call 0x14084869c
009DCCF9  EB 05                           jmp 0x1409dcd00
009DCCFB  E8 C0 C5 1E 00                  call 0x140bc92c0
009DCD00  E8 7F CD 1E 00                  call 0x140bc9a84
009DCD05  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
009DCD0A  48 85 C9                        test rcx, rcx
009DCD0D  74 05                           je 0x1409dcd14
009DCD0F  E8 3C C6 91 FF                  call 0x1402f9350
009DCD14  41 83 FC 01                     cmp r12d, 1
009DCD18  0F 85 99 05 00 00               jne 0x1409dd2b7
009DCD1E  48 8B CE                        mov rcx, rsi
009DCD21  E8 3A B8 E6 FF                  call 0x140848560
009DCD26  E9 8C 05 00 00                  jmp 0x1409dd2b7
009DCD2B  0F B6 44 24 43                  movzx eax, byte ptr [rsp + 0x43]
009DCD30  88 44 24 42                     mov byte ptr [rsp + 0x42], al
009DCD34  41 83 FC 01                     cmp r12d, 1
009DCD38  0F 85 EB 00 00 00               jne 0x1409dce29
009DCD3E  49 8B CF                        mov rcx, r15
009DCD41  E8 DA 2C 83 FF                  call 0x14020fa20
009DCD46  85 DB                           test ebx, ebx
009DCD48  75 11                           jne 0x1409dcd5b
009DCD4A  48 8B CE                        mov rcx, rsi
009DCD4D  E8 0E B8 E6 FF                  call 0x140848560
009DCD52  88 5C 24 42                     mov byte ptr [rsp + 0x42], bl
009DCD56  E9 CE 00 00 00                  jmp 0x1409dce29
009DCD5B  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
009DCD60  44 0F B6 8C 24 10 03 00 00      movzx r9d, byte ptr [rsp + 0x310]
009DCD69  44 8B 84 24 08 03 00 00         mov r8d, dword ptr [rsp + 0x308]
009DCD71  48 8B D6                        mov rdx, rsi
009DCD74  49 8B CF                        mov rcx, r15
009DCD77  E8 04 6F 06 00                  call 0x140a43c80
009DCD7C  8B D8                           mov ebx, eax
009DCD7E  0F B6 44 24 43                  movzx eax, byte ptr [rsp + 0x43]
009DCD83  88 44 24 42                     mov byte ptr [rsp + 0x42], al
009DCD87  85 DB                           test ebx, ebx
009DCD89  0F 89 9A 00 00 00               jns 0x1409dce29
009DCD8F  48 8B 0F                        mov rcx, qword ptr [rdi]
009DCD92  48 8B 47 08                     mov rax, qword ptr [rdi + 8]
009DCD96  48 39 79 08                     cmp qword ptr [rcx + 8], rdi
009DCD9A  0F 85 B0 04 00 00               jne 0x1409dd250
009DCDA0  48 39 38                        cmp qword ptr [rax], rdi
009DCDA3  0F 85 A7 04 00 00               jne 0x1409dd250
009DCDA9  48 89 08                        mov qword ptr [rax], rcx
009DCDAC  48 89 41 08                     mov qword ptr [rcx + 8], rax
009DCDB0  45 0F 20 C0                     mov r8, cr8
009DCDB4  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
009DCDB9  B8 01 00 00 00                  mov eax, 1
009DCDBE  44 0F 22 C0                     mov cr8, rax
009DCDC2  83 3D 57 9F 5E 00 00            cmp dword ptr [rip + 0x5e9f57], 0
009DCDC9  74 11                           je 0x1409dcddc
009DCDCB  0F B6 D0                        movzx edx, al
009DCDCE  41 0F B6 C8                     movzx ecx, r8b
009DCDD2  E8 25 89 B1 FF                  call 0x1404f56fc
009DCDD7  4C 8B 44 24 58                  mov r8, qword ptr [rsp + 0x58]
009DCDDC  48 8D 47 10                     lea rax, [rdi + 0x10]
009DCDE0  48 8B 10                        mov rdx, qword ptr [rax]
009DCDE3  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
009DCDE7  48 39 42 08                     cmp qword ptr [rdx + 8], rax
009DCDEB  0F 85 5F 04 00 00               jne 0x1409dd250
009DCDF1  48 39 01                        cmp qword ptr [rcx], rax
009DCDF4  0F 85 56 04 00 00               jne 0x1409dd250
009DCDFA  48 89 11                        mov qword ptr [rcx], rdx
009DCDFD  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
009DCE01  83 3D 18 9F 5E 00 00            cmp dword ptr [rip + 0x5e9f18], 0
009DCE08  74 0D                           je 0x1409dce17
009DCE0A  44 0F 20 C1                     mov rcx, cr8
009DCE0E  41 0F B6 D0                     movzx edx, r8b
009DCE12  E8 81 88 B1 FF                  call 0x1404f5698
009DCE17  0F B6 44 24 58                  movzx eax, byte ptr [rsp + 0x58]
009DCE1C  44 0F 22 C0                     mov cr8, rax
009DCE20  0F B6 44 24 43                  movzx eax, byte ptr [rsp + 0x43]
009DCE25  88 44 24 42                     mov byte ptr [rsp + 0x42], al
009DCE29  48 8D 0D 10 8B 51 00            lea rcx, [rip + 0x518b10]
009DCE30  E8 6B 35 87 FF                  call 0x1402503a0
009DCE35  41 83 FD 01                     cmp r13d, 1
009DCE39  75 0A                           jne 0x1409dce45
009DCE3B  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
009DCE3F  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
009DCE43  EB 32                           jmp 0x1409dce77
009DCE45  41 83 FD 02                     cmp r13d, 2
009DCE49  75 14                           jne 0x1409dce5f
009DCE4B  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
009DCE50  E8 17 4F E7 FF                  call 0x140851d6c
009DCE55  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
009DCE59  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
009DCE5D  EB 18                           jmp 0x1409dce77
009DCE5F  41 83 FD 03                     cmp r13d, 3
009DCE63  75 17                           jne 0x1409dce7c
009DCE65  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
009DCE69  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
009DCE6D  E8 FA 4E E7 FF                  call 0x140851d6c
009DCE72  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
009DCE77  E8 F0 4E E7 FF                  call 0x140851d6c
009DCE7C  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
009DCE80  41 83 FC 01                     cmp r12d, 1
009DCE84  75 0B                           jne 0x1409dce91
009DCE86  49 8B 57 08                     mov rdx, qword ptr [r15 + 8]
009DCE8A  E8 0D B8 E6 FF                  call 0x14084869c
009DCE8F  EB 05                           jmp 0x1409dce96
009DCE91  E8 2A C4 1E 00                  call 0x140bc92c0
009DCE96  E8 E9 CB 1E 00                  call 0x140bc9a84
009DCE9B  4D 85 FF                        test r15, r15
009DCE9E  74 08                           je 0x1409dcea8
009DCEA0  49 8B CF                        mov rcx, r15
009DCEA3  E8 A8 C4 91 FF                  call 0x1402f9350
009DCEA8  85 DB                           test ebx, ebx
009DCEAA  0F 88 A7 03 00 00               js 0x1409dd257
009DCEB0  83 7C 24 48 01                  cmp dword ptr [rsp + 0x48], 1
009DCEB5  0F 85 FC 03 00 00               jne 0x1409dd2b7
009DCEBB  E8 C0 C9 1E 00                  call 0x140bc9880
009DCEC0  45 32 E4                        xor r12b, r12b
009DCEC3  44 88 64 24 40                  mov byte ptr [rsp + 0x40], r12b
009DCEC8  44 88 64 24 43                  mov byte ptr [rsp + 0x43], r12b
009DCECD  45 33 ED                        xor r13d, r13d
009DCED0  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
009DCED5  41 B1 01                        mov r9b, 1
009DCED8  44 0F B6 44 24 41               movzx r8d, byte ptr [rsp + 0x41]
009DCEDE  33 D2                           xor edx, edx
009DCEE0  48 8B 4F 40                     mov rcx, qword ptr [rdi + 0x40]
009DCEE4  E8 C7 17 83 FF                  call 0x14020e6b0
009DCEE9  8B D8                           mov ebx, eax
009DCEEB  3D 01 01 00 00                  cmp eax, 0x101
009DCEF0  0F 84 DC 01 00 00               je 0x1409dd0d2
009DCEF6  3D C0 00 00 00                  cmp eax, 0xc0
009DCEFB  0F 84 D1 01 00 00               je 0x1409dd0d2
009DCF01  E8 2E CC 1E 00                  call 0x140bc9b34
009DCF06  48 8D 0D 33 8A 51 00            lea rcx, [rip + 0x518a33]
009DCF0D  E8 0E 68 A1 FF                  call 0x1403f3720
009DCF12  44 0F 20 C3                     mov rbx, cr8
009DCF16  B8 01 00 00 00                  mov eax, 1
009DCF1B  44 0F 22 C0                     mov cr8, rax
009DCF1F  44 39 2D FA 9D 5E 00            cmp dword ptr [rip + 0x5e9dfa], r13d
009DCF26  74 0B                           je 0x1409dcf33
009DCF28  0F B6 D0                        movzx edx, al
009DCF2B  0F B6 CB                        movzx ecx, bl
009DCF2E  E8 C9 87 B1 FF                  call 0x1404f56fc
009DCF33  44 0F B6 7C 24 42               movzx r15d, byte ptr [rsp + 0x42]
009DCF39  45 84 FF                        test r15b, r15b
009DCF3C  0F 84 B7 00 00 00               je 0x1409dcff9
009DCF42  E8 A1 D4 C8 FF                  call 0x14066a3e8
009DCF47  48 8B 0E                        mov rcx, qword ptr [rsi]
009DCF4A  85 C0                           test eax, eax
009DCF4C  74 63                           je 0x1409dcfb1
009DCF4E  48 85 C9                        test rcx, rcx
009DCF51  74 25                           je 0x1409dcf78
009DCF53  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
009DCF57  48 39 71 08                     cmp qword ptr [rcx + 8], rsi
009DCF5B  0F 85 EF 02 00 00               jne 0x1409dd250
009DCF61  48 39 30                        cmp qword ptr [rax], rsi
009DCF64  0F 85 E6 02 00 00               jne 0x1409dd250
009DCF6A  48 89 08                        mov qword ptr [rax], rcx
009DCF6D  48 89 41 08                     mov qword ptr [rcx + 8], rax
009DCF71  4C 89 2E                        mov qword ptr [rsi], r13
009DCF74  4C 89 6E 08                     mov qword ptr [rsi + 8], r13
009DCF78  48 8D 4E 10                     lea rcx, [rsi + 0x10]
009DCF7C  48 8B 11                        mov rdx, qword ptr [rcx]
009DCF7F  48 85 D2                        test rdx, rdx
009DCF82  75 06                           jne 0x1409dcf8a
009DCF84  4C 39 69 08                     cmp qword ptr [rcx + 8], r13
009DCF88  74 6F                           je 0x1409dcff9
009DCF8A  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
009DCF8E  48 39 4A 08                     cmp qword ptr [rdx + 8], rcx
009DCF92  0F 85 B8 02 00 00               jne 0x1409dd250
009DCF98  49 39 08                        cmp qword ptr [r8], rcx
009DCF9B  0F 85 AF 02 00 00               jne 0x1409dd250
009DCFA1  49 89 10                        mov qword ptr [r8], rdx
009DCFA4  4C 89 42 08                     mov qword ptr [rdx + 8], r8
009DCFA8  4C 89 29                        mov qword ptr [rcx], r13
009DCFAB  4C 89 69 08                     mov qword ptr [rcx + 8], r13
009DCFAF  EB 48                           jmp 0x1409dcff9
009DCFB1  48 85 C9                        test rcx, rcx
009DCFB4  74 1E                           je 0x1409dcfd4
009DCFB6  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
009DCFBA  48 39 71 08                     cmp qword ptr [rcx + 8], rsi
009DCFBE  0F 85 8C 02 00 00               jne 0x1409dd250
009DCFC4  48 39 30                        cmp qword ptr [rax], rsi
009DCFC7  0F 85 83 02 00 00               jne 0x1409dd250
009DCFCD  48 89 08                        mov qword ptr [rax], rcx
009DCFD0  48 89 41 08                     mov qword ptr [rcx + 8], rax
009DCFD4  48 8D 46 10                     lea rax, [rsi + 0x10]
009DCFD8  48 8B 10                        mov rdx, qword ptr [rax]
009DCFDB  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
009DCFDF  48 39 42 08                     cmp qword ptr [rdx + 8], rax
009DCFE3  0F 85 67 02 00 00               jne 0x1409dd250
009DCFE9  48 39 01                        cmp qword ptr [rcx], rax
009DCFEC  0F 85 5E 02 00 00               jne 0x1409dd250
009DCFF2  48 89 11                        mov qword ptr [rcx], rdx
009DCFF5  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
009DCFF9  48 8B 07                        mov rax, qword ptr [rdi]
009DCFFC  48 85 C0                        test rax, rax
009DCFFF  74 1E                           je 0x1409dd01f
009DD001  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
009DD005  48 39 78 08                     cmp qword ptr [rax + 8], rdi
009DD009  0F 85 41 02 00 00               jne 0x1409dd250
009DD00F  48 39 39                        cmp qword ptr [rcx], rdi
009DD012  0F 85 38 02 00 00               jne 0x1409dd250
009DD018  48 89 01                        mov qword ptr [rcx], rax
009DD01B  48 89 48 08                     mov qword ptr [rax + 8], rcx
009DD01F  48 8D 47 10                     lea rax, [rdi + 0x10]
009DD023  48 8B 10                        mov rdx, qword ptr [rax]
009DD026  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
009DD02A  48 39 42 08                     cmp qword ptr [rdx + 8], rax
009DD02E  0F 85 1C 02 00 00               jne 0x1409dd250
009DD034  48 39 01                        cmp qword ptr [rcx], rax
009DD037  0F 85 13 02 00 00               jne 0x1409dd250
009DD03D  48 89 11                        mov qword ptr [rcx], rdx
009DD040  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
009DD044  44 39 2D D5 9C 5E 00            cmp dword ptr [rip + 0x5e9cd5], r13d
009DD04B  74 0C                           je 0x1409dd059
009DD04D  44 0F 20 C1                     mov rcx, cr8
009DD051  0F B6 D3                        movzx edx, bl
009DD054  E8 3F 86 B1 FF                  call 0x1404f5698
009DD059  0F B6 C3                        movzx eax, bl
009DD05C  44 0F 22 C0                     mov cr8, rax
009DD060  48 8D 0D D9 88 51 00            lea rcx, [rip + 0x5188d9]
009DD067  E8 34 33 87 FF                  call 0x1402503a0
009DD06C  E8 13 CA 1E 00                  call 0x140bc9a84
009DD071  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
009DD075  8B 58 18                        mov ebx, dword ptr [rax + 0x18]
009DD078  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
009DD07D  89 18                           mov dword ptr [rax], ebx
009DD07F  80 7C 24 44 00                  cmp byte ptr [rsp + 0x44], 0
009DD084  74 06                           je 0x1409dd08c
009DD086  44 89 68 04                     mov dword ptr [rax + 4], r13d
009DD08A  EB 04                           jmp 0x1409dd090
009DD08C  4C 89 68 08                     mov qword ptr [rax + 8], r13
009DD090  44 0F B6 64 24 40               movzx r12d, byte ptr [rsp + 0x40]
009DD096  EB 20                           jmp 0x1409dd0b8
009DD098  8B D8                           mov ebx, eax
009DD09A  4C 8B 74 24 68                  mov r14, qword ptr [rsp + 0x68]
009DD09F  48 8B 7C 24 78                  mov rdi, qword ptr [rsp + 0x78]
009DD0A4  48 8B B4 24 98 00 00 00         mov rsi, qword ptr [rsp + 0x98]
009DD0AC  44 0F B6 64 24 43               movzx r12d, byte ptr [rsp + 0x43]
009DD0B2  44 0F B6 7C 24 42               movzx r15d, byte ptr [rsp + 0x42]
009DD0B8  45 84 FF                        test r15b, r15b
009DD0BB  74 08                           je 0x1409dd0c5
009DD0BD  48 8B CE                        mov rcx, rsi
009DD0C0  E8 9B B4 E6 FF                  call 0x140848560
009DD0C5  48 8B CF                        mov rcx, rdi
009DD0C8  E8 93 B4 E6 FF                  call 0x140848560
009DD0CD  E9 EB 01 00 00                  jmp 0x1409dd2bd
009DD0D2  E8 5D CA 1E 00                  call 0x140bc9b34
009DD0D7  48 8D 0D 62 88 51 00            lea rcx, [rip + 0x518862]
009DD0DE  E8 3D 66 A1 FF                  call 0x1403f3720
009DD0E3  45 0F 20 C4                     mov r12, cr8
009DD0E7  B8 01 00 00 00                  mov eax, 1
009DD0EC  44 0F 22 C0                     mov cr8, rax
009DD0F0  44 39 2D 29 9C 5E 00            cmp dword ptr [rip + 0x5e9c29], r13d
009DD0F7  74 0C                           je 0x1409dd105
009DD0F9  0F B6 D0                        movzx edx, al
009DD0FC  41 0F B6 CC                     movzx ecx, r12b
009DD100  E8 F7 85 B1 FF                  call 0x1404f56fc
009DD105  44 0F B6 7C 24 42               movzx r15d, byte ptr [rsp + 0x42]
009DD10B  45 84 FF                        test r15b, r15b
009DD10E  0F 84 B7 00 00 00               je 0x1409dd1cb
009DD114  E8 CF D2 C8 FF                  call 0x14066a3e8
009DD119  48 8B 0E                        mov rcx, qword ptr [rsi]
009DD11C  85 C0                           test eax, eax
009DD11E  74 63                           je 0x1409dd183
009DD120  48 85 C9                        test rcx, rcx
009DD123  74 25                           je 0x1409dd14a
009DD125  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
009DD129  48 39 71 08                     cmp qword ptr [rcx + 8], rsi
009DD12D  0F 85 1D 01 00 00               jne 0x1409dd250
009DD133  48 39 30                        cmp qword ptr [rax], rsi
009DD136  0F 85 14 01 00 00               jne 0x1409dd250
009DD13C  48 89 08                        mov qword ptr [rax], rcx
009DD13F  48 89 41 08                     mov qword ptr [rcx + 8], rax
009DD143  4C 89 2E                        mov qword ptr [rsi], r13
009DD146  4C 89 6E 08                     mov qword ptr [rsi + 8], r13
009DD14A  48 8D 4E 10                     lea rcx, [rsi + 0x10]
009DD14E  48 8B 11                        mov rdx, qword ptr [rcx]
009DD151  48 85 D2                        test rdx, rdx
009DD154  75 06                           jne 0x1409dd15c
009DD156  4C 39 69 08                     cmp qword ptr [rcx + 8], r13
009DD15A  74 6F                           je 0x1409dd1cb
009DD15C  4C 8B 41 08                     mov r8, qword ptr [rcx + 8]
009DD160  48 39 4A 08                     cmp qword ptr [rdx + 8], rcx
009DD164  0F 85 E6 00 00 00               jne 0x1409dd250
009DD16A  49 39 08                        cmp qword ptr [r8], rcx
009DD16D  0F 85 DD 00 00 00               jne 0x1409dd250
009DD173  49 89 10                        mov qword ptr [r8], rdx
009DD176  4C 89 42 08                     mov qword ptr [rdx + 8], r8
009DD17A  4C 89 29                        mov qword ptr [rcx], r13
009DD17D  4C 89 69 08                     mov qword ptr [rcx + 8], r13
009DD181  EB 48                           jmp 0x1409dd1cb
009DD183  48 85 C9                        test rcx, rcx
009DD186  74 1E                           je 0x1409dd1a6
009DD188  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
009DD18C  48 39 71 08                     cmp qword ptr [rcx + 8], rsi
009DD190  0F 85 BA 00 00 00               jne 0x1409dd250
009DD196  48 39 30                        cmp qword ptr [rax], rsi
009DD199  0F 85 B1 00 00 00               jne 0x1409dd250
009DD19F  48 89 08                        mov qword ptr [rax], rcx
009DD1A2  48 89 41 08                     mov qword ptr [rcx + 8], rax
009DD1A6  48 8D 46 10                     lea rax, [rsi + 0x10]
009DD1AA  48 8B 10                        mov rdx, qword ptr [rax]
009DD1AD  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
009DD1B1  48 39 42 08                     cmp qword ptr [rdx + 8], rax
009DD1B5  0F 85 95 00 00 00               jne 0x1409dd250
009DD1BB  48 39 01                        cmp qword ptr [rcx], rax
009DD1BE  0F 85 8C 00 00 00               jne 0x1409dd250
009DD1C4  48 89 11                        mov qword ptr [rcx], rdx
009DD1C7  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
009DD1CB  48 8B 07                        mov rax, qword ptr [rdi]
009DD1CE  48 85 C0                        test rax, rax
009DD1D1  74 16                           je 0x1409dd1e9
009DD1D3  48 8B 4F 08                     mov rcx, qword ptr [rdi + 8]
009DD1D7  48 39 78 08                     cmp qword ptr [rax + 8], rdi
009DD1DB  75 73                           jne 0x1409dd250
009DD1DD  48 39 39                        cmp qword ptr [rcx], rdi
009DD1E0  75 6E                           jne 0x1409dd250
009DD1E2  48 89 01                        mov qword ptr [rcx], rax
009DD1E5  48 89 48 08                     mov qword ptr [rax + 8], rcx
009DD1E9  48 8D 47 10                     lea rax, [rdi + 0x10]
009DD1ED  48 8B 10                        mov rdx, qword ptr [rax]
009DD1F0  48 8B 48 08                     mov rcx, qword ptr [rax + 8]
009DD1F4  48 39 42 08                     cmp qword ptr [rdx + 8], rax
009DD1F8  75 56                           jne 0x1409dd250
009DD1FA  48 39 01                        cmp qword ptr [rcx], rax
009DD1FD  75 51                           jne 0x1409dd250
009DD1FF  48 89 11                        mov qword ptr [rcx], rdx
009DD202  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
009DD206  44 39 2D 13 9B 5E 00            cmp dword ptr [rip + 0x5e9b13], r13d
009DD20D  74 0D                           je 0x1409dd21c
009DD20F  44 0F 20 C1                     mov rcx, cr8
009DD213  41 0F B6 D4                     movzx edx, r12b
009DD217  E8 7C 84 B1 FF                  call 0x1404f5698
009DD21C  41 0F B6 C4                     movzx eax, r12b
009DD220  44 0F 22 C0                     mov cr8, rax
009DD224  48 8D 0D 15 87 51 00            lea rcx, [rip + 0x518715]
009DD22B  E8 70 31 87 FF                  call 0x1402503a0
009DD230  E8 4F C8 1E 00                  call 0x140bc9a84
009DD235  45 84 FF                        test r15b, r15b
009DD238  74 08                           je 0x1409dd242
009DD23A  48 8B CE                        mov rcx, rsi
009DD23D  E8 1E B3 E6 FF                  call 0x140848560
009DD242  48 8B CF                        mov rcx, rdi
009DD245  E8 16 B3 E6 FF                  call 0x140848560
009DD24A  45 0F B6 E5                     movzx r12d, r13b
009DD24E  EB 6D                           jmp 0x1409dd2bd
009DD250  B9 03 00 00 00                  mov ecx, 3
009DD255  CD 29                           int 0x29
009DD257  48 8B CF                        mov rcx, rdi
009DD25A  E8 01 B3 E6 FF                  call 0x140848560
009DD25F  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
009DD264  48 85 C9                        test rcx, rcx
009DD267  74 4E                           je 0x1409dd2b7
009DD269  E8 E2 C0 91 FF                  call 0x1402f9350
009DD26E  EB 47                           jmp 0x1409dd2b7
009DD270  49 8B 4E 08                     mov rcx, qword ptr [r14 + 8]
009DD274  41 83 FC 01                     cmp r12d, 1
009DD278  75 0B                           jne 0x1409dd285
009DD27A  49 8B 57 08                     mov rdx, qword ptr [r15 + 8]
009DD27E  E8 19 B4 E6 FF                  call 0x14084869c
009DD283  EB 05                           jmp 0x1409dd28a
009DD285  E8 36 C0 1E 00                  call 0x140bc92c0
009DD28A  E8 F5 C7 1E 00                  call 0x140bc9a84
009DD28F  48 85 DB                        test rbx, rbx
009DD292  74 08                           je 0x1409dd29c
009DD294  48 8B CB                        mov rcx, rbx
009DD297  E8 B4 C0 91 FF                  call 0x1402f9350
009DD29C  41 83 FC 01                     cmp r12d, 1
009DD2A0  75 08                           jne 0x1409dd2aa
009DD2A2  48 8B CE                        mov rcx, rsi
009DD2A5  E8 B6 B2 E6 FF                  call 0x140848560
009DD2AA  48 8B CF                        mov rcx, rdi
009DD2AD  E8 AE B2 E6 FF                  call 0x140848560
009DD2B2  BB 7C 01 00 C0                  mov ebx, 0xc000017c
009DD2B7  44 0F B6 64 24 40               movzx r12d, byte ptr [rsp + 0x40]
009DD2BD  49 8B CE                        mov rcx, r14
009DD2C0  E8 8B C0 91 FF                  call 0x1402f9350
009DD2C5  45 84 E4                        test r12b, r12b
009DD2C8  74 05                           je 0x1409dd2cf
009DD2CA  E8 B1 C5 1E 00                  call 0x140bc9880
009DD2CF  48 8D 8C 24 80 00 00 00         lea rcx, [rsp + 0x80]
009DD2D7  E8 74 2A A4 FF                  call 0x14041fd50
009DD2DC  8B C3                           mov eax, ebx
009DD2DE  48 8B 8C 24 80 02 00 00         mov rcx, qword ptr [rsp + 0x280]
009DD2E6  48 33 CC                        xor rcx, rsp
009DD2E9  E8 52 F3 CC FF                  call 0x1406ac640
009DD2EE  48 81 C4 90 02 00 00            add rsp, 0x290
009DD2F5  41 5F                           pop r15
009DD2F7  41 5E                           pop r14
009DD2F9  41 5D                           pop r13
009DD2FB  41 5C                           pop r12
009DD2FD  5F                              pop rdi
009DD2FE  5E                              pop rsi
009DD2FF  5B                              pop rbx
009DD300  C3                              ret
009DD301  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtNotifyChangeMultipleKeys(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, __int64 a7, unsigned int a8, unsigned __int8 a9, __int64 a10, unsigned int a11, unsigned __int8 a12)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m228;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned __int64 v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned int v_stack_m280;
    unsigned __int8 v_stack_m284;
    unsigned __int8 v_stack_m285;
    unsigned __int8 v_stack_m286;
    unsigned __int8 v_stack_m287;
    unsigned __int8 v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m48;

    v_rsp = (v_rsp) - (656);
    result = (*(unsigned __int64 *)(v_rip + 4382838)) ^ (v_rsp);
    v_stack_m48 = result;
    v_stack_m228 = a4;
    v_stack_m250 = a3;
    v_stack_m270 = a1;
    v_stack_m258 = a7;
    result = 0;
    v_stack_m248 = v_xmm0;
    v_stack_m238 = 0;
    v_r13 = 0;
    v_stack_m260 = 0;
    v_stack_m278 = 0;
    v_stack_m230 = 0;
    v_stack_m280 = 1;
    a2 = 0;
    result = memset(v_stack_m218, a2, 464, a4);
    v_stack_m284 = 0;
    v_stack_m268 = 0;
    result = CmpInitializeThreadInfo(v_stack_m248, a2, 464, a4);
    result = CmpAcquireShutdownRundown(v_stack_m248, a2, 464, a4);
    v_stack_m288 = (unsigned __int8)(result);
    if ((unsigned __int8)(result) != 0) goto loc_009DC787;
    result = CmCleanupThreadInfo(v_stack_m248, a2, 464, a4);
    goto loc_009DD2DE;
loc_009DC787:
    if (((unsigned int)((unsigned int)(a2))) > 1) goto loc_009DC8D7;
    v_stack_m287 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if ((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)) == 0) goto loc_009DC8BF;
    if (condition_is_above_or_equal) goto loc_009DC7F2;
    if (a12 == 0) goto loc_009DC8D7;
    if (a5 != 0) goto loc_009DC8D7;
    if (a4 == 0) goto loc_009DC8D7;
    v_stack_m280 = 4;
    goto loc_009DC8FE;
loc_009DC7F2:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 784)) == 0) goto loc_009DC82B;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772))) == 332) goto loc_009DC826;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184) + 1772))) != 452) goto loc_009DC82B;
loc_009DC826:
    goto loc_009DC82E;
loc_009DC82B:
    v_r15 = 0;
loc_009DC82E:
    v_stack_m284 = 0;
    a2 = (0) ^ (1);
    result = ProbeForWrite(a7, a2 * 8 + 8, 4, a4);
    result = ProbeForWrite(4, (unsigned int)(a11), 4, a4);
    if (0 == 0) goto loc_009DC874;
    *(unsigned __int64 *)(a7) = 259;
    goto loc_009DC87F;
loc_009DC874:
    *(unsigned int *)(a7) = 259;
    *(unsigned __int64 *)(a7 + 8) = 0;
loc_009DC87F:
    if (a12 == 0) goto loc_009DC89E;
    v_stack_m280 = 2;
    goto loc_009DC904;
loc_009DC89E:
    goto loc_009DC904;
loc_009DC8BF:
    if (a12 == 0) goto loc_009DC8F3;
    v_stack_m280 = 3;
    if ((unsigned int)((unsigned int)(a2)) == 0) goto loc_009DC8F7;
loc_009DC8D7:
    result = CmpReleaseShutdownRundown(v_stack_m287, (unsigned int)(a11), 4, a4);
    result = CmCleanupThreadInfo(v_stack_m248, (unsigned int)(a11), 4, a4);
    goto loc_009DD2DE;
loc_009DC8F3:
loc_009DC8F7:
loc_009DC8FE:
loc_009DC904:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a8)))) & (0x1000000FULL));
    if (((unsigned int)((unsigned int)(a8))) != ((unsigned int)(result))) goto loc_009DC8D7;
    a2 = 0;
    v_stack_m2A0 = 0;
    v_stack_m2A8 = v_stack_m260;
    result = CmObReferenceObjectByHandle(v_stack_m270, 16, 4, (unsigned __int8)(v_stack_m248));
    if (sign_flag) goto loc_009DD2CA;
    v_rbx = 0;
    v_stack_m270 = 0;
    if (((unsigned int)((unsigned int)(a2))) != 1) goto loc_009DC9D5;
    result = CmpInitializeParseContext(v_stack_m218, 16, 4, (unsigned __int8)(v_stack_m248));
    v_stack_m298 = v_stack_m270;
    v_stack_m2A0 = v_stack_m218;
    v_stack_m2A8 = (unsigned __int8)(v_stack_m287);
    a2 = 0;
    result = CmObReferenceObjectByName(v_stack_m250, a2, v_rbx + 16, (unsigned __int8)(v_stack_m248));
    a2 = 0;
    result = CmpCleanupParseContext(v_stack_m218, a2, v_rbx + 16, (unsigned __int8)(v_stack_m248));
    if (sign_flag) goto loc_009DD2B7;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m260 + 8) + 32)) != (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m270 + 8) + 32))) goto loc_009DC9DC;
    result = ObfDereferenceObject(v_stack_m270, *(unsigned __int64 *)(v_stack_m260 + 8), v_rbx + 16, (unsigned __int8)(v_stack_m248));
    goto loc_009DD2B7;
loc_009DC9D5:
    goto loc_009DC9DE;
loc_009DC9DC:
    v_rbx = 0;
loc_009DC9DE:
    a4 = 0;
    a3 = 0;
    result = CmpAllocatePostBlock((unsigned int)((unsigned int)((unsigned int)(v_stack_m280))), (unsigned int)(0x10000ULL), a3, a4);
    v_stack_m250 = result;
    if (result != 0) goto loc_009DCA15;
    if (((unsigned int)((unsigned int)(a2))) == 1) {
        a1 = v_stack_m270;
        result = ObfDereferenceObject(a1, (unsigned int)(0x10000ULL), a3, a4);
    }
    goto loc_009DD2B7;
loc_009DCA15:
    if (((unsigned int)((unsigned int)(a2))) != 1) goto loc_009DCA56;
    a2 = 0;
    result = CmpAllocatePostBlock((unsigned int)(v_stack_m280), a2, v_stack_m270, result);
    v_stack_m230 = result;
    if (result != 0) goto loc_009DCA56;
    result = ObfDereferenceObject(v_stack_m270, a2, v_stack_m270, result);
    result = CmpFreePostBlock(result, a2, v_stack_m270, result);
    goto loc_009DD2B7;
loc_009DCA56:
    if (((unsigned int)((unsigned int)(v_stack_m280))) == 1) goto loc_009DCB94;
    if (v_stack_m228 == 0) goto loc_009DCAD5;
    v_stack_m278 = (unsigned int)(0xC000009AULL);
    v_stack_m2A0 = (unsigned int)(0xC000009AULL);
    v_stack_m2A8 = v_stack_m278;
    result = ObReferenceObjectByHandle(v_stack_m228, 2, *(unsigned __int64 *)(v_rip + 6201609), v_stack_m287);
    v_stack_m278 = v_stack_m278;
    if (!sign_flag) goto loc_009DCAC7;
    if (((unsigned int)((unsigned int)(a2))) == 1) {
        a1 = result;
        result = CmpFreePostBlock(a1, 2, *(unsigned __int64 *)(v_rip + 6201609), v_stack_m287);
    }
    result = CmpFreePostBlock(result, 2, *(unsigned __int64 *)(v_rip + 6201609), v_stack_m287);
    goto loc_009DD2B7;
loc_009DCAC7:
    result = KeResetEvent(result, 2, *(unsigned __int64 *)(v_rip + 6201609), v_stack_m287);
    goto loc_009DCADA;
loc_009DCAD5:
loc_009DCADA:
    if (((unsigned int)((unsigned int)(v_stack_m280))) != 2) goto loc_009DCB6C;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 64) + 104) = v_stack_m258;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 64) + 8) = v_stack_m278;
    a4 = v_stack_m287;
    if (a5 == 0) { a4 = 0; }
    a3 = v_rip + 557630;
    if (a5 != 0) { a3 = a5; }
    a1 = (*(unsigned __int64 *)(result + 64)) + (16);
    v_stack_m290 = a6;
    v_stack_m298 = (unsigned __int8)(a4);
    v_stack_m2A0 = a3;
    v_stack_m2A8 = v_rip - 2075580;
    result = KeInitializeApc(a1, *(unsigned __int64 *)(gs_base + (0 + 392)), 2, v_rip + 1158552);
    goto loc_009DCB99;
loc_009DCB6C:
    *(unsigned __int64 *)(result) = v_stack_m278;
    if (((unsigned int)(a1)) == 4) goto loc_009DCB99;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 64) + 8) = a5;
    *(unsigned int *)(*(unsigned __int64 *)(result + 64) + 16) = (unsigned int)((unsigned int)(a6));
    goto loc_009DCB99;
loc_009DCB94:
loc_009DCB99:
    result = CmpLockRegistry(*(unsigned __int64 *)(result + 64), *(unsigned __int64 *)(gs_base + (0 + 392)), 2, v_rip + 1158552);
    if (((unsigned int)((unsigned int)(a2))) != 1) goto loc_009DCBB3;
    result = CmpLockTwoKcbsShared(*(unsigned __int64 *)(v_stack_m260 + 8), *(unsigned __int64 *)(v_stack_m270 + 8), 2, v_rip + 1158552);
    goto loc_009DCBB8;
loc_009DCBB3:
    result = CmpLockKcbShared(*(unsigned __int64 *)(v_stack_m260 + 8), *(unsigned __int64 *)(v_stack_m270 + 8), 2, v_rip + 1158552);
loc_009DCBB8:
    a2 = 0;
    result = CmpIsKeyDeletedForKeyBody(v_stack_m260, a2, 2, v_rip + 1158552);
    if ((unsigned __int8)(result) != 0) goto loc_009DD270;
    if (((unsigned int)((unsigned int)(a2))) != 1) goto loc_009DCC49;
    a2 = 0;
    result = CmpIsKeyDeletedForKeyBody(v_stack_m270, a2, 2, v_rip + 1158552);
    if ((unsigned __int8)(result) != 0) goto loc_009DD270;
    if (((unsigned int)((unsigned int)(a2))) != ((unsigned int)((unsigned int)(a2)))) goto loc_009DCC49;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m260 + 8) + 32)) == (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m270 + 8) + 32))) goto loc_009DCC49;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m260 + 8) + 32)) >= (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m270 + 8) + 32))) goto loc_009DCC1F;
    result = CmLockHive(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m260 + 8) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m270 + 8) + 32), 2, v_rip + 1158552);
    result = CmLockHive(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m270 + 8) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m270 + 8) + 32), 2, v_rip + 1158552);
    v_stack_m268 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m270 + 8) + 32);
    goto loc_009DCC5C;
loc_009DCC1F:
    result = CmLockHive(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m270 + 8) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m270 + 8) + 32), 2, v_rip + 1158552);
    result = CmLockHive(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m260 + 8) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m270 + 8) + 32), 2, v_rip + 1158552);
    v_stack_m268 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m270 + 8) + 32);
    goto loc_009DCC5C;
loc_009DCC49:
    result = CmLockHive(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m260 + 8) + 32), *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m270 + 8) + 32), 2, v_rip + 1158552);
loc_009DCC5C:
    result = ExAcquireFastMutexUnsafe(v_rip + 5344477, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m270 + 8) + 32), 2, v_rip + 1158552);
    v_stack_m298 = result;
    result = CmpNotifyChangeKey(v_stack_m260, result, (unsigned int)(a8), a9);
    if (!sign_flag) goto loc_009DCD2B;
    result = ExReleaseFastMutexUnsafe(v_rip + 5344422, result, (unsigned int)(a8), a9);
    if (1 != 1) goto loc_009DCCAF;
    goto loc_009DCCE1;
loc_009DCCAF:
    if (1 != 2) goto loc_009DCCC9;
    result = CmUnlockHive(v_stack_m268, result, (unsigned int)(a8), a9);
    goto loc_009DCCE1;
loc_009DCCC9:
    if (1 != 3) goto loc_009DCCE6;
    result = CmUnlockHive(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m260 + 8) + 32), result, (unsigned int)(a8), a9);
loc_009DCCE1:
    result = CmUnlockHive(v_stack_m268, result, (unsigned int)(a8), a9);
loc_009DCCE6:
    if (((unsigned int)((unsigned int)(a2))) != 1) goto loc_009DCCFB;
    result = CmpUnlockTwoKcbs(*(unsigned __int64 *)(v_stack_m260 + 8), *(unsigned __int64 *)(v_stack_m270 + 8), (unsigned int)(a8), a9);
    goto loc_009DCD00;
loc_009DCCFB:
    result = CmpUnlockKcb(*(unsigned __int64 *)(v_stack_m260 + 8), *(unsigned __int64 *)(v_stack_m270 + 8), (unsigned int)(a8), a9);
loc_009DCD00:
    result = CmpUnlockRegistry(*(unsigned __int64 *)(v_stack_m260 + 8), *(unsigned __int64 *)(v_stack_m270 + 8), (unsigned int)(a8), a9);
    if (v_stack_m278 != 0) {
        result = ObfDereferenceObject(v_stack_m278, *(unsigned __int64 *)(v_stack_m270 + 8), (unsigned int)(a8), a9);
    }
    if (((unsigned int)((unsigned int)(a2))) != 1) goto loc_009DD2B7;
    result = CmpFreePostBlock(result, *(unsigned __int64 *)(v_stack_m270 + 8), (unsigned int)(a8), a9);
    goto loc_009DD2B7;
loc_009DCD2B:
    v_stack_m286 = (unsigned __int8)(v_stack_m285);
    if (((unsigned int)((unsigned int)(a2))) != 1) goto loc_009DCE29;
    result = ObfReferenceObject(v_stack_m270, *(unsigned __int64 *)(v_stack_m270 + 8), (unsigned int)(a8), a9);
    if ((unsigned int)((unsigned int)((unsigned int)(result))) != 0) goto loc_009DCD5B;
    result = CmpFreePostBlock(result, *(unsigned __int64 *)(v_stack_m270 + 8), (unsigned int)(a8), a9);
    v_stack_m286 = (unsigned __int8)((unsigned int)((unsigned int)(result)));
    goto loc_009DCE29;
loc_009DCD5B:
    v_stack_m298 = result;
    result = CmpNotifyChangeKey(v_stack_m270, result, (unsigned int)(a8), a9);
    v_stack_m286 = (unsigned __int8)(v_stack_m285);
    if (!sign_flag) goto loc_009DCE29;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8)) != result) goto loc_009DD250;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) != result) goto loc_009DD250;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8)) = *(unsigned __int64 *)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8) = *(unsigned __int64 *)(result + 8);
    v_stack_m270 = v_cr8;
    result = 1;
    if ((*(unsigned int *)(v_rip + 6201175)) != 0) {
        a2 = 1;
        a1 = (unsigned __int8)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, v_cr8, a9);
        a3 = v_stack_m270;
    }
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8)) != (result + 16)) goto loc_009DD250;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16 + 8))) != (result + 16)) goto loc_009DD250;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16 + 8)) = *(unsigned __int64 *)(result + 16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8) = *(unsigned __int64 *)(result + 16 + 8);
    result = result + 16;
    if ((*(unsigned int *)(v_rip + 6201112)) != 0) {
        a1 = 1;
        a2 = (unsigned __int8)(a3);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, a3, a9);
    }
    v_stack_m286 = (unsigned __int8)(v_stack_m285);
loc_009DCE29:
    result = ExReleaseFastMutexUnsafe(v_rip + 5344016, a2, a3, a9);
    if (1 != 1) goto loc_009DCE45;
    goto loc_009DCE77;
loc_009DCE45:
    if (1 != 2) goto loc_009DCE5F;
    result = CmUnlockHive(v_stack_m268, a2, a3, a9);
    goto loc_009DCE77;
loc_009DCE5F:
    if (1 != 3) goto loc_009DCE7C;
    result = CmUnlockHive(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m260 + 8) + 32), a2, a3, a9);
loc_009DCE77:
    result = CmUnlockHive(v_stack_m268, a2, a3, a9);
loc_009DCE7C:
    if (((unsigned int)((unsigned int)(a2))) != 1) goto loc_009DCE91;
    result = CmpUnlockTwoKcbs(*(unsigned __int64 *)(v_stack_m260 + 8), *(unsigned __int64 *)(v_stack_m270 + 8), a3, a9);
    goto loc_009DCE96;
loc_009DCE91:
    result = CmpUnlockKcb(*(unsigned __int64 *)(v_stack_m260 + 8), *(unsigned __int64 *)(v_stack_m270 + 8), a3, a9);
loc_009DCE96:
    result = CmpUnlockRegistry(*(unsigned __int64 *)(v_stack_m260 + 8), *(unsigned __int64 *)(v_stack_m270 + 8), a3, a9);
    if (v_stack_m270 != 0) {
        a1 = v_stack_m270;
        result = ObfDereferenceObject(a1, *(unsigned __int64 *)(v_stack_m270 + 8), a3, a9);
    }
    if (sign_flag) goto loc_009DD257;
    if (v_stack_m280 != 1) goto loc_009DD2B7;
    result = CmpReleaseShutdownRundown(a1, *(unsigned __int64 *)(v_stack_m270 + 8), a3, a9);
    v_r12 = 0;
    v_stack_m288 = 0;
    v_stack_m285 = 0;
    v_r13 = 0;
    v_stack_m2A8 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(*(unsigned __int64 *)(result + 64), a2, v_stack_m287, 1);
    if (((unsigned int)(result)) == 257) goto loc_009DD0D2;
    if (((unsigned int)(result)) == 192) goto loc_009DD0D2;
    result = CmpLockRegistry(*(unsigned __int64 *)(result + 64), a2, v_stack_m287, 1);
    result = ExAcquireFastMutexUnsafe(v_rip + 5343795, a2, v_stack_m287, 1);
    result = 1;
    if ((*(unsigned int *)(v_rip + 6200826)) != 0) {
        a2 = 1;
        a1 = (unsigned __int8)(v_stack_m270);
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, v_stack_m287, 1);
    }
    if ((unsigned __int8)(v_stack_m286) == 0) goto loc_009DCFF9;
    result = Feature_2602282298__private_IsEnabledDeviceUsageNoInline(a1, a2, v_stack_m287, 1);
    if ((unsigned int)(result) == 0) goto loc_009DCFB1;
    if (*(unsigned __int64 *)(result) == 0) goto loc_009DCF78;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8)) != result) goto loc_009DD250;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) != result) goto loc_009DD250;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8)) = *(unsigned __int64 *)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8) = *(unsigned __int64 *)(result + 8);
    *(unsigned __int64 *)(result) = 0;
    *(unsigned __int64 *)(result + 8) = 0;
loc_009DCF78:
    if (*(unsigned __int64 *)(result + 16) != 0) goto loc_009DCF8A;
    if ((*(unsigned __int64 *)(result + 16 + 8)) == 0) goto loc_009DCFF9;
loc_009DCF8A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8)) != (result + 16)) goto loc_009DD250;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16 + 8))) != (result + 16)) goto loc_009DD250;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16 + 8)) = *(unsigned __int64 *)(result + 16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8) = *(unsigned __int64 *)(result + 16 + 8);
    *(unsigned __int64 *)(result + 16) = 0;
    *(unsigned __int64 *)(result + 16 + 8) = 0;
    goto loc_009DCFF9;
loc_009DCFB1:
    if (result + 16 == 0) goto loc_009DCFD4;
    if ((*(unsigned __int64 *)(result + 16 + 8)) != result) goto loc_009DD250;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) != result) goto loc_009DD250;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8)) = result + 16;
    *(unsigned __int64 *)(result + 16 + 8) = *(unsigned __int64 *)(result + 8);
loc_009DCFD4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8)) != (result + 16)) goto loc_009DD250;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16 + 8))) != (result + 16)) goto loc_009DD250;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16 + 8)) = *(unsigned __int64 *)(result + 16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8) = *(unsigned __int64 *)(result + 16 + 8);
loc_009DCFF9:
    if (*(unsigned __int64 *)(result) == 0) goto loc_009DD01F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8)) != result) goto loc_009DD250;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) != result) goto loc_009DD250;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8)) = *(unsigned __int64 *)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8) = *(unsigned __int64 *)(result + 8);
loc_009DD01F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8)) != (result + 16)) goto loc_009DD250;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16 + 8))) != (result + 16)) goto loc_009DD250;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16 + 8)) = *(unsigned __int64 *)(result + 16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8) = *(unsigned __int64 *)(result + 16 + 8);
    result = result + 16;
    if ((*(unsigned int *)(v_rip + 6200533)) != 0) {
        a1 = 1;
        a2 = (unsigned __int8)(v_stack_m270);
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(result + 16 + 8), 1);
    }
    result = ExReleaseFastMutexUnsafe(v_rip + 5343449, a2, *(unsigned __int64 *)(result + 16 + 8), 1);
    result = CmpUnlockRegistry(v_rip + 5343449, a2, *(unsigned __int64 *)(result + 16 + 8), 1);
    *(unsigned int *)(v_stack_m258) = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 64) + 24)));
    if (v_stack_m284 == 0) goto loc_009DD08C;
    *(unsigned int *)(v_stack_m258 + 4) = 0;
    goto loc_009DD090;
loc_009DD08C:
    *(unsigned __int64 *)(v_stack_m258 + 8) = 0;
loc_009DD090:
    goto loc_009DD0B8;
loc_009DD0B8:
    result = v_stack_m258;
    if ((unsigned __int8)(v_stack_m286) != 0) {
        a1 = result;
        result = CmpFreePostBlock(a1, a2, *(unsigned __int64 *)(result + 16 + 8), 1);
    }
    result = CmpFreePostBlock(result, a2, *(unsigned __int64 *)(result + 16 + 8), 1);
    goto loc_009DD2BD;
loc_009DD0D2:
    result = CmpLockRegistry(result, a2, *(unsigned __int64 *)(result + 16 + 8), 1);
    result = ExAcquireFastMutexUnsafe(v_rip + 5343330, a2, *(unsigned __int64 *)(result + 16 + 8), 1);
    result = 1;
    if ((*(unsigned int *)(v_rip + 6200361)) != 0) {
        a2 = 1;
        a1 = (unsigned __int8)((unsigned __int8)(v_stack_m270));
        result = KiRaiseIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(result + 16 + 8), 1);
    }
    if ((unsigned __int8)(v_stack_m286) == 0) goto loc_009DD1CB;
    result = Feature_2602282298__private_IsEnabledDeviceUsageNoInline(a1, a2, *(unsigned __int64 *)(result + 16 + 8), 1);
    if ((unsigned int)(result) == 0) goto loc_009DD183;
    if (*(unsigned __int64 *)(result) == 0) goto loc_009DD14A;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8)) != result) goto loc_009DD250;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) != result) goto loc_009DD250;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8)) = *(unsigned __int64 *)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8) = *(unsigned __int64 *)(result + 8);
    *(unsigned __int64 *)(result) = 0;
    *(unsigned __int64 *)(result + 8) = 0;
loc_009DD14A:
    if (*(unsigned __int64 *)(result + 16) != 0) goto loc_009DD15C;
    if ((*(unsigned __int64 *)(result + 16 + 8)) == 0) goto loc_009DD1CB;
loc_009DD15C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8)) != (result + 16)) goto loc_009DD250;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16 + 8))) != (result + 16)) goto loc_009DD250;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16 + 8)) = *(unsigned __int64 *)(result + 16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8) = *(unsigned __int64 *)(result + 16 + 8);
    *(unsigned __int64 *)(result + 16) = 0;
    *(unsigned __int64 *)(result + 16 + 8) = 0;
    goto loc_009DD1CB;
loc_009DD183:
    if (result + 16 == 0) goto loc_009DD1A6;
    if ((*(unsigned __int64 *)(result + 16 + 8)) != result) goto loc_009DD250;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) != result) goto loc_009DD250;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8)) = result + 16;
    *(unsigned __int64 *)(result + 16 + 8) = *(unsigned __int64 *)(result + 8);
loc_009DD1A6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8)) != (result + 16)) goto loc_009DD250;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16 + 8))) != (result + 16)) goto loc_009DD250;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16 + 8)) = *(unsigned __int64 *)(result + 16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8) = *(unsigned __int64 *)(result + 16 + 8);
loc_009DD1CB:
    if (*(unsigned __int64 *)(result) == 0) goto loc_009DD1E9;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8)) != result) goto loc_009DD250;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 8))) != result) goto loc_009DD250;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 8)) = *(unsigned __int64 *)(result);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result) + 8) = *(unsigned __int64 *)(result + 8);
loc_009DD1E9:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8)) != (result + 16)) goto loc_009DD250;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 16 + 8))) != (result + 16)) goto loc_009DD250;
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16 + 8)) = *(unsigned __int64 *)(result + 16);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 16) + 8) = *(unsigned __int64 *)(result + 16 + 8);
    result = result + 16;
    if ((*(unsigned int *)(v_rip + 6200083)) != 0) {
        a1 = 1;
        a2 = (unsigned __int8)((unsigned __int8)(v_stack_m270));
        result = KiLowerIrqlProcessIrqlFlags(a1, a2, *(unsigned __int64 *)(result + 16 + 8), 1);
    }
    result = ExReleaseFastMutexUnsafe(v_rip + 5342997, a2, *(unsigned __int64 *)(result + 16 + 8), 1);
    result = CmpUnlockRegistry(v_rip + 5342997, a2, *(unsigned __int64 *)(result + 16 + 8), 1);
    if ((unsigned __int8)(v_stack_m286) != 0) {
        a1 = result;
        result = CmpFreePostBlock(a1, a2, *(unsigned __int64 *)(result + 16 + 8), 1);
    }
    result = CmpFreePostBlock(result, a2, *(unsigned __int64 *)(result + 16 + 8), 1);
    goto loc_009DD2BD;
loc_009DD250:
loc_009DD257:
    result = CmpFreePostBlock(result, a2, *(unsigned __int64 *)(result + 16 + 8), 1);
    if (v_stack_m278 == 0) goto loc_009DD2B7;
    result = ObfDereferenceObject(v_stack_m278, a2, *(unsigned __int64 *)(result + 16 + 8), 1);
    goto loc_009DD2B7;
loc_009DD270:
    if (0 != 1) goto loc_009DD285;
    result = CmpUnlockTwoKcbs(*(unsigned __int64 *)(v_stack_m260 + 8), *(unsigned __int64 *)(v_stack_m286 + 8), *(unsigned __int64 *)(result + 16 + 8), 1);
    goto loc_009DD28A;
loc_009DD285:
    result = CmpUnlockKcb(*(unsigned __int64 *)(v_stack_m260 + 8), *(unsigned __int64 *)(v_stack_m286 + 8), *(unsigned __int64 *)(result + 16 + 8), 1);
loc_009DD28A:
    result = CmpUnlockRegistry(*(unsigned __int64 *)(v_stack_m260 + 8), *(unsigned __int64 *)(v_stack_m286 + 8), *(unsigned __int64 *)(result + 16 + 8), 1);
    if ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 64) + 24)) != 0) {
        a1 = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 64) + 24));
        result = ObfDereferenceObject(a1, *(unsigned __int64 *)(v_stack_m286 + 8), *(unsigned __int64 *)(result + 16 + 8), 1);
    }
    if (0 == 1) {
        a1 = result;
        result = CmpFreePostBlock(a1, *(unsigned __int64 *)(v_stack_m286 + 8), *(unsigned __int64 *)(result + 16 + 8), 1);
    }
    result = CmpFreePostBlock(result, *(unsigned __int64 *)(v_stack_m286 + 8), *(unsigned __int64 *)(result + 16 + 8), 1);
loc_009DD2B7:
loc_009DD2BD:
    result = ObfDereferenceObject(v_stack_m260, *(unsigned __int64 *)(v_stack_m286 + 8), *(unsigned __int64 *)(result + 16 + 8), 1);
    if ((unsigned __int8)(v_stack_m288) != 0) {
        result = CmpReleaseShutdownRundown(v_stack_m260, *(unsigned __int64 *)(v_stack_m286 + 8), *(unsigned __int64 *)(result + 16 + 8), 1);
    }
    result = CmCleanupThreadInfo(v_stack_m248, *(unsigned __int64 *)(v_stack_m286 + 8), *(unsigned __int64 *)(result + 16 + 8), 1);
loc_009DD2DE:
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int64 *)(v_stack_m286 + 8), *(unsigned __int64 *)(result + 16 + 8), 1);
    v_rsp = (v_rsp) + (656);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtNotifyChangeMultipleKeys(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, void *Arg7, uint32_t Arg8, uint8_t Arg9, int64_t Arg10, uint32_t Arg11, uint8_t Arg12)
{
    uint8_t *arg7 = (uint8_t *)Arg7;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m218;
    uint64_t v_stack_m228;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint64_t v_stack_m270;
    uint64_t v_stack_m278;
    uint32_t v_stack_m280;
    uint8_t v_stack_m284;
    uint8_t v_stack_m285;
    uint8_t v_stack_m286;
    uint8_t v_stack_m287;
    uint8_t v_stack_m288;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m48;

    local_rsp = (local_rsp) - (656);
    result = (*(uint64_t *)(v_rip + 0x42E076)) ^ (local_rsp);
    v_stack_m48 = result;
    v_stack_m228 = Arg4;
    v_stack_m250 = Arg3;
    v_stack_m270 = Arg1;
    v_stack_m258 = Arg7;
    result = 0;
    v_stack_m248 = v_xmm0;
    v_stack_m238 = 0;
    local_r13 = 0;
    v_stack_m260 = 0;
    v_stack_m278 = 0;
    v_stack_m230 = 0;
    v_stack_m280 = 1;
    Arg2 = 0;
    result = memset(v_stack_m218, Arg2, 464, Arg4);
    v_stack_m284 = 0;
    v_stack_m268 = 0;
    result = CmpInitializeThreadInfo(v_stack_m248, Arg2, 464, Arg4);
    result = CmpAcquireShutdownRundown(v_stack_m248, Arg2, 464, Arg4);
    v_stack_m288 = (uint8_t)(result);
    if ((uint8_t)(result) != 0) goto loc_009DC787;
    result = CmCleanupThreadInfo(v_stack_m248, Arg2, 464, Arg4);
    goto loc_009DD2DE;
loc_009DC787:
    if (((uint32_t)((uint32_t)(Arg2))) > 1) goto loc_009DC8D7;
    v_stack_m287 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if ((uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)) == 0) goto loc_009DC8BF;
    if (condition_is_above_or_equal) goto loc_009DC7F2;
    if (Arg12 == 0) goto loc_009DC8D7;
    if (Arg5 != 0) goto loc_009DC8D7;
    if (Arg4 == 0) goto loc_009DC8D7;
    v_stack_m280 = 4;
    goto loc_009DC8FE;
loc_009DC7F2:
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x310)) == 0) goto loc_009DC82B;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC))) == 332) goto loc_009DC826;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8) + 0x6EC))) != 452) goto loc_009DC82B;
loc_009DC826:
    goto loc_009DC82E;
loc_009DC82B:
    local_r15 = 0;
loc_009DC82E:
    v_stack_m284 = 0;
    Arg2 = (0) ^ (1);
    result = ProbeForWrite(Arg7, Arg2 * 8 + 8, 4, Arg4);
    result = ProbeForWrite(4, (uint32_t)(Arg11), 4, Arg4);
    if (0 == 0) goto loc_009DC874;
    *(uint64_t *)(arg7) = 259;
    goto loc_009DC87F;
loc_009DC874:
    *(uint32_t *)(arg7) = 259;
    *(uint64_t *)(arg7 + 0x8) = 0;
loc_009DC87F:
    if (Arg12 == 0) goto loc_009DC89E;
    v_stack_m280 = 2;
    goto loc_009DC904;
loc_009DC89E:
    goto loc_009DC904;
loc_009DC8BF:
    if (Arg12 == 0) goto loc_009DC8F3;
    v_stack_m280 = 3;
    if ((uint32_t)((uint32_t)(Arg2)) == 0) goto loc_009DC8F7;
loc_009DC8D7:
    result = CmpReleaseShutdownRundown(v_stack_m287, (uint32_t)(Arg11), 4, Arg4);
    result = CmCleanupThreadInfo(v_stack_m248, (uint32_t)(Arg11), 4, Arg4);
    goto loc_009DD2DE;
loc_009DC8F3:
loc_009DC8F7:
loc_009DC8FE:
loc_009DC904:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg8)))) & (0x1000000FULL));
    if (((uint32_t)((uint32_t)(Arg8))) != ((uint32_t)(result))) goto loc_009DC8D7;
    Arg2 = 0;
    v_stack_m2A0 = 0;
    v_stack_m2A8 = v_stack_m260;
    result = CmObReferenceObjectByHandle(v_stack_m270, 16, 4, (uint8_t)(v_stack_m248));
    if (sign_flag) goto loc_009DD2CA;
    local_rbx = 0;
    v_stack_m270 = 0;
    if (((uint32_t)((uint32_t)(Arg2))) != 1) goto loc_009DC9D5;
    result = CmpInitializeParseContext(v_stack_m218, 16, 4, (uint8_t)(v_stack_m248));
    v_stack_m298 = v_stack_m270;
    v_stack_m2A0 = v_stack_m218;
    v_stack_m2A8 = (uint8_t)(v_stack_m287);
    Arg2 = 0;
    result = CmObReferenceObjectByName(v_stack_m250, Arg2, local_rbx + 16, (uint8_t)(v_stack_m248));
    Arg2 = 0;
    result = CmpCleanupParseContext(v_stack_m218, Arg2, local_rbx + 16, (uint8_t)(v_stack_m248));
    if (sign_flag) goto loc_009DD2B7;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m260 + 0x8) + 0x20)) != (*(uint64_t *)(*(uint64_t *)(v_stack_m270 + 0x8) + 0x20))) goto loc_009DC9DC;
    result = ObfDereferenceObject(v_stack_m270, *(uint64_t *)(v_stack_m260 + 0x8), local_rbx + 16, (uint8_t)(v_stack_m248));
    goto loc_009DD2B7;
loc_009DC9D5:
    goto loc_009DC9DE;
loc_009DC9DC:
    local_rbx = 0;
loc_009DC9DE:
    Arg4 = 0;
    Arg3 = 0;
    result = CmpAllocatePostBlock((uint32_t)((uint32_t)((uint32_t)(v_stack_m280))), (uint32_t)(0x10000ULL), Arg3, Arg4);
    v_stack_m250 = result;
    if (result != 0) goto loc_009DCA15;
    if (((uint32_t)((uint32_t)(Arg2))) == 1) {
        Arg1 = v_stack_m270;
        result = ObfDereferenceObject(Arg1, (uint32_t)(0x10000ULL), Arg3, Arg4);
    }
    goto loc_009DD2B7;
loc_009DCA15:
    if (((uint32_t)((uint32_t)(Arg2))) != 1) goto loc_009DCA56;
    Arg2 = 0;
    result = CmpAllocatePostBlock((uint32_t)(v_stack_m280), Arg2, v_stack_m270, result);
    v_stack_m230 = result;
    if (result != 0) goto loc_009DCA56;
    result = ObfDereferenceObject(v_stack_m270, Arg2, v_stack_m270, result);
    result = CmpFreePostBlock(result, Arg2, v_stack_m270, result);
    goto loc_009DD2B7;
loc_009DCA56:
    if (((uint32_t)((uint32_t)(v_stack_m280))) == 1) goto loc_009DCB94;
    if (v_stack_m228 == 0) goto loc_009DCAD5;
    v_stack_m278 = (uint32_t)(0xC000009AULL);
    v_stack_m2A0 = (uint32_t)(0xC000009AULL);
    v_stack_m2A8 = v_stack_m278;
    result = ObReferenceObjectByHandle(v_stack_m228, 2, *(uint64_t *)(v_rip + 0x5EA109), v_stack_m287);
    v_stack_m278 = v_stack_m278;
    if (!sign_flag) goto loc_009DCAC7;
    if (((uint32_t)((uint32_t)(Arg2))) == 1) {
        Arg1 = result;
        result = CmpFreePostBlock(Arg1, 2, *(uint64_t *)(v_rip + 0x5EA109), v_stack_m287);
    }
    result = CmpFreePostBlock(result, 2, *(uint64_t *)(v_rip + 0x5EA109), v_stack_m287);
    goto loc_009DD2B7;
loc_009DCAC7:
    result = KeResetEvent(result, 2, *(uint64_t *)(v_rip + 0x5EA109), v_stack_m287);
    goto loc_009DCADA;
loc_009DCAD5:
loc_009DCADA:
    if (((uint32_t)((uint32_t)(v_stack_m280))) != 2) goto loc_009DCB6C;
    *(uint64_t *)(*(uint64_t *)(result + 0x40) + 0x68) = v_stack_m258;
    *(uint64_t *)(*(uint64_t *)(result + 0x40) + 0x8) = v_stack_m278;
    Arg4 = v_stack_m287;
    if (Arg5 == 0) { Arg4 = 0; }
    Arg3 = v_rip + 557630;
    if (Arg5 != 0) { Arg3 = Arg5; }
    Arg1 = (*(uint64_t *)(result + 0x40)) + (16);
    v_stack_m290 = Arg6;
    v_stack_m298 = (uint8_t)(Arg4);
    v_stack_m2A0 = Arg3;
    v_stack_m2A8 = v_rip - 2075580;
    result = KeInitializeApc(Arg1, *(uint64_t *)(gs_base + (0 + 0x188)), 2, v_rip + 1158552);
    goto loc_009DCB99;
loc_009DCB6C:
    *(uint64_t *)(result) = v_stack_m278;
    if (((uint32_t)(Arg1)) == 4) goto loc_009DCB99;
    *(uint64_t *)(*(uint64_t *)(result + 0x40) + 0x8) = Arg5;
    *(uint32_t *)(*(uint64_t *)(result + 0x40) + 0x10) = (uint32_t)((uint32_t)(Arg6));
    goto loc_009DCB99;
loc_009DCB94:
loc_009DCB99:
    result = CmpLockRegistry(*(uint64_t *)(result + 0x40), *(uint64_t *)(gs_base + (0 + 0x188)), 2, v_rip + 1158552);
    if (((uint32_t)((uint32_t)(Arg2))) != 1) goto loc_009DCBB3;
    result = CmpLockTwoKcbsShared(*(uint64_t *)(v_stack_m260 + 0x8), *(uint64_t *)(v_stack_m270 + 0x8), 2, v_rip + 1158552);
    goto loc_009DCBB8;
loc_009DCBB3:
    result = CmpLockKcbShared(*(uint64_t *)(v_stack_m260 + 0x8), *(uint64_t *)(v_stack_m270 + 0x8), 2, v_rip + 1158552);
loc_009DCBB8:
    Arg2 = 0;
    result = CmpIsKeyDeletedForKeyBody(v_stack_m260, Arg2, 2, v_rip + 1158552);
    if ((uint8_t)(result) != 0) goto loc_009DD270;
    if (((uint32_t)((uint32_t)(Arg2))) != 1) goto loc_009DCC49;
    Arg2 = 0;
    result = CmpIsKeyDeletedForKeyBody(v_stack_m270, Arg2, 2, v_rip + 1158552);
    if ((uint8_t)(result) != 0) goto loc_009DD270;
    if (((uint32_t)((uint32_t)(Arg2))) != ((uint32_t)((uint32_t)(Arg2)))) goto loc_009DCC49;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m260 + 0x8) + 0x20)) == (*(uint64_t *)(*(uint64_t *)(v_stack_m270 + 0x8) + 0x20))) goto loc_009DCC49;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_m260 + 0x8) + 0x20)) >= (*(uint64_t *)(*(uint64_t *)(v_stack_m270 + 0x8) + 0x20))) goto loc_009DCC1F;
    result = CmLockHive(*(uint64_t *)(*(uint64_t *)(v_stack_m260 + 0x8) + 0x20), *(uint64_t *)(*(uint64_t *)(v_stack_m270 + 0x8) + 0x20), 2, v_rip + 1158552);
    result = CmLockHive(*(uint64_t *)(*(uint64_t *)(v_stack_m270 + 0x8) + 0x20), *(uint64_t *)(*(uint64_t *)(v_stack_m270 + 0x8) + 0x20), 2, v_rip + 1158552);
    v_stack_m268 = *(uint64_t *)(*(uint64_t *)(v_stack_m270 + 0x8) + 0x20);
    goto loc_009DCC5C;
loc_009DCC1F:
    result = CmLockHive(*(uint64_t *)(*(uint64_t *)(v_stack_m270 + 0x8) + 0x20), *(uint64_t *)(*(uint64_t *)(v_stack_m270 + 0x8) + 0x20), 2, v_rip + 1158552);
    result = CmLockHive(*(uint64_t *)(*(uint64_t *)(v_stack_m260 + 0x8) + 0x20), *(uint64_t *)(*(uint64_t *)(v_stack_m270 + 0x8) + 0x20), 2, v_rip + 1158552);
    v_stack_m268 = *(uint64_t *)(*(uint64_t *)(v_stack_m270 + 0x8) + 0x20);
    goto loc_009DCC5C;
loc_009DCC49:
    result = CmLockHive(*(uint64_t *)(*(uint64_t *)(v_stack_m260 + 0x8) + 0x20), *(uint64_t *)(*(uint64_t *)(v_stack_m270 + 0x8) + 0x20), 2, v_rip + 1158552);
loc_009DCC5C:
    result = ExAcquireFastMutexUnsafe(v_rip + 5344477, *(uint64_t *)(*(uint64_t *)(v_stack_m270 + 0x8) + 0x20), 2, v_rip + 1158552);
    v_stack_m298 = result;
    result = CmpNotifyChangeKey(v_stack_m260, result, (uint32_t)(Arg8), Arg9);
    if (!sign_flag) goto loc_009DCD2B;
    result = ExReleaseFastMutexUnsafe(v_rip + 5344422, result, (uint32_t)(Arg8), Arg9);
    if (1 != 1) goto loc_009DCCAF;
    goto loc_009DCCE1;
loc_009DCCAF:
    if (1 != 2) goto loc_009DCCC9;
    result = CmUnlockHive(v_stack_m268, result, (uint32_t)(Arg8), Arg9);
    goto loc_009DCCE1;
loc_009DCCC9:
    if (1 != 3) goto loc_009DCCE6;
    result = CmUnlockHive(*(uint64_t *)(*(uint64_t *)(v_stack_m260 + 0x8) + 0x20), result, (uint32_t)(Arg8), Arg9);
loc_009DCCE1:
    result = CmUnlockHive(v_stack_m268, result, (uint32_t)(Arg8), Arg9);
loc_009DCCE6:
    if (((uint32_t)((uint32_t)(Arg2))) != 1) goto loc_009DCCFB;
    result = CmpUnlockTwoKcbs(*(uint64_t *)(v_stack_m260 + 0x8), *(uint64_t *)(v_stack_m270 + 0x8), (uint32_t)(Arg8), Arg9);
    goto loc_009DCD00;
loc_009DCCFB:
    result = CmpUnlockKcb(*(uint64_t *)(v_stack_m260 + 0x8), *(uint64_t *)(v_stack_m270 + 0x8), (uint32_t)(Arg8), Arg9);
loc_009DCD00:
    result = CmpUnlockRegistry(*(uint64_t *)(v_stack_m260 + 0x8), *(uint64_t *)(v_stack_m270 + 0x8), (uint32_t)(Arg8), Arg9);
    if (v_stack_m278 != 0) {
        result = ObfDereferenceObject(v_stack_m278, *(uint64_t *)(v_stack_m270 + 0x8), (uint32_t)(Arg8), Arg9);
    }
    if (((uint32_t)((uint32_t)(Arg2))) != 1) goto loc_009DD2B7;
    result = CmpFreePostBlock(result, *(uint64_t *)(v_stack_m270 + 0x8), (uint32_t)(Arg8), Arg9);
    goto loc_009DD2B7;
loc_009DCD2B:
    v_stack_m286 = (uint8_t)(v_stack_m285);
    if (((uint32_t)((uint32_t)(Arg2))) != 1) goto loc_009DCE29;
    result = ObfReferenceObject(v_stack_m270, *(uint64_t *)(v_stack_m270 + 0x8), (uint32_t)(Arg8), Arg9);
    if ((uint32_t)((uint32_t)((uint32_t)(result))) != 0) goto loc_009DCD5B;
    result = CmpFreePostBlock(result, *(uint64_t *)(v_stack_m270 + 0x8), (uint32_t)(Arg8), Arg9);
    v_stack_m286 = (uint8_t)((uint32_t)((uint32_t)(result)));
    goto loc_009DCE29;
loc_009DCD5B:
    v_stack_m298 = result;
    result = CmpNotifyChangeKey(v_stack_m270, result, (uint32_t)(Arg8), Arg9);
    v_stack_m286 = (uint8_t)(v_stack_m285);
    if (!sign_flag) goto loc_009DCE29;
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x8)) != result) goto loc_009DD250;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) != result) goto loc_009DD250;
    *(uint64_t *)(*(uint64_t *)(result + 0x8)) = *(uint64_t *)(result);
    *(uint64_t *)(*(uint64_t *)(result) + 0x8) = *(uint64_t *)(result + 0x8);
    v_stack_m270 = v_cr8;
    result = 1;
    if ((*(uint32_t *)(v_rip + 0x5E9F57)) != 0) {
        Arg2 = 1;
        Arg1 = (uint8_t)(v_cr8);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, v_cr8, Arg9);
        Arg3 = v_stack_m270;
    }
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8)) != (result + 16)) goto loc_009DD250;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x10 + 0x8))) != (result + 16)) goto loc_009DD250;
    *(uint64_t *)(*(uint64_t *)(result + 0x10 + 0x8)) = *(uint64_t *)(result + 0x10);
    *(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8) = *(uint64_t *)(result + 0x10 + 0x8);
    result = result + 16;
    if ((*(uint32_t *)(v_rip + 0x5E9F18)) != 0) {
        Arg1 = 1;
        Arg2 = (uint8_t)(Arg3);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, Arg3, Arg9);
    }
    v_stack_m286 = (uint8_t)(v_stack_m285);
loc_009DCE29:
    result = ExReleaseFastMutexUnsafe(v_rip + 5344016, Arg2, Arg3, Arg9);
    if (1 != 1) goto loc_009DCE45;
    goto loc_009DCE77;
loc_009DCE45:
    if (1 != 2) goto loc_009DCE5F;
    result = CmUnlockHive(v_stack_m268, Arg2, Arg3, Arg9);
    goto loc_009DCE77;
loc_009DCE5F:
    if (1 != 3) goto loc_009DCE7C;
    result = CmUnlockHive(*(uint64_t *)(*(uint64_t *)(v_stack_m260 + 0x8) + 0x20), Arg2, Arg3, Arg9);
loc_009DCE77:
    result = CmUnlockHive(v_stack_m268, Arg2, Arg3, Arg9);
loc_009DCE7C:
    if (((uint32_t)((uint32_t)(Arg2))) != 1) goto loc_009DCE91;
    result = CmpUnlockTwoKcbs(*(uint64_t *)(v_stack_m260 + 0x8), *(uint64_t *)(v_stack_m270 + 0x8), Arg3, Arg9);
    goto loc_009DCE96;
loc_009DCE91:
    result = CmpUnlockKcb(*(uint64_t *)(v_stack_m260 + 0x8), *(uint64_t *)(v_stack_m270 + 0x8), Arg3, Arg9);
loc_009DCE96:
    result = CmpUnlockRegistry(*(uint64_t *)(v_stack_m260 + 0x8), *(uint64_t *)(v_stack_m270 + 0x8), Arg3, Arg9);
    if (v_stack_m270 != 0) {
        Arg1 = v_stack_m270;
        result = ObfDereferenceObject(Arg1, *(uint64_t *)(v_stack_m270 + 0x8), Arg3, Arg9);
    }
    if (sign_flag) goto loc_009DD257;
    if (v_stack_m280 != 1) goto loc_009DD2B7;
    result = CmpReleaseShutdownRundown(Arg1, *(uint64_t *)(v_stack_m270 + 0x8), Arg3, Arg9);
    local_r12 = 0;
    v_stack_m288 = 0;
    v_stack_m285 = 0;
    local_r13 = 0;
    v_stack_m2A8 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(*(uint64_t *)(result + 0x40), Arg2, v_stack_m287, 1);
    if (((uint32_t)(result)) == 257) goto loc_009DD0D2;
    if (((uint32_t)(result)) == 192) goto loc_009DD0D2;
    result = CmpLockRegistry(*(uint64_t *)(result + 0x40), Arg2, v_stack_m287, 1);
    result = ExAcquireFastMutexUnsafe(v_rip + 5343795, Arg2, v_stack_m287, 1);
    result = 1;
    if ((*(uint32_t *)(v_rip + 0x5E9DFA)) != 0) {
        Arg2 = 1;
        Arg1 = (uint8_t)(v_stack_m270);
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, v_stack_m287, 1);
    }
    if ((uint8_t)(v_stack_m286) == 0) goto loc_009DCFF9;
    result = Feature_2602282298__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, v_stack_m287, 1);
    if ((uint32_t)(result) == 0) goto loc_009DCFB1;
    if (*(uint64_t *)(result) == 0) goto loc_009DCF78;
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x8)) != result) goto loc_009DD250;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) != result) goto loc_009DD250;
    *(uint64_t *)(*(uint64_t *)(result + 0x8)) = *(uint64_t *)(result);
    *(uint64_t *)(*(uint64_t *)(result) + 0x8) = *(uint64_t *)(result + 0x8);
    *(uint64_t *)(result) = 0;
    *(uint64_t *)(result + 0x8) = 0;
loc_009DCF78:
    if (*(uint64_t *)(result + 0x10) != 0) goto loc_009DCF8A;
    if ((*(uint64_t *)(result + 0x10 + 0x8)) == 0) goto loc_009DCFF9;
loc_009DCF8A:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8)) != (result + 16)) goto loc_009DD250;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x10 + 0x8))) != (result + 16)) goto loc_009DD250;
    *(uint64_t *)(*(uint64_t *)(result + 0x10 + 0x8)) = *(uint64_t *)(result + 0x10);
    *(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8) = *(uint64_t *)(result + 0x10 + 0x8);
    *(uint64_t *)(result + 0x10) = 0;
    *(uint64_t *)(result + 0x10 + 0x8) = 0;
    goto loc_009DCFF9;
loc_009DCFB1:
    if (result + 16 == 0) goto loc_009DCFD4;
    if ((*(uint64_t *)(result + 0x10 + 0x8)) != result) goto loc_009DD250;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) != result) goto loc_009DD250;
    *(uint64_t *)(*(uint64_t *)(result + 0x8)) = result + 16;
    *(uint64_t *)(result + 0x10 + 0x8) = *(uint64_t *)(result + 0x8);
loc_009DCFD4:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8)) != (result + 16)) goto loc_009DD250;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x10 + 0x8))) != (result + 16)) goto loc_009DD250;
    *(uint64_t *)(*(uint64_t *)(result + 0x10 + 0x8)) = *(uint64_t *)(result + 0x10);
    *(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8) = *(uint64_t *)(result + 0x10 + 0x8);
loc_009DCFF9:
    if (*(uint64_t *)(result) == 0) goto loc_009DD01F;
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x8)) != result) goto loc_009DD250;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) != result) goto loc_009DD250;
    *(uint64_t *)(*(uint64_t *)(result + 0x8)) = *(uint64_t *)(result);
    *(uint64_t *)(*(uint64_t *)(result) + 0x8) = *(uint64_t *)(result + 0x8);
loc_009DD01F:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8)) != (result + 16)) goto loc_009DD250;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x10 + 0x8))) != (result + 16)) goto loc_009DD250;
    *(uint64_t *)(*(uint64_t *)(result + 0x10 + 0x8)) = *(uint64_t *)(result + 0x10);
    *(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8) = *(uint64_t *)(result + 0x10 + 0x8);
    result = result + 16;
    if ((*(uint32_t *)(v_rip + 0x5E9CD5)) != 0) {
        Arg1 = 1;
        Arg2 = (uint8_t)(v_stack_m270);
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(result + 0x10 + 0x8), 1);
    }
    result = ExReleaseFastMutexUnsafe(v_rip + 5343449, Arg2, *(uint64_t *)(result + 0x10 + 0x8), 1);
    result = CmpUnlockRegistry(v_rip + 5343449, Arg2, *(uint64_t *)(result + 0x10 + 0x8), 1);
    *(uint32_t *)(v_stack_m258) = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x40) + 0x18)));
    if (v_stack_m284 == 0) goto loc_009DD08C;
    *(uint32_t *)(v_stack_m258 + 0x4) = 0;
    goto loc_009DD090;
loc_009DD08C:
    *(uint64_t *)(v_stack_m258 + 0x8) = 0;
loc_009DD090:
    goto loc_009DD0B8;
loc_009DD0B8:
    result = v_stack_m258;
    if ((uint8_t)(v_stack_m286) != 0) {
        Arg1 = result;
        result = CmpFreePostBlock(Arg1, Arg2, *(uint64_t *)(result + 0x10 + 0x8), 1);
    }
    result = CmpFreePostBlock(result, Arg2, *(uint64_t *)(result + 0x10 + 0x8), 1);
    goto loc_009DD2BD;
loc_009DD0D2:
    result = CmpLockRegistry(result, Arg2, *(uint64_t *)(result + 0x10 + 0x8), 1);
    result = ExAcquireFastMutexUnsafe(v_rip + 5343330, Arg2, *(uint64_t *)(result + 0x10 + 0x8), 1);
    result = 1;
    if ((*(uint32_t *)(v_rip + 0x5E9C29)) != 0) {
        Arg2 = 1;
        Arg1 = (uint8_t)((uint8_t)(v_stack_m270));
        result = KiRaiseIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(result + 0x10 + 0x8), 1);
    }
    if ((uint8_t)(v_stack_m286) == 0) goto loc_009DD1CB;
    result = Feature_2602282298__private_IsEnabledDeviceUsageNoInline(Arg1, Arg2, *(uint64_t *)(result + 0x10 + 0x8), 1);
    if ((uint32_t)(result) == 0) goto loc_009DD183;
    if (*(uint64_t *)(result) == 0) goto loc_009DD14A;
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x8)) != result) goto loc_009DD250;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) != result) goto loc_009DD250;
    *(uint64_t *)(*(uint64_t *)(result + 0x8)) = *(uint64_t *)(result);
    *(uint64_t *)(*(uint64_t *)(result) + 0x8) = *(uint64_t *)(result + 0x8);
    *(uint64_t *)(result) = 0;
    *(uint64_t *)(result + 0x8) = 0;
loc_009DD14A:
    if (*(uint64_t *)(result + 0x10) != 0) goto loc_009DD15C;
    if ((*(uint64_t *)(result + 0x10 + 0x8)) == 0) goto loc_009DD1CB;
loc_009DD15C:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8)) != (result + 16)) goto loc_009DD250;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x10 + 0x8))) != (result + 16)) goto loc_009DD250;
    *(uint64_t *)(*(uint64_t *)(result + 0x10 + 0x8)) = *(uint64_t *)(result + 0x10);
    *(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8) = *(uint64_t *)(result + 0x10 + 0x8);
    *(uint64_t *)(result + 0x10) = 0;
    *(uint64_t *)(result + 0x10 + 0x8) = 0;
    goto loc_009DD1CB;
loc_009DD183:
    if (result + 16 == 0) goto loc_009DD1A6;
    if ((*(uint64_t *)(result + 0x10 + 0x8)) != result) goto loc_009DD250;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) != result) goto loc_009DD250;
    *(uint64_t *)(*(uint64_t *)(result + 0x8)) = result + 16;
    *(uint64_t *)(result + 0x10 + 0x8) = *(uint64_t *)(result + 0x8);
loc_009DD1A6:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8)) != (result + 16)) goto loc_009DD250;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x10 + 0x8))) != (result + 16)) goto loc_009DD250;
    *(uint64_t *)(*(uint64_t *)(result + 0x10 + 0x8)) = *(uint64_t *)(result + 0x10);
    *(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8) = *(uint64_t *)(result + 0x10 + 0x8);
loc_009DD1CB:
    if (*(uint64_t *)(result) == 0) goto loc_009DD1E9;
    if ((*(uint64_t *)(*(uint64_t *)(result) + 0x8)) != result) goto loc_009DD250;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x8))) != result) goto loc_009DD250;
    *(uint64_t *)(*(uint64_t *)(result + 0x8)) = *(uint64_t *)(result);
    *(uint64_t *)(*(uint64_t *)(result) + 0x8) = *(uint64_t *)(result + 0x8);
loc_009DD1E9:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8)) != (result + 16)) goto loc_009DD250;
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x10 + 0x8))) != (result + 16)) goto loc_009DD250;
    *(uint64_t *)(*(uint64_t *)(result + 0x10 + 0x8)) = *(uint64_t *)(result + 0x10);
    *(uint64_t *)(*(uint64_t *)(result + 0x10) + 0x8) = *(uint64_t *)(result + 0x10 + 0x8);
    result = result + 16;
    if ((*(uint32_t *)(v_rip + 0x5E9B13)) != 0) {
        Arg1 = 1;
        Arg2 = (uint8_t)((uint8_t)(v_stack_m270));
        result = KiLowerIrqlProcessIrqlFlags(Arg1, Arg2, *(uint64_t *)(result + 0x10 + 0x8), 1);
    }
    result = ExReleaseFastMutexUnsafe(v_rip + 5342997, Arg2, *(uint64_t *)(result + 0x10 + 0x8), 1);
    result = CmpUnlockRegistry(v_rip + 5342997, Arg2, *(uint64_t *)(result + 0x10 + 0x8), 1);
    if ((uint8_t)(v_stack_m286) != 0) {
        Arg1 = result;
        result = CmpFreePostBlock(Arg1, Arg2, *(uint64_t *)(result + 0x10 + 0x8), 1);
    }
    result = CmpFreePostBlock(result, Arg2, *(uint64_t *)(result + 0x10 + 0x8), 1);
    goto loc_009DD2BD;
loc_009DD250:
loc_009DD257:
    result = CmpFreePostBlock(result, Arg2, *(uint64_t *)(result + 0x10 + 0x8), 1);
    if (v_stack_m278 == 0) goto loc_009DD2B7;
    result = ObfDereferenceObject(v_stack_m278, Arg2, *(uint64_t *)(result + 0x10 + 0x8), 1);
    goto loc_009DD2B7;
loc_009DD270:
    if (0 != 1) goto loc_009DD285;
    result = CmpUnlockTwoKcbs(*(uint64_t *)(v_stack_m260 + 0x8), *(uint64_t *)(v_stack_m286 + 0x8), *(uint64_t *)(result + 0x10 + 0x8), 1);
    goto loc_009DD28A;
loc_009DD285:
    result = CmpUnlockKcb(*(uint64_t *)(v_stack_m260 + 0x8), *(uint64_t *)(v_stack_m286 + 0x8), *(uint64_t *)(result + 0x10 + 0x8), 1);
loc_009DD28A:
    result = CmpUnlockRegistry(*(uint64_t *)(v_stack_m260 + 0x8), *(uint64_t *)(v_stack_m286 + 0x8), *(uint64_t *)(result + 0x10 + 0x8), 1);
    if ((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x40) + 0x18)) != 0) {
        Arg1 = (uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x40) + 0x18));
        result = ObfDereferenceObject(Arg1, *(uint64_t *)(v_stack_m286 + 0x8), *(uint64_t *)(result + 0x10 + 0x8), 1);
    }
    if (0 == 1) {
        Arg1 = result;
        result = CmpFreePostBlock(Arg1, *(uint64_t *)(v_stack_m286 + 0x8), *(uint64_t *)(result + 0x10 + 0x8), 1);
    }
    result = CmpFreePostBlock(result, *(uint64_t *)(v_stack_m286 + 0x8), *(uint64_t *)(result + 0x10 + 0x8), 1);
loc_009DD2B7:
loc_009DD2BD:
    result = ObfDereferenceObject(v_stack_m260, *(uint64_t *)(v_stack_m286 + 0x8), *(uint64_t *)(result + 0x10 + 0x8), 1);
    if ((uint8_t)(v_stack_m288) != 0) {
        result = CmpReleaseShutdownRundown(v_stack_m260, *(uint64_t *)(v_stack_m286 + 0x8), *(uint64_t *)(result + 0x10 + 0x8), 1);
    }
    result = CmCleanupThreadInfo(v_stack_m248, *(uint64_t *)(v_stack_m286 + 0x8), *(uint64_t *)(result + 0x10 + 0x8), 1);
loc_009DD2DE:
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint64_t *)(v_stack_m286 + 0x8), *(uint64_t *)(result + 0x10 + 0x8), 1);
    local_rsp = (local_rsp) + (656);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg7` | `+ 0x0` | `32` | `W` |
| `Arg7` | `+ 0x0` | `64` | `W` |
| `Arg7` | `+ 0x8` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009DC6B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
