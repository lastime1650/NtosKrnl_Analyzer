# PnpObjectRaiseCreateEvent

- RVA: `0x008FF9CC`–`0x008FFA05` (길이 `57` bytes)
- VA: `0x00000001408FF9CC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C2A4`
- 디코드: `14`개 명령, `57/57` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008FF9FA` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [PnpCreateObjectDispatch](../82/PnpCreateObjectDispatch_function_0082C3EC.md) at `0x0082C4C7`
- [CmRaiseCreateEvent](CmRaiseCreateEvent_function_008FF944.md) at `0x008FF977`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008FF9FA` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008FF9CC  48 83 EC 58                     sub rsp, 0x58
008FF9D0  48 8B 81 F0 01 00 00            mov rax, qword ptr [rcx + 0x1f0]
008FF9D7  0F 57 C0                        xorps xmm0, xmm0
008FF9DA  F3 0F 7F 44 24 38               movdqu xmmword ptr [rsp + 0x38], xmm0
008FF9E0  48 85 C0                        test rax, rax
008FF9E3  74 1A                           je 0x1408ff9ff
008FF9E5  4C 89 4C 24 30                  mov qword ptr [rsp + 0x30], r9
008FF9EA  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
008FF9EF  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
008FF9F4  41 B9 02 00 00 00               mov r9d, 2
008FF9FA  E8 D1 B0 DB FF                  call 0x1406baad0
008FF9FF  48 83 C4 58                     add rsp, 0x58
008FFA03  C3                              ret
008FFA04  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpObjectRaiseCreateEvent(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;

    v_rsp = (v_rsp) - (88);
    v_stack_m20 = v_xmm0;
    result = *(unsigned __int64 *)(a1 + 496);
    if (*(unsigned __int64 *)(a1 + 496) != 0) {
        v_stack_m28 = a4;
        a4 = v_stack_m28;
        v_stack_m38 = a4;
        a4 = 2;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (88);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PnpObjectRaiseCreateEvent(void *Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    v_stack_m20 = v_xmm0;
    result = *(uint64_t *)(arg1 + 0x1F0);
    if (*(uint64_t *)(arg1 + 0x1F0) != 0) {
        v_stack_m28 = Arg4;
        Arg4 = v_stack_m28;
        v_stack_m38 = Arg4;
        Arg4 = 2;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
    local_rsp = (local_rsp) + (88);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1F0` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008FF9CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008FF9CC[BB_008FF9CC]
  bb_008FF9E5[BB_008FF9E5]
  bb_008FF9FF[BB_008FF9FF]
  bb_008FFA04[BB_008FFA04]
  bb_008FF9CC -->|branch| bb_008FF9FF
  bb_008FF9CC -->|fallthrough| bb_008FF9E5
  bb_008FF9E5 -->|flow| bb_008FF9FF
```
