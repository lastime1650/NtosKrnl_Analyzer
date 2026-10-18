# PipDereferenceDependencyNode

- RVA: `0x00ACD5A0`–`0x00ACD5B5` (길이 `21` bytes)
- VA: `0x0000000140ACD5A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `7`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00ACD5AA` → [PipDeleteDependencyNode](../6F/PipDeleteDependencyNode_function_006FE670.md) (function, `0x006FE670`)

### Direct callers
- [IoResolveDependency](../../text/4C/IoResolveDependency_function_004C4380.md) at `0x004C4485`
- [IoResolveDependency](../../text/4C/IoResolveDependency_function_004C4380.md) at `0x004C4494`
- [PipFreeDependencyEdge](../../text/4D/PipFreeDependencyEdge_function_004D7658.md) at `0x004D770E`
- [PipFreeDependencyEdge](../../text/4D/PipFreeDependencyEdge_function_004D7658.md) at `0x004D7717`
- [IoDuplicateDependency](../72/IoDuplicateDependency_function_00727580.md) at `0x00727660`
- [PipMergeDependencyEdgeList](../72/PipMergeDependencyEdgeList_function_00727D4C.md) at `0x00727E66`
- [PipMergeDependencyNodes](../72/PipMergeDependencyNodes_function_00727EB8.md) at `0x00727F03`
- [PipMergeDependencyNodes](../72/PipMergeDependencyNodes_function_00727EB8.md) at `0x00727F0B`
- [PipSetDependency](../72/PipSetDependency_function_00727F24.md) at `0x00727F9D`
- [PipSetDependency](../72/PipSetDependency_function_00727F24.md) at `0x00727FAA`
- [PipProcessRebuildPowerRelationsQueue](../A0/PipProcessRebuildPowerRelationsQueue_function_00A06844.md) at `0x00A068EC`
- [PipProcessRebuildPowerRelationsQueue](../A0/PipProcessRebuildPowerRelationsQueue_function_00A06844.md) at `0x00A0693F`
- [PipDeleteAllDependencyRelations](../A0/PipDeleteAllDependencyRelations_function_00A06950.md) at `0x00A069FB`
- [PipDeleteAllDependencyRelations](../A0/PipDeleteAllDependencyRelations_function_00A06950.md) at `0x00A06A13`
- [PipUnlinkDeviceObjectAndDependencyNode](PipUnlinkDeviceObjectAndDependencyNode_function_00ACD550.md) at `0x00ACD587`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00ACD5A0  48 83 EC 28                     sub rsp, 0x28
00ACD5A4  83 41 58 FF                     add dword ptr [rcx + 0x58], -1
00ACD5A8  75 05                           jne 0x140acd5af
00ACD5AA  E8 C1 10 C3 FF                  call 0x1406fe670
00ACD5AF  48 83 C4 28                     add rsp, 0x28
00ACD5B3  C3                              ret
00ACD5B4  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PipDereferenceDependencyNode(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (!(condition_is_not_equal)) {
        result = PipDeleteDependencyNode(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PipDereferenceDependencyNode(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (!(condition_is_not_equal)) {
        result = PipDeleteDependencyNode(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x58` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00ACD5A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00ACD5A0[BB_00ACD5A0]
  bb_00ACD5AA[BB_00ACD5AA]
  bb_00ACD5AF[BB_00ACD5AF]
  bb_00ACD5B4[BB_00ACD5B4]
  bb_00ACD5A0 -->|branch| bb_00ACD5AF
  bb_00ACD5A0 -->|fallthrough| bb_00ACD5AA
  bb_00ACD5AA -->|flow| bb_00ACD5AF
```
