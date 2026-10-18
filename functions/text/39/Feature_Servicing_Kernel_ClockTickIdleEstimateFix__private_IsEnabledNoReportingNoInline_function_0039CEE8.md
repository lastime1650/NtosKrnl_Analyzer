# Feature_Servicing_Kernel_ClockTickIdleEstimateFix__private_IsEnabledNoReportingNoInline

- RVA: `0x0039CEE8`–`0x0039CF17` (길이 `47` bytes)
- VA: `0x000000014039CEE8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00064C74`
- 디코드: `14`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **5**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0039CF10` → [Feature_Servicing_Kernel_ClockTickIdleEstimateFix__private_IsEnabledFallback](../4F/Feature_Servicing_Kernel_ClockTickIdleEstimateFix__private_IsEnabledFallback_function_004FC904.md) (function, `0x004FC904`)

### Direct callers
- [KiSetClockTimerKTimerDeadlines](../23/KiSetClockTimerKTimerDeadlines_function_0023671C.md) at `0x0023675D`
- [KiUpdateTime](KiUpdateTime_function_0039B530.md) at `0x0039B7CA`
- [sub_0039CA0B](Unknown_function_0039CA0B.md) at `0x0039CA8C`
- [KeEstimateClockTickDuration](../4C/KeEstimateClockTickDuration_function_004C7CCC.md) at `0x004C7D43`
- [KeEstimateClockTickDuration](../4C/KeEstimateClockTickDuration_function_004C7CCC.md) at `0x004C7E67`
- [KePrepareClockTimerForIdle](../5B/KePrepareClockTimerForIdle_function_005BA49C.md) at `0x005BA51A`
- [KePrepareClockTimerForIdle](../5B/KePrepareClockTimerForIdle_function_005BA49C.md) at `0x005BA5AA`

### Static image references
- `0x0039CEF2` → RVA `0x00FC49C8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0039CEE8  48 83 EC 28                     sub rsp, 0x28
0039CEEC  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0039CEF2  8B 05 D0 7A C2 00               mov eax, dword ptr [rip + 0xc27ad0]
0039CEF8  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0039CEFC  A8 02                           test al, 2
0039CEFE  74 09                           je 0x14039cf09
0039CF00  83 E0 01                        and eax, 1
0039CF03  48 83 C4 28                     add rsp, 0x28
0039CF07  C3                              ret
0039CF08  CC                              int3
0039CF09  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0039CF0E  33 D2                           xor edx, edx
0039CF10  E8 EF F9 15 00                  call 0x1404fc904
0039CF15  EB EC                           jmp 0x14039cf03
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Servicing_Kernel_ClockTickIdleEstimateFix__private_IsEnabledNoReportingNoInline(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12745424)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12745424)))) & (2)) == 0) goto loc_0039CF09;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 12745424))) & (1));
loc_0039CF03:
    v_rsp = (v_rsp) + (40);
    return result;
loc_0039CF09:
    a2 = 0;
    result = Feature_Servicing_Kernel_ClockTickIdleEstimateFix__private_IsEnabledFallback(v_stack_p30, a2, a3, a4);
    goto loc_0039CF03;
}
```

## 5. (Beta) C Style

```c
int64_t Feature_Servicing_Kernel_ClockTickIdleEstimateFix__private_IsEnabledNoReportingNoInline(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC27AD0)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xC27AD0)))) & (2)) == 0) goto loc_0039CF09;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xC27AD0))) & (1));
loc_0039CF03:
    local_rsp = (local_rsp) + (40);
    return result;
loc_0039CF09:
    Arg2 = 0;
    result = Feature_Servicing_Kernel_ClockTickIdleEstimateFix__private_IsEnabledFallback(v_stack_p30, Arg2, a3, a4);
    goto loc_0039CF03;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0039CEE8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0039CEE8[BB_0039CEE8]
  bb_0039CF00[BB_0039CF00]
  bb_0039CF03[BB_0039CF03]
  bb_0039CF08[BB_0039CF08]
  bb_0039CF09[BB_0039CF09]
  bb_0039CEE8 -->|branch| bb_0039CF09
  bb_0039CEE8 -->|fallthrough| bb_0039CF00
  bb_0039CF00 -->|flow| bb_0039CF03
  bb_0039CF08 -->|flow| bb_0039CF09
  bb_0039CF09 -->|branch| bb_0039CF03
```
