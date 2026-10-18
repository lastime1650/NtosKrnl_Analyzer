# Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline

- RVA: `0x004F2E10`–`0x004F2E42` (길이 `50` bytes)
- VA: `0x00000001404F2E10`
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
- `0x004F2E37` → [Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledFallback](../5A/Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledFallback_function_005A9EF0.md) (function, `0x005A9EF0`)

### Direct callers
- [PiCMCaptureObjectInputData](../../page/8E/PiCMCaptureObjectInputData_function_008E8220.md) at `0x008E831D`
- [PiCMCaptureRegistryPropertyInputData](../../page/8E/PiCMCaptureRegistryPropertyInputData_function_008ED078.md) at `0x008ED1A2`
- [PiCMCapturePropertyInputData](../../page/8E/PiCMCapturePropertyInputData_function_008ED3A0.md) at `0x008ED4CE`
- [PiCMCaptureRegistryInputData](../../page/96/PiCMCaptureRegistryInputData_function_00962108.md) at `0x00962207`
- [PiCMCaptureRegisterInterfaceInputData](../../page/96/PiCMCaptureRegisterInterfaceInputData_function_00962C94.md) at `0x00962E75`
- [PiCMCaptureRegisterInterfaceInputData](../../page/96/PiCMCaptureRegisterInterfaceInputData_function_00962C94.md) at `0x00962FFA`
- [PiCMCaptureInterfaceAliasInputData](../../page/A4/PiCMCaptureInterfaceAliasInputData_function_00A47B18.md) at `0x00A47CB2`
- [PiCMCaptureCreateDeviceInputData](../../page/AC/PiCMCaptureCreateDeviceInputData_function_00ACBFA8.md) at `0x00ACC176`
- [PiCMCaptureCreateDeviceInputData](../../page/AC/PiCMCaptureCreateDeviceInputData_function_00ACBFA8.md) at `0x00ACC2F7`

### Static image references
- `0x004F2E1A` → RVA `0x00FC4898` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F2E10  48 83 EC 28                     sub rsp, 0x28
004F2E14  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004F2E1A  8B 05 78 1A AD 00               mov eax, dword ptr [rip + 0xad1a78]
004F2E20  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F2E24  A8 10                           test al, 0x10
004F2E26  74 05                           je 0x1404f2e2d
004F2E28  83 E0 01                        and eax, 1
004F2E2B  EB 0F                           jmp 0x1404f2e3c
004F2E2D  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004F2E32  BA 03 00 00 00                  mov edx, 3
004F2E37  E8 B4 70 0B 00                  call 0x1405a9ef0
004F2E3C  48 83 C4 28                     add rsp, 0x28
004F2E40  C3                              ret
004F2E41  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11344504)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11344504)))) & (16)) == 0) goto loc_004F2E2D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11344504))) & (1));
    goto loc_004F2E3C;
loc_004F2E2D:
    result = Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F2E3C:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAD1A78)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAD1A78)))) & (16)) == 0) goto loc_004F2E2D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xAD1A78))) & (1));
    goto loc_004F2E3C;
loc_004F2E2D:
    result = Feature_KernelPnP_ObjectNameUpdates__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F2E3C:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F2E10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F2E10[BB_004F2E10]
  bb_004F2E28[BB_004F2E28]
  bb_004F2E2D[BB_004F2E2D]
  bb_004F2E3C[BB_004F2E3C]
  bb_004F2E41[BB_004F2E41]
  bb_004F2E10 -->|branch| bb_004F2E2D
  bb_004F2E10 -->|fallthrough| bb_004F2E28
  bb_004F2E28 -->|branch| bb_004F2E3C
  bb_004F2E2D -->|flow| bb_004F2E3C
```
