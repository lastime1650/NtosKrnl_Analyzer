# PoUserShutdownInitiated

- RVA: `0x00AB81D0`–`0x00AB81EF` (길이 `31` bytes)
- VA: `0x0000000140AB81D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00090138`
- 디코드: `10`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00AB81D4` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (function, `0x004362E0`)
- `0x00AB81E8` → [PopSwitchUpdateUserShutdownScenarioState](../75/PopSwitchUpdateUserShutdownScenarioState_function_0075F260.md) (function, `0x0075F260`)

### Direct callers
- [PopPowerInformationInternal](../A8/PopPowerInformationInternal_function_00A8B7C0.md) at `0x00A8C5E0`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00AB81D4` → [PsIsCurrentThreadInServerSilo](../../text/43/PsIsCurrentThreadInServerSilo_function_004362E0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AB81D0  48 83 EC 28                     sub rsp, 0x28
00AB81D4  E8 07 E1 97 FF                  call 0x1404362e0
00AB81D9  84 C0                           test al, al
00AB81DB  74 06                           je 0x140ab81e3
00AB81DD  48 83 C4 28                     add rsp, 0x28
00AB81E1  C3                              ret
00AB81E2  CC                              int3
00AB81E3  B9 03 00 00 00                  mov ecx, 3
00AB81E8  E8 73 70 CA FF                  call 0x14075f260
00AB81ED  EB EE                           jmp 0x140ab81dd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PoUserShutdownInitiated(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PsIsCurrentThreadInServerSilo(a1, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00AB81E3;
loc_00AB81DD:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00AB81E3:
    result = PopSwitchUpdateUserShutdownScenarioState(3, a2, a3, a4);
    goto loc_00AB81DD;
}
```

## 5. (Beta) C Style

```c
void PoUserShutdownInitiated(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PsIsCurrentThreadInServerSilo(a1, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00AB81E3;
loc_00AB81DD:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00AB81E3:
    result = PopSwitchUpdateUserShutdownScenarioState(3, a2, a3, a4);
    goto loc_00AB81DD;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AB81D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AB81D0[BB_00AB81D0]
  bb_00AB81DD[BB_00AB81DD]
  bb_00AB81E2[BB_00AB81E2]
  bb_00AB81E3[BB_00AB81E3]
  bb_00AB81D0 -->|branch| bb_00AB81E3
  bb_00AB81D0 -->|fallthrough| bb_00AB81DD
  bb_00AB81E2 -->|flow| bb_00AB81E3
  bb_00AB81E3 -->|branch| bb_00AB81DD
```
