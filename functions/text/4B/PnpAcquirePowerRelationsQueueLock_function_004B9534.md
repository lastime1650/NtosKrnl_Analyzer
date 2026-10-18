# PnpAcquirePowerRelationsQueueLock

- RVA: `0x004B9534`–`0x004B954A` (길이 `22` bytes)
- VA: `0x00000001404B9534`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `6`개 명령, `22/22` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004B953F` → [ExAcquireFastMutex](../20/ExAcquireFastMutex_function_0020E5A0.md) (function, `0x0020E5A0`)

### Direct callers
- [PipProcessRebuildPowerRelationsQueue](../../page/A0/PipProcessRebuildPowerRelationsQueue_function_00A06844.md) at `0x00A0685F`
- [PiQueryPowerRelations](../../page/AA/PiQueryPowerRelations_function_00AA3F9C.md) at `0x00AA4001`
- [PiQueryPowerRelations](../../page/AA/PiQueryPowerRelations_function_00AA3F9C.md) at `0x00AA4105`
- [PiQueryPowerDependencyRelations](../../page/AA/PiQueryPowerDependencyRelations_function_00AA4524.md) at `0x00AA45EA`
- [PiQueryPowerDependencyRelations](../../page/AA/PiQueryPowerDependencyRelations_function_00AA4524.md) at `0x00AA4693`
- [PiQueryPowerDependencyRelations](../../page/AA/PiQueryPowerDependencyRelations_function_00AA4524.md) at `0x00AA46DA`
- [PiValidatePowerRelations](../../page/AA/PiValidatePowerRelations_function_00AA4768.md) at `0x00AA4778`

### Static image references
- `0x004B9538` → RVA `0x00F8C3A0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B9534  48 83 EC 28                     sub rsp, 0x28
004B9538  48 8D 0D 61 2E AD 00            lea rcx, [rip + 0xad2e61]
004B953F  E8 5C 50 D5 FF                  call 0x14020e5a0
004B9544  48 83 C4 28                     add rsp, 0x28
004B9548  C3                              ret
004B9549  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpAcquirePowerRelationsQueueLock(void)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = ExAcquireFastMutex(v_rip + 11349601, a2, a3, a4);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void PnpAcquirePowerRelationsQueueLock(void)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = ExAcquireFastMutex(v_rip + 11349601, a2, a3, a4);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B9534&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B9534[BB_004B9534]
  bb_004B9549[BB_004B9549]
```
