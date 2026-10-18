# MiGetLargestPageIndex

- RVA: `0x0049F730`–`0x0049F742` (길이 `18` bytes)
- VA: `0x000000014049F730`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `6`개 명령, `18/18` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiAddPhysicalMemoryChunks](../../page/7F/MiAddPhysicalMemoryChunks_function_007F98D4.md) at `0x007F9D19`
- [MmManagePartitionCreateLargePages](../../page/80/MmManagePartitionCreateLargePages_function_0080E000.md) at `0x0080E070`
- [MmBuildLargePages](../../page/9F/MmBuildLargePages_function_009FFB08.md) at `0x009FFB2F`
- [MiFindLargePageMemory](../../page/AA/MiFindLargePageMemory_function_00AA8334.md) at `0x00AA841B`
- [MiQueryMemoryPhysicalContiguity](../../page/AD/MiQueryMemoryPhysicalContiguity_function_00AD5B98.md) at `0x00AD5CDE`
- [sub_00B31388](../../page/B3/Unknown_function_00B31388.md) at `0x00B31421`

### Static image references
- `0x0049F730` → RVA `0x00FC6B30` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0049F730  48 8B 05 F9 73 B2 00            mov rax, qword ptr [rip + 0xb273f9]
0049F737  48 C1 E8 25                     shr rax, 0x25
0049F73B  F7 D0                           not eax
0049F73D  83 E0 01                        and eax, 1
0049F740  C3                              ret
0049F741  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiGetLargestPageIndex(void)
{
    __int64 result;

    result = (*(unsigned __int64 *)(v_rip + 11695097)) >> (37);
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & (1));
    return result;
}
```

## 5. (Beta) C Style

```c
void MiGetLargestPageIndex(void)
{
    int64_t result;

    result = (*(uint64_t *)(v_rip + 0xB273F9)) >> (37);
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & (1));
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0049F730&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0049F730[BB_0049F730]
  bb_0049F741[BB_0049F741]
```
