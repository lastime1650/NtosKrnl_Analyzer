# PopChangeCapability

- RVA: `0x0090FF48`–`0x0090FF5D` (길이 `21` bytes)
- VA: `0x000000014090FF48`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0090FF52` → [PopResetCurrentPolicies](PopResetCurrentPolicies_function_0090FF64.md) (function, `0x0090FF64`)

### Direct callers
- [PopThermalZoneAdd](../75/PopThermalZoneAdd_function_0075F980.md) at `0x0075FA98`
- [PopThermalZoneRemove](../75/PopThermalZoneRemove_function_0075FAD0.md) at `0x0075FBED`
- [PopPolicyDeviceHandleWakeAlarmNotification](../76/PopPolicyDeviceHandleWakeAlarmNotification_function_007660A4.md) at `0x007663AB`
- [PopPolicyDeviceHandleWakeAlarmNotification](../76/PopPolicyDeviceHandleWakeAlarmNotification_function_007660A4.md) at `0x007663C2`
- [PopBatteryAdd](../76/PopBatteryAdd_function_00766580.md) at `0x007665C9`
- [PopBatteryRemove](../76/PopBatteryRemove_function_00766D40.md) at `0x00766DE5`
- [PopBatteryUpdateTestExempt](../76/PopBatteryUpdateTestExempt_function_00766F54.md) at `0x00767161`
- [PopBatteryUpdateTestExempt](../76/PopBatteryUpdateTestExempt_function_00766F54.md) at `0x00767235`
- [PdcPoReportButton](../76/PdcPoReportButton_function_007694A0.md) at `0x007694CA`
- [PdcPoReportButton](../76/PdcPoReportButton_function_007694A0.md) at `0x007694E6`
- [PdcPoReportButton](../76/PdcPoReportButton_function_007694A0.md) at `0x00769502`
- [NtPowerInformation](../95/NtPowerInformation_function_00955D80.md) at `0x00956541`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0090FF48  48 83 EC 28                     sub rsp, 0x28
0090FF4C  38 11                           cmp byte ptr [rcx], dl
0090FF4E  74 07                           je 0x14090ff57
0090FF50  88 11                           mov byte ptr [rcx], dl
0090FF52  E8 0D 00 00 00                  call 0x14090ff64
0090FF57  48 83 C4 28                     add rsp, 0x28
0090FF5B  C3                              ret
0090FF5C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopChangeCapability(__int64 a1, unsigned __int8 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int8 *)(a1)) != a2) {
        *(unsigned __int8 *)(a1) = a2;
        result = PopResetCurrentPolicies(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopChangeCapability(void *Arg1, uint8_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint8_t *)(arg1)) != Arg2) {
        *(uint8_t *)(arg1) = Arg2;
        result = PopResetCurrentPolicies(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `8` | `R` |
| `Arg1` | `+ 0x0` | `8` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0090FF48&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0090FF48[BB_0090FF48]
  bb_0090FF50[BB_0090FF50]
  bb_0090FF57[BB_0090FF57]
  bb_0090FF5C[BB_0090FF5C]
  bb_0090FF48 -->|branch| bb_0090FF57
  bb_0090FF48 -->|fallthrough| bb_0090FF50
  bb_0090FF50 -->|flow| bb_0090FF57
```
