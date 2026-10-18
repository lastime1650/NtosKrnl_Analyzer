# Feature_SuspendThread2__private_IsEnabledOtherReporting

- RVA: `0x005E3430`–`0x005E3462` (길이 `50` bytes)
- VA: `0x00000001405E3430`
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
- `0x005E3457` → [Feature_SuspendThread2__private_IsEnabledFallback](../5C/Feature_SuspendThread2__private_IsEnabledFallback_function_005C3560.md) (function, `0x005C3560`)

### Direct callers
- [NtChangeThreadState](../../page/AE/NtChangeThreadState_function_00AEA210.md) at `0x00AEA390`

### Static image references
- `0x005E343A` → RVA `0x00FC48C0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005E3430  48 83 EC 28                     sub rsp, 0x28
005E3434  48 83 64 24 38 00               and qword ptr [rsp + 0x38], 0
005E343A  8B 05 80 14 9E 00               mov eax, dword ptr [rip + 0x9e1480]
005E3440  89 44 24 38                     mov dword ptr [rsp + 0x38], eax
005E3444  A8 02                           test al, 2
005E3446  74 05                           je 0x1405e344d
005E3448  83 E0 01                        and eax, 1
005E344B  EB 0F                           jmp 0x1405e345c
005E344D  48 8B 4C 24 38                  mov rcx, qword ptr [rsp + 0x38]
005E3452  BA 01 00 00 00                  mov edx, 1
005E3457  E8 04 01 FE FF                  call 0x1405c3560
005E345C  48 83 C4 28                     add rsp, 0x28
005E3460  C3                              ret
005E3461  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_SuspendThread2__private_IsEnabledOtherReporting(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;

    v_rsp = (v_rsp) - (40);
    v_stack_p10 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10359936)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10359936)))) & (2)) == 0) goto loc_005E344D;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10359936))) & (1));
    goto loc_005E345C;
loc_005E344D:
    result = Feature_SuspendThread2__private_IsEnabledFallback(v_stack_p10, 1, a3, a4);
loc_005E345C:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_SuspendThread2__private_IsEnabledOtherReporting(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;

    local_rsp = (local_rsp) - (40);
    v_stack_p10 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9E1480)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9E1480)))) & (2)) == 0) goto loc_005E344D;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9E1480))) & (1));
    goto loc_005E345C;
loc_005E344D:
    result = Feature_SuspendThread2__private_IsEnabledFallback(v_stack_p10, 1, a3, a4);
loc_005E345C:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005E3430&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005E3430[BB_005E3430]
  bb_005E3448[BB_005E3448]
  bb_005E344D[BB_005E344D]
  bb_005E345C[BB_005E345C]
  bb_005E3461[BB_005E3461]
  bb_005E3430 -->|branch| bb_005E344D
  bb_005E3430 -->|fallthrough| bb_005E3448
  bb_005E3448 -->|branch| bb_005E345C
  bb_005E344D -->|flow| bb_005E345C
```
