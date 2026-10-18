# HalpInterruptIsGsiValid

- RVA: `0x007072F0`–`0x00707309` (길이 `25` bytes)
- VA: `0x00000001407072F0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `25/25` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007072F9` → [HalpInterruptGsiToLine](../../text/2D/HalpInterruptGsiToLine_function_002D2DD0.md) (function, `0x002D2DD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007072F9` → [HalpInterruptGsiToLine](../../text/2D/HalpInterruptGsiToLine_function_002D2DD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007072F0  48 83 EC 28                     sub rsp, 0x28
007072F4  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
007072F9  E8 D2 BA BC FF                  call 0x1402d2dd0
007072FE  85 C0                           test eax, eax
00707300  0F 99 C0                        setns al
00707303  48 83 C4 28                     add rsp, 0x28
00707307  C3                              ret
00707308  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpInterruptIsGsiValid(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_rsp = (v_rsp) - (40);
    result = HalpInterruptGsiToLine(a1, v_stack_p10, a3, a4);
    result = (!sign_flag) ? 1 : 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void HalpInterruptIsGsiValid(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    local_rsp = (local_rsp) - (40);
    result = HalpInterruptGsiToLine(a1, v_stack_p10, a3, a4);
    result = (!sign_flag) ? 1 : 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007072F0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007072F0[BB_007072F0]
  bb_00707308[BB_00707308]
```
