# Feature_WorkQueueShardingWithinNodes__private_IsEnabledDeviceUsageNoInline

- RVA: `0x0065AA34`–`0x0065AA66` (길이 `50` bytes)
- VA: `0x000000014065AA34`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0065AA5B` → [Feature_WorkQueueShardingWithinNodes__private_IsEnabledFallback](Feature_WorkQueueShardingWithinNodes__private_IsEnabledFallback_function_0065AA6C.md) (function, `0x0065AA6C`)

### Direct callers
- [ExpWorkQueueHealthMetricsMonitorCallback](ExpWorkQueueHealthMetricsMonitorCallback_function_0065A7F0.md) at `0x0065A80D`
- [ExStartStopWorkQueueProvider](../../page/7C/ExStartStopWorkQueueProvider_function_007CF59C.md) at `0x007CF5CB`
- [ExpWorkQueueInitializeHealthMetricsMonitor](../../page/7D/ExpWorkQueueInitializeHealthMetricsMonitor_function_007D00F4.md) at `0x007D00FA`
- [ExpWorkerInitialization](../../init/C5/ExpWorkerInitialization_function_00C539A4.md) at `0x00C53AFD`

### Static image references
- `0x0065AA3E` → RVA `0x00FC48B0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0065AA34  48 83 EC 28                     sub rsp, 0x28
0065AA38  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0065AA3E  8B 05 6C 9E 96 00               mov eax, dword ptr [rip + 0x969e6c]
0065AA44  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0065AA48  A8 10                           test al, 0x10
0065AA4A  74 05                           je 0x14065aa51
0065AA4C  83 E0 01                        and eax, 1
0065AA4F  EB 0F                           jmp 0x14065aa60
0065AA51  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0065AA56  BA 03 00 00 00                  mov edx, 3
0065AA5B  E8 0C 00 00 00                  call 0x14065aa6c
0065AA60  48 83 C4 28                     add rsp, 0x28
0065AA64  C3                              ret
0065AA65  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_WorkQueueShardingWithinNodes__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9870956)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9870956)))) & (16)) == 0) goto loc_0065AA51;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9870956))) & (1));
    goto loc_0065AA60;
loc_0065AA51:
    result = Feature_WorkQueueShardingWithinNodes__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0065AA60:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_WorkQueueShardingWithinNodes__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x969E6C)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x969E6C)))) & (16)) == 0) goto loc_0065AA51;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x969E6C))) & (1));
    goto loc_0065AA60;
loc_0065AA51:
    result = Feature_WorkQueueShardingWithinNodes__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0065AA60:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0065AA34&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0065AA34[BB_0065AA34]
  bb_0065AA4C[BB_0065AA4C]
  bb_0065AA51[BB_0065AA51]
  bb_0065AA60[BB_0065AA60]
  bb_0065AA65[BB_0065AA65]
  bb_0065AA34 -->|branch| bb_0065AA51
  bb_0065AA34 -->|fallthrough| bb_0065AA4C
  bb_0065AA4C -->|branch| bb_0065AA60
  bb_0065AA51 -->|flow| bb_0065AA60
```
