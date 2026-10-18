# Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline

- RVA: `0x005D9484`–`0x005D94B6` (길이 `50` bytes)
- VA: `0x00000001405D9484`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **7**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005D94AB` → [Feature_BatteryChargeLimitV2Support__private_IsEnabledFallback](Feature_BatteryChargeLimitV2Support__private_IsEnabledFallback_function_005D94BC.md) (function, `0x005D94BC`)

### Direct callers
- [PopBatteryInitialize](../../page/76/PopBatteryInitialize_function_00766834.md) at `0x007668DD`
- [PopSetBatteryDischargingState](../../page/A8/PopSetBatteryDischargingState_function_00A8450C.md) at `0x00A84582`
- [PopAccountBatteryEnergyChange](../../page/AD/PopAccountBatteryEnergyChange_function_00ADFE50.md) at `0x00ADFFAA`
- [PopAccountCbEnergyChange](../../page/AE/PopAccountCbEnergyChange_function_00AE0680.md) at `0x00AE074A`
- [PopBatteryWorker](../../page/AE/PopBatteryWorker_function_00AE1650.md) at `0x00AE189E`
- [PopBatteryWorker](../../page/AE/PopBatteryWorker_function_00AE1650.md) at `0x00AE19E5`
- [PopBatteryWorker](../../page/AE/PopBatteryWorker_function_00AE1650.md) at `0x00AE1F5F`
- [PopBatteryWorker](../../page/AE/PopBatteryWorker_function_00AE1650.md) at `0x00AE225D`
- [PopBatteryWorker](../../page/AE/PopBatteryWorker_function_00AE1650.md) at `0x00AE25DF`
- [PopBatteryInitPhaseTwo](../../init/C4/PopBatteryInitPhaseTwo_function_00C42148.md) at `0x00C42258`
- [PopBatteryReadOscBits](../../init/C4/PopBatteryReadOscBits_function_00C422A0.md) at `0x00C422E8`

### Static image references
- `0x005D948E` → RVA `0x00FC4770` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D9484  48 83 EC 28                     sub rsp, 0x28
005D9488  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
005D948E  8B 05 DC B2 9E 00               mov eax, dword ptr [rip + 0x9eb2dc]
005D9494  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
005D9498  A8 10                           test al, 0x10
005D949A  74 05                           je 0x1405d94a1
005D949C  83 E0 01                        and eax, 1
005D949F  EB 0F                           jmp 0x1405d94b0
005D94A1  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
005D94A6  BA 03 00 00 00                  mov edx, 3
005D94AB  E8 0C 00 00 00                  call 0x1405d94bc
005D94B0  48 83 C4 28                     add rsp, 0x28
005D94B4  C3                              ret
005D94B5  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10400476)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10400476)))) & (16)) == 0) goto loc_005D94A1;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10400476))) & (1));
    goto loc_005D94B0;
loc_005D94A1:
    result = Feature_BatteryChargeLimitV2Support__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_005D94B0:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_BatteryChargeLimitV2Support__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9EB2DC)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9EB2DC)))) & (16)) == 0) goto loc_005D94A1;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9EB2DC))) & (1));
    goto loc_005D94B0;
loc_005D94A1:
    result = Feature_BatteryChargeLimitV2Support__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_005D94B0:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D9484&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D9484[BB_005D9484]
  bb_005D949C[BB_005D949C]
  bb_005D94A1[BB_005D94A1]
  bb_005D94B0[BB_005D94B0]
  bb_005D94B5[BB_005D94B5]
  bb_005D9484 -->|branch| bb_005D94A1
  bb_005D9484 -->|fallthrough| bb_005D949C
  bb_005D949C -->|branch| bb_005D94B0
  bb_005D94A1 -->|flow| bb_005D94B0
```
