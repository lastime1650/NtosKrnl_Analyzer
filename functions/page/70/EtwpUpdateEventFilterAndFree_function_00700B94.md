# EtwpUpdateEventFilterAndFree

- RVA: `0x00700B94`–`0x00700BB7` (길이 `35` bytes)
- VA: `0x0000000140700B94`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00700BAC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [EtwpUpdateGuidFilterData](../9F/EtwpUpdateGuidFilterData_function_009FD214.md) at `0x009FD512`
- [EtwpUpdateGuidFilterData](../9F/EtwpUpdateGuidFilterData_function_009FD214.md) at `0x009FD59D`
- [EtwpUpdateGuidFilterData](../9F/EtwpUpdateGuidFilterData_function_009FD214.md) at `0x009FD5B9`
- [EtwpUpdateGuidFilterData](../9F/EtwpUpdateGuidFilterData_function_009FD214.md) at `0x009FD5D5`
- [EtwpUpdateGuidFilterData](../9F/EtwpUpdateGuidFilterData_function_009FD214.md) at `0x009FD5F1`
- [sub_00B326BC](../B3/Unknown_function_00B326BC.md) at `0x00B326D0`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00700BAC` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00700B94  48 83 EC 28                     sub rsp, 0x28
00700B98  48 8B 02                        mov rax, qword ptr [rdx]
00700B9B  48 87 01                        xchg qword ptr [rcx], rax
00700B9E  48 83 22 00                     and qword ptr [rdx], 0
00700BA2  48 85 C0                        test rax, rax
00700BA5  74 0A                           je 0x140700bb1
00700BA7  33 D2                           xor edx, edx
00700BA9  48 8B C8                        mov rcx, rax
00700BAC  E8 BF 1C 48 00                  call 0x140b82870
00700BB1  48 83 C4 28                     add rsp, 0x28
00700BB5  C3                              ret
00700BB6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpUpdateEventFilterAndFree(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = *(unsigned __int64 *)(a2);
    if (*(unsigned __int64 *)(a2) != 0) {
        a2 = 0;
        a1 = *(unsigned __int64 *)(a2);
        result = ExFreePoolWithTag(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t EtwpUpdateEventFilterAndFree(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = *(uint64_t *)(arg2);
    if (*(uint64_t *)(arg2) != 0) {
        Arg2 = 0;
        Arg1 = *(uint64_t *)(arg2);
        result = ExFreePoolWithTag(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00700B94&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00700B94[BB_00700B94]
  bb_00700BA7[BB_00700BA7]
  bb_00700BB1[BB_00700BB1]
  bb_00700BB6[BB_00700BB6]
  bb_00700B94 -->|branch| bb_00700BB1
  bb_00700B94 -->|fallthrough| bb_00700BA7
  bb_00700BA7 -->|flow| bb_00700BB1
```
