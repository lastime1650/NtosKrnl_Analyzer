# PopQueryPowerButtonSuppressionCount

- RVA: `0x00ABC338`–`0x00ABC342` (길이 `10` bytes)
- VA: `0x0000000140ABC338`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `4`개 명령, `10/10` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PopCaptureSleepStudyStatistics](../../text/43/PopCaptureSleepStudyStatistics_function_004399F4.md) at `0x00439EEF`
- [PopCalculateCsSummary](../../text/43/PopCalculateCsSummary_function_0043A1B0.md) at `0x0043A44C`

### Static image references
- `0x00ABC338` → RVA `0x00F09220` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ABC338  8B 05 E2 CE 44 00               mov eax, dword ptr [rip + 0x44cee2]
00ABC33E  89 01                           mov dword ptr [rcx], eax
00ABC340  C3                              ret
00ABC341  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopQueryPowerButtonSuppressionCount(__int64 a1)
{
    *(unsigned int *)(a1) = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 4509410)));
    return (unsigned int)(*(unsigned int *)(v_rip + 4509410));
}
```

## 5. (Beta) C Style

```c
int64_t PopQueryPowerButtonSuppressionCount(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    *(uint32_t *)(arg1) = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x44CEE2)));
    return (uint32_t)(*(uint32_t *)(v_rip + 0x44CEE2));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ABC338&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00ABC338[BB_00ABC338]
  bb_00ABC341[BB_00ABC341]
```
