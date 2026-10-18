# PiDmObjectManagerAcquireExclusiveLock

- RVA: `0x00951334`–`0x00951356` (길이 `34` bytes)
- VA: `0x0000000140951334`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **9**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0095134B` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (function, `0x00214E20`)

### Direct callers
- [PopDripsWatchdogStopWatchdog](../70/PopDripsWatchdogStopWatchdog_function_00705674.md) at `0x0070567F`
- [PopPowerAggregatorEngageModernStandby](../76/PopPowerAggregatorEngageModernStandby_function_00764784.md) at `0x0076483A`
- [PopDripsWatchdogCallbackWorker](../76/PopDripsWatchdogCallbackWorker_function_0076C360.md) at `0x0076C384`
- [PopDripsWatchdogCallbackWorker](../76/PopDripsWatchdogCallbackWorker_function_0076C360.md) at `0x0076C4F4`
- [PopDripsWatchdogDiagnosticWorker](../76/PopDripsWatchdogDiagnosticWorker_function_0076C600.md) at `0x0076C65E`
- [PopDripsWatchdogDiagnosticWorker](../76/PopDripsWatchdogDiagnosticWorker_function_0076C600.md) at `0x0076C7BE`
- [PiDmListAddObjectWorker](PiDmListAddObjectWorker_function_009507B4.md) at `0x009507FF`
- [PiDmRemoveCacheReferenceForObject](PiDmRemoveCacheReferenceForObject_function_00950F24.md) at `0x00950F48`
- [PiDmAddCacheReferenceForObject](PiDmAddCacheReferenceForObject_function_00950FB4.md) at `0x0095101D`
- [PopDripsWatchdogStartWatchdog](../A3/PopDripsWatchdogStartWatchdog_function_00A32148.md) at `0x00A32166`
- [PiDmListRemoveObjectWorker](../A8/PiDmListRemoveObjectWorker_function_00A88748.md) at `0x00A887C9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0095134B` → [ExAcquireResourceExclusiveLite](../../text/21/ExAcquireResourceExclusiveLite_function_00214E20.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00951334  48 83 EC 28                     sub rsp, 0x28
00951338  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00951341  B2 01                           mov dl, 1
00951343  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
0095134A  90                              nop
0095134B  E8 D0 3A 8C FF                  call 0x140214e20
00951350  48 83 C4 28                     add rsp, 0x28
00951354  C3                              ret
00951355  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDmObjectManagerAcquireExclusiveLock(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExAcquireResourceExclusiveLite(a1, 1, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PiDmObjectManagerAcquireExclusiveLock(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExAcquireResourceExclusiveLite(a1, 1, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00951334&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00951334[BB_00951334]
  bb_00951355[BB_00951355]
```
