# sub_006FC686

- RVA: `0x006FC686`–`0x006FC6A7` (길이 `33` bytes)
- VA: `0x00000001406FC686`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BB8EC`
- 디코드: `9`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006FC686` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x006FC691` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x006FC69C` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x006FC686` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`.text` → `PAGE`)
  - `0x006FC691` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`.text` → `PAGE`)
  - `0x006FC69C` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x006FC68C` → [CmpRemoveSecurityCellList + 0x104](../4B/CmpRemoveSecurityCellList_function_004BC1FC.md) (`tail-transfer`)
  - `0x006FC697` → [CmpRemoveSecurityCellList + 0x109](../4B/CmpRemoveSecurityCellList_function_004BC1FC.md) (`tail-transfer`)
  - `0x006FC6A2` → [CmpRemoveSecurityCellList + 0x10E](../4B/CmpRemoveSecurityCellList_function_004BC1FC.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006FC686  E8 B5 98 15 00                  call 0x140855f40
006FC68B  90                              nop
006FC68C  E9 6F FC DB FF                  jmp 0x1404bc300
006FC691  E8 AA 98 15 00                  call 0x140855f40
006FC696  90                              nop
006FC697  E9 69 FC DB FF                  jmp 0x1404bc305
006FC69C  E8 9F 98 15 00                  call 0x140855f40
006FC6A1  90                              nop
006FC6A2  E9 63 FC DB FF                  jmp 0x1404bc30a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006FC686(void)
{
    __int64 result;

    result = HvpReleaseCellPaged(a1, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_006FC686(void)
{
    int64_t result;

    result = HvpReleaseCellPaged(a1, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006FC686&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006FC686[BB_006FC686]
  bb_006FC691[BB_006FC691]
  bb_006FC69C[BB_006FC69C]
```
