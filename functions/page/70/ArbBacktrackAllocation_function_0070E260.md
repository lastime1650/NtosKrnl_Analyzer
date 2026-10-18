# ArbBacktrackAllocation

- RVA: `0x0070E260`–`0x0070E282` (길이 `34` bytes)
- VA: `0x000000014070E260`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `10`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0070E277` → [RtlDeleteRange](../78/RtlDeleteRange_function_0078A920.md) (function, `0x0078A920`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0070E260  48 83 EC 28                     sub rsp, 0x28
0070E264  4C 8B 4A 20                     mov r9, qword ptr [rdx + 0x20]
0070E268  4C 8B 42 08                     mov r8, qword ptr [rdx + 8]
0070E26C  48 8B 12                        mov rdx, qword ptr [rdx]
0070E26F  48 8B 49 30                     mov rcx, qword ptr [rcx + 0x30]
0070E273  4D 8B 49 20                     mov r9, qword ptr [r9 + 0x20]
0070E277  E8 A4 C6 07 00                  call 0x14078a920
0070E27C  48 83 C4 28                     add rsp, 0x28
0070E280  C3                              ret
0070E281  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ArbBacktrackAllocation(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = RtlDeleteRange(*(unsigned __int64 *)(a1 + 48), *(unsigned __int64 *)(a2), *(unsigned __int64 *)(a2 + 8), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 32) + 32));
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ArbBacktrackAllocation(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = RtlDeleteRange(*(uint64_t *)(arg1 + 0x30), *(uint64_t *)(arg2), *(uint64_t *)(arg2 + 0x8), *(uint64_t *)(*(uint64_t *)(arg2 + 0x20) + 0x20));
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x30` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0070E260&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0070E260[BB_0070E260]
  bb_0070E281[BB_0070E281]
```
