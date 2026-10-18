# HalpKsrCallbackRoutine

- RVA: `0x0070C5E0`–`0x0070C612` (길이 `50` bytes)
- VA: `0x000000014070C5E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `18`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0070C607` → [HalpSetShutdownResetHandler](../../text/54/HalpSetShutdownResetHandler_function_00546948.md) (function, `0x00546948`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0070C600` → RVA `0x00546BA0` (`HalpShutdownReset`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0070C607` → [HalpSetShutdownResetHandler](../../text/54/HalpSetShutdownResetHandler_function_00546948.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0070C5E0  48 83 EC 28                     sub rsp, 0x28
0070C5E4  85 D2                           test edx, edx
0070C5E6  74 18                           je 0x14070c600
0070C5E8  83 EA 01                        sub edx, 1
0070C5EB  74 0F                           je 0x14070c5fc
0070C5ED  83 EA 01                        sub edx, 1
0070C5F0  74 1A                           je 0x14070c60c
0070C5F2  83 EA 01                        sub edx, 1
0070C5F5  74 09                           je 0x14070c600
0070C5F7  83 FA 01                        cmp edx, 1
0070C5FA  75 10                           jne 0x14070c60c
0070C5FC  33 C9                           xor ecx, ecx
0070C5FE  EB 07                           jmp 0x14070c607
0070C600  48 8D 0D 99 A5 E3 FF            lea rcx, [rip - 0x1c5a67]
0070C607  E8 3C A3 E3 FF                  call 0x140546948
0070C60C  48 83 C4 28                     add rsp, 0x28
0070C610  C3                              ret
0070C611  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpKsrCallbackRoutine(int a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a2 == 0) goto loc_0070C600;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_0070C5FC;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_0070C60C;
    a2 = (unsigned int)((a2) - (1));
    if (condition_is_equal) goto loc_0070C600;
    if (a2 != 1) goto loc_0070C60C;
loc_0070C5FC:
    a1 = 0;
    goto loc_0070C607;
loc_0070C600:
loc_0070C607:
    result = HalpSetShutdownResetHandler(v_rip - 1858151, a2, a3, a4);
loc_0070C60C:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t HalpKsrCallbackRoutine(int32_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg2 == 0) goto loc_0070C600;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_0070C5FC;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_0070C60C;
    Arg2 = (uint32_t)((Arg2) - (1));
    if (condition_is_equal) goto loc_0070C600;
    if (Arg2 != 1) goto loc_0070C60C;
loc_0070C5FC:
    Arg1 = 0;
    goto loc_0070C607;
loc_0070C600:
loc_0070C607:
    result = HalpSetShutdownResetHandler(v_rip - 1858151, Arg2, a3, a4);
loc_0070C60C:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0070C5E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0070C5E0[BB_0070C5E0]
  bb_0070C5E8[BB_0070C5E8]
  bb_0070C5ED[BB_0070C5ED]
  bb_0070C5F2[BB_0070C5F2]
  bb_0070C5F7[BB_0070C5F7]
  bb_0070C5FC[BB_0070C5FC]
  bb_0070C600[BB_0070C600]
  bb_0070C607[BB_0070C607]
  bb_0070C60C[BB_0070C60C]
  bb_0070C611[BB_0070C611]
  bb_0070C5E0 -->|branch| bb_0070C600
  bb_0070C5E0 -->|fallthrough| bb_0070C5E8
  bb_0070C5E8 -->|branch| bb_0070C5FC
  bb_0070C5E8 -->|fallthrough| bb_0070C5ED
  bb_0070C5ED -->|branch| bb_0070C60C
  bb_0070C5ED -->|fallthrough| bb_0070C5F2
  bb_0070C5F2 -->|branch| bb_0070C600
  bb_0070C5F2 -->|fallthrough| bb_0070C5F7
  bb_0070C5F7 -->|branch| bb_0070C60C
  bb_0070C5F7 -->|fallthrough| bb_0070C5FC
  bb_0070C5FC -->|branch| bb_0070C607
  bb_0070C600 -->|flow| bb_0070C607
  bb_0070C607 -->|flow| bb_0070C60C
```
