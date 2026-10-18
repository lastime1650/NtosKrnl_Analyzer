# MiWakeFileOnlyReaper

- RVA: `0x004D1D00`–`0x004D1D4C` (길이 `76` bytes)
- VA: `0x00000001404D1D00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `76/76` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **7**

### Outgoing calls
- `0x004D1D3A` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)

### Direct callers
- [MiInsertPageInList](../2B/MiInsertPageInList_function_002BA000.md) at `0x002BA979`
- [MiQueueExtentPfnDeletion](MiQueueExtentPfnDeletion_function_004D1C80.md) at `0x004D1CC3`
- [MiQueueExtentPfnDeletion](MiQueueExtentPfnDeletion_function_004D1C80.md) at `0x004D1CDD`

### Static image references
- `0x004D1D04` → RVA `0x00E2D701` (`.data`; read)
- `0x004D1D0D` → RVA `0x00E2D6C0` (`.data`; read/write)
- `0x004D1D15` → RVA `0x006808B0` (`MiDeleteExtentPfns`; read)
- `0x004D1D21` → RVA `0x00E2D6D0` (`.data`; write)
- `0x004D1D28` → RVA `0x00E2D6C0` (`.data`; read)
- `0x004D1D2F` → RVA `0x00E2D6D8` (`.data`; write)
- `0x004D1D3F` → RVA `0x00E2D701` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004D1D00  48 83 EC 28                     sub rsp, 0x28
004D1D04  80 3D F6 B9 95 00 00            cmp byte ptr [rip + 0x95b9f6], 0
004D1D0B  75 39                           jne 0x1404d1d46
004D1D0D  48 83 25 AB B9 95 00 00         and qword ptr [rip + 0x95b9ab], 0
004D1D15  48 8D 05 94 EB 1A 00            lea rax, [rip + 0x1aeb94]
004D1D1C  BA 01 00 00 00                  mov edx, 1
004D1D21  48 89 05 A8 B9 95 00            mov qword ptr [rip + 0x95b9a8], rax
004D1D28  48 8D 0D 91 B9 95 00            lea rcx, [rip + 0x95b991]
004D1D2F  48 C7 05 9E B9 95 00 01 00 00 00  mov qword ptr [rip + 0x95b99e], 1
004D1D3A  E8 E1 77 E2 FF                  call 0x1402f9520
004D1D3F  C6 05 BB B9 95 00 01            mov byte ptr [rip + 0x95b9bb], 1
004D1D46  48 83 C4 28                     add rsp, 0x28
004D1D4A  C3                              ret
004D1D4B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiWakeFileOnlyReaper(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if ((*(unsigned __int8 *)(v_rip + 9812470)) == 0) {
        result = v_rip + 1764244;
        a2 = 1;
        *(unsigned __int64 *)(v_rip + 9812392) = result;
        a1 = v_rip + 9812369;
        *(unsigned __int64 *)(v_rip + 9812382) = 1;
        result = ExQueueWorkItem(a1, a2, a3, a4);
        *(unsigned __int8 *)(v_rip + 9812411) = 1;
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void MiWakeFileOnlyReaper(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if ((*(uint8_t *)(v_rip + 0x95B9F6)) == 0) {
        result = v_rip + 1764244;
        a2 = 1;
        *(uint64_t *)(v_rip + 0x95B9A8) = result;
        a1 = v_rip + 9812369;
        *(uint64_t *)(v_rip + 0x95B99E) = 1;
        result = ExQueueWorkItem(a1, a2, a3, a4);
        *(uint8_t *)(v_rip + 0x95B9BB) = 1;
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004D1D00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004D1D00[BB_004D1D00]
  bb_004D1D0D[BB_004D1D0D]
  bb_004D1D46[BB_004D1D46]
  bb_004D1D4B[BB_004D1D4B]
  bb_004D1D00 -->|branch| bb_004D1D46
  bb_004D1D00 -->|fallthrough| bb_004D1D0D
  bb_004D1D0D -->|flow| bb_004D1D46
```
