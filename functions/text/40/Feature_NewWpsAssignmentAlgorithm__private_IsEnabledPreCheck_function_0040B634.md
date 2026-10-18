# Feature_NewWpsAssignmentAlgorithm__private_IsEnabledPreCheck

- RVA: `0x0040B634`–`0x0040B69C` (길이 `104` bytes)
- VA: `0x000000014040B634`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009AE6C`
- 디코드: `24`개 명령, `104/104` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0040B67F` → [wil_details_FeatureReporting_ReportUsageToService](../53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (function, `0x0053E6E4`)
- `0x0040B695` → [wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath](../53/wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath_function_0053E774.md) (function, `0x0053E774`)

### Direct callers
- [PpmPerfRecordMostActiveWorkloadClass](PpmPerfRecordMostActiveWorkloadClass_function_0040B1A4.md) at `0x0040B3B7`

### Static image references
- `0x0040B63E` → RVA `0x00FC4998` (`.data`; read)
- `0x0040B66F` → RVA `0x000DE580` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0040B634  48 83 EC 28                     sub rsp, 0x28
0040B638  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0040B63E  8B 0D 54 93 BB 00               mov ecx, dword ptr [rip + 0xbb9354]
0040B644  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0040B648  F6 C1 10                        test cl, 0x10
0040B64B  74 0B                           je 0x14040b658
0040B64D  B8 01 00 00 00                  mov eax, 1
0040B652  48 83 C4 28                     add rsp, 0x28
0040B656  C3                              ret
0040B657  CC                              int3
0040B658  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0040B65D  83 C9 01                        or ecx, 1
0040B660  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0040B665  41 B9 01 00 00 00               mov r9d, 1
0040B66B  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
0040B66F  48 8D 0D 0A 2F CD FF            lea rcx, [rip - 0x32d0f6]
0040B676  48 8B 54 24 30                  mov rdx, qword ptr [rsp + 0x30]
0040B67B  45 8D 41 02                     lea r8d, [r9 + 2]
0040B67F  E8 60 30 13 00                  call 0x14053e6e4
0040B684  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0040B689  4C 8D 05 F0 2E CD FF            lea r8, [rip - 0x32d110]
0040B690  BA 03 00 00 00                  mov edx, 3
0040B695  E8 DA 30 13 00                  call 0x14053e774
0040B69A  EB B1                           jmp 0x14040b64d
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_NewWpsAssignmentAlgorithm__private_IsEnabledPreCheck(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12292948)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 12292948)))) & (16)) == 0) goto loc_0040B658;
loc_0040B64D:
    v_rsp = (v_rsp) + (40);
    return 1;
loc_0040B658:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 12292948))) | (1));
    v_stack_p30 = v_stack_p30;
    v_stack_p30 = (unsigned int)(a1);
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 3330294, v_stack_p30, 1 + 2, 1);
    result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(v_stack_p30, 3, v_rip - 3330320, 1);
    goto loc_0040B64D;
}
```

## 5. (Beta) C Style

```c
void Feature_NewWpsAssignmentAlgorithm__private_IsEnabledPreCheck(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p30;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB9354)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB9354)))) & (16)) == 0) goto loc_0040B658;
loc_0040B64D:
    local_rsp = (local_rsp) + (40);
    return 1;
loc_0040B658:
    a1 = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xBB9354))) | (1));
    v_stack_p30 = v_stack_p30;
    v_stack_p30 = (uint32_t)(a1);
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 3330294, v_stack_p30, 1 + 2, 1);
    result = wil_details_FeatureStateCache_TryEnableDeviceUsageFastPath(v_stack_p30, 3, v_rip - 3330320, 1);
    goto loc_0040B64D;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0040B634&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0040B634[BB_0040B634]
  bb_0040B64D[BB_0040B64D]
  bb_0040B657[BB_0040B657]
  bb_0040B658[BB_0040B658]
  bb_0040B634 -->|branch| bb_0040B658
  bb_0040B634 -->|fallthrough| bb_0040B64D
  bb_0040B657 -->|flow| bb_0040B658
  bb_0040B658 -->|branch| bb_0040B64D
```
