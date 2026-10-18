# Feature_PreventInterfaceChangeConcurrentNotify__private_ReportDeviceUsage

- RVA: `0x00487ED0`–`0x00487F33` (길이 `99` bytes)
- VA: `0x0000000140487ED0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009AE6C`
- 디코드: `23`개 명령, `99/99` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00487F16` → [wil_details_FeatureReporting_ReportUsageToService](../53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (function, `0x0053E6E4`)
- `0x00487F2C` → [wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath](../53/wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath_function_0053E774.md) (function, `0x0053E774`)

### Direct callers
- [IoRegisterPlugPlayNotification](../../page/95/IoRegisterPlugPlayNotification_function_009535A0.md) at `0x009538A5`
- [IoRegisterPlugPlayNotification](../../page/95/IoRegisterPlugPlayNotification_function_009535A0.md) at `0x009538D7`
- [PnpNotifyDriverCallback](../../page/95/PnpNotifyDriverCallback_function_00954AA0.md) at `0x00954ABE`

### Static image references
- `0x00487EDA` → RVA `0x00FC4840` (`.data`; read)
- `0x00487F06` → RVA `0x000DDBE0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00487ED0  48 83 EC 28                     sub rsp, 0x28
00487ED4  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00487EDA  8B 0D 60 C9 B3 00               mov ecx, dword ptr [rip + 0xb3c960]
00487EE0  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00487EE4  F6 C1 10                        test cl, 0x10
00487EE7  74 06                           je 0x140487eef
00487EE9  48 83 C4 28                     add rsp, 0x28
00487EED  C3                              ret
00487EEE  CC                              int3
00487EEF  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
00487EF4  41 B9 01 00 00 00               mov r9d, 1
00487EFA  41 0B C9                        or ecx, r9d
00487EFD  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00487F02  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00487F06  48 8D 0D D3 5C C5 FF            lea rcx, [rip - 0x3aa32d]
00487F0D  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
00487F12  45 8D 41 02                     lea r8d, [r9 + 2]
00487F16  E8 C9 67 0B 00                  call 0x14053e6e4
00487F1B  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00487F20  4C 8D 05 B9 5C C5 FF            lea r8, [rip - 0x3aa347]
00487F27  BA 03 00 00 00                  mov edx, 3
00487F2C  E8 43 68 0B 00                  call 0x14053e774
00487F31  EB B6                           jmp 0x140487ee9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_PreventInterfaceChangeConcurrentNotify__private_ReportDeviceUsage(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11782496)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11782496)))) & (16)) == 0) goto loc_00487EEF;
loc_00487EE9:
    v_rsp = (v_rsp) + (40);
    return result;
loc_00487EEF:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11782496))) | (1));
    v_stack_p30 = v_stack_p30;
    v_stack_p30 = (unsigned int)(a1);
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 3842861, v_stack_p30, 1 + 2, 1);
    result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(v_stack_p30, 3, v_rip - 3842887, 1);
    goto loc_00487EE9;
}
```

## 5. (Beta) C Style

```c
void Feature_PreventInterfaceChangeConcurrentNotify__private_ReportDeviceUsage(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB3C960)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xB3C960)))) & (16)) == 0) goto loc_00487EEF;
loc_00487EE9:
    local_rsp = (local_rsp) + (40);
    return result;
loc_00487EEF:
    a1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xB3C960))) | (1));
    v_stack_p30 = v_stack_p30;
    v_stack_p30 = (uint32_t)(a1);
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 3842861, v_stack_p30, 1 + 2, 1);
    result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(v_stack_p30, 3, v_rip - 3842887, 1);
    goto loc_00487EE9;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00487ED0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00487ED0[BB_00487ED0]
  bb_00487EE9[BB_00487EE9]
  bb_00487EEE[BB_00487EEE]
  bb_00487EEF[BB_00487EEF]
  bb_00487ED0 -->|branch| bb_00487EEF
  bb_00487ED0 -->|fallthrough| bb_00487EE9
  bb_00487EEE -->|flow| bb_00487EEF
  bb_00487EEF -->|branch| bb_00487EE9
```
