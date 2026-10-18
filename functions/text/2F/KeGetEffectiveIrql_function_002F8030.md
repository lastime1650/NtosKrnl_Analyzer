# KeGetEffectiveIrql

- RVA: `0x002F8030`–`0x002F804F` (길이 `31` bytes)
- VA: `0x00000001402F8030`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00072520`
- 디코드: `12`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **41**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002F8034` → [KeAreInterruptsEnabled](KeAreInterruptsEnabled_function_002F8060.md) (function, `0x002F8060`)

### Direct callers
- [KiRcuFlushCompleted](../20/KiRcuFlushCompleted_function_0020AD38.md) at `0x0020AD67`
- [ObpPushStackInfo](../21/ObpPushStackInfo_function_002109E4.md) at `0x00210A5B`
- [EtwpEventWriteFull](../22/EtwpEventWriteFull_function_00225C10.md) at `0x00225E8E`
- [EtwpEventWriteFull](../22/EtwpEventWriteFull_function_00225C10.md) at `0x00226417`
- [IopReleaseFileObjectLock](../25/IopReleaseFileObjectLock_function_00250A90.md) at `0x00250EE7`
- [RtlpWalkFrameChain](RtlpWalkFrameChain_function_002F3ED0.md) at `0x002F4B3B`
- [ObfDereferenceObjectWithTag](ObfDereferenceObjectWithTag_function_002F78E0.md) at `0x002F7A3A`
- [ObfDereferenceObject](ObfDereferenceObject_function_002F9350.md) at `0x002F94D2`
- [NtTraceEvent](NtTraceEvent_function_002FA6C0.md) at `0x002FB1E3`
- [EtwpReserveTraceBuffer](EtwpReserveTraceBuffer_function_002FC8C0.md) at `0x002FCBAC`
- [EtwpReserveTraceBuffer](EtwpReserveTraceBuffer_function_002FC8C0.md) at `0x002FCC6A`
- [EtwTraceEvent](EtwTraceEvent_function_002FD290.md) at `0x002FD346`
- [EtwpRequestFlushTimer](EtwpRequestFlushTimer_function_002FE6B0.md) at `0x002FE6C9`
- [CmFcManagerNotifyFeatureUsage](../37/CmFcManagerNotifyFeatureUsage_function_00378598.md) at `0x003785B2`
- [ObpDeferObjectDeletion](../3A/ObpDeferObjectDeletion_function_003A2394.md) at `0x003A23D2`
- [RtlpIsFrameInBoundsEx](../41/RtlpIsFrameInBoundsEx_function_00415510.md) at `0x0041566C`
- [EtwpGetStackExtendedHeaderItem](../44/EtwpGetStackExtendedHeaderItem_function_00443D70.md) at `0x00443DF1`
- [EtwTelemetryCoverageReport](../46/EtwTelemetryCoverageReport_function_00460430.md) at `0x00460471`
- [PnpIsSafeToExamineUserModeTeb](../47/PnpIsSafeToExamineUserModeTeb_function_00478CF0.md) at `0x00478D41`
- [WheaIsCriticalState](../48/WheaIsCriticalState_function_004849A0.md) at `0x004849A4`
- [CmFcManagerRecordFeatureUsage](../49/CmFcManagerRecordFeatureUsage_function_0049C7B4.md) at `0x0049C7D6`
- [CmFcpManagerArmFeatureUsageProviderFlushNotification](../49/CmFcpManagerArmFeatureUsageProviderFlushNotification_function_0049C978.md) at `0x0049C9D3`
- [EtwpSendTraceEvent](../4B/EtwpSendTraceEvent_function_004B6E10.md) at `0x004B6E4C`
- [RtlQueryFeatureConfiguration](../4B/RtlQueryFeatureConfiguration_function_004BDD10.md) at `0x004BDD41`
- [RtlRegisterFeatureConfigurationChangeNotification](../4D/RtlRegisterFeatureConfigurationChangeNotification_function_004D6350.md) at `0x004D6370`
- [KeTryToInsertQueueApc](../4D/KeTryToInsertQueueApc_function_004D72B8.md) at `0x004D72EE`
- [EtwpContextRegisterTracingDispatcher](../4D/EtwpContextRegisterTracingDispatcher_function_004D83F4.md) at `0x004D842B`
- [KdPowerTransitionEx](../4D/KdPowerTransitionEx_function_004D9150.md) at `0x004D91CB`
- [KdPowerTransitionEx](../4D/KdPowerTransitionEx_function_004D9150.md) at `0x004D9242`
- [sub_0050C0E0](../50/Unknown_function_0050C0E0.md) at `0x0050C203`
- [sub_0050C0E0](../50/Unknown_function_0050C0E0.md) at `0x0050C242`
- [sub_0050C0E0](../50/Unknown_function_0050C0E0.md) at `0x0050C252`
- [sub_0050C0E0](../50/Unknown_function_0050C0E0.md) at `0x0050C28C`
- [sub_0050C0E0](../50/Unknown_function_0050C0E0.md) at `0x0051A85E`
- [sub_0050C0E0](../50/Unknown_function_0050C0E0.md) at `0x0051A88F`
- [sub_0050C0E0](../50/Unknown_function_0050C0E0.md) at `0x0051A8C0`
- [sub_0050C0E0](../50/Unknown_function_0050C0E0.md) at `0x0051ABD7`
- [KeResumeClockTimerSafe](../5B/KeResumeClockTimerSafe_function_005BB334.md) at `0x005BB33A`
- [KeSuspendClockTimerSafe](../5B/KeSuspendClockTimerSafe_function_005BB394.md) at `0x005BB3A3`
- [KiSrcuFlushCompleted](../5C/KiSrcuFlushCompleted_function_005C22B4.md) at `0x005C22D5`
- [KiGetRecoveryInformation](../5C/KiGetRecoveryInformation_function_005C7794.md) at `0x005C77C4`
- [RtlQueryInternalFeatureConfiguration](../5E/RtlQueryInternalFeatureConfiguration_function_005E7500.md) at `0x005E752E`
- [EtwSendTraceBuffer](../65/EtwSendTraceBuffer_function_00651560.md) at `0x0065165D`
- [EtwpDisableCompression](../65/EtwpDisableCompression_function_006534F8.md) at `0x00653529`
- [EtwpReenableCompression](../65/EtwpReenableCompression_function_00653768.md) at `0x00653783`
- [sub_006DFB24](../6D/Unknown_function_006DFB24.md) at `0x006DFBD2`
- [sub_006DFE7E](../6D/Unknown_function_006DFE7E.md) at `0x006DFE9F`
- [sub_006E9870](../6E/Unknown_function_006E9870.md) at `0x006E9880`
- [EtwInitialize](../../page/7B/EtwInitialize_function_007B4D40.md) at `0x007B4E26`
- [EtwpStopLoggerInstance](../../page/9B/EtwpStopLoggerInstance_function_009BEB94.md) at `0x009BEF03`
- [EtwpSynchronizeWithLogger](../../page/A6/EtwpSynchronizeWithLogger_function_00A66250.md) at `0x00A6627A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002F8030  48 83 EC 28                     sub rsp, 0x28
002F8034  E8 27 00 00 00                  call 0x1402f8060
002F8039  84 C0                           test al, al
002F803B  74 0A                           je 0x1402f8047
002F803D  44 0F 20 C0                     mov rax, cr8
002F8041  48 83 C4 28                     add rsp, 0x28
002F8045  C3                              ret
002F8046  CC                              int3
002F8047  B0 0F                           mov al, 0xf
002F8049  48 83 C4 28                     add rsp, 0x28
002F804D  C3                              ret
002F804E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeGetEffectiveIrql(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = KeAreInterruptsEnabled(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_002F8047;
    v_rsp = (v_rsp) + (40);
    return v_cr8;
loc_002F8047:
    v_rsp = (v_rsp) + (40);
    return 15;
}
```

## 5. (Beta) C Style

```c
void KeGetEffectiveIrql(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = KeAreInterruptsEnabled(a1, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_002F8047;
    local_rsp = (local_rsp) + (40);
    return v_cr8;
loc_002F8047:
    local_rsp = (local_rsp) + (40);
    return 15;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002F8030&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002F8030[BB_002F8030]
  bb_002F803D[BB_002F803D]
  bb_002F8046[BB_002F8046]
  bb_002F8047[BB_002F8047]
  bb_002F804E[BB_002F804E]
  bb_002F8030 -->|branch| bb_002F8047
  bb_002F8030 -->|fallthrough| bb_002F803D
  bb_002F8046 -->|flow| bb_002F8047
```
