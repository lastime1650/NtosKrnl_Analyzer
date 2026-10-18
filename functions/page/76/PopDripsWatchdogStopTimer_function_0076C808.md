# PopDripsWatchdogStopTimer

- RVA: `0x0076C808`–`0x0076C82A` (길이 `34` bytes)
- VA: `0x000000014076C808`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `12`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0076C813` → [KeCancelTimer2](../../text/3A/KeCancelTimer2_function_003A01E0.md) (function, `0x003A01E0`)

### Direct callers
- [PopDripsWatchdogStopWatchdog](../70/PopDripsWatchdogStopWatchdog_function_00705674.md) at `0x0070569F`
- [PopDripsWatchdogStopWatchdog](../70/PopDripsWatchdogStopWatchdog_function_00705674.md) at `0x007056B5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0076C813` → [KeCancelTimer2](../../text/3A/KeCancelTimer2_function_003A01E0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0076C808  40 53                           push rbx
0076C80A  48 83 EC 20                     sub rsp, 0x20
0076C80E  33 D2                           xor edx, edx
0076C810  48 8B D9                        mov rbx, rcx
0076C813  E8 C8 39 C3 FF                  call 0x1403a01e0
0076C818  84 C0                           test al, al
0076C81A  74 07                           je 0x14076c823
0076C81C  83 A3 B4 00 00 00 FD            and dword ptr [rbx + 0xb4], 0xfffffffd
0076C823  48 83 C4 20                     add rsp, 0x20
0076C827  5B                              pop rbx
0076C828  C3                              ret
0076C829  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopDripsWatchdogStopTimer(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    a2 = 0;
    result = KeCancelTimer2(a1, a2, a3, a4);
    if ((unsigned __int8)(result) != 0) {
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopDripsWatchdogStopTimer(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    Arg2 = 0;
    result = KeCancelTimer2(Arg1, Arg2, a3, a4);
    if ((uint8_t)(result) != 0) {
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xB4` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0076C808&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0076C808[BB_0076C808]
  bb_0076C81C[BB_0076C81C]
  bb_0076C823[BB_0076C823]
  bb_0076C829[BB_0076C829]
  bb_0076C808 -->|branch| bb_0076C823
  bb_0076C808 -->|fallthrough| bb_0076C81C
  bb_0076C81C -->|flow| bb_0076C823
```
