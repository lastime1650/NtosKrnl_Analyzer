# Feature_PpmParkEx__private_IsEnabledNoReportingNoInline

- RVA: `0x004F40E0`–`0x004F410F` (길이 `47` bytes)
- VA: `0x00000001404F40E0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **11**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004F4104` → [Feature_PpmParkEx__private_IsEnabledFallback](../5B/Feature_PpmParkEx__private_IsEnabledFallback_function_005B613C.md) (function, `0x005B613C`)

### Direct callers
- [KeGetTopologySiblingGroupAffinityForProcessor](../39/KeGetTopologySiblingGroupAffinityForProcessor_function_0039EEE4.md) at `0x0039EF74`
- [KeGetTopologySiblingAffinityForProcessor](../4A/KeGetTopologySiblingAffinityForProcessor_function_004A946C.md) at `0x004A94B1`
- [KiConfigureInitialNodes](../5B/KiConfigureInitialNodes_function_005BC738.md) at `0x005BC784`
- [KiComputeTopologyConstants](../5C/KiComputeTopologyConstants_function_005C9CB8.md) at `0x005C9D2C`
- [KiComputeTopologyConstantsAmd](../5C/KiComputeTopologyConstantsAmd_function_005C9DCC.md) at `0x005C9EC4`
- [KiComputeTopologyConstantsAmd](../5C/KiComputeTopologyConstantsAmd_function_005C9DCC.md) at `0x005C9FBC`
- [KiComputeTopologyConstantsIntelCompatible](../5C/KiComputeTopologyConstantsIntelCompatible_function_005CA0A4.md) at `0x005CA26F`
- [KiComputeTopologyConstantsIntelCompatible](../5C/KiComputeTopologyConstantsIntelCompatible_function_005CA0A4.md) at `0x005CA27D`
- [KiComputeTopologyConstantsIntelCompatible](../5C/KiComputeTopologyConstantsIntelCompatible_function_005CA0A4.md) at `0x005CA389`
- [PpmHeteroHgsCpuSupportedForContainment](../5D/PpmHeteroHgsCpuSupportedForContainment_function_005D86C0.md) at `0x005D86D1`
- [PpmHeteroHgsDetectContainmentPresence](../5D/PpmHeteroHgsDetectContainmentPresence_function_005D8768.md) at `0x005D882C`
- [KiInitializeTopologyStructures](../../pagelk/B6/KiInitializeTopologyStructures_function_00B69708.md) at `0x00B69793`
- [KiSetFeatureBits](../../pagelk/B6/KiSetFeatureBits_function_00B6A03C.md) at `0x00B6A486`
- [KiSetFeatureBits](../../pagelk/B6/KiSetFeatureBits_function_00B6A03C.md) at `0x00B6A521`
- [KiSetFeatureBits](../../pagelk/B6/KiSetFeatureBits_function_00B6A03C.md) at `0x00B6A585`
- [KeInitSystem](../../init/C7/KeInitSystem_function_00C71660.md) at `0x00C71AFB`

### Static image references
- `0x004F40EA` → RVA `0x00FC4988` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F40E0  48 83 EC 28                     sub rsp, 0x28
004F40E4  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004F40EA  8B 05 98 08 AD 00               mov eax, dword ptr [rip + 0xad0898]
004F40F0  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F40F4  A8 02                           test al, 2
004F40F6  74 05                           je 0x1404f40fd
004F40F8  83 E0 01                        and eax, 1
004F40FB  EB 0C                           jmp 0x1404f4109
004F40FD  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004F4102  33 D2                           xor edx, edx
004F4104  E8 33 20 0C 00                  call 0x1405b613c
004F4109  48 83 C4 28                     add rsp, 0x28
004F410D  C3                              ret
004F410E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_PpmParkEx__private_IsEnabledNoReportingNoInline(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11339928)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11339928)))) & (2)) == 0) goto loc_004F40FD;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11339928))) & (1));
    goto loc_004F4109;
loc_004F40FD:
    a2 = 0;
    result = Feature_PpmParkEx__private_IsEnabledFallback(v_stack_p8, a2, a3, a4);
loc_004F4109:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Feature_PpmParkEx__private_IsEnabledNoReportingNoInline(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAD0898)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAD0898)))) & (2)) == 0) goto loc_004F40FD;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xAD0898))) & (1));
    goto loc_004F4109;
loc_004F40FD:
    Arg2 = 0;
    result = Feature_PpmParkEx__private_IsEnabledFallback(v_stack_p8, Arg2, a3, a4);
loc_004F4109:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F40E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F40E0[BB_004F40E0]
  bb_004F40F8[BB_004F40F8]
  bb_004F40FD[BB_004F40FD]
  bb_004F4109[BB_004F4109]
  bb_004F410E[BB_004F410E]
  bb_004F40E0 -->|branch| bb_004F40FD
  bb_004F40E0 -->|fallthrough| bb_004F40F8
  bb_004F40F8 -->|branch| bb_004F4109
  bb_004F40FD -->|flow| bb_004F4109
```
