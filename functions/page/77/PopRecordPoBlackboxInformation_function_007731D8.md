# PopRecordPoBlackboxInformation

- RVA: `0x007731D8`–`0x007731F1` (길이 `25` bytes)
- VA: `0x00000001407731D8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007731DC` → [PopRecordPoIrpBlackboxInformation](../../text/4C/PopRecordPoIrpBlackboxInformation_function_004CE14C.md) (function, `0x004CE14C`)
- `0x007731E1` → [PopRecordPepWorkorderBlackboxInformation](../../text/5D/PopRecordPepWorkorderBlackboxInformation_function_005DF8F8.md) (function, `0x005DF8F8`)
- `0x007731E6` → [PopRecordPowerWatchdogBlackboxInformation](../../text/4D/PopRecordPowerWatchdogBlackboxInformation_function_004D3A18.md) (function, `0x004D3A18`)

### Direct callers
- [PopPowerButtonWorkCallback](../../text/5D/PopPowerButtonWorkCallback_function_005D9A70.md) at `0x005D9C2A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x007731DC` → [PopRecordPoIrpBlackboxInformation](../../text/4C/PopRecordPoIrpBlackboxInformation_function_004CE14C.md) (`PAGE` → `.text`)
  - `0x007731E1` → [PopRecordPepWorkorderBlackboxInformation](../../text/5D/PopRecordPepWorkorderBlackboxInformation_function_005DF8F8.md) (`PAGE` → `.text`)
  - `0x007731E6` → [PopRecordPowerWatchdogBlackboxInformation](../../text/4D/PopRecordPowerWatchdogBlackboxInformation_function_004D3A18.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007731D8  48 83 EC 28                     sub rsp, 0x28
007731DC  E8 6B AF D5 FF                  call 0x1404ce14c
007731E1  E8 12 C7 E6 FF                  call 0x1405df8f8
007731E6  E8 2D 08 D6 FF                  call 0x1404d3a18
007731EB  48 83 C4 28                     add rsp, 0x28
007731EF  C3                              ret
007731F0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopRecordPoBlackboxInformation(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PopRecordPoIrpBlackboxInformation(a1, a2, a3, a4);
    result = PopRecordPepWorkorderBlackboxInformation(a1, a2, a3, a4);
    result = PopRecordPowerWatchdogBlackboxInformation(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PopRecordPoBlackboxInformation(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PopRecordPoIrpBlackboxInformation(a1, a2, a3, a4);
    result = PopRecordPepWorkorderBlackboxInformation(a1, a2, a3, a4);
    result = PopRecordPowerWatchdogBlackboxInformation(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007731D8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007731D8[BB_007731D8]
  bb_007731F0[BB_007731F0]
```
