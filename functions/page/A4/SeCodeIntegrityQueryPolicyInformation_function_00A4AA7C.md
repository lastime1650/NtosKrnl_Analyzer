# SeCodeIntegrityQueryPolicyInformation

- RVA: `0x00A4AA7C`–`0x00A4AAB6` (길이 `58` bytes)
- VA: `0x0000000140A4AA7C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082E10`
- 디코드: `16`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A4AAA4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- [ExpQuerySystemInformation](../A5/ExpQuerySystemInformation_function_00A57858.md) at `0x00A5B709`

### Static image references
- `0x00A4AA80` → RVA `0x00F04EC8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A4AAA4` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A4AA7C  48 83 EC 48                     sub rsp, 0x48
00A4AA80  48 8B 05 41 A4 4B 00            mov rax, qword ptr [rip + 0x4ba441]
00A4AA87  44 8B D1                        mov r10d, ecx
00A4AA8A  48 85 C0                        test rax, rax
00A4AA8D  74 20                           je 0x140a4aaaf
00A4AA8F  48 8B 4C 24 78                  mov rcx, qword ptr [rsp + 0x78]
00A4AA94  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00A4AA99  8B 4C 24 70                     mov ecx, dword ptr [rsp + 0x70]
00A4AA9D  89 4C 24 20                     mov dword ptr [rsp + 0x20], ecx
00A4AAA1  41 8B CA                        mov ecx, r10d
00A4AAA4  E8 27 00 C7 FF                  call 0x1406baad0
00A4AAA9  48 83 C4 48                     add rsp, 0x48
00A4AAAD  C3                              ret
00A4AAAE  CC                              int3
00A4AAAF  B8 01 00 00 C0                  mov eax, 0xc0000001
00A4AAB4  EB F3                           jmp 0x140a4aaa9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SeCodeIntegrityQueryPolicyInformation(int a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, __int64 a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (72);
    if (*(unsigned __int64 *)(v_rip + 4957249) == 0) goto loc_00A4AAAF;
    v_stack_m20 = a6;
    v_stack_m28 = (unsigned int)((unsigned int)(a5));
    result = guard_dispatch_icall((unsigned int)((unsigned int)((unsigned int)(a1))), a2, a3, a4);
loc_00A4AAA9:
    v_rsp = (v_rsp) + (72);
    return result;
loc_00A4AAAF:
    goto loc_00A4AAA9;
}
```

## 5. (Beta) C Style

```c
int64_t SeCodeIntegrityQueryPolicyInformation(int32_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m20;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    if (*(uint64_t *)(v_rip + 0x4BA441) == 0) goto loc_00A4AAAF;
    v_stack_m20 = Arg6;
    v_stack_m28 = (uint32_t)((uint32_t)(Arg5));
    result = guard_dispatch_icall((uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg2, Arg3, Arg4);
loc_00A4AAA9:
    local_rsp = (local_rsp) + (72);
    return result;
loc_00A4AAAF:
    goto loc_00A4AAA9;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A4AA7C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A4AA7C[BB_00A4AA7C]
  bb_00A4AA8F[BB_00A4AA8F]
  bb_00A4AAA9[BB_00A4AAA9]
  bb_00A4AAAE[BB_00A4AAAE]
  bb_00A4AAAF[BB_00A4AAAF]
  bb_00A4AA7C -->|branch| bb_00A4AAAF
  bb_00A4AA7C -->|fallthrough| bb_00A4AA8F
  bb_00A4AA8F -->|flow| bb_00A4AAA9
  bb_00A4AAAE -->|flow| bb_00A4AAAF
  bb_00A4AAAF -->|branch| bb_00A4AAA9
```
