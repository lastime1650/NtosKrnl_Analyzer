# Feature_UpperThresholdInheritance__private_ReportDeviceUsage

- RVA: `0x004AEE8C`–`0x004AEEEF` (길이 `99` bytes)
- VA: `0x00000001404AEE8C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009AE6C`
- 디코드: `23`개 명령, `99/99` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x004AEED2` → [wil_details_FeatureReporting_ReportUsageToService](../53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (function, `0x0053E6E4`)
- `0x004AEEE8` → [wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath](../53/wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath_function_0053E774.md) (function, `0x0053E774`)

### Direct callers
- [PopConfigureHeteroThresholds](../../page/A3/PopConfigureHeteroThresholds_function_00A36288.md) at `0x00A363FC`

### Static image references
- `0x004AEE96` → RVA `0x00FC4798` (`.data`; read)
- `0x004AEEC2` → RVA `0x000DD748` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004AEE8C  48 83 EC 28                     sub rsp, 0x28
004AEE90  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004AEE96  8B 0D FC 58 B1 00               mov ecx, dword ptr [rip + 0xb158fc]
004AEE9C  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
004AEEA0  F6 C1 10                        test cl, 0x10
004AEEA3  74 06                           je 0x1404aeeab
004AEEA5  48 83 C4 28                     add rsp, 0x28
004AEEA9  C3                              ret
004AEEAA  CC                              int3
004AEEAB  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
004AEEB0  41 B9 01 00 00 00               mov r9d, 1
004AEEB6  41 0B C9                        or ecx, r9d
004AEEB9  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
004AEEBE  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
004AEEC2  48 8D 0D 7F E8 C2 FF            lea rcx, [rip - 0x3d1781]
004AEEC9  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
004AEECE  45 8D 41 02                     lea r8d, [r9 + 2]
004AEED2  E8 0D F8 08 00                  call 0x14053e6e4
004AEED7  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004AEEDC  4C 8D 05 65 E8 C2 FF            lea r8, [rip - 0x3d179b]
004AEEE3  BA 03 00 00 00                  mov edx, 3
004AEEE8  E8 87 F8 08 00                  call 0x14053e774
004AEEED  EB B6                           jmp 0x1404aeea5
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_UpperThresholdInheritance__private_ReportDeviceUsage(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11622652)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11622652)))) & (16)) == 0) goto loc_004AEEAB;
loc_004AEEA5:
    v_rsp = (v_rsp) + (40);
    return result;
loc_004AEEAB:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11622652))) | (1));
    v_stack_p30 = v_stack_p30;
    v_stack_p30 = (unsigned int)(a1);
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 4003713, v_stack_p30, 1 + 2, 1);
    result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(v_stack_p30, 3, v_rip - 4003739, 1);
    goto loc_004AEEA5;
}
```

## 5. (Beta) C Style

```c
void Feature_UpperThresholdInheritance__private_ReportDeviceUsage(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB158FC)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB158FC)))) & (16)) == 0) goto loc_004AEEAB;
loc_004AEEA5:
    local_rsp = (local_rsp) + (40);
    return result;
loc_004AEEAB:
    a1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB158FC))) | (1));
    v_stack_p30 = v_stack_p30;
    v_stack_p30 = (uint32_t)(a1);
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 4003713, v_stack_p30, 1 + 2, 1);
    result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(v_stack_p30, 3, v_rip - 4003739, 1);
    goto loc_004AEEA5;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004AEE8C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004AEE8C[BB_004AEE8C]
  bb_004AEEA5[BB_004AEEA5]
  bb_004AEEAA[BB_004AEEAA]
  bb_004AEEAB[BB_004AEEAB]
  bb_004AEE8C -->|branch| bb_004AEEAB
  bb_004AEE8C -->|fallthrough| bb_004AEEA5
  bb_004AEEAA -->|flow| bb_004AEEAB
  bb_004AEEAB -->|branch| bb_004AEEA5
```
