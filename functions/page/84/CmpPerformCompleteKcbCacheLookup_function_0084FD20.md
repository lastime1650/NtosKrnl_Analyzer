# CmpPerformCompleteKcbCacheLookup

- RVA: `0x0084FD20`–`0x0085126F` (길이 `5,455` bytes)
- VA: `0x000000014084FD20`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069D7C`
- 디코드: `1,280`개 명령, `5,455/5,455` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **100**; 고유 호출 대상: **29**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **15**

### Outgoing calls
- `0x0084FDA6` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0084FE23` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0084FE44` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)
- `0x0084FFF5` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00850010` → [CmpDeleteHive](../86/CmpDeleteHive_function_0086450C.md) (function, `0x0086450C`)
- `0x0085004D` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00850068` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (function, `0x00BC9A1C`)
- `0x0085008F` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00850103` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00850183` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (function, `0x00BC9A1C`)
- `0x008501F5` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x008502B1` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x008502D6` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (function, `0x0042A7F0`)
- `0x0085032B` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0085033E` → [CmpDeleteHive](../86/CmpDeleteHive_function_0086450C.md) (function, `0x0086450C`)
- `0x008503A8` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x008503C9` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x008503D2` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00850423` → [CmpDeleteHive](../86/CmpDeleteHive_function_0086450C.md) (function, `0x0086450C`)
- `0x00850471` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0085048A` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x008504D0` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008504EC` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00850588` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008505C0` → [ExpAcquireFastMutexContended](../../text/45/ExpAcquireFastMutexContended_function_00450288.md) (function, `0x00450288`)
- `0x0085060A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0085063A` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00850669` → [CmpCleanUpKcbCacheWithLock](../86/CmpCleanUpKcbCacheWithLock_function_00861F20.md) (function, `0x00861F20`)
- `0x00850680` → [CmpDecommisssionKcb](../86/CmpDecommisssionKcb_function_00862750.md) (function, `0x00862750`)
- `0x008506C6` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x008506CB` → [CmpArmDelayedCloseTimer](../../text/46/CmpArmDelayedCloseTimer_function_00462DD0.md) (function, `0x00462DD0`)
- `0x008506D3` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x008506E0` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x0085074F` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00850767` → [CmpDeleteHive](../86/CmpDeleteHive_function_0086450C.md) (function, `0x0086450C`)
- `0x00850773` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)
- `0x00850792` → [CmLockHive](../85/CmLockHive_function_008512B4.md) (function, `0x008512B4`)
- `0x008507BF` → [CmUnlockHive](../85/CmUnlockHive_function_00851D6C.md) (function, `0x00851D6C`)
- `0x0085082B` → [CmpReferenceHive](CmpReferenceHive_function_0084FCF0.md) (function, `0x0084FCF0`)
- `0x00850839` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)
- `0x00850843` → [RtlUpcaseUnicodeChar](../85/RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)
- `0x00850867` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00850875` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x008508A0` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x008508BC` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008508EE` → [ExpAcquireFastMutexContended](../../text/45/ExpAcquireFastMutexContended_function_00450288.md) (function, `0x00450288`)
- `0x00850971` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x00850979` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x0085098B` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (function, `0x004F56FC`)
- `0x008509B5` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x008509C3` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008509DF` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00850A03` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00850A1F` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00850A51` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00850A5A` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00850A6A` → [CmpLockHashEntrySharedByKcb](../9F/CmpLockHashEntrySharedByKcb_function_009F52D4.md) (function, `0x009F52D4`)
- `0x00850A72` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (function, `0x00BC9A1C`)
- `0x00850A7A` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00850A9E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00850AC1` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (function, `0x002519C0`)
- `0x00850B6E` → [CmpCleanUpKcbCacheWithLock](../86/CmpCleanUpKcbCacheWithLock_function_00861F20.md) (function, `0x00861F20`)
- `0x00850BB9` → [CmpDereferenceHive](../86/CmpDereferenceHive_function_008632B0.md) (function, `0x008632B0`)
- `0x00850C08` → [CmpGetComponentNameAtIndex](../9A/CmpGetComponentNameAtIndex_function_009A7A50.md) (function, `0x009A7A50`)
- `0x00850C17` → [CmpWaitForHiveMount](../AC/CmpWaitForHiveMount_function_00ACB524.md) (function, `0x00ACB524`)
- `0x00850C4E` → [CmpRecordParseFailure](../85/CmpRecordParseFailure_function_00851280.md) (function, `0x00851280`)
- `0x00850C69` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00850D1E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00850D40` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (function, `0x0042A7F0`)
- `0x00850D92` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x00850D9B` → [CmpDeleteHive](../86/CmpDeleteHive_function_0086450C.md) (function, `0x0086450C`)
- `0x00850DE6` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00850DFF` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00850E45` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x00850E61` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00850EF3` → [CmpAddToDelayedClose](CmpAddToDelayedClose_function_0084FBC0.md) (function, `0x0084FBC0`)
- `0x00850EFB` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00850F08` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00850F74` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x00850F8B` → [CmpDeleteHive](../86/CmpDeleteHive_function_0086450C.md) (function, `0x0086450C`)
- `0x00850F97` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (function, `0x0041B9A0`)
- `0x00850FCA` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x00850FF9` → [CmpCleanUpKcbCacheWithLock](../86/CmpCleanUpKcbCacheWithLock_function_00861F20.md) (function, `0x00861F20`)
- `0x00851014` → [CmpDecommisssionKcb](../86/CmpDecommisssionKcb_function_00862750.md) (function, `0x00862750`)
- `0x00851032` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (function, `0x00BC92C0`)
- `0x00851040` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0085105C` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x00851089` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008510A3` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x008510D5` → [CmLockHive](../85/CmLockHive_function_008512B4.md) (function, `0x008512B4`)
- `0x00851109` → [CmUnlockHive](../85/CmUnlockHive_function_00851D6C.md) (function, `0x00851D6C`)
- `0x00851155` → [CmpReferenceHive](CmpReferenceHive_function_0084FCF0.md) (function, `0x0084FCF0`)
- `0x00851164` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)
- `0x0085116E` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x0085118D` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x008511B1` → [CmpDoQueueLateUnloadWorker](CmpDoQueueLateUnloadWorker_function_0084FB18.md) (function, `0x0084FB18`)
- `0x008511C7` → [CmpCleanUpKcbCacheWithLock](../86/CmpCleanUpKcbCacheWithLock_function_00861F20.md) (function, `0x00861F20`)
- `0x00851216` → [CmpDereferenceHive](../86/CmpDereferenceHive_function_008632B0.md) (function, `0x008632B0`)
- `0x0085123E` → [CmpDoQueueLateUnloadWorker](CmpDoQueueLateUnloadWorker_function_0084FB18.md) (function, `0x0084FB18`)
- `0x00851252` → [RtlUpcaseUnicodeChar](../85/RtlUpcaseUnicodeChar_function_0085F0F0.md) (function, `0x0085F0F0`)

### Direct callers
- [sub_00857A33](../85/Unknown_function_00857A33.md) at `0x00857ACC`
- [CmpDoParseKey](../85/CmpDoParseKey_function_0085F750.md) at `0x0085FA68`

### Static image references
- `0x00850566` → RVA `0x00E0ECC0` (`.data`; read)
- `0x0085057F` → RVA `0x00EF5880` (`.data`; read)
- `0x0085059E` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x008505AB` → RVA `0x00EF5880` (`.data`; read/write)
- `0x008505D7` → RVA `0x00EF5888` (`.data`; write)
- `0x008505E2` → RVA `0x00EF58B0` (`.data`; write)
- `0x00850699` → RVA `0x00EF58E0` (`.data`; write)
- `0x008506A0` → RVA `0x00EEFC30` (`.data`; read)
- `0x008506AD` → RVA `0x00FDA438` (`PAGEDATA`; read/write)
- `0x008506B4` → RVA `0x00E0ECA8` (`.data`; read)
- `0x008506BA` → RVA `0x00EEFC30` (`.data`; write)
- `0x00850946` → RVA `0x00EEFC30` (`.data`; read/write)
- `0x00850AA4` → RVA `0x00EF58E0` (`.data`; read)
- `0x00850BC3` → RVA `0x00EEFB44` (`.data`; read)
- `0x00850BE6` → RVA `0x00EEFB48` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **71**
  - `0x0084FDA6` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x0084FE23` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0084FE44` → [ExfAcquirePushLockSharedEx](../../text/21/ExfAcquirePushLockSharedEx_function_0021044C.md) (`PAGE` → `.text`)
  - `0x0084FFF5` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x0085004D` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00850068` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (`PAGE` → `PAGECMRC`)
  - `0x0085008F` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00850103` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00850183` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (`PAGE` → `PAGECMRC`)
  - `0x008501F5` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x008502B1` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x008502D6` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (`PAGE` → `.text`)
  - `0x0085032B` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x008503A8` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x008503C9` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x008503D2` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x00850471` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0085048A` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x008504D0` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008504EC` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00850588` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008505C0` → [ExpAcquireFastMutexContended](../../text/45/ExpAcquireFastMutexContended_function_00450288.md) (`PAGE` → `.text`)
  - `0x0085060A` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x0085063A` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x008506C6` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (`PAGE` → `.text`)
  - `0x008506CB` → [CmpArmDelayedCloseTimer](../../text/46/CmpArmDelayedCloseTimer_function_00462DD0.md) (`PAGE` → `.text`)
  - `0x008506D3` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x008506E0` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x0085074F` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00850773` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
  - `0x00850839` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (`PAGE` → `.text`)
  - `0x00850867` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00850875` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (`PAGE` → `.text`)
  - `0x008508A0` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x008508BC` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008508EE` → [ExpAcquireFastMutexContended](../../text/45/ExpAcquireFastMutexContended_function_00450288.md) (`PAGE` → `.text`)
  - `0x00850971` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (`PAGE` → `.text`)
  - `0x00850979` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x0085098B` → [KiRaiseIrqlProcessIrqlFlags](../../text/4F/KiRaiseIrqlProcessIrqlFlags_function_004F56FC.md) (`PAGE` → `.text`)
  - `0x008509B5` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x008509C3` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008509DF` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00850A03` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00850A1F` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00850A51` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00850A5A` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x00850A72` → [CmpLockKcbShared](../../pagecmrc/BC/CmpLockKcbShared_function_00BC9A1C.md) (`PAGE` → `PAGECMRC`)
  - `0x00850A7A` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x00850A9E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00850AC1` → [ExReleaseFastMutex](../../text/25/ExReleaseFastMutex_function_002519C0.md) (`PAGE` → `.text`)
  - `0x00850C69` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x00850D1E` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00850D40` → [CmpInitializeDelayDerefContext](../../text/42/CmpInitializeDelayDerefContext_function_0042A7F0.md) (`PAGE` → `.text`)
  - `0x00850D92` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x00850DE6` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00850DFF` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00850E45` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x00850E61` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00850EFB` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x00850F08` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x00850F74` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x00850F97` → [CmpDrainDelayDerefContext](../../text/41/CmpDrainDelayDerefContext_function_0041B9A0.md) (`PAGE` → `.text`)
  - `0x00850FCA` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x00851032` → [CmpUnlockKcb](../../pagecmrc/BC/CmpUnlockKcb_function_00BC92C0.md) (`PAGE` → `PAGECMRC`)
  - `0x00851040` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0085105C` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00851089` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008510A3` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x00851164` → [ExQueueWorkItem](../../text/2F/ExQueueWorkItem_function_002F9520.md) (`PAGE` → `.text`)
  - `0x0085116E` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x0085118D` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0084FD20  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
0084FD25  44 89 44 24 18                  mov dword ptr [rsp + 0x18], r8d
0084FD2A  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
0084FD2E  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0084FD33  53                              push rbx
0084FD34  55                              push rbp
0084FD35  56                              push rsi
0084FD36  57                              push rdi
0084FD37  41 54                           push r12
0084FD39  41 55                           push r13
0084FD3B  41 56                           push r14
0084FD3D  41 57                           push r15
0084FD3F  48 81 EC 98 00 00 00            sub rsp, 0x98
0084FD46  45 33 FF                        xor r15d, r15d
0084FD49  48 89 4C 24 50                  mov qword ptr [rsp + 0x50], rcx
0084FD4E  49 8B F9                        mov rdi, r9
0084FD51  66 44 89 7C 24 34               mov word ptr [rsp + 0x34], r15w
0084FD57  48 8B E9                        mov rbp, rcx
0084FD5A  41 8D 77 01                     lea esi, [r15 + 1]
0084FD5E  4C 8B 6D 20                     mov r13, qword ptr [rbp + 0x20]
0084FD62  41 0F B7 CF                     movzx ecx, r15w
0084FD66  45 32 F6                        xor r14b, r14b
0084FD69  4C 89 6C 24 58                  mov qword ptr [rsp + 0x58], r13
0084FD6E  66 89 4C 24 32                  mov word ptr [rsp + 0x32], cx
0084FD73  48 8B C6                        mov rax, rsi
0084FD76  44 88 74 24 30                  mov byte ptr [rsp + 0x30], r14b
0084FD7B  F0 48 0F C1 45 00               lock xadd qword ptr [rbp], rax
0084FD81  48 83 C0 01                     add rax, 1
0084FD85  0F 84 CA 0A 00 00               je 0x140850855
0084FD8B  48 83 F8 01                     cmp rax, 1
0084FD8F  75 1B                           jne 0x14084fdac
0084FD91  45 33 F6                        xor r14d, r14d
0084FD94  45 33 C9                        xor r9d, r9d
0084FD97  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
0084FD9C  45 33 C0                        xor r8d, r8d
0084FD9F  41 8D 51 15                     lea edx, [r9 + 0x15]
0084FDA3  8D 4A 3C                        lea ecx, [rdx + 0x3c]
0084FDA6  E8 B5 D8 CA FF                  call 0x1404fd660
0084FDAB  CC                              int3
0084FDAC  8B 5D 10                        mov ebx, dword ptr [rbp + 0x10]
0084FDAF  4C 8B FD                        mov r15, rbp
0084FDB2  48 89 6C 24 38                  mov qword ptr [rsp + 0x38], rbp
0084FDB7  44 8B E2                        mov r12d, edx
0084FDBA  44 89 64 24 48                  mov dword ptr [rsp + 0x48], r12d
0084FDBF  45 3B E0                        cmp r12d, r8d
0084FDC2  0F 83 CD 0B 00 00               jae 0x140850995
0084FDC8  41 83 FC 08                     cmp r12d, 8
0084FDCC  0F 83 76 05 00 00               jae 0x140850348
0084FDD2  41 8B C4                        mov eax, r12d
0084FDD5  4C 8D 70 02                     lea r14, [rax + 2]
0084FDD9  8B 04 87                        mov eax, dword ptr [rdi + rax*4]
0084FDDC  49 C1 E6 04                     shl r14, 4
0084FDE0  4C 03 F7                        add r14, rdi
0084FDE3  6B DB 25                        imul ebx, ebx, 0x25
0084FDE6  45 33 C0                        xor r8d, r8d
0084FDE9  33 D2                           xor edx, edx
0084FDEB  03 D8                           add ebx, eax
0084FDED  8B C3                           mov eax, ebx
0084FDEF  C1 E8 09                        shr eax, 9
0084FDF2  33 C3                           xor eax, ebx
0084FDF4  69 C0 A3 8A 01 00               imul eax, eax, 0x18aa3
0084FDFA  8B C8                           mov ecx, eax
0084FDFC  8B E8                           mov ebp, eax
0084FDFE  49 8B 85 70 06 00 00            mov rax, qword ptr [r13 + 0x670]
0084FE05  48 C1 ED 09                     shr rbp, 9
0084FE09  48 33 E9                        xor rbp, rcx
0084FE0C  41 8B 8D 78 06 00 00            mov ecx, dword ptr [r13 + 0x678]
0084FE13  FF C9                           dec ecx
0084FE15  48 23 CD                        and rcx, rbp
0084FE18  48 8D 0C 49                     lea rcx, [rcx + rcx*2]
0084FE1C  48 8D 34 C8                     lea rsi, [rax + rcx*8]
0084FE20  48 8B CE                        mov rcx, rsi
0084FE23  E8 08 04 9C FF                  call 0x140210230
0084FE28  48 8B F8                        mov rdi, rax
0084FE2B  B9 11 00 00 00                  mov ecx, 0x11
0084FE30  33 C0                           xor eax, eax
0084FE32  F0 48 0F B1 0E                  lock cmpxchg qword ptr [rsi], rcx
0084FE37  74 10                           je 0x14084fe49
0084FE39  4C 8B CE                        mov r9, rsi
0084FE3C  4C 8B C7                        mov r8, rdi
0084FE3F  33 D2                           xor edx, edx
0084FE41  48 8B CE                        mov rcx, rsi
0084FE44  E8 03 06 9C FF                  call 0x14021044c
0084FE49  48 85 FF                        test rdi, rdi
0084FE4C  74 04                           je 0x14084fe52
0084FE4E  C6 47 0A 01                     mov byte ptr [rdi + 0xa], 1
0084FE52  41 0F 0D 8D 88 10 00 00         prefetchw byte ptr [r13 + 0x1088]
0084FE5A  41 8B 85 88 10 00 00            mov eax, dword ptr [r13 + 0x1088]
0084FE61  85 C0                           test eax, eax
0084FE63  0F 84 49 05 00 00               je 0x1408503b2
0084FE69  8D 48 01                        lea ecx, [rax + 1]
0084FE6C  F0 41 0F B1 8D 88 10 00 00      lock cmpxchg dword ptr [r13 + 0x1088], ecx
0084FE75  75 EA                           jne 0x14084fe61
0084FE77  41 8B 8D 78 06 00 00            mov ecx, dword ptr [r13 + 0x678]
0084FE7E  45 33 C9                        xor r9d, r9d
0084FE81  49 8B 85 70 06 00 00            mov rax, qword ptr [r13 + 0x670]
0084FE88  FF C9                           dec ecx
0084FE8A  48 23 CD                        and rcx, rbp
0084FE8D  44 89 8C 24 84 00 00 00         mov dword ptr [rsp + 0x84], r9d
0084FE95  48 8D 0C 49                     lea rcx, [rcx + rcx*2]
0084FE99  4C 8B 7C C8 10                  mov r15, qword ptr [rax + rcx*8 + 0x10]
0084FE9E  4D 85 FF                        test r15, r15
0084FEA1  0F 84 EE 01 00 00               je 0x140850095
0084FEA7  41 39 1F                        cmp dword ptr [r15], ebx
0084FEAA  0F 85 AC 01 00 00               jne 0x14085005c
0084FEB0  48 8B 44 24 38                  mov rax, qword ptr [rsp + 0x38]
0084FEB5  49 8D 7F F0                     lea rdi, [r15 - 0x10]
0084FEB9  48 39 47 48                     cmp qword ptr [rdi + 0x48], rax
0084FEBD  0F 85 99 01 00 00               jne 0x14085005c
0084FEC3  48 8B 4F 50                     mov rcx, qword ptr [rdi + 0x50]
0084FEC7  8B 01                           mov eax, dword ptr [rcx]
0084FEC9  48 8D 51 1A                     lea rdx, [rcx + 0x1a]
0084FECD  A8 01                           test al, 1
0084FECF  0F 84 F6 0B 00 00               je 0x140850acb
0084FED5  41 0F B7 36                     movzx esi, word ptr [r14]
0084FED9  4D 8B 6E 08                     mov r13, qword ptr [r14 + 8]
0084FEDD  0F B7 69 18                     movzx ebp, word ptr [rcx + 0x18]
0084FEE1  66 D1 EE                        shr si, 1
0084FEE4  66 85 F6                        test si, si
0084FEE7  74 4F                           je 0x14084ff38
0084FEE9  66 85 ED                        test bp, bp
0084FEEC  74 4A                           je 0x14084ff38
0084FEEE  41 0F B7 4D 00                  movzx ecx, word ptr [r13]
0084FEF3  49 83 C5 02                     add r13, 2
0084FEF7  44 0F B6 22                     movzx r12d, byte ptr [rdx]
0084FEFB  48 FF C2                        inc rdx
0084FEFE  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
0084FF03  66 41 3B CC                     cmp cx, r12w
0084FF07  74 22                           je 0x14084ff2b
0084FF09  66 83 F9 61                     cmp cx, 0x61
0084FF0D  72 12                           jb 0x14084ff21
0084FF0F  66 83 F9 7A                     cmp cx, 0x7a
0084FF13  0F 87 2A 09 00 00               ja 0x140850843
0084FF19  B8 E0 FF 00 00                  mov eax, 0xffe0
0084FF1E  66 03 C8                        add cx, ax
0084FF21  66 41 3B CC                     cmp cx, r12w
0084FF25  0F 85 31 01 00 00               jne 0x14085005c
0084FF2B  B8 FF FF 00 00                  mov eax, 0xffff
0084FF30  66 03 F0                        add si, ax
0084FF33  66 03 E8                        add bp, ax
0084FF36  EB AC                           jmp 0x14084fee4
0084FF38  66 3B F5                        cmp si, bp
0084FF3B  0F 85 1B 01 00 00               jne 0x14085005c
0084FF41  48 85 FF                        test rdi, rdi
0084FF44  0F 84 4B 01 00 00               je 0x140850095
0084FF4A  48 8B 07                        mov rax, qword ptr [rdi]
0084FF4D  0F 1F 00                        nop dword ptr [rax]
0084FF50  48 85 C0                        test rax, rax
0084FF53  0F 84 0C 01 00 00               je 0x140850065
0084FF59  48 8D 48 01                     lea rcx, [rax + 1]
0084FF5D  48 85 C9                        test rcx, rcx
0084FF60  0F 84 25 09 00 00               je 0x14085088b
0084FF66  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
0084FF6B  75 E3                           jne 0x14084ff50
0084FF6D  44 8B 84 24 F0 00 00 00         mov r8d, dword ptr [rsp + 0xf0]
0084FF75  44 8B 64 24 48                  mov r12d, dword ptr [rsp + 0x48]
0084FF7A  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
0084FF7F  41 8D 40 FF                     lea eax, [r8 - 1]
0084FF83  44 3B E0                        cmp r12d, eax
0084FF86  0F 84 A5 03 00 00               je 0x140850331
0084FF8C  8B C3                           mov eax, ebx
0084FF8E  C1 E8 09                        shr eax, 9
0084FF91  33 C3                           xor eax, ebx
0084FF93  69 C0 A3 8A 01 00               imul eax, eax, 0x18aa3
0084FF99  8B C8                           mov ecx, eax
0084FF9B  8B D0                           mov edx, eax
0084FF9D  49 8B 85 70 06 00 00            mov rax, qword ptr [r13 + 0x670]
0084FFA4  48 C1 EA 09                     shr rdx, 9
0084FFA8  48 33 D1                        xor rdx, rcx
0084FFAB  41 8B 8D 78 06 00 00            mov ecx, dword ptr [r13 + 0x678]
0084FFB2  FF C9                           dec ecx
0084FFB4  48 23 D1                        and rdx, rcx
0084FFB7  45 33 C0                        xor r8d, r8d
0084FFBA  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
0084FFBE  48 8D 34 C8                     lea rsi, [rax + rcx*8]
0084FFC2  4C 89 46 08                     mov qword ptr [rsi + 8], r8
0084FFC6  0F 0D 0E                        prefetchw byte ptr [rsi]
0084FFC9  48 8B 06                        mov rax, qword ptr [rsi]
0084FFCC  48 8B C8                        mov rcx, rax
0084FFCF  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0084FFD3  48 83 F9 10                     cmp rcx, 0x10
0084FFD7  48 8D 50 F0                     lea rdx, [rax - 0x10]
0084FFDB  49 0F 46 D0                     cmovbe rdx, r8
0084FFDF  A8 02                           test al, 2
0084FFE1  0F 85 BE 03 00 00               jne 0x1408503a5
0084FFE7  F0 48 0F B1 16                  lock cmpxchg qword ptr [rsi], rdx
0084FFEC  0F 85 B3 03 00 00               jne 0x1408503a5
0084FFF2  48 8B CE                        mov rcx, rsi
0084FFF5  E8 06 16 A9 FF                  call 0x1402e1600
0084FFFA  B8 FF FF FF FF                  mov eax, 0xffffffff
0084FFFF  F0 41 0F C1 85 88 10 00 00      lock xadd dword ptr [r13 + 0x1088], eax
00850008  83 F8 01                        cmp eax, 1
0085000B  75 08                           jne 0x140850015
0085000D  49 8B CD                        mov rcx, r13
00850010  E8 F7 44 01 00                  call 0x14086450c
00850015  44 8B 84 24 F0 00 00 00         mov r8d, dword ptr [rsp + 0xf0]
0085001D  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
00850022  48 C7 C0 FF FF FF FF            mov rax, 0xffffffffffffffff
00850029  F0 48 0F C1 01                  lock xadd qword ptr [rcx], rax
0085002E  48 83 F8 01                     cmp rax, 1
00850032  0F 85 38 03 00 00               jne 0x140850370
00850038  45 33 F6                        xor r14d, r14d
0085003B  45 33 C9                        xor r9d, r9d
0085003E  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00850043  45 33 C0                        xor r8d, r8d
00850046  41 8D 51 1F                     lea edx, [r9 + 0x1f]
0085004A  8D 4A 32                        lea ecx, [rdx + 0x32]
0085004D  E8 0E D6 CA FF                  call 0x1404fd660
00850052  CC                              int3
00850053  66 3B EE                        cmp bp, si
00850056  0F 84 E5 FE FF FF               je 0x14084ff41
0085005C  4D 8B 7F 08                     mov r15, qword ptr [r15 + 8]
00850060  E9 39 FE FF FF                  jmp 0x14084fe9e
00850065  48 8B CF                        mov rcx, rdi
00850068  E8 AF 99 37 00                  call 0x140bc9a1c
0085006D  F7 47 08 00 00 08 00            test dword ptr [rdi + 8], 0x80000
00850074  0F 84 05 08 00 00               je 0x14085087f
0085007A  45 33 ED                        xor r13d, r13d
0085007D  45 33 C9                        xor r9d, r9d
00850080  4C 8B C7                        mov r8, rdi
00850083  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00850088  41 8D 55 20                     lea edx, [r13 + 0x20]
0085008C  8D 4A 31                        lea ecx, [rdx + 0x31]
0085008F  E8 CC D5 CA FF                  call 0x1404fd660
00850094  CC                              int3
00850095  4C 8B 6C 24 58                  mov r13, qword ptr [rsp + 0x58]
0085009A  8B C3                           mov eax, ebx
0085009C  C1 E8 09                        shr eax, 9
0085009F  33 C3                           xor eax, ebx
008500A1  69 C0 A3 8A 01 00               imul eax, eax, 0x18aa3
008500A7  8B C8                           mov ecx, eax
008500A9  8B D0                           mov edx, eax
008500AB  49 8B 85 70 06 00 00            mov rax, qword ptr [r13 + 0x670]
008500B2  48 C1 EA 09                     shr rdx, 9
008500B6  48 33 D1                        xor rdx, rcx
008500B9  41 8B 8D 78 06 00 00            mov ecx, dword ptr [r13 + 0x678]
008500C0  FF C9                           dec ecx
008500C2  48 23 D1                        and rdx, rcx
008500C5  45 33 F6                        xor r14d, r14d
008500C8  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
008500CC  48 8D 1C C8                     lea rbx, [rax + rcx*8]
008500D0  4C 89 73 08                     mov qword ptr [rbx + 8], r14
008500D4  0F 0D 0B                        prefetchw byte ptr [rbx]
008500D7  48 8B 03                        mov rax, qword ptr [rbx]
008500DA  48 8B C8                        mov rcx, rax
008500DD  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
008500E1  48 83 F9 10                     cmp rcx, 0x10
008500E5  48 8D 50 F0                     lea rdx, [rax - 0x10]
008500E9  49 0F 46 D6                     cmovbe rdx, r14
008500ED  A8 02                           test al, 2
008500EF  0F 85 DA 02 00 00               jne 0x1408503cf
008500F5  F0 48 0F B1 13                  lock cmpxchg qword ptr [rbx], rdx
008500FA  0F 85 CF 02 00 00               jne 0x1408503cf
00850100  48 8B CB                        mov rcx, rbx
00850103  E8 F8 14 A9 FF                  call 0x1402e1600
00850108  49 C7 C4 FF FF FF FF            mov r12, 0xffffffffffffffff
0085010F  41 8B C4                        mov eax, r12d
00850112  F0 41 0F C1 85 88 10 00 00      lock xadd dword ptr [r13 + 0x1088], eax
0085011B  83 F8 01                        cmp eax, 1
0085011E  0F 84 17 02 00 00               je 0x14085033b
00850124  4C 8B 7C 24 38                  mov r15, qword ptr [rsp + 0x38]
00850129  0F B7 4C 24 32                  movzx ecx, word ptr [rsp + 0x32]
0085012E  48 8B BC 24 F8 00 00 00         mov rdi, qword ptr [rsp + 0xf8]
00850136  48 8B 6C 24 50                  mov rbp, qword ptr [rsp + 0x50]
0085013B  48 3B AC 24 E0 00 00 00         cmp rbp, qword ptr [rsp + 0xe0]
00850143  74 13                           je 0x140850158
00850145  49 8B C4                        mov rax, r12
00850148  F0 48 0F C1 45 00               lock xadd qword ptr [rbp], rax
0085014E  48 83 F8 01                     cmp rax, 1
00850152  0F 84 E3 FE FF FF               je 0x14085003b
00850158  0F B7 54 24 34                  movzx edx, word ptr [rsp + 0x34]
0085015D  66 03 D1                        add dx, cx
00850160  0F BF C1                        movsx eax, cx
00850163  01 84 24 E8 00 00 00            add dword ptr [rsp + 0xe8], eax
0085016A  41 F7 87 B8 00 00 00 00 00 02 00  test dword ptr [r15 + 0xb8], 0x20000
00850175  66 89 54 24 34                  mov word ptr [rsp + 0x34], dx
0085017A  0F 84 5C 02 00 00               je 0x1408503dc
00850180  49 8B CF                        mov rcx, r15
00850183  E8 94 98 37 00                  call 0x140bc9a1c
00850188  41 F7 87 B8 00 00 00 00 00 02 00  test dword ptr [r15 + 0xb8], 0x20000
00850193  0F 84 CB 10 00 00               je 0x140851264
00850199  49 8B 6F 68                     mov rbp, qword ptr [r15 + 0x68]
0085019D  BE 01 00 00 00                  mov esi, 1
008501A2  48 89 6C 24 50                  mov qword ptr [rsp + 0x50], rbp
008501A7  8B C6                           mov eax, esi
008501A9  F0 48 0F C1 45 00               lock xadd qword ptr [rbp], rax
008501AF  48 03 C6                        add rax, rsi
008501B2  0F 84 87 08 00 00               je 0x140850a3f
008501B8  48 3B C6                        cmp rax, rsi
008501BB  0F 84 D3 FB FF FF               je 0x14084fd94
008501C1  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
008501C5  8B 81 A0 00 00 00               mov eax, dword ptr [rcx + 0xa0]
008501CB  A8 20                           test al, 0x20
008501CD  74 16                           je 0x1408501e5
008501CF  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008501D8  48 39 81 48 10 00 00            cmp qword ptr [rcx + 0x1048], rax
008501DF  0F 85 DE 09 00 00               jne 0x140850bc3
008501E5  F7 45 08 00 00 04 00            test dword ptr [rbp + 8], 0x40000
008501EC  0F 85 44 0A 00 00               jne 0x140850c36
008501F2  49 8B CF                        mov rcx, r15
008501F5  E8 C6 90 37 00                  call 0x140bc92c0
008501FA  44 0F B6 74 24 30               movzx r14d, byte ptr [rsp + 0x30]
00850200  45 33 ED                        xor r13d, r13d
00850203  45 84 F6                        test r14b, r14b
00850206  0F 84 BD 00 00 00               je 0x1408502c9
0085020C  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
00850210  8B C8                           mov ecx, eax
00850212  49 8B 7F 20                     mov rdi, qword ptr [r15 + 0x20]
00850216  C1 E9 09                        shr ecx, 9
00850219  33 C8                           xor ecx, eax
0085021B  69 C1 A3 8A 01 00               imul eax, ecx, 0x18aa3
00850221  8B C8                           mov ecx, eax
00850223  8B D0                           mov edx, eax
00850225  48 8B 87 70 06 00 00            mov rax, qword ptr [rdi + 0x670]
0085022C  48 C1 EA 09                     shr rdx, 9
00850230  48 33 D1                        xor rdx, rcx
00850233  8B 8F 78 06 00 00               mov ecx, dword ptr [rdi + 0x678]
00850239  FF C9                           dec ecx
0085023B  48 23 D1                        and rdx, rcx
0085023E  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
00850242  4C 89 6C C8 08                  mov qword ptr [rax + rcx*8 + 8], r13
00850247  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
0085024B  8B C8                           mov ecx, eax
0085024D  4D 8B 47 20                     mov r8, qword ptr [r15 + 0x20]
00850251  C1 E9 09                        shr ecx, 9
00850254  33 C8                           xor ecx, eax
00850256  69 C1 A3 8A 01 00               imul eax, ecx, 0x18aa3
0085025C  8B C8                           mov ecx, eax
0085025E  8B D0                           mov edx, eax
00850260  49 8B 80 70 06 00 00            mov rax, qword ptr [r8 + 0x670]
00850267  48 C1 EA 09                     shr rdx, 9
0085026B  48 33 D1                        xor rdx, rcx
0085026E  41 8B 88 78 06 00 00            mov ecx, dword ptr [r8 + 0x678]
00850275  FF C9                           dec ecx
00850277  48 23 D1                        and rdx, rcx
0085027A  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
0085027E  48 8D 1C C8                     lea rbx, [rax + rcx*8]
00850282  0F 0D 0B                        prefetchw byte ptr [rbx]
00850285  48 8B 03                        mov rax, qword ptr [rbx]
00850288  48 8B C8                        mov rcx, rax
0085028B  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0085028F  48 83 F9 10                     cmp rcx, 0x10
00850293  48 8D 50 F0                     lea rdx, [rax - 0x10]
00850297  49 0F 46 D5                     cmovbe rdx, r13
0085029B  A8 02                           test al, 2
0085029D  0F 85 94 03 00 00               jne 0x140850637
008502A3  F0 48 0F B1 13                  lock cmpxchg qword ptr [rbx], rdx
008502A8  0F 85 89 03 00 00               jne 0x140850637
008502AE  48 8B CB                        mov rcx, rbx
008502B1  E8 4A 13 A9 FF                  call 0x1402e1600
008502B6  41 8B C4                        mov eax, r12d
008502B9  F0 0F C1 87 88 10 00 00         lock xadd dword ptr [rdi + 0x1088], eax
008502C1  3B C6                           cmp eax, esi
008502C3  0F 84 57 01 00 00               je 0x140850420
008502C9  0F 57 C0                        xorps xmm0, xmm0
008502CC  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
008502D1  0F 11 44 24 60                  movups xmmword ptr [rsp + 0x60], xmm0
008502D6  E8 15 A5 BD FF                  call 0x14042a7f0
008502DB  49 8B 5F 20                     mov rbx, qword ptr [r15 + 0x20]
008502DF  49 8B 0F                        mov rcx, qword ptr [r15]
008502E2  48 3B CE                        cmp rcx, rsi
008502E5  0F 86 42 01 00 00               jbe 0x14085042d
008502EB  48 8D 51 FF                     lea rdx, [rcx - 1]
008502EF  48 83 FA 02                     cmp rdx, 2
008502F3  0F 84 17 03 00 00               je 0x140850610
008502F9  45 32 C0                        xor r8b, r8b
008502FC  48 8B C1                        mov rax, rcx
008502FF  F0 49 0F B1 17                  lock cmpxchg qword ptr [r15], rdx
00850304  48 8B C8                        mov rcx, rax
00850307  48 8D 42 01                     lea rax, [rdx + 1]
0085030B  48 3B C8                        cmp rcx, rax
0085030E  75 D2                           jne 0x1408502e2
00850310  48 3B CA                        cmp rcx, rdx
00850313  0F 83 71 04 00 00               jae 0x14085078a
00850319  45 33 C9                        xor r9d, r9d
0085031C  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00850321  4D 8B C7                        mov r8, r15
00850324  41 8D 51 25                     lea edx, [r9 + 0x25]
00850328  8D 4A 2C                        lea ecx, [rdx + 0x2c]
0085032B  E8 30 D3 CA FF                  call 0x1404fd660
00850330  CC                              int3
00850331  C6 44 24 30 01                  mov byte ptr [rsp + 0x30], 1
00850336  E9 E2 FC FF FF                  jmp 0x14085001d
0085033B  49 8B CD                        mov rcx, r13
0085033E  E8 C9 41 01 00                  call 0x14086450c
00850343  E9 DC FD FF FF                  jmp 0x140850124
00850348  41 8D 44 24 F8                  lea eax, [r12 - 8]
0085034D  44 8B F0                        mov r14d, eax
00850350  8B C8                           mov ecx, eax
00850352  49 83 C6 06                     add r14, 6
00850356  48 8B 87 A0 00 00 00            mov rax, qword ptr [rdi + 0xa0]
0085035D  49 C1 E6 04                     shl r14, 4
00850361  4C 03 B7 A0 00 00 00            add r14, qword ptr [rdi + 0xa0]
00850368  8B 04 88                        mov eax, dword ptr [rax + rcx*4]
0085036B  E9 73 FA FF FF                  jmp 0x14084fde3
00850370  0F B7 4C 24 32                  movzx ecx, word ptr [rsp + 0x32]
00850375  4C 8B FF                        mov r15, rdi
00850378  66 FF C1                        inc cx
0085037B  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00850380  F7 87 B8 00 00 00 00 00 10 00   test dword ptr [rdi + 0xb8], 0x100000
0085038A  48 8B BC 24 F8 00 00 00         mov rdi, qword ptr [rsp + 0xf8]
00850392  66 89 4C 24 32                  mov word ptr [rsp + 0x32], cx
00850397  0F 85 F8 05 00 00               jne 0x140850995
0085039D  41 FF C4                        inc r12d
008503A0  E9 15 FA FF FF                  jmp 0x14084fdba
008503A5  48 8B CE                        mov rcx, rsi
008503A8  E8 23 35 A1 FF                  call 0x1402638d0
008503AD  E9 40 FC FF FF                  jmp 0x14084fff2
008503B2  41 B9 09 00 00 00               mov r9d, 9
008503B8  8B C3                           mov eax, ebx
008503BA  4D 8B C5                        mov r8, r13
008503BD  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
008503C2  41 8D 51 0E                     lea edx, [r9 + 0xe]
008503C6  8D 4A 3A                        lea ecx, [rdx + 0x3a]
008503C9  E8 92 D2 CA FF                  call 0x1404fd660
008503CE  CC                              int3
008503CF  48 8B CB                        mov rcx, rbx
008503D2  E8 F9 34 A1 FF                  call 0x1402638d0
008503D7  E9 24 FD FF FF                  jmp 0x140850100
008503DC  44 0F B6 74 24 30               movzx r14d, byte ptr [rsp + 0x30]
008503E2  48 8B 84 24 08 01 00 00         mov rax, qword ptr [rsp + 0x108]
008503EA  45 33 ED                        xor r13d, r13d
008503ED  41 8B F5                        mov esi, r13d
008503F0  4C 89 38                        mov qword ptr [rax], r15
008503F3  48 8B 84 24 10 01 00 00         mov rax, qword ptr [rsp + 0x110]
008503FB  44 88 30                        mov byte ptr [rax], r14b
008503FE  48 8B 84 24 18 01 00 00         mov rax, qword ptr [rsp + 0x118]
00850406  66 89 10                        mov word ptr [rax], dx
00850409  8B C6                           mov eax, esi
0085040B  48 81 C4 98 00 00 00            add rsp, 0x98
00850412  41 5F                           pop r15
00850414  41 5E                           pop r14
00850416  41 5D                           pop r13
00850418  41 5C                           pop r12
0085041A  5F                              pop rdi
0085041B  5E                              pop rsi
0085041C  5D                              pop rbp
0085041D  5B                              pop rbx
0085041E  C3                              ret
0085041F  CC                              int3
00850420  48 8B CF                        mov rcx, rdi
00850423  E8 E4 40 01 00                  call 0x14086450c
00850428  E9 9C FE FF FF                  jmp 0x1408502c9
0085042D  45 8B 77 10                     mov r14d, dword ptr [r15 + 0x10]
00850431  45 33 C0                        xor r8d, r8d
00850434  49 8B 5F 20                     mov rbx, qword ptr [r15 + 0x20]
00850438  41 8B C6                        mov eax, r14d
0085043B  C1 E8 09                        shr eax, 9
0085043E  41 33 C6                        xor eax, r14d
00850441  69 C0 A3 8A 01 00               imul eax, eax, 0x18aa3
00850447  8B C8                           mov ecx, eax
00850449  8B D0                           mov edx, eax
0085044B  48 8B 83 70 06 00 00            mov rax, qword ptr [rbx + 0x670]
00850452  48 C1 EA 09                     shr rdx, 9
00850456  48 33 D1                        xor rdx, rcx
00850459  8B 8B 78 06 00 00               mov ecx, dword ptr [rbx + 0x678]
0085045F  FF C9                           dec ecx
00850461  48 23 D1                        and rdx, rcx
00850464  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
00850468  33 D2                           xor edx, edx
0085046A  48 8D 3C C8                     lea rdi, [rax + rcx*8]
0085046E  48 8B CF                        mov rcx, rdi
00850471  E8 BA FD 9B FF                  call 0x140210230
00850476  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
0085047C  48 8B F0                        mov rsi, rax
0085047F  73 0E                           jae 0x14085048f
00850481  4C 8B C7                        mov r8, rdi
00850484  48 8B D0                        mov rdx, rax
00850487  48 8B CF                        mov rcx, rdi
0085048A  E8 01 F8 9B FF                  call 0x14020fc90
0085048F  48 85 F6                        test rsi, rsi
00850492  74 04                           je 0x140850498
00850494  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
00850498  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008504A1  48 89 47 08                     mov qword ptr [rdi + 8], rax
008504A5  0F 0D 8B 88 10 00 00            prefetchw byte ptr [rbx + 0x1088]
008504AC  8B 83 88 10 00 00               mov eax, dword ptr [rbx + 0x1088]
008504B2  85 C0                           test eax, eax
008504B4  0F 84 CF 05 00 00               je 0x140850a89
008504BA  8D 48 01                        lea ecx, [rax + 1]
008504BD  F0 0F B1 8B 88 10 00 00         lock cmpxchg dword ptr [rbx + 0x1088], ecx
008504C5  75 EB                           jne 0x1408504b2
008504C7  45 33 C0                        xor r8d, r8d
008504CA  49 8D 4F 30                     lea rcx, [r15 + 0x30]
008504CE  33 D2                           xor edx, edx
008504D0  E8 5B FD 9B FF                  call 0x140210230
008504D5  F0 49 0F BA 6F 30 00            lock bts qword ptr [r15 + 0x30], 0
008504DC  48 8B F0                        mov rsi, rax
008504DF  73 10                           jae 0x1408504f1
008504E1  4D 8D 47 30                     lea r8, [r15 + 0x30]
008504E5  48 8B D0                        mov rdx, rax
008504E8  49 8D 4F 30                     lea rcx, [r15 + 0x30]
008504EC  E8 9F F7 9B FF                  call 0x14020fc90
008504F1  48 85 F6                        test rsi, rsi
008504F4  74 04                           je 0x1408504fa
008504F6  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
008504FA  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00850503  49 8B FD                        mov rdi, r13
00850506  49 89 47 38                     mov qword ptr [r15 + 0x38], rax
0085050A  49 8B 87 C0 00 00 00            mov rax, qword ptr [r15 + 0xc0]
00850511  48 85 C0                        test rax, rax
00850514  0F 85 87 04 00 00               jne 0x1408509a1
0085051A  49 8B 4F 20                     mov rcx, qword ptr [r15 + 0x20]
0085051E  49 8B C4                        mov rax, r12
00850521  F0 49 0F C1 07                  lock xadd qword ptr [r15], rax
00850526  48 FF C8                        dec rax
00850529  48 83 F8 02                     cmp rax, 2
0085052D  0F 84 60 0C 00 00               je 0x140851193
00850533  48 85 C0                        test rax, rax
00850536  0F 85 94 01 00 00               jne 0x1408506d0
0085053C  41 F7 87 B8 00 00 00 00 00 04 00  test dword ptr [r15 + 0xb8], 0x40000
00850547  0F 85 15 06 00 00               jne 0x140850b62
0085054D  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
00850551  41 8B D5                        mov edx, r13d
00850554  8B C8                           mov ecx, eax
00850556  C1 E8 11                        shr eax, 0x11
00850559  F6 D0                           not al
0085055B  24 01                           and al, 1
0085055D  F6 C1 20                        test cl, 0x20
00850560  0F B6 C0                        movzx eax, al
00850563  0F 44 D0                        cmove edx, eax
00850566  8B 05 54 E7 5B 00               mov eax, dword ptr [rip + 0x5be754]
0085056C  85 C0                           test eax, eax
0085056E  0F 85 D0 00 00 00               jne 0x140850644
00850574  84 D2                           test dl, dl
00850576  0F 84 E5 00 00 00               je 0x140850661
0085057C  45 33 C0                        xor r8d, r8d
0085057F  48 8D 0D FA 52 6A 00            lea rcx, [rip + 0x6a52fa]
00850586  33 D2                           xor edx, edx
00850588  E8 A3 FC 9B FF                  call 0x140210230
0085058D  48 8B F0                        mov rsi, rax
00850590  44 0F 20 C5                     mov rbp, cr8
00850594  41 B8 01 00 00 00               mov r8d, 1
0085059A  45 0F 22 C0                     mov cr8, r8
0085059E  83 3D 7B 67 77 00 00            cmp dword ptr [rip + 0x77677b], 0
008505A5  0F 85 C2 02 00 00               jne 0x14085086d
008505AB  F0 0F BA 35 CC 52 6A 00 00      lock btr dword ptr [rip + 0x6a52cc], 0
008505B4  72 0F                           jb 0x1408505c5
008505B6  48 8B D6                        mov rdx, rsi
008505B9  48 8D 0D C0 52 6A 00            lea rcx, [rip + 0x6a52c0]
008505C0  E8 C3 FC BF FF                  call 0x140450288
008505C5  48 85 F6                        test rsi, rsi
008505C8  74 04                           je 0x1408505ce
008505CA  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
008505CE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008505D7  48 89 05 AA 52 6A 00            mov qword ptr [rip + 0x6a52aa], rax
008505DE  40 0F B6 C5                     movzx eax, bpl
008505E2  89 05 C8 52 6A 00               mov dword ptr [rip + 0x6a52c8], eax
008505E8  49 8D 87 E0 00 00 00            lea rax, [r15 + 0xe0]
008505EF  48 39 00                        cmp qword ptr [rax], rax
008505F2  0F 84 AC 04 00 00               je 0x140850aa4
008505F8  45 33 C9                        xor r9d, r9d
008505FB  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00850600  4D 8B C7                        mov r8, r15
00850603  41 8D 51 34                     lea edx, [r9 + 0x34]
00850607  8D 4A 1D                        lea ecx, [rdx + 0x1d]
0085060A  E8 51 D0 CA FF                  call 0x1404fd660
0085060F  CC                              int3
00850610  41 F7 87 B8 00 00 00 00 00 04 00  test dword ptr [r15 + 0xb8], 0x40000
0085061B  0F 84 D8 FC FF FF               je 0x1408502f9
00850621  40 38 B3 80 0B 00 00            cmp byte ptr [rbx + 0xb80], sil
00850628  0F 85 CB FC FF FF               jne 0x1408502f9
0085062E  44 0F B6 C6                     movzx r8d, sil
00850632  E9 C5 FC FF FF                  jmp 0x1408502fc
00850637  48 8B CB                        mov rcx, rbx
0085063A  E8 91 32 A1 FF                  call 0x1402638d0
0085063F  E9 6A FC FF FF                  jmp 0x1408502ae
00850644  41 0F B7 87 BA 00 00 00         movzx eax, word ptr [r15 + 0xba]
0085064C  A8 10                           test al, 0x10
0085064E  0F 94 C1                        sete cl
00850651  41 F6 47 08 08                  test byte ptr [r15 + 8], 8
00850656  0F 94 C0                        sete al
00850659  84 C8                           test al, cl
0085065B  0F 84 13 FF FF FF               je 0x140850574
00850661  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00850666  49 8B CF                        mov rcx, r15
00850669  E8 B2 18 01 00                  call 0x140861f20
0085066E  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00850677  49 39 47 38                     cmp qword ptr [r15 + 0x38], rax
0085067B  74 53                           je 0x1408506d0
0085067D  49 8B CF                        mov rcx, r15
00850680  E8 CB 20 01 00                  call 0x140862750
00850685  EB 49                           jmp 0x1408506d0
00850687  48 89 08                        mov qword ptr [rax], rcx
0085068A  48 89 50 08                     mov qword ptr [rax + 8], rdx
0085068E  48 89 41 08                     mov qword ptr [rcx + 8], rax
00850692  48 8D 0D E7 51 6A 00            lea rcx, [rip + 0x6a51e7]
00850699  48 89 05 40 52 6A 00            mov qword ptr [rip + 0x6a5240], rax
008506A0  8B 05 8A F5 69 00               mov eax, dword ptr [rip + 0x69f58a]
008506A6  41 80 4F 40 02                  or byte ptr [r15 + 0x40], 2
008506AB  FF C0                           inc eax
008506AD  48 FF 05 84 9D 78 00            inc qword ptr [rip + 0x789d84]
008506B4  3B 05 EE E5 5B 00               cmp eax, dword ptr [rip + 0x5be5ee]
008506BA  89 05 70 F5 69 00               mov dword ptr [rip + 0x69f570], eax
008506C0  0F 86 FB 03 00 00               jbe 0x140850ac1
008506C6  E8 F5 12 A0 FF                  call 0x1402519c0
008506CB  E8 00 27 C1 FF                  call 0x140462dd0
008506D0  49 8B CF                        mov rcx, r15
008506D3  E8 E8 8B 37 00                  call 0x140bc92c0
008506D8  48 85 FF                        test rdi, rdi
008506DB  74 08                           je 0x1408506e5
008506DD  48 8B CF                        mov rcx, rdi
008506E0  E8 DB 8B 37 00                  call 0x140bc92c0
008506E5  41 8B C6                        mov eax, r14d
008506E8  C1 E8 09                        shr eax, 9
008506EB  41 33 C6                        xor eax, r14d
008506EE  69 C0 A3 8A 01 00               imul eax, eax, 0x18aa3
008506F4  8B C8                           mov ecx, eax
008506F6  8B D0                           mov edx, eax
008506F8  48 8B 83 70 06 00 00            mov rax, qword ptr [rbx + 0x670]
008506FF  48 C1 EA 09                     shr rdx, 9
00850703  48 33 D1                        xor rdx, rcx
00850706  8B 8B 78 06 00 00               mov ecx, dword ptr [rbx + 0x678]
0085070C  FF C9                           dec ecx
0085070E  48 23 D1                        and rdx, rcx
00850711  45 33 FF                        xor r15d, r15d
00850714  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
00850718  48 8D 3C C8                     lea rdi, [rax + rcx*8]
0085071C  4C 89 7F 08                     mov qword ptr [rdi + 8], r15
00850720  0F 0D 0F                        prefetchw byte ptr [rdi]
00850723  48 8B 07                        mov rax, qword ptr [rdi]
00850726  48 8B C8                        mov rcx, rax
00850729  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
0085072D  48 83 F9 10                     cmp rcx, 0x10
00850731  48 8D 50 F0                     lea rdx, [rax - 0x10]
00850735  49 0F 46 D7                     cmovbe rdx, r15
00850739  A8 02                           test al, 2
0085073B  0F 85 16 03 00 00               jne 0x140850a57
00850741  F0 48 0F B1 17                  lock cmpxchg qword ptr [rdi], rdx
00850746  0F 85 0B 03 00 00               jne 0x140850a57
0085074C  48 8B CF                        mov rcx, rdi
0085074F  E8 AC 0E A9 FF                  call 0x1402e1600
00850754  41 8B C4                        mov eax, r12d
00850757  F0 0F C1 83 88 10 00 00         lock xadd dword ptr [rbx + 0x1088], eax
0085075F  83 F8 01                        cmp eax, 1
00850762  75 08                           jne 0x14085076c
00850764  48 8B CB                        mov rcx, rbx
00850767  E8 A0 3D 01 00                  call 0x14086450c
0085076C  33 D2                           xor edx, edx
0085076E  48 8D 4C 24 60                  lea rcx, [rsp + 0x60]
00850773  E8 28 B2 BC FF                  call 0x14041b9a0
00850778  48 8B 6C 24 50                  mov rbp, qword ptr [rsp + 0x50]
0085077D  BE 01 00 00 00                  mov esi, 1
00850782  44 0F B6 74 24 30               movzx r14d, byte ptr [rsp + 0x30]
00850788  EB 3D                           jmp 0x1408507c7
0085078A  45 84 C0                        test r8b, r8b
0085078D  74 35                           je 0x1408507c4
0085078F  48 8B CB                        mov rcx, rbx
00850792  E8 1D 0B 00 00                  call 0x1408512b4
00850797  8B C6                           mov eax, esi
00850799  F0 0F C1 83 8C 10 00 00         lock xadd dword ptr [rbx + 0x108c], eax
008507A1  83 E0 7F                        and eax, 0x7f
008507A4  C7 84 83 90 10 00 00 13 00 00 00  mov dword ptr [rbx + rax*4 + 0x1090], 0x13
008507AF  48 8B 83 78 0B 00 00            mov rax, qword ptr [rbx + 0xb78]
008507B6  48 83 38 02                     cmp qword ptr [rax], 2
008507BA  74 30                           je 0x1408507ec
008507BC  48 8B CB                        mov rcx, rbx
008507BF  E8 A8 15 00 00                  call 0x140851d6c
008507C4  45 33 FF                        xor r15d, r15d
008507C7  45 84 F6                        test r14b, r14b
008507CA  0F 85 94 02 00 00               jne 0x140850a64
008507D0  44 8B 84 24 F0 00 00 00         mov r8d, dword ptr [rsp + 0xf0]
008507D8  48 8B BC 24 F8 00 00 00         mov rdi, qword ptr [rsp + 0xf8]
008507E0  8B 94 24 E8 00 00 00            mov edx, dword ptr [rsp + 0xe8]
008507E7  E9 72 F5 FF FF                  jmp 0x14084fd5e
008507EC  8B C6                           mov eax, esi
008507EE  F0 0F C1 83 8C 10 00 00         lock xadd dword ptr [rbx + 0x108c], eax
008507F6  83 E0 7F                        and eax, 0x7f
008507F9  C7 84 83 90 10 00 00 14 00 00 00  mov dword ptr [rbx + rax*4 + 0x1090], 0x14
00850804  33 C0                           xor eax, eax
00850806  F0 0F B1 B3 C0 12 00 00         lock cmpxchg dword ptr [rbx + 0x12c0], esi
0085080E  75 AC                           jne 0x1408507bc
00850810  8B C6                           mov eax, esi
00850812  F0 0F C1 83 8C 10 00 00         lock xadd dword ptr [rbx + 0x108c], eax
0085081A  83 E0 7F                        and eax, 0x7f
0085081D  48 8B CB                        mov rcx, rbx
00850820  C7 84 83 90 10 00 00 15 00 00 00  mov dword ptr [rbx + rax*4 + 0x1090], 0x15
0085082B  E8 C0 F4 FF FF                  call 0x14084fcf0
00850830  48 8B 8B D0 12 00 00            mov rcx, qword ptr [rbx + 0x12d0]
00850837  8B D6                           mov edx, esi
00850839  E8 E2 8C AA FF                  call 0x1402f9520
0085083E  E9 79 FF FF FF                  jmp 0x1408507bc
00850843  E8 A8 E8 00 00                  call 0x14085f0f0
00850848  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
0085084D  0F B7 C8                        movzx ecx, ax
00850850  E9 CC F6 FF FF                  jmp 0x14084ff21
00850855  45 33 C9                        xor r9d, r9d
00850858  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
0085085D  4C 8B C5                        mov r8, rbp
00850860  41 8D 51 24                     lea edx, [r9 + 0x24]
00850864  8D 4A 2D                        lea ecx, [rdx + 0x2d]
00850867  E8 F4 CD CA FF                  call 0x1404fd660
0085086C  CC                              int3
0085086D  41 0F B6 D0                     movzx edx, r8b
00850871  40 0F B6 CD                     movzx ecx, bpl
00850875  E8 82 4E CA FF                  call 0x1404f56fc
0085087A  E9 2C FD FF FF                  jmp 0x1408505ab
0085087F  41 BE 01 00 00 00               mov r14d, 1
00850885  F0 48 FF 07                     lock inc qword ptr [rdi]
00850889  75 1B                           jne 0x1408508a6
0085088B  45 33 ED                        xor r13d, r13d
0085088E  45 33 C9                        xor r9d, r9d
00850891  4C 8B C7                        mov r8, rdi
00850894  4C 89 6C 24 20                  mov qword ptr [rsp + 0x20], r13
00850899  41 8D 55 24                     lea edx, [r13 + 0x24]
0085089D  8D 4A 2D                        lea ecx, [rdx + 0x2d]
008508A0  E8 BB CD CA FF                  call 0x1404fd660
008508A5  CC                              int3
008508A6  F6 47 40 02                     test byte ptr [rdi + 0x40], 2
008508AA  0F 84 C6 00 00 00               je 0x140850976
008508B0  45 33 C0                        xor r8d, r8d
008508B3  48 8D 0D C6 4F 6A 00            lea rcx, [rip + 0x6a4fc6]
008508BA  33 D2                           xor edx, edx
008508BC  E8 6F F9 9B FF                  call 0x140210230
008508C1  48 8B F0                        mov rsi, rax
008508C4  44 0F 20 C5                     mov rbp, cr8
008508C8  45 0F 22 C6                     mov cr8, r14
008508CC  83 3D 4D 64 77 00 00            cmp dword ptr [rip + 0x77644d], 0
008508D3  0F 85 AA 00 00 00               jne 0x140850983
008508D9  F0 0F BA 35 9E 4F 6A 00 00      lock btr dword ptr [rip + 0x6a4f9e], 0
008508E2  72 0F                           jb 0x1408508f3
008508E4  48 8B D6                        mov rdx, rsi
008508E7  48 8D 0D 92 4F 6A 00            lea rcx, [rip + 0x6a4f92]
008508EE  E8 95 F9 BF FF                  call 0x140450288
008508F3  48 85 F6                        test rsi, rsi
008508F6  74 04                           je 0x1408508fc
008508F8  44 88 76 0A                     mov byte ptr [rsi + 0xa], r14b
008508FC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00850905  48 89 05 7C 4F 6A 00            mov qword ptr [rip + 0x6a4f7c], rax
0085090C  40 0F B6 C5                     movzx eax, bpl
00850910  89 05 9A 4F 6A 00               mov dword ptr [rip + 0x6a4f9a], eax
00850916  0F B6 47 40                     movzx eax, byte ptr [rdi + 0x40]
0085091A  A8 02                           test al, 2
0085091C  74 4C                           je 0x14085096a
0085091E  48 8D 8F E0 00 00 00            lea rcx, [rdi + 0xe0]
00850925  A8 04                           test al, 4
00850927  0F 85 26 02 00 00               jne 0x140850b53
0085092D  48 8B 11                        mov rdx, qword ptr [rcx]
00850930  48 39 4A 08                     cmp qword ptr [rdx + 8], rcx
00850934  75 09                           jne 0x14085093f
00850936  48 8B 41 08                     mov rax, qword ptr [rcx + 8]
0085093A  48 39 08                        cmp qword ptr [rax], rcx
0085093D  74 07                           je 0x140850946
0085093F  B9 03 00 00 00                  mov ecx, 3
00850944  CD 29                           int 0x29
00850946  FF 0D E4 F2 69 00               dec dword ptr [rip + 0x69f2e4]
0085094C  48 89 10                        mov qword ptr [rax], rdx
0085094F  48 89 42 08                     mov qword ptr [rdx + 8], rax
00850953  48 FF 0D DE 9A 78 00            dec qword ptr [rip + 0x789ade]
0085095A  48 89 49 08                     mov qword ptr [rcx + 8], rcx
0085095E  48 89 09                        mov qword ptr [rcx], rcx
00850961  F0 83 0C 24 00                  lock or dword ptr [rsp], 0
00850966  80 67 40 FD                     and byte ptr [rdi + 0x40], 0xfd
0085096A  48 8D 0D 0F 4F 6A 00            lea rcx, [rip + 0x6a4f0f]
00850971  E8 4A 10 A0 FF                  call 0x1402519c0
00850976  48 8B CF                        mov rcx, rdi
00850979  E8 42 89 37 00                  call 0x140bc92c0
0085097E  E9 EA F5 FF FF                  jmp 0x14084ff6d
00850983  41 0F B6 D6                     movzx edx, r14b
00850987  40 0F B6 CD                     movzx ecx, bpl
0085098B  E8 6C 4D CA FF                  call 0x1404f56fc
00850990  E9 44 FF FF FF                  jmp 0x1408508d9
00850995  45 33 F6                        xor r14d, r14d
00850998  4D 8D 66 FF                     lea r12, [r14 - 1]
0085099C  E9 95 F7 FF FF                  jmp 0x140850136
008509A1  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
008509A5  48 85 C9                        test rcx, rcx
008509A8  0F 84 6C FB FF FF               je 0x14085051a
008509AE  48 8B 79 10                     mov rdi, qword ptr [rcx + 0x10]
008509B2  49 8B CF                        mov rcx, r15
008509B5  E8 06 89 37 00                  call 0x140bc92c0
008509BA  45 33 C0                        xor r8d, r8d
008509BD  48 8D 4F 30                     lea rcx, [rdi + 0x30]
008509C1  33 D2                           xor edx, edx
008509C3  E8 68 F8 9B FF                  call 0x140210230
008509C8  F0 48 0F BA 6F 30 00            lock bts qword ptr [rdi + 0x30], 0
008509CF  48 8B E8                        mov rbp, rax
008509D2  73 10                           jae 0x1408509e4
008509D4  4C 8D 47 30                     lea r8, [rdi + 0x30]
008509D8  48 8B D0                        mov rdx, rax
008509DB  48 8D 4F 30                     lea rcx, [rdi + 0x30]
008509DF  E8 AC F2 9B FF                  call 0x14020fc90
008509E4  48 85 ED                        test rbp, rbp
008509E7  74 04                           je 0x1408509ed
008509E9  C6 45 0A 01                     mov byte ptr [rbp + 0xa], 1
008509ED  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008509F6  49 8D 4F 30                     lea rcx, [r15 + 0x30]
008509FA  45 33 C0                        xor r8d, r8d
008509FD  48 89 47 38                     mov qword ptr [rdi + 0x38], rax
00850A01  33 D2                           xor edx, edx
00850A03  E8 28 F8 9B FF                  call 0x140210230
00850A08  F0 49 0F BA 6F 30 00            lock bts qword ptr [r15 + 0x30], 0
00850A0F  48 8B E8                        mov rbp, rax
00850A12  73 10                           jae 0x140850a24
00850A14  4D 8D 47 30                     lea r8, [r15 + 0x30]
00850A18  48 8B D0                        mov rdx, rax
00850A1B  49 8D 4F 30                     lea rcx, [r15 + 0x30]
00850A1F  E8 6C F2 9B FF                  call 0x14020fc90
00850A24  48 85 ED                        test rbp, rbp
00850A27  74 04                           je 0x140850a2d
00850A29  C6 45 0A 01                     mov byte ptr [rbp + 0xa], 1
00850A2D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00850A36  49 89 47 38                     mov qword ptr [r15 + 0x38], rax
00850A3A  E9 DB FA FF FF                  jmp 0x14085051a
00850A3F  45 33 C9                        xor r9d, r9d
00850A42  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00850A47  4C 8B C5                        mov r8, rbp
00850A4A  41 8D 51 24                     lea edx, [r9 + 0x24]
00850A4E  8D 4A 2D                        lea ecx, [rdx + 0x2d]
00850A51  E8 0A CC CA FF                  call 0x1404fd660
00850A56  CC                              int3
00850A57  48 8B CF                        mov rcx, rdi
00850A5A  E8 71 2E A1 FF                  call 0x1402638d0
00850A5F  E9 E8 FC FF FF                  jmp 0x14085074c
00850A64  48 8B CD                        mov rcx, rbp
00850A67  4C 8B FD                        mov r15, rbp
00850A6A  E8 65 48 1A 00                  call 0x1409f52d4
00850A6F  48 8B CD                        mov rcx, rbp
00850A72  E8 A5 8F 37 00                  call 0x140bc9a1c
00850A77  49 8B CF                        mov rcx, r15
00850A7A  E8 41 88 37 00                  call 0x140bc92c0
00850A7F  0F B7 54 24 34                  movzx edx, word ptr [rsp + 0x34]
00850A84  E9 59 F9 FF FF                  jmp 0x1408503e2
00850A89  41 B9 08 00 00 00               mov r9d, 8
00850A8F  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00850A94  4C 8B C3                        mov r8, rbx
00850A97  41 8D 51 0F                     lea edx, [r9 + 0xf]
00850A9B  8D 4A 3A                        lea ecx, [rdx + 0x3a]
00850A9E  E8 BD CB CA FF                  call 0x1404fd660
00850AA3  CC                              int3
00850AA4  48 8B 0D 35 4E 6A 00            mov rcx, qword ptr [rip + 0x6a4e35]
00850AAB  48 8D 15 2E 4E 6A 00            lea rdx, [rip + 0x6a4e2e]
00850AB2  48 39 51 08                     cmp qword ptr [rcx + 8], rdx
00850AB6  0F 85 83 FE FF FF               jne 0x14085093f
00850ABC  E9 C6 FB FF FF                  jmp 0x140850687
00850AC1  E8 FA 0E A0 FF                  call 0x1402519c0
00850AC6  E9 05 FC FF FF                  jmp 0x1408506d0
00850ACB  0F B7 71 18                     movzx esi, word ptr [rcx + 0x18]
00850ACF  41 0F B7 2E                     movzx ebp, word ptr [r14]
00850AD3  4D 8B 66 08                     mov r12, qword ptr [r14 + 8]
00850AD7  66 D1 ED                        shr bp, 1
00850ADA  66 89 B4 24 80 00 00 00         mov word ptr [rsp + 0x80], si
00850AE2  66 89 B4 24 82 00 00 00         mov word ptr [rsp + 0x82], si
00850AEA  66 D1 EE                        shr si, 1
00850AED  48 89 94 24 88 00 00 00         mov qword ptr [rsp + 0x88], rdx
00850AF5  66 85 ED                        test bp, bp
00850AF8  0F 84 55 F5 FF FF               je 0x140850053
00850AFE  66 85 F6                        test si, si
00850B01  0F 84 4C F5 FF FF               je 0x140850053
00850B07  41 0F B7 0C 24                  movzx ecx, word ptr [r12]
00850B0C  49 83 C4 02                     add r12, 2
00850B10  44 0F B7 2A                     movzx r13d, word ptr [rdx]
00850B14  48 83 C2 02                     add rdx, 2
00850B18  48 89 54 24 40                  mov qword ptr [rsp + 0x40], rdx
00850B1D  66 41 3B CD                     cmp cx, r13w
00850B21  75 0D                           jne 0x140850b30
00850B23  B8 FF FF 00 00                  mov eax, 0xffff
00850B28  66 03 E8                        add bp, ax
00850B2B  66 03 F0                        add si, ax
00850B2E  EB C5                           jmp 0x140850af5
00850B30  66 83 F9 61                     cmp cx, 0x61
00850B34  72 12                           jb 0x140850b48
00850B36  66 83 F9 7A                     cmp cx, 0x7a
00850B3A  0F 87 12 07 00 00               ja 0x140851252
00850B40  B8 E0 FF 00 00                  mov eax, 0xffe0
00850B45  66 03 C8                        add cx, ax
00850B48  66 41 3B CD                     cmp cx, r13w
00850B4C  74 D5                           je 0x140850b23
00850B4E  E9 09 F5 FF FF                  jmp 0x14085005c
00850B53  48 8B 01                        mov rax, qword ptr [rcx]
00850B56  44 88 30                        mov byte ptr [rax], r14b
00850B59  80 67 40 FB                     and byte ptr [rdi + 0x40], 0xfb
00850B5D  E9 F8 FD FF FF                  jmp 0x14085095a
00850B62  49 8B 77 20                     mov rsi, qword ptr [r15 + 0x20]
00850B66  48 8D 54 24 60                  lea rdx, [rsp + 0x60]
00850B6B  49 8B CF                        mov rcx, r15
00850B6E  E8 AD 13 01 00                  call 0x140861f20
00850B73  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00850B7C  81 8E A0 00 00 00 80 00 00 00   or dword ptr [rsi + 0xa0], 0x80
00850B86  48 89 86 50 10 00 00            mov qword ptr [rsi + 0x1050], rax
00850B8D  B8 01 00 00 00                  mov eax, 1
00850B92  F0 0F C1 86 8C 10 00 00         lock xadd dword ptr [rsi + 0x108c], eax
00850B9A  83 E0 7F                        and eax, 0x7f
00850B9D  C7 84 86 90 10 00 00 1F 00 00 00  mov dword ptr [rsi + rax*4 + 0x1090], 0x1f
00850BA8  8B 86 A0 00 00 00               mov eax, dword ptr [rsi + 0xa0]
00850BAE  A8 20                           test al, 0x20
00850BB0  0F 85 1A FB FF FF               jne 0x1408506d0
00850BB6  48 8B CE                        mov rcx, rsi
00850BB9  E8 F2 26 01 00                  call 0x1408632b0
00850BBE  E9 0D FB FF FF                  jmp 0x1408506d0
00850BC3  80 3D 7A EF 69 00 00            cmp byte ptr [rip + 0x69ef7a], 0
00850BCA  BE 34 00 00 C0                  mov esi, 0xc0000034
00850BCF  48 8B 9C 24 00 01 00 00         mov rbx, qword ptr [rsp + 0x100]
00850BD7  0F 84 6B 06 00 00               je 0x140851248
00850BDD  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00850BE6  48 39 05 5B EF 69 00            cmp qword ptr [rip + 0x69ef5b], rax
00850BED  0F 84 55 06 00 00               je 0x140851248
00850BF3  48 85 DB                        test rbx, rbx
00850BF6  0F 84 4C 06 00 00               je 0x140851248
00850BFC  8B 94 24 E8 00 00 00            mov edx, dword ptr [rsp + 0xe8]
00850C03  48 8B CF                        mov rcx, rdi
00850C06  FF CA                           dec edx
00850C08  E8 43 6E 15 00                  call 0x1409a7a50
00850C0D  48 8B C8                        mov rcx, rax
00850C10  4C 8D 8B 88 00 00 00            lea r9, [rbx + 0x88]
00850C17  E8 08 A9 27 00                  call 0x140acb524
00850C1C  84 C0                           test al, al
00850C1E  0F 84 24 06 00 00               je 0x140851248
00850C24  81 0B 00 01 00 00               or dword ptr [rbx], 0x100
00850C2A  BE 03 01 00 00                  mov esi, 0x103
00850C2F  BA 00 03 06 00                  mov edx, 0x60300
00850C34  EB 12                           jmp 0x140850c48
00850C36  48 8B 9C 24 00 01 00 00         mov rbx, qword ptr [rsp + 0x100]
00850C3E  BE 25 04 00 C0                  mov esi, 0xc0000425
00850C43  BA 00 05 06 00                  mov edx, 0x60500
00850C48  44 8B C6                        mov r8d, esi
00850C4B  48 8B CB                        mov rcx, rbx
00850C4E  E8 2D 06 00 00                  call 0x140851280
00850C53  49 8B C4                        mov rax, r12
00850C56  F0 48 0F C1 45 00               lock xadd qword ptr [rbp], rax
00850C5C  48 83 F8 01                     cmp rax, 1
00850C60  0F 84 D5 F3 FF FF               je 0x14085003b
00850C66  49 8B CF                        mov rcx, r15
00850C69  E8 52 86 37 00                  call 0x140bc92c0
00850C6E  80 7C 24 30 00                  cmp byte ptr [rsp + 0x30], 0
00850C73  0F 84 BA 00 00 00               je 0x140850d33
00850C79  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
00850C7D  8B C8                           mov ecx, eax
00850C7F  49 8B 7F 20                     mov rdi, qword ptr [r15 + 0x20]
00850C83  C1 E9 09                        shr ecx, 9
00850C86  33 C8                           xor ecx, eax
00850C88  69 C1 A3 8A 01 00               imul eax, ecx, 0x18aa3
00850C8E  8B C8                           mov ecx, eax
00850C90  8B D0                           mov edx, eax
00850C92  48 8B 87 70 06 00 00            mov rax, qword ptr [rdi + 0x670]
00850C99  48 C1 EA 09                     shr rdx, 9
00850C9D  48 33 D1                        xor rdx, rcx
00850CA0  8B 8F 78 06 00 00               mov ecx, dword ptr [rdi + 0x678]
00850CA6  FF C9                           dec ecx
00850CA8  48 23 D1                        and rdx, rcx
00850CAB  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
00850CAF  4C 89 74 C8 08                  mov qword ptr [rax + rcx*8 + 8], r14
00850CB4  41 8B 47 10                     mov eax, dword ptr [r15 + 0x10]
00850CB8  8B C8                           mov ecx, eax
00850CBA  4D 8B 47 20                     mov r8, qword ptr [r15 + 0x20]
00850CBE  C1 E9 09                        shr ecx, 9
00850CC1  33 C8                           xor ecx, eax
00850CC3  69 C1 A3 8A 01 00               imul eax, ecx, 0x18aa3
00850CC9  8B C8                           mov ecx, eax
00850CCB  8B D0                           mov edx, eax
00850CCD  49 8B 80 70 06 00 00            mov rax, qword ptr [r8 + 0x670]
00850CD4  48 C1 EA 09                     shr rdx, 9
00850CD8  48 33 D1                        xor rdx, rcx
00850CDB  41 8B 88 78 06 00 00            mov ecx, dword ptr [r8 + 0x678]
00850CE2  FF C9                           dec ecx
00850CE4  48 23 D1                        and rdx, rcx
00850CE7  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
00850CEB  48 8D 1C C8                     lea rbx, [rax + rcx*8]
00850CEF  0F 0D 0B                        prefetchw byte ptr [rbx]
00850CF2  48 8B 03                        mov rax, qword ptr [rbx]
00850CF5  48 8B C8                        mov rcx, rax
00850CF8  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00850CFC  48 83 F9 10                     cmp rcx, 0x10
00850D00  48 8D 50 F0                     lea rdx, [rax - 0x10]
00850D04  49 0F 46 D6                     cmovbe rdx, r14
00850D08  A8 02                           test al, 2
00850D0A  0F 85 B7 02 00 00               jne 0x140850fc7
00850D10  F0 48 0F B1 13                  lock cmpxchg qword ptr [rbx], rdx
00850D15  0F 85 AC 02 00 00               jne 0x140850fc7
00850D1B  48 8B CB                        mov rcx, rbx
00850D1E  E8 DD 08 A9 FF                  call 0x1402e1600
00850D23  41 8B C4                        mov eax, r12d
00850D26  F0 0F C1 87 88 10 00 00         lock xadd dword ptr [rdi + 0x1088], eax
00850D2E  83 F8 01                        cmp eax, 1
00850D31  74 65                           je 0x140850d98
00850D33  0F 57 C0                        xorps xmm0, xmm0
00850D36  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00850D3B  0F 11 44 24 70                  movups xmmword ptr [rsp + 0x70], xmm0
00850D40  E8 AB 9A BD FF                  call 0x14042a7f0
00850D45  49 8B 5F 20                     mov rbx, qword ptr [r15 + 0x20]
00850D49  49 8B 0F                        mov rcx, qword ptr [r15]
00850D4C  48 83 F9 01                     cmp rcx, 1
00850D50  76 50                           jbe 0x140850da2
00850D52  48 8D 51 FF                     lea rdx, [rcx - 1]
00850D56  48 83 FA 02                     cmp rdx, 2
00850D5A  0F 84 41 02 00 00               je 0x140850fa1
00850D60  45 32 C0                        xor r8b, r8b
00850D63  48 8B C1                        mov rax, rcx
00850D66  F0 49 0F B1 17                  lock cmpxchg qword ptr [r15], rdx
00850D6B  48 8B C8                        mov rcx, rax
00850D6E  48 8D 42 01                     lea rax, [rdx + 1]
00850D72  48 3B C8                        cmp rcx, rax
00850D75  75 D5                           jne 0x140850d4c
00850D77  48 3B CA                        cmp rcx, rdx
00850D7A  0F 83 49 03 00 00               jae 0x1408510c9
00850D80  45 33 C9                        xor r9d, r9d
00850D83  4C 89 74 24 20                  mov qword ptr [rsp + 0x20], r14
00850D88  4D 8B C7                        mov r8, r15
00850D8B  41 8D 51 25                     lea edx, [r9 + 0x25]
00850D8F  8D 4A 2C                        lea ecx, [rdx + 0x2c]
00850D92  E8 C9 C8 CA FF                  call 0x1404fd660
00850D97  CC                              int3
00850D98  48 8B CF                        mov rcx, rdi
00850D9B  E8 6C 37 01 00                  call 0x14086450c
00850DA0  EB 91                           jmp 0x140850d33
00850DA2  45 8B 77 10                     mov r14d, dword ptr [r15 + 0x10]
00850DA6  45 33 C0                        xor r8d, r8d
00850DA9  49 8B 5F 20                     mov rbx, qword ptr [r15 + 0x20]
00850DAD  41 8B C6                        mov eax, r14d
00850DB0  C1 E8 09                        shr eax, 9
00850DB3  41 33 C6                        xor eax, r14d
00850DB6  69 C0 A3 8A 01 00               imul eax, eax, 0x18aa3
00850DBC  8B C8                           mov ecx, eax
00850DBE  8B D0                           mov edx, eax
00850DC0  48 8B 83 70 06 00 00            mov rax, qword ptr [rbx + 0x670]
00850DC7  48 C1 EA 09                     shr rdx, 9
00850DCB  48 33 D1                        xor rdx, rcx
00850DCE  8B 8B 78 06 00 00               mov ecx, dword ptr [rbx + 0x678]
00850DD4  FF C9                           dec ecx
00850DD6  48 23 D1                        and rdx, rcx
00850DD9  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
00850DDD  33 D2                           xor edx, edx
00850DDF  48 8D 3C C8                     lea rdi, [rax + rcx*8]
00850DE3  48 8B CF                        mov rcx, rdi
00850DE6  E8 45 F4 9B FF                  call 0x140210230
00850DEB  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
00850DF1  48 8B E8                        mov rbp, rax
00850DF4  73 0E                           jae 0x140850e04
00850DF6  4C 8B C7                        mov r8, rdi
00850DF9  48 8B D0                        mov rdx, rax
00850DFC  48 8B CF                        mov rcx, rdi
00850DFF  E8 8C EE 9B FF                  call 0x14020fc90
00850E04  48 85 ED                        test rbp, rbp
00850E07  74 04                           je 0x140850e0d
00850E09  C6 45 0A 01                     mov byte ptr [rbp + 0xa], 1
00850E0D  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00850E16  48 89 47 08                     mov qword ptr [rdi + 8], rax
00850E1A  0F 0D 8B 88 10 00 00            prefetchw byte ptr [rbx + 0x1088]
00850E21  8B 83 88 10 00 00               mov eax, dword ptr [rbx + 0x1088]
00850E27  85 C0                           test eax, eax
00850E29  0F 84 49 03 00 00               je 0x140851178
00850E2F  8D 48 01                        lea ecx, [rax + 1]
00850E32  F0 0F B1 8B 88 10 00 00         lock cmpxchg dword ptr [rbx + 0x1088], ecx
00850E3A  75 EB                           jne 0x140850e27
00850E3C  45 33 C0                        xor r8d, r8d
00850E3F  49 8D 4F 30                     lea rcx, [r15 + 0x30]
00850E43  33 D2                           xor edx, edx
00850E45  E8 E6 F3 9B FF                  call 0x140210230
00850E4A  F0 49 0F BA 6F 30 00            lock bts qword ptr [r15 + 0x30], 0
00850E51  48 8B E8                        mov rbp, rax
00850E54  73 10                           jae 0x140850e66
00850E56  4D 8D 47 30                     lea r8, [r15 + 0x30]
00850E5A  48 8B D0                        mov rdx, rax
00850E5D  49 8D 4F 30                     lea rcx, [r15 + 0x30]
00850E61  E8 2A EE 9B FF                  call 0x14020fc90
00850E66  48 85 ED                        test rbp, rbp
00850E69  74 04                           je 0x140850e6f
00850E6B  C6 45 0A 01                     mov byte ptr [rbp + 0xa], 1
00850E6F  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00850E78  45 33 ED                        xor r13d, r13d
00850E7B  49 89 47 38                     mov qword ptr [r15 + 0x38], rax
00850E7F  41 8B FD                        mov edi, r13d
00850E82  49 8B 87 C0 00 00 00            mov rax, qword ptr [r15 + 0xc0]
00850E89  48 85 C0                        test rax, rax
00850E8C  0F 85 8C 01 00 00               jne 0x14085101e
00850E92  49 8B 4F 20                     mov rcx, qword ptr [r15 + 0x20]
00850E96  49 8B C4                        mov rax, r12
00850E99  F0 49 0F C1 07                  lock xadd qword ptr [r15], rax
00850E9E  48 FF C8                        dec rax
00850EA1  48 83 F8 02                     cmp rax, 2
00850EA5  0F 84 75 03 00 00               je 0x140851220
00850EAB  48 85 C0                        test rax, rax
00850EAE  75 48                           jne 0x140850ef8
00850EB0  41 F7 87 B8 00 00 00 00 00 04 00  test dword ptr [r15 + 0xb8], 0x40000
00850EBB  0F 85 FA 02 00 00               jne 0x1408511bb
00850EC1  41 8B 47 08                     mov eax, dword ptr [r15 + 8]
00850EC5  41 8B D5                        mov edx, r13d
00850EC8  8B C8                           mov ecx, eax
00850ECA  C1 E8 11                        shr eax, 0x11
00850ECD  F6 D0                           not al
00850ECF  24 01                           and al, 1
00850ED1  F6 C1 20                        test cl, 0x20
00850ED4  0F B6 C0                        movzx eax, al
00850ED7  0F 44 D0                        cmove edx, eax
00850EDA  8B 05 E0 DD 5B 00               mov eax, dword ptr [rip + 0x5bdde0]
00850EE0  85 C0                           test eax, eax
00850EE2  0F 85 EC 00 00 00               jne 0x140850fd4
00850EE8  84 D2                           test dl, dl
00850EEA  0F 84 01 01 00 00               je 0x140850ff1
00850EF0  49 8B CF                        mov rcx, r15
00850EF3  E8 C8 EC FF FF                  call 0x14084fbc0
00850EF8  49 8B CF                        mov rcx, r15
00850EFB  E8 C0 83 37 00                  call 0x140bc92c0
00850F00  48 85 FF                        test rdi, rdi
00850F03  74 08                           je 0x140850f0d
00850F05  48 8B CF                        mov rcx, rdi
00850F08  E8 B3 83 37 00                  call 0x140bc92c0
00850F0D  41 8B C6                        mov eax, r14d
00850F10  C1 E8 09                        shr eax, 9
00850F13  41 33 C6                        xor eax, r14d
00850F16  69 C0 A3 8A 01 00               imul eax, eax, 0x18aa3
00850F1C  8B C8                           mov ecx, eax
00850F1E  8B D0                           mov edx, eax
00850F20  48 8B 83 70 06 00 00            mov rax, qword ptr [rbx + 0x670]
00850F27  48 C1 EA 09                     shr rdx, 9
00850F2B  48 33 D1                        xor rdx, rcx
00850F2E  8B 8B 78 06 00 00               mov ecx, dword ptr [rbx + 0x678]
00850F34  FF C9                           dec ecx
00850F36  48 23 D1                        and rdx, rcx
00850F39  48 8D 0C 52                     lea rcx, [rdx + rdx*2]
00850F3D  48 8D 3C C8                     lea rdi, [rax + rcx*8]
00850F41  4C 89 6F 08                     mov qword ptr [rdi + 8], r13
00850F45  0F 0D 0F                        prefetchw byte ptr [rdi]
00850F48  48 8B 07                        mov rax, qword ptr [rdi]
00850F4B  48 8B C8                        mov rcx, rax
00850F4E  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
00850F52  48 83 F9 10                     cmp rcx, 0x10
00850F56  48 8D 50 F0                     lea rdx, [rax - 0x10]
00850F5A  49 0F 46 D5                     cmovbe rdx, r13
00850F5E  A8 02                           test al, 2
00850F60  0F 85 05 02 00 00               jne 0x14085116b
00850F66  F0 48 0F B1 17                  lock cmpxchg qword ptr [rdi], rdx
00850F6B  0F 85 FA 01 00 00               jne 0x14085116b
00850F71  48 8B CF                        mov rcx, rdi
00850F74  E8 87 06 A9 FF                  call 0x1402e1600
00850F79  F0 44 0F C1 A3 88 10 00 00      lock xadd dword ptr [rbx + 0x1088], r12d
00850F82  41 83 FC 01                     cmp r12d, 1
00850F86  75 08                           jne 0x140850f90
00850F88  48 8B CB                        mov rcx, rbx
00850F8B  E8 7C 35 01 00                  call 0x14086450c
00850F90  33 D2                           xor edx, edx
00850F92  48 8D 4C 24 70                  lea rcx, [rsp + 0x70]
00850F97  E8 04 AA BC FF                  call 0x14041b9a0
00850F9C  E9 68 F4 FF FF                  jmp 0x140850409
00850FA1  41 F7 87 B8 00 00 00 00 00 04 00  test dword ptr [r15 + 0xb8], 0x40000
00850FAC  0F 84 AE FD FF FF               je 0x140850d60
00850FB2  80 BB 80 0B 00 00 01            cmp byte ptr [rbx + 0xb80], 1
00850FB9  0F 85 A1 FD FF FF               jne 0x140850d60
00850FBF  41 B0 01                        mov r8b, 1
00850FC2  E9 9C FD FF FF                  jmp 0x140850d63
00850FC7  48 8B CB                        mov rcx, rbx
00850FCA  E8 01 29 A1 FF                  call 0x1402638d0
00850FCF  E9 47 FD FF FF                  jmp 0x140850d1b
00850FD4  41 0F B7 87 BA 00 00 00         movzx eax, word ptr [r15 + 0xba]
00850FDC  A8 10                           test al, 0x10
00850FDE  0F 94 C1                        sete cl
00850FE1  41 F6 47 08 08                  test byte ptr [r15 + 8], 8
00850FE6  0F 94 C0                        sete al
00850FE9  84 C8                           test al, cl
00850FEB  0F 84 F7 FE FF FF               je 0x140850ee8
00850FF1  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
00850FF6  49 8B CF                        mov rcx, r15
00850FF9  E8 22 0F 01 00                  call 0x140861f20
00850FFE  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00851007  49 39 47 38                     cmp qword ptr [r15 + 0x38], rax
0085100B  0F 84 E7 FE FF FF               je 0x140850ef8
00851011  49 8B CF                        mov rcx, r15
00851014  E8 37 17 01 00                  call 0x140862750
00851019  E9 DA FE FF FF                  jmp 0x140850ef8
0085101E  48 8B 48 18                     mov rcx, qword ptr [rax + 0x18]
00851022  48 85 C9                        test rcx, rcx
00851025  0F 84 67 FE FF FF               je 0x140850e92
0085102B  48 8B 79 10                     mov rdi, qword ptr [rcx + 0x10]
0085102F  49 8B CF                        mov rcx, r15
00851032  E8 89 82 37 00                  call 0x140bc92c0
00851037  45 33 C0                        xor r8d, r8d
0085103A  48 8D 4F 30                     lea rcx, [rdi + 0x30]
0085103E  33 D2                           xor edx, edx
00851040  E8 EB F1 9B FF                  call 0x140210230
00851045  F0 48 0F BA 6F 30 00            lock bts qword ptr [rdi + 0x30], 0
0085104C  4C 8B F8                        mov r15, rax
0085104F  73 10                           jae 0x140851061
00851051  4C 8D 47 30                     lea r8, [rdi + 0x30]
00851055  48 8B D0                        mov rdx, rax
00851058  48 8D 4F 30                     lea rcx, [rdi + 0x30]
0085105C  E8 2F EC 9B FF                  call 0x14020fc90
00851061  4D 85 FF                        test r15, r15
00851064  74 05                           je 0x14085106b
00851066  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
0085106B  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00851074  45 33 C0                        xor r8d, r8d
00851077  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
0085107C  33 D2                           xor edx, edx
0085107E  48 83 C5 30                     add rbp, 0x30
00851082  48 89 47 38                     mov qword ptr [rdi + 0x38], rax
00851086  48 8B CD                        mov rcx, rbp
00851089  E8 A2 F1 9B FF                  call 0x140210230
0085108E  F0 48 0F BA 6D 00 00            lock bts qword ptr [rbp], 0
00851095  4C 8B F8                        mov r15, rax
00851098  73 0E                           jae 0x1408510a8
0085109A  4C 8B C5                        mov r8, rbp
0085109D  48 8B D0                        mov rdx, rax
008510A0  48 8B CD                        mov rcx, rbp
008510A3  E8 E8 EB 9B FF                  call 0x14020fc90
008510A8  4D 85 FF                        test r15, r15
008510AB  74 05                           je 0x1408510b2
008510AD  41 C6 47 0A 01                  mov byte ptr [r15 + 0xa], 1
008510B2  4C 8B 7C 24 38                  mov r15, qword ptr [rsp + 0x38]
008510B7  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008510C0  49 89 47 38                     mov qword ptr [r15 + 0x38], rax
008510C4  E9 C9 FD FF FF                  jmp 0x140850e92
008510C9  45 84 C0                        test r8b, r8b
008510CC  0F 84 37 F3 FF FF               je 0x140850409
008510D2  48 8B CB                        mov rcx, rbx
008510D5  E8 DA 01 00 00                  call 0x1408512b4
008510DA  41 B8 01 00 00 00               mov r8d, 1
008510E0  41 8B C0                        mov eax, r8d
008510E3  F0 0F C1 83 8C 10 00 00         lock xadd dword ptr [rbx + 0x108c], eax
008510EB  83 E0 7F                        and eax, 0x7f
008510EE  C7 84 83 90 10 00 00 13 00 00 00  mov dword ptr [rbx + rax*4 + 0x1090], 0x13
008510F9  48 8B 83 78 0B 00 00            mov rax, qword ptr [rbx + 0xb78]
00851100  48 83 38 02                     cmp qword ptr [rax], 2
00851104  74 0D                           je 0x140851113
00851106  48 8B CB                        mov rcx, rbx
00851109  E8 5E 0C 00 00                  call 0x140851d6c
0085110E  E9 F6 F2 FF FF                  jmp 0x140850409
00851113  41 8B C0                        mov eax, r8d
00851116  F0 0F C1 83 8C 10 00 00         lock xadd dword ptr [rbx + 0x108c], eax
0085111E  83 E0 7F                        and eax, 0x7f
00851121  C7 84 83 90 10 00 00 14 00 00 00  mov dword ptr [rbx + rax*4 + 0x1090], 0x14
0085112C  33 C0                           xor eax, eax
0085112E  F0 44 0F B1 83 C0 12 00 00      lock cmpxchg dword ptr [rbx + 0x12c0], r8d
00851137  75 CD                           jne 0x140851106
00851139  41 8B C0                        mov eax, r8d
0085113C  F0 0F C1 83 8C 10 00 00         lock xadd dword ptr [rbx + 0x108c], eax
00851144  83 E0 7F                        and eax, 0x7f
00851147  48 8B CB                        mov rcx, rbx
0085114A  C7 84 83 90 10 00 00 15 00 00 00  mov dword ptr [rbx + rax*4 + 0x1090], 0x15
00851155  E8 96 EB FF FF                  call 0x14084fcf0
0085115A  48 8B 8B D0 12 00 00            mov rcx, qword ptr [rbx + 0x12d0]
00851161  41 8B D0                        mov edx, r8d
00851164  E8 B7 83 AA FF                  call 0x1402f9520
00851169  EB 9B                           jmp 0x140851106
0085116B  48 8B CF                        mov rcx, rdi
0085116E  E8 5D 27 A1 FF                  call 0x1402638d0
00851173  E9 F9 FD FF FF                  jmp 0x140850f71
00851178  41 B9 08 00 00 00               mov r9d, 8
0085117E  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
00851183  4C 8B C3                        mov r8, rbx
00851186  41 8D 51 0F                     lea edx, [r9 + 0xf]
0085118A  8D 4A 3A                        lea ecx, [rdx + 0x3a]
0085118D  E8 CE C4 CA FF                  call 0x1404fd660
00851192  CC                              int3
00851193  41 F7 87 B8 00 00 00 00 00 04 00  test dword ptr [r15 + 0xb8], 0x40000
0085119E  0F 84 2C F5 FF FF               je 0x1408506d0
008511A4  80 B9 80 0B 00 00 01            cmp byte ptr [rcx + 0xb80], 1
008511AB  0F 85 1F F5 FF FF               jne 0x1408506d0
008511B1  E8 62 E9 FF FF                  call 0x14084fb18
008511B6  E9 15 F5 FF FF                  jmp 0x1408506d0
008511BB  49 8B 6F 20                     mov rbp, qword ptr [r15 + 0x20]
008511BF  48 8D 54 24 70                  lea rdx, [rsp + 0x70]
008511C4  49 8B CF                        mov rcx, r15
008511C7  E8 54 0D 01 00                  call 0x140861f20
008511CC  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008511D5  41 B8 01 00 00 00               mov r8d, 1
008511DB  81 8D A0 00 00 00 80 00 00 00   or dword ptr [rbp + 0xa0], 0x80
008511E5  48 89 85 50 10 00 00            mov qword ptr [rbp + 0x1050], rax
008511EC  F0 44 0F C1 85 8C 10 00 00      lock xadd dword ptr [rbp + 0x108c], r8d
008511F5  41 83 E0 7F                     and r8d, 0x7f
008511F9  42 C7 84 85 90 10 00 00 1F 00 00 00  mov dword ptr [rbp + r8*4 + 0x1090], 0x1f
00851205  8B 85 A0 00 00 00               mov eax, dword ptr [rbp + 0xa0]
0085120B  A8 20                           test al, 0x20
0085120D  0F 85 E5 FC FF FF               jne 0x140850ef8
00851213  48 8B CD                        mov rcx, rbp
00851216  E8 95 20 01 00                  call 0x1408632b0
0085121B  E9 D8 FC FF FF                  jmp 0x140850ef8
00851220  41 F7 87 B8 00 00 00 00 00 04 00  test dword ptr [r15 + 0xb8], 0x40000
0085122B  0F 84 C7 FC FF FF               je 0x140850ef8
00851231  80 B9 80 0B 00 00 01            cmp byte ptr [rcx + 0xb80], 1
00851238  0F 85 BA FC FF FF               jne 0x140850ef8
0085123E  E8 D5 E8 FF FF                  call 0x14084fb18
00851243  E9 B0 FC FF FF                  jmp 0x140850ef8
00851248  BA 00 04 06 00                  mov edx, 0x60400
0085124D  E9 F6 F9 FF FF                  jmp 0x140850c48
00851252  E8 99 DE 00 00                  call 0x14085f0f0
00851257  48 8B 54 24 40                  mov rdx, qword ptr [rsp + 0x40]
0085125C  0F B7 C8                        movzx ecx, ax
0085125F  E9 E4 F8 FF FF                  jmp 0x140850b48
00851264  44 0F B6 74 24 30               movzx r14d, byte ptr [rsp + 0x30]
0085126A  E9 08 F8 FF FF                  jmp 0x140850a77
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpPerformCompleteKcbCacheLookup(__int64 a1, int a2, int a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m54;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int16 v_stack_mA4;
    unsigned __int16 v_stack_mA6;
    unsigned __int8 v_stack_mA8;
    unsigned __int64 v_stack_mB8;
    unsigned int v_stack_p0;
    unsigned int v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int8 v_stack_p30;
    unsigned __int16 v_stack_p34;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p60;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p8;
    unsigned __int16 v_stack_p80;
    unsigned __int16 v_stack_p82;
    unsigned __int64 v_stack_p88;
    unsigned int v_stack_pE8;
    unsigned int v_stack_pF0;
    unsigned __int64 v_stack_pF8;

    v_stack_p20 = a4;
    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (152);
    v_r15 = 0;
    v_stack_m88 = a1;
    v_stack_mA4 = 0;
loc_0084FD5E:
    v_r14 = 0;
    v_stack_m80 = *(unsigned __int64 *)(a1 + 32);
    v_stack_mA6 = 0;
    v_stack_mA8 = 0;
    result = (v_r15 + 1) + (1);
    if (condition_is_equal) goto loc_00850855;
    if (result != 1) goto loc_0084FDAC;
    v_r14 = 0;
loc_0084FD94:
    a4 = 0;
    v_stack_mB8 = 0;
    a3 = 0;
    result = KeBugCheckEx(a4 + 21 + 60, a4 + 21, a3, a4);
loc_0084FDAC:
    v_stack_mA0 = a1;
loc_0084FDBA:
    v_stack_m90 = (unsigned int)((unsigned int)((unsigned int)(a4 + 21)));
    if (((unsigned int)((unsigned int)((unsigned int)(a4 + 21)))) >= 0) goto loc_00850995;
    if (((unsigned int)((unsigned int)((unsigned int)(a4 + 21)))) >= 8) goto loc_00850348;
    v_r14 = ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4 + 21)))) + 2) << (4);
    v_r14 = (v_r14) + (0);
loc_0084FDE3:
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 16))) * ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16)))));
    a3 = 0;
    a2 = 0;
    v_rbx = (unsigned int)((v_rbx) + ((unsigned int)((unsigned int)(*(unsigned int *)(a4 + (unsigned int)((unsigned int)((unsigned int)((unsigned int)(a4 + 21)))) * 4)))));
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (9));
    result = (unsigned int)((result) ^ ((unsigned int)(v_rbx)));
    result = (unsigned int)((result) * ((unsigned int)(result)));
    v_rbp = ((unsigned int)((unsigned int)(result))) >> (9);
    v_rbp = (v_rbp) ^ ((unsigned int)((unsigned int)(result)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 1656))) - 1);
    a1 = (a1) & (v_rbp);
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8;
        a3 = 0;
        a2 = 0;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
loc_0084FE61:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 4232))) == 0) goto loc_008503B2;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 4232))) != 0) goto loc_0084FE61;
    a4 = 0;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 32) + 1656))) - 1);
    a1 = (a1) & (v_rbp);
    v_stack_m54 = 0;
loc_0084FE9E:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8 + 16) == 0) goto loc_00850095;
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8 + 16))) != ((unsigned int)(v_rbx))) goto loc_0085005C;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8 + 16) - 16 + 72)) != v_stack_mA0) goto loc_0085005C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8 + 16) - 16 + 80))))) & (1)) == 0) goto loc_00850ACB;
    v_rsi = (unsigned __int16)((*(unsigned __int16 *)(v_r14)) >> (1));
loc_0084FEE4:
    if ((unsigned __int16)(v_rsi) == 0) goto loc_0084FF38;
    if ((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8 + 16) - 16 + 80) + 24)) == 0) goto loc_0084FF38;
    v_r13 = (*(unsigned __int64 *)(v_r14 + 8)) + (2);
    a2 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8 + 16) - 16 + 80) + 26) + 1;
    v_stack_m98 = a2;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r14 + 8)))) == ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8 + 16) - 16 + 80) + 26)))) goto loc_0084FF2B;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r14 + 8)))) < 97) goto loc_0084FF21;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r14 + 8)))) > 122) goto loc_00850843;
    a1 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_r14 + 8))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_0084FF21:
    if (((unsigned __int16)(a1)) != ((unsigned __int16)(*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8 + 16) - 16 + 80) + 26)))) goto loc_0085005C;
loc_0084FF2B:
    v_rsi = (unsigned __int16)((v_rsi) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    v_rbp = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8 + 16) - 16 + 80) + 24)) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    goto loc_0084FEE4;
loc_0084FF38:
    if (((unsigned __int16)(v_rsi)) != ((unsigned __int16)(v_rbp))) goto loc_0085005C;
loc_0084FF41:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8 + 16) - 16 == 0) goto loc_00850095;
loc_0084FF50:
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8 + 16) - 16) == 0) goto loc_00850065;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8 + 16) - 16) + 1 == 0) goto loc_0085088B;
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8 + 16) - 16) + 1 != 0) goto loc_0084FF50;
loc_0084FF6D:
    if (((unsigned int)((unsigned int)(v_stack_m90))) == ((unsigned int)((unsigned int)(v_stack_p18) - 1))) goto loc_00850331;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (9));
    result = (unsigned int)((result) ^ ((unsigned int)(v_rbx)));
    result = (unsigned int)((result) * ((unsigned int)(result)));
    a2 = ((unsigned int)((unsigned int)(result))) >> (9);
    a2 = (a2) ^ ((unsigned int)((unsigned int)(result)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m80 + 1656))) - 1);
    a2 = (a2) & (a1);
    a3 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80 + 1648) + a2 + a2 * 2 * 8 + 8) = 0;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80 + 1648) + a2 + a2 * 2 * 8)) & (-16);
    a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80 + 1648) + a2 + a2 * 2 * 8) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80 + 1648) + a2 + a2 * 2 * 8))) & (2)) != 0) goto loc_008503A5;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80 + 1648) + a2 + a2 * 2 * 8))) & (2)) != 0) goto loc_008503A5;
loc_0084FFF2:
    result = KeAbPostRelease(*(unsigned __int64 *)(v_stack_m80 + 1648) + a2 + a2 * 2 * 8, a2, a3, a4);
    result = (unsigned int)(0xFFFFFFFFULL);
    if (((unsigned int)((unsigned int)(0xFFFFFFFFULL))) == 1) {
        a1 = v_stack_m80;
        result = CmpDeleteHive(a1, a2, a3, a4);
    }
loc_0085001D:
    if (-1 != 1) goto loc_00850370;
    v_r14 = 0;
loc_0085003B:
    a4 = 0;
    v_stack_mB8 = 0;
    a3 = 0;
    result = KeBugCheckEx(a4 + 31 + 50, a4 + 31, a3, a4);
loc_00850053:
    if (((unsigned __int16)(v_rbp)) == ((unsigned __int16)(*(unsigned __int64 *)(v_stack_m80 + 1648) + a2 + a2 * 2 * 8))) goto loc_0084FF41;
loc_0085005C:
    goto loc_0084FE9E;
loc_00850065:
    result = CmpLockKcbShared(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8 + 16) - 16, a4 + 31, a3, a4);
    if (((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8 + 16) - 16 + 8)) & (0x80000ULL)) == 0) goto loc_0085087F;
    v_r13 = 0;
    a4 = 0;
    v_stack_mB8 = 0;
    result = KeBugCheckEx(v_r13 + 32 + 49, v_r13 + 32, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8 + 16) - 16, a4);
loc_00850095:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (9));
    result = (unsigned int)((result) ^ ((unsigned int)(v_rbx)));
    result = (unsigned int)((result) * ((unsigned int)(result)));
    a2 = ((unsigned int)((unsigned int)(result))) >> (9);
    a2 = (a2) ^ ((unsigned int)((unsigned int)(result)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m80 + 1656))) - 1);
    a2 = (a2) & (a1);
    v_r14 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80 + 1648) + a2 + a2 * 2 * 8 + 8) = 0;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80 + 1648) + a2 + a2 * 2 * 8)) & (-16);
    a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80 + 1648) + a2 + a2 * 2 * 8) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80 + 1648) + a2 + a2 * 2 * 8))) & (2)) != 0) goto loc_008503CF;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_m80 + 1648) + a2 + a2 * 2 * 8))) & (2)) != 0) goto loc_008503CF;
loc_00850100:
    result = KeAbPostRelease(*(unsigned __int64 *)(v_stack_m80 + 1648) + a2 + a2 * 2 * 8, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8 + 16) - 16, a4);
    if (-1 == 1) goto loc_0085033B;
loc_00850124:
loc_00850136:
    if (v_stack_m88 == v_stack_p8) goto loc_00850158;
    if (-1 == 1) goto loc_0085003B;
loc_00850158:
    a2 = (unsigned __int16)((v_stack_mA4) + ((unsigned __int16)(v_stack_mA6)));
    v_stack_mA4 = (unsigned __int16)(a2);
    if (((*(unsigned int *)(v_stack_mA0 + 184)) & (0x20000ULL)) == 0) goto loc_008503DC;
    result = CmpLockKcbShared(v_stack_mA0, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8 + 16) - 16, a4);
    if (((*(unsigned int *)(v_stack_mA0 + 184)) & (0x20000ULL)) == 0) goto loc_00851264;
    v_stack_m88 = *(unsigned __int64 *)(v_stack_mA0 + 104);
    result = (1) + (1);
    if (condition_is_equal) goto loc_00850A3F;
    if (result == 1) goto loc_0084FD94;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 104) + 32) + 160)))) & (32)) == 0) goto loc_008501E5;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 104) + 32) + 4168)) != (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00850BC3;
loc_008501E5:
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_mA0 + 104) + 8)) & (0x40000ULL)) != 0) goto loc_00850C36;
    result = CmpUnlockKcb(v_stack_mA0, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 1648) + a1 + a1 * 2 * 8 + 16) - 16, a4);
    v_r13 = 0;
    if ((unsigned __int8)(v_stack_mA8) == 0) goto loc_008502C9;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mA0 + 16))))) >> (9));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mA0 + 16)))));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mA0 + 16))) * ((unsigned int)(a1)));
    a2 = ((unsigned int)((unsigned int)(result))) >> (9);
    a2 = (a2) ^ ((unsigned int)((unsigned int)(result)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 1656))) - 1);
    a2 = (a2) & (a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 1648) + a2 + a2 * 2 * 8 + 8) = 0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mA0 + 16))))) >> (9));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_mA0 + 16)))));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_mA0 + 16))) * ((unsigned int)(a1)));
    a2 = ((unsigned int)((unsigned int)(result))) >> (9);
    a2 = (a2) ^ ((unsigned int)((unsigned int)(result)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 1656))) - 1);
    a2 = (a2) & (a1);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 1648) + a2 + a2 * 2 * 8)) & (-16);
    a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 1648) + a2 + a2 * 2 * 8) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 1648) + a2 + a2 * 2 * 8))) & (2)) != 0) goto loc_00850637;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 1648) + a2 + a2 * 2 * 8))) & (2)) != 0) goto loc_00850637;
loc_008502AE:
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 1648) + a2 + a2 * 2 * 8, a2, *(unsigned __int64 *)(v_stack_mA0 + 32), a4);
    if (-1 == 1) goto loc_00850420;
loc_008502C9:
    v_stack_m78 = v_xmm0;
    result = CmpInitializeDelayDerefContext(v_stack_m78, a2, *(unsigned __int64 *)(v_stack_mA0 + 32), a4);
loc_008502E2:
    if ((*(unsigned __int64 *)(v_stack_mA0)) <= 1) goto loc_0085042D;
    if ((*(unsigned __int64 *)(v_stack_mA0) - 1) == 2) goto loc_00850610;
loc_008502F9:
    a3 = 0;
loc_008502FC:
    if ((*(unsigned __int64 *)(v_stack_mA0)) != (*(unsigned __int64 *)(v_stack_mA0) - 1 + 1)) goto loc_008502E2;
    if ((*(unsigned __int64 *)(v_stack_mA0)) >= (*(unsigned __int64 *)(v_stack_mA0) - 1)) goto loc_0085078A;
    a4 = 0;
    v_stack_mB8 = 0;
    result = KeBugCheckEx(a4 + 37 + 44, a4 + 37, v_stack_mA0, a4);
loc_00850331:
    v_stack_mA8 = 1;
    goto loc_0085001D;
loc_0085033B:
    result = CmpDeleteHive(0, a4 + 37, v_stack_mA0, a4);
    goto loc_00850124;
loc_00850348:
    v_r14 = ((unsigned int)((unsigned int)(-1 - 8))) + (6);
    v_r14 = (v_r14) << (4);
    v_r14 = (v_r14) + (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 160));
    goto loc_0084FDE3;
loc_00850370:
    a1 = (unsigned __int16)((v_stack_mA6) + 1);
    v_stack_mA0 = *(unsigned __int64 *)(v_stack_mA0 + 32);
    v_stack_mA6 = (unsigned __int16)(a1);
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 184)) & (0x100000ULL)) != 0) goto loc_00850995;
    v_r12 = (unsigned int)((-1) + 1);
    goto loc_0084FDBA;
loc_008503A5:
    result = ExfReleasePushLock(1, a4 + 37, v_stack_mA0, a4);
    goto loc_0084FFF2;
loc_008503B2:
    v_stack_mB8 = (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_mA0 + 32)));
    result = KeBugCheckEx(9 + 14 + 58, 9 + 14, 0, 9);
loc_008503CF:
    result = ExfReleasePushLock(*(unsigned __int64 *)(v_stack_mA0 + 32), 9 + 14, 0, 9);
    goto loc_00850100;
loc_008503DC:
loc_008503E2:
    v_r13 = 0;
    *(unsigned __int64 *)(a6) = *(unsigned __int64 *)(v_stack_mA0 + 32);
    *(unsigned __int8 *)(a7) = (unsigned __int8)(v_stack_mA8);
    *(unsigned __int16 *)(a8) = (unsigned __int16)(9 + 14);
loc_00850409:
    v_rsp = (v_rsp) + (152);
    return 0;
loc_00850420:
    result = CmpDeleteHive(v_stack_p20, 9 + 14, 0, 9);
    goto loc_008502C9;
loc_0085042D:
    a3 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 16))))) >> (9));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 16)))));
    result = (unsigned int)((result) * ((unsigned int)(result)));
    a2 = ((unsigned int)((unsigned int)(result))) >> (9);
    a2 = (a2) ^ ((unsigned int)((unsigned int)(result)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32) + 1656))) - 1);
    a2 = (a2) & (a1);
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32) + 1648) + a2 + a2 * 2 * 8, a2, a3, 9);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32) + 1648) + a2 + a2 * 2 * 8;
        a2 = result;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32) + 1648) + a2 + a2 * 2 * 8;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, 9);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32) + 1648) + a2 + a2 * 2 * 8 + 8) = *(unsigned __int64 *)(gs_base + (0 + 392));
loc_008504B2:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32) + 4232))) == 0) goto loc_00850A89;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32) + 4232))) != 0) goto loc_008504B2;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(v_stack_mA0 + 32) + 48, a2, a3, 9);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(v_stack_mA0 + 32) + 48;
        a2 = result;
        a1 = *(unsigned __int64 *)(v_stack_mA0 + 32) + 48;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, 9);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 56) = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 192) != 0) goto loc_008509A1;
loc_0085051A:
    result = (v_r12) - 1;
    if (result == 2) goto loc_00851193;
    if (result != 0) goto loc_008506D0;
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 184)) & (0x40000ULL)) != 0) goto loc_00850B62;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 8))) >> (17));
    result = (unsigned __int8)(~(result));
    result = (unsigned __int8)((result) & (1));
    a2 = 0;
    if ((((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 8)))))) & (32)) == 0) { a2 = (unsigned int)((unsigned __int8)(result)); }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6022996))) != 0) goto loc_00850644;
loc_00850574:
    if ((unsigned __int8)(a2) == 0) goto loc_00850661;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 6968058, a2, a3, 9);
    if ((*(unsigned int *)(v_rip + 7825275)) != 0) goto loc_0085086D;
loc_008505AB:
    if ((*(unsigned int *)(v_rip + 7825275)) >= 0) {
        a2 = result;
        a1 = v_rip + 6968000;
        result = ExpAcquireFastMutexContended(a1, a2, 1, 9);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int64 *)(v_rip + 6967978) = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned int *)(v_rip + 6968008) = (unsigned int)((unsigned __int8)(v_cr8));
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 224)) == (*(unsigned __int64 *)(v_stack_mA0 + 32) + 224)) goto loc_00850AA4;
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(a4 + 52 + 29, a4 + 52, *(unsigned __int64 *)(v_stack_mA0 + 32), a4);
loc_00850610:
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 184)) & (0x40000ULL)) == 0) goto loc_008502F9;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32) + 2944)) != ((unsigned __int8)(result))) goto loc_008502F9;
    goto loc_008502FC;
loc_00850637:
    result = ExfReleasePushLock(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32), a4 + 52, (unsigned __int8)(result), a4);
    goto loc_008502AE;
loc_00850644:
    a1 = ((((unsigned __int8)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 186))) & (16)) == 0) ? 1 : 0;
    result = (((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 8)) & (8)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00850574;
loc_00850661:
    result = CmpCleanUpKcbCacheWithLock(*(unsigned __int64 *)(v_stack_mA0 + 32), v_stack_p60, (unsigned __int8)(result), a4);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 56)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_008506D0;
    result = CmpDecommisssionKcb(*(unsigned __int64 *)(v_stack_mA0 + 32), v_stack_p60, (unsigned __int8)(result), a4);
    goto loc_008506D0;
loc_00850687:
    *(unsigned __int64 *)(result) = *(unsigned __int64 *)(v_stack_mA0 + 32);
    *(unsigned __int64 *)(result + 8) = v_stack_p60;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 8) = result;
    *(unsigned __int64 *)(v_rip + 6967872) = result;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 6944138))) + 1);
    *(unsigned int *)(v_rip + 6944112) = (unsigned int)(result);
    if (((unsigned int)(result)) <= (*(unsigned int *)(v_rip + 6022638))) goto loc_00850AC1;
    result = ExReleaseFastMutex(v_rip + 6967783, v_stack_p60, (unsigned __int8)(result), a4);
    result = CmpArmDelayedCloseTimer(v_rip + 6967783, v_stack_p60, (unsigned __int8)(result), a4);
loc_008506D0:
    result = CmpUnlockKcb(*(unsigned __int64 *)(v_stack_mA0 + 32), v_stack_p60, (unsigned __int8)(result), a4);
    if (0 != 0) {
        a1 = 0;
        result = CmpUnlockKcb(a1, v_stack_p60, (unsigned __int8)(result), a4);
    }
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 16))))) >> (9));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 16)))));
    result = (unsigned int)((result) * ((unsigned int)(result)));
    a2 = ((unsigned int)((unsigned int)(result))) >> (9);
    a2 = (a2) ^ ((unsigned int)((unsigned int)(result)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32) + 1656))) - 1);
    a2 = (a2) & (a1);
    v_r15 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32) + 1648) + a2 + a2 * 2 * 8 + 8) = 0;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32) + 1648) + a2 + a2 * 2 * 8)) & (-16);
    a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32) + 1648) + a2 + a2 * 2 * 8) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32) + 1648) + a2 + a2 * 2 * 8))) & (2)) != 0) goto loc_00850A57;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32) + 1648) + a2 + a2 * 2 * 8))) & (2)) != 0) goto loc_00850A57;
loc_0085074C:
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32) + 1648) + a2 + a2 * 2 * 8, a2, (unsigned __int8)(result), a4);
    result = (unsigned int)((unsigned int)(v_r12));
    if (((unsigned int)((unsigned int)((unsigned int)(v_r12)))) == 1) {
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32);
        result = CmpDeleteHive(a1, a2, (unsigned __int8)(result), a4);
    }
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_p60, a2, (unsigned __int8)(result), a4);
    goto loc_008507C7;
loc_0085078A:
    if ((unsigned __int8)((unsigned __int8)(result)) == 0) goto loc_008507C4;
    result = CmLockHive(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32), a2, (unsigned __int8)(result), a4);
    result = (unsigned int)((1) & (127));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32) + result * 4 + 4240) = 19;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32) + 2936))) == 2) goto loc_008507EC;
loc_008507BC:
    result = CmUnlockHive(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32), a2, (unsigned __int8)(result), a4);
loc_008507C4:
    v_r15 = 0;
loc_008507C7:
    if ((unsigned __int8)(v_stack_p30) != 0) goto loc_00850A64;
    goto loc_0084FD5E;
loc_008507EC:
    result = (unsigned int)((1) & (127));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32) + result * 4 + 4240) = 20;
    result = 0;
    if (condition_is_not_equal) goto loc_008507BC;
    result = (unsigned int)((1) & (127));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32) + result * 4 + 4240) = 21;
    result = CmpReferenceHive(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32), (unsigned int)(v_stack_pE8), (unsigned int)(v_stack_pF0), a4);
    result = ExQueueWorkItem(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32) + 4816), 1, (unsigned int)(v_stack_pF0), a4);
    goto loc_008507BC;
loc_00850843:
    result = RtlUpcaseUnicodeChar(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32) + 4816), 1, (unsigned int)(v_stack_pF0), a4);
    goto loc_0084FF21;
loc_00850855:
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(a4 + 36 + 45, a4 + 36, v_stack_p50, a4);
loc_0085086D:
    result = KiRaiseIrqlProcessIrqlFlags((unsigned __int8)(v_stack_p50), (unsigned __int8)(v_stack_p50), v_stack_p50, a4);
    goto loc_008505AB;
loc_0085087F:
    if (!(condition_is_not_equal)) {
        v_r13 = 0;
        a4 = 0;
        a3 = v_stack_pF8;
        v_stack_p20 = 0;
        a2 = v_r13 + 36;
        a1 = a2 + 45;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    if (((*(unsigned __int8 *)(v_stack_pF8 + 64)) & (2)) == 0) goto loc_00850976;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 6967238, a2, a3, a4);
    if ((*(unsigned int *)(v_rip + 7824461)) != 0) goto loc_00850983;
loc_008508D9:
    if ((*(unsigned int *)(v_rip + 7824461)) >= 0) {
        a2 = result;
        a1 = v_rip + 6967186;
        result = ExpAcquireFastMutexContended(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int64 *)(v_rip + 6967164) = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned int *)(v_rip + 6967194) = 1;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_pF8 + 64))) & (2)) == 0) goto loc_0085096A;
    if ((((unsigned __int8)(*(unsigned __int8 *)(v_stack_pF8 + 64))) & (4)) != 0) goto loc_00850B53;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pF8 + 224) + 8)) != (v_stack_pF8 + 224)) goto loc_0085093F;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pF8 + 224 + 8))) != (v_stack_pF8 + 224)) {
        a1 = 3;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pF8 + 224 + 8)) = *(unsigned __int64 *)(v_stack_pF8 + 224);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_pF8 + 224) + 8) = *(unsigned __int64 *)(v_stack_pF8 + 224 + 8);
loc_0085095A:
    *(unsigned __int64 *)(a1 + 8) = a1;
    *(unsigned __int64 *)(a1) = a1;
loc_0085096A:
    result = ExReleaseFastMutex(v_rip + 6967055, *(unsigned __int64 *)(v_stack_pF8 + 224), a3, a4);
loc_00850976:
    result = CmpUnlockKcb(v_stack_pF8, *(unsigned __int64 *)(v_stack_pF8 + 224), a3, a4);
    goto loc_0084FF6D;
loc_00850983:
    result = KiRaiseIrqlProcessIrqlFlags(1, 1, a3, a4);
    goto loc_008508D9;
loc_00850995:
    v_r14 = 0;
    goto loc_00850136;
loc_008509A1:
    if (*(unsigned __int64 *)(result + 24) == 0) goto loc_0085051A;
    result = CmpUnlockKcb(0, 1, a3, a4);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24) + 16) + 48, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 24) + 16) + 48;
        a2 = result;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 24) + 16) + 48;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a3 = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24) + 16) + 56) = *(unsigned __int64 *)(gs_base + (0 + 392));
    a2 = 0;
    result = KeAbPreAcquire(v_r15 + 48, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_r15 + 48;
        a2 = result;
        a1 = v_r15 + 48;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int64 *)(v_r15 + 56) = *(unsigned __int64 *)(gs_base + (0 + 392));
    goto loc_0085051A;
loc_00850A3F:
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(a4 + 36 + 45, a4 + 36, result, a4);
loc_00850A57:
    result = ExfReleasePushLock(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24) + 16), a4 + 36, result, a4);
    goto loc_0085074C;
loc_00850A64:
    result = CmpLockHashEntrySharedByKcb(result, a4 + 36, result, a4);
    result = CmpLockKcbShared(result, a4 + 36, result, a4);
loc_00850A77:
    result = CmpUnlockKcb(result, a4 + 36, result, a4);
    goto loc_008503E2;
loc_00850A89:
    v_stack_p20 = result;
    result = KeBugCheckEx(8 + 15 + 58, 8 + 15, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32), 8);
loc_00850AA4:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 6966837) + 8)) != (v_rip + 6966830)) goto loc_0085093F;
    goto loc_00850687;
loc_00850AC1:
    result = ExReleaseFastMutex(*(unsigned __int64 *)(v_rip + 6966837), v_rip + 6966830, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32), 8);
    goto loc_008506D0;
loc_00850ACB:
    v_rbp = (unsigned __int16)((*(unsigned __int16 *)(v_r14)) >> (1));
    v_stack_p80 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 6966837) + 24));
    v_stack_p82 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 6966837) + 24));
    v_rsi = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 6966837) + 24)) >> (1));
    v_stack_p88 = v_rip + 6966830;
loc_00850AF5:
    if ((unsigned __int16)(v_rbp) == 0) goto loc_00850053;
    if ((unsigned __int16)(v_rsi) == 0) goto loc_00850053;
    v_r12 = (*(unsigned __int64 *)(v_r14 + 8)) + (2);
    a2 = (v_rip + 6966830) + (2);
    v_stack_p40 = a2;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r14 + 8)))) != ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 6966830)))) goto loc_00850B30;
loc_00850B23:
    v_rbp = (unsigned __int16)((v_rbp) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    v_rsi = (unsigned __int16)((v_rsi) + ((unsigned __int16)((unsigned int)(0xFFFFULL))));
    goto loc_00850AF5;
loc_00850B30:
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r14 + 8)))) < 97) goto loc_00850B48;
    if (((unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(v_r14 + 8)))) > 122) goto loc_00851252;
    a1 = (unsigned __int16)((*(unsigned __int16 *)(*(unsigned __int64 *)(v_r14 + 8))) + ((unsigned __int16)((unsigned int)(0xFFE0ULL))));
loc_00850B48:
    if (((unsigned __int16)(a1)) == ((unsigned __int16)(*(unsigned __int16 *)(v_rip + 6966830)))) goto loc_00850B23;
    goto loc_0085005C;
loc_00850B53:
    *(unsigned __int8 *)(*(unsigned __int64 *)(a1)) = 0;
    goto loc_0085095A;
loc_00850B62:
    result = CmpCleanUpKcbCacheWithLock(result, v_stack_p60, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32), 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 4176) = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = (unsigned int)((1) & (127));
    *(unsigned int *)(*(unsigned __int64 *)(result + 32) + result * 4 + 4240) = 31;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 160)))) & (32)) != 0) goto loc_008506D0;
    result = CmpDereferenceHive(*(unsigned __int64 *)(result + 32), v_stack_p60, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32), 8);
    goto loc_008506D0;
loc_00850BC3:
    if ((*(unsigned __int8 *)(v_rip + 6942586)) == 0) goto loc_00851248;
    if ((*(unsigned __int64 *)(v_rip + 6942555)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00851248;
    if (a5 == 0) goto loc_00851248;
    a2 = (unsigned int)(((unsigned int)(v_stack_pE8)) - 1);
    result = CmpGetComponentNameAtIndex(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24) + 16), a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32), 8);
    result = CmpWaitForHiveMount(result, a2, *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_mA0 + 32) + 32), a5 + 136);
    if ((unsigned __int8)(result) == 0) goto loc_00851248;
    goto loc_00850C48;
loc_00850C36:
loc_00850C48:
    result = CmpRecordParseFailure(a5, (unsigned int)(0x60500ULL), (unsigned int)((unsigned int)((unsigned int)(0xC0000425ULL))), a5 + 136);
    if (v_r12 == 1) goto loc_0085003B;
    result = CmpUnlockKcb(result, (unsigned int)(0x60500ULL), (unsigned int)((unsigned int)((unsigned int)(0xC0000425ULL))), a5 + 136);
    if (v_stack_p30 == 0) goto loc_00850D33;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 16))))) >> (9));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 16)))));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 16))) * ((unsigned int)(a1)));
    a2 = ((unsigned int)((unsigned int)(result))) >> (9);
    a2 = (a2) ^ ((unsigned int)((unsigned int)(result)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 1656))) - 1);
    a2 = (a2) & (a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8 + 8) = 0;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 16))))) >> (9));
    a1 = (unsigned int)((a1) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 16)))));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 16))) * ((unsigned int)(a1)));
    a2 = ((unsigned int)((unsigned int)(result))) >> (9);
    a2 = (a2) ^ ((unsigned int)((unsigned int)(result)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 1656))) - 1);
    a2 = (a2) & (a1);
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8)) & (-16);
    a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8))) & (2)) != 0) goto loc_00850FC7;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8))) & (2)) != 0) goto loc_00850FC7;
loc_00850D1B:
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8, a2, *(unsigned __int64 *)(result + 32), a5 + 136);
    if (((unsigned int)((unsigned int)((unsigned int)(v_r12)))) == 1) goto loc_00850D98;
loc_00850D33:
    v_stack_p70 = v_xmm0;
    result = CmpInitializeDelayDerefContext(v_stack_p70, a2, *(unsigned __int64 *)(result + 32), a5 + 136);
loc_00850D4C:
    if ((*(unsigned __int64 *)(result)) <= 1) goto loc_00850DA2;
    if ((*(unsigned __int64 *)(result) - 1) == 2) goto loc_00850FA1;
loc_00850D60:
    a3 = 0;
loc_00850D63:
    if ((*(unsigned __int64 *)(result)) != (*(unsigned __int64 *)(result) - 1 + 1)) goto loc_00850D4C;
    if ((*(unsigned __int64 *)(result)) >= (*(unsigned __int64 *)(result) - 1)) goto loc_008510C9;
    a4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(a4 + 37 + 44, a4 + 37, result, a4);
loc_00850D98:
    result = CmpDeleteHive(*(unsigned __int64 *)(result + 32), a4 + 37, result, a4);
    goto loc_00850D33;
loc_00850DA2:
    a3 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 16))))) >> (9));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 16)))));
    result = (unsigned int)((result) * ((unsigned int)(result)));
    a2 = ((unsigned int)((unsigned int)(result))) >> (9);
    a2 = (a2) ^ ((unsigned int)((unsigned int)(result)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 1656))) - 1);
    a2 = (a2) & (a1);
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8;
        a2 = result;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8 + 8) = *(unsigned __int64 *)(gs_base + (0 + 392));
loc_00850E27:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 4232))) == 0) goto loc_00851178;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 4232))) != 0) goto loc_00850E27;
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(result + 48, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = result + 48;
        a2 = result;
        a1 = result + 48;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_r13 = 0;
    *(unsigned __int64 *)(result + 56) = *(unsigned __int64 *)(gs_base + (0 + 392));
    if (*(unsigned __int64 *)(result + 192) != 0) goto loc_0085101E;
loc_00850E92:
    result = (v_r12) - 1;
    if (result == 2) goto loc_00851220;
    if (result != 0) goto loc_00850EF8;
    if (((*(unsigned int *)(result + 184)) & (0x40000ULL)) != 0) goto loc_008511BB;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 8))) >> (17));
    result = (unsigned __int8)(~(result));
    result = (unsigned __int8)((result) & (1));
    a2 = 0;
    if ((((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 8)))))) & (32)) == 0) { a2 = (unsigned int)((unsigned __int8)(result)); }
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 6020576))) != 0) goto loc_00850FD4;
loc_00850EE8:
    if ((unsigned __int8)(a2) == 0) goto loc_00850FF1;
    result = CmpAddToDelayedClose(result, a2, a3, a4);
loc_00850EF8:
    result = CmpUnlockKcb(result, a2, a3, a4);
    if (0 != 0) {
        a1 = 0;
        result = CmpUnlockKcb(a1, a2, a3, a4);
    }
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(result + 16))))) >> (9));
    result = (unsigned int)((result) ^ ((unsigned int)((unsigned int)(*(unsigned int *)(result + 16)))));
    result = (unsigned int)((result) * ((unsigned int)(result)));
    a2 = ((unsigned int)((unsigned int)(result))) >> (9);
    a2 = (a2) ^ ((unsigned int)((unsigned int)(result)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(result + 32) + 1656))) - 1);
    a2 = (a2) & (a1);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8 + 8) = 0;
    a1 = (*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8)) & (-16);
    a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8))) & (2)) != 0) goto loc_0085116B;
    if ((((unsigned __int8)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8))) & (2)) != 0) goto loc_0085116B;
loc_00850F71:
    result = KeAbPostRelease(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 1648) + a2 + a2 * 2 * 8, a2, a3, a4);
    if (((unsigned int)(v_r12)) == 1) {
        a1 = *(unsigned __int64 *)(result + 32);
        result = CmpDeleteHive(a1, a2, a3, a4);
    }
    a2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_p70, a2, a3, a4);
    goto loc_00850409;
loc_00850FA1:
    if (((*(unsigned int *)(result + 184)) & (0x40000ULL)) == 0) goto loc_00850D60;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(result + 32) + 2944)) != 1) goto loc_00850D60;
    goto loc_00850D63;
loc_00850FC7:
    result = ExfReleasePushLock(*(unsigned __int64 *)(result + 32), a2, 1, a4);
    goto loc_00850D1B;
loc_00850FD4:
    a1 = ((((unsigned __int8)(*(unsigned __int16 *)(result + 186))) & (16)) == 0) ? 1 : 0;
    result = (((*(unsigned __int8 *)(result + 8)) & (8)) == 0) ? 1 : 0;
    if ((((unsigned __int8)(result)) & ((unsigned __int8)(a1))) == 0) goto loc_00850EE8;
loc_00850FF1:
    result = CmpCleanUpKcbCacheWithLock(result, v_stack_p70, 1, a4);
    if ((*(unsigned __int64 *)(result + 56)) == (*(unsigned __int64 *)(gs_base + (0 + 392)))) goto loc_00850EF8;
    result = CmpDecommisssionKcb(result, v_stack_p70, 1, a4);
    goto loc_00850EF8;
loc_0085101E:
    if (*(unsigned __int64 *)(result + 24) == 0) goto loc_00850E92;
    result = CmpUnlockKcb(result, v_stack_p70, 1, a4);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24) + 16) + 48, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 24) + 16) + 48;
        a2 = result;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 24) + 16) + 48;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a3 = 0;
    a2 = 0;
    v_rbp = (v_stack_p38) + (48);
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24) + 16) + 56) = *(unsigned __int64 *)(gs_base + (0 + 392));
    result = KeAbPreAcquire(v_rbp, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rbp;
        a2 = result;
        a1 = v_rbp;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    *(unsigned __int64 *)(v_stack_p38 + 56) = *(unsigned __int64 *)(gs_base + (0 + 392));
    goto loc_00850E92;
loc_008510C9:
    if ((unsigned __int8)(a3) == 0) goto loc_00850409;
    result = CmLockHive(*(unsigned __int64 *)(result + 32), a2, a3, a4);
    result = (unsigned int)((1) & (127));
    *(unsigned int *)(*(unsigned __int64 *)(result + 32) + result * 4 + 4240) = 19;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 2936))) == 2) goto loc_00851113;
loc_00851106:
    result = CmUnlockHive(*(unsigned __int64 *)(result + 32), a2, 1, a4);
    goto loc_00850409;
loc_00851113:
    result = (unsigned int)((1) & (127));
    *(unsigned int *)(*(unsigned __int64 *)(result + 32) + result * 4 + 4240) = 20;
    result = 0;
    if (condition_is_not_equal) goto loc_00851106;
    result = (unsigned int)((1) & (127));
    *(unsigned int *)(*(unsigned __int64 *)(result + 32) + result * 4 + 4240) = 21;
    result = CmpReferenceHive(*(unsigned __int64 *)(result + 32), a2, 1, a4);
    result = ExQueueWorkItem(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) + 4816), 1, 1, a4);
    goto loc_00851106;
loc_0085116B:
    result = ExfReleasePushLock(*(unsigned __int64 *)(*(unsigned __int64 *)(result + 24) + 16), 1, 1, a4);
    goto loc_00850F71;
loc_00851178:
    v_stack_p20 = v_stack_p38;
    result = KeBugCheckEx(8 + 15 + 58, 8 + 15, *(unsigned __int64 *)(result + 32), 8);
loc_00851193:
    if (((*(unsigned int *)(v_stack_p38 + 184)) & (0x40000ULL)) == 0) goto loc_008506D0;
    if ((*(unsigned __int8 *)(8 + 15 + 58 + 2944)) != 1) goto loc_008506D0;
    result = CmpDoQueueLateUnloadWorker(8 + 15 + 58, 8 + 15, *(unsigned __int64 *)(result + 32), 8);
    goto loc_008506D0;
loc_008511BB:
    result = CmpCleanUpKcbCacheWithLock(v_stack_p38, v_stack_p70, *(unsigned __int64 *)(result + 32), 8);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_stack_p38 + 32) + 4176) = *(unsigned __int64 *)(gs_base + (0 + 392));
    a3 = (unsigned int)((1) & (127));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_p38 + 32) + a3 * 4 + 4240) = 31;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p38 + 32) + 160)))) & (32)) != 0) goto loc_00850EF8;
    result = CmpDereferenceHive(*(unsigned __int64 *)(v_stack_p38 + 32), v_stack_p70, a3, 8);
    goto loc_00850EF8;
loc_00851220:
    if (((*(unsigned int *)(v_stack_p38 + 184)) & (0x40000ULL)) == 0) goto loc_00850EF8;
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_stack_p38 + 32) + 2944)) != 1) goto loc_00850EF8;
    result = CmpDoQueueLateUnloadWorker(*(unsigned __int64 *)(v_stack_p38 + 32), v_stack_p70, a3, 8);
    goto loc_00850EF8;
loc_00851248:
    goto loc_00850C48;
loc_00851252:
    result = RtlUpcaseUnicodeChar(*(unsigned __int64 *)(v_stack_p38 + 32), (unsigned int)(0x60400ULL), a3, 8);
    goto loc_00850B48;
loc_00851264:
    goto loc_00850A77;
}
```

## 5. (Beta) C Style

```c
int64_t CmpPerformCompleteKcbCacheLookup(int64_t Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, int64_t Arg5, void *Arg6, void *Arg7, void *Arg8)
{
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg8 = (uint8_t *)Arg8;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m54;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint32_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint16_t v_stack_mA4;
    uint16_t v_stack_mA6;
    uint8_t v_stack_mA8;
    uint64_t v_stack_mB8;
    uint32_t v_stack_p0;
    uint32_t v_stack_p10;
    uint32_t v_stack_p18;
    uint64_t v_stack_p20;
    uint8_t v_stack_p30;
    uint16_t v_stack_p34;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p50;
    uint64_t v_stack_p60;
    uint64_t v_stack_p70;
    uint64_t v_stack_p8;
    uint16_t v_stack_p80;
    uint16_t v_stack_p82;
    uint64_t v_stack_p88;
    uint32_t v_stack_pE8;
    uint32_t v_stack_pF0;
    uint64_t v_stack_pF8;

    v_stack_p20 = Arg4;
    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (152);
    local_r15 = 0;
    v_stack_m88 = Arg1;
    v_stack_mA4 = 0;
loc_0084FD5E:
    local_r14 = 0;
    v_stack_m80 = *(uint64_t *)(Arg1 + 0x20);
    v_stack_mA6 = 0;
    v_stack_mA8 = 0;
    result = (local_r15 + 1) + (1);
    if (condition_is_equal) goto loc_00850855;
    if (result != 1) goto loc_0084FDAC;
    local_r14 = 0;
loc_0084FD94:
    Arg4 = 0;
    v_stack_mB8 = 0;
    Arg3 = 0;
    result = KeBugCheckEx(Arg4 + 21 + 60, Arg4 + 21, Arg3, Arg4);
loc_0084FDAC:
    v_stack_mA0 = Arg1;
loc_0084FDBA:
    v_stack_m90 = (uint32_t)((uint32_t)((uint32_t)(Arg4 + 21)));
    if (((uint32_t)((uint32_t)((uint32_t)(Arg4 + 21)))) >= 0) goto loc_00850995;
    if (((uint32_t)((uint32_t)((uint32_t)(Arg4 + 21)))) >= 8) goto loc_00850348;
    local_r14 = ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4 + 21)))) + 2) << (4);
    local_r14 = (local_r14) + (0);
loc_0084FDE3:
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1 + 0x10))) * ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x10)))));
    Arg3 = 0;
    Arg2 = 0;
    local_rbx = (uint32_t)((local_rbx) + ((uint32_t)((uint32_t)(*(uint32_t *)(Arg4 + (uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg4 + 0x15)))) * 4)))));
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (9));
    result = (uint32_t)((result) ^ ((uint32_t)(local_rbx)));
    result = (uint32_t)((result) * ((uint32_t)(result)));
    local_rbp = ((uint32_t)((uint32_t)(result))) >> (9);
    local_rbp = (local_rbp) ^ ((uint32_t)((uint32_t)(result)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x678))) - 1);
    Arg1 = (Arg1) & (local_rbp);
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8, Arg2, Arg3, Arg4);
    result = 0;
    if (!(condition_is_equal)) {
        Arg4 = *(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = *(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
loc_0084FE61:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x1088))) == 0) goto loc_008503B2;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x1088))) != 0) goto loc_0084FE61;
    Arg4 = 0;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x678))) - 1);
    Arg1 = (Arg1) & (local_rbp);
    v_stack_m54 = 0;
loc_0084FE9E:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8 + 0x10) == 0) goto loc_00850095;
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8 + 0x10))) != ((uint32_t)(local_rbx))) goto loc_0085005C;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8 + 0x10) - 0x10 + 0x48)) != v_stack_mA0) goto loc_0085005C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8 + 0x10) - 0x10 + 0x50))))) & (1)) == 0) goto loc_00850ACB;
    local_rsi = (uint16_t)((*(uint16_t *)(local_r14)) >> (1));
loc_0084FEE4:
    if ((uint16_t)(local_rsi) == 0) goto loc_0084FF38;
    if ((uint16_t)(*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8 + 0x10) - 0x10 + 0x50) + 0x18)) == 0) goto loc_0084FF38;
    local_r13 = (*(uint64_t *)(local_r14 + 0x8)) + (2);
    Arg2 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8 + 0x10) - 0x10 + 0x50) + 26) + 1;
    v_stack_m98 = Arg2;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_r14 + 0x8)))) == ((uint16_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8 + 0x10) - 0x10 + 0x50) + 0x1A)))) goto loc_0084FF2B;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_r14 + 0x8)))) < 97) goto loc_0084FF21;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_r14 + 0x8)))) > 122) goto loc_00850843;
    Arg1 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(local_r14 + 0x8))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_0084FF21:
    if (((uint16_t)(Arg1)) != ((uint16_t)(*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8 + 0x10) - 0x10 + 0x50) + 0x1A)))) goto loc_0085005C;
loc_0084FF2B:
    local_rsi = (uint16_t)((local_rsi) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    local_rbp = (uint16_t)((*(uint16_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8 + 0x10) - 0x10 + 0x50) + 0x18)) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    goto loc_0084FEE4;
loc_0084FF38:
    if (((uint16_t)(local_rsi)) != ((uint16_t)(local_rbp))) goto loc_0085005C;
loc_0084FF41:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8 + 0x10) - 16 == 0) goto loc_00850095;
loc_0084FF50:
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8 + 0x10) - 0x10) == 0) goto loc_00850065;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8 + 0x10) - 0x10) + 1 == 0) goto loc_0085088B;
    if (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8 + 0x10) - 0x10) + 1 != 0) goto loc_0084FF50;
loc_0084FF6D:
    if (((uint32_t)((uint32_t)(v_stack_m90))) == ((uint32_t)((uint32_t)(v_stack_p18) - 1))) goto loc_00850331;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (9));
    result = (uint32_t)((result) ^ ((uint32_t)(local_rbx)));
    result = (uint32_t)((result) * ((uint32_t)(result)));
    Arg2 = ((uint32_t)((uint32_t)(result))) >> (9);
    Arg2 = (Arg2) ^ ((uint32_t)((uint32_t)(result)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x678))) - 1);
    Arg2 = (Arg2) & (Arg1);
    Arg3 = 0;
    *(uint64_t *)(*(uint64_t *)(v_stack_m80 + 0x670) + Arg2 + Arg2 * 2 * 8 + 0x8) = 0;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m80 + 0x670) + Arg2 + Arg2 * 2 * 8)) & (-16);
    Arg2 = *(uint64_t *)(*(uint64_t *)(v_stack_m80 + 0x670) + Arg2 + Arg2 * 2 * 8) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m80 + 0x670) + Arg2 + Arg2 * 2 * 8))) & (2)) != 0) goto loc_008503A5;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m80 + 0x670) + Arg2 + Arg2 * 2 * 8))) & (2)) != 0) goto loc_008503A5;
loc_0084FFF2:
    result = KeAbPostRelease(*(uint64_t *)(v_stack_m80 + 0x670) + Arg2 + Arg2 * 2 * 8, Arg2, Arg3, Arg4);
    result = (uint32_t)(0xFFFFFFFFULL);
    if (((uint32_t)((uint32_t)(0xFFFFFFFFULL))) == 1) {
        Arg1 = v_stack_m80;
        result = CmpDeleteHive(Arg1, Arg2, Arg3, Arg4);
    }
loc_0085001D:
    if (-1 != 1) goto loc_00850370;
    local_r14 = 0;
loc_0085003B:
    Arg4 = 0;
    v_stack_mB8 = 0;
    Arg3 = 0;
    result = KeBugCheckEx(Arg4 + 31 + 50, Arg4 + 31, Arg3, Arg4);
loc_00850053:
    if (((uint16_t)(local_rbp)) == ((uint16_t)(*(uint64_t *)(v_stack_m80 + 0x670) + Arg2 + Arg2 * 2 * 8))) goto loc_0084FF41;
loc_0085005C:
    goto loc_0084FE9E;
loc_00850065:
    result = CmpLockKcbShared(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8 + 0x10) - 16, Arg4 + 31, Arg3, Arg4);
    if (((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8 + 0x10) - 0x10 + 0x8)) & (0x80000ULL)) == 0) goto loc_0085087F;
    local_r13 = 0;
    Arg4 = 0;
    v_stack_mB8 = 0;
    result = KeBugCheckEx(local_r13 + 32 + 49, local_r13 + 32, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8 + 0x10) - 16, Arg4);
loc_00850095:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (9));
    result = (uint32_t)((result) ^ ((uint32_t)(local_rbx)));
    result = (uint32_t)((result) * ((uint32_t)(result)));
    Arg2 = ((uint32_t)((uint32_t)(result))) >> (9);
    Arg2 = (Arg2) ^ ((uint32_t)((uint32_t)(result)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m80 + 0x678))) - 1);
    Arg2 = (Arg2) & (Arg1);
    local_r14 = 0;
    *(uint64_t *)(*(uint64_t *)(v_stack_m80 + 0x670) + Arg2 + Arg2 * 2 * 8 + 0x8) = 0;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(v_stack_m80 + 0x670) + Arg2 + Arg2 * 2 * 8)) & (-16);
    Arg2 = *(uint64_t *)(*(uint64_t *)(v_stack_m80 + 0x670) + Arg2 + Arg2 * 2 * 8) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m80 + 0x670) + Arg2 + Arg2 * 2 * 8))) & (2)) != 0) goto loc_008503CF;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(v_stack_m80 + 0x670) + Arg2 + Arg2 * 2 * 8))) & (2)) != 0) goto loc_008503CF;
loc_00850100:
    result = KeAbPostRelease(*(uint64_t *)(v_stack_m80 + 0x670) + Arg2 + Arg2 * 2 * 8, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8 + 0x10) - 16, Arg4);
    if (-1 == 1) goto loc_0085033B;
loc_00850124:
loc_00850136:
    if (v_stack_m88 == v_stack_p8) goto loc_00850158;
    if (-1 == 1) goto loc_0085003B;
loc_00850158:
    Arg2 = (uint16_t)((v_stack_mA4) + ((uint16_t)(v_stack_mA6)));
    v_stack_mA4 = (uint16_t)(Arg2);
    if (((*(uint32_t *)(v_stack_mA0 + 0xB8)) & (0x20000ULL)) == 0) goto loc_008503DC;
    result = CmpLockKcbShared(v_stack_mA0, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8 + 0x10) - 16, Arg4);
    if (((*(uint32_t *)(v_stack_mA0 + 0xB8)) & (0x20000ULL)) == 0) goto loc_00851264;
    v_stack_m88 = *(uint64_t *)(v_stack_mA0 + 0x68);
    result = (1) + (1);
    if (condition_is_equal) goto loc_00850A3F;
    if (result == 1) goto loc_0084FD94;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x68) + 0x20) + 0xA0)))) & (32)) == 0) goto loc_008501E5;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x68) + 0x20) + 0x1048)) != (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00850BC3;
loc_008501E5:
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_mA0 + 0x68) + 0x8)) & (0x40000ULL)) != 0) goto loc_00850C36;
    result = CmpUnlockKcb(v_stack_mA0, Arg2, *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(Arg1 + 0x20) + 0x670) + Arg1 + Arg1 * 2 * 8 + 0x10) - 16, Arg4);
    local_r13 = 0;
    if ((uint8_t)(v_stack_mA8) == 0) goto loc_008502C9;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x10))))) >> (9));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x10)))));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x10))) * ((uint32_t)(Arg1)));
    Arg2 = ((uint32_t)((uint32_t)(result))) >> (9);
    Arg2 = (Arg2) ^ ((uint32_t)((uint32_t)(result)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x678))) - 1);
    Arg2 = (Arg2) & (Arg1);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8 + 0x8) = 0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x10))))) >> (9));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x10)))));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_mA0 + 0x10))) * ((uint32_t)(Arg1)));
    Arg2 = ((uint32_t)((uint32_t)(result))) >> (9);
    Arg2 = (Arg2) ^ ((uint32_t)((uint32_t)(result)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x678))) - 1);
    Arg2 = (Arg2) & (Arg1);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8)) & (-16);
    Arg2 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8))) & (2)) != 0) goto loc_00850637;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8))) & (2)) != 0) goto loc_00850637;
loc_008502AE:
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8, Arg2, *(uint64_t *)(v_stack_mA0 + 0x20), Arg4);
    if (-1 == 1) goto loc_00850420;
loc_008502C9:
    v_stack_m78 = v_xmm0;
    result = CmpInitializeDelayDerefContext(v_stack_m78, Arg2, *(uint64_t *)(v_stack_mA0 + 0x20), Arg4);
loc_008502E2:
    if ((*(uint64_t *)(v_stack_mA0)) <= 1) goto loc_0085042D;
    if ((*(uint64_t *)(v_stack_mA0) - 1) == 2) goto loc_00850610;
loc_008502F9:
    Arg3 = 0;
loc_008502FC:
    if ((*(uint64_t *)(v_stack_mA0)) != (*(uint64_t *)(v_stack_mA0) - 1 + 1)) goto loc_008502E2;
    if ((*(uint64_t *)(v_stack_mA0)) >= (*(uint64_t *)(v_stack_mA0) - 1)) goto loc_0085078A;
    Arg4 = 0;
    v_stack_mB8 = 0;
    result = KeBugCheckEx(Arg4 + 37 + 44, Arg4 + 37, v_stack_mA0, Arg4);
loc_00850331:
    v_stack_mA8 = 1;
    goto loc_0085001D;
loc_0085033B:
    result = CmpDeleteHive(0, Arg4 + 37, v_stack_mA0, Arg4);
    goto loc_00850124;
loc_00850348:
    local_r14 = ((uint32_t)((uint32_t)(-1 - 8))) + (6);
    local_r14 = (local_r14) << (4);
    local_r14 = (local_r14) + (*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0xA0));
    goto loc_0084FDE3;
loc_00850370:
    Arg1 = (uint16_t)((v_stack_mA6) + 1);
    v_stack_mA0 = *(uint64_t *)(v_stack_mA0 + 0x20);
    v_stack_mA6 = (uint16_t)(Arg1);
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0xB8)) & (0x100000ULL)) != 0) goto loc_00850995;
    local_r12 = (uint32_t)((-1) + 1);
    goto loc_0084FDBA;
loc_008503A5:
    result = ExfReleasePushLock(1, Arg4 + 37, v_stack_mA0, Arg4);
    goto loc_0084FFF2;
loc_008503B2:
    v_stack_mB8 = (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_mA0 + 0x20)));
    result = KeBugCheckEx(9 + 14 + 58, 9 + 14, 0, 9);
loc_008503CF:
    result = ExfReleasePushLock(*(uint64_t *)(v_stack_mA0 + 0x20), 9 + 14, 0, 9);
    goto loc_00850100;
loc_008503DC:
loc_008503E2:
    local_r13 = 0;
    *(uint64_t *)(arg6) = *(uint64_t *)(v_stack_mA0 + 0x20);
    *(uint8_t *)(arg7) = (uint8_t)(v_stack_mA8);
    *(uint16_t *)(arg8) = (uint16_t)(9 + 14);
loc_00850409:
    local_rsp = (local_rsp) + (152);
    return 0;
loc_00850420:
    result = CmpDeleteHive(v_stack_p20, 9 + 14, 0, 9);
    goto loc_008502C9;
loc_0085042D:
    Arg3 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x10))))) >> (9));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x10)))));
    result = (uint32_t)((result) * ((uint32_t)(result)));
    Arg2 = ((uint32_t)((uint32_t)(result))) >> (9);
    Arg2 = (Arg2) ^ ((uint32_t)((uint32_t)(result)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20) + 0x678))) - 1);
    Arg2 = (Arg2) & (Arg1);
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8, Arg2, Arg3, 9);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8;
        Arg2 = result;
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, 9);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8 + 0x8) = *(uint64_t *)(gs_base + (0 + 0x188));
loc_008504B2:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20) + 0x1088))) == 0) goto loc_00850A89;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20) + 0x1088))) != 0) goto loc_008504B2;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(v_stack_mA0 + 0x20) + 48, Arg2, Arg3, 9);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(v_stack_mA0 + 0x20) + 48;
        Arg2 = result;
        Arg1 = *(uint64_t *)(v_stack_mA0 + 0x20) + 48;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, 9);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x38) = *(uint64_t *)(gs_base + (0 + 0x188));
    if (*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0xC0) != 0) goto loc_008509A1;
loc_0085051A:
    result = (local_r12) - 1;
    if (result == 2) goto loc_00851193;
    if (result != 0) goto loc_008506D0;
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0xB8)) & (0x40000ULL)) != 0) goto loc_00850B62;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x8))) >> (17));
    result = (uint8_t)(~(result));
    result = (uint8_t)((result) & (1));
    Arg2 = 0;
    if ((((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x8)))))) & (32)) == 0) { Arg2 = (uint32_t)((uint8_t)(result)); }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5BE754))) != 0) goto loc_00850644;
loc_00850574:
    if ((uint8_t)(Arg2) == 0) goto loc_00850661;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 6968058, Arg2, Arg3, 9);
    if ((*(uint32_t *)(v_rip + 0x77677B)) != 0) goto loc_0085086D;
loc_008505AB:
    if ((*(uint32_t *)(v_rip + 0x77677B)) >= 0) {
        Arg2 = result;
        Arg1 = v_rip + 6968000;
        result = ExpAcquireFastMutexContended(Arg1, Arg2, 1, 9);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint64_t *)(v_rip + 0x6A52AA) = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint32_t *)(v_rip + 0x6A52C8) = (uint32_t)((uint8_t)(v_cr8));
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0xE0)) == (*(uint64_t *)(v_stack_mA0 + 0x20) + 224)) goto loc_00850AA4;
    Arg4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(Arg4 + 52 + 29, Arg4 + 52, *(uint64_t *)(v_stack_mA0 + 0x20), Arg4);
loc_00850610:
    if (((*(uint32_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0xB8)) & (0x40000ULL)) == 0) goto loc_008502F9;
    if ((*(uint8_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20) + 0xB80)) != ((uint8_t)(result))) goto loc_008502F9;
    goto loc_008502FC;
loc_00850637:
    result = ExfReleasePushLock(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20), Arg4 + 52, (uint8_t)(result), Arg4);
    goto loc_008502AE;
loc_00850644:
    Arg1 = ((((uint8_t)(*(uint16_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0xBA))) & (16)) == 0) ? 1 : 0;
    result = (((*(uint8_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x8)) & (8)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00850574;
loc_00850661:
    result = CmpCleanUpKcbCacheWithLock(*(uint64_t *)(v_stack_mA0 + 0x20), v_stack_p60, (uint8_t)(result), Arg4);
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x38)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_008506D0;
    result = CmpDecommisssionKcb(*(uint64_t *)(v_stack_mA0 + 0x20), v_stack_p60, (uint8_t)(result), Arg4);
    goto loc_008506D0;
loc_00850687:
    *(uint64_t *)(result) = *(uint64_t *)(v_stack_mA0 + 0x20);
    *(uint64_t *)(result + 0x8) = v_stack_p60;
    *(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x8) = result;
    *(uint64_t *)(v_rip + 0x6A5240) = result;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x69F58A))) + 1);
    *(uint32_t *)(v_rip + 0x69F570) = (uint32_t)(result);
    if (((uint32_t)(result)) <= (*(uint32_t *)(v_rip + 0x5BE5EE))) goto loc_00850AC1;
    result = ExReleaseFastMutex(v_rip + 6967783, v_stack_p60, (uint8_t)(result), Arg4);
    result = CmpArmDelayedCloseTimer(v_rip + 6967783, v_stack_p60, (uint8_t)(result), Arg4);
loc_008506D0:
    result = CmpUnlockKcb(*(uint64_t *)(v_stack_mA0 + 0x20), v_stack_p60, (uint8_t)(result), Arg4);
    if (0 != 0) {
        Arg1 = 0;
        result = CmpUnlockKcb(Arg1, v_stack_p60, (uint8_t)(result), Arg4);
    }
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x10))))) >> (9));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x10)))));
    result = (uint32_t)((result) * ((uint32_t)(result)));
    Arg2 = ((uint32_t)((uint32_t)(result))) >> (9);
    Arg2 = (Arg2) ^ ((uint32_t)((uint32_t)(result)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20) + 0x678))) - 1);
    Arg2 = (Arg2) & (Arg1);
    local_r15 = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8 + 0x8) = 0;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8)) & (-16);
    Arg2 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8))) & (2)) != 0) goto loc_00850A57;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8))) & (2)) != 0) goto loc_00850A57;
loc_0085074C:
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8, Arg2, (uint8_t)(result), Arg4);
    result = (uint32_t)((uint32_t)(local_r12));
    if (((uint32_t)((uint32_t)((uint32_t)(local_r12)))) == 1) {
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20);
        result = CmpDeleteHive(Arg1, Arg2, (uint8_t)(result), Arg4);
    }
    Arg2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_p60, Arg2, (uint8_t)(result), Arg4);
    goto loc_008507C7;
loc_0085078A:
    if ((uint8_t)((uint8_t)(result)) == 0) goto loc_008507C4;
    result = CmLockHive(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20), Arg2, (uint8_t)(result), Arg4);
    result = (uint32_t)((1) & (127));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20) + result * 4 + 0x1090) = 19;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20) + 0xB78))) == 2) goto loc_008507EC;
loc_008507BC:
    result = CmUnlockHive(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20), Arg2, (uint8_t)(result), Arg4);
loc_008507C4:
    local_r15 = 0;
loc_008507C7:
    if ((uint8_t)(v_stack_p30) != 0) goto loc_00850A64;
    goto loc_0084FD5E;
loc_008507EC:
    result = (uint32_t)((1) & (127));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20) + result * 4 + 0x1090) = 20;
    result = 0;
    if (condition_is_not_equal) goto loc_008507BC;
    result = (uint32_t)((1) & (127));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20) + result * 4 + 0x1090) = 21;
    result = CmpReferenceHive(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20), (uint32_t)(v_stack_pE8), (uint32_t)(v_stack_pF0), Arg4);
    result = ExQueueWorkItem(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20) + 0x12D0), 1, (uint32_t)(v_stack_pF0), Arg4);
    goto loc_008507BC;
loc_00850843:
    result = RtlUpcaseUnicodeChar(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20) + 0x12D0), 1, (uint32_t)(v_stack_pF0), Arg4);
    goto loc_0084FF21;
loc_00850855:
    Arg4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(Arg4 + 36 + 45, Arg4 + 36, v_stack_p50, Arg4);
loc_0085086D:
    result = KiRaiseIrqlProcessIrqlFlags((uint8_t)(v_stack_p50), (uint8_t)(v_stack_p50), v_stack_p50, Arg4);
    goto loc_008505AB;
loc_0085087F:
    if (!(condition_is_not_equal)) {
        local_r13 = 0;
        Arg4 = 0;
        Arg3 = v_stack_pF8;
        v_stack_p20 = 0;
        Arg2 = local_r13 + 36;
        Arg1 = Arg2 + 45;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (((*(uint8_t *)(v_stack_pF8 + 0x40)) & (2)) == 0) goto loc_00850976;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 6967238, Arg2, Arg3, Arg4);
    if ((*(uint32_t *)(v_rip + 0x77644D)) != 0) goto loc_00850983;
loc_008508D9:
    if ((*(uint32_t *)(v_rip + 0x77644D)) >= 0) {
        Arg2 = result;
        Arg1 = v_rip + 6967186;
        result = ExpAcquireFastMutexContended(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint64_t *)(v_rip + 0x6A4F7C) = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint32_t *)(v_rip + 0x6A4F9A) = 1;
    if ((((uint8_t)(*(uint8_t *)(v_stack_pF8 + 0x40))) & (2)) == 0) goto loc_0085096A;
    if ((((uint8_t)(*(uint8_t *)(v_stack_pF8 + 0x40))) & (4)) != 0) goto loc_00850B53;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_pF8 + 0xE0) + 0x8)) != (v_stack_pF8 + 224)) goto loc_0085093F;
    if ((*(uint64_t *)(*(uint64_t *)(v_stack_pF8 + 0xE0 + 0x8))) != (v_stack_pF8 + 224)) {
        Arg1 = 3;
    }
    *(uint64_t *)(*(uint64_t *)(v_stack_pF8 + 0xE0 + 0x8)) = *(uint64_t *)(v_stack_pF8 + 0xE0);
    *(uint64_t *)(*(uint64_t *)(v_stack_pF8 + 0xE0) + 0x8) = *(uint64_t *)(v_stack_pF8 + 0xE0 + 0x8);
loc_0085095A:
    *(uint64_t *)(Arg1 + 0x8) = Arg1;
    *(uint64_t *)(Arg1) = Arg1;
loc_0085096A:
    result = ExReleaseFastMutex(v_rip + 6967055, *(uint64_t *)(v_stack_pF8 + 0xE0), Arg3, Arg4);
loc_00850976:
    result = CmpUnlockKcb(v_stack_pF8, *(uint64_t *)(v_stack_pF8 + 0xE0), Arg3, Arg4);
    goto loc_0084FF6D;
loc_00850983:
    result = KiRaiseIrqlProcessIrqlFlags(1, 1, Arg3, Arg4);
    goto loc_008508D9;
loc_00850995:
    local_r14 = 0;
    goto loc_00850136;
loc_008509A1:
    if (*(uint64_t *)(result + 0x18) == 0) goto loc_0085051A;
    result = CmpUnlockKcb(0, 1, Arg3, Arg4);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(result + 0x18) + 0x10) + 48, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(result + 0x18) + 0x10) + 48;
        Arg2 = result;
        Arg1 = *(uint64_t *)(*(uint64_t *)(result + 0x18) + 0x10) + 48;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    Arg3 = 0;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x18) + 0x10) + 0x38) = *(uint64_t *)(gs_base + (0 + 0x188));
    Arg2 = 0;
    result = KeAbPreAcquire(local_r15 + 48, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_r15 + 48;
        Arg2 = result;
        Arg1 = local_r15 + 48;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint64_t *)(local_r15 + 0x38) = *(uint64_t *)(gs_base + (0 + 0x188));
    goto loc_0085051A;
loc_00850A3F:
    Arg4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(Arg4 + 36 + 45, Arg4 + 36, result, Arg4);
loc_00850A57:
    result = ExfReleasePushLock(*(uint64_t *)(*(uint64_t *)(result + 0x18) + 0x10), Arg4 + 36, result, Arg4);
    goto loc_0085074C;
loc_00850A64:
    result = CmpLockHashEntrySharedByKcb(result, Arg4 + 36, result, Arg4);
    result = CmpLockKcbShared(result, Arg4 + 36, result, Arg4);
loc_00850A77:
    result = CmpUnlockKcb(result, Arg4 + 36, result, Arg4);
    goto loc_008503E2;
loc_00850A89:
    v_stack_p20 = result;
    result = KeBugCheckEx(8 + 15 + 58, 8 + 15, *(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20), 8);
loc_00850AA4:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x6A4E35) + 0x8)) != (v_rip + 6966830)) goto loc_0085093F;
    goto loc_00850687;
loc_00850AC1:
    result = ExReleaseFastMutex(*(uint64_t *)(v_rip + 0x6A4E35), v_rip + 6966830, *(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20), 8);
    goto loc_008506D0;
loc_00850ACB:
    local_rbp = (uint16_t)((*(uint16_t *)(local_r14)) >> (1));
    v_stack_p80 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x6A4E35) + 0x18));
    v_stack_p82 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(v_rip + 0x6A4E35) + 0x18));
    local_rsi = (uint16_t)((*(uint16_t *)(*(uint64_t *)(v_rip + 0x6A4E35) + 0x18)) >> (1));
    v_stack_p88 = v_rip + 6966830;
loc_00850AF5:
    if ((uint16_t)(local_rbp) == 0) goto loc_00850053;
    if ((uint16_t)(local_rsi) == 0) goto loc_00850053;
    local_r12 = (*(uint64_t *)(local_r14 + 0x8)) + (2);
    Arg2 = (v_rip + 6966830) + (2);
    v_stack_p40 = Arg2;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_r14 + 0x8)))) != ((uint16_t)(*(uint16_t *)(v_rip + 0x6A4E2E)))) goto loc_00850B30;
loc_00850B23:
    local_rbp = (uint16_t)((local_rbp) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    local_rsi = (uint16_t)((local_rsi) + ((uint16_t)((uint32_t)(0xFFFFULL))));
    goto loc_00850AF5;
loc_00850B30:
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_r14 + 0x8)))) < 97) goto loc_00850B48;
    if (((uint16_t)(*(uint16_t *)(*(uint64_t *)(local_r14 + 0x8)))) > 122) goto loc_00851252;
    Arg1 = (uint16_t)((*(uint16_t *)(*(uint64_t *)(local_r14 + 0x8))) + ((uint16_t)((uint32_t)(0xFFE0ULL))));
loc_00850B48:
    if (((uint16_t)(Arg1)) == ((uint16_t)(*(uint16_t *)(v_rip + 0x6A4E2E)))) goto loc_00850B23;
    goto loc_0085005C;
loc_00850B53:
    *(uint8_t *)(*(uint64_t *)(Arg1)) = 0;
    goto loc_0085095A;
loc_00850B62:
    result = CmpCleanUpKcbCacheWithLock(result, v_stack_p60, *(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20), 8);
    *(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x1050) = *(uint64_t *)(gs_base + (0 + 0x188));
    result = (uint32_t)((1) & (127));
    *(uint32_t *)(*(uint64_t *)(result + 0x20) + result * 4 + 0x1090) = 31;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0xA0)))) & (32)) != 0) goto loc_008506D0;
    result = CmpDereferenceHive(*(uint64_t *)(result + 0x20), v_stack_p60, *(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20), 8);
    goto loc_008506D0;
loc_00850BC3:
    if ((*(uint8_t *)(v_rip + 0x69EF7A)) == 0) goto loc_00851248;
    if ((*(uint64_t *)(v_rip + 0x69EF5B)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00851248;
    if (Arg5 == 0) goto loc_00851248;
    Arg2 = (uint32_t)(((uint32_t)(v_stack_pE8)) - 1);
    result = CmpGetComponentNameAtIndex(*(uint64_t *)(*(uint64_t *)(result + 0x18) + 0x10), Arg2, *(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20), 8);
    result = CmpWaitForHiveMount(result, Arg2, *(uint64_t *)(*(uint64_t *)(v_stack_mA0 + 0x20) + 0x20), Arg5 + 136);
    if ((uint8_t)(result) == 0) goto loc_00851248;
    goto loc_00850C48;
loc_00850C36:
loc_00850C48:
    result = CmpRecordParseFailure(Arg5, (uint32_t)(0x60500ULL), (uint32_t)((uint32_t)((uint32_t)(0xC0000425ULL))), Arg5 + 136);
    if (local_r12 == 1) goto loc_0085003B;
    result = CmpUnlockKcb(result, (uint32_t)(0x60500ULL), (uint32_t)((uint32_t)((uint32_t)(0xC0000425ULL))), Arg5 + 136);
    if (v_stack_p30 == 0) goto loc_00850D33;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10))))) >> (9));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)))));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x10))) * ((uint32_t)(Arg1)));
    Arg2 = ((uint32_t)((uint32_t)(result))) >> (9);
    Arg2 = (Arg2) ^ ((uint32_t)((uint32_t)(result)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0x678))) - 1);
    Arg2 = (Arg2) & (Arg1);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8 + 0x8) = 0;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10))))) >> (9));
    Arg1 = (uint32_t)((Arg1) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)))));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x10))) * ((uint32_t)(Arg1)));
    Arg2 = ((uint32_t)((uint32_t)(result))) >> (9);
    Arg2 = (Arg2) ^ ((uint32_t)((uint32_t)(result)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0x678))) - 1);
    Arg2 = (Arg2) & (Arg1);
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8)) & (-16);
    Arg2 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8))) & (2)) != 0) goto loc_00850FC7;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8))) & (2)) != 0) goto loc_00850FC7;
loc_00850D1B:
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8, Arg2, *(uint64_t *)(result + 0x20), Arg5 + 136);
    if (((uint32_t)((uint32_t)((uint32_t)(local_r12)))) == 1) goto loc_00850D98;
loc_00850D33:
    v_stack_p70 = v_xmm0;
    result = CmpInitializeDelayDerefContext(v_stack_p70, Arg2, *(uint64_t *)(result + 0x20), Arg5 + 136);
loc_00850D4C:
    if ((*(uint64_t *)(result)) <= 1) goto loc_00850DA2;
    if ((*(uint64_t *)(result) - 1) == 2) goto loc_00850FA1;
loc_00850D60:
    Arg3 = 0;
loc_00850D63:
    if ((*(uint64_t *)(result)) != (*(uint64_t *)(result) - 1 + 1)) goto loc_00850D4C;
    if ((*(uint64_t *)(result)) >= (*(uint64_t *)(result) - 1)) goto loc_008510C9;
    Arg4 = 0;
    v_stack_p20 = 0;
    result = KeBugCheckEx(Arg4 + 37 + 44, Arg4 + 37, result, Arg4);
loc_00850D98:
    result = CmpDeleteHive(*(uint64_t *)(result + 0x20), Arg4 + 37, result, Arg4);
    goto loc_00850D33;
loc_00850DA2:
    Arg3 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10))))) >> (9));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)))));
    result = (uint32_t)((result) * ((uint32_t)(result)));
    Arg2 = ((uint32_t)((uint32_t)(result))) >> (9);
    Arg2 = (Arg2) ^ ((uint32_t)((uint32_t)(result)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0x678))) - 1);
    Arg2 = (Arg2) & (Arg1);
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8;
        Arg2 = result;
        Arg1 = *(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8 + 0x8) = *(uint64_t *)(gs_base + (0 + 0x188));
loc_00850E27:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0x1088))) == 0) goto loc_00851178;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0x1088))) != 0) goto loc_00850E27;
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(result + 48, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = result + 48;
        Arg2 = result;
        Arg1 = result + 48;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_r13 = 0;
    *(uint64_t *)(result + 0x38) = *(uint64_t *)(gs_base + (0 + 0x188));
    if (*(uint64_t *)(result + 0xC0) != 0) goto loc_0085101E;
loc_00850E92:
    result = (local_r12) - 1;
    if (result == 2) goto loc_00851220;
    if (result != 0) goto loc_00850EF8;
    if (((*(uint32_t *)(result + 0xB8)) & (0x40000ULL)) != 0) goto loc_008511BB;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x8))) >> (17));
    result = (uint8_t)(~(result));
    result = (uint8_t)((result) & (1));
    Arg2 = 0;
    if ((((uint8_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x8)))))) & (32)) == 0) { Arg2 = (uint32_t)((uint8_t)(result)); }
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x5BDDE0))) != 0) goto loc_00850FD4;
loc_00850EE8:
    if ((uint8_t)(Arg2) == 0) goto loc_00850FF1;
    result = CmpAddToDelayedClose(result, Arg2, Arg3, Arg4);
loc_00850EF8:
    result = CmpUnlockKcb(result, Arg2, Arg3, Arg4);
    if (0 != 0) {
        Arg1 = 0;
        result = CmpUnlockKcb(Arg1, Arg2, Arg3, Arg4);
    }
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10))))) >> (9));
    result = (uint32_t)((result) ^ ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x10)))));
    result = (uint32_t)((result) * ((uint32_t)(result)));
    Arg2 = ((uint32_t)((uint32_t)(result))) >> (9);
    Arg2 = (Arg2) ^ ((uint32_t)((uint32_t)(result)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(result + 0x20) + 0x678))) - 1);
    Arg2 = (Arg2) & (Arg1);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8 + 0x8) = 0;
    Arg1 = (*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8)) & (-16);
    Arg2 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8))) & (2)) != 0) goto loc_0085116B;
    if ((((uint8_t)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8))) & (2)) != 0) goto loc_0085116B;
loc_00850F71:
    result = KeAbPostRelease(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x670) + Arg2 + Arg2 * 2 * 8, Arg2, Arg3, Arg4);
    if (((uint32_t)(local_r12)) == 1) {
        Arg1 = *(uint64_t *)(result + 0x20);
        result = CmpDeleteHive(Arg1, Arg2, Arg3, Arg4);
    }
    Arg2 = 0;
    result = CmpDrainDelayDerefContext(v_stack_p70, Arg2, Arg3, Arg4);
    goto loc_00850409;
loc_00850FA1:
    if (((*(uint32_t *)(result + 0xB8)) & (0x40000ULL)) == 0) goto loc_00850D60;
    if ((*(uint8_t *)(*(uint64_t *)(result + 0x20) + 0xB80)) != 1) goto loc_00850D60;
    goto loc_00850D63;
loc_00850FC7:
    result = ExfReleasePushLock(*(uint64_t *)(result + 0x20), Arg2, 1, Arg4);
    goto loc_00850D1B;
loc_00850FD4:
    Arg1 = ((((uint8_t)(*(uint16_t *)(result + 0xBA))) & (16)) == 0) ? 1 : 0;
    result = (((*(uint8_t *)(result + 0x8)) & (8)) == 0) ? 1 : 0;
    if ((((uint8_t)(result)) & ((uint8_t)(Arg1))) == 0) goto loc_00850EE8;
loc_00850FF1:
    result = CmpCleanUpKcbCacheWithLock(result, v_stack_p70, 1, Arg4);
    if ((*(uint64_t *)(result + 0x38)) == (*(uint64_t *)(gs_base + (0 + 0x188)))) goto loc_00850EF8;
    result = CmpDecommisssionKcb(result, v_stack_p70, 1, Arg4);
    goto loc_00850EF8;
loc_0085101E:
    if (*(uint64_t *)(result + 0x18) == 0) goto loc_00850E92;
    result = CmpUnlockKcb(result, v_stack_p70, 1, Arg4);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(*(uint64_t *)(*(uint64_t *)(result + 0x18) + 0x10) + 48, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(result + 0x18) + 0x10) + 48;
        Arg2 = result;
        Arg1 = *(uint64_t *)(*(uint64_t *)(result + 0x18) + 0x10) + 48;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    Arg3 = 0;
    Arg2 = 0;
    local_rbp = (v_stack_p38) + (48);
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x18) + 0x10) + 0x38) = *(uint64_t *)(gs_base + (0 + 0x188));
    result = KeAbPreAcquire(local_rbp, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rbp;
        Arg2 = result;
        Arg1 = local_rbp;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    *(uint64_t *)(v_stack_p38 + 0x38) = *(uint64_t *)(gs_base + (0 + 0x188));
    goto loc_00850E92;
loc_008510C9:
    if ((uint8_t)(Arg3) == 0) goto loc_00850409;
    result = CmLockHive(*(uint64_t *)(result + 0x20), Arg2, Arg3, Arg4);
    result = (uint32_t)((1) & (127));
    *(uint32_t *)(*(uint64_t *)(result + 0x20) + result * 4 + 0x1090) = 19;
    if ((*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0xB78))) == 2) goto loc_00851113;
loc_00851106:
    result = CmUnlockHive(*(uint64_t *)(result + 0x20), Arg2, 1, Arg4);
    goto loc_00850409;
loc_00851113:
    result = (uint32_t)((1) & (127));
    *(uint32_t *)(*(uint64_t *)(result + 0x20) + result * 4 + 0x1090) = 20;
    result = 0;
    if (condition_is_not_equal) goto loc_00851106;
    result = (uint32_t)((1) & (127));
    *(uint32_t *)(*(uint64_t *)(result + 0x20) + result * 4 + 0x1090) = 21;
    result = CmpReferenceHive(*(uint64_t *)(result + 0x20), Arg2, 1, Arg4);
    result = ExQueueWorkItem(*(uint64_t *)(*(uint64_t *)(result + 0x20) + 0x12D0), 1, 1, Arg4);
    goto loc_00851106;
loc_0085116B:
    result = ExfReleasePushLock(*(uint64_t *)(*(uint64_t *)(result + 0x18) + 0x10), 1, 1, Arg4);
    goto loc_00850F71;
loc_00851178:
    v_stack_p20 = v_stack_p38;
    result = KeBugCheckEx(8 + 15 + 58, 8 + 15, *(uint64_t *)(result + 0x20), 8);
loc_00851193:
    if (((*(uint32_t *)(v_stack_p38 + 0xB8)) & (0x40000ULL)) == 0) goto loc_008506D0;
    if ((*(uint8_t *)(8 + 0xF + 0x3A + 0xB80)) != 1) goto loc_008506D0;
    result = CmpDoQueueLateUnloadWorker(8 + 15 + 58, 8 + 15, *(uint64_t *)(result + 0x20), 8);
    goto loc_008506D0;
loc_008511BB:
    result = CmpCleanUpKcbCacheWithLock(v_stack_p38, v_stack_p70, *(uint64_t *)(result + 0x20), 8);
    *(uint64_t *)(*(uint64_t *)(v_stack_p38 + 0x20) + 0x1050) = *(uint64_t *)(gs_base + (0 + 0x188));
    Arg3 = (uint32_t)((1) & (127));
    *(uint32_t *)(*(uint64_t *)(v_stack_p38 + 0x20) + Arg3 * 4 + 0x1090) = 31;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p38 + 0x20) + 0xA0)))) & (32)) != 0) goto loc_00850EF8;
    result = CmpDereferenceHive(*(uint64_t *)(v_stack_p38 + 0x20), v_stack_p70, Arg3, 8);
    goto loc_00850EF8;
loc_00851220:
    if (((*(uint32_t *)(v_stack_p38 + 0xB8)) & (0x40000ULL)) == 0) goto loc_00850EF8;
    if ((*(uint8_t *)(*(uint64_t *)(v_stack_p38 + 0x20) + 0xB80)) != 1) goto loc_00850EF8;
    result = CmpDoQueueLateUnloadWorker(*(uint64_t *)(v_stack_p38 + 0x20), v_stack_p70, Arg3, 8);
    goto loc_00850EF8;
loc_00851248:
    goto loc_00850C48;
loc_00851252:
    result = RtlUpcaseUnicodeChar(*(uint64_t *)(v_stack_p38 + 0x20), (uint32_t)(0x60400ULL), Arg3, 8);
    goto loc_00850B48;
loc_00851264:
    goto loc_00850A77;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0` | `64` | `W` |
| `Arg7` | `+ 0x0` | `8` | `W` |
| `Arg8` | `+ 0x0` | `16` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0084FD20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
