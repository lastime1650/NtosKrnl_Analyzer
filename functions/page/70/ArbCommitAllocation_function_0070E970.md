# ArbCommitAllocation

- RVA: `0x0070E970`–`0x0070E99B` (길이 `43` bytes)
- VA: `0x000000014070E970`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `14`개 명령, `43/43` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0070E97D` → [RtlFreeRangeList](../A6/RtlFreeRangeList_function_00A69850.md) (function, `0x00A69850`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0070E970  40 53                           push rbx
0070E972  48 83 EC 20                     sub rsp, 0x20
0070E976  48 8B D9                        mov rbx, rcx
0070E979  48 8B 49 28                     mov rcx, qword ptr [rcx + 0x28]
0070E97D  E8 CE AE 35 00                  call 0x140a69850
0070E982  48 8B 43 30                     mov rax, qword ptr [rbx + 0x30]
0070E986  48 8B 53 28                     mov rdx, qword ptr [rbx + 0x28]
0070E98A  48 89 43 28                     mov qword ptr [rbx + 0x28], rax
0070E98E  33 C0                           xor eax, eax
0070E990  48 89 53 30                     mov qword ptr [rbx + 0x30], rdx
0070E994  48 83 C4 20                     add rsp, 0x20
0070E998  5B                              pop rbx
0070E999  C3                              ret
0070E99A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ArbCommitAllocation(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = RtlFreeRangeList(*(unsigned __int64 *)(a1 + 40), a2, a3, a4);
    *(unsigned __int64 *)(a1 + 40) = *(unsigned __int64 *)(a1 + 48);
    result = 0;
    *(unsigned __int64 *)(a1 + 48) = *(unsigned __int64 *)(a1 + 40);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ArbCommitAllocation(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = RtlFreeRangeList(*(uint64_t *)(arg1 + 0x28), a2, a3, a4);
    *(uint64_t *)(arg1 + 0x28) = *(uint64_t *)(arg1 + 0x30);
    result = 0;
    *(uint64_t *)(arg1 + 0x30) = *(uint64_t *)(arg1 + 0x28);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg1` | `+ 0x30` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0070E970&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0070E970[BB_0070E970]
  bb_0070E99A[BB_0070E99A]
```
