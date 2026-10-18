# KiNotifyAvailableCpusChangeCpuPartition

- RVA: `0x005B9AD8`–`0x005B9AFB` (길이 `35` bytes)
- VA: `0x00000001405B9AD8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `35/35` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005B9AF0` → [KiAvailableCpusSubscriptionQueueWorkItem](../4F/KiAvailableCpusSubscriptionQueueWorkItem_function_004FCE5C.md) (function, `0x004FCE5C`)

### Direct callers
- [KeTransitionProcessorParkState](../35/KeTransitionProcessorParkState_function_003527EC.md) at `0x00352B02`
- [KeCpuPartitionMoveCpus](../5C/KeCpuPartitionMoveCpus_function_005C0B70.md) at `0x005C0D8C`
- [KiAddCpuToSystemCpuPartition](../../pagelk/B6/KiAddCpuToSystemCpuPartition_function_00B680F0.md) at `0x00B6818C`

### Static image references
- `0x005B9ADC` → RVA `0x00F22FB0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005B9AD8  48 83 EC 28                     sub rsp, 0x28
005B9ADC  48 8D 05 CD 94 96 00            lea rax, [rip + 0x9694cd]
005B9AE3  48 39 05 C6 94 96 00            cmp qword ptr [rip + 0x9694c6], rax
005B9AEA  74 09                           je 0x1405b9af5
005B9AEC  48 83 C1 28                     add rcx, 0x28
005B9AF0  E8 67 33 F4 FF                  call 0x1404fce5c
005B9AF5  48 83 C4 28                     add rsp, 0x28
005B9AF9  C3                              ret
005B9AFA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiNotifyAvailableCpusChangeCpuPartition(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = v_rip + 9868493;
    if ((*(unsigned __int64 *)(v_rip + 9868486)) != (v_rip + 9868493)) {
        a1 = (a1) + (40);
        result = KiAvailableCpusSubscriptionQueueWorkItem(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiNotifyAvailableCpusChangeCpuPartition(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = v_rip + 9868493;
    if ((*(uint64_t *)(v_rip + 0x9694C6)) != (v_rip + 9868493)) {
        Arg1 = (Arg1) + (40);
        result = KiAvailableCpusSubscriptionQueueWorkItem(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B9AD8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005B9AD8[BB_005B9AD8]
  bb_005B9AEC[BB_005B9AEC]
  bb_005B9AF5[BB_005B9AF5]
  bb_005B9AFA[BB_005B9AFA]
  bb_005B9AD8 -->|branch| bb_005B9AF5
  bb_005B9AD8 -->|fallthrough| bb_005B9AEC
  bb_005B9AEC -->|flow| bb_005B9AF5
```
