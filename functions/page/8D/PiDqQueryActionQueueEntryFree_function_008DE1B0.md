# PiDqQueryActionQueueEntryFree

- RVA: `0x008DE1B0`–`0x008DE1E9` (길이 `57` bytes)
- VA: `0x00000001408DE1B0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `18`개 명령, `57/57` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008DE1C2` → [PiDmObjectRelease](../8E/PiDmObjectRelease_function_008E4F70.md) (function, `0x008E4F70`)
- `0x008DE1D0` → [PiPnpRtlObjectEventRelease](../8E/PiPnpRtlObjectEventRelease_function_008E6E24.md) (function, `0x008E6E24`)
- `0x008DE1DD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [PiDqQuerySerializeActionQueue](PiDqQuerySerializeActionQueue_function_008DD340.md) at `0x008DD55E`
- [PiDqQueryFreeActiveData](PiDqQueryFreeActiveData_function_008DE4FC.md) at `0x008DE55A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008DE1DD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008DE1B0  40 53                           push rbx
008DE1B2  48 83 EC 20                     sub rsp, 0x20
008DE1B6  48 8B D9                        mov rbx, rcx
008DE1B9  48 8B 49 10                     mov rcx, qword ptr [rcx + 0x10]
008DE1BD  48 85 C9                        test rcx, rcx
008DE1C0  74 05                           je 0x1408de1c7
008DE1C2  E8 A9 6D 00 00                  call 0x1408e4f70
008DE1C7  48 8B 4B 18                     mov rcx, qword ptr [rbx + 0x18]
008DE1CB  48 85 C9                        test rcx, rcx
008DE1CE  74 05                           je 0x1408de1d5
008DE1D0  E8 4F 8C 00 00                  call 0x1408e6e24
008DE1D5  BA 50 6E 70 58                  mov edx, 0x58706e50
008DE1DA  48 8B CB                        mov rcx, rbx
008DE1DD  E8 8E 46 2A 00                  call 0x140b82870
008DE1E2  48 83 C4 20                     add rsp, 0x20
008DE1E6  5B                              pop rbx
008DE1E7  C3                              ret
008DE1E8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDqQueryActionQueueEntryFree(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 16) != 0) {
        result = PiDmObjectRelease(*(unsigned __int64 *)(a1 + 16), a2, a3, a4);
    }
    if (*(unsigned __int64 *)(a1 + 24) != 0) {
        result = PiPnpRtlObjectEventRelease(*(unsigned __int64 *)(a1 + 24), a2, a3, a4);
    }
    result = ExFreePoolWithTag(a1, (unsigned int)(0x58706E50ULL), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PiDqQueryActionQueueEntryFree(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0x10) != 0) {
        result = PiDmObjectRelease(*(uint64_t *)(arg1 + 0x10), a2, a3, a4);
    }
    if (*(uint64_t *)(arg1 + 0x18) != 0) {
        result = PiPnpRtlObjectEventRelease(*(uint64_t *)(arg1 + 0x18), a2, a3, a4);
    }
    result = ExFreePoolWithTag(Arg1, (uint32_t)(0x58706E50ULL), a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008DE1B0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008DE1B0[BB_008DE1B0]
  bb_008DE1C2[BB_008DE1C2]
  bb_008DE1C7[BB_008DE1C7]
  bb_008DE1D0[BB_008DE1D0]
  bb_008DE1D5[BB_008DE1D5]
  bb_008DE1E8[BB_008DE1E8]
  bb_008DE1B0 -->|branch| bb_008DE1C7
  bb_008DE1B0 -->|fallthrough| bb_008DE1C2
  bb_008DE1C2 -->|flow| bb_008DE1C7
  bb_008DE1C7 -->|branch| bb_008DE1D5
  bb_008DE1C7 -->|fallthrough| bb_008DE1D0
  bb_008DE1D0 -->|flow| bb_008DE1D5
```
