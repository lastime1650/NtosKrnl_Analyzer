# Feature_WorkQueueShardingWithinNodes__private_IsEnabledNoReportingNoInline

- RVA: `0x0065AA88`–`0x0065AAB7` (길이 `47` bytes)
- VA: `0x000000014065AA88`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0065AAAC` → [Feature_WorkQueueShardingWithinNodes__private_IsEnabledFallback](Feature_WorkQueueShardingWithinNodes__private_IsEnabledFallback_function_0065AA6C.md) (function, `0x0065AA6C`)

### Direct callers
- [sub_0035853D](../35/Unknown_function_0035853D.md) at `0x00358552`
- [ExpWorkerThread](../4E/ExpWorkerThread_function_004ECAF0.md) at `0x004ECC82`
- [ExpWorkQueueHealthMetricsEnabled](ExpWorkQueueHealthMetricsEnabled_function_0065A7AC.md) at `0x0065A7BB`

### Static image references
- `0x0065AA92` → RVA `0x00FC48B0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0065AA88  48 83 EC 28                     sub rsp, 0x28
0065AA8C  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0065AA92  8B 05 18 9E 96 00               mov eax, dword ptr [rip + 0x969e18]
0065AA98  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0065AA9C  A8 02                           test al, 2
0065AA9E  74 05                           je 0x14065aaa5
0065AAA0  83 E0 01                        and eax, 1
0065AAA3  EB 0C                           jmp 0x14065aab1
0065AAA5  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0065AAAA  33 D2                           xor edx, edx
0065AAAC  E8 BB FF FF FF                  call 0x14065aa6c
0065AAB1  48 83 C4 28                     add rsp, 0x28
0065AAB5  C3                              ret
0065AAB6  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_WorkQueueShardingWithinNodes__private_IsEnabledNoReportingNoInline(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9870872)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9870872)))) & (2)) == 0) goto loc_0065AAA5;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9870872))) & (1));
    goto loc_0065AAB1;
loc_0065AAA5:
    a2 = 0;
    result = Feature_WorkQueueShardingWithinNodes__private_IsEnabledFallback(v_stack_p8, a2, a3, a4);
loc_0065AAB1:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Feature_WorkQueueShardingWithinNodes__private_IsEnabledNoReportingNoInline(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x969E18)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x969E18)))) & (2)) == 0) goto loc_0065AAA5;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x969E18))) & (1));
    goto loc_0065AAB1;
loc_0065AAA5:
    Arg2 = 0;
    result = Feature_WorkQueueShardingWithinNodes__private_IsEnabledFallback(v_stack_p8, Arg2, a3, a4);
loc_0065AAB1:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0065AA88&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0065AA88[BB_0065AA88]
  bb_0065AAA0[BB_0065AAA0]
  bb_0065AAA5[BB_0065AAA5]
  bb_0065AAB1[BB_0065AAB1]
  bb_0065AAB6[BB_0065AAB6]
  bb_0065AA88 -->|branch| bb_0065AAA5
  bb_0065AA88 -->|fallthrough| bb_0065AAA0
  bb_0065AAA0 -->|branch| bb_0065AAB1
  bb_0065AAA5 -->|flow| bb_0065AAB1
```
