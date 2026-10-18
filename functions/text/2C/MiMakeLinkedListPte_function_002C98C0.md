# MiMakeLinkedListPte

- RVA: `0x002C98C0`–`0x002C98E3` (길이 `35` bytes)
- VA: `0x00000001402C98C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `13`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_00247C30](../24/Unknown_function_00247C30.md) at `0x00247C6A`
- [MiConvertContiguousPages](../29/MiConvertContiguousPages_function_0029F894.md) at `0x0029F9D0`
- [sub_002B79A7](../2B/Unknown_function_002B79A7.md) at `0x002B79C3`
- [sub_002B79EA](../2B/Unknown_function_002B79EA.md) at `0x002B7A21`
- [MiUpdateCacheAttributeListsForPage](MiUpdateCacheAttributeListsForPage_function_002C97CC.md) at `0x002C9842`
- [MiUpdateCacheAttributeListsForPage](MiUpdateCacheAttributeListsForPage_function_002C97CC.md) at `0x002C9888`
- [MiFreeSlabEntry](../2D/MiFreeSlabEntry_function_002DC650.md) at `0x002DC8BC`
- [MiGetPageChain](../33/MiGetPageChain_function_00330130.md) at `0x0033065E`
- [MiGetPageChain](../33/MiGetPageChain_function_00330130.md) at `0x0033070D`
- [MiSwitchToTransition](../4C/MiSwitchToTransition_function_004C0F5C.md) at `0x004C1141`
- [MiChangeAwePageAttributes](../68/MiChangeAwePageAttributes_function_00687FB4.md) at `0x0068808D`

### Static image references
- `0x002C98C0` → RVA `0x00E2DC80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002C98C0  48 8B 05 B9 43 B6 00            mov rax, qword ptr [rip + 0xb643b9]
002C98C7  48 C1 E1 19                     shl rcx, 0x19
002C98CB  48 85 C0                        test rax, rax
002C98CE  74 09                           je 0x1402c98d9
002C98D0  48 85 C1                        test rcx, rax
002C98D3  74 09                           je 0x1402c98de
002C98D5  48 83 C9 10                     or rcx, 0x10
002C98D9  48 8B C1                        mov rax, rcx
002C98DC  C3                              ret
002C98DD  CC                              int3
002C98DE  48 0B C1                        or rax, rcx
002C98E1  C3                              ret
002C98E2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiMakeLinkedListPte(__int64 a1)
{
    __int64 result;

    a1 = (a1) << (25);
    if (*(unsigned __int64 *)(v_rip + 11944889) == 0) goto loc_002C98D9;
    if (((a1) & (*(unsigned __int64 *)(v_rip + 11944889))) == 0) goto loc_002C98DE;
    a1 = (a1) | (16);
loc_002C98D9:
    return a1;
loc_002C98DE:
    result = (a1) | (a1);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiMakeLinkedListPte(int64_t Arg1)
{
    int64_t result;

    Arg1 = (Arg1) << (25);
    if (*(uint64_t *)(v_rip + 0xB643B9) == 0) goto loc_002C98D9;
    if (((Arg1) & (*(uint64_t *)(v_rip + 0xB643B9))) == 0) goto loc_002C98DE;
    Arg1 = (Arg1) | (16);
loc_002C98D9:
    return Arg1;
loc_002C98DE:
    result = (Arg1) | (Arg1);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002C98C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002C98C0[BB_002C98C0]
  bb_002C98D0[BB_002C98D0]
  bb_002C98D5[BB_002C98D5]
  bb_002C98D9[BB_002C98D9]
  bb_002C98DD[BB_002C98DD]
  bb_002C98DE[BB_002C98DE]
  bb_002C98E2[BB_002C98E2]
  bb_002C98C0 -->|branch| bb_002C98D9
  bb_002C98C0 -->|fallthrough| bb_002C98D0
  bb_002C98D0 -->|branch| bb_002C98DE
  bb_002C98D0 -->|fallthrough| bb_002C98D5
  bb_002C98D5 -->|flow| bb_002C98D9
  bb_002C98DD -->|flow| bb_002C98DE
```
