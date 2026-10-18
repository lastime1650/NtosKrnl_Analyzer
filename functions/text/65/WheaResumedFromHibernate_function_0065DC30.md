# WheaResumedFromHibernate

- RVA: `0x0065DC30`–`0x0065DC91` (길이 `97` bytes)
- VA: `0x000000014065DC30`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `22`개 명령, `97/97` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0065DC70` → [wil_details_FeatureReporting_ReportUsageToService](../53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (function, `0x0053E6E4`)
- `0x0065DC86` → [wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath](../53/wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath_function_0053E774.md) (function, `0x0053E774`)

### Direct callers
- [PopTransitionSystemPowerStateEx](../../pagelk/B7/PopTransitionSystemPowerStateEx_function_00B7E8C0.md) at `0x00B7EF6A`

### Static image references
- `0x0065DC3A` → RVA `0x00FC4C50` (`.data`; read)
- `0x0065DC60` → RVA `0x000DF850` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0065DC30  48 83 EC 28                     sub rsp, 0x28
0065DC34  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0065DC3A  8B 0D 10 70 96 00               mov ecx, dword ptr [rip + 0x967010]
0065DC40  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0065DC44  F6 C1 10                        test cl, 0x10
0065DC47  75 42                           jne 0x14065dc8b
0065DC49  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0065DC4E  41 B9 01 00 00 00               mov r9d, 1
0065DC54  41 0B C9                        or ecx, r9d
0065DC57  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0065DC5C  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0065DC60  48 8D 0D E9 1B A8 FF            lea rcx, [rip - 0x57e417]
0065DC67  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
0065DC6C  45 8D 41 02                     lea r8d, [r9 + 2]
0065DC70  E8 6F 0A EE FF                  call 0x14053e6e4
0065DC75  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0065DC7A  4C 8D 05 CF 1B A8 FF            lea r8, [rip - 0x57e431]
0065DC81  BA 03 00 00 00                  mov edx, 3
0065DC86  E8 E9 0A EE FF                  call 0x14053e774
0065DC8B  48 83 C4 28                     add rsp, 0x28
0065DC8F  C3                              ret
0065DC90  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall WheaResumedFromHibernate(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9859088)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9859088)))) & (16)) == 0) {
        result = v_stack_p8;
        a4 = 1;
        a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9859088))) | ((unsigned int)(a4)));
        v_stack_p8 = result;
        v_stack_p8 = (unsigned int)(a1);
        a1 = v_rip - 5760023;
        a2 = v_stack_p8;
        a3 = a4 + 2;
        result = wil_details_FeatureReporting_ReportUsageToService(a1, a2, a3, a4);
        a1 = v_stack_p8;
        a3 = v_rip - 5760049;
        a2 = 3;
        result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void WheaResumedFromHibernate(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x967010)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x967010)))) & (16)) == 0) {
        result = v_stack_p8;
        a4 = 1;
        a1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x967010))) | ((uint32_t)(a4)));
        v_stack_p8 = result;
        v_stack_p8 = (uint32_t)(a1);
        a1 = v_rip - 5760023;
        a2 = v_stack_p8;
        a3 = a4 + 2;
        result = wil_details_FeatureReporting_ReportUsageToService(a1, a2, a3, a4);
        a1 = v_stack_p8;
        a3 = v_rip - 5760049;
        a2 = 3;
        result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(a1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0065DC30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0065DC30[BB_0065DC30]
  bb_0065DC49[BB_0065DC49]
  bb_0065DC8B[BB_0065DC8B]
  bb_0065DC90[BB_0065DC90]
  bb_0065DC30 -->|branch| bb_0065DC8B
  bb_0065DC30 -->|fallthrough| bb_0065DC49
  bb_0065DC49 -->|flow| bb_0065DC8B
```
