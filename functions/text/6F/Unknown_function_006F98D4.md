# sub_006F98D4

- RVA: `0x006F98D4`–`0x006F98F3` (길이 `31` bytes)
- VA: `0x00000001406F98D4`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B6E24`
- 디코드: `9`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x006F98D4` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (function, `0x00855F40`)
- `0x006F98DE` → [CmpRemoveSecurityCellList](../4B/CmpRemoveSecurityCellList_function_004BC1FC.md) (function, `0x004BC1FC`)
- `0x006F98E8` → [HvFreeCell](../../page/85/HvFreeCell_function_0085A72C.md) (function, `0x0085A72C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x006F98D4` → [HvpReleaseCellPaged](../../page/85/HvpReleaseCellPaged_function_00855F40.md) (`.text` → `PAGE`)
  - `0x006F98E8` → [HvFreeCell](../../page/85/HvFreeCell_function_0085A72C.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x006F98EE` → [CmpDereferenceSecurityNode + 0x69](../4A/CmpDereferenceSecurityNode_function_004A672C.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
006F98D4  E8 67 C6 15 00                  call 0x140855f40
006F98D9  8B D7                           mov edx, edi
006F98DB  48 8B CB                        mov rcx, rbx
006F98DE  E8 19 29 DC FF                  call 0x1404bc1fc
006F98E3  8B D7                           mov edx, edi
006F98E5  48 8B CB                        mov rcx, rbx
006F98E8  E8 3F 0E 16 00                  call 0x14085a72c
006F98ED  90                              nop
006F98EE  E9 A2 CE DA FF                  jmp 0x1404a6795
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_006F98D4(void)
{
    __int64 result;

    result = HvpReleaseCellPaged(a1, a2, a3, a4);
    result = CmpRemoveSecurityCellList(v_rbx, (unsigned int)((unsigned int)(v_rdi)), a3, a4);
    result = HvFreeCell(v_rbx, (unsigned int)((unsigned int)(v_rdi)), a3, a4);
}
```

## 5. (Beta) C Style

```c
void sub_006F98D4(void)
{
    int64_t result;

    result = HvpReleaseCellPaged(a1, a2, a3, a4);
    result = CmpRemoveSecurityCellList(local_rbx, (uint32_t)((uint32_t)(local_rdi)), a3, a4);
    result = HvFreeCell(local_rbx, (uint32_t)((uint32_t)(local_rdi)), a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006F98D4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006F98D4[BB_006F98D4]
```
