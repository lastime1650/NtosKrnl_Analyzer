# PoFxIssueComponentPerfStateChange

- RVA: `0x005D1A30`–`0x005D1A54` (길이 `36` bytes)
- VA: `0x00000001405D1A30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `9`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005D1A49` → [PoFxIssueComponentPerfStateChangeMultiple](PoFxIssueComponentPerfStateChangeMultiple_function_005D1A60.md) (function, `0x005D1A60`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D1A30  48 83 EC 38                     sub rsp, 0x38
005D1A34  48 8B 44 24 60                  mov rax, qword ptr [rsp + 0x60]
005D1A39  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
005D1A3E  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
005D1A43  41 B9 01 00 00 00               mov r9d, 1
005D1A49  E8 12 00 00 00                  call 0x1405d1a60
005D1A4E  48 83 C4 38                     add rsp, 0x38
005D1A52  C3                              ret
005D1A53  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PoFxIssueComponentPerfStateChange(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    v_stack_m10 = a5;
    v_stack_m18 = a4;
    result = PoFxIssueComponentPerfStateChangeMultiple(a1, a2, a3, 1);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PoFxIssueComponentPerfStateChange(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    v_stack_m10 = Arg5;
    v_stack_m18 = Arg4;
    result = PoFxIssueComponentPerfStateChangeMultiple(Arg1, Arg2, Arg3, 1);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D1A30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D1A30[BB_005D1A30]
  bb_005D1A53[BB_005D1A53]
```
