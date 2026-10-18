# PopAcquirePowerRequestPushLock

- RVA: `0x00A66D94`–`0x00A66DB5` (길이 `33` bytes)
- VA: `0x0000000140A66D94`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `10`개 명령, `33/33` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A66DA3` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (function, `0x00430B44`)
- `0x00A66DAE` → [PopAcquireRwLockShared](../../text/2D/PopAcquireRwLockShared_function_002D9A40.md) (function, `0x002D9A40`)

### Direct callers
- [PopPowerRequestCreateCommon](../../text/23/PopPowerRequestCreateCommon_function_00230150.md) at `0x0023019C`
- [PopPowerRequestCreateCommon](../../text/23/PopPowerRequestCreateCommon_function_00230150.md) at `0x00230281`
- [PopPowerRequestCreateCommon](../../text/23/PopPowerRequestCreateCommon_function_00230150.md) at `0x002303B5`
- [PopPowerRequestHandleRequestOverrideQueryResponse](../../text/47/PopPowerRequestHandleRequestOverrideQueryResponse_function_004777FC.md) at `0x0047781A`
- [PopPowerRequestCallbackWorker](../../text/47/PopPowerRequestCallbackWorker_function_00477AD0.md) at `0x00477BBF`
- [PopPowerRequestDebounceTimerWorker](../75/PopPowerRequestDebounceTimerWorker_function_00754A40.md) at `0x00754A4C`
- [PopPowerRequestExecutionRequiredTimeoutWorker](../75/PopPowerRequestExecutionRequiredTimeoutWorker_function_00754AF0.md) at `0x00754AF6`
- [PopPowerRequestNotificationsBegin](../75/PopPowerRequestNotificationsBegin_function_00754B24.md) at `0x00754B3A`
- [PopPowerRequestNotifyMobileHotspotChanged](../75/PopPowerRequestNotifyMobileHotspotChanged_function_00754BBC.md) at `0x00754BC6`
- [PopPowerRequestOverrideInitialize](../75/PopPowerRequestOverrideInitialize_function_00754C04.md) at `0x00754C10`
- [PopPowerRequestSpecialRequestSet](../A2/PopPowerRequestSpecialRequestSet_function_00A21B4C.md) at `0x00A21BEF`
- [PopPowerRequestNotifyUserSessionAttributed](../AD/PopPowerRequestNotifyUserSessionAttributed_function_00ADF48C.md) at `0x00ADF4B4`

### Static image references
- `0x00A66D9A` → RVA `0x00F0ED20` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A66DA3` → [PopAcquireRwLockExclusive](../../text/43/PopAcquireRwLockExclusive_function_00430B44.md) (`PAGE` → `.text`)
  - `0x00A66DAE` → [PopAcquireRwLockShared](../../text/2D/PopAcquireRwLockShared_function_002D9A40.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A66D94  48 83 EC 28                     sub rsp, 0x28
00A66D98  84 C9                           test cl, cl
00A66D9A  48 8D 0D 7F 7F 4A 00            lea rcx, [rip + 0x4a7f7f]
00A66DA1  74 0B                           je 0x140a66dae
00A66DA3  E8 9C 9D 9C FF                  call 0x140430b44
00A66DA8  48 83 C4 28                     add rsp, 0x28
00A66DAC  C3                              ret
00A66DAD  CC                              int3
00A66DAE  E8 8D 2C 87 FF                  call 0x1402d9a40
00A66DB3  EB F3                           jmp 0x140a66da8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopAcquirePowerRequestPushLock(unsigned __int8 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 == 0) goto loc_00A66DAE;
    result = PopAcquireRwLockExclusive(v_rip + 4882303, a2, a3, a4);
loc_00A66DA8:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00A66DAE:
    result = PopAcquireRwLockShared(v_rip + 4882303, a2, a3, a4);
    goto loc_00A66DA8;
}
```

## 5. (Beta) C Style

```c
int64_t PopAcquirePowerRequestPushLock(uint8_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 == 0) goto loc_00A66DAE;
    result = PopAcquireRwLockExclusive(v_rip + 4882303, a2, a3, a4);
loc_00A66DA8:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00A66DAE:
    result = PopAcquireRwLockShared(v_rip + 4882303, a2, a3, a4);
    goto loc_00A66DA8;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A66D94&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A66D94[BB_00A66D94]
  bb_00A66DA3[BB_00A66DA3]
  bb_00A66DA8[BB_00A66DA8]
  bb_00A66DAD[BB_00A66DAD]
  bb_00A66DAE[BB_00A66DAE]
  bb_00A66D94 -->|branch| bb_00A66DAE
  bb_00A66D94 -->|fallthrough| bb_00A66DA3
  bb_00A66DA3 -->|flow| bb_00A66DA8
  bb_00A66DAD -->|flow| bb_00A66DAE
  bb_00A66DAE -->|branch| bb_00A66DA8
```
