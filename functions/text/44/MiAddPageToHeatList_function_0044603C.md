# MiAddPageToHeatList

- RVA: `0x0044603C`–`0x0044605D` (길이 `33` bytes)
- VA: `0x000000014044603C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `12`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00446045` → [MiAddPageToHeatRanges](MiAddPageToHeatRanges_function_00446064.md) (function, `0x00446064`)
- `0x00446051` → [MiIssuePageHeatList](MiIssuePageHeatList_function_0044615C.md) (function, `0x0044615C`)

### Direct callers
- [MiGetPerfectColorHeadPage](../28/MiGetPerfectColorHeadPage_function_00289CA8.md) at `0x0028A0CA`
- [MiUpdatePfnForPrefetchByPte](../32/MiUpdatePfnForPrefetchByPte_function_00321210.md) at `0x00321604`
- [MiWalkEntireImage](../36/MiWalkEntireImage_function_00365D70.md) at `0x00366AD6`
- [MiCoalesceFreeLargePages](../37/MiCoalesceFreeLargePages_function_0037A7B4.md) at `0x0037AB28`
- [MiAllocateLargeZeroPages](../3B/MiAllocateLargeZeroPages_function_003B743C.md) at `0x003B769C`
- [MiReplenishPageSlist](../3B/MiReplenishPageSlist_function_003BADE0.md) at `0x003BB474`
- [MiChangePageHeatImmediate](MiChangePageHeatImmediate_function_00445F5C.md) at `0x00445FD3`
- [MiSplitDirectMapPage](../4D/MiSplitDirectMapPage_function_004DAAA0.md) at `0x004DAD2D`
- [MiZeroPageMakeHot](../69/MiZeroPageMakeHot_function_00696C08.md) at `0x00696D09`
- [sub_006E169E](../6E/Unknown_function_006E169E.md) at `0x006E16D0`
- [sub_006E7822](../6E/Unknown_function_006E7822.md) at `0x006E785F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0044603C  40 53                           push rbx
0044603E  48 83 EC 20                     sub rsp, 0x20
00446042  48 8B D9                        mov rbx, rcx
00446045  E8 1A 00 00 00                  call 0x140446064
0044604A  85 C0                           test eax, eax
0044604C  74 08                           je 0x140446056
0044604E  48 8B CB                        mov rcx, rbx
00446051  E8 06 01 00 00                  call 0x14044615c
00446056  48 83 C4 20                     add rsp, 0x20
0044605A  5B                              pop rbx
0044605B  C3                              ret
0044605C  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiAddPageToHeatList(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = MiAddPageToHeatRanges(a1, a2, a3, a4);
    if ((unsigned int)(result) != 0) {
        a1 = a1;
        result = MiIssuePageHeatList(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiAddPageToHeatList(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = MiAddPageToHeatRanges(Arg1, a2, a3, a4);
    if ((uint32_t)(result) != 0) {
        Arg1 = Arg1;
        result = MiIssuePageHeatList(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0044603C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0044603C[BB_0044603C]
  bb_0044604E[BB_0044604E]
  bb_00446056[BB_00446056]
  bb_0044605C[BB_0044605C]
  bb_0044603C -->|branch| bb_00446056
  bb_0044603C -->|fallthrough| bb_0044604E
  bb_0044604E -->|flow| bb_00446056
```
