# CmpFinishSystemHivesLoad

- RVA: `0x007DA210`–`0x007DAC74` (길이 `2,660` bytes)
- VA: `0x00000001407DA210`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D650C`
- 디코드: `645`개 명령, `2,660/2,660` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **103**; 고유 호출 대상: **43**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **28**

### Outgoing calls
- `0x007DA27C` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (function, `0x003FBE70`)
- `0x007DA290` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007DA2D6` → [RtlUnicodeStringCopyString](../../text/47/RtlUnicodeStringCopyString_function_00471270.md) (function, `0x00471270`)
- `0x007DA2F9` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (function, `0x003CD504`)
- `0x007DA320` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x007DA331` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (function, `0x003CD504`)
- `0x007DA358` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x007DA35E` → [CmpHiveRootSecurityDescriptor](../7E/CmpHiveRootSecurityDescriptor_function_007ED104.md) (function, `0x007ED104`)
- `0x007DA3A2` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x007DA3B3` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x007DA3C5` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x007DA3D2` → [CmpInitCmRM](../87/CmpInitCmRM_function_0087C700.md) (function, `0x0087C700`)
- `0x007DA3DD` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x007DA3FC` → [TmEnableCallbacks](../../text/4F/TmEnableCallbacks_function_004FE0E0.md) (function, `0x004FE0E0`)
- `0x007DA408` → [CmRmFinalizeRecovery](../AB/CmRmFinalizeRecovery_function_00ABEB68.md) (function, `0x00ABEB68`)
- `0x007DA436` → [KeWaitForMultipleObjects](../../text/20/KeWaitForMultipleObjects_function_0020D110.md) (function, `0x0020D110`)
- `0x007DA492` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x007DA4A8` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x007DA4AD` → [CmpLockRegistryExclusive](../84/CmpLockRegistryExclusive_function_0084F9B4.md) (function, `0x0084F9B4`)
- `0x007DA513` → [CmpLinkHiveToMaster](../87/CmpLinkHiveToMaster_function_00877D6C.md) (function, `0x00877D6C`)
- `0x007DA523` → [CmpLockHiveListExclusive](../A7/CmpLockHiveListExclusive_function_00A72240.md) (function, `0x00A72240`)
- `0x007DA562` → [CmpUnlockHiveList](../84/CmpUnlockHiveList_function_0084E424.md) (function, `0x0084E424`)
- `0x007DA56C` → [CmpRecheckHiveVolumePolicy](../../text/46/CmpRecheckHiveVolumePolicy_function_0046EE14.md) (function, `0x0046EE14`)
- `0x007DA59B` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DA5A8` → [CmpFlushHive](../9B/CmpFlushHive_function_009B3DC0.md) (function, `0x009B3DC0`)
- `0x007DA5AD` → [CmpLockRegistryExclusive](../84/CmpLockRegistryExclusive_function_0084F9B4.md) (function, `0x0084F9B4`)
- `0x007DA612` → [CmpAddToHiveFileList](../A8/CmpAddToHiveFileList_function_00A81914.md) (function, `0x00A81914`)
- `0x007DA630` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DA635` → [CmpMountPreloadedHives](CmpMountPreloadedHives_function_007DBE18.md) (function, `0x007DBE18`)
- `0x007DA63A` → [CmpLockRegistryExclusive](../84/CmpLockRegistryExclusive_function_0084F9B4.md) (function, `0x0084F9B4`)
- `0x007DA642` → [CmpInterlockedFunction](CmpInterlockedFunction_function_007DAD70.md) (function, `0x007DAD70`)
- `0x007DA660` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007DA679` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x007DA69A` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x007DA6A4` → [CmpNotifyMachineHiveLoaded](../../text/66/CmpNotifyMachineHiveLoaded_function_0066A43C.md) (function, `0x0066A43C`)
- `0x007DA6D6` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x007DA6DE` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x007DA6F6` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DA6FE` → [ExpRefreshSystemTime](../7C/ExpRefreshSystemTime_function_007C6264.md) (function, `0x007C6264`)
- `0x007DA708` → [CmpLoadSystemVersionData](../7E/CmpLoadSystemVersionData_function_007E70BC.md) (function, `0x007E70BC`)
- `0x007DA70D` → [CmpSetVersionData](../7E/CmpSetVersionData_function_007E7854.md) (function, `0x007E7854`)
- `0x007DA715` → [PsBootPhaseComplete](../77/PsBootPhaseComplete_function_0077EA18.md) (function, `0x0077EA18`)
- `0x007DA71F` → [CmpLoadSystemVersionData](../7E/CmpLoadSystemVersionData_function_007E70BC.md) (function, `0x007E70BC`)
- `0x007DA746` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DA766` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007DA77F` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x007DA7A3` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x007DA7B0` → [CmpNotifyMachineHiveLoaded](../../text/66/CmpNotifyMachineHiveLoaded_function_0066A43C.md) (function, `0x0066A43C`)
- `0x007DA7DC` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x007DA7E4` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x007DA7FC` → [ExpRefreshSystemTime](../7C/ExpRefreshSystemTime_function_007C6264.md) (function, `0x007C6264`)
- `0x007DA806` → [CmpLoadSystemVersionData](../7E/CmpLoadSystemVersionData_function_007E70BC.md) (function, `0x007E70BC`)
- `0x007DA80B` → [CmpSetVersionData](../7E/CmpSetVersionData_function_007E7854.md) (function, `0x007E7854`)
- `0x007DA813` → [PsBootPhaseComplete](../77/PsBootPhaseComplete_function_0077EA18.md) (function, `0x0077EA18`)
- `0x007DA81F` → [CmpSetVersionData](../7E/CmpSetVersionData_function_007E7854.md) (function, `0x007E7854`)
- `0x007DA82B` → [CmpCreatePerfKeys](CmpCreatePerfKeys_function_007D9F70.md) (function, `0x007D9F70`)
- `0x007DA85C` → [CmpLinkKeyToHive](CmpLinkKeyToHive_function_007DAF30.md) (function, `0x007DAF30`)
- `0x007DA861` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DA88A` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007DA8A3` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x007DA8C7` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x007DA8CF` → [CmpNotifyMachineHiveLoaded](../../text/66/CmpNotifyMachineHiveLoaded_function_0066A43C.md) (function, `0x0066A43C`)
- `0x007DA8FB` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x007DA903` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x007DA93B` → [CmpIsHiveLoadUnloadRundownActive](../../pagecmrc/BC/CmpIsHiveLoadUnloadRundownActive_function_00BC9FE4.md) (function, `0x00BC9FE4`)
- `0x007DA959` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DA993` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x007DA9A0` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007DA9B9` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x007DA9D0` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x007DA9D7` → [CmpNotifyMachineHiveLoaded](../../text/66/CmpNotifyMachineHiveLoaded_function_0066A43C.md) (function, `0x0066A43C`)
- `0x007DAA03` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x007DAA0B` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x007DAA41` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x007DAA47` → [CmpLockRegistryExclusive](../84/CmpLockRegistryExclusive_function_0084F9B4.md) (function, `0x0084F9B4`)
- `0x007DAA70` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DAA8B` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x007DAA98` → [CmpInitCmRM](../87/CmpInitCmRM_function_0087C700.md) (function, `0x0087C700`)
- `0x007DAAA3` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x007DAAC2` → [TmEnableCallbacks](../../text/4F/TmEnableCallbacks_function_004FE0E0.md) (function, `0x004FE0E0`)
- `0x007DAACE` → [CmRmFinalizeRecovery](../AB/CmRmFinalizeRecovery_function_00ABEB68.md) (function, `0x00ABEB68`)
- `0x007DAAD3` → [CmpMountPreloadedHives](CmpMountPreloadedHives_function_007DBE18.md) (function, `0x007DBE18`)
- `0x007DAAD8` → [CmpLockRegistryExclusive](../84/CmpLockRegistryExclusive_function_0084F9B4.md) (function, `0x0084F9B4`)
- `0x007DAADD` → [CmpInterlockedFunction](CmpInterlockedFunction_function_007DAD70.md) (function, `0x007DAD70`)
- `0x007DAAE2` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DAAF9` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x007DAB12` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)
- `0x007DAB29` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x007DAB30` → [CmpNotifyMachineHiveLoaded](../../text/66/CmpNotifyMachineHiveLoaded_function_0066A43C.md) (function, `0x0066A43C`)
- `0x007DAB5C` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (function, `0x002638D0`)
- `0x007DAB64` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (function, `0x002E1600`)
- `0x007DAB85` → [ExpRefreshSystemTime](../7C/ExpRefreshSystemTime_function_007C6264.md) (function, `0x007C6264`)
- `0x007DAB8A` → [PsBootPhaseComplete](../77/PsBootPhaseComplete_function_0077EA18.md) (function, `0x0077EA18`)
- `0x007DAB8F` → [CmpLoadSystemVersionData](../7E/CmpLoadSystemVersionData_function_007E70BC.md) (function, `0x007E70BC`)
- `0x007DAB94` → [CmpSetVersionData](../7E/CmpSetVersionData_function_007E7854.md) (function, `0x007E7854`)
- `0x007DABDB` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (function, `0x006AD470`)
- `0x007DABE8` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x007DAC14` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x007DAC23` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007DAC2C` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x007DAC35` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (function, `0x00475D80`)
- `0x007DAC3E` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)
- `0x007DAC4D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x007DA236` → RVA `0x00E0A740` (`.data`; read)
- `0x007DA295` → RVA `0x00FD8001` (`PAGEDATA`; write)
- `0x007DA29C` → RVA `0x00B08FE0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007DA2B1` → RVA `0x00EEFB48` (`.data`; write)
- `0x007DA368` → RVA `0x00E098F8` (`.data`; read)
- `0x007DA39B` → RVA `0x00E09B20` (`.data`; read)
- `0x007DA3B8` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x007DA3CA` → RVA `0x00EEFB68` (`.data`; read)
- `0x007DA3E2` → RVA `0x00EEFC78` (`.data`; read)
- `0x007DA3F1` → RVA `0x009B1950` (`CmKtmNotification`; read)
- `0x007DA40D` → RVA `0x00E098A0` (`.data`; read)
- `0x007DA528` → RVA `0x00FD9D20` (`PAGEDATA`; read)
- `0x007DA53B` → RVA `0x00FD9D18` (`PAGEDATA`; read)
- `0x007DA55B` → RVA `0x00FD9D20` (`PAGEDATA`; write)
- `0x007DA6E5` → RVA `0x00E09A48` (`.data`; read)
- `0x007DA6EE` → RVA `0x00E0EC74` (`.data`; read)
- `0x007DA7EB` → RVA `0x00E09B00` (`.data`; read)
- `0x007DA838` → RVA `0x00B08F60` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007DA83F` → RVA `0x00B08FA0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007DA84E` → RVA `0x00B08F00` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007DA855` → RVA `0x00B08F30` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007DA94B` → RVA `0x00EEFB44` (`.data`; write)
- `0x007DA961` → RVA `0x00E09928` (`.data`; read)
- `0x007DAA4C` → RVA `0x00FD8004` (`PAGEDATA`; read)
- `0x007DAA53` → RVA `0x00FD8017` (`PAGEDATA`; write)
- `0x007DAA5C` → RVA `0x00E0EC98` (`.data`; read)
- `0x007DAA6A` → RVA `0x00E0ECA0` (`.data`; write)
- `0x007DABA1` → RVA `0x00E0A010` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **68**
  - `0x007DA27C` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (`PAGE` → `.text`)
  - `0x007DA290` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007DA2D6` → [RtlUnicodeStringCopyString](../../text/47/RtlUnicodeStringCopyString_function_00471270.md) (`PAGE` → `.text`)
  - `0x007DA2F9` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (`PAGE` → `.text`)
  - `0x007DA320` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x007DA331` → [CmpAllocatePool](../../text/3C/CmpAllocatePool_function_003CD504.md) (`PAGE` → `.text`)
  - `0x007DA358` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x007DA3A2` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x007DA3B3` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x007DA3C5` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x007DA3DD` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x007DA3FC` → [TmEnableCallbacks](../../text/4F/TmEnableCallbacks_function_004FE0E0.md) (`PAGE` → `.text`)
  - `0x007DA436` → [KeWaitForMultipleObjects](../../text/20/KeWaitForMultipleObjects_function_0020D110.md) (`PAGE` → `.text`)
  - `0x007DA492` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (`PAGE` → `.text`)
  - `0x007DA4A8` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (`PAGE` → `.text`)
  - `0x007DA56C` → [CmpRecheckHiveVolumePolicy](../../text/46/CmpRecheckHiveVolumePolicy_function_0046EE14.md) (`PAGE` → `.text`)
  - `0x007DA59B` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DA630` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DA660` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007DA679` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x007DA69A` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x007DA6A4` → [CmpNotifyMachineHiveLoaded](../../text/66/CmpNotifyMachineHiveLoaded_function_0066A43C.md) (`PAGE` → `.text`)
  - `0x007DA6D6` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x007DA6DE` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x007DA6F6` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DA746` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DA766` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007DA77F` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x007DA7A3` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x007DA7B0` → [CmpNotifyMachineHiveLoaded](../../text/66/CmpNotifyMachineHiveLoaded_function_0066A43C.md) (`PAGE` → `.text`)
  - `0x007DA7DC` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x007DA7E4` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x007DA861` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DA88A` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007DA8A3` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x007DA8C7` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x007DA8CF` → [CmpNotifyMachineHiveLoaded](../../text/66/CmpNotifyMachineHiveLoaded_function_0066A43C.md) (`PAGE` → `.text`)
  - `0x007DA8FB` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x007DA903` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x007DA93B` → [CmpIsHiveLoadUnloadRundownActive](../../pagecmrc/BC/CmpIsHiveLoadUnloadRundownActive_function_00BC9FE4.md) (`PAGE` → `PAGECMRC`)
  - `0x007DA959` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DA993` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x007DA9A0` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007DA9B9` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x007DA9D0` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x007DA9D7` → [CmpNotifyMachineHiveLoaded](../../text/66/CmpNotifyMachineHiveLoaded_function_0066A43C.md) (`PAGE` → `.text`)
  - `0x007DAA03` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x007DAA0B` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x007DAA41` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x007DAA70` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DAA8B` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x007DAAA3` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x007DAAC2` → [TmEnableCallbacks](../../text/4F/TmEnableCallbacks_function_004FE0E0.md) (`PAGE` → `.text`)
  - `0x007DAAE2` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DAAF9` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x007DAB12` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
  - `0x007DAB29` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x007DAB30` → [CmpNotifyMachineHiveLoaded](../../text/66/CmpNotifyMachineHiveLoaded_function_0066A43C.md) (`PAGE` → `.text`)
  - `0x007DAB5C` → [ExfReleasePushLock](../../text/26/ExfReleasePushLock_function_002638D0.md) (`PAGE` → `.text`)
  - `0x007DAB64` → [KeAbPostRelease](../../text/2E/KeAbPostRelease_function_002E1600.md) (`PAGE` → `.text`)
  - `0x007DABDB` → [ZwCreateKey](../../text/6A/ZwCreateKey_function_006AD470.md) (`PAGE` → `.text`)
  - `0x007DABE8` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x007DAC14` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x007DAC23` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007DAC2C` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x007DAC35` → [CmSiFreeMemory](../../text/47/CmSiFreeMemory_function_00475D80.md) (`PAGE` → `.text`)
  - `0x007DAC3E` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
  - `0x007DAC4D` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007DA210  48 8B C4                        mov rax, rsp
007DA213  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
007DA217  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
007DA21B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
007DA21F  55                              push rbp
007DA220  41 54                           push r12
007DA222  41 55                           push r13
007DA224  41 56                           push r14
007DA226  41 57                           push r15
007DA228  48 8D A8 88 FD FF FF            lea rbp, [rax - 0x278]
007DA22F  48 81 EC 50 03 00 00            sub rsp, 0x350
007DA236  48 8B 05 03 05 63 00            mov rax, qword ptr [rip + 0x630503]
007DA23D  48 33 C4                        xor rax, rsp
007DA240  48 89 85 40 02 00 00            mov qword ptr [rbp + 0x240], rax
007DA247  0F 57 C0                        xorps xmm0, xmm0
007DA24A  33 C0                           xor eax, eax
007DA24C  4C 8B E9                        mov r13, rcx
007DA24F  48 89 45 B8                     mov qword ptr [rbp - 0x48], rax
007DA253  33 FF                           xor edi, edi
007DA255  89 45 C0                        mov dword ptr [rbp - 0x40], eax
007DA258  48 8D 4D C8                     lea rcx, [rbp - 0x38]
007DA25C  48 89 7D 80                     mov qword ptr [rbp - 0x80], rdi
007DA260  0F 11 45 98                     movups xmmword ptr [rbp - 0x68], xmm0
007DA264  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
007DA268  0F 11 45 A8                     movups xmmword ptr [rbp - 0x58], xmm0
007DA26C  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
007DA270  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
007DA274  0F 11 45 00                     movups xmmword ptr [rbp], xmm0
007DA278  0F 11 45 C8                     movups xmmword ptr [rbp - 0x38], xmm0
007DA27C  E8 EF 1B C2 FF                  call 0x1403fbe70
007DA281  33 D2                           xor edx, edx
007DA283  48 8D 4D 10                     lea rcx, [rbp + 0x10]
007DA287  41 B8 B0 01 00 00               mov r8d, 0x1b0
007DA28D  44 8A E7                        mov r12b, dil
007DA290  E8 AB C9 EE FF                  call 0x1406c6c40
007DA295  40 88 3D 65 DD 7F 00            mov byte ptr [rip + 0x7fdd65], dil
007DA29C  48 8D 15 3D ED 32 00            lea rdx, [rip + 0x32ed3d]
007DA2A3  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007DA2AC  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
007DA2B1  48 89 05 90 58 71 00            mov qword ptr [rip + 0x715890], rax
007DA2B8  0F 57 C0                        xorps xmm0, xmm0
007DA2BB  0F 11 44 24 68                  movups xmmword ptr [rsp + 0x68], xmm0
007DA2C0  B8 80 00 00 00                  mov eax, 0x80
007DA2C5  66 89 44 24 6A                  mov word ptr [rsp + 0x6a], ax
007DA2CA  48 8D 85 C0 01 00 00            lea rax, [rbp + 0x1c0]
007DA2D1  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
007DA2D6  E8 95 6F C9 FF                  call 0x140471270
007DA2DB  0F B7 44 24 68                  movzx eax, word ptr [rsp + 0x68]
007DA2E0  44 8D 77 40                     lea r14d, [rdi + 0x40]
007DA2E4  BE 43 4D 20 20                  mov esi, 0x20204d43
007DA2E9  66 89 44 24 62                  mov word ptr [rsp + 0x62], ax
007DA2EE  44 8B C6                        mov r8d, esi
007DA2F1  41 8B CE                        mov ecx, r14d
007DA2F4  BA 50 01 00 00                  mov edx, 0x150
007DA2F9  E8 06 32 BF FF                  call 0x1403cd504
007DA2FE  48 89 45 88                     mov qword ptr [rbp - 0x78], rax
007DA302  48 8B D8                        mov rbx, rax
007DA305  48 85 C0                        test rax, rax
007DA308  75 1C                           jne 0x1407da326
007DA30A  45 33 C9                        xor r9d, r9d
007DA30D  48 C7 44 24 20 9A 00 00 C0      mov qword ptr [rsp + 0x20], 0xffffffffc000009a
007DA316  8D 57 02                        lea edx, [rdi + 2]
007DA319  8D 4F 74                        lea ecx, [rdi + 0x74]
007DA31C  44 8D 47 04                     lea r8d, [rdi + 4]
007DA320  E8 3B 33 D2 FF                  call 0x1404fd660
007DA325  CC                              int3
007DA326  44 8B C6                        mov r8d, esi
007DA329  BA 38 00 00 00                  mov edx, 0x38
007DA32E  49 8B CE                        mov rcx, r14
007DA331  E8 CE 31 BF FF                  call 0x1403cd504
007DA336  48 89 45 90                     mov qword ptr [rbp - 0x70], rax
007DA33A  4C 8B F0                        mov r14, rax
007DA33D  48 85 C0                        test rax, rax
007DA340  75 1C                           jne 0x1407da35e
007DA342  45 33 C9                        xor r9d, r9d
007DA345  48 C7 44 24 20 9A 00 00 C0      mov qword ptr [rsp + 0x20], 0xffffffffc000009a
007DA34E  8D 50 02                        lea edx, [rax + 2]
007DA351  8D 48 74                        lea ecx, [rax + 0x74]
007DA354  44 8D 40 06                     lea r8d, [rax + 6]
007DA358  E8 03 33 D2 FF                  call 0x1404fd660
007DA35D  CC                              int3
007DA35E  E8 A1 2D 01 00                  call 0x1407ed104
007DA363  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
007DA368  48 8D 15 89 F5 62 00            lea rdx, [rip + 0x62f589]
007DA36F  49 8B CE                        mov rcx, r14
007DA372  41 B8 07 00 00 00               mov r8d, 7
007DA378  48 89 11                        mov qword ptr [rcx], rdx
007DA37B  48 81 C2 B8 00 00 00            add rdx, 0xb8
007DA382  48 8D 49 08                     lea rcx, [rcx + 8]
007DA386  49 83 E8 01                     sub r8, 1
007DA38A  75 EC                           jne 0x1407da378
007DA38C  4D 85 ED                        test r13, r13
007DA38F  75 7C                           jne 0x1407da40d
007DA391  45 33 C9                        xor r9d, r9d
007DA394  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
007DA399  33 D2                           xor edx, edx
007DA39B  48 8D 0D 7E F7 62 00            lea rcx, [rip + 0x62f77e]
007DA3A2  E8 09 43 A3 FF                  call 0x14020e6b0
007DA3A7  45 33 C0                        xor r8d, r8d
007DA3AA  48 8D 0D 6F F7 62 00            lea rcx, [rip + 0x62f76f]
007DA3B1  33 D2                           xor edx, edx
007DA3B3  E8 58 4F B6 FF                  call 0x14033f310
007DA3B8  48 8B 0D F1 C6 7E 00            mov rcx, qword ptr [rip + 0x7ec6f1]
007DA3BF  4C 8D 45 E0                     lea r8, [rbp - 0x20]
007DA3C3  33 D2                           xor edx, edx
007DA3C5  E8 56 C4 A3 FF                  call 0x140216820
007DA3CA  8A 15 98 57 71 00               mov dl, byte ptr [rip + 0x715798]
007DA3D0  33 C9                           xor ecx, ecx
007DA3D2  E8 29 23 0A 00                  call 0x14087c700
007DA3D7  33 D2                           xor edx, edx
007DA3D9  48 8D 4D E0                     lea rcx, [rbp - 0x20]
007DA3DD  E8 4E D9 A3 FF                  call 0x140217d30
007DA3E2  48 8B 0D 8F 58 71 00            mov rcx, qword ptr [rip + 0x71588f]
007DA3E9  48 85 C9                        test rcx, rcx
007DA3EC  74 1F                           je 0x1407da40d
007DA3EE  4C 8B C1                        mov r8, rcx
007DA3F1  48 8D 15 58 75 1D 00            lea rdx, [rip + 0x1d7558]
007DA3F8  48 8B 49 38                     mov rcx, qword ptr [rcx + 0x38]
007DA3FC  E8 DF 3C D2 FF                  call 0x1404fe0e0
007DA401  48 8B 0D 70 58 71 00            mov rcx, qword ptr [rip + 0x715870]
007DA408  E8 5B 47 2E 00                  call 0x140abeb68
007DA40D  48 8D 35 8C F4 62 00            lea rsi, [rip + 0x62f48c]
007DA414  45 33 C9                        xor r9d, r9d
007DA417  48 89 5C 24 38                  mov qword ptr [rsp + 0x38], rbx
007DA41C  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
007DA421  49 8B D6                        mov rdx, r14
007DA424  40 88 7C 24 28                  mov byte ptr [rsp + 0x28], dil
007DA429  40 88 7C 24 20                  mov byte ptr [rsp + 0x20], dil
007DA42E  45 8D 41 01                     lea r8d, [r9 + 1]
007DA432  41 8D 49 07                     lea ecx, [r9 + 7]
007DA436  E8 D5 2C A3 FF                  call 0x14020d110
007DA43B  40 88 7C 24 60                  mov byte ptr [rsp + 0x60], dil
007DA440  44 8B FF                        mov r15d, edi
007DA443  41 83 FF 07                     cmp r15d, 7
007DA447  0F 83 CF 04 00 00               jae 0x1407da91c
007DA44D  41 8B FF                        mov edi, r15d
007DA450  45 33 F6                        xor r14d, r14d
007DA453  48 69 DF B8 00 00 00            imul rbx, rdi, 0xb8
007DA45A  44 38 74 33 38                  cmp byte ptr [rbx + rsi + 0x38], r14b
007DA45F  75 0C                           jne 0x1407da46d
007DA461  44 38 74 33 39                  cmp byte ptr [rbx + rsi + 0x39], r14b
007DA466  75 0C                           jne 0x1407da474
007DA468  C6 44 24 60 01                  mov byte ptr [rsp + 0x60], 1
007DA46D  33 FF                           xor edi, edi
007DA46F  E9 A0 04 00 00                  jmp 0x1407da914
007DA474  0F B7 44 24 62                  movzx eax, word ptr [rsp + 0x62]
007DA479  48 8D 15 20 F4 62 00            lea rdx, [rip + 0x62f420]
007DA480  48 8B 54 13 08                  mov rdx, qword ptr [rbx + rdx + 8]
007DA485  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
007DA48A  41 8A F6                        mov sil, r14b
007DA48D  66 89 44 24 68                  mov word ptr [rsp + 0x68], ax
007DA492  E8 F9 54 C3 FF                  call 0x14040f990
007DA497  48 8D 05 02 F4 62 00            lea rax, [rip + 0x62f402]
007DA49E  48 8B 54 03 10                  mov rdx, qword ptr [rbx + rax + 0x10]
007DA4A3  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
007DA4A8  E8 E3 54 C3 FF                  call 0x14040f990
007DA4AD  E8 02 55 07 00                  call 0x14084f9b4
007DA4B2  48 8D 0D E7 F3 62 00            lea rcx, [rip + 0x62f3e7]
007DA4B9  4C 39 74 0B 18                  cmp qword ptr [rbx + rcx + 0x18], r14
007DA4BE  0F 85 3B 01 00 00               jne 0x1407da5ff
007DA4C4  4C 8B 44 0B 30                  mov r8, qword ptr [rbx + rcx + 0x30]
007DA4C9  4D 85 C0                        test r8, r8
007DA4CC  0F 84 2D 01 00 00               je 0x1407da5ff
007DA4D2  44 8A 4C 0B 3B                  mov r9b, byte ptr [rbx + rcx + 0x3b]
007DA4D7  48 8D 45 10                     lea rax, [rbp + 0x10]
007DA4DB  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
007DA4E0  33 D2                           xor edx, edx
007DA4E2  C6 44 24 50 01                  mov byte ptr [rsp + 0x50], 1
007DA4E7  33 C0                           xor eax, eax
007DA4E9  4C 89 74 24 48                  mov qword ptr [rsp + 0x48], r14
007DA4EE  4C 89 74 24 40                  mov qword ptr [rsp + 0x40], r14
007DA4F3  4C 8B 74 24 78                  mov r14, qword ptr [rsp + 0x78]
007DA4F8  4C 89 74 24 38                  mov qword ptr [rsp + 0x38], r14
007DA4FD  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007DA502  88 44 24 28                     mov byte ptr [rsp + 0x28], al
007DA506  8B 44 0B 28                     mov eax, dword ptr [rbx + rcx + 0x28]
007DA50A  48 8D 4C 24 68                  lea rcx, [rsp + 0x68]
007DA50F  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007DA513  E8 54 D8 09 00                  call 0x140877d6c
007DA518  48 63 C8                        movsxd rcx, eax
007DA51B  85 C0                           test eax, eax
007DA51D  0F 88 18 04 00 00               js 0x1407da93b
007DA523  E8 18 7D 29 00                  call 0x140a72240
007DA528  48 8B 0D F1 F7 7F 00            mov rcx, qword ptr [rip + 0x7ff7f1]
007DA52F  4C 8D 35 6A F3 62 00            lea r14, [rip + 0x62f36a]
007DA536  4A 8B 44 33 30                  mov rax, qword ptr [rbx + r14 + 0x30]
007DA53B  48 8D 15 D6 F7 7F 00            lea rdx, [rip + 0x7ff7d6]
007DA542  48 05 48 06 00 00               add rax, 0x648
007DA548  48 39 11                        cmp qword ptr [rcx], rdx
007DA54B  0F 85 E3 03 00 00               jne 0x1407da934
007DA551  48 89 10                        mov qword ptr [rax], rdx
007DA554  48 89 48 08                     mov qword ptr [rax + 8], rcx
007DA558  48 89 01                        mov qword ptr [rcx], rax
007DA55B  48 89 05 BE F7 7F 00            mov qword ptr [rip + 0x7ff7be], rax
007DA562  E8 BD 3E 07 00                  call 0x14084e424
007DA567  4A 8B 4C 33 30                  mov rcx, qword ptr [rbx + r14 + 0x30]
007DA56C  E8 A3 48 C9 FF                  call 0x14046ee14
007DA571  33 FF                           xor edi, edi
007DA573  42 38 7C 33 3B                  cmp byte ptr [rbx + r14 + 0x3b], dil
007DA578  74 50                           je 0x1407da5ca
007DA57A  4A 8B 44 33 30                  mov rax, qword ptr [rbx + r14 + 0x30]
007DA57F  83 88 A0 00 00 00 20            or dword ptr [rax + 0xa0], 0x20
007DA586  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
007DA58F  4A 8B 44 33 30                  mov rax, qword ptr [rbx + r14 + 0x30]
007DA594  48 89 88 48 10 00 00            mov qword ptr [rax + 0x1048], rcx
007DA59B  E8 E4 F4 3E 00                  call 0x140bc9a84
007DA5A0  4A 8B 4C 33 30                  mov rcx, qword ptr [rbx + r14 + 0x30]
007DA5A5  8D 57 04                        lea edx, [rdi + 4]
007DA5A8  E8 13 98 1D 00                  call 0x1409b3dc0
007DA5AD  E8 02 54 07 00                  call 0x14084f9b4
007DA5B2  4A 8B 44 33 30                  mov rax, qword ptr [rbx + r14 + 0x30]
007DA5B7  83 A0 A0 00 00 00 DF            and dword ptr [rax + 0xa0], 0xffffffdf
007DA5BE  4A 8B 44 33 30                  mov rax, qword ptr [rbx + r14 + 0x30]
007DA5C3  48 89 B8 48 10 00 00            mov qword ptr [rax + 0x1048], rdi
007DA5CA  48 8B 0D A7 56 71 00            mov rcx, qword ptr [rip + 0x7156a7]
007DA5D1  48 85 C9                        test rcx, rcx
007DA5D4  74 32                           je 0x1407da608
007DA5D6  4A 8B 54 33 30                  mov rdx, qword ptr [rbx + r14 + 0x30]
007DA5DB  8B 82 A0 00 00 00               mov eax, dword ptr [rdx + 0xa0]
007DA5E1  A8 02                           test al, 2
007DA5E3  75 23                           jne 0x1407da608
007DA5E5  48 39 BA 38 10 00 00            cmp qword ptr [rdx + 0x1038], rdi
007DA5EC  75 1A                           jne 0x1407da608
007DA5EE  FF 41 40                        inc dword ptr [rcx + 0x40]
007DA5F1  4A 8B 44 33 30                  mov rax, qword ptr [rbx + r14 + 0x30]
007DA5F6  48 89 88 38 10 00 00            mov qword ptr [rax + 0x1038], rcx
007DA5FD  EB 09                           jmp 0x1407da608
007DA5FF  4C 8D 35 9A F2 62 00            lea r14, [rip + 0x62f29a]
007DA606  33 FF                           xor edi, edi
007DA608  4A 8B 4C 33 30                  mov rcx, qword ptr [rbx + r14 + 0x30]
007DA60D  48 85 C9                        test rcx, rcx
007DA610  74 05                           je 0x1407da617
007DA612  E8 FD 72 2A 00                  call 0x140a81914
007DA617  42 C6 44 33 38 01               mov byte ptr [rbx + r14 + 0x38], 1
007DA61D  41 83 FF 03                     cmp r15d, 3
007DA621  0F 85 15 01 00 00               jne 0x1407da73c
007DA627  4D 85 ED                        test r13, r13
007DA62A  0F 85 31 02 00 00               jne 0x1407da861
007DA630  E8 4F F4 3E 00                  call 0x140bc9a84
007DA635  E8 DE 17 00 00                  call 0x1407dbe18
007DA63A  E8 75 53 07 00                  call 0x14084f9b4
007DA63F  41 B6 01                        mov r14b, 1
007DA642  E8 29 07 00 00                  call 0x1407dad70
007DA647  48 8D 3D 52 F2 62 00            lea rdi, [rip + 0x62f252]
007DA64E  45 33 C0                        xor r8d, r8d
007DA651  48 81 C7 88 00 00 00            add rdi, 0x88
007DA658  33 D2                           xor edx, edx
007DA65A  48 03 FB                        add rdi, rbx
007DA65D  48 8B CF                        mov rcx, rdi
007DA660  E8 CB 5B A3 FF                  call 0x140210230
007DA665  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
007DA66B  48 8B F0                        mov rsi, rax
007DA66E  73 0E                           jae 0x1407da67e
007DA670  4C 8B C7                        mov r8, rdi
007DA673  48 8B D0                        mov rdx, rax
007DA676  48 8B CF                        mov rcx, rdi
007DA679  E8 12 56 A3 FF                  call 0x14020fc90
007DA67E  48 85 F6                        test rsi, rsi
007DA681  74 04                           je 0x1407da687
007DA683  44 88 76 0A                     mov byte ptr [rsi + 0xa], r14b
007DA687  48 8D 0D 12 F2 62 00            lea rcx, [rip + 0x62f212]
007DA68E  45 33 C0                        xor r8d, r8d
007DA691  48 83 C1 70                     add rcx, 0x70
007DA695  33 D2                           xor edx, edx
007DA697  48 03 CB                        add rcx, rbx
007DA69A  E8 71 4C B6 FF                  call 0x14033f310
007DA69F  B9 03 00 00 00                  mov ecx, 3
007DA6A4  E8 93 FD E8 FF                  call 0x14066a43c
007DA6A9  0F 0D 0F                        prefetchw byte ptr [rdi]
007DA6AC  48 8B 07                        mov rax, qword ptr [rdi]
007DA6AF  41 B8 00 00 00 00               mov r8d, 0
007DA6B5  48 8B C8                        mov rcx, rax
007DA6B8  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
007DA6BC  48 83 F9 10                     cmp rcx, 0x10
007DA6C0  48 8D 50 F0                     lea rdx, [rax - 0x10]
007DA6C4  49 0F 46 D0                     cmovbe rdx, r8
007DA6C8  A8 02                           test al, 2
007DA6CA  75 07                           jne 0x1407da6d3
007DA6CC  F0 48 0F B1 17                  lock cmpxchg qword ptr [rdi], rdx
007DA6D1  74 08                           je 0x1407da6db
007DA6D3  48 8B CF                        mov rcx, rdi
007DA6D6  E8 F5 91 A8 FF                  call 0x1402638d0
007DA6DB  48 8B CF                        mov rcx, rdi
007DA6DE  E8 1D 6F B0 FF                  call 0x1402e1600
007DA6E3  33 FF                           xor edi, edi
007DA6E5  40 38 3D 5C F3 62 00            cmp byte ptr [rip + 0x62f35c], dil
007DA6EC  74 2C                           je 0x1407da71a
007DA6EE  39 3D 80 45 63 00               cmp dword ptr [rip + 0x634580], edi
007DA6F4  74 24                           je 0x1407da71a
007DA6F6  E8 89 F3 3E 00                  call 0x140bc9a84
007DA6FB  44 8A F7                        mov r14b, dil
007DA6FE  E8 61 BB FE FF                  call 0x1407c6264
007DA703  45 84 E4                        test r12b, r12b
007DA706  75 0D                           jne 0x1407da715
007DA708  E8 AF C9 00 00                  call 0x1407e70bc
007DA70D  E8 42 D1 00 00                  call 0x1407e7854
007DA712  41 B4 01                        mov r12b, 1
007DA715  E8 FE 42 FA FF                  call 0x14077ea18
007DA71A  45 84 E4                        test r12b, r12b
007DA71D  75 05                           jne 0x1407da724
007DA71F  E8 98 C9 00 00                  call 0x1407e70bc
007DA724  40 B6 01                        mov sil, 1
007DA727  45 84 F6                        test r14b, r14b
007DA72A  0F 84 DD 01 00 00               je 0x1407da90d
007DA730  4C 8D 35 69 F1 62 00            lea r14, [rip + 0x62f169]
007DA737  E9 25 01 00 00                  jmp 0x1407da861
007DA73C  41 83 FF 02                     cmp r15d, 2
007DA740  0F 85 EC 00 00 00               jne 0x1407da832
007DA746  E8 39 F3 3E 00                  call 0x140bc9a84
007DA74B  4D 85 ED                        test r13, r13
007DA74E  0F 85 D7 00 00 00               jne 0x1407da82b
007DA754  49 8D BE 88 00 00 00            lea rdi, [r14 + 0x88]
007DA75B  45 33 C0                        xor r8d, r8d
007DA75E  48 03 FB                        add rdi, rbx
007DA761  33 D2                           xor edx, edx
007DA763  48 8B CF                        mov rcx, rdi
007DA766  E8 C5 5A A3 FF                  call 0x140210230
007DA76B  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
007DA771  48 8B F0                        mov rsi, rax
007DA774  73 0E                           jae 0x1407da784
007DA776  4C 8B C7                        mov r8, rdi
007DA779  48 8B D0                        mov rdx, rax
007DA77C  48 8B CF                        mov rcx, rdi
007DA77F  E8 0C 55 A3 FF                  call 0x14020fc90
007DA784  45 33 F6                        xor r14d, r14d
007DA787  48 85 F6                        test rsi, rsi
007DA78A  74 04                           je 0x1407da790
007DA78C  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
007DA790  48 8D 0D 09 F1 62 00            lea rcx, [rip + 0x62f109]
007DA797  45 33 C0                        xor r8d, r8d
007DA79A  48 83 C1 70                     add rcx, 0x70
007DA79E  33 D2                           xor edx, edx
007DA7A0  48 03 CB                        add rcx, rbx
007DA7A3  E8 68 4B B6 FF                  call 0x14033f310
007DA7A8  B9 02 00 00 00                  mov ecx, 2
007DA7AD  40 B6 01                        mov sil, 1
007DA7B0  E8 87 FC E8 FF                  call 0x14066a43c
007DA7B5  0F 0D 0F                        prefetchw byte ptr [rdi]
007DA7B8  48 8B 07                        mov rax, qword ptr [rdi]
007DA7BB  48 8B C8                        mov rcx, rax
007DA7BE  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
007DA7C2  48 83 F9 10                     cmp rcx, 0x10
007DA7C6  48 8D 50 F0                     lea rdx, [rax - 0x10]
007DA7CA  49 0F 46 D6                     cmovbe rdx, r14
007DA7CE  A8 02                           test al, 2
007DA7D0  75 07                           jne 0x1407da7d9
007DA7D2  F0 48 0F B1 17                  lock cmpxchg qword ptr [rdi], rdx
007DA7D7  74 08                           je 0x1407da7e1
007DA7D9  48 8B CF                        mov rcx, rdi
007DA7DC  E8 EF 90 A8 FF                  call 0x1402638d0
007DA7E1  48 8B CF                        mov rcx, rdi
007DA7E4  E8 17 6E B0 FF                  call 0x1402e1600
007DA7E9  33 FF                           xor edi, edi
007DA7EB  40 38 3D 0E F3 62 00            cmp byte ptr [rip + 0x62f30e], dil
007DA7F2  74 26                           je 0x1407da81a
007DA7F4  39 3D 7A 44 63 00               cmp dword ptr [rip + 0x63447a], edi
007DA7FA  74 1E                           je 0x1407da81a
007DA7FC  E8 63 BA FE FF                  call 0x1407c6264
007DA801  45 84 E4                        test r12b, r12b
007DA804  75 0D                           jne 0x1407da813
007DA806  E8 B1 C8 00 00                  call 0x1407e70bc
007DA80B  E8 44 D0 00 00                  call 0x1407e7854
007DA810  44 8A E6                        mov r12b, sil
007DA813  E8 00 42 FA FF                  call 0x14077ea18
007DA818  EB 0A                           jmp 0x1407da824
007DA81A  45 84 E4                        test r12b, r12b
007DA81D  75 05                           jne 0x1407da824
007DA81F  E8 30 D0 00 00                  call 0x1407e7854
007DA824  4C 8D 35 75 F0 62 00            lea r14, [rip + 0x62f075]
007DA82B  E8 40 F7 FF FF                  call 0x1407d9f70
007DA830  EB 34                           jmp 0x1407da866
007DA832  41 83 FF 01                     cmp r15d, 1
007DA836  75 10                           jne 0x1407da848
007DA838  48 8D 15 21 E7 32 00            lea rdx, [rip + 0x32e721]
007DA83F  48 8D 0D 5A E7 32 00            lea rcx, [rip + 0x32e75a]
007DA846  EB 14                           jmp 0x1407da85c
007DA848  41 83 FF 04                     cmp r15d, 4
007DA84C  75 13                           jne 0x1407da861
007DA84E  48 8D 15 AB E6 32 00            lea rdx, [rip + 0x32e6ab]
007DA855  48 8D 0D D4 E6 32 00            lea rcx, [rip + 0x32e6d4]
007DA85C  E8 CF 06 00 00                  call 0x1407daf30
007DA861  E8 1E F2 3E 00                  call 0x140bc9a84
007DA866  4D 85 ED                        test r13, r13
007DA869  0F 85 9E 00 00 00               jne 0x1407da90d
007DA86F  40 84 F6                        test sil, sil
007DA872  0F 85 95 00 00 00               jne 0x1407da90d
007DA878  49 8D BE 88 00 00 00            lea rdi, [r14 + 0x88]
007DA87F  45 33 C0                        xor r8d, r8d
007DA882  48 03 FB                        add rdi, rbx
007DA885  33 D2                           xor edx, edx
007DA887  48 8B CF                        mov rcx, rdi
007DA88A  E8 A1 59 A3 FF                  call 0x140210230
007DA88F  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
007DA895  48 8B F0                        mov rsi, rax
007DA898  73 0E                           jae 0x1407da8a8
007DA89A  4C 8B C7                        mov r8, rdi
007DA89D  48 8B D0                        mov rdx, rax
007DA8A0  48 8B CF                        mov rcx, rdi
007DA8A3  E8 E8 53 A3 FF                  call 0x14020fc90
007DA8A8  45 33 F6                        xor r14d, r14d
007DA8AB  48 85 F6                        test rsi, rsi
007DA8AE  74 04                           je 0x1407da8b4
007DA8B0  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
007DA8B4  48 8D 35 E5 EF 62 00            lea rsi, [rip + 0x62efe5]
007DA8BB  45 33 C0                        xor r8d, r8d
007DA8BE  48 8D 4E 70                     lea rcx, [rsi + 0x70]
007DA8C2  33 D2                           xor edx, edx
007DA8C4  48 03 CB                        add rcx, rbx
007DA8C7  E8 44 4A B6 FF                  call 0x14033f310
007DA8CC  41 8B CF                        mov ecx, r15d
007DA8CF  E8 68 FB E8 FF                  call 0x14066a43c
007DA8D4  0F 0D 0F                        prefetchw byte ptr [rdi]
007DA8D7  48 8B 07                        mov rax, qword ptr [rdi]
007DA8DA  48 8B C8                        mov rcx, rax
007DA8DD  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
007DA8E1  48 83 F9 10                     cmp rcx, 0x10
007DA8E5  48 8D 50 F0                     lea rdx, [rax - 0x10]
007DA8E9  49 0F 46 D6                     cmovbe rdx, r14
007DA8ED  A8 02                           test al, 2
007DA8EF  75 07                           jne 0x1407da8f8
007DA8F1  F0 48 0F B1 17                  lock cmpxchg qword ptr [rdi], rdx
007DA8F6  74 08                           je 0x1407da900
007DA8F8  48 8B CF                        mov rcx, rdi
007DA8FB  E8 D0 8F A8 FF                  call 0x1402638d0
007DA900  48 8B CF                        mov rcx, rdi
007DA903  E8 F8 6C B0 FF                  call 0x1402e1600
007DA908  E9 60 FB FF FF                  jmp 0x1407da46d
007DA90D  48 8D 35 8C EF 62 00            lea rsi, [rip + 0x62ef8c]
007DA914  41 FF C7                        inc r15d
007DA917  E9 27 FB FF FF                  jmp 0x1407da443
007DA91C  40 38 7C 24 60                  cmp byte ptr [rsp + 0x60], dil
007DA921  0F 84 20 01 00 00               je 0x1407daa47
007DA927  4C 8B 75 90                     mov r14, qword ptr [rbp - 0x70]
007DA92B  48 8B 5D 88                     mov rbx, qword ptr [rbp - 0x78]
007DA92F  E9 E0 FA FF FF                  jmp 0x1407da414
007DA934  B9 03 00 00 00                  mov ecx, 3
007DA939  CD 29                           int 0x29
007DA93B  E8 A4 F6 3E 00                  call 0x140bc9fe4
007DA940  45 33 FF                        xor r15d, r15d
007DA943  84 C0                           test al, al
007DA945  0F 84 DE 00 00 00               je 0x1407daa29
007DA94B  44 88 3D F2 51 71 00            mov byte ptr [rip + 0x7151f2], r15b
007DA952  4C 89 3D EF 51 71 00            mov qword ptr [rip + 0x7151ef], r15
007DA959  E8 26 F1 3E 00                  call 0x140bc9a84
007DA95E  41 8B FF                        mov edi, r15d
007DA961  48 8D 1D C0 EF 62 00            lea rbx, [rip + 0x62efc0]
007DA968  44 39 7B BC                     cmp dword ptr [rbx - 0x44], r15d
007DA96C  0F 84 9E 00 00 00               je 0x1407daa10
007DA972  44 38 7B B0                     cmp byte ptr [rbx - 0x50], r15b
007DA976  0F 85 94 00 00 00               jne 0x1407daa10
007DA97C  44 38 7B B1                     cmp byte ptr [rbx - 0x4f], r15b
007DA980  75 16                           jne 0x1407da998
007DA982  48 8D 4B D0                     lea rcx, [rbx - 0x30]
007DA986  4C 89 7C 24 20                  mov qword ptr [rsp + 0x20], r15
007DA98B  45 33 C9                        xor r9d, r9d
007DA98E  45 33 C0                        xor r8d, r8d
007DA991  33 D2                           xor edx, edx
007DA993  E8 18 3D A3 FF                  call 0x14020e6b0
007DA998  45 33 C0                        xor r8d, r8d
007DA99B  33 D2                           xor edx, edx
007DA99D  48 8B CB                        mov rcx, rbx
007DA9A0  E8 8B 58 A3 FF                  call 0x140210230
007DA9A5  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
007DA9AB  48 8B F0                        mov rsi, rax
007DA9AE  73 0E                           jae 0x1407da9be
007DA9B0  4C 8B C3                        mov r8, rbx
007DA9B3  48 8B D0                        mov rdx, rax
007DA9B6  48 8B CB                        mov rcx, rbx
007DA9B9  E8 D2 52 A3 FF                  call 0x14020fc90
007DA9BE  48 85 F6                        test rsi, rsi
007DA9C1  74 04                           je 0x1407da9c7
007DA9C3  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
007DA9C7  48 8D 4B E8                     lea rcx, [rbx - 0x18]
007DA9CB  45 33 C0                        xor r8d, r8d
007DA9CE  33 D2                           xor edx, edx
007DA9D0  E8 3B 49 B6 FF                  call 0x14033f310
007DA9D5  8B CF                           mov ecx, edi
007DA9D7  E8 60 FA E8 FF                  call 0x14066a43c
007DA9DC  0F 0D 0B                        prefetchw byte ptr [rbx]
007DA9DF  48 8B 03                        mov rax, qword ptr [rbx]
007DA9E2  48 8B C8                        mov rcx, rax
007DA9E5  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
007DA9E9  48 83 F9 10                     cmp rcx, 0x10
007DA9ED  48 8D 50 F0                     lea rdx, [rax - 0x10]
007DA9F1  49 0F 46 D7                     cmovbe rdx, r15
007DA9F5  A8 02                           test al, 2
007DA9F7  75 07                           jne 0x1407daa00
007DA9F9  F0 48 0F B1 13                  lock cmpxchg qword ptr [rbx], rdx
007DA9FE  74 08                           je 0x1407daa08
007DAA00  48 8B CB                        mov rcx, rbx
007DAA03  E8 C8 8E A8 FF                  call 0x1402638d0
007DAA08  48 8B CB                        mov rcx, rbx
007DAA0B  E8 F0 6B B0 FF                  call 0x1402e1600
007DAA10  FF C7                           inc edi
007DAA12  48 81 C3 B8 00 00 00            add rbx, 0xb8
007DAA19  83 FF 07                        cmp edi, 7
007DAA1C  0F 82 46 FF FF FF               jb 0x1407da968
007DAA22  33 FF                           xor edi, edi
007DAA24  E9 C9 01 00 00                  jmp 0x1407dabf2
007DAA29  BA 01 00 00 00                  mov edx, 1
007DAA2E  48 8D 44 24 68                  lea rax, [rsp + 0x68]
007DAA33  4C 8B C1                        mov r8, rcx
007DAA36  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007DAA3B  4C 8B CF                        mov r9, rdi
007DAA3E  8D 4A 72                        lea ecx, [rdx + 0x72]
007DAA41  E8 1A 2C D2 FF                  call 0x1404fd660
007DAA46  CC                              int3
007DAA47  E8 68 4F 07 00                  call 0x14084f9b4
007DAA4C  40 38 3D B1 D5 7F 00            cmp byte ptr [rip + 0x7fd5b1], dil
007DAA53  40 88 3D BD D5 7F 00            mov byte ptr [rip + 0x7fd5bd], dil
007DAA5A  75 0B                           jne 0x1407daa67
007DAA5C  83 3D 35 42 63 00 01            cmp dword ptr [rip + 0x634235], 1
007DAA63  B0 01                           mov al, 1
007DAA65  74 03                           je 0x1407daa6a
007DAA67  40 8A C7                        mov al, dil
007DAA6A  88 05 30 42 63 00               mov byte ptr [rip + 0x634230], al
007DAA70  E8 0F F0 3E 00                  call 0x140bc9a84
007DAA75  4D 85 ED                        test r13, r13
007DAA78  0F 84 1B 01 00 00               je 0x1407dab99
007DAA7E  48 8B 0D 2B C0 7E 00            mov rcx, qword ptr [rip + 0x7ec02b]
007DAA85  4C 8D 45 E0                     lea r8, [rbp - 0x20]
007DAA89  33 D2                           xor edx, edx
007DAA8B  E8 90 BD A3 FF                  call 0x140216820
007DAA90  8A 15 D2 50 71 00               mov dl, byte ptr [rip + 0x7150d2]
007DAA96  33 C9                           xor ecx, ecx
007DAA98  E8 63 1C 0A 00                  call 0x14087c700
007DAA9D  33 D2                           xor edx, edx
007DAA9F  48 8D 4D E0                     lea rcx, [rbp - 0x20]
007DAAA3  E8 88 D2 A3 FF                  call 0x140217d30
007DAAA8  48 8B 0D C9 51 71 00            mov rcx, qword ptr [rip + 0x7151c9]
007DAAAF  48 85 C9                        test rcx, rcx
007DAAB2  74 1F                           je 0x1407daad3
007DAAB4  4C 8B C1                        mov r8, rcx
007DAAB7  48 8D 15 92 6E 1D 00            lea rdx, [rip + 0x1d6e92]
007DAABE  48 8B 49 38                     mov rcx, qword ptr [rcx + 0x38]
007DAAC2  E8 19 36 D2 FF                  call 0x1404fe0e0
007DAAC7  48 8B 0D AA 51 71 00            mov rcx, qword ptr [rip + 0x7151aa]
007DAACE  E8 95 40 2E 00                  call 0x140abeb68
007DAAD3  E8 40 13 00 00                  call 0x1407dbe18
007DAAD8  E8 D7 4E 07 00                  call 0x14084f9b4
007DAADD  E8 8E 02 00 00                  call 0x1407dad70
007DAAE2  E8 9D EF 3E 00                  call 0x140bc9a84
007DAAE7  45 33 F6                        xor r14d, r14d
007DAAEA  48 8D 1D 37 EE 62 00            lea rbx, [rip + 0x62ee37]
007DAAF1  45 33 C0                        xor r8d, r8d
007DAAF4  33 D2                           xor edx, edx
007DAAF6  48 8B CB                        mov rcx, rbx
007DAAF9  E8 32 57 A3 FF                  call 0x140210230
007DAAFE  F0 48 0F BA 2B 00               lock bts qword ptr [rbx], 0
007DAB04  48 8B F0                        mov rsi, rax
007DAB07  73 0E                           jae 0x1407dab17
007DAB09  4C 8B C3                        mov r8, rbx
007DAB0C  48 8B D0                        mov rdx, rax
007DAB0F  48 8B CB                        mov rcx, rbx
007DAB12  E8 79 51 A3 FF                  call 0x14020fc90
007DAB17  48 85 F6                        test rsi, rsi
007DAB1A  74 04                           je 0x1407dab20
007DAB1C  C6 46 0A 01                     mov byte ptr [rsi + 0xa], 1
007DAB20  48 8D 4B E8                     lea rcx, [rbx - 0x18]
007DAB24  45 33 C0                        xor r8d, r8d
007DAB27  33 D2                           xor edx, edx
007DAB29  E8 E2 47 B6 FF                  call 0x14033f310
007DAB2E  8B CF                           mov ecx, edi
007DAB30  E8 07 F9 E8 FF                  call 0x14066a43c
007DAB35  0F 0D 0B                        prefetchw byte ptr [rbx]
007DAB38  48 8B 03                        mov rax, qword ptr [rbx]
007DAB3B  48 8B C8                        mov rcx, rax
007DAB3E  48 83 E1 F0                     and rcx, 0xfffffffffffffff0
007DAB42  48 83 F9 10                     cmp rcx, 0x10
007DAB46  48 8D 50 F0                     lea rdx, [rax - 0x10]
007DAB4A  49 0F 46 D6                     cmovbe rdx, r14
007DAB4E  A8 02                           test al, 2
007DAB50  75 07                           jne 0x1407dab59
007DAB52  F0 48 0F B1 13                  lock cmpxchg qword ptr [rbx], rdx
007DAB57  74 08                           je 0x1407dab61
007DAB59  48 8B CB                        mov rcx, rbx
007DAB5C  E8 6F 8D A8 FF                  call 0x1402638d0
007DAB61  48 8B CB                        mov rcx, rbx
007DAB64  E8 97 6A B0 FF                  call 0x1402e1600
007DAB69  FF C7                           inc edi
007DAB6B  48 81 C3 B8 00 00 00            add rbx, 0xb8
007DAB72  83 FF 07                        cmp edi, 7
007DAB75  0F 82 76 FF FF FF               jb 0x1407daaf1
007DAB7B  33 FF                           xor edi, edi
007DAB7D  39 3D F1 40 63 00               cmp dword ptr [rip + 0x6340f1], edi
007DAB83  74 0A                           je 0x1407dab8f
007DAB85  E8 DA B6 FE FF                  call 0x1407c6264
007DAB8A  E8 89 3E FA FF                  call 0x14077ea18
007DAB8F  E8 28 C5 00 00                  call 0x1407e70bc
007DAB94  E8 BB CC 00 00                  call 0x1407e7854
007DAB99  45 33 C9                        xor r9d, r9d
007DAB9C  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
007DABA1  48 8D 05 68 F4 62 00            lea rax, [rip + 0x62f468]
007DABA8  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
007DABAC  0F 57 C0                        xorps xmm0, xmm0
007DABAF  C7 45 98 30 00 00 00            mov dword ptr [rbp - 0x68], 0x30
007DABB6  4C 8D 45 98                     lea r8, [rbp - 0x68]
007DABBA  48 89 7D A0                     mov qword ptr [rbp - 0x60], rdi
007DABBE  41 8D 51 02                     lea edx, [r9 + 2]
007DABC2  C7 45 B0 40 02 00 00            mov dword ptr [rbp - 0x50], 0x240
007DABC9  48 8D 4D 80                     lea rcx, [rbp - 0x80]
007DABCD  48 89 45 A8                     mov qword ptr [rbp - 0x58], rax
007DABD1  F3 0F 7F 45 B8                  movdqu xmmword ptr [rbp - 0x48], xmm0
007DABD6  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
007DABDB  E8 90 28 ED FF                  call 0x1406ad470
007DABE0  85 C0                           test eax, eax
007DABE2  78 09                           js 0x1407dabed
007DABE4  48 8B 4D 80                     mov rcx, qword ptr [rbp - 0x80]
007DABE8  E8 C3 26 ED FF                  call 0x1406ad2b0
007DABED  4C 8B 74 24 78                  mov r14, qword ptr [rsp + 0x78]
007DABF2  40 88 3D 1E D4 7F 00            mov byte ptr [rip + 0x7fd41e], dil
007DABF9  40 88 3D 44 4F 71 00            mov byte ptr [rip + 0x714f44], dil
007DAC00  48 89 3D 41 4F 71 00            mov qword ptr [rip + 0x714f41], rdi
007DAC07  4D 85 ED                        test r13, r13
007DAC0A  74 0D                           je 0x1407dac19
007DAC0C  45 33 C0                        xor r8d, r8d
007DAC0F  33 D2                           xor edx, edx
007DAC11  49 8B CD                        mov rcx, r13
007DAC14  E8 F7 46 B6 FF                  call 0x14033f310
007DAC19  4D 85 F6                        test r14, r14
007DAC1C  74 0A                           je 0x1407dac28
007DAC1E  33 D2                           xor edx, edx
007DAC20  49 8B CE                        mov rcx, r14
007DAC23  E8 48 7C 3A 00                  call 0x140b82870
007DAC28  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
007DAC2C  E8 4F B1 C9 FF                  call 0x140475d80
007DAC31  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
007DAC35  E8 46 B1 C9 FF                  call 0x140475d80
007DAC3A  48 8D 4D C8                     lea rcx, [rbp - 0x38]
007DAC3E  E8 0D 51 C4 FF                  call 0x14041fd50
007DAC43  48 8B 8D 40 02 00 00            mov rcx, qword ptr [rbp + 0x240]
007DAC4A  48 33 CC                        xor rcx, rsp
007DAC4D  E8 EE 19 ED FF                  call 0x1406ac640
007DAC52  4C 8D 9C 24 50 03 00 00         lea r11, [rsp + 0x350]
007DAC5A  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
007DAC5E  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
007DAC62  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
007DAC66  49 8B E3                        mov rsp, r11
007DAC69  41 5F                           pop r15
007DAC6B  41 5E                           pop r14
007DAC6D  41 5D                           pop r13
007DAC6F  41 5C                           pop r12
007DAC71  5D                              pop rbp
007DAC72  C3                              ret
007DAC73  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpFinishSystemHivesLoad(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m300;
    unsigned __int64 v_stack_m308;
    unsigned __int16 v_stack_m30E;
    unsigned __int64 v_stack_m310;
    unsigned __int16 v_stack_m316;
    unsigned __int8 v_stack_m318;
    unsigned __int64 v_stack_m320;
    unsigned __int8 v_stack_m328;
    unsigned __int64 v_stack_m330;
    unsigned __int64 v_stack_m338;
    unsigned __int64 v_stack_m340;
    unsigned __int64 v_stack_m348;
    unsigned __int8 v_stack_m350;
    unsigned __int64 v_stack_m358;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (848);
    result = (*(unsigned __int64 *)(v_rip + 6489347)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 632 + 576) = result;
    result = 0;
    *(unsigned __int64 *)(v_rsp - 632 - 72) = 0;
    v_rdi = 0;
    *(unsigned int *)(v_rsp - 632 - 64) = 0;
    *(unsigned __int64 *)(v_rsp - 632 - 128) = 0;
    *(unsigned __int64 *)(v_rsp - 632 - 104) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 632 - 40) = 0;
    *(unsigned __int64 *)(v_rsp - 632 - 88) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 632 - 32) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 632 - 16) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 632) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 632 - 56) = v_xmm0;
    result = CmpInitializeThreadInfo(v_rsp - 632 - 56, a2, a3, a4);
    a2 = 0;
    result = memset(v_rsp - 632 + 16, a2, 432, a4);
    *(unsigned __int8 *)(v_rip + 8379749) = 0;
    *(unsigned __int64 *)(v_rip + 7428240) = *(unsigned __int64 *)(gs_base + (0 + 392));
    v_stack_m310 = v_xmm0;
    v_stack_m30E = 128;
    v_stack_m308 = v_rsp - 632 + 448;
    result = RtlUnicodeStringCopyString(v_stack_m310, v_rip + 3337533, 432, a4);
    v_stack_m316 = (unsigned __int16)(v_stack_m310);
    result = CmpAllocatePool((unsigned int)((unsigned int)(v_rdi + 64)), 336, (unsigned int)((unsigned int)((unsigned int)(0x20204D43ULL))), a4);
    *(unsigned __int64 *)(v_rsp - 632 - 120) = result;
    if (result == 0) {
        a4 = 0;
        v_stack_m358 = 0xFFFFFFFFC000009AULL;
        a2 = v_rdi + 2;
        a1 = v_rdi + 116;
        a3 = v_rdi + 4;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = CmpAllocatePool(v_rdi + 64, 56, (unsigned int)((unsigned int)((unsigned int)(0x20204D43ULL))), a4);
    *(unsigned __int64 *)(v_rsp - 632 - 112) = result;
    if (result == 0) {
        a4 = 0;
        v_stack_m358 = 0xFFFFFFFFC000009AULL;
        a2 = result + 2;
        a1 = result + 116;
        a3 = result + 6;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = CmpHiveRootSecurityDescriptor(a1, a2, a3, a4);
    v_stack_m300 = result;
loc_007DA378:
    *(unsigned __int64 *)(result) = v_rip + 6485385;
    a2 = (v_rip + 6485385) + (184);
    a3 = (7) - (1);
    if (condition_is_not_equal) goto loc_007DA378;
    if (a1 != 0) goto loc_007DA40D;
    a4 = 0;
    v_stack_m358 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_rip + 6485886, a2, a3, a4);
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_rip + 6485871, a2, a3, a4);
    a2 = 0;
    result = KiStackAttachProcess(*(unsigned __int64 *)(v_rip + 8308465), a2, v_rsp - 632 - 32, a4);
    a1 = 0;
    result = CmpInitCmRM(a1, *(unsigned __int8 *)(v_rip + 7427992), v_rsp - 632 - 32, a4);
    a2 = 0;
    result = KiUnstackDetachProcess(v_rsp - 632 - 32, a2, v_rsp - 632 - 32, a4);
    if (*(unsigned __int64 *)(v_rip + 7428239) != 0) {
        a3 = *(unsigned __int64 *)(v_rip + 7428239);
        a2 = v_rip + 1930584;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7428239) + 56);
        result = TmEnableCallbacks(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(v_rip + 7428208);
        result = CmRmFinalizeRecovery(a1, a2, a3, a4);
    }
loc_007DA414:
    a4 = 0;
    v_stack_m340 = result;
    v_stack_m348 = 0;
    v_stack_m350 = 0;
    v_stack_m358 = 0;
    result = KeWaitForMultipleObjects(a4 + 7, result, a4 + 1, a4);
    v_stack_m318 = 0;
loc_007DA443:
    if (0 >= 7) goto loc_007DA91C;
    v_r14 = 0;
    v_rbx = (result) * (0);
    if ((*(unsigned __int8 *)(v_rbx + v_rip + 6485132 * 1 + 56)) != 0) goto loc_007DA46D;
    if ((*(unsigned __int8 *)(v_rbx + v_rip + 6485132 * 1 + 57)) != 0) goto loc_007DA474;
    v_stack_m318 = 1;
loc_007DA46D:
    v_rdi = 0;
    goto loc_007DA914;
loc_007DA474:
    v_stack_m310 = (unsigned __int16)(v_stack_m316);
    result = RtlAppendUnicodeToString(v_stack_m310, *(unsigned __int64 *)(v_rbx + v_rip + 6485024 * 1 + 8), a4 + 1, a4);
    result = RtlAppendUnicodeToString(v_stack_m310, *(unsigned __int64 *)(v_rbx + v_rip + 6484994 * 1 + 16), a4 + 1, a4);
    result = CmpLockRegistryExclusive(v_stack_m310, *(unsigned __int64 *)(v_rbx + v_rip + 6484994 * 1 + 16), a4 + 1, a4);
    if ((*(unsigned __int64 *)(v_rbx + v_rip + 6484967 * 1 + 24)) != 0) goto loc_007DA5FF;
    if (*(unsigned __int64 *)(v_rbx + v_rip + 6484967 * 1 + 48) == 0) goto loc_007DA5FF;
    v_stack_m320 = v_rsp - 632 + 16;
    a2 = 0;
    v_stack_m328 = 1;
    result = 0;
    v_stack_m330 = 0;
    v_stack_m338 = 0;
    v_stack_m340 = v_stack_m300;
    v_stack_m348 = 0;
    v_stack_m350 = 0;
    v_stack_m358 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rbx + v_rip + 6484967 * 1 + 40)));
    result = CmpLinkHiveToMaster(v_stack_m310, a2, *(unsigned __int64 *)(v_rbx + v_rip + 6484967 * 1 + 48), *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    if (sign_flag) goto loc_007DA93B;
    result = CmpLockHiveListExclusive((int)((unsigned int)(result)), a2, *(unsigned __int64 *)(v_rbx + v_rip + 6484967 * 1 + 48), *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    result = (*(unsigned __int64 *)(v_rbx + v_rip + 6484842 * 1 + 48)) + (0x648ULL);
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8386545))) != (v_rip + 8386518)) goto loc_007DA934;
    *(unsigned __int64 *)(result) = v_rip + 8386518;
    *(unsigned __int64 *)(result + 8) = *(unsigned __int64 *)(v_rip + 8386545);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 8386545)) = result;
    *(unsigned __int64 *)(v_rip + 8386494) = result;
    result = CmpUnlockHiveList(*(unsigned __int64 *)(v_rip + 8386545), v_rip + 8386518, *(unsigned __int64 *)(v_rbx + v_rip + 6484967 * 1 + 48), *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    result = CmpRecheckHiveVolumePolicy(*(unsigned __int64 *)(v_rbx + v_rip + 6484842 * 1 + 48), v_rip + 8386518, *(unsigned __int64 *)(v_rbx + v_rip + 6484967 * 1 + 48), *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rbx + v_rip + 6484842 * 1 + 59)) != 0) {
        result = *(unsigned __int64 *)(v_rbx + v_rip + 6484842 * 1 + 48);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = *(unsigned __int64 *)(v_rbx + v_rip + 6484842 * 1 + 48);
        *(unsigned __int64 *)(result + 4168) = a1;
        result = CmpUnlockRegistry(a1, v_rip + 8386518, *(unsigned __int64 *)(v_rbx + v_rip + 6484967 * 1 + 48), *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
        a1 = *(unsigned __int64 *)(v_rbx + v_rip + 6484842 * 1 + 48);
        a2 = v_rdi + 4;
        result = CmpFlushHive(a1, a2, *(unsigned __int64 *)(v_rbx + v_rip + 6484967 * 1 + 48), *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
        result = CmpLockRegistryExclusive(a1, a2, *(unsigned __int64 *)(v_rbx + v_rip + 6484967 * 1 + 48), *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
        result = *(unsigned __int64 *)(v_rbx + v_rip + 6484842 * 1 + 48);
        result = *(unsigned __int64 *)(v_rbx + v_rip + 6484842 * 1 + 48);
        *(unsigned __int64 *)(result + 4168) = 0;
    }
    if (*(unsigned __int64 *)(v_rip + 7427751) == 0) goto loc_007DA608;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rbx + v_rip + 6484842 * 1 + 48) + 160)))) & (2)) != 0) goto loc_007DA608;
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + v_rip + 6484842 * 1 + 48) + 4152)) != 0) goto loc_007DA608;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + v_rip + 6484842 * 1 + 48) + 4152) = *(unsigned __int64 *)(v_rip + 7427751);
    goto loc_007DA608;
loc_007DA5FF:
    v_rdi = 0;
loc_007DA608:
    result = *(unsigned __int64 *)(v_rbx + v_rip + 6484842 * 1 + 48);
    if (*(unsigned __int64 *)(v_rbx + v_rip + 6484634 * 1 + 48) != 0) {
        result = CmpAddToHiveFileList(*(unsigned __int64 *)(v_rbx + v_rip + 6484634 * 1 + 48), *(unsigned __int64 *)(v_rbx + v_rip + 6484842 * 1 + 48), *(unsigned __int64 *)(v_rbx + v_rip + 6484967 * 1 + 48), *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    }
    *(unsigned __int8 *)(v_rbx + v_rip + 6484634 * 1 + 56) = 1;
    if (0 != 3) goto loc_007DA73C;
    if (a1 != 0) goto loc_007DA861;
    result = CmpUnlockRegistry(*(unsigned __int64 *)(v_rbx + v_rip + 6484634 * 1 + 48), *(unsigned __int64 *)(v_rbx + v_rip + 6484842 * 1 + 48), *(unsigned __int64 *)(v_rbx + v_rip + 6484967 * 1 + 48), *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    result = CmpMountPreloadedHives(*(unsigned __int64 *)(v_rbx + v_rip + 6484634 * 1 + 48), *(unsigned __int64 *)(v_rbx + v_rip + 6484842 * 1 + 48), *(unsigned __int64 *)(v_rbx + v_rip + 6484967 * 1 + 48), *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    result = CmpLockRegistryExclusive(*(unsigned __int64 *)(v_rbx + v_rip + 6484634 * 1 + 48), *(unsigned __int64 *)(v_rbx + v_rip + 6484842 * 1 + 48), *(unsigned __int64 *)(v_rbx + v_rip + 6484967 * 1 + 48), *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    result = CmpInterlockedFunction(*(unsigned __int64 *)(v_rbx + v_rip + 6484634 * 1 + 48), *(unsigned __int64 *)(v_rbx + v_rip + 6484842 * 1 + 48), *(unsigned __int64 *)(v_rbx + v_rip + 6484967 * 1 + 48), *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    a3 = 0;
    v_rdi = (v_rip + 6484562) + (136);
    a2 = 0;
    v_rdi = (v_rdi) + (v_rbx);
    result = KeAbPreAcquire(v_rdi, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    if (!(condition_is_above_or_equal)) {
        a3 = v_rdi;
        a2 = result;
        a1 = v_rdi;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a3 = 0;
    a1 = (v_rip + 6484498) + (112);
    a2 = 0;
    a1 = (a1) + (v_rbx);
    result = KeSetEvent(a1, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    result = CmpNotifyMachineHiveLoaded(3, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    a1 = (*(unsigned __int64 *)(v_rdi)) & (-16);
    a2 = *(unsigned __int64 *)(v_rdi) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (2)) != 0) goto loc_007DA6D3;
    result = *(unsigned __int64 *)(v_rdi);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (2)) != 0) {
        a1 = v_rdi;
        result = ExfReleasePushLock(a1, a2, 0, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    }
    result = KeAbPostRelease(v_rdi, a2, 0, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 6484828)) == 0) goto loc_007DA71A;
    if ((*(unsigned int *)(v_rip + 6505856)) == 0) goto loc_007DA71A;
    result = CmpUnlockRegistry(v_rdi, a2, 0, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    result = ExpRefreshSystemTime(v_rdi, a2, 0, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    v_r12 = 0;
    if (0 == 0) {
        result = CmpLoadSystemVersionData(v_rdi, a2, 0, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
        result = CmpSetVersionData(v_rdi, a2, 0, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
        v_r12 = 1;
    }
    result = PsBootPhaseComplete(v_rdi, a2, 0, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
loc_007DA71A:
    if ((unsigned __int8)(v_r12) == 0) {
        result = CmpLoadSystemVersionData(v_rdi, a2, 0, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    }
    if (0 == 0) goto loc_007DA90D;
    goto loc_007DA861;
loc_007DA73C:
    if (0 != 2) goto loc_007DA832;
    result = CmpUnlockRegistry(v_rdi, a2, 0, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    if (a1 != 0) goto loc_007DA82B;
    a3 = 0;
    v_rdi = (v_rip + 6484329 + 136) + (v_rbx);
    a2 = 0;
    result = KeAbPreAcquire(v_rdi, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    if (!(condition_is_above_or_equal)) {
        a3 = v_rdi;
        a2 = result;
        a1 = v_rdi;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    }
    v_r14 = 0;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a3 = 0;
    a1 = (v_rip + 6484233) + (112);
    a2 = 0;
    a1 = (a1) + (v_rbx);
    result = KeSetEvent(a1, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    result = CmpNotifyMachineHiveLoaded(2, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    a1 = (*(unsigned __int64 *)(v_rdi)) & (-16);
    a2 = *(unsigned __int64 *)(v_rdi) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (2)) != 0) goto loc_007DA7D9;
    result = *(unsigned __int64 *)(v_rdi);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (2)) != 0) {
        a1 = v_rdi;
        result = ExfReleasePushLock(a1, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    }
    result = KeAbPostRelease(v_rdi, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 6484750)) == 0) goto loc_007DA81A;
    if ((*(unsigned int *)(v_rip + 6505594)) == 0) goto loc_007DA81A;
    result = ExpRefreshSystemTime(v_rdi, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    if ((unsigned __int8)(v_r12) == 0) {
        result = CmpLoadSystemVersionData(v_rdi, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
        result = CmpSetVersionData(v_rdi, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
        v_r12 = 1;
    }
    result = PsBootPhaseComplete(v_rdi, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    goto loc_007DA824;
loc_007DA81A:
    if ((unsigned __int8)(v_r12) == 0) {
        result = CmpSetVersionData(v_rdi, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    }
loc_007DA82B:
    result = CmpCreatePerfKeys(v_rdi, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    goto loc_007DA866;
loc_007DA832:
    if (0 != 1) goto loc_007DA848;
    goto loc_007DA85C;
loc_007DA848:
    if (0 != 4) goto loc_007DA861;
loc_007DA85C:
    result = CmpLinkKeyToHive(v_rip + 3335892, v_rip + 3335851, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
loc_007DA861:
    result = CmpUnlockRegistry(v_rip + 3335892, v_rip + 3335851, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
loc_007DA866:
    if (a1 != 0) goto loc_007DA90D;
    if (1 != 0) goto loc_007DA90D;
    a3 = 0;
    v_rdi = (v_rip + 6484085 + 136) + (v_rbx);
    a2 = 0;
    result = KeAbPreAcquire(v_rdi, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    if (!(condition_is_above_or_equal)) {
        a3 = v_rdi;
        a2 = result;
        a1 = v_rdi;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    }
    v_r14 = 0;
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a3 = 0;
    a2 = 0;
    a1 = (v_rip + 6483941 + 112) + (v_rbx);
    result = KeSetEvent(a1, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    result = CmpNotifyMachineHiveLoaded(0, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    a1 = (*(unsigned __int64 *)(v_rdi)) & (-16);
    a2 = *(unsigned __int64 *)(v_rdi) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (2)) != 0) goto loc_007DA8F8;
    result = *(unsigned __int64 *)(v_rdi);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rdi))) & (2)) != 0) {
        a1 = v_rdi;
        result = ExfReleasePushLock(a1, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    }
    result = KeAbPostRelease(v_rdi, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    goto loc_007DA46D;
loc_007DA90D:
loc_007DA914:
    v_r15 = (unsigned int)((0) + 1);
    goto loc_007DA443;
loc_007DA91C:
    if (v_stack_m318 == ((unsigned __int8)(v_rdi))) goto loc_007DAA47;
    goto loc_007DA414;
loc_007DA934:
loc_007DA93B:
    result = CmpIsHiveLoadUnloadRundownActive(3, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
    v_r15 = 0;
    if ((unsigned __int8)(result) == 0) goto loc_007DAA29;
    *(unsigned __int8 *)(v_rip + 7426546) = 0;
    *(unsigned __int64 *)(v_rip + 7426543) = 0;
    result = CmpUnlockRegistry(3, a2, a3, *(unsigned __int8 *)(v_rbx + v_rip + 6484967 * 1 + 59));
loc_007DA968:
    if ((*(unsigned int *)(v_rip + 6483904 - 68)) == 0) goto loc_007DAA10;
    if ((*(unsigned __int8 *)(v_rip + 6483904 - 80)) != 0) goto loc_007DAA10;
    if ((*(unsigned __int8 *)(v_rip + 6483904 - 79)) == 0) {
        a1 = v_rip + 6483904 - 48;
        v_stack_m358 = 0;
        a4 = 0;
        a3 = 0;
        a2 = 0;
        result = KeWaitForSingleObject(a1, a2, a3, a4);
    }
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 6483904, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 6483904;
        a2 = result;
        a1 = v_rip + 6483904;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_rip + 6483904 - 24, a2, a3, a4);
    result = CmpNotifyMachineHiveLoaded(0, a2, a3, a4);
    a1 = (*(unsigned __int64 *)(v_rip + 6483904)) & (-16);
    a2 = *(unsigned __int64 *)(v_rip + 6483904) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 6483904))) & (2)) != 0) goto loc_007DAA00;
    result = *(unsigned __int64 *)(v_rip + 6483904);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 6483904))) & (2)) != 0) {
        a1 = v_rip + 6483904;
        result = ExfReleasePushLock(a1, a2, a3, a4);
    }
    result = KeAbPostRelease(v_rip + 6483904, a2, a3, a4);
loc_007DAA10:
    v_rdi = (unsigned int)((0) + 1);
    v_rbx = (v_rip + 6483904) + (184);
    if (((unsigned int)(v_rdi)) < 7) goto loc_007DA968;
    v_rdi = 0;
    goto loc_007DABF2;
loc_007DAA29:
    v_stack_m358 = v_stack_m310;
    result = KeBugCheckEx(1 + 114, 1, v_rip + 6483904, 0);
loc_007DAA47:
    result = CmpLockRegistryExclusive(1 + 114, 1, v_rip + 6483904, 0);
    *(unsigned __int8 *)(v_rip + 8377789) = 0;
    if ((*(unsigned __int8 *)(v_rip + 8377777)) != 0) goto loc_007DAA67;
    result = 1;
    if ((*(unsigned int *)(v_rip + 6505013)) != 1) {
        result = 0;
    }
    *(unsigned __int8 *)(v_rip + 6505008) = (unsigned __int8)(result);
    result = CmpUnlockRegistry(1 + 114, 1, v_rip + 6483904, 0);
    if (a1 == 0) goto loc_007DAB99;
    a2 = 0;
    result = KiStackAttachProcess(*(unsigned __int64 *)(v_rip + 8306731), a2, v_rsp - 632 - 32, 0);
    a1 = 0;
    result = CmpInitCmRM(a1, *(unsigned __int8 *)(v_rip + 7426258), v_rsp - 632 - 32, 0);
    a2 = 0;
    result = KiUnstackDetachProcess(v_rsp - 632 - 32, a2, v_rsp - 632 - 32, 0);
    if (*(unsigned __int64 *)(v_rip + 7426505) != 0) {
        a3 = *(unsigned __int64 *)(v_rip + 7426505);
        a2 = v_rip + 1928850;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7426505) + 56);
        result = TmEnableCallbacks(a1, a2, a3, 0);
        a1 = *(unsigned __int64 *)(v_rip + 7426474);
        result = CmRmFinalizeRecovery(a1, a2, a3, 0);
    }
    result = CmpMountPreloadedHives(a1, a2, a3, 0);
    result = CmpLockRegistryExclusive(a1, a2, a3, 0);
    result = CmpInterlockedFunction(a1, a2, a3, 0);
    result = CmpUnlockRegistry(a1, a2, a3, 0);
    v_r14 = 0;
loc_007DAAF1:
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 6483511, a2, a3, 0);
    if (!(condition_is_above_or_equal)) {
        a3 = v_rip + 6483511;
        a2 = result;
        a1 = v_rip + 6483511;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, 0);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_rip + 6483511 - 24, a2, a3, 0);
    result = CmpNotifyMachineHiveLoaded(0, a2, a3, 0);
    a1 = (*(unsigned __int64 *)(v_rip + 6483511)) & (-16);
    a2 = *(unsigned __int64 *)(v_rip + 6483511) - 16;
    if (a1 <= 16) { a2 = 0; }
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 6483511))) & (2)) != 0) goto loc_007DAB59;
    result = *(unsigned __int64 *)(v_rip + 6483511);
    if ((((unsigned __int8)(*(unsigned __int64 *)(v_rip + 6483511))) & (2)) != 0) {
        a1 = v_rip + 6483511;
        result = ExfReleasePushLock(a1, a2, a3, 0);
    }
    result = KeAbPostRelease(v_rip + 6483511, a2, a3, 0);
    v_rdi = (unsigned int)((v_rdi) + 1);
    v_rbx = (v_rip + 6483511) + (184);
    if (((unsigned int)(v_rdi)) < 7) goto loc_007DAAF1;
    v_rdi = 0;
    if ((*(unsigned int *)(v_rip + 6504689)) != 0) {
        result = ExpRefreshSystemTime(v_rip + 6483511, a2, a3, 0);
        result = PsBootPhaseComplete(v_rip + 6483511, a2, a3, 0);
    }
    result = CmpLoadSystemVersionData(v_rip + 6483511, a2, a3, 0);
    result = CmpSetVersionData(v_rip + 6483511, a2, a3, 0);
loc_007DAB99:
    a4 = 0;
    v_stack_m348 = 0;
    v_stack_m350 = 0;
    *(unsigned int *)(v_rsp - 632 - 104) = 48;
    *(unsigned __int64 *)(v_rsp - 632 - 96) = 0;
    *(unsigned int *)(v_rsp - 632 - 80) = 576;
    *(unsigned __int64 *)(v_rsp - 632 - 88) = v_rip + 6485096;
    *(unsigned __int64 *)(v_rsp - 632 - 72) = v_xmm0;
    v_stack_m358 = 0;
    result = ZwCreateKey(v_rsp - 632 - 128, a4 + 2, v_rsp - 632 - 104, a4);
    if (!(sign_flag)) {
        a1 = *(unsigned __int64 *)(v_rsp - 632 - 128);
        result = ZwClose(a1, a4 + 2, v_rsp - 632 - 104, a4);
    }
loc_007DABF2:
    *(unsigned __int8 *)(v_rip + 8377374) = 0;
    *(unsigned __int8 *)(v_rip + 7425860) = 0;
    *(unsigned __int64 *)(v_rip + 7425857) = 0;
    if (a1 != 0) {
        a3 = 0;
        a2 = 0;
        a1 = a1;
        result = KeSetEvent(a1, a2, a3, a4);
    }
    if (v_stack_m300 != 0) {
        a2 = 0;
        a1 = v_stack_m300;
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    result = CmSiFreeMemory(*(unsigned __int64 *)(v_rsp - 632 - 120), a2, a3, a4);
    result = CmSiFreeMemory(*(unsigned __int64 *)(v_rsp - 632 - 112), a2, a3, a4);
    result = CmCleanupThreadInfo(v_rsp - 632 - 56, a2, a3, a4);
    a1 = (*(unsigned __int64 *)(v_rsp - 632 + 576)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpFinishSystemHivesLoad(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m300;
    uint64_t v_stack_m308;
    uint16_t v_stack_m30E;
    uint64_t v_stack_m310;
    uint16_t v_stack_m316;
    uint8_t v_stack_m318;
    uint64_t v_stack_m320;
    uint8_t v_stack_m328;
    uint64_t v_stack_m330;
    uint64_t v_stack_m338;
    uint64_t v_stack_m340;
    uint64_t v_stack_m348;
    uint8_t v_stack_m350;
    uint64_t v_stack_m358;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (848);
    result = (*(uint64_t *)(v_rip + 0x630503)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x278 + 0x240) = result;
    result = 0;
    *(uint64_t *)(local_rsp - 0x278 - 0x48) = 0;
    local_rdi = 0;
    *(uint32_t *)(local_rsp - 0x278 - 0x40) = 0;
    *(uint64_t *)(local_rsp - 0x278 - 0x80) = 0;
    *(uint64_t *)(local_rsp - 0x278 - 0x68) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x278 - 0x28) = 0;
    *(uint64_t *)(local_rsp - 0x278 - 0x58) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x278 - 0x20) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x278 - 0x10) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x278) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x278 - 0x38) = v_xmm0;
    result = CmpInitializeThreadInfo(local_rsp - 632 - 56, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = memset(local_rsp - 632 + 16, Arg2, 432, Arg4);
    *(uint8_t *)(v_rip + 0x7FDD65) = 0;
    *(uint64_t *)(v_rip + 0x715890) = *(uint64_t *)(gs_base + (0 + 0x188));
    v_stack_m310 = v_xmm0;
    v_stack_m30E = 128;
    v_stack_m308 = local_rsp - 632 + 448;
    result = RtlUnicodeStringCopyString(v_stack_m310, v_rip + 3337533, 432, Arg4);
    v_stack_m316 = (uint16_t)(v_stack_m310);
    result = CmpAllocatePool((uint32_t)((uint32_t)(local_rdi + 64)), 336, (uint32_t)((uint32_t)((uint32_t)(0x20204D43ULL))), Arg4);
    *(uint64_t *)(local_rsp - 0x278 - 0x78) = result;
    if (result == 0) {
        Arg4 = 0;
        v_stack_m358 = 0xFFFFFFFFC000009AULL;
        Arg2 = local_rdi + 2;
        Arg1 = local_rdi + 116;
        Arg3 = local_rdi + 4;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    result = CmpAllocatePool(local_rdi + 64, 56, (uint32_t)((uint32_t)((uint32_t)(0x20204D43ULL))), Arg4);
    *(uint64_t *)(local_rsp - 0x278 - 0x70) = result;
    if (result == 0) {
        Arg4 = 0;
        v_stack_m358 = 0xFFFFFFFFC000009AULL;
        Arg2 = result + 2;
        Arg1 = result + 116;
        Arg3 = result + 6;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    result = CmpHiveRootSecurityDescriptor(Arg1, Arg2, Arg3, Arg4);
    v_stack_m300 = result;
loc_007DA378:
    *(uint64_t *)(result) = v_rip + 6485385;
    Arg2 = (v_rip + 6485385) + (184);
    Arg3 = (7) - (1);
    if (condition_is_not_equal) goto loc_007DA378;
    if (Arg1 != 0) goto loc_007DA40D;
    Arg4 = 0;
    v_stack_m358 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_rip + 6485886, Arg2, Arg3, Arg4);
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_rip + 6485871, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = KiStackAttachProcess(*(uint64_t *)(v_rip + 0x7EC6F1), Arg2, local_rsp - 632 - 32, Arg4);
    Arg1 = 0;
    result = CmpInitCmRM(Arg1, *(uint8_t *)(v_rip + 0x715798), local_rsp - 632 - 32, Arg4);
    Arg2 = 0;
    result = KiUnstackDetachProcess(local_rsp - 632 - 32, Arg2, local_rsp - 632 - 32, Arg4);
    if (*(uint64_t *)(v_rip + 0x71588F) != 0) {
        Arg3 = *(uint64_t *)(v_rip + 0x71588F);
        Arg2 = v_rip + 1930584;
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x71588F) + 0x38);
        result = TmEnableCallbacks(Arg1, Arg2, Arg3, Arg4);
        Arg1 = *(uint64_t *)(v_rip + 0x715870);
        result = CmRmFinalizeRecovery(Arg1, Arg2, Arg3, Arg4);
    }
loc_007DA414:
    Arg4 = 0;
    v_stack_m340 = result;
    v_stack_m348 = 0;
    v_stack_m350 = 0;
    v_stack_m358 = 0;
    result = KeWaitForMultipleObjects(Arg4 + 7, result, Arg4 + 1, Arg4);
    v_stack_m318 = 0;
loc_007DA443:
    if (0 >= 7) goto loc_007DA91C;
    local_r14 = 0;
    local_rbx = (result) * (0);
    if ((*(uint8_t *)(local_rbx + v_rip + 0x62F48C * 1 + 0x38)) != 0) goto loc_007DA46D;
    if ((*(uint8_t *)(local_rbx + v_rip + 0x62F48C * 1 + 0x39)) != 0) goto loc_007DA474;
    v_stack_m318 = 1;
loc_007DA46D:
    local_rdi = 0;
    goto loc_007DA914;
loc_007DA474:
    v_stack_m310 = (uint16_t)(v_stack_m316);
    result = RtlAppendUnicodeToString(v_stack_m310, *(uint64_t *)(local_rbx + v_rip + 0x62F420 * 1 + 0x8), Arg4 + 1, Arg4);
    result = RtlAppendUnicodeToString(v_stack_m310, *(uint64_t *)(local_rbx + v_rip + 0x62F402 * 1 + 0x10), Arg4 + 1, Arg4);
    result = CmpLockRegistryExclusive(v_stack_m310, *(uint64_t *)(local_rbx + v_rip + 0x62F402 * 1 + 0x10), Arg4 + 1, Arg4);
    if ((*(uint64_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x18)) != 0) goto loc_007DA5FF;
    if (*(uint64_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x30) == 0) goto loc_007DA5FF;
    v_stack_m320 = local_rsp - 632 + 16;
    Arg2 = 0;
    v_stack_m328 = 1;
    result = 0;
    v_stack_m330 = 0;
    v_stack_m338 = 0;
    v_stack_m340 = v_stack_m300;
    v_stack_m348 = 0;
    v_stack_m350 = 0;
    v_stack_m358 = (uint32_t)((uint32_t)(*(uint32_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x28)));
    result = CmpLinkHiveToMaster(v_stack_m310, Arg2, *(uint64_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x30), *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    if (sign_flag) goto loc_007DA93B;
    result = CmpLockHiveListExclusive((int32_t)((uint32_t)(result)), Arg2, *(uint64_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x30), *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    result = (*(uint64_t *)(local_rbx + v_rip + 0x62F36A * 1 + 0x30)) + (0x648ULL);
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x7FF7F1))) != (v_rip + 8386518)) goto loc_007DA934;
    *(uint64_t *)(result) = v_rip + 8386518;
    *(uint64_t *)(result + 0x8) = *(uint64_t *)(v_rip + 0x7FF7F1);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x7FF7F1)) = result;
    *(uint64_t *)(v_rip + 0x7FF7BE) = result;
    result = CmpUnlockHiveList(*(uint64_t *)(v_rip + 0x7FF7F1), v_rip + 8386518, *(uint64_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x30), *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    result = CmpRecheckHiveVolumePolicy(*(uint64_t *)(local_rbx + v_rip + 0x62F36A * 1 + 0x30), v_rip + 8386518, *(uint64_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x30), *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    local_rdi = 0;
    if ((*(uint8_t *)(local_rbx + v_rip + 0x62F36A * 1 + 0x3B)) != 0) {
        result = *(uint64_t *)(local_rbx + v_rip + 0x62F36A * 1 + 0x30);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = *(uint64_t *)(local_rbx + v_rip + 0x62F36A * 1 + 0x30);
        *(uint64_t *)(result + 0x1048) = Arg1;
        result = CmpUnlockRegistry(Arg1, v_rip + 8386518, *(uint64_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x30), *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
        Arg1 = *(uint64_t *)(local_rbx + v_rip + 0x62F36A * 1 + 0x30);
        Arg2 = local_rdi + 4;
        result = CmpFlushHive(Arg1, Arg2, *(uint64_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x30), *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
        result = CmpLockRegistryExclusive(Arg1, Arg2, *(uint64_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x30), *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
        result = *(uint64_t *)(local_rbx + v_rip + 0x62F36A * 1 + 0x30);
        result = *(uint64_t *)(local_rbx + v_rip + 0x62F36A * 1 + 0x30);
        *(uint64_t *)(result + 0x1048) = 0;
    }
    if (*(uint64_t *)(v_rip + 0x7156A7) == 0) goto loc_007DA608;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(local_rbx + v_rip + 0x62F36A * 1 + 0x30) + 0xA0)))) & (2)) != 0) goto loc_007DA608;
    if ((*(uint64_t *)(*(uint64_t *)(local_rbx + v_rip + 0x62F36A * 1 + 0x30) + 0x1038)) != 0) goto loc_007DA608;
    *(uint64_t *)(*(uint64_t *)(local_rbx + v_rip + 0x62F36A * 1 + 0x30) + 0x1038) = *(uint64_t *)(v_rip + 0x7156A7);
    goto loc_007DA608;
loc_007DA5FF:
    local_rdi = 0;
loc_007DA608:
    result = *(uint64_t *)(local_rbx + v_rip + 0x62F36A * 1 + 0x30);
    if (*(uint64_t *)(local_rbx + v_rip + 0x62F29A * 1 + 0x30) != 0) {
        result = CmpAddToHiveFileList(*(uint64_t *)(local_rbx + v_rip + 0x62F29A * 1 + 0x30), *(uint64_t *)(local_rbx + v_rip + 0x62F36A * 1 + 0x30), *(uint64_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x30), *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    }
    *(uint8_t *)(local_rbx + v_rip + 0x62F29A * 1 + 0x38) = 1;
    if (0 != 3) goto loc_007DA73C;
    if (Arg1 != 0) goto loc_007DA861;
    result = CmpUnlockRegistry(*(uint64_t *)(local_rbx + v_rip + 0x62F29A * 1 + 0x30), *(uint64_t *)(local_rbx + v_rip + 0x62F36A * 1 + 0x30), *(uint64_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x30), *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    result = CmpMountPreloadedHives(*(uint64_t *)(local_rbx + v_rip + 0x62F29A * 1 + 0x30), *(uint64_t *)(local_rbx + v_rip + 0x62F36A * 1 + 0x30), *(uint64_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x30), *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    result = CmpLockRegistryExclusive(*(uint64_t *)(local_rbx + v_rip + 0x62F29A * 1 + 0x30), *(uint64_t *)(local_rbx + v_rip + 0x62F36A * 1 + 0x30), *(uint64_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x30), *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    result = CmpInterlockedFunction(*(uint64_t *)(local_rbx + v_rip + 0x62F29A * 1 + 0x30), *(uint64_t *)(local_rbx + v_rip + 0x62F36A * 1 + 0x30), *(uint64_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x30), *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    Arg3 = 0;
    local_rdi = (v_rip + 6484562) + (136);
    Arg2 = 0;
    local_rdi = (local_rdi) + (local_rbx);
    result = KeAbPreAcquire(local_rdi, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rdi;
        Arg2 = result;
        Arg1 = local_rdi;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    Arg3 = 0;
    Arg1 = (v_rip + 6484498) + (112);
    Arg2 = 0;
    Arg1 = (Arg1) + (local_rbx);
    result = KeSetEvent(Arg1, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    result = CmpNotifyMachineHiveLoaded(3, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    Arg1 = (*(uint64_t *)(local_rdi)) & (-16);
    Arg2 = *(uint64_t *)(local_rdi) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (2)) != 0) goto loc_007DA6D3;
    result = *(uint64_t *)(local_rdi);
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (2)) != 0) {
        Arg1 = local_rdi;
        result = ExfReleasePushLock(Arg1, Arg2, 0, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    }
    result = KeAbPostRelease(local_rdi, Arg2, 0, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x62F35C)) == 0) goto loc_007DA71A;
    if ((*(uint32_t *)(v_rip + 0x634580)) == 0) goto loc_007DA71A;
    result = CmpUnlockRegistry(local_rdi, Arg2, 0, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    result = ExpRefreshSystemTime(local_rdi, Arg2, 0, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    local_r12 = 0;
    if (0 == 0) {
        result = CmpLoadSystemVersionData(local_rdi, Arg2, 0, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
        result = CmpSetVersionData(local_rdi, Arg2, 0, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
        local_r12 = 1;
    }
    result = PsBootPhaseComplete(local_rdi, Arg2, 0, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
loc_007DA71A:
    if ((uint8_t)(local_r12) == 0) {
        result = CmpLoadSystemVersionData(local_rdi, Arg2, 0, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    }
    if (0 == 0) goto loc_007DA90D;
    goto loc_007DA861;
loc_007DA73C:
    if (0 != 2) goto loc_007DA832;
    result = CmpUnlockRegistry(local_rdi, Arg2, 0, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    if (Arg1 != 0) goto loc_007DA82B;
    Arg3 = 0;
    local_rdi = (v_rip + 6484329 + 136) + (local_rbx);
    Arg2 = 0;
    result = KeAbPreAcquire(local_rdi, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rdi;
        Arg2 = result;
        Arg1 = local_rdi;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    }
    local_r14 = 0;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    Arg3 = 0;
    Arg1 = (v_rip + 6484233) + (112);
    Arg2 = 0;
    Arg1 = (Arg1) + (local_rbx);
    result = KeSetEvent(Arg1, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    result = CmpNotifyMachineHiveLoaded(2, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    Arg1 = (*(uint64_t *)(local_rdi)) & (-16);
    Arg2 = *(uint64_t *)(local_rdi) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (2)) != 0) goto loc_007DA7D9;
    result = *(uint64_t *)(local_rdi);
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (2)) != 0) {
        Arg1 = local_rdi;
        result = ExfReleasePushLock(Arg1, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    }
    result = KeAbPostRelease(local_rdi, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x62F30E)) == 0) goto loc_007DA81A;
    if ((*(uint32_t *)(v_rip + 0x63447A)) == 0) goto loc_007DA81A;
    result = ExpRefreshSystemTime(local_rdi, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    if ((uint8_t)(local_r12) == 0) {
        result = CmpLoadSystemVersionData(local_rdi, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
        result = CmpSetVersionData(local_rdi, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
        local_r12 = 1;
    }
    result = PsBootPhaseComplete(local_rdi, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    goto loc_007DA824;
loc_007DA81A:
    if ((uint8_t)(local_r12) == 0) {
        result = CmpSetVersionData(local_rdi, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    }
loc_007DA82B:
    result = CmpCreatePerfKeys(local_rdi, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    goto loc_007DA866;
loc_007DA832:
    if (0 != 1) goto loc_007DA848;
    goto loc_007DA85C;
loc_007DA848:
    if (0 != 4) goto loc_007DA861;
loc_007DA85C:
    result = CmpLinkKeyToHive(v_rip + 3335892, v_rip + 3335851, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
loc_007DA861:
    result = CmpUnlockRegistry(v_rip + 3335892, v_rip + 3335851, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
loc_007DA866:
    if (Arg1 != 0) goto loc_007DA90D;
    if (1 != 0) goto loc_007DA90D;
    Arg3 = 0;
    local_rdi = (v_rip + 6484085 + 136) + (local_rbx);
    Arg2 = 0;
    result = KeAbPreAcquire(local_rdi, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    if (!(condition_is_above_or_equal)) {
        Arg3 = local_rdi;
        Arg2 = result;
        Arg1 = local_rdi;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    }
    local_r14 = 0;
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = (v_rip + 6483941 + 112) + (local_rbx);
    result = KeSetEvent(Arg1, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    result = CmpNotifyMachineHiveLoaded(0, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    Arg1 = (*(uint64_t *)(local_rdi)) & (-16);
    Arg2 = *(uint64_t *)(local_rdi) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (2)) != 0) goto loc_007DA8F8;
    result = *(uint64_t *)(local_rdi);
    if ((((uint8_t)(*(uint64_t *)(local_rdi))) & (2)) != 0) {
        Arg1 = local_rdi;
        result = ExfReleasePushLock(Arg1, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    }
    result = KeAbPostRelease(local_rdi, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    goto loc_007DA46D;
loc_007DA90D:
loc_007DA914:
    local_r15 = (uint32_t)((0) + 1);
    goto loc_007DA443;
loc_007DA91C:
    if (v_stack_m318 == ((uint8_t)(local_rdi))) goto loc_007DAA47;
    goto loc_007DA414;
loc_007DA934:
loc_007DA93B:
    result = CmpIsHiveLoadUnloadRundownActive(3, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
    local_r15 = 0;
    if ((uint8_t)(result) == 0) goto loc_007DAA29;
    *(uint8_t *)(v_rip + 0x7151F2) = 0;
    *(uint64_t *)(v_rip + 0x7151EF) = 0;
    result = CmpUnlockRegistry(3, Arg2, Arg3, *(uint8_t *)(local_rbx + v_rip + 0x62F3E7 * 1 + 0x3B));
loc_007DA968:
    if ((*(uint32_t *)(v_rip + 0x62EFC0 - 0x44)) == 0) goto loc_007DAA10;
    if ((*(uint8_t *)(v_rip + 0x62EFC0 - 0x50)) != 0) goto loc_007DAA10;
    if ((*(uint8_t *)(v_rip + 0x62EFC0 - 0x4F)) == 0) {
        Arg1 = v_rip + 6483904 - 48;
        v_stack_m358 = 0;
        Arg4 = 0;
        Arg3 = 0;
        Arg2 = 0;
        result = KeWaitForSingleObject(Arg1, Arg2, Arg3, Arg4);
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 6483904, Arg2, Arg3, Arg4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 6483904;
        Arg2 = result;
        Arg1 = v_rip + 6483904;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_rip + 6483904 - 24, Arg2, Arg3, Arg4);
    result = CmpNotifyMachineHiveLoaded(0, Arg2, Arg3, Arg4);
    Arg1 = (*(uint64_t *)(v_rip + 0x62EFC0)) & (-16);
    Arg2 = *(uint64_t *)(v_rip + 0x62EFC0) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x62EFC0))) & (2)) != 0) goto loc_007DAA00;
    result = *(uint64_t *)(v_rip + 0x62EFC0);
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x62EFC0))) & (2)) != 0) {
        Arg1 = v_rip + 6483904;
        result = ExfReleasePushLock(Arg1, Arg2, Arg3, Arg4);
    }
    result = KeAbPostRelease(v_rip + 6483904, Arg2, Arg3, Arg4);
loc_007DAA10:
    local_rdi = (uint32_t)((0) + 1);
    local_rbx = (v_rip + 6483904) + (184);
    if (((uint32_t)(local_rdi)) < 7) goto loc_007DA968;
    local_rdi = 0;
    goto loc_007DABF2;
loc_007DAA29:
    v_stack_m358 = v_stack_m310;
    result = KeBugCheckEx(1 + 114, 1, v_rip + 6483904, 0);
loc_007DAA47:
    result = CmpLockRegistryExclusive(1 + 114, 1, v_rip + 6483904, 0);
    *(uint8_t *)(v_rip + 0x7FD5BD) = 0;
    if ((*(uint8_t *)(v_rip + 0x7FD5B1)) != 0) goto loc_007DAA67;
    result = 1;
    if ((*(uint32_t *)(v_rip + 0x634235)) != 1) {
        result = 0;
    }
    *(uint8_t *)(v_rip + 0x634230) = (uint8_t)(result);
    result = CmpUnlockRegistry(1 + 114, 1, v_rip + 6483904, 0);
    if (Arg1 == 0) goto loc_007DAB99;
    Arg2 = 0;
    result = KiStackAttachProcess(*(uint64_t *)(v_rip + 0x7EC02B), Arg2, local_rsp - 632 - 32, 0);
    Arg1 = 0;
    result = CmpInitCmRM(Arg1, *(uint8_t *)(v_rip + 0x7150D2), local_rsp - 632 - 32, 0);
    Arg2 = 0;
    result = KiUnstackDetachProcess(local_rsp - 632 - 32, Arg2, local_rsp - 632 - 32, 0);
    if (*(uint64_t *)(v_rip + 0x7151C9) != 0) {
        Arg3 = *(uint64_t *)(v_rip + 0x7151C9);
        Arg2 = v_rip + 1928850;
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x7151C9) + 0x38);
        result = TmEnableCallbacks(Arg1, Arg2, Arg3, 0);
        Arg1 = *(uint64_t *)(v_rip + 0x7151AA);
        result = CmRmFinalizeRecovery(Arg1, Arg2, Arg3, 0);
    }
    result = CmpMountPreloadedHives(Arg1, Arg2, Arg3, 0);
    result = CmpLockRegistryExclusive(Arg1, Arg2, Arg3, 0);
    result = CmpInterlockedFunction(Arg1, Arg2, Arg3, 0);
    result = CmpUnlockRegistry(Arg1, Arg2, Arg3, 0);
    local_r14 = 0;
loc_007DAAF1:
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 6483511, Arg2, Arg3, 0);
    if (!(condition_is_above_or_equal)) {
        Arg3 = v_rip + 6483511;
        Arg2 = result;
        Arg1 = v_rip + 6483511;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, 0);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_rip + 6483511 - 24, Arg2, Arg3, 0);
    result = CmpNotifyMachineHiveLoaded(0, Arg2, Arg3, 0);
    Arg1 = (*(uint64_t *)(v_rip + 0x62EE37)) & (-16);
    Arg2 = *(uint64_t *)(v_rip + 0x62EE37) - 16;
    if (Arg1 <= 16) { Arg2 = 0; }
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x62EE37))) & (2)) != 0) goto loc_007DAB59;
    result = *(uint64_t *)(v_rip + 0x62EE37);
    if ((((uint8_t)(*(uint64_t *)(v_rip + 0x62EE37))) & (2)) != 0) {
        Arg1 = v_rip + 6483511;
        result = ExfReleasePushLock(Arg1, Arg2, Arg3, 0);
    }
    result = KeAbPostRelease(v_rip + 6483511, Arg2, Arg3, 0);
    local_rdi = (uint32_t)((local_rdi) + 1);
    local_rbx = (v_rip + 6483511) + (184);
    if (((uint32_t)(local_rdi)) < 7) goto loc_007DAAF1;
    local_rdi = 0;
    if ((*(uint32_t *)(v_rip + 0x6340F1)) != 0) {
        result = ExpRefreshSystemTime(v_rip + 6483511, Arg2, Arg3, 0);
        result = PsBootPhaseComplete(v_rip + 6483511, Arg2, Arg3, 0);
    }
    result = CmpLoadSystemVersionData(v_rip + 6483511, Arg2, Arg3, 0);
    result = CmpSetVersionData(v_rip + 6483511, Arg2, Arg3, 0);
loc_007DAB99:
    Arg4 = 0;
    v_stack_m348 = 0;
    v_stack_m350 = 0;
    *(uint32_t *)(local_rsp - 0x278 - 0x68) = 48;
    *(uint64_t *)(local_rsp - 0x278 - 0x60) = 0;
    *(uint32_t *)(local_rsp - 0x278 - 0x50) = 576;
    *(uint64_t *)(local_rsp - 0x278 - 0x58) = v_rip + 6485096;
    *(uint64_t *)(local_rsp - 0x278 - 0x48) = v_xmm0;
    v_stack_m358 = 0;
    result = ZwCreateKey(local_rsp - 632 - 128, Arg4 + 2, local_rsp - 632 - 104, Arg4);
    if (!(sign_flag)) {
        Arg1 = *(uint64_t *)(local_rsp - 0x278 - 0x80);
        result = ZwClose(Arg1, Arg4 + 2, local_rsp - 632 - 104, Arg4);
    }
loc_007DABF2:
    *(uint8_t *)(v_rip + 0x7FD41E) = 0;
    *(uint8_t *)(v_rip + 0x714F44) = 0;
    *(uint64_t *)(v_rip + 0x714F41) = 0;
    if (Arg1 != 0) {
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = Arg1;
        result = KeSetEvent(Arg1, Arg2, Arg3, Arg4);
    }
    if (v_stack_m300 != 0) {
        Arg2 = 0;
        Arg1 = v_stack_m300;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    }
    result = CmSiFreeMemory(*(uint64_t *)(local_rsp - 0x278 - 0x78), Arg2, Arg3, Arg4);
    result = CmSiFreeMemory(*(uint64_t *)(local_rsp - 0x278 - 0x70), Arg2, Arg3, Arg4);
    result = CmCleanupThreadInfo(local_rsp - 632 - 56, Arg2, Arg3, Arg4);
    Arg1 = (*(uint64_t *)(local_rsp - 0x278 + 0x240)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007DA210&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
