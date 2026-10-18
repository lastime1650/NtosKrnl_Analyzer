# PnpUnlockDeviceActionQueue

- RVA: `0x004A42F4`–`0x004A4380` (길이 `140` bytes)
- VA: `0x00000001404A42F4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0007A180`
- 디코드: `30`개 명령, `140/140` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **9**

### Outgoing calls
- `0x004A4301` → [KeAcquireSpinLockRaiseToDpc](../20/KeAcquireSpinLockRaiseToDpc_function_00208470.md) (function, `0x00208470`)
- `0x004A4342` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)
- `0x004A4350` → [KeReleaseSpinLock](../39/KeReleaseSpinLock_function_00392BA0.md) (function, `0x00392BA0`)
- `0x004A435A` → [PpDevNodeUnlockTree](../../page/A2/PpDevNodeUnlockTree_function_00A21290.md) (function, `0x00A21290`)
- `0x004A4379` → [KeSetEvent](../33/KeSetEvent_function_0033F310.md) (function, `0x0033F310`)

### Direct callers
- [IoControlPnpDeviceActionQueue](IoControlPnpDeviceActionQueue_function_004A42D4.md) at `0x004A42DC`
- [IoFreePoDeviceNotifyList](../../pagelk/B7/IoFreePoDeviceNotifyList_function_00B7CF84.md) at `0x00B7CFD4`
- [IopInitializeBootDrivers](../../init/C2/IopInitializeBootDrivers_function_00C2E6F4.md) at `0x00C2ECB1`
- [PipInitializeCoreDriversByGroup](../../init/C7/PipInitializeCoreDriversByGroup_function_00C740DC.md) at `0x00C741F4`

### Static image references
- `0x004A42FA` → RVA `0x00F8AD90` (`.data`; read)
- `0x004A4308` → RVA `0x00F8AD80` (`.data`; read)
- `0x004A4318` → RVA `0x00F8AD38` (`.data`; read/write)
- `0x004A4320` → RVA `0x00478400` (`PnpDeviceActionWorker`; read)
- `0x004A4327` → RVA `0x00F8AD20` (`.data`; read/write)
- `0x004A432F` → RVA `0x00F8AD20` (`.data`; read)
- `0x004A433B` → RVA `0x00F8AD30` (`.data`; write)
- `0x004A4369` → RVA `0x00F8AD40` (`.data`; write)
- `0x004A4372` → RVA `0x00F8AD60` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004A435A` → [PpDevNodeUnlockTree](../../page/A2/PpDevNodeUnlockTree_function_00A21290.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004A42F4  40 53                           push rbx
004A42F6  48 83 EC 20                     sub rsp, 0x20
004A42FA  48 8D 0D 8F 6A AE 00            lea rcx, [rip + 0xae6a8f]
004A4301  E8 6A 41 D6 FF                  call 0x140208470
004A4306  8A D8                           mov bl, al
004A4308  48 8D 05 71 6A AE 00            lea rax, [rip + 0xae6a71]
004A430F  48 39 05 6A 6A AE 00            cmp qword ptr [rip + 0xae6a6a], rax
004A4316  74 4E                           je 0x1404a4366
004A4318  48 83 25 18 6A AE 00 00         and qword ptr [rip + 0xae6a18], 0
004A4320  48 8D 05 D9 40 FD FF            lea rax, [rip - 0x2bf27]
004A4327  48 83 25 F1 69 AE 00 00         and qword ptr [rip + 0xae69f1], 0
004A432F  48 8D 0D EA 69 AE 00            lea rcx, [rip + 0xae69ea]
004A4336  BA 01 00 00 00                  mov edx, 1
004A433B  48 89 05 EE 69 AE 00            mov qword ptr [rip + 0xae69ee], rax
004A4342  E8 D9 51 E5 FF                  call 0x1402f9520
004A4347  8A D3                           mov dl, bl
004A4349  48 8D 0D 40 6A AE 00            lea rcx, [rip + 0xae6a40]
004A4350  E8 4B E8 EE FF                  call 0x140392ba0
004A4355  B9 01 00 00 00                  mov ecx, 1
004A435A  E8 31 CF 57 00                  call 0x140a21290
004A435F  48 83 C4 20                     add rsp, 0x20
004A4363  5B                              pop rbx
004A4364  C3                              ret
004A4365  CC                              int3
004A4366  45 33 C0                        xor r8d, r8d
004A4369  C6 05 D0 69 AE 00 00            mov byte ptr [rip + 0xae69d0], 0
004A4370  33 D2                           xor edx, edx
004A4372  48 8D 0D E7 69 AE 00            lea rcx, [rip + 0xae69e7]
004A4379  E8 92 AF E9 FF                  call 0x14033f310
004A437E  EB C7                           jmp 0x1404a4347
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpUnlockDeviceActionQueue(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11430543, a2, a3, a4);
    if ((*(unsigned __int64 *)(v_rip + 11430506)) == (v_rip + 11430513)) goto loc_004A4366;
    *(unsigned __int64 *)(v_rip + 11430382) = v_rip - 180007;
    result = ExQueueWorkItem(v_rip + 11430378, 1, a3, a4);
loc_004A4347:
    result = KeReleaseSpinLock(v_rip + 11430464, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    result = PpDevNodeUnlockTree(1, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_004A4366:
    a3 = 0;
    *(unsigned __int8 *)(v_rip + 11430352) = 0;
    a2 = 0;
    result = KeSetEvent(v_rip + 11430375, a2, a3, a4);
    goto loc_004A4347;
}
```

## 5. (Beta) C Style

```c
int64_t PnpUnlockDeviceActionQueue(int64_t Arg1, int64_t Arg2, int32_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = KeAcquireSpinLockRaiseToDpc(v_rip + 11430543, Arg2, Arg3, a4);
    if ((*(uint64_t *)(v_rip + 0xAE6A6A)) == (v_rip + 11430513)) goto loc_004A4366;
    *(uint64_t *)(v_rip + 0xAE69EE) = v_rip - 180007;
    result = ExQueueWorkItem(v_rip + 11430378, 1, Arg3, a4);
loc_004A4347:
    result = KeReleaseSpinLock(v_rip + 11430464, (uint8_t)((uint8_t)(result)), Arg3, a4);
    result = PpDevNodeUnlockTree(1, (uint8_t)((uint8_t)(result)), Arg3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_004A4366:
    Arg3 = 0;
    *(uint8_t *)(v_rip + 0xAE69D0) = 0;
    Arg2 = 0;
    result = KeSetEvent(v_rip + 11430375, Arg2, Arg3, a4);
    goto loc_004A4347;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004A42F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004A42F4[BB_004A42F4]
  bb_004A4318[BB_004A4318]
  bb_004A4347[BB_004A4347]
  bb_004A4365[BB_004A4365]
  bb_004A4366[BB_004A4366]
  bb_004A42F4 -->|branch| bb_004A4366
  bb_004A42F4 -->|fallthrough| bb_004A4318
  bb_004A4318 -->|flow| bb_004A4347
  bb_004A4365 -->|flow| bb_004A4366
  bb_004A4366 -->|branch| bb_004A4347
```
