# WdipSemSqmEnabled

- RVA: `0x0070276C`–`0x007027AD` (길이 `65` bytes)
- VA: `0x000000014070276C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `19`개 명령, `65/65` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00702780` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)
- `0x00702799` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (function, `0x00392450`)

### Direct callers
- [WdipSemLogInflightLimitExceededInformation](../7B/WdipSemLogInflightLimitExceededInformation_function_007B0B38.md) at `0x007B0BA2`
- [WdipSemLogInflightLimitExceededInformation](../7B/WdipSemLogInflightLimitExceededInformation_function_007B0B38.md) at `0x007B0C23`
- [WdipSemLogTimeoutInformation](../A5/WdipSemLogTimeoutInformation_function_00A5C02C.md) at `0x00A5C06B`

### Static image references
- `0x00702772` → RVA `0x00F01DD0` (`.data`; read)
- `0x00702779` → RVA `0x0001ED98` (`.rdata`; read)
- `0x00702792` → RVA `0x00022128` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00702780` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
  - `0x00702799` → [EtwEventEnabled](../../text/39/EtwEventEnabled_function_00392450.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0070276C  40 53                           push rbx
0070276E  48 83 EC 20                     sub rsp, 0x20
00702772  48 8B 0D 57 F6 7F 00            mov rcx, qword ptr [rip + 0x7ff657]
00702779  48 8D 15 18 C6 91 FF            lea rdx, [rip - 0x6e39e8]
00702780  E8 CB FC C8 FF                  call 0x140392450
00702785  32 DB                           xor bl, bl
00702787  84 C0                           test al, al
00702789  74 19                           je 0x1407027a4
0070278B  48 8B 0D 3E F6 7F 00            mov rcx, qword ptr [rip + 0x7ff63e]
00702792  48 8D 15 8F F9 91 FF            lea rdx, [rip - 0x6e0671]
00702799  E8 B2 FC C8 FF                  call 0x140392450
0070279E  84 C0                           test al, al
007027A0  74 02                           je 0x1407027a4
007027A2  B3 01                           mov bl, 1
007027A4  8A C3                           mov al, bl
007027A6  48 83 C4 20                     add rsp, 0x20
007027AA  5B                              pop rbx
007027AB  C3                              ret
007027AC  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WdipSemSqmEnabled(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 8386135), v_rip - 7223784, a3, a4);
    v_rbx = 0;
    if ((unsigned __int8)(result) == 0) goto loc_007027A4;
    result = EtwEventEnabled(*(unsigned __int64 *)(v_rip + 8386110), v_rip - 7210609, a3, a4);
    if ((unsigned __int8)(result) != 0) {
        v_rbx = 1;
    }
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)(v_rbx);
}
```

## 5. (Beta) C Style

```c
void WdipSemSqmEnabled(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x7FF657), v_rip - 7223784, a3, a4);
    local_rbx = 0;
    if ((uint8_t)(result) == 0) goto loc_007027A4;
    result = EtwEventEnabled(*(uint64_t *)(v_rip + 0x7FF63E), v_rip - 7210609, a3, a4);
    if ((uint8_t)(result) != 0) {
        local_rbx = 1;
    }
    local_rsp = (local_rsp) + (32);
    return (uint8_t)(local_rbx);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0070276C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0070276C[BB_0070276C]
  bb_0070278B[BB_0070278B]
  bb_007027A2[BB_007027A2]
  bb_007027A4[BB_007027A4]
  bb_007027AC[BB_007027AC]
  bb_0070276C -->|branch| bb_007027A4
  bb_0070276C -->|fallthrough| bb_0070278B
  bb_0070278B -->|branch| bb_007027A4
  bb_0070278B -->|fallthrough| bb_007027A2
  bb_007027A2 -->|flow| bb_007027A4
```
