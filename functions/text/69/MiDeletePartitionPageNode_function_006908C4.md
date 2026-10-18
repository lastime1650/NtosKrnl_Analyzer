# MiDeletePartitionPageNode

- RVA: `0x006908C4`–`0x006908E9` (길이 `37` bytes)
- VA: `0x00000001406908C4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `13`개 명령, `37/37` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006908D3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x006908DD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- [MiClearRangeInPartitionTree](MiClearRangeInPartitionTree_function_00690734.md) at `0x0069087C`
- [MiDeletePartitionPageNodes](MiDeletePartitionPageNodes_function_006908F0.md) at `0x00690960`
- [MiFinishChildPartitionHotAdd](MiFinishChildPartitionHotAdd_function_00690C00.md) at `0x00690CD0`
- [MiFreePartitionTree](MiFreePartitionTree_function_00690E50.md) at `0x00690EAC`
- [MiInsertPartitionPageNodes](MiInsertPartitionPageNodes_function_00690F94.md) at `0x0069117A`
- [MiPartitionDeleteMemoryNode](MiPartitionDeleteMemoryNode_function_00691A20.md) at `0x00691AC0`
- [MiReturnPartitionPagesToParent](MiReturnPartitionPagesToParent_function_00691B5C.md) at `0x00691CCB`
- [MiHotAddPartitionMemory](../../page/80/MiHotAddPartitionMemory_function_0080D5B4.md) at `0x0080D832`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x006908D3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
  - `0x006908DD` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006908C4  40 53                           push rbx
006908C6  48 83 EC 20                     sub rsp, 0x20
006908CA  48 8B D9                        mov rbx, rcx
006908CD  33 D2                           xor edx, edx
006908CF  48 8B 49 28                     mov rcx, qword ptr [rcx + 0x28]
006908D3  E8 98 1F 4F 00                  call 0x140b82870
006908D8  33 D2                           xor edx, edx
006908DA  48 8B CB                        mov rcx, rbx
006908DD  E8 8E 1F 4F 00                  call 0x140b82870
006908E2  48 83 C4 20                     add rsp, 0x20
006908E6  5B                              pop rbx
006908E7  C3                              ret
006908E8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiDeletePartitionPageNode(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a2 = 0;
    result = ExFreePoolWithTag(*(unsigned __int64 *)(a1 + 40), a2, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiDeletePartitionPageNode(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg2 = 0;
    result = ExFreePoolWithTag(*(uint64_t *)(arg1 + 0x28), Arg2, a3, a4);
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
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006908C4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006908C4[BB_006908C4]
  bb_006908E8[BB_006908E8]
```
