# HalProcessorIdle

- RVA: `0x006AC7C0`–`0x006AC7D0` (길이 `16` bytes)
- VA: `0x00000001406AC7C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BFAE0`
- 디코드: `6`개 명령, `16/16` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006AC7C4` → [HalpTimerResetProfileAdjustment](../54/HalpTimerResetProfileAdjustment_function_0054B660.md) (function, `0x0054B660`)

### Direct callers
- [PpmIdleDefaultExecute](../4A/PpmIdleDefaultExecute_function_004AF670.md) at `0x004AF696`
- [PpmIdleGuestExecute](../4B/PpmIdleGuestExecute_function_004BD260.md) at `0x004BD269`
- [KiHaltOnAddress](../4F/KiHaltOnAddress_function_004FBA3C.md) at `0x004FBAE0`
- [KiExecuteSmtIsolationThread](../5C/KiExecuteSmtIsolationThread_function_005C4070.md) at `0x005C41E6`
- [sub_006D8D08](../6D/Unknown_function_006D8D08.md) at `0x006D8D11`
- [sub_006DCDC2](../6D/Unknown_function_006DCDC2.md) at `0x006DCDD1`
- [sub_006DCDC2](../6D/Unknown_function_006DCDC2.md) at `0x006DCEB8`
- [sub_006ED39E](../6E/Unknown_function_006ED39E.md) at `0x006ED3B0`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006AC7C0  48 83 EC 28                     sub rsp, 0x28
006AC7C4  E8 97 EE E9 FF                  call 0x14054b660
006AC7C9  48 83 C4 28                     add rsp, 0x28
006AC7CD  FB                              sti
006AC7CE  F4                              hlt
006AC7CF  C3                              ret
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalProcessorIdle(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = HalpTimerResetProfileAdjustment(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void HalProcessorIdle(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = HalpTimerResetProfileAdjustment(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006AC7C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006AC7C0[BB_006AC7C0]
```
