# PipIsDeviceInDeviceObjectList

- RVA: `0x00A070D0`–`0x00A070EB` (길이 `27` bytes)
- VA: `0x0000000140A070D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A070DA` → [PipDeviceObjectListIndexOf](PipDeviceObjectListIndexOf_function_00A070F4.md) (function, `0x00A070F4`)

### Direct callers
- [IopCheckIfMergeRequired](IopCheckIfMergeRequired_function_00A061B4.md) at `0x00A06204`
- [IopCheckIfMergeRequired](IopCheckIfMergeRequired_function_00A061B4.md) at `0x00A0622B`
- [IopCheckIfMergeRequired](IopCheckIfMergeRequired_function_00A061B4.md) at `0x00A06286`
- [IopIsDescendantNode](IopIsDescendantNode_function_00A0665C.md) at `0x00A06683`
- [IopSortRelationListForRemove](IopSortRelationListForRemove_function_00A06C30.md) at `0x00A06CFF`
- [IopSortRelationListForRemove](IopSortRelationListForRemove_function_00A06C30.md) at `0x00A06D8A`
- [PipVisitDeviceObjectListEntry](PipVisitDeviceObjectListEntry_function_00A06F88.md) at `0x00A070AC`
- [sub_00B336B0](../B3/Unknown_function_00B336B0.md) at `0x00B33980`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A070D0  48 83 EC 28                     sub rsp, 0x28
00A070D4  4D 8B C8                        mov r9, r8
00A070D7  44 8B 01                        mov r8d, dword ptr [rcx]
00A070DA  E8 15 00 00 00                  call 0x140a070f4
00A070DF  83 F8 FF                        cmp eax, -1
00A070E2  0F 95 C0                        setne al
00A070E5  48 83 C4 28                     add rsp, 0x28
00A070E9  C3                              ret
00A070EA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PipIsDeviceInDeviceObjectList(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PipDeviceObjectListIndexOf(a1, a2, (unsigned int)(*(unsigned int *)(a1)), a3);
    result = (((unsigned int)(result)) != -1) ? 1 : 0;
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PipIsDeviceInDeviceObjectList(void *Arg1, int64_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PipDeviceObjectListIndexOf(Arg1, Arg2, (uint32_t)(*(uint32_t *)(arg1)), Arg3);
    result = (((uint32_t)(result)) != -1) ? 1 : 0;
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A070D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A070D0[BB_00A070D0]
  bb_00A070EA[BB_00A070EA]
```
