# Feature_TestUex12_IsEnabledWithReporting

- RVA: `0x0066CE40`–`0x0066CEBB` (길이 `123` bytes)
- VA: `0x000000014066CE40`
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
- `0x0066CE76` → [wil_details_FeatureReporting_ReportUsageToService](../53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (function, `0x0053E6E4`)
- `0x0066CEAB` → [Feature_TestUex12__private_ReportUsageFallback](Feature_TestUex12__private_ReportUsageFallback_function_0066CEC4.md) (function, `0x0066CEC4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0066CE6F` → RVA `0x000DCBB0` (`.rdata`; read)
- `0x0066CE7D` → RVA `0x00FC4588` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0066CE40  48 83 EC 28                     sub rsp, 0x28
0066CE44  33 C0                           xor eax, eax
0066CE46  8B D1                           mov edx, ecx
0066CE48  85 C9                           test ecx, ecx
0066CE4A  74 64                           je 0x14066ceb0
0066CE4C  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0066CE51  83 EA 03                        sub edx, 3
0066CE54  74 3C                           je 0x14066ce92
0066CE56  83 FA 01                        cmp edx, 1
0066CE59  74 22                           je 0x14066ce7d
0066CE5B  44 8B C1                        mov r8d, ecx
0066CE5E  C7 44 24 38 01 00 00 00         mov dword ptr [rsp + 0x38], 1
0066CE66  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
0066CE6B  44 8D 48 01                     lea r9d, [rax + 1]
0066CE6F  48 8D 0D 3A FD A6 FF            lea rcx, [rip - 0x5902c6]
0066CE76  E8 69 18 ED FF                  call 0x14053e6e4
0066CE7B  EB 33                           jmp 0x14066ceb0
0066CE7D  8B 05 05 77 95 00               mov eax, dword ptr [rip + 0x957705]
0066CE83  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0066CE87  A8 20                           test al, 0x20
0066CE89  75 25                           jne 0x14066ceb0
0066CE8B  BA 04 00 00 00                  mov edx, 4
0066CE90  EB 14                           jmp 0x14066cea6
0066CE92  8B 0D F0 76 95 00               mov ecx, dword ptr [rip + 0x9576f0]
0066CE98  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
0066CE9C  F6 C1 10                        test cl, 0x10
0066CE9F  75 0F                           jne 0x14066ceb0
0066CEA1  BA 03 00 00 00                  mov edx, 3
0066CEA6  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0066CEAB  E8 14 00 00 00                  call 0x14066cec4
0066CEB0  B8 01 00 00 00                  mov eax, 1
0066CEB5  48 83 C4 28                     add rsp, 0x28
0066CEB9  C3                              ret
0066CEBA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_TestUex12_IsEnabledWithReporting(int a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_rsp = (v_rsp) - (40);
    result = 0;
    if (a1 == 0) goto loc_0066CEB0;
    v_stack_p10 = 0;
    a2 = (unsigned int)(((unsigned int)(a1)) - (3));
    if (condition_is_equal) goto loc_0066CE92;
    if (((unsigned int)(a2)) == 1) goto loc_0066CE7D;
    v_stack_p10 = 1;
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 5833414, v_stack_p10, (unsigned int)(a1), result + 1);
    goto loc_0066CEB0;
loc_0066CE7D:
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9795333)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9795333)))) & (32)) != 0) goto loc_0066CEB0;
    goto loc_0066CEA6;
loc_0066CE92:
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9795312)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9795312)))) & (16)) != 0) goto loc_0066CEB0;
loc_0066CEA6:
    result = Feature_TestUex12__private_ReportUsageFallback(v_stack_p10, 3, (unsigned int)(a1), result + 1);
loc_0066CEB0:
    v_rsp = (v_rsp) + (40);
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t Feature_TestUex12_IsEnabledWithReporting(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    local_rsp = (local_rsp) - (40);
    result = 0;
    if (Arg1 == 0) goto loc_0066CEB0;
    v_stack_p10 = 0;
    a2 = (uint32_t)(((uint32_t)(Arg1)) - (3));
    if (condition_is_equal) goto loc_0066CE92;
    if (((uint32_t)(a2)) == 1) goto loc_0066CE7D;
    v_stack_p10 = 1;
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 5833414, v_stack_p10, (uint32_t)(Arg1), result + 1);
    goto loc_0066CEB0;
loc_0066CE7D:
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x957705)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x957705)))) & (32)) != 0) goto loc_0066CEB0;
    goto loc_0066CEA6;
loc_0066CE92:
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9576F0)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9576F0)))) & (16)) != 0) goto loc_0066CEB0;
loc_0066CEA6:
    result = Feature_TestUex12__private_ReportUsageFallback(v_stack_p10, 3, (uint32_t)(Arg1), result + 1);
loc_0066CEB0:
    local_rsp = (local_rsp) + (40);
    return 1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0066CE40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0066CE40[BB_0066CE40]
  bb_0066CE4C[BB_0066CE4C]
  bb_0066CE56[BB_0066CE56]
  bb_0066CE5B[BB_0066CE5B]
  bb_0066CE7D[BB_0066CE7D]
  bb_0066CE8B[BB_0066CE8B]
  bb_0066CE92[BB_0066CE92]
  bb_0066CEA1[BB_0066CEA1]
  bb_0066CEA6[BB_0066CEA6]
  bb_0066CEB0[BB_0066CEB0]
  bb_0066CEBA[BB_0066CEBA]
  bb_0066CE40 -->|branch| bb_0066CEB0
  bb_0066CE40 -->|fallthrough| bb_0066CE4C
  bb_0066CE4C -->|branch| bb_0066CE92
  bb_0066CE4C -->|fallthrough| bb_0066CE56
  bb_0066CE56 -->|branch| bb_0066CE7D
  bb_0066CE56 -->|fallthrough| bb_0066CE5B
  bb_0066CE5B -->|branch| bb_0066CEB0
  bb_0066CE7D -->|branch| bb_0066CEB0
  bb_0066CE7D -->|fallthrough| bb_0066CE8B
  bb_0066CE8B -->|branch| bb_0066CEA6
  bb_0066CE92 -->|branch| bb_0066CEB0
  bb_0066CE92 -->|fallthrough| bb_0066CEA1
  bb_0066CEA1 -->|flow| bb_0066CEA6
  bb_0066CEA6 -->|flow| bb_0066CEB0
```
