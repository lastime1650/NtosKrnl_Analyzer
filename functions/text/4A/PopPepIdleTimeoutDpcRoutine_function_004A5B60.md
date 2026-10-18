# PopPepIdleTimeoutDpcRoutine

- RVA: `0x004A5B60`–`0x004A5B8C` (길이 `44` bytes)
- VA: `0x00000001404A5B60`
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
- `0x004A5B74` → [ExQueueWorkItemEx](../35/ExQueueWorkItemEx_function_003567B0.md) (function, `0x003567B0`)
- `0x004A5B85` → [PopPepArmIdleTimer](../2C/PopPepArmIdleTimer_function_002C0B9C.md) (function, `0x002C0B9C`)

### Direct callers
- [KiProcessExpiredTimerList](../23/KiProcessExpiredTimerList_function_00234200.md) at `0x00234491`

### Static image references
- `0x004A5B68` → RVA `0x00F076A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004A5B60  48 83 EC 28                     sub rsp, 0x28
004A5B64  41 83 C8 FF                     or r8d, 0xffffffff
004A5B68  48 8D 0D 31 1B A6 00            lea rcx, [rip + 0xa61b31]
004A5B6F  BA 01 00 00 00                  mov edx, 1
004A5B74  E8 37 0C EB FF                  call 0x1403567b0
004A5B79  84 C0                           test al, al
004A5B7B  74 06                           je 0x1404a5b83
004A5B7D  48 83 C4 28                     add rsp, 0x28
004A5B81  C3                              ret
004A5B82  CC                              int3
004A5B83  B1 01                           mov cl, 1
004A5B85  E8 12 B0 E1 FF                  call 0x1402c0b9c
004A5B8A  EB F1                           jmp 0x1404a5b7d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPepIdleTimeoutDpcRoutine(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a3 = (unsigned int)((a3) | (0xFFFFFFFFULL));
    result = ExQueueWorkItemEx(v_rip + 10885937, 1, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_004A5B83;
loc_004A5B7D:
    v_rsp = (v_rsp) + (40);
    return result;
loc_004A5B83:
    result = PopPepArmIdleTimer(1, 1, a3, a4);
    goto loc_004A5B7D;
}
```

## 5. (Beta) C Style

```c
int64_t PopPepIdleTimeoutDpcRoutine(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg3 = (uint32_t)((Arg3) | (0xFFFFFFFFULL));
    result = ExQueueWorkItemEx(v_rip + 10885937, 1, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_004A5B83;
loc_004A5B7D:
    local_rsp = (local_rsp) + (40);
    return result;
loc_004A5B83:
    result = PopPepArmIdleTimer(1, 1, Arg3, a4);
    goto loc_004A5B7D;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A5B60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004A5B60[BB_004A5B60]
  bb_004A5B7D[BB_004A5B7D]
  bb_004A5B82[BB_004A5B82]
  bb_004A5B83[BB_004A5B83]
  bb_004A5B60 -->|branch| bb_004A5B83
  bb_004A5B60 -->|fallthrough| bb_004A5B7D
  bb_004A5B82 -->|flow| bb_004A5B83
  bb_004A5B83 -->|branch| bb_004A5B7D
```
