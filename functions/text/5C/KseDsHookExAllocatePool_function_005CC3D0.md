# KseDsHookExAllocatePool

- RVA: `0x005CC3D0`–`0x005CC422` (길이 `82` bytes)
- VA: `0x00000001405CC3D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000794E0`
- 디코드: `22`개 명령, `82/82` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005CC3EB` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x005CC409` → [KsepDsEventPoolAllocate](KsepDsEventPoolAllocate_function_005CD0D0.md) (function, `0x005CD0D0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x005CC3DF` → RVA `0x00E01608` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CC3D0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
005CC3D5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
005CC3DA  57                              push rdi
005CC3DB  48 83 EC 30                     sub rsp, 0x30
005CC3DF  48 8B 05 22 52 83 00            mov rax, qword ptr [rip + 0x835222]
005CC3E6  48 8B FA                        mov rdi, rdx
005CC3E9  8B F1                           mov esi, ecx
005CC3EB  E8 E0 E6 0E 00                  call 0x1406baad0
005CC3F0  48 8B 54 24 38                  mov rdx, qword ptr [rsp + 0x38]
005CC3F5  4C 8B CF                        mov r9, rdi
005CC3F8  44 8B C6                        mov r8d, esi
005CC3FB  C7 44 24 20 4E 6F 6E 65         mov dword ptr [rsp + 0x20], 0x656e6f4e
005CC403  48 8B C8                        mov rcx, rax
005CC406  48 8B D8                        mov rbx, rax
005CC409  E8 C2 0C 00 00                  call 0x1405cd0d0
005CC40E  48 8B 74 24 48                  mov rsi, qword ptr [rsp + 0x48]
005CC413  48 8B C3                        mov rax, rbx
005CC416  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
005CC41B  48 83 C4 30                     add rsp, 0x30
005CC41F  5F                              pop rdi
005CC420  C3                              ret
005CC421  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KseDsHookExAllocatePool(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (48);
    result = guard_dispatch_icall(a1, a2, a3, a4);
    v_stack_m18 = 0x656E6F4EULL;
    result = KsepDsEventPoolAllocate(result, v_stack_p0, (unsigned int)((unsigned int)((unsigned int)(a1))), a2);
    v_rsp = (v_rsp) + (48);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KseDsHookExAllocatePool(int32_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (48);
    result = guard_dispatch_icall(Arg1, Arg2, a3, a4);
    v_stack_m18 = 0x656E6F4EULL;
    result = KsepDsEventPoolAllocate(result, v_stack_p0, (uint32_t)((uint32_t)((uint32_t)(Arg1))), Arg2);
    local_rsp = (local_rsp) + (48);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CC3D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CC3D0[BB_005CC3D0]
  bb_005CC421[BB_005CC421]
```
