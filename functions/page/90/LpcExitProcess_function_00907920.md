# LpcExitProcess

- RVA: `0x00907920`–`0x0090795B` (길이 `59` bytes)
- VA: `0x0000000140907920`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `15`개 명령, `59/59` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0090793C` → [PsReturnProcessPagedPoolQuota](../../text/2A/PsReturnProcessPagedPoolQuota_function_002A6860.md) (function, `0x002A6860`)
- `0x0090794F` → [AlpcpCleanupProcessViews](AlpcpCleanupProcessViews_function_00907964.md) (function, `0x00907964`)

### Direct callers
- [PspExitLastThread](PspExitLastThread_function_00904184.md) at `0x0090426D`
- [PspProcessDelete](PspProcessDelete_function_00907B90.md) at `0x00907E48`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0090793C` → [PsReturnProcessPagedPoolQuota](../../text/2A/PsReturnProcessPagedPoolQuota_function_002A6860.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00907920  40 53                           push rbx
00907922  48 83 EC 20                     sub rsp, 0x20
00907926  48 8B 81 98 05 00 00            mov rax, qword ptr [rcx + 0x598]
0090792D  48 8B D9                        mov rbx, rcx
00907930  48 85 C0                        test rax, rax
00907933  74 17                           je 0x14090794c
00907935  48 8B 91 98 05 00 00            mov rdx, qword ptr [rcx + 0x598]
0090793C  E8 1F EF 99 FF                  call 0x1402a6860
00907941  48 C7 83 98 05 00 00 00 00 00 00  mov qword ptr [rbx + 0x598], 0
0090794C  48 8B CB                        mov rcx, rbx
0090794F  E8 10 00 00 00                  call 0x140907964
00907954  48 83 C4 20                     add rsp, 0x20
00907958  5B                              pop rbx
00907959  C3                              ret
0090795A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LpcExitProcess(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = *(unsigned __int64 *)(a1 + 1432);
    if (*(unsigned __int64 *)(a1 + 1432) != 0) {
        a2 = *(unsigned __int64 *)(a1 + 1432);
        result = PsReturnProcessPagedPoolQuota(a1, a2, a3, a4);
        *(unsigned __int64 *)(a1 + 1432) = 0;
    }
    result = AlpcpCleanupProcessViews(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t LpcExitProcess(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = *(uint64_t *)(arg1 + 0x598);
    if (*(uint64_t *)(arg1 + 0x598) != 0) {
        a2 = *(uint64_t *)(arg1 + 0x598);
        result = PsReturnProcessPagedPoolQuota(Arg1, a2, a3, a4);
        *(uint64_t *)(arg1 + 0x598) = 0;
    }
    result = AlpcpCleanupProcessViews(Arg1, a2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x598` | `64` | `R` |
| `Arg1` | `+ 0x598` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00907920&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00907920[BB_00907920]
  bb_00907935[BB_00907935]
  bb_0090794C[BB_0090794C]
  bb_0090795A[BB_0090795A]
  bb_00907920 -->|branch| bb_0090794C
  bb_00907920 -->|fallthrough| bb_00907935
  bb_00907935 -->|flow| bb_0090794C
```
