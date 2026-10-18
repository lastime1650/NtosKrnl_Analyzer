# MiImageVadHotPatchEligible

- RVA: `0x00803FB8`–`0x00803FD0` (길이 `24` bytes)
- VA: `0x0000000140803FB8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `24/24` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00803FBC` → [MiImageVadHotPatchEligibleEx](../../text/68/MiImageVadHotPatchEligibleEx_function_006836BC.md) (function, `0x006836BC`)

### Direct callers
- [MiGetVadForHotPatchInProgress](MiGetVadForHotPatchInProgress_function_008039C4.md) at `0x00803A25`
- [MmCommitHotPatchTable](MmCommitHotPatchTable_function_00807278.md) at `0x008072BA`
- [MmPrepareImagePagesForHotPatch](MmPrepareImagePagesForHotPatch_function_008074E8.md) at `0x0080755A`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00803FBC` → [MiImageVadHotPatchEligibleEx](../../text/68/MiImageVadHotPatchEligibleEx_function_006836BC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00803FB8  48 83 EC 28                     sub rsp, 0x28
00803FBC  E8 FB F6 E7 FF                  call 0x1406836bc
00803FC1  33 C9                           xor ecx, ecx
00803FC3  85 C0                           test eax, eax
00803FC5  0F 94 C1                        sete cl
00803FC8  8B C1                           mov eax, ecx
00803FCA  48 83 C4 28                     add rsp, 0x28
00803FCE  C3                              ret
00803FCF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiImageVadHotPatchEligible(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = MiImageVadHotPatchEligibleEx(a1, a2, a3, a4);
    a1 = 0;
    a1 = ((unsigned int)(result) == 0) ? 1 : 0;
    v_rsp = (v_rsp) + (40);
    return (unsigned int)(a1);
}
```

## 5. (Beta) C Style

```c
int64_t MiImageVadHotPatchEligible(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = MiImageVadHotPatchEligibleEx(Arg1, a2, a3, a4);
    Arg1 = 0;
    Arg1 = ((uint32_t)(result) == 0) ? 1 : 0;
    local_rsp = (local_rsp) + (40);
    return (uint32_t)(Arg1);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00803FB8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00803FB8[BB_00803FB8]
  bb_00803FCF[BB_00803FCF]
```
