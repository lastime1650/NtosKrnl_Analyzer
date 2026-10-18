# SepFilterPrivilegeAudits

- RVA: `0x00974F90`–`0x00974FB9` (길이 `41` bytes)
- VA: `0x0000000140974F90`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000964D8`
- 디코드: `16`개 명령, `41/41` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SepAdtPrivilegeObjectAuditAlarm](../86/SepAdtPrivilegeObjectAuditAlarm_function_0086E3F0.md) at `0x0086E4D3`
- [SepAdtAuditPrivilegeUseWithContext](../87/SepAdtAuditPrivilegeUseWithContext_function_00870BD0.md) at `0x00870C54`
- [SepAdtPrivilegedServiceAuditAlarm](../87/SepAdtPrivilegedServiceAuditAlarm_function_008714F0.md) at `0x008715E7`
- [SeCheckAuditPrivilege](SeCheckAuditPrivilege_function_00974E48.md) at `0x00974F6E`

### Static image references
- `0x00974F96` → RVA `0x00FD8238` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00974F90  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
00974F95  57                              push rdi
00974F96  4C 8B 1D 9B 32 66 00            mov r11, qword ptr [rip + 0x66329b]
00974F9D  33 DB                           xor ebx, ebx
00974F9F  4C 8B C2                        mov r8, rdx
00974FA2  8B F9                           mov edi, ecx
00974FA4  48 85 D2                        test rdx, rdx
00974FA7  75 0A                           jne 0x140974fb3
00974FA9  32 C0                           xor al, al
00974FAB  48 8B 5C 24 20                  mov rbx, qword ptr [rsp + 0x20]
00974FB0  5F                              pop rdi
00974FB1  C3                              ret
00974FB2  CC                              int3
00974FB3  8B 02                           mov eax, dword ptr [rdx]
00974FB5  85 C0                           test eax, eax
00974FB7  74 F0                           je 0x140974fa9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepFilterPrivilegeAudits(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_rbx;
    unsigned __int64 v_stack_p18;

    v_stack_p18 = v_rbx;
    v_rbx = 0;
    if (a2 != 0) goto loc_00974FB3;
loc_00974FA9:
    result = 0;
    return result;
loc_00974FB3:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a2))) == 0) goto loc_00974FA9;
}
```

## 5. (Beta) C Style

```c
int64_t SepFilterPrivilegeAudits(int32_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rbx;
    uint64_t v_stack_p18;

    v_stack_p18 = local_rbx;
    local_rbx = 0;
    if (Arg2 != 0) goto loc_00974FB3;
loc_00974FA9:
    result = 0;
    return result;
loc_00974FB3:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(Arg2))) == 0) goto loc_00974FA9;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00974F90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00974F90[BB_00974F90]
  bb_00974FA9[BB_00974FA9]
  bb_00974FB2[BB_00974FB2]
  bb_00974FB3[BB_00974FB3]
  bb_00974F90 -->|branch| bb_00974FB3
  bb_00974F90 -->|fallthrough| bb_00974FA9
  bb_00974FB2 -->|flow| bb_00974FB3
  bb_00974FB3 -->|branch| bb_00974FA9
```
