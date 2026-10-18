# Feature_Servicing_FixWarmRebootIssueOnLowCoreCPUs__private_IsEnabledDeviceUsageNoInline

- RVA: `0x0066B68C`–`0x0066B6BE` (길이 `50` bytes)
- VA: `0x000000014066B68C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0066B6B3` → [Feature_Servicing_FixWarmRebootIssueOnLowCoreCPUs__private_IsEnabledFallback](Feature_Servicing_FixWarmRebootIssueOnLowCoreCPUs__private_IsEnabledFallback_function_0066B6C4.md) (function, `0x0066B6C4`)

### Direct callers
- [CmFcManagerUnregisterFeatureUsageProvider](../../page/7F/CmFcManagerUnregisterFeatureUsageProvider_function_007F4ABC.md) at `0x007F4ADB`
- [CmFcpInitializeFeatureUsageProviderSubscription](../../page/7F/CmFcpInitializeFeatureUsageProviderSubscription_function_007F530C.md) at `0x007F5357`
- [CmFcpFeatureUsageProviderSubscriptionWrapper](../../page/AF/CmFcpFeatureUsageProviderSubscriptionWrapper_function_00AF7AB0.md) at `0x00AF7AD5`
- [CmFcpManagerProcessUsageDataProviders](../../page/AF/CmFcpManagerProcessUsageDataProviders_function_00AF7B6C.md) at `0x00AF7C3F`
- [CmFcpManagerProcessUsageDataProviders](../../page/AF/CmFcpManagerProcessUsageDataProviders_function_00AF7B6C.md) at `0x00AF7C5F`
- [CmFcpManagerProcessUsageDataProviders](../../page/AF/CmFcpManagerProcessUsageDataProviders_function_00AF7B6C.md) at `0x00AF7C83`

### Static image references
- `0x0066B696` → RVA `0x00FC4CA8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0066B68C  48 83 EC 28                     sub rsp, 0x28
0066B690  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0066B696  8B 05 0C 96 95 00               mov eax, dword ptr [rip + 0x95960c]
0066B69C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0066B6A0  A8 10                           test al, 0x10
0066B6A2  74 05                           je 0x14066b6a9
0066B6A4  83 E0 01                        and eax, 1
0066B6A7  EB 0F                           jmp 0x14066b6b8
0066B6A9  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0066B6AE  BA 03 00 00 00                  mov edx, 3
0066B6B3  E8 0C 00 00 00                  call 0x14066b6c4
0066B6B8  48 83 C4 28                     add rsp, 0x28
0066B6BC  C3                              ret
0066B6BD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Servicing_FixWarmRebootIssueOnLowCoreCPUs__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9803276)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9803276)))) & (16)) == 0) goto loc_0066B6A9;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9803276))) & (1));
    goto loc_0066B6B8;
loc_0066B6A9:
    result = Feature_Servicing_FixWarmRebootIssueOnLowCoreCPUs__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0066B6B8:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_Servicing_FixWarmRebootIssueOnLowCoreCPUs__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x95960C)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x95960C)))) & (16)) == 0) goto loc_0066B6A9;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x95960C))) & (1));
    goto loc_0066B6B8;
loc_0066B6A9:
    result = Feature_Servicing_FixWarmRebootIssueOnLowCoreCPUs__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0066B6B8:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0066B68C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0066B68C[BB_0066B68C]
  bb_0066B6A4[BB_0066B6A4]
  bb_0066B6A9[BB_0066B6A9]
  bb_0066B6B8[BB_0066B6B8]
  bb_0066B6BD[BB_0066B6BD]
  bb_0066B68C -->|branch| bb_0066B6A9
  bb_0066B68C -->|fallthrough| bb_0066B6A4
  bb_0066B6A4 -->|branch| bb_0066B6B8
  bb_0066B6A9 -->|flow| bb_0066B6B8
```
