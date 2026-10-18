# CmpFlushHive

- RVA: `0x009B3DC0`–`0x009B4918` (길이 `2,904` bytes)
- VA: `0x00000001409B3DC0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x0009E4F4`
- 디코드: `668`개 명령, `2,904/2,904` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **83**; 고유 호출 대상: **40**
- 직접 호출자로 확인된 함수: **15**
- RIP 상대 이미지 참조: **12**

### Outgoing calls
- `0x009B3F1D` → [EtwWriteTransfer](../../text/41/EtwWriteTransfer_function_0041C830.md) (function, `0x0041C830`)
- `0x009B3F2B` → [CmpTraceHiveFlushStart](CmpTraceHiveFlushStart_function_009B49B0.md) (function, `0x009B49B0`)
- `0x009B3F7D` → [CmpLockRegistryFreezeAware](CmpLockRegistryFreezeAware_function_009B4AE4.md) (function, `0x009B4AE4`)
- `0x009B3F85` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (function, `0x00BC9C50`)
- `0x009B3FA5` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (function, `0x00BC9C34`)
- `0x009B3FAA` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x009B3FCE` → [CmpWakeWriteQueueWaiters](../A6/CmpWakeWriteQueueWaiters_function_00A6B0C8.md) (function, `0x00A6B0C8`)
- `0x009B3FE4` → [CmpTraceHiveFlushStop](CmpTraceHiveFlushStop_function_009B4920.md) (function, `0x009B4920`)
- `0x009B4084` → [EtwWriteTransfer](../../text/41/EtwWriteTransfer_function_0041C830.md) (function, `0x0041C830`)
- `0x009B4096` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x009B40DA` → [CmpIsWriteQueueActive](../../text/48/CmpIsWriteQueueActive_function_0048C7D8.md) (function, `0x0048C7D8`)
- `0x009B40F1` → [CmpGenerateFlushControlData](CmpGenerateFlushControlData_function_009B4BCC.md) (function, `0x009B4BCC`)
- `0x009B41BC` → [EtwWriteTransfer](../../text/41/EtwWriteTransfer_function_0041C830.md) (function, `0x0041C830`)
- `0x009B41EA` → [CmpAcquireWriteQueue](../../text/49/CmpAcquireWriteQueue_function_0049E55C.md) (function, `0x0049E55C`)
- `0x009B4222` → [HvStoreModifiedData](HvStoreModifiedData_function_009B4FB4.md) (function, `0x009B4FB4`)
- `0x009B423B` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (function, `0x00BC9C34`)
- `0x009B4240` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x009B426C` → [CmpLogFlushPhaseStart](../A4/CmpLogFlushPhaseStart_function_00A4F450.md) (function, `0x00A4F450`)
- `0x009B4279` → [HvWriteLogFile](HvWriteLogFile_function_009B28E4.md) (function, `0x009B28E4`)
- `0x009B4289` → [CmpLogFlushPhaseEnd](../A4/CmpLogFlushPhaseEnd_function_00A4D268.md) (function, `0x00A4D268`)
- `0x009B429A` → [HvTruncateCurrentLogFileIfRequired](HvTruncateCurrentLogFileIfRequired_function_009B2728.md) (function, `0x009B2728`)
- `0x009B42BE` → [CmpLogFlushPhaseStart](../A4/CmpLogFlushPhaseStart_function_00A4F450.md) (function, `0x00A4F450`)
- `0x009B42DC` → [CmpLogFlushPhaseEnd](../A4/CmpLogFlushPhaseEnd_function_00A4D268.md) (function, `0x00A4D268`)
- `0x009B4336` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x009B433E` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (function, `0x00BC9C50`)
- `0x009B4381` → [CmpArmLazyWriter](../../text/20/CmpArmLazyWriter_function_00204770.md) (function, `0x00204770`)
- `0x009B439C` → [HvFreeUnreconciledData](HvFreeUnreconciledData_function_009B3CCC.md) (function, `0x009B3CCC`)
- `0x009B43C8` → [RtlMergeBitMaps](../../text/43/RtlMergeBitMaps_function_0043DF30.md) (function, `0x0043DF30`)
- `0x009B43D1` → [RtlNumberOfSetBits](../../text/43/RtlNumberOfSetBits_function_00433F70.md) (function, `0x00433F70`)
- `0x009B43DF` → [HvFreeDirtyData](HvFreeDirtyData_function_009B2678.md) (function, `0x009B2678`)
- `0x009B440A` → [CmpReleaseWriteQueue](CmpReleaseWriteQueue_function_009B4EE0.md) (function, `0x009B4EE0`)
- `0x009B441F` → [CmpReleaseWriteQueue](CmpReleaseWriteQueue_function_009B4EE0.md) (function, `0x009B4EE0`)
- `0x009B442A` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (function, `0x00BC9C34`)
- `0x009B442F` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x009B4452` → [CmpWakeWriteQueueWaiters](../A6/CmpWakeWriteQueueWaiters_function_00A6B0C8.md) (function, `0x00A6B0C8`)
- `0x009B446F` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x009B447C` → [HvLockHiveWriter](../85/HvLockHiveWriter_function_00859894.md) (function, `0x00859894`)
- `0x009B448C` → [HvMarkDirtyForFlush](../../text/49/HvMarkDirtyForFlush_function_00494CA4.md) (function, `0x00494CA4`)
- `0x009B44A2` → [HvUnlockHiveWriter](../85/HvUnlockHiveWriter_function_008598E4.md) (function, `0x008598E4`)
- `0x009B44C5` → [CmpIsWriteQueueActive](../../text/48/CmpIsWriteQueueActive_function_0048C7D8.md) (function, `0x0048C7D8`)
- `0x009B44CE` → [CmpAcquireWriteQueue](../../text/49/CmpAcquireWriteQueue_function_0049E55C.md) (function, `0x0049E55C`)
- `0x009B44E4` → [HvFoldBackUnreconciledData](../AC/HvFoldBackUnreconciledData_function_00AC27A8.md) (function, `0x00AC27A8`)
- `0x009B44F5` → [CmpIsWriteQueueActive](../../text/48/CmpIsWriteQueueActive_function_0048C7D8.md) (function, `0x0048C7D8`)
- `0x009B4508` → [CmpWaitOnHiveWriteQueue](../AA/CmpWaitOnHiveWriteQueue_function_00AA0110.md) (function, `0x00AA0110`)
- `0x009B4514` → [CmpLogFlushPhaseStart](../A4/CmpLogFlushPhaseStart_function_00A4F450.md) (function, `0x00A4F450`)
- `0x009B4523` → [HvExtendHivePrimaryFileValidDataLength](../AD/HvExtendHivePrimaryFileValidDataLength_function_00AD49C0.md) (function, `0x00AD49C0`)
- `0x009B4530` → [CmpLogFlushPhaseEnd](../A4/CmpLogFlushPhaseEnd_function_00A4D268.md) (function, `0x00A4D268`)
- `0x009B4550` → [CmpLogFlushPhaseStart](../A4/CmpLogFlushPhaseStart_function_00A4F450.md) (function, `0x00A4F450`)
- `0x009B4560` → [HvValidateOrInvalidatePrimaryFileHeader](HvValidateOrInvalidatePrimaryFileHeader_function_009B27A8.md) (function, `0x009B27A8`)
- `0x009B4570` → [CmpLogFlushPhaseEnd](../A4/CmpLogFlushPhaseEnd_function_00A4D268.md) (function, `0x00A4D268`)
- `0x009B4588` → [HvTruncateAllLogFilesIfRequired](HvTruncateAllLogFilesIfRequired_function_009B6E1C.md) (function, `0x009B6E1C`)
- `0x009B4594` → [CmpLogFlushPhaseStart](../A4/CmpLogFlushPhaseStart_function_00A4F450.md) (function, `0x00A4F450`)
- `0x009B45A1` → [HvWriteHivePrimaryFile](HvWriteHivePrimaryFile_function_009B2374.md) (function, `0x009B2374`)
- `0x009B45B1` → [CmpLogFlushPhaseEnd](../A4/CmpLogFlushPhaseEnd_function_00A4D268.md) (function, `0x00A4D268`)
- `0x009B45DE` → [CmpLogFlushPhaseStart](../A4/CmpLogFlushPhaseStart_function_00A4F450.md) (function, `0x00A4F450`)
- `0x009B45E8` → [CmpFileFlushAndPurge](CmpFileFlushAndPurge_function_009B2BAC.md) (function, `0x009B2BAC`)
- `0x009B460E` → [CmpLogFlushPhaseEnd](../A4/CmpLogFlushPhaseEnd_function_00A4D268.md) (function, `0x00A4D268`)
- `0x009B4623` → [HvUnCOWReconciledPages](../../text/43/HvUnCOWReconciledPages_function_0043DC20.md) (function, `0x0043DC20`)
- `0x009B462B` → [HvFreeUnreconciledData](HvFreeUnreconciledData_function_009B3CCC.md) (function, `0x009B3CCC`)
- `0x009B4646` → [HvResetLogFileStatusAll](../A9/HvResetLogFileStatusAll_function_00A9EB5C.md) (function, `0x00A9EB5C`)
- `0x009B4652` → [HvIsCurrentLogSwappable](../A8/HvIsCurrentLogSwappable_function_00A875D8.md) (function, `0x00A875D8`)
- `0x009B4661` → [HvSwapLogFiles](HvSwapLogFiles_function_009B1EF8.md) (function, `0x009B1EF8`)
- `0x009B466D` → [CmpLogFlushPhaseStart](../A4/CmpLogFlushPhaseStart_function_00A4F450.md) (function, `0x00A4F450`)
- `0x009B467D` → [HvValidateOrInvalidatePrimaryFileHeader](HvValidateOrInvalidatePrimaryFileHeader_function_009B27A8.md) (function, `0x009B27A8`)
- `0x009B468D` → [CmpLogFlushPhaseEnd](../A4/CmpLogFlushPhaseEnd_function_00A4D268.md) (function, `0x00A4D268`)
- `0x009B46B5` → [RtlMergeBitMaps](../../text/43/RtlMergeBitMaps_function_0043DF30.md) (function, `0x0043DF30`)
- `0x009B46BD` → [HvFreeDirtyData](HvFreeDirtyData_function_009B2678.md) (function, `0x009B2678`)
- `0x009B46F6` → [HvSwapLogFiles](HvSwapLogFiles_function_009B1EF8.md) (function, `0x009B1EF8`)
- `0x009B4746` → [CmpArmLazyWriter](../../text/20/CmpArmLazyWriter_function_00204770.md) (function, `0x00204770`)
- `0x009B476F` → [HvpLogTypeToLogArrayIndex](HvpLogTypeToLogArrayIndex_function_009B2DFC.md) (function, `0x009B2DFC`)
- `0x009B478A` → [CmpIsWriteQueueActive](../../text/48/CmpIsWriteQueueActive_function_0048C7D8.md) (function, `0x0048C7D8`)
- `0x009B4796` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (function, `0x00BC9C34`)
- `0x009B479B` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x009B47AF` → [CmpIsWriteQueueActive](../../text/48/CmpIsWriteQueueActive_function_0048C7D8.md) (function, `0x0048C7D8`)
- `0x009B47C6` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x009B47CE` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (function, `0x00BC9C50`)
- `0x009B47DA` → [CmpReleaseWriteQueue](CmpReleaseWriteQueue_function_009B4EE0.md) (function, `0x009B4EE0`)
- `0x009B47F7` → [CmpWakeWriteQueueWaiters](../A6/CmpWakeWriteQueueWaiters_function_00A6B0C8.md) (function, `0x00A6B0C8`)
- `0x009B4806` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (function, `0x00BC9C34`)
- `0x009B480B` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x009B482B` → [CmpWaitOnHiveWriteQueue](../AA/CmpWaitOnHiveWriteQueue_function_00AA0110.md) (function, `0x00AA0110`)
- `0x009B4852` → [HvUnlockHiveWriter](../85/HvUnlockHiveWriter_function_008598E4.md) (function, `0x008598E4`)
- `0x009B4874` → [HvFoldBackDirtyData](../A4/HvFoldBackDirtyData_function_00A463B8.md) (function, `0x00A463B8`)

### Direct callers
- [CmpDoFlushAll](../../text/34/CmpDoFlushAll_function_00349A9C.md) at `0x00349AEF`
- [CmpLoadKeyCommon](../../text/46/CmpLoadKeyCommon_function_0046E9F8.md) at `0x0046EDDD`
- [CmShutdownSystem1](../../text/66/CmShutdownSystem1_function_0066A5B0.md) at `0x0066A7A6`
- [CmpFinishSystemHivesLoad](../7D/CmpFinishSystemHivesLoad_function_007DA210.md) at `0x007DA5A8`
- [CmpLoadHiveThread](../7D/CmpLoadHiveThread_function_007DB040.md) at `0x007DB9D3`
- [CmpMountPreloadedHives](../7D/CmpMountPreloadedHives_function_007DBE18.md) at `0x007DC3CA`
- [CmFreezeRegistry](../7E/CmFreezeRegistry_function_007E834C.md) at `0x007E84C6`
- [CmReplaceKey](../7E/CmReplaceKey_function_007EA1C8.md) at `0x007EA304`
- [CmpDoFlushNextHive](../84/CmpDoFlushNextHive_function_0084C7C0.md) at `0x0084C844`
- [CmpDoFlushNextHive](../84/CmpDoFlushNextHive_function_0084C7C0.md) at `0x0084C914`
- [CmpInitHiveFromFile](../87/CmpInitHiveFromFile_function_008794D4.md) at `0x008799EB`
- [CmpTransMgrSyncHive](CmpTransMgrSyncHive_function_009B07C4.md) at `0x009B07FF`
- [CmpCompleteUnloadKey](CmpCompleteUnloadKey_function_009B32FC.md) at `0x009B3478`
- [CmpDoReconcileNextHive](CmpDoReconcileNextHive_function_009B6BE0.md) at `0x009B6D0D`
- [NtFlushKey](../A8/NtFlushKey_function_00A8A030.md) at `0x00A8A1C9`
- [sub_00B2DB96](../B2/Unknown_function_00B2DB96.md) at `0x00B2DBB2`

### Static image references
- `0x009B3DE6` → RVA `0x00E0A740` (`.data`; read)
- `0x009B3E13` → RVA `0x00E09F58` (`.data`; read)
- `0x009B3E1A` → RVA `0x0005BCFD` (`.rdata`; read)
- `0x009B3E2B` → RVA `0x00043590` (`.rdata`; read)
- `0x009B3E7F` → RVA `0x000561D8` (`.rdata`; read)
- `0x009B3E8A` → RVA `0x00E09F60` (`.data`; read)
- `0x009B3ED7` → RVA `0x000561E2` (`.rdata`; read)
- `0x009B3F05` → RVA `0x00E09F78` (`.data`; read)
- `0x009B400F` → RVA `0x0005625A` (`.rdata`; read)
- `0x009B4043` → RVA `0x00056264` (`.rdata`; read)
- `0x009B4143` → RVA `0x0005620F` (`.rdata`; read)
- `0x009B4173` → RVA `0x00056219` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **34**
  - `0x009B3F1D` → [EtwWriteTransfer](../../text/41/EtwWriteTransfer_function_0041C830.md) (`PAGE` → `.text`)
  - `0x009B3F85` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (`PAGE` → `PAGECMRC`)
  - `0x009B3FA5` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (`PAGE` → `PAGECMRC`)
  - `0x009B3FAA` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x009B4084` → [EtwWriteTransfer](../../text/41/EtwWriteTransfer_function_0041C830.md) (`PAGE` → `.text`)
  - `0x009B4096` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x009B40DA` → [CmpIsWriteQueueActive](../../text/48/CmpIsWriteQueueActive_function_0048C7D8.md) (`PAGE` → `.text`)
  - `0x009B41BC` → [EtwWriteTransfer](../../text/41/EtwWriteTransfer_function_0041C830.md) (`PAGE` → `.text`)
  - `0x009B41EA` → [CmpAcquireWriteQueue](../../text/49/CmpAcquireWriteQueue_function_0049E55C.md) (`PAGE` → `.text`)
  - `0x009B423B` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (`PAGE` → `PAGECMRC`)
  - `0x009B4240` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x009B4336` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x009B433E` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (`PAGE` → `PAGECMRC`)
  - `0x009B4381` → [CmpArmLazyWriter](../../text/20/CmpArmLazyWriter_function_00204770.md) (`PAGE` → `.text`)
  - `0x009B43C8` → [RtlMergeBitMaps](../../text/43/RtlMergeBitMaps_function_0043DF30.md) (`PAGE` → `.text`)
  - `0x009B43D1` → [RtlNumberOfSetBits](../../text/43/RtlNumberOfSetBits_function_00433F70.md) (`PAGE` → `.text`)
  - `0x009B442A` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (`PAGE` → `PAGECMRC`)
  - `0x009B442F` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x009B446F` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x009B448C` → [HvMarkDirtyForFlush](../../text/49/HvMarkDirtyForFlush_function_00494CA4.md) (`PAGE` → `.text`)
  - `0x009B44C5` → [CmpIsWriteQueueActive](../../text/48/CmpIsWriteQueueActive_function_0048C7D8.md) (`PAGE` → `.text`)
  - `0x009B44CE` → [CmpAcquireWriteQueue](../../text/49/CmpAcquireWriteQueue_function_0049E55C.md) (`PAGE` → `.text`)
  - `0x009B44F5` → [CmpIsWriteQueueActive](../../text/48/CmpIsWriteQueueActive_function_0048C7D8.md) (`PAGE` → `.text`)
  - `0x009B4623` → [HvUnCOWReconciledPages](../../text/43/HvUnCOWReconciledPages_function_0043DC20.md) (`PAGE` → `.text`)
  - `0x009B46B5` → [RtlMergeBitMaps](../../text/43/RtlMergeBitMaps_function_0043DF30.md) (`PAGE` → `.text`)
  - `0x009B4746` → [CmpArmLazyWriter](../../text/20/CmpArmLazyWriter_function_00204770.md) (`PAGE` → `.text`)
  - `0x009B478A` → [CmpIsWriteQueueActive](../../text/48/CmpIsWriteQueueActive_function_0048C7D8.md) (`PAGE` → `.text`)
  - `0x009B4796` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (`PAGE` → `PAGECMRC`)
  - `0x009B479B` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x009B47AF` → [CmpIsWriteQueueActive](../../text/48/CmpIsWriteQueueActive_function_0048C7D8.md) (`PAGE` → `.text`)
  - `0x009B47C6` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x009B47CE` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (`PAGE` → `PAGECMRC`)
  - `0x009B4806` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (`PAGE` → `PAGECMRC`)
  - `0x009B480B` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x009B48B1` → [sub_00B2DCD0](../B2/Unknown_function_00B2DCD0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
009B3DC0  48 8B C4                        mov rax, rsp
009B3DC3  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
009B3DC7  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
009B3DCB  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
009B3DCF  55                              push rbp
009B3DD0  41 54                           push r12
009B3DD2  41 55                           push r13
009B3DD4  41 56                           push r14
009B3DD6  41 57                           push r15
009B3DD8  48 8D A8 48 FF FF FF            lea rbp, [rax - 0xb8]
009B3DDF  48 81 EC 90 01 00 00            sub rsp, 0x190
009B3DE6  48 8B 05 53 69 45 00            mov rax, qword ptr [rip + 0x456953]
009B3DED  48 33 C4                        xor rax, rsp
009B3DF0  48 89 85 80 00 00 00            mov qword ptr [rbp + 0x80], rax
009B3DF7  33 C0                           xor eax, eax
009B3DF9  48 8D 99 40 07 00 00            lea rbx, [rcx + 0x740]
009B3E00  21 44 24 50                     and dword ptr [rsp + 0x50], eax
009B3E04  48 8D B1 30 07 00 00            lea rsi, [rcx + 0x730]
009B3E0B  45 33 FF                        xor r15d, r15d
009B3E0E  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
009B3E13  83 3D 3E 61 45 00 04            cmp dword ptr [rip + 0x45613e], 4
009B3E1A  4C 8D 25 DC 7E 6A FF            lea r12, [rip - 0x958124]
009B3E21  0F 57 C0                        xorps xmm0, xmm0
009B3E24  89 44 24 48                     mov dword ptr [rsp + 0x48], eax
009B3E28  44 8B F2                        mov r14d, edx
009B3E2B  4C 8D 2D 5E F7 68 FF            lea r13, [rip - 0x9708a2]
009B3E32  48 8B F9                        mov rdi, rcx
009B3E35  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
009B3E3A  0F 86 E2 00 00 00               jbe 0x1409b3f22
009B3E40  0F B7 0B                        movzx ecx, word ptr [rbx]
009B3E43  48 8D 55 D8                     lea rdx, [rbp - 0x28]
009B3E47  48 8B 43 08                     mov rax, qword ptr [rbx + 8]
009B3E4B  45 33 C9                        xor r9d, r9d
009B3E4E  44 21 7D CC                     and dword ptr [rbp - 0x34], r15d
009B3E52  45 33 C0                        xor r8d, r8d
009B3E55  44 21 7D DC                     and dword ptr [rbp - 0x24], r15d
009B3E59  44 21 7D EC                     and dword ptr [rbp - 0x14], r15d
009B3E5D  44 21 7D FC                     and dword ptr [rbp - 4], r15d
009B3E61  44 21 7D 0C                     and dword ptr [rbp + 0xc], r15d
009B3E65  4C 21 7C 24 78                  and qword ptr [rsp + 0x78], r15
009B3E6A  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
009B3E6E  48 8B 46 08                     mov rax, qword ptr [rsi + 8]
009B3E72  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
009B3E76  48 8D 44 24 64                  lea rax, [rsp + 0x64]
009B3E7B  48 89 45 00                     mov qword ptr [rbp], rax
009B3E7F  0F B7 05 52 23 6A FF            movzx eax, word ptr [rip - 0x95dcae]
009B3E86  89 44 24 74                     mov dword ptr [rsp + 0x74], eax
009B3E8A  48 8B 05 CF 60 45 00            mov rax, qword ptr [rip + 0x4560cf]
009B3E91  48 89 45 A0                     mov qword ptr [rbp - 0x60], rax
009B3E95  48 89 55 C0                     mov qword ptr [rbp - 0x40], rdx
009B3E99  48 8D 55 F8                     lea rdx, [rbp - 8]
009B3E9D  89 4D D8                        mov dword ptr [rbp - 0x28], ecx
009B3EA0  0F B7 0E                        movzx ecx, word ptr [rsi]
009B3EA3  48 89 55 E0                     mov qword ptr [rbp - 0x20], rdx
009B3EA7  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
009B3EAC  89 4D F8                        mov dword ptr [rbp - 8], ecx
009B3EAF  C7 45 C8 02 00 00 00            mov dword ptr [rbp - 0x38], 2
009B3EB6  C7 45 E8 02 00 00 00            mov dword ptr [rbp - 0x18], 2
009B3EBD  44 89 74 24 64                  mov dword ptr [rsp + 0x64], r14d
009B3EC2  C7 45 08 04 00 00 00            mov dword ptr [rbp + 8], 4
009B3EC9  C7 44 24 70 00 00 00 0B         mov dword ptr [rsp + 0x70], 0xb000000
009B3ED1  0F B7 00                        movzx eax, word ptr [rax]
009B3ED4  89 45 A8                        mov dword ptr [rbp - 0x58], eax
009B3ED7  48 8D 05 04 23 6A FF            lea rax, [rip - 0x95dcfc]
009B3EDE  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
009B3EE2  49 8B C4                        mov rax, r12
009B3EE5  41 2B C5                        sub eax, r13d
009B3EE8  C7 45 AC 02 00 00 00            mov dword ptr [rbp - 0x54], 2
009B3EEF  C7 45 B8 2B 00 00 00            mov dword ptr [rbp - 0x48], 0x2b
009B3EF6  C7 45 BC 01 00 00 00            mov dword ptr [rbp - 0x44], 1
009B3EFD  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
009B3F01  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
009B3F05  48 8B 0D 6C 60 45 00            mov rcx, qword ptr [rip + 0x45606c]
009B3F0C  48 8D 45 A0                     lea rax, [rbp - 0x60]
009B3F10  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009B3F15  C7 44 24 20 07 00 00 00         mov dword ptr [rsp + 0x20], 7
009B3F1D  E8 0E 89 A6 FF                  call 0x14041c830
009B3F22  45 8B C6                        mov r8d, r14d
009B3F25  48 8B D3                        mov rdx, rbx
009B3F28  48 8B CE                        mov rcx, rsi
009B3F2B  E8 80 0A 00 00                  call 0x1409b49b0
009B3F30  F7 87 A0 00 00 00 01 80 00 00   test dword ptr [rdi + 0xa0], 0x8001
009B3F3A  0F 85 A1 00 00 00               jne 0x1409b3fe1
009B3F40  4C 39 BF 08 06 00 00            cmp qword ptr [rdi + 0x608], r15
009B3F47  0F 84 17 05 00 00               je 0x1409b4464
009B3F4D  41 8B DE                        mov ebx, r14d
009B3F50  83 CB 0C                        or ebx, 0xc
009B3F53  F6 87 A0 00 00 00 02            test byte ptr [rdi + 0xa0], 2
009B3F5A  41 0F 44 DE                     cmove ebx, r14d
009B3F5E  44 8B EB                        mov r13d, ebx
009B3F61  41 C1 ED 04                     shr r13d, 4
009B3F65  41 83 E5 01                     and r13d, 1
009B3F69  45 33 E4                        xor r12d, r12d
009B3F6C  41 83 FC 02                     cmp r12d, 2
009B3F70  73 61                           jae 0x1409b3fd3
009B3F72  F6 C3 01                        test bl, 1
009B3F75  0F 85 F4 04 00 00               jne 0x1409b446f
009B3F7B  33 C9                           xor ecx, ecx
009B3F7D  E8 62 0B 00 00                  call 0x1409b4ae4
009B3F82  48 8B CF                        mov rcx, rdi
009B3F85  E8 C6 5C 21 00                  call 0x140bc9c50
009B3F8A  F6 87 A4 00 00 00 04            test byte ptr [rdi + 0xa4], 4
009B3F91  0F 95 C1                        setne cl
009B3F94  F6 C3 40                        test bl, 0x40
009B3F97  0F 94 C0                        sete al
009B3F9A  84 C8                           test al, cl
009B3F9C  0F 84 1B 01 00 00               je 0x1409b40bd
009B3FA2  48 8B CF                        mov rcx, rdi
009B3FA5  E8 8A 5C 21 00                  call 0x140bc9c34
009B3FAA  E8 D5 5A 21 00                  call 0x140bc9a84
009B3FAF  41 BF 89 01 00 C0               mov r15d, 0xc0000189
009B3FB5  EB 1C                           jmp 0x1409b3fd3
009B3FB7  48 8D 8F 70 10 00 00            lea rcx, [rdi + 0x1070]
009B3FBE  49 8B D5                        mov rdx, r13
009B3FC1  41 F6 C6 40                     test r14b, 0x40
009B3FC5  0F 84 4D 06 00 00               je 0x1409b4618
009B3FCB  45 8B C7                        mov r8d, r15d
009B3FCE  E8 F5 70 0B 00                  call 0x140a6b0c8
009B3FD3  4C 8D 25 23 7D 6A FF            lea r12, [rip - 0x9582dd]
009B3FDA  4C 8D 2D AF F5 68 FF            lea r13, [rip - 0x970a51]
009B3FE1  41 8B CF                        mov ecx, r15d
009B3FE4  E8 37 09 00 00                  call 0x1409b4920
009B3FE9  83 3D 68 5F 45 00 04            cmp dword ptr [rip + 0x455f68], 4
009B3FF0  0F 86 93 00 00 00               jbe 0x1409b4089
009B3FF6  83 65 3C 00                     and dword ptr [rbp + 0x3c], 0
009B3FFA  48 8D 44 24 50                  lea rax, [rsp + 0x50]
009B3FFF  48 83 65 98 00                  and qword ptr [rbp - 0x68], 0
009B4004  48 8D 55 90                     lea rdx, [rbp - 0x70]
009B4008  48 89 45 30                     mov qword ptr [rbp + 0x30], rax
009B400C  45 2B E5                        sub r12d, r13d
009B400F  0F B7 05 44 22 6A FF            movzx eax, word ptr [rip - 0x95ddbc]
009B4016  45 33 C9                        xor r9d, r9d
009B4019  89 45 94                        mov dword ptr [rbp - 0x6c], eax
009B401C  45 33 C0                        xor r8d, r8d
009B401F  48 8B 05 3A 5F 45 00            mov rax, qword ptr [rip + 0x455f3a]
009B4026  48 89 45 10                     mov qword ptr [rbp + 0x10], rax
009B402A  44 89 7C 24 50                  mov dword ptr [rsp + 0x50], r15d
009B402F  C7 45 38 04 00 00 00            mov dword ptr [rbp + 0x38], 4
009B4036  C7 45 90 00 00 00 0B            mov dword ptr [rbp - 0x70], 0xb000000
009B403D  0F B7 00                        movzx eax, word ptr [rax]
009B4040  89 45 18                        mov dword ptr [rbp + 0x18], eax
009B4043  48 8D 05 1A 22 6A FF            lea rax, [rip - 0x95dde6]
009B404A  48 89 45 20                     mov qword ptr [rbp + 0x20], rax
009B404E  C7 45 1C 02 00 00 00            mov dword ptr [rbp + 0x1c], 2
009B4055  C7 45 28 17 00 00 00            mov dword ptr [rbp + 0x28], 0x17
009B405C  C7 45 2C 01 00 00 00            mov dword ptr [rbp + 0x2c], 1
009B4063  44 89 64 24 60                  mov dword ptr [rsp + 0x60], r12d
009B4068  8B 44 24 60                     mov eax, dword ptr [rsp + 0x60]
009B406C  48 8B 0D 05 5F 45 00            mov rcx, qword ptr [rip + 0x455f05]
009B4073  48 8D 45 10                     lea rax, [rbp + 0x10]
009B4077  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009B407C  C7 44 24 20 03 00 00 00         mov dword ptr [rsp + 0x20], 3
009B4084  E8 A7 87 A6 FF                  call 0x14041c830
009B4089  41 8B C7                        mov eax, r15d
009B408C  48 8B 8D 80 00 00 00            mov rcx, qword ptr [rbp + 0x80]
009B4093  48 33 CC                        xor rcx, rsp
009B4096  E8 A5 85 CF FF                  call 0x1406ac640
009B409B  4C 8D 9C 24 90 01 00 00         lea r11, [rsp + 0x190]
009B40A3  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
009B40A7  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
009B40AB  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
009B40AF  49 8B E3                        mov rsp, r11
009B40B2  41 5F                           pop r15
009B40B4  41 5E                           pop r14
009B40B6  41 5D                           pop r13
009B40B8  41 5C                           pop r12
009B40BA  5D                              pop rbp
009B40BB  C3                              ret
009B40BC  CC                              int3
009B40BD  F6 C3 02                        test bl, 2
009B40C0  0F 85 BD 06 00 00               jne 0x1409b4783
009B40C6  44 8B C3                        mov r8d, ebx
009B40C9  41 83 E0 04                     and r8d, 4
009B40CD  0F 85 1B 04 00 00               jne 0x1409b44ee
009B40D3  48 8D 8F 60 10 00 00            lea rcx, [rdi + 0x1060]
009B40DA  E8 F9 86 AD FF                  call 0x14048c7d8
009B40DF  84 C0                           test al, al
009B40E1  0F 85 2E 07 00 00               jne 0x1409b4815
009B40E7  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
009B40EC  8B D3                           mov edx, ebx
009B40EE  48 8B CF                        mov rcx, rdi
009B40F1  E8 D6 0A 00 00                  call 0x1409b4bcc
009B40F6  83 3D 5B 5E 45 00 04            cmp dword ptr [rip + 0x455e5b], 4
009B40FD  0F 86 BE 00 00 00               jbe 0x1409b41c1
009B4103  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
009B4107  48 8D 0D 82 F4 68 FF            lea rcx, [rip - 0x970b7e]
009B410E  83 65 6C 00                     and dword ptr [rbp + 0x6c], 0
009B4112  48 8D 55 80                     lea rdx, [rbp - 0x80]
009B4116  83 65 7C 00                     and dword ptr [rbp + 0x7c], 0
009B411A  45 33 C9                        xor r9d, r9d
009B411D  48 83 65 88 00                  and qword ptr [rbp - 0x78], 0
009B4122  45 33 C0                        xor r8d, r8d
009B4125  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
009B4129  48 8D 44 24 68                  lea rax, [rsp + 0x68]
009B412E  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
009B4132  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
009B4136  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
009B413A  48 8D 44 24 60                  lea rax, [rsp + 0x60]
009B413F  48 89 45 70                     mov qword ptr [rbp + 0x70], rax
009B4143  0F B7 05 C5 20 6A FF            movzx eax, word ptr [rip - 0x95df3b]
009B414A  89 45 84                        mov dword ptr [rbp - 0x7c], eax
009B414D  48 8B 05 0C 5E 45 00            mov rax, qword ptr [rip + 0x455e0c]
009B4154  48 89 45 40                     mov qword ptr [rbp + 0x40], rax
009B4158  C7 45 68 04 00 00 00            mov dword ptr [rbp + 0x68], 4
009B415F  C7 45 78 04 00 00 00            mov dword ptr [rbp + 0x78], 4
009B4166  C7 45 80 00 00 00 0B            mov dword ptr [rbp - 0x80], 0xb000000
009B416D  0F B7 00                        movzx eax, word ptr [rax]
009B4170  89 45 48                        mov dword ptr [rbp + 0x48], eax
009B4173  48 8D 05 9F 20 6A FF            lea rax, [rip - 0x95df61]
009B417A  48 89 45 50                     mov qword ptr [rbp + 0x50], rax
009B417E  48 8D 05 78 7B 6A FF            lea rax, [rip - 0x958488]
009B4185  2B C1                           sub eax, ecx
009B4187  C7 45 4C 02 00 00 00            mov dword ptr [rbp + 0x4c], 2
009B418E  C7 45 58 3F 00 00 00            mov dword ptr [rbp + 0x58], 0x3f
009B4195  C7 45 5C 01 00 00 00            mov dword ptr [rbp + 0x5c], 1
009B419C  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
009B41A0  8B 44 24 58                     mov eax, dword ptr [rsp + 0x58]
009B41A4  48 8B 0D CD 5D 45 00            mov rcx, qword ptr [rip + 0x455dcd]
009B41AB  48 8D 45 40                     lea rax, [rbp + 0x40]
009B41AF  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
009B41B4  C7 44 24 20 04 00 00 00         mov dword ptr [rsp + 0x20], 4
009B41BC  E8 6F 86 A6 FF                  call 0x14041c830
009B41C1  44 8B 74 24 30                  mov r14d, dword ptr [rsp + 0x30]
009B41C6  41 F7 C6 58 03 00 00            test r14d, 0x358
009B41CD  0F 84 C0 05 00 00               je 0x1409b4793
009B41D3  41 F6 C6 02                     test r14b, 2
009B41D7  0F 85 E1 02 00 00               jne 0x1409b44be
009B41DD  41 F6 C6 01                     test r14b, 1
009B41E1  74 0C                           je 0x1409b41ef
009B41E3  48 8D 8F 60 10 00 00            lea rcx, [rdi + 0x1060]
009B41EA  E8 6D A3 AE FF                  call 0x14049e55c
009B41EF  41 F7 C6 10 01 00 00            test r14d, 0x110
009B41F6  41 8B DE                        mov ebx, r14d
009B41F9  40 0F 95 C6                     setne sil
009B41FD  C1 EB 06                        shr ebx, 6
009B4200  83 E3 01                        and ebx, 1
009B4203  41 F6 C6 08                     test r14b, 8
009B4207  0F 85 6C 02 00 00               jne 0x1409b4479
009B420D  45 33 E4                        xor r12d, r12d
009B4210  41 F7 C6 58 01 00 00            test r14d, 0x158
009B4217  74 16                           je 0x1409b422f
009B4219  44 8A C3                        mov r8b, bl
009B421C  40 8A D6                        mov dl, sil
009B421F  48 8B CF                        mov rcx, rdi
009B4222  E8 8D 0D 00 00                  call 0x1409b4fb4
009B4227  85 C0                           test eax, eax
009B4229  0F 85 9F 04 00 00               jne 0x1409b46ce
009B422F  45 84 F6                        test r14b, r14b
009B4232  0F 88 6B 06 00 00               js 0x1409b48a3
009B4238  48 8B CF                        mov rcx, rdi
009B423B  E8 F4 59 21 00                  call 0x140bc9c34
009B4240  E8 3F 58 21 00                  call 0x140bc9a84
009B4245  BB 01 00 00 00                  mov ebx, 1
009B424A  89 5C 24 3C                     mov dword ptr [rsp + 0x3c], ebx
009B424E  45 84 F6                        test r14b, r14b
009B4251  0F 88 BB 02 00 00               js 0x1409b4512
009B4257  8B 74 24 34                     mov esi, dword ptr [rsp + 0x34]
009B425B  B8 02 00 00 00                  mov eax, 2
009B4260  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
009B4264  41 F6 C6 08                     test r14b, 8
009B4268  74 3C                           je 0x1409b42a6
009B426A  8B D0                           mov edx, eax
009B426C  E8 DF B1 09 00                  call 0x140a4f450
009B4271  4C 8D 4C 24 50                  lea r9, [rsp + 0x50]
009B4276  48 8B CF                        mov rcx, rdi
009B4279  E8 66 E6 FF FF                  call 0x1409b28e4
009B427E  44 8B C0                        mov r8d, eax
009B4281  BA 02 00 00 00                  mov edx, 2
009B4286  44 8B F8                        mov r15d, eax
009B4289  E8 DA 8F 09 00                  call 0x140a4d268
009B428E  45 85 FF                        test r15d, r15d
009B4291  0F 88 9F 00 00 00               js 0x1409b4336
009B4297  48 8B CF                        mov rcx, rdi
009B429A  E8 89 E4 FF FF                  call 0x1409b2728
009B429F  83 CE 02                        or esi, 2
009B42A2  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
009B42A6  B8 03 00 00 00                  mov eax, 3
009B42AB  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
009B42AF  41 F6 C6 10                     test r14b, 0x10
009B42B3  0F 85 B2 03 00 00               jne 0x1409b466b
009B42B9  BA 04 00 00 00                  mov edx, 4
009B42BE  E8 8D B1 09 00                  call 0x140a4f450
009B42C3  41 8B C6                        mov eax, r14d
009B42C6  25 48 04 00 00                  and eax, 0x448
009B42CB  83 F8 48                        cmp eax, 0x48
009B42CE  0F 84 D3 03 00 00               je 0x1409b46a7
009B42D4  45 8B C7                        mov r8d, r15d
009B42D7  BA 04 00 00 00                  mov edx, 4
009B42DC  E8 87 8F 09 00                  call 0x140a4d268
009B42E1  41 F6 C6 20                     test r14b, 0x20
009B42E5  0F 85 FF 03 00 00               jne 0x1409b46ea
009B42EB  41 8B C6                        mov eax, r14d
009B42EE  83 E0 45                        and eax, 0x45
009B42F1  3C 41                           cmp al, 0x41
009B42F3  0F 84 CD 04 00 00               je 0x1409b47c6
009B42F9  B8 05 00 00 00                  mov eax, 5
009B42FE  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
009B4302  41 F6 C6 40                     test r14b, 0x40
009B4306  0F 85 86 02 00 00               jne 0x1409b4592
009B430C  B8 06 00 00 00                  mov eax, 6
009B4311  89 44 24 3C                     mov dword ptr [rsp + 0x3c], eax
009B4315  41 0F BA E6 08                  bt r14d, 8
009B431A  0F 82 2E 02 00 00               jb 0x1409b454e
009B4320  41 0F BA E6 09                  bt r14d, 9
009B4325  0F 82 A0 02 00 00               jb 0x1409b45cb
009B432B  45 8B FC                        mov r15d, r12d
009B432E  C7 44 24 3C 08 00 00 00         mov dword ptr [rsp + 0x3c], 8
009B4336  E8 F9 57 21 00                  call 0x140bc9b34
009B433B  48 8B CF                        mov rcx, rdi
009B433E  E8 0D 59 21 00                  call 0x140bc9c50
009B4343  45 85 FF                        test r15d, r15d
009B4346  0F 88 7A 05 00 00               js 0x1409b48c6
009B434C  40 F6 C6 20                     test sil, 0x20
009B4350  74 0D                           je 0x1409b435f
009B4352  09 9F 80 10 00 00               or dword ptr [rdi + 0x1080], ebx
009B4358  44 89 A7 84 10 00 00            mov dword ptr [rdi + 0x1084], r12d
009B435F  45 85 FF                        test r15d, r15d
009B4362  0F 88 7F 05 00 00               js 0x1409b48e7
009B4368  41 0F BA E6 0B                  bt r14d, 0xb
009B436D  0F 82 94 03 00 00               jb 0x1409b4707
009B4373  41 0F BA E6 0C                  bt r14d, 0xc
009B4378  73 0C                           jae 0x1409b4386
009B437A  44 8A C3                        mov r8b, bl
009B437D  33 D2                           xor edx, edx
009B437F  8B CB                           mov ecx, ebx
009B4381  E8 EA 03 85 FF                  call 0x140204770
009B4386  41 F6 C6 40                     test r14b, 0x40
009B438A  0F 85 48 01 00 00               jne 0x1409b44d8
009B4390  41 F7 C6 10 01 00 00            test r14d, 0x110
009B4397  74 08                           je 0x1409b43a1
009B4399  48 8B CF                        mov rcx, rdi
009B439C  E8 2B F9 FF FF                  call 0x1409b3ccc
009B43A1  41 F6 C6 08                     test r14b, 8
009B43A5  74 3D                           je 0x1409b43e4
009B43A7  40 F6 C6 04                     test sil, 4
009B43AB  75 37                           jne 0x1409b43e4
009B43AD  40 F6 C6 02                     test sil, 2
009B43B1  0F 84 BA 04 00 00               je 0x1409b4871
009B43B7  41 F6 C6 40                     test r14b, 0x40
009B43BB  75 1F                           jne 0x1409b43dc
009B43BD  48 8D 97 98 06 00 00            lea rdx, [rdi + 0x698]
009B43C4  48 8D 4F 70                     lea rcx, [rdi + 0x70]
009B43C8  E8 63 9B A8 FF                  call 0x14043df30
009B43CD  48 8D 4F 70                     lea rcx, [rdi + 0x70]
009B43D1  E8 9A FB A7 FF                  call 0x140433f70
009B43D6  89 87 80 00 00 00               mov dword ptr [rdi + 0x80], eax
009B43DC  48 8B CF                        mov rcx, rdi
009B43DF  E8 94 E2 FF FF                  call 0x1409b2678
009B43E4  4C 89 64 24 58                  mov qword ptr [rsp + 0x58], r12
009B43E9  4D 8B EC                        mov r13, r12
009B43EC  41 F6 C6 01                     test r14b, 1
009B43F0  0F 85 B6 00 00 00               jne 0x1409b44ac
009B43F6  41 8B DE                        mov ebx, r14d
009B43F9  D1 EB                           shr ebx, 1
009B43FB  80 E3 01                        and bl, 1
009B43FE  45 84 E4                        test r12b, r12b
009B4401  74 11                           je 0x1409b4414
009B4403  48 8D 97 60 10 00 00            lea rdx, [rdi + 0x1060]
009B440A  E8 D1 0A 00 00                  call 0x1409b4ee0
009B440F  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
009B4414  84 DB                           test bl, bl
009B4416  74 0F                           je 0x1409b4427
009B4418  48 8D 97 70 10 00 00            lea rdx, [rdi + 0x1070]
009B441F  E8 BC 0A 00 00                  call 0x1409b4ee0
009B4424  4C 8B E8                        mov r13, rax
009B4427  48 8B CF                        mov rcx, rdi
009B442A  E8 05 58 21 00                  call 0x140bc9c34
009B442F  E8 50 56 21 00                  call 0x140bc9a84
009B4434  45 84 E4                        test r12b, r12b
009B4437  74 1E                           je 0x1409b4457
009B4439  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
009B443E  48 8D 8F 60 10 00 00            lea rcx, [rdi + 0x1060]
009B4445  40 F6 C6 02                     test sil, 2
009B4449  0F 84 17 04 00 00               je 0x1409b4866
009B444F  45 33 C0                        xor r8d, r8d
009B4452  E8 71 6C 0B 00                  call 0x140a6b0c8
009B4457  84 DB                           test bl, bl
009B4459  0F 84 74 FB FF FF               je 0x1409b3fd3
009B445F  E9 53 FB FF FF                  jmp 0x1409b3fb7
009B4464  41 BF 0D 00 00 C0               mov r15d, 0xc000000d
009B446A  E9 72 FB FF FF                  jmp 0x1409b3fe1
009B446F  E8 C0 56 21 00                  call 0x140bc9b34
009B4474  E9 09 FB FF FF                  jmp 0x1409b3f82
009B4479  48 8B CF                        mov rcx, rdi
009B447C  E8 13 54 EA FF                  call 0x140859894
009B4481  33 D2                           xor edx, edx
009B4483  41 B8 00 10 00 00               mov r8d, 0x1000
009B4489  48 8B CF                        mov rcx, rdi
009B448C  E8 13 08 AE FF                  call 0x140494ca4
009B4491  45 33 E4                        xor r12d, r12d
009B4494  44 8B F8                        mov r15d, eax
009B4497  48 8B CF                        mov rcx, rdi
009B449A  85 C0                           test eax, eax
009B449C  0F 88 B0 03 00 00               js 0x1409b4852
009B44A2  E8 3D 54 EA FF                  call 0x1408598e4
009B44A7  E9 64 FD FF FF                  jmp 0x1409b4210
009B44AC  40 F6 C6 10                     test sil, 0x10
009B44B0  0F 85 40 FF FF FF               jne 0x1409b43f6
009B44B6  41 B4 01                        mov r12b, 1
009B44B9  E9 38 FF FF FF                  jmp 0x1409b43f6
009B44BE  48 8D 8F 70 10 00 00            lea rcx, [rdi + 0x1070]
009B44C5  E8 0E 83 AD FF                  call 0x14048c7d8
009B44CA  84 C0                           test al, al
009B44CC  75 34                           jne 0x1409b4502
009B44CE  E8 89 A0 AE FF                  call 0x14049e55c
009B44D3  E9 05 FD FF FF                  jmp 0x1409b41dd
009B44D8  48 8B CF                        mov rcx, rdi
009B44DB  45 85 FF                        test r15d, r15d
009B44DE  0F 89 3F 01 00 00               jns 0x1409b4623
009B44E4  E8 BF E2 10 00                  call 0x140ac27a8
009B44E9  E9 A2 FE FF FF                  jmp 0x1409b4390
009B44EE  48 8D 8F 70 10 00 00            lea rcx, [rdi + 0x1070]
009B44F5  E8 DE 82 AD FF                  call 0x14048c7d8
009B44FA  84 C0                           test al, al
009B44FC  0F 84 D1 FB FF FF               je 0x1409b40d3
009B4502  48 8B D1                        mov rdx, rcx
009B4505  48 8B CF                        mov rcx, rdi
009B4508  E8 03 BC 0E 00                  call 0x140aa0110
009B450D  E9 5A FA FF FF                  jmp 0x1409b3f6c
009B4512  8B D3                           mov edx, ebx
009B4514  E8 37 AF 09 00                  call 0x140a4f450
009B4519  8B 54 24 44                     mov edx, dword ptr [rsp + 0x44]
009B451D  45 8B C5                        mov r8d, r13d
009B4520  48 8B CF                        mov rcx, rdi
009B4523  E8 98 04 12 00                  call 0x140ad49c0
009B4528  44 8B C0                        mov r8d, eax
009B452B  8B D3                           mov edx, ebx
009B452D  44 8B F8                        mov r15d, eax
009B4530  E8 33 8D 09 00                  call 0x140a4d268
009B4535  8B 74 24 34                     mov esi, dword ptr [rsp + 0x34]
009B4539  45 85 FF                        test r15d, r15d
009B453C  0F 88 F4 FD FF FF               js 0x1409b4336
009B4542  83 CE 21                        or esi, 0x21
009B4545  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
009B4549  E9 0D FD FF FF                  jmp 0x1409b425b
009B454E  8B D0                           mov edx, eax
009B4550  E8 FB AE 09 00                  call 0x140a4f450
009B4555  45 8B CD                        mov r9d, r13d
009B4558  44 8A C3                        mov r8b, bl
009B455B  8A D3                           mov dl, bl
009B455D  48 8B CF                        mov rcx, rdi
009B4560  E8 43 E2 FF FF                  call 0x1409b27a8
009B4565  44 8B C0                        mov r8d, eax
009B4568  BA 06 00 00 00                  mov edx, 6
009B456D  44 8B F8                        mov r15d, eax
009B4570  E8 F3 8C 09 00                  call 0x140a4d268
009B4575  45 85 FF                        test r15d, r15d
009B4578  0F 88 B8 FD FF FF               js 0x1409b4336
009B457E  83 CE 20                        or esi, 0x20
009B4581  48 8B CF                        mov rcx, rdi
009B4584  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
009B4588  E8 8F 28 00 00                  call 0x1409b6e1c
009B458D  E9 8E FD FF FF                  jmp 0x1409b4320
009B4592  8B D0                           mov edx, eax
009B4594  E8 B7 AE 09 00                  call 0x140a4f450
009B4599  45 8B C5                        mov r8d, r13d
009B459C  8A D3                           mov dl, bl
009B459E  48 8B CF                        mov rcx, rdi
009B45A1  E8 CE DD FF FF                  call 0x1409b2374
009B45A6  44 8B C0                        mov r8d, eax
009B45A9  BA 05 00 00 00                  mov edx, 5
009B45AE  44 8B F8                        mov r15d, eax
009B45B1  E8 B2 8C 09 00                  call 0x140a4d268
009B45B6  45 85 FF                        test r15d, r15d
009B45B9  0F 88 77 FD FF FF               js 0x1409b4336
009B45BF  83 CE 20                        or esi, 0x20
009B45C2  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
009B45C6  E9 41 FD FF FF                  jmp 0x1409b430c
009B45CB  40 F6 C6 20                     test sil, 0x20
009B45CF  0F 85 56 FD FF FF               jne 0x1409b432b
009B45D5  41 BF 07 00 00 00               mov r15d, 7
009B45DB  41 8B D7                        mov edx, r15d
009B45DE  E8 6D AE 09 00                  call 0x140a4f450
009B45E3  33 D2                           xor edx, edx
009B45E5  48 8B CF                        mov rcx, rdi
009B45E8  E8 BF E5 FF FF                  call 0x1409b2bac
009B45ED  85 C0                           test eax, eax
009B45EF  78 07                           js 0x1409b45f8
009B45F1  83 CE 20                        or esi, 0x20
009B45F4  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
009B45F8  8B C6                           mov eax, esi
009B45FA  41 8B D7                        mov edx, r15d
009B45FD  24 20                           and al, 0x20
009B45FF  F6 D8                           neg al
009B4601  45 1B C0                        sbb r8d, r8d
009B4604  41 F7 D0                        not r8d
009B4607  41 81 E0 01 00 00 C0            and r8d, 0xc0000001
009B460E  E8 55 8C 09 00                  call 0x140a4d268
009B4613  E9 13 FD FF FF                  jmp 0x1409b432b
009B4618  41 B8 01 00 00 C0               mov r8d, 0xc0000001
009B461E  E9 AB F9 FF FF                  jmp 0x1409b3fce
009B4623  E8 F8 95 A8 FF                  call 0x14043dc20
009B4628  48 8B CF                        mov rcx, rdi
009B462B  E8 9C F6 FF FF                  call 0x1409b3ccc
009B4630  44 84 F3                        test bl, r14b
009B4633  0F 84 1B 01 00 00               je 0x1409b4754
009B4639  40 F6 C6 10                     test sil, 0x10
009B463D  0F 85 11 01 00 00               jne 0x1409b4754
009B4643  48 8B CF                        mov rcx, rdi
009B4646  E8 11 A5 0E 00                  call 0x140a9eb5c
009B464B  44 89 A7 B4 00 00 00            mov dword ptr [rdi + 0xb4], r12d
009B4652  E8 81 2F 0D 00                  call 0x140a875d8
009B4657  84 C0                           test al, al
009B4659  0F 84 31 FD FF FF               je 0x1409b4390
009B465F  33 D2                           xor edx, edx
009B4661  E8 92 D8 FF FF                  call 0x1409b1ef8
009B4666  E9 25 FD FF FF                  jmp 0x1409b4390
009B466B  8B D0                           mov edx, eax
009B466D  E8 DE AD 09 00                  call 0x140a4f450
009B4672  45 8B CD                        mov r9d, r13d
009B4675  44 8A C3                        mov r8b, bl
009B4678  33 D2                           xor edx, edx
009B467A  48 8B CF                        mov rcx, rdi
009B467D  E8 26 E1 FF FF                  call 0x1409b27a8
009B4682  44 8B C0                        mov r8d, eax
009B4685  BA 03 00 00 00                  mov edx, 3
009B468A  44 8B F8                        mov r15d, eax
009B468D  E8 D6 8B 09 00                  call 0x140a4d268
009B4692  45 85 FF                        test r15d, r15d
009B4695  0F 88 A8 01 00 00               js 0x1409b4843
009B469B  83 CE 20                        or esi, 0x20
009B469E  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
009B46A2  E9 12 FC FF FF                  jmp 0x1409b42b9
009B46A7  48 8D 97 98 06 00 00            lea rdx, [rdi + 0x698]
009B46AE  48 8D 8F C8 06 00 00            lea rcx, [rdi + 0x6c8]
009B46B5  E8 76 98 A8 FF                  call 0x14043df30
009B46BA  48 8B CF                        mov rcx, rdi
009B46BD  E8 B6 DF FF FF                  call 0x1409b2678
009B46C2  83 CE 04                        or esi, 4
009B46C5  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
009B46C9  E9 06 FC FF FF                  jmp 0x1409b42d4
009B46CE  83 E8 01                        sub eax, 1
009B46D1  0F 85 BB 01 00 00               jne 0x1409b4892
009B46D7  8B 74 24 34                     mov esi, dword ptr [rsp + 0x34]
009B46DB  45 8B FC                        mov r15d, r12d
009B46DE  83 CE 02                        or esi, 2
009B46E1  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
009B46E5  E9 FA FC FF FF                  jmp 0x1409b43e4
009B46EA  8B 54 24 38                     mov edx, dword ptr [rsp + 0x38]
009B46EE  48 8B CF                        mov rcx, rdi
009B46F1  C1 EA 02                        shr edx, 2
009B46F4  22 D3                           and dl, bl
009B46F6  E8 FD D7 FF FF                  call 0x1409b1ef8
009B46FB  83 CE 08                        or esi, 8
009B46FE  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
009B4702  E9 E4 FB FF FF                  jmp 0x1409b42eb
009B4707  49 B8 B0 03 00 00 80 F7 FF FF   movabs r8, 0xfffff780000003b0
009B4711  49 B9 08 00 00 00 80 F7 FF FF   movabs r9, 0xfffff78000000008
009B471B  49 8B 10                        mov rdx, qword ptr [r8]
009B471E  49 8B 09                        mov rcx, qword ptr [r9]
009B4721  49 8B 00                        mov rax, qword ptr [r8]
009B4724  48 3B D0                        cmp rdx, rax
009B4727  75 F2                           jne 0x1409b471b
009B4729  44 8B 74 24 30                  mov r14d, dword ptr [rsp + 0x30]
009B472E  48 2B CA                        sub rcx, rdx
009B4731  48 89 8F 30 10 00 00            mov qword ptr [rdi + 0x1030], rcx
009B4738  41 0F BA E6 0C                  bt r14d, 0xc
009B473D  72 0C                           jb 0x1409b474b
009B473F  45 33 C0                        xor r8d, r8d
009B4742  33 D2                           xor edx, edx
009B4744  8B CB                           mov ecx, ebx
009B4746  E8 25 00 85 FF                  call 0x140204770
009B474B  8B 74 24 34                     mov esi, dword ptr [rsp + 0x34]
009B474F  E9 1F FC FF FF                  jmp 0x1409b4373
009B4754  8B 8F A8 00 00 00               mov ecx, dword ptr [rdi + 0xa8]
009B475A  8D 41 FC                        lea eax, [rcx - 4]
009B475D  3B C3                           cmp eax, ebx
009B475F  0F 87 2B FC FF FF               ja 0x1409b4390
009B4765  83 E9 04                        sub ecx, 4
009B4768  F7 D9                           neg ecx
009B476A  1B C9                           sbb ecx, ecx
009B476C  83 C1 05                        add ecx, 5
009B476F  E8 88 E6 FF FF                  call 0x1409b2dfc
009B4774  8B C8                           mov ecx, eax
009B4776  44 88 A4 39 C0 00 00 00         mov byte ptr [rcx + rdi + 0xc0], r12b
009B477E  E9 0D FC FF FF                  jmp 0x1409b4390
009B4783  48 8D 8F 70 10 00 00            lea rcx, [rdi + 0x1070]
009B478A  E8 49 80 AD FF                  call 0x14048c7d8
009B478F  84 C0                           test al, al
009B4791  74 15                           je 0x1409b47a8
009B4793  48 8B CF                        mov rcx, rdi
009B4796  E8 99 54 21 00                  call 0x140bc9c34
009B479B  E8 E4 52 21 00                  call 0x140bc9a84
009B47A0  45 33 FF                        xor r15d, r15d
009B47A3  E9 2B F8 FF FF                  jmp 0x1409b3fd3
009B47A8  48 8D 8F 60 10 00 00            lea rcx, [rdi + 0x1060]
009B47AF  E8 24 80 AD FF                  call 0x14048c7d8
009B47B4  84 C0                           test al, al
009B47B6  0F 84 0A F9 FF FF               je 0x1409b40c6
009B47BC  F6 C3 04                        test bl, 4
009B47BF  74 D2                           je 0x1409b4793
009B47C1  E9 00 F9 FF FF                  jmp 0x1409b40c6
009B47C6  E8 69 53 21 00                  call 0x140bc9b34
009B47CB  48 8B CF                        mov rcx, rdi
009B47CE  E8 7D 54 21 00                  call 0x140bc9c50
009B47D3  48 8D 97 60 10 00 00            lea rdx, [rdi + 0x1060]
009B47DA  E8 01 07 00 00                  call 0x1409b4ee0
009B47DF  41 B8 01 00 00 C0               mov r8d, 0xc0000001
009B47E5  48 8D 8F 60 10 00 00            lea rcx, [rdi + 0x1060]
009B47EC  40 F6 C6 02                     test sil, 2
009B47F0  48 8B D0                        mov rdx, rax
009B47F3  45 0F 45 C7                     cmovne r8d, r15d
009B47F7  E8 CC 68 0B 00                  call 0x140a6b0c8
009B47FC  83 CE 10                        or esi, 0x10
009B47FF  48 8B CF                        mov rcx, rdi
009B4802  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
009B4806  E8 29 54 21 00                  call 0x140bc9c34
009B480B  E8 74 52 21 00                  call 0x140bc9a84
009B4810  E9 E4 FA FF FF                  jmp 0x1409b42f9
009B4815  45 85 C0                        test r8d, r8d
009B4818  75 64                           jne 0x1409b487e
009B481A  44 39 47 68                     cmp dword ptr [rdi + 0x68], r8d
009B481E  74 62                           je 0x1409b4882
009B4820  BE 01 00 00 00                  mov esi, 1
009B4825  48 8B D1                        mov rdx, rcx
009B4828  48 8B CF                        mov rcx, rdi
009B482B  E8 E0 B8 0E 00                  call 0x140aa0110
009B4830  44 8B F8                        mov r15d, eax
009B4833  85 C0                           test eax, eax
009B4835  0F 88 31 F7 FF FF               js 0x1409b3f6c
009B483B  44 03 E6                        add r12d, esi
009B483E  E9 29 F7 FF FF                  jmp 0x1409b3f6c
009B4843  41 0F BA EE 0A                  bts r14d, 0xa
009B4848  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
009B484D  E9 E4 FA FF FF                  jmp 0x1409b4336
009B4852  E8 8D 50 EA FF                  call 0x1408598e4
009B4857  41 BF 01 00 00 C0               mov r15d, 0xc0000001
009B485D  8B 74 24 34                     mov esi, dword ptr [rsp + 0x34]
009B4861  E9 7E FB FF FF                  jmp 0x1409b43e4
009B4866  41 B8 01 00 00 C0               mov r8d, 0xc0000001
009B486C  E9 E1 FB FF FF                  jmp 0x1409b4452
009B4871  48 8B CF                        mov rcx, rdi
009B4874  E8 3F 1B 09 00                  call 0x140a463b8
009B4879  E9 66 FB FF FF                  jmp 0x1409b43e4
009B487E  33 F6                           xor esi, esi
009B4880  EB A3                           jmp 0x1409b4825
009B4882  80 BF C3 00 00 00 00            cmp byte ptr [rdi + 0xc3], 0
009B4889  BE 02 00 00 00                  mov esi, 2
009B488E  74 95                           je 0x1409b4825
009B4890  EB 8E                           jmp 0x1409b4820
009B4892  41 BF 01 00 00 C0               mov r15d, 0xc0000001
009B4898  83 F8 01                        cmp eax, 1
009B489B  0F 85 8E F9 FF FF               jne 0x1409b422f
009B48A1  EB BA                           jmp 0x1409b485d
009B48A3  8B 87 18 01 00 00               mov eax, dword ptr [rdi + 0x118]
009B48A9  8B 8F 84 10 00 00               mov ecx, dword ptr [rdi + 0x1084]
009B48AF  3B C1                           cmp eax, ecx
009B48B1  0F 87 19 94 17 00               ja 0x140b2dcd0
009B48B7  41 0F BA F6 07                  btr r14d, 7
009B48BC  44 89 74 24 30                  mov dword ptr [rsp + 0x30], r14d
009B48C1  E9 72 F9 FF FF                  jmp 0x1409b4238
009B48C6  45 84 F6                        test r14b, r14b
009B48C9  0F 89 7D FA FF FF               jns 0x1409b434c
009B48CF  40 84 F3                        test bl, sil
009B48D2  0F 85 74 FA FF FF               jne 0x1409b434c
009B48D8  8B 44 24 40                     mov eax, dword ptr [rsp + 0x40]
009B48DC  89 87 84 10 00 00               mov dword ptr [rdi + 0x1084], eax
009B48E2  E9 65 FA FF FF                  jmp 0x1409b434c
009B48E7  40 F6 C6 02                     test sil, 2
009B48EB  0F 84 95 FA FF FF               je 0x1409b4386
009B48F1  41 0F BA E6 0A                  bt r14d, 0xa
009B48F6  0F 83 8A FA FF FF               jae 0x1409b4386
009B48FC  8B 44 24 50                     mov eax, dword ptr [rsp + 0x50]
009B4900  29 87 B4 00 00 00               sub dword ptr [rdi + 0xb4], eax
009B4906  FF 8F AC 00 00 00               dec dword ptr [rdi + 0xac]
009B490C  83 E6 FD                        and esi, 0xfffffffd
009B490F  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
009B4913  E9 6E FA FF FF                  jmp 0x1409b4386
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpFlushHive(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m128;
    unsigned int v_stack_m130;
    unsigned int v_stack_m138;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m144;
    unsigned __int64 v_stack_m148;
    unsigned int v_stack_m14C;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m154;
    unsigned int v_stack_m158;
    unsigned int v_stack_m15C;
    unsigned int v_stack_m160;
    unsigned int v_stack_m168;
    unsigned int v_stack_m170;
    unsigned __int64 v_stack_m178;
    unsigned __int64 v_stack_m188;
    unsigned __int64 v_stack_m190;
    unsigned int v_stack_m198;
    unsigned __int64 v_stack_m28;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (400);
    result = (*(unsigned __int64 *)(v_rip + 4548947)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 184 + 128) = result;
    result = 0;
    v_r15 = 0;
    v_stack_m178 = 0;
    v_stack_m170 = 0;
    v_stack_m188 = v_xmm0;
    if ((*(unsigned int *)(v_rip + 4546878)) >= = 4) {
        a1 = *(unsigned __int16 *)(a1 + 1856);
        a2 = v_rsp - 184 - 40;
        result = *(unsigned __int64 *)(a1 + 1856 + 8);
        a4 = 0;
        a3 = 0;
        *(unsigned __int64 *)(v_rsp - 184 - 48) = result;
        result = *(unsigned __int64 *)(a1 + 1840 + 8);
        *(unsigned __int64 *)(v_rsp - 184 - 16) = result;
        result = v_stack_m154;
        *(unsigned __int64 *)(v_rsp - 184) = result;
        result = *(unsigned __int16 *)(v_rip - 9821358);
        v_stack_m144 = (unsigned int)(result);
        result = *(unsigned __int64 *)(v_rip + 4546767);
        *(unsigned __int64 *)(v_rsp - 184 - 96) = result;
        *(unsigned __int64 *)(v_rsp - 184 - 64) = a2;
        a2 = v_rsp - 184 - 8;
        *(unsigned int *)(v_rsp - 184 - 40) = (unsigned int)(a1);
        a1 = *(unsigned __int16 *)(a1 + 1840);
        *(unsigned __int64 *)(v_rsp - 184 - 32) = a2;
        a2 = v_stack_m148;
        *(unsigned int *)(v_rsp - 184 - 8) = (unsigned int)(a1);
        *(unsigned int *)(v_rsp - 184 - 56) = 2;
        *(unsigned int *)(v_rsp - 184 - 24) = 2;
        v_stack_m154 = (unsigned int)((unsigned int)(a2));
        *(unsigned int *)(v_rsp - 184 + 8) = 4;
        v_stack_m148 = 0xB000000ULL;
        result = *(unsigned __int16 *)(result);
        *(unsigned int *)(v_rsp - 184 - 88) = (unsigned int)(result);
        result = v_rip - 9821436;
        *(unsigned __int64 *)(v_rsp - 184 - 80) = result;
        result = v_rip - 9797924;
        result = (unsigned int)((result) - ((unsigned int)(v_rip - 9898146)));
        *(unsigned int *)(v_rsp - 184 - 84) = 2;
        *(unsigned int *)(v_rsp - 184 - 72) = 43;
        *(unsigned int *)(v_rsp - 184 - 68) = 1;
        v_stack_m160 = (unsigned int)(result);
        result = v_stack_m160;
        a1 = *(unsigned __int64 *)(v_rip + 4546668);
        result = v_rsp - 184 - 96;
        v_stack_m190 = result;
        v_stack_m198 = 7;
        result = EtwWriteTransfer(a1, a2, a3, a4);
    }
    result = CmpTraceHiveFlushStart(a1 + 1840, a1 + 1856, (unsigned int)((unsigned int)((unsigned int)(a2))), a4);
    if (((*(unsigned int *)(a1 + 160)) & (0x8001ULL)) != 0) goto loc_009B3FE1;
    if ((*(unsigned __int64 *)(a1 + 1544)) == 0) goto loc_009B4464;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a2)))) | (12));
    if (((*(unsigned __int8 *)(a1 + 160)) & (2)) == 0) { v_rbx = (unsigned int)((unsigned int)(a2)); }
    v_r13 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (4));
    v_r13 = (unsigned int)((v_r13) & (1));
    v_r12 = 0;
loc_009B3F6C:
    if (0 >= 2) goto loc_009B3FD3;
    if ((((unsigned __int8)(v_rbx)) & (1)) != 0) goto loc_009B446F;
    a1 = 0;
    result = CmpLockRegistryFreezeAware(a1, a1 + 1856, (unsigned int)((unsigned int)((unsigned int)(a2))), a4);
loc_009B3F82:
    result = HvLockHiveFlusherExclusive(0, a1 + 1856, (unsigned int)((unsigned int)((unsigned int)(a2))), a4);
    a1 = (((*(unsigned __int8 *)(a1 + 164)) & (4)) != 0) ? 1 : 0;
    result = ((((unsigned __int8)(v_rbx)) & (64)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_009B40BD;
    result = HvUnlockHiveFlusherExclusive(a1, a1 + 1856, (unsigned int)((unsigned int)((unsigned int)(a2))), a4);
    result = CmpUnlockRegistry(a1, a1 + 1856, (unsigned int)((unsigned int)((unsigned int)(a2))), a4);
    goto loc_009B3FD3;
loc_009B3FB7:
    if ((((unsigned __int8)((unsigned int)(a2))) & (64)) == 0) goto loc_009B4618;
loc_009B3FCE:
    result = CmpWakeWriteQueueWaiters(a1 + 4208, v_r13, (unsigned int)((unsigned int)((unsigned int)(0xC0000189ULL))), a4);
loc_009B3FD3:
loc_009B3FE1:
    result = CmpTraceHiveFlushStop((unsigned int)((unsigned int)((unsigned int)(0xC0000189ULL))), v_r13, (unsigned int)((unsigned int)((unsigned int)(0xC0000189ULL))), a4);
    v_r12 = v_rip - 9798365;
    if ((*(unsigned int *)(v_rip + 4546408)) >= = 4) {
        result = v_stack_m168;
        a2 = v_rsp - 184 - 112;
        *(unsigned __int64 *)(v_rsp - 184 + 48) = result;
        v_r12 = (unsigned int)((v_rip - 9798365) - ((unsigned int)(v_rip - 9898577)));
        result = *(unsigned __int16 *)(v_rip - 9821628);
        a4 = 0;
        *(unsigned int *)(v_rsp - 184 - 108) = (unsigned int)(result);
        a3 = 0;
        result = *(unsigned __int64 *)(v_rip + 4546362);
        *(unsigned __int64 *)(v_rsp - 184 + 16) = result;
        v_stack_m168 = (unsigned int)((unsigned int)(0xC0000189ULL));
        *(unsigned int *)(v_rsp - 184 + 56) = 4;
        *(unsigned int *)(v_rsp - 184 - 112) = 0xB000000ULL;
        result = *(unsigned __int16 *)(result);
        *(unsigned int *)(v_rsp - 184 + 24) = (unsigned int)(result);
        result = v_rip - 9821670;
        *(unsigned __int64 *)(v_rsp - 184 + 32) = result;
        *(unsigned int *)(v_rsp - 184 + 28) = 2;
        *(unsigned int *)(v_rsp - 184 + 40) = 23;
        *(unsigned int *)(v_rsp - 184 + 44) = 1;
        v_stack_m158 = (unsigned int)(v_r12);
        result = v_stack_m158;
        a1 = *(unsigned __int64 *)(v_rip + 4546309);
        result = v_rsp - 184 + 16;
        v_stack_m190 = result;
        v_stack_m198 = 3;
        result = EtwWriteTransfer(a1, a2, a3, a4);
    }
    a1 = (*(unsigned __int64 *)(v_rsp - 184 + 128)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
loc_009B40BD:
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 56))) & (2)) != 0) goto loc_009B4783;
loc_009B40C6:
    a3 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56)))) & (4));
    if (condition_is_not_equal) goto loc_009B44EE;
loc_009B40D3:
    result = CmpIsWriteQueueActive(*(unsigned __int64 *)(v_stack_m28 + 72) + 4192, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_009B4815;
    result = CmpGenerateFlushControlData(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56))), v_stack_m160, a4);
    if ((*(unsigned int *)(v_rip + 4546139)) >= = 4) {
        result = v_stack_m160;
        a1 = v_rip - 9898878;
        a2 = v_rsp - 184 - 128;
        a4 = 0;
        a3 = 0;
        v_stack_m128 = (unsigned int)(result);
        result = v_stack_m128;
        *(unsigned __int64 *)(v_rsp - 184 + 96) = result;
        result = v_stack_m158;
        v_stack_m130 = (unsigned int)(result);
        result = v_stack_m130;
        *(unsigned __int64 *)(v_rsp - 184 + 112) = result;
        result = *(unsigned __int16 *)(v_rip - 9822011);
        *(unsigned int *)(v_rsp - 184 - 124) = (unsigned int)(result);
        result = *(unsigned __int64 *)(v_rip + 4546060);
        *(unsigned __int64 *)(v_rsp - 184 + 64) = result;
        *(unsigned int *)(v_rsp - 184 + 104) = 4;
        *(unsigned int *)(v_rsp - 184 + 120) = 4;
        *(unsigned int *)(v_rsp - 184 - 128) = 0xB000000ULL;
        result = *(unsigned __int16 *)(result);
        *(unsigned int *)(v_rsp - 184 + 72) = (unsigned int)(result);
        result = v_rip - 9822049;
        *(unsigned __int64 *)(v_rsp - 184 + 80) = result;
        result = v_rip - 9798792;
        result = (unsigned int)((result) - ((unsigned int)(a1)));
        *(unsigned int *)(v_rsp - 184 + 76) = 2;
        *(unsigned int *)(v_rsp - 184 + 88) = 63;
        *(unsigned int *)(v_rsp - 184 + 92) = 1;
        v_stack_m138 = (unsigned int)(result);
        result = v_stack_m138;
        a1 = *(unsigned __int64 *)(v_rip + 4545997);
        result = v_rsp - 184 + 64;
        v_stack_m168 = result;
        v_stack_m170 = 4;
        result = EtwWriteTransfer(a1, a2, a3, a4);
    }
    if ((((unsigned int)((unsigned int)(v_stack_m160))) & (856)) == 0) goto loc_009B4793;
    if ((((unsigned __int8)((unsigned int)(v_stack_m160))) & (2)) != 0) goto loc_009B44BE;
loc_009B41DD:
    if ((((unsigned __int8)((unsigned int)(v_stack_m160))) & (1)) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m28 + 72) + 4192;
        result = CmpAcquireWriteQueue(a1, a2, a3, a4);
    }
    v_rsi = ((((unsigned int)((unsigned int)(v_stack_m160))) & (272)) != 0) ? 1 : 0;
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m160)))) >> (6));
    v_rbx = (unsigned int)((v_rbx) & (1));
    if ((((unsigned __int8)((unsigned int)(v_stack_m160))) & (8)) != 0) goto loc_009B4479;
    v_r12 = 0;
loc_009B4210:
    if ((((unsigned int)((unsigned int)(v_stack_m160))) & (344)) == 0) goto loc_009B422F;
    result = HvStoreModifiedData(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned __int8)(v_rsi), (unsigned __int8)(v_rbx), a4);
    if ((unsigned int)(result) != 0) goto loc_009B46CE;
loc_009B422F:
    if (sign_flag) goto loc_009B48A3;
loc_009B4238:
    result = HvUnlockHiveFlusherExclusive(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned __int8)(v_rsi), (unsigned __int8)(v_rbx), a4);
    result = CmpUnlockRegistry(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned __int8)(v_rsi), (unsigned __int8)(v_rbx), a4);
    v_stack_m154 = 1;
    if (sign_flag) goto loc_009B4512;
loc_009B425B:
    v_stack_m154 = 2;
    if ((((unsigned __int8)((unsigned int)(v_stack_m160))) & (8)) == 0) goto loc_009B42A6;
    result = CmpLogFlushPhaseStart(*(unsigned __int64 *)(v_stack_m28 + 72), 2, (unsigned __int8)(v_rbx), a4);
    result = HvWriteLogFile(*(unsigned __int64 *)(v_stack_m28 + 72), 2, (unsigned __int8)(v_rbx), v_stack_m140);
    result = CmpLogFlushPhaseEnd(*(unsigned __int64 *)(v_stack_m28 + 72), 2, (unsigned int)((unsigned int)(result)), v_stack_m140);
    if (sign_flag) goto loc_009B4336;
    result = HvTruncateCurrentLogFileIfRequired(*(unsigned __int64 *)(v_stack_m28 + 72), 2, (unsigned int)((unsigned int)(result)), v_stack_m140);
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m15C)) | (2));
    v_stack_m15C = (unsigned int)(v_rsi);
loc_009B42A6:
    v_stack_m154 = 3;
    if ((((unsigned __int8)((unsigned int)(v_stack_m160))) & (16)) != 0) goto loc_009B466B;
loc_009B42B9:
    result = CmpLogFlushPhaseStart(*(unsigned __int64 *)(v_stack_m28 + 72), 4, (unsigned int)((unsigned int)(result)), v_stack_m140);
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m160)))) & (0x448ULL));
    if (((unsigned int)(result)) == 72) goto loc_009B46A7;
loc_009B42D4:
    result = CmpLogFlushPhaseEnd(*(unsigned __int64 *)(v_stack_m28 + 72), 4, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m140);
    if ((((unsigned __int8)((unsigned int)(v_stack_m160))) & (32)) != 0) goto loc_009B46EA;
loc_009B42EB:
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m160)))) & (69));
    if (((unsigned __int8)(result)) == 65) goto loc_009B47C6;
loc_009B42F9:
    v_stack_m154 = 5;
    if ((((unsigned __int8)((unsigned int)(v_stack_m160))) & (64)) != 0) goto loc_009B4592;
loc_009B430C:
    v_stack_m154 = 6;
    if (condition_is_below) goto loc_009B454E;
loc_009B4320:
    if (condition_is_below) goto loc_009B45CB;
loc_009B432B:
    v_stack_m154 = 8;
loc_009B4336:
    result = CmpLockRegistry(*(unsigned __int64 *)(v_stack_m28 + 72), 4, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m140);
    result = HvLockHiveFlusherExclusive(*(unsigned __int64 *)(v_stack_m28 + 72), 4, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), v_stack_m140);
    if (sign_flag) goto loc_009B48C6;
loc_009B434C:
    if ((((unsigned __int8)(v_rsi)) & (32)) != 0) {
        *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 4228) = 0;
    }
    if (sign_flag) goto loc_009B48E7;
    if (condition_is_below) goto loc_009B4707;
loc_009B4373:
    if (!(condition_is_above_or_equal)) {
        a3 = 1;
        a2 = 0;
        a1 = 1;
        result = CmpArmLazyWriter(a1, a2, a3, v_stack_m140);
    }
    if ((((unsigned __int8)((unsigned int)(v_stack_m160))) & (64)) != 0) goto loc_009B44D8;
loc_009B4390:
    if ((((unsigned int)((unsigned int)(v_stack_m160))) & (272)) != 0) {
        a1 = *(unsigned __int64 *)(v_stack_m28 + 72);
        result = HvFreeUnreconciledData(a1, a2, a3, v_stack_m140);
    }
    if ((((unsigned __int8)((unsigned int)(v_stack_m160))) & (8)) == 0) goto loc_009B43E4;
    if ((((unsigned __int8)(v_rsi)) & (4)) != 0) goto loc_009B43E4;
    if ((((unsigned __int8)(v_rsi)) & (2)) == 0) goto loc_009B4871;
    if ((((unsigned __int8)((unsigned int)(v_stack_m160))) & (64)) == 0) {
        a2 = *(unsigned __int64 *)(v_stack_m28 + 72) + 1688;
        a1 = *(unsigned __int64 *)(v_stack_m28 + 72) + 112;
        result = RtlMergeBitMaps(a1, a2, a3, v_stack_m140);
        a1 = *(unsigned __int64 *)(v_stack_m28 + 72) + 112;
        result = RtlNumberOfSetBits(a1, a2, a3, v_stack_m140);
        *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 128) = (unsigned int)(result);
    }
    result = HvFreeDirtyData(*(unsigned __int64 *)(v_stack_m28 + 72), a2, a3, v_stack_m140);
loc_009B43E4:
    v_stack_m138 = 0;
    if ((((unsigned __int8)((unsigned int)(v_stack_m160))) & (1)) != 0) goto loc_009B44AC;
loc_009B43F6:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(v_stack_m160)))) >> (1));
    v_rbx = (unsigned __int8)((v_rbx) & (1));
    if (0 != 0) {
        a2 = *(unsigned __int64 *)(v_stack_m28 + 72) + 4192;
        result = CmpReleaseWriteQueue(*(unsigned __int64 *)(v_stack_m28 + 72), a2, a3, v_stack_m140);
        v_stack_m138 = result;
    }
    v_r13 = 0;
    if ((unsigned __int8)(v_rbx) != 0) {
        a2 = *(unsigned __int64 *)(v_stack_m28 + 72) + 4208;
        result = CmpReleaseWriteQueue(*(unsigned __int64 *)(v_stack_m28 + 72), a2, a3, v_stack_m140);
        v_r13 = result;
    }
    result = HvUnlockHiveFlusherExclusive(*(unsigned __int64 *)(v_stack_m28 + 72), a2, a3, v_stack_m140);
    result = CmpUnlockRegistry(*(unsigned __int64 *)(v_stack_m28 + 72), a2, a3, v_stack_m140);
    if (0 == 0) goto loc_009B4457;
    if ((((unsigned __int8)(v_rsi)) & (2)) == 0) goto loc_009B4866;
    a3 = 0;
loc_009B4452:
    result = CmpWakeWriteQueueWaiters(*(unsigned __int64 *)(v_stack_m28 + 72) + 4192, v_stack_m138, a3, v_stack_m140);
loc_009B4457:
    if ((unsigned __int8)(v_rbx) == 0) goto loc_009B3FD3;
    goto loc_009B3FB7;
loc_009B4464:
    goto loc_009B3FE1;
loc_009B446F:
    result = CmpLockRegistry(*(unsigned __int64 *)(v_stack_m28 + 72) + 4192, v_stack_m138, a3, v_stack_m140);
    goto loc_009B3F82;
loc_009B4479:
    result = HvLockHiveWriter(*(unsigned __int64 *)(v_stack_m28 + 72), v_stack_m138, a3, v_stack_m140);
    a2 = 0;
    result = HvMarkDirtyForFlush(*(unsigned __int64 *)(v_stack_m28 + 72), a2, (unsigned int)(0x1000ULL), v_stack_m140);
    v_r12 = 0;
    if (sign_flag) goto loc_009B4852;
    result = HvUnlockHiveWriter(*(unsigned __int64 *)(v_stack_m28 + 72), a2, (unsigned int)(0x1000ULL), v_stack_m140);
    goto loc_009B4210;
loc_009B44AC:
    if ((((unsigned __int8)(v_rsi)) & (16)) != 0) goto loc_009B43F6;
    goto loc_009B43F6;
loc_009B44BE:
    result = CmpIsWriteQueueActive(*(unsigned __int64 *)(v_stack_m28 + 72) + 4208, a2, (unsigned int)(0x1000ULL), v_stack_m140);
    if ((unsigned __int8)(result) != 0) goto loc_009B4502;
    result = CmpAcquireWriteQueue(*(unsigned __int64 *)(v_stack_m28 + 72) + 4208, a2, (unsigned int)(0x1000ULL), v_stack_m140);
    goto loc_009B41DD;
loc_009B44D8:
    if (!sign_flag) goto loc_009B4623;
    result = HvFoldBackUnreconciledData(*(unsigned __int64 *)(v_stack_m28 + 72), a2, (unsigned int)(0x1000ULL), v_stack_m140);
    goto loc_009B4390;
loc_009B44EE:
    result = CmpIsWriteQueueActive(*(unsigned __int64 *)(v_stack_m28 + 72) + 4208, a2, (unsigned int)(0x1000ULL), v_stack_m140);
    if ((unsigned __int8)(result) == 0) goto loc_009B40D3;
loc_009B4502:
    result = CmpWaitOnHiveWriteQueue(*(unsigned __int64 *)(v_stack_m28 + 72), *(unsigned __int64 *)(v_stack_m28 + 72) + 4208, (unsigned int)(0x1000ULL), v_stack_m140);
    goto loc_009B3F6C;
loc_009B4512:
    result = CmpLogFlushPhaseStart(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)((unsigned int)(v_rbx)), (unsigned int)(0x1000ULL), v_stack_m140);
    result = HvExtendHivePrimaryFileValidDataLength(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)(v_stack_m14C), (unsigned int)((unsigned int)(v_r13)), v_stack_m140);
    result = CmpLogFlushPhaseEnd(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(result)), v_stack_m140);
    if (sign_flag) goto loc_009B4336;
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m15C)) | (33));
    v_stack_m15C = (unsigned int)(v_rsi);
    goto loc_009B425B;
loc_009B454E:
    result = CmpLogFlushPhaseStart(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(result)), v_stack_m140);
    result = HvValidateOrInvalidatePrimaryFileHeader(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned __int8)(v_rbx), (unsigned __int8)(v_rbx), (unsigned int)((unsigned int)(v_r13)));
    result = CmpLogFlushPhaseEnd(*(unsigned __int64 *)(v_stack_m28 + 72), 6, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_r13)));
    if (sign_flag) goto loc_009B4336;
    v_rsi = (unsigned int)((v_rsi) | (32));
    v_stack_m15C = (unsigned int)(v_rsi);
    result = HvTruncateAllLogFilesIfRequired(*(unsigned __int64 *)(v_stack_m28 + 72), 6, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_r13)));
    goto loc_009B4320;
loc_009B4592:
    result = CmpLogFlushPhaseStart(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_r13)));
    result = HvWriteHivePrimaryFile(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned __int8)(v_rbx), (unsigned int)((unsigned int)(v_r13)), (unsigned int)((unsigned int)(v_r13)));
    result = CmpLogFlushPhaseEnd(*(unsigned __int64 *)(v_stack_m28 + 72), 5, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_r13)));
    if (sign_flag) goto loc_009B4336;
    v_rsi = (unsigned int)((v_rsi) | (32));
    v_stack_m15C = (unsigned int)(v_rsi);
    goto loc_009B430C;
loc_009B45CB:
    if ((((unsigned __int8)(v_rsi)) & (32)) != 0) goto loc_009B432B;
    result = CmpLogFlushPhaseStart(*(unsigned __int64 *)(v_stack_m28 + 72), 7, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_r13)));
    a2 = 0;
    result = CmpFileFlushAndPurge(*(unsigned __int64 *)(v_stack_m28 + 72), a2, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_r13)));
    if (!(sign_flag)) {
        v_rsi = (unsigned int)((v_rsi) | (32));
        v_stack_m15C = (unsigned int)(v_rsi);
    }
    result = (unsigned __int8)(((unsigned int)((unsigned int)(v_rsi))) & (32));
    result = (unsigned __int8)(-(result));
    a3 = (unsigned int)(~((unsigned int)((unsigned int)(result))));
    a3 = (unsigned int)((a3) & (0xC0000001ULL));
    result = CmpLogFlushPhaseEnd(*(unsigned __int64 *)(v_stack_m28 + 72), 7, a3, (unsigned int)((unsigned int)(v_r13)));
    goto loc_009B432B;
loc_009B4618:
    goto loc_009B3FCE;
loc_009B4623:
    result = HvUnCOWReconciledPages(*(unsigned __int64 *)(v_stack_m28 + 72), 7, (unsigned int)(0xC0000001ULL), (unsigned int)((unsigned int)(v_r13)));
    result = HvFreeUnreconciledData(*(unsigned __int64 *)(v_stack_m28 + 72), 7, (unsigned int)(0xC0000001ULL), (unsigned int)((unsigned int)(v_r13)));
    if ((((unsigned __int8)(v_rbx)) & ((unsigned __int8)((unsigned int)(v_stack_m160)))) == 0) goto loc_009B4754;
    if ((((unsigned __int8)(v_rsi)) & (16)) != 0) goto loc_009B4754;
    result = HvResetLogFileStatusAll(*(unsigned __int64 *)(v_stack_m28 + 72), 7, (unsigned int)(0xC0000001ULL), (unsigned int)((unsigned int)(v_r13)));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 180) = 1;
    result = HvIsCurrentLogSwappable(*(unsigned __int64 *)(v_stack_m28 + 72), 7, (unsigned int)(0xC0000001ULL), (unsigned int)((unsigned int)(v_r13)));
    if ((unsigned __int8)(result) == 0) goto loc_009B4390;
    a2 = 0;
    result = HvSwapLogFiles(*(unsigned __int64 *)(v_stack_m28 + 72), a2, (unsigned int)(0xC0000001ULL), (unsigned int)((unsigned int)(v_r13)));
    goto loc_009B4390;
loc_009B466B:
    result = CmpLogFlushPhaseStart(*(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)((unsigned int)(result)), (unsigned int)(0xC0000001ULL), (unsigned int)((unsigned int)(v_r13)));
    a2 = 0;
    result = HvValidateOrInvalidatePrimaryFileHeader(*(unsigned __int64 *)(v_stack_m28 + 72), a2, (unsigned __int8)(v_rbx), (unsigned int)((unsigned int)(v_r13)));
    result = CmpLogFlushPhaseEnd(*(unsigned __int64 *)(v_stack_m28 + 72), 3, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_r13)));
    if (sign_flag) goto loc_009B4843;
    v_rsi = (unsigned int)((v_rsi) | (32));
    v_stack_m15C = (unsigned int)(v_rsi);
    goto loc_009B42B9;
loc_009B46A7:
    result = RtlMergeBitMaps(*(unsigned __int64 *)(v_stack_m28 + 72) + 1736, *(unsigned __int64 *)(v_stack_m28 + 72) + 1688, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_r13)));
    result = HvFreeDirtyData(*(unsigned __int64 *)(v_stack_m28 + 72), *(unsigned __int64 *)(v_stack_m28 + 72) + 1688, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_r13)));
    v_rsi = (unsigned int)((v_rsi) | (4));
    v_stack_m15C = (unsigned int)(v_rsi);
    goto loc_009B42D4;
loc_009B46CE:
    result = (unsigned int)((result) - (1));
    if (condition_is_not_equal) goto loc_009B4892;
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m15C)) | (2));
    v_stack_m15C = (unsigned int)(v_rsi);
    goto loc_009B43E4;
loc_009B46EA:
    a2 = (unsigned int)(((unsigned int)(v_stack_m158)) >> (2));
    a2 = (unsigned __int8)((a2) & ((unsigned __int8)(v_rbx)));
    result = HvSwapLogFiles(*(unsigned __int64 *)(v_stack_m28 + 72), a2, (unsigned int)((unsigned int)(result)), (unsigned int)((unsigned int)(v_r13)));
    v_rsi = (unsigned int)((v_rsi) | (8));
    v_stack_m15C = (unsigned int)(v_rsi);
    goto loc_009B42EB;
loc_009B4707:
loc_009B471B:
    if ((*(unsigned __int64 *)((unsigned int)((unsigned int)(result)))) != (*(unsigned __int64 *)((unsigned int)((unsigned int)(result))))) goto loc_009B471B;
    a1 = (*(unsigned __int64 *)((unsigned int)((unsigned int)(v_r13)))) - (*(unsigned __int64 *)((unsigned int)((unsigned int)(result))));
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 4144) = a1;
    result = *(unsigned __int64 *)((unsigned int)((unsigned int)(result)));
    if (!(condition_is_below)) {
        a3 = 0;
        a2 = 0;
        a1 = (unsigned int)(v_rbx);
        result = CmpArmLazyWriter(a1, a2, a3, (unsigned int)((unsigned int)(v_r13)));
    }
    goto loc_009B4373;
loc_009B4754:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 168)) - 4)) > ((unsigned int)(v_rbx))) goto loc_009B4390;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 168))) - (4));
    a1 = (unsigned int)(-(a1));
    a1 = (unsigned int)((a1) + (5));
    result = HvpLogTypeToLogArrayIndex(a1, a2, a3, (unsigned int)((unsigned int)(v_r13)));
    *(unsigned __int8 *)((unsigned int)((unsigned int)(result)) + *(unsigned __int64 *)(v_stack_m28 + 72) * 1 + 192) = 1;
    goto loc_009B4390;
loc_009B4783:
    result = CmpIsWriteQueueActive(*(unsigned __int64 *)(v_stack_m28 + 72) + 4208, a2, a3, (unsigned int)((unsigned int)(v_r13)));
    if ((unsigned __int8)(result) == 0) goto loc_009B47A8;
loc_009B4793:
    result = HvUnlockHiveFlusherExclusive(*(unsigned __int64 *)(v_stack_m28 + 72), a2, a3, (unsigned int)((unsigned int)(v_r13)));
    result = CmpUnlockRegistry(*(unsigned __int64 *)(v_stack_m28 + 72), a2, a3, (unsigned int)((unsigned int)(v_r13)));
    v_r15 = 0;
    goto loc_009B3FD3;
loc_009B47A8:
    result = CmpIsWriteQueueActive(*(unsigned __int64 *)(v_stack_m28 + 72) + 4192, a2, a3, (unsigned int)((unsigned int)(v_r13)));
    if ((unsigned __int8)(result) == 0) goto loc_009B40C6;
    if ((((unsigned __int8)(v_rbx)) & (4)) == 0) goto loc_009B4793;
    goto loc_009B40C6;
loc_009B47C6:
    result = CmpLockRegistry(*(unsigned __int64 *)(v_stack_m28 + 72) + 4192, a2, a3, (unsigned int)((unsigned int)(v_r13)));
    result = HvLockHiveFlusherExclusive(*(unsigned __int64 *)(v_stack_m28 + 72), a2, a3, (unsigned int)((unsigned int)(v_r13)));
    result = CmpReleaseWriteQueue(*(unsigned __int64 *)(v_stack_m28 + 72), *(unsigned __int64 *)(v_stack_m28 + 72) + 4192, a3, (unsigned int)((unsigned int)(v_r13)));
    a3 = (unsigned int)(0xC0000001ULL);
    if ((((unsigned __int8)((unsigned int)(v_stack_m15C))) & (2)) != 0) { a3 = 0; }
    result = CmpWakeWriteQueueWaiters(*(unsigned __int64 *)(v_stack_m28 + 72) + 4192, result, a3, (unsigned int)((unsigned int)(v_r13)));
    v_rsi = (unsigned int)(((unsigned int)(v_stack_m15C)) | (16));
    v_stack_m15C = (unsigned int)(v_rsi);
    result = HvUnlockHiveFlusherExclusive(*(unsigned __int64 *)(v_stack_m28 + 72), result, a3, (unsigned int)((unsigned int)(v_r13)));
    result = CmpUnlockRegistry(*(unsigned __int64 *)(v_stack_m28 + 72), result, a3, (unsigned int)((unsigned int)(v_r13)));
    goto loc_009B42F9;
loc_009B4815:
    if (a3 != 0) goto loc_009B487E;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 104)) == a3) goto loc_009B4882;
loc_009B4820:
loc_009B4825:
    result = CmpWaitOnHiveWriteQueue(*(unsigned __int64 *)(v_stack_m28 + 72), *(unsigned __int64 *)(v_stack_m28 + 72), a3, (unsigned int)((unsigned int)(v_r13)));
    if (sign_flag) goto loc_009B3F6C;
    v_r12 = (unsigned int)((1) + (1));
    goto loc_009B3F6C;
loc_009B4843:
    v_stack_m160 = (unsigned int)((unsigned int)(v_stack_m160));
    goto loc_009B4336;
loc_009B4852:
    result = HvUnlockHiveWriter(*(unsigned __int64 *)(v_stack_m28 + 72), *(unsigned __int64 *)(v_stack_m28 + 72), a3, (unsigned int)((unsigned int)(v_r13)));
loc_009B485D:
    goto loc_009B43E4;
loc_009B4866:
    goto loc_009B4452;
loc_009B4871:
    result = HvFoldBackDirtyData(*(unsigned __int64 *)(v_stack_m28 + 72), *(unsigned __int64 *)(v_stack_m28 + 72), (unsigned int)(0xC0000001ULL), (unsigned int)((unsigned int)(v_r13)));
    goto loc_009B43E4;
loc_009B487E:
    v_rsi = 0;
    goto loc_009B4825;
loc_009B4882:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 195)) == 0) goto loc_009B4825;
    goto loc_009B4820;
loc_009B4892:
    if (((unsigned int)(result)) != 1) goto loc_009B422F;
    goto loc_009B485D;
loc_009B48A3:
    v_stack_m160 = (unsigned int)((unsigned int)(v_stack_m160));
    goto loc_009B4238;
loc_009B48C6:
    if (!sign_flag) goto loc_009B434C;
    if ((((unsigned __int8)(v_rbx)) & (2)) != 0) goto loc_009B434C;
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m28 + 72) + 4228) = (unsigned int)((unsigned int)(v_stack_m150));
    goto loc_009B434C;
loc_009B48E7:
    if (2 == 0) goto loc_009B4386;
    if (condition_is_above_or_equal) goto loc_009B4386;
    v_rsi = (unsigned int)((2) & (0xFFFFFFFDULL));
    v_stack_m15C = (unsigned int)(v_rsi);
    goto loc_009B4386;
}
```

## 5. (Beta) C Style

```c
int64_t CmpFlushHive(void *Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m128;
    uint32_t v_stack_m130;
    uint32_t v_stack_m138;
    uint64_t v_stack_m140;
    uint32_t v_stack_m144;
    uint64_t v_stack_m148;
    uint32_t v_stack_m14C;
    uint32_t v_stack_m150;
    uint64_t v_stack_m154;
    uint32_t v_stack_m158;
    uint32_t v_stack_m15C;
    uint32_t v_stack_m160;
    uint32_t v_stack_m168;
    uint32_t v_stack_m170;
    uint64_t v_stack_m178;
    uint64_t v_stack_m188;
    uint64_t v_stack_m190;
    uint32_t v_stack_m198;
    uint64_t v_stack_m28;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (400);
    result = (*(uint64_t *)(v_rip + 0x456953)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0xB8 + 0x80) = result;
    result = 0;
    local_r15 = 0;
    v_stack_m178 = 0;
    v_stack_m170 = 0;
    v_stack_m188 = v_xmm0;
    if ((*(uint32_t *)(v_rip + 0x45613E)) >= = 4) {
        Arg1 = *(uint16_t *)(arg1 + 0x740);
        Arg2 = local_rsp - 184 - 40;
        result = *(uint64_t *)(arg1 + 0x740 + 0x8);
        Arg4 = 0;
        Arg3 = 0;
        *(uint64_t *)(local_rsp - 0xB8 - 0x30) = result;
        result = *(uint64_t *)(arg1 + 0x730 + 0x8);
        *(uint64_t *)(local_rsp - 0xB8 - 0x10) = result;
        result = v_stack_m154;
        *(uint64_t *)(local_rsp - 0xB8) = result;
        result = *(uint16_t *)(v_rip - 0x95DCAE);
        v_stack_m144 = (uint32_t)(result);
        result = *(uint64_t *)(v_rip + 0x4560CF);
        *(uint64_t *)(local_rsp - 0xB8 - 0x60) = result;
        *(uint64_t *)(local_rsp - 0xB8 - 0x40) = Arg2;
        Arg2 = local_rsp - 184 - 8;
        *(uint32_t *)(local_rsp - 0xB8 - 0x28) = (uint32_t)(Arg1);
        Arg1 = *(uint16_t *)(arg1 + 0x730);
        *(uint64_t *)(local_rsp - 0xB8 - 0x20) = Arg2;
        Arg2 = v_stack_m148;
        *(uint32_t *)(local_rsp - 0xB8 - 0x8) = (uint32_t)(Arg1);
        *(uint32_t *)(local_rsp - 0xB8 - 0x38) = 2;
        *(uint32_t *)(local_rsp - 0xB8 - 0x18) = 2;
        v_stack_m154 = (uint32_t)((uint32_t)(Arg2));
        *(uint32_t *)(local_rsp - 0xB8 + 0x8) = 4;
        v_stack_m148 = 0xB000000ULL;
        result = *(uint16_t *)(result);
        *(uint32_t *)(local_rsp - 0xB8 - 0x58) = (uint32_t)(result);
        result = v_rip - 9821436;
        *(uint64_t *)(local_rsp - 0xB8 - 0x50) = result;
        result = v_rip - 9797924;
        result = (uint32_t)((result) - ((uint32_t)(v_rip - 9898146)));
        *(uint32_t *)(local_rsp - 0xB8 - 0x54) = 2;
        *(uint32_t *)(local_rsp - 0xB8 - 0x48) = 43;
        *(uint32_t *)(local_rsp - 0xB8 - 0x44) = 1;
        v_stack_m160 = (uint32_t)(result);
        result = v_stack_m160;
        Arg1 = *(uint64_t *)(v_rip + 0x45606C);
        result = local_rsp - 184 - 96;
        v_stack_m190 = result;
        v_stack_m198 = 7;
        result = EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    result = CmpTraceHiveFlushStart(Arg1 + 1840, Arg1 + 1856, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg4);
    if (((*(uint32_t *)(arg1 + 0xA0)) & (0x8001ULL)) != 0) goto loc_009B3FE1;
    if ((*(uint64_t *)(arg1 + 0x608)) == 0) goto loc_009B4464;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg2)))) | (12));
    if (((*(uint8_t *)(arg1 + 0xA0)) & (2)) == 0) { local_rbx = (uint32_t)((uint32_t)(Arg2)); }
    local_r13 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (4));
    local_r13 = (uint32_t)((local_r13) & (1));
    local_r12 = 0;
loc_009B3F6C:
    if (0 >= 2) goto loc_009B3FD3;
    if ((((uint8_t)(local_rbx)) & (1)) != 0) goto loc_009B446F;
    Arg1 = 0;
    result = CmpLockRegistryFreezeAware(Arg1, Arg1 + 1856, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg4);
loc_009B3F82:
    result = HvLockHiveFlusherExclusive(0, Arg1 + 1856, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg4);
    Arg1 = (((*(uint8_t *)(arg1 + 0xA4)) & (4)) != 0) ? 1 : 0;
    result = ((((uint8_t)(local_rbx)) & (64)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_009B40BD;
    result = HvUnlockHiveFlusherExclusive(Arg1, Arg1 + 1856, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg4);
    result = CmpUnlockRegistry(Arg1, Arg1 + 1856, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg4);
    goto loc_009B3FD3;
loc_009B3FB7:
    if ((((uint8_t)((uint32_t)(Arg2))) & (64)) == 0) goto loc_009B4618;
loc_009B3FCE:
    result = CmpWakeWriteQueueWaiters(Arg1 + 4208, local_r13, (uint32_t)((uint32_t)((uint32_t)(0xC0000189ULL))), Arg4);
loc_009B3FD3:
loc_009B3FE1:
    result = CmpTraceHiveFlushStop((uint32_t)((uint32_t)((uint32_t)(0xC0000189ULL))), local_r13, (uint32_t)((uint32_t)((uint32_t)(0xC0000189ULL))), Arg4);
    local_r12 = v_rip - 9798365;
    if ((*(uint32_t *)(v_rip + 0x455F68)) >= = 4) {
        result = v_stack_m168;
        Arg2 = local_rsp - 184 - 112;
        *(uint64_t *)(local_rsp - 0xB8 + 0x30) = result;
        local_r12 = (uint32_t)((v_rip - 9798365) - ((uint32_t)(v_rip - 9898577)));
        result = *(uint16_t *)(v_rip - 0x95DDBC);
        Arg4 = 0;
        *(uint32_t *)(local_rsp - 0xB8 - 0x6C) = (uint32_t)(result);
        Arg3 = 0;
        result = *(uint64_t *)(v_rip + 0x455F3A);
        *(uint64_t *)(local_rsp - 0xB8 + 0x10) = result;
        v_stack_m168 = (uint32_t)((uint32_t)(0xC0000189ULL));
        *(uint32_t *)(local_rsp - 0xB8 + 0x38) = 4;
        *(uint32_t *)(local_rsp - 0xB8 - 0x70) = 0xB000000ULL;
        result = *(uint16_t *)(result);
        *(uint32_t *)(local_rsp - 0xB8 + 0x18) = (uint32_t)(result);
        result = v_rip - 9821670;
        *(uint64_t *)(local_rsp - 0xB8 + 0x20) = result;
        *(uint32_t *)(local_rsp - 0xB8 + 0x1C) = 2;
        *(uint32_t *)(local_rsp - 0xB8 + 0x28) = 23;
        *(uint32_t *)(local_rsp - 0xB8 + 0x2C) = 1;
        v_stack_m158 = (uint32_t)(local_r12);
        result = v_stack_m158;
        Arg1 = *(uint64_t *)(v_rip + 0x455F05);
        result = local_rsp - 184 + 16;
        v_stack_m190 = result;
        v_stack_m198 = 3;
        result = EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (*(uint64_t *)(local_rsp - 0xB8 + 0x80)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
loc_009B40BD:
    if ((((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x38))) & (2)) != 0) goto loc_009B4783;
loc_009B40C6:
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38)))) & (4));
    if (condition_is_not_equal) goto loc_009B44EE;
loc_009B40D3:
    result = CmpIsWriteQueueActive(*(uint64_t *)(v_stack_m28 + 0x48) + 4192, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_009B4815;
    result = CmpGenerateFlushControlData(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38))), v_stack_m160, Arg4);
    if ((*(uint32_t *)(v_rip + 0x455E5B)) >= = 4) {
        result = v_stack_m160;
        Arg1 = v_rip - 9898878;
        Arg2 = local_rsp - 184 - 128;
        Arg4 = 0;
        Arg3 = 0;
        v_stack_m128 = (uint32_t)(result);
        result = v_stack_m128;
        *(uint64_t *)(local_rsp - 0xB8 + 0x60) = result;
        result = v_stack_m158;
        v_stack_m130 = (uint32_t)(result);
        result = v_stack_m130;
        *(uint64_t *)(local_rsp - 0xB8 + 0x70) = result;
        result = *(uint16_t *)(v_rip - 0x95DF3B);
        *(uint32_t *)(local_rsp - 0xB8 - 0x7C) = (uint32_t)(result);
        result = *(uint64_t *)(v_rip + 0x455E0C);
        *(uint64_t *)(local_rsp - 0xB8 + 0x40) = result;
        *(uint32_t *)(local_rsp - 0xB8 + 0x68) = 4;
        *(uint32_t *)(local_rsp - 0xB8 + 0x78) = 4;
        *(uint32_t *)(local_rsp - 0xB8 - 0x80) = 0xB000000ULL;
        result = *(uint16_t *)(result);
        *(uint32_t *)(local_rsp - 0xB8 + 0x48) = (uint32_t)(result);
        result = v_rip - 9822049;
        *(uint64_t *)(local_rsp - 0xB8 + 0x50) = result;
        result = v_rip - 9798792;
        result = (uint32_t)((result) - ((uint32_t)(Arg1)));
        *(uint32_t *)(local_rsp - 0xB8 + 0x4C) = 2;
        *(uint32_t *)(local_rsp - 0xB8 + 0x58) = 63;
        *(uint32_t *)(local_rsp - 0xB8 + 0x5C) = 1;
        v_stack_m138 = (uint32_t)(result);
        result = v_stack_m138;
        Arg1 = *(uint64_t *)(v_rip + 0x455DCD);
        result = local_rsp - 184 + 64;
        v_stack_m168 = result;
        v_stack_m170 = 4;
        result = EtwWriteTransfer(Arg1, Arg2, Arg3, Arg4);
    }
    if ((((uint32_t)((uint32_t)(v_stack_m160))) & (856)) == 0) goto loc_009B4793;
    if ((((uint8_t)((uint32_t)(v_stack_m160))) & (2)) != 0) goto loc_009B44BE;
loc_009B41DD:
    if ((((uint8_t)((uint32_t)(v_stack_m160))) & (1)) != 0) {
        Arg1 = *(uint64_t *)(v_stack_m28 + 0x48) + 4192;
        result = CmpAcquireWriteQueue(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsi = ((((uint32_t)((uint32_t)(v_stack_m160))) & (272)) != 0) ? 1 : 0;
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m160)))) >> (6));
    local_rbx = (uint32_t)((local_rbx) & (1));
    if ((((uint8_t)((uint32_t)(v_stack_m160))) & (8)) != 0) goto loc_009B4479;
    local_r12 = 0;
loc_009B4210:
    if ((((uint32_t)((uint32_t)(v_stack_m160))) & (344)) == 0) goto loc_009B422F;
    result = HvStoreModifiedData(*(uint64_t *)(v_stack_m28 + 0x48), (uint8_t)(local_rsi), (uint8_t)(local_rbx), Arg4);
    if ((uint32_t)(result) != 0) goto loc_009B46CE;
loc_009B422F:
    if (sign_flag) goto loc_009B48A3;
loc_009B4238:
    result = HvUnlockHiveFlusherExclusive(*(uint64_t *)(v_stack_m28 + 0x48), (uint8_t)(local_rsi), (uint8_t)(local_rbx), Arg4);
    result = CmpUnlockRegistry(*(uint64_t *)(v_stack_m28 + 0x48), (uint8_t)(local_rsi), (uint8_t)(local_rbx), Arg4);
    v_stack_m154 = 1;
    if (sign_flag) goto loc_009B4512;
loc_009B425B:
    v_stack_m154 = 2;
    if ((((uint8_t)((uint32_t)(v_stack_m160))) & (8)) == 0) goto loc_009B42A6;
    result = CmpLogFlushPhaseStart(*(uint64_t *)(v_stack_m28 + 0x48), 2, (uint8_t)(local_rbx), Arg4);
    result = HvWriteLogFile(*(uint64_t *)(v_stack_m28 + 0x48), 2, (uint8_t)(local_rbx), v_stack_m140);
    result = CmpLogFlushPhaseEnd(*(uint64_t *)(v_stack_m28 + 0x48), 2, (uint32_t)((uint32_t)(result)), v_stack_m140);
    if (sign_flag) goto loc_009B4336;
    result = HvTruncateCurrentLogFileIfRequired(*(uint64_t *)(v_stack_m28 + 0x48), 2, (uint32_t)((uint32_t)(result)), v_stack_m140);
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m15C)) | (2));
    v_stack_m15C = (uint32_t)(local_rsi);
loc_009B42A6:
    v_stack_m154 = 3;
    if ((((uint8_t)((uint32_t)(v_stack_m160))) & (16)) != 0) goto loc_009B466B;
loc_009B42B9:
    result = CmpLogFlushPhaseStart(*(uint64_t *)(v_stack_m28 + 0x48), 4, (uint32_t)((uint32_t)(result)), v_stack_m140);
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m160)))) & (0x448ULL));
    if (((uint32_t)(result)) == 72) goto loc_009B46A7;
loc_009B42D4:
    result = CmpLogFlushPhaseEnd(*(uint64_t *)(v_stack_m28 + 0x48), 4, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m140);
    if ((((uint8_t)((uint32_t)(v_stack_m160))) & (32)) != 0) goto loc_009B46EA;
loc_009B42EB:
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m160)))) & (69));
    if (((uint8_t)(result)) == 65) goto loc_009B47C6;
loc_009B42F9:
    v_stack_m154 = 5;
    if ((((uint8_t)((uint32_t)(v_stack_m160))) & (64)) != 0) goto loc_009B4592;
loc_009B430C:
    v_stack_m154 = 6;
    if (condition_is_below) goto loc_009B454E;
loc_009B4320:
    if (condition_is_below) goto loc_009B45CB;
loc_009B432B:
    v_stack_m154 = 8;
loc_009B4336:
    result = CmpLockRegistry(*(uint64_t *)(v_stack_m28 + 0x48), 4, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m140);
    result = HvLockHiveFlusherExclusive(*(uint64_t *)(v_stack_m28 + 0x48), 4, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), v_stack_m140);
    if (sign_flag) goto loc_009B48C6;
loc_009B434C:
    if ((((uint8_t)(local_rsi)) & (32)) != 0) {
        *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x1084) = 0;
    }
    if (sign_flag) goto loc_009B48E7;
    if (condition_is_below) goto loc_009B4707;
loc_009B4373:
    if (!(condition_is_above_or_equal)) {
        Arg3 = 1;
        Arg2 = 0;
        Arg1 = 1;
        result = CmpArmLazyWriter(Arg1, Arg2, Arg3, v_stack_m140);
    }
    if ((((uint8_t)((uint32_t)(v_stack_m160))) & (64)) != 0) goto loc_009B44D8;
loc_009B4390:
    if ((((uint32_t)((uint32_t)(v_stack_m160))) & (272)) != 0) {
        Arg1 = *(uint64_t *)(v_stack_m28 + 0x48);
        result = HvFreeUnreconciledData(Arg1, Arg2, Arg3, v_stack_m140);
    }
    if ((((uint8_t)((uint32_t)(v_stack_m160))) & (8)) == 0) goto loc_009B43E4;
    if ((((uint8_t)(local_rsi)) & (4)) != 0) goto loc_009B43E4;
    if ((((uint8_t)(local_rsi)) & (2)) == 0) goto loc_009B4871;
    if ((((uint8_t)((uint32_t)(v_stack_m160))) & (64)) == 0) {
        Arg2 = *(uint64_t *)(v_stack_m28 + 0x48) + 1688;
        Arg1 = *(uint64_t *)(v_stack_m28 + 0x48) + 112;
        result = RtlMergeBitMaps(Arg1, Arg2, Arg3, v_stack_m140);
        Arg1 = *(uint64_t *)(v_stack_m28 + 0x48) + 112;
        result = RtlNumberOfSetBits(Arg1, Arg2, Arg3, v_stack_m140);
        *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x80) = (uint32_t)(result);
    }
    result = HvFreeDirtyData(*(uint64_t *)(v_stack_m28 + 0x48), Arg2, Arg3, v_stack_m140);
loc_009B43E4:
    v_stack_m138 = 0;
    if ((((uint8_t)((uint32_t)(v_stack_m160))) & (1)) != 0) goto loc_009B44AC;
loc_009B43F6:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(v_stack_m160)))) >> (1));
    local_rbx = (uint8_t)((local_rbx) & (1));
    if (0 != 0) {
        Arg2 = *(uint64_t *)(v_stack_m28 + 0x48) + 4192;
        result = CmpReleaseWriteQueue(*(uint64_t *)(v_stack_m28 + 0x48), Arg2, Arg3, v_stack_m140);
        v_stack_m138 = result;
    }
    local_r13 = 0;
    if ((uint8_t)(local_rbx) != 0) {
        Arg2 = *(uint64_t *)(v_stack_m28 + 0x48) + 4208;
        result = CmpReleaseWriteQueue(*(uint64_t *)(v_stack_m28 + 0x48), Arg2, Arg3, v_stack_m140);
        local_r13 = result;
    }
    result = HvUnlockHiveFlusherExclusive(*(uint64_t *)(v_stack_m28 + 0x48), Arg2, Arg3, v_stack_m140);
    result = CmpUnlockRegistry(*(uint64_t *)(v_stack_m28 + 0x48), Arg2, Arg3, v_stack_m140);
    if (0 == 0) goto loc_009B4457;
    if ((((uint8_t)(local_rsi)) & (2)) == 0) goto loc_009B4866;
    Arg3 = 0;
loc_009B4452:
    result = CmpWakeWriteQueueWaiters(*(uint64_t *)(v_stack_m28 + 0x48) + 4192, v_stack_m138, Arg3, v_stack_m140);
loc_009B4457:
    if ((uint8_t)(local_rbx) == 0) goto loc_009B3FD3;
    goto loc_009B3FB7;
loc_009B4464:
    goto loc_009B3FE1;
loc_009B446F:
    result = CmpLockRegistry(*(uint64_t *)(v_stack_m28 + 0x48) + 4192, v_stack_m138, Arg3, v_stack_m140);
    goto loc_009B3F82;
loc_009B4479:
    result = HvLockHiveWriter(*(uint64_t *)(v_stack_m28 + 0x48), v_stack_m138, Arg3, v_stack_m140);
    Arg2 = 0;
    result = HvMarkDirtyForFlush(*(uint64_t *)(v_stack_m28 + 0x48), Arg2, (uint32_t)(0x1000ULL), v_stack_m140);
    local_r12 = 0;
    if (sign_flag) goto loc_009B4852;
    result = HvUnlockHiveWriter(*(uint64_t *)(v_stack_m28 + 0x48), Arg2, (uint32_t)(0x1000ULL), v_stack_m140);
    goto loc_009B4210;
loc_009B44AC:
    if ((((uint8_t)(local_rsi)) & (16)) != 0) goto loc_009B43F6;
    goto loc_009B43F6;
loc_009B44BE:
    result = CmpIsWriteQueueActive(*(uint64_t *)(v_stack_m28 + 0x48) + 4208, Arg2, (uint32_t)(0x1000ULL), v_stack_m140);
    if ((uint8_t)(result) != 0) goto loc_009B4502;
    result = CmpAcquireWriteQueue(*(uint64_t *)(v_stack_m28 + 0x48) + 4208, Arg2, (uint32_t)(0x1000ULL), v_stack_m140);
    goto loc_009B41DD;
loc_009B44D8:
    if (!sign_flag) goto loc_009B4623;
    result = HvFoldBackUnreconciledData(*(uint64_t *)(v_stack_m28 + 0x48), Arg2, (uint32_t)(0x1000ULL), v_stack_m140);
    goto loc_009B4390;
loc_009B44EE:
    result = CmpIsWriteQueueActive(*(uint64_t *)(v_stack_m28 + 0x48) + 4208, Arg2, (uint32_t)(0x1000ULL), v_stack_m140);
    if ((uint8_t)(result) == 0) goto loc_009B40D3;
loc_009B4502:
    result = CmpWaitOnHiveWriteQueue(*(uint64_t *)(v_stack_m28 + 0x48), *(uint64_t *)(v_stack_m28 + 0x48) + 4208, (uint32_t)(0x1000ULL), v_stack_m140);
    goto loc_009B3F6C;
loc_009B4512:
    result = CmpLogFlushPhaseStart(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)((uint32_t)(local_rbx)), (uint32_t)(0x1000ULL), v_stack_m140);
    result = HvExtendHivePrimaryFileValidDataLength(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)(v_stack_m14C), (uint32_t)((uint32_t)(local_r13)), v_stack_m140);
    result = CmpLogFlushPhaseEnd(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(result)), v_stack_m140);
    if (sign_flag) goto loc_009B4336;
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m15C)) | (33));
    v_stack_m15C = (uint32_t)(local_rsi);
    goto loc_009B425B;
loc_009B454E:
    result = CmpLogFlushPhaseStart(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(result)), v_stack_m140);
    result = HvValidateOrInvalidatePrimaryFileHeader(*(uint64_t *)(v_stack_m28 + 0x48), (uint8_t)(local_rbx), (uint8_t)(local_rbx), (uint32_t)((uint32_t)(local_r13)));
    result = CmpLogFlushPhaseEnd(*(uint64_t *)(v_stack_m28 + 0x48), 6, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_r13)));
    if (sign_flag) goto loc_009B4336;
    local_rsi = (uint32_t)((local_rsi) | (32));
    v_stack_m15C = (uint32_t)(local_rsi);
    result = HvTruncateAllLogFilesIfRequired(*(uint64_t *)(v_stack_m28 + 0x48), 6, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_r13)));
    goto loc_009B4320;
loc_009B4592:
    result = CmpLogFlushPhaseStart(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_r13)));
    result = HvWriteHivePrimaryFile(*(uint64_t *)(v_stack_m28 + 0x48), (uint8_t)(local_rbx), (uint32_t)((uint32_t)(local_r13)), (uint32_t)((uint32_t)(local_r13)));
    result = CmpLogFlushPhaseEnd(*(uint64_t *)(v_stack_m28 + 0x48), 5, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_r13)));
    if (sign_flag) goto loc_009B4336;
    local_rsi = (uint32_t)((local_rsi) | (32));
    v_stack_m15C = (uint32_t)(local_rsi);
    goto loc_009B430C;
loc_009B45CB:
    if ((((uint8_t)(local_rsi)) & (32)) != 0) goto loc_009B432B;
    result = CmpLogFlushPhaseStart(*(uint64_t *)(v_stack_m28 + 0x48), 7, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_r13)));
    Arg2 = 0;
    result = CmpFileFlushAndPurge(*(uint64_t *)(v_stack_m28 + 0x48), Arg2, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_r13)));
    if (!(sign_flag)) {
        local_rsi = (uint32_t)((local_rsi) | (32));
        v_stack_m15C = (uint32_t)(local_rsi);
    }
    result = (uint8_t)(((uint32_t)((uint32_t)(local_rsi))) & (32));
    result = (uint8_t)(-(result));
    Arg3 = (uint32_t)(~((uint32_t)((uint32_t)(result))));
    Arg3 = (uint32_t)((Arg3) & (0xC0000001ULL));
    result = CmpLogFlushPhaseEnd(*(uint64_t *)(v_stack_m28 + 0x48), 7, Arg3, (uint32_t)((uint32_t)(local_r13)));
    goto loc_009B432B;
loc_009B4618:
    goto loc_009B3FCE;
loc_009B4623:
    result = HvUnCOWReconciledPages(*(uint64_t *)(v_stack_m28 + 0x48), 7, (uint32_t)(0xC0000001ULL), (uint32_t)((uint32_t)(local_r13)));
    result = HvFreeUnreconciledData(*(uint64_t *)(v_stack_m28 + 0x48), 7, (uint32_t)(0xC0000001ULL), (uint32_t)((uint32_t)(local_r13)));
    if ((((uint8_t)(local_rbx)) & ((uint8_t)((uint32_t)(v_stack_m160)))) == 0) goto loc_009B4754;
    if ((((uint8_t)(local_rsi)) & (16)) != 0) goto loc_009B4754;
    result = HvResetLogFileStatusAll(*(uint64_t *)(v_stack_m28 + 0x48), 7, (uint32_t)(0xC0000001ULL), (uint32_t)((uint32_t)(local_r13)));
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xB4) = 1;
    result = HvIsCurrentLogSwappable(*(uint64_t *)(v_stack_m28 + 0x48), 7, (uint32_t)(0xC0000001ULL), (uint32_t)((uint32_t)(local_r13)));
    if ((uint8_t)(result) == 0) goto loc_009B4390;
    Arg2 = 0;
    result = HvSwapLogFiles(*(uint64_t *)(v_stack_m28 + 0x48), Arg2, (uint32_t)(0xC0000001ULL), (uint32_t)((uint32_t)(local_r13)));
    goto loc_009B4390;
loc_009B466B:
    result = CmpLogFlushPhaseStart(*(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)((uint32_t)(result)), (uint32_t)(0xC0000001ULL), (uint32_t)((uint32_t)(local_r13)));
    Arg2 = 0;
    result = HvValidateOrInvalidatePrimaryFileHeader(*(uint64_t *)(v_stack_m28 + 0x48), Arg2, (uint8_t)(local_rbx), (uint32_t)((uint32_t)(local_r13)));
    result = CmpLogFlushPhaseEnd(*(uint64_t *)(v_stack_m28 + 0x48), 3, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_r13)));
    if (sign_flag) goto loc_009B4843;
    local_rsi = (uint32_t)((local_rsi) | (32));
    v_stack_m15C = (uint32_t)(local_rsi);
    goto loc_009B42B9;
loc_009B46A7:
    result = RtlMergeBitMaps(*(uint64_t *)(v_stack_m28 + 0x48) + 1736, *(uint64_t *)(v_stack_m28 + 0x48) + 1688, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_r13)));
    result = HvFreeDirtyData(*(uint64_t *)(v_stack_m28 + 0x48), *(uint64_t *)(v_stack_m28 + 0x48) + 1688, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_r13)));
    local_rsi = (uint32_t)((local_rsi) | (4));
    v_stack_m15C = (uint32_t)(local_rsi);
    goto loc_009B42D4;
loc_009B46CE:
    result = (uint32_t)((result) - (1));
    if (condition_is_not_equal) goto loc_009B4892;
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m15C)) | (2));
    v_stack_m15C = (uint32_t)(local_rsi);
    goto loc_009B43E4;
loc_009B46EA:
    Arg2 = (uint32_t)(((uint32_t)(v_stack_m158)) >> (2));
    Arg2 = (uint8_t)((Arg2) & ((uint8_t)(local_rbx)));
    result = HvSwapLogFiles(*(uint64_t *)(v_stack_m28 + 0x48), Arg2, (uint32_t)((uint32_t)(result)), (uint32_t)((uint32_t)(local_r13)));
    local_rsi = (uint32_t)((local_rsi) | (8));
    v_stack_m15C = (uint32_t)(local_rsi);
    goto loc_009B42EB;
loc_009B4707:
loc_009B471B:
    if ((*(uint64_t *)((uint32_t)((uint32_t)(result)))) != (*(uint64_t *)((uint32_t)((uint32_t)(result))))) goto loc_009B471B;
    Arg1 = (*(uint64_t *)((uint32_t)((uint32_t)(local_r13)))) - (*(uint64_t *)((uint32_t)((uint32_t)(result))));
    *(void **)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x1030) = Arg1;
    result = *(uint64_t *)((uint32_t)((uint32_t)(result)));
    if (!(condition_is_below)) {
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = (uint32_t)(local_rbx);
        result = CmpArmLazyWriter(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)(local_r13)));
    }
    goto loc_009B4373;
loc_009B4754:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xA8)) - 4)) > ((uint32_t)(local_rbx))) goto loc_009B4390;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xA8))) - (4));
    Arg1 = (uint32_t)(-(Arg1));
    Arg1 = (uint32_t)((Arg1) + (5));
    result = HvpLogTypeToLogArrayIndex(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)(local_r13)));
    *(uint8_t *)((uint32_t)((uint32_t)(result)) + *(uint64_t *)(v_stack_m28 + 0x48) * 1 + 0xC0) = 1;
    goto loc_009B4390;
loc_009B4783:
    result = CmpIsWriteQueueActive(*(uint64_t *)(v_stack_m28 + 0x48) + 4208, Arg2, Arg3, (uint32_t)((uint32_t)(local_r13)));
    if ((uint8_t)(result) == 0) goto loc_009B47A8;
loc_009B4793:
    result = HvUnlockHiveFlusherExclusive(*(uint64_t *)(v_stack_m28 + 0x48), Arg2, Arg3, (uint32_t)((uint32_t)(local_r13)));
    result = CmpUnlockRegistry(*(uint64_t *)(v_stack_m28 + 0x48), Arg2, Arg3, (uint32_t)((uint32_t)(local_r13)));
    local_r15 = 0;
    goto loc_009B3FD3;
loc_009B47A8:
    result = CmpIsWriteQueueActive(*(uint64_t *)(v_stack_m28 + 0x48) + 4192, Arg2, Arg3, (uint32_t)((uint32_t)(local_r13)));
    if ((uint8_t)(result) == 0) goto loc_009B40C6;
    if ((((uint8_t)(local_rbx)) & (4)) == 0) goto loc_009B4793;
    goto loc_009B40C6;
loc_009B47C6:
    result = CmpLockRegistry(*(uint64_t *)(v_stack_m28 + 0x48) + 4192, Arg2, Arg3, (uint32_t)((uint32_t)(local_r13)));
    result = HvLockHiveFlusherExclusive(*(uint64_t *)(v_stack_m28 + 0x48), Arg2, Arg3, (uint32_t)((uint32_t)(local_r13)));
    result = CmpReleaseWriteQueue(*(uint64_t *)(v_stack_m28 + 0x48), *(uint64_t *)(v_stack_m28 + 0x48) + 4192, Arg3, (uint32_t)((uint32_t)(local_r13)));
    Arg3 = (uint32_t)(0xC0000001ULL);
    if ((((uint8_t)((uint32_t)(v_stack_m15C))) & (2)) != 0) { Arg3 = 0; }
    result = CmpWakeWriteQueueWaiters(*(uint64_t *)(v_stack_m28 + 0x48) + 4192, result, Arg3, (uint32_t)((uint32_t)(local_r13)));
    local_rsi = (uint32_t)(((uint32_t)(v_stack_m15C)) | (16));
    v_stack_m15C = (uint32_t)(local_rsi);
    result = HvUnlockHiveFlusherExclusive(*(uint64_t *)(v_stack_m28 + 0x48), result, Arg3, (uint32_t)((uint32_t)(local_r13)));
    result = CmpUnlockRegistry(*(uint64_t *)(v_stack_m28 + 0x48), result, Arg3, (uint32_t)((uint32_t)(local_r13)));
    goto loc_009B42F9;
loc_009B4815:
    if (Arg3 != 0) goto loc_009B487E;
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x68)) == Arg3) goto loc_009B4882;
loc_009B4820:
loc_009B4825:
    result = CmpWaitOnHiveWriteQueue(*(uint64_t *)(v_stack_m28 + 0x48), *(uint64_t *)(v_stack_m28 + 0x48), Arg3, (uint32_t)((uint32_t)(local_r13)));
    if (sign_flag) goto loc_009B3F6C;
    local_r12 = (uint32_t)((1) + (1));
    goto loc_009B3F6C;
loc_009B4843:
    v_stack_m160 = (uint32_t)((uint32_t)(v_stack_m160));
    goto loc_009B4336;
loc_009B4852:
    result = HvUnlockHiveWriter(*(uint64_t *)(v_stack_m28 + 0x48), *(uint64_t *)(v_stack_m28 + 0x48), Arg3, (uint32_t)((uint32_t)(local_r13)));
loc_009B485D:
    goto loc_009B43E4;
loc_009B4866:
    goto loc_009B4452;
loc_009B4871:
    result = HvFoldBackDirtyData(*(uint64_t *)(v_stack_m28 + 0x48), *(uint64_t *)(v_stack_m28 + 0x48), (uint32_t)(0xC0000001ULL), (uint32_t)((uint32_t)(local_r13)));
    goto loc_009B43E4;
loc_009B487E:
    local_rsi = 0;
    goto loc_009B4825;
loc_009B4882:
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0xC3)) == 0) goto loc_009B4825;
    goto loc_009B4820;
loc_009B4892:
    if (((uint32_t)(result)) != 1) goto loc_009B422F;
    goto loc_009B485D;
loc_009B48A3:
    v_stack_m160 = (uint32_t)((uint32_t)(v_stack_m160));
    goto loc_009B4238;
loc_009B48C6:
    if (!sign_flag) goto loc_009B434C;
    if ((((uint8_t)(local_rbx)) & (2)) != 0) goto loc_009B434C;
    *(uint32_t *)(*(uint64_t *)(v_stack_m28 + 0x48) + 0x1084) = (uint32_t)((uint32_t)(v_stack_m150));
    goto loc_009B434C;
loc_009B48E7:
    if (2 == 0) goto loc_009B4386;
    if (condition_is_above_or_equal) goto loc_009B4386;
    local_rsi = (uint32_t)((2) & (0xFFFFFFFDULL));
    v_stack_m15C = (uint32_t)(local_rsi);
    goto loc_009B4386;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `16` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x68` | `32` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x80` | `32` | `W` |
| `Arg1` | `+ 0xA0` | `8` | `R` |
| `Arg1` | `+ 0xA0` | `32` | `R` |
| `Arg1` | `+ 0xA4` | `8` | `R` |
| `Arg1` | `+ 0xA8` | `32` | `R` |
| `Arg1` | `+ 0xAC` | `32` | `R/W` |
| `Arg1` | `+ 0xB4` | `32` | `R/W` |
| `Arg1` | `+ 0xB4` | `32` | `W` |
| `Arg1` | `+ 0xC3` | `8` | `R` |
| `Arg1` | `+ 0x118` | `32` | `R` |
| `Arg1` | `+ 0x608` | `64` | `R` |
| `Arg1` | `+ 0x698` | `64` | `R` |
| `Arg1` | `+ 0x6C8` | `64` | `R` |
| `Arg1` | `+ 0x730` | `64` | `R` |
| `Arg1` | `+ 0x740` | `64` | `R` |
| `Arg1` | `+ 0x1030` | `64` | `W` |
| `Arg1` | `+ 0x1060` | `64` | `R` |
| `Arg1` | `+ 0x1070` | `64` | `R` |
| `Arg1` | `+ 0x1080` | `32` | `R/W` |
| `Arg1` | `+ 0x1084` | `32` | `R` |
| `Arg1` | `+ 0x1084` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009B3DC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
