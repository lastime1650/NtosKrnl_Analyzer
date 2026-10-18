# HalpDmaAllocateScatterPagesFromScatterPoolAtHighLevel

- RVA: `0x0053F48C`–`0x0053F4B2` (길이 `38` bytes)
- VA: `0x000000014053F48C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0053F493` → [HalpDmaGetAdapterVersion](../3D/HalpDmaGetAdapterVersion_function_003DEC8C.md) (function, `0x003DEC8C`)
- `0x0053F4A0` → [HalpDmaAllocateScatterPagesFromScatterPoolAtHighLevelV3](HalpDmaAllocateScatterPagesFromScatterPoolAtHighLevelV3_function_0053E014.md) (function, `0x0053E014`)
- `0x0053F4A7` → [HalpDmaAllocateScatterPagesFromScatterPoolAtHighLevelV2](../55/HalpDmaAllocateScatterPagesFromScatterPoolAtHighLevelV2_function_00553F38.md) (function, `0x00553F38`)

### Direct callers
- [HalpDmaAllocateMapRegistersAtHighLevel](../55/HalpDmaAllocateMapRegistersAtHighLevel_function_005507A8.md) at `0x00550837`
- [HalpDmaAllocateMapRegistersAtHighLevel](../55/HalpDmaAllocateMapRegistersAtHighLevel_function_005507A8.md) at `0x00550876`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0053F48C  48 83 EC 28                     sub rsp, 0x28
0053F490  4C 8B D2                        mov r10, rdx
0053F493  E8 F4 F7 E9 FF                  call 0x1403dec8c
0053F498  49 8B D2                        mov rdx, r10
0053F49B  83 E8 02                        sub eax, 2
0053F49E  74 07                           je 0x14053f4a7
0053F4A0  E8 6F EB FF FF                  call 0x14053e014
0053F4A5  EB 05                           jmp 0x14053f4ac
0053F4A7  E8 8C 4A 01 00                  call 0x140553f38
0053F4AC  48 83 C4 28                     add rsp, 0x28
0053F4B0  C3                              ret
0053F4B1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpDmaAllocateScatterPagesFromScatterPoolAtHighLevel(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = HalpDmaGetAdapterVersion(a1, a2, a3, a4);
    result = (unsigned int)((result) - (2));
    if (condition_is_equal) goto loc_0053F4A7;
    result = HalpDmaAllocateScatterPagesFromScatterPoolAtHighLevelV3(a1, a2, a3, a4);
    goto loc_0053F4AC;
loc_0053F4A7:
    result = HalpDmaAllocateScatterPagesFromScatterPoolAtHighLevelV2(a1, a2, a3, a4);
loc_0053F4AC:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpDmaAllocateScatterPagesFromScatterPoolAtHighLevel(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = HalpDmaGetAdapterVersion(Arg1, Arg2, a3, a4);
    result = (uint32_t)((result) - (2));
    if (condition_is_equal) goto loc_0053F4A7;
    result = HalpDmaAllocateScatterPagesFromScatterPoolAtHighLevelV3(Arg1, Arg2, a3, a4);
    goto loc_0053F4AC;
loc_0053F4A7:
    result = HalpDmaAllocateScatterPagesFromScatterPoolAtHighLevelV2(Arg1, Arg2, a3, a4);
loc_0053F4AC:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0053F48C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0053F48C[BB_0053F48C]
  bb_0053F4A0[BB_0053F4A0]
  bb_0053F4A7[BB_0053F4A7]
  bb_0053F4AC[BB_0053F4AC]
  bb_0053F4B1[BB_0053F4B1]
  bb_0053F48C -->|branch| bb_0053F4A7
  bb_0053F48C -->|fallthrough| bb_0053F4A0
  bb_0053F4A0 -->|branch| bb_0053F4AC
  bb_0053F4A7 -->|flow| bb_0053F4AC
```
