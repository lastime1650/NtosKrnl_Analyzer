# CmpMountPreloadedHives

- RVA: `0x007DBE18`–`0x007DC5AA` (길이 `1,938` bytes)
- VA: `0x00000001407DBE18`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D6428`
- 디코드: `461`개 명령, `1,938/1,938` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **69**; 고유 호출 대상: **40**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **10**

### Outgoing calls
- `0x007DBE70` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x007DBEC0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)
- `0x007DBEE7` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x007DBEED` → [CmpLockRegistryExclusive](../84/CmpLockRegistryExclusive_function_0084F9B4.md) (function, `0x0084F9B4`)
- `0x007DBF11` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DBF7A` → [CmpQueryHiveRedirectionFileList](../87/CmpQueryHiveRedirectionFileList_function_00879094.md) (function, `0x00879094`)
- `0x007DBFAD` → [HalAdjustResourceList](../../text/48/HalAdjustResourceList_function_0048FDC0.md) (function, `0x0048FDC0`)
- `0x007DBFB5` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (function, `0x002250A0`)
- `0x007DBFD5` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x007DBFE4` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x007DC003` → [SyspartGetSystemPartition](../A9/SyspartGetSystemPartition_function_00A973CC.md) (function, `0x00A973CC`)
- `0x007DC026` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x007DC037` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (function, `0x0040F990`)
- `0x007DC045` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007DC09B` → [CmpOpenHiveFile](../87/CmpOpenHiveFile_function_0087A71C.md) (function, `0x0087A71C`)
- `0x007DC0F0` → [CmpOpenHiveFile](../87/CmpOpenHiveFile_function_0087A71C.md) (function, `0x0087A71C`)
- `0x007DC133` → [CmpOpenHiveFile](../87/CmpOpenHiveFile_function_0087A71C.md) (function, `0x0087A71C`)
- `0x007DC14A` → [CmpGetFileSize](../9B/CmpGetFileSize_function_009B9994.md) (function, `0x009B9994`)
- `0x007DC161` → [CmpGetFileSize](../9B/CmpGetFileSize_function_009B9994.md) (function, `0x009B9994`)
- `0x007DC174` → [CmpLogFailureToGetFileSize](../9B/CmpLogFailureToGetFileSize_function_009B9F5C.md) (function, `0x009B9F5C`)
- `0x007DC19A` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x007DC1AE` → [CmpGetFileSize](../9B/CmpGetFileSize_function_009B9994.md) (function, `0x009B9994`)
- `0x007DC1C1` → [CmpLogFailureToGetFileSize](../9B/CmpLogFailureToGetFileSize_function_009B9F5C.md) (function, `0x009B9F5C`)
- `0x007DC1E7` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x007DC1F3` → [CmpBecomeActiveFlusherAndReconciler](../7E/CmpBecomeActiveFlusherAndReconciler_function_007E7E20.md) (function, `0x007E7E20`)
- `0x007DC1F8` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x007DC200` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (function, `0x00BC9C50`)
- `0x007DC257` → [HvLockHiveWriter](../85/HvLockHiveWriter_function_00859894.md) (function, `0x00859894`)
- `0x007DC267` → [CmpDoFileSetSizeEx](../9B/CmpDoFileSetSizeEx_function_009B2A4C.md) (function, `0x009B2A4C`)
- `0x007DC271` → [HvUnlockHiveWriter](../85/HvUnlockHiveWriter_function_008598E4.md) (function, `0x008598E4`)
- `0x007DC2B2` → [HvLockHiveWriter](../85/HvLockHiveWriter_function_00859894.md) (function, `0x00859894`)
- `0x007DC2BA` → [HvCheckAndUpdateHiveBackupTimeStamp](../87/HvCheckAndUpdateHiveBackupTimeStamp_function_0087BE90.md) (function, `0x0087BE90`)
- `0x007DC2C2` → [HvUnlockHiveWriter](../85/HvUnlockHiveWriter_function_008598E4.md) (function, `0x008598E4`)
- `0x007DC2CC` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (function, `0x00BC9C34`)
- `0x007DC2D1` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DC2DD` → [CmpRecoverFlushProtocolStateFromFiles](../7E/CmpRecoverFlushProtocolStateFromFiles_function_007EE4B0.md) (function, `0x007EE4B0`)
- `0x007DC2EC` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x007DC2F4` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (function, `0x00BC9C50`)
- `0x007DC31B` → [RtlAreBitsClear](../../text/45/RtlAreBitsClear_function_00451800.md) (function, `0x00451800`)
- `0x007DC32D` → [RtlSetBits](../../text/3E/RtlSetBits_function_003E1610.md) (function, `0x003E1610`)
- `0x007DC33E` → [RtlNumberOfSetBits](../../text/43/RtlNumberOfSetBits_function_00433F70.md) (function, `0x00433F70`)
- `0x007DC36C` → [RtlSetAllBits](../../text/36/RtlSetAllBits_function_00362490.md) (function, `0x00362490`)
- `0x007DC37A` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (function, `0x00BC9C34`)
- `0x007DC37F` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DC384` → [CmpLockRegistryExclusive](../84/CmpLockRegistryExclusive_function_0084F9B4.md) (function, `0x0084F9B4`)
- `0x007DC38C` → [HvpDropPagedBins](../9B/HvpDropPagedBins_function_009B7168.md) (function, `0x009B7168`)
- `0x007DC393` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DC3A3` → [CmpFinishBeingActiveFlusherAndReconciler](../7E/CmpFinishBeingActiveFlusherAndReconciler_function_007E7EB0.md) (function, `0x007E7EB0`)
- `0x007DC3B9` → [ExIsSoftBoot](../../text/4F/ExIsSoftBoot_function_004FAE60.md) (function, `0x004FAE60`)
- `0x007DC3CA` → [CmpFlushHive](../9B/CmpFlushHive_function_009B3DC0.md) (function, `0x009B3DC0`)
- `0x007DC3CF` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x007DC3D7` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (function, `0x00BC9C50`)
- `0x007DC3E9` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (function, `0x00BC9C34`)
- `0x007DC3EE` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DC3FC` → [CmpDiskFullWarning](../7E/CmpDiskFullWarning_function_007E59E0.md) (function, `0x007E59E0`)
- `0x007DC401` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (function, `0x00BC9B34`)
- `0x007DC409` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (function, `0x00BC9C50`)
- `0x007DC423` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (function, `0x00BC9C34`)
- `0x007DC428` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (function, `0x00BC9A84`)
- `0x007DC43D` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (function, `0x00216820`)
- `0x007DC44D` → [CmpInitCmRM](../87/CmpInitCmRM_function_0087C700.md) (function, `0x0087C700`)
- `0x007DC45B` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x007DC481` → [TmEnableCallbacks](../../text/4F/TmEnableCallbacks_function_004FE0E0.md) (function, `0x004FE0E0`)
- `0x007DC48D` → [CmRmFinalizeRecovery](../AB/CmRmFinalizeRecovery_function_00ABEB68.md) (function, `0x00ABEB68`)
- `0x007DC51A` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (function, `0x0046EF54`)
- `0x007DC54E` → [ExRaiseHardError](../A6/ExRaiseHardError_function_00A64520.md) (function, `0x00A64520`)
- `0x007DC569` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x007DC574` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007DC583` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [CmpFinishSystemHivesLoad](CmpFinishSystemHivesLoad_function_007DA210.md) at `0x007DA635`
- [CmpFinishSystemHivesLoad](CmpFinishSystemHivesLoad_function_007DA210.md) at `0x007DAAD3`

### Static image references
- `0x007DBE3E` → RVA `0x00E0A740` (`.data`; read)
- `0x007DBEF2` → RVA `0x00EF7C00` (`.data`; read)
- `0x007DBFBA` → RVA `0x00B013A0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007DBFE9` → RVA `0x00B090D0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007DC01A` → RVA `0x00B01960` (` ?? ::NNGAKEGL::`string'`; read)
- `0x007DC27A` → RVA `0x00FD9A63` (`PAGEDATA`; write)
- `0x007DC3F3` → RVA `0x00FD9A63` (`PAGEDATA`; read)
- `0x007DC42D` → RVA `0x00FC6AB0` (`ALMOSTRO`; read)
- `0x007DC476` → RVA `0x009B1950` (`CmKtmNotification`; read)
- `0x007DC524` → RVA `0x00FD8005` (`PAGEDATA`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **42**
  - `0x007DBE70` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x007DBEC0` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
  - `0x007DBEE7` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x007DBF11` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DBFAD` → [HalAdjustResourceList](../../text/48/HalAdjustResourceList_function_0048FDC0.md) (`PAGE` → `.text`)
  - `0x007DBFB5` → [PsGetServerSiloGlobals](../../text/22/PsGetServerSiloGlobals_function_002250A0.md) (`PAGE` → `.text`)
  - `0x007DBFD5` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (`PAGE` → `.text`)
  - `0x007DBFE4` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (`PAGE` → `.text`)
  - `0x007DC026` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (`PAGE` → `.text`)
  - `0x007DC037` → [RtlAppendUnicodeToString](../../text/40/RtlAppendUnicodeToString_function_0040F990.md) (`PAGE` → `.text`)
  - `0x007DC045` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007DC19A` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x007DC1E7` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x007DC1F8` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DC200` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (`PAGE` → `PAGECMRC`)
  - `0x007DC2CC` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DC2D1` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DC2EC` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DC2F4` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (`PAGE` → `PAGECMRC`)
  - `0x007DC31B` → [RtlAreBitsClear](../../text/45/RtlAreBitsClear_function_00451800.md) (`PAGE` → `.text`)
  - `0x007DC32D` → [RtlSetBits](../../text/3E/RtlSetBits_function_003E1610.md) (`PAGE` → `.text`)
  - `0x007DC33E` → [RtlNumberOfSetBits](../../text/43/RtlNumberOfSetBits_function_00433F70.md) (`PAGE` → `.text`)
  - `0x007DC36C` → [RtlSetAllBits](../../text/36/RtlSetAllBits_function_00362490.md) (`PAGE` → `.text`)
  - `0x007DC37A` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DC37F` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DC393` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DC3B9` → [ExIsSoftBoot](../../text/4F/ExIsSoftBoot_function_004FAE60.md) (`PAGE` → `.text`)
  - `0x007DC3CF` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DC3D7` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (`PAGE` → `PAGECMRC`)
  - `0x007DC3E9` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DC3EE` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DC401` → [CmpLockRegistry](../../pagecmrc/BC/CmpLockRegistry_function_00BC9B34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DC409` → [HvLockHiveFlusherExclusive](../../pagecmrc/BC/HvLockHiveFlusherExclusive_function_00BC9C50.md) (`PAGE` → `PAGECMRC`)
  - `0x007DC423` → [HvUnlockHiveFlusherExclusive](../../pagecmrc/BC/HvUnlockHiveFlusherExclusive_function_00BC9C34.md) (`PAGE` → `PAGECMRC`)
  - `0x007DC428` → [CmpUnlockRegistry](../../pagecmrc/BC/CmpUnlockRegistry_function_00BC9A84.md) (`PAGE` → `PAGECMRC`)
  - `0x007DC43D` → [KiStackAttachProcess](../../text/21/KiStackAttachProcess_function_00216820.md) (`PAGE` → `.text`)
  - `0x007DC45B` → [KiUnstackDetachProcess](../../text/21/KiUnstackDetachProcess_function_00217D30.md) (`PAGE` → `.text`)
  - `0x007DC481` → [TmEnableCallbacks](../../text/4F/TmEnableCallbacks_function_004FE0E0.md) (`PAGE` → `.text`)
  - `0x007DC51A` → [SetFailureLocation](../../text/46/SetFailureLocation_function_0046EF54.md) (`PAGE` → `.text`)
  - `0x007DC569` → [KeBugCheckEx](../../text/4F/KeBugCheckEx_function_004FD660.md) (`PAGE` → `.text`)
  - `0x007DC574` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007DC583` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007DBE18  48 8B C4                        mov rax, rsp
007DBE1B  48 89 58 08                     mov qword ptr [rax + 8], rbx
007DBE1F  48 89 70 10                     mov qword ptr [rax + 0x10], rsi
007DBE23  48 89 78 18                     mov qword ptr [rax + 0x18], rdi
007DBE27  55                              push rbp
007DBE28  41 54                           push r12
007DBE2A  41 55                           push r13
007DBE2C  41 56                           push r14
007DBE2E  41 57                           push r15
007DBE30  48 8D A8 18 FE FF FF            lea rbp, [rax - 0x1e8]
007DBE37  48 81 EC C0 02 00 00            sub rsp, 0x2c0
007DBE3E  48 8B 05 FB E8 62 00            mov rax, qword ptr [rip + 0x62e8fb]
007DBE45  48 33 C4                        xor rax, rsp
007DBE48  48 89 85 B0 01 00 00            mov qword ptr [rbp + 0x1b0], rax
007DBE4F  33 F6                           xor esi, esi
007DBE51  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007DBE55  0F 57 C0                        xorps xmm0, xmm0
007DBE58  89 74 24 78                     mov dword ptr [rsp + 0x78], esi
007DBE5C  33 D2                           xor edx, edx
007DBE5E  89 75 84                        mov dword ptr [rbp - 0x7c], esi
007DBE61  41 B8 B0 01 00 00               mov r8d, 0x1b0
007DBE67  48 89 75 A8                     mov qword ptr [rbp - 0x58], rsi
007DBE6B  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
007DBE70  E8 CB AD EE FF                  call 0x1406c6c40
007DBE75  0F 57 C0                        xorps xmm0, xmm0
007DBE78  89 74 24 7C                     mov dword ptr [rsp + 0x7c], esi
007DBE7C  41 BD 00 10 00 00               mov r13d, 0x1000
007DBE82  48 89 75 90                     mov qword ptr [rbp - 0x70], rsi
007DBE86  41 8B D5                        mov edx, r13d
007DBE89  89 75 80                        mov dword ptr [rbp - 0x80], esi
007DBE8C  41 B8 43 4D 53 62               mov r8d, 0x62534d43
007DBE92  48 89 75 A0                     mov qword ptr [rbp - 0x60], rsi
007DBE96  B9 00 01 00 00                  mov ecx, 0x100
007DBE9B  89 74 24 60                     mov dword ptr [rsp + 0x60], esi
007DBE9F  0F 11 85 80 01 00 00            movups xmmword ptr [rbp + 0x180], xmm0
007DBEA6  48 89 75 88                     mov qword ptr [rbp - 0x78], rsi
007DBEAA  0F 11 85 90 01 00 00            movups xmmword ptr [rbp + 0x190], xmm0
007DBEB1  89 74 24 68                     mov dword ptr [rsp + 0x68], esi
007DBEB5  0F 11 85 A0 01 00 00            movups xmmword ptr [rbp + 0x1a0], xmm0
007DBEBC  48 89 75 98                     mov qword ptr [rbp - 0x68], rsi
007DBEC0  E8 2B 62 3A 00                  call 0x140b820f0
007DBEC5  48 89 45 B0                     mov qword ptr [rbp - 0x50], rax
007DBEC9  48 8B D8                        mov rbx, rax
007DBECC  48 85 C0                        test rax, rax
007DBECF  75 1C                           jne 0x1407dbeed
007DBED1  45 33 C9                        xor r9d, r9d
007DBED4  48 C7 44 24 20 9A 00 00 C0      mov qword ptr [rsp + 0x20], 0xffffffffc000009a
007DBEDD  8D 56 02                        lea edx, [rsi + 2]
007DBEE0  8D 4E 74                        lea ecx, [rsi + 0x74]
007DBEE3  44 8D 46 01                     lea r8d, [rsi + 1]
007DBEE7  E8 74 17 D2 FF                  call 0x1404fd660
007DBEEC  CC                              int3
007DBEED  E8 C2 3A 07 00                  call 0x14084f9b4
007DBEF2  48 8B 05 07 BD 71 00            mov rax, qword ptr [rip + 0x71bd07]
007DBEF9  48 8D 3D 00 BD 71 00            lea rdi, [rip + 0x71bd00]
007DBF00  EB 0A                           jmp 0x1407dbf0c
007DBF02  83 88 B8 09 00 00 04            or dword ptr [rax + 0x9b8], 4
007DBF09  48 8B 00                        mov rax, qword ptr [rax]
007DBF0C  48 3B C7                        cmp rax, rdi
007DBF0F  75 F1                           jne 0x1407dbf02
007DBF11  E8 6E DB 3E 00                  call 0x140bc9a84
007DBF16  48 8B 05 E3 BC 71 00            mov rax, qword ptr [rip + 0x71bce3]
007DBF1D  41 BF 01 00 00 00               mov r15d, 1
007DBF23  45 8D 67 01                     lea r12d, [r15 + 1]
007DBF27  45 8D 77 15                     lea r14d, [r15 + 0x15]
007DBF2B  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
007DBF30  48 3B C7                        cmp rax, rdi
007DBF33  0F 84 36 06 00 00               je 0x1407dc56f
007DBF39  48 8D B8 A8 F9 FF FF            lea rdi, [rax - 0x658]
007DBF40  8B 87 A0 00 00 00               mov eax, dword ptr [rdi + 0xa0]
007DBF46  8B C8                           mov ecx, eax
007DBF48  81 E1 00 00 00 01               and ecx, 0x1000000
007DBF4E  89 4C 24 64                     mov dword ptr [rsp + 0x64], ecx
007DBF52  41 84 C7                        test r15b, al
007DBF55  0F 85 41 05 00 00               jne 0x1407dc49c
007DBF5B  0F 57 C0                        xorps xmm0, xmm0
007DBF5E  48 8D 8F 40 07 00 00            lea rcx, [rdi + 0x740]
007DBF65  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
007DBF6A  48 8D 54 24 50                  lea rdx, [rsp + 0x50]
007DBF6F  66 44 89 6C 24 52               mov word ptr [rsp + 0x52], r13w
007DBF75  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
007DBF7A  E8 15 D1 09 00                  call 0x140879094
007DBF7F  84 C0                           test al, al
007DBF81  74 0C                           je 0x1407dbf8f
007DBF83  66 44 39 64 24 50               cmp word ptr [rsp + 0x50], r12w
007DBF89  0F 85 AD 00 00 00               jne 0x1407dc03c
007DBF8F  0F 57 C0                        xorps xmm0, xmm0
007DBF92  0F 11 44 24 50                  movups xmmword ptr [rsp + 0x50], xmm0
007DBF97  66 44 89 6C 24 52               mov word ptr [rsp + 0x52], r13w
007DBF9D  48 89 5C 24 58                  mov qword ptr [rsp + 0x58], rbx
007DBFA2  8B 87 A0 00 00 00               mov eax, dword ptr [rdi + 0xa0]
007DBFA8  41 85 C5                        test r13d, eax
007DBFAB  74 45                           je 0x1407dbff2
007DBFAD  E8 0E 3E CB FF                  call 0x14048fdc0
007DBFB2  48 8B C8                        mov rcx, rax
007DBFB5  E8 E6 90 A4 FF                  call 0x1402250a0
007DBFBA  48 8D 15 DF 53 32 00            lea rdx, [rip + 0x3253df]
007DBFC1  48 8B 88 D8 04 00 00            mov rcx, qword ptr [rax + 0x4d8]
007DBFC8  0F B7 01                        movzx eax, word ptr [rcx]
007DBFCB  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007DBFD0  66 89 44 24 68                  mov word ptr [rsp + 0x68], ax
007DBFD5  E8 B6 39 C3 FF                  call 0x14040f990
007DBFDA  48 8D 54 24 68                  lea rdx, [rsp + 0x68]
007DBFDF  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007DBFE4  E8 A7 39 C3 FF                  call 0x14040f990
007DBFE9  48 8D 15 E0 D0 32 00            lea rdx, [rip + 0x32d0e0]
007DBFF0  EB 2F                           jmp 0x1407dc021
007DBFF2  0F BA E0 0D                     bt eax, 0xd
007DBFF6  73 1C                           jae 0x1407dc014
007DBFF8  4C 8D 44 24 78                  lea r8, [rsp + 0x78]
007DBFFD  41 8B D5                        mov edx, r13d
007DC000  48 8B CB                        mov rcx, rbx
007DC003  E8 C4 B3 2B 00                  call 0x140a973cc
007DC008  8B D8                           mov ebx, eax
007DC00A  85 C0                           test eax, eax
007DC00C  0F 88 E6 04 00 00               js 0x1407dc4f8
007DC012  EB 17                           jmp 0x1407dc02b
007DC014  0F BA E0 15                     bt eax, 0x15
007DC018  73 11                           jae 0x1407dc02b
007DC01A  48 8D 15 3F 59 32 00            lea rdx, [rip + 0x32593f]
007DC021  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007DC026  E8 65 39 C3 FF                  call 0x14040f990
007DC02B  48 8B 97 28 07 00 00            mov rdx, qword ptr [rdi + 0x728]
007DC032  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007DC037  E8 54 39 C3 FF                  call 0x14040f990
007DC03C  48 8B 8F 28 07 00 00            mov rcx, qword ptr [rdi + 0x728]
007DC043  33 D2                           xor edx, edx
007DC045  E8 26 68 3A 00                  call 0x140b82870
007DC04A  48 8D 45 D0                     lea rax, [rbp - 0x30]
007DC04E  0F 57 C0                        xorps xmm0, xmm0
007DC051  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
007DC056  4C 8D 4C 24 60                  lea r9, [rsp + 0x60]
007DC05B  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
007DC060  48 8D 45 98                     lea rax, [rbp - 0x68]
007DC064  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
007DC069  4C 8D 45 88                     lea r8, [rbp - 0x78]
007DC06D  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007DC072  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007DC077  0F 11 87 20 07 00 00            movups xmmword ptr [rdi + 0x720], xmm0
007DC07E  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
007DC083  33 D2                           xor edx, edx
007DC085  C7 44 24 20 07 00 00 00         mov dword ptr [rsp + 0x20], 7
007DC08D  66 89 B7 22 07 00 00            mov word ptr [rdi + 0x722], si
007DC094  48 89 B7 28 07 00 00            mov qword ptr [rdi + 0x728], rsi
007DC09B  E8 7C E6 09 00                  call 0x14087a71c
007DC0A0  8B D8                           mov ebx, eax
007DC0A2  85 C0                           test eax, eax
007DC0A4  0F 88 49 04 00 00               js 0x1407dc4f3
007DC0AA  44 39 64 24 60                  cmp dword ptr [rsp + 0x60], r12d
007DC0AF  4C 8D 4C 24 7C                  lea r9, [rsp + 0x7c]
007DC0B4  B8 12 00 00 00                  mov eax, 0x12
007DC0B9  4C 8D 45 90                     lea r8, [rbp - 0x70]
007DC0BD  45 8B EC                        mov r13d, r12d
007DC0C0  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007DC0C5  44 0F 44 E8                     cmove r13d, eax
007DC0C9  BA 04 00 00 00                  mov edx, 4
007DC0CE  48 8D 45 D0                     lea rax, [rbp - 0x30]
007DC0D2  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
007DC0D7  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
007DC0DC  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
007DC0E1  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
007DC0E6  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
007DC0EB  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
007DC0F0  E8 27 E6 09 00                  call 0x14087a71c
007DC0F5  8B D8                           mov ebx, eax
007DC0F7  85 C0                           test eax, eax
007DC0F9  48 8D 45 D0                     lea rax, [rbp - 0x30]
007DC0FD  0F 88 E9 03 00 00               js 0x1407dc4ec
007DC103  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
007DC108  4C 8D 4D 80                     lea r9, [rbp - 0x80]
007DC10C  48 89 74 24 40                  mov qword ptr [rsp + 0x40], rsi
007DC111  4C 8D 45 A0                     lea r8, [rbp - 0x60]
007DC115  48 89 74 24 38                  mov qword ptr [rsp + 0x38], rsi
007DC11A  48 8D 4C 24 50                  lea rcx, [rsp + 0x50]
007DC11F  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
007DC124  BA 05 00 00 00                  mov edx, 5
007DC129  48 89 74 24 28                  mov qword ptr [rsp + 0x28], rsi
007DC12E  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
007DC133  E8 E4 E5 09 00                  call 0x14087a71c
007DC138  8B D8                           mov ebx, eax
007DC13A  85 C0                           test eax, eax
007DC13C  0F 88 A3 03 00 00               js 0x1407dc4e5
007DC142  48 8B 4D 88                     mov rcx, qword ptr [rbp - 0x78]
007DC146  48 8D 55 A8                     lea rdx, [rbp - 0x58]
007DC14A  E8 45 D8 1D 00                  call 0x1409b9994
007DC14F  8B D8                           mov ebx, eax
007DC151  85 C0                           test eax, eax
007DC153  0F 88 75 03 00 00               js 0x1407dc4ce
007DC159  48 8B 4D 90                     mov rcx, qword ptr [rbp - 0x70]
007DC15D  48 8D 55 B8                     lea rdx, [rbp - 0x48]
007DC161  E8 2E D8 1D 00                  call 0x1409b9994
007DC166  8B D8                           mov ebx, eax
007DC168  85 C0                           test eax, eax
007DC16A  79 37                           jns 0x1407dc1a3
007DC16C  44 8B C0                        mov r8d, eax
007DC16F  BA 04 00 00 00                  mov edx, 4
007DC174  E8 E3 DD 1D 00                  call 0x1409b9f5c
007DC179  48 8D 45 D0                     lea rax, [rbp - 0x30]
007DC17D  C7 44 24 20 2B 00 00 00         mov dword ptr [rsp + 0x20], 0x2b
007DC185  48 89 47 38                     mov qword ptr [rdi + 0x38], rax
007DC189  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007DC18D  44 8B CB                        mov r9d, ebx
007DC190  48 89 7D D0                     mov qword ptr [rbp - 0x30], rdi
007DC194  45 8B C6                        mov r8d, r14d
007DC197  41 8B D7                        mov edx, r15d
007DC19A  E8 B5 2D C9 FF                  call 0x14046ef54
007DC19F  48 89 75 B8                     mov qword ptr [rbp - 0x48], rsi
007DC1A3  4C 8B 6D A0                     mov r13, qword ptr [rbp - 0x60]
007DC1A7  48 8D 55 C0                     lea rdx, [rbp - 0x40]
007DC1AB  49 8B CD                        mov rcx, r13
007DC1AE  E8 E1 D7 1D 00                  call 0x1409b9994
007DC1B3  8B D8                           mov ebx, eax
007DC1B5  85 C0                           test eax, eax
007DC1B7  79 37                           jns 0x1407dc1f0
007DC1B9  44 8B C0                        mov r8d, eax
007DC1BC  BA 05 00 00 00                  mov edx, 5
007DC1C1  E8 96 DD 1D 00                  call 0x1409b9f5c
007DC1C6  48 8D 45 D0                     lea rax, [rbp - 0x30]
007DC1CA  C7 44 24 20 2D 00 00 00         mov dword ptr [rsp + 0x20], 0x2d
007DC1D2  48 89 47 38                     mov qword ptr [rdi + 0x38], rax
007DC1D6  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007DC1DA  44 8B CB                        mov r9d, ebx
007DC1DD  48 89 7D D0                     mov qword ptr [rbp - 0x30], rdi
007DC1E1  45 8B C6                        mov r8d, r14d
007DC1E4  41 8B D7                        mov edx, r15d
007DC1E7  E8 68 2D C9 FF                  call 0x14046ef54
007DC1EC  48 89 75 C0                     mov qword ptr [rbp - 0x40], rsi
007DC1F0  48 8B CF                        mov rcx, rdi
007DC1F3  E8 28 BC 00 00                  call 0x1407e7e20
007DC1F8  E8 37 D9 3E 00                  call 0x140bc9b34
007DC1FD  48 8B CF                        mov rcx, rdi
007DC200  E8 4B DA 3E 00                  call 0x140bc9c50
007DC205  48 8B 45 88                     mov rax, qword ptr [rbp - 0x78]
007DC209  48 8B CF                        mov rcx, rdi
007DC20C  0F 10 45 B8                     movups xmm0, xmmword ptr [rbp - 0x48]
007DC210  48 89 87 08 06 00 00            mov qword ptr [rdi + 0x608], rax
007DC217  48 8B 45 90                     mov rax, qword ptr [rbp - 0x70]
007DC21B  48 89 87 28 06 00 00            mov qword ptr [rdi + 0x628], rax
007DC222  48 8B 45 A8                     mov rax, qword ptr [rbp - 0x58]
007DC226  48 89 87 08 07 00 00            mov qword ptr [rdi + 0x708], rax
007DC22D  8B 45 9C                        mov eax, dword ptr [rbp - 0x64]
007DC230  4C 89 AF 30 06 00 00            mov qword ptr [rdi + 0x630], r13
007DC237  0F 11 87 10 07 00 00            movups xmmword ptr [rdi + 0x710], xmm0
007DC23E  83 A7 A0 00 00 00 FD            and dword ptr [rdi + 0xa0], 0xfffffffd
007DC245  8B 9F 18 01 00 00               mov ebx, dword ptr [rdi + 0x118]
007DC24B  81 C3 00 10 00 00               add ebx, 0x1000
007DC251  89 87 BC 00 00 00               mov dword ptr [rdi + 0xbc], eax
007DC257  E8 38 D6 07 00                  call 0x140859894
007DC25C  44 8B C3                        mov r8d, ebx
007DC25F  45 8B CF                        mov r9d, r15d
007DC262  33 D2                           xor edx, edx
007DC264  48 8B CF                        mov rcx, rdi
007DC267  E8 E0 67 1D 00                  call 0x1409b2a4c
007DC26C  48 8B CF                        mov rcx, rdi
007DC26F  8B D8                           mov ebx, eax
007DC271  E8 6E D6 07 00                  call 0x1408598e4
007DC276  85 DB                           test ebx, ebx
007DC278  79 07                           jns 0x1407dc281
007DC27A  44 88 3D E2 D7 7F 00            mov byte ptr [rip + 0x7fd7e2], r15b
007DC281  F7 87 10 10 00 00 00 80 00 00   test dword ptr [rdi + 0x1010], 0x8000
007DC28B  75 3C                           jne 0x1407dc2c9
007DC28D  39 74 24 64                     cmp dword ptr [rsp + 0x64], esi
007DC291  74 66                           je 0x1407dc2f9
007DC293  44 39 64 24 60                  cmp dword ptr [rsp + 0x60], r12d
007DC298  75 2F                           jne 0x1407dc2c9
007DC29A  48 B8 14 00 00 00 80 F7 FF FF   movabs rax, 0xfffff78000000014
007DC2A4  48 8B 00                        mov rax, qword ptr [rax]
007DC2A7  48 8B 4F 40                     mov rcx, qword ptr [rdi + 0x40]
007DC2AB  48 89 41 0C                     mov qword ptr [rcx + 0xc], rax
007DC2AF  48 8B CF                        mov rcx, rdi
007DC2B2  E8 DD D5 07 00                  call 0x140859894
007DC2B7  48 8B CF                        mov rcx, rdi
007DC2BA  E8 D1 FB 09 00                  call 0x14087be90
007DC2BF  48 8B CF                        mov rcx, rdi
007DC2C2  E8 1D D6 07 00                  call 0x1408598e4
007DC2C7  EB 30                           jmp 0x1407dc2f9
007DC2C9  48 8B CF                        mov rcx, rdi
007DC2CC  E8 63 D9 3E 00                  call 0x140bc9c34
007DC2D1  E8 AE D7 3E 00                  call 0x140bc9a84
007DC2D6  48 8D 55 D0                     lea rdx, [rbp - 0x30]
007DC2DA  48 8B CF                        mov rcx, rdi
007DC2DD  E8 CE 21 01 00                  call 0x1407ee4b0
007DC2E2  8B D8                           mov ebx, eax
007DC2E4  85 C0                           test eax, eax
007DC2E6  0F 88 CB 01 00 00               js 0x1407dc4b7
007DC2EC  E8 43 D8 3E 00                  call 0x140bc9b34
007DC2F1  48 8B CF                        mov rcx, rdi
007DC2F4  E8 57 D9 3E 00                  call 0x140bc9c50
007DC2F9  48 8B 5D 98                     mov rbx, qword ptr [rbp - 0x68]
007DC2FD  39 9F 88 00 00 00               cmp dword ptr [rdi + 0x88], ebx
007DC303  74 4D                           je 0x1407dc352
007DC305  4C 8D 6F 58                     lea r13, [rdi + 0x58]
007DC309  44 8B E6                        mov r12d, esi
007DC30C  41 39 75 00                     cmp dword ptr [r13], esi
007DC310  76 29                           jbe 0x1407dc33b
007DC312  44 8B C3                        mov r8d, ebx
007DC315  41 8B D4                        mov edx, r12d
007DC318  49 8B CD                        mov rcx, r13
007DC31B  E8 E0 54 C7 FF                  call 0x140451800
007DC320  84 C0                           test al, al
007DC322  75 0E                           jne 0x1407dc332
007DC324  44 8B C3                        mov r8d, ebx
007DC327  41 8B D4                        mov edx, r12d
007DC32A  49 8B CD                        mov rcx, r13
007DC32D  E8 DE 52 C0 FF                  call 0x1403e1610
007DC332  44 03 E3                        add r12d, ebx
007DC335  45 3B 65 00                     cmp r12d, dword ptr [r13]
007DC339  72 D7                           jb 0x1407dc312
007DC33B  49 8B CD                        mov rcx, r13
007DC33E  E8 2D 7C C5 FF                  call 0x140433f70
007DC343  89 47 68                        mov dword ptr [rdi + 0x68], eax
007DC346  41 BC 02 00 00 00               mov r12d, 2
007DC34C  89 9F 88 00 00 00               mov dword ptr [rdi + 0x88], ebx
007DC352  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
007DC356  44 8B 6C 24 64                  mov r13d, dword ptr [rsp + 0x64]
007DC35B  39 B0 FC 0F 00 00               cmp dword ptr [rax + 0xffc], esi
007DC361  75 05                           jne 0x1407dc368
007DC363  45 85 ED                        test r13d, r13d
007DC366  74 0F                           je 0x1407dc377
007DC368  48 8D 4F 58                     lea rcx, [rdi + 0x58]
007DC36C  E8 1F 61 B8 FF                  call 0x140362490
007DC371  8B 47 58                        mov eax, dword ptr [rdi + 0x58]
007DC374  89 47 68                        mov dword ptr [rdi + 0x68], eax
007DC377  48 8B CF                        mov rcx, rdi
007DC37A  E8 B5 D8 3E 00                  call 0x140bc9c34
007DC37F  E8 00 D7 3E 00                  call 0x140bc9a84
007DC384  E8 2B 36 07 00                  call 0x14084f9b4
007DC389  48 8B CF                        mov rcx, rdi
007DC38C  E8 D7 AD 1D 00                  call 0x1409b7168
007DC391  8B D8                           mov ebx, eax
007DC393  E8 EC D6 3E 00                  call 0x140bc9a84
007DC398  85 DB                           test ebx, ebx
007DC39A  0F 88 10 01 00 00               js 0x1407dc4b0
007DC3A0  48 8B CF                        mov rcx, rdi
007DC3A3  E8 08 BB 00 00                  call 0x1407e7eb0
007DC3A8  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
007DC3AC  39 B0 FC 0F 00 00               cmp dword ptr [rax + 0xffc], esi
007DC3B2  75 05                           jne 0x1407dc3b9
007DC3B4  45 85 ED                        test r13d, r13d
007DC3B7  74 3A                           je 0x1407dc3f3
007DC3B9  E8 A2 EA D1 FF                  call 0x1404fae60
007DC3BE  84 C0                           test al, al
007DC3C0  75 0D                           jne 0x1407dc3cf
007DC3C2  BA 0C 00 00 00                  mov edx, 0xc
007DC3C7  48 8B CF                        mov rcx, rdi
007DC3CA  E8 F1 79 1D 00                  call 0x1409b3dc0
007DC3CF  E8 60 D7 3E 00                  call 0x140bc9b34
007DC3D4  48 8B CF                        mov rcx, rdi
007DC3D7  E8 74 D8 3E 00                  call 0x140bc9c50
007DC3DC  48 8B 47 40                     mov rax, qword ptr [rdi + 0x40]
007DC3E0  48 8B CF                        mov rcx, rdi
007DC3E3  89 B0 FC 0F 00 00               mov dword ptr [rax + 0xffc], esi
007DC3E9  E8 46 D8 3E 00                  call 0x140bc9c34
007DC3EE  E8 91 D6 3E 00                  call 0x140bc9a84
007DC3F3  40 38 35 69 D6 7F 00            cmp byte ptr [rip + 0x7fd669], sil
007DC3FA  74 05                           je 0x1407dc401
007DC3FC  E8 DF 95 00 00                  call 0x1407e59e0
007DC401  E8 2E D7 3E 00                  call 0x140bc9b34
007DC406  48 8B CF                        mov rcx, rdi
007DC409  E8 42 D8 3E 00                  call 0x140bc9c50
007DC40E  8B 9F A0 00 00 00               mov ebx, dword ptr [rdi + 0xa0]
007DC414  48 8B CF                        mov rcx, rdi
007DC417  8B C3                           mov eax, ebx
007DC419  0F BA F0 0B                     btr eax, 0xb
007DC41D  89 87 A0 00 00 00               mov dword ptr [rdi + 0xa0], eax
007DC423  E8 0C D8 3E 00                  call 0x140bc9c34
007DC428  E8 57 D6 3E 00                  call 0x140bc9a84
007DC42D  48 8B 0D 7C A6 7E 00            mov rcx, qword ptr [rip + 0x7ea67c]
007DC434  4C 8D 85 80 01 00 00            lea r8, [rbp + 0x180]
007DC43B  33 D2                           xor edx, edx
007DC43D  E8 DE A3 A3 FF                  call 0x140216820
007DC442  C1 EB 0B                        shr ebx, 0xb
007DC445  48 8B CF                        mov rcx, rdi
007DC448  41 22 DF                        and bl, r15b
007DC44B  8A D3                           mov dl, bl
007DC44D  E8 AE 02 0A 00                  call 0x14087c700
007DC452  33 D2                           xor edx, edx
007DC454  48 8D 8D 80 01 00 00            lea rcx, [rbp + 0x180]
007DC45B  E8 D0 B8 A3 FF                  call 0x140217d30
007DC460  48 8B 8F 38 10 00 00            mov rcx, qword ptr [rdi + 0x1038]
007DC467  83 8F 10 10 00 00 08            or dword ptr [rdi + 0x1010], 8
007DC46E  48 85 C9                        test rcx, rcx
007DC471  74 1F                           je 0x1407dc492
007DC473  4C 8B C1                        mov r8, rcx
007DC476  48 8D 15 D3 54 1D 00            lea rdx, [rip + 0x1d54d3]
007DC47D  48 8B 49 38                     mov rcx, qword ptr [rcx + 0x38]
007DC481  E8 5A 1C D2 FF                  call 0x1404fe0e0
007DC486  48 8B 8F 38 10 00 00            mov rcx, qword ptr [rdi + 0x1038]
007DC48D  E8 D6 26 2E 00                  call 0x140abeb68
007DC492  48 8B 5D B0                     mov rbx, qword ptr [rbp - 0x50]
007DC496  41 BD 00 10 00 00               mov r13d, 0x1000
007DC49C  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
007DC4A1  48 8D 3D 58 B7 71 00            lea rdi, [rip + 0x71b758]
007DC4A8  48 8B 00                        mov rax, qword ptr [rax]
007DC4AB  E9 7B FA FF FF                  jmp 0x1407dbf2b
007DC4B0  BE 60 00 00 00                  mov esi, 0x60
007DC4B5  EB 41                           jmp 0x1407dc4f8
007DC4B7  48 8D 45 D0                     lea rax, [rbp - 0x30]
007DC4BB  BE 48 00 00 00                  mov esi, 0x48
007DC4C0  48 89 47 38                     mov qword ptr [rdi + 0x38], rax
007DC4C4  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007DC4C8  48 89 7D D0                     mov qword ptr [rbp - 0x30], rdi
007DC4CC  EB 40                           jmp 0x1407dc50e
007DC4CE  48 8D 45 D0                     lea rax, [rbp - 0x30]
007DC4D2  BE 28 00 00 00                  mov esi, 0x28
007DC4D7  48 89 47 38                     mov qword ptr [rdi + 0x38], rax
007DC4DB  48 8D 4D D0                     lea rcx, [rbp - 0x30]
007DC4DF  48 89 7D D0                     mov qword ptr [rbp - 0x30], rdi
007DC4E3  EB 29                           jmp 0x1407dc50e
007DC4E5  BE 30 00 00 00                  mov esi, 0x30
007DC4EA  EB 0C                           jmp 0x1407dc4f8
007DC4EC  BE 20 00 00 00                  mov esi, 0x20
007DC4F1  EB 09                           jmp 0x1407dc4fc
007DC4F3  BE 10 00 00 00                  mov esi, 0x10
007DC4F8  48 8D 45 D0                     lea rax, [rbp - 0x30]
007DC4FC  48 89 47 38                     mov qword ptr [rdi + 0x38], rax
007DC500  41 BE 15 00 00 00               mov r14d, 0x15
007DC506  48 89 7D D0                     mov qword ptr [rbp - 0x30], rdi
007DC50A  48 8B 4F 38                     mov rcx, qword ptr [rdi + 0x38]
007DC50E  44 8B CB                        mov r9d, ebx
007DC511  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
007DC515  45 8B C6                        mov r8d, r14d
007DC518  33 D2                           xor edx, edx
007DC51A  E8 35 2A C9 FF                  call 0x14046ef54
007DC51F  48 8D 44 24 50                  lea rax, [rsp + 0x50]
007DC524  44 88 3D DA BA 7F 00            mov byte ptr [rip + 0x7fbada], r15b
007DC52B  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
007DC530  4C 8D 4C 24 70                  lea r9, [rsp + 0x70]
007DC535  48 8D 45 84                     lea rax, [rbp - 0x7c]
007DC539  45 8B C7                        mov r8d, r15d
007DC53C  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007DC541  41 8B D7                        mov edx, r15d
007DC544  B9 18 02 00 C0                  mov ecx, 0xc0000218
007DC549  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
007DC54E  E8 CD 7F 28 00                  call 0x140a64520
007DC553  48 63 C3                        movsxd rax, ebx
007DC556  4C 8B CF                        mov r9, rdi
007DC559  4D 8B C7                        mov r8, r15
007DC55C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
007DC561  49 8B D4                        mov rdx, r12
007DC564  B9 74 00 00 00                  mov ecx, 0x74
007DC569  E8 F2 10 D2 FF                  call 0x1404fd660
007DC56E  CC                              int3
007DC56F  33 D2                           xor edx, edx
007DC571  48 8B CB                        mov rcx, rbx
007DC574  E8 F7 62 3A 00                  call 0x140b82870
007DC579  48 8B 8D B0 01 00 00            mov rcx, qword ptr [rbp + 0x1b0]
007DC580  48 33 CC                        xor rcx, rsp
007DC583  E8 B8 00 ED FF                  call 0x1406ac640
007DC588  4C 8D 9C 24 C0 02 00 00         lea r11, [rsp + 0x2c0]
007DC590  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
007DC594  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
007DC598  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
007DC59C  49 8B E3                        mov rsp, r11
007DC59F  41 5F                           pop r15
007DC5A1  41 5E                           pop r14
007DC5A3  41 5D                           pop r13
007DC5A5  41 5C                           pop r12
007DC5A7  5D                              pop rbp
007DC5A8  C3                              ret
007DC5A9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpMountPreloadedHives(__int64 a1, int a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m26C;
    unsigned int v_stack_m270;
    unsigned __int64 v_stack_m278;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m280;
    unsigned int v_stack_m284;
    unsigned int v_stack_m288;
    unsigned __int64 v_stack_m290;
    unsigned __int16 v_stack_m296;
    unsigned __int64 v_stack_m298;
    unsigned __int64 v_stack_m2A0;
    unsigned __int64 v_stack_m2A8;
    unsigned __int64 v_stack_m2B0;
    unsigned __int64 v_stack_m2B8;
    unsigned __int64 v_stack_m2C0;
    unsigned __int64 v_stack_m2C8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 24) = v_rdi;
    v_rsp = (v_rsp) - (704);
    result = (*(unsigned __int64 *)(v_rip + 6482171)) ^ (v_rsp);
    *(unsigned __int64 *)(v_rsp - 488 + 432) = result;
    v_rsi = 0;
    v_stack_m270 = 0;
    a2 = 0;
    *(unsigned int *)(v_rsp - 488 - 124) = 0;
    *(unsigned __int64 *)(v_rsp - 488 - 88) = 0;
    v_stack_m298 = v_xmm0;
    result = memset(v_rsp - 488 - 48, a2, 432, a4);
    v_stack_m26C = 0;
    *(unsigned __int64 *)(v_rsp - 488 - 112) = 0;
    *(unsigned int *)(v_rsp - 488 - 128) = 0;
    *(unsigned __int64 *)(v_rsp - 488 - 96) = 0;
    v_stack_m288 = 0;
    *(unsigned __int64 *)(v_rsp - 488 + 384) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 488 - 120) = 0;
    *(unsigned __int64 *)(v_rsp - 488 + 400) = v_xmm0;
    v_stack_m280 = 0;
    *(unsigned __int64 *)(v_rsp - 488 + 416) = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 488 - 104) = 0;
    result = ExAllocatePool2(256, (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))), (unsigned int)(0x62534D43ULL), a4);
    *(unsigned __int64 *)(v_rsp - 488 - 80) = result;
    if (result == 0) {
        a4 = 0;
        v_stack_m2C8 = 0xFFFFFFFFC000009AULL;
        a2 = v_rsi + 2;
        a1 = v_rsi + 116;
        a3 = v_rsi + 1;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    result = CmpLockRegistryExclusive(a1, a2, a3, a4);
    goto loc_007DBF0C;
loc_007DBF02:
loc_007DBF0C:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7453959))) != (v_rip + 7453952)) goto loc_007DBF02;
    result = CmpUnlockRegistry(a1, a2, a3, a4);
loc_007DBF2B:
    v_stack_m278 = *(unsigned __int64 *)(v_rip + 7453923);
    if ((*(unsigned __int64 *)(v_rip + 7453923)) == (v_rip + 7453952)) goto loc_007DC56F;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 160))))) & (0x1000000ULL));
    v_stack_m284 = (unsigned int)(a1);
    if (((1) & ((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 160))))) != 0) goto loc_007DC49C;
    v_stack_m298 = v_xmm0;
    v_stack_m296 = (unsigned __int16)((unsigned int)(0x1000ULL));
    v_stack_m290 = result;
    result = CmpQueryHiveRedirectionFileList(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 1856, v_stack_m298, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_007DBF8F;
    if (v_stack_m298 != ((unsigned __int16)(1 + 1))) goto loc_007DC03C;
loc_007DBF8F:
    v_stack_m298 = v_xmm0;
    v_stack_m296 = (unsigned __int16)((unsigned int)(0x1000ULL));
    v_stack_m290 = result;
    if ((((unsigned int)((unsigned int)(0x1000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 160))))) == 0) goto loc_007DBFF2;
    result = HalAdjustResourceList(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 1856, v_stack_m298, a3, a4);
    result = PsGetServerSiloGlobals(result, v_stack_m298, a3, a4);
    v_stack_m280 = (unsigned __int16)(*(unsigned __int16 *)(*(unsigned __int64 *)(result + 1240)));
    result = RtlAppendUnicodeToString(v_stack_m298, v_rip + 3298271, a3, a4);
    result = RtlAppendUnicodeToString(v_stack_m298, v_stack_m280, a3, a4);
    goto loc_007DC021;
loc_007DBFF2:
    if (condition_is_above_or_equal) goto loc_007DC014;
    result = SyspartGetSystemPartition(result, (unsigned int)((unsigned int)((unsigned int)(0x1000ULL))), v_stack_m270, a4);
    if (sign_flag) goto loc_007DC4F8;
    goto loc_007DC02B;
loc_007DC014:
    if (condition_is_above_or_equal) goto loc_007DC02B;
loc_007DC021:
    result = RtlAppendUnicodeToString(v_stack_m298, v_rip + 3299647, v_stack_m270, a4);
loc_007DC02B:
    result = RtlAppendUnicodeToString(v_stack_m298, *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 1832), v_stack_m270, a4);
loc_007DC03C:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 1832), a2, v_stack_m270, a4);
    v_stack_m2A0 = v_rsp - 488 - 48;
    v_stack_m2A8 = 0;
    v_stack_m2B0 = 0;
    v_stack_m2B8 = v_rsp - 488 - 104;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 1824) = v_xmm0;
    v_stack_m2C0 = 0;
    a2 = 0;
    v_stack_m2C8 = 7;
    *(unsigned __int16 *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 1826) = 0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 1832) = 0;
    result = CmpOpenHiveFile(v_stack_m298, a2, v_rsp - 488 - 120, v_stack_m288);
    if (sign_flag) goto loc_007DC4F3;
    v_r13 = (unsigned int)((unsigned int)(1 + 1));
    if (v_stack_m288 == ((unsigned int)(1 + 1))) { v_r13 = 18; }
    v_stack_m2A0 = v_rsp - 488 - 48;
    v_stack_m2A8 = 0;
    v_stack_m2B0 = 0;
    v_stack_m2B8 = 0;
    v_stack_m2C0 = 0;
    v_stack_m2C8 = (unsigned int)(v_r13);
    result = CmpOpenHiveFile(v_stack_m298, 4, v_rsp - 488 - 112, v_stack_m26C);
    if (sign_flag) goto loc_007DC4EC;
    v_stack_m2A0 = v_rsp - 488 - 48;
    v_stack_m2A8 = 0;
    v_stack_m2B0 = 0;
    v_stack_m2B8 = 0;
    v_stack_m2C0 = 0;
    v_stack_m2C8 = (unsigned int)(v_r13);
    result = CmpOpenHiveFile(v_stack_m298, 5, v_rsp - 488 - 96, v_rsp - 488 - 128);
    if (sign_flag) goto loc_007DC4E5;
    result = CmpGetFileSize(*(unsigned __int64 *)(v_rsp - 488 - 120), v_rsp - 488 - 88, v_rsp - 488 - 96, v_rsp - 488 - 128);
    if (sign_flag) goto loc_007DC4CE;
    result = CmpGetFileSize(*(unsigned __int64 *)(v_rsp - 488 - 112), v_rsp - 488 - 72, v_rsp - 488 - 96, v_rsp - 488 - 128);
    if (sign_flag) {
        a3 = (unsigned int)(result);
        a2 = 4;
        result = CmpLogFailureToGetFileSize(*(unsigned __int64 *)(v_rsp - 488 - 112), a2, a3, v_rsp - 488 - 128);
        result = v_rsp - 488 - 48;
        v_stack_m2C8 = 43;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 56) = result;
        a1 = v_rsp - 488 - 48;
        a4 = (unsigned int)((unsigned int)((unsigned int)(result)));
        *(unsigned __int64 *)(v_rsp - 488 - 48) = *(unsigned __int64 *)(v_rip + 7453923) - 1624;
        a3 = (unsigned int)(1 + 21);
        a2 = 1;
        result = SetFailureLocation(a1, a2, a3, a4);
        *(unsigned __int64 *)(v_rsp - 488 - 72) = 0;
    }
    result = CmpGetFileSize(*(unsigned __int64 *)(v_rsp - 488 - 96), v_rsp - 488 - 64, a3, a4);
    if (sign_flag) {
        a3 = (unsigned int)(result);
        a2 = 5;
        result = CmpLogFailureToGetFileSize(*(unsigned __int64 *)(v_rsp - 488 - 96), a2, a3, a4);
        result = v_rsp - 488 - 48;
        v_stack_m2C8 = 45;
        *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 56) = result;
        a1 = v_rsp - 488 - 48;
        a4 = (unsigned int)((unsigned int)((unsigned int)(result)));
        *(unsigned __int64 *)(v_rsp - 488 - 48) = *(unsigned __int64 *)(v_rip + 7453923) - 1624;
        a3 = (unsigned int)(1 + 21);
        a2 = 1;
        result = SetFailureLocation(a1, a2, a3, a4);
        *(unsigned __int64 *)(v_rsp - 488 - 64) = 0;
    }
    result = CmpBecomeActiveFlusherAndReconciler(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, a3, a4);
    result = CmpLockRegistry(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, a3, a4);
    result = HvLockHiveFlusherExclusive(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, a3, a4);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 1544) = *(unsigned __int64 *)(v_rsp - 488 - 120);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 1576) = *(unsigned __int64 *)(v_rsp - 488 - 112);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 1800) = *(unsigned __int64 *)(v_rsp - 488 - 88);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 1584) = *(unsigned __int64 *)(v_rsp - 488 - 96);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 1808) = v_xmm0;
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 280))) + (0x1000ULL));
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 188) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rsp - 488 - 100)));
    result = HvLockHiveWriter(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, a3, a4);
    a2 = 0;
    result = CmpDoFileSetSizeEx(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, (unsigned int)((unsigned int)(v_rbx)), 1);
    result = HvUnlockHiveWriter(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, (unsigned int)((unsigned int)(v_rbx)), 1);
    if (sign_flag) {
        *(unsigned __int8 *)(v_rip + 8378338) = 1;
    }
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 4112)) & (0x8000ULL)) != 0) goto loc_007DC2C9;
    if (v_stack_m284 == 0) goto loc_007DC2F9;
    if (v_stack_m288 != ((unsigned int)(1 + 1))) goto loc_007DC2C9;
    *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 64) + 12) = *(unsigned __int64 *)(result);
    result = HvLockHiveWriter(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, (unsigned int)((unsigned int)(v_rbx)), 1);
    result = HvCheckAndUpdateHiveBackupTimeStamp(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, (unsigned int)((unsigned int)(v_rbx)), 1);
    result = HvUnlockHiveWriter(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, (unsigned int)((unsigned int)(v_rbx)), 1);
    goto loc_007DC2F9;
loc_007DC2C9:
    result = HvUnlockHiveFlusherExclusive(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, (unsigned int)((unsigned int)(v_rbx)), 1);
    result = CmpUnlockRegistry(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, (unsigned int)((unsigned int)(v_rbx)), 1);
    result = CmpRecoverFlushProtocolStateFromFiles(*(unsigned __int64 *)(v_rip + 7453923) - 1624, v_rsp - 488 - 48, (unsigned int)((unsigned int)(v_rbx)), 1);
    if (sign_flag) goto loc_007DC4B7;
    result = CmpLockRegistry(*(unsigned __int64 *)(v_rip + 7453923) - 1624, v_rsp - 488 - 48, (unsigned int)((unsigned int)(v_rbx)), 1);
    result = HvLockHiveFlusherExclusive(*(unsigned __int64 *)(v_rip + 7453923) - 1624, v_rsp - 488 - 48, (unsigned int)((unsigned int)(v_rbx)), 1);
loc_007DC2F9:
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 136)) == ((unsigned int)(*(unsigned __int64 *)(v_rsp - 488 - 104)))) goto loc_007DC352;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 88)) <= 0) goto loc_007DC33B;
loc_007DC312:
    result = RtlAreBitsClear(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 88, 0, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 488 - 104))), 1);
    if ((unsigned __int8)(result) == 0) {
        a3 = (unsigned int)(*(unsigned __int64 *)(v_rsp - 488 - 104));
        a2 = 0;
        a1 = *(unsigned __int64 *)(v_rip + 7453923) - 1624 + 88;
        result = RtlSetBits(a1, a2, a3, 1);
    }
    v_r12 = (unsigned int)((0) + ((unsigned int)(*(unsigned __int64 *)(v_rsp - 488 - 104))));
    if (((unsigned int)(v_r12)) < (*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 88))) goto loc_007DC312;
loc_007DC33B:
    result = RtlNumberOfSetBits(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 88, a2, a3, 1);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 104) = (unsigned int)(result);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 136) = (unsigned int)(*(unsigned __int64 *)(v_rsp - 488 - 104));
loc_007DC352:
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 64) + 4092)) != 0) goto loc_007DC368;
    result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 64);
    if ((unsigned int)((unsigned int)(v_stack_m284)) != 0) {
        a1 = *(unsigned __int64 *)(v_rip + 7453923) - 1624 + 88;
        result = RtlSetAllBits(a1, a2, a3, 1);
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 88);
        *(unsigned int *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 104) = (unsigned int)(result);
    }
    result = HvUnlockHiveFlusherExclusive(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, a3, 1);
    result = CmpUnlockRegistry(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, a3, 1);
    result = CmpLockRegistryExclusive(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, a3, 1);
    result = HvpDropPagedBins(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, a3, 1);
    result = CmpUnlockRegistry(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, a3, 1);
    if (sign_flag) goto loc_007DC4B0;
    result = CmpFinishBeingActiveFlusherAndReconciler(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, a3, 1);
    if ((*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 64) + 4092)) != 0) goto loc_007DC3B9;
    if ((unsigned int)((unsigned int)(v_stack_m284)) == 0) goto loc_007DC3F3;
loc_007DC3B9:
    result = ExIsSoftBoot(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, a3, 1);
    if ((unsigned __int8)(result) == 0) {
        a2 = 12;
        a1 = *(unsigned __int64 *)(v_rip + 7453923) - 1624;
        result = CmpFlushHive(a1, a2, a3, 1);
    }
    result = CmpLockRegistry(a1, a2, a3, 1);
    result = HvLockHiveFlusherExclusive(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, a3, 1);
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 64) + 4092) = 0;
    result = HvUnlockHiveFlusherExclusive(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, a3, 1);
    result = CmpUnlockRegistry(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, a3, 1);
loc_007DC3F3:
    if ((*(unsigned __int8 *)(v_rip + 8377961)) != 0) {
        result = CmpDiskFullWarning(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, a3, 1);
    }
    result = CmpLockRegistry(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, a3, 1);
    result = HvLockHiveFlusherExclusive(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, a3, 1);
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 160) = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 160)))));
    result = HvUnlockHiveFlusherExclusive(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, a3, 1);
    result = CmpUnlockRegistry(*(unsigned __int64 *)(v_rip + 7453923) - 1624, a2, a3, 1);
    a2 = 0;
    result = KiStackAttachProcess(*(unsigned __int64 *)(v_rip + 8300156), a2, v_rsp - 488 + 384, 1);
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 160))) >> (11));
    v_rbx = (unsigned __int8)((v_rbx) & (1));
    result = CmpInitCmRM(*(unsigned __int64 *)(v_rip + 7453923) - 1624, (unsigned __int8)(v_rbx), v_rsp - 488 + 384, 1);
    a2 = 0;
    result = KiUnstackDetachProcess(v_rsp - 488 + 384, a2, v_rsp - 488 + 384, 1);
    if (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 4152) != 0) {
        a3 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 4152);
        a2 = v_rip + 1922259;
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 4152) + 56);
        result = TmEnableCallbacks(a1, a2, a3, 1);
        a1 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 7453923) - 1624 + 4152);
        result = CmRmFinalizeRecovery(a1, a2, a3, 1);
    }
loc_007DC49C:
    goto loc_007DBF2B;
loc_007DC4B0:
    goto loc_007DC4F8;
loc_007DC4B7:
    *(unsigned __int64 *)(v_rip + 7452504 + 56) = v_rsp - 488 - 48;
    *(unsigned __int64 *)(v_rsp - 488 - 48) = v_rip + 7452504;
    goto loc_007DC50E;
loc_007DC4CE:
    *(unsigned __int64 *)(v_rip + 7452504 + 56) = v_rsp - 488 - 48;
    *(unsigned __int64 *)(v_rsp - 488 - 48) = v_rip + 7452504;
    goto loc_007DC50E;
loc_007DC4E5:
    goto loc_007DC4F8;
loc_007DC4EC:
    goto loc_007DC4FC;
loc_007DC4F3:
loc_007DC4F8:
loc_007DC4FC:
    *(unsigned __int64 *)(v_rip + 7452504 + 56) = v_rsp - 488 - 48;
    *(unsigned __int64 *)(v_rsp - 488 - 48) = v_rip + 7452504;
loc_007DC50E:
    v_stack_m2C8 = 16;
    a2 = 0;
    result = SetFailureLocation(*(unsigned __int64 *)(v_rip + 7452504 + 56), a2, 21, (unsigned int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 488 - 80))));
    *(unsigned __int8 *)(v_rip + 8370906) = 1;
    v_stack_m278 = v_stack_m298;
    v_stack_m2C0 = v_rsp - 488 - 124;
    v_stack_m2C8 = 1;
    result = ExRaiseHardError((unsigned int)(0xC0000218ULL), 1, 1, v_stack_m278);
    v_stack_m2C8 = (int)((unsigned int)(*(unsigned __int64 *)(v_rsp - 488 - 80)));
    result = KeBugCheckEx(116, 2, 1, v_rip + 7452504);
loc_007DC56F:
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(v_rsp - 488 - 80), a2, 1, v_rip + 7452504);
    a1 = (*(unsigned __int64 *)(v_rsp - 488 + 432)) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, 1, v_rip + 7452504);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpMountPreloadedHives(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m26C;
    uint32_t v_stack_m270;
    uint64_t v_stack_m278;
    uint64_t v_stack_m28;
    uint32_t v_stack_m280;
    uint32_t v_stack_m284;
    uint32_t v_stack_m288;
    uint64_t v_stack_m290;
    uint16_t v_stack_m296;
    uint64_t v_stack_m298;
    uint64_t v_stack_m2A0;
    uint64_t v_stack_m2A8;
    uint64_t v_stack_m2B0;
    uint64_t v_stack_m2B8;
    uint64_t v_stack_m2C0;
    uint64_t v_stack_m2C8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rsi;
    *(uint64_t *)(local_rsp + 0x18) = local_rdi;
    local_rsp = (local_rsp) - (704);
    result = (*(uint64_t *)(v_rip + 0x62E8FB)) ^ (local_rsp);
    *(uint64_t *)(local_rsp - 0x1E8 + 0x1B0) = result;
    local_rsi = 0;
    v_stack_m270 = 0;
    Arg2 = 0;
    *(uint32_t *)(local_rsp - 0x1E8 - 0x7C) = 0;
    *(uint64_t *)(local_rsp - 0x1E8 - 0x58) = 0;
    v_stack_m298 = v_xmm0;
    result = memset(local_rsp - 488 - 48, Arg2, 432, Arg4);
    v_stack_m26C = 0;
    *(uint64_t *)(local_rsp - 0x1E8 - 0x70) = 0;
    *(uint32_t *)(local_rsp - 0x1E8 - 0x80) = 0;
    *(uint64_t *)(local_rsp - 0x1E8 - 0x60) = 0;
    v_stack_m288 = 0;
    *(uint64_t *)(local_rsp - 0x1E8 + 0x180) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x1E8 - 0x78) = 0;
    *(uint64_t *)(local_rsp - 0x1E8 + 0x190) = v_xmm0;
    v_stack_m280 = 0;
    *(uint64_t *)(local_rsp - 0x1E8 + 0x1A0) = v_xmm0;
    *(uint64_t *)(local_rsp - 0x1E8 - 0x68) = 0;
    result = ExAllocatePool2(256, (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))), (uint32_t)(0x62534D43ULL), Arg4);
    *(uint64_t *)(local_rsp - 0x1E8 - 0x50) = result;
    if (result == 0) {
        Arg4 = 0;
        v_stack_m2C8 = 0xFFFFFFFFC000009AULL;
        Arg2 = local_rsi + 2;
        Arg1 = local_rsi + 116;
        Arg3 = local_rsi + 1;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    result = CmpLockRegistryExclusive(Arg1, Arg2, Arg3, Arg4);
    goto loc_007DBF0C;
loc_007DBF02:
loc_007DBF0C:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x71BD07))) != (v_rip + 7453952)) goto loc_007DBF02;
    result = CmpUnlockRegistry(Arg1, Arg2, Arg3, Arg4);
loc_007DBF2B:
    v_stack_m278 = *(uint64_t *)(v_rip + 0x71BCE3);
    if ((*(uint64_t *)(v_rip + 0x71BCE3)) == (v_rip + 7453952)) goto loc_007DC56F;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0xA0))))) & (0x1000000ULL));
    v_stack_m284 = (uint32_t)(Arg1);
    if (((1) & ((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0xA0))))) != 0) goto loc_007DC49C;
    v_stack_m298 = v_xmm0;
    v_stack_m296 = (uint16_t)((uint32_t)(0x1000ULL));
    v_stack_m290 = result;
    result = CmpQueryHiveRedirectionFileList(*(uint64_t *)(v_rip + 0x71BCE3) - 1624 + 1856, v_stack_m298, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_007DBF8F;
    if (v_stack_m298 != ((uint16_t)(1 + 1))) goto loc_007DC03C;
loc_007DBF8F:
    v_stack_m298 = v_xmm0;
    v_stack_m296 = (uint16_t)((uint32_t)(0x1000ULL));
    v_stack_m290 = result;
    if ((((uint32_t)((uint32_t)(0x1000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0xA0))))) == 0) goto loc_007DBFF2;
    result = HalAdjustResourceList(*(uint64_t *)(v_rip + 0x71BCE3) - 1624 + 1856, v_stack_m298, Arg3, Arg4);
    result = PsGetServerSiloGlobals(result, v_stack_m298, Arg3, Arg4);
    v_stack_m280 = (uint16_t)(*(uint16_t *)(*(uint64_t *)(result + 0x4D8)));
    result = RtlAppendUnicodeToString(v_stack_m298, v_rip + 3298271, Arg3, Arg4);
    result = RtlAppendUnicodeToString(v_stack_m298, v_stack_m280, Arg3, Arg4);
    goto loc_007DC021;
loc_007DBFF2:
    if (condition_is_above_or_equal) goto loc_007DC014;
    result = SyspartGetSystemPartition(result, (uint32_t)((uint32_t)((uint32_t)(0x1000ULL))), v_stack_m270, Arg4);
    if (sign_flag) goto loc_007DC4F8;
    goto loc_007DC02B;
loc_007DC014:
    if (condition_is_above_or_equal) goto loc_007DC02B;
loc_007DC021:
    result = RtlAppendUnicodeToString(v_stack_m298, v_rip + 3299647, v_stack_m270, Arg4);
loc_007DC02B:
    result = RtlAppendUnicodeToString(v_stack_m298, *(uint64_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x728), v_stack_m270, Arg4);
loc_007DC03C:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x728), Arg2, v_stack_m270, Arg4);
    v_stack_m2A0 = local_rsp - 488 - 48;
    v_stack_m2A8 = 0;
    v_stack_m2B0 = 0;
    v_stack_m2B8 = local_rsp - 488 - 104;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x720) = v_xmm0;
    v_stack_m2C0 = 0;
    Arg2 = 0;
    v_stack_m2C8 = 7;
    *(uint16_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x722) = 0;
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x728) = 0;
    result = CmpOpenHiveFile(v_stack_m298, Arg2, local_rsp - 488 - 120, v_stack_m288);
    if (sign_flag) goto loc_007DC4F3;
    local_r13 = (uint32_t)((uint32_t)(1 + 1));
    if (v_stack_m288 == ((uint32_t)(1 + 1))) { local_r13 = 18; }
    v_stack_m2A0 = local_rsp - 488 - 48;
    v_stack_m2A8 = 0;
    v_stack_m2B0 = 0;
    v_stack_m2B8 = 0;
    v_stack_m2C0 = 0;
    v_stack_m2C8 = (uint32_t)(local_r13);
    result = CmpOpenHiveFile(v_stack_m298, 4, local_rsp - 488 - 112, v_stack_m26C);
    if (sign_flag) goto loc_007DC4EC;
    v_stack_m2A0 = local_rsp - 488 - 48;
    v_stack_m2A8 = 0;
    v_stack_m2B0 = 0;
    v_stack_m2B8 = 0;
    v_stack_m2C0 = 0;
    v_stack_m2C8 = (uint32_t)(local_r13);
    result = CmpOpenHiveFile(v_stack_m298, 5, local_rsp - 488 - 96, local_rsp - 488 - 128);
    if (sign_flag) goto loc_007DC4E5;
    result = CmpGetFileSize(*(uint64_t *)(local_rsp - 0x1E8 - 0x78), local_rsp - 488 - 88, local_rsp - 488 - 96, local_rsp - 488 - 128);
    if (sign_flag) goto loc_007DC4CE;
    result = CmpGetFileSize(*(uint64_t *)(local_rsp - 0x1E8 - 0x70), local_rsp - 488 - 72, local_rsp - 488 - 96, local_rsp - 488 - 128);
    if (sign_flag) {
        Arg3 = (uint32_t)(result);
        Arg2 = 4;
        result = CmpLogFailureToGetFileSize(*(uint64_t *)(local_rsp - 0x1E8 - 0x70), Arg2, Arg3, local_rsp - 488 - 128);
        result = local_rsp - 488 - 48;
        v_stack_m2C8 = 43;
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x38) = result;
        Arg1 = local_rsp - 488 - 48;
        Arg4 = (uint32_t)((uint32_t)((uint32_t)(result)));
        *(uint64_t *)(local_rsp - 0x1E8 - 0x30) = *(uint64_t *)(v_rip + 0x71BCE3) - 1624;
        Arg3 = (uint32_t)(1 + 21);
        Arg2 = 1;
        result = SetFailureLocation(Arg1, Arg2, Arg3, Arg4);
        *(uint64_t *)(local_rsp - 0x1E8 - 0x48) = 0;
    }
    result = CmpGetFileSize(*(uint64_t *)(local_rsp - 0x1E8 - 0x60), local_rsp - 488 - 64, Arg3, Arg4);
    if (sign_flag) {
        Arg3 = (uint32_t)(result);
        Arg2 = 5;
        result = CmpLogFailureToGetFileSize(*(uint64_t *)(local_rsp - 0x1E8 - 0x60), Arg2, Arg3, Arg4);
        result = local_rsp - 488 - 48;
        v_stack_m2C8 = 45;
        *(uint64_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x38) = result;
        Arg1 = local_rsp - 488 - 48;
        Arg4 = (uint32_t)((uint32_t)((uint32_t)(result)));
        *(uint64_t *)(local_rsp - 0x1E8 - 0x30) = *(uint64_t *)(v_rip + 0x71BCE3) - 1624;
        Arg3 = (uint32_t)(1 + 21);
        Arg2 = 1;
        result = SetFailureLocation(Arg1, Arg2, Arg3, Arg4);
        *(uint64_t *)(local_rsp - 0x1E8 - 0x40) = 0;
    }
    result = CmpBecomeActiveFlusherAndReconciler(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, Arg3, Arg4);
    result = CmpLockRegistry(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, Arg3, Arg4);
    result = HvLockHiveFlusherExclusive(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, Arg3, Arg4);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x608) = *(uint64_t *)(local_rsp - 0x1E8 - 0x78);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x628) = *(uint64_t *)(local_rsp - 0x1E8 - 0x70);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x708) = *(uint64_t *)(local_rsp - 0x1E8 - 0x58);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x630) = *(uint64_t *)(local_rsp - 0x1E8 - 0x60);
    *(uint64_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x710) = v_xmm0;
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x118))) + (0x1000ULL));
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0xBC) = (uint32_t)((uint32_t)(*(uint32_t *)(local_rsp - 0x1E8 - 0x64)));
    result = HvLockHiveWriter(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, Arg3, Arg4);
    Arg2 = 0;
    result = CmpDoFileSetSizeEx(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, (uint32_t)((uint32_t)(local_rbx)), 1);
    result = HvUnlockHiveWriter(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, (uint32_t)((uint32_t)(local_rbx)), 1);
    if (sign_flag) {
        *(uint8_t *)(v_rip + 0x7FD7E2) = 1;
    }
    if (((*(uint32_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x1010)) & (0x8000ULL)) != 0) goto loc_007DC2C9;
    if (v_stack_m284 == 0) goto loc_007DC2F9;
    if (v_stack_m288 != ((uint32_t)(1 + 1))) goto loc_007DC2C9;
    *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x40) + 0xC) = *(uint64_t *)(result);
    result = HvLockHiveWriter(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, (uint32_t)((uint32_t)(local_rbx)), 1);
    result = HvCheckAndUpdateHiveBackupTimeStamp(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, (uint32_t)((uint32_t)(local_rbx)), 1);
    result = HvUnlockHiveWriter(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, (uint32_t)((uint32_t)(local_rbx)), 1);
    goto loc_007DC2F9;
loc_007DC2C9:
    result = HvUnlockHiveFlusherExclusive(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, (uint32_t)((uint32_t)(local_rbx)), 1);
    result = CmpUnlockRegistry(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, (uint32_t)((uint32_t)(local_rbx)), 1);
    result = CmpRecoverFlushProtocolStateFromFiles(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, local_rsp - 488 - 48, (uint32_t)((uint32_t)(local_rbx)), 1);
    if (sign_flag) goto loc_007DC4B7;
    result = CmpLockRegistry(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, local_rsp - 488 - 48, (uint32_t)((uint32_t)(local_rbx)), 1);
    result = HvLockHiveFlusherExclusive(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, local_rsp - 488 - 48, (uint32_t)((uint32_t)(local_rbx)), 1);
loc_007DC2F9:
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x88)) == ((uint32_t)(*(uint64_t *)(local_rsp - 0x1E8 - 0x68)))) goto loc_007DC352;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x58)) <= 0) goto loc_007DC33B;
loc_007DC312:
    result = RtlAreBitsClear(*(uint64_t *)(v_rip + 0x71BCE3) - 1624 + 88, 0, (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x1E8 - 0x68))), 1);
    if ((uint8_t)(result) == 0) {
        Arg3 = (uint32_t)(*(uint64_t *)(local_rsp - 0x1E8 - 0x68));
        Arg2 = 0;
        Arg1 = *(uint64_t *)(v_rip + 0x71BCE3) - 1624 + 88;
        result = RtlSetBits(Arg1, Arg2, Arg3, 1);
    }
    local_r12 = (uint32_t)((0) + ((uint32_t)(*(uint64_t *)(local_rsp - 0x1E8 - 0x68))));
    if (((uint32_t)(local_r12)) < (*(uint32_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x58))) goto loc_007DC312;
loc_007DC33B:
    result = RtlNumberOfSetBits(*(uint64_t *)(v_rip + 0x71BCE3) - 1624 + 88, Arg2, Arg3, 1);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x68) = (uint32_t)(result);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x88) = (uint32_t)(*(uint64_t *)(local_rsp - 0x1E8 - 0x68));
loc_007DC352:
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x40) + 0xFFC)) != 0) goto loc_007DC368;
    result = *(uint64_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x40);
    if ((uint32_t)((uint32_t)(v_stack_m284)) != 0) {
        Arg1 = *(uint64_t *)(v_rip + 0x71BCE3) - 1624 + 88;
        result = RtlSetAllBits(Arg1, Arg2, Arg3, 1);
        result = *(uint32_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x58);
        *(uint32_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x68) = (uint32_t)(result);
    }
    result = HvUnlockHiveFlusherExclusive(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, Arg3, 1);
    result = CmpUnlockRegistry(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, Arg3, 1);
    result = CmpLockRegistryExclusive(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, Arg3, 1);
    result = HvpDropPagedBins(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, Arg3, 1);
    result = CmpUnlockRegistry(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, Arg3, 1);
    if (sign_flag) goto loc_007DC4B0;
    result = CmpFinishBeingActiveFlusherAndReconciler(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, Arg3, 1);
    if ((*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x40) + 0xFFC)) != 0) goto loc_007DC3B9;
    if ((uint32_t)((uint32_t)(v_stack_m284)) == 0) goto loc_007DC3F3;
loc_007DC3B9:
    result = ExIsSoftBoot(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, Arg3, 1);
    if ((uint8_t)(result) == 0) {
        Arg2 = 12;
        Arg1 = *(uint64_t *)(v_rip + 0x71BCE3) - 1624;
        result = CmpFlushHive(Arg1, Arg2, Arg3, 1);
    }
    result = CmpLockRegistry(Arg1, Arg2, Arg3, 1);
    result = HvLockHiveFlusherExclusive(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, Arg3, 1);
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x40) + 0xFFC) = 0;
    result = HvUnlockHiveFlusherExclusive(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, Arg3, 1);
    result = CmpUnlockRegistry(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, Arg3, 1);
loc_007DC3F3:
    if ((*(uint8_t *)(v_rip + 0x7FD669)) != 0) {
        result = CmpDiskFullWarning(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, Arg3, 1);
    }
    result = CmpLockRegistry(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, Arg3, 1);
    result = HvLockHiveFlusherExclusive(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, Arg3, 1);
    *(uint32_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0xA0) = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0xA0)))));
    result = HvUnlockHiveFlusherExclusive(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, Arg3, 1);
    result = CmpUnlockRegistry(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, Arg2, Arg3, 1);
    Arg2 = 0;
    result = KiStackAttachProcess(*(uint64_t *)(v_rip + 0x7EA67C), Arg2, local_rsp - 488 + 384, 1);
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0xA0))) >> (11));
    local_rbx = (uint8_t)((local_rbx) & (1));
    result = CmpInitCmRM(*(uint64_t *)(v_rip + 0x71BCE3) - 1624, (uint8_t)(local_rbx), local_rsp - 488 + 384, 1);
    Arg2 = 0;
    result = KiUnstackDetachProcess(local_rsp - 488 + 384, Arg2, local_rsp - 488 + 384, 1);
    if (*(uint64_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x1038) != 0) {
        Arg3 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x1038);
        Arg2 = v_rip + 1922259;
        Arg1 = *(uint64_t *)(*(uint64_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x1038) + 0x38);
        result = TmEnableCallbacks(Arg1, Arg2, Arg3, 1);
        Arg1 = *(uint64_t *)(*(uint64_t *)(v_rip + 0x71BCE3) - 0x658 + 0x1038);
        result = CmRmFinalizeRecovery(Arg1, Arg2, Arg3, 1);
    }
loc_007DC49C:
    goto loc_007DBF2B;
loc_007DC4B0:
    goto loc_007DC4F8;
loc_007DC4B7:
    *(uint64_t *)(v_rip + 0x71B758 + 0x38) = local_rsp - 488 - 48;
    *(uint64_t *)(local_rsp - 0x1E8 - 0x30) = v_rip + 7452504;
    goto loc_007DC50E;
loc_007DC4CE:
    *(uint64_t *)(v_rip + 0x71B758 + 0x38) = local_rsp - 488 - 48;
    *(uint64_t *)(local_rsp - 0x1E8 - 0x30) = v_rip + 7452504;
    goto loc_007DC50E;
loc_007DC4E5:
    goto loc_007DC4F8;
loc_007DC4EC:
    goto loc_007DC4FC;
loc_007DC4F3:
loc_007DC4F8:
loc_007DC4FC:
    *(uint64_t *)(v_rip + 0x71B758 + 0x38) = local_rsp - 488 - 48;
    *(uint64_t *)(local_rsp - 0x1E8 - 0x30) = v_rip + 7452504;
loc_007DC50E:
    v_stack_m2C8 = 16;
    Arg2 = 0;
    result = SetFailureLocation(*(uint64_t *)(v_rip + 0x71B758 + 0x38), Arg2, 21, (uint32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x1E8 - 0x50))));
    *(uint8_t *)(v_rip + 0x7FBADA) = 1;
    v_stack_m278 = v_stack_m298;
    v_stack_m2C0 = local_rsp - 488 - 124;
    v_stack_m2C8 = 1;
    result = ExRaiseHardError((uint32_t)(0xC0000218ULL), 1, 1, v_stack_m278);
    v_stack_m2C8 = (int32_t)((uint32_t)(*(uint64_t *)(local_rsp - 0x1E8 - 0x50)));
    result = KeBugCheckEx(116, 2, 1, v_rip + 7452504);
loc_007DC56F:
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(local_rsp - 0x1E8 - 0x50), Arg2, 1, v_rip + 7452504);
    Arg1 = (*(uint64_t *)(local_rsp - 0x1E8 + 0x1B0)) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, 1, v_rip + 7452504);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007DBE18&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
