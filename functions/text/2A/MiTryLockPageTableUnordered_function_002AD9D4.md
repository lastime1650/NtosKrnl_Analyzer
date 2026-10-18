# MiTryLockPageTableUnordered

- RVA: `0x002AD9D4`–`0x002AD9E9` (길이 `21` bytes)
- VA: `0x00000001402AD9D4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `21/21` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002AD9DE` → [MiLockPageTableInternal](MiLockPageTableInternal_function_002AD9F0.md) (function, `0x002AD9F0`)

### Direct callers
- [MiSwapStackPage](../29/MiSwapStackPage_function_0029FDE0.md) at `0x002A0048`
- [MiLockActivePageTableInList](MiLockActivePageTableInList_function_002AD86C.md) at `0x002AD8C7`
- [sub_006F60F8](../6F/Unknown_function_006F60F8.md) at `0x006F6233`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002AD9D4  48 83 EC 28                     sub rsp, 0x28
002AD9D8  41 B8 01 00 00 00               mov r8d, 1
002AD9DE  E8 0D 00 00 00                  call 0x1402ad9f0
002AD9E3  48 83 C4 28                     add rsp, 0x28
002AD9E7  C3                              ret
002AD9E8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiTryLockPageTableUnordered(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MiLockPageTableInternal(a1, a2, 1, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void MiTryLockPageTableUnordered(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MiLockPageTableInternal(a1, a2, 1, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002AD9D4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002AD9D4[BB_002AD9D4]
  bb_002AD9E8[BB_002AD9E8]
```
