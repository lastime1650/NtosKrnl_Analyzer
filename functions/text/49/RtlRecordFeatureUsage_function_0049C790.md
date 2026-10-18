# RtlRecordFeatureUsage

- RVA: `0x0049C790`–`0x0049C7AC` (길이 `28` bytes)
- VA: `0x000000014049C790`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082A88`
- 디코드: `10`개 명령, `28/28` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0049C7A5` → [CmFcManagerRecordFeatureUsage](CmFcManagerRecordFeatureUsage_function_0049C7B4.md) (function, `0x0049C7B4`)

### Direct callers
- [wil_details_RecordCachedUsage](../4E/wil_details_RecordCachedUsage_function_004ED6CC.md) at `0x004ED7F7`
- [wil_details_RecordFeatureUsageReporting](../66/wil_details_RecordFeatureUsageReporting_function_0066AAB0.md) at `0x0066AB2C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0049C790  48 83 EC 28                     sub rsp, 0x28
0049C794  48 85 D2                        test rdx, rdx
0049C797  75 06                           jne 0x14049c79f
0049C799  48 83 C4 28                     add rsp, 0x28
0049C79D  C3                              ret
0049C79E  CC                              int3
0049C79F  4C 8B C2                        mov r8, rdx
0049C7A2  48 8B D1                        mov rdx, rcx
0049C7A5  E8 0A 00 00 00                  call 0x14049c7b4
0049C7AA  EB ED                           jmp 0x14049c799
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlRecordFeatureUsage(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a2 != 0) goto loc_0049C79F;
loc_0049C799:
    v_rsp = (v_rsp) + (40);
    return result;
loc_0049C79F:
    result = CmFcManagerRecordFeatureUsage(a1, a1, a2, a4);
    goto loc_0049C799;
}
```

## 5. (Beta) C Style

```c
int64_t RtlRecordFeatureUsage(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg2 != 0) goto loc_0049C79F;
loc_0049C799:
    local_rsp = (local_rsp) + (40);
    return result;
loc_0049C79F:
    result = CmFcManagerRecordFeatureUsage(Arg1, Arg1, Arg2, a4);
    goto loc_0049C799;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0049C790&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0049C790[BB_0049C790]
  bb_0049C799[BB_0049C799]
  bb_0049C79E[BB_0049C79E]
  bb_0049C79F[BB_0049C79F]
  bb_0049C790 -->|branch| bb_0049C79F
  bb_0049C790 -->|fallthrough| bb_0049C799
  bb_0049C79E -->|flow| bb_0049C79F
  bb_0049C79F -->|branch| bb_0049C799
```
