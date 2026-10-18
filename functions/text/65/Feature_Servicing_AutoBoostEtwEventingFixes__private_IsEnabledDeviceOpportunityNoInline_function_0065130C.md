# Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledDeviceOpportunityNoInline

- RVA: `0x0065130C`–`0x0065133E` (길이 `50` bytes)
- VA: `0x000000014065130C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00651333` → [Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledFallback](../4F/Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledFallback_function_004F6A4C.md) (function, `0x004F6A4C`)

### Direct callers
- [Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledWithReporting](../22/Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledWithReporting_function_00222FF0.md) at `0x0022300B`

### Static image references
- `0x00651316` → RVA `0x00FC4BD8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0065130C  48 83 EC 28                     sub rsp, 0x28
00651310  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00651316  8B 05 BC 38 97 00               mov eax, dword ptr [rip + 0x9738bc]
0065131C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00651320  A8 20                           test al, 0x20
00651322  74 05                           je 0x140651329
00651324  83 E0 01                        and eax, 1
00651327  EB 0F                           jmp 0x140651338
00651329  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0065132E  BA 04 00 00 00                  mov edx, 4
00651333  E8 14 57 EA FF                  call 0x1404f6a4c
00651338  48 83 C4 28                     add rsp, 0x28
0065133C  C3                              ret
0065133D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledDeviceOpportunityNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9910460)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9910460)))) & (32)) == 0) goto loc_00651329;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9910460))) & (1));
    goto loc_00651338;
loc_00651329:
    result = Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledFallback(v_stack_p8, 4, a3, a4);
loc_00651338:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledDeviceOpportunityNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9738BC)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9738BC)))) & (32)) == 0) goto loc_00651329;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9738BC))) & (1));
    goto loc_00651338;
loc_00651329:
    result = Feature_Servicing_AutoBoostEtwEventingFixes__private_IsEnabledFallback(v_stack_p8, 4, a3, a4);
loc_00651338:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0065130C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0065130C[BB_0065130C]
  bb_00651324[BB_00651324]
  bb_00651329[BB_00651329]
  bb_00651338[BB_00651338]
  bb_0065133D[BB_0065133D]
  bb_0065130C -->|branch| bb_00651329
  bb_0065130C -->|fallthrough| bb_00651324
  bb_00651324 -->|branch| bb_00651338
  bb_00651329 -->|flow| bb_00651338
```
