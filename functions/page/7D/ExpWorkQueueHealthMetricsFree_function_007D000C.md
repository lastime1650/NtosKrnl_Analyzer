# ExpWorkQueueHealthMetricsFree

- RVA: `0x007D000C`–`0x007D0045` (길이 `57` bytes)
- VA: `0x00000001407D000C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `20`개 명령, `57/57` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007D001F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007D002F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007D0039` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [ExpWorkQueueDestroy](../7C/ExpWorkQueueDestroy_function_007CFE70.md) at `0x007CFEFC`
- [ExpWorkQueueHealthMetricsAllocate](../7C/ExpWorkQueueHealthMetricsAllocate_function_007CFF1C.md) at `0x007CFFDC`
- [ExpPartitionCreatePoolInternal](../AF/ExpPartitionCreatePoolInternal_function_00AF6C08.md) at `0x00AF6D08`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x007D001F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007D002F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x007D0039` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007D000C  40 53                           push rbx
007D000E  48 83 EC 20                     sub rsp, 0x20
007D0012  48 8B D9                        mov rbx, rcx
007D0015  48 8B 09                        mov rcx, qword ptr [rcx]
007D0018  48 85 C9                        test rcx, rcx
007D001B  74 07                           je 0x1407d0024
007D001D  33 D2                           xor edx, edx
007D001F  E8 4C 28 3B 00                  call 0x140b82870
007D0024  48 8B 4B 08                     mov rcx, qword ptr [rbx + 8]
007D0028  48 85 C9                        test rcx, rcx
007D002B  74 07                           je 0x1407d0034
007D002D  33 D2                           xor edx, edx
007D002F  E8 3C 28 3B 00                  call 0x140b82870
007D0034  33 D2                           xor edx, edx
007D0036  48 8B CB                        mov rcx, rbx
007D0039  E8 32 28 3B 00                  call 0x140b82870
007D003E  48 83 C4 20                     add rsp, 0x20
007D0042  5B                              pop rbx
007D0043  C3                              ret
007D0044  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpWorkQueueHealthMetricsFree(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1), a2, a3, a4);
    }
    if (*(unsigned __int64 *)(a1 + 8) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 8), a2, a3, a4);
    }
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpWorkQueueHealthMetricsFree(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1), Arg2, a3, a4);
    }
    if (*(uint64_t *)(arg1 + 0x8) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x8), Arg2, a3, a4);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007D000C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007D000C[BB_007D000C]
  bb_007D001D[BB_007D001D]
  bb_007D0024[BB_007D0024]
  bb_007D002D[BB_007D002D]
  bb_007D0034[BB_007D0034]
  bb_007D0044[BB_007D0044]
  bb_007D000C -->|branch| bb_007D0024
  bb_007D000C -->|fallthrough| bb_007D001D
  bb_007D001D -->|flow| bb_007D0024
  bb_007D0024 -->|branch| bb_007D0034
  bb_007D0024 -->|fallthrough| bb_007D002D
  bb_007D002D -->|flow| bb_007D0034
```
