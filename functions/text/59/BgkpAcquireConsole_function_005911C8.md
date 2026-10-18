# BgkpAcquireConsole

- RVA: `0x005911C8`–`0x005911E3` (길이 `27` bytes)
- VA: `0x00000001405911C8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005911D3` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)

### Direct callers
- [BgkDisplayStringEx](BgkDisplayStringEx_function_00590C04.md) at `0x00590C28`
- [BgkSetTextColor](BgkSetTextColor_function_00590F00.md) at `0x00590F0D`
- [BgkSolidColorFill](BgkSolidColorFill_function_00591150.md) at `0x00591175`
- [BgkDisplayCharacter](../../pagebgfx/BC/BgkDisplayCharacter_function_00BC0240.md) at `0x00BC025F`
- [BgkGetConsoleState](../../pagebgfx/BC/BgkGetConsoleState_function_00BC0370.md) at `0x00BC0379`
- [BgkGetCursorState](../../pagebgfx/BC/BgkGetCursorState_function_00BC03C0.md) at `0x00BC03D8`
- [BgkSetCursor](../../pagebgfx/BC/BgkSetCursor_function_00BC0490.md) at `0x00BC04A6`

### Static image references
- `0x005911CC` → RVA `0x00E0A9A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005911C8  48 83 EC 28                     sub rsp, 0x28
005911CC  48 8D 0D CD 97 87 00            lea rcx, [rip + 0x8797cd]
005911D3  E8 48 54 C8 FF                  call 0x140216620
005911D8  84 C0                           test al, al
005911DA  0F 95 C0                        setne al
005911DD  48 83 C4 28                     add rsp, 0x28
005911E1  C3                              ret
005911E2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall BgkpAcquireConsole(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExAcquireRundownProtection(v_rip + 8886221, a2, a3, a4);
    result = ((unsigned __int8)(result) != 0) ? 1 : 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void BgkpAcquireConsole(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExAcquireRundownProtection(v_rip + 8886221, a2, a3, a4);
    result = ((uint8_t)(result) != 0) ? 1 : 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005911C8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005911C8[BB_005911C8]
  bb_005911E2[BB_005911E2]
```
