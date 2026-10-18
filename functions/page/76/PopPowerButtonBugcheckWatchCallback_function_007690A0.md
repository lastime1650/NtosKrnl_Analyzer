# PopPowerButtonBugcheckWatchCallback

- RVA: `0x007690A0`–`0x007690BB` (길이 `27` bytes)
- VA: `0x00000001407690A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007690B0` → [PopPowerButtonBugcheckConfigure](PopPowerButtonBugcheckConfigure_function_00768F84.md) (function, `0x00768F84`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007690A0  48 83 EC 28                     sub rsp, 0x28
007690A4  4C 8D 44 24 30                  lea r8, [rsp + 0x30]
007690A9  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
007690AE  B2 01                           mov dl, 1
007690B0  E8 CF FE FF FF                  call 0x140768f84
007690B5  48 83 C4 28                     add rsp, 0x28
007690B9  C3                              ret
007690BA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPowerButtonBugcheckWatchCallback(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = 0;
    result = PopPowerButtonBugcheckConfigure(a1, 1, v_stack_p8, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PopPowerButtonBugcheckWatchCallback(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = 0;
    result = PopPowerButtonBugcheckConfigure(a1, 1, v_stack_p8, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007690A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007690A0[BB_007690A0]
  bb_007690BA[BB_007690BA]
```
