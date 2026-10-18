# PopDeepSleepEnabled

- RVA: `0x0049E5E0`–`0x0049E5EC` (길이 `12` bytes)
- VA: `0x000000014049E5E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `4`개 명령, `12/12` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PopDripsWatchdogDiagnosticWorker](../../page/76/PopDripsWatchdogDiagnosticWorker_function_0076C600.md) at `0x0076C785`
- [PopDripsWatchdogUpdateMetrics](../../page/76/PopDripsWatchdogUpdateMetrics_function_0076C830.md) at `0x0076C92A`
- [PopCheckResiliencyScenarios](../../page/A3/PopCheckResiliencyScenarios_function_00A31718.md) at `0x00A31769`
- [PopCheckResiliencyScenarios](../../page/A3/PopCheckResiliencyScenarios_function_00A31718.md) at `0x00A31782`
- [PopCheckResiliencyScenarios](../../page/A3/PopCheckResiliencyScenarios_function_00A31718.md) at `0x00A317B3`
- [PopEnforceDeepSleep](../../page/AC/PopEnforceDeepSleep_function_00AC3E1C.md) at `0x00AC3E37`

### Static image references
- `0x0049E5E0` → RVA `0x00F092F2` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0049E5E0  80 3D 0B AD A6 00 00            cmp byte ptr [rip + 0xa6ad0b], 0
0049E5E7  0F 95 C0                        setne al
0049E5EA  C3                              ret
0049E5EB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDeepSleepEnabled(void)
{
    __int64 result;

    result = ((*(unsigned __int8 *)(v_rip + 10923275)) != 0) ? 1 : 0;
    return result;
}
```

## 5. (Beta) C Style

```c
void PopDeepSleepEnabled(void)
{
    int64_t result;

    result = ((*(uint8_t *)(v_rip + 0xA6AD0B)) != 0) ? 1 : 0;
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0049E5E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0049E5E0[BB_0049E5E0]
  bb_0049E5EB[BB_0049E5EB]
```
