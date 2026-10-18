# CmpLockSiloKeyLockTrackerExclusive

- RVA: `0x008F9EF8`–`0x008F9F4E` (길이 `86` bytes)
- VA: `0x00000001408F9EF8`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `25`개 명령, `86/86` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **23**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008F9F1B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x008F9F34` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (function, `0x0020FC90`)

### Direct callers
- [PiDmListRemoveObject](../70/PiDmListRemoveObject_function_007045E8.md) at `0x0070461A`
- [PiPnpRtlEnsureObjectCached](../72/PiPnpRtlEnsureObjectCached_function_0072F928.md) at `0x0072F9A5`
- [PiDmListRemoveList](../73/PiDmListRemoveList_function_00730474.md) at `0x007304A9`
- [PiDmListRemoveList](../73/PiDmListRemoveList_function_00730474.md) at `0x007304C5`
- [KsepDbCacheInsertDevice](../74/KsepDbCacheInsertDevice_function_00748C64.md) at `0x00748C9B`
- [KseLookupHardwareId](../74/KseLookupHardwareId_function_0074A62C.md) at `0x0074A6A4`
- [KseLookupHardwareId](../74/KseLookupHardwareId_function_0074A62C.md) at `0x0074A6ED`
- [CmInitServerSiloState](../7E/CmInitServerSiloState_function_007E5B14.md) at `0x007E5B66`
- [sub_008E28A3](../8E/Unknown_function_008E28A3.md) at `0x008E29C3`
- [sub_008E2EB2](../8E/Unknown_function_008E2EB2.md) at `0x008E30BD`
- [sub_008E314B](../8E/Unknown_function_008E314B.md) at `0x008E3183`
- [sub_008E314B](../8E/Unknown_function_008E314B.md) at `0x008E32E6`
- [sub_008E314B](../8E/Unknown_function_008E314B.md) at `0x008E338F`
- [PiDmListEnumObjectsWithCallback](../8E/PiDmListEnumObjectsWithCallback_function_008E3B60.md) at `0x008E3CE0`
- [PiPnpRtlObjectEventWorker](PiPnpRtlObjectEventWorker_function_008F8630.md) at `0x008F8912`
- [PiDmObjectProcessPropertyChange](PiDmObjectProcessPropertyChange_function_008F8A48.md) at `0x008F8BFB`
- [PiDmObjectProcessPropertyChange](PiDmObjectProcessPropertyChange_function_008F8A48.md) at `0x008F8CD2`
- [PiDmObjectUpdateCachedObjectProperty](PiDmObjectUpdateCachedObjectProperty_function_008F9C94.md) at `0x008F9D60`
- [PiDmObjectUpdateCachedObjectProperty](PiDmObjectUpdateCachedObjectProperty_function_008F9C94.md) at `0x008F9E5A`
- [PiDmListAddList](../94/PiDmListAddList_function_0094F4F8.md) at `0x0094F537`
- [PiDmListAddList](../94/PiDmListAddList_function_0094F4F8.md) at `0x0094F576`
- [PiDmListAddObject](../95/PiDmListAddObject_function_00950128.md) at `0x0095015A`
- [IopProcessSetInterfaceState](../95/IopProcessSetInterfaceState_function_00950964.md) at `0x00950C45`
- [IopProcessSetInterfaceState](../95/IopProcessSetInterfaceState_function_00950964.md) at `0x00950D7C`
- [KseAddHardwareId](../95/KseAddHardwareId_function_00959254.md) at `0x009592B8`
- [KseQueryDeviceDataList](../95/KseQueryDeviceDataList_function_00959390.md) at `0x00959443`
- [KseResetDeviceCache](../95/KseResetDeviceCache_function_00959CDC.md) at `0x00959CF2`
- [KsepDbCacheQueryDevice](../95/KsepDbCacheQueryDevice_function_00959D20.md) at `0x00959D76`
- [CmpStopSiloKeyLockTracker](../9E/CmpStopSiloKeyLockTracker_function_009E7BF0.md) at `0x009E7C00`
- [sub_00B1DC0E](../B1/Unknown_function_00B1DC0E.md) at `0x00B1DE9C`
- [sub_00B3073E](../B3/Unknown_function_00B3073E.md) at `0x00B30761`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x008F9F1B` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x008F9F34` → [ExfAcquirePushLockExclusiveEx](../../text/20/ExfAcquirePushLockExclusiveEx_function_0020FC90.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008F9EF8  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008F9EFD  57                              push rdi
008F9EFE  48 83 EC 20                     sub rsp, 0x20
008F9F02  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
008F9F0B  45 33 C0                        xor r8d, r8d
008F9F0E  33 D2                           xor edx, edx
008F9F10  48 8B F9                        mov rdi, rcx
008F9F13  66 FF 88 E4 01 00 00            dec word ptr [rax + 0x1e4]
008F9F1A  90                              nop
008F9F1B  E8 10 63 91 FF                  call 0x140210230
008F9F20  F0 48 0F BA 2F 00               lock bts qword ptr [rdi], 0
008F9F26  48 8B D8                        mov rbx, rax
008F9F29  73 0E                           jae 0x1408f9f39
008F9F2B  4C 8B C7                        mov r8, rdi
008F9F2E  48 8B D0                        mov rdx, rax
008F9F31  48 8B CF                        mov rcx, rdi
008F9F34  E8 57 5D 91 FF                  call 0x14020fc90
008F9F39  48 85 DB                        test rbx, rbx
008F9F3C  74 04                           je 0x1408f9f42
008F9F3E  C6 43 0A 01                     mov byte ptr [rbx + 0xa], 1
008F9F42  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
008F9F47  48 83 C4 20                     add rsp, 0x20
008F9F4B  5F                              pop rdi
008F9F4C  C3                              ret
008F9F4D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpLockSiloKeyLockTrackerExclusive(__int64 a1, int a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a3 = 0;
    a2 = 0;
    result = KeAbPreAcquire(a1, a2, a3, a4);
    if (!(condition_is_above_or_equal)) {
        a3 = a1;
        a2 = result;
        a1 = a1;
        result = ExfAcquirePushLockExclusiveEx(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = 1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpLockSiloKeyLockTrackerExclusive(void *Arg1, int32_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg3 = 0;
    Arg2 = 0;
    result = KeAbPreAcquire(Arg1, Arg2, Arg3, a4);
    if (!(condition_is_above_or_equal)) {
        Arg3 = Arg1;
        Arg2 = result;
        Arg1 = Arg1;
        result = ExfAcquirePushLockExclusiveEx(Arg1, Arg2, Arg3, a4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = 1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008F9EF8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008F9EF8[BB_008F9EF8]
  bb_008F9F2B[BB_008F9F2B]
  bb_008F9F39[BB_008F9F39]
  bb_008F9F3E[BB_008F9F3E]
  bb_008F9F42[BB_008F9F42]
  bb_008F9F4D[BB_008F9F4D]
  bb_008F9EF8 -->|branch| bb_008F9F39
  bb_008F9EF8 -->|fallthrough| bb_008F9F2B
  bb_008F9F2B -->|flow| bb_008F9F39
  bb_008F9F39 -->|branch| bb_008F9F42
  bb_008F9F39 -->|fallthrough| bb_008F9F3E
  bb_008F9F3E -->|flow| bb_008F9F42
```
