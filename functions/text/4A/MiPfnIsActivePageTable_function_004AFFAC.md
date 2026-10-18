# MiPfnIsActivePageTable

- RVA: `0x004AFFAC`–`0x004AFFD0` (길이 `36` bytes)
- VA: `0x00000001404AFFAC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00069B1C`
- 디코드: `13`개 명령, `36/36` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004AFFB3` → [MiPfnIsPageTable](../4F/MiPfnIsPageTable_function_004F2D90.md) (function, `0x004F2D90`)

### Direct callers
- [MiStealPage](../2B/MiStealPage_function_002B28D0.md) at `0x002B3E8D`
- [MiValidFault](../32/MiValidFault_function_003280B4.md) at `0x00328542`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004AFFAC  48 83 EC 28                     sub rsp, 0x28
004AFFB0  4C 8B C9                        mov r9, rcx
004AFFB3  E8 D8 2D 04 00                  call 0x1404f2d90
004AFFB8  85 C0                           test eax, eax
004AFFBA  74 10                           je 0x1404affcc
004AFFBC  41 8B 41 24                     mov eax, dword ptr [r9 + 0x24]
004AFFC0  C1 E8 1A                        shr eax, 0x1a
004AFFC3  83 E0 01                        and eax, 1
004AFFC6  48 83 C4 28                     add rsp, 0x28
004AFFCA  C3                              ret
004AFFCB  CC                              int3
004AFFCC  33 C0                           xor eax, eax
004AFFCE  EB F6                           jmp 0x1404affc6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiPfnIsActivePageTable(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MiPfnIsPageTable(a1, a2, a3, a1);
    if ((unsigned int)(result) == 0) goto loc_004AFFCC;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 36))) >> (26));
    result = (unsigned int)((result) & (1));
loc_004AFFC6:
    v_rsp = (v_rsp) + (40);
    return result;
loc_004AFFCC:
    result = 0;
    goto loc_004AFFC6;
}
```

## 5. (Beta) C Style

```c
int64_t MiPfnIsActivePageTable(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MiPfnIsPageTable(Arg1, a2, a3, Arg1);
    if ((uint32_t)(result) == 0) goto loc_004AFFCC;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg1 + 0x24))) >> (26));
    result = (uint32_t)((result) & (1));
loc_004AFFC6:
    local_rsp = (local_rsp) + (40);
    return result;
loc_004AFFCC:
    result = 0;
    goto loc_004AFFC6;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004AFFAC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004AFFAC[BB_004AFFAC]
  bb_004AFFBC[BB_004AFFBC]
  bb_004AFFC6[BB_004AFFC6]
  bb_004AFFCB[BB_004AFFCB]
  bb_004AFFCC[BB_004AFFCC]
  bb_004AFFAC -->|branch| bb_004AFFCC
  bb_004AFFAC -->|fallthrough| bb_004AFFBC
  bb_004AFFBC -->|flow| bb_004AFFC6
  bb_004AFFCB -->|flow| bb_004AFFCC
  bb_004AFFCC -->|branch| bb_004AFFC6
```
