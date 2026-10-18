# PpmPerfCheckForIllegalProcessorThrottle

- RVA: `0x0044B700`–`0x0044B71B` (길이 `27` bytes)
- VA: `0x000000014044B700`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A66D4`
- 디코드: `6`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PpmPerfSnapDeliveredPerformance](../2D/PpmPerfSnapDeliveredPerformance_function_002D7F30.md) at `0x002D8226`

### Static image references
- `0x0044B706` → RVA `0x00E0B3EC` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0044B719` → [sub_0044B794](Unknown_function_0044B794.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0044B700  40 53                           push rbx
0044B702  48 83 EC 20                     sub rsp, 0x20
0044B706  83 3D DF FC 9B 00 00            cmp dword ptr [rip + 0x9bfcdf], 0
0044B70D  48 8B D9                        mov rbx, rcx
0044B710  48 C7 44 24 30 00 00 00 00      mov qword ptr [rsp + 0x30], 0
0044B719  74 79                           je 0x14044b794
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall PpmPerfCheckForIllegalProcessorThrottle(__int64 a1)
{
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (32);
    v_stack_p8 = 0;
}
```

## 5. (Beta) C Style

```c
void PpmPerfCheckForIllegalProcessorThrottle(int64_t Arg1)
{
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (32);
    v_stack_p8 = 0;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0044B700&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0044B700[BB_0044B700]
```
