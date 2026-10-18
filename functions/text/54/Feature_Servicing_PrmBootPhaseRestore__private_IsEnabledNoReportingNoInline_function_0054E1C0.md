# Feature_Servicing_PrmBootPhaseRestore__private_IsEnabledNoReportingNoInline

- RVA: `0x0054E1C0`–`0x0054E1EF` (길이 `47` bytes)
- VA: `0x000000014054E1C0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0054E1E4` → [Feature_Servicing_PrmBootPhaseRestore__private_IsEnabledFallback](Feature_Servicing_PrmBootPhaseRestore__private_IsEnabledFallback_function_0054E1A4.md) (function, `0x0054E1A4`)

### Direct callers
- [HaliLocateHiberRanges](../../pagelk/B5/HaliLocateHiberRanges_function_00B5CE50.md) at `0x00B5CF1A`
- [HaliLocateHiberRanges](../../pagelk/B5/HaliLocateHiberRanges_function_00B5CE50.md) at `0x00B5D066`

### Static image references
- `0x0054E1CA` → RVA `0x00FC46E8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0054E1C0  48 83 EC 28                     sub rsp, 0x28
0054E1C4  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0054E1CA  8B 05 18 65 A7 00               mov eax, dword ptr [rip + 0xa76518]
0054E1D0  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0054E1D4  A8 02                           test al, 2
0054E1D6  74 05                           je 0x14054e1dd
0054E1D8  83 E0 01                        and eax, 1
0054E1DB  EB 0C                           jmp 0x14054e1e9
0054E1DD  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0054E1E2  33 D2                           xor edx, edx
0054E1E4  E8 BB FF FF FF                  call 0x14054e1a4
0054E1E9  48 83 C4 28                     add rsp, 0x28
0054E1ED  C3                              ret
0054E1EE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Servicing_PrmBootPhaseRestore__private_IsEnabledNoReportingNoInline(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10970392)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10970392)))) & (2)) == 0) goto loc_0054E1DD;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10970392))) & (1));
    goto loc_0054E1E9;
loc_0054E1DD:
    a2 = 0;
    result = Feature_Servicing_PrmBootPhaseRestore__private_IsEnabledFallback(v_stack_p8, a2, a3, a4);
loc_0054E1E9:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Feature_Servicing_PrmBootPhaseRestore__private_IsEnabledNoReportingNoInline(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA76518)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA76518)))) & (2)) == 0) goto loc_0054E1DD;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA76518))) & (1));
    goto loc_0054E1E9;
loc_0054E1DD:
    Arg2 = 0;
    result = Feature_Servicing_PrmBootPhaseRestore__private_IsEnabledFallback(v_stack_p8, Arg2, a3, a4);
loc_0054E1E9:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0054E1C0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0054E1C0[BB_0054E1C0]
  bb_0054E1D8[BB_0054E1D8]
  bb_0054E1DD[BB_0054E1DD]
  bb_0054E1E9[BB_0054E1E9]
  bb_0054E1EE[BB_0054E1EE]
  bb_0054E1C0 -->|branch| bb_0054E1DD
  bb_0054E1C0 -->|fallthrough| bb_0054E1D8
  bb_0054E1D8 -->|branch| bb_0054E1E9
  bb_0054E1DD -->|flow| bb_0054E1E9
```
