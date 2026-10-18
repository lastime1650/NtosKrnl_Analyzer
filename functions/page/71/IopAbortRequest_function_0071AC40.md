# IopAbortRequest

- RVA: `0x0071AC40`–`0x0071AC64` (길이 `36` bytes)
- VA: `0x000000014071AC40`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `10`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0071AC59` → [IopCompleteRequest](../../text/20/IopCompleteRequest_function_0020AF50.md) (function, `0x0020AF50`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0071AC59` → [IopCompleteRequest](../../text/20/IopCompleteRequest_function_0020AF50.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0071AC40  48 83 EC 38                     sub rsp, 0x38
0071AC44  48 8D 41 48                     lea rax, [rcx + 0x48]
0071AC48  4C 8D 49 40                     lea r9, [rcx + 0x40]
0071AC4C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0071AC51  4C 8D 41 38                     lea r8, [rcx + 0x38]
0071AC55  48 8D 51 30                     lea rdx, [rcx + 0x30]
0071AC59  E8 F2 02 AF FF                  call 0x14020af50
0071AC5E  48 83 C4 38                     add rsp, 0x38
0071AC62  C3                              ret
0071AC63  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopAbortRequest(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    v_stack_m18 = a1 + 72;
    result = IopCompleteRequest(a1, a1 + 48, a1 + 56, a1 + 64);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t IopAbortRequest(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    v_stack_m18 = Arg1 + 72;
    result = IopCompleteRequest(Arg1, Arg1 + 48, Arg1 + 56, Arg1 + 64);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |
| `Arg1` | `+ 0x48` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0071AC40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0071AC40[BB_0071AC40]
  bb_0071AC63[BB_0071AC63]
```
