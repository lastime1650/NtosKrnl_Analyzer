# PoUserShutdownCancelled

- RVA: `0x007051C0`–`0x007051DD` (길이 `29` bytes)
- VA: `0x00000001407051C0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007051C4` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x007051D2` → [PopSwitchUpdateUserShutdownScenarioState](../75/PopSwitchUpdateUserShutdownScenarioState_function_0075F260.md) (function, `0x0075F260`)

### Direct callers
- [PopPowerInformationInternal](../A8/PopPowerInformationInternal_function_00A8B7C0.md) at `0x00A8C5EA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007051C4` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007051C0  48 83 EC 28                     sub rsp, 0x28
007051C4  E8 17 11 D3 FF                  call 0x1404362e0
007051C9  84 C0                           test al, al
007051CB  75 0A                           jne 0x1407051d7
007051CD  B9 01 00 00 00                  mov ecx, 1
007051D2  E8 89 A0 05 00                  call 0x14075f260
007051D7  48 83 C4 28                     add rsp, 0x28
007051DB  C3                              ret
007051DC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PoUserShutdownCancelled(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PsIsCurrentThreadInServerSilo(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) {
        a1 = 1;
        result = PopSwitchUpdateUserShutdownScenarioState(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PoUserShutdownCancelled(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PsIsCurrentThreadInServerSilo(a1, a2, a3, a4);
    if ((uint8_t)(result) == 0) {
        a1 = 1;
        result = PopSwitchUpdateUserShutdownScenarioState(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007051C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007051C0[BB_007051C0]
  bb_007051CD[BB_007051CD]
  bb_007051D7[BB_007051D7]
  bb_007051DC[BB_007051DC]
  bb_007051C0 -->|branch| bb_007051D7
  bb_007051C0 -->|fallthrough| bb_007051CD
  bb_007051CD -->|flow| bb_007051D7
```
