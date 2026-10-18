# Feature_UxPerfImp_IsEnabledWithReporting

- RVA: `0x0066D660`–`0x0066D6DB` (길이 `123` bytes)
- VA: `0x000000014066D660`
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
- `0x0066D696` → [wil_details_FeatureReporting_ReportUsageToService](../53/wil_details_FeatureReporting_ReportUsageToService_function_0053E6E4.md) (function, `0x0053E6E4`)
- `0x0066D6CB` → [Feature_UxPerfImp__private_ReportUsageFallback](Feature_UxPerfImp__private_ReportUsageFallback_function_0066D6E4.md) (function, `0x0066D6E4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0066D68F` → RVA `0x000DC408` (`.rdata`; read)
- `0x0066D69D` → RVA `0x00FC4538` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0066D660  48 83 EC 28                     sub rsp, 0x28
0066D664  33 C0                           xor eax, eax
0066D666  8B D1                           mov edx, ecx
0066D668  85 C9                           test ecx, ecx
0066D66A  74 64                           je 0x14066d6d0
0066D66C  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
0066D671  83 EA 03                        sub edx, 3
0066D674  74 3C                           je 0x14066d6b2
0066D676  83 FA 01                        cmp edx, 1
0066D679  74 22                           je 0x14066d69d
0066D67B  44 8B C1                        mov r8d, ecx
0066D67E  C7 44 24 38 01 00 00 00         mov dword ptr [rsp + 0x38], 1
0066D686  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
0066D68B  44 8D 48 01                     lea r9d, [rax + 1]
0066D68F  48 8D 0D 72 ED A6 FF            lea rcx, [rip - 0x59128e]
0066D696  E8 49 10 ED FF                  call 0x14053e6e4
0066D69B  EB 33                           jmp 0x14066d6d0
0066D69D  8B 05 95 6E 95 00               mov eax, dword ptr [rip + 0x956e95]
0066D6A3  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
0066D6A7  A8 20                           test al, 0x20
0066D6A9  75 25                           jne 0x14066d6d0
0066D6AB  BA 04 00 00 00                  mov edx, 4
0066D6B0  EB 14                           jmp 0x14066d6c6
0066D6B2  8B 0D 80 6E 95 00               mov ecx, dword ptr [rip + 0x956e80]
0066D6B8  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
0066D6BC  F6 C1 10                        test cl, 0x10
0066D6BF  75 0F                           jne 0x14066d6d0
0066D6C1  BA 03 00 00 00                  mov edx, 3
0066D6C6  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
0066D6CB  E8 14 00 00 00                  call 0x14066d6e4
0066D6D0  B8 01 00 00 00                  mov eax, 1
0066D6D5  48 83 C4 28                     add rsp, 0x28
0066D6D9  C3                              ret
0066D6DA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_UxPerfImp_IsEnabledWithReporting(int a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_rsp = (v_rsp) - (40);
    result = 0;
    if (a1 == 0) goto loc_0066D6D0;
    v_stack_p10 = 0;
    a2 = (unsigned int)(((unsigned int)(a1)) - (3));
    if (condition_is_equal) goto loc_0066D6B2;
    if (((unsigned int)(a2)) == 1) goto loc_0066D69D;
    v_stack_p10 = 1;
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 5837454, v_stack_p10, (unsigned int)(a1), result + 1);
    goto loc_0066D6D0;
loc_0066D69D:
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9793173)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9793173)))) & (32)) != 0) goto loc_0066D6D0;
    goto loc_0066D6C6;
loc_0066D6B2:
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9793152)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9793152)))) & (16)) != 0) goto loc_0066D6D0;
loc_0066D6C6:
    result = Feature_UxPerfImp__private_ReportUsageFallback(v_stack_p10, 3, (unsigned int)(a1), result + 1);
loc_0066D6D0:
    v_rsp = (v_rsp) + (40);
    return 1;
}
```

## 5. (Beta) C Style

```c
int64_t Feature_UxPerfImp_IsEnabledWithReporting(int32_t Arg1)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    local_rsp = (local_rsp) - (40);
    result = 0;
    if (Arg1 == 0) goto loc_0066D6D0;
    v_stack_p10 = 0;
    a2 = (uint32_t)(((uint32_t)(Arg1)) - (3));
    if (condition_is_equal) goto loc_0066D6B2;
    if (((uint32_t)(a2)) == 1) goto loc_0066D69D;
    v_stack_p10 = 1;
    result = wil_details_FeatureReporting_ReportUsageToService(v_rip - 5837454, v_stack_p10, (uint32_t)(Arg1), result + 1);
    goto loc_0066D6D0;
loc_0066D69D:
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x956E95)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x956E95)))) & (32)) != 0) goto loc_0066D6D0;
    goto loc_0066D6C6;
loc_0066D6B2:
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x956E80)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x956E80)))) & (16)) != 0) goto loc_0066D6D0;
loc_0066D6C6:
    result = Feature_UxPerfImp__private_ReportUsageFallback(v_stack_p10, 3, (uint32_t)(Arg1), result + 1);
loc_0066D6D0:
    local_rsp = (local_rsp) + (40);
    return 1;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0066D660&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0066D660[BB_0066D660]
  bb_0066D66C[BB_0066D66C]
  bb_0066D676[BB_0066D676]
  bb_0066D67B[BB_0066D67B]
  bb_0066D69D[BB_0066D69D]
  bb_0066D6AB[BB_0066D6AB]
  bb_0066D6B2[BB_0066D6B2]
  bb_0066D6C1[BB_0066D6C1]
  bb_0066D6C6[BB_0066D6C6]
  bb_0066D6D0[BB_0066D6D0]
  bb_0066D6DA[BB_0066D6DA]
  bb_0066D660 -->|branch| bb_0066D6D0
  bb_0066D660 -->|fallthrough| bb_0066D66C
  bb_0066D66C -->|branch| bb_0066D6B2
  bb_0066D66C -->|fallthrough| bb_0066D676
  bb_0066D676 -->|branch| bb_0066D69D
  bb_0066D676 -->|fallthrough| bb_0066D67B
  bb_0066D67B -->|branch| bb_0066D6D0
  bb_0066D69D -->|branch| bb_0066D6D0
  bb_0066D69D -->|fallthrough| bb_0066D6AB
  bb_0066D6AB -->|branch| bb_0066D6C6
  bb_0066D6B2 -->|branch| bb_0066D6D0
  bb_0066D6B2 -->|fallthrough| bb_0066D6C1
  bb_0066D6C1 -->|flow| bb_0066D6C6
  bb_0066D6C6 -->|flow| bb_0066D6D0
```
