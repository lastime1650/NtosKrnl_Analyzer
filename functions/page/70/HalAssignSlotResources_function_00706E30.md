# HalAssignSlotResources

- RVA: `0x00706E30`–`0x00706E8C` (길이 `92` bytes)
- VA: `0x0000000140706E30`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C2A4`
- 디코드: `19`개 명령, `92/92` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00706E7A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00706E51` → RVA `0x00E00830` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00706E7A` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00706E30  48 83 EC 58                     sub rsp, 0x58
00706E34  83 BC 24 80 00 00 00 05         cmp dword ptr [rsp + 0x80], 5
00706E3C  4D 8B D9                        mov r11, r9
00706E3F  75 40                           jne 0x140706e81
00706E41  4C 8B 94 24 98 00 00 00         mov r10, qword ptr [rsp + 0x98]
00706E49  44 8B 8C 24 88 00 00 00         mov r9d, dword ptr [rsp + 0x88]
00706E51  48 8B 05 D8 99 6F 00            mov rax, qword ptr [rip + 0x6f99d8]
00706E58  4C 89 54 24 38                  mov qword ptr [rsp + 0x38], r10
00706E5D  44 8B 94 24 90 00 00 00         mov r10d, dword ptr [rsp + 0x90]
00706E65  44 89 54 24 30                  mov dword ptr [rsp + 0x30], r10d
00706E6A  44 89 4C 24 28                  mov dword ptr [rsp + 0x28], r9d
00706E6F  4D 8B CB                        mov r9, r11
00706E72  C7 44 24 20 05 00 00 00         mov dword ptr [rsp + 0x20], 5
00706E7A  E8 51 3C FB FF                  call 0x1406baad0
00706E7F  EB 05                           jmp 0x140706e86
00706E81  B8 02 00 00 C0                  mov eax, 0xc0000002
00706E86  48 83 C4 58                     add rsp, 0x58
00706E8A  C3                              ret
00706E8B  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalAssignSlotResources(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6, unsigned int a7, __int64 a8)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m28;
    unsigned int v_stack_m30;
    unsigned int v_stack_m38;

    v_rsp = (v_rsp) - (88);
    if (a5 != 5) goto loc_00706E81;
    v_stack_m20 = a8;
    v_stack_m28 = (unsigned int)((unsigned int)(a7));
    v_stack_m30 = (unsigned int)((unsigned int)(a6));
    v_stack_m38 = 5;
    result = guard_dispatch_icall(a1, a2, a3, a4);
    goto loc_00706E86;
loc_00706E81:
loc_00706E86:
    v_rsp = (v_rsp) + (88);
    return (unsigned int)(0xC0000002ULL);
}
```

## 5. (Beta) C Style

```c
int64_t HalAssignSlotResources(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6, uint32_t Arg7, int64_t Arg8)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint32_t v_stack_m28;
    uint32_t v_stack_m30;
    uint32_t v_stack_m38;

    local_rsp = (local_rsp) - (88);
    if (Arg5 != 5) goto loc_00706E81;
    v_stack_m20 = Arg8;
    v_stack_m28 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m30 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m38 = 5;
    result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    goto loc_00706E86;
loc_00706E81:
loc_00706E86:
    local_rsp = (local_rsp) + (88);
    return (uint32_t)(0xC0000002ULL);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00706E30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00706E30[BB_00706E30]
  bb_00706E41[BB_00706E41]
  bb_00706E81[BB_00706E81]
  bb_00706E86[BB_00706E86]
  bb_00706E8B[BB_00706E8B]
  bb_00706E30 -->|branch| bb_00706E81
  bb_00706E30 -->|fallthrough| bb_00706E41
  bb_00706E41 -->|branch| bb_00706E86
  bb_00706E81 -->|flow| bb_00706E86
```
