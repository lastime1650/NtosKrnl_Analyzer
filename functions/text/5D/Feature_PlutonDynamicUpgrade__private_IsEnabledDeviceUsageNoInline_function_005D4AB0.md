# Feature_PlutonDynamicUpgrade__private_IsEnabledDeviceUsageNoInline

- RVA: `0x005D4AB0`–`0x005D4AE2` (길이 `50` bytes)
- VA: `0x00000001405D4AB0`
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
- `0x005D4AD7` → [Feature_PlutonDynamicUpgrade__private_IsEnabledFallback](Feature_PlutonDynamicUpgrade__private_IsEnabledFallback_function_005D4AE8.md) (function, `0x005D4AE8`)

### Direct callers
- [PopBuildMemoryImageHeader](../../pagelk/B6/PopBuildMemoryImageHeader_function_00B6CA20.md) at `0x00B6CCB0`

### Static image references
- `0x005D4ABA` → RVA `0x00FC4B00` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D4AB0  48 83 EC 28                     sub rsp, 0x28
005D4AB4  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
005D4ABA  8B 05 40 00 9F 00               mov eax, dword ptr [rip + 0x9f0040]
005D4AC0  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
005D4AC4  A8 10                           test al, 0x10
005D4AC6  74 05                           je 0x1405d4acd
005D4AC8  83 E0 01                        and eax, 1
005D4ACB  EB 0F                           jmp 0x1405d4adc
005D4ACD  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
005D4AD2  BA 03 00 00 00                  mov edx, 3
005D4AD7  E8 0C 00 00 00                  call 0x1405d4ae8
005D4ADC  48 83 C4 28                     add rsp, 0x28
005D4AE0  C3                              ret
005D4AE1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_PlutonDynamicUpgrade__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10420288)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10420288)))) & (16)) == 0) goto loc_005D4ACD;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10420288))) & (1));
    goto loc_005D4ADC;
loc_005D4ACD:
    result = Feature_PlutonDynamicUpgrade__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_005D4ADC:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_PlutonDynamicUpgrade__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9F0040)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9F0040)))) & (16)) == 0) goto loc_005D4ACD;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9F0040))) & (1));
    goto loc_005D4ADC;
loc_005D4ACD:
    result = Feature_PlutonDynamicUpgrade__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_005D4ADC:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D4AB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D4AB0[BB_005D4AB0]
  bb_005D4AC8[BB_005D4AC8]
  bb_005D4ACD[BB_005D4ACD]
  bb_005D4ADC[BB_005D4ADC]
  bb_005D4AE1[BB_005D4AE1]
  bb_005D4AB0 -->|branch| bb_005D4ACD
  bb_005D4AB0 -->|fallthrough| bb_005D4AC8
  bb_005D4AC8 -->|branch| bb_005D4ADC
  bb_005D4ACD -->|flow| bb_005D4ADC
```
