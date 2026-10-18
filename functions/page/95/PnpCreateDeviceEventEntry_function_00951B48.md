# PnpCreateDeviceEventEntry

- RVA: `0x00951B48`–`0x00951B70` (길이 `40` bytes)
- VA: `0x0000000140951B48`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `11`개 명령, `40/40` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **14**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00951B59` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [PnpSetDeviceInstancePropertyChangeEventFromDeviceInstance](../../text/49/PnpSetDeviceInstancePropertyChangeEventFromDeviceInstance_function_00493500.md) at `0x0049352E`
- [PnpSetDeviceInstanceStartedEventFromDeviceInstance](../../text/4A/PnpSetDeviceInstanceStartedEventFromDeviceInstance_function_004AED80.md) at `0x004AEDAE`
- [PnpSetDeviceInstanceRemovalEvent](../../text/4B/PnpSetDeviceInstanceRemovalEvent_function_004B16D8.md) at `0x004B171E`
- [PnpShutdownDevices](../72/PnpShutdownDevices_function_00723F20.md) at `0x00723F8E`
- [PnpSetBlockedDriverEvent](../73/PnpSetBlockedDriverEvent_function_00738114.md) at `0x00738132`
- [PnpSetDeviceRemovalSafe](../73/PnpSetDeviceRemovalSafe_function_00738184.md) at `0x007381D5`
- [PnpSetHwProfileChangeEvent](../73/PnpSetHwProfileChangeEvent_function_00738290.md) at `0x007382C5`
- [PnpSetInvalidIDEvent](../73/PnpSetInvalidIDEvent_function_0073832C.md) at `0x0073835D`
- [PnpSetPowerVetoEvent](../73/PnpSetPowerVetoEvent_function_007383E4.md) at `0x00738458`
- [PnpSetPlugPlayEvent](../8F/PnpSetPlugPlayEvent_function_008FBE04.md) at `0x008FBE53`
- [PnpSetDeviceClassChange](PnpSetDeviceClassChange_function_009517B0.md) at `0x009517F0`
- [PnpInsertNoopEvent](PnpInsertNoopEvent_function_0095197C.md) at `0x00951991`
- [PnpSetCustomTargetEvent](PnpSetCustomTargetEvent_function_009519E8.md) at `0x00951A58`
- [PnpSynchronizeDeviceEventQueue](../AA/PnpSynchronizeDeviceEventQueue_function_00AA4F60.md) at `0x00AA4F8B`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00951B59` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00951B48  48 83 EC 28                     sub rsp, 0x28
00951B4C  8B D1                           mov edx, ecx
00951B4E  41 B8 50 6E 70 4B               mov r8d, 0x4b706e50
00951B54  B9 00 01 00 00                  mov ecx, 0x100
00951B59  E8 92 05 23 00                  call 0x140b820f0
00951B5E  48 85 C0                        test rax, rax
00951B61  74 07                           je 0x140951b6a
00951B63  C7 40 40 01 00 00 00            mov dword ptr [rax + 0x40], 1
00951B6A  48 83 C4 28                     add rsp, 0x28
00951B6E  C3                              ret
00951B6F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpCreateDeviceEventEntry(int a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExAllocatePool2(256, (unsigned int)(a1), (unsigned int)(0x4B706E50ULL), a4);
    if (result != 0) {
        *(unsigned int *)(result + 64) = 1;
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PnpCreateDeviceEventEntry(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExAllocatePool2(256, (uint32_t)(Arg1), (uint32_t)(0x4B706E50ULL), a4);
    if (result != 0) {
        *(uint32_t *)(result + 0x40) = 1;
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00951B48&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00951B48[BB_00951B48]
  bb_00951B63[BB_00951B63]
  bb_00951B6A[BB_00951B6A]
  bb_00951B6F[BB_00951B6F]
  bb_00951B48 -->|branch| bb_00951B6A
  bb_00951B48 -->|fallthrough| bb_00951B63
  bb_00951B63 -->|flow| bb_00951B6A
```
