# RtlpCheckFunctionPatchApplied

- RVA: `0x00B75828`–`0x00B7583E` (길이 `22` bytes)
- VA: `0x0000000140B75828`
- 실행 섹션: `PAGELK`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `7`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B75833` → [RtlpCheckFunctionPatchAppliedInOriginalImage](../../text/6A/RtlpCheckFunctionPatchAppliedInOriginalImage_function_006AA408.md) (function, `0x006AA408`)

### Direct callers
- [MiPrepareToHotPatchImage](../../page/80/MiPrepareToHotPatchImage_function_00806820.md) at `0x00806C93`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B75833` → [RtlpCheckFunctionPatchAppliedInOriginalImage](../../text/6A/RtlpCheckFunctionPatchAppliedInOriginalImage_function_006AA408.md) (`PAGELK` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B75828  48 83 EC 48                     sub rsp, 0x48
00B7582C  33 D2                           xor edx, edx
00B7582E  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00B75833  E8 D0 4B B3 FF                  call 0x1406aa408
00B75838  48 83 C4 48                     add rsp, 0x48
00B7583C  C3                              ret
00B7583D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpCheckFunctionPatchApplied(__int64 a1, int a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;

    v_rsp = (v_rsp) - (72);
    a2 = 0;
    v_stack_m28 = a4;
    result = RtlpCheckFunctionPatchAppliedInOriginalImage(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpCheckFunctionPatchApplied(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    Arg2 = 0;
    v_stack_m28 = Arg4;
    result = RtlpCheckFunctionPatchAppliedInOriginalImage(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagelk&rva=0x00B75828&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B75828[BB_00B75828]
  bb_00B7583D[BB_00B7583D]
```
