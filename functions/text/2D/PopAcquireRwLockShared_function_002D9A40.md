# PopAcquireRwLockShared

- RVA: `0x002D9A40`–`0x002D9A9E` (길이 `94` bytes)
- VA: `0x00000001402D9A40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00068D5C`
- 디코드: `28`개 명령, `94/94` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **43**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002D9A63` → [KeAbPreAcquire](../21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x002D9A84` → [ExfAcquirePushLockSharedEx](../21/ExfAcquirePushLockSharedEx_function_0021044C.md) (function, `0x0021044C`)

### Direct callers
- [PpmIdleUpdateSystemLatencyLimit](PpmIdleUpdateSystemLatencyLimit_function_002D9204.md) at `0x002D92A5`
- [PopThermalUpdateTimerPolicy](../43/PopThermalUpdateTimerPolicy_function_00430BEC.md) at `0x00430C19`
- [PpmQueryPlatformStateResidency](../43/PpmQueryPlatformStateResidency_function_0043AEF4.md) at `0x0043AF5B`
- [PoIssueCoalescingNotification](../44/PoIssueCoalescingNotification_function_0044D670.md) at `0x0044D6A8`
- [PopThermalTraceRundownEvents](../4A/PopThermalTraceRundownEvents_function_004AF1A8.md) at `0x004AF1B9`
- [PopFanSxEntry](../4B/PopFanSxEntry_function_004BEF04.md) at `0x004BEF1A`
- [PopFanSxExit](../4D/PopFanSxExit_function_004DAA14.md) at `0x004DAA2A`
- [PopThermalSxEntry](../4E/PopThermalSxEntry_function_004E3D20.md) at `0x004E3D71`
- [PopThermalSxExit](../5D/PopThermalSxExit_function_005D55F8.md) at `0x005D56C7`
- [PopThermalTelemetryWorker](../5D/PopThermalTelemetryWorker_function_005D57F0.md) at `0x005D5810`
- [PoQueryPowerLimitAttributes](../../page/75/PoQueryPowerLimitAttributes_function_00755A70.md) at `0x00755AA5`
- [PopPowerAggregatorHandleModernStandbyIntent](../../page/76/PopPowerAggregatorHandleModernStandbyIntent_function_007649F0.md) at `0x00764A76`
- [PopBatteryEtwCallback](../../page/76/PopBatteryEtwCallback_function_00766800.md) at `0x00766810`
- [PopEtProcessEnumSnapshotCallback](../../page/91/PopEtProcessEnumSnapshotCallback_function_0091CCA0.md) at `0x0091CD51`
- [PopEtProcessEnumSnapshotCallback](../../page/91/PopEtProcessEnumSnapshotCallback_function_0091CCA0.md) at `0x0091CD95`
- [PopEtInternerLock](../../page/98/PopEtInternerLock_function_0098DEC0.md) at `0x0098DEDE`
- [PopEtGetNextEnergyTracker](../../page/98/PopEtGetNextEnergyTracker_function_0098E384.md) at `0x0098E3A3`
- [PpmWmiGetAllData](../../page/9E/PpmWmiGetAllData_function_009E1470.md) at `0x009E14CB`
- [PoThermalCounterSetCallback](../../page/A0/PoThermalCounterSetCallback_function_00A0E350.md) at `0x00A0E392`
- [PopProcessorInformation](../../page/A1/PopProcessorInformation_function_00A11CA0.md) at `0x00A11D03`
- [PopCurrentPowerState](../../page/A3/PopCurrentPowerState_function_00A356D8.md) at `0x00A356E8`
- [PopDiagTraceControlCallback](../../page/A3/PopDiagTraceControlCallback_function_00A38CB0.md) at `0x00A38D1A`
- [PpmEventTraceControlCallback](../../page/A5/PpmEventTraceControlCallback_function_00A51F60.md) at `0x00A522BC`
- [PopAcquirePowerRequestPushLock](../../page/A6/PopAcquirePowerRequestPushLock_function_00A66D94.md) at `0x00A66DAE`
- [PopBatteryDeviceState](../../page/A7/PopBatteryDeviceState_function_00A7905C.md) at `0x00A79172`
- [PopBatteryDeviceState](../../page/A7/PopBatteryDeviceState_function_00A7905C.md) at `0x00A7917E`
- [PopBootBatteryStatusWorker](../../page/A8/PopBootBatteryStatusWorker_function_00A86FA0.md) at `0x00A86FC1`
- [PopFanReadFanNoiseInfo](../../page/A9/PopFanReadFanNoiseInfo_function_00A91138.md) at `0x00A91176`
- [PopGetPowerRequestListInfo](../../page/A9/PopGetPowerRequestListInfo_function_00A92948.md) at `0x00A92971`
- [PopTransitionTelemetryOsState](../../page/A9/PopTransitionTelemetryOsState_function_00A9DD40.md) at `0x00A9DF3D`
- [PopMeasureEnergyChange](../../page/A9/PopMeasureEnergyChange_function_00A9E230.md) at `0x00A9E24C`
- [PoQueryProcessEnergyTrackingState](../../page/AA/PoQueryProcessEnergyTrackingState_function_00AAC8D0.md) at `0x00AAC91C`
- [PopThermalZoneUpdateCoolingPolicy](../../page/AB/PopThermalZoneUpdateCoolingPolicy_function_00AB1584.md) at `0x00AB159A`
- [PopGetEnergyCounter](../../page/AB/PopGetEnergyCounter_function_00AB1BA4.md) at `0x00AB1BB4`
- [PopEsStartTelemetry](../../page/AC/PopEsStartTelemetry_function_00AC5B20.md) at `0x00AC5B54`
- [PopIsDetailedSleepReliabilityDiagEnabled](../../page/AC/PopIsDetailedSleepReliabilityDiagEnabled_function_00ACEEA4.md) at `0x00ACEEB1`
- [PopDirectedDripsUmMarkTestDevices](../../page/AC/PopDirectedDripsUmMarkTestDevices_function_00ACF828.md) at `0x00ACF856`
- [PopEsEnterSleepShutdown](../../page/AD/PopEsEnterSleepShutdown_function_00AD168C.md) at `0x00AD1697`
- [PopSleepstudyCaptureResiliencyStatistics](../../page/AD/PopSleepstudyCaptureResiliencyStatistics_function_00AD6B74.md) at `0x00AD6BD3`
- [PopBatteryWorker](../../page/AE/PopBatteryWorker_function_00AE1650.md) at `0x00AE16D6`
- [PopCurrentSystemPowerSourceState](../../page/AE/PopCurrentSystemPowerSourceState_function_00AE2D3C.md) at `0x00AE2D4C`
- [PopQueryLastStateTransitionInfo](../../pagelk/B7/PopQueryLastStateTransitionInfo_function_00B707A8.md) at `0x00B707CA`
- [PopIsStateTransitionBlockingThread](../../pagelk/B7/PopIsStateTransitionBlockingThread_function_00B79380.md) at `0x00B7938F`
- [PopDiagInitialize](../../init/C3/PopDiagInitialize_function_00C3F2C0.md) at `0x00C3F3D1`
- [PopFanReportBootStartDevices](../../init/C4/PopFanReportBootStartDevices_function_00C4289C.md) at `0x00C428AD`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002D9A40  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
002D9A45  57                              push rdi
002D9A46  48 83 EC 20                     sub rsp, 0x20
002D9A4A  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
002D9A53  45 33 C0                        xor r8d, r8d
002D9A56  33 D2                           xor edx, edx
002D9A58  48 8B F9                        mov rdi, rcx
002D9A5B  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
002D9A62  90                              nop
002D9A63  E8 C8 67 F3 FF                  call 0x140210230
002D9A68  48 8B D8                        mov rbx, rax
002D9A6B  B9 11 00 00 00                  mov ecx, 0x11
002D9A70  33 C0                           xor eax, eax
002D9A72  F0 48 0F B1 0F                  lock cmpxchg qword ptr [rdi], rcx
002D9A77  74 10                           je 0x1402d9a89
002D9A79  4C 8B CF                        mov r9, rdi
002D9A7C  4C 8B C3                        mov r8, rbx
002D9A7F  33 D2                           xor edx, edx
002D9A81  48 8B CF                        mov rcx, rdi
002D9A84  E8 C3 69 F3 FF                  call 0x14021044c
002D9A89  48 85 DB                        test rbx, rbx
002D9A8C  74 04                           je 0x1402d9a92
002D9A8E  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
002D9A92  48 8B 5C 24 38                  mov rbx, qword ptr [rsp + 0x38]
002D9A97  48 83 C4 20                     add rsp, 0x20
002D9A9B  5F                              pop rdi
002D9A9C  C3                              ret
002D9A9D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopAcquireRwLockShared(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1, a2, a3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = a1;
        a3 = 0;
        a2 = 0;
        a1 = a1;
        result = ExfAcquirePushLockSharedEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopAcquireRwLockShared(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1, Arg2, Arg3, a4);
    result = 0;
    if (!(condition_is_equal)) {
        a4 = Arg1;
        Arg3 = 0;
        Arg2 = 0;
        Arg1 = Arg1;
        result = ExfAcquirePushLockSharedEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002D9A40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002D9A40[BB_002D9A40]
  bb_002D9A79[BB_002D9A79]
  bb_002D9A89[BB_002D9A89]
  bb_002D9A8E[BB_002D9A8E]
  bb_002D9A92[BB_002D9A92]
  bb_002D9A9D[BB_002D9A9D]
  bb_002D9A40 -->|branch| bb_002D9A89
  bb_002D9A40 -->|fallthrough| bb_002D9A79
  bb_002D9A79 -->|flow| bb_002D9A89
  bb_002D9A89 -->|branch| bb_002D9A92
  bb_002D9A89 -->|fallthrough| bb_002D9A8E
  bb_002D9A8E -->|flow| bb_002D9A92
```
