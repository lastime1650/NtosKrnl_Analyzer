# PopBatteryEtwCallback

- RVA: `0x00766800`–`0x0076682E` (길이 `46` bytes)
- VA: `0x0000000140766800`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `12`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00766810` → [PopAcquireRwLockShared](../../text/2D/PopAcquireRwLockShared_function_002D9A40.md) (function, `0x002D9A40`)
- `0x00766817` → [PopBatteryTraceSystemBatteryStatus](../../text/4E/PopBatteryTraceSystemBatteryStatus_function_004E93D8.md) (function, `0x004E93D8`)
- `0x00766823` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00766809` → RVA `0x00F0C238` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00766810` → [PopAcquireRwLockShared](../../text/2D/PopAcquireRwLockShared_function_002D9A40.md) (`PAGE` → `.text`)
  - `0x00766817` → [PopBatteryTraceSystemBatteryStatus](../../text/4E/PopBatteryTraceSystemBatteryStatus_function_004E93D8.md) (`PAGE` → `.text`)
  - `0x00766823` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00766800  48 83 EC 28                     sub rsp, 0x28
00766804  83 FA 02                        cmp edx, 2
00766807  75 1F                           jne 0x140766828
00766809  48 8D 0D 28 5A 7A 00            lea rcx, [rip + 0x7a5a28]
00766810  E8 2B 32 B7 FF                  call 0x1402d9a40
00766815  B1 01                           mov cl, 1
00766817  E8 BC 2B D8 FF                  call 0x1404e93d8
0076681C  48 8D 0D 15 5A 7A 00            lea rcx, [rip + 0x7a5a15]
00766823  E8 94 93 B7 FF                  call 0x1402dfbbc
00766828  48 83 C4 28                     add rsp, 0x28
0076682C  C3                              ret
0076682D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopBatteryEtwCallback(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a2 == 2) {
        a1 = v_rip + 8018472;
        result = PopAcquireRwLockShared(a1, a2, a3, a4);
        a1 = 1;
        result = PopBatteryTraceSystemBatteryStatus(a1, a2, a3, a4);
        a1 = v_rip + 8018453;
        result = PopReleaseRwLock(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopBatteryEtwCallback(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg2 == 2) {
        Arg1 = v_rip + 8018472;
        result = PopAcquireRwLockShared(Arg1, Arg2, a3, a4);
        Arg1 = 1;
        result = PopBatteryTraceSystemBatteryStatus(Arg1, Arg2, a3, a4);
        Arg1 = v_rip + 8018453;
        result = PopReleaseRwLock(Arg1, Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00766800&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00766800[BB_00766800]
  bb_00766809[BB_00766809]
  bb_00766828[BB_00766828]
  bb_0076682D[BB_0076682D]
  bb_00766800 -->|branch| bb_00766828
  bb_00766800 -->|fallthrough| bb_00766809
  bb_00766809 -->|flow| bb_00766828
```
