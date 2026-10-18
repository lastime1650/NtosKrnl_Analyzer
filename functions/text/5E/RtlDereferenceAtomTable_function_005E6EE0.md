# RtlDereferenceAtomTable

- RVA: `0x005E6EE0`–`0x005E6EEF` (길이 `15` bytes)
- VA: `0x00000001405E6EE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `5`개 명령, `15/15` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005E6EE4` → [RtlDestroyAtomTable](../../page/9C/RtlDestroyAtomTable_function_009C43F0.md) (function, `0x009C43F0`)

### Direct callers
- [NtAddAtomEx](../../page/AF/NtAddAtomEx_function_00AF7320.md) at `0x00AF7498`
- [NtDeleteAtom](../../page/AF/NtDeleteAtom_function_00AF74E0.md) at `0x00AF7539`
- [NtFindAtom](../../page/AF/NtFindAtom_function_00AF7560.md) at `0x00AF76DF`
- [NtQueryInformationAtom](../../page/AF/NtQueryInformationAtom_function_00AF7720.md) at `0x00AF78C3`
- [sub_00B3D6E4](../../page/B3/Unknown_function_00B3D6E4.md) at `0x00B3D73E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x005E6EE4` → [RtlDestroyAtomTable](../../page/9C/RtlDestroyAtomTable_function_009C43F0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005E6EE0  48 83 EC 28                     sub rsp, 0x28
005E6EE4  E8 07 D5 3D 00                  call 0x1409c43f0
005E6EE9  48 83 C4 28                     add rsp, 0x28
005E6EED  C3                              ret
005E6EEE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlDereferenceAtomTable(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = RtlDestroyAtomTable(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void RtlDereferenceAtomTable(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = RtlDestroyAtomTable(a1, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005E6EE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005E6EE0[BB_005E6EE0]
  bb_005E6EEE[BB_005E6EEE]
```
