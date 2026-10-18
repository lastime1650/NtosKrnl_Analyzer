# PopFxResidentTimeoutDpcRoutine

- RVA: `0x004A54C0`–`0x004A54EC` (길이 `44` bytes)
- VA: `0x00000001404A54C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006EDE0`
- 디코드: `13`개 명령, `44/44` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004A54D4` → [ExQueueWorkItemEx](../35/ExQueueWorkItemEx_function_003567B0.md) (function, `0x003567B0`)
- `0x004A54E5` → [PopFxArmResidentTimer](../2C/PopFxArmResidentTimer_function_002C0680.md) (function, `0x002C0680`)

### Direct callers
- [KiProcessExpiredTimerList](../23/KiProcessExpiredTimerList_function_00234200.md) at `0x0023453A`

### Static image references
- `0x004A54C8` → RVA `0x00F0E4E0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004A54C0  48 83 EC 28                     sub rsp, 0x28
004A54C4  41 83 C8 FF                     or r8d, 0xffffffff
004A54C8  48 8D 0D 11 90 A6 00            lea rcx, [rip + 0xa69011]
004A54CF  BA 01 00 00 00                  mov edx, 1
004A54D4  E8 D7 12 EB FF                  call 0x1403567b0
004A54D9  84 C0                           test al, al
004A54DB  74 06                           je 0x1404a54e3
004A54DD  48 83 C4 28                     add rsp, 0x28
004A54E1  C3                              ret
004A54E2  CC                              int3
004A54E3  B1 01                           mov cl, 1
004A54E5  E8 96 B1 E1 FF                  call 0x1402c0680
004A54EA  EB F1                           jmp 0x1404a54dd
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopFxResidentTimeoutDpcRoutine(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a3 = (unsigned int)((a3) | (0xFFFFFFFFULL));
    result = ExQueueWorkItemEx(v_rip + 10915857, 1, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_004A54E3;
loc_004A54DD:
    v_rsp = (v_rsp) + (40);
    return result;
loc_004A54E3:
    result = PopFxArmResidentTimer(1, 1, a3, a4);
    goto loc_004A54DD;
}
```

## 5. (Beta) C Style

```c
int64_t PopFxResidentTimeoutDpcRoutine(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg3 = (uint32_t)((Arg3) | (0xFFFFFFFFULL));
    result = ExQueueWorkItemEx(v_rip + 10915857, 1, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_004A54E3;
loc_004A54DD:
    local_rsp = (local_rsp) + (40);
    return result;
loc_004A54E3:
    result = PopFxArmResidentTimer(1, 1, Arg3, a4);
    goto loc_004A54DD;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A54C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004A54C0[BB_004A54C0]
  bb_004A54DD[BB_004A54DD]
  bb_004A54E2[BB_004A54E2]
  bb_004A54E3[BB_004A54E3]
  bb_004A54C0 -->|branch| bb_004A54E3
  bb_004A54C0 -->|fallthrough| bb_004A54DD
  bb_004A54E2 -->|flow| bb_004A54E3
  bb_004A54E3 -->|branch| bb_004A54DD
```
