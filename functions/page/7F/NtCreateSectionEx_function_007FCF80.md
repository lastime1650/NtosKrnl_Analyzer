# NtCreateSectionEx

- RVA: `0x007FCF80`–`0x007FCFE4` (길이 `100` bytes)
- VA: `0x00000001407FCF80`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006E590`
- 디코드: `19`개 명령, `100/100` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007FCFD9` → [MiCreateSectionCommon](../8A/MiCreateSectionCommon_function_008A9AA4.md) (function, `0x008A9AA4`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007FCF80  48 83 EC 68                     sub rsp, 0x68
007FCF84  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
007FCF8D  44 8A 90 32 02 00 00            mov r10b, byte ptr [rax + 0x232]
007FCF94  8B 84 24 B0 00 00 00            mov eax, dword ptr [rsp + 0xb0]
007FCF9B  44 88 54 24 50                  mov byte ptr [rsp + 0x50], r10b
007FCFA0  83 64 24 48 00                  and dword ptr [rsp + 0x48], 0
007FCFA5  89 44 24 40                     mov dword ptr [rsp + 0x40], eax
007FCFA9  48 8B 84 24 A8 00 00 00         mov rax, qword ptr [rsp + 0xa8]
007FCFB1  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
007FCFB6  48 8B 84 24 A0 00 00 00         mov rax, qword ptr [rsp + 0xa0]
007FCFBE  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
007FCFC3  8B 84 24 98 00 00 00            mov eax, dword ptr [rsp + 0x98]
007FCFCA  89 44 24 28                     mov dword ptr [rsp + 0x28], eax
007FCFCE  8B 84 24 90 00 00 00            mov eax, dword ptr [rsp + 0x90]
007FCFD5  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
007FCFD9  E8 C6 CA 0A 00                  call 0x1408a9aa4
007FCFDE  48 83 C4 68                     add rsp, 0x68
007FCFE2  C3                              ret
007FCFE3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtCreateSectionEx(__int64 a1, __int64 a2, __int64 a3, __int64 a4, unsigned int a5, unsigned int a6, __int64 a7, __int64 a8, unsigned int a9)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_m18;
    unsigned int v_stack_m20;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned int v_stack_m40;
    unsigned int v_stack_m48;

    v_rsp = (v_rsp) - (104);
    v_stack_m18 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    v_stack_m28 = (unsigned int)((unsigned int)(a9));
    v_stack_m30 = a8;
    v_stack_m38 = a7;
    v_stack_m40 = (unsigned int)((unsigned int)(a6));
    v_stack_m48 = (unsigned int)((unsigned int)(a5));
    result = MiCreateSectionCommon(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (104);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t NtCreateSectionEx(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint32_t Arg5, uint32_t Arg6, int64_t Arg7, int64_t Arg8, uint32_t Arg9)
{
    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_m18;
    uint32_t v_stack_m20;
    uint32_t v_stack_m28;
    uint64_t v_stack_m30;
    uint64_t v_stack_m38;
    uint32_t v_stack_m40;
    uint32_t v_stack_m48;

    local_rsp = (local_rsp) - (104);
    v_stack_m18 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    v_stack_m28 = (uint32_t)((uint32_t)(Arg9));
    v_stack_m30 = Arg8;
    v_stack_m38 = Arg7;
    v_stack_m40 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m48 = (uint32_t)((uint32_t)(Arg5));
    result = MiCreateSectionCommon(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (104);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007FCF80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007FCF80[BB_007FCF80]
  bb_007FCFE3[BB_007FCFE3]
```
