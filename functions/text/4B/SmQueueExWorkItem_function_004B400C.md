# SmQueueExWorkItem

- RVA: `0x004B400C`–`0x004B402E` (길이 `34` bytes)
- VA: `0x00000001404B400C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CEE8`
- 디코드: `11`개 명령, `34/34` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004B401C` → [ExQueueWorkItemToPartition](../35/ExQueueWorkItemToPartition_function_00356E2C.md) (function, `0x00356E2C`)
- `0x004B4027` → [ExQueueWorkItem](../2F/ExQueueWorkItem_function_002F9520.md) (function, `0x002F9520`)

### Direct callers
- [SMKM_STORE_MGR&lt;SM_TRAITS&gt;::SmHighMemPriorityWatchdogTimerCallback](../4C/SMKM_STORE_MGR_SM_TRAITS_SmHighMemPriorityWatchdogTimerCallback_function_004C6560.md) at `0x004C65BF`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B400C  48 83 EC 28                     sub rsp, 0x28
004B4010  4D 85 C0                        test r8, r8
004B4013  74 12                           je 0x1404b4027
004B4015  4D 8B C8                        mov r9, r8
004B4018  41 83 C8 FF                     or r8d, 0xffffffff
004B401C  E8 0B 2E EA FF                  call 0x140356e2c
004B4021  48 83 C4 28                     add rsp, 0x28
004B4025  C3                              ret
004B4026  CC                              int3
004B4027  E8 F4 54 E4 FF                  call 0x1402f9520
004B402C  EB F3                           jmp 0x1404b4021
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SmQueueExWorkItem(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (a3 == 0) goto loc_004B4027;
    a3 = (unsigned int)((a3) | (0xFFFFFFFFULL));
    result = ExQueueWorkItemToPartition(a1, a2, a3, a3);
loc_004B4021:
    v_rsp = (v_rsp) + (40);
    return result;
loc_004B4027:
    result = ExQueueWorkItem(a1, a2, a3, a3);
    goto loc_004B4021;
}
```

## 5. (Beta) C Style

```c
int64_t SmQueueExWorkItem(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (Arg3 == 0) goto loc_004B4027;
    Arg3 = (uint32_t)((Arg3) | (0xFFFFFFFFULL));
    result = ExQueueWorkItemToPartition(Arg1, Arg2, Arg3, Arg3);
loc_004B4021:
    local_rsp = (local_rsp) + (40);
    return result;
loc_004B4027:
    result = ExQueueWorkItem(Arg1, Arg2, Arg3, Arg3);
    goto loc_004B4021;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B400C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B400C[BB_004B400C]
  bb_004B4015[BB_004B4015]
  bb_004B4021[BB_004B4021]
  bb_004B4026[BB_004B4026]
  bb_004B4027[BB_004B4027]
  bb_004B400C -->|branch| bb_004B4027
  bb_004B400C -->|fallthrough| bb_004B4015
  bb_004B4015 -->|flow| bb_004B4021
  bb_004B4026 -->|flow| bb_004B4027
  bb_004B4027 -->|branch| bb_004B4021
```
