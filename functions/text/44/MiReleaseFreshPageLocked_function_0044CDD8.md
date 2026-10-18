# MiReleaseFreshPageLocked

- RVA: `0x0044CDD8`–`0x0044CDE9` (길이 `17` bytes)
- VA: `0x000000014044CDD8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `17/17` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0044CDDE` → [MiReturnFreeZeroPage](../33/MiReturnFreeZeroPage_function_00334BD0.md) (function, `0x00334BD0`)

### Direct callers
- [MiTradePage](../28/MiTradePage_function_0028D160.md) at `0x0028DB03`
- [MiRemoveLowestPriorityStandbyPage](../33/MiRemoveLowestPriorityStandbyPage_function_00334600.md) at `0x00334A3D`
- [MiLockLeafPage](../36/MiLockLeafPage_function_003658C0.md) at `0x00365A6D`
- [MiWalkEntireImage](../36/MiWalkEntireImage_function_00365D70.md) at `0x00366FD1`
- [MiLockSpecialPurposeMemoryCachedPage](../40/MiLockSpecialPurposeMemoryCachedPage_function_004049F0.md) at `0x00404A0B`
- [MiHandleSpecialPurposeMemoryCachedFault](MiHandleSpecialPurposeMemoryCachedFault_function_0044C740.md) at `0x0044C886`
- [MiHandleSpecialPurposeMemoryCachedFault](MiHandleSpecialPurposeMemoryCachedFault_function_0044C740.md) at `0x0044C97C`
- [MiHandleSpecialPurposeMemoryCachedFault](MiHandleSpecialPurposeMemoryCachedFault_function_0044C740.md) at `0x0044CA06`
- [MiHandleSpecialPurposeMemoryCachedFault](MiHandleSpecialPurposeMemoryCachedFault_function_0044C740.md) at `0x0044CA3B`
- [MiDemoteSlabEntry](MiDemoteSlabEntry_function_0044CB0C.md) at `0x0044CCC2`
- [MiFreeLargeInitializationCodePages](../67/MiFreeLargeInitializationCodePages_function_00670080.md) at `0x00670124`
- [MiRepointPteAtExtendedStandby](../68/MiRepointPteAtExtendedStandby_function_0068B6F4.md) at `0x0068B7BE`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0044CDD8  48 83 EC 28                     sub rsp, 0x28
0044CDDC  33 D2                           xor edx, edx
0044CDDE  E8 ED 7D EE FF                  call 0x140334bd0
0044CDE3  48 83 C4 28                     add rsp, 0x28
0044CDE7  C3                              ret
0044CDE8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiReleaseFreshPageLocked(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = 0;
    result = MiReturnFreeZeroPage(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiReleaseFreshPageLocked(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = 0;
    result = MiReturnFreeZeroPage(Arg1, Arg2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0044CDD8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0044CDD8[BB_0044CDD8]
  bb_0044CDE8[BB_0044CDE8]
```
