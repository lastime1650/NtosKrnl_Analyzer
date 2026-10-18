# CmpLoadHiveThread

- RVA: `0x007DB040`–`0x007DBBA4` (길이 `2,916` bytes)
- VA: `0x00000001407DB040`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D633C`
- 디코드: `681`개 명령, `2,916/2,916` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **83**; 고유 호출 대상: **47**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **25**

### Outgoing calls
- `0x007DB0AB` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007DB0B9` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (function, `0x003FBE70`)
- `0x007DB102` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x007DB126` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (function, `0x0020E6B0`)
- `0x007DB197` → [wil_details_FeatureReporting_ReportUsageToService](../../text/53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (function, `0x0053E6E4`)
- `0x007DB1AB` → [wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath](../../text/53/wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath_function_0053E774.md) (function, `0x0053E774`)
- `0x007DB1C5` → [CmpMachineHiveCacheClaimEntry](../7E/CmpMachineHiveCacheClaimEntry_function_007E8DFC.md) (function, `0x007E8DFC`)
- `0x007DB1E8` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x007DB25B` → [wil_details_FeatureReporting_ReportUsageToService](../../text/53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (function, `0x0053E6E4`)
- `0x007DB26F` → [wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath](../../text/53/wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath_function_0053E774.md) (function, `0x0053E774`)
- `0x007DB2B6` → [CmpInitHiveFromFile](../87/CmpInitHiveFromFile_function_008794D4.md) (function, `0x008794D4`)
- `0x007DB324` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x007DB351` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x007DB376` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007DB3C3` → [wil_details_FeatureReporting_ReportUsageToService](../../text/53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (function, `0x0053E6E4`)
- `0x007DB3D7` → [wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath](../../text/53/wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath_function_0053E774.md) (function, `0x0053E774`)
- `0x007DB3F5` → [CmpHiveCacheEntryCleanup](../7F/CmpHiveCacheEntryCleanup_function_007F5B38.md) (function, `0x007F5B38`)
- `0x007DB3FE` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (function, `0x0041FD50`)
- `0x007DB405` → [PsTerminateSystemThread](../9B/PsTerminateSystemThread_function_009BCE50.md) (function, `0x009BCE50`)
- `0x007DB414` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x007DB462` → [CmpIsHiveLoadUnloadRundownActive](../../pagecmrc/BC/CmpIsHiveLoadUnloadRundownActive_function_00BC9FE4.md) (function, `0x00BC9FE4`)
- `0x007DB48D` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x007DB4FE` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x007DB544` → [CmpInitBackupHive](../7E/CmpInitBackupHive_function_007EC594.md) (function, `0x007EC594`)
- `0x007DB5C8` → [CmpOpenHiveFile](../87/CmpOpenHiveFile_function_0087A71C.md) (function, `0x0087A71C`)
- `0x007DB620` → [CmpOpenHiveFile](../87/CmpOpenHiveFile_function_0087A71C.md) (function, `0x0087A71C`)
- `0x007DB666` → [CmpOpenHiveFile](../87/CmpOpenHiveFile_function_0087A71C.md) (function, `0x0087A71C`)
- `0x007DB683` → [CmpGetFileSize](../9B/CmpGetFileSize_function_009B9994.md) (function, `0x009B9994`)
- `0x007DB6A3` → [CmpGetFileSize](../9B/CmpGetFileSize_function_009B9994.md) (function, `0x009B9994`)
- `0x007DB6B6` → [CmpLogFailureToGetFileSize](../9B/CmpLogFailureToGetFileSize_function_009B9F5C.md) (function, `0x009B9F5C`)
- `0x007DB6DF` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x007DB6F3` → [CmpGetFileSize](../9B/CmpGetFileSize_function_009B9994.md) (function, `0x009B9994`)
- `0x007DB706` → [CmpLogFailureToGetFileSize](../9B/CmpLogFailureToGetFileSize_function_009B9F5C.md) (function, `0x009B9F5C`)
- `0x007DB72F` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x007DB73B` → [CmpBecomeActiveFlusherAndReconciler](../7E/CmpBecomeActiveFlusherAndReconciler_function_007E7E20.md) (function, `0x007E7E20`)
- `0x007DB740` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x007DB748` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (function, `0x00BC9C50`)
- `0x007DB7CB` → [HvLockHiveWriter](../85/HvLockHiveWriter_function_00859894.md) (function, `0x00859894`)
- `0x007DB7E1` → [CmpDoFileSetSizeEx](../9B/CmpDoFileSetSizeEx_function_009B2A4C.md) (function, `0x009B2A4C`)
- `0x007DB7EB` → [HvUnlockHiveWriter](../85/HvUnlockHiveWriter_function_008598E4.md) (function, `0x008598E4`)
- `0x007DB7FE` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (function, `0x00BC9C34`)
- `0x007DB803` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DB814` → [CmpRecoverFlushProtocolStateFromFiles](../7E/CmpRecoverFlushProtocolStateFromFiles_function_007EE4B0.md) (function, `0x007EE4B0`)
- `0x007DB829` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x007DB831` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (function, `0x00BC9C50`)
- `0x007DB859` → [RtlAreBitsClear](../../text/45/RtlAreBitsClear_function_00451800.md) (function, `0x00451800`)
- `0x007DB86B` → [RtlSetBits](../../text/3E/RtlSetBits_function_003E1610.md) (function, `0x003E1610`)
- `0x007DB87D` → [RtlNumberOfSetBits](../../text/43/RtlNumberOfSetBits_function_00433F70.md) (function, `0x00433F70`)
- `0x007DB8AF` → [RtlSetAllBits](../../text/36/RtlSetAllBits_function_00362490.md) (function, `0x00362490`)
- `0x007DB8BD` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (function, `0x00BC9C34`)
- `0x007DB8C2` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DB8C7` → [CmpLockRegistryExclusive](../84/CmpLockRegistryExclusive_function_0084F9B4.md) (function, `0x0084F9B4`)
- `0x007DB8D4` → [HvLockHiveFlusherShared](../84/HvLockHiveFlusherShared_function_0084F95C.md) (function, `0x0084F95C`)
- `0x007DB8E3` → [CmpMarkCurrentValueDirty](CmpMarkCurrentValueDirty_function_007DBD1C.md) (function, `0x007DBD1C`)
- `0x007DB8EB` → [HvUnlockHiveFlusherShared](../84/HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x007DB909` → [HvpDropPagedBins](../9B/HvpDropPagedBins_function_009B7168.md) (function, `0x009B7168`)
- `0x007DB910` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DB93F` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x007DB985` → [ExRaiseHardError](../A6/ExRaiseHardError_function_00A64520.md) (function, `0x00A64520`)
- `0x007DB99E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x007DB9A7` → [CmpFinishBeingActiveFlusherAndReconciler](../7E/CmpFinishBeingActiveFlusherAndReconciler_function_007E7EB0.md) (function, `0x007E7EB0`)
- `0x007DB9C2` → [ExIsSoftBoot](../../text/4F/ExIsSoftBoot_function_004FAE60.md) (function, `0x004FAE60`)
- `0x007DB9D3` → [CmpFlushHive](../9B/CmpFlushHive_function_009B3DC0.md) (function, `0x009B3DC0`)
- `0x007DB9D8` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x007DB9E0` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (function, `0x00BC9C50`)
- `0x007DB9FD` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (function, `0x00BC9C34`)
- `0x007DBA02` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DBA10` → [CmpDiskFullWarning](../7E/CmpDiskFullWarning_function_007E59E0.md) (function, `0x007E59E0`)
- `0x007DBA48` → [RtlAppendStringToString](../A9/RtlAppendStringToString_function_00A97740.md) (function, `0x00A97740`)
- `0x007DBA6A` → [CmpInitBackupHive](../7E/CmpInitBackupHive_function_007EC594.md) (function, `0x007EC594`)
- `0x007DBA90` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x007DBA98` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (function, `0x00BC9C50`)
- `0x007DBAA7` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (function, `0x00BC9C34`)
- `0x007DBAAC` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DBAE4` → [RtlAppendStringToString](../A9/RtlAppendStringToString_function_00A97740.md) (function, `0x00A97740`)
- `0x007DBAFE` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x007DBB06` → [HvLockHiveFlusherShared](../84/HvLockHiveFlusherShared_function_0084F95C.md) (function, `0x0084F95C`)
- `0x007DBB16` → [HvUnlockHiveFlusherShared](../84/HvUnlockHiveFlusherShared_function_00848738.md) (function, `0x00848738`)
- `0x007DBB1B` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DBB29` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (function, `0x00BC9400`)
- `0x007DBB70` → [CmpApplyAdminSdOnHiveFiles](../../text/66/CmpApplyAdminSdOnHiveFiles_function_0066A168.md) (function, `0x0066A168`)
- `0x007DBB97` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x007DBB9D` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (function, `0x00BC9880`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x007DB066` → RVA `0x00E0A740` (`.data`; read)
- `0x007DB0CF` → RVA `0x00E098A0` (`.data`; read)
- `0x007DB107` → RVA `0x00FD8188` (`PAGEDATA`; read)
- `0x007DB11D` → RVA `0x00EF7C20` (`.data`; read)
- `0x007DB12B` → RVA `0x00F475F8` (`.data`; read)
- `0x007DB134` → RVA `0x00F475DC` (`.data`; read)
- `0x007DB143` → RVA `0x00EF59C0` (`.data`; read)
- `0x007DB15D` → RVA `0x00FC4958` (`.data`; read)
- `0x007DB190` → RVA `0x000DE388` (`.rdata`; read)
- `0x007DB2F0` → RVA `0x00E09948` (`.data`; read)
- `0x007DB31A` → RVA `0x00E098F8` (`.data`; read)
- `0x007DB32B` → RVA `0x00EEFB40` (`.data`; read/write)
- `0x007DB47E` → RVA `0x00FD8005` (`PAGEDATA`; write)
- `0x007DB4E2` → RVA `0x00EEFB68` (`.data`; write)
- `0x007DB4E9` → RVA `0x00E098E0` (`.data`; read)
- `0x007DB527` → RVA `0x00EEFC20` (`.data`; read)
- `0x007DB558` → RVA `0x00EEFC20` (`.data`; write)
- `0x007DB7F4` → RVA `0x00FD9A63` (`PAGEDATA`; write)
- `0x007DBA07` → RVA `0x00FD9A63` (`PAGEDATA`; read)
- `0x007DBA15` → RVA `0x00FDA8B0` (`PAGEDATA`; read)
- `0x007DBA1C` → RVA `0x00FD9ED0` (`PAGEDATA`; write)
- `0x007DBA26` → RVA `0x00FD9ED8` (`PAGEDATA`; write)
- `0x007DBA37` → RVA `0x00FD9ED0` (`PAGEDATA`; read)
- `0x007DBA7B` → RVA `0x00FD8006` (`PAGEDATA`; read)
- `0x007DBA84` → RVA `0x00EEFB5C` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **51**
  - `0x007DB0AB` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007DB0B9` → [CmpInitializeThreadInfo](../../text/3F/CmpInitializeThreadInfo_function_003FBE70.md) (`PAGE` → `.text`)
  - `0x007DB102` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x007DB126` → [KeWaitForSingleObject](../../text/20/KeWaitForSingleObject_function_0020E6B0.md) (`PAGE` → `.text`)
  - `0x007DB197` → [wil_details_FeatureReporting_ReportUsageToService](../../text/53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (`PAGE` → `.text`)
  - `0x007DB1AB` → [wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath](../../text/53/wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath_function_0053E774.md) (`PAGE` → `.text`)
  - `0x007DB1E8` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x007DB25B` → [wil_details_FeatureReporting_ReportUsageToService](../../text/53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (`PAGE` → `.text`)
  - `0x007DB26F` → [wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath](../../text/53/wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath_function_0053E774.md) (`PAGE` → `.text`)
  - `0x007DB324` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x007DB351` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x007DB376` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007DB3C3` → [wil_details_FeatureReporting_ReportUsageToService](../../text/53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (`PAGE` → `.text`)
  - `0x007DB3D7` → [wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath](../../text/53/wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath_function_0053E774.md) (`PAGE` → `.text`)
  - `0x007DB3FE` → [CmCleanupThreadInfo](../../text/41/CmCleanupThreadInfo_function_0041FD50.md) (`PAGE` → `.text`)
  - `0x007DB414` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x007DB462` → [CmpIsHiveLoadUnloadRundownActive](../../pagecmrc/BC/CmpIsHiveLoadUnloadRundownActive_function_00BC9FE4.md) (`PAGE` → `PAGECMRC`)
  - `0x007DB48D` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x007DB4FE` → [KeSetEvent](../../text/33/KeSetEvent_function_0033F310.md) (`PAGE` → `.text`)
  - `0x007DB6DF` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x007DB72F` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x007DB740` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DB748` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (`PAGE` → `PAGECMRC`)
  - `0x007DB7FE` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DB803` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DB829` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DB831` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (`PAGE` → `PAGECMRC`)
  - `0x007DB859` → [RtlAreBitsClear](../../text/45/RtlAreBitsClear_function_00451800.md) (`PAGE` → `.text`)
  - `0x007DB86B` → [RtlSetBits](../../text/3E/RtlSetBits_function_003E1610.md) (`PAGE` → `.text`)
  - `0x007DB87D` → [RtlNumberOfSetBits](../../text/43/RtlNumberOfSetBits_function_00433F70.md) (`PAGE` → `.text`)
  - `0x007DB8AF` → [RtlSetAllBits](../../text/36/RtlSetAllBits_function_00362490.md) (`PAGE` → `.text`)
  - `0x007DB8BD` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DB8C2` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DB910` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DB93F` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x007DB99E` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x007DB9C2` → [ExIsSoftBoot](../../text/4F/ExIsSoftBoot_function_004FAE60.md) (`PAGE` → `.text`)
  - `0x007DB9D8` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DB9E0` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (`PAGE` → `PAGECMRC`)
  - `0x007DB9FD` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DBA02` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DBA90` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DBA98` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (`PAGE` → `PAGECMRC`)
  - `0x007DBAA7` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DBAAC` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DBAFE` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DBB1B` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DBB29` → [CmpAcquireShutdownRundown](../../pagecmrc/BC/CmpAcquireShutdownRundown_function_00BC9400.md) (`PAGE` → `PAGECMRC`)
  - `0x007DBB70` → [CmpApplyAdminSdOnHiveFiles](../../text/66/CmpApplyAdminSdOnHiveFiles_function_0066A168.md) (`PAGE` → `.text`)
  - `0x007DBB97` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x007DBB9D` → [CmpReleaseShutdownRundown](../../pagecmrc/BC/CmpReleaseShutdownRundown_function_00BC9880.md) (`PAGE` → `PAGECMRC`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007DB040  48 8B C4                        mov rax, rsp
007DB043  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
007DB047  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
007DB04B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
007DB04F  55                              push rbp
007DB050  41 54                           push r12
007DB052  41 55                           push r13
007DB054  41 56                           push r14
007DB056  41 57                           push r15
007DB058  48 8D A8 28 FE FF FF            lea rbp, [rax - 0x1d8]
007DB05F  48 81 EC B0 02 00 00            sub rsp, 0x2b0
007DB066  48 8B 05 D3 F6 62 00            mov rax, qword ptr [rip + 0x62f6d3]
007DB06D  48 33 C4                        xor rax, rsp
007DB070  48 89 85 A0 01 00 00            mov qword ptr [rbp + 0x1a0], rax
007DB077  33 FF                           xor edi, edi
007DB079  4C 8B F1                        mov r14, rcx
007DB07C  0F 57 C0                        xorps xmm0, xmm0
007DB07F  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
007DB084  33 C0                           xor eax, eax
007DB086  89 7D 88                        mov dword ptr [rbp - 0x78], edi
007DB089  48 8D 4D F0                     lea rcx, [rbp - 0x10]
007DB08D  48 89 45 E0                     mov qword ptr [rbp - 0x20], rax
007DB091  33 D2                           xor edx, edx
007DB093  48 89 7D A8                     mov qword ptr [rbp - 0x58], rdi
007DB097  41 B8 B0 01 00 00               mov r8d, 0x1b0
007DB09D  89 7D 80                        mov dword ptr [rbp - 0x80], edi
007DB0A0  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
007DB0A4  89 7D 84                        mov dword ptr [rbp - 0x7c], edi
007DB0A7  89 7C 24 68                     mov dword ptr [rsp + 0x68], edi
007DB0AB  E8 90 BB EE FF                  call 0x1406c6c40
007DB0B0  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007DB0B4  48 89 7C 24 60                  mov qword ptr [rsp + 0x60], rdi
007DB0B9  E8 B2 0D C2 FF                  call 0x1403fbe70
007DB0BE  0F 57 C0                        xorps xmm0, xmm0
007DB0C1  45 8B E6                        mov r12d, r14d
007DB0C4  4D 69 FC B8 00 00 00            imul r15, r12, 0xb8
007DB0CB  0F 11 45 B0                     movups xmmword ptr [rbp - 0x50], xmm0
007DB0CF  48 8D 35 CA E7 62 00            lea rsi, [rip + 0x62e7ca]
007DB0D6  48 89 7C 24 78                  mov qword ptr [rsp + 0x78], rdi
007DB0DB  48 8D 4E 40                     lea rcx, [rsi + 0x40]
007DB0DF  48 89 7D 90                     mov qword ptr [rbp - 0x70], rdi
007DB0E3  49 03 CF                        add rcx, r15
007DB0E6  48 89 7D 98                     mov qword ptr [rbp - 0x68], rdi
007DB0EA  45 33 C9                        xor r9d, r9d
007DB0ED  48 89 7D A0                     mov qword ptr [rbp - 0x60], rdi
007DB0F1  45 33 C0                        xor r8d, r8d
007DB0F4  40 88 7C 24 50                  mov byte ptr [rsp + 0x50], dil
007DB0F9  33 D2                           xor edx, edx
007DB0FB  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
007DB100  8B DF                           mov ebx, edi
007DB102  E8 A9 35 A3 FF                  call 0x14020e6b0
007DB107  8B 05 7B D0 7F 00               mov eax, dword ptr [rip + 0x7fd07b]
007DB10D  44 3B F0                        cmp r14d, eax
007DB110  75 2C                           jne 0x1407db13e
007DB112  45 33 C9                        xor r9d, r9d
007DB115  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
007DB11A  45 33 C0                        xor r8d, r8d
007DB11D  48 8D 0D FC CA 71 00            lea rcx, [rip + 0x71cafc]
007DB124  33 D2                           xor edx, edx
007DB126  E8 85 35 A3 FF                  call 0x14020e6b0
007DB12B  40 38 3D C6 C4 76 00            cmp byte ptr [rip + 0x76c4c6], dil
007DB132  74 0A                           je 0x1407db13e
007DB134  40 38 3D A1 C4 76 00            cmp byte ptr [rip + 0x76c4a1], dil
007DB13B  75 01                           jne 0x1407db13e
007DB13D  CC                              int3
007DB13E  BA 01 00 00 00                  mov edx, 1
007DB143  48 8D 05 76 A8 71 00            lea rax, [rip + 0x71a876]
007DB14A  41 88 54 37 3A                  mov byte ptr [r15 + rsi + 0x3a], dl
007DB14F  49 8B 74 37 18                  mov rsi, qword ptr [r15 + rsi + 0x18]
007DB154  48 85 F6                        test rsi, rsi
007DB157  0F 85 06 04 00 00               jne 0x1407db563
007DB15D  8B 0D F5 97 7E 00               mov ecx, dword ptr [rip + 0x7e97f5]
007DB163  44 8D 6A 02                     lea r13d, [rdx + 2]
007DB167  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
007DB16C  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
007DB170  F6 C1 10                        test cl, 0x10
007DB173  75 42                           jne 0x1407db1b7
007DB175  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
007DB17A  0B CA                           or ecx, edx
007DB17C  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
007DB181  44 8B CA                        mov r9d, edx
007DB184  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
007DB188  45 8B C5                        mov r8d, r13d
007DB18B  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
007DB190  48 8D 0D F1 31 90 FF            lea rcx, [rip - 0x6fce0f]
007DB197  E8 48 35 D6 FF                  call 0x14053e6e4
007DB19C  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
007DB1A1  4C 8D 05 E0 31 90 FF            lea r8, [rip - 0x6fce20]
007DB1A8  41 8B D5                        mov edx, r13d
007DB1AB  E8 C4 35 D6 FF                  call 0x14053e774
007DB1B0  48 8D 05 09 A8 71 00            lea rax, [rip + 0x71a809]
007DB1B7  49 69 CC 40 03 00 00            imul rcx, r12, 0x340
007DB1BE  4C 8D 4D B0                     lea r9, [rbp - 0x50]
007DB1C2  48 03 C8                        add rcx, rax
007DB1C5  E8 32 DC 00 00                  call 0x1407e8dfc
007DB1CA  8B D8                           mov ebx, eax
007DB1CC  85 C0                           test eax, eax
007DB1CE  79 2D                           jns 0x1407db1fd
007DB1D0  BA 01 00 00 00                  mov edx, 1
007DB1D5  C7 44 24 20 08 00 00 00         mov dword ptr [rsp + 0x20], 8
007DB1DD  44 8B C8                        mov r9d, eax
007DB1E0  48 8D 4D F0                     lea rcx, [rbp - 0x10]
007DB1E4  44 8D 42 15                     lea r8d, [rdx + 0x15]
007DB1E8  E8 67 3D C9 FF                  call 0x14046ef54
007DB1ED  48 8D 35 AC E6 62 00            lea rsi, [rip + 0x62e6ac]
007DB1F4  48 83 C6 3B                     add rsi, 0x3b
007DB1F8  49 03 F7                        add rsi, r15
007DB1FB  EB 23                           jmp 0x1407db220
007DB1FD  8A 45 B9                        mov al, byte ptr [rbp - 0x47]
007DB200  48 8D 35 99 E6 62 00            lea rsi, [rip + 0x62e699]
007DB207  48 83 C6 3B                     add rsi, 0x3b
007DB20B  49 03 F7                        add rsi, r15
007DB20E  88 06                           mov byte ptr [rsi], al
007DB210  48 8B 45 B0                     mov rax, qword ptr [rbp - 0x50]
007DB214  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
007DB219  8A 45 B8                        mov al, byte ptr [rbp - 0x48]
007DB21C  88 44 24 50                     mov byte ptr [rsp + 0x50], al
007DB220  8B 0D 32 97 7E 00               mov ecx, dword ptr [rip + 0x7e9732]
007DB226  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
007DB22B  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
007DB22F  F6 C1 10                        test cl, 0x10
007DB232  75 40                           jne 0x1407db274
007DB234  48 8B 44 24 58                  mov rax, qword ptr [rsp + 0x58]
007DB239  45 8B C5                        mov r8d, r13d
007DB23C  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
007DB241  B8 01 00 00 00                  mov eax, 1
007DB246  0B C8                           or ecx, eax
007DB248  44 8B C8                        mov r9d, eax
007DB24B  89 4C 24 58                     mov dword ptr [rsp + 0x58], ecx
007DB24F  48 8D 0D 32 31 90 FF            lea rcx, [rip - 0x6fcece]
007DB256  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
007DB25B  E8 84 34 D6 FF                  call 0x14053e6e4
007DB260  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
007DB265  4C 8D 05 1C 31 90 FF            lea r8, [rip - 0x6fcee4]
007DB26C  41 8B D5                        mov edx, r13d
007DB26F  E8 00 35 D6 FF                  call 0x14053e774
007DB274  85 DB                           test ebx, ebx
007DB276  79 45                           jns 0x1407db2bd
007DB278  48 8D 15 21 E6 62 00            lea rdx, [rip + 0x62e621]
007DB27F  4C 8B CE                        mov r9, rsi
007DB282  48 8D 8A A8 00 00 00            lea rcx, [rdx + 0xa8]
007DB289  41 8B 54 17 20                  mov edx, dword ptr [r15 + rdx + 0x20]
007DB28E  48 8D 45 F0                     lea rax, [rbp - 0x10]
007DB292  49 03 CF                        add rcx, r15
007DB295  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
007DB29A  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
007DB29F  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007DB2A4  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
007DB2A9  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
007DB2AE  C7 44 24 20 01 00 59 01         mov dword ptr [rsp + 0x20], 0x1590001
007DB2B6  E8 19 E2 09 00                  call 0x1408794d4
007DB2BB  8B D8                           mov ebx, eax
007DB2BD  4C 8D 05 DC E5 62 00            lea r8, [rip + 0x62e5dc]
007DB2C4  BA 34 00 00 C0                  mov edx, 0xc0000034
007DB2C9  41 83 FE 06                     cmp r14d, 6
007DB2CD  0F 85 68 01 00 00               jne 0x1407db43b
007DB2D3  43 38 7C 07 3C                  cmp byte ptr [r15 + r8 + 0x3c], dil
007DB2D8  0F 85 5D 01 00 00               jne 0x1407db43b
007DB2DE  3B DA                           cmp ebx, edx
007DB2E0  74 0C                           je 0x1407db2ee
007DB2E2  81 FB 3B 00 00 C0               cmp ebx, 0xc000003b
007DB2E8  0F 85 4D 01 00 00               jne 0x1407db43b
007DB2EE  8B DF                           mov ebx, edi
007DB2F0  4C 8D 25 51 E6 62 00            lea r12, [rip + 0x62e651]
007DB2F7  41 8B C6                        mov eax, r14d
007DB2FA  BE 01 00 00 00                  mov esi, 1
007DB2FF  48 69 C8 B8 00 00 00            imul rcx, rax, 0xb8
007DB306  41 8B C6                        mov eax, r14d
007DB309  33 D2                           xor edx, edx
007DB30B  42 88 74 01 39                  mov byte ptr [rcx + r8 + 0x39], sil
007DB310  45 33 C0                        xor r8d, r8d
007DB313  48 69 C8 B8 00 00 00            imul rcx, rax, 0xb8
007DB31A  48 8D 05 D7 E5 62 00            lea rax, [rip + 0x62e5d7]
007DB321  48 03 C8                        add rcx, rax
007DB324  E8 E7 3F B6 FF                  call 0x14033f310
007DB329  8B C6                           mov eax, esi
007DB32B  F0 0F C1 05 0D 48 71 00         lock xadd dword ptr [rip + 0x71480d], eax
007DB333  03 C6                           add eax, esi
007DB335  83 F8 06                        cmp eax, 6
007DB338  75 1C                           jne 0x1407db356
007DB33A  8B 05 48 CE 7F 00               mov eax, dword ptr [rip + 0x7fce48]
007DB340  83 F8 07                        cmp eax, 7
007DB343  73 11                           jae 0x1407db356
007DB345  45 33 C0                        xor r8d, r8d
007DB348  48 8D 0D D1 C8 71 00            lea rcx, [rip + 0x71c8d1]
007DB34F  33 D2                           xor edx, edx
007DB351  E8 BA 3F B6 FF                  call 0x14033f310
007DB356  41 8B C6                        mov eax, r14d
007DB359  48 69 C8 B8 00 00 00            imul rcx, rax, 0xb8
007DB360  48 8D 05 39 E5 62 00            lea rax, [rip + 0x62e539]
007DB367  48 8B 8C 01 B0 00 00 00         mov rcx, qword ptr [rcx + rax + 0xb0]
007DB36F  48 85 C9                        test rcx, rcx
007DB372  74 19                           je 0x1407db38d
007DB374  33 D2                           xor edx, edx
007DB376  E8 F5 74 3A 00                  call 0x140b82870
007DB37B  41 8B C6                        mov eax, r14d
007DB37E  0F 57 C0                        xorps xmm0, xmm0
007DB381  48 69 C8 B8 00 00 00            imul rcx, rax, 0xb8
007DB388  42 0F 11 04 21                  movups xmmword ptr [rcx + r12], xmm0
007DB38D  8B 0D C5 95 7E 00               mov ecx, dword ptr [rip + 0x7e95c5]
007DB393  48 89 7C 24 70                  mov qword ptr [rsp + 0x70], rdi
007DB398  89 4C 24 70                     mov dword ptr [rsp + 0x70], ecx
007DB39C  F6 C1 10                        test cl, 0x10
007DB39F  75 3B                           jne 0x1407db3dc
007DB3A1  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
007DB3A6  0B CE                           or ecx, esi
007DB3A8  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
007DB3AD  4C 8B CE                        mov r9, rsi
007DB3B0  89 4C 24 60                     mov dword ptr [rsp + 0x60], ecx
007DB3B4  45 8B C5                        mov r8d, r13d
007DB3B7  48 8B 54 24 60                  mov rdx, qword ptr [rsp + 0x60]
007DB3BC  48 8D 0D C5 2F 90 FF            lea rcx, [rip - 0x6fd03b]
007DB3C3  E8 1C 33 D6 FF                  call 0x14053e6e4
007DB3C8  48 8B 4C 24 60                  mov rcx, qword ptr [rsp + 0x60]
007DB3CD  4C 8D 05 B4 2F 90 FF            lea r8, [rip - 0x6fd04c]
007DB3D4  41 8B D5                        mov edx, r13d
007DB3D7  E8 98 33 D6 FF                  call 0x14053e774
007DB3DC  41 8B C6                        mov eax, r14d
007DB3DF  BA 06 00 00 00                  mov edx, 6
007DB3E4  48 69 C8 40 03 00 00            imul rcx, rax, 0x340
007DB3EB  48 8D 05 CE A5 71 00            lea rax, [rip + 0x71a5ce]
007DB3F2  48 03 C8                        add rcx, rax
007DB3F5  E8 3E A7 01 00                  call 0x1407f5b38
007DB3FA  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007DB3FE  E8 4D 49 C4 FF                  call 0x14041fd50
007DB403  8B CB                           mov ecx, ebx
007DB405  E8 46 1A 1E 00                  call 0x1409bce50
007DB40A  48 8B 8D A0 01 00 00            mov rcx, qword ptr [rbp + 0x1a0]
007DB411  48 33 CC                        xor rcx, rsp
007DB414  E8 27 12 ED FF                  call 0x1406ac640
007DB419  4C 8D 9C 24 B0 02 00 00         lea r11, [rsp + 0x2b0]
007DB421  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
007DB425  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
007DB429  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
007DB42D  49 8B E3                        mov rsp, r11
007DB430  41 5F                           pop r15
007DB432  41 5E                           pop r14
007DB434  41 5D                           pop r13
007DB436  41 5C                           pop r12
007DB438  5D                              pop rbp
007DB439  C3                              ret
007DB43A  CC                              int3
007DB43B  43 0F BA 64 07 20 0F            bt dword ptr [r15 + r8 + 0x20], 0xf
007DB442  73 16                           jae 0x1407db45a
007DB444  49 69 C4 B8 00 00 00            imul rax, r12, 0xb8
007DB44B  42 38 7C 00 3C                  cmp byte ptr [rax + r8 + 0x3c], dil
007DB450  75 08                           jne 0x1407db45a
007DB452  3B DA                           cmp ebx, edx
007DB454  0F 84 94 FE FF FF               je 0x1407db2ee
007DB45A  81 FB 89 01 00 C0               cmp ebx, 0xc0000189
007DB460  75 31                           jne 0x1407db493
007DB462  E8 7D EB 3E 00                  call 0x140bc9fe4
007DB467  84 C0                           test al, al
007DB469  0F 85 81 FE FF FF               jne 0x1407db2f0
007DB46F  BA 02 00 00 00                  mov edx, 2
007DB474  48 63 C3                        movsxd rax, ebx
007DB477  45 8B CE                        mov r9d, r14d
007DB47A  4C 8D 45 F0                     lea r8, [rbp - 0x10]
007DB47E  C6 05 80 CB 7F 00 01            mov byte ptr [rip + 0x7fcb80], 1
007DB485  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007DB48A  8D 4A 72                        lea ecx, [rdx + 0x72]
007DB48D  E8 CE 21 D2 FF                  call 0x1404fd660
007DB492  CC                              int3
007DB493  85 DB                           test ebx, ebx
007DB495  78 D8                           js 0x1407db46f
007DB497  43 0F BA 64 07 20 0F            bt dword ptr [r15 + r8 + 0x20], 0xf
007DB49E  48 8B 74 24 78                  mov rsi, qword ptr [rsp + 0x78]
007DB4A3  72 12                           jb 0x1407db4b7
007DB4A5  48 39 BE 28 06 00 00            cmp qword ptr [rsi + 0x628], rdi
007DB4AC  74 C1                           je 0x1407db46f
007DB4AE  48 39 BE 30 06 00 00            cmp qword ptr [rsi + 0x630], rdi
007DB4B5  74 B8                           je 0x1407db46f
007DB4B7  41 8B D6                        mov edx, r14d
007DB4BA  48 69 C2 B8 00 00 00            imul rax, rdx, 0xb8
007DB4C1  42 8B 4C 00 24                  mov ecx, dword ptr [rax + r8 + 0x24]
007DB4C6  48 69 C2 B8 00 00 00            imul rax, rdx, 0xb8
007DB4CD  83 C9 04                        or ecx, 4
007DB4D0  89 8E 10 10 00 00               mov dword ptr [rsi + 0x1010], ecx
007DB4D6  4A 89 74 00 30                  mov qword ptr [rax + r8 + 0x30], rsi
007DB4DB  40 38 7C 24 50                  cmp byte ptr [rsp + 0x50], dil
007DB4E0  74 35                           je 0x1407db517
007DB4E2  C6 05 7F 46 71 00 01            mov byte ptr [rip + 0x71467f], 1
007DB4E9  4C 8D 3D F0 E3 62 00            lea r15, [rip + 0x62e3f0]
007DB4F0  41 BC 07 00 00 00               mov r12d, 7
007DB4F6  45 33 C0                        xor r8d, r8d
007DB4F9  33 D2                           xor edx, edx
007DB4FB  49 8B CF                        mov rcx, r15
007DB4FE  E8 0D 3E B6 FF                  call 0x14033f310
007DB503  49 81 C7 B8 00 00 00            add r15, 0xb8
007DB50A  49 83 EC 01                     sub r12, 1
007DB50E  75 E6                           jne 0x1407db4f6
007DB510  4C 8D 05 89 E3 62 00            lea r8, [rip + 0x62e389]
007DB517  F7 86 A0 00 00 00 01 80 00 00   test dword ptr [rsi + 0xa0], 0x8001
007DB521  0F 85 FB 05 00 00               jne 0x1407dbb22
007DB527  39 3D F3 46 71 00               cmp dword ptr [rip + 0x7146f3], edi
007DB52D  0F 84 EF 05 00 00               je 0x1407dbb22
007DB533  41 8B C6                        mov eax, r14d
007DB536  48 8B CE                        mov rcx, rsi
007DB539  48 69 D0 B8 00 00 00            imul rdx, rax, 0xb8
007DB540  4A 8B 14 02                     mov rdx, qword ptr [rdx + r8]
007DB544  E8 4B 10 01 00                  call 0x1407ec594
007DB549  4C 8D 25 F8 E3 62 00            lea r12, [rip + 0x62e3f8]
007DB550  85 C0                           test eax, eax
007DB552  0F 89 D1 05 00 00               jns 0x1407dbb29
007DB558  89 3D C2 46 71 00               mov dword ptr [rip + 0x7146c2], edi
007DB55E  E9 C6 05 00 00                  jmp 0x1407dbb29
007DB563  8B 86 A0 00 00 00               mov eax, dword ptr [rsi + 0xa0]
007DB569  41 BD 03 00 00 00               mov r13d, 3
007DB56F  48 89 74 24 78                  mov qword ptr [rsp + 0x78], rsi
007DB574  A9 01 80 00 00                  test eax, 0x8001
007DB579  0F 85 FC 04 00 00               jne 0x1407dba7b
007DB57F  48 8D 45 F0                     lea rax, [rbp - 0x10]
007DB583  33 D2                           xor edx, edx
007DB585  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
007DB58A  4C 8D 25 0F E3 62 00            lea r12, [rip + 0x62e30f]
007DB591  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
007DB596  48 8D 44 24 60                  lea rax, [rsp + 0x60]
007DB59B  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
007DB5A0  4C 8D 4C 24 68                  lea r9, [rsp + 0x68]
007DB5A5  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007DB5AA  4C 8D 45 90                     lea r8, [rbp - 0x70]
007DB5AE  49 81 C4 A8 00 00 00            add r12, 0xa8
007DB5B5  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
007DB5BA  4D 03 E7                        add r12, r15
007DB5BD  C7 44 24 20 07 00 00 00         mov dword ptr [rsp + 0x20], 7
007DB5C5  49 8B CC                        mov rcx, r12
007DB5C8  E8 4F F1 09 00                  call 0x14087a71c
007DB5CD  8B D8                           mov ebx, eax
007DB5CF  85 C0                           test eax, eax
007DB5D1  0F 88 4B 03 00 00               js 0x1407db922
007DB5D7  83 7C 24 68 02                  cmp dword ptr [rsp + 0x68], 2
007DB5DC  41 8D 45 FE                     lea eax, [r13 - 2]
007DB5E0  44 8B FF                        mov r15d, edi
007DB5E3  4C 8D 4D 80                     lea r9, [rbp - 0x80]
007DB5E7  44 0F 44 F8                     cmove r15d, eax
007DB5EB  4C 8D 45 98                     lea r8, [rbp - 0x68]
007DB5EF  48 8D 45 F0                     lea rax, [rbp - 0x10]
007DB5F3  41 C1 E7 04                     shl r15d, 4
007DB5F7  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
007DB5FC  41 8D 55 01                     lea edx, [r13 + 1]
007DB600  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
007DB605  41 83 CF 02                     or r15d, 2
007DB609  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
007DB60E  49 8B CC                        mov rcx, r12
007DB611  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
007DB616  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
007DB61B  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
007DB620  E8 F7 F0 09 00                  call 0x14087a71c
007DB625  8B D8                           mov ebx, eax
007DB627  85 C0                           test eax, eax
007DB629  48 8D 45 F0                     lea rax, [rbp - 0x10]
007DB62D  79 09                           jns 0x1407db638
007DB62F  41 8D 7D 0D                     lea edi, [r13 + 0xd]
007DB633  E9 EE 02 00 00                  jmp 0x1407db926
007DB638  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
007DB63D  4C 8D 4D 84                     lea r9, [rbp - 0x7c]
007DB641  48 89 7C 24 40                  mov qword ptr [rsp + 0x40], rdi
007DB646  4C 8D 45 A0                     lea r8, [rbp - 0x60]
007DB64A  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
007DB64F  BA 05 00 00 00                  mov edx, 5
007DB654  48 89 7C 24 30                  mov qword ptr [rsp + 0x30], rdi
007DB659  49 8B CC                        mov rcx, r12
007DB65C  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
007DB661  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
007DB666  E8 B1 F0 09 00                  call 0x14087a71c
007DB66B  8B D8                           mov ebx, eax
007DB66D  85 C0                           test eax, eax
007DB66F  79 0A                           jns 0x1407db67b
007DB671  BF 20 00 00 00                  mov edi, 0x20
007DB676  E9 A7 02 00 00                  jmp 0x1407db922
007DB67B  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
007DB67F  48 8D 55 A8                     lea rdx, [rbp - 0x58]
007DB683  E8 0C E3 1D 00                  call 0x1409b9994
007DB688  8B D8                           mov ebx, eax
007DB68A  85 C0                           test eax, eax
007DB68C  79 0A                           jns 0x1407db698
007DB68E  BF 28 00 00 00                  mov edi, 0x28
007DB693  E9 8A 02 00 00                  jmp 0x1407db922
007DB698  4C 8B 65 98                     mov r12, qword ptr [rbp - 0x68]
007DB69C  48 8D 55 C0                     lea rdx, [rbp - 0x40]
007DB6A0  49 8B CC                        mov rcx, r12
007DB6A3  E8 EC E2 1D 00                  call 0x1409b9994
007DB6A8  8B D8                           mov ebx, eax
007DB6AA  85 C0                           test eax, eax
007DB6AC  79 3A                           jns 0x1407db6e8
007DB6AE  44 8B C0                        mov r8d, eax
007DB6B1  BA 04 00 00 00                  mov edx, 4
007DB6B6  E8 A1 E8 1D 00                  call 0x1409b9f5c
007DB6BB  BA 01 00 00 00                  mov edx, 1
007DB6C0  C7 44 24 20 2B 00 00 00         mov dword ptr [rsp + 0x20], 0x2b
007DB6C8  48 8D 45 F0                     lea rax, [rbp - 0x10]
007DB6CC  44 8B CB                        mov r9d, ebx
007DB6CF  48 89 46 38                     mov qword ptr [rsi + 0x38], rax
007DB6D3  48 8D 4D F0                     lea rcx, [rbp - 0x10]
007DB6D7  48 89 75 F0                     mov qword ptr [rbp - 0x10], rsi
007DB6DB  44 8D 42 15                     lea r8d, [rdx + 0x15]
007DB6DF  E8 70 38 C9 FF                  call 0x14046ef54
007DB6E4  48 89 7D C0                     mov qword ptr [rbp - 0x40], rdi
007DB6E8  4C 8B 7D A0                     mov r15, qword ptr [rbp - 0x60]
007DB6EC  48 8D 55 C8                     lea rdx, [rbp - 0x38]
007DB6F0  49 8B CF                        mov rcx, r15
007DB6F3  E8 9C E2 1D 00                  call 0x1409b9994
007DB6F8  8B D8                           mov ebx, eax
007DB6FA  85 C0                           test eax, eax
007DB6FC  79 3A                           jns 0x1407db738
007DB6FE  44 8B C0                        mov r8d, eax
007DB701  BA 05 00 00 00                  mov edx, 5
007DB706  E8 51 E8 1D 00                  call 0x1409b9f5c
007DB70B  BA 01 00 00 00                  mov edx, 1
007DB710  C7 44 24 20 2D 00 00 00         mov dword ptr [rsp + 0x20], 0x2d
007DB718  48 8D 45 F0                     lea rax, [rbp - 0x10]
007DB71C  44 8B CB                        mov r9d, ebx
007DB71F  48 89 46 38                     mov qword ptr [rsi + 0x38], rax
007DB723  48 8D 4D F0                     lea rcx, [rbp - 0x10]
007DB727  48 89 75 F0                     mov qword ptr [rbp - 0x10], rsi
007DB72B  44 8D 42 15                     lea r8d, [rdx + 0x15]
007DB72F  E8 20 38 C9 FF                  call 0x14046ef54
007DB734  48 89 7D C8                     mov qword ptr [rbp - 0x38], rdi
007DB738  48 8B CE                        mov rcx, rsi
007DB73B  E8 E0 C6 00 00                  call 0x1407e7e20
007DB740  E8 EF E3 3E 00                  call 0x140bc9b34
007DB745  48 8B CE                        mov rcx, rsi
007DB748  E8 03 E5 3E 00                  call 0x140bc9c50
007DB74D  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
007DB751  B9 00 80 00 00                  mov ecx, 0x8000
007DB756  0F 10 45 C0                     movups xmm0, xmmword ptr [rbp - 0x40]
007DB75A  48 89 86 08 06 00 00            mov qword ptr [rsi + 0x608], rax
007DB761  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
007DB765  4C 89 A6 28 06 00 00            mov qword ptr [rsi + 0x628], r12
007DB76C  4C 89 BE 30 06 00 00            mov qword ptr [rsi + 0x630], r15
007DB773  48 89 86 08 07 00 00            mov qword ptr [rsi + 0x708], rax
007DB77A  0F 11 86 10 07 00 00            movups xmmword ptr [rsi + 0x710], xmm0
007DB781  83 A6 A0 00 00 00 FD            and dword ptr [rsi + 0xa0], 0xfffffffd
007DB788  44 8B BE 10 10 00 00            mov r15d, dword ptr [rsi + 0x1010]
007DB78F  44 23 F9                        and r15d, ecx
007DB792  41 8B C6                        mov eax, r14d
007DB795  48 69 C0 B8 00 00 00            imul rax, rax, 0xb8
007DB79C  48 8D 0D FD E0 62 00            lea rcx, [rip + 0x62e0fd]
007DB7A3  44 89 7C 24 58                  mov dword ptr [rsp + 0x58], r15d
007DB7A8  8B 44 08 24                     mov eax, dword ptr [rax + rcx + 0x24]
007DB7AC  48 8B CE                        mov rcx, rsi
007DB7AF  89 86 10 10 00 00               mov dword ptr [rsi + 0x1010], eax
007DB7B5  8B 44 24 64                     mov eax, dword ptr [rsp + 0x64]
007DB7B9  89 86 BC 00 00 00               mov dword ptr [rsi + 0xbc], eax
007DB7BF  8B 9E 18 01 00 00               mov ebx, dword ptr [rsi + 0x118]
007DB7C5  81 C3 00 10 00 00               add ebx, 0x1000
007DB7CB  E8 C4 E0 07 00                  call 0x140859894
007DB7D0  41 BC 01 00 00 00               mov r12d, 1
007DB7D6  44 8B C3                        mov r8d, ebx
007DB7D9  45 8B CC                        mov r9d, r12d
007DB7DC  33 D2                           xor edx, edx
007DB7DE  48 8B CE                        mov rcx, rsi
007DB7E1  E8 66 72 1D 00                  call 0x1409b2a4c
007DB7E6  48 8B CE                        mov rcx, rsi
007DB7E9  8B D8                           mov ebx, eax
007DB7EB  E8 F4 E0 07 00                  call 0x1408598e4
007DB7F0  85 DB                           test ebx, ebx
007DB7F2  79 07                           jns 0x1407db7fb
007DB7F4  44 88 25 68 E2 7F 00            mov byte ptr [rip + 0x7fe268], r12b
007DB7FB  48 8B CE                        mov rcx, rsi
007DB7FE  E8 31 E4 3E 00                  call 0x140bc9c34
007DB803  E8 7C E2 3E 00                  call 0x140bc9a84
007DB808  45 85 FF                        test r15d, r15d
007DB80B  74 1C                           je 0x1407db829
007DB80D  48 8D 55 F0                     lea rdx, [rbp - 0x10]
007DB811  48 8B CE                        mov rcx, rsi
007DB814  E8 97 2C 01 00                  call 0x1407ee4b0
007DB819  8B D8                           mov ebx, eax
007DB81B  85 C0                           test eax, eax
007DB81D  79 0A                           jns 0x1407db829
007DB81F  BF 48 00 00 00                  mov edi, 0x48
007DB824  E9 F9 00 00 00                  jmp 0x1407db922
007DB829  E8 06 E3 3E 00                  call 0x140bc9b34
007DB82E  48 8B CE                        mov rcx, rsi
007DB831  E8 1A E4 3E 00                  call 0x140bc9c50
007DB836  48 8B 5C 24 60                  mov rbx, qword ptr [rsp + 0x60]
007DB83B  39 9E 88 00 00 00               cmp dword ptr [rsi + 0x88], ebx
007DB841  74 4D                           je 0x1407db890
007DB843  4C 8D 66 58                     lea r12, [rsi + 0x58]
007DB847  44 8B FF                        mov r15d, edi
007DB84A  41 39 3C 24                     cmp dword ptr [r12], edi
007DB84E  76 29                           jbe 0x1407db879
007DB850  44 8B C3                        mov r8d, ebx
007DB853  41 8B D7                        mov edx, r15d
007DB856  49 8B CC                        mov rcx, r12
007DB859  E8 A2 5F C7 FF                  call 0x140451800
007DB85E  84 C0                           test al, al
007DB860  75 0E                           jne 0x1407db870
007DB862  44 8B C3                        mov r8d, ebx
007DB865  41 8B D7                        mov edx, r15d
007DB868  49 8B CC                        mov rcx, r12
007DB86B  E8 A0 5D C0 FF                  call 0x1403e1610
007DB870  44 03 FB                        add r15d, ebx
007DB873  45 3B 3C 24                     cmp r15d, dword ptr [r12]
007DB877  72 D7                           jb 0x1407db850
007DB879  48 8D 4E 58                     lea rcx, [rsi + 0x58]
007DB87D  E8 EE 86 C5 FF                  call 0x140433f70
007DB882  44 8B 7C 24 58                  mov r15d, dword ptr [rsp + 0x58]
007DB887  89 46 68                        mov dword ptr [rsi + 0x68], eax
007DB88A  89 9E 88 00 00 00               mov dword ptr [rsi + 0x88], ebx
007DB890  48 8B 46 40                     mov rax, qword ptr [rsi + 0x40]
007DB894  39 B8 FC 0F 00 00               cmp dword ptr [rax + 0xffc], edi
007DB89A  75 0F                           jne 0x1407db8ab
007DB89C  8B 80 F8 0F 00 00               mov eax, dword ptr [rax + 0xff8]
007DB8A2  A8 04                           test al, 4
007DB8A4  75 05                           jne 0x1407db8ab
007DB8A6  45 85 FF                        test r15d, r15d
007DB8A9  74 0F                           je 0x1407db8ba
007DB8AB  48 8D 4E 58                     lea rcx, [rsi + 0x58]
007DB8AF  E8 DC 6B B8 FF                  call 0x140362490
007DB8B4  8B 46 58                        mov eax, dword ptr [rsi + 0x58]
007DB8B7  89 46 68                        mov dword ptr [rsi + 0x68], eax
007DB8BA  48 8B CE                        mov rcx, rsi
007DB8BD  E8 72 E3 3E 00                  call 0x140bc9c34
007DB8C2  E8 BD E1 3E 00                  call 0x140bc9a84
007DB8C7  E8 E8 40 07 00                  call 0x14084f9b4
007DB8CC  45 3B F5                        cmp r14d, r13d
007DB8CF  75 1F                           jne 0x1407db8f0
007DB8D1  48 8B CE                        mov rcx, rsi
007DB8D4  E8 83 40 07 00                  call 0x14084f95c
007DB8D9  48 8B 56 40                     mov rdx, qword ptr [rsi + 0x40]
007DB8DD  48 8B CE                        mov rcx, rsi
007DB8E0  8B 52 24                        mov edx, dword ptr [rdx + 0x24]
007DB8E3  E8 34 04 00 00                  call 0x1407dbd1c
007DB8E8  48 8B CE                        mov rcx, rsi
007DB8EB  E8 48 CE 06 00                  call 0x140848738
007DB8F0  41 8B C6                        mov eax, r14d
007DB8F3  4C 8D 3D A6 DF 62 00            lea r15, [rip + 0x62dfa6]
007DB8FA  48 69 C8 B8 00 00 00            imul rcx, rax, 0xb8
007DB901  4A 89 74 39 30                  mov qword ptr [rcx + r15 + 0x30], rsi
007DB906  48 8B CE                        mov rcx, rsi
007DB909  E8 5A B8 1D 00                  call 0x1409b7168
007DB90E  8B D8                           mov ebx, eax
007DB910  E8 6F E1 3E 00                  call 0x140bc9a84
007DB915  85 DB                           test ebx, ebx
007DB917  0F 89 87 00 00 00               jns 0x1407db9a4
007DB91D  BF 50 00 00 00                  mov edi, 0x50
007DB922  48 8D 45 F0                     lea rax, [rbp - 0x10]
007DB926  48 89 46 38                     mov qword ptr [rsi + 0x38], rax
007DB92A  48 89 75 F0                     mov qword ptr [rbp - 0x10], rsi
007DB92E  33 D2                           xor edx, edx
007DB930  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
007DB934  44 8B CB                        mov r9d, ebx
007DB937  48 8D 4D F0                     lea rcx, [rbp - 0x10]
007DB93B  44 8D 42 16                     lea r8d, [rdx + 0x16]
007DB93F  E8 10 36 C9 FF                  call 0x14046ef54
007DB944  BF 01 00 00 00                  mov edi, 1
007DB949  41 8B C6                        mov eax, r14d
007DB94C  48 69 C8 B8 00 00 00            imul rcx, rax, 0xb8
007DB953  48 8D 05 EE DF 62 00            lea rax, [rip + 0x62dfee]
007DB95A  40 88 3D A4 C6 7F 00            mov byte ptr [rip + 0x7fc6a4], dil
007DB961  48 03 C8                        add rcx, rax
007DB964  4C 8D 4C 24 70                  lea r9, [rsp + 0x70]
007DB969  48 8D 45 88                     lea rax, [rbp - 0x78]
007DB96D  48 89 4C 24 70                  mov qword ptr [rsp + 0x70], rcx
007DB972  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007DB977  B9 18 02 00 C0                  mov ecx, 0xc0000218
007DB97C  44 8B C7                        mov r8d, edi
007DB97F  89 7C 24 20                     mov dword ptr [rsp + 0x20], edi
007DB983  8B D7                           mov edx, edi
007DB985  E8 96 8B 28 00                  call 0x140a64520
007DB98A  48 63 C3                        movsxd rax, ebx
007DB98D  8D 57 01                        lea edx, [rdi + 1]
007DB990  45 8B CE                        mov r9d, r14d
007DB993  8D 4F 73                        lea ecx, [rdi + 0x73]
007DB996  44 8B C7                        mov r8d, edi
007DB999  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007DB99E  E8 BD 1C D2 FF                  call 0x1404fd660
007DB9A3  CC                              int3
007DB9A4  48 8B CE                        mov rcx, rsi
007DB9A7  E8 04 C5 00 00                  call 0x1407e7eb0
007DB9AC  48 8B 46 40                     mov rax, qword ptr [rsi + 0x40]
007DB9B0  39 B8 FC 0F 00 00               cmp dword ptr [rax + 0xffc], edi
007DB9B6  75 0A                           jne 0x1407db9c2
007DB9B8  8B 80 F8 0F 00 00               mov eax, dword ptr [rax + 0xff8]
007DB9BE  A8 04                           test al, 4
007DB9C0  74 45                           je 0x1407dba07
007DB9C2  E8 99 F4 D1 FF                  call 0x1404fae60
007DB9C7  84 C0                           test al, al
007DB9C9  75 0D                           jne 0x1407db9d8
007DB9CB  BA 0C 00 00 00                  mov edx, 0xc
007DB9D0  48 8B CE                        mov rcx, rsi
007DB9D3  E8 E8 83 1D 00                  call 0x1409b3dc0
007DB9D8  E8 57 E1 3E 00                  call 0x140bc9b34
007DB9DD  48 8B CE                        mov rcx, rsi
007DB9E0  E8 6B E2 3E 00                  call 0x140bc9c50
007DB9E5  48 8B 46 40                     mov rax, qword ptr [rsi + 0x40]
007DB9E9  48 8B CE                        mov rcx, rsi
007DB9EC  89 B8 FC 0F 00 00               mov dword ptr [rax + 0xffc], edi
007DB9F2  48 8B 46 40                     mov rax, qword ptr [rsi + 0x40]
007DB9F6  83 A0 F8 0F 00 00 FB            and dword ptr [rax + 0xff8], 0xfffffffb
007DB9FD  E8 32 E2 3E 00                  call 0x140bc9c34
007DBA02  E8 7D E0 3E 00                  call 0x140bc9a84
007DBA07  40 38 3D 55 E0 7F 00            cmp byte ptr [rip + 0x7fe055], dil
007DBA0E  74 05                           je 0x1407dba15
007DBA10  E8 CB 9F 00 00                  call 0x1407e59e0
007DBA15  48 8D 05 94 EE 7F 00            lea rax, [rip + 0x7fee94]
007DBA1C  C7 05 AA E4 7F 00 00 00 80 00   mov dword ptr [rip + 0x7fe4aa], 0x800000
007DBA26  48 89 05 AB E4 7F 00            mov qword ptr [rip + 0x7fe4ab], rax
007DBA2D  4C 8D 25 14 DF 62 00            lea r12, [rip + 0x62df14]
007DBA34  41 8B C6                        mov eax, r14d
007DBA37  48 8D 0D 92 E4 7F 00            lea rcx, [rip + 0x7fe492]
007DBA3E  48 69 D0 B8 00 00 00            imul rdx, rax, 0xb8
007DBA45  49 03 D4                        add rdx, r12
007DBA48  E8 F3 BC 2B 00                  call 0x140a97740
007DBA4D  39 3D CD 41 71 00               cmp dword ptr [rip + 0x7141cd], edi
007DBA53  0F 84 99 00 00 00               je 0x1407dbaf2
007DBA59  41 8B C6                        mov eax, r14d
007DBA5C  48 8B CE                        mov rcx, rsi
007DBA5F  48 69 D0 B8 00 00 00            imul rdx, rax, 0xb8
007DBA66  4A 8B 14 3A                     mov rdx, qword ptr [rdx + r15]
007DBA6A  E8 25 0B 01 00                  call 0x1407ec594
007DBA6F  85 C0                           test eax, eax
007DBA71  79 7F                           jns 0x1407dbaf2
007DBA73  89 3D A7 41 71 00               mov dword ptr [rip + 0x7141a7], edi
007DBA79  EB 77                           jmp 0x1407dbaf2
007DBA7B  40 38 3D 84 C5 7F 00            cmp byte ptr [rip + 0x7fc584], dil
007DBA82  75 08                           jne 0x1407dba8c
007DBA84  39 3D D2 40 71 00               cmp dword ptr [rip + 0x7140d2], edi
007DBA8A  74 5F                           je 0x1407dbaeb
007DBA8C  A8 02                           test al, 2
007DBA8E  74 21                           je 0x1407dbab1
007DBA90  E8 9F E0 3E 00                  call 0x140bc9b34
007DBA95  48 8B CE                        mov rcx, rsi
007DBA98  E8 B3 E1 3E 00                  call 0x140bc9c50
007DBA9D  83 A6 A0 00 00 00 FD            and dword ptr [rsi + 0xa0], 0xfffffffd
007DBAA4  48 8B CE                        mov rcx, rsi
007DBAA7  E8 88 E1 3E 00                  call 0x140bc9c34
007DBAAC  E8 D3 DF 3E 00                  call 0x140bc9a84
007DBAB1  48 8D 05 F8 ED 7F 00            lea rax, [rip + 0x7fedf8]
007DBAB8  C7 05 0E E4 7F 00 00 00 80 00   mov dword ptr [rip + 0x7fe40e], 0x800000
007DBAC2  48 89 05 0F E4 7F 00            mov qword ptr [rip + 0x7fe40f], rax
007DBAC9  4C 8D 25 78 DE 62 00            lea r12, [rip + 0x62de78]
007DBAD0  41 8B C6                        mov eax, r14d
007DBAD3  48 8D 0D F6 E3 7F 00            lea rcx, [rip + 0x7fe3f6]
007DBADA  48 69 D0 B8 00 00 00            imul rdx, rax, 0xb8
007DBAE1  49 03 D4                        add rdx, r12
007DBAE4  E8 57 BC 2B 00                  call 0x140a97740
007DBAE9  EB 07                           jmp 0x1407dbaf2
007DBAEB  4C 8D 25 56 DE 62 00            lea r12, [rip + 0x62de56]
007DBAF2  83 8E 10 10 00 00 04            or dword ptr [rsi + 0x1010], 4
007DBAF9  45 3B F5                        cmp r14d, r13d
007DBAFC  75 2B                           jne 0x1407dbb29
007DBAFE  E8 31 E0 3E 00                  call 0x140bc9b34
007DBB03  48 8B CE                        mov rcx, rsi
007DBB06  E8 51 3E 07 00                  call 0x14084f95c
007DBB0B  0F BA AE A0 00 00 00 09         bts dword ptr [rsi + 0xa0], 9
007DBB13  48 8B CE                        mov rcx, rsi
007DBB16  E8 1D CC 06 00                  call 0x140848738
007DBB1B  E8 64 DF 3E 00                  call 0x140bc9a84
007DBB20  EB 07                           jmp 0x1407dbb29
007DBB22  4C 8D 25 1F DE 62 00            lea r12, [rip + 0x62de1f]
007DBB29  E8 D2 D8 3E 00                  call 0x140bc9400
007DBB2E  84 C0                           test al, al
007DBB30  75 11                           jne 0x1407dbb43
007DBB32  BB 89 01 00 C0                  mov ebx, 0xc0000189
007DBB37  4C 8D 05 62 DD 62 00            lea r8, [rip + 0x62dd62]
007DBB3E  E9 B4 F7 FF FF                  jmp 0x1407db2f7
007DBB43  F7 86 A0 00 00 00 01 80 00 00   test dword ptr [rsi + 0xa0], 0x8001
007DBB4D  75 4E                           jne 0x1407dbb9d
007DBB4F  48 39 BE 08 06 00 00            cmp qword ptr [rsi + 0x608], rdi
007DBB56  74 45                           je 0x1407dbb9d
007DBB58  41 8B C6                        mov eax, r14d
007DBB5B  48 8B CE                        mov rcx, rsi
007DBB5E  4C 69 F8 B8 00 00 00            imul r15, rax, 0xb8
007DBB65  48 8D 05 34 DD 62 00            lea rax, [rip + 0x62dd34]
007DBB6C  49 8B 14 07                     mov rdx, qword ptr [r15 + rax]
007DBB70  E8 F3 E5 E8 FF                  call 0x14066a168
007DBB75  48 63 D8                        movsxd rbx, eax
007DBB78  85 C0                           test eax, eax
007DBB7A  79 21                           jns 0x1407dbb9d
007DBB7C  BA 13 00 00 00                  mov edx, 0x13
007DBB81  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
007DBB86  48 8D 05 13 DD 62 00            lea rax, [rip + 0x62dd13]
007DBB8D  4C 8B C6                        mov r8, rsi
007DBB90  4D 8B 0C 07                     mov r9, qword ptr [r15 + rax]
007DBB94  8D 4A 3E                        lea ecx, [rdx + 0x3e]
007DBB97  E8 C4 1A D2 FF                  call 0x1404fd660
007DBB9C  CC                              int3
007DBB9D  E8 DE DC 3E 00                  call 0x140bc9880
007DBBA2  EB 93                           jmp 0x1407dbb37
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpLoadHiveThread(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m238;
    unsigned __int64 v_stack_m240;
    unsigned __int64 v_stack_m248;
    unsigned int v_stack_m24C;
    unsigned __int64 v_stack_m250;
    unsigned int v_stack_m258;
    unsigned __int64 v_stack_m260;
    unsigned __int64 v_stack_m268;
    unsigned int v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m280;
    unsigned __int8 v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2B0;
    unsigned __int64 v_stack_m2B8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (688);
    result = (*(unsigned __int64 *)(v_rip + 6485715)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 472 + 416) = result;
    v_rdi = 0;
    v_stack_m268 = 0;
    result = 0;
    *(unsigned int *)(v_rsp - 472 - 120) = 0;
    *(unsigned __int64 *)(v_rsp - 472 - 32) = 0;
    a2 = 0;
    *(unsigned __int64 *)(v_rsp - 472 - 88) = 0;
    *(unsigned int *)(v_rsp - 472 - 128) = 0;
    *(unsigned __int64 *)(v_rsp - 472 - 48) = v_xmm0;
    *(unsigned int *)(v_rsp - 472 - 124) = 0;
    v_stack_m270 = 0;
    result = memset(v_rsp - 472 - 16, a2, 432, a4);
    v_stack_m278 = 0;
    result = CmpInitializeThreadInfo(v_rsp - 472 - 48, a2, 432, a4);
    v_r15 = (v_r15) * ((unsigned int)((unsigned int)(a1)));
    *(unsigned __int64 *)(v_rsp - 472 - 80) = v_xmm0;
    v_stack_m260 = 0;
    *(unsigned __int64 *)(v_rsp - 472 - 112) = 0;
    a1 = (v_rip + 6481866 + 64) + (v_r15);
    *(unsigned __int64 *)(v_rsp - 472 - 104) = 0;
    a4 = 0;
    *(unsigned __int64 *)(v_rsp - 472 - 96) = 0;
    a3 = 0;
    v_stack_m288 = 0;
    a2 = 0;
    v_stack_m2B8 = 0;
    result = KeWaitForSingleObject(a1, a2, a3, a4);
    if (((unsigned int)(a1)) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8376443))))) goto loc_007DB13E;
    a4 = 0;
    v_stack_m2B8 = 0;
    a3 = 0;
    a2 = 0;
    result = KeWaitForSingleObject(v_rip + 7457532, a2, a3, a4);
    if ((*(unsigned __int8 *)(v_rip + 7783622)) == 0) goto loc_007DB13E;
    if ((*(unsigned __int8 *)(v_rip + 7783585)) == 0) {
    }
    *(unsigned __int8 *)(v_r15 + v_rip + 6481866 * 1 + 58) = 1;
    if (*(unsigned __int64 *)(v_r15 + v_rip + 6481866 * 1 + 24) != 0) goto loc_007DB563;
    v_stack_m280 = 0;
    v_stack_m280 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8296437)));
    result = v_rip + 7448694;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 8296437)))) & (16)) == 0) {
        result = v_stack_m280;
        a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 8296437))) | (1));
        v_stack_m280 = result;
        a4 = 1;
        v_stack_m280 = (unsigned int)(a1);
        a3 = (unsigned int)(1 + 2);
        a2 = v_stack_m280;
        a1 = v_rip - 7327247;
        result = wil_details_FeatureReporting_ReportUsageToService(a1, a2, a3, a4);
        a1 = v_stack_m280;
        a3 = v_rip - 7327264;
        a2 = (unsigned int)(1 + 2);
        result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(a1, a2, a3, a4);
        result = v_rip + 7448585;
    }
    a1 = (a1) * ((unsigned int)((unsigned int)(a1)));
    a1 = (a1) + (result);
    result = CmpMachineHiveCacheClaimEntry(a1, a2, a3, v_rsp - 472 - 80);
    if (!sign_flag) goto loc_007DB1FD;
    v_stack_m2B8 = 8;
    result = SetFailureLocation(v_rsp - 472 - 16, 1, 1 + 21, (unsigned int)((unsigned int)(result)));
    v_rsi = (v_rip + 6481580) + (59);
    v_rsi = (v_rsi) + (v_r15);
    goto loc_007DB220;
loc_007DB1FD:
    v_rsi = (v_rip + 6481561) + (59);
    v_rsi = (v_rsi) + (v_r15);
    *(unsigned __int8 *)(v_rsi) = (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 472 - 71));
    v_stack_m260 = *(unsigned __int64 *)(v_rsp - 472 - 80);
    v_stack_m288 = (unsigned __int8)(*(unsigned __int8 *)(v_rsp - 472 - 72));
loc_007DB220:
    v_stack_m280 = 0;
    v_stack_m280 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8296242)));
    result = *(unsigned __int8 *)(v_rsp - 472 - 72);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 8296242)))) & (16)) == 0) {
        result = v_stack_m280;
        a3 = (unsigned int)(1 + 2);
        v_stack_m280 = result;
        result = 1;
        a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 8296242))) | ((unsigned int)(result)));
        a4 = (unsigned int)(result);
        v_stack_m280 = (unsigned int)(a1);
        a1 = v_rip - 7327438;
        a2 = v_stack_m280;
        result = wil_details_FeatureReporting_ReportUsageToService(a1, a2, a3, a4);
        a1 = v_stack_m280;
        a3 = v_rip - 7327460;
        a2 = (unsigned int)(1 + 2);
        result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(a1, a2, a3, a4);
    }
    v_rbx = (unsigned int)((unsigned int)(result));
    if (sign_flag) {
        a2 = v_rip + 6481441;
        a4 = v_rsi;
        a1 = a2 + 168;
        a2 = *(unsigned int *)(v_r15 + a2 * 1 + 32);
        result = v_rsp - 472 - 16;
        a1 = (a1) + (v_r15);
        v_stack_m290 = result;
        a3 = v_stack_m260;
        result = v_stack_m288;
        v_stack_m298 = result;
        v_stack_m2B0 = 0;
        v_stack_m2B8 = 0x1590001ULL;
        result = CmpInitHiveFromFile(a1, a2, a3, a4);
        v_rbx = (unsigned int)(result);
    }
    if (((unsigned int)(a1)) != 6) goto loc_007DB43B;
    if ((*(unsigned __int8 *)(v_r15 + v_rip + 6481372 * 1 + 60)) != 0) goto loc_007DB43B;
    if (((unsigned int)(v_rbx)) == ((unsigned int)((unsigned int)(0xC0000034ULL)))) goto loc_007DB2EE;
    if (((unsigned int)(v_rbx)) != 0xC000003BULL) goto loc_007DB43B;
loc_007DB2EE:
loc_007DB2F0:
loc_007DB2F7:
    a1 = (a1) * ((unsigned int)((unsigned int)(a1)));
    a2 = 0;
    *(unsigned __int8 *)(a1 + v_rip + 6481372 * 1 + 57) = 1;
    a3 = 0;
    a1 = (a1) * ((unsigned int)((unsigned int)(a1)));
    a1 = (a1) + (v_rip + 6481367);
    result = KeSetEvent(a1, a2, a3, a4);
    result = (unsigned int)((1) + (1));
    if (((unsigned int)(result)) != 6) goto loc_007DB356;
    result = (unsigned int)(*(unsigned int *)(v_rip + 8375880));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8375880)))) < 7) {
        a3 = 0;
        a1 = v_rip + 7456977;
        a2 = 0;
        result = KeSetEvent(a1, a2, a3, a4);
    }
    a1 = (a1) * ((unsigned int)((unsigned int)(a1)));
    result = v_rip + 6481209;
    if (*(unsigned __int64 *)(a1 + v_rip + 6481209 * 1 + 176) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + v_rip + 6481209 * 1 + 176), a2, a3, a4);
        result = (unsigned int)(a1);
        a1 = (*(unsigned __int64 *)(a1 + v_rip + 6481209 * 1 + 176)) * (result);
        *(unsigned __int64 *)(a1 + v_rip + 6481489 * 1) = v_xmm0;
    }
    v_stack_m268 = 0;
    v_stack_m268 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 8295877)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 8295877)))) & (16)) == 0) {
        result = v_stack_m268;
        a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 8295877))) | (1));
        v_stack_m278 = result;
        a4 = 1;
        v_stack_m278 = (unsigned int)(a1);
        a3 = (unsigned int)(1 + 2);
        a2 = v_stack_m278;
        a1 = v_rip - 7327803;
        result = wil_details_FeatureReporting_ReportUsageToService(a1, a2, a3, a4);
        a1 = v_stack_m278;
        a3 = v_rip - 7327820;
        a2 = (unsigned int)(1 + 2);
        result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(a1, a2, a3, a4);
    }
    a1 = (a1) * ((unsigned int)((unsigned int)(a1)));
    a1 = (a1) + (v_rip + 7448014);
    result = CmpHiveCacheEntryCleanup(a1, 6, a3, a4);
    result = CmCleanupThreadInfo(v_rsp - 472 - 48, 6, a3, a4);
    result = PsTerminateSystemThread(0, 6, a3, a4);
    a1 = (*(unsigned __int64 *)(v_rsp - 472 + 416)) ^ (v_rsp);
    result = _security_check_cookie(a1, 6, a3, a4);
    return result;
loc_007DB43B:
    if (condition_is_above_or_equal) goto loc_007DB45A;
    result = (result) * (v_rip + 6481489);
    if ((*(unsigned __int8 *)(result + a3 * 1 + 60)) != ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 72)))) goto loc_007DB45A;
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56))) == 6) goto loc_007DB2EE;
loc_007DB45A:
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56))) != 0xC0000189ULL) goto loc_007DB493;
    result = CmpIsHiveLoadUnloadRundownActive(a1, 6, a3, a4);
    if ((unsigned __int8)(result) != 0) goto loc_007DB2F0;
loc_007DB46F:
    *(unsigned __int8 *)(v_rip + 8375168) = 1;
    v_stack_m290 = (int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56)));
    result = KeBugCheckEx(2 + 114, 2, v_rsp - 472 - 16, (unsigned int)((unsigned int)(a1)));
loc_007DB493:
    if (sign_flag) goto loc_007DB46F;
    if (condition_is_below) goto loc_007DB4B7;
    if ((*(unsigned __int64 *)(v_stack_m238 + 1576)) == (*(unsigned __int64 *)(v_stack_m28 + 72))) goto loc_007DB46F;
    if ((*(unsigned __int64 *)(v_stack_m238 + 1584)) == (*(unsigned __int64 *)(v_stack_m28 + 72))) goto loc_007DB46F;
loc_007DB4B7:
    result = (result) * ((unsigned int)((unsigned int)(a1)));
    result = (result) * ((unsigned int)((unsigned int)(a1)));
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + v_rsp - 472 - 16 * 1 + 36))) | (4));
    *(unsigned int *)(v_stack_m238 + 4112) = (unsigned int)(a1);
    *(unsigned __int64 *)(result + v_rsp - 472 - 16 * 1 + 48) = v_stack_m238;
    if (v_stack_m260 == ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 72)))) goto loc_007DB517;
    *(unsigned __int8 *)(v_rip + 7423615) = 1;
loc_007DB4F6:
    a3 = 0;
    a2 = 0;
    result = KeSetEvent(v_rip + 6480880, a2, a3, (unsigned int)((unsigned int)(a1)));
    v_r15 = (v_rip + 6480880) + (184);
    v_r12 = (7) - (1);
    if (condition_is_not_equal) goto loc_007DB4F6;
loc_007DB517:
    if (((*(unsigned int *)(v_stack_m238 + 160)) & (0x8001ULL)) != 0) goto loc_007DBB22;
    if ((*(unsigned int *)(v_rip + 7423731)) == ((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72)))) goto loc_007DBB22;
    a2 = (a2) * ((unsigned int)((unsigned int)(a1)));
    result = CmpInitBackupHive(v_stack_m238, *(unsigned __int64 *)(a2 + v_rip + 6480777 * 1), v_rip + 6480777, (unsigned int)((unsigned int)(a1)));
    if (!sign_flag) goto loc_007DBB29;
    *(unsigned int *)(v_rip + 7423682) = (unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72));
    goto loc_007DBB29;
loc_007DB563:
    v_stack_m238 = v_stack_m238;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m238 + 160)))) & (0x8001ULL)) != 0) goto loc_007DBA7B;
    a2 = 0;
    v_stack_m268 = v_rsp - 472 - 16;
    v_stack_m270 = *(unsigned __int64 *)(v_stack_m28 + 72);
    v_stack_m278 = *(unsigned __int64 *)(v_stack_m28 + 72);
    v_stack_m280 = v_stack_m250;
    v_r12 = (v_rip + 6480655) + (168);
    v_stack_m288 = *(unsigned __int64 *)(v_stack_m28 + 72);
    v_r12 = (v_r12) + (v_r15);
    v_stack_m290 = 7;
    result = CmpOpenHiveFile(v_r12, a2, v_rsp - 472 - 112, v_stack_m248);
    if (sign_flag) goto loc_007DB922;
    v_r15 = (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 72)));
    if (v_stack_m248 == 2) { v_r15 = (unsigned int)(3 - 2); }
    v_r15 = (unsigned int)((v_r15) << (4));
    v_stack_m268 = v_rsp - 472 - 16;
    v_stack_m270 = *(unsigned __int64 *)(v_stack_m28 + 72);
    v_r15 = (unsigned int)((v_r15) | (2));
    v_stack_m278 = *(unsigned __int64 *)(v_stack_m28 + 72);
    v_stack_m280 = *(unsigned __int64 *)(v_stack_m28 + 72);
    v_stack_m288 = *(unsigned __int64 *)(v_stack_m28 + 72);
    v_stack_m290 = (unsigned int)(v_r15);
    result = CmpOpenHiveFile(v_r12, 3 + 1, v_rsp - 472 - 104, v_rsp - 472 - 128);
    if (!sign_flag) goto loc_007DB638;
    goto loc_007DB926;
loc_007DB638:
    v_stack_m268 = v_rsp - 472 - 16;
    v_stack_m270 = 3 + 13;
    v_stack_m278 = 3 + 13;
    v_stack_m280 = 3 + 13;
    v_stack_m288 = 3 + 13;
    v_stack_m290 = (unsigned int)(v_r15);
    result = CmpOpenHiveFile(v_r12, 5, v_rsp - 472 - 96, v_rsp - 472 - 124);
    if (!sign_flag) goto loc_007DB67B;
    goto loc_007DB922;
loc_007DB67B:
    result = CmpGetFileSize(*(unsigned __int64 *)(v_rsp - 472 - 112), v_rsp - 472 - 88, v_rsp - 472 - 96, v_rsp - 472 - 124);
    if (!sign_flag) goto loc_007DB698;
    goto loc_007DB922;
loc_007DB698:
    result = CmpGetFileSize(*(unsigned __int64 *)(v_rsp - 472 - 104), v_rsp - 472 - 64, v_rsp - 472 - 96, v_rsp - 472 - 124);
    if (sign_flag) {
        a3 = (unsigned int)(result);
        a2 = 4;
        result = CmpLogFailureToGetFileSize(*(unsigned __int64 *)(v_rsp - 472 - 104), a2, a3, v_rsp - 472 - 124);
        a2 = 1;
        v_stack_m290 = 43;
        result = v_rsp - 472 - 16;
        a4 = (unsigned int)((unsigned int)((unsigned int)(result)));
        *(unsigned __int64 *)(v_stack_m238 + 56) = result;
        a1 = v_rsp - 472 - 16;
        *(unsigned __int64 *)(v_rsp - 472 - 16) = v_stack_m238;
        a3 = a2 + 21;
        result = SetFailureLocation(a1, a2, a3, a4);
        *(unsigned __int64 *)(v_rsp - 472 - 64) = 40;
    }
    result = CmpGetFileSize(*(unsigned __int64 *)(v_rsp - 472 - 96), v_rsp - 472 - 56, a3, a4);
    if (sign_flag) {
        a3 = (unsigned int)(result);
        a2 = 5;
        result = CmpLogFailureToGetFileSize(*(unsigned __int64 *)(v_rsp - 472 - 96), a2, a3, a4);
        a2 = 1;
        v_stack_m290 = 45;
        result = v_rsp - 472 - 16;
        a4 = (unsigned int)((unsigned int)((unsigned int)(result)));
        *(unsigned __int64 *)(v_stack_m238 + 56) = result;
        a1 = v_rsp - 472 - 16;
        *(unsigned __int64 *)(v_rsp - 472 - 16) = v_stack_m238;
        a3 = a2 + 21;
        result = SetFailureLocation(a1, a2, a3, a4);
        *(unsigned __int64 *)(v_rsp - 472 - 56) = 40;
    }
    result = CmpBecomeActiveFlusherAndReconciler(v_stack_m238, a2, a3, a4);
    result = CmpLockRegistry(v_stack_m238, a2, a3, a4);
    result = HvLockHiveFlusherExclusive(v_stack_m238, a2, a3, a4);
    *(unsigned __int64 *)(v_stack_m238 + 1544) = *(unsigned __int64 *)(v_rsp - 472 - 112);
    *(unsigned __int64 *)(v_stack_m238 + 1576) = *(unsigned __int64 *)(v_rsp - 472 - 104);
    *(unsigned __int64 *)(v_stack_m238 + 1584) = *(unsigned __int64 *)(v_rsp - 472 - 96);
    *(unsigned __int64 *)(v_stack_m238 + 1800) = *(unsigned __int64 *)(v_rsp - 472 - 88);
    *(unsigned __int64 *)(v_stack_m238 + 1808) = v_xmm0;
    v_r15 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m238 + 4112))) & ((unsigned int)((unsigned int)(0x8000ULL))));
    result = ((unsigned int)((unsigned int)(a1))) * ((unsigned int)((unsigned int)(a1)));
    v_stack_m258 = (unsigned int)(v_r15);
    *(unsigned int *)(v_stack_m238 + 4112) = (unsigned int)((unsigned int)(*(unsigned int *)(result + v_rip + 6480125 * 1 + 36)));
    *(unsigned int *)(v_stack_m238 + 188) = (unsigned int)((unsigned int)(v_stack_m24C));
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(v_stack_m238 + 280))) + (0x1000ULL));
    result = HvLockHiveWriter(v_stack_m238, a2, a3, a4);
    a2 = 0;
    result = CmpDoFileSetSizeEx(v_stack_m238, a2, (unsigned int)((unsigned int)(v_rbx)), 1);
    result = HvUnlockHiveWriter(v_stack_m238, a2, (unsigned int)((unsigned int)(v_rbx)), 1);
    if (sign_flag) {
        *(unsigned __int8 *)(v_rip + 8381032) = 1;
    }
    result = HvUnlockHiveFlusherExclusive(v_stack_m238, a2, (unsigned int)((unsigned int)(v_rbx)), 1);
    result = CmpUnlockRegistry(v_stack_m238, a2, (unsigned int)((unsigned int)(v_rbx)), 1);
    if ((unsigned int)(v_r15) == 0) goto loc_007DB829;
    result = CmpRecoverFlushProtocolStateFromFiles(v_stack_m238, v_rsp - 472 - 16, (unsigned int)((unsigned int)(v_rbx)), 1);
    if (!sign_flag) goto loc_007DB829;
    goto loc_007DB922;
loc_007DB829:
    result = CmpLockRegistry(v_stack_m238, v_rsp - 472 - 16, (unsigned int)((unsigned int)(v_rbx)), 1);
    result = HvLockHiveFlusherExclusive(v_stack_m238, v_rsp - 472 - 16, (unsigned int)((unsigned int)(v_rbx)), 1);
    if ((*(unsigned int *)(v_stack_m238 + 136)) == ((unsigned int)(v_stack_m250))) goto loc_007DB890;
    if ((*(unsigned int *)(v_stack_m238 + 88)) <= 72) goto loc_007DB879;
loc_007DB850:
    result = RtlAreBitsClear(v_stack_m238 + 88, 72, (unsigned int)((unsigned int)(v_stack_m250)), 1);
    if ((unsigned __int8)(result) == 0) {
        a3 = (unsigned int)(v_stack_m250);
        a2 = 72;
        a1 = v_stack_m238 + 88;
        result = RtlSetBits(a1, a2, a3, 1);
    }
    v_r15 = (unsigned int)((72) + ((unsigned int)(v_stack_m250)));
    if (((unsigned int)(v_r15)) < (*(unsigned int *)(v_stack_m238 + 88))) goto loc_007DB850;
loc_007DB879:
    result = RtlNumberOfSetBits(v_stack_m238 + 88, a2, a3, 1);
    *(unsigned int *)(v_stack_m238 + 104) = (unsigned int)(result);
    *(unsigned int *)(v_stack_m238 + 136) = (unsigned int)(v_stack_m250);
loc_007DB890:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m238 + 64) + 4092)) != 72) goto loc_007DB8AB;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m238 + 64) + 4088)))) & (4)) != 0) goto loc_007DB8AB;
    result = (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m238 + 64) + 4088));
    if ((unsigned int)((unsigned int)(v_stack_m258)) != 0) {
        a1 = v_stack_m238 + 88;
        result = RtlSetAllBits(a1, a2, a3, 1);
        result = *(unsigned int *)(v_stack_m238 + 88);
        *(unsigned int *)(v_stack_m238 + 104) = (unsigned int)(result);
    }
    result = HvUnlockHiveFlusherExclusive(v_stack_m238, a2, a3, 1);
    result = CmpUnlockRegistry(v_stack_m238, a2, a3, 1);
    result = CmpLockRegistryExclusive(v_stack_m238, a2, a3, 1);
    if (((unsigned int)(a1)) == 3) {
        a1 = v_stack_m238;
        result = HvLockHiveFlusherShared(a1, a2, a3, 1);
        a2 = *(unsigned __int64 *)(v_stack_m238 + 64);
        a1 = v_stack_m238;
        a2 = *(unsigned int *)(a2 + 36);
        result = CmpMarkCurrentValueDirty(a1, a2, a3, 1);
        a1 = v_stack_m238;
        result = HvUnlockHiveFlusherShared(a1, a2, a3, 1);
    }
    a1 = (a1) * ((unsigned int)((unsigned int)(a1)));
    *(unsigned __int64 *)(a1 + v_rip + 6479782 * 1 + 48) = v_stack_m238;
    result = HvpDropPagedBins(v_stack_m238, a2, a3, 1);
    result = CmpUnlockRegistry(v_stack_m238, a2, a3, 1);
    if (!sign_flag) goto loc_007DB9A4;
loc_007DB922:
loc_007DB926:
    *(unsigned __int64 *)(v_stack_m238 + 56) = v_rsp - 472 - 16;
    *(unsigned __int64 *)(v_rsp - 472 - 16) = v_stack_m238;
    a2 = 0;
    v_stack_m290 = 80;
    result = SetFailureLocation(v_rsp - 472 - 16, a2, a2 + 22, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))));
    a1 = (v_rsp - 472 - 16) * ((unsigned int)((unsigned int)(a1)));
    *(unsigned __int8 *)(v_rip + 8373924) = 1;
    a1 = (a1) + (v_rip + 6479854);
    v_stack_m240 = a1;
    v_stack_m288 = v_rsp - 472 - 120;
    v_stack_m290 = 1;
    result = ExRaiseHardError((unsigned int)(0xC0000218ULL), 1, 1, v_stack_m240);
    v_stack_m290 = (int)((unsigned int)((unsigned int)((unsigned int)(result))));
    result = KeBugCheckEx(1 + 115, 1 + 1, 1, (unsigned int)((unsigned int)(a1)));
loc_007DB9A4:
    result = CmpFinishBeingActiveFlusherAndReconciler(v_stack_m238, 1 + 1, 1, (unsigned int)((unsigned int)(a1)));
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_stack_m238 + 64) + 4092)) != 1) goto loc_007DB9C2;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_m238 + 64) + 4088)))) & (4)) == 0) goto loc_007DBA07;
loc_007DB9C2:
    result = ExIsSoftBoot(v_stack_m238, 1 + 1, 1, (unsigned int)((unsigned int)(a1)));
    if ((unsigned __int8)(result) == 0) {
        a2 = 12;
        a1 = v_stack_m238;
        result = CmpFlushHive(a1, a2, 1, (unsigned int)((unsigned int)(a1)));
    }
    result = CmpLockRegistry(a1, a2, 1, (unsigned int)((unsigned int)(a1)));
    result = HvLockHiveFlusherExclusive(v_stack_m238, a2, 1, (unsigned int)((unsigned int)(a1)));
    *(unsigned int *)(*(unsigned __int64 *)(v_stack_m238 + 64) + 4092) = 1;
    result = HvUnlockHiveFlusherExclusive(v_stack_m238, a2, 1, (unsigned int)((unsigned int)(a1)));
    result = CmpUnlockRegistry(v_stack_m238, a2, 1, (unsigned int)((unsigned int)(a1)));
loc_007DBA07:
    if ((*(unsigned __int8 *)(v_rip + 8380501)) != 1) {
        result = CmpDiskFullWarning(v_stack_m238, a2, 1, (unsigned int)((unsigned int)(a1)));
    }
    *(unsigned int *)(v_rip + 8381610) = 0x800000ULL;
    *(unsigned __int64 *)(v_rip + 8381611) = v_rip + 8384148;
    a2 = (a2) * ((unsigned int)((unsigned int)(a1)));
    a2 = (a2) + (v_rip + 6479636);
    result = RtlAppendStringToString(v_rip + 8381586, a2, 1, (unsigned int)((unsigned int)(a1)));
    if ((*(unsigned int *)(v_rip + 7422413)) == 1) goto loc_007DBAF2;
    a2 = (a2) * ((unsigned int)((unsigned int)(a1)));
    result = CmpInitBackupHive(v_stack_m238, *(unsigned __int64 *)(a2 + v_rip + 6479782 * 1), 1, (unsigned int)((unsigned int)(a1)));
    if (!sign_flag) goto loc_007DBAF2;
    *(unsigned int *)(v_rip + 7422375) = 1;
    goto loc_007DBAF2;
loc_007DBA7B:
    if ((*(unsigned __int8 *)(v_rip + 8373636)) != 1) goto loc_007DBA8C;
    if ((*(unsigned int *)(v_rip + 7422162)) == 1) goto loc_007DBAEB;
loc_007DBA8C:
    if ((((unsigned __int8)(result)) & (2)) != 0) {
        result = CmpLockRegistry(v_stack_m238, *(unsigned __int64 *)(a2 + v_rip + 6479782 * 1), 1, (unsigned int)((unsigned int)(a1)));
        a1 = v_stack_m238;
        result = HvLockHiveFlusherExclusive(a1, *(unsigned __int64 *)(a2 + v_rip + 6479782 * 1), 1, (unsigned int)((unsigned int)(a1)));
        a1 = v_stack_m238;
        result = HvUnlockHiveFlusherExclusive(a1, *(unsigned __int64 *)(a2 + v_rip + 6479782 * 1), 1, (unsigned int)((unsigned int)(a1)));
        result = CmpUnlockRegistry(a1, *(unsigned __int64 *)(a2 + v_rip + 6479782 * 1), 1, (unsigned int)((unsigned int)(a1)));
    }
    *(unsigned int *)(v_rip + 8381454) = 0x800000ULL;
    *(unsigned __int64 *)(v_rip + 8381455) = v_rip + 8383992;
    a2 = (*(unsigned __int64 *)(a2 + v_rip + 6479782 * 1)) * ((unsigned int)((unsigned int)(a1)));
    a2 = (a2) + (v_rip + 6479480);
    result = RtlAppendStringToString(v_rip + 8381430, a2, 1, (unsigned int)((unsigned int)(a1)));
    goto loc_007DBAF2;
loc_007DBAEB:
loc_007DBAF2:
    if (((unsigned int)(a1)) != 3) goto loc_007DBB29;
    result = CmpLockRegistry(v_rip + 8381430, a2, 1, (unsigned int)((unsigned int)(a1)));
    result = HvLockHiveFlusherShared(v_stack_m238, a2, 1, (unsigned int)((unsigned int)(a1)));
    result = HvUnlockHiveFlusherShared(v_stack_m238, a2, 1, (unsigned int)((unsigned int)(a1)));
    result = CmpUnlockRegistry(v_stack_m238, a2, 1, (unsigned int)((unsigned int)(a1)));
    goto loc_007DBB29;
loc_007DBB22:
loc_007DBB29:
    result = CmpAcquireShutdownRundown(v_stack_m238, a2, 1, (unsigned int)((unsigned int)(a1)));
    if ((unsigned __int8)(result) != 0) goto loc_007DBB43;
loc_007DBB37:
    goto loc_007DB2F7;
loc_007DBB43:
    if (((*(unsigned int *)(v_stack_m238 + 160)) & (0x8001ULL)) != 0) goto loc_007DBB9D;
    if ((*(unsigned __int64 *)(v_stack_m238 + 1544)) == 1) goto loc_007DBB9D;
    v_r15 = (v_rip + 6479782) * ((unsigned int)((unsigned int)(a1)));
    result = CmpApplyAdminSdOnHiveFiles(v_stack_m238, *(unsigned __int64 *)(v_r15 + v_rip + 6479156 * 1), v_rip + 6479202, (unsigned int)((unsigned int)(a1)));
    if (sign_flag) {
        a2 = 19;
        v_stack_m290 = (int)((unsigned int)(result));
        result = v_rip + 6479123;
        a3 = v_stack_m238;
        a4 = *(unsigned __int64 *)(v_r15 + result * 1);
        a1 = a2 + 62;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = CmpReleaseShutdownRundown(a1, a2, a3, a4);
    goto loc_007DBB37;
}
```

## 5. (Beta) C Style

```c
int64_t CmpLoadHiveThread(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m238;
    uint64_t v_stack_m240;
    uint64_t v_stack_m248;
    uint32_t v_stack_m24C;
    uint64_t v_stack_m250;
    uint32_t v_stack_m258;
    uint64_t v_stack_m260;
    uint64_t v_stack_m268;
    uint32_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m28;
    uint64_t v_stack_m280;
    uint8_t v_stack_m288;
    uint64_t v_stack_m290;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2B0;
    uint64_t v_stack_m2B8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (688);
    result = (*(uint64_t *)(v_rip + 0x62F6D3)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x1D8 + 0x1A0) = result;
    local_rdi = 0;
    v_stack_m268 = 0;
    result = 0;
    *(uint32_t *)(local_rsp - 0x1D8 - 0x78) = 0;
    *(uint64_t *)(local_rsp - 0x1D8 - 0x20) = 0;
    Arg2 = 0;
    *(uint64_t *)(local_rsp - 0x1D8 - 0x58) = 0;
    *(uint32_t *)(local_rsp - 0x1D8 - 0x80) = 0;
    *(uint64_t *)(local_rsp - 0x1D8 - 0x30) = v_xmm0;
    *(uint32_t *)(local_rsp - 0x1D8 - 0x7C) = 0;
    v_stack_m270 = 0;
    result = memset(local_rsp - 472 - 16, Arg2, 432, Arg4);
    v_stack_m278 = 0;
    result = CmpInitializeThreadInfo(local_rsp - 472 - 48, Arg2, 432, Arg4);
    local_r15 = (local_r15) * ((uint32_t)((uint32_t)(Arg1)));
    *(uint64_t *)(local_rsp - 0x1D8 - 0x50) = v_xmm0;
    v_stack_m260 = 0;
    *(uint64_t *)(local_rsp - 0x1D8 - 0x70) = 0;
    Arg1 = (v_rip + 6481866 + 64) + (local_r15);
    *(uint64_t *)(local_rsp - 0x1D8 - 0x68) = 0;
    Arg4 = 0;
    *(uint64_t *)(local_rsp - 0x1D8 - 0x60) = 0;
    Arg3 = 0;
    v_stack_m288 = 0;
    Arg2 = 0;
    v_stack_m2B8 = 0;
    result = KeWaitForSingleObject(Arg1, Arg2, Arg3, Arg4);
    if (((uint32_t)(Arg1)) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x7FD07B))))) goto loc_007DB13E;
    Arg4 = 0;
    v_stack_m2B8 = 0;
    Arg3 = 0;
    Arg2 = 0;
    result = KeWaitForSingleObject(v_rip + 7457532, Arg2, Arg3, Arg4);
    if ((*(uint8_t *)(v_rip + 0x76C4C6)) == 0) goto loc_007DB13E;
    if ((*(uint8_t *)(v_rip + 0x76C4A1)) == 0) {
    }
    *(uint8_t *)(local_r15 + v_rip + 0x62E7CA * 1 + 0x3A) = 1;
    if (*(uint64_t *)(local_r15 + v_rip + 0x62E7CA * 1 + 0x18) != 0) goto loc_007DB563;
    v_stack_m280 = 0;
    v_stack_m280 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x7E97F5)));
    result = v_rip + 7448694;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x7E97F5)))) & (16)) == 0) {
        result = v_stack_m280;
        Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x7E97F5))) | (1));
        v_stack_m280 = result;
        Arg4 = 1;
        v_stack_m280 = (uint32_t)(Arg1);
        Arg3 = (uint32_t)(1 + 2);
        Arg2 = v_stack_m280;
        Arg1 = v_rip - 7327247;
        result = wil_details_FeatureReporting_ReportUsageToService(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_m280;
        Arg3 = v_rip - 7327264;
        Arg2 = (uint32_t)(1 + 2);
        result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(Arg1, Arg2, Arg3, Arg4);
        result = v_rip + 7448585;
    }
    Arg1 = (Arg1) * ((uint32_t)((uint32_t)(Arg1)));
    Arg1 = (Arg1) + (result);
    result = CmpMachineHiveCacheClaimEntry(Arg1, Arg2, Arg3, local_rsp - 472 - 80);
    if (!sign_flag) goto loc_007DB1FD;
    v_stack_m2B8 = 8;
    result = SetFailureLocation(local_rsp - 472 - 16, 1, 1 + 21, (uint32_t)((uint32_t)(result)));
    local_rsi = (v_rip + 6481580) + (59);
    local_rsi = (local_rsi) + (local_r15);
    goto loc_007DB220;
loc_007DB1FD:
    local_rsi = (v_rip + 6481561) + (59);
    local_rsi = (local_rsi) + (local_r15);
    *(uint8_t *)(local_rsi) = (uint8_t)(*(uint8_t *)(local_rsp - 0x1D8 - 0x47));
    v_stack_m260 = *(uint64_t *)(local_rsp - 0x1D8 - 0x50);
    v_stack_m288 = (uint8_t)(*(uint8_t *)(local_rsp - 0x1D8 - 0x48));
loc_007DB220:
    v_stack_m280 = 0;
    v_stack_m280 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x7E9732)));
    result = *(uint8_t *)(local_rsp - 0x1D8 - 0x48);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x7E9732)))) & (16)) == 0) {
        result = v_stack_m280;
        Arg3 = (uint32_t)(1 + 2);
        v_stack_m280 = result;
        result = 1;
        Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x7E9732))) | ((uint32_t)(result)));
        Arg4 = (uint32_t)(result);
        v_stack_m280 = (uint32_t)(Arg1);
        Arg1 = v_rip - 7327438;
        Arg2 = v_stack_m280;
        result = wil_details_FeatureReporting_ReportUsageToService(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_m280;
        Arg3 = v_rip - 7327460;
        Arg2 = (uint32_t)(1 + 2);
        result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(Arg1, Arg2, Arg3, Arg4);
    }
    local_rbx = (uint32_t)((uint32_t)(result));
    if (sign_flag) {
        Arg2 = v_rip + 6481441;
        Arg4 = local_rsi;
        Arg1 = Arg2 + 168;
        Arg2 = *(uint32_t *)(local_r15 + Arg2 * 1 + 0x20);
        result = local_rsp - 472 - 16;
        Arg1 = (Arg1) + (local_r15);
        v_stack_m290 = result;
        Arg3 = v_stack_m260;
        result = v_stack_m288;
        v_stack_m298 = result;
        v_stack_m2B0 = 0;
        v_stack_m2B8 = 0x1590001ULL;
        result = CmpInitHiveFromFile(Arg1, Arg2, Arg3, Arg4);
        local_rbx = (uint32_t)(result);
    }
    if (((uint32_t)(Arg1)) != 6) goto loc_007DB43B;
    if ((*(uint8_t *)(local_r15 + v_rip + 0x62E5DC * 1 + 0x3C)) != 0) goto loc_007DB43B;
    if (((uint32_t)(local_rbx)) == ((uint32_t)((uint32_t)(0xC0000034ULL)))) goto loc_007DB2EE;
    if (((uint32_t)(local_rbx)) != 0xC000003BULL) goto loc_007DB43B;
loc_007DB2EE:
loc_007DB2F0:
loc_007DB2F7:
    Arg1 = (Arg1) * ((uint32_t)((uint32_t)(Arg1)));
    Arg2 = 0;
    *(uint8_t *)(Arg1 + v_rip + 0x62E5DC * 1 + 0x39) = 1;
    Arg3 = 0;
    Arg1 = (Arg1) * ((uint32_t)((uint32_t)(Arg1)));
    Arg1 = (Arg1) + (v_rip + 6481367);
    result = KeSetEvent(Arg1, Arg2, Arg3, Arg4);
    result = (uint32_t)((1) + (1));
    if (((uint32_t)(result)) != 6) goto loc_007DB356;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x7FCE48));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x7FCE48)))) < 7) {
        Arg3 = 0;
        Arg1 = v_rip + 7456977;
        Arg2 = 0;
        result = KeSetEvent(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (Arg1) * ((uint32_t)((uint32_t)(Arg1)));
    result = v_rip + 6481209;
    if (*(uint64_t *)(Arg1 + v_rip + 0x62E539 * 1 + 0xB0) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(Arg1 + v_rip + 0x62E539 * 1 + 0xB0), Arg2, Arg3, Arg4);
        result = (uint32_t)(Arg1);
        Arg1 = (*(uint64_t *)(Arg1 + v_rip + 0x62E539 * 1 + 0xB0)) * (result);
        *(uint64_t *)(Arg1 + v_rip + 0x62E651 * 1) = v_xmm0;
    }
    v_stack_m268 = 0;
    v_stack_m268 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x7E95C5)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x7E95C5)))) & (16)) == 0) {
        result = v_stack_m268;
        Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x7E95C5))) | (1));
        v_stack_m278 = result;
        Arg4 = 1;
        v_stack_m278 = (uint32_t)(Arg1);
        Arg3 = (uint32_t)(1 + 2);
        Arg2 = v_stack_m278;
        Arg1 = v_rip - 7327803;
        result = wil_details_FeatureReporting_ReportUsageToService(Arg1, Arg2, Arg3, Arg4);
        Arg1 = v_stack_m278;
        Arg3 = v_rip - 7327820;
        Arg2 = (uint32_t)(1 + 2);
        result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (Arg1) * ((uint32_t)((uint32_t)(Arg1)));
    Arg1 = (Arg1) + (v_rip + 7448014);
    result = CmpHiveCacheEntryCleanup(Arg1, 6, Arg3, Arg4);
    result = CmCleanupThreadInfo(local_rsp - 472 - 48, 6, Arg3, Arg4);
    result = PsTerminateSystemThread(0, 6, Arg3, Arg4);
    Arg1 = (*(uint64_t *)(local_rsp - 0x1D8 + 0x1A0)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, 6, Arg3, Arg4);
    return result;
loc_007DB43B:
    if (condition_is_above_or_equal) goto loc_007DB45A;
    result = (result) * (v_rip + 6481489);
    if ((*(uint8_t *)(result + Arg3 * 1 + 0x3C)) != ((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x48)))) goto loc_007DB45A;
    if (((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38))) == 6) goto loc_007DB2EE;
loc_007DB45A:
    if (((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38))) != 0xC0000189ULL) goto loc_007DB493;
    result = CmpIsHiveLoadUnloadRundownActive(Arg1, 6, Arg3, Arg4);
    if ((uint8_t)(result) != 0) goto loc_007DB2F0;
loc_007DB46F:
    *(uint8_t *)(v_rip + 0x7FCB80) = 1;
    v_stack_m290 = (int32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38)));
    result = KeBugCheckEx(2 + 114, 2, local_rsp - 472 - 16, (uint32_t)((uint32_t)(Arg1)));
loc_007DB493:
    if (sign_flag) goto loc_007DB46F;
    if (condition_is_below) goto loc_007DB4B7;
    if ((*(uint64_t *)(v_stack_m238 + 0x628)) == (*(uint64_t *)(v_stack_m28 + 0x48))) goto loc_007DB46F;
    if ((*(uint64_t *)(v_stack_m238 + 0x630)) == (*(uint64_t *)(v_stack_m28 + 0x48))) goto loc_007DB46F;
loc_007DB4B7:
    result = (result) * ((uint32_t)((uint32_t)(Arg1)));
    result = (result) * ((uint32_t)((uint32_t)(Arg1)));
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + local_rsp - 0x1D8 - 0x10 * 1 + 0x24))) | (4));
    *(uint32_t *)(v_stack_m238 + 0x1010) = (uint32_t)(Arg1);
    *(uint64_t *)(result + local_rsp - 0x1D8 - 0x10 * 1 + 0x30) = v_stack_m238;
    if (v_stack_m260 == ((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x48)))) goto loc_007DB517;
    *(uint8_t *)(v_rip + 0x71467F) = 1;
loc_007DB4F6:
    Arg3 = 0;
    Arg2 = 0;
    result = KeSetEvent(v_rip + 6480880, Arg2, Arg3, (uint32_t)((uint32_t)(Arg1)));
    local_r15 = (v_rip + 6480880) + (184);
    local_r12 = (7) - (1);
    if (condition_is_not_equal) goto loc_007DB4F6;
loc_007DB517:
    if (((*(uint32_t *)(v_stack_m238 + 0xA0)) & (0x8001ULL)) != 0) goto loc_007DBB22;
    if ((*(uint32_t *)(v_rip + 0x7146F3)) == ((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48)))) goto loc_007DBB22;
    Arg2 = (Arg2) * ((uint32_t)((uint32_t)(Arg1)));
    result = CmpInitBackupHive(v_stack_m238, *(uint64_t *)(Arg2 + v_rip + 0x62E389 * 1), v_rip + 6480777, (uint32_t)((uint32_t)(Arg1)));
    if (!sign_flag) goto loc_007DBB29;
    *(uint32_t *)(v_rip + 0x7146C2) = (uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48));
    goto loc_007DBB29;
loc_007DB563:
    v_stack_m238 = v_stack_m238;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m238 + 0xA0)))) & (0x8001ULL)) != 0) goto loc_007DBA7B;
    Arg2 = 0;
    v_stack_m268 = local_rsp - 472 - 16;
    v_stack_m270 = *(uint64_t *)(v_stack_m28 + 0x48);
    v_stack_m278 = *(uint64_t *)(v_stack_m28 + 0x48);
    v_stack_m280 = v_stack_m250;
    local_r12 = (v_rip + 6480655) + (168);
    v_stack_m288 = *(uint64_t *)(v_stack_m28 + 0x48);
    local_r12 = (local_r12) + (local_r15);
    v_stack_m290 = 7;
    result = CmpOpenHiveFile(local_r12, Arg2, local_rsp - 472 - 112, v_stack_m248);
    if (sign_flag) goto loc_007DB922;
    local_r15 = (uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x48)));
    if (v_stack_m248 == 2) { local_r15 = (uint32_t)(3 - 2); }
    local_r15 = (uint32_t)((local_r15) << (4));
    v_stack_m268 = local_rsp - 472 - 16;
    v_stack_m270 = *(uint64_t *)(v_stack_m28 + 0x48);
    local_r15 = (uint32_t)((local_r15) | (2));
    v_stack_m278 = *(uint64_t *)(v_stack_m28 + 0x48);
    v_stack_m280 = *(uint64_t *)(v_stack_m28 + 0x48);
    v_stack_m288 = *(uint64_t *)(v_stack_m28 + 0x48);
    v_stack_m290 = (uint32_t)(local_r15);
    result = CmpOpenHiveFile(local_r12, 3 + 1, local_rsp - 472 - 104, local_rsp - 472 - 128);
    if (!sign_flag) goto loc_007DB638;
    goto loc_007DB926;
loc_007DB638:
    v_stack_m268 = local_rsp - 472 - 16;
    v_stack_m270 = 3 + 13;
    v_stack_m278 = 3 + 13;
    v_stack_m280 = 3 + 13;
    v_stack_m288 = 3 + 13;
    v_stack_m290 = (uint32_t)(local_r15);
    result = CmpOpenHiveFile(local_r12, 5, local_rsp - 472 - 96, local_rsp - 472 - 124);
    if (!sign_flag) goto loc_007DB67B;
    goto loc_007DB922;
loc_007DB67B:
    result = CmpGetFileSize(*(uint64_t *)(local_rsp - 0x1D8 - 0x70), local_rsp - 472 - 88, local_rsp - 472 - 96, local_rsp - 472 - 124);
    if (!sign_flag) goto loc_007DB698;
    goto loc_007DB922;
loc_007DB698:
    result = CmpGetFileSize(*(uint64_t *)(local_rsp - 0x1D8 - 0x68), local_rsp - 472 - 64, local_rsp - 472 - 96, local_rsp - 472 - 124);
    if (sign_flag) {
        Arg3 = (uint32_t)(result);
        Arg2 = 4;
        result = CmpLogFailureToGetFileSize(*(uint64_t *)(local_rsp - 0x1D8 - 0x68), Arg2, Arg3, local_rsp - 472 - 124);
        Arg2 = 1;
        v_stack_m290 = 43;
        result = local_rsp - 472 - 16;
        Arg4 = (uint32_t)((uint32_t)((uint32_t)(result)));
        *(uint64_t *)(v_stack_m238 + 0x38) = result;
        Arg1 = local_rsp - 472 - 16;
        *(uint64_t *)(local_rsp - 0x1D8 - 0x10) = v_stack_m238;
        Arg3 = Arg2 + 21;
        result = SetFailureLocation(Arg1, Arg2, Arg3, Arg4);
        *(uint64_t *)(local_rsp - 0x1D8 - 0x40) = 40;
    }
    result = CmpGetFileSize(*(uint64_t *)(local_rsp - 0x1D8 - 0x60), local_rsp - 472 - 56, Arg3, Arg4);
    if (sign_flag) {
        Arg3 = (uint32_t)(result);
        Arg2 = 5;
        result = CmpLogFailureToGetFileSize(*(uint64_t *)(local_rsp - 0x1D8 - 0x60), Arg2, Arg3, Arg4);
        Arg2 = 1;
        v_stack_m290 = 45;
        result = local_rsp - 472 - 16;
        Arg4 = (uint32_t)((uint32_t)((uint32_t)(result)));
        *(uint64_t *)(v_stack_m238 + 0x38) = result;
        Arg1 = local_rsp - 472 - 16;
        *(uint64_t *)(local_rsp - 0x1D8 - 0x10) = v_stack_m238;
        Arg3 = Arg2 + 21;
        result = SetFailureLocation(Arg1, Arg2, Arg3, Arg4);
        *(uint64_t *)(local_rsp - 0x1D8 - 0x38) = 40;
    }
    result = CmpBecomeActiveFlusherAndReconciler(v_stack_m238, Arg2, Arg3, Arg4);
    result = CmpLockRegistry(v_stack_m238, Arg2, Arg3, Arg4);
    result = HvLockHiveFlusherExclusive(v_stack_m238, Arg2, Arg3, Arg4);
    *(uint64_t *)(v_stack_m238 + 0x608) = *(uint64_t *)(local_rsp - 0x1D8 - 0x70);
    *(uint64_t *)(v_stack_m238 + 0x628) = *(uint64_t *)(local_rsp - 0x1D8 - 0x68);
    *(uint64_t *)(v_stack_m238 + 0x630) = *(uint64_t *)(local_rsp - 0x1D8 - 0x60);
    *(uint64_t *)(v_stack_m238 + 0x708) = *(uint64_t *)(local_rsp - 0x1D8 - 0x58);
    *(uint64_t *)(v_stack_m238 + 0x710) = v_xmm0;
    local_r15 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m238 + 0x1010))) & ((uint32_t)((uint32_t)(0x8000ULL))));
    result = ((uint32_t)((uint32_t)(Arg1))) * ((uint32_t)((uint32_t)(Arg1)));
    v_stack_m258 = (uint32_t)(local_r15);
    *(uint32_t *)(v_stack_m238 + 0x1010) = (uint32_t)((uint32_t)(*(uint32_t *)(result + v_rip + 0x62E0FD * 1 + 0x24)));
    *(uint32_t *)(v_stack_m238 + 0xBC) = (uint32_t)((uint32_t)(v_stack_m24C));
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(v_stack_m238 + 0x118))) + (0x1000ULL));
    result = HvLockHiveWriter(v_stack_m238, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = CmpDoFileSetSizeEx(v_stack_m238, Arg2, (uint32_t)((uint32_t)(local_rbx)), 1);
    result = HvUnlockHiveWriter(v_stack_m238, Arg2, (uint32_t)((uint32_t)(local_rbx)), 1);
    if (sign_flag) {
        *(uint8_t *)(v_rip + 0x7FE268) = 1;
    }
    result = HvUnlockHiveFlusherExclusive(v_stack_m238, Arg2, (uint32_t)((uint32_t)(local_rbx)), 1);
    result = CmpUnlockRegistry(v_stack_m238, Arg2, (uint32_t)((uint32_t)(local_rbx)), 1);
    if ((uint32_t)(local_r15) == 0) goto loc_007DB829;
    result = CmpRecoverFlushProtocolStateFromFiles(v_stack_m238, local_rsp - 472 - 16, (uint32_t)((uint32_t)(local_rbx)), 1);
    if (!sign_flag) goto loc_007DB829;
    goto loc_007DB922;
loc_007DB829:
    result = CmpLockRegistry(v_stack_m238, local_rsp - 472 - 16, (uint32_t)((uint32_t)(local_rbx)), 1);
    result = HvLockHiveFlusherExclusive(v_stack_m238, local_rsp - 472 - 16, (uint32_t)((uint32_t)(local_rbx)), 1);
    if ((*(uint32_t *)(v_stack_m238 + 0x88)) == ((uint32_t)(v_stack_m250))) goto loc_007DB890;
    if ((*(uint32_t *)(v_stack_m238 + 0x58)) <= 72) goto loc_007DB879;
loc_007DB850:
    result = RtlAreBitsClear(v_stack_m238 + 88, 72, (uint32_t)((uint32_t)(v_stack_m250)), 1);
    if ((uint8_t)(result) == 0) {
        Arg3 = (uint32_t)(v_stack_m250);
        Arg2 = 72;
        Arg1 = v_stack_m238 + 88;
        result = RtlSetBits(Arg1, Arg2, Arg3, 1);
    }
    local_r15 = (uint32_t)((72) + ((uint32_t)(v_stack_m250)));
    if (((uint32_t)(local_r15)) < (*(uint32_t *)(v_stack_m238 + 0x58))) goto loc_007DB850;
loc_007DB879:
    result = RtlNumberOfSetBits(v_stack_m238 + 88, Arg2, Arg3, 1);
    *(uint32_t *)(v_stack_m238 + 0x68) = (uint32_t)(result);
    *(uint32_t *)(v_stack_m238 + 0x88) = (uint32_t)(v_stack_m250);
loc_007DB890:
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m238 + 0x40) + 0xFFC)) != 72) goto loc_007DB8AB;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m238 + 0x40) + 0xFF8)))) & (4)) != 0) goto loc_007DB8AB;
    result = (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m238 + 0x40) + 0xFF8));
    if ((uint32_t)((uint32_t)(v_stack_m258)) != 0) {
        Arg1 = v_stack_m238 + 88;
        result = RtlSetAllBits(Arg1, Arg2, Arg3, 1);
        result = *(uint32_t *)(v_stack_m238 + 0x58);
        *(uint32_t *)(v_stack_m238 + 0x68) = (uint32_t)(result);
    }
    result = HvUnlockHiveFlusherExclusive(v_stack_m238, Arg2, Arg3, 1);
    result = CmpUnlockRegistry(v_stack_m238, Arg2, Arg3, 1);
    result = CmpLockRegistryExclusive(v_stack_m238, Arg2, Arg3, 1);
    if (((uint32_t)(Arg1)) == 3) {
        Arg1 = v_stack_m238;
        result = HvLockHiveFlusherShared(Arg1, Arg2, Arg3, 1);
        Arg2 = *(uint64_t *)(v_stack_m238 + 0x40);
        Arg1 = v_stack_m238;
        Arg2 = *(uint32_t *)(Arg2 + 0x24);
        result = CmpMarkCurrentValueDirty(Arg1, Arg2, Arg3, 1);
        Arg1 = v_stack_m238;
        result = HvUnlockHiveFlusherShared(Arg1, Arg2, Arg3, 1);
    }
    Arg1 = (Arg1) * ((uint32_t)((uint32_t)(Arg1)));
    *(uint64_t *)(Arg1 + v_rip + 0x62DFA6 * 1 + 0x30) = v_stack_m238;
    result = HvpDropPagedBins(v_stack_m238, Arg2, Arg3, 1);
    result = CmpUnlockRegistry(v_stack_m238, Arg2, Arg3, 1);
    if (!sign_flag) goto loc_007DB9A4;
loc_007DB922:
loc_007DB926:
    *(uint64_t *)(v_stack_m238 + 0x38) = local_rsp - 472 - 16;
    *(uint64_t *)(local_rsp - 0x1D8 - 0x10) = v_stack_m238;
    Arg2 = 0;
    v_stack_m290 = 80;
    result = SetFailureLocation(local_rsp - 472 - 16, Arg2, Arg2 + 22, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))));
    Arg1 = (local_rsp - 472 - 16) * ((uint32_t)((uint32_t)(Arg1)));
    *(uint8_t *)(v_rip + 0x7FC6A4) = 1;
    Arg1 = (Arg1) + (v_rip + 6479854);
    v_stack_m240 = Arg1;
    v_stack_m288 = local_rsp - 472 - 120;
    v_stack_m290 = 1;
    result = ExRaiseHardError((uint32_t)(0xC0000218ULL), 1, 1, v_stack_m240);
    v_stack_m290 = (int32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
    result = KeBugCheckEx(1 + 115, 1 + 1, 1, (uint32_t)((uint32_t)(Arg1)));
loc_007DB9A4:
    result = CmpFinishBeingActiveFlusherAndReconciler(v_stack_m238, 1 + 1, 1, (uint32_t)((uint32_t)(Arg1)));
    if ((*(uint32_t *)(*(uint64_t *)(v_stack_m238 + 0x40) + 0xFFC)) != 1) goto loc_007DB9C2;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_m238 + 0x40) + 0xFF8)))) & (4)) == 0) goto loc_007DBA07;
loc_007DB9C2:
    result = ExIsSoftBoot(v_stack_m238, 1 + 1, 1, (uint32_t)((uint32_t)(Arg1)));
    if ((uint8_t)(result) == 0) {
        Arg2 = 12;
        Arg1 = v_stack_m238;
        result = CmpFlushHive(Arg1, Arg2, 1, (uint32_t)((uint32_t)(Arg1)));
    }
    result = CmpLockRegistry(Arg1, Arg2, 1, (uint32_t)((uint32_t)(Arg1)));
    result = HvLockHiveFlusherExclusive(v_stack_m238, Arg2, 1, (uint32_t)((uint32_t)(Arg1)));
    *(uint32_t *)(*(uint64_t *)(v_stack_m238 + 0x40) + 0xFFC) = 1;
    result = HvUnlockHiveFlusherExclusive(v_stack_m238, Arg2, 1, (uint32_t)((uint32_t)(Arg1)));
    result = CmpUnlockRegistry(v_stack_m238, Arg2, 1, (uint32_t)((uint32_t)(Arg1)));
loc_007DBA07:
    if ((*(uint8_t *)(v_rip + 0x7FE055)) != 1) {
        result = CmpDiskFullWarning(v_stack_m238, Arg2, 1, (uint32_t)((uint32_t)(Arg1)));
    }
    *(uint32_t *)(v_rip + 0x7FE4AA) = 0x800000ULL;
    *(uint64_t *)(v_rip + 0x7FE4AB) = v_rip + 8384148;
    Arg2 = (Arg2) * ((uint32_t)((uint32_t)(Arg1)));
    Arg2 = (Arg2) + (v_rip + 6479636);
    result = RtlAppendStringToString(v_rip + 8381586, Arg2, 1, (uint32_t)((uint32_t)(Arg1)));
    if ((*(uint32_t *)(v_rip + 0x7141CD)) == 1) goto loc_007DBAF2;
    Arg2 = (Arg2) * ((uint32_t)((uint32_t)(Arg1)));
    result = CmpInitBackupHive(v_stack_m238, *(uint64_t *)(Arg2 + v_rip + 0x62DFA6 * 1), 1, (uint32_t)((uint32_t)(Arg1)));
    if (!sign_flag) goto loc_007DBAF2;
    *(uint32_t *)(v_rip + 0x7141A7) = 1;
    goto loc_007DBAF2;
loc_007DBA7B:
    if ((*(uint8_t *)(v_rip + 0x7FC584)) != 1) goto loc_007DBA8C;
    if ((*(uint32_t *)(v_rip + 0x7140D2)) == 1) goto loc_007DBAEB;
loc_007DBA8C:
    if ((((uint8_t)(result)) & (2)) != 0) {
        result = CmpLockRegistry(v_stack_m238, *(uint64_t *)(Arg2 + v_rip + 0x62DFA6 * 1), 1, (uint32_t)((uint32_t)(Arg1)));
        Arg1 = v_stack_m238;
        result = HvLockHiveFlusherExclusive(Arg1, *(uint64_t *)(Arg2 + v_rip + 0x62DFA6 * 1), 1, (uint32_t)((uint32_t)(Arg1)));
        Arg1 = v_stack_m238;
        result = HvUnlockHiveFlusherExclusive(Arg1, *(uint64_t *)(Arg2 + v_rip + 0x62DFA6 * 1), 1, (uint32_t)((uint32_t)(Arg1)));
        result = CmpUnlockRegistry(Arg1, *(uint64_t *)(Arg2 + v_rip + 0x62DFA6 * 1), 1, (uint32_t)((uint32_t)(Arg1)));
    }
    *(uint32_t *)(v_rip + 0x7FE40E) = 0x800000ULL;
    *(uint64_t *)(v_rip + 0x7FE40F) = v_rip + 8383992;
    Arg2 = (*(uint64_t *)(Arg2 + v_rip + 0x62DFA6 * 1)) * ((uint32_t)((uint32_t)(Arg1)));
    Arg2 = (Arg2) + (v_rip + 6479480);
    result = RtlAppendStringToString(v_rip + 8381430, Arg2, 1, (uint32_t)((uint32_t)(Arg1)));
    goto loc_007DBAF2;
loc_007DBAEB:
loc_007DBAF2:
    if (((uint32_t)(Arg1)) != 3) goto loc_007DBB29;
    result = CmpLockRegistry(v_rip + 8381430, Arg2, 1, (uint32_t)((uint32_t)(Arg1)));
    result = HvLockHiveFlusherShared(v_stack_m238, Arg2, 1, (uint32_t)((uint32_t)(Arg1)));
    result = HvUnlockHiveFlusherShared(v_stack_m238, Arg2, 1, (uint32_t)((uint32_t)(Arg1)));
    result = CmpUnlockRegistry(v_stack_m238, Arg2, 1, (uint32_t)((uint32_t)(Arg1)));
    goto loc_007DBB29;
loc_007DBB22:
loc_007DBB29:
    result = CmpAcquireShutdownRundown(v_stack_m238, Arg2, 1, (uint32_t)((uint32_t)(Arg1)));
    if ((uint8_t)(result) != 0) goto loc_007DBB43;
loc_007DBB37:
    goto loc_007DB2F7;
loc_007DBB43:
    if (((*(uint32_t *)(v_stack_m238 + 0xA0)) & (0x8001ULL)) != 0) goto loc_007DBB9D;
    if ((*(uint64_t *)(v_stack_m238 + 0x608)) == 1) goto loc_007DBB9D;
    local_r15 = (v_rip + 6479782) * ((uint32_t)((uint32_t)(Arg1)));
    result = CmpApplyAdminSdOnHiveFiles(v_stack_m238, *(uint64_t *)(local_r15 + v_rip + 0x62DD34 * 1), v_rip + 6479202, (uint32_t)((uint32_t)(Arg1)));
    if (sign_flag) {
        Arg2 = 19;
        v_stack_m290 = (int32_t)((uint32_t)(result));
        result = v_rip + 6479123;
        Arg3 = v_stack_m238;
        Arg4 = *(uint64_t *)(local_r15 + result * 1);
        Arg1 = Arg2 + 62;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    result = CmpReleaseShutdownRundown(Arg1, Arg2, Arg3, Arg4);
    goto loc_007DBB37;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007DB040&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
