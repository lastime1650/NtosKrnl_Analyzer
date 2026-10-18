# VrpFindExactNamespaceNode

- RVA: `0x00934748`–`0x00934763` (길이 `27` bytes)
- VA: `0x0000000140934748`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `8`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00934758` → [VrpFindNamespaceNode](VrpFindNamespaceNode_function_00934770.md) (function, `0x00934770`)

### Direct callers
- [VrpPostEnumerateKey](VrpPostEnumerateKey_function_00933EA8.md) at `0x00934147`
- [VrpDestroyNamespaceNode](VrpDestroyNamespaceNode_function_00934A50.md) at `0x00934A7B`
- [VrpAddNamespaceNodeToList](VrpAddNamespaceNodeToList_function_00935A94.md) at `0x00935ABF`
- [VrpPreUnloadKey](VrpPreUnloadKey_function_00937950.md) at `0x0093797D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00934748  48 83 EC 38                     sub rsp, 0x38
0093474C  48 83 64 24 20 00               and qword ptr [rsp + 0x20], 0
00934752  4D 8B C8                        mov r9, r8
00934755  45 33 C0                        xor r8d, r8d
00934758  E8 13 00 00 00                  call 0x140934770
0093475D  48 83 C4 38                     add rsp, 0x38
00934761  C3                              ret
00934762  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VrpFindExactNamespaceNode(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    a3 = 0;
    result = VrpFindNamespaceNode(a1, a2, a3, a3);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VrpFindExactNamespaceNode(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    Arg3 = 0;
    result = VrpFindNamespaceNode(Arg1, Arg2, Arg3, Arg3);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00934748&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00934748[BB_00934748]
  bb_00934762[BB_00934762]
```
