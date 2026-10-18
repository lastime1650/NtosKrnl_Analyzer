# PopEtAllocate

- RVA: `0x0098C8E0`–`0x0098C8FD` (길이 `29` bytes)
- VA: `0x000000014098C8E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `8`개 명령, `29/29` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0098C8F2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [PopEtAggregateGet](PopEtAggregateGet_function_0098DEEC.md) at `0x0098E063`
- [PopEtProcessSnapshotCreate](PopEtProcessSnapshotCreate_function_0098E4C8.md) at `0x0098E634`
- [PopEtInit](../../init/C4/PopEtInit_function_00C43018.md) at `0x00C432E0`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0098C8F2` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0098C8E0  48 83 EC 28                     sub rsp, 0x28
0098C8E4  48 8B D1                        mov rdx, rcx
0098C8E7  41 B8 50 6F 45 54               mov r8d, 0x54456f50
0098C8ED  B9 00 01 00 00                  mov ecx, 0x100
0098C8F2  E8 F9 57 1F 00                  call 0x140b820f0
0098C8F7  48 83 C4 28                     add rsp, 0x28
0098C8FB  C3                              ret
0098C8FC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopEtAllocate(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExAllocatePool2(256, a1, (unsigned int)(0x54456F50ULL), a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopEtAllocate(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExAllocatePool2(256, Arg1, (uint32_t)(0x54456F50ULL), a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0098C8E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0098C8E0[BB_0098C8E0]
  bb_0098C8FC[BB_0098C8FC]
```
