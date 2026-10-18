# PpmReleaseLock

- RVA: `0x002DA428`–`0x002DA4B4` (길이 `140` bytes)
- VA: `0x00000001402DA428`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `32`개 명령, `140/140` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **44**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002DA43E` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)
- `0x002DA464` → [KiAcquireThreadLockRaiseToDpc](../39/KiAcquireThreadLockRaiseToDpc_function_00396280.md) (function, `0x00396280`)
- `0x002DA47A` → [KiClearPriorityFloor](../39/KiClearPriorityFloor_function_00396314.md) (function, `0x00396314`)
- `0x002DA49A` → [KiProcessDeferredReadyList](../25/KiProcessDeferredReadyList_function_00250800.md) (function, `0x00250800`)
- `0x002DA4A8` → [KeLeaveCriticalRegionThread](../25/KeLeaveCriticalRegionThread_function_0025EFF0.md) (function, `0x0025EFF0`)

### Direct callers
- [PpmIdleUpdateSystemLatencyLimit](PpmIdleUpdateSystemLatencyLimit_function_002D9204.md) at `0x002D9443`
- [PpmCheckRun](PpmCheckRun_function_002DA0C0.md) at `0x002DA156`
- [PpmMediaBufferingWorker](PpmMediaBufferingWorker_function_002DA680.md) at `0x002DA6E6`
- [PpmRegisterPerfCap](../42/PpmRegisterPerfCap_function_0042B0D0.md) at `0x0042B1EA`
- [PopDeepSleepEvaluateCallback](../46/PopDeepSleepEvaluateCallback_function_00469F10.md) at `0x00469FB5`
- [PoNotifyVSyncChange](../46/PoNotifyVSyncChange_function_00469FD0.md) at `0x00469FF6`
- [PpmCheckPausePpmEngineForSx](../49/PpmCheckPausePpmEngineForSx_function_00499104.md) at `0x00499135`
- [PpmCheckResumePpmEngineFromSx](../49/PpmCheckResumePpmEngineFromSx_function_00499148.md) at `0x004991DE`
- [PpmParkSetLpiCap](../4D/PpmParkSetLpiCap_function_004D9358.md) at `0x004D949A`
- [PpmSetExitLatencySamplingPercentage](../4D/PpmSetExitLatencySamplingPercentage_function_004DA9B0.md) at `0x004DA9FA`
- [PpmPerfGetVmPerfConfig](../4D/PpmPerfGetVmPerfConfig_function_004DE504.md) at `0x004DE6EB`
- [PpmClearExitLatencySamplingPercentage](../4E/PpmClearExitLatencySamplingPercentage_function_004E1538.md) at `0x004E1565`
- [PpmPerfGetVmCppcConfig](../5D/PpmPerfGetVmCppcConfig_function_005D41A8.md) at `0x005D4425`
- [PpmPerfGetVmPerfPriorityConfig](../5D/PpmPerfGetVmPerfPriorityConfig_function_005D4454.md) at `0x005D44C8`
- [PpmPerfGetVmPerfPrioritySupport](../../page/75/PpmPerfGetVmPerfPrioritySupport_function_0075AD28.md) at `0x0075AD71`
- [PpmPerfTelemetryWorker](../../page/75/PpmPerfTelemetryWorker_function_0075AED0.md) at `0x0075AFA3`
- [PpmRegisterPerfStates](../../page/75/PpmRegisterPerfStates_function_0075B084.md) at `0x0075B56A`
- [PpmUpdatePerfStates](../../page/75/PpmUpdatePerfStates_function_0075BD90.md) at `0x0075BE46`
- [PpmParkApplyForcedMask](../../page/76/PpmParkApplyForcedMask_function_0076A904.md) at `0x0076A9BB`
- [PpmParkClearForcedMask](../../page/76/PpmParkClearForcedMask_function_0076AB20.md) at `0x0076AB5B`
- [PpmDisableProfile](../../page/77/PpmDisableProfile_function_00770858.md) at `0x00770910`
- [PpmRegisterProfiles](../../page/77/PpmRegisterProfiles_function_007709F0.md) at `0x00770BA4`
- [PpmPerfRegisterHvPerfStateCounters](../../page/77/PpmPerfRegisterHvPerfStateCounters_function_00770C40.md) at `0x00770D11`
- [PpmInfoReleaseLocks](../../page/91/PpmInfoReleaseLocks_function_00916154.md) at `0x00916165`
- [PopWnfFullscreenVideoCallback](../../page/A4/PopWnfFullscreenVideoCallback_function_00A49EB0.md) at `0x00A49F83`
- [PpmEventTraceControlCallback](../../page/A5/PpmEventTraceControlCallback_function_00A51F60.md) at `0x00A522A6`
- [PpmApplyProfile](../../page/A5/PpmApplyProfile_function_00A52B08.md) at `0x00A52B8C`
- [PpmCompareAndApplyPolicySettings](../../page/A5/PpmCompareAndApplyPolicySettings_function_00A52CEC.md) at `0x00A52ED0`
- [PpmReapplyPerfPolicy](../../page/A5/PpmReapplyPerfPolicy_function_00A53148.md) at `0x00A53311`
- [PpmPerfGetFrequencyBandStats](../../page/A5/PpmPerfGetFrequencyBandStats_function_00A542B0.md) at `0x00A543AB`
- [PpmIdleGetConcurrencyStats](../../page/A7/PpmIdleGetConcurrencyStats_function_00A798E4.md) at `0x00A799AB`
- [PpmIdleGetPackageIdleIntervalStats](../../page/A7/PpmIdleGetPackageIdleIntervalStats_function_00A7EE4C.md) at `0x00A7EEF2`
- [PpmCheckInitProcessors](../../page/A8/PpmCheckInitProcessors_function_00A84AE8.md) at `0x00A84CC9`
- [PopPowerInformationInternal](../../page/A8/PopPowerInformationInternal_function_00A8B7C0.md) at `0x00A8C0FB`
- [PpmPerfUpdateDomainPolicy](../../page/A9/PpmPerfUpdateDomainPolicy_function_00A97030.md) at `0x00A971BA`
- [PdcPoPpmResetProfile](../../page/AB/PdcPoPpmResetProfile_function_00ABA420.md) at `0x00ABA45D`
- [PopEnforceResiliencyScenarios](../../page/AC/PopEnforceResiliencyScenarios_function_00AC3D90.md) at `0x00AC3DB9`
- [PpmSetSimulatedLoad](../../page/AC/PpmSetSimulatedLoad_function_00ACD710.md) at `0x00ACD7F2`
- [PpmClearSimulatedLoad](../../page/AC/PpmClearSimulatedLoad_function_00ACE938.md) at `0x00ACE9EA`
- [PpmPerfGetBrandedFrequency](../../page/AD/PpmPerfGetBrandedFrequency_function_00AD4900.md) at `0x00AD49A0`
- [PpmPerfGetVmPerfControlSupport](../../page/AD/PpmPerfGetVmPerfControlSupport_function_00ADB2BC.md) at `0x00ADB322`
- [sub_00B39B7E](../../page/B3/Unknown_function_00B39B7E.md) at `0x00B39B85`
- [PpmInitPolicyConfiguration](../../init/C4/PpmInitPolicyConfiguration_function_00C40708.md) at `0x00C408C3`
- [PoInitSystem](../../init/C7/PoInitSystem_function_00C72358.md) at `0x00C72E22`
- [PoInitSystem](../../init/C7/PoInitSystem_function_00C72358.md) at `0x00C72E74`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002DA428  40 53                           push rbx
002DA42A  48 83 EC 20                     sub rsp, 0x20
002DA42E  48 8B 19                        mov rbx, qword ptr [rcx]
002DA431  45 33 C0                        xor r8d, r8d
002DA434  48 83 21 00                     and qword ptr [rcx], 0
002DA438  33 D2                           xor edx, edx
002DA43A  48 83 C1 08                     add rcx, 8
002DA43E  E8 CD 4E 06 00                  call 0x14033f310
002DA443  48 85 DB                        test rbx, rbx
002DA446  74 65                           je 0x1402da4ad
002DA448  65 48 8B 1C 25 88 01 00 00      mov rbx, qword ptr gs:[0x188]
002DA451  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
002DA456  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
002DA45C  48 8B CB                        mov rcx, rbx
002DA45F  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
002DA464  E8 17 BE 0B 00                  call 0x140396280
002DA469  41 B1 01                        mov r9b, 1
002DA46C  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
002DA471  41 B8 16 00 00 00               mov r8d, 0x16
002DA477  48 8B CB                        mov rcx, rbx
002DA47A  E8 95 BE 0B 00                  call 0x140396314
002DA47F  48 C7 43 40 00 00 00 00         mov qword ptr [rbx + 0x40], 0
002DA487  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
002DA48C  65 48 8B 0C 25 20 00 00 00      mov rcx, qword ptr gs:[0x20]
002DA495  44 8A 44 24 30                  mov r8b, byte ptr [rsp + 0x30]
002DA49A  E8 61 63 F7 FF                  call 0x140250800
002DA49F  65 48 8B 0C 25 88 01 00 00      mov rcx, qword ptr gs:[0x188]
002DA4A8  E8 43 4B F8 FF                  call 0x14025eff0
002DA4AD  48 83 C4 20                     add rsp, 0x20
002DA4B1  5B                              pop rbx
002DA4B2  C3                              ret
002DA4B3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmReleaseLock(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    a1 = (a1) + (8);
    result = KeSetEvent(a1, a2, a3, a4);
    v_rbx = *(unsigned __int64 *)(a1);
    if (*(unsigned __int64 *)(a1) != 0) {
        v_rbx = *(unsigned __int64 *)(gs_base + (0 + 392));
        a2 = v_stack_p8;
        a1 = v_rbx;
        v_stack_p8 = 0;
        result = KiAcquireThreadLockRaiseToDpc(a1, a2, a3, a4);
        a4 = 1;
        a2 = v_stack_p10;
        a3 = 22;
        a1 = v_rbx;
        result = KiClearPriorityFloor(a1, a2, a3, a4);
        *(unsigned __int64 *)(v_rbx + 64) = 0;
        a2 = v_stack_p10;
        a1 = *(unsigned __int64 *)(gs_base + (0 + 32));
        a3 = v_stack_p8;
        result = KiProcessDeferredReadyList(a1, a2, a3, a4);
        a1 = *(unsigned __int64 *)(gs_base + (0 + 392));
        result = KeLeaveCriticalRegionThread(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PpmReleaseLock(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    Arg1 = (Arg1) + (8);
    result = KeSetEvent(Arg1, Arg2, Arg3, a4);
    local_rbx = *(uint64_t *)(arg1);
    if (*(uint64_t *)(arg1) != 0) {
        local_rbx = *(uint64_t *)(gs_base + (0 + 0x188));
        Arg2 = v_stack_p8;
        Arg1 = local_rbx;
        v_stack_p8 = 0;
        result = KiAcquireThreadLockRaiseToDpc(Arg1, Arg2, Arg3, a4);
        a4 = 1;
        Arg2 = v_stack_p10;
        Arg3 = 22;
        Arg1 = local_rbx;
        result = KiClearPriorityFloor(Arg1, Arg2, Arg3, a4);
        *(uint64_t *)(local_rbx + 0x40) = 0;
        Arg2 = v_stack_p10;
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x20));
        Arg3 = v_stack_p8;
        result = KiProcessDeferredReadyList(Arg1, Arg2, Arg3, a4);
        Arg1 = *(uint64_t *)(gs_base + (0 + 0x188));
        result = KeLeaveCriticalRegionThread(Arg1, Arg2, Arg3, a4);
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
| `Arg1` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002DA428&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002DA428[BB_002DA428]
  bb_002DA448[BB_002DA448]
  bb_002DA4AD[BB_002DA4AD]
  bb_002DA4B3[BB_002DA4B3]
  bb_002DA428 -->|branch| bb_002DA4AD
  bb_002DA428 -->|fallthrough| bb_002DA448
  bb_002DA448 -->|flow| bb_002DA4AD
```
