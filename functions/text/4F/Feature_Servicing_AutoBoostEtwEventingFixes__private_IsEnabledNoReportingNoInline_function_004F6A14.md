# Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledNoReportingNoInline

- RVA: `0x004F6A14`–`0x004F6A43` (길이 `47` bytes)
- VA: `0x00000001404F6A14`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `47/47` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004F6A38` → [Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledFallback](Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledFallback_function_004F6A4C.md) (function, `0x004F6A4C`)

### Direct callers
- [EtwTraceAutoBoostEntryExhaustion](../21/EtwTraceAutoBoostEntryExhaustion_function_00210B04.md) at `0x00210B28`
- [Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledWithReporting](../22/Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledWithReporting_function_00222FF0.md) at `0x00223019`
- [EtwTraceAutoBoostClearFloor](../22/EtwTraceAutoBoostClearFloor_function_0022302C.md) at `0x00223058`

### Static image references
- `0x004F6A1E` → RVA `0x00FC4BD8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F6A14  48 83 EC 28                     sub rsp, 0x28
004F6A18  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004F6A1E  8B 05 B4 E1 AC 00               mov eax, dword ptr [rip + 0xace1b4]
004F6A24  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F6A28  A8 02                           test al, 2
004F6A2A  74 05                           je 0x1404f6a31
004F6A2C  83 E0 01                        and eax, 1
004F6A2F  EB 0C                           jmp 0x1404f6a3d
004F6A31  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004F6A36  33 D2                           xor edx, edx
004F6A38  E8 0F 00 00 00                  call 0x1404f6a4c
004F6A3D  48 83 C4 28                     add rsp, 0x28
004F6A41  C3                              ret
004F6A42  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledNoReportingNoInline(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11329972)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11329972)))) & (2)) == 0) goto loc_004F6A31;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11329972))) & (1));
    goto loc_004F6A3D;
loc_004F6A31:
    a2 = 0;
    result = Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledFallback(v_stack_p8, a2, a3, a4);
loc_004F6A3D:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledNoReportingNoInline(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACE1B4)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACE1B4)))) & (2)) == 0) goto loc_004F6A31;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xACE1B4))) & (1));
    goto loc_004F6A3D;
loc_004F6A31:
    Arg2 = 0;
    result = Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledFallback(v_stack_p8, Arg2, a3, a4);
loc_004F6A3D:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F6A14&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F6A14[BB_004F6A14]
  bb_004F6A2C[BB_004F6A2C]
  bb_004F6A31[BB_004F6A31]
  bb_004F6A3D[BB_004F6A3D]
  bb_004F6A42[BB_004F6A42]
  bb_004F6A14 -->|branch| bb_004F6A31
  bb_004F6A14 -->|fallthrough| bb_004F6A2C
  bb_004F6A2C -->|branch| bb_004F6A3D
  bb_004F6A31 -->|flow| bb_004F6A3D
```
