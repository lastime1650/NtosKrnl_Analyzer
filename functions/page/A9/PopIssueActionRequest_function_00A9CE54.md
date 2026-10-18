# PopIssueActionRequest

- RVA: `0x00A9CE54`–`0x00A9D32F` (길이 `1,243` bytes)
- VA: `0x0000000140A9CE54`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BA6B8`
- 디코드: `335`개 명령, `1,243/1,243` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **61**; 고유 호출 대상: **41**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **23**

### Outgoing calls
- `0x00A9CE9A` → [PopAcquireAwaymodeLock](../../pagelk/B7/PopAcquireAwaymodeLock_function_00B7BF60.md) (function, `0x00B7BF60`)
- `0x00A9CE9F` → [PopReadSystemAwayModePolicy](PopReadSystemAwayModePolicy_function_00A9D368.md) (function, `0x00A9D368`)
- `0x00A9CEFC` → [PopSetSystemState](../../text/48/PopSetSystemState_function_00482A98.md) (function, `0x00482A98`)
- `0x00A9CF03` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00A9CF0B` → [PopSetSystemAwayMode](../75/PopSetSystemAwayMode_function_0075EF00.md) (function, `0x0075EF00`)
- `0x00A9CF12` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00A9CF17` → [PopReleaseAwaymodeLock](../../pagelk/B7/PopReleaseAwaymodeLock_function_00B7BB3C.md) (function, `0x00B7BB3C`)
- `0x00A9CF23` → [PopReleaseAwaymodeLock](../../pagelk/B7/PopReleaseAwaymodeLock_function_00B7BB3C.md) (function, `0x00B7BB3C`)
- `0x00A9CF60` → [PopPotsGetActionEntryReason](PopPotsGetActionEntryReason_function_00A9D45C.md) (function, `0x00A9D45C`)
- `0x00A9CF75` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00A9CF7C` → [PopScreenOff](../98/PopScreenOff_function_0098A758.md) (function, `0x0098A758`)
- `0x00A9CF81` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00A9CFA9` → [PopSetPowerActionWatchdogState](../../text/4C/PopSetPowerActionWatchdogState_function_004C86B8.md) (function, `0x004C86B8`)
- `0x00A9CFC7` → [PopPushPowerStateTransitionRecord](../../pagelk/B7/PopPushPowerStateTransitionRecord_function_00B7CC90.md) (function, `0x00B7CC90`)
- `0x00A9D013` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00A9D018` → [PpmBeginHighPerfRequest](../../text/47/PpmBeginHighPerfRequest_function_004774FC.md) (function, `0x004774FC`)
- `0x00A9D02E` → [PopPowerAggregatorNotifySuspendResume](../AB/PopPowerAggregatorNotifySuspendResume_function_00AB9728.md) (function, `0x00AB9728`)
- `0x00A9D064` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00A9D075` → [PopDiagTracePowerTransitionStart](../AB/PopDiagTracePowerTransitionStart_function_00AB74F8.md) (function, `0x00AB74F8`)
- `0x00A9D07C` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00A9D088` → [PopEnableSystemSleepCheckpoint](../AC/PopEnableSystemSleepCheckpoint_function_00AC4F50.md) (function, `0x00AC4F50`)
- `0x00A9D092` → [PopCheckpointSystemSleep](../../pagelk/B7/PopCheckpointSystemSleep_function_00B77C90.md) (function, `0x00B77C90`)
- `0x00A9D0A4` → [PopSetSleepMarker](../AA/PopSetSleepMarker_function_00AA86FC.md) (function, `0x00AA86FC`)
- `0x00A9D0B9` → [PopTransitionSystemPowerState](../../pagelk/B5/PopTransitionSystemPowerState_function_00B5B0A0.md) (function, `0x00B5B0A0`)
- `0x00A9D0ED` → [PopDispatchStateCallout](../91/PopDispatchStateCallout_function_0091248C.md) (function, `0x0091248C`)
- `0x00A9D108` → [PopPrepareSleep](../../text/4C/PopPrepareSleep_function_004C80BC.md) (function, `0x004C80BC`)
- `0x00A9D111` → [PoBlockConsoleSwitch](../AC/PoBlockConsoleSwitch_function_00ACCCA0.md) (function, `0x00ACCCA0`)
- `0x00A9D148` → [PfPowerActionNotify](../../pagelk/B7/PfPowerActionNotify_function_00B7AC98.md) (function, `0x00B7AC98`)
- `0x00A9D161` → [PopSuspendApps](../75/PopSuspendApps_function_0075F008.md) (function, `0x0075F008`)
- `0x00A9D16A` → [PopSuspendServices](../75/PopSuspendServices_function_0075F05C.md) (function, `0x0075F05C`)
- `0x00A9D175` → [EtwShutdown](../7B/EtwShutdown_function_007B50B0.md) (function, `0x007B50B0`)
- `0x00A9D180` → [PopDispatchSuperfetchNotification](../AC/PopDispatchSuperfetchNotification_function_00AC3FD8.md) (function, `0x00AC3FD8`)
- `0x00A9D18E` → [PopTransitionSystemPowerState](../../pagelk/B5/PopTransitionSystemPowerState_function_00B5B0A0.md) (function, `0x00B5B0A0`)
- `0x00A9D195` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00A9D1A0` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00A9D1B8` → [PopResumeServices](../91/PopResumeServices_function_00912410.md) (function, `0x00912410`)
- `0x00A9D1BF` → [PopPowerAggregatorNotifySuspendResume](../AB/PopPowerAggregatorNotifySuspendResume_function_00AB9728.md) (function, `0x00AB9728`)
- `0x00A9D1CB` → [PopResumeApps](../75/PopResumeApps_function_0075EBFC.md) (function, `0x0075EBFC`)
- `0x00A9D1DD` → [PfPowerActionNotify](../../pagelk/B7/PfPowerActionNotify_function_00B7AC98.md) (function, `0x00B7AC98`)
- `0x00A9D1EF` → [PopDispatchStateCallout](../91/PopDispatchStateCallout_function_0091248C.md) (function, `0x0091248C`)
- `0x00A9D1F4` → [TtmIsEnabled](../91/TtmIsEnabled_function_009143D8.md) (function, `0x009143D8`)
- `0x00A9D206` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00A9D218` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00A9D226` → [TtmNotifyLowPowerStateExited](../98/TtmNotifyLowPowerStateExited_function_0098A878.md) (function, `0x0098A878`)
- `0x00A9D22B` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00A9D237` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (function, `0x00B78410`)
- `0x00A9D253` → [PopDispatchStateCallout](../91/PopDispatchStateCallout_function_0091248C.md) (function, `0x0091248C`)
- `0x00A9D262` → [PopPowerAggregatorNotifySuspendResume](../AB/PopPowerAggregatorNotifySuspendResume_function_00AB9728.md) (function, `0x00AB9728`)
- `0x00A9D27C` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (function, `0x0037E7E0`)
- `0x00A9D28B` → [PopDiagTraceHiberStats](../A7/PopDiagTraceHiberStats_function_00A72FB4.md) (function, `0x00A72FB4`)
- `0x00A9D290` → [PopDiagTracePowerTransitionTime](PopDiagTracePowerTransitionTime_function_00A9B84C.md) (function, `0x00A9B84C`)
- `0x00A9D298` → [PopDiagTracePerfTrackData](../A7/PopDiagTracePerfTrackData_function_00A733CC.md) (function, `0x00A733CC`)
- `0x00A9D2BD` → [PopCheckpointSystemSleep](../../pagelk/B7/PopCheckpointSystemSleep_function_00B77C90.md) (function, `0x00B77C90`)
- `0x00A9D2CB` → [RtlBootStatusDisableFlushing](../../text/4F/RtlBootStatusDisableFlushing_function_004FC6C0.md) (function, `0x004FC6C0`)
- `0x00A9D2DA` → [PopQueueWorkItem](../../text/4A/PopQueueWorkItem_function_004A20F8.md) (function, `0x004A20F8`)
- `0x00A9D2E1` → [PopDiagTracePowerTransitionEnd](../AD/PopDiagTracePowerTransitionEnd_function_00AD24DC.md) (function, `0x00AD24DC`)
- `0x00A9D2EF` → [PopPotsLogPowerTransitionReliability](../AA/PopPotsLogPowerTransitionReliability_function_00AAE1C4.md) (function, `0x00AAE1C4`)
- `0x00A9D2F9` → [PpmEndHighPerfRequest](../../text/47/PpmEndHighPerfRequest_function_00477490.md) (function, `0x00477490`)
- `0x00A9D2FE` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (function, `0x00B783C0`)
- `0x00A9D308` → [PoDelistPowerStateTransitionBlocker](../../pagelk/B7/PoDelistPowerStateTransitionBlocker_function_00B795D4.md) (function, `0x00B795D4`)
- `0x00A9D30F` → [PopSetPowerActionWatchdogState](../../text/4C/PopSetPowerActionWatchdogState_function_004C86B8.md) (function, `0x004C86B8`)

### Direct callers
- [PopPolicyWorkerAction](PopPolicyWorkerAction_function_00A9CC40.md) at `0x00A9CCBB`
- [PopPolicyWorkerActionPromote](../AB/PopPolicyWorkerActionPromote_function_00ABFE10.md) at `0x00ABFE5C`

### Static image references
- `0x00A9CEA4` → RVA `0x00F0CE10` (`.data`; read)
- `0x00A9CEB1` → RVA `0x00F0CE11` (`.data`; read)
- `0x00A9CEC5` → RVA `0x00F0BD54` (`.data`; read)
- `0x00A9CED7` → RVA `0x00F0CE18` (`.data`; read)
- `0x00A9CEEA` → RVA `0x00F0CF0C` (`.data`; read)
- `0x00A9CF57` → RVA `0x00F0BD58` (`.data`; read)
- `0x00A9CF6D` → RVA `0x00E67A50` (`.data`; read)
- `0x00A9CFD8` → RVA `0x00F06628` (`.data`; read)
- `0x00A9D005` → RVA `0x00F0BD40` (`.data`; read/write)
- `0x00A9D00C` → RVA `0x00F0BE00` (`.data`; read)
- `0x00A9D036` → RVA `0x00F0C300` (`.data`; write)
- `0x00A9D057` → RVA `0x00F0C300` (`.data`; read)
- `0x00A9D081` → RVA `0x00F0C308` (`.data`; write)
- `0x00A9D14D` → RVA `0x00F0C6F4` (`.data`; write)
- `0x00A9D20B` → RVA `0x00F0D100` (`.data`; read)
- `0x00A9D211` → RVA `0x00F0D101` (`.data`; write)
- `0x00A9D230` → RVA `0x00F0D100` (`.data`; write)
- `0x00A9D284` → RVA `0x00F0C330` (`.data`; write)
- `0x00A9D29D` → RVA `0x00F0E790` (`.data`; write)
- `0x00A9D2A4` → RVA `0x00F0C678` (`.data`; write)
- `0x00A9D2AA` → RVA `0x00F0C67C` (`.data`; write)
- `0x00A9D2C4` → RVA `0x00E0B578` (`.data`; write)
- `0x00A9D2D3` → RVA `0x00F0F100` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **34**
  - `0x00A9CE9A` → [PopAcquireAwaymodeLock](../../pagelk/B7/PopAcquireAwaymodeLock_function_00B7BF60.md) (`PAGE` → `PAGELK`)
  - `0x00A9CEFC` → [PopSetSystemState](../../text/48/PopSetSystemState_function_00482A98.md) (`PAGE` → `.text`)
  - `0x00A9CF03` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`PAGE` → `PAGELK`)
  - `0x00A9CF12` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`PAGE` → `PAGELK`)
  - `0x00A9CF17` → [PopReleaseAwaymodeLock](../../pagelk/B7/PopReleaseAwaymodeLock_function_00B7BB3C.md) (`PAGE` → `PAGELK`)
  - `0x00A9CF23` → [PopReleaseAwaymodeLock](../../pagelk/B7/PopReleaseAwaymodeLock_function_00B7BB3C.md) (`PAGE` → `PAGELK`)
  - `0x00A9CF75` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`PAGE` → `PAGELK`)
  - `0x00A9CF81` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`PAGE` → `PAGELK`)
  - `0x00A9CFA9` → [PopSetPowerActionWatchdogState](../../text/4C/PopSetPowerActionWatchdogState_function_004C86B8.md) (`PAGE` → `.text`)
  - `0x00A9CFC7` → [PopPushPowerStateTransitionRecord](../../pagelk/B7/PopPushPowerStateTransitionRecord_function_00B7CC90.md) (`PAGE` → `PAGELK`)
  - `0x00A9D013` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`PAGE` → `PAGELK`)
  - `0x00A9D018` → [PpmBeginHighPerfRequest](../../text/47/PpmBeginHighPerfRequest_function_004774FC.md) (`PAGE` → `.text`)
  - `0x00A9D064` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
  - `0x00A9D07C` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`PAGE` → `.text`)
  - `0x00A9D092` → [PopCheckpointSystemSleep](../../pagelk/B7/PopCheckpointSystemSleep_function_00B77C90.md) (`PAGE` → `PAGELK`)
  - `0x00A9D0B9` → [PopTransitionSystemPowerState](../../pagelk/B5/PopTransitionSystemPowerState_function_00B5B0A0.md) (`PAGE` → `PAGELK`)
  - `0x00A9D108` → [PopPrepareSleep](../../text/4C/PopPrepareSleep_function_004C80BC.md) (`PAGE` → `.text`)
  - `0x00A9D148` → [PfPowerActionNotify](../../pagelk/B7/PfPowerActionNotify_function_00B7AC98.md) (`PAGE` → `PAGELK`)
  - `0x00A9D18E` → [PopTransitionSystemPowerState](../../pagelk/B5/PopTransitionSystemPowerState_function_00B5B0A0.md) (`PAGE` → `PAGELK`)
  - `0x00A9D195` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`PAGE` → `PAGELK`)
  - `0x00A9D1A0` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`PAGE` → `PAGELK`)
  - `0x00A9D1DD` → [PfPowerActionNotify](../../pagelk/B7/PfPowerActionNotify_function_00B7AC98.md) (`PAGE` → `PAGELK`)
  - `0x00A9D206` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`PAGE` → `PAGELK`)
  - `0x00A9D218` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`PAGE` → `PAGELK`)
  - `0x00A9D22B` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`PAGE` → `PAGELK`)
  - `0x00A9D237` → [PopReleasePolicyLock](../../pagelk/B7/PopReleasePolicyLock_function_00B78410.md) (`PAGE` → `PAGELK`)
  - `0x00A9D27C` → [KeQueryPerformanceCounter](../../text/37/KeQueryPerformanceCounter_function_0037E7E0.md) (`PAGE` → `.text`)
  - `0x00A9D2BD` → [PopCheckpointSystemSleep](../../pagelk/B7/PopCheckpointSystemSleep_function_00B77C90.md) (`PAGE` → `PAGELK`)
  - `0x00A9D2CB` → [RtlBootStatusDisableFlushing](../../text/4F/RtlBootStatusDisableFlushing_function_004FC6C0.md) (`PAGE` → `.text`)
  - `0x00A9D2DA` → [PopQueueWorkItem](../../text/4A/PopQueueWorkItem_function_004A20F8.md) (`PAGE` → `.text`)
  - `0x00A9D2F9` → [PpmEndHighPerfRequest](../../text/47/PpmEndHighPerfRequest_function_00477490.md) (`PAGE` → `.text`)
  - `0x00A9D2FE` → [PopAcquirePolicyLock](../../pagelk/B7/PopAcquirePolicyLock_function_00B783C0.md) (`PAGE` → `PAGELK`)
  - `0x00A9D308` → [PoDelistPowerStateTransitionBlocker](../../pagelk/B7/PoDelistPowerStateTransitionBlocker_function_00B795D4.md) (`PAGE` → `PAGELK`)
  - `0x00A9D30F` → [PopSetPowerActionWatchdogState](../../text/4C/PopSetPowerActionWatchdogState_function_004C86B8.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A9CE54  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00A9CE59  89 54 24 10                     mov dword ptr [rsp + 0x10], edx
00A9CE5D  88 4C 24 08                     mov byte ptr [rsp + 8], cl
00A9CE61  55                              push rbp
00A9CE62  56                              push rsi
00A9CE63  57                              push rdi
00A9CE64  41 54                           push r12
00A9CE66  41 55                           push r13
00A9CE68  41 56                           push r14
00A9CE6A  41 57                           push r15
00A9CE6C  48 8B EC                        mov rbp, rsp
00A9CE6F  48 83 EC 70                     sub rsp, 0x70
00A9CE73  0F 57 C0                        xorps xmm0, xmm0
00A9CE76  4D 63 E8                        movsxd r13, r8d
00A9CE79  33 C0                           xor eax, eax
00A9CE7B  C7 45 BC 01 00 00 C0            mov dword ptr [rbp - 0x44], 0xc0000001
00A9CE82  33 FF                           xor edi, edi
00A9CE84  89 45 E0                        mov dword ptr [rbp - 0x20], eax
00A9CE87  0F 11 45 C0                     movups xmmword ptr [rbp - 0x40], xmm0
00A9CE8B  89 7D B4                        mov dword ptr [rbp - 0x4c], edi
00A9CE8E  45 8B E1                        mov r12d, r9d
00A9CE91  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00A9CE95  8B F2                           mov esi, edx
00A9CE97  44 8A F9                        mov r15b, cl
00A9CE9A  E8 C1 F0 0D 00                  call 0x140b7bf60
00A9CE9F  E8 C4 04 00 00                  call 0x140a9d368
00A9CEA4  40 38 3D 65 FF 46 00            cmp byte ptr [rip + 0x46ff65], dil
00A9CEAB  44 8D 77 01                     lea r14d, [rdi + 1]
00A9CEAF  75 09                           jne 0x140a9ceba
00A9CEB1  40 38 3D 59 FF 46 00            cmp byte ptr [rip + 0x46ff59], dil
00A9CEB8  74 69                           je 0x140a9cf23
00A9CEBA  83 FE 02                        cmp esi, 2
00A9CEBD  75 64                           jne 0x140a9cf23
00A9CEBF  41 83 FD 05                     cmp r13d, 5
00A9CEC3  7D 5E                           jge 0x140a9cf23
00A9CEC5  8B 05 89 EE 46 00               mov eax, dword ptr [rip + 0x46ee89]
00A9CECB  A9 FA FF FF FF                  test eax, 0xfffffffa
00A9CED0  75 51                           jne 0x140a9cf23
00A9CED2  41 3B C6                        cmp eax, r14d
00A9CED5  74 4C                           je 0x140a9cf23
00A9CED7  8B 05 3B FF 46 00               mov eax, dword ptr [rip + 0x46ff3b]
00A9CEDD  85 C0                           test eax, eax
00A9CEDF  75 36                           jne 0x140a9cf17
00A9CEE1  40 38 3D 29 FF 46 00            cmp byte ptr [rip + 0x46ff29], dil
00A9CEE8  74 19                           je 0x140a9cf03
00A9CEEA  F7 05 18 00 47 00 00 00 00 04   test dword ptr [rip + 0x470018], 0x4000000
00A9CEF4  74 21                           je 0x140a9cf17
00A9CEF6  8D 56 05                        lea edx, [rsi + 5]
00A9CEF9  8D 4E 02                        lea ecx, [rsi + 2]
00A9CEFC  E8 97 5B 9E FF                  call 0x140482a98
00A9CF01  EB 14                           jmp 0x140a9cf17
00A9CF03  E8 08 B5 0D 00                  call 0x140b78410
00A9CF08  41 8B CE                        mov ecx, r14d
00A9CF0B  E8 F0 1F CC FF                  call 0x14075ef00
00A9CF10  8B F8                           mov edi, eax
00A9CF12  E8 A9 B4 0D 00                  call 0x140b783c0
00A9CF17  E8 20 EC 0D 00                  call 0x140b7bb3c
00A9CF1C  8B C7                           mov eax, edi
00A9CF1E  E9 F3 03 00 00                  jmp 0x140a9d316
00A9CF23  E8 14 EC 0D 00                  call 0x140b7bb3c
00A9CF28  44 8B 05 25 EE 46 00            mov r8d, dword ptr [rip + 0x46ee25]
00A9CF2F  41 8B C8                        mov ecx, r8d
00A9CF32  45 85 C0                        test r8d, r8d
00A9CF35  74 1D                           je 0x140a9cf54
00A9CF37  83 E9 06                        sub ecx, 6
00A9CF3A  74 11                           je 0x140a9cf4d
00A9CF3C  41 2B CE                        sub ecx, r14d
00A9CF3F  74 0C                           je 0x140a9cf4d
00A9CF41  83 F9 04                        cmp ecx, 4
00A9CF44  74 07                           je 0x140a9cf4d
00A9CF46  BB 14 00 00 00                  mov ebx, 0x14
00A9CF4B  EB 0A                           jmp 0x140a9cf57
00A9CF4D  BB 15 00 00 00                  mov ebx, 0x15
00A9CF52  EB 03                           jmp 0x140a9cf57
00A9CF54  41 8B DE                        mov ebx, r14d
00A9CF57  8B 15 FB ED 46 00               mov edx, dword ptr [rip + 0x46edfb]
00A9CF5D  41 8B C8                        mov ecx, r8d
00A9CF60  E8 F7 04 00 00                  call 0x140a9d45c
00A9CF65  89 45 F0                        mov dword ptr [rbp - 0x10], eax
00A9CF68  83 FE 08                        cmp esi, 8
00A9CF6B  75 2A                           jne 0x140a9cf97
00A9CF6D  39 3D DD AA 3C 00               cmp dword ptr [rip + 0x3caadd], edi
00A9CF73  74 18                           je 0x140a9cf8d
00A9CF75  E8 96 B4 0D 00                  call 0x140b78410
00A9CF7A  8B CB                           mov ecx, ebx
00A9CF7C  E8 D7 D7 EE FF                  call 0x14098a758
00A9CF81  E8 3A B4 0D 00                  call 0x140b783c0
00A9CF86  33 C0                           xor eax, eax
00A9CF88  E9 89 03 00 00                  jmp 0x140a9d316
00A9CF8D  B8 03 A0 00 C0                  mov eax, 0xc000a003
00A9CF92  E9 7F 03 00 00                  jmp 0x140a9d316
00A9CF97  8D 46 FC                        lea eax, [rsi - 4]
00A9CF9A  83 F8 02                        cmp eax, 2
00A9CF9D  76 32                           jbe 0x140a9cfd1
00A9CF9F  41 8B CE                        mov ecx, r14d
00A9CFA2  40 88 7D B0                     mov byte ptr [rbp - 0x50], dil
00A9CFA6  40 8A F7                        mov sil, dil
00A9CFA9  E8 0A B7 A2 FF                  call 0x1404c86b8
00A9CFAE  65 48 8B 14 25 88 01 00 00      mov rdx, qword ptr gs:[0x188]
00A9CFB7  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A9CFC0  48 8B 88 B8 00 00 00            mov rcx, qword ptr [rax + 0xb8]
00A9CFC7  E8 C4 FC 0D 00                  call 0x140b7cc90
00A9CFCC  89 45 BC                        mov dword ptr [rbp - 0x44], eax
00A9CFCF  EB 07                           jmp 0x140a9cfd8
00A9CFD1  41 8A F6                        mov sil, r14b
00A9CFD4  44 88 75 B0                     mov byte ptr [rbp - 0x50], r14b
00A9CFD8  40 38 3D 49 96 46 00            cmp byte ptr [rip + 0x469649], dil
00A9CFDF  74 08                           je 0x140a9cfe9
00A9CFE1  40 84 F6                        test sil, sil
00A9CFE4  40 8A F7                        mov sil, dil
00A9CFE7  74 03                           je 0x140a9cfec
00A9CFE9  41 8A F6                        mov sil, r14b
00A9CFEC  41 8B C4                        mov eax, r12d
00A9CFEF  41 0B C6                        or eax, r14d
00A9CFF2  45 8B F4                        mov r14d, r12d
00A9CFF5  41 83 E6 FE                     and r14d, 0xfffffffe
00A9CFF9  45 85 E4                        test r12d, r12d
00A9CFFC  44 0F 49 F0                     cmovns r14d, eax
00A9D000  40 84 F6                        test sil, sil
00A9D003  74 07                           je 0x140a9d00c
00A9D005  80 25 34 ED 46 00 FD            and byte ptr [rip + 0x46ed34], 0xfd
00A9D00C  44 8A 25 ED ED 46 00            mov r12b, byte ptr [rip + 0x46eded]
00A9D013  E8 F8 B3 0D 00                  call 0x140b78410
00A9D018  E8 DF A4 9D FF                  call 0x1404774fc
00A9D01D  45 84 FF                        test r15b, r15b
00A9D020  75 1D                           jne 0x140a9d03f
00A9D022  40 84 F6                        test sil, sil
00A9D025  75 18                           jne 0x140a9d03f
00A9D027  45 84 E4                        test r12b, r12b
00A9D02A  75 07                           jne 0x140a9d033
00A9D02C  B1 01                           mov cl, 1
00A9D02E  E8 F5 C6 01 00                  call 0x140ab9728
00A9D033  41 B7 01                        mov r15b, 1
00A9D036  40 88 3D C3 F2 46 00            mov byte ptr [rip + 0x46f2c3], dil
00A9D03D  EB 10                           jmp 0x140a9d04f
00A9D03F  44 8A FF                        mov r15b, dil
00A9D042  40 88 3D B7 F2 46 00            mov byte ptr [rip + 0x46f2b7], dil
00A9D049  40 38 7D 40                     cmp byte ptr [rbp + 0x40], dil
00A9D04D  75 4A                           jne 0x140a9d099
00A9D04F  40 38 7D B0                     cmp byte ptr [rbp - 0x50], dil
00A9D053  75 54                           jne 0x140a9d0a9
00A9D055  33 D2                           xor edx, edx
00A9D057  48 8D 0D A2 F2 46 00            lea rcx, [rip + 0x46f2a2]
00A9D05E  41 B8 80 03 00 00               mov r8d, 0x380
00A9D064  E8 D7 9B C2 FF                  call 0x1406c6c40
00A9D069  8B 15 E9 EC 46 00               mov edx, dword ptr [rip + 0x46ece9]
00A9D06F  8B 0D DF EC 46 00               mov ecx, dword ptr [rip + 0x46ecdf]
00A9D075  E8 7E A4 01 00                  call 0x140ab74f8
00A9D07A  33 C9                           xor ecx, ecx
00A9D07C  E8 5F 17 8E FF                  call 0x14037e7e0
00A9D081  48 89 05 80 F2 46 00            mov qword ptr [rip + 0x46f280], rax
00A9D088  E8 C3 7E 02 00                  call 0x140ac4f50
00A9D08D  B9 01 00 00 00                  mov ecx, 1
00A9D092  E8 F9 AB 0D 00                  call 0x140b77c90
00A9D097  EB 06                           jmp 0x140a9d09f
00A9D099  40 38 7D B0                     cmp byte ptr [rbp - 0x50], dil
00A9D09D  75 0A                           jne 0x140a9d0a9
00A9D09F  B9 01 00 00 00                  mov ecx, 1
00A9D0A4  E8 53 B6 00 00                  call 0x140aa86fc
00A9D0A9  40 84 F6                        test sil, sil
00A9D0AC  74 1B                           je 0x140a9d0c9
00A9D0AE  8B 5D 48                        mov ebx, dword ptr [rbp + 0x48]
00A9D0B1  45 8B C6                        mov r8d, r14d
00A9D0B4  8B CB                           mov ecx, ebx
00A9D0B6  41 8B D5                        mov edx, r13d
00A9D0B9  E8 E2 DF 0B 00                  call 0x140b5b0a0
00A9D0BE  44 8A 65 40                     mov r12b, byte ptr [rbp + 0x40]
00A9D0C2  8B F0                           mov esi, eax
00A9D0C4  E9 92 01 00 00                  jmp 0x140a9d25b
00A9D0C9  8A 45 40                        mov al, byte ptr [rbp + 0x40]
00A9D0CC  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00A9D0D0  88 45 D0                        mov byte ptr [rbp - 0x30], al
00A9D0D3  33 D2                           xor edx, edx
00A9D0D5  8B 45 48                        mov eax, dword ptr [rbp + 0x48]
00A9D0D8  89 45 D4                        mov dword ptr [rbp - 0x2c], eax
00A9D0DB  44 89 6D D8                     mov dword ptr [rbp - 0x28], r13d
00A9D0DF  44 89 75 DC                     mov dword ptr [rbp - 0x24], r14d
00A9D0E3  89 5D E4                        mov dword ptr [rbp - 0x1c], ebx
00A9D0E6  C7 45 E0 01 00 00 00            mov dword ptr [rbp - 0x20], 1
00A9D0ED  E8 9A 53 E7 FF                  call 0x14091248c
00A9D0F2  8B F0                           mov esi, eax
00A9D0F4  8A 45 40                        mov al, byte ptr [rbp + 0x40]
00A9D0F7  84 C0                           test al, al
00A9D0F9  75 21                           jne 0x140a9d11c
00A9D0FB  85 F6                           test esi, esi
00A9D0FD  78 0E                           js 0x140a9d10d
00A9D0FF  45 84 E4                        test r12b, r12b
00A9D102  75 09                           jne 0x140a9d10d
00A9D104  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00A9D108  E8 AF AF A2 FF                  call 0x1404c80bc
00A9D10D  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00A9D111  E8 8A FB 02 00                  call 0x140accca0
00A9D116  89 45 B4                        mov dword ptr [rbp - 0x4c], eax
00A9D119  8A 45 40                        mov al, byte ptr [rbp + 0x40]
00A9D11C  85 F6                           test esi, esi
00A9D11E  0F 88 BE 00 00 00               js 0x140a9d1e2
00A9D124  84 C0                           test al, al
00A9D126  0F 85 B6 00 00 00               jne 0x140a9d1e2
00A9D12C  41 8B CE                        mov ecx, r14d
00A9D12F  41 8B DE                        mov ebx, r14d
00A9D132  C1 F9 1F                        sar ecx, 0x1f
00A9D135  4D 8B C5                        mov r8, r13
00A9D138  83 E1 02                        and ecx, 2
00A9D13B  8B D1                           mov edx, ecx
00A9D13D  83 CA 04                        or edx, 4
00A9D140  83 E3 08                        and ebx, 8
00A9D143  0F 44 D1                        cmove edx, ecx
00A9D146  33 C9                           xor ecx, ecx
00A9D148  E8 4B DB 0D 00                  call 0x140b7ac98
00A9D14D  C6 05 A0 F5 46 00 01            mov byte ptr [rip + 0x46f5a0], 1
00A9D154  F0 09 3C 24                     lock or dword ptr [rsp], edi
00A9D158  45 84 E4                        test r12b, r12b
00A9D15B  75 12                           jne 0x140a9d16f
00A9D15D  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00A9D161  E8 A2 1E CC FF                  call 0x14075f008
00A9D166  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00A9D16A  E8 ED 1E CC FF                  call 0x14075f05c
00A9D16F  85 DB                           test ebx, ebx
00A9D171  74 07                           je 0x140a9d17a
00A9D173  B1 01                           mov cl, 1
00A9D175  E8 36 7F D1 FF                  call 0x1407b50b0
00A9D17A  41 8B D5                        mov edx, r13d
00A9D17D  41 8B CE                        mov ecx, r14d
00A9D180  E8 53 6E 02 00                  call 0x140ac3fd8
00A9D185  8B 4D 48                        mov ecx, dword ptr [rbp + 0x48]
00A9D188  45 8B C6                        mov r8d, r14d
00A9D18B  41 8B D5                        mov edx, r13d
00A9D18E  E8 0D DF 0B 00                  call 0x140b5b0a0
00A9D193  8B F0                           mov esi, eax
00A9D195  E8 26 B2 0D 00                  call 0x140b783c0
00A9D19A  8A 1D 60 EC 46 00               mov bl, byte ptr [rip + 0x46ec60]
00A9D1A0  E8 6B B2 0D 00                  call 0x140b78410
00A9D1A5  40 88 3D 48 F5 46 00            mov byte ptr [rip + 0x46f548], dil
00A9D1AC  F0 09 3C 24                     lock or dword ptr [rsp], edi
00A9D1B0  84 DB                           test bl, bl
00A9D1B2  75 1E                           jne 0x140a9d1d2
00A9D1B4  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00A9D1B8  E8 53 52 E7 FF                  call 0x140912410
00A9D1BD  33 C9                           xor ecx, ecx
00A9D1BF  E8 64 C5 01 00                  call 0x140ab9728
00A9D1C4  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00A9D1C8  44 8A FF                        mov r15b, dil
00A9D1CB  E8 2C 1A CC FF                  call 0x14075ebfc
00A9D1D0  EB 03                           jmp 0x140a9d1d5
00A9D1D2  44 8A FF                        mov r15b, dil
00A9D1D5  33 D2                           xor edx, edx
00A9D1D7  4D 8B C5                        mov r8, r13
00A9D1DA  8D 4A 07                        lea ecx, [rdx + 7]
00A9D1DD  E8 B6 DA 0D 00                  call 0x140b7ac98
00A9D1E2  33 D2                           xor edx, edx
00A9D1E4  C7 45 E0 08 00 00 00            mov dword ptr [rbp - 0x20], 8
00A9D1EB  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00A9D1EF  E8 98 52 E7 FF                  call 0x14091248c
00A9D1F4  E8 DF 71 E7 FF                  call 0x1409143d8
00A9D1F9  44 8A 65 40                     mov r12b, byte ptr [rbp + 0x40]
00A9D1FD  45 84 E4                        test r12b, r12b
00A9D200  75 56                           jne 0x140a9d258
00A9D202  84 C0                           test al, al
00A9D204  74 38                           je 0x140a9d23e
00A9D206  E8 B5 B1 0D 00                  call 0x140b783c0
00A9D20B  8A 1D EF FE 46 00               mov bl, byte ptr [rip + 0x46feef]
00A9D211  40 88 3D E9 FE 46 00            mov byte ptr [rip + 0x46fee9], dil
00A9D218  E8 F3 B1 0D 00                  call 0x140b78410
00A9D21D  84 DB                           test bl, bl
00A9D21F  8B 5D B4                        mov ebx, dword ptr [rbp - 0x4c]
00A9D222  74 1D                           je 0x140a9d241
00A9D224  8B CB                           mov ecx, ebx
00A9D226  E8 4D D6 EE FF                  call 0x14098a878
00A9D22B  E8 90 B1 0D 00                  call 0x140b783c0
00A9D230  40 88 3D C9 FE 46 00            mov byte ptr [rip + 0x46fec9], dil
00A9D237  E8 D4 B1 0D 00                  call 0x140b78410
00A9D23C  EB 03                           jmp 0x140a9d241
00A9D23E  8B 5D B4                        mov ebx, dword ptr [rbp - 0x4c]
00A9D241  48 8D 55 E8                     lea rdx, [rbp - 0x18]
00A9D245  89 5D E8                        mov dword ptr [rbp - 0x18], ebx
00A9D248  48 8D 4D C0                     lea rcx, [rbp - 0x40]
00A9D24C  C7 45 E0 07 00 00 00            mov dword ptr [rbp - 0x20], 7
00A9D253  E8 34 52 E7 FF                  call 0x14091248c
00A9D258  8B 5D 48                        mov ebx, dword ptr [rbp + 0x48]
00A9D25B  45 84 FF                        test r15b, r15b
00A9D25E  74 07                           je 0x140a9d267
00A9D260  33 C9                           xor ecx, ecx
00A9D262  E8 C1 C4 01 00                  call 0x140ab9728
00A9D267  45 84 E4                        test r12b, r12b
00A9D26A  0F 85 84 00 00 00               jne 0x140a9d2f4
00A9D270  40 38 7D B0                     cmp byte ptr [rbp - 0x50], dil
00A9D274  75 7E                           jne 0x140a9d2f4
00A9D276  85 F6                           test esi, esi
00A9D278  78 3E                           js 0x140a9d2b8
00A9D27A  33 C9                           xor ecx, ecx
00A9D27C  E8 5F 15 8E FF                  call 0x14037e7e0
00A9D281  41 8B CE                        mov ecx, r14d
00A9D284  48 89 05 A5 F0 46 00            mov qword ptr [rip + 0x46f0a5], rax
00A9D28B  E8 24 5D FD FF                  call 0x140a72fb4
00A9D290  E8 B7 E5 FF FF                  call 0x140a9b84c
00A9D295  41 8B CE                        mov ecx, r14d
00A9D298  E8 2F 61 FD FF                  call 0x140a733cc
00A9D29D  48 89 3D EC 14 47 00            mov qword ptr [rip + 0x4714ec], rdi
00A9D2A4  89 1D CE F3 46 00               mov dword ptr [rip + 0x46f3ce], ebx
00A9D2AA  44 89 2D CB F3 46 00            mov dword ptr [rip + 0x46f3cb], r13d
00A9D2B1  C6 05 48 F0 46 00 01            mov byte ptr [rip + 0x46f048], 1
00A9D2B8  B9 29 00 00 00                  mov ecx, 0x29
00A9D2BD  E8 CE A9 0D 00                  call 0x140b77c90
00A9D2C2  33 C9                           xor ecx, ecx
00A9D2C4  C6 05 AD E2 36 00 01            mov byte ptr [rip + 0x36e2ad], 1
00A9D2CB  E8 F0 F3 A5 FF                  call 0x1404fc6c0
00A9D2D0  8D 51 01                        lea edx, [rcx + 1]
00A9D2D3  48 8D 0D 26 1E 47 00            lea rcx, [rip + 0x471e26]
00A9D2DA  E8 19 4E A0 FF                  call 0x1404a20f8
00A9D2DF  8B CE                           mov ecx, esi
00A9D2E1  E8 F6 51 03 00                  call 0x140ad24dc
00A9D2E6  44 8B 45 F0                     mov r8d, dword ptr [rbp - 0x10]
00A9D2EA  41 8B D5                        mov edx, r13d
00A9D2ED  8B CE                           mov ecx, esi
00A9D2EF  E8 D0 0E 01 00                  call 0x140aae1c4
00A9D2F4  B9 02 00 00 00                  mov ecx, 2
00A9D2F9  E8 92 A1 9D FF                  call 0x140477490
00A9D2FE  E8 BD B0 0D 00                  call 0x140b783c0
00A9D303  39 7D BC                        cmp dword ptr [rbp - 0x44], edi
00A9D306  7C 05                           jl 0x140a9d30d
00A9D308  E8 C7 C2 0D 00                  call 0x140b795d4
00A9D30D  33 C9                           xor ecx, ecx
00A9D30F  E8 A4 B3 A2 FF                  call 0x1404c86b8
00A9D314  8B C6                           mov eax, esi
00A9D316  48 8B 9C 24 C0 00 00 00         mov rbx, qword ptr [rsp + 0xc0]
00A9D31E  48 83 C4 70                     add rsp, 0x70
00A9D322  41 5F                           pop r15
00A9D324  41 5E                           pop r14
00A9D326  41 5D                           pop r13
00A9D328  41 5C                           pop r12
00A9D32A  5F                              pop rdi
00A9D32B  5E                              pop rsi
00A9D32C  5D                              pop rbp
00A9D32D  C3                              ret
00A9D32E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopIssueActionRequest(unsigned __int8 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned int v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned int v_stack_m60;
    unsigned int v_stack_m64;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m78;
    unsigned int v_stack_m7C;
    unsigned int v_stack_m84;
    unsigned __int8 v_stack_m88;
    unsigned int v_stack_mA8;
    unsigned int v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p8;

    v_stack_p18 = v_rbx;
    v_stack_p10 = a2;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (112);
    result = 0;
    v_stack_m7C = 0xC0000001ULL;
    v_rdi = 0;
    v_stack_m58 = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m84 = 0;
    v_stack_m68 = v_xmm0;
    result = PopAcquireAwaymodeLock(a1, a2, a3, a4);
    result = PopReadSystemAwayModePolicy(a1, a2, a3, a4);
    if ((*(unsigned __int8 *)(v_rip + 4652901)) != 0) goto loc_00A9CEBA;
    if ((*(unsigned __int8 *)(v_rip + 4652889)) == 0) goto loc_00A9CF23;
loc_00A9CEBA:
    if (((unsigned int)((unsigned int)(a2))) != 2) goto loc_00A9CF23;
    if (((unsigned int)((int)(a3))) >= 5) goto loc_00A9CF23;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4648585)))) & (0xFFFFFFFAULL)) != 0) goto loc_00A9CF23;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4648585)))) == ((unsigned int)(v_rdi + 1))) goto loc_00A9CF23;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4652859))) != 0) goto loc_00A9CF17;
    if ((*(unsigned __int8 *)(v_rip + 4652841)) == 0) goto loc_00A9CF03;
    if (((*(unsigned int *)(v_rip + 4653080)) & (0x4000000ULL)) == 0) goto loc_00A9CF17;
    result = PopSetSystemState((unsigned int)(a2) + 2, (unsigned int)(a2) + 5, a3, a4);
    goto loc_00A9CF17;
loc_00A9CF03:
    result = PopReleasePolicyLock((unsigned int)(a2) + 2, (unsigned int)(a2) + 5, a3, a4);
    result = PopSetSystemAwayMode((unsigned int)((unsigned int)(v_rdi + 1)), (unsigned int)(a2) + 5, a3, a4);
    result = PopAcquirePolicyLock((unsigned int)((unsigned int)(v_rdi + 1)), (unsigned int)(a2) + 5, a3, a4);
loc_00A9CF17:
    result = PopReleaseAwaymodeLock((unsigned int)((unsigned int)(v_rdi + 1)), (unsigned int)(a2) + 5, a3, a4);
    goto loc_00A9D316;
loc_00A9CF23:
    result = PopReleaseAwaymodeLock((unsigned int)((unsigned int)(v_rdi + 1)), (unsigned int)(a2) + 5, a3, a4);
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4648485))) == 0) goto loc_00A9CF54;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4648485))))) - (6));
    if (condition_is_equal) goto loc_00A9CF4D;
    a1 = (unsigned int)((a1) - ((unsigned int)(v_rdi + 1)));
    if (condition_is_equal) goto loc_00A9CF4D;
    if (a1 == 4) goto loc_00A9CF4D;
    goto loc_00A9CF57;
loc_00A9CF4D:
    goto loc_00A9CF57;
loc_00A9CF54:
loc_00A9CF57:
    result = PopPotsGetActionEntryReason((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4648485)))), (unsigned int)(*(unsigned int *)(v_rip + 4648443)), (unsigned int)(*(unsigned int *)(v_rip + 4648485)), a4);
    v_stack_m48 = (unsigned int)(result);
    if (((unsigned int)((unsigned int)(a2))) != 8) goto loc_00A9CF97;
    if ((*(unsigned int *)(v_rip + 3975901)) == ((unsigned int)((unsigned int)((unsigned int)(result))))) goto loc_00A9CF8D;
    result = PopReleasePolicyLock((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4648485)))), (unsigned int)(*(unsigned int *)(v_rip + 4648443)), (unsigned int)(*(unsigned int *)(v_rip + 4648485)), a4);
    result = PopScreenOff((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi + 1)))), (unsigned int)(*(unsigned int *)(v_rip + 4648443)), (unsigned int)(*(unsigned int *)(v_rip + 4648485)), a4);
    result = PopAcquirePolicyLock((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rdi + 1)))), (unsigned int)(*(unsigned int *)(v_rip + 4648443)), (unsigned int)(*(unsigned int *)(v_rip + 4648485)), a4);
    result = 0;
    goto loc_00A9D316;
loc_00A9CF8D:
    goto loc_00A9D316;
loc_00A9CF97:
    if (((unsigned int)((unsigned int)(a2) - 4)) <= 2) goto loc_00A9CFD1;
    v_stack_m88 = (unsigned __int8)((unsigned int)((unsigned int)(result)));
    result = PopSetPowerActionWatchdogState((unsigned int)((unsigned int)(v_rdi + 1)), (unsigned int)(*(unsigned int *)(v_rip + 4648443)), (unsigned int)(*(unsigned int *)(v_rip + 4648485)), a4);
    result = PopPushPowerStateTransitionRecord(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(*(unsigned int *)(v_rip + 4648485)), a4);
    v_stack_m7C = (unsigned int)(result);
    goto loc_00A9CFD8;
loc_00A9CFD1:
    v_stack_m88 = (unsigned __int8)(v_rdi + 1);
loc_00A9CFD8:
    if ((*(unsigned __int8 *)(v_rip + 4625993)) == ((unsigned __int8)((unsigned int)((unsigned int)(result))))) goto loc_00A9CFE9;
    v_rsi = (unsigned __int8)((unsigned int)((unsigned int)(result)));
    if ((unsigned __int8)((unsigned __int8)(v_rdi + 1)) != 0) {
        v_rsi = (unsigned __int8)(v_rdi + 1);
    }
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) | ((unsigned int)(v_rdi + 1)));
    v_r14 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a4)))) & (0xFFFFFFFEULL));
    if (!sign_flag) { v_r14 = (unsigned int)(result); }
    if ((unsigned __int8)(v_rsi) != 0) {
    }
    result = PopReleasePolicyLock(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(*(unsigned int *)(v_rip + 4648485)), a4);
    result = PpmBeginHighPerfRequest(*(unsigned __int64 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 184), *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(*(unsigned int *)(v_rip + 4648485)), a4);
    if (a1 != 0) goto loc_00A9D03F;
    if ((unsigned __int8)(v_rsi) != 0) goto loc_00A9D03F;
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 4648429)) == 0) {
        a1 = 1;
        result = PopPowerAggregatorNotifySuspendResume(a1, *(unsigned __int64 *)(gs_base + (0 + 392)), (unsigned int)(*(unsigned int *)(v_rip + 4648485)), a4);
    }
    *(unsigned __int8 *)(v_rip + 4649667) = (unsigned __int8)((unsigned int)((unsigned int)(result)));
    goto loc_00A9D04F;
loc_00A9D03F:
    *(unsigned __int8 *)(v_rip + 4649655) = (unsigned __int8)((unsigned int)((unsigned int)(result)));
    if (v_stack_p8 != ((unsigned __int8)((unsigned int)((unsigned int)(result))))) goto loc_00A9D099;
loc_00A9D04F:
    if (v_stack_m88 != ((unsigned __int8)((unsigned int)((unsigned int)(result))))) goto loc_00A9D0A9;
    a2 = 0;
    result = memset(v_rip + 4649634, a2, 896, a4);
    result = PopDiagTracePowerTransitionStart((unsigned int)(*(unsigned int *)(v_rip + 4648159)), (unsigned int)(*(unsigned int *)(v_rip + 4648169)), 896, a4);
    a1 = 0;
    result = KeQueryPerformanceCounter(a1, (unsigned int)(*(unsigned int *)(v_rip + 4648169)), 896, a4);
    *(unsigned __int64 *)(v_rip + 4649600) = result;
    result = PopEnableSystemSleepCheckpoint(a1, (unsigned int)(*(unsigned int *)(v_rip + 4648169)), 896, a4);
    result = PopCheckpointSystemSleep(1, (unsigned int)(*(unsigned int *)(v_rip + 4648169)), 896, a4);
    goto loc_00A9D09F;
loc_00A9D099:
    if (v_stack_m88 == ((unsigned __int8)((unsigned int)((unsigned int)(result))))) {
        a1 = 1;
        result = PopSetSleepMarker(a1, (unsigned int)(*(unsigned int *)(v_rip + 4648169)), 896, a4);
    }
    if ((unsigned __int8)(v_rsi) == 0) goto loc_00A9D0C9;
    result = PopTransitionSystemPowerState((unsigned int)((unsigned int)((unsigned int)(v_stack_p10))), (unsigned int)((unsigned int)((int)(a3))), (unsigned int)((unsigned int)(v_r14)), a4);
    goto loc_00A9D25B;
loc_00A9D0C9:
    v_stack_m68 = (unsigned __int8)(v_stack_p8);
    a2 = 0;
    v_stack_m64 = (unsigned int)((unsigned int)(v_stack_p10));
    v_stack_m60 = (unsigned int)((int)(a3));
    v_stack_m5C = (unsigned int)(v_r14);
    v_stack_m54 = (unsigned int)((unsigned int)(v_stack_p10));
    v_stack_m58 = 1;
    result = PopDispatchStateCallout(v_stack_m78, a2, (unsigned int)((unsigned int)(v_r14)), a4);
    if ((unsigned __int8)(v_stack_p8) != 0) goto loc_00A9D11C;
    if (sign_flag) goto loc_00A9D10D;
    result = v_stack_p8;
    if ((unsigned __int8)(v_stack_p8) == 0) {
        a1 = v_stack_m78;
        result = PopPrepareSleep(a1, a2, (unsigned int)((unsigned int)(v_r14)), a4);
    }
    result = PoBlockConsoleSwitch(v_stack_m78, a2, (unsigned int)((unsigned int)(v_r14)), a4);
    v_stack_m84 = (unsigned int)(result);
loc_00A9D11C:
    if (sign_flag) goto loc_00A9D1E2;
    if ((unsigned __int8)(v_stack_p8) != 0) goto loc_00A9D1E2;
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) >> (31));
    a1 = (unsigned int)((a1) & (2));
    a2 = (unsigned int)(((unsigned int)(a1)) | (4));
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_r14))) & (8));
    if (condition_is_equal) { a2 = a1; }
    a1 = 0;
    result = PfPowerActionNotify(a1, a2, (int)(a3), a4);
    *(unsigned __int8 *)(v_rip + 4650400) = 1;
    if ((unsigned __int8)(v_stack_p8) == 0) {
        a1 = v_stack_m78;
        result = PopSuspendApps(a1, a2, (int)(a3), a4);
        a1 = v_stack_m78;
        result = PopSuspendServices(a1, a2, (int)(a3), a4);
    }
    if ((unsigned int)(v_rbx) != 0) {
        a1 = 1;
        result = EtwShutdown(a1, a2, (int)(a3), a4);
    }
    result = PopDispatchSuperfetchNotification((unsigned int)((unsigned int)(v_r14)), (unsigned int)((unsigned int)((int)(a3))), (int)(a3), a4);
    result = PopTransitionSystemPowerState((unsigned int)(v_stack_p10), (unsigned int)((unsigned int)((int)(a3))), (unsigned int)((unsigned int)(v_r14)), a4);
    result = PopAcquirePolicyLock((unsigned int)(v_stack_p10), (unsigned int)((unsigned int)((int)(a3))), (unsigned int)((unsigned int)(v_r14)), a4);
    result = PopReleasePolicyLock((unsigned int)(v_stack_p10), (unsigned int)((unsigned int)((int)(a3))), (unsigned int)((unsigned int)(v_r14)), a4);
    *(unsigned __int8 *)(v_rip + 4650312) = (unsigned __int8)((unsigned int)((unsigned int)(result)));
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 4648032)) != 0) goto loc_00A9D1D2;
    result = PopResumeServices(v_stack_m78, (unsigned int)((unsigned int)((int)(a3))), (unsigned int)((unsigned int)(v_r14)), a4);
    a1 = 0;
    result = PopPowerAggregatorNotifySuspendResume(a1, (unsigned int)((unsigned int)((int)(a3))), (unsigned int)((unsigned int)(v_r14)), a4);
    result = PopResumeApps(v_stack_m78, (unsigned int)((unsigned int)((int)(a3))), (unsigned int)((unsigned int)(v_r14)), a4);
    goto loc_00A9D1D5;
loc_00A9D1D2:
loc_00A9D1D5:
    a2 = 0;
    result = PfPowerActionNotify(a2 + 7, a2, (int)(a3), a4);
loc_00A9D1E2:
    a2 = 0;
    v_stack_m58 = 8;
    result = PopDispatchStateCallout(v_stack_m78, a2, (int)(a3), a4);
    result = TtmIsEnabled(v_stack_m78, a2, (int)(a3), a4);
    if ((unsigned __int8)(v_stack_p8) != 0) goto loc_00A9D258;
    if ((unsigned __int8)(result) == 0) goto loc_00A9D23E;
    result = PopAcquirePolicyLock(v_stack_m78, a2, (int)(a3), a4);
    *(unsigned __int8 *)(v_rip + 4652777) = (unsigned __int8)((unsigned int)((unsigned int)(result)));
    result = PopReleasePolicyLock(v_stack_m78, a2, (int)(a3), a4);
    if ((unsigned __int8)(*(unsigned __int8 *)(v_rip + 4652783)) == 0) goto loc_00A9D241;
    result = TtmNotifyLowPowerStateExited((unsigned int)((unsigned int)((unsigned int)(v_stack_m84))), a2, (int)(a3), a4);
    result = PopAcquirePolicyLock((unsigned int)((unsigned int)((unsigned int)(v_stack_m84))), a2, (int)(a3), a4);
    *(unsigned __int8 *)(v_rip + 4652745) = (unsigned __int8)((unsigned int)((unsigned int)(result)));
    result = PopReleasePolicyLock((unsigned int)((unsigned int)((unsigned int)(v_stack_m84))), a2, (int)(a3), a4);
    goto loc_00A9D241;
loc_00A9D23E:
loc_00A9D241:
    v_stack_m50 = (unsigned int)((unsigned int)(v_stack_m84));
    v_stack_m58 = 7;
    result = PopDispatchStateCallout(v_stack_m78, v_stack_m50, (int)(a3), a4);
loc_00A9D258:
loc_00A9D25B:
    if ((unsigned __int8)((unsigned __int8)((unsigned int)((unsigned int)(result)))) != 0) {
        a1 = 0;
        result = PopPowerAggregatorNotifySuspendResume(a1, v_stack_m50, (int)(a3), a4);
    }
    if ((unsigned __int8)(v_stack_p8) != 0) goto loc_00A9D2F4;
    if (v_stack_m88 != ((unsigned __int8)((unsigned int)((unsigned int)(result))))) goto loc_00A9D2F4;
    if (!(sign_flag)) {
        a1 = 0;
        result = KeQueryPerformanceCounter(a1, v_stack_m50, (int)(a3), a4);
        a1 = (unsigned int)(v_r14);
        *(unsigned __int64 *)(v_rip + 4649125) = result;
        result = PopDiagTraceHiberStats(a1, v_stack_m50, (int)(a3), a4);
        result = PopDiagTracePowerTransitionTime(a1, v_stack_m50, (int)(a3), a4);
        a1 = (unsigned int)(v_r14);
        result = PopDiagTracePerfTrackData(a1, v_stack_m50, (int)(a3), a4);
        *(unsigned __int64 *)(v_rip + 4658412) = (unsigned int)((unsigned int)(result));
        *(unsigned int *)(v_rip + 4649934) = (unsigned int)((unsigned int)(v_stack_p10));
        *(unsigned int *)(v_rip + 4649931) = (unsigned int)((int)(a3));
        *(unsigned __int8 *)(v_rip + 4649032) = 1;
    }
    result = PopCheckpointSystemSleep(41, v_stack_m50, (int)(a3), a4);
    a1 = 0;
    *(unsigned __int8 *)(v_rip + 3596973) = 1;
    result = RtlBootStatusDisableFlushing(a1, v_stack_m50, (int)(a3), a4);
    result = PopQueueWorkItem(v_rip + 4660774, a1 + 1, (int)(a3), a4);
    result = PopDiagTracePowerTransitionEnd((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), a1 + 1, (int)(a3), a4);
    result = PopPotsLogPowerTransitionReliability((unsigned int)((unsigned int)((unsigned int)((unsigned int)(result)))), (unsigned int)((unsigned int)((int)(a3))), (unsigned int)(v_stack_m48), a4);
loc_00A9D2F4:
    result = PpmEndHighPerfRequest(2, (unsigned int)((unsigned int)((int)(a3))), (unsigned int)(v_stack_m48), a4);
    result = PopAcquirePolicyLock(2, (unsigned int)((unsigned int)((int)(a3))), (unsigned int)(v_stack_m48), a4);
    if (v_stack_m7C >= ((unsigned int)((unsigned int)((unsigned int)(result))))) {
        result = PoDelistPowerStateTransitionBlocker(2, (unsigned int)((unsigned int)((int)(a3))), (unsigned int)(v_stack_m48), a4);
    }
    a1 = 0;
    result = PopSetPowerActionWatchdogState(a1, (unsigned int)((unsigned int)((int)(a3))), (unsigned int)(v_stack_m48), a4);
loc_00A9D316:
    v_rsp = (v_rsp) + (112);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t PopIssueActionRequest(uint8_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m48;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint32_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint32_t v_stack_m60;
    uint32_t v_stack_m64;
    uint64_t v_stack_m68;
    uint64_t v_stack_m78;
    uint32_t v_stack_m7C;
    uint32_t v_stack_m84;
    uint8_t v_stack_m88;
    uint32_t v_stack_mA8;
    uint32_t v_stack_p10;
    uint64_t v_stack_p18;
    uint8_t v_stack_p8;

    v_stack_p18 = local_rbx;
    v_stack_p10 = Arg2;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (112);
    result = 0;
    v_stack_m7C = 0xC0000001ULL;
    local_rdi = 0;
    v_stack_m58 = 0;
    v_stack_m78 = v_xmm0;
    v_stack_m84 = 0;
    v_stack_m68 = v_xmm0;
    result = PopAcquireAwaymodeLock(Arg1, Arg2, Arg3, Arg4);
    result = PopReadSystemAwayModePolicy(Arg1, Arg2, Arg3, Arg4);
    if ((*(uint8_t *)(v_rip + 0x46FF65)) != 0) goto loc_00A9CEBA;
    if ((*(uint8_t *)(v_rip + 0x46FF59)) == 0) goto loc_00A9CF23;
loc_00A9CEBA:
    if (((uint32_t)((uint32_t)(Arg2))) != 2) goto loc_00A9CF23;
    if (((uint32_t)((int32_t)(Arg3))) >= 5) goto loc_00A9CF23;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x46EE89)))) & (0xFFFFFFFAULL)) != 0) goto loc_00A9CF23;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x46EE89)))) == ((uint32_t)(local_rdi + 1))) goto loc_00A9CF23;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x46FF3B))) != 0) goto loc_00A9CF17;
    if ((*(uint8_t *)(v_rip + 0x46FF29)) == 0) goto loc_00A9CF03;
    if (((*(uint32_t *)(v_rip + 0x470018)) & (0x4000000ULL)) == 0) goto loc_00A9CF17;
    result = PopSetSystemState((uint32_t)(Arg2) + 2, (uint32_t)(Arg2) + 5, Arg3, Arg4);
    goto loc_00A9CF17;
loc_00A9CF03:
    result = PopReleasePolicyLock((uint32_t)(Arg2) + 2, (uint32_t)(Arg2) + 5, Arg3, Arg4);
    result = PopSetSystemAwayMode((uint32_t)((uint32_t)(local_rdi + 1)), (uint32_t)(Arg2) + 5, Arg3, Arg4);
    result = PopAcquirePolicyLock((uint32_t)((uint32_t)(local_rdi + 1)), (uint32_t)(Arg2) + 5, Arg3, Arg4);
loc_00A9CF17:
    result = PopReleaseAwaymodeLock((uint32_t)((uint32_t)(local_rdi + 1)), (uint32_t)(Arg2) + 5, Arg3, Arg4);
    goto loc_00A9D316;
loc_00A9CF23:
    result = PopReleaseAwaymodeLock((uint32_t)((uint32_t)(local_rdi + 1)), (uint32_t)(Arg2) + 5, Arg3, Arg4);
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x46EE25))) == 0) goto loc_00A9CF54;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x46EE25))))) - (6));
    if (condition_is_equal) goto loc_00A9CF4D;
    Arg1 = (uint32_t)((Arg1) - ((uint32_t)(local_rdi + 1)));
    if (condition_is_equal) goto loc_00A9CF4D;
    if (Arg1 == 4) goto loc_00A9CF4D;
    goto loc_00A9CF57;
loc_00A9CF4D:
    goto loc_00A9CF57;
loc_00A9CF54:
loc_00A9CF57:
    result = PopPotsGetActionEntryReason((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x46EE25)))), (uint32_t)(*(uint32_t *)(v_rip + 0x46EDFB)), (uint32_t)(*(uint32_t *)(v_rip + 0x46EE25)), Arg4);
    v_stack_m48 = (uint32_t)(result);
    if (((uint32_t)((uint32_t)(Arg2))) != 8) goto loc_00A9CF97;
    if ((*(uint32_t *)(v_rip + 0x3CAADD)) == ((uint32_t)((uint32_t)((uint32_t)(result))))) goto loc_00A9CF8D;
    result = PopReleasePolicyLock((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x46EE25)))), (uint32_t)(*(uint32_t *)(v_rip + 0x46EDFB)), (uint32_t)(*(uint32_t *)(v_rip + 0x46EE25)), Arg4);
    result = PopScreenOff((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi + 1)))), (uint32_t)(*(uint32_t *)(v_rip + 0x46EDFB)), (uint32_t)(*(uint32_t *)(v_rip + 0x46EE25)), Arg4);
    result = PopAcquirePolicyLock((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rdi + 1)))), (uint32_t)(*(uint32_t *)(v_rip + 0x46EDFB)), (uint32_t)(*(uint32_t *)(v_rip + 0x46EE25)), Arg4);
    result = 0;
    goto loc_00A9D316;
loc_00A9CF8D:
    goto loc_00A9D316;
loc_00A9CF97:
    if (((uint32_t)((uint32_t)(Arg2) - 4)) <= 2) goto loc_00A9CFD1;
    v_stack_m88 = (uint8_t)((uint32_t)((uint32_t)(result)));
    result = PopSetPowerActionWatchdogState((uint32_t)((uint32_t)(local_rdi + 1)), (uint32_t)(*(uint32_t *)(v_rip + 0x46EDFB)), (uint32_t)(*(uint32_t *)(v_rip + 0x46EE25)), Arg4);
    result = PopPushPowerStateTransitionRecord(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(*(uint32_t *)(v_rip + 0x46EE25)), Arg4);
    v_stack_m7C = (uint32_t)(result);
    goto loc_00A9CFD8;
loc_00A9CFD1:
    v_stack_m88 = (uint8_t)(local_rdi + 1);
loc_00A9CFD8:
    if ((*(uint8_t *)(v_rip + 0x469649)) == ((uint8_t)((uint32_t)((uint32_t)(result))))) goto loc_00A9CFE9;
    local_rsi = (uint8_t)((uint32_t)((uint32_t)(result)));
    if ((uint8_t)((uint8_t)(local_rdi + 1)) != 0) {
        local_rsi = (uint8_t)(local_rdi + 1);
    }
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) | ((uint32_t)(local_rdi + 1)));
    local_r14 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg4)))) & (0xFFFFFFFEULL));
    if (!sign_flag) { local_r14 = (uint32_t)(result); }
    if ((uint8_t)(local_rsi) != 0) {
    }
    result = PopReleasePolicyLock(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(*(uint32_t *)(v_rip + 0x46EE25)), Arg4);
    result = PpmBeginHighPerfRequest(*(uint64_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0xB8), *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(*(uint32_t *)(v_rip + 0x46EE25)), Arg4);
    if (Arg1 != 0) goto loc_00A9D03F;
    if ((uint8_t)(local_rsi) != 0) goto loc_00A9D03F;
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x46EDED)) == 0) {
        Arg1 = 1;
        result = PopPowerAggregatorNotifySuspendResume(Arg1, *(uint64_t *)(gs_base + (0 + 0x188)), (uint32_t)(*(uint32_t *)(v_rip + 0x46EE25)), Arg4);
    }
    *(uint8_t *)(v_rip + 0x46F2C3) = (uint8_t)((uint32_t)((uint32_t)(result)));
    goto loc_00A9D04F;
loc_00A9D03F:
    *(uint8_t *)(v_rip + 0x46F2B7) = (uint8_t)((uint32_t)((uint32_t)(result)));
    if (v_stack_p8 != ((uint8_t)((uint32_t)((uint32_t)(result))))) goto loc_00A9D099;
loc_00A9D04F:
    if (v_stack_m88 != ((uint8_t)((uint32_t)((uint32_t)(result))))) goto loc_00A9D0A9;
    Arg2 = 0;
    result = memset(v_rip + 4649634, Arg2, 896, Arg4);
    result = PopDiagTracePowerTransitionStart((uint32_t)(*(uint32_t *)(v_rip + 0x46ECDF)), (uint32_t)(*(uint32_t *)(v_rip + 0x46ECE9)), 896, Arg4);
    Arg1 = 0;
    result = KeQueryPerformanceCounter(Arg1, (uint32_t)(*(uint32_t *)(v_rip + 0x46ECE9)), 896, Arg4);
    *(uint64_t *)(v_rip + 0x46F280) = result;
    result = PopEnableSystemSleepCheckpoint(Arg1, (uint32_t)(*(uint32_t *)(v_rip + 0x46ECE9)), 896, Arg4);
    result = PopCheckpointSystemSleep(1, (uint32_t)(*(uint32_t *)(v_rip + 0x46ECE9)), 896, Arg4);
    goto loc_00A9D09F;
loc_00A9D099:
    if (v_stack_m88 == ((uint8_t)((uint32_t)((uint32_t)(result))))) {
        Arg1 = 1;
        result = PopSetSleepMarker(Arg1, (uint32_t)(*(uint32_t *)(v_rip + 0x46ECE9)), 896, Arg4);
    }
    if ((uint8_t)(local_rsi) == 0) goto loc_00A9D0C9;
    result = PopTransitionSystemPowerState((uint32_t)((uint32_t)((uint32_t)(v_stack_p10))), (uint32_t)((uint32_t)((int32_t)(Arg3))), (uint32_t)((uint32_t)(local_r14)), Arg4);
    goto loc_00A9D25B;
loc_00A9D0C9:
    v_stack_m68 = (uint8_t)(v_stack_p8);
    Arg2 = 0;
    v_stack_m64 = (uint32_t)((uint32_t)(v_stack_p10));
    v_stack_m60 = (uint32_t)((int32_t)(Arg3));
    v_stack_m5C = (uint32_t)(local_r14);
    v_stack_m54 = (uint32_t)((uint32_t)(v_stack_p10));
    v_stack_m58 = 1;
    result = PopDispatchStateCallout(v_stack_m78, Arg2, (uint32_t)((uint32_t)(local_r14)), Arg4);
    if ((uint8_t)(v_stack_p8) != 0) goto loc_00A9D11C;
    if (sign_flag) goto loc_00A9D10D;
    result = v_stack_p8;
    if ((uint8_t)(v_stack_p8) == 0) {
        Arg1 = v_stack_m78;
        result = PopPrepareSleep(Arg1, Arg2, (uint32_t)((uint32_t)(local_r14)), Arg4);
    }
    result = PoBlockConsoleSwitch(v_stack_m78, Arg2, (uint32_t)((uint32_t)(local_r14)), Arg4);
    v_stack_m84 = (uint32_t)(result);
loc_00A9D11C:
    if (sign_flag) goto loc_00A9D1E2;
    if ((uint8_t)(v_stack_p8) != 0) goto loc_00A9D1E2;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) >> (31));
    Arg1 = (uint32_t)((Arg1) & (2));
    Arg2 = (uint32_t)(((uint32_t)(Arg1)) | (4));
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(local_r14))) & (8));
    if (condition_is_equal) { Arg2 = Arg1; }
    Arg1 = 0;
    result = PfPowerActionNotify(Arg1, Arg2, (int32_t)(Arg3), Arg4);
    *(uint8_t *)(v_rip + 0x46F5A0) = 1;
    if ((uint8_t)(v_stack_p8) == 0) {
        Arg1 = v_stack_m78;
        result = PopSuspendApps(Arg1, Arg2, (int32_t)(Arg3), Arg4);
        Arg1 = v_stack_m78;
        result = PopSuspendServices(Arg1, Arg2, (int32_t)(Arg3), Arg4);
    }
    if ((uint32_t)(local_rbx) != 0) {
        Arg1 = 1;
        result = EtwShutdown(Arg1, Arg2, (int32_t)(Arg3), Arg4);
    }
    result = PopDispatchSuperfetchNotification((uint32_t)((uint32_t)(local_r14)), (uint32_t)((uint32_t)((int32_t)(Arg3))), (int32_t)(Arg3), Arg4);
    result = PopTransitionSystemPowerState((uint32_t)(v_stack_p10), (uint32_t)((uint32_t)((int32_t)(Arg3))), (uint32_t)((uint32_t)(local_r14)), Arg4);
    result = PopAcquirePolicyLock((uint32_t)(v_stack_p10), (uint32_t)((uint32_t)((int32_t)(Arg3))), (uint32_t)((uint32_t)(local_r14)), Arg4);
    result = PopReleasePolicyLock((uint32_t)(v_stack_p10), (uint32_t)((uint32_t)((int32_t)(Arg3))), (uint32_t)((uint32_t)(local_r14)), Arg4);
    *(uint8_t *)(v_rip + 0x46F548) = (uint8_t)((uint32_t)((uint32_t)(result)));
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x46EC60)) != 0) goto loc_00A9D1D2;
    result = PopResumeServices(v_stack_m78, (uint32_t)((uint32_t)((int32_t)(Arg3))), (uint32_t)((uint32_t)(local_r14)), Arg4);
    Arg1 = 0;
    result = PopPowerAggregatorNotifySuspendResume(Arg1, (uint32_t)((uint32_t)((int32_t)(Arg3))), (uint32_t)((uint32_t)(local_r14)), Arg4);
    result = PopResumeApps(v_stack_m78, (uint32_t)((uint32_t)((int32_t)(Arg3))), (uint32_t)((uint32_t)(local_r14)), Arg4);
    goto loc_00A9D1D5;
loc_00A9D1D2:
loc_00A9D1D5:
    Arg2 = 0;
    result = PfPowerActionNotify(Arg2 + 7, Arg2, (int32_t)(Arg3), Arg4);
loc_00A9D1E2:
    Arg2 = 0;
    v_stack_m58 = 8;
    result = PopDispatchStateCallout(v_stack_m78, Arg2, (int32_t)(Arg3), Arg4);
    result = TtmIsEnabled(v_stack_m78, Arg2, (int32_t)(Arg3), Arg4);
    if ((uint8_t)(v_stack_p8) != 0) goto loc_00A9D258;
    if ((uint8_t)(result) == 0) goto loc_00A9D23E;
    result = PopAcquirePolicyLock(v_stack_m78, Arg2, (int32_t)(Arg3), Arg4);
    *(uint8_t *)(v_rip + 0x46FEE9) = (uint8_t)((uint32_t)((uint32_t)(result)));
    result = PopReleasePolicyLock(v_stack_m78, Arg2, (int32_t)(Arg3), Arg4);
    if ((uint8_t)(*(uint8_t *)(v_rip + 0x46FEEF)) == 0) goto loc_00A9D241;
    result = TtmNotifyLowPowerStateExited((uint32_t)((uint32_t)((uint32_t)(v_stack_m84))), Arg2, (int32_t)(Arg3), Arg4);
    result = PopAcquirePolicyLock((uint32_t)((uint32_t)((uint32_t)(v_stack_m84))), Arg2, (int32_t)(Arg3), Arg4);
    *(uint8_t *)(v_rip + 0x46FEC9) = (uint8_t)((uint32_t)((uint32_t)(result)));
    result = PopReleasePolicyLock((uint32_t)((uint32_t)((uint32_t)(v_stack_m84))), Arg2, (int32_t)(Arg3), Arg4);
    goto loc_00A9D241;
loc_00A9D23E:
loc_00A9D241:
    v_stack_m50 = (uint32_t)((uint32_t)(v_stack_m84));
    v_stack_m58 = 7;
    result = PopDispatchStateCallout(v_stack_m78, v_stack_m50, (int32_t)(Arg3), Arg4);
loc_00A9D258:
loc_00A9D25B:
    if ((uint8_t)((uint8_t)((uint32_t)((uint32_t)(result)))) != 0) {
        Arg1 = 0;
        result = PopPowerAggregatorNotifySuspendResume(Arg1, v_stack_m50, (int32_t)(Arg3), Arg4);
    }
    if ((uint8_t)(v_stack_p8) != 0) goto loc_00A9D2F4;
    if (v_stack_m88 != ((uint8_t)((uint32_t)((uint32_t)(result))))) goto loc_00A9D2F4;
    if (!(sign_flag)) {
        Arg1 = 0;
        result = KeQueryPerformanceCounter(Arg1, v_stack_m50, (int32_t)(Arg3), Arg4);
        Arg1 = (uint32_t)(local_r14);
        *(uint64_t *)(v_rip + 0x46F0A5) = result;
        result = PopDiagTraceHiberStats(Arg1, v_stack_m50, (int32_t)(Arg3), Arg4);
        result = PopDiagTracePowerTransitionTime(Arg1, v_stack_m50, (int32_t)(Arg3), Arg4);
        Arg1 = (uint32_t)(local_r14);
        result = PopDiagTracePerfTrackData(Arg1, v_stack_m50, (int32_t)(Arg3), Arg4);
        *(uint64_t *)(v_rip + 0x4714EC) = (uint32_t)((uint32_t)(result));
        *(uint32_t *)(v_rip + 0x46F3CE) = (uint32_t)((uint32_t)(v_stack_p10));
        *(uint32_t *)(v_rip + 0x46F3CB) = (uint32_t)((int32_t)(Arg3));
        *(uint8_t *)(v_rip + 0x46F048) = 1;
    }
    result = PopCheckpointSystemSleep(41, v_stack_m50, (int32_t)(Arg3), Arg4);
    Arg1 = 0;
    *(uint8_t *)(v_rip + 0x36E2AD) = 1;
    result = RtlBootStatusDisableFlushing(Arg1, v_stack_m50, (int32_t)(Arg3), Arg4);
    result = PopQueueWorkItem(v_rip + 4660774, Arg1 + 1, (int32_t)(Arg3), Arg4);
    result = PopDiagTracePowerTransitionEnd((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), Arg1 + 1, (int32_t)(Arg3), Arg4);
    result = PopPotsLogPowerTransitionReliability((uint32_t)((uint32_t)((uint32_t)((uint32_t)(result)))), (uint32_t)((uint32_t)((int32_t)(Arg3))), (uint32_t)(v_stack_m48), Arg4);
loc_00A9D2F4:
    result = PpmEndHighPerfRequest(2, (uint32_t)((uint32_t)((int32_t)(Arg3))), (uint32_t)(v_stack_m48), Arg4);
    result = PopAcquirePolicyLock(2, (uint32_t)((uint32_t)((int32_t)(Arg3))), (uint32_t)(v_stack_m48), Arg4);
    if (v_stack_m7C >= ((uint32_t)((uint32_t)((uint32_t)(result))))) {
        result = PoDelistPowerStateTransitionBlocker(2, (uint32_t)((uint32_t)((int32_t)(Arg3))), (uint32_t)(v_stack_m48), Arg4);
    }
    Arg1 = 0;
    result = PopSetPowerActionWatchdogState(Arg1, (uint32_t)((uint32_t)((int32_t)(Arg3))), (uint32_t)(v_stack_m48), Arg4);
loc_00A9D316:
    local_rsp = (local_rsp) + (112);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A9CE54&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
