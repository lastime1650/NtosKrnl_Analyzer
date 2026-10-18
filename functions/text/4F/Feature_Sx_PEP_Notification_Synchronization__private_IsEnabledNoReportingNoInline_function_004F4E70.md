# Feature_Sx_PEP_Notification_Synchronization__private_IsEnabledNoReportingNoInline

- RVA: `0x004F4E70`–`0x004F4E9F` (길이 `47` bytes)
- VA: `0x00000001404F4E70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **6**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004F4E94` → [Feature_Sx_PEP_Notification_Synchronization__private_IsEnabledFallback](Feature_Sx_PEP_Notification_Synchronization__private_IsEnabledFallback_function_004F4EA8.md) (function, `0x004F4EA8`)

### Direct callers
- [PopIrpWorker](../26/PopIrpWorker_function_0026D410.md) at `0x0026D6D2`
- [PopFxHandleReportDevicePoweredOn](../26/PopFxHandleReportDevicePoweredOn_function_0026D980.md) at `0x0026DA89`
- [PopFxHandleReportDevicePoweredOn](../26/PopFxHandleReportDevicePoweredOn_function_0026D980.md) at `0x0026DB03`
- [PopFxHandleReportDevicePoweredOn](../26/PopFxHandleReportDevicePoweredOn_function_0026D980.md) at `0x0026DB3D`
- [PopHandleDevicePowerIrpCompletion](../26/PopHandleDevicePowerIrpCompletion_function_0026F030.md) at `0x0026F089`
- [PopHandleDevicePowerIrpCompletion](../26/PopHandleDevicePowerIrpCompletion_function_0026F030.md) at `0x0026F12C`
- [PopHandleDevicePowerIrpCompletion](../26/PopHandleDevicePowerIrpCompletion_function_0026F030.md) at `0x0026F1A3`
- [PopFxActivateDevice](../4A/PopFxActivateDevice_function_004A0DC8.md) at `0x004A0F07`
- [PopSystemIrpCompletion](../../pagelk/B7/PopSystemIrpCompletion_function_00B70CC0.md) at `0x00B70D50`
- [PopSystemIrpCompletion](../../pagelk/B7/PopSystemIrpCompletion_function_00B70CC0.md) at `0x00B70E66`
- [PopNotifyDevice](../../pagelk/B7/PopNotifyDevice_function_00B7DAAC.md) at `0x00B7DB69`
- [PopNotifyDevice](../../pagelk/B7/PopNotifyDevice_function_00B7DAAC.md) at `0x00B7DBEF`

### Static image references
- `0x004F4E7A` → RVA `0x00FC4760` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F4E70  48 83 EC 28                     sub rsp, 0x28
004F4E74  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004F4E7A  8B 05 E0 F8 AC 00               mov eax, dword ptr [rip + 0xacf8e0]
004F4E80  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F4E84  A8 02                           test al, 2
004F4E86  74 05                           je 0x1404f4e8d
004F4E88  83 E0 01                        and eax, 1
004F4E8B  EB 0C                           jmp 0x1404f4e99
004F4E8D  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004F4E92  33 D2                           xor edx, edx
004F4E94  E8 0F 00 00 00                  call 0x1404f4ea8
004F4E99  48 83 C4 28                     add rsp, 0x28
004F4E9D  C3                              ret
004F4E9E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Sx_PEP_Notification_Synchronization__private_IsEnabledNoReportingNoInline(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11335904)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11335904)))) & (2)) == 0) goto loc_004F4E8D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11335904))) & (1));
    goto loc_004F4E99;
loc_004F4E8D:
    a2 = 0;
    result = Feature_Sx_PEP_Notification_Synchronization__private_IsEnabledFallback(v_stack_p8, a2, a3, a4);
loc_004F4E99:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Feature_Sx_PEP_Notification_Synchronization__private_IsEnabledNoReportingNoInline(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACF8E0)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACF8E0)))) & (2)) == 0) goto loc_004F4E8D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xACF8E0))) & (1));
    goto loc_004F4E99;
loc_004F4E8D:
    Arg2 = 0;
    result = Feature_Sx_PEP_Notification_Synchronization__private_IsEnabledFallback(v_stack_p8, Arg2, a3, a4);
loc_004F4E99:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F4E70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F4E70[BB_004F4E70]
  bb_004F4E88[BB_004F4E88]
  bb_004F4E8D[BB_004F4E8D]
  bb_004F4E99[BB_004F4E99]
  bb_004F4E9E[BB_004F4E9E]
  bb_004F4E70 -->|branch| bb_004F4E8D
  bb_004F4E70 -->|fallthrough| bb_004F4E88
  bb_004F4E88 -->|branch| bb_004F4E99
  bb_004F4E8D -->|flow| bb_004F4E99
```
