# PopPowerRequestRevokeRequestsForSleep

- RVA: `0x00AC68AC`–`0x00AC68DA` (길이 `46` bytes)
- VA: `0x0000000140AC68AC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `46/46` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AC68B7` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x00AC68C3` → [PopPowerRequestRevokeRequests](../../text/4C/PopPowerRequestRevokeRequests_function_004C0158.md) (function, `0x004C0158`)
- `0x00AC68CF` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (function, `0x002DFBBC`)

### Direct callers
- [PopPowerAggregatorEngageModernStandby](../76/PopPowerAggregatorEngageModernStandby_function_00764784.md) at `0x0076482E`
- [PopPowerAggregatorSystemTransitionEnterStateHandler](../76/PopPowerAggregatorSystemTransitionEnterStateHandler_function_007650E0.md) at `0x0076513B`

### Static image references
- `0x00AC68B0` → RVA `0x00F0ED20` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x00AC68B7` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x00AC68C3` → [PopPowerRequestRevokeRequests](../../text/4C/PopPowerRequestRevokeRequests_function_004C0158.md) (`PAGE` → `.text`)
  - `0x00AC68CF` → [PopReleaseRwLock](../../text/2D/PopReleaseRwLock_function_002DFBBC.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AC68AC  48 83 EC 28                     sub rsp, 0x28
00AC68B0  48 8D 0D 69 84 44 00            lea rcx, [rip + 0x448469]
00AC68B7  E8 88 A2 96 FF                  call 0x140430b44
00AC68BC  B2 01                           mov dl, 1
00AC68BE  B9 0A 00 00 00                  mov ecx, 0xa
00AC68C3  E8 90 98 9F FF                  call 0x1404c0158
00AC68C8  48 8D 0D 51 84 44 00            lea rcx, [rip + 0x448451]
00AC68CF  E8 E8 92 81 FF                  call 0x1402dfbbc
00AC68D4  48 83 C4 28                     add rsp, 0x28
00AC68D8  C3                              ret
00AC68D9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPowerRequestRevokeRequestsForSleep(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = PopAcquireRwLockExclusive(v_rip + 4490345, a2, a3, a4);
    result = PopPowerRequestRevokeRequests(10, 1, a3, a4);
    result = PopReleaseRwLock(v_rip + 4490321, 1, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PopPowerRequestRevokeRequestsForSleep(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = PopAcquireRwLockExclusive(v_rip + 4490345, a2, a3, a4);
    result = PopPowerRequestRevokeRequests(10, 1, a3, a4);
    result = PopReleaseRwLock(v_rip + 4490321, 1, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AC68AC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AC68AC[BB_00AC68AC]
  bb_00AC68D9[BB_00AC68D9]
```
