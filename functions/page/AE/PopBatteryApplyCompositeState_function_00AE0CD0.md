# PopBatteryApplyCompositeState

- RVA: `0x00AE0CD0`–`0x00AE1448` (길이 `1,912` bytes)
- VA: `0x0000000140AE0CD0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000AB7D4`
- 디코드: `447`개 명령, `1,912/1,912` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **45**; 고유 호출 대상: **38**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **76**

### Outgoing calls
- `0x00AE0D1D` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00AE0D24` → [PopUpdateAcDcState](../../text/4B/PopUpdateAcDcState_function_004B8C68.md) (function, `0x004B8C68`)
- `0x00AE0D32` → [PopBatteryUpdateAlarms](../91/PopBatteryUpdateAlarms_function_00910058.md) (function, `0x00910058`)
- `0x00AE0D3C` → [PopSetNotificationWork](../../text/48/PopSetNotificationWork_function_00482C78.md) (function, `0x00482C78`)
- `0x00AE0D43` → [PopRecordAcDcState](../AB/PopRecordAcDcState_function_00AB96DC.md) (function, `0x00AB96DC`)
- `0x00AE0D4D` → [PopUpdateSystemIdleContext](../91/PopUpdateSystemIdleContext_function_00911BB4.md) (function, `0x00911BB4`)
- `0x00AE0D52` → [PopInitilizeAcDcSettings](../../text/48/PopInitilizeAcDcSettings_function_004828D0.md) (function, `0x004828D0`)
- `0x00AE0D57` → [PpmProfileAcDcUpdate](../A5/PpmProfileAcDcUpdate_function_00A5280C.md) (function, `0x00A5280C`)
- `0x00AE0D88` → [PopSetPowerSettingValueAcDc](../91/PopSetPowerSettingValueAcDc_function_00914D6C.md) (function, `0x00914D6C`)
- `0x00AE0DDB` → [PopDiagTraceBatteryCountChange](../76/PopDiagTraceBatteryCountChange_function_00760B54.md) (function, `0x00760B54`)
- `0x00AE0DE4` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00AE0DF2` → [PopBatteryCheckCompositeCapacity](../A8/PopBatteryCheckCompositeCapacity_function_00A84358.md) (function, `0x00A84358`)
- `0x00AE0E11` → [PopSetNotificationWork](../../text/48/PopSetNotificationWork_function_00482C78.md) (function, `0x00482C78`)
- `0x00AE0E81` → [PopSetPowerSettingValueAcDc](../91/PopSetPowerSettingValueAcDc_function_00914D6C.md) (function, `0x00914D6C`)
- `0x00AE0E89` → [PopRecordBatteryPercentage](../AC/PopRecordBatteryPercentage_function_00AC5EB4.md) (function, `0x00AC5EB4`)
- `0x00AE0EE1` → [PopSqmBatteryUpdate](../AC/PopSqmBatteryUpdate_function_00AC1794.md) (function, `0x00AC1794`)
- `0x00AE0EF2` → [PopBatteryTracePercentageRemaining](../AD/PopBatteryTracePercentageRemaining_function_00AD8B24.md) (function, `0x00AD8B24`)
- `0x00AE0F05` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x00AE0F53` → [DbgPrintEx](../../text/35/DbgPrintEx_function_00359290.md) (function, `0x00359290`)
- `0x00AE10AD` → [PopCheckCachedPowerSourceStateUpdates](../76/PopCheckCachedPowerSourceStateUpdates_function_0076728C.md) (function, `0x0076728C`)
- `0x00AE10B2` → [PopAccountCbEnergyChange](PopAccountCbEnergyChange_function_00AE0680.md) (function, `0x00AE0680`)
- `0x00AE10B9` → [PopBatteryTraceSystemBatteryStatus](../../text/4E/PopBatteryTraceSystemBatteryStatus_function_004E93D8.md) (function, `0x004E93D8`)
- `0x00AE10C5` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)
- `0x00AE10D3` → [PopRecalculateCBTriggerLevels](PopRecalculateCBTriggerLevels_function_00AE3018.md) (function, `0x00AE3018`)
- `0x00AE10F7` → [PopBatteryCheckTriggerAllBatteries](../A7/PopBatteryCheckTriggerAllBatteries_function_00A77B2C.md) (function, `0x00A77B2C`)
- `0x00AE110F` → [PopGetPolicyWorker](../../text/48/PopGetPolicyWorker_function_00482D24.md) (function, `0x00482D24`)
- `0x00AE1114` → [PopCheckForWork](../../text/48/PopCheckForWork_function_00482CAC.md) (function, `0x00482CAC`)
- `0x00AE1119` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00AE116A` → [PopBatteryCheckTrigger](../A7/PopBatteryCheckTrigger_function_00A77AF4.md) (function, `0x00A77AF4`)
- `0x00AE11A3` → [PopDiagTraceBatteryAlarmStatus](../76/PopDiagTraceBatteryAlarmStatus_function_00760804.md) (function, `0x00760804`)
- `0x00AE11E3` → [PopDiagTraceBatteryTriggerMet](../76/PopDiagTraceBatteryTriggerMet_function_00760C60.md) (function, `0x00760C60`)
- `0x00AE1229` → [PopExecutePowerAction](../75/PopExecutePowerAction_function_0075E6B4.md) (function, `0x0075E6B4`)
- `0x00AE125D` → [PopDiagTraceBatteryTriggerFlags](../A8/PopDiagTraceBatteryTriggerFlags_function_00A84A50.md) (function, `0x00A84A50`)
- `0x00AE12B0` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (function, `0x006B0D10`)
- `0x00AE1310` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (function, `0x00427304`)
- `0x00AE1343` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00AE137D` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (function, `0x0042EAA0`)
- `0x00AE13C6` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (function, `0x004260E0`)
- `0x00AE13D8` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x00AE13F5` → [PopBsdHandleRequest](../../text/4B/PopBsdHandleRequest_function_004B27A0.md) (function, `0x004B27A0`)
- `0x00AE1401` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)
- `0x00AE140B` → [PopTracePowerReconfig](../../text/4D/PopTracePowerReconfig_function_004D09AC.md) (function, `0x004D09AC`)
- `0x00AE1410` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00AE1418` → [PopEsQueueStateEvaluation](../A4/PopEsQueueStateEvaluation_function_00A4A398.md) (function, `0x00A4A398`)
- `0x00AE1427` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PopBatteryWorker](PopBatteryWorker_function_00AE1650.md) at `0x00AE2310`

### Static image references
- `0x00AE0CEC` → RVA `0x00E0A740` (`.data`; read)
- `0x00AE0D61` → RVA `0x00E678B8` (`.data`; write)
- `0x00AE0D6C` → RVA `0x00F0C038` (`.data`; read)
- `0x00AE0D75` → RVA `0x00F0C034` (`.data`; read)
- `0x00AE0D81` → RVA `0x0001E238` (`.rdata`; read)
- `0x00AE0D8D` → RVA `0x00F0C040` (`.data`; read)
- `0x00AE0DC0` → RVA `0x00E0B830` (`.data`; read)
- `0x00AE0DD5` → RVA `0x00E0B830` (`.data`; write)
- `0x00AE0DF9` → RVA `0x00F0C060` (`.data`; read)
- `0x00AE0E16` → RVA `0x00F0C038` (`.data`; write)
- `0x00AE0E2B` → RVA `0x00F0C070` (`.data`; read)
- `0x00AE0E37` → RVA `0x00F0C080` (`.data`; write)
- `0x00AE0E42` → RVA `0x00F0C088` (`.data`; write)
- `0x00AE0E48` → RVA `0x00F0C08C` (`.data`; write)
- `0x00AE0E58` → RVA `0x00F0C20C` (`.data`; read)
- `0x00AE0E6F` → RVA `0x00024A68` (`.rdata`; read)
- `0x00AE0EBD` → RVA `0x00F0C210` (`.data`; read)
- `0x00AE0EF7` → RVA `0x00F0C210` (`.data`; write)
- `0x00AE0EFE` → RVA `0x00F0C238` (`.data`; read)
- `0x00AE0F0A` → RVA `0x00F0C08C` (`.data`; read)
- `0x00AE0F10` → RVA `0x00B02830` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE0F35` → RVA `0x00F0C06C` (`.data`; read)
- `0x00AE0F3F` → RVA `0x00F0C068` (`.data`; read)
- `0x00AE0F49` → RVA `0x00F0C064` (`.data`; read)
- `0x00AE0F58` → RVA `0x00F0C0B4` (`.data`; read)
- `0x00AE0F67` → RVA `0x00F0C248` (`.data`; read)
- `0x00AE0F6E` → RVA `0x00F0C24F` (`.data`; write)
- `0x00AE0F79` → RVA `0x00F0C268` (`.data`; write)
- `0x00AE0F86` → RVA `0x00F0C258` (`.data`; read)
- `0x00AE0F8D` → RVA `0x00F0C26C` (`.data`; write)
- `0x00AE0F93` → RVA `0x00F0C270` (`.data`; write)
- `0x00AE0F99` → RVA `0x00F0C274` (`.data`; write)
- `0x00AE0F9F` → RVA `0x00F0C278` (`.data`; write)
- `0x00AE0FA5` → RVA `0x00F0C27C` (`.data`; write)
- `0x00AE0FAB` → RVA `0x00F0C280` (`.data`; write)
- `0x00AE0FB1` → RVA `0x00F0C248` (`.data`; write)
- `0x00AE0FBF` → RVA `0x00F0C249` (`.data`; write)
- `0x00AE0FCE` → RVA `0x00F0C24A` (`.data`; write)
- `0x00AE0FD7` → RVA `0x00F0C208` (`.data`; read)
- `0x00AE0FDE` → RVA `0x00F0C284` (`.data`; write)
- `0x00AE0FEA` → RVA `0x00F0C0A0` (`.data`; read)
- `0x00AE0FF0` → RVA `0x00F0C250` (`.data`; write)
- `0x00AE0FFC` → RVA `0x00F0C254` (`.data`; write)
- `0x00AE1008` → RVA `0x00F0C258` (`.data`; write)
- `0x00AE1014` → RVA `0x00F0C25C` (`.data`; write)
- `0x00AE101A` → RVA `0x00F0C0A4` (`.data`; read)
- `0x00AE1020` → RVA `0x00F0C260` (`.data`; write)
- `0x00AE1026` → RVA `0x00F0C0A8` (`.data`; read)
- `0x00AE102C` → RVA `0x00F0C264` (`.data`; write)
- `0x00AE1032` → RVA `0x00F0C074` (`.data`; read)
- `0x00AE103E` → RVA `0x00F0C078` (`.data`; read)
- `0x00AE104A` → RVA `0x00F0C07C` (`.data`; read)
- `0x00AE1056` → RVA `0x00F0C080` (`.data`; read)
- `0x00AE1068` → RVA `0x00F0C288` (`.data`; write)
- `0x00AE106E` → RVA `0x00F0C24B` (`.data`; write)
- `0x00AE1074` → RVA `0x00F0C2D8` (`.data`; read)
- `0x00AE10D8` → RVA `0x00F0C09C` (`.data`; read)
- `0x00AE10DF` → RVA `0x00F0C188` (`.data`; read)
- `0x00AE1100` → RVA `0x00F0C18C` (`.data`; read)
- `0x00AE1124` → RVA `0x00000000` (`image boundary/outside`; read)
- `0x00AE1181` → RVA `0x00F0CE68` (`.data`; read)
- `0x00AE11ED` → RVA `0x00F0C180` (`.data`; read)
- `0x00AE127F` → RVA `0x00F0C0B8` (`.data`; read)
- `0x00AE129B` → RVA `0x00020A70` (`.rdata`; read)
- `0x00AE12B5` → RVA `0x00E07748` (`.data`; read)
- `0x00AE12D2` → RVA `0x00B028E0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE12E0` → RVA `0x00B028C0` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE12EE` → RVA `0x00B02920` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE12FA` → RVA `0x00B02900` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE1301` → RVA `0x00B02960` (` ?? ::NNGAKEGL::`string'`; read)
- `0x00AE1321` → RVA `0x0004C7FD` (`.rdata`; read)
- `0x00AE138A` → RVA `0x0004C841` (`.rdata`; read)
- `0x00AE13CB` → RVA `0x00F0F1E0` (`.data`; read)
- `0x00AE13D2` → RVA `0x00F0C0B8` (`.data`; write)
- `0x00AE13DD` → RVA `0x00E6741A` (`.data`; read)
- `0x00AE13EF` → RVA `0x00E6741A` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **24**
  - `0x00AE0D1D` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`PAGE` → `PAGELK`)
  - `0x00AE0D24` → [PopUpdateAcDcState](../../text/4B/PopUpdateAcDcState_function_004B8C68.md) (`PAGE` → `.text`)
  - `0x00AE0D3C` → [PopSetNotificationWork](../../text/48/PopSetNotificationWork_function_00482C78.md) (`PAGE` → `.text`)
  - `0x00AE0D52` → [PopInitilizeAcDcSettings](../../text/48/PopInitilizeAcDcSettings_function_004828D0.md) (`PAGE` → `.text`)
  - `0x00AE0DE4` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`PAGE` → `PAGELK`)
  - `0x00AE0E11` → [PopSetNotificationWork](../../text/48/PopSetNotificationWork_function_00482C78.md) (`PAGE` → `.text`)
  - `0x00AE0F05` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x00AE0F53` → [DbgPrintEx](../../text/35/DbgPrintEx_function_00359290.md) (`PAGE` → `.text`)
  - `0x00AE10B9` → [PopBatteryTraceSystemBatteryStatus](../../text/4E/PopBatteryTraceSystemBatteryStatus_function_004E93D8.md) (`PAGE` → `.text`)
  - `0x00AE10C5` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
  - `0x00AE110F` → [PopGetPolicyWorker](../../text/48/PopGetPolicyWorker_function_00482D24.md) (`PAGE` → `.text`)
  - `0x00AE1114` → [PopCheckForWork](../../text/48/PopCheckForWork_function_00482CAC.md) (`PAGE` → `.text`)
  - `0x00AE1119` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`PAGE` → `PAGELK`)
  - `0x00AE12B0` → [ZwUpdateWnfStateData](../../text/6B/ZwUpdateWnfStateData_function_006B0D10.md) (`PAGE` → `.text`)
  - `0x00AE1310` → [tlgCreate1Sz_char](../../text/42/tlgCreate1Sz_char_function_00427304.md) (`PAGE` → `.text`)
  - `0x00AE1343` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00AE137D` → [tlgKeywordOn](../../text/42/tlgKeywordOn_function_0042EAA0.md) (`PAGE` → `.text`)
  - `0x00AE13C6` → [tlgWriteTransfer_EtwWriteTransfer](../../text/42/tlgWriteTransfer_EtwWriteTransfer_function_004260E0.md) (`PAGE` → `.text`)
  - `0x00AE13D8` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x00AE13F5` → [PopBsdHandleRequest](../../text/4B/PopBsdHandleRequest_function_004B27A0.md) (`PAGE` → `.text`)
  - `0x00AE1401` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
  - `0x00AE140B` → [PopTracePowerReconfig](../../text/4D/PopTracePowerReconfig_function_004D09AC.md) (`PAGE` → `.text`)
  - `0x00AE1410` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`PAGE` → `PAGELK`)
  - `0x00AE1427` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AE0CD0  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00AE0CD5  55                              push rbp
00AE0CD6  56                              push rsi
00AE0CD7  57                              push rdi
00AE0CD8  41 54                           push r12
00AE0CDA  41 55                           push r13
00AE0CDC  41 56                           push r14
00AE0CDE  41 57                           push r15
00AE0CE0  48 8D 6C 24 D9                  lea rbp, [rsp - 0x27]
00AE0CE5  48 81 EC A0 00 00 00            sub rsp, 0xa0
00AE0CEC  48 8B 05 4D 9A 32 00            mov rax, qword ptr [rip + 0x329a4d]
00AE0CF3  48 33 C4                        xor rax, rsp
00AE0CF6  48 89 45 17                     mov qword ptr [rbp + 0x17], rax
00AE0CFA  8B 19                           mov ebx, dword ptr [rcx]
00AE0CFC  45 33 E4                        xor r12d, r12d
00AE0CFF  F7 D3                           not ebx
00AE0D01  44 89 65 CB                     mov dword ptr [rbp - 0x35], r12d
00AE0D05  45 8B F8                        mov r15d, r8d
00AE0D08  44 89 65 D3                     mov dword ptr [rbp - 0x2d], r12d
00AE0D0C  8B F2                           mov esi, edx
00AE0D0E  44 88 65 C7                     mov byte ptr [rbp - 0x39], r12b
00AE0D12  45 8D 6C 24 01                  lea r13d, [r12 + 1]
00AE0D17  48 8B F9                        mov rdi, rcx
00AE0D1A  41 23 DD                        and ebx, r13d
00AE0D1D  E8 9E 76 09 00                  call 0x140b783c0
00AE0D22  8B CB                           mov ecx, ebx
00AE0D24  E8 3F 7F 9D FF                  call 0x1404b8c68
00AE0D29  84 C0                           test al, al
00AE0D2B  74 3F                           je 0x140ae0d6c
00AE0D2D  33 D2                           xor edx, edx
00AE0D2F  41 8A CD                        mov cl, r13b
00AE0D32  E8 21 F3 E2 FF                  call 0x140910058
00AE0D37  41 8D 4C 24 04                  lea ecx, [r12 + 4]
00AE0D3C  E8 37 1F 9A FF                  call 0x140482c78
00AE0D41  8B CB                           mov ecx, ebx
00AE0D43  E8 94 89 FD FF                  call 0x140ab96dc
00AE0D48  41 8D 4C 24 02                  lea ecx, [r12 + 2]
00AE0D4D  E8 62 0E E3 FF                  call 0x140911bb4
00AE0D52  E8 79 1B 9A FF                  call 0x1404828d0
00AE0D57  E8 B0 1A F7 FF                  call 0x140a5280c
00AE0D5C  41 3B DD                        cmp ebx, r13d
00AE0D5F  75 07                           jne 0x140ae0d68
00AE0D61  4C 89 25 50 6B 38 00            mov qword ptr [rip + 0x386b50], r12
00AE0D68  44 88 6D C7                     mov byte ptr [rbp - 0x39], r13b
00AE0D6C  44 38 25 C5 B2 42 00            cmp byte ptr [rip + 0x42b2c5], r12b
00AE0D73  74 6F                           je 0x140ae0de4
00AE0D75  4C 8D 05 B8 B2 42 00            lea r8, [rip + 0x42b2b8]
00AE0D7C  BA 04 00 00 00                  mov edx, 4
00AE0D81  48 8D 0D B0 D4 53 FF            lea rcx, [rip - 0xac2b50]
00AE0D88  E8 DF 3F E3 FF                  call 0x140914d6c
00AE0D8D  48 8B 05 AC B2 42 00            mov rax, qword ptr [rip + 0x42b2ac]
00AE0D94  4C 8D 0D A5 B2 42 00            lea r9, [rip + 0x42b2a5]
00AE0D9B  45 8B C4                        mov r8d, r12d
00AE0D9E  41 8B D4                        mov edx, r12d
00AE0DA1  EB 18                           jmp 0x140ae0dbb
00AE0DA3  8B 48 68                        mov ecx, dword ptr [rax + 0x68]
00AE0DA6  83 F9 02                        cmp ecx, 2
00AE0DA9  74 0A                           je 0x140ae0db5
00AE0DAB  83 F9 04                        cmp ecx, 4
00AE0DAE  75 08                           jne 0x140ae0db8
00AE0DB0  45 03 C5                        add r8d, r13d
00AE0DB3  EB 03                           jmp 0x140ae0db8
00AE0DB5  41 03 D5                        add edx, r13d
00AE0DB8  48 8B 00                        mov rax, qword ptr [rax]
00AE0DBB  49 3B C1                        cmp rax, r9
00AE0DBE  75 E3                           jne 0x140ae0da3
00AE0DC0  8B 05 6A AA 32 00               mov eax, dword ptr [rip + 0x32aa6a]
00AE0DC6  8B 0D 68 B2 42 00               mov ecx, dword ptr [rip + 0x42b268]
00AE0DCC  83 F8 FF                        cmp eax, -1
00AE0DCF  74 04                           je 0x140ae0dd5
00AE0DD1  3B C1                           cmp eax, ecx
00AE0DD3  74 0B                           je 0x140ae0de0
00AE0DD5  89 0D 55 AA 32 00               mov dword ptr [rip + 0x32aa55], ecx
00AE0DDB  E8 74 FD C7 FF                  call 0x140760b54
00AE0DE0  44 88 6D C7                     mov byte ptr [rbp - 0x39], r13b
00AE0DE4  E8 27 76 09 00                  call 0x140b78410
00AE0DE9  4C 8D 45 CB                     lea r8, [rbp - 0x35]
00AE0DED  8B D3                           mov edx, ebx
00AE0DEF  48 8B CF                        mov rcx, rdi
00AE0DF2  E8 61 35 FA FF                  call 0x140a84358
00AE0DF7  8B 07                           mov eax, dword ptr [rdi]
00AE0DF9  33 05 61 B2 42 00               xor eax, dword ptr [rip + 0x42b261]
00AE0DFF  A8 0F                           test al, 0xf
00AE0E01  75 09                           jne 0x140ae0e0c
00AE0E03  44 38 25 2E B2 42 00            cmp byte ptr [rip + 0x42b22e], r12b
00AE0E0A  74 11                           je 0x140ae0e1d
00AE0E0C  B9 08 00 00 00                  mov ecx, 8
00AE0E11  E8 62 1E 9A FF                  call 0x140482c78
00AE0E16  44 88 25 1B B2 42 00            mov byte ptr [rip + 0x42b21b], r12b
00AE0E1D  0F 10 07                        movups xmm0, xmmword ptr [rdi]
00AE0E20  0F 11 05 39 B2 42 00            movups xmmword ptr [rip + 0x42b239], xmm0
00AE0E27  0F 10 4F 10                     movups xmm1, xmmword ptr [rdi + 0x10]
00AE0E2B  0F 11 0D 3E B2 42 00            movups xmmword ptr [rip + 0x42b23e], xmm1
00AE0E32  F2 0F 10 47 20                  movsd xmm0, qword ptr [rdi + 0x20]
00AE0E37  F2 0F 11 05 41 B2 42 00         movsd qword ptr [rip + 0x42b241], xmm0
00AE0E3F  8B 47 28                        mov eax, dword ptr [rdi + 0x28]
00AE0E42  89 05 40 B2 42 00               mov dword ptr [rip + 0x42b240], eax
00AE0E48  89 35 3E B2 42 00               mov dword ptr [rip + 0x42b23e], esi
00AE0E4E  44 39 65 CB                     cmp dword ptr [rbp - 0x35], r12d
00AE0E52  0F 84 A6 00 00 00               je 0x140ae0efe
00AE0E58  8B 0D AE B3 42 00               mov ecx, dword ptr [rip + 0x42b3ae]
00AE0E5E  4C 8D 45 CF                     lea r8, [rbp - 0x31]
00AE0E62  81 C1 F4 01 00 00               add ecx, 0x1f4
00AE0E68  B8 D3 4D 62 10                  mov eax, 0x10624dd3
00AE0E6D  F7 E1                           mul ecx
00AE0E6F  48 8D 0D F2 3B 54 FF            lea rcx, [rip - 0xabc40e]
00AE0E76  C1 EA 06                        shr edx, 6
00AE0E79  89 55 CF                        mov dword ptr [rbp - 0x31], edx
00AE0E7C  BA 04 00 00 00                  mov edx, 4
00AE0E81  E8 E6 3E E3 FF                  call 0x140914d6c
00AE0E86  8B 4D CF                        mov ecx, dword ptr [rbp - 0x31]
00AE0E89  E8 26 50 FE FF                  call 0x140ac5eb4
00AE0E8E  83 3D 77 B3 42 00 FF            cmp dword ptr [rip + 0x42b377], -1
00AE0E95  41 8B C5                        mov eax, r13d
00AE0E98  48 BE 08 00 00 00 80 F7 FF FF   movabs rsi, 0xfffff78000000008
00AE0EA2  41 8B FC                        mov edi, r12d
00AE0EA5  41 0F 45 C4                     cmovne eax, r12d
00AE0EA9  48 8B 36                        mov rsi, qword ptr [rsi]
00AE0EAC  84 C0                           test al, al
00AE0EAE  75 25                           jne 0x140ae0ed5
00AE0EB0  48 8B CE                        mov rcx, rsi
00AE0EB3  48 B8 4B 59 86 38 D6 C5 6D 34   movabs rax, 0x346dc5d63886594b
00AE0EBD  48 2B 0D 4C B3 42 00            sub rcx, qword ptr [rip + 0x42b34c]
00AE0EC4  48 81 C1 88 13 00 00            add rcx, 0x1388
00AE0ECB  48 F7 E1                        mul rcx
00AE0ECE  48 8B FA                        mov rdi, rdx
00AE0ED1  48 C1 EF 0B                     shr rdi, 0xb
00AE0ED5  8B 55 CB                        mov edx, dword ptr [rbp - 0x35]
00AE0ED8  44 8B CF                        mov r9d, edi
00AE0EDB  8B 4D CF                        mov ecx, dword ptr [rbp - 0x31]
00AE0EDE  44 8B C3                        mov r8d, ebx
00AE0EE1  E8 AE 08 FE FF                  call 0x140ac1794
00AE0EE6  8B 55 CB                        mov edx, dword ptr [rbp - 0x35]
00AE0EE9  44 8B CF                        mov r9d, edi
00AE0EEC  8B 4D CF                        mov ecx, dword ptr [rbp - 0x31]
00AE0EEF  44 8B C3                        mov r8d, ebx
00AE0EF2  E8 2D 7C FF FF                  call 0x140ad8b24
00AE0EF7  48 89 35 12 B3 42 00            mov qword ptr [rip + 0x42b312], rsi
00AE0EFE  48 8D 0D 33 B3 42 00            lea rcx, [rip + 0x42b333]
00AE0F05  E8 3A FC 94 FF                  call 0x140430b44
00AE0F0A  8B 05 7C B1 42 00               mov eax, dword ptr [rip + 0x42b17c]
00AE0F10  4C 8D 05 19 19 02 00            lea r8, [rip + 0x21919]
00AE0F17  44 8B 0D 42 B1 42 00            mov r9d, dword ptr [rip + 0x42b142]
00AE0F1E  83 CB FF                        or ebx, 0xffffffff
00AE0F21  3B C3                           cmp eax, ebx
00AE0F23  BA 03 00 00 00                  mov edx, 3
00AE0F28  B9 92 00 00 00                  mov ecx, 0x92
00AE0F2D  41 0F 44 C4                     cmove eax, r12d
00AE0F31  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
00AE0F35  8B 05 31 B1 42 00               mov eax, dword ptr [rip + 0x42b131]
00AE0F3B  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00AE0F3F  8B 05 23 B1 42 00               mov eax, dword ptr [rip + 0x42b123]
00AE0F45  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
00AE0F49  8B 05 15 B1 42 00               mov eax, dword ptr [rip + 0x42b115]
00AE0F4F  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00AE0F53  E8 38 83 87 FF                  call 0x140359290
00AE0F58  8A 05 56 B1 42 00               mov al, byte ptr [rip + 0x42b156]
00AE0F5E  0F 57 C0                        xorps xmm0, xmm0
00AE0F61  8A 0D F9 B0 42 00               mov cl, byte ptr [rip + 0x42b0f9]
00AE0F67  0F 11 05 DA B2 42 00            movups xmmword ptr [rip + 0x42b2da], xmm0
00AE0F6E  88 05 DB B2 42 00               mov byte ptr [rip + 0x42b2db], al
00AE0F74  8A C1                           mov al, cl
00AE0F76  41 22 C5                        and al, r13b
00AE0F79  89 1D E9 B2 42 00               mov dword ptr [rip + 0x42b2e9], ebx
00AE0F7F  44 39 25 AE B0 42 00            cmp dword ptr [rip + 0x42b0ae], r12d
00AE0F86  0F 11 05 CB B2 42 00            movups xmmword ptr [rip + 0x42b2cb], xmm0
00AE0F8D  89 1D D9 B2 42 00               mov dword ptr [rip + 0x42b2d9], ebx
00AE0F93  89 1D D7 B2 42 00               mov dword ptr [rip + 0x42b2d7], ebx
00AE0F99  89 1D D5 B2 42 00               mov dword ptr [rip + 0x42b2d5], ebx
00AE0F9F  89 1D D3 B2 42 00               mov dword ptr [rip + 0x42b2d3], ebx
00AE0FA5  89 1D D1 B2 42 00               mov dword ptr [rip + 0x42b2d1], ebx
00AE0FAB  89 1D CF B2 42 00               mov dword ptr [rip + 0x42b2cf], ebx
00AE0FB1  88 05 91 B2 42 00               mov byte ptr [rip + 0x42b291], al
00AE0FB7  0F 86 B7 00 00 00               jbe 0x140ae1074
00AE0FBD  8A C1                           mov al, cl
00AE0FBF  44 88 2D 83 B2 42 00            mov byte ptr [rip + 0x42b283], r13b
00AE0FC6  C0 E8 02                        shr al, 2
00AE0FC9  41 22 C5                        and al, r13b
00AE0FCC  D0 E9                           shr cl, 1
00AE0FCE  88 05 76 B2 42 00               mov byte ptr [rip + 0x42b276], al
00AE0FD4  41 22 CD                        and cl, r13b
00AE0FD7  44 38 25 2A B2 42 00            cmp byte ptr [rip + 0x42b22a], r12b
00AE0FDE  44 89 3D 9F B2 42 00            mov dword ptr [rip + 0x42b29f], r15d
00AE0FE5  0F 95 C0                        setne al
00AE0FE8  0A C8                           or cl, al
00AE0FEA  8B 05 B0 B0 42 00               mov eax, dword ptr [rip + 0x42b0b0]
00AE0FF0  89 05 5A B2 42 00               mov dword ptr [rip + 0x42b25a], eax
00AE0FF6  8B 05 68 B0 42 00               mov eax, dword ptr [rip + 0x42b068]
00AE0FFC  89 05 52 B2 42 00               mov dword ptr [rip + 0x42b252], eax
00AE1002  8B 05 64 B0 42 00               mov eax, dword ptr [rip + 0x42b064]
00AE1008  89 05 4A B2 42 00               mov dword ptr [rip + 0x42b24a], eax
00AE100E  8B 05 78 B0 42 00               mov eax, dword ptr [rip + 0x42b078]
00AE1014  89 05 42 B2 42 00               mov dword ptr [rip + 0x42b242], eax
00AE101A  8B 05 84 B0 42 00               mov eax, dword ptr [rip + 0x42b084]
00AE1020  89 05 3A B2 42 00               mov dword ptr [rip + 0x42b23a], eax
00AE1026  8B 05 7C B0 42 00               mov eax, dword ptr [rip + 0x42b07c]
00AE102C  89 05 32 B2 42 00               mov dword ptr [rip + 0x42b232], eax
00AE1032  8B 05 3C B0 42 00               mov eax, dword ptr [rip + 0x42b03c]
00AE1038  89 05 2A B2 42 00               mov dword ptr [rip + 0x42b22a], eax
00AE103E  8B 05 34 B0 42 00               mov eax, dword ptr [rip + 0x42b034]
00AE1044  89 05 22 B2 42 00               mov dword ptr [rip + 0x42b222], eax
00AE104A  8B 05 2C B0 42 00               mov eax, dword ptr [rip + 0x42b02c]
00AE1050  89 05 1A B2 42 00               mov dword ptr [rip + 0x42b21a], eax
00AE1056  8B 05 24 B0 42 00               mov eax, dword ptr [rip + 0x42b024]
00AE105C  89 05 12 B2 42 00               mov dword ptr [rip + 0x42b212], eax
00AE1062  8B 05 00 B0 42 00               mov eax, dword ptr [rip + 0x42b000]
00AE1068  89 05 1A B2 42 00               mov dword ptr [rip + 0x42b21a], eax
00AE106E  88 0D D7 B1 42 00               mov byte ptr [rip + 0x42b1d7], cl
00AE1074  48 8B 15 5D B2 42 00            mov rdx, qword ptr [rip + 0x42b25d]
00AE107B  48 85 D2                        test rdx, rdx
00AE107E  74 2D                           je 0x140ae10ad
00AE1080  44 39 AA 80 00 00 00            cmp dword ptr [rdx + 0x80], r13d
00AE1087  75 24                           jne 0x140ae10ad
00AE1089  8B 82 B8 00 00 00               mov eax, dword ptr [rdx + 0xb8]
00AE108F  89 05 E3 B1 42 00               mov dword ptr [rip + 0x42b1e3], eax
00AE1095  8B 82 BC 00 00 00               mov eax, dword ptr [rdx + 0xbc]
00AE109B  89 05 DB B1 42 00               mov dword ptr [rip + 0x42b1db], eax
00AE10A1  8B 82 C0 00 00 00               mov eax, dword ptr [rdx + 0xc0]
00AE10A7  89 05 D3 B1 42 00               mov dword ptr [rip + 0x42b1d3], eax
00AE10AD  E8 DA 61 C8 FF                  call 0x14076728c
00AE10B2  E8 C9 F5 FF FF                  call 0x140ae0680
00AE10B7  33 C9                           xor ecx, ecx
00AE10B9  E8 1A 83 A0 FF                  call 0x1404e93d8
00AE10BE  48 8D 0D 73 B1 42 00            lea rcx, [rip + 0x42b173]
00AE10C5  E8 F2 EA 7F FF                  call 0x1402dfbbc
00AE10CA  44 39 25 CF AF 42 00            cmp dword ptr [rip + 0x42afcf], r12d
00AE10D1  76 05                           jbe 0x140ae10d8
00AE10D3  E8 40 1F 00 00                  call 0x140ae3018
00AE10D8  44 39 25 BD AF 42 00            cmp dword ptr [rip + 0x42afbd], r12d
00AE10DF  48 8D 05 A2 B0 42 00            lea rax, [rip + 0x42b0a2]
00AE10E6  77 09                           ja 0x140ae10f1
00AE10E8  44 39 25 B1 AF 42 00            cmp dword ptr [rip + 0x42afb1], r12d
00AE10EF  76 28                           jbe 0x140ae1119
00AE10F1  41 8B D5                        mov edx, r13d
00AE10F4  48 8B C8                        mov rcx, rax
00AE10F7  E8 30 6A F9 FF                  call 0x140a77b2c
00AE10FC  84 C0                           test al, al
00AE10FE  74 19                           je 0x140ae1119
00AE1100  8B 05 86 B0 42 00               mov eax, dword ptr [rip + 0x42b086]
00AE1106  A8 02                           test al, 2
00AE1108  75 0F                           jne 0x140ae1119
00AE110A  B9 40 00 00 00                  mov ecx, 0x40
00AE110F  E8 10 1C 9A FF                  call 0x140482d24
00AE1114  E8 93 1B 9A FF                  call 0x140482cac
00AE1119  E8 A2 72 09 00                  call 0x140b783c0
00AE111E  8B 05 10 AF 42 00               mov eax, dword ptr [rip + 0x42af10]
00AE1124  4C 8D 35 D5 EE 51 FF            lea r14, [rip - 0xae112b]
00AE112B  F7 D8                           neg eax
00AE112D  44 89 65 CB                     mov dword ptr [rbp - 0x35], r12d
00AE1131  41 8B FC                        mov edi, r12d
00AE1134  41 8B CC                        mov ecx, r12d
00AE1137  1B DB                           sbb ebx, ebx
00AE1139  41 8B C4                        mov eax, r12d
00AE113C  83 E3 03                        and ebx, 3
00AE113F  44 8B F8                        mov r15d, eax
00AE1142  4D 8D AE 88 C1 F0 00            lea r13, [r14 + 0xf0c188]
00AE1149  8B C1                           mov eax, ecx
00AE114B  45 8B E7                        mov r12d, r15d
00AE114E  48 C1 E0 05                     shl rax, 5
00AE1152  4C 03 E8                        add r13, rax
00AE1155  49 C1 E4 05                     shl r12, 5
00AE1159  48 8D 05 2C B0 42 00            lea rax, [rip + 0x42b02c]
00AE1160  49 8B CD                        mov rcx, r13
00AE1163  4C 03 E0                        add r12, rax
00AE1166  41 8B 34 24                     mov esi, dword ptr [r12]
00AE116A  E8 85 69 F9 FF                  call 0x140a77af4
00AE116F  84 C0                           test al, al
00AE1171  0F 84 CF 00 00 00               je 0x140ae1246
00AE1177  43 39 B4 BE 18 B8 E0 00         cmp dword ptr [r14 + r15*4 + 0xe0b818], esi
00AE117F  74 6A                           je 0x140ae11eb
00AE1181  48 8B 05 E0 BC 42 00            mov rax, qword ptr [rip + 0x42bce0]
00AE1188  49 8D 57 04                     lea rdx, [r15 + 4]
00AE118C  48 8D 14 52                     lea rdx, [rdx + rdx*2]
00AE1190  43 89 B4 BE 18 B8 E0 00         mov dword ptr [r14 + r15*4 + 0xe0b818], esi
00AE1198  4C 8D 45 CB                     lea r8, [rbp - 0x35]
00AE119C  49 8B CD                        mov rcx, r13
00AE119F  48 8D 14 D0                     lea rdx, [rax + rdx*8]
00AE11A3  E8 5C F6 C7 FF                  call 0x140760804
00AE11A8  8B 7D CB                        mov edi, dword ptr [rbp - 0x35]
00AE11AB  44 8B C7                        mov r8d, edi
00AE11AE  8B C7                           mov eax, edi
00AE11B0  49 C1 E0 05                     shl r8, 5
00AE11B4  43 81 BC 30 8C C1 F0 00 80 00 00 00  cmp dword ptr [r8 + r14 + 0xf0c18c], 0x80
00AE11C0  75 29                           jne 0x140ae11eb
00AE11C2  48 83 C0 04                     add rax, 4
00AE11C6  48 8D 0C 40                     lea rcx, [rax + rax*2]
00AE11CA  48 8B 05 97 BC 42 00            mov rax, qword ptr [rip + 0x42bc97]
00AE11D1  48 8D 14 C8                     lea rdx, [rax + rcx*8]
00AE11D5  49 8D 8E 88 C1 F0 00            lea rcx, [r14 + 0xf0c188]
00AE11DC  49 03 C8                        add rcx, r8
00AE11DF  4C 8D 45 CB                     lea r8, [rbp - 0x35]
00AE11E3  E8 78 FA C7 FF                  call 0x140760c60
00AE11E8  8B 7D CB                        mov edi, dword ptr [rbp - 0x35]
00AE11EB  33 F6                           xor esi, esi
00AE11ED  40 38 35 8C AF 42 00            cmp byte ptr [rip + 0x42af8c], sil
00AE11F4  75 38                           jne 0x140ae122e
00AE11F6  4C 8B 0D 6B BC 42 00            mov r9, qword ptr [rip + 0x42bc6b]
00AE11FD  48 8D 15 84 AF 42 00            lea rdx, [rip + 0x42af84]
00AE1204  8B CF                           mov ecx, edi
00AE1206  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
00AE120E  4D 8D 41 68                     lea r8, [r9 + 0x68]
00AE1212  48 8D 04 49                     lea rax, [rcx + rcx*2]
00AE1216  48 C1 E1 05                     shl rcx, 5
00AE121A  45 8B 4C C1 74                  mov r9d, dword ptr [r9 + rax*8 + 0x74]
00AE121F  4D 8D 04 C0                     lea r8, [r8 + rax*8]
00AE1223  48 03 CA                        add rcx, rdx
00AE1226  8D 56 08                        lea edx, [rsi + 8]
00AE1229  E8 86 D4 C7 FF                  call 0x14075e6b4
00AE122E  83 FB 03                        cmp ebx, 3
00AE1231  75 34                           jne 0x140ae1267
00AE1233  85 FF                           test edi, edi
00AE1235  75 05                           jne 0x140ae123c
00AE1237  8D 5F 01                        lea ebx, [rdi + 1]
00AE123A  EB 2B                           jmp 0x140ae1267
00AE123C  83 FF 01                        cmp edi, 1
00AE123F  75 26                           jne 0x140ae1267
00AE1241  8D 5F 01                        lea ebx, [rdi + 1]
00AE1244  EB 21                           jmp 0x140ae1267
00AE1246  43 83 8C BE 18 B8 E0 00 FF      or dword ptr [r14 + r15*4 + 0xe0b818], 0xffffffff
00AE124F  48 8D 4D CB                     lea rcx, [rbp - 0x35]
00AE1253  83 E6 FC                        and esi, 0xfffffffc
00AE1256  49 8B D5                        mov rdx, r13
00AE1259  41 89 34 24                     mov dword ptr [r12], esi
00AE125D  E8 EE 37 FA FF                  call 0x140a84a50
00AE1262  8B 7D CB                        mov edi, dword ptr [rbp - 0x35]
00AE1265  33 F6                           xor esi, esi
00AE1267  FF C7                           inc edi
00AE1269  41 BF 04 00 00 00               mov r15d, 4
00AE126F  89 7D CB                        mov dword ptr [rbp - 0x35], edi
00AE1272  8B C7                           mov eax, edi
00AE1274  8B CF                           mov ecx, edi
00AE1276  41 3B FF                        cmp edi, r15d
00AE1279  0F 82 C0 FE FF FF               jb 0x140ae113f
00AE127F  39 1D 33 AE 42 00               cmp dword ptr [rip + 0x42ae33], ebx
00AE1285  44 8A 75 C7                     mov r14b, byte ptr [rbp - 0x39]
00AE1289  0F 84 77 01 00 00               je 0x140ae1406
00AE128F  89 74 24 30                     mov dword ptr [rsp + 0x30], esi
00AE1293  48 8D 55 D3                     lea rdx, [rbp - 0x2d]
00AE1297  89 74 24 28                     mov dword ptr [rsp + 0x28], esi
00AE129B  48 8D 0D CE F7 53 FF            lea rcx, [rip - 0xac0832]
00AE12A2  45 33 C9                        xor r9d, r9d
00AE12A5  48 89 74 24 20                  mov qword ptr [rsp + 0x20], rsi
00AE12AA  45 8B C7                        mov r8d, r15d
00AE12AD  89 5D D3                        mov dword ptr [rbp - 0x2d], ebx
00AE12B0  E8 5B FA BC FF                  call 0x1406b0d10
00AE12B5  8B 0D 8D 64 32 00               mov ecx, dword ptr [rip + 0x32648d]
00AE12BB  48 8D 3D 86 64 32 00            lea rdi, [rip + 0x326486]
00AE12C2  44 8B C0                        mov r8d, eax
00AE12C5  83 F9 05                        cmp ecx, 5
00AE12C8  0F 86 80 00 00 00               jbe 0x140ae134e
00AE12CE  85 DB                           test ebx, ebx
00AE12D0  75 09                           jne 0x140ae12db
00AE12D2  48 8D 15 07 16 02 00            lea rdx, [rip + 0x21607]
00AE12D9  EB 31                           jmp 0x140ae130c
00AE12DB  83 FB 01                        cmp ebx, 1
00AE12DE  75 09                           jne 0x140ae12e9
00AE12E0  48 8D 15 D9 15 02 00            lea rdx, [rip + 0x215d9]
00AE12E7  EB 23                           jmp 0x140ae130c
00AE12E9  83 FB 02                        cmp ebx, 2
00AE12EC  75 09                           jne 0x140ae12f7
00AE12EE  48 8D 15 2B 16 02 00            lea rdx, [rip + 0x2162b]
00AE12F5  EB 15                           jmp 0x140ae130c
00AE12F7  83 FB 03                        cmp ebx, 3
00AE12FA  48 8D 15 FF 15 02 00            lea rdx, [rip + 0x215ff]
00AE1301  48 8D 05 58 16 02 00            lea rax, [rip + 0x21658]
00AE1308  48 0F 45 D0                     cmovne rdx, rax
00AE130C  48 8D 4D F7                     lea rcx, [rbp - 9]
00AE1310  E8 EF 5F 94 FF                  call 0x140427304
00AE1315  48 8D 45 CF                     lea rax, [rbp - 0x31]
00AE1319  44 89 45 CF                     mov dword ptr [rbp - 0x31], r8d
00AE131D  48 89 45 07                     mov qword ptr [rbp + 7], rax
00AE1321  48 8D 15 D5 B4 56 FF            lea rdx, [rip - 0xa94b2b]
00AE1328  48 8D 45 D7                     lea rax, [rbp - 0x29]
00AE132C  4C 89 7D 0F                     mov qword ptr [rbp + 0xf], r15
00AE1330  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE1335  45 33 C9                        xor r9d, r9d
00AE1338  45 33 C0                        xor r8d, r8d
00AE133B  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
00AE1340  48 8B CF                        mov rcx, rdi
00AE1343  E8 98 4D 94 FF                  call 0x1404260e0
00AE1348  8B 0D FA 63 32 00               mov ecx, dword ptr [rip + 0x3263fa]
00AE134E  8D 43 FF                        lea eax, [rbx - 1]
00AE1351  83 F8 01                        cmp eax, 1
00AE1354  8B 05 5E AD 42 00               mov eax, dword ptr [rip + 0x42ad5e]
00AE135A  41 0F 96 C0                     setbe r8b
00AE135E  FF C8                           dec eax
00AE1360  83 F8 01                        cmp eax, 1
00AE1363  0F 96 C0                        setbe al
00AE1366  44 3A C0                        cmp r8b, al
00AE1369  74 60                           je 0x140ae13cb
00AE136B  83 F9 05                        cmp ecx, 5
00AE136E  76 5B                           jbe 0x140ae13cb
00AE1370  48 BA 00 00 00 00 00 40 00 00   movabs rdx, 0x400000000000
00AE137A  48 8B CF                        mov rcx, rdi
00AE137D  E8 1E D7 94 FF                  call 0x14042eaa0
00AE1382  84 C0                           test al, al
00AE1384  74 45                           je 0x140ae13cb
00AE1386  41 0F B6 C0                     movzx eax, r8b
00AE138A  48 8D 15 B0 B4 56 FF            lea rdx, [rip - 0xa94b50]
00AE1391  89 45 CF                        mov dword ptr [rbp - 0x31], eax
00AE1394  45 33 C9                        xor r9d, r9d
00AE1397  48 8D 45 CF                     lea rax, [rbp - 0x31]
00AE139B  4C 89 7D FF                     mov qword ptr [rbp - 1], r15
00AE139F  48 89 45 F7                     mov qword ptr [rbp - 9], rax
00AE13A3  45 33 C0                        xor r8d, r8d
00AE13A6  48 8D 45 CB                     lea rax, [rbp - 0x35]
00AE13AA  89 5D CB                        mov dword ptr [rbp - 0x35], ebx
00AE13AD  48 89 45 07                     mov qword ptr [rbp + 7], rax
00AE13B1  48 8B CF                        mov rcx, rdi
00AE13B4  48 8D 45 D7                     lea rax, [rbp - 0x29]
00AE13B8  4C 89 7D 0F                     mov qword ptr [rbp + 0xf], r15
00AE13BC  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00AE13C1  44 89 7C 24 20                  mov dword ptr [rsp + 0x20], r15d
00AE13C6  E8 15 4D 94 FF                  call 0x1404260e0
00AE13CB  48 8D 0D 0E DE 42 00            lea rcx, [rip + 0x42de0e]
00AE13D2  89 1D E0 AC 42 00               mov dword ptr [rip + 0x42ace0], ebx
00AE13D8  E8 67 F7 94 FF                  call 0x140430b44
00AE13DD  8A 05 37 60 38 00               mov al, byte ptr [rip + 0x386037]
00AE13E3  B9 01 00 00 00                  mov ecx, 1
00AE13E8  24 3F                           and al, 0x3f
00AE13EA  C0 E3 06                        shl bl, 6
00AE13ED  0A D8                           or bl, al
00AE13EF  88 1D 25 60 38 00               mov byte ptr [rip + 0x386025], bl
00AE13F5  E8 A6 13 9D FF                  call 0x1404b27a0
00AE13FA  48 8D 0D DF DD 42 00            lea rcx, [rip + 0x42dddf]
00AE1401  E8 B6 E7 7F FF                  call 0x1402dfbbc
00AE1406  45 84 F6                        test r14b, r14b
00AE1409  74 05                           je 0x140ae1410
00AE140B  E8 9C F5 9E FF                  call 0x1404d09ac
00AE1410  E8 FB 6F 09 00                  call 0x140b78410
00AE1415  41 8A CE                        mov cl, r14b
00AE1418  E8 7B 8F F6 FF                  call 0x140a4a398
00AE141D  41 8A C6                        mov al, r14b
00AE1420  48 8B 4D 17                     mov rcx, qword ptr [rbp + 0x17]
00AE1424  48 33 CC                        xor rcx, rsp
00AE1427  E8 14 B2 BC FF                  call 0x1406ac640
00AE142C  48 8B 9C 24 F8 00 00 00         mov rbx, qword ptr [rsp + 0xf8]
00AE1434  48 81 C4 A0 00 00 00            add rsp, 0xa0
00AE143B  41 5F                           pop r15
00AE143D  41 5E                           pop r14
00AE143F  41 5D                           pop r13
00AE1441  41 5C                           pop r12
00AE1443  5F                              pop rdi
00AE1444  5E                              pop rsi
00AE1445  5D                              pop rbp
00AE1446  C3                              ret
00AE1447  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopBatteryApplyCompositeState(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r13;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m5F;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_m8C;
    unsigned __int64 v_stack_m90;
    unsigned int v_stack_m94;
    unsigned __int8 v_stack_m98;
    unsigned int v_stack_mA0;
    unsigned int v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB8;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 3316301)) ^ (v_rsp);
    v_stack_m48 = result;
    v_r12 = 0;
    v_rbx = (unsigned int)(~((unsigned int)(*(unsigned int *)(a1))));
    v_stack_m94 = 0;
    v_stack_m8C = 0;
    v_stack_m98 = 0;
    v_rbx = (unsigned int)((v_rbx) & ((unsigned int)(v_r12 + 1)));
    result = PopAcquirePolicyLock(a1, a2, a3, a4);
    result = PopUpdateAcDcState((unsigned int)((unsigned int)(v_rbx)), a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AE0D6C;
    a2 = 0;
    result = PopBatteryUpdateAlarms((unsigned __int8)(v_r12 + 1), a2, a3, a4);
    result = PopSetNotificationWork(v_r12 + 4, a2, a3, a4);
    result = PopRecordAcDcState((unsigned int)((unsigned int)(v_rbx)), a2, a3, a4);
    result = PopUpdateSystemIdleContext(v_r12 + 2, a2, a3, a4);
    result = PopInitilizeAcDcSettings(v_r12 + 2, a2, a3, a4);
    result = PpmProfileAcDcUpdate(v_r12 + 2, a2, a3, a4);
    if (((unsigned int)(v_rbx)) == ((unsigned int)(v_r12 + 1))) {
        *(unsigned __int64 *)(v_rip + 3697488) = 0;
    }
    v_stack_m98 = (unsigned __int8)(v_r12 + 1);
loc_00AE0D6C:
    if ((*(unsigned __int8 *)(v_rip + 4371141)) == 0) goto loc_00AE0DE4;
    result = PopSetPowerSettingValueAcDc(v_rip - 11283280, 4, v_rip + 4371128, a4);
    goto loc_00AE0DBB;
loc_00AE0DA3:
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4371116) + 104)))) == 2) goto loc_00AE0DB5;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4371116) + 104)))) != 4) goto loc_00AE0DB8;
    a3 = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
    goto loc_00AE0DB8;
loc_00AE0DB5:
    a2 = (unsigned int)((0) + ((unsigned int)(v_r12 + 1)));
loc_00AE0DB8:
loc_00AE0DBB:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 4371116))) != (v_rip + 4371109)) goto loc_00AE0DA3;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3320426)))) == -1) goto loc_00AE0DD5;
    result = (unsigned int)(*(unsigned int *)(v_rip + 3320426));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3320426)))) != ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4371048))))) {
        *(unsigned int *)(v_rip + 3320405) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4371048)));
        result = PopDiagTraceBatteryCountChange((unsigned int)(*(unsigned int *)(v_rip + 4371048)), a2, a3, v_rip + 4371109);
    }
    v_stack_m98 = (unsigned __int8)(v_r12 + 1);
loc_00AE0DE4:
    result = PopReleasePolicyLock((unsigned int)(*(unsigned int *)(v_rip + 4371048)), a2, a3, v_rip + 4371109);
    result = PopBatteryCheckCompositeCapacity(a1, (unsigned int)((unsigned int)(v_rbx)), v_stack_m94, v_rip + 4371109);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1))) ^ (*(unsigned int *)(v_rip + 4371041)));
    if ((((unsigned __int8)(result)) & (15)) != 0) goto loc_00AE0E0C;
    if ((*(unsigned __int8 *)(v_rip + 4370990)) != 0) {
        a1 = 8;
        result = PopSetNotificationWork(a1, (unsigned int)((unsigned int)(v_rbx)), v_stack_m94, v_rip + 4371109);
        *(unsigned __int8 *)(v_rip + 4370971) = 0;
    }
    *(unsigned __int64 *)(v_rip + 4371001) = v_xmm0;
    *(unsigned __int64 *)(v_rip + 4371006) = v_xmm1;
    *(unsigned __int64 *)(v_rip + 4371009) = v_xmm0;
    *(unsigned int *)(v_rip + 4371008) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 40)));
    *(unsigned int *)(v_rip + 4371006) = (unsigned int)((unsigned int)(a2));
    if (v_stack_m94 == 0) goto loc_00AE0EFE;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 4371374))) + (500));
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) >> (6));
    v_stack_m90 = a2;
    result = PopSetPowerSettingValueAcDc(v_rip - 11256846, 4, v_stack_m90, v_rip + 4371109);
    result = PopRecordBatteryPercentage((unsigned int)(v_stack_m90), 4, v_stack_m90, v_rip + 4371109);
    result = (unsigned int)((unsigned int)(v_r12 + 1));
    if ((*(unsigned int *)(v_rip + 4371319)) != -1) { result = 0; }
    v_rdi = 0;
    if ((unsigned __int8)(result) == 0) {
        a1 = *(unsigned __int64 *)((unsigned int)(a2));
        a1 = (a1) - (*(unsigned __int64 *)(v_rip + 4371276));
        a1 = (a1) + (0x1388ULL);
        v_rdi = 4;
        v_rdi = (v_rdi) >> (11);
    }
    result = PopSqmBatteryUpdate((unsigned int)(v_stack_m90), (unsigned int)(v_stack_m94), (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(v_rdi)));
    result = PopBatteryTracePercentageRemaining((unsigned int)(v_stack_m90), (unsigned int)(v_stack_m94), (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(v_rdi)));
    *(unsigned __int64 *)(v_rip + 4371218) = *(unsigned __int64 *)((unsigned int)(a2));
loc_00AE0EFE:
    result = PopAcquireRwLockExclusive(v_rip + 4371251, (unsigned int)(v_stack_m94), (unsigned int)((unsigned int)(v_rbx)), (unsigned int)((unsigned int)(v_rdi)));
    v_rbx = (unsigned int)((v_rbx) | (0xFFFFFFFFULL));
    result = (unsigned int)(*(unsigned int *)(v_rip + 4370812));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4370812)))) == ((unsigned int)(v_rbx))) { result = 0; }
    v_stack_mA0 = (unsigned int)(result);
    v_stack_mA8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4370737)));
    v_stack_mB0 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4370723)));
    v_stack_mB8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4370709)));
    result = DbgPrintEx(146, 3, v_rip + 137497, (unsigned int)(*(unsigned int *)(v_rip + 4370754)));
    *(unsigned __int64 *)(v_rip + 4371162) = v_xmm0;
    *(unsigned __int8 *)(v_rip + 4371163) = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 4370774));
    result = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(v_rip + 4370681))) & ((unsigned __int8)(v_r12 + 1)));
    *(unsigned int *)(v_rip + 4371177) = (unsigned int)(v_rbx);
    *(unsigned __int64 *)(v_rip + 4371147) = v_xmm0;
    *(unsigned int *)(v_rip + 4371161) = (unsigned int)(v_rbx);
    *(unsigned int *)(v_rip + 4371159) = (unsigned int)(v_rbx);
    *(unsigned int *)(v_rip + 4371157) = (unsigned int)(v_rbx);
    *(unsigned int *)(v_rip + 4371155) = (unsigned int)(v_rbx);
    *(unsigned int *)(v_rip + 4371153) = (unsigned int)(v_rbx);
    *(unsigned int *)(v_rip + 4371151) = (unsigned int)(v_rbx);
    *(unsigned __int8 *)(v_rip + 4371089) = (unsigned __int8)(result);
    if ((*(unsigned int *)(v_rip + 4370606)) >= = 0) {
        result = (unsigned __int8)(*(unsigned __int8 *)(v_rip + 4370681));
        *(unsigned __int8 *)(v_rip + 4371075) = (unsigned __int8)(v_r12 + 1);
        result = (unsigned __int8)((result) >> (2));
        result = (unsigned __int8)((result) & ((unsigned __int8)(v_r12 + 1)));
        a1 = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 4370681)) >> (1));
        *(unsigned __int8 *)(v_rip + 4371062) = (unsigned __int8)(result);
        a1 = (unsigned __int8)((a1) & ((unsigned __int8)(v_r12 + 1)));
        *(unsigned int *)(v_rip + 4371103) = (unsigned int)((unsigned int)(a3));
        result = ((*(unsigned __int8 *)(v_rip + 4370986)) != 0) ? 1 : 0;
        a1 = (unsigned __int8)((a1) | ((unsigned __int8)(result)));
        result = *(unsigned int *)(v_rip + 4370608);
        *(unsigned int *)(v_rip + 4371034) = (unsigned int)(result);
        result = *(unsigned int *)(v_rip + 4370536);
        *(unsigned int *)(v_rip + 4371026) = (unsigned int)(result);
        result = *(unsigned int *)(v_rip + 4370532);
        *(unsigned int *)(v_rip + 4371018) = (unsigned int)(result);
        result = *(unsigned int *)(v_rip + 4370552);
        *(unsigned int *)(v_rip + 4371010) = (unsigned int)(result);
        result = *(unsigned int *)(v_rip + 4370564);
        *(unsigned int *)(v_rip + 4371002) = (unsigned int)(result);
        result = *(unsigned int *)(v_rip + 4370556);
        *(unsigned int *)(v_rip + 4370994) = (unsigned int)(result);
        result = *(unsigned int *)(v_rip + 4370492);
        *(unsigned int *)(v_rip + 4370986) = (unsigned int)(result);
        result = *(unsigned int *)(v_rip + 4370484);
        *(unsigned int *)(v_rip + 4370978) = (unsigned int)(result);
        result = *(unsigned int *)(v_rip + 4370476);
        *(unsigned int *)(v_rip + 4370970) = (unsigned int)(result);
        result = *(unsigned int *)(v_rip + 4370468);
        *(unsigned int *)(v_rip + 4370962) = (unsigned int)(result);
        result = *(unsigned int *)(v_rip + 4370432);
        *(unsigned int *)(v_rip + 4370970) = (unsigned int)(result);
        *(unsigned __int8 *)(v_rip + 4370903) = (unsigned __int8)(a1);
    }
    if (*(unsigned __int64 *)(v_rip + 4371037) == 0) goto loc_00AE10AD;
    if ((*(unsigned int *)(*(unsigned __int64 *)(v_rip + 4371037) + 128)) == ((unsigned int)(v_r12 + 1))) {
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rip + 4371037) + 184);
        *(unsigned int *)(v_rip + 4370915) = (unsigned int)(result);
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rip + 4371037) + 188);
        *(unsigned int *)(v_rip + 4370907) = (unsigned int)(result);
        result = *(unsigned int *)(*(unsigned __int64 *)(v_rip + 4371037) + 192);
        *(unsigned int *)(v_rip + 4370899) = (unsigned int)(result);
    }
    result = PopCheckCachedPowerSourceStateUpdates(a1, *(unsigned __int64 *)(v_rip + 4371037), v_rip + 137497, (unsigned int)(*(unsigned int *)(v_rip + 4370754)));
    result = PopAccountCbEnergyChange(a1, *(unsigned __int64 *)(v_rip + 4371037), v_rip + 137497, (unsigned int)(*(unsigned int *)(v_rip + 4370754)));
    a1 = 0;
    result = PopBatteryTraceSystemBatteryStatus(a1, *(unsigned __int64 *)(v_rip + 4371037), v_rip + 137497, (unsigned int)(*(unsigned int *)(v_rip + 4370754)));
    result = PopReleaseRwLock(v_rip + 4370803, *(unsigned __int64 *)(v_rip + 4371037), v_rip + 137497, (unsigned int)(*(unsigned int *)(v_rip + 4370754)));
    if ((*(unsigned int *)(v_rip + 4370383)) >= = 0) {
        result = PopRecalculateCBTriggerLevels(v_rip + 4370803, *(unsigned __int64 *)(v_rip + 4371037), v_rip + 137497, (unsigned int)(*(unsigned int *)(v_rip + 4370754)));
    }
    if ((*(unsigned int *)(v_rip + 4370365)) > 0) goto loc_00AE10F1;
    if ((*(unsigned int *)(v_rip + 4370353)) <= 0) goto loc_00AE1119;
loc_00AE10F1:
    result = PopBatteryCheckTriggerAllBatteries(v_rip + 4370594, (unsigned int)((unsigned int)(v_r12 + 1)), v_rip + 137497, (unsigned int)(*(unsigned int *)(v_rip + 4370754)));
    if ((unsigned __int8)(result) == 0) goto loc_00AE1119;
    result = (unsigned int)(*(unsigned int *)(v_rip + 4370566));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 4370566)))) & (2)) == 0) {
        a1 = 64;
        result = PopGetPolicyWorker(a1, (unsigned int)((unsigned int)(v_r12 + 1)), v_rip + 137497, (unsigned int)(*(unsigned int *)(v_rip + 4370754)));
        result = PopCheckForWork(a1, (unsigned int)((unsigned int)(v_r12 + 1)), v_rip + 137497, (unsigned int)(*(unsigned int *)(v_rip + 4370754)));
    }
    result = PopAcquirePolicyLock(a1, (unsigned int)((unsigned int)(v_r12 + 1)), v_rip + 137497, (unsigned int)(*(unsigned int *)(v_rip + 4370754)));
    result = (unsigned int)(-((unsigned int)(*(unsigned int *)(v_rip + 4370192))));
    v_stack_m94 = 0;
    v_rbx = (unsigned int)((v_rbx) & (3));
loc_00AE113F:
    result = (0) << (5);
    v_r13 = (v_rip - 11407659 + 15778184) + (result);
    v_r12 = (0) << (5);
    v_r12 = (v_r12) + (v_rip + 4370476);
    result = PopBatteryCheckTrigger(v_r13, (unsigned int)((unsigned int)(v_r12 + 1)), v_rip + 137497, (unsigned int)(*(unsigned int *)(v_rip + 4370754)));
    if ((unsigned __int8)(result) == 0) goto loc_00AE1246;
    if ((*(unsigned int *)(v_rip - 11407659 + 0 * 4 + 14727192)) == ((unsigned int)((unsigned int)(*(unsigned int *)(v_r12))))) goto loc_00AE11EB;
    *(unsigned int *)(v_rip - 11407659 + 0 * 4 + 14727192) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r12)));
    result = PopDiagTraceBatteryAlarmStatus(v_r13, *(unsigned __int64 *)(v_rip + 4373728) + 0 + 4 + 0 + 4 * 2 * 8, v_stack_m94, (unsigned int)(*(unsigned int *)(v_rip + 4370754)));
    a3 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m94)))) << (5);
    result = (unsigned int)((unsigned int)((unsigned int)(v_stack_m94)));
    v_rdi = (unsigned int)(v_stack_m94);
    if ((*(unsigned int *)(a3 + v_rip - 11407659 * 1 + 15778188)) == 128) {
        result = ((unsigned int)((unsigned int)((unsigned int)(v_stack_m94)))) + (4);
        a1 = result + result * 2;
        result = *(unsigned __int64 *)(v_rip + 4373655);
        a2 = result + a1 * 8;
        a1 = v_rip - 11407659 + 15778184;
        a1 = (a1) + (a3);
        a3 = v_stack_m94;
        result = PopDiagTraceBatteryTriggerMet(a1, a2, a3, (unsigned int)(*(unsigned int *)(v_rip + 4370754)));
        v_rdi = v_stack_m94;
    }
    v_rsi = 0;
    if ((*(unsigned __int8 *)(v_rip + 4370316)) == 0) {
        a4 = *(unsigned __int64 *)(v_rip + 4373611);
        a2 = v_rip + 4370308;
        a1 = (unsigned int)(v_rdi);
        v_stack_mB8 = 1;
        a3 = a4 + 104;
        result = a1 + a1 * 2;
        a1 = (a1) << (5);
        a4 = *(unsigned int *)(a4 + result * 8 + 116);
        a3 = a3 + result * 8;
        a1 = (a1) + (a2);
        a2 = v_rsi + 8;
        result = PopExecutePowerAction(a1, a2, a3, a4);
    }
    if (((unsigned int)(v_rbx)) != 3) goto loc_00AE1267;
    if ((unsigned int)(v_rdi) != 0) goto loc_00AE123C;
    goto loc_00AE1267;
loc_00AE123C:
    if (((unsigned int)(v_rdi)) != 1) goto loc_00AE1267;
    goto loc_00AE1267;
loc_00AE1246:
    v_rsi = (unsigned int)((v_rsi) & (0xFFFFFFFCULL));
    *(unsigned int *)(v_r12) = (unsigned int)(v_rsi);
    result = PopDiagTraceBatteryTriggerFlags(v_stack_m94, v_r13, a3, a4);
    v_rsi = 0;
loc_00AE1267:
    v_rdi = (unsigned int)(((unsigned int)(v_stack_m94)) + 1);
    v_stack_m94 = (unsigned int)(v_rdi);
    if (((unsigned int)(v_rdi)) < 4) goto loc_00AE113F;
    if ((*(unsigned int *)(v_rip + 4369971)) == ((unsigned int)(v_rdi + 1))) goto loc_00AE1406;
    v_stack_mA8 = 0;
    v_stack_mB0 = 0;
    a4 = 0;
    v_stack_mB8 = 0;
    v_stack_m8C = (unsigned int)(v_rdi + 1);
    result = ZwUpdateWnfStateData(v_rip - 11274290, v_stack_m8C, 4, a4);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3302541)))) <= 5) goto loc_00AE134E;
    if ((unsigned int)(v_rdi + 1) != 0) goto loc_00AE12DB;
    goto loc_00AE130C;
loc_00AE12DB:
    if (((unsigned int)(v_rdi + 1)) != 1) goto loc_00AE12E9;
    goto loc_00AE130C;
loc_00AE12E9:
    if (((unsigned int)(v_rdi + 1)) != 2) goto loc_00AE12F7;
    goto loc_00AE130C;
loc_00AE12F7:
    a2 = v_rip + 136703;
    if (((unsigned int)(v_rdi + 1)) != 3) { a2 = v_rip + 136792; }
loc_00AE130C:
    result = tlgCreate1Sz_char(v_stack_m68, a2, (unsigned int)((unsigned int)(result)), a4);
    v_stack_m90 = (unsigned int)((unsigned int)((unsigned int)(result)));
    v_stack_m58 = v_stack_m90;
    v_stack_m50 = 4;
    v_stack_mB0 = v_stack_m88;
    a4 = 0;
    a3 = 0;
    v_stack_mB8 = 4;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 3302534, v_rip - 11094827, a3, a4);
loc_00AE134E:
    a3 = (((unsigned int)(v_rdi + 1 - 1)) <= 1) ? 1 : 0;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 4369758))) - 1);
    result = (((unsigned int)(result)) <= 1) ? 1 : 0;
    if (((unsigned __int8)(a3)) == ((unsigned __int8)(result))) goto loc_00AE13CB;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 3302394)))) <= 5) goto loc_00AE13CB;
    result = tlgKeywordOn(v_rip + 3302534, v_rip - 11094827, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        result = (unsigned __int8)(a3);
        a2 = v_rip - 11094864;
        v_stack_m90 = (unsigned int)(result);
        a4 = 0;
        result = v_stack_m90;
        v_stack_m60 = 4;
        v_stack_m68 = result;
        a3 = 0;
        result = v_stack_m94;
        v_stack_m94 = (unsigned int)(v_rdi + 1);
        v_stack_m58 = result;
        a1 = v_rip + 3302534;
        result = v_stack_m88;
        v_stack_m50 = 4;
        v_stack_mB0 = result;
        v_stack_mB8 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(a1, a2, a3, a4);
    }
    *(unsigned int *)(v_rip + 4369632) = (unsigned int)(v_rdi + 1);
    result = PopAcquireRwLockExclusive(v_rip + 4382222, a2, a3, a4);
    result = (unsigned __int8)((*(unsigned __int8 *)(v_rip + 3694647)) & (63));
    v_rbx = (unsigned __int8)((v_rdi + 1) << (6));
    v_rbx = (unsigned __int8)((v_rbx) | ((unsigned __int8)(result)));
    *(unsigned __int8 *)(v_rip + 3694629) = (unsigned __int8)(v_rbx);
    result = PopBsdHandleRequest(1, a2, a3, a4);
    result = PopReleaseRwLock(v_rip + 4382175, a2, a3, a4);
loc_00AE1406:
    if ((unsigned __int8)(v_stack_m98) != 0) {
        result = PopTracePowerReconfig(v_rip + 4382175, a2, a3, a4);
    }
    result = PopReleasePolicyLock(v_rip + 4382175, a2, a3, a4);
    result = PopEsQueueStateEvaluation((unsigned __int8)(v_stack_m98), a2, a3, a4);
    a1 = (v_stack_m48) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (160);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopBatteryApplyCompositeState(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r12;
    int64_t local_r13;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m5F;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m88;
    uint32_t v_stack_m8C;
    uint64_t v_stack_m90;
    uint32_t v_stack_m94;
    uint8_t v_stack_m98;
    uint32_t v_stack_mA0;
    uint32_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB8;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x329A4D)) ^ (local_rsp);
    v_stack_m48 = result;
    local_r12 = 0;
    local_rbx = (uint32_t)(~((uint32_t)(*(uint32_t *)(arg1))));
    v_stack_m94 = 0;
    v_stack_m8C = 0;
    v_stack_m98 = 0;
    local_rbx = (uint32_t)((local_rbx) & ((uint32_t)(local_r12 + 1)));
    result = PopAcquirePolicyLock(Arg1, Arg2, Arg3, a4);
    result = PopUpdateAcDcState((uint32_t)((uint32_t)(local_rbx)), Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_00AE0D6C;
    Arg2 = 0;
    result = PopBatteryUpdateAlarms((uint8_t)(local_r12 + 1), Arg2, Arg3, a4);
    result = PopSetNotificationWork(local_r12 + 4, Arg2, Arg3, a4);
    result = PopRecordAcDcState((uint32_t)((uint32_t)(local_rbx)), Arg2, Arg3, a4);
    result = PopUpdateSystemIdleContext(local_r12 + 2, Arg2, Arg3, a4);
    result = PopInitilizeAcDcSettings(local_r12 + 2, Arg2, Arg3, a4);
    result = PpmProfileAcDcUpdate(local_r12 + 2, Arg2, Arg3, a4);
    if (((uint32_t)(local_rbx)) == ((uint32_t)(local_r12 + 1))) {
        *(uint64_t *)(v_rip + 0x386B50) = 0;
    }
    v_stack_m98 = (uint8_t)(local_r12 + 1);
loc_00AE0D6C:
    if ((*(uint8_t *)(v_rip + 0x42B2C5)) == 0) goto loc_00AE0DE4;
    result = PopSetPowerSettingValueAcDc(v_rip - 11283280, 4, v_rip + 4371128, a4);
    goto loc_00AE0DBB;
loc_00AE0DA3:
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42B2AC) + 0x68)))) == 2) goto loc_00AE0DB5;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0x42B2AC) + 0x68)))) != 4) goto loc_00AE0DB8;
    Arg3 = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
    goto loc_00AE0DB8;
loc_00AE0DB5:
    Arg2 = (uint32_t)((0) + ((uint32_t)(local_r12 + 1)));
loc_00AE0DB8:
loc_00AE0DBB:
    if ((*(uint64_t *)(*(uint64_t *)(v_rip + 0x42B2AC))) != (v_rip + 4371109)) goto loc_00AE0DA3;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x32AA6A)))) == -1) goto loc_00AE0DD5;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x32AA6A));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x32AA6A)))) != ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42B268))))) {
        *(uint32_t *)(v_rip + 0x32AA55) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42B268)));
        result = PopDiagTraceBatteryCountChange((uint32_t)(*(uint32_t *)(v_rip + 0x42B268)), Arg2, Arg3, v_rip + 4371109);
    }
    v_stack_m98 = (uint8_t)(local_r12 + 1);
loc_00AE0DE4:
    result = PopReleasePolicyLock((uint32_t)(*(uint32_t *)(v_rip + 0x42B268)), Arg2, Arg3, v_rip + 4371109);
    result = PopBatteryCheckCompositeCapacity(Arg1, (uint32_t)((uint32_t)(local_rbx)), v_stack_m94, v_rip + 4371109);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1))) ^ (*(uint32_t *)(v_rip + 0x42B261)));
    if ((((uint8_t)(result)) & (15)) != 0) goto loc_00AE0E0C;
    if ((*(uint8_t *)(v_rip + 0x42B22E)) != 0) {
        Arg1 = 8;
        result = PopSetNotificationWork(Arg1, (uint32_t)((uint32_t)(local_rbx)), v_stack_m94, v_rip + 4371109);
        *(uint8_t *)(v_rip + 0x42B21B) = 0;
    }
    *(uint64_t *)(v_rip + 0x42B239) = v_xmm0;
    *(uint64_t *)(v_rip + 0x42B23E) = v_xmm1;
    *(uint64_t *)(v_rip + 0x42B241) = v_xmm0;
    *(uint32_t *)(v_rip + 0x42B240) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x28)));
    *(uint32_t *)(v_rip + 0x42B23E) = (uint32_t)((uint32_t)(Arg2));
    if (v_stack_m94 == 0) goto loc_00AE0EFE;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x42B3AE))) + (500));
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) >> (6));
    v_stack_m90 = Arg2;
    result = PopSetPowerSettingValueAcDc(v_rip - 11256846, 4, v_stack_m90, v_rip + 4371109);
    result = PopRecordBatteryPercentage((uint32_t)(v_stack_m90), 4, v_stack_m90, v_rip + 4371109);
    result = (uint32_t)((uint32_t)(local_r12 + 1));
    if ((*(uint32_t *)(v_rip + 0x42B377)) != -1) { result = 0; }
    local_rdi = 0;
    if ((uint8_t)(result) == 0) {
        Arg1 = *(uint64_t *)((uint32_t)(Arg2));
        Arg1 = (Arg1) - (*(uint64_t *)(v_rip + 0x42B34C));
        Arg1 = (Arg1) + (0x1388ULL);
        local_rdi = 4;
        local_rdi = (local_rdi) >> (11);
    }
    result = PopSqmBatteryUpdate((uint32_t)(v_stack_m90), (uint32_t)(v_stack_m94), (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(local_rdi)));
    result = PopBatteryTracePercentageRemaining((uint32_t)(v_stack_m90), (uint32_t)(v_stack_m94), (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(local_rdi)));
    *(uint64_t *)(v_rip + 0x42B312) = *(uint64_t *)((uint32_t)(Arg2));
loc_00AE0EFE:
    result = PopAcquireRwLockExclusive(v_rip + 4371251, (uint32_t)(v_stack_m94), (uint32_t)((uint32_t)(local_rbx)), (uint32_t)((uint32_t)(local_rdi)));
    local_rbx = (uint32_t)((local_rbx) | (0xFFFFFFFFULL));
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x42B17C));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42B17C)))) == ((uint32_t)(local_rbx))) { result = 0; }
    v_stack_mA0 = (uint32_t)(result);
    v_stack_mA8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42B131)));
    v_stack_mB0 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42B123)));
    v_stack_mB8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42B115)));
    result = DbgPrintEx(146, 3, v_rip + 137497, (uint32_t)(*(uint32_t *)(v_rip + 0x42B142)));
    *(uint64_t *)(v_rip + 0x42B2DA) = v_xmm0;
    *(uint8_t *)(v_rip + 0x42B2DB) = (uint8_t)(*(uint8_t *)(v_rip + 0x42B156));
    result = (uint8_t)(((uint8_t)(*(uint8_t *)(v_rip + 0x42B0F9))) & ((uint8_t)(local_r12 + 1)));
    *(uint32_t *)(v_rip + 0x42B2E9) = (uint32_t)(local_rbx);
    *(uint64_t *)(v_rip + 0x42B2CB) = v_xmm0;
    *(uint32_t *)(v_rip + 0x42B2D9) = (uint32_t)(local_rbx);
    *(uint32_t *)(v_rip + 0x42B2D7) = (uint32_t)(local_rbx);
    *(uint32_t *)(v_rip + 0x42B2D5) = (uint32_t)(local_rbx);
    *(uint32_t *)(v_rip + 0x42B2D3) = (uint32_t)(local_rbx);
    *(uint32_t *)(v_rip + 0x42B2D1) = (uint32_t)(local_rbx);
    *(uint32_t *)(v_rip + 0x42B2CF) = (uint32_t)(local_rbx);
    *(uint8_t *)(v_rip + 0x42B291) = (uint8_t)(result);
    if ((*(uint32_t *)(v_rip + 0x42B0AE)) >= = 0) {
        result = (uint8_t)(*(uint8_t *)(v_rip + 0x42B0F9));
        *(uint8_t *)(v_rip + 0x42B283) = (uint8_t)(local_r12 + 1);
        result = (uint8_t)((result) >> (2));
        result = (uint8_t)((result) & ((uint8_t)(local_r12 + 1)));
        Arg1 = (uint8_t)((*(uint8_t *)(v_rip + 0x42B0F9)) >> (1));
        *(uint8_t *)(v_rip + 0x42B276) = (uint8_t)(result);
        Arg1 = (uint8_t)((Arg1) & ((uint8_t)(local_r12 + 1)));
        *(uint32_t *)(v_rip + 0x42B29F) = (uint32_t)((uint32_t)(Arg3));
        result = ((*(uint8_t *)(v_rip + 0x42B22A)) != 0) ? 1 : 0;
        Arg1 = (uint8_t)((Arg1) | ((uint8_t)(result)));
        result = *(uint32_t *)(v_rip + 0x42B0B0);
        *(uint32_t *)(v_rip + 0x42B25A) = (uint32_t)(result);
        result = *(uint32_t *)(v_rip + 0x42B068);
        *(uint32_t *)(v_rip + 0x42B252) = (uint32_t)(result);
        result = *(uint32_t *)(v_rip + 0x42B064);
        *(uint32_t *)(v_rip + 0x42B24A) = (uint32_t)(result);
        result = *(uint32_t *)(v_rip + 0x42B078);
        *(uint32_t *)(v_rip + 0x42B242) = (uint32_t)(result);
        result = *(uint32_t *)(v_rip + 0x42B084);
        *(uint32_t *)(v_rip + 0x42B23A) = (uint32_t)(result);
        result = *(uint32_t *)(v_rip + 0x42B07C);
        *(uint32_t *)(v_rip + 0x42B232) = (uint32_t)(result);
        result = *(uint32_t *)(v_rip + 0x42B03C);
        *(uint32_t *)(v_rip + 0x42B22A) = (uint32_t)(result);
        result = *(uint32_t *)(v_rip + 0x42B034);
        *(uint32_t *)(v_rip + 0x42B222) = (uint32_t)(result);
        result = *(uint32_t *)(v_rip + 0x42B02C);
        *(uint32_t *)(v_rip + 0x42B21A) = (uint32_t)(result);
        result = *(uint32_t *)(v_rip + 0x42B024);
        *(uint32_t *)(v_rip + 0x42B212) = (uint32_t)(result);
        result = *(uint32_t *)(v_rip + 0x42B000);
        *(uint32_t *)(v_rip + 0x42B21A) = (uint32_t)(result);
        *(uint8_t *)(v_rip + 0x42B1D7) = (uint8_t)(Arg1);
    }
    if (*(uint64_t *)(v_rip + 0x42B25D) == 0) goto loc_00AE10AD;
    if ((*(uint32_t *)(*(uint64_t *)(v_rip + 0x42B25D) + 0x80)) == ((uint32_t)(local_r12 + 1))) {
        result = *(uint32_t *)(*(uint64_t *)(v_rip + 0x42B25D) + 0xB8);
        *(uint32_t *)(v_rip + 0x42B1E3) = (uint32_t)(result);
        result = *(uint32_t *)(*(uint64_t *)(v_rip + 0x42B25D) + 0xBC);
        *(uint32_t *)(v_rip + 0x42B1DB) = (uint32_t)(result);
        result = *(uint32_t *)(*(uint64_t *)(v_rip + 0x42B25D) + 0xC0);
        *(uint32_t *)(v_rip + 0x42B1D3) = (uint32_t)(result);
    }
    result = PopCheckCachedPowerSourceStateUpdates(Arg1, *(uint64_t *)(v_rip + 0x42B25D), v_rip + 137497, (uint32_t)(*(uint32_t *)(v_rip + 0x42B142)));
    result = PopAccountCbEnergyChange(Arg1, *(uint64_t *)(v_rip + 0x42B25D), v_rip + 137497, (uint32_t)(*(uint32_t *)(v_rip + 0x42B142)));
    Arg1 = 0;
    result = PopBatteryTraceSystemBatteryStatus(Arg1, *(uint64_t *)(v_rip + 0x42B25D), v_rip + 137497, (uint32_t)(*(uint32_t *)(v_rip + 0x42B142)));
    result = PopReleaseRwLock(v_rip + 4370803, *(uint64_t *)(v_rip + 0x42B25D), v_rip + 137497, (uint32_t)(*(uint32_t *)(v_rip + 0x42B142)));
    if ((*(uint32_t *)(v_rip + 0x42AFCF)) >= = 0) {
        result = PopRecalculateCBTriggerLevels(v_rip + 4370803, *(uint64_t *)(v_rip + 0x42B25D), v_rip + 137497, (uint32_t)(*(uint32_t *)(v_rip + 0x42B142)));
    }
    if ((*(uint32_t *)(v_rip + 0x42AFBD)) > 0) goto loc_00AE10F1;
    if ((*(uint32_t *)(v_rip + 0x42AFB1)) <= 0) goto loc_00AE1119;
loc_00AE10F1:
    result = PopBatteryCheckTriggerAllBatteries(v_rip + 4370594, (uint32_t)((uint32_t)(local_r12 + 1)), v_rip + 137497, (uint32_t)(*(uint32_t *)(v_rip + 0x42B142)));
    if ((uint8_t)(result) == 0) goto loc_00AE1119;
    result = (uint32_t)(*(uint32_t *)(v_rip + 0x42B086));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x42B086)))) & (2)) == 0) {
        Arg1 = 64;
        result = PopGetPolicyWorker(Arg1, (uint32_t)((uint32_t)(local_r12 + 1)), v_rip + 137497, (uint32_t)(*(uint32_t *)(v_rip + 0x42B142)));
        result = PopCheckForWork(Arg1, (uint32_t)((uint32_t)(local_r12 + 1)), v_rip + 137497, (uint32_t)(*(uint32_t *)(v_rip + 0x42B142)));
    }
    result = PopAcquirePolicyLock(Arg1, (uint32_t)((uint32_t)(local_r12 + 1)), v_rip + 137497, (uint32_t)(*(uint32_t *)(v_rip + 0x42B142)));
    result = (uint32_t)(-((uint32_t)(*(uint32_t *)(v_rip + 0x42AF10))));
    v_stack_m94 = 0;
    local_rbx = (uint32_t)((local_rbx) & (3));
loc_00AE113F:
    result = (0) << (5);
    local_r13 = (v_rip - 11407659 + 15778184) + (result);
    local_r12 = (0) << (5);
    local_r12 = (local_r12) + (v_rip + 4370476);
    result = PopBatteryCheckTrigger(local_r13, (uint32_t)((uint32_t)(local_r12 + 1)), v_rip + 137497, (uint32_t)(*(uint32_t *)(v_rip + 0x42B142)));
    if ((uint8_t)(result) == 0) goto loc_00AE1246;
    if ((*(uint32_t *)(v_rip - 0xAE112B + 0x0 * 4 + 0xE0B818)) == ((uint32_t)((uint32_t)(*(uint32_t *)(local_r12))))) goto loc_00AE11EB;
    *(uint32_t *)(v_rip - 0xAE112B + 0x0 * 4 + 0xE0B818) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r12)));
    result = PopDiagTraceBatteryAlarmStatus(local_r13, *(uint64_t *)(v_rip + 0x42BCE0) + 0 + 4 + 0 + 4 * 2 * 8, v_stack_m94, (uint32_t)(*(uint32_t *)(v_rip + 0x42B142)));
    Arg3 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m94)))) << (5);
    result = (uint32_t)((uint32_t)((uint32_t)(v_stack_m94)));
    local_rdi = (uint32_t)(v_stack_m94);
    if ((*(uint32_t *)(Arg3 + v_rip - 0xAE112B * 1 + 0xF0C18C)) == 128) {
        result = ((uint32_t)((uint32_t)((uint32_t)(v_stack_m94)))) + (4);
        Arg1 = result + result * 2;
        result = *(uint64_t *)(v_rip + 0x42BC97);
        Arg2 = result + Arg1 * 8;
        Arg1 = v_rip - 11407659 + 15778184;
        Arg1 = (Arg1) + (Arg3);
        Arg3 = v_stack_m94;
        result = PopDiagTraceBatteryTriggerMet(Arg1, Arg2, Arg3, (uint32_t)(*(uint32_t *)(v_rip + 0x42B142)));
        local_rdi = v_stack_m94;
    }
    local_rsi = 0;
    if ((*(uint8_t *)(v_rip + 0x42AF8C)) == 0) {
        a4 = *(uint64_t *)(v_rip + 0x42BC6B);
        Arg2 = v_rip + 4370308;
        Arg1 = (uint32_t)(local_rdi);
        v_stack_mB8 = 1;
        Arg3 = a4 + 104;
        result = Arg1 + Arg1 * 2;
        Arg1 = (Arg1) << (5);
        a4 = *(uint32_t *)(a4 + result * 8 + 0x74);
        Arg3 = Arg3 + result * 8;
        Arg1 = (Arg1) + (Arg2);
        Arg2 = local_rsi + 8;
        result = PopExecutePowerAction(Arg1, Arg2, Arg3, a4);
    }
    if (((uint32_t)(local_rbx)) != 3) goto loc_00AE1267;
    if ((uint32_t)(local_rdi) != 0) goto loc_00AE123C;
    goto loc_00AE1267;
loc_00AE123C:
    if (((uint32_t)(local_rdi)) != 1) goto loc_00AE1267;
    goto loc_00AE1267;
loc_00AE1246:
    local_rsi = (uint32_t)((local_rsi) & (0xFFFFFFFCULL));
    *(uint32_t *)(local_r12) = (uint32_t)(local_rsi);
    result = PopDiagTraceBatteryTriggerFlags(v_stack_m94, local_r13, Arg3, a4);
    local_rsi = 0;
loc_00AE1267:
    local_rdi = (uint32_t)(((uint32_t)(v_stack_m94)) + 1);
    v_stack_m94 = (uint32_t)(local_rdi);
    if (((uint32_t)(local_rdi)) < 4) goto loc_00AE113F;
    if ((*(uint32_t *)(v_rip + 0x42AE33)) == ((uint32_t)(local_rdi + 1))) goto loc_00AE1406;
    v_stack_mA8 = 0;
    v_stack_mB0 = 0;
    a4 = 0;
    v_stack_mB8 = 0;
    v_stack_m8C = (uint32_t)(local_rdi + 1);
    result = ZwUpdateWnfStateData(v_rip - 11274290, v_stack_m8C, 4, a4);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x32648D)))) <= 5) goto loc_00AE134E;
    if ((uint32_t)(local_rdi + 1) != 0) goto loc_00AE12DB;
    goto loc_00AE130C;
loc_00AE12DB:
    if (((uint32_t)(local_rdi + 1)) != 1) goto loc_00AE12E9;
    goto loc_00AE130C;
loc_00AE12E9:
    if (((uint32_t)(local_rdi + 1)) != 2) goto loc_00AE12F7;
    goto loc_00AE130C;
loc_00AE12F7:
    Arg2 = v_rip + 136703;
    if (((uint32_t)(local_rdi + 1)) != 3) { Arg2 = v_rip + 136792; }
loc_00AE130C:
    result = tlgCreate1Sz_char(v_stack_m68, Arg2, (uint32_t)((uint32_t)(result)), a4);
    v_stack_m90 = (uint32_t)((uint32_t)((uint32_t)(result)));
    v_stack_m58 = v_stack_m90;
    v_stack_m50 = 4;
    v_stack_mB0 = v_stack_m88;
    a4 = 0;
    Arg3 = 0;
    v_stack_mB8 = 4;
    result = tlgWriteTransfer_EtwWriteTransfer(v_rip + 3302534, v_rip - 11094827, Arg3, a4);
loc_00AE134E:
    Arg3 = (((uint32_t)(local_rdi + 1 - 1)) <= 1) ? 1 : 0;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x42AD5E))) - 1);
    result = (((uint32_t)(result)) <= 1) ? 1 : 0;
    if (((uint8_t)(Arg3)) == ((uint8_t)(result))) goto loc_00AE13CB;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x3263FA)))) <= 5) goto loc_00AE13CB;
    result = tlgKeywordOn(v_rip + 3302534, v_rip - 11094827, Arg3, a4);
    if ((uint8_t)(result) != 0) {
        result = (uint8_t)(Arg3);
        Arg2 = v_rip - 11094864;
        v_stack_m90 = (uint32_t)(result);
        a4 = 0;
        result = v_stack_m90;
        v_stack_m60 = 4;
        v_stack_m68 = result;
        Arg3 = 0;
        result = v_stack_m94;
        v_stack_m94 = (uint32_t)(local_rdi + 1);
        v_stack_m58 = result;
        Arg1 = v_rip + 3302534;
        result = v_stack_m88;
        v_stack_m50 = 4;
        v_stack_mB0 = result;
        v_stack_mB8 = 4;
        result = tlgWriteTransfer_EtwWriteTransfer(Arg1, Arg2, Arg3, a4);
    }
    *(uint32_t *)(v_rip + 0x42ACE0) = (uint32_t)(local_rdi + 1);
    result = PopAcquireRwLockExclusive(v_rip + 4382222, Arg2, Arg3, a4);
    result = (uint8_t)((*(uint8_t *)(v_rip + 0x386037)) & (63));
    local_rbx = (uint8_t)((local_rdi + 1) << (6));
    local_rbx = (uint8_t)((local_rbx) | ((uint8_t)(result)));
    *(uint8_t *)(v_rip + 0x386025) = (uint8_t)(local_rbx);
    result = PopBsdHandleRequest(1, Arg2, Arg3, a4);
    result = PopReleaseRwLock(v_rip + 4382175, Arg2, Arg3, a4);
loc_00AE1406:
    if ((uint8_t)(v_stack_m98) != 0) {
        result = PopTracePowerReconfig(v_rip + 4382175, Arg2, Arg3, a4);
    }
    result = PopReleasePolicyLock(v_rip + 4382175, Arg2, Arg3, a4);
    result = PopEsQueueStateEvaluation((uint8_t)(v_stack_m98), Arg2, Arg3, a4);
    Arg1 = (v_stack_m48) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, a4);
    local_rsp = (local_rsp) + (160);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x0` | `128` | `R` |
| `Arg1` | `+ 0x10` | `128` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AE0CD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
