# Feature_2875967801__private_IsEnabledNoReportingNoInline

- RVA: `0x005C16CC`–`0x005C16FB` (길이 `47` bytes)
- VA: `0x00000001405C16CC`
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
- `0x005C16F0` → [Feature_2875967801__private_IsEnabledFallback](Feature_2875967801__private_IsEnabledFallback_function_005C16B0.md) (function, `0x005C16B0`)

### Direct callers
- [KiApplyProcessorErrata](KiApplyProcessorErrata_function_005C1704.md) at `0x005C17CD`

### Static image references
- `0x005C16D6` → RVA `0x00FC49E0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005C16CC  48 83 EC 28                     sub rsp, 0x28
005C16D0  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
005C16D6  8B 05 04 33 A0 00               mov eax, dword ptr [rip + 0xa03304]
005C16DC  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
005C16E0  A8 02                           test al, 2
005C16E2  74 05                           je 0x1405c16e9
005C16E4  83 E0 01                        and eax, 1
005C16E7  EB 0C                           jmp 0x1405c16f5
005C16E9  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
005C16EE  33 D2                           xor edx, edx
005C16F0  E8 BB FF FF FF                  call 0x1405c16b0
005C16F5  48 83 C4 28                     add rsp, 0x28
005C16F9  C3                              ret
005C16FA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_2875967801__private_IsEnabledNoReportingNoInline(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10498820)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10498820)))) & (2)) == 0) goto loc_005C16E9;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10498820))) & (1));
    goto loc_005C16F5;
loc_005C16E9:
    a2 = 0;
    result = Feature_2875967801__private_IsEnabledFallback(v_stack_p8, a2, a3, a4);
loc_005C16F5:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t Feature_2875967801__private_IsEnabledNoReportingNoInline(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA03304)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA03304)))) & (2)) == 0) goto loc_005C16E9;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA03304))) & (1));
    goto loc_005C16F5;
loc_005C16E9:
    Arg2 = 0;
    result = Feature_2875967801__private_IsEnabledFallback(v_stack_p8, Arg2, a3, a4);
loc_005C16F5:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005C16CC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005C16CC[BB_005C16CC]
  bb_005C16E4[BB_005C16E4]
  bb_005C16E9[BB_005C16E9]
  bb_005C16F5[BB_005C16F5]
  bb_005C16FA[BB_005C16FA]
  bb_005C16CC -->|branch| bb_005C16E9
  bb_005C16CC -->|fallthrough| bb_005C16E4
  bb_005C16E4 -->|branch| bb_005C16F5
  bb_005C16E9 -->|flow| bb_005C16F5
```
