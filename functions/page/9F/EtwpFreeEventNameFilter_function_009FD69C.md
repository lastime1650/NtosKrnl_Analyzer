# EtwpFreeEventNameFilter

- RVA: `0x009FD69C`–`0x009FD6C6` (길이 `42` bytes)
- VA: `0x00000001409FD69C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `15`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x009FD6B0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x009FD6BA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [EtwpFreeFilterInfo](../8C/EtwpFreeFilterInfo_function_008C8A24.md) at `0x008C8B03`
- [EtwpAllocateEventNameFilter](EtwpAllocateEventNameFilter_function_009FCBA4.md) at `0x009FCE88`
- [EtwpUpdateGuidFilterData](EtwpUpdateGuidFilterData_function_009FD214.md) at `0x009FD54A`
- [EtwpUpdateGuidFilterData](EtwpUpdateGuidFilterData_function_009FD214.md) at `0x009FD67A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x009FD6B0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x009FD6BA` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009FD69C  40 53                           push rbx
009FD69E  48 83 EC 20                     sub rsp, 0x20
009FD6A2  48 8B D9                        mov rbx, rcx
009FD6A5  48 8B 49 20                     mov rcx, qword ptr [rcx + 0x20]
009FD6A9  48 85 C9                        test rcx, rcx
009FD6AC  74 07                           je 0x1409fd6b5
009FD6AE  33 D2                           xor edx, edx
009FD6B0  E8 BB 51 18 00                  call 0x140b82870
009FD6B5  33 D2                           xor edx, edx
009FD6B7  48 8B CB                        mov rcx, rbx
009FD6BA  E8 B1 51 18 00                  call 0x140b82870
009FD6BF  48 83 C4 20                     add rsp, 0x20
009FD6C3  5B                              pop rbx
009FD6C4  C3                              ret
009FD6C5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpFreeEventNameFilter(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a1 + 32) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 32), a2, a3, a4);
    }
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpFreeEventNameFilter(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg1 + 0x20) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x20), Arg2, a3, a4);
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
| `Arg1` | `+ 0x20` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009FD69C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_009FD69C[BB_009FD69C]
  bb_009FD6AE[BB_009FD6AE]
  bb_009FD6B5[BB_009FD6B5]
  bb_009FD6C5[BB_009FD6C5]
  bb_009FD69C -->|branch| bb_009FD6B5
  bb_009FD69C -->|fallthrough| bb_009FD6AE
  bb_009FD6AE -->|flow| bb_009FD6B5
```
