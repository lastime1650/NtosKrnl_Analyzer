# Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledOtherReporting

- RVA: `0x0065137C`–`0x006513CB` (길이 `79` bytes)
- VA: `0x000000014065137C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `22`개 명령, `79/79` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x006513AC` → [wil_details_FeatureReporting_ReportUsageToService](../53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (function, `0x0053E6E4`)
- `0x006513BF` → [Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledFallback](../4F/Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledFallback_function_004F6A4C.md) (function, `0x004F6A4C`)

### Direct callers
- [Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledWithReporting](../22/Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledWithReporting_function_00222FF0.md) at `0x00223004`

### Static image references
- `0x00651388` → RVA `0x00FC4BD8` (`.data`; read)
- `0x0065139F` → RVA `0x000DF4D0` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0065137C  40 53                           push rbx
0065137E  48 83 EC 20                     sub rsp, 0x20
00651382  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
00651388  8B 1D 4A 38 97 00               mov ebx, dword ptr [rip + 0x97384a]
0065138E  89 5C 24 38                     mov dword ptr [rsp + 0x38], ebx
00651392  F6 C3 02                        test bl, 2
00651395  74 21                           je 0x1406513b8
00651397  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
0065139C  44 8B C1                        mov r8d, ecx
0065139F  48 8D 0D 2A E1 A8 FF            lea rcx, [rip - 0x571ed6]
006513A6  41 B9 01 00 00 00               mov r9d, 1
006513AC  E8 33 D3 EE FF                  call 0x14053e6e4
006513B1  83 E3 01                        and ebx, 1
006513B4  8B C3                           mov eax, ebx
006513B6  EB 0C                           jmp 0x1406513c4
006513B8  8B D1                           mov edx, ecx
006513BA  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
006513BF  E8 88 56 EA FF                  call 0x1404f6a4c
006513C4  48 83 C4 20                     add rsp, 0x20
006513C8  5B                              pop rbx
006513C9  C3                              ret
006513CA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledOtherReporting(int a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_rsp = (v_rsp) - (32);
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9910346)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9910346)))) & (2)) == 0) goto loc_006513B8;
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 5709526, v_stack_p10, (unsigned int)(a1), 1);
    v_rbx = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9910346))) & (1));
    goto loc_006513C4;
loc_006513B8:
    result = Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledFallback(v_stack_p10, (unsigned int)((unsigned int)(v_rip - 5709526)), (unsigned int)(a1), 1);
loc_006513C4:
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledOtherReporting(int32_t Arg1)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    local_rsp = (local_rsp) - (32);
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x97384A)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x97384A)))) & (2)) == 0) goto loc_006513B8;
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 5709526, v_stack_p10, (uint32_t)(Arg1), 1);
    local_rbx = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x97384A))) & (1));
    goto loc_006513C4;
loc_006513B8:
    result = Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledFallback(v_stack_p10, (uint32_t)((uint32_t)(v_rip - 5709526)), (uint32_t)(Arg1), 1);
loc_006513C4:
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0065137C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0065137C[BB_0065137C]
  bb_00651397[BB_00651397]
  bb_006513B8[BB_006513B8]
  bb_006513C4[BB_006513C4]
  bb_006513CA[BB_006513CA]
  bb_0065137C -->|branch| bb_006513B8
  bb_0065137C -->|fallthrough| bb_00651397
  bb_00651397 -->|branch| bb_006513C4
  bb_006513B8 -->|flow| bb_006513C4
```
