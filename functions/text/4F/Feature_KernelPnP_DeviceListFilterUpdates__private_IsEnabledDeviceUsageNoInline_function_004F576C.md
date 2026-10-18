# Feature_KernelPnP_DeviceListFilterUpdates__private_IsEnabledDeviceUsageNoInline

- RVA: `0x004F576C`–`0x004F579E` (길이 `50` bytes)
- VA: `0x00000001404F576C`
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
- `0x004F5793` → [Feature_KernelPnP_DeviceListFilterUpdates__private_IsEnabledFallback](Feature_KernelPnP_DeviceListFilterUpdates__private_IsEnabledFallback_function_004F57A4.md) (function, `0x004F57A4`)

### Direct callers
- [PiCMCaptureDeviceListInputData](../../page/A2/PiCMCaptureDeviceListInputData_function_00A2BD70.md) at `0x00A2BEFD`

### Static image references
- `0x004F5776` → RVA `0x00FC4868` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F576C  48 83 EC 28                     sub rsp, 0x28
004F5770  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004F5776  8B 05 EC F0 AC 00               mov eax, dword ptr [rip + 0xacf0ec]
004F577C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F5780  A8 10                           test al, 0x10
004F5782  74 05                           je 0x1404f5789
004F5784  83 E0 01                        and eax, 1
004F5787  EB 0F                           jmp 0x1404f5798
004F5789  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004F578E  BA 03 00 00 00                  mov edx, 3
004F5793  E8 0C 00 00 00                  call 0x1404f57a4
004F5798  48 83 C4 28                     add rsp, 0x28
004F579C  C3                              ret
004F579D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_KernelPnP_DeviceListFilterUpdates__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11333868)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11333868)))) & (16)) == 0) goto loc_004F5789;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11333868))) & (1));
    goto loc_004F5798;
loc_004F5789:
    result = Feature_KernelPnP_DeviceListFilterUpdates__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F5798:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_KernelPnP_DeviceListFilterUpdates__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACF0EC)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACF0EC)))) & (16)) == 0) goto loc_004F5789;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xACF0EC))) & (1));
    goto loc_004F5798;
loc_004F5789:
    result = Feature_KernelPnP_DeviceListFilterUpdates__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F5798:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F576C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F576C[BB_004F576C]
  bb_004F5784[BB_004F5784]
  bb_004F5789[BB_004F5789]
  bb_004F5798[BB_004F5798]
  bb_004F579D[BB_004F579D]
  bb_004F576C -->|branch| bb_004F5789
  bb_004F576C -->|fallthrough| bb_004F5784
  bb_004F5784 -->|branch| bb_004F5798
  bb_004F5789 -->|flow| bb_004F5798
```
