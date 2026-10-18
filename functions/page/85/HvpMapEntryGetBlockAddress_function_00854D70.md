# HvpMapEntryGetBlockAddress

- RVA: `0x00854D70`–`0x00854D82` (길이 `18` bytes)
- VA: `0x0000000140854D70`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `18/18` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00854D74` → [HvpMapEntryGetBinAddress](../../pagecmrc/BC/HvpMapEntryGetBinAddress_function_00BC9770.md) (function, `0x00BC9770`)

### Direct callers
- [HvpGetCellPaged](HvpGetCellPaged_function_00854CB0.md) at `0x00854D4A`
- [HvpFindNextDirtyBlock](../9B/HvpFindNextDirtyBlock_function_009B5540.md) at `0x009B5613`
- [HvpFindNextDirtyBlock](../9B/HvpFindNextDirtyBlock_function_009B5540.md) at `0x009B5700`
- [HvpCopyModifiedData](../9B/HvpCopyModifiedData_function_009B70A8.md) at `0x009B7119`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00854D74` → [HvpMapEntryGetBinAddress](../../pagecmrc/BC/HvpMapEntryGetBinAddress_function_00BC9770.md) (`PAGE` → `PAGECMRC`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00854D70  48 83 EC 28                     sub rsp, 0x28
00854D74  E8 F7 49 37 00                  call 0x140bc9770
00854D79  48 03 02                        add rax, qword ptr [rdx]
00854D7C  48 83 C4 28                     add rsp, 0x28
00854D80  C3                              ret
00854D81  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HvpMapEntryGetBlockAddress(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = HvpMapEntryGetBinAddress(a1, a2, a3, a4);
    result = (result) + (*(unsigned __int64 *)(a2));
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HvpMapEntryGetBlockAddress(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = HvpMapEntryGetBinAddress(Arg1, Arg2, a3, a4);
    result = (result) + (*(uint64_t *)(Arg2));
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00854D70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00854D70[BB_00854D70]
  bb_00854D81[BB_00854D81]
```
