# Feature_PpmDynamicHintAdjust__private_IsEnabledNoReportingNoInline

- RVA: `0x004FC610`–`0x004FC63F` (길이 `47` bytes)
- VA: `0x00000001404FC610`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004FC634` → [Feature_PpmDynamicHintAdjust__private_IsEnabledFallback](Feature_PpmDynamicHintAdjust__private_IsEnabledFallback_function_004FC210.md) (function, `0x004FC210`)

### Direct callers
- [PpmIdleSelectStates](../2C/PpmIdleSelectStates_function_002CFFE8.md) at `0x002D011E`
- [PpmEstimateIdleDuration](../4C/PpmEstimateIdleDuration_function_004C79DC.md) at `0x004C7B18`
- [PpmEstimateIdleDuration](../4C/PpmEstimateIdleDuration_function_004C79DC.md) at `0x004C7BA1`

### Static image references
- `0x004FC61A` → RVA `0x00FC4990` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FC610  48 83 EC 28                     sub rsp, 0x28
004FC614  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004FC61A  8B 05 70 83 AC 00               mov eax, dword ptr [rip + 0xac8370]
004FC620  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004FC624  A8 02                           test al, 2
004FC626  74 05                           je 0x1404fc62d
004FC628  83 E0 01                        and eax, 1
004FC62B  EB 0C                           jmp 0x1404fc639
004FC62D  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004FC632  33 D2                           xor edx, edx
004FC634  E8 D7 FB FF FF                  call 0x1404fc210
004FC639  48 83 C4 28                     add rsp, 0x28
004FC63D  C3                              ret
004FC63E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_PpmDynamicHintAdjust__private_IsEnabledNoReportingNoInline(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11305840)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11305840)))) & (2)) == 0) goto loc_004FC62D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11305840))) & (1));
    goto loc_004FC639;
loc_004FC62D:
    a2 = 0;
    result = Feature_PpmDynamicHintAdjust__private_IsEnabledFallback(v_stack_p8, a2, a3, a4);
loc_004FC639:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Feature_PpmDynamicHintAdjust__private_IsEnabledNoReportingNoInline(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAC8370)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAC8370)))) & (2)) == 0) goto loc_004FC62D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xAC8370))) & (1));
    goto loc_004FC639;
loc_004FC62D:
    Arg2 = 0;
    result = Feature_PpmDynamicHintAdjust__private_IsEnabledFallback(v_stack_p8, Arg2, a3, a4);
loc_004FC639:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FC610&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FC610[BB_004FC610]
  bb_004FC628[BB_004FC628]
  bb_004FC62D[BB_004FC62D]
  bb_004FC639[BB_004FC639]
  bb_004FC63E[BB_004FC63E]
  bb_004FC610 -->|branch| bb_004FC62D
  bb_004FC610 -->|fallthrough| bb_004FC628
  bb_004FC628 -->|branch| bb_004FC639
  bb_004FC62D -->|flow| bb_004FC639
```
