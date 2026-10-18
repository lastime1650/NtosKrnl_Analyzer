# Feature_Servicing_ThermalSxExitRereadZones__private_IsEnabledDeviceUsageNoInline

- RVA: `0x005D53F4`–`0x005D5426` (길이 `50` bytes)
- VA: `0x00000001405D53F4`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005D541B` → [Feature_Servicing_ThermalSxExitRereadZones__private_IsEnabledFallback](Feature_Servicing_ThermalSxExitRereadZones__private_IsEnabledFallback_function_005D542C.md) (function, `0x005D542C`)

### Direct callers
- [PopThermalSxExit](PopThermalSxExit_function_005D55F8.md) at `0x005D564E`
- [PopThermalSxExit](PopThermalSxExit_function_005D55F8.md) at `0x005D5711`

### Static image references
- `0x005D53FE` → RVA `0x00FC4B10` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D53F4  48 83 EC 28                     sub rsp, 0x28
005D53F8  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
005D53FE  8B 05 0C F7 9E 00               mov eax, dword ptr [rip + 0x9ef70c]
005D5404  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
005D5408  A8 10                           test al, 0x10
005D540A  74 05                           je 0x1405d5411
005D540C  83 E0 01                        and eax, 1
005D540F  EB 0F                           jmp 0x1405d5420
005D5411  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
005D5416  BA 03 00 00 00                  mov edx, 3
005D541B  E8 0C 00 00 00                  call 0x1405d542c
005D5420  48 83 C4 28                     add rsp, 0x28
005D5424  C3                              ret
005D5425  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Servicing_ThermalSxExitRereadZones__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10417932)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10417932)))) & (16)) == 0) goto loc_005D5411;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10417932))) & (1));
    goto loc_005D5420;
loc_005D5411:
    result = Feature_Servicing_ThermalSxExitRereadZones__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_005D5420:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_Servicing_ThermalSxExitRereadZones__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9EF70C)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9EF70C)))) & (16)) == 0) goto loc_005D5411;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9EF70C))) & (1));
    goto loc_005D5420;
loc_005D5411:
    result = Feature_Servicing_ThermalSxExitRereadZones__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_005D5420:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D53F4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D53F4[BB_005D53F4]
  bb_005D540C[BB_005D540C]
  bb_005D5411[BB_005D5411]
  bb_005D5420[BB_005D5420]
  bb_005D5425[BB_005D5425]
  bb_005D53F4 -->|branch| bb_005D5411
  bb_005D53F4 -->|fallthrough| bb_005D540C
  bb_005D540C -->|branch| bb_005D5420
  bb_005D5411 -->|flow| bb_005D5420
```
