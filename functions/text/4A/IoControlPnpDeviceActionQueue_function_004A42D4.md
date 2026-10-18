# IoControlPnpDeviceActionQueue

- RVA: `0x004A42D4`–`0x004A42EE` (길이 `26` bytes)
- VA: `0x00000001404A42D4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `9`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004A42DC` → [PnpUnlockDeviceActionQueue](PnpUnlockDeviceActionQueue_function_004A42F4.md) (function, `0x004A42F4`)
- `0x004A42E7` → [PnpLockDeviceActionQueue](PnpLockDeviceActionQueue_function_004A4388.md) (function, `0x004A4388`)

### Direct callers
- [WmipRegistrationWorker](../../page/9D/WmipRegistrationWorker_function_009DD820.md) at `0x009DD87D`
- [WmipRegistrationWorker](../../page/9D/WmipRegistrationWorker_function_009DD820.md) at `0x009DD884`
- [PopDirectedDripsInitializeBroadcast](../../page/A4/PopDirectedDripsInitializeBroadcast_function_00A4D634.md) at `0x00A4D6C7`
- [PopDirectedDripsInitializeBroadcast](../../page/A4/PopDirectedDripsInitializeBroadcast_function_00A4D634.md) at `0x00A4D82C`
- [IoDiagTraceDevicesRundown](../../page/A5/IoDiagTraceDevicesRundown_function_00A554C0.md) at `0x00A554C8`
- [IoDiagTraceDevicesRundown](../../page/A5/IoDiagTraceDevicesRundown_function_00A554C0.md) at `0x00A55524`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004A42D4  48 83 EC 28                     sub rsp, 0x28
004A42D8  84 C9                           test cl, cl
004A42DA  75 0B                           jne 0x1404a42e7
004A42DC  E8 13 00 00 00                  call 0x1404a42f4
004A42E1  48 83 C4 28                     add rsp, 0x28
004A42E5  C3                              ret
004A42E6  CC                              int3
004A42E7  E8 9C 00 00 00                  call 0x1404a4388
004A42EC  EB F3                           jmp 0x1404a42e1
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoControlPnpDeviceActionQueue(unsigned __int8 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a1 != 0) goto loc_004A42E7;
    result = PnpUnlockDeviceActionQueue(a1, a2, a3, a4);
loc_004A42E1:
    v_rsp = (v_rsp) + (40);
    return result;
loc_004A42E7:
    result = PnpLockDeviceActionQueue(a1, a2, a3, a4);
    goto loc_004A42E1;
}
```

## 5. (Beta) C Style

```c
int64_t IoControlPnpDeviceActionQueue(uint8_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg1 != 0) goto loc_004A42E7;
    result = PnpUnlockDeviceActionQueue(Arg1, a2, a3, a4);
loc_004A42E1:
    local_rsp = (local_rsp) + (40);
    return result;
loc_004A42E7:
    result = PnpLockDeviceActionQueue(Arg1, a2, a3, a4);
    goto loc_004A42E1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A42D4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004A42D4[BB_004A42D4]
  bb_004A42DC[BB_004A42DC]
  bb_004A42E1[BB_004A42E1]
  bb_004A42E6[BB_004A42E6]
  bb_004A42E7[BB_004A42E7]
  bb_004A42D4 -->|branch| bb_004A42E7
  bb_004A42D4 -->|fallthrough| bb_004A42DC
  bb_004A42DC -->|flow| bb_004A42E1
  bb_004A42E6 -->|flow| bb_004A42E7
  bb_004A42E7 -->|branch| bb_004A42E1
```
