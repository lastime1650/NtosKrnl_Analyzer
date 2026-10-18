# AuthzBasepMemAlloc

- RVA: `0x002FFD90`–`0x002FFDB6` (길이 `38` bytes)
- VA: `0x00000001402FFD90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `12`개 명령, `38/38` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002FFDA4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [AuthzBasepUnicodeStringFromOperandValue](AuthzBasepUnicodeStringFromOperandValue_function_002FE4E8.md) at `0x002FE57C`
- [AuthzBasepEvaluateAceCondition](AuthzBasepEvaluateAceCondition_function_002FEBD0.md) at `0x002FEF22`
- [AuthzBasepAllocateSecurityAttributesList](../30/AuthzBasepAllocateSecurityAttributesList_function_003013F4.md) at `0x00301403`
- [sub_006E041A](../6E/Unknown_function_006E041A.md) at `0x006E046E`
- [AuthzBasepAllocateClaimCollectionNoLists](../../page/A7/AuthzBasepAllocateClaimCollectionNoLists_function_00A7648C.md) at `0x00A7649D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x002FFDA4` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`.text` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002FFD90  48 83 EC 28                     sub rsp, 0x28
002FFD94  48 8B D1                        mov rdx, rcx
002FFD97  B9 00 01 00 00                  mov ecx, 0x100
002FFD9C  44 0F 20 C0                     mov rax, cr8
002FFDA0  3C 02                           cmp al, 2
002FFDA2  73 0B                           jae 0x1402ffdaf
002FFDA4  E8 47 23 88 00                  call 0x140b820f0
002FFDA9  48 83 C4 28                     add rsp, 0x28
002FFDAD  C3                              ret
002FFDAE  CC                              int3
002FFDAF  B9 40 00 00 00                  mov ecx, 0x40
002FFDB4  EB EE                           jmp 0x1402ffda4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AuthzBasepMemAlloc(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (((unsigned __int8)(v_cr8)) >= 2) goto loc_002FFDAF;
loc_002FFDA4:
    result = ExAllocatePool2(256, a1, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
loc_002FFDAF:
    goto loc_002FFDA4;
}
```

## 5. (Beta) C Style

```c
int64_t AuthzBasepMemAlloc(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (((uint8_t)(v_cr8)) >= 2) goto loc_002FFDAF;
loc_002FFDA4:
    result = ExAllocatePool2(256, Arg1, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
loc_002FFDAF:
    goto loc_002FFDA4;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002FFD90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002FFD90[BB_002FFD90]
  bb_002FFDA4[BB_002FFDA4]
  bb_002FFDAE[BB_002FFDAE]
  bb_002FFDAF[BB_002FFDAF]
  bb_002FFD90 -->|branch| bb_002FFDAF
  bb_002FFD90 -->|fallthrough| bb_002FFDA4
  bb_002FFDAE -->|flow| bb_002FFDAF
  bb_002FFDAF -->|branch| bb_002FFDA4
```
