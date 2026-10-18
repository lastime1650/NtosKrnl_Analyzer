# Feature_PerfImpTest_IsEnabledWithReporting

- RVA: `0x0066C320`–`0x0066C39B` (길이 `123` bytes)
- VA: `0x000000014066C320`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `34`개 명령, `123/123` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x0066C356` → [wil_details_FeatureReporting_ReportUsageToService](../53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (function, `0x0053E6E4`)
- `0x0066C38B` → [Feature_PerfImpTest__private_ReportUsageFallback](Feature_PerfImpTest__private_ReportUsageFallback_function_0066C3A4.md) (function, `0x0066C3A4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0066C34F` → RVA `0x000DC830` (`.rdata`; read)
- `0x0066C35D` → RVA `0x00FC45E0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0066C320  48 83 EC 28                     sub rsp, 0x28
0066C324  33 C0                           xor eax, eax
0066C326  8B D1                           mov edx, ecx
0066C328  85 C9                           test ecx, ecx
0066C32A  74 64                           je 0x14066c390
0066C32C  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0066C331  83 EA 03                        sub edx, 3
0066C334  74 3C                           je 0x14066c372
0066C336  83 FA 01                        cmp edx, 1
0066C339  74 22                           je 0x14066c35d
0066C33B  44 8B C1                        mov r8d, ecx
0066C33E  C7 44 24 38 01 00 00 00         mov dword ptr [rsp + 0x38], 1
0066C346  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
0066C34B  44 8D 48 01                     lea r9d, [rax + 1]
0066C34F  48 8D 0D DA 04 A7 FF            lea rcx, [rip - 0x58fb26]
0066C356  E8 89 23 ED FF                  call 0x14053e6e4
0066C35B  EB 33                           jmp 0x14066c390
0066C35D  8B 05 7D 82 95 00               mov eax, dword ptr [rip + 0x95827d]
0066C363  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0066C367  A8 20                           test al, 0x20
0066C369  75 25                           jne 0x14066c390
0066C36B  BA 04 00 00 00                  mov edx, 4
0066C370  EB 14                           jmp 0x14066c386
0066C372  8B 0D 68 82 95 00               mov ecx, dword ptr [rip + 0x958268]
0066C378  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
0066C37C  F6 C1 10                        test cl, 0x10
0066C37F  75 0F                           jne 0x14066c390
0066C381  BA 03 00 00 00                  mov edx, 3
0066C386  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0066C38B  E8 14 00 00 00                  call 0x14066c3a4
0066C390  B8 01 00 00 00                  mov eax, 1
0066C395  48 83 C4 28                     add rsp, 0x28
0066C399  C3                              ret
0066C39A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_PerfImpTest_IsEnabledWithReporting(int a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_rsp = (v_rsp) - (40);
    result = 0;
    if (a1 == 0) goto loc_0066C390;
    v_stack_p10 = 0;
    a2 = (unsigned int)(((unsigned int)(a1)) - (3));
    if (condition_is_equal) goto loc_0066C372;
    if (((unsigned int)(a2)) == 1) goto loc_0066C35D;
    v_stack_p10 = 1;
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 5831462, v_stack_p10, (unsigned int)(a1), result + 1);
    goto loc_0066C390;
loc_0066C35D:
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9798269)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9798269)))) & (32)) != 0) goto loc_0066C390;
    goto loc_0066C386;
loc_0066C372:
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9798248)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9798248)))) & (16)) != 0) goto loc_0066C390;
loc_0066C386:
    result = Feature_PerfImpTest__private_ReportUsageFallback(v_stack_p10, 3, (unsigned int)(a1), result + 1);
loc_0066C390:
    v_rsp = (v_rsp) + (40);
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t Feature_PerfImpTest_IsEnabledWithReporting(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    local_rsp = (local_rsp) - (40);
    result = 0;
    if (Arg1 == 0) goto loc_0066C390;
    v_stack_p10 = 0;
    a2 = (uint32_t)(((uint32_t)(Arg1)) - (3));
    if (condition_is_equal) goto loc_0066C372;
    if (((uint32_t)(a2)) == 1) goto loc_0066C35D;
    v_stack_p10 = 1;
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 5831462, v_stack_p10, (uint32_t)(Arg1), result + 1);
    goto loc_0066C390;
loc_0066C35D:
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x95827D)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x95827D)))) & (32)) != 0) goto loc_0066C390;
    goto loc_0066C386;
loc_0066C372:
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x958268)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x958268)))) & (16)) != 0) goto loc_0066C390;
loc_0066C386:
    result = Feature_PerfImpTest__private_ReportUsageFallback(v_stack_p10, 3, (uint32_t)(Arg1), result + 1);
loc_0066C390:
    local_rsp = (local_rsp) + (40);
    return 1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0066C320&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0066C320[BB_0066C320]
  bb_0066C32C[BB_0066C32C]
  bb_0066C336[BB_0066C336]
  bb_0066C33B[BB_0066C33B]
  bb_0066C35D[BB_0066C35D]
  bb_0066C36B[BB_0066C36B]
  bb_0066C372[BB_0066C372]
  bb_0066C381[BB_0066C381]
  bb_0066C386[BB_0066C386]
  bb_0066C390[BB_0066C390]
  bb_0066C39A[BB_0066C39A]
  bb_0066C320 -->|branch| bb_0066C390
  bb_0066C320 -->|fallthrough| bb_0066C32C
  bb_0066C32C -->|branch| bb_0066C372
  bb_0066C32C -->|fallthrough| bb_0066C336
  bb_0066C336 -->|branch| bb_0066C35D
  bb_0066C336 -->|fallthrough| bb_0066C33B
  bb_0066C33B -->|branch| bb_0066C390
  bb_0066C35D -->|branch| bb_0066C390
  bb_0066C35D -->|fallthrough| bb_0066C36B
  bb_0066C36B -->|branch| bb_0066C386
  bb_0066C372 -->|branch| bb_0066C390
  bb_0066C372 -->|fallthrough| bb_0066C381
  bb_0066C381 -->|flow| bb_0066C386
  bb_0066C386 -->|flow| bb_0066C390
```
