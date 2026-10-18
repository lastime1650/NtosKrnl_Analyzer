# HalpMmAllocCtxBufferCleanup

- RVA: `0x003E1B34`–`0x003E1B5E` (길이 `42` bytes)
- VA: `0x00000001403E1B34`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `15`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003E1B48` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x003E1B52` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [HalpMmAllocCtxAllocBuffer](HalpMmAllocCtxAllocBuffer_function_003E16B8.md) at `0x003E174A`
- [HalpMmAllocCtxFree](HalpMmAllocCtxFree_function_003E1904.md) at `0x003E1A3E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x003E1B48` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x003E1B52` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003E1B34  40 53                           push rbx
003E1B36  48 83 EC 20                     sub rsp, 0x20
003E1B3A  48 8B 4A 10                     mov rcx, qword ptr [rdx + 0x10]
003E1B3E  48 8B DA                        mov rbx, rdx
003E1B41  48 85 C9                        test rcx, rcx
003E1B44  74 07                           je 0x1403e1b4d
003E1B46  33 D2                           xor edx, edx
003E1B48  E8 23 0D 7A 00                  call 0x140b82870
003E1B4D  33 D2                           xor edx, edx
003E1B4F  48 8B CB                        mov rcx, rbx
003E1B52  E8 19 0D 7A 00                  call 0x140b82870
003E1B57  48 83 C4 20                     add rsp, 0x20
003E1B5B  5B                              pop rbx
003E1B5C  C3                              ret
003E1B5D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpMmAllocCtxBufferCleanup(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (*(unsigned __int64 *)(a2 + 16) != 0) {
        a2 = 0;
        result = ExFreePoolWithTag(*(unsigned __int64 *)(a2 + 16), a2, a3, a4);
    }
    a2 = 0;
    result = ExFreePoolWithTag(0, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpMmAllocCtxBufferCleanup(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (*(uint64_t *)(arg2 + 0x10) != 0) {
        Arg2 = 0;
        result = ExFreePoolWithTag(*(uint64_t *)(arg2 + 0x10), Arg2, a3, a4);
    }
    Arg2 = 0;
    result = ExFreePoolWithTag(0, Arg2, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E1B34&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003E1B34[BB_003E1B34]
  bb_003E1B46[BB_003E1B46]
  bb_003E1B4D[BB_003E1B4D]
  bb_003E1B5D[BB_003E1B5D]
  bb_003E1B34 -->|branch| bb_003E1B4D
  bb_003E1B34 -->|fallthrough| bb_003E1B46
  bb_003E1B46 -->|flow| bb_003E1B4D
```
