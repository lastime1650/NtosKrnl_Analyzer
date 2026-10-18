# CmRestoreKey

- RVA: `0x007DCF04`–`0x007DDBD6` (길이 `3,282` bytes)
- VA: `0x00000001407DCF04`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D65E8`
- 디코드: `850`개 명령, `3,282/3,282` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **118**; 고유 호출 대상: **48**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **8**

### Outgoing calls
- `0x007DCFA1` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007DCFBB` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (function, `0x0042A7F0`)
- `0x007DCFF1` → [CmpTraceHiveRestoreStart](../7E/CmpTraceHiveRestoreStart_function_007E6624.md) (function, `0x007E6624`)
- `0x007DD033` → [CmpLoadHiveVolatile](CmpLoadHiveVolatile_function_007DE5F0.md) (function, `0x007DE5F0`)
- `0x007DD048` → [CmpRefreshHive](CmpRefreshHive_function_007DEAD0.md) (function, `0x007DEAD0`)
- `0x007DD0BB` → [CmpCreateHive](../87/CmpCreateHive_function_00879DF0.md) (function, `0x00879DF0`)
- `0x007DD0CC` → [CmpLockRegistryFreezeAware](../9B/CmpLockRegistryFreezeAware_function_009B4AE4.md) (function, `0x009B4AE4`)
- `0x007DD0D7` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (function, `0x00BC9A1C`)
- `0x007DD0F2` → [CmpLogUnsupportedOperation](../9A/CmpLogUnsupportedOperation_function_009AEA40.md) (function, `0x009AEA40`)
- `0x007DD106` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x007DD148` → [HvLockHiveFlusherShared](../84/HvLockHiveFlusherShared_function_0084F95C.md) (function, `0x0084F95C`)
- `0x007DD164` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007DD16B` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007DD1C8` → [CmpCopyKeyPartial](../85/CmpCopyKeyPartial_function_0085AFF4.md) (function, `0x0085AFF4`)
- `0x007DD205` → [HvReallocateCell](../85/HvReallocateCell_function_0085B5D0.md) (function, `0x0085B5D0`)
- `0x007DD232` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x007DD276` → [CmpCopySyncTree](../7F/CmpCopySyncTree_function_007F21A0.md) (function, `0x007F21A0`)
- `0x007DD288` → [HvUnlockHiveFlusherShared](../84/HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x007DD296` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x007DD29B` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DD2B0` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DD2B7` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007DD2D3` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DD2DA` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007DD2E6` → [CmpLockRegistryFreezeAware](../9B/CmpLockRegistryFreezeAware_function_009B4AE4.md) (function, `0x009B4AE4`)
- `0x007DD2EE` → [CmpIsShutdownRundownActive](../../pagecmrc/BC/CmpIsShutdownRundownActive_function_00BC9C20.md) (function, `0x00BC9C20`)
- `0x007DD300` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (function, `0x00BC9480`)
- `0x007DD34F` → [CmpCheckKeyAccess](../A6/CmpCheckKeyAccess_function_00A6DE7C.md) (function, `0x00A6DE7C`)
- `0x007DD373` → [CmpCheckKeyAccess](../A6/CmpCheckKeyAccess_function_00A6DE7C.md) (function, `0x00A6DE7C`)
- `0x007DD38B` → [CmpTryAcquireKcbIXLocks](../9B/CmpTryAcquireKcbIXLocks_function_009B056C.md) (function, `0x009B056C`)
- `0x007DD3A9` → [CmpLogTransactionAbortedWithChildName](../9A/CmpLogTransactionAbortedWithChildName_function_009AED70.md) (function, `0x009AED70`)
- `0x007DD3AE` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DD3B9` → [CmpAbortRollbackPacket](../AB/CmpAbortRollbackPacket_function_00ABEA80.md) (function, `0x00ABEA80`)
- `0x007DD3CC` → [CmpCleanupRollbackPacket](../9B/CmpCleanupRollbackPacket_function_009B014C.md) (function, `0x009B014C`)
- `0x007DD3DC` → [CmpRetryBackOff](../94/CmpRetryBackOff_function_0094B474.md) (function, `0x0094B474`)
- `0x007DD3E3` → [CmpLockRegistryFreezeAware](../9B/CmpLockRegistryFreezeAware_function_009B4AE4.md) (function, `0x009B4AE4`)
- `0x007DD40D` → [CmpDoAccessCheckOnSubtree](../../pagecmrc/BC/CmpDoAccessCheckOnSubtree_function_00BC9CD0.md) (function, `0x00BC9CD0`)
- `0x007DD42F` → [CmpPrepareToInvalidateAllHigherLayerKcbs](../7F/CmpPrepareToInvalidateAllHigherLayerKcbs_function_007F174C.md) (function, `0x007F174C`)
- `0x007DD454` → [CmpPrepareForSubtreeInvalidation](../9B/CmpPrepareForSubtreeInvalidation_function_009B01B0.md) (function, `0x009B01B0`)
- `0x007DD47C` → [CmpLogTransactionAbortedWithChildName](../9A/CmpLogTransactionAbortedWithChildName_function_009AED70.md) (function, `0x009AED70`)
- `0x007DD481` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DD491` → [CmpAbortRollbackPacket](../AB/CmpAbortRollbackPacket_function_00ABEA80.md) (function, `0x00ABEA80`)
- `0x007DD4A0` → [CmpCleanupRollbackPacket](../9B/CmpCleanupRollbackPacket_function_009B014C.md) (function, `0x009B014C`)
- `0x007DD4B0` → [CmpRetryBackOff](../94/CmpRetryBackOff_function_0094B474.md) (function, `0x0094B474`)
- `0x007DD4BE` → [CmpLockRegistryFreezeAware](../9B/CmpLockRegistryFreezeAware_function_009B4AE4.md) (function, `0x009B4AE4`)
- `0x007DD4D9` → [CmpInvalidateAllHigherLayerKcbs](../7F/CmpInvalidateAllHigherLayerKcbs_function_007F1560.md) (function, `0x007F1560`)
- `0x007DD4F5` → [CmpInvalidateSubtree](../7E/CmpInvalidateSubtree_function_007EAEC0.md) (function, `0x007EAEC0`)
- `0x007DD500` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)
- `0x007DD509` → [CmpLockRegistryFreezeAware](../9B/CmpLockRegistryFreezeAware_function_009B4AE4.md) (function, `0x009B4AE4`)
- `0x007DD51E` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (function, `0x0042A7F0`)
- `0x007DD54A` → [CmpEnumerateAllHigherLayerKcbs](../A5/CmpEnumerateAllHigherLayerKcbs_function_00A55234.md) (function, `0x00A55234`)
- `0x007DD555` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)
- `0x007DD55D` → [CmpDoesKeyHaveOpenSubkeys](../9B/CmpDoesKeyHaveOpenSubkeys_function_009B0274.md) (function, `0x009B0274`)
- `0x007DD582` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x007DD5A7` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007DD5AE` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007DD5EB` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007DD5F2` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007DD623` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DD62A` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007DD642` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007DD649` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007DD672` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DD679` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007DD692` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x007DD6B4` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007DD6BB` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007DD6E6` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DD6ED` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007DD704` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007DD70B` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007DD768` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007DD76F` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007DD790` → [HvpMarkCellDirty](../85/HvpMarkCellDirty_function_00858080.md) (function, `0x00858080`)
- `0x007DD7F3` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DD7FA` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007DD816` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007DD838` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DD850` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DD857` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007DD890` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007DD897` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007DD8B2` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007DD8B9` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007DD8DA` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DD8E1` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007DD8FC` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DD903` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007DD913` → [CmpCleanUpKcbCachedSymlink](../84/CmpCleanUpKcbCachedSymlink_function_0084DF6C.md) (function, `0x0084DF6C`)
- `0x007DD938` → [HvpGetCellFlat](../85/HvpGetCellFlat_function_00854C60.md) (function, `0x00854C60`)
- `0x007DD93F` → [HvpGetCellPaged](../85/HvpGetCellPaged_function_00854CB0.md) (function, `0x00854CB0`)
- `0x007DD984` → [CmpAssignSecurityToKcb](../9D/CmpAssignSecurityToKcb_function_009DA720.md) (function, `0x009DA720`)
- `0x007DD98E` → [CmpCleanUpSubKeyInfo](../84/CmpCleanUpSubKeyInfo_function_0084C6F4.md) (function, `0x0084C6F4`)
- `0x007DDA10` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DDA17` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007DDA2B` → [CmpDeleteTree](../7F/CmpDeleteTree_function_007F3E44.md) (function, `0x007F3E44`)
- `0x007DDA3C` → [CmpFreeKeyByCell](../84/CmpFreeKeyByCell_function_0084AD70.md) (function, `0x0084AD70`)
- `0x007DDA4E` → [CmpReportNotify](../8C/CmpReportNotify_function_008C8094.md) (function, `0x008C8094`)
- `0x007DDA77` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)
- `0x007DDA7C` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DDA88` → [CmpDestroyHive](../9B/CmpDestroyHive_function_009B1708.md) (function, `0x009B1708`)
- `0x007DDA95` → [CmpSignalDeferredPosts](../84/CmpSignalDeferredPosts_function_008484B0.md) (function, `0x008484B0`)
- `0x007DDAD2` → [CmpDeleteTree](../7F/CmpDeleteTree_function_007F3E44.md) (function, `0x007F3E44`)
- `0x007DDAE4` → [CmpFreeKeyByCell](../84/CmpFreeKeyByCell_function_0084AD70.md) (function, `0x0084AD70`)
- `0x007DDAF1` → [HvUnlockHiveFlusherShared](../84/HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x007DDAFE` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x007DDB13` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)
- `0x007DDB1D` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DDB2B` → [CmpDestroyHive](../9B/CmpDestroyHive_function_009B1708.md) (function, `0x009B1708`)
- `0x007DDB4A` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DDB51` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007DDB6B` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DDB72` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007DDB8D` → [HvpReleaseCellFlat](../85/HvpReleaseCellFlat_function_0085CC20.md) (function, `0x0085CC20`)
- `0x007DDB94` → [HvpReleaseCellPaged](../85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x007DDB9D` → [CmpCleanupRollbackPacket](../9B/CmpCleanupRollbackPacket_function_009B014C.md) (function, `0x009B014C`)
- `0x007DDBA4` → [CmpTraceHiveRestoreStop](../7E/CmpTraceHiveRestoreStop_function_007E6738.md) (function, `0x007E6738`)
- `0x007DDBB5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [NtRestoreKey](../7E/NtRestoreKey_function_007E0CC0.md) at `0x007E0E8D`

### Static image references
- `0x007DCF23` → RVA `0x00E0A740` (`.data`; read)
- `0x007DD129` → RVA `0x00FD9A90` (`PAGEDATA`; read)
- `0x007DD534` → RVA `0x007F1450` (`CmpCleanUpHigherLayerKcbCachesPostCallback`; read)
- `0x007DD540` → RVA `0x0070BAD0` (`CmpCleanUpHigherLayerKcbCachesPreCallback`; read)
- `0x007DDA53` → RVA `0x00FD9A62` (`PAGEDATA`; read)
- `0x007DDA5C` → RVA `0x00FD8060` (`PAGEDATA`; read)
- `0x007DDA63` → RVA `0x00FD81C0` (`PAGEDATA`; write)
- `0x007DDA6A` → RVA `0x00FD9A62` (`PAGEDATA`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **21**
  - `0x007DCFA1` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007DCFBB` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (`PAGE` → `.text`)
  - `0x007DD0D7` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (`PAGE` → `PAGECMRC`)
  - `0x007DD106` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x007DD232` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x007DD296` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x007DD29B` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DD2EE` → [CmpIsShutdownRundownActive](../../pagecmrc/BC/CmpIsShutdownRundownActive_function_00BC9C20.md) (`PAGE` → `PAGECMRC`)
  - `0x007DD300` → [CmpIsKeyDeletedForKeyBody](../../pagecmrc/BC/CmpIsKeyDeletedForKeyBody_function_00BC9480.md) (`PAGE` → `PAGECMRC`)
  - `0x007DD3AE` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DD40D` → [CmpDoAccessCheckOnSubtree](../../pagecmrc/BC/CmpDoAccessCheckOnSubtree_function_00BC9CD0.md) (`PAGE` → `PAGECMRC`)
  - `0x007DD481` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DD500` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
  - `0x007DD51E` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (`PAGE` → `.text`)
  - `0x007DD555` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
  - `0x007DDA77` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
  - `0x007DDA7C` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DDAFE` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x007DDB13` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
  - `0x007DDB1D` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DDBB5` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007DCF04  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
007DCF09  55                              push rbp
007DCF0A  56                              push rsi
007DCF0B  57                              push rdi
007DCF0C  41 54                           push r12
007DCF0E  41 55                           push r13
007DCF10  41 56                           push r14
007DCF12  41 57                           push r15
007DCF14  48 8D AC 24 F0 FD FF FF         lea rbp, [rsp - 0x210]
007DCF1C  48 81 EC 10 03 00 00            sub rsp, 0x310
007DCF23  48 8B 05 16 D8 62 00            mov rax, qword ptr [rip + 0x62d816]
007DCF2A  48 33 C4                        xor rax, rsp
007DCF2D  48 89 85 00 02 00 00            mov qword ptr [rbp + 0x200], rax
007DCF34  33 FF                           xor edi, edi
007DCF36  44 89 45 E8                     mov dword ptr [rbp - 0x18], r8d
007DCF3A  41 83 CE FF                     or r14d, 0xffffffff
007DCF3E  44 88 4C 24 74                  mov byte ptr [rsp + 0x74], r9b
007DCF43  0F 57 C0                        xorps xmm0, xmm0
007DCF46  48 89 7D F0                     mov qword ptr [rbp - 0x10], rdi
007DCF4A  8B C7                           mov eax, edi
007DCF4C  44 89 75 B8                     mov dword ptr [rbp - 0x48], r14d
007DCF50  45 8B F8                        mov r15d, r8d
007DCF53  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
007DCF57  48 8B DA                        mov rbx, rdx
007DCF5A  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
007DCF5E  4C 8B E1                        mov r12, rcx
007DCF61  89 7D BC                        mov dword ptr [rbp - 0x44], edi
007DCF64  33 D2                           xor edx, edx
007DCF66  44 89 75 A0                     mov dword ptr [rbp - 0x60], r14d
007DCF6A  41 B8 B0 01 00 00               mov r8d, 0x1b0
007DCF70  89 7D A4                        mov dword ptr [rbp - 0x5c], edi
007DCF73  48 8D 4D 50                     lea rcx, [rbp + 0x50]
007DCF77  44 89 75 80                     mov dword ptr [rbp - 0x80], r14d
007DCF7B  44 8B EF                        mov r13d, edi
007DCF7E  89 7D 84                        mov dword ptr [rbp - 0x7c], edi
007DCF81  44 89 75 90                     mov dword ptr [rbp - 0x70], r14d
007DCF85  89 7D 94                        mov dword ptr [rbp - 0x6c], edi
007DCF88  48 89 7D B0                     mov qword ptr [rbp - 0x50], rdi
007DCF8C  44 89 74 24 78                  mov dword ptr [rsp + 0x78], r14d
007DCF91  89 7C 24 7C                     mov dword ptr [rsp + 0x7c], edi
007DCF95  0F 11 45 28                     movups xmmword ptr [rbp + 0x28], xmm0
007DCF99  0F 11 45 38                     movups xmmword ptr [rbp + 0x38], xmm0
007DCF9D  0F 11 45 08                     movups xmmword ptr [rbp + 8], xmm0
007DCFA1  E8 9A 9C EE FF                  call 0x1406c6c40
007DCFA6  0F 57 C0                        xorps xmm0, xmm0
007DCFA9  89 7D 98                        mov dword ptr [rbp - 0x68], edi
007DCFAC  0F 57 C9                        xorps xmm1, xmm1
007DCFAF  48 8D 4D F8                     lea rcx, [rbp - 8]
007DCFB3  0F 11 45 F8                     movups xmmword ptr [rbp - 8], xmm0
007DCFB7  0F 11 4D D0                     movups xmmword ptr [rbp - 0x30], xmm1
007DCFBB  E8 30 D8 C4 FF                  call 0x14042a7f0
007DCFC0  44 89 75 E0                     mov dword ptr [rbp - 0x20], r14d
007DCFC4  40 8A F7                        mov sil, dil
007DCFC7  44 89 74 24 70                  mov dword ptr [rsp + 0x70], r14d
007DCFCC  4D 8B 74 24 08                  mov r14, qword ptr [r12 + 8]
007DCFD1  49 8B 7E 20                     mov rdi, qword ptr [r14 + 0x20]
007DCFD5  F7 87 A0 00 00 00 00 00 10 00   test dword ptr [rdi + 0xa0], 0x100000
007DCFDF  74 0A                           je 0x1407dcfeb
007DCFE1  BB 22 00 00 C0                  mov ebx, 0xc0000022
007DCFE6  E9 1F 0B 00 00                  jmp 0x1407ddb0a
007DCFEB  41 8B D7                        mov edx, r15d
007DCFEE  48 8B CB                        mov rcx, rbx
007DCFF1  E8 2E 96 00 00                  call 0x1407e6624
007DCFF6  41 F7 C7 FD FF FF FF            test r15d, 0xfffffffd
007DCFFD  0F 95 C1                        setne cl
007DD000  41 F6 C7 02                     test r15b, 2
007DD004  0F 95 C0                        setne al
007DD007  84 C8                           test al, cl
007DD009  0F 85 F6 0A 00 00               jne 0x1407ddb05
007DD00F  33 C0                           xor eax, eax
007DD011  49 39 44 24 38                  cmp qword ptr [r12 + 0x38], rax
007DD016  0F 85 E9 0A 00 00               jne 0x1407ddb05
007DD01C  49 39 44 24 40                  cmp qword ptr [r12 + 0x40], rax
007DD021  0F 85 DE 0A 00 00               jne 0x1407ddb05
007DD027  41 F6 C7 01                     test r15b, 1
007DD02B  74 12                           je 0x1407dd03f
007DD02D  48 8B D3                        mov rdx, rbx
007DD030  49 8B CC                        mov rcx, r12
007DD033  E8 B8 15 00 00                  call 0x1407de5f0
007DD038  8B D8                           mov ebx, eax
007DD03A  E9 CB 0A 00 00                  jmp 0x1407ddb0a
007DD03F  41 F6 C7 02                     test r15b, 2
007DD043  74 0A                           je 0x1407dd04f
007DD045  49 8B CC                        mov rcx, r12
007DD048  E8 83 1A 00 00                  call 0x1407dead0
007DD04D  EB E9                           jmp 0x1407dd038
007DD04F  45 33 FF                        xor r15d, r15d
007DD052  48 89 5D 28                     mov qword ptr [rbp + 0x28], rbx
007DD056  48 8D 45 08                     lea rax, [rbp + 8]
007DD05A  4C 89 7D 40                     mov qword ptr [rbp + 0x40], r15
007DD05E  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
007DD062  48 8D 4D B0                     lea rcx, [rbp - 0x50]
007DD066  48 8D 45 08                     lea rax, [rbp + 8]
007DD06A  0F 57 C0                        xorps xmm0, xmm0
007DD06D  48 89 45 08                     mov qword ptr [rbp + 8], rax
007DD071  41 8D 57 02                     lea edx, [r15 + 2]
007DD075  48 8D 45 50                     lea rax, [rbp + 0x50]
007DD079  45 33 C9                        xor r9d, r9d
007DD07C  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
007DD081  41 B8 00 80 00 00               mov r8d, 0x8000
007DD087  4C 89 7C 24 58                  mov qword ptr [rsp + 0x58], r15
007DD08C  48 8D 45 28                     lea rax, [rbp + 0x28]
007DD090  4C 89 7C 24 50                  mov qword ptr [rsp + 0x50], r15
007DD095  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
007DD09A  4C 89 7C 24 40                  mov qword ptr [rsp + 0x40], r15
007DD09F  C7 44 24 38 01 00 19 01         mov dword ptr [rsp + 0x38], 0x1190001
007DD0A7  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
007DD0AC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007DD0B1  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
007DD0B6  F3 0F 7F 45 30                  movdqu xmmword ptr [rbp + 0x30], xmm0
007DD0BB  E8 30 CD 09 00                  call 0x140879df0
007DD0C0  8B D8                           mov ebx, eax
007DD0C2  85 C0                           test eax, eax
007DD0C4  0F 88 43 0A 00 00               js 0x1407ddb0d
007DD0CA  33 C9                           xor ecx, ecx
007DD0CC  E8 13 7A 1D 00                  call 0x1409b4ae4
007DD0D1  49 8B CE                        mov rcx, r14
007DD0D4  40 B6 01                        mov sil, 1
007DD0D7  E8 40 C9 3E 00                  call 0x140bc9a1c
007DD0DC  41 8B 5E 28                     mov ebx, dword ptr [r14 + 0x28]
007DD0E0  33 C0                           xor eax, eax
007DD0E2  44 8A FE                        mov r15b, sil
007DD0E5  89 5D 88                        mov dword ptr [rbp - 0x78], ebx
007DD0E8  66 41 39 46 42                  cmp word ptr [r14 + 0x42], ax
007DD0ED  74 12                           je 0x1407dd101
007DD0EF  8D 48 11                        lea ecx, [rax + 0x11]
007DD0F2  E8 49 19 1D 00                  call 0x1409aea40
007DD0F7  BB 02 00 00 C0                  mov ebx, 0xc0000002
007DD0FC  E9 FA 09 00 00                  jmp 0x1407ddafb
007DD101  33 D2                           xor edx, edx
007DD103  49 8B CC                        mov rcx, r12
007DD106  E8 75 C3 3E 00                  call 0x140bc9480
007DD10B  84 C0                           test al, al
007DD10D  74 0A                           je 0x1407dd119
007DD10F  BB 21 01 00 C0                  mov ebx, 0xc0000121
007DD114  E9 E2 09 00 00                  jmp 0x1407ddafb
007DD119  41 38 76 41                     cmp byte ptr [r14 + 0x41], sil
007DD11D  75 0A                           jne 0x1407dd129
007DD11F  BB 22 00 00 C0                  mov ebx, 0xc0000022
007DD124  E9 D2 09 00 00                  jmp 0x1407ddafb
007DD129  48 3B 3D 60 C9 7F 00            cmp rdi, qword ptr [rip + 0x7fc960]
007DD130  74 ED                           je 0x1407dd11f
007DD132  40 38 B7 80 0B 00 00            cmp byte ptr [rdi + 0xb80], sil
007DD139  75 0A                           jne 0x1407dd145
007DD13B  BB 89 01 00 C0                  mov ebx, 0xc0000189
007DD140  E9 B6 09 00 00                  jmp 0x1407ddafb
007DD145  48 8B CF                        mov rcx, rdi
007DD148  E8 0F 28 07 00                  call 0x14084f95c
007DD14D  4C 8D 45 80                     lea r8, [rbp - 0x80]
007DD151  40 88 74 24 75                  mov byte ptr [rsp + 0x75], sil
007DD156  8B D3                           mov edx, ebx
007DD158  48 8B CF                        mov rcx, rdi
007DD15B  40 84 B7 8C 00 00 00            test byte ptr [rdi + 0x8c], sil
007DD162  74 07                           je 0x1407dd16b
007DD164  E8 F7 7A 07 00                  call 0x140854c60
007DD169  EB 05                           jmp 0x1407dd170
007DD16B  E8 40 7B 07 00                  call 0x140854cb0
007DD170  4C 8B E8                        mov r13, rax
007DD173  48 85 C0                        test rax, rax
007DD176  75 0A                           jne 0x1407dd182
007DD178  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007DD17D  E9 6C 09 00 00                  jmp 0x1407ddaee
007DD182  41 F6 45 02 04                  test byte ptr [r13 + 2], 4
007DD187  74 05                           je 0x1407dd18e
007DD189  83 C8 FF                        or eax, 0xffffffff
007DD18C  EB 04                           jmp 0x1407dd192
007DD18E  41 8B 45 10                     mov eax, dword ptr [r13 + 0x10]
007DD192  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
007DD196  4C 8D 4C 24 70                  lea r9, [rsp + 0x70]
007DD19B  4C 89 4C 24 38                  mov qword ptr [rsp + 0x38], r9
007DD1A0  44 8B C3                        mov r8d, ebx
007DD1A3  41 C1 E8 1F                     shr r8d, 0x1f
007DD1A7  44 8B C8                        mov r9d, eax
007DD1AA  44 89 44 24 30                  mov dword ptr [rsp + 0x30], r8d
007DD1AF  48 8B 51 40                     mov rdx, qword ptr [rcx + 0x40]
007DD1B3  44 89 45 A8                     mov dword ptr [rbp - 0x58], r8d
007DD1B7  4C 8B C7                        mov r8, rdi
007DD1BA  89 45 E4                        mov dword ptr [rbp - 0x1c], eax
007DD1BD  C7 44 24 20 06 00 00 00         mov dword ptr [rsp + 0x20], 6
007DD1C5  8B 52 24                        mov edx, dword ptr [rdx + 0x24]
007DD1C8  E8 27 DE 07 00                  call 0x14085aff4
007DD1CD  8B D8                           mov ebx, eax
007DD1CF  85 C0                           test eax, eax
007DD1D1  0F 88 17 09 00 00               js 0x1407ddaee
007DD1D7  45 0F B7 45 48                  movzx r8d, word ptr [r13 + 0x48]
007DD1DC  48 8D 45 A0                     lea rax, [rbp - 0x60]
007DD1E0  8B 54 24 70                     mov edx, dword ptr [rsp + 0x70]
007DD1E4  41 83 C0 4C                     add r8d, 0x4c
007DD1E8  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007DD1ED  44 8A CE                        mov r9b, sil
007DD1F0  48 8D 45 C8                     lea rax, [rbp - 0x38]
007DD1F4  48 8B CF                        mov rcx, rdi
007DD1F7  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007DD1FC  48 8D 45 E0                     lea rax, [rbp - 0x20]
007DD200  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007DD205  E8 C6 E3 07 00                  call 0x14085b5d0
007DD20A  8B D8                           mov ebx, eax
007DD20C  85 C0                           test eax, eax
007DD20E  0F 88 A6 08 00 00               js 0x1407ddaba
007DD214  48 8B 5D C8                     mov rbx, qword ptr [rbp - 0x38]
007DD218  49 8D 55 4C                     lea rdx, [r13 + 0x4c]
007DD21C  44 8B 7D E0                     mov r15d, dword ptr [rbp - 0x20]
007DD220  45 0F B7 45 48                  movzx r8d, word ptr [r13 + 0x48]
007DD225  44 89 7C 24 70                  mov dword ptr [rsp + 0x70], r15d
007DD22A  48 8D 4B 4C                     lea rcx, [rbx + 0x4c]
007DD22E  48 89 5D C0                     mov qword ptr [rbp - 0x40], rbx
007DD232  E8 09 96 EE FF                  call 0x1406c6840
007DD237  41 0F B7 45 48                  movzx eax, word ptr [r13 + 0x48]
007DD23C  66 89 43 48                     mov word ptr [rbx + 0x48], ax
007DD240  41 F6 45 02 20                  test byte ptr [r13 + 2], 0x20
007DD245  74 07                           je 0x1407dd24e
007DD247  66 83 4B 02 20                  or word ptr [rbx + 2], 0x20
007DD24C  EB 09                           jmp 0x1407dd257
007DD24E  B8 DF FF 00 00                  mov eax, 0xffdf
007DD253  66 21 43 02                     and word ptr [rbx + 2], ax
007DD257  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
007DD25B  45 8B CF                        mov r9d, r15d
007DD25E  4C 8B C7                        mov r8, rdi
007DD261  48 8B 41 40                     mov rax, qword ptr [rcx + 0x40]
007DD265  8B 50 24                        mov edx, dword ptr [rax + 0x24]
007DD268  33 C0                           xor eax, eax
007DD26A  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
007DD26E  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
007DD276  E8 25 4F 01 00                  call 0x1407f21a0
007DD27B  8B D8                           mov ebx, eax
007DD27D  85 C0                           test eax, eax
007DD27F  0F 88 3D 08 00 00               js 0x1407ddac2
007DD285  48 8B CF                        mov rcx, rdi
007DD288  E8 AB B4 06 00                  call 0x140848738
007DD28D  33 DB                           xor ebx, ebx
007DD28F  49 8B CE                        mov rcx, r14
007DD292  88 5C 24 75                     mov byte ptr [rsp + 0x75], bl
007DD296  E8 25 C0 3E 00                  call 0x140bc92c0
007DD29B  E8 E4 C7 3E 00                  call 0x140bc9a84
007DD2A0  48 8D 55 80                     lea rdx, [rbp - 0x80]
007DD2A4  48 8B CF                        mov rcx, rdi
007DD2A7  40 84 B7 8C 00 00 00            test byte ptr [rdi + 0x8c], sil
007DD2AE  74 07                           je 0x1407dd2b7
007DD2B0  E8 6B F9 07 00                  call 0x14085cc20
007DD2B5  EB 05                           jmp 0x1407dd2bc
007DD2B7  E8 84 8C 07 00                  call 0x140855f40
007DD2BC  48 8D 55 A0                     lea rdx, [rbp - 0x60]
007DD2C0  4C 8B EB                        mov r13, rbx
007DD2C3  48 8B CF                        mov rcx, rdi
007DD2C6  48 89 5D C8                     mov qword ptr [rbp - 0x38], rbx
007DD2CA  40 84 B7 8C 00 00 00            test byte ptr [rdi + 0x8c], sil
007DD2D1  74 07                           je 0x1407dd2da
007DD2D3  E8 48 F9 07 00                  call 0x14085cc20
007DD2D8  EB 05                           jmp 0x1407dd2df
007DD2DA  E8 61 8C 07 00                  call 0x140855f40
007DD2DF  48 89 5D C0                     mov qword ptr [rbp - 0x40], rbx
007DD2E3  40 8A CE                        mov cl, sil
007DD2E6  E8 F9 77 1D 00                  call 0x1409b4ae4
007DD2EB  8B 75 88                        mov esi, dword ptr [rbp - 0x78]
007DD2EE  E8 2D C9 3E 00                  call 0x140bc9c20
007DD2F3  84 C0                           test al, al
007DD2F5  0F 85 A1 07 00 00               jne 0x1407dda9c
007DD2FB  33 D2                           xor edx, edx
007DD2FD  49 8B CC                        mov rcx, r12
007DD300  E8 7B C1 3E 00                  call 0x140bc9480
007DD305  84 C0                           test al, al
007DD307  0F 85 59 02 00 00               jne 0x1407dd566
007DD30D  41 3B 76 28                     cmp esi, dword ptr [r14 + 0x28]
007DD311  0F 85 99 07 00 00               jne 0x1407ddab0
007DD317  41 F7 46 08 00 00 04 00         test dword ptr [r14 + 8], 0x40000
007DD31F  0F 85 81 07 00 00               jne 0x1407ddaa6
007DD325  80 BF 80 0B 00 00 01            cmp byte ptr [rdi + 0xb80], 1
007DD32C  0F 84 6A 07 00 00               je 0x1407dda9c
007DD332  8B 45 E4                        mov eax, dword ptr [rbp - 0x1c]
007DD335  83 F8 FF                        cmp eax, -1
007DD338  74 24                           je 0x1407dd35e
007DD33A  44 8A 44 24 74                  mov r8b, byte ptr [rsp + 0x74]
007DD33F  41 B9 04 00 00 00               mov r9d, 4
007DD345  8B D0                           mov edx, eax
007DD347  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
007DD34C  48 8B CF                        mov rcx, rdi
007DD34F  E8 28 0B 29 00                  call 0x140a6de7c
007DD354  8B D8                           mov ebx, eax
007DD356  85 C0                           test eax, eax
007DD358  0F 88 65 01 00 00               js 0x1407dd4c3
007DD35E  44 8A 44 24 74                  mov r8b, byte ptr [rsp + 0x74]
007DD363  41 B9 00 00 01 00               mov r9d, 0x10000
007DD369  8B D6                           mov edx, esi
007DD36B  C6 44 24 20 01                  mov byte ptr [rsp + 0x20], 1
007DD370  48 8B CF                        mov rcx, rdi
007DD373  E8 04 0B 29 00                  call 0x140a6de7c
007DD378  8B D8                           mov ebx, eax
007DD37A  85 C0                           test eax, eax
007DD37C  0F 88 41 01 00 00               js 0x1407dd4c3
007DD382  4C 8D 4D D0                     lea r9, [rbp - 0x30]
007DD386  B2 01                           mov dl, 1
007DD388  49 8B CE                        mov rcx, r14
007DD38B  E8 DC 31 1D 00                  call 0x1409b056c
007DD390  8B D8                           mov ebx, eax
007DD392  3D 2D 02 00 C0                  cmp eax, 0xc000022d
007DD397  75 54                           jne 0x1407dd3ed
007DD399  8B 45 D0                        mov eax, dword ptr [rbp - 0x30]
007DD39C  33 D2                           xor edx, edx
007DD39E  49 8B CE                        mov rcx, r14
007DD3A1  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007DD3A5  44 8D 42 07                     lea r8d, [rdx + 7]
007DD3A9  E8 C2 19 1D 00                  call 0x1409aed70
007DD3AE  E8 D1 C6 3E 00                  call 0x140bc9a84
007DD3B3  33 D2                           xor edx, edx
007DD3B5  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007DD3B9  E8 C2 16 2E 00                  call 0x140abea80
007DD3BE  8B D8                           mov ebx, eax
007DD3C0  85 C0                           test eax, eax
007DD3C2  0F 88 F4 00 00 00               js 0x1407dd4bc
007DD3C8  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007DD3CC  E8 7B 2D 1D 00                  call 0x1409b014c
007DD3D1  0F 57 C0                        xorps xmm0, xmm0
007DD3D4  48 8D 4D 98                     lea rcx, [rbp - 0x68]
007DD3D8  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
007DD3DC  E8 93 E0 16 00                  call 0x14094b474
007DD3E1  B1 01                           mov cl, 1
007DD3E3  E8 FC 76 1D 00                  call 0x1409b4ae4
007DD3E8  E9 01 FF FF FF                  jmp 0x1407dd2ee
007DD3ED  85 DB                           test ebx, ebx
007DD3EF  0F 88 CE 00 00 00               js 0x1407dd4c3
007DD3F5  44 8A 44 24 74                  mov r8b, byte ptr [rsp + 0x74]
007DD3FA  41 B9 00 00 01 00               mov r9d, 0x10000
007DD400  8B D6                           mov edx, esi
007DD402  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
007DD40A  48 8B CF                        mov rcx, rdi
007DD40D  E8 BE C8 3E 00                  call 0x140bc9cd0
007DD412  8B D8                           mov ebx, eax
007DD414  85 C0                           test eax, eax
007DD416  0F 88 A7 00 00 00               js 0x1407dd4c3
007DD41C  F6 45 E8 08                     test byte ptr [rbp - 0x18], 8
007DD420  0F 84 ED 00 00 00               je 0x1407dd513
007DD426  4C 8D 45 D0                     lea r8, [rbp - 0x30]
007DD42A  33 D2                           xor edx, edx
007DD42C  49 8B CE                        mov rcx, r14
007DD42F  E8 18 43 01 00                  call 0x1407f174c
007DD434  B9 00 00 00 80                  mov ecx, 0x80000000
007DD439  8B F0                           mov esi, eax
007DD43B  8B D8                           mov ebx, eax
007DD43D  03 C1                           add eax, ecx
007DD43F  85 C1                           test ecx, eax
007DD441  75 08                           jne 0x1407dd44b
007DD443  81 FB 2D 02 00 C0               cmp ebx, 0xc000022d
007DD449  75 78                           jne 0x1407dd4c3
007DD44B  4C 8D 45 D0                     lea r8, [rbp - 0x30]
007DD44F  33 D2                           xor edx, edx
007DD451  49 8B CE                        mov rcx, r14
007DD454  E8 57 2D 1D 00                  call 0x1409b01b0
007DD459  B9 2D 02 00 C0                  mov ecx, 0xc000022d
007DD45E  8B D8                           mov ebx, eax
007DD460  3B C1                           cmp eax, ecx
007DD462  74 08                           je 0x1407dd46c
007DD464  85 C0                           test eax, eax
007DD466  78 5B                           js 0x1407dd4c3
007DD468  3B F1                           cmp esi, ecx
007DD46A  75 5F                           jne 0x1407dd4cb
007DD46C  8B 45 D0                        mov eax, dword ptr [rbp - 0x30]
007DD46F  33 D2                           xor edx, edx
007DD471  49 8B CE                        mov rcx, r14
007DD474  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007DD478  44 8D 42 07                     lea r8d, [rdx + 7]
007DD47C  E8 EF 18 1D 00                  call 0x1409aed70
007DD481  E8 FE C5 3E 00                  call 0x140bc9a84
007DD486  33 C0                           xor eax, eax
007DD488  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007DD48C  33 D2                           xor edx, edx
007DD48E  40 8A F0                        mov sil, al
007DD491  E8 EA 15 2E 00                  call 0x140abea80
007DD496  8B D8                           mov ebx, eax
007DD498  85 C0                           test eax, eax
007DD49A  78 6B                           js 0x1407dd507
007DD49C  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007DD4A0  E8 A7 2C 1D 00                  call 0x1409b014c
007DD4A5  0F 57 C0                        xorps xmm0, xmm0
007DD4A8  48 8D 4D 98                     lea rcx, [rbp - 0x68]
007DD4AC  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
007DD4B0  E8 BF DF 16 00                  call 0x14094b474
007DD4B5  B1 01                           mov cl, 1
007DD4B7  E9 2A FE FF FF                  jmp 0x1407dd2e6
007DD4BC  B1 01                           mov cl, 1
007DD4BE  E8 21 76 1D 00                  call 0x1409b4ae4
007DD4C3  40 B6 01                        mov sil, 1
007DD4C6  E9 F7 05 00 00                  jmp 0x1407ddac2
007DD4CB  45 33 C0                        xor r8d, r8d
007DD4CE  4C 8D 4D F8                     lea r9, [rbp - 8]
007DD4D2  49 8B CE                        mov rcx, r14
007DD4D5  41 8D 50 01                     lea edx, [r8 + 1]
007DD4D9  E8 82 40 01 00                  call 0x1407f1560
007DD4DE  45 33 E4                        xor r12d, r12d
007DD4E1  4C 8D 4D F8                     lea r9, [rbp - 8]
007DD4E5  45 33 C0                        xor r8d, r8d
007DD4E8  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
007DD4ED  49 8B CE                        mov rcx, r14
007DD4F0  41 8D 54 24 01                  lea edx, [r12 + 1]
007DD4F5  E8 C6 D9 00 00                  call 0x1407eaec0
007DD4FA  33 D2                           xor edx, edx
007DD4FC  48 8D 4D F8                     lea rcx, [rbp - 8]
007DD500  E8 9B E4 C3 FF                  call 0x14041b9a0
007DD505  EB 6F                           jmp 0x1407dd576
007DD507  B1 01                           mov cl, 1
007DD509  E8 D6 75 1D 00                  call 0x1409b4ae4
007DD50E  E9 AF 05 00 00                  jmp 0x1407ddac2
007DD513  0F 57 C0                        xorps xmm0, xmm0
007DD516  48 8D 4D 18                     lea rcx, [rbp + 0x18]
007DD51A  0F 11 45 18                     movups xmmword ptr [rbp + 0x18], xmm0
007DD51E  E8 CD D2 C4 FF                  call 0x14042a7f0
007DD523  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
007DD528  4C 8D 4D 18                     lea r9, [rbp + 0x18]
007DD52C  45 33 E4                        xor r12d, r12d
007DD52F  C6 44 24 28 01                  mov byte ptr [rsp + 0x28], 1
007DD534  4C 8D 05 15 3F 01 00            lea r8, [rip + 0x13f15]
007DD53B  4C 89 64 24 20                  mov qword ptr [rsp + 0x20], r12
007DD540  48 8D 15 89 E5 F2 FF            lea rdx, [rip - 0xd1a77]
007DD547  49 8B CE                        mov rcx, r14
007DD54A  E8 E5 7C 27 00                  call 0x140a55234
007DD54F  33 D2                           xor edx, edx
007DD551  48 8D 4D 18                     lea rcx, [rbp + 0x18]
007DD555  E8 46 E4 C3 FF                  call 0x14041b9a0
007DD55A  49 8B CE                        mov rcx, r14
007DD55D  E8 12 2D 1D 00                  call 0x1409b0274
007DD562  84 C0                           test al, al
007DD564  74 0A                           je 0x1407dd570
007DD566  BB 21 01 00 C0                  mov ebx, 0xc0000121
007DD56B  E9 53 FF FF FF                  jmp 0x1407dd4c3
007DD570  49 83 3E 01                     cmp qword ptr [r14], 1
007DD574  75 F0                           jne 0x1407dd566
007DD576  45 33 C9                        xor r9d, r9d
007DD579  45 33 C0                        xor r8d, r8d
007DD57C  41 8B D7                        mov edx, r15d
007DD57F  48 8B CF                        mov rcx, rdi
007DD582  E8 F9 AA 07 00                  call 0x140858080
007DD587  8B D8                           mov ebx, eax
007DD589  40 B6 01                        mov sil, 1
007DD58C  85 C0                           test eax, eax
007DD58E  0F 88 2E 05 00 00               js 0x1407ddac2
007DD594  4C 8D 45 A0                     lea r8, [rbp - 0x60]
007DD598  8B 55 88                        mov edx, dword ptr [rbp - 0x78]
007DD59B  48 8B CF                        mov rcx, rdi
007DD59E  40 84 B7 8C 00 00 00            test byte ptr [rdi + 0x8c], sil
007DD5A5  74 07                           je 0x1407dd5ae
007DD5A7  E8 B4 76 07 00                  call 0x140854c60
007DD5AC  EB 05                           jmp 0x1407dd5b3
007DD5AE  E8 FD 76 07 00                  call 0x140854cb0
007DD5B3  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
007DD5B7  48 85 C0                        test rax, rax
007DD5BA  75 0A                           jne 0x1407dd5c6
007DD5BC  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007DD5C1  E9 FC 04 00 00                  jmp 0x1407ddac2
007DD5C6  F6 40 02 04                     test byte ptr [rax + 2], 4
007DD5CA  44 8B 78 10                     mov r15d, dword ptr [rax + 0x10]
007DD5CE  41 8B D7                        mov edx, r15d
007DD5D1  0F 84 B2 00 00 00               je 0x1407dd689
007DD5D7  48 8B 0D B2 C4 7F 00            mov rcx, qword ptr [rip + 0x7fc4b2]
007DD5DE  4C 8D 45 90                     lea r8, [rbp - 0x70]
007DD5E2  40 84 B1 8C 00 00 00            test byte ptr [rcx + 0x8c], sil
007DD5E9  74 07                           je 0x1407dd5f2
007DD5EB  E8 70 76 07 00                  call 0x140854c60
007DD5F0  EB 05                           jmp 0x1407dd5f7
007DD5F2  E8 B9 76 07 00                  call 0x140854cb0
007DD5F7  44 8B 64 24 70                  mov r12d, dword ptr [rsp + 0x70]
007DD5FC  48 85 C0                        test rax, rax
007DD5FF  75 0A                           jne 0x1407dd60b
007DD601  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007DD606  E9 BC 04 00 00                  jmp 0x1407ddac7
007DD60B  44 89 60 1C                     mov dword ptr [rax + 0x1c], r12d
007DD60F  48 8D 55 90                     lea rdx, [rbp - 0x70]
007DD613  48 8B 0D 76 C4 7F 00            mov rcx, qword ptr [rip + 0x7fc476]
007DD61A  40 84 B1 8C 00 00 00            test byte ptr [rcx + 0x8c], sil
007DD621  74 07                           je 0x1407dd62a
007DD623  E8 F8 F5 07 00                  call 0x14085cc20
007DD628  EB 05                           jmp 0x1407dd62f
007DD62A  E8 11 89 07 00                  call 0x140855f40
007DD62F  4C 8D 45 80                     lea r8, [rbp - 0x80]
007DD633  41 8B D4                        mov edx, r12d
007DD636  48 8B CF                        mov rcx, rdi
007DD639  40 84 B7 8C 00 00 00            test byte ptr [rdi + 0x8c], sil
007DD640  74 07                           je 0x1407dd649
007DD642  E8 19 76 07 00                  call 0x140854c60
007DD647  EB 05                           jmp 0x1407dd64e
007DD649  E8 62 76 07 00                  call 0x140854cb0
007DD64E  4C 8B E8                        mov r13, rax
007DD651  48 85 C0                        test rax, rax
007DD654  74 AB                           je 0x1407dd601
007DD656  44 89 78 10                     mov dword ptr [rax + 0x10], r15d
007DD65A  48 8D 55 80                     lea rdx, [rbp - 0x80]
007DD65E  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
007DD662  48 8B CF                        mov rcx, rdi
007DD665  44 89 60 24                     mov dword ptr [rax + 0x24], r12d
007DD669  40 84 B7 8C 00 00 00            test byte ptr [rdi + 0x8c], sil
007DD670  74 07                           je 0x1407dd679
007DD672  E8 A9 F5 07 00                  call 0x14085cc20
007DD677  EB 05                           jmp 0x1407dd67e
007DD679  E8 C2 88 07 00                  call 0x140855f40
007DD67E  45 33 FF                        xor r15d, r15d
007DD681  45 8B EF                        mov r13d, r15d
007DD684  E9 7F 02 00 00                  jmp 0x1407dd908
007DD689  45 33 C9                        xor r9d, r9d
007DD68C  45 33 C0                        xor r8d, r8d
007DD68F  48 8B CF                        mov rcx, rdi
007DD692  E8 E9 A9 07 00                  call 0x140858080
007DD697  8B D8                           mov ebx, eax
007DD699  85 C0                           test eax, eax
007DD69B  0F 88 21 04 00 00               js 0x1407ddac2
007DD6A1  4C 8D 45 90                     lea r8, [rbp - 0x70]
007DD6A5  41 8B D7                        mov edx, r15d
007DD6A8  48 8B CF                        mov rcx, rdi
007DD6AB  40 84 B7 8C 00 00 00            test byte ptr [rdi + 0x8c], sil
007DD6B2  74 07                           je 0x1407dd6bb
007DD6B4  E8 A7 75 07 00                  call 0x140854c60
007DD6B9  EB 05                           jmp 0x1407dd6c0
007DD6BB  E8 F0 75 07 00                  call 0x140854cb0
007DD6C0  48 8B C8                        mov rcx, rax
007DD6C3  48 85 C0                        test rax, rax
007DD6C6  0F 84 F0 FE FF FF               je 0x1407dd5bc
007DD6CC  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007DD6D3  48 8D 55 90                     lea rdx, [rbp - 0x70]
007DD6D7  8B 45 A8                        mov eax, dword ptr [rbp - 0x58]
007DD6DA  8B 74 81 1C                     mov esi, dword ptr [rcx + rax*4 + 0x1c]
007DD6DE  48 8B CF                        mov rcx, rdi
007DD6E1  89 75 A8                        mov dword ptr [rbp - 0x58], esi
007DD6E4  74 07                           je 0x1407dd6ed
007DD6E6  E8 35 F5 07 00                  call 0x14085cc20
007DD6EB  EB 05                           jmp 0x1407dd6f2
007DD6ED  E8 4E 88 07 00                  call 0x140855f40
007DD6F2  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007DD6F9  4C 8D 45 B8                     lea r8, [rbp - 0x48]
007DD6FD  8B D6                           mov edx, esi
007DD6FF  48 8B CF                        mov rcx, rdi
007DD702  74 07                           je 0x1407dd70b
007DD704  E8 57 75 07 00                  call 0x140854c60
007DD709  EB 05                           jmp 0x1407dd710
007DD70B  E8 A0 75 07 00                  call 0x140854cb0
007DD710  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
007DD714  48 8B C8                        mov rcx, rax
007DD717  48 85 C0                        test rax, rax
007DD71A  75 0A                           jne 0x1407dd726
007DD71C  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007DD721  E9 9D FD FF FF                  jmp 0x1407dd4c3
007DD726  B8 72 69 00 00                  mov eax, 0x6972
007DD72B  66 39 01                        cmp word ptr [rcx], ax
007DD72E  75 0A                           jne 0x1407dd73a
007DD730  0F B7 41 02                     movzx eax, word ptr [rcx + 2]
007DD734  4C 8D 69 04                     lea r13, [rcx + 4]
007DD738  EB 09                           jmp 0x1407dd743
007DD73A  B8 01 00 00 00                  mov eax, 1
007DD73F  4C 8D 6D A8                     lea r13, [rbp - 0x58]
007DD743  89 45 98                        mov dword ptr [rbp - 0x68], eax
007DD746  44 3B E0                        cmp r12d, eax
007DD749  0F 83 29 01 00 00               jae 0x1407dd878
007DD74F  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007DD756  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
007DD75B  41 8B DC                        mov ebx, r12d
007DD75E  48 8B CF                        mov rcx, rdi
007DD761  41 8B 54 9D 00                  mov edx, dword ptr [r13 + rbx*4]
007DD766  74 07                           je 0x1407dd76f
007DD768  E8 F3 74 07 00                  call 0x140854c60
007DD76D  EB 05                           jmp 0x1407dd774
007DD76F  E8 3C 75 07 00                  call 0x140854cb0
007DD774  48 8B F0                        mov rsi, rax
007DD777  33 C0                           xor eax, eax
007DD779  48 85 F6                        test rsi, rsi
007DD77C  0F 84 E6 00 00 00               je 0x1407dd868
007DD782  41 8B 54 9D 00                  mov edx, dword ptr [r13 + rbx*4]
007DD787  45 33 C9                        xor r9d, r9d
007DD78A  45 33 C0                        xor r8d, r8d
007DD78D  48 8B CF                        mov rcx, rdi
007DD790  E8 EB A8 07 00                  call 0x140858080
007DD795  33 D2                           xor edx, edx
007DD797  8B D8                           mov ebx, eax
007DD799  85 C0                           test eax, eax
007DD79B  0F 88 9E 00 00 00               js 0x1407dd83f
007DD7A1  0F B7 06                        movzx eax, word ptr [rsi]
007DD7A4  B9 6C 66 00 00                  mov ecx, 0x666c
007DD7A9  44 8B 45 88                     mov r8d, dword ptr [rbp - 0x78]
007DD7AD  66 2B C1                        sub ax, cx
007DD7B0  B9 FF FD 00 00                  mov ecx, 0xfdff
007DD7B5  66 85 C1                        test cx, ax
007DD7B8  8B C2                           mov eax, edx
007DD7BA  0F B7 56 02                     movzx edx, word ptr [rsi + 2]
007DD7BE  74 11                           je 0x1407dd7d1
007DD7C0  3B C2                           cmp eax, edx
007DD7C2  73 1E                           jae 0x1407dd7e2
007DD7C4  8B C8                           mov ecx, eax
007DD7C6  44 39 44 8E 04                  cmp dword ptr [rsi + rcx*4 + 4], r8d
007DD7CB  74 3D                           je 0x1407dd80a
007DD7CD  FF C0                           inc eax
007DD7CF  EB EF                           jmp 0x1407dd7c0
007DD7D1  3B C2                           cmp eax, edx
007DD7D3  73 0D                           jae 0x1407dd7e2
007DD7D5  8B C8                           mov ecx, eax
007DD7D7  44 39 44 CE 04                  cmp dword ptr [rsi + rcx*8 + 4], r8d
007DD7DC  74 3F                           je 0x1407dd81d
007DD7DE  FF C0                           inc eax
007DD7E0  EB EF                           jmp 0x1407dd7d1
007DD7E2  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007DD7E9  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
007DD7EE  48 8B CF                        mov rcx, rdi
007DD7F1  74 07                           je 0x1407dd7fa
007DD7F3  E8 28 F4 07 00                  call 0x14085cc20
007DD7F8  EB 05                           jmp 0x1407dd7ff
007DD7FA  E8 41 87 07 00                  call 0x140855f40
007DD7FF  8B 45 98                        mov eax, dword ptr [rbp - 0x68]
007DD802  41 FF C4                        inc r12d
007DD805  E9 3C FF FF FF                  jmp 0x1407dd746
007DD80A  44 8B 64 24 70                  mov r12d, dword ptr [rsp + 0x70]
007DD80F  44 89 64 8E 04                  mov dword ptr [rsi + rcx*4 + 4], r12d
007DD814  EB 11                           jmp 0x1407dd827
007DD816  E8 25 87 07 00                  call 0x140855f40
007DD81B  EB 60                           jmp 0x1407dd87d
007DD81D  44 8B 64 24 70                  mov r12d, dword ptr [rsp + 0x70]
007DD822  44 89 64 CE 04                  mov dword ptr [rsi + rcx*8 + 4], r12d
007DD827  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007DD82E  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
007DD833  48 8B CF                        mov rcx, rdi
007DD836  74 DE                           je 0x1407dd816
007DD838  E8 E3 F3 07 00                  call 0x14085cc20
007DD83D  EB 3E                           jmp 0x1407dd87d
007DD83F  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007DD846  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
007DD84B  48 8B CF                        mov rcx, rdi
007DD84E  74 07                           je 0x1407dd857
007DD850  E8 CB F3 07 00                  call 0x14085cc20
007DD855  EB 05                           jmp 0x1407dd85c
007DD857  E8 E4 86 07 00                  call 0x140855f40
007DD85C  4C 8B 6D C8                     mov r13, qword ptr [rbp - 0x38]
007DD860  40 B6 01                        mov sil, 1
007DD863  E9 5A 02 00 00                  jmp 0x1407ddac2
007DD868  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007DD86D  40 B6 01                        mov sil, 1
007DD870  4C 8B E8                        mov r13, rax
007DD873  E9 4A 02 00 00                  jmp 0x1407ddac2
007DD878  44 8B 64 24 70                  mov r12d, dword ptr [rsp + 0x70]
007DD87D  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007DD884  4C 8D 45 90                     lea r8, [rbp - 0x70]
007DD888  41 8B D7                        mov edx, r15d
007DD88B  48 8B CF                        mov rcx, rdi
007DD88E  74 07                           je 0x1407dd897
007DD890  E8 CB 73 07 00                  call 0x140854c60
007DD895  EB 05                           jmp 0x1407dd89c
007DD897  E8 14 74 07 00                  call 0x140854cb0
007DD89C  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007DD8A3  4C 8D 45 80                     lea r8, [rbp - 0x80]
007DD8A7  48 8B F0                        mov rsi, rax
007DD8AA  41 8B D4                        mov edx, r12d
007DD8AD  48 8B CF                        mov rcx, rdi
007DD8B0  74 07                           je 0x1407dd8b9
007DD8B2  E8 A9 73 07 00                  call 0x140854c60
007DD8B7  EB 05                           jmp 0x1407dd8be
007DD8B9  E8 F2 73 07 00                  call 0x140854cb0
007DD8BE  0F B7 40 4A                     movzx eax, word ptr [rax + 0x4a]
007DD8C2  39 46 38                        cmp dword ptr [rsi + 0x38], eax
007DD8C5  73 03                           jae 0x1407dd8ca
007DD8C7  89 46 38                        mov dword ptr [rsi + 0x38], eax
007DD8CA  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007DD8D1  48 8D 55 80                     lea rdx, [rbp - 0x80]
007DD8D5  48 8B CF                        mov rcx, rdi
007DD8D8  74 07                           je 0x1407dd8e1
007DD8DA  E8 41 F3 07 00                  call 0x14085cc20
007DD8DF  EB 05                           jmp 0x1407dd8e6
007DD8E1  E8 5A 86 07 00                  call 0x140855f40
007DD8E6  45 33 FF                        xor r15d, r15d
007DD8E9  48 8D 55 90                     lea rdx, [rbp - 0x70]
007DD8ED  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007DD8F4  45 8B EF                        mov r13d, r15d
007DD8F7  48 8B CF                        mov rcx, rdi
007DD8FA  74 07                           je 0x1407dd903
007DD8FC  E8 1F F3 07 00                  call 0x14085cc20
007DD901  EB 05                           jmp 0x1407dd908
007DD903  E8 38 86 07 00                  call 0x140855f40
007DD908  48 8D 55 F8                     lea rdx, [rbp - 8]
007DD90C  45 89 66 28                     mov dword ptr [r14 + 0x28], r12d
007DD910  49 8B CE                        mov rcx, r14
007DD913  E8 54 06 07 00                  call 0x14084df6c
007DD918  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
007DD91C  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
007DD921  83 4C 24 78 FF                  or dword ptr [rsp + 0x78], 0xffffffff
007DD926  83 64 24 7C 00                  and dword ptr [rsp + 0x7c], 0
007DD92B  41 8B 56 28                     mov edx, dword ptr [r14 + 0x28]
007DD92F  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
007DD936  74 07                           je 0x1407dd93f
007DD938  E8 23 73 07 00                  call 0x140854c60
007DD93D  EB 05                           jmp 0x1407dd944
007DD93F  E8 6C 73 07 00                  call 0x140854cb0
007DD944  48 8B F0                        mov rsi, rax
007DD947  48 85 C0                        test rax, rax
007DD94A  75 0D                           jne 0x1407dd959
007DD94C  BB 9A 00 00 C0                  mov ebx, 0xc000009a
007DD951  40 B6 01                        mov sil, 1
007DD954  E9 6E 01 00 00                  jmp 0x1407ddac7
007DD959  8B 4E 28                        mov ecx, dword ptr [rsi + 0x28]
007DD95C  45 33 C9                        xor r9d, r9d
007DD95F  8B 46 24                        mov eax, dword ptr [rsi + 0x24]
007DD962  45 33 C0                        xor r8d, r8d
007DD965  41 89 4E 64                     mov dword ptr [r14 + 0x64], ecx
007DD969  49 8B CE                        mov rcx, r14
007DD96C  41 89 46 60                     mov dword ptr [r14 + 0x60], eax
007DD970  0F B7 46 02                     movzx eax, word ptr [rsi + 2]
007DD974  66 41 89 86 BA 00 00 00         mov word ptr [r14 + 0xba], ax
007DD97C  8B 56 2C                        mov edx, dword ptr [rsi + 0x2c]
007DD97F  44 88 7C 24 20                  mov byte ptr [rsp + 0x20], r15b
007DD984  E8 97 CD 1F 00                  call 0x1409da720
007DD989  B2 01                           mov dl, 1
007DD98B  49 8B CE                        mov rcx, r14
007DD98E  E8 61 ED 06 00                  call 0x14084c6f4
007DD993  49 FF 86 30 01 00 00            inc qword ptr [r14 + 0x130]
007DD99A  48 8D 54 24 78                  lea rdx, [rsp + 0x78]
007DD99F  48 8B 46 04                     mov rax, qword ptr [rsi + 4]
007DD9A3  49 89 86 A8 00 00 00            mov qword ptr [r14 + 0xa8], rax
007DD9AA  0F B7 46 34                     movzx eax, word ptr [rsi + 0x34]
007DD9AE  66 41 89 86 B0 00 00 00         mov word ptr [r14 + 0xb0], ax
007DD9B6  0F B7 46 3C                     movzx eax, word ptr [rsi + 0x3c]
007DD9BA  66 41 89 86 B2 00 00 00         mov word ptr [r14 + 0xb2], ax
007DD9C2  8B 46 40                        mov eax, dword ptr [rsi + 0x40]
007DD9C5  41 89 86 B4 00 00 00            mov dword ptr [r14 + 0xb4], eax
007DD9CC  41 8B 86 B8 00 00 00            mov eax, dword ptr [r14 + 0xb8]
007DD9D3  0F B7 4E 36                     movzx ecx, word ptr [rsi + 0x36]
007DD9D7  33 C8                           xor ecx, eax
007DD9D9  83 E1 0F                        and ecx, 0xf
007DD9DC  33 C8                           xor ecx, eax
007DD9DE  41 89 8E B8 00 00 00            mov dword ptr [r14 + 0xb8], ecx
007DD9E5  0F B7 46 36                     movzx eax, word ptr [rsi + 0x36]
007DD9E9  33 C1                           xor eax, ecx
007DD9EB  25 F0 00 00 00                  and eax, 0xf0
007DD9F0  33 C1                           xor eax, ecx
007DD9F2  49 8B 4E 20                     mov rcx, qword ptr [r14 + 0x20]
007DD9F6  41 89 86 B8 00 00 00            mov dword ptr [r14 + 0xb8], eax
007DD9FD  8A 46 37                        mov al, byte ptr [rsi + 0x37]
007DDA00  41 88 86 B9 00 00 00            mov byte ptr [r14 + 0xb9], al
007DDA07  F6 81 8C 00 00 00 01            test byte ptr [rcx + 0x8c], 1
007DDA0E  74 07                           je 0x1407dda17
007DDA10  E8 0B F2 07 00                  call 0x14085cc20
007DDA15  EB 05                           jmp 0x1407dda1c
007DDA17  E8 24 85 07 00                  call 0x140855f40
007DDA1C  8B 75 88                        mov esi, dword ptr [rbp - 0x78]
007DDA1F  48 8B CF                        mov rcx, rdi
007DDA22  8B D6                           mov edx, esi
007DDA24  66 41 C7 46 08 40 00            mov word ptr [r14 + 8], 0x40
007DDA2B  E8 14 64 01 00                  call 0x1407f3e44
007DDA30  84 C0                           test al, al
007DDA32  74 0D                           je 0x1407dda41
007DDA34  45 33 C0                        xor r8d, r8d
007DDA37  8B D6                           mov edx, esi
007DDA39  48 8B CF                        mov rcx, rdi
007DDA3C  E8 2F D3 06 00                  call 0x14084ad70
007DDA41  4C 8D 4D 08                     lea r9, [rbp + 8]
007DDA45  41 B8 01 00 00 00               mov r8d, 1
007DDA4B  49 8B CE                        mov rcx, r14
007DDA4E  E8 41 A6 0E 00                  call 0x1408c8094
007DDA53  44 38 3D 08 C0 7F 00            cmp byte ptr [rip + 0x7fc008], r15b
007DDA5A  75 15                           jne 0x1407dda71
007DDA5C  48 8B 05 FD A5 7F 00            mov rax, qword ptr [rip + 0x7fa5fd]
007DDA63  48 89 05 56 A7 7F 00            mov qword ptr [rip + 0x7fa756], rax
007DDA6A  C6 05 F1 BF 7F 00 01            mov byte ptr [rip + 0x7fbff1], 1
007DDA71  33 D2                           xor edx, edx
007DDA73  48 8D 4D F8                     lea rcx, [rbp - 8]
007DDA77  E8 24 DF C3 FF                  call 0x14041b9a0
007DDA7C  E8 03 C0 3E 00                  call 0x140bc9a84
007DDA81  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
007DDA85  41 8A F7                        mov sil, r15b
007DDA88  E8 7B 3C 1D 00                  call 0x1409b1708
007DDA8D  48 8D 4D 08                     lea rcx, [rbp + 8]
007DDA91  4C 89 7D B0                     mov qword ptr [rbp - 0x50], r15
007DDA95  E8 16 AA 06 00                  call 0x1408484b0
007DDA9A  EB 71                           jmp 0x1407ddb0d
007DDA9C  BB 89 01 00 C0                  mov ebx, 0xc0000189
007DDAA1  E9 1D FA FF FF                  jmp 0x1407dd4c3
007DDAA6  BB 25 04 00 C0                  mov ebx, 0xc0000425
007DDAAB  E9 13 FA FF FF                  jmp 0x1407dd4c3
007DDAB0  BB 7C 01 00 C0                  mov ebx, 0xc000017c
007DDAB5  E9 09 FA FF FF                  jmp 0x1407dd4c3
007DDABA  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
007DDABE  48 89 45 C0                     mov qword ptr [rbp - 0x40], rax
007DDAC2  44 8B 64 24 70                  mov r12d, dword ptr [rsp + 0x70]
007DDAC7  44 8A 7C 24 75                  mov r15b, byte ptr [rsp + 0x75]
007DDACC  41 8B D4                        mov edx, r12d
007DDACF  48 8B CF                        mov rcx, rdi
007DDAD2  E8 6D 63 01 00                  call 0x1407f3e44
007DDAD7  84 C0                           test al, al
007DDAD9  74 0E                           je 0x1407ddae9
007DDADB  45 33 C0                        xor r8d, r8d
007DDADE  41 8B D4                        mov edx, r12d
007DDAE1  48 8B CF                        mov rcx, rdi
007DDAE4  E8 87 D2 06 00                  call 0x14084ad70
007DDAE9  45 84 FF                        test r15b, r15b
007DDAEC  74 1C                           je 0x1407ddb0a
007DDAEE  48 8B CF                        mov rcx, rdi
007DDAF1  E8 42 AC 06 00                  call 0x140848738
007DDAF6  45 84 FF                        test r15b, r15b
007DDAF9  74 0F                           je 0x1407ddb0a
007DDAFB  49 8B CE                        mov rcx, r14
007DDAFE  E8 BD B7 3E 00                  call 0x140bc92c0
007DDB03  EB 05                           jmp 0x1407ddb0a
007DDB05  BB 0D 00 00 C0                  mov ebx, 0xc000000d
007DDB0A  45 33 FF                        xor r15d, r15d
007DDB0D  33 D2                           xor edx, edx
007DDB0F  48 8D 4D F8                     lea rcx, [rbp - 8]
007DDB13  E8 88 DE C3 FF                  call 0x14041b9a0
007DDB18  40 84 F6                        test sil, sil
007DDB1B  74 05                           je 0x1407ddb22
007DDB1D  E8 62 BF 3E 00                  call 0x140bc9a84
007DDB22  48 8B 4D B0                     mov rcx, qword ptr [rbp - 0x50]
007DDB26  48 85 C9                        test rcx, rcx
007DDB29  74 09                           je 0x1407ddb34
007DDB2B  E8 D8 3B 1D 00                  call 0x1409b1708
007DDB30  4C 89 7D B0                     mov qword ptr [rbp - 0x50], r15
007DDB34  4C 39 7D F0                     cmp qword ptr [rbp - 0x10], r15
007DDB38  74 1C                           je 0x1407ddb56
007DDB3A  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007DDB41  48 8D 55 B8                     lea rdx, [rbp - 0x48]
007DDB45  48 8B CF                        mov rcx, rdi
007DDB48  74 07                           je 0x1407ddb51
007DDB4A  E8 D1 F0 07 00                  call 0x14085cc20
007DDB4F  EB 05                           jmp 0x1407ddb56
007DDB51  E8 EA 83 07 00                  call 0x140855f40
007DDB56  4D 85 ED                        test r13, r13
007DDB59  74 1C                           je 0x1407ddb77
007DDB5B  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007DDB62  48 8D 55 80                     lea rdx, [rbp - 0x80]
007DDB66  48 8B CF                        mov rcx, rdi
007DDB69  74 07                           je 0x1407ddb72
007DDB6B  E8 B0 F0 07 00                  call 0x14085cc20
007DDB70  EB 05                           jmp 0x1407ddb77
007DDB72  E8 C9 83 07 00                  call 0x140855f40
007DDB77  4C 39 7D C0                     cmp qword ptr [rbp - 0x40], r15
007DDB7B  74 1C                           je 0x1407ddb99
007DDB7D  F6 87 8C 00 00 00 01            test byte ptr [rdi + 0x8c], 1
007DDB84  48 8D 55 A0                     lea rdx, [rbp - 0x60]
007DDB88  48 8B CF                        mov rcx, rdi
007DDB8B  74 07                           je 0x1407ddb94
007DDB8D  E8 8E F0 07 00                  call 0x14085cc20
007DDB92  EB 05                           jmp 0x1407ddb99
007DDB94  E8 A7 83 07 00                  call 0x140855f40
007DDB99  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007DDB9D  E8 AA 25 1D 00                  call 0x1409b014c
007DDBA2  8B CB                           mov ecx, ebx
007DDBA4  E8 8F 8B 00 00                  call 0x1407e6738
007DDBA9  8B C3                           mov eax, ebx
007DDBAB  48 8B 8D 00 02 00 00            mov rcx, qword ptr [rbp + 0x200]
007DDBB2  48 33 CC                        xor rcx, rsp
007DDBB5  E8 86 EA EC FF                  call 0x1406ac640
007DDBBA  48 8B 9C 24 60 03 00 00         mov rbx, qword ptr [rsp + 0x360]
007DDBC2  48 81 C4 10 03 00 00            add rsp, 0x310
007DDBC9  41 5F                           pop r15
007DDBCB  41 5E                           pop r14
007DDBCD  41 5D                           pop r13
007DDBCF  41 5C                           pop r12
007DDBD1  5F                              pop rdi
007DDBD2  5E                              pop rsi
007DDBD3  5D                              pop rbp
007DDBD4  C3                              ret
007DDBD5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmRestoreKey(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m1F8;
    unsigned __int64 v_stack_m208;
    unsigned __int64 v_stack_m210;
    unsigned __int64 v_stack_m218;
    unsigned __int64 v_stack_m220;
    unsigned __int64 v_stack_m230;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned __int64 v_stack_m250;
    unsigned __int64 v_stack_m258;
    unsigned int v_stack_m260;
    unsigned int v_stack_m264;
    unsigned int v_stack_m268;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m280;
    unsigned __int64 v_stack_m288;
    unsigned int v_stack_m28C;
    unsigned int v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned int v_stack_m2A0;
    unsigned int v_stack_m2A4;
    unsigned int v_stack_m2A8;
    unsigned int v_stack_m2B0;
    unsigned int v_stack_m2B4;
    unsigned int v_stack_m2B8;
    unsigned int v_stack_m2C0;
    unsigned int v_stack_m2C4;
    unsigned int v_stack_m2C8;
    unsigned int v_stack_m2CC;
    unsigned int v_stack_m2D0;
    unsigned __int8 v_stack_m2D3;
    unsigned __int8 v_stack_m2D4;
    unsigned int v_stack_m2D8;
    unsigned __int64 v_stack_m2E8;
    unsigned __int64 v_stack_m2F0;
    unsigned __int64 v_stack_m2F8;
    unsigned __int64 v_stack_m300;
    unsigned __int64 v_stack_m308;
    unsigned int v_stack_m310;
    unsigned __int64 v_stack_m318;
    unsigned __int64 v_stack_m320;
    unsigned __int64 v_stack_m328;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rsp = (v_rsp) - (784);
    result = (*(unsigned __int64 *)(v_rip + 6477846)) ^ (v_rsp);
    v_stack_m48 = result;
    v_rdi = 0;
    v_stack_m260 = a3;
    v_r14 = (unsigned int)((v_r14) | (0xFFFFFFFFULL));
    v_stack_m2D4 = (unsigned __int8)(a4);
    v_stack_m258 = 0;
    v_stack_m290 = (unsigned int)(v_r14);
    v_stack_m288 = 0;
    v_stack_m280 = 0;
    v_stack_m28C = 0;
    a2 = 0;
    v_stack_m2A8 = (unsigned int)(v_r14);
    v_stack_m2A4 = 0;
    v_stack_m2C8 = (unsigned int)(v_r14);
    v_stack_m2C4 = 0;
    v_stack_m2B8 = (unsigned int)(v_r14);
    v_stack_m2B4 = 0;
    v_stack_m298 = 0;
    v_stack_m2D0 = (unsigned int)(v_r14);
    v_stack_m2CC = 0;
    v_stack_m220 = v_xmm0;
    v_stack_m210 = v_xmm0;
    v_stack_m240 = v_xmm0;
    result = memset(v_stack_m1F8, a2, 432, a4);
    v_stack_m2B0 = 0;
    v_stack_m250 = v_xmm0;
    v_stack_m278 = v_xmm1;
    result = CmpInitializeDelayDerefContext(v_stack_m250, a2, 432, a4);
    v_stack_m268 = (unsigned int)(v_r14);
    v_stack_m2D8 = (unsigned int)(v_r14);
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 160)) & (0x100000ULL)) == 0) goto loc_007DCFEB;
    goto loc_007DDB0A;
loc_007DCFEB:
    result = CmpTraceHiveRestoreStart((unsigned int)(0xC0000022ULL), (unsigned int)((unsigned int)((unsigned int)(a3))), 432, a4);
    a1 = ((((unsigned int)((unsigned int)(a3))) & (0xFFFFFFFDULL)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)((unsigned int)(a3))) & (2)) != 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) != 0) goto loc_007DDB05;
    result = 0;
    if ((*(unsigned __int64 *)(a1 + 56)) != 0) goto loc_007DDB05;
    if ((*(unsigned __int64 *)(a1 + 64)) != 0) goto loc_007DDB05;
    if ((((unsigned __int8)((unsigned int)(a3))) & (1)) == 0) goto loc_007DD03F;
    result = CmpLoadHiveVolatile(a1, (unsigned int)(0xC0000022ULL), 432, a4);
loc_007DD038:
    goto loc_007DDB0A;
loc_007DD03F:
    if ((((unsigned __int8)((unsigned int)(a3))) & (2)) == 0) goto loc_007DD04F;
    result = CmpRefreshHive(a1, (unsigned int)(0xC0000022ULL), 432, a4);
    goto loc_007DD038;
loc_007DD04F:
    v_r15 = 0;
    v_stack_m220 = (unsigned int)((unsigned int)(result));
    v_stack_m208 = 0;
    v_stack_m238 = v_stack_m240;
    v_stack_m240 = v_stack_m240;
    a4 = 0;
    v_stack_m2E8 = v_stack_m1F8;
    v_stack_m2F0 = 0;
    v_stack_m2F8 = 0;
    v_stack_m300 = 0;
    v_stack_m308 = 0;
    v_stack_m310 = 0x1190001ULL;
    v_stack_m318 = 0;
    v_stack_m320 = v_stack_m220;
    v_stack_m328 = 0;
    v_stack_m218 = v_xmm0;
    result = CmpCreateHive(v_stack_m298, v_r15 + 2, (unsigned int)(0x8000ULL), a4);
    if (sign_flag) goto loc_007DDB0D;
    a1 = 0;
    result = CmpLockRegistryFreezeAware(a1, v_r15 + 2, (unsigned int)(0x8000ULL), a4);
    result = CmpLockKcbShared(*(unsigned __int64 *)(a1 + 8), v_r15 + 2, (unsigned int)(0x8000ULL), a4);
    result = 0;
    v_stack_m2C0 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)));
    if ((*(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 66)) == 0) goto loc_007DD101;
    result = CmpLogUnsupportedOperation(result + 17, v_r15 + 2, (unsigned int)(0x8000ULL), a4);
    goto loc_007DDAFB;
loc_007DD101:
    a2 = 0;
    result = CmpIsKeyDeletedForKeyBody(0, a2, (unsigned int)(0x8000ULL), a4);
    if ((unsigned __int8)(result) == 0) goto loc_007DD119;
    goto loc_007DDAFB;
loc_007DD119:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 65)) != 1) goto loc_007DD129;
loc_007DD11F:
    goto loc_007DDAFB;
loc_007DD129:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32)) == (*(unsigned __int64 *)(v_rip + 8374624))) goto loc_007DD11F;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 2944)) != 1) goto loc_007DD145;
    goto loc_007DDAFB;
loc_007DD145:
    result = HvLockHiveFlusherShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), a2, (unsigned int)(0x8000ULL), a4);
    v_stack_m2D3 = 1;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DD16B;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(0xC0000189ULL))), v_stack_m2C8, a4);
    goto loc_007DD170;
loc_007DD16B:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(0xC0000189ULL))), v_stack_m2C8, a4);
loc_007DD170:
    if (result != 0) goto loc_007DD182;
    goto loc_007DDAEE;
loc_007DD182:
    if (((*(unsigned __int8 *)(result + 2)) & (4)) == 0) goto loc_007DD18E;
    result = (unsigned int)((result) | (0xFFFFFFFFULL));
    goto loc_007DD192;
loc_007DD18E:
loc_007DD192:
    v_stack_m310 = v_stack_m2D8;
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(0xC000009AULL)))) >> (31));
    v_stack_m318 = a3;
    v_stack_m2A0 = a3;
    v_stack_m264 = (unsigned int)((unsigned int)(*(unsigned int *)(result + 16)));
    v_stack_m328 = 6;
    result = CmpCopyKeyPartial(v_stack_m298, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m298 + 64) + 36)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 16)))));
    if (sign_flag) goto loc_007DDAEE;
    a3 = (unsigned int)((*(unsigned __int16 *)(result + 72)) + (76));
    v_stack_m318 = v_stack_m2A8;
    v_stack_m320 = v_stack_m280;
    v_stack_m328 = v_stack_m268;
    result = HvReallocateCell(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(v_stack_m2D8), a3, 1);
    if (sign_flag) goto loc_007DDABA;
    v_stack_m2D8 = (unsigned int)((unsigned int)(v_stack_m268));
    v_stack_m288 = v_stack_m280;
    result = memcpy(v_stack_m280 + 76, result + 76, *(unsigned __int16 *)(result + 72), 1);
    *(unsigned __int16 *)(v_stack_m280 + 72) = (unsigned __int16)(*(unsigned __int16 *)(result + 72));
    if (((*(unsigned __int8 *)(result + 2)) & (32)) == 0) goto loc_007DD24E;
    goto loc_007DD257;
loc_007DD24E:
loc_007DD257:
    result = 0;
    v_stack_m320 = 0;
    v_stack_m328 = 2;
    result = CmpCopySyncTree(v_stack_m298, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m298 + 64) + 36)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m268))));
    if (sign_flag) goto loc_007DDAC2;
    result = HvUnlockHiveFlusherShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m298 + 64) + 36)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m268))));
    v_rbx = 0;
    v_stack_m2D3 = 0;
    result = CmpUnlockKcb(*(unsigned __int64 *)(a1 + 8), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m298 + 64) + 36)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m268))));
    result = CmpUnlockRegistry(*(unsigned __int64 *)(a1 + 8), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m298 + 64) + 36)), *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m268))));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DD2B7;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2C8, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m268))));
    goto loc_007DD2BC;
loc_007DD2B7:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2C8, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m268))));
loc_007DD2BC:
    v_stack_m280 = 0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DD2DA;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2A8, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m268))));
    goto loc_007DD2DF;
loc_007DD2DA:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2A8, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m268))));
loc_007DD2DF:
    v_stack_m288 = 0;
loc_007DD2E6:
    result = CmpLockRegistryFreezeAware(1, v_stack_m2A8, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m268))));
loc_007DD2EE:
    result = CmpIsShutdownRundownActive(1, v_stack_m2A8, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m268))));
    if ((unsigned __int8)(result) != 0) goto loc_007DDA9C;
    a2 = 0;
    result = CmpIsKeyDeletedForKeyBody(0, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m268))));
    if ((unsigned __int8)(result) != 0) goto loc_007DD566;
    if (((unsigned int)((unsigned int)(v_stack_m2C0))) != (*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40))) goto loc_007DDAB0;
    if (((*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 8)) & (0x40000ULL)) != 0) goto loc_007DDAA6;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 2944)) == 1) goto loc_007DDA9C;
    if (((unsigned int)((unsigned int)(v_stack_m264))) == -1) goto loc_007DD35E;
    v_stack_m328 = 1;
    result = CmpCheckKeyAccess(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m264))), v_stack_m2D4, 4);
    if (sign_flag) goto loc_007DD4C3;
loc_007DD35E:
    v_stack_m328 = 1;
    result = CmpCheckKeyAccess(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m2C0))), v_stack_m2D4, (unsigned int)(0x10000ULL));
    if (sign_flag) goto loc_007DD4C3;
    result = CmpTryAcquireKcbIXLocks(*(unsigned __int64 *)(a1 + 8), 1, v_stack_m2D4, v_stack_m278);
    if (((unsigned int)(result)) != 0xC000022DULL) goto loc_007DD3ED;
    a2 = 0;
    v_stack_m328 = (unsigned int)((unsigned int)(v_stack_m278));
    result = CmpLogTransactionAbortedWithChildName(*(unsigned __int64 *)(a1 + 8), a2, a2 + 7, v_stack_m278);
    result = CmpUnlockRegistry(*(unsigned __int64 *)(a1 + 8), a2, a2 + 7, v_stack_m278);
    a2 = 0;
    result = CmpAbortRollbackPacket(v_stack_m278, a2, a2 + 7, v_stack_m278);
    if (sign_flag) goto loc_007DD4BC;
    result = CmpCleanupRollbackPacket(v_stack_m278, a2, a2 + 7, v_stack_m278);
    v_stack_m278 = v_xmm0;
    result = CmpRetryBackOff(v_stack_m2B0, a2, a2 + 7, v_stack_m278);
    result = CmpLockRegistryFreezeAware(1, a2, a2 + 7, v_stack_m278);
    goto loc_007DD2EE;
loc_007DD3ED:
    if (sign_flag) goto loc_007DD4C3;
    v_stack_m328 = 2;
    result = CmpDoAccessCheckOnSubtree(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m2C0))), v_stack_m2D4, (unsigned int)(0x10000ULL));
    if (sign_flag) goto loc_007DD4C3;
    if (((v_stack_m260) & (8)) == 0) goto loc_007DD513;
    a2 = 0;
    result = CmpPrepareToInvalidateAllHigherLayerKcbs(*(unsigned __int64 *)(a1 + 8), a2, v_stack_m278, (unsigned int)(0x10000ULL));
    result = (unsigned int)((result) + ((unsigned int)((unsigned int)(0x80000000ULL))));
    if ((((unsigned int)((unsigned int)(0x80000000ULL))) & ((unsigned int)(result))) != 0) goto loc_007DD44B;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != 0xC000022DULL) goto loc_007DD4C3;
loc_007DD44B:
    a2 = 0;
    result = CmpPrepareForSubtreeInvalidation(*(unsigned __int64 *)(a1 + 8), a2, v_stack_m278, (unsigned int)(0x10000ULL));
    if (((unsigned int)(result)) == ((unsigned int)((unsigned int)(0xC000022DULL)))) goto loc_007DD46C;
    if (sign_flag) goto loc_007DD4C3;
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) != ((unsigned int)((unsigned int)(0xC000022DULL)))) goto loc_007DD4CB;
loc_007DD46C:
    a2 = 0;
    v_stack_m328 = (unsigned int)((unsigned int)(v_stack_m278));
    result = CmpLogTransactionAbortedWithChildName(*(unsigned __int64 *)(a1 + 8), a2, a2 + 7, (unsigned int)(0x10000ULL));
    result = CmpUnlockRegistry(*(unsigned __int64 *)(a1 + 8), a2, a2 + 7, (unsigned int)(0x10000ULL));
    result = 0;
    a2 = 0;
    result = CmpAbortRollbackPacket(v_stack_m278, a2, a2 + 7, (unsigned int)(0x10000ULL));
    if (sign_flag) goto loc_007DD507;
    result = CmpCleanupRollbackPacket(v_stack_m278, a2, a2 + 7, (unsigned int)(0x10000ULL));
    v_stack_m278 = v_xmm0;
    result = CmpRetryBackOff(v_stack_m2B0, a2, a2 + 7, (unsigned int)(0x10000ULL));
    goto loc_007DD2E6;
loc_007DD4BC:
    result = CmpLockRegistryFreezeAware(1, a2, a2 + 7, (unsigned int)(0x10000ULL));
loc_007DD4C3:
    goto loc_007DDAC2;
loc_007DD4CB:
    a3 = 0;
    result = CmpInvalidateAllHigherLayerKcbs(*(unsigned __int64 *)(a1 + 8), a3 + 1, a3, v_stack_m250);
    v_r12 = 0;
    a3 = 0;
    v_stack_m328 = 0;
    result = CmpInvalidateSubtree(*(unsigned __int64 *)(a1 + 8), v_r12 + 1, a3, v_stack_m250);
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m250, a2, a3, v_stack_m250);
    goto loc_007DD576;
loc_007DD507:
    result = CmpLockRegistryFreezeAware(1, a2, a3, v_stack_m250);
    goto loc_007DDAC2;
loc_007DD513:
    v_stack_m230 = v_xmm0;
    result = CmpInitializeDelayDerefContext(v_stack_m230, a2, a3, v_stack_m250);
    v_stack_m318 = 1;
    v_r12 = 0;
    v_stack_m320 = 1;
    v_stack_m328 = 0;
    result = CmpEnumerateAllHigherLayerKcbs(*(unsigned __int64 *)(a1 + 8), v_rip - 858743, v_rip + 81685, v_stack_m230);
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m230, a2, v_rip + 81685, v_stack_m230);
    result = CmpDoesKeyHaveOpenSubkeys(*(unsigned __int64 *)(a1 + 8), a2, v_rip + 81685, v_stack_m230);
    if ((unsigned __int8)(result) == 0) goto loc_007DD570;
loc_007DD566:
    goto loc_007DD4C3;
loc_007DD570:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8))) != 1) goto loc_007DD566;
loc_007DD576:
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m268))), a3, a4);
    if (sign_flag) goto loc_007DDAC2;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DD5AE;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(v_stack_m2C0), v_stack_m2A8, a4);
    goto loc_007DD5B3;
loc_007DD5AE:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(v_stack_m2C0), v_stack_m2A8, a4);
loc_007DD5B3:
    v_stack_m288 = result;
    if (result != 0) goto loc_007DD5C6;
loc_007DD5BC:
    goto loc_007DDAC2;
loc_007DD5C6:
    if (((*(unsigned __int8 *)(result + 2)) & (4)) == 0) goto loc_007DD689;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 8373426) + 140)) & (1)) == 0) goto loc_007DD5F2;
    result = HvpGetCellFlat(*(unsigned __int64 *)(v_rip + 8373426), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 16)))), v_stack_m2B8, a4);
    goto loc_007DD5F7;
loc_007DD5F2:
    result = HvpGetCellPaged(*(unsigned __int64 *)(v_rip + 8373426), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 16)))), v_stack_m2B8, a4);
loc_007DD5F7:
    if (result != 0) goto loc_007DD60B;
loc_007DD601:
    goto loc_007DDAC7;
loc_007DD60B:
    *(unsigned int *)(result + 28) = (unsigned int)((unsigned int)(v_stack_m2D8));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 8373366) + 140)) & (1)) == 0) goto loc_007DD62A;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(v_rip + 8373366), v_stack_m2B8, v_stack_m2B8, a4);
    goto loc_007DD62F;
loc_007DD62A:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(v_rip + 8373366), v_stack_m2B8, v_stack_m2B8, a4);
loc_007DD62F:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DD649;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m2D8))), v_stack_m2C8, a4);
    goto loc_007DD64E;
loc_007DD649:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m2D8))), v_stack_m2C8, a4);
loc_007DD64E:
    if (result == 0) goto loc_007DD601;
    *(unsigned int *)(result + 16) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 16)));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 64) + 36) = (unsigned int)((unsigned int)(v_stack_m2D8));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DD679;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2C8, v_stack_m2C8, a4);
    goto loc_007DD67E;
loc_007DD679:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2C8, v_stack_m2C8, a4);
loc_007DD67E:
    v_r15 = 0;
    goto loc_007DD908;
loc_007DD689:
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2C8, a3, a4);
    if (sign_flag) goto loc_007DDAC2;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DD6BB;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), 0, v_stack_m2B8, a4);
    goto loc_007DD6C0;
loc_007DD6BB:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), 0, v_stack_m2B8, a4);
loc_007DD6C0:
    if (result == 0) goto loc_007DD5BC;
    v_stack_m2A0 = (unsigned int)((unsigned int)(*(unsigned int *)(result + (unsigned int)(v_stack_m2A0) * 4 + 28)));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DD6ED;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2B8, v_stack_m2B8, a4);
    goto loc_007DD6F2;
loc_007DD6ED:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2B8, v_stack_m2B8, a4);
loc_007DD6F2:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DD70B;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + (unsigned int)(v_stack_m2A0) * 4 + 28)))), v_stack_m290, a4);
    goto loc_007DD710;
loc_007DD70B:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + (unsigned int)(v_stack_m2A0) * 4 + 28)))), v_stack_m290, a4);
loc_007DD710:
    v_stack_m258 = result;
    if (result != 0) goto loc_007DD726;
    goto loc_007DD4C3;
loc_007DD726:
    if ((*(unsigned __int16 *)(result)) != ((unsigned __int16)((unsigned int)(0x6972ULL)))) goto loc_007DD73A;
    goto loc_007DD743;
loc_007DD73A:
loc_007DD743:
    v_stack_m2B0 = 1;
loc_007DD746:
    if (((unsigned int)((unsigned int)(v_stack_m2D8))) >= 1) goto loc_007DD878;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DD76F;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(v_stack_m2A0 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m2D8))) * 4)), v_stack_m2D0, a4);
    goto loc_007DD774;
loc_007DD76F:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(v_stack_m2A0 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m2D8))) * 4)), v_stack_m2D0, a4);
loc_007DD774:
    result = 0;
    if (0 == 0) goto loc_007DD868;
    a4 = 0;
    a3 = 0;
    result = HvpMarkCellDirty(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(v_stack_m2A0 + (unsigned int)((unsigned int)((unsigned int)(v_stack_m2D8))) * 4)), a3, a4);
    a2 = 0;
    if (sign_flag) goto loc_007DD83F;
    result = (unsigned __int16)((*(unsigned __int16 *)(result)) - ((unsigned __int16)((unsigned int)(0x666CULL))));
    if ((((unsigned __int16)((unsigned int)(0xFDFFULL))) & ((unsigned __int16)(result))) == 0) goto loc_007DD7D1;
loc_007DD7C0:
    if (0 >= ((unsigned int)(*(unsigned __int16 *)(result + 2)))) goto loc_007DD7E2;
    if ((*(unsigned int *)(result + 0 * 4 + 4)) == ((unsigned int)((unsigned int)(v_stack_m2C0)))) goto loc_007DD80A;
    result = (unsigned int)((0) + 1);
    goto loc_007DD7C0;
loc_007DD7D1:
    if (((unsigned int)(result)) >= ((unsigned int)(*(unsigned __int16 *)(result + 2)))) goto loc_007DD7E2;
    if ((*(unsigned int *)(result + (unsigned int)((unsigned int)(result)) * 8 + 4)) == ((unsigned int)((unsigned int)(v_stack_m2C0)))) goto loc_007DD81D;
    result = (unsigned int)((result) + 1);
    goto loc_007DD7D1;
loc_007DD7E2:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DD7FA;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2D0, (unsigned int)(v_stack_m2C0), a4);
    goto loc_007DD7FF;
loc_007DD7FA:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2D0, (unsigned int)(v_stack_m2C0), a4);
loc_007DD7FF:
    v_r12 = (unsigned int)(((unsigned int)(v_stack_m2D8)) + 1);
    goto loc_007DD746;
loc_007DD80A:
    *(unsigned int *)(result + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) * 4 + 4) = (unsigned int)((unsigned int)(v_stack_m2D8));
    goto loc_007DD827;
loc_007DD816:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2D0, (unsigned int)(v_stack_m2C0), a4);
    goto loc_007DD87D;
loc_007DD81D:
    *(unsigned int *)(result + *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) * 8 + 4) = (unsigned int)((unsigned int)(v_stack_m2D8));
loc_007DD827:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DD816;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2D0, (unsigned int)(v_stack_m2C0), a4);
    goto loc_007DD87D;
loc_007DD83F:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DD857;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2D0, (unsigned int)(v_stack_m2C0), a4);
    goto loc_007DD85C;
loc_007DD857:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2D0, (unsigned int)(v_stack_m2C0), a4);
loc_007DD85C:
    goto loc_007DDAC2;
loc_007DD868:
    goto loc_007DDAC2;
loc_007DD878:
loc_007DD87D:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DD897;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), 0, v_stack_m2B8, a4);
    goto loc_007DD89C;
loc_007DD897:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), 0, v_stack_m2B8, a4);
loc_007DD89C:
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DD8B9;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m2D8))), v_stack_m2C8, a4);
    goto loc_007DD8BE;
loc_007DD8B9:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m2D8))), v_stack_m2C8, a4);
loc_007DD8BE:
    if ((*(unsigned int *)(result + 56)) < ((unsigned int)(*(unsigned __int16 *)(result + 74)))) {
        *(unsigned int *)(result + 56) = (unsigned int)(*(unsigned __int16 *)(result + 74));
    }
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DD8E1;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2C8, v_stack_m2C8, a4);
    goto loc_007DD8E6;
loc_007DD8E1:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2C8, v_stack_m2C8, a4);
loc_007DD8E6:
    v_r15 = 0;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DD903;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2B8, v_stack_m2C8, a4);
    goto loc_007DD908;
loc_007DD903:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2B8, v_stack_m2C8, a4);
loc_007DD908:
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40) = (unsigned int)((unsigned int)(v_stack_m2D8));
    result = CmpCleanUpKcbCachedSymlink(*(unsigned __int64 *)(a1 + 8), v_stack_m250, v_stack_m2C8, a4);
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DD93F;
    result = HvpGetCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), v_stack_m2D0, a4);
    goto loc_007DD944;
loc_007DD93F:
    result = HvpGetCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 40)), v_stack_m2D0, a4);
loc_007DD944:
    if (result != 0) goto loc_007DD959;
    goto loc_007DDAC7;
loc_007DD959:
    a4 = 0;
    a3 = 0;
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 100) = (unsigned int)((unsigned int)(*(unsigned int *)(1 + 40)));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 96) = (unsigned int)((unsigned int)(*(unsigned int *)(1 + 36)));
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 186) = (unsigned __int16)(*(unsigned __int16 *)(1 + 2));
    v_stack_m328 = 0;
    result = CmpAssignSecurityToKcb(*(unsigned __int64 *)(a1 + 8), (unsigned int)(*(unsigned int *)(1 + 44)), a3, a4);
    result = CmpCleanUpSubKeyInfo(*(unsigned __int64 *)(a1 + 8), 1, a3, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 168) = *(unsigned __int64 *)(1 + 4);
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 176) = (unsigned __int16)(*(unsigned __int16 *)(1 + 52));
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 178) = (unsigned __int16)(*(unsigned __int16 *)(1 + 60));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 180) = (unsigned int)((unsigned int)(*(unsigned int *)(1 + 64)));
    a1 = (unsigned int)((*(unsigned __int16 *)(1 + 54)) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 184)))));
    a1 = (unsigned int)((a1) & (15));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 184)))));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 184) = (unsigned int)(a1);
    result = (unsigned int)((*(unsigned __int16 *)(1 + 54)) ^ ((unsigned int)(a1)));
    result = (unsigned int)((result) & (240));
    result = (unsigned int)((result) ^ ((unsigned int)(a1)));
    *(unsigned int *)(*(unsigned __int64 *)(a1 + 8) + 184) = (unsigned int)(result);
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 8) + 185) = (unsigned __int8)(*(unsigned __int8 *)(1 + 55));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DDA17;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2D0, a3, a4);
    goto loc_007DDA1C;
loc_007DDA17:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2D0, a3, a4);
loc_007DDA1C:
    *(unsigned __int16 *)(*(unsigned __int64 *)(a1 + 8) + 8) = 64;
    result = CmpDeleteTree(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m2C0))), a3, a4);
    if ((unsigned __int8)(result) != 0) {
        a3 = 0;
        a2 = (unsigned int)((unsigned int)(v_stack_m2C0));
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32);
        result = CmpFreeKeyByCell(a1, a2, a3, a4);
    }
    result = CmpReportNotify(*(unsigned __int64 *)(a1 + 8), a2, 1, v_stack_m240);
    if ((*(unsigned __int8 *)(v_rip + 8372232)) == 0) {
        result = *(unsigned __int64 *)(v_rip + 8365565);
        *(unsigned __int64 *)(v_rip + 8365910) = result;
        *(unsigned __int8 *)(v_rip + 8372209) = 1;
    }
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m250, a2, 1, v_stack_m240);
    result = CmpUnlockRegistry(v_stack_m250, a2, 1, v_stack_m240);
    result = CmpDestroyHive(v_stack_m298, a2, 1, v_stack_m240);
    v_stack_m298 = 0;
    result = CmpSignalDeferredPosts(v_stack_m240, a2, 1, v_stack_m240);
    goto loc_007DDB0D;
loc_007DDA9C:
    goto loc_007DD4C3;
loc_007DDAA6:
    goto loc_007DD4C3;
loc_007DDAB0:
    goto loc_007DD4C3;
loc_007DDABA:
    v_stack_m288 = v_stack_m280;
loc_007DDAC2:
loc_007DDAC7:
    result = CmpDeleteTree(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), (unsigned int)((unsigned int)((unsigned int)(v_stack_m2D8))), 1, v_stack_m240);
    if ((unsigned __int8)(result) != 0) {
        a3 = 0;
        a2 = (unsigned int)((unsigned int)(v_stack_m2D8));
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32);
        result = CmpFreeKeyByCell(a1, a2, a3, v_stack_m240);
    }
    if ((unsigned __int8)(v_stack_m2D3) == 0) goto loc_007DDB0A;
loc_007DDAEE:
    result = HvUnlockHiveFlusherShared(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), a2, a3, v_stack_m240);
    if ((unsigned __int8)(v_stack_m2D3) == 0) goto loc_007DDB0A;
loc_007DDAFB:
    result = CmpUnlockKcb(*(unsigned __int64 *)(a1 + 8), a2, a3, v_stack_m240);
    goto loc_007DDB0A;
loc_007DDB05:
loc_007DDB0A:
    v_r15 = 0;
loc_007DDB0D:
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m250, a2, a3, v_stack_m240);
    if (0 != 0) {
        result = CmpUnlockRegistry(v_stack_m250, a2, a3, v_stack_m240);
    }
    if (v_stack_m298 != 0) {
        result = CmpDestroyHive(v_stack_m298, a2, a3, v_stack_m240);
        v_stack_m298 = 0;
    }
    if (v_stack_m258 == 0) goto loc_007DDB56;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DDB51;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m290, a3, v_stack_m240);
    goto loc_007DDB56;
loc_007DDB51:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m290, a3, v_stack_m240);
loc_007DDB56:
    if (0 == 0) goto loc_007DDB77;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DDB72;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2C8, a3, v_stack_m240);
    goto loc_007DDB77;
loc_007DDB72:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2C8, a3, v_stack_m240);
loc_007DDB77:
    if (v_stack_m288 == 0) goto loc_007DDB99;
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32) + 140)) & (1)) == 0) goto loc_007DDB94;
    result = HvpReleaseCellFlat(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2A8, a3, v_stack_m240);
    goto loc_007DDB99;
loc_007DDB94:
    result = HvpReleaseCellPaged(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 8) + 32), v_stack_m2A8, a3, v_stack_m240);
loc_007DDB99:
    result = CmpCleanupRollbackPacket(v_stack_m278, v_stack_m2A8, a3, v_stack_m240);
    result = CmpTraceHiveRestoreStop((unsigned int)((unsigned int)((unsigned int)(0xC000000DULL))), v_stack_m2A8, a3, v_stack_m240);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, v_stack_m2A8, a3, v_stack_m240);
    v_rsp = (v_rsp) + (784);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmRestoreKey(void *Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m1F8;
    uint64_t v_stack_m208;
    uint64_t v_stack_m210;
    uint64_t v_stack_m218;
    uint64_t v_stack_m220;
    uint64_t v_stack_m230;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint64_t v_stack_m250;
    uint64_t v_stack_m258;
    uint32_t v_stack_m260;
    uint32_t v_stack_m264;
    uint32_t v_stack_m268;
    uint64_t v_stack_m278;
    uint64_t v_stack_m280;
    uint64_t v_stack_m288;
    uint32_t v_stack_m28C;
    uint32_t v_stack_m290;
    uint64_t v_stack_m298;
    uint32_t v_stack_m2A0;
    uint32_t v_stack_m2A4;
    uint32_t v_stack_m2A8;
    uint32_t v_stack_m2B0;
    uint32_t v_stack_m2B4;
    uint32_t v_stack_m2B8;
    uint32_t v_stack_m2C0;
    uint32_t v_stack_m2C4;
    uint32_t v_stack_m2C8;
    uint32_t v_stack_m2CC;
    uint32_t v_stack_m2D0;
    uint8_t v_stack_m2D3;
    uint8_t v_stack_m2D4;
    uint32_t v_stack_m2D8;
    uint64_t v_stack_m2E8;
    uint64_t v_stack_m2F0;
    uint64_t v_stack_m2F8;
    uint64_t v_stack_m300;
    uint64_t v_stack_m308;
    uint32_t v_stack_m310;
    uint64_t v_stack_m318;
    uint64_t v_stack_m320;
    uint64_t v_stack_m328;
    uint64_t v_stack_m48;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rsp = (local_rsp) - (784);
    result = (*(uint64_t *)(v_rip + 0x62D816)) ^ (local_rsp);
    v_stack_m48 = result;
    local_rdi = 0;
    v_stack_m260 = Arg3;
    local_r14 = (uint32_t)((local_r14) | (0xFFFFFFFFULL));
    v_stack_m2D4 = (uint8_t)(Arg4);
    v_stack_m258 = 0;
    v_stack_m290 = (uint32_t)(local_r14);
    v_stack_m288 = 0;
    v_stack_m280 = 0;
    v_stack_m28C = 0;
    Arg2 = 0;
    v_stack_m2A8 = (uint32_t)(local_r14);
    v_stack_m2A4 = 0;
    v_stack_m2C8 = (uint32_t)(local_r14);
    v_stack_m2C4 = 0;
    v_stack_m2B8 = (uint32_t)(local_r14);
    v_stack_m2B4 = 0;
    v_stack_m298 = 0;
    v_stack_m2D0 = (uint32_t)(local_r14);
    v_stack_m2CC = 0;
    v_stack_m220 = v_xmm0;
    v_stack_m210 = v_xmm0;
    v_stack_m240 = v_xmm0;
    result = memset(v_stack_m1F8, Arg2, 432, Arg4);
    v_stack_m2B0 = 0;
    v_stack_m250 = v_xmm0;
    v_stack_m278 = v_xmm1;
    result = CmpInitializeDelayDerefContext(v_stack_m250, Arg2, 432, Arg4);
    v_stack_m268 = (uint32_t)(local_r14);
    v_stack_m2D8 = (uint32_t)(local_r14);
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xA0)) & (0x100000ULL)) == 0) goto loc_007DCFEB;
    goto loc_007DDB0A;
loc_007DCFEB:
    result = CmpTraceHiveRestoreStart((uint32_t)(0xC0000022ULL), (uint32_t)((uint32_t)((uint32_t)(Arg3))), 432, Arg4);
    Arg1 = ((((uint32_t)((uint32_t)(Arg3))) & (0xFFFFFFFDULL)) != 0) ? 1 : 0;
    result = ((((uint8_t)((uint32_t)(Arg3))) & (2)) != 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) != 0) goto loc_007DDB05;
    result = 0;
    if ((*(uint64_t *)(arg1 + 0x38)) != 0) goto loc_007DDB05;
    if ((*(uint64_t *)(arg1 + 0x40)) != 0) goto loc_007DDB05;
    if ((((uint8_t)((uint32_t)(Arg3))) & (1)) == 0) goto loc_007DD03F;
    result = CmpLoadHiveVolatile(Arg1, (uint32_t)(0xC0000022ULL), 432, Arg4);
loc_007DD038:
    goto loc_007DDB0A;
loc_007DD03F:
    if ((((uint8_t)((uint32_t)(Arg3))) & (2)) == 0) goto loc_007DD04F;
    result = CmpRefreshHive(Arg1, (uint32_t)(0xC0000022ULL), 432, Arg4);
    goto loc_007DD038;
loc_007DD04F:
    local_r15 = 0;
    v_stack_m220 = (uint32_t)((uint32_t)(result));
    v_stack_m208 = 0;
    v_stack_m238 = v_stack_m240;
    v_stack_m240 = v_stack_m240;
    Arg4 = 0;
    v_stack_m2E8 = v_stack_m1F8;
    v_stack_m2F0 = 0;
    v_stack_m2F8 = 0;
    v_stack_m300 = 0;
    v_stack_m308 = 0;
    v_stack_m310 = 0x1190001ULL;
    v_stack_m318 = 0;
    v_stack_m320 = v_stack_m220;
    v_stack_m328 = 0;
    v_stack_m218 = v_xmm0;
    result = CmpCreateHive(v_stack_m298, local_r15 + 2, (uint32_t)(0x8000ULL), Arg4);
    if (sign_flag) goto loc_007DDB0D;
    Arg1 = 0;
    result = CmpLockRegistryFreezeAware(Arg1, local_r15 + 2, (uint32_t)(0x8000ULL), Arg4);
    result = CmpLockKcbShared(*(uint64_t *)(arg1 + 0x8), local_r15 + 2, (uint32_t)(0x8000ULL), Arg4);
    result = 0;
    v_stack_m2C0 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x28)));
    if ((*(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x42)) == 0) goto loc_007DD101;
    result = CmpLogUnsupportedOperation(result + 17, local_r15 + 2, (uint32_t)(0x8000ULL), Arg4);
    goto loc_007DDAFB;
loc_007DD101:
    Arg2 = 0;
    result = CmpIsKeyDeletedForKeyBody(0, Arg2, (uint32_t)(0x8000ULL), Arg4);
    if ((uint8_t)(result) == 0) goto loc_007DD119;
    goto loc_007DDAFB;
loc_007DD119:
    if ((*(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0x41)) != 1) goto loc_007DD129;
loc_007DD11F:
    goto loc_007DDAFB;
loc_007DD129:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20)) == (*(uint64_t *)(v_rip + 0x7FC960))) goto loc_007DD11F;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xB80)) != 1) goto loc_007DD145;
    goto loc_007DDAFB;
loc_007DD145:
    result = HvLockHiveFlusherShared(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), Arg2, (uint32_t)(0x8000ULL), Arg4);
    v_stack_m2D3 = 1;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DD16B;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(0xC0000189ULL))), v_stack_m2C8, Arg4);
    goto loc_007DD170;
loc_007DD16B:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(0xC0000189ULL))), v_stack_m2C8, Arg4);
loc_007DD170:
    if (result != 0) goto loc_007DD182;
    goto loc_007DDAEE;
loc_007DD182:
    if (((*(uint8_t *)(result + 0x2)) & (4)) == 0) goto loc_007DD18E;
    result = (uint32_t)((result) | (0xFFFFFFFFULL));
    goto loc_007DD192;
loc_007DD18E:
loc_007DD192:
    v_stack_m310 = v_stack_m2D8;
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(0xC000009AULL)))) >> (31));
    v_stack_m318 = Arg3;
    v_stack_m2A0 = Arg3;
    v_stack_m264 = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)));
    v_stack_m328 = 6;
    result = CmpCopyKeyPartial(v_stack_m298, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m298 + 0x40) + 0x24)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)))));
    if (sign_flag) goto loc_007DDAEE;
    Arg3 = (uint32_t)((*(uint16_t *)(result + 0x48)) + (76));
    v_stack_m318 = v_stack_m2A8;
    v_stack_m320 = v_stack_m280;
    v_stack_m328 = v_stack_m268;
    result = HvReallocateCell(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)(v_stack_m2D8), Arg3, 1);
    if (sign_flag) goto loc_007DDABA;
    v_stack_m2D8 = (uint32_t)((uint32_t)(v_stack_m268));
    v_stack_m288 = v_stack_m280;
    result = memcpy(v_stack_m280 + 76, result + 76, *(uint16_t *)(result + 0x48), 1);
    *(uint16_t *)(v_stack_m280 + 0x48) = (uint16_t)(*(uint16_t *)(result + 0x48));
    if (((*(uint8_t *)(result + 0x2)) & (32)) == 0) goto loc_007DD24E;
    goto loc_007DD257;
loc_007DD24E:
loc_007DD257:
    result = 0;
    v_stack_m320 = 0;
    v_stack_m328 = 2;
    result = CmpCopySyncTree(v_stack_m298, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m298 + 0x40) + 0x24)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m268))));
    if (sign_flag) goto loc_007DDAC2;
    result = HvUnlockHiveFlusherShared(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m298 + 0x40) + 0x24)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m268))));
    local_rbx = 0;
    v_stack_m2D3 = 0;
    result = CmpUnlockKcb(*(uint64_t *)(arg1 + 0x8), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m298 + 0x40) + 0x24)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m268))));
    result = CmpUnlockRegistry(*(uint64_t *)(arg1 + 0x8), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m298 + 0x40) + 0x24)), *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m268))));
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DD2B7;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2C8, *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m268))));
    goto loc_007DD2BC;
loc_007DD2B7:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2C8, *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m268))));
loc_007DD2BC:
    v_stack_m280 = 0;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DD2DA;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2A8, *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m268))));
    goto loc_007DD2DF;
loc_007DD2DA:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2A8, *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m268))));
loc_007DD2DF:
    v_stack_m288 = 0;
loc_007DD2E6:
    result = CmpLockRegistryFreezeAware(1, v_stack_m2A8, *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m268))));
loc_007DD2EE:
    result = CmpIsShutdownRundownActive(1, v_stack_m2A8, *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m268))));
    if ((uint8_t)(result) != 0) goto loc_007DDA9C;
    Arg2 = 0;
    result = CmpIsKeyDeletedForKeyBody(0, Arg2, *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m268))));
    if ((uint8_t)(result) != 0) goto loc_007DD566;
    if (((uint32_t)((uint32_t)(v_stack_m2C0))) != (*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x28))) goto loc_007DDAB0;
    if (((*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8)) & (0x40000ULL)) != 0) goto loc_007DDAA6;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0xB80)) == 1) goto loc_007DDA9C;
    if (((uint32_t)((uint32_t)(v_stack_m264))) == -1) goto loc_007DD35E;
    v_stack_m328 = 1;
    result = CmpCheckKeyAccess(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m264))), v_stack_m2D4, 4);
    if (sign_flag) goto loc_007DD4C3;
loc_007DD35E:
    v_stack_m328 = 1;
    result = CmpCheckKeyAccess(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m2C0))), v_stack_m2D4, (uint32_t)(0x10000ULL));
    if (sign_flag) goto loc_007DD4C3;
    result = CmpTryAcquireKcbIXLocks(*(uint64_t *)(arg1 + 0x8), 1, v_stack_m2D4, v_stack_m278);
    if (((uint32_t)(result)) != 0xC000022DULL) goto loc_007DD3ED;
    Arg2 = 0;
    v_stack_m328 = (uint32_t)((uint32_t)(v_stack_m278));
    result = CmpLogTransactionAbortedWithChildName(*(uint64_t *)(arg1 + 0x8), Arg2, Arg2 + 7, v_stack_m278);
    result = CmpUnlockRegistry(*(uint64_t *)(arg1 + 0x8), Arg2, Arg2 + 7, v_stack_m278);
    Arg2 = 0;
    result = CmpAbortRollbackPacket(v_stack_m278, Arg2, Arg2 + 7, v_stack_m278);
    if (sign_flag) goto loc_007DD4BC;
    result = CmpCleanupRollbackPacket(v_stack_m278, Arg2, Arg2 + 7, v_stack_m278);
    v_stack_m278 = v_xmm0;
    result = CmpRetryBackOff(v_stack_m2B0, Arg2, Arg2 + 7, v_stack_m278);
    result = CmpLockRegistryFreezeAware(1, Arg2, Arg2 + 7, v_stack_m278);
    goto loc_007DD2EE;
loc_007DD3ED:
    if (sign_flag) goto loc_007DD4C3;
    v_stack_m328 = 2;
    result = CmpDoAccessCheckOnSubtree(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m2C0))), v_stack_m2D4, (uint32_t)(0x10000ULL));
    if (sign_flag) goto loc_007DD4C3;
    if (((v_stack_m260) & (8)) == 0) goto loc_007DD513;
    Arg2 = 0;
    result = CmpPrepareToInvalidateAllHigherLayerKcbs(*(uint64_t *)(arg1 + 0x8), Arg2, v_stack_m278, (uint32_t)(0x10000ULL));
    result = (uint32_t)((result) + ((uint32_t)((uint32_t)(0x80000000ULL))));
    if ((((uint32_t)((uint32_t)(0x80000000ULL))) & ((uint32_t)(result))) != 0) goto loc_007DD44B;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != 0xC000022DULL) goto loc_007DD4C3;
loc_007DD44B:
    Arg2 = 0;
    result = CmpPrepareForSubtreeInvalidation(*(uint64_t *)(arg1 + 0x8), Arg2, v_stack_m278, (uint32_t)(0x10000ULL));
    if (((uint32_t)(result)) == ((uint32_t)((uint32_t)(0xC000022DULL)))) goto loc_007DD46C;
    if (sign_flag) goto loc_007DD4C3;
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) != ((uint32_t)((uint32_t)(0xC000022DULL)))) goto loc_007DD4CB;
loc_007DD46C:
    Arg2 = 0;
    v_stack_m328 = (uint32_t)((uint32_t)(v_stack_m278));
    result = CmpLogTransactionAbortedWithChildName(*(uint64_t *)(arg1 + 0x8), Arg2, Arg2 + 7, (uint32_t)(0x10000ULL));
    result = CmpUnlockRegistry(*(uint64_t *)(arg1 + 0x8), Arg2, Arg2 + 7, (uint32_t)(0x10000ULL));
    result = 0;
    Arg2 = 0;
    result = CmpAbortRollbackPacket(v_stack_m278, Arg2, Arg2 + 7, (uint32_t)(0x10000ULL));
    if (sign_flag) goto loc_007DD507;
    result = CmpCleanupRollbackPacket(v_stack_m278, Arg2, Arg2 + 7, (uint32_t)(0x10000ULL));
    v_stack_m278 = v_xmm0;
    result = CmpRetryBackOff(v_stack_m2B0, Arg2, Arg2 + 7, (uint32_t)(0x10000ULL));
    goto loc_007DD2E6;
loc_007DD4BC:
    result = CmpLockRegistryFreezeAware(1, Arg2, Arg2 + 7, (uint32_t)(0x10000ULL));
loc_007DD4C3:
    goto loc_007DDAC2;
loc_007DD4CB:
    Arg3 = 0;
    result = CmpInvalidateAllHigherLayerKcbs(*(uint64_t *)(arg1 + 0x8), Arg3 + 1, Arg3, v_stack_m250);
    local_r12 = 0;
    Arg3 = 0;
    v_stack_m328 = 0;
    result = CmpInvalidateSubtree(*(uint64_t *)(arg1 + 0x8), local_r12 + 1, Arg3, v_stack_m250);
    Arg2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m250, Arg2, Arg3, v_stack_m250);
    goto loc_007DD576;
loc_007DD507:
    result = CmpLockRegistryFreezeAware(1, Arg2, Arg3, v_stack_m250);
    goto loc_007DDAC2;
loc_007DD513:
    v_stack_m230 = v_xmm0;
    result = CmpInitializeDelayDerefContext(v_stack_m230, Arg2, Arg3, v_stack_m250);
    v_stack_m318 = 1;
    local_r12 = 0;
    v_stack_m320 = 1;
    v_stack_m328 = 0;
    result = CmpEnumerateAllHigherLayerKcbs(*(uint64_t *)(arg1 + 0x8), v_rip - 858743, v_rip + 81685, v_stack_m230);
    Arg2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m230, Arg2, v_rip + 81685, v_stack_m230);
    result = CmpDoesKeyHaveOpenSubkeys(*(uint64_t *)(arg1 + 0x8), Arg2, v_rip + 81685, v_stack_m230);
    if ((uint8_t)(result) == 0) goto loc_007DD570;
loc_007DD566:
    goto loc_007DD4C3;
loc_007DD570:
    if ((*(uint64_t *)(*(uint64_t *)(arg1 + 0x8))) != 1) goto loc_007DD566;
loc_007DD576:
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m268))), Arg3, Arg4);
    if (sign_flag) goto loc_007DDAC2;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DD5AE;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)(v_stack_m2C0), v_stack_m2A8, Arg4);
    goto loc_007DD5B3;
loc_007DD5AE:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)(v_stack_m2C0), v_stack_m2A8, Arg4);
loc_007DD5B3:
    v_stack_m288 = result;
    if (result != 0) goto loc_007DD5C6;
loc_007DD5BC:
    goto loc_007DDAC2;
loc_007DD5C6:
    if (((*(uint8_t *)(result + 0x2)) & (4)) == 0) goto loc_007DD689;
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0x7FC4B2) + 0x8C)) & (1)) == 0) goto loc_007DD5F2;
    result = HvpGetCellFlat(*(uint64_t *)(v_rip + 0x7FC4B2), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)))), v_stack_m2B8, Arg4);
    goto loc_007DD5F7;
loc_007DD5F2:
    result = HvpGetCellPaged(*(uint64_t *)(v_rip + 0x7FC4B2), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)))), v_stack_m2B8, Arg4);
loc_007DD5F7:
    if (result != 0) goto loc_007DD60B;
loc_007DD601:
    goto loc_007DDAC7;
loc_007DD60B:
    *(uint32_t *)(result + 0x1C) = (uint32_t)((uint32_t)(v_stack_m2D8));
    if (((*(uint8_t *)(*(uint64_t *)(v_rip + 0x7FC476) + 0x8C)) & (1)) == 0) goto loc_007DD62A;
    result = HvpReleaseCellFlat(*(uint64_t *)(v_rip + 0x7FC476), v_stack_m2B8, v_stack_m2B8, Arg4);
    goto loc_007DD62F;
loc_007DD62A:
    result = HvpReleaseCellPaged(*(uint64_t *)(v_rip + 0x7FC476), v_stack_m2B8, v_stack_m2B8, Arg4);
loc_007DD62F:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DD649;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m2D8))), v_stack_m2C8, Arg4);
    goto loc_007DD64E;
loc_007DD649:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m2D8))), v_stack_m2C8, Arg4);
loc_007DD64E:
    if (result == 0) goto loc_007DD601;
    *(uint32_t *)(result + 0x10) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x40) + 0x24) = (uint32_t)((uint32_t)(v_stack_m2D8));
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DD679;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2C8, v_stack_m2C8, Arg4);
    goto loc_007DD67E;
loc_007DD679:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2C8, v_stack_m2C8, Arg4);
loc_007DD67E:
    local_r15 = 0;
    goto loc_007DD908;
loc_007DD689:
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2C8, Arg3, Arg4);
    if (sign_flag) goto loc_007DDAC2;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DD6BB;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), 0, v_stack_m2B8, Arg4);
    goto loc_007DD6C0;
loc_007DD6BB:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), 0, v_stack_m2B8, Arg4);
loc_007DD6C0:
    if (result == 0) goto loc_007DD5BC;
    v_stack_m2A0 = (uint32_t)((uint32_t)(*(uint32_t *)(result + (uint32_t)(v_stack_m2A0) * 4 + 0x1C)));
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DD6ED;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2B8, v_stack_m2B8, Arg4);
    goto loc_007DD6F2;
loc_007DD6ED:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2B8, v_stack_m2B8, Arg4);
loc_007DD6F2:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DD70B;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + (uint32_t)(v_stack_m2A0) * 4 + 0x1C)))), v_stack_m290, Arg4);
    goto loc_007DD710;
loc_007DD70B:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + (uint32_t)(v_stack_m2A0) * 4 + 0x1C)))), v_stack_m290, Arg4);
loc_007DD710:
    v_stack_m258 = result;
    if (result != 0) goto loc_007DD726;
    goto loc_007DD4C3;
loc_007DD726:
    if ((*(uint16_t *)(result)) != ((uint16_t)((uint32_t)(0x6972ULL)))) goto loc_007DD73A;
    goto loc_007DD743;
loc_007DD73A:
loc_007DD743:
    v_stack_m2B0 = 1;
loc_007DD746:
    if (((uint32_t)((uint32_t)(v_stack_m2D8))) >= 1) goto loc_007DD878;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DD76F;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(v_stack_m2A0 + (uint32_t)((uint32_t)((uint32_t)(v_stack_m2D8))) * 4)), v_stack_m2D0, Arg4);
    goto loc_007DD774;
loc_007DD76F:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(v_stack_m2A0 + (uint32_t)((uint32_t)((uint32_t)(v_stack_m2D8))) * 4)), v_stack_m2D0, Arg4);
loc_007DD774:
    result = 0;
    if (0 == 0) goto loc_007DD868;
    Arg4 = 0;
    Arg3 = 0;
    result = HvpMarkCellDirty(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(v_stack_m2A0 + (uint32_t)((uint32_t)((uint32_t)(v_stack_m2D8))) * 4)), Arg3, Arg4);
    Arg2 = 0;
    if (sign_flag) goto loc_007DD83F;
    result = (uint16_t)((*(uint16_t *)(result)) - ((uint16_t)((uint32_t)(0x666CULL))));
    if ((((uint16_t)((uint32_t)(0xFDFFULL))) & ((uint16_t)(result))) == 0) goto loc_007DD7D1;
loc_007DD7C0:
    if (0 >= ((uint32_t)(*(uint16_t *)(result + 0x2)))) goto loc_007DD7E2;
    if ((*(uint32_t *)(result + 0x0 * 4 + 0x4)) == ((uint32_t)((uint32_t)(v_stack_m2C0)))) goto loc_007DD80A;
    result = (uint32_t)((0) + 1);
    goto loc_007DD7C0;
loc_007DD7D1:
    if (((uint32_t)(result)) >= ((uint32_t)(*(uint16_t *)(result + 0x2)))) goto loc_007DD7E2;
    if ((*(uint32_t *)(result + (uint32_t)((uint32_t)(result)) * 8 + 0x4)) == ((uint32_t)((uint32_t)(v_stack_m2C0)))) goto loc_007DD81D;
    result = (uint32_t)((result) + 1);
    goto loc_007DD7D1;
loc_007DD7E2:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DD7FA;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2D0, (uint32_t)(v_stack_m2C0), Arg4);
    goto loc_007DD7FF;
loc_007DD7FA:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2D0, (uint32_t)(v_stack_m2C0), Arg4);
loc_007DD7FF:
    local_r12 = (uint32_t)(((uint32_t)(v_stack_m2D8)) + 1);
    goto loc_007DD746;
loc_007DD80A:
    *(uint32_t *)(result + *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) * 4 + 0x4) = (uint32_t)((uint32_t)(v_stack_m2D8));
    goto loc_007DD827;
loc_007DD816:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2D0, (uint32_t)(v_stack_m2C0), Arg4);
    goto loc_007DD87D;
loc_007DD81D:
    *(uint32_t *)(result + *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) * 8 + 0x4) = (uint32_t)((uint32_t)(v_stack_m2D8));
loc_007DD827:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DD816;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2D0, (uint32_t)(v_stack_m2C0), Arg4);
    goto loc_007DD87D;
loc_007DD83F:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DD857;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2D0, (uint32_t)(v_stack_m2C0), Arg4);
    goto loc_007DD85C;
loc_007DD857:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2D0, (uint32_t)(v_stack_m2C0), Arg4);
loc_007DD85C:
    goto loc_007DDAC2;
loc_007DD868:
    goto loc_007DDAC2;
loc_007DD878:
loc_007DD87D:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DD897;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), 0, v_stack_m2B8, Arg4);
    goto loc_007DD89C;
loc_007DD897:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), 0, v_stack_m2B8, Arg4);
loc_007DD89C:
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DD8B9;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m2D8))), v_stack_m2C8, Arg4);
    goto loc_007DD8BE;
loc_007DD8B9:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m2D8))), v_stack_m2C8, Arg4);
loc_007DD8BE:
    if ((*(uint32_t *)(result + 0x38)) < ((uint32_t)(*(uint16_t *)(result + 0x4A)))) {
        *(uint32_t *)(result + 0x38) = (uint32_t)(*(uint16_t *)(result + 0x4A));
    }
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DD8E1;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2C8, v_stack_m2C8, Arg4);
    goto loc_007DD8E6;
loc_007DD8E1:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2C8, v_stack_m2C8, Arg4);
loc_007DD8E6:
    local_r15 = 0;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DD903;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2B8, v_stack_m2C8, Arg4);
    goto loc_007DD908;
loc_007DD903:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2B8, v_stack_m2C8, Arg4);
loc_007DD908:
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x28) = (uint32_t)((uint32_t)(v_stack_m2D8));
    result = CmpCleanUpKcbCachedSymlink(*(uint64_t *)(arg1 + 0x8), v_stack_m250, v_stack_m2C8, Arg4);
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DD93F;
    result = HvpGetCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x28)), v_stack_m2D0, Arg4);
    goto loc_007DD944;
loc_007DD93F:
    result = HvpGetCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x28)), v_stack_m2D0, Arg4);
loc_007DD944:
    if (result != 0) goto loc_007DD959;
    goto loc_007DDAC7;
loc_007DD959:
    Arg4 = 0;
    Arg3 = 0;
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x64) = (uint32_t)((uint32_t)(*(uint32_t *)(1 + 0x28)));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0x60) = (uint32_t)((uint32_t)(*(uint32_t *)(1 + 0x24)));
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0xBA) = (uint16_t)(*(uint16_t *)(1 + 0x2));
    v_stack_m328 = 0;
    result = CmpAssignSecurityToKcb(*(uint64_t *)(arg1 + 0x8), (uint32_t)(*(uint32_t *)(1 + 0x2C)), Arg3, Arg4);
    result = CmpCleanUpSubKeyInfo(*(uint64_t *)(arg1 + 0x8), 1, Arg3, Arg4);
    *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0xA8) = *(uint64_t *)(1 + 0x4);
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0xB0) = (uint16_t)(*(uint16_t *)(1 + 0x34));
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0xB2) = (uint16_t)(*(uint16_t *)(1 + 0x3C));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0xB4) = (uint32_t)((uint32_t)(*(uint32_t *)(1 + 0x40)));
    Arg1 = (uint32_t)((*(uint16_t *)(1 + 0x36)) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0xB8)))));
    Arg1 = (uint32_t)((Arg1) & (15));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0xB8)))));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0xB8) = (uint32_t)(Arg1);
    result = (uint32_t)((*(uint16_t *)(1 + 0x36)) ^ ((uint32_t)(Arg1)));
    result = (uint32_t)((result) & (240));
    result = (uint32_t)((result) ^ ((uint32_t)(Arg1)));
    *(uint32_t *)(*(uint64_t *)(arg1 + 0x8) + 0xB8) = (uint32_t)(result);
    *(uint8_t *)(*(uint64_t *)(arg1 + 0x8) + 0xB9) = (uint8_t)(*(uint8_t *)(1 + 0x37));
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DDA17;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2D0, Arg3, Arg4);
    goto loc_007DDA1C;
loc_007DDA17:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2D0, Arg3, Arg4);
loc_007DDA1C:
    *(uint16_t *)(*(uint64_t *)(arg1 + 0x8) + 0x8) = 64;
    result = CmpDeleteTree(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m2C0))), Arg3, Arg4);
    if ((uint8_t)(result) != 0) {
        Arg3 = 0;
        Arg2 = (uint32_t)((uint32_t)(v_stack_m2C0));
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20);
        result = CmpFreeKeyByCell(Arg1, Arg2, Arg3, Arg4);
    }
    result = CmpReportNotify(*(uint64_t *)(arg1 + 0x8), Arg2, 1, v_stack_m240);
    if ((*(uint8_t *)(v_rip + 0x7FC008)) == 0) {
        result = *(uint64_t *)(v_rip + 0x7FA5FD);
        *(uint64_t *)(v_rip + 0x7FA756) = result;
        *(uint8_t *)(v_rip + 0x7FBFF1) = 1;
    }
    Arg2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m250, Arg2, 1, v_stack_m240);
    result = CmpUnlockRegistry(v_stack_m250, Arg2, 1, v_stack_m240);
    result = CmpDestroyHive(v_stack_m298, Arg2, 1, v_stack_m240);
    v_stack_m298 = 0;
    result = CmpSignalDeferredPosts(v_stack_m240, Arg2, 1, v_stack_m240);
    goto loc_007DDB0D;
loc_007DDA9C:
    goto loc_007DD4C3;
loc_007DDAA6:
    goto loc_007DD4C3;
loc_007DDAB0:
    goto loc_007DD4C3;
loc_007DDABA:
    v_stack_m288 = v_stack_m280;
loc_007DDAC2:
loc_007DDAC7:
    result = CmpDeleteTree(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), (uint32_t)((uint32_t)((uint32_t)(v_stack_m2D8))), 1, v_stack_m240);
    if ((uint8_t)(result) != 0) {
        Arg3 = 0;
        Arg2 = (uint32_t)((uint32_t)(v_stack_m2D8));
        Arg1 = *(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20);
        result = CmpFreeKeyByCell(Arg1, Arg2, Arg3, v_stack_m240);
    }
    if ((uint8_t)(v_stack_m2D3) == 0) goto loc_007DDB0A;
loc_007DDAEE:
    result = HvUnlockHiveFlusherShared(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), Arg2, Arg3, v_stack_m240);
    if ((uint8_t)(v_stack_m2D3) == 0) goto loc_007DDB0A;
loc_007DDAFB:
    result = CmpUnlockKcb(*(uint64_t *)(arg1 + 0x8), Arg2, Arg3, v_stack_m240);
    goto loc_007DDB0A;
loc_007DDB05:
loc_007DDB0A:
    local_r15 = 0;
loc_007DDB0D:
    Arg2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_m250, Arg2, Arg3, v_stack_m240);
    if (0 != 0) {
        result = CmpUnlockRegistry(v_stack_m250, Arg2, Arg3, v_stack_m240);
    }
    if (v_stack_m298 != 0) {
        result = CmpDestroyHive(v_stack_m298, Arg2, Arg3, v_stack_m240);
        v_stack_m298 = 0;
    }
    if (v_stack_m258 == 0) goto loc_007DDB56;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DDB51;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m290, Arg3, v_stack_m240);
    goto loc_007DDB56;
loc_007DDB51:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m290, Arg3, v_stack_m240);
loc_007DDB56:
    if (0 == 0) goto loc_007DDB77;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DDB72;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2C8, Arg3, v_stack_m240);
    goto loc_007DDB77;
loc_007DDB72:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2C8, Arg3, v_stack_m240);
loc_007DDB77:
    if (v_stack_m288 == 0) goto loc_007DDB99;
    if (((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20) + 0x8C)) & (1)) == 0) goto loc_007DDB94;
    result = HvpReleaseCellFlat(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2A8, Arg3, v_stack_m240);
    goto loc_007DDB99;
loc_007DDB94:
    result = HvpReleaseCellPaged(*(uint64_t *)(*(uint64_t *)(arg1 + 0x8) + 0x20), v_stack_m2A8, Arg3, v_stack_m240);
loc_007DDB99:
    result = CmpCleanupRollbackPacket(v_stack_m278, v_stack_m2A8, Arg3, v_stack_m240);
    result = CmpTraceHiveRestoreStop((uint32_t)((uint32_t)((uint32_t)(0xC000000DULL))), v_stack_m2A8, Arg3, v_stack_m240);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, v_stack_m2A8, Arg3, v_stack_m240);
    local_rsp = (local_rsp) + (784);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007DCF04&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
