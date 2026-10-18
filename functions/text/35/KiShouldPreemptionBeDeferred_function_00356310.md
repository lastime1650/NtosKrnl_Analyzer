# KiShouldPreemptionBeDeferred

- RVA: `0x00356310`–`0x0035632A` (길이 `26` bytes)
- VA: `0x0000000140356310`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `10`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **12**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiDeferGroupSchedulingPreemption](../20/KiDeferGroupSchedulingPreemption_function_0020076C.md) at `0x002008A6`
- [KiDeferGroupSchedulingPreemption](../20/KiDeferGroupSchedulingPreemption_function_0020076C.md) at `0x00200960`
- [KiDeferGroupSchedulingPreemption](../20/KiDeferGroupSchedulingPreemption_function_0020076C.md) at `0x00200DF1`
- [KiQueueReadyThread](../21/KiQueueReadyThread_function_0021C7B0.md) at `0x0021CC4B`
- [KiQueueReadyThread](../21/KiQueueReadyThread_function_0021C7B0.md) at `0x0021CE03`
- [sub_0021D7F8](../21/Unknown_function_0021D7F8.md) at `0x0021E228`
- [sub_0021D7F8](../21/Unknown_function_0021D7F8.md) at `0x0021E4F5`
- [sub_00254461](../25/Unknown_function_00254461.md) at `0x0025464D`
- [sub_00257DDC](../25/Unknown_function_00257DDC.md) at `0x00257E27`
- [sub_0025852E](../25/Unknown_function_0025852E.md) at `0x0025854B`
- [KiSearchForNewThreadsForRescheduleContext](../25/KiSearchForNewThreadsForRescheduleContext_function_00258620.md) at `0x00258F95`
- [KiAttemptToScheduleThreadToBusyIsolationUnit](../25/KiAttemptToScheduleThreadToBusyIsolationUnit_function_00259B00.md) at `0x0025ABA1`
- [KiGroupSchedulingQuantumEnd](../30/KiGroupSchedulingQuantumEnd_function_0030B220.md) at `0x0030B3CB`
- [KiGroupSchedulingQuantumEnd](../30/KiGroupSchedulingQuantumEnd_function_0030B220.md) at `0x0030B539`
- [KiSearchForNewThreadsOnTarget](../30/KiSearchForNewThreadsOnTarget_function_0030F500.md) at `0x0030FFFE`
- [KiSearchForNewThreadsOnTarget](../30/KiSearchForNewThreadsOnTarget_function_0030F500.md) at `0x003103E9`
- [KiSearchForNewThreadsOnTarget](../30/KiSearchForNewThreadsOnTarget_function_0030F500.md) at `0x003106E2`
- [KiSearchForNewThreadsOnTarget](../30/KiSearchForNewThreadsOnTarget_function_0030F500.md) at `0x0031074B`
- [KiSearchForNewThreadsOnTarget](../30/KiSearchForNewThreadsOnTarget_function_0030F500.md) at `0x00310B78`
- [KiSearchForNewThreadsOnTarget](../30/KiSearchForNewThreadsOnTarget_function_0030F500.md) at `0x00311027`
- [sub_0035602F](Unknown_function_0035602F.md) at `0x00356044`
- [KiQueryEffectivePriorityThreadWithStateLock](../5C/KiQueryEffectivePriorityThreadWithStateLock_function_005C6604.md) at `0x005C661F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00356310  83 B9 E4 01 00 00 00            cmp dword ptr [rcx + 0x1e4], 0
00356317  75 09                           jne 0x140356322
00356319  80 B9 86 01 00 00 01            cmp byte ptr [rcx + 0x186], 1
00356320  75 04                           jne 0x140356326
00356322  B0 01                           mov al, 1
00356324  C3                              ret
00356325  CC                              int3
00356326  32 C0                           xor al, al
00356328  C3                              ret
00356329  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiShouldPreemptionBeDeferred(__int64 a1)
{
    __int64 result;

    if ((*(unsigned int *)(a1 + 484)) != 0) goto loc_00356322;
    if ((*(unsigned __int8 *)(a1 + 390)) != 1) goto loc_00356326;
loc_00356322:
    return 1;
loc_00356326:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiShouldPreemptionBeDeferred(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if ((*(uint32_t *)(arg1 + 0x1E4)) != 0) goto loc_00356322;
    if ((*(uint8_t *)(arg1 + 0x186)) != 1) goto loc_00356326;
loc_00356322:
    return 1;
loc_00356326:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x186` | `8` | `R` |
| `Arg1` | `+ 0x1E4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00356310&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00356310[BB_00356310]
  bb_00356319[BB_00356319]
  bb_00356322[BB_00356322]
  bb_00356325[BB_00356325]
  bb_00356326[BB_00356326]
  bb_00356329[BB_00356329]
  bb_00356310 -->|branch| bb_00356322
  bb_00356310 -->|fallthrough| bb_00356319
  bb_00356319 -->|branch| bb_00356326
  bb_00356319 -->|fallthrough| bb_00356322
  bb_00356325 -->|flow| bb_00356326
```
